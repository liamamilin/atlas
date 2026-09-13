# Research Notes — Digital Sculpting Application

Research date: 2026-09-07
Methodology: v1.1 (update-v1/)
Directory leaf: "Digital Sculpting Application" (Section 04.13 3D Creation)
Slug: digital-sculpting-application

---

## Research Goal

Understand what a Digital Sculpting Application is as an Application Type: what object the software operates on, what the primary interaction is, what structure and capabilities mature products share, how the products differ in representation and packaging, and where the Type's boundary sits against the 3D Modeling Application and other 3D-creation neighbors.

## Initial Boundary (hypothesis before research)

- A sculpting application shapes a 3D surface directly with brush-like tools, the way an artist works clay — pushing, pulling, smoothing, carving — rather than building geometry from discrete components (vertices/edges/faces editing, parametric features, booleans as primary operations).
- Primary users: character/creature artists, prop and collectible artists, 3D-printing hobbyists, concept artists.
- Nearest neighbors: 3D Modeling Application (closest and riskiest boundary), Texture/Material Authoring Application, Digital Painting Application (2D analog), Procedural 3D Creation Application, Photogrammetry Application, 3D Animation.
- Unknowns going in: topology strategies per product (subdiv levels vs dynamic tessellation vs voxel); whether retopology/UV/painting are in-Type or adjacent; whether symmetry/masking/layers are definitional; historical-sample survival.

## Research Questions

1. What is the sculpted object, and how do products represent it (polygon mesh with subdivision levels, dynamic tessellation, voxels)?
2. What is the brush/tool model? What operation families exist, and what controls a stroke (size, strength, falloff, alpha, pressure)?
3. How do products let artists manage detail resolution without managing topology manually?
4. What supporting machinery is bundled (masking, hiding, layers, symmetry, posing/transform, multi-object scenes)?
5. What is the canonical workflow arc: base mesh → block-out → detail → preparation (retopo/UV/bake) → export/render?
6. How do products differ in philosophy, platform, packaging, business model, and customer tier?
7. Where exactly is the boundary with the 3D Modeling Application, and with texture authoring?
8. Historical check: would earlier/simpler/lite sculpting products still fit the definition?

## Representative Products

Selected for market representability + documentation quality + different philosophies + different customer tiers/platforms:

| Product | Vendor | Philosophy / why sampled |
|---|---|---|
| ZBrush | Maxon (Pixologic heritage) | The category-defining dedicated desktop sculpting suite; subscription; pro studios |
| Blender (Sculpt Mode) | Blender Foundation | Free open-source full 3D suite where sculpting is one mode; different packaging pole |
| Nomad Sculpt | Hexanomad (single developer) | Mobile/tablet-first standalone sculpting app; one-time purchase; consumer/prosumer tier |
| 3D-Coat | Pilgway | Sculpt-first pipeline app with a voxel representation and rooms architecture (sculpt → retopo → UV → paint); perpetual + subscription |

Mudbox (Autodesk) was considered but skipped: documentation availability uncertain and the four sampled products already cover the philosophy space. Sculptris and ZBrushCore/Mini are used as historical/lite reference points where the vendors' own material mentions them.

## Sources

Tier 1 (official operational documentation — fetched 2026-09-07):

- Nomad Sculpt Manual: https://nomadsculpt.com/manual (Overview), /manual/gettingstarted, /manual/tools, /manual/topology, /manual/files
- 3DCoat Documentation: https://3dcoat.com/documentation/ (portal), /manual/workspaces-rooms/ (Rooms), /manual/workspaces-rooms/sculpt/ (Sculpt room: Voxel mode / Surface mode / Sculpt Layers / Transform tools / Live Booleans / Primitives)
- ZBrush Online Help (Maxon): https://help.maxon.net/zbr/en-us/Content/html/zbrush-online-help.html (full table of contents: Getting Started / Basic Concepts (Pixol, ZTools, Canvas Document, Projects), 3D Modeling user guide (Creating Meshes: Primitives, DynaMesh, Sculptris Pro, ZSpheres, Live Boolean, Remeshing; Subdivision Levels; Dynamic Subdivision; Masking; Polygroups; Sculpting Brushes; Symmetry; 3D Layers; Morph Targets; Posing/Transpose; Topology/ZRemesher/Retopo; Exporting: Displacement/Normal maps; Ready for Print), ZBrushCore/ZBrushCoreMini)

Tier 2 (official product pages — fetched 2026-09-07):

- Maxon ZBrush product page: https://www.maxon.net/en/zbrush (positioning, FAQ, audiences, platforms)
- Blender: https://www.blender.org/features/ and https://www.blender.org/features/sculpting/ (official sculpting feature page)
- Nomad Sculpt homepage: https://nomadsculpt.com/ (licensing FAQ, platforms)

Source-access limitations:

- Blender Manual (docs.blender.org) returned HTTP 403 on every attempt (2 attempts, 2026-09-07) and was abandoned per the network-restriction rule. Blender-specific sculpting claims therefore rest on the official blender.org feature pages (Tier 2) plus cross-product commonality, and are worded accordingly. No precise Blender operational details are asserted from memory.
- ZBrush's legacy Pixologic docs (docs.pixologic.com) served only a JavaScript shell ("HTML5") on every attempt and were abandoned; ZBrush Tier-1 evidence instead comes from Maxon's online help (help.maxon.net/zbr), whose table of contents was fully retrievable, plus the Maxon product page.
- The Maxon ZBrush "features" web app (maxon.net/en/product-detail/zbrush/features?categories=...) renders via JavaScript; feature-detail body text was not retrievable. The help-center TOC + product-page copy were used instead.

Evidence layers used below: **A** = directly observed in one product's official docs; **B** = observed across multiple sampled products; **C** = canonical inference from cross-product comparison and boundary reasoning.

---

## Product observations

### ZBrush (Maxon) — evidence layer A unless noted

Positioning (product page): "Shape characters, creatures, and worlds in virtual clay. Maxon ZBrush is an Academy Award-winning and industry-leading tool for digital sculpting, modeling and painting. Its customizable tools and features, including more than 200 proprietary brushes, allow you to work with polygons the same way you would with actual clay." FAQ: "It lets you shape highly detailed 3D models the way you would work with real clay, with a brush system that can handle tens of millions of polygons in real time." File formats: "imports and exports standard 3D geometry formats and most industry-standard image formats for texturing, and connects to other applications through GoZ." Platforms: Windows, macOS, iPadOS, Windows on Arm; "A graphics tablet is strongly recommended." Audiences listed: character & creature artists, digital sculptors, concept artists, toy & collectible artists, product designers, illustrators moving into 3D, studios. Feature pillars on the page: Sculpting ("dynamic brush system, base mesh creation tools, and remeshing that lets you stop thinking about topology and just sculpt. Combine, inflate, drape, and instance geometry"), Hard-surface & polygon modelling (ZModeler, Live Boolean), Painting & texturing (PolyPaint — "paint directly on the surface with no UVs or texture maps assigned in advance"; UV Master; SpotLight; MorphUV), Rendering (Redshift; BPR), Pipeline (GoZ to Cinema 4D).

Help-center structure (Tier 1, TOC directly observed):
- Basic Concepts: The Pixol, ZTools and Edit mode, The Canvas Document, ZBrush Projects — ZBrush's native document/tool model (a 2.5D canvas heritage plus 3D "Tools").
- Base mesh creation: Primitives, Polymeshes, ShadowBox, Mesh Extract, ZModeler, Quick Mesh, Live Boolean, Snapshot3D, Remeshing, DynaMesh, Sculptris Pro, ZSpheres, ZSketch, Mannequins.
- Mesh organization: SubTools (multiple objects within one Tool), SubTool Folders, Polygroups, Mesh Visibility.
- Resolution: Subdivision Levels, HD Geometry, Dynamic Subdivision; topology-rebuilding: DynaMesh, Remeshing, Sculptris Pro (dynamic tessellation mode named after the acquired Sculptris app).
- Sculpting: Sculpting Brushes (Smooth; Curve brushes; Insert Mesh / IMM; Alphas; Vector Displacement Meshes; Snake Curve; Strokes; Lazy Mouse; Brush Noise), Symmetry (incl. Dynamic Symmetry), Morph Targets, 3D Layers, Surface Noise/NoiseMaker, Bas Relief, Projection Master, Slime Bridge.
- Masking (incl. Mask by PolyPaint, Mask Region), Deformations, Transpose, Gizmo 3D with Deformers.
- Posing: Transpose (Action Line), Rigging (pose-only), Transpose Master, Proxy Pose.
- Topology: ZRemesher (automatic retopology; adaptive size; transferring detail), Topology Brush, manual Retopo workflow, ZSphere Topology.
- Painting: Polypaint (vertex-level color without UVs), Texture Maps, Spotlight, ZAppLink.
- Exporting: UV Mapping (UV Map: Unwrap), Texture Maps, Displacement Maps, Vector Displacement Maps, Normal Maps — the "hand the detail to a downstream renderer/game engine" mechanism.
- Ready for Print: Draft Analysis, Mask by Draft, PolyPaint from Thickness/Draft — 3D-printing orientation.
- Materials/Lights/Rendering: MatCap, LightCap, BPR, Redshift.
- Editions documented in the same help: ZBrushCore and ZBrushCoreMini (simplified editions).

### Blender Sculpt Mode (Blender Foundation) — evidence layer A (official feature pages) with documented limitation

Positioning: "Blender is the free and open source 3D creation suite. It supports the entirety of the 3D pipeline—modeling, rigging, animation, simulation, rendering, compositing and motion tracking, even video editing..." Sculpting is one named feature area alongside Modeling, Animation & Rigging, Rendering, etc. (blender.org/features). Feature page for modeling: "Sculpting, retopology, modeling, curves. Blender's modeling toolset is extensive."

Official Sculpting feature page (blender.org/features/sculpting/), direct quotes:
- "Digital sculpting tools provide the power and flexibility required in several stages of the digital production pipeline. For example, during character design and exploration or environment design."
- "By offering the sculpting and the polygonal modeling toolsets side by side, Blender greatly simplifies the transition between conceptual research and final model production."
- "Sculpting in Blender includes: 20 different brush types; Multi-res sculpting support; Dynamic Topology sculpting; Mirrored sculpting." (a dedicated Sculpting workspace is shown)
- "Blender comes with built-in brushes such as Crease, Clay Strips, Pinch, Grab, Smooth, Mask and many more. It is also possible to customize your own."
- Dynamic Topology: "Dynamic topology (also known as dyntopo) is a dynamic tessellation sculpting method, which adds and removes details on the fly, whereas regular sculpting only affects the shape of a mesh."
- Masking: "While sculpting, areas might be hidden behind parts of the mesh or they might be too close to other parts... it is useful to isolate parts of a mesh to sculpt on. This can be done by either completely hiding parts of the mesh or by masking areas that can not be sculpted on."
- Homepage feature bullets (fetched): "Advanced sculpting tools and brushes; Multi-resolution and Dynamic subdivision; 3D painting with textured brushes and masking."

### Nomad Sculpt (Hexanomad) — evidence layer A (official manual, rich)

Positioning (Getting Started): "Nomad is a 3d sculpting app that works on many devices, and works best on tablets with a pressure sensitive stylus, eg an Apple iPad and pencil... It is inspired by desktop sculpting apps like Zbrush and Blender, with a focus on an easy to understand UI, without sacrificing on features." Homepage: "A sculpting and painting application." Platforms: iPad, Android, desktop (Windows/macOS), web demo; one-time purchase, per-platform.

First-sculpt workflow (Getting Started, directly observed): app opens with a sphere; "Simply drag your stylus on the sphere to start sculpting. Symmetry is enabled by default to make sculpting easier." Radius and intensity sliders; default tool is the Clay tool, which "adds to the surface"; `Sub` button subtracts; Smooth is a sticky shortcut; two-finger gestures rotate/zoom/pan/undo. Interface: top menus, stats, nav cube, toolbox (right), left toolbar (radius/intensity + shortcuts for Symmetry, Sub, Smooth, Mask, Hide, Gizmo, Color, Alpha), bottom toolbar (Undo/Redo/History/Solo/X-Ray/Voxel remesh shortcut/Grid/Wire/Inspect).

Tool model (Tools page, directly observed): tools are color-coded by category — Brush tools (Clay, Brush, Smooth, Layer, Inflate, Nudge, Stamp, DelLayer), Move tools (Move, Drag), Mask tools (Mask, SelMask), Paint tools (Paint, Smudge), Flatten tools (Flatten, Planar), Pinch tools (Crease, Pinch), Selection-based tools (Trim, Split, Project — draw a 2D shape first, then operate), Creation tools (Tube, Lathe, Insert), Transform tools (Transform, Gizmo), Misc (Facegroup, Hide, Measure, Select, Quad Remesher), View. Every tool has a `Sub` (alternate/inverse) mode; e.g. Clay Sub removes material, Paint Sub erases. Masked vertices "are protected from sculpting or painting"; masks can be painted or drawn with lasso/polygon/rect/ellipse shapes, blurred/sharpened, converted to facegroups, and used to create new geometry via Extract/Split/Carve. Trim/Split notes: the cut is projected from the camera — orthographic recommended; perspective warns the user. Layer tool raises surface to a limited height; combined with the Layers system for a constant max height.

Topology menu (Topology page, directly observed): polygon-based (triangles and quads); polygon stats display. Three detail-resolution methods, explicitly framed: **Multiresolution** (subdivision levels; go down a level, edit, return — high-res details reproject automatically; WARNING that topology-altering tools destroy the other levels), **Voxel Remesher** ("Recompute a new topology with uniform density... very useful when you don't want to think about topology and simply do free-form sculpting"; voxel used temporarily; self-intersections resolved; non-watertight holes filled first), **Dynamic Topology** ("As you sculpt, Nomad will adaptively add and remove polygons during the brush stroke"; detail based on Screen / Radius / Constant; protect masked areas; triangles). Misc: Decimation (reduce polygons, keep detail; masked areas preserved; recommended for 3D-print export), UV Unwrap (UVAtlas and BFF algorithms; UV analogy explained: "wrapping a gift"), Bake → texture (bake high-res detail/paint from other visible objects into the selected low-poly object's textures: normal/roughness/metalness/color/emissive/opacity), Reproject to vertex (inverse of baking). "When models are made in Nomad, you can paint directly onto objects without UVs."

Files (Files page, directly observed): native project (.nom) with save/open/rename/clone/autosave (autosave is a prompted popup because 3D files are big; scene is compressed before saving). Import: Nomad, glTF (.glb/.gltf), OBJ, STL, PLY, FBX (experimental). Export: NOM, GLTF/GLB, OBJ, USD, PLY, STL, FBX — with a documented per-format feature matrix (vertex colors, vertex PBR, quads, layers via glTF morph targets, objects, facegroups, hierarchy, lights, textures); e.g. STL loses layers/objects/facegroups; layers survive only in NOM/glTF/PLY/FBX. Render export to PNG (transparent background option, render ratio, final size).

Scene/primitives (Overview/Getting Started): Scene menu adds primitives; presets include demos and character components. Background menu: reference images. Painting: PBR vertex painting (color + roughness/metalness channels). Symmetry menu: manage the mirror plane of the current mesh. Layers menu: per-object layers. History: undo/redo stack options.

### 3D-Coat (Pilgway) — evidence layer A (official documentation)

Positioning ("Why 3DCoat is Unique?"): "considering the breadth of pipeline coverage, 3DCoat can be regarded in some sense as the optimum golden mean between Blender, ZBrush, and Substance Painter, offering comprehensive professional capabilities in sculpting, retopology, UV editing, texturing, and photogrammetry... Thus, it covers the entire cycle (sculpt → retopo → UV → PBR texturing → export)." Also claims "true volumetric painting" on voxels as unique.

Rooms architecture (Workspaces Rooms, directly observed): "View each Room or Workspaces as a 'mini-application' connected through and through. The structure helps you to concentrate on one operation at a time." Rooms documented: Sculpt, Retopology, UV, Paint, Render, Tweak, Modeling ("The Retopo room is designed to create a low poly mesh based on a sculpt mesh. The modeling room... intended for modeling a low poly mesh without a sculpt mesh"), Kitbash, 3DPrint, Photogrammetry (RealityCapture integration), Nurbs, Nodes. "Retopo room and UV room are pre process and post process of UV creation/editing."

Sculpt room (Sculpt page, directly observed): "This room is home to some of the tools and features of 3D sculpting. The Sculpt Room consists of two working modes, Voxels, and Surfaces (polygons). You can begin in Voxel mode for rough sketches and eventually move your sculpture into Surface mode (for increased performance, memory preservation, and fine detail work). Many of the Voxel Tools lend themselves to freeform 'Brush-Based' sculpting operations, giving the artist the freedom to build with the equivalents of clay, wax, wood, stone, and paint. 3DCoat also makes full use of the possibilities of your graphic tablet." Surface mode has "Dynamic Subdivision built into the brushes", stores **Sculpt Layers**, and voxel edits can be projected onto a Surface copy; "both platforms have their own unique features... which is why we make it easy to switch between them at any point." Voxel mode notes: memory/processor intensive; "If you'd like to preserve the different stages of modeling as represented by resolution (from low to high), simply duplicate a layer before applying 'Res+' (Resampling)". "Voxel volumes does not support Layers." Sculpt Layers Panel stores "different versions of your sculpture, as well as parts of the model that need different and separate features and detail... transferred into different PolyGroups... and ultimately to the Paint Workspace for final displacement, bump and color texture creation." Surface-mode "Remove stretching" tool "remeshes directly beneath the brush... bringing much of the dynamic Tessellation features in Brushes to the Standard Surface mode brushes." Transform tools in Sculpt room: Transform, Instancer, Move, Pose, Fit, Reproject, Surface Array. Also: Primitives, Live Booleans, Sculpt curves (spline-based), Vector Displacement brushes. Statistics panel shows voxel-sculpture stats. Autopick lets the user start sculpting on a new object without selecting its layer first.

Brush machinery (Brush Components chapter, TOC directly observed): Brushes + alphas (create alpha brushes and decals; make alpha from current sculpt; create a brush from a 3D object; curve-based brushes; load Photoshop .abr brushes), Strokes, Brush Options panel, Conditions (Height/Color) limiter, Strips, Stencils, Smart Materials, presets.

Retopology room: manual retopo tools plus AUTORETOPO (automatic), poly groups, and a Bake menu that transfers sculpt detail to the new mesh. Paint room: per-pixel, micro-vertex (displacement), Ptex and surface (vertex) painting modes; smart materials; texture baking. Free 3DCoatPrint: "Compact free application with one primary goal – let you create your models for 3D-printing as easily as possible." Applinks documented for Blender, 3ds Max, Houdini, Lightwave.

---

## Cross-product Comparison

| Dimension | ZBrush | Blender Sculpt | Nomad Sculpt | 3D-Coat |
|---|---|---|---|---|
| Packaging | dedicated desktop+iPad app | one mode inside a full 3D suite | dedicated app, mobile-first + desktop | dedicated app organized into rooms spanning sculpt→retopo→UV→paint→render |
| Sculpted object | polygon mesh (polymesh/ZTool), optional 2.5D canvas heritage | polygon mesh | polygon mesh (tris+quads) | voxel volume OR polygon surface; switchable; edits projected between |
| Detail strategy | subdivision levels + HD geometry + dynamic subdivision; DynaMesh remesh; Sculptris Pro dyntopo | multires subdivision + dyntopo (+ remesh per homepage copy) | multiresolution + voxel remesher + dyntopo (three explicit methods) | voxel resampling ("Res+") in voxel mode; multires in surface mode; per-brush dynamic remesh |
| Brush palette | 200+ proprietary brushes (vendor claim); Smooth/Curve/Insert-Mesh/VDM/Alpha families | built-in set (Crease, Clay Strips, Pinch, Grab, Smooth, Mask...) + custom | categorized toolbox (Clay, Brush, Smooth, Layer, Inflate, Nudge, Stamp, Move, Drag, Flatten, Planar, Crease, Pinch, Trim, Split, Project...) | voxel + surface toolsets; brush engine with alphas/strokes/stencils/conditions |
| Stroke controls | size/strength/falloff/alpha/stroke + Lazy Mouse, brush noise | brush settings (manual unreachable; feature page confirms customizable brushes) | radius + intensity + Sub mode + falloff/alpha/stroke via Stroke menu + pressure page | brush top bar + options panel + strokes + stencils + conditions |
| Symmetry | symmetry incl. dynamic symmetry | "Mirrored sculpting" | mirror plane, on by default for new sculpts | Symmetry menu (app-wide) |
| Masking | masking chapter (by polypaint, region) | masking + hiding (feature page) | mask tool; masked areas protected from sculpt & paint; masks→geometry | Freeze menu (freeze = 3D-Coat's protect mechanism, observed in menus); conditions limiter |
| Layers | 3D Layers | (suite has modifiers/shape keys — out of sampled scope) | per-object layers; exported via glTF morph targets | Sculpt Layers in surface mode; "Voxel volumes does not support Layers" |
| Posing/transform | Transpose/Gizmo 3D/Deformers, Transpose Master | suite gizmos | Transform/Gizmo/Move/Drag tools | Transform/Move/Pose/Fit/Reproject/Instancer |
| Base mesh creation | primitives, ZSpheres, ShadowBox, mannequins, Live Boolean, Snapshot3D | suite primitives | scene primitives + Tube/Lathe/Insert tools | primitives, kitbash, live booleans, spline curves |
| Retopology | ZRemesher auto + manual retopo + Topology Brush; detail transfer | retopology in modeling toolset (feature page) | Quad Remesher tool + decimation + UV unwrap + bake | dedicated Retopo room (manual + AUTORETOPO) + bake menu |
| Painting | PolyPaint (no UVs) + texture maps | "3D painting with textured brushes and masking" | paint tool (color + PBR vertex painting) | full Paint room (per-pixel/micro-vertex/Ptex/surface) |
| Map output | displacement/normal/vector-displacement maps on export | bake workflow (suite) | bake→texture (normal/rough/metal/color) | Retopo bake + paint bake |
| Multi-object | SubTools + folders | scene objects | scene objects (solo/x-ray) | objects/layers/voxel objects |
| 3D print support | Ready for Print (draft analysis etc.) | (export via formats) | STL export + decimation tip | 3DPrint room + free 3DCoatPrint product |
| Rendering | BPR + Redshift integration | Cycles/Eevee (suite) | PNG render + post-processing | Render room |
| Formats | standard 3D geometry + image formats + GoZ | (glTF/USD/OBJ/FBX/Alembic per pipeline page logos) | NOM/glTF/OBJ/USD/PLY/STL/FBX import-export matrix | standard + applinks |
| Business model | subscription (incl. iPad in plan) | free, open source | one-time purchase per platform (~US$35 desktop observed on purchase dialog) | perpetual + subscription; lite/derived products (3DCoatPrint/Textura) |
| Customer tier | studios/pro artists | everyone; small studios prosumer→studio | hobbyists/prosumers/mobile pros | professionals; pipeline-oriented studios |

### What repeats across all four (layer B)

1. The unit of work is a **brush stroke applied directly to a 3D surface**; every product's core vocabulary is brushes (Clay/Brush, Smooth, Pinch/Crease, Inflate, Move/Grab, Flatten/Planar, plus cut/trim-style tools).
2. Per-stroke controls: **size/radius + strength/intensity**, with falloff/alpha/stroke-style options and stylus-pressure support.
3. **Symmetry (mirroring)** is available in all four; in Nomad it is default-on for new sculpts.
4. **Masking/protecting and hiding** surface regions is available in all four.
5. **Topology-management machinery** to add detail without hand-editing topology: subdivision levels/multires, dynamic tessellation, remesh/voxel — at least two of the three in every sampled product.
6. **Base-mesh creation**: primitives at minimum; several richer silhouette/skeleton approaches.
7. **Transform/gizmo + move/pose** tools separate from surface brushes.
8. **Multiple objects** per scene/project with show/hide/solo.
9. **Undo/history**.
10. **Import/export of standard 3D formats**; the artifact leaves the app as geometry (and often as baked maps).
11. **Painting on the surface** (vertex/polypaint at minimum) exists in all four.
12. **Reference images / background** support (observed in ZBrush Reference Images, Nomad Background menu, 3D-Coat back references; Blender common practice — treated as common, not definitional).
13. A **prepare-for-hand-off step**: retopology or decimation, UV, and detail baking exist in all four in some form (essential for the film/game pipeline; skippable for 3D printing).

### Defining-core candidates and their status

| Candidate | Verdict | Reason |
|---|---|---|
| 3D surface under direct brush deformation | **Defining (L0)** | every product's primary interaction; removing it leaves a generic 3D viewer |
| Brush-as-primary-instrument vs component editing | **Defining (L0)** | the clay analogy is the vendor-positioning core in ZBrush ("actual clay"), Nomad ("3d sculpting app"), 3D-Coat ("Brush-Based sculpting... equivalents of clay, wax, wood, stone"); Blender's dyntopo copy frames sculpting vs "regular sculpting only affects the shape" |
| Result persists and is exportable as a 3D model | **Defining (L0)** | all four export standard formats; without it the app is a demo toy |
| Symmetry | Common (L1) | default-on in Nomad, but sculpting asymmetric objects (busts, props) is normal |
| Masking | Common (L1) | universal in sample, but a minimal sculptor (lite editions) can work by hiding/isolating |
| Subdivision levels / multires | Common (L1) | absent in voxel-mode sculpting (3D-Coat voxel) and in dyntopo-only flow |
| Dynamic tessellation | Common (L1) | absent as such in classic subdiv flow (ZBrush default path) |
| Voxels | Common (L1) | only one sampled product uses voxels as a primary mode |
| Layers | Common→Optional (L1/L2) | "Voxel volumes does not support Layers" (3D-Coat) proves non-universality |
| Paint/color | Common (L1) | all four have it, but the Type is defined by shape, not color |
| Retopo/UV/bake | Common (L1) | pipeline machinery; not required for print-oriented sculpting |
| Pressure/stylus | Common (L1) | recommended/everywhere, but desktop mouse workflows documented (ZBrush FAQ runs with mouse+keyboard; Nomad has desktop without stylus) |
| Rendering, lighting, materials depth | Optional (L2) | varies from viewport-only to built-in production renderers |
| Suite integration, applinks, bridges | Optional/vendor (L2/L3) | GoZ, Applinks, Substance Bridge are vendor mechanisms |

## Canonical Abstraction

### L0 — Defining Invariant

A Digital Sculpting Application is:

1. **A persistent 3D surface** — a polygonal (or voxel-equivalent) surface object that is the model being shaped.
2. **Brush-driven direct deformation** — the primary way the model changes is applying adjustable brush-like tools along strokes on the surface (build up / remove material, push, pull, smooth, pinch, inflate, move regions), with size and strength under the user's control.
3. **The shaped result is a 3D model** — the sculpt persists in a native project and can be exported as standard 3D geometry for downstream use.

Test: remove any one and the Type stops being recognizable — no surface = nothing to sculpt; no brush-deformation = it is a component/parametric modeler or a viewer; no exportable 3D model = it is a display/render toy, not a sculpting application.

Historical / market-sample check: the definition does not depend on the modern bundle. The vendors' own lite/beginner editions (e.g., ZBrushCoreMini, documented in the same help system as a simplified interface) and the earliest widely-adopted dedicated sculptors (the Sculptris lineage, named inside ZBrush's own docs as "Sculptris Pro" mode) operated on a single mesh with a small brush set, symmetry, and export — squarely inside L0 without layers, retopology suites, VDM brushes, or rendering. Platform-native variants (iPad-only sculpting, Android) also fit. The canonical abstraction therefore sits above subdivision levels, voxels, dyntopo, masks, layers, paint, and retopo — all of which are implementation or maturity layers.

### L1 — Common Mature Structure

- Brush/tool palette with the shared operation families: build-up (clay/brush), carve/remove, smooth, pinch/crease, flatten/planar, inflate, move/grab/drag, stamp/alpha, and cut/trim/split-style shaping.
- Per-stroke controls: radius/size, intensity/strength, falloff, alpha/stamp, stroke style; stylus-pressure mapping.
- Symmetry/mirroring of strokes.
- Masking and hiding of surface regions (protection + isolation).
- Detail-resolution machinery: subdivision levels/multires, dynamic tessellation, remesh/voxel — so artists "stop thinking about topology" while sculpting.
- Base-mesh creation: primitives, plus silhouette/skeleton-based starters (ZSpheres/ShadowBox/mannequins-class tools, primitives, spline curves).
- Multiple objects in one project (SubTools/objects/layers) with visibility controls.
- Transform/gizmo and move/pose tools for global shape and posing.
- Undo/history.
- Surface painting (vertex/polypaint-class) and viewport shading/materials.
- Hand-off preparation: retopology or decimation, UV generation, baking detail into maps or a lower-res mesh; export to standard 3D formats (OBJ/glTF/STL/PLY/FBX-class).
- Reference-image support.

### L2 — Variant / Optional Structure

- Topology representation strategy: classic base-mesh + subdivision levels; dynamic tessellation; voxel sculpting; dual-mode with projection between modes.
- Packaging: dedicated sculpting app; sculpting mode inside a full 3D suite; rooms-based pipeline app covering sculpt→retopo→UV→paint→render.
- Platform: desktop workstation, tablet/mobile-first, web demo.
- Business model: subscription, free/open-source, one-time purchase, perpetual.
- Customer tier: studio production vs prosumer vs hobbyist/education; lite editions.
- Domain emphasis: characters/creatures, collectibles/3D printing, jewelry/product design, concept art, hard-surface sculpting.
- Rendering depth: viewport matcap-class shading only, up to integrated production renderers.
- Import/export format depth; per-format feature loss (e.g., layers survive only in some formats).

### L3 — Vendor-specific (research notes only)

ZBrush: Pixol/2.5D canvas document model, ZTools, DynaMesh, Sculptris Pro, ZSpheres/ZSketch/Mannequins/ShadowBox, ZModeler, Live Boolean, Snapshot3D, FiberMesh, MicroMesh/NanoMesh/Array Mesh, cloth brushes, Transpose/Transpose Master, ZRemesher 4.0, UV Master/SpotLight/MorphUV/ZAppLink, GoZ, MatCap/LightCap/BPR, Redshift-in-ZBrush, polygroups machinery, Lazy Mouse 2.0, vector-displacement (VDM) brushes, Surface Noise/NoiseMaker, Slime Bridge, Thick Skin, BevelPro, Ready-for-Print draft analysis, ZBrushCore/Mini editions, iMage3D, Projection Master, Morph Targets, HD Geometry, 200+ brushes claim, dual desktop+iPad licensing.
Nomad: .nom project format, per-tool Sub (sticky) modes, sticky shortcuts (Smooth/Mask/Hide/Gizmo/Color/Alpha), Trim/Split/Project camera-projected cut tools with hole-filling options (Boolean/Legacy/Fill), facegroups + mask-to-facegroup, dyntopo detail modes (screen/radius/constant) + uniformisation/subdivision/decimation methods, UVAtlas vs BFF unwrap pair, bake matrix (normal/roughness/metalness/color/emissive/opacity), reproject-to-vertex, vertex-PBR channel packing, per-format export matrix, Quad Remesher tool, web demo, per-platform purchases, license activation by machine.
3D-Coat: rooms architecture, voxel + surface dual-mode Sculpt room, Clay Engine, Res+ resampling, Sculpt Layers/Tree, AUTORETOPO, retopo bake, Paint room modes (per-pixel/micro-vertex/Ptex/surface), Smart Materials, Conditions (height/color) limiter, Strips/Stencils, Photoshop .abr brush import, Quixel Megascans import, voxel volumetric-painting claim, Applinks (Blender/Max/Houdini/Lightwave), 3DCoatPrint/Textura derivatives, NGL node system, RealityCapture integration.
Blender: Sculpt workspace/mode inside the suite, add-on/Python extensibility, suite pipeline integration (Cycles, geometry nodes context).

## Vendor-specific Findings → rejected from core

- "200+ brushes" (ZBrush page) — marketing scale; Nomad ships a small categorized set and is fully a sculpting app.
- Voxels as the sculpting substrate — 3 of 4 products are polygon-first; 3D-Coat treats voxel as one of two modes.
- 2.5D canvas/pixol document model (ZBrush heritage) — not present elsewhere.
- Rooms architecture (3D-Coat) — organizational choice, not Type structure.
- GoZ/Applinks/Substance bridges — vendor interop mechanisms.
- Machine-activation licensing, per-platform purchases (Nomad FAQ) — commercial detail.

## Boundary Findings

1. **vs 3D Modeling Application (the sharp seam).** Modeling applications change shape by constructing/editing discrete components and operations (primitives, extrude/bevel/booleans, vertex-edge-face editing); sculpting applications change shape by brush deformation of the surface as a continuum. Evidence of the seam: Blender's own copy puts them "side by side" as separate toolsets; 3D-Coat separates the Sculpt room from the Modeling room ("The Retopo room is designed to create a low poly mesh based on a sculpt mesh. The modeling room... for modeling a low poly mesh without a sculpt mesh"); ZBrush ships ZModeler (polygon modeling) as a secondary capability beside its brush core. Discriminator: what is the *primary* instrument — the brush stroke on the surface, or the component operation? Suite products legitimately host both Types as modes. "去掉什么就变成另一个 Type": take away the brush-as-primary-instrument (keep primitives + component editing) and it becomes a 3D Modeling Application.
2. **vs Texture/Material Authoring Application.** Texture authoring paints color/materials onto surfaces (UV/layer stacks); sculpting deforms geometry. Sculpt apps include paint (Polypaint, vertex PBR, Paint room) and export displacement/normal maps — the seam is 3D-Coat's micro-vertex "displacement painting", which blurs into geometry. Discriminator: the primary output — shape vs surface appearance.
3. **vs Digital Painting Application (2D).** Same brush interaction grammar, different medium: pigment on a 2D canvas vs geometry deformation in 3D. Nomad self-describes as "a sculpting and painting application" — a combined product, not a merged Type.
4. **vs Photogrammetry Application.** Photogrammetry derives geometry from captured images; sculpting authors geometry manually. Adjacent enough that 3D-Coat embeds a Photogrammetry room (RealityCapture) — integration, not the same Type.
5. **vs 3D Animation / Character Animation.** Pose tools (Transpose/Pose) pose a static sculpt; they do not manage rigs/timelines/keyframes. Sculpt apps' "rigging" (ZBrush) exists for posing only.
6. **vs Procedural 3D Creation.** Procedural apps generate geometry from graphs/parameters; sculpting is direct manual deformation. ZBrush parametric meshes and gizmo deformers are convenience, not a procedural core.
7. **Internal taxonomy fit.** The leaf sits under "04.13 3D Creation" next to "3D Modeling Application" — research supports these being sibling Types (different primary instruments) rather than alias/variant. No evidence found that Digital Sculpting is merely a capability of 3D Modeling: three of four sampled products are dedicated sculpt-first applications.

## Uncertainties

- Blender Manual inaccessible (403): Blender-specific operational details (exact brush set size today, remesher names, sculpt-layer behavior) are not asserted. The "20 different brush types" figure on the official feature page is dated copy and should not be read as current.
- ZBrush feature-detail body text beyond the TOC was not retrievable (JS shell + JS feature app); precise ZBrush numeric claims (e.g., "tens of millions of polygons") are quoted as vendor claims, not verified facts.
- Nomad's desktop licensing price observed on the purchase dialog (~US$35) may change; treat as point-in-time.
- Historical evidence for Sculptris/Mudbox is indirect (Sculptris Pro named in ZBrush docs; Mudbox not sampled). The historical check therefore leans on lite editions and the vendors' own simplified products rather than on fetched legacy manuals.
- AI-assisted sculpting: no AI features surfaced in the fetched official docs; no claim made.
- 3D-Coat "Why unique" page includes AI-chat-generated comparison copy (the vendor says so itself); used only for the pipeline-coverage claim (sculpt → retopo → UV → PBR texturing → export), which matches the documented room structure.

## Final Synthesis

A Digital Sculpting Application is a 3D content-creation application whose defining core is deforming a persistent 3D surface directly with brush-like tools — the digital equivalent of working clay — and producing an exportable 3D model. Around that core, mature products share a stable layer: categorized brush families, per-stroke controls (size/strength/falloff/alpha/pressure), symmetry, masking/hiding, topology-management machinery (subdiv levels, dyntopo, voxel remesh), base-mesh creation, multi-object scenes, transform/pose tools, undo, surface painting, and a hand-off stage (retopo/decimate, UV, bake, export). Beyond that, products vary by representation (subdiv vs dyntopo vs voxel), packaging (dedicated app / suite mode / rooms pipeline), platform (desktop / tablet), business model, and domain emphasis. The Type's sharpest boundary is with the 3D Modeling Application: same objects, different primary instrument.
