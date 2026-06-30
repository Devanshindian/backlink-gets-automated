---
name: seo-foundation
description: The backlink machine for any company. Part A - the SEO foundation (catalogue every page, pull top pages from Semrush, build the brand brain). Part B - the Asset Engine (build a free asset other sites link to). Run Part A first for a new company, then Part B. All outputs land under projects/<company>/.
---

# Backlink Machine

A reusable machine that earns backlinks for any company. Two parts, run in order:

- **Part A - Foundation** (Steps 1-3): learn the company - every page it has, the pages that win, and
  exactly how it writes. *Done once per company.*
- **Part B - Asset Engine** (Stages D0-D5): build one genuinely useful **free asset** (calculator, data
  report, index, guide) that other sites *choose* to link to, then funnel that earned authority to the
  money pages. *Run after the foundation is in place.*

All outputs go under `projects/<company>/`.

---

# Part A - Foundation

Three steps, run in order, to set up a company. Works for any company. All outputs go under
`projects/<company>/`.

## Step 1 - Content Database
Catalogue every page the site has.
- Pull every page's URL, type, title, description **and full content** in bulk from the site's **WordPress REST API**.
- Fill any blank descriptions (template pages don't expose one) from the page's content and meta tags.
- Scripts (`workflows/00-foundation/scripts/content-database/`): `build_content_database.py` pulls and
  assembles the catalogue; `enrich_descriptions.py` and `enrich_meta_descriptions.py` fill the blank descriptions.
- **Full steps:** `workflows/00-foundation/content-database.workflow.md`.
- **Output:** `projects/<company>/content-database.csv` (one row per page: URL, Type, Title, Description,
  **Full content**, Traffic, Keywords, Intent) and `content-database.md` (a short summary). `Full content` is
  the page's entire clean text (no word limit) - it's what the asset-engine **reuse check** runs RAG against.

## Step 2 - Semrush Top Pages
Find the pages that already win on traffic.
- In Semrush, open the company's **Top Pages** report and export it to CSV.
- This gives the top pages by organic traffic. Its output fills the **Traffic** column in Step 1's
  content database, **and is what Step 3 uses to pick which pages to study.**
- **Full steps:** `workflows/00-foundation/semrush-top-pages.workflow.md`.
- **Output:** `projects/<company>/semrush-top-pages.csv` (top pages by traffic).

## Step 3 - Brand Brain
Learn exactly how the company writes, from its best pages.
- **Uses:** `projects/<company>/semrush-top-pages.csv` (from Step 2) - the top pages, whose URLs also
  give the spread across page types.
- From those, take ~20-40 pages, read them word-for-word, and capture the voice: how it writes, the words
  it uses and avoids, and the rules that keep content from sounding AI-written.
- **Full steps:** `workflows/00-foundation/brand-brain.workflow.md`.
- **Output:** the `projects/<company>/brand-brain/` folder (files listed below).

## What you have at the end - `projects/<company>/`
- `content-database.csv` + `content-database.md` - the full page catalogue and its summary.
- `semrush-top-pages.csv` - top pages by traffic.
- `brand-brain/`:
  - `brand-brain.md` - the hub: what the company is, who it talks to, its voice, the anti-AI rules, a brand-assets summary, and a voice-test checklist.
  - `voice-analysis.md` - the evidence behind the voice.
  - `brand-assets.md` - colours, fonts, logo, key links.
  - `stats.md` - the company's real numbers.
  - `stories.md` - approved brand anecdotes (stub, filled over time).
  - `opinions.md` - approved strong opinions (stub, filled over time).
  - `page-shortlist.md` - the pages studied to build the voice.
  - `voice-data/` - the raw analyzer measurements (6 JSON files) behind voice-analysis.md.

---

# Part B - Asset Engine

Build one free asset other sites *choose* to link to - the **reverse-silo**: external links -> the asset
-> internal links -> the money pages. Six stages, D0-D5. Full recipe: `01-asset-engine.workflow.md`.
Outputs go under `projects/<company>/asset-engine/`.

## D1 - Idea Backlog (built)
Three methods, each a deep recipe in `01-asset-engine/idea-backlog/`, each producing its **own** idea pool.
They share one ownership anchor - **`brand-scope.md`** (derived from the brand brain, user-approved) - so the
three pools can be compared and merged. Run all three, then **merge them into one sheet** (next section).

### Method 1 - Competitor Study
**What it is:** steal the formats that already earn competitors the most backlinks (the shape, not the topic),
and build our own version on a subject we own.
**Full steps:** `01-asset-engine/idea-backlog/1-competitor-study.md`
**Output:** `projects/<company>/asset-engine/competitor-study/competitor-study-ideas.xlsx` - Tab 2 (Ideas) is the one we use.
**Columns (Tab 2):** `# · Build window · Brand fit · Asset · Our subject · Format · Total domains · # comps · # pages · Beat. · Effort · Distinct angle · Backing URLs`

### Method 2 - Model Other Niches
**What it is:** import proven link-bait formats from other industries that no competitor in our niche has
built yet, and adapt each one on-brand.
**Full steps:** `01-asset-engine/idea-backlog/2-model-other-niches.md`
**Output:** `projects/<company>/asset-engine/model-other-niches/model-other-niches-ideas.xlsx`
**Columns:** `Idea # · Method · Brand fit · Asset · Format · Our topic · Distinct angle · Source niche · Evidence URLs · Beatability · Effort · Notes`

### Method 3 - Study Trends
**What it is:** read what the niche is fired up about right now on Reddit, distil it into recurring tensions,
and shape each into a timely asset idea.
**Full steps:** `01-asset-engine/idea-backlog/3-study-trends.md`
**Output:** `projects/<company>/asset-engine/study-trends/study-trends-ideas.csv`
**Columns:** `Tension · Asset title · What it'd be · Brand fit · Unfair advantage · # posts · Audience · Emotion · Best example URL`

## Merge the three pools into one sheet
Once all three are done, club them into a single **CSV** file (CSV, not xlsx — the reuse check later pastes
whole pages into it, which Excel would truncate).

**Save to a new folder:** `projects/<company>/asset-engine/clubbed/clubbed-ideas.csv`

**Layout:** stack the three pools top to bottom - **Competitor (M1) -> Reddit / Study Trends (M3) ->
Other-niche (M2)**. Each block keeps its own sort order; blocks are contiguous by row order (a CSV has no colour).

**Columns** (a blank cell is expected when a column doesn't apply to that method):

| Column | Applies to |
|---|---|
| Brand fit | M1 M2 M3 |
| Asset | M1 M2 M3 |
| Format | M1 M2 |
| Distinct angle | M1 M2 M3 *(for M3, fill from "What it'd be")* |
| Total domains | M1 |
| # comps | M1 |
| # posts | M3 |
| Beatability | M1 M2 |
| Effort | M1 M2 |
| Proof URLs | M1 M2 |

A Reddit (M3) row only fills **Brand fit · Asset · Distinct angle · # posts** - the rest stay blank, and
that's fine. The merge is **pure assembly:** every cell is lifted straight from a method's own output above.

## Reuse check - do we already have it? (D2)
Before building anything, match every idea in `clubbed-ideas` against the company's **existing content** (the
`Full content` in the content database) - **Voyage (`voyage-4-large`) two-vector retrieval (title + body,
blended) → `rerank-2.5` → top 7 pages**, then **parallel LLM sub-agents (one idea each)** read them and judge.
Fills, in `clubbed-ideas.csv`: **RAG candidates** + **Candidate 1–7 content** (the
candidates' full text, pasted inline) in Stage 2, then **Reuse verdict** (Already have it / Improve existing /
Build from parts / Brand new) **· Chosen links · Why** in Stage 3. So you never rebuild what already exists,
and you reuse existing research when you do build.

**Outputs (under `projects/<company>/asset-engine/clubbed/`):**
- `clubbed-ideas.csv` — the full scored + reuse-checked pool (includes the bulky `Candidate 1–7 content` columns).
- `clubbed-ideas-review.csv` — the lean **review copy** (same file minus the content columns), opens cleanly.
- **A web viewer** — a self-contained `index.html` (search · filter · expand · Keep/Maybe/Cut + CSV export),
  published to a **public GitHub Pages URL** (personal account, randomised repo name, push-clone kept in
  `clubbed/_pages-repo/`) so a reviewer just opens one link. Built from the review CSV; on later runs, **update
  the same repo's `index.html` — never create a second repo / link**.

**Full steps:** `01-asset-engine/reuse-check.md`.

