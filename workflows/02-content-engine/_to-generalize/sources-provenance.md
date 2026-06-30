# Sources & provenance (rubric claims)

The SEO/AEO/GEO standards in this repo are not opinion - each load-bearing claim traces to a primary source below. This file exists so the standards stay auditable and so adjacent work (e.g. the backlinking repo) can subscribe to the same signals. Article *statistics* are sourced per-claim at write time via `references/claims-integrity.md`; THIS file sources the *rubric's own* claims.

All URLs curl-verified 200 on 2026-06-28 (re-check on edit).

## Claim -> primary source

| Rubric claim (where it appears) | Primary source | URL |
|---|---|---|
| GEO: inline stats + quotes + outbound citations each lift AI-citation likelihood ~30-40% (seo-aeo "6 levers" #1; SKILL Step 3 #1) | Aggarwal et al., "GEO: Generative Engine Optimization" (Princeton/Allen AI, KDD 2024), arXiv 2311.09735 | https://arxiv.org/abs/2311.09735 |
| Scaled content abuse is a spam violation; mass low-value pages get deindexed ("no matter how it's created") (POLICIES #1; SKILL "one rule") | Google Search Central - March 2024 core update + new spam policies | https://developers.google.com/search/blog/2024/03/core-update-spam-policies |
| Definition of scaled-content abuse / site-reputation abuse used in triage + guardrails | Google Search Essentials - Spam policies | https://developers.google.com/search/docs/essentials/spam-policies |
| Helpful-Content / people-first signals; first-hand experience; single-topic focus (seo-aeo "2026 ranking bar"; HCU references) | Google Search Central - Helpful Content update (Aug 2022; later folded into core) | https://developers.google.com/search/blog/2022/08/helpful-content-update |
| FAQ + HowTo rich results dead for general sites since 2023 (do not invest) (schema-types.md; seo-aeo CORRECTION; SKILL Step 4) | Google Search Central - "Changes to HowTo and FAQ rich results" (Aug 2023) | https://developers.google.com/search/blog/2023/08/howto-faq-changes |
| INP replaced FID as a Core Web Vital (March 2024) (seo-aeo Core Web Vitals) | web.dev - "INP is a Core Web Vital" | https://web.dev/blog/inp-cwv-launch |

## Not first-party (used in article bodies, not the rubric)

These appear as example evidence in posts and are sourced per-use via claims-integrity; listed here so they aren't mistaken for rubric provenance: Schmidt & Hunter selection-method validity meta-analysis; Gallup engagement/Q12; SHRM cost-per-hire/benefits; LinkedIn Talent; McKinsey; HBR. See `references/source-authority.md` for the approved primary-source tiers.

## Keeping this current (for the backlinking repo / signal subscription)

Monitor these for new ranking/GEO practices, then update the rubric + this table together:

- **Google Search Central blog** (algorithm, spam, structured-data changes): https://developers.google.com/search/blog
- **Google Search status dashboard** (ranking/indexing incidents + update rollouts): https://status.search.google.com/
- **arXiv cs.IR + cs.CL "generative engine optimization" / "LLM citation"** (the GEO research frontier): https://arxiv.org/list/cs.IR/recent
- **web.dev** (Core Web Vitals changes): https://web.dev/blog
- Secondary corroboration (never a primary cite, never a competitor): Search Engine Land, Search Engine Roundtable for early signal on confirmed Google updates.

Rule: a new "practice" only enters the rubric once it traces to a primary source in the first three bullets. Secondary blogs flag it; they don't justify it.
