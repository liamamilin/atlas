# Aquaculture Management

## Overview

An **Aquaculture Management** application is farm-operated production software for raising aquatic organisms — finfish, shrimp, and related farmed species. It models the farm's water-based production units (ponds, tanks, raceways, sea cages), tracks the living stock held in those units across bounded production cycles, records the ongoing rearing activity (feeding, water condition, losses, treatments, growth), and accounts for each cycle from stocking through to harvest.

The defining core is small:

```text
Production unit (pond · tank · raceway · cage · line)
└── Stock population living in the unit across a production cycle
    ├── Rearing records (feeding · water condition · mortality · treatments · growth)
    └── Standing stock: count / biomass evolving across the cycle
        └── Harvest (partial or total) closes the cycle
```

Everything else commonly associated with the category — sensor networks, automated feeders, computer-vision biomass estimation, financial modules, regulatory reporting, broodstock-level traceability — is widely present in mature products but is not what makes the software aquaculture management. A recording tool operated entirely by hand still qualifies; a sensor dashboard with no production-unit, stock, or cycle accounting does not.

When the software instead manages wild-capture stocks, vessels, quotas, and landings, it belongs to Fisheries Management, a neighboring Type. When it manages terrestrial animals, it belongs to Livestock Management.

## Users & Context

Primary users are the people who run an aquaculture farm:

- **Farm / site managers** — oversee ponds, tanks, or cage sites; watch cycle progress, water conditions, stock status, and alerts; decide on feeding adjustments, treatments, and harvest timing.
- **Farm workers / technicians** — perform and record daily work at the water's edge: measuring water parameters, feeding, checking stock, recording mortality and treatments. In shrimp farming this recording typically happens pond-side on a phone; in sea-cage farming, on site or from feed barges and control rooms.
- **Production / biology roles** — track growth performance, stock health, and loss rates; compare cycles; plan stocking and harvest schedules.

Secondary users include **owners and company management** — particularly in multi-site companies, where production performance and cost are reviewed across farms — and, in enterprise deployments, **finance and compliance staff** who consume the production record for costing and reporting.

The work context is distinctive: production is dispersed over water (pond clusters, sea sites), animals are held in water whose condition must be watched, cycles run from a few months (shrimp) to a year or more (larger finfish), and much of the recording happens in field conditions rather than at a desk. This drives the category's characteristic dual surfaces: a field-side recording app and an office-side dashboard.

## Core Model

### The Defining Core

Four structures. Remove any one and the software stops being recognizable as aquaculture management:

- **Production units** — the farm's water-based production containers, each held as an identified managed record with its own identity, capacity, and state. A shrimp farm's ponds, a hatchery's tanks, a cage farm's pens, a shellfish farm's longlines are all instances of the same idea: the unit is where stock lives and where work happens.
- **Stocked population per unit, across a production cycle** — aquatic stock is placed into a unit (stocking: post-larvae, juveniles, smolt, seed) and thereafter tracked as a **population**, not as individually identified animals. A production cycle is the bounded span from stocking to harvest during which one population occupies one unit.
- **Rearing records** — dated operational events and observations attached to the unit and its population during the cycle. The typical content: feeding, water condition, mortality, treatments, growth samples. Exactly which items matter varies by species — shrimp farming is dominated by water quality and feed; sea-cage finfish add health, welfare, and loss control; shellfish are not fed at all.
- **Cycle quantity accounting with harvest** — the system maintains the running account of the stock (count and/or biomass) as stocking input, growth, and losses accumulate, and records **harvest** — partial or total — as the production output that closes (or extends) the cycle.

The population convention matters: unlike dairy or beef systems built around individual animal identity, aquaculture normally manages groups per unit. Biomass is derived — counts combined with estimated average weight — rather than registered animal by animal.

### Standard Capabilities in Mature Products

These capabilities appear across the researched products and make the software practical, but they do not define the Type:

- **Water-quality monitoring** — manual entry of measured parameters, automated feeds from probes and handheld instruments, or both. Near-universal, because water condition is the animal's living environment and a primary risk factor.
- **Feeding management** — recording feed quantities and types for fed species, tracking feed conversion, and, in more automated deployments, controlling feeders. Absent for unfed species (shellfish).
- **Mortality and loss recording** — recording deaths and removals, updating standing stock.
- **Growth and biomass estimation** — manual sampling, device-based counting and weighing, or camera/sonar estimation; typically paired with yield and harvest forecasting.
- **Sensor and equipment integration** — oxygen and temperature probes, feeders, aerators, cameras, and power monitoring feeding data into the same unit-and-cycle model.
- **Field-side mobile recording** — quick daily logs at the pond or site, often usable offline, synced to the office view.
- **Dashboards, alerts, and trends** — current conditions per unit, threshold alerts, historical charts and cycle-over-cycle comparison.
- **Roles and access control** — owners, managers, and technicians with differentiated views and permissions.
- **Reports** — cultivation/production reports per unit and cycle, sometimes financial reports.

### One Structure, Many Implementations

The core model is conceptual; products implement it differently:

```text
Concept:     Production unit
Implements:  shrimp pond, sea cage/pen, raceway, tank, longline/raft

Concept:     Stock population
Implements:  pond cycle batch, pen group of fish, shellfish lot on a line

Concept:     Rearing record
Implements:  manual daily log, sensor time series, feeder events,
             camera-derived size distributions, treatment logs

Concept:     Quantity accounting
Implements:  counted stock × estimated weight, sampling-based biomass,
             device-based counting, harvest weigh-in
```

## How It Works

### Set up the farm

```text
Register the farm
→ define its production units (each pond, tank, cage, or line)
→ record unit attributes (type, capacity, location)
→ optionally connect measurement devices
```

### Stock a unit and open a cycle

```text
Choose a unit
→ record a stocking event (species, life stage, origin, quantity)
→ the cycle opens: the population is now associated with the unit
→ expected performance and harvest plans may be recorded
```

### Run the daily rearing loop

```text
Observe the unit (water condition — measured or sensed)
→ feed the stock (record feed, or let controlled feeders operate)
→ check stock behavior / health; record anything unusual
→ record mortality and other events (treatments, grading, moves)
→ receive alerts when readings or equipment cross thresholds
```

This loop is the heart of the product. It repeats daily — or continuously where sensors stream data — for the length of the cycle.

### Track growth and standing stock

```text
Sample or measure the stock (manual sampling, device counting,
or camera/sonar estimation)
→ the system updates estimated average weight, count, and biomass
→ forecasts project yield and harvest timing from growth trends
```

### Harvest and close the cycle

```text
Schedule and perform harvest (partial removal or total)
→ record harvested quantity and destination
→ the cycle closes; its record becomes the basis for
   performance review (growth, feed conversion, losses, cost)
→ the unit is cleaned, rested, or restocked — the next cycle begins
```

### Review and plan

Across cycles, users compare performance between units, sites, and periods; enterprise products extend this into scenario planning, budgeting, and company-level production control, with costs and income attached to the biological record.

### Core vs Common vs Optional

**Defining core** — without these, not aquaculture management:

- production-unit register
- stocked population per unit across a production cycle
- rearing records attached to the unit/population
- standing-stock accounting with harvest as the cycle output

**Standard capabilities** — present in most modern products:

- water-quality monitoring (manual or sensor)
- feeding management and feed-conversion tracking (fed species)
- mortality recording
- growth/biomass estimation and harvest forecasting
- sensor/equipment integration
- field-side mobile recording
- dashboards, alerts, trends, cycle reports
- multi-user roles

**Variant / optional** — depends on segment, region, and scale:

- automated feeding and demand-based feeding control
- computer-vision biomass, welfare, and parasite monitoring
- financial management (costs, income, assets, budgets)
- regulatory/compliance reporting and broodstock-to-harvest traceability
- multi-site / company-level portfolio management
- bundled input supply, harvest services, financing, or market linkage

## Interfaces

### Farm / cycle dashboard

The office-side home surface.

- typical information: list of units with current status, cycle stage, latest water readings, standing-stock estimates, active alerts
- primary actions: open a unit or cycle, record or review events, compare cycles, configure alerts

### Unit record and event log

The record of one production unit and the population it holds.

- typical information: unit attributes, current cycle, chronological rearing records (water readings, feedings, mortality, treatments, growth samples), charts over time
- primary actions: record events, view trends, edit cycle details, plan harvest

### Mobile field recording

The pond-side / site-side surface.

- typical information: today's tasks and readings for the assigned unit(s)
- primary actions: quick daily logs (water measurements, feed given, activities, mortality), often offline-capable with later sync

### Feeding / monitoring console

The industrial-deployment surface, present where hardware is integrated.

- typical information: live sensor readings, feeder status, camera or sonar views, equipment alerts
- primary actions: start/stop or adjust feeding, acknowledge alarms, inspect live conditions

### Reports and analysis

- typical information: cycle reports (yield, feed use, losses, cost), cross-cycle and cross-unit comparisons, financial summaries where the product includes them
- primary actions: generate, filter, export

## Important Rules / Behaviors

### Cycles bound the accounting

Quantities and performance are accounted per unit per cycle. Stocking opens a cycle; harvest closes it. Performance metrics (growth, feed conversion, losses) are meaningful only within a cycle; cross-cycle comparison is a first-class activity.

### Population, not individual animals

Records attach to the unit's population. Individual identity is exceptional (for example broodstock contexts); the normal currency is count, average weight, and derived biomass.

### Mortality reduces standing stock

Deaths and removals are recorded as events that decrease the stock account; biomass estimates combine counts with average-weight estimates, so repeated loss events visibly erode projected yield.

### A unit typically holds one population per cycle

Typically one stocked population occupies a unit per cycle, with cleaning or rest periods between cycles in some segments. Partial harvests may thin the population without closing the cycle; total harvest closes it.

### Manual and automatic records coexist

Sensor-derived data streams in automatically where devices are connected; hand-entered logs remain essential elsewhere. Both are rearing records in the same model. Alerts fire from thresholds on device readings; manual entry correctness depends on the users.

### Feeding is species-dependent

Feeding management applies to fed species. Shellfish and similar farmed organisms are reared without feeding; their rearing records center on placement, condition, and harvest. A product's capability set follows the species it serves.

### Roles constrain the record

Technicians record; managers review and decide; owners and administrators see finances and configuration. Access control is a normal part of even small-farm products.

## Variants

- **Intensive shrimp ponds** — short cycles; water quality and power reliability as daily risks; smallholder-to-mid farms; mobile-first recording; automated feeders and aerator/power monitoring common in some regions.
- **Sea-cage finfish (salmon and similar)** — long cycles; feeding optimization, health and welfare monitoring, parasite management, escape prevention, and heavy regulatory reporting; hardware-dense sites; enterprise suites with biological and financial production control.
- **Land-based / recirculating systems (RAS)** — tanks in controlled facilities; water treatment parameters and equipment monitoring dominate; often part of turnkey facility technology.
- **Hatcheries and broodstock operations** — tanks and breeding populations; more individual-level and life-stage tracking; feeds the stocking stage of grow-out farms.
- **Shellfish farming** — lines, rafts, and racks instead of ponds; no feeding; placement, grading, and harvest dominate. Mainstream management products in the researched sample focus on finfish and shrimp; shellfish-specific coverage is comparatively rare, and how far general products serve it varies.
- **Scale tiers** — free/basic recording tools for small farms; subscription tiers adding finance, stock, and analysis; enterprise suites adding planning, traceability, and multi-site control.
- **Regulatory intensity** — regions with strict aquaculture regulation drive compliance reporting and traceability depth; unregulated or lightly regulated segments leave those capabilities absent without breaking the Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Fisheries Management | manages wild-capture stocks, vessels, quotas, and landings — not reared populations in owned production units; no stocking/feeding/harvest cycle |
| Livestock Management | structurally the closest cousin (populations, events, feed, health) but for terrestrial animals; no water-environment parameters, no aquatic unit taxonomy; livestock systems more often track individual animals or flocks rather than per-unit populations |
| Farm Management Platform | land parcels and crop cycles are the core objects; no ponds/cages or aquatic stock; a generic farm tool with fish records remains a farm platform unless the aquatic production model is primary |
| Feed Management | feed formulation and inventory for feed operations; in aquaculture software, feeding is an execution activity inside the rearing loop, not a formulation business |
| Agricultural IoT Platform | device connectivity and sensor data plumbing; aquaculture management binds that data to units, populations, and cycle accounting and adds production records |
| Food Traceability Platform | post-harvest chain custody; aquaculture traceability normally ends at harvest and first sale (enterprise suites may extend it upstream to broodstock) |
| Agribusiness ERP | financial and commodity back office; may integrate with aquaculture management but the production-unit/cycle model is not its center |
| Marine Fleet Management | manages workboats and vessel logistics serving cage sites — support logistics, not stock rearing |

The boundary that most often causes confusion is with Fisheries Management, because both concern "fish and water". The structural test is the object model: reared population in an owned production unit with a stocking→harvest cycle (Aquaculture Management) versus wild stock under capture management with quotas, effort, and landings (Fisheries Management).

## Representative Products

- **AKVA group — AKVA fishtalk suite** (Norway) — enterprise production control and planning for sea-cage and land-based finfish; biological and financial record-keeping with hardware integration
- **Aquabyte** (Norway) — camera-based weight, health, and feeding insight for salmon pens
- **AquaExchange** (India) — IoT-first shrimp-farm ecosystem combining monitoring devices with a farm management app
- **JALA App** (Indonesia) — mobile-first shrimp pond and cycle recording, monitoring, and forecasting

The model was checked across both major species segments (sea-cage finfish and pond shrimp), four product philosophies (integrated suites, vision-based data layers, IoT-first ecosystems, mobile-first recording), and different customer tiers (enterprise down to smallholder).

## Sources

Research date: **2026-09-06**

- AKVA group — Our digital solutions: https://www.akvagroup.com/digital/solutions/
- AKVA group — AKVA fishtalk: https://www.akvagroup.com/fishtalk/akva-fishtalk
- Aquabyte: https://aquabyte.ai/
- AquaExchange: https://aquaexchange.com/
- JALA — JALA App: https://jala.tech/app ; FAQ: https://jala.tech/faq ; App Basic FAQ: https://jala.tech/faq/jala-app

> Sourcing limitation: AKVA group's user manuals and product documentation are gated behind customer login, so detailed operational rules for its products could not be directly observed; statements about that product family are limited to its public product pages. Vendor-reported scale figures were treated as marketing claims and excluded from the general description. Shellfish coverage claims are analytic inferences flagged in the paired Research Notes rather than observed product behavior.

Detailed product-by-product observations, the cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
