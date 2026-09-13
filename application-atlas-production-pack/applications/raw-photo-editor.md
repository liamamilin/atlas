# RAW Photo Editor

## Overview

A **RAW Photo Editor** is an application for **developing camera RAW files**: it takes the unprocessed sensor data recorded by a camera, interprets it through the application's own processing engine, lets the photographer adjust that interpretation with a set of revisable parameters, and renders the result into standard delivered image formats.

The defining structure is small:

```text
RAW file (camera sensor data, per camera model)
└── the application's own development engine
    └── parametric develop loop (revisable recipe over the interpretation)
        └── rendered output (JPEG/TIFF-class deliverable)
```

Three properties hold together. Remove the RAW input and the product is an ordinary photo editor working on already-rendered photographs. Remove the parametric develop loop and the product is a RAW file converter or viewer. Remove the rendering step and there is no deliverable — a RAW file cannot be "saved" as an edited RAW in place, so producing a finished image always means rendering the recipe out.

Everything else commonly associated with these products — the photo library, tethered capture, AI-assisted processing, presets, local adjustments, batch export, printing — is standard capability that packages around the develop loop, not what makes the product a RAW editor. Older and simpler RAW converters, including the converters camera manufacturers bundle with their own cameras, satisfy the same core without any of those additions.

## Users & Context

The primary user is a photographer who shoots RAW and wants control over how the captured sensor data becomes a finished image — from enthusiasts shooting their camera's RAW format occasionally to working professionals delivering from every shoot.

Typical reasons to open the application:

- process a shoot's RAW files into deliverable images with the intended exposure, color, and look
- recover detail the in-camera rendering discarded (blown highlights, off white balance, lens faults)
- apply a consistent interpretation across many frames from the same camera and lighting
- produce print-ready or client-ready output at controlled quality

The work context is after the shoot and before delivery. The primary surface is a desktop application; at least one sampled product also ships a tablet/mobile companion that works with the same per-camera RAW support. Studio photographers may work while the camera is still tethered to the computer; the develop loop itself is the same.

## Core Model

### The Defining Core

**The RAW file.** The object of work is a camera-origin file containing sensor data — minimally processed, per camera model. RAW formats are vendor-specific (each major camera line has its own), and support for a given camera is something the product maintains explicitly: mature RAW editors publish per-camera support matrices, track which RAW sub-formats of each camera they support (compressed variants, new bit depths), and add newly released cameras in product updates. The application's own engine — not the camera's in-camera processing — performs the development: decoding the sensor data, demosaicing it into a full-color image, and establishing the initial color interpretation. This is why the same RAW file can look different in different RAW editors, and why a RAW editor's rendering of a file can change when its engine improves.

**The develop recipe.** The user's work is a set of parameters — white balance, exposure, tonal ranges, color, sharpening and noise treatment, lens and geometry corrections — held as a revisable recipe over the RAW interpretation. The original RAW file is never overwritten. Every adjustment remains re-editable; the recipe, not baked pixels, is the edit. This is structurally forced by the format (a RAW file is not an image you can paint on and save back) and is the reason these products keep per-image settings in a database or sidecar files alongside the RAW.

**The rendered output.** The deliverable is produced by rendering the recipe into a standard image format — typically JPEG- or TIFF-class files, with some products also exporting DNG (a standardized RAW container that can carry corrections as metadata rather than baked pixels). The exported image is a snapshot of the recipe at export time; the RAW and its recipe remain the working state, and the same recipe can be re-rendered differently at any time.

### Standard Capabilities

Mature RAW editors commonly add the following around the core. They make the product practical but do not define the Type:

- **A working library surface** — a browser over the RAW files being processed: folders, projects, sessions or catalogs; ratings, color labels, tags, and search. Its scope is the develop work, not the lifetime collection (see Related Application Types).
- **Histogram and clipping instrumentation** — a live histogram linked to the exposure and tone controls, with warnings showing where highlights or shadows lose data. Because the RAW holds more information than the rendered image will, these instruments are the photographer's evidence for how far an adjustment can go.
- **Presets and styles** — saved parameter sets, applied in one step. Products commonly apply a default look to each image as it opens (and a "no correction" state still decodes and demosaics the file — it is not "no processing").
- **Local adjustments** — applying corrections to regions of the image through masks (brushed, drawn, or computed from image content), layered over the global recipe.
- **History and revisability** — a per-image record of the corrections applied, letting the user return to any earlier state of the recipe.
- **Lens and optical corrections** — per-lens profiles or lab-measured correction data for distortion, vignetting, chromatic aberration, and sharpness, bound to the camera/lens combination the file came from.
- **Batch application** — applying one recipe or export configuration across many RAW files.
- **Soft proofing and gamut warnings** — previewing how the rendering will survive the target output (print, specific color spaces).
- **Print and export machinery** — the terminal step: format, size, quality, color space, naming, and destination for the rendered deliverables.

### One Structure, Many Implementations

The core is written conceptually. Implementations vary:

```text
Concept:   RAW input bound to a camera model
Realized:  vendor RAW formats (per-camera support matrices), DNG as a
           standardized input, smartphone RAW as a growing edge

Concept:   the develop recipe as the edit
Realized:  settings in the product's database, XMP-class sidecar files
           next to the RAW, or both

Concept:   the working library
Realized:  shoot-scoped session folders, a catalog database over the
           whole disk, or a plain folder browser

Concept:   rendering out
Realized:  per-image export, batch export with presets, direct print,
           DNG export carrying corrections as metadata
```

A reader who has only seen one product should still be able to recognize the others — including a camera manufacturer's own bundled converter — from the core.

## How It Works

### Bring files into the working library

```text
Point the application at a folder / import from a card
→ the engine builds previews for each RAW file
→ organize (folders/projects/sessions), rate, tag as needed
```

Import depth varies: some products maintain a catalog database over the whole collection, others work directly against folders on disk. Either way, the RAW files themselves stay where they are.

### Develop an image (the center of the product)

```text
Open a RAW file
→ the engine renders its initial interpretation
  (commonly with a default look applied on top)
→ adjust white balance, exposure, tonal ranges, color
→ correct optics (distortion, vignetting, aberrations, sharpness)
→ inspect: histogram, clipping warnings, zoom to pixel level
→ add local adjustments where the global recipe is not enough
→ compare states (before/after, history steps, variants)
```

The loop is interactive and revisable: every control reads and writes the recipe, the preview re-renders, and nothing is final until export. Adjustments interact — exposure changes what tone controls do, optical corrections change what sharpening does — so the develop vocabulary (light → color → detail → geometry) is also the recommended order in most products.

### Render the deliverable

```text
Select image(s)
→ choose format, size, quality, color space, naming
→ export (single or batch)
→ or print directly from the application
```

The exported file is a rendering of the recipe. The RAW and its recipe stay in place; re-opening the image later reproduces or revises the develop state.

### Capability tiers

**Defining core** — without these, not a RAW editor:

- RAW input bound to camera models, developed by the application's own engine
- the parametric non-destructive develop loop
- rendering out to standard formats as the deliverable

**Standard capabilities** — present in most mature products:

- working library surface; histogram and clipping instrumentation
- presets/styles with a default look at open; local adjustments with masks
- history/revisability; lens and optical corrections
- batch application; soft proofing; print; export machinery

**Common variants / optional** — depends on product and segment:

- tethered capture (studio pole); AI-executed processing (neural demosaicing/denoising, AI masking)
- mobile/companion surfaces; command-line and scripting surfaces
- negative-film conversion; DNG export; scene-referred pipeline philosophy
- licensing posture (subscription, perpetual editions, free open source)

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Library / browser surface

The entry surface over the files being processed.

- grid of thumbnails with previews, ratings, labels, metadata
- primary actions: import/locate files, organize into folders/projects/sessions, filter and sort, select images to develop

### Develop surface

The center of the product. A large image viewer flanked by tool panels.

- viewer with zoom to pixel level, before/after and multi-state comparison
- histogram and clipping indicators
- tool palettes organized by photographic concern (light, color, detail, geometry)
- filmstrip of neighboring images from the same shoot
- primary actions: adjust parameters, apply/reset presets, add local adjustments, step through history

### Local adjustment surface

Mask-driven regional corrections, reached from the develop surface.

- mask drawing (brush, gradient, geometric shapes) or content-computed masks
- per-mask parameter sets layered over the global recipe

### Export surface

The terminal step.

- format, resolution, quality, color space, sharpening-for-output, naming and destination
- presets for recurring deliverables; batch across a selection

### Print surface

Present in mature products as a direct output path: layout, size, color management, printer rendering.

### Instrument surfaces

Soft proofing and gamut warning appear as modes or overlays on the develop viewer, previewing the rendering against the intended output.

## Important Rules / Behaviors

### The original is never the deliverable

The RAW file is never overwritten by editing. The recipe lives beside it (database or sidecar); the deliverable exists only as rendered exports. Deleting the recipe loses the develop work; deleting the export loses only that rendering.

### A default interpretation always exists

Opening a RAW file always shows an interpretation — the engine's decode and demosaic, commonly with a default look applied. Even a "no corrections" state is processed output of the engine, not the untouched sensor data. This is why the same file opens differently in different products, and why engine updates can change existing images' appearance.

### Camera support is versioned and granular

Support for a camera model is maintained by the vendor and arrives in product updates. Within one camera, specific RAW sub-formats may be unsupported (particular compression modes, burst formats), and some output options (such as DNG export) may be excluded for particular cameras. Whether a given file is supported is a per-camera-model, per-format question, not a blanket "reads RAW" property.

### RAW and rendered inputs behave differently

The same tool acts differently on RAW and already-rendered input: highlight recovery can rebuild information from RAW channel data that a JPEG has permanently lost, because the RAW retains more than the rendered image shows. At least one sampled product documents this distinction inside its own tool guidance.

### Order matters in pipeline-based products

Where the engine is organized as an ordered processing pipeline, the sequence of operations is part of the recipe and can be inspected and changed; the same parameters in a different order can produce a different result.

### Export semantics vary by target

Rendering to JPEG/TIFF bakes the recipe into pixels. Exporting to DNG-class containers may instead carry corrections as metadata for later re-editing — a different contract, and one some products restrict for particular cameras.

## Variants

- **Pro studio pole** — tethered capture integrated with the develop loop, shoot-scoped session documents, high-volume batch delivery (e.g. Capture One)
- **Optical-science pole** — development built on lab-measured per-camera/lens correction data and neural processing technologies (e.g. DxO PhotoLab)
- **Open-source pipeline pole** — free development around an explicit, re-orderable processing pipeline with scene-referred rendering philosophy (e.g. darktable)
- **Ecosystem/catalog pole** — RAW development embedded in a subscription ecosystem with a whole-library catalog and handoff to a pixel editor for layered work (Lightroom Classic-class)
- **Camera-vendor bundled converters** — the camera manufacturer's own RAW converter, satisfying the same core with support locked to that vendor's cameras
- **Mobile RAW editing** — developing smartphone RAW on the device; a growing edge as phones shoot RAW formats

A variant remains a variant while the develop loop stays the center. When camera control during the shoot becomes the center, the product is a tethered shooting application; when the lifetime collection becomes the center, it is a photo workflow/catalog application.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Photo Editor | edits already-rendered photographs (retouch, filters, layers as the center); may open RAW as a capability without developing being the center |
| Photo Workflow / Catalog Application | the collection system of record across shoots — ingest, select, edit, deliver tracked at library scope; the RAW editor's library is a working surface for the develop loop, not the system of record |
| Tethered Shooting Application | capture-side: camera control, live view, instant capture review; RAW editors bundle tethering as a capability, not the core |
| Image Conversion Application | changes encoding while preserving content; camera RAW appears as read-only decode, with no development of the interpretation |
| Image Batch Processor | configures operations once for a set; RAW editors' batch modes apply the develop recipe at set level, while the interactive per-image loop is the center |
| Raster Image Editor | source-agnostic pixel editing (paint, composite, graphics); a RAW editor never starts from a blank canvas and works in photographic develop vocabulary |
| Photo Culling Application | records selection decisions without altering pixels; cull first, develop the keepers |
| AI Image Editing Application | system models interpret content and produce the change; AI features inside RAW editors execute steps beside the user-driven parametric loop |

The boundary with the Photo Editor is the most important one, because pro products bundle both behaviors. The structural test is the center of gravity: when the product's core job is developing the RAW negative — per-camera support, white balance before rendering, highlight recovery from sensor data, optical corrections, render out — it is a RAW Photo Editor; when the core job is improving already-rendered photographs, it is a Photo Editor.

## Representative Products

- **Capture One** — pro RAW editor; per-camera RAW support matrix as a first-class structure; tethering and session/catalog documents
- **DxO PhotoLab** — RAW-first editor built on per-camera/lens optical correction modules and neural processing
- **darktable** — open-source "raw developer"; virtual lighttable and darkroom; explicit processing pipeline
- **Adobe Lightroom Classic** — market-defining RAW-centric develop + catalog product (referenced as a market anchor; its documentation was not reachable during this research pass — see Sources)

## Sources

Research date: **2026-09-08**

- Capture One Help Center — https://support.captureone.com/hc/en-us — including "Camera Models and RAW Files Supported by Capture One" and "Get Started with Capture One"
- DxO Help Center — https://support.dxo.com/ — DxO PhotoLab FAQ (supported cameras/lenses/formats, DNG input, DeepPRIME, editions)
- DxO PhotoLab 10 Online User Guide — https://userguides.dxo.com/photolab/en/ — Library tab, Customize tab, Local Adjustments, Exporting, Printing chapters
- darktable 5.6 user manual — https://docs.darktable.org/usermanual/5.6/en/ — self-definition, workflow (import & review → process → export), sidecar files & non-destructive editing, Lighttable/Darkroom/Tethering/Print views, module reference
- darktable resources — https://www.darktable.org/documentation/

> Sourcing limitation: Adobe's documentation (helpx.adobe.com) was unreachable during this pass (repeated timeouts). Lightroom Classic is therefore used as a widely-attested market anchor only; no internal operational claims about it are made in this document. Precise vendor facts (support-matrix figures, edition gating, engine internals, default settings) are recorded in the paired Research Notes rather than stated here.
