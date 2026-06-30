---
type: standard / workflow-recipe
reusable: any company
applies_to: every page that needs images (blogs, assets, money pages)
last_updated: 2026-06-22
---

# Image Sourcing Standard — where page images come from + how to ship them

Two jobs: **source** the right image, then **ship** it to spec so it helps (not hurts) SEO and speed.

## Where images come from (in priority order)
1. **Design-team originals** — for the **hero image** and any **data-viz / diagrams / infographics**. These
   are the images that carry the brand and that other sites can't copy — so they also **double as
   link-building seeds** (`research/strategies/image-link-building.md`: publish the original, then reclaim
   credit/links where others reuse it). Raise a design ticket with the spec below.
2. **Free stock** — for generic / filler images. Unsplash or Pexels (free APIs; needs a free key). Pick
   relevant, non-cliché shots; avoid the obvious "people in suits shaking hands" stock look.
3. **Screenshots** — product UI, dashboards, real examples — often the most useful and most cited.

> Don't use an image you don't have rights to. Originals and properly-licensed stock only.

## Ship-to-spec (every image, before publish)
- **Format:** **WebP**, compressed — aim **< 200 KB** (hero can be a bit larger if needed).
- **Dimensions:** set explicit **width + height** attributes (prevents layout shift / CLS). Use a responsive
  `srcset` for large images. **Social/OG image: 1200×630.**
- **Filename:** descriptive, hyphenated, keyword where natural (e.g. `skills-based-hiring-funnel.webp`) —
  never `IMG_2843.png`.
- **Alt text:** describes the image + keyword where natural (accessibility *and* a ranking signal).
- **Loading:** lazy-load anything below the fold; the hero loads eagerly.

## Converting to WebP
Use a tool that actually outputs WebP — e.g. Python **Pillow** (`img.save('out.webp', 'webp', quality=82)`)
or `cwebp`. (Note: macOS `sips` cannot output WebP.)

## Done when
Every image on the page is WebP, under budget, has alt text + dimensions + a descriptive filename, the hero
+ data-viz are originals (design ticket raised), and the OG image is 1200×630. Verify with the image audits
in `lighthouse-qa.workflow.md`.
