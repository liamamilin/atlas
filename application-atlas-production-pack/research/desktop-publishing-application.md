# Research Notes — Desktop Publishing Application

Research date: 2026-09-07
Leaf: Desktop Publishing Application (DIRECTORY §04.17 Publishing & Layout)
Slug: desktop-publishing-application

## Research Goal

Understand what a Desktop Publishing (DTP) Application actually is as an Application Type — its core object model, its defining workflow, its output obligations, and its boundaries against neighboring Types (word processors, graphic design applications, typesetting systems, template-based design platforms) — from real products' official documentation, not from memory or marketing.

## Initial Boundary

Initial hypothesis before research:

- Core use: assembling text and graphics into page layouts for print/digital publication with precise typographic control.
- Users: graphic designers, production artists, publishers, in-house marketing, small businesses, students.
- Nearest neighbors: Page Layout Application (sibling leaf — likely the same thing), Professional Typesetting Application (sibling leaf — possibly a variant), Document Editor / word processor, Graphic Design Application, Vector Graphics Editor, Template-based Design Platform, Presentation Application.
- Likely confusion: "desktop publishing" is a 1985-coined market term; "page layout" is the modern functional term. Same products are marketed under both labels.

## Research Questions

1. What is the core object model? (document/project, pages/spreads, master pages, frames/boxes, text flow, styles, layers, color)
2. How does text work? (frames vs. linear stream; threading/linking; stories; reflow; overflow; auto page insertion)
3. What is the canonical workflow from empty document to delivered publication?
4. What output obligations define the Type? (print, PDF, preflight, packaging, bleed/crop marks, color separations)
5. What distinguishes DTP from a word processor, from a graphic design app, from a typesetting system?
6. What variants exist? (professional vs consumer/SMB pole; long-document vs single-page; print vs digital output)
7. Is "Page Layout Application" a separate Type or an alias?

## Representative Products

Selected for market representativeness, different philosophies, different customer tiers:

| Product | Pole | Why selected |
|---|---|---|
| QuarkXPress (Quark Software) | legacy professional leader, print+digital | original DTP standard-bearer since 1987; deep official user guide reachable |
| Microsoft Publisher | consumer/SMB, Office-bundled | the mass-market template-driven pole; official support docs reachable |
| Scribus | open-source community | free/open-source pole; official project README reachable |
| Adobe InDesign | current professional market leader | included as market anchor; docs unreachable this pass (see Sources) |
| Affinity Publisher | modern challenger, one-time purchase | included as market anchor; docs unreachable this pass (see Sources) |

## Sources

Fetched 2026-09-07:

1. QuarkXPress product page — https://www.quark.com/products/quarkxpress (Tier 2, positioning)
2. QuarkXPress documentation index — https://www.quark.com/support/documentation/quarkxpress/ (Tier 1 index; versions 2015–2026 listed)
3. QuarkXPress 2026 User Guide — https://www.quark.com/documentation/quarkxpress/2026/english/A%20Guide%20to%20QuarkXPress%202026 (Tier 1)
   - Chapter "Projects and Layouts" (fetched in full)
   - Chapter "Text and Typography" (fetched; large, partially read)
   - Chapter "Output" (fetched in full)
4. Microsoft Publisher support — https://support.microsoft.com/en-us/publisher → "Microsoft Publisher will no longer be supported after October 2026" (Tier 1)
5. Scribus official GitHub mirror README — https://github.com/scribusproject/scribus ("Scribus - Open Source Desktop Publishing") (Tier 1-equivalent project surface)

Access limitations (recorded per evidence rules):

- helpx.adobe.com (InDesign User Guide): request timed out ×3 → abandoned. www.adobe.com/products/indesign.html: timed out ×2 → abandoned. **No direct Adobe evidence this pass.** InDesign appears in this research only through Quark's official interop documentation (IDML/INDD import/export) and as market context.
- affinity.help: 403; affinity.serif.com: transport error, then observed redirect to Canva-owned web infrastructure (Canva acquired Serif in 2024 — ownership not independently verified this pass; the redirect itself was directly observed). **No direct Affinity evidence this pass.**
- docs.scribus.net (Scribus online manual): blocked by Anubis anti-bot challenge → abandoned; substituted with the official GitHub mirror README.
- No pricing, numeric limits, or default values from unreachable sources are used anywhere.

## Product Observations

### QuarkXPress 2026 (evidence layer A — direct, Tier 1 user guide)

Positioning (product page): "QuarkXPress Desktop Publishing and Page Layout Software … the original desktop publishing software … refined for over 40 years." The same vendor page uses "desktop publishing" and "page layout" interchangeably for one product — direct evidence the two directory labels name one market category.

Core model (User Guide):

- **Project / Layout**: "QuarkXPress files are referred to as *projects*, and each project contains one or more *layouts*." Layout types: Print and Digital (Fixed or Flex). One project can hold multiple layouts (e.g., same content in US Letter and A4). Layout-level facts: up to 10,000 pages per layout; page size up to 224"×224" (112"×224" two-page spread) — precise numbers are vendor facts, kept here only.
- **Pages/spreads**: Facing Pages option creates spreads; odd-page-left/right controls; page count set at creation.
- **Master pages**: New Project offers an "Automatic Text Box check box [that] lets you add a text box to the default master page"; "Master Guides & Grid dialog box" configures column/margin guides on master pages; design grids configurable on "master page grids and text box grids".
- **Pasteboard**: work area around pages; size adjustable (default 0.5" vertical historically — vendor fact).
- **Guides**: column and margin guides, ruler guides (drag from rulers), snapping with configurable Snap Distance, Dynamic Guides (smart alignment to item centers/edges, page center, equal dimensions/spacing).
- **Objects**: "Boxes, Lines, and Tables" chapter; "Native QuarkXPress Objects" chapter; text boxes, picture boxes, no-content boxes, lines; Item Styles chapter (object-level styles).
- **Text flow / stories**: "A *story* is all of the text in a text box. If a series of boxes is linked, all of the text in all of the boxes is a single story." Overflow symbol displays when text doesn't fit; Fit Box to Text / Fit Text to Box / AutoFit Text; **Auto Page Insertion**: "pages are inserted (when you import text into an automatic text box) as necessary to contain the text."
- **Text import**: from Word (.docx filter with style sheets, footnotes, tables, hyperlinks, inline pictures), Markdown (mapped to style sheets via Style Groups), XPress Tags (vendor markup), plain text with encoding; Convert Quotes (typographer's quotes).
- **Typography**: character attributes (font, size, type styles, color/shade/opacity, scale, baseline shift, stroke); paragraph attributes (alignment, indents, leading, space before/after, tabs, **widow and orphan control**, **column flow**); kerning (manual/automatic), tracking tables, **hyphenation and justification (H&J)** with exception files; style sheets (paragraph, character), conditional styles, style groups; bullets/numbering; drop caps; rules above/below paragraphs; text runaround (wrap around items/pictures/lines/text boxes, editable runaround path); text paths; anchored boxes; baseline grid; vertical alignment; insets; story direction; OpenType styles/ligatures/stylistic sets; variable fonts; color fonts (COLRv1); font manager, font usage, font fallback; East Asian typography (design grids, rubi, Mojigumi, hanging characters); footnotes/endnotes with numbering styles; Find/Change incl. GREP and attribute-based search; spell check (live + palette, Hunspell); word count.
- **Pictures**: Pictures chapter; pictures are imported and *linked* — "A path to a picture is established when you import a picture… If a picture is moved or changed after it is imported, the application warns you when you execute the Output command… or the Collect for Output command." PDF pages can be imported into picture boxes.
- **Color**: Color/Opacity/Drop Shadows chapter; PANTONE and other spot-color systems; composite vs separations output; color management setups (source/output setups, ICC profiles).
- **Layers**: layers exist per layout; Layers pane in Print/PDF output controls which layers output.
- **Output** (chapter read in full):
  - Print dialog panes: Device (PPD selection, resolution, paper offset/page gap for imagesetters), Pages (orientation, tiling, thumbnails, page flip), Pictures (Normal / Low Resolution / Rough output), Fonts (font download control), Color (Composite vs Separations; In-RIP separations; composite setups: Grayscale / Composite RGB / Composite CMYK / Composite CMYK and Spot / As Is), Registration Marks (crop marks, registration marks, bleed marks), Layers, Bleed (symmetric/asymmetric; Page Items; Clip at Bleed Edge), Transparency (flattening resolution controls), JDF, Advanced (PostScript level), Summary.
  - Export formats: PDF (with PDF/X-1a / PDF/X-3 / PDF/X-4 verification; PDF/A-1b/2b/2u/3b archive standards; PDF/UA tagged accessible PDF), EPS, PostScript, JPEG/PNG/TIFF (image export with resolution/quality), HTML5 Publications, ePub (fixed-layout and reflow), Article, IDML/IDML Package (InDesign interchange).
  - **Collect for Output**: copies project + linked pictures + ICC color profiles + fonts (screen/printer) + interactivity assets + generates a report; Usage dialog checks font/picture status ("display a status of OK") before output.
  - Output styles: reusable captured settings for print/PDF/EPS/image/ePub/HTML5 output.
  - Trapping (overprint/knockout controls in Colors palette); transparency flattening explained as output-stream-only process.
- **Collaboration**: Job Jackets (shared job specifications, JDF output), Composition Zones (multiple people working on one publication simultaneously), Notes, Redline (tracked text changes), CopyDesk add-on ("content components … edited without altering an established layout … writers and editors can amend text, place, crop or rotate images").
- **Extensibility/automation**: XTensions modules; AppleScript; QX.js JavaScript scripting; XTensions Developer Kit.
- **Interop**: IDML import (from InDesign CS5/CS6/CC exports; INDD open requires local InDesign install), bulk InDesign→QXP conversion, IDML export/Package export; nested projects (import one project into another like an image, Edit Original, Update); import from Word/Excel/Illustrator/Photoshop.
- **Digital publishing**: Digital layouts (Fixed/Flex), HTML5 Publications, ePub, native-app export ("Digital Publishing with QuarkXPress" dedicated guide).

### Microsoft Publisher (evidence layer A — direct, Tier 1 support)

- Official retirement notice (support.microsoft.com): Publisher reaches end of life October 2026; removed from Microsoft 365; perpetual versions unsupported after Oct 13, 2026. Files (.pub) should be converted to PDF (File > Save As > PDF) or PDF→Word before retirement.
- Scenario space (Microsoft's own list of "common Publisher scenarios"): "creating professionally branded templates, printing envelopes and labels, and producing customized calendars, business cards, and programs"; recommended-replacement table lists: ads, flyers, brochures, banners/signs/posters, certificates, business cards, invoices/applications/forms, calendars, envelopes, labels, letterhead, newsletters, programs/folded paper projects, greeting cards.
- This confirms the consumer/SMB pole of the Type: small-circulation, template-driven publications (cards, flyers, newsletters, labels) produced on desktop Office environments, output as print/PDF.
- Microsoft's replacement guidance routes these scenarios to Word/PowerPoint + Microsoft Create templates — evidence that the consumer pole of DTP is being absorbed by word processors + template libraries (market trend, not a Type boundary change).

### Scribus (evidence layer A — direct, official project README)

- Self-identification: "Scribus - Open Source Desktop Publishing."
- Text frames: "add ability to link selected text frames directly" — direct evidence of frame linking (threading) in the open-source pole.
- Complex text layout: RTL languages (Arabic, Persian, Urdu, Hebrew), bidirectional text, Indic scripts, 500+ languages, OpenType font features, customizable hyphenation character; "Loading and render long docs are faster."
- Community infrastructure: SVN repository, bug tracker, wiki, forums, mailing lists (typical open-source delivery; no vendor support org).

### Adobe InDesign (evidence layer B — indirect via Quark's official interop docs; no direct Adobe source)

- Quark's official documentation treats InDesign as the dominant interchange counterpart: "Creating a project from an IDML file", "Convert InDesign files to QuarkXPress Projects" (bulk Smart Scan; INDD open requires local InDesign), "Export QuarkXPress files to InDesign Package (IDML Package)" with fonts + links + IDML included. IDML supported from InDesign CS5/CS6/CC exports.
- IDML mapping notes name InDesign-side structures: style sheets, colors, blend modes, gradients, anchored items, table styles, cell styles, object styles, footnotes, conditional styles, endnotes, TOC, grid styles, notes, interactivity.
- Inference (layer C): InDesign is the reference implementation of the same core model (frames, threading, master pages, styles, packaging) and the de facto interchange hub of the Type. No InDesign-specific feature claims are made in the final document.

### Affinity Publisher (no direct evidence)

- Official surfaces unreachable this pass (403 / transport error / Canva redirect). Listed as a representative product (market context only). No claims.

## Cross-product Comparison

| Dimension | QuarkXPress | MS Publisher | Scribus | (InDesign — indirect) |
|---|---|---|---|---|
| Self-label | "desktop publishing software & page layout software" | Publisher (DTP app in Office) | "Open Source Desktop Publishing" | page layout application (market usage) |
| Document container | Project → Layouts → Pages | Publication (.pub) | Document | Document |
| Free-placed frames | text/picture/no-content boxes, lines, tables | text/picture frames (scenario evidence) | text frames (+ linked frames) | frames (per IDML mapping) |
| Text flow | linked boxes = one story; auto page insertion | connected frames (pole behavior) | "link selected text frames directly" | threaded frames (IDML mapping) |
| Master pages | yes (automatic text box, master guides & grid) | not directly evidenced | not directly evidenced | yes (IDML mapping implies) |
| Styles | paragraph/character/item styles, conditional, groups | not directly evidenced | not directly evidenced | style sheets (IDML mapping) |
| Typography depth | extreme (H&J, kerning/tracking tables, OpenType, variable/color fonts, East Asian grids, rubi) | basic (consumer pole) | strong CJK/RTL/Indic, OpenType, hyphenation | professional |
| Color | CMYK/spot (Pantone), separations, ICC, output setups | not directly evidenced | not directly evidenced | professional |
| Output | print w/ PPD/marks/bleed/separations; PDF (X/A/UA); EPS; PS; images; ePub; HTML5 | print; Save As PDF | print/PDF (DTP identity; specifics not fetched) | PDF/print (market usage) |
| Handoff | Collect for Output (fonts/links/profiles/report); Usage checks; output styles | PDF conversion guidance | n/a | package (market usage) |
| Collaboration | Job Jackets, Composition Zones, CopyDesk, Notes, Redline | none evidenced | community model | InCopy (market usage, unverified) |
| Customer tier | professional + enterprise publishing | consumer/SMB | community/prosumer | professional |
| Business model | perpetual + subscription | bundled in Microsoft 365 (being retired) | free open source | subscription (market usage) |

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

A Desktop Publishing Application is recognizable by exactly this structure:

1. **Multi-page paginated document** — a fixed-geometry page set (with optional spreads) as the container of work.
2. **Free-placed layout objects** — text and picture frames/boxes positioned anywhere on a page canvas (pasteboard), not in a linear text stream.
3. **Text as reflowing stories** — text lives in frames as flowable content that threads across linked frames and pages, reflowing when content or geometry changes.
4. **Paginated publication output** — the deliverable is a paginated artifact for print or print-equivalent distribution (print engine output, PDF).

Remove free-placed frames + flowing text → word processor. Remove pagination/multi-page publication orientation → graphic design canvas. Remove frames (keep markup) → typesetting system. Remove output orientation → generic canvas editor.

Historical check (older/regional/platform-native products): Aldus PageMaker / Ventura Publisher / early QuarkXPress / MS Publisher 1.0 / Scribus / regional newspaper systems all satisfy these four properties; none of them require cloud, subscription, styles, or master pages to qualify. The L0 holds across eras.

### L1 — Common Mature Structure

Present in essentially all mature professional products (Quark direct; InDesign via IDML mapping; Scribus partially evidenced):

- master pages / parent pages (reusable page templates; automatic text boxes; master guides/grids)
- guides & grids: margins, columns, ruler guides, baseline grid, smart/dynamic alignment guides, snapping
- style sheets: paragraph + character styles; object/item styles; (conditional styles in some)
- text wrap / runaround around objects
- tables as layout objects
- layers
- professional typography: kerning, tracking, hyphenation & justification, widow/orphan control, OpenType features, drop caps, paragraph rules, anchored (inline) objects
- long-document machinery: footnotes/endnotes, cross references, TOC/lists, multi-page limits in the thousands
- linked asset management: pictures remain linked to source files; usage/links panels; modified-missing warnings
- output-readiness machinery: font/picture usage checks, verification against PDF standards (PDF/X family), Collect/Packaging (document + fonts + links + profiles + report)
- print production controls: bleed, crop/registration marks, separations vs composite, overprint/trapping, transparency flattening
- color management: CMYK + spot colors, swatch libraries, ICC profiles
- PDF export as the universal interchange output
- find/change incl. attribute- and pattern-based (GREP-class) search; spell check
- word-processor import filters (styles, footnotes, tables carried in)

### L2 — Variant / Optional Structure

- digital output channels: ePub (fixed/reflow), HTML5 publications, interactive PDF, app export
- consumer/SMB template pole: template-first small publications (cards, flyers, labels, calendars), simplified controls (MS Publisher pattern)
- editorial collaboration layer: copy-editing without layout alteration, tracked changes/notes, shared job specifications (CopyDesk/InCopy-class, Job Jackets-class)
- data merge / variable-data printing / web-to-print automation
- multi-layout projects, nested projects, adaptive scaling to other page sizes
- East Asian typography sets (design grids, rubi, Mojigumi, hanging punctuation)
- scripting/automation (AppleScript/JS/Python-class) and plugin/extension architectures
- interoperability formats (IDML-class interchange)
- cloud/web delivery of the authoring surface (rare in this Type; the market pole here remains desktop)

### L3 — Vendor-specific (research notes only)

- QuarkXPress: Project/Layout two-level container; Job Jackets/Job Tickets; Composition Zones; XPress Tags; XTensions/XDK; QX.js; CopyDesk; QuarkXPress Server (web-to-print/variable data); ImageGrid; Flex layouts; Content Variables; Redline; AutoFit min 7pt; 10,000-page layout limit; 224"×224" max page; pasteboard defaults; Hunspell; DejaVu bundling; Java requirement for IDML export.
- Microsoft Publisher: .pub format; Office-suite bundling; retirement timeline (Oct 2026); PowerShell bulk PDF conversion script; replacement mapping to Word/PowerPoint/Microsoft Create.
- Adobe InDesign: IDML as interchange substrate; CS5/CS6/CC version lineage (as documented by Quark).
- Scribus: GPL open source; SVN-based development; community support model.

## Rejected Findings (not promoted to core)

- "Desktop publishing = print only" — rejected; digital paginated outputs (ePub/HTML5) are documented output channels of the same layout model (Quark direct evidence). L0 says "print or print-equivalent paginated output."
- "DTP requires master pages" — rejected; master pages are L1. Older products and simple documents work without them.
- "DTP requires CMYK/spot color separations" — rejected as definitional; consumer pole (Publisher) doesn't evidence it; it's professional-pole L1/L2.
- "DTP is template-driven" — rejected; that's the consumer pole variant (and overlaps Template-based Design Platform). Professional DTP is layout-first, not template-first.
- "DTP includes photo editing / illustration" — rejected as definitional; Quark bundles photo editing and native-object illustration, but that's vendor bundling (L3), not the Type.
- "DTP is a web/cloud application" — rejected; the researched sample is desktop-installed software. Web delivery is at most an emerging L2.

## Boundary Findings

| Neighboring Type | Boundary judgment | "Remove what → becomes the other" |
|---|---|---|
| Page Layout Application (sibling leaf) | **Alias / same Type.** Quark's own product page titles one product "Desktop Publishing Software & Page Layout Software"; the user guide's chapters are the page-layout model. No structural difference found. | n/a — same referent |
| Professional Typesetting Application (sibling leaf) | Adjacent, likely distinct mechanism: typesetting systems compose pages from markup/batch rules (non-interactive), while DTP is interactive WYSIWYG frame layout. Both produce paginated output. Deserves its own research pass; do not merge blindly. | Remove interactive frame manipulation, drive layout from markup → typesetting system |
| Document Editor / Word Processor | Adjacent. Word processor: linear text stream, layout secondary, single-flow. DTP: layout canvas first, text flows into placed frames, multi-flow multi-frame. | Remove free-placed frames + threading → word processor |
| Graphic Design Application | Adjacent. Graphic design: single-canvas artwork, objects as artwork. DTP: multi-page text-centric publication assembly with reflow. | Remove pagination + text flow → design canvas |
| Template-based Design Platform | Adjacent. Template-first web canvas, light print production, consumer output. DTP: blank-page layout authoring with production-grade output controls. | Remove production output machinery + frame-level typography → template design platform |
| Presentation Application | Adjacent. Slides are page-like but screen-deck-oriented, linear delivery, no print production chain. | Swap print pagination for deck delivery → presentation app |
| Vector Graphics Editor | Adjacent. Object drawing vs page assembly; DTP places vector art as linked/embedded content. | Remove page/flow/publication semantics → vector editor |

## Taxonomy Issues (for STATUS.md Boundary Issues)

1. **Page Layout Application (§04.17) is almost certainly an alias of Desktop Publishing Application.** Direct evidence: Quark markets one product under both labels; the professional market uses "page layout application" as the modern functional term for the same software category (InDesign-class). Recommend joint review / merge rather than two Types.
2. **Professional Typesetting Application (§04.17)** overlaps on output but differs in authoring mechanism (markup/batch vs interactive frames). Flag for its own pass; likely a distinct Type or a variant of this one depending on what its research shows.
3. Market trend note: the consumer/SMB pole is contracting (Microsoft retiring Publisher Oct 2026, routing scenarios to Word/PowerPoint + template galleries). This does not dissolve the Type — the professional pole remains robust — but the Type's center of gravity is now unambiguously professional print/digital publication production.

## Uncertainties

- InDesign and Affinity Publisher operational details unverified this pass (sources unreachable). All InDesign statements in the final document are limited to ecosystem facts documented by Quark + market-context framing.
- MS Publisher's internal model (master pages? connected-frame mechanics? mail merge?) not directly evidenced; the consumer pole is characterized by Microsoft's own scenario list rather than by feature documentation.
- Scribus operational depth (output chain, color management) not directly evidenced beyond the README; Scribus claims kept minimal.
- Whether "Professional Typesetting Application" should be a separate Type is unresolved (needs its own pass).
- Exact numeric limits (page counts, sizes, font minimums) observed at Quark only; treated as vendor facts, excluded from the final document.

## Final Synthesis

The Desktop Publishing Application is the interactive page-assembly application of the publishing world. Its defining core is small: a multi-page paginated document, free-placed text/picture frames on a pasteboard canvas, text that flows as rethreading stories across frames and pages, and paginated publication output (print/PDF). Everything else the market associates with the category — master pages, style sheets, guides and baseline grids, professional typography controls, layers, color separations, preflight/packaging, PDF standards, long-document machinery, digital output channels, editorial collaboration — is mature standard structure layered on that core, with a consumer template-driven pole and a professional production pole as the main market variants. "Page Layout Application" is the same Type under a modern label; "Professional Typesetting Application" is a neighboring mechanism that must be researched separately.
