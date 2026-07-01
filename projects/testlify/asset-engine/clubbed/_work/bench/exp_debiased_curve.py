#!/usr/bin/env python3
"""
De-biased recall@K curve: settle (a) the right RECALL_N and (b) whether adding
decomposition beats just widening K, on the EXPANDED (de-biased) ground truth.

Variants per asset:
  - dense@K            : single asset-title query, dense blended top-K
  - dense+decomp@K     : union of dense top-K and the decomposition catalog (max-sim),
                         truncated to K  (the decomposition list is fix_decomp.catalog40)
CAVEAT: the de-biased GT was seeded partly BY decomposition, so dense+decomp is
upward-biased here. Read it as an UPPER bound on decomposition's help.
"""
import json, os, re, sys, warnings
import numpy as np
warnings.filterwarnings("ignore")
HERE = os.path.dirname(os.path.abspath(__file__)); WORK = os.path.dirname(HERE)
REPO = "/Users/devanshmehta/Desktop/SUTRA/backlink-gets-automated"
sys.path.insert(0, WORK); sys.path.insert(0, HERE)
import rag, metrics
import csv; csv.field_size_limit(1 << 24)

IDX = os.path.join(WORK, "content-index")
KS = [15, 25, 40, 50, 75]
LOCALES = {"ar","pl","it","pt-br","no","ja","da","es","de","el","sv","nl","fr","pt","zh","ko","ru","tr","hi","id","th","vi"}
def foreign(u):
    m = re.match(r"https?://(?:www\.)?[^/]+/([^/]+)/", u or ""); return bool(m and m.group(1).lower() in LOCALES)
def qtext(a): return re.sub(r"\s+", " ", re.sub(r"\([^)]*\)", " ", a or "")).strip() or "untitled"

# de-biased GT = union of base + delta labels
gt = {json.loads(l)["idx"]: set(json.loads(l)["relevant"]) for l in open(os.path.join(HERE, "groundtruth.jsonl"))}
for l in open(os.path.join(HERE, "groundtruth_delta.jsonl")):
    d = json.loads(l); gt.setdefault(d["idx"], set()).update(d["relevant"])
assets = {a["idx"]: a for a in json.load(open(os.path.join(HERE, "benchmark_assets.json")))}
decomp = {json.loads(l)["idx"]: json.loads(l)["catalog40"] for l in open(os.path.join(HERE, "fix_decomp.jsonl"))}

Vt, Mt = rag.load_vecs(os.path.join(IDX, "title"))
Vb, Mb = rag.load_vecs(os.path.join(IDX, "body"))
allurls = [m["url"] for m in Mt]; uidx = {u: i for i, u in enumerate(allurls)}
body_uidx = np.array([uidx[m["url"]] for m in Mb])
nf = np.array([not foreign(u) for u in allurls])

def dense_rank(qv):
    bb = np.full(len(allurls), -1.0, dtype=np.float32); np.maximum.at(bb, body_uidx, Vb @ qv)
    bl = np.where(nf, rag.ALPHA * (Vt @ qv) + (1 - rag.ALPHA) * bb, -1e9)
    return [allurls[i] for i in np.argsort(bl)[::-1]]

agg = {f"dense@{k}": [] for k in KS}; agg.update({f"dense+decomp@{k}": [] for k in KS})
for idx, rel in gt.items():
    rel = list(rel)
    qv = rag.embed([qtext(assets[idx]["asset"])], "query")[0]; qv /= (np.linalg.norm(qv) + 1e-9)
    dorder = dense_rank(qv)
    for k in KS:
        agg[f"dense@{k}"].append(metrics.recall_at_k(rel, dorder[:k], k) or 0.0)
        union = list(dict.fromkeys(dorder[:k] + decomp.get(idx, [])))[:k]   # blend decomp into budget K
        agg[f"dense+decomp@{k}"].append(metrics.recall_at_k(rel, union, k) or 0.0)

n = len(gt)
print(f"DE-BIASED recall@K over {n} assets (decomp variant is an UPPER bound — GT seeded by it)")
print(f"{'K':>5} | {'dense':>8} | {'dense+decomp':>12}")
for k in KS:
    print(f"{k:>5} | {sum(agg[f'dense@{k}'])/n:>8.3f} | {sum(agg[f'dense+decomp@{k}'])/n:>12.3f}")
