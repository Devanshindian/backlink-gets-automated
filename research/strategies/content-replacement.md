---
slug: content-replacement
type: strategy
title: "Content Replacement (update outdated pages on live trusted sites)"
category: outreach
aliases: ["outdated content replacement", "skyscraper technique variant", "content update outreach"]
difficulty: medium
cost: medium
risk: low
white_hat: true
tools: [semrush]
sources: [0002]
automatable: partial
last_updated: 2026-06-18
---

## 1. What it is
Finding *live* pages on trusted industry websites that are clearly outdated (e.g. published in 2015
and never updated), creating a newer, better version of the same content, and pitching the site
owner to replace or update their old piece with yours.

In plain terms: you identify a respected website's page that has aged poorly — the information is
stale, the stats are from years ago, the advice is outdated. You build a current, comprehensive
version, then pitch it as an upgrade. They get fresh content for their readers; you earn a link.

This differs from [[strategies/content-resurrection]] (which targets *dead pages* on *expired
domains*) — here the page is *live* and on an *active, trusted site*.

## 2. Why it works
- Trusted sites that care about their readers' experience don't want to keep linking to or hosting
  outdated content. A ready-made replacement removes the work for them.
- The older the content and the more prominent the site, the more valuable the replacement link —
  because those pages often already have significant backlinks pointing at them.

## 3. When to use / prerequisites
- Works best in niches where information changes meaningfully over time (tech, regulations, pricing,
  statistics, rankings, research findings).
- You need to be able to produce a genuinely better, updated version — not just reformatted.

## 4. End-to-end process

1. **Find outdated content on trusted sites using Google search operators**

   Use the `site:` operator combined with a year to surface old posts:

   > `site:[competitor or trusted site].com + "[YEAR]"` — e.g. `site:moz.com + "2015"`

   This surfaces pages on that domain that still prominently feature the old year (often in the
   title or opening paragraph).

   Additional search strings to try:
   > `[NICHE] + "updated [YEAR]" site:[trusted domain]`
   > `[TOPIC] + "statistics [YEAR]" site:[trusted domain]`

   More operators to find outdated content:

   | Goal | Search string |
   |---|---|
   | Pages published before a year | `site:example.com before:2021` |
   | Pages mentioning a specific old update year | `site:example.com "last updated in 2018"` |
   | Pages with old copyright dates | `site:example.com "copyright 2015"` |
   | Pages with year in the URL | `site:example.com inurl:2017` |
   | Pages explicitly flagged as outdated | `site:example.com "obsolete" OR "discontinued"` |
   | Pages referencing old versions | `site:example.com "old version" OR "outdated"` |
   | Pages excluding recent years from URL | `site:example.com -inurl:2024 -inurl:2023` |
   | Archived pages | `site:example.com intitle:"archive" OR intitle:"archived"` |
   | Pages signaling unavailability | `site:example.com "expired" OR "no longer available"` |
   | Pages flagged for updates | `site:example.com "please update" OR "needs update"` |

2. **Evaluate whether the page is worth targeting**
   - Does it have significant backlinks? (Check in Semrush — Backlink Analytics → enter the page URL.)
   - Is the content genuinely outdated in a way that a new version would be clearly better?
   - Is the site the kind of place that would want to keep their content current?

3. **Create the updated replacement asset**
   Must be measurably better: updated statistics, newer examples, additional sections the old piece
   missed, improved design/UX. The bar is "clearly the definitive current resource on this topic."

4. **Send outreach**
   Reach out to the site owner or editor:
   - Point to their old page specifically (show you read it).
   - Note one or two ways the content is now outdated.
   - Present your updated resource as a ready-made replacement or reference.
   - Offer to write a new version *for their site* if they'd prefer (guest-post angle).

   _Example angle:_ "For Moz's post about 'The Incredible Shrinking SERP' (2015), I could create
   a timeline-based asset showing how SERPs have changed from 2015 to now."

## 5. Tools
- [[tools/tools#semrush]] — check backlink value of the outdated page; identify sites worth targeting.

## 6. Success metrics
- Number of outdated content opportunities identified per domain.
- Replacement placement rate (how many pitches result in a link).
- Referring domains earned per replacement asset.

## 7. Risks & pitfalls
- **Replacing instead of adding** — make sure you're not just recreating what exists; add a genuinely
  new dimension (richer data, a visual element, a timeline, a tool).
- **Pitching before the replacement is live** — same rule as content resurrection: have the asset
  ready before outreach.
- **Targeting low-authority sites** — prioritize sites where the old page already has backlinks;
  that's where the value is.

## 8. Conflicting views
- None recorded yet.

## 9. Automation hooks
- Step 1: scriptable via Google Custom Search API or site-specific crawl + year-pattern detection
  (partial — Google rate-limits automated scraping; use Semrush/Ahrefs indexed pages instead).
- Step 2: Semrush API to pull referring-domain counts per page (high).
- Full pipeline: automated discovery of outdated high-backlink pages → prioritized prospect list (high automation potential once data sources are wired up).

## 10. Sources
- [[sources/0005-seo-marketing-database]] — **"Templates - Link Outreach"** tab (outdated-content template #13, skyscraper #11/#33, shared-content #10) and **"Templates - Search Strings"** tab ("Find Outdated Content" operators).
- [[sources/0002-gotch-seo-academy-link-building-sop]] (Nathan Gotch) — search string technique, Moz example, and the outreach approach.
