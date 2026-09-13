# Orchard Management

## Overview

An **Orchard Management** application is the orchard operation's system of record, organized around the orchard planting — the long-lived block of fruit or nut trees — as a persistent production asset. It holds the planting's identity, records the perennial cycle of care and protection work against it, and credits each season's harvest back to it as an accumulating performance history that informs the next cycle.

The defining core is small:

```text
Orchard planting (persistent asset)
└── block hierarchy with planting identity (variety; commonly area, planting year)
    └── perennial-cycle work recorded against the asset
        (pruning, thinning, training, grafting, spray, irrigation, nutrition)
    └── the season's harvest credited to the asset
        └── year-over-year performance history per block and variety
```

Everything else commonly associated with modern orchard software — piece-rate payroll, bin ticketing, fruit-sizing cameras, spray-plan libraries, GAP audit packs, sensor networks — is widespread in current products but is not what makes the product an orchard management system. A paper planting register with spray journals, pruning tallies, and per-block yield books satisfies the same core.

When the center of gravity shifts to the season-scoped crop cycle, the product is Crop Management; when it shifts to the harvest operation itself, it is Harvest Management; when it shifts to sensing and models, it is a monitoring Type.

## Users & Context

The primary user is the **orchard manager** — the person accountable for what happens in the orchards each day: which crews are working which blocks, whether pruning or thinning is progressing, what the pick is producing, and what each block and variety is costing and yielding. The **orchard owner/grower** is the principal and data owner, watching performance and cost across the whole planting. **Crew leaders and supervisors** capture work in the field — clocking teams in and out, recording trees pruned or bins picked. **Packers who also grow** (a common structure in tree fruit) run the same records with one eye on fruit quality and packout. In records-oriented products, **agronomists and advisors** read and contribute spray and nutrition records.

The work environment is perennial tree fruit and nuts — apples, cherries, pears, citrus, stone fruit, nuts — where the same planting produces for many years and the year's decisions (how much to thin, how hard to prune) shape the next year's crop. Work is seasonal and crew-heavy: winter pruning, spring protection and thinning, summer irrigation and care, and an intense harvest in which large volumes of bins move from blocks to storage or packhouse within a short window. Much of the work is paid by piece rate — per tree pruned, per bucket or bin picked — which makes per-tree and per-bin crediting a structural need, not a nicety.

## Core Model

### The Defining Core

**The orchard planting as the persistent production asset.** The system's anchor is an identified planting — typically an orchard or ranch subdivided into **blocks**, each carrying its planting identity: the **variety** (with its fruit type), commonly the area, and where kept, the planting year, rootstock, or spacing. Blocks commonly subdivide into **variety sub-blocks**, and, where work granularity requires, into **rows and individual trees**. This hierarchy is not a map layer: it is the persistent asset that outlives every season, the "crop" and the "field" at once. Work, inputs, and outcomes all attach to it.

**Perennial-cycle work recorded against the asset.** The orchard's year is a repeating cycle of care and protection — pruning, training, thinning, grafting or top-working, spraying, irrigating, feeding, mowing, pollinating — and the system records this work as dated, attributed, location-bound entries attached to the block, row, or tree. Tree-shaped jobs are the characteristic case: pruning and thinning are done tree by tree, often by piece rate, so the system tracks which trees in which rows have been completed, by whom, at what rate — with per-tree completion state that persists until deliberately reset for the next pass.

**The season's production outcome credited to the asset.** At harvest, what each block produces is recorded as it comes in — bins, buckets, or loads, commonly with picker or crew identity and quality context — and credited to the block and variety. These outcomes accumulate into the asset's year-over-year performance history: yield, quality, and cost per block and variety, season over season, which is the record the next cycle's decisions are made from.

The three structures are jointly load-bearing. A planting registry alone is a land record; work records without the asset are a free-floating task log; yield without the asset is a bare statistic; asset plus work without recorded outcomes is a journal with no production loop.

### One Structure, Many Implementations

The core is written in conceptual terms. Products realize each concept differently:

```text
Concept:   the persistent planting asset
Realized as:   orchard/ranch → block → variety sub-block → row → tree;
               growing areas with field/row boundaries and replant/rotation edits

Concept:   planting identity
Realized as:   variety + fruit type (universal); area (common);
               planting year, rootstock, spacing (where kept)

Concept:   tree-shaped work
Realized as:   per-tree completion state with reset; row-level task logs;
               volume-only recording when tree identity is not needed

Concept:   the season's outcome
Realized as:   bins/buckets/loads credited per picker; weigh tickets;
               per-block/variety yield and quality totals
```

A reader who has only seen one realization — say, a per-tree piece-rate harvest app — should still be able to recognize a row-level records system or a paper block register as the same Type.

### Standard Capabilities

Mature products commonly add these. They make the system practical; they do not define the Type:

- **Variety catalog** — varieties with fruit type, established before locations so work can be recorded variety-specifically.
- **Job catalog and pay rates** — named job types (pruning, thinning, picking, spraying…) with hourly and piece-rate structures (per tree, per bin, per bucket).
- **Crew and payroll machinery** — timesheets for teams and individuals, leave types, piece-rate calculation with minimum-wage top-ups where law requires, payroll exports.
- **Harvest crediting and traceability** — bins/buckets recorded at or near picking, credited to pickers, ticketed (printed or scanned), and traceable back to the block.
- **Spray plans and records** — planned and recorded applications with chemical inventory withdrawal and worker-safety intervals (re-entry, pre-harvest).
- **Analytics by block and variety** — yield, cost per area, bins per area, cost per bin, picker productivity; harvest maps plotting picked bins by location.
- **Quality control** — defect and pick-quality capture, picker performance comparison; in some products, fruit sizing and color assessment tools.
- **Compliance reporting** — food-safety and audit packs (GAP-class), treatment and destination details carried on harvest records.
- **Mobile field capture with offline capability**, paired with a web dashboard for setup, maps, and reports.

## How It Works

### Set up the asset

```text
Create the variety catalog (variety + fruit type)
→ add orchards/ranches
→ add blocks, assign varieties (variety sub-blocks), areas
→ where needed, add rows and tree numbers
→ define job types and pay rates
→ add staff and issue badges
```

Setup is done once and maintained over years; the block record persists as varieties change, areas are edited, and blocks are eventually replanted.

### Run the perennial cycle

```text
Prune (winter) → crews clocked in to rows; trees marked complete as work proceeds;
                piece rates per tree entered and settled
Protect and feed (spring–summer) → spray plans scheduled and recorded against blocks;
                chemical inventory drawn down; safety intervals observed
Thin → tree-by-tree crop-load work, recorded and credited like pruning
Irrigate and care → operations recorded against blocks
```

Each operation lands as a dated, attributed record on the block/row/tree. The manager's daily view answers: what, where, and by whom is being done today — and how fast, at what cost.

### Harvest and credit

```text
Pick → bins/buckets recorded as picked (who, which block, which variety)
     → bin tickets printed or scanned; GPS position captured
     → credited to pickers for piece-rate pay
     → fruit traced from block toward storage or packhouse
```

### Close the season and look back

```text
Yield by block and variety → quality and size outcomes → costs by job and block
→ year-over-year comparison → decisions for next cycle
→ (eventually) replant or rework a block, updating the planting record
```

### Capability tiers

**Defining core** — without these, not orchard management:

- the persistent planting asset with planting identity
- perennial-cycle work recorded against the asset
- the season's outcome credited to the asset as accumulating history

**Standard capabilities** — present in most mature products:

- variety and job catalogs; pay-rate structures
- crew/timesheet/payroll machinery with piece rates
- harvest crediting, tickets, and traceability
- spray plans and records with inventory and safety intervals
- block/variety analytics and harvest maps
- QC capture; compliance and audit reporting
- mobile + offline capture with a web dashboard

**Optional / variant** — depends on segment, region, and business model:

- fruit sizing/color/maturity tools; pre-harvest yield estimation
- storage-room and packing/shipping traceability (packer-side extension)
- bundled monitoring: weather stations, disease/pest models, frost warning
- season/production planning and budgeting depth
- industry-body data exchange; regional labor- and spray-regime machinery

## Interfaces

Described in conceptual terms; exact layouts and names vary by product.

### Setup / admin surface

The asset registry. Purpose: build and maintain the planting hierarchy and its catalogs. Typical information: orchards, blocks, variety sub-blocks, rows/trees, varieties, job types, pay rates, staff. Primary actions: create and edit hierarchy levels, assign varieties, define jobs and rates.

### Field app

The crew-facing capture surface, used in the orchard. Purpose: record work and harvest as they happen. Typical information: today's jobs, rows with their completion state (in products that track it, color-coded done/partial), clock-in state, per-picker counts. Primary actions: clock teams in/out, select rows, assign workers, enter piece rates and tree counts, record bins/buckets with picker identity, print or scan bin tickets, capture QC observations. Offline operation is standard.

### Dashboard

The manager's web surface. Purpose: see the operation over time and get reports out. Typical information: harvest maps plotting picked bins by location (with bin identity, date, pickers, variety — in products that capture position), yield reports, labor cost by job and location, picker productivity, cost per block and variety. Primary actions: filter, drill down, export payroll and compliance reports.

### Records and reports surface

The compliance face. Purpose: produce the records regulators, auditors, and buyers ask for. Typical information: spray/application histories, treatment and destination details on harvest lots, GAP-class audit forms. Primary actions: compile, fill, export.

## Important Rules / Behaviors

### The asset outlives the season

Records bind to a block and its varieties across years. The unit of management is not "this year's crop" but the planting itself; season history accumulates on the asset. Replanting or reworking a block is an edit to the asset's record, not the creation of a new field.

### Tree-shaped work has state

Where a product tracks work at tree level, a tree that has been pruned or thinned is marked complete and is no longer available for that same job — until deliberately reset for a later pass. Row selection surfaces this state (complete vs partially complete). This per-tree completion machinery is what makes piece-rate tree work auditable; products that stop at row-level logging offer the coarser version of the same discipline.

### Piece-rate crediting ties work to pay

Trees pruned, buckets picked, and bins logged are credited to named workers and flow to payroll. Where law requires, piece-rate pay is reconciled against minimum-wage floors. Rates are configurable per job and commonly per variety or block.

### Traceability runs from block to buyer

Harvest records carry block, variety, picker, and often treatment and destination details, so any lot of fruit can be traced back to where it was picked — the food-safety backbone of tree fruit.

### Spray records carry legal weight

Applications are recorded with product, rate, timing, and location; worker re-entry and pre-harvest intervals gate subsequent work. Record-keeping requirements and formats vary by jurisdiction; the record-keeping duty itself is structural.

### Exact mechanics vary by product

State labels, rate structures, report formats, and integration depths differ across products. The behaviors above are the stable shape; their precise parameters are product decisions.

## Variants

- **Operational pole** — harvest/labor/quality-centric systems built around daily orchard execution: tree-level piece work, bin crediting, picker performance, payroll. Common in high-labor crops (apples, cherries).
- **Records pole** — compliance/traceability-centric systems built around spray records, production-practice logs, GAP audits, and block-to-buyer traceability; often extended from fruit-and-vegetable farm management.
- **Agronomy-planning pole** — general farm-management platforms that treat tree fruit as a crop type within their field/season/activity model; orchard-specific depth (tree-level work, bin crediting) is thin or absent.
- **Grower-packer extension** — the same records extended into storage rooms (including controlled-atmosphere), packing, and shipping traceability; fruit sizing/color grading at the packhouse.
- **Monitoring-bundled vs monitoring-adjacent** — some operations run orchard management beside a separate sensing/model service (weather, disease/pest models, frost warning); bundling varies by vendor and region.
- **Regional regimes** — piece-rate and minimum-wage top-up machinery (US-style), treatment-journal traditions (EU-style), industry-body data exchange (e.g., apple/pear industry APIs in New Zealand) shape the compliance layer without changing the core.
- **Crop-type scope** — pome fruit, stone fruit, cherries, citrus, nuts; some products generalize to berries, vines, and vegetables.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Crop Management | closest sibling | its unit of record is the season-scoped crop (crop × field × season, closed with season history); Orchard Management's unit is the persistent planting that outlives seasons, with asset-shaping work (pruning/thinning/grafting) and a row/tree work substrate the annual cycle lacks |
| Vineyard Management | sibling | expected to bind blocks to winery-bound lots (harvest → crush → wine); orchards bind to fresh-fruit packhouse and traceability — boundary deserves its own research pass |
| Nursery Management | sibling | propagates plants as sale inventory (plant lots, orders); the orchard grows fruit for harvest from planted trees — boundary deserves its own research pass |
| Farm Management Platform | broader | whole-operation scope (land, livestock, finance, equipment); orchard management is production-scoped to the planting asset |
| Harvest Management | interlocking | its center is the harvest operation itself (bin ticketing, crediting, campaign, packhouse handoff), crop-agnostic; Orchard Management's harvest leg is the asset's outcome record, not the operation machinery |
| Farm Labor Management | interlocking | crew/time/piece-rate machinery is shared; the labor Type centers the workforce across the farm, the orchard Type centers the asset |
| Crop Protection Management | interlocking | spray records, safety intervals, chemical inventory are that domain's machinery; orchard management carries them as one recorded operation among many |
| Precision Agriculture / Agricultural IoT / monitoring services | adjacent | sensing- and model-driven decision support; the monitoring pole lacks the asset record entirely, and orchard management consumes monitoring without being defined by it |
| Field Management | substrate | the land-unit register (extent, soil, boundaries) is the ground the planting sits on — leg one alone |
| Produce Packing House Management | downstream | packing operations beyond the grower's own records are that Type |

The boundary with Crop Management is the most important one, because generic crop tools can carry orchard blocks as season-scoped crops. The structural test: if the system's center is the season and its closure, it is crop management applied to orchards; if the center is the planting that persists across seasons — with tree-shaped work and renewal in its model — it is Orchard Management.

## Representative Products

- **Hectre** — orchard management and fruit quality software for growers and packers (apples, cherries, pears, citrus, stone fruit); operational pole with tree-level piece work, bin crediting, and fruit-sizing tools
- **Croptracker** — orchard management software for fruit and nut growers, extended from a fruit-and-vegetable farm-management base; records/compliance pole with spray records, GAP audits, and fruit-quality vision tools

Adjacent specimens examined to draw boundaries (monitoring/decision-support services for orchards and vineyards): Semios, FruitWeb. General farm-management platforms that absorb tree fruit as a crop type: Agrivi, Agworld.

## Sources

Research date: **2026-09-09**

- Hectre — official site and product page: https://hectre.com/ , https://hectre.com/products/farm-management-software/ ; help center: https://hectre.helpscoutdocs.com/ (articles: orchard location setup, varieties, pruning/thinning jobs, harvest maps, manager getting-started; spray category index)
- Croptracker — official site: https://www.croptracker.com/ ; Orchard Management Software product page: https://www.croptracker.com/product/orchard-management-software.html ; Farm Management Software product page: https://www.croptracker.com/product/farm-management-software.html
- Semios — official site: https://semios.com/
- FruitWeb — official site (EN): https://fruitweb.info/en/
- Agrivi — official site: https://www.agrivi.com/ , https://www.agrivi.com/products/360-farm-enterprise/
- Agworld — official site: https://www.agworld.com/

> Sourcing limitation: several orchard-sector vendors could not be reached from the research environment (FarmSoft and AgCode returned errors on repeated attempts; a third was unreachable once). Their structures are not asserted anywhere in this document. Hectre's spray-plan mechanics were verified at help-category level only. Rootstock and planting-year fields, though standard orchard practice, were not explicitly enumerated on any fetched page and are described as "where kept". Operational details beyond what these pages support (exact rate structures, numeric limits, integration catalogs) are intentionally not stated.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical market-sample check are recorded in the paired Research Notes.
