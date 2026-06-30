#!/usr/bin/env python3
"""Scaffold a SERP study for a focus keyword.

What this is
------------
A fallback SERP study scaffolder. It produces the JSON skeleton the refresh
workflow expects at ``research-notes/<slug>-serp-<date>.json`` so drafting can
proceed even when a paid SERP source is unavailable.

HONESTY ABOUT DATA SOURCES
--------------------------
The REAL source of SERP intelligence is the Semrush MCP (keyword_overview,
related_keywords, keyword_questions) and a proper SERP API or browser
automation (top 20 results, featured snippet owner, AI Overview presence,
People-Also-Ask). This script CANNOT reliably scrape Google: Google blocks
automated queries and the result is neither stable nor ToS-compliant.

What this script does:
  - Optionally attempts a lightweight HTML fetch of a search results page IF
    you pass --serp-html-url (e.g. a permitted SERP API endpoint that returns
    HTML/JSON). With no such URL it writes an empty scaffold for manual fill.
  - Writes a structured JSON file with every field the workflow needs.

What it does NOT do:
  - It does NOT fabricate top_urls, word counts, snippet owners, or PAA
    questions. Unknown fields are written as null/empty for the operator (or
    Semrush MCP) to fill. Inventing this data would corrupt the drafting brief.

DATE
----
The date is REQUIRED via --date (YYYY-MM-DD). This script never calls
datetime.now() implicitly, so studies are reproducible and dated by the
operator's intent, not wall-clock.

CLI
---
    python serp_study.py "candidate screening" --date 2026-06-16
    python serp_study.py "candidate screening" --date 2026-06-16 \\
        --serp-html-url "https://your-serp-api/search?q=candidate+screening" \\
        --out-dir research-notes
"""

import argparse
import json
import pathlib
import re
import sys
import urllib.error
import urllib.request

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)


def slugify(text):
    """Lowercase, hyphenated, alnum-only slug."""
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "keyword"


def validate_date(value):
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise argparse.ArgumentTypeError(
            f"--date must be YYYY-MM-DD, got '{value}'"
        )
    return value


def try_fetch_urls(serp_html_url):
    """Best-effort extraction of result URLs from a SERP HTML/JSON endpoint.

    Returns a list of URLs, or [] if nothing usable is found. This is a
    convenience for permitted SERP API endpoints, not a Google scraper.
    """
    if not serp_html_url:
        return []
    try:
        req = urllib.request.Request(
            serp_html_url, headers={"User-Agent": USER_AGENT}
        )
        with urllib.request.urlopen(req, timeout=45) as resp:
            body = resp.read().decode("utf-8", "replace")
    except (urllib.error.URLError, urllib.error.HTTPError) as exc:
        print(f"[WARN] could not fetch --serp-html-url: {exc}", file=sys.stderr)
        return []

    # Grab http(s) URLs; drop obvious Google/asset noise. Dedup, keep order.
    candidates = re.findall(r'https?://[^\s"\'<>)]+', body)
    seen, urls = set(), []
    skip = ("google.", "gstatic.", "googleusercontent.", "schema.org",
            "w3.org", "youtube.com/redirect")
    for url in candidates:
        if any(s in url for s in skip):
            continue
        if url in seen:
            continue
        seen.add(url)
        urls.append(url)
        if len(urls) >= 10:
            break
    return urls


def build_study(keyword, date, top_urls):
    """Assemble the study dict. Unknown numeric/feature fields stay null."""
    return {
        "keyword": keyword,
        "date": date,
        "source_note": (
            "Scaffold from serp_study.py. REAL SERP data should come from "
            "Semrush MCP + a SERP API / browser automation. Fields left null "
            "below were NOT fetched and must be filled before drafting."
        ),
        "top_urls": top_urls,  # may be [] if no source provided
        "median_word_count": None,
        "citation_target": None,    # set to SERP median citations + 1
        "schema_target": None,      # set to SERP median schema types + 1
        "features": {
            "featured_snippet": None,   # owner domain string, or false
            "ai_overview": None,        # true / false
            "paa": [],                  # People-Also-Ask questions
        },
    }


def main(argv=None):
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("keyword", help="Focus keyword")
    parser.add_argument("--date", required=True, type=validate_date,
                        help="Study date, YYYY-MM-DD (no implicit now())")
    parser.add_argument("--out-dir", default="research-notes",
                        help="Output directory")
    parser.add_argument("--serp-html-url", default=None,
                        help="Optional permitted SERP API endpoint returning "
                             "HTML/JSON to extract result URLs from")
    args = parser.parse_args(argv)

    top_urls = try_fetch_urls(args.serp_html_url)
    if not top_urls:
        print("[INFO] No top_urls fetched. Writing empty scaffold for manual "
              "or Semrush-MCP fill.", file=sys.stderr)

    study = build_study(args.keyword, args.date, top_urls)

    out_dir = pathlib.Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{slugify(args.keyword)}-serp-{args.date}.json"
    out_path.write_text(json.dumps(study, indent=2, ensure_ascii=False))

    print(f"Wrote SERP study scaffold: {out_path}")
    print("Fill median_word_count, citation_target, schema_target, and "
          "features via Semrush MCP / SERP API before drafting.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
