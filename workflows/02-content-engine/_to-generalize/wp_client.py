#!/usr/bin/env python3
"""Shared WordPress REST client for the testlify-content-refresh skill.

This module wraps the testlify.com WordPress REST API and the RankMath SEO
API. It is importable by the other skill scripts and also exposes a small CLI
for ad-hoc operations.

SECURITY
--------
Credentials are NEVER hardcoded. They are loaded at runtime from
``~/.testlify-wp-credentials``, a two-line file:

    WP_USERNAME=your-wp-user@example.com
    WP_APP_PASSWORD=xxxx xxxx xxxx xxxx xxxx xxxx

The username and the WordPress application password are base64-encoded
(``user:password``) into a Basic Authorization header at request time.

CLOUDFLARE
----------
testlify.com sits behind Cloudflare, which returns 403 to "default" clients.
Every request therefore carries a full set of browser-like headers
(Authorization, Content-Type, User-Agent, Accept, Origin, Referer). See
``auth_headers``.

SAFETY
------
``update_post`` and ``update_rankmath`` default to ``dry_run=True``. In dry-run
mode they print the exact payload and endpoint and send nothing. A real write
only happens when the caller passes ``dry_run=False`` explicitly. This mirrors
the skill's HARD-NEVER rules around touching production content.

CLI examples
------------
    python wp_client.py get-post 1234
    python wp_client.py search "candidate screening"
    python wp_client.py backup 1234 ./backups
    python wp_client.py verify-url https://testlify.com/candidate-screening/
    python wp_client.py update-post 1234 --content-file new.html          # dry-run
    python wp_client.py update-post 1234 --content-file new.html --execute # live
"""

import argparse
import base64
import datetime
import json
import pathlib
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

API_BASE = "https://testlify.com/wp-json/wp/v2/"
RANKMATH_ENDPOINT = "https://testlify.com/wp-json/rankmath/v1/updateMeta"
CREDENTIALS_PATH = pathlib.Path.home() / ".testlify-wp-credentials"

# A real Chrome UA string. Cloudflare rejects requests without one.
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)


class WPClientError(Exception):
    """Raised for any client-level failure with a human-readable message."""


def load_creds():
    """Load WP_USERNAME and WP_APP_PASSWORD from ~/.testlify-wp-credentials.

    Returns a (username, app_password) tuple. Raises WPClientError with a
    clear remediation message if the file is missing or malformed.

    Cloud-ready: env vars WP_USERNAME + WP_APP_PASSWORD take precedence over the
    local file (so the same code runs in a cloud environment with secrets set).
    """
    import os
    env_u, env_p = os.environ.get("WP_USERNAME"), os.environ.get("WP_APP_PASSWORD")
    if env_u and env_p:
        return env_u.strip(), env_p.strip()
    if not CREDENTIALS_PATH.exists():
        raise WPClientError(
            f"Credentials file not found: {CREDENTIALS_PATH}\n"
            "Create it with two lines:\n"
            "  WP_USERNAME=your-wp-user@example.com\n"
            "  WP_APP_PASSWORD=xxxx xxxx xxxx xxxx xxxx xxxx"
        )
    cfg = dict(
        line.split("=", 1)
        for line in CREDENTIALS_PATH.read_text().splitlines()
        if "=" in line
    )
    username = cfg.get("WP_USERNAME", "").strip()
    password = cfg.get("WP_APP_PASSWORD", "").strip()
    if not username or not password:
        raise WPClientError(
            f"{CREDENTIALS_PATH} must contain non-empty WP_USERNAME and "
            "WP_APP_PASSWORD lines."
        )
    return username, password


def auth_headers(extra=None):
    """Return the full header set required for every testlify.com API call.

    Pass ``extra`` to override or add headers (e.g. media upload headers).
    """
    username, password = load_creds()
    token = base64.b64encode(f"{username}:{password}".encode()).decode()
    headers = {
        "Authorization": f"Basic {token}",
        "Content-Type": "application/json",
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
        "Origin": "https://testlify.com",
        "Referer": "https://testlify.com/wp-admin/",
    }
    if extra:
        headers.update(extra)
    return headers


def _request(url, data=None, method="GET", headers=None):
    """Low-level request helper. Returns parsed JSON (or raw text fallback)."""
    headers = headers or auth_headers()
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            body = resp.read()
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:1000]
        raise WPClientError(
            f"HTTP {exc.code} from {method} {url}\n{detail}"
        ) from exc
    except urllib.error.URLError as exc:
        raise WPClientError(f"Network error for {method} {url}: {exc.reason}") from exc
    if not body:
        return {}
    try:
        return json.loads(body)
    except json.JSONDecodeError:
        return {"_raw": body.decode("utf-8", "replace")}


def get_post(post_id, context="edit"):
    """Fetch a single post. context='edit' returns raw Gutenberg blocks."""
    url = f"{API_BASE}posts/{post_id}?context={urllib.parse.quote(context)}"
    return _request(url)


def search_posts(keyword):
    """Search posts by keyword. Returns a list of post objects (edit context)."""
    q = urllib.parse.urlencode(
        {"search": keyword, "per_page": 10, "context": "edit"}
    )
    return _request(f"{API_BASE}posts?{q}")


def get_media():
    """List media items (most recent first)."""
    q = urllib.parse.urlencode({"per_page": 20, "orderby": "date", "order": "desc"})
    return _request(f"{API_BASE}media?{q}")


def backup_post(post_id, dir):
    """Fetch the post and write it to <dir>/<id>-<ts>.json. Returns the path."""
    post = get_post(post_id, context="edit")
    out_dir = pathlib.Path(dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
    out_path = out_dir / f"{post_id}-{ts}.json"
    out_path.write_text(json.dumps(post, indent=2, ensure_ascii=False))
    return out_path


def update_post(post_id, content, title=None, dry_run=True):
    """Update a post's content (and optionally title). DRY-RUN BY DEFAULT.

    With dry_run=True (default) this prints the endpoint and payload and sends
    NOTHING. A live POST happens only when dry_run=False is passed explicitly.
    """
    url = f"{API_BASE}posts/{post_id}"
    payload = {"content": content}
    if title:
        payload["title"] = title
    if dry_run:
        print("[DRY-RUN] would POST to:", url)
        print("[DRY-RUN] payload:")
        print(json.dumps(payload, indent=2, ensure_ascii=False)[:4000])
        return {"dry_run": True, "url": url}
    data = json.dumps(payload).encode()
    headers = auth_headers({"Cache-Control": "no-cache"})
    return _request(url, data=data, method="POST", headers=headers)


def update_rankmath(post_id, title, description, focus_keyword, dry_run=True):
    """Update RankMath SEO meta. DRY-RUN BY DEFAULT.

    RankMath does not update from the posts endpoint. This is a separate POST.
    With dry_run=True (default) it prints the payload and sends nothing.
    """
    # VERIFIED CONTRACT (2026-06-16 live deploy): fields nest inside `meta`
    # with rank_math_ keys. Flat {title,description,focusKeyword} returns
    # HTTP 400 rest_missing_callback_param: meta.
    payload = {
        "objectID": post_id,
        "objectType": "post",
        "meta": {
            "rank_math_title": title,
            "rank_math_description": description,
            "rank_math_focus_keyword": focus_keyword,
            "rank_math_pillar_content": "on",
        },
    }
    if dry_run:
        print("[DRY-RUN] would POST to:", RANKMATH_ENDPOINT)
        print("[DRY-RUN] payload:")
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return {"dry_run": True, "url": RANKMATH_ENDPOINT}
    data = json.dumps(payload).encode()
    return _request(RANKMATH_ENDPOINT, data=data, method="POST")


def upload_media(path):
    """Upload a .webp or .pdf file to the media library. Returns the API JSON.

    Sets Content-Type and Content-Disposition based on the file extension.
    This is a real write (no dry-run) because it adds a new asset rather than
    overwriting existing post content.
    """
    p = pathlib.Path(path)
    if not p.exists():
        raise WPClientError(f"File not found: {p}")
    ext = p.suffix.lower()
    content_types = {".webp": "image/webp", ".pdf": "application/pdf"}
    if ext not in content_types:
        raise WPClientError(
            f"Unsupported media type '{ext}'. Only .webp and .pdf are allowed."
        )
    data = p.read_bytes()
    headers = auth_headers(
        {
            "Content-Type": content_types[ext],
            "Content-Disposition": f'attachment; filename="{p.name}"',
        }
    )
    return _request(f"{API_BASE}media", data=data, method="POST", headers=headers)


def verify_url_200(url, timeout=10):
    """Return True if ``url`` resolves to a live page (final 2xx/3xx after redirects).

    Uses ``curl -sILo /dev/null -w %{http_code}`` so redirects are FOLLOWED and the
    FINAL status code is read - a plain ``-sI`` returns the first 301/302 line and
    yields false FAILs on the http->https / trailing-slash redirects that are
    ubiquitous on the open web. Accepts 2xx and 3xx; only 4xx/5xx (or curl error)
    count as dead. Never raises.
    """
    def _code(head):
        flags = ["-sIL"] if head else ["-sL"]
        try:
            r = subprocess.run(
                ["curl", *flags, "-o", "/dev/null", "-w", "%{http_code}",
                 "-A", USER_AGENT, url],
                capture_output=True, text=True, timeout=timeout,
            )
        except (subprocess.TimeoutExpired, FileNotFoundError) as exc:
            print(f"[WARN] curl failed for {url}: {exc}", file=sys.stderr)
            return None
        c = (r.stdout or "").strip()[-3:]
        return int(c) if c.isdigit() else None

    code = _code(head=True)
    # Many origins/CDNs 403/405 a HEAD even with a browser UA; fall back to GET.
    if code in (403, 405, 400) or code is None:
        code = _code(head=False)
    return code is not None and 200 <= code < 400


def fetch_rendered(url):
    """Return the rendered HTML of a public page via curl, or "" on failure.

    Used by verify_post.py's render-time checks (meta title/description, page
    H1, Gutenberg render integrity). This is the page as Google + a reader see
    it, NOT the post.content.raw Gutenberg source. Read-only, never raises.
    """
    try:
        result = subprocess.run(
            ["curl", "-sL", "-A", USER_AGENT, url],
            capture_output=True,
            text=True,
            timeout=45,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError) as exc:
        print(f"[WARN] curl failed for {url}: {exc}", file=sys.stderr)
        return ""
    return result.stdout or ""


def _build_parser():
    parser = argparse.ArgumentParser(
        description="Testlify WordPress REST client CLI."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("get-post", help="Fetch a post (edit context)")
    p.add_argument("post_id", type=int)
    p.add_argument("--context", default="edit")

    p = sub.add_parser("search", help="Search posts by keyword")
    p.add_argument("keyword")

    sub.add_parser("media", help="List recent media")

    p = sub.add_parser("backup", help="Backup a post to <dir>/<id>-<ts>.json")
    p.add_argument("post_id", type=int)
    p.add_argument("dir")

    p = sub.add_parser("verify-url", help="Check a URL returns 200")
    p.add_argument("url")

    p = sub.add_parser("upload-media", help="Upload a .webp or .pdf file")
    p.add_argument("path")

    p = sub.add_parser("update-post", help="Update post content (dry-run default)")
    p.add_argument("post_id", type=int)
    p.add_argument("--content-file", required=True)
    p.add_argument("--title", default=None, help="Optional post title to update")
    p.add_argument(
        "--execute",
        action="store_true",
        help="Actually send the write. Omit for dry-run.",
    )

    p = sub.add_parser(
        "update-rankmath", help="Update RankMath meta (dry-run default)"
    )
    p.add_argument("post_id", type=int)
    p.add_argument("--title", required=True)
    p.add_argument("--description", required=True)
    p.add_argument("--focus-keyword", required=True)
    p.add_argument("--execute", action="store_true")

    return parser


def main(argv=None):
    args = _build_parser().parse_args(argv)
    try:
        if args.command == "get-post":
            print(json.dumps(get_post(args.post_id, args.context), indent=2,
                             ensure_ascii=False))
        elif args.command == "search":
            posts = search_posts(args.keyword)
            for post in posts if isinstance(posts, list) else []:
                print(post.get("id"), "-",
                      post.get("title", {}).get("raw", ""),
                      "-", post.get("link", ""))
        elif args.command == "media":
            print(json.dumps(get_media(), indent=2, ensure_ascii=False))
        elif args.command == "backup":
            print("Backup written:", backup_post(args.post_id, args.dir))
        elif args.command == "verify-url":
            ok = verify_url_200(args.url)
            print("200 OK" if ok else "NOT 200")
            return 0 if ok else 1
        elif args.command == "upload-media":
            print(json.dumps(upload_media(args.path), indent=2, ensure_ascii=False))
        elif args.command == "update-post":
            content = pathlib.Path(args.content_file).read_text()
            update_post(args.post_id, content, title=getattr(args, "title", None), dry_run=not args.execute)
        elif args.command == "update-rankmath":
            update_rankmath(
                args.post_id, args.title, args.description,
                args.focus_keyword, dry_run=not args.execute,
            )
    except WPClientError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())

