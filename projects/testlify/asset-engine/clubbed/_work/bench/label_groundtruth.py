#!/usr/bin/env python3
"""
Ground-truth labeling for the reuse-check benchmark.

For each asset we have a candidate POOL (built by run_baseline.py). An LLM labels
each pooled page relevant / not-relevant by the brief's rubric, giving the
ground-truth relevant set we score retrievers against.

Labeling is INDEPENDENT of rank: the LLM sees title + a short snippet per page
(not the retriever's order) and judges subject-relevance only. One `claude` CLI
call per asset (headless, logged-in session — no API key), ~4 concurrent.
Resumable: appends to groundtruth.jsonl; re-running skips done assets.

Usage: python3 label_groundtruth.py [limit]
"""
import csv, json, os, re, subprocess, sys, threading, time
from concurrent.futures import ThreadPoolExecutor, as_completed
csv.field_size_limit(1 << 24)

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.dirname(HERE)
REPO = "/Users/devanshmehta/Desktop/SUTRA/backlink-gets-automated"
CONTENT = os.path.join(REPO, "projects/testlify/content-database.csv")
LOG = os.path.join(HERE, "label.log")

MODEL = "sonnet"
WORKERS = 4
SNIPPET = 900          # chars of body shown per candidate (brief v2 used ~900)

def _flag(name, default):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default
POOL = os.path.join(HERE, _flag("--pool", "retrieval_baseline.jsonl"))
OUT = os.path.join(HERE, _flag("--out", "groundtruth.jsonl"))
_pos = [a for a in sys.argv[1:] if not a.startswith("--") and a not in (POOL, OUT)
        and not a.endswith(".jsonl")]
LIMIT = int(_pos[0]) if _pos else None

# `claude -p` must use the claude.ai login, NOT the (invalid) ANTHROPIC_API_KEY
# that's set in this environment and takes precedence. Strip it for the subprocess.
CLI_ENV = {k: v for k, v in os.environ.items() if k != "ANTHROPIC_API_KEY"}

lock = threading.Lock()
def log(m):
    with lock, open(LOG, "a", encoding="utf-8") as f:
        f.write(m + "\n")
    print(m, file=sys.stderr, flush=True)

RUBRIC = """You are a content strategist at Testlify deciding, for a PROPOSED content asset, which of our EXISTING pages are RELEVANT — i.e. pages you'd want to see when building this asset, to reuse, improve, interlink, or avoid duplicating.

PROPOSED ASSET
- Title: {asset}
- Distinct angle: {angle}

RELEVANCE RUBRIC (judge by what you READ, not word overlap):
- RELEVANT  = the page covers the SAME specific subject as the asset — a page a strategist building this asset would genuinely pull up to reuse, improve, interlink, or avoid duplicating. Be SELECTIVE: most pages in the pool are near-misses, not relevant.
- NOT       = shares only a generic word ("hiring", "test", "skills"), covers a DIFFERENT subject, or only touches the asset's topic in passing / as one section of a broader page about something else.
Most assets have on the order of ~15-25 genuinely-relevant pages, not 40+. If you are marking more than ~30, you are being too loose — re-read and keep only the same-subject pages.

CANDIDATE PAGES (each: number, title, snippet):
{cands}

Return ONE line, nothing else, no preamble:
RELEVANT: <comma-separated candidate numbers that are relevant; empty if none>"""

def parse(out, n_cands):
    m = re.search(r'(?im)^\s*RELEVANT:\s*(.*)$', out or "")
    if not m:
        return None
    nums = re.findall(r'\d+', m.group(1))
    keep = sorted({int(x) for x in nums if 1 <= int(x) <= n_cands})
    return keep

def build_prompt(asset, angle, cands):
    blocks = []
    for i, (u, title, snip) in enumerate(cands, 1):
        blocks.append(f"[{i}] {title}\n{snip}")
    return RUBRIC.format(asset=asset, angle=angle or "(none)", cands="\n\n".join(blocks))

def call(rec, cmap, tmap):
    pool = rec["pool"]
    cands = []
    for u in pool:
        snip = (cmap.get(u, "") or "").replace("\x00", " ").strip()[:SNIPPET]
        cands.append((u, (tmap.get(u, "") or u)[:160], snip or "(no snippet)"))
    prompt = build_prompt(rec["asset"], rec.get("angle", ""), cands)
    for attempt in range(3):
        try:
            p = subprocess.run(["claude", "-p", "--model", MODEL, "--dangerously-skip-permissions"],
                               input=prompt, text=True, capture_output=True, timeout=900, env=CLI_ENV)
            keep = parse(p.stdout or "", len(cands))
            if keep is not None:
                rel_urls = [pool[i - 1] for i in keep]
                return rec["idx"], rel_urls
            log(f"idx {rec['idx']}: unparseable (try {attempt+1}) out[:100]={(p.stdout or '')[:100]!r}")
        except subprocess.TimeoutExpired:
            log(f"idx {rec['idx']}: timeout (try {attempt+1})")
        except Exception as e:
            log(f"idx {rec['idx']}: err {e} (try {attempt+1})")
        time.sleep(6 * (attempt + 1))
    return rec["idx"], None

def main():
    cmap, tmap = {}, {}
    for r in csv.DictReader(open(CONTENT, encoding="utf-8")):
        u = (r.get("URL") or "").strip()
        cmap[u] = r.get("Full content", "") or ""
        tmap[u] = r.get("Title", "") or ""
    recs = [json.loads(l) for l in open(POOL, encoding="utf-8")]
    done = set()
    if os.path.exists(OUT):
        for l in open(OUT):
            try: done.add(json.loads(l)["idx"])
            except Exception: pass
    todo = [r for r in recs if r["idx"] not in done]
    if LIMIT:
        todo = todo[:LIMIT]
    log(f"=== label start: {len(todo)} todo, {len(done)} done, {WORKERS} workers, model={MODEL} ===")

    n = 0
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(call, r, cmap, tmap): r["idx"] for r in todo}
        for fut in as_completed(futs):
            idx, rel = fut.result()
            if rel is not None:
                with lock, open(OUT, "a", encoding="utf-8") as f:
                    f.write(json.dumps({"idx": idx, "relevant": rel, "n_relevant": len(rel)}) + "\n")
                n += 1
                log(f"[{n}/{len(todo)}] idx {idx} -> {len(rel)} relevant")
            else:
                log(f"idx {idx}: FAILED after retries (left for resume)")
    log(f"=== label done: {n} assets labeled this run ===")

if __name__ == "__main__":
    main()
