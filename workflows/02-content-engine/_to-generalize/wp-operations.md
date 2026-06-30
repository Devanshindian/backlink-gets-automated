# Safe WordPress Operations + Deploy-to-Prod Runbook

Production WordPress at testlify.com. Treat every existing post as live and irreplaceable. Default to read; mutate only through the gated deploy path.

---

## Credentials — NEVER hardcoded

WP credentials load at **runtime** from `~/.testlify-wp-credentials`:

```
WP_USERNAME=...
WP_APP_PASSWORD=...
```

- Read those two lines at run time; build the Basic-auth header from them.
- **NEVER** write a plaintext password into any file, payload, log, prompt, or commit. If you find one in a source doc, do not copy it — reference this creds file instead.
- Base64 the `WP_USERNAME:WP_APP_PASSWORD` pair only in memory for the `Authorization` header.

---

## API endpoints

| Purpose | Endpoint |
|---|---|
| REST base | `https://testlify.com/wp-json/wp/v2/` |
| RankMath SEO meta | `https://testlify.com/wp-json/rankmath/v1/updateMeta` (POST) |

---

## Cloudflare bypass — required on EVERY request

Cloudflare returns **403 (code 1010)** without browser-like headers. Send all of these on every REST call:

```json
{
  "Authorization": "Basic <base64(WP_USERNAME:WP_APP_PASSWORD)>",
  "Content-Type": "application/json",
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
  "Accept": "application/json",
  "Origin": "https://testlify.com",
  "Referer": "https://testlify.com/wp-admin/",
  "Cache-Control": "no-cache"
}
```

For media uploads override `Content-Type` (`image/webp`, `application/pdf`) and add `Content-Disposition: attachment; filename="name.ext"`.

---

## Allowed vs forbidden REST operations

| ✓ Allowed | ✗ Forbidden |
|---|---|
| `POST /wp/v2/posts` status=**draft** (single call, all fields) | `status=publish` on a **new** draft |
| `POST rankmath/v1/updateMeta` (single call, all meta) | PATCH an existing post ID outside deploy-to-prod |
| `GET /wp/v2/posts/<id>` (use `?context=edit` for raw blocks) | Editing `content.raw` of an existing post directly |
| `GET /wp/v2/media`, `GET /wp/v2/search` | Changing slugs on existing posts |
| `POST /wp/v2/media` (WebP / PDF upload) | Swapping featured / body images |
| `DELETE /wp/v2/posts/<id>` (**only** status=draft AND own author) | Modifying another writer's posts |
| `PATCH /wp/v2/posts/<id>` **only** via deploy-to-prod with `DEPLOY_APPROVED=1` | Pushing with banned words / AI-signature chars / no approval |

**REST batching:** max 2 calls per push (content + meta). `Cache-Control: no-cache` always.

---

## Block rule — core Gutenberg only

Allowed blocks:
`core/paragraph`, `core/heading` (H2, H3), `core/list`, `core/quote`, `core/table`, `core/image` (existing media), `core/code`. NOT `core/separator` (horizontal dividers are banned - POLICIES.md #10; separate sections with headings + spacing).

**Never** use Kadence custom blocks in REST — **one exception**: the FAQ accordion.

### FAQ exception — Kadence accordion (FAQ sections only)

```
<!-- wp:kadence/accordion {"uniqueID":"_XXXX"} -->
<div class="wp-block-kadence-accordion alignnone">…</div>
<!-- /wp:kadence/accordion -->
```
- Each pane: `<!-- wp:kadence/pane {"id":"_paneN","title":"Question?"} -->`, answer as `<p class="wp-block-paragraph">Answer text.</p>`
- Always: `data-allow-multiple-open="false" data-start-open="0"`
- **5 panes per FAQ block** (matches the 5-Q&A standard); first pane active (`kt-accordion-panel-active`)
- Set `faqSchema:true` on the accordion. Note: this renders an FAQ accordion for UX. **CORRECTION:** FAQPage schema yields no rich result on a general site since Aug 2023 — keep it for structure/UX, do not claim ranking benefit. See schema-types.md.

### Table formatting
- Every `th`/`td` needs explicit `style="text-align:left"` (Gutenberg won't apply it).
- Headers: `style="text-align:left;font-weight:bold"`. Use `has-fixed-layout` on the table.

---

## Brand tokens

| Token | Value |
|---|---|
| Primary red | `#F23F44` (brand primary; dark `#A91E23`) |
| Text dark | `#1D2130` |
| Subtle background | `#F3F6F9` |
| Border gray | `#D6DBE2` |
| Font | Poppins |

- CTA group: background `#F3F6F9`, border `#D6DBE2`; button background `#F23F44`, text `#ffffff`.
- Callout boxes: `wp:group` background `#F3F6F9`. Separate H2 sections with headings + spacing only - NEVER `wp:separator`/`<hr>` (horizontal dividers are banned, POLICIES #10).

---

## Demo URL rule

- **CORRECT:** `https://hs.testlify.com/meetings/testlify/demo`
- **NEVER:** `https://testlify.com/request-demo/` (404, dead).
- **Verify every URL** before inserting: `curl -I` must return `200`. Skip any non-200; never guess URL patterns.

---

## Image preservation (critical before any content replace)

1. `GET …?context=edit` for current raw content.
2. Extract all existing `wp:image` blocks + their media IDs.
3. Re-insert those images at appropriate positions in rewritten content.
4. Never overwrite — full content replacement permanently loses uploaded media.

New images: WebP only (convert with Pillow, **not** macOS `sips`), content-descriptive alt + file name, `POST /wp/v2/media`, use `source_url` from the response.

---

## DEPLOY TO PROD (existing-post rework)

### Pre-gate — ALL must pass before any write

1. Weighted Overall score ≥80 (the canonical publish gate, founder D2026-06-18) + SERP benchmarks met + 2026 ranking bar present
2. **Substantive-change check:** the rework adds real value. A cosmetic-only change (date bump / typo / image swap) is a **HARD STOP** — abort, do not deploy.
3. Backup captured (30-day retention)
4. Pre-PATCH body MD5 hash captured
5. Zero banned words / zero AI-signature chars
6. Rate limit OK (**<5 deploys/hour**)
7. Stack-analysis pre-flight exists

### 10 steps

1. `GET` full post → save `backups/<id>-<ts>.json`; getHead → meta backup.
2. Hash current body → `pre_push_hash`.
3. **Autonomous publish gate (NO human `y`):** `verify_post.py` passes + weighted Overall ≥80. There is no per-post human approval in routine mode (founder D2026-06-18). If the gate fails, leave the post a draft and report - do not wait for input.
4. `PATCH /wp/v2/posts/<id>` with `Cache-Control: no-cache`, **status=publish kept**, **slug unchanged**, **author unchanged** (NEVER send the `author` field on a refresh - keep each existing post's current author; the company "Testlify Team" byline is for NEW content only, founder decision 2026-06-19).
5. `POST updateMeta` — all RankMath fields in one call.
6. Verify each field via re-fetch.
7. Recompute `post_push_hash`. Unexpected change → **halt + alert**.
8. Append `push-log/pushes.jsonl`, hash-chained (SHA-256 of prior entry).
9. Return: live URL + backup path + rollback command + 5-min cooldown warning.

### Rate limit & cooldown
- **Max 5 deploys / hour.**
- **5-minute cooldown** watch period after each deploy. Refuse additional deploys to the **same post** during cooldown.
- Pace deploys across the program over time (scaled-content guardrail) — don't burst.

### Rollback
`rollback <post_id>` → load latest backup → show diff → confirm → PATCH back → purge cache → log.

### Dry-run
Manual/ops use only. Prefix a push with `dry-run` to simulate everything except the REST PATCH/POST (prints payloads + backup path + log entry). The autonomous routine does NOT dry-run - it publishes directly once the score+verify gate passes.

---

## RankMath update payload

```json
{
  "objectID": <POST_ID>,
  "objectType": "post",
  "meta": {
    "rank_math_title": "<Focus Keyword>: <Angle> | Testlify",
    "rank_math_description": "<Problem w/ keyword in first 10 words>. <Solution>. <CTA>.",
    "rank_math_focus_keyword": "<primary keyword>",
    "rank_math_pillar_content": "on"
  }
}
```
- **VERIFIED CONTRACT (2026-06-16 live deploy):** fields go INSIDE a `meta` object with `rank_math_`-prefixed keys. The flat `{title, description, focusKeyword, isPillarContent}` shape returns HTTP 400 `rest_missing_callback_param: meta`. A 200 response looks like `{"slug":true,"schemas":[]}`.
- SEO title 50-60 chars (canonical, per seo-aeo-geo-bar.md), focus keyword in first 3 words. Meta description 140-160 chars, keyword present, end on an action word. (The render-gate accepts 40-65 / 120-165 as a looser guardrail; author to 50-60 / 140-160.)
- **RankMath needs a separate POST** — it does not update when post content updates.

---

## Common errors → fixes

| Error | Cause | Fix |
|---|---|---|
| 403 (Cloudflare 1010) | Missing browser headers | Add User-Agent / Accept / Origin / Referer |
| RankMath meta not updating | Separate API | Always POST to `rankmath/v1/updateMeta` after content |
| Images disappear after update | Full content replace | Extract + re-insert `wp:image` blocks first |
| `sips` can't write WebP | macOS sips unsupported | Use Pillow `img.save(buf, format="WebP", quality=85)` |
| Tables not left-aligned | Gutenberg default | Add `style="text-align:left"` to every th/td |
