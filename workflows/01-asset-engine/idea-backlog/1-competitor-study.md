---
type: workflow-step
parent: asset-engine / idea-backlog (Method 1 of 3)
reusable: any company
needs: Semrush (backlink access) · the company's brand brain (for named competitors) · our page extractor
produces: projects/[company]/asset-engine/competitor-study/
last_updated: 2026-06-22
---

# Idea Backlog — Method 1: Competitor Study

**The single strongest way to find link-bait ideas:** look at the pages that already earn competitors the
most backlinks, and steal the **format** (not the topic). If a *format* pulled hundreds of linking domains
for a competitor, that format works in this niche — so we build our own version of it on a topic we own.

> **Format, not topic.** The *topic* is what a page is about (retention bonuses, a typing-speed test). The
> *format* is its shape (a "what is X / how it works" post, an annual data report, a free skills test). We
> copy the **shape that earns links**, never the exact topic — copying the topic just means competing
> head-to-head and losing. Example: TestGorilla's "Retention Bonus: What It Is, How It Works" → topic =
> retention bonus (ignore); **format = definitional answer-bait (steal this)** → apply it to a Testlify term.

This is **Method 1 of 3** that feed the idea backlog (the others: Model Other Niches, Study
Trends — separate files). Each method adds ideas to the same pool.

---

## Output (what this step produces) — and the folder layout
**Keep the folder clean. Only the deliverables sit at the top; raw inputs and working files go in subfolders,**
so anyone opening `competitor-study/` immediately sees what matters.

```
projects/[company]/asset-engine/competitor-study/
  competitor-study-ideas.xlsx   ← ★ THE DELIVERABLE (decision file): format summary + the ranked, MERGED ideas
  competitor-formats.xlsx       ← the MASTER / evidence file: one row per kept page (every page read), tagged + idea#
  competitors.md                ← the 15 chosen competitors + category (Step A)
  brand-scope.md                ← the approved brand scope (G0) — the reference every G2 agent reasons against
  RUN-LOG-problems.md           ← per-run log of anything that broke + how it was handled
  _raw/                         ← raw Semrush exports: [competitor]-indexed-pages.csv  +  discovery/ (competitor lists)
  _work/                        ← everything intermediate: _candidates/, fetch/+digests/ (Step E),
                                  agent_out/ (G2 sub-agent chunks), format-summary.csv, ideas.csv, scripts
```

The two files you actually use:
1. **`competitor-study-ideas.xlsx` — the decision file.** Tab 1 = the **format summary** (Step F, "which shapes
   earn links"). Tab 2 = the **ideas** (Step G), one row per distinct, plain-named idea, each with a **Build?**
   verdict (✅ core / ⚠️ adjacent / ❌ off-brand-skip), ranked **tier-first then by domains**, showing its source pages.
2. **`competitor-formats.xlsx` — the master / evidence file.** One row per kept page across all competitors:
   `Competitor | URL | Format | Domains | Backlinks | What it is | Build? | Idea`. Every row is read (Step E) and
   tagged to the idea it rolls up into. This is the long list **with** duplicates; the deliverable is that same
   data **collapsed** into the ranked shortlist.

> **One deliverable, one master — and they are different files on purpose.** Don't ship the ideas file as a
> `.csv` *and* `.xlsx` of the same thing (that's the confusing duplication). One name = one job.

---

# ✅ RUN CHECKLIST — tick every box; do not call the run done until all are ticked
> Copy this into the run's `RUN-LOG-problems.md` and tick as you go. It exists because steps get silently
> skipped (Step E was once faked with page titles). A box is only ticked when it is *really* true.

**Setup & inputs**
- [ ] `competitors.md` exists and the 15 are user-approved (Step A4 gate passed).
- [ ] All approved competitors received as exports; missing ones explicitly listed (e.g. "12/15; missing: …").
- [ ] **Every export validated** (real header row, not an HTML login wall; not a tiny file); newest dup used.
- [ ] Raw exports filed to `_raw/`; folder structure created (`_raw/`, `_work/`).

**Step C — filter**
- [ ] Top 300 by Domains taken per competitor; junk dropped (home/root-variants/locale/commercial/nav/non-content subdomains/404). **Non-200 content paths (301/302/0) KEPT** — only root-variant redirects + 404/410 dropped. Per-competitor kept counts sanity-checked (no competitor an order of magnitude below the rest).
- [ ] Keyword matching done on the **URL path**, not the full URL (brand-name-in-domain trap avoided).
- [ ] Free tests/tools/calculators **kept**; per-competitor candidate lists saved to `_work/_candidates/`.

**Step D — tag format**
- [ ] Every kept page tagged with a format; new formats named + defined when nothing fits.

**Step E — read (the one that gets skipped)**
- [ ] **Every kept row** fetched and read — not a top slice.
- [ ] "What it is" = the full scraped page text (verbatim), not a summary — **zero** rows left as `(from title)`.
- [ ] Un-fetchable pages marked `FETCH FAILED` (never disguised).
- [ ] **Read tally printed + logged:** `N rows → X read, Y failed`, and X + Y = N.

**Step F — aggregate**
- [ ] `_work/format-summary.csv` written (`Format | # pages | Total Domains | Avg Domains`, ranked).

**Step G — ideas (brand scope → parallel reasoning → intelligent merge → rank)**
- [ ] **G0 `brand-scope.md` distilled from the brand brain FIRST and user-approved** (a derived scope, NOT a hand-written topic list).
- [ ] Every kept row reasoned against the brand scope by the **G2 sub-agents** (sharded by format); every row returned exactly once and stitched back by Row ID (no holes).
- [ ] Every row's `Asset` is a **real working title**, not `<Format> on <Topic>` glued together (see G2's good/bad table). Free text, no forced key.
- [ ] Every row's `Angle gap` cites a concrete fact from THAT page; **no gap string appears in >~10 rows** (≥1 distinct gap per 5 rows).
- [ ] Every row has a `Brand fit` (CORE / TRANSPLANT / ADJACENT / SKIP).
- [ ] **G3 merge done by one strong-model intelligent read of all assets (no string keys)**; rows assigned to ideas; **duplicates + over-merges fixed**.
- [ ] Each idea has a `Distinct angle` from the actual gaps; scored `Beatability` (1–3) + `Effort` (S/M/L); ranked **Brand fit → Evidence × Beatability → Effort**.
- [ ] `Build window` set (NOW vs LATER) by team capacity, not list length.
- [ ] **G6 sanity check ticked in full** before declaring G complete.

**Step H — deliver**
- [ ] `competitor-study-ideas.xlsx` (Tab1 summary + Tab2 merged ideas) written.
- [ ] `competitor-formats.xlsx` (master, every row, with Idea#) written.
- [ ] No duplicate "same data as .csv and .xlsx"; folder clean (only deliverables + `competitors.md` +
      `RUN-LOG-problems.md` at top; everything else in `_raw/`/`_work/`).
- [ ] `RUN-LOG-problems.md` updated with problems, fixes, and the read tally.

---

# Step A — Identify & categorize the competitors
You can't study competitors until you've named them — and **most companies won't list their rivals on a
`/vs/` or `/alternatives/` page**, so don't rely on the brand brain alone. Build the list from **Semrush +
the user**, then **gate on the user's approval** before studying anyone.

### A1. Gather candidate competitors (3 sources)
> **Two of these run in Semrush on the user's login — the agent can't.** Give the user the exact steps,
> have them export both files, and **attach them here.**

1. **Semrush — Main Organic Competitors (sites ranking for the same keywords).** Walk the user through:
   left sidebar **SEO → Domain Overview** (under *Competitive Analysis*) → type **[the company in focus]** →
   Search → scroll to **"Main Organic Competitors"** → **Export → Excel/CSV, top 100**.
2. **Semrush — Main Paid Competitors (sites bidding on the same terms = direct commercial rivals).** Same
   Domain Overview page → **"Main Paid Competitors"** → **Export → Excel, top 100**.
3. **Ask the user directly:** "Any competitors you already have in mind?"

Save both files to `projects/[company]/asset-engine/competitor-study/discovery/`. Their columns:
`Domain · Competitor Relevance · Common Keywords · Organic Keywords · Organic Traffic · Organic Cost ·
Adwords Keywords` (organic) and the Adwords equivalents (paid).

### A2. Build the shortlist (15)
From the two files + the user's suggestions, pick **15 competitors**:
- **Rank by Competitor Relevance** (both files are sorted by it — the truest "are they really a competitor"
  signal). Among the relevant ones, prefer higher **Organic Keywords / Traffic** = more content = more
  formats to mine.
- **Domains that appear in BOTH the organic *and* paid lists are the strongest** — prioritise them.
- Take a few from each list + anything the user named; **dedupe; drop the company itself** and obvious
  non-competitors (consumer-only or off-topic domains).

### A3. Categorize (direct vs adjacent)
**First, search each of the 15 before you bucket any of them.** A domain name alone doesn't tell you what a
company does, so **run a quick web/Google search on each competitor** ("what is [domain]" / its homepage) to
confirm what it actually sells and who it sells to. Don't guess from the name. Then bucket each, aiming for
**~10 direct + ~5 adjacent**:
- **Direct** — *same product* (skills assessment / hiring tools). "What link-bait works in our exact space."
- **Adjacent content leaders** — *same audience, different product* (ATS, HR academies, HR authorities like
  Workable / AIHR / SHRM). Format goldmines.
- **If the lists contain no adjacent content leaders, add them yourself** (from the search) — every niche
  has 2-3 big content machines worth mining.

### A4. Get the user's sign-off (this is a gate)
Present the final 15 + the split: *"These are the 15 — X direct, Y adjacent. Good to proceed?"*
**Only continue to Step B once the user approves.** Then write the approved list to `competitors.md` in this
format:
```markdown
# Competitors — [Company]

## Direct competitors (same product)
- [Name] — [domain]
- …

## Adjacent content leaders (same audience, format goldmines)
- [Name] — [domain]
- …
```

---

# The loop — run Steps B → E for every competitor
Steps **B, C, D, E repeat for each of the 15 approved competitors.** Each pass appends that competitor's
kept pages to **one growing master sheet** — `competitor-formats.csv` — so by the end of the loop you have a
single complete detail sheet across all 15. Only *after* the loop do you aggregate (Step F), write ideas
(Step G), and build the final file (Step H).

Master sheet columns (built across the loop): `Competitor | URL | Format | Domains | Backlinks | What it is`
(Step D writes the first five; Step E fills "What it is"; Step G adds the idea column later).

---

# Step B — Pull a competitor's Indexed Pages (Semrush)
> **This runs in Semrush on the user's login — the agent can't.** Walk the user through it; they export the
> file and hand it over.

For the current competitor:
1. Top search bar → type the competitor domain → set scope to **Root Domain** → Search.
2. Left sidebar → **Link Building → Backlinks** (opens Backlink Analytics).
3. In the tab row at the top, click **Indexed Pages**. *(This lists the competitor's own pages ranked by how
   many sites link to each — their link magnets. Not "Top Pages," which is by traffic.)*
4. Click the **Domains** column header → sort **descending**.
5. **Export → CSV/XLSX.** Semrush exports the **whole** list (can be tens of thousands of rows) — there's no
   "top 300" option, that's fine. The **agent** slices the top 300 by Domains when processing (Step C).
6. **Just attach the file in the chat** — the agent copies it into
   `projects/[company]/asset-engine/competitor-study/_raw/[competitor]-indexed-pages.(csv/xlsx)` itself.
   (No need to save it to a path by hand.)

> **Validate every export before trusting it (learned the hard way):**
> - The first row must be the real header `Source url,Source title,Response code,Backlinks,Domains,...`.
>   If the file starts with `<!DOCTYPE html>` or is only a few KB, **the export failed** — it's a Semrush
>   login / "Multilogin" wall saved as a .csv. Log back in and re-export.
> - A domain that should have thousands of pages but produced a tiny file is a red flag.
> - **Tick off each approved competitor as its valid file arrives** (15 approved vs N received) so a missing
>   one is obvious *before* processing — e.g. "12 of 15 received; missing: PMaps, HireVue, Thomas."
> - Browser "(1)/(2)" suffixes mean a re-download — always use the newest.

---

# Step C — Filter the top 300 down to the replicable pages
**Work from the file saved in Step B:**
`projects/[company]/asset-engine/competitor-study/[competitor]-indexed-pages.(csv/xlsx)`.
Take its **top 300 rows by Domains** (it's already sorted that way), then **drop** these (they're not
formats we can build):
1. **Homepages / root variants** — `domain.com/`, `www.`, `http://…`, `?affiliate=`/tracking-query homepages,
   empty or brand-only titles. Drop these at **any** response code.
2. **Dead pages only** — `404` / `410` (genuinely gone). **Do NOT blanket-drop every non-200.** A `301`/`302`/
   `307`/`308` (or a Semrush `0`) on a *root* URL is just a homepage dupe and is already dropped by rule 1 — but
   the **same codes on a real content path are kept**: many sites serve their actual editorial on redirecting
   URLs (a migrated blog whose old `/article/NNN/…` slugs still hold all the domains) or return `0` for JS-rendered
   pages Semrush couldn't probe. Those redirect to live content the moment you fetch them and still earn the links,
   so dropping them throws away exactly the formats we're hunting. **Rule: keep any non-200 with a substantive
   content path; only root-variant redirects (rule 1) and `404`/`410` are dropped.**
3. **Locale duplicates** — `/fr/`, `/de/`, `/es/`, `/nl/`, `/ja/`… (first path segment is a 2-letter locale) → keep the one English original, drop the rest.
4. **Commercial / utility pages** — pricing, login, signup, contact, "for enterprise", solution/marketing pages.
5. **Navigation / archive** — `/blog/` index, author / tag / category archive pages.
6. **User-generated / utility** — user certificate pages (`/cert/…`, `download-certificate`), single
   question pages and filtered question lists (`/questions/…`, `/questions?…`), `/for-jobseekers`, homepage
   variants (`/home-redux/`), and capitalised nav dupes (`/Tests`). These slip through and earn "links" only
   from user shares — not replicable formats.
7. **Job postings & app pages** — individual job ads on customers' ATS subdomains/paths (`…/jobs/<id>`,
   `recruiterflow.com/<db>/jobs/…`, `<customer>.talentlyft.com/jobs/…`), and the product app itself
   (`/auth/`, `/quizzes/`, `/reports/`, `/instructions`, `/registration`, `/tour`, `/api`, `/openapi`).
8. **Non-content subdomains (use an allow-list, not a block-list)** — keep only the subdomains that actually
   carry editorial: **root, `www.`, `blog.`, `resources.`**. Drop **every other** subdomain — these are customer
   ATS career sites (`<customer>.talentlyft.com`, `bracbank.imocha.io`), the test/app runtime (`assess.`, `test.`,
   `tests.`, `app.`, `hireselect.`), and utility (`help.`, `support.`, `accounts.`, `get.`, `go.`, `status.`). An
   allow-list is safer than naming each bad subdomain: a customer's brand name can be anything, so you can't
   enumerate them — only the handful of content subdomains are knowable.

**Keep** everything editorial or genuinely useful — including **free tests / tools / calculators**, even
though they're technically "product" pages: they earn real links and are replicable (this is usually the
single most valuable format for an assessment company). Only *commercial* product pages get dropped.

After this, ~120-250 pages per competitor typically remain (fewer for small/migrated sites). Tag/scrape only those.

> **Caution — the redirect trap (learned the hard way, 2026-06-26):** an early version of the filter dropped
> **every** non-200 row ("redirects = homepage dupes"). It quietly destroyed real editorial: eSkill collapsed
> to 38 kept pages and TalentLyft to 22, because both serve their content on `301`-migrated URLs, and
> TestGorilla/Vervoe's free **test-library** pages came back as Semrush `0`. The whole study is built on
> *recurrence of formats* — silently deleting a competitor's editorial wrecks that signal. **Over-dropping is
> unrecoverable; over-keeping isn't** (a commercial page that slips through gets marked `SKIP` later at G2). So
> bias toward keep: only kill root-variant redirects and `404`/`410` (rule 2). Sanity-check per-competitor kept
> counts — if one competitor is an order of magnitude below the others, the filter is eating its content.
>
> **Caution when filtering by keyword (learned the hard way):** match drop/keep words against the URL
> **path** (the part after the domain), **not the whole URL** — or the brand name in the domain creates false
> matches. Example: a "keep anything with *test* in it" rule matched *every* page on `testgorilla.com` /
> `testdome.com`, so login/careers/locale junk never got dropped. Path-only matching fixes it.
>
> The per-competitor filtered lists are written to `_work/_candidates/[competitor]-candidates.csv` (so the
> filter is auditable); the filter+tag script lives in `_work/`.

---

# Step D — Tag each kept page by FORMAT (not topic)
> **Append this competitor's kept pages to the master sheet** `competitor-formats.csv`, writing the
> `Competitor | URL | Format | Domains | Backlinks` columns (one row per kept page). Step E fills the
> "What it is" column on the same rows.

Read the URL + title and assign one **format**. Starting catalog (extend freely):

**Universal formats:** answer-bait (what-is / how-it-works) · facts page · glossary / dictionary · rankings
/ tier list · quiz · calculator / estimator · generator · data-driven / original research (reports,
surveys) · interactive / animated infographic · marketer bait (case study / controversy) · jobs page ·
interview-questions listicle · templates · "best tools / X vs Y" comparison list · ultimate guide / pillar ·
checklist / cheat sheet.

**Company-specific formats** (emerge from what the company is): e.g. for an assessment company,
**free test / skill assessment**.

> **The extensibility rule:** if a page genuinely fits **no** existing format, **add a new named category**
> (name it + one-line definition) and use it. The catalog is a starting set, not a cage. Keep a running note
> of any new category so it's applied consistently across all 15 competitors.

---

# Step E — Read EVERY kept page in full, codify "what it is"
For **every kept page** (all of them, not a top slice), **scrape the entire page** and put that **full scraped
clean text — everything saved to `_work/`, as-is — into the "What it is" column** of the same
`competitor-formats.csv` row. **Don't summarise it, don't shorten it, don't reduce it to a description:** the
column holds the page's complete scraped content, verbatim. (Don't fall back to the meta description or the
title — that isn't the page.) This full content is exactly what Step G reads to find the gaps and the
*distinct angle*, so the more complete it is, the better.

> ⛔ **HARD RULES — this is the step that gets silently skipped. Do not.**
> 1. **Read all kept rows.** Not the top 80, not "the magnets" — every kept page. Reading the long tail is the
>    point; that's where under-served formats hide.
> 2. **A page that won't load is marked `FETCH FAILED`, never `(from title)`.** Title-as-description is
>    banned — it looks like data but isn't, and it hides the gap. A real failure must be *visible*.
> 3. **At the end, print a tally** and put it in the RUN-LOG: `N rows → X read, Y FETCH FAILED`. The run is
>    not "done" until X + Y = every kept row and Y is genuinely just the un-fetchable ones (blocked/404).

**How (efficient + durable):** fetch in bulk and **save each page's FULL clean text + status to `_work/` as you
go** — the entire page, **no character cap** (the vendored extractor already returns the whole article; don't
slice it). Resumable: a crash/compaction continues instead of refetching. Then put that saved full text into
the "What it is" column **as-is**, per row. Persist after each competitor so progress is never lost.

**Use a 3-step fetch ladder — many competitor sites are JS-heavy (learned the hard way: ~40% returned HTTP 200
but empty on the first pass):**
1. **Vendored extractor** (`workflows/00-foundation/scripts/voice-analyser/dist/utils/extractor.js` —
   `extractArticleContent`, same one the brand brain uses), ~15-20 URLs concurrently. Clean article text — it
   returns the **whole** article; save all of it (no truncation).
2. **Raw-HTML-strip fallback** for the ones that come back empty (JS-rendered sites like Next.js/React):
   pull `<title>` + the `h1/h2` headings + the **full** visible body text (keep all of it). When a page renders
   nearly empty, the **headings alone still capture "what it is" well** (a glossary's H2s, a listicle's
   questions, a test page's sections).
3. **WebFetch** for the last stragglers (it renders + summarises). Whatever still won't load → `FETCH FAILED`.

> Don't WebFetch all N pages one-by-one — that's thousands of calls. Bulk-fetch (steps 1-2) handles the vast
> majority cheaply; reserve WebFetch for the residue.

> **End of loop:** once B → E have run for all competitors, `competitor-formats.csv` is complete — every kept
> page tagged and **really** described (or flagged failed). Now leave the loop for Steps F → H.









# Step E output — what the master sheet looks like

Before Step G runs, here's what `competitor-formats.csv` looks like at the end of the B → E loop. One row per kept page across all 15 competitors, every row tagged by format, with the page's **full scraped text** saved in the "What it is" column (verbatim, not a summary).

| # | Competitor | URL | Format | Domains | Backlinks | What it is |


"What it is" holds the **entire scraped page** — the full clean text saved in `_work/`, put into the column verbatim (not a curated summary). Reading that complete content is how Step G later sees what the page actually contains (length, format, what's bundled), what's missing (no calculator, no live editor, no sample preview), and what's paywalled, and turns it into an angle. A row whose "What it is" is just the page title or a meta-description guess kills Step G silently — no angle is possible.

---

# Step F — Aggregate by format (across all 15)
From the finished `competitor-formats.csv`, aggregate **every row** by Format:

| Format | # pages | Total Domains | Avg Domains |
|---|---|---|---|
| Data report | … | … | … |
| Free test/assessment | … | … | … |
| … | | | |

Rank by **Total Domains** (then Avg). **Formats that recur across several competitors = highest confidence**
— if reports + free tests top the table for direct rivals *and* the adjacent content leaders, build those
first.

> **Step F writes its own file:** save this table to `_work/format-summary.csv` (`Format | # pages | Total
> Domains | Avg Domains`). It is *also* Tab 1 of the deliverable (Step H) — but it must exist as a standalone
> file too, so the aggregation is inspectable on its own and never lives only inside the xlsx.

---
# Step G — Turn every row into an idea (with proof)

## The unit of work

An "idea" is one asset we could build, defined by three things:

1. **Format** — the shape (glossary, free test, data report, calculator, listicle…) carried over from Step D.
2. **Our subject** — the specific subject we cover, which must sit inside the **brand scope** (G0, derived from the brand brain). Never a competitor's exact topic.
3. **Distinct angle** — what makes our version different/better, drawn from what's thin or missing in the backing pages (the "What it is" column from Step E).

A row produces an idea. Multiple rows that produce the same idea get merged, and the merged idea carries all their backlink evidence. **There is no target idea count.** A 1,500–2,500 row master sheet typically yields anywhere from 100 to 300+ ideas. The build-now / build-later split in G5 is what makes that list actionable.

## Three traps Step G is designed against

**Trap 1 — Too generic.** "Build a glossary because glossaries pull links." No topic, no angle, useless to a writer.

**Trap 2 — Too copying.** "Build a retention-bonus glossary because [Adjacent-A] has one." Head-to-head on their exact topic = we lose.

**Trap 3 — Fake analysis: output that looks like hundreds of ideas but is really one template filled in
hundreds of times.** This is the easiest trap to fall into and the hardest to spot, because the spreadsheet
*looks* full and busy. You can recognise it by three tells:

- **Glued-together asset names.** The `Asset` is just `Format + " on " + Topic` (e.g. "Glossary on hiring
  terms") instead of a real title for a thing you'd actually build.
- **Junk subjects.** The subject field holds scraps pulled from URLs or page titles — "stay ask", "speechx" —
  not real subjects.
- **Repeated angle gaps.** The `Angle gap` field reuses the same few sentences across hundreds of rows, so
  every "idea" has the same generic reason.

When all three show up, you don't have 400 ideas — you have ~8 templates copy-pasted 400 times.

**What stops it in this workflow:** (1) **G0's brand scope** gives the agents a real reference to reason
against (instead of inventing junk subjects); (2) **G2's per-page reasoning** makes each agent actually read
the page and write a specific asset + gap (instead of pattern-filling); (3) **G3's intelligent merge** reads
the real assets and groups them by judgment (instead of blindly matching strings).

### What a good idea looks like (passes all three traps)

> *"Build a **Hiring & Assessment Glossary with Bundled Micro-Tests.** 47 competitor glossary pages across 8
> competitors prove this format pulls links. Of those 47: 32 are definition-only with no template, 11 add a
> worked example but nothing interactive, and 4 include a template but no test. **Nobody bundles a test with
> the definition — that's our angle.**"*

Why it's good — it has the three things every real idea needs:

1. **A real asset name** — "Hiring & Assessment Glossary with Bundled Micro-Tests" (a thing you could open a
   doc and start building), not "Glossary on hiring terms".
2. **A subject we can own** — glossaries of hiring/assessment terms sit squarely inside Testlify's brand scope.
3. **An angle built from real evidence** — the "32 / 11 / 4" counts come from actually reading those 47 pages,
   so the gap (nobody bundles a test) is proven, not guessed.

---

## G0 — Distil the brand scope from the brand brain (do this once, before G1)

**What G0 produces:** a short `brand-scope.md` (at the competitor-study top, beside `competitors.md`), distilled from the [company] **brand brain** (and its
companion `stats.md` / `opinions.md` / `brand-assets.md` if present). It is the single shared reference that
every per-row reasoning agent in G2 reads, so 30 parallel agents stay pointed the same way. Sections:

1. **What we are / who we serve** — one short paragraph: the product, the buyer, the job they hire it for.
2. **Subjects we can credibly own** — a handful of *example* themes drawn from the brand brain, written only to
   point the agents in the right direction. **These are NOT hardcoded and NOT a checklist to obey.** They are
   illustrative, not exhaustive — if an agent reads a page and sees a strong on-brand subject that isn't listed
   here, it should use it. Treat this as "here's the kind of thing we own," never as "only these are allowed."
   (The moment this becomes a strict allow-list, we're back to the rigid-list problem we're avoiding.)
3. **Off-limits / not us** — *examples* of subjects clearly outside the company's world, again as directional
   signal, not a hard ban. The agent still judges each page; a listed "off-limits" cue is a strong hint to skip
   or transplant, not an automatic rule that overrides what the page actually is.
4. **Transplant note** — when a competitor wins links on an off-brand subject, **keep the winning format,
   point it at our world.** Record the original off-brand subject in Notes; never let it become our subject.

> **New subjects need no special handling.** Because agents *reason* against the scope (G2) rather than match
> a fixed list, a genuinely new ownable subject is simply used and noted in passing; G3's merge then
> reconciles near-duplicates by judgment.

### G0 is a gate
Write `brand-scope.md`, then **show it to the user and get approval before running G2.** This is the one place
a human sets direction; everything downstream is the agents reasoning against this approved anchor. (Keep it
short — a page. A bloated scope is as bad as a rigid list.)

---

## G1 — Set up the working sheet

Give every master row a stable **Row ID** (its line number is fine) — this is how the parallel agents' output
gets stitched back to the right row. Then add these empty columns to the right of the "What it is" column:

| Idea # | Asset | Brand fit | Angle gap | Distinct angle | Notes |

`Asset`, `Brand fit`, `Angle gap`, `Distinct angle`, `Notes` are all filled in **G2** (by the sub-agents — the
distinct angle is written there, not later). `Idea #` is filled in **G3** (after the intelligent merge).

---

## G2 — Per-row reasoning at scale (parallel sub-agents)

This is the main work and it is **large** — a master of 1,500–3,000 rows. Two ways NOT to do it: a keyword
script (that just recreates the pre-decided-buckets problem we left behind in G0), or one model alone (too
slow, and a single context **drifts** over thousands of rows — it'll name the same thing two different ways).
So run it as **parallel sub-agents**, each reasoning genuinely against the approved brand scope.

### Set up the run
- **Shard by format** (the Step D tag), so like pages travel together — this makes G3's merge cleaner.
- **Work in tiny batches — ~5 rows per reasoning pass. Never hand an agent a big block.** Given many rows at
  once, the model pattern-matches *across* the batch and goes generic (it stops reading each page and starts
  writing one description that "fits them all"). Five rows keeps its attention on each individual page, which
  is the whole point. This means **many small passes** (e.g. ~1,500 rows ≈ ~300 batches of 5) run across
  parallel agents — an agent can take a format-shard and walk it **5 rows at a time**, emitting output after
  each five, or one 5-row batch per agent. Either way, **no single prompt ever holds more than ~5 rows.**
- Use a **fast mid-tier model** (e.g. Sonnet) for these per-row passes; reserve the **strong model** (e.g.
  Opus) for the G3 merge.
- **Each pass receives:** (a) the approved `brand-scope.md`; (b) a fixed **naming convention + the good/bad
  asset & gap examples below** (the anti-template guardrail that keeps every pass writing the same way); (c)
  its **~5 rows with the full page text** (the "What it is" column saved in Step E — title + headings + full
  body) — never just the title.

### The sub-agent prompt — send this verbatim
**Everything from here to the output spec below *is* the prompt each agent receives** — not commentary about
the agents. Paste in the approved `brand-scope.md` and that agent's `~5 rows + page content` where shown, and
send the whole thing. (Keeping the prompt here, in the recipe, is the point: there's no gap between what the
recipe says and what the agent actually gets.) Lead with the frame:

> *You are [company] (here's the brand scope). Each row below is a page from a **competitor** that already
> earns backlinks — and it earns them because of its **format** (its shape: glossary, free test, data report,
> calculator…), not its exact topic. Your job, for each page: look at what they built and the proof it pulls
> links, then design the asset **we** would build — **the same winning format, but on a subject we can own
> (per the brand scope), and better than theirs.** Steal the shape, never the topic.*

### What each agent does, per row
1. **Read** the competitor page: its format tag and the Step E "What it is" (the full page text — its headings
   tell you what's actually on it). Resist leading with their title/brand framing — it leaks their angle into yours.
2. **Judge against the brand scope → set `Brand fit`:**
   - `CORE` — on-brand subject the company can own outright.
   - `TRANSPLANT` — off-brand subject but a link-pulling *format*: keep the format, point it at our world;
     record the original subject in Notes (e.g. `transplanted from: compensation`).
   - `ADJACENT` — same buyer, broader subject (best-of round-ups, industry trends).
   - `SKIP` — outside the company's world, or fetch-failed / junk. Leave the columns blank, Notes `SKIP — reason`.
3. **Write the `Angle gap` FIRST — what's thin/missing/paywalled/stale on this specific page.** This comes
   before the asset on purpose: **the gap is what the asset is built to beat.** Anti-template rule: *"Could I
   have written this gap without reading this row?"* If yes, rewrite. Cite a concrete fact — word count, what's
   on the page, what's missing, what's gated, a staleness date, a format limit.

   | ❌ Templated gap (banned) | ✅ Good gap (usable) |
   |---|---|
   | "generic explainer - no original data, no inline test" | "11 questions, MCQ only, no public sample, free PDF cert" |
   | "rival test page is a marketing landing - no public Qs" | "350-word definition, no template, no example screenshots" |
   | "thin editorial list - generic items" | "interactive but only 8 inputs, no industry benchmark" |
   | "round-up that rarely updates" | "2022 salary data, last refresh 14 months ago" |

   A genuinely strong page with no obvious gap → `strong — no obvious gap` (tells G4 to score Beatability harder).
4. **Write the `Asset` — the thing WE would build to beat that gap.** Take the page's winning **format**, apply
   it to a subject inside our brand scope (copy the shape, not their exact topic), **and bake in the fix for the
   gap you just wrote** — our version exists precisely to do what theirs doesn't. Name it as a **real working
   title a writer could open a doc with** — free text, **no forced key**. It is **not** "[Format] on [Topic]"
   glued together; the differentiator from the gap should be visible in the name:

   | Their gap (step 3) | ❌ Template fill | ✅ Real asset built from the gap |
   |---|---|---|
   | "350-word definition, no template, no micro-test" | "Glossary on hiring terms" | "Hiring & Assessment Glossary with Bundled Micro-Tests + Templates" |
   | "MCQ-only test, no public sample, cert paywalled" | "Free skills test on AI roles" | "Free AI & ML Skills Test (public sample Qs + free shareable cert)" |
   | "static 2022 PDF, summary paywalled" | "Data report on skills-based hiring" | "Annual Skills-Based Hiring Report (free, interactive, quarterly-refreshed)" |

   **Test:** does the asset name reflect the gap from step 3? If it could stand without ever having read the
   page, it's a template-fill — rewrite it.
5. **Write the `Distinct angle` — the third creative output, here on the same row.** You found the gap (step 3)
   and built the asset to beat it (step 4); now state in one line how OUR version is different/better than
   *this* page — the angle, drawn straight from the gap. **This IS the distinct angle for this row — nothing
   downstream re-writes it.** The merge (G3) just carries it to the idea; G4 only scores. It must cite the
   concrete gap — if it could be written without reading this page, rewrite.
   > e.g. gap "MCQ-only, no public sample, cert paywalled" → Distinct angle: *"adds a live editor, 5 sample Qs
   > visible pre-signup, and a free shareable cert — all three things this page withholds."*

So the G2 sub-agent does the **whole creative judgment in one place: gap → asset → distinct angle.** That's the point.

### Output format — the closing line of the prompt
End the prompt by demanding strict output: **one line per Row ID and nothing else** —
`Row ID | Brand fit | Angle gap | Asset | Distinct angle | Notes`. (That keeps every chunk machine-stitchable.)

— end of the verbatim prompt —

### Stitch & validate (the runner does this, after the agents return)
- Each agent writes its chunk to `_work/agent_out/` (resumable — a re-run skips chunks already done).
- A small script **stitches every chunk back into the master by Row ID.** Then **validate: every kept row came
  back exactly once.** Re-dispatch any agent that dropped rows or returned malformed lines — do not proceed to
  G3 with holes.
- **Do every kept row.** Yes, all of them. The long tail is where under-served formats hide.

---

## G3 — Merge by intelligent reading (one strong-model pass, no string keys)

After G2 every row has a freely-written `Asset`. **Do not merge by string-match or a normalised "asset key"** —
that re-imposes the exact pre-decided structure we removed in G0, and free-text assets won't string-match
anyway ("Python Skills Test" vs "Coding Assessment (Python)"). Instead, **let one strong model read all the
proposed assets at once and merge them by judgment.**

### Step 1. The merge read
Hand the **strong model** (e.g. Opus) the whole list of proposed assets, kept lean so it all fits one context:
**one compact line per row — `Row ID · Asset · Format · Competitor · Domains`.** (Leave the long angle-gaps
*out* of the merge input — they aren't needed to decide grouping, and dropping them keeps the full list
readable in one pass.)

Its task: **cluster the assets into the real distinct ideas, deciding the organising structure from the data
itself** — by underlying build / subject / however it naturally groups, *not* a pre-set list. For each cluster
it picks one clean canonical `Asset` name, a `Brand fit`, and a short `Our subject` label, then **assigns every
Row ID to a cluster.** Output: `Idea # · canonical Asset · Brand fit · Our subject · member Row IDs`.

> **No target number of ideas.** Do not restrict to "around N" clusters or force the list to hit a count — the
> right number is whatever the data actually contains (it could be 50, it could be 400). Let it emerge. But the
> **classification itself must be world-class**: precise grouping, genuinely distinct ideas kept separate,
> genuine duplicates merged, no lazy lumping and no needless splitting. The number is free; the quality is not.

> **Merge judgement:** when two assets are *similar but not the same*, ask "would ONE asset we build satisfy
> both?" Yes → one idea (use the cleaner name). No → split. When in doubt, **split** — a tight buildable idea
> beats a fuzzy one covering three things.

### Step 2. Fallback for very large runs (≈2,500+ assets)
If one pass strains (output too big, or clustering goes coarse), split the merge — still pure reasoning, no
keys: **(a)** the strong model first produces only the **canonical idea list** (~150–300 ideas, each with a
one-line definition); **(b)** a second pass (batched, can reuse the G2 sub-agents) **assigns each row to one of
those ideas.** "Decide the buckets" then "place the rows."

### Step 3. Build the idea list
Write `ideas.csv`, one row per Idea #, rolling up from its member master rows:

| Column | What it is |
|---|---|
| `Idea #` · `Asset` · `Brand fit` · `Our subject` | From the merge |
| `Distinct angle` | **Carried up from G2** — the clearest of the member rows' `Distinct angle` lines, selected here (never re-written). If an idea's members are all empty / `weak — recheck reads`, leave it blank and flag the idea (not buildable yet → LATER). |
| `Format` | The dominant format tag across backing rows |
| `# backing pages` / `# competitors` | Count of member rows / distinct competitors among them |
| `Total domains` / `Total backlinks` | Sums across member rows |
| `Backing URLs` | Every member URL — the proof; anyone can click through and verify |
| `Angle gaps` | **Every** member row's `Angle gap`, kept in full (not summarised), each tagged with the URL it came from — e.g. `[url-1] gap-1 ‖ [url-2] gap-2 ‖ …`. The evidence behind the carried angle. |

> **How every idea's angle gaps stay tracked (don't lose them).** The angle gaps are *not* used to merge — we
> merge on assets — so they're re-attached **after** the merge via the `Row ID → Idea #` link:
> 1. The **master sheet** is the authoritative store: every row keeps its own `Angle gap` **and** `URL`, and
>    G3 writes its `Idea #` onto that row. So for any idea you can **filter the master by `Idea #`** and see
>    every backing gap, each next to the exact page it came from. Nothing is dropped or blended away.
> 2. The `Angle gaps` cell in `ideas.csv` is the **convenience copy** — the same per-row gaps gathered into one
>    place (URL-tagged, all of them) so the scoring step (G4) and any reviewer can read them without re-joining. It must contain **all** member
>    gaps, not a picked few.
> Build it by the join: merge output gives the member Row IDs per idea → look each Row ID up in the master →
> collect its `Angle gap` + `URL`. That guarantees completeness and full traceability both ways.

### Step 4. Merge-quality check (this IS the deliverable quality)
Scan the merged list for **duplicate ideas** (two clusters that are really the same build) and **over-merges**
(one cluster lumping unrelated builds). Fix by re-running the merge on just the offending clusters. Drift from
G2 is expected; G3 is where it gets reconciled — if you skip this, you ship duplicate ideas.

---

## G4 — Score each idea: beatability and effort

(There is no separate "write the angle" step — G2 already wrote the distinct angle per row and G3 carried the
clearest one onto each idea. The only per-idea judgment left is **scoring.**)

Add two columns to each idea in `ideas.csv`. This rides naturally **inside the G3 merge** (the strong model
already has each cluster and its full gaps) or a light per-idea pass — one read, both scores.

### `Beatability` (1–3)

From the idea's `Angle gaps`:

- **3 — easy win.** Backing pages are thin, text-only, stale, paywalled, or single-format. Lots of gaps to exploit.
- **2 — winnable with one or two clear differentiators.** Backing pages are decent, the angle exploits a specific gap.
- **1 — hard.** Backing pages are strong, recent, well-resourced. Only winnable with a real moat (proprietary data, original tool, etc.).

### `Effort` (S/M/L)

- **S** — one page, days to a week. (One glossary entry, one calculator, one free test.)
- **M** — a small hub, weeks. (A glossary section with 30 entries, a test library on one topic.)
- **L** — original-data report, full hub, interactive product. A month or more.

---

## G5 — Rank and split into NOW vs LATER

Sort `ideas.csv` by, in this order:

1. **Brand fit** — CORE and TRANSPLANT first, ADJACENT below.
2. **Evidence × Beatability** — within tier, sort by (`Total domains` × `Beatability`) descending. This rewards ideas that have *both* link-proof AND are winnable.
3. **Effort** — tiebreaker, S before M before L.

Then add a `Build window` column with two values:

- **NOW** — top ideas the team can realistically ship this quarter. Pick based on team capacity, not list length. Could be 8 ideas, could be 30. The capacity-based cutoff is what makes this a plan instead of a menu.
- **LATER** — everything else. Not discarded — fully scored, in the backlog, ready to pull from when NOW slots free up.

---

## G6 — Sanity check before handoff

Before calling Step G done, spot-check the top ~20 ideas:

- ☐ **No too-generic names.** Every `Asset` contains a specific topic, not just a format. ❌ `Glossary` ✅ `Glossary on hiring & assessment terms`.
- ☐ **No too-copying ideas.** No idea's subject is a single competitor page's exact subject. If it is, the angle had better justify it.
- ☐ **Every NOW idea has a real angle** drawn from gaps, not a hand-wave.
- ☐ **Every NOW idea has ≥3 backing pages from ≥2 competitors.** Recurrence is the real link-pull signal. A 1-page idea with 1,500 domains might be a one-off; an 8-page idea across 5 competitors with 400 domains each is a near-certainty.
- ☐ **`Backing URLs` is populated** for every idea. Empty proof column = idea not grounded.
- ☐ **No template-fill Asset names.** Spot-check: do any Asset names read as literally `<Format> on <Topic>`? If yes, those ideas need their Asset rewritten as real working titles (see G2's good/bad table).
- ☐ **Angle gap diversity check.** Count distinct gap strings across the master. If fewer than ~1 distinct gap per 5 rows (i.e. heavy reuse), the gaps were templated — the G2 angles inherit the problem. Re-do gaps for any cluster where one string covers 10+ rows.
- ☐ **Brand-scope + merge-quality check.** Every idea sits inside the approved `brand-scope.md` (CORE / TRANSPLANT / ADJACENT) — none on an off-limits subject without a transplant justification. And the merged list has **no duplicate ideas** (same build under two names) and **no over-merges** (unrelated builds lumped together).

Tick all 8 boxes in `RUN-LOG-problems.md` before declaring G complete.

---

## Sample output — what `ideas.csv` looks like

| # | Build window | Brand fit | Asset | Format | Our subject | Distinct angle | Total domains | # comps | # pages | Beat. | Effort | Backing URLs |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | NOW | CORE | Free Python Skills Test (live editor + 5 public sample Qs + shareable cert) | Free test | Skills tests — technical & coding | 3 competitor tests are MCQ-only or paywall the cert; ours adds a live code editor, 5 sample Qs visible without signup, and a free shareable candidate cert | 1,050 | 3 | 3 | 3 | S | [Direct-A]/tests/python-online; [Direct-B]/python-skills-test; [Direct-C]/tests/python-developer |
| 2 | NOW | CORE | AI Literacy Skills Test for Non-Technical Hires (scenario-based + shareable badge) | Free test | Skills tests — AI & data-science roles | Competitor's only AI test is generic 12-question coding MCQ — ours uses 25 scenario-based Qs requiring no coding and produces an employer-shareable badge | 510 | 1 | 1 | 2 | S | [Direct-A]/tests/ai-skills-literacy |
| 3 | NOW | TRANSPLANT | Hiring & Assessment Glossary with Bundled Micro-Tests | Glossary | Assessment & hiring terminology (glossary) | 32 of 47 competitor glossary entries are definition-only with no template or example; ours bundles every term with a 3-question micro-test or downloadable template | 1,040 | 2 | 3 | 3 | M | [Adjacent-A]/glossary/retention-bonus; [Adjacent-A]/glossary/360-feedback; [Adjacent-B]/hr-terms/onboarding |
| 4 | NOW | TRANSPLANT | Annual Skills-Based Hiring Benchmark Report (free, interactive, quarterly-refreshed) | Data report | Recruitment metrics & analytics | Only competitor benchmark is paywalled summary + static 2022 PDF; ours publishes the full report free with quarterly-refreshed interactive dashboard and raw data download | 1,200 | 1 | 1 | 2 | L | [Adjacent-A]/reports/comp-benchmark-2024 |
| 5 | LATER | CORE | Python Interview Questions Hub with One-Click Self-Tests | Interview-questions listicle | Interview questions & answers | Competitor lists 50 Qs with answers but no way to self-assess; ours links each question to a 1-question micro-test for 30-second self-check | 180 | 1 | 1 | 2 | S | [Direct-A]/interview-questions/python |
| 6 | LATER | CORE | Cost-per-Hire Calculator with Industry Benchmarking | Calculator | Recruitment metrics & analytics | Competitor calculator has 8 inputs and no benchmark layer; ours adds anonymised customer averages so users see where they stand vs peers | 90 | 1 | 1 | 3 | S | [Adjacent-B]/tools/cost-per-hire-calc |
| … | … | … | … | … | … | … | … | … | … | … | … | … |


Read across one row and the whole logic is visible: **what we'd build, why it's ours, how it'll be different, the proof it'll pull links, when to build it.** That's what Step G is delivering.


---
# Step H — Build the two clean end-files

Produce exactly **two** files (don't ship the same data as both .csv and .xlsx):

**1. `competitor-study-ideas.xlsx` — the DELIVERABLE (decision file).** Two tabs:

- **Tab 1 — Format summary** (Step F): `Format | # pages | Total Domains | Avg Domains | # competitors`, ranked
  by Total Domains. This is the "which *shapes* earn links" view across all 15 competitors.

- **Tab 2 — Ideas** (Step G): one row per merged idea, sorted by **Build window** (NOW above LATER), then
  **Brand fit** (CORE → TRANSPLANT → ADJACENT), then by **Evidence × Beatability** descending, with **Effort**
  as tiebreaker. Columns:

  | # | Build window | Brand fit | Asset | Total domains | # comps | Beat. | Effort | Distinct angle |
|---|---|---|---|---|---|---|---|---|
| 1 | NOW | CORE | Free Python Skills Test (live editor + 5 public sample Qs + shareable cert) | 1,050 | 3 | 3 | S | 3 competitor tests MCQ-only or paywall cert; ours adds live editor + public sample Qs + free cert |
| 2 | NOW | TRANSPLANT | Hiring & Assessment Glossary with Bundled Micro-Tests | 4,565 | 7 | 3 | M | 32 of 47 glossary entries are definition-only; ours bundles each with a 3-Q micro-test |
| 3 | NOW | TRANSPLANT | Annual Skills-Based Hiring Benchmark Report | 1,200 | 1 | 2 | L | Competitor benchmark paywalled + static 2022 PDF; ours free + quarterly-refreshed dashboard |
| … | LATER | ADJACENT | Best-of Tools Round-up (refreshed quarterly, filterable by company size) | 380 | 2 | 1 | S | Competitor lists update yearly with no filters; ours quarterly + filterable by buyer size |



  Colour the rows by Brand fit: **CORE green**, **TRANSPLANT blue**, **ADJACENT amber**. The `Backing URLs`
  column carries every URL behind the idea — this is the inline proof, and it's why the deliverable stands
  alone without anyone needing to open the master sheet.

**2. `competitor-formats.xlsx` — the MASTER / evidence file.** One row per kept page across all 15
competitors. Columns:

  `Competitor | URL | Format | Domains | Backlinks | What it is | Asset | Brand fit | Angle gap | Distinct angle | Idea # | Notes`

  This is the long list **with** duplicates; Tab 2 is the same data collapsed by `Idea #`. The `Idea #` column
  links the two — filter the master by an idea number to see every page behind it. The `Angle gap` column is
  the raw material that produced Tab 2's `Distinct angle` — filter to an idea to see how the angle was built.

These two files are the competitor-study output the rest of the idea backlog (and the other methods of
generating link-bait ideas) builds on.

---

# How the output looks

**Tab 1 — format summary (excerpt, illustrative):**

| Format | # pages | Total Domains | Avg Domains | # competitors |
|---|---|---|---|---|
| Glossary / dictionary | 37 | 4,565 | 123 | 7 |
| Free test / assessment | 332 | 5,654 | 17 | 9 |
| Data report | 14 | 3,820 | 273 | 6 |

**Tab 2 — ideas (excerpt, illustrative):**

| # | Build window | Brand fit | Asset | Total domains | # comps | Beat. | Effort | Distinct angle |
|---|---|---|---|---|---|---|---|---|
| 1 | NOW | CORE | Free test on Python developer skills | 1,050 | 3 | 3 | S | Live editor + free cert + 5 sample Qs visible without signup |
| 2 | NOW | TRANSPLANT | Glossary on [our domain] terms | 4,565 | 7 | 3 | M | Each term bundled with a free 3-question micro-test (no competitor does this) |
| 3 | NOW | TRANSPLANT | Annual industry benchmark report | 1,200 | 1 | 2 | L | Free full report, no paywall + quarterly-refreshed interactive dashboard |
| … | LATER | ADJACENT | Best-tools round-up: [adjacent category] | 380 | 2 | 1 | S | Updated quarterly + filterable by buyer size |

(Numbers and asset names above are illustrative — your real run produces 100–300+ idea rows depending on the
master sheet size.)

---

# Gotchas

- **Format not topic** — every time. Copy the shape, change the subject. The TRANSPLANT tier in Tab 2 is
  built entirely on this principle; without it, the highest-link-pull formats in the niche get lost.
- **Keep free tools, drop commercial** — the test-library pages are link magnets, not noise.
- **Collapse locale duplicates** so one report doesn't get counted six times.
- **Save the whole page text** into "What it is" — never the meta, **never the title**. Title-as-content is
  banned: it looks like data but isn't. Read **all** kept pages, not just the high-domain "magnets" — the
  long tail is where under-served formats hide. If a page won't load, mark it `FETCH FAILED`, don't fake it.
- Some pages block scraping or 404 — skip and note them; don't let one failure stall the run.
- **Recurrence beats raw domains.** An idea backed by 8 pages from 5 competitors at 400 domains each is a
  stronger signal than a single 1,500-domain page — the latter could be a one-off, the former is a pattern.
  G6's sanity check enforces ≥3 backing pages from ≥2 competitors on every NOW idea for this reason.
- This is **one of three** idea sources (the others: Model Other Niches, Study Trends). Don't over-index on
  any single competitor — recurrence across the 15 is the real link-pull signal.