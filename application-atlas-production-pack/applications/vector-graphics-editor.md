# Vector Graphics Editor

## Overview

A **Vector Graphics Editor** is a general-purpose application for creating and editing **vector graphics** — images composed of geometry-defined objects that remain individually editable and render sharply at any size. Its editable material is not a grid of pixels but **vector objects**: paths made of anchor points and curve segments, parametric shape primitives, and text. The user draws and reshapes these objects directly on a canvas, composes them in a persistent, re-openable document, and finishes the work as graphics files in standard formats.

The defining structure is small:

```text
Vector Document
└── Vector objects (paths of anchor points, shape primitives, editable text)
    └── Direct drawing & editing (the user authors and reshapes the geometry)
        └── Persistent document + standard output
            (re-openable work; vector interchange formats, raster export, print)
```

Everything commonly associated with modern products — Bézier pen tools, Boolean shaping, layers, snapping systems, artboards, CMYK print discipline, cloud collaboration, AI helpers — is widespread today but is not part of the defining core. Simpler and older products without any of those (the mouse-era object-drawing lineage, minimal browser editors) still fit this definition.

One naming caution matters when reading the market: vendors sell one product family under several labels — "vector graphics", "illustration", and "graphic design" are used interchangeably for the same flagships. This document describes that family from the general-purpose vector tooling center of gravity: the editor as such, serving the full breadth of vector work — logos, icons, web and UI assets, technical and isometric drawing, print assets, and artwork alike. Its closest sibling Types are flagged in Related Application Types.

When the organizing job shifts — to composing design deliverables with typography and layout machinery, to expressive artwork creation as the craft itself, to painting pigment, to editing the pixels of existing images, or to generating images from prompts — the product is drifting toward a different Application Type (Graphic Design Application, Illustration Application, Digital Painting Application, Raster Image Editor, AI Image Generator).

## Users & Context

The primary user is anyone who needs to **author scalable graphics from geometry**:

- **graphic designers** — logos, icons, brand marks, and reusable vector assets
- **web and UI designers** — interface assets, web-ready graphics sized precisely for screen output
- **illustrators** — artwork drawn as editable objects rather than painted pixels
- **marketing and content operators** — banners, presentations graphics, social assets, print collateral
- **technical and hobbyist users** — diagrams, isometric artwork, signage, engraving and cutting layouts

The work environment is a single user in front of a canvas, typically with a mouse or stylus. Work is session-based and iterative: create or import objects, refine their geometry, inspect at deep zoom, adjust, export. Collaboration where present (shared cloud documents, real-time co-editing) is a variant surface, not the core loop — most products remain single-user file-based tools.

## Core Model

### The Defining Core

```text
Vector Document
└── Vector objects (paths of anchor points, shape primitives, editable text)
    └── Direct drawing & editing (the user authors and reshapes the geometry)
        └── Persistent document + standard output
```

Three properties, held jointly. If any one is removed, the product is no longer recognizable as a vector graphics editor:

- **Vector object model.** The document holds discrete, individually addressable objects whose geometry is mathematically defined — rendered by computation rather than stored pixels, hence resolution-independent: an object can be scaled arbitrarily without losing fidelity. Without this, the product is a raster editor or painting studio.
- **Direct drawing and editing of geometry.** The user creates the objects and then modifies their geometry — drawing paths, placing shapes, moving and converting anchor points, adjusting curves, cutting and combining objects — with immediate visual feedback. Without this, the product is a viewer/converter (nothing authored) or a generation-first AI tool (the system authors the first pass).
- **Persistent document with standard output.** Work accumulates in a re-openable document whose objects stay editable over time, and the result leaves the tool as usable graphics: standard vector interchange formats, raster image export, or print. Without this, the product is an ideation whiteboard or a one-shot conversion utility.

### Standard Capabilities of Mature Products

A typical modern vector editor carries most of the following. They are not what makes the product a vector editor, but they make the work practical. All are documented across the researched sample; the minimal and historical products lack some and remain vector editors.

- **Pen and node machinery** — a pen tool places anchor points joined by straight or curved segments; a node (direct-selection) tool moves, adds, deletes, and converts anchor points (corner ↔ smooth) and drags curve handles; paths may be open or closed, and several products support multi-node selection and alignment.
- **Freehand instruments** — pencil-class tools that follow the hand and simplify/smooth the resulting path; brush-class tools producing variable-width vector strokes; stroke stabilizers; pressure sensitivity where the input device supports it.
- **Shape primitives with live parameters** — rectangle (often with corner rounding), ellipse, polygon, star, line, arc — editable after placement.
- **Shaping machinery** — Boolean operations (union, subtract, intersect, exclude/divide classes) to combine objects; interactive shape-building/merging; cutting tools (knife/scissors class) that split paths; a vector eraser; clipping masks that crop artwork to a shape; contour/offset-path and corner tools that derive new geometry from existing shapes.
- **Strokes and fills** — stroke width, dash patterns, arrowheads; multiple strokes and fills per object in several products; solid colors, gradients (linear/radial, with mesh-class gradients at the professional pole), and image fills; opacity and blend modes; live effects (shadow, glow, blur) that remain adjustable.
- **Object organization** — a layers panel with stacking order (front to back), groups, sublayers, lock/hide states; symbol/asset libraries holding reusable elements, both built-in and user-defined.
- **Transform and precision machinery** — move/scale/rotate/shear/flip; align and distribute; snapping to points, guides, and grids; smart guides; rulers; very deep zoom; and view modes — outline/wireframe previews that show bare geometry, and pixel previews that simulate how the artwork rasterizes on screen.
- **Typography as vector content** — point text and text boxes; text on a path; text in a shape; many products can convert text to curves/outlines, trading text editability for pure geometry.
- **Color systems** — swatches and palettes; global colors (change one definition, update every use); whole-artwork recoloring; RGB for screen work and CMYK for print, with color profiles; spot-color-class support at the professional pole.
- **Undo / history** — editing actions recorded and reversible; history panels in mature products.
- **Raster integration** — placing bitmap images inside the document; bitmap-to-vector tracing that converts images into editable paths; several products add a pixel-editing mode or rely on companion pixel applications.
- **Output** — a native document format that preserves full editability; standard vector interchange (SVG and PDF are universal in current products; EPS and AI-format import are common); raster export in standard image formats; multi-scale export for screen assets; print capability with CMYK color at the professional pole.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. Implementations vary:

```text
Concept:            Vector object model
Implementations:    Bézier path objects; parametric primitives; editable text;
                    hybrid documents that also carry bitmap image layers

Concept:            Path authoring
Implementations:    pen tool (placed anchors + handles); freehand tools with
                    smoothing; live-parameter shape primitives; tracing imported bitmaps

Concept:            Reshaping
Implementations:    node editing; Boolean operations (destructive in some products,
                    non-destructive "compound" objects in others); shape building;
                    knife/scissors cutting; masks; corner/contour/offset tools

Concept:            Precision
Implementations:    snapping systems; smart guides; grids (including isometric-class);
                    view modes (outline / pixel preview); numeric transforms; deep zoom

Concept:            Output
Implementations:    native formats (each product's own); SVG/PDF/EPS-class interchange;
                    raster export incl. multi-scale screen sizes; CMYK/print
```

A reader who has only seen one product should still be able to recognize any other vector editor from the Core Model.

## How It Works

### Start the document

```text
Create a new document (or open/import one)
→ optionally set up artboards/sheets for multiple artworks in one file
→ optionally place or trace reference images
```

### Draw the objects

```text
Choose an instrument (pen / freehand / shape primitive)
→ create paths and shapes on the canvas
→ adjust while drawing (modifier keys, smoothing, handle manipulation)
```

### Refine the geometry

```text
Switch to the node tool
→ move / add / delete / convert anchor points, drag curve handles
→ combine or cut objects (Boolean operations, shape building, knife/scissors)
→ mask or clip artwork to shapes; round corners; offset contours
```

### Compose and organize

```text
Group related objects
→ order them front-to-back in layers
→ store repeated elements as symbols/assets
→ enter groups or masks in isolation mode to edit inside them
```

### Apply appearance

```text
Set strokes, fills, gradients, transparency
→ add live effects (shadow, glow, blur)
→ add and format text; place text on paths
→ define colors as swatches/global colors for consistent reuse
```

### Precision pass

```text
Align and distribute objects
→ enable snapping / smart guides / grids
→ switch to outline view to inspect bare geometry
→ switch to pixel preview to check how the artwork rasterizes on screen
```

### Finish: save and export

```text
Save the working document in the native format (editability retained)
→ export to standard vector formats (SVG / PDF / EPS-class) for interchange and print
→ export raster versions (PNG / JPEG / TIFF-class) in the needed sizes
→ optionally print directly with CMYK color management (professional products)
```

The heart of the application is the middle loop — **draw → refine → compose** — repeated many times per document, often over days or years: a well-built vector file remains fully editable long after it was first drawn.

### Core vs standard vs optional

**Defining core** — without these, not a vector graphics editor:

- vector object model (geometry-defined, individually editable objects)
- direct drawing and editing of geometry
- persistent document
- standard-format output (vector interchange and/or raster export)

**Standard mature structure** — present in most modern products:

- pen/node machinery; freehand instruments; shape primitives
- Boolean/shaping machinery; masks
- strokes/fills/gradients; blend modes; live effects
- layers, groups, symbols/assets
- snapping/guides/grids; view modes; align/distribute
- typography as vector objects
- swatches/global colors; RGB/CMYK
- undo/history; raster integration (place, trace)
- native format + SVG/PDF-class interchange + raster export

**Optional / variant** — depends on segment, philosophy, and era:

- hybrid pixel editing modes; companion pixel applications
- artboards/sheets/multipage documents
- print production depth (spot colors, overprint, bleed, PDF/X presets)
- multi-scale/retina export and web-asset postures
- real-time collaboration, cloud workspaces, cross-device sync
- AI helpers (vectorization of images, prompt-based generation, background removal)
- isometric/axonometric grid systems and other technical drawing aids
- pressure/stylus input; platform (desktop/tablet/web); business model

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Canvas (document window)

The primary surface.

- the artwork at zoom/pan, with deep zoom for fine anchor work
- in-canvas handles for selected objects, anchors, and curve segments
- primary actions: draw, select, move, transform, reshape

### Toolbox

The instrument switcher.

- grouped tools: selection, direct/node selection, pen, freehand, shapes, text, fill/stroke, knife/eraser-class, zoom
- primary actions: choose the active instrument

### Context / tool options

Options for the active tool.

- parameters like smoothing, corner radii, polygon sides, star points, stroke profiles
- primary actions: tune instrument behavior before or while drawing

### Layers / objects panel

The document's structure map.

- ordered stack of layers, sublayers, groups, and objects; top = front
- per-object visibility, lock, opacity
- primary actions: select, reorder, group/ungroup, duplicate, isolate, add masks

### Appearance / stroke / fill panels

The object's visual recipe.

- multiple strokes and fills per object where supported; gradient editors; effect lists
- primary actions: add/edit/remove strokes, fills, gradients, live effects

### Color and swatches

Color selection and reuse.

- color pickers/models (RGB/CMYK), palettes, global colors, recoloring tools
- primary actions: apply colors; define reusable color definitions

### Libraries / assets / symbols

Reusable element storage.

- built-in shape libraries and user-saved objects
- primary actions: place, save, organize reusable graphics

### Transform / align

Numeric precision surface.

- exact position, size, rotation, shear values; align/distribute controls
- primary actions: precise placement and arrangement

### View-mode and zoom controls

Inspection aids.

- outline/wireframe and pixel-preview toggles; zoom level; rulers/guides/grid visibility
- primary actions: switch how the artwork is displayed for inspection

### Export dialog

The output surface.

- format selection (vector/raster), areas or artboards/sheets to export, sizes/scales
- primary actions: export selections or whole documents to interchange and raster formats

## Important Rules / Behaviors

### Geometry stays live

Objects remain re-editable at any time — a path drawn years ago can be re-opened and reshaped anchor by anchor. This durability of editability is the economic core of the Type (assets are maintained, not redrawn). Two deliberate exceptions exist in most products: converting text to outlines/curves replaces the text object with pure geometry (the text is no longer editable as text), and some Boolean operations replace the original objects with the resulting shape — though several products now offer non-destructive "compound" variants that keep originals editable.

### Edits apply to the selection

The tool acts on the currently selected object(s). Objects nested in groups or masks may need an isolation mode to be reached; forgetting the nesting is a common source of "nothing happens" confusion.

### Stacking order changes the result

The same objects render differently depending on front-to-back order, opacity, and blend mode; reordering is itself an edit.

### Resolution independence is the point — and has limits

Vector objects scale without loss of fidelity; bitmap content placed inside the document does not share that property, and at export the artwork is rasterized into a grid at a chosen size. Pixel-preview view modes exist precisely because screen output rasterizes — artwork meant for screens is checked against the pixel grid.

### Native format preserves editability; interchange may not

The native document format retains layers, groups, live effects, and text. Standard interchange formats carry the geometry well but may flatten structure or drop product-specific features; exporting to raster fixes pixels permanently. The save/export distinction is structural, not a product quirk.

### Undo has limits

History is bounded (some products allow saving history with the document; others cap its depth); certain operations (flattening, some conversions) sit outside undo in various products.

## Variants

The Type is realized in several common forms:

- **professional desktop editor** — the full standard capability set plus print production depth, color management, and hybrid pixel capability; the reference segment for print and brand work
- **hybrid vector+pixel single application** — vector and raster editing combined in one document (one product family's headline design)
- **professional suite member** — the vector editor as one pillar of a wider design suite with companion pixel/photo/layout applications
- **free open-source desktop editor** — the same core model, community-developed
- **minimal web editor** — a no-registration browser tool carrying the core with a reduced standard set
- **cloud collaborative editor** — the core delivered as a shared, synced web workspace with real-time co-editing
- **tablet-native editor** — the core on pen-driven tablets/phones with touch gestures
- **AI-augmented consumer editor** — the core plus AI vectorization, prompt-based vector generation, and automated cleanup; the editing core remains the structure

A variant remains a **Variant**, not a separate Type, unless it changes users, core objects, workflow, or rules so much that the Core Model no longer applies.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Illustration Application | sibling; **joint review recommended** (same directory section) | the market sells one vector product family under both labels; this leaf carries the general-purpose precision tooling center of gravity (any vector work), the sibling carries the artwork-creation craft center (expressive drawing first-class, artwork as the job) |
| Graphic Design Application | sibling-family seam; **joint review recommended** | the graphic-design center is composing design deliverables (typography + layout + output machinery for communication); this leaf centers drawing and editing vector geometry as such; flagship products straddle both labels |
| Digital Painting Application | different medium | painting's marks are raster pigment; here the artwork is geometry-defined objects |
| Raster Image Editor | different medium | the raster editor modifies existing pixel data on a pixel grid; this editor authors resolution-independent geometry |
| Pixel Art Editor | different constraint | pixel-art tools constrain artwork to a pixel grid and palette — the opposite of free resolution-independent geometry |
| Font Editor | adjacent | glyph artwork is vector geometry, but a font editor adds the glyph set with character mapping, font geometry, metrics, and font-file generation — all absent here |
| Diagramming Application | adjacent | diagramming shapes come from a notation vocabulary and connectors stay attached and re-route; this editor's objects are freeform artwork with no semantic binding |
| UI Design Application | adjacent | shares the vector substrate but adds screen frames, component/instance semantics, and implementation handoff — none of which exist here |
| Desktop Publishing / Page Layout Application | adjacent | there, vector art is placed content inside a page/flow/publication model; here, object drawing is the core |
| Template-based Design Platform | adjacent | template platforms organize work around browsed pre-made compositions for non-designers; here the user authors freeform from a blank canvas (templates at most optional starters) |
| AI Image Generator / AI Design Generator | adjacent | generation-first (system composes the first pass from a description) vs authoring-first (the user draws and edits); AI helpers inside a vector editor do not flip the center |
| Mechanical CAD | conceptual boundary | CAD geometry carries parametric constraints, assemblies, manufacturing dimensions and change semantics; vector-editor precision serves visual design without engineering semantics |
| Digital Whiteboard / Collaborative Canvas | weaker | ideation surfaces without production fidelity (layers, precision machinery, finished standard-format output) |

The two sibling seams are the most important. The honest statement, corroborated across the researched passes: **the market does not cleanly separate the "vector graphics", "illustration", and "graphic design" labels** — the same flagship products are cited under all three. The directory's leaves are best understood as centers of gravity over one shared product family: composing deliverables (graphic design), creating expressive artwork (illustration), and general-purpose precision vector tooling (this leaf). None of the three centers changes the other's defining core — which is why they are gradients between sibling leaves, not feature walls between unrelated Types.

## Representative Products

- Adobe Illustrator — professional desktop vector editor; the market archetype (official documentation not reachable on the research date; included as a widely-attested market anchor)
- Inkscape — free open-source desktop vector editor (same sourcing limitation; market anchor)
- Affinity Designer — professional one-time-purchase vector editor with hybrid pixel capability
- Amadine — Apple-ecosystem vector design application (Mac/iPad/iPhone)
- Vectr — cloud-based web vector editor with real-time collaboration
- Method Draw — minimal open-source web vector editor

The Core Model was checked against the historical mouse-era object-drawing generation (no pen tools, no SVG, no color management) and the minimal web pole to avoid over-fitting the definition to the modern professional feature set.

## Sources

Research date: **2026-09-09**

Official documentation directly consulted:

- Affinity Designer 2 Help — What is Affinity Designer 2? — https://affinity.help/designer2/en-US.lproj/pages/Introduction/about_designer.html
- Affinity Designer 2 Help — Key Features — https://affinity.help/designer2/en-US.lproj/pages/Introduction/keyFeatures.html
- Amadine — product page — https://amadine.com/ and Features — https://amadine.com/features
- Vectr — product page and FAQ — https://vectr.com/ ; "What Are Vector Graphics?" — https://vectr.com/en/what-are-vector-graphics
- Method of Action / Method Draw — https://method.ac/

Official documentation consulted via the paired sibling passes (cross-referenced evidence):

- Linearity Curve product page and user guide (drawing/editing/shaping tools) — URLs in research/illustration-application.md
- CorelDRAW product, family, and educational-guide pages; Xara Designer Pro+ pages — URLs in research/graphic-design-application.md

> Sourcing limitation: official documentation for Adobe Illustrator (helpx.adobe.com) and Inkscape (inkscape.org) could not be fetched from the research environment on the research date (HTTP 403; timeouts also recorded in prior passes). Boxy SVG and SVG-Edit were also unreachable and excluded. These products are retained as representative market anchors only; no product-specific operational claims about them appear in this document, and assertion strength is calibrated accordingly.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, rejected findings, and the historical / market-sample breadth check are recorded in the paired Research Notes.
