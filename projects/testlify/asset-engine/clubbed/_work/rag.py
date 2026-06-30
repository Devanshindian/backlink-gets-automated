#!/usr/bin/env python3
"""
RAG for the asset-engine reuse check (Stages 1 & 2). Improvements over v1:
  - Option B title weighting: separate TITLE vector + BODY (chunked) vectors per page,
    blended at query time:  score = ALPHA*title_sim + (1-ALPHA)*best_body_chunk_sim
  - Clean query: the Asset TITLE only (the verbose "Distinct angle" is dropped).
  - Reranker: dense gives top-N, then Voyage rerank-2.5 picks the final TOPK.

  index    : python3 rag.py index    <content-database.csv> <index_dir>
  retrieve : python3 rag.py retrieve <clubbed-ideas.csv> <index_dir> <content-database.csv>

Key: VOYAGE_API_KEY env var, else first `pa-...` token in ~/.testlify-access.md (never printed).
"""
import csv, json, os, re, sys, time, urllib.request, urllib.error
import numpy as np
from collections import defaultdict
csv.field_size_limit(1 << 24)

EMB_MODEL = "voyage-4-large"     # best general embedding model on the free tier
RERANK_MODEL = "rerank-2.5"      # best reranker on the free tier
ALPHA = 0.5            # title weight in blended score (1-ALPHA = body); tunable
N_RETRIEVE = 40        # dense candidates before reranking (>= TOPK)
TOPK = 15              # RAG candidate LINKS kept per idea (links only — no content stored)
CHUNK_CHARS = 4800
OVERLAP = 600
MAX_ITEMS = 64
MAX_CHARS = 90000
RERANK_DOC_CHARS = 4000   # truncate each candidate for the rerank call

def get_key():
    k = os.environ.get("VOYAGE_API_KEY")
    if k:
        return k
    p = os.path.expanduser("~/.testlify-access.md")
    if os.path.exists(p):
        m = re.search(r'pa-[A-Za-z0-9_\-]{20,}', open(p).read())
        if m:
            return m.group(0)
    sys.exit("no VOYAGE_API_KEY (env or ~/.testlify-access.md)")
KEY = get_key()

def _post(url, body):
    for attempt in range(6):
        try:
            req = urllib.request.Request(url, data=json.dumps(body).encode(),
                headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=180) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            w = 2 ** attempt
            if e.code == 429:
                w = max(w, 15)
            print(f"   HTTP {e.code} retry {w}s {e.read()[:120]!r}", file=sys.stderr); time.sleep(w)
        except Exception as ex:
            print(f"   err {ex} retry", file=sys.stderr); time.sleep(2 ** attempt)
    raise RuntimeError("voyage call failed after retries")

def embed(texts, input_type):
    texts = [t if (t and t.strip()) else "untitled" for t in texts]   # Voyage 400s on empty strings
    out, i = [], 0
    while i < len(texts):
        batch, chars = [], 0
        while i < len(texts) and len(batch) < MAX_ITEMS and chars + len(texts[i]) <= MAX_CHARS:
            batch.append(texts[i]); chars += len(texts[i]); i += 1
        if not batch:
            batch = [texts[i][:MAX_CHARS]]; i += 1
        d = _post("https://api.voyageai.com/v1/embeddings",
                  {"input": batch, "model": EMB_MODEL, "input_type": input_type})
        out.extend(e["embedding"] for e in sorted(d["data"], key=lambda x: x["index"]))
        time.sleep(0.2)
    return np.asarray(out, dtype=np.float32)

def rerank(query, docs, top_k):
    d = _post("https://api.voyageai.com/v1/rerank",
              {"query": query, "documents": docs, "model": RERANK_MODEL,
               "top_k": top_k, "return_documents": False})
    return [(r["index"], r["relevance_score"]) for r in d["data"]]

def chunks(text):
    text = (text or "").strip()
    if not text:
        return []
    if len(text) <= CHUNK_CHARS:
        return [text]
    out, s = [], 0
    while s < len(text):
        out.append(text[s:s + CHUNK_CHARS]); s += CHUNK_CHARS - OVERLAP
    return out

# ---------------- INDEX ----------------
def load_pages(content_csv):
    pages = []
    with open(content_csv, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            url = (row.get("URL") or "").strip()
            title = (row.get("Title") or "").strip()
            fc = (row.get("Full content") or "").strip()
            if url and fc:                       # only pages with real content can be reuse candidates
                pages.append((url, title, fc))
    return pages

def do_index(content_csv, idx_dir):
    pages = load_pages(content_csv)
    print(f"index: {len(pages)} pages with content", file=sys.stderr)

    # --- TITLE index: one vector per page (cheap, one shot) ---
    tdir = os.path.join(idx_dir, "title")
    if os.path.exists(os.path.join(tdir, "vectors.npy")):
        print("title index already present, skipping", file=sys.stderr)
    else:
        os.makedirs(tdir, exist_ok=True)
        tvecs = embed([t if t else u for u, t, fc in pages], "document")
        np.save(os.path.join(tdir, "vectors.npy"), tvecs)
        with open(os.path.join(tdir, "meta.jsonl"), "w", encoding="utf-8") as f:
            for u, t, fc in pages:
                f.write(json.dumps({"url": u, "title": t}) + "\n")
        print("title index done", file=sys.stderr)

    # --- BODY index: chunked, resumable ---
    bdir = os.path.join(idx_dir, "body")
    os.makedirs(os.path.join(bdir, "parts"), exist_ok=True)
    state_p = os.path.join(bdir, "state.json")
    meta_p = os.path.join(bdir, "meta.jsonl")
    state = json.load(open(state_p)) if os.path.exists(state_p) else {"done": [], "part": 0}
    done = set(state["done"])
    todo = [(u, t, fc) for u, t, fc in pages if u not in done]
    print(f"body index: {len(todo)} pages to embed ({len(done)} done)", file=sys.stderr)
    meta_f = open(meta_p, "a", encoding="utf-8")
    buf, buf_chunks = [], 0

    def flush():
        nonlocal buf, buf_chunks
        if not buf:
            return
        texts, metas = [], []
        for u, t, fc in buf:
            for ci, ch in enumerate(chunks(fc)):
                texts.append(ch); metas.append({"url": u, "title": t, "chunk": ci})
        vecs = embed(texts, "document")
        np.save(os.path.join(bdir, "parts", f"part_{state['part']:05d}.npy"), vecs)
        for m in metas:
            meta_f.write(json.dumps(m) + "\n")
        meta_f.flush()
        state["part"] += 1
        state["done"].extend(u for u, _, _ in buf)
        json.dump(state, open(state_p, "w"))
        print(f"   flushed {len(buf)} pages / {len(texts)} chunks (done {len(state['done'])})", file=sys.stderr)
        buf, buf_chunks = [], 0

    for p in todo:
        buf.append(p); buf_chunks += len(chunks(p[2]))
        if buf_chunks >= MAX_ITEMS:
            flush()
    flush()
    meta_f.close()
    print("body index done", file=sys.stderr)

# ---------------- RETRIEVE ----------------
def load_vecs(subdir):
    vp = os.path.join(subdir, "vectors.npy")
    if os.path.exists(vp):
        V = np.load(vp)
    else:
        parts = sorted(os.listdir(os.path.join(subdir, "parts")))
        V = np.concatenate([np.load(os.path.join(subdir, "parts", p)) for p in parts], axis=0)
    M = [json.loads(l) for l in open(os.path.join(subdir, "meta.jsonl"), encoding="utf-8")]
    assert len(M) == len(V), f"{subdir}: meta {len(M)} != vecs {len(V)}"
    V = V.astype(np.float32)
    V /= (np.linalg.norm(V, axis=1, keepdims=True) + 1e-9)
    return V, M

def do_retrieve(clubbed_csv, idx_dir, content_csv):
    Vt, Mt = load_vecs(os.path.join(idx_dir, "title"))
    Vb, Mb = load_vecs(os.path.join(idx_dir, "body"))
    urls = [m["url"] for m in Mt]                       # title order == page order
    uidx = {u: i for i, u in enumerate(urls)}
    body_uidx = np.array([uidx[m["url"]] for m in Mb])  # url-index per body chunk
    print(f"retrieve: {len(urls)} pages | {len(Vb)} body chunks", file=sys.stderr)

    cmap, tmap = {}, {}
    for row in csv.DictReader(open(content_csv, encoding="utf-8")):
        u = (row.get("URL") or "").strip()
        cmap[u] = (row.get("Full content") or ""); tmap[u] = (row.get("Title") or "")

    with open(clubbed_csv, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f); fields = reader.fieldnames; rows = list(reader)

    # CLEAN query = Asset title, with parenthetical feature/qualifier detail stripped
    # (e.g. "... Benchmark Report (Adoption, Completion, AI Cheating)" -> "... Benchmark Report").
    # The parenthetical is mini-angle noise that drags retrieval off-topic.
    def query_text(r):
        a = re.sub(r"\([^)]*\)", " ", (r.get("Asset") or ""))
        a = re.sub(r"\s+", " ", a).strip()
        return a or (r.get("Asset") or "").strip() or (r.get("Distinct angle") or "").strip() or "untitled"
    queries = [query_text(r) for r in rows]
    Q = embed(queries, "query"); Q /= (np.linalg.norm(Q, axis=1, keepdims=True) + 1e-9)

    for n, r in enumerate(rows):
        q = Q[n]
        tsim = Vt @ q                                   # per page
        bsim = Vb @ q                                   # per body chunk
        bestbody = np.full(len(urls), -1.0, dtype=np.float32)
        np.maximum.at(bestbody, body_uidx, bsim)        # best chunk per page
        blended = ALPHA * tsim + (1 - ALPHA) * bestbody
        cand = [urls[k] for k in np.argsort(blended)[::-1][:N_RETRIEVE]]
        # rerank the dense top-N with the cross-encoder
        docs = [((tmap[u][:200] + "\n" + cmap[u])[:RERANK_DOC_CHARS]) for u in cand]
        order = rerank(queries[n] or r.get("Asset", ""), docs, min(TOPK, len(cand)))
        top = [(cand[i], sc) for i, sc in order]
        # LINKS ONLY — we store the candidate links, not their content. Any step that needs the
        # page text (Stage-3 judge, content creation) fetches it on demand: look it up by URL in
        # content-database.csv (already holds Full content) or web-fetch the live page.
        r["RAG candidates"] = "; ".join(f"{tmap[u]} — {u} ({sc:.2f})" for u, sc in top)
        if (n + 1) % 50 == 0:
            print(f"   retrieved {n+1}/{len(rows)}", file=sys.stderr)

    with open(clubbed_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)
    print(f"retrieve: wrote candidates for {len(rows)} ideas", file=sys.stderr)

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "index":
        do_index(sys.argv[2], sys.argv[3])
    elif cmd == "retrieve":
        do_retrieve(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        sys.exit("unknown command")
