#!/usr/bin/env python3
"""
Freeze the reuse-check benchmark sample: a stratified draw of assets from the
clubbed pool, matching the RAG-improvement-brief's split (≈36 competitor / 8
other-niche / 6 reddit = 50; brief scored 49 after one data drop).

Deterministic: fixed seed, so the same sample is reproducible across machines.
Output: benchmark_assets.json  — [{idx, asset, angle, format, source}]

Usage: python3 sample_benchmark.py <clubbed-ideas-review.csv> <out.json>
"""
import csv, json, random, sys
csv.field_size_limit(1 << 24)

SEED = 20260630
# target per source-method (caps to availability)
QUOTA = {"Competitor": 36, "Other-niche": 8, "Reddit": 6}

def main(clubbed_csv, out_path):
    rows = list(csv.DictReader(open(clubbed_csv, encoding="utf-8")))
    by_src = {}
    for i, r in enumerate(rows):
        src = (r.get("Source method") or "?").strip()
        by_src.setdefault(src, []).append(i)

    rng = random.Random(SEED)
    picked = []
    for src, want in QUOTA.items():
        pool = by_src.get(src, [])
        take = pool if len(pool) <= want else rng.sample(pool, want)
        picked.extend(sorted(take))

    sample = []
    for i in sorted(picked):
        r = rows[i]
        sample.append({
            "idx": i,
            "asset": (r.get("Asset") or "").strip(),
            "angle": (r.get("Distinct angle") or "").strip(),
            "format": (r.get("Format") or "").strip(),
            "source": (r.get("Source method") or "").strip(),
        })

    json.dump(sample, open(out_path, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    from collections import Counter
    dist = Counter(s["source"] for s in sample)
    print(f"sampled {len(sample)} assets -> {out_path}")
    print("by source:", dict(dist))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
