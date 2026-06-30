# Canonical FAQ format - Kadence accordion (house standard)

Every Testlify FAQ ships as a **Kadence accordion**, not core heading+paragraph blocks. Collapsible panes are the better UX and match the rest of the site. Reference implementation: post 293423 (/how-to-ensure-language-fairness-in-assessments/).

**Do not hand-write this markup.** Generate it with `scripts/faq_accordion.py` so the byte structure stays identical to the reference. Hand-rolled Kadence markup breaks the block editor.

```
python3 scripts/faq_accordion.py --post-id <ID> --qa qa.json > faq_block.html
# qa.json = [{"q": "Question?", "a": "Answer (may contain inline <a>/<strong>)."}, ...]
```

Or import: `from faq_accordion import build_accordion; build_accordion(post_id, [(q, a), ...])`.

## Locked properties (matched to the reference)

| Property | Value |
|---|---|
| Block | `wp:kadence/accordion` + `wp:kadence/pane` (one pane per Q) |
| `faqSchema` | `true` (kept for structure/UX; note FAQ rich results are dead for general sites, so expect no rich result, just clean markup) |
| Open behaviour | single-open: `data-allow-multiple-open="false"`, `data-start-open="0"` (first pane open, `kt-active-pane-0`) |
| Icon | `arrow`, right side (`kt-accodion-icon-style-arrow kt-accodion-icon-side-right`) |
| Title align | left (`kt-pane-header-alignment-left`), question wrapped in `<strong>` |
| Active border accent | `#0e9cd1` left border on the open pane |
| Pane count | 5 for most posts (house rubric); the reference uses 10 for a pillar |

## Structure (what the generator emits)

- Accordion wrapper carries the full style JSON (content bg, title styles, borders) verbatim from the reference, with only `uniqueID` and `paneCount` substituted.
- Wrapper div: `kt-accordion-wrap kt-accordion-id<UID> kt-accordion-has-<N>-panes kt-active-pane-0 ...`.
- Pane 1 attrs: `{"uniqueID":"<UID>"}` (no `id` key). Panes 2..N: `{"id":<n>,"uniqueID":"<UID>"}`.
- Each pane: header button with `<strong>Question</strong>` + a `wp:paragraph` answer inside `kt-accordion-panel-inner`.
- Unique IDs are derived deterministically from the post ID, so re-running is stable.

## Rule

Use this for the FAQ section in BOTH `testlify-content-refresh` (refreshing a page) and `testlify-content-write` (new posts). Never substitute core h3+paragraph for the FAQ unless the Kadence plugin is unavailable on the target install.
