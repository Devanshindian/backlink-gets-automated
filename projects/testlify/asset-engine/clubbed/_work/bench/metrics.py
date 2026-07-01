#!/usr/bin/env python3
"""
Retrieval metrics for the reuse-check benchmark.

Given, per asset:
  - relevant: set of URLs an LLM labelled relevant (ground truth)
  - ranked:   list of URLs the retriever returned, best-first
compute recall@k, precision@k. Aggregate = macro-average over assets
(every asset weighted equally, matching the brief's reporting).

URLs are normalised (strip scheme/trailing slash/locale) so that
http vs https and trailing-slash differences don't cause false misses.
"""
import re

def norm_url(u):
    u = (u or "").strip().lower()
    u = re.sub(r"^https?://", "", u)
    u = re.sub(r"^www\.", "", u)
    return u.rstrip("/")

def recall_at_k(relevant, ranked, k):
    rel = {norm_url(u) for u in relevant if u}
    if not rel:
        return None  # undefined — caller drops these from the macro-average
    topk = {norm_url(u) for u in ranked[:k]}
    return len(rel & topk) / len(rel)

def precision_at_k(relevant, ranked, k):
    rel = {norm_url(u) for u in relevant if u}
    topk = [norm_url(u) for u in ranked[:k]]
    if not topk:
        return 0.0
    hits = sum(1 for u in topk if u in rel)
    return hits / min(k, len(topk))

def evaluate(per_asset, ks=(10, 15)):
    """per_asset: list of {asset, relevant:[urls], ranked:[urls]}.
    Returns macro-averaged recall@k / precision@k over assets with a
    non-empty relevant set, plus n scored."""
    out = {}
    scored = [a for a in per_asset if {norm_url(u) for u in a["relevant"] if u}]
    n = len(scored)
    for k in ks:
        rec = [recall_at_k(a["relevant"], a["ranked"], k) for a in scored]
        prec = [precision_at_k(a["relevant"], a["ranked"], k) for a in scored]
        out[f"recall@{k}"] = round(sum(rec) / n, 4) if n else None
        out[f"precision@{k}"] = round(sum(prec) / n, 4) if n else None
    out["n_assets_scored"] = n
    out["avg_relevant_set"] = round(
        sum(len({norm_url(u) for u in a["relevant"] if u}) for a in scored) / n, 2
    ) if n else None
    return out

if __name__ == "__main__":
    # tiny self-test
    demo = [{
        "asset": "demo",
        "relevant": ["https://x.com/a/", "https://x.com/b", "https://x.com/c"],
        "ranked": ["http://x.com/a", "https://x.com/z", "https://www.x.com/b/"],
    }]
    print(evaluate(demo, ks=(2, 3)))
    # relevant={a,b,c}; ranked=[a, z, b]. recall divides by |relevant|=3:
    #   recall@2 = |{a}|/3 = 0.333 ; recall@3 = |{a,b}|/3 = 0.667
    #   precision@2 = |{a}|/2 = 0.5 ; precision@3 = |{a,b}|/3 = 0.667
