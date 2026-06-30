# Staged Testlify scripts + docs — PENDING GENERALIZATION

These were pulled out of the Testlify project (which is being retired) so they survive and can be reviewed.
**They are still Testlify-specific and platform-specific (WordPress/RankMath/Kadence/Semrush).** Do NOT treat
them as generalized standards yet — they are raw source to generalize later, then wire into the recipe steps.

Each file maps to a step in `../02-content-engine.workflow.md`:

| File | Backs step | What it does | Status |
|---|---|---|---|
| `serp_study.py` | Step 1 (Study the SERP) | **Scaffolder, not a scraper.** Writes the JSON skeleton a SERP brief needs; the REAL data comes from the **Semrush MCP** (keyword_overview, related_keywords, keyword_questions) + a SERP API/browser for top-20, snippet owner, AI Overview, PAA. Won't fabricate fields. | to generalize |
| `faq_accordion.py` + `faq-accordion.md` | Step 5 (on-page) | Generates the FAQ block. WP/Kadence-specific markup — the *idea* (FAQ accordion for UX) generalizes; the markup doesn't. | to generalize |
| `verify_post.py` | Step 7 (score + gate) | The big quality/verify gate (639 lines) — element-parity rubric, link-rel, banned-words, render checks. WP-coupled. | to generalize |
| `outbound_link_audit.py` | Step 4/5 (citations) | Audits outbound links/citations against the source + rel rules. | to generalize |
| `wp_client.py` + `wp-operations.md` | Step 8 (deploy) | The WordPress deploy client + ops doc. This is the `[PLATFORM]` layer — fully platform-specific. | to generalize |
| `schema-types.md` | Step 5 (schema) | Which schema types are worth it (Article/Breadcrumb) vs dead (FAQPage/HowTo/Speakable). Mostly general knowledge. | to generalize |
| `sources-provenance.md` | the bar (proof trail) | The "says who?" evidence behind each ranking rule. The optional companion to `seo-aeo-geo-bar.md`. | to generalize |

## NOT pulled (deliberately, out of content-build scope)
- `build_triage.py`, `inventory_triage.py` — the site-wide refresh-triage you cut from Step 0.
- `gsc_submit.py` — GSC re-indexing; off the per-post content path.

## Format-coverage gaps (from the Step 1 audit) — where each lives
- **tool / calculator / glossary** formats → already covered in this machine by the **asset engine**
  (`research/strategies/link-bait-asset-types.md` + `01-asset-engine.workflow.md` D3). Nothing to pull.
- **"definition" page** format → no dedicated source exists (in Testlify or here). A genuine small gap if we
  want it; would be a new short standard, not a pull.
- **intent → post-type mapping** → no source file anywhere; assumed knowledge. Genuine gap to write later.
