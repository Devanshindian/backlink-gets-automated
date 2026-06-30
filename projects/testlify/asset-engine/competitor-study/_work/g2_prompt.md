# G2 sub-agent task — per-row reasoning (Competitor Study, Testlify)

You are **Testlify** (brand scope below). Each row in your shard is a page from a **competitor** that already
earns backlinks — and it earns them because of its **format** (its shape: glossary, free test, data report,
calculator…), not its exact topic. Your job, for each page: look at what they built and the proof it pulls
links, then design the asset **WE** would build — **the same winning format, but on a subject we can own (per
the brand scope), and better than theirs.** Steal the shape, never the topic.

## How to run (IMPORTANT — read carefully)
- Your shard file is `g2_shards/shard_NN.csv` (columns: `RowID,Competitor,URL,Format,Domains`). NN is given to you.
- For each row, **read the full page text** from `fetch/<RowID>.json` (the `text` field — the complete scraped
  page saved in Step E). This is what you reason against. Never reason from the URL/title alone.
- **Work in batches of 5 rows.** Read 5 rows' page text, reason each one individually, emit 5 output lines,
  then move to the next 5. Do NOT pattern-match across a big block — read each page on its own. If you process
  more than 5 at once you WILL go generic, which is the one failure this method exists to prevent.
- **Write your output incrementally** to `agent_out/shard_NN.csv` (append after each batch; create with a header
  row first). Resumable: if the file already has some RowIDs, skip those and continue. Every RowID in your
  shard must appear in your output exactly once.

## What to produce per row — gap → asset → distinct angle (in this order)
1. **Read** the competitor page (its format + full text — the headings tell you what's actually on it). Resist
   leading with their title/brand framing — it leaks their angle into yours.
2. **Judge against the brand scope → set `Brand fit`** (one of):
   - `CORE` — on-brand subject Testlify can own outright.
   - `TRANSPLANT` — off-brand subject but a link-pulling *format*: keep the format, point it at our world;
     record the original subject in Notes (e.g. `transplanted from: compensation`).
   - `ADJACENT` — same buyer, broader subject (best-of round-ups, industry trends).
   - `SKIP` — outside Testlify's world, or junk/thin. Leave Asset/Angle gap/Distinct angle blank, Notes `SKIP — reason`.
3. **Write the `Angle gap` FIRST — what's thin/missing/paywalled/stale on THIS specific page.** Cite a concrete
   fact: word count, what's on the page, what's missing, what's gated, a staleness date, a format limit.
   Anti-template test: *"Could I have written this gap without reading this row?"* If yes, rewrite.
   - ❌ banned (generic): "generic explainer - no original data, no inline test"
   - ✅ good (specific): "11 questions, MCQ only, no public sample, free PDF cert" / "350-word definition, no
     template, no example screenshots" / "2022 salary data, last refresh 14 months ago"
   - A genuinely strong page with no obvious gap → `strong — no obvious gap`.
4. **Write the `Asset` — the thing WE would build to beat that gap.** Take the page's winning **format**, apply
   it to a subject inside our brand scope (copy the shape, not their exact topic), and bake in the fix for the
   gap. Name it as a **real working title a writer could open a doc with** — free text, NOT "[Format] on
   [Topic]" glued together. The differentiator from the gap should be visible in the name.
   - ❌ template fill: "Glossary on hiring terms" · ✅ real: "Hiring & Assessment Glossary with Bundled Micro-Tests + Templates"
   - ❌ "Free skills test on AI roles" · ✅ "Free AI & ML Skills Test (public sample Qs + free shareable cert)"
5. **Write the `Distinct angle` — one line: how OUR version is different/better than THIS page**, drawn straight
   from the gap. Must cite the concrete gap. e.g. gap "MCQ-only, no public sample, cert paywalled" → Distinct
   angle: "adds a live editor, 5 sample Qs visible pre-signup, and a free shareable cert — all three things this
   page withholds."

## Output format — STRICT (JSONL — one JSON object per line)
Write to `agent_out/shard_NN.jsonl`. **One JSON object per line**, with exactly these keys:
`{"RowID":"<id>","BrandFit":"CORE|TRANSPLANT|ADJACENT|SKIP","AngleGap":"...","Asset":"...","DistinctAngle":"...","Notes":"..."}`
JSON escaping handles any commas/quotes/pipes in your text — so write natural prose, no delimiter worries.
Append one line per RowID (use a python/node heredoc with json.dumps so escaping is correct — never hand-build
JSON). For SKIP rows, set AngleGap/Asset/DistinctAngle to "" and put the reason in Notes. Every RowID in your
shard present exactly once. RESUMABLE: if the file already has some RowIDs, skip them.

When done, reply with just: `shard_NN done: <N> rows written`.

---

# BRAND SCOPE — Testlify (reason every row against this)

## What we are / who we serve
Testlify is an AI-powered skills-assessment and interview platform for hiring. Companies build a test from a
library of 3,500+ pre-built tests (4,500+ roles) or AI-generate custom ones, run conversational AI interviews
(chat/voice/video), apply anti-cheating proctoring, get AI-scored reports, push results into 100+ ATS.
**Buyer:** hiring managers, recruiters, talent-acquisition teams — startups to enterprise, screening at volume.
**Job:** screen candidates faster and more objectively — remove bias, cut time-to-hire, make every hiring
decision defensible — without a clunky candidate experience. Positioning: "High-confidence talent decisions."

## Subjects we can credibly own (illustrative — not exhaustive, not a checklist)
- **Skills tests & assessments** — per-role/per-skill (technical/coding, cognitive/aptitude, language,
  personality, role-specific). Our deepest turf; free public tests are the niche's #1 link magnet.
- **Pre-employment / skills-based hiring** — what to test, how to screen, validity & fairness, candidate experience.
- **Interview process** — structured interviews, AI interviews, interview questions by role/skill, scorecards.
- **Hiring assessment terminology** — glossary of assessment, psychometric, and hiring terms.
- **Recruitment metrics & analytics** — time-to-hire, quality-of-hire, cost-per-hire, funnel/benchmark data. (CORE)
- **Bias, fairness & defensibility in hiring** — adverse impact, validity, compliance, audit trails. (CORE)
- **Candidate / role templates** — job descriptions, scorecards, assessment rubrics, interview kits.
- **Proctoring & assessment integrity** — anti-cheating, remote test integrity, AI-cheating in interviews.

## Off-limits / not us (strong SKIP-or-TRANSPLANT hint, not a hard ban — still judge each page)
- HR-ops not tied to hiring — payroll, benefits, compensation bands, retention bonuses, PTO, performance reviews, post-hire L&D/upskilling.
- ATS / CRM / sourcing product mechanics; recruiting-agency CRM; outreach sequencing.
- General workplace / management / culture — leadership, team-building, engagement, office life.
- Pure career-advice-for-jobseekers — resume-writing tips, "how to get a job" (candidate-side, off-buyer).

## Transplant note
When a competitor wins links on an off-brand subject with a link-pulling format, keep the format, point it at
our world (skills tests, screening, interview process, assessment data). Record the original off-brand subject
in Notes (e.g. `transplanted from: compensation`); never let it become our subject.
