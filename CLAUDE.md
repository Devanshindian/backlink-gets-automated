# Backlink Automation — Project Brain & Progress

> Read this first every session. It says what we're building, how the folders work, and where we are.
> **Update the "Current status" + "Session log" at the end of every session.**

## What we're building (one image)

A reusable **machine** that earns backlinks. It's made of **recipes** (general, work for any company).
**Testlify is the first real client** we run the machine for. We build one recipe at a time.

## Core rule: recipe vs. dish

- **`workflows/`** = the **recipes**. General. Reusable for *any* company. Written with placeholders
  like [COMPANY] / [WEBSITE], never Testlify-specific data inside.
- **`projects/<client>/`** = the **dish**. The actual results produced by *running* a recipe
  (e.g. Testlify's brand brain, content map, campaign output).
- **`research/`** = the **raw reference shelf** (the 9 orchestrations + 32 strategies + sources). These
  are good *ideas and sequences*, NOT runnable step-by-step. Recipes are built *from* these; we link to
  them, we don't copy them.

## Folder map

```
Backlink gets Automated/
  CLAUDE.md          ← this file (project brain + progress)
  research/          ← raw reference (orchestrations, strategies, sources, tools)
  workflows/         ← RECIPES (general, reusable)
    00-foundation/   ← sitemap-pull, brand-brain, content-map recipes
    01-asset-engine.workflow.md
  projects/
    testlify/        ← Testlify's actual results
```
