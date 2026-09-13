# Structural Engineering Design

## Overview

A **Structural Engineering Design** application is the structural engineer's workbench for proving that a load-bearing structure — a building frame, a bridge, a tower, an industrial or specialty structure — can safely carry its loads. It holds the structure as an engineered model, subjects it to defined loading, computes how the structure responds, and checks every element against the rules of a recognized structural design standard. The output is a verified design plus the calculation record and construction deliverables that follow from it.

The defining structure is small:

```text
Structural model of record
└── Loading regime (load cases → combinations)
    └── Structural response (internal forces, deflections, reactions)
        └── Code-based verification & sizing
```

Everything else commonly associated with these products — finite element meshing, automated wind and seismic load generation, reinforcement design, connection and foundation modules, BIM exchange, cloud delivery — is widespread in current products but is not what makes the product a structural design tool. Remove the loading-and-analysis loop and the product is a CAD modeler with structural vocabulary. Remove the code-bound verification and the product is a general analysis/simulation tool. Remove the computed response and only component calculators remain.

## Users & Context

The primary user is a **structural engineer in a design office**, working on the load-bearing structure of a construction project. The engineer's relationship to the software is that of an author and a verifier at once: they build the structural model, decide the loading and the structural system, and then demand that the software prove — element by element, against the governing standard — that the design works.

Secondary users and consumers:

- **checking/reviewing engineers** (within the office or at reviewing authorities) who read the calculation record and inspect the design checks
- **BIM coordinators and architects**, whose building geometry feeds the structural model and whose models receive the verified structure back
- **detailers, fabricators and contractors**, who consume beam reactions, bracing forces, reinforcement drawings, and material take-offs
- **students and educators**, whom several products serve through dedicated tiers and free tools

The work context is the consulting engineering office. The governing design standard is that of the project's jurisdiction, which makes the code ecosystem — not the software — the source of the engineering rules. The software sits between the architect's building design (upstream) and construction (downstream), and its results are the engineer's professional evidence that the structure is safe and code-compliant.

## Core Model

### The Defining Core

Four parts, jointly held:

**1. The structural model of record.** The load-bearing structure exists as a persistent, editable, real-world-scaled model. Its elements — members (beams, columns, braces, cables) as the canonical class, plus surfaces and solids in finite-element-based products — carry structural properties: cross-section, material, connectivity and end conditions. Supports ground the structure to its foundations. The model is the subject of everything else; loads act on it, analysis computes through it, checks apply to its elements.

**2. The loading regime.** Loads are first-class managed data, not annotations. They are organized as **load cases** (self-weight, dead, live, wind, snow, seismic, thermal, imposed deformations), and in mature practice they are combined into **load combinations** — commonly generated automatically according to the selected design standard's combination rules. Many products generate environmental loads (wind, snow, seismic) from code procedures rather than requiring hand entry.

**3. The structural response.** Analysis is an explicit computation step in which the software determines how the structure responds to the loading: internal forces (axial, shear, moment, torsion), deflections and deformations, support reactions, and stresses. The response belongs to the current state of the model — it is recomputed when the model or loading changes. The solution method (frame stiffness method, finite element method) is an implementation choice; what is defining is that the software computes the structure's response to its loads at all.

**4. Code-based verification and sizing.** The computed response is checked, element by element, against a recognized structural design standard: strength (is the member strong enough), stability (will it buckle, is it too slender), serviceability (does it deflect too much). The result is expressed as a utilization/capacity ratio with pass/fail semantics — the ratio exceeding 1.0 means the element fails the check. Verification drives sizing: the engineer resizes elements, or lets an optimizer propose sections, until the checks pass. The specific code family (European, American, Australian, Indian, and others) is a regional variant; the invariant is that the check binds to a recognized standard, which is what makes this engineering *design* rather than mere analysis.

### Standard Capabilities of Mature Products

These are not part of the definition, but mature products carry most of them, and they make the type practical:

- **section and material libraries** — catalogs of standard profiles and materials, with custom section builders
- **finite element modeling** — surfaces and solids with automated meshing, for slabs, walls, shells and complex geometry
- **code-based load generation** — wind, snow and seismic loads produced from standard procedures for the building's geometry and site
- **advanced analysis types** — second-order (P-Delta) analysis, buckling analysis, modal and response-spectrum (seismic) analysis, staged construction analysis
- **per-material design modules** — steel member design, reinforced concrete design with reinforcement calculation and detailing output, timber, cold-formed steel; often packaged as add-on modules or separate products in a suite
- **connection and foundation design** — steel joint and base-plate checks, footing and pile design, commonly fed by the superstructure's computed reactions
- **design optimizers** — automatic proposal of the lightest/cheapest passing sections
- **calculation documentation** — report composition with the design checks' own formulas visible or embedded; in some products reports update automatically as the model changes
- **construction deliverables** — reinforcement drawings, steel tonnages, material take-offs, exported member reactions for contractors
- **exchange and automation** — CAD/BIM interoperability (including IFC and bidirectional links to building-model tools), and programmatic APIs

### One Structure, Many Implementations

The core is written conceptually. Current products realize each concept differently:

```text
Concept:  structural model of record
Realized as:  analytical-first member/plate models drawn directly in the tool;
              physical building models auto-converted into an analytical model;
              2D frame models

Concept:  loading regime
Realized as:  hand-entered load cases; code-schema combination generators;
              dedicated load generators (wind/snow/seismic per standard)

Concept:  verification & sizing
Realized as:  integrated design modes; purchasable per-material add-on modules;
              cooperating suite products per component (frame, floor, connection, foundation)

Concept:  calculation documentation
Realized as:  composed report documents with embedded check formulas;
              calculation reports linked to the model and regenerated on change
```

A reader who has only seen one implementation — say, a desktop finite-element package — should still be able to recognize a 2D frame tool, a cloud app, or a building-specialized design product as the same type.

## How It Works

The working loop of the type is: **model → load → solve → review → verify → iterate → document**.

**Establish the structural model.** The engineer draws the structure on grids and elevations with snapping aids (nodes, members, supports), or imports geometry from a building model or CAD file and assigns structural meaning to it. Sections and materials are assigned from libraries; connectivity and support conditions are set. In physical-model-first products, the engineer models the real building elements and the software derives the analysis model automatically; in analytical-first products, the drawn model is itself the analysis model.

**Define the loading.** Self-weight is usually computed from the model. Dead, live and other use loads are entered as cases and applied to members, surfaces or areas. Wind, snow and seismic actions are commonly generated from the applicable standard using the structure's geometry and site parameters. Load combinations are then produced — typically auto-generated per the selected standard's combination rules, editable by the engineer.

**Solve.** The engineer runs the analysis — an explicit action with its own settings (analysis type, solver parameters) and its own failure paths: models are validated or repaired first, and solvers report errors and warnings (unstable or ill-conditioned models among them). The output is the structure's response for every load case and combination.

**Review the response.** The engineer inspects deformed shapes, force and moment diagrams along members, stress contours on surfaces, and reaction tables — looking for unexpected behavior before any check is run.

**Verify against the standard.** The engineer selects the design standard and runs the design checks. The check module carries the analysis results into the design layer automatically — internal forces including their load combinations — and checks each member on the worst case across those combinations. The engineer controls the design parameters that standards require judgment for: braced and unbraced lengths, effective length factors, deflection and slenderness limits. Results appear as utilization ratios with pass/fail coloring directly on the model and in tables; elements that cannot be checked (unsupported section shapes, for example) are flagged rather than silently skipped.

**Iterate.** Failed elements are resized — manually or with an optimizer — and the loop re-runs: any change to the model, loads or combinations makes the previous results stale and demands a fresh solve and fresh checks. This change-recompute discipline is the type's central rhythm; scheme comparison (several alternative structural systems) is a common extension of it.

**Document and deliver.** The engineer composes the calculation report — the professional record of model, loads, analysis and checks — and produces construction-facing outputs: reinforcement drawings and quantities, steel schedules and tonnages, member reactions for the contractor, and the structural model itself exchanged back into the project's BIM environment.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### 3D workspace / viewport

The central surface, serving both modeling and results.

- the structure in 3D (or 2D), navigable and rotatable; elements colored by assigned properties during modeling and by results or check ratios after analysis
- primary actions: draw/duplicate/modify elements, assign properties, apply loads, inspect result displays

### Data navigator and tables

The model's data in structured form alongside the graphic view.

- tree navigator organizing elements, loads, and results; spreadsheet-style tables where element and load data can be created and edited en masse
- primary actions: create/edit records, filter, switch between data, display and result views

### Load case / combination manager

The loading regime's control surface.

- list of load cases with types and assignments; combination definitions and their generation schema; load groups
- primary actions: add cases, apply loads to elements, generate combinations per standard, edit generated sets

### Solve / analysis control

- analysis type selection, calculation parameters, model validation and repair; solver progress and error/warning reporting
- primary actions: validate model, run analysis, read diagnostics

### Results views

- deformed-shape animation, internal force diagrams along members, stress contours on surfaces, reaction and result tables, section cuts
- primary actions: switch result types and combinations, query values, annotate

### Design-check surfaces

- per-material check modules: member tables with engineering parameters, worst-case forces shown per combination; model colored by utilization ratio (passing / near-limit / failing / not checked); check detail views exposing the governing case
- primary actions: select standard and module, adjust design parameters, run checks, review pass/fail

### Reporting and exchange

- report composer assembling model, loads, results and checks (often with the checks' formulas); export of drawings, schedules, quantities, reactions; BIM/CAD import and export; API access

## Important Rules / Behaviors

**Results belong to the current model state.** Every edit — geometry, section, load, combination — invalidates previously computed results until the analysis is re-run. Some products make the discipline explicit (model validation before solving, stale-result states), and some regenerate linked documentation automatically when the model changes; the underlying rule is the same: reported numbers must correspond to the model they claim to describe.

**The worst case governs.** Verification evaluates each element across all load combinations and checks against the most demanding one. A member that passes under gravity loading can still fail under a wind or seismic combination; the check surface therefore always works with combination sets, not single load cases.

**The design standard is the authority.** The selected standard determines both the loading procedures (load generation, combination rules) and the check rules (strength, stability, serviceability formulas). Changing the standard changes what the software computes and demands — which is why code selection is a project-level setting, and why products maintain many regional standards.

**Transparency of the check is structural.** These products are used to produce evidence for review and approval, so the checks are inspectable: governing combinations, computed capacities and utilization ratios are displayed, and calculation reports expose the checks' formulas. The software checks; the engineer remains the decision-maker — design parameters that require engineering judgment (effective lengths, limits, boundary conditions) stay under the engineer's control.

**Unchecked is not passing.** Elements that cannot be checked by the selected module — unsupported section shapes, custom sections, missing material data — are reported as not checked, not as passing. This keeps silent gaps out of a safety-relevant record.

**Conventions matter.** Sign conventions for forces and moments, and unit systems, are explicit user-facing settings, because misread forces propagate directly into wrong designs.

## Variants

- **Packaging**: main program with purchasable per-material add-on modules; a cooperating suite of single-purpose products (frames, floors, connections, foundations) exchanging data; a single integrated product with no modules; cloud SaaS with free/education tiers
- **Model philosophy**: analytical-first products where the drawn model is the analysis model; physical-first building products that auto-derive the analytical model from constructible building elements
- **Regional code ecosystems**: products anchored in particular standards families with localized national parameters, extending to multi-standard global coverage
- **Structure domain**: general-purpose products for all structure types; building-specialized products (gravity + lateral systems, staged construction); bridge and specialty-structure work within the same core; component-level modules (connections, base plates, footings, retaining walls) sold both embedded and standalone
- **Audience and scale**: education-oriented tiers and free calculator tools at the entry end; mid-size engineering offices as the volume market; large-project and enterprise deployments at the top
- **Deployment**: desktop applications with local licensing; browser-delivered cloud applications with mobile companions; hybrid with cloud computing for heavy solves

## Related Application Types

| Application Type | Distinction |
|---|---|
| CAE / Engineering Simulation | simulates an engineering artifact's physical behavior with general FEA; does not bind results to a construction design standard or produce construction deliverables. Remove the code-bound check here and the product drifts into CAE territory. |
| BIM Authoring | owns the data-rich element model as the project's cross-discipline record; the analytical model used for verification here is a derived, reduced representation exchanged with it. |
| Architecture Design Application | the architect's surface: spatial and geometric building design plus documentation. This type verifies load-bearing behavior of the structure. |
| MEP Design | sibling in the building-design family (context + designed objects + engineering sizing/verification loop + deliverables), but for building-services networks; its loads derive from rooms and occupancy, while structural loads come from self-weight, use, and environmental code actions. |
| Civil / Site Design | authors proposed land-form objects (routes, grading) against measured existing ground; its evaluation is geometric (cut/fill, slopes), not response-then-code-check. |
| Mechanical CAD | models manufactured products for fabrication; this type models load-bearing structures for construction. |
| Quantity Takeoff / Construction Estimating | downstream consumers of structural outputs (quantities, tonnages); they measure and price the design but do not verify it. |

The sharpest boundary is with general simulation: the defining act of this type is not computing a structure's behavior but *judging it against a design standard* and producing the evidence that it complies.

## Representative Products

- **Dlubal RFEM 6** (with per-material add-on modules) — modular European analysis + design family
- **SkyCiv Structural 3D** — cloud/browser analysis + design platform with per-code design modules
- **Tekla Structural Designer** — building-focused, one-model analysis + design with BIM synchronization
- **RISA-3D / RISAFloor / RISAFoundation / RISAConnection** — cooperating suite with a separation-of-tasks philosophy
- **SCIA Engineer** — integrated multi-material analysis + design for all structure types with openBIM exchange

The wider market also includes long-established analysis/design platforms (e.g., Robot Structural Analysis, SAP2000/ETABS, STAAD, MIDAS) that were not directly documented in this pass; no operational claims are made about them here.

## Sources

Research date: **2026-09-10**

- Dlubal Software — RFEM 6 product page: https://www.dlubal.com/en/products/rfem-fea-software
- SkyCiv Engineering — product page: https://www.skyciv.com/structural-3d/
- SkyCiv Engineering — Software Documentation (Structural 3D: Modelling, Members, Applying Loads, Solving, Design, Post Processing, Reporting; Integrated Member Design): https://skyciv.com/docs/ and https://skyciv.com/docs/skyciv-member-design/general/integrated/
- Tekla (Trimble) — Tekla Structural Designer product page: https://www.tekla.com/products/tekla-structural-designer
- RISA Tech, Inc. — product family site and FAQ: https://risa.com/
- SCIA — SCIA Engineer product page: https://www.scia.net/en/scia-engineer

> Sourcing limitation: official documentation of several widely referenced market platforms (Autodesk, Bentley, CSI) was not accessed in this pass; they are named only as market context. Precise operational facts (numeric limits, defaults, code-edition lists, prices) observed on vendor pages were deliberately kept out of this document. Vendor marketing claims (user counts, code-coverage breadth) are not repeated as facts.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
