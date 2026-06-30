---
slug: content-resurrection
type: strategy
title: "Content Resurrection (replace dead pages that still have backlinks)"
category: outreach
aliases: ["broken link building", "expired domain content", "dead link replacement"]
difficulty: medium
cost: medium
risk: low
white_hat: true
tools: [spamzilla, semrush, ahrefs]
sources: [0002, 0006]
automatable: partial
last_updated: 2026-06-19
---

## 1. What it is
Finding old or expired websites whose pages are dead (404 errors) but still have other sites
linking to them — and then creating a **better, updated version** of that dead content and reaching
out to ask those linking sites to swap the dead link for yours.

In plain terms: imagine 20 websites still point to a door that no longer exists. You build a new
door in the same spot and ask each of those 20 sites to update their signpost. Everyone benefits —
they fix a broken link; you get a backlink.

This is distinct from simple broken link building because it starts with *expired domain prospecting*
(using SpamZilla) to find niche-relevant dead pages with quality backlinks, rather than hunting
random broken links on live sites.

> **Note:** the same Semrush **Indexed Pages → Broken Pages** flow used below also works on *live*
> competitor sites — that generic broken-link case lives in
> [[strategies/resource-page-link-building]] (variant 4). This file is the *expired-domain* version.

## 2. Why it works
- The backlinks already exist — the hardest part of link building is done. You're not asking someone
  to create something new; you're asking them to fix something broken (a much lower-friction ask).
- Replacing a dead resource with a better one is a genuine win for the linker (they help their
  readers) and for you (you earn the link).

## 3. When to use / prerequisites
- You have access to SpamZilla (or a similar expired-domain tool) and Semrush/Ahrefs.
- You can identify or create an asset that genuinely replaces the dead content.
- Best suited to informational niches with decent expired-domain activity.

## 4. End-to-end process

1. **Find relevant expired domains in SpamZilla**

   In SpamZilla, filter the expired-domain list by **Majestic Topical Trust Flow** topic category
   (e.g. "Home & Garden" for plumbing, "Computers / Internet" for SaaS). This limits results to
   domains that were topically relevant before expiring.

   SpamZilla's result table shows these columns:
   `Domain | Source (🔗 icon = link type) | TF (Trust Flow) | CF (Citation Flow) | Maj BL (Majestic backlinks) | Maj RD (Majestic referring domains) | Maj Topics (color-coded topic numbers) | Maj Lang | Site Lang | Ahrefs DR`

   Sort by **TF** (Trust Flow) descending to surface the highest-quality expired domains first.
   _tool(s): spamzilla_

2. **Evaluate the domain's backlink quality in Semrush**

   Enter the expired domain into Semrush's search bar → **Backlink Analytics**.

   In the **Backlinks** tab you'll see a summary panel:
   - **Backlinks** total count
   - **Referring Domains** count
   - **Referring IPs** count
   - **Backlink Types** breakdown (Text / Image / Form / Frame — mostly Text is healthy)
   - **Link Attributes** breakdown (Follow % / Nofollow % / Sponsored % / UGC %)

   Switch to **Indexed Pages** (the tab in the same row) and look at which pages have the most
   referring domains. Click through to the individual page's backlink list to evaluate further.

   A *good* backlink profile has:
   - Links from relevant sources or well-known trusted entities.
   - No signs of artificial link building (no web 2.0s, spammy directories, etc.).
   - Most links hitting **content pages**, not the homepage.
   - Anchor text that is **under-optimized** (mostly branded or natural phrasing, not money keywords).
   _tool(s): semrush_

3. **Identify the specific dead pages worth targeting**

   Once the domain's overall profile passes the quality check:

   - Semrush → Indexed Pages → click the **Backlinks count** number for one of the top indexed
     pages. This opens the detailed backlink list for that specific page.

   Apply these three filters in the filter bar:
   - **Active** — shows only links that still exist on the referring page right now (not lost/removed
     ones). This confirms the editor hasn't cleaned up the link yet — so your outreach has a live
     target.
   - **Follow** — shows only dofollow links. These pass ranking value, so they're worth pursuing.
     Nofollow links on a dead page aren't worth the effort.
   - **Placement: Content** — click the "Ref. page platform" dropdown or use the filter row and add
     `Placement: Content ×`. Filters to links inside the editorial body of an article, not sidebars,
     footers, or comment sections.

   **Why these three together isolate your best prospects:**
   These filters don't directly surface broken pages — they surface the *linkers worth contacting*.
   The dead page's URL (the Target URL column) is already the broken destination. What you need to
   know is: which referring pages still have that broken link live, in an editorial context, passing
   SEO value? That's exactly what Active + Follow + Content answers. Every row in the result is one
   outreach target: a real editor whose article still links to a dead page you can replace.

   The combined filter strip looks like:
   `All | Active | New | Lost | 📅 | All | Follow | Nofollow | Sponsored | UGC | Links per ref. domain: All/1/3/10 | Placement: Content ×`

   The results show: `Page AS | Source page Title and URL | Ext. Links | Int. Links | Anchor and Target URL | First Seen | Last Seen`
   _tool(s): semrush_

   > **Note:** Verifying which target URLs are actually returning 404s must be done manually after
   > exporting this list. [TODO: document this step]

   > **Scale-up: don't stop at one page — do this for every broken page on the domain.**
   > Go back to Indexed Pages and repeat this filter process for *every* page with a meaningful
   > referring-domain count (not just the top one). Each page is a separate dead URL that other
   > sites still link to — each one is its own set of outreach prospects. One expired domain can
   > yield 5–20 separate broken pages, each with its own pool of linkers. Covering all of them
   > multiplies your prospect list without finding a new domain.

4. **Export and add to the link-building dashboard**

   Click **Export** (top right of the backlinks table) → export as CSV.

   Add to the Link Building Dashboard with these columns:
   `Status | Link Type (= "Broken Link") | If Other | Source (= the dead page URL) | Opportunity URL (= the live site still linking to the dead page) | Relevance | Target URL (= your replacement asset — mark [NEEDS CONTENT] if not built yet)`

   Mark Status as "Prospect".

5. **Identify or create a replacement asset**
   - Search your existing content inventory for a high-quality, closely matching page.
   - If none exists, **create one** before doing outreach (pitching a live replacement is far more
     convincing than pitching a page you "plan to write").

6. **Send outreach emails** (broken-link template)

---

**Outreach email template:**

> **Subject:** Broken link
>
> Hey [NAME],
>
> My name is [NAME] and I'm the [POSITION] at [COMPANY or BLOG].
>
> I found your article and noticed that you're linking to a dead resource.
>
> We actually just published something similar: [TITLE] and were wondering if you'd like to
> replace that dead link with our new resource?
>
> I'm confident it will add value for your readers.
>
> Please let me know your terms and we're open to negotiation.
>
> Thank you!
> [NAME]

---

## 5. Tools
- [[tools/tools#spamzilla]] — expired-domain discovery filtered by Majestic Topical Trust Flow.
- [[tools/tools#semrush]] — quality-check the expired domain's backlink profile; find specific dead pages with quality links.
- [[tools/tools#ahrefs]] — alternative for backlink profile analysis.

## 6. Success metrics
- Number of quality expired domains with usable backlink profiles found.
- Number of prospect URLs added (sites linking to dead pages you can target).
- Outreach reply rate and link conversion rate.
- Referring domains earned per campaign.

## 7. Risks & pitfalls
- **Pitching before the replacement asset is live** — always have the asset ready first; "we're about to publish X" is a weak pitch.
- **Skipping the backlink quality check** — not every expired domain is worth pursuing. A domain full of web 2.0s or spammy directories should be skipped even if it has backlinks.
- **Matching at the wrong level of depth** — the replacement needs to be a genuine *better* version of the dead content, not a vaguely similar page from a different angle.

## 8. Conflicting views
- None recorded yet.

## 9. Automation hooks
- Step 1: SpamZilla can be filtered by Trust Flow and exported in bulk (partial — manual review still needed).
- Step 2–3: Semrush API can pull backlink quality data and filter for Active + Follow + Content placement (high — core automation candidate).
- Step 6: outreach email can be templatized and batch-sent via email sequence tool once prospects are validated (partial).
- Full pipeline: SpamZilla export → Semrush API quality filter → dashboard population → personalized outreach generation (high automation potential).

## 10. Sources
- [[sources/0005-seo-marketing-database]] — **"Templates - Search Strings"** tab ("Find Outdated Content" operators to surface dead/stale pages).
- [[sources/0002-gotch-seo-academy-link-building-sop]] (Nathan Gotch) — full step-by-step process including SpamZilla, backlink quality checklist, Semrush filters, and broken-link outreach template.
- [[sources/0006-semrush-backlink-tutorial]] (Semrush) — corroborates the Indexed Pages → Broken Pages flow (also applicable to live sites) and the Active/Follow/Content lens on the linkers worth contacting.
