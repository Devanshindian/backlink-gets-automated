# Content policy — the cross-cutting hard rules

The non-negotiables every piece of content obeys, whatever the job (write new / refresh / build a link asset).
The quality *standards* live in `seo-aeo-geo-bar.md` and its companions; this file holds the *policies* — the
hard rules about competitors, links, URLs, publishing pace, and credentials. Company-specific values (the
actual competitor list, the platform) live in `projects/[company]/`, never here.

## 1. Never cite or link a direct competitor
The principle is universal: never cite, link, or favorably position a **direct competitor** — not as a
source, not for a stat, not for "context". If the only source for a figure is a competitor, drop the figure
or find a neutral primary. Critique competitor approaches generically, never by name.
- **The actual competitor list is a per-company value** — keep it in `projects/[company]/brand-brain/`, not
  in this general policy.

## 2. Outbound link rel policy
- **Internal links → dofollow.**
- **Editorial citations → `rel="nofollow noopener"`.**
- **Paid / partner placements → `rel="sponsored"`.** Never ship a paid link as dofollow.
- More citations does not change the rel policy — an evidence link is still nofollow. (Source selection +
  anchor + density rules live in `source-authority.md`.)

## 3. URL / slug + 301 redirects (change is the exception)
A title change does NOT require a URL change; title and slug need not match. A slug that already ranks carries
link equity + crawl history, so changing it always risks a ranking dip even with a perfect 301.
- **Default: KEEP the slug.** Refresh the title, meta, and body; leave the URL alone. This is the right call
  for the large majority of refreshes.
- **Change ONLY if the slug is genuinely harmful:** a dated slug on evergreen content (`/...-2021/`), a real
  intent mismatch (slug promises X, page answers Y), misleading/gibberish, or the wrong primary keyword baked
  into the path. "The new title reads better" is NOT a reason.
- **A warranted change is equity-risky surgery:** it needs a 301 from old→new, every internal link updated to
  the new slug, and the old URL must never 404.
- **In autonomous/routine mode, do NOT auto-change a slug.** Keep it, and FLAG the recommended new slug + 301
  plan for a human to execute. URL changes at scale, unattended, can tank rankings — a human owns that call.

## 4. Scaled-content-abuse guardrails
Applies to every page touched.
- **Human value gate (per page):** every published/updated page must add net-new value a reader couldn't get
  elsewhere. If you can't name what improved, don't publish.
- **Substantive-change minimum:** a refresh must change meaningful content — new data, new sections, corrected
  claims, restructured answers.
- **Cosmetic-only = HARD STOP:** a date bump, typo fix, or image swap alone is NOT a refresh and must not ship
  as an "update".
- **Pace publishing over time:** never mass-deploy refreshed/new pages in a single burst; spread them.
- **Disclose AI use where non-obvious**, per the company's editorial policy.

## 5. Credentials
Never hardcode platform or API credentials into a recipe, standard, doc, ticket, or commit. Load them from the
company's secrets file at run time. Platform-specific deploy mechanics travel with `[PLATFORM]` in the recipe's
deploy step, not here.
