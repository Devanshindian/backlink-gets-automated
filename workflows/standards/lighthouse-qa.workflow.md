---
type: standard / workflow-recipe
applies_to: every page after publishing or editing
reusable: any company
last_updated: 2026-06-22
---

# Lighthouse QA Standard

After a page is published or edited, **verify it with Lighthouse, fix until the scores are ideal, recheck.**
This is the "technical SEO" gate — on a stack with an SEO plugin (e.g. WordPress + RankMath), the sitemap,
robots, schema, canonical and OG already ship; Lighthouse confirms it all actually works and catches
performance / layout-shift (CLS) / accessibility issues.

## How (free, no auth needed)
Use Google's **PageSpeed Insights API**, which runs Lighthouse server-side and returns JSON:

```bash
URL="https://[website]/your-page/"
curl -s "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=$URL&strategy=mobile&category=performance&category=seo&category=accessibility&category=best-practices" \
  | python3 -c "import sys,json; d=json.load(sys.stdin)['lighthouseResult']['categories']; [print(f\"{k:14} {round(v['score']*100)}\") for k,v in d.items()]"
```

Run it for **both** `strategy=mobile` and `strategy=desktop` (mobile is what Google indexes on).

> **Setup needed — free API key.** The **keyless** quota is tiny and exhausts fast (we hit a `429
> Quota exceeded` in testing). Create a **free PageSpeed Insights API key** (Google Cloud → enable
> "PageSpeed Insights API" → create an API key — **no billing required**, ~25,000 queries/day) and
> append `&key=YOUR_KEY` to the URL. Store it in the project's local access file (outside the repo).
> Alternative: run Lighthouse locally via the `lighthouse` npm CLI (needs Node + Chrome) — heavier, but no quota.

## Target scores (ideal)
| Category | Target |
|---|---|
| SEO | **100** |
| Best Practices | **100** (≥95 acceptable) |
| Accessibility | **≥95** |
| Performance (mobile) | **≥90** |

## The loop
1. Publish/edit the page.
2. Run PageSpeed Insights (mobile + desktop); read the four scores.
3. If any are below target, read the **failing audits** (the JSON `audits` → "opportunities" and
   "diagnostics"): common fixes = compress/resize images (WebP), set width/height (CLS), lazy-load,
   reduce render-blocking CSS/fonts, fix contrast / alt text / link names (a11y), fix meta/schema (SEO).
4. Apply fixes (most are image/font/CLS — see image-sourcing.workflow.md).
5. **Re-run until all targets are met.** Don't call a page "done" until Lighthouse passes.

## Notes
- PageSpeed reflects the **live** page, so run it *after* publishing (or on a staging URL if available).
- Pair with the on-page-seo.md checklist — Lighthouse catches the technical/perf items; the checklist
  covers the content/E-E-A-T items Lighthouse can't see.
