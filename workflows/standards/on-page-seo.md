---
type: standard
reusable: any company
applies_to: every page we generate or edit (blogs, assets, money pages)
read_before: building any asset/page (the Asset Engine's build step chains this in)
last_updated: 2026-06-22
---

# On-Page SEO Standard — do these on every page

The complete on-page spec. **Every applicable item must be satisfied before a page ships.**

## How to read this (AUTO vs MANUAL)
Most modern stacks (e.g. **WordPress + an SEO plugin like RankMath/Yoast**, or a Next.js setup with an SEO
config) **auto-handle** the *technical* items. So each item is tagged:
- **[AUTO]** — the CMS / SEO plugin / theme does it. We **verify** it (the plugin's score + Lighthouse); we
  don't hand-build it.
- **[MANUAL]** — **we** write or set it. This is where the work goes. **On a stack with no SEO plugin, the
  [AUTO] items become [MANUAL].**

> Brand-specific values (demo/CTA link, brand colour, fonts) come from the company's
> `brand-brain/brand-assets.md`. Technical/perf verification is in `lighthouse-qa.workflow.md`.

---

## 1. Head & metadata — what Google indexes first
- **[MANUAL] Title tag** — 50-60 chars, primary keyword near the start.
- **[MANUAL] Meta description** — 150-160 chars, keyword + benefit + soft CTA.
- **[AUTO] Canonical URL** — verify no duplicate/wrong canonical.
- **[AUTO] Open Graph** (og:title/description/image 1200×630/url/type) — verify the OG image.
- **[AUTO] Twitter Card** (summary_large_image).
- **[AUTO] Language / Viewport / Charset / Favicon + apple-touch-icon.**

## 2. URL structure — clean, readable, keyword-forward
- **[MANUAL] Short slug** — under 60 chars, **primary keyword in the slug**, hyphens (never underscores),
  lowercase, no stop words ("the/a/of") unless necessary. Logical hierarchy (`/blog/[slug]`, `/[asset]/[slug]`).

## 3. Headings — structure for skimmers & bots
- **[MANUAL] Exactly one H1** containing the primary keyword.
- **[MANUAL] Logical H2 → H3** (never skip levels). H2s use supporting keywords + **questions from the keyword cluster**.
- **[MANUAL] No keyword stuffing** — write naturally (see the brand brain's anti-AI rules).

## 4. Copy & body — answer the query, fast
- **[MANUAL] Primary keyword in the first 100 words.**
- **[MANUAL] Direct answer to the query in the first paragraph** (answer-first).
- **[MANUAL] Length matches the SERP top-3 for the target keyword (within 20%)** — check the top-3 ranking
  pages' word counts first; don't pad or starve. **Don't just clone a competitor's topic/format** — match
  the *intent and depth*, then add a unique angle (data, a tool, a real opinion).
- **[MANUAL]** Short paragraphs (1-4 sentences) · readability 8th-10th grade · active voice · bold key
  phrases sparingly · bullets/numbered lists where useful.

## 5. FAQ section — every long-form / blog post
- **[MANUAL] 4-8 questions** from Semrush "Questions" + Google "People Also Ask", with **direct 2-4
  sentence answers**.
- **[MANUAL/AUTO] FAQ schema (JSON-LD / FAQPage)** — build the FAQ with a block your CMS turns into valid
  FAQPage schema (e.g. a WordPress accordion block with FAQ schema enabled, or hand-rolled JSON-LD on a
  custom stack). Verify in Google's Rich Results Test.

## 6. Images — every image is a ranking signal
- **[MANUAL] Alt text** describing the image + keyword where natural.
- **[MANUAL] Descriptive filenames** (hyphens, e.g. `skills-based-hiring-funnel.webp`).
- **[MANUAL] WebP, compressed (aim <200 KB)** · width/height attributes (prevents layout shift / CLS) ·
  lazy-load below the fold · responsive `srcset` where needed · a featured/hero image for social sharing.
- Where images come from → `image-sourcing.workflow.md` (design originals + stock fillers).

## 7. Internal links — pass authority across the site
- **[MANUAL] 3-5 internal links** per post, to **related posts + relevant money pages**. Use the
  **content database** (`projects/[company]/content-database.csv`) to find the best related pages.
- **[MANUAL] Descriptive anchor text** (never "click here"/"read more"), contextually placed in the body.
- **[AUTO] Breadcrumbs** — verify present.

## 8. External links — cite authority, don't hoard it
- **[MANUAL] 2-3 external links** to authoritative sources (.gov, .edu, major industry bodies), relevant to
  the topic, opening in a new tab with `rel="noopener"`. Use `rel="nofollow"`/`"sponsored"` for paid links.

## 9. Schema markup — JSON-LD
- **[AUTO via SEO plugin]** Article (blogs), FAQPage (where the FAQ block is used), BreadcrumbList,
  Organization (site-wide), Author/Person (bylines). For money/product pages, set the appropriate schema.
  **We verify** each renders (Rich Results Test); we don't hand-code it (unless the stack has no plugin).

## 10. E-E-A-T — Experience · Expertise · Authority · Trust
- **[MANUAL] Author byline with name** on every blog post; **author bio with real credentials**; link to a
  **dedicated author page**. (If author infrastructure is missing, flag it to the site owner.)
- **[MANUAL] Published date** shown; **"Last updated" date** when refreshed.
- **[MANUAL] Real stories / numbers / opinions** — from `stats.md` / `stories.md` / `opinions.md` (never improvise).
- **[MANUAL] Cite authoritative sources** (ties to §8). About + Contact pages exist site-wide.

## 11. Accessibility — a11y signals = SEO signals
- **[AUTO] Semantic HTML5 / responsive layout** (theme). **[MANUAL]** alt text, descriptive link text,
  sufficient colour contrast (WCAG AA — check the brand colour from `brand-assets.md` against its
  background, especially small text), focus indicators, skip-to-content. Verify in Lighthouse Accessibility.

## 12. Mobile & responsive — mobile-first indexing
- **[AUTO via theme]** responsive layout, touch targets ≥48×48, body font ≥16px, no horizontal scroll.
  **[MANUAL]** no intrusive interstitials/popups that block content. Verify in Lighthouse (mobile).

## 13. Social preview — shareable card
- **[MANUAL] OG image** 1200×630, under 1 MB · Twitter card image 1200×600 · compelling `og:description`
  (different from the meta description if it adds value).

## 14. Conversion elements (money / product / landing pages)
- **[MANUAL]** Primary CTA above the fold (the demo/trial link from `brand-assets.md`). Trust signals (real
  ratings/reviews from `stats.md`), testimonials with names, multiple CTA placements. **Get owner sign-off
  on revenue-surface pages before publishing.**

## 15. Long-form (1500+ words)
- **[MANUAL] Table of contents** with anchor links at the top · **jump links for each H2** · back-to-top button.

---

## Required for EVERY long-form post (the non-negotiables)
1. FAQ section with FAQPage schema.
2. Breadcrumbs + BreadcrumbList schema.
3. Author byline + Person schema.
4. Table of contents with anchor links.
5. 3-5 internal links + 2-3 external links to authoritative sources.
6. Open Graph + Twitter Card meta.
7. **Length within 20% of the SERP top-3** for the target keyword.

## The SEO content brief (fill before writing)
Use the **SEO content-brief template in `research/strategies/guest-posting.md`** (STRATEGY → SEO → WRITING
GUIDELINES → OUTLINE → LINKS → DESIGN). It captures primary keyword, volume, KD, SERP features, title
options, meta, word-count target, NLP keywords, audience/tone, outline, and the links table.

## Hard rules (carry the brand brain's into every build)
- The CTA/demo link is **only** the exact URL in `brand-assets.md` (verify it's not a 404).
- Apply the brand brain's mechanics: **no em dashes, no exclamation marks, no AI-slop words.**
- **Verify every link returns HTTP 200 before publishing.**
- When editing a live CMS post, **preserve existing image blocks** — fetch and re-insert them, or you'll
  destroy the live images.
