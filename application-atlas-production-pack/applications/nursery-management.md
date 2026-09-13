# Nursery Management

## Overview

A **Nursery Management** application is the plant-production business's system of record. Its center is the **plant batch** — a living line of stock that changes size, grade, count, and location as the plants grow — tracked from propagation through growing stages to sale-ready, with the system continuously expressing what is available to sell now and what will be ready later.

The defining core is small:

```text
Plant batch (living inventory, not a static SKU)
└── growth lifecycle recorded on the batch
    (propagation → growing on → sale-ready;
     movements, potting-on, grading, losses)
    └── sale-readiness / availability
        (what can be sold now, what will be ready later)
```

Everything else commonly associated with nursery software — sales orders, availability lists, space planning, propagation planning, plant passports, dig lists, POS, EDI, accounting — is widespread in current products but is not what makes the product a nursery management system. A paper stock book with one line per lot — variety, container size, quantity, location, ready date — updated as lots are potted on, graded, culled, and sold, satisfies the same core.

When the center of gravity shifts to operating the controlled enclosure itself, the product is Greenhouse Management; when it shifts to a long-lived planting grown for its fruit, it is Orchard Management; when it is static non-growing stock, it is generic inventory or ERP.

## Users & Context

Primary users:

- **grower / production manager** — owns the batch record: what is in propagation, what is growing where, what is ready, what was lost. Plans production against expected demand and space.
- **sales / order staff** — sell from live availability: check what is ready or will be ready, take orders, reserve stock, hand fulfillment to the yard or shipping team.

Secondary users:

- **yard / field crew** — move batches between locations, pot on, grade, count, and pick orders; in field-grown tree nurseries, execute dig lists.
- **owner / manager** — watches stock value, sales, and shortages across locations.
- **retail staff** — at garden centers, sell over the counter from the same stock pool.

The work context is commercial plant production: wholesale growers producing annuals, perennials, trees, shrubs, and young plants for other growers, landscapers, retailers, and garden centers; propagation specialists selling rooted and unrooted cuttings; retail nurseries and garden centers; forestry seedling nurseries. The characteristic difficulty the software exists for: the product is alive — it grows, changes container size, occupies space, dies — and it must be sold at the right moment, so stock, space, time, and sales all move together.

## Core Model

### The plant batch: the unit of record

The system's anchor is the **batch** (lot): an identified quantity of one variety, commonly carrying its container size or grade, its age or production start, and its current location. The batch — not a fixed product code — is the stock line. One variety can exist as many simultaneous batches in different containers, stages, and locations, and each is tracked separately because each is separately sellable.

The batch is *living*: its count, size, grade, and location are current state, not fixed attributes. Potting a batch on into larger containers changes its size class while preserving its identity; grading sorts it into quality categories; losses and culls reduce its count; movements relocate it. One vendor in the researched market states the contrast directly: the center is "not a fixed product code, but a living batch that changes pot size, grade and location while it grows."

### The growth lifecycle

The batch moves through production stages from its origin — seed, cutting, graft, division, or liner — through growing on, toward sale-ready. Products model this as stages or states (propagation, growing, ready), and record the events that change the batch along the way:

- **propagation and origin** — where the batch came from (mother stock, seed lot, cutting source) and when it started
- **movements** — relocations across greenhouses, container yards, fields, benches, and overwintering areas
- **potting-on / transplanting** — container-size changes that keep the batch's identity
- **grading and quality** — sorting into grades or quality categories
- **losses** — shrinkage and culls, which reduce the count and are recorded rather than silently absorbed

The lifecycle is what turns a stock list into a production record: from a batch's history one can see where losses appeared, how long the crop took, and what the batch went through to become sellable.

### Sale-readiness: the bridge to the sales side

The third leg binds production to commerce: the system expresses **availability** — what is ready to sell now, what is reserved or committed, and what will be ready in coming weeks. Mature products compute this from the batch record (on-hand minus reserved, plus future batches approaching readiness) and present it to sales staff, publish it as availability lists, and check it live while orders are taken. This is the nursery's defining economic question — a batch is only revenue when someone buys the living plant — and it is why production and sales work from the same data.

### What sits beside the core

Mature products commonly add, as standard capabilities: sales-order lifecycles with reservation against availability; purchasing of hard goods and finished stock; space planning across growing areas; propagation planning (mother stock management, rooting windows, crop-specific lead times and expected loss rates feeding availability forecasts); work and care recording against batches; traceability documents (batch passports, plant passports, phytosanitary certificates, labels); mobile operations for the work floor; and accounting integration. Segment-specific extensions include dig-list field harvesting for field-grown trees, retail EPOS and webshops for garden centers, and EDI connections to retail chains.

## How It Works

### Set up the catalog and locations

```text
define varieties and products (with sizes/containers)
→ define locations (greenhouses, yards, fields, benches, warehouses)
→ enter or import initial stock as batches
```

### Start and grow a batch

```text
propagate or receive a new batch (variety, quantity, origin, start date)
→ batch occupies a location
→ record work and care against it
→ move it as it grows (pot on, shift houses/yards)
→ grade; record losses and culls
→ batch reaches sale-ready
```

Each event lands on the batch, keeping its count, size, grade, and location current. The batch's history is its production record.

### Sell from availability

```text
sales checks availability (ready now / ready later)
→ order taken; stock reserved or allocated
→ pick / pull / dig the ordered plants
→ ship; batch count reduced; order invoiced
```

In field-grown tree nurseries, the pull step is a coordinated field operation: dig requests flow from sales orders to crews as prioritized dig lists, and completed digs update both inventory and order status.

### Look back and plan forward

Completed batches feed planning: realized loss rates, growth durations, and output inform the next cycle's availability forecasts and space plans. Sales history informs what to propagate and how much.

### Capability tiers

**Defining core** — without these, not a nursery management system:

- the plant batch as the unit of stock record
- the growth lifecycle recorded on the batch (stages, movements, potting-on, grading, losses)
- sale-readiness / availability as a first-class, sales-facing dimension

**Standard capabilities** — present across the mature market:

- availability computation with reservation (available-to-sell; future availability by week)
- sales orders from quote to invoice against live availability
- production locations and space management
- propagation planning (mother stock, lead times, expected loss rates)
- work/care recording against batches
- traceability and document generation (labels, passports, phytosanitary certificates)
- purchasing and receiving
- mobile operations for stock moves, counts, and inspections

**Optional / variant** — depends on segment, region, and business model:

- dig lists / field harvesting (field-grown tree nurseries)
- plant passports and regional phytosanitary regimes
- retail face: EPOS, webshop, B2B portal
- EDI / API order intake for retail supply chains
- full accounting inside the product vs export/sync vs none
- AI assistance (order reading, photo identification, batch comparison)

## Interfaces

Described in conceptual terms; exact layouts and names vary by product.

### Batch / inventory overview

- Purpose: see the living stock — what batches exist, where they stand, what is ready.
- Typical information: batches with variety, size/grade, quantity, location, stage or readiness; shortage alerts.
- Primary actions: open a batch, filter by variety/location/readiness, adjust counts.

### Batch detail

- Purpose: follow one batch's life.
- Typical information: origin and start date, current location and count, stage, recorded events (movements, potting-on, grading, losses), care history.
- Primary actions: record an event, move the batch, pot on, grade, write off losses.

### Availability surface

- Purpose: answer "what can I sell?" — the sales-facing view of production.
- Typical information: available quantities by variety/size; reserved and committed amounts; future availability by week where supported.
- Primary actions: publish or export availability lists, check availability while ordering.

### Order management

- Purpose: take and fulfill orders against real stock.
- Typical information: order lifecycle status (quote → open → reserved → picking → ready → shipping → invoiced), live availability checks, customer and delivery details.
- Primary actions: create orders, reserve stock, generate pick lists and documents, invoice.

### Location / space view

- Purpose: see what occupies the growing areas.
- Typical information: batches by location; occupancy of houses, yards, fields, benches.
- Primary actions: move batches, plan space.

### Mobile work-floor app

- Purpose: record stock reality where it happens.
- Typical information: batch locations, move and count tasks.
- Primary actions: scan or select batches, record movements and counts, log care.

## Important Rules / Behaviors

- **The batch is the stock identity.** Potting on, grading, and moving a batch change its attributes without breaking its identity; the batch's history stays in one record. Splitting or merging stock creates linked batch records rather than losing lineage.
- **Losses are recorded, not absorbed.** Shrinkage and culls are explicit events on the batch; the count on the record is meant to match what is standing in the bed or pot.
- **Availability is production-derived.** What sales can promise is computed from batch state (on hand, reserved, future batches with expected ready dates); overselling is guarded by checking availability live during order entry.
- **Reservation ties orders to stock.** An order reserves or allocates specific availability; fulfillment (picking, digging, shipping) reduces the batch count and advances the order's lifecycle.
- **Space is a real constraint.** Batches occupy locations; growing areas are finite, and moving a batch is a recorded operation, not an invisible edit.
- **The plant is sold alive.** Unlike harvested-crop records, the batch's end state is a sale and shipment of the living plant itself; quality and readiness at sale time are part of the record.
- **Exact mechanics vary by product.** Stage names, reservation semantics, document formats, and integration depths differ; the behaviors above are the stable shape.

## Variants

- **Wholesale grower ERP** — the full business in one system: production, inventory, sales, purchasing, shipping, accounting (the enterprise pole).
- **Young-plant / propagation specialist** — depth in mother stock, rooting windows, rooted/unrooted batches, and weekly availability planning; customers are other growers.
- **Field-grown / B&B tree nursery** — dig-list field harvesting: orders become prioritized dig lists for field crews; completed digs update stock and orders.
- **Retail nursery / garden center** — the same stock pool behind a counter (EPOS), webshop, and B2B portal; seasonal rotations and walk-in sales.
- **Lightweight inventory-first** — in-production tracking and multi-location stock without ERP weight, for smaller operations.
- **Production-context pole** — batch passports, protocols, and work recording focused on growing context, with inventory/sales left to connected systems.
- **Forestry seedling nursery** — the same batch/order/space machinery applied to forest stock, often at very high seedling volumes.
- **Regional regulatory shapes** — plant passports and phytosanitary documentation regimes vary by jurisdiction without changing the core.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Greenhouse Management | sibling in the same industry | greenhouse management operates the controlled enclosure — zones, sensors, climate equipment, alarms; nursery management holds the plant-production business record — batches, availability, orders. A nursery can run on records without climate-control software; a greenhouse control system runs the house without keeping the plant-lot books. Ornamental growers commonly use both. |
| Orchard Management | sibling | the orchard's unit is the long-lived planting grown for harvest (pruning, thinning, yield credited to blocks across years); the nursery's unit is the batch grown to be sold as a plant. Different objects, cycles, and outcomes. |
| Farm Management Platform | adjacent | whole-operation scope (land, seasons, activities, finance) centered on field cropping; nursery management is production-scoped to saleable living stock. |
| Crop Management | adjacent | crop management's record closes with the season's crop cycle; the nursery batch closes with the sale/shipment of the plants themselves. |
| Inventory Management / ERP | substrate | generic stock systems hold static SKUs; the nursery-specific substance is the living batch whose size, grade, count, and location change as it grows. Generic ERP "stops at finance, purchasing and basic stock control" — nursery management is the horticulture-specific Type built on top of that substrate. |
| E-commerce / Retail POS | downstream variant | the garden-center retail face sits on the nursery stock pool; it is packaging, not identity. |
| Wholesale Distribution | adjacent | distributes finished goods; nursery management's stock is produced in-house and sold alive, with growth state as part of the record. |

The boundary with Greenhouse Management is the most important one, because both leaves live in protected plant production and the same growers use both. The structural test is the center of gravity: the enclosure's operating loop (climate control) versus the plant-production business record (batches and sales).

## Representative Products

- **Agriware 365 (Mprise Agriware)** — Netherlands; nursery ERP built on Microsoft Dynamics 365 Business Central; batch management, available-to-sell inventory, production and space planning, sales and shipping
- **PAT Horticulture** — Austria/Europe; ERP for young-plant growers; mother stock, rooted/unrooted batches, weekly availability planning, loss-rate modeling, phytosanitary documentation
- **Genesys (NVK)** — United States; all-in-one platform for nurseries and wholesale growers; plant catalog, order lifecycle, dig-list field harvesting
- **Plantatory** — United States; lightweight inventory management for plant nurseries; in-production tracking from propagation to sale across locations

Boundary probes examined: Gros.farm (production-context pole), Textcubed (state-machine lifecycle), Atlas Core Cloud (living-batch articulation, retail face), ET Grow (staging and availability), CONIC-SOFT (forestry nurseries).

## Sources

Research date: **2026-09-10**

- Mprise Agriware — Plant Nursery Software: https://www.mprise-agriware.com/plant-nursery-software
- pat. Horticulture Software — Young Plants: https://pat-horticulture.com/young-plants/
- Genesys (NVK) — product site: https://www.nvkgenesys.com/
- Plantatory — official site: https://www.plantatory.com/
- Gros.farm — plant nursery management software: https://gros.farm/en-us/plant-nursery-management-software
- Textcubed — nursery & greenhouse management software: https://www.textcubed.com/
- Atlas Core Cloud — nursery management software: https://atlascore.cloud/
- ET Grow — nursery platform: https://www.etgrow.com/nextgen-platform-nursery
- CONIC-SOFT — nursery software: https://www.smartsowing.com/en/products/conic-software/

> Sourcing limitation: vendor help centers and knowledge bases were not fetched; findings rest on official product pages and FAQs. One product's page (Plantatory) was captured via search rather than a direct fetch. Precise operational parameters (stage names, reservation semantics, numeric limits, integration catalogs) are intentionally not stated; assertions are calibrated to the reachable evidence, and such details remain in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical market-sample check are recorded in the paired Research Notes.
