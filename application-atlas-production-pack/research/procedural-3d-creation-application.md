# Research Notes — Procedural 3D Creation Application

Research date: 2026-09-08

## Research Goal

Understand what a Procedural 3D Creation Application is as an Application Type: what the user actually authors, what the system's "world" is made of, how work flows from definition to 3D result, and where the Type ends relative to neighboring 3D Types (modeling, sculpting, animation, material authoring, CAD, game engines, AI generators).

## Initial Boundary

Hypothesis before research:

- Core purpose: create 3D content by defining an explicit procedure (rules, node networks, parameters, scripts) that the application evaluates to produce 3D results; change the definition and the results regenerate.
- Users: technical directors / effects artists in film and games; also designers in architecture and urban planning.
- Nearest neighbors: 3D Modeling Application (direct element editing), Digital Sculpting (brush shaping), 3D Animation (time axis), Texture / Material Authoring (procedural node graphs over 2D output), Mechanical CAD (parametric history with engineering intent), Game Engine (runtime).
- Known flags from sibling passes (must be resolved here):
  - `3d-animation-application` pass: gradient, not a wall — the canonical procedural product is simultaneously a full 3D animation application; split is center of gravity (node-network content generation vs time-varying scene state).
  - `3d-modeling-application` pass: gradient — direct element editing vs rule/node-driven generation; modifier/generator stacks inside direct-manipulation products blur the line.
- Unknowns: Is "node graph" definitional or era machinery? Does the Type include parametric design tools (CAD-adjacent) and domain rule generators (cities, terrain)? Is "procedural inside a general DCC" (modifier stacks) the same Type or a capability?

## Research Questions

1. What does the user author, and what is the content of record — the procedure or the resulting geometry?
2. How does evaluation work: when is it triggered, what is recomputed, what is observable?
3. What data flows through the procedure (geometry model, attributes, groups)?
4. What interfaces exist (network editor, parameter editor, viewport, data tables)?
5. How are procedures packaged, reused, and shared (custom nodes/tools)?
6. How do results leave the procedural context (export, scene formats, embedding in other applications)?
7. Where do simulations fit (procedural setup vs simulated execution)?
8. Where does the script/code layer sit relative to the node graph?
9. Boundaries: vs direct-manipulation modelers, animation, material authoring (2D procedural), CAD parametric, AI generators, game engines.
10. Historical: would pre-node-graph procedural systems (script-driven generation) still fit the definition?

## Representative Products

| Product | Why selected | Evidence level |
|---|---|---|
| SideFX Houdini | The canonical pure-procedural 3D package; studio/VFX customer tier; richest official documentation | A (full official help, 6+ pages fetched) |
| Blender | Procedural machinery embedded inside a general direct-manipulation 3D suite; free/open source; individual-to-studio tier; the "gradient pole" flagged by sibling passes | B (official positioning page only; manual unreachable) |
| Grasshopper (McNeel/Rhino ecosystem) | Parametric visual-programming pole used by AEC professionals; different philosophy (design exploration, precision) and customer base | Market anchor only (all official doc hosts unreachable) |
| Esri CityEngine | Domain rule-driven generator (urban models); enterprise GIS customer tier | Market anchor only (official docs unreachable) |

Deliberately excluded: TouchDesigner-class real-time node-based media environments (boundary pole, discussed in findings only), standalone terrain generators (below-Type tools, discussed in Variants), game engine node editors (behavior logic, not content creation).

## Sources

Fetched successfully (2026-09-08):

- SideFX Houdini 22.0 official documentation:
  - Introduction to Houdini — https://www.sidefx.com/docs/houdini/basics/intro.html (procedural workflow, networks, nodes, parameters, geometry/attributes, digital assets)
  - Cooking — https://www.sidefx.com/docs/houdini/basics/cooking.html (evaluation semantics, update modes, simulation controls)
  - Networks and parameters — https://www.sidefx.com/docs/houdini/network/index.html (nodes as building blocks, wiring, parameter editor, expressions, references, recipes)
  - Geometry — https://www.sidefx.com/docs/houdini/model/index.html (geometry representation map: primitives, points/vertices, attributes, groups, volumes, looping, compiled blocks, programmatic geometry with verbs)
  - Geometry attributes — https://www.sidefx.com/docs/houdini/model/attributes.html (attribute data model, precedence, group-by-attribute, dictionary attributes, VEX/Python access, common attributes)
  - Digital assets — https://www.sidefx.com/docs/houdini/assets/index.html (packaging networks into reusable nodes/tools, versioning, HIP files as plain text for source control)
- Blender — https://www.blender.org/features/ (official positioning: free and open source 3D creation suite; full-pipeline scope; Python API scripting)

Unreachable (recorded per source-access limitation rules):

- Blender Manual (docs.blender.org) — 403 on two URLs (geometry nodes introduction and index). Operational claims about Blender's node-based geometry system are NOT made from memory; Blender is used only as a market anchor at positioning level, plus cross-reference to sibling passes' prior research.
- Grasshopper: grasshopper3d.com (404), docs.mcneel.com (403), rhino3d.com (404). No product-level claims.
- Esri CityEngine: doc.arcgis.com (404, then timeout). No product-level claims.

Cross-references (prior sibling passes in this repo, with their own fetched evidence):

- research/3d-modeling-application.md — Blender modifier stacks / C4D generators recorded as semi-procedural structures inside direct-manipulation products.
- research/3d-animation-application.md — Houdini observed as full 3D animation world (keys/tracks/playback) on a node-graph architecture; KineFX/Cinema 4D MoGraph observations.

## Product A — SideFX Houdini

### Key observations (evidence layer A unless noted)

- Self-description: "an advanced procedural modeling, animation, effects, simulation, rendering, and compositing package. Houdini's power is based on procedural workflows. Working in Houdini involves creating networks of nodes connected together that describe the steps to accomplish a task." (intro)
- Explicit regeneration semantics: "You can go back to previous nodes in the network and change selections, change settings, or swap out assets. The changes automatically propagate through the network to change the final result. You never have to undo or start over..." (intro)
- Explicit non-destructive prototyping posture: "You don't have to throw away work you do while exploring ideas - just reuse parts of the network or reconfigure the network." (intro)
- Procedural scale rationale: "Because Houdini is based on generating things procedurally, it has a lot of tools for managing extremely large and complex scenes, including support for generating/loading geometry, and adding detail at render time instead of keeping everything in memory." (intro)
- Packaging without code: "You can package up networks and make them into new tools with their own interfaces without having to write any code. In Houdini, these tools are called digital assets." (intro); assets support versioning/namespaces; HIP files can be saved as plain text for diffing and source control (assets index).
- Evaluation is a first-class concept with a name: cooking = "evaluating the nodes in the networks to compute the state of the scene in the current frame. Whenever you wire in a new node or change a parameter, Houdini re-evaluates the networks to compute the new outputs." Cook cost is a managed concern: performance monitor, cook cancel (Esc), update modes (Auto Update / On Mouse Up / Manual + Force Update). (cooking)
- Scene built from nodes organized in networks; networks have types; some nodes contain other nodes (containers/subnetworks); "networks are like folders and nodes are like files". (networks index, intro)
- Two-level structure: object/scene level network `/obj` holds top-level objects (geometry objects, lights, cameras) with transform/parenting; geometry subnetworks contain surface (SOP) nodes that generate geometry. (intro)
- Node/parameter machinery: every node has parameters; parameters accept expressions ("computed instead of being static or keyframe animated"); parameter references between nodes; dependencies visualization; recipes (saved parameter/node groups). (networks index)
- Geometry data model: geometry = points/vertices/primitives (polygons, NURBS/Bézier, metaballs…) plus named attributes; "Much of the information that makes up a scene is stored in attributes - hidden data stored on models, primitives, points, and vertices." Position is just an attribute (`P`). Attributes attach at vertex/point/primitive/detail levels with defined precedence; custom attributes are first-class. (intro, attributes)
- Data is inspectable: geometry spreadsheet shows attribute values per node; visualizers render attribute data in the viewport. (attributes, basics index)
- Attribute-driven operations: nodes' Group fields accept patterns selecting components by attribute value (`@foo>5`); conventionally-named attributes (`P`, `N`, `Cd`, `uv`, `v`, `pscale`, `instance`, `piece`, `id`...) are read/written across node types and by renderer/solvers. (attributes)
- Code is a native layer inside the graph: VEX snippet nodes (Attribute Wrangle), Python SOPs, dictionary attributes with a JSON-like data model; "Many geometry (SOP) nodes allow you to use them in Python scripts to generate geometry programmatically" (verbs); compiled blocks execute node chains compiled for parallel speed; looping constructs inside geometry networks. (attributes, model index)
- Network-type taxonomy (vendor-specific naming): OBJ (objects), SOP (geometry), DOP (dynamics), VOP (shader programs compiled to VEX), LOP (USD scene layers), ROP (render outputs/dependencies), CHOP (channel data), COP (image processing), TOP (task/work items for pipelines), APEX (rig graphs). (basics index)
- Simulation is set up procedurally: dynamics networks "set up the conditions and rules for dynamics simulations" (pyro, fluids, Vellum cloth/hair/grains, MPM, destruction, particles, crowds, FEM); live-simulation cooking controls separate sim cooking from static recooks. (basics index, cooking)
- Pipeline reach: TOP/PDG task networks ("data is fed into the network, turned into work items and manipulated... many nodes represent external processes... run on the local machine or a server farm"), HQueue scheduling, Houdini Engine (C/Python APIs + plugins into other applications), machine-learning platform for synthetic data generation. (basics index)
- Heightfields/terrains and Copernicus GPU image processing are network-based domains inside the same package. (basics index)
- Cross-reference from the animation sibling pass: Houdini's animation surface (KineFX/APEX rigging, keys, playback) is conventional; the node-graph architecture underlies it all.

### Reading

Houdini realizes the Type at its purest: the scene file is a web of editable procedures; every visible result is a computed output; re-authoring is the normal editing loop; code and graphs are interchangeable layers of the same procedure. The vendor's own marketing-language-free documentation repeatedly names propagation, non-destructive re-editing, and procedural scale as the reasons the architecture exists.

## Product B — Blender

### Key observations

- Official positioning (evidence layer A at positioning level): "Blender is the free and open source 3D creation suite. It supports the entirety of the 3D pipeline—modeling, rigging, animation, simulation, rendering, compositing and motion tracking, even video editing and game asset creation." Python API available for scripting/custom tools. (blender.org/features)
- Blender official Manual unreachable this session (403 ×2) — no operational claims made here about its node-based geometry system beyond cross-reference.
- Cross-reference (sibling passes, prior evidence): Blender is a direct-manipulation modeler (object mode + modifier stack + editors) that also hosts procedural structures — the modifier stack, and a node-based geometry toolset (Geometry Nodes) — inside the same application. Sibling research records this as the blurring case between modeling and procedural creation.

### Reading

Blender demonstrates that "procedural" can be an embedded subsystem of a direct-manipulation application rather than the whole application's organizing principle. The Type question is about center of gravity: in Blender the geometry remains the content of record for most users, with procedural structures as a layer. This is a Variant posture of the Type (procedural inside a general DCC), and simultaneously evidence that the Type is defined by the authoring model, not by being a standalone product category.

## Product C — Grasshopper (market anchor, degraded evidence)

- All official documentation hosts unreachable this session (404/403/404). Market-anchor status only.
- Market-known position (no product-level operational claims): a visual-programming environment used with Rhino by architects/engineers for parametric/generative design; parameters and components drive model geometry; the de facto AEC pole of the Type.
- Used in this research only to establish: (1) the Type spans beyond entertainment-industry content into design disciplines; (2) the authoring substrate there is also an explicit editable rule structure, supporting the claim that node-graph UI is not the invariant but a common interface realization.

## Product D — Esri CityEngine (market anchor, degraded evidence)

- Official docs unreachable this session. Market-anchor status only.
- Market-known position (no product-level operational claims): standalone rule-based procedural generation of 3D city models for urban planning/GIS/entertainment; enterprise customer tier.
- Used only as evidence that domain-specific rule-driven 3D generators exist as a Variant posture (rules + regeneration + 3D output), and as an enterprise-tier counterpoint to the studio/individual tiers.

## Cross-product Comparison

| Dimension | Houdini | Blender | Grasshopper (anchor) | CityEngine (anchor) |
|---|---|---|---|---|
| Procedural posture | whole application organized around procedural authoring | procedural subsystem inside a general direct-manipulation suite | companion visual-programming editor for parametric design | standalone domain-specific rule-based generator |
| Authoring substrate | node networks + parameter expressions + VEX/Python + compiled blocks, in one product | modifier stack + node-based geometry toolset (operational detail unverified this session) | node canvas (unverified this session) | rule language (unverified this session) |
| Evaluation semantics | documented first-class: cook-on-change with managed cook cost, update modes | live re-evaluation expected in current products (unverified this session) | parametric association expected (unverified) | rule regeneration expected (unverified) |
| Primary output | geometry/scenes/USD/renders; also tasks and images | geometry inside its own scene | geometry into the host CAD model | 3D city models |
| Data model | geometry = components + named attributes (documented in depth) | attribute-bearing mesh + node data (unverified detail) | (unverified) | (unverified) |
| Packaging/reuse | digital assets with versioning; recipes | add-ons/extensions; node groups (unverified detail) | shared definitions (unverified) | rule packages (unverified) |
| Customer tier | studios (film/VFX/games), artist-to-studio editions | individuals/small studios (free) | AEC professionals | enterprise/urban planning/GIS |
| Simulation | procedural setup of solvers inside same system | simulation present (suite) | not central | not central |

Stable across all poles (evidence B/C): the user maintains an explicit rule structure; 3D results are computed from it; results respond to definition changes; the procedure is the durable artifact that artists exchange, version, and reuse.

## Canonical Model

### L0 — Defining Invariant (minimal)

Three jointly-held structures plus one domain binding:

1. **The procedure is the content of record.** The user authors and persistently maintains an explicit, editable rule structure — a wired network of operators, a parametric graph, or code — and the saved document is this definition. The resulting geometry is derived output, not the authored artifact. Remove → direct-manipulation 3D application (geometry is the record) or a bare scripting library.
2. **Evaluation produces the 3D results.** The application executes ("cooks") the definition to compute concrete 3D data (geometry with attributes, scene elements), and exposes the evaluated results to observation (viewport, data tables). Remove → a diagram tool or IDE with no 3D product.
3. **Regeneration on change.** Editing any part of the definition — inserting, reordering, re-wiring, re-parameterizing — recomputes the affected results and propagates forward through the defined procedure, without the user re-authoring the output. Remove → one-shot generators and static converters; also separates from AI generators (prompt → result, no editable persistent procedure).
4. **Domain binding: primary output is 3D content** (geometry/scene data). If the procedural machinery's primary output is 2D imagery (textures, materials, composites), the product belongs to Texture/Material Authoring or Compositing Types.

Load-bearing as a set: 1 alone = a code library / text editor; 2 alone = an evaluation demo; 3 without 1+2 = a batch generator; 1+2 without 3 = a script runner, not an authoring application; 1+3 without 2 = pseudo-code tooling. Historical check below shows the set holds for script-era and feature-tree-era systems, so no modern machinery (node editor, GPU, USD, fields systems) is in the definition.

### L1 — Common Mature Structure

- Network editor as the dominant authoring surface: create/arrange/wire operator nodes; subnetworks and nesting ("networks are like folders, nodes like files"); flags/badges showing evaluation state.
- Parameter machinery: per-node parameters; expressions computing parameter values; references (links) between parameters across nodes; ramps/multiparms; spare/custom parameters.
- Geometry-with-attributes data model: components (points/vertices/primitives/detail) carrying named attributes; conventional attribute vocabularies (`P`, `N`, color, uv, velocity, instance); groups; attribute-driven selection and node application.
- Operator libraries organized by task: generators, deformers, copy/instance/scatter, attribute manipulation, volume/heightfield ops.
- 3D viewport bound to the evaluated state, with handles, inspection, and visualizers for hidden data.
- Data inspection surfaces: geometry spreadsheet / data tables; node info (statistics, timing).
- Packaging: wrap networks into reusable custom nodes/tools with own UI (digital assets), versioned, shareable; recipes/presets for parameter groups.
- Scripting/expression languages coexisting with graphs (wrangle nodes, Python, compiled blocks, programmatic geometry via node verbs).
- Looping/iteration constructs inside networks.
- Simulation networks: solvers configured procedurally; simulation cooking managed separately (live mode, reset, caching).
- Render/export layer: render output nodes and render dependency networks; import/export of geometry/scene formats; late-loading detail and render-time generation for scale.
- Update management for expensive evaluation: auto/on-mouse-up/manual cook modes; performance monitoring; cook cancellation.

### L2 — Variant / Optional Structure

- **Procedural subsystem inside a general DCC** (Blender modifier stack + node-based geometry; C4D generators/fields per sibling evidence): the same authoring model as a layer, not the whole app.
- **Parametric design pole** (Grasshopper-class, AEC): precision/associativity orientation, design-intent parameters, host-CAD integration.
- **Domain rule generators** (city/terrain/vegetation-class products and modules): rules specialized to one content domain; standalone or bundled.
- **Pipeline-scale task graphs** (PDG/TOP-class): the procedural model extended from geometry to whole workloads (work items, external processes, farm scheduling).
- **Embedded runtimes**: the procedural engine offered as plugin/API into other DCCs and game engines.
- **Real-time/interactive node-based media environments**: same authoring model oriented to live output (boundary case with media-performance tools).
- **ML/AI assistance**: synthetic data generation, ML-tool platforms layered on the procedural machinery (emerging; era machinery, not definitional).

### L3 — Vendor-specific Structure (kept out of the final document)

- Houdini: SOP/DOP/VOP/LOP/ROP/CHOP/COP/TOP/APEX network taxonomy; VEX; HScript; HIP file format and plain-text mode; digital-asset namespaces/versioning; Solaris/Karma (USD stage building); Copernicus GPU image framework; HQueue; Houdini Engine plugins; specific cook-update mode names.
- Blender: modifier-stack specifics; Geometry Nodes fields system (unverified this session).
- Grasshopper: data-tree data structures (unverified; general market knowledge only).
- CityEngine: CGA rule language (unverified; general market knowledge only).

## Vendor-specific Findings

- The word "cooking" for evaluation is Houdini terminology; other products use "evaluate"/"rebuild" or no special term. Concept is common; word is vendor-specific.
- Multi-network-type architecture (scene/geometry/dynamics/image/render/task as separate network types) is a Houdini design; single-graph products and embedded-subsystem products differ structurally.
- Digital assets with vendor versioning/namespaces is Houdini; concept (package networks as tools) is common, machinery is not.
- USD-centric scene building (LOP/Solaris/Karma) is vendor posture.

## Boundary Findings

1. **vs 3D Modeling Application** (resolves sibling flag): confirmed gradient, keep both. The discriminator is the object of editing: in modeling the user's persistent edits are made directly to geometry elements (the geometry is the record); in procedural creation the persistent edits are to a rule structure from which geometry is re-derived. Modifier/generator stacks inside modelers are semi-procedural capabilities embedded in direct-manipulation products — they do not reclassify the product. Remove procedure-as-record → procedural Type collapses into modeling. Remove direct element editing as the primary mode → modeling remains modeling.
2. **vs 3D Animation Application** (resolves sibling flag): confirmed gradient, keep both. Animation authors time-varying scene state (values over frames, playback, delivery as moving image); procedural creation authors content-generating rules (space and structure). The canonical procedural product is also a full animation application — the Types overlap in products but name different centers of gravity. Cross-reference both documents.
3. **vs Digital Sculpting Application**: clean gradient — hand shaping of surfaces vs rule-driven generation; a sculpting product's record is the deformed surface.
4. **vs Texture / Material Authoring Application**: node-based procedural systems whose primary output is 2D texture/material data belong there, not here. The 3D-output domain binding is what keeps this Type separate. (Same authoring model, different output domain.)
5. **vs Mechanical CAD / parametric CAD**: history-based parametric CAD (feature trees) satisfies the three-leg L0 — the feature tree is a persistent editable recipe that regenerates geometry. The discriminator is purpose and semantics: CAD binds parameters as engineering dimensions/constraints serving manufacturing definition (and sits in Domain 16 of the directory); this Type binds parameters as content-generation controls for media/design output (Domain 04). Grasshopper-class parametric design sits on the seam but serves form exploration for design/content, not manufacturing documentation. Recorded as a Boundary Issue for the taxonomy owner rather than resolved unilaterally.
6. **vs AI 3D Generator Applications** (adjacent generative Types): prompt-driven generation produces geometry without a persistent user-editable procedure and without regeneration semantics tied to user-edited rules; fails L0 legs 1 and 3. Reasoned boundary, not product-verified.
7. **vs Game Engine / Game Development Platform**: engines author behavior/runtime interactivity; node editors inside engines target logic, not the content-creation pipeline. Clean.
8. **Alias/Variant check**: not an alias of 3D Modeling — the differing leg (what is edited + regeneration) is load-bearing, confirmed from both sides by prior sibling passes and this pass. Keep-both as separate Types.

### Historical / Market-Sample Check

- Script-era procedural 3D (1980s production tools and research systems: script/code-driven geometry generation, procedural shaders/primitives, L-systems, parametric description languages) satisfies all three legs at "code as the procedure" level; node-graph UI is era machinery.
- History-based parametric CAD (feature-tree era, late 1980s onward) satisfies the legs on the recipe side; excluded by domain binding (engineering definition), see Boundary Finding 5.
- The modern studio package (node graphs + code + attributes) satisfies trivially.
- Older/niche products that "bake" procedures into one-shot outputs would fail leg 3 — correctly outside the Type.
- Conclusion: the definition does not over-fit to the modern node-graph studio product; "explicit editable rule structure" (graph, recipe, or code) is the era-stable invariant.

## Uncertainties

- Blender, Grasshopper, CityEngine official operational documentation was unreachable this session; their rows in the comparison rest on positioning pages, sibling-pass evidence, and market-anchor status. No precise operational claims about them are made.
- Whether the market would classify domain generators (cities/terrain) as members of this Type or as their own micro-Types: treated here as Variants; thin standalone generators that lack the full authoring surface may sit below the Type. Needs joint review if a dedicated leaf ever appears in the directory.
- The seam with parametric CAD (Boundary Finding 5) is principled but not empirically testable with current evidence; flagged for taxonomy owner.
- Extent to which "procedural subsystem inside a general DCC" products should be counted as full members vs boundary cases of the Type: treated as Variant posture (Type defined by authoring model, not by standalone product shape).

## Final Synthesis

A Procedural 3D Creation Application is defined by a minimal core: the user authors a persistent, explicit, editable rule structure (node network, parametric recipe, or code); the application evaluates that structure to produce 3D data (geometry carrying attributes); and every edit to the definition regenerates the affected results by propagation, making the procedure — not the geometry — the content of record. Around this core, mature products converge on a standard structure: a network editor plus parameter machinery; a geometry-with-attributes data model with inspection surfaces; operator libraries by task; viewport visualization of evaluated state; packaging of networks into reusable tools; script/expression languages beside graphs; simulation networks; render/export layers; and update management for expensive evaluation. Products realize the Type as: the whole application (studio-grade procedural package), an embedded subsystem of a direct-manipulation suite, a parametric design companion, or a domain-specific rule generator. The Type's boundaries: modeling (geometry-as-record), animation (time axis), sculpting (hand shaping), material authoring (2D procedural output), CAD (engineering intent), AI generators (no editable persistent procedure), and game engines (runtime behavior) — with the modeling and animation boundaries being documented gradients, and the CAD seam flagged for taxonomy review.
