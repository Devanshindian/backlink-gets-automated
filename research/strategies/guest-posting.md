---
slug: guest-posting
type: strategy
title: "Write Guest Posts (contribute articles to other blogs for in-body links)"
category: outreach
aliases: ["guest posting", "guest blogging", "write for us links"]
difficulty: medium
cost: medium
risk: low
white_hat: true
tools: [ahrefs, rankability]
sources: [0002]
automatable: partial
last_updated: 2026-06-19
---

<!-- WRITING STYLE: assume the reader is new to SEO. Explain every term in plain English on first use. -->

## 1. What it is
Writing an article for someone else's blog in exchange for a backlink. A time-tested technique — but
it must be done the right way.

In plain terms: you give a publisher free, high-quality content; they publish it with a link to your
site. **In a perfect world the link sits in the body of the post** (where it carries the most weight),
not just in the author bio at the bottom.

## 2. Why it works
- A contextual, in-body editorial link from a relevant blog is a strong ranking signal.
- It builds your brand and relationships with publishers in your niche.
- You control the content, so you can place a natural, relevant link to your asset.

## 3. When to use / prerequisites
- You can produce (or outsource) genuinely good, on-brief content.
- You have a relevant asset worth linking to from the post.
- Pairs with [[strategies/niche-business-associations]] and [[strategies/link-prospecting-prioritization]].

## 4. End-to-end process

### 1. Find opportunities (search strings)
- `list of guest posting sites`
- `[KEYWORD] "Guest post"`
- `[KEYWORD] "Write for us"`

### 2. Reverse-engineer with Ahrefs
**Navigation:** Ahrefs → **Site Explorer** → competitor → **Backlinks** → search `/author/`,
`guest post`, or `contributor` in the referring-page filter (these patterns reveal blogs that accept
outside contributors).
_tool(s): ahrefs_

### 3. Reach out
**Important:**
- **Never write the guest post upfront.** Get approval first, *then* create.
- **Pitch unique ideas** that haven't already been covered on the target blog.

> **Subject:** Guest post ideas!
>
> Hey [NAME], my name is [YOUR NAME] and I'm the [POSITION] of [COMPANY]. I was wondering if you're
> still accepting guest posts on your blog? I'd love to add value to your audience if you are.
> Here are 3 ideas:
> - [UNIQUE IDEA #1]
> - [UNIQUE IDEA #2]
> - [UNIQUE IDEA #3]
> Let me know what you think and thanks for your time!

### 4. Create
1. **Build an SEO content brief.** Treat it like content for your own site (use the template below or
   **Rankability**). _tool(s): rankability_
2. **Write or outsource** (get budget approved; use approved vendors).
3. **Inject a link naturally.** A reliable framework:
   > If you want to learn more about [TOPIC], here are 3 awesome resources:
   > - Resource #1
   > - Resource #2 ← a link to one of *your* relevant content assets
   > - Resource #3

   Surrounding your link with other genuinely useful resources keeps it natural and editorial.

### SEO content brief template
Fill this out before writing (or hand it to a vendor) so the guest post is on-brief, optimized, and
carries your link correctly. `{...}` = fill in; `-` = leave blank until decided.

```markdown
# SEO Content Brief

## STRATEGY
- **Primary Keyword:** {the exact keyword phrase you're trying to rank}
- **Search Volume:** {searches per month according to Semrush}
- **KD %:** {#}
- **SERP Features present:** (check what shows for this query)
  - [ ] Google Ads (Top, Bottom, Shopping, etc.)
  - [ ] Featured Snippet, Instant Answer, or SGE
  - [ ] Rich Results (Reviews, Sitelinks, Breadcrumbs, etc.)
  - [ ] Local pack
  - [ ] Image pack
  - [ ] Video pack
  - [ ] Top stories
  - [ ] Local news
  - [ ] People also ask
  - [ ] Discussions and forums
  - [ ] Related searches
- **Search Intent:** -
- **Subject Matter Expert:** -
- **Content Angle:** -

## SEO
- **Title options:**
  1. {OPTION #1}
  2. {OPTION #2}
  3. {OPTION #3}
  4. {OPTION #4}
  5. {OPTION #5}
- **Meta Description:**
- **Domain:**
- **URL:**
- **Word Count Target:**
- **NLP Keywords:** See Rankability Content Optimizer report.

## WRITING GUIDELINES
- **Audience:** -
- **Formality:** -
- **Tone:** -
- **Domain:** -
- **Intent:** -
- **CTA:**
- **Models:**
- **Formatting:** Use short paragraphs (1–3 sentences), headings, subheadings, bullet points, and
  numbered lists.

## OUTLINE
-

## LINKS
| Type | Target URL | Anchor Text |
|---|---|---|
| - | | |
| - | | |
| - | | |
| - | | |
| - | | |

## DESIGN & DEVELOPMENT
Link to Brand Style Guidelines >>
- **Graphics & Images:** {N/A | enter graphic and image requirements}
- **Video:** {N/A | enter video requirements}
- **Photography:** {N/A | enter photography requirements}
- **Web Page Design:** {N/A | enter design requirements}
- **Development:** {N/A | enter development requirements related to filtering mechanisms or tools}
```

Keep anchor text in the LINKS table natural/branded ([[strategies/anchor-text-optimization]]).

## 5. Tools
- [[tools/tools#ahrefs]] — find guest-accepting blogs via competitor backlinks (`/author/`, "guest
  post", "contributor").
- [[tools/tools#rankability]] — build the SEO content brief for the guest article.

## 6. Success metrics
- Guest posts published with an in-body (not just bio) followed link.
- Relevance/authority of the host blogs; referral traffic from posts.

## 7. Risks & pitfalls
- **Writing before approval** — wasted effort if the pitch is declined.
- **Bio-only links** — aim for in-body placement; bio links are weaker.
- **Thin/spun content at scale** — low-quality guest posting is a known spam pattern; keep quality high.
- **Exact-match anchors in the body** — keep anchors natural ([[strategies/anchor-text-optimization]]).

## 8. Conflicting views
- None recorded yet.

## 9. Automation hooks
- Discovery: search-string scrape + Ahrefs API (`/author/`, "write for us") (high).
- Pitch personalization + idea generation: LLM drafts 3 unique ideas per blog from its existing content
  (partial).
- Content creation: human/SME or vetted vendor (manual).

## 10. Sources
- [[sources/0005-seo-marketing-database]] — **"Journalists & Copywriters"** tab (writer/editor contacts + their publications), **"Templates - Link Outreach"** tab (guest-post templates #3, #8, #9), and **"Templates - Search Strings"** tab ("Find Guest Posts" operators).
- [[sources/0002-gotch-seo-academy-link-building-sop]] (Nathan Gotch) — in-body-link goal, search
  strings, Ahrefs reverse-engineering, get-approval-before-writing rule, pitch template, content-brief
  + natural link-injection framework.
