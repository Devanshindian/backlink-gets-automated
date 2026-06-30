// Voice-analyser driver - generate the analyzer DATA for a company's brand brain.
//
// The analyzers are VENDORED (trimmed copy) right next to this file, in ./voice-analyser/.
// Build them once, ever (not per company):
//   cd workflows/00-foundation/scripts/voice-analyser && npm install && npm run build
//
// Then, from the project root, per company:
//   node workflows/00-foundation/scripts/voice-analyser-run.mjs <company>
//
// Corpus  = the URLs in projects/<company>/brand-brain/page-shortlist.md  (the Semrush top ~30 pages)
// Output  = projects/<company>/brand-brain/voice-data/*.json  (the 6 analyzer files)
import fs from 'fs/promises';
import path from 'path';

const SCRIPTS = import.meta.dirname;
const ROOT = path.resolve(SCRIPTS, '../../../..');
const company = process.argv[2];
if (!company) { console.error('usage: node voice-analyser-run.mjs <company>'); process.exit(1); }

const toolDist = path.join(SCRIPTS, 'voice-analyser/dist');
let extractArticleContent, analyzeCorpus;
try {
  ({ extractArticleContent } = await import(path.join(toolDist, 'utils/extractor.js')));
  ({ analyzeCorpus } = await import(path.join(toolDist, 'tools/analyze-corpus.js')));
} catch {
  console.error('Vendored analyzers not built. Build them once:\n' +
    '  cd workflows/00-foundation/scripts/voice-analyser && npm install && npm run build');
  process.exit(1);
}

const bb = path.join(ROOT, 'projects', company, 'brand-brain');
const shortlist = await fs.readFile(path.join(bb, 'page-shortlist.md'), 'utf-8');
const urls = [...new Set([...shortlist.matchAll(/https?:\/\/[^\s)]+/g)].map(m => m[0]))]
  .filter(u => !u.endsWith('.csv'));

const work = path.join(bb, 'voice-data', '_corpus');
const articlesDir = path.join(work, 'articles');
await fs.rm(path.join(bb, 'voice-data'), { recursive: true, force: true });
await fs.mkdir(articlesDir, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36';
let kept = 0, words = 0;
for (let i = 0; i < urls.length; i++) {
  try {
    const html = await (await fetch(urls[i], { headers: { 'User-Agent': UA } })).text();
    const art = extractArticleContent(html, urls[i]);
    if (!art) continue;
    const slug = (art.title || 'page').toLowerCase().replace(/[^a-z0-9]+/g, '-').slice(0, 50);
    await fs.writeFile(path.join(articlesDir, `${String(i + 1).padStart(3, '0')}-${slug}.md`),
      `---\ntitle: ${art.title}\nurl: ${art.url}\nword_count: ${art.wordCount}\n---\n\n${art.content}`, 'utf-8');
    kept++; words += art.wordCount;
  } catch (e) { console.error('  err', urls[i], e.message); }
  await new Promise(r => setTimeout(r, 200));
}
console.error(`corpus: ${kept} articles, ${words} words`);

await analyzeCorpus({ corpus_name: '_corpus', corpus_dir: path.join(bb, 'voice-data') });
// flatten: move the 6 JSONs up to voice-data/, drop the temp corpus
const analysisDir = path.join(work, 'analysis');
for (const f of await fs.readdir(analysisDir)) {
  await fs.rename(path.join(analysisDir, f), path.join(bb, 'voice-data', f));
}
await fs.rm(work, { recursive: true, force: true });
console.error(`done -> projects/${company}/brand-brain/voice-data/*.json`);
