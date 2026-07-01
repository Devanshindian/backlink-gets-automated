#!/usr/bin/env python3
"""
Build the DELTA labeling pool for de-biased validation.

The existing ground truth was labeled over the baseline pool (dense top-75 ∪ kw-net).
Decomposition reaches OUTSIDE that (sub-angle retrievals surface pages dense ranked
>75). So the delta = (decomposition catalog40) MINUS (already-labeled baseline pool)
= candidate relevant pages the original labels never saw. Labeling these de-biases
the recall denominator.

Output delta_pool.jsonl in label format: {idx, asset, angle, pool:[new urls]}.

Usage: python3 build_delta_pool.py
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(HERE, "retrieval_baseline.jsonl")   # has per-asset labeled pool
FIX = os.path.join(HERE, "fix_decomp.jsonl")            # independent candidate source
BENCH = os.path.join(HERE, "benchmark_assets.json")
OUT = os.path.join(HERE, "delta_pool.jsonl")
CAP = 40   # cap new pages to label per asset

def main():
    base = {json.loads(l)["idx"]: set(json.loads(l)["pool"]) for l in open(BASE)}
    fix = {json.loads(l)["idx"]: json.loads(l) for l in open(FIX)}
    angle = {a["idx"]: a.get("angle", "") for a in json.load(open(BENCH))}
    n_new = []
    with open(OUT, "w", encoding="utf-8") as f:
        for idx, fx in fix.items():
            already = base.get(idx, set())
            delta = [u for u in fx["catalog40"] if u not in already][:CAP]
            n_new.append(len(delta))
            if delta:
                f.write(json.dumps({"idx": idx, "asset": fx["asset"],
                                    "angle": angle.get(idx, ""), "pool": delta}) + "\n")
    print(f"delta pool: {sum(1 for x in n_new if x)} assets with new pages; "
          f"avg new/asset {round(sum(n_new)/max(len(n_new),1),1)}, max {max(n_new) if n_new else 0}")

if __name__ == "__main__":
    main()
