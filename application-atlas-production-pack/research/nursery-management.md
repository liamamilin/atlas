# Research Notes — Nursery Management

## Research Goal

Understand what a Nursery Management application really is, from real products: what the core objects are, how plant production connects to sales, and where the boundary lies against Greenhouse Management, Orchard Management, Farm Management, and generic inventory/ERP.

## Initial Boundary

Prior hypothesis from the sibling passes (greenhouse-management, orchard-management, both dated 2026-09-08/09, both deferring this boundary to "its own research pass"):

- Greenhouse Management's framing: "nursery management holds the plant-production business (plant lots from propagation to finished stock across all production areas, with sales context); greenhouse management operates the controlled enclosures within it."
- Orchard Management's framing: "propagates plants as sale inventory (plant lots, orders); the orchard grows fruit for harvest from planted trees."

Working hypothesis: the unit of record is the plant batch/lot as living, saleable inventory — not a season-scoped crop (Crop Management), not a long-lived harvest asset (Orchard), not a controlled enclosure (Greenhouse).

Note on naming: "nursery" also means childcare; Atlas Core Cloud explicitly disambiguates ("For a plant nursery — not a childcare setting"). This leaf is the plant-production business.

## Research Questions

1. What is the central object — batch, lot, SKU, crop, location?
2. What lifecycle does a plant batch go through, and what state changes are recorded (propagation, potting-on, grading, losses, movements)?
3. How does production connect to sales — availability, reservation, orders, dig lists?
4. What role do production locations/space play?
5. Which capabilities are common-mature vs variant (dig lists, plant passports, POS, EDI, propagation planning)?
6. Where are the boundaries against the neighboring Types?

## Representative Products

Sample chosen for market representativeness, documentation quality, different product philosophies, different geographies and customer tiers:

| Product | Vendor / origin | Segment | Philosophy |
|---|---|---|---|
| Agriware 365 | Mprise Agriware (NL) | enterprise nursery ERP | ERP-suite pole: horticulture layer on Microsoft Dynamics 365 Business Central |
| PAT Horticulture (Young Plants) | pat. Horticulture Software (AT/EU) | young-plant / propagation specialists | propagation-specialist ERP pole; mother stock, rooting, availability planning |
| Genesys | NVK (US) | wholesale growers & garden centers | wholesale order-to-invoice pole; dig-list field harvesting |
| Plantatory | (US) | small nurseries & garden centers | lightweight inventory pole: in-production tracking without ERP weight |

Boundary probes (official pages, lighter evidence): Gros.farm (production-context pole that explicitly does not replace inventory/sales), Textcubed (state-machine lifecycle articulation), Atlas Core Cloud (UK; "living batch" articulation, plant passports, one stock pool), ET Grow (staging/rack builds), CONIC-SOFT (Spanish forestry/ornamental nurseries).

## Sources

Fetched directly (2026-09-10):

- Agriware 365 — Plant Nursery Software page: https://www.mprise-agriware.com/plant-nursery-software (full fetch)
- Genesys — home/product page: https://www.nvkgenesys.com/ (full fetch)
- PAT Horticulture — Young Plants page: https://pat-horticulture.com/young-plants/ (full fetch)
- Plantatory — home page: https://www.plantatory.com/ (fetch returned title only; content taken from search-engine capture of the same official page)

From search captures of official pages (evidence layer A but less complete): Gros.farm (https://gros.farm/en-us/plant-nursery-management-software), Textcubed (https://www.textcubed.com/), Atlas Core Cloud (https://atlascore.cloud/), ET Grow (https://www.etgrow.com/nextgen-platform-nursery), CONIC-SOFT (https://www.smartsowing.com/en/products/conic-software/), Plantiful (https://plantiful.ai/), Growflo (https://growflo.com/), Tend (https://www.tend.com/solutions/nursery-management-software), Folio3 AgTech (https://agtech.folio3.com/crop-management-software/nursery-management/), Sembrent (https://3rdrockdata.com/sembrent-nursery-management/).

Not reachable / not pursued: legacy US desktop-era products (NMS nurserymanagementsoftware.com, Seracon, PICS) did not surface in search; no claims about them are made. Help-center/knowledge-base depth (Agriware KB, Genesys API docs) not fetched — assertions calibrated accordingly.

## Product Observations

### Agriware 365 (Mprise) — evidence layer A

- Positioning: "Connect nursery operations, office and finance in one ERP"; extends Business Central with nursery-specific processes: "Crop and batch management, Available-to-sell (ATS) inventory, Production and space planning, Mobile operations, Integrated sales and shipping."
- Batch as inventory: "manage plant batches, locations, sizes, varieties, qualities and availability in one system"; real-time current AND future stock ("what will be ready next week, next month or later in the season").
- Sales/planning/production "work with the same data, so everyone knows what can be sold, reserved, moved or produced."
- Locations: "inventory and stock movements across greenhouses, fields, cold storage, warehouses and production stages."
- Modules: financial management, planning & forecast, production (crop management), inventory, sales & order management (orders, contracts, EDI), loading & shipping (picking, racking).
- Mobile apps: inventory control, stock movements, labor registration, inspections, picking, packing.
- Customers: young-plant growers, potted-plant growers, seed production, plant genetics — horticulture-wide, nursery is one solution page.

### PAT Horticulture — Young Plants — evidence layer A

- Positioning: ERP for young-plant growers (seedlings, cuttings, plugs); "Track mother stock and cuttings, plan rooting windows, manage (un)rooted batches, and align orders with production capacity."
- Availability planning: "precise availability plans down to the delivery week or production week and batch level. Define expected output by variety, rooting status, and production phase."
- Batch tracking: "From cutting to delivery, every unit is traceable. See real-time status, rooting stage, and losses across locations."
- Loss/lead-time modeling: "crop-specific lead times, expected and realized loss rates, and growth durations for every variety"; actual batch performance feeds back into planning.
- Documents: labels, picking lists, phytosanitary certificates generated from order data, linked to live batch and order details.
- Modules: planning & forecast, sales, production, inventory, mobile operations, integrations. Customers: Dümmen Orange, Florensis, Volmary (international young-plant producers).

### Genesys (NVK) — evidence layer A

- Positioning: all-in-one for nurseries, garden centers, wholesale growers; "from plant catalog to invoice."
- Sales order lifecycle: Quote → Open → Reserve → Picking → Ready → Shipping → Invoice, with real-time inventory checks while building orders.
- Inventory: "Track every plant and product by location, status, and availability."
- Dig Management: "Coordinate field harvesting from sales requests to dig crew execution — the feature only nurseries need." Dig requests flow from sales orders to the field; completed digs update inventory and order status.
- Plant & product catalog; purchasing/POs; CRM; accounting & invoicing export; audit trail; 8 roles / 400+ permissions.
- Anti-generic framing: "They were all built for manufacturing or retail and just didn't understand nursery workflows."

### Plantatory — evidence layer A (search-captured official page)

- Positioning: "Inventory Management for Plant Nurseries... Track plants, manage in-production entries, and optimize stock across multiple locations."
- In-production tracking: "Track every plant from propagation to sale. Monitor in-production health, growth stages, and movements."
- Multi-location: "greenhouses, retail stores, and warehouses."
- Care activities, plant health status, care histories; low-stock and care-reminder notifications.
- Segments: retail nurseries (retail floor, backyard, storage) and wholesale growers (propagation through growth stages to wholesale distribution).
- No ERP/accounting claims — deliberately inventory-scoped.

### Boundary probes — evidence layer A (official pages, lighter depth)

- **Gros.farm** — nursery batch passports ("origin, site, age, stage, container size, losses, grade, expected yield"), sites hierarchy (fields, greenhouses, beds, container yards, blocks, rows), protocols (stages, rates, dates per crop/propagation method), tasks, batch balance (initial vs actual count, survival, grades, sale-ready material). FAQ: "Does Gros.farm replace inventory, sales, or local automation? No. Gros.farm manages growing context." — a production-context-only pole; still tracks "when the batch is ready for sale."
- **Textcubed** — "State machine tracks every plant from propagation through growing, ready, sold, and shipped. The system enforces valid transitions." Batch operations ("Move 200 flats from propagation to shade house 3 in one operation"); locations: greenhouse, shade house, field block, bench row; wholesale marketplace publishing availability from live inventory.
- **Atlas Core Cloud** — "Not a fixed product code, but a living batch that changes pot size, grade and location while it grows." Batches through potting on, grading, losses; plant passports generated from entered data; one stock pool feeding till (EPOS), trade order, webshop; B2B portal.
- **ET Grow** — "From propagation to staging, see what's ready—right from the field"; live availability, plant stages, location shifts; nursery ERP: orders, pick lists, rack builds, shipping.
- **CONIC-SOFT** — horticultural, ornamental, and forestry nurseries; customer orders, supplier purchases, greenhouse space management ("positioning and tracking of plant batches"), sowing schedules, traceability from sowing to final delivery.
- **Plantiful** — "Track every crop from propagation to sale"; availability lists; orders; POS; QuickBooks sync; "crop codes, container sizes, availability lists, picking tickets, pot-ups."
- **Growflo** — production, inventory, sales, fulfilment; picking/packing/dispatch.
- **Tend** — production planning, task management, inventory, record keeping, sales for plant nurseries (farm-management lineage).
- **Folio3** — lot/tray-level data, growth stage, readiness date, shrinkage; parent-child batch linking; barcode/RFID; pre-committed/available/pending plant states.
- **Sembrent** — wholesale nursery planning/scheduling/inventory calculation engine (FileMaker platform).

## Cross-product Comparison

| Structure | Agriware | PAT | Genesys | Plantatory | Gros.farm | Textcubed | Atlas Core |
|---|---|---|---|---|---|---|---|
| plant batch/lot as unit of record | ✓ batches | ✓ (un)rooted batches | ✓ plants by location/status | ✓ in-production entries | ✓ batch passports | ✓ flats/batches | ✓ living batch |
| growth-stage lifecycle on the batch | ✓ production stages | ✓ rooting stage, losses | ✓ status | ✓ growth stages | ✓ stages, potting, grading | ✓ state machine propagation→growing→ready→sold→shipped | ✓ potting on, grading |
| sale-readiness / availability | ✓ ATS, current+future | ✓ weekly availability plans | ✓ availability, reserve | ✓ ready to sell | ✓ sale-ready material | ✓ ready stage → availability list | ✓ one stock pool → till/trade/webshop |
| orders/reservation against availability | ✓ orders, contracts, EDI | ✓ align orders with capacity | ✓ quote→invoice lifecycle | – (retail orders light) | – explicit no | ✓ wholesale marketplace | ✓ trade orders, B2B |
| locations/space | ✓ greenhouses, fields, warehouses | ✓ across locations | ✓ by location | ✓ multi-location | ✓ sites→rows | ✓ greenhouse/shade house/field block/bench | ✓ bays/beds |
| propagation depth (mother stock, rooting) | ✓ (young-plant solution) | ✓ core | – | ✓ propagation tracking | ✓ mother stock, protocols | ✓ propagation state | ✓ propagation bench |
| losses/shrinkage/grading | ✓ qualities | ✓ loss rates | – | ✓ health status | ✓ survival, grades | ✓ | ✓ grading, losses |
| dig/field-harvest lists | – | – | ✓ dig lists | – | – | – | – |
| plant passports / phytosanitary docs | – | ✓ phytosanitary certificates | – | – | – | – | ✓ plant passports |
| POS / webshop / B2B portal | ✓ ecommerce integration | – | – | – | – | ✓ marketplace | ✓ EPOS, webshop, B2B |
| accounting/finance | ✓ full ERP | ✓ ERP | ✓ export | – | – | – | ✓ ledger |

## Abstraction Hierarchy

### L0 — Defining Invariant

The smallest structure without which the product stops being a nursery management system:

1. **The plant batch as living inventory** — an identified quantity of one variety (commonly carrying container size / grade / age) held as the unit of stock record. Not a static SKU: the batch is the stock line, and it is alive.
2. **The growth lifecycle recorded on the batch** — the batch moves through production stages (propagation → growing on → sale-ready) with recorded state changes: movements between locations, potting-on/up-potting (changing container size), grading, and losses (shrinkage) reducing count. The batch's count, size, grade, and location are current state, maintained over time.
3. **Sale-readiness as a first-class dimension** — the system expresses what is ready to sell now and what will be ready later (availability), binding the production record to the sales side.

Jointly load-bearing: batch alone = a static stock list; lifecycle without the batch = a task/growth log with no stock identity; readiness without the batch = an availability spreadsheet with nothing behind it. Remove the sale-readiness leg and the product is crop/production record-keeping (Gros.farm's self-declared scope boundary); remove the lifecycle and it is generic inventory.

Historical check: a paper nursery stock book — one line per lot with variety, container size, quantity, location, and ready date, updated as lots are potted on, graded, culled, and sold — satisfies all three structures. Desktop-era and regional products (forestry nurseries per CONIC-SOFT) fit. The core is not the ERP, the cloud, the mobile app, or the marketplace.

### L1 — Common Mature Structure

- **Availability management depth** — available-to-sell computation (on-hand minus reserved/committed), future availability by week (PAT, Agriware), availability lists published to buyers (Textcubed, Plantiful, ET Grow).
- **Sales orders / reservation against availability** — quote→order→pick→ship→invoice lifecycle with real-time inventory checks (Genesys, Agriware, Atlas Core).
- **Production locations and space** — greenhouses, container yards, fields, benches, blocks, warehouses as managed places; space planning as a constraint (Agriware, CONIC-SOFT, Gros.farm).
- **Propagation planning** — mother stock, cutting/seed lots, rooting windows, crop-specific lead times and expected loss rates feeding availability forecasts (PAT; Agriware young-plants).
- **Work/task recording against batches** — care activities, treatments, inspections (Plantatory, Gros.farm, PAT mobile).
- **Traceability and regulatory documents** — batch passport, plant passports, phytosanitary certificates, labels (PAT, Atlas Core, Gros.farm).
- **Purchasing** — hard goods and finished-stock buying, POs, receiving (Genesys, Agriware, Plantiful).
- **Mobile field operations** — stock moves, counts, inspections from the work floor (Agriware, PAT, Atlas Core, Folio3).

### L2 — Variant / Optional

- **Dig lists / field harvesting** — B&B (balled-and-burlapped) field-tree nurseries dig to order; Genesys calls dig management "the feature only nurseries need" but it is segment-specific (field-grown trees), not definitional — absent from Agriware's, PAT's, Plantatory's core pages.
- **Plant passports / phytosanitary regime depth** — EU/regional regulatory shape (Atlas Core, PAT).
- **Retail face** — garden-center EPOS, webshop, B2B portal (Atlas Core, Genesys, Plantiful POS).
- **EDI / API order intake** — retail/garden-center supply chains (Agriware, Genesys).
- **Accounting depth** — full GL inside the product (Agriware, Atlas Core) vs export/sync (Genesys, Plantiful→QuickBooks) vs none (Plantatory, Gros.farm).
- **Segment scope** — young-plant/plug specialists (PAT), wholesale growers (Genesys, Growflo), retail/garden centers (Plantatory, Atlas Core), forestry nurseries (CONIC-SOFT), cannabis nurseries (adjacent market), contract growing (Textcubed).
- **AI assistance** — order reading, photo identification, batch comparison (Plantiful, Textcubed, Gros.farm).

### L3 — Vendor-specific (Research Notes only)

- Genesys's specific role catalog (8 roles, 400+ permissions), JWT/session specifics, Vercel/Postgres stack — vendor detail.
- Agriware's Business Central foundation and "100+ more" module count.
- PAT's named customer deployments (Dümmen Orange, Florensis, Volmary) and 150-business claim.
- Textcubed's AI import from photos/PDFs; private-preview status.
- Atlas Core's three concrete selection tests (pot-on link preservation, passport from entered data, one stock pool) — good articulation, vendor framing.

## Vendor-specific Findings

- Dig management as a headline feature is Genesys-specific positioning (though the B&B dig-to-order workflow is a real industry practice).
- "Available-to-sell (ATS)" as named vocabulary is Agriware's; the concept (availability net of reservations) is common.
- Gros.farm's explicit "we do not replace inventory/sales" scoping is a positioning choice; it demonstrates the production-context pole but does not define the Type's minimum.

## Boundary Findings

| Neighbor | Test | Disposition |
|---|---|---|
| Greenhouse Management | enclosure control loop vs plant-production business record | keep-both, ratified from this side: a greenhouse control system runs zones/equipment without keeping plant-lot stock books; a nursery system holds batches and sales without operating vents/boilers. Ornamental nurseries commonly run both. |
| Orchard Management | plants as sale inventory vs planting as permanent harvest asset | keep-both, ratified from this side: the nursery's batch exists to be sold as a plant; the orchard's block exists to produce fruit across years. Orchard software centers pruning/thinning/harvest crediting on the asset; nursery software centers batch stock and availability. |
| Farm Management Platform | whole-operation scope vs plant-production inventory business | keep-both: farm management's center is the field/season/activity across the farm operation; nursery management's center is the saleable batch. Tend (farm-management lineage) shipping a nursery solution shows the adjacency. |
| Crop Management | season-scoped crop cycle vs living saleable batch | keep-both: crop management closes the record with the season; the nursery batch closes with the sale/shipment. |
| Generic Inventory / ERP | static SKU stock vs living growing stock | the nursery-specific substance is the batch lifecycle; generic ERP "stops at finance, purchasing and basic stock control" (Agriware's own framing). Nursery management is the horticulture-specific Type, not an ERP variant. |
| E-commerce / Retail POS | garden-center retail face is a variant extension | the retail face (EPOS, webshop) sits on the nursery stock pool; it is packaging, not identity. |
| Forestry seedling systems | same batch structure, different crop domain | in-type variant (CONIC-SOFT covers forestry nurseries with the same order/space/batch machinery). |

"去掉什么就变成另一个 Type" judgments: remove the living-batch stock model → generic inventory/ERP; remove the sale-readiness bridge → crop/production record-keeping (Gros.farm pole); remove the plant-production subject entirely → generic wholesale distribution.

## Uncertainties

- Legacy desktop-era US products (NMS, Seracon, PICS) could not be examined; the historical check rests on the paper-record thought experiment and the era-independent articulation of the batch concept, not on those products' documentation.
- Help-center depth not fetched for any product; precise operational parameters (state names, reservation semantics, numeric limits) intentionally not asserted.
- Whether "space planning" should sit in L0 was considered and rejected: batches carry location (L0), but space *planning* as forward-looking allocation is L1 — Plantatory and Genesys satisfy the core without it.
- The exact boundary of the "young plants" segment (propagation specialists selling rooted/unrooted cuttings to other growers) is a segment of this Type per PAT's own positioning ("Want to see the right setup for your nursery?"), not a separate Type — but a full taxonomy pass could revisit.

## Final Synthesis

Nursery Management is the plant-production business's system of record: its unit of record is the plant batch — living inventory that changes size, grade, count, and location as it grows — tracked through a propagation-to-sale-ready lifecycle, with sale-readiness (what is sellable now and later) as the bridge to orders and fulfillment. Orders, availability lists, space planning, propagation planning, traceability documents, retail faces, and dig lists are the mature market's standard or variant capabilities, not the definition. The Type is distinct from Greenhouse Management (control loop vs business record), Orchard Management (sale inventory vs harvest asset), and generic ERP/inventory (living stock vs static SKU).
