---
type: workflow-recipe
stage: orchestration
orchestration: content-engine
reusable: any company
reads:
  - projects/[company]/brand-brain/                 # voice + stats + frameworks → write on-brand, never AI
  - projects/[company]/content-database.csv         # reuse check + internal-link targets
  - projects/[company]/semrush-top-pages.csv        # winners + competitor context
  - workflows/standards/                            # the rules shelf (the bar + source/claims/format/humanize)
follows_bar: workflows/standards/seo-aeo-geo-bar.md  # every step maps to a section of the bar (see map below)
produces: the live page (or draft) + a handoff (score, claims ledger, what changed)
last_updated: 2026-06-30
replaces: standalone content-write / content-refresh skills (those are orchestration-only — no original rules)
---

# Recipe — The Content Engine

> **This file is the flow** — the single, top-to-bottom path that turns a topic (or an old page, or a chosen
> asset) into content good enough to rank #1 AND get cited by AI engines. It is the *process*. The *rules* it
> follows live in `workflows/standards/` (the bar + its companions); each step points to the exact rule file
> instead of restating it, so a rule lives in one place and never drifts. Read this for the order of moves;
> read the standards for the depth.

## What this does
Produce one piece of content to the full SEO + AEO + GEO bar — for **any** of the three jobs below — so it
ranks on Google and gets quoted by AI Overviews / ChatGPT / Perplexity / Gemini. Same spine for all three;
they differ only at where they *enter* and where they *exit*.

## The one rule that governs everything
> The content must add real value a reader can't get elsewhere, or it does not ship. This is the gate at
> Step 7. Mass-producing thin or cosmetic content to chase rankings is exactly what Google's scaled-content
> policy punishes (`workflows/standards/content-policy.md`). Every piece passes the value gate or it stays a draft.

## The three jobs it covers (one spine, different ends)

| Job | Enters at | Skips | Exits at |
|---|---|---|---|
| **Write new** (blog, PR, case study, landing, etc.) | Step 0 with a topic/keyword | — | Step 8: push as **draft only** (never auto-publish new) |
| **Refresh old** (rework a live URL) | Step 0 with a live URL | reuse check (you already have the page) | Step 8: backup → PATCH **keeping the slug** → render check |
| **Build a link asset** (asset-engine D3) | Step 2 with a chosen asset (from D2) | — | Step 8: publish + **wire the reverse-silo internal links** |

## What you produce
Built in order, one per step:
- `content-brief.md` — the job, keyword, audience, page type. *(Step 0)*
- `serp-brief.md` — what the live SERP demands the skeleton satisfy. *(Step 1)*
- `outline.md` — the validated skeleton (H1, question H2s, TL;DR/FAQ/table/CTA slots). *(Step 2)*
- the **draft** with every stat tagged + a claims ledger. *(Steps 3–6)*
- `score.md` — the 0–100 score + publish/draft decision. *(Step 7)*
- the **live page (or draft)** + a handoff (what changed, claims ledger). *(Steps 8–9)*

## Inputs you need
- The foundation files above (run the `seo-foundation` skill first if `brand-brain/` doesn't exist).
- Live SERP access (read the actual top-ranking pages) + Semrush for keyword/competitor data.
- The standards in `workflows/standards/` (the rules shelf — see the port list at the bottom).

---

# The steps (in order)

## Step 0 — Pick the job + the target → `content-brief.md`
**What it does:** decide which of the three jobs this is, and lock the target on one page.

**Process:**
1. Identify the job (write new / refresh / link asset) and the **content type** (blog, comparison, PR, case
   study, landing, calculator, glossary…).
2. Name the **primary keyword**, the **audience** (`[AUDIENCE]`, from the brand brain), and the URL (refresh)
   or slug-to-be (new).

*(Intent-match — does the page actually serve what the SERP rewards — is checked downstream in Steps 1–2, not here.)*

**Output `content-brief.md`:** job · content type · primary keyword · audience · target URL/slug.

## Step 1 — Study the live SERP → `serp-brief.md` (mandatory, never skip)
**What it does:** read the actual top-ranking pages and turn them into a brief the skeleton must satisfy.
**Follows the bar:** *SERP brief* + *SERP benchmark dimensions*.
**Read / run:** `02-content-engine/_to-generalize/serp_study.py` scaffolds the brief JSON *(staged, Testlify-specific — to generalize)*; the live data comes from the **Semrush MCP** (keyword overview · related keywords · questions) + a SERP source (top-20 · snippet owner · PAA · AI Overview). Once the **dominant format** is known, build it from `workflows/standards/formats.md` + `listicle-formatting.md`; tool / calculator / glossary formats → `01-asset-engine.workflow.md` (the asset engine).

**Capture for the primary keyword:**
- **Intent** (informational / commercial / transactional / navigational) — match the post type.
- **Dominant format** of the top 5–10 (how-to / listicle / comparison / definition / tool) — match it.
- **Required subtopics** recurring across top results → these become the H2s. Off-intent H2s are a fail.
- **SERP features** — featured snippet (note its format), People-Also-Ask, AI Overview, image/video pack.
- **PAA → FAQ** — harvest 3–5 PAA questions for the FAQ + section lead answers.
- **Targets from the median** (not arbitrary): length ≥ median ×1.0 (aim ×1.2), citations ≥ median +1,
  schema depth ≥ median +1 type, include a table if the winners do.
- **Differentiation angle** — what the top results miss that `[COMPANY]` can add (first-hand data, its angle).

**Output `serp-brief.md`** — the above. Cache it; reuse ~7 days.

## Step 2 — Build + validate the skeleton → `outline.md`
**What it does:** turn the brief into a structure before writing a word.
**Follows the bar:** *AEO* (question H2s, TL;DR, FAQ) + *Featured Snippet* + *Topical authority*.

**The skeleton has:** one H1 (primary keyword, natural) · H2s phrased as real search queries (≥50%
questions, the core answer-targets are questions; keyword-phrase headings like "Benefits of X" allowed —
don't force every heading into a question) · a TL;DR slot · a FAQ slot (5 Q&As from the PAA) · a table slot
(if the SERP uses one) · a single CTA slot (placed AFTER the body, BEFORE Key Takeaways + FAQ) · an
internal-link plan (≥3 related `[COMPANY]` pages, varied anchors). For *new* content, pick the **format spec**
first (`workflows/standards/formats.md` — each format has its own person, length, structure).

**Validate the skeleton against `serp-brief.md` before writing.** Every required subtopic is an H2; nothing
off-intent.

> **Human gate 1 — approve the plan.** Show the SERP brief + the outline as ONE block and get a single
> `approve` before any writing happens. No drafting until the plan is signed off.

**Output `outline.md`** — the approved skeleton.

## Step 3 — Reuse check (don't rebuild what exists) — *write/asset only*
**What it does:** before writing new, search `content-database.csv` — improve an existing page if one already
covers this. *(Refresh skips this: you already have the page.)* → mirrors the asset-engine reuse check.

## Step 4 — Draft the body to the bar → the draft (with stats tagged)
**What it does:** write the piece. This is the heart of the recipe.
**Follows the bar:** *the 6 levers* (lever 1 first + densest) + *per-engine SEO/AEO/GEO cores*.

**The moves, in priority order:**
1. **Inject cite-able evidence (lever 1 — the strongest AI-citation driver).** Inline stats + direct quotes +
   outbound citations to **named primary sources**. Source selection, tiers, freshness, density (~1 citation
   / 150–250 words, ≥3 distinct domains), and 2–6 word natural anchors → `workflows/standards/source-authority.md`.
   **Every claim** (exact figure + named primary + a live 200 URL + correct year, no fabrication, honest
   product-fit, self-consistency, a claims ledger) → `workflows/standards/claims-integrity.md`.
   **Never cite or link a direct competitor** (the list is a `projects/[company]/` value → content-policy).
2. **Answer-first.** Intro answers the core query in the first 1–2 sentences (no scene-setting). TL;DR =
   4–6 plain-language **summary** bullets (key takeaways, not a stat dump). Under each question H2, the first
   40–60 words are a self-contained, quotable answer.
3. **Write in `[COMPANY]`'s voice, not AI's.** Brand voice + real numbers from `brand-brain/` (`stats.md`);
   body copy in the brand's standard person (no "I/my experience" in body for third-person brand voice).
   Name ≥1 owned `[COMPANY]` framework (from the brand brain / frameworks asset — never invent one).
4. **Structure for extraction.** Comparison tables, numbered steps, short scannable sections, ≥1 data table,
   Pro Tip + Key Takeaway callouts (5–7 substantive items: insight + why + implication). No horizontal
   dividers. For list / comparison / "best X" / "alternatives" pieces → `workflows/standards/listicle-formatting.md`
   (every recommended tool its own H2, H3 Features/Pros/Cons/Best-For/Pricing, comparison table, ToC anchors).

**Output:** the full draft with every stat tagged `[STAT: figure | source | year | URL | CONFIDENCE]`.

## Step 5 — E-E-A-T + on-page hygiene → the draft
**What it does:** add the trust + on-page signals.
**Follows the bar:** *E-E-A-T* + *SEO core* + *Topical authority*; mechanics → `workflows/standards/on-page-seo.md`.
**Read / run:** schema → `02-content-engine/_to-generalize/schema-types.md`; FAQ accordion → `_to-generalize/faq_accordion.py` + `faq-accordion.md`; external-link / citation audit → `_to-generalize/outbound_link_audit.py`. *(all staged, Testlify/platform-specific — to generalize)*

- **Author authority renders NATIVELY** from the `[PLATFORM]` author field (name, title, bio, credentials,
  link) — **never write a byline or "About the author" into the body.**
- **Title** matches search intent + leads with the primary keyword (not just catchy). **Meta** 140–160 chars,
  leads with the keyword + the core value term.
- ≥3 internal links, descriptive varied anchors (exact-match <30%); 4–5 external links to primary sources.
- Schema: Article + BreadcrumbList. FAQ ships as the house accordion **for UX only** (FAQPage/HowTo/Speakable
  give no rich result for general sites — don't invest there). Schema gives ~0 AI-citation lift.
- Every image: descriptive, keyword-aware alt.

## Step 6 — Humanize + final editorial pass (mandatory) → clean draft
**What it does:** strip every AI tell and fix every flow/grammar problem. Never ship model output verbatim.
**Follows:** `workflows/standards/write-like-a-human.md` (reconcile with the existing
`workflows/00-foundation/scripts/brand-brain/avoid-ai-writing/SKILL.md`).

- No em dashes, no banned words, no AI-signature phrases ("delve", "landscape", "seamless", "robust"…), no
  hedging, no exclamation/emoji (per the brand brain).
- **Human-experience rewrite:** a real practitioner's voice — point of view, concrete examples, tradeoffs,
  varied sentence rhythm, plain language. Originality lives in framing/analysis only, never invented data.
- **Final read as a line editor:** grammar, punctuation, run-ons, broken sentences, weak transitions, abrupt
  jumps. Every section flows into the next. (Not regex-catchable — a real read.)
- Concision gate: ×1.2 length is a **ceiling, not a floor** — never pad to hit a number.

## Step 7 — Score + value gate → `score.md`
**What it does:** decide if it's good enough to ship.
**Follows the bar:** *Scoring + publish threshold* (the rubric dimensions are defined in the bar; the loop runs here).
**Read / run:** `02-content-engine/_to-generalize/verify_post.py` — the element-parity + link-rel + banned-words + render gate *(staged, WP-coupled — to generalize)*.

- Score 0–100 across five dimensions: `SEO ×0.25 + Structure ×0.15 + Content ×0.25 + EEAT ×0.15 + AEO/GEO ×0.20`.
- **Claims-ledger self-audit:** every stat is fetched, returns 200, the figure is actually present, year
  correct — or the stat is **cut**. Zero unverified numbers ship. Zero `[` draft brackets remain.
- **Publish-ready at Overall ≥ 80.** A P0 failure (unverified stat, intent mismatch, competitor cited,
  cosmetic-only refresh) caps it below 80 until fixed. Rework the lowest items + re-score, **cap 3 passes**;
  if it still can't reach 80 without fabricating or padding, keep it a **draft** and report. The score makes
  it *publish-ready*; the human go-ahead at Step 8 makes it *published*.

**Output `score.md`** — the five scores, the overall, the decision (publish-ready / draft), the claims ledger.

## Step 8 — Deploy (per job) → the live page (or draft)
**What it does:** ship it, the right way for the job.
**Follows:** `workflows/standards/content-policy.md` (slug/301 + pacing) + the asset engine for reverse-silo.
**Read / run:** the `[PLATFORM]` deploy layer → `02-content-engine/_to-generalize/wp_client.py` + `wp-operations.md` *(staged, WordPress-specific — to generalize)*.

> **Human gate 2 — preview + approve.** Before anything is pushed, show ONE preview block: the quality score,
> how it beats the current SERP, and the meta (slug · H1 · title · description · excerpt). Get the go-ahead.
> Nothing is pushed without it.

- **Write-new:** push to `[PLATFORM]` as **`status=draft` only** (never auto-publish a new piece). Set meta in
  a separate call. Return the admin URL.
- **Refresh:** backup first → PATCH **keeping the slug** (a title change does NOT need a URL change; the slug
  holds equity) → **post-push render check** (accordion + schema rendered, zero leftover `[` tokens) →
  re-verify each field → log the change. Change a slug only if genuinely harmful, and then flag the 301 plan
  for a human — never auto-change it at scale.
- **Link asset:** publish, then **wire the reverse-silo** — contextual internal links from the asset → the
  money pages, varied natural anchors (`research/strategies/reverse-silo.md`).
- **Pace publishing** — never mass-deploy in one burst (a scaled-content signal → content-policy).

## Step 9 — Post-publish → the handoff
**What it does:** close the loop.
- Set `dateModified` (the visible "Updated on" date) **only** when a substantive change was made.
- File the handoff / review note: live URL, before→after score, what changed, the claims ledger, the
  recommended author for topical authority. Nudge re-indexing if your process supports it.
- Re-evaluate every 3–6 months (quarterly beats annual).

---

# How each step maps to the SEO-AEO-GEO bar (grounding check)
Every step above is traceable to a section of `workflows/standards/seo-aeo-geo-bar.md` — nothing is invented here:

| Step | Bar section it runs / follows |
|---|---|
| 1 SERP study | *SERP brief* + *SERP benchmark dimensions* |
| 2 Skeleton | *AEO* (question H2s, TL;DR, FAQ) + *Featured Snippet* + *Topical authority* |
| 4 Draft | *The 6 levers* + *SEO/AEO/GEO per-engine cores* |
| 5 E-E-A-T + on-page | *E-E-A-T* + *2026 Google ranking bar* + *What is dead* |
| 6 Humanize | the bar's *anti-fluff / concision* note + the voice standard |
| 7 Score | *Scoring + publish threshold* |
| 8 Deploy | *URL/slug policy* + *scaled-content guardrails* (now in content-policy) |

---

# The rules shelf this recipe uses
This recipe holds the **steps**; the **rules** live in the files below, and each step points to them (one
rule, one home, no drift). Only what we actually need is listed. Each rule's permanent home is
`workflows/standards/` (general, any company) or `projects/[company]/` (company-specific) — no reference here
points outside this machine.

| Rule file | What it owns | Home | Status |
|---|---|---|---|
| `seo-aeo-geo-bar.md` | the quality bar — the rubric, the engines/levers, the 0–100 score | `workflows/standards/` | **built** |
| `formats.md` | per-type blueprints — blog · PR · white paper · case study · landing | `workflows/standards/` | **built** |
| `source-authority.md` | which sources to cite, freshness, link density + anchor rules | `workflows/standards/` | **built** |
| `claims-integrity.md` | never invent a stat — figure + named source + live URL + year, or cut | `workflows/standards/` | **built** |
| `listicle-formatting.md` | "best X" / comparison posts — each tool its own H2, table, pros/cons | `workflows/standards/` | **built** |
| `write-like-a-human.md` | the final anti-AI / human-voice pass (points to `…/avoid-ai-writing/SKILL.md` for the mechanical line-edit) | `workflows/standards/` | **built** |
| `content-policy.md` | slug/301, publish pacing, no-competitor, link rel | `workflows/standards/` | **built** |
| `on-page-seo.md` · `lighthouse-qa` · `image-sourcing` | on-page mechanics + build QA | `workflows/standards/` | already exists |
| brand voice · real stats · named frameworks · author byline | how *this* company sounds + what it can claim | `projects/[company]/brand-brain/` | per-company (built by `seo-foundation`) |

*Optional companion:* `sources-provenance.md` — the evidence behind each bar rule ("says who?"). A reference
for challenging a rule, not a front-line writing file; port it only if we want the proof trail.

**Tools (staged, pending generalization).** The scripts that back Steps 1 / 5 / 7 / 8 are parked in
`02-content-engine/_to-generalize/` — SERP scaffolder, FAQ accordion, link audit, the verify gate, the deploy
client — Testlify/platform-specific for now (see that folder's `README.md`). Each step's **Read / run** line
names the one it uses. These get generalized + wired in properly later.

---

# Gotchas
- **Step 1 (SERP):** read the *actual* live pages, not a guess. The brief is the contract the skeleton obeys.
- **Step 4 (evidence):** lever 1 is the whole game for AI citation — do it first and densely. A vague,
  uncited claim is not cited by anyone.
- **Step 6 (humanize):** prompting reduces AI tells; only line-editing removes them — this pass is mandatory,
  not optional. Never ship model output verbatim.
- **Step 7 (gate):** an unverified stat is dropped, not shipped "hoping someone checks later" — no one will.
- **Reuse, don't duplicate:** before deepening `write-like-a-human.md`, reconcile it with the existing
  653-line `avoid-ai-writing/SKILL.md` so one voice rule doesn't live in two files.
</content>
</invoke>
