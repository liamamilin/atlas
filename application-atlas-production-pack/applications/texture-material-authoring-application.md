# Texture / Material Authoring Application

## Overview

A **Texture / Material Authoring Application** creates the surface appearance of 3D models — texture maps and material definitions — and delivers that appearance as reusable assets into a 3D pipeline (game engines, renderers, and other 3D applications).

The defining core is small:

```text
Surface-appearance data (texture maps and/or material definitions)
  bound to 3D surface context the application itself holds
    → authored through editable, non-destructive structures
      → delivered as consumable appearance assets
```

Everything else the market associates with the category — PBR channel sets, layer stacks, node graphs, smart materials, mesh-map baking, UDIM tile scale, real-time ray-traced previews, AI texture generation — is widespread in current products but is not what makes the product this Type. Older pre-PBR texture painters and renderer-era procedural shading tools fit the same core without any of those specifics.

The Type sits in the 3D production pipeline between modeling (which delivers geometry) and rendering/engines (which consume appearance to produce images). Its deliverable is the **asset**, never the final image — that distinction is the boundary with 3D rendering software.

## Users & Context

Primary users are artists who make 3D surfaces look right:

- **texture artists** — paint and assemble the appearance of characters, props, and environments
- **material artists** — author reusable surface materials (procedurally or from scans/photos) for teams to apply
- **character and environment artists** — texture their own models as part of asset creation
- **lookdev artists** (film/VFX) — develop and validate the shaded look of assets before final rendering

Typical contexts: game development (assets must export in engine-ready form), film and VFX (very large, high-precision texture sets on hero assets), product visualization and archviz (materials applied to CAD/BIM-derived models), and independent art creation.

The work context is a pipeline position: models arrive from modeling/sculpting applications; textured, material-complete assets leave toward engines, renderers, or lookdev scenes. The application is a desktop, GPU-heavy workstation tool in current products; customer tiers range from individual artists to enterprise studios.

## Core Model

### The Defining Core

Three properties hold together. Remove any one and the product stops being this Type:

- **Surface-appearance data as the unit of record.** The product's central, persistent objects are texture maps and/or material definitions — data that describes how a 3D surface looks: its color, surface-normal detail, roughness or shininess, metalness, height, emissive glow, and similar qualities. The output is not geometry (that is modeling) and not an image (that is rendering); it is the appearance layer in between.
- **Binding to 3D surface context.** The application itself holds the 3D frame the appearance is authored against. In the painting form, that is an imported mesh with its UV layout, painted directly on the surface. In the procedural form, it is a material defined in surface terms — parameterized by UV space, surface position, and orientation — destined for 3D surfaces. The data model is surface-oriented, not a flat canvas. This is what separates the Type from raster image editing: an image editor used to paint a UV texture is image editing *serving* a texture pipeline, not a texture authoring application.
- **Delivery into the 3D pipeline.** The authored appearance leaves the application as consumable assets — exported texture-map sets (commonly organized and packed for a target engine or renderer) and/or reusable material definitions — to be applied to 3D models downstream. Without delivery, the product is a paint sandbox, not a production authoring tool.

### What Mature Products Add

These capabilities are effectively universal in current products. They make the Type practical; they do not define it.

- **Named appearance channels.** The appearance is decomposed into named maps — base color/albedo, normal, roughness, metallic, height, ambient occlusion, emissive, ID masks and more — each bound to an input of the target surface shader. Physically based rendering (PBR) workflows (metalness or specular) are the dominant modern channel vocabulary, and some products also offer simpler non-PBR workflows.
- **Non-destructive authoring structures, in two forms.** Painters organize appearance as **layer stacks** — paint layers, fill layers, procedural layers, adjustment layers, and masks that can be reordered, grouped, and re-edited at any time. Procedural tools organize appearance as **node graphs** — networks of operations whose parameters stay editable. Both are the same idea (an editable build-up of appearance) realized differently, and many products offer both.
- **Mesh-driven masks and generators.** Effects are driven by data computed from the mesh itself — curvature, cavities, occlusion, thickness, position — so weathering and wear adapt automatically to the model's shape instead of being hand-painted everywhere.
- **Reusable materials and libraries.** Materials, masks, brushes, and textures are saved, shared, and dragged into projects; "smart" materials adapt their behavior to whatever mesh they are dropped onto.
- **Real-time preview on the actual mesh.** The viewport shows the model with its authored appearance under configurable lighting while the artist works — instant visual feedback is the standard working rhythm.
- **Mesh-map baking.** Detail is transferred between meshes: normal, height, ambient occlusion, curvature and similar maps are computed from a high-poly version onto the low-poly mesh that will actually be used — inside the product or in a companion step.
- **Multi-tile and multi-set handling.** Large assets are split across UV tiles (UDIM workflows) and multiple texture sets; enterprise products handle thousands of tiles at very high resolutions.
- **Engine-targeted export.** Export presets arrange maps, naming, bit depth, and per-channel packing to match the expectations of specific engines and renderers.
- **Project files.** The mesh, layers, materials, and brushes travel together in a savable project.

### One Structure, Many Implementations

The core model is conceptual. Current products realize each concept differently:

```text
Concept:            Surface-appearance data
Implementations:    texture-map sets (painter pole), procedural material
                    definitions (procedural pole), scan-derived materials

Concept:            3D surface binding
Implementations:    imported mesh + UV map, UDIM tiles, multiple texture
                    sets, triplanar/screen projection, sample surfaces
                    for procedural materials

Concept:            Authoring structure
Implementations:    layer stacks with masks (painters), node graphs
                    (procedural tools), both in one product

Concept:            Delivery
Implementations:    per-map or packed texture-set export with engine
                    presets, reusable material packages, live links
                    into engines and DCC tools
```

A reader who has only seen one form — say, painting color maps on a game asset — should still be able to recognize the procedural and scan-based forms as the same Type from this table.

## How It Works

### The painting workflow (the dominant form)

```text
Import the mesh (with its UV layout)
→ optionally bake mesh maps (normal/AO/curvature from a high-poly version)
→ block out the look: fill layers with materials from the library
→ paint on the 3D surface: brush strokes, decals, stencils, text
→ refine with masks and generators driven by mesh data
   (edge wear, dirt in cavities, grime along curvature)
→ preview continuously in the real-time viewport
→ export the texture set — individual maps or engine-packed channels
→ (if the UVs or mesh were modified in-product, export the mesh too)
```

The layer stack stays editable throughout: a mask can be inverted, a fill layer re-colored, a generator re-tuned, and the exported maps update. Nothing is flattened until export.

### The procedural workflow

```text
Build the material as a node graph
  (patterns, noises, gradients, masks, channel outputs)
→ evaluate it on a sample surface inside the product
→ parameterize it so others can adjust it
→ publish/package the material as a reusable asset
→ the material is applied to models downstream and resolves
   into that application's texture/shader inputs
```

The same graph can be exposed as a "smart material" that adapts to whatever mesh it is applied to.

### The scan/photo workflow

```text
Start from a photo or a scanned material sample
→ extract the appearance channels from it
   (base color, normal, roughness, height, occlusion)
→ clean up, tile, and assemble into a material
→ use it to paint, or export it as a texture set
```

### Where baking fits

Baking is the bridge from the modeling side: detail that exists in a high-poly sculpt is computed into maps the low-poly game/render mesh can carry. Mature products bake in-product (often GPU-accelerated) and feed the results straight into the texture project as masks and input maps.

### Capability tiers

**Defining core** — surface-appearance data as the record; 3D surface binding; delivery of consumable assets.

**Standard capabilities** — named channels bound to shader inputs; layer stacks and/or node graphs; mesh-driven masks; material libraries and smart materials; real-time preview; mesh-map baking; multi-tile/texture-set handling; engine-targeted export; project files.

**Optional / variant** — bundled final rendering and presentation; displacement painting that deforms geometry; AI assistance (text-to-texture, photo-to-PBR extraction, upscaling); live links into engines; enterprise pipeline machinery (scripting APIs, color management, session sharing); attached asset-library services; non-PBR workflows.

## Interfaces

Described conceptually; exact layout and naming vary by product.

### 3D viewport (paint + preview)

The working center. Shows the mesh with its authored appearance under configurable lighting; painting tools act directly on the surface.

- typical information: the model, its texture state, environment lighting, wireframe/UV overlays, channel-isolation modes
- primary actions: paint, erase, fill, stamp decals, project stencils, orbit/zoom, toggle channel visualization, capture previews

### Layer stack panel

The appearance's structure, in the painter form.

- typical information: ordered layers (paint/fill/procedural/adjustment), their masks, opacities, blend modes, channel assignments
- primary actions: add/reorder/group layers, add and edit masks, convert or merge, set which channels a layer affects

### Node graph editor

The appearance's structure, in the procedural form — and in many products an alternate surface over the same data as the layer stack.

- typical information: nodes and connections producing each channel; parameters per node
- primary actions: add/connect nodes, tune parameters, preview intermediate results, expose parameters for reuse

### 2D channel view

The flat projection of the surface-bound data: the UV-unwrapped channels of the selected layer or object, updated live as the artist paints in 3D (and paintable directly).

### Material / asset library

Browsable materials, smart materials, masks, brushes, and textures; drag-and-drop onto the model or layer stack; save and share custom content.

### Bake panel

Mesh-map baking: choose maps (normal, AO, curvature, height, thickness, ID…), source and target meshes, and settings; results land in the texture project as usable maps and masks.

### Export dialog

The delivery terminus.

- typical information: resolution, bit depth, format, per-map or packed output, naming schemes, engine presets
- primary actions: export all or selected maps, choose packing/presets, export the (possibly modified) mesh alongside

## Important Rules / Behaviors

- **Appearance is bound to surface coordinates.** The maps are meaningful only through the mesh's UV layout. If the UVs or mesh are modified in-product, the mesh must be exported together with the textures or the downstream application cannot map them correctly.
- **Authoring is non-destructive until export.** Layers, masks, and node parameters stay editable; the exported maps are a resolution of the stack at export time. Changing the stack and re-exporting is the normal iteration loop.
- **Channels follow the target workflow.** The set of maps a project carries matches the downstream shading model — a full PBR set for engine work, a reduced set for non-PBR targets. Products let the artist configure which channels exist and which layers affect them.
- **Mesh-driven effects adapt to the model.** Masks generated from curvature, occlusion, or position recompute against the mesh, so a weathering layer survives topology changes better than hand-painted masks.
- **Export must match the consumer.** Engines and renderers expect specific map naming, channel packing, bit depths, and color encodings; export presets exist because a correct-looking asset in the authoring tool can still arrive broken if delivered in the wrong arrangement.
- **The viewport is an instrument, not the deliverable.** Preview quality exists to validate the asset ("will this look right in the final render?"); the asset — maps and materials — is what leaves the application.
- **Baking transfers detail across meshes.** Normal/height/AO bakes move high-poly detail onto the low-poly mesh; baked maps then feed masks and generators rather than being painted from scratch.

## Variants

- **Paint-first products** — the mesh is imported and appearance is painted and layered directly on it; the dominant form for character and prop work.
- **Procedural-first products** — materials are authored as node graphs and published as reusable, parameterized assets; the dominant form for material libraries and team-wide surfacing.
- **Scan/photo-first products** — appearance starts from photographs or scanned material samples and is extracted into PBR maps; often paired with a large asset library. (One well-known scan-mixing product of this pole has been retired from the market; the pole itself persists inside other products' photo-to-material features.)
- **Lookdev-suite straddles** — products that bundle baking, texturing, and final rendering for game-art asset validation; the authoring core is intact but rendering/presentation is included.
- **Scale postures** — enterprise film/VFX tools handling thousands of high-resolution UV tiles per asset vs lightweight standalone painters running on modest hardware.
- **Enterprise pipeline variants** — scripting APIs, color-management compliance, session sharing, and render-target validation for studio pipelines.
- **AI-assisted variants** — local or cloud models for text-to-texture generation, photo-to-PBR extraction, and upscaling, embedded as nodes or tools.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| 3D Rendering Application | sibling; closest boundary | the primary deliverable is rendered images; here it is material/texture assets. Rendering applications consume and assign materials to produce images. Products that bundle both (bake + texture + render) straddle the seam but keep the asset workflow central |
| Digital Sculpting Application | adjacent | sculpting changes geometry with brushes; this Type describes surface appearance. Displacement/height painting (which can deform geometry) is the shared gray zone — treated here as an appearance channel, there as the product itself |
| 3D Modeling Application | upstream neighbor | modeling assigns materials at surface level and prepares UVs as secondary activities; here the appearance is the product. Models flow from modeling into this Type |
| Procedural 3D Creation Application | same authoring model, different output | node-based procedural systems whose primary output is 3D content (geometry/scenes) vs 2D surface-appearance data here |
| Raster Image Editor / Digital Painting Application | hard boundary | flat-pixel canvas with no 3D surface binding. Painting a UV texture in an image editor is image editing serving a texture pipeline, not this Type — the application itself must hold the surface context |
| Photogrammetry Application | adjacent | photogrammetry captures appearance from photos as part of geometric reconstruction; this Type authors appearance for models (including extracting maps from a photo as authoring input) |
| Game Engine / Game Development Platform | downstream consumer | engines apply the authored materials at runtime; they are a delivery target, not the authoring venue |
| Rendering Management Application | sibling | render-job logistics (queues, farms, deadlines) vs appearance authoring; different units of record |

## Representative Products

- **Adobe Substance 3D Painter** — the market-defining 3D texture-painting application (painter pole)
- **Adobe Substance 3D Designer** — node-based procedural material authoring (procedural pole)
- **Foundry Mari** — high-end film/VFX texture painting at UDIM scale
- **Marmoset Toolbag** — game-art lookdev suite bundling baking, texturing, and rendering
- **ArmorPaint** — open-source standalone GPU texture painter (minimal/indie pole)

The core model was checked against pre-PBR texture-painting practice, renderer-era procedural shading, and a retired scan-mixing product (Quixel Mixer) to avoid over-fitting the definition to the current PBR-era, GPU-viewport market shape.

## Sources

Research date: **2026-09-09**

- Foundry Mari — product page: https://www.foundry.com/products/mari ; documentation: https://learn.foundry.com/mari/docs (User Guide: Shading Networks, Channels, Export/Import)
- Marmoset Toolbag — https://marmoset.co/toolbag/ ; texturing: https://marmoset.co/toolbag/texturing/
- ArmorPaint — https://armorpaint.org/ ; manual: https://armorpaint.org/manual
- Quixel — https://quixel.com/mixer (observed serving the Megascans library page; Mixer no longer marketed as a standalone product)

> Sourcing limitation: the Adobe Substance 3D product family could not be fetched from the research environment on 2026-09-09 (vendor domains repeatedly timed out; third-party documentation of its integrations was also unreachable). Substance 3D Painter / Designer are included as representative products at positioning level only, corroborated by third-party vendor statements; no operational details about them are asserted in this document. Claims about all other products are calibrated to the fetched official sources.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
