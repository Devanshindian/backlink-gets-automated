#!/usr/bin/env python3
"""Step D — tag each kept candidate page by FORMAT (not topic), build the master
competitor-formats.csv with a stable Row ID. Heuristic on URL path + title against the
spec's format catalog. Order = most specific first. Default falls to 'answer-bait' for
blog-style editorial, 'guide' for long-form, else 'other' (refined by reading in Step E)."""
import csv, glob, os, re
from urllib.parse import urlparse, unquote

CAND = os.path.join(os.path.dirname(__file__), "_candidates")
OUT  = os.path.join(os.path.dirname(__file__), "..", "competitor-formats.csv")

def fmt(url, title):
    p = unquote(urlparse(url).path or "").lower()
    t = (title or "").lower()
    s = p + " " + t

    # --- company-specific: free test / skill assessment ---
    if re.search(r"/(test|tests|assessment|assessments|skills?-test|online-test|quiz-test)/", p) \
       or re.search(r"\b(test|assessment)\b.*\b(online|skills?|pre-employment|free)\b", t) \
       or re.search(r"-(test|assessment|aptitude-test|coding-test)(\b|/|$)", p):
        if "interview" not in s:
            return "Free test / assessment"
    # --- interview-questions listicle ---
    if "interview-question" in p or "interview question" in t or re.search(r"interview.*questions", t):
        return "Interview-questions listicle"
    # --- glossary / dictionary ---
    if re.search(r"/(glossary|dictionary|hr-terms|terms|definition)s?(/|$)", p) or "glossary" in t:
        return "Glossary / dictionary"
    # --- templates ---
    if re.search(r"/(template|templates|examples?|sample|samples)(/|$)", p) or "template" in t \
       or re.search(r"\bjob description\b", t):
        return "Templates"
    # --- calculator / estimator / generator / tool ---
    if re.search(r"/(calculator|estimator|generator|tool|tools|maker)(/|$)", p) \
       or re.search(r"\b(calculator|generator|estimator)\b", t):
        return "Calculator / generator / tool"
    # --- data-driven / original research / report / survey / statistics ---
    if re.search(r"/(report|reports|research|survey|statistics|stats|study|state-of|benchmark|trends?)(/|$|-)", p) \
       or re.search(r"\b(report|statistics|survey|state of|benchmark|original research|study)\b", t):
        return "Data report / research"
    # --- rankings / best tools / X vs Y comparison ---
    if re.search(r"/(best|top|alternatives?|vs|compare|comparison)(/|-|$)", p) \
       or re.search(r"\b(best|top \d+|alternatives|vs\.?|comparison)\b", t):
        return "Rankings / best-tools / comparison"
    # --- checklist / cheat sheet ---
    if "checklist" in s or "cheat-sheet" in p or "cheat sheet" in t:
        return "Checklist / cheat sheet"
    # --- facts page ---
    if re.search(r"\bfacts\b", t) or "/facts" in p:
        return "Facts page"
    # --- quiz ---
    if "/quiz" in p or re.search(r"\bquiz\b", t):
        return "Quiz"
    # --- jobs / careers descriptions (kept ones = JD libraries, not postings) ---
    if "job-description" in p or "/jobs/" in p or "job description" in t:
        return "Jobs / JD page"
    # --- case study / controversy = marketer bait ---
    if "case-study" in p or "case study" in t or "customer-story" in p:
        return "Case study / marketer bait"
    # --- ultimate guide / pillar / how-to ---
    if re.search(r"\b(ultimate guide|complete guide|the guide to|how to|how-to|playbook|handbook)\b", t) \
       or "/guide" in p or "/how-to" in p:
        return "Guide / pillar"
    # --- answer-bait (what is / how it works) ---
    if re.search(r"\b(what is|what are|how (it|does)|definition of|meaning of)\b", t) \
       or re.search(r"/what-is|/how-", p):
        return "Answer-bait (what-is / how-it-works)"
    # editorial blog post default
    if "/blog/" in p or "/resources/" in p or "/hr-glossary" in p:
        return "Answer-bait (what-is / how-it-works)"
    return "Other / editorial"

rows = []
rid = 0
for fp in sorted(glob.glob(os.path.join(CAND, "*-candidates.csv"))):
    with open(fp, newline="", encoding="utf-8", errors="replace") as f:
        for r in csv.DictReader(f):
            rid += 1
            rows.append({
                "RowID": rid,
                "Competitor": r["Competitor"],
                "URL": r["URL"],
                "Format": fmt(r["URL"], r["Title"]),
                "Domains": r["Domains"],
                "Backlinks": r["Backlinks"],
                "Title": r["Title"],
                "WhatItIs": "",   # filled in Step E
            })

with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["RowID","Competitor","URL","Format","Domains","Backlinks","Title","WhatItIs"])
    w.writeheader(); w.writerows(rows)

from collections import Counter
c = Counter(r["Format"] for r in rows)
print(f"Master written: {len(rows)} rows → {OUT}")
print("\nFormat distribution (Step D tags):")
for fmtname, n in c.most_common():
    print(f"  {n:>5}  {fmtname}")
