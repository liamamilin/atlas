# Crop Management

## Overview

A **Crop Management** application manages a crop through its cycle on a specific piece of land. The managed unit of record is the **crop-season**: a defined crop (variety) grown on an identified field, plot or block for one season or production cycle. The application directs that season with a plan or schedule of operations, captures what was actually done and observed as dated records, watches the crop's condition and risk while it grows, and closes the season with a harvest outcome that is retained as history for the next cycle.

The defining structure is small:

```text
Field / plot / block
└── Crop-season (crop × land × cycle)
    ├── Plan / schedule of operations
    ├── Operation & observation records
    └── Closure & season history
```

Everything commonly associated with modern products — field mapping, input inventories, crew and labor management, sensor networks, satellite imagery, compliance audits, traceability chains — is widespread in current products but is not what makes the product a crop-management application. The pre-digital pattern (a planting plan, a spray log, a field notebook, a yield book) satisfies the same definition.

When the center of gravity shifts — to input-decision recommendations, to whole-farm business operations, to variable-rate machine execution, or to a sensing backbone — the product is drifting toward a different Application Type (Agronomy Management, Farm Management Platform, Precision Agriculture Platform, Agricultural IoT Platform).

## Users & Context

The primary user is the **grower or farm operator** — the person responsible for what happens to the crop: planning the season, deciding and scheduling operations, recording what was done, and watching the crop through the season.

Around that primary user, larger operations add roles with different relationships to the same crop-season record:

- **farm manager**: plans seasons across many fields, assigns work, watches progress and cost
- **agronomist**: advises on what to do and when; in some products configures the crop schedules and advisories that drive field work
- **supervisor / crew lead**: assigns tasks to workers, tracks completion
- **field workers and crews**: execute operations and capture records from the field, often on mobile devices
- **pest control advisors and food-safety leads** (specialty crops): use monitoring and records to time interventions and pass audits

In enterprise and contract-farming deployments, the operating organization is not the grower but an agribusiness, processor, or development program that manages **many growers' plots** through the same structures — geotagged plots, activity logs, and advisories pushed out to farmers.

The work environment follows the season: the field is the map, the season is the rhythm, mobile capture in the field is the norm, and the office watches dashboards and reports. The application is used continuously through the cycle — at planning time, daily during the growing season, intensively at harvest, and at audit time.

## Core Model

### The Defining Core

```text
Field / plot / block
└── Crop-season (crop × land × cycle)
    ├── Plan / schedule of operations
    ├── Operation & observation records
    └── Closure & season history
```

Four properties. If any one is removed, the product is no longer recognizable as crop management:

- **The crop-season as the managed unit of record** — an identified crop grown on an identified piece of land for a defined cycle. Plans, records, observations and outcomes all attach to it. Without it, the product becomes generic land records or task lists.
- **Planned/scheduled crop operations** — the cycle is directed by a plan or schedule of what will be done to the crop and when, whether built by hand, drawn from template libraries, derived from packaged crop programs, or driven by pest and disease models. Without it, the product is a record log or a monitoring dashboard.
- **Recorded operations and observations** — dated, attributed records of what was done and seen: planting, input applications, care work (pruning, thinning, mowing), scouting notes, irrigation, harvest. Without it, the product is a planning calendar with no memory.
- **Cycle closure with retained season history** — the season ends in a recorded outcome (harvest, yield, quality) and the record persists as season-over-season history that informs the next cycle. Without it, the product is a one-shot planning or logging calculator.

### Capabilities Shared by Mature Products

A typical modern crop-management product carries most of these capabilities. They are not what makes the product a crop-management application, but they make managing a crop-season practical:

- **Field/plot registry with boundaries** — mapped growing areas (fields, blocks, rows) with hazards and irrigation zones; the spatial substrate every record anchors to.
- **Crop/variety catalog and rotation** — what can be grown, what was grown before; replanting and rotation records.
- **Input/product catalogs with inventory linkage** — seeds, fertilizers, crop-protection products; applications draw down inventory automatically in several products.
- **In-season crop condition monitoring** — weather, pest and disease pressure, crop health (from sensors, satellite or aerial imagery, and human scouting), growth stage.
- **Risk alerts and advisories** — threshold-based notifications to specified recipients; spray-timing tools; weather advisories; in some products, packaged crop programs (recommended practice schedules) pushed to farmers.
- **Task and work management** — operations assigned to workers, crews or contractors, with status tracking and mobile capture.
- **Labor and cost tracking** — hours or piece rates per operation; input, labor and equipment costs accumulated per crop, field and activity.
- **Harvest/yield records and performance analytics** — yields by block and variety, best-performing comparisons, planned-versus-actual views.
- **Compliance and audit reporting** — spray and application records, food-safety and certification audit packs, traceability from field to shipment.
- **Reports and dashboards** — season progress, costs, conditions; multi-season comparison.
- **Mobile apps and integrations** — field capture on phones/tablets; connections to machinery data, weather sources, sensors and ERP systems.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. Specific products realize each concept differently:

```text
Concept:            Managed unit (the crop-season)
Implementations:    field × crop × season (row crops), orchard block (perennials),
                    geotagged smallholder plot (contract farming), greenhouse compartment

Concept:            The cycle plan
Implementations:    hand-built schedule, template library, packaged crop program (PoP),
                    model-driven timing (pest/disease degree-day models)

Concept:            Operation records
Implementations:    structured activity records, spray/application records,
                    harvest and quality records, scouting notes with photos

Concept:            In-season monitoring
Implementations:    in-field sensor networks, satellite/aerial imagery, weather data,
                    automated traps, human scouting

Concept:            Closure & history
Implementations:    yield records, quality assessments, performance analytics,
                    season-over-season comparison
```

A reader who only encounters one implementation (for example, a sensor-heavy specialty-crop platform) should still be able to recognize a records-first or planning-first product as the same Application Type from the Core Model.

## How It Works

### Set up the land and the crop

```text
Map or register fields / plots / blocks (boundaries, rows, hazards)
→ register the crop / variety to be grown
→ the crop-season begins
```

### Plan the season

```text
Build the crop plan / schedule of operations
  (by hand, from a template library, from a packaged crop program,
   or informed by models and prior-season data)
→ budget inputs, labor and costs for the season
```

### Run the season loop

```text
Scheduled operation comes due
→ assign it to a worker / crew / contractor
→ execute in the field
→ capture the record (what, where, when, who, how much)
→ inventory and costs update
→ repeat through the season
```

This plan → assign → execute → record loop is the application's working heartbeat. Records accumulate on the crop-season as it progresses.

### Watch the crop

```text
Monitor conditions (weather, pest/disease pressure, crop health, growth stage)
→ alerts fire when risk thresholds are met
→ adjust the schedule: time an intervention, add an operation, protect the crop
```

In monitoring-heavy products this loop dominates the season; in records-first products it is lighter. Either way, the crop's observed state feeds back into the plan.

### Close the season

```text
Record harvest (quantities, quality, pickers, locations)
→ compare outcomes against plan (yield, cost, performance by field/variety)
→ retain the season as history
→ next cycle starts from the accumulated record
```

### Core vs Common vs Optional

Capabilities fall into three tiers:

**Defining core** — without these, not crop management:

- crop-season as managed unit of record
- planned/scheduled crop operations
- recorded operations and observations
- cycle closure with retained season history

**Common mature structure** — present in most modern products:

- field/plot registry with boundaries
- crop/variety catalog and rotation
- input catalogs and inventory linkage
- in-season condition monitoring
- risk alerts and advisories
- task/work assignment with mobile capture
- labor and cost tracking
- harvest/yield records and performance analytics
- compliance/audit reporting
- reports, dashboards, multi-season views
- mobile apps and integrations

**Variant / optional** — depends on segment, operating side, and region:

- sensor networks and automated traps; satellite/imagery analytics
- packaged crop programs (PoP) and advisory push to farmers
- worker-safety interval automation (re-entry / pre-harvest windows)
- post-harvest modules: packing, storage, shipping traceability
- computer-vision quality and yield estimation
- multi-grower enterprise hierarchies; development-sector deployments
- grain marketing and finance (belongs to the neighboring farm-management Type)

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Field / plot map

The spatial entry surface.

- growing areas with boundaries, blocks and rows; status overlays (conditions, alerts, recent activity)
- primary actions: select a field or block, inspect its crop-season, locate work

### Crop-season / field detail

The record surface for one crop on one piece of land.

- the season's plan, recorded operations, observations, inputs and costs in one place
- primary actions: review history, add a record, compare planned vs actual

### Activity capture (mobile)

The field surface where work is recorded as it happens.

- operation-specific capture forms (spray/application, practice work, harvest, scouting, irrigation)
- primary actions: record an operation with date, location, product/inputs, quantity, person; scan or tag inventory where supported

### Schedule / task board

The forward-looking surface.

- planned operations by date, field and crop; assignments and completion status
- primary actions: schedule or reschedule an operation, assign people, mark complete

### Monitoring & alerts

The in-season risk surface.

- current conditions per field/block (weather, pest counts, disease risk, crop-health indicators), alert history, forecast views
- primary actions: set or adjust thresholds, choose alert recipients, act on an alert (schedule a response)

### Harvest & yield records

The closing surface.

- harvest events with quantities, quality, locations and pickers; yield by block and variety
- primary actions: record harvest, view yield reports, compare performance

### Reports & compliance

The outward-facing surface.

- spray/application reports, audit packs for food-safety and certification schemes, traceability reports from field to shipment
- primary actions: generate a report for a period/field/audit, share with auditors or buyers

### Settings / administration

- fields and boundaries, crops and varieties, input products, people and roles, alert configurations

## Important Rules / Behaviors

### Everything anchors to the crop-season

Records are not free-floating notes: an operation record belongs to a crop, on a field or block, at a date, by a person. This anchoring is what makes the accumulated record usable for audits, traceability and next-season planning.

### Operations are dated and attributed

The who-what-where-when of each operation is the audit spine. Food-safety and certification regimes in the specialty-crop segment treat these records as first-class output; products are built so the record exists as a byproduct of doing the work.

### Safety windows can govern the field

Application records matter beyond bookkeeping: re-entry and pre-harvest intervals are regulatory realities in sprayed crops, and some specialty-crop products compute these windows directly from the spray record — alerting when an interval ends and warning when work is scheduled in an area that is not yet safe to enter. The intervals themselves are regulatory; computing them from records is a product capability, not a universal.

### Planned vs actual is the standing comparison

The season's plan is the reference against which recorded operations, input usage, costs and yield are compared. This comparison is how performance by field, variety and practice becomes visible.

### The season closes; history persists

A crop-season ends — typically at harvest — but its record does not disappear. Season-over-season history is the substrate for rotation decisions, performance benchmarking and the next cycle's plan.

### Monitoring feeds the plan, not just the report

Alerts and advisories are actionable: they exist to change what happens next in the field (time a spray, irrigate, protect against frost), not merely to document conditions.

## Variants

The Type is implemented differently across crop segments and operating models. Common variants:

- **row-crop / field-scale** — large fields, machine-data-heavy capture, season plans and input costs; often bundled inside broader farm-management products
- **specialty horticulture (fruit & vegetable)** — block- and row-level records, crew and piece-rate labor, worker-safety windows, food-safety traceability and audits
- **perennial / orchard crops** — multi-year blocks, bloom-to-harvest monitoring, pest and disease models, thinning and harvest-timing decisions
- **enterprise / contract farming** — an agribusiness manages many growers' geotagged plots; packaged crop programs and advisories pushed to farmers via app or SMS
- **monitoring-heavy service pole** — sensor networks installed and maintained by the provider; models and alerts drive intervention timing; records and reports surround the monitoring core
- **development-sector / smallholder digitization** — plot registration, simple activity logs, SMS advisories; deployed by programs, governments and buyers rather than by growers themselves

A variant remains a **Variant** unless it changes users, core objects, workflow or rules so much that the Core Model no longer applies — in which case it is a neighboring Type (see below).

## Related Application Types

| Application Type | Distinction |
|---|---|
| Agronomy Management | centers the input-decision practice: field test data → professional recommendation → execution record; crop management centers the season's operation record. Agronomic knowledge appears in crop management as plan inputs (templates, crop programs, models), not as the recommendation artifact |
| Farm Management Platform | centers whole-farm business operations — finance, grain marketing, inventory, payroll; crop management centers the crop cycle itself. Row-crop products often bundle both |
| Precision Agriculture Platform | centers the variable-rate execution loop (prescription → machine → as-applied verification) with equipment data as first-class; crop management centers the season's operations at crop level |
| Agricultural IoT Platform | centers the sensing backbone (devices, connectivity, telemetry); crop management centers the crop-season operation loop. A pure sensor dashboard without operation records is the IoT pattern |
| Field Management | centers the land unit as a persistent asset (boundaries, soil, infrastructure); crop management centers the crop-season on that land. Field mapping appears in crop management as substrate |
| Harvest Management | centers the harvest operation itself (crews, bins, loads, packing); crop management treats harvest as the cycle's closing phase. Some vendors ship both |
| Irrigation / Crop Protection / Nutrient / Soil Management | each centers one input domain or operation class; crop management integrates all operation classes across the cycle. Each domain typically appears as a module inside crop-management products |
| Orchard / Greenhouse / Vineyard Management | the crop-management pattern scoped to a crop type and its structures; boundary (variant vs sibling) deserves joint review |
| Agricultural GIS | centers the spatial land base and map-layer analytics; crop management uses maps as a surface over the operation record |
| Food Traceability Platform | centers the supply-chain traceability chain after (and beyond) the field; crop management produces the field-side records that feed it |

The boundary with **Agronomy Management** is the closest, because both sit on the same field record and vendors legitimately span both. The structural difference: agronomy management's defining artifact is the recommendation (what to apply, at what rate, and why); crop management's defining artifact is the season's operation record (what was planned, done, observed and harvested). Remove the recommendation loop and crop management stands; remove the operation record and agronomy management stands.

## Representative Products

- Agrivi 360 FMS (Farm Enterprise) — enterprise farm management with crop planning, activities and compliance reporting at the center (Europe/global)
- Croptracker — specialty-crop record-keeping and operations: spray, practice and harvest records, crew labor, food-safety traceability and GAP audits (North America)
- Semios — specialty-crop monitoring and intervention: sensor networks, pest/disease models, spray timing, alerts and field services (North America)
- Cropin Grow (SmartFarm Plus) — enterprise farm digitization: geotagged plots, activity logs, packaged crop programs and advisories across many growers (global South/enterprise)

The Core Model was also checked against a row-crop farm-management product (Bushel Farm, formerly FarmLogs) as a boundary case: it carries field activity records but centers farm business operations, confirming the Farm Management Platform boundary rather than extending this Type's definition.

## Sources

Research date: **2026-09-07**

Primary vendor surfaces (official product / solution pages):

- Agrivi — https://www.agrivi.com/ , https://www.agrivi.com/products/ , https://www.agrivi.com/products/360-farm-enterprise/
- Croptracker — https://www.croptracker.com/ , https://www.croptracker.com/product/farm-management-software.html , https://www.croptracker.com/why-use-crop-management-software.html
- Semios — https://semios.com/ , https://semios.com/solutions/reporting-tools/ , https://semios.com/solutions/insect-pest-management/
- Cropin — https://www.cropin.com/ , https://www.cropin.com/cropin-grow-smartfarm-plus/
- Bushel Farm (boundary check) — https://www.bushelfarm.com/

> Sourcing limitation: no vendor help centers or operational manuals were reachable in this research pass; all evidence is official product/solution-page level. Operational mechanics (record schemas, workflow states, permission models, numeric limits) are therefore stated only at the level the pages support, and precise vendor-specific details are intentionally omitted from this document. Such details remain in the Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison matrix, and the historical / market-sample breadth check are recorded in the paired Research Notes.
