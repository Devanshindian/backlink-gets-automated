---
slug: get-interviewed
type: strategy
title: "Get Interviewed (podcasts, YouTube, expert features for backlinks)"
category: digital-pr
aliases: ["podcast link building", "interview link building", "podcast guest links"]
difficulty: medium
cost: low
risk: low
white_hat: true
tools: [semrush, ahrefs, matchmaker-fm]
sources: [0002]
automatable: partial
last_updated: 2026-06-18
---

## 1. What it is
Getting a founder or subject-matter expert booked as a guest on podcasts, YouTube shows, and
expert-interview features — specifically ones that **link back to your website** in their show notes
or episode page.

In plain terms: when you appear on a podcast, the host typically writes an episode page with
show notes listing guest links. That's an editorial backlink from a real, trusted domain — and it
came from a conversation, not cold outreach begging for a link.

This is a more operationally specific version of [[strategies/founder-expert-led-link-building]],
focused entirely on the podcast/interview channel.

**Critical filter:** only target opportunities that *actually link out* on their website. Some
shows only appear on Spotify/Apple Podcasts with no website page — those are still valuable for
brand exposure but produce no backlink.

## 2. Why it works
- The link is editorial (the host decided to include it) — a strong signal to search engines.
- The guest relationship makes the link natural and contextually relevant.
- Podcast and YouTube audiences are often high-trust, so referral traffic converts well (aligning
  with the [[strategies/link-prospecting-prioritization]] referral-traffic principle).
- Warm pitches (where you've had some interaction before asking) dramatically outperform cold ones.

## 3. When to use / prerequisites
- A figurehead or SME exists who can speak credibly on a topic — see [[strategies/founder-expert-led-link-building]].
- They need 3 compelling "episode headline" ideas that would genuinely interest a podcast audience.
- Works best when combined with warm relationship-building (following hosts, commenting, joining newsletters) before outreach.

## 4. End-to-end process

### Finding opportunities (six methods)

**Method 1 — Google search strings:**
- `"[INFLUENCER NAME]" + "interview"`
- `[NICHE] + "interview with"`
- `inurl:[keyword] inurl:podcast`

**Method 2 — Reverse-engineer competitors in Semrush:**

**Navigation:** Semrush → enter the competitor's domain in the search bar → **Backlink Analytics**
→ **Backlinks** tab.

In the Backlinks tab filter bar, locate the search input labeled **"Filter by title or URL"**
(right side of the filter strip). Type `interview` or `interview-with`. Semrush will filter the
backlink list to only rows where the *source page URL* or title contains that word — surfacing every
site that has published an interview with your competitor.

The results show:
`Page AS | Source page Title and URL | Ext. Links | Int. Links | Anchor and Target URL | First Seen | Last Seen`

Scan for shows that have their own website episode pages (not just Spotify/Apple URLs) — these are
the ones that will produce a backlink.
_tool(s): semrush_

**Method 3 — Reverse-engineer competitors in Ahrefs:**

**Navigation:** Ahrefs → enter the competitor's domain → **Backlinks** report.

Apply these filters:
- Toggle **All** → **Dofollow** (top-left selector, changes from "All" to show only followed links)
- Click **+ More filters** → add **DR: From 30** (Domain Rating minimum — filters out low-authority podcasts)
- Click **Ref. page URL** dropdown → select **Contains** → type `interview-with`
- Optional: enable **"Exclude subdomains"** toggle to keep results to root domains

Active filter chips will show:
`Backlink type: Regular links × | DR: From 30 × | Ref. page URL: Contains interview-with ×`

The results table shows:
`Referring page | DR | Domain traffic | Referring domains | Linked domains | Ext. Page | Kw. | Page traffic | First / Last seen`

Sort by **Domain traffic** descending to prioritize the shows with the biggest audiences.
_tool(s): ahrefs_

**Method 4 — Spotify or Apple Podcasts native search:**
Search your niche keywords directly in Spotify or iTunes. Browse the results; check each podcast's
website to confirm they link to guests.

**Method 5 — YouTube:**
Same search strings as Google work well on YouTube:
- `"interview with" + "[NICHE]"`
- Confirm the video description or about page links to guests.

**Method 6 — Matchmaker.fm:**
A dedicated platform connecting podcast hosts with potential guests. Create a profile describing
your expert's background and the topics they can speak on. Podcast hosts browse and invite guests.
_tool(s): matchmaker-fm_

### Vetting: does the show link out?
Before adding to your outreach list: visit the show's website and check a recent episode page.
Confirm there is a dedicated episode page with show notes containing guest website links
(not just a podcast aggregator embed).

### Outreach

**Cold outreach template:**

> **Subject:** Podcast Guest Pitch: [TOPIC // EXPERTISE]
>
> Hi [podcast host name],
>
> I'm [name], and I'm a [job title] at [organization name]. I [what you do that's relevant to
> the podcast].
>
> I really enjoyed the episode where you discussed [specific topic of the episode]. [Unique
> insight you gained from the episode].
>
> I believe there is a gap in the conversation [unique value you can add]. I have a few ideas
> of what I could talk about on your podcast to help fix this. I could make an episode on any
> of these, or any other ideas you have that your audience would find interesting.
>
> HEADLINE IDEA #1
> HEADLINE IDEA #2
> HEADLINE IDEA #3
>
> I [1–2 sentences on credentials and why you're qualified to speak on X].
>
> Please let me know if you're accepting new guests — thanks for your time!

**Warm outreach (preferred):**
Build a relationship first — listen to the show, comment meaningfully, join their newsletter —
then reach out informally:

> "Hey [NAME], hope business is going well! I just finished your interview with [GUEST] and it was
> awesome. Are you bringing any new guests on? I'd love to geek out about [TOPIC] if you're open
> to it. Thanks either way!"

Warm outreach converts significantly better because there is an existing relationship; the host
already "knows" you.

## 5. Tools
- [[tools/tools#semrush]] — competitor backlink search filtered by "interview" in the URL.
- [[tools/tools#ahrefs]] — same; DR filter adds quality control.
- [[tools/tools#matchmaker-fm]] — podcast guest/host matching platform.

## 6. Success metrics
- Number of podcast appearances booked per month.
- % of appearances that result in a followed, editorial backlink on the show's website.
- Authority and relevance of the linking domain (check DR/AS).

## 7. Risks & pitfalls
- **Booking shows that don't link** — always verify the show has a website with episode pages before investing prep time.
- **Cold pitching without personalization** — referencing a specific episode or insight signals you
  actually listened; generic pitches are ignored.
- **Expert unavailability** — interview link building is bottlenecked by the figurehead's schedule;
  batch record sessions to make efficient use of time.

## 8. Conflicting views
- None recorded yet.

## 9. Automation hooks
- Methods 2 & 3 (competitor backlink mining): Semrush/Ahrefs API → pull backlinks filtered by "interview" URL pattern → prioritized list (high).
- Matchmaker.fm: semi-automated matching (platform handles discovery, human handles conversation).
- Outreach personalization: LLM can draft warm/cold templates per show using episode data (partial — requires episode-page scraping for context).

## 10. Sources
- [[sources/0005-seo-marketing-database]] — **"Journalists & Copywriters"** tab: prebuilt media contacts (with topics + publications) to pitch for interviews/features.
- [[sources/0002-gotch-seo-academy-link-building-sop]] (Nathan Gotch) — all six discovery methods, vetting filter, cold and warm outreach templates, Matchmaker.fm recommendation.
