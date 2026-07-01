#!/usr/bin/env python3
"""
Local-only viewer rebuild. Same as build_review_html.py but uses the existing
standalone clubbed-ideas-review.html as BOTH template and output (the _pages-repo/
publish clone is gitignored / absent in a fresh checkout). Publishing to GitHub
Pages stays a separate, explicit step.

Usage: python3 build_review_local.py
"""
import csv, json, re, os
csv.field_size_limit(1 << 24)
C = "/Users/devanshmehta/Desktop/SUTRA/backlink-gets-automated/projects/testlify/asset-engine/clubbed"
REVIEW = os.path.join(C, "clubbed-ideas-review.csv")
HTML = os.path.join(C, "clubbed-ideas-review.html")   # template + output (local standalone)

def parse_rag(cell):
    out = []
    for seg in (cell or "").split(";"):
        seg = seg.strip()
        if not seg:
            continue
        m = re.match(r'^(.*?) — (https?://\S+) \(([\-\d.]+)\)$', seg)
        if m:
            out.append({"title": m.group(1), "url": m.group(2), "score": m.group(3)})
        else:
            mu = re.search(r'(https?://\S+)', seg)
            out.append({"title": seg, "url": mu.group(1) if mu else "", "score": ""})
    return out

def urls(cell):
    return [u.strip() for u in (cell or "").split(";") if u.strip()]

def parse_cat(cell):
    out = []
    for seg in (cell or "").split(";"):
        seg = seg.strip()
        if not seg:
            continue
        m = re.match(r'^(.*?) — (https?://\S+)$', seg)
        if m:
            out.append({"title": m.group(1), "url": m.group(2), "score": ""})
    return out

data = []
for i, r in enumerate(csv.DictReader(open(REVIEW, encoding="utf-8"))):
    data.append({
        "i": i, "src": r["Source method"], "fit": r["Brand fit"], "asset": r["Asset"],
        "format": r["Format"], "angle": r["Distinct angle"], "domains": r["Total domains"],
        "comps": r["# comps"], "posts": r["# posts"], "beat": r["Beatability"], "effort": r["Effort"],
        "verdict": r["Reuse verdict"], "why": r["Why"],
        "rag": parse_rag(r["RAG candidates"]), "chosen": urls(r["Chosen links"]), "proof": urls(r["Proof URLs"]),
        "cat": parse_cat(r.get("Topic pages we own", "")),
    })

blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
lines = open(HTML, encoding="utf-8").read().split("\n")
for idx, l in enumerate(lines):
    if l.startswith("const DATA ="):
        lines[idx] = "const DATA = " + blob + ";"
        break
else:
    raise SystemExit("could not find 'const DATA =' line in template")
open(HTML, "w", encoding="utf-8").write("\n".join(lines))
avg_cat = sum(len(d["cat"]) for d in data) / max(len(data), 1)
print(f"rebuilt local viewer: {len(data)} ideas, avg catalogue {avg_cat:.1f} pages/idea -> {HTML}")
