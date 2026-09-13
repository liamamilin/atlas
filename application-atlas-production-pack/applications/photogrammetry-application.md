# Photogrammetry Application

## Overview

A **Photogrammetry Application** reconstructs three-dimensional geometry of a real-world subject from multiple photographs. It takes a set of overlapping images of an existing object, scene, structure, or terrain as its input, computes how those images relate to each other in space, and from that relationship derives the geometry of the subject itself — delivered as usable 3D data: a point cloud, a mesh, a textured model, or derived surfaces such as terrain models and orthomosaics.

Its defining core is small:

```text
Photograph Set (multiple views of a real subject)
└── Computed Reconstruction (camera positions + subject geometry derived from image correspondence)
    └── Reconstruction Result (point cloud / mesh / derived surfaces, held in the project)
        └── Deliverable (export, upload, or share for use in other software)
```

Everything else commonly associated with modern photogrammetry — automated alignment, dense point clouds, texturing, drones, cloud processing, phone capture, georeferencing — is widespread in current products but not part of the definition. Older photogrammetry done with manually marked points on photo pairs, and even the analog stereo-plotter workflows that preceded software entirely, satisfy the same core without any of those specifics: the geometry is *measured from what the photographs share*, not authored and not imagined.

## Users & Context

The same reconstruction core serves very different working populations:

- **Surveying and mapping professionals** process drone or aerial imagery into georeferenced maps, terrain models, and measurable 3D surfaces for engineering, construction, agriculture, and public-safety work.
- **Heritage and documentation specialists** (archaeology, cultural heritage, forensics) record sites, artifacts, and scenes as measurable 3D evidence.
- **Game, film, and 3D artists** capture real-world objects, sets, and locations as photorealistic assets for engines and pipelines.
- **Product, design, and e-commerce users** digitize objects for visualization, prototyping, and archives — increasingly with nothing more than a phone.
- **Prosumers and consumers** scan objects and spaces from a guided mobile capture, storing and sharing results in a personal library.

The work has two places: capture happens near the subject (drone flight, walk-around, tabletop rig), while processing is compute-heavy and happens on a workstation or in a cloud service afterwards. The results are almost never the end point — they are consumed by CAD, GIS, game engines, viewers, and record systems, so the application's delivery surface matters as much as its reconstruction engine.

## Core Model

### The Defining Core

Three structures, jointly held:

- **The photograph set as the input of record.** A collection of photographs of one real subject, taken from multiple viewpoints with overlapping coverage. The photographs are the measurement source — nothing is drawn, sculpted, or modeled by hand. If the input is not photographs of a real subject, the product belongs to 3D modeling or sculpting; if the input is a single image and the result is *invented* rather than measured, it belongs to generative image-to-3D tools.
- **Computed reconstruction from image correspondence.** The application relates the overlapping images to each other — older products relied on a user manually marking corresponding points; modern products match image features automatically — and from those correspondences solves both the camera positions and the subject's 3D geometry. This is the defining act of the Type: geometry derived by measurement across views.
- **The reconstruction as a usable 3D deliverable.** The computed geometry materializes as reviewable 3D data in the project — point cloud, mesh, textured model, terrain surface, or map projection — and leaves the application through export, upload, or sharing. Without a deliverable, there is no application, only a calculation.

### Objects Inside a Mature Product

A typical modern product works with these objects, bound together in a **project** (or, on mobile products, a **capture**) that holds the photograph set, the processing settings, and the results:

- **Photographs / cameras** — the imported images, each treated as a camera observation. Products commonly estimate or let users supply each camera's calibrated properties (lens distortion) and its computed position and orientation.
- **Alignment (sparse correspondence)** — the computed web of matching points across images from which camera poses and initial geometry are solved. This is the load-bearing intermediate: reconstruction quality depends on it.
- **Dense point cloud** — the densified 3D point set computed from the aligned images; in mature products it is user-editable and classifiable (e.g., separating ground from vegetation or buildings).
- **Mesh and texture** — the triangulated surface generated from the point cloud, with photographic appearance projected onto it from the source images.
- **Derived map surfaces** — in mapping-oriented products, orthomosaics (georeferenced image maps), digital surface/terrain models, and index or thermal maps computed from the same reconstruction.
- **Control** — the user-supplied constraints that anchor the model to reality: measured scale references, marked control points with known coordinates, or geotagged position metadata read from the images.
- **Verification surfaces** — the products' own quality machinery: reports on alignment and calibration, and visualizations that connect any point of the reconstruction back to the original images it came from, so users can check results against their sources.
- **Measurements** — distances, areas, and volumes taken directly on the reconstruction.
- **Exports** — the deliverable step, in interchange formats (point-cloud, mesh, and geospatial raster/vector formats) or via direct upload to viewers, platforms, and engines.

### One Structure, Many Implementations

The core is conceptual; implementations vary widely across the market:

```text
Concept:             Photograph set of a real subject
Implementations:     drone frames, DSLR ring/tabletop shots, phone walk-around,
                     video frames, 360° panoramas, digitized film, satellite imagery

Concept:             Correspondence-derived reconstruction
Implementations:     manual point marking (older form), automated feature
                     matching + bundle adjustment (modern form)

Concept:             Reconstruction result
Implementations:     textured mesh, point cloud, DEM/DSM + orthomosaic,
                     Gaussian-splat clouds (emerging)

Concept:             Processing substrate
Implementations:     offline desktop workstation, distributed local network,
                     cloud service, phone-capture + cloud, embeddable SDK

Concept:             Scale and position anchoring
Implementations:     scale bar reference, surveyed control points,
                     geotag/flight-log metadata, none (relative model)
```

## How It Works

### The canonical pipeline

Across the researched sample, work flows through the same staged loop, whatever the market pole:

```text
Acquire photographs (overlapping coverage of the subject)
→ import the photograph set into a project
→ align: compute camera positions and the sparse correspondence across images
→ (optionally) add control: scale references, control points, geotags; inspect quality
→ dense reconstruction: compute the dense point cloud
→ generate results: mesh + texture, or map surfaces (orthomosaic / terrain models)
→ inspect, measure, edit: classify points, clean the model, take measurements
→ export / upload / share the deliverables
```

Two behaviors characterize the loop:

- **Results are derived, not edited into being.** The point cloud, mesh, and maps are recomputed outputs of the photograph set plus settings. Users refine results chiefly by improving inputs, adding control, or adjusting processing settings — then re-running the pipeline. Products support this with processing templates at one end (near-one-click) and fully manual parameter control at the other.
- **Verification is a first-class step.** Because everything downstream trusts the alignment, mature products expose quality machinery: reports covering calibration and alignment health, and views that tie any reconstructed point back to the original images, so a user can visually confirm accuracy before delivering.

### Pole-specific realizations

- **Survey / mapping:** drone imagery plus position metadata goes in; the user marks control points, checks the quality report against accuracy requirements, and delivers georeferenced orthomosaics, terrain models, and classified point clouds into GIS and CAD workflows.
- **Creative / entertainment:** tabletop or rig captures of objects, people, and sets; alignment and dense reconstruction feed a textured mesh that is polished and exported into game engines and VFX pipelines — products in this pole commonly expose command-line and API automation so the reconstruction can be scripted into studio pipelines.
- **Mobile / consumer:** a guided in-app capture (walk around the subject at multiple heights and angles), then the photos upload and process in a cloud service; the finished model appears in the user's library for editing, measurement, link-sharing, and export into design software.

### What typically goes wrong

Reconstruction is only as good as the photograph set. Capture guidance in the sampled products consistently directs users to ample overlap between images, sharp texture-rich surfaces, and full angular coverage. Correspondingly, the characteristic failure modes are cameras that fail to align into the block (leaving images unlinked from the reconstruction), distorted or noisy geometry over featureless, reflective, transparent, or moving content, and results with correct shape but no absolute scale — the last being an expected state, not an error, when no scale constraint was supplied.

## Interfaces

Conceptual surfaces; layouts and names vary by product.

### Project / photograph workspace

- Purpose: hold and organize the input of record.
- Typical information: image thumbnails, per-image alignment status and camera properties, project settings.
- Primary actions: import photos, review which cameras aligned, adjust selection.

### 3D reconstruction viewport

- Purpose: the central working surface — inspect the point cloud, mesh, or map results in space.
- Typical information: the reconstruction itself, colorized or textured; measurement overlays; classification colors.
- Primary actions: orbit/zoom, select and edit points or regions, measure, place control.

### Processing configuration

- Purpose: govern how the pipeline runs.
- Typical information: processing templates or step-by-step settings, quality/detail parameters.
- Primary actions: run steps individually or as a batch, re-run after changes.

### Control and quality surfaces

- Purpose: anchor the model to real-world scale/position and verify accuracy.
- Typical information: control-point marking screens, scale references, quality reports, image-to-point linkage views.
- Primary actions: mark/import control, review residuals and calibration, verify against source images.

### Delivery surfaces

- Purpose: get results into the consuming tool.
- Typical information: format options, upload/share targets, export progress.
- Primary actions: export to file formats, upload to platforms/viewers, share links.

### Mobile capture screen (mobile products)

- Purpose: guide the photograph acquisition itself.
- Typical information: live camera view, coverage/positioning cues, capture progress.
- Primary actions: capture frames or video, review coverage, submit for processing.

## Important Rules / Behaviors

- **Scale is not free.** A reconstruction computed purely from photographs has correct relative shape but arbitrary absolute scale and position. True scale requires a supplied constraint — a measured reference distance, surveyed control points, or geotagged metadata. One sampled product ships a dedicated scale-reference tool precisely so users can add real-world distance "without implementation of positioning equipment"; survey products build entire control-point workflows around this rule.
- **Alignment governs everything.** The sparse correspondence solved at the start is the foundation; if images fail to align, nothing downstream exists for them. Products surface per-image alignment status and make re-alignment a routine user action.
- **Coverage and surface character decide success.** The documented capture guidance converges on overlapping coverage from many angles and subjects with visible surface detail. Featureless, mirror-like, transparent, and fast-moving content are the recurring documented hazards; one professional product builds a dedicated filter against artifacts from moving objects.
- **Verification is expected before delivery.** Quality reports and image-to-reconstruction linkage views exist in every professional product researched; in survey practice, checking the report against accuracy requirements is part of the job, not an extra.
- **Everything is re-computable.** Because results derive from inputs plus settings, the project acts as a reproducible recipe: change the control, the settings, or the image set, and the results regenerate. Deliverables are snapshots of that recipe.
- **Reconstruction and capture are separable.** Professional products accept photograph sets from any camera after the fact; mobile products integrate the capture step but still accept uploaded imagery. The defining act remains the reconstruction, not the capture.

## Variants

- **Desktop professional generalist** — offline workstation processing for GIS, heritage, measurement, and VFX imagery alike; edition-split packaging; scripting APIs and distributed processing for large projects.
- **Entertainment-pipeline workstation** — GPU-focused desktop tooling embedded in a game-engine ecosystem, with command-line and remote-automation surfaces for studio integration.
- **Survey / mapping suite** — drone-first products delivering georeferenced maps and terrain models, often as a family: desktop processors, a cloud platform, a mobile terrestrial capture companion, and a separate CAD-bridge product for post-processing.
- **Mobile-first capture app** — guided phone capture with cloud processing, a persistent capture library, annotation and link sharing, and app-store distribution; consumer and prosumer tiers with paid export/limit gates.
- **Cloud platform and SDK postures** — the reconstruction engine itself offered as an online service or as an embeddable SDK running on the customer's infrastructure.
- **Emerging representation** — Gaussian-splatting capture modes appearing alongside classical mesh/point-cloud outputs in several products' current offerings.
- **Historical forms** — manual-marking desktop photogrammetry (user-marked correspondences, solved coordinates, CAD export) and the analog stereo-plotter workflows before it; both satisfy the defining core without any modern machinery.

## Related Application Types

| Application Type | Distinction |
|---|---|
| 3D Modeling Application / Digital Sculpting Application | geometry is authored by hand; photogrammetry's geometry is measured from photographs of an existing subject |
| Generative image-to-3D tools (AI generators) | imagine a model from one or few images; photogrammetry derives geometry from correspondence across many views — vendors themselves ship these as separate tools |
| 3D scanning / laser-scan tooling | measures depth directly with a sensor; photogrammetry derives geometry from image correspondence; professional products commonly accept laser scans as hybrid inputs, but the scan pipeline is a different act |
| Construction Reality Capture Platform | a construction project's visual-record system of record (project container, dated capture sessions, spatial anchoring, progress history) that may use photogrammetric processing internally as one mechanism; remove the record semantics → this Type; remove the reconstruction pipeline → that Type |
| Photo Editor | pixel-level 2D edits on individual images vs cross-image 3D reconstruction |
| 3D Rendering Application | inverse direction: images derived from existing 3D, vs 3D derived from existing images |
| Texture / Material Authoring Application | paints or generates appearance for existing models; photogrammetry captures appearance from the source photos as part of reconstruction |
| GIS platforms / Digital Twin Platforms | consumers and servers of photogrammetric deliverables; they store, analyze, and present the reconstruction rather than compute it |
| Drone flight-planning applications | orchestrate the capture mission; reconstruction is the separate processing act some vendors bundle alongside |

## Representative Products

- Agisoft Metashape — offline desktop professional generalist (GIS, heritage, VFX, measurement)
- RealityScan (Epic Games; formerly RealityCapture) — GPU-speed desktop in an entertainment ecosystem
- Pix4Dmapper / PIX4Dmatic (Pix4D) — drone-first survey and mapping suite
- Polycam — mobile-first capture app with cloud photogrammetry

## Sources

Research date: 2026-09-08. Official product pages and documentation:

- Agisoft — https://www.agisoft.com/ , https://www.agisoft.com/features/professional-edition/ , https://www.agisoft.com/downloads/user-manuals/
- Epic Games (RealityScan documentation) — https://dev.epicgames.com/documentation/en-us/reality-capture , https://dev.epicgames.com/documentation/en-us/realityscan/getting-realityscan , https://dev.epicgames.com/documentation/en-us/realityscan/camera-geometry-in-realityscan-camera-models-and-coordinate-systems-reference
- Pix4D — https://www.pix4d.com/ , https://www.pix4d.com/product/pix4dmapper-photogrammetry-software/ , https://support.pix4d.com/hc/en-us
- Polycam — https://poly.cam/ , https://poly.cam/object-capture , https://poly.cam/tools/photogrammetry

> Sourcing limitation: RealityScan's product site and Polycam's help center were unreachable from the research environment on 2026-09-08, and vendor manual PDFs were not fetched. Claims about those products are kept at the level their reachable official pages support; vendor accuracy figures (e.g., advertised precision numbers) are deliberately excluded as marketing claims. Product-specific capture recommendations (image counts, overlap percentages) are noted as such and not generalized.
