# Claims integrity + authority honesty (authoring contract)

The contract for any factual claim in [COMPANY] content. It exists to kill the single worst failure mode: a confident, fabricated, or scope-inflated claim shipping live.

## Autonomous posture (no human in the loop)

AI makes the publish decision and publishes for release with no pre-publish human gate. Accuracy is enforced by **machine verification before publish**: every stat is fetched and confirmed against its source, and anything that cannot be verified is cut rather than shipped. Publishing does not wait on a human.

After publish, the content team gets a review ticket: they review the live post in a **post-publish review**, not a pre-publish gate. The claims ledger in the ticket is what makes their review fast, and the backup is the rollback path if they find an error.

## ROLE framing (set this before writing)

Write as a subject-matter expert for [AUDIENCE], the specific buyer defined in the brand brain — write to the exact reader, at a depth they respect. Pick that exact reader and write to them, not to their category in general.

No generic filler. If a sentence would survive on any vendor's blog, it is filler. Cut it or make it specific.

## Rule 1 - Statistics: zero tolerance for invention

- Use a statistic ONLY if you can name the exact figure AND a specific, nameable source. No "studies show", no "research suggests", no number rounded from memory.
- **Source whitelist (named primaries):** the approved tiered list, freshness rules, and linking density live in `workflows/standards/source-authority.md`. A government or primary research body beats a secondary blog. Prioritize Tier 1; cite Tier-2 vendors' research, not their products. [COMPANY]'s own first-party data is allowed only when actually supplied (see Rule 4).
- **NEVER cite a competitor as a source** (the competitor list and the no-competitor rule are owned by `workflows/standards/content-policy.md`). Their data is off-limits even when convenient.
- While drafting, tag each stat inline in this exact format so it is easy to find and verify:
  `[STAT: figure | source | year | exact URL | CONFIDENCE: high/med/low]`
- If you cannot produce a real URL and the exact figure, DO NOT use the stat. State the point qualitatively or omit it. Never approximate a number to sound authoritative.
- **Autonomous verification gate (replaces human checking).** Before publish, for every stat: fetch the source URL, confirm it returns 200 AND that the exact figure (or a figure that directly supports the claim) actually appears in the source. A stat that fails any of these - no 200, figure not found, source is a hub/redirect, or CONFIDENCE low - is **DROPPED**, not published. Never ship an unverified number on the assumption someone will check it later. No one will.
- **Prefer 4 verifiable stats over 12 impressive-sounding ones.** Density of proof, not volume.

## Rule 2 - Self-consistency check (blocks publish)

Before publishing, list every number used and confirm none contradict each other (any two percentages, an ROI figure, and a time-based metric must all reconcile and not imply impossible math). Output `Consistency check: PASS/FAIL + any conflicts`. A FAIL blocks publish - fix the conflict autonomously (re-verify or drop the offending stat), then re-run. Do not publish on FAIL.

## Rule 3 - Authority honesty (topic-product fit)

Position [COMPANY] precisely where it genuinely wins, and nowhere else.

- [COMPANY]'s true scope — its real capabilities AND what it does NOT do — comes from `projects/[company]/brand-brain/`. Position [COMPANY] only where it genuinely wins; when the topic is broad, write the broad context honestly, then locate [COMPANY] only at the slice it truly owns. Never imply coverage it lacks.
- Claiming one slice well beats claiming the whole stack vaguely. [COMPANY] integrates with parts of the wider stack; it does not replace what it does not do.

## Rule 4 - Differentiation + [COMPANY] stories/use cases (autonomous)

- The piece must say something only [COMPANY], or someone who has done this work, would say: a point of view, a non-obvious tradeoff, a real workflow.
- **Write stories/use cases on [COMPANY]'s behalf** to make it concrete. Allowed: clearly-illustrative, explicitly-hypothetical scenarios framed as illustrative, not as real events. Tie each to a genuine [COMPANY] capability and, where you make a quantified claim inside the scenario, anchor it to a verified third-party stat (Rule 1), not an invented result.
- **HARD BAN, never autofilled:** a named or implied real customer, a fake quote, a logo/brand claim, or any fabricated first-party metric (win rate, conversion delta, NPS, customer count, or any other). Use real [COMPANY] first-party data ONLY if it is actually supplied to you in this run. If it is not, do not leave a placeholder and do not invent one - differentiate with verified public data + genuine product capability + clearly-hypothetical use cases instead. Since there is no human to fill a slot, there are no `[INSERT ...]` placeholders in autonomous mode; resolve differentiation fully before publish.

## Rule 5 - Claims ledger (autonomous self-audit + audit trail)

Build a CLAIMS LEDGER of every factual/statistical claim. In autonomous mode it serves two purposes: it is the self-audit the AI runs before publish, and it is the rollback trail after.

| Claim | Figure | Source | Year | URL | HTTP | Verified? |
|---|---|---|---|---|---|---|

- **Self-audit (pre-publish):** every row must be `HTTP 200` AND `Verified? = yes` (figure confirmed present in the source). Any row that is not verified means the claim is **cut from the content** before publish - the ledger cannot contain an unverified claim that also survives in the body.
- **Audit trail (post-publish):** the final ledger is written into the review ticket so any error is traceable and the page can be reverted from its backup. This is a record, not a request for human sign-off.
- The ledger NEVER appears in the published page body.

## Reconciliations with the publish gates (do not skip)

- **Brackets are draft-only.** `[STAT: ...]` is an internal working marker. The verification gate FAILS publish on any leftover `[` token, so every bracket must be resolved before deploy: the stat is verified and rewritten as clean prose with its link, or it is dropped. There are no `[INSERT ...]` human-fill slots in autonomous mode. Zero `[` in the live body.
- **Voice still applies.** After claims are locked, the piece still passes the voice/humanizer pass in `workflows/standards/write-like-a-human.md`. Verifiable does not mean robotic.
- **No em dashes / forbidden characters / banned words**, same as everywhere.

## Cite, do not promote; cap per domain

- A citation is EVIDENCE for one stat, not an endorsement. Never write "X has a guide", "pairs well with X's resource", or otherwise promote/drive traffic to another brand's content. State the fact, cite the source (neutral, nofollow), move on. The full cite-don't-promote and competitor rules live in `workflows/standards/content-policy.md`.
- **No more than 2 citations from the same external domain in a single post.** If one primary source is already cited twice, the next stat MUST come from a different primary domain or be dropped. Aim for 3+ distinct domains.
