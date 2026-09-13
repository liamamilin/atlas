# Production Planning

## Overview

A **Production Planning application** is a manufacturer's planning system that converts demand — confirmed customer orders and sales forecasts — into a time-phased plan of what to produce, and carries that plan into the production orders the factory executes. It nets forward requirements against stock and incoming supply, explodes them through bills of material into planned production and purchase orders, and puts those orders on the production schedule for a planner to firm, adjust, and release toward the shop floor.

The defining structure is deliberately small:

```text
Demand (orders + forecast + stock policies)
  → netted against stock and scheduled receipts
  → exploded through build definitions (BOMs, operations)
  → time-phased planned orders (make + buy)
  → planner review and firming
  → scheduled, released production orders
```

Everything else commonly associated with the category — Gantt boards, capacity load charts, what-if simulation, available-to-promise, automation triggers — is standard or optional capability layered on that spine. The application plans; it does not execute the work on the floor, does not optimize detailed operation-by-operation schedules against finite capacity, and does not own the financial record of production.

## Users & Context

The primary user is the **production planner** (often titled master scheduler or production planner): the person responsible for answering "what do we make, how much, and when, so that demand is covered and the factory stays loaded." Their work is cyclical — full planning runs on a weekly or monthly rhythm, incremental re-planning as orders and actuals arrive — and it spans a horizon from the current week out to months or years ahead.

Secondary users:

- **production manager / plant management** — reviews the plan's feasibility, load, and exceptions; arbitrates priorities.
- **buyer / purchasing agent** — receives the planned purchase side (component and material orders) and works it in procurement; in some organizations the purchase side is split out entirely.
- **sales and customer service** — consult planned supply (and available-to-promise views where offered) to estimate delivery dates.
- **shop-floor supervisors and operators** — do not work the plan itself; they receive released orders and tasks through separate execution surfaces.

The setting is a production control or planning office; the application's objects are orders, quantities, and dates rather than machines and material movements, so its surfaces are grids, calendars, and boards rather than terminals or devices.

## Core Model

### The demand picture

The plan's target is a forward picture of production requirements, composed of three streams: confirmed customer orders (deliveries due in each period), the sales forecast (expected demand without orders yet), and stock policies (safety stock, reorder points) that create requirements of their own. In make-to-order-heavy operations the order stream dominates and the forecast may be thin or absent; in make-to-stock operations the forecast and policies carry the plan. Mature products commonly hold this picture as an editable, period-by-period grid — quantities per item per time bucket — that the planner can adjust by hand; some products suggest the forecast rows from sales history.

### Build definitions

To plan production, the system must know how products are made. Manufactured items carry a build definition — a bill of materials (components and quantities, possibly nested through subassemblies) and, where scheduling depth exists, the operations or routing that produce them at particular resources. The planning application commonly consumes these definitions from the same system's product data or from an upstream system; what matters to planning is that the explosion can walk them. Some products also hold the build definitions inside the planning module itself; where they live varies, but the plan always explodes through them.

### The supply position

Requirements are meaningful only against supply: stock on hand, plus scheduled receipts — open purchase orders and production orders already in flight, with their expected dates. The plan's arithmetic continuously compares what will be needed with what will be there.

### Planned orders

The plan's working objects are **planned orders**: time-phased suggestions to produce or purchase specific quantities on specific dates. They are computed, not yet committed. A planned production order exists in a lighter state than a real production order — typically regenerated or replaced when the plan re-runs, unless the planner firms it. Planned orders arise at every level of the build structure: a demand for a finished item explodes into a planned production order for it, which explodes into planned orders for its components, recursively, with component orders timed to finish before their parents need to start.

### Production orders and their lifecycle

When a planner commits, planned orders become real **production orders** (and the purchase side becomes purchase orders or requisitions). A production order advances through a recognizable lifecycle — planned or scheduled, then released to the floor, then done — with the release step marking the boundary where execution recording begins. The production-order pipeline is the plan's output and its memory: scheduled orders yet to run, orders in progress, and completions that feed back into the next planning run.

### Resources, calendars, and capacity

The factory's resources — work centers, workstations, machine or labor groups — exist in the planning model with their working calendars and available hours. At planning grain, capacity is treated as a rough-check, not a constraint solver: calculations commonly assume resources can absorb the load, and capacity appears as comparison views — required hours versus available hours per resource group per period, with over- and under-load highlighted. Detailed, finite-capacity assignment of operations belongs to a different application type.

### Planning parameters and messages

The computation is steered by parameters held on items and locations: lead times, lot sizes and order multiples, safety stocks, planning horizons, and reordering policies. The computation talks back through **action and exception messages** — suggestions to create, increase, reduce, expedite, postpone, or cancel supply orders, and warnings when something unusual happened, such as stock going negative, a safety stock violation, or a proposed change to an order already released. These messages, plus color-coded plan states, are the planner's steering wheel.

```text
Customer orders + forecast + stock policies      (the demand picture)
        ↓ net against
Stock on hand + open production/purchase orders  (the supply position)
        ↓ explode through
Build definitions (BOMs, operations)             (how things are made)
        ↓ time-phase across the horizon
Planned orders (make + buy)                      (the plan's working objects)
        ↓ planner firms
Production orders + purchase orders              (committed supply)
        ↓ schedule & release
Shop-floor execution                             (the boundary)
        ↑ completions and actuals feed the next run
```

## How It Works

### The planning run

The heart of the application is a recurring calculation:

```text
collect demand (orders, forecast, policies)
→ net against stock and scheduled receipts, period by period
→ explode net requirements through the build definitions
→ create time-phased planned production and purchase orders
→ place suggestions and warnings on the planner's worksheet
```

Products differ in how the run is triggered and scoped — a full recalculation of everything, an incremental run over changed items only, or an order-by-order pass for make-to-order demand — but the net-explode-time-phase shape is the same. The horizon has an end date; demand and supply beyond it are not considered.

### The planner's loop

The computed plan is a proposal. The planner reviews the worksheet or grid — usually exception-first, via warnings and highlighted cells — adjusts quantities and dates where judgment says so, and accepts suggestions. Accepting firms the planned orders into real production and purchase orders; firmed orders survive the next planning run instead of being regenerated. Some products emphasize this suggest-then-commit philosophy to the point of refusing to create anything automatically; others offer automatic triggers (reorder points, auto-created subassembly orders) as an option. Either way, a human decision point exists between the suggestion and the committed order.

### Scheduling and capacity

Committed production orders are placed on the production schedule with start and finish dates — derived from routings and lead times in the calculation, then adjustable by the planner on a calendar, Gantt chart, or prioritized list. Where drag-and-drop scheduling is offered, moving an order to a new time respects resource availability and material readiness; work already started is typically locked. Alongside the order schedule sit the capacity views: required hours per resource group per period against available hours, with overload and underload flagged, and the ability to simulate changed capacity or changed production quantities to see the effect before committing.

### Release and feedback

Released orders leave the planning world: they appear on execution surfaces where workers report consumption, output, and time. Completions flow back as scheduled receipts turned into stock, and progress against open orders keeps the supply position current — which is why the plan is re-run. The loop closes: demand changes, actuals arrive, the plan recomputes, the planner works the differences.

### Capability tiers

**Defining core** — without these, it is not production planning:

- the makeable planning model (items, build definitions, stock and supply position, planning parameters)
- the net-and-explode computation producing time-phased planned orders
- the planner's review-firm-release loop with re-planning

**Standard capabilities** — present in most mature products:

- production-order pipeline with statuses from planned to done
- scheduling surfaces (calendar, Gantt, or priority list) and forward/backward scheduling
- rough-cut capacity views (required vs available hours per resource group)
- action and exception messages; pegging between demand and supply; material booking from stock or planned supply
- make-to-order and make-to-stock order generation; forecast entry or linkage
- multi-level build structures, including subassemblies and kits

**Optional** — depends on product and segment:

- available-to-promise and delivery-date promising; what-if scenario simulation
- automation triggers (reorder-point order creation, automatic subassembly orders)
- subcontracting of operations; multi-site/multi-warehouse planning
- sales-forecast linkage and statistical forecast suggestions

## Interfaces

### Planning worksheet / master schedule grid

The planner's primary surface: the computed plan as actionable lines or a period grid. Lines show the item, the requirement that drove it, the suggested action, quantities and dates, and warning state; grid layouts show per-item-per-period rows — demand, planned supply, projected stock — with editable cells and suggestion indicators. Primary actions: run the calculation, filter to exceptions, adjust values, accept or carry out suggestions, drill into source documents.

### Production schedule

The committed orders on a time axis. Presentations vary — calendar, Gantt chart, or a prioritized queue — but the information is consistent: each order with its item, quantity, dates, resource, progress state, and material availability. Primary actions: reschedule (drag, rebook), change priority, open order details, view resource load. Views commonly split between orders and operations, and between the forward view of open orders and the archive of completed ones.

### Order detail

The single production order: its source (which demand generated it), build definition reference, component list with availability and reservations, operation list with dates and resources, and status. Primary actions: schedule or reschedule, book or release materials, change status, replan the order and its children.

### Capacity and load views

Required versus available hours per resource group per period, drawn from the plan; over- and under-load highlighting; manual overrides to simulate changed capacity. Read-mostly surfaces with simulation as their main action.

### Exception and warning surfaces

Lists and filters over what needs attention: safety stock violations, negative stock, orders needing date changes, materials that will not arrive in time, demand exceeding forecast. These are cross-cutting views over the plan rather than a separate module.

## Important Rules / Behaviors

- **Planned is not firm.** Planned orders are computed suggestions: a full re-plan typically regenerates or deletes them, while firmed orders — the ones the planner accepted — survive. Committed supply can be protected explicitly so the next run adjusts everything except it.
- **Capacity is checked, not solved, at this level.** The planning calculation commonly assumes resources can absorb the plan; capacity appears as rough-cut comparison views. Overload surfaced here is a signal to act — move demand, add shifts, or hand the problem to detailed scheduling — not an automatic rescheduling.
- **Exceptions expect human judgment.** Warning-class lines (negative stock, safety stock violations, proposed changes to released orders) are deliberately not auto-accepted; the planner is expected to investigate before acting. Noise dampeners keep trivial changes from generating messages.
- **Level timing matters.** Where order dates are computed from routings and lead times, component orders are timed to finish before their parents need them; a change to a parent cascades down the build structure, and a change to a component's date can invalidate the parent's promised date.
- **Materials gate the schedule.** Orders consume reserved materials; booking can draw on current stock or on planned supply arriving later, and scheduling tools check that materials will be there by the planned start. Some products prevent rescheduling work that has already started.
- **The current period belongs to actuals.** In period-grid planners, the nearest period typically reflects confirmed orders and in-progress work, with editable plan values starting from the following periods.
- **Suggestion vs automation is a posture, not a given.** Some products refuse to create orders without a planner's action; others create them automatically from reorder points or forecast triggers. Both are production planning; the difference is where the human decision sits.

## Variants

- **By production mode**: make-to-stock (plan against forecast and policies), make-to-order (plan against confirmed orders, order by order), and blends such as engineer-to-order, where the build definition itself is created per job.
- **By packaging**: a deep planning area inside a manufacturing ERP; a module of a modular business suite; a standalone MRP product for small manufacturers; a modern SaaS operations tool where planning is one screen among sales, purchasing, and stock. The same structures appear in all four packagings.
- **By planner surface**: worksheet-and-engine products (calculate, review lines, carry out), interactive period-grid products (edit the plan by hand, then commit), and queue-driven products (a single prioritized list of orders feeding the floor).
- **By automation posture**: suggest-only at one pole, automatic order creation at the other, with most products configurable in between.
- **By granularity and horizon**: daily buckets for near-term plans; weekly, monthly, or quarterly buckets for medium- and long-term plans; some products span several years of periods.
- **By industry vocabulary**: discrete assembly (BOMs and routings) and process/recipe production share the same planning structure under different names.
- **By scope**: single plant versus multi-site planning with per-location parameters and inter-site transfers.

A variant remains a variant unless it changes the core objects or the loop itself. Adding finite-capacity, operation-level scheduling optimization does exactly that — such products belong to a different type, however much their marketing says "production planning."

## Related Application Types

| Application Type | Distinction |
|---|---|
| Advanced Planning & Scheduling (APS) | assigns operations to finite-capacity resources in wall-clock time and lets planners edit the resulting detailed schedule; production planning nets and explodes demand into time-phased orders assuming effectively unlimited capacity. Suite vendors often bundle both and name the seam themselves (rough-cut vs detailed; "classic MRP" vs constraint-based scheduling) |
| Manufacturing ERP | owns the business record of production — orders, build definitions, inventory, costs — with planning as one capability among many; production planning centers the planning loop itself and may exist without the financial spine |
| Manufacturing Execution System (MES) | executes released orders at operation grain and produces the as-built record of what was actually made; production planning decides what and when ahead of time, at order grain, before release |
| Supply Planning | computes the network-wide supply response — what to buy, make, and move across locations and echelons; production planning owns the make-side plan inside the production domain, exploding through build definitions onto plant resources. The netting computation is shared machinery; the domain and object of record differ |
| Demand Planning | produces and works the forecast of record; production planning consumes forecasts as one requirements stream among orders and stock policies |
| Inventory Management System | records what is and what moved, with rule-triggered replenishment; reorder-point order creation is the thin shared edge — the explosion through build definitions and the production-order pipeline lie beyond it |
| Shop Floor Management | handles live floor events and responses (andon, dispatch, issues); production planning feeds the floor its schedule but does not manage the floor's running state |
| Manufacturing Supplier Collaboration | exchanges demand signals, schedules, and responses with suppliers; production planning computes internal plans that never leave the company unless shared |
| Bill of Materials Management / Engineering Change Management | governs the build definitions as engineering records over their lifecycle; production planning consumes whichever approved version is current |

## Representative Products

- Microsoft Dynamics 365 Business Central (manufacturing planning area)
- Odoo Manufacturing
- MRPeasy
- Katana

The core model was checked against the MRP and MRP II lineage and against spreadsheet-era planning practice, so the definition does not depend on any current packaging, engine, or interface style.

## Sources

Research date: **2026-09-09**

- Microsoft Learn — Dynamics 365 Business Central: "About planning functionality" — https://learn.microsoft.com/en-us/dynamics365/business-central/production-about-planning-functionality ; "Run Full Planning, MPS, or MRP" — https://learn.microsoft.com/en-us/dynamics365/business-central/production-how-to-run-mps-and-mrp
- Odoo documentation (official docs repository): "Master production schedule" — https://raw.githubusercontent.com/odoo/documentation/master/content/applications/inventory_and_mrp/manufacturing/workflows/use_mps.rst
- MRPeasy User Manual: Getting started — https://www.mrpeasy.com/resources/user-manual/ ; Production Schedule — https://www.mrpeasy.com/resources/user-manual/production-planning/production-schedule/ ; Master Production Schedule (MPS) — https://www.mrpeasy.com/resources/user-manual/settings/system/enterprise-functions/master-production-schedule-mps/
- Katana: "How to use the Make screen (Schedule)" — https://support.katanamrp.com/en/articles/5914378-how-to-use-the-make-screen-schedule ; Manufacturing collection — https://support.katanamrp.com/en/collections/3312515-manufacturing ; product root — https://katanamrp.com/
- Cross-referenced prior research in the same project: advanced-planning-scheduling-aps, manufacturing-erp, manufacturing-execution-system-mes, demand-planning, supply-planning, manufacturing-supplier-collaboration.

> Sourcing limitations: the enterprise-suite pole was not fetched directly (a major vendor's help portal is a script-only shell for automated access and its manufacturing pages returned errors), so enterprise-suite behavior is asserted only at pattern level, corroborated by that vendor's own public navigation wording. One SaaS sample's planning depth is documented at screen and collection level rather than full article level, and its claims are calibrated accordingly. No numeric limits, algorithm parameters, or plan-horizon defaults from any vendor are asserted in this document; vendor-specific mechanics remain in the paired Research Notes.
