# Research Notes — Digital Painting Application

> DIRECTORY leaf: "Digital Painting Application" (section 04.02 Raster & Painting)
> Slug: digital-painting-application
> Research date: 2026-09-07
> Sibling leaf already processed: raster-image-editor (its STATUS.md boundary note is the starting constraint for this pass)

---

## Research Goal

Understand what a Digital Painting Application is as an Application Type — from real products, not from feature lists:

- what the defining core is (and what is merely common modern equipment)
- how the painting workflow actually runs (canvas → brush → layers → export)
- where the boundary with Raster Image Editor (already processed), Pixel Art Editor, Illustration Application (vector), and adjacent Types lies
- whether older / regional / lighter products still fit the definition (historical check)

## Initial Boundary (pre-research hypothesis)

- Core use: creating original artwork from scratch on a raster canvas with brush-driven mark-making.
- Users: illustrators, concept artists, comic/manga artists, hobbyists, students.
- Nearest neighbors: Raster Image Editor (same machinery, different primary job — the sibling leaf recorded this as a "primary-job gradient, not a structural wall"), Pixel Art Editor (constrained resolution/palette), Illustration Application (vector object model), Graphic Design Application, AI Image Editing/Generator, 2D Animation Application.
- Unknowns: whether pressure/stylus input is definitional; whether layers are definitional; whether natural-media simulation is definitional; how comic/animation machinery and gallery/artwork management fit; how the low end (simple paint programs) is shared with the raster-editor leaf.

## Research Questions

1. What is the central instrument — is the brush engine the load-bearing structure?
2. What is the document model (canvas, layers, color) and how does it differ from a raster editor's, if at all?
3. How do input devices (stylus pressure/tilt, finger, mouse) enter the model?
4. What auxiliary structures exist (stabilizers, symmetry, perspective guides, reference images, 3D figures)?
5. What are the finish/export mechanics (native format, PSD, PNG/JPEG, time-lapse)?
6. Which capabilities are variant-scoped (natural-media physics, comic production, animation, vector linework, photo-art)?
7. Where exactly is the Raster Image Editor boundary, and is it stable from this side?
8. Historical check: do older/regional/lighter painting products (Deluxe Paint lineage, Paint Tool SAI, ArtRage, Tux Paint) satisfy the minimal definition?

## Representative Products

Selected for market representation + documentation quality + different product philosophies + different customer tiers:

| Product | Philosophy / segment | Evidence tier reached |
|---|---|---|
| Krita | free open-source generalist painting program (illustration, concept art, comics, animation) | Tier 1 — full official manual (docs.krita.org) |
| Corel Painter | premium natural-media emulation heritage, professional desktop | Tier 2 — official product/feature pages (painterartist.com); user guide PDF not fetched |
| Clip Studio Paint | mainstream paid illustration/comic/animation production, multi-device, strong asset ecosystem | Tier 2 — official product pages (clipstudio.net en/ja); operational manual not fetched |
| Procreate | platform-native iPad painting app, consumer-pro, gesture/touch-first | Tier 1 — official handbook (help.procreate.com) |
| Rebelle | small-vendor natural-media simulation specialist (watercolor/oil physics) | Tier 2 — official product page (escapemotions.com); user manual URL 404 |

Historical / breadth check samples (no fetches; structural reasoning + one direct Krita anchor): Deluxe Paint (1985, Amiga, mouse-era paint program), Paint Tool SAI (2000s Japanese lightweight painting program — Krita ships an official "coming from Paint Tool SAI" migration guide, which is direct evidence that SAI is a recognized member of this category), ArtRage (natural-media, simpler), Tux Paint (children's painting program), openCanvas (Japanese).

## Sources

Fetched 2026-09-07 (all successful unless noted):

- Krita 5.3 Manual — https://docs.krita.org/en/ (welcome/positioning)
- Krita 5.3 Manual — User Manual TOC: https://docs.krita.org/en/user_manual.html
- Krita 5.3 Manual — Basic Concepts: https://docs.krita.org/en/user_manual/getting_started/basic_concepts.html
- Krita 5.3 Manual — Brush Engines: https://docs.krita.org/en/reference_manual/brushes/brush_engines.html
- Procreate Handbook — Introduction + full TOC: https://help.procreate.com/procreate/handbook/introduction (via procreate.com/handbook)
- Procreate Handbook — Paint, Smudge, and Erase: https://help.procreate.com/procreate/handbook/brushes/paint-smudge-erase
- Clip Studio Paint — English top page: https://www.clipstudio.net/en/ (incl. PRO/EX comparison table, FAQ)
- Clip Studio Paint — Japanese top page: https://www.clipstudio.net/ja/ (richer feature prose)
- Corel Painter — product page: https://www.painterartist.com/en/product/painter/ (incl. full version-comparison matrix)
- Corel Painter — brand page: https://www.painterartist.com/en/
- Rebelle — product page: https://www.escapemotions.com/products/rebelle (about + key features + version comparison)
- Rebelle user manual — https://www.escapemotions.com/products/rebelle/docs/usermanual/ → **404, abandoned after 1 attempt** (source-access limitation)

Not fetched (avoided per network-effort rule): CSP operational manual (manual URL redirected to marketing top page; not retried after the en/ja tops yielded sufficient Tier-2 evidence), Painter user guide PDF (redirect link), Photoshop/Affinity (not sampled — raster-editor leaf already established their positioning).

Evidence layers used below: **A** = directly observed on an official source for a specific product; **B** = cross-product commonality across the sampled set; **C** = canonical inference (Type-level abstraction).

---

## Product A — Krita (Layer A, Tier-1 manual)

Official positioning (welcome page, quoted):

> "Krita is a sketching and painting program designed for digital artists… an end-to-end solution for creating digital art files from scratch… Explicitly supported fields of painting are illustrations, concept art, matte painting, textures, comics and animations… Although it has features that overlap with other raster editors its intended purpose is to provide robust tool for digital painting and creating artworks from scratch… it is not intended as a replacement for Photoshop… other programs may have more features than Krita for image manipulation tasks, such as stitching together photos."

This is the same quote the raster-image-editor pass used as boundary evidence — from this side it is the *self-declaration* of the Type.

Key observations (all Layer A):

- **Document model**: Image (working copy with layers, color space, canvas size, DPI, metadata) / View (zoom, rotate, **mirror** — "changing the way they view the image is a common way to diagnose… a drawing which is skewed towards one side") / Window; multiple images and views at once. Canvas: "When you save the painting as JPG, PNG et cetera or take a print out… only the content inside this area is taken into consideration."
- **Layers & compositing**: layer stack = drawing order; layer types: Paint (raster, default), Vector, Group, Clone, File, Fill, Filter; transparency masks (grayscale-driven), filter layers/masks, transform masks; "Inherit Alpha or Clipping layers" chapter; 76 blending modes documented.
- **Brush engines**: "Brush engines… take a path and tablet information and add effects to it, making a stroke." 18 named engines (Pixel, Color Smudge, Sketch, Shape, Bristle, Chalk, Clone, Curve, Deform, Dyna, Filter, Grid, Hatching, MyPaint, Particle, Quick, Spray, Tangent Normal). Configurations saved as **presets**; presets loadable/savable/shareable; tag management for brushes.
- **Erase is a brush mode**: "Erasing is a blending mode in Krita. There is no eraser tool, but you can toggle on the brush quickly with the E key to become an eraser." Also a Deform brush engine (brush-driven liquify) and Filter brush engine (brush-driven filters).
- **Colors**: RGB/CMYK/LAB/grayscale education; channels; alpha; color management "very complex"; **Gamut Masks** (constrain the selectable color gamut for color-scheme discipline); soft proofing.
- **Input**: dedicated "Drawing Tablets" chapter — supported tablets, drivers, pressure sensitivity, Wacom specifics; "you can hardly put a ruler against your tablet" → **Assistants** (vanishing point, concentric circles, parallel lines) + grids/guides + snapping; **Mirror Tools** chapter.
- **Animation**: timeline, animation, onionskin dockers; raster frame animation; Japanese animation template (layer structure for production animation).
- **Templates**: Animation / Comic / Design / DSLR / Texture template families.
- **Vector graphics**: vector layers and shape tools exist ("Krita is regarded primarily a raster based application" with some vector capability).
- **Working with images**: save/export/open distinction; incremental version saves; autosave/backup/crash recovery.
- **Customization**: dockers, workspaces, toolbars, shortcuts, canvas input settings.
- Migration guides: "coming from Photoshop" and **"coming from Paint Tool SAI"** — the latter is direct evidence that lightweight regional painting programs are category members.

## Product B — Procreate (Layer A, Tier-1 handbook)

Official positioning: "Procreate is the most advanced painting app ever designed for a mobile device… gives you the feeling of real-world drawing with the power of digital art." iPad + Apple Pencil first.

Key observations (all Layer A):

- **Handbook structure** (itself evidence of the Type's shape): Interface & Gestures (incl. Apple Pencil, Accessibility), **Gallery** (create/preview/organize/import-share/file types — an artwork-management surface), **Colors** (Disc, Classic, Harmony, Value, Palettes, Profiles), **Brushes** (Paint/Smudge/Erase, Brush Libraries, Brush Studio, Brush Studio Settings, Dual Brush, Import & Share), **Layers** (interface/create/organize/options/blend modes/mask/share), Text, **Drawing Guides and Assistance** (2D Grid, Isometric, Perspective, Symmetry, Drawing Assist, QuickShape), **Animation**, **Page Assist** (a sketchbook/journal surface), **3D Painting**, Actions (Add/Canvas/Share/3D/**Video**), Selections, Transform, Adjustments (color adjustments, blur, noise, liquify, clone…).
- **One brush system, three tools**: "Paint, Smudge and Erase are the essential tools of Procreate… You can use *any* brush with Paint, Smudge and Erase." Pigment language: "Paint to add pigment to your canvas… Smudge to move pigment around your canvas… Erase to remove pigment from your canvas." Same brush library shared across all three; tap-and-hold transfers current brush between tools.
- **Brushes**: "hundreds of responsive brushes representing a wealth of various mediums"; most brushes use variable Apple Pencil input — "pressure, tilt, azimuth and barrel roll… to alter brush behaviour"; some brushes respond to stroke speed; **Brush Studio** = build/tweak brushes from the ground up; Dual Brush; brush import/share.
- **Input**: finger or Apple Pencil ("Start creating right away with your finger or the Apple Pencil"); sidebar sliders = size (upper) and opacity (lower); Brush Size Memory (4 saved size/opacity marks per brush).
- **Color**: multiple pickers (Disc/Classic/Harmony/Value), Palettes, color **Profiles** (color management present).
- **Guides**: 2D grid, isometric, perspective, symmetry guides with **Drawing Assist** (strokes snap to the guide); **QuickShape** (draw a shape freehand, it snaps to a perfect form).
- **Animation**: frame-based Animation Assist (handbook section).
- **Page Assist**: a journal/sketchbook mode over artworks (artwork-management variant).
- **3D Painting**: import 3D models and paint directly on them (variant surface).
- **Time-lapse**: Actions → Video (record/export the painting process).
- **File types**: own format + import/share section (PSD/PNG/JPEG etc. per handbook TOC).

## Product C — Clip Studio Paint (Layer A on official product pages; Tier-2)

Official positioning: "The ultimate drawing & painting app… The artist's app for drawing and painting." FAQ: "In addition to its natural and easy-to-use pens and brushes, it offers convenient features not found in other drawing apps/paint apps."

Key observations (Layer A, official pages):

- **Brushes as traditional materials**: "quality brushes that feel just like traditional materials"; "All the brushes you need… from watercolors, to oil paints, crayons, colored pencils, and more. Mix colors just like traditional materials and paint intuitively"; decoration brushes (frills, accessories, clouds, forests "in an instant"); paper texture; brush customization ("描き味の調整" — adjusting the drawing feel).
- **Brush-as-eraser**: "好みのブラシを消しゴムとしても使える" — use your favorite brush as an eraser (ja top page).
- **Asset ecosystem**: CLIP STUDIO ASSETS — "40,000+ free brushes", "100,000+ materials" (ja page), user-created; CLIP STUDIO TIPS official tutorials; ASK Q&A community.
- **Line quality**: "Draw smooth and natural lines with a stylus or your finger. Pen pressure can be adjusted to fit your stylus"; hand-shake correction/stabilization ("手振れ補助… 指描きでもガタガタな線にならない" — even finger drawing yields clean lines); line start/end tapering (入り抜き).
- **Vector layers for linework**: "Adjust the thickness and position of lines after they're drawn, and erase intersecting lines"; "Scale up and down without losing quality"; "4K解像度に拡大しても劣化しないベクターデータ" (vector data that survives 4K upscaling).
- **Coloring machinery**: Fill tool that closes gaps ("線画がつながっていなくても塗りつぶす" — fill even when line art isn't closed; drag to bridge gaps), **lock transparent pixels** ("透明部分をロックして、はみ出さずに塗る"), mask & clip across layers, layer colors for organization, blending modes, Shading Assist (place a light source → suggested shading), filters (blur, line extraction), gradient assets.
- **Reference & support**: 3D drawing figures (デッサン人形) with poseable bodies, 3D head models, **Hand Scanner** (pose 3D hands from live camera video), drawing directly on 3D models, perspective rulers (incl. fisheye ruler per artist testimonial), symmetry ruler, snapping.
- **Adjust-after-draw**: Puppet Warp ("manipulate parts of your drawing like a doll"), Liquify, Mesh Transformation.
- **Comic/manga/webtoon machinery**: panel frames (コマ割り), speech balloons, text, effect lines (集中線), screentones (トーン) "in an instant"; multi-page project management; webtoon tools; print/publishing settings (入稿・印刷設定); PDF/ebook export (EX).
- **Animation**: light table + onion-skin; "from simple gifs to full-blown animations"; used by animation studios; audio + camera work (EX).
- **Editions**: PRO ("for professional illustration") vs EX ("All PRO features + animation and comic features" — multi-page, webtoon, PDF/ebook, full-length animation; PRO limited to simple animation up to 24 frames). Pricing: monthly plans from US$0.99/month; one-time purchase from US$63.00 (Windows/macOS). Devices: Windows/macOS/iPad/iPhone/Galaxy/Android/Chromebook. Volume licensing for education/enterprise; named university and studio adopters. Cloud service (10 GB for works/materials, ja page). Dedicated hardware accessory (TABMATE pen device). Simple mode vs Studio mode (mobile simplified UI).
- **Time-lapse**: export mentioned in an official artist testimonial ("タイムラプスの書き出し").

## Product D — Corel Painter (Layer A on official product pages; Tier-2)

Official positioning: "A realistic painting experience that is anything but ordinary"; "World-class blank canvas painting and photo-art tools; Acclaimed Natural-Media™ emulation & digital art brushes; Infinite customization of brushes, textures, and other media."

Key observations (Layer A, official pages):

- **Media-first brush taxonomy** (version-comparison matrix brush category list): Acrylics, Airbrushes, Blenders, Calligraphy, Chalks, Charcoal, Cloners, Clone Tinting, Conte, Erasers, F-X, Gouache, Glazing, Image Hose, Impasto, Inks, Liquify, Markers, Oils, Pastels, Palette Knives (via Thick Paint), Particles, Pattern Pens, Pens, Pencils, Sargent, Selection brushes, Smart Strokes, Stamps, Sponges, Sumi-e, Texture Brushes, Thick Paint, Watercolors. "renowned dry, wet, and blending media"; "paint that will flow, mix, absorb, and evaporate just like the real thing"; brushes "respond to angle, bearing, and flow data from a stylus".
- **Color tools**: Color Wheel, Mixer, Color Sets, Harmonies, Gradients, color picker, color ramps.
- **Composition tools**: Divine Proportion, Layout Grid, Perspective Guides, **Mirror Painting** (symmetry), Reference Image, Image Navigator.
- **Content library**: Papers, Flow Maps, Patterns, Textures, Gradients, Nozzles, Looks, Weaves, Images, Selections — "Create your own brushes, textures, patterns, palettes and so much more."
- **Photo-art pole**: AI Styles, Auto-Painting, cloning (multiple clone sources, tracing paper, Quick Clone), Photo Restoration — "Use artificial intelligence to jump start the painting process."
- **Layers**: blend modes, layer masks, preserve transparency, pick up underlying color, Thick Paint / Watercolor layer types, Spotlight layer, group/collapse.
- **Selections**: marquee/lasso/wand + **Selection brushes** with Color Selection ("Combine the power of a Magic Wand and the versatility of a Selection Brush"); overlay mode; feather up to 2000 px (numeric detail — research notes only).
- **Performance**: Brush Accelerator™ (one-click hardware optimization); GPU/CPU acceleration claims.
- **Platform**: Windows/Mac; Wacom/Xencelabs/Huion Wintab tablets; Apple Sidecar + Apple Pencil tilt; M1 native; subscription or perpetual/upgrade licensing; **Painter Essentials** (beginner edition) and **ParticleShop** (Photoshop brush plugin powered by Painter) as family satellites; brush packs as add-on commerce; PSD compatibility ("Preserve file content with ease when transferring files between Photoshop and Painter").
- Artist quotes reinforce the Type's promise: "the paper never gets overworked, and you are able to zoom in for ultra-levels of detail, not possible in the traditional world."

## Product E — Rebelle (Layer A on official product page; Tier-2)

Official positioning: "hyper-realistic painting software with phenomenal oils, acrylics, watercolors, and other wet and dry media. Paint pigments color mixing, oil thickness, watercolor diffusion, and NanoPixel technology convincingly mimic the way natural media interact with the canvas and itself."

Key observations (Layer A, official page):

- **Physics simulation as the differentiator**: Real Watercolor Simulation (DropEngine drips, Blow Tool, "Tilt the canvas to get flow effects", granulation, transparent/semi-transparent/opaque media); Oil & Acrylic Impasto; Mixed Media Interactions (oils and watercolors mingle); Bristle Brushes ("particle brush system mimicking each strand"); RealShader with SoftShadows (environment-lit impasto); **Pigment color mixing** ("the first software with physical color mixing based on the light spectrum of the pigments… you can still work in a full RGB color gamut"); RYB color wheel; Metallic materials.
- **Brush system**: wet tools (Oils & Acrylics, Express Oils, Watercolors, Gouache & Inks), dry tools (Pencils, Pastels, Markers, Airbrushes); 260+ presets; Powerful Brush Creator; dirty brush / multicolor brush; Blend, Smudge and Liquify tools; **Brush Line Stabilization** ("Moving Average" or "Pulled String").
- **Canvas & surfaces**: "Full-color ultra-realistic papers, canvases, and other art surfaces" (180+ sold separately); Instant Paper Preview.
- **Layers & masks**: Clipping Masks, Layer Masks, **'Masking Fluid' layer** (traditional-media metaphor made literal), layer groups, Filter Layers, Layer Settings.
- **Aids**: Ruler and Perspective Tool (1/2/3-point), **Symmetry Tool**, Reference Image Guides, grids.
- **Selections/transform**: Selection tools & Magic wand, Paint selection, Rough Feather (organic selection edges), Transform & Warp, Liquify, Fractal Image Processing (ML-based resize).
- **Files**: PNG/JPG/TIF/BMP/WEBP + REB native; Advanced PSD import/export (Pro); heightmap EXR export; **iterative save** (numbered versions); time-lapse recording; Photoshop plug-in (Escape Motions Connect); Motion IO animation scripting (used on a Spider-Verse production per vendor); WebSocket control input.
- **Editions**: Rebelle 8 vs 8 Pro (Pro = bristle brushes, pigment mixing, fractal processing, color management, PSD, etc.); lifetime license + 1 year updates; education discounts; Windows/Mac; tablet support (Wacom/Windows Ink in system requirements).

---

## Cross-product Comparison

| Structure / capability | Krita | Procreate | Clip Studio | Painter | Rebelle | Evidence |
|---|---|---|---|---|---|---|
| Blank-canvas artwork creation as the stated purpose | A ("creating digital art files from scratch") | A ("feeling of real-world drawing") | A ("app made for drawing") | A ("blank canvas painting") | A ("transfer your ideas into digital canvas") | B |
| Brush/stroke engine as central instrument | A (18 engines; "take a path and tablet information… making a stroke") | A (one library drives Paint/Smudge/Erase) | A (brush feel tuning; brush assets) | A (media-category brush taxonomy) | A (260+ presets; Brush Creator) | **B — strongest commonality** |
| Paint / smudge(blend) / erase as modes of the same brush system | A (erase = blending mode; deform/filter brush engines) | A (explicit three-tool one-library) | A (favorite brush as eraser) | A (Blenders category; Erasers category) | A (Blend/Smudge tools) | **B** |
| Raster canvas + pixel artwork | A ("primarily a raster based application") | A | A (raster; vector layers as special layer type) | A | A | B |
| Persist/export as image files | A (save vs export; JPG/PNG etc.) | A (file types, share) | A (industry-standard formats) | A (PSD/TIFF/PCX/TGA guides) | A (PNG/JPG/TIF/BMP/WEBP/REB) | B |
| Layers + blend modes + masks | A (7 layer types, 76 blend modes, transparency masks) | A (blend modes, masks) | A (mask/clip, layer effects, layer colors) | A (layer masks, media-specific layer types) | A (clipping/masks/filter layers) | B |
| Pressure/tilt stylus input | A (dedicated tablets chapter) | A (pressure/tilt/azimuth/barrel roll) | A (pen pressure adjustable) | A (angle/bearing/flow) | A (tablet in sysreqs) | B |
| Brush customization + preset/library + sharing | A (presets, tags, share) | A (Brush Studio, import/share) | A (customization + asset store) | A (infinite customization; brush packs) | A (Brush Creator; free library) | B |
| Color wheel/palette/mixer surfaces | A (+ gamut masks, soft proofing) | A (Disc/Classic/Harmony/Value/Palettes/Profiles) | A (mix like real paint) | A (Wheel/Mixer/Sets/Harmonies) | A (RYB wheel, mixing palette, harmonies) | B |
| Stroke stabilization/smoothing | (in brush settings; not directly quoted this pass) | (Brush Studio settings; not directly quoted) | A (hand-shake correction) | A ("Enhanced brush smoothing") | A (Moving Average / Pulled String) | B (documented in ≥3 of 5) |
| Symmetry / mirror painting | A (Mirror Tools chapter) | A (Symmetry Guide) | A (symmetry ruler) | A (Mirror Painting) | A (Symmetry Tool) | **B — 5/5** |
| Perspective guides / rulers / assistants | A (Assistants) | A (Perspective Guide + Drawing Assist) | A (perspective rulers, fisheye) | A (Perspective Guides) | A (1/2/3-point perspective tool) | **B — 5/5** |
| Selections | A | A | A | A (wand + selection brushes) | A (wand, paint selection) | B |
| Fill / bucket (with line-art-aware behavior) | (fill tools present) | (color drop — not directly quoted) | A (gap-closing fill, lock transparency) | A (Fill Tool, Paint Bucket) | A (Fill tools) | B |
| Transform (incl. warp/liquify/puppet) | A (transform tool, warp/cage/liquify, deform engine) | A (transform section) | A (puppet warp, liquify, mesh) | A (transform tool) | A (transform/warp/liquify) | B |
| Text | A | A | A | A | (not listed) | B (4/5) |
| Reference images | (reference features present) | (reference companion — not directly quoted) | A (3D figures, hand scanner) | A (Reference Image) | A (Reference Image Guides) | B (3/5 direct) |
| Native format + PSD interop | A (.kra; PSD support documented in FAQ — not fetched this pass) | A (own format + share) | A (.clip; Photoshop brush compat quoted) | A (PSD support) | A (REB + PSD Pro) | B (moderate wording in final doc) |
| Time-lapse recording | — | A (Actions → Video) | A (testimonial) | — | A (Record Time-Lapse) | B (3/5 — "several products") |
| Frame animation | A | A | A | — | (scripting only) | variant |
| Vector layers for linework | A (vector layers) | — | A (vector layers headline) | — | — | variant |
| Natural-media physics simulation | partial (color smudge mixing) | partial ("wealth of mediums") | A (materials feel, paper texture) | A (Natural-Media™, flow/absorb/evaporate) | A (full physics: drips, tilt, impasto, pigment mixing) | variant (depth varies hugely) |
| Comic/manga production machinery | partial (comic templates, text tools) | — | A (panels/balloons/tones/multi-page) | — | — | variant |
| 3D reference figures | — | — | A (figures + hand scanner) | — | — | variant (product-specific depth) |
| Photo-art / auto-painting | — | — | — | A (AI styles, auto-paint, clone) | — | variant |
| Artwork browser/gallery surface | (file-based; welcome screen) | A (Gallery) | A (cloud works management) | (file-based) | (file-based + iterative save) | variant (platform-shaped) |
| Editions / pricing spread | free OSS (+ supporter packs) | one-time purchase (iPad) | PRO/EX; subscription or one-time | subscription or perpetual; Essentials edition | 8 vs 8 Pro; lifetime | variant |
| Community asset ecosystem | A (resources page, brush packs) | (folio community) | A (Assets/Tips/ASK) | A (brush packs, Masters) | A (free brush library, gallery) | variant |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

```text
Artwork-creation orientation (blank canvas is the normal starting point;
the artifact is the user's own artwork)
└── Brush-driven mark-making as the central instrument
    (a stroke engine deposits pigment in a user-chosen color along the
     user's gesture; paint / blend / erase are modes of the same brush system)
    └── Raster canvas (the artwork is a pixel image)
        └── Persist as image (save/export the artwork to standard image files)
```

Test — "if this disappeared, would it still be the Type?":

- **Artwork-creation orientation** — without it (primary job = modifying existing images), the product is a Raster Image Editor. This is the recorded sibling boundary; Krita's own positioning ("creating artworks from scratch… not intended as a replacement for Photoshop") is the vendor-side proof.
- **Brush-driven mark-making as central instrument** — without a stroke/pigment engine, the product is a shape/layout tool or a filter box, not a painting app. Cross-product: all five sampled products organize their entire toolset around brushes; erase and blend are brush modes, not separate tool families.
- **Raster canvas** — without it, the product is a vector Illustration Application (different Type in the directory).
- **Persist as image** — without it, it is not a content-creation tool at all.

Deliberately NOT in L0 (each fails the historical check): pressure/stylus input (mouse-era Deluxe Paint, finger-painting Procreate, Tux Paint all qualify without it), layers (Deluxe Paint / simple paint programs have none), natural-media physics simulation (pixel brushes suffice), stabilizers, color management, animation, gallery/artwork browser, 3D references, asset ecosystems, subscription/editions.

### L1 — Common Mature Structure (present in most modern products; not definitional)

- layers with blend modes, opacity, masks, clipping/inherit-alpha, lock-transparency
- pressure/tilt-driven brush dynamics; per-brush size/opacity controls
- brush libraries/presets; brush editors (create/tweak brushes); brush import/sharing
- color surfaces: wheel/disc pickers, mixers, palettes/swatches, harmonies, color history
- stroke stabilization/smoothing
- drawing aids: symmetry/mirror, perspective guides/rulers/assistants, grids, snapping, quick-shape tools
- selections, fill (line-art-aware), transform (incl. warp/liquify/puppet in several products)
- undo/history; canvas navigation (zoom/rotate/mirror view)
- canvas setup (size/DPI presets, templates); native project format + export (PNG/JPEG/TIFF; PSD interop common)
- text tools; reference-image display
- time-lapse recording (several products)

### L2 — Variant / Optional Structure

- natural-media physics simulation depth (from "materials feel" to full watercolor/oil physics with pigment mixing)
- comic/manga/webtoon production machinery (panels, balloons, screentones, effect lines, multi-page projects, print settings)
- frame animation (timeline/onion skin) — when it grows to be the primary job, the product drifts toward 2D Animation Application
- vector layers for editable linework
- 3D reference figures / drawing directly on 3D models
- photo-art / auto-painting / AI style transfer over imported photos
- artwork-management surfaces (gallery/journal/cloud works) — platform-shaped
- platform & business model: desktop/iPad/Android/Chromebook; free OSS vs one-time vs subscription; edition ladders (illustration vs comic/animation tiers; base vs Pro); education/volume licensing
- community asset ecosystems (brush/material marketplaces)
- AI assistance (era-common)

### L3 — Vendor-specific (research notes only)

- Krita: 18 named brush engines; wrap-around mode; gamut masks; MyPaint engine; Python scripting; dockers/workspaces; separate-channels; storyboard SVG export; Japanese animation template.
- Clip Studio Paint: screentones/effect-lines one-action drawing; 3D drawing figures + Hand Scanner; fisheye ruler; Simple/Studio mode switch; page manager; TABMATE hardware; CLIPPY currency; 10 GB cloud; PRO/EX feature split (24-frame animation cap in PRO); creator certification program.
- Painter: Natural-Media™ branding; paper/flow-map/nozzle/image-hose content system; Divine Proportion; Brush Accelerator™; Sargent/Thick Paint/Watercolor layer types; tracing paper; ParticleShop plugin; brush-pack commerce.
- Procreate: QuickShape; QuickMenu; gesture system; Brush Size Memory; Dual Brush; Page Assist; 3D Painting + Lighting Studio; Apple Pencil barrel roll; Scribble.
- Rebelle: DropEngine; NanoPixel 2; RealShader/SoftShadows; pigment spectrum mixing; Masking Fluid layer; Motion IO scripting; WebSocket input; iterative save naming.

## Rejected Findings (considered and NOT promoted)

- **"Pressure-sensitive stylus input" as definitional** — rejected: mouse-era and finger-first products (Deluxe Paint, Tux Paint, Procreate-with-finger) satisfy the Type. L1.
- **"Layers" as definitional** — rejected: the simple paint-program lineage lacks layers and is still a painting program. L1.
- **"Natural-media simulation" as definitional** — rejected: pixel-brush painting (pixel engine, SAI-class linework apps) is core category practice. L2 variant with depth spectrum.
- **"Artwork gallery/management" as definitional** — rejected: desktop products are file-system-based; the gallery is a tablet/platform-shaped surface. L2.
- **"Animation" as definitional** — rejected: Painter (the category's senior product) ships none; Rebelle's is a scripting tool. L2.
- **"Comic/manga machinery" as definitional** — rejected: only one sampled product leads with it; Krita offers only templates. L2.
- **"PSD compatibility" as definitional** — supported in 4–5 products but it is an interchange detail, not a structure. L1 (moderate wording).
- **"Time-lapse" as definitional** — 3/5 products; creator-economy feature. L1 tail / optional.
- **"AI features" as definitional** — era-common at best; only Painter leads with AI photo-art. L2.

## Boundary Findings

### vs Raster Image Editor (sibling leaf, already processed)

The recorded boundary: "primary-job gradient (edit existing pixels vs create artwork from scratch), not a structural wall." This pass confirms it from the painting side:

- Krita's own manual states the split in both directions (painting purpose; explicitly "not intended as a replacement for Photoshop" for image manipulation).
- The machinery (layers, brushes, filters, selections, transform) overlaps almost completely — the L1 sets of the two Types are nearly identical.
- Discriminator test: 去掉"以创作作品为中心"并把"修改已有像素"放到中心 → Raster Image Editor; 去掉"以修改已有图像为中心"并把"从零创作"放到中心 → Digital Painting Application.
- Products genuinely straddle the gradient (painting-first hybrids with full editing cores; editors used for painting). The primary job — and the product's self-positioning — decides the Type. The STATUS.md joint-review flag from the raster pass is discharged from this side: both passes independently reached the same primary-job criterion.
- Residual ambiguity: the platform-native simple paint-program lineage (MS Paint-class) sits on the gradient. The raster leaf claimed it as its historical sample; this leaf's historical check instead uses painting-specific lineage (Deluxe Paint, SAI, ArtRage, Tux Paint). Both claims can coexist because the class is genuinely on the boundary; no taxonomy change proposed.

### vs Pixel Art Editor

Pixel art constrains resolution (small fixed canvases) and color (limited palettes) and demands pixel-accurate placement; painting apps treat resolution and color as free parameters and optimize stroke expressiveness. Pixel-art tools are a constrained specialization, adjacent in the same directory section.

### vs Illustration Application (04.03, under Vector Graphics)

The directory places Illustration under vector graphics: editable object is geometry (Bézier paths), resolution-independent. Painting apps are raster-first; vector layers (CSP, Krita) are a linework convenience inside a raster document, not a different object model. Boundary test: if the artwork's primary editable object is geometry → Illustration Application.

### vs Graphic Design Application (04.01)

Design apps center on layout, templates, brand assets, multi-artboard production; painting apps center on mark-making. Painting is one capability inside a design suite, not its organizing structure.

### vs Photo Editor / RAW Photo Editor (04.04)

Camera-origin single images and photographic adjustment pipelines are the organizing object there; painting apps start from a blank canvas (importing photos is a secondary use — Painter's photo-art pole is the strongest overlap and stays a variant because the brush/paint loop remains the product's center).

### vs AI Image Editing / AI Image Generator (04.20)

Prompt-driven generation or generative editing has no brush-stroke loop as the central instrument. AI features *inside* painting apps (Painter AI styles) are variants.

### vs 2D Animation Application (04.08)

When the timeline/frames/exposure-sheet becomes the primary object and drawing is frame-filling, the product is an animation tool. Painting apps with animation modes (Krita, CSP, Procreate) remain painting-first.

### vs Digital Whiteboard (03.05)

Free-form ink exists on whiteboards, but the organizing structure is shared spatial collaboration (sticky notes, shapes, multi-user canvas), not artwork creation and image persistence.

## Uncertainties

- CSP and Painter operational manuals were not fetched (Tier-2 product pages only). Workflow details for those two products (exact tool options, dialog behavior) are inferred from official feature prose, not manual walkthroughs. Assertion strength in the final doc is calibrated accordingly (no precise numeric limits, no product-specific workflow claims).
- Rebelle user manual 404; all Rebelle evidence is from the official product page (feature list + comparison table). Treated as reliable for capability existence, not for operational detail.
- Krita's stabilizer options and Procreate's StreamLine smoothing were not directly quoted this pass; stabilization is claimed only at "documented in several products" strength (CSP, Painter, Rebelle direct).
- Undo/history: universal in practice but directly quoted only via Rebelle artist quote and Procreate gesture docs; written at common-practice strength without specifics.
- Historical samples (Deluxe Paint, SAI, ArtRage, Tux Paint) were reasoned structurally, not fetched; the SAI membership claim is anchored by Krita's official migration guide (direct evidence), the others by general market knowledge — flagged as inference, not observation.
- Market-size / market-share claims deliberately not made (no source).

## Final Synthesis

A Digital Painting Application is a creation-first raster art studio whose defining core is: **artwork-creation orientation + brush-driven mark-making as the central instrument (with paint/blend/erase as modes of one brush system) + raster canvas + persist as image**. Everything else the market associates with the category — pressure dynamics, layers, natural-media physics, stabilizers, symmetry/perspective aids, color management, animation, comic machinery, galleries, asset ecosystems — is common mature equipment or variant scope, not the definition. The Type's sharpest boundary is the primary-job gradient with the Raster Image Editor (same machinery, opposite starting point: blank canvas vs existing image), confirmed independently by both passes and by vendor self-positioning (Krita). The Type survives the historical check: mouse-era paint programs, lightweight regional linework apps, and children's painting apps all satisfy the minimal core without any modern equipment.
