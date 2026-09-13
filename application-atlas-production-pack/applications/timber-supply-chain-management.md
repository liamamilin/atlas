# Timber Supply Chain Management

## Overview

A **Timber Supply Chain Management** application manages the flow of wood fiber from the forest to the mill. It holds a wood-flow plan that allocates fiber supply — harvest output and purchased wood — to demand: mill intake needs and buyer contracts. It executes that flow through loads: each load is captured once as a shared record (species, grade, volume, origin, destination, time), hauled under dispatch, verified at the scale, and checked against contract terms. And it keeps a running picture of wood held at every point of the chain — roadside, on the road, in the yard, at the mill — so supply and consumption stay balanced.

The defining core is small:

```text
Wood-flow allocation plan
└── loads / deliveries (the chain's shared transactional records)
    └── chain inventory picture (roadside → rolling → yard → mill)
```

Everything else commonly associated with modern wood-supply software — digital transport certificates, weighbridge automation, optimization modeling, certification traceability, GPS tracking — is widespread in current products but is not what makes the product a timber supply chain management system. The paper-era wood flow (an allocation board, phone-and-radio dispatch, handwritten delivery and scale tickets, a wood-yard ledger, contract books) satisfies the same definition without any of it.

When the center of gravity shifts to running the harvest job itself — crews, machines, production, contractor pay — the product is a Logging Operations Management system. When it shifts to holding the forest estate — ownership, standing inventory, the multi-year program — it is Forestry Management. When it only reports prices and benchmarks *about* the wood market, it is market intelligence, not supply chain management.

## Users & Context

Primary users:

- **fiber supply / wood-supply manager** (at a mill or forest owner's supply organization) — keeps the mill fed: watches what is loaded, what is rolling, and what is arriving; forecasts intake against production needs; reroutes loads when conditions change
- **timber marketing / procurement manager** — matches fiber supply to contracts and delivery commitments; decides which volumes go to which buyers; tracks what was delivered against each contract
- **transport / logistics manager and dispatchers** — schedule and dispatch trucks against roadside inventory, build delivery schedules, and adjust when weather, road bans, or mill shutdowns hit

Secondary users:

- **haulers / truck drivers** — receive assignments and plan updates digitally, capture delivery information at the load point and the scale
- **mill receiving / scale operators** — weigh loads in, verify arrivals, and complete delivery records
- **forest owners and contractors** — parties to the same delivery record, each seeing their own slice
- **executives / planners** — consume supply-pipeline and delivery-performance views

The work context shapes the software: wood moves across long distances between remote harvest sites and mills, through many independent organizations (forest owner, contractor, hauler, mill), in weather and on roads that fail. Loads are money — every delivery settles against a contract. Products are therefore built around shared multiparty records, capture that tolerates disconnection, and scale-grade evidence rather than desk-bound data entry.

## Core Model

### The Defining Core

**The wood-flow allocation plan.** The unit of planning work is the allocation of wood volumes to destinations over time. Supply comes from harvest units (planned and actual output, by species and product) and from purchased wood; demand comes from mill consumption needs and buyer contracts. The allocation plan is what turns "the forest produced (or will produce) this much wood" into "this wood goes to this mill, this week." Mature products support this with supply forecasting from harvest plans and, at the planning pole, optimization modeling that balances harvest scheduling, road capacity, and wood flow against delivered cost.

**The load/delivery record.** The unit of execution is the load. Each load is captured once — species, grade, volume or weight, origin, destination, timestamps — and that single record travels with the load through its life: built at the load point, hauled under dispatch, weighed at the scale, received at the mill. The record is deliberately multiparty: the forest owner sees what left their land, the hauler sees what they delivered, the mill sees what arrived — the same record, not competing copies. It is the artifact against which deliveries are verified, disputes are resolved, and contracts are fulfilled.

**The chain inventory picture.** Wood is held as flowing stock at the chain's nodes: roadside inventory at landings and sort yards, loads in transit, yard and mill inventory at the destination. The picture updates continuously from load capture and scale data. It is what lets a supply manager see "what's roadside, what's rolling, and what's scheduled to arrive" and forecast mill intake before it falls short — the balancing act that gives the Type its name.

All three are jointly load-bearing:

- allocation plan alone → a spreadsheet exercise or an S&OP report
- load records alone → load slips and e-dockets with nothing organizing them into a flow
- inventory picture alone → stock counters with no flow to manage
- plan + records without the inventory picture → allocation and deliveries with no stock position, no pipeline to balance
- plan + inventory without records → a planned flow nobody executes
- records + inventory without the plan → loads moving with no allocation logic — dispatch and ticketing, not supply chain management

### Capabilities Shared by Mature Products

A typical modern product carries most of these. They make the Type practical; they do not define it.

- **Transport scheduling and dispatch** — assigning transport fleets against roadside inventory, building delivery schedules from harvest unit to mill, and pushing plan updates digitally to trucks instead of by phone.
- **Weighbridge / scale integration** — automated weight capture at truck scales and mill sites, recorded directly to the load record; load verification and faster scale throughput.
- **Delivery-versus-plan visibility** — every truck, load, and arrival compared against the plan, with exceptions and ETAs surfaced in real time.
- **Supply-pipeline forecasting** — projecting what will arrive at the mill from what is roadside, rolling, and scheduled, so production can plan intake instead of guessing.
- **Contract compliance checking** — deliveries confirmed against contract terms (product specs, quantity, certification status, delivery dates), with mismatches flagged before they become delivery problems.
- **Chain-of-custody traceability** — the unbroken record of who held each load and when, with timestamps, locations, and signatures at each handoff; certification status (scheme-tagged loads) carried on the same record for buyer audits and regulatory regimes.
- **Multiparty role-based visibility** — each party (forest owner, hauler, mill) sees the slice of the shared record it needs.
- **Disruption response** — rerouting loads and resetting schedules from one connected view when weather, road closures, or mill shutdowns hit.
- **Truck utilization coordination** — fleet scheduling across the network to reduce empty runs and turnaround time.
- **Offline field capture** — delivery capture that works without coverage and syncs when connectivity returns; fleet devices, RFID, or hybrid paper-to-digital capture where smartphones do not fit.
- **Mill/yard inventory planning** — production inventory, purchases, disposals, transfers, and usage tracked at mill and yard level.
- **Wood-flow optimization modeling** — at the planning pole: harvest, road, and wood-flow scenarios balanced against delivered wood cost.
- **Systems integration** — delivery records connected to mill intake systems, ERPs, and log-accounting systems.

### One Structure, Many Implementations

```text
Concept:   the wood-flow allocation plan
Realized as:  allocation boards and allocation-planning modules, supply forecasts
              from harvest plans, optimization-modeled wood-flow scenarios

Concept:   the load/delivery record
Realized as:  handwritten delivery and scale tickets, digital load slips,
              electronic transport certificates / e-dockets, weighbridge-fed records

Concept:   the chain inventory picture
Realized as:  wood-yard ledgers, roadside-inventory views, supply-pipeline
              dashboards, mill/yard inventory modules
```

A reader who has only seen one realization — for example a digital transport-certificate platform — should still be able to recognize a phone-dispatch, paper-ticket wood room as running the same Type.

## How It Works

### The wood-flow cycle

```text
Forecast supply from harvest plans and purchases
→ allocate volumes to destinations (mills, yards, buyers) against contracts and mill needs
→ schedule transport against roadside inventory
→ dispatch trucks; loads built at the landing, each load recorded once
→ haul; plan updates reach the truck digitally
→ weigh in and receive; the scale completes the delivery record
→ balance the pipeline: what's roadside, rolling, arriving vs what production needs
→ check deliveries against contract terms; resolve discrepancies from the shared record
```

The cycle is continuous: harvest output changes with weather and machines, mill needs change with production, roads and markets interrupt — so allocation, schedules, and routes are revised constantly, and every revision propagates through the loads already moving.

### Allocating the wood

Supply planners work from harvest plans and real-time output ("what is actually on the ground") and allocate volumes to destinations — at the level of harvest units, products, or loads — balancing buyer specifications, contract commitments, mill consumption needs, and margin. At the optimization pole, the product models scenarios (which loads to which buyers, which harvest sequence) and shows trade-offs before volume is committed.

### Scheduling and dispatching transport

Transport capacity is assigned against roadside inventory to create delivery schedules from unit to mill. Dispatch then runs the day: assignments and plan updates go to trucks digitally; when a road washes out or a mill stops, loads are rerouted and schedules reset from one connected view rather than by phone.

### Recording the delivery

The load record is created once, at the load point, and follows the load: species, grade, volume or weight, origin, destination, timestamps, and confirmations. At the scale, weight data is captured automatically into the record; at the mill gate, receipt completes it. Because every party references the same record from the moment of creation, reconciliation is fast and disputes have a shared factual basis. Mature products enforce rules on the record itself — loads picked up from the correct location and delivered to the right customer.

### Balancing the pipeline

The supply pipeline — what is roadside, what is rolling, what is scheduled to arrive — is compared continuously against mill consumption needs. This is the fiber supply manager's core act: seeing intake shortfalls before they happen, and adjusting allocation, schedules, or harvest output while there is still time.

### Fulfilling contracts

Deliveries are tracked against the contracts they serve: product specs, quantities, certification status, and delivery dates checked as wood moves, with mismatches flagged early. What was delivered against each contract is readable directly from the delivery records — the basis for settlement, buyer reporting, and audit.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Allocation / wood-flow workspace

Where supply is matched to demand.

- typical information: harvest output by species/product, purchased wood, mill consumption needs, contract commitments, allocations by destination and period
- primary actions: allocate volumes to destinations, model scenarios, adjust allocations when supply or demand shifts

### Transport schedule / dispatch board

Where the day's movement is organized.

- typical information: roadside inventory, trucks and fleets, delivery schedules, load status, exceptions
- primary actions: assign trucks to loads, build and revise delivery schedules, reroute, push updates to drivers

### Driver / hauler surface

What travels with the truck.

- typical information: current assignment, origin and destination, load details, plan changes
- primary actions: confirm pickup, record delivery information at the load point and scale, work offline and sync

### Scale / receiving surface

Where loads become verified deliveries.

- typical information: inbound loads, expected vs arriving, weighbridge data, delivery confirmations
- primary actions: weigh in, verify against the record, complete the delivery, flag discrepancies

### Delivery records view

The chain's shared ledger.

- typical information: each load's species, grade, volume, origin, route, timestamps, custody handoffs, contract linkage
- primary actions: inspect a load's history, resolve discrepancies, export evidence for settlement or audit

### Pipeline / intake dashboard

The mill-supply view.

- typical information: roadside, rolling, and scheduled arrivals by species/grade; intake vs production needs; delivery-vs-plan performance
- primary actions: forecast intake, drill into shortfalls, trigger reallocation

## Important Rules / Behaviors

### The load record is created once and shared

The record of each load is captured at the point of loading and then referenced — not re-created — by every party. Role-based access gives each party its slice; the record itself is treated as money-grade evidence, designed to be tamper-resistant, because payments, disputes, and audits all draw on it.

### Loads bind to their allocation

Mature products enforce that loads are picked up from the correct location and delivered to the right customer — the allocation plan is not just a view but a constraint on execution.

### Deliveries are checked against contracts in motion

Contract terms (specs, quantity, certification, dates) are evaluated against deliveries as wood moves, with mismatches flagged before they become delivery problems — not discovered at month-end.

### Chain of custody rides the record

In mature products, custody handoffs (loading site, truck, scale, mill) are recorded with time, location, and signature, and certification status travels on the same record — traceability evidence becomes a by-product of execution rather than a separate documentation exercise. The depth of this machinery varies by product and by the certification and regulatory regimes a deployment serves.

### The pipeline is the early-warning system

Because the inventory picture updates from every load and weigh-in, intake shortfalls surface before the mill runs short. The comparison of supply pipeline against production needs is continuous, not a weekly review.

### The field tolerates disconnection

Wood moves beyond reliable coverage. Capture continues offline and syncs when connectivity returns; some deployments add fleet devices, RFID, or hybrid paper-to-digital capture at the scale. The exact mechanisms vary by product.

### Plan changes ripple

A mill shutdown, road ban, or weather event forces rerouting and rescheduling; because loads, schedules, and allocations hang off one flow, changes propagate through all of them from one connected view.

## Variants

- **Who leads the deployment** — forest-owner organizations managing flow off their estates; mills and procurement organizations managing inbound fiber; integrated forest-products companies running the whole chain from harvest to mill gate.
- **Planning depth** — manual allocation against spreadsheets and boards at one pole; optimization-modeled wood flow (harvest, roads, delivered cost) at the other.
- **Commercial depth** — delivery-against-contract visibility as the base; contract portfolios, pricing, and market-data integration as extensions (market-intelligence platforms are a separate product category).
- **Regional haulage regimes** — jurisdictions with transport-certificate requirements, certified weighbridge processes, and regulatory traceability regimes shape how strictly deliveries must be documented.
- **Packaging** — standalone logistics products; supply-chain lines inside wider forestry suites (alongside estate, operations, and mill products); wood-procurement ERP modules.
- **Harvest-method context** — cut-to-length operations feed the flow with machine-reported production; tree-length operations feed it with load slips; the flow structures hold across both.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Logging Operations Management | upstream sibling (most important boundary) | runs the harvest job — operation, crews, machines, production, contractor settlement; the load there is the job's production-and-pay artifact, here it is the chain's transaction (allocated, dispatched, delivered against contracts) |
| Forestry Management | upstream sibling | holds the forest estate of record — units, standing inventory, multi-year program; the wood-flow plan consumes its harvest plans and forecasts |
| Transportation Management System | generic cousin | manages shipments, carriers, and rates for any freight; no wood semantics (species/grade volumes, roadside inventory, harvest-plan coupling, scale tickets, chain of custody) |
| Supply Chain Planning Platform | generic cousin | plans demand/supply/inventory for manufacturing and retail; the wood-domain realization adds harvest-coupled supply and scale-ticket settlement |
| Freight Brokerage / Load Board | adjacent | matches loads to carriers; does not hold the chain-wide flow, allocation, or inventory picture |
| Timber Market Intelligence | data pole | prices, benchmarks, forecasts, and trade flows *about* the wood market; no flow machinery of its own |
| Grain Origination Platform | agricultural parallel | similar commodity-flow shape (contracts → flow → settlement) on a different object world — no harvest-plan coupling, no roadside inventory, no certification riding loads |
| Mill Production Systems | downstream | the mill's internal production execution begins after intake; this Type ends at the mill gate |

The most important boundary is with Logging Operations Management, and vendors themselves draw it in their product lines: operations-execution products on one side, logistics/supply-chain products on the other. Remove the chain-wide flow and only the harvest job remains (Logging Operations Management); remove the job and only the flow remains (this Type). The hand-off is bidirectional: harvest operations produce the loads that enter the flow, and the flow's delivery records feed back into production and settlement.

## Representative Products

- **Remsoft** — Logistics line with LOGR (digital delivery records) and ScalePass (digital load slips), Remsoft Operations (allocation, transport scheduling, mill/yard inventory planning), and Tactical Optimization (harvest, roads, and wood-flow planning); planning-led platform serving forest owners, mills, and supply-chain organizations, with explicit fiber-supply and procurement role surfaces
- **Trimble Forestry** — Wood Supply Execution (log supply plan execution and dispatch), LogForce (wood transportation management), and SilvaPRO (wood procurement ERP), positioned by the vendor as the procurement and logistics links of a five-link forestry supply chain

The Core Model was checked against a market-intelligence platform (timber pricing and benchmarks) to confirm what this Type is not, and against both vendors' estate-management and operations product lines to confirm the seams toward Forestry Management and Logging Operations Management.

## Sources

Research date: **2026-09-10**

Primary vendor surfaces (solution, product, and role pages):

- Remsoft — https://remsoft.com/solutions/logistics/ , https://remsoft.com/remsoft-logr/ , https://remsoft.com/roles/fiber-supply-mill-manager/ , https://remsoft.com/roles/timber-marketing-procurement/ , https://remsoft.com/tactical-optimization/
- Trimble — https://www.trimble.com/en/industries/forestry , https://www.trimble.com/en/products/forestry/wood-supply-execution , https://www.trimble.com/en/products/forestry/logforce
- ResourceWise (Forest2Market) — https://www.forest2market.com/ (boundary pole)

> Sourcing limitation: vendor help centers and user guides were not reachable from the research environment on 2026-09-10; Trimble product pages are JavaScript-rendered and yielded hero positioning only, so Trimble evidence is positioning-tier. Several specialist candidates could not be reached at all (a log-scaling and settlement vendor, a wood-flow optimization platform, a log-haulage specialist, a Nordic forest-industry software vendor — domains unreachable or timed out), so the flow-management sample is two vendors with multiple product lines rather than a wider spread; cross-product commonality claims rest on those two independent vendors. Procurement/settlement depth (pay computation, pricing engines) is unverified in public documentation and is stated here as delivery-against-contract visibility, not in-product invoicing. Precise operational details (numeric limits, default settings, exact state names) are intentionally not stated; vendor marketing figures were recorded in the Research Notes only. The historical (paper-era) check is conceptual, drawn from the documented delivery-ticket, scale-ticket, and wood-yard-ledger tradition, not from a fetched historical source.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary tests are recorded in the paired Research Notes.
