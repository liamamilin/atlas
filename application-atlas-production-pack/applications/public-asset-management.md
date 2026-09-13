# Public Asset Management

## Overview

A **Public Asset Management** application is a public agency's system of record for the physical infrastructure estate it stewards — the roads, bridges, sidewalks, traffic signals, streetlights, signs, trees, parks and grounds assets, storm and waste lines, public buildings, and vehicles that make up a community's built environment.

It solves a specific stewardship problem: a public agency owns thousands of long-lived physical assets, funded by constrained public money, expected to deliver a safe and reliable level of service, and answerable to councils, oversight bodies, and residents for every dollar spent. The application gives the agency one durable register of what it owns and where, attaches every inspection and maintenance action to the asset it was performed on, and rolls condition, cost, and risk up into defensible decisions — what to fix, what to replace, what to defer, and how to justify those choices to the people funding them.

The defining core is small, and it is shared with the broader asset-management family:

```text
Public asset register of record
└── Recorded care attached to each asset
    │   (inspections/condition + work orders → persistent per-asset history)
    └── Lifecycle outlook feeding stewardship decisions
        (condition/cost/risk → repair-vs-replace → multi-year plans → funding justification)
```

held by a **public-steward operator**: an agency managing the estate in trust for public service, where the records exist to make stewardship defensible rather than to generate profit. What distinguishes this Type from generic enterprise asset management is that estate and that frame, not any single feature.

## Users & Context

The primary users are the agency staff who operate and steward the estate:

- **asset stewards / engineers** — build and maintain the register, define asset classes and attributes, own condition standards and long-term plans
- **inspectors and field crews** — capture condition in the field, execute and close work orders, update asset information from mobile devices
- **work schedulers / operations supervisors** — triage requests, schedule crews and contractors, balance workloads
- **capital and finance staff** — track cost per asset, model funding scenarios, prepare capital programs and budget justification

Secondary participants:

- **contractors** — deliver outsourced maintenance work inside the same system
- **residents** — commonly report issues (potholes, broken lights, damaged signs) through a public portal and track progress
- **council / oversight bodies** — consume the reports and evidence the system produces

The work environment spans office and field: desktop planning and analysis surfaces, mobile devices for crews working across a dispersed estate (often offline), and map-based views because the estate lives in public space.

## Core Model

### The Defining Core

**1. The public asset register of record.** One durable, individually identified record per physical asset, classified by category, class, and type, carrying the attributes the agency needs (location, installation/construction data, condition, cost history). Two properties make this register distinctive:

- *The estate is mixed civil infrastructure.* Unlike a plant's equipment list or a building's equipment systems, the population spans point assets (signals, lights, signs, benches, trees), linear and network assets (road segments, sidewalks, pipes), facilities, and often vehicles — organized by asset class rather than by a single equipment taxonomy.
- *Assets are located in public space.* Every asset sits somewhere in the field, and its location is part of its identity. Modern products realize this through GIS — embedded GIS platforms, native GIS capabilities, or synchronization with an external GIS — but the conceptual requirement is the located asset population, not any particular GIS machinery.

**2. Recorded care attached to each asset.** Every act of care — an inspection, a condition assessment, a repair, a preventive maintenance visit — is captured as a record bound to the asset it concerns, executed (often by crews or contractors in the field) and closed into persistent per-asset history: what was done, when, by whom, at what cost. Requests from staff or residents enter the same pipeline, converting into asset-bound work. This history is the agency's memory; it is what later condition judgments, warranty questions, and budget cases are built from.

**3. Lifecycle outlook feeding stewardship decisions.** Condition, age, usage, and cost accumulate on each asset and roll up across the estate into forward-looking judgment: which assets are deteriorating, where risk is mounting (commonly framed as likelihood of failure weighted by consequence), what should be repaired versus replaced, and what the multi-year maintenance and capital program should be under the funding actually available. The output of this leg is characteristically public: reports and dashboards that show the reasoning behind spending decisions and the impact of infrastructure investment — the evidence used to justify budgets to funders.

**The public-stewardship frame.** The operator is a public agency; the estate is held for public service; the money is public money. This frame does not add a fourth structure — it shapes what the three structures are for. The register exists because the public deserves to know what it owns; the history exists because spending must be accountable; the outlook exists because limited funds must be prioritized and defended.

### Standard Capabilities

Mature products commonly add, without these defining the Type:

- a work-order engine covering reactive and planned/preventive maintenance, with scheduling, assignment, and completion recording
- inspection programs with schedules, checklists, and condition scoring
- service-request intake (staff and, commonly, resident portals) converting into asset-bound work
- mobile field execution with offline support, photos, and location awareness
- contractor management — contracted work brought into the same system and schedule view
- per-asset cost rollup (labor, parts, vendor/contractor spend)
- map-based display of assets, work, and requests
- dashboards, KPIs, and risk scoring
- capital/renewal planning views: spend against budget, funding sources, project approval tracking
- configurable asset templates, hierarchies, and attribute sets

### One Structure, Many Implementations

```text
Concept:   Located asset population
Realized as:  embedded GIS platform, native GIS engine, synchronization with an
              external GIS, or plain location attributes

Concept:   Care request intake
Realized as:  internal staff requests, public resident portal, field observation,
              inspection findings

Concept:   Lifecycle outlook
Realized as:  risk dashboards, what-if funding scenarios, deterioration modeling,
              component-level valuation, capital project lists
```

A reader who encounters only one realization (say, a product with an embedded GIS platform) should still be able to recognize products built on the other patterns from this core model.

## How It Works

The typical operating loop runs from knowing the estate to defending the spend:

**1. Build and maintain the register.** The agency consolidates what it owns into the register — asset records with class, attributes, and location. Vendors' own implementation guidance stresses this step: an accurate registry of assets, condition data, and maintenance history is the foundation everything else depends on. The register is never finished; assets are added, replaced, and retired as the estate changes.

**2. Inspect and capture condition.** Scheduled inspection programs and field observations update each asset's condition. Findings raised during an assessment can become work orders directly. Condition, with age and usage, is the raw material for every later decision.

**3. Run the care loop.** Requests arrive (from staff, from residents, from inspections), become work orders bound to specific assets, get triaged, scheduled, and assigned to crews or contractors, and are executed — increasingly from mobile devices, often offline — and closed with labor, parts, and cost recorded back onto the asset.

**4. Roll up and prioritize.** Condition, cost, and risk roll up per asset and across each asset class. Risk views highlight where failure likelihood and consequence are highest; backlog and cost trends show where deferred maintenance is accumulating.

**5. Plan and justify.** The agency models scenarios — what different budget levels, timelines, and work mixes do to condition and risk over multiple years — selects the optimal mix of work against its objectives, and produces the reports that show the reasoning behind the plan and the impact of investment. This is where the system earns its public keep: the difference between "we need more money" and "here is the evidence that we need more money."

**6. Serve the public.** Resident-reported issues flow into the same work pipeline; progress is visible back to the resident as work moves from scheduled to in-progress to complete. Response timeliness and visible progress are themselves stewardship outcomes the agency is judged on.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Map / GIS view

The spatial face of the estate.

- assets, work orders, service requests, and projects displayed on a map of the community
- primary actions: locate an asset, see what work is active where, select assets for inspection or work

### Asset register (list and detail)

The system of record itself.

- asset records organized by category/class/type with configurable attributes; drill-down through class hierarchies
- per-asset detail: location, condition, installation data, work and cost history, attachments
- primary actions: create/edit assets, open related work, review history

### Work management surfaces

Where care is organized.

- work-order lists and detail (status, assignee, asset, costs), scheduling views for crews and contractors, request queues
- primary actions: triage requests, create/schedule/assign work orders, record completion

### Mobile field app

The crew's surface.

- assigned work, asset lookup, condition capture, photos, completion recording — usable offline
- primary actions: complete work orders, update asset information, manage requests

### Dashboards and reports

The stewardship-evidence surface.

- condition and risk summaries, backlog and cost trends, program performance, benchmarking comparisons (in some products)
- primary actions: review, configure, export/share for budget and oversight audiences

### Capital planning views

The forward-looking surface.

- renewal/replacement candidates, multi-year programs, spend against budget and funding sources
- primary actions: model scenarios, prioritize projects, track approvals and spend

### Public request portal

The resident-facing surface (common, not universal).

- issue reporting with location, request tracking as work progresses

## Important Rules / Behaviors

- **The asset record is the anchor.** Inspections, work orders, costs, and requests bind to assets; the register's integrity is what makes history, condition, and planning coherent. Implementation guidance from vendors consistently frames registry quality as the precondition for reliable reporting and planning.
- **Care history accumulates and is never discarded.** The per-asset record of what was done, when, at what cost is the basis for troubleshooting, warranty and audit questions, and repair-vs-replace judgment.
- **Condition drives priority.** Maintenance and renewal priorities are derived from condition, risk, and service-level objectives — not from first-in-first-out queuing. Risk framing (likelihood × consequence) is a common realization.
- **Funding is the binding constraint.** Plans are built against available budgets and funding sources; scenario comparison exists precisely because the agency cannot afford everything the estate needs.
- **Requests become asset-bound work.** A resident report is not a free-floating ticket; it attaches to the asset in question and joins the same care pipeline as internally generated work.
- **Location is structural.** Work is scheduled and allocated against where assets are; spatial display reduces the effort of day-to-day work. The GIS realization varies (embedded, native, integrated), but the located-asset character does not.
- **Evidence is an output, not a byproduct.** Reports showing the reasoning behind decisions and the impact of investment are a first-class product of the system, consumed by councils, oversight bodies, and the public.

## Variants

- **GIS posture** — GIS-centric platforms built on an embedded GIS engine (with linear-referencing support for road networks); products with their own native GIS; products that synchronize with an external GIS. The seam matters for licensing cost and data ownership, not for the core model.
- **Strategic depth** — operational work-management-first products versus strategic asset-management-first products that emphasize condition modeling, deterioration prediction, funding scenarios, and even component-level depreciation accounting.
- **Regional vocabulary and regime** — US public-works and state-DOT practice; UK council and highways practice; Australian and New Zealand council practice with long-term financial plans and regulatory reporting. The core model is the same; the vocabulary and reporting obligations differ.
- **Asset-class breadth** — whole-of-agency estates versus department-scoped deployments (a parks department, a facilities portfolio, a fleet operation). Fleet in particular is sometimes served by a sibling product rather than included.
- **Citizen engagement depth** — public request portals with visible progress tracking versus internal-only request intake.
- **Maturity packaging** — some vendors package capability tiers (foundational register and work management → condition modeling and funding scenarios → sensor-based monitoring), reflecting adoption stages rather than different Types.
- **Packaging** — standalone products versus modules of broader government suites; cloud versus hosted deployment.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Enterprise Asset Management (EAM) | same family, generic | shares the register + work + whole-life core; EAM serves any asset-intensive operator, without the public-infrastructure estate or the public-stewardship frame |
| CMMS / Maintenance Management | contained core | the care loop (assets + work orders + history) is the maintenance-operations center; this Type adds estate breadth, lifecycle outlook, and stewardship |
| Enterprise Asset Registry | record layer only | a registry holds the per-item records; strip the care loop and lifecycle outlook and only the registry remains |
| Public Works Management | adjacent, unprocessed sibling | centers the public-works department's operations; this Type centers the asset estate's lifecycle — asset management is one system public-works teams use |
| Government GIS | adjacent | the GIS maintains the jurisdiction's georeferenced layers; this Type centers asset records and their care, consuming GIS as a location substrate |
| Capital Improvement Planning | downstream consumer | CIP decides which new/renewal investments to fund in which years; this Type holds existing-asset condition and maintenance whose data feeds those capital needs |
| Utility Asset Management | scoped sibling (unprocessed) | utilities hold networked assets with utility operations; this Type centers the agency's mixed civil estate |
| Building Asset Management | scoped sibling | centers building equipment systems in site→building→floor locations; here facilities are one asset class within a civil-infrastructure estate |
| Parks & Recreation Administration | adjacent | treats the park as bookable venue inventory and program catalog; here the park appears as maintained asset estate |
| 311 / Citizen Service Request Platform | intake channel | centers the citizen request case; here resident requests are one intake into asset-bound work |
| Fleet Management System | asset-class overlap | centers vehicles and their operations (telematics, drivers, fuel); here vehicles are one class in the estate, sometimes served by a sibling product |
| Building Condition Assessment | upstream deliverable | produces the quantified condition survey; this Type is the living system of record that consumes condition data and acts on it |

The most important boundary is with **EAM**: the structural core is genuinely shared, and vendors sell into both worlds. What makes this a distinct Type is the estate (mixed public civil infrastructure, located in public space) and the frame (publicly funded stewardship whose records must justify spending to external funders and serve residents). Remove the frame and the estate and the product is simply EAM.

## Representative Products

- **Trimble Unity Maintain** (Trimble; the merged Cityworks and AgileAssets line) — GIS-centric public-infrastructure asset management for cities, state DOTs, utilities, and airports
- **Brightly Assetic** (Siemens) — cloud strategic asset management with a class-configured register, assessments, work management, and component-level accounting; strong in Australian and New Zealand government
- **Brightly Confirm** (Siemens) — asset management for government infrastructure (UK councils and highways): centralized register, native GIS, contractor management, community engagement, benchmarking
- **AssetWorks EAM, Government & Public Works** — public-sector asset management spanning public works, facilities, parks, and (via a sibling product line) government fleet

The core model was checked against the already-processed generic family members (CMMS, EAM, Enterprise Asset Registry, Building Asset Management) and against paper-era municipal practice to avoid over-fitting to any one region, era, or vendor pattern.

## Sources

Research date: **2026-09-09**

- Trimble Unity Maintain — https://www.cityworks.com/ (redirects to the Trimble Unity Maintain product page); https://www.trimble.com/en/products/trimble-unity
- Brightly Assetic — https://www.brightlysoftware.com/products/assetic
- Brightly Confirm — https://www.brightlysoftware.com/products/confirm
- AssetWorks EAM (Government & Public Works) — https://www.assetworks.com/eam/ ; https://www.assetworks.com/eam/asset-management-software/
- Brightly government use case — https://www.brightlysoftware.com/use-cases/government

> Sourcing limitation: official help-center / user-guide articles were not reachable for any sampled product; evidence comes from official product, use-case, and case-study pages. Operational specifics (condition-scoring scales, risk formulas, planning horizons, numeric limits, default settings) are intentionally not stated. Cartegraph, OpenGov, and Tyler Technologies product pages were unreachable (access denied), so the US pure-play local-government pole is evidenced indirectly through the sampled products' government positioning and public-sector case studies. Detailed observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
