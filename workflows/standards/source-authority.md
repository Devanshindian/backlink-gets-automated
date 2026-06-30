# External linking, citation & source authority

The canonical source-selection + external-linking contract for [COMPANY] content (write + refresh). Pairs with `workflows/standards/claims-integrity.md` (verify/never-fabricate) and the competitor-exclusion + outbound-`rel` rules in `workflows/standards/content-policy.md`.

## House reconciliations (these win on conflict)

1. **Direct competitors are NEVER cited or linked** — not as a source, not for a stat, not for "context". The competitor list and this rule are owned by `workflows/standards/content-policy.md`. This overrides any tier below.
2. **Vendors in [COMPANY]'s space: cite their RESEARCH, not their product.** Original-research arms of vendors (workforce reports, research institutes, hiring labs, etc.) are fine as sources. Do NOT link a vendor's product/marketing page or position a competing product favorably. If a vendor competes directly with [COMPANY], treat it like a competitor and exclude it (per `workflows/standards/content-policy.md`). Prefer a neutral Tier-1 primary when one exists.
3. **External citations follow the outbound-`rel` policy** owned by `workflows/standards/content-policy.md`. The density rules below do not change the `rel` policy — more citations, same `rel`.
4. **Every stat still passes `workflows/standards/claims-integrity.md`:** exact figure + nameable source + live-URL check + figure actually present in the source + correct year, or it is dropped. Authority tier does not excuse verification.

## Core principles

- Use an external link only when it adds credibility, supports a claim, is original research, or genuinely helps the reader learn more.
- Anchor text: natural, concise, contextually relevant, **2-6 words**. Never "click here", "learn more", "read this article". Exact-match anchors <30%.
- Avoid over-linking. Quality over quantity. Never multiple links in one sentence; don't link every paragraph.
- Prefer **primary sources over secondary commentary**. Cite the **original research**, not a publication that references it.
- Never cite a statistic, trend, benchmark, forecast, or research finding without a source.

## Source authority hierarchy (prioritize top-down)

**Tier 1 - Primary (highest trust):** official company docs, government agencies, regulatory bodies, academic journals, original research reports, industry analyst reports. Examples: relevant government statistics agencies, standards/regulatory bodies for [COMPANY]'s field, and analyst houses (e.g. Gartner, Forrester, IDC, McKinsey, Deloitte Insights, PwC, EY, KPMG, BCG).

**Tier 2 - Niche vendor & domain authorities (use for facts inside [COMPANY]'s field):** the original-research arms of established vendors and platforms in [COMPANY]'s space. Cite their research/reports, not product pages — see reconciliation #2. *Illustrative example only:* in HR/talent-tech this tier holds sources like LinkedIn Workforce Reports and Indeed Hiring Lab. [COMPANY]'s actual Tier-2 list is niche-specific — see the note below.

**Tier 3 - Niche industry publications:** the trade press and practitioner publications that cover [COMPANY]'s field. *Illustrative example only:* in HR/talent-tech this tier holds outlets like HR Dive and People Matters. [COMPANY]'s actual Tier-3 list is niche-specific — see the note below.

> **Tier 2 and Tier 3 are niche-specific.** [COMPANY]'s authoritative sources for these tiers live in `projects/[company]/brand-brain/` — extend it with the primary sources, analysts, and publications that own facts in [COMPANY]'s field, aimed at [AUDIENCE]. Do not treat any one example list as canonical.

**Tier 4 - Academic & research:** Google Scholar, ResearchGate, SSRN, JSTOR, Nature, Springer, Wiley, ScienceDirect, PubMed, and university research centers (Harvard, MIT, Stanford, etc.).

**Tier 5 - Reputable business & news (commentary / market context only, NOT primary evidence):** Reuters, Bloomberg, Financial Times, The Economist, WSJ, BBC, CNBC, Fortune, Forbes, NYT, Fast Company, Business Insider.

## Source selection: match the source to the claim (do NOT default to two sources)

**Pick the most SPECIFIC and most RECENT primary for each individual claim.** Do NOT reflexively reach for the same one or two familiar names — over-relying on a couple of sources is a known, flagged failure. Actively research across the tiers and pick the source that genuinely owns that fact.

For each claim type in [COMPANY]'s field, define the go-to primaries in `projects/[company]/brand-brain/` (claim-type → best-fit, most-recent source). As a universal anchor:

| Claim type | Go-to primaries (pick the best-fit, most recent) |
|---|---|
| Labor market / official economic & demographic stats | National statistics agencies (e.g. U.S. BLS, UK ONS, Eurostat), OECD |
| Cross-industry technology & market shifts | Gartner, Forrester, IDC, McKinsey, WEF |
| Academic / scientific findings, validity, methodology | Peer-reviewed journals, meta-analyses, Tier-4 academic sources |
| Niche-specific facts in [COMPANY]'s field | The claim-type → source map in `projects/[company]/brand-brain/` |

Use any single familiar source ONLY where it is genuinely the best primary for that specific claim — never as the lazy default, never more than twice, and never as one of only two domains in a post. A post leaning on just two domains fails the diversity bar.

## Source freshness

| Topic | Prefer published within |
|---|---|
| Fast-moving tech / [COMPANY]'s core field | 12 months |
| Market & trend data | 12 months |
| Slower-moving operational / planning data | 24 months |
| Frameworks & evergreen concepts | up to 5 years if still relevant (evergreen ok) |
| Any statistic/research | the most recent available version, always |

## External linking density

- ~1 external authority citation every **150-250 words**; **3-8** authority links for a 2,000-word article, across **>=3 distinct domains** (a 2,000-word post should not lean on just 1-2 sources).
- Link directly to the original report whenever possible.
- **Avoid:** multiple links per sentence, a link in every paragraph, excessive vendor citations, low-authority blogs, AI-generated/anonymous sources, forums as evidence.

## E-E-A-T this enforces

- **Experience:** practical, first-hand insight from [COMPANY]'s field (first-hand markers).
- **Expertise:** named industry best practices + subject-matter depth.
- **Authoritativeness:** claims backed by recognized, correctly-tiered sources.
- **Trustworthiness:** verifiable stats, transparent attribution, credible citations (all live-URL checked, correct year).

## Quality bar

Content must be more useful than the ranking competitors, more authoritative than generic AI output, more trustworthy than SEO-first filler — backed by credible research + real-world expertise, optimized for engines AND humans, worth bookmarking and citing.

## Citation diversity + no brand promotion

- **Cite, do not promote.** Link a source as evidence for a stat only — neutral, following the outbound-`rel` policy. NEVER recommend or send readers to another brand's guide/tool/template/report ("X has a great guide", "pairs well with X's resource", "check out X's toolkit"). The reader stays on our page; the link backs a number, nothing more.
- **Max 2 citations per external domain per post.** Do not cite any one domain 3+ times. Aim for 3+ distinct primary domains across the post. If a third stat would come from an already-used domain, find a different primary (a government/statistics body, a major analyst, an academic source, or another Tier-1 primary) or drop it.
