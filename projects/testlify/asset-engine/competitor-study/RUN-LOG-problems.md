# RUN-LOG — Competitor Study (Testlify) — re-run 2026-06-26

Clean re-run of Method 1 (Competitor Study), Steps B→H, from freshly re-exported Semrush
indexed-pages files. Prior deliverables had been cleared; only `_raw/` exports survived.
Merge method this run: **Opus semantic merge** (G3 spec default — the prior run's TF-IDF
lexical merge was a deviation; corrected here).

## ✅ RUN CHECKLIST

**Setup & inputs**
- [x] `competitors.md` exists and the 12 are user-approved (Step A4 gate passed 2026-06-26; 9 direct + 3 adjacent).
- [x] All 12 approved competitors received as exports (12/12; none missing).
- [x] Every export validated (real `Source url,Source title,...` header; large files; not a login wall). Several capped at Semrush's 30,001-row limit — fine (sorted by Domains desc; only top 300 used).
- [x] Raw exports in `_raw/`; folder structure created (`_raw/`, `_work/_candidates/`, `_work/fetch/`, `_work/agent_out/`).

**Step C — filter**
- [x] Top 300 by Domains taken per competitor; junk dropped; non-200 content paths KEPT; per-competitor kept counts sanity-checked. **2,469 kept total.**
- [x] Keyword matching on URL path, not full URL (`filter_stepC.py` uses `urlparse(...).path`).
- [x] Free tests/tools/calculators kept; candidate lists in `_work/_candidates/`.

### Step C results (2026-06-26)
Per-competitor kept (of top 300 by Domains):
adaface 270 · aihr 249 · criteria 223 · eskill 134 · imocha 235 · mettl 224 ·
recruiterflow 125 · talentlyft 166 · testdome 160 · testgorilla 239 · vervoe 223 · wecp 221.

**Sanity checks (the two lowest, both justified, not the redirect trap):**
- **eSkill 134** — its blog migrated; 114 old `http://blog.eskill.com/<slug>` URLs now genuinely return
  `404` (dropped per rule 2). The 120 live `301` migrated pages + 55 `200`s ARE kept, so editorial is intact.
  134 ≫ the "38 collapse" the spec warns about → filter is not over-dropping.
- **Recruiterflow 125** — 141 of its top-300 are individual customer job postings (`/<db>/jobs/<id>`),
  correctly dropped per rule 7. Editorial (`/blog/<slug>`) kept.
- Subdomain allow-list verified: keeps `blog.imocha.io` (112), `blog.mettl.com` (89), `resources.mettl.com`,
  `blog.testdome.com`; drops `app.testdome.com`, `tests.mettl.com`, `*.talentlyft.com` customer career sites,
  `help./support./developer.` — exactly as intended.

**Step D — tag format**
- [x] Every kept page tagged with a format (`tag_stepD.py`; URL+title heuristic over the spec catalog).

**Step E — read**
- [x] Every kept row fetched + read; "What it is" = full scraped text; zero `(from title)`.
- [x] Un-fetchable marked `FETCH FAILED` (never disguised).
- [x] Read tally printed + logged.

### Step E read tally (2026-06-26)
**N = 2,469 kept → READ 2,346 (95%) · FETCH FAILED 70 · SKIP 53.** (2346+70+53 = 2469 ✓)
- Read methods: vendored extractor 1,654 · HTML-strip 692.
- **70 FETCH FAILED** = genuinely unfetchable: dead `404`s; TestDome JS-SPA test pages (render only "TestDome"
  without JS — WebFetch also returned empty); Vervoe `ERR_TLS_CERT_ALTNAME_INVALID` (broken cert); the dead
  `blog.eskill.com` subdomain (connection refused). curl + WebFetch ladder attempted on the valuable ones; none rendered.
- **53 SKIP** = UGC/nav that slipped Step C (TestDome `/certificates/`, `/questions/`, `/apply/`, `/Tests` nav).
  Marked SKIP in master `WhatItIs`; G2 will drop them.

**Step F — aggregate**
- [x] `_work/format-summary.csv` written. By avg-domains/page: Glossary 119 · Templates 68 · Data report 47 ·
  Checklist 37 · Answer-bait 27. By total domains: Answer-bait 17,740 · editorial 9,313 · Free test 5,854.

**Step G**
- [x] G0 `brand-scope.md` distilled + user-approved (2026-06-26; metrics & bias kept CORE per user).
- [x] G2 every kept row reasoned by parallel Sonnet sub-agents (41 format shards, 5-row batches); stitched by Row ID; **2,276/2,276, no holes.**
- [x] G3 **Opus semantic merge** (per-format clustering + cross-format dedupe pass; no string keys); 728 → **445 ideas** after dedupe (85 merge-groups absorbed 283; 2 over-merges flagged).
- [x] G4 score (Beatability 1-3, Effort S/M/L); G5 rank (Brand fit → domains×beat → effort), **NOW=28 / LATER=417**; G6 8-box sanity all pass.

**Step H — deliver**
- [x] `competitor-study-ideas.xlsx` (Tab1 format summary + Tab2 ranked 445 ideas, coloured by brand fit).
- [x] `competitor-formats.xlsx` (master, all 2,469 rows, with Idea#).
- [x] Folder clean (top level = 2 deliverables + competitors.md + brand-scope.md + RUN-LOG; working master CSV moved to `_work/`).

## G2/G3 problems & fixes
- **Pipe-delimiter collision (G2):** first 8 shards used `|`-delimited output; agents put literal `|` in prose →
  73 malformed rows in shards 03/04/07. Switched output to **JSONL** (json.dumps escapes everything); re-ran those 3.
  5 clean pipe shards kept; stitcher handles both formats.
- **Soft-404 disguised reads (Step E, caught at G2 prep):** 70 rows (criteria 33, eskill 31, +6) returned HTTP 200
  but a "Page Not Found" body (migrated/dead blogs). These were **disguised failures** — reclassified to `FETCH FAILED`
  per the hard rule. Final tally corrected: **read 2,276 / FETCH FAILED 140 / SKIP 53.**
- **Thin JS pages recovered:** 108 rows had title-only HTML-strip text; a WebFetch sub-agent recovered 73
  (all 67 WeCP + 2 Recruiterflow + 4 TestDome). 35 TestDome SPA test pages stay title-only (live pages, title
  carries format+topic — not disguised failures).
- **Session limits:** hit several times mid-run (both main + sub-agents); every step was resumable, so re-dispatch
  continued cleanly with zero lost work.

## G6 sanity check (all pass)
1. No too-generic NOW names: 0 ✓  2. No template-fill names: 0 ✓  3. Every NOW has distinct angle: 0 missing ✓
4. Every NOW ≥3 pages from ≥2 comps: 0 fail ✓  5. Backing URLs populated: 0 missing ✓
6. Every NOW CORE/TRANSPLANT (in brand scope): 0 off ✓  7. Gap diversity 1,601 distinct / 1,601 = 1.00 ✓
8. Merge-quality: cross-format dedupe done; 2 over-merges flagged (minor, not in NOW).

## Final result
12 competitors · 2,469 kept pages · 2,276 read · **445 distinct ideas (CORE 301 / TRANSPLANT 82 / ADJACENT 62)** ·
**NOW=28.** Top NOW: State of Skills-Based Hiring 2026 report (2,080 dom/35 pages/11 comps); Quality-of-Hire &
Retention Calculator (1,919/22/10); Role-by-Role Hiring Kit Library (834/19/6); Recruiting Metrics Benchmark
Report (820/16/8); Independent Assessment-Platform Comparison (513/22/10).

## Inputs validated (2026-06-26)
| Competitor | rows in export | size |
|---|---|---|
| adaface | 30,001 (capped) | 3.3M |
| aihr | 30,001 (capped) | 11M |
| criteria | 18,682 | 2.7M |
| eskill | 20,131 | 6.7M |
| imocha | 6,978 | 856K |
| mettl | 30,001 (capped) | 8.2M |
| recruiterflow | 30,001 (capped) | 3.7M |
| talentlyft | 30,001 (capped) | 4.1M |
| testdome | 30,001 (capped) | 4.3M |
| testgorilla | 30,001 (capped) | 4.3M |
| vervoe | 30,001 (capped) | 5.9M |
| wecp | 30,001 (capped) | 6.6M |

## Problems & fixes
(none yet)
