# Backlink Automation — a reusable machine for earning backlinks

A system that earns backlinks for any company. It's built as **recipes** (general, reusable processes)
that you *run* for a specific client to produce **dishes** (the actual results). Testlify is the first
client the machine was run for.

---

## Where to start

1. **`CLAUDE.md`** — the project brain. Read this first: what we're building, how the folders work, the core rules.
2. **`workflows/`** — the recipes (start with `01-asset-engine/`).
3. **`projects/testlify/`** — a worked example: the recipes actually run for a real company.

---

## The core idea (recipe vs. dish vs. reference)

| Folder | What it is | Reusable? |
|---|---|---|
| **`workflows/`** | The **recipes** — general, step-by-step processes written with placeholders (`[COMPANY]`, `[WEBSITE]`). | ✅ any company |
| **`projects/<client>/`** | The **dishes** — the real outputs of running a recipe (brand brain, content map, idea banks, campaigns). | ❌ client-specific |
| **`research/`** | The **reference shelf** — orchestrations, strategies, and sources the recipes are built *from*. | reference only |

---

## Folder map

```
Backlink gets Automated/
├── CLAUDE.md                     ← read first: project brain + progress log
├── README.md                     ← this file
├── workflows/                    ← THE RECIPES (general, reusable)
│   ├── 00-foundation/            ← sitemap/content-database pull, brand-brain, Semrush top-pages
│   │   └── scripts/              ← reddit scraper, content-database builder, brand-brain tools
│   ├── 01-asset-engine/          ← the asset engine
│   │   ├── idea-backlog/         ← Method 1 competitor-study · Method 2 model-other-niches · Method 3 study-trends
│   │   └── reuse-check.md        ← RAG + LLM reuse check (do we already own this asset?)
│   └── 02-content-engine.workflow.md
├── research/                     ← raw reference (orchestrations · strategies · sources)
└── projects/testlify/            ← worked example (the "dish")
    ├── brand-brain/              ← the company's voice/product/data/authority
    ├── content-database.*        ← catalogue of every existing page  (regenerated — see note)
    └── asset-engine/
        ├── competitor-study/     ← Method 1 outputs
        ├── model-other-niches/   ← Method 2 outputs
        ├── study-trends/         ← Method 3 outputs (Reddit-driven tensions → ideas)
        └── clubbed/              ← the three idea pools merged + reuse-checked → the review deliverable
```

---

## The asset-engine flow (the main pipeline)

1. **Foundation** (`workflows/00-foundation/`) — build the content database (every page the site has) and the brand brain.
2. **Idea backlog** (`workflows/01-asset-engine/idea-backlog/`) — three independent idea methods:
   - **Method 1 — Competitor study:** what already earns links in the niche.
   - **Method 2 — Model other niches:** proven link-bait *formats* from adjacent niches.
   - **Method 3 — Study trends:** Reddit-driven *tensions* turned into timely assets.
3. **Merge + reuse check** (`reuse-check.md`) — the three pools are merged into one `clubbed-ideas` file, then each idea is checked against existing content via **RAG (retrieve) → LLM judgment (verdict)**, plus a deterministic **topic catalogue** of every page we already own on that topic.
4. **Review** — the clubbed pool is shipped as a self-contained HTML viewer for human review.

The reuse check stores **links only** — page text is fetched on demand (looked up in the content database, or web-fetched live) when judging or building content.

---

## Note on excluded files

Large, derived, or regenerable artifacts are **git-ignored** (see `.gitignore`) to keep the repo lean:
- the embeddings index (`content-index/`), raw scrape dumps (`_raw/`), and `content-database.csv` (>100 MB) — all regenerable from the scripts in `workflows/00-foundation/scripts/`;
- `node_modules/`, backups (`*.bak`), OS files, and the GitHub-Pages publish clone (`_pages-repo/`).

Credentials are **never** in this repo — they live in a `chmod 600` file outside the project tree.
