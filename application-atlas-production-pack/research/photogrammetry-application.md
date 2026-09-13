# Research Notes — Photogrammetry Application

Research date: 2026-09-08
Directory leaf: Photogrammetry Application (§04.13 3D Creation)
Slug: photogrammetry-application

## Research Goal

Understand what a Photogrammetry Application really is as an Application Type: its defining structure, its canonical processing pipeline, the objects users work with, the rules that govern success/failure, and — critically — its boundaries against (a) 3D Modeling / Sculpting (geometry authoring), (b) laser/depth-sensor scanning, (c) generative AI image-to-3D tools, (d) Construction Reality Capture Platform (a pre-hung joint-review flag from that pass, 2026-09-07), and (e) GIS / digital-twin consumers of its outputs.

## Initial Boundary (hypothesis before research)

- Core use: reconstruct measured 3D geometry (point cloud/mesh/map surfaces) of a real subject from multiple photographs.
- Users: surveyors/GIS, drone mappers, heritage/archaeology documenters, VFX/game artists, product/e-commerce creators, prosumers with phones.
- Nearest neighbors: 3D Modeling Application, Digital Sculpting Application (both author geometry rather than measure it); Construction Reality Capture Platform (records system vs mechanism); laser-scan/3D-scanner tooling (sensor depth vs photo correspondence); generative image-to-3D (imagined vs measured); GIS platforms (consumers).
- Unknowns: per-product pipeline shapes, mobile products' capture-mode bundles, where Gaussian-splatting capture sits, historical fit of analog/manual photogrammetry.

## Research Questions

1. What objects exist inside a photogrammetry project (photos, alignment, clouds, mesh, control, outputs)?
2. What is the canonical processing pipeline, and how does it differ across market poles?
3. What constraints/rules determine success (coverage, overlap, texture, scale, georeferencing)?
4. What is delivered, in what formats, to whom?
5. Which capabilities are survey-pole-specific vs creative-pole-specific vs general?
6. Where exactly are the boundaries vs 3D modeling, scanning, generative 3D, construction reality capture, GIS?
7. Would older / analog / manual forms of photogrammetry still fit the definition?

## Representative Products

Selected for market representativeness + documentation completeness + different product philosophy + different customer tier:

| Product | Pole / philosophy | Customer tier |
|---|---|---|
| Agisoft Metashape | stand-alone offline desktop professional; generalist (GIS, heritage, VFX, measurement) | professional |
| RealityScan (Epic Games; formerly RealityCapture) | GPU-speed desktop embedded in an entertainment ecosystem; automation surfaces (CLI/API) | professional / entertainment |
| Pix4D (PIX4Dmapper / PIX4Dmatic, plus PIX4Dcatch/PIX4Dcloud/PIX4Dsurvey ecosystem) | drone-first survey & mapping suite; accuracy/quality-report culture | geospatial professional |
| Polycam | mobile-first capture app + cloud processing; consumer/prosumer; library/sharing posture | consumer / prosumer / teams |

## Sources

All fetched 2026-09-08 unless noted.

### Agisoft Metashape (Tier 1–2)
- https://www.agisoft.com/ — positioning statement (Tier 2)
- https://www.agisoft.com/features/professional-edition/ — full feature list (Tier 1)
- https://www.agisoft.com/downloads/user-manuals/ — User Manual PDFs exist (Pro + Standard, v2.3; PDFs not fetched — noted as limitation)

### RealityScan (Epic Games)
- https://dev.epicgames.com/documentation/en-us/reality-capture — documentation index (Tier 1)
- https://dev.epicgames.com/documentation/en-us/realityscan/getting-realityscan — install/account flow (Tier 1)
- https://dev.epicgames.com/documentation/en-us/realityscan/camera-geometry-in-realityscan-camera-models-and-coordinate-systems-reference — camera geometry import/estimation/export reference (Tier 1)
- https://www.realityscan.com/en-US — **unreachable ×2 (timeout)**. GUI workflow pages not obtained; see Source-access Limitation.

### Pix4D
- https://www.pix4d.com/ — product ecosystem overview (Tier 2)
- https://www.pix4d.com/product/pix4dmapper-photogrammetry-software/ — workflow, inputs, outputs (Tier 1/2 mix)
- https://support.pix4d.com/hc/en-us — documentation portal with per-product descriptions (Tier 1)

### Polycam
- https://poly.cam/ — product overview, capture modes (Tier 2)
- https://poly.cam/object-capture — Object mode / cloud photogrammetry pipeline (Tier 1/2)
- https://poly.cam/tools/photogrammetry — free photogrammetry tool FAQ incl. capture guidance (Tier 1)
- https://learn.poly.cam/hc/en-us — **unreachable (timeout ×1, retried once)**; help-center detail not obtained.

### Source-access Limitation
RealityScan's marketing site and Polycam's help center were not reachable; Agisoft and Metashape manual PDFs were not fetched. Consequently: no claims are made about those products' GUI step sequences or numeric parameters beyond what the fetched pages document; assertions about those products are kept at positioning/feature-list level.

## Product Observations

### Agisoft Metashape

Key observations (evidence layer A unless noted):

- Positioning (vendor's own words): "a stand-alone software product that performs photogrammetric processing of digital images and generates 3D spatial data to be used in GIS applications, cultural heritage documentation, and visual effects production as well as for indirect measurements of objects of various scales." — defines the Type's breadth from the professional side.
- Documented feature pipeline mirrors the classic photogrammetric chain:
  - **Photogrammetric triangulation** — "processing of various types of imagery: aerial (nadir, oblique), close-range, satellite"; "auto calibration: frame (incl. fisheye), spherical & cylindrical cameras"; multi-camera projects; "scanned images with fiducial marks support" (i.e., even digitized film photography is an input class).
  - **Dense point cloud: editing and classification** — "elaborate model editing", "automatic multi-class points classification", "import/export to benefit from classical point data processing workflow".
  - **DEM: DSM/DTM generation and editing** — breaklines, fill tools; **georeferencing based on EXIF metadata/flight log, GCPs data**; EPSG registry coordinate systems; configurable vertical datums via geoid grids.
  - **Georeferenced orthomosaic generation** — GeoTIFF, KML; block export for huge projects; color correction; "inbuilt ghosting filter to combat artifacts due to moving objects"; custom planar/cylindrical projection for close-range.
  - **3D model: generation and texturing** — "various scenes: archaeological sites, artifacts, buildings, interiors, people"; "direct upload to various online resources and export to many popular formats"; photorealistic textures with HDR and UDIM support.
- Control/accuracy machinery: **GCP import** for georeferencing and accuracy control; "coded/non-coded targets auto-detection for fast GCPs input"; **scale bar tool "to set reference distance without implementation of positioning equipment"** (documented proof that absolute scale is an added constraint, not a free byproduct).
- Measurement: "inbuilt tools to measure distances, areas and volumes"; "to perform more sophisticated metric analysis the products of photogrammetric processing can be smoothly transferred to external tools thanks to a variety of export formats" — the export/handoff act is explicitly the product's delivery logic.
- Adjacent-input fusion: **LiDAR data support** — "aerial LiDAR point attributes support", "external registration support for laser scans", "marker-based alignment of laser scans" — photo reconstruction and scan registration coexist in one product (hybrid capability, not the core).
- Breadth features (professional tier): stereoscopic measurements; hierarchical tiled model + Cesium publishing; 4D modeling from multi-camera rigs ("cinematographic art, game industry"); panorama stitching; multispectral/thermal processing with NDVI; powerline detection; satellite imagery via RPC; Python/Java API; batch processing; network (distributed) processing; cloud processing interface ("visualize and share the variety of the processing results online with colleagues or customers, as well as to embed published projects").
- Edition split: Professional vs Standard editions; separate user manuals per edition.

### RealityScan (Epic Games; formerly RealityCapture)

Key observations (evidence layer A within the limits of the doc pages fetched):

- Documentation portal titles the product family under "RealityScan Documentation" (the desktop product formerly branded RealityCapture now documented as RealityScan in Epic's developer community).
- Install posture: distributed through the Epic Games Launcher with an Epic account; pricing options presented at install (marketing site unreachable, so licensing specifics are NOT recorded).
- The single most defining documentation artifact fetched: **"Camera Geometry in RealityScan: Camera Models and Coordinate Systems Reference"** — "a rigorous reference on the camera models and coordinate systems RealityScan uses to **import, estimate, and export camera geometry** — from the frontal pinhole model ... to the supported lens distortion models and the yaw/pitch/roll and omega/phi/kappa orientation conventions", plus XMP sidecar file formats. This documents, at reference-manual level, that the product's core act includes estimating camera poses and geometry and interoperating (import/export) with external camera-geometry data — i.e., the correspondence/estimation leg and the handoff leg are first-class.
- Automation surfaces: **Command Line Operations** ("Automate your workflow with the CLI commands"); **paRSer templating language** to "extract information about your project, images, creations, and more"; **Remote Command Plugin (REST/gRPC)**; Linux build. A workstation product built to be scripted/embedded in studio pipelines.
- Entertainment-ecosystem adjacency: install path sits alongside Unreal Engine / Fab / Twinmotion in the same launcher — the downstream consumer of its assets is the game/VFX pipeline.
- Layer B inference (cross-product, limited by unreachable marketing pages): the product's *documented vocabulary* (projects, images, "creations", alignment/estimation, exports) matches the same object world as Metashape/Pix4D.

### Pix4D (PIX4Dmapper / PIX4Dmatic ecosystem)

Key observations (evidence layer A):

- Documented end-to-end workflow on the PIX4Dmapper product page, in the vendor's own five stages: **Capture → Digitize → Control → Measure & inspect → Collaborate & share**.
  - Capture: "Capture RGB, thermal, or multispectral images with any camera or drone and import them to PIX4Dmapper."
  - Digitize: "PIX4Dmapper's photogrammetry algorithms transform your ground or aerial images in digital maps and 3D models. Seamlessly process your projects on your desktop ... or bundle with PIX4Dcloud for online processing."
  - Control: "Use the power of photogrammetry in the rayCloud environment to assess, control and improve the quality of your projects. Use the quality report to examine a preview of the generated results, calibration details, and many more project quality indicators." rayCloud described as "a unique environment connecting your original images to each point of the 3D reconstruction to visually verify and improve the accuracy".
  - Measure & inspect: "Accurately measure distances, areas, and volumes."
  - Collaborate & share: "Selectively and securely share project data and insights ... using standard file formats."
- Project control: "Define an area of interest, select processing options, add ground control points or edit point clouds, DSMs, meshes, and orthomosaics." "Use default templates for automatic processing of your projects, or create your own with custom settings."
- Input breadth, vendor's own slogan: "Any camera. Any drone. Any imagery. As long as it's a .jpg or a .tif." — RGB, multispectral, thermal, fisheye, 360° camera images, camera rigs, videos.
- Output/deliverable breadth (with formats): full-color point cloud (.las, .laz, .ply, .xyz); orthomosaic (GeoTIFF, .kml); DSM (GeoTIFF, .xyz, .las, .laz); 3D textured mesh (.ply, .fbx, .dxf, .obj, .pdf); index map (GeoTIFF, .shp); thermal maps (GeoTIFF).
- Additional documented machinery: automatic point cloud classification (machine-learning assisted); flatten/smoothen digital surfaces; detailed quality report; GCPs.
- Ecosystem descriptions from the documentation portal:
  - PIX4Dmatic — "optimized for accurate and fast photogrammetric processing for large scale, corridor and terrestrial projects" (next-generation, thousand-plus-image posture).
  - PIX4Dcatch — "Turn your mobile device into a professional 3D scanner using the power of photogrammetry" (mobile terrestrial capture feeding the same engine family; RTK/LiDAR accessories marketed alongside).
  - PIX4Dsurvey — "bridges the gap between photogrammetry and CAD and allows you to seamlessly import PIX4Dmapper and PIX4Dmatic projects" (a dedicated post-processing handoff product — evidence that the reconstruction app's job ENDS at deliverable handoff).
  - PIX4Dengine SDK — "The fully customizable photogrammetry reconstruction engine. PIX4Dengine SDK runs on your infrastructure" (the same reconstruction capability sold as an embeddable engine).
  - PIX4Dcloud — "The online platform for ground and drone mapping, progress tracking, and site documentation."
- Gaussian splatting is arriving in PIX4Dmatic per the vendor's own homepage banner (representation-level extension, not a replacement of the pipeline).
- The vendor also publishes an "Open Photogrammetry Format" (OPF) page (nav reference only; not fetched).
- Accuracy claims ("sub-centimetre", "1–2 pixel GSD") appear in marketing copy — recorded here as vendor claims, deliberately NOT carried into the canonical document.

### Polycam

Key observations (evidence layer A):

- Positioning: "AI 3D Scanning, Floor Plans & Reality Capture for Teams" — a multi-mode capture app of which photogrammetry is one mode family among several (Spatial/LiDAR capture, Virtual Walkthrough, Object Capture, AI Capture, Floor Plans, Drone/Aerial).
- Object Capture page (the photogrammetry mode):
  - "True 3D Photography — capture true-to-life detail, simply by **walking around a subject at different angles**, all with the phone in your pocket."
  - "**Cloud-based photogrammetry pipeline**. Scanning an object to create a 3D model of it requires only a compatible smartphone — no need for expensive equipment."
  - "Unmatched export compatibility — bring your Object captures into any 3D design software."
  - Captures collect in a library; "sync your captures to share them with friends or colleagues, and with comments and annotations" — a library/sharing posture foreign to the desktop poles.
- Free photogrammetry tool FAQ (operational detail, Tier 1):
  - "upload your images to create a 3D model with photogrammetry. We recommend using a **minimum of 20 images** or a video that's at least 20 seconds" (product-specific recommendation).
  - "choose a subject that has lots of **surface detail and texture**" (documented capture rule).
  - Models "automatically saved in your Polycam account. From within your account, you can edit your models, and **export in 12+ formats** to popular software such as Blender, SketchUp, Unreal, Unity, and more. You can also **share your models** ... by sending them a link."
  - Drone photogrammetry: "upload your keyframed drone images to this tool and you'll get a capture back in minutes."
  - XL Photogrammetry (interiors): >250 constituent images gated to a paid tier; documented multi-pass interior capture technique with "at least a 30% overlap between frames, but preferably 50%"; explicit comparison "Why use Photogrammetry over LiDAR to capture interiors?" — photogrammetry for photo-realistic detail vs LiDAR for quick geometry.
  - The vendor's own general definition: "Photogrammetry is a technology that captures precise three-dimensional measurements and visual representations of objects, terrain, or structures using photographs. It relies on advanced software to analyze multiple images taken from different angles, enabling accurate reconstruction and measurement of the subject."
- Boundary evidence inside one vendor: Polycam lists "AI 3D model generator — Generate a 3D Model from a 2D image!" as a **separate tool** from its "Photogrammetry Tool" — the market itself separates generative image-to-3D from multi-view photogrammetry. Gaussian splatting and LiDAR scanning are likewise separate modes/tools.
- Industries marketed: AEC, real estate, forensics/law enforcement, product design, 3D/VFX, facilities — the prosumer/professional bridge tier.

## Cross-product Comparison

| Dimension | Agisoft Metashape | RealityScan (Epic) | Pix4D ecosystem | Polycam |
|---|---|---|---|---|
| Primary input | aerial nadir/oblique, close-range, satellite, scanned film w/ fiducials, fisheye/spherical cameras | photos of real scenes (documented via camera-geometry import/estimation) | any camera/drone; RGB/multispectral/thermal/fisheye/360°/rig/video (.jpg/.tif) | phone walk-around photos/video, drone frames, uploaded image sets |
| Reconstruction act (documented vocabulary) | "photogrammetric triangulation" + dense cloud | "import, estimate, and export camera geometry" | "photogrammetry algorithms transform ... images in digital maps and 3D models" | "software to analyze multiple images taken from different angles, enabling accurate reconstruction and measurement" |
| Intermediate results | dense point cloud (editable/classifiable) | point clouds / projects ("creations") | point clouds, DSMs, meshes (editable) | capture objects in account library (editable) |
| Final results | 3D textured model, DEM (DSM/DTM), georeferenced orthomosaic, tiled models | 3D assets ("creations") for entertainment pipelines, camera geometry exports | point cloud, orthomosaic, DSM, 3D textured mesh, index/thermal maps | 3D model in library; exports to design/game software |
| Scale / georeference | GCP import + target auto-detection; scale bar tool; EXIF/flight log; EPSG; geoid datums | camera-geometry import/export; coordinate-system conventions documented | GCPs; georeferenced map outputs | geotagged drone inputs; consumer tier largely relative (not documented) |
| Quality/verification | accuracy control via GCPs; ghosting filter | paRSer reporting system; XMP sidecars | quality report; rayCloud image↔point verification | guided capture technique; overlap advice |
| Measurement | distances, areas, volumes; stereo vectorization | (not fetched in detail) | distances, areas, volumes | measurement surfaces in app (documented via product pages) |
| Processing substrate | local desktop; network distributed; optional cloud | local workstation (GPU); Linux; CLI | desktop; cloud (PIX4Dcloud); on-prem SDK | smartphone capture + cloud pipeline |
| Delivery/export | "direct upload to various online resources and export to many popular formats" | exports documented via CLI/XMP; engine-adjacent | standard formats (.las/.ply/.obj/.fbx/GeoTIFF/...) | "export in 12+ formats"; share links |
| Automation | batch, Python/Java API, network processing | CLI, paRSer, REST/gRPC remote command | templates; SDK | one-tap modes |
| Adjacent modes bundled | LiDAR import/registration, panorama, 4D rigs, multispectral | Unreal-ecosystem integration posture | mobile capture (catch), CAD bridge (survey), agriculture (fields), public safety (react) | LiDAR mode, floor plans, AI capture, splat tool — photogrammetry kept distinct |
| Customer tier | professional generalist | studio/entertainment professional | geospatial professional | consumer/prosumer/teams |

Cross-product commonalities (evidence layer B): every sampled product (1) ingests a multi-view photograph set of a real subject, (2) computes alignment/poses + geometry from image correspondence, (3) materializes the result as 3D data held in a project/capture, (4) delivers it outward in interchange formats (or via upload/share), and (5) exposes quality-control surfaces connecting images to the reconstruction. All four also bundle adjacent capture modes or hybrid inputs (LiDAR, multispectral, floor plans, rigs) while keeping the photo-reconstruction pipeline distinct.

## L0 / L1 / L2 / L3

### L0 — Defining Invariant (deliberately minimal)

Three jointly-held structures:

1. **Multi-view photograph set of a real subject as the input of record.** The photos are the measurement source — an existing object, scene, structure, or terrain photographed from multiple viewpoints. Remove it → 3D Modeling / Sculpting (geometry authored, nothing photographed).
2. **Computed spatial reconstruction from inter-image correspondence.** The application derives the cameras' spatial relationships and the subject's 3D geometry by relating what the overlapping images share — whether by manual marking (older form) or automated matching (modern form). The geometry is *measured*, not authored and not imagined. Remove it → an image viewer / a generative image-to-3D tool.
3. **The reconstruction as a usable 3D deliverable.** The computed geometry is materialized as reviewable 3D data (point cloud, mesh, textured model, or derived surface such as a terrain model or orthomosaic) and handed off — exported in interchange formats, uploaded, or shared — for use in other software. Remove it → a measurement/pose calculation demo with no product deliverable.

Joint-held is load-bearing: 1 alone = photo library; 2 alone = algorithm demo; 3 without 1+2 = generic 3D file converter/viewer; 1+3 without 2 = AI image-to-3D generator territory; 1+2 without 3 = calculation tool, not this application Type.

### L1 — Common Mature Structure (present across the sample, not definitional)

- staged processing pipeline (align/triangulate → dense reconstruction → mesh/texturing or map surfaces)
- dense point cloud as an intermediate, editable, classifiable result
- mesh generation and texturing
- scale/position control (scale bars, control points/marks, geotag/flight-log ingestion, coordinate systems) — ubiquitous in professional products, optional in consumer tiers
- quality/verification surfaces (quality reports; image↔point linkage; residuals)
- measurement tools (distances, areas, volumes)
- project/capture container binding photos + settings + results
- broad export formats; direct upload/share in several products
- automation range from one-click templates to scriptable pipelines
- hybrid inputs (LiDAR scan import/registration; video frames; rigs) in professional products

### L2 — Variant / Optional Structure

- market poles: survey/mapping (orthomosaics, DSM/DTM, classification, index/thermal maps, corridor mapping) vs creative/entertainment (photoreal textures, UDIM/HDR, 4D rigs, engine handoff) vs consumer/prosumer (mobile capture, library, sharing)
- capture substrate: drone frames, DSLR ring/tabletop, phone walk-around, video, 360° cameras, scanned film with fiducial marks, satellite imagery (with RPC)
- processing substrate: offline desktop, distributed network, cloud service, hybrid, embeddable SDK
- representation: mesh+texture vs point cloud vs DEM/ortho surfaces vs **Gaussian splatting** (emerging; documented in 2/4 vendors' current marketing)
- georeferencing depth: none → scale bar → GCP survey-grade with datums
- edition/packaging: edition splits, free web tools, app-plus-cloud bundles

### L3 — Vendor-specific (research notes only)

- Agisoft: Standard/Professional edition split; Agisoft Cloud site-inspection platform; powerline detection; Cesium publishing; network processing nodes; geoid grid downloads.
- Epic/RealityScan: Epic Games Launcher distribution + account; paRSer templating language; Remote Command Plugin (REST/gRPC); XMP sidecar specifics; Linux build; engine-ecosystem adjacency.
- Pix4D: rayCloud environment; quality-report specifics; PIX4Dcatch+RTK hardware line; PIX4Dsurvey CAD bridge as separate product; PIX4Dengine SDK; OPF; "sub-centimetre"/GSD marketing accuracy claims (not carried into canonical doc).
- Polycam: XL Photogrammetry image-count tiers (250+ images gated); documented 30%/50% overlap and 20-image minimum recommendations; comments/annotations on captures; Xactimate exports; floor-plan and AI-capture modes; "trusted by half of the Fortune 500" marketing.

## Vendor-specific Findings

See L3. Additionally: only Pix4D documents a *separate downstream product* (PIX4Dsurvey) dedicated to bridging into CAD; only Polycam documents consumer-tier numeric capture recommendations; only Epic documents a templating/reporting language for project introspection. None of these generalize.

## Boundary Findings

1. **vs 3D Modeling Application / Digital Sculpting Application (§04.13 siblings)** — modeling/sculpting author geometry that never existed as measured reality; photogrammetry's geometry is computed from photographs of an existing subject. Remove the photograph-derived measurement → modeling. Keep separate.
2. **vs generative image-to-3D (AI generators; no dedicated leaf in this directory)** — generative tools *imagine* a 3D model from one/few images (or text); photogrammetry *measures* geometry from correspondence across multiple views. Market evidence: Polycam itself lists "AI 3D model generator" (from a 2D image) as a separate tool from its photogrammetry tool. Boundary = correspondence-based measurement vs generation. (No directory conflict; recorded for future taxonomy passes if an AI-3D leaf is added.)
3. **vs laser/depth-sensor scanning (3D scanner apps; point-cloud registration ecosystems; no dedicated leaf)** — scanning measures depth directly with a sensor; photogrammetry derives geometry from image correspondence. Many products fuse both (Metashape imports/aligns laser scans; Polycam ships LiDAR and photo modes side by side; PIX4Dcatch pairs phone LiDAR/RTK with photogrammetry). The photo-correspondence pipeline is this Type's defining act; scan processing remains adjacent tooling (consistent with the construction-reality-capture pass's note that "reality capture" as a market label also covers scan-registration ecosystems).
4. **vs Construction Reality Capture Platform (§17, processed 2026-09-07) — PRE-HUNG FLAG DISCHARGED.** That pass recorded: "vs Photogrammetry Application (§04.13, unprocessed — general 3D-from-photos creation vs construction-scoped record system; photogrammetry appears inside this Type as one processing mechanism; joint review recommended)". This pass ratifies keep-both: the CRC's defining core is the construction project's visual-history record system (project container + dated capture sessions + spatial anchoring + chronological accumulation + hosted access), which may *use* photogrammetric processing as one internal mechanism; the Photogrammetry Application's defining core is the reconstruction pipeline and its deliverables, with no construction-record semantics (no project-as-construction-site container, no progress/closeout workflow). Seam = record system vs reconstruction mechanism. Remove the reconstruction pipeline → CRC remains; remove the construction record semantics → this Type remains.
5. **vs Photo Editor (§04.04)** — pixel-level 2D edits on individual images vs 3D reconstruction across a set of images. Completely different object world.
6. **vs GIS / mapping platforms and Digital Twin Platforms** — consumers of photogrammetric deliverables (Metashape's own positioning says outputs are "to be used in GIS applications"). Photogrammetry produces the 3D data; GIS/twin platforms store, analyze, and serve it.
7. **vs 3D Rendering Application (§04.14)** — inverse directions: rendering derives 2D images from existing 3D; photogrammetry derives 3D from existing 2D images.
8. **vs Texture / Material Authoring (§04.14)** — photogrammetry *captures* texture from photos as part of reconstruction; texture authoring *paints/generates* appearance for existing models.
9. **Gaussian splatting capture** — same input contract (multi-view photos of a real subject) and same reconstruction intent with a different result representation. Held as an emerging representation variant at the Type's periphery, not a separate Type (documented inside PIX4Dmatic's roadmap banner and Polycam's tool set; both vendors keep it beside — not instead of — mesh/point-cloud photogrammetry).
10. **Drone flight-planning applications** — orchestrate capture missions; reconstruction is the separate processing act. Some vendors bundle flight apps and reconstruction (Pix4D ecosystem sells capture apps, hardware, and engines), but bundling is packaging, not Type identity.

## Historical / Market-Sample Check (§24)

- **Analog/stereo-plotter photogrammetry (20th century aerial survey)**: photographs (stereo pairs) of real terrain → operator measures correspondences on the plotter → computed 3D positions/terrain surfaces → map/orthophoto deliverables. Fits all three L0 legs with zero automation, no dense clouds, no GPUs, no cloud. (Conceptual — not web-verified this pass.)
- **1990s/2000s manual-marking desktop photogrammetry (PhotoModeler-class, close-range)**: photos of an object → user marks corresponding points across images → software solves poses and 3D coordinates → export to CAD. Fits all three legs. (Conceptual — product site not fetched; classification cautious.)
- **Early 2010s research SfM tools (Bundler/VisualSFM-era)**: photos → automated alignment → sparse/dense point cloud → export. Fits without texturing, georeferencing, or GUI polish. (Conceptual.)
- Modern additions (drone-first, mobile cloud, splatting, satellite, multispectral) all sit inside the same three legs. Conclusion: L0 is not overfit to the current automated/drone/mobile market; the manual/analog lineage passes the test, so no further abstraction is required. The definition deliberately does NOT name SfM/MVS algorithms, automation, dense clouds, texturing, drones, cloud processing, or georeferencing.

## Uncertainties

- RealityScan's GUI step sequence and feature depth are evidenced only by the doc index + camera-geometry reference + install page (marketing site unreachable ×2). Assertions about it are kept at vocabulary level.
- Polycam's help-center operational detail was unreachable; numeric capture guidance used here comes from its own product/FAQ pages (marked product-specific).
- Agisoft/Pix4D accuracy figures are vendor marketing, not independently verified; excluded from the canonical document.
- OPF (Open Photogrammetry Format) referenced via nav only; not assessed.
- Gaussian-splatting maturity/positioning could shift; held as emerging variant.
- Historical/legacy products (analog workflow, PhotoModeler-class) verified conceptually, not via fetched primary sources — flagged per evidence rules.

## Final Synthesis

A Photogrammetry Application is defined by a three-part invariant: a multi-view photograph set of a real subject as the input of record; computed spatial reconstruction of camera poses and subject geometry from inter-image correspondence (manual or automated); and the reconstruction delivered as a usable, exportable 3D artifact (point cloud, mesh/textured model, or derived map surfaces). Around this core, mature products add a staged pipeline (align → dense → mesh/texture or ortho/DEM), scale/georeference control, quality-verification surfaces, measurement, and broad export; variants divide along market poles (survey/mapping vs creative/entertainment vs consumer mobile), capture substrates (drone/DSLR/phone/video/film/satellite), processing substrates (desktop/network/cloud/SDK), and result representations (mesh vs point cloud vs splats). The Type's boundary is sharp against geometry authoring (3D modeling/sculpting), against generative image-to-3D (measured vs imagined), against sensor scanning (correspondence vs direct depth), and against record systems that consume reconstructions (Construction Reality Capture Platform — flag discharged, keep-both).
