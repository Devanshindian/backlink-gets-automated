#!/usr/bin/env python3
"""Step C — filter each competitor's top-300-by-Domains indexed pages down to replicable
formats. Implements the keep/drop rules from 1-competitor-study.md. Path-based matching.
Bias = KEEP (over-dropping is unrecoverable; commercial slips get SKIP'd later at G2)."""
import csv, os, re, glob
from urllib.parse import urlparse, unquote

RAW = os.path.join(os.path.dirname(__file__), "..", "_raw")
OUT = os.path.join(os.path.dirname(__file__), "_candidates")
os.makedirs(OUT, exist_ok=True)

TOP_N = 300
ALLOW_SUB = {"", "www", "blog", "resources"}
LOCALES = {"fr","de","es","nl","ja","it","pt","ru","zh","ko","ar","pl","tr","sv","da",
           "no","fi","cs","hu","ro","el","he","th","vi","id","uk","hi","bg","sk","hr",
           "lt","sl","et","lv","ms","ca","fa"}  # 2-letter locale first-segment
# english kept; "en" first segment also kept (canonical english)

def registrable(host):
    labels = host.split(".")
    if len(labels) <= 2:
        return host
    # crude multi-part TLD handling (.co.uk etc.) — niche, but safe
    if labels[-2] in {"co","com","org","net","gov","ac"} and len(labels[-1])==2:
        return ".".join(labels[-3:])
    return ".".join(labels[-2:])

def subdomain(host, reg):
    if host == reg: return ""
    return host[:-(len(reg)+1)]

# --- drop predicates on the PATH (already lowercased, no domain) ---
DROP_PATH_SUBSTR = [
    "/pricing", "/login", "/log-in", "/signin", "/sign-in", "/signup", "/sign-up",
    "/register", "/registration", "/contact", "/demo", "/book-a-demo", "/request-demo",
    "/free-trial", "/get-started", "/checkout", "/cart", "/account", "/billing",
    "/auth/", "/quizzes/", "/reports/", "/instructions", "/tour", "/api/", "/openapi",
    "/cert/", "download-certificate", "/certificate/", "/for-jobseekers", "/home-redux",
    "/careers", "/privacy", "/terms", "/cookie", "/gdpr", "/sitemap", "/search",
    "/wp-login", "/wp-admin", "/cdn-cgi/", "/feed",
]
# nav/archive index pages (exact-ish path segments)
NAV_SEGMENTS = {"blog","author","authors","tag","tags","category","categories","topic","topics"}
JOB_RE = re.compile(r"/jobs?/[^/]+")   # /jobs/<id> style postings
COMMERCIAL_RE = re.compile(r"/(enterprise|solutions?|use-cases?|industries|for-)")

def first_seg(path):
    parts = [p for p in path.split("/") if p]
    return parts[0] if parts else ""

def is_locale_dup(path):
    return first_seg(path) in LOCALES

def is_homepage(path, query):
    # root or empty path = homepage/root variant
    return path in ("", "/")

def is_nav_index(path):
    parts = [p for p in path.split("/") if p]
    if not parts: return False
    # a bare /blog/ or /blog (index), /tag/x, /category/x, /author/x
    if parts[0] in NAV_SEGMENTS:
        # /blog/<slug> is a real post -> keep; /blog (index) or /tag/<x> archive -> drop
        if parts[0] == "blog" and len(parts) >= 2:
            return False  # real blog post
        return True
    return False

def should_drop(url, code):
    try:
        u = urlparse(url)
    except Exception:
        return True, "unparseable"
    host = u.netloc.lower().split(":")[0]
    reg = registrable(host)
    sub = subdomain(host, reg)
    path = unquote(u.path or "").lower()
    query = u.query or ""

    # rule 1 + 2: homepage/root variants (any code), and dead pages 404/410
    if is_homepage(path, query):
        return True, "homepage/root-variant"
    if code in ("404", "410"):
        return True, "dead-404/410"
    # rule 8: subdomain allow-list (root/www/blog/resources only)
    if sub not in ALLOW_SUB:
        return True, f"non-content-subdomain:{sub}"
    # rule 3: locale duplicate
    if is_locale_dup(path):
        return True, "locale-dup"
    # rule 5: nav/archive index
    if is_nav_index(path):
        return True, "nav/archive-index"
    # rule 7: job postings
    if JOB_RE.search(path):
        return True, "job-posting"
    # rule 4/6: commercial + utility substrings
    for s in DROP_PATH_SUBSTR:
        if s in path:
            return True, f"commercial/utility:{s}"
    if COMMERCIAL_RE.search(path):
        return True, "commercial-marketing"
    # capitalised nav dupes like /Tests -> path lowercased already; catch trailing dup via raw
    return False, ""

summary = []
for fp in sorted(glob.glob(os.path.join(RAW, "*-indexed-pages.csv"))):
    comp = os.path.basename(fp).replace("-indexed-pages.csv", "")
    rows = []
    with open(fp, newline="", encoding="utf-8", errors="replace") as f:
        r = csv.DictReader(f)
        for row in r:
            try:
                dom = int(row.get("Domains") or 0)
            except ValueError:
                dom = 0
            rows.append((dom, row))
    rows.sort(key=lambda x: x[0], reverse=True)
    top = rows[:TOP_N]
    kept = []
    drop_reasons = {}
    for dom, row in top:
        url = (row.get("Source url") or "").strip()
        code = (row.get("Response code") or "").strip()
        drop, why = should_drop(url, code)
        if drop:
            key = why.split(":")[0]
            drop_reasons[key] = drop_reasons.get(key, 0) + 1
            continue
        kept.append({
            "Competitor": comp,
            "URL": url,
            "Domains": dom,
            "Backlinks": (row.get("Backlinks") or "").strip(),
            "ResponseCode": code,
            "Title": (row.get("Source title") or "").strip(),
        })
    outp = os.path.join(OUT, f"{comp}-candidates.csv")
    with open(outp, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["Competitor","URL","Domains","Backlinks","ResponseCode","Title"])
        w.writeheader(); w.writerows(kept)
    summary.append((comp, len(top), len(kept), drop_reasons))

print(f"{'Competitor':<16}{'top':>5}{'kept':>6}   top drop reasons")
total_kept = 0
for comp, ntop, nkept, dr in summary:
    total_kept += nkept
    topdr = ", ".join(f"{k}={v}" for k,v in sorted(dr.items(), key=lambda x:-x[1])[:4])
    print(f"{comp:<16}{ntop:>5}{nkept:>6}   {topdr}")
print(f"\nTOTAL kept across {len(summary)} competitors: {total_kept}")
