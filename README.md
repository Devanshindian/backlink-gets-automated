# Backlink Machine

A system that earns backlinks for a company.

The problem it solves: a company wants other sites to link to it, because search engines still
treat a link as a vote. Buying links is risky and asking for them does not scale. The only
durable answer is publishing things good enough that people choose to link to them.

So the machine does that, end to end.

---

## The five stages

It is a **factory line with numbered stations**, not one clever model. Each station is a folder,
numbered by its position in the line. Each has one command you run, and it writes named files to
disk. The next station reads those files by name. Nothing is passed in memory.

| Stage | What it does |
|---|---|
| **00 Foundation** | Catalogues every page the company already has, and what each one ranks for |
| **01 Brand context** | Learns how the company writes and what it actually sells |
| **02 Asset engine** | Finds ideas worth building. Three independent methods, merged and deduplicated |
| **03 Content machine** | Turns one chosen idea into a write-ready evidence bundle |
| **04 Write phase** | Plans, designs and writes the article, then checks it a dozen ways |

Stages 00 to 02 run **once per company**. Stages 03 and 04 run **once per article**.

---

## The three rules it is built on

**Code counts, AI judges.** If a thing can be counted, a script counts it. If two sensible
people could disagree, the model decides. Nothing arguable goes to a script, and nothing
countable goes to a model.

**Nothing is invented.** Every fact carries an ID, a word-for-word quote and a live URL. A
separate step whose only job is checking opens that URL and confirms the number is really on the
page. It is the most expensive step in the system, and the right place for the budget.

**Every step writes a named file.** So a crash resumes where it stopped, every number in the
finished article traces back to the step that produced it, and you can open the state anywhere.

---

## The guard pattern

The same shape repeats everywhere an AI touches the text:

```
code measures  →  AI edits  →  code checks what actually changed  →  any failure, the original ships
```

An automated edit can fail to improve something. It can never damage it.

---

## Where to start

1. **`README.md`** — you are here
2. **`CLAUDE.md`** — the conventions every engine obeys
3. **`workflows/`** — the reusable recipes, company-agnostic
4. **`projects/testlify/`** — a worked example, the recipes run for a real company

---

## What is proven, and what is not

**Proven.** It runs end to end. Articles have been through it. The catalogue and cost figures
are measured, not estimated.

**Not proven.** Whether the articles earn links. None have been live long enough to say.

**Partly proven.** Reusability. The brand-context layer ran end to end on a second company. The
full pipeline has only ever run on one.

---

*This repository is a snapshot of the reusable recipes and one worked example. The live system
continues in a private repo.*
