---
slug: niche-edits
type: strategy
title: "Niche Edits (land a link inside an existing, already-published page)"
category: outreach
aliases: ["niche edit", "link insert", "curated link", "paid collaboration link"]
difficulty: medium
cost: high
risk: medium
white_hat: false
tools: [ahrefs]
sources: [0002]
automatable: partial
last_updated: 2026-06-18
---

<!-- WRITING STYLE: assume the reader is new to SEO. Explain every term in plain English on first use. -->

## 1. What it is
A **niche edit** (a.k.a. link insert) is the process of finding an existing, relevant, already-indexed
page and getting your link **added into it** — rather than getting a new article published.

In plain terms: instead of creating new content, you ask a site owner to drop your link into a page
they already have. Often money changes hands (an "editorial fee"), which is why this leans grey-hat.

## 2. Why it works
- The page is already indexed and may already have authority/links, so a link from it can pass value
  quickly (no waiting for a new page to age).
- It's contextual and relevant if you target pages on your topic.

## 3. When to use / prerequisites
- You're comfortable with some risk and possible paid placement (see risks).
- You have a relevant asset worth inserting a link to.
- **Flagged as not strictly white-hat:** paying for link insertions is against Google's link-spam
  guidelines. Use judgment; keep it relevant and natural. Closely related to
  [[strategies/buy-backlinks]].

## 4. End-to-end process

### 1. Find relevant pages with Ahrefs Link Intersect
**Navigation:** Ahrefs → **Keyword Explorer** → enter the keyword you want to rank for → open the
**Link Intersect** tool.

Paste the **most linked-to pages** for that keyword into the "Show me who is linking to these domains
or URLs" boxes, and put **your** page under "But doesn't link to (optional)." Ahrefs returns the
domains that link to those top pages but **not** to you — your niche-edit prospect list. Export and add
to the link prospecting database.
_tool(s): ahrefs_

### 2. Reach out
> **Subject:** Paid Collaboration with [brand name]
>
> Hi [NAME | BRAND NAME TEAM], [NAME] here from [COMPANY]. We [WHAT THE COMPANY OFFERS].
>
> I'm contacting you because I saw an article of yours here [prospect's URL] and wanted to see if you'd
> be interested in a small collaboration.
>
> We just published: "[TITLE OF ASSET]", which [UNIQUE SELLING PROPOSITION]. I was wondering if you'd
> check it out and, if it's a good fit, add it to your article?
>
> I totally understand that there might be an editorial or administrative fee for linking to our
> website. Could you mention the rates, if applicable?
>
> Let me know your thoughts on this. Thank you in advance. Best regards, [NAME]

## 5. Tools
- [[tools/tools#ahrefs]] — Keyword Explorer → Link Intersect to find pages linking to top results but
  not to you.

## 6. Success metrics
- Inserts landed per batch; relevance + authority of the host pages.
- Cost per link (when fees are involved) vs. ranking impact.

## 7. Risks & pitfalls
- **Against Google guidelines when paid** — paid link inserts can be penalized; this is grey-hat.
  Keep placements genuinely relevant and avoid obvious link networks.
- **Exact-match anchors** — over-optimized anchors compound the risk
  ([[strategies/anchor-text-optimization]]).
- **Low-quality host pages** — a link insert on a thin or spammy page can hurt more than help.

## 8. Conflicting views
- None recorded yet. (The SOP presents this as effective but explicitly frames it around a *paid*
  "collaboration," acknowledging fees — note the guideline tension.)

## 9. Automation hooks
- Prospecting: Ahrefs Link Intersect via API → domains linking to top pages but not to you (high).
- Outreach drafting: LLM template per prospect page (partial).
- Negotiation/payment: manual.

## 10. Sources
- [[sources/0005-seo-marketing-database]] — **"Templates - Link Outreach"** tab (link-insert templates #24 local-blogger, #26 competitor-link) and **"Templates - Search Strings"** tab (sponsored/competitor operators).
- [[sources/0002-gotch-seo-academy-link-building-sop]] (Nathan Gotch) — definition, Ahrefs Keyword
  Explorer → Link Intersect prospecting, "Paid Collaboration" outreach template acknowledging editorial fees.
