#!/usr/bin/env python3
"""
Score a retriever's ranked output against the ground-truth labels.

Reads:
  - groundtruth.jsonl        (idx -> relevant[urls])   from label_groundtruth.py
  - <retrieval>.jsonl        (idx -> ranked15[urls])   from run_baseline.py / a fix variant
Prints macro-averaged recall@10/15, precision@10, n scored, avg relevant set,
plus a per-source breakdown and the worst-recall assets.

Usage: python3 score.py [retrieval.jsonl] [groundtruth.jsonl]
  defaults: retrieval_baseline.jsonl , groundtruth.jsonl
  ranked field: uses "ranked15" if present, else "catalog40"[:15] is NOT used —
  pass --catalog to score the catalog list instead.
"""
import json, os, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import metrics

args = [a for a in sys.argv[1:] if not a.startswith("--")]
USE_CATALOG = "--catalog" in sys.argv
RANKED = args[0] if len(args) > 0 else os.path.join(HERE, "retrieval_baseline.jsonl")
GT = args[1] if len(args) > 1 else os.path.join(HERE, "groundtruth.jsonl")
BENCH = os.path.join(HERE, "benchmark_assets.json")

def main():
    gt = {json.loads(l)["idx"]: json.loads(l)["relevant"] for l in open(GT)}
    ranked = {json.loads(l)["idx"]: json.loads(l) for l in open(RANKED)}
    src = {a["idx"]: a["source"] for a in json.load(open(BENCH))}

    per_asset, by_src = [], defaultdict(list)
    for idx, rel in gt.items():
        if idx not in ranked:
            continue
        rec = {"asset": ranked[idx]["asset"], "relevant": rel, "ranked": ranked[idx]["ranked15"]}
        per_asset.append(rec)
        by_src[src.get(idx, "?")].append(rec)

    print(f"=== {os.path.basename(RANKED)} vs {len(gt)} labeled assets ===")
    overall = metrics.evaluate(per_asset, ks=(10, 15))
    for k, v in overall.items():
        print(f"  {k}: {v}")

    print("--- by source ---")
    for s, recs in sorted(by_src.items()):
        e = metrics.evaluate(recs, ks=(10, 15))
        print(f"  {s:12s} n={e['n_assets_scored']:2d}  recall@15={e['recall@15']}  precision@10={e['precision@10']}  avg_rel={e['avg_relevant_set']}")

    print("--- 8 worst recall@15 ---")
    scored = [(metrics.recall_at_k(r["relevant"], r["ranked"], 15), r) for r in per_asset
              if metrics.recall_at_k(r["relevant"], r["ranked"], 15) is not None]
    for rec15, r in sorted(scored, key=lambda x: x[0])[:8]:
        print(f"  {rec15:.2f}  rel={len(r['relevant']):2d}  {r['asset'][:60]}")

if __name__ == "__main__":
    main()
