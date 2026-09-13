# Research Notes — 3D Rendering Application

## Research Goal

Understand what a 3D Rendering Application is as an Application Type: its defining core structure, its standard mature capabilities, its common variants, and its boundaries against neighboring Types (3D Modeling, 3D Animation, Texture/Material Authoring, Rendering Management, Game Engine, AI Image Generation).

## Initial Boundary

Working hypothesis before research:

- Core use: producing 2D images (stills or frame sequences) from a 3D scene — geometry with assigned materials, lit, and viewed by a camera — through a rendering process the user controls.
- Primary users: product/industrial designers, architectural visualization specialists, film/VFX lighting-lookdev artists, game artists.
- Nearest neighbors: Texture/Material Authoring Application and Rendering Management Application (siblings under 04.14); 3D Modeling (04.13), 3D Animation (04.08), Photogrammetry (04.13); Game Engine (12); AI Image Generator (04.20).
- Likely boundary logic: modeling delivers the model; animation delivers authored motion; material authoring delivers material/texture assets; rendering delivers the final image.
- Known tension going in: most production renderers ship as plugins/engines inside host DCC/CAD applications rather than standalone products; a definitional overfit to "standalone app" would be wrong.
- Unknowns: whether an interactive viewport is defining (command-line renderers historically lacked one); where realtime rendering (archviz tools) sits relative to offline production rendering; whether motion output (turntables, camera paths) pulls the Type toward 3D Animation.

## Research Questions

1. What is the minimal input the render consumes? (scene, materials, lights, camera — in what form?)
2. What does the user configure for a render? (resolution, quality/sampling, output format, passes)
3. What is the typical workflow from model to final image?
4. Which interaction surfaces exist? (viewport/preview, material/lighting editors, render settings, render result window, output/export)
5. Which behaviors matter? (preview vs final render, time/quality trade-off, scene source variations, motion output limits)
6. How do products differ in packaging (standalone vs host plugin vs bundled engine), technology (path tracing vs realtime), and market focus (product design, archviz, film/VFX, game art)?
7. Where are the boundaries with material authoring, render-farm management, animation, game engines, and AI image generation?
8. Historical check: do 1990s-era renderers (no viewport, no libraries, no GPU) satisfy the definition?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Philosophy / tier | Evidence access |
|---|---|---|
| Blender (Cycles / EEVEE / FreeStyle) | free/open-source 3D creation suite with rendering as a feature area; multiple engines (production path tracer, real-time, NPR) | Tier 2 (blender.org rendering features page; manual was 403 in a prior sibling research pass, not retried) |
| Chaos V-Ray | industry-standard photorealistic production renderer; delivered inside host DCC/CAD applications; film/arch/product tiers | Tier 2 (chaos.com V-Ray product page); docs.chaos.com timed out twice → abandoned |
| KeyShot | standalone real-time rendering application built for product design/CAD teams; WYSIWYG viewport philosophy | Tier 2 (keyshot.com product page, support portal, manual index); manual article pages not fetched |
| Lumion | real-time architectural visualization renderer for architects; CAD/BIM live-link model; Build/Photo/Movie/Panorama mode structure | Tier 1-2 (lumion.com product page + support knowledge-base section structure; KB article bodies not individually fetched) |
| Marmoset Toolbag | game-art lookdev/presentation suite: bake, texture, render; ray-traced + raster renderers | Tier 2 (marmoset.co product page); docs URL 404 |
| POV-Ray (historical anchor) | free raytracer dating to 1991 (DKBTrace lineage); scene description language + command-line/INI rendering; no modern viewport tooling | Tier 1 (povray.org + wiki.povray.org full documentation TOC) |

## Sources

Research date: 2026-09-06

- Blender — https://www.blender.org/features/rendering/ (fetched)
- Chaos V-Ray — https://www.chaos.com/vray (fetched)
- KeyShot — https://www.keyshot.com/what-is-keyshot/ (fetched; resolves to KeyShot Studio product page)
- KeyShot — https://help.keyshot.com/ (fetched; support portal hub)
- KeyShot — https://manual.keyshot.com/ (fetched; manual index: KeyShot Studio 2026 / VR / Network Rendering / Plugin manuals)
- Lumion — https://lumion.com/ (fetched)
- Lumion — https://support.lumion.com/hc/en-us (fetched)
- Lumion — https://support.lumion.com/knowledge-base/movie-photo-mode-questions (fetched; section article lists)
- Lumion — https://support.lumion.com/knowledge-base/rendering-questions (fetched; section article lists)
- Marmoset Toolbag — https://marmoset.co/toolbag/ (fetched)
- POV-Ray — https://www.povray.org/ (fetched)
- POV-Ray — https://wiki.povray.org/content/Documentation:Contents (fetched; full documentation TOC)

Source-access limitations:

- docs.chaos.com (V-Ray Tier 1 manual) timed out twice → abandoned per retry rule. V-Ray evidence is Tier 2 (product page): sufficient for positioning, capability inventory, and packaging model; not sufficient for precise operational rules.
- KeyShot manual index was reached but individual manual articles were not fetched; KeyShot operational claims rest on the vendor product page (Tier 2) plus support/manual hub structure.
- Marmoset documentation URL 404; Toolbag evidence is the product page only.
- Lumion KB article bodies were not individually fetched; evidence is the knowledge-base section/article structure plus the product page.
- No product-specific operational claims are made beyond what fetched pages support.

## Product Observations

### Blender — Rendering feature area (evidence layer A, blender.org features page)

- Rendering is one of several feature areas of the suite (modeling, sculpting, animation & rigging, rendering, simulation, video editing, scripting, VFX…).
- Three engines presented side by side:
  - **Cycles** — "Blender's ray-trace based production render engine": unidirectional path tracing with multiple importance sampling; multi-core CPU rendering with SIMD; GPU rendering (NVIDIA CUDA/OptiX, AMD HIP, Intel OneAPI, Apple Metal); multi-GPU; unified CPU/GPU kernel.
  - **FreeStyle** — "edge- and line-based non-photorealistic (NPR) rendering engine"; draws stylized or technical line looks from mesh data.
  - **EEVEE** — real-time engine; "the gap between offline and real-time rendering is being bridged"; viewport previsualization of Cycles shading.
- Cycles capability inventory: geometry (meshes, hair curves, volumes, instancing, BVH), subdivision & displacement, shading (PBR, node-based shaders and lights, Principled BSDF, Open Shading Language), lighting (global illumination, point/sun/spot/area lights, mesh lights, environment light, sky model, light portals), interactivity ("designed for interactive updates", "tiled and progressive rendering"), layers & passes (render layers, render passes for geometry and lighting, shadow catcher, holdout mattes, denoising), camera & effects (perspective/orthographic, panoramic/fisheye, stereoscopic, depth of field with anamorphic bokeh), motion blur (cameras, object transforms, meshes/hair), volumes (absorption/scattering/emission, smoke/fire, SSS), textures (image, environment maps, procedural, bump/normal).
- Vendor framing: "Blender comes with a powerful unbiased rendering engine that offers stunning ultra-realistic rendering" — marketing language, but the structural inventory is explicit and feature-complete.

### Chaos V-Ray (evidence layer A for chaos.com product page; manual inaccessible)

- Positioning: "Industry-standard photorealistic rendering", "Award-winning 3D rendering technology with AI capabilities"; Emmy and Academy Award citations; "Trusted by the world's leading architecture, VFX, and design studios."
- Packaging: "Available in Revit / SketchUp / Rhino / 3ds Max / Cinema 4D / Blender" — the renderer is delivered inside host applications. FAQ asks "do I need a separate 3D software to use it?" — confirming host-integration as the default model. "Create your scene once and render it anywhere—zero rebuilding."
- Capability claims: physically based rendering "for true-to-life stills and animations"; "Realistic lighting, materials, atmospheric effects, and cameras"; asset library; advanced scattering; built-in post-processing.
- Execution: "Select CPU, GPU, or hybrid mode"; "Speed up production rendering with multiple machines."
- Real-time + offline: "Real-time rendering at final-frame quality, directly in the V-Ray viewport"; "100% real-time ray tracing, no rasterizations or approximations"; "Real-time and offline rendering in one production-proven workflow."
- Vendor-stated workflow stages: Concept → Lighting & materials → Rendering & output → Delivery & collaboration. Under Rendering & output: Sun & Sky systems, procedural clouds, global illumination, materials.
- Ecosystem: Chaos Vantage ("Instantly explore your V-Ray 3D scenes in fully ray-traced real-time without conversion overhead"); Chaos Cloud ("Cloud Rendering" in tiers); "Find a render farm" in the buy menu; Veras AI (ideation); AI material generation from photos; still-to-animation AI feature.
- Tiering bundles: Solo / Premium / Collection; Collection adds "Real-time viewport rendering via Vantage" and cloud rendering/collaboration.

### KeyShot (evidence layer A for keyshot.com product page + support/manual hub structure)

- Positioning: "3D visualization software. From CAD to Anything." Explicit anti-film/arch positioning: "Most rendering tools weren't built for product design… KeyShot Studio was built from day one for teams working with physical products and CAD data."
- Scene intake: 34 native 3D file formats claimed, 14 CAD plugins; "Import your file. Start rendering immediately. No conversion, no workarounds."
- LiveLinking: "bridges your CAD software and KeyShot, letting you refine your model and sync changes with a click, while keeping your views, materials, textures, and animations intact."
- WYSIWYG philosophy: "Real-Time Ray Tracing — What you see in the viewport is what you get in the final visual. No test renders, no surprises." "Every change updates instantly in the viewport."
- Execution: "Render on CPU, GPU, or both"; hardware-accelerated ray tracing.
- Appearance authoring: "Drag-and-Drop Materials — go from bare geometry to client-ready materials in seconds"; material graph with procedural texturing; partner-certified libraries (Pantone, RAL, Mold-Tech, Sorensen, Coloro, INTERPON, Axalta); physically based rendering "based on scientific research in global illumination."
- Lighting: "physical lights or KeyShot's patented HDRI editor"; light layers & advanced lighting control; AI denoise "for dramatically faster renders"; caustics & global illumination.
- Motion: "One-Click Animations — turntables, exploded views, and colorway transitions ready in minutes" (presentation-level motion primitives).
- Output/pipeline features in the buy list: Cryptomatte & OpenPBR "for pro pipelines".
- Product family structure: KeyShot Studio, KeyShot Studio VR, KeyShot Studio Web, KeyShot DAM, **Cloud Rendering**, **Network Rendering** (both separate products), Education tier, Studio Plugins.
- Manual index: KeyShot Studio 2026 Manual, KeyShot Studio VR Manual, **KeyShot Network Rendering Manual**, KeyShot Studio Plugin Manual — network rendering and plugins are documented as separate manuals/products.

### Lumion (evidence layer A/B: product page + knowledge-base structure)

- Positioning: "Industry-Leading 3D Rendering Software For Architects"; "Turn your CAD or BIM model into a place people can see, understand, and respond to. Shape context, materials, lighting, and atmosphere…"
- Intake: LiveSync plugins keep CAD/BIM model and visualization in sync (SketchUp, Revit, ArchiCAD, Rhino, AutoCAD, Allplan, Vectorworks, BricsCAD, 3ds Max, FormIt); "Model and render in perfect sync… Real-time rendering."
- Scene staging: context/entourage — "Shape your scene with 10,000+ high-quality assets, materials, lighting, and effects. Add terrain, nature, entourage, and atmosphere"; "Build custom FX stacks or layer up from preset styles. Choose diagram clarity for reviews or high-detail realism for presentations."
- Outputs: "high-resolution images and videos to immersive 360° panoramas for VR walkthroughs, reviews, approvals, and presentations."
- Knowledge-base structure (operational model):
  - **Build Mode**: landscape/terrains, OpenStreetMap, "Lighting: Sun and Artificial Lights", library content (versioned).
  - **Movie & Photo Mode**: Photo Mode ("How can you render all Photos in one go?"), Movie Mode (clips vs entire movie, camera paths/keyframes, render two clip sets to a single MP4), Animation in Movie Mode (construction process, walkthrough at eye level, animate sun/door/clouds, 360 turntable), Effects in Photo or Movie Mode (Custom Styles, Ray Tracing Effect, Raytraced Volumetrics Fog, Color Correction, save/load effects), Reflections (SpeedRay, planar, projected).
  - **Material Questions**, **Rendering Questions**: "Introduction to Ray Trace rendering in Lumion" (ray tracing introduced with Lumion 2023), "What does the Output Quality setting mean in Movie and 360 Panorama Modes?", resolutions for Ray Trace rendering in Photo Mode, "render images at a higher resolution than Poster renderings", DPI/PPI adjustment, "render a Clip or Movie as an Image Sequence", stereoscopic 3D video, "Is 'render farm' or 'render node' functionality available in Lumion?", "How does background rendering work in Lumion?", reducing rendering times.
  - **Panorama Mode** (360° rendering), File & Backup (saving projects).
- Lumion Cloud: review/comment/version-compare; AI tools (enhance/upscale images, generate PBR material maps from references) — AI positioned as post-production aid: "AI works from what you've already created."

### Marmoset Toolbag (evidence layer A, marmoset.co product page)

- Positioning: "Bake, texture, and render show-stopping 3D artwork in one software" — game-art production suite; "all-in-one creative software package for 3D artists" for "games, film, product viz, and beyond."
- Renderers: "physically-accurate ray-traced and raster renderers."
- Feature areas: Edit (setup), Bake (texture baking), Texture (painting, Texture Projects), **Render** ("Create breathtaking renders with speed using Toolbag's advanced rendering solutions"), Library (materials/textures/brushes), Viewer ("Export, upload, and share interactive Toolbag scenes using our WebGL-powered Marmoset Viewer").
- User framing: "a tool between a modeling package and a game engine… test and validate PBR assets… I use it exclusively to render my personal artwork"; "rendering assets just like I would in a photography setting" (camera system).

### POV-Ray — historical anchor (evidence layer A, Tier 1 documentation TOC)

- Homepage: "The Persistence of Vision Raytracer is a high-quality, Free Software tool for creating stunning three-dimensional graphics"; first beta July 1991; descended from DKBTrace (David K. Buck).
- Documentation structure confirms the historical shape of the Type:
  - **Scene Description Language (SDL)**: scenes are text files; tutorial "Our First Image" walks through adding a camera → describing an object → adding texture → defining a light source.
  - Scene contents: primitives (box, cone, cylinder, plane, torus, sphere…), CSG (union/intersection/difference/merge), mesh/mesh2/polygon, spline shapes (lathe, prism…), isosurface/height field; textures (pigment, normal, finish), layered textures, UV mapping.
  - **Camera**: location/look-at, projection types (perspective, orthographic, fisheye, ultra-wide, omnimax, panoramic, cylindrical, spherical), focal blur, aspect ratio.
  - **Lighting**: point, spotlight, cylindrical, parallel, area lights; radiosity; photon mapping; light fading.
  - **Atmosphere/media**: fog, sky sphere, rainbow, media (emission/absorption/scattering), interior (refraction/dispersion).
  - **Render invocation & options**: command-line switches and INI files; height/width of output; output file type/name; quality settings; anti-aliasing options; render block/pattern; gamma handling; animation via a clock variable with frame subsets and INI animation options.
  - **GUI shells** (Windows/Unix): internal text editor + **Render Window** + Render menu (start/stop rendering, file queue, render priority, thread count, "on completion" actions, benchmark); "mosaic preview" display option.
- Interpretation for the historical check: a 1991-era renderer has scene + camera + lights + textures + quality/output settings + image output, with **no modeling viewport, no material library, no PBR material graph, no GPU acceleration, no denoising** — yet it is unmistakably the same Application Type.

## Cross-product Comparison

| Structure / capability | Blender (Cycles/EEVEE) | V-Ray | KeyShot | Lumion | Marmoset | POV-Ray | Verdict |
|---|---|---|---|---|---|---|---|
| Render computation: 3D scene → 2D image | yes | yes | yes | yes | yes | yes | **Core (all)** |
| Scene with defined appearance (materials/textures) | yes (shading) | yes | yes | yes | yes | yes (SDL) | **Core (all)** |
| Lighting as part of the scene | yes (GI, env, light types) | yes (Sun & Sky, GI) | yes (HDRI, physical lights) | yes (sun + artificial) | yes | yes (5+ light types) | **Core (all)** |
| Camera defines the rendered view | yes | yes | yes | yes (camera views/keyframes) | yes | yes | **Core (all)** |
| User-set render parameters (resolution/quality/output format) | yes | yes | yes | yes (output quality, resolutions, DPI) | yes | yes (W/H, quality, file type) | **Core (all)** |
| Rendered image(s) as deliverable, exported as files | yes | yes | yes | yes (stills, MP4, image sequence, panoramas) | yes | yes | **Core (all)** |
| Interactive/progressive preview viewport | yes (interactive updates, EEVEE) | yes (real-time viewport) | yes (WYSIWYG core claim) | yes (real-time by design) | yes (real-time) | **no** (editor + render window; mosaic preview only) | Common modern; **not defining** |
| Scene hosting/appearance assignment inside the product | yes (full suite) | limited (scene lives in host app) | yes (import + assign) | yes (Build mode) | yes | text editor only | Common; varies in degree — **not defining** |
| Material/lighting authoring tools beyond assignment | yes (node shaders, OSL) | yes | yes (graph, libraries) | yes (materials, effects) | yes (texture projects) | yes (SDL authoring) | Common — **not defining** |
| Motion output (turntables, camera paths, frame sequences) | yes (motion blur; animation in suite) | stills + animations | one-click turntables/exploded views | Movie mode + animation effects | camera/animation | clock-variable frames | Common — **not defining** |
| CPU/GPU execution modes | yes | yes (CPU/GPU/hybrid) | yes (CPU/GPU/both) | GPU real-time | yes | CPU-era | Common modern — not defining |
| Render passes/AOVs & post effects | yes (layers, passes, denoising) | yes (post-processing) | Cryptomatte | FX stacks | yes | no | Common modern — optional |
| Denoising | yes | (claimed AI era) | AI denoise | (ray tracing era) | — | no | Common modern — optional |
| Distributed/cloud rendering | (Flamenco project exists on site) | yes (cloud, farm ecosystem) | separate Network Rendering/Cloud products | farm/node question addressed in KB | no | no | Optional — boundary with Rendering Management |
| Asset/material libraries | — | yes | yes | yes | yes | include files (.inc) | Common modern — optional |
| NPR / non-photoreal output | yes (FreeStyle) | — | — | diagram/styles, outline looks | — | — | Optional |
| Packaging: standalone vs plugin vs bundled | bundled engine in suite | plugin inside hosts (+ ecosystem) | standalone | standalone (+CAD plugins) | standalone | standalone (CLI/GUI shell) | **Variant (L2)** — every packaging form exists |

## Abstraction

### Level 0 — Defining Invariant

```text
3D Scene with defined appearance (surfaces carry materials/textures; scene is lit)
└── Camera defining the view to render
    └── User-invoked render process under user-set parameters
        (resolution, quality, output format)
        └── Rendered 2D image(s) as the deliverable
```

Five properties. Removing any one ends the Type:

- **Scene with defined appearance** — the input is a 3D scene whose surfaces have materials/textures and which is lit. Without appearance/lighting to resolve, it is geometry tooling, not rendering.
- **Camera as the rendered view** — the image is defined by a viewpoint (and its projection/lens parameters). Without a defined view there is no image.
- **User-invoked render process** — the image is *computed* by a rendering process the user triggers (render command, render button, queued job). Without it, the product is a viewer or modeler.
- **User-set render parameters** — resolution, quality, output format are under user control. Without these the product is a fixed camera, not a rendering tool.
- **Rendered image as deliverable** — the output is the image (still, sequence, panorama), not a scene file. If the primary deliverable is the model → 3D Modeling; if authored motion → 3D Animation; if material assets → Texture/Material Authoring.

Historical check (older / differently positioned products): POV-Ray (1991, SDL text scenes, command-line/INI rendering, no viewport/libraries/PBR/GPU) satisfies all five. Therefore none of the following may enter the definition: interactive viewport, material libraries, denoising, GPU acceleration, physically based shading, real-time preview, scene hosting, asset libraries.

### Level 1 — Common Mature Structure

Present in essentially all modern products; expected by the market but not definitional:

- **Interactive render surface** — a viewport or preview that approximates the final image progressively or in real time (KeyShot's WYSIWYG claim; V-Ray's real-time viewport; Blender's interactive Cycles/EEVEE; Lumion's real-time design surface; Marmoset's real-time renderers).
- **Appearance authoring** — material editors/graphs, texture handling, material/asset libraries, drag-and-drop assignment.
- **Lighting tools** — environment/HDRI lighting, sun/sky systems, physical light types, light layers.
- **Camera tools** — saved views/cameras, projection and lens parameters (focal blur/DOF appears in Blender, POV-Ray, Lumion, KeyShot-style photography framing).
- **Render output controls** — resolution/aspect (portrait, poster/panorama sizes in Lumion), quality/sampling settings, output formats (stills, MP4, image sequences, panoramas), DPI for print-oriented output.
- **Render result handling** — a render result surface with the computed image; passes/channels (AOVs, Cryptomatte) and post effects in production-oriented products.
- **Denoising** and progressive refinement in sampling-based renderers.
- **CPU and GPU execution**, with hardware-accelerated ray tracing in modern products.
- **Motion output** — turntables, camera-path movies, frame sequences, sun/object animation as presentation-level primitives.
- **Scene persistence** — scenes/projects saved as documents (Blender .blend-style project, Lumion project save, POV-Ray .pov/.ini files, KeyShot scene files).

### Level 2 — Variant / Optional Structure

Depends on packaging, market, era, deployment:

- **Packaging** — standalone rendering application (KeyShot, Lumion, Marmoset, POV-Ray); rendering engine delivered as plugin/extension inside host DCC/CAD applications (V-Ray; KeyShot also ships a Plugin Manual; Lumion ships CAD LiveSync plugins); rendering engine bundled inside a 3D creation suite (Blender's Cycles/EEVEE/FreeStyle).
- **Rendering technology posture** — offline production path tracing (Cycles, V-Ray), real-time ray tracing (V-Ray viewport, KeyShot, Lumion ray tracing), rasterization/real-time (EEVEE, Marmoset raster mode, Lumion), hybrid ray-traced + raster (Marmoset), NPR/line rendering (FreeStyle, diagram styles).
- **Market focus** — product design/industrial (KeyShot: CAD import, certified color/material libraries); architecture/visualization (Lumion: BIM/CAD live sync, context assets, panorama/VR output); film/VFX production (V-Ray: host pipelines, passes, farm scaling); game art (Marmoset: bake/texture/render for PBR assets).
- **Scene intake** — import file formats (KeyShot's broad CAD format support; Lumion's model import guidelines), live CAD/BIM links (LiveSync/LiveLinking), host scene (V-Ray in-host), textual scene description (POV-Ray SDL).
- **Delivery extensions** — network rendering products, cloud rendering services, render-farm ecosystems, web/VR/interactive scene sharing (KeyShot Studio Web/VR, Marmoset WebGL Viewer, Lumion 360 panoramas).
- **Realism posture** — physically based rendering as the dominant modern posture, with non-photoreal/diagram output as a recognized alternative.
- **AI assistance** — image enhancement/upscale, material generation, prompt-based restyling (Lumion Cloud, KeyShot Studio AI, V-Ray/Veras) — positioned by vendors as assistance on top of scene-based rendering, not a replacement for it.

### Level 3 — Vendor-specific Structure

(Research Notes only; excluded from the final document.)

- KeyShot: LiveLinking, patented HDRI editor, partner-certified libraries (Pantone/RAL/Mold-Tech/Coloro/INTERPON/Axalta), KeyShot Studio AI modes (Restyle/Background/Imagine/Transform/Replace), Network Rendering / Cloud Rendering / Studio VR / Studio Web product split, 34-formats/14-plugins counts.
- Chaos: Vantage standalone real-time explorer, Veras AI, Chaos Cloud / Chaos Credits, Chaos Scatter, V-Ray tier packaging (Solo/Premium/Collection), Emmy/Award positioning, "5B+ renders" stats.
- Lumion: Build/Photo/Movie/Panorama mode naming, LiveSync, SpeedRay/planar/projected reflections, Custom Styles, Lumion Cloud review/AI tooling, 10,000+ asset library claim, versioned library content per release.
- Marmoset: texture baking engine framing, Library asset drops, WebGL Marmoset Viewer, licensing split (individual/studio/academic).
- Blender: engine names Cycles/EEVEE/FreeStyle, Principled BSDF, Open Shading Language, shadow catcher/holdout mattes, unified CPU/GPU kernel.
- POV-Ray: SDL/INI/command-line option system, radiosity/photon settings, include-file library, Windows GUI render queue/benchmark.

## Boundary Findings

| Neighbor Type | Relationship | Distinction test (remove-what → becomes the other) |
|---|---|---|
| 3D Modeling Application (04.13) | upstream producer | If the primary job is creating/editing geometry and the deliverable is the model → 3D Modeling. Rendering apps consume models; the researched products either import them (KeyShot, Lumion), take them from a host (V-Ray), or bundle modeling as a separate suite feature area (Blender). |
| 3D Animation Application (04.08) | adjacent; overlaps on "rendered moving image" | If the core job is authoring time-varying scene state (keyframes/rigs/performance) → 3D Animation. Rendering apps' motion output in the sample is presentation-level: camera paths, turntables, sun/door/cloud effects (Lumion KB animation list; KeyShot one-click turntables). Gradient, not a wall — see Boundary Issues. |
| Texture / Material Authoring Application (04.14 sibling) | sibling; overlaps on materials | If the primary deliverable is material/texture assets (authored substance, baked maps) → Material Authoring. Rendering apps consume/assign materials to produce images. Marmoset straddles (bake+texture+render in one product) — gradient. |
| Rendering Management Application (04.14 sibling) | downstream layer | If the primary object is a queue of render jobs distributed across machines/farm/cloud → Rendering Management. Vendors themselves split it: KeyShot Network Rendering is a separate product with its own manual; Chaos sells cloud rendering separately and links to render farms; Lumion's KB treats farm/node availability as a distinct question. Remove the farm → the renderer still renders; remove the renderer → the farm still manages jobs. |
| Game Engine (12) | distant; shares real-time rendering technology | Game engines run interactive, playable experiences; rendering applications produce images. Real-time renderers (Lumion, KeyShot) adopt engine-grade technology but have no runtime/game-object model as their user-facing core. (Inference from Type definitions; no game-engine research pass this session.) |
| AI Image Generator (04.20) | adjacent in output, different in input | AI image generation has no 3D scene, no camera, no lights — prompt → image. Sampled renderers position AI strictly as assistance over existing scene work (Lumion: "AI works from what you've already created"; KeyShot AI "fits into your existing workflow"). |
| Photogrammetry Application (04.13) | upstream capture | Photogrammetry derives models from photos; rendering app consumes models to produce images. (Not directly researched this session; boundary stated as structural reasoning.) |

Taxonomy observations:

- The leaf holds as an independent Type: standalone products that people buy *as renderers* exist across four decades and four market tiers (POV-Ray, KeyShot, Lumion, Marmoset; V-Ray ecosystem).
- The dominant modern packaging (plugin/engine inside a host) must not override the definition; it is a delivery variant, not the Type.
- The siblings under 04.14 ("Texture / Material Authoring", "Rendering Management") correspond to genuinely different primary objects (material assets; render-job logistics), confirmed by vendor product splits.

## Uncertainties

- **V-Ray operational detail** is Tier 2 only (manual timed out). Claims about V-Ray's render-settings workflow specifics were not made.
- **KeyShot manual article pages** were not fetched; KeyShot workflow detail rests on the product page (Tier 2). Its WYSIWYG claim ("no test renders") is vendor marketing language and was treated as a philosophy indicator, not a literal operational guarantee.
- **Lumion KB article bodies** were not fetched (section structure only); statements about Lumion are confined to what section/article titles and the product page support.
- Whether real-time-only archviz renderers are converging toward a distinct sub-Type (scene staging + review collaboration, e.g., Lumion Cloud) is an open question; current evidence still fits the render-to-image core.
- Marmoset's rendering detail (its docs 404) is limited to positioning; it was used mainly as evidence of the bake/texture/render gradient toward Material Authoring.
- Game Engine and Photogrammetry boundaries are structural inferences, not researched passes.

## Final Synthesis

A 3D Rendering Application is defined by a small core: it takes a 3D scene whose surfaces carry materials and which is lit, framed by a camera, and computes 2D images from it through a render process the user invokes and parameterizes (resolution, quality, output format), delivering the rendered image as the product's output.

Everything else is stratified:

- What mature products add: interactive/progressive preview, appearance and lighting authoring tools, camera tools, render output controls, passes and post effects, denoising, CPU/GPU execution, presentation-level motion output, scene persistence.
- What varies by packaging/market/era: standalone app vs host plugin vs bundled engine; path tracing vs real-time vs raster vs NPR; product design vs archviz vs film/VFX vs game-art focus; scene intake by import/live-link/host/text; network/cloud delivery extensions; AI assistance.
- What stays out: render-farm/queue management (separate sibling Type), material/texture asset authoring as a primary deliverable (sibling Type), geometry authoring (modeling), motion authoring over time (animation), interactive playable runtime (game engine), prompt-based image synthesis (AI image generation).

The POV-Ray anchor proves the definition survives the removal of every modern comfort; the KeyShot/V-Ray contrast proves it survives both extreme packaging forms (fully standalone scene-hosting app vs engine living entirely inside a host); the Lumion/Marmoset/Blender spread proves the market-tier breadth.
