---
type: workflow-recipe
stage: foundation
reusable: any company
inputs: [WEBSITE domain, Semrush login]
last_updated: 2026-06-22
---

# Recipe — Semrush Top Pages (a site's pages ranked by traffic)

> **Manual method - assumes no Semrush API access** (most plans have none, so you export by hand).
> With an API key you'd pull this automatically instead.

## What this does
Find the pages that already get the most Google traffic - the proven winners.

## What you get (the output)
A CSV at **`projects/[company]/semrush-top-pages.csv`** - the site's pages ranked by organic traffic
(each row: URL, estimated monthly traffic, number of keywords, top keyword, search intent).

It's used **twice**:
- it **fills the Traffic / Keywords / Intent columns** in the content database, and
- it **tells the brand brain which pages to study** (the top pages are the winners worth learning the voice from).

## When to run it
After the content database (Step 1), before the brand brain (Step 3).

## Inputs you need
- `[WEBSITE]` - the company's domain.
- A **Semrush login**.

## Steps the user does (give these to them - the agent can't log into Semrush)
Walk the user through these in Semrush and wait for the exported file:
1. Log into Semrush.
2. Left menu -> **Top Pages** (under "Competitive Analysis"). *(Older menus: Organic Research -> the "Pages" tab.)*
3. Enter `[WEBSITE]`; if asked for a country, pick the company's **main market** (often US).
4. Sort by **Traffic** (highest first).
5. **Export -> CSV** - this downloads the file (usually to the `Downloads` folder).
6. **Move the downloaded file into the company's folder and rename it** to
   **`projects/[company]/semrush-top-pages.csv`** - the same `projects/[company]/` folder that was created
   in the content-database step. (Save it as a file there - don't paste the contents into the chat.)

## Then the agent does this
7. **Fill the content database:** match the CSV to `content-database.csv` by URL to fill its empty
   **Traffic / Keywords / Intent** columns. (`build_content_database.py` does this join when given the CSV.)

## Gotchas
- Semrush traffic is an **estimate** (Google Search Console is exact, but that usually needs verified-owner
  access we don't have). For "which pages win," the estimate is plenty.
