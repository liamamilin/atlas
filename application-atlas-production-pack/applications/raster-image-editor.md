# Raster Image Editor

## Overview

A **Raster Image Editor** is a general-purpose application for directly editing images made of pixels. Its editable object is a **raster document** — a pixel grid with defined dimensions where each pixel carries a color (and optionally transparency). The user modifies this grid through tools (painting, erasing, filling, transforming) on a visual canvas, and persists the result as standard image files.

The defining structure is small:

```text
Raster Document (pixel grid)
└── Direct pixel manipulation (tools that change pixel values)
    └── Visual canvas (zoomable direct-manipulation surface)
        └── Persist as image (save/export to standard formats)
```

Everything commonly associated with modern editors — layers, masks, blend modes, adjustment stacks, color management, non-destructive workflows — is widespread in current products but is not part of the defining core. Simpler and older raster editors without any of those (the platform-native paint-program lineage) still fit this definition.

When the primary job shifts to creating artwork from scratch with brushes, developing camera RAW files, editing geometry instead of pixels, or generating images from prompts, the product is drifting toward a different Application Type (Digital Painting, RAW Photo Editor, Vector Graphics Editor, AI Image Editing).

## Users & Context

The primary user is anyone who needs to change the pixels of an existing image:

- **retouchers and photographers** — remove objects, fix blemishes, adjust color and tone of prepared images
- **graphic and web designers** — composite elements, cut out subjects, prepare assets in exact dimensions and formats
- **illustrators and concept artists** — refine, recolor, and composite scanned or imported artwork
- **marketing / content operators** — resize, crop, and adapt images for channels and placements
- **casual users** — crop, rotate, annotate, and fix personal images

The work environment is a single user in front of a canvas, typically with a mouse or stylus; tablet and stylus input is common where brushwork matters. Work is session-based and iterative: open an image, change it, inspect the result, change it again, export. There is normally no multi-user concurrency in the core editing act — collaboration, where present, is a variant surface (shared/cloud documents), not the core loop.

## Core Model

### The Defining Core

```text
Raster Document (pixel grid: defined dimensions; per-pixel color, optionally alpha)
└── Direct pixel manipulation (tools/operations that paint, erase, fill, transform pixels)
    └── Visual canvas (zoomable direct-manipulation surface where edits happen)
        └── Persist as image (save/export the result to standard image formats)
```

Four properties. If any one is removed, the product is no longer recognizable as a raster image editor:

- **Raster document** — the editable object is a bitmap: a grid of pixels, each holding color values (and optionally an alpha/transparency value). Without this, the product is a vector editor or a 3D tool.
- **Direct pixel manipulation** — the user changes pixel values through operations: paint, erase, fill, clone, transform. Without this, the product is a viewer.
- **Visual canvas** — the raster is displayed at zoom/pan and edited in place through direct manipulation. Without this, the product is a batch processor or conversion utility.
- **Persist as image** — the edited result can be saved or exported into standard image formats. Without this, it is not an editor.

### Capabilities Shared by Mature Products

A typical modern raster editor carries most of these capabilities. They are not what makes the product a raster editor, but they make it practical. All of the following are documented across the researched sample (three products with directly accessible official documentation); the simpler historical editors lack most of them and remain raster editors.

- **Layers** — the document is composed as a vertical stack of pixel planes rendered one on top of another. Each layer holds part of the image (an area of opaque, partially transparent, or transparent pixels) and can be edited without affecting the others. Layer order determines what appears in front; opacity and blend modes determine how a layer combines with what is beneath it. Layers can be grouped, reordered, duplicated, merged, and toggled visible/hidden.
- **Selections** — a region of the canvas that constrains where edits apply. Made geometrically (rectangle, ellipse), freehand (lasso), or by image content (color similarity, edges). Selections can be added, subtracted, inverted, feathered, grown, shrunk, and saved for reuse.
- **Masks** — a grayscale image attached to a layer that controls its per-pixel visibility without deleting pixel data: black hides, white shows, gray gives partial transparency. Editing the mask is itself pixel editing; disabling the mask restores the unmasked view.
- **Undo / history** — editing actions are recorded and reversible; mature products surface this as a History panel listing each action, allowing return to any earlier state. Undo coverage has limits in every product (some operations cannot be undone).
- **Color adjustments & filters** — operations that transform pixel values mathematically: brightness/contrast, curves and levels, hue/saturation, white balance, blur, sharpen, noise, distortion, stylized effects. Applied to a selection, a layer, or the whole image.
- **Transform operations** — crop, resize/scale, rotate, flip, skew, perspective, free transform of layers or selections.
- **Retouching tools** — pixel-level repair tools: clone (copy pixels from elsewhere), heal (blend repaired pixels with surroundings), smudge, dodge/burn, red-eye and blemish correction.
- **Text layers** — editable text placed as its own layer, re-editable after placement rather than burned into pixels immediately.
- **Color management** — the document carries a color space/profile (commonly ICC-based); products support several standard profiles and bit depths so colors survive movement between devices and output targets.
- **Native project format vs export formats** — the working document (with layers, masks, text) is saved in a product-native format that preserves editability; finished images are exported to interchange formats (e.g. JPEG, PNG, TIFF, GIF, WebP) where layer structure may be flattened or lost.
- **Navigation & aids** — zoom/pan, rulers, guides, grids, and snapping that make pixel-accurate work possible.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. Implementations vary:

```text
Concept:          Raster Document
Implementations:  fixed-canvas bitmap; layered document; layer sizes independent of canvas

Concept:          Selection
Implementations:  geometric marquees, freehand lasso, color-similarity wand, edge-based,
                  painted masks (quick-mask mode), saved channels

Concept:          Non-destructive hiding
Implementations:  layer masks (raster), vector masks (Bézier-derived), quick masks

Concept:          Native project format
Implementations:  product-specific formats that preserve layers (each product has its own),
                  vs export to interchange formats
```

A reader who has only seen one product should still be able to recognize any other raster editor from the Core Model.

## How It Works

### Acquire or create the document

```text
Open an existing image file
  or create a new document (choose dimensions, background, color model)
→ the raster document loads onto the canvas
```

### The core editing loop

```text
Select a tool (paint / erase / fill / retouch / transform)
→ set tool options (size, opacity, hardness, color)
→ optionally restrict scope (selection, mask, target layer)
→ apply strokes or operations on the canvas
→ inspect the result (zoom, toggle layers, compare with history)
→ undo or continue
```

This loop is the heart of the application. Everything else — layers, masks, adjustments — exists to give the loop better scope control and reversibility.

### Compose with layers

```text
Add/import a layer (new, duplicate, open file as layer)
→ reorder it in the stack (front/back)
→ set opacity and blend mode
→ edit its pixels (tools act on the active layer)
→ optionally attach a mask to hide parts non-destructively
→ merge or flatten when the structure is final
```

Only one layer is active at a time; edits land on it. The visible result is the stack rendered top to bottom.

### Isolate with selections and masks

```text
Make a selection (geometric / freehand / by color / by edge)
→ refine it (feather, grow/shrink, add/subtract)
→ edits now apply only inside the selection
→ optionally save the selection, or convert it to a mask for permanent non-destructive control
```

### Adjust and transform

```text
Apply color adjustments (curves, levels, hue/saturation, white balance)
  or filters (blur, sharpen, stylize) to a scope
→ transform (crop, scale, rotate, flip, perspective)
→ inspect via before/after or history
```

### Finish: save and export

```text
Save the working document in the native format (layers preserved, editability retained)
→ export the finished image to a standard format
   (flattening or format constraints may apply — e.g. formats without transparency)
→ optionally export multiple variants (sizes, formats)
```

### Core vs Common vs Optional

**Defining core** — without these, not a raster image editor:

- raster document (pixel grid)
- direct pixel manipulation via tools
- visual canvas
- persist as image

**Common mature structure** — present in most modern products:

- layers, selections, masks
- undo/history
- adjustments & filters, transforms, retouching tools
- text layers, color management
- native project format vs export formats
- navigation & aids

**Variant / optional** — depends on segment, philosophy, surface:

- non-destructive models (adjustment layers, smart objects, live filters)
- embedded vector tools, animation, artboards
- automation (actions, scripts, plugins)
- precision/color posture (16/32-bit, CMYK, HDR)
- surface (desktop / web / tablet), cloud collaboration, RAW modules, AI features

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Canvas (document window)

The primary surface.

- the raster at zoom/pan, composited result of the layer stack
- in-canvas handles for selections and transforms
- primary actions: apply the active tool, move/transform, pick colors

### Toolbox

The tool switcher.

- grouped tools: selection, paint, erase, fill, retouch, transform, text, color picker, zoom
- foreground/background color swatches
- primary actions: choose the active tool

### Tool options

Options for the active tool.

- size, opacity/hardness, mode, dynamics — varies per tool
- primary actions: tune how the tool behaves before applying it

### Layers panel

The document's structure map.

- ordered list of layers with thumbnails; top = front
- per-layer visibility, opacity, blend mode, lock state
- primary actions: select active layer, add/delete/duplicate, reorder, group, merge, add mask

### History panel

The session's action log.

- chronological list of editing actions
- primary actions: undo/redo, jump to an earlier state

### Adjustments / filters

Dialogs or panels for pixel-value transformations.

- parameter controls with live preview on the scoped region
- primary actions: apply, reset, preview toggle

### Color & swatches

Color selection surface.

- color picker, palettes/swatches, recent colors
- primary actions: set foreground/background colors

### Menus / command surface

File (open/save/export), Edit (undo, fill, stroke), Image (size, crop, mode), Layer, Select, Filter menus — or the equivalent ribbon/command palette. Automation entries (actions, scripts, plugins) live here where present.

## Important Rules / Behaviors

### Edits land on the active layer

With a layer stack, tools act on the currently selected layer. Editing one layer does not change the pixels of other layers; the visible image is the composite. Forgetting which layer is active is a common source of "nothing happens" or "edited the wrong thing" — at least one major product devotes a troubleshooting section to exactly this class of confusion.

### Selections constrain edits

When a selection exists, painting, filling, filtering, and transforming apply only inside it; operations outside it do nothing. A selection can persist invisibly and silently constrain later edits — products provide "select none" and visibility toggles for this reason.

### Layer order and blend modes change the result

The same pixels produce different visible outcomes depending on stack order, opacity, and blend mode. Reordering is itself an edit.

### Masks hide without destroying

Mask edits change visibility, not pixel data; disabling or deleting the mask restores the layer. This is the primary non-destructive mechanism common across mature products.

### Undo has limits

The researched products all document limits: some operations cannot be undone, and history depth is bounded by available resources. Saving, flattening, and mode conversions are typical hard boundaries; the History panel mitigates but does not remove them.

### Native format preserves editability; export may not

Layer structure, masks, and text survive in the native project format. Exporting to interchange formats may flatten layers or drop features (e.g. transparency in formats without alpha). The save/export distinction is a structural rule of the Type, not a product quirk.

### Destructive vs non-destructive is a spectrum

Direct pixel edits are destructive by default. Masks, and (where offered) adjustment layers/smart objects, defer or avoid pixel destruction. Products differ in how far they push non-destructive editing; the raster editor as a Type does not require it.

## Variants

The Type is implemented in many forms. Common variants:

- **professional desktop editor** — the full set of standard capabilities plus non-destructive models, deep color management, automation; subscription or one-time licensing; the reference segment for print/photo/retouching work
- **free open-source editor** — comparable structural core (layers, selections, masks, filters), extensible via scripting/plugins; community-documented
- **lightweight consumer editor** — simplified layer model, essential adjustments, approachable UI; often platform-native or low-cost
- **web-based editor** — the same core model delivered in the browser, frequently with local processing; freemium business models are common
- **painting-first hybrid** — brush-centric products that still carry the full raster editing core; the primary job (create from scratch vs edit existing) decides the adjacent Type
- **photo-workflow-embedded editor** — pixel editing offered inside a photo catalog/RAW pipeline; the editing core is the same, the surrounding workflow differs
- **AI-augmented editor** — generative fill/expansion and automated selection added to the manual toolset; the manual core remains the document's structure

A variant should remain a **Variant**, not become a separate Type, unless it changes users, core objects, workflow or rules so much that the Core Model no longer applies (e.g. pure prompt-based generation → AI Image Editing Application).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Digital Painting Application | adjacent (same directory section) | primary job is creating artwork from scratch with brushes; raster editing centers on modifying existing pixel data |
| Photo Editor | adjacent | assumes camera-origin single images; centers on photographic adjustments rather than general pixel editing |
| RAW Photo Editor | adjacent | centers on developing sensor data (demosaic, exposure); raster editing operates on already-rendered pixels |
| Pixel Art Editor | variant-adjacent | constrains resolution and palette for pixel-accurate sprite work; raster editor treats both as free parameters |
| Vector Graphics Editor | different object model | editable object is geometry (Bézier/shapes), not a pixel grid; raster editors may embed vector tools as a variant |
| Graphic Design Application | broader | centers on layout, templates, and design assets; raster editing is one capability inside it |
| AI Image Editing Application | adjacent | primary edit surface is prompt/generative; manual pixel tools are secondary |
| Image Viewer | weaker | renders images without pixel manipulation |
| Image Batch Processor / Image Conversion Application | weaker | automated multi-file operations without an interactive canvas |

The most important boundary is with **Digital Painting Application**: the structural machinery (layers, brushes, filters) overlaps almost completely, and at least one major painting product explicitly documents the distinction as one of purpose — image manipulation versus creating artwork from scratch. The primary job, not the feature list, decides the Type.

## Representative Products

- Adobe Photoshop — professional desktop raster editor; category reference (official documentation not reachable on the research date; included as a widely-attested market anchor)
- GIMP — free open-source desktop raster editor
- Affinity Photo — professional one-time-purchase raster editor (official documentation not reachable on the research date; included as a widely-attested market anchor)
- Photopea — web-based raster editor with local in-browser processing
- Paint.NET — free Windows raster editor

The Core Model was checked against simpler/historical samples (the platform-native paint-program lineage, e.g. single-layer editors without layers or masks) to avoid over-fitting the definition to the modern professional feature set.

## Sources

Research date: **2026-09-06**

Official documentation directly consulted:

- GIMP 2.10 User Manual — https://docs.gimp.org/2.10/en/ (incl. Combining Images: https://docs.gimp.org/2.10/en/gimp-image-combining.html)
- Photopea Learn — https://www.photopea.com/learn/ (Layers: /learn/layers; Masks: /learn/masks)
- Paint.NET Documentation — https://www.getpaint.net/doc/latest/index.html
- Krita 5.3 Manual (boundary evidence) — https://docs.krita.org/en/

> Sourcing limitation: official documentation for Adobe Photoshop (helpx.adobe.com, adobe.com) and Affinity Photo (affinity.help, serif.com) could not be fetched from the research environment on 2026-09-06 (timeouts / HTTP 403 / domain redirect). These products are retained as representative market anchors only; no product-specific operational claims about them appear in this document.

Detailed evidence, product-by-product observations, cross-product comparison matrix, rejected findings, and the historical / market-sample breadth check are recorded in the paired Research Notes.
