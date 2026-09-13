# Harvest Management

## Overview

A **Harvest Management** application is the grower's or farm operator's system of record for running the harvest operation itself. It records the work of picking as it happens — what was picked, from which block, when, how much, and by whom — turns that work into identified, credited harvest inventory (bins, totes, crates, loads) that stays traceable from the field to the receiving dock, and manages the harvest as a bounded campaign: real-time progress, expected-versus-actual yield, and reconciled totals per block and variety.

The defining core is small:

```text
Production unit (block / field / orchard)
└── Harvest campaign (the season's picking, run as one operation)
    ├── Harvest event — attributed record of picking production
    ├── Harvest inventory — the picked product as identified, credited units
    └── Campaign close — reconciled totals and handoff to the next stage
```

Everything else commonly associated with modern products — barcode tags, offline mobile apps, piece-rate payroll, computer-vision quality checks, receiving and storage modules — is widespread in current products but is not what makes the product a harvest-management application. The pre-digital pattern (a crew tally sheet, a bin ticket stapled to each bin, a load ticket to the winery or packing house, a harvest book of per-block totals) satisfies the same definition.

When the center of gravity shifts — to the crop's whole growing season, to the workforce and their pay, to the packing line, or to the machines doing the work — the product is drifting toward a different Application Type (Crop Management, Farm Labor Management, Produce Packing House Management, Precision Agriculture).

## Users & Context

The primary user is the **harvest or operations manager** on a specialty-crop or high-value-crop operation (orchard fruit, berries, table and wine grapes, nuts, vegetables): the person accountable for getting the crop off the plant, crediting it correctly, and delivering it to the packhouse or processor with records intact.

Around that primary user, a working harvest system is touched by:

- **crew leaders / field supervisors** — carry the field device into the block; log and tag bins, credit pickers, and keep the record moving while the crew picks
- **pickers and field workers** — the people whose production is credited; they generate the record by working, and their credited totals follow them to pay
- **office staff and bookkeepers** — watch totals and costs, run payroll exports and reports, resolve tally disputes
- **packhouse / receiving staff** — the receiving end of the handoff: they take in loads against the field's records rather than starting fresh paper
- **farm owner / management** — read yield, quality, and cost outcomes by block and variety

The work environment is the harvest itself: weeks of peak intensity, crews spread across blocks, connectivity unreliable in the field, and every unit of fruit needing to be counted, credited, and traceable the day it is picked. Mobile capture at the point of picking is the norm; the office watches the same records accumulate in real time. The season ends, but the records persist as the block- and variety-level history the next season's planning leans on.

## Core Model

### The Defining Core

Three structures, held together. Remove any one and the product stops being recognizable as harvest management:

- **The harvest event as the unit of production record.** A harvest event is a dated, attributed record of picking production bound to an identified production unit — the block, field, or orchard section. It captures what was picked (crop, variety), where (block, often row), when, how much (count or weight), and commonly by whom. Events are recorded at or near the moment of picking, not reconstructed later, and they accumulate into live totals by block and variety. Without the event record, there is only an agronomic yield log — harvest as a data point in a crop record, not an operation being run.

- **The harvested product as credited, traceable harvest inventory.** The moment fruit is picked it becomes product, and the system holds it as inventory: discrete identified units — bins, totes, crates, buckets, lugs, truckloads — each carrying the identity of its block and its picker. The physical link is a ticket or tag (handwritten in the analog pattern; printed, scanned, or barcode/QR-linked in current products) that turns a physical container into a record the system can credit, follow, and reconcile. Without this, the product is a tally sheet or a container-tracking tool with no harvest semantics.

- **The harvest campaign as a managed whole.** The season's harvest is run as one bounded operation: progress and accumulation are watched as they come in, expected yields are compared with actuals, field records are reconciled against what the dock or packhouse receives, and the campaign closes with block- and variety-level totals. Without this, the system is per-event recording machinery with no managed season — exactly the nightly-reconciliation burden the products exist to remove.

### How the Structures Bind

```text
Block / field / orchard  (the production unit)
   │
   ├── Harvest estimate  (expected yield — what this block should give)
   │
   └── Harvest campaign (the season)
         ├── Harvest event  (what / where / when / how much / by whom)
         │      └── materializes as →
         ├── Harvest inventory unit  (bin / tote / load — tagged, credited)
         │      └── moves as →
         └── Handoff  (receiving at packhouse / processor / storage)
                └── reconciled back into →
                     Campaign close (totals by block, variety, picker, cost)
```

Two properties are worth stating plainly:

- **Attribution is double-sided.** Every inventory unit points at a production unit (where it came from) and at a worker or crew (who produced it). This is what lets the same record serve traceability ("which block did this fruit come from?") and crediting ("what did this picker pick?") at once.
- **Inventory custody is temporary but continuous.** The system is the product's custodian only across the harvest window — from tree or vine to dock — but during that window every unit is findable: picked where, picked by whom, received where, stored where.

### Capabilities Shared by Mature Products

A typical modern harvest-management product carries most of the following. They make the operation practical; they are not what defines the Type:

- **Worker crediting and pay feed** — credited units accumulate per picker and crew, feeding piece-rate and hourly payroll calculations and exports. The workforce machinery itself (rosters, schedules, wage rules) belongs to farm labor management; here it appears as attribution of production.
- **Harvest-time quality assessment** — inspection templates scored against per-variety specs (size, color, firmness, defects), maturity readings (sugar, starch, pressure) captured on the same record, increasingly supported by computer-vision scans of bins or fruit.
- **Harvest estimation** — projected yields per block, maintained through the season and compared against actuals; depth varies by product (some link estimates to crew, storage, and sales commitments).
- **Offline-first field capture** — recording, tagging, and crediting work without connectivity and sync when signal returns.
- **Receiving and storage records** — inbound loads recorded at the dock against lot or tag identity; bins scanned into cold or controlled-atmosphere storage with location detail.
- **Reporting and analytics** — yield by block and variety over time, picker productivity, cost per bin, per block, or per acre.
- **Integrations** — payroll export, packhouse systems, and traceability reporting outward.

### One Structure, Many Implementations

```text
Concept:   production unit        Implementations: orchard block, field, vineyard rows, ranch
Concept:   identified inventory   Implementations: printed bin tag, scanned existing ticket, QR tag,
           unit                     bulk end-of-shift entry, weigh ticket
Concept:   crediting              Implementations: per-picker credit at tag time, crew credit divided,
           attribution              hourly + piece-rate mixed schedules
Concept:   campaign oversight     Implementations: live bin counts, estimate-vs-actual reports,
                                    cost-per-block analytics, dock reconciliation
Concept:   handoff                Implementations: receiving records at the dock, early inventory
                                    visibility for the packhouse, lot codes carried onward
```

A reader who encounters only one implementation — say, a crew leader scanning pre-printed QR tags on apple bins — should still be able to recognize a bulk-recording vegetable operation or a paper-ticket era system as the same Application Type.

## How It Works

### Before the crews arrive

```text
Register the season's production units (blocks, varieties)
→ record expected yields per block (estimates, revised as the season runs)
→ set up crews, leaders, and pay rates (hourly floors, piece rates per unit)
→ choose the recording workflow (pre-print tags, tag as you go, bulk entry)
```

The estimate is the campaign's expectation: crews, storage bookings, and sales commitments are arranged against it.

### The picking loop

```text
Crew works a block
→ crew leader logs or tags each unit as it fills
   (scan a pre-printed tag, print a tag, or log the bin)
→ the unit is credited: block + variety + picker(s) + time
→ totals accumulate live (bins by block, credit by picker)
→ quality checks happen at the bin while the block is open
→ repeat across blocks and days
```

This loop is the system's heartbeat. The record exists as a byproduct of doing the work — the ticket is made when the bin is made — which is why payroll disputes and end-of-day tally reconciliation shrink rather than merely get faster.

### The handoff

```text
Bins / loads leave the field
→ receiving records the inbound load against its tag or lot identity
   (supplier, block, arrival time)
→ fruit bound for storage is scanned into rooms with location detail
→ field records and dock receipts reconcile against each other
→ the packhouse or processor works from the same records the crew created
```

In products that extend past the dock, the lot's identity — grower, block, variety, picker, date — travels with the fruit, and each later step appends to it.

### Closing the campaign

```text
Harvest ends on a block
→ totals close per block, variety, picker, and cost
→ actuals are compared with estimates and with prior seasons
→ the record persists as the yield and performance history
   the next season's estimates and decisions start from
```

### Core vs Standard vs Optional

**Defining core** — without these, not harvest management:

- harvest events as attributed production records on identified production units
- the picked product held as identified, credited, traceable inventory units
- the harvest campaign run and closed as a managed whole

**Standard capabilities** — present in most modern products:

- worker crediting feeding piece-rate/hourly pay
- harvest-time quality and maturity assessment
- yield estimation and expected-versus-actual comparison
- offline-first mobile capture
- receiving and storage records at the dock
- reporting, analytics, and payroll/packhouse integrations

**Common variants** — depend on crop, operation style, and packaging:

- field packing (labels, inventory, productivity at the point of packing)
- harvest packaged as a module inside broader farm-management products
- machine-executed harvest overseen through equipment telemetry
- capture vocabulary varying by crop: buckets and lugs for berries, bins for orchards, loads for machine harvest

## Interfaces

The following surfaces are described in conceptual terms; exact layouts and names vary by product.

### Field capture app (crew leader's device)

The in-field surface where the record is created.

- fast unit logging: record or scan a bin in seconds, offline-capable
- per-unit attribution shown at capture time (block, picker, time)
- primary actions: log a unit, scan or print a tag, credit a picker, run an in-field quality check

### Tag / ticket printing and scanning

The physical-digital link for harvest inventory.

- printed or pre-printed tags with barcodes or QR codes; support for scanning tickets a operation already uses
- primary actions: generate tags, scan a ticket into a record, reprint or correct attribution

### Campaign dashboard (office / web)

The real-time oversight surface.

- live totals by block, variety, and day; picker and crew credit views; estimate-versus-actual comparison
- primary actions: monitor progress, spot underperforming blocks or crews, adjust plans and bookings

### Receiving / dock records

The handoff surface at the packhouse.

- inbound loads listed against tag or lot identity with source and arrival detail; storage locations where fruit is placed
- primary actions: receive a load, record storage placement, reconcile dock receipts with field records

### Reports & analytics

- yield by block/variety over time, productivity and quality by picker and crew, cost per bin/block/acre, audit- and traceability-oriented reports
- primary actions: run a report for a period or block, export to payroll or packhouse systems, answer an audit query

### Setup & administration

- production units and varieties, crews and pay rates, tag formats, recording-workflow choices, user roles

## Important Rules / Behaviors

### Attribution completeness is the point

A unit without block and picker attribution is a failed record: the same event feeds traceability and crediting, so both identities attach at capture time. Products are built so the attributed record is a byproduct of the physical act (tag the bin, credit the picker) rather than a separate bookkeeping task.

### Field reality governs the capture design

Connectivity drops in blocks; crews move; thousands of units move in a day. Mature products therefore offer multiple recording workflows (pre-printed tags, tag-as-you-go, bulk end-of-shift entry) and offline capture with sync, treating connectivity as a variable rather than an assumption.

### The field and the dock must reconcile

The system's authority depends on the field's records and the packhouse's receipts matching. Receiving records the inbound load against the tag or lot identity created in the field; early inventory visibility lets the packhouse plan before fruit arrives. Where they diverge, the reconciliation is the exception that must be resolved.

### Quality windows close fast

Quality decisions belong at the bin while the block is still open — once picked, fruit moves toward storage or packing quickly, and defects discovered at the dock are discovered too late. This timing pressure is why inspection templates and vision scans ride on the harvest record rather than on later packhouse systems.

### Pay rules reach into the record

In regions with piece-rate rules, harvest records may carry pay-law consequences: credited units must support compliant pay calculations, and incidental time may need separate treatment. The payroll machinery belongs to the labor-management Type, but the harvest record is the evidence it computes from.

### The campaign closes; history persists

Season totals per block and variety are the system's memory. They seed next season's estimates, benchmark blocks and varieties against each other, and anchor audit answers ("which block, which picker, which day") long after the fruit is gone.

## Variants

- **Dedicated modular harvest systems** — harvest-first products sold as a core (harvest recording + crediting) with optional additions (field packing, quality, storage, receiving); typical of specialty-crop growers and packers.
- **Harvest as a module inside farm-management suites** — smaller or diversified farms record harvests, yields, and inventory inside all-in-one farm software; same core structures, lighter campaign machinery.
- **Mechanized-execution oversight** — operations where harvest is done largely by machines: the harvest window is managed through equipment telemetry (activity by block, speeds, throughput), with the product side thin or absent; shares the campaign idea, realizes the event record as machine activity. Drifts toward precision-agriculture territory.
- **Crop-specific vocabularies** — berry crews credited by bucket or lug, orchard operations moving thousands of bins in a day, weigh-ticketed truckloads; same spine, different unit names.
- **Processor-side harvest intake** — a winery or processor managing inbound grower fruit and grower credit through the same ticket-to-receiving logic (observed only as the receiving end of the handoff in this research; not independently verified as a standalone product form).

## Related Application Types

| Application Type | Distinction |
|---|---|
| Crop Management | owns the crop-season across its whole cycle — plan, inputs, sprays, observations; harvest is its closing record. Harvest management owns the harvest operation and the picked product itself. Some vendors ship both |
| Farm Labor Management | owns the workforce — worker records, crews, schedules, hours, pay owed. Harvest management attributes production to workers but does not manage them; the two meet where credited bins become pay records |
| Produce Packing House Management | owns the processing after the dock — packing lines, food safety, finished goods. Harvest management's custody ends at the handoff; receiving is the seam |
| Food Traceability Platform | owns the chain-wide lot ledger across partners. Harvest management is one event source plus field-side custody, not the cross-partner join |
| Precision Agriculture Platform | owns the variable-rate machine execution loop and equipment data. Machine-harvested operations realize harvest through telemetry; the credited-product inventory spine is absent |
| Farm Management Platform | owns whole-farm business operations — finance, marketing, inventory, payroll. Harvest management is operation-scoped, not business-scoped |
| Grain Management | owns stored-grain condition and conditioning after the grain is in storage — a different object and season entirely |
| Orchard / Vineyard Management | the crop-management pattern scoped to perennial crop types and their structures; harvest appears there as one phase, not the center |
| Winery Management | adjacent at the crush: fruit intake is the receiving end of the harvest handoff; fermentation and production are a different Type |
| Generic Inventory Management | harvest inventory is perishable, field-born, and production-attributed; without production-unit attribution and the season shape it is a different system |

The two boundaries that matter most: against **crop management**, the seam is the season (crop management treats harvest as closure; harvest management centers it); against **farm labor management**, the seam is the center (harvest management centers what was picked and where it went; the workforce is attribution, not the managed population).

## Representative Products

- **Croptracker** — modular farm software for fruit and vegetable growers whose harvest line covers harvest events, bin tags, estimates, crediting, field packing, quality, receiving, and storage (North America and international)
- **Hectre** — orchard management software whose harvest line covers bin ticketing, real-time crediting, progress, picker performance, and packhouse traceability (New Zealand/Australia origin, international packers)
- **Fieldin** — mechanized-operations platform for high-value permanent crops; included as the boundary case where harvest is overseen as machine execution rather than product inventory

Harvest-recording modules inside broader suites (for example all-in-one farm software) were also examined to confirm the module-packaging variant; a wine-grape harvest-tracking vendor and a European orchard app were attempted but unreachable and are not counted as evidence.

## Sources

Research date: **2026-09-08**

Primary vendor surfaces (official product pages):

- Croptracker — https://www.croptracker.com/ ; Harvest Management Software: https://www.croptracker.com/product/harvest-management-software.html ; Harvest Estimates: https://www.croptracker.com/product/farm-management-software/harvest-estimates.html ; Harvest Crop Yield Records: https://www.croptracker.com/product/farm-management-software/harvest-crop-yield-records.html
- Hectre — https://hectre.com/ ; Harvest: https://hectre.com/products/farm-management-software/harvest-management/
- Fieldin — https://fieldin.com/
- Farmbrite — https://www.farmbrite.com/ (module-packaging context)
- xFarm — https://www.xfarm.ag/ (module-packaging context)

> Sourcing limitation: vendor help centers and operational manuals were not reachable in this research pass; evidence is official product/marketing-page level. Operational mechanics (record schemas, workflow states, permission models, numeric limits, pricing) are stated only at the level those pages support, and precise vendor-specific figures are intentionally omitted from this document. Several category-adjacent vendors (wine-grape harvest tracking, European orchard apps) were unreachable after repeated attempts and were excluded rather than filled from memory. Productivity and accuracy claims found on vendor pages are recorded only in the paired Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison, and the historical / market-sample breadth check are recorded in the paired Research Notes.
