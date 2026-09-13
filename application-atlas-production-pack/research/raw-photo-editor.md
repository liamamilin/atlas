# Research Notes — RAW Photo Editor

## Research Goal

Understand what a RAW Photo Editor actually is, from real products: what its world is made of, what users do in it, how the develop workflow flows, what rules and states matter, and where its boundary runs against Photo Editor, Photo Workflow / Catalog Application, Tethered Shooting Application, Image Conversion Application, Image Batch Processor, Raster Image Editor, Photo Culling Application, and AI Image Editing Application.

This pass also carries two pre-hung joint-review obligations:

1. **photo-editor pass (§04.04, processed 2026-09-08)** — seam (a): "RAW development (sensor data, demosaicing, camera/lens calibration) vs rendered-photo editing: many photo editors open RAW as a capability without becoming RAW editors; center of gravity decides." This pass must ratify or amend from the RAW side.
2. **photo-workflow-catalog-application pass (§04.04, processed 2026-09-08)** — "RAW-development depth → raw-photo-editor when central (raw-photo-editor still unprocessed — seam recorded for that pass to ratify)."

## Initial Boundary

Working hypothesis before research:

- A RAW Photo Editor is an application whose center of gravity is **developing camera RAW files** — interpreting sensor data (demosaicing, white balance, tone, color, optical corrections) through the application's own processing engine, non-destructively, and rendering the result out to standard formats.
- Nearest neighbors: Photo Editor (rendered-photo editing), Photo Workflow / Catalog (library of record), Tethered Shooting (capture side), Image Conversion (RAW decode without development).
- Main unknowns: whether the library surface is definitional; whether tethering is definitional; whether the category is separable from Photo Editor at all (alias risk); how camera-vendor bundled converters fit.

## Research Questions

1. What is the object of work — the RAW file, the rendered image, or both?
2. What does "developing" a RAW file mean operationally (decode, demosaic, white balance, tone, color, optics)?
3. Is editing non-destructive by structural necessity (RAW cannot be saved in place) or by product philosophy?
4. What is the terminal step — is rendering/export to standard formats part of the core loop?
5. How is per-camera support structured (camera models, lens profiles, RAW format variants)?
6. What library/organization surface do RAW editors carry, and is it the same object as the Photo Workflow / Catalog Type's library of record?
7. Where do tethering, AI processing, presets/styles, local adjustments, batch, print, soft-proofing sit — core, common, or variant?
8. What separates a RAW editor from a photo editor that merely opens RAW files?

## Representative Products

| Product | Vendor | Why sampled | Philosophy / tier |
|---|---|---|---|
| Capture One | Capture One (formerly Phase One) | high-end pro RAW editor; per-camera RAW support matrix is a first-class help category | pro studio; tethering + Sessions/Catalogs; perpetual/subscription |
| DxO PhotoLab | DxO Labs | RAW-first editor built on lab-measured optical corrections and neural processing | prosumer/pro; optical-science philosophy; perpetual editions |
| darktable | darktable project (open source, GPL) | self-described "raw developer"; FOSS pole with scene-referred pipeline | enthusiast/pro FOSS; pipeline philosophy; free |
| Adobe Lightroom Classic | Adobe | market-defining RAW-centric develop + catalog product | mass-pro; ecosystem/subscription — **unreachable this pass, anchor only** |

Selection satisfies: market representation (three directly observed across commercial and FOSS poles), different product philosophies (ecosystem/catalog, optical-science, pipeline/FOSS), different customer tiers (pro studio, prosumer, FOSS enthusiast), documentation completeness (all three have Tier-1 operational documentation).

## Sources

Research date: **2026-09-08**

Tier 1 (official operational documentation, directly fetched):

- Capture One Help Center (Zendesk) — https://support.captureone.com/hc/en-us — categories: Shooting Tethered; Camera & Lens support; User guide; Release notes; Learning hub; Capture One mobile
- Capture One — "Camera Models and RAW Files Supported by Capture One" — https://support.captureone.com/hc/en-us/articles/360002718118-Camera-Models-and-RAW-Files-Supported-by-Capture-One
- Capture One — "Get Started with Capture One" (Learning hub) — https://support.captureone.com/hc/en-us/articles/35077523196317-Get-Started-with-Capture-One
- DxO Help Center — https://support.dxo.com/ — PhotoLab FAQ category (v10 documents, General Product Information, Supported Cameras Lenses & Formats, How to's / Functionality)
- DxO PhotoLab 10 Online User Guide — https://userguides.dxo.com/photolab/en/ — chapters: Overview; Interface; Manage images and metadata in the Library tab; Edit pictures with the Customize tab; Local Adjustments; Exporting images; Printing your Images
- DxO PhotoLab 10 User Guide — "Edit pictures with the Customize tab" — https://userguides.dxo.com/photolab/en/the-customize-tab/
- darktable 5.6 user manual — https://docs.darktable.org/usermanual/5.6/en/ — self-definition, Overview (workflow, sidecar files & non-destructive editing, supported file formats), Lighttable, Darkroom (pixelpipe, history stack, masking & blending), Tethering, Print, Module Reference, Special Topics
- darktable resources page — https://www.darktable.org/documentation/ (redirects to resources; manual links, camera support, GPL license statement)

Tier 1 reused from sibling passes (cross-referenced, originally fetched by those passes):

- Capture One Sessions/Catalogs, Variants, Process Recipes, Assisted Review, tethering pillar — research/photo-editor.md, research/photo-workflow-catalog-application.md (2026-09-08)

Unreachable / degraded:

- **Adobe Lightroom Classic** — helpx.adobe.com timed out twice (user-guide root and camera-support page). Used as a widely-attested market anchor only (develop-module + catalog + Photoshop handoff positioning); no internal operational claims made from memory. Recorded per the source-access limitation rule.
- dxo.com product pages returned 403; evidence taken from support.dxo.com and userguides.dxo.com instead (both Tier 1).
- docs.darktable.org/user-guide/* paths 404; correct path is /usermanual/<version>/en/ (found via darktable.org resources page).

## Product A — Capture One (evidence layer A, official help center)

### Key observations

- **Per-camera RAW support as a first-class structure**: the help center maintains a dedicated "Camera & Lens support" category; the article "Camera Models and RAW Files Supported by Capture One" states "All **600+ camera models** listed below are also compatible with Capture One mobile (with the exception of Phase One digital backs and camera systems – currently support is limited to IQ4 digital backs only…)". Each camera entry carries: Version Added, File Support (RAF / ARW / CR3 / CR2 / NEF / NRW / SR2 / DNG native), and a Tethered/Live View/Wireless triple.
- **RAW variant granularity**: per-camera notes document RAW sub-format support — "Lossless Compressed RAW files supported only (not enabled by default)" (Sony a7R VI, a7 V), "mRAW not supported" (Canon 80D), "RAW-S not supported" (Nikon D4/D810), "RAW Burst Mode not supported" (Canon R6 II), "X-Trans to DNG not supported" (Fujifilm), "NEFX files supported from 16.3.4" (Nikon Z8/Zf).
- **DNG export with per-camera exceptions**: "Export to DNG not possible" noted for Canon R5C/R7/R10 — DNG export exists as a capability with documented exceptions.
- **Workflow framing**: "Get Started with Capture One" — "a complete A to Z walkthrough, from image import to final export, with editing tips along the way"; a "Getting Started" short series "explaining key concepts"; related articles: Interface Explained, Five top Capture One Pro tools for tethered photography, Negative Film Conversion Rundown, Headshot Tools: Learn to Retouch.
- **Organizational documents**: Sessions vs Catalogs dual model (article "Sessions vs Catalogs in Capture One: how they work and where to store them"; backups article) — Tier-1 detail already documented by the photo-editor and photo-workflow passes (Sessions = shoot-scoped folders; Catalogs = library database).
- **Tethering embedded**: "Shooting Tethered" is a top-level help category; tethering columns in the camera matrix; ReTether article; "Can I import from a camera over USB?" FAQ.
- **Retouch inside the RAW editor**: "Retouch Tools" article; "Headshot Tools: Learn to Retouch in Capture One"; "Negative Film Scanning and Conversion" (RAW-based film conversion).
- **Mobile companion**: "Capture One mobile" category — "User guide and FAQ related to Capture One for iPad & iPhone"; Session and Catalog documents exist in mobile.

## Product B — DxO PhotoLab (evidence layer A, official user guide + FAQ)

### Key observations

- **Two-tab structure**: PhotoLibrary tab ("Manage images and metadata in the Library tab") + Customize tab ("Edit pictures with the Customize tab") + Local Adjustments chapter + Exporting images + Printing your Images. The edit/manage/export/print split is the product's documented spine.
- **Customize tab = the develop surface**: left pane — Histogram, Move/Zoom, Projects, History, Preset Editor; right pane — Light, Color, Detail, Geometry, Local adjustments, Watermark, DxO ViewPoint, DxO FilmPack palettes.
- **RAW vs rendered distinction documented in the tool itself**: Exposure — "The Exposure tool can often recover information in these areas… particularly with respect to RAW images, whose color channels generally retain some information even for burnt areas. With JPEG images, which have already undergone a series of in-camera processes relative to each RGB channel, however, highlights that are lost are gone for good." A "Correction drop-down menu, specific to RAW-format images" offers five automatic highlight-recovery modes plus manual.
- **Demosaicing named**: the "No correction" preset "deactivates all of the corrections in DxO PhotoLab, so images are displayed 'as shot.' In the case of RAW files, DxO PhotoLab still performs demosaicing using all of the basic settings that are optimal for your camera."
- **Default preset on open**: "As soon as you open an image in DxO PhotoLab, the default full preset DxO Style – Natural is automatically applied" — corrections (Smart Lighting, Selective Tone, ClearView Plus, contrast, vignetting auto, HSL, denoising, lens sharpness, distortion auto) applied at open; user can change the default.
- **Presets**: full presets (every correction on/off with values) vs partial presets (subset); preset categories (General, Portrait/Landscape, B&W, Atmospheres, single-shot HDR, Smartphones, FilmPack designer); create-from-current-settings; ELITE-edition Preset Editor with import/export/sharing.
- **History**: "the Advanced History palette displays all the steps in the work and corrections made to an image… All this information is stored in real time in the DxO PhotoLab database"; steps retained across sessions; default 50 states (10/50/100/250 configurable); "Deleting the history does not delete or reset your corrections."
- **Histogram as develop instrument**: interactive histogram linked to Exposure and Selective Tone sliders; shadow/highlight clipping displayed in false colors; RGB/CMYK channels; pointer color readout.
- **Tone curve**: RGB/R/G/B/L channels; inverted mode "allowing you to convert and work on negative images, including scans of analog film."
- **Camera/lens support as FAQ structure**: "Which camera/lens combinations are supported by DxO PhotoLab for use with RAW images?"; "Which DNG files are supported by DxO PhotoLab as input?"; "Support for RAW generated by smartphones"; X-Trans restrictions article; "My camera and/or lens is not supported. How do I request it?"; supported-cameras page: "Check that DxO PureRAW or DxO PhotoLab supports your camera's RAW format."
- **Neural processing**: DeepPRIME technologies and AI Masks (FAQ: "Will my images be sent to DxO servers when using DeepPRIME technologies or AI Masks?" — local-processing posture); error article for DeepPRIME/DeepPRIME XD artifacts.
- **DNG export semantics**: "Why does DxO PhotoLab now export DNG files with only technical corrections?" — DNG export carries corrections as metadata, not baked pixels.
- **Editions**: Essential and Elite editions (feature gating: Preset Editor, ClearView Plus, Perspective are ELITE).
- **Sibling products in family**: PureRAW (RAW pre-processing for other editors' workflows), FilmPack (film renderings), ViewPoint (geometry) — appear as palettes inside PhotoLab when activated.

## Product C — darktable (evidence layer A, official manual)

### Key observations

- **Self-definition names the category**: "darktable is an open source photography workflow application and **raw developer** — a virtual lighttable and darkroom for photographers. It manages your digital negatives in a database, lets you view them through a zoomable lighttable and enables you to develop and enhance your raw images." (Manual front page, v5.6.)
- **Documented workflow**: Overview → "an introduction to darktable's workflow": introduction → **import & review** → **process** → **export**.
- **Non-destructive by architecture**: "sidecar files & non-destructive editing" chapter (sidecar files, importing sidecars from other applications, local copies); Darkroom chapter: the **pixelpipe** (anatomy of a processing module, pixelpipe & module order, **the history stack**, undo/redo).
- **Views**: Lighttable (digital asset management: collections & film rolls, star ratings & color labels, image grouping, metadata and tagging; lighttable modes include a **culling** mode and full preview), Darkroom (processing modules, masking & blending), Tethering, Map, Slideshow, Print.
- **Masking & blending**: drawn masks, parametric masks, combining drawn & parametric, raster masks, AI masking; blend modes.
- **Module reference = the RAW-development vocabulary**: demosaic, white balance, exposure, raw black/white point, raw chromatic aberrations, raw denoise, highlight reconstruction, input color profile, output color profile, lens correction, filmic rgb, sigmoid, AgX, color balance rgb, color calibration, tone equalizer, color equalizer, negadoctor (film negatives), retouch, crop, rotate and perspective, watermark, etc.
- **Develop-quality utilities**: clipping warning, raw overexposed warning, gamut check, soft proof, color assessment, snapshots, duplicate manager, high quality processing, module order, scopes.
- **Styles** (lighttable utility) = saved looks; **export** utility module shared across views; batch-editing guide ("batch-editing images" tutorial).
- **Programmatic surfaces**: darktable-cli (command-line RAW processing), Lua scripting API, GIMP integration, OpenCL acceleration, darktable-chart (profile calibration), MIDI device support.
- **AI features** chapter in Special Topics (how AI features work, GPU acceleration) + "neural restore" utility module — AI present as additions.
- **Licensing**: GPL 3.0; free; current stable 5.6.1.

## Cross-product Comparison

| Dimension | Capture One | DxO PhotoLab | darktable |
|---|---|---|---|
| Self-positioning | pro RAW editor (camera/lens support as first-class category) | RAW editor built on optical modules + neural processing | "photography workflow application and raw developer" |
| Object of work | per-camera RAW files (600+ models, per-model file-support matrix) | RAW files bound to camera/lens combinations (modules per combination) | "digital negatives" managed in a database |
| Development engine | own RAW engine, per-camera version-gated support | own engine + demosaicing named in docs + DeepPRIME neural | own pixelpipe with demosaic module and module order |
| Non-destructive structure | Sessions/Catalogs + per-image settings | corrections stored in PhotoLab database; history palette | sidecar files + history stack in database |
| Develop vocabulary | exposure/color/detail tools, retouch tools, layers | Light/Color/Detail/Geometry palettes, tone curve, local adjustments | exposure, white balance, tone curve/equalizer, color modules, lens correction, retouch |
| Library surface | Sessions & Catalogs | PhotoLibrary tab (projects, metadata) | Lighttable view (collections, film rolls, ratings, tags) |
| Terminal step | "from image import to final export" | Exporting images chapter (+ DNG export semantics) | workflow: process → export (+ print view) |
| Presets/styles | styles (sibling-pass Tier-1) | full/partial presets, default preset on open | styles utility, module presets |
| Local adjustments | layers/masks (sibling-pass Tier-1) | Local Adjustments chapter | drawn/parametric/raster/AI masks per module |
| Tethering | first-class (help category, camera matrix columns) | not present in documented structure | Tethering view |
| AI processing | noise/retouch AI (learning hub) | DeepPRIME / DeepPRIME XD, AI Masks | AI masking, neural restore |
| Batch | batch export/processing (sibling-pass) | export multiple images | batch-editing guide, darktable-cli |
| Print | (print module, sibling-pass) | Printing your Images chapter | Print view |
| Soft proofing / gamut | (pro color tooling) | gamut warnings FAQ | soft proof + gamut check modules |
| Negative film | Negative Film Conversion articles | inverted tone curve; FilmPack | negadoctor module |
| Mobile | Capture One mobile (iPad/iPhone) | none documented (iOS FAQ says not compatible) | none |
| Licensing | subscription/perpetual | perpetual editions (Essential/Elite) | free, GPL |

## Canonical Model

### L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being a RAW Photo Editor:

1. **The RAW file as the object of work** — the application's central input is camera-origin sensor data (per camera model, with per-model support maintenance), and the application's **own processing engine** performs the development — decoding, demosaicing, color interpretation — rather than consuming the camera's in-camera rendering. Remove → a rendered-photo editor (Photo Editor).
2. **The parametric non-destructive develop loop** — the user adjusts interpretation parameters (white balance, exposure, tone, color, detail, optics) held as a revisable recipe over the RAW interpretation; the original RAW file is never overwritten; every adjustment remains re-editable and the recipe is the edit. Remove → a destructive pixel editor that merely reads RAW (not a RAW developer), or a photo editor.
3. **Rendering out as the deliverable** — the developed result is exported/converted into standard rendered formats (JPEG/TIFF-class, with DNG-export variants); the deliverable is a rendering of the recipe, saved separately from the untouched RAW + recipe working state. Remove → a RAW viewer/converter with no editing deliverable.

Jointly-held load-bearing tests:

- 1 alone (RAW in, render out, no parametric editing) = RAW file converter/viewer (Image Conversion territory)
- 2 without 1 (parametric non-destructive editing over rendered images) = photo editor with non-destructive recipes
- 3 without 1+2 = format converter
- 1+2 without 3 = develop loop with no deliverable (viewer with adjustments)
- 1+3 without 2 = converter with rendering options
- 2+3 without 1 = photo editor (rendered input)

Anti-overfitting note: **demosaicing** is the canonical operation for Bayer-pattern RAW, but the higher-level invariant is "the application's own interpretation of sensor data" — some RAW inputs are already demosaiced (linear DNG), some sensors are not Bayer (Foveon 3-layer), and DxO documents that even its "no correction" preset still demosaics. Demosaicing is the common implementation, not the definition.

### L1 — Common Mature Structure

Present across the directly-observed sample (layer B, cross-product commonality):

- **Library/organize working surface** — Lighttable view (darktable), PhotoLibrary tab (DxO), Sessions/Catalogs (Capture One): collections/film rolls/projects, ratings/labels, metadata. Bundled as packaging for the develop loop; NOT the collection system of record (that is the Photo Workflow / Catalog Type).
- **Histogram + clipping instrumentation** — interactive histogram linked to exposure/tone controls (DxO), clipping warning + raw overexposed warning + scopes (darktable), histogram tooling (Capture One).
- **Presets / styles** — saved parameter sets: full/partial presets with a default applied at open (DxO), styles (darktable), styles (Capture One).
- **Local adjustments with masks** — Local Adjustments chapter (DxO), drawn/parametric/raster masks per module (darktable), layers/masks (Capture One).
- **History stack / revisability** — history palette in a database (DxO), history stack (darktable), per-image settings history (Capture One).
- **Camera/lens optical corrections** — lens correction module (darktable), DxO optical modules per camera/lens combination, lens support category (Capture One).
- **Batch application of the develop recipe** — batch-editing (darktable), export multiple (DxO), batch processing (Capture One).
- **Soft proofing / gamut warning** — soft proof + gamut check (darktable), gamut warnings (DxO FAQ).
- **Print** — Print view (darktable), Printing chapter (DxO), print module (Capture One).
- **Export to standard formats** — the shared terminal step (all three).

### L2 — Variant / Optional Structure

- **Tethered capture** — first-class in Capture One (help category + camera matrix) and darktable (Tethering view); absent from DxO PhotoLab's documented structure. → Tethered Shooting Application when central.
- **AI-executed processing** — DeepPRIME/DeepPRIME XD neural demosaic-denoise + AI Masks (DxO), AI masking + neural restore (darktable), AI noise/retouch (Capture One). Additions beside the parametric loop.
- **Library depth** — whole-collection database, cross-shoot scope, DNG-archive ambitions → Photo Workflow / Catalog when central.
- **Mobile/companion surfaces** — Capture One mobile (iPad/iPhone, 600+ cameras compatible); DxO documents iOS incompatibility; darktable none.
- **Programmatic surfaces** — darktable-cli, Lua API, GIMP integration, OpenCL (darktable); none documented for the commercial two at this depth.
- **Negative-film conversion** — negadoctor (darktable), Negative Film Conversion (Capture One), inverted tone curve + FilmPack (DxO).
- **DNG export** — with per-camera exceptions (Capture One) and "technical corrections only" semantics (DxO).
- **Licensing posture** — subscription (Capture One), perpetual editions (DxO Essential/Elite), free GPL (darktable).
- **Scene-referred vs display-referred pipeline philosophy** — darktable's filmic rgb/sigmoid/AgX module generation is a philosophy variant, not the Type's structure.
- **Input breadth** — JPEG/TIFF correction alongside RAW (DxO documents JPEG/TIFF modes explicitly); RAW-only poles exist.

### L3 — Vendor-specific Structure

Remains in Research Notes only:

- **DxO**: Smart Lighting (uniform/spot-weighted face detection), ClearView Plus haze removal, DeepPRIME/DeepPRIME XD neural processing, lab-measured DxO Optics Modules per camera/lens combination, ViewPoint/FilmPack palettes, Essential vs Elite gating, PhotoLab database history with 50-state default (10/50/100/250), default preset "DxO Style – Natural" with named values, DNG export "technical corrections only" policy, PureRAW sibling (RAW pre-processing for other editors).
- **Capture One**: Sessions vs Catalogs dual documents, Variants (New/Clone, variant groups), Process Recipes with tokens, Assisted Review culling, ReTether, per-camera Tethered/Live View/Wireless matrix, Capture One mobile, Phase One digital-back support scope, Cultural Heritage/Enterprise editions (sibling-pass Tier-1).
- **darktable**: pixelpipe with re-orderable modules, parametric masks, scene-referred module set (filmic rgb, sigmoid, AgX), duplicate manager, darktable-chart calibration tool, Lua/dbus scripting, MIDI support, GIMP integration, OpenCL scheduling profiles.
- **Lightroom Classic (unreachable, widely attested only)**: develop module + catalog database + Photoshop handoff for pixel editing; subscription. No internal claims made this pass.

## Rejected Findings

- **"Tethering is definitional"** — rejected: DxO PhotoLab's documented structure has no tethering chapter; darktable and Capture One both carry it. L2; the capture-side Type is Tethered Shooting Application.
- **"A catalog/library of record is definitional"** — rejected: the library surface is packaging for the develop loop; the develop vocabulary (Customize tab, Darkroom view) is the center in all three products. The library-of-record Type is Photo Workflow / Catalog. Consistent with that pass's own finding.
- **"AI processing is definitional"** — rejected: all three sampled products ship AI features (DeepPRIME, AI masking, neural restore), but removing them leaves the parametric develop loop intact. Consistent with the ai-image-editing pass's who-executes seam.
- **"Scene-referred pipeline is definitional"** — rejected: it is darktable's philosophy (L3); DxO and Capture One do not structure around it.
- **"DNG is the defining format"** — rejected: vendor RAWs (RAF/ARW/CR3/CR2/NEF) are the norm in the camera matrices; DNG appears as one input option and one export option with per-camera exceptions.
- **"RAW editors must be desktop applications"** — rejected: Capture One documents 600+ camera models compatible with its mobile app; surface is L2.
- **"Demosaicing is the definition"** — rejected as the L0 wording: some RAW inputs are linear/already demosaiced; the invariant is the application's own interpretation of sensor data, with demosaicing as the common implementation.
- **"RAW editors are defined by per-pixel retouching"** — rejected: retouch exists (DxO retouch inside local adjustments; darktable retouch module; Capture One Retouch Tools) but operates within the develop pipeline; heavy pixel compositing is the raster editor's territory.

## Boundary Findings

1. **vs Photo Editor (04.04, processed) — DISCHARGES the pre-hung seam (a).** The discriminator is the input model + center of gravity, exactly as the photo-editor pass proposed. RAW editors develop sensor data through their own engine (per-camera support maintenance, demosaic, white balance before rendering, highlight recovery from RAW channel data — DxO documents the RAW-vs-JPEG recovery difference in its own Exposure tool); photo editors improve already-rendered photographs. Many photo editors open RAW as a capability (Zoner's RAW pillar; the photo-editor pass's own Capture One sample is RAW-centric) — a capability, not a boundary. Structural tests: remove RAW development (accept only rendered input) → a photo editor remains; remove the rendered-photo editing center (retouch/filters/layers as the headline) and keep the develop loop → a RAW editor remains. **Keep-both RATIFIED from this side.**
2. **vs Photo Workflow / Catalog Application (04.04, processed) — DISCHARGES the pre-hung seam.** That pass held "RAW-development depth → raw-photo-editor when central." Ratified: the library of record + whole-collection production cycle is the catalog Type's core; RAW editors bundle a working library (Lighttable/PhotoLibrary/Sessions) as packaging for the develop loop. Test: remove the library → the develop loop remains a RAW editor; make the cross-shoot collection system of record the center → photo-workflow-catalog. The two Types bundle each other's capabilities at the pro pole (Capture One, Lightroom) — packaging, not identity.
3. **vs Tethered Shooting Application (04.04, unprocessed)** — capture-side (camera control, live view, instant capture review) vs develop-side (interpretation of captured files). Capture One and darktable bundle tethering; DxO PhotoLab does not. **Flag for that pass**: tethering inside a RAW editor is a variant capability; when camera control is the center, the product is the tethered Type.
4. **vs Image Conversion Application (04.05, processed)** — converters preserve content while changing encoding; that pass's own evidence documents camera RAW as **read-only decode** in converters (no development). RAW editors change the interpretation (exposure/WB/tone/color/optics) per creative intent. The seam is corroborated from the converter side's own findings.
5. **vs Image Batch Processor (04.05, processed)** — batch modes inside RAW editors (darktable batch-editing guide; DxO multi-image export; Capture One batch) apply the develop recipe at set level; the interactive per-image develop loop is the Type's center. Consistent with the batch pass's boundary.
6. **vs Raster Image Editor (04.02, processed)** — photo-centric assumption + photographic develop vocabulary vs source-agnostic pixel editing. A RAW editor never starts from a blank canvas; even its retouch tools operate inside the develop pipeline. Consistent with the raster pass's boundary as ratified by the photo-editor pass.
7. **vs Photo Culling Application (04.04, processed)** — culling records selection decisions without altering pixels; RAW editors transform the interpretation. darktable ships a culling *mode* inside its Lighttable — capability overlap, consistent with the culling pass's viewer-with-ratings note. Fixed order holds: cull first, develop the keepers.
8. **vs AI Image Editing Application (04.20, processed)** — AI-executed operations (neural demosaic/denoise, AI masking) are L2 additions beside the parametric loop; the user still drives the develop parameters. Consistent with that pass's who-executes seam and the photo-editor pass's discharge.
9. **Camera-vendor bundled RAW converters (no directory leaf)** — Canon/Nikon-class bundled converters satisfy the L0 (RAW input, parametric develop, render out) with vendor-locked camera support; they are in-type instances (vendor-locked variant), not a separate Type. Recorded so the definition is not over-fitted to independent commercial products.

## Uncertainties

- **Adobe Lightroom Classic unreachable** (helpx.adobe.com timeouts ×2). Its develop-module + catalog model is consistent with the L0 as a widely-attested anchor, but no internal operational claims are made. If a later pass reaches Adobe docs, the L1 list (presets, local adjustments, tethering absence in Classic, mobile/cloud variants) should be re-verified.
- **DxO PhotoLab tethering**: no tethering chapter in the documented structure — held as "not present in documented structure," not a categorical product claim.
- **Capture One's internal RAW engine details** (demosaic options, pipeline internals) not fetched; the per-camera support matrix is sufficient for the L0 and L2 camera-support findings.
- **Mobile RAW editors** (phone DNG editing) not directly sampled; the only direct evidence is Capture One's mobile camera-compatibility note. Held as variant.
- **Whether every RAW editor accepts rendered inputs (JPEG/TIFF) alongside RAW**: DxO documents JPEG/TIFF correction explicitly; darktable's supported-formats page lists more than RAW; not verified for every product — held as common, not definitional.
- **Exact export-format lists** vary by product and version; the final document speaks of "standard rendered formats" without inventing lists.

## Final Synthesis

The RAW Photo Editor is the **develop-side** photographic application: its object of work is the camera RAW file, its center is the parametric non-destructive develop loop over the application's own interpretation of the sensor data, and its terminal step is rendering the developed recipe out to standard formats. Everything else — the bundled library surface, tethering, AI processing, presets, local adjustments, batch, print, soft-proofing, mobile and CLI surfaces — is common mature structure or variant capability that packages around that loop.

The category is real and distinct from Photo Editor by center of gravity (developing the negative vs improving the rendered photo), and distinct from Photo Workflow / Catalog by what is the system of record (the develop recipe per image vs the collection across shoots). The market's own vocabulary supports the split: darktable self-identifies as a "raw developer"; Capture One maintains per-camera RAW support as a first-class help category; DxO builds its product on camera/lens-specific optical modules. The historical check passes: early-2000s RAW converters (Capture One DSLR, Bibble, RawShooter, Apple Aperture, camera-vendor converters, dcraw-lineage open-source tools) all satisfy the three-leg L0 with no cloud, AI, catalogs, tethering, or subscriptions.

```text
L0 (defining invariant)
- RAW file as the object of work (camera sensor data, per-camera support, app's own development engine)
- Parametric non-destructive develop loop (revisable recipe over the RAW interpretation; original untouched)
- Rendering out to standard formats as the deliverable

L1 (common mature structure)
- Library/organize working surface (bundled, not the collection system of record)
- Histogram + clipping instrumentation
- Presets/styles (saved parameter sets, often with a default applied at open)
- Local adjustments with masks
- History stack / revisability
- Camera/lens optical corrections
- Batch application of the develop recipe
- Soft proofing / gamut warning
- Print
- Export to standard formats (the shared terminal step)

L2 (variant / optional)
- Tethered capture (→ Tethered Shooting when central)
- AI-executed processing (neural demosaic/denoise, AI masking)
- Library depth (→ Photo Workflow / Catalog when central)
- Mobile/companion surfaces
- Programmatic surfaces (CLI, scripting, integrations)
- Negative-film conversion
- DNG export
- Licensing posture (subscription / perpetual / free)
- Pipeline philosophy (scene-referred vs display-referred)
- Input breadth (rendered inputs alongside RAW)

L3 (vendor-specific)
- DxO: Smart Lighting, ClearView Plus, DeepPRIME, Optics Modules, editions, database history
- Capture One: Sessions/Catalogs, Variants, Process Recipes, ReTether, camera matrix, mobile
- darktable: pixelpipe, parametric masks, scene-referred modules, Lua/CLI, OpenCL, chart tool
- Lightroom Classic: develop module + catalog + Photoshop handoff (unreachable, attested only)
```
