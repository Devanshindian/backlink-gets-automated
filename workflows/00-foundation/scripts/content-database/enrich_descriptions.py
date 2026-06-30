#!/usr/bin/env python3
"""
Enrich blank descriptions in a content database by pulling the first content
paragraph from the WordPress REST API (for post types that don't use excerpts).

Usage: enrich_descriptions.py <site_base> <db_csv> <type1,type2,...>
"""
import csv, json, re, sys, time, urllib.request, urllib.error
csv.field_size_limit(1 << 24)   # Full content cells can be large

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=45) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 400:
                return None
            time.sleep(1)
        except Exception:
            time.sleep(1)
    return None

def first_para(html):
    if not html:
        return ""
    for p in re.findall(r"<p[^>]*>(.*?)</p>", html, re.S | re.I):
        t = re.sub(r"<[^>]+>", "", p)
        t = t.replace("&nbsp;", " ").replace("&amp;", "&").replace("&#8217;", "'")
        t = re.sub(r"\s+", " ", t).strip()
        if len(t) >= 40:
            return t[:300]
    t = re.sub(r"<[^>]+>", " ", html)
    return re.sub(r"\s+", " ", t).strip()[:300]

def main():
    base, db_csv, types = sys.argv[1], sys.argv[2], sys.argv[3].split(",")
    api = base.rstrip("/") + "/wp-json/wp/v2"
    desc = {}
    for t in types:
        page = 1
        while True:
            data = fetch(f"{api}/{t}?per_page=100&page={page}&_fields=link,content")
            if not data:
                break
            for it in data:
                desc[(it.get("link", "")).rstrip("/")] = first_para((it.get("content") or {}).get("rendered", ""))
            if len(data) < 100:
                break
            page += 1
            time.sleep(0.15)
        print(f"  {t}: fetched", file=sys.stderr)

    rows = list(csv.DictReader(open(db_csv, encoding="utf-8")))
    updated = 0
    for r in rows:
        if not r["Description"].strip():
            d = desc.get(r["URL"].rstrip("/"))
            if d:
                r["Description"] = d
                updated += 1
    with open(db_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["URL", "Type", "Title", "Description", "Full content", "Traffic", "Keywords", "Intent"])
        w.writeheader()
        w.writerows(rows)
    print(f"Updated {updated} descriptions.", file=sys.stderr)

if __name__ == "__main__":
    main()
