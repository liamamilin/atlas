# Soil Management

## Overview

A **Soil Management** application is the agriculture-domain system of record for the soil resource itself. It holds the measured state of the soil of a farming operation's land units — fertility and chemistry (pH, nutrients, organic matter) and, where kept, physical and biological condition — as an accumulating record; it runs the measurement cycle (sampling, testing, result matching) that produces and refreshes that record; and it turns the record into decisions and actions on the soil — lime and amendments, fertility programmes, soil-health practices — whose effects the next measurement round reveals.

The defining core is small:

```text
Identified land unit (field / paddock / zone / sample point)
└── Soil record of record
    │   (measured soil state per unit, commonly per depth,
    │    accumulating across sampling rounds and years)
├── fed by → the measurement cycle
│   (sample plans → field collection → laboratory analysis
│    → results matched back to the correct location)
└── drives → the soil-management decision layer
    (amendments, fertility programmes, soil-health practices;
     recommendations → plans → recorded applications)
```

Everything else commonly associated with the category — grid or zone sampling designs, barcodes and GPS capture, laboratory feeds, variable-rate maps, carbon programmes, compliance reporting — is widespread in current products but is not what makes the product a soil-management application. The pre-digital routine (a per-field soil-test file, lime decided from the report, a re-test a few years later) satisfies the same core with no software at all.

When the center of gravity shifts to the crop cycle, the water decision, the nutrient-input regime, or the land asset itself, the product has drifted into a neighboring Application Type (Crop Management, Irrigation Management, Nutrient Management, Field Management).

## Users & Context

The Type is operated from two directions, and most of the market sits between them:

**Service pole (the dominant professional realization):**

- **Agronomists and advisors** — manage soil data and fertility decisions across many client farms; produce recommendations and reports the client acts on.
- **Soil-sampling service providers and contractors** — run sampling campaigns across many farms in tight seasonal windows: plan sample points, coordinate field samplers, hand over to laboratories, deliver mapped results.
- **Carbon and natural-capital programme teams** — run large soil-measurement programmes with protocol and audit requirements (a variant pole).

**Self-serve pole:**

- **Growers and farm managers** — track their soil's fertility and health themselves, decide lime and amendments, and watch change over seasons.
- **Farm field staff** — collect samples and record observations in the field, often offline.

Laboratories are counterparties (results flow in from them), not the operating users; the laboratory's own side belongs to laboratory information systems. In service deployments the farmer commonly has read-only visibility of results and reports.

The working rhythm is multi-year: soils change slowly, so the record is refreshed on a sampling cycle set by the farming calendar and judged over seasons, not days.

## Core Model

### The Defining Core

**1. The soil record of record.** The soil of each identified land unit — field, paddock, zone, or sample point — is held as measured data: test and analysis results describing the soil's state. The canonical properties are fertility and chemistry: pH, macro- and micro-nutrients, organic matter (with cation-exchange-class measures where kept). Mature products extend the record to physical condition (structure, compaction, moisture-holding) and biological condition (biology indicators, earthworm-class counts). Results attach to the unit — commonly per sampling depth — and accumulate across sampling rounds and years, so each unit carries a soil history, not just a latest value.

**2. The measurement cycle.** The soil's state is not self-reported; it is established by measurement. The dominant implementation is the sampling-and-testing loop: a sampling plan defines where samples come from (whole-field composites, zones, grids, or fixed points), field collection captures each sample with its location identity (GPS position, barcode or sample ID, depth, photos and notes), samples are submitted to a laboratory, and the returning results are matched back to the correct unit, depth, and round. The cycle re-runs on a cadence, which is what keeps the record current and makes change visible. Equivalent measurement realizations exist — in-field self-tests recorded directly in the app, sensor scans, satellite/model inference — but the record is always measurement-based.

**3. The soil-management decision layer.** The record exists to drive and account for decisions about the soil itself: correcting pH with lime, balancing fertility with fertiliser and amendments, building organic matter and structure, and adjusting practices (cover crops, tillage, conservation measures) that act on the soil. The decision layer appears in three depths: advisory (summaries and recommendations the user acts on), planned (fertiliser/lime programmes and application maps), and recorded (applications logged against the plan, with planned-vs-actual comparison). The next measurement round is the loop's verification: it shows whether the management worked.

Remove the soil record → sampling logistics with no soil data. Remove the measurement cycle → a one-off test report or recommendations on assumed data. Remove the decision layer → a soil data archive, measurement without management.

### Standard Capabilities

Mature products commonly add, without these defining the Type:

- **Sampling campaign machinery** — sampler tasking, point navigation, barcode/sample-ID capture, photo and note records, depth and round metadata, offline capture with later sync.
- **Laboratory integration** — submissions tied to samples, result feeds by file or API, automated matching of results to the right location.
- **Map-first presentation** — farm and field maps with colour-coded soil data (nutrient maps, pH maps), results as layers over boundaries.
- **Multi-year trend views** — compare results across rounds and years per field, zone, or point; benchmarking against regional values in some products.
- **Fertility and amendment planning outputs** — fertiliser and lime plans, variable-rate application maps derived from soil indexes.
- **Soil health reporting** — farm-level soil health reports, indicator summaries, benchmarks.
- **Multi-client operation** — client/property registries, manager dashboards, farmer read-only logins, white-label delivery for sampling businesses.
- **Compliance and audit reporting** — records packaged for regional nutrient or conservation programmes, certification, and audit.

### One Structure, Many Implementations

```text
Concept:            Soil state of a land unit
Implementations:    laboratory analysis of sampled soil (dominant),
                    in-field self-tests, sensor scans,
                    satellite/model inference

Concept:            Sampling design
Implementations:    grid, zone-based, composite/paddock, fixed-point
                    trails, stratified; model-guided point reduction

Concept:            Decision output
Implementations:    advisory summary, fertiliser/lime plan,
                    variable-rate application map,
                    recorded application with planned-vs-actual
```

A reader who has only seen grid-sampled, laboratory-analyzed soil data should still be able to recognize a farmer's spade-test soil-health log or a satellite-inferred soil map as the same Type from the Core Model.

## How It Works

### The measurement cycle

```text
Plan the round
→ define sample units (zones / grid / points / composites) and depths
→ collect in the field
   (navigate to points, capture GPS/barcode/depth, photos, notes)
→ submit to the laboratory
→ results return and are matched back
   to the correct unit, depth, and round
→ the soil record updates; history is retained
```

The identity chain — sample → location → depth → round — is the cycle's discipline. A result matched to the wrong field poisons the record; keeping samples, submissions, and results tied together from the start is the operational problem this cycle exists to solve.

### The decision loop

```text
Read the record (per field/zone: pH, indexes, organic matter)
→ decide the soil action
   (lime to correct pH, fertiliser/amendment to balance indexes,
    practices to build OM and structure)
→ hold it as recommendation, plan, or application map
→ apply (and record what was applied, in mature implementations)
→ next measurement round reveals the effect
→ adjust over seasons
```

### The multi-year arc

Soil management is judged across years, not days: a baseline round, practice changes, re-measurement, trend comparison. Products therefore treat historical rounds as retained record, not superseded scratch data, and surface "changes over time" as a first-class view.

### Capability tiers

**Defining core** — without these, not soil management:

- soil record of record per identified land unit (measured, accumulating)
- measurement cycle producing and refreshing the record
- soil-management decision layer (amendments / fertility / soil-health practices)

**Standard capabilities** — present in most mature products:

- sampling campaign machinery; laboratory integration
- map-first soil data presentation; multi-year trends
- fertility/amendment planning outputs; soil health reports
- multi-client delivery; compliance/audit reporting

**Variant / optional** — depends on segment, region, and business model:

- carbon-programme machinery (protocols, audit-grade traceability)
- variable-rate application maps; model-guided sample-count reduction
- sensor and satellite inference substrates
- regional nutrient-management planning modules
- environmental/natural-capital assessment baselining
- white-label delivery; farmer read-only portals

## Interfaces

Described in conceptual terms; exact layouts and names vary by product.

### Farm/field map with soil layers

The primary orientation surface. Fields or paddocks displayed with colour-coded soil data (nutrient index, pH, organic matter); clicking a unit opens its soil detail. Primary actions: inspect a unit's soil state, start a sampling plan, open results.

### Sampling plan / campaign dashboard

The round-planning surface for service operations. Sample units on a map, sampler assignments, progress tracking, submission status. Primary actions: create/adjust sample plans, task samplers, track the round from collection to lab to results.

### Mobile field collection app

The sampler's surface. Point navigation, GPS capture, barcode/sample-ID scanning, depth selection, photos and notes, offline operation with later sync. Primary actions: record a sample's collection identity, complete a task.

### Results view

Per unit (and per depth where kept): measured values in tables and charts, threshold flags (deficiency alerts), and the unit's result history. Primary actions: read the state, compare rounds, flag concerns.

### Trend / comparison view

Change over time per field, zone, or point; cross-field and cross-farm comparison; benchmarks where offered. Primary actions: compare periods, identify improving or degrading units.

### Report builder / client reports

The outward-facing surface: farm-level soil health or fertility reports, client-branded in service deployments, audit-grade exports where regimes require. Primary actions: generate, brand, share.

### Suite-embedded surfaces

In ERP and agronomy-suite realizations, these surfaces appear as the soil module inside a wider product, with soil data flowing to crop planning, procurement, and financials.

## Important Rules / Behaviors

- **Result matching is the record's integrity rule.** A laboratory result must land against the correct unit, depth, and round; the whole workflow is built to keep sample identity unbroken from field to lab to record.
- **The record is cumulative.** New rounds add to the soil's history rather than replacing it; multi-year retention is what makes trend judgment — and therefore management — possible.
- **Measurements are estimates of parts, not the whole.** A sample represents its zone, grid cell, or point — not the entire field; the sampling design determines what the data can support, and recommendations are made against the tested indexes, not beyond them.
- **The decision layer is bounded by the measurement.** Lime and amendment decisions answer the record's findings (e.g., a pH or index reading); products flag deficiencies and concerns from the data rather than from assumptions.
- **Soil moisture sits at a coordination seam, not at the center.** Moisture sensing and monitoring appear in soil records, but the water decision belongs to irrigation management; soil products coordinate with it rather than decide it.
- **Compliance artifacts are regime-bound.** In regulated settings, the soil record feeds official reporting (regional nutrient-management planning, conservation-programme documentation, certification audits); the regimes vary by geography and are packaging, not structure.

## Variants

- **By purpose pole:**
  - *agronomic fertility* — pH, lime, P/K indexes, fertiliser planning (the classic center)
  - *soil health / regenerative* — biology, structure, organic matter; spade-test self-monitoring with benchmarks
  - *soil carbon programmes* — SOC stock measurement under protocols with audit-grade traceability
  - *environmental / natural-capital assessment* — farm baselining and indicator monitoring
- **By operating side:** agri-service and sampling contractors (campaign machinery, white-label) · advisors/consultants (multi-client recommendation practice) · grower self-serve · ERP module inside a farm enterprise system.
- **By data substrate:** laboratory-dominant; in-field self-tests; sensor scans; satellite/model inference.
- **By regional regime:** nutrient-management-planning jurisdictions, conservation-programme documentation, certification schemes — the record's compliance packaging varies; the core does not.

A variant remains a variant unless it changes the core: a product whose center is the carbon credit programme or the laboratory's own workflow belongs to a different Type even though it measures the same soil.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Nutrient Management | centers nutrient inputs as materials (fertiliser/manure budgets, application planning, regulation); soil management centers the soil resource itself — the soil test is the shared artifact, and fertility planning is the shared seam |
| Agronomy Management | the multi-domain recommendation practice (seed + nutrients + protection) on the field record; soil data and lime/fertility recommendations are inputs to it; soil management ships as a module inside agronomy suites and equally as standalone products |
| Field Management | centers the land asset (extent, boundaries, standing characterization) with soil as one attribute family; soil management centers the measured soil state and its improvement loop |
| Irrigation Management | centers the water decision; soil moisture sensing is its data substrate, and soil products coordinate with rather than decide watering |
| Precision Agriculture Platform | centers the variable-rate prescription-execution loop; soil management produces the soil-data basis from which VRA maps may be built |
| Agricultural IoT Platform | centers the connected field-device fleet and telemetry; in-ground soil probes are its devices, lab sampling is soil management's substrate |
| Carbon Accounting (§21) | centers the emissions/credit programme; soil-carbon measurement under protocols serves it — a soil product whose center is carbon programmes belongs there |
| Laboratory LIMS | runs the laboratory's side (sample registration, analysis, QC); soil management consumes results and manages the farm/advisor side of the handover |
| Agricultural GIS | centers the georeferenced land base; soil data appears there as layers, without the measurement cycle or decision loop |
| Contaminated Site Management (§21) | soil as pollution subject under remediation regimes — shared measurement machinery, different subject and context |

The closest boundary is **Nutrient Management**: both read the same soil test, but one manages the soil resource (its state and improvement) while the other manages nutrient inputs (their budgeting, application, and regulation). The seam is flagged for joint review when that leaf is processed.

## Representative Products

- **GXLab** (FarmLab, Australia) — measurement-workflow platform spanning sampling → lab → analysis → reporting across agronomy, carbon, and natural-capital programmes
- **Senus Soil** (Ireland) — sampling-campaign management with protocol traceability, soil health/carbon reporting, and regional nutrient planning
- **KORE** (SoilEssentials, UK) — white-label precision-farming portal for agronomists and soil-sampling companies; soil sampling and VRA lime/P/K apps
- **AgriERP Soil Management** (US) — soil as a module inside a farm ERP: fertility planning, testing, fertilizer/amendment tracking, financials
- **Soilmentor** (Integrity Soils, UK) — farmer self-serve soil-health testing with GPS-mapped repeat samples and benchmarks

Boundary pole examined: **LandPKS** (Terraso) — free public-good soil-science apps (soil identification, soil-health tracking) at the Type's thin, advisory edge.

## Sources

Research date: **2026-09-09**

- GXLab (FarmLab PTY LTD) — Agriculture industry page: https://gxlab.com/industries/agriculture/
- Senus — Senus Soil product page: https://senus.com/senus-soil/
- SoilEssentials — KORE product page: https://soilessentials.com/kore/
- AgriERP — Soil Management module page: https://agrierp.com/product-features/crop-management/soil-management/
- LandPKS (Terraso) — https://landpotential.org/
- Soilmentor (Integrity Soils) — https://www.integritysoils.com/pages/soilmentor-regen-platform (content captured via search index; live fetch unsuccessful)

> Sourcing limitation: no Tier-1 help centers were reachable for the sampled products in this pass; all direct evidence is official product-page level, so operational mechanics are stated at correspondingly moderate strength. The sampling-job machinery is additionally corroborated by Tier-1 documentation from a sibling pass (soil-sampling jobs, sample labeling, and lab-result import in a collaborative agronomy platform's help center). Soilmentor's evidence derives from search-captured content of its official page after two failed live fetches, and its pole's claims are kept correspondingly qualified. Precise vendor numbers (sample-reduction claims, package feature lists, program names) are recorded in the Research Notes, not asserted here.

Detailed product-by-product observations, the cross-product comparison matrix, and the boundary analysis against neighboring Types are recorded in the paired Research Notes.
