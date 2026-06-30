#!/usr/bin/env python3
"""
Build a content database for a WordPress site via its REST API.
Pulls URL + type + title + description (excerpt) for each content type,
then joins traffic/keywords/intent from a Semrush "Pages" CSV export.

Usage: build_content_database.py <site_base> <semrush_csv> <out_csv>
  site_base : e.g. https://example.com
Generic recipe lives in ../../content-database.workflow.md
"""
import csv, json, re, sys, time, html, urllib.request, urllib.error, glob
from concurrent.futures import ThreadPoolExecutor

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# English/core content types to include (skip translated libs + technical types)
TYPES = ["posts", "pages", "test-library", "hr-glossary", "techglossary",
         "job-description", "interviews", "competitors", "integrations",
         "successstory", "certifications", "ebooks", "podcast",
         "job-openings", "our-partner", "skill-mapping", "press-release"]

def strip_html(s):
    if not s:
        return ""
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()

# Content types whose body is page-builder / custom-template rendered, so WP REST `content`
# comes back EMPTY — these need the live-HTML fallback (the 2026-06 test-library gap).
FALLBACK_TYPES = {"test-library", "interviews", "competitors", "integrations",
                  "successstory", "certifications", "skill-mapping"}
MIN_BODY_CHARS = 400   # below this a recovered page is a genuine stub; leave it empty

def extract_visible(h):
    """Strip chrome + tags from a live HTML page → visible text."""
    for tag in ("script", "style", "nav", "footer", "header", "form", "aside", "svg", "noscript"):
        h = re.sub(rf"<{tag}[^>]*>.*?</{tag}>", " ", h, flags=re.S | re.I)
    h = re.sub(r"<!--.*?-->", " ", h, flags=re.S)
    h = re.sub(r"<[^>]+>", " ", h)
    h = html.unescape(h)
    h = re.sub(r"\s+", " ", h).strip()
    i = h.lower().find("skip to content")
    if 0 <= i < 200:
        h = h[i + 15:].strip()
    return h

def fetch_html(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode("utf-8", "ignore")
        except urllib.error.HTTPError as e:
            if e.code in (404, 410):
                return ""
            time.sleep(1.0 * (attempt + 1))
        except Exception:
            time.sleep(1.0 * (attempt + 1))
    return ""

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 400:   # past last page
                return None
            time.sleep(1)
        except Exception:
            time.sleep(1)
    return None

def main():
    base, semrush_csv, out_csv = sys.argv[1], sys.argv[2], sys.argv[3]
    api = base.rstrip("/") + "/wp-json/wp/v2"

    # 1) pull pages from WP REST
    rows, per_type = [], {}
    for t in TYPES:
        page, n = 1, 0
        while True:
            url = f"{api}/{t}?per_page=100&page={page}&_fields=link,type,title,excerpt,content"
            data = fetch(url)
            if not data:
                break
            for it in data:
                rows.append({
                    "url": it.get("link", ""),
                    "type": t,
                    "title": strip_html((it.get("title") or {}).get("rendered", "")),
                    "description": strip_html((it.get("excerpt") or {}).get("rendered", "")),
                    "full_content": strip_html((it.get("content") or {}).get("rendered", "")),
                })
                n += 1
            if len(data) < 100:
                break
            page += 1
            time.sleep(0.15)
        per_type[t] = n
        print(f"  {t}: {n}", file=sys.stderr)

    # 1b) LIVE-HTML FALLBACK — WP REST `content` is empty for page-builder/custom-template
    # post types (test-library, interviews, …). Fetch the live page and extract visible text
    # for any content-bearing row that came back empty. Parallel → minutes, not hours.
    empties = [r for r in rows if not r["full_content"].strip() and r["type"] in FALLBACK_TYPES]
    print(f"  live-HTML fallback: {len(empties)} empty content-bearing pages to recover", file=sys.stderr)
    def _recover(r):
        txt = extract_visible(fetch_html(r["url"]))
        if len(txt) >= MIN_BODY_CHARS:
            r["full_content"] = txt
            return 1
        return 0
    recovered = 0
    if empties:
        with ThreadPoolExecutor(max_workers=16) as ex:
            recovered = sum(ex.map(_recover, empties))
    print(f"  fallback recovered {recovered}/{len(empties)} (rest are genuine stubs)", file=sys.stderr)

    # 2) load Semrush traffic map (proper CSV parse handles quoted fields)
    sem = {}
    files = [semrush_csv] if semrush_csv != "auto" else glob.glob(
        f"{base.rstrip('/').split('//')[-1]}*Pages*.csv")
    try:
        with open(semrush_csv, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                key = (row.get("URL") or "").rstrip("/")
                sem[key] = (row.get("Traffic", ""), row.get("Number of Keywords", ""),
                            row.get("Primary Intent", ""))
    except FileNotFoundError:
        print("  (Semrush CSV not found; traffic columns will be blank)", file=sys.stderr)

    # 3) join + write
    with_traffic = 0
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["URL", "Type", "Title", "Description", "Full content", "Traffic", "Keywords", "Intent"])
        for r in rows:
            tr, kw, intent = sem.get(r["url"].rstrip("/"), ("", "", ""))
            if tr:
                with_traffic += 1
            w.writerow([r["url"], r["type"], r["title"], r["description"], r["full_content"], tr, kw, intent])

    print(f"\nTOTAL rows: {len(rows)} | rows with Semrush traffic: {with_traffic}", file=sys.stderr)
    print("PER TYPE: " + ", ".join(f"{k}={v}" for k, v in per_type.items()), file=sys.stderr)

    # 4) COVERAGE GATE — surface content gaps at build time, not weeks later inside RAG
    from collections import Counter
    have = sum(1 for r in rows if r["full_content"].strip())
    pct = 100 * have // max(1, len(rows))
    print(f"COVERAGE: {have}/{len(rows)} rows have Full content ({pct}%)", file=sys.stderr)
    empty_by_type = Counter(r["type"] for r in rows if not r["full_content"].strip())
    if empty_by_type:
        print("  still-empty by type: " + ", ".join(f"{t}={c}" for t, c in empty_by_type.most_common()), file=sys.stderr)
    if pct < 90:
        print("  ⚠️  COVERAGE BELOW 90% — investigate the types above before using this DB for RAG.", file=sys.stderr)

if __name__ == "__main__":
    main()
