---
slug: toxic-backlink-audit
type: strategy
title: "Toxic Backlink Audit (flag low-quality links before building new ones)"
category: technical
aliases: ["backlink audit", "toxic links", "disavow"]
difficulty: medium
cost: low
risk: low
white_hat: true
tools: [semrush]
sources: [0002]
automatable: partial
last_updated: 2026-06-18
---

## 1. What it is
Scanning your site's existing backlinks to flag low-quality or "toxic" ones — links from spammy
sites that may be doing more harm than good. Think of it like a health check before adding more
weight: you want to know what's already there before pouring effort into new link building.

**Important caveat from Gotch:** the goal is *awareness*, not panic. You're cataloguing the
bad-looking links, not automatically removing them. Even some technically "toxic" links may be
harmless or even net-positive because of the traffic they send.

## 2. Why it works
- Google can detect link profiles that look manipulated. A clean, natural-looking link profile
  is the baseline you want before scaling link acquisition.
- Knowing which links are problematic helps you prioritize: if a keyword is stuck despite good
  on-page work, a toxic link cluster could be dragging it down.

## 3. When to use / prerequisites
- **Run this before starting any new link-building campaign** — it's step 3 in the example
  workflow (after taking asset inventory and generating link-bait ideas).
- Also run when: taking over a site, diagnosing a rankings drop, or noticing a sudden influx of
  low-quality links (could be a negative SEO attack).

## 4. End-to-end process

### Part A — Manual scan (seven toxic types to look for)
Open your backlink list in Semrush or Ahrefs and scan for each of these:

1. **DoFollow blog comments** — spammy comments on random posts, with a keyword-stuffed anchor
   text link. ("Click here for gymnastic mats" type comments.) The site owner didn't editorially
   choose to link to you; someone spammed your URL into a comment box.
2. **Directory links with keyword-rich anchor text** — cheap paid directory listings where your
   money keywords were used as the anchor text. The combination of "directory" + "keyword anchor"
   is a red flag.
3. **Spammy donation links** — lists of donors on low-quality sites. Tells you someone bought a
   "donation link" package in the past.
4. **Article directory links** — thin, machine-spun articles on sites like EzineArticles or
   similar article farms, stuffed with keyword links.
5. **Web 2.0 links** — links buried in subdomains like `johndoe123.wixsite.com/mysite/post/...`
   or deep inside Weebly, Blogger, etc. Very low link equity; usually built by cheap services.
6. **Public blog networks (PBNs)** — sites with a suspiciously high number of "Linked Domains"
   or external links and *zero* organic traffic/keywords. They exist only to sell links.
   *For example, in Semrush or Ahrefs you might see a site with 1,155 Linked Domains and
   1,828 Ext. Links but Traffic: 0.00. That's a textbook PBN signal — it has no organic
   traffic yet links out to a massive number of different websites, which is exactly the
   behaviour of a site built purely to distribute link juice.*
7. **Fake .edu/.gov backlinks** — comment spam or deeply buried links on .edu/.gov subpages.
   These are sold as "powerful .edu/.gov links" but are the same as comment spam.

Add every flagged link to the **"Toxic Backlinks" tab** in the Link Building Dashboard.

### Part B — Semrush Backlink Audit (semi-automated)

**Navigation:** Left sidebar → **SEO** section → **Link Building** → **Backlink Audit**.

1. On the Backlink Audit landing page you'll see a table of your projects. Find the domain you
   want to audit (or click **Set up** if it hasn't been configured yet). The table shows each
   domain's **Overall Toxicity Score** (High / Low / N/A) and the date of the last re-crawl.

2. Click into the project. The **Overview** dashboard shows:
   - **Overall Toxicity Score** badge (e.g. "High — Your backlink profile looks dangerous!")
   - **Toxic domains** count (e.g. 205 — 6.3% of referring domains)
   - **Potentially toxic** count (e.g. 325 — 10.0%)
   - **Non-toxic** count (e.g. 2.7K — 83.7%)
   - **Referring Domains** total with breakdown (New / Broken / Lost)
   - **Analyzed Backlinks** total

3. Click the **Domains by Toxicity Score** tab (next to "Profile Dynamic" and "New & Lost Domains").
   This shows a colour-coded bar chart over time with checkboxes to toggle:
   **Disavowed | Non-toxic | Potentially toxic | Toxic**
   Use the **Weekly / Last 3M / Last 12M** toggle to see trends.

4. Switch to the **Audit** tab to get the full list of flagged domains. For each flagged domain
   you can click through to see which specific backlinks triggered the toxicity flag.

5. Manually review each flagged domain. Add confirmed toxic links to the **"Toxic Backlinks" tab**
   in the Link Building Dashboard with these columns: Action | Status | Date | URL | Domain.

## 5. Tools
- [[tools/tools#semrush]] — Backlink Audit tool provides an automated toxicity score and domain breakdown.

## 6. Success metrics
- Number of toxic/potentially-toxic links identified and catalogued.
- Toxicity score trend over time (should fall as the profile matures naturally or links drop off).

## 7. Risks & pitfalls
- **Don't rush to disavow.** Gotch explicitly says: *"I don't recommend disavowing in 99.9% of
  cases."* The only scenario that warrants it is an active **negative SEO attack** — and even
  then, it's risky because a poorly done disavow file can accidentally disavow good links.
- Even a clearly spammy link (the "Gotch SEO" donation example in the PDF) may not be doing
  measurable harm on its own. Use judgment, not automation.
- Semrush's "toxicity" score is a heuristic, not a Google signal — don't treat every flagged link
  as a confirmed problem.

## 8. Conflicting views
- None recorded yet.

## 9. Automation hooks
- Step 1 (manual scan): automatable via Semrush/Ahrefs API — pull full backlink list, apply
  heuristic filters (anchor text over-optimized + directory domain, subdomain depth > 2, DR=0
  + no organic traffic, etc.) to pre-flag candidates for human review (partial).
- Step B (Semrush audit): API-accessible; toxicity data can be pulled into a dashboard (high).

## 10. Sources
- [[sources/0002-gotch-seo-academy-link-building-sop]] (Nathan Gotch) — seven toxic types, SEMRush workflow, disavow philosophy.
