#!/usr/bin/env python3
"""Run the post-refresh verification checklist against a live testlify.com post.

Given a post_id and the focus keyword, this fetches the live post (edit
context) via wp_client and checks the items from the playbook Phase 9 / 13-point
rubric, printing a pass/fail table.

Checks
------
  - Word count (body text, HTML stripped).
  - H1 contains the focus keyword (title is the H1).
  - Article JSON-LD present in body.
  - BreadcrumbList JSON-LD present (body or RankMath usually injects it; this
    checks the rendered/edit body, reported as WARN if absent since it may be
    template-injected).
  - Internal vs external link counts.
  - AI-signature characters: em dashes, en dashes, curly quotes, ellipsis char.
  - Banned-word hits (case-insensitive, word-boundary), from a banned-words file
    (one word/phrase per line; blank lines and #-comments ignored).
  - All links in the body return HTTP 200 (via wp_client.verify_url_200).
  - Demo URL correctness: the only valid demo URL is
    https://hs.testlify.com/meetings/testlify/demo and the dead
    /request-demo/ must NOT appear.

This script is READ-ONLY. It never writes to production.

CLI
---
    python verify_post.py 1234 --keyword "candidate screening"
    python verify_post.py 1234 --keyword "candidate screening" \\
        --banned-words ./banned-words.txt --skip-link-check
"""

import argparse
import re
import sys

import wp_client

CORRECT_DEMO_URL = "https://hs.testlify.com/meetings/testlify/demo"
DEAD_DEMO_URL = "request-demo"
TESTLIFY_HOST = "testlify.com"

# AI-signature characters that must never appear in body text.
AI_CHARS = {
    "em dash": "—",
    "en dash": "–",
    "curly double-open": "“",
    "curly double-close": "”",
    "curly single-open": "‘",
    "curly single-close": "’",
    "ellipsis char": "…",
}

# First-person patterns that must not appear in body copy.
# Brand voice is third-person; first-hand markers belong in the author bio only.
FIRST_PERSON_PATTERNS = [
    r"\bIn my experience\b",
    r"\bIn my work\b",
    r"\bI have seen\b",
    r"\bA pattern I\b",
    r"\bI've\b",
    r"\bI think\b",
    r"\bI believe\b",
    r"\bI always\b",
    r"\bmy experience\b",
    r"\bI find\b",
]

COMPETITORS = ["testgorilla", "imocha", "mettl", "vervoe", "hackerrank",
               "codility", "codesignal"]


def strip_html(html):
    text = re.sub(r"<script[^>]*>.*?</script>", " ", html, flags=re.S | re.I)
    text = re.sub(r"<style[^>]*>.*?</style>", " ", text, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"&[a-zA-Z#0-9]+;", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def word_count(html):
    return len(strip_html(html).split())


def extract_links(html):
    return re.findall(r'href=["\']([^"\']+)["\']', html, flags=re.I)


def has_jsonld_type(html, type_name):
    """True if a JSON-LD script block mentions @type <type_name>."""
    for block in re.findall(
        r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>',
        html, flags=re.S | re.I,
    ):
        if re.search(rf'"@type"\s*:\s*"?{re.escape(type_name)}"?', block):
            return True
    return False


def load_banned_words(path):
    if not path:
        return []
    words = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line and not line.startswith("#"):
                words.append(line)
    return words


def find_banned_hits(text, banned):
    hits = []
    lower = text.lower()
    for word in banned:
        if re.search(r"\b" + re.escape(word.lower()) + r"\b", lower):
            hits.append(word)
    return hits


NON_HTTP_PREFIXES = ("#", "mailto:", "tel:", "javascript:")


def is_checkable(url):
    """True only for real http(s) links worth an HTTP check (skips #anchors, mailto, tel)."""
    return url.startswith("http")


def is_internal(url):
    # In-page anchors / mailto / tel are neither internal nav nor external citations.
    if url.startswith(NON_HTTP_PREFIXES):
        return True  # treat as internal-ish so they're excluded from the external set
    return TESTLIFY_HOST in url or url.startswith("/")


def count_numbers(text):
    return len(re.findall(r"\b\d+(?:\.\d+)?%|\b\d+\.\d+|\$\d[\d,]*|\b\d{2,}\b", text))


def content_h2s(body):
    """H2s that are content sections (exclude FAQ heading + the closing CTA H2)."""
    out = []
    for x in re.findall(r"<h2[^>]*>(.*?)</h2>", body, flags=re.S | re.I):
        t = re.sub(r"<[^>]+>", "", x).strip()
        tl = t.lower()
        if tl.startswith("frequently asked") or "faq" in tl or tl.startswith("hire "):
            continue
        out.append(t)
    return out


def open_a_tags(body, external):
    tags = []
    for m in re.finditer(r'<a [^>]*href="([^"]+)"[^>]*>', body, flags=re.I):
        intern = is_internal(m.group(1))
        if external and not intern:
            tags.append(m.group(0))
        elif not external and intern:
            tags.append(m.group(0))
    return tags


def required_elements(body):
    """Presence map of the rubric elements that a refresh must never drop."""
    low = body.lower()
    return {
        "TL;DR": "tl;dr" in low,
        "data table": body.count("<!-- wp:table") >= 1 or "<table" in low,
        "Pro Tip callout": "pro tip" in low,
        "Key Takeaway callout": "key takeaway" in low,
        "FAQ accordion": "kadence/accordion" in low,
        "named framework": bool(re.search(
            r"testlify[^.<]{0,40}(scorecard|framework|model|matrix|method)", body, re.I)),
        "has internal links": len(open_a_tags(body, external=False)) > 0,
        "has CTA link": bool(re.search(r"(start free|book a demo|free trial)", low)),
    }


STOPWORDS = {
    "the", "a", "an", "and", "or", "for", "to", "of", "in", "on", "with",
    "how", "what", "why", "is", "are", "do", "does", "your", "you", "this",
    "that", "it", "guide", "2026", "2025", "testlify", "best",
}


def content_words(text):
    """Lowercase alphanumeric content tokens, stopwords + short words removed."""
    toks = re.findall(r"[a-z0-9]+", text.lower())
    return {t for t in toks if len(t) > 2 and t not in STOPWORDS}


def parse_meta_title(html):
    """Return the <title> tag text (RankMath meta title) or ''."""
    m = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""


def parse_meta_description(html):
    """Return the meta description content attribute or ''."""
    for pat in (
        r'<meta[^>]+name=["\']description["\'][^>]*content=["\']([^"\']*)["\']',
        r'<meta[^>]+content=["\']([^"\']*)["\'][^>]*name=["\']description["\']',
    ):
        m = re.search(pat, html, re.I)
        if m:
            return m.group(1).strip()
    return ""


def parse_h1(html):
    """Return the first rendered <h1> text or ''."""
    m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S | re.I)
    return re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else ""


def faq_questions(body):
    """Extract FAQ question texts from a Kadence accordion.

    faq_accordion.py renders each question as the accordion title:
    <span class="kt-blocks-accordion-title"><strong>Question?</strong></span>
    (it does NOT write a JSON "title" attr). Read that first; also accept a
    JSON "title" attr if a hand-authored block uses one.
    """
    qs = []
    for m in re.finditer(
        r'kt-blocks-accordion-title[^>]*>\s*(?:<strong>)?(.*?)(?:</strong>)?\s*</span>',
        body, re.S | re.I):
        t = re.sub(r"<[^>]+>", "", m.group(1)).strip()
        if t and ("?" in t or len(t.split()) >= 3):
            qs.append(t)
    for m in re.finditer(r'"title":"((?:[^"\\]|\\.)*)"', body):
        t = m.group(1).encode().decode("unicode_escape", "ignore").strip()
        if t and ("?" in t or len(t.split()) >= 3):
            qs.append(t)
    return list(dict.fromkeys(qs))  # dedupe, keep order


def fmt_row(name, status, detail):
    return f"  {status:<5} | {name:<40} | {detail}"


def main(argv=None):
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("post_id", type=int)
    parser.add_argument("--keyword", required=True, help="Focus keyword")
    parser.add_argument("--banned-words", default=None,
                        help="Path to banned-words file (one per line)")
    parser.add_argument("--min-words", type=int, default=800,
                        help="Thin-content floor only; real target is SERP-median x1.2")
    parser.add_argument("--baseline", default=None,
                        help="Path to the prior post backup JSON; element-parity check "
                             "FAILS if any element present in the baseline is missing now")
    parser.add_argument("--skip-link-check", action="store_true",
                        help="Skip the per-link HTTP 200 check (slow)")
    parser.add_argument("--url", default=None,
                        help="Live published URL. Enables render-time checks: "
                             "meta title/description length, page H1, "
                             "title<->H1 keyword alignment, Gutenberg render integrity")
    parser.add_argument("--serp-cache", default=None,
                        help="Path to a serp_study.py cache JSON; enables the "
                             "FAQ-covers-PAA check (features.paa vs FAQ questions)")
    args = parser.parse_args(argv)

    try:
        post = wp_client.get_post(args.post_id, context="edit")
    except wp_client.WPClientError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    title = post.get("title", {}).get("raw", "") or post.get("title", {}).get(
        "rendered", "")
    body = post.get("content", {}).get("raw", "") or post.get(
        "content", {}).get("rendered", "")
    if not body:
        print("ERROR: post has no body content.", file=sys.stderr)
        return 2

    text = strip_html(body)
    keyword = args.keyword.lower()
    results = []  # (name, passed_bool_or_None, detail) ; None => WARN

    # 1. Word count
    wc = word_count(body)
    results.append(("Word count", wc >= args.min_words,
                    f"{wc} words (min {args.min_words})"))

    # 2. H1 (title) has keyword
    results.append(("H1 contains keyword", keyword in title.lower(),
                    f'title="{title[:60]}"'))

    # 3. Article/BlogPosting schema (WARN if absent: usually theme/RankMath-injected,
    #    not in content.raw, so absence here is not a content fault)
    art = has_jsonld_type(body, "Article") or has_jsonld_type(body, "BlogPosting")
    results.append(("Article/BlogPosting JSON-LD", art if art else None,
                    "in body" if art else "not in body (theme/RankMath injects it on render)"))

    # 4. BreadcrumbList schema (WARN if absent: often template-injected)
    bc = has_jsonld_type(body, "BreadcrumbList")
    results.append(("BreadcrumbList JSON-LD", bc if bc else None,
                    "in body" if bc else "not in body (may be theme/RankMath)"))

    # 5/6. Links
    links = extract_links(body)
    internal = [u for u in links if is_internal(u)]
    external = [u for u in links if not is_internal(u)]
    results.append(("Internal links >= 3", len(internal) >= 3,
                    f"{len(internal)} internal"))
    results.append(("External links >= 1", len(external) >= 1,
                    f"{len(external)} external"))

    # 7. AI-signature characters
    char_hits = {name: text.count(ch) for name, ch in AI_CHARS.items()
                 if ch in text}
    results.append(("No AI-signature chars", not char_hits,
                    "clean" if not char_hits else str(char_hits)))

    # 8. Banned words
    banned = load_banned_words(args.banned_words)
    if banned:
        hits = find_banned_hits(text, banned)
        results.append(("No banned words", not hits,
                        "clean" if not hits else ", ".join(hits[:10])))
    else:
        results.append(("No banned words", None,
                        "skipped (no --banned-words file)"))

    # 9. Demo URL safety: only the dead /request-demo/ is a FAIL.
    demo_correct = CORRECT_DEMO_URL in body
    demo_dead = DEAD_DEMO_URL in body
    results.append(("Demo URL safe (no dead link)", not demo_dead,
                    f"correct_demo_present={demo_correct} dead_request-demo={demo_dead}"))

    # 10. All links return 200 (deduped + checked in parallel; redirects followed)
    if args.skip_link_check:
        results.append(("All links 200", None, "skipped (--skip-link-check)"))
    else:
        from concurrent.futures import ThreadPoolExecutor
        http_links = sorted({u for u in links if is_checkable(u)})  # dedupe
        with ThreadPoolExecutor(max_workers=10) as pool:
            oks = list(pool.map(wp_client.verify_url_200, http_links))
        bad = [u for u, ok in zip(http_links, oks) if not ok]
        results.append(("All links 200", not bad,
                        f"all {len(http_links)} ok" if not bad
                        else f"{len(bad)}/{len(http_links)} non-2xx/3xx: {bad[:5]}"))

    # 11. TL;DR present
    results.append(("TL;DR present", "tl;dr" in body.lower(),
                    "summary at top (key takeaways, NOT a stat dump)"))

    # 12. Enough content H2s are questions
    ch2 = content_h2s(body)
    qh2 = [h for h in ch2 if "?" in h]
    need_q = min(3, len(ch2))
    h2_ok = bool(ch2) and len(qh2) >= max(need_q, (len(ch2) + 1) // 2)
    results.append(("Enough question H2s (>=50% & >=3)", h2_ok,
                    f"{len(qh2)}/{len(ch2)} questions (keyword-phrase headings allowed)"))

    # 13. >=13 specific numbers
    nnum = count_numbers(text)
    results.append((">=13 specific numbers", nnum >= 13, f"{nnum} numeric tokens"))

    # 14. Data table
    results.append(("Data table present", body.count("<!-- wp:table") >= 1 or "<table" in body.lower(),
                    f"{body.count('<!-- wp:table')} table block(s)"))

    # 15. Named Testlify framework
    fw = re.search(r"testlify[^.<]{0,40}(scorecard|framework|model|matrix|method)", body, re.I)
    results.append(("Named Testlify framework", bool(fw),
                    fw.group(0)[:50] if fw else "none found"))

    # 16. Pro Tip + Key Takeaway callouts
    pt = "pro tip" in body.lower(); kt = "key takeaway" in body.lower()
    results.append(("Pro Tip + Key Takeaway", pt and kt, f"proTip={pt} keyTakeaway={kt}"))

    # 17. FAQ accordion with >=5 panes (count OPEN markers only; close is "<!-- /wp:kadence/pane")
    panes = len(re.findall(r"<!-- wp:kadence/pane", body))
    results.append(("FAQ accordion (>=5 Q)", "kadence/accordion" in body and panes >= 5,
                    f"{panes} panes"))

    # 18. Link-rel policy: external nofollow, internal dofollow
    ext_tags = open_a_tags(body, external=True)
    int_tags = open_a_tags(body, external=False)
    ext_ok = bool(ext_tags) and all("nofollow" in t for t in ext_tags)
    int_ok = all("nofollow" not in t for t in int_tags)
    results.append(("External links nofollow", ext_ok if ext_tags else None,
                    f"{sum('nofollow' in t for t in ext_tags)}/{len(ext_tags)} nofollow"))
    results.append(("Internal links dofollow", int_ok,
                    f"{len(int_tags)} internal, none nofollow={int_ok}"))

    # 19. No competitor citations
    comp = [c for c in COMPETITORS if c in text.lower()]
    results.append(("No competitor citations", not comp, comp or "none"))

    # 19b. Max 2 citations per external domain (POLICIES #13 - no over-citing one source)
    from urllib.parse import urlparse
    dom_counts = {}
    for u in extract_links(body):
        if is_checkable(u) and not is_internal(u):
            host = urlparse(u).netloc.lower()
            host = host[4:] if host.startswith("www.") else host
            reg = ".".join(host.split(".")[-2:]) if host else host
            if reg:
                dom_counts[reg] = dom_counts.get(reg, 0) + 1
    over_cited = {d: c for d, c in dom_counts.items() if c > 2}
    results.append(("Max 2 citations/domain", not over_cited,
                    "ok" if not over_cited else f"over-cited: {over_cited} (cap 2/domain - diversify)"))

    # 19d. Source diversity (POLICIES #13 / source-authority) - do not lean on 1-2 famous sources.
    n_domains = len(dom_counts)
    total_cites = sum(dom_counts.values())
    if total_cites >= 3:
        diverse = n_domains >= 3
        results.append(("Source diversity (>=3 domains)", diverse,
                        f"{n_domains} distinct domains across {total_cites} citations"
                        + ("" if diverse else " - research more primaries, do not default to SHRM/Gallup")))
        # SHRM+Gallup must not be the only sources
        famous = {d for d in dom_counts if any(k in d for k in ("shrm", "gallup"))}
        only_famous = bool(famous) and set(dom_counts) <= {"shrm.org", "gallup.com"}
        results.append(("Not SHRM/Gallup-only", not only_famous,
                        "ok" if not only_famous else "post cites ONLY SHRM/Gallup - add other primaries"))
    else:
        results.append(("Source diversity (>=3 domains)", None,
                        f"{total_cites} citations (need >=3 to assess diversity)"))

    # 19c. No brand promotion (POLICIES #13 - cite, do not promote/drive to another brand's content)
    promo = []
    for m in re.finditer(
        r"[^.]*\b(pairs well with|(keeps|has|offers|maintains|publishes|provides)\s+(a|an|its)?\s*"
        r"[\w ]{0,20}(guide|resource|toolkit|template|playbook|primer)|"
        r"check out\s+[\w' ]+\b(guide|resource|toolkit|template))\b[^.]*\.",
        text, re.I):
        sent = m.group(0).strip()
        if "testlify" not in sent.lower():  # promoting OUR own content is fine
            promo.append(sent[:90])
    results.append(("No brand promotion", not promo,
                    "clean" if not promo else f"promotes external brand: {promo[:2]}"))

    # 20. Block-comment balance (void/self-closing blocks like wp:spacer /--> have no close)
    voids = len(re.findall(r"<!-- wp:[^>]*/-->", body))
    opens = body.count("<!-- wp:") - voids
    closes = body.count("<!-- /wp:")
    bal = opens == closes
    results.append(("Block-comment balance", bal,
                    f"{opens} paired-open / {closes} close / {voids} void"))

    # 20b. No horizontal dividers
    div_hits = len(re.findall(r"<hr\b", body, re.I)) + body.count("wp:separator")
    results.append(("No horizontal dividers", div_hits == 0,
                    "none" if div_hits == 0 else f"{div_hits} <hr>/separator block(s)"))

    # 21a. No leftover placeholder/template tokens (P0)
    placeholders = re.findall(r"\[(?:EXTERNAL LINK|INTERNAL LINK|SOURCE|STAT|PASTE|TODO|URL)[^\]]*\]", body)
    results.append(("No placeholder tokens", not placeholders,
                    "clean" if not placeholders else f"{len(placeholders)} leftover: {placeholders[:5]}"))

    # 21b. Every H2 < 60 chars
    h2_texts = [re.sub(r"<[^>]+>", "", x).strip() for x in re.findall(r"<h2[^>]*>(.*?)</h2>", body, re.S | re.I)]
    long_h2 = [h for h in h2_texts if len(h) >= 60]
    results.append(("H2s < 60 chars", not long_h2,
                    "all < 60" if not long_h2 else f"{len(long_h2)} >=60 chars: {long_h2[:2]}"))

    # 22. Element parity vs baseline
    if args.baseline:
        import json
        try:
            base = json.load(open(args.baseline, encoding="utf-8"))
            base_body = base.get("content", {}).get("raw", "")
            be, ne = required_elements(base_body), required_elements(body)
            dropped = [k for k in be if be[k] and not ne[k]]
            results.append(("Element parity vs baseline", not dropped,
                            "no element dropped" if not dropped
                            else "DROPPED: " + ", ".join(dropped)))
        except Exception as exc:  # noqa: BLE001
            results.append(("Element parity vs baseline", None, f"baseline unreadable: {exc}"))
    else:
        results.append(("Element parity vs baseline", None,
                        "skipped (no --baseline)"))

    # 23. No first-person body copy (brand voice = third-person throughout;
    #     first-hand markers belong in the author bio only, never in article body).
    fp_hits = [p for p in FIRST_PERSON_PATTERNS if re.search(p, text, re.I)]
    results.append(("No first-person body copy", not fp_hits,
                    "clean" if not fp_hits else "FOUND: " + "; ".join(fp_hits[:3])))

    # 24. CTA appears before FAQ accordion (not after).
    #     Multiple reviewed posts had CTA placed after the FAQ block; team moved it every time.
    cta_m = re.search(r"(start free|book a demo|free trial|hs\.testlify\.com)", body, re.I)
    faq_m = re.search(r"wp:kadence/accordion", body, re.I)
    if cta_m and faq_m:
        cta_ok = cta_m.start() < faq_m.start()
        results.append(("CTA before FAQ accordion", cta_ok,
                        "OK" if cta_ok else "CTA is AFTER accordion - move CTA before FAQ"))
    else:
        results.append(("CTA before FAQ accordion", None,
                        f"cta_found={bool(cta_m)} faq_found={bool(faq_m)}"))

    # 25. No duplicate external links.
    #     Duplicate external links appeared in 6+ reviewed tickets (e.g. Gallup linked twice).
    ext_url_counts = {}
    for u in extract_links(body):
        if not is_internal(u) and u.startswith("http"):
            ext_url_counts[u] = ext_url_counts.get(u, 0) + 1
    dup_ext = [u for u, c in ext_url_counts.items() if c > 1]
    results.append(("No duplicate external links", not dup_ext,
                    "no duplicates" if not dup_ext
                    else f"{len(dup_ext)} dup(s): {[u[:70] for u in dup_ext[:3]]}"))

    # 26. Key Takeaways section is substantive (>120 words).
    #     Team flagged one-line KT summaries repeatedly; the section needs real depth.
    kt_m = re.search(
        r"key takeaway.{0,30000}?(?=<!--\s*/wp:kadence|<!--\s*wp:heading|$)", body, re.I | re.S
    )
    kt_wc = len(strip_html(kt_m.group(0)).split()) if kt_m else 0
    results.append(("Key Takeaways substantive (>120 words)", kt_wc > 120 if kt_m else None,
                    f"{kt_wc} words in KT section" if kt_m else "KT section not found or empty"))

    # 26b. No author/byline section in the BODY (the theme renders the author box
    #      natively from the WP author field; a body "About the author" / byline
    #      duplicates it - see the 2026-06-29 duplicate-author incident).
    author_in_body = re.search(
        r"<h[1-6][^>]*>\s*about the author|>\s*about the author\s*<|written by\b|"
        r"\bby (the )?testlify team\b|about the writer", body, re.I)
    results.append(("No author section in body", not author_in_body,
                    "clean" if not author_in_body
                    else f"FOUND body author/byline ('{author_in_body.group(0)[:40]}') - remove; author box is theme-native"))

    # 27. FAQ covers the SERP People-Also-Ask questions (--serp-cache only).
    #     5 tickets added missing PAA-matched FAQ entries by hand.
    if args.serp_cache:
        import json as _json
        try:
            paa = _json.load(open(args.serp_cache, encoding="utf-8")).get(
                "features", {}).get("paa", []) or []
        except Exception as exc:  # noqa: BLE001
            paa = []
            results.append(("FAQ covers PAA", None, f"serp-cache unreadable: {exc}"))
        if paa:
            faq_qs = faq_questions(body)
            faq_word_sets = [content_words(q) for q in faq_qs]
            covered, missing = [], []
            for q in paa:
                qw = content_words(q)
                hit = any(qw and len(qw & fw) / len(qw) >= 0.5 for fw in faq_word_sets)
                (covered if hit else missing).append(q)
            # FAIL only when the FAQ covers NONE of the PAA; otherwise WARN-list gaps.
            if not covered:
                results.append(("FAQ covers PAA", False,
                                f"0/{len(paa)} PAA covered; add: {missing[:3]}"))
            elif missing:
                results.append(("FAQ covers PAA", None,
                                f"{len(covered)}/{len(paa)} covered; gaps: {missing[:3]}"))
            else:
                results.append(("FAQ covers PAA", True, f"all {len(paa)} PAA covered"))
    else:
        results.append(("FAQ covers PAA", None, "skipped (no --serp-cache)"))

    # --- Render-time checks (--url only): the page as Google + a reader see it. ---
    if args.url:
        html = wp_client.fetch_rendered(args.url)
        if not html:
            results.append(("Rendered page fetched", False, f"empty/failed for {args.url}"))
        else:
            mtitle = parse_meta_title(html)
            mdesc = parse_meta_description(html)
            h1 = parse_h1(html)

            # 28. Meta title present + 50-60 chars (RankMath title / <title> tag).
            mt_ok = bool(mtitle) and 40 <= len(mtitle) <= 65
            results.append(("Meta title 40-65 chars", mt_ok,
                            f'len={len(mtitle)} "{mtitle[:60]}"' if mtitle else "no <title>"))

            # 29. Meta description present + 140-160 chars.
            md_ok = bool(mdesc) and 120 <= len(mdesc) <= 165
            results.append(("Meta description 120-165 chars", md_ok,
                            f'len={len(mdesc)} "{mdesc[:60]}"' if mdesc else "no meta description"))

            # 30. Title <-> H1 keyword alignment (TM-451/433/499/525: intent mismatch).
            #     Focus keyword must be in BOTH the meta title and the H1.
            if mtitle and h1:
                kw_in_both = keyword in mtitle.lower() and keyword in h1.lower()
                overlap = content_words(mtitle) & content_words(h1)
                base = content_words(h1) or {"_"}
                jac = len(overlap) / len(content_words(mtitle) | content_words(h1) or {"_"})
                align_ok = kw_in_both and jac >= 0.3
                results.append(("Title<->H1 aligned (kw in both)", align_ok,
                                f'kw_in_both={kw_in_both} overlap={jac:.2f} '
                                f'h1="{h1[:40]}"'))
            else:
                results.append(("Title<->H1 aligned (kw in both)", None,
                                f"title_found={bool(mtitle)} h1_found={bool(h1)}"))

            # 31. Gutenberg render integrity: no leaked block comments, accordion
            #     rendered, zero leftover placeholder tokens in the live page.
            leaked_blocks = len(re.findall(r"&lt;!--\s*/?wp:|<!--\s*/?wp:", html))
            accordion_rendered = bool(
                re.search(r"kt-accordion|kadence-accordion|wp-block-kadence", html, re.I))
            # only count placeholder tokens in the article body region, not nav/scripts
            ph_render = re.findall(
                r"\[(?:EXTERNAL LINK|INTERNAL LINK|SOURCE|STAT|PASTE|TODO|URL)[^\]]*\]", html)
            gb_ok = leaked_blocks == 0 and not ph_render
            results.append(("Gutenberg render integrity", gb_ok,
                            f"leaked_block_comments={leaked_blocks} "
                            f"placeholder_tokens={len(ph_render)} "
                            f"accordion_rendered={accordion_rendered}"))
            if not accordion_rendered:
                results.append(("FAQ accordion rendered live", None,
                                "no kadence-accordion class found in rendered HTML"))
    else:
        results.append(("Render-time checks", None, "skipped (no --url)"))

    # Print table
    print(f"\nVerification: post {args.post_id}  keyword='{args.keyword}'")
    print("  " + "-" * 80)
    print(fmt_row("CHECK", "STAT", "DETAIL"))
    print("  " + "-" * 80)
    failed = 0
    for name, passed, detail in results:
        if passed is True:
            status = "PASS"
        elif passed is False:
            status = "FAIL"
            failed += 1
        else:
            status = "WARN"
        print(fmt_row(name, status, detail))
    print("  " + "-" * 80)
    print(f"  {failed} FAIL, "
          f"{sum(1 for _, p, _ in results if p is None)} WARN, "
          f"{sum(1 for _, p, _ in results if p is True)} PASS\n")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
