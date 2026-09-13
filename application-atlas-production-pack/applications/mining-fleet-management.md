# Mining Fleet Management

## Overview

A **Mining Fleet Management System** (industry term: FMS; also sold as "dispatch" or "mine control" software) is the mine's real-time execution system for its mobile equipment fleet — the haul trucks, loading units (shovels, excavators, loaders, underground LHDs), drills, and support machines that move the mine's material.

The defining structure is small:

```text
Mine's mobile equipment fleet (individually identified machines)
└── Assignment loop maintained through the shift
    │   (which loading unit or feed point a truck serves, which destination it hauls to,
    │    which task a drill or support machine works)
    └── Production record at machine/load grain
        (attributed loads/cycles: machine, operator, source, destination, material, time)
        └── Shift accumulation (per-shift production against the shift plan)
```

Everything commonly associated with modern mining FMS — GPS positioning, mathematical and AI-assisted dispatch optimization, autonomous haulage, machine-health modules, payload and fuel management — is widespread in current products but is not part of the defining core. A radio-dispatch operation, in which a controller directs trucks by voice and logs loads as crews call them in, satisfies the same core; it survives today as a product tier for sites without network infrastructure.

When the center of gravity shifts to designing the deposit and scheduling periods (Mine Planning), to drivers and compliance on public roads (Fleet Management System), or to the whole mine's production accounting and cost (Mining Operations Management), the product is drifting toward a different Application Type.

## Users & Context

Primary users:

- **dispatcher / mine controller** (control room): watches the live fleet picture, assigns and reassigns machines, logs events, responds to deviations
- **equipment operator** (in-cab terminal or radio): receives assignments, works the load–haul–dump cycle or assigned task, logs activity and status
- **shift supervisor**: monitors shift progress against plan, handles exceptions on the ground

Secondary users:

- **mine and planning engineers**: consume production data to reconcile actual movement against the geological plan
- **maintenance teams**: consume equipment time-usage and machine-health data
- **system administrator**: configures machines, locations, material classes, shift structures, rules, and integrations

The work environment is a private mine site — open pit or underground — operating in shifts around the clock. The FMS serves as the site's operational single source of truth for what the fleet did: mature deployments replace competing spreadsheets and standalone databases with one captured record.

## Core Model

### The Defining Core

```text
Mine's mobile equipment fleet (individually identified machines)
└── Assignment loop maintained through the shift
    └── Production record at machine/load grain
        └── Shift accumulation against the shift plan
```

Three structures. The Type is recognizable only when all three are present:

- **The fleet as individually identified managed units.** Each machine — haul truck, loading unit, drill, support vehicle — is a persistent identified record the system watches and directs. Without this, the product is a telemetry feed or an asset list.
- **The assignment loop.** Machines are continuously directed to the mine's own work: which loading unit or feed point a truck serves, which destination (dump, crusher, stockpile) it hauls to, which task a drill or support machine works. Assignments are adjusted as the shift unfolds — queues lengthen, machines break down, grade targets change. The loop binds machines to the mine's own work locations and material destinations (source → destination), not to customer jobs or public-road routes. Without this, the product is a schedule (planning territory) or a tracking display with no direction.
- **The production record at machine/load grain.** What the fleet actually moved is captured as attributed records — each load or cycle carrying machine, operator, source, destination, material type, and time — accumulating per shift into the operational production record (tonnes moved, cycles completed, equipment time). Without this, dispatch is blind to its own output, and production reporting, reconciliation against the plan, and contractor payment have no basis.

The three are jointly load-bearing: a fleet register alone is asset tracking; an assignment loop without identified machines is a whiteboard; production records without the loop are weighbridge reports with no fleet behind them; live dispatch without records is direction with no memory; tracking plus reports without the loop is monitoring, not management.

### Standard Capabilities in Mature Products

A typical modern mining FMS carries most of these. They are not what makes the product an FMS, but they make it practical at production scale:

- **Live positioning** — machine locations on a site map; GPS or high-precision positioning in open pits, tag- or Wi-Fi-based positioning underground, with infrastructure-free options where connectivity is impractical.
- **Machine status and time usage** — operating / idle / down states per machine, converting shift activity into availability and utilization metrics.
- **Operator logon** — operators identify themselves on the machine; production and equipment time are attributed to the operator as well as the machine.
- **Shift plan and compliance monitoring** — the shift's plan (machines, activities, targets) held at per-machine granularity; short interval control compares expected vs actual through the shift and alerts on deviations (behind target, wrong source or destination, delayed start).
- **In-cab operator terminal** — a ruggedized onboard device showing the current assignment and guidance, carrying messages from the control room, and logging activity; tolerant of lost connectivity.
- **Control-room console** — the dispatcher's or mine controller's surface: fleet map, machine statuses, queue states at loading units and destinations, assignment controls, deviation alerts.
- **Production reporting and KPIs** — tonnes, loads, cycle times, availability and utilization, plan vs actual — per shift, machine, operator, and destination.
- **Payload, fuel, and material machinery** — payload monitoring at loading units, fueling/charging coordination, and blending or grade control toward crusher and stockpile targets; depth varies by product.
- **Machine-health and maintenance integration** — companion modules of varying depth feeding maintenance planning.
- **Analytics layer** — dashboards, benchmarks, enterprise KPIs.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. The Variants section below enumerates how specific implementations realize each concept.

```text
Concept:            Machine identity & live position
Implementations:    GPS / high-precision ranging (open pit), tag or Wi-Fi positioning,
                    radio-reported position (no network infrastructure)

Concept:            Assignment intelligence
Implementations:    manual dispatcher decision → rules-based automation →
                    mathematical optimization → AI-adaptive assignment

Concept:            Operator surface
Implementations:    in-cab ruggedized touchscreen, onboard tablet,
                    radio call-in logged by the controller

Concept:            Connectivity
Implementations:    networked real-time, Wi-Fi zones with store-and-forward,
                    radio/voice logging
```

A reader who has only seen a GPS-and-AI open-pit dispatch system should still be able to recognize a radio-based underground deployment as the same Type from the Core Model.

## How It Works

### Configure the mine's work structure

Before the loop can run, the system is configured with the site's own structure: machines enrolled as identified units; work locations defined (pit benches or underground headings, dumps, crushers, stockpiles, workshops, and where supported, restricted zones); material classes defined (commonly ore, waste, and development); the shift calendar and rosters; and the rules that let status, location, and material assignments update automatically as work progresses. No two mining operations are configured alike; site-specific configuration is part of every deployment.

### Run the shift

```text
Shift plan loaded (machines, activities, targets — per machine)
→ operators log on to machines
→ assignments issued (by the dispatcher, by rules, or by an optimizer)
→ machines work the load → haul → dump cycle (or their assigned task)
→ each load/cycle recorded: machine, operator, source, destination, material, time
→ control room watches progress against plan; deviations alert
→ assignments adjusted through the shift
→ shift closes with its production record complete
```

This is the defining loop. The assignment is the system's central act: a haul truck's assignment is a (loading unit, destination) pair, and changing that pair — to rebalance queues, cover a breakdown, or steer grade — is what dispatching means.

### Capture production

Each load is recorded with its location, equipment, shift, and destination, building a traceable record from source to destination. Where dedicated material machinery is present, material is classified at the point of loading and status updates flow into dispatch, production tracking, and shift dashboards; stockpile inventories update; and production is reconciled against geological expectations as the shift proceeds.

### Monitor compliance through the shift (short interval control)

The shift schedule — with granularity down to each machine and activity — is visible in the control room, on onboard devices, and to supervisors. The system monitors compliance continuously and raises automatic alerts to the control room: task progress expected vs actual, and incorrect source or destination of material movements. This is the mechanism that keeps execution tied to the plan without waiting for end-of-shift reports.

### Handle the exceptions

Real shifts deviate constantly, and the loop is built to absorb it:

- machine breakdown → its feed is reassigned; downtime enters the time-usage record
- operator absence or roster change → re-logon and reassignment
- queue imbalance at a loading unit or destination → assignments rebalanced
- wrong destination or material mismatch → deviation alert; correction recorded
- connectivity loss → in-cab capture continues offline and transmits when the machine regains coverage; radio call-in remains a workable fallback
- entry into a restricted area → alert, in products with zone-control machinery

### Core vs Common vs Optional

**Defining core** — without these, not a mining FMS:

- the fleet as individually identified managed units
- the assignment loop maintained through the shift
- the production record at machine/load grain

**Standard capabilities** — present in most modern products:

- live positioning; machine status and time usage; operator logon
- shift plan with compliance monitoring (short interval control)
- in-cab operator terminal; control-room console
- production reporting and KPIs
- payload, fuel, and material machinery (depth varies)
- machine-health integration; analytics layer

**Variant / optional** — depends on environment, OEM posture, and era:

- optimization depth (manual → rules → mathematical → AI-adaptive)
- execution mode (manually driven, tele-remote, autonomous haulage)
- environment-specific machinery (caving compliance, development-heading workflows)
- connectivity tier (radio/voice logging → networked real-time) as a deployment ladder inside single products

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Control-room console

The dispatcher's / mine controller's primary surface.

- live fleet map with machine positions and statuses; queue states at loading units and destinations; shift progress against plan; deviation alerts
- primary actions: assign and reassign machines, log events, respond to alerts, message operators

### In-cab operator terminal

The operator's surface, ruggedized for the cab and tolerant of offline operation.

- current assignment, guidance to the loading unit and destination, messages from the control room, activity logging
- primary actions: acknowledge assignment, log activity and status, send and receive messages

### Shift planning surface

Where the shift's work structure is built and tracked.

- shift plans at per-machine and per-activity granularity; baselines of agreed plans; actuals captured against plan in near real time
- primary actions: create or import a shift plan, assign machines to activities, track progress, adjust

### Production reporting / analytics

- tonnes, loads, cycle times, availability and utilization, plan vs actual — per shift, machine, operator, source, and destination; dashboards and reconciliation views
- primary actions: filter, compare, drill into a machine's or shift's history, export

### Administration / configuration

- machines, locations, material classes, rules, rosters, restricted zones, and integrations with site systems (for example weighbridges, conveyors, ERP, geological models)
- primary actions: register machines, define locations and materials, configure rules and integrations

## Important Rules / Behaviors

### The assignment binds a machine to the mine's own work

A truck's assignment is a (loading unit, destination) pair; a drill's or support machine's assignment is a task. Assignments are the system's central manipulable object, and reassignment is continuous through the shift.

### Production is attributed, never anonymous

Every load carries machine, operator, source, destination, material, and time. This attribution is what makes the record usable for reconciliation against the plan, equipment and operator performance, and contractor payment.

### State updates by rule, not retyping

As work progresses, equipment status, locations, and material assignments update automatically under configured rules — helping prevent material mismatches and keeping the record current without manual re-entry.

### Plan compliance is evaluated continuously

Expected vs actual is compared at shift (and sub-shift) granularity; deviations — behind target, wrong source or destination, delayed start — alert the control room during the shift, not after it.

### The system is the single source of truth

Operational data is captured once and flows to dispatch, dashboards, and reports. Mature deployments treat competing spreadsheets and standalone databases as the failure mode this system exists to eliminate.

### Connectivity loss degrades but does not break the loop

In-cab capture works offline and transmits when the machine re-enters coverage; some products ship radio-based activity logging as a current tier for sites without network infrastructure — evidence that the core loop predates modern connectivity machinery.

### Time usage is a first-class record

Operating, idle, and downtime states are captured per machine and converted into availability and performance metrics — the bridge between the production record and maintenance.

## Variants

- **Open-pit dispatch FMS** — GPS/high-precision positioning, haul-road networks, large truck-and-shovel fleets; the classic dispatch-optimization heartland.
- **Underground mine control** — constrained connectivity, headings and development cycles, LHD-centric loading, tag/Wi-Fi or infrastructure-free positioning; often packaged alongside shift-execution scheduling.
- **OEM-integrated vs OEM-agnostic** — a vendor's FMS bound to its own machines vs open, mixed-fleet systems integrating across brands via APIs.
- **Optimization ladder** — manual dispatcher judgment, rules-based automation, mathematical optimization, AI-adaptive assignment — all current realizations of the same assignment act.
- **Execution mode** — manually driven, tele-remote, or autonomous haulage; autonomy is an execution mode inside the FMS frame (optimized assignments drive autonomous trucks), and mixed fleets are common.
- **Connectivity tier** — radio/voice logging vs networked real-time; single products ship both as tiers for different sites.
- **Commodity and method tuning** — coal, iron ore, caving, room-and-pillar; single pit to multi-site scale.

A variant should remain a **Variant**, not become a separate Type, unless it changes users, core objects, workflow, or rules so much that the Core Model no longer applies.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Mine Planning Application | upstream plan-of-record: designs the deposit, estimates reserves, schedules periods; the FMS executes the shift and records what moved. The shift plan is the handoff artifact; haul data feeds back into planning. Remove the live assignment/production loop → planning; remove the deposit model and reserves → this Type. |
| Fleet Management System (road) | road FMS centers on drivers (behavior, hours of service, licensing), compliance, and public-road routes over an organization's vehicles; this Type centers on production cycles (load → haul → dump), material identity, and plan execution at a private mine site. |
| Vehicle Telematics Platform | the data feed (position, state, engine data); this Type is the management application over the feed — assignment decisions and production records. |
| Mining Operations Management | probable broader sibling: whole-mine operations (production accounting, reconciliation, cost, compliance) vs this Type's fleet-level execution loop. |
| Robot Fleet Management | task-execution-centric robot missions (the robot is the executing party) vs production-cycle-centric mine fleets (machines moving material under operator or autonomous control). |
| Autonomous Fleet Management (road) | road AV fleets run autonomy-executed missions under a supervisory loop; in mines, autonomous haulage is an execution mode inside the mining FMS. |
| Construction Equipment Management | job-allocation-centric (machines to jobsites with cost and charge-out) vs production-cycle-centric (loading and hauling with material and destinations). |
| SCADA / HMI | supervises fixed process equipment through control loops; this Type directs mobile machines through an assignment loop and records production. Both may share a control room. |
| Dispatch Management (generic) | generic dispatch assigns a queue of incoming customer work to field resources; mine dispatch centers on the mine's own material movement. The assignment mechanism is shared; the object world differs. |
| Quarry Management | aggregates operations center on the product-sales loop (produce → stockpile → sell → weighbridge → invoice); fleet tracking appears there as a module, not the center. |

The boundary with **Mine Planning** is the most important one, because the two Types meet at the shift plan. Planning decides where and when to mine over weeks and months; the FMS decides which machine does what now and records what actually moved. Products that extend short-interval scheduling down to shift execution sit on this seam.

## Representative Products

- **DISPATCH** (Modular Mining, a Komatsu company) — the category-defining dispatch-optimization FMS; open and mixed-fleet; open-pit heartland.
- **Pitram** (Micromine) — OEM-agnostic fleet management and mine control; modular connectivity tiers from radio-based logging to networked real-time; underground and surface.
- **Deswik.OPS + ORB** (Sandvik) — underground shift-execution scheduling plus dispatch-decision optimization; with the AutoMine automation line, an example of the FMS function sold as decomposed products.

Major market anchors also named in the industry — Wenco FMS (Hitachi Construction Machinery), Caterpillar MineStar, Hexagon OP Pro — could not be independently documented in this research pass (see Sources).

## Sources

Research date: **2026-09-09** (research notes); application document completed **2026-09-10**.

Primary vendor surfaces (official product pages):

- Komatsu / Modular Mining — DISPATCH and Smart Mining ecosystem: https://www.modularmining.com/ , https://www.komatsu.com/en-us/technology/smart-mining/loading-and-haulage/dispatch
- Micromine — Pitram (fleet management and mine control) and Material Management: https://www.micromine.com/pitram/ , https://www.micromine.com/pitram/material-management/
- Sandvik — Operational planning and shift execution (Deswik.OPS + ORB): https://www.rocktechnology.sandvik/en/digital-solutions/operations-and-connected-fleet/operational-planning-and-shift-execution/

> Sourcing limitation: official documentation for Wenco FMS, Caterpillar MineStar, and Hexagon OP Pro was not reachable during research (bot-check / access-denied / transport errors). Claims in this document are calibrated to the three reachable products; the unreachable market anchors are named without operational claims. Vendor marketing figures and module names are kept in the Research Notes, not in this document.

Detailed evidence, product-by-product observations, the cross-product comparison, and the historical / market-sample check are recorded in the paired Research Notes.
