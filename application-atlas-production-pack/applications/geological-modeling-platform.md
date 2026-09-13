# Geological Modeling Platform

## Overview

A **Geological Modeling Platform** is the geoscientist's workbench for building an interpretive 3D model of the subsurface: it takes sparse observations of the real earth — drillholes, surface mapping, geophysics, points and surfaces — validates and displays them in a shared 3D scene, computes continuous geological geometry from those observations, and lets the geologist interrogate, adjust, and update the model as new data arrives. The finished geological model is then handed downstream as the foundation for resource estimation, mine planning, hydrogeology, and other technical uses.

The defining core is small:

```text
Sparse real-earth observations
└── Interpretive geological model (project of record)
    └── Data-driven construction of continuous geological geometry
        └── 3D interpretive loop (compare model ↔ data → adjust → regenerate)
```

Everything else commonly associated with these products — block models, grade estimation, collaboration platforms, market-specific editions, AI assistants — is standard or optional capability, not what makes the product a geological modeling platform. A product that designs mines on an imported model is a mine planning tool; a product that authors imagined geometry on a blank canvas is a 3D modeling tool; a product that only stores and displays observational data is a data-management tool. Geological modeling is the Type in between: **measured evidence in, interpretive geometry out**.

## Users & Context

Primary users are geoscientists — the people responsible for turning raw field observations into a defensible picture of what lies underground:

- **Exploration geologists** — visualize early drill results, build first models of a prospect, target the next drilling.
- **Resource geologists** — build and maintain the geological model (lithology units, structures, ore domains) that frames mineral resource estimation and public reporting.
- **Production / grade-control geologists** — keep the model current against daily production data and define ore boundaries for the mine.
- **Geotechnical engineers and hydrogeologists** — model rock-mass structure and groundwater conditions, often from the same project.

The work context is mining first (the market's center of gravity), with the same engines sold in editions or used directly for geothermal and other energy projects, groundwater studies, and civil/environmental work such as tunnels and dams. Secondary roles interact with the model rather than build it: surveyors contribute topographic surfaces, database administrators manage drillhole data quality, and mine planners consume the published model. One geologist typically owns a project; models are shared as read-only scenes or through collaboration layers rather than co-edited freely.

## Core Model

### The Defining Core

```text
Sparse real-earth observations
└── Interpretive geological model (project of record)
    └── Data-driven construction of continuous geological geometry
        └── 3D interpretive loop (compare ↔ adjust ↔ regenerate)
```

Four properties. If any one is removed, the product is no longer recognizable as geological modeling:

- **Sparse real-earth observations as the input of record.** Drillhole data (collars, surveys, lithology logs, assays), surface mapping, points, polylines, meshes, and geophysical data are imported, validated, and displayed in 3D. The observations are the evidence: the interpretation must honor them, and they anchor every boundary the model draws. Without this, the product is a generic 3D modeling application.
- **The interpretive geological model as the object of record.** A persistent project holds the geologist's interpretation of the geology — named units, boundaries, faults, domains — as bounded geometry in 3D space. The project persists across the life of the deposit or site and accumulates revisions. Without this, there is nothing being modeled, only data being stored or mined being planned.
- **Data-driven construction of continuous geological geometry.** The software computes continuous geometry from the sparse observations: interpolating surfaces and boundaries where the earth has not been directly sampled. How it computes them is an implementation choice — algebraic implicit interpolation, hand-guided explicit wireframing, or machine learning are all realizations of the same invariant. Without computation, the product is a viewer or a plotting tool.
- **The 3D interpretive loop.** Model and observations coexist in one 3D scene. The geologist slices through the model, compares it against the data it must honor, adjusts the interpretation, and regenerates — and when new drilling arrives, the model is updated, not redrawn from scratch. Without this loop, there is no interpretation being worked, only one-shot processing.

### Capabilities Shared by Mature Products

These are not what makes the product a geological modeling platform, but they make the work practical:

- **Drillhole database machinery** — collar / survey / log / assay tables with validation rules; import from and export to the wide range of formats the industry exchanges.
- **Domain definition** — the working act of naming and bounding geological units (lithology, alteration, ore shells) before or while geometry is built.
- **Sectioning and slicing** — cutting through model and data on any plane; generating cross-sections and plans for review and reporting.
- **Block models and estimation adjacency** — in mining, the geological model typically frames block models and grade estimation (kriging / inverse-distance class methods); some products do this internally, others hand the model to a dedicated estimation product or extension.
- **Publishing and viewers** — read-only scene files or viewers so the model can be shared with planners, reviewers, and stakeholders without a modeling license.
- **Model management and collaboration** — a layer (native or companion product) for versioning models, keeping teams current, and publishing to the cloud.
- **Georeferencing and GIS utilities** — coordinate systems, topographic surfaces, contouring, online imagery — the spatial furniture the 3D world stands on.
- **Extension surfaces** — hydrogeology (groundwater flow models), geophysics (seismic and other methods), and geotechnical analysis fed by or feeding the geology model.
- **Uncertainty tools** — visualizing where data is sparse (e.g., drillhole-spacing analysis) to guide infill drilling and model confidence.

### One Structure, Many Implementations

The core is written conceptually. Current products realize each element differently, and the differences are philosophy, not identity:

```text
Concept:  Computed continuous geometry
Realizations:  implicit interpolation (engine-driven surfaces)
               explicit wireframing (hand-guided digitising, classical control)
               machine learning (neural-network domain and grade models)
               — often mixed inside one product

Concept:  The 3D interpretive loop
Realizations:  workflow-structured steps (data → domains → model → publish)
               free-form scene interpretation (build in the 3D view)
               hybrid: repeatable steps with immediate scene feedback

Concept:  Estimation adjacency
Realizations:  built into the modeling product
               a licensed extension on the same engine
               a separate product in the same suite that the model is published to
```

## How It Works

### The interpretive workflow

The standard loop runs from raw field data to a published model:

```text
Import observations (drillholes, surfaces, geophysics, mapping)
→ validate the data (checks, corrections, deduplication)
→ visualize everything in the 3D scene alongside existing work
→ define geological domains (name and bound the units being modeled)
→ construct the model (computed geometry honoring the observations)
→ validate the model (slice it, compare it to the data, numeric checks)
→ publish / export (to estimation, mine planning, hydrogeology, viewers)
→ repeat as new observations arrive — the model updates, not rebuilds
```

Vendors describe this loop in nearly identical terms: data loading and validation first, domain definition, then generating, validating, and publishing models — with "repeatable steps" so that changing a domain updates the model immediately, and "easily update models with new data" as a standing expectation. The loop is the product's center of gravity; everything else hangs off it.

### Building the model

Construction blends computing and judgment. The geologist guides the software — through interpretation points, structural measurements, section strings, or domain rules — and the software interpolates continuous surfaces and volumes between the observations. Method choice varies by geology and by preference: automated implicit methods trade control for speed; explicit wireframing trades speed for classical hand control; machine-learning options generate candidate domains or grade shells from the sample data directly. Mature products offer more than one method in the same project, because real geology mixes easy and hard problems.

### Validating against the evidence

A geological model is only as good as its agreement with the data. Products provide dedicated validation surfaces: slicing the model in sections to compare against raw logs, checking that adjacent units line up where they meet, running numeric consistency checks, and visually comparing modeled boundaries against the drillholes that constrain them. Validation failures send the geologist back to interpretation, not to the data — unless the data itself is wrong, in which case the corrections flow back into the drillhole database first.

### Publishing downstream

The model's purpose is consumption. It is published — to a collaboration layer, a companion estimation product, a mine design suite, a flow-modeling tool, or a read-only viewer — in interchange formats the wider toolchain reads. From there, resource geologists estimate and report, planners design pits and stopes against the modeled geometry, hydrogeologists build flow models on the modeled structure. The geological model is the foundation the rest of the mining workflow builds on; vendors describe it in exactly those words.

### Core vs Standard vs Optional

**Defining core** — without these, not geological modeling:

- sparse real-earth observations as the input of record
- the interpretive geological model as a persistent project of record
- data-driven construction of continuous geological geometry
- the 3D interpretive loop (compare ↔ adjust ↔ regenerate, updating on new data)

**Standard capabilities** — present in most mature products:

- drillhole database machinery and validation
- domain definition tools
- sectioning / cross-sections / plotting
- block models and estimation adjacency (in mining realizations)
- publishing, viewers, model management
- georeferencing / GIS utilities
- wide file-format interchange

**Optional / variant** — depends on sector, scale, and product philosophy:

- grade-control machinery (dig lines, ore tracking, reconciliation)
- hydrogeology, geophysics, geotechnical extensions
- AI-assisted modeling (era-current)
- cloud collaboration platforms and enterprise deployment
- market-specific editions of the same engine

## Interfaces

Described conceptually; exact layouts and names vary by product.

### The 3D scene

The primary working surface. All observations, interpretive geometry, and model results render together in one navigable 3D environment.

- purpose: hold everything in one spatial context for interpretation and validation
- typical content: drillholes, topography, modeled volumes and surfaces, block models, imported data
- primary actions: rotate/zoom/pan, slice on any plane, display/hide layers, measure, query

### The project tree

The model's table of contents. Organizes data tables, interpretation objects, domain definitions, model outputs, and versions as a navigable hierarchy.

- purpose: structure the project of record and make objects addressable
- primary actions: create/rename/organize objects, open objects into the scene, inspect properties

### Data views and validation tools

Tabular and graphical views over the observational record — drillhole tables, log displays, validation reports.

- purpose: keep the evidence inspectable and clean before it anchors interpretation
- primary actions: import/export, validate and correct records, profile statistics, cross-plot data

### Section / cross-section surfaces

2D cutting planes through the 3D world where interpretation and checking often happen.

- purpose: compare model against data at readable scale; capture interpretation
- primary actions: position/slice sections, draw or adjust interpretation on the section, generate deliverable section plots

### Publishing / collaboration surfaces

Export dialogs, viewer applications, and (in current products) cloud layers where models are shared and versioned.

- purpose: move the model out of the geologist's hands, intact and traceable
- primary actions: publish/serialize models, manage versions, open read-only scenes

## Important Rules / Behaviors

### The observations are the anchor

The model must honor the data. Bounding geometry snaps to or is constrained by the drillhole intersections, survey paths, and structural measurements it interprets; validation is the act of checking that agreement. New observations do not merely coexist with the model — they are expected to change it.

### Models update; they are not rebuilt

The living-model behavior is structural: changes to domain definitions or newly arrived data propagate into regenerated geometry rather than requiring a manual redraw. This is why products emphasize "repeatable steps" and "dynamically updated" models — the interpretation, not the drawing, is what the geologist maintains.

### Interpretation is a hypothesis, explicitly

Because the earth is sampled sparsely, the model contains extrapolation between and beyond observations. Mature practice treats competing interpretations as alternative hypotheses to be tested against the same data; some products support scenario experimentation and comparison directly rather than forcing a single answer.

### Validation precedes publication

A model that fails its own validation checks (against data or numeric consistency) is not publishable in good practice. The publish step is a boundary: models cross it when they can serve downstream consumers, and in resource-reporting contexts the documented, auditable version of the model is what the estimate and the public statement stand on.

### Data quality gates modeling

Bad collar coordinates, survey errors, or mis-assayed intervals corrupt every geometry built from them. Products carry validation machinery — and vendors dedicate training content to it — because data quality failures are the industry's recognized workflow hazard.

## Variants

- **Implicit-first platforms** — engine-computed surfaces from data, positioning speed and automatic updating as the philosophy; explicit drawing treated as the traditional alternative.
- **Mixed-method environments** — implicit, explicit wireframing, and ML offered side by side in one product; the geologist chooses per problem.
- **Suite-embedded geology** — geological modeling as the geology pole of a broader mining suite, publishing models to the suite's design, estimation, and scheduling products.
- **Market editions of one engine** — the same core sold as mining, energy (geothermal / offshore wind / CCUS / hydrocarbon), and civil/environmental editions.
- **Workflow-stage subscriptions** — licensing by stage of the geology job (exploration → geology modeling → resource modeling → grade control → enterprise teams).
- **Grade-control realizations** — production-geology versions of the same machinery operating against daily production data.
- **Standalone versus platform-era** — desktop-installed modeling applications versus cloud-platform products with collaboration, data management, and AI services attached.

A variant stays a variant while the four-part core still applies; when the model of record stops being interpretive geology (e.g., pure mine design, or pure data management), the product has crossed into a neighboring Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Mine Planning Application | downstream sibling | designs pits/stopes/schedules consuming the geological model; the plan is its object of record, the geology model is imported context. Suites separate the two (geology modeling products publish models into mine-design products) |
| 3D Modeling Application | adjacent creation tool | authors imagined geometry from a blank canvas; geological modeling derives geometry from measurements of the real earth and must honor them |
| GIS (Agricultural / Government) | adjacent spatial tool | maps and analyzes surface features; geological modeling centers subsurface interpretive volumes. 3D GIS utilities appear inside modeling products as features |
| Digital Twin Platform | adjacent representation | models live operations against telemetry; the geology model is an iterated interpretive representation of nature, not an operations-linked twin |
| CAE / Engineering Simulation | downstream consumer | runs physics through models (flow, stress); the geological modeling platform builds the model. Hydrogeology/numerical tools exist as extensions, confirming the seam |
| Environmental Data Platform | observational-corpus sibling | holds samples/results/stations as the system of record; geological modeling consumes observations to compute interpretive geometry |
| Drillhole / sample data management products | upstream sibling | capture, manage, and quality-control the observational data; same vendors ship them as separate products feeding the modeling work |

The boundary with **Mine Planning** is the most consequential, because the block model sits on the seam: the geological model defines the domains block models are built on, while reserve consumption and mine design belong to planning. The market itself polices the boundary — vendors split geology from design into different products, and publish models across it.

## Representative Products

- **Seequent Leapfrog Geo** — implicit-modeling specialist; same engine sold as Geo (mining), Energy, and Works (civil & environmental) editions
- **Maptek Vulcan / GeologyCore** — mine-suite heritage with a dedicated connected geological modeling product publishing into the suite
- **Micromine Origin** — exploration-to-grade-control environment selling implicit, explicit, and AI-assisted modeling side by side
- GEOVIA Surpac (Dassault Systèmes) and Datamine Studio — long-established market anchors (not directly documented in this pass; see Sources)

The core was checked against the older desktop generation of mining software (drillhole databases, wireframing, block models, 3D visualisation without implicit algorithms, cloud, or AI) and against the paper-era interpretation workflow (hand-drawn sections and plans updated as drilling arrived) to avoid defining the Type by the current implicit/ML/cloud generation.

## Sources

Research date: **2026-09-08**

Primary vendor sources (fetched):

- Seequent — Leapfrog Geo product page: https://www.seequent.com/products-solutions/leapfrog-geo/
- Seequent — "What is Implicit Modelling?": https://www.seequent.com/community/learn-geoscience/implicit-modelling/
- Seequent — Help portal and Leapfrog Geo 2026.1 help: https://help.seequent.com/ , https://help.seequent.com/Geo/2026.1/en-GB/Content/intro.htm
- Maptek — Vulcan product page: https://www.maptek.com/products/vulcan/
- Maptek — GeologyCore product page: https://www.maptek.com/products/geologycore/
- Micromine — Origin product page: https://www.micromine.com/origin/ ; product family: https://www.micromine.com/

> Sourcing limitation: GEOVIA Surpac (3ds.com product pages returned 404) and Datamine (site rendered no content) could not be fetched; they are named as market anchors only and no operational claims about them appear in this document. Oil & gas subsurface modeling products were not sampled; the definition is written at a level that abstracts over their grid structures, but no first-hand sector evidence is cited. Deep help-topic pages (beyond the help-intro level) were not fetched; interface descriptions rest on help-portal-level evidence and product pages. Detailed product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
