#!/usr/bin/env python3
"""Generate the CANONICAL Testlify Kadence FAQ accordion block.

Reference implementation: post 293423 (/how-to-ensure-language-fairness-in-assessments/).
This is the house-standard FAQ format for ALL Testlify content - use it instead of
core heading+paragraph blocks, for better UX (collapsible) and a consistent look.

Markup is byte-matched to the live reference: arrow icon, left-aligned titles,
single-open (data-allow-multiple-open="false"), first pane open (kt-active-pane-0),
faqSchema:true. Only the question/answer text and the unique IDs change per post.

Usage:
    python3 faq_accordion.py --post-id 285939 --qa qa.json > faq_block.html
where qa.json is a list of {"q": "...", "a": "..."} (answers may contain inline HTML
such as <a href> and <strong>; they are inserted verbatim inside a wp:paragraph).

Importable:  from faq_accordion import build_accordion
    block = build_accordion(post_id, [("Question?", "Answer."), ...])
"""
import argparse, hashlib, json, sys

# Exact accordion attribute JSON from the reference post (uniqueID + paneCount filled in).
_ACC_ATTRS = (
    '{{"uniqueID":"{uid}","paneCount":{n},"contentBgColor":"#ffffff",'
    '"contentBorderStyle":[{{"top":["","",0],"right":["","",1],"bottom":["","",1],"left":["","",1],"unit":"px"}}],'
    '"titleStyles":[{{"size":["","",""],"sizeType":"px","lineHeight":["","",""],"lineType":"","letterSpacing":"",'
    '"family":"","google":"","style":"","weight":"","variant":"","subset":"","loadGoogle":true,'
    '"padding":[14,16,14,16],"marginTop":10,"color":"#444444","background":"#ffffff","border":["","","",""],'
    '"borderRadius":["","","",""],"borderWidth":["","","",""],"colorHover":"#444444","backgroundHover":"#ffffff",'
    '"borderHover":["","","",""],"colorActive":"#444444","backgroundActive":"#ffffff","borderActive":["","","",""],'
    '"textTransform":""}}],'
    '"titleBorder":[{{"top":["#eeeeee","",1],"right":["#eeeeee","",1],"bottom":["#eeeeee","",1],"left":["#eeeeee","",2],"unit":"px"}}],'
    '"titleBorderHover":[{{"top":["#d4d4d4","",""],"right":["#d4d4d4","",""],"bottom":["#d4d4d4","",""],"left":["#d4d4d4","",""],"unit":"px"}}],'
    '"titleBorderActive":[{{"top":["#eeeeee","",""],"right":["#eeeeee","",""],"bottom":["#eeeeee","",""],"left":["#0e9cd1","",""],"unit":"px"}}],'
    '"titleBorderRadius":[0,0,0,0],"iconStyle":"arrow","faqSchema":true}}'
)


def _uid(post_id, salt):
    h = hashlib.md5(f"{post_id}:{salt}".encode()).hexdigest()
    return f"{post_id}_{h[:6]}-{h[6:8]}"


def build_accordion(post_id, qa_pairs):
    """qa_pairs: list of (question, answer_html). Returns the full accordion block string."""
    n = len(qa_pairs)
    acc_uid = _uid(post_id, "accordion")
    panes = []
    for i, (q, a) in enumerate(qa_pairs, start=1):
        puid = _uid(post_id, f"pane{i}")
        idattr = "" if i == 1 else f'"id":{i},'
        panes.append(
            f'<!-- wp:kadence/pane {{{idattr}"uniqueID":"{puid}"}} -->\n'
            f'<div class="wp-block-kadence-pane kt-accordion-pane kt-accordion-pane-{i} kt-pane{puid}">'
            f'<div class="kt-accordion-header-wrap"><button class="kt-blocks-accordion-header kt-acccordion-button-label-show" type="button">'
            f'<span class="kt-blocks-accordion-title-wrap"><span class="kt-blocks-accordion-title"><strong>{q}</strong></span></span>'
            f'<span class="kt-blocks-accordion-icon-trigger"></span></button></div>'
            f'<div class="kt-accordion-panel"><div class="kt-accordion-panel-inner"><!-- wp:paragraph -->\n'
            f'<p>{a}</p>\n'
            f'<!-- /wp:paragraph --></div></div></div>\n'
            f'<!-- /wp:kadence/pane -->'
        )
    attrs = _ACC_ATTRS.format(uid=acc_uid, n=n)
    inner = "\n\n".join(panes)
    return (
        f'<!-- wp:kadence/accordion {attrs} -->\n'
        f'<div class="wp-block-kadence-accordion alignnone">'
        f'<div class="kt-accordion-wrap kt-accordion-id{acc_uid} kt-accordion-has-{n}-panes kt-active-pane-0 '
        f'kt-accordion-block kt-pane-header-alignment-left kt-accodion-icon-style-arrow kt-accodion-icon-side-right" style="max-width:none">'
        f'<div class="kt-accordion-inner-wrap" data-allow-multiple-open="false" data-start-open="0">'
        f'{inner}</div></div></div>\n'
        f'<!-- /wp:kadence/accordion -->'
    )


def main():
    ap = argparse.ArgumentParser(description="Generate the canonical Testlify Kadence FAQ accordion.")
    ap.add_argument("--post-id", required=True)
    ap.add_argument("--qa", required=True, help="JSON file: list of {q, a}")
    args = ap.parse_args()
    qa = json.load(open(args.qa))
    pairs = [(item["q"], item["a"]) for item in qa]
    if not pairs:
        print("no Q/A pairs", file=sys.stderr); sys.exit(1)
    sys.stdout.write(build_accordion(args.post_id, pairs))


if __name__ == "__main__":
    main()
