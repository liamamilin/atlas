# Research Notes — Photo Editor

## Research Goal

Identify the smallest stable invariant that defines the **Photo Editor** Application Type (DIRECTORY 04.04 Photography), and place every other observed capability at the correct abstraction level.

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

This pass also carries three pre-hung flags from sibling passes that it must discharge or refine:

1. **raster-image-editor (04.02, processed)** — boundary claim: "Photo Editor assumes camera-origin single images and centers on photographic adjustments"; test recorded there: remove the photo-centric assumption → generic raster editor; remove general pixel editing, keep only photo adjustments → Photo Editor.
2. **ai-image-editing-application (04.20, processed)** — joint-review flag: the "who executes the edit" seam (system models vs user-driven deterministic tools) is a gradient; flagged for joint review when Photo Editor is processed.
3. **photo-centric-social-network (01.05, processed)** — joint-review flag: VSCO-class creation-first products (editing-first with a community layer) straddle §04.04 and that Type; this pass must apply the remove-social-loop test.

## Initial Boundary

Target:

> Photo Editor (DIRECTORY 04.04 Photography)

Nearest confusing Types:

- Raster Image Editor (04.02, processed) — general pixel editing, source-agnostic
- Digital Painting Application (04.02, processed) — artwork from scratch
- RAW Photo Editor (04.04, unprocessed) — developing sensor data
- Photo Workflow / Catalog Application (04.04, unprocessed) — library/organization/pipeline
- Photo Culling Application (04.04, processed) — selection decisions without pixel changes
- Tethered Shooting Application (04.04, unprocessed) — capture-side
- AI Image Editing Application (04.20, processed) — system-executed edits
- Image Batch Processor / Image Conversion Application (04.05, processed) — set-level automated utilities
- Image Viewer (04.05) — read-only
- Graphic Design Application (04.01, processed) — layout/template compositions
- Photo-centric Social Network (01.05, processed) — social loop over photos

Working hypothesis:

> A photo editor is an application whose object of work is the photograph (a camera-origin image), edited through photographic operations — exposure, tone, color, geometry, retouching — that the user drives with deterministic tools in an interactive per-image loop, producing an edited photo.

Key uncertainties at start:

- Is "camera-origin" load-bearing, or is the real invariant the photographic operation vocabulary?
- Are layers definitional (as in raster editors) or variant? (BeFunky, a major consumer photo editor, appears not to use a layer stack in its edit tab — local adjustments are done per-tool instead.)
- Are presets/filters definitional (mobile-filter-era intuition) or common structure?
- Where does the Type end and RAW Photo Editor / Photo Workflow begin, given that pro products bundle all three?

## Research Questions

1. What is the smallest object/operation model without which a product is no longer recognizable as a photo editor?
2. Where do the adjustment toolset, local adjustments, retouching, presets/filters, layers/masks, non-destructive editing, RAW support, library/organization, batch modes, and AI features sit in the L0–L3 hierarchy?
3. How do consumer web editors, mobile filter-era editors, photographer desktop suites, and professional studio tools realize the same core?
4. What is the structural boundary with Raster Image Editor, RAW Photo Editor, Photo Workflow/Catalog, Photo Culling, AI Image Editing, Image Batch Processor, and Photo-centric Social Network?
5. Do older / platform-native / simpler products (no layers, no presets marketplace, no RAW, no AI) still fit the definition? (§24 check)
6. Does the remove-social-loop test cleanly separate editing-first products with community layers (VSCO-class) from the social Type?

## Representative Products

| Product | Why selected | Docs accessed |
|---|---|---|
| BeFunky | consumer web/mobile photo editor; freemium; explicitly named "Photo Editor"; US | yes (product page + Edit-tab learn article + help center index) |
| Zoner Studio | photographer desktop suite; editor+manager+RAW straddle; European (CZ) vendor; subscription | yes (homepage + functions page) |
| Polarr | mobile/web-first, filter-creator economy; aesthetic-centric philosophy | partial (support center index; article pages blocked) |
| Capture One | professional studio tier; color/tethering-centric; Danish vendor; subscription/perpetual | yes (help center index + User guide category + Styles vs Presets article) |

Selection rationale: four different product philosophies (consumer simplicity / photographer all-in-one / filter-creator economy / professional color+tethering), four customer tiers (consumer → professional), three geographies (US / CZ / DK), three surface families (web+mobile / desktop / desktop+mobile+studio).

Market anchors retained for positioning only (official docs unreachable — see Sources): Adobe Lightroom / Photoshop family, Affinity Photo, Apple Photos, Google Photos, Snapseed, Luminar Neo, Pixlr, Fotor.

## Sources

Research date: **2026-09-08**

Directly fetched official sources (Layer A evidence):

- BeFunky — Photo Editor product page: https://www.befunky.com/features/photo-editor/
- BeFunky — Edit Tab Essentials learn article: https://www.befunky.com/learn/edit-tab-essentials/
- BeFunky — Help Center index: https://support.befunky.com/hc/en-us
- Zoner Studio — homepage: https://www.zoner.com/ and functions page: https://www.zoner.com/en/functions
- Polarr — homepage: https://www.polarr.com and Creator Support index: https://support.polarr.co/hc/en-us
- Capture One — homepage: https://www.captureone.com/ , Help Center index: https://support.captureone.com/hc/en-us , User guide category: https://support.captureone.com/hc/en-us/categories/360000279017-User-guide , Styles vs. Presets article: https://support.captureone.com/hc/en-us/articles/29030106099485-Styles-vs-Presets-What-s-the-Difference , Get Started article: https://support.captureone.com/hc/en-us/articles/35077523196317-Get-Started-with-Capture-One

Source-access Limitation (per `WORKFLOW_v1.1.md §23`):

- `skylum.com` (Luminar Neo) returned HTTP 403 twice → abandoned; no Luminar-specific claims made.
- `pixlr.com` timed out twice → abandoned.
- `support.google.com/snapseed` timed out → abandoned.
- `support.befunky.com` deep category/article pages failed twice (transport error) after the index succeeded → article-level BeFunky evidence limited to the index's promoted-article titles and snippets; the learn article on the reachable `befunky.com` domain was used instead.
- `support.polarr.co` article/category pages returned HTTP 403 after the index succeeded → Polarr evidence limited to index-level titles and the filter-definition snippet visible on the index page.
- `docs.darktable.org` returned HTTP 403 → RAW-side boundary evidence rests on sampled products' own RAW documentation plus widely-attested positioning, not darktable internals.
- `en.wikipedia.org` timed out → the historical check is conceptual (widely-attested product facts only), consistent with how sibling passes handled unreachable historical sources.
- `vsco.co` returned HTTP 403 (consistent with the photo-centric-social-network pass) → the remove-social-loop test is applied structurally, not from VSCO internals.
- Adobe (helpx), Affinity, Apple, Google Photos, Fotor were not attempted this pass: helpx.adobe.com and affinity.help were already established as unreachable in the raster-image-editor pass (timeouts / 403), and platform-native photo apps have no fetchable help-center layer in this environment.
- Consequence: market anchors are retained with **widely-attested structural facts only**; no precise operational claims about them are made. No detail was filled from model memory.

## Product Observations

### BeFunky (Layer A — official product page, learn article, help center index)

- Self-description: "Free Online Photo Editor — Edit your photos in just a few clicks." Suite = Photo Editor + Collage Maker + Graphic Designer (three distinct products in one brand).
- Documented core loop (product page, "How to Edit a Photo in Just a Few Clicks"): **01. Upload Your Photo** (from device, drag-and-drop, or paste) → **02. Make Your Edits** ("crop, adjust lighting and color, apply filters, add text, and more") → **03. Save and Share** ("download your finished photo to your device or post it straight to social media").
- Edit tab → Essentials toolset (learn article, step-by-step): **Crop** (pre-made dimensions or custom; lock aspect ratio), **Exposure** (Brightness / Contrast / Highlights / Shadows sliders; **Erase tab** = brush-paint the same adjustment onto regions; **Isolate Subject** = AI subject isolation so subject and background can be edited separately), **Color** (Hue / Saturation / Temperature + Erase tab + Isolate Subject), **A.I. Image Enhancer** (one-click brightness/color enhancement with an intensity slider), **Rotate** (clockwise/counterclockwise, flip horizontal/vertical, **Straighten** with alignment grid), **Resize** (dimensions or X-Scale/Y-Scale percentages), **Sharpen** (incl. a Smart tab).
- Recommended order in the learn article: crop → exposure → color → enhance → rotate/straighten → resize → sharpen; advanced tools named: Levels, Cutout.
- Other tool families (product page): Touch Up (skin smoothing, teeth whitening, natural retouch), Photo Effects (vintage film, chromatic tones, lens flare), Text Editor, Frames, AI tools (Background Remover, Object Eraser, Sky Replacer, Deblur, Old Photo Restorer, Image Upscaler, AI Image Extender), Photo-to-Art (Cartoonizer™, Oil Painting, Sketcher, Watercolor).
- Batch Photo Editor (Plus subscription): "upload hundreds of images and apply essential editing tools or photo effects to all of them at once."
- Help center index (Tier-1): "Saving as a Project to Edit Later" (save work as a project for future edits), "Resizing Your Images," "Changing Your Download Location" (browser saves to Downloads), "Printing Your Images Created in BeFunky."
- Commercial posture: freemium; many tools free without an account; premium (advanced effects, batch, AI tools) behind BeFunky Plus; no watermark on output; web + iOS/Android app.

### Zoner Studio (Layer A — official homepage + functions page)

- Self-description: "The best photo and video software… From first steps to advanced editing." Windows desktop; subscription (US$5.99/month or US$59/year); unlimited devices; 20 GB cloud; 15 free photo prints; updated twice a year.
- FAQ (homepage): "What can I edit in Zoner Studio? Edit both photos and videos, **including RAW files**. Zoner Studio offers basic and advanced tools, including **cropping, exposure, layers, effects, and color correction**. **Non-destructive editing** ensures the original image data remains unchanged."
- Functions-page feature pillars: **RAW editing** ("lightning-fast RAW loading, batch editing hundreds of photos at once, and intuitive presets"), **Local adjustments**, **Layers and masks**, **LUTs and presets**, **AI editing** ("automatic enhancement for hundreds of photos at once, detect faces, or remove backgrounds with one click"), **Lens and camera profiles**.
- "One Editor, Endless Possibilities — From editing and sorting, to sharing and printing": organize photos (folders, sort by date or location, label, delete, watermark); batch editing; share/back up/print via the Zonerama online gallery; video editing included.
- Adjustment showcase (before/after pairs): Brightening, Vibrance, Sharpness, Straighten Lines (Smart Straighten), Reduce noise, HDR editing ("one of the few programs that works with true HDR"), Retouch facial features and bodies ("add volume to hair, brighten teeth, smooth skin, and shape curves").
- Additional named capabilities: Adjustment variants, Retouching, Layers & masks, Crop and Rotate, Anonymous mode, RAW editing, Lens correction, Resize.
- Positioning: EISA Photo Software 2025-2026 award; learn.zoner.com magazine; masterclass book; testimonials from working photographers (documentary, studio).

### Polarr (Layer A — official homepage + support center index; article pages blocked)

- Self-description (homepage): "Polarr | Photo and Video AI Editors — Elevate your aesthetics with dozens of advanced AI enabled tools, and **millions of Polarr filters made by creators around the world**."
- Product family: Polarr (iOS/Android), Polarr Pro (iOS/macOS/Windows/Web), Polarr Next ("World's first batch RAW editing AI workflow in your browser"), 24FPS (video LUT editor).
- Filter concept (promoted article snippet visible on the support index, Tier-1): "**A Polarr filter is a custom preset containing a series of adjustments you've made.**" Companion articles: "Creating and saving Polarr filters," "Importing Polarr filter" (import filters made by other users).
- Tool names visible in promoted article titles/snippets: Calibration ("Effortlessly Colorize with Calibration… existing color tools like HSL saturations and Toning Curves"), Magic Retouch ("Authentically you with Magic Retouch" — face appearance), AI Color Match, Polarr Copilot (AI assistant).
- Commercial posture: freemium ("Experience Polarr Free… may not love our subscription plans"); multi-language support center (10+ locales) indicating a global consumer audience.

### Capture One (Layer A — official help center: index, User guide category, two articles)

- Self-description (homepage): "Photo software trusted by the best… From first capture to final export, Capture One gives you total control over **color, detail, and tethering**." Genres: portrait, fashion & beauty (tethering on-set), product & food, weddings & events ("easy culling"), landscape.
- User guide editing-tool sections (Tier-1, article counts in parentheses):
  - **Exposure and Contrast** (32): Exposure, Brightness, Contrast, Saturation; Auto adjustments.
  - **Working with Colors** (60): ICC profiles, tone curves, Base Characteristics panel, ProStandard profiles.
  - **Details** (16): Sharpening (with user presets and saved defaults), Enhanced Denoise, focus/sharpness checking.
  - **Lens Correction** (27): lens profiles (specific/generic), chromatic aberration, purple fringing.
  - **Composition** (22): Crop tool, aspect ratios, crop grid, AI Crop (Pro/Studio).
  - **Layer Adjustments** (45): Overview of Layers and Masks, AI Masking, Magic Eraser, Combine Masks, exporting masks to Photoshop.
  - **Retouching Tools**: Retouch Face Selector, Face Skin, Eyes, Teeth.
  - **Histograms / Exposure Evaluation**: exposure meter, optimal exposure for RAW and RGB files.
  - **Styles and Presets** (20) — see below.
  - **Smart Adjustments**: Smart Adjustments, Match Look Tool, Smart Styles.
  - **HDR Merging**, **Panorama Stitching**, **Negative Film scanning/conversion**.
- Styles vs Presets article (Tier-1, verbatim definitions): "A **Style** is a group of pre-configured adjustments made using multiple tools in Capture One. You can apply a Style to one or more images with a single click. Styles can include anything from color grading and exposure to contrast and sharpening settings." / "A **Preset** is a saved adjustment for a single tool, such as Film Grain, White Balance, or Exposure. Presets can be built-in or user-created, and are accessible directly from the tool they apply to." Stacking, copying between images, and saving custom Styles are documented.
- Workflow container (User guide): **Sessions vs Catalogs** (two organizational models), Library tool, Folders, Albums, Smart Albums, Selects Folder/Collection, **Variants** (New Variant / Clone Variant / variant groups), Keywords & Metadata, File naming with tokens, Sequences, **Export/Process Recipes** (multiple formats simultaneously, proofing), Printing, Contact Sheets, **External Editing** (Open With / Edit With; plugins; Affinity .af and PSB file support), **Culling** (Assisted Review Beta), **Shooting Tethered** category, Capture Pilot, Capture One Live, mobile apps (Retouch Faces, Session/Catalog documents), Studio/Enterprise tiers (Actions, multi-user admin, barcode scanner, Cultural Heritage edition with Auto Crop).
- Get Started article: "a complete A to Z walkthrough, **from image import to final export**, with editing tips along the way."

## Historical / Market-Sample Check (§24)

The sampled products are all current-market. Before freezing the core, the definition was tested against older / platform-native / simpler patterns:

- **1990s–2000s consumer photo editors** (Microsoft Picture It!, Adobe PhotoDeluxe, Picasa, iPhoto's edit mode — widely-attested product facts; Wikipedia unreachable so kept conceptual): photograph as object, photographic adjustments (brightness/color/red-eye/crop), interactive per-image loop, save the edited photo. **No layers, no preset marketplace, no RAW, no AI, no library-centricity** (Picasa/iPhoto bundled light organization, but the edit loop stands alone). All satisfy the proposed L0 → the L0 is not an artifact of the current market.
- **Platform-native photo apps** (Apple Photos, Google Photos editors — market anchors, unreachable): conceptually satisfy the L0 (photo + photographic adjustments + interactive loop + saved result) without layers, presets-as-products, or RAW. No platform-bound feature entered the core.
- **Mobile filter-era editors** (Snapseed, VSCO's edit surface — anchors, unreachable): satisfy the L0; filters/presets are saved adjustment sets (the Polarr filter definition generalizes), not a separate structure.
- **Analog ancestor**: the darkroom/print workflow (exposure control, dodging/burning, color correction, cropping, retouching of photographic prints) is the pre-digital form of the same job — the software Type digitizes it. Conceptual support that "photograph + photographic operations" is era-stable.
- **Regional check**: the sample spans US (BeFunky), Czech (Zoner), global-consumer (Polarr), Danish (Capture One) products; no region-bound feature entered the core.

Conclusion: the L0 holds across eras, platforms, and regions. Layers, presets marketplaces, RAW, non-destructive models, libraries, and AI are NOT definitional.

## Cross-product Comparison

| Finding | BeFunky | Zoner Studio | Polarr | Capture One | Level |
|---|---|---|---|---|---|
| object of work is the photograph (camera-origin images) | yes ("upload your photo") | yes (photos incl. RAW) | yes (photo editors) | yes (photos incl. RAW) | **L0** |
| photographic adjustment vocabulary (exposure/tone/color) | yes (Exposure, Color tools) | yes (exposure, color correction, vibrance) | yes (HSL, Toning Curves, Calibration) | yes (Exposure/Contrast, Colors sections) | **L0** |
| user-driven deterministic execution (sliders/tools the user sets) | yes (sliders + Apply) | yes | yes | yes | **L0** |
| interactive per-image loop with immediate visual feedback | yes (edit tab on canvas) | yes | yes | yes (Viewer + tools) | **L0** |
| edited photo as deliverable (save/export/share) | yes (download / post to social) | yes (export/print/Zonerama) | yes | yes (Export Recipes, printing) | **L0** |
| geometry: crop / rotate / flip / straighten | yes (Crop, Rotate, Straighten) | yes (Crop and Rotate, Smart Straighten) | yes (standard) | yes (Composition section, AI Crop) | L1 |
| detail tools: sharpening, noise reduction | yes (Sharpen) | yes (Sharpness, Reduce noise) | yes (standard) | yes (Details section, Enhanced Denoise) | L1 |
| retouching (skin/teeth/eyes/blemishes) | yes (Touch Up) | yes (face/body retouching) | yes (Magic Retouch) | yes (Retouching Tools) | L1 |
| local/regional adjustments (apply an adjustment to part of the photo) | yes (per-tool Erase brush + Isolate Subject) | yes (Local adjustments pillar) | yes (standard masking) | yes (Layer Adjustments, AI Masking) | L1 |
| presets / styles / filters (saved adjustment sets) | yes (Effects, one-click looks) | yes (LUTs and presets) | yes (filter = "custom preset containing a series of adjustments") | yes (Styles = multi-tool group; Presets = single-tool) | L1 |
| before/after comparison | yes (learn article pairs) | yes (showcase pairs) | yes (standard) | yes (standard) | L1 |
| one-click auto enhancement | yes (A.I. Image Enhancer) | yes (AI automatic enhancement) | yes (AI tools) | yes (Auto adjustments, Smart Adjustments) | L1 |
| layers (compositing stack) | **no layer stack observed** (per-tool masking instead) | yes (Layers and masks pillar) | not observed at index level | yes (Layer Adjustments section) | L2 |
| non-destructive editing | partial (save as Project) | yes (FAQ: original data unchanged) | not observed | yes (adjustment/variant model) | L2 |
| RAW support | not observed (consumer web) | yes (RAW editing pillar) | yes (Polarr Next batch RAW) | yes (core; RAW support lists) | L2 |
| library / organization / culling | no (single-image surface) | yes (organize, folders, labels) | no | yes (Catalogs/Sessions, Library, Selects, Assisted Review) | L2 (drifts to Photo Workflow) |
| batch editing | yes (Plus feature) | yes (hundreds at once) | yes (Polarr Next) | yes (batch + recipes) | L2 (drifts to Batch Processor) |
| AI-executed content operations (bg/object removal, sky replace, restoration) | yes (named AI set) | yes (one-click background removal, face detection) | yes (AI tools, Copilot) | yes (AI Masking, AI Crop, Magic Eraser) | L2 (drifts to AI Image Editing) |
| photo-to-art / creative stylization | yes (Cartoonizer, painting/sketch/watercolor) | yes (effects) | yes (aesthetic filters) | less prominent | L2 |
| HDR / panorama | not observed | yes (true HDR) | not observed | yes (HDR Merging, Panorama Stitching) | L2 |
| tethered capture | no | no | no | yes (core pillar) | L2 (adjacent Type) |
| video editing | no | yes (included) | yes (24FPS sibling) | no | L2 (suite bundling) |
| collage/design integration | yes (suite siblings) | no | no | no | L2 (suite bundling) |
| social/community surface | yes (post to social) | no (Zonerama gallery is share/print) | yes (filter creator economy) | no | L2 (drifts to social Type) |
| print output | yes (help article) | yes (prints + Zonerama) | not observed | yes (Printing section) | L2 |
| cloud/mobile companions | yes (mobile app) | yes (Photo Cloud, 20 GB) | yes (mobile-first) | yes (mobile apps, Live) | L2 |
| color management depth (ICC) | not observed | not observed at fetched layer | not observed | yes (60-article Colors section) | L2 (pro depth) |

## L0 — Defining Invariant

The smallest structure without which the product would no longer be recognizable as a photo editor:

```text
Photograph (camera-origin image as the object of work)
└── Photographic operations (exposure, tone, color, geometry, retouching vocabulary)
    └── User-driven execution (deterministic tools; the user sets what changes and by how much)
        └── Interactive per-image loop (adjust while viewing the photo; immediate visual feedback)
            └── Edited photo as deliverable (save/export/share)
```

Removal tests:

- remove *photograph as object* (any raster source: screenshots, scans of graphics, compositing canvases) → **Raster Image Editor**
- remove *user-driven execution* (the system's models interpret content and produce the change) → **AI Image Editing Application**
- remove *interactive per-image loop* (operations configured once, applied to a set) → **Image Batch Processor**
- remove *photographic vocabulary* (only encoding/format changes, content preserved) → **Image Conversion Application**
- remove *deliverable* (view only) → **Image Viewer**

§24 historical check: 1990s–2000s consumer editors, platform-native photo apps, and mobile filter-era editors all satisfy the five properties with no layers, no preset marketplace, no RAW, no non-destructive model, and no AI. Therefore none of those are L0. The definition does not depend on any era, platform, region, or vendor pattern.

Note on the object property: "camera-origin" is the assumption, not a runtime gate — scans of photographs and screenshots of the world pass through the same pipeline; what matters is that the product's world is built around photos of real scenes (people, places, moments), not around synthetic graphics or blank canvases.

## L1 — Common Mature Structure

Common across the researched sample (all four products document them); they make the editor practical but do not define the Type:

```text
Adjustment toolset (exposure: brightness/contrast/highlights/shadows;
  color: saturation/vibrance/temperature/HSL; tone curve/levels;
  sharpening; noise reduction)
Geometry operations (crop with aspect ratios, rotate, flip, straighten)
Retouching (skin smoothing, teeth/eyes, blemish and object cleanup)
Local adjustments (apply an adjustment to a region: brush/gradient/radial
  masking, subject isolation — implemented per-tool or via layers)
Presets / styles / filters (saved adjustment sets applied in one click;
  single-tool presets vs multi-tool styles vs shareable filters)
One-click auto enhancement (deterministic or AI-assisted starting point)
Before/after comparison (the loop's feedback mechanism)
Revisability (undo/step-back and reset; formalized as history or
  non-destructive stacks depending on the product)
Save/export with format and size options
Single-photo editing surface (photo viewer + tool panel)
```

## L2 — Variant / Optional Structure

Presence or absence does not change the Type:

```text
Input & depth
- RAW support (when central → RAW Photo Editor)
- non-destructive editing (adjustment recipes stored; original untouched)
- layers as a compositing stack (pro products; consumer editors often
  use per-tool local adjustments instead)
- HDR merging, panorama stitching
- color management depth (ICC workflows)

Workflow extensions (when central → Photo Workflow / Catalog Application)
- library/organization (folders, albums, keywords, ratings)
- culling/selection stages
- variants (multiple edit versions per photo)
- export recipes / batch pipelines / printing / contact sheets

Automation & AI (when headline → AI Image Editing Application)
- AI-executed content operations (background/object removal, sky
  replacement, restoration, upscaling, subject isolation)
- AI assistants / copilots; AI auto-enhancement as default path

Adjacent surfaces (suite bundling, not Type identity)
- tethered capture (→ Tethered Shooting Application)
- video editing; collage makers; graphic-design siblings
- social sharing / community / filter-creator economies
  (remove the social loop → the photo editor remains)
- cloud sync, mobile companions, web delivery

Commercial posture
- freemium metering, subscriptions, one-time purchase, watermarking
  policies, style/filter marketplaces
```

## L3 — Vendor-specific Structure

Remains in Research Notes only:

- BeFunky: Cartoonizer™ and photo-to-art heritage (since 2007); per-tool "Erase tab" masking; "Isolate Subject"; BeFunky Plus freemium gating; no-watermark promise; suite siblings (Collage Maker, Graphic Designer).
- Zoner Studio: Zonerama online gallery; 15 free prints with subscription; Anonymous mode; Smart Straighten; true-HDR positioning; EISA award; Czech origin; unlimited-device subscription.
- Polarr: filter creator economy ("millions of filters made by creators"); filter import/export between users; Polarr Copilot; 24FPS video sibling; Polarr Next browser batch-RAW.
- Capture One: Sessions vs Catalogs dual organizational model; Variants (New/Clone, variant groups); Export/Process Recipes with tokens; Capture Pilot; Live for Studio; Cultural Heritage edition (Auto Crop, roll-film feedback); barcode scanner tool (Enterprise); Actions with third-party services (Pixelz, Photoroom, Gemini); Style packs as products.
- Market anchors (unreachable, widely-attested only): Adobe Lightroom's develop-module + catalog model; Affinity Photo's layer-based professional editing; Apple Photos / Google Photos platform-native editors; Snapseed's mobile gesture editing; Luminar Neo's AI-first catalog.

## Rejected Findings

- **"Layers are definitional"** — rejected: BeFunky, a major consumer photo editor, documents no layer stack in its edit tab; local adjustments are achieved per-tool (Erase brush, Isolate Subject). Layers are a pro-product implementation of local adjustments (L2). Local adjustments themselves are L1.
- **"Presets/filters are definitional"** — rejected: they are saved adjustment sets (Capture One's own Tier-1 definition; Polarr's filter definition). A photo editor without any preset system is still a photo editor (historical editors had none). L1 because they are near-universal today, but the underlying structure is just "adjustments, saved."
- **"Non-destructive editing is definitional"** — rejected: consumer web editors apply edits to a working copy and save out; non-destructive recipes are a philosophy/implementation (L2). Zoner states it explicitly; BeFunky offers "save as project" as an option.
- **"RAW support is definitional"** — rejected: BeFunky and Polarr's consumer surfaces are photo editors without RAW as the center. RAW is L2; when RAW development is the center of gravity the product is the adjacent RAW Photo Editor Type.
- **"AI features are definitional"** — rejected: all four sampled products ship AI features, but the L0's user-driven execution is what remains when they are removed. AI-executed operations are L2; when they are the headline, the product is the AI Image Editing Type (per that pass's own boundary finding).
- **"The photo editor must include a library"** — rejected: BeFunky and Polarr have no library; the edit loop stands alone. Library/organization is L2 and drifts toward Photo Workflow/Catalog.
- **"Mobile-first or web-first is a different Type"** — rejected: surface is L2; BeFunky (web+mobile), Polarr (mobile/web/desktop), Zoner (desktop), Capture One (desktop+mobile+studio) share the same core.
- **"One-click enhancement makes a product an AI Image Editor"** — rejected: auto-enhancement is a parameterized adjustment the user configures (intensity slider in BeFunky's enhancer); the ai-image-editing pass reached the same conclusion from its side. The discriminator is who interprets the content and decides the change.

## Boundary Findings

1. **vs Raster Image Editor (04.02, processed)** — the discriminator is the photo-centric assumption plus the photographic operation vocabulary. Raster editors are source-agnostic (screenshots, scans, composited graphics, web assets) and center on direct pixel manipulation (paint/erase/fill); photo editors assume camera-origin images and center on photographic adjustments (exposure/tone/color/retouch). Products straddle (Affinity Photo-class; Zoner's layers/effects), decided by center of gravity. Structural tests: remove the photo assumption → raster editor remains; remove general pixel editing/compositing and keep photo adjustments → photo editor remains. **Ratifies the raster pass's boundary from this side.**
2. **vs RAW Photo Editor (04.04, unprocessed)** — the discriminator is the input model: developing sensor data (demosaicing, camera/lens calibration, raw interpretation) vs editing rendered photographs. Many photo editors also open RAW (Zoner, Capture One) — a capability, not a boundary. When RAW development is the center, the product is the RAW sibling. **Flag for the raw-photo-editor pass.**
3. **vs Photo Workflow / Catalog Application (04.04, unprocessed)** — the discriminator is the center of gravity: per-image editing vs the cross-shoot library/organization/pipeline. Pro products bundle both (Zoner organizes + edits; Capture One's Sessions/Catalogs + editing; Lightroom-class). Structural test: remove the library/organization → the editing core remains a photo editor; remove per-image editing → a catalog/browser. **Flag for the photo-workflow pass** (consistent with the culling pass's joint-review note).
4. **vs Photo Culling Application (04.04, processed)** — culling records selection decisions without altering pixels; the photo editor transforms pixels. Fixed order: cull first, then edit the keepers. Capture One ships both (Assisted Review + editing) as stages of one workflow. **Ratifies the culling pass's boundary from this side.**
5. **vs AI Image Editing Application (04.20, processed)** — the discriminator is who executes the edit: the user drives deterministic tools (sets the slider, paints the mask) vs the system's models interpret content and produce the change. All four sampled products bundle AI-executed operations beside manual toolchains; the center of gravity decides. Structural tests: remove AI-executed operations → photo editor remains; remove manual toolchains → AI editor remains. **DISCHARGES the ai-image-editing pass's joint-review flag from this side** — the seam is confirmed as a gradient with a workable center-of-gravity rule, consistent with that pass's finding 2 and its rejected finding "any photo editor with an AI feature belongs to this Type."
6. **vs Image Batch Processor (04.05, processed)** — editors make interactive, per-image decisions while looking at the photo; batch processors configure operations once for a set. Editor batch modes (BeFunky Batch Photo Editor, Zoner batch editing, Capture One recipes) are this Type's capability embedded in another packaging. **Ratifies the batch pass's boundary from this side.**
7. **vs Image Conversion Application (04.05, processed)** — converters preserve content while changing encoding; photo editors change content per creative intent. Export dialogs inside editors are delivery, not conversion-as-purpose.
8. **vs Digital Painting Application (04.02, processed)** — painting starts from a blank canvas with brush-centric creation; photo editing starts from an existing photograph with adjustment-centric improvement. BeFunky's photo-to-art effects (photo → painting stylization) sit at this seam but remain photo-editor capabilities (the input is still the photo).
9. **vs Graphic Design Application (04.01, processed)** — design centers on layout, templates, multi-element compositions; photo editing centers on the single photograph. Direct vendor evidence: BeFunky ships **Photo Editor and Graphic Designer as separate named products** in one suite — the vendor's own taxonomy separates them.
10. **vs Photo-centric Social Network (01.05, processed)** — remove-social-loop test: remove publish/stream/ties/feeds from a VSCO-class editing-first product and an editing tool remains; the community layer is an added surface (L2), not the editing core. Conversely, adding editing tools to a social network does not make it a photo editor (the feed/ties remain the center). **DISCHARGES the photo-centric-social-network pass's flag from this side**, with the recorded limitation that VSCO's own site remained unreachable (403), so the test is applied structurally, not from VSCO internals.
11. **vs Image Viewer (04.05)** — viewers render without transforming; editors transform. (The culling pass already recorded the viewer-with-ratings overlap; the same capability-overlap logic applies to viewers with rudimentary adjust-and-save.)
12. **vs Tethered Shooting Application (04.04, unprocessed)** — capture-side (camera control, instant capture review) vs edit-side. Capture One bundles both; tethering is a workflow pillar there, not the editing core.

## Uncertainties

- Polarr's article-level documentation was blocked (403); its editing-tool structure beyond the index-visible names (HSL, Toning Curves, Calibration, Magic Retouch, AI Color Match) is unverified. No Polarr-internal claims beyond the index are made.
- BeFunky's help-center article pages were unreachable; the project-save, resize, download-location, and printing facts come from the index's promoted-article titles/snippets and the learn article. Layer-stacking inside BeFunky's editor (if any exists beyond the observed per-tool masking) is unverified — the "no layer stack" observation is scoped to the documented Edit tab.
- Zoner's evidence is product-page level (Tier-2); its in-product module names (Manager/Develop/Editor heritage) were not verified this pass. No module-level claims made.
- Adobe Lightroom, Affinity Photo, Apple/Google platform editors, Snapseed, Luminar Neo, Pixlr, Fotor remain unreachable market anchors; they are used for positioning and the historical check only, with widely-attested facts.
- The exact seam between "photo editor with a library" and "photo workflow application" is a gradient deferred to the photo-workflow pass; this pass records the center-of-gravity test only.
- Whether every consumer photo editor keeps a manual toolchain beside AI features is verified in the sample (all four do) but not beyond it; the final document phrases manual tools as the defining execution model, with AI features as common additions.

## Final Synthesis

Canonical Photo Editor:

```text
L0 (defining invariant)
- Photograph as the object of work (camera-origin image assumed)
- Photographic operations (exposure, tone, color, geometry, retouching)
- User-driven deterministic execution (the user sets the change)
- Interactive per-image loop (adjust while viewing; immediate feedback)
- Edited photo as deliverable (save/export/share)

L1 (common mature structure)
- Adjustment toolset (exposure/color/tone/detail)
- Geometry (crop/rotate/flip/straighten)
- Retouching
- Local adjustments (regional application, per-tool or layered)
- Presets/styles/filters (saved adjustment sets)
- One-click auto enhancement; before/after comparison
- Revisability (undo/reset; non-destructive where implemented)
- Save/export options; single-photo editing surface

L2 (variant / optional)
- RAW support; non-destructive recipes; layer stacks; HDR/panorama; ICC depth
- Library/organization/culling/variants/export pipelines (→ Photo Workflow)
- Batch modes (→ Image Batch Processor capability)
- AI-executed operations and assistants (→ AI Image Editing when headline)
- Tethered capture, video, collage/design siblings, social/community layers
- Cloud/mobile/web surfaces; commercial postures

L3 (vendor-specific)
- BeFunky photo-to-art/Erase-tab/Plus; Zoner Zonerama/prints/Smart Straighten;
  Polarr filter economy/Copilot; Capture One Sessions-Catalogs/Variants/
  Recipes/Cultural Heritage; (anchors: Lightroom develop model, etc.)
```

The Application Document will present the defining core and the common mature structure in natural language, with a Variants section naming the L2 options. L3 stays in Research Notes. The three sibling flags are discharged/ratified as recorded in Boundary Findings.
