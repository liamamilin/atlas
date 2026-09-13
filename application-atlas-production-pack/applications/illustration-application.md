# Illustration Application

## Overview

An **Illustration Application** is an application for creating illustration artwork — characters, scenes, logos, icons, decorative and explanatory art — by drawing **vector objects**: paths, shapes, and text whose geometry is mathematically defined, stays individually editable, and renders cleanly at any size.

The defining core is small:

- the artwork is composed of **discrete vector objects** (curve-based paths, shape primitives, editable text), not pixels;
- the user **authors the artwork by drawing** — the first pass is made by the user's own hand, object by object, normally starting from a blank canvas;
- the work lives in a **persistent, re-openable document** in which every object remains editable, and the workflow ends in **finished artwork output** (export or print).

Everything else commonly associated with these products — pressure-sensitive brushes, freehand smoothing tools, Boolean shaping, artboards, cloud collaboration, AI tracing, CMYK print pipelines — is standard or optional capability in current products, not what makes the product an illustration application. The definition is deliberately independent of platform (desktop, tablet, phone, web), licensing (subscription, one-time purchase, free and open source), and era: the vector illustration tools of the 1980s and 1990s satisfy it without any modern feature.

One naming caution matters when reading the market: vendors sell one product family under the labels "vector graphics" and "illustration" interchangeably. This document describes that family from the illustration center of gravity — artwork creation as the job — and its closest sibling Type, the Vector Graphics Editor, is flagged for joint review (see Related Application Types).

## Users & Context

Primary users are people making artwork as the deliverable:

- **illustrators** producing character art, scenes, spot illustrations, and editorial or book artwork;
- **logo and icon designers** drawing marks that must scale from favicon to billboard;
- **artists and hobbyists** drawing for print, merchandise, embroidery, laser cutting, and social content;
- **designers drawing artwork components** (mascots, decorative elements, lettering) that later flow into broader design work.

The work session is typically solitary and craft-oriented: long, iterative drawing sessions in which the artist builds and refines objects over days or weeks, returning to a saved document each time. Inputs vary — a blank canvas, a placed sketch or photo to trace, an imported file from another tool. Outputs leave the tool as vector formats (for further production or handoff), raster images (for screens), or print-ready files.

Secondary contexts: print and signage shops using the same tools for production artwork; apparel and embroidery workflows where clean vector lines drive cutting and stitching machines; brand teams maintaining scalable logo systems.

## Core Model

### The Defining Core

```text
Document (persistent, re-openable)
└── Canvas / Artboard
    └── Vector Objects  ← the artwork
        ├── Path (anchor points + curve handles)
        ├── Shape primitive
        └── Editable text object
    ├── Stacking order / Groups / Layers
    └── Styling: fill · stroke · gradient · transparency · effects
        ↓
Rendered output (vector / raster / print)
```

Four load-bearing ideas:

- **The vector object model.** Every element of the artwork is an object whose shape is described by geometry — anchor points connected by curves, parametric shapes — rather than by a grid of stored pixels. The application renders the objects on screen; because rendering is computed, the same artwork scales from a small icon to a large banner without pixelation. This is the property that separates the Type from raster brush painting, where marks are pigment deposits on a pixel canvas.
- **Objects stay editable.** A path drawn months ago can be reopened and its anchor points adjusted; a shape's fill, stroke, and effects can be changed without redrawing it. Editability over time — not just at creation — is what makes the document a working asset rather than a picture.
- **The user makes the first pass.** The application is an authoring instrument. Whatever assistance exists (templates, tracing, AI helpers), the artwork originates from the user's drawing decisions. This separates the Type from generation-first tools.
- **Document and output.** Work persists in a native document format that preserves full editability, and the point of the work is a finished artifact: exported vector files, raster images at chosen sizes, or print. A drawing surface without persistence or output is a scratchpad, not this Type.

### Standard Capabilities of Mature Products

These appear across the researched products and make the core practical, but no single one is required to recognize the Type:

**Drawing instruments**

- a **Pen-class tool** for placing anchor points and pulling curve handles — the precise way to draw Bézier paths;
- **freehand tools** (pencil-class) that follow the hand and then smooth/simplify the drawn path;
- **vector brushes** — pressure-sensitive, variable-width strokes that give hand-drawn expressiveness while remaining vector objects; brush presets and custom brush creation are common in illustration-oriented products;
- **shape tools** — rectangles, ellipses, polygons, stars, lines, spirals, often with live parameters (corner radius, point count).

**Path and object editing**

- a **node/direct-selection tool** for editing individual anchor points and their handles (moving, adding, deleting, converting; opening and closing paths);
- cutting and splitting tools (scissors-class, knife-class) and erasing tools;
- **Boolean shaping** — combining overlapping shapes by unite/subtract/intersect-type operations, often with an interactive shape-builder mode; clipping masks that crop artwork to a shape's boundaries.

**Styling**

- fills, strokes (width, dash patterns, arrowheads), gradients (linear and radial; mesh-class gradients in professional products), transparency;
- color systems: swatches and palettes; global and spot colors and color management at the professional pole;
- **non-destructive live effects** on objects — shadows, blurs, contours, blends — that remain editable and removable.

**Composition**

- stacking order (z-order), grouping, layers, per-object opacity and blend modes;
- alignment, distribution, snapping, guides and grids, precise numeric transforms;
- reusable element libraries (symbols/assets) in many products.

**Typography as artwork**

- text as editable vector content: point text and frame text, text on a path, and conversion of type to outlines when lettering must become pure artwork.

**Raster integration**

- placing bitmap images inside the document (as reference, texture, or masked content);
- **bitmap-to-vector tracing** that converts sketches or photos into editable paths;
- raster-side painting or retouching either in a second tool mode (some products) or a companion application (suite packaging).

**Precision and output**

- undo/history and canvas navigation (zoom, rotate);
- native document format plus standard vector interchange (SVG, EPS, PDF) and raster export at chosen scales; print capability with professional color discipline where print production matters.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:   vector object        →  implementations: Bézier paths with anchor
                                   points/handles, parametric shapes, text objects

Concept:   drawing instrument   →  implementations: pen tool, smoothed pencil,
                                   pressure-sensitive vector brush, parametric
                                   shape tools

Concept:   document container   →  implementations: single canvas, artboards,
                                   multi-page documents

Concept:   raster integration   →  implementations: second tool mode in the same
                                   app, companion pixel application, tracing,
                                   placed images only

Concept:   delivery             →  implementations: desktop app, tablet/phone app,
                                   web app; offline files or cloud-synced projects
```

A reader who has only seen a modern tablet drawing app should be able to recognize the 1990s desktop ancestor — and vice versa — from this model.

## How It Works

### The drawing loop

The central interaction loop of the Type:

```text
Start a document (blank canvas, artboard, or placed reference)
→ draw objects (pen paths · freehand strokes · brush strokes · shape primitives)
→ refine geometry (edit anchor points and handles · smooth · reshape)
→ shape combinations (Boolean ops · shape builder · masks · cutting)
→ style objects (fill · stroke · gradient · transparency · live effects)
→ compose (stacking · groups · layers)
→ repeat until the artwork is done
→ export / print
```

Two properties make the loop productive: **everything stays editable** (the artist can return to any earlier decision by editing objects, not repainting), and **the render is computed** (the same artwork serves a 16-pixel icon and a poster).

### Building complex forms from simple parts

Illustration rarely draws final shapes in one stroke. The characteristic workflow composes: draw rough overlapping primitives → combine or carve them with Boolean operations or an interactive shape-builder → smooth and node-edit the result → apply live effects for dimension. Masks crop artwork into containers; corner-rounding and contour-type modifiers turn hard geometry into finished forms.

### Tracing and hybrid raster work

A common entry path starts outside the vector world: a pencil sketch or photo is placed on the canvas and either traced by hand with pen/freehand tools on top, or auto-traced into editable paths by the application. Products differ in how far the raster world reaches into the tool — some keep raster to placed images and tracing; others offer a full pixel-painting mode beside the vector mode in the same document, with the vector editing retained throughout.

### Finishing and output

```text
Choose output → vector file (SVG/EPS/PDF-class) for production or handoff
             → raster export at chosen sizes for screens
             → print with color discipline (CMYK-class) where print matters
```

Professional-context products add print-production machinery around this step: bleed, spot colors, preflight-class checks, and packaging of the document with its linked resources.

## Interfaces

Described conceptually; exact layout and naming vary by product.

### Canvas / artboard

The main surface.

- the artwork at zoom, navigable and rotatable in most products;
- rulers, guides, grids; snapping indicators while drawing;
- primary actions: draw, select, transform, edit objects directly.

### Toolbar (drawing instruments)

The instrument rack, usually persistent.

- selection and node tools, pen, pencil, brush, shape tools, shaping tools (scissors/knife/eraser/shape-builder), text, plus view tools;
- per-tool context options appear beside it (e.g., smoothing strength for the pencil, parameters for shape tools).

### Inspector / style panels

Where object appearance is set.

- fill and stroke sections, gradient editing, transparency, effect stacks;
- object-level properties (opacity, blend mode, corner parameters);
- color swatches and palettes.

### Layers / objects panel

The document's structure map.

- object tree with stacking order, groups, layers, masks;
- visibility, locking, renaming; isolation modes for working inside groups.

### Node editing surface

The geometry-level view of a path.

- visible anchor points and handles on the selected path;
- per-node handle behavior; add/delete points, open/close path actions.

### Export / output surfaces

- export dialog or dedicated export workspace (some products) with format, scale, and slice-level choices;
- print setup with color management at the professional pole.

### Document management

- document setup (size, units, color mode), templates; artboard management where the product offers multiple canvases;
- cloud project libraries and workspace/team surfaces in collaboration-enabled products.

## Important Rules / Behaviors

- **Editing is object-level and durable.** Selecting an object edits that object; geometry edits (node moves) and style edits both persist in the document. Most operations are non-destructive — live effects can be removed or re-parameterized later. Local exceptions exist: in one researched product the freehand eraser is explicitly destructive (a single undo step), while path-splitting tools remain non-destructive — products differ on where destructiveness sits, and it is a real behavioral difference the user learns.
- **Stacking order decides rendering.** Objects composite from the bottom of the stack up; z-order changes, groups, and masks are the main compositional controls. Masks confine content to a container shape; content outside is hidden, not deleted.
- **Booleans restructure objects.** Combine/subtract-type operations produce new object structure from overlapping shapes; several products keep the operation reversible (compound form) while others commit it — reversibility varies by product.
- **Resolution independence is structural, not an export option.** Scaling changes object geometry, never quality; rasterized results only appear where a raster effect or placed bitmap is involved, and some products let users force rasterization deliberately for problematic effects.
- **Text is artwork only after conversion.** Live text keeps font dependency and editability; converting type to outlines makes it pure paths — no longer font-bound, no longer re-typeset. This trade-off is a deliberate user decision.
- **Interchange has fidelity boundaries.** Standard formats (SVG/EPS/PDF) move artwork between tools, and importing competitors' native formats is common, but effect- and feature-specific behavior may not survive interchange — professional workflows plan around this.
- **Input determines expressiveness, not capability.** Pen/stylus pressure drives brush width variation where supported; the same tools work with mouse/trackpad. The instrument set is input-agnostic.

## Variants

- **Professional print-oriented suites** — the drawing application bundled with pixel-editing, font management, and tracing companions; deepest print/color/prepress machinery; verticals like signage, apparel, engraving.
- **Single hybrid applications** — vector drawing with a pixel mode in one document; one-time-purchase licensing has been a hallmark of this pole.
- **Tablet/mobile-first products** — touch and stylus-native instruments, gesture-driven, cloud-synced projects, positioned explicitly for illustrators.
- **Free open-source editors** — full vector toolkits without commercial content libraries or support.
- **Web-delivered editors** — browser canvases, lighter toolsets, closer to marketing/design-team usage; some products run a beginner web tier beside a professional desktop tier.
- **AI-augmented editors** — current-generation products embed tracing, background removal, subject isolation, and sometimes generative imagery; the drawing-first workflow remains the center.
- **Technical-leaning configurations** — isometric/axonometric grids, drawing scale, dimensioning for diagram-adjacent artwork.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Vector Graphics Editor | sibling under the same family; **joint review recommended** | the market sells one vector product family under both labels; this leaf carries the illustration-artwork center of gravity (expressive drawing craft for artwork deliverables); the sibling leaf is expected to carry general-purpose precision vector tooling for any vector work (icons, diagrams, technical, UI). The keep-both-with-center-of-gravity-split vs merge decision is deferred to joint review |
| Digital Painting Application | closest raster neighbor | artwork made of brush-applied raster pigment vs artwork made of geometry-defined objects; machinery overlaps (brushes, layers, pressure) but the primary medium decides the Type |
| Raster Image Editor | adjacent | center is modifying existing pixel images; here the artwork is authored from scratch as objects |
| Graphic Design Application | adjacent | center is composing design deliverables (typography + layout + output for mixed-element compositions); here the center is the artwork itself; the market straddles the seam at product level |
| AI Image Generator | adjacent | generation-first (system composes the first pass) vs authoring-first (user draws it); generative helpers inside these products do not flip the center |
| Template-based Design Platform | adjacent | composition starts from browsed pre-made templates for non-designers vs freeform object drawing from a blank canvas |
| Pixel Art Editor | adjacent | creation constrained to a pixel grid/palette — the opposite of resolution-independent geometry |
| 2D Animation Application | adjacent | timeline/scene center for moving work; some illustration tools add frame animation or export animation-ready assets as optional capability |
| Diagramming Application | adjacent | objects carry semantic/connector behavior for structured diagrams; here objects are freeform artwork |
| Data Visualization Application | adjacent | marks are computed from user data; here shapes are hand-authored |
| Font Editor | adjacent | draws glyph outlines with similar vector machinery, but the font context (mapping, metrics, font-file generation) carries that Type |

## Representative Products

- **Adobe Illustrator** — the long-standing market standard; the archetype whose very name anchors the illustration reading of the family (official documentation was not reachable during research; no product-specific claims are made)
- **Affinity Designer** — professional single-application hybrid of vector and pixel tooling
- **CorelDRAW** (Graphics Suite) — long-lived professional suite pairing vector illustration with page layout and print production
- **Linearity Curve** (formerly Vectornator) — iPad/Mac-first product explicitly positioned for illustrators
- **Inkscape** — the free open-source editor of the family (official documentation was not reachable during research)

## Sources

Research date: **2026-09-07**

- Affinity Designer 2 Help — "What is Affinity Designer 2?" — https://affinity.help/designer2/en-US.lproj/pages/Introduction/about_designer.html
- Affinity Designer 2 Help — contents index (feature/tool/panel structure) — https://affinity.help/designer2/en-US.lproj/index.html
- Linearity Curve — product page — https://www.linearity.io/curve
- Linearity Curve User Guide (iPad) — Drawing tools / Editing tools / Shaping tools / Start here — https://www.linearity.io/academy/curve/ipad/user-guide/
- CorelDRAW product family and educational pages (fetched in the graphic-design-application research pass, 2026-09-07; URLs in research/graphic-design-application.md)
- Xara Designer Pro+ product and feature pages (fetched in the graphic-design-application research pass, 2026-09-07)

> Sourcing limitation: Adobe (helpx.adobe.com, adobe.com) and Inkscape (inkscape.org, docs.inkscape.org) documentation could not be fetched from the research environment on 2026-09-07 (timeouts / 403). Both products are therefore listed as market anchors without product-specific operational claims; all operational statements in this document rest on the three directly documented products and cross-product reasoning. Precise limits, counts, and version-specific defaults are intentionally not stated.

Detailed evidence, product-by-product observations, the cross-product comparison, and the historical/market-sample check are recorded in the paired Research Notes.
