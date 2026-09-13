# Research Notes — Pixel Art Editor

## Research Goal

Identify the smallest stable invariant that defines the **Pixel Art Editor** Application Type (DIRECTORY 04.02 Raster & Painting), and place every other observed capability at the correct abstraction level.

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

> Pixel Art Editor (DIRECTORY 04.02 Raster & Painting)

Nearest confusing Types:

- Raster Image Editor (same section 04.02, processed 2026-09-06) — sharpest seam: both edit pixel grids
- Digital Painting Application (same section 04.02, processed 2026-09-07) — recorded seam: "Pixel Art Editor (constrained resolution/palette)"
- Illustration Application (04.03, processed 2026-09-07) — recorded seam: resolution-constrained pixels vs resolution-independent geometry
- 2D Animation Application (04.08) — pixel editors commonly do frame animation
- Font Editor (04.18, processed 2026-09-07) — bitmap glyph editing exists inside font editors
- Graphic Design Application (04.01, processed 2026-09-07) — composition vs pixel authoring
- Photo Editor / AI Image Editing (04.04 / 04.20) — photographic vs synthetic pixel authoring
- Game-engine sprite/tile editors — embedded asset tools vs standalone art editors

Working hypothesis:

> A pixel art editor is a specialized raster authoring application in which the pixel is the deliberate unit of composition: canvases are small and resolution-constrained by design, colors are commonly palette-managed, and output is images/sprite animations for games or pixel-art as an art form.

Key uncertainties at start:

1. Is palette/indexed color definitional, or a mode?
2. Is frame animation definitional, or common mature structure?
3. Is the "game asset" purpose definitional, or a dominant-but-variant context?
4. Do older products (Deluxe Paint era, static tile/icon editors) still fit a definition built from modern samples?

## Research Questions

1. What is the smallest object model without which a product is no longer recognizable as a pixel art editor?
2. Where do palette management, indexed color, frame animation, onion skinning, layers, tile modes, sprite-sheet export, pixel-precise tool behavior sit in the L0–L3 hierarchy?
3. What exactly distinguishes this Type from the general Raster Image Editor, given both edit pixels?
4. What is the boundary with 2D Animation Application, given near-universal frame animation in the sample?
5. Do historical products (no layers, no onion skin, no web distribution) still satisfy the definition?

## Representative Products

| Product | Why selected | Docs accessed |
|---|---|---|
| Aseprite | de-facto professional desktop standard; animation-first; paid | yes (aseprite.org/docs — 10 pages, Tier 1) |
| Piskel | free web-based editor; simple, browser-native pole | yes (piskelapp.com home/about, Tier 1) |
| Pro Motion NG | commercial game-industry tool; Deluxe Paint lineage; Windows | yes (cosmigo.com product site, Tier 2) |
| Pixelorama | free open-source multiplatform (Godot); hobbyist/indie pole | yes (official GitHub README, Tier 2) |
| Pixilart | web community/social pole (market anchor) | **no** (403 ×2 — see Sources limitation) |

Historical / market-sample breadth check (per `WORKFLOW_v1.1.md §24`), used for boundary reasoning:

- Deluxe Paint (Amiga, 1980s) — Pro Motion's own site declares lineage ("designed similar to the famous Amiga Deluxe Paint"): palette-driven pixel painting on constrained low-res screens; animation added in later versions. Fits the candidate core.
- Static icon/tile editors of the early console/computer era — pixel editing, tiny palettes, no animation, no layers. Must still fit → animation and layers cannot be L0.
- MS Paint lineage — claimed by the Raster Image Editor pass as *its* historical sample (pixel editing at any resolution without constraint). Supports that the seam is the constraint, not the tools.

## Sources

Research date: **2026-09-08**

Directly fetched official sources (Layer A evidence):

- Aseprite Docs (overview, sprite, color, color-mode, drawing, animation, tiled-mode, zoom, save, exporting): https://www.aseprite.org/docs/ (pages under /docs/)
- Piskel — home/about: https://www.piskelapp.com/about
- Pro Motion NG — product site: https://www.cosmigo.com/ (features overview; online help at cosmigo.com/promotion/docs/onlinehelp/ referenced but not fetched)
- Pixelorama — official GitHub repository README: https://github.com/Orama-Interactive/Pixelorama

Source-access Limitation (per `WORKFLOW_v1.1.md §23`):

- Pixilart (pixilart.com, /draw) returned HTTP 403 twice → abandoned. No product-specific claims are made about Pixilart anywhere in this research or the final document; the community-editor variant is written only as generic market posture.
- Pixelorama's dedicated manual (orama-interactive.github.io/Pixelorama-Manual) returned 404; the README names the current docs location (Pixelorama-Docs, "work in progress"). Product claims for Pixelorama are drawn from the official README feature list only.
- Pro Motion NG's detailed online help (onlinehelp/*.htm pages) was referenced from the fetched page but not fetched; product claims are limited to the fetched feature overview.
- Consequence: no numeric limits or defaults are asserted in the final document beyond what fetched pages directly state; those stay in these notes.

## Product Observations

### Aseprite (Layer A — official docs, 10 pages)

- Positioning: "Aseprite lets you create 2D animations for videogames. From sprites, to pixel-art, retro style graphics, and whatever you like about the 8-bit and 16-bit era."
- Document model ("Sprite structure"): a sprite has (1) a size in pixels (width/height), (2) a color mode telling how many colors the image can handle (one mode per sprite; cannot mix RGB and Indexed images in the same sprite), (3) a color profile, (4) a set of layers (one opaque background layer + several transparent layers), (5) animation frames, each with a duration in milliseconds, (6) the layer×frame intersection is a **cel** which "contains the image where you finally can paint". The Timeline shows the whole structure as a grid — rows are layers, columns are frames; tags organize several animations of the same sprite; linked cels reuse frames across animations.
- Color modes: **RGB/RGBA** (each pixel independent, alpha 0–255), **Indexed** (each pixel stores a number referencing a palette color; "your palette can contain up to 256 colors"; modifying a palette color changes all pixels referencing it; indexed images have a designated transparent index, generally 0, changeable via Sprite > Properties), **Grayscale** (value+alpha).
- Drawing: pencil-first toolset — Pencil (B), Line (L), Curve (Shift+L), Rectangle (U), Ellipse (Shift+U), Contour (D), Polygon (Shift+D); Eraser (E), Eyedropper (Alt/I), Rectangular Marquee (M), Move Cel, Slice, Zoom (Z). "Left click to paint with the Foreground color and the active brush, or Right click to paint with the Background color… true for almost all painting tools." Tool behavior modified by the active **ink** and **dynamics** options. Helpers: Preview Window, Tiled Mode, Symmetry.
- Animation: "Aseprite's main goal is to be a tool to create animations." Workflow: draw first frame → add new frames (Alt+N) → navigate with arrow keys → preview with Play (Enter) → tag ranges of frames. Common operations: add frame copying/empty, copy/move frames or cels, remove, reuse via linked cels, tag frames, change frame duration, copy layers/frames/cels between files, loop a section, reverse frames. Onion skinning and Preview Window as extra tools.
- Tiled Mode: "a simple method to draw patterns quickly"; simpler than tilemaps, which "offer a more extensive way to create levels using repeated tiles in any possible arrangement."
- Zoom: Z tool; keys 1–6 map to 100%, 200%, 400%, 800%, 1600%, 3200%; mouse wheel; status-bar slider. (Magnified per-pixel working view is the norm.)
- Save vs Export: Save (Ctrl+S) writes the native `.aseprite` format — "keep the full sprite information intact (layers, frames, etc.)"; can also save PNG directly (losing layer/frame info). Export converts to `.gif` or sequences of `.png` (numbered filenames, e.g. `frame001.png`), can export just one frame/layer/selected frames, has an automatic **Resize on export** field (e.g. 400% for social networks), Animation Direction (Forward/Backward/Ping-Pong), Apply pixel ratio (for non-square pixel sprites, e.g. 2:1), Export for Twitter. Sprite sheets are a dedicated export concept; a CLI exists for automation.
- Customization: preferences, keyboard shortcuts, workspace layout, extensions, scripting. Troubleshooting: data recovery (implies crash-recovery machinery).

### Piskel (Layer A — official home/about page)

- Positioning: "Piskel is a **free online editor** for **animated sprites** & **pixel art**. Design characters, animations, and tiles — right in your browser." Best used in a desktop browser, landscape; "start from scratch" or pick an example sprite.
- Live preview: "Check a preview of your animation in real time as you draw. Adjust the frame delay on the fly."
- Export: "Several export modes supported. Animated GIFs for sharing, spritesheet PNG/ZIP for bigger projects etc…"
- Packaging: open source (GitHub); "Free desktop & offline applications for Windows, OSX and Linux."
- Audience variants: "Piskel For Kids — a child-friendly version of the Piskel editor, designed to be safe and distraction-free"; a "For teachers and parents" section.
- Example gallery grouped by use: Sprite examples, Gameboy retro, Layered backgrounds, Tilesets (attributed to open game art creators). This documents the game-asset + community-sharing context.

### Pro Motion NG (Layer A on the fetched page — official product site)

- Positioning: "pro motion is a pixel drawing and animation software designed similar to the famous Amiga Deluxe Paint (DPaint). Ideal for artists working on detailed and **pixel precise** graphics as required for mobile games and portable game consoles. It also suites well to create light weight graphics for web games."
- Feature set (fetched overview): **Pixel perfect Drawing** ("Automatically remove smeared pixels while drawing freehand"); **Image and Animation Layers** ("decouple editing different parts of your graphic"; can display contents of different projects as a layer, e.g. to test backgrounds or parallax scrolling); **Tile Map Engine** ("Create level maps right inside pro motion. Edit tile graphics in place"); **Onion skinning / Light table** ("See several frames at once and draw inbetween frames"); **Tile and pattern drawing** (pattern draw engine "to create tiles that give seamless patterns when placed side by side"); **Bitmap Fonts** ("Use and create multi colored bitmap fonts"); **Flexible grids** ("any type of grid including Isometric, Octagon, Box and flexible pixels like 2x1"); **Color Palette Editor** ("Cut, Move, Insert or Modify Ranges of Colors, Contrast, Saturation...").
- Commercial tiers: Free edition ($0, limited features, commercial use allowed); full license ($19); upgrade price. Professional users listed: Glu Mobile, Halfbrick, Ubi Soft, WayForward, Gameloft, Digital Eclipse; school adoption list. User quotes reference "pixel art, sprite animating and tile-set creation pipeline".
- Links into a deeper online help (LayersPrimer, tileMappingPrimer, PatternDrawPrimer, bitmapFonts, ZoomGridSettingsDlg, OnScreenPalette) — not fetched; structure of the claims above is limited to the overview page.

### Pixelorama (Layer A on the fetched README — official repository)

- Positioning: "a powerful and accessible open-source pixel art multitool. Whether you want to create sprites, tiles, animations, or just express yourself in the language of pixel art." Available on Windows, Linux, macOS and the Web (Steam, itch.io, Flathub, WinGet, GitHub Pages web build).
- Features (fetched README list): wide range of tools with dynamic mapping to left/right mouse buttons; **advanced animation** — "a timeline composed of layers and frames, including features like onion skinning, audio synchronization, frame tags, and the ability to draw while the animation is playing"; **pixel art focused** — "Perfect pixel lines, indexed mode, and rotation and scaling algorithms tailored specifically to pixel art, like cleanEdge, OmniScale, and rotxel"; **seamless tilemap creation** — "rectangular, isometric or hexagonal tiles for your games"; **powerful layer system** — clipping masks, non-destructive effects (outlines, gradient maps, drop shadows); **palette management** — "choosing from pre-made palettes, importing your own, or creating custom ones"; visual effects; canvas options (guides, rectangular and isometric grids, tile mode); automatic backups; customizable UI; export/import PNG, animated PNG, spritesheets, GIFs, videos; 3D layer support (3D models/shapes into the 2D canvas); command line automation for bulk export; project metadata on layers/frames/cels "to integrate with game development"; extension support (e.g. 2D pixels → 3D voxels); MIT license; multi-language.

### Pixilart (no claims — unreachable)

- Market anchor for the web community pole (editor + sharing community). 403 on both fetch attempts; excluded from all structural claims.

### Historical / market-sample breadth (Layer B / vendor-attested lineage)

- Deluxe Paint lineage is directly asserted by Pro Motion's own site. Palette-driven low-res pixel painting with later animation support satisfies the candidate core with no modern features.
- Static tile/icon editors (no animation, no layers, minimal palettes) satisfy the candidate core → animation, layers, onion skinning, sprite-sheet packaging cannot be definitional.
- MS Paint-class editors (pixel editing at unconstrained resolution) are claimed by the Raster Image Editor pass — the differentiator must therefore be the deliberate constraint (small fixed canvas + per-pixel deliberateness), not the presence of a pencil tool.

## Cross-product Comparison

| Finding | Aseprite | Piskel | Pro Motion NG | Pixelorama | Abstraction level |
|---|---|---|---|---|---|
| document = fixed pixel-size canvas (sprite) | A (size in pixels) | A ("sprite" documents, examples) | A (pixel-precise graphics framing) | A (sprites/tiles framing) | **L0** |
| pixel as deliberate unit of composition (per-pixel placement; pixel-perfect aids) | A (pencil-first toolset, cels to paint) | A (implied by editor nature) | A ("pixel precise", "pixel perfect drawing") | A ("pixel-perfect", perfect pixel lines, pixel-art-tailored algorithms) | **L0** |
| magnified working view over a small grid | A (zoom to 3200%) | A (browser canvas for tiny sprites) | A (grids engine over pixel art) | A (grids, pixel-art canvas options) | **L0** (realization of the constrained canvas) |
| save/export to standard image formats + animation deliverables | A (.aseprite native vs PNG/GIF export) | A (GIF, PNG, spritesheet PNG/ZIP) | A (spritesheet export referenced in quotes) | A (PNG/APNG/spritesheet/GIF/video) | **L0** |
| managed palette surface (swatches, fg/bg colors) | A (color bar, fg/bg, palette) | not documented on fetched page | A (Color Palette Editor) | A (palette management) | L1 (3/4 documented) |
| indexed color mode (pixels reference palette entries) | A (up to 256, propagation rule, transparent index) | — | A (range-based palette editor implies indexed work) | A ("indexed mode") | L1 (common discipline, not universal mode) |
| frame animation machinery (frames with duration, playback preview) | A (frames, duration, Play) | A (live preview, frame delay) | A (animation layers, onion skinning) | A (timeline of layers+frames, audio sync) | L1 (4/4, but static editors fit historically) |
| onion skinning / light table | A | not on fetched page | A | A | L1 (3/4) |
| timeline as layers × frames grid; frame tags; cel/frame reuse | A (tags, linked cels) | — | A (animation layers) | A (frame tags; metadata on cels) | L1 |
| layers | A (background + transparent) | not documented (product has them) | A | A (clipping masks, effects) | L1 (3/4) |
| tile machinery (tiled mode / tilemaps / seamless patterns) | A (tiled mode + tilemaps) | A (tilesets among example uses) | A (tile map engine, pattern engine) | A (rect/iso/hex tilemaps, tile mode) | L1→L2 (game-asset packaging) |
| sprite-sheet export | A | A | A (quotes) | A | L1 |
| export scaling (enlarged output, e.g. for viewing/sharing) | A (Resize on export) | — | — | A (pixel-art-tailored scaling algorithms) | L1 (2/4) |
| pixel-precise freehand cleanup ("pixel perfect") | — (ink/dynamics exist; not named) | — | A | A | L1 (2/4 named) |
| symmetry drawing | A (helper) | — | — | — | L2 (1/4 named on fetched pages) |
| non-square pixel aspect ratios (e.g. 2:1) | A (apply pixel ratio) | — | A (flexible pixels like 2x1) | — | L2 (retro-console packaging) |
| native project format preserving layers/frames/palette | A (.aseprite) | implied (sprite URLs) | — (docs not fetched) | implied (project metadata) | L1 (concept), names vary |
| scriptable/CLI automation | A (CLI, scripting) | — | — | A (CLI) | L2 |
| scripting/extensions | A (extensions, scripting) | open source | — | A (extensions) | L2 |
| web packaging / offline desktop / kids & education editions | desktop (Steam etc.) | A (web + offline + Kids) | desktop; schools list | desktop + web | L2 (packaging/audience) |
| free vs paid posture | paid | free | free tier + paid | free (MIT) | L2 (business model) |

## Canonical Model

### L0 — Defining Invariant (three jointly-held structures)

```text
Constrained low-resolution canvas (the document's pixel dimensions
are a deliberate design constraint, worked on magnified)
    +
Pixel as the unit of composition (editing = placing/modifying
individual pixels; tools snap to the grid; no free-stroke object model)
    +
Persist as standard image / animation deliverable
(PNG/GIF-class export, commonly sprite-sheet/animation packaging)
```

Jointly-held is load-bearing:

- canvas constraint alone (no per-pixel tools) = a viewer/scaler, not an editor
- per-pixel tools without the constraint = the general Raster Image Editor (MS Paint-class)
- constraint + tools without persistence = a toy/demo, not an editor of record

Rejected for L0 (checked against §24):

- **Frame animation** — 4/4 in the modern sample, but static tile/icon editors are historically and presently recognizable pixel editors; animation is the Type's dominant mature capability, not its invariant.
- **Palette/indexed color** — Aseprite itself ships an RGB mode where each pixel is independent; the palette is the discipline of the art form and a near-universal surface, but not required for recognition (tiny-canvas unlimited-color editing is still pixel art editing).
- **Game-asset purpose** — the market is dominated by game asset work, but "express yourself in the language of pixel art" (Pixelorama) and community art editors show purpose is a variant axis.
- **Layers** — 3/4 sampled document them; static single-layer editors fit.

### L1 — Common Mature Structure

- managed palette surface (active fg/bg colors, swatch sets; palette editing operations)
- indexed color mode as a first-class discipline (pixel→palette-index, palette edits propagate)
- pencil-first, pixel-snapped toolset (pencil/eraser/fill-class, line/shape tools, eyedropper, marquee/selection, move)
- pixel-precision aids (pixel-perfect freehand cleanup, perfect-pixel line algorithms)
- frame animation machinery (frames with durations, timeline, playback preview, onion skinning, frame tags, reuse of frames/cels)
- layers with stacking (background/transparent distinction)
- tile/pattern machinery (tiled mode for seamless patterns; tilemap layers)
- zoom/magnification far beyond 100% with grid helpers (incl. isometric grids in some products)
- preview window (work at 1× while zoomed, or animate while drawing)
- native project format vs flattened export; export scaling; sprite-sheet export
- undo/history; autosave/backups; crash recovery in mature desktop products

### L2 — Variant / Optional

- color-mode posture (indexed-first vs RGB-first vs both)
- tilemap engines with level-map authoring inside the art tool
- non-square pixel aspect ratios (retro-console packaging)
- scripting/CLI/extensions
- 3D reference layers, audio sync, bitmap font authoring (single/multi-product extras)
- packaging: desktop app vs web app vs both; Steam/itch distribution; free/OSS vs one-time purchase
- audience editions: kids/education variants; community/gallery pairing (web community editors — Pixilart-class; not directly evidenced this pass)
- business model (free, one-time, freemium)

### L3 — Vendor-specific (research notes only)

- Aseprite: cel/linked-cel terminology, tags, slices, color profiles, Export-for-Twitter option, specific shortcuts (B/E/Z/Alt+N, 1–6 zoom keys), data recovery, .aseprite format name
- Pro Motion NG: DPaint-lineage claim, pattern draw engine, Octagon/Box grids, bitmap fonts, named studio user list, $19 license / free edition split
- Pixelorama: Godot 4 base, cleanEdge/OmniScale/rotxel algorithm names, 3D layers, 2D→voxel extension, Crowdin localization, MIT
- Piskel: spriteKey example URLs, Piskel for Kids branding, offline desktop builds

## Rejected Findings

- "Pixel art editors are game-asset tools" — rejected as definitional; the art-form/community pole exists (Pixelorama positioning; Piskel gallery; Pixilart market posture).
- "Indexed palettes define the Type" — rejected; RGB mode documented in Aseprite; palette discipline is L1.
- "Animation defines the Type" — rejected; historical static editors pass the §24 check.
- "Layers define the Type" — rejected; single-layer historical editors pass.
- "Sprite-sheet export defines the Type" — rejected; it is the game-asset packaging of the general export leg.
- "Web-based" or "desktop" — packaging variants, both poles exist.

## Boundary Findings

### vs Raster Image Editor (processed sibling)

Raster L0 = pixel grid document + direct pixel manipulation + visual canvas + persist as image. Pixel art editor shares every leg but adds the **deliberate constraint**: the canvas is small/fixed as a design decision and the pixel is the individual unit of authorship. Removal tests:

- enlarge the canvas to any free resolution and relax per-pixel deliberateness → general Raster Image Editor
- the reverse direction: a general raster editor *can* be used for pixel art with a pencil tool at 800% zoom — the seam is that this Type's whole toolset, defaults, and output packaging are purpose-built for constrained per-pixel work (pixel-perfect cleanup, palette discipline, tile/sprite-sheet export), not the mere capability

Consistent with the raster pass's own note ("Pixel Art Editor constrains the canvas — low resolution, indexed palettes, pixel-accurate placement tools") and the painting pass's ("constrained resolution/palette… demands pixel-accurate placement").

### vs Digital Painting Application (processed sibling)

Painting optimizes stroke expressiveness at free resolution/size; pixel art removes free-stroke expressiveness (a stroke is just a run of pixels) and adds resolution/color constraints. The painting pass recorded this seam from its side; confirmed from this side.

### vs 2D Animation Application (unprocessed sibling)

Both do frames. The seam is the unit of work and the output: in a pixel art editor each frame is a whole small pixel canvas hand-drawn per frame, the timeline exists to organize sprite animation, and output is GIF/sprite-sheet frames handed to games. In a 2D animation application, scenes/rigs/interpolation/vector artwork dominate. Remove the pixel-grid constraint → 2D animation territory; remove animation from the pixel editor → still a pixel art editor (asymmetric test, so animation stays L1).

### vs Font Editor (processed sibling)

FontForge-class editors include bitmap glyph editing, but the font context (character mapping, metrics, font-file generation) is the discriminator recorded by that pass. A pixel editor without that context is not a font editor; bitmap-glyph editing is a capability slice either way.

### vs game-engine sprite/tile editors

Game engines embed tile/sprite editing; the standalone Type's center of gravity is the art authoring itself, delivered as files to engines. Engine-embedded editing is packaging overlap; the leaf stands as the art-editor Type. (No engine docs fetched this pass — kept as market-structural reasoning, moderate strength.)

### vs Photo Editor / AI Image Editing / Graphic Design

Pixel editors author synthetic images pixel-by-pixel from a blank constrained canvas — no camera-origin images (photo editor), no generative model execution (AI image editing), no object composition model (graphic design).

### vs Illustration Application (processed sibling)

Recorded there: resolution-constrained pixels vs resolution-independent vector geometry. Confirmed from this side.

### Taxonomy note

No taxonomy problem found. The leaf is a genuine Type in the 04.02 family, distinct from both processed siblings by the constraint leg. Consistent with the family's recorded seams.

## Uncertainties

- Pixilart (and the community-editor pole generally) could not be documented from official sources; the community/gallery variant is written as market posture only.
- Piskel's in-editor feature set (layers, palette panel, tools list) was not documented on the fetched page; Piskel claims are limited to positioning, preview, export, and packaging.
- Pro Motion NG's deep operational behavior (online help pages) was not fetched; its claims rest on the vendor's own feature overview.
- Pixelorama's dedicated manual was not reachable (404; docs marked work-in-progress by the vendor); claims rest on the official README feature list.
- Whether every mature product's palette is *index*-based (vs purely a swatch tray in RGB mode) could not be verified across the sample; Aseprite documents both postures (Indexed mode vs RGB with palette bar). Final document therefore treats indexed mode as a common discipline, not a universal mechanism.
- Precise limits (palette max 256 in Aseprite, zoom key percentages, export resize examples) are kept in these notes and out of the final document.

## Final Synthesis

The Pixel Art Editor is the constraint-specialized member of the raster family. Its defining core is three jointly-held structures: a deliberately constrained low-resolution canvas worked on magnified; per-pixel authorship where the individual pixel is the unit of composition; and persistence as standard image/animation deliverables. Around that core, mature products concentrate a characteristic capability set: managed palettes (with indexed color as a common discipline), pencil-first pixel-precise toolsets, frame animation machinery (timeline, onion skinning, preview, tags, reuse), layers, tile/pattern machinery, and a save-vs-export split where the native project preserves layers/frames/palette and export flattens to PNG/GIF/sprite sheets (commonly with scaling for display). Game-asset work is the dominant context but a variant axis, not the definition; the art-form/community pole qualifies equally. The Type holds its seam against Raster Image Editor (constraint + per-pixel deliberateness), Digital Painting (no free-stroke expressiveness), and 2D Animation (frames are whole pixel canvases, not scenes/rigs).
