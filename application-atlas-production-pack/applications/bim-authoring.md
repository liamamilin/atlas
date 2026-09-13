# BIM Authoring

## Overview

A **BIM Authoring** application is the authoring environment in which a building (or other built asset) is created not merely as geometry or as a drawing set, but as a **data-rich model of elements**: every wall, slab, column, opening, duct, and beam exists as a typed object that carries structured information, the model as a whole serves as the project's single source of truth, and the project's deliverables — drawings, schedules, quantities, and exchange files — are derived from that model and kept consistent with it.

The defining structure is small:

```text
Building element objects (typed objects for physical parts of the building)
└── each element carries structured data (identity, type, properties, classification)
    └── one model maintained as the project's system of record
        └── derived, coordinated outputs: drawings, schedules, quantities, exchange files
```

Everything commonly associated with modern BIM practice — openBIM/IFC exchange, cloud collaboration, model-development frameworks, clash detection, scan-to-BIM conversion, AI-assisted classification — makes the work faster or the deliverable more interoperable, but is not what makes the software a BIM authoring tool. Early object-based BIM products satisfied the defining structure above without any of those capabilities, and a discipline-scoped structural or fabrication model built before those practices existed still fits it today.

Two boundaries frame the Type. When models are consumed rather than authored — federated from several authors to detect and resolve cross-discipline conflicts — the work belongs to BIM Coordination. And in the current market, the same leading products are frequently marketed as both "BIM software" and architecture design tools; the working distinction is which artifact is the system of record — the architect's design documentation (Architecture Design Application) or the shared data-rich model exchanged across disciplines (this Type).

## Users & Context

The primary users are building-design and construction professionals who author the model:

- **Architects and designers** — the model is the vehicle for developing and delivering the building design.
- **Structural and MEP engineers** — the model carries their systems (structure, ducts, pipes, cable routes) as data-bearing elements rather than as annotations on drawings.
- **Modelers and BIM technicians** — in larger practices, specialists who develop the model, maintain its data quality, and manage exchange under the project's standards.
- **Detailers and fabricators** — on the construction side, they author fabrication-grade models (connections, rebar, precast pieces) whose data drives production.
- **Contractors and construction planners** — they use authoring tools to build constructible models for sequencing, quantities, and site planning.

Alongside the authors sits the **BIM manager**, who configures templates, element libraries, classification systems, and exchange requirements rather than authoring elements directly.

The work is desktop professional software on Windows or macOS, organized around projects that run for months. Where public clients or large programs mandate information delivery, exchange capability and data standards shape how the tool is configured; team sizes range from a solo practitioner to distributed multidiscipline teams working on one shared model.

## Core Model

### The defining core

**1. Building elements.** The model is composed of individual elements, each an object representing a physical part of the building: walls, slabs, roofs, columns, beams, foundations, stairs, doors, windows, facades — and, depending on discipline scope, structural members and connections, ducts and pipes, or precast and steel assemblies. Elements are typically organized by **levels/stories** (vertical structure) and **grids** (horizontal structure). This is what separates the Type from generic 3D modeling: the model's parts mean something in building terms, not just in geometric terms.

**2. Element data.** Each element carries structured information beyond its shape — what it is (type and classification), what it is made of, its dimensions and properties, and other project-defined attributes. The data is first-class: it can be listed, filtered, and extracted without re-authoring it anywhere else. This is the "information" in Building Information Modeling; without it, an element is only geometry and the tool is a modeler.

**3. The model as single source.** The project's outputs are derived from the one model: plans, sections, and elevations are views of the model's geometry; schedules and quantity take-offs are tables over the model's element data; exchange files are serializations of the model (or parts of it) for other parties. Change the model and the outputs follow. The model — not the drawing set — is the project's system of record; this is the property that most clearly separates BIM authoring from 2D drafting that merely carries attributes.

### Standard capabilities of mature products

Most current BIM authoring products carry the following. They make the workflow efficient and the model deliverable, but a product can be genuine BIM authoring without every one of them:

- **Parametric element toolset** — typed elements with editable properties and behavior (an opening exists in a wall; a stair connects two levels; walls join slabs), placed by tool rather than composed from raw geometry.
- **Documentation generation** — plans, sections, elevations, and sheet layouts derived from the model and updated as it changes; annotation and dimensioning applied over the derived views.
- **Schedules and quantity take-offs** — door/window/finish schedules, material lists, and measurable quantities computed from element data, typically supporting early cost estimating.
- **Element libraries and office standards** — catalogs of reusable element types, manufacturer content, and project/office templates that pre-configure data and representation.
- **Exchange and interoperability** — import/export of open model formats (IFC being the industry standard), issue-exchange formats (BCF) for coordination with other parties, and common CAD formats (DWG/DXF) for drawing-era data.
- **Classification and data requirements** — the ability to attach classification-system references to elements and, in more standards-driven products, to check the model against defined information requirements.
- **Multi-user model sharing** — mechanisms for several people to work on one model, whether through file-based coordination, network worksharing, or cloud-hosted sharing.
- **Visualization** — renderings, walkthroughs, and presentation output generated from the same model.
- **Site context** — terrain, georeferencing, and survey/point-cloud data situating the building in its environment.

### One core, several realizations

The defining core is stable, but the market realizes it through visibly different philosophies, and understanding them explains most product differences:

```text
Concept:              Where elements come from
Realizations:         authored as parametric objects ("draw the building");
                      geometry modeled freely, then classified into elements;
                      scanned reality converted into elements (scan-to-BIM)

Concept:              How the model reaches other parties
Realizations:         open standards exchange (IFC/BCF);
                      native file exchange between matching tools;
                      vendor cloud platforms hosting the shared model

Concept:              How teams work on one model
Realizations:         file-based handoff;
                      network worksharing;
                      cloud model sharing with simultaneous users
```

No single realization is the definition. Object-first authoring dominates full-BIM practices; classification of existing geometry is the common bridge for CAD-established offices; construction-side detailing extends the model to fabrication grade.

## How It Works

A typical project moves through the following loop — not strictly linearly, but as repeated model → derive → exchange → change cycles:

**1. Set up the project and its standards.**
Start from a template; establish levels and grids, units, and location/site context; configure the classification system and element libraries the project will use; and, where the project has information-delivery requirements, configure what data the model must carry and in what form it will be exchanged.

**2. Author elements.**
Practitioners create the building by placing and editing elements — drawing walls, slabs, and roofs; inserting doors and windows into their hosts; adding structure and services per discipline. Depending on the product philosophy this happens through parametric element tools, through freeform modeling later classified into elements, or by converting imported 2D/3D data and scans into classified elements. Elements are placed at real-world scale and carry their data from the moment of creation.

**3. Derive documentation and data.**
Plans, sections, elevations, and 3D views are generated from the model; schedules and quantity take-offs are computed from the element data. Because these are derived, they stay consistent as the model changes — the discipline that defines the Type.

**4. Enrich and verify the data.**
Properties and classifications are refined so the model can serve downstream uses; in standards-driven projects the model is checked against the agreed information requirements. Some products include model-quality checks such as collision identification inside the authoring environment, though thorough cross-discipline checking is usually a separate coordination activity.

**5. Exchange with other parties.**
The model — or discipline-relevant parts of it — is exported in exchange formats (IFC for cross-vendor exchange, native formats between matching tools) and imported models from other disciplines are brought in for reference and overlay. Issues raised by other parties flow back (increasingly through standardized issue-exchange formats) and become model changes.

**6. Change and re-derive.**
Design evolution, coordination results, and site feedback all arrive as model edits; every derived drawing, schedule, and quantity regenerates. Managing that change — knowing what the model looked like at each issue, and keeping issued documents tied to the model state they were produced from — is part of the daily workflow.

**7. Work as a team on one model.**
Where teams share a model, the authoring tool's sharing mechanism divides the work so that people do not silently collide — whether by partitioning regions/levels, by reservation of elements, or by cloud synchronization.

### What is core, common, and optional

- **Defining core** — element-based model, element data, single-source derivation of outputs.
- **Common mature structure** — parametric element toolsets, documentation generation, schedules/take-offs, libraries, levels/grids, IFC/BCF exchange, multi-user sharing, visualization, site context.
- **Variant or optional** — discipline scope (architecture-wide vs structural/fabrication vs engineering conversion), scan-to-BIM intake, collision checking in the authoring tool, analytical-model bridges to engineering analysis, information-requirement checking, cloud collaboration platforms, AI-assisted classification or modeling, fabrication-machine integration.

## Interfaces

The following surfaces are described conceptually; exact names and layouts vary by product.

### 3D model viewport

The spatial working surface.

- the building model in 3D — orbit, zoom, walk-through; visual styles from plain model to textured
- primary actions: create and edit elements, inspect element geometry and data, review spatial relationships

### 2D plan / drawing window

The plan-oriented working surface — historically the primary one, still where much element placement happens.

- the floor plan (or section/elevation) as a scaled, measured view of the model
- primary actions: draw walls and partitions, place openings and components, dimension, annotate

### Element tool palette and properties panels

How elements get created and controlled.

- a tool per element type plus generic modeling tools; selecting a tool and clicking in plan or model places an element configured by its properties
- properties panels define and edit what an element is: dimensions, materials, classification, data fields

### Project navigator

The map of the model's structure.

- levels/stories, views (plans, sections, elevations, 3D), schedules, and sheet layouts
- primary actions: create views and sheets, control what each view displays, navigate the model

### Schedule / table surface

The tabular face of the element data.

- tables computed over the model's elements (schedules, material lists, quantities)
- primary actions: define which elements and fields appear, read/export quantities, in some products edit the model through the table

### Library / type manager

Access to reusable element types and content.

- element type catalogs, office templates, manufacturer content
- primary actions: search, load, place, save custom types

### Exchange and classification surfaces

How the model meets the outside world.

- import/export dialogs and mappings for IFC and CAD formats; classification assignment; issue exchange; where present, information-requirement checking
- primary actions: export model parts, import external models, assign/verify classifications, send/receive coordination issues

### Collaboration console (when present)

Shared-model administration — team members, access, synchronization state. Present in products and editions with multi-user sharing.

## Important Rules / Behaviors

### Edit the model, not the outputs

Derived views, schedules, and take-offs are regenerated from the model; editing them independently is either impossible or temporary. This is the defining discipline of the Type — a tool whose drawings silently drift from its model is not doing BIM authoring, whatever its marketing says.

### Elements carry their context

An opening exists in its wall; a stair connects its levels; a duct connects its system. Placement and editing are constrained by those relationships, which is what keeps the model coherent as it grows — and what distinguishes a classified element from a decorated solid.

### Data must survive leaving the tool

The model's value depends on its information remaining meaningful after export — to another discipline, another tool, or the project archive. Open exchange standards exist precisely for this, and products differ in how faithfully their data translates; lossy exchange is a known hazard, especially for geometry-only imports that arrive without element semantics.

### The model obeys the project's information requirements

In standards-driven projects, the model is not free-form: agreed requirements define which elements must carry which data and to what level of development. Authoring teams configure and check against these requirements; conformance is part of the deliverable, not an afterthought.

### Shared models must not collide

Where several people author one model, the sharing mechanism enforces non-conflicting work — nobody silently overwrites a colleague's elements. The mechanics vary by product; the guarantee is structural.

### Model versions underlie issued documents

Every issued drawing set corresponds to a model state. Practitioners manage revisions so that any delivered document can be traced to the model content it was derived from.

### Exceptions the workflow must absorb

- **Discipline divergence** — other parties' models evolve independently; the authoring tool shows them as references/overlays, and reconciling differences happens through exchange and coordination, not through the authoring tool's own consistency machinery (which stops at its own model).
- **Semantics-free imports** — geometry from generic CAD or scans arrives without element identity or data; converting it into real elements is a distinct, often labor-intensive workflow.
- **Existing conditions and remodeling** — as-built conditions are captured (increasingly via scan-to-BIM conversion) and new work is modeled against them.
- **Exchange loss** — translated models may lose types, properties, or relationships; teams verify round-trips rather than trusting them.

## Variants

- **Architecture-first BIM authoring platform** — the full building design authored as the information model; typical of architecture practices delivering BIM projects.
- **Drafting-hybrid authoring** — precision 2D drafting and free modeling in one environment with the BIM layer adopted "at your own pace"; serves offices with deep drawing-era standards.
- **CAD-native BIM conversion** — BIM capability inside a familiar CAD platform: existing 2D/3D assets and scans are classified into elements and enriched with data; the low-cost bridge from drawing practice to information modeling.
- **Constructible detailing** — fabrication-grade structural authoring (steel connections, rebar, precast) whose data drives fabrication machinery; centered on the construction phase and the fabricator/contractor audience.
- **Multi-discipline suites** — one vendor family spanning architecture, structure, and services, with discipline-specific authoring products sharing exchange conventions.
- **Mandate-driven openBIM depth** — the same Type tuned by regional/public-client requirements for information delivery, with heavier classification and requirement-checking machinery.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Architecture Design Application | closest sibling — heavily conflated in the market | centers on the architect's design and its documentation deliverable; this Type centers on the data-rich element model as the shared cross-discipline information asset. The same leading products often occupy both lenses; the overlap is flagged as a taxonomy issue |
| BIM Coordination | downstream consumer | federates models authored elsewhere to detect/resolve cross-discipline conflicts and manage issues; it does not author elements |
| Structural Engineering Design / MEP Design / Civil / Site Design | discipline siblings | engineering objects and analysis (member design, duct sizing, grading) as the primary structure; authoring products offer these only as extensions, and construction-side detailing sits on the boundary |
| Mechanical CAD | adjacent engineering authoring | precise part/product modeling without building-element semantics, building scale, or building information deliverables |
| 3D Modeling Application (general) | tool-sibling | freeform geometry without element identity, classification, or data extraction; a general modeler approaches this Type only when its geometry is classified into data-bearing elements |
| Quantity Takeoff / Construction Estimating | downstream consumer | measures and prices from model element data; the authoring tool's take-off is an output, not its center of gravity |
| Construction Reality Capture Platform | data source | captures and processes scans; converting scans into classified elements (scan-to-BIM) is an intake capability of this Type |
| Construction / Engineering Document Management | downstream | manages produced documents and transmittals; authoring creates the model the documents depict |
| Digital Twin Platform | downstream / lifecycle | operates the asset over its life; authoring tools may deliver model data toward it |

The most consequential boundary is with **Architecture Design Application**: current-market language uses "BIM software" for the same tools this document and that document both describe. The working distinction — which artifact is the system of record, the design's documentation or the shared data-rich model — separates the lenses, but the overlap is real and is recorded as an open taxonomy issue.

## Representative Products

- Graphisoft **Archicad** — architect-first BIM authoring with strong openBIM positioning
- **Vectorworks Architect** — drafting-and-modeling hybrid with a BIM data layer
- **BricsCAD BIM** — CAD-native BIM: classification/conversion of 2D, 3D, and scanned assets in a DWG platform
- **Tekla Structures** — constructible structural detailing for engineers, detailers, and fabricators
- **ALLPLAN** — multi-discipline BIM suite for modeling and design documentation
- Autodesk **Revit** — the market-dominant BIM platform, listed for market completeness (its documentation could not be reviewed in this research pass; see Sources)

## Sources

Research date: **2026-09-06**

- Bricsys — BricsCAD BIM product page: https://www.bricsys.com/en-intl/bim/ ; BIM toolset page: https://www.bricsys.com/bricscad/features/bim
- Trimble — Tekla Structures product page: https://www.tekla.com/products/tekla-structures
- Nemetschek ALLPLAN — product page (ALLPLAN Concept): https://www.allplan.com/products/allplan-architecture
- buildingSMART International — openBIM overview (IFC / IDS / BCF / bSDD definitions): https://www.buildingsmart.org/about/openbim/
- Graphisoft — Archicad product page: https://graphisoft.com/archicad
- Vectorworks — Architect product and capabilities pages: https://www.vectorworks.net/en-US/architect , https://www.vectorworks.net/en-US/architect/capabilities

> Sourcing limitation: Autodesk's product and help domains for Revit returned 403 / script-only pages on 2026-09-06 (in both this and the same-day Architecture Design Application research pass) and were abandoned per source-access rules; Revit is therefore not characterized in this document, and no claims are made about it. The Graphisoft help center was likewise unreachable, and no Tier-1 operational help documentation for any BIM authoring product was reachable in either pass — product evidence rests on official product pages plus the buildingSMART standards pages. Accordingly, no precise operational details (exact sharing mechanics, exact format-version support, numeric limits, defaults) are asserted in this document; such detail as was recorded remains in the paired Research Notes.
