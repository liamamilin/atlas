# Research Notes — Page Layout Application

Research date: 2026-09-08
Leaf: Page Layout Application (DIRECTORY §04.17 Publishing & Layout)
Slug: page-layout-application

## Research Goal

Understand what a Page Layout Application is as an Application Type — its core object model, defining workflow, output obligations, and boundaries — from real products' official documentation. Additionally, this pass carries a mandatory joint review: the already-processed sibling leaf **Desktop Publishing Application** (researched 2026-09-07) left an ALIAS flag in STATUS.md Boundary Issues stating that the two directory labels appear to name one product category, with direct vendor evidence (Quark marketing one product under both labels), and recommended joint review when this leaf is processed. Candidate outcomes recorded by the sibling: merge as one Type, or keep-both with explicit alias cross-reference.

## Initial Boundary

Initial hypothesis before research:

- Core use: assembling text and graphics into multi-page layouts for print/digital publication with precise typographic control — i.e., the same territory as Desktop Publishing Application.
- Users: publication designers, production artists, publishers, in-house marketing, small businesses.
- Nearest neighbors: Desktop Publishing Application (sibling — suspected alias), Professional Typesetting Application (sibling — different mechanism?), Document Editor / word processor, Graphic Design Application, Template-based Design Platform, Presentation Application, Vector Graphics Editor.
- Known term ambiguity: "page layout" is used in two senses in the market — (1) the application category (InDesign/QuarkXPress-class software), and (2) a document model inside word processors (Apple Pages documents "page layout documents" as a document type alongside "word-processing documents"). The directory leaf must be sense (1); sense (2) belongs to the Document Editor Type.

## Research Questions

1. Is "Page Layout Application" the same Type as "Desktop Publishing Application" (alias), or structurally distinct? (joint review — mandatory)
2. What is the core object model when documented from the page-layout angle? (document/pages/spreads, frames, text flow, masters, styles)
3. What is the canonical workflow from empty document to delivered publication?
4. What output obligations define the Type?
5. What distinguishes it from the word processor (including word processors that contain a "page layout" document mode), the graphic design application, the typesetting system, the template-based design platform?
6. What variants exist?
7. How do the two market senses of the term "page layout" relate, and which sense does this leaf name?

## Representative Products

Selected for market representativeness, different philosophies, different customer tiers. Because the alias hypothesis predicts the same product category as the sibling pass, the sample is the same category sampled independently:

| Product | Pole | Why selected |
|---|---|---|
| Adobe InDesign | current professional market leader | market anchor; docs unreachable this pass (see Sources) |
| QuarkXPress (Quark Software) | legacy professional leader, print+digital | original standard-bearer; product page + dedicated page-layout capability page reachable fresh this pass; deep Tier-1 user-guide evidence exists from the sibling pass (2026-09-07) |
| Affinity Publisher | modern challenger, one-time purchase | market anchor; docs unreachable this pass (see Sources) |
| Scribus | open-source community | free/open-source pole; official repository README reachable fresh |
| Microsoft Publisher | consumer/SMB, Office-bundled | the mass-market template-driven pole; official retirement notice reachable fresh |

## Sources

Fetched 2026-09-08 (this pass):

1. QuarkXPress product page — https://www.quark.com/products/quarkxpress (Tier 2, positioning; fetched OK)
2. QuarkXPress "Page Layouts" capability page — https://www.quark.com/page-layouts (Tier 2, capability positioning; fetched OK)
3. Scribus official repository README — https://github.com/scribusproject/scribus ("Scribus - Open Source Desktop Publishing") (Tier 1-equivalent project surface; fetched OK)
4. Microsoft — "Microsoft Publisher will no longer be supported after October 2026" — https://support.microsoft.com/en-us/publisher (Tier 1 support; fetched OK)
5. Apple — "Intro to word-processing and page layout documents in Pages on Mac" — https://support.apple.com/guide/pages/word-processing-or-page-layout-tan6129a1862/mac (Tier 1 user guide; fetched OK) — used for term disambiguation, not as evidence about this Type's products

Prior atlas evidence relied upon (recorded in the sibling pass's research notes, research/desktop-publishing-application.md, fetched 2026-09-07):

6. QuarkXPress 2026 User Guide (Tier 1) — chapters "Projects and Layouts", "Text and Typography", "Output" — the deepest operational evidence for the Type's core model; re-verified at product-page level this pass
7. QuarkXPress documentation index (Tier 1 index)

Access limitations (recorded per evidence rules):

- **Adobe InDesign**: helpx.adobe.com/indesign/user-guide.html timed out; www.adobe.com/products/indesign.html timed out → abandoned after 2 failures this pass (sibling pass additionally recorded 3+2 failures on 2026-09-07). **No direct Adobe evidence in either pass.** InDesign appears only through Quark's official interop documentation (IDML/INDD import/export, documented in the sibling pass's Tier-1 fetches) and as market context.
- **Affinity Publisher**: affinity.serif.com/en-us/publisher/ served a Canva-owned "Unsupported client" browser-check page (directly observed; consistent with the sibling pass's observation of a redirect to Canva infrastructure after Canva's 2024 acquisition of Serif — ownership not independently verified). **No direct Affinity evidence in either pass.** No claims made.
- No pricing, numeric limits, or default values from unreachable sources are used anywhere.

## Product Observations

### QuarkXPress (evidence layer A — direct, fresh this pass at product-page level; deep Tier-1 user-guide evidence from sibling pass 2026-09-07)

**The alias evidence (fresh, product page):** The page title is "QuarkXPress Desktop Publishing and Page Layout Software". Body copy: "QuarkXPress is the original and powerful desktop publishing software… trusted today by creative professionals for brilliant print and digital design" and later "Brilliant print and digital content design begins with QuarkXPress, the original desktop publishing and page layout software for creative professionals." One product carries both labels in its own marketing title and body.

**The page-layout capability evidence (fresh, dedicated capability page):** Quark operates a dedicated "Page Layouts" page for the same product: "Produce stunning page layouts for any medium… design stunning layouts for brochures, magazines, books and more… Whether it's for print or digital". It calls the product "QuarkXPress page layout software" and "The world's most powerful page layout and digital publishing software package". Customer quotes on the same page: "by far a best tool for Page Layouts"; "set type for page layout applications such as magazines, books, or flyers"; "the best when it comes to page layout and typesetting design". Use-case pages: brochure layout design, book layout design, magazine layout design, newspaper layout design.

**Page-layout mechanics documented on the capability page (fresh):**

- style sheets ("pre-built and custom style sheets… well-organized, consistent, and uniform… especially when working on large or complex projects")
- import/conversion of InDesign and PDF files, "importing long documents with up to 10,000 pages to IDML, INDD and PDFs formats", brand themes (color, styles, formatting) carried across migration
- synchronized text edits across layouts/assets
- "Cross-media publishing in one file… print, online, tablet and mobile formats in many sizes and all within one file"
- all-in-one positioning: "creating page layouts, adjusting images, and producing exquisite graphics" in one place
- master-page image grids ("Enhanced Image Grids on Master Page Layouts… large-scale, multi-page documents like catalogs, lookbooks or event albums with heavy photo layouts")
- variable fonts, LaTeX/MathML equations, AI text assistant and AI font pairing (2026-era features), paper color previews, "Paste Into" container masking

**Deep core model (from the sibling pass's Tier-1 user-guide fetch, 2026-09-07 — relied on here as the operational baseline):** Project → Layouts (Print/Digital) → Pages/Spreads; master pages with automatic text boxes and master guides/grids; pasteboard; column/margin/ruler guides with snapping and dynamic alignment; text boxes/picture boxes/no-content boxes/lines/tables; stories flowing through linked boxes with overflow indication and auto page insertion; text import from Word/Markdown/plain text with style mapping; deep typography (kerning/tracking tables, H&J with exception files, widow/orphan control, OpenType/variable/color fonts, East Asian grids, footnotes/endnotes, GREP find/change); pictures imported and *linked* with output-time warnings; color (PANTONE spot, composite vs separations, ICC); layers; output chapter (PPD/print controls, marks, bleed, flattening, PDF/X-A-UA verification, EPS/PostScript/image/ePub/HTML5 export, Collect for Output packaging with fonts+links+profiles+report, output styles); collaboration (Job Jackets, Composition Zones, CopyDesk, Notes, Redline); scripting (AppleScript, QX.js, XTensions/XDK); IDML interchange both directions.

### Adobe InDesign (evidence layer B — indirect via Quark's official interop docs from the sibling pass; no direct Adobe source in either pass)

- Quark's official documentation treats InDesign as the dominant interchange counterpart: IDML import (CS5/CS6/CC exports), bulk InDesign→QXP conversion, INDD open requiring local InDesign, IDML Package export with fonts+links. IDML mapping notes name InDesign-side structures: style sheets, colors, anchored items, table/cell/object styles, footnotes, conditional styles, endnotes, TOC, grid styles, notes, interactivity.
- Inference (layer C): InDesign is the reference implementation of the same core model and the de facto interchange hub of the category. The professional market uses "page layout application" as the functional term for this class of software. No InDesign-specific feature claims are made.

### Affinity Publisher (no direct evidence)

- Official surfaces unreachable in both passes (Canva browser-check block observed fresh this pass). Listed as market context only. No claims.

### Scribus (evidence layer A — direct, fresh, official repository README)

- Self-identification: "Scribus - Open Source Desktop Publishing" — the open-source pole self-labels with the sibling term, confirming one category spanning both labels.
- Text frames with direct linking ("add ability to link selected text frames directly") — the threading mechanism in the open-source pole.
- Complex text layout: RTL (Arabic, Persian, Urdu, Hebrew), BiDi, Indic scripts, 500+ languages, OpenType features, customizable hyphenation character; faster loading/rendering of long docs.
- Community delivery model: SVN repository, bug tracker, wiki, forums, mailing lists.

### Microsoft Publisher (evidence layer A — direct, fresh, Tier 1 support)

- Official retirement notice: Publisher reaches end of life October 2026; removed from Microsoft 365 after Oct 1, 2026; perpetual versions unsupported after Oct 13, 2026; files should be converted to PDF (File > Save As > PDF; bulk PowerShell script provided) or PDF→Word.
- Microsoft's own scenario list for the product: "creating professionally branded templates, printing envelopes and labels, and producing customized calendars, business cards, and programs"; recommended-replacement table routes ads, flyers, brochures, banners/signs/posters, certificates, business cards, invoices/forms, calendars, envelopes, labels, letterhead, newsletters, programs, greeting cards to Word/PowerPoint + Microsoft Create templates.
- Confirms the consumer/SMB pole of the Type: small-circulation, template-driven publications produced on desktop Office environments, output as print/PDF — and the market trend of this pole being absorbed by word processors + template galleries.

### Apple Pages (evidence layer A — direct, fresh; used for term disambiguation only)

- Apple's official user guide distinguishes two document types inside Pages: *word-processing* documents ("a body text area where you type, the text flows from one page to the next, with new pages created automatically") and *page layout* documents ("like a canvas that you add text boxes, images, and other objects to, then arrange the objects on the page however you like… there is no body text area; to add text you need to add a text box… New pages must be added manually"). The mode is a per-document setting (Document Body checkbox) and documents can be converted between the two. Word-processing documents are "great for reports and letters, while page layout documents are better for flyers or posters".
- Interpretation: this is the second market sense of "page layout" — a **document model** (canvas + placed frames + manual pages) that exists *inside* a word-processor product. It is not an application category. Notably, the document model it describes is the same frame-canvas model this Type uses — evidence that the *model* is distinct from the *application Type*, and that the Type boundary is drawn at the application level (center of gravity), not the document level.

## Cross-product Comparison

| Dimension | QuarkXPress | Adobe InDesign (indirect) | Scribus | MS Publisher |
|---|---|---|---|---|
| Self-label | "desktop publishing and page layout software" (both labels, one product) | page layout application (market usage) | "Open Source Desktop Publishing" | Publisher (DTP app in Office) |
| Document container | Project → Layouts → Pages | Document (per IDML mapping) | Document | Publication (.pub) |
| Free-placed frames | text/picture/no-content boxes, lines, tables | frames (per IDML mapping) | text frames (+ direct linking) | text/picture frames (scenario evidence) |
| Text flow | linked boxes = one story; overflow flag; auto page insertion | threaded frames (IDML mapping) | linked text frames | connected frames (pole behavior) |
| Master pages | yes (automatic text box, master guides/grids, image grids on masters) | yes (IDML mapping implies) | not directly evidenced | not directly evidenced |
| Styles | paragraph/character/item, conditional, groups | style sheets (IDML mapping) | not directly evidenced | not directly evidenced |
| Typography depth | extreme (H&J, kerning/tracking tables, OpenType/variable/color fonts, East Asian grids) | professional | strong RTL/BiDi/Indic, OpenType, hyphenation | basic (consumer pole) |
| Color | CMYK/spot (Pantone), separations, ICC | professional | not directly evidenced | not directly evidenced |
| Output | print w/ PPD/marks/bleed/separations; PDF (X/A/UA); EPS; images; ePub; HTML5; cross-media in one file | PDF/print (market usage) | print/PDF (DTP identity; specifics not fetched) | print; Save As PDF |
| Handoff | Collect for Output (fonts/links/profiles/report); usage checks | package (market usage) | n/a | PDF conversion guidance (retirement) |
| Customer tier | professional + enterprise publishing | professional | community/prosumer | consumer/SMB |
| Business model | perpetual + subscription | subscription (market usage) | free open source | bundled in Microsoft 365 (retiring Oct 2026) |

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

A Page Layout Application is recognizable by exactly this structure:

1. **Multi-page paginated document** — a fixed-geometry page set (with optional spreads) as the container of work.
2. **Free-placed layout objects** — text and picture frames positioned anywhere on a page canvas (pasteboard), not in a linear text stream.
3. **Text as reflowing stories** — text lives in frames as flowable content that threads across linked frames and pages, reflowing when content or geometry changes.
4. **Paginated publication output** — the deliverable is a paginated artifact for print or print-equivalent distribution (print engine output, PDF).

Remove free-placed frames + flowing text → word processor. Remove pagination/multi-page publication orientation → graphic design canvas. Remove frames (keep markup) → typesetting system. Remove output orientation → generic canvas editor.

**Joint-review note (the alias question):** this L0 is identical in structure to the Desktop Publishing Application L0 derived independently by the sibling pass from the same category's products. The two directory leaves therefore name one Application Type. Direct fresh evidence: one vendor markets one product under both labels in the same page title ("Desktop Publishing and Page Layout Software") and operates a dedicated "Page Layouts" capability page for it; the open-source pole self-labels "Desktop Publishing" while the professional market calls the same class "page layout applications". No structural difference was found in either pass.

**Historical / market-sample check (§24 analog):** Aldus PageMaker (1985, the product that launched "desktop publishing"), Ventura Publisher, early QuarkXPress, MS Publisher 1.0, and Scribus all satisfy the four properties; none require cloud, subscription, styles, or master pages to qualify. The L0 holds across eras and regions. The check also runs in the other direction: Apple Pages' "page layout document" mode (canvas + text boxes + manual pages, convertible per document) satisfies the *document-model* legs but is a mode inside a word processor, not an application whose center of gravity is page assembly — the Type boundary is drawn at the application level. This confirms the L0 is not over-fitted to the professional desktop product pattern while still excluding look-alike surfaces.

### L1 — Common Mature Structure

Present in essentially all mature professional products (Quark direct; InDesign via IDML mapping; Scribus partially evidenced):

- master pages / parent pages (reusable page templates; automatic text frames; master guides/grids; image grids on masters in one product)
- guides & grids: margins, columns, ruler guides, baseline grid, smart/dynamic alignment, snapping
- style sheets: paragraph + character styles; object/item styles; conditional styles in some
- professional typography: kerning, tracking, hyphenation & justification, widow/orphan control, OpenType features (variable fonts era-current), drop caps, paragraph rules, text on a path, anchored (inline) objects
- text wrap / runaround around objects
- tables as layout objects
- layers
- linked asset management: placed pictures remain linked; usage/links panels; modified/missing warnings at output time
- long-document machinery: footnotes/endnotes, cross references, TOC/indexes, very large page counts
- color management: CMYK + spot color systems, swatch libraries, ICC profiles
- output-readiness machinery: font/picture usage checks, PDF print-standard verification, packaging/collect (document + fonts + links + profiles + report)
- print production controls: bleed, crop/registration marks, composite vs separations, transparency flattening
- PDF export as the universal interchange output
- find/change incl. pattern-based (GREP-class) search; spell check
- word-processor import filters (styles, footnotes, tables carried in)

### L2 — Variant / Optional Structure

- digital output channels: ePub (fixed/reflow), HTML5 publications, interactive PDF, native-app export; cross-media output from one file
- consumer/SMB template pole: template-first small publications (cards, flyers, labels, calendars), simplified controls (MS Publisher pattern; contracting — retirement announced Oct 2026, scenarios routed to word processors + template galleries)
- editorial collaboration layer: copy-editing without layout alteration, tracked changes/notes, shared job specifications (CopyDesk/InCopy-class, Job Jackets-class)
- data merge / variable-data printing / web-to-print automation
- multi-layout projects, nested projects, synchronized content across layouts
- East Asian typography sets (design grids, rubi, hanging punctuation)
- scripting/automation (AppleScript/JS-class) and plugin/extension architectures
- interchange formats (IDML-class) as the migration/interop substrate
- bundled image editing / illustration / AI assistance ("all-in-one publishing" positioning; era-current)

### L3 — Vendor-specific (research notes only)

- QuarkXPress: Project/Layout two-level container; Job Jackets/Job Tickets; Composition Zones; CopyDesk add-on; XPress Tags; XTensions/XDK; QX.js; QuarkXPress Server (web-to-print/variable data); ImageGrid; Flex layouts; Content Variables; Redline; 10,000-page layout limit; 224"×224" max page; IDML/INDD import + bulk conversion; LaTeX/MathML equations; Quarky AI assistant; AI font pairing (Google Fonts); paper color previews; Paste Into; Pantone libraries included; perpetual + subscription licensing.
- Microsoft Publisher: .pub format; Office-suite bundling; retirement timeline (Oct 1 / Oct 13, 2026); PowerShell bulk PDF conversion script; replacement mapping to Word/PowerPoint/Microsoft Create.
- Adobe InDesign: IDML as interchange substrate; CS5/CS6/CC lineage (as documented by Quark); InCopy/InDesign editorial ecosystem (market usage, unverified).
- Scribus: GPL open source; SVN-based development; community support model.
- Apple Pages: page-layout document mode (Document Body checkbox; conversion between word-processing and page-layout document types) — an L3 fact of the Document Editor Type, recorded here as disambiguation.

## Rejected Findings (not promoted to core)

- **"Page Layout Application is a distinct Type from Desktop Publishing Application"** — rejected. Direct vendor evidence (one product, both labels in one title; dedicated page-layout capability page for the DTP product; open-source pole self-labeling DTP while market uses page-layout for the same class). The two leaves are aliases; joint review discharged with keep-both + cross-reference (directory merge out of scope for a leaf pass).
- **"Page layout = any application that can arrange objects on pages"** — rejected. Presentation applications, whiteboards, and template design platforms arrange objects but lack the flowing-story model and the paginated publication/production orientation.
- **"Page layout requires print production machinery (separations, marks, packaging)"** — rejected as definitional; the consumer pole (Publisher) operates without it. Production machinery is professional-pole L1.
- **"Page layout requires master pages / style sheets"** — rejected; L1. Older products and simple documents work without them.
- **"Page layout is template-driven"** — rejected; that is the consumer-pole variant (overlapping Template-based Design Platform). The professional pole is layout-first, not template-first.
- **"The Pages page-layout document mode is an instance of this Type"** — rejected; it is a document mode inside a word-processor product (different application, different center of gravity). It does show the frame-canvas *model* is shared, which is why the term collides.
- **"Page layout includes photo editing / illustration"** — rejected as definitional; bundling is vendor positioning ("all-in-one publishing"), not the Type.

## Boundary Findings

| Neighboring Type | Boundary judgment | "Remove what → becomes the other" |
|---|---|---|
| Desktop Publishing Application (sibling leaf) | **Same Type — alias.** Joint review discharged 2026-09-08. One product marketed under both labels; no structural difference in either pass. Keep-both with explicit cross-reference; merge requires a directory edit outside a leaf pass's scope. | n/a — same referent |
| Professional Typesetting Application (sibling leaf) | Adjacent, likely distinct mechanism: typesetting systems compose pages from markup/batch rules (non-interactive), while this Type is interactive WYSIWYG frame layout. Both produce paginated output. Deserves its own research pass; do not merge blindly. | Remove interactive frame manipulation, drive layout from markup → typesetting system |
| Document Editor / Word Processor | Adjacent. Word processor: linear body-text stream, layout secondary, automatic pagination. This Type: layout canvas first, text flows into placed frames, multi-flow multi-frame. Note: word processors may contain a "page layout" document mode (canvas + text boxes + manual pages) — the model appears there, but the application's center of gravity remains the flowing document. | Remove free-placed frames + threading (or demote page assembly to a secondary mode) → word processor |
| Graphic Design Application | Adjacent. Graphic design: single-canvas artwork, objects as artwork. This Type: multi-page text-centric publication assembly with reflow. | Remove pagination + text flow → design canvas |
| Template-based Design Platform | Adjacent. Template-first web canvas, light print production, consumer output. This Type: blank-page layout authoring with production-grade output controls. | Remove production output machinery + frame-level typography → template design platform |
| Presentation Application | Adjacent. Slides are page-like but screen-deck-oriented, linear delivery, no print production chain. | Swap print pagination for deck delivery → presentation app |
| Vector Graphics Editor | Adjacent. Object drawing vs page assembly; this Type places vector art as linked/placed content. | Remove page/flow/publication semantics → vector editor |
| Photo Editor / Raster Image Editor | Complementary. Images are prepared there and placed here as linked content; bundling is vendor positioning, not Type identity. | n/a — different objects entirely |

## Taxonomy Issues (for STATUS.md Boundary Issues)

1. **ALIAS DISCHARGED (joint review with desktop-publishing-application):** the two §04.17 leaves name one Application Type. Fresh direct evidence this pass: Quark's product page title "QuarkXPress Desktop Publishing and Page Layout Software" + dedicated "Page Layouts" capability page for the same product; Scribus self-labels "Open Source Desktop Publishing" while professional-market usage (including Quark's own customer quotes) calls the same class "page layout applications". Recommendation stands: merge as one Type (desktop publishing = historical label, page layout = functional label) at the next directory revision; until then keep-both with explicit alias cross-reference in both documents. This pass cannot edit DIRECTORY.md.
2. **Professional Typesetting Application (§04.17)** remains unprocessed; overlaps on output but differs in authoring mechanism (markup/batch vs interactive frames). Flagged for its own pass by the sibling; re-flagged here.
3. **Term-collision note:** "page layout" also names a document mode inside word processors (Apple-documented). Any future leaf or variant named "page layout" must disambiguate the application category from the document model. No directory change proposed.

## Uncertainties

- InDesign and Affinity Publisher operational details unverified in both passes (sources unreachable). All InDesign statements are limited to ecosystem facts documented by Quark + market-context framing; Affinity carries no claims.
- MS Publisher's internal model (master pages? connected-frame mechanics?) not directly evidenced; the consumer pole is characterized by Microsoft's own scenario list and retirement notice rather than feature documentation.
- Scribus operational depth (output chain, color management) not directly evidenced beyond the README; Scribus claims kept minimal.
- Whether "Professional Typesetting Application" should be a separate Type is unresolved (needs its own pass).
- Exact numeric limits (page counts, page sizes) observed at Quark only; treated as vendor facts, excluded from the final document.
- The Canva/Serif ownership situation is inferred from the observed redirect only; not independently verified; no claims depend on it.

## Final Synthesis

The Page Layout Application is the same Application Type as the Desktop Publishing Application — the interactive page-assembly application of the publishing world — under its modern functional label. Its defining core is small: a multi-page paginated document, free-placed text/picture frames on a pasteboard canvas, text that flows as rethreading stories across frames and pages, and paginated publication output (print/PDF). Everything else the market associates with the category — master pages, style sheets, guides and baseline grids, fine typography controls, layers, color separations, preflight/packaging, PDF standards, long-document machinery, digital output channels, editorial collaboration — is mature standard structure layered on that core, with a professional production pole and a contracting consumer template pole as the main market variants. The term "page layout" has a second, narrower market sense — a document model inside word processors — which must not be confused with the application category. The joint review with the sibling leaf is discharged: alias confirmed, keep-both with cross-reference, merge recommended at directory-revision time.
