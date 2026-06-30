# Schema Decision Guide

**Bottom line:** add schema **only** to earn Google rich results. Schema gives ~**zero** independent AI-citation lift — AI citations come from in-body stats, quotes, and outbound citations to named primary sources (see seo-aeo-geo-bar.md, lever 1). Do not over-invest in markup.

> **Corrections vs older house docs:** the older SOP told you to add FAQPage, HowTo, and Speakable schema and implied they help snippets / AI. Since Aug 2023 those produce **no rich results for general (non-gov/health/news) sites** (HowTo was fully removed). This file is corrected; trust it over the originals.

---

## Schema type table

| Type | Status | Use it? | Notes |
|---|---|---|---|
| **Article** | Supported, worth it | YES | Core type for every blog post. Author + publisher + dates. |
| **BreadcrumbList** | Supported, worth it | YES | Renders breadcrumb rich result; cheap, reliable. |
| **Organization** | Supported, worth it | YES | Site-level Testlify entity / knowledge-panel signal. |
| **Product** | Supported, worth it | If applicable | For product/feature pages with real product data. |
| **Review / AggregateRating** | Supported, worth it | If genuine | Only with real, policy-compliant reviews. |
| **Video** (VideoObject) | Supported, worth it | If page has video | Video rich result + Google video surfaces. |
| **FAQPage** | Deprecated for rich result | NO (markup) | No rich result for general sites since Aug 2023. Keep FAQ **accordion for UX only**. |
| **HowTo** | Removed | NO | Fully removed by Google (Aug 2023). Write numbered steps in body instead. |
| **Speakable** | No general rich result | NO | News-only / limited. Write a clean liftable answer instead. |
| **Dataset / others** | Niche | Rarely | Only for genuine datasets; not a general blog need. |

**AI-citation reality:** none of the above meaningfully moves AI citations. Schema is a Google-rich-result tool, full stop.

---

## Required JSON-LD templates

Add as a `wp:html` block at the **top** of post content. Author = the routed voice (Abhishek for leadership/vision/strategy; Yashika otherwise). Publisher = Testlify.

### Article

```html
<!-- wp:html -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "<Post title>",
  "description": "<Meta description>",
  "author": {
    "@type": "Person",
    "name": "<Yashika Khandelwal | Abhishek Shah>",
    "url": "<author profile URL>"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Testlify",
    "url": "https://testlify.com"
  },
  "datePublished": "<YYYY-MM-DD>",
  "dateModified": "<YYYY-MM-DD>"
}
</script>
<!-- /wp:html -->
```

- `datePublished` = original publish date (preserve on a refresh).
- `dateModified` = the refresh date — but only set it when the change is **substantive** (a cosmetic-only date bump is a hard stop; see wp-operations.md).

### BreadcrumbList

```html
<!-- wp:html -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://testlify.com/" },
    { "@type": "ListItem", "position": 2, "name": "Blog", "item": "https://testlify.com/blog/" },
    { "@type": "ListItem", "position": 3, "name": "<Post title>", "item": "<Post URL>" }
  ]
}
</script>
<!-- /wp:html -->
```

---

## FAQ accordion — kept for UX only

- Render FAQs via the Kadence accordion (5 panes / 5 Q&As). See wp-operations.md for the exact block markup.
- This is a **UX/structure** decision: scannable, on-brand, helps readers.
- Do **not** expect FAQPage schema to produce a rich result, snippet, or ranking lift on testlify.com.

---

## Validation

- Validate every page's markup with Google's **Rich Results Test** (`https://search.google.com/test/rich-results`).
- Confirm Article + BreadcrumbList parse with **no errors/warnings** before considering a deploy verified.
- If a type shows "no eligible rich results detected" for FAQPage/HowTo/Speakable, that is expected — do not chase it.
