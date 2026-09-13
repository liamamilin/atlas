# Mine Planning Application

## Overview

A **Mine Planning Application** is the mining engineer's planning system of record for a mineral deposit: it turns a deposit model into engineered extraction geometry, evaluates that geometry against the model to produce reserves, and time-phases those reserves into a production schedule — answering, in the industry's own framing, **where and when to mine**.

The defining core is small:

```text
Deposit model (the plan's substrate)
└── Mine design (engineered extraction geometry — the "where")
    └── Reserves (design evaluated against the model — the "how much")
        └── Schedule (material assigned to periods — the "when")
            └── The plan of record, iterated as scenarios and handed to operations
```

Everything else commonly associated with the category — 3D visualization, pit and stope optimization engines, cut-off grade policies, automatic scheduling, haulage optimization, cloud processing — is widespread in current products but is not what makes the product a mine planning application. Paper-era planning (design drawings, reserve calculations, period schedules) and 1980s–90s desktop products satisfy the same core without any of it.

When the dominant object shifts from the plan to the live execution of the mine, the product is drifting toward a different Application Type (Mining Operations Management, Mining Fleet Management). When the dominant work is constructing the interpretive geological model itself, that is Geological Modeling territory.

## Users & Context

The primary user is a **mine planning engineer** — sometimes split by horizon into strategic/life-of-mine planners, medium-term planners, and short-term planners — working in the technical services department of a mining company or in a mining consultancy.

Typical work:

- design or update pit, dump, ramp and road geometry (open pit), or stopes, development and shaft/decline layouts (underground)
- evaluate what the design contains in tonnes and grade
- build and maintain production schedules across planning horizons
- compare alternative designs and schedules as scenarios
- report the plan and reconcile it against what the mine actually mined

Secondary users include geologists (who supply the deposit model), surveyors (who supply as-mined topography), geotechnical engineers (whose slope constraints bound the design), and operations staff (who receive the plan). The work environment is desktop workstations handling large 3D datasets; some vendors add cloud processing for schedule optimization. Planning runs on a cycle: strategic plans set the life-of-mine shape, and short-term plans are refreshed as new survey, production and model data arrive.

## Core Model

### The Defining Core

**Deposit model (planning substrate).** A persistent volumetric model of the mineral deposit — most commonly a block model: the deposit divided into blocks, each carrying estimated attributes (grade, density, rock type). The plan consumes this model; every quantity the plan speaks in (tonnes, grade, metal content) is computed by intersecting mine geometry with it. In split-product ecosystems the model is imported from a separate geological modeling product; in integrated products it may also be created in-product. The substrate is the concept — the block model is its dominant implementation, not the definition.

**Mine design (extraction geometry).** The engineered shapes of extraction, authored and edited in 3D:

- *Open pit:* pit shells and final pit designs built from benches, with ramps and haul roads spiraling between them, plus waste dumps and landforms. Designs must adhere to geotechnical constraints — batter angles, berms, bench heights, slope angles per geotechnical domain.
- *Underground:* mineable shapes per mining method (sub-level stoping, cut-and-fill, room-and-pillar, caving), connected by a development network — drives, levels, crosscuts, declines, ramps, shafts — plus ventilation and other ancillary development.

Designs are typically produced both interactively (drawing and editing in the 3D scene) and automatically (pit-shell optimizers, ramp generators, stope optimizers, auto-development tools), then refined into practical mining shapes.

**Reserves (design evaluated against the model).** The evaluation step that makes design speak in quantities: the designed geometry is intersected with the deposit model to compute tonnage, grade and content per mining unit — bench, stope, development length — under cut-off and economic rules (loss and dilution applied, economic block values computed). This is what turns "a shape" into "so many tonnes at so many grams per tonne, available from this period."

**Schedule (the time-phased plan).** The designed mining units assigned to time periods — periods that coarsen with horizon, from fine periods in short-term plans to years in life-of-mine plans — under constraints: equipment and fleet availability, site calendars, production and blending targets, mining sequence and dependency rules (what must be mined before what), and downstream process capacity. Schedules span planning horizons from strategic life-of-mine down to short-term execution plans, and can be built manually or by rules-based/optimization engines. The schedule is the artifact the name "planning" hangs on.

**Scenarios.** Because the future is uncertain, the plan lives as a set of alternatives: multiple designs, schedules, cut-off policies and sequencing options are run, compared on physical and economic outcomes, and iterated as new data arrives.

### Capabilities Shared by Mature Products

- **3D visualization environment** — design data, triangulations, drillholes, the deposit model and the schedule in one navigable scene.
- **Pit optimization** — computing ultimate and nested pit shells under slope constraints with an economic objective (net present value), providing the starting shells that designs are refined from.
- **Cut-off grade optimization** — variable cut-off policies over mine life to maximize project value.
- **Stope optimization** — automatically generating highest-value stope solids with pillar and dilution parameters for underground mines.
- **Rules-based and optimization-driven scheduling** alongside manual scheduling; resource leveling across equipment pools.
- **Design↔schedule linkage** — converting designs into schedulable tasks and dynamically updating the schedule when the design changes (and vice versa).
- **Reporting and plotting** — production reports, dashboards, plan drawings, spreadsheet export; results written back into the deposit model.
- **Reconciliation and compliance** — comparing the plan against as-mined topography and production; checking compliance to design and to plan.

### One Structure, Many Implementations

```text
Concept:   Deposit model substrate
Implementations:  block model (dominant), stratigraphic/seam models, imported grid models, paper-era sections

Concept:   Engineered extraction geometry
Implementations:  pit shells/benches/ramps/dumps; stopes/development/shafts; longwall layouts; cave networks

Concept:   Reserves
Implementations:  in-product reserving engines; optimizer on-the-fly reserving; imported reserve reports

Concept:   Schedule
Implementations:  Gantt-based manual scheduling; rules-based auto-scheduling; NPV optimization engines; block-by-block sequencing

Concept:   Scenario iteration
Implementations:  scenario managers; parallel optimization runs; sensitivity analysis; schedule-vs-model comparison
```

## How It Works

### The planning loop

```text
Import/receive the deposit model
→ design extraction geometry (pit or underground), honoring geotechnical and method constraints
→ evaluate the design against the model (reserves: tonnes, grade, content)
→ schedule the mining units into periods with resources and targets
→ compare scenarios; iterate on economics, constraints and new data
→ report the plan; hand it to operations
→ as the mine advances, reconcile plan vs actual and re-plan
```

This loop is the interaction core of the Type. It runs at every horizon — a strategic planner may iterate it over the whole life of mine; a short-term planner runs it weekly against fresh survey and production data.

### Open-pit design in practice

```text
Start from an optimized pit shell (or draw the pit outline)
→ generate benches, ramps, berms, switchbacks (automatically or interactively)
→ adjust geometry against geotechnical domain constraints
→ break the bench into mineable solids/blocks
→ reserve the solids against the block model
→ pass the mining units to the scheduler
```

### Underground design in practice

```text
Define mining shapes per method (stopes, rooms, panels)
→ optimize stope layout (highest-value solids, pillar/dilution parameters) or design manually
→ generate the development network connecting them (drives, declines, shafts, level access)
→ reserve shapes and development against the model
→ schedule development and production with dependencies (development before stoping)
```

### Scheduling in practice

```text
Convert designs into schedulable tasks (mining units with quantities)
→ assign resources (equipment individually or as pools) and site calendars
→ set targets (production, blending, product specs) and constraints (sequence, capacity)
→ schedule manually on a Gantt timeline, or by rules, or by optimization engine
→ check the schedule against targets; adjust; lock a period; publish
```

### Scenario iteration

```text
Duplicate the plan as a scenario
→ change an input (cut-off policy, pit shell, fleet, sequencing)
→ re-reserve and re-schedule
→ compare outcomes (tonnes, grade, value, practicality)
→ adopt, refine, or discard
```

### Core vs Common vs Optional

**Defining core** — without these, not a mine planning application:

- deposit model as planning substrate
- engineered extraction geometry (mine design)
- evaluation of design against the model (reserves)
- time-phased extraction schedule

**Common mature structure** — present in most modern products:

- 3D visualization environment
- pit optimization, cut-off grade optimization, stope optimization
- rules-based/optimization scheduling alongside manual scheduling
- resource and calendar modeling; production/blending targets
- design↔schedule dynamic linkage
- scenario management and sensitivity analysis
- reporting, plotting, export; write-back into the model
- reconciliation/compliance surfaces

**Variant / optional** — depends on commodity, method, packaging, deployment:

- method/commodity packaging (open-pit metals, underground metals, coal/stratigraphic, oil sands, caving)
- packaging architecture (one integrated product vs split design/scheduling products vs dedicated strategic optimizers)
- haulage/fleet optimization in-plan; waste dump and landform optimization
- drill & blast design; survey processing; grade control; geotechnical analysis suites
- cloud/SaaS processing; data/workflow governance layers; environmental/closure design

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### 3D design viewport

The engineer's primary workspace.

- the deposit model, design solids, drillholes, surfaces and as-mined topography in one scene
- primary actions: draw and edit design geometry, slice/section, run Boolean operations, query attributes, animate the schedule through time

### Design tool palettes / wizards

Structured generators for standard geometry.

- pit generators (shells → benches → ramps), road/ramp designers, stope optimizers with parameter wizards (orientation, widths, dilution), auto-development designers
- primary actions: set parameters, run, review results in the viewport, refine

### Attribute / block tables

Tabular views over the model and the design.

- block attributes, mining-unit properties, reserves by unit
- primary actions: filter, interrogate, edit attributes, write data back to blocks

### Scheduler (Gantt timeline)

The schedule surface.

- mining units as bars across periods; resources and calendars alongside; targets and actuals overlaid
- primary actions: assign, sequence, level resources, run rules/optimization, edit in place, compare horizons

### Scenario manager

The comparison surface.

- list of plan alternatives with their assumptions and outcomes
- primary actions: duplicate, modify inputs, run, compare results, promote a scenario to the working plan

### Reports / dashboards / plotting

The communication surface.

- production reports by period, reserve statements, plan drawings and plots, dashboards with charts
- primary actions: generate, filter, export (spreadsheets, plots), publish to stakeholders

## Important Rules / Behaviors

### The design must honor the ground

Design geometry is bounded by geotechnical constraints (batter angles, berms, bench heights, slope angles per domain) and by mining-method geometry (minimum mining widths, pillar requirements, dilution allowances). A design that violates them is not mineable; products enforce or check these constraints during design and optimization.

### Quantities come from the model, not from the drawing

Reserves are computed by intersecting design with the deposit model. When the model updates (new drilling, reconciliation), the plan's quantities change — plans are re-evaluated and re-scheduled on new data rather than rebuilt from scratch.

### The schedule is constrained from many directions

Equipment and fleet capacity, site calendars, production and blending targets, sequence dependencies (development before stoping underground, waste and ore sequencing in open pits), and downstream process capacity all bound what a valid schedule looks like. Manual and automatic scheduling coexist: engineers typically hand-tune short-term detail and let rules or optimizers propose strategic sequences.

### The plan is a living record, iterated as scenarios

Plans are rarely single artifacts: alternatives are run in parallel, compared, and refined. Sensitivity of outcomes to economic parameters (prices, costs, cut-off) is a standard check before adopting a plan.

### The plan meets the mine at a compliance seam

The schedule is handed to operations as the plan the mine executes against; actual survey and production come back and are reconciled against it (compliance to design, compliance to plan). Persistent divergence drives re-planning. The execution itself belongs to neighboring Types (operations/fleet management), not to the planning application.

## Variants

- **Open-pit metals planning** — pit shells, nested pits, cut-off grade policy, haulage; the classic strategic-planning heartland.
- **Underground metals planning** — stope optimization, development networks, dependency-heavy scheduling.
- **Coal / stratigraphic planning** — seam models, strip scheduling, longwall and dragline workflows, washability.
- **Bulk/soft-rock and oil-sands planning** — landform and material-movement-heavy design.
- **Strategic optimizer products** — dedicated life-of-mine optimization tools (scenario/NPV engines) at the strategic pole of the same Type.
- **Integrated suite vs split products** — one product carrying design+reserves+schedule, or separate design (CAD) and scheduling products dynamically linked; both realize the same core.
- **Horizon-specialized tools** — strategic, medium-term, and short-term planners as separate products or modes.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Geological Modeling Platform | upstream, strongest boundary | constructs the interpretive geological model from sparse observations; the mine plan consumes that model. Vendors split them into different products and publish models across the seam; the block model sits on the seam (geology builds it, planning consumes reserves from it). Remove model construction → still mine planning; remove the plan → still geological modeling |
| Mining Operations Management | downstream | runs the mine on execution records (production, material movements, shift data); the plan is its input and its compliance reference. Remove the future-facing plan → still operations |
| Mining Fleet Management | downstream, adjacent | live dispatch and telemetry of equipment; planning's haulage work is in-plan (routes, cycle times, fleet sizing), not live control |
| CAD | adjacent capability | mine design uses CAD techniques, but its objects are mine-specific (mining blocks, pit shells under slope constraints, stopes with dilution) and its purpose is extraction planning (reserves + schedule). Generic geometry editing alone is CAD territory |
| Project Management / Construction Scheduling | adjacent | schedules activities with resources, but its tasks are WBS activities, not deposit-derived material quantities with grade and blend targets |
| Quarry Management | sibling (§20) | shares geometry+reserves+scheduling grammar at the aggregates tier; different commodity context and market tier — deserves its own research pass |
| Civil / Site Design | adjacent | earthworks design shares terrain tools, but lacks the deposit model, reserves and extraction scheduling |

## Representative Products

- **Maptek Vulcan** (+ **Evolution** for scheduling) — classic integrated 3D mine planning environment; design, reserving, optimization and scheduling as add-ons and companion products
- **Deswik** (Deswik.Spatial, Deswik.Planning, Deswik.SO, Deswik.SPD, Deswik.APEX) — split design(CAD)/scheduling architecture with dynamically linked products and a dedicated optimizer family
- **Micromine Beyond** (+ Alastri / Spry / Advance) — integrated design+optimization+scheduling product with method-specific planning siblings

Market anchors also used to position the Type (operational documentation not reachable during research; no operational claims drawn from them): **GEOVIA** (Whittle — strategic mine planning; MineSched; Surpac) and **Hexagon Mining** (MinePlan).

## Sources

Research date: **2026-09-09**

Official vendor product documentation (product and add-on pages):

- Maptek — Vulcan: https://www.maptek.com/products/vulcan/index.html
- Maptek — Vulcan Open Pit Design: https://www.maptek.com/products/vulcan/open_pit_design.html
- Maptek — Vulcan Underground Design: https://www.maptek.com/products/vulcan/underground_design.html
- Maptek — Vulcan Open Pit Optimisation: https://www.maptek.com/products/vulcan/open_pit_optimisation.html
- Maptek — Evolution: https://www.maptek.com/products/evolution/
- Deswik — home and product pages (Spatial, Planning, SO): https://www.deswik.com/ , https://www.deswik.com/products/spatial , https://www.deswik.com/products/planning , https://www.deswik.com/products/so
- Micromine — home and Beyond: https://micromine.com/ , https://www.micromine.com/beyond/
- GEOVIA — Whittle (page title only): https://www.3ds.com/products/geovia/whittle

> Sourcing limitation: vendor help-center portals (Maptek Help, Deswik Help) are JavaScript applications or login-gated and could not be fetched; GEOVIA and Hexagon Mining product pages were unreachable from the research environment. All operational statements in this document are calibrated to official product-page evidence; precise numeric limits, algorithm parameters, defaults and step-by-step procedures are intentionally not stated. Detailed observations, cross-product comparison and the boundary analysis are recorded in the paired Research Notes.
