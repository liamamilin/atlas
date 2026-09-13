# Research Notes — Mechanical CAD

Research date: 2026-09-09

## Research Goal

Understand what a Mechanical CAD application is from real products: its core object model, its defining work-mode, how assemblies and engineering deliverables relate to the model, and where its boundaries sit against Industrial Design, generic 3D Modeling, CAM, CAE, PLM, and BIM. This pass also carries two joint-review obligations recorded by earlier passes: the industrial-design-application forward flag (ID/MCAD seam, proposed discriminator = center of gravity) and the 3d-modeling-application flag (precision/engineering-intent gradient).

## Initial Boundary

Working hypothesis before research:

- Core use: define physical components (parts) and whole products (assemblies) as precise engineering geometry, and derive engineering documentation/manufacturing data from that geometry.
- Users: mechanical engineers, mechanical designers, drafters, manufacturing engineers.
- Nearest neighbors: Industrial Design Application, 3D Modeling Application, CAM, CAE / Engineering Simulation, PLM, BIM Authoring, ECAD/EDA, Additive Manufacturing Software.
- Likely confusion: with Industrial Design (both produce precise geometry exchanged via STEP-class formats); with 3D Modeling (both are 3D modelers); with CAM (both serve manufacturing).
- Unknowns: whether "parametric feature tree" is definitional or merely the dominant implementation; whether the drawing module is definitional or replaceable by exported views; how cloud-native products restructure the object model; whether assembly constraints are definitional.

## Research Questions

1. What is the unit of record — the part? the document? the assembly?
2. How is geometry constructed and changed? What carries "design intent"?
3. How do assemblies work — what is a component instance, what do mates/constraints define?
4. How are engineering drawings and manufacturing data produced, and how do they relate to the model?
5. What rules govern regeneration, dependencies, constraint states, and failures?
6. How do variants (configurations) work?
7. How does data exchange happen (neutral formats, native formats), and what survives exchange?
8. What interfaces does the user actually operate?
9. Where is the ID/MCAD seam, structurally?
10. Would older / minimal / differently-positioned products still fit the definition?

## Representative Products

Selected for market representation, documentation reachability, different product philosophies, and different customer tiers:

| Product | Philosophy / tier | Evidence reached |
|---|---|---|
| Onshape (PTC) | cloud-native SaaS parametric MCAD; browser; built-in data management | Tier-1 help center, multiple full topics (2026-09-09) |
| FreeCAD | open-source parametric MCAD; workbench-modular; community | Tier-2 official site + features page (wiki blocked by anti-bot) |
| SolveSpace | minimal open-source parametric 2D/3D CAD | Tier-1 official site (features, manual) |
| Alibre Design | SMB / perpetual-license parametric MCAD; hobby tiers | Tier-2 official product pages (help portal is JS) |
| IronCAD | history-optional direct/parametric hybrid; catalog-driven; single-file scene | Tier-2 official product pages |

Market anchors (official docs unreachable this pass — JS shells or login walls; used only as market context, no product-level claims): SOLIDWORKS, Autodesk Fusion, PTC Creo, Siemens NX, CATIA, Autodesk Inventor, Solid Edge.

## Sources

Fetched 2026-09-09:

- Onshape Help (Tier-1): Getting Started (`cad.onshape.com/help/Content/Home/getting_started_with_onshape.htm`), Part Studios (`/PartStudio/part_studios.htm`), Sketch Tools (`/Sketch/sketch_tools.htm`), Feature Tools (`/PartStudio/feature_tools.htm`), Mates (`/Assembly/mates.htm`), Insert Parts and Assemblies (`/Assembly/insert_parts_and_assemblies.htm`), Modeling In-Context (`/Assembly/modeling_in_context.htm`), Bill of Materials (`/Assembly/bill_of_material.htm`), Drawings (`/Drawing/drawings.htm`), Configurations (`/PartStudio/configurations.htm`), Supported File Formats (`/File/supported_file_formats.htm`)
- SolveSpace (Tier-1): `solvespace.com` (home), `solvespace.com/features.pl`
- FreeCAD (Tier-2): `freecad.org` (home), `freecad.org/features.php`
- Alibre (Tier-2): `alibre.com` (home/product pages)
- IronCAD (Tier-2): `ironcad.com` (home), `ironcad.com/design-collaboration-suite/ironcad/`

Unreachable (recorded per source-access limitation):

- `help.solidworks.com` — JS shell, content not rendered (2 attempts)
- `help.autodesk.com` Fusion — 404 on URL guesses ×2; `autodesk.com` product page 403
- `support.ptc.com` Creo help — 404 redirect ×2
- `wiki.freecad.org` — Anubis anti-bot challenge (site-wide)
- `help.3ds.com` (CATIA) — login wall
- `help.bricsys.com` — JS app shell
- `help.alibre.com` — JS app shell
- Bing/DDG site-scoped queries — mangled or timed out; Bing general search worked

## Product Observations

### Onshape (evidence layer A — direct observation, official help)

- **Document/tabs model**: a document is a project-level container; tabs hold Part Studios, Assemblies, Drawings, Feature Studios, imported files. "Onshape does not use files."
- **Part Studio**: "a container used to create and edit parts, surfaces, and sketches… not a model, rather a design environment." Contains Feature toolbar, **Feature list** (the parametric history), **Rollback bar** (repositionable to regenerate the list up to that point), Parts list, default planes (Top/Front/Right) + Origin (cannot be deleted, can be hidden).
- **Sketching**: sketch tools create 2D geometry (line, rectangle, circle, arc, spline, construction); constraints including dimensions can be applied between sketch curves and planes; non-fully-constrained points display in blue/red vs black when fully constrained; expressions and trig functions allowed in numeric fields.
- **Features**: feature tools "create, modify, or manipulate 3-dimensional geometry to create new parts"; canonical loop: base geometry → select tool → select geometry → input parameters → preview slider → accept. Categories include extrude, fillet, pattern, boolean, modify, planes.
- **Assemblies**: insert instances of parts, subassemblies, sketches, surfaces from current document, other documents (linked), or standard content; configurations chosen at insert; released revisions selectable via Reference manager; instances list; default positioning aligns origins.
- **Mates**: "Mates… define the degrees of freedom between those two instances." Mate types: Fastened, Slider, Revolute, Planar, Cylindrical, Pin Slot, Ball, Parallel, Tangent, Width, Group, Rigid. **Mate connectors** are local coordinate systems on entities (implicit from geometry or explicit). Offsets and limits per mate; animate a DOF; Solve computes all mates; DOF indicators (triad icon) show unconstrained instances; Fix is distinct from a mate (assembly-local, doesn't carry over).
- **In-context modeling**: edit a part in its Part Studio while seeing the assembly ghosted around it; assembly context snapshots capture geometry/positions; updates are manual (never automatic); top-down design methods enumerated (in-context, create Part Studio in context, multi-part Part Studios).
- **BOM**: automatically created from any assembly; structured (with subassembly expansion) or flattened; property columns; non-geometric items insertable; export CSV; cross-highlighting with instances.
- **Drawings**: created from Part Studios and Assemblies; DWG/DXF-based; dimension tools (linear/radial/diameter/min-max), notes, projected views, sheets; "Update drawing" command; export PDF/DWG/DXF/SVG/PNG.
- **Configurations**: inputs/options/parameters tables; configure feature parameters (e.g., extrude depth), suppression (e.g., fillet), part numbers, colors, materials; options appear in the Insert dialog.
- **Data management**: automatic save; "automatic and infinite history and restore points"; immutable versions, branching, restore to any point (Version Manager); release management with revisions, part numbers, states (In progress/Pending/Rejected/Released).
- **Collaboration**: simultaneous editing on the same part; follow mode; comments.
- **FeatureScript**: "the programming language that all Onshape features are built with"; users can define custom features.
- **Interop**: imports Parasolid (preferred), ACIS, STEP AP203/214/242, IGES, plus native formats of SOLIDWORKS, Inventor, Creo, NX, Solid Edge, CATIA v5, Rhino; meshes (STL/OBJ) view/reference only, "unable to edit a mesh"; exports STEP (with MBD data), IGES, Parasolid, STL, 3MF, JT, URDF; drawings to PDF/DWG/DXF/SVG.
- **Analysis surfaces**: Measure tool, Mass Properties tool (requires material assignment for mass).

### FreeCAD (evidence layer A for its own claims; Tier-2 official site)

- "Open-source parametric 3D modeler made primarily to design real-life objects of any size."
- "Parametric modeling allows you to easily modify your design by going back into your model history and changing its parameters."
- Real-world units throughout; "full-precision models"; export for 3D printing or CNC machining; "create 2D drawings and views of your models"; FEA; export quantities/BOM.
- Geometry kernel: Open CASCADE; solids, BRep, NURBS; Boolean operations, fillets.
- "All FreeCAD objects are natively parametric" — shape based on properties; recalculated on demand; undo/redo; "maintain a precise modelling history"; properties of one object can drive another (parametric chains).
- Sketcher: constraint-solver; "sketches are the main building block"; constrained 2D shapes feed Part Design workbench and others.
- Assembly: built-in Assembly workbench since 1.0 (Ondsel solver) — "define 3D constraints between parts, assemble the different components of a model, and animate"; previously community add-on assembly workbenches with different solvers.
- Workbenches: Part (CSG), Draft (2D), Surface, BIM, Path (CAM/CNC), FEM, Robot, OpenSCAD.
- Formats: STEP, IGES, STL, OBJ, DWG, DXF, SVG, IFC, native FCStd; dozens more.
- Python everywhere: console, macros, custom workbenches.

### SolveSpace (evidence layer A — direct observation, official site)

- "A free (GPLv3) parametric 3d CAD tool." Applications listed: modeling 3D parts (extrudes, revolves, helixes, Booleans), 2D parts (single section exported as DXF/PDF/SVG, "use 3d assembly to verify fit"), 3D-printed parts (STL), preparing CAM data (STEP/STL for third-party CAM; 2D vector for waterjet/laser), mechanism design (constraint solver for planar/spatial linkages with pin/ball/slide joints).
- Sketch: lines, rectangles, datum lines/points, circles, arcs, Bezier/splines, text as vectors, trims, tangent arcs (fillets), construction geometry, snap grid, background image tracing.
- Constraints/dimensions: distance, projected distance, angle, tangency, parallel, perpendicular, horizontal/vertical, equal length/angle/radius, ratio, point-on-line/circle/face, midpoint, symmetry; metric/inch; lengths as arithmetic expressions.
- Solids: extrude, lathe (solid of revolution), helix from a sketch; Boolean union/difference/intersection; parametric step-and-repeat (pattern); operations on meshes or NURBS surfaces.
- Assembly: "parametric and associative assembly — link parts and drag them with six degrees of freedom… place parts in assembly using constraints… changes in parts propagate automatically into assembly."
- Analysis: measurements (point/line/face distances, angles), mechanism path trace exportable to spreadsheet, sketch area, solid volume, **degrees-of-freedom check showing unconstrained points in sketch**, **interference check for assemblies**, STL check.
- Export: 2D vector drawing as DXF/EPS/PDF/SVG/HPGL/STEP (hidden-line removed, sections, isometric/orthogonal views); toolpath as G code; 3D wireframe DXF/STEP; triangle mesh STL/OBJ; NURBS surfaces STEP; shaded bitmap.
- No persistent associative drawing document — drawing output is exported views. No BOM, no PDM, no configurations panel.

### Alibre Design (evidence layer A-lite; Tier-2 official product pages)

- Positioning: "Powerful & Affordable 3D CAD Software"; business-class CAD ("design, document, communicate, and maintain your engineering portfolio"); hobby tiers (Atom3D; Workshop CAD/CAM).
- Precision Modeling: "Create components of any complexity with a huge 3D feature set alongside an epic sketching environment. Precision is built into everything, and models can be easily edited repeatedly."
- Sheet Metal: dedicated environment; "instant flat patterns"; conversion of regular models to unfoldable sheet-metal models.
- Assembly Modeling: "Bring components together and represent the full digital prototype. See and simulate realistic motion including gears, pulleys, and screws. Create exploded views that can be consumed later in 2D documentation."
- Drawings: "Create perfect 2D documentation for individual components and assemblies… confidence with manufacturing and patents."
- Rendering; Python-based scripting; PDM ("versioning, where-used, rollback, search, rich metadata, backups, multiple users, local deployment").
- File formats: import SOLIDWORKS, Inventor, Pro/E-CREO, CATIA, Solid Edge, NX, Rhino, STEP, SAT, IGES, Parasolid, DWG, DXF, SVG; export STEP, SAT, IGES, STL, OBJ, Parasolid, ZPR, JT, DWG (2D), DXF (2D), SVG, PDF (2D & 3D).

### IronCAD (evidence layer A-lite; Tier-2 official product pages)

- "IRONCAD is a desktop 3D and 2D design program that allows users to choose from **parametric, direct, or a combination of both modalities on demand** in a single environment."
- "Make design changes when you want… IronCAD empowers you to model **with or without history-dependency**."
- Interaction: patented TriBall positioning tool; resize by stretching handles; "drag and drop predefined shapes into the design scene"; catalogs of predefined shapes/parts/assemblies for reuse.
- Data model: "3D models made in IRONCAD only require one file, no matter how complex. Assembly part data is integrated into a file's unified design environment, rather than linking to external files."
- Suite: IRONCAD (3D+2D), INOVATE (3D design/collaboration), DRAFT ("2D Detailing and 3D Collaboration"), COMPOSE (viewing/configuration); design extensions: IronCAD Mechanical, Multiphysics, SimWise Motion, NestIt, KeyShot, Translators.
- Solutions: machinery, modular, sheet metal, part, tooling design; configuration solutions.

## Cross-product Comparison

| Structure | Onshape | FreeCAD | SolveSpace | Alibre | IronCAD |
|---|---|---|---|---|---|
| Precise part model of record (real-world scale) | ✓ Part Studio parts | ✓ full-precision solids | ✓ solids/NURBS/mesh | ✓ "precision built into everything" | ✓ |
| Sketch + constraints/dimensions → features | ✓ | ✓ Sketcher/PartDesign | ✓ | ✓ sketching environment | optional (parametric or direct modality) |
| Editable definition / history with regeneration | ✓ Feature list + rollback | ✓ modeling history, recalc on demand | ✓ parametric | ✓ "edited repeatedly" | optional history-dependency |
| Assembly of component instances with constraints | ✓ mates (DOF-based) | ✓ Assembly WB constraints | ✓ constraints, 6-DOF drag | ✓ assembly + motion | ✓ (positional; TriBall; catalogs) |
| Model-derived engineering drawings/views | ✓ Drawing tabs (DWG-based) | ✓ 2D drawings and views | ✓ exported hidden-line vector views | ✓ drawings module | ✓ IronCAD Draft |
| Manufacturing-facing exchange | ✓ STEP/IGES/Parasolid/STL/3MF/JT | ✓ STEP/IGES/STL/CNC | ✓ STEP/STL/G-code | ✓ STEP/IGES/STL/JT/Parasolid | ✓ Translators |
| Configurations / variants | ✓ configurations | (parameter machinery; not confirmed this pass) | (expressions only) | (not confirmed) | ✓ configurator (Synergy, suite-level) |
| BOM from assembly | ✓ auto BOM | ✓ BOM/quantities export claim | ✗ | (not confirmed) | (not confirmed) |
| Data management (versions/revisions) | ✓ built-in versions + release mgmt | (not confirmed) | ✗ | ✓ PDM product | ✓ Synergy Vault (suite) |
| Embedded simulation | (mass properties; simulation separate) | ✓ FEM workbench | ✓ DOF/interference checks | ✓ FEA add-on | ✓ Multiphysics add-on |
| CAM | ✗ (separate products) | ✓ Path workbench | ✓ G-code export | ✓ EZ-CAM / Workshop bundles | ✓ NestIt (nesting) |
| Sheet metal | (in-type capability class) | (not confirmed this pass) | ✗ | ✓ dedicated environment | ✓ solution page |
| Scripting/automation | ✓ FeatureScript | ✓ Python | ✗ | ✓ Python scripting | (not confirmed) |
| Real-time collaboration | ✓ simultaneous editing | ✗ | ✗ | ✗ | (suite-level) |
| Deployment | cloud/browser + mobile | desktop (Win/Mac/Linux) | desktop | desktop | desktop |

Reading of the table:

- The first five rows hold across **all five products** — including the two poles (SolveSpace minimal, IronCAD history-optional). These are the invariant candidates.
- Parametric feature-tree *as a specific UX* (ordered feature list, rollback) is universal in four products but explicitly optional in IronCAD ("with or without history-dependency"). The invariant must be phrased as the *concept* (intent-carrying editable definition) rather than the implementation (feature tree).
- The drawing deliverable appears in two realizations: a persistent drawing document associated with the model (Onshape, Alibre, IronCAD Draft, FreeCAD TechDraw-class) vs exported model views (SolveSpace). The invariant is "model-derived engineering deliverables," not "drawing module."
- Everything from configurations down varies in presence and depth → L1/L2, not core.

## Canonical Model (L0–L3)

### L0 — Defining Invariant (four jointly-held structures)

1. **The engineering model of record.** Precise, real-world-scale geometry of physical components (parts), maintained inside the application as the authoritative definition of what will be manufactured. The model — not a document about the model — is the artifact of record. *Remove → concept/illustration 3D modeling or a precision geometry engine with no product meaning.*

2. **Intent-carrying editable definition.** The model is built and changed by editing a structured definition — sketches with constraints and dimensions, features, parameters, properties — such that an edit to the definition recomputes dependent geometry. Design change is a definition edit, not a re-shape. *Remove → freeform-only shaping (industrial-design / artist-DCC territory), or a one-shot geometry tool.*

3. **Assembly-level product structure.** Component instances are brought into defined positional/functional relationships (assembly constraints / mates) so that the model defines a whole product — including its degrees of freedom — not merely isolated parts. *Remove → single-part modeler; a scene of loosely arranged bodies.*

4. **Model-derived engineering deliverables.** Engineering drawings/views and manufacturing-facing outputs are generated from, and remain associated with, the model; the model drives the deliverables. *Remove → standalone drafting (the drawing becomes the record) or a visualization tool with no engineering handoff.*

Jointly-held load-bearing checks:

- 1 alone = precision geometry engine / generic 3D modeling.
- 2 without 1 = abstract parametric machinery (procedural-3D territory).
- 3 without 1+2 = block/scene arrangement (generic 3D layout).
- 4 without 1–3 = standalone 2D drafting.
- 1+2 without 3 = part-only modeler (niche pole; not the market's center).
- 1+3 without 2 = pre-parametric generation / pure direct modeling (historical/variant pole — see historical check).
- 1+2+3 without 4 = modeling with no engineering handoff (3D-modeling territory).

### L1 — Common Mature Structure

- **Parametric feature-based construction as the dominant work-mode**: sketch → feature → ordered feature tree; dimensions/constraints as driving parameters; regeneration on edit; parent-child dependencies; rollback. Universal in the sampled modern products; explicitly optional in the direct-modeling pole.
- **Configurations/variants** of parts and assemblies (named option sets driving feature parameters, suppression, properties).
- **BOM generation** from the assembly (structured/flattened, property columns, non-geometric items).
- **Mass properties / measurement / interference checking** on parts and assemblies.
- **Neutral-format exchange** (STEP/IGES-class; Parasolid/ACIS kernels) plus native-format import of other MCAD systems; mesh formats (STL/3MF) for printing as a secondary path.
- **Sheet metal design** (dedicated feature set, flat patterns) in mature mechanical products.
- **Data management**: versions/revisions either built in (cloud-native) or via companion PDM.
- **Standard content libraries** (fasteners, standard parts) and reusable catalogs.
- **Rendering/visualization** of the model for communication.

### L2 — Variant / Optional Structure

- Deployment: cloud-native SaaS vs desktop; file-based vs database/document container; browser/mobile clients.
- Modeling modality: history-based parametric vs direct editing vs hybrid on demand (IronCAD pole); multi-part single-history containers vs one-part-per-file (Onshape best-practice vs IronCAD single-file scene).
- Integrated CAM/CAE: embedded workbenches (FreeCAD Path/FEM), bundled add-ons (Alibre EZ-CAM/FEA, IronCAD Multiphysics), or separate products (Onshape-class); integration depth is packaging.
- Scripting/automation: FeatureScript, Python consoles/macros, API.
- Collaboration depth: real-time co-editing and follow mode (cloud pole) vs file-based handoff.
- Release/change management formality: built-in release workflows vs external PLM/PDM.
- Industry packaging: machinery, tooling, sheet metal, mechanism design emphasis.
- 2D drafting strength: dedicated 2D detailing products/modules (IronCAD Draft) vs drawing tabs vs exported views.

### L3 — Vendor-specific (research notes only)

- Onshape: Documents/Tabs container; FeatureScript; Version Manager; mate-type naming (Fastened/Slider/Revolute/…); Standard Content; in-context "references never lost" claim; rollout of release states.
- IronCAD: TriBall; catalog drag-drop; single-file unified scene; COMPOSE viewer/configurator.
- FreeCAD: workbench architecture; Ondsel solver; community add-on assembly workbenches; FCStd format.
- Alibre: Atom3D/Workshop tiering; EZ-CAM bundling; local PDM.
- SolveSpace: linkage-mechanism simulation focus; HPGL export; no drawing document.

## Vendor-specific Findings

- Onshape's "Documents, not files" container and built-in versioning/release management are product architecture, not Type structure — a desktop file-based MCAD (Alibre, IronCAD) is equally in-type.
- IronCAD's "with or without history-dependency" is the clearest market statement that the feature tree is a modality, not the invariant.
- SolveSpace's exported-views deliverable (no persistent drawing document) shows the drawing leg must be phrased as "model-derived deliverables," not "drawing module."
- Onshape's mate model (one mate embeds the DOF between two instances; mate connectors as coordinate systems) differs from classical constraint-based assembly mating — implementation variance within the same concept.

## Boundary Findings

### vs Industrial Design Application (joint review — RATIFIED with sharpening)

The industrial-design pass proposed a center-of-gravity discriminator: ID = form/appearance exploration (freeform precision, direct fluid editing, design communication as deliverable); MCAD = engineering function definition (parametric feature trees carrying controlled change, assemblies, engineering drawings/manufacturing data as deliverables). **This pass ratifies the seam and grounds it structurally:**

- MCAD's L0 includes **assembly-level product structure with constraint/mate-defined relationships and degrees of freedom** — sampled ID products do not carry constraint-mated assemblies as a defining structure.
- MCAD's deliverable chain is **model-associated engineering drawings + manufacturing data**; ID's deliverable chain is renderings/design communication + geometry-preserving exchange toward engineering.
- The work loop differs: ID = form-first fluid iteration (their L0 leg 2); MCAD = intent-carrying structured construction where change is a definition edit (this pass's L0 leg 2).
- Hybrid products exist at the seam (integrated cloud product-development suites bridging concept and engineering; ID products shipping optional parametric capability). Center of gravity still discriminates: what the model is *for* — appearance/form definition vs engineering function definition. Keep both Types. The inverse straddle (engineers doing form studies in MCAD) is not counter-evidence.

### vs 3D Modeling Application (§04.13 flag — RATIFIED keep-both)

The 3d-modeling pass flagged a precision/engineering-intent gradient (SketchUp-class architecture-leaning modelers straddle toward CAD; 3D suites merely import CAD formats). This pass resolves: the seam is **destination + product structure + associative deliverables**. Artist/scene-oriented 3D modelers lack constraint-based assemblies, DOF semantics, and model-associated engineering drawings; MCAD lacks (as its center) scene/animation/content concerns. CAD-format *import* in 3D suites is interop, not identity. Keep both.

### vs Procedural 3D Creation Application

The procedural-3d pass noted history-based parametric CAD satisfies its legs (rule structure as content of record). Resolution: **domain binding + what the record is for**. Procedural-3D authors generative rules whose output is 3D content (media/asset); MCAD maintains an engineering definition of a physical product whose regeneration serves controlled design change, with assembly structure and engineering deliverables attached. The parametric machinery overlaps; the record's purpose and deliverable chain do not. Keep both.

### vs CAM

MCAD produces and maintains the engineering definition; CAM consumes model geometry to generate toolpaths/machining programs. Integration is packaging (FreeCAD Path workbench, Alibre EZ-CAM/Workshop, IronCAD NestIt, integrated cloud suites): removing CAM leaves MCAD intact; removing part/assembly modeling leaves CAM. Separate Types.

### vs CAE / Engineering Simulation

Simulation analyzes behavior of a defined design; MCAD defines the design. Embedded simulation (FreeCAD FEM, Alibre FEA add-on, IronCAD Multiphysics, suite-embedded simulation) is packaging. Separate Types.

### vs PLM

PLM manages product lifecycle data and processes *above* the model (items, changes, releases across disciplines); MCAD authors and maintains the model itself. Built-in release management (cloud pole) and companion PDM (SMB pole) are data-management packaging whose depth varies widely. Separate Types.

### vs BIM Authoring

BIM authors building-scale element models (walls, slabs, spaces) with construction semantics; MCAD authors mechanical component/product models. One open-source product ships both workbenches (packaging in one binary, distinct centers). MEP/equipment modeling is the overlap zone. Separate Types.

### vs ECAD / EDA

Electrical/electronic design vs mechanical design; co-design handoff (board outline ↔ enclosure) is interop. Separate Types.

### vs Additive Manufacturing Software

Print preparation/orientation/supports/slicing vs engineering definition; mesh/STL export from MCAD is a handoff (and mesh editing is explicitly limited in sampled products). Separate Types.

### Historical boundary note (2D mechanical drafting)

The 2D drafting era (drawing-as-definition-of-record) is this Type's ancestor craft. The modern Type centers the **3D model of record** with derived drawings; a 2D-only drafting tool fails L0 legs 1–3 and sits on the "remove" side of leg 4 (standalone drafting). Recorded as lineage, not folded into the invariant.

## Historical / Market-Sample Check

- **Pre-parametric 3D generation** (early solid/surface modelers with assemblies and associative drawings, before feature-tree parametrics became universal): satisfies legs 1/3/4; leg 2 holds in weaker form (editable definition without full parametric regeneration). Therefore leg 2 is phrased as the *concept* (intent-carrying editable definition), not the feature-tree implementation. The definition names no era machinery. ✓ (with recorded nuance; qualitative — no fetched source for this generation, kept out of the final document's precise claims)
- **Direct-modeling pole** (IronCAD's direct modality; SpaceClaim-class tools): fits legs 1/3/4; leg 2 via dimension/constraint-driven editing without full history. In-type as a modality variant. ✓
- **Minimal pole** (SolveSpace): fits all four legs with no BOM/PDM/configurations/collaboration. ✓
- **Open-source / regional / SMB poles** (FreeCAD, Alibre): fit. ✓
- **Cloud-native pole** (Onshape): fits; its container/versioning architecture is variant, not invariant. ✓
- Anti-overfit: parametric feature tree, configurations, BOM, PDM, sheet metal, rendering, simulation, CAM, real-time collaboration, cloud deployment — all present in the modern market but **none** required by the definition.

## Uncertainties

- SOLIDWORKS / Fusion / Creo / NX / CATIA / Inventor / Solid Edge official documentation unreachable this pass (JS shells, 403/404, login walls). They are carried as market anchors only; no product-level operational claims about them appear in the final document. The sampled five are argued to cover the Type's structural space (cloud-native, open-source modular, minimal, SMB, direct/hybrid poles), but the enterprise tier is evidenced only indirectly (via import-format support lists in sampled products).
- FreeCAD wiki (Tier-1 depth: Part Design, TechDraw, Assembly workbench details) blocked by anti-bot; FreeCAD evidence is Tier-2 official site/features page only.
- Alibre help portal is a JS app; Alibre evidence is Tier-2 product pages only (claims about assembly motion, drawings, PDM are vendor-positioning statements, not operational walkthroughs).
- Configurations/BOM/PDM presence in FreeCAD/Alibre/IronCAD not confirmed at operational depth this pass; treated as L1/L2 with "commonly present" wording only where multi-product evidence exists.
- Pre-parametric-era and 2D-drafting-era statements are qualitative context from general knowledge, not fetched sources; they inform the abstraction but no precise historical claims are made in the final document.
- Whether every mature MCAD ships a *persistent* drawing document (vs exported views): SolveSpace shows the exported-views pole; leg 4 phrased to cover both realizations.

## Final Synthesis

A Mechanical CAD application is the engineering definition environment for physical products: it maintains precise component geometry as the model of record, builds and changes that geometry by editing an intent-carrying definition (constrained sketches, features, parameters), assembles components into a constrained product structure with defined degrees of freedom, and derives engineering drawings and manufacturing-facing outputs from the model. Parametric feature-based construction is the dominant modern work-mode and the practical face of the Type, but the invariant is the intent-carrying editable definition, not the feature tree; the drawing deliverable may be a persistent associative document or exported model views; deployment, data management, collaboration depth, and integrated CAM/CAE are variant packaging. The Type's center of gravity — engineering function definition of a manufacturable product — separates it from industrial design (form/appearance definition), generic 3D modeling (visual/media content), procedural 3D (generative content rules), CAM (machining consumption of geometry), CAE (analysis of the defined design), and PLM (lifecycle data above the model).
