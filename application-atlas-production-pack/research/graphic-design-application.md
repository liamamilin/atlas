# Research Notes — Graphic Design Application

## Research Goal

Understand what a Graphic Design Application is as an Application Type: its defining core, its standard mature structure, its variants, and its boundaries against the neighboring creation Types (Vector Graphics Editor, Illustration Application, Template-based Design Platform, Collaborative Design Platform, Raster Image Editor, Desktop Publishing Application, AI Design Generator).

This leaf sits in DIRECTORY section 04.01 "General Visual Design" with two siblings: Template-based Design Platform and Collaborative Design Platform (both processed in earlier passes). Two prior passes recorded boundary gradients against this leaf:

- collaborative-design-platform (§Boundary Findings #1): "the graphic design application centers a single professional designer working in local files (desktop, print/illustration-oriented)"; seam = whether the shared multi-user file is the unit of work or a distribution convenience.
- ai-design-generator (§Boundary Findings #3): "who composes the first pass: the system (generation-first) vs the user (editing-first)… the difference is the workflow center of gravity, not feature presence."

This pass must ratify or refine both from this side, and draw the remaining boundaries.

## Initial Boundary (hypothesis before research)

- What: general-purpose application where a user composes visual designs (multi-element compositions of shapes, text, images) into design artifacts (logos, posters, collateral, packaging, signage, social graphics) and produces finished output.
- Users: graphic designers (professional/in-house/freelance), print/sign shops, marketing teams, small businesses, hobbyists.
- Nearest neighbors: Vector Graphics Editor (04.03), Illustration Application (04.03), Template-based Design Platform (04.01), Collaborative Design Platform (04.01), Raster Image Editor (04.02), Desktop Publishing Application (04.17), AI Design Generator (04.20), UI Design Application (04.15).
- Sharpest expected seam: vs Vector Graphics Editor — the market flagship products (Illustrator, CorelDRAW) are commonly cited under both labels.
- Unknowns: whether "graphic design" is separable from "vector editing" as a market category; whether multi-page layout belongs in the core; how the consumer/browser pole (CorelDRAW Go-class) relates to template platforms.

## Research Questions

1. What is the unit of work (document/canvas/artboard/page) and what object classes does it hold?
2. What is the canonical workflow from start to delivered artifact?
3. Which capabilities are universal in the sample vs tier/segment-dependent?
4. What output machinery exists (color modes, print preparation, export formats)?
5. Where is the boundary vs vector editing, illustration, template platforms, collaborative platforms, raster editing, DTP, and AI generation?
6. Historical check: do 1980s–90s desktop products (and regional/platform-native ones) satisfy the definition without cloud/subscription/AI?

## Representative Products

Selection principles: market representation + documentation accessibility + different product philosophies + different customer tiers.

| Product | Role in sample | Directly researched? |
|---|---|---|
| CorelDRAW Graphics Suite (Corel) | legacy all-in-one professional graphic design suite; print/sign/apparel verticals; tier ladder (Go/Standard/Suite) | YES — product page, family comparison, Standard page, learning-center guide, how-to index, poster tutorial |
| Xara Designer Pro+ (Xara GmbH) | all-in-one single-application graphic design for designers/marketers/businesses; DTP+web+photo+illustration+PDF pillars | YES — product page + features page |
| Adobe Illustrator (Adobe) | market-standard professional design/vector application | NO — helpx.adobe.com unreachable (timeouts ×2); market anchor only |
| Affinity Designer (Serif/Canva) | modern professional design application, one-time-purchase heritage | NO — affinity.serif.com 403, affinity.help 403; market anchor only |

Rejected candidates: Inkscape (docs unreachable; also the Vector Graphics Editor archetype — boundary evidence only), Canvas X Draw (canvas.graphics transport error, acdsee.com 404), Gravit/Corel Vector (discontinued), Sketch (sampled by the collaborative-design-platform pass; UI-design-centric), Canva (Template-based Design Platform archetype; unreachable in prior passes).

## Sources

Fetched 2026-09-07 (all official vendor surfaces):

- CorelDRAW Graphics Suite product page — https://www.coreldraw.com/en/product/coreldraw/
- CorelDRAW product family comparison — https://www.coreldraw.com/en/product/family/
- CorelDRAW Standard product page — https://www.coreldraw.com/en/product/coreldraw/standard/
- CorelDRAW How-to Guides index — https://www.coreldraw.com/en/learn/how-to/
- CorelDRAW official tutorial "How To Make a Poster" — https://www.coreldraw.com/en/tips/design/advertising/design-a-poster/
- CorelDRAW Guide to Vector Design: "What is Vector Art?" — https://www.coreldraw.com/en/learn/guide-to-vector-design/what-is-vector-art/
- CorelDRAW Guide to Vector Design: "Choosing Vector Software" — https://www.coreldraw.com/en/learn/guide-to-vector-design/choosing-vector-software/
- Xara Designer Pro+ product page — https://www.xara.com/designerpro-plus/
- Xara Designer Pro+ features page — https://www.xara.com/designerpro-plus/features/

Unreachable (recorded per source-access limitation; abandoned after 1–2 failures each):

- helpx.adobe.com (Illustrator user guide, get-started): timeout ×2
- affinity.serif.com: 403; affinity.help: 403
- inkscape.org: 403; docs.inkscape.org: transport error
- canvas.graphics: transport error; acdsee.com Canvas page: 404
- xara.com /designer-pro-plus/ and /us/designer-pro-plus/: 404 (correct path found at /designerpro-plus/)
- support.corel.com KB: shell reachable but article bodies do not render (JS-gated); product.corel.com legacy help: 404

Evidence layers used below: **A** = directly observed on an official source for a specific product; **B** = cross-product commonality; **C** = canonical inference.

## Product Observations

### CorelDRAW Graphics Suite (Corel) — evidence layer A

Positioning (product page): "Professional graphic design software for Mac/Windows"; FAQ: "a professional graphic design software solution for Windows, Mac, and web." Suite composition: CorelDRAW ("vector illustration and page layout"), Corel PHOTO-PAINT ("image editing and pixel-based design"), Corel Font Manager, CorelDRAW Web (browser-based, subscriber-exclusive), CAPTURE (screen capture), PowerTRACE (bitmap-to-vector tracing inside CorelDRAW).

Job scope (how-to index, official tutorials — the vendor's own list of "the most common graphic design tasks"): brand identity (logo, letterhead, business cards, monogram), social/web graphics (banners, newsletters, covers, web graphics, site icons), advertising/marketing materials (postcards, labels, flyers, posters, brochures, gift certificates), technical drawings (schematic diagrams), banners, character design, infographics, calendars, cards, wedding programs, restaurant menus, car wraps, car magnets, stickers/decals, page layouts (yearbook, comic, homepage, landing page, magazine, manga), t-shirt design, vectorizing images.

Feature pillars (product page): vector illustration (shaping/drawing tools; effects: Contour, Envelope, Blend, Mesh Fill), page layout (brochures, multi-page documents; toggle single-page vs multipage editing), typography (text effects, variable fonts, fit text to path), font management, photo editing (PHOTO-PAINT), AI (prompt-based image generation with selectable models, image remix, one-click background removal, AI masking), print/web output (color management engine, prepress tools, free Pantone libraries), non-destructive editing (block shadows, symmetry, perspective as reversible adjustments), PowerTRACE tracing, multipage view (manage assets across pages), multi-asset export, object styles/style sets, object management (Objects docker: hide/rename/search/stacking order; Focus Mode isolation), workspace/shortcut customization, color/fills/transparencies (swatches, harmonies, gradients, mesh fills), extensive file compatibility, bundled content (clipart, photos, fonts incl. Google Fonts access, templates, fills, brushes).

Tier ladder (family comparison page):
- **CorelDRAW Go** — "Intuitive web-based graphic design app"; "beginner-friendly graphic design toolset"; "more vector editing capabilities than many template-based alternatives"; millions of design assets; "virtually no learning curve"; ~10 file formats; subscription; AI image creation/editing.
- **CorelDRAW Standard** — "Desktop graphic design software for your hobby or home business"; two apps (CorelDRAW Standard + PHOTO-PAINT Standard); one-time purchase; ~70 formats; 2,000+ assets; features: vector illustration, page layout (rulers/grids/guidelines), photo editing, typography, web graphics ("pixel-perfect tools" for crisp web export), color/fills/transparencies, object management, creative templates (certificates, ads, business cards, letterhead, flyers, posters), PowerTRACE.
- **CorelDRAW Graphics Suite** — "Comprehensive graphic design toolbox for professionals"; "total output control for professional printing & production"; "integrated functionality for design and multi-page layout in one application"; ~100 formats; Pantone integration; subscription/one-time/maintenance.

FAQ facts (family page): all three support RGB; all three support CMYK but Suite has "advanced color management tools for precise control over color profiles, spot colors, and professional-grade output"; text-to-path in all; bitmap-to-vector tracing in Suite + Standard, not Go; generative AI in Suite and Go (credit-metered; prompts/results not used for training). Format list includes native CDR plus PSD, AI, EPS, SVG, PDF, DOCX, DWG/DXF, PUB (Microsoft Publisher), VSD imports.

Industry verticals (product page): branding/marketing, signage & large-format printing ("powerful color management engine and superior prepress tools"), apparel & textiles (screen printing, embroidery, DTG), retail/e-commerce, blueprints/maps/schematics, illustration/fine art. Customer stories: sign-making tools, vinyl graphics, technical documentation illustration, metal cut signs, flags/embroidery, sewing patterns, laser-cut leather designs.

Official tutorial workflow ("How To Make a Poster"): Welcome Screen → New From Template (filter by type "Posters/signs") → page setup (change page size) → modify content (delete logo, add rectangle, replace image, import company logo, change text) → output (inkjet printer, or local copy house for larger quantities).

Educational guide ("What is vector art?"): vector = math-defined lines/points/curves/shapes, infinitely scalable; uses: logos, icons, billboards, posters, flyers, apparel (embroidery/sublimation machinery follows clean lines), web/UX; users: web/UX designers, print-industry graphic designers, illustrators, CAD/engineers. History: Sketchpad (1963) → Illustrator (1985) → CorelDRAW (1989).

Educational guide ("Choosing Vector Software"): category framed as "vector graphics software" with options CorelDRAW, Illustrator, Inkscape, Canva; "free vector software like Canva, Krita, and Inkscape gives you basic graphic design functions"; Canva distinguished as "not purely a vector graphics software… browser-based design software… many pre-made templates and design elements… popular for social media graphics and posters"; CorelDRAW "used by graphic design professionals and hobbyists alike"; Illustrator "popular vector editor… since 1985… in the Adobe Creative Cloud with Photoshop and InDesign… subscription model launched in 2012, no one-time purchase option."

### Xara Designer Pro+ (Xara GmbH) — evidence layer A

Positioning (product page): "All-in-One Graphic Design, Photo Editing & Web Design Software"; "Create vector graphics, edit photos, design websites and publish professional documents… powerful creative software for designers, marketers and businesses." Tagline: "Vector design, above industry-level… Whether it's a billboard, business card, social post, or a website."

Five capability pillars (features page, each framed as "Replaces" a category of competitors):
1. **Desktop publishing** (replaces MS Publisher, InDesign, Word, Affinity Designer): advanced text flow & columns, Pantone support, automatic text flow around images, text styles & custom fonts, table of contents, multi-page documents (multi-column, auto page numbering, headers/footers), document auto-resize (A3→A4→US Letter with items adapting), commercial printing (orientation, image fit, print layers, print borders, print-color simulation, full color separation), Page and Layer Gallery (organize/hide/lock pages, layers, elements; 'Solo' mode isolation).
2. **Web design** (replaces Dreamweaver, Wix, WordPress): WYSIWYG editor, drag-and-drop, website templates, responsive variants, freehand or snap-to-object placement, global styles, SEO controls, image optimization, self-hosted fonts.
3. **Photo editing** (replaces Photoshop, Affinity Photo): Magic Erase, background remover, color-select enhancement, compression ("up to ten times smaller"), Magic Undo (undo changes to saved photos), one-click enhance, Photoshop plugin support, Bitmap Tracer (photos/line-art/logos → editable vector shapes).
4. **Illustration** (replaces Illustrator, CorelDRAW, Affinity Designer): QuickShape & freehand drawing, Blend tool, soft vectors & feathering, transparency, scatter/art brushes, 3D extrude, **Live Effects** ("vector objects remain editable after applying effects"), ClipView (object-as-window masking), shadows, bevels, contours, **Live Copies** (duplicates update instantly when one is edited).
5. **PDF editing** (replaces Acrobat): edit any PDF, merge, password protect, Illustrator compatibility ("vector artwork… imported cleanly into Illustrator versions 9 onwards"), multiple PDF export profiles (Draft, Email, High Quality, Commercial Printing; PDF/X for commercial printing), compress.

Integrations: forms (JotForm/Typeform/Airtable), ecommerce (Stripe/PayPal/Gumroad), scheduling, lead capture, media embeds, Xara Cloud (browser companion), cloud drives (Google Drive/OneDrive/Dropbox).

Product family context: Xara's desktop line = Designer Pro+ (all-in-one), Photo & Graphic Designer+ (photo+illustration), Web Designer+ (web); the company's homepage has pivoted to real-estate marketing automation, but the desktop design apps remain marketed under "Desktop Creative Tools."

### Adobe Illustrator (Adobe) — NO direct evidence; market anchor

Widely-attested structural facts only (no operational claims): industry-standard professional application for vector-based design work (logos, icons, typography, illustration); part of Adobe Creative Cloud alongside Photoshop and InDesign; subscription-only since 2012 (this last fact sourced from Corel's official educational guide — layer B, competitor-published). Corel's guide also names Illustrator's bitmap-to-vector tool "Image Trace" (layer B).

### Affinity Designer (Serif) — NO direct evidence; market anchor

Widely-attested structural facts only: professional graphic design application from Serif, positioned against Illustrator; one-time-purchase heritage. Serif's web properties were unreachable this pass (403 ×2). The desktop-publishing pass directly observed affinity.serif.com redirecting to Canva-owned web infrastructure (ownership change not independently verified). No operational claims made.

## Cross-product Comparison

| Dimension | CorelDRAW Graphics Suite | Xara Designer Pro+ | (Anchors: Illustrator, Affinity Designer) |
|---|---|---|---|
| Self-label | "professional graphic design software" | "All-in-One Graphic Design, Photo Editing & Web Design Software" | positioned as professional design applications (market-attested) |
| Unit of work | design document (single- or multi-page; CDR) | design document (single- or multi-page; pages + layers gallery) | design document (artboards per market attestation — not operationally claimed here) |
| Element classes | vector shapes/curves, text, bitmaps | vector shapes, text, bitmaps | same (market-attested) |
| Composition machinery | drawing/shaping tools, effects (Contour/Envelope/Blend/Mesh Fill), object styles, stacking | QuickShape/freehand, blend, brushes, 3D extrude, Live Effects, Live Copies, ClipView | same class (market-attested) |
| Typography | text effects, variable fonts, text-on-path, Font Manager companion | text styles, custom fonts, text flow around images | same class (market-attested) |
| Raster capability | companion app (PHOTO-PAINT) + bitmap fills/tracing | integrated photo editing + bitmap tracer | companion/integrated (market-attested) |
| Multi-page | page layout pillar; single/multipage toggle; multipage view | DTP pillar: multi-page, text flow, auto page numbering | artboards (market-attested) |
| Output machinery | color management, Pantone, prepress, ~100 formats | commercial printing controls, color separation, PDF/X profiles, ~30 formats | print production (market-attested) |
| Color modes | RGB + CMYK (depth by tier; spot colors in Suite) | Pantone; print-color simulation; separation | same class |
| Tracing | PowerTRACE (AI-assisted) | Bitmap Tracer | Image Trace (named by Corel's guide) |
| Templates/content | 200+ templates, clipart, fonts, fills; template-filtered start | template collection (print & web); Elements library | same class |
| AI (current gen) | AI Generate (prompt→image, model choice), remix, bg removal, masking; credit-metered | AI-help built in (v25.1); magic erase/bg remover | generative features (market-attested) |
| Web delivery | CorelDRAW Web (subscriber-exclusive browser app); Go (beginner web app) | web design/publishing pillar; Xara Cloud companion | n/a |
| Collaboration | cloud collaboration/asset management as subscription-exclusive features | Xara Cloud "create, collaborate, brand… from your browser" | Figma-class competitors own this pole |
| Licensing | subscription + one-time + maintenance; AI credits | subscription ("as low as" monthly) | subscription (Illustrator, per Corel's guide); one-time heritage (Affinity) |
| Audience tiers | Go (beginner/web) → Standard (hobby/home business) → Suite (professionals/enterprise) | designers, marketers, businesses (SMB/pro pole) | professionals |

### Cross-product commonalities (layer B)

Across the two directly-researched products (plus the anchors' market position and Corel's category guide):

1. The unit of work is a **design document**: a canvas (page/artboard) holding a composition of discrete elements — drawn shapes, text, imported images — that remain individually editable objects.
2. The toolset is **mixed-media by design**: vector drawing + typography + bitmap handling + effects in one product (or one suite), because design deliverables combine all of them.
3. The workflow is **editing-first**: start blank/from template/from imported artwork → compose → style → refine → prepare → deliver. Templates and AI generation are starting points/capabilities, not the organizing structure.
4. **Output machinery is part of the Type**: export to standard formats (image/vector/PDF), color modes matched to destination (RGB web / CMYK print), print-production controls at the professional pole.
5. **Object permanence**: effects and styling remain reversible/editable (Corel "non-destructive editing"; Xara "Live Effects… vector objects remain editable").
6. **Content libraries and templates** ship with the product as starting points (clipart, fonts, fills, templates).
7. **Tier laddering**: the same product family spans beginner (web, template-adjacent, limited formats) → enthusiast (desktop, one-time) → professional (full output control).
8. **Current-generation AI** (generation, background removal, masking) is being embedded as credit-metered capabilities without changing the editing-first center.

## Abstraction Levels

### L0 — Defining Invariant (deliberately small)

1. **Design composition on a canvas** — the user assembles multiple visual elements (drawn shapes, text, imported images) into a composed design, with free placement, stacking, and alignment. Remove → painting app / photo editor / simple drawing tool.
2. **Editable object state** — elements remain discrete, individually selectable and re-editable objects; the design persists as a re-editable document (not baked into flat pixels). Remove → destructive raster editor or one-shot generator.
3. **User-composed, editing-first** — the first pass is composed by the user through direct manipulation; the application is an instrument the user operates. Remove → AI Design Generator.
4. **Finished design output** — the composition can be finished and rendered out as usable artwork (export/print/publish) for real-world design purposes. Remove → ideation whiteboard / mockup toy.

Historical check (§24): Illustrator (1985), CorelDRAW (1989), FreeHand, Xara Studio (1990s) — all single-user desktop applications composing multi-element vector/text/image designs with export, before cloud/subscription/AI/web existed. The L0 contains none of those modern specifics. Early consumer "print studio" products (template-driven greeting-card makers) do NOT satisfy L0 property 3/1 (no freeform composition) — correctly excluded as ancestors of the Template-based Design Platform. The definition is delivery-agnostic (desktop/web), licensing-agnostic, and AI-agnostic.

### L1 — Common Mature Structure (cross-product, layer B)

- vector drawing toolset (shape tools, Bézier/curve editing, shaping operations)
- typography tools (text objects, font handling, text effects, text-on-path)
- layers/objects panel with stacking order; grouping; isolation modes
- alignment/distribution, rulers, grids, guides, snapping
- color system: palettes/swatches, fills (solid/gradient/pattern/mesh), outlines, transparency
- effects: shadows, bevels, contours, blends, envelopes/distortion
- non-destructive/live effects and styles (object styles, text styles)
- bitmap handling: import, placement, basic editing, bitmap-to-vector tracing
- multi-page documents / artboards (depth varies)
- native document format + import/export of standard formats (image, vector, PDF)
- color modes RGB/CMYK; print-production controls at the professional pole (color management, spot colors, separation, PDF/X)
- templates and bundled content libraries (clipart, fonts, fills)
- font management (companion app or built-in)
- current-generation AI assistance (generation, background removal, masking) — common in 2026 products, absent in older generations

### L2 — Variant / Optional Structure

- web design/publishing capability (Xara pillar; absent in CorelDRAW proper)
- PDF editing as a first-class pillar (Xara)
- companion-app packaging (photo editor, font manager, screen capture as separate apps in a suite) vs single all-in-one application
- browser-delivered editing (CorelDRAW Web/Go; Xara Cloud companion)
- cloud storage/collaboration features (subscription-tier gated in the sample; the collaboration-first pole is a different Type)
- industry vertical tuning: sign-making/large-format, apparel/textile, vehicle wraps, laser/engraving, flags/embroidery
- licensing models: subscription / perpetual / maintenance / freemium
- platform: Windows/Mac desktop, web, tablet
- AI credit metering and model choice

### L3 — Vendor-specific (research notes only)

- Corel: PowerTRACE, CorelDRAW Web, Corel Font Manager, CAPTURE, "dockers" panel terminology, CDR/CDT formats, Multipage View, Focus Mode, AI Generate with named models (Flux, Stable Diffusion, Nano Banana), 2,000 monthly AI credits (subscription), Pantone integration "free of charge", specific content counts (7,000 clipart, 1,000 photos, 1,700 Google Fonts families, 200+ templates), format lists (~10/~70/~100 by tier), 15-day trials
- Xara: Live Effects, Live Copies, ClipView, Magic Erase, Magic Undo (undo of saved photos), Solo mode, document auto-resize, "Replaces…" competitive framing, PDF/X export profiles (Draft/Email/High Quality/Commercial Printing), Illustrator-9-onwards import compatibility claim, "up to ten times smaller" file-size claim, 130+ photo filters, 240+ website templates, 30+ import/export formats
- Adobe: Creative Cloud packaging; Image Trace (name per Corel's guide); artboards (market-attested, not operationally claimed)
- Serif: personas concept (from memory — NOT asserted anywhere)

## Rejected Findings

- **"Graphic design application = vector graphics editor"** — rejected as a merge. The market uses the labels interchangeably for the same product family (Corel's own materials do both), but the directory holds separate leaves and the center-of-gravity distinction (composition of design deliverables vs drawing craft) is real and policed in product framing (CorelDRAW: "vector illustration **and page layout**" inside a "graphic design" suite; Xara separates "Illustration" from "Desktop publishing" pillars). Held as adjacent Types with a documented gradient.
- **"Multi-page layout is part of the defining core"** — rejected. Single-page design (logo, icon, social graphic) is fully within the Type; multi-page is common mature structure with varying depth (CorelDRAW multipage view; Xara DTP pillar; Illustrator artboards). Making pagination core would collapse this Type into Desktop Publishing.
- **"Templates are defining"** — rejected. All sampled products ship templates, but as optional starting points; the organizing structure is freeform composition. Template-first products are the sibling Type (Template-based Design Platform). Corel itself positions its beginner web app against "template-based alternatives" on vector-editing depth.
- **"Generative AI is defining"** — rejected. AI features are current-generation additions, credit-metered, and absent from the historical sample; the editing-first center is unchanged.
- **"Cloud collaboration is defining"** — rejected. In the sampled products collaboration/cloud features are subscription-tier extras or companion services; the collaboration-first pole (shared multi-user files as the unit of work) is the Collaborative Design Platform Type.
- **"Raster editing capability disqualifies design applications from having a raster sibling"** — rejected as a boundary confusion: the presence of raster capability is L1/L2; the *center* (composition vs pixel manipulation) decides the Type.

## Boundary Findings

| Neighboring Type | Judgment | "Remove what → becomes the other" |
|---|---|---|
| Vector Graphics Editor (04.03) | **Sharpest seam; gradient.** Same flagship products straddle both labels (Corel's materials use "vector graphics software" and "graphic design software" for the same family). Discriminator: center of gravity — composing design deliverables (mixed elements, typography, layout, output for communication) vs precision vector drawing craft. | Strip design-deliverable/layout/typography semantics, keep pure geometry drawing → vector editor |
| Illustration Application (04.03) | Adjacent gradient. Artwork/expressive creation vs design composition for communication deliverables; same tools serve both (Corel lists "illustration and fine art" as an industry). | Remove deliverable/communication framing, center expressive artwork → illustration |
| Template-based Design Platform (04.01) | Adjacent sibling. Origin of the first pass: browsed pre-made compositions constrained for non-designers vs blank/freeform composition (templates as optional starters). Corel positions its beginner web app as having "more vector editing capabilities than many template-based alternatives"; its guide distinguishes Canva as template/browser-based. | Make browsed templates the organizing structure and constrain editing for non-designers → template platform |
| Collaborative Design Platform (04.01) | **Ratifies the sibling's gradient from this side.** Sampled products are single-user design documents; cloud/web surfaces (CorelDRAW Web, Xara Cloud) are distribution/companion conveniences, not shared multi-user working files. | Make the shared multi-user file the unit of work → collaborative design platform |
| Raster Image Editor (04.02) | Adjacent. Raster editing is one capability inside the design application (companion app in Corel's suite; integrated pillar in Xara). The raster editor centers pixel manipulation of an existing image. | Strip composition/layout/typography semantics, keep pixel editing → raster editor |
| Desktop Publishing Application (04.17) | Adjacent gradient. Both sampled products include page-layout capability; DTP centers multi-page text-centric publication assembly with text flow/reflow; the design application centers the composition (which may span pages). | Center long-document text flow and publication assembly → DTP |
| AI Design Generator (04.20) | **Ratifies the sibling's gradient from this side.** Who composes the first pass: user (editing-first) vs system (generation-first). Sampled products embed generation as a credit-metered capability (Corel AI Generate; Xara AI-help) without changing the center. | Make described-intent machine composition the primary loop → AI design generator |
| UI Design Application (04.15) | Adjacent (conceptual; not directly researched this pass). Target artifact: user interfaces vs general design deliverables. | Constrain the artifact to UI screens/components → UI design application |
| Presentation Application | Distinct (conceptual). Slides are page-like but deck/screen-delivery-oriented with content-driven structure. | Swap design deliverables for slide decks → presentation app |
| Collaborative Canvas / Digital Whiteboard (03.05) | Distinct (consistent with the sibling pass). Ideation surfaces lack production fidelity (layers/components/output machinery). | Strip production output machinery → whiteboard |

## Taxonomy Issues (for STATUS.md Boundary Issues)

1. **vs vector-graphics-editor (04.03, unprocessed): the market does not cleanly separate the two labels.** Corel's own official materials use "vector graphics software" as the category name while the product pages self-label "graphic design software"; the flagship products (Illustrator, CorelDRAW) are cited under both labels across the market. The directory's split is defensible only as a center-of-gravity split (composition of design deliverables vs drawing craft). Joint review recommended when vector-graphics-editor is processed; candidate outcomes: keep-both with the center-of-gravity seam (this pass's framing) or present the two leaves as one family with two named centers.
2. **Discharges the collaborative-design-platform pass's gradient flag from this side:** confirmed — the sampled graphic design products are single-user design documents; their web/cloud surfaces are distribution conveniences. The seam (shared multi-user file as unit of work vs distribution convenience) holds.
3. **Discharges the ai-design-generator pass's gradient flag from this side:** confirmed — editing-first vs generation-first; generation embedded as a capability does not flip the center.
4. **04.01 three-way split ratified:** editing-first freeform (this leaf) / template-first (Template-based Design Platform) / collaboration-first (Collaborative Design Platform) is a coherent partition; flag for the template-based-design-platform pass to ratify from its side.
5. **Consumer/browser pole drift watch:** CorelDRAW Go (beginner web app, millions of assets, "virtually no learning curve") sits deliberately close to the template-platform pole while keeping freeform vector editing as its differentiator — market evidence that the editing-first/template-first seam is the load-bearing one, not surface or audience.

## Uncertainties

- Adobe Illustrator and Affinity Designer documentation was unreachable; no operational claims are made about them. Their inclusion as representative products rests on widely-attested market position plus Corel's official educational guide (competitor-published, layer B).
- The free/open-source pole (Inkscape) and the technical-illustration-flavored pole (Canvas X Draw) were not directly evidenced; the L0/L1 claims rest on the two directly-researched products plus anchors.
- Exact feature depth of the professional pole (spot-color handling, prepress dialogs, artboard semantics) is evidenced only at the marketing/feature-list level for Corel and Xara; no step-level operational claims are made beyond the one official tutorial observed.
- Whether any market segment sells a "graphic design application" without vector drawing capability — none found in the sample; if one exists, the vector-toolset item in L1 would need re-grading (it is deliberately NOT in L0).

## Final Synthesis

A Graphic Design Application is an editing-first application in which a user composes visual designs — multi-element compositions of drawn shapes, text, and images on a design canvas — as persistent, editable design documents, and finishes them into usable design artwork (logos, posters, flyers, packaging, signage, social graphics, brand collateral) for print or digital delivery.

The defining core is small: design composition on a canvas + editable object state + user-composed (editing-first) + finished design output. Everything else commonly associated — vector toolsets, typography depth, layers, effects, styles, multi-page layout, color management, templates, content libraries, AI assistance, web delivery, tier ladders — is standard mature structure or variant capability, not definition.

The Type's center of gravity is the composition of design deliverables for visual communication. The same market products often also serve vector-drawing craft (Vector Graphics Editor), artwork creation (Illustration Application), page assembly (Desktop Publishing), and pixel editing (Raster Image Editor) — these are gradients across shared tooling, not identical Types. The directory's 04.01 partition (editing-first / template-first / collaboration-first) is coherent and ratified from this side.
