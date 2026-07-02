#!/usr/bin/env python3
"""
Final de-biased validation. Merges the original ground truth with the delta labels
(relevant pages found via the independent decomposition source), then scores the
two-path recall list (dense top-50) against the EXPANDED ground truth.

Reports, on de-biased labels:
  - how much the relevant set grew (the de-bias magnitude)
  - baseline rerank@15           (job A short-list, for reference)
  - dense@15  /  dense@50        (the JOB B recall path — the fix)

Usage: python3 validate_final.py
"""
import csv, json, os, re, sys, warnings
import numpy as np
warnings.filterwarnings("ignore")
csv.field_size_limit(1 << 24)
HERE = os.path.dirname(os.path.abspath(__file__)); WORK = os.path.dirname(HERE)
REPO = "/Users/devanshmehta/Desktop/SUTRA/backlink-gets-automated"
sys.path.insert(0, WORK); sys.path.insert(0, HERE)
import rag, metrics

IDX = os.path.join(WORK, "content-index")
CONTENT = os.path.join(REPO, "projects/testlify/content-database.csv")
GT = os.path.join(HERE, "groundtruth.jsonl")
GT_DELTA = os.path.join(HERE, "groundtruth_delta.jsonl")
BENCH = os.path.join(HERE, "benchmark_assets.json")
BASE = os.path.join(HERE, "retrieval_baseline.jsonl")
LOCALES = {"ar","pl","it","pt-br","no","ja","da","es","de","el","sv","nl","fr","pt","zh","ko","ru","tr","hi","id","th","vi"}
def foreign(u):
    m = re.match(r"https?://(?:www\.)?[^/]+/([^/]+)/", u or ""); return bool(m and m.group(1).lower() in LOCALES)
def qtext(a):
    return re.sub(r"\s+", " ", re.sub(r"\([^)]*\)", " ", a or "")).strip() or "untitled"

# merge ground truth (union of relevant per asset)
gt = {json.loads(l)["idx"]: set(json.loads(l)["relevant"]) for l in open(GT)}
n_before = {i: len(s) for i, s in gt.items()}
if os.path.exists(GT_DELTA):
    for l in open(GT_DELTA):
        d = json.loads(l); gt.setdefault(d["idx"], set()).update(d["relevant"])
grew = sum(len(gt[i]) - n_before.get(i, 0) for i in gt)
print(f"de-bias: relevant set grew by {grew} pages total "
      f"({round(grew/max(len(gt),1),2)}/asset avg); now avg {round(sum(len(s) for s in gt.values())/len(gt),1)}/asset")

Vt, Mt = rag.load_vecs(os.path.join(IDX, "title"))
Vb, Mb = rag.load_vecs(os.path.join(IDX, "body"))
allurls = [m["url"] for m in Mt]; uidx = {u: i for i, u in enumerate(allurls)}
body_uidx = np.array([uidx[m["url"]] for m in Mb])
nf = np.array([not foreign(u) for u in allurls])
assets = {a["idx"]: a for a in json.load(open(BENCH))}
base = {json.loads(l)["idx"]: json.loads(l) for l in open(BASE)}

def dense(qv):
    bb = np.full(len(allurls), -1.0, dtype=np.float32); np.maximum.at(bb, body_uidx, Vb @ qv)
    bl = np.where(nf, rag.ALPHA * (Vt @ qv) + (1 - rag.ALPHA) * bb, -1e9)
    return [allurls[i] for i in np.argsort(bl)[::-1][:50]]

rer15, dn15, dn50 = [], [], []
for idx, rel in gt.items():
    rel = list(rel)
    qv = rag.embed([qtext(assets[idx]["asset"])], "query")[0]; qv /= (np.linalg.norm(qv) + 1e-9)
    d50 = dense(qv)
    rer15.append(metrics.recall_at_k(rel, base[idx]["ranked15"], 15) or 0.0)
    dn15.append(metrics.recall_at_k(rel, d50, 15) or 0.0)
    dn50.append(metrics.recall_at_k(rel, d50, 50) or 0.0)

n = len(gt)
print(f"\n=== DE-BIASED recall over {n} assets ===")
print(f"  baseline rerank @15 : {sum(rer15)/n:.3f}   (job A short-list)")
print(f"  two-path dense  @15 : {sum(dn15)/n:.3f}")
print(f"  two-path dense  @50 : {sum(dn50)/n:.3f}   <-- JOB B recall path (the fix)")
