# Supply Planning

## Overview

A **Supply Planning** application is an organization's supply-response planning system: it maintains the time-phased plan of what to buy, make, and move — across the supply network, against anticipated demand — and hands that plan to execution systems.

Where demand planning answers *"what will customers need?"*, supply planning answers *"what must we do about it?"* It takes a forward demand picture as its target, computes the supply actions that satisfy it under real-world constraints (lead times, minimum order quantities, safety stock, capacity), and produces planned orders that planners review, adjust, and release to procurement, production, and warehouse systems.

The defining structure is small:

```text
Supply-side planning model (items × locations × supply sources, with parameters)
└── Demand requirements to satisfy (time-phased, forward-looking)
    └── Supply plan of record (planned buy / make / move orders)
        └── Planner review → release to execution
```

The application plans; it never executes. A planned order is a recommendation until it is released, at which point it becomes a real purchase, production, or transfer order in the execution system. When the dominant surface shifts to producing the forecast itself, the product is drifting toward Demand Planning; when it spans demand, supply, and consensus reconciliation in one model, it is a Supply Chain Planning Platform.

## Users & Context

The primary user is the **supply planner** (in smaller organizations, the purchasing/buying role wearing the planner hat): the person responsible for ensuring materials and goods arrive where they are needed, on time, without excess stock.

Typical work:

- review the system's order recommendations and decide what to release
- investigate exceptions — shortages, late supply, items that will run out before the next delivery
- adjust plans when reality diverges from the forecast (promotions, disruptions, supplier problems)
- maintain the planning parameters that drive the calculations (lead times, policies, supplier constraints)

Secondary users:

- **inventory planners / S&OP participants** — align the supply plan with financial and demand plans at aggregate level
- **supply chain managers** — oversee service, inventory, and cost trade-offs across the network
- **buyers / procurement** — receive released purchase recommendations and turn them into orders

The work environment is a planning desk on top of ERP data: the application continuously imports master data, stock positions, and open orders from the ERP, and exports released orders back. Planning runs on a cadence — typically a daily or weekly review cycle per supplier or planning group, with the plan recomputed whenever inputs change.

## Core Model

### The Defining Core

Three structures, held together. Remove any one and the product stops being supply planning:

- **The supply-side planning model** — the organization's items/SKUs, locations, and supply sources: which suppliers provide which items, which plants make which products (via bills of material), which locations supply which others (distribution links). Each link carries planning parameters: lead times, lot sizes, minimum order quantities, order multiples, safety-stock and stocking policies, capacity parameters. This model is the substrate every plan is computed on. Without it there is nothing to plan against — just an order calculator.
- **The demand requirements it must satisfy** — a time-phased, forward-looking picture of what will be needed, where, and when, over the planning horizon. It is composed from multiple demand streams: the forecast (typically produced in demand planning and imported or maintained here), open customer orders, downstream distribution requirements (what branch warehouses need supplied), and component requirements (what production will consume, derived from bills of material). Without a forward demand picture, only history-triggered replenishment remains — inventory-management territory, not planning.
- **The supply plan of record** — the time-phased set of planned orders: what to **buy** (purchase orders), what to **make** (production orders), what to **move** (transfer orders), in what quantities, for which items, at which locations, in which periods. It is computed by netting demand requirements against the current stock position and in-transit/on-order supply, under the planning model's policies and constraints. Planners review and adjust it, then release it to execution systems. Without it, the product is a forecast archive with no supply response.

### The Central Object: the Planned Order

The planned order is the unit of the supply plan. It carries:

- item and quantity
- source (supplier, production line, or supplying location)
- destination location
- suggested timing (order date / delivery date, driven by lead time)
- status: **planned** (a recommendation) → **firmed/released** (an execution order)

Everything in the application ultimately exists to generate, justify, adjust, and release planned orders.

### The Netting Calculation

The engine's core question, per item × location × period, is: *what supply actions are needed so that projected stock covers projected demand?* The general shape:

```text
Projected stock = on hand − commitments (allocations, back orders)
                + on order / in transit
                + planned orders

If projected stock falls below the policy target
(safety stock + expected demand during lead time)
→ a planned order is generated to restore coverage
```

The exact mathematics vary widely — from reorder-point-style coverage targets to full multi-level optimization — but every implementation nets demand against supply position under policies. Two details matter in practice:

- **The stock position is not the shelf count.** Committed stock (allocated to orders, back-ordered) reduces what is available; incoming supply (open orders, in-transit) adds to it. Planning runs on this net position.
- **Constraints reshape the ideal answer.** Minimum order quantities, order multiples, batch sizes, and supplier calendars can raise a recommended quantity above the mathematically ideal one. The plan is what is *feasible*, not what is *perfect*.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. Implementations realize each concept differently:

```text
Concept:            Planned order
Implementations:    purchase order recommendation, manufacturing order,
                    transfer/deployment order

Concept:            Demand requirements
Implementations:    statistical forecast, demand-sensed forecast, open sales
                    orders, distribution requirements, BOM component explosion

Concept:            Policy target
Implementations:    safety stock in days or units, service-level-driven targets,
                    reorder point / order-up-to level, DDMRP buffers

Concept:            Engine
Implementations:    MRP-style netting rules, coverage-target calculations,
                    constraint-based optimization
```

## How It Works

### The planning loop

```text
Maintain the planning model
(items, locations, suppliers, BOMs, lead times, policies)
→ Refresh inputs
(demand requirements, stock position, open supply orders)
→ Compute the supply plan
(net requirements → planned buy/make/move orders)
→ Planner review
(exceptions first → validate → adjust with justification)
→ Release
(firm planned orders → purchase/production/transfer orders in the ERP)
→ Monitor and re-plan
(actuals flow back; the plan recomputes; exceptions re-surface)
```

The loop repeats on a cadence — daily or weekly per planning group — and re-runs whenever inputs change materially.

### Compute the plan

For each item × location, the engine projects stock forward across the horizon: demand arrives (from all demand streams), supply arrives (open orders on their lead times), and whenever projected coverage falls below policy, a planned order is generated — sized to restore coverage, rounded to lot rules, timed by lead time. For manufactured items, component demand explodes down the bill of material, generating planned orders for materials in turn. The output is a full time-phased plan across the network.

### Review the plan

The planner's review is a judgment pass, not a rubber stamp. The typical sequence:

1. **Orient** — scan the plan at aggregate level (per supplier, per location, total value and volume). If it looks fundamentally wrong, the inputs are wrong; fix them before touching lines.
2. **Prioritize** — sort by value, quantity, shortage risk, or urgency rating; review effort goes where impact is greatest.
3. **Validate** — open the item's projection (time-phased stock, demand, receipts, planned orders) and confirm the recommendation makes sense against policy and forecast.
4. **Adjust only with justification** — legitimate adjustments are execution decisions (consolidating small orders, filling containers, reaching discount thresholds). Problems with inputs — wrong lead times, stale forecasts, missing promotions — are corrected at the source, not overridden line by line. Repeated manual overrides on the same item signal an upstream data or policy problem.
5. **Finalize** — review a summary of system recommendations versus amended quantities, then release.

### Release to execution

Released planned orders leave the planning world and enter the execution world: purchase orders to procurement, production orders to manufacturing, transfer orders to warehouses. Mature products support the handoff — exporting order files for ERP upload or sending orders directly — and some surface status tracking of what has been downloaded and actioned. Stale, unreleased recommendations are treated as suspect — the plan ages as inputs change, so old recommendations are archived and regenerated rather than reused.

### Core vs Common vs Optional

**Defining core** — without these, not supply planning:

- supply-side planning model with parameters
- forward demand requirements as the plan's target
- time-phased planned orders (buy/make/move) computed by netting
- planner review and adjustment
- release to execution systems

**Standard capabilities** — present in most mature products:

- safety-stock / stocking-policy machinery
- supplier constraint handling (MOQs, order multiples, lead times)
- exception alerts and prioritization
- what-if scenario analysis
- ERP integration in both directions
- dashboards and KPIs (projected stock, service risk, order value)
- rough-cut capacity checks (enterprise products)

**Optional / variant** — depends on segment and philosophy:

- multi-echelon inventory optimization
- probabilistic, service-level-driven policy setting
- DDMRP buffer management
- response management / short-horizon deployment and allocation
- supplier collaboration portals
- finite-capacity scheduling (crosses into the APS Type)
- AI-era assistance (demand sensing, AI trade-off analysis, agentic execution)

## Interfaces

The following surfaces are described conceptually. Exact layouts and names vary by product.

### Order recommendations / supply plan screen

The central working surface.

- lists planned orders grouped by source (suppliers, distribution centers, internal locations) with quantities, dates, and urgency
- primary actions: filter and sort (value, shortage risk, urgency), open an order schedule for review, create orders

### Order schedule review

The line-level review surface for one order (one supplier or source, one cycle).

- order lines with recommended quantities, policy context behind each recommendation, and projection previews
- primary actions: adjust quantities, add top-up lines, consolidate, run target-seeking helpers (hit a value/volume/container target), finalize

### Item inquiry / projection

The time-phased diagnostic view for a single item × location.

- opening and projected stock, demand by stream, scheduled receipts, planned orders, safety stock, lead-time demand
- primary actions: inspect why a recommendation exists, trace the effect of a change — the surface planners use to justify or reject a recommendation

### Planning model maintenance

Configuration surfaces for the substrate: items and their stocking classes, locations, suppliers and their constraints (lead times, MOQs, multiples), bills of material, distribution links, policies.

### Exception / alert views

Surfaces that surface what needs attention: items projected to run out, late supply, recommendations that violate constraints, forecasts needing attention.

### Scenario / what-if views (enterprise)

Side-by-side plan variants under changed assumptions (demand shifts, supplier loss, capacity changes), with trade-off comparison across service, cost, and inventory.

### Dashboards

Aggregate views of projected service risk, inventory levels, order values, and planner workload.

### Release / export surface

The handoff to execution: export order files for ERP upload or send orders directly, with status tracking of what has been downloaded and actioned.

## Important Rules / Behaviors

### A planned order is not an order

Recommendations carry no commitment until a planner firms and releases them. This separation is the structural boundary between planning and execution, and it is why review-and-release is a defining workflow rather than an administrative step.

### The plan runs on net stock, not shelf stock

Allocations, back orders, and on-order supply all change the position the engine plans from. Reviewing only physical stock leads to wrong conclusions about why an order was (or was not) recommended.

### Constraints beat ideals

Minimum order quantities, order multiples, and batch sizes can push recommended quantities above the ideal calculation. Unexpectedly large orders usually trace to a constraint, not an error.

### The plan ages

Recommendations are computed from inputs at a point in time. As demand, stock, and supply change, unreleased recommendations become stale. Some products snapshot recommendations when created and flag outdated ones; the underlying behavior is universal — stale recommendations are archived and regenerated rather than reused.

### Fix inputs at the source

Adjusting the same item's orders repeatedly indicates an upstream problem — a wrong lead time, a stale forecast, an overstated safety stock. Vendor planning guidance in this category is explicit on the point: correct the model or policy at the source rather than habitually overriding recommendations.

### Timing risk is separate from quantity risk

A quantity can be right while its delivery timing still creates a stockout. Lead-time accuracy is as load-bearing as demand accuracy.

### Item classes change planning behavior

Stocking class matters: actively stocked items, non-stocked items, and obsolete items can follow different planning logic — in some products, for example, non-stocked items are ordered only against an actual deficit, and obsolete items receive no recommendations at all. Classification is a planning input, not just a report filter.

## Variants

Common shapes of the Type:

- **Enterprise network planning** — constraint-aware, scenario-heavy supply planning inside integrated platforms; multi-echelon optimization; S&OP integration (e.g. Kinaxis, SAP IBP)
- **MRP-style netting** — bill-of-material explosion and planned-order generation, embedded in ERP or standalone; the historical core of the Type, still the dominant implementation inside ERPs
- **Replenishment-centric (SMB)** — forecast-driven ordering recommendations per supplier cycle, released to the ERP; the dominant standalone shape for distributors and wholesalers (e.g. Netstock)
- **Probabilistic / inventory-optimization** — service-level-driven safety stock and multi-echelon optimization as the center of gravity (e.g. ToolsGroup)
- **Response / short-horizon** — deployment, allocation, and available-to-promise over days rather than weeks; packaged inside supply or response modules
- **Industry flavors** — manufacturing (BOM depth, make-to-order vs make-to-stock, batch rounding), distribution/wholesale (purchasing focus), retail (allocation and replenishment to stores)

A variant remains a variant unless it changes the core users, objects, or workflow — finite-capacity shop-floor scheduling, for example, changes the object (operations on resources, not network orders) and belongs to the APS Type even when sold inside a planning suite.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Demand Planning | produces the forecast (what will be needed); supply planning consumes it and produces the response (what to buy/make/move). The demand plan is supply planning's input, not its record of record |
| Supply Chain Planning Platform | the integrated whole — network model, demand plan, supply plan, and S&OP consensus in one reconcilable system; supply planning is the supply-domain application that also exists standalone |
| Inventory Management System | records what stock is and what moved, with rule-triggered replenishment; supply planning holds the forward time-phased plan. Remove the forward demand picture and supply planning collapses into IMS |
| Production Planning / APS | assigns operations to finite capacity at operation-level time inside the plant; supply planning produces aggregate, bucketed, network-level orders |
| ERP | transactional system of record; executes released orders. ERP-embedded MRP is the replenishment-level ancestor of this Type's logic; dedicated supply planning adds forecast depth, network scope, and scenario work |
| Purchase Order Management / Procurement | executes buying (POs, suppliers, receiving); supply planning decides what and when to buy before any PO exists |
| WMS / TMS | execute the movement of goods; supply planning only plans what should move |
| S&OP | the cross-functional consensus process reconciling demand, supply, and financial views; supply planning feeds it the supply-side view |
| Control Tower / Visibility platforms | observe actuals and alert; supply planning decides the future |

The two most important boundaries: against **Demand Planning** (forecast-producing vs forecast-consuming — the same vendors sell both as separate categories), and against the **Supply Chain Planning Platform** (the platform holds demand and supply plans together under consensus; standalone supply planning holds the supply response and imports the demand picture).

## Representative Products

- Kinaxis (Maestro / RapidResponse) — enterprise concurrent planning; supply planning as a named application
- SAP Integrated Business Planning (IBP) — enterprise suite; Response and Supply Planning module
- ToolsGroup — mid-market probabilistic planning; supply planning as inventory optimization + replenishment
- GMDH Streamline — SMB standalone demand + MRP-style supply planning
- Netstock — SMB/mid-market ERP-companion replenishment planning

The defining core was checked against the historical MRP pattern (item/BOM/inventory master + master schedule + time-phased planned orders + planner action messages) and the spreadsheet-era planning shape to avoid over-fitting to modern optimization platforms.

## Sources

Research date: **2026-09-08**

Primary vendor surfaces:

- Kinaxis — Supply Planning solution page — https://www.kinaxis.com/en/solutions/supply-planning
- SAP — Integrated Business Planning product page and FAQ — https://www.sap.com/products/scm/integrated-business-planning.html
- ToolsGroup — solution navigation (Supply Planning category) — https://www.toolsgroup.com/
- GMDH Streamline — Manufacturing solution page — https://gmdhsoftware.com/solutions/manufacturing/
- Netstock Help Center — Ordering & Replenishment collection, ROQ calculation and order-schedule review articles — https://help.netstock.com/en/collections/18733735-ordering-replenishment

> Sourcing limitation: operational help-center documentation was directly reachable only for the SMB-pole product (Netstock). Enterprise vendors' detailed documentation is login-gated or JS-shell (SAP Help Portal, Kinaxis knowledge base); GMDH Streamline's webhelp and Microsoft Learn's Dynamics 365 master-planning pages were unreachable from the research environment. Enterprise behavior is therefore described at process level, not UI level, and no precise vendor figures, defaults, or algorithm parameters are asserted. Detailed evidence and per-product observations are recorded in the paired Research Notes.
