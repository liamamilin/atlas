# Port Terminal Operating System

## Overview

A **Port Terminal Operating System (TOS)** is the terminal operator's execution system of record for a cargo terminal: it plans, coordinates, and records the movement and storage of cargo through the facility — between ships at the berth, the terminal's storage yard, and the landside interfaces (trucks and rail).

The defining core is small:

```text
Vessel call (berth + ship stay + load/discharge plan)
└── Cargo lot individually tracked through the terminal's own geography
    └── Planned-and-confirmed move (quay lift / yard transfer / gate transaction)
        └── Real-time convergence of the system record with physical reality
```

Everything else commonly associated with modern terminal software — electronic data interchange with shipping lines, tariff-based invoicing, KPI dashboards, optimization engines, equipment automation, digital twins — is widespread in current products but is not what makes the system a TOS. Older, regional, and paper-era terminal operations fit the same core without any of those specifics.

When the dominant object shifts to goods inside a building driven by orders, or to trailers in a distribution-center yard, the product is a different Application Type (Warehouse Management, Yard Management). When the dominant party is the ship rather than the facility, it is a vessel/fleet platform. The TOS is the facility operator's system.

## Users & Context

The primary users are the terminal operator's operations staff:

- **Vessel / stowage planner** — builds the plan for each vessel call: berth allocation, the loading/discharge sequence, and where each cargo unit will be placed in the yard.
- **Yard planner / controller** — manages yard positions and housekeeping, decides stacking strategy, and reacts to congestion and plan deviations.
- **Operations control / dispatch** — monitors work in progress, assigns and reassigns equipment and labor, and resolves exceptions in real time.
- **Gate clerks** — process trucks arriving to deliver or pick up cargo.
- **Equipment operators** — crane, yard-crane, and terminal-tractor drivers who receive job instructions and confirm completions, typically through in-cab or vehicle-mounted terminals.
- **Finance / billing staff** — turn recorded service events into invoices for shipping lines and other customers.

Secondary users include management (through KPI dashboards and reports), shipping lines and their agents (through status data, portals, and message exchange), and — at automated terminals — remote operators in control rooms.

The work environment is a 24/7 industrial operation: quay cranes and ship schedules set the rhythm, yard space is the binding constraint, and trucks and trains arrive on their own schedules. The system is mission-critical: when it stops, the terminal effectively stops.

## Core Model

### The Defining Core

**The vessel call.** The terminal's production is organized around vessel visits. A vessel call binds a specific ship, a berth, a stay window, and a load/discharge plan — the stowage plan that says which cargo comes off the ship, in what order, and which cargo goes on, into which bay. The vessel call is the anchor to which quay-crane work, yard positioning, and billing for ship services attach. Without it, the system is a berth scheduler or a generic yard system, not a terminal operating system.

**The cargo lot.** Each unit of cargo is individually recorded and positioned inside the terminal's own geography. For containers this is the identified container; for general cargo it is the typed and measured lot; for bulk it is the tracked quantity; for RoRo it is the wheeled unit. The terminal's geography is modeled explicitly: the quay, yard areas organized into blocks/stacks/rows (or cargo heaps and warehouses for non-container cargo), specialized zones (refrigerated stacks, inspection, stuffing/destuffing, empty-container depot, repair), the gate, and the rail front. The cargo lot carries its identity (number, type, size, weight, marks), its commercial context (shipping line, port of discharge, import/export/transshipment character), and its position, which changes only through recorded moves.

**The move.** The work primitive is the individual move: a quay-crane lift on or off the ship, a yard transfer between positions, a gate transaction in or out. Moves are planned in advance (the vessel plan, the yard plan, the work schedule), dispatched to specific equipment and operators, executed, and confirmed back — so the system's picture of the yard converges with physical reality in real time. This plan–dispatch–confirm loop is what makes the system an *operating* system rather than an inventory list.

**Real-time convergence.** The system's record is the terminal's operational truth: what is in the yard, where, in what state, and what work is under way. Dispatch boards, control-room views, and driver consoles all read from and write back to this single record.

### Standard Capabilities

Mature products commonly add the following. They make a TOS practical, but a system without some of them can still be recognized as a TOS:

- **Gate operations** — truck gate-in/gate-out transactions, identity and damage checks at the gate, access control, and commonly truck time-slotting so landside arrivals are spread across the day.
- **Rail front** — train loading/discharge handling where the terminal interchanges with rail; some vendors ship this as a dedicated rail-terminal product rather than inside the marine TOS.
- **Electronic data exchange** — structured messages with shipping lines, agents, customs, and port community systems (commonly in the EDIFACT and ANSI X12 families, plus product-definable formats), carrying load/discharge lists, container status, and instructions.
- **Billing** — tariffs configured in the system; service events (lifts, storage days, handling by measure) captured as billable events; invoices generated for shipping lines and cargo owners. In some product families billing is a separate engine or even a separate product beside the TOS.
- **KPI dashboards and reporting** — vessel productivity, yard utilization, dwell times, equipment performance, gate throughput.
- **Role-based workstations** — separate working surfaces for vessel planning, yard control, gate processing, equipment operation, finance, and management.
- **Customer visibility** — web portals or message feeds through which shipping lines see their cargo's status in the terminal.
- **Equipment and resource management** — cranes, yard equipment, terminal tractors, and labor shifts as schedulable, assignable resources.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:  Vessel call plan
Realizations:  planner-built stowage plans; rule-based auto-generated stowage;
               digitized berth requests with approval workflows

Concept:  Terminal geography
Realizations:  container blocks/stacks; cargo heaps; warehouse positions;
               zone models (reefer, inspection, empty depot, repair)

Concept:  Move dispatch
Realizations:  manual job lists; optimized real-time dispatch of yard vehicles
               and cranes; equipment-control integration at automated terminals
```

A reader who has only seen a large automated container terminal should still be able to recognize a small mixed-cargo terminal's TOS from the core model.

## How It Works

### Plan a vessel call

```text
Vessel schedule received (directly or via message exchange)
→ berth requested and allocated for the call window
→ discharge and loading lists assembled from shipping-line data
→ stowage plan built (by the planner, or generated and then adjusted)
→ yard positions pre-planned for discharge cargo
→ quay cranes and gangs assigned to the call
```

The vessel call now exists as the terminal's production commitment for that ship.

### Execute the call

```text
Vessel berths; call starts
→ quay cranes work the planned sequence, lift by lift
→ each discharged container is trucked to its pre-planned yard position
→ yard crane places it; position confirmed in the system
→ loading works in reverse: yard crane pulls from planned positions,
   terminal tractor delivers to the quay, crane loads into the planned bay
→ deviations (damaged units, plan changes, equipment faults) are
   re-planned in real time by yard control and dispatch
→ call completes; vessel sails; the call's record closes
```

Throughout, the move is the unit of progress: planned, dispatched, executed, confirmed. Productivity is measured move by move and lift by lift.

### Run the landside

```text
Truck arrives (ideally within a booked time slot)
→ gate identifies truck, driver, and cargo; interchange checks recorded
→ gate-in transaction creates the terminal's custody of the cargo
→ internal dispatch routes the truck to a yard position; yard crane
   handles the lift; position updated
→ gate-out transaction releases cargo (or an empty unit) to the carrier
→ rail fronts work the same way for trains, in train-load quantities
```

### Keep the yard healthy

Between vessel calls, yard control manages the buffer: consolidating stacks, separating cargo by next destination, rehandling to reduce future work, and housekeeping moves — all recorded as moves against positions, all visible on the yard view.

### Turn operations into money

```text
Service events accumulate on the call / the cargo lot
(lifts, storage days, handling by measure, value-added services)
→ tariffs configured in the system price the events
→ invoices generated for shipping lines and cargo interests
→ disputes traceable back to the recorded events
```

### Exchange data with the outside world

Load/discharge lists, container status, and instructions flow between the TOS and shipping lines, agents, customs, and port community systems in structured message formats. The TOS is the terminal's side of that exchange; the port community system and customs systems remain external parties the TOS integrates with.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Vessel / stowage planning view

The planner's workbench for a call.

- the ship's bays, the discharge/loading lists, berth and crane assignment
- primary actions: build or generate the stowage plan, adjust bay sequences, assign resources, release the plan to operations

### Yard view / control board

The terminal's living map.

- yard blocks/stacks with occupancy, cargo by category and status, equipment positions, work in progress
- primary actions: reassign positions, prioritize jobs, dispatch equipment, resolve exceptions

### Gate processing

The landside transaction surface.

- truck/driver/cargo identification, interchange checks, transaction history
- primary actions: gate-in, gate-out, verify and correct cargo data, manage time slots

### Equipment operator console

The in-cab or vehicle-mounted surface for crane and tractor drivers.

- the job list for that machine and operator, one job at a time
- primary actions: accept job, navigate to position, confirm completion, report exceptions

### Billing / tariff administration

The commercial surface.

- tariff tables, contracts, billable events, invoice drafts
- primary actions: configure tariffs, review billable events, generate and issue invoices

### Dashboards and reports

Management's view.

- vessel productivity, yard utilization, dwell, gate throughput, equipment performance
- primary actions: monitor, compare against plan, export reports

### Customer portal

The shipping line's window into the terminal.

- container status and events for that line's cargo
- primary actions: inquire status, download documents, submit instructions where supported

## Important Rules / Behaviors

### The record must match reality

The system's value depends on the yard record being trustworthy. Every position change is the result of a confirmed move; unconfirmed or failed work surfaces as an exception for control to resolve. This is why driver consoles and confirmations exist even in minimally automated terminals.

### The vessel call drives the schedule

Quay work is sequenced to the ship's plan and stay window; yard work is sequenced to the vessel plan (what must be ready to load, and where discharged cargo will land). Landside priorities typically yield to vessel priorities — a late ship costs far more than a late truck.

### Yard space is the binding constraint

Stacking decisions trade off immediate efficiency against future work: poor placement creates rehandles (a container moved more than necessary). Yard capacity, mixing rules (by line, destination, weight, reefer, dangerous goods), and housekeeping all shape how much cargo the terminal can flow.

### Custody changes only through recorded transactions

Cargo enters the terminal's custody at gate-in (or by ship discharge) and leaves it at gate-out (or ship loading). The transactions are the basis for storage and handling charges and for the terminal's accountability for the cargo.

### Billing follows recorded events

Invoices are built from events the system recorded — lifts, storage days, measures handled — priced against configured tariffs. This is why operations capture and billing live in the same system of record, even when billing is packaged as a separate module.

### Roles gate the actions

Planners plan; control dispatches; drivers execute and confirm; clerks transact the gate; finance bills. Role-based access reflects the operational chain of command, and at larger terminals the control room centralizes monitoring and intervention.

## Variants

- **By cargo type** — container terminals (the dominant case); general-cargo and mixed-cargo terminals (cargo tracked by type/subtype and measure, warehouses and cargo heaps instead of stacks); bulk terminals (quantities, weighbridges, loading rates); RoRo terminals (wheeled units); multipurpose terminals running several of these in one system.
- **By scale** — small and mid-sized terminals on lightweight or SaaS products replacing paper and spreadsheets; large and mega terminals on deeply configurable systems with optimization engines.
- **By automation depth** — conventional manned operations; semi-automated (optimized dispatch, remote-controlled cranes); fully automated terminals where the TOS directs equipment-control systems that move containers without drivers.
- **By deployment** — on-premises installations traditional in the industry; cloud/SaaS delivery increasingly common, including one platform operating several terminals across sites.
- **By geography of the facility** — marine port terminals are the defining case; the same product family extends to inland terminals and dry ports, where train and truck fronts replace the vessel call. This extension is a variant of the family, not the defining case of this Type.
- **By mode specialization** — some vendors ship marine and rail-terminal systems as separate products with the same conceptual core.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Yard Management System | adjacent (converges at intermodal yards) | YMS manages trailers and moves in a shipper/DC yard, gate-in to gate-out, with no vessel and no shipside; the TOS's unit of work is the vessel call plus cargo through terminal geography. Vendors themselves sell them as separate products. |
| Warehouse Management System | adjacent | WMS handles goods inside a building driven by orders (receive, put away, pick, ship); the terminal is a transport interchange where storage is a buffer between carriers. Sold as separate products by the same vendors. |
| Transportation Management System | adjacent | TMS plans transport for a shipper or carrier across journeys; the TOS executes cargo transfer inside one facility for the facility's operator. Different party, different unit of work. |
| Marine Fleet Management / Vessel Operations Platform | adjacent (ship-side) | serves the vessel owner's operations with the ship as the asset; the TOS serves the terminal operator with the facility as the asset. |
| Ocean Freight Management | adjacent | manages the forwarder's/carrier's shipment business; the TOS executes the terminal side of the same physical moves. |
| Marina Management | adjacent | recreational berthing of leisure vessels (slips, leases, boater services) vs cargo interchange under vessel calls; different users, objects, and economics. |
| Dock Scheduling Platform | adjacent | plans appointments before arrival at facility docks; berth request/approval for ships lives inside the TOS's vessel-call leg. |
| Airport Operations Platform / Ground Handling Management | cross-mode analog | plays an analogous role for air cargo and aircraft turnaround, but with different objects and systems; not the same Type. |
| Port Community System | external party | multi-party data exchange at port level; the TOS integrates with it but remains the single facility's execution system. |

The most important boundary is with Yard Management: both are "yard" systems, but the TOS is anchored on the shipside — berth, vessel call, quay-crane work — while the YMS is anchored on the trailer in a distribution yard. Where the two worlds meet (container yards at inland rail facilities), the same vendors sell distinct products for each.

## Representative Products

- Kaleris N4 (Navis N4) — the market-leading container-terminal TOS
- Kaleris Octopi — cloud SaaS TOS for small and mid-sized terminals and inland depots
- Kaleris Master Terminal — mixed/general-cargo TOS
- Solvo.TOS — multi-cargo TOS (container, general, bulk, RoRo, river and inland terminals)
- Tideworks Mainsail — marine-terminal TOS for container, RoRo, and general cargo
- CyberLogitec OPUS Terminal / OPUS Terminal M — container and multipurpose TOS

The core model was checked across independent vendor families (Kaleris, Solvo, Tideworks, CyberLogitec), across cargo types, across customer tiers from mega-terminals to paper-replacing SaaS deployments, and against the paper-era practice the software digitized.

## Sources

Research date: **2026-09-09**

- Kaleris — Terminal Operating System pages: https://kaleris.com/solutions/terminal-operating-system/ , https://kaleris.com/what-is-a-terminal-operating-system/ , https://kaleris.com/solutions/terminal-operating-system/container-terminals/ , https://kaleris.com/solutions/terminal-operating-system/cloud-based-tos/
- Solvo — Solvo.TOS product pages: https://www.solvo.ru/en/ , https://www.solvo.ru/products/solvo-tos/
- Tideworks — Mainsail and FAQ: https://tideworks.com/ , https://tideworks.com/mainsail/ , https://tideworks.com/faq/
- CyberLogitec — OPUS Terminal family and press releases: https://www.cyberlogitec.com/

> Sourcing limitation: vendor in-product help centers and user manuals were not reachable from the research environment (login-gated); evidence is from official product, FAQ, and press pages. Precise operational parameters (specific message-type names, numeric limits, state labels, tariff structures) are intentionally not stated. Octopi's own site (getoctopi.com) was unreachable; its capabilities are documented from the vendor's product pages.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
