---
slug: resource-page-link-building
type: strategy
title: "Resource Page Link Building (get listed on curated 'resources' pages)"
category: outreach
aliases: ["resource page links", "links page outreach", "useful resources page"]
difficulty: medium
cost: low
risk: low
white_hat: true
tools: [ahrefs, semrush, check-my-links]
sources: [0002, 0006]
automatable: partial
last_updated: 2026-06-19
---

<!-- WRITING STYLE: assume the reader is new to SEO. Explain every term in plain English on first use. -->

## 1. What it is
Getting your content listed on **resource pages** — pages a site maintains specifically to link out to
helpful resources on a topic (e.g. a "Workout Guides" page linking to recommended workout articles).

In plain terms: some sites keep a dedicated page of "here are the best resources on X." You find those
pages and ask to be added. The page exists *to* link out, so the ask is natural.

## 2. Why it works
- Resource pages are built to link out, so the publisher is already willing to add quality links.
- They're topically focused, so the links are relevant.
- Combined with broken-link outreach, you can give the publisher a reason to edit the page (and add you).

## 3. When to use / prerequisites
- You have a genuinely useful resource worth listing (content, tool, guide).
- Pairs with [[strategies/linkable-asset-creation]] and overlaps with
  [[strategies/content-resurrection]] (both use dead links as outreach hooks).

## 4. End-to-end process

### 1. Find opportunities (search strings)
- `keyword + inurl:resources`, `Inurl:[keyword] + resources`
- `keyword + "best resources"`, `keyword + "useful resources"`, `keyword + "resources"`,
  `keyword intitle:"resources"`
- `keyword + intitle:links`, `keyword + "helpful links"`
- `keyword intext:"further reading"`, `keyword intext:"more resources"`,
  `keyword intext:"other resources"`, `keyword intext:"favorite resources"`,
  `keyword intext:"favorite tools"`

### 2. Reverse-engineer with Ahrefs
**Navigation:** Ahrefs → **Site Explorer** → competitor → **Backlinks** → search `resources`.
_tool(s): ahrefs_

### 3. Reach out

**If the page has broken links (two-email sequence):**

> **Part 1 — Subject:** Question about (insert site)
>
> Hi [First Name], today I came across your page about [quick description]. Really nice list of
> resources! I did notice that one of the links on your page is not working — let me know if you're
> still updating this site and page, and I can pass the dead link along to be fixed. Have a great day,
> [Your name]

> **Part 2** (after they reply):
>
> Hi [First Name], the broken link I found is on [Resource Page URL]. Here's the broken link:
> [Broken URL]. Also, I just posted a new resource all about [your topic]: [URL of your page]. Thinking
> this could make a nice replacement for your broken link if you'd like. Either way, keep up what
> you're doing on [Their website]! [Your name]

**If the page has no broken links:**

> **Subject:** Your awesome resource page
>
> Hey [NAME], thanks for putting together your awesome [what it is] resource. Quick question: are you
> accepting new submissions to this page? {I|We} {what you want to promote and why it's useful} and
> would love to be listed (if possible). Please let me know your terms and thanks in advance!

### 4. (Variant) Broken link building — recreate dead resources to win their links
You can also find **404 pages that still have backlinks**, recreate the asset, and reach out to
everyone linking to the dead version. This is **broken link building** in its general form, and it
works on any live, relevant site (not just resource pages):

**Navigation:** Semrush → **Backlink Analytics** → enter a competitor (or any relevant site) →
**Indexed Pages** tab → check the **Broken Pages** box. This lists the domain's dead (404) URLs sorted
by **how many domains link to them** — the most-linked dead pages (your biggest opportunities) sit at
the top.

Then, for each promising dead page:
1. **Infer what was there** from the title and URL, and decide whether you have a page that fits — or
   could build one. Skip pages you can't realistically replace (e.g. a login page — no one linking to a
   competitor's login page wants *your* login page).
2. **Confirm by opening the dead URL** (and/or a Wayback snapshot) to see the old content.
3. **Find the exact broken link on each linking page** with the **Ctrl+F / Cmd+F** trick: open a page
   that links to the dead URL, search for the dead page's **anchor text**, and it jumps you straight to
   the broken link.
4. **Find contact info** (email, social, or contact form) and reach out, offering your page as the
   replacement.

**Why it converts (win-win-win):** the reader gets a working link (better UX), the site owner fixes a
dead link that hurts their own SEO with almost no effort, and you get the backlink — as long as you hand
them a genuinely relevant replacement.

(This is the live-site cousin of [[strategies/content-resurrection]], which runs the same
Indexed Pages → Broken Pages flow against *expired domains*.)
_tool(s): semrush, check-my-links_

## 5. Tools
- [[tools/tools#ahrefs]] — find resource pages via competitor backlinks ("resources").
- [[tools/tools#semrush]] — Indexed Pages → Broken Pages to find 404s with backlinks.
- [[tools/tools#check-my-links]] — detect broken links on a resource page for outreach leverage.

## 6. Success metrics
- Resource-page placements per batch; reply/acceptance rate.
- Number of recreated-asset links won from 404 pages.

## 7. Risks & pitfalls
- **Leading with the ask, not value** — the broken-link sequence works because you help first.
- **Listing low-quality resources** — only pitch genuinely useful pages.

## 8. Conflicting views
- None recorded yet.

## 9. Automation hooks
- Discovery: search-string SERP scrape + Ahrefs API ("resources") (high).
- Broken-link detection on resource pages + Semrush Broken Pages export: scriptable (high).
- Outreach drafting: LLM template per page (partial).

## 10. Sources
- [[sources/0005-seo-marketing-database]] — **"Templates - Link Outreach"** tab (resource-page templates #2, #29, #30 + broken-link templates #16–#21) and **"Templates - Search Strings"** tab ("Find Resource Pages" operators).
- [[sources/0002-gotch-seo-academy-link-building-sop]] (Nathan Gotch) — search strings, Ahrefs
  reverse-engineering, broken-link two-email sequence + no-broken-link template, Semrush Broken Pages
  recreate-and-reach-out variant.
- [[sources/0006-semrush-backlink-tutorial]] (Semrush) — the generic broken-link workflow (Backlink
  Analytics → Indexed Pages → Broken Pages, sorted by referring domains), the Ctrl+F anchor-text trick to
  locate the broken link, and the win-win-win framing.
