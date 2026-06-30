# RAG Improvement Brief — Reuse-Check Retrieval

*A briefing for a RAG specialist. What the system does, what we're trying to improve, every approach we've
tried and why it failed, how we measured, and the problem statement to solve.*

Last updated: 2026-06-30.

---

## 1. TL;DR / Problem statement (full version at the end)

We run a **reuse-check**: given a proposed content asset (a marketing title), retrieve the existing pages on
our own site that are relevant, so we can decide *reuse / improve / build-from-parts / brand-new* and show a
human everything we already own on that topic.

**The problem: recall.** On a 49-asset benchmark against independent LLM relevance labels, our best retriever
gets **recall@15 ≈ 0.64** — it misses ~36% of the genuinely-relevant pages. The corpus is content-rich and
semantically self-overlapping (a topic like "psychometric tests" has ~15 near-sibling pages; the broader
"assessment/hiring" neighbourhood has hundreds), and the asset queries are long, specific marketing titles.
A cross-encoder reranker optimises precision-to-query, which structurally caps recall of pages that are
*on-topic but off the asset's specific angle*. **We need to lift recall without wrecking precision.** We have
already disproven the obvious levers (query rewriting, BM25 hybrid, MMR, best-chunk) on the benchmark.

---

## 2. What the system does

**Input:** one proposed asset = a title string, e.g. *"Psychometric Tests for Hiring: Which Type Predicts
What, by Role (with Validity Data & Sample Items)"*.

**Goal (two jobs, and they conflict):**
- **(A) Precision — "is this exact asset already built?"** Find the closest few existing pages so an LLM can
  judge a verdict (Already-have / Improve / Build-from-parts / Brand-new).
- **(B) Recall — "what do we already own on this topic?"** Show a human *all* related existing pages (to reuse,
  improve, interlink). This is the job that's failing.

**Pipeline (current baseline):**
1. **Index** every page twice with **Voyage `voyage-4-large`**: a **title vector** (the title embedded alone)
   and **body vectors** (full content chunked at ~4,800 chars, 600 overlap), each chunk tagged to its page.
2. **Query** = the asset title with parenthetical/sub-angle stripped (e.g. → *"Psychometric Tests for Hiring:
   Which Type Predicts What, by Role"*). Embedded as a query vector.
3. **Blended dense score per page:** `score = α·cos(query, title_vec) + (1−α)·max_chunk cos(query, body_chunk)`,
   α = 0.5. Take top-N (30–40) pages.
4. **Rerank** the top-N with **Voyage `rerank-2.5`** (cross-encoder, query + page text) → keep top-K (7, now 15).
5. The top-K **links** are stored; page text is fetched on demand. An LLM judge reads the top candidates' full
   text and writes the verdict.

**Corpus:** a WordPress site, **~10,085 pages total → ~9,520 English** (565 foreign-language translation
duplicates excluded by URL locale prefix) → **~9,669 with usable `Full content`** after a coverage fix
(see §4). Page types: blog posts, glossary terms, a 3,500-test product library, competitor-comparison pages,
integrations, etc. Heavy near-duplication and sub-topic overlap is the defining property of this corpus.

**Stack constraints:** Voyage AI free tier (voyage-4-large embeddings + rerank-2.5; rerank has a ~2M tokens/min
limit we already hit). No fine-tuning infra assumed. ~9.5k docs — small enough to brute-force, large enough that
the relevant-set-per-query overlap matters.

---

## 3. How we measure (the evaluation harness)

To avoid tuning to anecdotes, we built an offline benchmark:

- **Sample:** 50 assets stratified across our three idea sources (36 competitor-derived, 6 Reddit-derived,
  8 adjacent-niche). 49 scored (1 dropped on a data error).
- **Ground truth (independent of the retriever under test):** for each asset we pool candidates from *both*
  retrieval variants + a lexical keyword net, then an **LLM labels each pooled page relevant / not** by a rubric
  ("would a content strategist want to see this when building this asset — to reuse/improve/link/avoid
  duplicating; same subject = relevant; generic word overlap or different subject = not"). We strengthened this
  pass (v2) from 220-char snippets to 900-char content + a tighter rubric; results held.
- **Avg ground-truth set size: ~19.2 relevant pages per asset** (the relevant set is large — this is central).
- **Metrics:** recall@10, recall@15, precision@10, and per-asset head-to-head.

> Caveat we're aware of: the ground-truth pool is seeded partly by the retrievers + a keyword net, so it can
> under-count truly-relevant pages that *no* method surfaces. It is, however, a fair *relative* comparison
> (same labels for every method) and the keyword net adds independence.

---

## 4. What works (keep / not the problem)

- **Baseline retrieval** (full-title query → blended dense → rerank-2.5 → top-K): the strongest of everything
  tried. recall@15 ≈ 0.64, precision@10 ≈ 0.81.
- **Coverage re-scrape (data fix, big win):** the WordPress REST API returns empty `content` for page-builder /
  custom-template post types — ~2,700 pages (incl. the entire test-library) had blank content and were invisible
  to retrieval. Fix: fall back to fetching the live HTML and extracting visible text. **Coverage 73% → 95%
  (+2,332 pages).** This was a data-completeness bug, not a retrieval-algorithm issue.
- **Foreign-language filter:** exclude translation duplicates (URL first segment is an ISO language code,
  confirmed by a matching English-slug twin). Removes 565 dupes that wasted result slots.
- **Deterministic topic catalogue (companion for job B):** a non-semantic keyword lookup — an LLM tags each
  asset's distinctive topic term(s), then we list *every* English page whose title/URL contains that term (with
  light stemming so screening/screener/screen match; over-generic terms dropped). This **guarantees completeness
  by definition** (e.g. all 15 "psychometric" pages) and is what we ship alongside the RAG. Its limit: purely
  literal — it misses synonyms (a psychometric page titled only "Personality Assessment" won't match
  "psychometric"). It's a band-aid for recall, not a semantic solution.

---

## 5. Everything we tried to improve recall — and why each failed

All measured on the 49-asset benchmark (except where noted). The baseline beat every retrieval variant.

| # | Approach | Hypothesis | Result | Why it failed |
|---|---|---|---|---|
| 1 | **Best-chunk rerank** — feed the reranker each page's *best-matching chunk* instead of the page head | a long landing page wins on a keyword-stuffed intro; show the reranker the actually-matching passage | **Worse** (A/B on the psychometric query: the broad "aptitude" pillar page went head-rank #9 → chunk-rank **#1**; a focused "types of psychometric tests" blog went #4 → #9) | A comprehensive/pillar page's *best* passage is an *even stronger* point-match than its intro. Best-chunk **amplifies** broad pages and buries focused ones — opposite of intended. |
| 2 | **Short query** — truncate the asset title at the first colon | the long title over-specifies; the topic is the part before the colon | **Overfit** — won the 2 hand-picked examples, lost across 50 | Mechanical truncation is arbitrary; helped the cherry-picked cases, hurt the average. |
| 3 | **LLM-crafted short query** — an LLM rewrites the title into a clean topic phrase | a smart topic query retrieves the topic neighbourhood better | **Worse, decisively:** full-title vs LLM-query → recall@15 **0.644 vs 0.530**, precision@10 **0.81 vs 0.69**, head-to-head **28–6** for full title | Shortening **removes disambiguating signal**. The full title's qualifiers/angle help the embedder + reranker lock onto the right neighbourhood; a generic topic query pulls broad/popular pages instead. |
| 4 | **BM25 + RRF hybrid** — add a lexical (keyword) ranker, fuse with dense via reciprocal-rank-fusion | dense misses exact-term matches; BM25 guarantees them; fuse for recall | **No measurable gain** | The missed pages were **already in the dense candidate pool** — they were *ranked below the cutoff*, not absent. BM25 surfaced nothing new for these queries; it re-ordered without adding relevant pages. |
| 5 | **MMR diversity re-rank** — penalise near-duplicates so one cluster can't fill all slots | the top slots are hogged by one sub-topic cluster; force variety | **No gain** | Forcing diversity pulled in *off-topic* pages (e.g. an HR-ops "selection tests for HRM" page into a psychometric result set) without surfacing the missed *on-topic* pages. Re-ordered noise. |
| 6 | **Top-K 7 → 15** (show more) | the relevant set is ~19; 7 slots can't hold it | **Partial** — more relevant pages appear, but borderline off-angle pages remain and several relevant pages still sit beyond #15 | Helps mechanically but doesn't address *why* relevant pages rank low; just widens the window. |

### Why the relevant pages rank low (the core diagnostic)
Tracing the "missed" pages for the two canonical assets (§6), they are **in the dense top-75 candidate pool**
and the **reranker scores them 0.54–0.74** (well above any floor) — but they land at **rerank ranks #15–33**,
below the display/judge cutoff. The reranker is *correctly* ranking them below the pages that match the asset's
**specific angle**. The relevant *set* per asset is large (~19) and spans **multiple sub-angles** of the topic;
the asset query encodes one specific angle; so genuinely-relevant pages on *other* sub-angles are demoted by an
instrument doing exactly its job (precision to the query). A *smarter* reranker would, if anything, demote them
*more* confidently. This is a **precision-tool / recall-need mismatch**, not a reranker-quality problem.

---

## 6. Two canonical failure cases (concrete)

**Case A — Psychometric.** Asset: *"Psychometric Tests for Hiring: Which Type Predicts What, by Role."*
We own **15** clearly-relevant psychometric pages (predict-performance, value, enhance-accuracy, hire-top-talent,
reduce-turnover, types, glossary, the "Best Psychometric Tests" hub, etc.).
- Baseline RAG surfaced **3/15 at top-7, 7/15 at top-15.**
- The missed pages rank #17–33 in the reranker (in the pool, scored 0.66–0.74) — crowded out by *cognitive
  ability* and *aptitude* pages (true test-types matching "which **type** predicts") and a couple of off-topic
  pages (an HR-ops "selection tests for HRM" page).
- The missed psychometric pages are about *other sub-angles* (turnover, performance, accuracy) than the asset's
  "which type predicts what."

**Case B — Resume.** Asset: *"AI Resume Screening vs Skills Testing: An Independent Accuracy Benchmark."*
We own 4 resume-screening pages (incl. `/ai-resume-screener/`, `/resume-screening-techniques/`).
- Baseline RAG surfaced **0/4 at top-7** (they ranked #15–33).
- The asset is a *comparison/benchmark*, so the reranker (correctly) favours comparison + skills-testing pages;
  the pure resume-screening explainers are a weaker match to *this* framing and fit sibling assets better.
- One page (`/ai-resume-screener/`) even dropped out of the candidate net under the hybrid config (title says
  "screen**er**", query/keyword said "screen**ing**" — a stemming gap).

In both cases the human reviewer's complaint is *recall/completeness* ("we own tons of these, show them all"),
which is **job B**, while the tuned system optimises **job A** (precision to the asset's angle).

---

## 7. What we learned (so you don't re-walk it)
1. **Query rewriting is a dead end here** — full title > short > LLM-short, robustly across two ground-truth
   versions. More query signal helps; less hurts.
2. **The missed pages are retrieved-but-demoted, not absent** — so the bottleneck is *ranking/selection under a
   large relevant set*, not first-stage recall (with N≥75 they're in the pool).
3. **Cross-encoder rerank is precision-oriented** — it can't be coaxed into recall of off-angle-but-on-topic
   pages by swapping models; the relevance *criterion* (query-match) is the constraint.
4. **A deterministic keyword catalogue solves completeness but not semantics** — it's our current shipped
   workaround; it misses synonyms and isn't a real retrieval fix.
5. **Evaluate on the 49-asset harness, not anecdotes** — we nearly shipped 2 overfit changes; the benchmark
   caught them.

---

## 8. Constraints / context for solutions
- Embeddings + reranker via **Voyage free tier** (voyage-4-large, rerank-2.5; rerank ~2M TPM cap — batching
  matters). Open to other providers/local models if justified.
- ~9.5k docs; full re-index is feasible. Page text is available (title + full content).
- Two distinct consumers: an **LLM judge** (wants the *most relevant* few, precision) and a **human catalogue
  view** (wants *all on-topic*, recall). A solution can serve them differently.
- Latency is not critical (offline batch). Cost is moderate (free-tier limits).

---

## 9. Problem statement (the ask)

> On a ~9.5k-page corpus with heavy sub-topic and near-duplicate overlap, our reuse-check retriever (Voyage
> dense + rerank-2.5, query = full asset title) achieves only **recall@15 ≈ 0.64** against LLM ground truth,
> because the **relevant set per query is large (~19 pages) and spans multiple sub-angles**, while the query
> encodes one specific angle — so a precision-oriented cross-encoder structurally demotes on-topic / off-angle
> pages to ranks #15–33. Query rewriting, BM25+RRF hybrid, MMR, and best-chunk reranking have all been
> benchmarked and **do not help** (details above).
>
> **How do we lift recall of the topically-relevant pages without sacrificing the precision the verdict needs?**
> Specifically, we'd value your read on:
> 1. Is this better framed as **multi-query / query-decomposition** (expand the asset into its sub-angles and
>    union the retrievals), **HyDE / generated-doc retrieval**, **multi-vector / late-interaction (ColBERT-style)**,
>    a **fine-tuned or differently-prompted reranker**, or **cluster/topic-level retrieval**?
> 2. Is the real fix at **indexing/representation** (e.g. per-section embeddings, topic tagging, a learned
>    topic taxonomy) rather than at query/rerank time?
> 3. Given two consumers (precision for the LLM judge, recall for the human catalogue), should these be **two
>    separate retrieval paths** rather than one ranked list — and if so, what's the right recall-path design
>    beyond our literal keyword catalogue (e.g. embedding-based topic clustering)?
> 4. What would you measure differently? (Our ground truth is pool-seeded; is there a better cheap label source?)

Repo with the recipes + code: https://github.com/Devanshindian/backlink-gets-automated
(retrieval implementation: `projects/testlify/asset-engine/clubbed/_work/rag.py`; full spec:
`workflows/01-asset-engine/reuse-check.md`).
