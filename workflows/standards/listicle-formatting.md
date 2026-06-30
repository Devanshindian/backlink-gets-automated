# Product & tool-list formatting (listicles, comparisons, "best X", "alternatives")

How to structure any list-based article: "Best [Category] Tools", "Top [Category] Platforms", "Best [Category] Software", "Alternatives to [Product]", etc.

## Competitor reconciliation (read FIRST - governs WHICH tools appear)

Formatting below applies to every list article. WHICH tools you list is still governed by the no-competitor policy:

- **NEVER auto-list or recommend a direct competitor as an H2 section** (competitor list and policy owned by `workflows/standards/content-policy.md`). Don't give a rival product its own promoted section on our site.
- **Adjacent, non-competing tools are fine** to feature - tools in neighbouring categories that don't overlap [COMPANY]'s core offering can be listed normally.
- **Competitor-comparison and "alternatives to [competitor]" pages that name rivals are a deliberate human/legal/brand decision, NOT an autonomous one.** In autonomous/routine mode, if the post requires naming direct competitors as recommended tools, do NOT expand or invent that coverage - FLAG it in the review ticket for a human and refresh only the non-competitor parts.
- [COMPANY] itself, when featured, gets the same H2 treatment as any tool (no over-claiming - honest scope).

## The one hard rule: tool names are HEADINGS, never bold text

Never introduce a product/tool/platform/software/framework/vendor using only bold text or a bold lead-in inside a bullet.

WRONG: `**ToolName**` then a paragraph. WRONG: `- **ToolName** provides...`
RIGHT: `## ToolName` (or `### ToolName`) then the paragraph.

Every software, platform, product, tool, integration, framework, methodology, or vendor mentioned as a **primary recommendation** MUST have its own H2 section.

## Recommended structure for a "Best X Tools" article

1. `#` Title
2. Introduction (answer-first, matches intent - see `workflows/standards/seo-aeo-geo-bar.md`)
3. `## How we evaluated these tools` (evaluation criteria)
4. `## Quick comparison table` (all tools, scannable, side-by-side)
5. `## 1. <Tool>` ... one H2 per tool, numbered, each with:
   - `### Key features`
   - `### Pros`
   - `### Cons`
   - `### Best for`
   - `### Pricing`
   - (`### Integrations` / `### Use cases` where relevant)
6. `## FAQ` (5 Q&As)
7. `## Final thoughts` - a forward-looking next step + ONE CTA (relevant [COMPANY] product + clear action), NOT an "In conclusion" recap.

## Heading hierarchy

- **H2 for:** individual tools/products, major software categories, alternatives sections, comparison sections, buying guides, evaluation criteria.
- **H3 for:** Key Features, Pros, Cons, Pricing, Integrations, Use Cases, Benefits, Limitations, Best For.
- **Never skip levels.** H1 -> H2 -> H3. Never H1 -> H3.

## SEO / AEO requirements per tool

Every listed tool must:
- Have its own H2 heading.
- Have 150-300 words of unique content (not boilerplate).
- Include semantic keywords naturally (no stuffing).
- Be independently understandable if an AI Overview / answer engine extracts just that section.
- Be reachable via a table-of-contents anchor link.

The tool name should appear: in the H2 heading, within the first paragraph of its section, and in a subheading where relevant.

## Comparison/list articles with 3+ tools MUST include

1. Introduction
2. Evaluation criteria (`## How we evaluated`)
3. Comparison table
4. A dedicated H2 section per tool
5. Conclusion (forward CTA, not a recap)

Never present recommended tools as a plain bullet list with one-line descriptions.

## UX test (if it fails, the formatting is wrong)

A reader can scan quickly, jump directly to any tool, compare side-by-side, and understand each tool without reading the whole article. **If a tool cannot be found from the table of contents, the formatting is incorrect.**

## No horizontal dividers between tools/sections

Do NOT separate tool sections (or FAQs, or pros/cons) with `<hr>`, markdown `---`, or any separator block. The H2 per tool already creates the visual break. Heading hierarchy + spacing is the separator. (Full rule in `workflows/standards/seo-aeo-geo-bar.md`.)

## Element-parity note

These tool-H2s, the comparison table, and per-tool H3s are structural elements: on a refresh of an existing listicle, do not silently drop a tool section or the comparison table. Keep or improve; state any intentional removal.
