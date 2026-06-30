# SEO + AEO + GEO Standards Bar (2026)

The shared quality bar for [COMPANY] content (write + refresh). Audience: [AUDIENCE] (defined in the company's brand brain). Goal: rank #1 on Google AND get cited by AI Overview / ChatGPT / Perplexity / Gemini.

This is the definition of "good content." The recipe at `workflows/02-content-engine.workflow.md` runs the process; this file defines the targets it must hit.

---

## The 3 engines (how they differ)

| Attribute | SEO | AEO | GEO |
|---|---|---|---|
| Engine | Google / Bing crawlers | Answer engines, AI Overviews, voice | Generative AI (ChatGPT, Claude, Gemini, Perplexity) |
| Intent | Navigational / informational / transactional | Quick, conversational, voice-first | Deep synthesis, multi-step reasoning |
| Output | Ranked links | Featured snippet / spoken answer | Generated prose citing sources |
| Primary signal | Backlinks, E-E-A-T, Core Web Vitals | Concise structured answers | In-body stats + quotes + outbound citations to named primaries |
| Win condition | Drive organic traffic | Be the lifted answer | Get quoted / cited in AI output |

---

## The 6 levers that compound (priority order)

Spend effort top-down. Lever 1 is the strongest *causal* AI-citation driver; the rest support ranking and eligibility.

| # | Lever | Why it matters |
|---|---|---|
| 1 | **Inline stats + direct quotes + outbound citations to named primary sources** | Strongest causal AI-citation lift. Princeton GEO study: each of these ~+30-40% citation likelihood. This is where the leverage is — do it first, do it densely. |
| 2 | **E-E-A-T on page** | Author box (bio + credentials + LinkedIn) rendered NATIVELY by the [PLATFORM] author field - NEVER write it into the body (see `content-policy.md`). Google's trust gate; AI engines weigh source authority. |
| 3 | **Direct 40-60 word answers under question H2s** | Featured-snippet + AI-Overview eligibility. One clean liftable answer per section. |
| 4 | **Beat the SERP median** (length, citations, depth) | Relative, not absolute. See benchmark dimensions below. |
| 5 | **Topical authority** | 3+ internal links to related [COMPANY] posts, pillar links, varied anchors (<30% exact-match). |
| 6 | **Freshness + substantive change** | dateModified current, 2026 framing where natural, post-2022 sources. Must be a *real* update (see `content-policy.md`). |

---

## 2026 Google ranking bar

### Helpful Content (HCU March 2024 + ongoing)
- People-first writing, first-hand experience demonstrated
- Original insight not available elsewhere
- Specific numbers + named entities
- Author credibility visible on page
- Single-topic focus
- No scaled / templated / thin content

### E-E-A-T (Experience, Expertise, Authority, Trust)
- Author box (bio + credentials + LinkedIn + years exp) visible via the [PLATFORM]-native author field - never authored into the body
- Author has 3+ prior posts in same cluster
- First-hand markers: "I have seen…", "In my work with…", "A pattern I keep observing…"
- Cite **primary sources only**: .gov, .edu, peer-reviewed, original research, named industry authorities. **Full tiered source-authority hierarchy + freshness rules + external-link density + anchor-text rules: `source-authority.md`** (the canonical source list).
- **NEVER cite or link a direct competitor** (see `content-policy.md` for the list + rationale). If the only source for a stat is a competitor, drop the stat or use a neutral primary. Critique competitor approaches generically, never by name.
- **Citation integrity (P0):** every stat links to its SPECIFIC source (the report/page, not a category hub), returns 200, and the year matches the source; no stat uncited, none repeated; verify each figure (entity + number + year) by web search, never from memory; aim for >= 2-3 distinct citation domains per post. (See `claims-integrity.md`.)
- **Stat freshness + precise framing:** prefer the most recent primary figure; if you keep an older-but-canonical stat, attribute the correct year (do not imply it is newer than it is). When you cite the high/low end of a range or a sub-segment, frame it precisely to match the source — use the exact wording the source supports, not a convenient rounding.
- datePublished + dateModified visible
- Organization schema linked

### AI Overview eligibility (50%+ of SERPs in 2026)
- Clear topic definition in first 100 words
- Listicle / structured format
- **Citation density 4+ inline** (lever 1)
- Brand mention 3-5x natural
- Direct factual claims with cited sources
- Q&A sections at section breaks
- No hedging — authoritative claims only
- Freshness: dateModified ≤6 months

> Schema gives ~**zero** independent AI-citation lift. Do schema for Google rich results only. AI Overview eligibility comes from in-body density (stats/quotes/citations), not markup.

### Featured Snippet
- 40-60 word answer in first 200 words
- Paragraph / list / table matching the current SERP format
- Question phrasing in the H2 above the answer
- Definition box for "what is" intent; comparison table for "X vs Y"

### Site reputation (May 2024)
- No scaled-content site refs, no parasitic SEO subdomains
- Editorial review visible (date-stamped, author named)

### Core Web Vitals (INP replaced FID, March 2024)
- Avoid heavy inline images; keyword-aware alt text

### Topical authority
- 3+ internal links to related [COMPANY] posts
- Pillar pages linked from cluster posts
- Internal anchor varies (no exact-match >30%)
- **Semantic coverage: include related subtopics, entities, and semantic keywords (not just the exact keyword).** Cover the entities and questions the top results and PAA reveal, plus the natural co-occurring terms a domain expert would use. This signals topical depth to both Google and AI engines. Place them naturally - this is coverage, not keyword stuffing.

### Conclusion / close
- **Close with a forward-looking next step + one specific CTA, NOT a recap.** A "strong conclusion" here means telling the reader what to do next and pointing to the single best action (e.g. the relevant [COMPANY] product + demo link), not an "In conclusion, we covered..." summary. Recap-style wrap-ups and "In conclusion" are banned (see `write-like-a-human.md`); the CTA block IS the deliberate, allowed ending. End on the next step, not a summary of what was already said.

### Freshness
- 2026 in title where natural
- dateModified updated quarterly minimum
- 2026 data + post-2022 sources only

---

## Per-engine guidelines, do/don'ts, checklists

### SEO — write for humans first, signal quality second

**Core**
- Identify intent type before writing; match format to intent.
- Study top 3 SERP results; match their depth.
- One H1 with primary keyword natural; H2s on secondary keywords / subtopics.
- Keyword in first 100 words without forcing.
- Paragraphs ≤4 sentences; bullet lists for scannability.
- **No horizontal dividers anywhere in the body.** Never use `<hr>`, a markdown `---` rule, or a separator block between sections, tools, FAQs, or pros/cons. Separate content with heading hierarchy (H2/H3/H4), paragraph spacing, lists, and tables only. Dividers read as AI-generated, add whitespace, and hurt mobile flow. Aim for clean editorial flow like HubSpot/SHRM/McKinsey/Gartner - if a section "needs" a divider, the heading structure is wrong. (Note: `---` as YAML/front-matter or a genuine table border is not a body divider; this rule is about decorative section separators.)
- Author box ([PLATFORM]-native, from the [PLATFORM] author field) on every article - not body content.
- ≥3 internal links, descriptive anchors (no "click here").
- **Outbound link rel policy:** internal = dofollow, editorial citations = `rel="nofollow noopener"`, paid/partner = `rel="sponsored"`. Never ship a paid link as dofollow. (Owned by `content-policy.md`.)
- Every image: descriptive, keyword-aware alt.
- **Title must match search intent (not just be catchy).** The H1 and meta title must reflect what the searcher actually wants for the primary keyword (the dominant intent/format from the SERP brief) and lead with that keyword. If the current title is clever but off-intent, rewrite it to the intent. A title that mismatches intent costs clicks and rankings even when the body is good.
- **Meta description: lead with the primary keyword AND the core value/intent term, directly.** 140-160 chars, NEVER over ~160 (Google truncates ~155-160 chars, so a 169-char meta loses its tail in the SERP). State the payoff the searcher wants in their words - explicitly, not implied. Do not write a vague benefit line that dances around the keyword. Unique per page; title tag 50-60 chars.

| ✓ Do | ✗ Don't |
|---|---|
| Unique title tag per page (50-60 chars) | Stuff keywords into headings/copy |
| 1 primary keyword + 3-5 related terms | Duplicate content (canonicalise) |
| Include data, stats, original insight | Ship thin pages (<300 words unjustified) |
| Benefit-driven meta descriptions | Over-use exact-match internal anchors |
| Length from competitors, not a quota | Neglect mobile (Google indexes mobile-first) |

**Pre-publish SEO checklist**
- [ ] Primary keyword in H1, URL slug, first paragraph
- [ ] Meta title 50-60 chars with keyword
- [ ] Meta description 140-160 chars with value prop
- [ ] ≥3 internal links, descriptive anchors
- [ ] All images have alt; descriptive file names
- [ ] Author box present ([PLATFORM]-native author field; NOT an "About the author" section in the body)
- [ ] External sources are authoritative + linked
- [ ] Article schema added

### AEO — give the exact answer in 40-60 words

**Core**
- **Phrase H2s as real search queries - questions where the subtopic is question-intent, concise keyword phrases otherwise.** Do NOT force every heading into a question; a clean keyword phrase ("Benefits of X", "How to do Y") beats an awkward forced question. Keep the core answer-target sections as questions (so PAA/snippet capture holds) - aim for at least half the H2s as questions, and always phrase to match how people actually search.
- Answer immediately in the first sentence below the heading, 40-60 words (do this under question H2s especially).
- Follow with numbered list (steps) or table (comparison).
- Conversational, jargon-free tone; sentences readable aloud in <10 sec.
- **Intro = answer-first, no fluff (AEO-critical).** The first 1-2 sentences of the opening paragraph must directly answer/address the page's core query - the thing the searcher typed. No scene-setting, no "in today's world", no throat-clearing before the point. If the reader stopped after the first two sentences, they should already have the gist. Context and nuance come after, not before, the answer.
- **TL;DR = a SUMMARY, not a stat dump.** The TL;DR is 4-6 plain-language bullets that summarize the key answers and takeaways - what the reader will learn and what to do. One idea per bullet. Weave a number in ONLY where it supports the point; never a list of disconnected standalone stats. A reader who reads only the TL;DR should understand the article's argument, not just see figures.

| ✓ Do | ✗ Don't |
|---|---|
| Open with "X is…" / "To do X, you…" | Bury the answer after long intros |
| Numbered lists for processes | Hedge ("it depends…") before answering |
| Dedicated FAQ section (5 Q&As) | Use jargon a non-expert can't parse |
| Keep snippet answer <60 words | Long compound sentences |
| Match query language in heading | — |

**Pre-publish AEO checklist**
- [ ] H2s match search phrasing (questions where question-intent, keyword phrases otherwise); >=50% are questions and the core answer-targets are questions - not every heading forced into a question
- [ ] 40-60 word direct answer follows each question heading
- [ ] Quick Answer / TL;DR above the fold
- [ ] Tone conversational, jargon-free
- [ ] Step content uses numbered lists
- [ ] FAQ = 5 Q&As (accordion for UX)

> FAQPage / HowTo / Speakable produce **no rich results** for a general SaaS site since Aug 2023 (HowTo fully removed). Keep the FAQ accordion for UX/structure only - expect no snippet, rich-result, or ranking lift from the schema.
> FAQ count is **5 Q&As** (2026 standard).

### GEO — become a source AI trusts enough to cite

**Core**
- Author credentials clear: name, title, years, certifications.
- Cite primary sources: original research, official reports, gov data, peer-reviewed.
- Include ≥1 original/proprietary stat ([COMPANY] platform data or named scenario).
- Write quotable, self-contained sentences (make sense out of context).
- Precise numbers, dates, named entities — vague claims are not cited.
- Lead each section with its most citation-worthy claim.
- Structured formats: tables, numbered lists, definition lists.
- Cover the topic exhaustively; anticipate follow-ups; build pillar→cluster.
- Original frameworks / named methodologies (named things get cited).

| ✓ Do | ✗ Don't |
|---|---|
| Precise quotable sentences w/ numbers + named sources | Vague, hedged, evidence-free claims |
| Create original research / proprietary data | Rely solely on secondary sources |
| Comprehensive coverage, no missed subtopic | Let stats go stale |
| Author attribution + institutional affiliation | Marketing fluff / superlatives |
| Clear semantic sections (H2/H3, definition lists) | Write for word count alone |

**Pre-publish GEO checklist**
- [ ] Author name, credentials, bio visible
- [ ] ≥1 original stat / study / proprietary data point
- [ ] Every claim backed by a named, linked primary source
- [ ] Key statements quotable out of context
- [ ] Topic covered comprehensively
- [ ] Tables / structured lists / clear headings throughout
- [ ] Unique insight not easily found elsewhere

---

## Scoring rubric (the definition of how content is scored)

Score each post 0-100 across five dimensions; the default publish-ready threshold is **Overall >= 80**.

`Overall = SEO x0.25 + Structure x0.15 + Content x0.25 + EEAT x0.15 + AEO/GEO x0.20`

A P0 checklist failure caps Overall below the threshold until fixed.

> The recipe runs the scoring loop, rework passes, and publish/draft decision (`workflows/02-content-engine.workflow.md`, Step 7). This file only defines the five dimensions + weights.

## SERP brief

> The recipe runs the SERP brief before building the skeleton (`workflows/02-content-engine.workflow.md`, Step 1). The skeleton must satisfy it; the benchmark-dimensions table below defines the targets the brief is checked against.

## SERP benchmark dimensions (beat or match the median)

| Dimension | Target |
|---|---|
| Word count vs SERP median | ≥ median ×1.0, target ×1.2 |
| Citation count vs SERP median | ≥ median + 1 |
| Schema depth (for Google rich results) | ≥ median + 1 supported type |
| Named [COMPANY] framework | 1+ owning a gap |
| Featured-snippet eligibility | 40-60 word answer in first 200 words |
| AI Overview score | ≥ 8/10 |
| E-E-A-T signals visible | [PLATFORM]-native author box + 4+ sources + dates (no body author section) |
| Internal rubric | ≥ 90/100 |

> **No fixed word-count quota.** Length is SERP-median-relative (×1.0 to ×1.2): a short SERP means a short winning piece.
> **ANTI-FLUFF:** ×1.2 is a **ceiling guide, not a floor**. Never add a sentence to reach a length or a count. "Comprehensive" means no missing subtopic, not more words — a complete answer in fewer words beats a padded one. Density (claims, stats, citations per 100 words) is the goal, not volume. Every draft clears the concision gate in `write-like-a-human.md` before publish.

---

## URL / slug policy + 301 redirects

> Moved to `content-policy.md`.

## What is dead — do not spend effort here

| Dead / no-value | Why | Do instead |
|---|---|---|
| FAQPage schema | No rich result for general sites since Aug 2023 | Keep FAQ accordion for UX only |
| HowTo schema | Fully removed by Google (Aug 2023) | Write clear numbered steps in body |
| Speakable schema | No general rich result | Write a clean liftable answer |
| Schema for AI citations | ~0 independent lift | Citations come from in-body stats/quotes/sources (lever 1) |
| llms.txt | No AI engine reads it | Skip entirely |
| Fixed word-count quotas | Length is relative to SERP | Use median ×1.0-1.2 |
| Keyword stuffing / exact-match anchor spam | Penalised | Natural keyword + varied anchors |
| Cosmetic-only "refreshes" | See `content-policy.md` | Make substantive change or don't touch |

---

## Scaled-content-abuse guardrails

> Moved to `content-policy.md`.
