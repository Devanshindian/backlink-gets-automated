// Step E — fetch + read EVERY kept page in full. Ladder per spec:
//  (1) vendored extractor (cheerio→clean markdown), (2) raw-HTML-strip (title+h1/h2/h3+body).
//  Whatever still won't load → status 'empty' (residue for WebFetch) or 'failed'.
// Resumable: writes _work/fetch/<RowID>.json as it goes; re-run skips done rows.
import fs from 'fs/promises';
import path from 'path';
import { createRequire } from 'module';

const VA = "/Users/devanshasawa/Desktop/SEO by Devansh/Backlink gets Automated/workflows/00-foundation/scripts/brand-brain/voice-analyser";
const require = createRequire(path.join(VA, "package.json"));
const cheerio = require("cheerio");
const { extractArticleContent } = await import(path.join(VA, "dist/utils/extractor.js"));

const HERE = import.meta.dirname;
const MASTER = path.join(HERE, "..", "competitor-formats.csv");
const FETCH = path.join(HERE, "fetch");
await fs.mkdir(FETCH, { recursive: true });

const CONC = 16;
const TIMEOUT = 25000;
const UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36";

// --- minimal CSV parse (handles quoted fields) ---
function parseCSV(txt) {
  const rows = []; let i = 0, field = "", row = [], q = false;
  while (i < txt.length) {
    const c = txt[i];
    if (q) {
      if (c === '"') { if (txt[i+1] === '"') { field += '"'; i++; } else q = false; }
      else field += c;
    } else {
      if (c === '"') q = true;
      else if (c === ",") { row.push(field); field = ""; }
      else if (c === "\n") { row.push(field); rows.push(row); row = []; field = ""; }
      else if (c === "\r") {}
      else field += c;
    }
    i++;
  }
  if (field.length || row.length) { row.push(field); rows.push(row); }
  return rows;
}

const raw = await fs.readFile(MASTER, "utf-8");
const rows = parseCSV(raw);
const hdr = rows[0];
const idx = Object.fromEntries(hdr.map((h, i) => [h, i]));
const records = rows.slice(1).filter(r => r.length > 1).map(r => ({
  RowID: r[idx.RowID], URL: r[idx.URL], Title: r[idx.Title] || "",
}));

function stripText($) {
  $("script, style, nav, footer, header, aside, iframe, form, button, noscript, svg").remove();
  const title = ($("title").first().text() || "").trim();
  const heads = [];
  $("h1, h2, h3").each((_, el) => { const t = $(el).text().trim(); if (t) heads.push(t); });
  const body = ($("main").text() || $("body").text() || "").replace(/\s+/g, " ").trim();
  return { title, text: [title, heads.join(" · "), body].filter(Boolean).join("\n\n") };
}

async function fetchOne(rec) {
  const out = path.join(FETCH, rec.RowID + ".json");
  try { const ex = JSON.parse(await fs.readFile(out, "utf-8")); if (ex.status === "ok") return ex.status; } catch {}
  let res;
  try {
    const ctl = new AbortController();
    const tm = setTimeout(() => ctl.abort(), TIMEOUT);
    res = await fetch(rec.URL, { redirect: "follow", signal: ctl.signal,
      headers: { "User-Agent": UA, "Accept": "text/html,application/xhtml+xml" } });
    clearTimeout(tm);
  } catch (e) {
    const rec2 = { rowid: rec.RowID, url: rec.URL, status: "failed", method: "fetch-error", error: String(e).slice(0,200), text: "" };
    await fs.writeFile(out, JSON.stringify(rec2)); return "failed";
  }
  let html = "";
  try { html = await res.text(); } catch (e) {}
  let result = { rowid: rec.RowID, url: rec.URL, http: res.status };
  // (1) extractor
  try {
    const art = extractArticleContent(html, rec.URL);
    if (art && art.content && art.content.replace(/\s+/g,"").length > 200) {
      result = { ...result, status: "ok", method: "extractor", title: art.title, wordCount: art.wordCount, text: art.content };
      await fs.writeFile(out, JSON.stringify(result)); return "ok";
    }
  } catch {}
  // (2) html-strip
  try {
    const $ = cheerio.load(html);
    const s = stripText($);
    if (s.text && s.text.replace(/\s+/g,"").length > 150) {
      result = { ...result, status: "ok", method: "htmlstrip", title: s.title, text: s.text };
      await fs.writeFile(out, JSON.stringify(result)); return "ok";
    }
  } catch {}
  // (3) residue for WebFetch
  result = { ...result, status: "empty", method: "none", title: rec.Title, text: "" };
  await fs.writeFile(out, JSON.stringify(result)); return "empty";
}

let done = 0, ok = 0, empty = 0, failed = 0;
const queue = [...records];
async function worker() {
  while (queue.length) {
    const rec = queue.shift();
    const st = await fetchOne(rec);
    done++; if (st === "ok") ok++; else if (st === "empty") empty++; else failed++;
    if (done % 100 === 0) console.log(`  ${done}/${records.length}  ok=${ok} empty=${empty} failed=${failed}`);
  }
}
console.log(`Step E: fetching ${records.length} pages (conc ${CONC})...`);
await Promise.all(Array.from({ length: CONC }, worker));
console.log(`\nDONE: ${done} rows → ok=${ok}, empty=${empty}, failed=${failed}`);
