# voice-analyser (vendored, trimmed)

This is a **trimmed copy** of [`houtini-ai/voice-analyser-mcp`](https://github.com/houtini-ai/voice-analyser-mcp)
(Apache-2.0, © Houtini, version 2.1.1 at time of vendoring). We keep only the parts we run:

- `src/analyzers/` — the **six analyzers** (the heart of it):
  `phrase-extraction`, `voice-markers`, `punctuation`, `vocabulary-tiers`,
  `vulnerability-patterns`, `specificity-patterns`.
- `src/utils/extractor.ts` + `src/utils/cleaner.ts` — turn a fetched HTML page into clean article text.
- `src/tools/analyze-corpus.ts` — runs all six analyzers over a folder of articles and writes the 6 JSON files.

**What we dropped:** the MCP server, the sitemap crawler, and `generate-voice-skill.ts` (the auto-`SKILL.md`
generator). We don't auto-generate a skill — its orchestration *ideas* are folded into our brand-brain
workflow by hand instead (see `../../brand-brain.workflow.md`, Step 4). Dropping the MCP server cuts the
runtime dependencies from 11 to 3 (`cheerio`, `compromise`, `turndown`).

## One-time setup (run once, ever — not per company)
```
cd workflows/00-foundation/scripts/brand-brain/voice-analyser
npm install
npm run build
```
This produces `dist/`, which `../voice-analyser-run.mjs` imports.

## Running it (per company)
From the project root:
```
node workflows/00-foundation/scripts/brand-brain/voice-analyser-run.mjs <company>
```
It reads the page URLs from `projects/<company>/brand-brain/page-shortlist.md`, fetches each page,
builds a corpus, runs the six analyzers, and writes
`projects/<company>/brand-brain/voice-data/*.json`.
