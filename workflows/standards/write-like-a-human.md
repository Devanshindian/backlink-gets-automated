# Write Like A Human — voice standard

The final voice pass: make persuasive prose sound like a person who has done the work, not a model. This is the concise standard for *voice* (stance, rhythm, plain words, real examples). It does NOT own the banned-word lists or the line-edit mechanics — those live in the avoid-ai-writing skill (see "The mechanical pass is mandatory" below).

## Scope (read first)

Apply to **persuasive, editorial, and marketing copy**: blog bodies, opinion sections, landing-page narrative, outreach pitches, thought pieces.

Do NOT force "voice" onto **functional docs** where tidy structure is correct: API references, exec briefs, step-by-step instructions, changelogs, comparison tables, spec sheets. There, clean and scannable wins.

**Voice governs prose, not scaffolding.** If the format requires a structure (TL;DR, question-style H2s, a self-contained answer per section, a table, an FAQ, callouts), keep that skeleton intact and write the PROSE inside it like a human. "Open with the conclusion" and "digress once" apply *within* sections, never as a license to delete required structure.

## Take a stance

- Have a point of view, not a neutral summary anyone could generate. Say what you'd actually advise and why.
- Where two reasonable people would disagree, pick a side and defend it.
- Address the reader directly: "you," "here's the thing."
- State the number, then name the source plainly. Don't hedge by citation ("according to a report, roughly..."). Confidence in voice — never invented data. Every stat still gets verified against its named primary source.

## Concrete over generic

- Replace every vague phrase with a specific: a named scenario, a real number, a before/after, an example of how the work actually happens. If a sentence could appear on any competitor's page, it's generic — rewrite it.
- Real advice has edges. Name when the approach does NOT work, the cost, the exception, the thing people get wrong. A page with no caveats reads as marketing, not experience.
- Don't just restate a stat — say what it means for the reader and what to do about it.

## Plain words

- Use contractions (it's, don't, we're) by default.
- Pick the plain word over the Latinate one: "more than" not "exceeds," "use" not "employ," "so" not "therefore," "about" not "approximately."
- A bright non-expert should follow every sentence on first read. Explain any term you must use, in-line, the first time. One idea per sentence; if it needs re-reading, split it. Simple, not dumbed-down — keep the substance, drop the complexity in how it's said.
- A casual aside (the way people actually talk) goes in parentheses or commas.

## Vary the rhythm

- Vary sentence length hard. Follow a 30-word sentence with a 4-word one. Never three sentences in a row with the same length or shape.
- Use fragments occasionally. For emphasis. Like this.
- Start some sentences with And, But, So.
- Vary sentence TYPE, not just length: mix in a question, a command, a one-word reaction. Not every line is a declarative.
- Vary your opening sentence shape every paragraph. Don't let two paragraphs start the same way.
- Don't write tidy point-by-point order inside a section. Open with the conclusion, the objection, or a concrete scene. Digress once per piece (once, not five times) — bury a good detail mid-paragraph instead of flagging it.

## No chatbot voice

- No closers or reassurance: "I hope this helps," "Let me know if," "Feel free to," "Happy to," "Great question," "Hope that makes sense," "Let's dive in."
- Don't narrate what you're about to do ("First, let's look at..."). Just do it.
- End on the last real point. No wrap-up, no offer, no summary sentence. (A deliberate CTA block is a separate element, not a chatbot closer.)

## Kill padding and hedging

- Cut on sight: restated points, throat-clearing intros, sentences that only set up the next sentence, examples that repeat the prior one, adjectives doing a number's job.
- Never pad to hit a word count, and never manufacture stats/tables to tick a rubric. If the best version is shorter, ship it shorter. If an element would force filler, drop the element, not the quality.
- One-test: for each paragraph ask "what does the reader now know that they didn't?" If nothing, delete it.

## The human-experience rewrite (never ship model output verbatim)

The piece must read like a person who actually did this work wrote it. Do not accept a model draft as-is — rewrite it. Add a real point of view, concrete details and examples, at least one caveat or tradeoff, varied rhythm, and original analysis (not just restated facts). Where the format allows first person, add a first-hand marker framed as an observed pattern ("A pattern I keep seeing...", "Across the teams I've worked with...") — never a fabricated memory or invented fact. Originality lives in framing and analysis, never in the data.

## The mechanical pass is mandatory (avoid-ai-writing)

Voice work alone is not enough. Prompting *reduces* AI tells; only line-editing *removes* them. So after the voice pass above, the mechanical anti-AI pass is a required final step — it owns the banned-word list, AI-cliché detection, em-dash/forbidden-character handling, and the line-by-line edits this standard deliberately does NOT duplicate.

Run it via the skill at:
`workflows/00-foundation/scripts/brand-brain/avoid-ai-writing/SKILL.md`

That pass (and not this doc) is the single source of truth for: which words/phrases/characters are banned, copula-avoidance and "-ing fake depth" fixes, negative-parallelism cliches, transition signposts, and the iterate-to-convergence line edit.

**Company-specific banned words and voice** (the words *this* company never uses, its tone, its first-person framing) live in `projects/[COMPANY]/brand-brain/`. Load that before the avoid-ai-writing pass so its house list runs alongside the generic one.

## Priority

If you can only enforce two rules: **vary sentence length**, and **kill the transition + chatbot words**. Those two clear most of the robotic feel. Then run the avoid-ai-writing line edit — it's what actually moves a draft from "sounds like a model" to "sounds like a person."
