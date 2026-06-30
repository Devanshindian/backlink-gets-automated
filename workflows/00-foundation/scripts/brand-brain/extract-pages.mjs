// Extract READABLE copies of a company's shortlisted pages - for Step 2 of the brand brain
// (reading the pages to sketch what the company is / who it talks to / positioning).
//
// Reuses the vendored page extractor (the same one the analyzers use) to strip each page's
// HTML chrome down to clean article text, then saves one markdown file per page so you can
// read clean prose instead of raw HTML. This does NOT analyze - it's just for reading.
// (The analyzer step, voice-analyser-run.mjs, fetches its own copy separately. Fetching twice
// is fine - both are one-time.)
//
// Build the vendored tool once first:
//   cd workflows/00-foundation/scripts/voice-analyser && npm install && npm run build
//
// Then, from the project root:
//   node workflows/00-foundation/scripts/extract-pages.mjs <company>
//
// Input  = projects/<company>/brand-brain/page-shortlist.md  (the 20-40 shortlisted URLs)
// Output = projects/<company>/brand-brain/pages/*.md         (clean, readable copies)
import fs from 'fs/promises';
import path from 'path';

const SCRIPTS = import.meta.dirname;
const ROOT = path.resolve(SCRIPTS, '../../../..');
const company = process.argv[2];
if (!company) { console.error('usage: node extract-pages.mjs <company>'); process.exit(1); }

let extractArticleContent;
try {
  ({ extractArticleContent } = await import(path.join(SCRIPTS, 'voice-analyser/dist/utils/extractor.js')));
} catch {
  console.error('Vendored analyzers not built. Build them once:\n' +
    '  cd workflows/00-foundation/scripts/voice-analyser && npm install && npm run build');
  process.exit(1);
}

const bb = path.join(ROOT, 'projects', company, 'brand-brain');
const shortlist = await fs.readFile(path.join(bb, 'page-shortlist.md'), 'utf-8');
const urls = [...new Set([...shortlist.matchAll(/https?:\/\/[^\s)]+/g)].map(m => m[0]))]
  .filter(u => !u.endsWith('.csv'));

const pagesDir = path.join(bb, 'pages');
await fs.rm(pagesDir, { recursive: true, force: true });
await fs.mkdir(pagesDir, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36';
let kept = 0, thin = [];
for (let i = 0; i < urls.length; i++) {
  try {
    const html = await (await fetch(urls[i], { headers: { 'User-Agent': UA } })).text();
    const art = extractArticleContent(html, urls[i]);
    if (!art) { thin.push(urls[i]); continue; }
    const slug = (art.title || 'page').toLowerCase().replace(/[^a-z0-9]+/g, '-').slice(0, 50);
    await fs.writeFile(path.join(pagesDir, `${String(i + 1).padStart(3, '0')}-${slug}.md`),
      `---\ntitle: ${art.title}\nurl: ${art.url}\nword_count: ${art.wordCount}\n---\n\n${art.content}`, 'utf-8');
    kept++;
    if (art.wordCount < 120) thin.push(urls[i]);   // likely a homepage/pricing/landing page - read it live too
  } catch (e) { console.error('  err', urls[i], e.message); }
  await new Promise(r => setTimeout(r, 250));
}
console.error(`read ${kept}/${urls.length} pages -> projects/${company}/brand-brain/pages/*.md`);
if (thin.length) {
  console.error(`\nThin or skipped (extractor is article-tuned - open these live too):\n  ` + thin.join('\n  '));
}
