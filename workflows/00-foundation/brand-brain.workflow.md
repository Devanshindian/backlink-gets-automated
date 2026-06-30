---
type: workflow-recipe
stage: foundation
reusable: any company
inputs: [WEBSITE domain, the top-pages list (projects/[company]/semrush-top-pages.csv)]
produces: projects/[company]/brand-brain/ (7 files + voice-data/)
worked_example: projects/testlify/brand-brain/  (a filled set - copy its shape)
last_updated: 2026-06-22
---

# Recipe — Brand Brain

## What this does
Learn exactly how a company writes - from its own best pages - and lock it into a small set of files, so
anything we write later sounds like the company and never like AI. The hub file is `brand-brain.md`: read
that one file and you can write in the company's voice.

## What you end up with (all under `projects/[company]/brand-brain/`)
We build these **in order** (the steps below). Each step produces or adds to one of these:
- `page-shortlist.md` - the 20-40 best pages we studied (the evidence trail).
- `voice-data/` - the raw measurements: 6 JSON files the analyzers spit out.
- `voice-analysis.md` - the read of the voice (tone score + the do/don't patterns, with real examples).
- `brand-brain.md` - **THE HUB**, assembled across steps 2, 5 and 8 (company -> voice -> style rules).
- `brand-assets.md` - logo, fonts, colours, key links, CTAs.
- `stats.md`, `stories.md`, `opinions.md` - real numbers / anecdotes / strong opinions. Started as stubs,
  filled by asking the user (Step 7) and topped up over time.

---

## Inputs you need
- `[WEBSITE]` (the public site) + any brand/voice guidelines the company already has.
- `projects/[company]/semrush-top-pages.csv` (from the Semrush step - picks which pages to study).

---

# The steps (in order)

## Step 1 - Shortlist the pages -> `page-shortlist.md`
**What you do:** from `semrush-top-pages.csv`, pick the **20-40 pages** worth learning the voice from, and
write them into `page-shortlist.md`. Take the top-traffic winners, then *deliberately add* the commercial
and positioning pages even if their traffic is low (homepage, pricing, competitor/"alternatives", product) -
voice matters most exactly there, and raw traffic alone misses them.

**`page-shortlist.md` contains:**
- A header: the **source** (`projects/[company]/semrush-top-pages.csv`), the **date**, a one-line *why
  these pages*, and a note that the number beside each page is its estimated monthly traffic.
- A **grouped list of 20-40 pages**, bucketed by page type, each line = `URL  (traffic, short note)`.
  Buckets (rename to fit the company): **A.** positioning/commercial (homepage, why-us, pricing, compare,
  competitor/alternatives, integrations); **B.** money/product pages; **C.** top blogs; **D.** tools/
  calculators; **E-F.** glossaries; **G.** interview/Q&A pages; **H.** templates.
- A closing line: "analysed in `voice-analysis.md`".

## Step 2 - Read the shortlist, sketch who the company is -> start `brand-brain.md`
**First, pull clean readable copies of the pages so you read prose, not raw HTML.** Run the extractor
(it reuses the vendored page extractor on the shortlist URLs and saves one clean markdown file per page):
```
node workflows/00-foundation/scripts/brand-brain/extract-pages.mjs [company]
```
This writes `projects/[company]/brand-brain/pages/*.md`. (This is just for reading - the analyzer step
fetches its own copy separately; fetching twice is fine, both are one-time.)

**Then read those page files** and, from that reading, write the **top three sections of the hub** (we'll
come back and finish `brand-brain.md` in steps 5 and 8):
1. **What the company is** - what it sells, the money pages, proof points, named competitors.
2. **Who we talk to** - the audience (who the writing is aimed at).
3. **Positioning / value prop** - the core promise, in the company's own words.

Leave the rest of `brand-brain.md` as headers for now (Voice & tone, Style rules, Anti-AI guard, etc.).

> The extractor is **article-tuned** - it cleans blog / glossary / interview pages well, but on a
> **homepage / pricing / landing page** it can strip out feature grids and pricing tables (exactly where
> "what the company is" lives). The script flags pages that came out thin; **open those live too.**

## Step 3 - Run the six analyzers -> `voice-data/*.json`
**What you do:** run the driver (it reads the URLs from `page-shortlist.md`, fetches each page, builds a
clean text corpus, runs all six analyzers):
```
node workflows/00-foundation/scripts/brand-brain/voice-analyser-run.mjs [company]
```
This writes six JSON files into `projects/[company]/brand-brain/voice-data/`:
- `voice.json` - how it addresses the reader (you/your vs I), hedging, passive ratio, the hollow
  intensifiers / AI cliches / marketing-speak it uses.
- `punctuation.json` - dash/comma habits + the real em-dash count.
- `vocabulary-tiers.json` - how formal its words are + the AI-slop words (with plain-word swaps).
- `phrase-library.json` - candidate openings, transitions, recurring/caveat phrases.
- `vulnerability-patterns.json` - how it admits limits / hedges.
- `specificity-patterns.json` - "their/your X" (specific) vs "the X" (generic).

(Each file holds more than this one-liner - the full field-by-field breakdown is the mapping table in Step 4.)

## Step 4 - Score the voice -> `voice-analysis.md`
**What you do:** apply the 3-layer method above to the numbers in `voice-data/`, then **curate the examples
by hand**. This is the heart of the recipe. Write `voice-analysis.md` with these sections, in order:

1. **Header** - the date, "based on N pages (see page-shortlist.md)", and a one-line method note.
2. **Consistency check** - is the voice consistent, or scattered across authors/pages? If scattered
   (multi-author site), the decision: codify the **best** version (usually the newest flagship pages), not
   the average.
3. **Tone fingerprint (layer 1)** - score the **4 Nielsen Norman dimensions** (which end of each dial, with
   one phrase of proof) + the **one-line summary**.
4. **Measured rules (layer 2)** - the numbers, turned into do/don't rules. **Work through the mapping table
   below file by file and write a finding for every row marked §4 - do not stop at the first few.** That
   covers: the address-the-reader ratio, passive ratio, formality score, the full punctuation profile
   (em-dash, exclamation, semicolon, colon, quotation style), the plain-word swaps, and the banned lists
   (hollow intensifiers, AI cliches, AI slop). Three files (`vocabulary-tiers`, `vulnerability`,
   `specificity`) also ship their own `recommendations` / `interpretation` / `guidanceText` strings - read
   those; they're a first draft to adapt, never to paste.
5. **Recurring patterns, with real examples (layer 3)** - the "do this" patterns, **each with real lines
   pulled from the pages**. Again, **cover every row marked §5 in the table** (openings, transitions,
   conversational markers, identity markers, hedges/caveats, possessive vs generic, dominant topics) plus
   structure (H2 style, FAQ block), the exact CTAs, recurring brand lines, and sentence rhythm.
6. **Target voice** - if multi-author, name the best/newest pages as the bar to pull everything up to.
7. **AVOID** - the real weak patterns found on *this* site (boilerplate, puffery, grammar slips,
   inconsistent CTA casing, em dashes) + the standard AI tells.

**The mapping table - every meaningful field across the six files. Work through every row; don't cherry-pick.**
(`§` = which `voice-analysis.md` section the row feeds.)
| JSON | fields | turn it into | feeds |
|---|---|---|---|
| `voice.json` | `firstPerson` / `secondPerson` (counts) | who it addresses - you/your vs I | §4 |
| | `passiveVoiceRatio` | active-vs-passive rule | §4 |
| | `hollowIntensifiers`, `aiCliches`, `marketingSpeak` (w/ alternatives) | banned-word lists (with swaps) | §4 + §7 |
| | `hedgingLanguage`, `certaintyMarkers` | how tentative vs assertive it sounds | §5 |
| | `conversationalMarkers` | conversational tone words ("look", "well") | §5 (+§3) |
| | `openingPatterns` | how sentences/sections open | §5 |
| | `identityMarkers` (genuineInterest/humbleHelper/transparency) | personality signals | §5 (+§3) |
| | `collegialPatterns`, `signatureHedging`, `equipmentSpecificity` | signature moves; "your X" vs "the X" lean | §5 |
| `punctuation.json` | `dashTypes` + `dashConsistency.aiDetectionFlag` | the em-dash rule | §4 |
| | `commaDensity`, `semicolonFrequency`, `colonFrequency`, `parentheticalFrequency`, `ellipsisFrequency`, `quotationStyle` | punctuation mechanics | §4 |
| | `exclamationFrequency` | if ~0, lock the no-exclamation rule | §4 + §7 |
| `vocabulary-tiers.json` | `formalityScore`, `totalFormalWords` | how formal (words per 1000) | §3 + §4 |
| | `formalVerbs` / `formalAdjectives` / `formalAdverbs` (`suggestedAlternatives`) | plain-word swaps (provide->give) | §4 |
| | `aiSlop` (`suggestedAlternatives`) | AI-slop banned list (with swaps) | §4 + §7 |
| | `recommendations` | the tool's own flags - a first draft | §4 |
| `phrase-library.json` | `openingPatterns` (personalStory/directAction/protectiveWarning) | real opening shapes | §5 |
| | `transitionPhrases` | how it moves between ideas | §5 |
| | `caveatPhrases` | real caveats / hedges | §5 |
| | `equipmentReferences` (withPossessive/generic) | specific vs generic phrasing | §5 |
| `vulnerability-patterns.json` | `mistakeAdmissions` / `uncertaintyMarkers` / `limitationStatements` | whether/how it admits limits | §5 |
| | `vulnerabilityScore` + `interpretation` | confident vs hedging (one-line read) | §3 + §5 |
| | `guidanceText` | ready-made "how to replicate" block - adapt it | §5 |
| `specificity-patterns.json` | `possessivePatterns` / `genericPatterns` + `specificityRatio` | "your X" vs "the X" balance | §4 + §5 |
| | `dominantNouns` | the topics it writes about (ability, hiring, tests) | §1 + §5 |
| | `interpretation` + `guidanceText` | ready-made read + how-to - adapt it | §5 |

> Curate the phrase/example rows by hand - on multi-author sites they pick up noise (e.g. candidate sample
> answers). And **never paste `guidanceText` / `interpretation` / `recommendations` verbatim** - they're a
> draft to adapt, not final copy.

**Detailed example - a slice of `voice-analysis.md` (real Testlify numbers). This shows the *format*; your
real output writes a line for *every* table row above, pulling from all six files - not just these.**
```markdown
## 3. Tone fingerprint (Nielsen Norman)
- Funny <-> Serious:        Serious (explains, doesn't joke)
- Formal <-> Casual:        Leans casual - talks to "you"; but formalityScore 15/1000 (moderately formal words)
- Respectful <-> Irreverent: Respectful (never mocks the reader or rivals)
- Enthusiastic <-> Matter-of-fact: Matter-of-fact; vulnerabilityScore 0.08 = "rarely hedges, sounds confident"
One-line summary: a hiring expert talking to a busy recruiter - plain, direct, confident, not salesy.

## 4. Measured rules (one finding per §4 row - across ALL files)
voice.json
- Address the reader: "you" x303, "your" x224 (~1.0/100 words); "I" almost never. RULE: write to "you", avoid "I/we".
- Passive voice: 31% of sentences (a bit high). RULE: prefer active ("the test scores candidates").
- Ban hollow intensifiers: "honestly", "genuinely", "really". Ban AI cliches: "dive into", "delve into", "unlock".
punctuation.json
- Em dashes: 6 in 50k words (en-dash x20, hyphen x1315). RULE: no em dashes - comma / full stop / spaced hyphen.
- Exclamations: ~0.2/1000 = basically none. RULE: no exclamation marks. Quotes: single. Colons used freely.
vocabulary-tiers.json
- formalityScore 15/1000 (moderate). Plain-word swaps: provide->give, require->need, additionally->also.
- Ban AI slop (swap in plain word): optimize->improve, robust->strong; dynamic / strategic / innovative -> rewrite.
- Tool's own flag: "CRITICAL: 15 AI slop words - remove."
specificity-patterns.json
- specificityRatio 0.31 = balanced, slight lean to "their/your X". RULE: prefer "your candidates" over "the candidates".

## 5. Recurring patterns (one finding per §5 row - across ALL files, curated by hand)
- phrase-library openings: "Hiring the right candidate is..." (lead with the reader's problem; pick 3-4 real ones).
- voice conversational markers: "look", "well" appear often -> keep a light conversational tone.
- voice identity markers: leans "humble helper / transparency" -> guide the reader, don't boast.
- vulnerability hedging: "However...", "might be", "can be complex" -> short honest caveats (adapt its guidanceText).
- specificity dominant topics: ability, hiring, tests, skills, talent.
- CTAs: exact on-site text - "Book a demo", "Start free trial" (note the casing).
```
*(Numbers are read straight from `voice-data/`; the example sentences are curated by hand - keep the real
brand lines, drop the tool's noisy picks.)*

## Step 5 - Turn the read into the hub's Voice & Tone -> `brand-brain.md`
**What you do:** distill `voice-analysis.md` (the long evidence file) into the **Voice & tone** section of
`brand-brain.md` (the short hub a writer reads before drafting). This is a **distillation, not a copy** -
the hub carries the *rules*, the evidence file keeps the *numbers*.

**The translation rule (apply to every finding in `voice-analysis.md`):**
- **Turn each measured finding into an instruction, and drop the number.** "you x303 / your x224, I almost
  never" -> *"Write to 'you'; don't use 'I/we'."* The count stays in `voice-analysis.md` as the audit
  trail; the hub gets the rule only.
- **Keep 2-3 real example lines** (openings, CTAs, a caveat) - a writer needs real samples to match the
  rhythm, not just rules. Point to `voice-analysis.md` for the full set.
- **Don't duplicate.** The full banned-word lists and the mechanical style rules go to the Style-rules and
  Anti-AI sections built in **Step 8** - the voice chart can reference them, but doesn't repeat them.

**The Voice & tone section contains, in this order:**
1. **The dials + one-line summary** - carried over from `voice-analysis.md` §3 (the 4 Nielsen Norman
   dimensions + the one-liner). The orientation.
2. **Voice chart** - a `Trait | Do | Don't` table, **one row per voice trait**, built by collapsing the §4
   measured rules and §5 patterns into Do/Don't pairs. Cover at least: how to address the reader, formality
   level, sentence voice (active/passive), punctuation mechanics, vocabulary, confidence/hedging, openings,
   and conversational warmth.
3. **Tone by page type** - a short list of how the same voice flexes: money/product page (tight, benefit-led,
   CTA-forward) vs blog (more conversational, examples) vs comparison/competitor (factual, fair, no
   trash-talk) vs glossary (plain, definitional).
4. **A few exemplars** - 2-3 real opening lines + the exact CTAs, with a pointer to `voice-analysis.md`.

**Detailed example - the Voice & tone section for Testlify (built from the voice-analysis findings):**
```markdown
## Voice & tone
**Dials:** serious · leans casual (talks to "you") · respectful · matter-of-fact.
**In one line:** a hiring expert talking to a busy recruiter - plain, direct, confident, not salesy.

| Trait | Do | Don't |
|---|---|---|
| Address the reader | Write to "you" / "your" | First person ("I", "we") |
| Formality | Plain, professional words | AI slop (optimize, robust, dynamic); hollow intensifiers (honestly, really) |
| Sentence voice | Prefer active | Don't drift into passive (it already runs ~31%) |
| Confidence | State findings directly | Over-hedge - the brand rarely does |
| Punctuation | Commas, full stops, single quotes | Em dashes; exclamation marks |
| Vocabulary | Swap to plain words (provide->give) | Formal/abstract verbs |
| Openings | Lead with the reader's problem | Generic "In today's world..." |
| Warmth | A light conversational touch ("look", "well") | Stiff corporate tone |

**Tone by page type:** money/product pages = tight + benefit-led + a clear CTA; blogs = more conversational,
real examples; competitor/comparison = factual and fair, never trash-talk; glossary = plain and definitional.

**Exemplars:** openings like "Hiring the right candidate is..."; CTAs "Book a demo", "Start free trial".
(Full evidence + counts in `voice-analysis.md`.)
```

## Step 6 - Capture the visual + link assets -> `brand-assets.md`
**What you do:** pull from the live homepage HTML and write `brand-assets.md`:
- **Logo** - primary SVG/PNG, icon/favicon, default social image (the `og:image`/`twitter:image` URLs).
- **Typography** - font family + weights (`fonts.googleapis` / `font-family`).
- **Colours** - a table `Role | Hex | Source` (brand primary, heading/body text, backgrounds, borders,
  accents) - the most-frequent `#hex` values, cross-checked against any brand notes.
- **Key links** - the ONE correct demo/booking link, homepage, pricing, the money pages, login.
- **Standard CTAs** - the exact button text used on-site, standardised.

## Step 7 - Stats / stories / opinions: make the stubs, then ask the user
These three files hold things we must **never invent** - they're filled by asking the user and topped up
over time. Create each as a stub (a "how to add" template + an empty list), then **ask the user all the
relevant questions for their particular industry** to fill it. The aim is SEO: original stats and strong,
sourced opinions are what earn citations and backlinks and pass Google's E-E-A-T bar - so ask whatever
draws those out for *this* company's field.

**`stats.md`** (canonical real numbers - so content never improvises a figure). Seed it with numbers you
can verify on the live site / public sources (note the source), then ask the user for the rest - the real
numbers that matter in their field (scale, proof/results, customers, pricing, credibility/ratings, and any
unique internal data they'd publish - those are the **backlink magnets**). For each: the exact number, the
date/source, and "OK to publish?"

**`stories.md`** (approved anecdotes - real examples raise trust, dwell time, shareability). Ask the user
for the real stories that matter in their field (customer wins, the origin story, a lesson learned,
behind-the-scenes). For each: the story in 2-4 sentences, the point it makes, any number (link to
`stats.md`), who approved it.

**`opinions.md`** (approved strong opinions - point-of-view content ranks, earns links, differentiates).
Ask the user for the strong, defensible takes in their field (beliefs others get wrong, practices they're
against, predictions). For each: the opinion in one line, the **number/evidence backing it**, why they
believe it, who approved it. (One opinion per post max, always backed by a real number.)

## Step 8 - Finish the hub -> `brand-brain.md`
**What you do:** complete the remaining `brand-brain.md` sections so the whole file reads top-to-bottom as:
1. What the company is · 2. Who we talk to · 3. Positioning *(done in Step 2)*
4. **Voice & tone** *(done in Step 5)*
5. **Style rules (concrete)** - openings, structure, how to address the reader; evidence (numbers from
   `stats.md`, never round); one story max (`stories.md`), one opinion max (`opinions.md`); the "say when
   NOT to use us" honesty tell; vocabulary; sentence mechanics (no em dashes); the CTAs + demo link.
6. **Anti-AI guard** - the company-specific banned buzzwords + no exclamation marks/emojis + the
   hedging/tricolon/signposting tells. **Write the anti-AI file's path into `brand-brain.md` itself, as a
   hard rule** - both as a banner at the very top of the file and in this section, worded like:
   > **HARD RULE - read before writing anything:** before you draft or publish any article, page, or piece
   > of copy, you must read and run `workflows/00-foundation/scripts/brand-brain/avoid-ai-writing/SKILL.md` as the final
   > line-edit pass. No draft ships without it.

   (Remember: prompting reduces AI tells; only line-editing removes them - so this pass is mandatory, not
   optional.)
7. **Brand assets summary** - brand colour, font, logo, demo link (full list -> `brand-assets.md`).
8. **Voice-test rubric** - an 8-point checklist to run on every draft (sounds like a real expert; opens
   strong; second-person / benefit-framed; has a real sourced stat; right structure; CTAs correct; clean of
   AI tells; clean grammar/rhythm).
9. **Companion reference files** - `stats.md`, `stories.md`, `opinions.md`.
10. **Sources** - `voice-analysis.md`, `brand-assets.md`, `page-shortlist.md`, any interview notes.

---

# Gotchas (and when each applies)
- **Step 1 (shortlist):** raw traffic misses the product/pricing pages where voice matters most - add them
  by hand.
- **Step 3 (run the tool):** the corpus is the page-shortlist pages. Keep the laptop awake if it's slow.
  If the analyzers aren't built yet, do the one-time `npm install && npm run build` in
  `scripts/brand-brain/voice-analyser/` first.
- **Step 4 (curate):** trust the JSON numbers; the tool's example phrases are noisy on multi-author sites -
  curate them by hand. If the voice is scattered, codify the best/newest pages, don't average the mess.
  Never ship the tool's own auto-`SKILL.md`.
- **Step 7 (stubs):** never invent stats/stories/opinions. `stats.md` gets only verifiable numbers (with a
  source); stories/opinions stay empty until the user gives and approves real ones.
