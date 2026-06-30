/**
 * HTML to clean markdown extraction
 */
import * as cheerio from 'cheerio';
import TurndownService from 'turndown';
import { cleanArticleContent } from './cleaner.js';
const turndownService = new TurndownService({
    headingStyle: 'atx',
    codeBlockStyle: 'fenced',
    emDelimiter: '*',
    strongDelimiter: '**',
});
// Remove unwanted elements during conversion
turndownService.remove([
    'script',
    'style',
    'nav',
    'footer',
    'header',
    'aside',
    'iframe',
    'form',
    'button',
]);
export function extractArticleContent(html, url) {
    const $ = cheerio.load(html);
    // Remove unwanted elements
    $('script, style, nav, footer, header, aside, iframe, form, button, .comments, .sidebar, #comments').remove();
    // Remove shortcodes (WordPress pattern)
    $('[class*="shortcode"]').remove();
    // Try multiple article selectors
    const articleSelectors = [
        'article',
        '[role="main"]',
        '.post-content',
        '.entry-content',
        '.article-content',
        'main',
    ];
    let $article = null;
    for (const selector of articleSelectors) {
        $article = $(selector).first();
        if ($article.length > 0)
            break;
    }
    if (!$article || $article.length === 0) {
        // Fallback to body
        $article = $('body');
    }
    // Extract title
    let title = $('h1').first().text().trim();
    if (!title) {
        title = $('title').text().trim();
    }
    // Extract date
    const dateSelectors = [
        'time[datetime]',
        '.published',
        '.entry-date',
        '[property="article:published_time"]',
    ];
    let date;
    for (const selector of dateSelectors) {
        const $date = $(selector).first();
        if ($date.length > 0) {
            date = $date.attr('datetime') || $date.text().trim();
            break;
        }
    }
    // Get HTML content
    const htmlContent = $article.html() || '';
    // Convert to markdown
    const markdown = turndownService.turndown(htmlContent);
    // Clean up markdown with comprehensive artifact removal
    const { content: cleanedContent, report: cleaningReport } = cleanArticleContent(markdown);
    // Count words on cleaned content
    const wordCount = cleanedContent
        .split(/\s+/)
        .filter(word => word.length > 0).length;
    if (wordCount < 100) {
        return null; // Too short to be useful
    }
    return {
        title,
        url,
        date,
        wordCount,
        content: cleanedContent,
        cleaningReport,
    };
}
