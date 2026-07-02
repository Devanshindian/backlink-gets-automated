#!/usr/bin/env python3
"""
Baseline retrieval + labeling-pool builder for the reuse-check benchmark.

For each benchmark asset it produces TWO things:
  - ranked15 : the baseline retriever's final top-15 (dense blend -> rerank-2.5).
               This is the output whose recall@k we score.
  - pool     : a WIDE candidate set (dense top-POOL_N  ∪  keyword-net) used only
               as the set an LLM will label relevant/not (ground truth). Pooling
               wider than the retriever is what lets us measure pages the baseline
               misses. Keyword-net adds independence from the dense retriever.

Reuses the live Voyage index via rag.py. Resumable (skips assets already written).

Usage: python3 run_baseline.py
"""
import csv, json, os, re, sys, time
import numpy as np
csv.field_size_limit(1 << 24)

HERE = os.path.dirname(os.path.abspath(__file__))            # .../clubbed/_work/bench
WORK = os.path.dirname(HERE)                                 # .../clubbed/_work
sys.path.insert(0, WORK)
import rag                                                   # noqa: E402

REPO = "/Users/devanshmehta/Desktop/SUTRA/backlink-gets-automated"
IDX = os.path.join(WORK, "content-index")
CONTENT = os.path.join(REPO, "projects/testlify/content-database.csv")
BENCH = os.path.join(HERE, "benchmark_assets.json")
TOPIC_KW = os.path.join(WORK, "topic_keywords.json")
OUT = os.path.join(HERE, "retrieval_baseline.jsonl")

POOL_N = 75          # dense candidates pooled for labeling (brief: missed pages sit in top-75)
RERANK_N = 40        # dense candidates fed to the cross-encoder
TOPK = 15            # baseline final output size (the scored list)
MAX_POOL = 120       # cap labeling pool size (generic keywords can match 100s of pages)

LOCALES = {"ar","pl","it","pt-br","no","ja","da","es","de","el","sv","nl","fr",
           "pt","zh","ko","ru","tr","hi","id","th","vi"}
def foreign(u):
    m = re.match(r"https?://(?:www\.)?testlify\.com/([^/]+)/", u)
    return bool(m and m.group(1).lower() in LOCALES)

def query_text(asset):
    a = re.sub(r"\([^)]*\)", " ", asset or "")
    return re.sub(r"\s+", " ", a).strip() or "untitled"

def kw_norm(s):
    return re.sub(r"[^a-z0-9 ]", " ", (s or "").lower())

def main():
    # 1) load index + corpus + keywords
    Vt, Mt = rag.load_vecs(os.path.join(IDX, "title"))
    Vb, Mb = rag.load_vecs(os.path.join(IDX, "body"))
    allurls = [m["url"] for m in Mt]
    uidx = {u: i for i, u in enumerate(allurls)}
    body_uidx = np.array([uidx[m["url"]] for m in Mb])
    cmap, tmap = {}, {}
    for r in csv.DictReader(open(CONTENT, encoding="utf-8")):
        u = (r.get("URL") or "").strip()
        cmap[u] = r.get("Full content", "") or ""
        tmap[u] = r.get("Title", "") or ""
    kw_by_idx = {e["i"]: e.get("keywords", []) for e in json.load(open(TOPIC_KW))}
    assets = json.load(open(BENCH))
    print(f"index {len(allurls)} pages | {len(Vb)} chunks | {len(assets)} bench assets", file=sys.stderr)

    # precompute searchable text (title + url slug) per page for the keyword net
    search_text = {u: kw_norm(tmap.get(u, "") + " " + u) for u in allurls}

    done = set()
    if os.path.exists(OUT):
        for line in open(OUT):
            try: done.add(json.loads(line)["idx"])
            except Exception: pass

    out_f = open(OUT, "a", encoding="utf-8")
    for n, a in enumerate(assets):
        if a["idx"] in done:
            continue
        q = query_text(a["asset"])
        Q = rag.embed([q], "query"); Q /= (np.linalg.norm(Q, axis=1, keepdims=True) + 1e-9)
        qv = Q[0]
        tsim = Vt @ qv
        bsim = Vb @ qv
        bb = np.full(len(allurls), -1.0, dtype=np.float32)
        np.maximum.at(bb, body_uidx, bsim)
        blended = rag.ALPHA * tsim + (1 - rag.ALPHA) * bb
        order = [k for k in np.argsort(blended)[::-1] if not foreign(allurls[k])]
        dense_pool = [allurls[k] for k in order[:POOL_N]]
        rerank_cand = [allurls[k] for k in order[:RERANK_N]]

        # baseline final: rerank the dense top-RERANK_N -> top-K
        docs = [((tmap[u][:200] + "\n" + cmap[u])[:rag.RERANK_DOC_CHARS]).replace("\x00", " ").strip() or "(no content)"
                for u in rerank_cand]
        try:
            ro = rag.rerank(q, docs, min(TOPK, len(rerank_cand)))
            ranked15 = [rerank_cand[i] for i, _ in ro]
        except Exception as e:
            print(f"  asset {a['idx']}: rerank fallback {str(e)[:50]}", file=sys.stderr)
            ranked15 = rerank_cand[:TOPK]

        # keyword net (independent of dense): pages whose title/slug contains a keyword
        kws = [kw_norm(k) for k in kw_by_idx.get(a["idx"], []) if len(kw_norm(k).strip()) >= 4]
        kw_net = []
        if kws:
            for u in allurls:
                if foreign(u):
                    continue
                st = search_text[u]
                if any(k.strip() and k.strip() in st for k in kws):
                    kw_net.append(u)

        # bound the pool: dense top-75 + keyword-net extras (ranked by dense score), capped
        dense_set = set(dense_pool)
        kw_extra = [u for u in kw_net if u not in dense_set]
        kw_extra.sort(key=lambda u: float(blended[uidx[u]]), reverse=True)
        kw_kept = kw_extra[:max(0, MAX_POOL - len(dense_pool))]
        pool = list(dict.fromkeys(dense_pool + kw_kept + ranked15))  # union, ranked15 ⊆ pool
        out_f.write(json.dumps({
            "idx": a["idx"], "asset": a["asset"], "query": q,
            "ranked15": ranked15, "pool": pool,
            "n_dense": len(dense_pool), "n_kw_net": len(kw_net),
            "n_kw_kept": len(kw_kept), "n_pool": len(pool),
        }) + "\n")
        out_f.flush()
        print(f"[{n+1}/{len(assets)}] idx {a['idx']}: ranked15={len(ranked15)} kw_net={len(kw_net)} kept={len(kw_kept)} pool={len(pool)}", file=sys.stderr)
        time.sleep(1.0)   # respect rerank TPM
    out_f.close()
    print("done", file=sys.stderr)

if __name__ == "__main__":
    main()
