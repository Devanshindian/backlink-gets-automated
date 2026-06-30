# G3 merge — cluster competitor-derived assets into distinct, buildable IDEAS (Testlify)

You are doing the **intelligent merge** step of a competitor study. Input is a list of proposed assets (each
is "the thing WE would build" that a per-page reasoning pass already wrote, one per competitor page that earns
backlinks). Many describe the **same build** in different words. Your job: **cluster them into the real
distinct ideas, by judgment** — NOT by string matching.

## Input
A TSV file (path given to you): columns `RowID  BrandFit  Domains  Asset`. All rows share ONE format (e.g. all
"Free test", all "Glossary"). So you're clustering within a format — group by the underlying **build / subject**.

## The merge rule
- For any two assets ask: **"Would ONE asset we build satisfy both?"** Yes → same idea. No → split.
- **When in doubt, SPLIT.** A tight buildable idea beats a fuzzy one covering three things.
- Keep genuinely distinct subjects separate (a Python skills test ≠ a Java skills test ≠ an AI-roles skills
  test — different builds). But a "Python Skills Test" and a "Python Coding Assessment (live editor)" ARE one idea.
- **No target number of clusters.** Could be 10, could be 80. The right number is whatever the data contains.
  World-class precision: no lazy lumping, no needless splitting.

## For each cluster output
- `idea` — one clean canonical asset name (pick/refine the best member name; a real working title, not "<Format> on <Topic>").
- `brand_fit` — the dominant fit among members (CORE / TRANSPLANT / ADJACENT).
- `our_subject` — a short subject label (e.g. "Skills tests — coding & technical").
- `member_rowids` — **every** RowID in the cluster (as strings). Every input RowID must appear in exactly one cluster.

## Output — JSONL
Write to the output path given to you (`g3_ideas/<slug>.jsonl`), one JSON object per line:
`{"idea":"...","brand_fit":"CORE","our_subject":"...","member_rowids":["12","87",...]}`
Use a python heredoc with json.dumps. After writing, verify every input RowID is covered exactly once and
reply only: `<slug> done: <K> ideas from <N> rows (all covered: yes/no)`.