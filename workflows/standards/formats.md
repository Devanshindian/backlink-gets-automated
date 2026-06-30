# Formats

Per-type content blueprints. One rule across all: every sentence earns its place. Padding kills.

Voices: [COMPANY]'s named house voices/bylines are defined in `projects/[company]/brand-brain/` — route the right voice per topic there. Where a format calls for a specific person below, pull that byline from the brand brain rather than hard-coding a name.

Shared quality bar lives elsewhere — do not restate it here:
- SEO/AEO/GEO element rubric, TL;DR rules, H2 phrasing, answer-first intros → `workflows/standards/seo-aeo-geo-bar.md`.
- Claims, sourcing, and citation integrity → `workflows/standards/claims-integrity.md`.
- List, listicle, and X-vs-Y comparison formatting → `workflows/standards/listicle-formatting.md`.

Global notes:
- **Length is a ceiling guide, never a floor to pad toward.** SERP-median x1.2 is the most a piece should need, not a target to fill. If the best version is shorter than the median, ship it shorter. Run every draft through the concision gate before push.
- No fixed word-count minimums beyond the per-format ranges below.
- Never include plaintext credentials. The CTA/booking link is only [COMPANY]'s approved booking/CTA link from the brand brain — verify any URL before using it.
- FAQ = 5 Q&As, rendered as the canonical accordion component, never core h3+paragraph. FAQPage/HowTo/Speakable schema give no rich results for general sites; keep them out as a ranking play.

---

## 1. Blog post

**What it is:** Educational article that helps a specific [AUDIENCE] reader solve a specific problem. Lives on [WEBSITE], targets Google, free to read.
**What it is NOT:** Press release, white paper, case study, or sales brochure.

**Tone + person:** Direct, warm, opinionated. Take a side. "you" and "I" freely. Tone shades by the chosen [COMPANY] voice (practitioner-friendly vs. peer-to-peer) — route per topic in the brand brain.
**Length:** SERP median x 1.2, within the type band below. No arbitrary minimum.

### The 5 blog types — pick one before writing

| # | Type | Use for | Band |
|---|---|---|---|
| 1 | How-it-works (deep) / How-to | High buyer intent, deep "how it works" | 1,200–2,500 / 8–10 H2 / framework + tables |
| 2 | Trend post | Timely traffic, social engagement | 1,000–2,000 / 6–8 H2 |
| 3 | Focused tactical / Opinion-POV | Thought leadership, social shares | 600–1,800 / 5–7 H2 |
| 4 | X vs Y comparison | Comparison intent | 1,800–2,200 / mandatory table |
| 5 | Listicle / Framework listicle / Data post | SEO traffic, backlinks, citations | 800–2,500 / named framework or original data |

(Bands above are SERP-median-relative guides, NOT fixed quotas — never pad to hit them.) Before drafting any type, study live exemplars of that type on [WEBSITE] for structure and voice. For list/comparison pieces (types 4 and 5), follow `workflows/standards/listicle-formatting.md`.

**Research for first-hand insight (the "experience" in E-E-A-T):** before drafting, mine community sources for real practitioner pain points and patterns relevant to [AUDIENCE] — Reddit, LinkedIn, YouTube case studies, Quora. Convert findings into observed patterns ("Across the teams I've worked with…", "A pattern people keep raising…"), never fabricated memories. These are for INSIGHT only — never cite a forum/Reddit/Quora as a source; citations still come from primaries per `workflows/standards/claims-integrity.md`.

### Structure (exact order)

1. **Headline** — target keyword, under 65 chars, number or question where natural, benefit/problem obvious.
2. **Hook (50–80w)** — problem, surprising stat, or provocative statement. Never open with banned AI openers.
3. **What the reader will learn (1–2 sentences).**
4. **TL;DR** — 4–6 plain-language SUMMARY bullets of the key takeaways/answers (NOT a stat dump; weave a number only where it supports the point). See `workflows/standards/seo-aeo-geo-bar.md`.
5. **Body** — subheading every 300–400w; paragraphs 2–4 lines; mix prose with occasional bullets, never bullets-only; each section makes one point + one example/number.
6. **Personal story/observation** — at least one first-hand moment, placed at the strongest point.
7. **FAQ** — 5 Q&As, accordion for UX only.
8. **Conclusion** — a forward-looking next step, NOT a recap. Do not restate what was already said or write "In conclusion"; lead straight into the CTA.
9. **CTA — one only**, specific and relevant (e.g. free trial, demo at [COMPANY]'s approved booking/CTA link, named resource).

### The blog rubric

The element rubric is OWNED by `workflows/standards/seo-aeo-geo-bar.md` (single source — do not restate it here). In brief, each is a quality bar when present, never a quota to manufacture (the concision gate overrides any count): answer-first intro; TL;DR = SUMMARY bullets (key takeaways, NOT a stat dump); H2s match search phrasing; 40–60 word answers under question H2s; specific numbers + named primary sources (per `workflows/standards/claims-integrity.md`); 1+ named [COMPANY] framework; 1+ data table; Pro Tip + Key Takeaway; 3+ internal links (dofollow) + external citations (`rel="nofollow noopener"`); FAQ accordion (5 Q&As); one specific CTA; length = SERP-median x1.2 (ceiling guide, not a quota). No `[EXTERNAL LINK]`/`[INTERNAL LINK]` placeholder brackets survive to publish; resolve links inline.

### Non-negotiable rules

- SERP study before drafting, always.
- Keyword in headline, first 100 words, and ≥1 subheading.
- Meta description under 155 chars including keyword.
- ≥1 internal link + ≥1 external credible source minimum (rubric raises this to 3 internal / 4–5 external).
- Author bio + credentials + dates visible (E-E-A-T).
- Authoritative claims, no hedging without a source.

### Banned words (blog)

leverage (verb), synergise, holistic approach, best-in-class, cutting-edge, game-changing, rapidly evolving, in today's world, paradigm, thought leader, robust, seamless, streamline (use simplify), utilise (use use), facilitate (use help). Plus banned AI openers: "In today's rapidly evolving…", "[Topic] has never been more important…", "With the rise of…".

---

## 2. Press release / PR-HARO pitch

**What it is:** Factual news announcement for journalists to republish near-verbatim.
**What it is NOT:** A blog, a sales pitch.

**When:** Product/feature launch, funding, named partnership, award, C-level hire, research stat, major conference.
**Tone + person:** Third person throughout. Neutral, journalistic. No opinions, no exclamation marks, ever. First person only inside quotes. Voice: [COMPANY]'s spokesperson byline from the brand brain.
**Length:** 400–600 words. Never more.

### Structure (exact order)

1. **FOR IMMEDIATE RELEASE** — top left, all caps, every time.
2. **Headline** — 65–80 chars, active verb, lead with result/benefit not company name. No adjective hype.
3. **Subheadline (optional)** — one sentence, under 120 chars, only if it adds new info.
4. **Dateline** — `City, Country, Date —` then straight into the first sentence.
5. **Lead paragraph (40–50w)** — Who/What/When/Where/Why; standalone story. Write last.
6. **Body paragraph 1 (60–80w)** — why it matters; back every claim with a number or named source.
7. **Quote 1 — [COMPANY] spokesperson** — only first-person spot; sounds like a real human, not marketing.
8. **Body paragraph 2** — product/announcement details, pricing, availability, access. Factual only.
9. **Quote 2 (optional)** — client/partner/investor, same rules.
10. **Boilerplate** — fixed company description: what [COMPANY] does, who it serves, and the [WEBSITE] link. Maintained in the brand brain; update quarterly.
11. **Contact line** — name | email | [WEBSITE] (pull the spokesperson contact from the brand brain).
12. **###** — three hashes, always, to signal end.

### Non-negotiable rules

- Third person throughout; never "we"/"I" outside quotes.
- Max 2 quotes; both must sound human.
- Headline active verb, under 80 chars, result-led.
- Lead answers 5 Ws in under 50 words.
- Output only the press release, no explanations.

### Banned words (press release)

revolutionary, game-changing, world-class, cutting-edge, best-in-class, disruptive, innovative, excited, thrilled, delighted, pleased, proud, paradigm shift, synergy, holistic, leverage (verb), utilise, facilitate.

---

## 3. White paper

**What it is:** Research-backed, in-depth document that names a serious industry problem and presents a [COMPANY] framework/methodology to solve it. Highest-value thought-leadership asset. Gated.
**What it is NOT:** A blog with headers, a product brochure, an opinion piece without data, a how-to guide.

**Tone + person:** Expert, authoritative, research-backed. Third person in research/data sections; first person allowed only in framework/methodology sections ("We've found…", "Across the companies we've worked with…"). Voice: [COMPANY]'s authoritative/founder byline from the brand brain.
**Length:** 2,000–5,000 words (6–12 PDF pages).

### Structure (exact order)

1. **Title page** — provocative, problem-focused, under 12 words; sounds like a finding not a guide. Plus the [COMPANY] author byline (name, title, company) + date, from the brand brain.
2. **Executive summary (150–200w)** — whole paper in miniature: the problem, why existing solutions fail, the framework, what to do. Write last.
3. **Table of contents** — required if over 3,000 words.
4. **Section 1 — The Problem (400–600w)** — data-heavy, industry stats, cost in money and people. Cite every major claim to named primary sources (per `workflows/standards/claims-integrity.md`). Write as a researcher.
5. **Section 2 — Why Existing Solutions Fall Short (300–400w)** — critique current approaches, never name competitors.
6. **Section 3 — The Framework/Methodology (600–900w)** — the IP. Name it. 3–5 named components, each with a subheading. First person OK here.
7. **Section 4 — Evidence and Proof Points (300–500w)** — 2–3 short anonymised examples with numbers.
8. **Section 5 — Recommendations (300–400w)** — numbered action steps usable this week, product-agnostic.
9. **Conclusion (150–200w)** — restate problem + core insight; one CTA.
10. **About [COMPANY] + References** — short company description + full linked source list.

### Non-negotiable rules

- Every claim needs a source or a number.
- Subheading every 400–500w max.
- No bullet-only sections; prose before and after every list.
- No product selling in the body; educate only. Product mentioned only in the closing CTA.
- Spell out every acronym on first use.
- Title sounds like a research finding, never a marketing guide.

### Banned words (white paper)

Same set as press release/blog hype list: revolutionary, game-changing, world-class, cutting-edge, best-in-class, disruptive, innovative, excited, thrilled, delighted, pleased, proud, paradigm, synergy, holistic, leverage (verb), utilise, facilitate, plus the marketing-fluff superlatives.

---

## 4. Case study

**What it is:** Before-and-after story about a real client proving [COMPANY] works. The client is the hero; [COMPANY] is the enabler. Numbers are the point.
**What it is NOT:** A product showcase, a press release about a client win, a story without numbers, [COMPANY]'s story.

**Tone + person:** Third person throughout. Narrative but precise. Numbers do the selling; the client quote carries the emotion.
**Length:** 600–1,200 words.

### Structure (exact order)

1. **Results headline** — lead with the outcome number, not the client name. e.g. "How a 300-Person E-Commerce Company Cut [Key Metric] by 42% in One Quarter."
2. **Client snapshot (50–80w)** — industry, size, employee count, geography, growth stage. Anonymise with a description if unnamed (e.g. "A Series B fintech in [City], 300 employees across three cities").
3. **The challenge (150–200w)** — exact problem + business impact in money/time/people. One client quote allowed here; it must describe the pain, not compliment [COMPANY].
4. **The solution (200–300w)** — what [COMPANY] did: process and approach, not feature list. What changed day to day. Reads like a story.
5. **The results (150–200w)** — minimum 3 hard metrics, each with a timeframe. Pattern: `[Metric] [improved/reduced/increased] by [X%] within [timeframe]`. End with the strongest client quote referencing the specific result.

### Non-negotiable rules

- Every result needs a number and a timeframe. No exceptions.
- Max 2 client quotes total.
- If unnamed, still give title + company type.
- Never list product features; describe what changed in their process.
- Always from the client's POV, never [COMPANY]'s.
- Banned vague language: "significantly improved", "better results", "more efficient" — replace each with a number.

---

## 5. Landing page

**What it is:** Standalone page with one goal — one action (sign up / start trial / book demo / download). Everything pushes toward that one action.
**What it is NOT:** A homepage, blog, full product page, or a page doing five things.

**Tone + person:** Direct, benefit-focused, second person. Every sentence is "you". Never about [COMPANY]-the-company. Brand-neutral (no personal byline).
**Length:** No fixed count — 300 to 1,500 words depending on trust needed. Every word earns its place.
**The single rule:** One page. One goal. One CTA. No nav menu, no unrelated links.

Before writing, every section answers one of: *What is this and is it for me? Why trust this? What do I do next?*

### Structure (every section in order)

1. **Hero** — Headline (core benefit, plain language, under 10 words, passes the 3-second test) + Subheadline (who it's for + what they get, under 30 words) + one Primary CTA button (action text, e.g. "Start Free Trial" / "Book a Demo") + supporting visual (product screenshot/demo, never stock office photos). Under 30 words above the fold.
2. **Social proof bar** — logos (5–8 max) or a stat line, immediately below hero.
3. **Problem statement (2–4 sentences)** — the exact pain, with empathy not drama. No heading needed.
4. **Solution / how it works** — Part A: one-sentence core solution. Part B: exactly 3 steps (number + 3–5 word title + one sentence each).
5. **Features as benefits (4–6 max)** — formula `[Feature] so you can [Benefit]`. Never raw features.
6. **Social proof in depth** — numbers first (3–4 stats), then 2–3 named customer quotes (name + title + company, specific result).
7. **Objection handling (3–4)** — neutralise top silent objections; weave in naturally, or a clean FAQ accordion at the bottom if more than 4.
8. **Final CTA** — 1–2 line closing benefit restatement + the same CTA button + a risk-reducer line below it (e.g. "No credit card required", "Free 14-day trial").

### Non-negotiable rules

- One CTA only; CTA appears at least twice (hero + bottom). The booking/demo CTA URL is only [COMPANY]'s approved booking/CTA link from the brand brain.
- Remove navigation menu (every nav link is an exit door).
- Second person always; benefits before features; active voice; sentences ≤20 words; paragraphs ≤3 lines.
- Numbers over vague claims; specificity over generality (name real customers/industries).
- No stock photography. Mobile-readable. Loads under 3 seconds. Zero spelling errors.

### Banned words (landing page)

revolutionary, game-changing, world-class, cutting-edge, best-in-class, next-generation, innovative, seamless, robust, leverage, synergy, holistic, empower, transform, disrupt, paradigm, end-to-end, best-of-breed, thought leader, future-proof, scalable solution, industry-leading. Replace each with a specific claim backed by a number.
