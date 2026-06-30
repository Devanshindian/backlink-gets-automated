---
slug: outreach-execution
type: strategy
title: "Outreach Execution (find contacts, send, and fix poor outreach results)"
category: outreach
aliases: ["find contact info", "send outreach", "email deliverability", "outreach troubleshooting", "cold email"]
difficulty: medium
cost: low
risk: low
white_hat: true
tools: [hunter, voila-norbert, pitchbox, buzzstream, postaga, semrush]
sources: [0002, 0006]
automatable: high
last_updated: 2026-06-19
---

<!-- WRITING STYLE: assume the reader is new to SEO. Explain every term in plain English on first use. -->

## 1. What it is
The shared mechanics behind *every* outreach-based tactic: finding the prospect's contact info,
validating it, sending and tracking outreach, and troubleshooting when results are poor. This is the
"how to actually run the campaign" layer beneath strategies like [[strategies/guest-posting]],
[[strategies/link-roundups]], [[strategies/resource-page-link-building]], and [[strategies/niche-edits]].

In plain terms: a great pitch fails if it lands in spam, hits the wrong inbox, or never gets tracked.
This file covers getting the email right and the follow-through disciplined.

## 2. Why it works
- Most outreach failure is *operational* (deliverability, wrong contact, weak subject line) — fixing
  these lifts the whole program.
- Tracking touchpoints and following up multiplies results (the SOP's flowchart calls for ~5 follow-ups
  per prospect).

## 3. When to use / prerequisites
- Any time you run an outreach campaign.
- Pair with [[strategies/outreach-value-proposition]] (the offer/WIIFM) and
  [[strategies/link-prospecting-prioritization]] (who to contact).

## 4. End-to-end process

### A. Find contact info
**Email finders:**
- **Hunter.io** — enter a domain to find email addresses and the site's common pattern (e.g.
  `{first}@domain.com`).
- **Voila Norbert** — enter a name + domain to find the email.
- **Fiverr** — many vendors will do contact-finding for you.

**Other channels:**
- **Social media** — don't restrict yourself to email; DMs work too.
- **Join their newsletter** — the sneakiest way to capture an email is to subscribe; people often send
  newsletters from a personal address.

> 📊 **Spreadsheet shortcut:** for a head start, there's a prebuilt contact list (~110 journalists &
> copywriters with email/social/topics/publications) in the database — see [[sources/0005-seo-marketing-database]] →
> **"Journalists & Copywriters"** tab. (Skews health/personal-finance; verify emails before sending.)

**All-in-one option — Semrush Link Building Tool (source 0006):** for prospects surfaced by the
[[strategies/link-prospecting-prioritization]] Link Building Tool, Semrush will **auto-find contact
emails** and let you run outreach without leaving the tool: pick an **outreach strategy** (e.g.
directory/catalog, guest post) and it pre-fills an email template with **placeholders** (domain/URL) you
can edit, then **save as a template** and **send + track** from inside Semrush. Still personalize every
email — pre-filled placeholders are a base, not a finished pitch.
_tool(s): hunter, voila-norbert, semrush_

### B. Validate contact info
Verify emails before sending so bounces don't hurt deliverability. **Hunter** streamlines this — upload
a `.csv` and it verifies the list (Fiverr vendors can also validate).
_tool(s): hunter_

### C. Send outreach
1. **Track everything.** Whether manual or with a tool, log every touchpoint — record the send date in
   the "Outreach #" columns of the link-building dashboard. (Plan for multiple follow-ups per prospect.)
   The prospect-tracking sheet on the dashboard uses these columns:

   | Column | What goes in it |
   |---|---|
   | **Status** | Pipeline stage via dropdown — e.g. `Prospect` → (contacted) → won/lost. |
   | **Outreach #1** | Date you sent the first email. |
   | **Outreach #2** | Date of the first follow-up. |
   | **Outreach #3** | Date of the second follow-up. (Add more columns if you do ~5 follow-ups.) |
   | **Link Type** | The tactic for this prospect via dropdown — e.g. `Broken Link`, `Dream 100`, guest post, niche edit, resource page, roundup. |
   | **If Other** | Free text when Link Type doesn't fit a preset option. |
   | **Source** | The prospect's URL — where you found them / the page you're targeting. |

   Use dropdowns for **Status** and **Link Type** so the sheet stays filterable (sort by Dream 100,
   see everyone still at "Prospect", etc.). One row per prospect.
2. **Try to get a branded email.** Reaching out as `john@nike.com` is far more trustworthy than
   `joe@linkbuildinggurus.com`. If you can't use the client's domain, create a dedicated outreach domain
   — and **don't** put "SEO", "backlinks", or marketing lingo in it.
_tool(s): pitchbox, buzzstream, postaga_

### D. Troubleshoot poor results (FAQ)
- **Email deliverability** — "warm up" a new email address before scaling (an aged, company email is
  best). Test your spam score *before* launching with: Hunter Email Verifier (`hunter.io/email-verifier`),
  `mail-tester.com`, `mailgenius.com`, `glockapps.com/spam-testing`.
- **Subject line** — the body doesn't matter if no one opens. Lead with the value ("what's in it for
  me"). Proven examples: "Quick question NAME", "Paid collaboration for NAME", "Can I interview you,
  NAME?", "Unique idea for your blog, NAME", "14 broken links NAME :(".
- **Value proposition** — most non-responses are a weak offer. Make it a real win-win (see
  [[strategies/outreach-value-proposition]]).
- **Poor page selection** — only promote genuinely awesome, unique-value pages; no one links to
  generic/rehashed content or commercial pages (category/product/lead-gen).
- **Lack of personalization** — generic templated blasts get ignored (and sometimes called out
  publicly). Use template libraries as a *base*, then personalize every single email.

> 📊 **Template library:** 33 ready outreach emails (by link type — roundups, resource pages, guest
> posts, brand-mention reclamation, image reclamation, skyscraper, broken links, sponsored, expert
> roundups, etc.) are in [[sources/0005-seo-marketing-database]] → **"Templates - Link Outreach"** tab.
> Treat each as a starting point, then personalize.

### E. How long until results?
Google must crawl the new backlink first (≈1–2 weeks, faster for high-authority/high-traffic sites).
After it's crawled, expect **≈4–8 weeks** to see ranking movement.

## 5. Tools
- [[tools/tools#hunter]] — find + verify email addresses (domain patterns, `.csv` bulk verify).
- [[tools/tools#voila-norbert]] — find emails by name + domain.
- [[tools/tools#pitchbox]], [[tools/tools#buzzstream]], [[tools/tools#postaga]] — outreach
  management/sending (Postaga focuses on link building).

## 6. Success metrics
- Email deliverability / spam score; open rate (subject line) → reply rate (value prop + personalization).
- Follow-ups sent per prospect; links won per 100 emails.

## 7. Risks & pitfalls
- **Scaling a cold/un-warmed email** — tanks deliverability; warm up first.
- **Marketing lingo in the outreach domain** — signals "link builder" and gets ignored.
- **One-and-done sends** — most wins come from disciplined follow-up.
- **Generic blasts** — personalize or get ignored/blasted on social.

## 8. Conflicting views
- None recorded yet.

## 9. Automation hooks
- Contact finding + validation: Hunter/Voila Norbert APIs → verified contacts (high).
- Sending, sequencing, and follow-up tracking: Pitchbox/BuzzStream/Postaga handle this natively (high).
- Deliverability pre-checks (spam-score tools) scriptable before each campaign (high).
- Personalization: LLM-drafted, human-reviewed per prospect (partial).

## 10. Sources
- [[sources/0002-gotch-seo-academy-link-building-sop]] (Nathan Gotch) — Find Contact Info (Hunter, Voila
  Norbert, Fiverr, newsletter trick), validate, Send Outreach (track everything, branded email), the
  poor-results troubleshooting FAQ (deliverability tools, subject lines, value prop, personalization),
  and the 4–8-week results timeline.
- [[sources/0005-seo-marketing-database]] — **"Journalists & Copywriters"** tab (prebuilt contact list)
  and **"Templates - Link Outreach"** tab (33 ready email templates by link type).
- [[sources/0006-semrush-backlink-tutorial]] (Semrush) — the Link Building Tool outreach layer: auto
  contact-finding, outreach-strategy templates with placeholders, and in-tool save/send/track.
