# Swine Management

## Overview

A **Swine Management** application is the swine producer's production system of record and daily management console: it holds the pigs being produced as persistent records — individually identified breeding animals with their reproductive histories, and batch groups for the growing herd — documents the production cycle as it happens in the system's own event vocabulary, and converts the accumulated records into the performance picture and daily work lists that keep a pig operation running: which sows to serve, scan, treat, wean or cull, and which batches to feed, check or market.

Its defining structure is small:

```text
Swine production population (records at phase-matched granularity)
├── breeding herd: individually identified sows/boars with cycle histories
└── growing herd: batch groups (counts, placed into rooms/barns/sites)
    └── Dated event stream in the swine production-cycle vocabulary
        (breeding side: service → scan → farrow/litter → foster → wean → re-serve/cull
         growing side: placement → weights/feed/health/mortality → sale)
        └── Records → performance → decisions loop
            (farrowing rate, litter output, pigs-weaned measures, growth, FCR,
             mortality · benchmarks · action lists, alerts → act)
```

Everything else commonly associated with modern products — electronic sow feeding stations, RFID and ear-tag readers, mobile apps with offline capture, cloud deployment, industry benchmarking programs, packer and carcass data feeds, forecasting and traceability modules — is widespread in today's market but is not what makes the software swine management. A paper sow record card, a breeding board, a batch treatment sheet, and a hand-computed annual summary per sow satisfy the same core.

The Type is the hybrid member of the livestock family. Its siblings hold different shapes: Livestock Management holds long-lived breeding herds as individuals or mobs; Dairy Farm Management holds individually identified animals around the lactation/milking cycle; Poultry Farm Management holds batch flocks at population level. Swine spans two of those shapes at once — the breeding herd is managed as individuals around a recorded cycle, while growing pigs move as batches — unified by the swine cycle vocabulary and the weaned-batch handover between the two halves.

## Users & Context

Primary users are the people who run pig production:

- **sow-farm manager / herdsman** — owns the breeding-herd records; records services, pregnancy checks, farrowings and weanings as they happen; works from action lists of animals due
- **stockpeople / barn staff** — capture events in the barn (mortality, treatments, weights, transfers), often on a mobile device that works without internet
- **farm / production manager** — monitors performance across rooms, barns and sites, sets targets, responds to alerts and deviations
- **grower / finisher operator** — receives weaned batches, records growth, feed and mortality, markets the batch

Secondary users:

- **service technicians** in integrated operations — record events at contracted sites against the same central record
- **production coordinators and company management** — roll results up across many farms, compare sites, manage the flow of pigs between them
- **veterinarians, nutritionists and consultants** — given access to records and performance reports; some products offer dedicated consultant views across all their client farms
- **breeding-company and slaughterhouse/packer partners** — exchange data at the edges (genetics in, carcass results out)

The work environment is the barn as much as the office. Daily routine revolves around the animals' state: sows due for service or scanning, sows farrowing, litters to foster and wean, batches to weigh and check. Office and mobile views serve the planning and analysis side: reviewing performance against targets, comparing farms and batches, planning the flow of pigs between sites.

## Core Model

### The Defining Core

Three structures, held together. Remove any one and the product stops being swine management:

- **The swine production population as persistent records at phase-matched granularity.** The system holds the pigs being produced as records whose granularity matches their production phase. The breeding herd — gilts, sows, boars — is held as individually identified animals (sow number, ear tag or electronic ID) that persist across reproductive cycles and accumulate a history: across the researched sample, every breeding-capable product centers on a per-animal record with the animal's full cycle history available at a click. The growing herd — weaners and finishers — is held as batch groups: counts with composition and location, placed into rooms, barns or sites, managed through their growth as one unit; individual identity for growing pigs exists in some products as an optional welfare/health layer, but the batch is the unit of production. The population persists across cycles and outlives any single event; what the system holds is not a head count but a set of records that carry their histories.
- **The dated event stream in the swine production-cycle vocabulary, bound to the phase-appropriate unit.** On the breeding side, events are recorded against the sow and her litter: service or insemination, pregnancy check/scan and its result, farrowing with the litter's outcome (born, losses), fostering onto or off a nursing sow, weaning, abortion, and exit (cull, death, sale) — the sequence that defines one reproductive cycle, repeated across parities. On the growing side, events are recorded against the batch: placement or receipt, weights and growth, feed, health and treatments, mortality, sales and movements. Both sides share the inventory transactions — purchases, sales, deaths — and the transfers that move pigs between rooms, barns and sites. Every event is dated and attributed. This vocabulary is what turns a list of animals into a history of the operation.
- **The records → performance → decisions loop.** The accumulated records are continuously converted into production measures — farrowing rate, repeat rate, litter size, pre-weaning mortality and pigs-weaned measures on the breeding side; growth, feed conversion and mortality on the growing side — and compared against targets, the farm's own history, other farms, or industry benchmarks. Deviations surface as alerts; the records also drive the daily work directly as action lists (services due, farrowings due, weanings due) and problem-animal lists. The loop closes when the resulting decisions — serve, treat, foster, wean, cull, adjust feed, market — are recorded back as events.

### Capabilities Mature Products Add

These are standard in the market and expected by users, but they are layers on the core, not the definition:

- **In-barn mobile capture** — phone/tablet entry with offline recording, entry validation, scanning of ear tags (RFID/EID), barcodes and QR codes, and call-up of an animal's history on the spot.
- **KPI dashboards and targets** — configurable goal-setting with the farm's own targets visible in graphs; real-time deviation detection.
- **Medicine machinery** — treatment recording, planned medications, prescriptions, and withdrawal-relevant records shared with vets.
- **Feed recording** — consumption tracking, feed movements, and integration with scales and feeding systems for automatic intake data; feed conversion as a computed measure.
- **Inventory and stocktaking** — the counted population reconciled against recorded events; buying, selling and death registration as first-class entries.
- **Growth management** — weight recording, growing curves, comparison against standard curves and previous groups; automatic in-pen weighing in equipment-integrated products.
- **Multi-farm and multi-site roll-ups** — consolidated reporting across holdings; flows and business units as organizing filters; shipments between farms reflected in planning.
- **Benchmarking** — comparison against other farms and industry datasets, offered variously as built-in comparisons, opt-in quarterly/annual programs, or ranking communities.
- **External data exchange** — breeding/genetics companies, slaughterhouses and packers, feed suppliers, accounting and BI systems; open APIs.
- **Equipment integration** — electronic sow feeding stations, readers, climate and feeding controllers feeding data into the record automatically.
- **Planning and money layers** — forecasting, simulation and budgeting from historical data; cost reports, production accounting, and (in the deepest case) packer sales and carcass data joined to batch closeout.

### One Structure, Many Implementations

The core is written conceptually. Products realize it differently, and the differences are variants, not definitions:

```text
Concept:                  Unit of record — breeding side
Realizations:             sow card (sow number / tattoo / electronic ID), per-animal record
                          with full cycle history

Concept:                  Unit of record — growing side
Realizations:             batch / group with count and location; group closeout;
                          pen-level feeding data rolled into the batch

Concept:                  Cycle events
Realizations:             service/serving, scan/pregnancy test, farrowing, abortion,
                          fostering/nursing sow, weaning, exit/cull — vocabulary
                          shared across products, labels differ

Concept:                  Data capture
Realizations:             manual office entry · offline mobile in the barn ·
                          electronic sow feeding and weighing stations ·
                          climate/feeding controllers

Concept:                  Records → decisions
Realizations:             action lists and worklists · dashboards with targets ·
                          alerts and problem-animal lists · benchmark reports
                          (own farm / other farms / industry)
```

A reader who has only seen one style — say, a cloud platform with ESF-fed sow records — should still be able to recognize a client-hosted record program with quarterly benchmark submissions, or a paper sow-card system, as the same Type.

## How It Works

### Run the breeding cycle

The reproductive cycle is the rhythm the sow-side record stream follows:

```text
Gilt enters the herd (purchase or home-reared; recorded as inventory)
→ service/insemination recorded against the sow (first cycle point)
→ pregnancy check/scan at the operation's chosen interval; result recorded
→ farrowing recorded with the litter outcome: born total/alive, losses
→ fostering recorded: piglets moved onto or off the nursing sow
→ lactation runs; piglet events recorded (treatments, losses, numbering)
→ weaning recorded: litter closed, sow exits the cycle
→ sow re-served … or culled and replaced (exit recorded)
```

The sow's card accumulates this cycle after cycle; the system can always answer where each sow stands in her cycle, which sows are due for what, and how each parity and each boar/semen source performed. Action lists are generated from the due state of the cycle; scanning, farrowing and weaning work is organized from them, and entry validation keeps the recorded sequence consistent with it.

### Run the growing batch

The growing side follows the batch from arrival to sale:

```text
Weaners placed / batch received (from the sow farm or purchased)
→ recorded as a batch with count, source and location
→ daily/weekly routine: mortality recorded, weights sampled or automatic,
  feed consumption recorded or collected from feeding systems
→ treatments and health events recorded against the batch
→ growth tracked against curve and previous groups
→ marketing: batches sold in loads; movements and sales recorded
→ (where supported) closeout: batch performance and costs resolved
  against the received sales/packer data
```

In multi-site systems the handover is explicit: the weaned batch leaving the sow farm becomes the batch received at the nursery or finisher, with the transfer recorded on both ends and shipments between farms reflected in planning.

### Convert records into decisions

```text
Open the dashboard: today's status across rooms, barns, sites
→ review performance: farrowing rate, litter output, pigs-weaned measures,
  growth, feed conversion, mortality — against targets and benchmarks
→ work the lists: sows due to serve/scan/wean; sows with problems;
  batches deviating from curve or intake
→ act: serve, treat, foster, adjust, cull, market
→ the act is recorded as events — the loop closes
```

### Core vs Common vs Optional

**Defining core** — without these, not swine management:

- swine production population as persistent records (individuals for the breeding herd, batches for the growing herd)
- dated event stream in the swine production-cycle vocabulary bound to those units
- records → performance → decisions loop (measures, targets/benchmarks, action lists/alerts)

**Standard capabilities** — present in most modern products:

- in-barn mobile capture with offline mode and validation
- sow card / animal card as the per-animal record surface
- action lists and worklists; KPI dashboards with targets
- medicine recording (usage, planned, prescriptions)
- feed consumption tracking; weight recording and growth curves
- inventory/stocktaking; buy/sell/death registration; transfers and relocations
- multi-farm roll-ups; benchmark comparisons; external partner exchange
- role-based access; report libraries with export

**Variant / optional** — depends on production system, region, scale, packaging:

- phase coverage of the product (sow-only, grower-only, full-cycle)
- production-system shape (single-site farrow-to-finish vs multi-site flow vs contract growing)
- batch formalism depth; individual identity for growing pigs (welfare/health layer)
- breeding & multiplication and boar-semen management modules
- equipment-ecosystem depth (vendor's own feeding/weighing/welfare hardware)
- regional ID and traceability regimes; welfare-machinery contexts
- whole-farm suite embedding; chain modules beyond the farm gate
- money depth (cost reports → budgeting → closeout with packer data)

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Herd overview / dashboard

The primary entry surface for managers.

- current state of the herd: counts by phase and location, KPIs against targets, deviations and alerts
- primary actions: drill into a room, batch or animal; check alerts; open reports

### Sow card / animal record

The record of one breeding animal.

- identity (number, tag), cycle status, parity, and the full dated event history — services, scans, farrowings, litter outcomes, weanings, treatments, movements
- primary actions: record a cycle event, view history, transfer, exit the animal

### Batch / pen overview

The record of one growing batch.

- placement details (count, source, age), current count, growth against curve, feed and mortality to date
- primary actions: record events (mortality, weights, feed, treatments), view the batch's history, plan or record marketing

### Event entry surfaces

The capture forms for the record vocabulary, optimized for the barn: service, scan result, farrowing, fostering, weaning, transfer, death, sale, purchase, treatment, weight. On mobile they are built for a few taps per animal with scanning and offline storage; equipment-integrated products collect much of this automatically and surface it for confirmation.

### Action lists / worklists

The daily-work surface derived from the records: animals due for service, scanning or weaning; animals with problems; batches needing attention; missed entries flagged. Users can typically build their own lists with filters and sorting.

### Performance and benchmark reports

The decision surface.

- production summaries (services, farrowings, piglet losses, weanings, inventory), trend analyses, fertility and parity reports, growth and feed-conversion reports, cost reports
- comparisons: this period vs previous, this farm vs other farms or an industry database, actual vs target
- primary actions: run, filter, compare, export, share with vets/consultants

### Settings / administration

Site, barn and room structure; user roles and per-user permissions; target/KPI configuration; integrations (feeding systems, readers, controllers, partner data); language and audit settings.

## Important Rules / Behaviors

### The cycle events must follow in order

A sow's cycle is a state machine as much as a history: services precede pregnancy checks, checks precede farrowings, farrowings open a lactation that weaning closes. Products organize entry, validation and action lists around this order — an animal's current cycle point drives what work is due and how entry is organized. Repeat services and abortions are recorded as cycle outcomes in their own right, because they drive the decisions (re-serve or cull).

### The litter is the pivot between the two halves

Farrowing creates the litter record; fostering moves piglets between litters while keeping their origin traceable; weaning closes the litter and creates the batch that flows on. Litter outcome — born, losses, weaned — is the unit through which breeding performance is measured and through which the growing population comes into existence.

### Every pig is accounted for

The counted population must reconcile against the recorded events: placements, births, transfers in, and purchases on one side; deaths, sales, transfers out, and culls on the other. Stocktaking against the event record is a standard surface; unexplained variance is a data-quality problem to fix, which is why entry validation and audit features are common.

### Batch integrity carries the growing phase's economics

Growth, feed conversion, mortality and closeout are all computed per batch; commingling and splitting must be recorded as batch events or the economics become unverifiable. The batch's source (which sow farm, which week) stays attached to it, because health and performance follow it.

### Identity integrity is guarded

The record system is only as good as the match between the physical animal and its record. Tag loss, re-tagging, and misidentification are handled as explicit events; equipment integrations (readers, ESF stations) exist substantially to enforce the identity match at the moment of capture.

### Medicine records carry obligations

Treatments are recorded with animal, batch, product and date because withdrawal and audit requirements make them a compliance surface as well as a health record; planned medications and prescriptions are common because dosing regimes shape the work.

### Performance is measured against benchmarks, not raw numbers

Farrowing rate, litter output and pigs-weaned measures, growth and feed conversion are read against targets, previous periods, other farms and industry datasets. The comparison — not the raw figure — is what drives decisions; this is why benchmarking programs and cross-farm comparisons are a structural layer of the category, not a marketing extra.

## Variants

- **Sow-farm record products** — the breeding cycle at the center: services through weaning, parity and fertility analysis, gilt management; historically the heart of the category.
- **Grower/finisher products** — the batch at the center: placement to sale, growth and feed conversion, mortality, closeout; strong in contract-growing and multi-site settings.
- **Full-cycle platforms** — one record spine from gilt entry to sold finished pig, with the weaned-batch handover and site flow managed inside the same system.
- **Integrated-company platforms** — multi-farm roll-ups, flow and business-unit filters, service-technician capture at contracted sites, packer/sales data joined to batch closeout; management and coordination as primary users.
- **Equipment-ecosystem products** — the management layer arriving with the barn build: feeding, weighing, climate and welfare installations operated through a control system that stores the performance history.
- **Breeding & multiplication products** — genetic-pyramid management: multiplication levels, boar and semen records, genetics-company data exchange.
- **Data-specialist and benchmarking products** — record keeping plus opt-in industry benchmarking and percentile comparison as the differentiating service.
- **Whole-farm suites with a swine module** — diversified small farms managing pigs beside crops and accounting; the swine core carried with less depth.
- **Regional editions** — markets where national identification, traceability schemes, or welfare regulation shape the record set and exports.

A variant stays a variant unless it changes the core: hold long-lived animals without the litter-and-cycle machinery and the product is generic livestock management; put the ration and feed supply at the center and it becomes feed management; add the whole-operation scope (land, crops, money, work) and it becomes a farm management platform.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Livestock Management | sibling (seam = production-system shape) | long-lived breeding herds as individuals or mobs with open-ended event histories; swine adds the cycle-and-litter machinery plus the batch growing flow — swine is the hybrid case |
| Poultry Farm Management | sibling (meets at the weaned-batch interface) | batch flocks at population level with placement-to-clearance cycles vs swine's individually identified breeding herd with cycle records; the growing halves are structurally parallel |
| Dairy Farm Management | sibling (both individual + cycle) | lactation/milking cycle with daily milk per lactation vs gestation/farrowing cycle with litter outcome and weaning; the cycle vocabulary is the discriminator |
| Feed Management | interlocking discipline | ration formulation and feed supply are the subject there; feed consumption, deliveries and conversion are recorded here as a layer |
| Farm Management Platform | superset | whole-operation scope (land + crops + livestock + money + work); remove the whole-operation scope and the swine slice is this Type |
| Agribusiness ERP | adjacent | commercial/commodity flow and ledgers at the center; swine closeout economics and cost reports sit at the seam but read as production-side layers |
| Agricultural IoT Platform | adjacent | manages the connected device fleet as its packaged outcome; here ESF stations, readers and controllers are capture hardware bound to animals and batches |
| Research Animal Facility Management | structurally distant | research-governance context (protocols, strains, per-diem billing) vs production-economics context |
| Veterinary practice management | adjacent profession | clinic-side system of record; vets are collaborators and data consumers on the farm's records here |

The most consequential boundary is with **Livestock Management**, because both hold "animals + events + records → decisions". The structural test is the production machinery at the center: if the managed subject is a long-lived herd with open-ended events, it is Livestock Management; if the center is the swine reproductive cycle with litter recording plus the batch growing flow — as it is in every product researched here — it is this Type. Species lists are the wrong test: multi-species products can manage pigs without carrying this Type's core.

## Representative Products

- **PigCHAMP** — long-established swine record keeping (sow/reproductive records, 40+ report types, action lists) plus opt-in industry benchmarking; US heritage, global reach
- **AgroVision (PigVision / PigExpert)** — herd management for sow and grower farms; physical and financial performance, weekly monitors, quarterly benchmarks, consultant views; NL/EU
- **Cloudfarms** — cloud pig-production suite with separate Sow Management and Wean-to-Finish services, mobile-first barn capture, ESF and genetics-company integrations; EU with international reach
- **MetaFarms** — US integrated-production platform (SOW / FINISH / SALES): group tracking and closeout, roll-up reporting across flows and business units, packer and ESF integrations
- **Agrisys** — equipment-integrated management (control system over feeding, weighing and welfare installations; batch and herd comparisons); Danish, successor to the Nedap pig-management lineage

The definition was checked against all five across the breeding-record, growing-batch, equipment-integrated and integrated-company poles, and against the paper-era lineage (sow record card + breeding board + batch treatment sheet + hand-computed annual summary).

## Sources

Research date: **2026-09-10**

- PigCHAMP — official site and product pages: https://www.pigchamp.com/ , https://www.pigchamp.com/benchmarking , https://www.pigchamp.com/products/reproductive/reports
- AgroVision — PigVision product page and pigs solution pages: https://agrovision.com/uk/software/pigs/pigvision/ , https://agrovision.com/uk/software/pigs/ , https://agrovision.com/pigexpert/
- Cloudfarms — product site and service pages: https://en.cloudfarms.com/ , https://en.cloudfarms.com/services/sow-management/ , https://en.cloudfarms.com/services/wean-to-finish-management/
- MetaFarms — solutions and product pages: https://www.metafarms.com/solutions.html , https://www.metafarms.com/sow.html , https://www.metafarms.com/finish.html , https://www.metafarms.com/sales.html
- Agrisys — product site and control-system pages: https://en.agrisys.dk/ , https://en.agrisys.dk/en/agrisys-control-system-dk , https://en.agrisys.dk/en/autopig-dk ; Nedap pigs-division succession note: https://nedap-livestockmanagement.com/pig-farming-activities/

> Sourcing limitations: PigCHAMP and MetaFarms official pages could not be fetched directly from the research environment (timeouts / 403); their claims are taken from search-index copies of those pages and kept at the level of listed features. Agrisys was reached at positioning and control-system level; its per-animal record depth is kept at inference strength. Direct fetches of PigCHAMP (×2) and Agritec Porcitec (×2, candidate dropped) failed and were not filled from memory. Precise numeric limits, KPI values and time windows are intentionally not stated in this document; detailed product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
