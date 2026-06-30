#!/usr/bin/env python3
"""
Fill blank descriptions in a content database by fetching each page's rendered HTML
and extracting the SEO meta description (RankMath), with og:description and first-paragraph
fallbacks. For template-driven pages whose text isn't exposed via the REST API.

Usage: enrich_meta_descriptions.py <db_csv> <progress_log>
Saves the CSV every 200 pages so partial progress is never lost.
"""
import csv, re, sys, time, urllib.request
csv.field_size_limit(1 << 24)   # Full content cells can be large

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
FIELDS = ["URL", "Type", "Title", "Description", "Full content", "Traffic", "Keywords", "Intent"]

def unescape(t):
    return (t.replace("&amp;", "&").replace("&#8217;", "'").replace("&#039;", "'")
             .replace("&#8216;", "'").replace("&quot;", '"').replace("&nbsp;", " ")
             .replace("&#8211;", "-").replace("&#8230;", "...").strip())

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for _ in range(2):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode("utf-8", "ignore")
        except Exception:
            time.sleep(0.5)
    return ""

def extract(html):
    if not html:
        return ""
    for pat in [r'<meta[^>]+name=["\']description["\'][^>]*content=["\'](.*?)["\']',
                r'<meta[^>]+content=["\'](.*?)["\'][^>]*name=["\']description["\']',
                r'<meta[^>]+property=["\']og:description["\'][^>]*content=["\'](.*?)["\']']:
        m = re.search(pat, html, re.I | re.S)
        if m:
            t = re.sub(r"\s+", " ", m.group(1)).strip()
            if len(t) >= 20:
                return unescape(t)[:300]
    for p in re.findall(r"<p[^>]*>(.*?)</p>", html, re.S | re.I):
        t = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", p)).strip()
        if len(t) >= 40:
            return unescape(t)[:300]
    return ""

def save(rows, path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)

def main():
    db, logp = sys.argv[1], sys.argv[2]
    rows = list(csv.DictReader(open(db, encoding="utf-8")))
    blanks = [r for r in rows if not r["Description"].strip()]
    log = open(logp, "w")
    log.write(f"START: {len(blanks)} blank rows to fill\n"); log.flush()
    filled = 0
    for n, r in enumerate(blanks, 1):
        d = extract(fetch(r["URL"]))
        if d:
            r["Description"] = d
            filled += 1
        if n % 200 == 0:
            log.write(f"{n}/{len(blanks)} processed, {filled} filled\n"); log.flush()
            save(rows, db)
        time.sleep(0.12)
    save(rows, db)
    log.write(f"DONE: {n}/{len(blanks)} processed, {filled} filled\n"); log.flush()

if __name__ == "__main__":
    main()
