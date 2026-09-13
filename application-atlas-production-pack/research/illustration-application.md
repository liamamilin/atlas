# Research Notes — Illustration Application

Research date: **2026-09-07**
Directory leaf: `Illustration Application` (§04.03 Vector Graphics)
Slug: `illustration-application`

---

## Research Goal

Understand what an **Illustration Application** is as an Application Type: what objects exist inside it, how users create illustration artwork, which structures are definitional vs common vs variant, and where its boundaries sit against the neighboring creation-family Types — especially the two closest neighbors, **Vector Graphics Editor** (same directory section, 04.03) and **Digital Painting Application** (04.02).

The directory places this leaf under "Vector Graphics" together with Vector Graphics Editor. Prior passes constrain the interpretation:

- `digital-painting-application` (§04.02, processed) recorded its boundary as "vs Illustration Application (vector object model)" — i.e., the painting pass reads this leaf as the vector-object-model artwork Type.
- `graphic-design-application` (§04.01, processed) flagged that the market does not cleanly separate "graphic design" from "vector graphics" labels and recommended joint review when the 04.03 leaves are processed.
- `font-editor` (§04.18, processed) drew its own seam against Vector Graphics Editor by the absence of font context.

This pass therefore researches the leaf as **the illustration-oriented pole of vector-artwork applications**, while honestly testing whether the market realizes it as a population distinct from the generic vector editor.

## Initial Boundary

Working hypothesis at start:

- An Illustration Application is an application for **creating illustration artwork by drawing vector objects** — paths, shapes, text — that remain individually editable and scale without pixelation.
- Users: illustrators, logo/icon artists, character artists, designers doing artwork creation.
- Nearest neighbors: Vector Graphics Editor (sibling, same section), Digital Painting Application (raster brushes), Graphic Design Application (deliverable composition), Raster Image Editor (existing-pixel manipulation), AI Image Generator (generation-first), 2D Animation Application (timeline center), Diagramming Application (semantic connector objects).
- Key open question: is "Illustration Application" a distinct market population, or the same product family as "Vector Graphics Editor" under a second label?

## Research Questions

1. What is the core object model of illustration applications (document, canvas/artboard, path, anchor point/node, shape primitive, fill/stroke, layer, group)?
2. What drawing instruments exist (Pen/Bézier, pencil/freehand with smoothing, variable-width brushes, shape tools) and how do they relate to the vector object model?
3. How does shaping work (Boolean operations, shape builder, masks/clipping, cutting tools)?
4. What is the document/output model (native format, standard vector formats, raster export, print, artboards/multipage)?
5. How does raster content integrate (placed images, tracing, pixel painting) without breaking the vector center?
6. What is the illustration-craft orientation — expressive drawing instruments, pressure, brush libraries — and is it definitional or common?
7. Where is the boundary vs Vector Graphics Editor: distinct population or one family, two labels?
8. What does the historical check say (older/regional products; mouse-era vs pen-era)?

## Representative Products

Selection: market representation + documentation completeness + different product philosophies + different customer tiers.

| Product | Vendor | Why sampled | Evidence level |
|---|---|---|---|
| Affinity Designer 2 | Serif/Canva | professional single-app hybrid vector+pixel; one-time-purchase pole; full official help reachable | A — official help (intro page + full TOC) fetched this pass |
| Linearity Curve (formerly Vectornator) | Linearity GmbH | modern iPad/Mac-first illustration-positioned vector app; Apple-ecosystem pole; full user guide + product pages reachable | A — official user guide pages + product page fetched this pass |
| CorelDRAW Graphics Suite | Corel | long-lived professional suite; print/sign/apparel verticals; official product pages + educational guides | A — official pages fetched by the graphic-design-application pass (2026-09-07); reused with cross-reference |
| Xara Designer Pro+ | Xara GmbH | all-in-one single-application designer with an explicit separate "Illustration" pillar | A — official product/features pages fetched by the graphic-design-application pass (2026-09-07); reused |
| Adobe Illustrator | Adobe | the market archetype (literally named "Illustrator"); subscription professional standard | NO direct evidence — helpx.adobe.com and adobe.com unreachable (timeouts ×2 this pass; ×3+ in prior passes). Market anchor only; structural facts kept to widely-attested level, sourced Layer B via Corel's official guide |
| Inkscape | Inkscape project | the free/open-source vector editor archetype | NO direct evidence — inkscape.org 403, docs.inkscape.org transport error (abandoned per network rule). Market anchor only |

The three product-level poles (professional suite / hybrid single-app / mobile-first) are covered with direct evidence; the two archetypes anchor the family at market level only.

## Sources

### Fetched this pass (2026-09-07)

- Affinity Designer 2 Help — "What is Affinity Designer 2?" — https://affinity.help/designer2/en-US.lproj/pages/Introduction/about_designer.html
- Affinity Designer 2 Help — full contents/TOC (index) — https://affinity.help/designer2/en-US.lproj/index.html
- Linearity Curve — product page ("Curve: Advanced Vector Design Software") — https://www.linearity.io/curve
- Linearity Curve User Guide (iPad) — Drawing tools — https://www.linearity.io/academy/curve/ipad/user-guide/vector-editing/drawing-tools/
- Linearity Curve User Guide (iPad) — Editing tools — https://www.linearity.io/academy/curve/ipad/user-guide/vector-editing/editing-tools/
- Linearity Curve User Guide (iPad) — Shaping tools — https://www.linearity.io/academy/curve/ipad/user-guide/vector-editing/shaping-tools/
- Linearity Curve User Guide (iPad) — Start here — https://www.linearity.io/academy/curve/ipad/user-guide/start-here/

### Fetched by prior passes (evidence reused, originally Layer A)

- CorelDRAW Graphics Suite product page, family comparison, Standard page, how-to index, poster tutorial, "What is Vector Art?" and "Choosing Vector Software" guides (URLs recorded in research/graphic-design-application.md §Sources)
- Xara Designer Pro+ product page and features page (URLs recorded in research/graphic-design-application.md §Sources)

### Unreachable / abandoned (Source-access limitation)

- helpx.adobe.com (Illustrator user guide) — timeout ×1 this pass; adobe.com/products/illustrator.html — timeout ×1 this pass; prior passes recorded helpx timeouts ×3+. **Abandoned.** No product-specific operational claims made for Illustrator; the only Illustrator facts carried are competitor-published (Corel's official educational guide) and kept at widely-attested level.
- inkscape.org/doc — 403; docs.inkscape.org — transport error. **Abandoned per network rule.** No operational claims for Inkscape.
- product.corel.com/help — 404 at attempted path (Corel evidence stands on the prior pass's coreldraw.com pages instead).
- Corollary per evidence rules: assertion strength reduced accordingly; no numeric limits, no version-specific defaults, no precise format lists asserted for unreachable products.

---

## Product Observations

### Affinity Designer 2 — evidence layer A (official help, this pass)

Positioning (Introduction / "What is Affinity Designer 2?"): "a powerful vector design app coupled with pixel-based textures and retouching, all brought together in the same user interface." Key concepts stated by the vendor: different tool sets called **Personas** for different design needs; combined vector and pixel editing in the same document "retaining vector editing throughout"; **non-destructive operations**; real-time dynamic tools and effects; high-end file format support.

Structure observable from the official help contents:

- **Documents & artboards**: create new documents; document units; drawing scale; document templates; **artbooks → artboards** (about/adding/moving/aligning; artboard-level color and opacity; artboard export and printing) — multiple artboards per document.
- **Drawing curves and shapes**: about lines, curves and shapes; draw/edit curves and shapes; pencil lines; **pressure sensitivity** and **edit on-page pressure profiles**; geometric shapes; QR code tool; arrowheads; dot/dash and texture line styles; **multiple strokes and fills** per object; node selecting/aligning; transforming curves; **expand stroke**; **contouring**; **cornering**; fill modes.
- **Vector painting**: painting **vector brush strokes**; modifying strokes; **creating custom vector brushes**; pressure sensitivity.
- **Pixel painting** (second persona): pixel brush strokes; custom pixel brushes; symmetry/mirror; erasing; retouch.
- **Object control**: selecting (incl. by attribute); grouping; duplicating; **Boolean operations** (joining; creating **compounds**); **shape builder**; cutting (knife); warping; aligning; distributing; ordering; isolating; **rasterizing**; flooding; **convert to curves**; styles; quick grids; **assets**; **symbols**; layer states; object defaults.
- **Layers**: layers with drop zones; blend modes/ranges; **image layers**; **layer clipping**; **layer masking**; adjustment layers.
- **Color**: color models/spaces; **color management**; **global colors**; **spot colors**; overprint; **gradient and bitmap fills**; transparency editing.
- **Text**: artistic text; frame text; **text on a path**; shape text; character/paragraph formatting; variable fonts; OpenType features; text styles.
- **Design aids**: undo/redo/**history**; clip to canvas; rotate view; grids incl. **isometric/axonometric**; rulers/guides/margins; measuring; dynamic guides; snapping (incl. curve/construction snapping); force pixel alignment; constraints; snapshots.
- **Layer effects** (non-destructive FX): 3D, bevel/emboss, color/gradient overlay, Gaussian blur, inner/outer glow, inner shadow, outer shadow, outline.
- **Output**: save; bleed; working with SVGs; **Export** + **Export Persona** (export options, slices); print; **packaging** (document + resources handoff); import/export file formats appendix; import of PDF/Adobe/CAD documents; embedding vs linking with a **Resource Manager**.
- **Panels**: layers, appearance, assets, brushes, character/paragraph/typography, color, swatches, stroke, styles, symbols, transform, navigator, history, isometric, glyph browser, etc.

### Linearity Curve — evidence layer A (official user guide + product page, this pass)

Positioning (product page): "Fast and intuitive vector design"; "Curve exists for the **illustrators**, graphic designers tired of bloated interfaces"; "tools built for expressive, **editable vector illustration**"; use-case page "Digital Illustration"; Apple-ecosystem native (Mac, iPad, iPhone; Apple Pencil optimized); offline-capable native apps; workspaces & collaboration (personal/team/client workspaces, sync).

Drawing tools (user guide): "generate vector shapes and lines from scratch."

- **Pen Tool** — creates **Bézier curves** ("vector paths") that can be "drawn, curved, edited, and closed"; "scaled infinitely"; node handles determine direction/angle; straight paths by tapping, curves by tap-drag; node types selectable while drawing; **Close Path / Finish Path** actions; an open path can be continued from its end node.
- **Pencil Tool** — freeform paths following the hand, with a **smoothness** control (higher smoothing simplifies the path and removes nodes; post-draw smoothing also possible); closed freeform shapes can be filled and combined with Boolean operations.
- **Brush Tool** — freeform paths with **variable widths**; brush presets; brush profiles; stroke width = maximum width of a variable-width stroke; brush strokes can also be applied to an existing path.
- **Shape tools** — rectangle, oval, line, star (point count parameter), spiral (decay parameter), polygon; constraint modifiers for squares/circles and 45° snapping.

Editing tools (user guide): modify existing vector shapes.

- **Selection Tool** — select/move/resize/rotate whole objects; multi-select; duplicate mode (drag to duplicate; combinable with rotate/scale for rotational/scalable copies); click-through mode (bypasses layer hierarchy; useful inside masks/groups).
- **Node Tool** ("also known as the Direct Selection Tool") — "select individual points"; create/select/move/edit **Bézier nodes**; color-coded nodes (start/standard/end); **node types** (single / mirrored / asymmetric / disconnected — handle behavior defined per type); add/delete nodes; open/close path.
- **Scissors Tool** — splits a path/shape into open paths (vector shapes only; not grouped/masked objects).
- **Eraser Tool** — erases areas along a drawn path; **destructive** ("you can only undo it once"); vector shapes only; layer locking excludes layers from erasing.

Shaping tools (user guide):

- **Boolean operations** — five: **Unite, Subtract, Intersect, Divide, Exclude**; described as "often used in Icon and Logo Design."
- **Clipping masks** — "a shape that only reveals artwork within its boundaries — in effect cropping the artwork"; any closed shape can become a mask; mask identifiable in layers; edit by entering an isolated state.
- **Shape Builder** — merge/erase intersecting parts of selected overlapping shapes interactively (merge mode default; erase mode alternative).

Product page capabilities: **custom brushes** ("pressure-sensitive, fully vector"); advanced gradients (linear, radial, "mesh-style"); vector effects ("shadows, blurs, and more — non-destructive and editable anytime"); typography (tracking/kerning/alignment, **text on path**, custom fonts, **convert type to outlines** with vector brush styling); print (CMYK support; export "clean PDFs, SVGs, EPS"); **PDF editing** ("open, edit, and transform PDFs as native Curve files"); **Auto Trace** (convert images/logos/sketches into editable vector paths); raster/AI helpers (background removal, AI grab, magic eraser); content integrations (Unsplash, SF Symbols, Icons8, Brandfetch); templates; **cross-tool compatibility** (import/export to Figma, Illustrator, Sketch).

Glossary-level concepts (official FAQ/glossary): path = line made of anchor points/nodes; open/closed/compound paths; Pen tool named after Bézier.

### CorelDRAW Graphics Suite — evidence layer A (official pages, via graphic-design-application pass)

- Product composition: CorelDRAW itself is positioned as **"vector illustration and page layout"** inside a graphic-design suite (with PHOTO-PAINT for pixel editing, Font Manager, PowerTRACE bitmap-to-vector, CAPTURE).
- Vector illustration pillar: shaping/drawing tools; effects including **Contour, Envelope, Blend, Mesh Fill**; non-destructive adjustments (block shadows, symmetry, perspective); **PowerTRACE** tracing; object management (Objects docker with stacking order, hide/rename/search; Focus Mode isolation); object styles/style sets; color/fills/transparencies (swatches, harmonies, gradients, **mesh fills**); multipage documents with a multipage view; typography (text effects, variable fonts, **fit text to path**); print/web output (color management engine, prepress tools); extensive file-format compatibility.
- Audience framing: illustrators listed among vector-art users; industry verticals include **"illustration/fine art"** alongside signage, apparel, branding.
- Educational guide ("What is Vector Art?"): vector = math-defined lines/points/curves/shapes, **infinitely scalable**; history narrative: Sketchpad (1963) → Illustrator → CorelDRAW (1989).
- Educational guide ("Choosing Vector Software"): frames the category as "vector graphics software" with options CorelDRAW, Illustrator, Inkscape, Canva; distinguishes Canva as template/browser-based design software rather than purely vector.

### Xara Designer Pro+ — evidence layer A (official pages, via graphic-design-application pass)

- An all-in-one designer application whose feature set is organized into explicit pillars, one of which is **"Illustration"** (distinct from its Desktop-publishing, Web-design, PDF, Photo-editing pillars): QuickShape & freehand drawing, Blend tool, **soft vectors & feathering**, transparency, **scatter/art brushes**, 3D extrude, **Live Effects** ("vector objects remain editable after applying effects"), ClipView (object-as-window masking), shadows, bevels, contours.
- The existence of a discrete, named "Illustration" pillar inside a general design application is direct vendor evidence that "illustration" denotes a recognizable capability cluster within the vector tool family.

### Adobe Illustrator — no direct evidence; market anchor (layer B)

- Unreachable this pass and in prior passes. Widely-attested structural facts only, no operational claims: the industry-standard professional application for vector-based design work (illustration, logos, icons, typography); the product name itself ("Illustrator") is the strongest market signal that illustration is a primary job of this family; subscription-only licensing (competitor-published fact, Corel guide, layer B); bitmap-to-vector tool named "Image Trace" (layer B, Corel guide).

### Inkscape — no direct evidence; market anchor (layer B)

- Unreachable this pass. Widely-attested structural facts only: free open-source desktop vector editor; named as "free vector software" in Corel's official guide. No operational claims.

---

## Cross-product Comparison

| Dimension | Affinity Designer 2 | Linearity Curve | CorelDRAW (suite) | Xara Designer Pro+ | Illustrator / Inkscape (anchors) |
|---|---|---|---|---|---|
| Self-labeling | "vector design app" + pixel | "vector design… expressive, editable vector illustration"; audience "illustrators" | "vector illustration and page layout" inside a design suite | discrete "Illustration" pillar | "Illustrator" (name); "free vector software" (Inkscape, via Corel guide) |
| Defining object | vector curves/shapes ("retaining vector editing throughout" even in hybrid docs) | Bézier paths of anchor points; open/closed/compound | vector illustration objects | vector objects (Live Effects keep them editable) | vector artwork (attested) |
| Path drawing | Pen/pencil; pressure + pressure profiles | Pen (node types), Pencil (smoothing), Brush (variable width, presets) | shaping/drawing tools | QuickShape, freehand | Pen-class tools (attested) |
| Expressive brushes | vector painting; custom vector brushes; pixel brushes in second persona | custom brushes; brush presets/profiles; pressure | brushes among bundled content | scatter/art brushes | attested (Illustrator brush lineage) |
| Shaping | Boolean ops + compounds + shape builder + knife | 5 Boolean ops + Shape Builder + masks | shaping tools | Blend, ClipView | Boolean tooling attested |
| Node editing | node tool; select/align nodes | node tool; node types; add/delete/open/close path | node editing within object model | — | attested |
| Non-destructive effects | layer effects; adjustments | vector effects "non-destructive and editable anytime" | non-destructive adjustments; effects | Live Effects | attested lineage |
| Raster integration | pixel persona in same document; image layers; rasterizing; bitmap fills | placed images; auto trace; background removal/AI helpers | PHOTO-PAINT companion; PowerTRACE | photo pillar | Image Trace (attested, layer B) |
| Typography | artistic/frame/path/shape text; convert to curves | text tool; text on path; outlines | fit text to path; text effects | text pillar | attested |
| Color discipline | color management; global/spot colors | CMYK support; palettes | color management engine; prepress; Pantone (vendor claim) | — | attested lineage |
| Output | SVG/PDF/print; export persona slices; packaging | PDF/SVG/EPS; PDF editing | print-standard output; ~100 formats (vendor claim, tier-dependent) | PDF profiles | attested lineage |
| Canvas organization | artboards; drawing scale | artboard mentioned; projects | multipage documents | — | artboards (attested lineage) |
| Platform | desktop (macOS/Windows/iPad) | Mac/iPad/iPhone native; offline | Windows/Mac/web | Windows desktop | desktop lineage |
| Collaboration/cloud | — | workspaces; sync; team sharing | CorelDRAW Web (subscriber) | Xara Cloud companion | cloud lineage (CC) |
| AI features | — | auto trace, background removal, AI grab, magic eraser | AI image generation/remix/masking | — | current-gen AI (attested) |
| Business model | one-time (V2 era) | freemium/subscription | subscription + one-time + maintenance | subscription | subscription (attested, layer B) |

**Reading of the table**: every sampled product, regardless of positioning, shares one structural center — the user draws and edits **vector objects** (Bézier paths, shape primitives, text) in a **persistent document**, composes them with shaping machinery (Boolean, masks, shape builder) and layering, and outputs finished artwork (print/digital vector + raster). Around that center, the illustration-oriented products add an **expressive drawing layer** (pressure-sensitive vector brushes, freehand smoothing, brush libraries) as first-class machinery. Delivery, licensing, collaboration, AI, and platform are peripheral.

---

## Abstraction Hierarchy

### L0 — Defining Invariant

Three properties, held jointly:

1. **Vector object model as the artwork's primary medium.** The artwork consists of discrete, individually addressable objects whose geometry is mathematically defined — paths built from anchor points and curve handles, shape primitives, text as editable objects — rendered by computation rather than stored pixels, hence resolution-independent. Remove it → the product becomes a raster brush studio (Digital Painting Application) or a pixel editor (Raster Image Editor).
2. **User-authored illustration creation.** The normal job is the user making the first pass of the artwork by drawing — starting from a blank canvas and building the image object by object with drawing/editing instruments. Remove it → the product becomes a viewer/converter, or a generation-first tool (AI Image Generator), or a template-composition platform (Template-based Design Platform).
3. **Persistent editable document with rendered artwork output.** Work lives in a re-openable document whose objects retain editability (re-editing a path months later is meaningful), and the workflow ends in finished artwork taken out of the tool (export/print). Remove it → a scratchpad/whiteboard, or a one-shot output utility.

### L1 — Common Mature Structure

Present across the sampled products; expected in any current product but not required to recognize the Type:

- Bézier path machinery: Pen tool (tapped anchor points + curve handles), node/direct-selection tool (move/add/delete nodes; per-node handle behavior), open/closed/compound paths
- Freehand instruments: pencil-class freehand drawing with smoothing/path simplification; variable-width vector brushes with pressure support and brush presets/custom brushes
- Shape primitives with live parameters (rectangle, ellipse, polygon, star, spiral, line)
- Shaping machinery: Boolean operations (unite/subtract/intersect/divide/exclude-class), shape-builder-style interactive merging, cutting/splitting tools, clipping masks, corner rounding/contour-class modifiers
- Strokes and fills: stroke width/styles (dash, arrowheads), fills, gradients (linear/radial, mesh-class in professional products), transparency; color systems (swatches; global/spot colors at the professional pole)
- Object composition: stacking/z-order, groups, layers panel, per-object opacity and blend modes, non-destructive live effects on objects
- Transform and precision machinery: align/distribute, snapping, guides/grids, precise numeric transforms
- Typography as vector content: point/frame text, text-on-path, convert text to outlines
- Reusable elements: symbols/assets-class libraries (some products)
- Undo/history; zoom/navigate canvas controls
- Raster integration: placing images; bitmap-to-vector tracing; export to standard raster sizes
- Output: native format + standard vector interchange (SVG/EPS/PDF-class) + raster export; print capability at the professional pole

### L2 — Variant / Optional Structure

- **Hybrid pixel side**: a second tool mode/persona for pixel painting and raster retouch inside the same document (one sampled product's headline design), or raster capability left to companion applications (suite pole)
- **Canvas organization**: artboards (multiple canvases per document), multipage documents, or single canvas
- **Print production depth**: CMYK/spot/overprint, bleed, prepress checks, packaging handoff (professional/print-vertical pole)
- **Collaboration/cloud**: cloud workspaces, team/client sharing, browser delivery, real-time collaboration
- **AI-era helpers**: auto-trace, background removal/subject isolation, generative image features
- **Templates & content libraries** as starting points (nearer the design-composition neighbor)
- **Animation/3D extras**: blend/3D-extrude-class object effects; companion animation applications; frame animation in some products
- **Technical-leaning aids**: isometric/axonometric grids, dimension/measure tools, drawing scale
- **Platform & input**: desktop/iPad/mobile/web delivery; pen-tablet vs mouse-era input (pressure common but not definitional)
- **Business model**: subscription / one-time / freemium / free OSS

### L3 — Vendor-specific Structure (research notes only)

- Affinity: **Personas** (named tool-set modes), Export Persona/Slices, Assets panel, "Studio" panel family, packaging workflow, isometric panel, OpenColorIO support
- Linearity Curve: color-coded Bézier nodes with named node types (single/mirrored/asymmetric/disconnected), content-aware options, 5-in-1 selection modes, Brandfetch/Unsplash/SF Symbols/Icons8 integrations, "Vector 1.0" AI model, Vectornator rebrand history
- CorelDRAW: "dockers" panel terminology, PowerTRACE, CDR/CDT formats, CorelDRAW Web/Go tiers, Focus Mode, bundled Pantone integration, named AI models, tier content counts (~10/~70/~100 formats) — vendor claims
- Xara: Live Effects, Live Copies, ClipView, soft vectors & feathering, PDF/X export profiles, "Replaces…" competitive framing
- Adobe: "Image Trace" tool name (layer B), Creative Cloud packaging (layer B)

---

## Vendor-specific Findings

See L3. Additional cross-pass observations:

- The sampled vendors disagree on packaging (suite + companion pixel app vs single hybrid app vs mobile app), while agreeing on the underlying structure — the classic "one Type, many packagings" pattern.
- Linearity and Xara both explicitly name illustration as the use/pillar; CorelDRAW names "vector illustration" as its module's job; Affinity markets vector design with illustration among its uses. No sampled vendor markets a product called an "illustration application" that lacks the standard vector machinery — there is no separate "illustration-only" product family with different internals.

## Rejected Findings

- **"Illustration application = drawing tablet software with pressure support"** — rejected. Pressure/stylus machinery is common (Affinity, Linearity) but the mouse-era generation of the same Type (documented history: Illustrator/CorelDRAW in the 1980s–90s) lacks it, and it is a hardware/input affordance, not the Type's structure.
- **"Illustration application = raster natural-media painting"** — rejected as the definition; that is the Digital Painting Application Type. Vector brush strokes (Affinity vector painting, Linearity brushes, Xara art brushes) make the raster-brush feel available *within* the vector object model, which is exactly the hybrid capability that distinguishes the illustration pole.
- **"Illustration application requires AI tracing/AI generation"** — rejected; AI helpers are current-gen additions across several products (Linearity, CorelDRAW) but absent in others (Affinity's help documents none as core) and absent historically.
- **"Multi-page/artboards are definitional"** — rejected; single-canvas documents satisfy the Type (historical products and current mobile products).
- **"Cloud collaboration is definitional"** — rejected; desktop one-time and OSS products satisfy the Type fully offline.

## Boundary Findings

### vs Vector Graphics Editor (04.03 sibling — the critical boundary)

The market does **not** realize two distinct product populations behind the two 04.03 leaves. Evidence:

- Corel's official educational guide frames the category as "vector graphics software" and lists the same flagship products the market calls illustration tools; CorelDRAW itself is marketed as "vector illustration and page layout."
- Adobe's archetype is named "Illustrator" yet is universally cited as *the* vector graphics editor; Linearity Curve is positioned for "illustrators" while self-labeling "vector design software."
- The graphic-design-application pass already recorded: "the market does not cleanly separate the two labels (…sampled vendor's own official educational guide frames the category as 'vector graphics software' listing CorelDRAW/Illustrator/Inkscape/Canva while its product pages self-label 'graphic design software'…) — joint review recommended when vector-graphics-editor is processed."

**Assessment: probable one-family-two-labels relationship, closest in the whole creation family.** This document is written from the illustration-oriented pole: audience is illustrators/artists; the expressive drawing layer (pressure vector brushes, freehand smoothing, brush libraries) is first-class; the center of gravity is the artwork itself. The generic vector editor pole would be written around precision tooling for any vector work (icons, diagrams, technical, UI, logos). Removal test between the poles: strip the artwork-creation orientation and expressive-drawing layer → generic vector tooling; strip general-purpose precision tooling framing → illustration craft. Both leaves can coexist under the raster-editor/painting precedent (two leaves, shared machinery, primary-job gradient), but this is a judgment the joint review with the vector-graphics-editor pass should ratify. **Joint review recommended (three-way: graphic-design-application + vector-graphics-editor + illustration-application).**

### vs Digital Painting Application (04.02, processed)

Same machinery family on the surface (brushes, layers, pressure) but opposite primary object model: painting's marks are raster pigment on a canvas; this Type's artwork is geometry-defined objects. The painting pass recorded this boundary from its side ("vs Illustration Application (vector object model)"). Overlap specimen: products with vector linework layers (painting side) and products with pixel painting modes (this side) — both are capability overlaps, not identity arguments. The seam is the primary medium of the artwork.

### vs Graphic Design Application (04.01, processed)

The graphic-design pass centers composing **design deliverables** (typography + layout + output machinery for mixed-element compositions); this leaf centers the **artwork** (drawing craft). The two families share products (CorelDRAW is marketed in both spaces: "vector illustration **and page layout**") — the market straddles the seam at product level while the capability centers differ. Held consistent with that pass's framing.

### vs AI Image Generator (04.20, unprocessed)

Generation-first (system composes the first pass from a description) vs authoring-first (user draws the first pass). Some sampled products embed generative features (Linearity AI backgrounds; CorelDRAW AI generation) as helpers without flipping the center. Same "editing-first vs generation-first" gradient the graphic-design pass recorded.

### vs Raster Image Editor (04.02, processed) and Pixel Art Editor (04.02)

Raster editor's center is modifying existing pixel images; this Type creates artwork from objects. Pixel Art Editor constrains to a pixel grid/palette — the opposite of resolution-independent geometry.

### vs Diagramming Application (03.05) and Data Visualization Application (13)

Diagramming's objects carry semantic/connector behavior for structured diagrams; this Type's objects are freeform artwork with no semantic connectors. Data visualization renders computed marks from user data; here the user hand-authors the shapes. The data-viz pass recorded this same seam from its side ("computed marks vs hand-authored shapes").

### vs 2D Animation Application (04.08)

Timeline/scene center vs static artwork center. Some vector tools add frame animation or export animation-ready assets — optional capability, not the center.

### "去掉什么就变成另一个 Type" removal tests (summary)

- Remove vector object model → Digital Painting Application / Raster Image Editor
- Remove user-authoring (generation-first) → AI Image Generator
- Remove persistent editable document → whiteboard/scratchpad or one-shot output tool
- Remove artwork creation orientation (keep generic precision vector tooling as the frame) → Vector Graphics Editor (sibling leaf — joint review)
- Remove freeform drawing (start from browsed templates constrained for non-designers) → Template-based Design Platform

## Historical / Market-Sample Check (§24)

- **1980s–90s desktop generation**: Illustrator (documented history per Corel's official guide), CorelDRAW (1989), FreeHand, Xara Studio — single-user desktop applications for drawing vector artwork with persistent documents and export. All satisfy the L0. None had cloud, AI, artboards-as-cloud-projects, or pressure-critical input. ✔
- **Mouse-era vs pen-era**: pressure is common today but not definitional; the historical check forces pen input out of the core. ✔
- **Regional/mobile-first products** (Vectornator lineage, regional vector apps): same core — vector objects, drawing, persistent documents, export. ✔
- **Early consumer clip-art studios**: template-driven composition without freeform object authoring do NOT satisfy L0 property 2 — correctly excluded (consistent with the graphic-design pass's exclusion of template ancestors). ✔
- The definition is delivery-agnostic (desktop/tablet/mobile/web), licensing-agnostic, collaboration-agnostic, AI-agnostic.

## Uncertainties

1. **The leaf's independence from Vector Graphics Editor is the main open taxonomy question.** Evidence points to one market family; this pass documents the illustration-oriented pole and defers the keep-both vs merge decision to the three-way joint review. (Recorded in STATUS.md Boundary Issues.)
2. **Adobe Illustrator operational structure unverified** (source unreachable across three passes). Widely-attested facts only. If the Illustrator help becomes reachable, its Pen/Appearance/artboard mechanics should be checked against the L1 list — no claim in this document depends on it.
3. **Inkscape operational structure unverified** (source unreachable). Same caveat.
4. **Affinity Designer's exact artifact-level behavior** (e.g., Boolean compound semantics, pressure-profile editing UX) was evidenced at help-TOC + intro level, not full-text for every topic; topic titles are reliable, fine-grained behaviors were not asserted.
5. **Format/export precision**: exact supported-format lists vary by product and tier (CorelDRAW's ~10/~70/~100 are vendor tier claims); the final document speaks of "standard vector and raster formats" without inventing lists.
6. **Market share / prevalence claims** deliberately absent — no evidence gathered for share assertions.

## Final Synthesis

The Illustration Application is the **artwork-creation pole of the vector tool family**: an application in which the user creates illustration artwork — characters, scenes, logos, icons, decorative art — by drawing **vector objects** (Bézier paths, shape primitives, editable text) that remain individually editable and render at any scale, inside a **persistent document**, ending in **finished artwork output**. Around this defining core, mature products add: expressive drawing instruments (pressure-sensitive vector brushes, smoothing freehand), Bézier node editing, Boolean/mask shaping, strokes/fills/gradients with color systems, layering with non-destructive effects, typography as objects, raster integration (placement, tracing), and standard-format output. Hybrids (pixel modes), suites (companion pixel apps), platforms (desktop/iPad/web), and business models vary; the defining core does not.

The Type's sharpest honest statement: **the market sells one vector product family under the labels "vector graphics" and "illustration"; the directory holds two leaves for it, and this leaf carries the illustration-craft center of gravity.** Joint review with the vector-graphics-editor pass (and the graphic-design pass's existing flag) is the correct resolution path.
