---
slug: link-prospecting-prioritization
type: strategy
title: "Link Prospecting & Prioritization (relevancy pyramid, Dream 100, LLM research)"
category: outreach
aliases: ["link prospecting", "relevancy pyramid", "dream 100"]
difficulty: medium
cost: low
risk: low
white_hat: true
tools: [chatgpt-deep-research, semrush, ahrefs]
sources: [0001, 0002, 0006]
automatable: high
last_updated: 2026-06-19
---

## 1. What it is
Two jobs: **finding** websites that might link to you (prospecting), and **ranking** that list so you
spend your time on the best targets first. The tools for this are the referral-traffic question, the
relevancy pyramid, a Dream 100 list, and using AI ("LLM" = large language model, like ChatGPT) to do
the legwork.

In plain terms: don't email 1,000 random sites. Build a short list of the *right* sites and go after
those.

> 📊 **Spreadsheet shortcuts:** two tabs in the database supercharge this — [[sources/0005-seo-marketing-database]] →
> **"Techniques - Link Building"** (≈95 techniques pre-scored on Impact/Confidence/Ease → Total — a
> ready ICE scoreboard for deciding *what* to work on first) and **"Templates - Search Strings"**
> (hundreds of Google operators grouped by link type — for *finding* the targets below).

## 2. Why it works
- **Relevance beats volume.** A few links from highly relevant, trusted sites move your rankings far
  more than a pile of links from random ones.
- **AI saves huge amounts of time.** A research task that takes a team member hours can be done by an
  AI "deep research" tool in minutes.

## 3. When to use / prerequisites
- You have an asset/page to promote and need a target list.
- Best paired with [[strategies/outreach-value-proposition]] for the actual pitch.

## 4. End-to-end process
1. **Referral-traffic question:** for each site ask "If this site linked to me, would real, relevant
   visitors actually click through and possibly become customers?" Use the answer to *rank* prospects,
   not to throw any out.
2. **Relevancy pyramid** — sort prospects into relevance "buckets" and work from the top down,
   moving to the next bucket only once the one above is used up:
   - Tier 1: 100% relevant (e.g. same-niche, same-city competitor — tiny pool, unlikely).
   - Tier 2: adjacent local businesses (plumbers, electricians, foundation repair — "home services").
   - Tier 3: same niche in other cities/counties.
   - Tier 4: locally relevant but not niche (local softball league, theater) — still trusted + local.
3. **Dream 100 — discovery process (source 0002):**

   **Navigation:** Left sidebar → **KEYWORD RESEARCH** section → **Keyword Overview** → type your
   niche broadly (e.g. "hvac", "plumbing", "personal injury lawyer") → click **Search**.

   The Keyword Overview page shows:
   - **Volume** (e.g. 201.0K monthly searches in the US)
   - **Global Volume** (e.g. 454.5K)
   - **Keyword Difficulty** (e.g. 99% — Very hard)
   - Country breakdown bars (US / IN / CA / UK)

   Scroll down or click through to the **SERP results** panel to see the top 100 ranking pages.
   Work through those domains and ask: is this a genuinely niche-relevant, trusted site I'd want a
   link from? Skip mass-market giants (Home Depot, Amazon, government directories) — they rank for
   everything but aren't realistic prospects.

   For each qualifying domain:
   - Add it to the Link Building Dashboard → **Status: Prospect** → **Link Type: Dream 100**
   - Use the Like-to-Link method ([[strategies/link-bait-generation-methods]]) on each Dream 100
     site to figure out *what kind of content* would earn a link from them.
   _tool(s): semrush_

4. **Link Intersect / Backlink Gap (source 0002):** Find sites that link to competitors but not to you.

   **Navigation:** Left sidebar → **COMPETITIVE RESEARCH** → **Backlink Gap**.

   The Backlink Gap tool has two input rows:
   - **You** field: enter your domain + set scope to **Root Domain**
   - **Competitor** fields: add up to 3 competitor domains (each has its own row; click
     **"+ Add up to 3 competitors"**)
   - Click the green **Find prospects** button.

   Results appear with these tabs across the top:
   `Best | Weak | Strong | Shared | **Unique** | All`

   Click **Unique** — this filters to domains that link to at least one of your competitors but
   **not** to you. These are pre-qualified opportunities you're currently missing.

   The results table shows:
   `Referring Domain | AS (Authority Score) ↕ | Monthly Visits | Matches | [your domain] | [competitor domain]`

   Use the **Authority Score** column to prioritize. Click **+ Start outreach** (top right) or
   **Export** to add to your link-building database.
   _tool(s): semrush_
5. **Semrush Link Building Tool (source 0006):** enter your domain + a handful of target keywords
   (delete the weak auto-suggested keywords; add real ones, e.g. "organic dog food", "natural cat
   toys"). Semrush returns a **prospect list** — sites that link to your competitors and/or rank for
   those keywords — with each prospect's domain, a content snippet, URL type, **Authority Score**, and a
   **fit rating**. Open each to vet it (the rating is a guess, not gospel), then add the good ones to the
   **In Progress** list (the outreach half of this is in [[strategies/outreach-execution]]).
   _tool(s): semrush_
6. **LLM deep research:** upload a good **SOP**, have ChatGPT Deep Research (or similar) auto-find
   opportunities (e.g. donation link-building); narrow per city. ~9 min vs. hours manually.
   _tool(s): chatgpt-deep-research_

7. **Score & rank with the point system (source 0002):** Once prospects are in your database, score
   each one to decide where it sits on the priority list — the higher the total, the more time/budget
   it deserves. (This lives in the Link Building Dashboard's "Reference - Point System" tab.) The full
   "extreme" version uses 5 points = best, 1 = worst across three groups — trim it to your situation:

   | Variable | 5 | 4 | 3 | 2 | 1 |
   |---|---|---|---|---|---|
   | **Topic relevance** | 100% | 75% | 50% | 25% | 0% |
   | **Link relevance** (the linking *page's* topic) | 100% | 75% | 50% | 25% | 0% |
   | **Keyword relevance** | 100% | 75% | 50% | 25% | 0% |
   | **Site quality** | Exceptional | High-quality | Average | Below avg | Awful |
   | **Content quality** | Exceptional | High-quality | Average | Below avg | Awful |
   | **Outbound link quality** | Exceptional | High-quality | Average | Below avg | Awful |
   | **Editorial guidelines** | Elite | Professional | Decent | Below avg | Non-existent |
   | **Traffic growth** | Explosive | Growing | Flat | Declining | Dead |
   | **Total organic traffic** | >100,001 | 50,001–100,000 | 10,001–50,000 | 1,001–10,000 | <1,000 |
   | **Total RDs** (referring domains) | >50,001 | 10,001–50,000 | 2,501–10,000 | 1,001–2,500 | <1,000 |
   | **Domain Rating (DR)** | >90 | 70–90 | 51–70 | 31–50 | <30 |
   | **Ease to acquire** | Easy | Doable | Challenging | Difficult | Impossible |
   | **Potential cost** (time + $) | $0 | Doable | Challenging | Difficult | Impossible |

   The three groups are **Relevance**, **Metrics** (site quality + authority), and **Resources** (ease
   + cost). Relevance and quality matter most; metrics confirm authority; the resources row keeps you
   from over-investing in long shots. Note the deliberate tension: a high-DR, high-relevance site might
   still score low on "ease to acquire" — the score tells you where the *effort is worth it*, not just
   where the best links theoretically are.

## 5. Tools
- [[tools/tools#chatgpt-deep-research]] — automated opportunity discovery from an SOP.
- [[tools/tools#semrush]], [[tools/tools#ahrefs]] — competitor/backlink data for prospecting.

## 6. Success metrics
- Quality (relevance, authority) of prospect list; % of Dream 100 reached/won.
- Time spent prospecting (should drop sharply with LLM research).

## 7. Risks & pitfalls
- Eliminating prospects on referral traffic alone (it's a prioritizer, not a filter).
- Chasing volume over the relevance-first principle.

## 8. Conflicting views
- None recorded yet.

## 9. Automation hooks
- **High overall.** Step 4 is explicitly automatable: SOP-driven LLM/agent prospecting → structured
  database (domain, relevance tier, contact, estimated cost).
- Steps 1–2 scriptable: score prospects by relevance tier + referral-traffic proxy.
- Dream 100 maintainable as a tracked list/CRM.

## 10. Sources
- [[sources/0001-nathan-gotch-link-building-blueprint]] (Nathan Gotch) — referral-traffic principle, relevancy pyramid (his own framework), Dream 100, LLM deep-research prospecting with an SOP.
- [[sources/0002-gotch-seo-academy-link-building-sop]] (Nathan Gotch) — Dream 100 detailed discovery process (Semrush Keyword Overview → top-100 ranking sites); Link Intersect via Semrush Backlink Gap; the 13-variable point system for scoring and prioritizing prospects.
- [[sources/0005-seo-marketing-database]] — **"Techniques - Link Building"** tab (≈95 techniques ICE-scored) and **"Templates - Search Strings"** tab (Google search operators by link type).
- [[sources/0006-semrush-backlink-tutorial]] (Semrush) — the Semrush Link Building Tool as a prospecting source (domain + keywords → prospects with Authority Score + fit rating).
