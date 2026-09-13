# Winery Management

## Overview

A **Winery Management** application is the winery's wine-production system of record. It holds every lot of wine the winery makes as an identified record carrying its identity — variety, vintage, and where the grapes came from — keeps that wine's physical location in the cellar's tanks, barrels, and bins, and records every operation performed on it: crush, press, rack, transfer, blend, addition, topping, and bottling. From that operation record the system maintains each lot's quantity, composition, and cost, and produces the production and compliance reporting the alcohol regime requires.

The defining core is small:

```text
Wine lot (identified quantity carrying varietal / vintage / origin identity)
└── held in the vessel estate (tanks, barrels, bins — capacity, location, contents)
    └── changed by recorded cellar operations
        (quantity conserved — losses booked, not dropped;
         composition and cost carried proportionally)
        └── accumulating into the lot's authoritative history
```

Everything else commonly associated with modern winery software — lab-device integrations, mobile capture at the tank, 3D tank maps, vineyard modules, direct-to-consumer sales tooling, custom-crush client billing — is widespread in current products but is not what makes the product a winery management system. A paper-era winery running on a cellar book of tank and lot records, weigh tags at the scale, blend ledgers, and filed production reports satisfies the same structure.

When the center of the system shifts to the vineyard planting rather than the wine lot, the product is describing a different Application Type (Vineyard Management). When the record flavor shifts to recipe-executed beer batches, it is the sibling Type in the same fermented-beverage family (Brewery Management).

## Users & Context

The primary users are the winemaking and cellar team:

- **winemaker / assistant winemaker** — decides and directs: plans work, monitors ripening and fermentation, designs and commits blends, checks composition against label rules
- **cellar master / cellar hands** — executes: performs rackings, transfers, additions, topping, and barrel work, recording each operation where it happens, at the vessel
- **lab technician** — measures: enters and imports analyses (sugar, acidity, pH, sulfur dioxide), runs fermentation checks

Around them:

- **production / operations manager** — schedules crush-pad and cellar capacity, forecasts vessel space, manages dry goods and supplies
- **compliance owner** — produces the regime's production and excise reports, declarations, and audit records
- **finance** — tracks cost per lot and per bottled product, reconciles with accounting
- **owner / general manager** — reads profitability per wine and the state of the season

At custom crush facilities — wineries that make wine for client brands — client winemakers are also users, and the system attributes work and storage to the client for billing.

The work context is strongly seasonal. The crush season is the structural peak: fruit arrives at the crush pad over compressed weeks, fermenters fill, and every vessel matters. The rest of the year is slower cellar work — racking, topping, sampling, blending trials — closing with bottling campaigns and the compliance cycle.

## Core Model

### The defining core

**The wine lot.** The central record is the lot (products also say *batch* or *wine*): an identified quantity of wine — from the moment fruit is received, through must and juice, to finished wine — that carries its composition identity: the variety or varietal, the vintage, and the origin (vineyard or block source, and the appellation set where the regime defines one). The lot is persistent: it is created at intake and lives in the system for months to years, accumulating everything done to it. Its identity is not typed in repeatedly; it is established once at the origin record (the weigh tag or intake) and then *computed forward* — every later blend's varietal, vintage, and appellation percentages are derived from the lots that went into it. This matters because in wine, composition is a legal claim: a label that says a variety or a region must be demonstrably true, and the lot's computed composition is what makes the claim defensible.

**The vessel estate.** Wine lives in vessels: tanks, barrels, and bins, held as identified containers with capacity, location, and current contents. The system knows what is in which vessel, how full it is, and where it stands — and barrels are typically tracked as individually identified vessels, groupable into programs and movable between locations. The vessel estate is the physical frame of the cellar: work orders name vessels, lab samples attach to vessels, and the winemaker's view of "what's in what" is a live picture of this estate.

**The recorded cellar operation.** The unit of change is the operation: crush, press, fermentation, rack, transfer, blend, addition, topping, filtration, and finally bottling. Each operation is recorded as an event that moves or transforms wine between vessels, and it *conserves*: what leaves one vessel, minus measured loss, is what arrives in the next — wine lost to the press pan, the hose, or evaporation is booked as loss with its cost, never silently dropped. Composition and cost travel with the wine proportionally: blend part of one tank with part of another and the new wine's varietal, vintage, appellation percentages, and cost are the exact quantity-weighted consequence of the inputs. Each committed operation writes into the lot's history, which is kept as an authoritative, audit-grade record — the reason a compliance report or a label claim can be reconstructed months later.

Three properties of the operation ledger deserve emphasis, because they are what the products are built to guarantee:

- **quantity is conserved** — volume is neither created nor destroyed between crush and bottle; operations that do not balance are not committed
- **composition follows the wine** — identity percentages and cost move with volume on every transfer and blend, computed rather than retyped
- **history is immutable** — committed operations leave a permanent record of what any vessel held at any point in the season

### What mature products add

Around this core, mature winery software carries a standard set of capabilities:

- **Lab and analyses** — sugar, acidity, pH, and sulfur-dioxide measurements attached to the vessel or lot they belong to; fermentation monitoring (cap management, pumpover planning); integrations that pull readings directly from lab instruments
- **Work orders** — planned and scheduled cellar work, assigned to people, teams, or clients, executed on mobile devices (often offline, in a cold cellar with no signal) and completed back into the record
- **Fruit intake and crush scheduling** — the weigh tag or grape-reception record that starts each lot's history; intake scheduled against crush-pad capacity; corrections after processing
- **Dry goods and additives inventory** — stocked supplies and additives, with lot codes and expiry dates where tracked; consumption carried to the wine as cost; ingredient traceability per lot
- **Bottling and finished goods** — packaging operations convert bulk wine into bottled products and case-goods inventory; the bottled product inherits the full composition and cost history of everything that flowed into it
- **Cost tracking to the lot** — fruit and freight costs, per-operation costs, storage costs, and overhead allocated to bulk wine and finished goods; cost per lot and per SKU
- **Compliance and traceability** — the operation record rolls up into the alcohol regime's reporting (in the United States, the TTB's production report computed from the season's operations, with every line traceable back to the operation behind it; elsewhere, excise and tax machinery on production and sales); two-directional lot traceability — which additive lot went into which wines, and which vineyard blocks are in which bottled product
- **Blending machinery** — trial blends to test a blend before committing it, composition preview, and label-rule checking where the regime defines one (in the US, the varietal and appellation percentage rules)
- **Barrel programs** — barrel groups, locations, topping to replace evaporation loss, stave additions, barrel-analysis device integrations
- **Bulk wine intake and dispatch** — wine received and shipped in bulk between wineries, with cost and compliance handling
- **Purchasing and sales orders** — purchase orders for supplies, barrels, and grapes; sales orders and price lists for bulk and finished wine
- **Roles and permissions** — role-gated operations and visibility across the winery team

### One structure, many implementations

The core model is conceptual; products realize it differently:

```text
Concept:   the lot's origin record (fruit becomes a lot)
Implementations:  weigh tag at the crush pad, scalehouse intake, bulk-wine intake record

Concept:   the lot's identity
Implementations:  batch code + varietal/vintage/origin fields; block-and-vintage
                  inheritance from the vineyard record; appellation set resolved
                  from block geography

Concept:   the compliance closure
Implementations:  US TTB production report computed from operations; Australian
                  wine-equalisation and excise handling; New Zealand excise;
                  wine declarations by analysis or treatment
```

A reader who has only seen one realization — say, a US product organized around TTB reporting — should still be able to recognize a regional product organized around excise and tax handling as the same Type.

## How It Works

### The season, one lot at a time

The defining workflow is the lot's journey through the season:

```text
Fruit arrives at the crush pad
→ weigh tag / intake record created (tonnage, block, vintage — the lot's origin)
→ crush into fermenter; ferment; press off
→ rack to tank or barrel
→ aging cellar work: rack off lees, top up, add (SO2 and others), sample
→ blending bench: trial blends, then the committed blend
→ bottling: the finished product inherits composition and cost
→ compliance: the season's operations roll up into the regime's report
```

Before a grape moves, the identity is usually already on file: the vineyard source, variety, vintage, and appellation set are established (in integrated products, from the vineyard record), so the intake record starts the lot's history with its identity attached.

### The operation-recording loop

Day to day, the cellar runs on a tight loop:

```text
work order issued (or operation needed)
→ cellar hand opens the vessel (often by scanning its code on a phone)
→ performs the work: rack, transfer, addition, topping
→ records it at the tank: source vessel, destination, quantity, additive and its lot
→ the operation commits: vessel contents, lot quantity, composition, and cost update
→ lab readings for that vessel sit on the same page the winemaker decides from
```

The loop's discipline is the point: because every operation is recorded once, at the moment it happens, the system's picture of the cellar is current, and the season's paperwork writes itself at the end instead of being reconstructed from whiteboards and memory.

### Blending

Blending is the season's mathematical climax. The winemaker composes trial blends, sees the resulting composition — varietal, vintage, and appellation percentages, and cost — before committing, checks it against the label rules the regime defines, and then commits the blend as an operation. The new lot's composition is computed from its inputs, never estimated.

### Bottling and the back office

At bottling, the finished product inherits everything: case count, blend percentages, per-bottle cost, all tracing back through the season to the intake records. The compliance report is then computed from the recorded operations — receipts, transfers, losses, taxable removals — with each line traceable to the operation behind it, and the filed numbers frozen as a snapshot.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Lot / wine list and lot detail

The system's center of gravity. Lists the winery's lots with variety, vintage, vessel, and volume; the detail view holds the lot's identity, current composition, cost, lab history, additions, and its full operation history. Primary actions: open a lot, trace its history, generate its record.

### Vessel / tank view

The cellar's physical picture. Shows each vessel's contents, fill level, capacity, and location — tanks, barrels, and bins; some products render the tank room as an interactive map. Primary actions: see what is in what, record an operation on a vessel, check capacity and vessel-space forecasts.

### Work orders

The cellar's task surface. Planned work (rackings, additions, sanitizing, barrel work) assigned to people or teams, with instructions and completion recording — on the web or on a phone at the vessel, including offline. Primary actions: create, assign, execute, complete.

### Lab entry

Where measurements land. Analyses entered manually or imported from lab devices, attached to the vessel or lot they belong to, with fermentation curves and current chemistry visible where decisions are made. Primary actions: enter or import results, review trends, request analyses.

### Blending bench

The composition surface. Build trial blends from available lots, preview the resulting varietal/vintage/appellation percentages and cost, check label rules, commit. Primary actions: compose, preview, check, commit.

### Bottling and inventory

Where bulk becomes product. Packaging operations draw wine from vessels into bottled goods; case-goods inventory tracks the results by product and location, alongside dry goods and supplies with their lot codes. Primary actions: record a bottling, manage stock, receive supplies.

### Compliance console

The regime-facing surface. The production report computed from the season's operations, with drill-back from each line to the operation behind it; declarations; excise and tax handling on the sales side. Primary actions: generate, review, file, snapshot.

### Costing views

Cost per lot and per product: fruit and freight, operations, storage, overhead, bottling. Primary actions: review cost buildup, allocate overhead, reconcile with accounting.

### Dashboard

The season at a glance: harvest progress and intake schedule, vessel space forecast, fermentation status, work outstanding, expiring supplies.

## Important Rules / Behaviors

### Operations must balance

The system will not commit an operation that creates or destroys volume: what leaves a vessel minus measured loss equals what arrives in the next. Losses (press pan, hose, evaporation) are booked explicitly, with their cost following the volume out. This conservation discipline is the ledger's integrity guarantee.

### Composition is computed, not typed

A lot's varietal, vintage, and appellation percentages are derived from its origin and every operation since. Retyping them is not how the system works; correcting them means correcting the underlying record. This is what makes label claims defensible after the fact.

### The history is authoritative

Committed operations write a permanent record. The system can show what any vessel held at any point in the season — which is what compliance reporting, audits, and label defense rely on. Some products allow recorded fruit or analyses to be corrected after the fact, but the correction is itself recorded.

### Vessels have limits

Capacity is enforced: overfilling a vessel is prevented or warned. Vessel-space forecasting exists because cellar capacity — tank space at crush, barrel inventory for aging — is a real constraint on the season's plan.

### Identity-carrying inputs are lot-controlled

Where traceability duties apply, tracked additives and supplies carry lot codes: receiving them requires a lot code, using them in an operation records which lot went in, and reports can show which wines — and which packaged goods — a given lot reached. Expiry tracking flags aging supplies.

### Regime state matters

In regimes with bonded production, wine carries a bonded/taxpaid state that governs what may be blended or moved; designations such as formula wines require flags; declarations are made on defined bases (analysis, treatment). Label rules — minimum percentages for a stated variety or appellation — are checked against the computed composition. The specifics vary by country; the existence of a regime-facing rule layer is structural.

### Permissions gate the record

Operations, corrections, and compliance filings are role-gated; the full activity trail is kept. Winery teams are small, but the record's legal weight makes attribution and control structural, not cosmetic.

## Variants

- **Production-led standalone** — cellar and production depth as the product's center, with vineyard, compliance, and costing around it (the mid-market standard)
- **Full business suite** — production packaged with vineyard tracking, case-goods inventory, cost accounting, and compliance as named pillars of one platform
- **Small-winery pole** — streamlined cellar software for producers who have outgrown spreadsheets, often with the compliance report as a headline feature
- **ERP-grade pole** — winery operations embedded in a fuller ERP frame (inventory, finance, production planning at ERP grain)
- **Custom crush facilities** — wineries making wine for client brands: work and storage attributed to clients and billed (per-operation billing, storage and hire charges, installments)
- **Estate vs grape-buying winery** — estate wineries consume their own vineyard records; grape-buying wineries run intake on grower deliveries, with fruit contracts and grower settlements at the seam
- **Multi-beverage platforms** — one platform selling winery, brewery, cidery, meadery, and distillery variants of the same lot/vessel/operation logic; hard seltzer and spirits (distilled-spirits-plant, dealcoholization) modules inside winery products
- **Sparkling-wine programs** — tirage, riddling, and specialized vessel machinery
- **Regional regimes** — US bonded/TTB semantics, Australian wine-equalisation and excise handling, New Zealand excise; the compliance layer reshapes per regime while the core holds

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Vineyard Management | upstream; the crush-pad seam | centers the vineyard planting (blocks, vines, viticultural work, ripening) and ends at weighed fruit credited to blocks; this Type begins at fruit intake, where the weigh tag starts the lot's history. A vineyard module inside a winery suite is that Type at module grain |
| Brewery Management | sibling in the fermented-beverage family | same family shape (batch/lot + vessels + time-extended process + materials in/packaged out + compliance); the seam is record flavor — beer's batch identity is recipe-executed (grain bill, hop schedule, gravity), wine's lot identity is blend-computed label composition (varietal/vintage/appellation percentages), over a barrel-heavy aging estate on a crush-season calendar |
| Distillery Management | adjacent sibling | centers spirits production (distillation runs, proof); appears inside winery products only as a distilled-spirits-plant / dealcoholization module |
| Harvest Management | handoff | centers the picking operation and credited harvest inventory on the grower side; ends where the winery's intake record begins |
| Food Manufacturing ERP | genus | generic batch manufacturing has batches, materials, and production orders but not the wine lot's label-computable identity, the barrel-heavy aging estate with topping and loss accounting, or the alcohol regime's bonded record |
| Food Traceability Platform | capability overlap | two-directional lot traceability is a capability built on the operation ledger here; traceability is not the center |
| Inventory Management System | partial overlap | generic inventory tracks stock levels; it does not carry composition and cost proportionally through transfers and blends |
| Restaurant POS / tasting-room retail | downstream | the sale surface (tasting room, wine club) is adjacent; winery products integrate with commerce but the production record is the center |

The boundary with Vineyard Management is the most important one, because winery suites package both sides. The structural test: if the system's center is the wine lot — its identity, its vessels, its operations — it is Winery Management; if the center is the planting asset, it is Vineyard Management. The weigh tag is the handoff object, owned by the winery side.

## Representative Products

- **vintrace** — global mid-market+ winery production software (Australian origin, now part of a beverage-industry platform); production-led pole with deep winemaking, compliance, costing, and custom-crush breadth
- **InnoVint** — US mid-market winery suite packaging vineyard tracking, wine production, inventory, cost accounting, and TTB compliance as pillars
- **Crush.wine** — US small/mid-winery cellar software built on a compute-from-operations philosophy: record each operation once at the tank, and quantity, composition, cost, and the compliance report follow

The core model was checked against two-decade-old market evidence (trade-press reviews of winery software from the mid-2000s and early 2010s describing weigh tags tracked through the winery to shipping, and tank views showing which vineyard blocks' grapes each tank contains) and against the paper-era winery record (cellar books, weigh tags, blend ledgers, filed production reports) to avoid over-fitting to the current mobile-cloud implementation.

## Sources

Research date: **2026-09-10**

- vintrace — Winery Software / Wine Production page: https://www.vintrace.com/wine-production-software
- vintrace — Help Center (Winemaking, Barrel Management, Bottling and Inventory, Compliance, Costing, Custom Crush Billing, Lab work, Work orders sections; Lot Tracking Traceability article): https://support.vintrace.com/hc/en-us
- InnoVint — product site and Wine Production (MAKE) page: https://www.innovint.us/ , https://www.innovint.us/product/wine-production/
- Crush.wine — product site and "Crush to Cellar" walkthrough: https://crush.wine/ , https://crush.wine/crush-to-cellar
- Cross-pass corroboration: paired research notes for vineyard-management (2026-09-10) and brewery-management (2026-09-06), including trade-press historical anchors (Wine Business Monthly vineyard/winery software reviews, 2006 and 2011)

> Sourcing limitation: two additional market products (a multi-beverage business-management platform and an ERP-grade winery suite) could not be reached from the research environment and are held as market anchors only, with no structural claims made from them; one previously sampled Australian winery product's domain now serves an unrelated product, so its winery-side observations are used only as corroboration captured in the paired vineyard research. Precise numeric limits, plan tiers, and vendor marketing statistics are intentionally not stated in this document; such details remain in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary resolutions with the vineyard and brewery passes are recorded in the paired Research Notes.
