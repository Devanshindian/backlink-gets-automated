---
slug: list-post-link-building
type: strategy
title: "List Post Link Building (get included in 'best/top X' list articles)"
category: outreach
aliases: ["list post links", "best of list links", "top X list building"]
difficulty: medium
cost: low
risk: low
white_hat: true
tools: [ahrefs, check-my-links]
sources: [0002]
automatable: partial
last_updated: 2026-06-18
---

<!-- WRITING STYLE: assume the reader is new to SEO. Explain every term in plain English on first use. -->

## 1. What it is
Getting your business, tool, blog, or content added to "best of" / "top X" list articles — e.g.
"29 Awesome SEO Blogs to Follow (Graded and Ranked)".

In plain terms: writers publish curated lists ("the 12 best plumbers in St. Louis", "top 20 SEO
tools"). You reach out and ask to be added. Like roundups, it's content-dependent — you usually need
real content, a tool, or a strong blog to deserve a spot.

## 2. Why it works
- List posts are editorial, often rank well, and exist to feature/link to things — a natural link target.
- Inclusion alongside respected names lends credibility (and referral traffic from list readers).

## 3. When to use / prerequisites
- You have something genuinely list-worthy: content, a tool, or a strong blog/brand.
- Pairs with [[strategies/linkable-asset-creation]] (build the thing worth listing first).

## 4. End-to-end process

### 1. Find opportunities (search string syntax)
`{top|best} {niche|city} {blogs|tools|training|courses|websites|designs|landing pages|companies|
examples|podcasts|experts|experts to follow|infographics|newsletters|newsletter sign up forms|call to
action|twitter|influencers|things to do|things to eat|things to see|essential|facebook ads|google
ads|advertising examples|email marketing examples|copywriting examples|of all time|places to learn}`

### 2. Reverse-engineer with Ahrefs
**Navigation:** Ahrefs → **Site Explorer** → competitor → **Backlinks** → search `best`, `examples`,
or `top` in the referring-page URL filter.
_tool(s): ahrefs_

### 3. Reach out
> **Subject:** Awesome list!
>
> Hey [NAME],
>
> Thank you so much for putting together the awesome list of [insert what it is]. I [something specific
> from the content: what you liked, an insight you gained].
>
> I was wondering if you're accepting submissions to this list at this time? [I|We] [what you want to
> be promoted on this list] and think it would help your audience a ton.
>
> Please let me know if this is possible and what your terms are. Thanks for your time!

**Leverage tip:** run the list page through **Check My Links** (a Chrome extension that highlights
broken links on a page). If the list has dead links, mention them in your outreach — offering to flag a
broken link gives the author a reason to reply and edit the page (where they can also add you).
_tool(s): check-my-links_

## 5. Tools
- [[tools/tools#ahrefs]] — find list posts via competitor backlinks ("best"/"examples"/"top").
- [[tools/tools#check-my-links]] — spot broken links on the list page to use as outreach leverage.

## 6. Success metrics
- List inclusions per batch; authority/traffic of the list pages.

## 7. Risks & pitfalls
- **Pitching to be listed when you're not list-worthy** — build the asset first.
- **No personalization** — reference a specific item you liked; generic asks get ignored.

## 8. Conflicting views
- None recorded yet.

## 9. Automation hooks
- Discovery: expand the syntax into queries + SERP scrape + Ahrefs API competitor mining (high).
- Broken-link detection on list pages: scriptable (crawl + status-code check) to auto-generate leverage
  (high).

## 10. Sources
- [[sources/0005-seo-marketing-database]] — **"Templates - Link Outreach"** tab ("top blogs" inclusion template #31) and **"Templates - Search Strings"** tab ("Find Lists" operators).
- [[sources/0002-gotch-seo-academy-link-building-sop]] (Nathan Gotch) — search-string syntax, Ahrefs
  reverse-engineering, outreach template, Check My Links broken-link leverage tip.
