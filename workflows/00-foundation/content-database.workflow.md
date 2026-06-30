---
type: workflow-recipe
stage: foundation
reusable: any company
inputs: [WEBSITE domain]
last_updated: 2026-06-22
---

# Recipe — Content Database (catalogue every page a site has)

## What this does
Build a catalogue of every page the site has, so we always know what already exists - so we don't
duplicate a page that's already there, we spot pages worth improving, and we can pick good internal links.

## What you get (the output)
**Two files in `projects/[company]/`:**
- **`content-database.csv`** - one row per page: `URL · Type · Title · Description · Full content · Traffic · Keywords · Intent`.
- **`content-database.md`** - a short summary (page counts per type + how to use the CSV).

**`Full content`** is the page's entire clean text, stored **inline in the CSV, with no word limit** - it's
what the asset-engine **reuse check** runs RAG against to find pages we already have
(see `01-asset-engine/reuse-check.md`). Store the whole page, never a truncated slice.

*(For scale: a large site can run to 10,000+ rows; with full content inline the CSV can reach many MB - that's
expected and fine, the reuse check needs the full text.)*

## When to run it
Once per company. It's the **first** foundation step. Refresh occasionally.

## Inputs you need
- `[WEBSITE]` - the company's domain. **That's all.**

The **Traffic / Keywords / Intent** columns start **empty** here - they're filled in the **next step
(Semrush)**. This step does not touch Semrush.

## Choose the method
- **Method A - WordPress site (best).** Most sites run WordPress, which has a built-in **REST API** that
  returns every page's title + summary in bulk - so you get the full URL list and the descriptions in one go.
  (You do NOT need the sitemap for WordPress sites.)
- **Method B - non-WordPress site (fallback).** Use the site's XML **sitemap** to list the URLs, then
  fetch each page's title + meta description.

## Steps - Method A (WordPress)
1. **Check the API is on:** open `https://[WEBSITE]/wp-json/` in a browser - it should return data, not an error.
2. **List the content types:** `GET /wp-json/wp/v2/types`; note each type's `rest_base` (posts, pages, and
   custom types like products or glossaries). Skip technical types (media, blocks, templates) and, unless asked, translated duplicates.
3. **Pull each type in bulk** (100 per request): `GET /wp-json/wp/v2/{rest_base}?per_page=100&page=N&_fields=link,title,excerpt,content`.
   This assembles the table - URL, Type, Title, Description. Also pull **`content`** (the page's full body):
   strip its HTML to clean text and store it **whole, no truncation,** in the **`Full content`** column.
   -> `scripts/content-database/build_content_database.py` does steps 2-3 (it must keep `content.rendered`).
3b. **Live-HTML fallback for empty bodies (REQUIRED — do not skip).** WP REST `content` comes back **empty for
   page-builder / custom-template post types** (e.g. `test-library`, `interviews`, `competitors`,
   `integrations`) because their visible body isn't in the standard content field — it's rendered from builder
   meta at display time. Relying on REST alone silently drops their `Full content` (the 2026-06 gap: ~2,700
   pages, 27% of the site, invisible to RAG). So for **every content-bearing row that came back empty**, fetch
   the **live page HTML** and extract the visible text into `Full content`; keep it only if it's a real body
   (≥ ~400 chars — below that it's a genuine stub, leave empty). `build_content_database.py` does this
   automatically (parallel, ~minutes) for the types in its `FALLBACK_TYPES`.
4. **Fill blank descriptions** (custom types often have none): `scripts/content-database/enrich_descriptions.py` (from page
   content), then for template-driven pages `scripts/content-database/enrich_meta_descriptions.py` (from the page's meta tags).
5. **Save** `projects/[company]/content-database.csv` + `content-database.md`. At this point the
   **Traffic / Keywords / Intent** columns are still empty.
6. **Traffic is joined in the next step (Semrush).** Once Step 2 produces `semrush-top-pages.csv`, it's
   matched to the catalogue by URL to fill the Traffic / Keywords / Intent columns.
   *(`build_content_database.py` does this join automatically when it's given the Semrush CSV.)*

## Steps - Method B (non-WordPress)
1. Fetch `https://[WEBSITE]/sitemap_index.xml` (or `/sitemap.xml`; or read `/robots.txt` for its location).
2. It lists child sitemaps by type - pull each and collect every `<loc>` URL.
3. For each URL, fetch the page and read its `<title>` + `<meta name="description">`, and capture the **full
   visible body text** (whole, no truncation) into the `Full content` column.
4. Save the same two files. (Traffic is joined later by the Semrush step, same as Method A.)

## Coverage gate (check before using the DB downstream)
After the build, confirm **what share of rows actually have `Full content`** — `build_content_database.py`
prints `COVERAGE: X/N (pct%)` plus the still-empty count by type. If coverage is **below ~90%**, a content
type is being missed (almost always a page-builder type the REST API can't see) — fix it with the 3b fallback
*before* this DB feeds the reuse-check RAG. A silent coverage hole reads downstream as "we don't have a page on
that," when we do. (This gate exists because the 2026-06 run shipped at 73% and the gap was only caught when a
reviewer noticed RAG missing obvious pages.)

## Gotchas (and when each applies)
- **Every web request (both methods):** send a **browser User-Agent** - sites behind Cloudflare block plain bots.
- **Page-builder bodies (Method A):** never trust WP REST `content` alone — run the **3b live-HTML fallback**, or whole custom post types land with empty `Full content` and vanish from RAG.
- **The bulk pulls / fetches (both methods):** a single fetch can come back **truncated** - re-run if a count looks suspiciously short.
- **The meta-description pass (Method A, step 4):** it's slow and best run in the background, so **keep the
  laptop awake** - sleeping suspends the job.
- **Always:** **don't classify pages here** (reuse / improve / leave). That needs page context and happens
  later, at build time - not in this catalogue.
