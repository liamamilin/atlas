# Research Notes — Texture / Material Authoring Application

## Research Goal

Understand the Application Type whose products create the **surface appearance of 3D models** — texture maps and/or material definitions — and deliver that appearance into a 3D pipeline (game engines, renderers, DCC applications). The leaf sits under §04.14 "3D Materials & Rendering" between 3D Creation (§04.13) and 3D Rendering (sibling).

Three sibling passes left boundary flags that this pass must discharge:

1. **3d-rendering-application** (sibling, §04.14): game-art suites span bake+texture+render in one product (Marmoset Toolbag named); structural test proposed = primary deliverable (material/texture assets vs rendered images); flagged for joint review here.
2. **digital-sculpting-application** (§04.13): displacement-class painting (displacement/normal-map baking, micro-vertex painting) blurs shape vs surface appearance; secondary gray zone toward this leaf.
3. **procedural-3d-creation-application / 3d-modeling-application / photogrammetry-application** (§04.13): each recorded a one-line seam (output domain; assignment-level vs authoring-level; capture vs authoring) — confirm from this side.

## Initial Boundary

Hypothesis before research:

- Core use: authoring how 3D surfaces LOOK (color, normal, roughness/metalness, height, emissive…) as reusable assets.
- Users: texture artists, lookdev/lighting artists, character/environment artists, material artists in games, film/VFX, product viz.
- Nearest neighbors: 3D Rendering (consumes materials → images), Digital Sculpting (changes shape), 3D Modeling (geometry + assignment-level materials), Raster Image Editor (flat pixels, no 3D binding), Procedural 3D Creation (same node model, 3D output), Photogrammetry (captures appearance).
- Unknowns: is the procedural-material pole (Designer-style) the same Type as the painting pole (Painter-style)? Is mesh-map baking in-type? Is the unit of record the texture set, the material, or the project? Where exactly does the rendering boundary sit?

## Research Questions

1. What is the unit of record — texture set? material? project? How do the painting pole and the procedural pole differ?
2. How is appearance bound to 3D surfaces (UV maps, UDIM tiles, texture sets, mesh objects)?
3. What is the authoring structure — layer stacks, node graphs, both? Which parts are non-destructive?
4. Which channel/map types are standard, and how are they bound to shader inputs?
5. How does delivery work — export presets, channel packing, material packages, live links?
6. What role do material/texture libraries and "smart" reusable materials play?
7. Is mesh-map baking (normal/AO/curvature from high-poly) part of this Type?
8. What does the real-time preview viewport do, and is it definitional?
9. Where are the exact boundaries vs rendering, sculpting, modeling, image editing, procedural 3D, photogrammetry?

## Representative Products

Selected for market representation + documentation quality + different product philosophies + different customer tiers:

| Product | Vendor | Pole | Customer tier | Evidence quality |
|---|---|---|---|---|
| Mari | Foundry | high-end film/VFX 3D texture painting (UDIM scale) | enterprise studios | Tier 1 (user guide) + Tier 2 (product page) — strong |
| Marmoset Toolbag | Marmoset LLC | game-art lookdev suite: bake + texture + render (straddling product) | indie → studio | Tier 2 (feature pages, detailed specs) — strong |
| ArmorPaint | Armory (open-source) | standalone GPU PBR texture painter (minimal/indie pole) | individual artists | Tier 1 (full manual) — strong |
| Quixel Mixer | Quixel (Epic) | scan-based texture mixing (Megascans) | individual/indie | retirement evidence only (product page now redirects to Megascans library) |
| Substance 3D Painter / Designer | Adobe | market-defining painting + procedural-material family | individual → enterprise | positioning-level only — Adobe domains unreachable (see Sources) |

## Sources

Research date: 2026-09-09.

Reached (Tier 1/2):

- Foundry Mari product page — https://www.foundry.com/products/mari (positioning, features, pricing tiers)
- Foundry Mari docs home — https://learn.foundry.com/mari/docs
- Mari User Guide — https://learn.foundry.com/mari/Content/user_guide/user_guide.html
- Mari User Guide: Shading Networks — https://learn.foundry.com/mari/Content/user_guide/sub_landing_page/shading_networks.html
- Mari User Guide: Channels — https://learn.foundry.com/mari/Content/user_guide/channels/channels.html
- Mari User Guide: Exporting/Importing — https://learn.foundry.com/mari/Content/online_help/importing_exporting_sessions.html
- Marmoset Toolbag product page — https://marmoset.co/toolbag/
- Marmoset Toolbag texturing page — https://marmoset.co/toolbag/texturing/ (feature + specification lists)
- ArmorPaint site — https://armorpaint.org/
- ArmorPaint manual — https://armorpaint.org/manual (full workflow documentation)
- Quixel — https://quixel.com/mixer (observed serving the Megascans library page — Mixer product page no longer present)

Not reached (source-access limitation):

- **Adobe Substance 3D Painter / Designer**: all adobe.com / helpx.adobe.com / substance3d.adobe.com / docs.substance3d.com fetch attempts timed out (6+ URLs). Third-party corroboration attempts (docs.blender.org Substance add-on page, dev.epicgames.com Substance plugin page) returned 403/empty. GitHub org guess 404.
  - Consequence: Substance claims in this research are limited to positioning-level statements corroborated by third parties (a 3DCoat vendor quote captured by the digital-sculpting pass names Substance Painter as the texturing benchmark: "the optimum golden mean between Blender, ZBrush, and Substance Painter… covers the entire cycle (sculpt → retopo → UV → PBR texturing → export)"). **No precise Substance operational details (layer types, export formats, smart-material mechanics, SBSAR behavior) are asserted from memory.**
- **InstaMAT**: instamat.io timed out twice; docs.instamat.io root reachable but content-free; subpage guesses 404. Dropped from sample.

## Product Observations

### Foundry Mari (film/VFX enterprise pole) — Evidence Layer A

Positioning (product page, directly observed):

- "Mari — Digital 3D texture painting software. From procedural to hand-painted textures and everything in between. Mari: 3D painting without limits."
- Projection Painting: "Work in 3D or 2D depending on your needs. With support for UDIM workflows, artists can work with hundreds of high-resolution texture maps, as well as easily painting a 2D image with full Node Graph or Layer support."
- Scale claims: "paint across thousands of UDIMs"; "Supports up to 32K @ 32bit per UDIM"; "thousands of textures per model via UDIMs".
- "Use Mari's powerful Bakery to bake mesh texture maps in seconds, even on the largest meshes"; "bake without leaving Mari".
- "Easily create the look you want with Mari's wide range of Smart Masks"; "Rapidly block out the look of an asset with Mari's Material System".
- "Streamlined look development with shaders… paint textures with more confidence, knowing that your art will look correct in the final render."
- Multi-channel Paint (7.5): "paint up to 8 streams at once from a single node"; Texture Transfer ("speed of texture transfers between objects… using the power of the Bakery engine").
- Pipeline: OpenColorIO, OpenSubdiv, FBX, Alembic; "Extensive API for customisation and pipeline development"; Python scripting (Python Shelf).
- Pricing tiers: team subscription, quarterly rental, individual subscription, non-commercial, education — enterprise-first.

User guide (Tier 1, directly observed):

- "A Mari project stores your work on geometries, and any associated textures." (Managing Projects)
- **Channels**: "Channels hold layers stacks, filled with paint layers, procedurals, and adjustments in your project. For example, a project might have channels for diffuse color, displacement, or specularity, but each of those channels contain individual layers for paint, masks, and filters. Channels can then be used in shader inputs so you can adjust the amount of diffuse or specularity… A single project can hold all the channel data required for the model - diffuse, dirt, specular, luminescence, displacement, and so on. Each object in a Mari project has its own set of channels."
- Channel creation: color depth + patch size set at creation; color vs scalar channels; HDR (16/32-bit) channels; bulk creation from presets "optionally importing textures into the channel at the same time".
- **Layers**: "the primary system for painting in Mari, they are the source of your paint textures in a project."
- **Shaders**: "control how Mari displays the model on the canvas under certain, user-specified lighting conditions."
- **Node Graph**: "another way of viewing and managing channels, layers, and shaders."
- Geometry organization: items, objects, **patches** (UV patches); painting across patches; geometry formats.
- Export/Import: "export and import textures… be they layer or channel texture data, or session scripts" (session scripts share projects between users).
- Previewing/rendering: preview in Modo; projectors store camera details.

Interpretation: Mari's model = project → objects → (patches/UVs) → channels (named maps) → layer stacks (paint/procedural/adjustment/masks) → shader inputs → export. Painting happens on the 3D model in the canvas; the node graph is an alternate manipulation surface over the same structures.

### Marmoset Toolbag (game-art lookdev suite; straddling product) — Evidence Layer A (feature/spec pages)

Positioning (directly observed):

- "Bake, texture, and render show-stopping 3D artwork in one software."
- "Marmoset Toolbag is the all-in-one creative software package for 3D artists… industry-leading texture baking engine, intuitive texturing & painting tools, and physically-accurate ray-traced and raster renderers."
- Feature pillars: Edit / Bake / Texture / Render / Library / Viewer (WebGL scene sharing).
- Testimonial framing: "Toolbag makes it quick and easy to test and validate PBR assets" (between modeling package and game engine).

Texturing page (directly observed, detailed):

- "Leverage intuitive texturing tools to author and paint physically accurate materials using a non-destructive layer-based workflow. Toolbag's Texture Projects delivers easy-to-use painting tools, UDIM support…"
- "Infinite Layering & Masking": unrestricted layering hierarchy; drag materials from Library to block out; stack and mask any layer type; grouping, converting, rasterizing.
- Paint in 3D: brush engine, symmetry, gradient tool, flood fill, clone stamp; brush presets from Library.
- "Texture Across Tiles": "Effortlessly manage UDIMs and Multiple Texture Sets from a single Texture Project. Paint, mask, and build smart materials that apply seamlessly over tile borders."
- Weathering: "input maps and procedural layers… auto-generated input maps"; "Smart Materials that adapt to your mesh… drop them into your layer stack"; create/save/share in Library.
- Vector layers (seams/panel lines/stitching, boolean ops); Carve Groups (height-style gradient blending); Sync Points ("masks aware of newly added details below… sync curvature, height, and AO data of all layers below").
- Layer types: Paint, Fill, Procedural (Cellular/Perlin/Voronoi/Turbulence…), Vector, Adjustment (Blur/Curves/Gradient Map/Hue-Sat/Invert/Levels/Recolor/Sharpen), Processor (Color Selection/Curvation/Direction/Dirt/Height/Occlusion/Scratch/Thickness), Group, Carve Group.
- Input map types (28 listed): Albedo, AO, Anisotropic Direction, Bump, Cavity, Curvature, Emissive, Fuzz, Glint, Gloss, Group/Material/Object/UV-island ID, Height, Metalness, Normal (+Object), Refraction Depth, Roughness, Sheen, Specular, Thickness, Transmission Mask, Transparency, Custom.
- Project settings: up to 8192²; UV padding; tangent orientation; **Metalness & Specular PBR workflows**; generation of missing input maps.
- Output settings: export by project or individual map; map-naming customization; export size multipliers; RGB/RGBA/grayscale; **custom texture packing per channel**; PNG/JPG/TGA/PSD; 8/16 bits.
- "Bake Project Live-Link" (bake results feed the texture project).

Interpretation: Toolbag's Texture Project is the same painter model as Mari/ArmorPaint (layers+masks+input maps over UV/texture sets), bundled with baking and rendering — the straddle the rendering pass flagged.

### ArmorPaint (open-source standalone painter; minimal pole) — Evidence Layer A (manual)

Positioning (directly observed):

- "ArmorPaint is a stand-alone software designed for physically-based texture painting. Drag & drop your 3D models and start painting. Receive instant visual feedback in the viewport as you paint."
- "Node Based: Work fast with the convenience of nodes. Paint with fully procedural materials. Build fill layers with material nodes. Use brush nodes to create patterns and procedural brushes."
- GPU-accelerated (4K painting on integrated hardware; 16K on high-end); ray-traced baking; path-traced viewport; live-link plugins (Blender, Unreal, Unity — in development); runs on desktop + experimental iOS/Android; portable, <10MB.

Manual (Tier 1, directly observed — workflow):

- Import meshes: drag & drop unwrapped .obj (UDIM tile split option; .fbx/.blend/.stl/.gltf/.glb also); built-in UV unwrap; "if you modify UV map of the imported mesh, you will have to also export the modified mesh back out of ArmorPaint alongside the painted textures so they can be UV mapped properly."
- Import materials: "Drag and drop a folder with PBR texture set onto the viewport. ArmorPaint will recognize the file extensions and create a new material from imported textures."
- **Export Textures**: resolution, 8/16/32-bit color, png/jpg/exr; export all visible or selected layers; **presets**: Generic (individual PBR textures), Unreal (packed occlusion-roughness-metallic), Unity (packed metallic-occlusion-smoothness), Minecraft, base_color, specular; custom channel swizzling per preset (RGBA per texture slot); padding to prevent seams; export to disk or pack into project.
- **Export Mesh** (.obj/.glb) — for sculpted or UV-modified meshes.
- Project file .arm: "Mesh, layers, materials and brushes will be saved."
- Tools: Brush (radius/opacity/hardness/blending/TexCoord [UV Map, Project from view, Triplanar]/X-Ray/Symmetry), Eraser, Fill (face/angle/UV-island fill modes), Decal, Text, Clone, Blur/Smudge, Particle, Color ID (mask by color-id map), Picker (reads base color/normal/occlusion/roughness/metallic from surface; paint mask by picked material), Material (live preview), Cursor, Select (viewport mask).
- **Materials composed with nodes**: "When painting, brush applies a material onto the surface"; set which channels the material affects; Fill Layer from material; bake material into textures; nodes mimic Blender Cycles.
- **Layers**: Paint Layer, Fill Layer, Decal, Path/Curve, Black/White Mask, Fill Mask, Filter (adjust layer with nodes), Group; layer affects chosen channels; layer parented to object → multiple UV maps per project; merge/duplicate/convert/export layer; mask operations (apply/invert/merge).
- 2D View: shows channels of selected layer, "updated immediately as you paint"; paint tools usable in 2D view; UV wireframe overlay; tiling.
- Viewport modes: Lit / individual channel visualization (no lighting) / Path Traced; environment map; split view.
- **Workspaces**: paint 3d / paint 2d / nodes / script. **Workflow setting**: pbr (all channels) / base ("restricts painting to base color and opacity, use for non-PBR projects") / sculpt ("enables displacement socket").
- **Baking** (Bake Texture node): AO, Curvature, Lightmap, Bent Normal, Thickness, Normal (from high-poly), Height (from high-poly), Derivative, Position, TexCoord, Material ID, Object ID, Vertex Color; "Use AO bake with small Radius to bake Cavity"; "Use Curvature bake to create dirt masks"; results processable with nodes or exportable.
- **Sculpting**: work-in-progress mode; "Use non-destructive layer workflow to refine the mesh with details. All tools from paint workflow available for sculpting"; displacement socket in sculpt workflow.
- Neural nodes (local AI): Image to PBR ("Extract base color, occlusion, roughness, normal map and height from color input. A photo image is expected"), Text to Image (seamless/tile option), Edit Image, Upscale; photo→material pipeline documented.
- Picker/Color ID/masks: painting restricted by mesh faces, color IDs, picked materials, viewport masks.

Interpretation: ArmorPaint is the cleanest minimal expression of the painter pole: mesh in → layers/materials over channels → paint on surface → bake mesh maps → export PBR texture sets (engine presets) → mesh out if modified. It also shows the Type's edges: non-PBR workflow (base), sculpt-adjacent displacement, photo→material authoring.

### Quixel Mixer (scan-mixing pole; retired) — Evidence Layer A (retirement observation)

- https://quixel.com/mixer now serves the general Megascans library page ("Capturing the world. Empowering creativity… Browse on Fab"). No Mixer product page, download, or documentation is reachable from the site's navigation.
- Interpretation: the scan-based texture-mixing product is no longer marketed as a standalone application; the Megascans asset library continues (distributed via Fab). Mixer is retained in this research as (a) evidence that scan/photo-sourced texture authoring was a recognized pole of this Type, and (b) a market-structure observation: asset libraries and authoring tools are separable businesses. No operational claims about Mixer are made.

### Substance 3D Painter / Designer (market-defining family) — Evidence Layer B/C only (source-limited)

- Adobe domains unreachable during this pass (see Sources). No Tier-1/2 evidence fetched.
- Third-party corroboration (captured by the digital-sculpting pass): 3DCoat's own positioning names Substance Painter as the reference PBR-texturing product in its market ("golden mean between Blender, ZBrush, and Substance Painter… sculpt → retopo → UV → PBR texturing → export").
- The sibling passes' research notes (3d-rendering, digital-sculpting, procedural-3d) treat Substance Painter/Designer as the canonical members of the texture-painting and procedural-material poles respectively.
- Held claims: Substance 3D Painter is a 3D texture-painting application (painter pole); Substance 3D Designer is a node-based procedural material-authoring application (procedural pole). Both are listed as representative products. **No operational detail asserted.**

## Cross-product Comparison

| Structure / capability | Mari | Toolbag | ArmorPaint | Substance (source-limited) | Assessment |
|---|---|---|---|---|---|
| Appearance data as the product's output (texture maps / material definitions) | yes (channels → export textures) | yes (Texture Projects → export maps) | yes (layers/materials → export PBR textures) | yes (positioning-level) | **Core (all)** |
| Application holds the 3D surface context (mesh + UV) | yes (project stores geometries; patches) | yes (Texture Project on mesh, texture sets) | yes (drag & drop mesh; UV map central) | yes (positioning-level) | **Core (all)** |
| Paint directly on the 3D surface | yes (projection painting, 3D or 2D) | yes (real-time 3D painting) | yes (paint 3d workspace) | yes (positioning-level) | **Core (painter pole)** |
| Named channel/map structure bound to shader inputs | yes (channels: diffuse/displacement/specularity… → shader inputs) | yes (28 input-map types; metalness & specular workflows) | yes (channels per layer; picker reads base color/normal/occlusion/roughness/metallic) | yes (positioning-level) | **Core-adjacent: universal realization; single-map pre-PBR era kept the Type alive → common-mature, not invariant** |
| Non-destructive layer stacks with masks | yes (layer stacks in channels; paint/procedural/adjustment/masks) | yes (infinite layering & masking; layer types) | yes (paint/fill/decal/path/mask/filter/group layers) | yes (positioning-level) | Common mature (form varies; node graphs are the procedural form) |
| Node-graph material authoring | yes (node graph manages channels/layers/shaders) | partial (procedural layers; not a full graph workspace per fetched pages) | yes (materials composed with nodes; brush nodes) | yes (Designer pole; positioning-level) | Common mature (pole-dependent) |
| Masks/generators driven by mesh data (curvature/AO/cavity/position) | yes (Smart Masks; procedurals) | yes (input maps auto-generated; Processor layers: Curvation/Dirt/Occlusion/Scratch/Thickness) | yes (bake curvature→dirt masks; AO→cavity; Color ID masks) | yes (positioning-level) | Common mature |
| Reusable material/texture libraries; "smart" materials | yes (Material System; Smart Masks; content library) | yes (Library: materials/smart materials/brushes/grunges; drag-drop blockout) | yes (import .arm materials; ArmorPaint Cloud browser) | yes (positioning-level) | Common mature |
| Real-time PBR preview viewport on the mesh | yes (canvas display under user-specified lighting; shaders) | yes (real-time painting; physically accurate) | yes (instant visual feedback; Lit/Path-Traced modes) | yes (positioning-level) | Common mature |
| Mesh-map baking (normal/AO/curvature/height from high-poly) | yes (Bakery bakes mesh texture maps; Texture Transfer) | yes (dedicated Bake pillar; bake live-link into texture project) | yes (Bake Texture node: normal/height from high-poly, AO, curvature, thickness…) | yes (positioning-level) | Common mature (also sold standalone elsewhere) |
| UDIM / multi-tile / multiple texture sets | yes (thousands of UDIMs; 32K/UDIM) | yes (UDIM & multiple texture sets from one project) | yes (UDIM tile split on import; atlases) | yes (positioning-level) | Common mature (scale is variant) |
| 2D view of channels alongside 3D paint | yes (paint in 3D or 2D viewports or onto UVs) | partial (per fetched pages: painting tools; 2D not headline) | yes (2D View of layer channels; paint in 2D) | yes (positioning-level) | Common |
| Engine-targeted export presets & channel packing | partial (export textures; pipeline formats; OCIO) | yes (custom texture packing per channel; map naming) | yes (Generic/Unreal/Unity/Minecraft presets; swizzling) | yes (positioning-level) | Common mature |
| Project file holding mesh + layers + materials | yes (project stores geometries + textures; session scripts) | yes (Texture Project) | yes (.arm: mesh, layers, materials, brushes) | yes (positioning-level) | Common mature |
| Photo/scan → material extraction | not observed on fetched pages | not observed | yes (Image-to-PBR neural node; photo→4K PBR material) | yes (Sampler pole; positioning-level) | Variant (pole-dependent) |
| Bundled final rendering/presentation | partial (preview; render in Modo) | yes (ray-traced + raster renderers; WebGL viewer) | partial (path-traced viewport; screenshots) | no (positioning-level) | Variant — the straddle axis vs 3D Rendering |
| Displacement/height painting that deforms geometry | yes (displacement channels; displacement named as channel data) | not observed | yes (sculpt workflow WIP; displacement socket; Apply Displacement to mesh) | not asserted | Variant — the gray zone vs Digital Sculpting |
| AI assistance (text-to-texture, image-to-PBR, upscale) | not observed on fetched pages | not observed | yes (neural nodes, local models) | not asserted | Variant (era machinery) |
| Enterprise pipeline machinery (Python API, OCIO, session sharing) | yes (extensive API; Python Shelf; OCIO; session scripts) | partial (studio licensing) | partial (scripting/plugins) | not asserted | Variant (customer-tier dependent) |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

A Texture / Material Authoring Application is recognizable when — and only when — all three hold:

1. **Surface-appearance data as the unit of record.** The product's central, persistent objects are texture maps and/or material definitions that describe how a 3D surface looks (color, normal, roughness/metalness, height, emissive…). Remove → a flat image editor (pixels without surface meaning) or a geometry tool.
2. **Binding to 3D surface context.** The application itself holds the 3D surface frame the appearance is authored against — an imported mesh with its UV layout that the user paints on (painting pole), or surface-shading definitions parameterized for 3D surfaces (procedural pole). The data model is surface-oriented (UV space / mesh surface / 3D position), not flat-canvas-oriented. Remove → raster image editing; a UV-snapshot Photoshop workflow is image editing *serving* a texture pipeline, not this Type.
3. **Delivery of the authored appearance into the 3D pipeline.** The result leaves the application as consumable appearance assets — exported texture-map sets (commonly engine-targeted, channel-packed) and/or reusable material definitions — for use on 3D models in downstream applications. Remove → a paint sandbox or viewer with no pipeline role.

Jointly-held load-bearing test:

- 1 alone = image editor with channel vocabulary
- 2 without 1 = mesh/UV tooling (modeling territory)
- 3 without 1+2 = file converter
- 1+2 without 3 = paint sandbox, not a production authoring tool
- 1+3 without 2 = batch texture converter / material library with no surface binding

### L1 — Common Mature Structure (very common, not defining)

- Named channel/map structure (base color/albedo, normal, roughness, metallic, height, AO, emissive, ID maps…) bound to shader inputs; PBR metalness/specular workflows as the dominant modern posture (ArmorPaint even ships a non-PBR "base" workflow — proof the channel set is configurable, not invariant).
- Non-destructive authoring structures: layer stacks (paint/fill/procedural/adjustment/mask layer types) and/or node graphs — the two realized forms of the same "editable build-up" idea.
- Masks and generators driven by mesh data (curvature, cavity, AO, position, thickness, color ID) — "smart masks"/input maps that adapt effects to the mesh.
- Reusable material/texture libraries and "smart materials" that adapt to the mesh; drag-drop blockout of looks.
- Real-time PBR preview of the actual mesh while authoring (instant visual feedback).
- Mesh-map baking (normal/height/AO/curvature from high-poly to low-poly) — in-product (Mari Bakery, Toolbag Bake, ArmorPaint Bake node) or companion.
- UDIM / multi-tile / multiple texture sets handling; per-object channel sets.
- 2D channel view alongside 3D painting.
- Engine-targeted export presets and per-channel texture packing.
- Project files holding mesh + layers + materials + brushes.
- Import of standard mesh formats; re-export of modified/UV-changed meshes alongside textures.

### L2 — Variant / Optional Structure

- Authoring philosophy: paint-first (Mari, Toolbag, ArmorPaint, Substance Painter) vs procedural-first (Designer pole; ArmorPaint nodes; Mari node graph) vs scan/photo-first (Quixel Mixer; ArmorPaint photo→PBR; Sampler pole).
- Scale posture: thousands of UDIMs @ 32K (Mari enterprise) vs portable GPU painter (ArmorPaint) vs mid-range (Toolbag).
- Displacement/height painting that deforms geometry (sculpt-adjacent; ArmorPaint sculpt workflow; Mari displacement channels).
- AI assistance: text-to-texture, image-to-PBR extraction, upscaling (ArmorPaint neural nodes; era machinery).
- Live links to engines/DCCs (ArmorPaint live-link plugins; Toolbag bake live-link; Substance bridges per third-party quotes).
- Enterprise pipeline machinery: Python APIs, OCIO color management, session sharing, render-target validation (Mari).
- Bundled final rendering/presentation (Toolbag's ray-traced/raster renderers, WebGL viewer) — the straddle axis.
- Asset-library services attached to the authoring tool (Megascans/Fab; Toolbag Library; ArmorPaint Cloud).
- Non-PBR workflows (ArmorPaint "base" workflow for non-PBR projects).
- Customer-tier packaging: enterprise node-locked/floating (Mari), individual/studio/academic (Toolbag), one-time purchase/pay-what-you-want (ArmorPaint), subscription suites (Substance).

### L3 — Vendor-specific Structure (research notes only)

- Mari: patches (UV patch organization), Bakery engine, Texture Transfer, Multi-Paint (8 simultaneous streams), Smart Masks content, Python Shelf, session scripts, Modo preview integration, 32K@32bit-per-UDIM ceiling.
- Toolbag: Sync Points, Carve Groups, Vector layers with boolean ops, Processor layers, 28 named input-map types, Marmoset Viewer (WebGL), Library asset drops, individual/studio/academic licensing split.
- ArmorPaint: .arm project/material/brush format, Cycles-mimicking node set, named neural models (FLUX/Image-to-PBR/Real-ESRGAN/Hunyuan3D/Qwen), portable <10MB distribution, named export presets (Unreal/Unity/Minecraft packing schemes), workflow switch (pbr/base/sculpt).
- Substance: SBSAR material packages and the smart-material ecosystem (existence corroborated third-party; mechanics unverified — not asserted).
- Quixel Mixer: Megascans-native mixing workflow (product retired; mechanics not asserted).

## Rejected Findings

- **"PBR channel set is definitional"** — rejected. ArmorPaint documents a non-PBR "base" workflow ("restricts painting to base color and opacity, use for non-PBR projects"); the pre-PBR era (diffuse/bump/specular maps) is the Type's own history. The channel *structure* (named maps → shader inputs) is the stable idea; the specific channel set is era- and workflow-dependent.
- **"Layer stacks are definitional"** — rejected as L0. The procedural pole (Designer-style; ArmorPaint node materials; Mari node graph) authors without layer stacks. The stable idea is non-destructive editable build-up; layers and node graphs are its two forms (L1).
- **"Painting on the mesh is definitional"** — rejected as L0 for the whole Type. The procedural pole authors materials without importing a specific mesh. Painting-on-mesh defines the *painter pole*; the Type-level invariant is the 3D surface frame (leg 2 phrased to cover both poles).
- **"Baking is definitional"** — rejected. Baking is universal in the current sample but is a pipeline step that also exists as standalone tooling; a material authoring product without high-poly baking still fits (procedural pole). Common mature (L1).
- **"Real-time GPU viewport is definitional"** — rejected. Era machinery; the historical check below covers pre-GPU products. Common mature.
- **"UDIM support is definitional"** — rejected. UDIM is a film/VFX-scale realization; game-art products use texture sets/tiles; small-pole products use single UV maps. L1/L2.
- **"AI texture generation is definitional"** — rejected. Era machinery (L2), present in one sampled product's documented workflow.

## Boundary Findings

**1. vs 3D Rendering Application (sibling §04.14) — JOINT REVIEW FLAG DISCHARGED (keep-both ratified).**
The rendering pass proposed the primary-deliverable test; this pass confirms it from the authoring side. The structural seam: **what the product's primary deliverable is** — material/texture *assets* (this Type) vs rendered *images* (rendering Type). Evidence from this side: every authoring product's export path delivers maps/materials (Mari export textures; Toolbag export by project/map with packing; ArmorPaint export presets), while their viewports/renders are preview/presentation surfaces. Marmoset Toolbag straddles by bundling renderers with its Texture Projects — but its own framing ("test and validate PBR assets… between a modeling package and a game engine") keeps the asset workflow central. Gradient acknowledged; keep-both. A game-art suite hosting all three (bake+texture+render) is one product spanning two Types, not evidence that the Types merge.

**2. vs Digital Sculpting Application (§04.13) — gray zone confirmed, seam held.**
The sculpting pass flagged displacement-class painting. From this side: the seam is **whether the primary output changes geometry or describes surface appearance**. This Type's products treat height/displacement as *appearance channels* (Mari: "channels for diffuse color, displacement, or specularity"; ArmorPaint: displacement socket + Apply Displacement as an edit operation); sculpting products treat deformation as the product. ArmorPaint's in-development sculpt mode ("all tools from paint workflow available for sculpting") shows one product hosting both — mode-level, same pattern as the sculpting pass's suite observation. Keep-both; displacement painting recorded as a variant axis (L2).

**3. vs 3D Modeling Application (§04.13) — confirmed from this side.**
Modeling assigns materials at surface level and prepares UVs as a *secondary* activity; here the appearance IS the product. The traffic direction is the tell: modeling apps export meshes *to* this Type; this Type exports maps/materials *back* to engines/renderers. ArmorPaint's built-in UV unwrap and mesh modifiers are convenience repairs of the binding, not modeling features ("Less Modeling, More Texturing" is Toolbag's own framing of the same pull).

**4. vs Procedural 3D Creation Application (§04.13) — confirmed from this side.**
Same node-based authoring model, different output domain: 3D content (geometry/scene data) vs 2D surface-appearance data. The procedural-3d pass's own boundary line ("node-based procedural systems whose primary output is 2D texture/material data belong there") is ratified.

**5. vs Raster Image Editor / Digital Painting Application (§04.02) — hard boundary.**
No 3D surface binding: a raster editor's canvas is flat pixels; this Type's data model binds appearance to UV/surface coordinates and resolves it on a mesh. The historical Photoshop-plus-UV-snapshot workflow is image editing *serving* a texture pipeline — excluded from the Type (the application itself must hold the surface context). Conversely, this Type's 2D view (ArmorPaint 2D View; Mari 2D painting) is a projection of the surface-bound data, not a flat document.

**6. vs Photogrammetry Application (§04.13) — confirmed from this side.**
Photogrammetry *captures* appearance from photos as part of geometric reconstruction; this Type *authors* appearance for models (including, at one pole, extracting PBR maps *from* a photo — ArmorPaint Image-to-PBR — which is authoring input, not reconstruction).

**7. vs Game Engine / 3D Animation / Rendering Management** — engines consume assets at runtime; animation adds the time axis; rendering management handles job logistics. None of these author surface appearance as their unit of record.

**"去掉什么就变成另一个 Type" 判据汇总**: remove the surface binding → raster image editing; remove the appearance focus → modeling; remove the asset delivery → paint sandbox/viewer; make rendered images the deliverable → 3D Rendering; make geometry change the deliverable → Digital Sculpting; make 3D content the procedural output → Procedural 3D Creation.

## Historical / Market-Sample Check

- **Pre-PBR texture painting (1990s–2000s dedicated 3D painters, e.g. the Deep Paint 3D / BodyPaint 3D generation; held conceptual — no fetched source):** paint color/bump/specular maps directly on meshes with layers, export maps for the era's engines/renderers. Satisfies all three L0 legs with no PBR channel set, no GPU viewport, no UDIM. ✓
- **Procedural shading in the renderer era (RenderMan-style shader authoring; held conceptual):** material definitions authored as surface-shading programs destined for 3D surfaces — the procedural pole's ancestry. Satisfies legs 1–3 with no mesh import at all. ✓
- **ZBrush PolyPaint (sculpting pass's evidence):** color painted directly on surfaces without UVs — surface-bound appearance authoring inside a sculpt-first product; fits the painter pole's binding leg while remaining a sibling-Type product. ✓ (boundary, not counterexample)
- **Photoshop + UV snapshot workflow:** fails leg 2 (the application holds no surface context) — correctly excluded; it is image editing serving the pipeline. This is the historical check's most useful exclusion: it proves leg 2 is load-bearing, not era-specific.
- **Quixel Mixer (2010s scan-mixing pole):** satisfied the legs (appearance authored from scans, delivered as maps); its retirement is a market event, not a Type change. ✓
- Conclusion: the L0 survives era, scale, and philosophy variation; nothing in it names PBR, GPU, UDIM, layers, nodes, or AI.

## Uncertainties

1. **Substance operational detail** — the market-defining family could not be fetched; its smart-material/SBSAR mechanics, layer-system specifics, and export machinery are unverified here. All Substance-specific claims in the final document are kept at positioning level. (Source-access limitation recorded.)
2. **InstaMAT** — dropped from the sample (site unreachable). Its reported all-in-one posture (painting + procedural + asset management) could not be confirmed; no claims made.
3. **Procedural-pole depth** — the strongest direct evidence for the procedural pole comes from ArmorPaint's node materials and Mari's node graph; a dedicated procedural-material product (Designer-class) was not directly observed this pass. The pole's existence is corroborated by sibling-pass notes and third-party quotes (Layer B/C), not Layer A.
4. **Toolbag 2D-view parity** — the fetched Toolbag pages headline 3D painting; whether it offers a full 2D UV-space painting view was not confirmed. Held as unconfirmed; not asserted either way.
5. **Mixer retirement timing/reason** — observed only as the current state of quixel.com/mixer; no claim about when or why.
6. **Lookdev scope** — Mari's "look development with shaders" suggests material-assignment/preview workflows straddle into rendering territory; the exact lookdev split was not deeply researched. Recorded as a soft edge.

## Final Synthesis

The Type is real and coherent across its poles. Its defining core is a three-leg structure: **authored surface-appearance data (texture maps and/or material definitions), bound to 3D surface context the application itself holds, delivered as consumable assets into the 3D pipeline.** Everything else the market associates with the category — PBR channel sets, layer stacks, node graphs, smart materials, mesh-map baking, UDIM scale, real-time viewports, AI texture generation — is common mature structure or variant machinery, not definition. The painting pole (paint on the mesh) and the procedural pole (author materials as surface-shading definitions) are two realizations of the same binding-and-delivery structure; products increasingly host both. The three sibling flags are discharged: rendering keeps the image as deliverable (Toolbag straddle = gradient, keep-both); sculpting keeps geometry change as deliverable (displacement painting = variant axis); modeling/procedural-3d/photogrammetry seams all confirmed from this side.
