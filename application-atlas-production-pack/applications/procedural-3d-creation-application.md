# Procedural 3D Creation Application

## Overview

A **Procedural 3D Creation Application** creates 3D content by having the user author an explicit, persistent, editable rule structure — a network of connected operators, a parametric recipe, or code — which the application evaluates to produce 3D results (geometry and scene elements). When any part of the definition changes, the application regenerates the affected results automatically. The procedure, not the resulting geometry, is the artifact the user maintains and saves.

This is the Type's defining difference from neighboring 3D Types. In a direct-manipulation modeler, the user's persistent edits are made to the geometry itself, and the geometry is the document. Here the user's persistent edits are made to the rules from which geometry is derived — insert a step, rewire a connection, change a parameter, and the content recomputes. This makes the Type well suited to work where content must be revisable late in production, generated at scale (thousands of variations, vast scenes), and packaged into reusable tools.

The defining structure is small. Everything else commonly associated with procedural products — node-graph editors, specific data formats, simulation toolkits, real-time preview, USD pipelines — is standard capability or variant machinery, not the definition. Script-driven generation from earlier decades satisfies the same structure with no node graph at all.

## Users & Context

Primary users are people who create 3D content where scale, revisability, or rule-driven variation matters:

- **Technical directors and effects artists** in film, episodic, and games, who build effects setups (destruction, particles, cloth, terrain, crowds) and content-generation tools used by whole productions.
- **3D artists** who need repeatability: scattering vegetation across a landscape, assembling a city from rules, generating variants of a product model.
- **Designers in architecture and engineering** who drive form from parameters and rules and need the model to respond when a design input changes.

Secondary users include pipeline/technical staff who connect procedural output to downstream systems (render farms, game engines, CAD), and artists who consume packaged procedural tools created by others without ever editing the underlying networks.

The work environment is a desktop workstation; the material being edited is expensive to compute, so interactive work and final computation are typically separated. The customer base spans studios (film/VFX), individuals and small teams, design professionals, and enterprise/geospatial organizations.

## Core Model

### The Defining Core

```text
Procedure (explicit, persistent, editable rule structure)
└── Evaluation (executing the procedure — some products call this "cooking")
    └── 3D data (geometry carrying attributes, scene elements)
        └── Regeneration: edits to the procedure propagate
            and recompute the affected results
```

Three properties held together, plus one domain binding. If any is removed, the product stops being this Type:

- **The procedure is the content of record.** The user authors and maintains an explicit rule structure — a wired graph of operators, a parametric definition, or code. The saved document is this definition. Without it, the product is a direct-manipulation modeler (geometry as the document) or a bare code library.
- **Evaluation produces the 3D results.** The application executes the definition to compute concrete 3D data and shows the evaluated results to the user. Without it, there is no 3D product — only a diagram or a text editor.
- **Regeneration on change.** Editing any part of the definition — inserting, reordering, rewiring, re-parameterizing — recomputes the affected output and propagates forward through the procedure, without the user re-authoring the result. Without it, the product is a one-shot generator or a static converter.
- **Primary output is 3D content.** The same authoring model aimed primarily at 2D output (textures, materials, image composites) belongs to the texture/material authoring and compositing Types.

The procedure can take several interchangeable forms inside one product: a visual network of nodes, per-parameter expressions and references between parameters, and embedded code. Mature products treat these as layers of the same underlying definition rather than as separate paradigms.

### The Data Model

What flows through the procedure is 3D data — most importantly, **geometry carrying attributes**. Geometry is made of components (points, vertices, faces or other primitives, and whole-object "detail" data), and information such as position, normals, color, texture coordinates, velocity, or instance references is stored as named values attached to those components. Attributes are first-class: users create custom ones, inspect them in data tables, select geometry by attribute values, and later stages of a procedure behave differently depending on attribute content. This "data flows through operators" model is what lets one well-built rule structure serve as a tool for others: the structure defines the transformation, the input geometry and parameters define the instance.

### Standard Capabilities

Mature products commonly add the following. These make the Type practical but do not define it:

- **Network editor** — the dominant authoring surface: create, arrange, and wire operators; nest networks inside container nodes; annotate and organize. Terminology and layout vary; the concept is common.
- **Parameter machinery** — every operator exposes parameters; parameters can be driven by expressions, by references to other parameters, or by animation; presets and saved parameter sets.
- **Operator libraries** — generators (primitives, curves, volumes), deformers, copy/instance/scatter operations, attribute manipulation, heightfield/terrain operations, organized by task.
- **Viewport bound to evaluated state** — the 3D view shows the computed result, with handles for direct manipulation *of procedure inputs* (moving a handle edits a parameter, not the mesh).
- **Data inspection** — spreadsheets/tables showing the geometry and attribute values at any point in the procedure; node statistics and timings.
- **Packaging** — wrap a network into a reusable custom node with its own user interface, versioned and shareable, so studios build tool libraries and non-technical artists consume them.
- **Code layers** — snippet/code nodes and scripting languages alongside the graph; some products compile portions of networks for speed; iteration/looping constructs inside networks.
- **Simulation networks** — solvers (particles, smoke/fire, cloth, grains, rigid bodies) are configured procedurally; simulation is set up as a rule structure, then advanced over time as a separate computed process.
- **Scale management** — evaluation/update modes (continuous, deferred, on demand), recomputation cost controls, caching/baking, loading detail only when needed, render-time generation and instancing.
- **Interchange and delivery** — import/export of geometry and scene formats, render output nodes, and embedding of the procedural engine into other applications via plugins/APIs.

## How It Works

### The authoring loop

```text
Create operators and wire them into a network
→ set parameters (values, expressions, references)
→ the application evaluates the network
→ inspect the result (viewport + data tables)
→ edit the definition: insert / reorder / rewire / re-parameterize
→ affected results recompute and propagate forward
→ repeat
```

This loop replaces the undo-and-redo cycle of direct-manipulation work. Changing an early decision — the base curve, the scatter density, the fracture pattern — flows through everything built after it. Products differ in when evaluation happens (continuously while dragging, on release, on demand) and how its cost is managed, but the semantics are the same: the visible 3D state is always a computed consequence of the definition.

### Building content at scale

A typical workflow starts from a small input (a curve, a grid, a model) and builds structure on top: copy and instance geometry onto points, scatter instances by attribute-driven rules, deform, refine, iterate inside the network. Because the recipe is data, the same network can produce unbounded variants by changing inputs or parameters. Mature products commonly also support deferring or optimizing evaluation — caching results, generating late-stage detail only when needed, and instancing at render time — which is what makes scenes possible whose full detail would not fit in memory.

### Packaging a procedure into a tool

Once a network solves a problem, it is collapsed into a single custom node with a curated parameter interface. Other artists use that node like any built-in operator, without seeing the internals. Studios accumulate these packaged tools as a shared library — this is the main mechanism by which procedural work becomes production infrastructure.

### Simulating within the same model

Effects work uses the same authoring model: a network configures a solver — initial conditions, forces, collision rules — and the simulation is then computed (often over a frame range) as a separate, cacheable process distinct from the interactive re-evaluation of static networks. The setup is procedural; the simulated motion is the evaluated result.

### Leaving the procedural context

Results leave in three common ways: as exported geometry/scene data consumed by other software; as rendered images; and as packaged procedures embedded into other applications (game engines, modelers, CAD) through plugin runtimes, where the receiving side can still adjust the exposed parameters.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Network editor

The home surface of the Type.

- operators as nodes with inputs/outputs; wires defining data flow; nesting via container/subnetwork nodes
- evaluation-state indicators on nodes; annotations and layout organization
- primary actions: create/insert/wire/reorder nodes, navigate between nested networks, collapse selections into reusable subnetworks

### Parameter editor

The per-operator control surface.

- the selected node's exposed settings; expression fields; references to other parameters
- primary actions: set values, bind expressions/links, save presets

### 3D viewport

Shows the evaluated result; the bridge between graph and geometry.

- the cooked scene, handles for editing procedure inputs in place, display of hidden data (attribute visualizations, guides)
- primary actions: select, position/transform inputs, inspect, flag regions for downstream operations

### Data spreadsheet / inspection tables

The "X-ray" surface unique in importance to this Type.

- per-component attribute values at a chosen point in the network; node statistics
- primary actions: read/verify data, compare before/after an operator

### Packaging and tool interfaces

- dialogs/editors for wrapping networks into custom nodes, defining their exposed parameters and UI, versioning
- shelf/tool palettes where packaged tools appear for other users

### Render and delivery surfaces

- render output nodes with dependencies; export dialogs for geometry/scene formats

## Important Rules / Behaviors

- **The definition, not the result, is authoritative.** Editing geometry directly is either impossible, temporary, or an edit to a *specific evaluation* — the durable way to change content is to change the procedure. Products that permit sculpt-like direct edits typically do so as an operator stage inside the network.
- **Order in the procedure is meaning.** The same operators wired in a different order produce different results; reordering is a normal editing act, not a stylistic preference.
- **Evaluation is the cost center.** Every edit can trigger recomputation; mature products expose control over when this happens (continuously while dragging, on release, on demand) and over how expensive recomputation is managed, because a single parameter change can invalidate a large amount of computation.
- **Parameters are inputs, not annotations.** A parameter can be a static value, a computed expression, a reference to another parameter elsewhere, or a keyed animation. What looks like a simple number may be a live computation.
- **Changes propagate forward only.** Editing a node recomputes the nodes downstream of it; earlier parts of the network are unaffected. This one-way flow is what makes results reproducible.
- **Determinism is expected but managed.** Users expect the same definition to regenerate the same result; some products provide controls where performance optimizations could otherwise make results vary.
- **The tool boundary is the parameter interface.** Consumers of a packaged tool can only change what its author exposed — encapsulation is a user-facing rule, not just a convenience.

## Variants

- **Whole-application procedural package** — the entire product is organized around authoring and evaluating rule structures; geometry, effects, scene assembly, rendering, and even pipeline tasks are all procedural networks. The historical center of the Type (film/VFX).
- **Procedural subsystem inside a direct-manipulation suite** — a general 3D application whose main workflow is direct editing, hosting a procedural layer (modifier stacks, node-based geometry systems) within it. The authoring model is identical; the center of gravity of the product is not.
- **Parametric design companion** — visual rule structures used in architecture/engineering to drive model geometry from design parameters, integrated with CAD/modeling hosts; oriented to precision and design intent rather than entertainment content.
- **Domain-specific rule generators** — standalone products or modules whose rule structures are specialized to one content domain (cities, terrain, vegetation); rule language and controls tailored to that domain.
- **Pipeline-scale task graphs** — the authoring model extended from geometry to whole workloads: data becomes work items, nodes represent external processes, networks schedule farm-scale execution.
- **Embedded procedural runtimes** — the engine delivered as a plugin/API so other applications can host packaged procedures and expose their parameters.
- **Real-time interactive media environments** — the same authoring model aimed at live, interactive output (installations, shows); on the boundary with media-performance tools.

## Related Application Types

| Application Type | Distinction |
|---|---|
| 3D Modeling Application | the geometry is the document; persistent edits are made directly to mesh elements. Procedural products generate geometry from editable rules; the gradient between them is real (modifier stacks) but the object of editing differs |
| 3D Animation Application | authors time-varying scene state (keys, tracks, playback, rendered motion); a procedural product may be simultaneously a full animation application — the Types overlap in products but name different centers of gravity |
| Digital Sculpting Application | hand-shaped surfaces via brushes; the deformed surface is the record, not a rule structure |
| Texture / Material Authoring Application | the same node-based authoring model, but the primary output is 2D texture/material data, not 3D content |
| Photogrammetry Application | geometry is measured from photographs of real subjects, not generated from rules |
| Mechanical CAD | history-based parametric CAD also keeps a recipe that regenerates geometry, but its parameters are engineering dimensions/constraints serving manufacturing definition; this Type serves content generation |
| Game Engine / Game Development Platform | authors runtime behavior and interactivity; node editors inside engines target logic, not content creation |
| AI 3D Generator (adjacent generative Types) | prompt-to-geometry without a persistent user-editable procedure and without regeneration driven by edited rules |

The most important boundary is with the 3D Modeling Application, because the two share outputs and often coexist in one product. The structural test: **what does the user's saved edit change — the geometry, or the rules that recompute the geometry?**

## Representative Products

- SideFX Houdini — whole-application procedural package (film/VFX/games)
- Blender — general 3D creation suite hosting procedural machinery (modifier stack, node-based geometry tools) inside a direct-manipulation workflow
- Grasshopper (McNeel/Rhino ecosystem) — parametric visual programming for design (AEC)
- Esri CityEngine — rule-based procedural generation of 3D city models (enterprise/geospatial)

## Sources

Research date: **2026-09-08**

- SideFX Houdini 22.0 official documentation:
  - Introduction to Houdini — https://www.sidefx.com/docs/houdini/basics/intro.html
  - Cooking — https://www.sidefx.com/docs/houdini/basics/cooking.html
  - Networks and parameters — https://www.sidefx.com/docs/houdini/network/index.html
  - Geometry — https://www.sidefx.com/docs/houdini/model/index.html
  - Geometry attributes — https://www.sidefx.com/docs/houdini/model/attributes.html
  - Digital assets — https://www.sidefx.com/docs/houdini/assets/index.html
- Blender — official features/positioning page: https://www.blender.org/features/
- Grasshopper — market anchor only; official documentation hosts were unreachable during research (no product-level claims are made)
- Esri CityEngine — market anchor only; official documentation was unreachable during research (no product-level claims are made)

> Sourcing limitation: the Blender Manual (docs.blender.org) returned access errors on repeated attempts, and the official documentation sites for Grasshopper and CityEngine could not be reached from the research environment on 2026-09-08. Claims about those products are therefore held at positioning/market-anchor level, cross-checked against prior research passes recorded in this repository; no operational specifics are asserted for them. Product-specific terminology and machinery observed only in one product (network-type taxonomies, evaluation vocabulary, packaging formats) are intentionally kept out of the general description above.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
