# Index

The single scannable map of the knowledge base. Updated on every ingestion.

## Strategies

| Strategy | Category | Difficulty | Risk | Automatable | Sources |
|---|---|---|---|---|---|
| [reverse-silo](strategies/reverse-silo.md) | technical | medium | low | partial | 0001 |
| [toxic-backlink-audit](strategies/toxic-backlink-audit.md) | technical | medium | low | partial | 0002 |
| [linkable-asset-creation](strategies/linkable-asset-creation.md) | content-driven | high | low | partial | 0001, 0002 |
| [link-bait-generation-methods](strategies/link-bait-generation-methods.md) | content-driven | medium | low | high | 0002 |
| [link-bait-asset-types](strategies/link-bait-asset-types.md) | content-driven | high | low | partial | 0001, 0002 |
| [content-resurrection](strategies/content-resurrection.md) | outreach | medium | low | partial | 0002, 0006 |
| [content-replacement](strategies/content-replacement.md) | outreach | medium | low | partial | 0002 |
| [jobs-page-link-building](strategies/jobs-page-link-building.md) | content-driven | low | low | high | 0002 |
| [founder-expert-led-link-building](strategies/founder-expert-led-link-building.md) | digital-pr | high | low | partial | 0001, 0002 |
| [get-interviewed](strategies/get-interviewed.md) | digital-pr | medium | low | partial | 0002 |
| [donation-link-building](strategies/donation-link-building.md) | outreach | low | low | high | 0002 |
| [linkable-asset-promotion](strategies/linkable-asset-promotion.md) | outreach | medium | low | partial | 0001 |
| [link-prospecting-prioritization](strategies/link-prospecting-prioritization.md) | outreach | medium | low | high | 0001, 0002, 0006 |
| [outreach-value-proposition](strategies/outreach-value-proposition.md) | outreach | low | low | partial | 0001 |
| [local-chamber-of-commerce](strategies/local-chamber-of-commerce.md) | directories-citations | low | low | high | 0002 |
| [niche-business-associations](strategies/niche-business-associations.md) | directories-citations | low | low | high | 0002 |
| [testimonial-link-building](strategies/testimonial-link-building.md) | outreach | low | low | partial | 0002 |
| [link-roundups](strategies/link-roundups.md) | outreach | medium | low | partial | 0002 |
| [reverse-expert-roundups](strategies/reverse-expert-roundups.md) | outreach | medium | low | partial | 0002 |
| [list-post-link-building](strategies/list-post-link-building.md) | outreach | medium | low | partial | 0002 |
| [resource-page-link-building](strategies/resource-page-link-building.md) | outreach | medium | low | partial | 0002, 0006 |
| [merger-technique](strategies/merger-technique.md) | technical | high | medium | partial | 0002 |
| [guest-posting](strategies/guest-posting.md) | outreach | medium | low | partial | 0002 |
| [haro-journalist-requests](strategies/haro-journalist-requests.md) | digital-pr | medium | low | high | 0002, 0003 |
| [niche-edits](strategies/niche-edits.md) | outreach | medium | medium | partial | 0002 |
| [oprah-technique-podcast](strategies/oprah-technique-podcast.md) | digital-pr | high | low | partial | 0002 |
| [awards-and-badges](strategies/awards-and-badges.md) | content-driven | high | low | partial | 0002 |
| [buy-backlinks](strategies/buy-backlinks.md) | paid | medium | high | partial | 0002 |
| [anchor-text-optimization](strategies/anchor-text-optimization.md) | technical | medium | medium | high | 0002 |
| [outreach-execution](strategies/outreach-execution.md) | outreach | medium | low | high | 0002, 0006 |
| [image-link-building](strategies/image-link-building.md) | content-driven | low | low | high | 0004 |
| [profile-link-building](strategies/profile-link-building.md) | directories-citations | low | low | partial | 0004 |

## Orchestrations

Runbooks that sequence the strategy files into end-to-end campaigns. Order + links only — all
how-to detail lives in the strategy files. The 4 original campaigns have been **refined** to absorb
the new strategies, and **5 new campaigns** added (05–09) — so all 32 strategies are now sequenced.
**Cross-cutting spines** appear in most campaigns: [outreach-execution](strategies/outreach-execution.md)
(find/verify contacts, send, follow up), [outreach-value-proposition](strategies/outreach-value-proposition.md)
(the win-win pitch), [link-prospecting-prioritization](strategies/link-prospecting-prioritization.md)
(find/rank targets), [anchor-text-optimization](strategies/anchor-text-optimization.md) (anchor guardrail),
and [reverse-silo](strategies/reverse-silo.md) (where links ultimately point).

The **Asset Engine (01) is the hub**: the Expert (02), Replacement (03), Promotion (05), Goodwill (06),
and Merger (07) engines all create or point links at assets, and the Paid Supplement (08) only layers
on once 01 is doing the heavy lifting. The **Quick-Win Link Engine (09)** is a low-effort "cheap tricks"
layer (profile + image links) that compounds in the background — a supplement, never a foundation.

| Orchestration | Goal | Strategies used (in order) |
|---|---|---|
| [01-asset-engine](orchestrations/01-asset-engine.md) | Build a link magnet, funnel authority to money pages | toxic-backlink-audit → link-bait-generation-methods → link-bait-asset-types → linkable-asset-creation → linkable-asset-promotion (→ link-prospecting-prioritization + outreach-value-proposition) → outreach-execution + anchor-text-optimization → reverse-silo |
| [02-expert-engine](orchestrations/02-expert-engine.md) | Use a real person as a link magnet | founder-expert-led-link-building → get-interviewed → oprah-technique-podcast → reverse-expert-roundups → haro-journalist-requests → outreach-value-proposition + outreach-execution → linkable-asset-creation |
| [03-replacement-outreach](orchestrations/03-replacement-outreach.md) | Replace broken/outdated links with yours | content-resurrection / content-replacement / resource-page-link-building → linkable-asset-creation → outreach-value-proposition + outreach-execution |
| [04-eligibility-pages](orchestrations/04-eligibility-pages.md) | Qualify for links a known class of sites gives out | donation-link-building / jobs-page-link-building / local-chamber-of-commerce / niche-business-associations → link-prospecting-prioritization → outreach-value-proposition + outreach-execution |
| [05-content-promotion-outreach](orchestrations/05-content-promotion-outreach.md) | Get existing content featured, listed, and linked | link-prospecting-prioritization → link-roundups → list-post-link-building → resource-page-link-building → guest-posting → outreach-value-proposition + outreach-execution + anchor-text-optimization |
| [06-goodwill-engine](orchestrations/06-goodwill-engine.md) | Give recognition/praise, get a link in return | testimonial-link-building → awards-and-badges → outreach-value-proposition + outreach-execution + anchor-text-optimization |
| [07-site-acquisition-merger](orchestrations/07-site-acquisition-merger.md) | Buy a relevant site, inherit its links via 301 | merger-technique (find/vet) → toxic-backlink-audit → merger-technique (negotiate) + outreach-execution → linkable-asset-creation → merger-technique (merge) + reverse-silo + anchor-text-optimization |
| [08-paid-supplement](orchestrations/08-paid-supplement.md) | Carefully buy/insert links atop a content foundation | link-prospecting-prioritization → niche-edits → buy-backlinks → anchor-text-optimization + outreach-execution |
| [09-quick-win-links](orchestrations/09-quick-win-links.md) | Low-effort, scalable "cheap trick" links that run in the background | profile-link-building → image-link-building → anchor-text-optimization |

> **Source 0002 fully ingested (pages 1–113).** The former "pending" list (Chamber of Commerce, Niche
> Associations, Testimonials, Link Roundups, Reverse Expert Roundups, List Posts,
> Resource Pages, Merger Technique 2.0, Guest Posts, Journalist Requests/HARO, Niche Edits, Oprah
> Technique, Awards & Badges, Advanced techniques, Vetting point system, How to Buy Backlinks, Anchor
> Text Optimization, Relationship Building & Outreach) is now all captured as strategy files above.

## Sources

| ID | Type | Expert | Title | Feeds strategies |
|---|---|---|---|---|
| [0001](sources/0001-nathan-gotch-link-building-blueprint.md) | transcript | Nathan Gotch | Link Building Blueprint | reverse-silo, linkable-asset-creation, link-bait-asset-types, founder-expert-led-link-building, linkable-asset-promotion, link-prospecting-prioritization, outreach-value-proposition |
| [0002](sources/0002-gotch-seo-academy-link-building-sop.md) | pdf (complete, pp. 1–113) | Nathan Gotch | Link Building — Gotch SEO Academy SOP | toxic-backlink-audit, link-bait-generation-methods, link-bait-asset-types, content-resurrection, content-replacement, jobs-page-link-building, get-interviewed, donation-link-building, linkable-asset-creation, link-prospecting-prioritization, founder-expert-led-link-building, local-chamber-of-commerce, niche-business-associations, testimonial-link-building, link-roundups, reverse-expert-roundups, list-post-link-building, resource-page-link-building, merger-technique, guest-posting, haro-journalist-requests, niche-edits, oprah-technique-podcast, awards-and-badges, buy-backlinks, anchor-text-optimization, outreach-execution |
| [0003](sources/0003-usman-tariq-backlinkerai-automated-haro.md) | transcript (promo, Hindi/Urdu) | Usman Tariq | How an AI tool (BacklinkerAI) almost replaced off-page SEO | haro-journalist-requests |
| [0004](sources/0004-edward-sturm-four-backlink-opportunities.md) | transcript (podcast, promo) | Edward Sturm (citing Charles Floate) | Four backlink opportunities (image link building, Favikon, Featured, Grokipedia) — ep. 958 | image-link-building, profile-link-building, haro-journalist-requests |
| [0005](sources/0005-seo-marketing-database.md) | spreadsheet (6 tabs) | (compiled database) | Database - SEO & Marketing (link-bait, journalists, ICE techniques, outreach templates, data sources, search strings) | cross-cutting — link-bait/asset, journalists→outreach, prospecting, resource/roundup/guest/donation/list/niche-edit/buy, content-replacement |
| [0006](sources/0006-semrush-backlink-tutorial.md) | transcript (Semrush tutorial, promo) | Semrush | How to find backlink opportunities with Semrush (broken link building, Link Building Tool, Backlink Gap) | resource-page-link-building, content-resurrection, link-prospecting-prioritization, outreach-execution |

## Tools
See [tools/tools.md](tools/tools.md): ahrefs, semrush, reddit, chatgpt-deep-research, chatgpt, digital-pr, spamzilla, data-miner, matchmaker-fm, hunter, voila-norbert, pitchbox, buzzstream, postaga, featured, backlinker-ai, qwoted, muck-rack, help-a-b2b-writer, sparktoro, link-prospector, zipsprout, loganix, check-my-links, archive-org, free-stock-image-sites, tineye, favikon, grokipedia, rapid-url-indexer, rankability, riverside, anchor.
