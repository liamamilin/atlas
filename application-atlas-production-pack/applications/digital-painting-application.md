# Digital Painting Application

## Overview

A **Digital Painting Application** is a creation-first art studio for making original artwork on a raster canvas: the user starts from a blank (or near-blank) canvas and produces a painting, illustration, sketch, or comic artwork through brush-driven mark-making, then saves or exports the result as an image.

The defining structure is small:

```text
Artwork-creation orientation (blank canvas is the normal starting point)
└── Brush-driven mark-making (the central instrument —
    one brush system whose modes are paint, blend/smudge, and erase)
    └── Raster canvas (the artwork is a pixel image)
        └── Persist as image (save/export to standard image files)
```

Everything else the market associates with the category — pressure-sensitive stylus input, layers, natural-media simulation, stroke stabilizers, symmetry and perspective aids, color management, animation, comic-page machinery, artwork galleries — is widespread in current products but is not part of the defining core. Mouse-era paint programs, lightweight regional linework applications, and children's painting apps all fit this definition without any of those specifics.

When the primary job shifts to modifying an existing image rather than creating artwork from scratch, the product is drifting toward a different Application Type (Raster Image Editor). The two Types share almost all of their machinery; the starting point — blank canvas versus existing image — is what separates them.

## Users & Context

The primary user is someone making original artwork:

- **illustrators and character artists** — finished illustrations for publishing, games, and personal work
- **concept artists and matte painters** — environments, creatures, and key art for films and games
- **comic, manga, and webtoon artists** — page-based sequential artwork, from thumbnail to finished tone
- **texture and background artists** — painted surfaces for games and animation
- **students and hobbyists** — learning to draw and paint digitally
- **children and casual users** — at the simplest end of the category, with heavily simplified painting apps

The work environment is a single artist in front of a canvas. Input is dominated by pressure-sensitive styluses — pen tablets and pen displays on the desktop, stylus-and-touch on tablets — though finger and mouse input remain fully supported entry points. Work is session-based and iterative: sketch, step back, adjust, layer color, blend, refine, and export. The core act of painting is single-user; sharing and cloud features, where present, surround the artwork rather than the stroke.

## Core Model

### The Defining Core

```text
Artwork-creation orientation
└── Brush-driven mark-making
    └── Raster canvas
        └── Persist as image
```

Four properties. If any one is removed, the product is no longer recognizable as a digital painting application:

- **Artwork-creation orientation** — the normal job is producing original artwork from an empty state; the artifact is the user's own drawing or painting. Without this, the product is an image editor (its job would be modifying pictures that already exist).
- **Brush-driven mark-making as the central instrument** — the user's gestures become strokes: a brush engine deposits pigment in a user-chosen color along the path the hand travels. Painting, blending/smudging, and erasing are modes of the same brush system, not separate tool families. Without this, the product is a shape tool, a filter box, or a layout application.
- **Raster canvas** — the artwork lives as a pixel image. Without this, the product is a vector illustration tool with a different object model.
- **Persist as image** — the artwork can be saved in a native working format and exported to standard image files. Without this, it is not a content-creation tool.

### Standard Capabilities

A typical modern painting application carries most of the following. They are not what makes the product a painting app, but they make it practical. All are documented across the researched sample; the simpler historical and entry-level products lack most of them and remain painting applications.

- **Layers** — the artwork is composed as a vertical stack of planes rendered top to bottom. Each layer holds part of the artwork (line art, base color, shading, background) and can be edited without touching the others. Blend modes, opacity, clipping to the layer below, transparency locking, and masks control how layers combine. Layer order is itself an editing decision.
- **Pressure and tilt dynamics** — stylus pressure, tilt, and bearing are mapped to brush behavior (size, opacity, angle, scatter, color variation), so a stroke responds to the hand like a physical tool. The mapping is configurable per brush.
- **Brush libraries and brush editors** — the product ships a library of brushes organized by medium (pencil, ink, watercolor, oil, pastel, airbrush, and so on), and lets the user tune existing brushes or build new ones, save them as presets, and import or share brushes.
- **Color surfaces** — a color wheel or disc, mixers that emulate pigment blending, palettes and swatches, color harmonies, and color history. Some products add gamut-limiting masks or print-oriented color profiles.
- **Stroke stabilization** — smoothing options that steady hand tremor so lines come out clean, especially valued for inking.
- **Drawing aids** — symmetry/mirror painting, perspective guides and rulers, grids, snapping, and quick-shape tools that snap a freehand stroke to a perfect form.
- **Selections, fill, and transform** — regions that constrain where edits apply; fill tools that respect line art (closing small gaps, locking transparency to stay inside lines); and transforms including scale/rotate plus, in several products, warp, liquify, and puppet-style bending of drawn content.
- **Undo / history** — strokes and operations are reversible.
- **Canvas navigation and setup** — zoom, rotate, and mirror the view (mirroring is a standard way artists check a drawing's balance); new-canvas presets with size and print resolution; templates for common artwork formats.
- **Native format and export** — the working document (layers, masks, guides) is saved in a product-native format that preserves editability; finished artwork is exported to standard formats (PNG, JPEG, TIFF; Photoshop-format interchange is common). Several products also record the painting process as a time-lapse video.
- **Text and reference** — editable text for lettering and captions; reference images displayed beside or behind the canvas.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. Implementations vary:

```text
Concept:          Brush system
Implementations:  multiple named brush engines; one engine with many presets;
                  media-category brush catalogs; physics-simulated media

Concept:          Erase / blend
Implementations:  erase as a blend mode of the brush; dedicated eraser and
                  blender tools sharing the brush library

Concept:          Color selection
Implementations:  wheel/disc pickers, pigment mixers, palette sets,
                  harmony tools, gamut masks

Concept:          Drawing aids
Implementations:  symmetry guides, perspective rulers/assistants,
                  grids, snapping, shape-snap strokes

Concept:          Artwork storage
Implementations:  desktop file documents; tablet gallery with artwork
                  thumbnails; cloud-synced works
```

A reader who has only seen one product should still be able to recognize any other painting application from the Core Model.

## How It Works

### Start the artwork

```text
Create a new canvas (choose size, resolution, background)
   or start from a template / open a draft
→ optionally place reference images beside or behind the canvas
```

There is no project hierarchy, no team structure, no upstream data. The canvas and the artist's intent are the starting point.

### Set up the stroke

```text
Pick a brush from the library (pencil / ink / watercolor / oil / …)
→ adjust size and opacity (sliders, per-brush memory)
→ optionally tune the brush's dynamics or pick a saved preset
→ pick a color (wheel, palette, mixer)
```

Brush and color are the two live parameters of every stroke; mature products keep both within one gesture's reach.

### The painting loop

```text
Make strokes (sketch → line art → base color → rendering)
→ blend and smudge where media should mix
→ erase — with a brush, not a separate tool — to carve back
→ step back, zoom, mirror the view to check the work
→ undo or continue
```

This loop is the heart of the application. The same brush system serves all three mark-making modes; switching between painting, blending, and erasing is a mode switch, not a tool change.

### Build the artwork in layers

```text
Separate the work into layers (sketch / line / color / shading / background)
→ reorder, set blend modes and opacity
→ clip shading layers to the line art below
→ lock transparency to stay inside painted shapes
→ group, merge, or flatten when the structure is settled
```

Strokes land on the active layer; the visible artwork is the composite of the stack.

### Use the drawing aids

```text
Enable symmetry or a perspective guide
→ draw freehand; strokes follow or mirror the guide
→ snap a rough stroke to a perfect shape where wanted
→ stabilize shaky lines for clean inking
```

Aids are opt-in per stroke or per layer; the artist turns them on for construction and off for expression.

### Refine and finish

```text
Transform what is drawn (move, scale, rotate; warp or bend in several products)
→ apply adjustments and filters where needed
→ save the working file in the native format (layers and aids preserved)
→ export the finished artwork to standard image formats
   (layer structure may flatten; transparency depends on the format)
→ optionally export a time-lapse video of the process
```

### Core vs Common vs Optional

**Defining core** — without these, not a digital painting application:

- artwork-creation orientation (blank canvas as the normal start)
- brush-driven mark-making as the central instrument (paint / blend / erase as modes of one brush system)
- raster canvas
- persist as image

**Standard capabilities** — present in most modern products:

- layers with blend modes, masks, clipping, transparency locking
- pressure/tilt dynamics and per-brush configuration
- brush libraries, brush editors, brush sharing
- color wheel/palette/mixer surfaces
- stroke stabilization
- symmetry, perspective guides, grids, snapping, quick shapes
- selections, line-art-aware fill, transforms
- undo/history, canvas navigation and setup, templates
- native format + export (PNG/JPEG/TIFF; Photoshop-format interchange common)
- text, reference images, time-lapse recording (several products)

**Variant / optional** — depends on segment, platform, and product philosophy:

- natural-media physics simulation (from "materials feel" to full water/oil behavior with pigment mixing)
- comic/manga/webtoon production machinery (panels, speech balloons, screentones, multi-page projects, print settings)
- frame animation (timeline, onion skinning)
- vector layers for editable, resolution-independent linework
- 3D reference figures, or painting directly on imported 3D models
- photo-art modes (auto-painting and style transfer over imported photos)
- artwork galleries/journals and cloud sync (platform-shaped)
- community brush/material marketplaces
- AI assistance (era-common)

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Canvas

The primary surface.

- the artwork at zoom/rotate/mirror, composited from the layer stack
- in-canvas guides, symmetry lines, and transform handles when active
- primary actions: make strokes with the active brush, move/transform, pick colors from the artwork

### Brush library and brush editor

The instrument cabinet.

- brushes grouped by medium or use, with search, favorites, and tags
- per-brush previews; import/share of brush files
- the editor exposes the brush's behavior (shape, grain, dynamics, pressure mapping) for tuning and preset-saving
- primary actions: choose the active brush, create or modify brushes

### Color surfaces

Where the stroke's pigment is chosen.

- color wheel/disc, sliders, pigment-style mixer, palettes, harmonies, recent colors
- primary actions: set the active color, save palettes

### Layers panel

The artwork's structure map.

- ordered layer list with thumbnails; per-layer visibility, opacity, blend mode, lock
- primary actions: select the active layer, add/delete/duplicate, reorder, group, clip, mask, merge

### Tool options and sliders

The active tool's parameters.

- size and opacity within immediate reach (sidebar sliders on tablet products, option bars on desktop)
- primary actions: tune how the next stroke behaves

### Guides and assistants

Construction aids.

- symmetry axes, perspective vanishing lines, grids, snapping targets
- primary actions: place/edit guides, enable stroke-following

### Artwork browser

Where finished and in-progress artworks live.

- on tablet products, a gallery of artwork thumbnails with folders and previews; on desktop, the file system plus a start/recent surface; some products add cloud-synced works
- primary actions: create, open, duplicate, organize, share/export

### Menus, shortcuts, and gestures

- desktop products expose deep menus and heavy keyboard-shortcut customization; tablet products replace menus with gesture vocabularies (two-finger undo, quick menus)
- primary actions: reach every command without leaving the painting flow

## Important Rules / Behaviors

### Strokes land on the active layer

With a layer stack, the brush paints on the currently selected layer; the visible artwork is the composite. Painting on the wrong layer is the category's classic mistake, and products provide layer selection affordances and transparency locking to manage it.

### The brush is the universal instrument

Painting, blending/smudging, and erasing are modes of the same brush system — one sampled product implements erasing purely as a blend mode of the brush, and others let any brush serve as eraser or blender. Consequence: eraser quality is brush quality, and artists curate brushes rather than "the eraser."

### Input device and pressure mapping are configurable and matter

Stylus pressure, tilt, and bearing drive brush behavior; the mapping is adjustable per brush and per device. Driver and device setup is a real-world failure point — at least one product devotes a dedicated manual chapter to tablet drivers and pressure sensitivity.

### Canvas bounds define what is saved

The canvas is the artwork's frame: what is exported is what lies inside the canvas bounds. Content painted beyond the edge may be stored but is not part of the saved image.

### Native format preserves editability; export may not

Layers, masks, guides, and assistants survive in the native working format. Exporting to interchange formats may flatten layers or drop transparency. The save/export distinction is structural to the Type.

### Aids are opt-in, stroke-scoped

Symmetry, perspective, snapping, and stabilization apply only while enabled. They shape construction strokes; they do not silently alter the artwork when off.

### Performance is engineered, not incidental

Brush engines are compute-intensive; products ship hardware-acceleration tuning and preview optimizations so strokes stay responsive on large, high-resolution canvases. Responsiveness under load is a first-class quality of the Type.

### Color management posture varies

Products range from simple RGB canvases to full color-managed pipelines with print profiles, soft proofing, and gamut warnings. The artwork's color space is a document property; depth of management is a product differentiator, not a requirement of the Type.

## Variants

The Type is implemented in many forms. Common variants:

- **generalist open-source studio** — the full standard capability set, free, community-documented, extensible with brush packs and scripting (e.g. Krita)
- **natural-media simulation specialists** — the brush engine models physical media: water that flows and dries, paint that piles and mixes as pigment, canvas texture and tilt (e.g. Corel Painter, Rebelle)
- **comic/manga/webtoon production tools** — painting core plus page machinery: panel frames, speech balloons, screentones, effect lines, multi-page project management, and print/web export settings (e.g. Clip Studio Paint)
- **tablet-native apps** — gesture-first, stylus-first products built around a device's pencil and touch, with an artwork gallery instead of a file system (e.g. Procreate)
- **beginner editions and simple modes** — the same painting core with reduced depth and guided flows, sometimes as separate editions of a professional product
- **plugin and brush-ecosystem products** — painting engines delivered as plugins into other hosts, and marketplaces where artists trade brushes and materials
- **animation-capable painting apps** — the painting core plus frame timelines and onion skinning; when animation becomes the primary job, the product crosses into the 2D Animation Type
- **photo-art pole** — auto-painting and style-transfer over imported photos alongside the brush loop; the brush remains the product's center

A variant should remain a **Variant**, not become a separate Type, unless it changes users, core objects, workflow, or rules so much that the Core Model no longer applies.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Raster Image Editor | closest sibling (same directory section) | same machinery (layers, brushes, filters), opposite primary job: editing existing pixel images vs creating artwork from a blank canvas; the starting point decides the Type |
| Pixel Art Editor | constrained specialization | fixes low resolution and limited palettes and demands pixel-accurate placement; painting apps treat resolution and color as free parameters |
| Illustration Application | different object model | the editable object is vector geometry (resolution-independent paths), not a pixel canvas; vector layers inside painting apps are a linework convenience, not the document model |
| Graphic Design Application | broader | centers on layout, templates, and design assets; painting is one capability inside it, not its organizing structure |
| Photo Editor / RAW Photo Editor | adjacent | assumes camera-origin images and photographic adjustment pipelines; painting apps start from a blank canvas (imported photos are a secondary use) |
| AI Image Editing / AI Image Generator | adjacent | the primary edit surface is a prompt, not a brush-stroke loop; AI features inside painting apps are variants |
| 2D Animation Application | downstream | when the timeline and frames become the primary object and drawing is frame-filling, the product is an animation tool |
| Digital Whiteboard | weak | free-form ink exists there, but the organizing structure is shared spatial collaboration, not artwork creation and image persistence |

The most important boundary is with the **Raster Image Editor**: the structural machinery overlaps almost completely, and painting products themselves document the distinction as one of purpose — creating artwork from scratch versus manipulating existing images. The primary job, not the feature list, decides the Type.

## Representative Products

- Krita — free open-source painting studio; full official manual available
- Corel Painter — professional natural-media painting heritage product
- Clip Studio Paint — mainstream illustration/comic/animation production tool with a large asset ecosystem
- Procreate — tablet-native painting app built around stylus and touch
- Rebelle — natural-media simulation specialist (watercolor and oil physics)

The Core Model was checked against older and lighter samples (the mouse-era paint-program lineage, lightweight regional linework applications, natural-media hobbyist products, and children's painting apps) to avoid over-fitting the definition to the modern professional feature set.

## Sources

Research date: **2026-09-07**

Official documentation directly consulted:

- Krita 5.3 Manual — https://docs.krita.org/en/ (positioning; User Manual; Basic Concepts; Brush Engines)
- Procreate Handbook — https://help.procreate.com/procreate/handbook (Introduction; Paint, Smudge, and Erase)
- Clip Studio Paint — https://www.clipstudio.net/en/ (product and feature pages, edition comparison, FAQ)
- Corel Painter — https://www.painterartist.com/en/product/painter/ (product and feature pages, version-comparison matrix)
- Rebelle — https://www.escapemotions.com/products/rebelle (product page, key features, edition comparison)

> Sourcing limitation: operational manuals for Clip Studio Paint, Corel Painter, and Rebelle were not reachable as fetchable documentation on the research date (manual URL redirected or not found); evidence for those products comes from official product and feature pages. Krita and Procreate provided manual-grade documentation. Accordingly, this document states no precise numeric limits, defaults, or product-specific workflow details; such details remain in the Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison, and the historical / market-sample breadth check are recorded in the paired Research Notes.
