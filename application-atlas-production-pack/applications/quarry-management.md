# Quarry Management

## Overview

A **Quarry Management** application is the site-and-sales system of record for an aggregate-producing operation — a quarry or pit that extracts and processes rock, sand, and gravel into saleable products and sells them by the ton.

Its defining core is small:

```text
Producing site (pit + plant) with its saleable products
└── Ticketed load — every weighed load of product leaving the site
    ├── → customer order → invoice / payment
    └── → stockpile movement → the site's material ledger
```

Three things are held together:

- **The producing site as the unit of record** — a persistent, identified quarry operation carrying a defined set of saleable products (crushed stone sizes, sand, gravel, screened or washed specifications).
- **The ticketed load as the atomic transaction** — each load of a specific product, weighed on the site's scale and recorded as a ticket bound to product, weight, vehicle and driver, and customer or order. The ticket is the record from which billing and inventory both move.
- **The site's material ledger** — stockpiles of each product at the site, built up by production and drawn down by ticketed sales loads, reconciled against physical measurement.

Everything else commonly associated with these products — driver kiosks, RFID truck recognition, GPS fleet tracking, customer portals, hauler marketplaces, ERP integrations — is widespread but not what makes the application a quarry management system. In fact the weighing-and-ticketing machinery itself is deliberately cross-industry: the same ticketing products serve landfills, agriculture, and bulk liquids. What makes this Type distinct is the producing-site context: extraction, processing, stockpiles of saleable products, and a direct product-sales loop off the site scale.

When the center of gravity shifts to mineral extraction feeding a processing or metals chain, the operation is managed by mining operations software instead; when it shifts to hauling between locations, it becomes a dispatch/trucking concern.

## Users & Context

The application is operated by the quarry's staff, with the scale house and dispatch as the daily center of gravity:

- **Scale operator / weighmaster** — records every load at the site scale: identifies the truck and product, captures tare and gross weights, issues the ticket.
- **Dispatcher** — schedules loads and trucks against orders, communicates with drivers and third-party haulers, tracks ETAs and cycle times.
- **Loader operator** — loads trucks from the correct stockpile; mature products give them a screen showing vehicles in-plant and what to load.
- **Quarry / site manager** — watches throughput, inventory position, and site performance across days and weeks.

Secondary users:

- **Sales / counter staff** — create quotes and orders, maintain products and pricing.
- **Back office** — billing prep, invoicing, accounts receivable, reconciliation of tickets to invoices.
- **Drivers and haulers** — check in (often self-service), receive load instructions, complete and confirm loads.
- **Customers** — place order requests, track deliveries, retrieve their tickets through a portal in mature deployments.

The environment is an industrial site: trucks cycle continuously between the scale, the stockpiles, and the gate; connectivity at the scale is treated as production-critical; and many sites run with minimal office staff, which is why self-service kiosks and unattended operation are common.

## Core Model

### The Defining Core

**The producing site.** The system is organized around the quarry operation itself: an identified site — commonly a pit with its processing plant (crushers, screens, washers) — held persistently with its identity, its location, and its catalog of saleable products. A producer running many sites holds them all in one system and rolls inventory and performance up across them.

**The saleable product.** Each product is a defined aggregate material — a size, specification, or processed grade — with a price basis. Products are what orders are placed for, what tickets name, and what the material ledger tracks. This product orientation (tons of defined materials sold to customers) is what separates a quarry from a generic weighing station.

**The ticketed load.** The atomic transaction is the load: a truck arrives, is weighed empty, is loaded with a specific product, is weighed full, and the system issues a ticket recording product, net weight, vehicle, driver, customer or order, and time. The ticket is the unit of sale, the input to billing, and the movement against inventory — one record, three consumers. Mature products expose the ticket instantly across the system the moment it is created and treat it as the single source of truth that downstream processes reference.

**The material ledger.** The site holds a live picture of its stockpiles: how much of each product is on the ground. Sales loads draw it down; production adds to it where production is tracked; and because stockpiles are physical and imprecise, the ledger is periodically reconciled against measurement — historically manual tallying, today commonly phone- or drone-based measurement of pile volumes converted to tonnage. Reconciliation against book inventory, and the write-offs it surfaces, is a recognized operational concern in this market.

### Capabilities Shared by Mature Products

A typical modern product carries most of these. They make the core practical but do not define the Type:

- **Orders and quoting** — quotes converted to orders; products and pricing maintained centrally so order, ticket, and invoice agree.
- **Dispatch** — a real-time board of orders, loads, trucks, and locations; scheduling with live ETAs; constraint-aware sequencing of trucks through the plant.
- **Scale automation** — driver kiosks covering check-in, tare-in, weigh-out, and ticket printing; automatic vehicle recognition; camera verification of loads; support for fully unattended scale operation alongside manual ticketing as a fallback.
- **Load-out support** — a screen for loader operators showing vehicles in-plant and the loads to be filled from the stockpiles.
- **E-ticketing** — digital tickets shared with customers and haulers, timestamped, with traceable change history when corrected.
- **Billing path** — billing prep, invoicing that combines product lines with freight, surcharges, environmental fees, and tax; accounts receivable; card and online payments.
- **ERP / accounting integration** — structured exports or automated feeds carrying ticket and invoice data to financial systems.
- **Fleet and driver tools** — driver mobile apps for load completion and confirmation; GPS tracking of trucks and loads; cycle-time measurement.
- **Multi-site roll-up** — inventory and performance dashboards spanning pits, yards, terminals, and plants.

### One Structure, Many Implementations

```text
Concept:          The load of record
Implementations:  weighbridge ticket, digital/e-ticket, paper ticket book (historical)

Concept:          Site measurement
Implementations:  attended scale house, kiosk + automatic vehicle ID + cameras (unattended)

Concept:          Material ledger
Implementations:  ticket-driven inventory updates, periodic physical measurement
                  (manual tally, phone/drone pile measurement, installed cameras)

Concept:          Hauling capacity
Implementations:  owned fleet with driver apps, third-party haulers, dispatch marketplace
```

A reader who has only seen a fully automated cloud deployment should still recognize a paper-ticket quarry with a hand-tallied stockpile ledger as the same kind of operation — the defining structure does not depend on any of the current automation.

## How It Works

### Set up the site and its products

```text
Register the site (pit + plant)
→ define its saleable products and price basis
→ connect scales and, where used, kiosks / vehicle ID / cameras
→ establish inventory baselines for the stockpiles
```

### Sell a load — the daily transaction loop

```text
Order (or quote → order) for a product
→ dispatch assigns trucks/haulers and sequences loads
→ truck checks in (kiosk or attended) → tare weight captured
→ loader fills the truck from the product's stockpile
→ truck weighs out → gross weight captured → net weight computed
→ ticket issued: product, weight, vehicle, driver, customer/order, time
→ ticket flows instantly to billing and to inventory
```

This loop is the application's heartbeat. Its speed is a managed metric: producers measure time-in-plant per truck, and automation (kiosks, vehicle recognition, live load-out screens) is sold on squeezing cycle time.

### Keep the material ledger honest

```text
Ticketed sales draw stockpiles down
→ production adds back (where tracked)
→ periodic physical measurement of piles (phone/drone/camera or tally)
→ reconcile measured tonnage against book inventory
→ investigate and record the variance (write-off or correction)
```

### Coordinate hauling

```text
Internal fleet and/or third-party haulers
→ driver receives assignment (app or dispatch)
→ driver punches in, completes loads, punches out
→ GPS/cycle-time tracking per truck and per load
→ hauler earnings computed from tickets/load slips
```

### Resolve the day

```text
End-of-day ticket exports (or automated feeds) to billing/ERP
→ invoices assembled from tickets (products + freight + surcharges + fees + tax)
→ payments and AR
→ disputes resolved against timestamped tickets
```

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Scale ticketing screen

The scale operator's primary surface.

- current truck at the scale, tare/gross/net weights, product, customer/order, ticket history for the day
- primary actions: identify vehicle and product, capture weights, issue or reprint ticket, correct with traceable history

### Dispatch board

The dispatcher's view of the day.

- orders, loads in progress, trucks and haulers, ETAs, site status
- primary actions: schedule and reassign loads, sequence trucks, communicate changes

### Load-out screen

The loader operator's surface.

- vehicles in-plant, loads to fill, product/stockpile to load
- primary actions: confirm loads filled, keep trucks moving to the correct pile

### Driver kiosk

Self-service check-in at the scale.

- identification, tare-in, weigh-out, ticket printing

### Driver mobile app

The hauler's surface.

- assignments, load completion and confirmation, earnings by job and period

### Inventory / stockpile view

The site's material state.

- stockpiles by product and site, ticket-driven movements, measurement results and variances
- primary actions: record adjustments, launch or review measurement, roll up across sites

### Sales orders & quotes; Customer portal

Commercial surfaces.

- quotes→orders, products, pricing, delivery tracking, ticket retrieval

### Back office

Billing prep, invoicing, payments, accounts receivable, ERP synchronization, and management dashboards spanning sites.

## Important Rules / Behaviors

### The ticket is the transaction of record

Sales, billing, and inventory all reference the same ticket. Mature products make the ticket immediately visible system-wide (legacy setups required a nightly "ticket out" replication step) and keep an audit trail: corrected tickets carry a traceable change history, which is what makes the record defensible in billing and delivery disputes.

### The weighing sequence is structured

A load is identified → weighed empty (tare-in) → loaded → weighed full (weigh-out) → ticketed. Each step may be attended or self-service; automatic vehicle recognition can make it effectively unattended. Manual ticketing remains supported as a fallback — including when site connectivity fails, which is why edge gateways and redundancy at the scale are treated as production infrastructure.

### Ticket fields are permissioned

Sensitive fields on the ticket screen — commonly freight rates and tax codes — can be hidden per user role while the ticket record stays complete underneath.

### Invoices assemble from tickets

One invoice commonly combines multiple products plus freight charges, surcharges, environmental fees, and other billable items, with tax computed from location-based rules. The ticket data feeding billing is expected to be complete and immediate; missing-paperwork gaps are treated as failures to engineer away.

### Inventory moves by recorded activity

The material ledger is driven by tickets (and, on the inbound side, received-material tickets). Discrepancies between book and measured inventory surface as write-offs; measurement programs exist precisely to bound them, and reducing year-end/month-end write-offs is a named selling point of the measurement pole.

### Disputes are answered with evidence

Timestamped tickets with weight, product, and delivery data are the instrument for resolving customer and hauler disputes — "you can't bill for what you can't prove" is the operating assumption.

## Variants

- **Commodity mix** — aggregate-only sites; aggregates alongside asphalt/HMA plants; integrated producers running aggregate, asphalt, and ready-mix on one platform family.
- **Scale of operation** — a single pit with one scale house, versus multi-site networks where inventory, orders, and performance roll up to central management.
- **Automation posture** — attended scale house with paper fallback; partially automated (kiosks + auto vehicle ID); fully unattended operation with camera verification.
- **Fleet model** — owned fleet with driver apps; predominantly third-party haulers; marketplace-based hauling where work is posted and haulers claim it.
- **Regional regimes** — legal-for-trade weighing requirements and ticket tax treatment vary by jurisdiction; regional ticket formats and tax rules are configuration, not structure.
- **Adjacent reusers** — the same machinery serves landfills/recycle yards, agriculture, and bulk liquids; these are different applications of the ticketing machinery, not quarry variants.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Mining Operations Management | centers on mineral extraction and production reporting feeding a processing/metals chain; quarry management centers on producing saleable products and selling them off the site scale |
| Mine Planning Application | reserves, geology, and pit design are the objects; quarry management runs the site's operations and sales once extraction is underway |
| Mining Fleet Management | equipment assignment, payload, and grade telemetry; quarry products may include fleet tracking as a module, but the Type's center is the site's production-inventory-sales loop |
| Inventory Management System | generic SKU stock management; the quarry's material ledger is bound to producing sites, weighbridge tickets, and tons of defined aggregate products |
| Dispatch Management (Trucking) / hauling platforms | coordinate trucks between locations; in quarry management the dispatch leg is embedded in the site's own order→load→ticket→billing loop, and hauling data is consumed rather than the point |
| Grain Elevator Management | shares the weigh-in/weigh-out ticket machinery family, but handles third-party growers' grain (receipts, grades, storage) rather than producing and selling its own extracted product |
| Natural Resource Rights Management | land, lease, and rights administration is a separate Type; no rights objects appear in the quarry sample |

The most important boundary is with generic weighbridge ticketing: the ticketing machinery is cross-industry by design. Remove the producing site and its material ledger, and what remains is a bulk-materials ticketing platform, not quarry management.

## Representative Products

- **Command Alkon** — Apex (quarry and plant automation, scale ticketing) and Command Cloud's Dispatch & Scale Ticketing and Material Supply; the incumbent enterprise suite for aggregate producers.
- **Trux** — cloud ticketing "purpose-built for quarries, pits, and HMA plants" plus dump-truck dispatch, hauler marketplace, and e-ticketing.
- **Stockpile Reports** — specialized stockpile-measurement pole (phone/drone/camera imagery → verified tonnage per pile by product and site); included as the boundary anchor for the measurement capability, not as a full management system.

## Sources

Research date: **2026-09-09**

- Command Alkon — https://www.commandalkon.com/ , https://www.commandalkon.com/aggregate/ , https://www.commandalkon.com/products/apex/ , https://www.commandalkon.com/products/dispatch-and-scale-ticketing/ , https://www.commandalkon.com/products/material-supply/
- Trux — https://www.truxnow.com/ , https://www.truxnow.com/products-trux-ticketing/
- Stockpile Reports — https://www.stockpilereports.com/

> Sourcing limitation: vendor help-center articles were not reachable from the research environment on 2026-09-09 (Trux help center timed out; third-party software directories were blocked), so all claims rest on official product and FAQ pages rather than step-level operational documentation. Precise operational parameters (numeric limits, exact defaults, specific regulatory machinery, royalty handling) are intentionally not asserted in this document; they are recorded as open questions in the paired Research Notes.
