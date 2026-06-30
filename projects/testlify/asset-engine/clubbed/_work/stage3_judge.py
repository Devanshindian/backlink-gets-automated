#!/usr/bin/env python3
"""
Stage 3 — reuse-check LLM judgment, run via the `claude` CLI headless (uses the
logged-in session; no API key). One idea per call, ~6 concurrent. Resumable:
each result is appended to stage3_results.jsonl as it lands, and merged into
clubbed-ideas.csv. Re-running skips ideas already done.

Usage: stage3_judge.py [limit]   (limit = process only the first N todo rows, for a smoke test)
"""
import csv, json, os, re, subprocess, sys, threading, time
from concurrent.futures import ThreadPoolExecutor, as_completed
csv.field_size_limit(1 << 24)

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # .../clubbed
CSV  = os.path.join(BASE, "clubbed-ideas.csv")
RES  = os.path.join(BASE, "_work", "stage3_results.jsonl")
LOG  = os.path.join(BASE, "_work", "stage3.log")
WORKERS = 6
MODEL = "sonnet"
VERDICTS = ["Already have it", "Improve existing", "Build from parts", "Brand new"]
LIMIT = int(sys.argv[1]) if len(sys.argv) > 1 else None

lock = threading.Lock()
def log(m):
    with lock:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(m + "\n")
    print(m, file=sys.stderr, flush=True)

PROMPT = """You are helping Testlify decide one thing about a proposed content asset: should we BUILD it, or does our EXISTING content already cover it (fully or partly)? Read the existing pages and return one verdict, the links it points to, and why.

THE PROPOSED ASSET
- Asset (working title): {asset}
- Distinct angle (the twist that makes it link-worthy): {angle}
- Format (its shape): {fmt}

OUR CLOSEST EXISTING PAGES -- full text of each; these are the ONLY pages you may cite:
{cands}

STEP 1 -- run three tests on EACH candidate, judging by what you READ, not keyword overlap:
- Topic test: is the page actually about this asset's subject (not just sharing a word)?
- Format test: is it the SAME SHAPE as the asset? A text article is NOT a calculator / quiz / index / data report / template.
- Angle test: does it already have the asset's distinct angle (above)?

STEP 2 -- pick exactly ONE verdict, top-down, first match wins:
- Already have it: a page already delivers this asset -- SAME topic + SAME format + ALREADY has the angle, at good quality. Building again would just duplicate. RARE: the angle is usually new, don't reach for it.
- Improve existing: ONE page is clearly this same topic but WEAKER than the asset would be (missing the angle, wrong/old format, thin, outdated). Building means upgrading THAT page, not making a second one.
- Build from parts: NO single page is this asset, but >=2 candidates each hold reusable material (data, definitions, sections) you'd pull from to build it. Build new, reuse the research.
- Brand new: NO candidate is genuinely relevant -- none really covers the topic, or only touches it superficially. Build from scratch.

RULES
- Cite ONLY links from the candidates above -- never invent a URL.
- Base the verdict on the FULL TEXT you actually read, not the title.
- Be strict about "Already have it": if a page lacks the asset's angle OR its format, it is at most "Improve existing", never "Already have it".

RETURN EXACTLY THESE THREE FIELDS -- nothing else, no preamble:
Reuse verdict: <one of: Already have it / Improve existing / Build from parts / Brand new>
Chosen links: <the link(s) the verdict points to -- 1 for Already-have; 1-3 for Improve; the source links for Build from parts; BLANK for Brand new. Links only, drawn from the candidates, semicolon-separated.>
Why: <a short paragraph citing concrete evidence -- what the page(s) have or lack that drove the verdict.>"""

def build_prompt(r):
    cands = []
    for i in range(1, 8):
        c = (r.get(f"Candidate {i} content") or "").strip()
        if c:
            cands.append(f"--- CANDIDATE {i} ---\n{c}")
    return PROMPT.format(asset=r.get("Asset", ""), angle=r.get("Distinct angle", ""),
                         fmt=r.get("Format", "") or "(none specified)",
                         cands="\n\n".join(cands) if cands else "(no candidates)")

def parse(out):
    v = re.search(r'(?im)^[ \t]*Reuse verdict:[ \t]*(.+?)[ \t]*$', out)
    l = re.search(r'(?im)^[ \t]*Chosen links:[ \t]*(.*)$', out)   # [ \t] not \s — don't eat the newline into the next line
    w = re.search(r'(?is)\bWhy:\s*(.+)$', out)
    if not v:
        return None
    verdict = re.sub(r'^[^A-Za-z]*', '', v.group(1)).strip()      # strip any emoji/punct prefix
    match = next((vd for vd in VERDICTS if vd.lower() in verdict.lower()), None)
    if not match:
        return None
    return {"verdict": match,
            "links": (l.group(1).strip() if l else ""),
            "why": (w.group(1).strip() if w else "")}

def call(i, r):
    prompt = build_prompt(r)
    for attempt in range(3):
        try:
            p = subprocess.run(["claude", "-p", "--model", MODEL, "--dangerously-skip-permissions"],
                               input=prompt, text=True, capture_output=True, timeout=900)
            parsed = parse(p.stdout or "")
            if parsed:
                return i, parsed
            log(f"row {i}: unparseable (attempt {attempt+1}) rc={p.returncode} out[:120]={(p.stdout or '')[:120]!r}")
        except subprocess.TimeoutExpired:
            log(f"row {i}: timeout (attempt {attempt+1})")
        except Exception as e:
            log(f"row {i}: error {e} (attempt {attempt+1})")
        time.sleep(8 * (attempt + 1))
    return i, None

def merge_into_csv(rows, fields):
    done = {}
    if os.path.exists(RES):
        for line in open(RES, encoding="utf-8"):
            d = json.loads(line); done[d["i"]] = d
    for i, d in done.items():
        rows[i]["Reuse verdict"] = d["verdict"]
        rows[i]["Chosen links"] = d["links"]
        rows[i]["Why"] = d["why"]
    tmp = CSV + ".tmp"
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)
    os.replace(tmp, CSV)

def main():
    with open(CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f); fields = reader.fieldnames; rows = list(reader)
    done = set()
    if os.path.exists(RES):
        for line in open(RES, encoding="utf-8"):
            done.add(json.loads(line)["i"])
    todo = [i for i, r in enumerate(rows)
            if i not in done and not (r.get("Reuse verdict") or "").strip()]
    if LIMIT:
        todo = todo[:LIMIT]
    log(f"=== stage3 start: {len(todo)} todo, {len(done)} already done, {WORKERS} workers ===")

    n_done = 0
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(call, i, rows[i]): i for i in todo}
        for fut in as_completed(futs):
            i, parsed = fut.result()
            if parsed:
                with lock:
                    with open(RES, "a", encoding="utf-8") as f:
                        f.write(json.dumps({"i": i, **parsed}) + "\n")
                n_done += 1
                log(f"[{n_done}/{len(todo)}] row {i} -> {parsed['verdict']}")
                if n_done % 50 == 0:
                    merge_into_csv(rows, fields); log(f"   (merged {n_done} into CSV)")
            else:
                log(f"row {i}: FAILED after retries (left for resume)")
    merge_into_csv(rows, fields)
    log(f"=== stage3 done: {n_done} judged this run ===")

if __name__ == "__main__":
    main()
