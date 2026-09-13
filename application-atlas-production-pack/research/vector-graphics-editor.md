# Research Notes — Vector Graphics Editor

Research date: **2026-09-09**
Directory leaf: `Vector Graphics Editor` (§04.03 Vector Graphics)
Slug: `vector-graphics-editor`

---

## Research Goal

Understand what a **Vector Graphics Editor** is as an Application Type: what the core object model is (document, canvas, paths, shapes, fills/strokes, layers), what drawing and editing machinery defines it, how precision and output machinery work, and where its boundaries sit against the neighboring creation-family Types.

This leaf carries two pre-hung flags that this pass must discharge (both recorded in STATUS.md Boundary Issues):

- `graphic-design-application` (§04.01, processed 2026-09-07): market uses "vector graphics" and "graphic design" labels for the same flagship products; center-of-gravity split proposed (composing design deliverables vs drawing craft); joint review recommended when this leaf is processed.
- `illustration-application` (§04.03 sibling, processed 2026-09-07): probable one-family-two-labels vs this leaf; that pass documented the illustration-craft pole (expressive drawing layer first-class, artwork-as-job) and recommended a THREE-WAY joint review (graphic-design-application + vector-graphics-editor + illustration-application), with candidate outcomes "keep-both with center-of-gravity seam" or "one-family-two-centers presentation", mirroring the 04.02 raster/painting keep-both precedent.

This pass therefore researches the leaf as **the general-purpose precision vector tooling pole** — the editor for the full breadth of vector work (logos, icons, UI/web assets, technical/isometric drawing, print assets, artwork) — while honestly testing whether the market realizes a distinct population behind the "vector graphics editor" label.

## Initial Boundary

Working hypothesis at start:

- A Vector Graphics Editor is an application for **creating and editing vector graphics** — images represented as geometry-defined objects (paths, shapes, text) that remain individually editable and scale without pixelation.
- Users: graphic designers, illustrators, icon/logo makers, web/UI designers, technical/marketing asset producers.
- Nearest neighbors: Illustration Application (sibling, same section — flagged), Graphic Design Application (04.01 — flagged), Digital Painting Application / Raster Image Editor (04.02), Font Editor (04.18), Diagramming Application (03.05), UI Design Application (04.15), Template-based Design Platform (04.01), AI Image/Design Generator (04.20), Mechanical CAD (16), Desktop Publishing (04.17).
- Sharpest seams: the two flagged siblings above (same market family under different labels); medium seams vs raster editing and font editing.
- Unknowns: whether the "general vector tooling" pole has its own defensible center of gravity distinct from illustration; whether SVG-centric products (web-native editors) form a structural variant; what the historical floor of the Type is (pre-Bézier draw programs).

## Research Questions

1. What is the core object model (document, canvas/artboard/sheet, path/anchor/handle, shape primitive, text object, fill/stroke, layer/group)?
2. What drawing and editing instruments exist (pen/Bézier, freehand, primitives, node editing) and which are universal vs tier-specific?
3. What shaping machinery exists (Boolean operations, shape-building, cutting, masks, corner/contour/offset)?
4. What precision machinery exists (snapping, smart guides, grids incl. isometric-class, rulers, view modes, deep zoom) and is any of it definitional?
5. What is the document/output model (native format, SVG/PDF/EPS/AI-class interchange, raster export, multi-scale/retina export, print/CMYK)?
6. How does raster content integrate (placed images, bitmap-to-vector tracing, hybrid pixel modes)?
7. What job breadth does the market realize (icons, logos, UI/web, technical, illustration, print) — where does the general-purpose center of gravity sit vs the illustration pole?
8. Where are the boundaries vs the flagged siblings (three-way joint review) and the other neighbors — can keep-both be ratified?
9. Historical check: do 1980s object-draw programs (mouse-era, pre-Bézier), regional products, OSS desktop products, and minimal web editors satisfy the definition without modern machinery (SVG, artboards, cloud, AI)?

## Representative Products

Selection: market representation + documentation completeness + different product philosophies + different customer tiers; deliberately adding poles NOT deeply sampled by the two sibling passes.

| Product | Vendor | Pole in the sample | Evidence level |
|---|---|---|---|
| Affinity Designer 2 | Serif (Canva) | professional one-time-purchase hybrid vector+pixel; full official help reachable | A — intro + key-features help pages fetched this pass |
| Amadine | BeLight Software | mid-tier Apple-ecosystem general-purpose vector design app (Mac/iPad/iPhone); detailed official features page | A — main + features pages fetched this pass |
| Vectr | Pixlr Pte Ltd | consumer cloud web vector editor with real-time collaboration; AI-era pivot specimen | A — main page + FAQ + vendor education page fetched this pass |
| Method Draw | Method of Action (open source) | minimal free web vector editor (no registration); the Type's floor | A — home page (thin) |
| Adobe Illustrator | Adobe | market archetype, professional subscription standard | NO direct evidence — helpx.adobe.com 403 this pass (timeouts in 3+ prior passes). Market anchor only |
| Inkscape | Inkscape project | free open-source desktop archetype | NO direct evidence — inkscape.org and /doc/ 403 this pass and prior passes. Market anchor only |
| Linearity Curve | Linearity GmbH | illustration-oriented vector app (cross-reference) | A via illustration-application pass (2026-09-07), reused |
| CorelDRAW Graphics Suite | Corel | long-lived professional suite (cross-reference) | A via graphic-design-application pass (2026-09-07), reused |
| Xara Designer Pro+ | Xara GmbH | all-in-one designer (cross-reference) | A via graphic-design-application pass (2026-09-07), reused |

Rejected candidates: Boxy SVG (main page returns empty SPA shell; /docs 404 — abandoned per network rule), SVG-Edit on GitHub (timeout ×1; Method Draw — its web-editor descendant — covers the web-OSS pole), Sketch (sampled by the collaborative-design-platform pass; UI-design-centric), Canvas X Draw (unreachable in prior passes), Gravit/Corel Vector (discontinued).

## Sources

### Fetched this pass (2026-09-09)

- Affinity Designer 2 Help — "What is Affinity Designer 2?" — https://affinity.help/designer2/en-US.lproj/pages/Introduction/about_designer.html
- Affinity Designer 2 Help — Key Features — https://affinity.help/designer2/en-US.lproj/pages/Introduction/keyFeatures.html
- Amadine — product page — https://amadine.com/
- Amadine — Features — https://amadine.com/features
- Vectr — product page + FAQ — https://vectr.com/
- Vectr — "What Are Vector Graphics?" — https://vectr.com/en/what-are-vector-graphics
- Method of Action / Method Draw — https://method.ac/

### Reused from prior passes (originally Layer A)

- Linearity Curve product page + user guide pages (drawing/editing/shaping tools) — URLs recorded in research/illustration-application.md §Sources
- CorelDRAW product/family/Standard pages + "What is Vector Art?" and "Choosing Vector Software" guides; Xara Designer Pro+ pages — URLs recorded in research/graphic-design-application.md §Sources

### Unreachable / abandoned (Source-access limitation)

- helpx.adobe.com/illustrator/user-guide.html — HTTP 403 this pass; timeouts recorded in 3+ prior passes. **Abandoned.** Illustrator facts carried are only widely-attested/competitor-published (Corel guide, layer B).
- inkscape.org and inkscape.org/doc — HTTP 403 (this pass ×2; also 403/transport errors in prior passes). **Abandoned.**
- boxy-svg.com — empty SPA shell ×1, /docs 404 ×1. **Abandoned; excluded from sample.**
- github.com/SVG-Edit/svgedit — timeout ×1. **Excluded** (Method Draw covers the pole).
- Corollary per evidence rules: assertion strength reduced accordingly; no numeric limits, version-specific defaults, or precise format lists asserted for unreachable products.

---

## Product Observations

### Affinity Designer 2 — evidence layer A (official help, this pass)

Positioning ("What is Affinity Designer 2?"): "a powerful vector design app coupled with pixel-based textures and retouching, all brought together in the same user interface." Key concepts stated by the vendor: **Personas** (different tool sets for different design needs); **combined vector and pixel editing in the same document, retaining vector editing throughout**; **non-destructive operations**; real-time dynamic tools and effects; high-end file format support.

Structure from the Key Features page:

- **Vector tools**: Artboards; Move tool; **Precise Pen Tool**; **Node Tool** ("fine tuning vectors"); **Contour Tool**; **Corner Tool**; freeform **Pencil with Sculpt mode**; **stroke stabilizer**; multiple strokes and fills per object; arrowheads; customizable geometric shapes; **Boolean operations (Add, Subtract, Intersect, Divide, Xor)** with live-preview non-destructive compounds; convert shapes/text to fully editable curves; symbols; assets; selectable-by-attribute object selection; multi-node selection/alignment/transform; control-handle snapping to angles and distances.
- **Precision/design aids**: dynamic snapping guides; fixed and column guides; rulers; multi-object alignment/distribution; on-object alignment handles; **pixel-accurate alignment for web graphics and website mockups**; managers for brushes/grids/snapping; **automatic, fixed and projection grids**; **isometric/advanced axonometric grids** (Isometric Panel, plane switching, cube mode); view modes **Pixel, Retina, and Wireframe (Outline and X-ray)** with split view; constraints for intelligent object scaling/anchoring; deep zoom; rotate document view; history with branching (vendor documents an upper bound on steps and optional save-with-document).
- **Layers**: non-destructive adjustment layers; adjustments/blend modes at stack/layer/group/selection/object level; clipping within layers; layer effects; blend ranges; hierarchical antialiasing.
- **Color**: 16-bits per channel; **CMYK, Lab, Grayscale, RGB modes**; swatches; global colors; tints; **PANTONE support**; ICC profiling; ASE palette import.
- **Vector brushes**: galleries; custom/image-based brushes; pressure and velocity controllers; controller ramps.
- **Text**: artistic and frame text; text on a path; path text overflow control; flowing text; OpenType features; text styles.
- **Pixel persona**: pixel brushes, pixel selections (smart selection over pixel AND vector data), refine, masks, flood fill, dodge/burn/smudge/blur/sharpen brushes — "seamlessly switch to and from pixel editing mode to apply finish to vector artwork."
- **Interoperability/output**: PSD import/place/export; **Adobe Illustrator (.ai) import**; PDF import and **PDF passthrough**; place PNG/JPEG/GIF/TIFF/SVG/EPS/EXR/HDR; **SVG import and export including Inkscape extended SVG**; export slices/layers/pages/artboards to PNG/JPEG/TIFF/GIF/EPS/SVG/PDF; **automatic retina @2x/@3x export**; PDF/X hi-res CMYK printing with presets; spot colors and overprint control; bleed and printer's marks; desktop printing.
- **Resource management**: linked vs embedded resources; Resource Manager; packaging for project portability.

### Amadine — evidence layer A (official product + features pages, this pass)

Positioning: "Design Any Vector Graphics You Can Envision" — "vector graphic design software for Mac, iPad and iPhone"; lifetime license available.

Vendor-stated use cases (main page) — the breadth is the point:

- **Create Illustrations** — "solution for vector graphics developed with precision"
- **Branding & Lettering** — circular text, text on path, text in shape; vector lettering for brand identity
- **Web & User Interface** — "Perfect positioning with **Pixel Preview, Snap to Grid and Snap to Pixel** options; Smart Guides for precision of website or UI layout"
- **Print Projects** — "CMYK color mode for accurate color rendering" + export formats (SVG, PDF, EPS, TIFF, PNG, JPEG)

Structure from the Features page:

- **Tools (vendor lists 30+)**: select/modify — Move, Selection, Lasso, Eyedropper, Scissors, Eraser, Knife, Free Transform; draw/edit paths — **Pen**, Draw (combines Pencil + Brush), Width, Gradient, **Path Width** (intuitive variable stroke), Rectangle, Rounded Rectangle, Ellipse, Polygon, Star, Line, Arc; transform — Free Transform, Symmetrical/Free Distortion.
- **Sheets** (artboard-class): store multiple artworks in one document; per-sheet size/orientation/background; arrange on canvas; export sheets as separate documents.
- **Path editing**: add/remove/arrange anchor points; convert corner ↔ smooth points; edit via Knife/Scissors/Eraser and a Draw-tool mode; **Simplify Paths** (remove excessive points); **Rounded Corners** with radius/curvature tuning; **Offset Path** (evenly spaced outline around any shape/path).
- **Object editing**: position/size/rotation; shear; flip; scale strokes and effects with the object; **Boolean operations (Union, Subtract, Intersect, Exclude, Divide)**; **Isolation Mode** (edit an object separately); **Clipping Mask** (masked objects stay editable).
- **Strokes & fills**: multiple strokes and fills; savable stroke profiles; pressure-sensitive tablets + Apple Pencil; brushes with width/angle/roundness; Color/Gradient/Image fills; blend modes (vendor lists the standard set); Distinct Effects (Shadow, Inner Shadow, Blur, Inner/Outer Glow).
- **Layers**: multiple layers and sublayers; per-layer opacity; blend modes; duplicate/merge/lock/hide.
- **Text**: Text tool (distortable + boxed), Text on Path, Text in Shape; in-place editing; alignment/distribution; lists; **Flowing Text** (linked text boxes).
- **Workspace**: attached/detached panels (Mac); zoom to 6400%; guides, smart guides, **guides from path**; grids **isometric, dimetric, trimetric**; rulers; view modes **Outline Preview, Pixel Preview, Retina Preview**; iOS canvas rotation with native gestures.
- **Color**: Recolor panel (whole-design recolor); RGB + CMYK full support; color profiles for cross-device accuracy.
- **Raster integration**: **Image Trace** ("vectorize any bitmap image… colored or black vector images"); import JPEG/TIFF/PNG/HEIC + SVG/PDF/AI; Pexels/Pixabay/Unsplash stock integration.
- **Libraries**: built-in vector shape libraries; custom user libraries.
- **Import/Export**: vector SVG, PDF, AI in; save vector as **SVG and PDF**; raster JPEG/TIFF/PNG/PDF out; export document/sheet/selection; zipped native document format (.amdc) for cloud storage.
- **Distinct named features**: Fusion tool (combine multiple contours/lines into one object — vendor calls it "an alternative to boolean operations"); Variable Strokes (Width tool); Recolor panel.

### Vectr — evidence layer A (official product + FAQ + education pages, this pass)

Positioning: "AI Vector Graphics Editor and Logo Maker"; "The #1 Cloud-Based AI Vector And Logo Maker With Real-Time Collaboration." Cloud-based editor with real-time collaboration ("Collaboration is as simple as sharing a URL and working together live on various designs") and cross-device sync.

Operational facts from the official FAQ:

- "Vectr lets you **create shapes, edit paths, insert text, upload images**" plus AI features (background remover, text-to-image).
- Save/export as **SVG, PNG, JPG**; import formats **SVG, PNG, JPG, EPS, AI, PDF, SVGZ** (credit-gated for EPS/AI/PDF/SVGZ).
- "Can I create web ready graphics?" — "Yes… lightweight web ready graphics optimized for fast loading."
- Uses named: logos, icons, presentations, vector conversions.
- Works in the browser ("Vectr works on almost all browsers").

Vendor education page ("What Are Vector Graphics?"): vector graphics "use mathematical equations… translated into points connected by either lines or curves, also known as vector paths"; "scaled to any size without sacrificing image quality"; raster contrast explained; "if you're not working with digital photographs, Vector graphics editors would be your best bet for all other types of design editing."

AI-era layer (current generation): AI Vectorizer (raster→vector), Text to Vector/SVG, AI Logo Maker, background remover, image generators/upscalers. These sit on top of the editor core; the core FAQ facts above are unchanged.

Note: Vectr's user guide lives off-site (Reddit community guide, linked from the official footer); only the on-site pages were used as evidence.

### Method Draw — evidence layer A (home page, this pass; thin)

"Method Draw is a simple and easy vector editor for the web. Use Method Draw online, **no registration required**. It is open source." Served by Method of Action, whose learning games ("The Bézier Game — practice using the pen tool", "The Boolean Game — practice boolean vector operations") corroborate — at market level — that pen-path drawing and Boolean shaping are the category's signature skills worth dedicated training games.

### Adobe Illustrator — no direct evidence; market anchor (layer B)

Unreachable this pass (403) and in prior passes (timeouts ×3+). Widely-attested structural facts only, no operational claims: the industry-standard professional vector application; the product family whose name is the archetype of the category; competitor-published facts (Corel's official guide) place it in the "vector graphics software" category with bitmap-to-vector "Image Trace". Subscription licensing is competitor-published (layer B).

### Inkscape — no direct evidence; market anchor (layer B)

Unreachable (403 ×2 this pass, plus prior failures). Widely-attested facts only: free open-source desktop vector editor; named "free vector software" in Corel's official guide. No operational claims.

### Cross-referenced products (Layer A via sibling passes)

- **Linearity Curve** (illustration pass): Pen (Bézier, node types, close/finish path), Pencil (smoothing), Brush (variable width, presets, pressure), shapes with live parameters; node editing; 5 Boolean ops ("often used in Icon and Logo Design"); Shape Builder; clipping masks; Scissors; Eraser (destructive); custom vector brushes; gradients incl. mesh-style; vector effects non-destructive; text on path; convert to outlines; CMYK; PDF/SVG/EPS export; PDF editing; Auto Trace; Figma/Illustrator/Sketch compatibility.
- **CorelDRAW** (graphic-design pass): "vector illustration and page layout"; shaping/drawing tools; Contour/Envelope/Blend/Mesh Fill; PowerTRACE; object styles; multipage; fit text to path; color management/prepress; category guide "vector graphics software" listing CorelDRAW/Illustrator/Inkscape/Canva; history Sketchpad (1963) → Illustrator → CorelDRAW (1989).
- **Xara Designer Pro+** (graphic-design pass): pillars include a discrete "Illustration" pillar; QuickShape & freehand; Blend tool; soft vectors & feathering; Live Effects ("vector objects remain editable after applying effects"); ClipView masking; scatter/art brushes; 3D extrude.

---

## Cross-product Comparison

| Dimension | Affinity Designer 2 | Amadine | Vectr | Method Draw | Linearity Curve (x-ref) | CorelDRAW (x-ref) | Illustrator / Inkscape (anchors) |
|---|---|---|---|---|---|---|---|
| Self-label | "vector design app" + pixel | "vector graphic design software" | "AI Vector Graphics Editor" / SVG editor | "simple and easy vector editor for the web" | "vector design software" for "illustrators" | "vector illustration and page layout" | category "vector graphics software" (Corel guide, layer B) |
| Delivery | desktop (macOS/Windows/iPad) | Mac/iPad/iPhone native | cloud web + sync | web, no registration | Mac/iPad/iPhone native | Windows/Mac/web | desktop lineage |
| Defining object | vector objects in mixed vector/pixel docs | vector objects on sheets | vector shapes/paths in cloud docs | SVG shapes/paths | Bézier paths, open/closed/compound | vector objects, multipage | vector artwork (attested) |
| Path drawing | Precise Pen; Pencil + Sculpt; stroke stabilizer | Pen; Draw (Pencil+Brush); Width/Path Width | "create shapes, edit paths" (FAQ) | pen-class (web editor) | Pen/Pencil/Brush trio | shaping/drawing tools | Pen-class (attested) |
| Node editing | Node Tool; multi-node selection/align; handle snapping | add/remove/arrange anchors; corner↔smooth conversion | "edit paths" (FAQ) | node editing (web editor) | node tool; typed nodes | node editing in object model | attested |
| Shaping | Booleans (Add/Subtract/Intersect/Divide/Xor); non-destructive compounds; Contour; Corner | Booleans (Union/Subtract/Intersect/Exclude/Divide); Fusion; Knife/Scissors/Eraser; Offset Path; Rounded Corners | (not detailed on-site) | (minimal) | 5 Booleans; Shape Builder; masks; Scissors | Contour/Envelope/Blend | Booleans attested |
| Precision aids | snapping system; dynamic guides; isometric/axonometric grids; constraints; pixel-accurate alignment | smart guides; guides from path; isometric/dimetric/trimetric grids; snap-to-pixel; zoom 6400% | (not detailed) | (minimal) | constraint modifiers; 45° snapping | (professional aids) | attested |
| View modes | Pixel / Retina / Wireframe (Outline, X-ray); split view | Outline / Pixel / Retina | (not stated) | (not stated) | (not detailed) | (not detailed) | — |
| Canvas organization | artboards | Sheets (multi-artwork documents) | (cloud docs) | single canvas | artboard mentioned | multipage documents | artboards (attested lineage) |
| Raster integration | pixel persona; image layers; PSD/AI/PDF import; Resource Manager | Image Trace; image fills; stock libraries; AI/PDF/SVG import | image upload; AI Vectorizer | (SVG web) | Auto Trace; AI helpers; image placement | PowerTRACE; PHOTO-PAINT companion | Image Trace (layer B) |
| Typography | artistic/frame; path text; flowing; OpenType | Text/Path/Shape; flowing text; lists | "insert text" | (basic) | text on path; outlines | fit text to path; effects | attested |
| Color | CMYK/Lab/Gray/RGB; global; PANTONE; ICC | RGB+CMYK; Recolor panel; profiles | (basic) | (basic) | CMYK; palettes | color management; prepress | attested lineage |
| Output | SVG (incl. Inkscape-extended) import/export; PDF/X; EPS; slices; @2x/@3x retina; print | SVG/PDF vector out; JPEG/TIFF/PNG/PDF raster; per-sheet export; .amdc native | SVG/PNG/JPG out; EPS/AI/PDF/SVGZ in | SVG (web) | PDF/SVG/EPS; PDF editing | ~100 formats (vendor tier claim); print standard | attested lineage |
| Collaboration/cloud | — (desktop files) | — (cloud storage of .amdc) | real-time co-editing via URL; sync | — | workspaces; sync | CorelDRAW Web (subscriber) | cloud lineage (CC) |
| AI features | — | — | AI vectorizer; text-to-vector; logo maker; background removal | — | auto trace; AI grab; background removal | AI generate/remix/mask | current-gen AI (attested) |
| Business model | one-time | one-time/lifetime + store | freemium/credits | free open source | freemium/subscription | subscription + tiers | subscription (layer B) |

**Reading of the table**: every product — from the minimal no-registration web editor to the professional hybrid suite — shares one structural center: the user draws and edits **geometry-defined vector objects** in a **persistent document** using drawing instruments (pen-class, freehand, primitives) and shaping machinery (Booleans, cutting, masks), with precision aids (snapping/guides/grids/view modes), and outputs finished graphics through **standard vector interchange formats** (SVG/PDF/EPS-class) plus raster export. Around that center, products differ in delivery (desktop/native/cloud web), packaging (artboards/sheets/multipage/single canvas), raster integration depth, collaboration, AI helpers, and business model. The vendor-stated use-case breadth (Amadine: illustrations + branding + web/UI + print; Vectr: logos + icons + web graphics; Affinity: web mockups + print + artwork) is what marks the family's **general-purpose** center of gravity.

---

## Abstraction Hierarchy

### L0 — Defining Invariant

Three properties, held jointly:

1. **Vector object model as the primary editable medium.** The document holds discrete, individually addressable objects whose geometry is mathematically defined — paths built from anchor points and segments (Bézier-class), parametric shape primitives, editable text — rendered by computation rather than stored pixels, hence resolution-independent. Remove it → the product becomes a raster editor or painting studio (pixel medium) or a pixel-art tool.
2. **Direct drawing and editing of geometry.** The user authors and reshapes the objects themselves: creating paths/shapes, then modifying their geometry (moving/adding/removing anchors, adjusting handles/parameters, cutting/combining objects) with immediate visual feedback on a zoomable canvas. Remove it → the product is a viewer/converter (nothing authored) or a generation-first AI tool (the system authors the first pass).
3. **Persistent editable document with standard-format output.** Work accumulates in a re-openable document whose objects retain editability, and the result leaves the tool as usable graphics files — standard vector interchange (SVG/PDF/EPS-class) and/or raster export (or print). Remove it → an ideation whiteboard/scratchpad, or a one-shot conversion utility.

Jointly-held load-bearing checks: (1 alone = geometry viewer/3D tool territory; 2 without 1 = raster painting; 3 without 1+2 = file converter; 1+2 without 3 = sketchpad/whiteboard).

Note the deliberate convergence with the illustration-application pass's L0 (vector object model + user-authored creation + persistent document with output): **the two leaves' invariant cores converge because the market realizes one product family** — the leaves are separated by center of gravity (see Boundary Findings), not by structure.

### L1 — Common Mature Structure

Present across the sampled products; expected in any current product but not required to recognize the Type:

- **Pen/node machinery**: pen tool placing anchor points with curve handles; node/direct-selection tool (move/add/delete/convert nodes; corner ↔ smooth; per-node handle behavior); open/closed paths; multi-node selection/alignment
- **Freehand instruments**: pencil-class freehand drawing with smoothing/simplification; draw/brush tools producing vector strokes; variable-width strokes (width tool class); stroke stabilizers; pressure support where input allows
- **Shape primitives with live parameters**: rectangle (rounded), ellipse, polygon, star, line, arc
- **Shaping machinery**: Boolean operations (union/add, subtract, intersect, exclude/xor, divide-class); interactive shape-building/merging (shape-builder/Fusion class); cutting tools (knife/scissors); vector eraser; clipping masks; corner rounding; contour/offset-path; isolation mode for editing inside groups/masks
- **Strokes and fills**: multiple strokes and fills per object; gradients (linear/radial; mesh-class at the professional pole); dash/arrowheads; opacity and blend modes; non-destructive live effects (shadow, glow, blur)
- **Object organization**: layers/sublayers with stacking order, lock/hide; groups; symbol/asset libraries (built-in shape libraries; custom user libraries)
- **Transform and precision machinery**: move/scale/rotate/shear/flip; align/distribute; snapping systems (points, guides, grids); smart guides; guides (incl. guides-from-path); rulers; deep zoom; **view modes** — outline/wireframe and pixel-preview classes
- **Typography as vector content**: point text and text boxes/frames; text on path; text in shape; convert text to outlines; flowing text in several products
- **Color**: swatches; global colors; recolor-class whole-artwork recoloring; RGB and CMYK modes; color profiles (ICC-class); spot/Pantone-class support at the professional pole
- **Undo/history**; rotate canvas; keyboard modifiers
- **Raster integration**: placing images; bitmap-to-vector tracing (Image Trace/PowerTRACE/Auto Trace class); hybrid pixel-editing modes or companion pixel applications
- **Output**: native document format (preserving editability); standard vector interchange — SVG and PDF universal in current samples, EPS/AI-class common; raster export (PNG/JPEG/TIFF class); multi-scale/retina export for web assets in web/UI-oriented products; print/CMYK at the professional pole

### L2 — Variant / Optional Structure

- **Hybrid pixel capability**: a second in-document pixel mode/persona (one sampled product's headline design), or raster capability in companion suite applications, or none (minimal web editors)
- **Canvas organization**: artboards/sheets/multipage documents vs single canvas
- **Print production depth**: spot colors/overprint, bleed, printer's marks, PDF/X presets, packaging of linked resources (professional/print-vertical pole)
- **Web/UI asset production posture**: pixel preview, snap-to-pixel, multi-scale (@2x/@3x-class) export, SVG emphasis, web-ready optimization claims
- **Cloud/collaboration**: real-time co-editing via shared URL, workspaces, cross-device sync (one sampled product's core model) — absent in desktop-file and OSS poles
- **AI-era helpers**: AI vectorization, text-to-vector generation, AI logo makers, background removal (current-generation consumer pole) — layered on the editor without changing its center; distinct from classic deterministic tracing (which is L1-common)
- **Technical drawing aids depth**: isometric/dimetric/trimetric grids, axonometric plane switching, constraints — depth varies by product
- **Platform & input**: desktop/iPad/phone/web; mouse/stylus/pressure/touch
- **Business model**: subscription / one-time / freemium-credits / free OSS

### L3 — Vendor-specific Structure (research notes only)

- Affinity: **Personas** named tool-set modes; Export Persona/slices; Isometric Panel + cube mode; Wireframe/X-ray view modes; history branching with vendor-documented step bound and save-with-document; Stock panel; Resource Manager/packaging; Blend ranges; Serif Labs heritage
- Amadine: **Fusion tool** (named boolean-alternative), **Path Width** tool, **Sheets** terminology, Recolor panel, .amdc zipped document format, "Distinct Effects" bundle naming
- Vectr: AI suite naming (Nano Banana 2, Crystal Upscaler, Magic Edit), credit-gated opening of EPS/AI/PDF/SVGZ, real-time-URL collaboration model, Reddit-hosted user guide
- Linearity: color-coded nodes with named types (single/mirrored/asymmetric/disconnected), click-through mode, content integrations (Unsplash/SF Symbols/Icons8/Brandfetch), Vectornator rebrand lineage
- CorelDRAW: PowerTRACE, dockers terminology, CDR formats, tier-based format counts (vendor claims), CorelDRAW Web/Go tiers
- Xara: Live Effects, Live Copies, ClipView, soft vectors & feathering
- Adobe: "Image Trace" tool name, artboards, Appearance stack, Creative Cloud packaging (all layer B — competitor-published or widely attested)
- Method of Action: Bézier Game / Boolean Game learning games

---

## Vendor-specific Findings

See L3. Cross-pass observations:

- Packaging disagreement (hybrid single app vs suite with companions vs cloud web vs minimal OSS) over structural agreement — the classic "one Type, many packagings" pattern, consistent with the sibling passes' finding.
- No sampled vendor positions a general-purpose vector editor around a single job: Amadine states four use-case families (illustration, branding/lettering, web/UI, print); Affinity's features name web mockups, print production, and artwork alike; Vectr names logos, icons, presentations, web graphics. This contrasts with the illustration pole's artwork-centered framing (Linearity "exists for the illustrators").
- The consumer pole is currently absorbing AI generation/vectorization (Vectr), while professional poles remain tool-centered — the same editing-first/generation-first gradient the graphic-design pass recorded, observed here at the consumer end.

## Rejected Findings

- **"A vector graphics editor is an SVG editor"** — rejected. SVG is one interchange format (standardized in the web era); the historical 1980s generation used proprietary and PostScript-derived formats, and current products treat SVG as import/export among several (Affinity: SVG *including Inkscape-extended* dialects; Amadine: SVG/PDF/AI in, SVG/PDF out; Vectr: SVG/PNG/JPG out with credit-gated EPS/AI/PDF in). The canonical object is the vector object model, not a file format.
- **"A vector editor requires a Bézier pen tool"** — rejected as definitional. The mouse-era object-draw generation (MacDraw-class, 1984) satisfied the Type with primitives/lines/polylines before Bézier pen tools were universal; pen/node machinery is common mature structure (L1), not the invariant.
- **"Vector editor = illustration tool"** — rejected as an identity claim. Illustration is one job of the family (the sibling leaf's center of gravity); the same products equally serve icons, logos, UI/web assets, and print assets (vendor-stated use cases across the sample).
- **"Artboards/sheets are definitional"** — rejected; single-canvas products (Method Draw; the historical generation) satisfy the Type.
- **"Real-time collaboration is definitional"** — rejected; desktop-file, OSS, and offline-native poles satisfy the Type without it.
- **"AI vectorization/generation is definitional"** — rejected; deterministic tracing is optional-common, generative helpers are a current-generation variant.
- **"Precision machinery means CAD"** — rejected; snapping/grids/preview modes serve visual-design precision with no parametric constraints, assemblies, or manufacturing semantics.

## Boundary Findings

### vs Illustration Application (04.03 sibling — the flagged critical boundary; THREE-WAY joint review discharged here)

The market realizes **one product family** sold under the labels "vector graphics", "illustration", and "graphic design" (Corel's own guide frames the category as "vector graphics software" listing the flagships; the archetype is named "Illustrator"; Linearity self-labels "vector design software" while positioning for "illustrators"). The two 04.03 leaves' L0s converge (see Abstraction Hierarchy note). Consistent with the 04.02 raster/painting precedent (two leaves, shared machinery, primary-job gradient), this pass **ratifies keep-both with a center-of-gravity seam**:

- **This leaf (Vector Graphics Editor)**: general-purpose precision vector tooling — the editor as such, serving the full breadth of vector work (logos, icons, UI/web assets, technical/isometric drawing, print assets, artwork) with precision machinery and format interchange as first-class concerns; artwork is one use among several.
- **Illustration leaf**: the artwork-creation center of gravity — expressive drawing layer (pressure vector brushes, freehand smoothing, brush libraries) first-class; artwork-as-job.
- Removal tests: strip the artwork-creation orientation and expressive-drawing emphasis → general-purpose vector tooling (this leaf); narrow the framing from "any vector work" to expressive artwork creation → Illustration Application. Neither removal breaks the other leaf's L0 — confirming gradient, not identity.

### vs Graphic Design Application (04.01 — flagged; joint review discharged here)

Same product family at market level (flagships cited under both labels). Seam: the graphic-design leaf centers **composing design deliverables** — mixed-element compositions with typography, layout, and output machinery for visual communication; this leaf centers **drawing and editing vector geometry as such**. CorelDRAW self-labels "vector illustration **and page layout**" — the market itself names both centers. Keep-both with the center-of-gravity seam, consistent with that pass's framing.

### vs Digital Painting Application / Raster Image Editor (04.02)

Medium seam: the editable object is geometry (computed rendering, resolution-independent) vs a pixel grid (stored values, resolution-bound). Hybrids documented on both sides (pixel personas inside vector editors; vector linework layers inside painting apps) — capability overlap, not identity. Confirms the boundary recorded from the 04.02 passes' side.

### vs Font Editor (04.18)

Glyph artwork is vector geometry and font editors import vector art across this seam, but a vector graphics editor has no font project, no mapped glyph set, no em-based font geometry/metrics, and no font-file generation. Confirms the font-editor pass's seam from this side.

### vs Diagramming Application (03.05)

A vector editor's objects are freeform artwork with no semantic binding; a diagramming application's shapes come from a notation vocabulary and connectors stay attached to shapes and re-route. Removal test: give shapes meaning + glue → diagramming; strip glue → vector editor.

### vs UI Design Application (04.15)

Both share the vector substrate; a UI design application adds screen frames as canvases, component/instance semantics, and implementation handoff. A vector editor can produce UI mockup assets (pixel-accurate alignment, snap-to-pixel — vendor-documented) without any of that machinery.

### vs Mechanical CAD (16; conceptual, not directly researched)

Precision machinery in a vector editor serves visual design (snapping, grids, preview modes); CAD geometry carries parametric constraints, assemblies, manufacturing dimensions/tolerances, and engineering change semantics. A vector editor draws isometric artwork; it does not model manufacturable parts. Boundary asserted conceptually at family level.

### vs 3D Modeling Application (04.13)

2D plane geometry vs 3D space/solids/materials; 3D-extrude-class object effects and isometric grids are vector-tool capabilities, not 3D modeling.

### vs Desktop Publishing / Page Layout Application (04.17)

Object drawing is the core here; there, vector art is placed content within a page/flow/publication model (confirmed by that family's recorded boundary wording).

### vs Template-based Design Platform (04.01)

Freeform authoring from a blank canvas vs browsed pre-made compositions constrained for non-designers; templates appear in vector editors as optional starters, never as the organizing structure.

### vs AI Image Generator / AI Design Generator (04.20)

Authoring-first (user draws/edits the geometry) vs generation-first (system composes the first pass from a description). Vectr demonstrates a consumer vector editor absorbing generative helpers without flipping the center: its FAQ still defines the core as "create shapes, edit paths, insert text."

### vs Collaborative Canvas / Digital Whiteboard (03.05)

Whiteboards are ideation surfaces without production fidelity (layers, precision machinery, standard-format finished output). Strip production/output machinery → whiteboard.

### "去掉什么就变成另一个 Type" removal tests (summary)

- Remove vector object model → Digital Painting Application / Raster Image Editor / Pixel Art Editor
- Remove user geometry authoring (generation-first) → AI Image Generator / AI Design Generator
- Remove persistent document + standard output → whiteboard/scratchpad or one-shot converter
- Narrow the frame from any vector work to expressive artwork creation → Illustration Application (sibling — keep-both ratified)
- Add design-deliverable/layout/typography semantics as the center → Graphic Design Application (keep-both ratified)
- Add glyph set/character mapping/font geometry/font generation → Font Editor
- Add notation vocabulary + connector binding → Diagramming Application
- Add screen frames/components/handoff → UI Design Application
- Add parametric constraints/manufacturing semantics → Mechanical CAD
- Constrain geometry to a pixel grid → Pixel Art Editor

---

## Historical / Market-Sample Check (§24)

- **1980s mouse-era object-draw generation** (MacDraw 1984-class): discrete objects, selection/direct manipulation, persistent documents, print/PICT output — no Bézier pen, no color depth, no SVG, no artboards, no cloud. Satisfies the L0 → Bézier pen machinery and SVG stay OUT of the core. ✔
- **Bézier generation** (Illustrator 1987 / FreeHand / CorelDRAW 1989 — documented history per Corel's official guide, Sketchpad 1963 lineage): single-canvas persistent documents, pen-drawn paths, export to PostScript/proprietary formats. Satisfies the L0 without any current-gen machinery. ✔
- **Free/OSS desktop pole** (Inkscape): satisfies conceptually (anchor-only evidence; no operational claims made). ✔ (moderate confidence)
- **Minimal web pole** (Method Draw): no registration, browser, SVG — satisfies with a subset of L1. ✔
- **Cloud consumer pole** (Vectr, AI-era form): satisfies through its FAQ-stated core (create shapes, edit paths, insert text, export SVG/PNG/JPG) despite the AI-pivoted presentation. ✔
- **Regional/mobile-first products** (Linearity lineage; Amadine): same core on Apple-ecosystem native delivery. ✔
- **Early consumer clip-art studios**: template-driven composition without freeform geometry authoring do NOT satisfy L0 property 2 — correctly excluded (consistent with sibling passes). ✔
- The definition is delivery-agnostic, licensing-agnostic, format-agnostic (native formats + standard interchange), collaboration-agnostic, and AI-agnostic.

## Uncertainties

1. **The three-way joint-review disposition** (keep-both with center-of-gravity seams for graphic-design-application / illustration-application / vector-graphics-editor) is this pass's ratification from the vector-editor side; final directory decisions belong to the maintainers. Recorded in STATUS.md Boundary Issues.
2. **Adobe Illustrator operational structure unverified** (403/timeouts across four passes). Widely-attested facts only; no claim in this document depends on Illustrator internals.
3. **Inkscape operational structure unverified** (403 across passes). Anchor only.
4. **Method Draw evidenced only from its home page** — the editor is a JS application; internals not fetched. Its L1 coverage is asserted minimally (self-description as a vector editor; SVG web context).
5. **Vectr's marketing-heavy presentation**: only FAQ/education-page operational facts were used; AI-suite claims treated as current-generation variant material, not structure.
6. **Affinity behaviors evidenced at intro/key-features level** (help TOC per the illustration pass); fine-grained behaviors not asserted beyond the feature list.
7. **CAD boundary asserted conceptually** (no CAD product fetched); low risk given the family-level difference.
8. **No market-share/prevalence claims** — none gathered.

## Final Synthesis

A **Vector Graphics Editor** is an application in which the user creates and edits **vector graphics** — discrete, geometry-defined objects (Bézier-class paths with anchor points and handles, parametric shape primitives, editable text) rendered by computation rather than stored pixels — inside a **persistent, re-openable document**, using drawing instruments (pen-class path tools, freehand tools with smoothing, shape primitives) and reshaping machinery (node editing, Boolean operations, cutting, masking), supported by precision aids (snapping, guides, grids, outline/pixel view modes), and finishing work as **standard-format output** (SVG/PDF/EPS-class vector interchange, raster export, print at the professional pole).

Around this defining core, mature products add: freehand variable-width strokes and brushes, multi-stroke/multi-fill styling with gradients and non-destructive effects, layer/group organization with symbols and asset libraries, typography as vector objects, color systems up to CMYK/spot/print discipline, raster integration (placement, bitmap-to-vector tracing, hybrid pixel modes), artboards/multipage canvases, cloud collaboration, and — in the current consumer generation — AI helpers for vectorization and generation.

The Type's honest market statement: **the market sells one vector product family under the labels "vector graphics", "illustration", and "graphic design"; the directory holds three leaves over this family, and this leaf carries the general-purpose precision tooling center of gravity** — the editor as such, serving the full breadth of vector work (logos, icons, UI/web assets, technical/isometric drawing, print assets, artwork) rather than any single job. This pass ratifies keep-both(-three) with center-of-gravity seams, mirroring the 04.02 raster/painting precedent, and discharges the two pre-hung joint-review flags.
