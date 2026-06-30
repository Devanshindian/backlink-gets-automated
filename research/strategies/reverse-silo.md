---
slug: reverse-silo
type: strategy
title: "Reverse Silo (link to assets, internally link to money pages)"
category: technical
aliases: ["reverse silo link building", "linkable asset silo"]
difficulty: medium
cost: medium
risk: low
white_hat: true
tools: [semrush, ahrefs]
sources: [0001]
automatable: partial
last_updated: 2026-06-18
---

## 1. What it is
A way of organizing where your backlinks point. Instead of pointing links straight at your
**money pages** (the pages that sell something — product, service, or pricing pages), you point most
of your backlinks at **linkable assets** (genuinely useful free things like guides, tools, data, or
glossaries that other sites are happy to link to). Those assets then link *internally* to your money
pages.

In plain terms: it's like water flowing downhill. Links pour into your popular, useful pages at the
top, and that value flows downhill through internal links into your sales pages at the bottom.

## 2. Why it works
- **It spreads authority across the whole site.** "A rising tide lifts all ships" — when your
  linkable assets earn authority, internal links pass some of that value ("link equity" — think of it
  as a vote of trust being shared) to your money pages and the rest of the site.
- **It's safer.** Blasting links directly at sales pages leaves an obvious, unnatural pattern (a
  "footprint") that Google can spot. Pointing links at editorial assets instead looks natural, which
  lowers your risk of a link-based penalty — the most common way sites get penalized.

## 3. When to use / prerequisites
- You have (or can create) linkable assets — see [[strategies/linkable-asset-creation]].
- You have commercial pages that need authority but are risky to link to directly.
- Good when building links at any meaningful scale; especially valuable in competitive/spam-sensitive niches.

## 4. End-to-end process
1. Identify the commercial/money pages that need to rank.
2. Build linkable assets relevant to those pages — _see [[strategies/linkable-asset-creation]]_.
3. Acquire external backlinks **to the assets** (not the money pages) — _see [[strategies/linkable-asset-promotion]], [[strategies/link-prospecting-prioritization]]_.
4. Add contextual **internal links from the assets to the commercial pages**.
5. Reinforce with internal links from other existing pages to the assets. _tool(s): site search_

## 5. Tools
- [[tools/tools#semrush]] / [[tools/tools#ahrefs]] — to find which asset types attract links in your niche.

## 6. Success metrics
- Referring domains pointing to assets (rising).
- Rankings/organic traffic of the linked-to commercial pages.
- Overall domain rating/authority trend.

## 7. Risks & pitfalls
- Don't make the internal links to money pages all use the exact same keyword-stuffed text ("anchor
  text" = the clickable words of a link); repeating the same commercial phrase everywhere looks
  manipulative.
- The assets must be genuinely worth linking to — a thin, low-effort asset earns no links, so there's
  nothing to flow downhill.
- Low risk overall; this approach exists specifically to *reduce* penalty risk.

## 8. Conflicting views
- None recorded yet.

## 9. Automation hooks
- Step 5 (internal-link discovery): scriptable — crawl the site, find pages mentioning the asset's
  topic/keywords, suggest internal-link insertion points (none → partial).
- Step 3 ties into prospecting automation — see [[strategies/link-prospecting-prioritization]].

## 10. Sources
- [[sources/0001-nathan-gotch-link-building-blueprint]] (Nathan Gotch) — defined the reverse silo, its authority-spreading rationale, and penalty-risk reduction.
