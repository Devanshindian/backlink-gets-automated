# Backlink Knowledge Base

A research base on **how backlinking is best done**, synthesized from many subject experts
(e.g. Nathan Gotch). Sources are ingested one at a time — video transcripts and/or attached
documents (Excel, Word, PDF, slides). The goal is a clean, de-duplicated, fully-attributed set of
end-to-end strategy playbooks that will later inform a backlink **automation tool**.

> Automation is intentionally deferred. For now we just accumulate best practices. Each strategy
> still carries an `automatable` flag and an "Automation hooks" section to give the future tool a
> head start.

## How it's organized

```
backlink-knowledge-base/
├── README.md            # this file
├── INDEX.md             # scannable map of every strategy, source, and tool
├── _templates/          # source + strategy templates (copy when ingesting)
├── sources/             # one file per ingested source — the provenance ledger
├── raw/                 # original attachments (xlsx/docx/pdf), named by source id
├── strategies/          # one file per strategy, end-to-end — the synthesized output
│   └── _categories.md   # controlled vocabulary for the `category:` field
├── tools/tools.md       # catalog of every tool mentioned
└── glossary.md          # SEO / backlink terms
```

**Two layers:** `sources/` preserves *who said what* (audit trail). `strategies/` is the
*de-duplicated synthesis* — the actual deliverable. Everything in a strategy traces back to one or
more source ids.

## Ingestion workflow (run on every new resource)

When a transcript is pasted, or a file (Excel/Word/PDF) is shared:

0. **If it's a file**, save the original into `raw/NNNN-<expert>-<topic>.<ext>` and set the source's
   `source_type` + `raw_file`. Extract the meaningful content — for spreadsheets, the rows/columns
   (checklists, prospect lists, metrics); for docs, the strategies/processes described.
1. **Create the source file** `sources/NNNN-<expert>-<topic>.md` from `_templates/source.template.md`;
   fill metadata, summary, and raw notes. (NNNN = next zero-padded number.)
2. **For each strategy in the source:**
   - If `strategies/<slug>.md` exists → **enrich** it: merge new steps/tools, append the source id to
     `sources:`, and if it contradicts existing content, add to the **Conflicting views** section
     (attributed to each expert). Bump `last_updated`.
   - If not → create it from `_templates/strategy.template.md`, picking a `category` from
     `strategies/_categories.md`.
3. **Update `tools/tools.md`** with any new tools (or append the source to an existing entry).
4. **Add new terms** to `glossary.md`.
5. **Update `INDEX.md`** (strategies, sources, tools rows).
6. **Report back:** what was created vs. enriched, and any conflicts detected.

## Writing style (applies to every strategy & source file)
Write so that someone **new to SEO** can follow it — assume little prior knowledge.
- **Explain, don't just state.** After a claim, add a short *why* in plain words.
- **Expand jargon on first use** and add a one-line plain-English meaning, e.g.
  "referring domains (the number of *different* websites linking to you)". Link the term to
  `glossary.md` where useful.
- **Use a quick analogy** where a concept is abstract (e.g. the reverse silo = "water flowing
  downhill from your popular pages into your sales pages").
- **Prefer short sentences and concrete examples** over dense SEO shorthand.
- Keep it accurate — explaining more simply must not change the meaning of what the expert said.

## Conventions
- Source IDs are zero-padded sequential: `0001`, `0002`, …
- Strategy `slug`s are kebab-case and stable (used as cross-reference anchors).
- `category` values must come from `strategies/_categories.md`.
- Cross-link with `[[path]]` wikilinks (Obsidian-compatible).
- Frontmatter stays machine-parseable — that's what the automation tool will consume.
