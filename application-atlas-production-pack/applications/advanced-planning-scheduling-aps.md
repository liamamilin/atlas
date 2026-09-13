# Advanced Planning & Scheduling / APS

## Overview

An **Advanced Planning & Scheduling (APS) application** is the manufacturing plant's finite-capacity scheduling layer. It holds a working model of the factory — production orders broken into operations, resources such as machines and crews with calendars and capacity limits, setup and changeover rules, and material availability — and computes a wall-clock schedule that assigns each operation to a resource and a time slot. That schedule is the application's central object: planners inspect it on a time-axis board, adjust it, test alternatives, and publish it to the shop floor and ERP as dated, sequenced, resource-assigned work.

The defining structure is small:

```text
Production orders
└── Operations (steps per order)
    └── Finite-capacity resources with availability calendars
        └── Computed schedule (operation → resource → time)
            └── Planner review → adjustment → regeneration loop
```

What distinguishes this Type from the planning modules around it is **finite capacity at operation level**: work is scheduled in real clock time onto resources that cannot be double-booked, not spread over weeks as "capacity requirements". Execution recording (what actually happened) belongs to MES; the business records (orders, inventory, routings as master data) belong to ERP; demand-to-order explosion belongs to MRP-style production planning. The APS consumes those systems' data and returns the schedule.

## Users & Context

Primary users:

- **Production planner / scheduler** — the core role. Loads the current order book and plant model, generates and reshapes the schedule, handles rush orders, machine breakdowns and material delays, and issues the shop-floor schedule. This person lives on the schedule board.
- **Planning lead / master scheduler** — defines what a good schedule means (priorities, due-date rules, capacity policies), arbitrates conflicts between customer commitments and plant capacity, and approves scenarios before they become the working schedule.

Secondary users:

- **Plant / operations management** — consumes load, bottleneck and on-time views of the schedule.
- **IT / integration staff** — maintains the data exchange with ERP, MES and inventory systems; the APS is only as current as its last data feed.
- **Shop floor (supervisors, operators)** — normally consumers of the schedule (dispatch lists, sequence, dates) rather than operators of the tool.

Typical context: discrete and process manufacturers with shared machines, changing priorities, meaningful setup/changeover times, and material or labor constraints — anywhere ERP dates and shop-floor reality drift apart and planners would otherwise rebuild schedules manually in spreadsheets.

## Core Model

### The Defining Core

**Production order (job)** — a schedulable unit of work for producing an item in a quantity by a date. Orders arrive from customer orders, forecasts or MRP output, or are created by the planner (for example to replenish stock). The order is the handle through which priorities, due dates and promise dates flow into the schedule.

**Operation** — one step of an order's work: a segment of processing on a resource with a duration driven by quantity and process rates. Orders whose production spans several stages carry a sequence of operations (a routing); dependencies tie operations to their predecessors. One operation is the smallest thing the scheduler moves around.

**Resource with calendar and capacity** — machines, work centers, production lines, crews, workers, tooling and molds that operations occupy. Each resource has an availability calendar (shifts, holidays, planned maintenance, downtime) and a capacity rule, so its working time is finite and time-bounded. Labor and tooling can attach to an operation alongside the machine, optionally gated by skills.

**Constraint** — the rules the schedule must respect: resource capacity and calendars; sequence-dependent setup and changeover times between operations on the same resource; material availability for the operation's inputs; order priorities and due dates; and industry-specific rules (batch limits, cleaning cycles, storage or expiry windows) where they apply.

**Schedule** — the central object the application exists to produce and maintain: the assignment of every operation to a resource and a start/end time such that the constraints hold. It is user-visible on a time axis, and it is a living object — parts of it are proposed and regenerable, parts are fixed or locked.

**The review–adjust–regenerate loop** — planners do not merely receive the schedule; they operate it. They inspect it, move and reassign work, lock what is committed, and have the system recompute the rest when orders, priorities or conditions change.

### How the Pieces Fit

```text
Orders (from ERP / MRP / planner)
  ↓ decomposed into
Operations (routing steps, quantities, durations)
  ↓ assigned onto
Resources × Calendars (finite capacity)
  + constraints (setup/changeover, materials, priorities, dates)
  ↓ computed by the scheduling engine
Schedule  ←── planner adjusts (move / reassign / lock / expedite)
  ↓ regenerated on change
Published as dated, sequenced, resource-assigned work
  → ERP / MES / shop floor
```

### One Structure, Many Implementations

The core model is written conceptually. Implementations differ in vocabulary and depth, not in structure:

```text
Concept:      Production order
Realized as:  manufacturing order, work order, production job — sourced from
              ERP sales/production orders, MRP planned orders, or planner entry

Concept:      Operation
Realized as:  routing steps, process steps, task divisions — fixed-duration or
              per-quantity time, with alternates, splits and parallel branches

Concept:      Finite-capacity resource
Realized as:  machine, work center, line, tank/furnace, labor crew, worker with
              skill matrix, tooling/mold — each with shift calendars and limits

Concept:      Constraint set
Realized as:  setup matrices and changeover rules, material checks, pegging
              rules, expiry/batch rules, priority and due-date policies
```

### Standard Capabilities Around the Core

Mature products commonly add — without these being definitional:

- a Gantt-style **schedule board** as the primary working surface
- **constraint and problem reporting**: overloads, material shortages, late orders, bottleneck resources, critical-path coloring
- **what-if scenarios**: private copies of the model to test a rush order or an extra shift before committing
- **forward and backward scheduling modes**: start-as-soon-as-possible versus anchored to the due date
- **proposed versus firm/locked schedule elements**, so regeneration cannot wipe out commitments
- **setup/changeover modeling** and setup-time minimization within sequences
- **material availability** feeding the schedule decision
- **alternate resources** and multi-resource operations (machine + crew + tool)
- **bidirectional integration**: orders, routings, calendars and inventory in; dates, sequences and priorities out
- load leveling, due-date quoting, expedite/prioritization actions, KPI dashboards

Optional, segment-dependent structure includes weighted multi-objective optimization engines, multi-plant/network scope, mid- and long-term planning tiers synchronized with short-term scheduling, labor/shift scheduling integration, and process-industry constraint packs (batch furnaces, tank cleanup, campaigns, expiry).

## How It Works

The lifecycle runs as a continuous loop rather than a one-way transaction.

### 1. Load the plant model

```text
Connect to ERP / MES / inventory (or files/spreadsheets)
→ import orders, quantities, due dates
→ import routings/operations, work centers, resources
→ import calendars, shifts, downtime, skills
→ import current inventory and material status
```

The APS is a consumer of master and transactional data; it does not replace the systems of record. In some products the exchange is incremental — only changed records move between systems — so the model can be refreshed frequently.

### 2. Generate the schedule

The engine assigns each operation a resource and a start/end time within calendar availability, honoring capacity, setup/changeover rules, material availability and priorities. Planners typically choose a direction — forward (start immediately, finish when work allows) or backward (finish by the due date, start as late as possible) — and dispatching rules (by priority, due date, setup affinity). Products differ in how far they go beyond rules toward weighted optimization; manual, rule-driven scheduling is a fully legitimate form of the Type.

### 3. Review and adjust

```text
Open the schedule board (Gantt)
→ check colors/flags: overloads, shortages, late orders, bottlenecks
→ drag an order to a new time, reassign to an alternate resource
→ fix (firm/lock) what is committed
→ expedite or re-prioritize the rest
→ let the engine re-place affected operations
```

This step is the heart of the Type: the planner's judgment is applied on top of the engine's proposal, not instead of it.

### 4. Test alternatives

A rush order, a machine outage or a new hire plan is evaluated in a what-if scenario — a sandboxed copy of the model — and compared against the working schedule before anything is committed.

### 5. Publish to execution

```text
Confirm the schedule
→ export planned start/finish dates, resource assignments, sequence
→ ERP / MES / shop-floor surfaces receive the work
→ dispatch lists or sequences guide the day's production
```

### 6. Replan on change

Machine breakdowns, late materials, new orders and priority changes re-enter the loop: refresh the affected data, regenerate the impacted portion of the schedule (proposed elements move; locked elements stay), and republish. A schedule that has drifted from shop-floor reality is replanned from current status — completions and downtime reported by MES or the shop floor are standard inputs here.

### What the Type Requires vs What Products Add

**Required for the Type**: production orders; operations; finite-capacity resources with calendars; a computed, user-visible, adjustable schedule; the regenerate loop.

**Standard in mature products**: Gantt board; constraint/problem reports; what-if scenarios; forward/backward modes; firm/locked elements; setup/changeover modeling; material availability; alternate resources; bidirectional ERP/MES integration; priority and expedite handling.

**Varies by product and deployment**: optimization weighting; multi-plant scope; mid/long-term planning tiers; labor and skill depth; industry-specific constraint packs; open-source versus commercial packaging; cloud versus on-premise.

## Interfaces

Exact layouts and names vary by product; these are the recurring surfaces.

### Schedule board (Gantt)

The primary working surface. The schedule is drawn as bars on a time axis, one lane per resource (or per order), typically starting at the current shop-floor state and extending across the planning horizon.

- Typical information: operations as time bars with order/item labels; resource lanes; calendar/downtime shading; color coding for feasibility, lateness, priority or criticality.
- Primary actions: drag a bar to a new time; drag onto an alternate resource; open order/operation detail; fix/lock; filter to a resource, order or date range.

### Order and operation lists

Table views of manufacturing orders and their operations.

- Typical information: order number, item, quantity, due date, status (proposed/firmed/completed), planned start/end, assigned resource.
- Primary actions: create/edit orders, change priorities and due dates, firm or release, drill into the schedule position.

### Constraint and problem reports

The exception surface: capacity overloads, material shortages, late orders, bottleneck resources, critical-path items.

- Typical information: which orders are late or at risk, which resources are overloaded, what constraint blocks a date.
- Primary actions: navigate to the offending operations on the board, expedite, reassign, re-prioritize.

### Resource / load views

Per-resource schedules and utilization over the horizon.

- Typical information: load versus capacity per day/shift, idle time, setup time consumed, utilization trends.
- Primary actions: adjust calendars, rebalance work, identify bottlenecks.

### Scenario (what-if) screens

Lists and comparison views for alternative plans.

- Typical information: scenario copies, their differences from the working plan (dates, lateness, cost).
- Primary actions: create a scenario from the current plan, modify it, and compare it against the working schedule before applying any of its changes.

### Integration and publish outputs

Not always a rich screen, but a defined surface: import jobs/mappings for ERP and MES data; export/publish actions that push dates, sequences and assignments back; dispatch lists or sequence views destined for the shop floor.

## Important Rules / Behaviors

### Finite capacity is binding

A resource cannot host more concurrent work than its capacity and calendar allow; an operation can only land inside available time. This is the structural rule that separates the Type from infinite-capacity planning, and it is why calendars, shifts, holidays and downtime are first-class data.

### Schedule elements have commitment states

The schedule distinguishes proposed work from fixed or locked work (and, in integrated deployments, work already in execution). Replanning moves proposed elements; fixed and locked elements are preserved. What starts out locked — e.g. work already released to the floor — varies by product and stage, but the distinction itself is universal.

### Replanning respects direction and constraints

Forward planning places work as early as capacity allows; backward planning anchors completion at the due date. Regeneration cannot place an operation outside the calendars, before its material is available, or ahead of a higher-priority order if the dispatching rules say otherwise. When constraints cannot be met, the violation is surfaced (late, overloaded, short) rather than silently ignored.

### The schedule is only as current as its inputs

Orders, inventory and shop-floor status live in other systems. Stale data yields unrealistic schedules; a machine breakdown or a stockout discovered mid-week is a replan trigger, not a footnote. This dependency is why integration quality, not algorithm sophistication, is the most common determinant of whether an APS deployment works.

### Objectives are configured, not universal

"Good" is defined per plant: meet due dates, minimize changeovers, maximize utilization, level load, cut overtime. Products express this as prioritization rules, dispatching heuristics, or weighted optimization factors. No single objective function defines the Type.

## Variants

- **Short-term shop scheduler** — the classic form: finite-capacity scheduling of the current order book over a near-term horizon, with maximum interaction on the board.
- **Integrated planning + scheduling tiers** — mid/long-term planning synchronized with detailed short-term scheduling in one product (aggregate decisions feeding daily schedules).
- **Suite module vs standalone** — APS embedded in a vendor's manufacturing/operations suite, or a dedicated product that sits beside any ERP.
- **Discrete vs process overlays** — job shops and fabrication (setup affinity, alternates) versus batch/process industries (campaign planning, tank and furnace constraints, cleaning, expiry).
- **Single-plant vs multi-plant** — one site's schedule versus network views spanning plants and shared resources; the multi-plant edge overlaps supply planning territory.
- **Optimization posture** — planner-driven, rule-based scheduling versus optimization engines with weighted business objectives.
- **Deployment and packaging** — on-premise desktop-era clients through cloud/web applications; commercial licenses through open source.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Production Planning | upstream, adjacent | bucketed (day/week) requirements, typically infinite or rough-cut capacity, explodes demand into planned orders and materials; APS consumes its orders and assigns them to real resources in clock time |
| Manufacturing ERP | system of record | owns orders, inventory, items, routings as business records; leaves operation-level scheduling to the APS and receives its dates back |
| Manufacturing Execution System / MES | execution counterpart | records what actually happened (completions, downtime, progress); APS decides what should happen; they exchange status and priorities |
| Shop Floor Management | execution surface | day-of work execution, reporting and visual management on the floor; the APS owns the schedule across the horizon above it |
| Demand Planning / Supply Planning / Supply Chain Planning | network-level planning | aggregate demand and supply across sites in time buckets; no operation-level, resource-bound factory schedule |
| Resource Calendar / Enterprise Resource Scheduling | generic booking | reserves arbitrary resources for appointments or events; lacks orders, routings, BOMs and manufacturing constraint semantics |
| Construction Scheduling | different domain, similar verb | schedules a project network of activities to a completion date; not recurring production orders routed over factory resources |

The most important boundary is against **Production Planning**: both hold orders, resources and calendars, and both produce "plans". The structural test is the capacity model and the time granularity — remove per-resource, operation-level finite time assignment and what remains is production planning; keep it and the application is an APS regardless of what era or vendor it came from.

## Representative Products

- **PlanetTogether APS** — dedicated APS for mid-market and larger manufacturers; explicit five-step discipline from ERP data import through optimization and manual adjustment to publishing the schedule back to ERP.
- **Asprova** — long-established (since 1994) dedicated APS with a module family separating short-term finite-capacity scheduling from mid/long-term planning, MRP and MES; strong in Japanese and Asian manufacturing.
- **frePPLe** — open-source planning and scheduling application; a transparent data model (orders, operations, resources, calendars, setup matrices) and an interactive Gantt plan editor with scenarios and constraint reporting; popular with smaller manufacturers.

The definition was checked against older-generation finite-capacity schedulers (1990s lineage, of which Asprova is a surviving example) so that it does not assume modern optimization engines, cloud delivery, or specific integration stacks.

## Sources

Research date: **2026-09-06**

- PlanetTogether — https://www.planettogether.com/ ; "What Is Advanced Planning and Scheduling (APS)?" — https://www.planettogether.com/aps-software/what-is-advanced-planning-scheduling
- Asprova — https://www.asprova.com/en/ ; product overview https://www.asprova.com/en/asprova.html ; Asprova MS (short-term scheduler) https://www.asprova.com/en/asprova/asprova_ms.html ; scheduling logic https://www.asprova.com/en/asprova/equipped_with_advanced_and_highly-flexible_scheduling_logic.html
- frePPLe — documentation index https://frepple.com/docs/current/ ; "A day in the life" https://frepple.com/docs/current/a-day-in-the-life/index.php ; data model https://frepple.com/docs/current/model-reference/ and domain model https://frepple.com/docs/current/model-reference/domain-model.php ; user interface https://frepple.com/docs/current/user-interface/ ; plan editor https://frepple.com/docs/current/user-interface/plan-analysis/plan-editor.php

> Sourcing limitations: Asprova's online help requires a member login and its knowledge center was unreachable during research, so Asprova claims rest on official product pages. PlanetTogether's support knowledge base is access-gated, so its behavior is documented at the process/positioning level. Documentation for one further suite-vendor product (Siemens Opcenter APS) could not be reached at all and was excluded from the researched sample. Precise numeric details (scheduling-engine internals, default rules, plan-horizon limits) are therefore intentionally not stated in this document; they are recorded, where available at all, in the Research Notes.

Detailed product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
