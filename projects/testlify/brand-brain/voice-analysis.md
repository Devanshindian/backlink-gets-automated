# Voice Analysis — Testlify

1. **Based on:** 30 pages (see `page-shortlist.md`), 51,361 words, fetched 2026-06-22.
   **Method:** the six analyzers in `voice-data/*.json` give the measured numbers; the example lines are
   curated by hand from the pages. Three layers — tone fingerprint (Nielsen Norman) + measured rules +
   real exemplars.

## 2. Consistency check
Testlify is a **multi-author site** (3,299 indexed pages). The corpus shows two voices:
- **Informational pages** (blogs, glossary, interview Q&A) — plain, direct, reader-facing, evidence-led.
- **Commercial pages** (homepage, product, comparison, "alternatives") — the same backbone, but loaded with
  marketing/AI vocabulary (`seamless` ×16, `leverage` ×11, `robust` ×11, `empower` ×8, `dynamic` ×31).
The analyzers found **no personal identity markers** (genuineInterest/humbleHelper/transparency all 0) —
this is a company voice, not a personal one. **Decision: codify the best version** = the plain, "you"-facing
blog voice, and pull the commercial pages **up to it** by stripping the marketing words. We do not average
the two.

## 3. Tone fingerprint (Nielsen Norman)
- **Funny ⟷ Serious:** **Serious.** Explains and instructs; never jokes.
- **Formal ⟷ Casual:** **Middle, leaning professional.** Talks straight to "you" (casual signal) but uses
  formal verbs heavily (`provide` ×94, `require` ×64, `maintain` ×38; formalityScore 15/1000).
- **Respectful ⟷ Irreverent:** **Respectful.** Even the head-to-head pages describe rivals neutrally and
  fairly — no trash-talk.
- **Enthusiastic ⟷ Matter-of-fact:** **Matter-of-fact and confident.** vulnerabilityScore 0.08 ("very low —
  rarely admits limitations"); states findings as fact. (Commercial pages add a promotional tinge.)
- **One line:** *a hiring expert talking to a busy recruiter — plain, direct, and confident, not salesy.*

## 4. Measured rules (from `voice-data/` — one finding per source)
**`voice.json`**
- **Address the reader:** heavy second person — "you" ×302, "your" ×221 (~1.0/100 words). First person almost
  never (0.03/100). **RULE:** write to "you"; avoid "I/we".
- **Passive voice:** 30.7% of sentences (a bit high). **RULE:** prefer active ("the test scores candidates",
  not "candidates are scored").
- **Hedging:** 0.32/100 (might, may, could, probably). Confident overall (see vulnerability). **RULE:** hedge
  only when honestly warranted, not by reflex.
- **Ban hollow intensifiers:** `truly` (×7), honestly, genuinely, really, "the real".
- **Ban AI clichés (they appear — strip them):** `seamless`/`seamlessly` (×24), `leverage`/`leveraging` (×16),
  `robust` (×11), `unlock` (×5), `delve` (×4), `dive into`, `elevate your`.

**`punctuation.json`**
- **Em dashes:** only 7 in 51k words (en-dash ×17, hyphen ×1307; 98% hyphen-dominant). **RULE:** no em dashes
  — use a comma, a full stop, or a spaced hyphen.
- **Exclamation marks:** ~0.21/1000 = essentially none. **RULE:** no exclamation marks.
- **Quotes:** single. **Colons:** very frequent (9.97/1000 — listicle/heading style). **Semicolons:** rare
  (0.60). **Parentheticals:** common (4.77). Commas: ~1.04/sentence. **RULE:** match this — colon-led lead-ins
  and lists are on-brand; semicolons are not.

**`vocabulary-tiers.json`**
- **Formality:** 15 formal words/1000 (moderate). Tool flag: *"MODERATE FORMALITY — consider simplifying."*
- **Plain-word swaps:** provide→give, require→need, maintain→keep, implement→use, perform→do, demonstrate→show.
- **Ban AI slop (swap in the plain word):** dynamic→rewrite, optimize→improve, strategic→rewrite,
  innovative→rewrite, robust→strong, leverage→use, seamless→smooth, empower→enable, unlock→discover,
  delve→explore, elevate→improve, transform→change. Tool flag: *"CRITICAL: 15 AI-slop words — remove."*

**`specificity-patterns.json`**
- specificityRatio 0.31 ("balanced"). Slight lean to possessive ("their/your X"). **RULE:** prefer
  "your candidates" over "the candidates" when it reads naturally.

## 5. Recurring patterns (real examples — curated)
- **Openings:** mostly direct-action / problem-first (phrase-library: directAction 39, protectiveWarning 34,
  personalStory 5). E.g. blogs open on the reader's problem or a plain definition, not a personal anecdote.
- **Structure:** listicle DNA — lots of H2/H3, colon-led lead-ins, pros/cons blocks, numbered "how it works"
  steps, FAQ blocks. Comparison pages run a fair "What is X? / What is Y?" structure.
- **Conversational warmth:** light touches — "look" (×45), "well" (×35), "simply" (×4), "actually" (×3).
  Keeps it human without going chatty.
- **Confidence / hedging:** very low vulnerability (0.08) — states things as fact; the few caveats are
  pros/cons honesty on comparison pages ("may not be cost-effective for smaller organizations").
- **Evidence:** leans on hard numbers and proof (1,500+ teams, 55% faster, 4,500+ roles) — see `stats.md`.
- **CTAs (exact on-site text):** "Try for Free", "Book a Demo", "Login".
- **Dominant topics (what it writes about):** ability, skills, tests, hiring, talent.

## 6. Target voice
Pull everything up to the **plain, "you"-facing, evidence-led blog voice**: direct openings, active sentences,
real numbers, light conversational touches — **minus** the marketing vocabulary that creeps into the
commercial pages. The newest informational pages are the bar.

## 7. AVOID (real weak patterns found on this site + standard AI tells)
- **Its own marketing vocabulary** — the AI-slop words above are over-used on commercial pages; strip them.
- **Drifting passive** (already ~31%).
- **Formal verbs** where a plain one works (provide→give).
- **Boilerplate/puffery** on product pages; em dashes; exclamation marks; emojis.
- **Standard AI tells:** "In today's world…", "It's important to note", tricolons, hollow intensifiers
  (truly), over-signposting.
