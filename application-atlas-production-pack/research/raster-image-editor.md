# Research Notes — Raster Image Editor

## Research Goal

Identify the smallest stable invariant that defines the **Raster Image Editor** Application Type, and place every other observed capability at the correct abstraction level.

Following `WORKFLOW_v1.1.md §22` and `WRITING_GUIDE_v1.1.md §28`, this document separates:

```text
L0 Defining Invariant
L1 Common Mature Structure
L2 Variant / Optional
L3 Vendor-specific
```

Evidence layers per `WORKFLOW_v1.1.md §23`:

```text
A Direct Product Observation (official source for a specific product)
B Cross-product Commonality
C Canonical Inference
```

## Initial Boundary

Target:

> Raster Image Editor (DIRECTORY 04.02 Raster & Painting)

Nearest confusing Types:

- Digital Painting Application (same section 04.02)
- Pixel Art Editor (same section 04.02)
- Photo Editor / RAW Photo Editor (04.04)
- Vector Graphics Editor (04.03)
- Graphic Design Application (04.01)
- AI Image Editing Application (04.20)
- Image Viewer / Image Batch Processor / Image Conversion Application (04.05)

Working hypothesis:

> A raster image editor is a general-purpose application whose editable object is a pixel grid (bitmap), manipulated directly through tools on a visual canvas, with the result persisted as standard image files.

Key uncertainty at start: are **layers** part of the defining invariant? Historical check (§24) says probably not — platform-native raster editors without layers exist (MS Paint lineage).

## Research Questions

1. What is the smallest object model without which a product is no longer recognizable as a raster image editor?
2. Where do Document / Canvas / Layer / Selection / Mask / Tool / Adjustment / History / Export sit in the L0–L3 hierarchy?
3. How is destructive vs non-destructive editing distributed across the levels?
4. Are color model, bit depth, and color management definitional or variant?
5. What is the structural boundary with Digital Painting Application, Photo Editor, Pixel Art Editor, and Vector Graphics Editor?
6. Do older / platform-native / simpler products (no layers, no masks) still fit the definition?

## Representative Products

| Product | Why selected | Docs accessed |
|---|---|---|
| GIMP | free open-source desktop raster editor; different philosophy (FOSS, extensible); full official manual | yes (docs.gimp.org 2.10 manual) |
| Photopea | web-based freemium editor; browser surface; PSD-compatible philosophy; official Learn site | yes (photopea.com/learn) |
| Paint.NET | free Windows editor; simpler consumer/prosumer tier; official documentation | yes (getpaint.net docs) |
| Adobe Photoshop | category-defining professional product; subscription tier | **no** (see Sources limitation) |
| Affinity Photo | professional one-time-purchase alternative; non-destructive philosophy | **no** (see Sources limitation) |

Historical / market-sample breadth check (per `WORKFLOW_v1.1.md §24`), used for boundary reasoning, not primary structural evidence:

- MS Paint lineage (platform-native, single-layer, no masks) — proves layers/masks are not definitional
- Krita (docs.krita.org) — self-declared painting program; used as boundary evidence for Digital Painting Application

## Sources

Research date: **2026-09-06**

Directly fetched official sources (Layer A evidence):

- GIMP 2.10 User Manual (full TOC + Combining Images chapter): https://docs.gimp.org/2.10/en/ , https://docs.gimp.org/2.10/en/gimp-image-combining.html
- Photopea Learn — Introduction, Layers, Masks: https://www.photopea.com/learn/ , https://www.photopea.com/learn/layers , https://www.photopea.com/learn/masks
- Paint.NET Documentation — Overview/Features: https://www.getpaint.net/doc/latest/index.html
- Krita 5.3 Manual (welcome/positioning page): https://docs.krita.org/en/

Source-access Limitation (per `WORKFLOW_v1.1.md §23`):

- `helpx.adobe.com` (Photoshop User Guide / Get Started) timed out twice → abandoned.
- `adobe.com/products/photoshop.html` timed out → abandoned.
- `affinity.help` returned HTTP 403; `serif.com` now redirects to Canva (post-acquisition) → abandoned.
- Consequence: Photoshop and Affinity Photo are retained as market anchors with **widely-attested structural facts only**; no precise operational claims about them are made in this research or the final document. No detail was filled from model memory.

## Product Observations

### GIMP (Layer A — official manual)

- Core concepts documented: Image, Layers, Layer Modes, Selections, QuickMask, Paths, Brushes/Gradients/Patterns/Palettes, Undo, Save vs Export, Color modes (RGB / Grayscale / Indexed), Precision, ICC color management, Transform tools, Filters, Text layers, Scripting/plugins.
- Layers chapter: "You can think of layers as a stack of slides… construct an image of several conceptual parts, each of which can be manipulated without affecting any other part." Bottom layer = background; foreground above. Layer count limited only by memory.
- Layer properties: name; presence/absence of alpha channel (background layer special case); layer type (RGB / RGBA / Gray / GrayA / Indexed / IndexedA); visibility toggle; active layer ("active drawable" — layers, channels, layer masks, selection mask are all paintable); linkage (chain icon for grouped transforms); size/boundaries (layer boundaries may differ from canvas; "you can't act on what doesn't exist" outside layer boundaries); opacity (0–100); blend mode; layer mask (extra grayscale drawable, must be added explicitly).
- Layer modes organized in families: Normal, Lighten, Darken, Contrast, Inversion, HSV components, LCh components (+ legacy modes).
- Selection tools: rectangle, ellipse, free (lasso), fuzzy (magic wand), by color, intelligent scissors, foreground select. Selection operations: add/subtract, feather, shrink/grow, border, invert, save to channel, to path. QuickMask converts selection to a paintable temporary mask.
- Paint tools: pencil, paintbrush, airbrush, ink, MyPaint brush, eraser, bucket fill, gradient, clone, heal, perspective clone, blur/sharpen, smudge, dodge/burn.
- Transform tools: move, crop, rotate, scale, shear, perspective, flip, unified/handle transform, warp, cage, 3D transform, align.
- Undo: dedicated concept page incl. "Things That Cannot be Undone" (undo has limits); Undo History dialog.
- Save vs Export: Save writes the native format (XCF); Export produces standard formats (JPEG/PNG/etc.). Documented as distinct operations with distinct dialogs.
- Color: image mode conversion (RGB / grayscale / indexed), precision settings, assign/convert ICC color profiles.
- Text: text tool creates text layers; text commands in Layer menu.
- Filters: large categorized menu (blur, enhance, distort, light & shadow, noise, edge-detect, artistic, decor, map, render, web, animation).
- Extensibility: plugins, Script-Fu (Scheme), Python-Fu.
- "Getting unstuck" section documents real operational constraints: floating selection blocks other actions; acting outside the selection does nothing; acting outside the layer boundary does nothing; indexed mode restricts tools; eraser needs an alpha channel to produce transparency.

### Photopea (Layer A — official Learn site)

- Self-description: "an advanced image editor, which can work with both raster and vector graphics"; runs entirely in the browser, files stay on the device.
- Color: works with many color spaces (ICC profile in file), 8/16/32-bit depth.
- Layers: "Each PSD document consists of layers. The layer represents some part of the image… an area filled with transparent, partially transparent or opaque pixels." "Layers are rendered one on top of another, to create the final image. You usually edit just one layer at a time. Changing (moving, rotating, drawing into) one layer has no effect on other layers."
- Layers panel: list with thumbnails; top of list = front, bottom = back; single and multi-select; nested folders of layers; drag-and-drop reordering.
- Layer properties: visibility (eye), blend mode, opacity, locks (transparency / pixels / position / all), name.
- Layer operations: new layer, new folder, duplicate (incl. across documents), merge down / merge selected, delete, raster mask creation.
- Masks: "an extra image, attached to the layer… same size… black and white only… black hides, white shows; grays give partial transparency." Raster mask (any layer tool works on it, colors become grays) vs vector mask (Bézier shapes, auto-converted to grayscale). At most one raster + one vector mask per layer; folders can carry masks. Enable/disable, link to layer content, Density and Feather properties.
- Other documented surfaces: Smart Objects, Layer Styles, Adjustments & Filters, Selections (make / advanced / refine edge / move selected data), Channels, Brush tools (basic / advanced / smart), Text, Vector graphics (structure / shapes / vectorize bitmap), Video editing, Automate (Actions / Scripts / Variables), Storages, Artboards, Color Spaces, Guides & Snapping, Animations, Slices, Layer Comps, Free Transform.

### Paint.NET (Layer A — official documentation)

- Self-description: "the best free image and photo editing application for Windows"; UI familiar to users of MS Paint and Photoshop.
- Documents: tabbed interface, multiple images open simultaneously, live thumbnails.
- Layers: "Layers allow an image to be composed from a stack of images that are blended together." Supports many blend modes, layer transparency, drag-and-drop reordering.
- History: "Every editing action performed on an image is recorded in the History window… undoing actions as simple as clicking on a previous entry"; bounded only by disk/memory ("Unlimited History").
- Files: native `.pdn` "preserves the layer structure… lossless… default format for saving multi-layered images. If the image is a single layer, the format for saving defaults to *.PNG." Export formats: PNG, JPEG, JPEG XL/XR, BMP, GIF, TGA, DDS, TIFF, HEIC, WebP, AVIF (some via plugins).
- Color management: "full color management support"; built-in profiles sRGB, Adobe RGB, Display P3, Pro Photo RGB; arbitrary .icc/.icm import.
- Extensibility: third-party plugins add effects, adjustments, and file formats.

### Krita (Layer A — boundary evidence only)

- Official positioning: "a sketching and painting program designed for digital artists… end-to-end solution for creating digital art files from scratch… Although it has features that overlap with other raster editors its intended purpose is to provide robust tool for digital painting and creating artworks from scratch… it is not intended as a replacement for Photoshop… other programs may have more features than Krita for image manipulation tasks, such as stitching together photos."
- This is direct vendor evidence for the Raster Image Editor ↔ Digital Painting Application boundary: the same structural machinery (layers, brushes, filters) serves two different primary jobs — creating artwork from scratch vs manipulating existing images.

### Historical / market-sample breadth (Layer B / widely-attested)

- MS Paint lineage (platform-native since the 1980s): single-layer pixel editing with pencil/brush/fill/eraser/selection tools, undo, save to standard formats — **no layers, no masks, no blend modes**. It is still recognizably a raster image editor. This is the decisive §24 check: layers, masks, blend modes, and adjustment stacks cannot be L0.
- Adobe Photoshop and Affinity Photo: universally positioned as professional raster image editors (market position widely attested); official documentation not reachable on the research date, so no product-specific structural claims are made here.

## Cross-product Comparison

| Finding | GIMP | Photopea | Paint.NET | MS Paint (historical) | Abstraction level |
|---|---|---|---|---|---|
| editable object is a pixel grid (raster document) | yes | yes | yes | yes | **L0** |
| direct pixel manipulation via tools (paint/erase/fill/transform) | yes | yes | yes | yes | **L0** |
| visual canvas with zoom/pan as the edit surface | yes | yes | yes | yes | **L0** |
| save/export to standard image formats | yes (Export) | yes | yes | yes | **L0** |
| layers (stack, order, opacity, blend modes) | yes | yes | yes | **no** | L1 |
| layer masks (grayscale per-layer transparency) | yes | yes (raster + vector) | limited | no | L1 |
| selections constrain where edits apply | yes (7+ tools) | yes (basic/advanced/refine) | yes | basic rectangular only | L1 |
| undo / history (often a visible panel) | yes (with documented limits) | yes | yes ("Unlimited History") | simple undo | L1 |
| color adjustments & filters | yes (Colors menu + Filters) | yes (Adjust. & Filters) | yes (Adjustments + plugin effects) | minimal | L1 |
| transform ops (crop/resize/rotate/flip) | yes | yes (Free Transform) | yes | basic | L1 |
| retouching tools (clone/heal/smudge/dodge-burn) | yes | yes (advanced/smart tools) | via plugins | no | L1 |
| text layers | yes | yes | yes | no | L1 |
| color management (ICC) | yes | yes | yes | no | L1 |
| native project format preserving layers vs export formats | yes (XCF vs Export) | yes (PSD-compatible) | yes (.pdn vs PNG default) | n/a (single layer) | L1 |
| non-destructive adjustment/smart layers | partial | yes (Smart Objects) | no | no | L2 |
| layer styles / effects | partial | yes | no | no | L2 |
| vector tools inside the raster editor | yes (paths) | yes (shapes, vector masks) | limited | no | L2 |
| automation (actions/scripts/plugins) | yes (Script-Fu/Python-Fu) | yes (Actions/Scripts) | yes (plugins) | no | L2 |
| animation support | yes (filters/playback) | yes | no | no | L2 |
| artboards / multiple canvases | no | yes | tabs (documents) | no | L2 |
| web / local-browser surface | desktop | web (local processing) | desktop (Windows only) | platform-native | L2 (surface) |
| RAW photo development | no | no | no | no | adjacent Type (04.04) |

## L0 — Defining Invariant

The smallest structure without which the product would no longer be recognizable as a raster image editor:

```text
Raster Document (pixel grid: defined dimensions; per-pixel color, optionally alpha)
└── Direct pixel manipulation (tools/operations that paint, erase, fill, transform pixels)
    └── Visual canvas (zoomable direct-manipulation surface where edits happen)
        └── Persist as image (save/export the result to standard image formats)
```

Removal tests:

- remove *raster document* (editable object becomes geometry) → Vector Graphics Editor
- remove *direct pixel manipulation* (view only) → Image Viewer
- remove *visual canvas* (no direct manipulation surface) → batch processor / conversion tool
- remove *persist as image* → not an editor at all

§24 historical check: MS Paint lineage satisfies all four properties with no layers, no masks, no blend modes, no adjustments. Therefore layers/masks/adjustments are **L1**, not L0. The definition does not depend on any era, platform, or vendor pattern.

## L1 — Common Mature Structure

Common across the researched sample (GIMP + Photopea + Paint.NET all document them); they make the editor practical but do not define the Type:

```text
Layers (compositing stack: order, opacity, blend modes, visibility, grouping)
Selections (constrain where edits apply: geometric, freehand, color-based)
Masks (per-layer grayscale transparency control, non-destructive hiding)
Undo / history (frequently surfaced as a History panel)
Color adjustments & filters (brightness/contrast, curves/levels, blur/sharpen, …)
Transform operations (crop, resize, rotate, flip, perspective)
Retouching tools (clone, heal, smudge, dodge/burn)
Text layers (editable text as a layer kind)
Color management (ICC profiles, color spaces, bit depth)
Native project format (preserves layers) distinct from export formats
Navigation & aids (zoom/pan, guides, grids, rulers)
```

## L2 — Variant / Optional Structure

Presence or absence does not change the Type:

```text
Non-destructive editing models
- adjustment layers / live filter layers
- smart objects / linked embedded documents
- layer styles (drop shadow, stroke, …)

Embedded secondary paradigms
- vector tools inside the raster editor (shape layers, pen tool, vector masks)
- animation / timeline support
- video layers
- artboards / multiple canvases per document

Automation & extensibility
- macro/action recording
- scripting (Scheme/Python/JS)
- plugin ecosystems (effects, adjustments, file formats)

Color & depth posture
- 8/16/32-bit precision
- CMYK / print-oriented workflows
- HDR / scene-referred editing

Surface & delivery
- desktop / web / tablet+stylus / mobile
- cloud documents & collaboration (drifts toward Collaborative Design Platform)
- RAW development modules (drifts toward RAW Photo Editor)
- AI generative editing (drifts toward AI Image Editing Application)
```

## L3 — Vendor-specific Structure

Remains in Research Notes only:

- GIMP: XCF native format; explicit Save-vs-Export separation; Script-Fu/Python-Fu; GEGL operations; MyPaint brush engine; QuickMask; "active drawable" concept; documented "getting unstuck" constraints (floating selection, acting outside selection/layer, indexed-mode restrictions).
- Photopea: PSD-format compatibility focus; fully local in-browser processing; Storages; Layer Comps; Slices.
- Paint.NET: `.pdn` format; single-layer save defaults to PNG; tabbed document interface; plugin taxonomy (effects / adjustments / file types).
- Adobe Photoshop (not verified on research date; widely-attested only): Smart Objects, adjustment layers, generative AI features, Camera Raw, PSD/PSB.
- Affinity Photo (not verified on research date): live filters, personas, one-time-purchase licensing.

## Rejected Findings

- **"Layers are definitional"** — rejected by the §24 historical check (MS Paint lineage is a raster image editor without layers). Layers are L1.
- **"Masks are definitional"** — same reasoning; masks presuppose layers. L1.
- **"Blend modes are definitional"** — only meaningful with a layer stack. L1.
- **"Non-destructive editing is definitional"** — only some products implement it (Paint.NET does not document it); it is a philosophy variant. L2.
- **"Color management / ICC is definitional"** — present in all three sampled modern products but absent in simpler/historical editors; a quality attribute. L1 (common) with L2 depth variants.
- **"A raster image editor must support photos"** — rejected: the Type is defined by the editable object (pixel grid), not by input source. Photo-centric products are the adjacent Photo Editor Type.
- **"Web-based = different Type"** — rejected: surface is L2; Photopea's local-processing web delivery does not change the object model.

## Boundary Findings

### vs Digital Painting Application

Krita's own documentation states the distinction: it "has features that overlap with other raster editors" but its purpose is "digital painting and creating artworks from scratch," explicitly "not intended as a replacement for Photoshop" for "image manipulation tasks."

- Raster Image Editor: primary job is **modifying existing pixel data** (retouch, composite, adjust, prepare for output).
- Digital Painting Application: primary job is **creating artwork from scratch** with brush-centric workflows.
- Boundary test: 去掉"以编辑已有图像为中心"并把笔刷创作放到中心 → Digital Painting Application. The machinery overlaps; the primary job decides the Type.

### vs Photo Editor / RAW Photo Editor

- Photo Editor assumes camera-origin single images and centers on photographic adjustments; RAW Photo Editor centers on demosaicing/developing sensor data.
- Raster Image Editor is source-agnostic: screenshots, scans, composited graphics, web assets, artwork.
- Boundary test: 去掉"照片中心假设"（相机来源、镜头/传感器语义）→ generic raster editor; 去掉通用像素编辑、只留照片调整 → Photo Editor.

### vs Pixel Art Editor

- Pixel Art Editor constrains the canvas (low resolution, indexed palettes, pixel-accurate placement tools).
- Raster Image Editor treats resolution and palette as free parameters.
- Boundary test: 去掉分辨率/调色板约束 → raster editor.

### vs Vector Graphics Editor

- Editable object: pixel grid vs geometric primitives (Bézier, shapes).
- Boundary test: 把像素网格换成几何对象 → vector editor. (Raster editors may embed vector tools — L2 — but the document remains raster.)

### vs Graphic Design Application / Template-based Design Platform

- Design applications center on layout, templates, brand assets, multi-element compositions; raster editing is one capability among many.
- Boundary test: 去掉版式/模板/设计资产语义、只留像素编辑 → raster editor.

### vs AI Image Editing Application

- AI editing centers the primary edit surface on prompts/generative output; manual pixel tools are secondary.
- Boundary test: 去掉生成式主表面 → raster editor. (AI features inside a raster editor are L2.)

### vs Image Viewer / Batch Processor / Conversion Application

- Viewer: read-only rendering, no pixel manipulation.
- Batch processor / converter: automated multi-file operations, no interactive canvas.
- Boundary test: 去掉交互式画布与逐像素编辑 → utility Types.

## Uncertainties

- Photoshop and Affinity Photo official documentation was unreachable on the research date (timeouts / 403 / domain redirect). Their inclusion as representative products rests on widely-attested market position; no product-specific structural claims were made. A later pass with access to their help centers could confirm L1/L2 placement for Smart Objects, adjustment layers, and live filters.
- The exact L0 wording could alternatively fold "visual canvas" into "direct pixel manipulation" (3 items instead of 4). Kept separate because the canvas is the user-visible surface that distinguishes an editor from a batch/conversion utility.
- Selections were placed at L1 despite near-universality, because a minimal editor without selections is still recognizable (MS Paint's selection is rudimentary). If a later pass finds a mature product without any selection concept, L1 placement is confirmed; if not, this could be argued into L0.
- The boundary with Digital Painting Application is a gradient, not a wall; products in 04.02 vs 04.02-adjacent may need a joint review pass (recorded for STATUS.md awareness, not a taxonomy error).

## Final Synthesis

Canonical Raster Image Editor:

```text
L0 (defining invariant)
- Raster document (pixel grid: dimensions + per-pixel color/alpha)
- Direct pixel manipulation via tools
- Visual canvas (zoomable direct-manipulation surface)
- Persist as image (save/export to standard formats)

L1 (common mature structure)
- Layers (stack, order, opacity, blend modes, groups)
- Selections; Masks
- Undo / history
- Adjustments & filters; transforms; retouching tools
- Text layers; color management
- Native project format vs export formats
- Navigation & aids (zoom, guides, grids)

L2 (variant / optional)
- Non-destructive models (adjustment layers, smart objects, live filters)
- Embedded vector tools, animation, artboards
- Automation (actions, scripts, plugins)
- Precision/color posture (16/32-bit, CMYK, HDR)
- Surface (desktop/web/tablet), cloud collaboration, RAW modules, AI features
```

The Application Document will present only L0 and L1, with a Variants section naming L2 options. L3 stays in Research Notes.
