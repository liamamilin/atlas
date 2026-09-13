# Mechanical CAD

## Overview

A **Mechanical CAD** application is the engineering definition environment for physical products. It maintains precise, real-world-scale geometry of components as the authoritative model of what will be manufactured, builds and changes that geometry by editing an intent-carrying definition — constrained sketches, features, parameters — assembles components into a product structure with defined relationships and degrees of freedom, and derives engineering drawings and manufacturing-facing outputs from that model.

The defining core is small:

```text
Engineering model of record (precise component geometry)
└── Intent-carrying editable definition (sketches, features, parameters)
    └── Assembly-level product structure (constrained component relationships)
        └── Model-derived engineering deliverables (drawings, manufacturing data)
```

Everything else commonly associated with modern mechanical CAD — the ordered feature tree with rollback, configurations, bills of materials, built-in versioning, sheet-metal environments, embedded simulation or CAM, real-time collaboration — is widespread in current products but is not what makes the product a Mechanical CAD application. Minimal open-source modelers, desktop SMB tools, history-optional direct modelers, and cloud-native platforms all fit the same definition.

The Type's center of gravity is **engineering function definition**: the model exists to define how a physical product is built, how its parts relate, and how it will be manufactured. When the center of gravity shifts to form and appearance exploration, the product is drifting toward Industrial Design; when it shifts to visual or media content, toward 3D Modeling.

## Users & Context

Primary users:

- **mechanical engineers and mechanical designers** — define component geometry and product structure; the model is their daily work product
- **drafters / documentation engineers** — derive and maintain engineering drawings from the model
- **manufacturing and process engineers** — consume the model's geometry and drawings for fabrication planning

Secondary users:

- simulation and analysis engineers, who take the defined geometry as input
- data management / engineering management roles, who govern revisions and releases of the model

The work context is product development in industries that make physical goods: machinery, equipment, consumer products, tooling, fixtures, vehicles. The application sits upstream of manufacturing and downstream of concept work: concept and form exploration happen before or beside it (often in industrial-design or sketch tools), and machining, analysis, and lifecycle management happen after or around it. The model produced here is the artifact other engineering systems consume.

## Core Model

### The Defining Core

**1. The engineering model of record.** The application holds precise geometry of physical components — parts — at real-world scale and real-world units. This model is the authoritative definition of what will be manufactured; drawings, exports, and analyses are derived from it, not the other way around. The model persists and is edited over the product's life.

**2. Intent-carrying editable definition.** Geometry is not shaped freely; it is *defined*. A component is built as a structured definition: 2D sketches whose elements are held by constraints and dimensions, features that consume those sketches (extrudes, revolves, holes, fillets, patterns, shells), and parameters that drive them. When the user edits the definition — changes a dimension, a constraint, a feature — the application recomputes the dependent geometry. Design change is an edit to the definition, and the definition is what carries the design intent.

**3. Assembly-level product structure.** Components are brought into an assembly as instances and positioned by defined relationships — assembly constraints or mates — which specify how parts touch, align, slide, or rotate relative to each other. The assembly is the model of the whole product, including its degrees of freedom: what can move, what is fixed, how mechanisms behave. Sub-assemblies compose into larger structures.

**4. Model-derived engineering deliverables.** Engineering drawings (views, dimensions, annotations) and manufacturing-facing outputs are generated from the model and remain associated with it. The realization varies: a persistent drawing document that updates with the model, or exported model views in exchange formats; the constant is that the deliverable is *derived from and driven by* the model.

### Standard Capabilities

Mature products commonly add the following. They make the Type practical; they do not define it.

- **Parametric feature-based construction** — the dominant modern work-mode: an ordered feature tree with rollback, parent-child dependencies, and regeneration on edit. Present in nearly all current products; explicitly optional in history-free direct-modeling products, which still edit dimensions and constraints to drive geometry.
- **Configurations / variants** — named option sets that drive feature parameters, feature suppression, and properties, producing part or product variants from one definition.
- **Bills of materials** — generated from the assembly's component structure, with properties, quantities, and sub-assembly handling.
- **Analysis surfaces** — measurement, mass properties (from assigned materials), interference checking, degrees-of-freedom checks.
- **Data exchange** — import and export in neutral formats (STEP/IGES-class, kernel formats) and in other systems' native formats; mesh formats (STL-class) for 3D printing as a secondary path.
- **Sheet metal design** — dedicated feature sets with flat-pattern derivation.
- **Data management** — versions, revisions, and release states, either built in or via companion PDM/PLM products.
- **Standard content** — libraries of fasteners and catalog parts for reuse.
- **Visualization** — rendering and exploded views for communication and documentation.

### One Structure, Many Implementations

The core model is written in conceptual terms; products realize each concept differently:

```text
Concept:      Engineering model of record
Realizations: part files in a file system; a project container holding tabs;
              a single unified scene file; a database-backed cloud document

Concept:      Intent-carrying editable definition
Realizations: ordered feature tree with rollback; object property graph with
              recalculation; constraint-driven direct editing without history

Concept:      Assembly product structure
Realizations: constraint/mate solvers over component instances; DOF-embedded
              mates; positional assembly with constraint checking

Concept:      Model-derived deliverables
Realizations: persistent associative drawing documents; exported hidden-line
              views in exchange formats; drawing modules as separate products
```

A reader who has only seen one implementation — say, a desktop feature-tree modeler — should still be able to recognize a cloud-native document-container product, a workbench-modular open-source tool, or a catalog-driven direct modeler as the same Type.

## How It Works

### Define a component

```text
Create a part
→ sketch on a plane or face
→ constrain and dimension the sketch (until fully defined)
→ apply features that consume the sketch (extrude, revolve, hole, fillet, pattern…)
→ the feature tree accumulates the definition
→ edit = change a parameter or feature → dependent geometry recomputes
```

The sketch is the seed of most geometry; constraints and dimensions are what make it an engineering definition rather than a picture. Features transform sketches and existing geometry into the finished component. The component's definition — not its current shape — is what gets saved and reused.

### Build the product

```text
Create an assembly
→ insert component instances (from this project, other projects, or standard libraries)
→ position them with assembly constraints / mates
→ degrees of freedom resolve (fixed, sliding, rotating, free)
→ drag or animate to test motion
→ compose sub-assemblies into the full product structure
```

The assembly answers engineering questions the part model cannot: how parts fit, what moves, whether mechanisms behave as intended, whether anything interferes. Some products also allow editing a part *in the context of* the assembled neighbors, so a feature can be defined relative to another component's geometry.

### Derive the deliverables

```text
Open a drawing on the model (or export views)
→ place projected views (front, section, detail, isometric…)
→ add dimensions, annotations, notes, title blocks
→ the drawing references the model
→ export for manufacturing: drawings to PDF/DWG-class formats;
  geometry to STEP/IGES-class neutral formats or mesh formats for printing
```

Because deliverables derive from the model, a model change flows forward: update the drawing, regenerate the export. The model of record stays the single source of truth.

### Manage change

```text
Edit the definition (dimension, feature, constraint, mate)
→ regeneration recomputes dependents in order
→ broken references surface as errors to repair
→ variants handled as configurations where supported
→ revisions/versions recorded where data management exists
```

### Core vs Common vs Optional

**Defining core** — without these, not Mechanical CAD:

- precise engineering model of record for physical components
- intent-carrying editable definition (constraints/dimensions/features/parameters)
- assembly-level product structure with defined component relationships
- model-derived engineering deliverables (drawings and/or manufacturing outputs)

**Standard capabilities** — present in most mature products:

- parametric feature tree with regeneration and rollback
- configurations/variants
- BOM generation
- measurement, mass properties, interference and DOF checks
- neutral-format exchange plus native-format import
- sheet metal environments
- data management (built-in or companion)
- standard-part libraries, rendering

**Optional / variant** — depends on segment, era, deployment:

- cloud-native vs desktop deployment; document-container vs file-based data model
- history-based parametric vs direct editing vs hybrid modality
- embedded CAM/CAE workbenches or bundled add-ons vs separate products
- scripting/automation layers
- real-time collaboration
- formal release/change management workflows
- dedicated 2D detailing products beside the 3D modeler

## Interfaces

Described in conceptual terms; exact layouts and names vary by product.

### Graphics viewport

The 3D workspace. Purpose: see and manipulate the model. Typical contents: the geometry, orientation aids (view cube / standard views), planes and origin, section views, display styles. Primary actions: rotate/zoom/pan, select geometry, drag-test assembly motion.

### Feature tree / model browser

The definition's outline. Purpose: show how the component was built and drive edits. Typical contents: ordered features, sketches, reference geometry, parts list; rollback control in tree-based products. Primary actions: edit/reorder/suppress/delete features, roll back and replay the definition, locate errors.

### Sketcher

The 2D definition surface. Purpose: create constrained profile geometry. Typical contents: drawing tools (lines, circles, arcs, splines), constraint and dimension tools, constraint-state indicators. Primary actions: draw, constrain, dimension, trim, convert to construction geometry.

### Feature dialogs

Parameter entry for each feature. Typical contents: selection fields for geometry, numeric parameters (accepting expressions in many products), direction/offset options, live preview. Primary actions: select references, set parameters, preview, accept or cancel.

### Assembly environment

The product-structure surface. Typical contents: instances list, mate/constraint list, degrees-of-freedom indicators, motion tools. Primary actions: insert instances, apply mates/constraints, fix or float components, drag/animate motion, check interference.

### Drawing environment

The documentation surface. Typical contents: sheets, projected views, dimension and annotation tools, title blocks, BOM tables where supported. Primary actions: place views, dimension, annotate, update from model, export.

### Data management surfaces

Where supported: version/history browsers, revision and release controls, BOM tables, export panels. Purpose: govern the model's life beyond a single editing session.

## Important Rules / Behaviors

### Regeneration and dependencies

The definition's elements depend on each other — a feature depends on its sketch, downstream features on upstream ones. An edit triggers recomputation of dependents; a broken reference (deleted face, changed edge) surfaces as a failed feature that the user must repair. This dependency web is why change is *controlled*: the model's behavior under edit is predictable and traceable.

### Constraint states are visible and consequential

Sketches and assemblies expose their constraint state. Under-constrained sketch elements are flagged — color-coded in some products, listed by a degrees-of-freedom check in others; assemblies indicate which instances can still move. Reaching a fully defined sketch is a normal engineering goal, not an incidental UI detail.

### Fix is not a relationship

In assemblies, pinning a component in place is distinct from constraining it to another component; a fixed position is local to that assembly and does not express a relationship. The assembly needs an anchor — a fixed or origin-anchored foundation component — and everything else is positioned by relationships.

### The model drives the deliverables

Drawings and exports are downstream of the model. When the model changes, deliverables are updated from it — in associative-drawing products explicitly, in export-based products by regenerating the export. Editing a drawing does not change the model.

### Exchange carries geometry, not intent

Neutral formats (STEP/IGES-class) move precise geometry between systems but do not carry the feature definition; an imported model typically arrives as geometry without the authoring system's feature history, and further editing happens on that imported geometry. Native-format import across systems has the same character. This is why the model of record lives in the authoring system.

### Units, precision, and expressions

Geometry is held at real-world scale in real-world units. Numeric fields commonly accept expressions and formulas, so parameters can be computed rather than typed — a small but structural part of how intent is expressed.

### Suppression and variants

Features, constraints, and components can be suppressed — temporarily excluded from the computed result without deletion. Configurations (where supported) are named, persistent combinations of parameter values and suppression states, letting one definition yield a family of parts.

## Variants

- **Cloud-native platforms** — the model lives in a managed cloud container; versions, branching, sharing, and release management are built in; browser and mobile clients; real-time co-editing.
- **Classic desktop modelers** — file- or project-based; local data management or companion PDM; the historical mainstream form.
- **Open-source modular tools** — capability organized in switchable workbenches (part design, drafting, assembly, CAM, FEM); extensible through scripting and community add-ons.
- **Direct / hybrid modelers** — editing with or without history-dependence; catalog-driven construction; positioned for speed and design change freedom.
- **Minimal parametric modelers** — the smallest structure that satisfies the core: sketches, constraints, features, constrained assemblies, exported views; often single-developer or small-team open source.
- **Integrated product-development suites** — CAD bundled with CAM, CAE, PDM/PLM, and data management under one platform; the integration is packaging around the same core.
- **Industry packaging** — machinery, tooling, sheet-metal, and mechanism-design emphases; dedicated 2D detailing products beside 3D modelers.

A variant remains a variant unless it changes the users, core objects, workflow, or rules so much that the defining core no longer applies.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Industrial Design Application | adjacent, heavily hybridized market | center of gravity: form/appearance exploration with fluid freeform editing and design-communication deliverables; generally no constraint-mated assembly structure; MCAD centers engineering function definition, assemblies, and model-driven engineering deliverables |
| 3D Modeling Application | adjacent | serves visual/media content (scenes, assets, animation); lacks constraint-based assemblies, DOF semantics, and model-associated engineering drawings; CAD-format import there is interop, not identity |
| Procedural 3D Creation Application | adjacent | authors generative rule structures whose output is 3D content; MCAD maintains an engineering definition of a physical product whose regeneration serves controlled design change |
| CAM | downstream consumer | consumes model geometry to generate toolpaths and machining programs; integration into MCAD products is packaging |
| CAE / Engineering Simulation | downstream consumer | analyzes the behavior of the defined design; embedded simulation modules are packaging |
| PLM | upstream/around | manages product lifecycle data and processes above the model across disciplines; MCAD authors and maintains the model itself |
| BIM Authoring | adjacent domain | authors building-scale element models with construction semantics; equipment/MEP modeling is the overlap zone |
| ECAD / EDA | adjacent domain | electrical/electronic design; mechanical-electrical co-design is a handoff, not a shared center |
| Additive Manufacturing Software | downstream consumer | print preparation, orientation, supports, slicing; MCAD exports mesh/geometry to it |

The Industrial Design boundary is the most heavily hybridized in the market — products exist on both sides that reach toward the other — and is best resolved by center of gravity plus structure: MCAD's defining core includes constrained assembly product structure and model-driven engineering deliverables, which industrial-design products do not carry as their center.

## Representative Products

- **Onshape** — cloud-native SaaS parametric MCAD; document-container data model with built-in versioning and release management
- **FreeCAD** — open-source parametric modeler; workbench-modular architecture
- **Alibre Design** — SMB/perpetual-license parametric MCAD with hobby tiers
- **IronCAD** — history-optional parametric/direct hybrid; catalog-driven, single-scene data model
- **SolveSpace** — minimal open-source parametric modeler; exported-view deliverables

The defining core was checked across these five poles (cloud-native, open-source modular, SMB, direct/hybrid, minimal) to avoid over-fitting the definition to any single era, deployment, or vendor pattern. Major enterprise systems (SOLIDWORKS, Creo, NX, CATIA, Inventor, Solid Edge, Fusion) are market anchors; their documentation was not reachable during research, so no product-specific claims about them are made here.

## Sources

Research date: **2026-09-09**

- Onshape Help (official): Getting Started; Part Studios; Sketch Tools; Feature Tools; Mates; Insert Parts and Assemblies; Modeling In-Context; Bill of Materials; Drawings; Configurations; Supported File Formats — https://cad.onshape.com/help/
- SolveSpace (official): home and Features — https://solvespace.com/ , https://solvespace.com/features.pl
- FreeCAD (official): home and Key Features — https://www.freecad.org/ , https://www.freecad.org/features.php
- Alibre (official): home and product pages — https://www.alibre.com/
- IronCAD (official): home and IRONCAD product page — https://www.ironcad.com/

> Sourcing limitation: official documentation for SOLIDWORKS, Autodesk Fusion, PTC Creo, Siemens NX/Solid Edge, CATIA, and Autodesk Inventor could not be fetched from the research environment (JavaScript-rendered help systems, login walls, or blocked hosts). These products are treated as market anchors only. FreeCAD's community wiki and Alibre's help portal were likewise unreachable (anti-bot protection / JavaScript application), so those products are evidenced at the level of their official public product pages. Operational details that would require those deeper sources (exact limits, defaults, version-specific behaviors) are intentionally not stated in this document.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical / market-sample breadth check are recorded in the paired Research Notes.
