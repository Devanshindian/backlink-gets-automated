---
slug: merger-technique
type: strategy
title: "The Merger Technique 2.0 (acquire a site/tool and 301-redirect it into yours)"
category: technical
aliases: ["merger technique", "site acquisition link building", "301 redirect acquisition"]
difficulty: high
cost: high
risk: medium
white_hat: true
tools: [semrush, ahrefs, archive-org]
sources: [0002]
automatable: partial
last_updated: 2026-06-18
---

<!-- WRITING STYLE: assume the reader is new to SEO. Explain every term in plain English on first use. -->

## 1. What it is
Acquiring another website, tool, or asset and **merging it into yours** with **301 redirects** — a 301
is a permanent "this page moved here" instruction that passes most of the old page's link value to the
new destination. You buy the asset for its backlinks, then redirect each of its pages to a relevant
page on your site.

In plain terms: instead of earning links one by one, you buy a site that *already has* links and point
them all at yours. Think of it as acquiring a competitor and inheriting their reputation.

> **WARNING (from the source):** Do **not** use *expired domains* for this anymore. It may still work
> despite Google's warnings, but the risk is too high. The "2.0" version only merges *live, real* sites
> or tools you genuinely acquire.

## 2. Why it works
- A 301 from a relevant, authoritative page passes its accumulated link equity to your page.
- You're acquiring proven, editorial links at once rather than building them slowly.
- Done with real assets and relevant redirects, it mirrors normal business M&A (mergers/acquisitions),
  which Google tolerates.

## 3. When to use / prerequisites
- You have real budget (this costs money — you're buying assets) and the patience to vet carefully.
- You can create or already have relevant destination pages for the redirects.
- **Not** for expired domains (see warning). This is an advanced, high-effort play.

## 4. End-to-end process

### Find opportunities
- Search `best free [NICHE] {calculators | tools | software}` to find curated lists of single-use-case
  tools (these are acquirable assets with link profiles).
- Repeat with `best [NICHE] blogs` to find **inactive** blogs with high-quality link profiles.
- Build a list of **at least 100** potential acquisition targets. (Real examples: WebFX acquired
  colorpicker.com, wikigrabber.com, faqfox.com etc. and 301'd them; Neil Patel acquired ubersuggest.org.)

### Vet opportunities (treat it like buying a real business)
1. **Relevance + editorial link profile.** You want mostly editorial links. A profile full of directory
   links is bad; links from outlets like the New York Times are great. In Ahrefs, filter to **Dofollow**
   and sort by **DR (Domain Rating)** to see its best links.
2. **Anchor text profile.** It should be **under-optimized** — a healthy blend of branded and generic
   anchors, *not* full of exact-match commercial keywords or foreign-language anchors (those signal past
   manipulation). Avoid over-optimized domains.
3. **Review its history.** Use **Archive.org** (the Wayback Machine — shows old snapshots of a site) to
   confirm the domain wasn't previously used for spam or aggressive SEO.
4. **Make sure it's indexed.** Do a `site:domain.com` search. Being de-indexed is acceptable if it's
   because the domain was redirected / dormant / blocked crawlers — but **not** if it was removed for spam.

_tool(s): ahrefs, archive-org_

### Execute
**Phase 1 — Outreach.** Email owners asking if they'd sell (subject like "Interested in selling your
website?"). A short, warm note works — open with a genuine compliment, make the ask low-pressure, and
give them an easy out so it doesn't feel like a hard pitch. Template:

> Hey [Name]!
>
> I've been a long-time follower of your work in the SEO industry. Thanks for everything you've
> contributed over the years.
>
> I know this is a long shot, but I wanted to see if you'd be open to selling your website
> ([site].com).
>
> Let me know and thanks either way 👍

(Swap "in the SEO industry" for whatever niche the owner is in. The "long shot… thanks either way"
framing keeps it warm and non-pushy, which lifts reply rates on cold acquisition emails.)

**Phase 2 — Negotiation.** Export the backlink profile and assign rough value per link to anchor your
budget:
- DR 40–69 ≈ **$200**
- DR 70 ≈ **$300**

You won't pay full estimated value — the goal is to acquire for pennies on the dollar. (Harder in the
SEO niche, where everyone knows link value; easier in most other industries.) A useful counter when
they ask your offer: *"Honestly, I know you've put a lot of work into your site and don't want to
offend you. What do you think it's worth? I'll leave it up to you."*

**Phase 3 — Build (fallback).** Most deals won't close. That's fine — you now have validation that the
asset is linkable. Build a *better* version yourself and reach out to the sites linking to the original
to promote yours (this is just [[strategies/content-resurrection]] / broken-link logic applied to a
live competitor).

**Phase 4 — Merge domains (301 redirects):**
1. Run the acquired domain through **Semrush → Backlink Analytics → Indexed Pages → Export**.
2. In a redirect-mapping sheet, list each **Old URL** with its **RDs** (referring domains).
3. Map each old URL to the most relevant **New URL** on your site.
4. If no relevant page exists, **create one** to receive the links — ideally a strong linkable asset.
   (Gotch acquired a domain with many links to Facebook-marketing articles, had no matching content, so
   built data-driven content at `gotchseo.com/facebook-stats/` to receive them.)
5. **Redirect page-by-page.** On WordPress, the **Redirection** plugin can import a `.csv` of redirects
   (`source URL, target URL`). Page-by-page mapping is harder than a blanket redirect but is the best
   method — a blanket redirect of irrelevant pages can look unnatural.

## 5. Tools
- [[tools/tools#ahrefs]] — vet the acquisition's link profile (Dofollow, sort by DR) and anchor text.
- [[tools/tools#semrush]] — export the acquired domain's Indexed Pages for redirect mapping.
- [[tools/tools#archive-org]] — Wayback Machine history check for past spam.

## 6. Success metrics
- Referring domains inherited via 301s; cost per inherited RD (acquisition price ÷ links).
- Ranking lift on the destination pages after the merge (allow 4–8 weeks; see
  [[strategies/outreach-execution]]).

## 7. Risks & pitfalls
- **Expired domains** — explicitly discouraged now; too risky.
- **Buying a spammy/over-optimized domain** — can *hurt* your SEO; the vetting steps exist to prevent this.
- **Irrelevant blanket redirects** — map page-by-page to relevant destinations to keep it natural.
- **Overpaying** — value links first, then negotiate well below estimate.

## 8. Conflicting views
- None recorded yet. (Note the source's own evolution: expired-domain mergers were once recommended,
  now discouraged — captured in the warning above.)

## 9. Automation hooks
- Opportunity discovery + 100-target list building: search-string scrape + Ahrefs/Semrush API (high).
- Vetting (DR-sorted Dofollow links, anchor profile, index check): API-able scoring (partial — history
  judgment via Archive.org stays human).
- Redirect mapping: export → fuzzy-match old↔new URLs into a `.csv` → import via Redirection plugin
  (partial; relevance mapping benefits from human/LLM review).
- Outreach + negotiation + payment: manual.

## 10. Sources
- [[sources/0002-gotch-seo-academy-link-building-sop]] (Nathan Gotch) — expired-domain warning, find +
  vet process (relevance, anchors, Archive.org history, index), 4-phase execution with DR pricing,
  counter template, and Semrush-export → page-by-page 301 (WordPress Redirection plugin) merge.
