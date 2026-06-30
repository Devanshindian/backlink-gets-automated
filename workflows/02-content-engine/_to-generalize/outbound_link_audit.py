#!/usr/bin/env python3
"""Inventory outbound external links across testlify.com and flag likely PAID placements.

Seeds the sponsored-link cleanup (Jira TM-408). For every public URL in the sitemap
index, fetch the page, extract external <a> links, and record: source page, target
domain, anchor text, current rel, whether it is dofollow, and a classification.

Classification:
  PAID-REVIEW         dofollow external link to a non-authority/commercial domain -> likely a
                      paid/partner placement that should become rel="sponsored".
  EDITORIAL-DOFOLLOW  dofollow link to a known authority/neutral source -> should be nofollow
                      per the citation policy, but is probably not a paid placement.
  OK-NOFOLLOW         already nofollow/sponsored -> no action.

Output: CSV (source_url, target_url, target_domain, anchor, rel, dofollow, classification)
plus a printed summary (pages scanned, dofollow external count, top target domains).

Usage:
  python3 outbound_link_audit.py [--out PATH] [--max-pages N] [--workers 8]
Reads nothing authenticated; public pages only. Honors a modest concurrency to be polite.
"""
import argparse, csv, re, sys, urllib.request, urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import Counter

SITEMAP_INDEX = "https://testlify.com/sitemap_index.xml"
OWN = ("testlify.com",)  # any *.testlify.com is internal
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# neutral/authority domains we cite editorially (NOT paid). Extend as needed.
AUTHORITY = (
    ".gov", ".edu", "shrm.org", "gallup.com", "mckinsey.com", "gartner.com", "bls.gov",
    "linkedin.com", "deloitte.com", "hbr.org", "wikipedia.org", "weforum.org", "who.int",
    "harvard.edu", "nih.gov", "pubmed", "arxiv.org", "sagepub.com", "wharton.upenn.edu",
    "statista.com", "pewresearch.org", "glassdoor.com", "indeed.com/lead", "g2.com",
)

def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,application/xml"})
    return urllib.request.urlopen(req, timeout=timeout).read().decode("utf-8", "ignore")

def locs(xml):
    return re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", xml)

def all_page_urls():
    idx = fetch(SITEMAP_INDEX)
    subs = locs(idx)
    if not subs:  # not an index, treat as urlset
        return locs(idx)
    urls = []
    for s in subs:
        try:
            urls.extend(locs(fetch(s)))
        except Exception as e:
            print(f"  sitemap fail {s}: {e}", file=sys.stderr)
    # de-dupe, keep only testlify pages
    seen, out = set(), []
    for u in urls:
        if u not in seen and "testlify.com" in u:
            seen.add(u); out.append(u)
    return out

A_RE = re.compile(r"<a\s+([^>]*?)>(.*?)</a>", re.S | re.I)
HREF_RE = re.compile(r'href=["\']([^"\']+)["\']', re.I)
REL_RE = re.compile(r'rel=["\']([^"\']*)["\']', re.I)

def is_internal(host):
    return any(host == d or host.endswith("." + d) for d in OWN)

SOCIAL_HOSTS = (
    "facebook.com", "twitter.com", "x.com", "youtube.com", "youtu.be", "instagram.com",
    "pinterest.com", "mail.google.com", "wa.me", "whatsapp.com", "t.me", "telegram.me",
    "reddit.com", "tumblr.com", "messenger.com", "snapchat.com", "threads.net",
)
SHARE_PAT = re.compile(r"(share|sharer|sharing|/intent|/submit|mailto:)", re.I)

def classify(domain, rel, href):
    # social / share / nav buttons - not paid placements, ignore
    if any(domain == h or domain.endswith("." + h) for h in SOCIAL_HOSTS) or SHARE_PAT.search(href):
        return "SOCIAL-NAV", False
    rl = rel.lower()
    if "nofollow" in rl or "sponsored" in rl or "ugc" in rl:
        return "OK-NOFOLLOW", False
    # dofollow external
    if any(a in domain for a in AUTHORITY):
        return "EDITORIAL-DOFOLLOW", True
    return "PAID-REVIEW", True

def scan_page(url):
    rows = []
    try:
        html = fetch(url)
    except Exception:
        return rows, False
    for attrs, inner in A_RE.findall(html):
        hm = HREF_RE.search(attrs)
        if not hm:
            continue
        href = hm.group(1).strip()
        if not href.startswith("http"):
            continue
        host = urllib.parse.urlparse(href).netloc.lower()
        host = host[4:] if host.startswith("www.") else host
        if not host or is_internal(host):
            continue
        rel = (REL_RE.search(attrs).group(1) if REL_RE.search(attrs) else "")
        anchor = re.sub("<[^>]+>", "", inner)
        anchor = re.sub(r"\s+", " ", anchor).strip()[:120]
        cls, dofollow = classify(host, rel, href)
        rows.append((url, href, host, anchor, rel or "(none=dofollow)", dofollow, cls))
    return rows, True

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="outbound-link-audit.csv")  # cwd-relative; was a hardcoded Desktop path that fails in cloud
    ap.add_argument("--max-pages", type=int, default=0, help="0 = all")
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()

    print("collecting sitemap URLs...", flush=True)
    pages = all_page_urls()
    if args.max_pages:
        pages = pages[: args.max_pages]
    print(f"pages to scan: {len(pages)}", flush=True)

    all_rows = []
    ok = fail = 0
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(scan_page, u): u for u in pages}
        for i, fut in enumerate(as_completed(futs), 1):
            rows, good = fut.result()
            if good: ok += 1
            else: fail += 1
            all_rows.extend(rows)
            if i % 250 == 0:
                print(f"  scanned {i}/{len(pages)} (ok={ok} fail={fail}, links so far={len(all_rows)})", flush=True)

    with open(args.out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source_url", "target_url", "target_domain", "anchor", "rel", "dofollow", "classification"])
        w.writerows(all_rows)

    dofollow = [r for r in all_rows if r[5]]
    paid = [r for r in all_rows if r[6] == "PAID-REVIEW"]
    edit = [r for r in all_rows if r[6] == "EDITORIAL-DOFOLLOW"]
    print("\n==== SUMMARY ====", flush=True)
    print(f"pages scanned ok: {ok} | failed: {fail}")
    print(f"external links found: {len(all_rows)}")
    print(f"  dofollow external: {len(dofollow)}")
    print(f"  PAID-REVIEW (likely paid, fix to sponsored): {len(paid)} across {len(set(r[0] for r in paid))} pages")
    print(f"  EDITORIAL-DOFOLLOW (should be nofollow): {len(edit)}")
    print(f"  already OK (nofollow/sponsored): {len(all_rows)-len(dofollow)}")
    print("\nTop PAID-REVIEW target domains:")
    for dom, c in Counter(r[2] for r in paid).most_common(25):
        print(f"  {c:5d}  {dom}")
    print(f"\nCSV written: {args.out}")

if __name__ == "__main__":
    main()
