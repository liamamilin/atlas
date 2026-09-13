# Tool Management

## Overview

A **Tool Management** application is a manufacturing organization's system of record for its production tooling: it holds the organization's tools as an identified population, operates their circulation between storage and the points of use, and manages tooling as a consumed and replenished supply.

The defining core is small and jointly held:

```text
Tooling population of record
└── Issue / return circulation loop
    └── Tooling supply & consumption loop
```

- The **tooling population of record** — tool and item types carried as stock positions, individually identified physical units (labeled, barcoded, or chipped), and, in machining-focused products, tool assemblies composed of components — each record carrying location, custody, and condition.
- The **issue/return circulation loop** — recorded transactions that move tools between the tool crib, storeroom, cabinets, or point-of-use dispensers and the people, jobs, cost centers, and machines that use them, keeping custody, availability, and location current and attributable.
- The **tooling supply & consumption loop** — usage recorded per issue, tools cycling through wear, repair, regrind, recalibration, or scrap, minimum-stock and reorder machinery replenishing the population, and usage charged back to users, cost centers, or jobs.

Remove the circulation loop and the product becomes a static asset register or stock list. Remove the supply/consumption loop and it becomes a library-style checkout tracker — the shape tools take when they ride inside maintenance software as ordinary assets. Remove the population of record and there is nothing for the transactions to operate on. All three legs are load-bearing together.

Everything else commonly associated with the category — barcode/RFID identification, vending machines and smart cabinets, kiosks, calibration scheduling, rental billing, CNC tool-data interfaces — is a widespread implementation or a segment variant, not part of the definition. A paper-era tool crib with a card file, a sign-out board, a regrind rotation, and a reorder practice satisfies the same core.

## Users & Context

Primary users:

- **Tool crib attendants / storeroom staff** — issue and receive tools, keep the crib's stock and records true, send worn tools to service, prepare replenishment.
- **Production workers, machinists, maintenance technicians, contractors** — draw tools for a job or shift, return them, and are accountable for what they hold.
- **Tooling / manufacturing engineers** (prominent in machining plants) — maintain tool definitions, assemblies, and measured data; decide what tooling the plant needs.

Secondary users:

- **Purchasing / supply chain** — receives consumption signals and reorder suggestions; buys tooling.
- **Production / operations management** — consumes availability and cost views; owns the downtime and spend outcomes.
- **Finance / controlling** — consumes usage-based chargeback to cost centers and jobs.

The work environment is the factory floor and the job site: a staffed tool crib or storeroom, unmanned point-of-use dispensers, and machines and work areas where tools are consumed. In machining plants the system also reaches the tool room (assembly, presetting, measuring) and connects upward to planning and purchasing systems.

## Core Model

### The tooling population of record

The system's backbone is a persistent register of the organization's tooling, held at up to three granularities that coexist in mature products:

- **Item / tool types as stock positions** — a defined tool or consumable (a class of item) carried with a quantity on hand, one or more storage locations, and reorder parameters. Consumables (inserts, bits, gloves) live naturally at this level.
- **Individually identified units** — durable tools labeled with a barcode, RFID tag, or chip so that each physical tool is its own record with its own custody, history, and condition. This is what makes "who has which tool" answerable.
- **Tool assemblies of components** (machining products) — a complete cutting tool composed of holders, adapters, and inserts, with the assembly's identity distinct from its parts, so that the assembly can be booked, measured, and issued as one unit while its components are tracked underneath.

Each record carries its **location** (crib, cabinet, machine, job site), its **custody** (who currently holds it), and its **condition/status** (new, in service, worn, out for repair, scrapped). In machining products the record additionally carries the tool's **production data** — geometry and measured values, tool life — because the same record feeds both the crib and the machine.

### The circulation loop

Tools move through recorded transactions. The recurring set, expressed conceptually (exact vocabularies vary by product):

```text
Receive into stock
→ Issue (checkout) to a person / job / cost center / machine
→ Use
→ Return (check-in) — or transfer to another holder or location
→ …or send out for service (repair / regrind / recalibration)
→ return to stock, or scrap and replace
```

Every movement is recorded against the tool record and the parties involved, which is what produces the system's two core answers at any moment: **where is each tool, and who is accountable for it**. The transaction log is also the audit trail that loss, hoarding, and disputes are settled from.

### The supply & consumption loop

Tooling is treated as a supply that production consumes, not a static asset base:

- **Consumption per issue** — each issue (and each dispensed consumable) records usage against the item, the taker, and a cost object.
- **Decay and service cycles** — worn tools go out for regrind, repair, recalibration, or recertification and either return to stock or are scrapped; the cycle is a routine part of the flow, not an exceptional event.
- **Replenishment** — stock positions are watched against minimum levels; low stock triggers reorder suggestions or purchase orders into the purchasing process.
- **Cost allocation** — usage is charged back to the users, cost centers, jobs, or projects that consumed it, making tooling spend visible and attributable.

### One structure, many implementations

The core is conceptual; products realize it differently:

```text
Concept:            identified tool unit
Implementations:    barcode label, RFID tag, embedded chip, (machining) tool assembly ID

Concept:            storage / point of issue
Implementations:    staffed tool crib, storeroom, cabinet, vending machine, smart cabinet, kiosk

Concept:            issue destination
Implementations:    employee/contractor, job or project, cost center, machine / tool magazine

Concept:            consumption signal
Implementations:    checkout transaction, vending dispense, scale weigh, bin-sensor depletion
```

A reader who has only seen one implementation — say, an RFID vending crib — should still be able to recognize a staffed crib with barcode scanners, or a machining tool room with chipped tool assemblies, as the same Type.

## How It Works

### Put the tooling under management

```text
Define item/tool types (and, in machining, components and assemblies)
→ label each durable unit (barcode / RFID / chip) and register it
→ set storage locations and stock/reorder parameters
→ the population of record is now live
```

### Run the daily circulation

```text
Worker presents identity (badge / scan / kiosk login)
→ tool is scanned or vended
→ system records: which tool, to whom, for which job/cost center, when
→ worker returns the tool (or a dispenser accepts it back)
→ custody and availability update in real time
```

In a staffed crib the attendant performs these bookings with a scanner; at a vending machine or kiosk the worker self-serves and the transaction records itself. The result either way is the same live picture: what is in stock, what is out, and who holds it.

### Work the consumption and replenishment cycle

```text
Usage accumulates per item and cost object
→ stock position falls
→ minimum-stock check raises a reorder suggestion
→ purchasing creates and tracks the purchase order
→ goods received back into crib stock
→ worn/dulled tools sent to service; regrind/recalibration returns them to stock, or they are scrapped
→ usage charged back to cost centers / jobs
```

### The machining tool-data loop (machining products)

In metal-cutting plants the same record base carries the tool's production data:

```text
Define components and assemble complete tools
→ measure on a presetting/measuring device; measured geometry flows into the record
→ tool data (geometry, offsets, tool life) transferred to CAM systems and CNC machines
→ tool issued and mounted; usage and tool-life consumption recorded
→ worn assembly back to the tool room; re-measure, re-cut or scrap; data updated
```

Here the tool record serves two consumers at once: the crib (physical availability) and production (correct data on the machine). Vendors in this pole describe their systems as the link between ERP/PLM/MES and the shop floor precisely because both flows meet in one tool record.

### Capability tiers

**Defining core** — without these, not tool management:

- tooling population of record (types with stock, identified units, machining assemblies)
- recorded issue/return/transfer circulation with custody and availability
- supply & consumption loop (usage, service cycles, replenishment, cost allocation)

**Standard capabilities** in mature products:

- barcode/RFID/chip identification with mobile scanners and kiosks
- service/maintenance/calibration scheduling attached to tools
- purchasing/replenishment module
- usage-based cost allocation and chargeback reporting
- multi-location / multi-crib / multi-plant operation
- usage reporting and crib statistics
- ERP integration for inventory and purchasing activity

**Common variants / optional:**

- point-of-use vending machines, smart cabinets, scales, bin sensors
- CNC tool-data management (assemblies, measured geometry, tool life, CAM/CNC/presetting interfaces) — the machining pole
- rental management with rates and billing (construction segment)
- PPE and indirect-materials breadth alongside tooling
- cloud or on-premise deployment

## Interfaces

Described conceptually; names and layouts vary by product.

### Crib / issue-return workstation

The transaction surface of the crib or storeroom.

- tool lookup by scan or search, item detail (stock, location, custody, condition)
- primary actions: issue, return, transfer, send to service, record scrap, count

### Self-service point (kiosk / vending)

The worker-facing capture surface.

- identity sign-in, tool dispense or return, immediate transaction recording
- primary actions: check out a tool, return a tool, see what I hold

### Item / tool record

The per-tool detail surface.

- identification, type, serial/label, location, custody, condition, transaction history, service history, (machining) assembly composition and measured data
- primary actions: edit attributes, view history, schedule service, adjust stock

### Stock & replenishment views

The supply-control surface for crib staff and purchasing.

- stock positions by item and location, minimum-level alerts, reorder suggestions, purchase-order status
- primary actions: review alerts, create/track purchase orders, receive goods

### Tool-data management surface (machining products)

The engineering-facing surface of the tool record.

- component catalog, assembly builder, measured geometry, tool-life data, graphics
- primary actions: build/modify assemblies, import measured data, transfer data to CAM/machines

### Reporting / controlling

- usage by item, user, cost center, job; stock-out and consumption trends; tooling spend
- primary actions: filter, export, feed chargeback

## Important Rules / Behaviors

### Custody is transactional, not assumed

A tool's holder changes only through a recorded transaction. The register stays true because every hand — attendant, kiosk, vending machine, scanner — writes the same kind of record. Untracked movement is the failure mode the discipline exists to prevent.

### Availability gates production

The point of the live picture is that production can trust it: an availability check before committing a job to a machine is what prevents tool-related stoppages. Machining vendors state this explicitly — the right tool on the right machine at the right time.

### Consumables and durable tools follow different record shapes

Durable tools are individually identified and circulate by custody; consumables are carried as stock and deplete by issue. Mature products hold both shapes side by side in one system.

### Service is a loop, not a dead end

A tool sent for repair, regrind, or calibration remains in the population in a distinct state and returns to stock (or is scrapped with a recorded reason). The cycle is expected and repeated, which distinguishes tooling from ordinary fixed assets.

### Usage has a cost object

Issues are recorded against users, cost centers, jobs, or projects so that tooling spend can be charged back. Products differ in how elaborate the chargeback is (simple usage reports to full internal rental billing), but the attribution principle is common.

### Condition and location travel together

The record answers "where is it" and "what state is it in" as one picture; a tool that is out for regrind is both somewhere else and not available, and the system holds both facts.

## Variants

- **Crib / tracking pole** — general industrial tooling (construction, utilities, mining, oil & gas, power generation, maintenance shops); staffed cribs and storerooms; barcode/RFID tracking; often extended with PPE and indirect materials; rental billing in the construction segment.
- **Point-of-use vending variant** — the crib is partly or fully automated: industrial vending machines, smart cabinets, scales, and bin sensors dispense and receive items and record transactions at the point of use; popular where accountability for high-volume consumables matters.
- **Machining tool-data pole** — metal-cutting plants; the record base carries tool assemblies, measured geometry, and tool life, and the system integrates with presetting/measuring devices, CAM systems, and CNC machines; tool circulation and tool data are managed as one.
- **Gage crib overlap** — measurement instruments circulate through the same issue/return machinery; where measurement fitness (procedures, intervals, certificates) becomes the center, the domain is calibration management.
- **Deployment variants** — cloud-hosted, vendor-hosted, and on-premise all exist; desktop clients, web clients, and mobile scanning apps are combined differently by product.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Equipment Administration Platform | adjacent, shared skeleton | both hold identified item records with recorded handover; equipment administration centers the custody/readiness loop over general shared equipment, without tooling supply economics (stock, consumption, reorder, chargeback) as the spine |
| CMMS / Maintenance Management | adjacent, module-level overlap | CMMS centers maintenance work orders over assets; tools ride inside as assets with check-in/out. Tool management centers the crib circulation and supply loop; tool repair is a loop endpoint, not a work-order spine |
| Calibration Management | adjacent, gage-crib seam | gage issue/return is circulation machinery this Type provides; calibration procedures, intervals, as-found/as-left results, and certificates are the other Type's center |
| Inventory Management System | adjacent, consumable seam | crib stock of consumables is inventory-like; the tooling population's individual identity, circulation, and production binding are the seam. A pure goods stockroom is inventory management |
| Construction Equipment Management | sibling, population seam | heavy machines and fleet (telematics, utilization) vs small tools; mixed products track small tools as an adjacent population |
| CAM / CNC Programming | upstream consumer | CAM references tool assemblies inside programs; tool management is the system of record for the tooling data and inventory that CAM, presetting, and machines draw from |
| Enterprise Asset Management / Registry | broader/different economics | EAM holds whole-life governance over major assets; tooling is a high-churn, low-unit-cost circulating population managed as supply |
| Construction Materials Management | sibling, durability seam | materials are consumed; tools are durable reusable units that circulate |

The most important boundary is with Equipment Administration Platform and the CMMS tool module, because both share the "identified items + handover" skeleton. The distinguishing leg is the supply & consumption loop: stock positions, consumption per issue, wear/service cycles, replenishment, and usage-based chargeback. A checkout tracker without that loop is one of those neighbors; with it, it is tool management.

## Representative Products

- **CribMaster** (Stanley Black & Decker) — crib/vending pole; inventory software suite with industrial vending, RFID portals, scales, and bin sensors; enterprise manufacturing, aerospace, and MRO installations.
- **ToolHound** — crib/tracking pole; software-first tool inventory management for construction, industrial, mining, utilities, and oil & gas; cloud or on-premise.
- **TDM Systems** (Sandvik / Walter) — machining tool-data pole; central tool database with tool assemblies, CAM/CNC/presetting interfaces, plus a tool crib module and ordering.
- **ZOLLER TMS / webTMS** — machining tool-data pole; tool management software with smart cabinets, presetting/measuring integration, and CAM/machine data transfer.

The core model was checked against a CMMS tool module (tools as assets with check-in/out, no supply economics) as the documented contrast shape, and against paper-era tool crib practice for historical fit.

## Sources

Research date: **2026-09-10**

- ToolHound — https://www.toolhound.com/ ; https://www.toolhound.com/products/toolhound-system-overview
- TDM Systems — https://www.tdmsystems.com/en ; https://www.tdmsystems.com/en/solutions/tool-management/what-is-tool-data-management/ ; https://www.tdmsystems.com/en/solutions/shopfloor-management/tdm-tool-crib-module/
- ZOLLER — https://www.zoller.info/en_DE/solutions/tool-management/software ; https://www.zoller.info/en_DE/tool-management
- CribMaster (Stanley Black & Decker) — https://www.cribmaster.com/ ; https://storage.stanleyblackanddecker.com/cribmaster/products/software ; https://stanleyblackanddecker.com/brands/industrial/cribmaster
- Limble CMMS Help Center — https://help.limblecmms.com/en/articles/7020225-using-tools-in-limble (boundary witness)
- Reliable Plant — Boeing Mesa tool-crib case study: https://www.reliableplant.com/Read/4891/lean-inventory-control-boeing

> Sourcing limitation: cribmaster.com could not be fetched directly (repeated timeouts); CribMaster evidence rests on official Stanley Black & Decker pages reached through search plus one independent case study. No help-center/user-manual-grade operational documentation was fetched for the crib-pole products. Exact transaction-type lists, state vocabularies, and numeric limits are therefore not stated in this document; vendor benefit claims are excluded.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
