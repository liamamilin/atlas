# Supply Chain Planning Platform

## Overview

A **Supply Chain Planning Platform** is an organization's forward-planning system for its supply network. It maintains a planning model of that network — the items, locations, and supply relationships an organization buys, makes, and moves through — and uses it to hold two connected, time-phased plans: a **forward demand plan** (what is expected to be needed, where, and when) and a **supply plan** derived from it (what to buy, make, and move in response). Planners review, adjust, and approve these plans in the system, and the resulting planned orders are released to execution systems such as ERP, procurement, and production.

The defining core is small:

```text
Planning model of the supply network
    └── Forward demand plan (time-phased, per item × location)
        └── Derived supply plan (planned buy / make / transfer orders)
            └── Planner review → release to execution
```

Everything else commonly associated with this category — statistical forecasting engines, safety-stock optimization, what-if scenarios, S&OP consensus processes, dashboards, AI demand sensing — is standard capability in mature products but is not what makes the product a supply chain planning platform.

The boundary is equally important: a planning platform **plans; it does not execute**. It does not receive goods, pick orders, ship freight, or post financial documents. It consumes data from systems of record (typically an ERP), produces the plan of what should happen next, and hands released orders back to the systems that execute. And it looks **forward**: where an inventory management system records what stock is and what moved, a planning platform maintains the expectation of what will be needed and the response to it.

## Users & Context

Primary users are planning professionals:

- **Demand planners** — own the forward demand plan: review statistical forecasts, apply market knowledge, adjust at item and group level, defend accuracy.
- **Supply planners / material planners** — own the supply response: review planned orders, balance stock against demand and capacity, decide what to release.
- **Inventory planners / planning analysts** — tune stocking policies, safety stock, and coverage parameters that translate demand into order quantities.
- **Planner-buyers** — in smaller organizations, one person often does all of the above and also places the purchase orders.

Secondary users:

- **S&OP process leads and supply chain managers** — run the periodic cross-functional reconciliation of demand, supply, and financial expectations.
- **Executives** — consume plan summaries, scenario comparisons, and KPI dashboards during S&OP cycles.
- **IT / integration administrators** — maintain the data connection to ERP and master-data quality, on which every calculation depends.

Typical context: manufacturers, distributors, wholesalers, and retailers with multiple locations and a real replenishment problem — enough items and locations that spreadsheet planning breaks. Work runs in a **rolling cycle**: plans cover a horizon extending weeks to months ahead, are refreshed as actuals arrive, and are revisited in weekly or monthly planning rhythms, with a periodic S&OP loop on top in larger organizations.

## Core Model

### The planning model of the supply network

The substrate on which everything is computed. It holds:

- **Items / SKUs** — the planned articles, with planning-relevant attributes (classifications, unit measures, costing where needed).
- **Locations** — the places stock is held, made, sold, or shipped from: plants, warehouses, distribution centers, stores.
- **Supply relationships and links** — which suppliers provide which items, which location supplies which (distribution links), and how components compose into finished goods (**bills of material**).
- **Planning parameters** — lead times, stocking policies, safety-stock targets, review frequencies, batch or lot sizes, capacity notes.

This model is the product's representation of the physical network. It is maintained continuously: items and locations change, BOMs change, lead times drift. Mature products treat keeping this model current as a first-class activity, because every downstream number inherits its quality.

### The forward demand plan

A time-phased expectation of demand, held per item and location across the planning horizon. It is:

- **Generated** — from sales history by statistical (increasingly machine-learned) forecasting methods.
- **Composed from multiple demand streams** — in a typical implementation, direct sales at a location, the supply required by downstream locations the location feeds, and the component usage implied by planned production of finished goods. The total demand for an item at a location is the sum of the streams that apply to it.
- **Human-shaped** — planners adjust forecasts at item or aggregate level; adjustments can be protected so that forecast regeneration does not overwrite them; one-off disruptions (a strike, a pandemic dip, a supplier shutdown) can be corrected out of the history so they do not distort the future.
- **Measured** — past forecasts are retained and compared against actuals, so forecast accuracy is a visible, managed number.

The demand plan is the "what will be needed" object. It is what separates this Type from replenishment logic that reacts to stock levels alone.

### The derived supply plan

The system's computed answer to the demand plan: **planned orders** — what to buy from suppliers, what to make, what to transfer between locations — positioned in time so that stock, lead times, safety stock, and review cycles are respected. Conceptually the supply plan is the demand plan translated through the network model:

```text
Demand plan (per item × location × period)
  + current/projected stock
  + stocking policies and coverage parameters
  + lead times, BOMs, supply links
  → planned orders (buy / make / transfer), time-phased
```

Implementations vary widely — from MRP-style netting of requirements to optimization engines that weigh service, cost, and capacity trade-offs — but the object is the same: a set of recommended, dated orders that together constitute the supply plan.

### The planner review loop and release

Planned orders are **recommendations, not commitments**. The planner inspects them, traces why each recommendation exists (the policy inputs and projections behind it), adjusts quantities and timing, and finalizes. Released orders leave the planning system — exported as files or transmitted directly — into the ERP, procurement, or production systems that turn them into real purchase orders, production orders, and transfers. The planning platform does not execute them.

### Standard capabilities around the core

Mature products commonly add:

- **Safety stock and inventory policy machinery** — service-level-driven stock targets; in enterprise products, multi-echelon optimization across the whole network.
- **Scenario analysis** — copy the plan, change an assumption (a demand spike, a supplier failure, a tariff), recompute, and compare outcomes before committing.
- **S&OP support** — the demand plan, supply plan, and financial expectations brought into one reconciled view for cross-functional consensus; rough-cut capacity checks; plan-vs-budget alignment.
- **Dashboards, KPIs, and exception flags** — forecast accuracy, stockout and excess risk, items whose forecasts or orders need attention.
- **ERP integration** — bidirectional: master data, stock, orders, and actuals flow in; released orders flow out.
- **Supplier monitoring** — lead-time actuals and supplier performance feeding the planning parameters.

### Concept vs implementation

The core model is conceptual; products realize it differently:

```text
Concept:  forward demand plan
Implementations:  statistical time-series forecasts, ML/demand-sensing models,
                  consensus forecasts shaped in S&OP, forecast + open-order blends

Concept:  derived supply plan
Implementations:  MRP-style netting, heuristic replenishment calculations,
                  optimization engines balancing service/cost/capacity

Concept:  release to execution
Implementations:  file export (CSV/spreadsheet), direct ERP transmission,
                  API integration
```

A reader who has only seen one implementation — say, a mid-market tool that exports recommended purchase orders to an ERP — should still be able to recognize an enterprise concurrent-planning suite as the same Type.

## How It Works

The canonical work of a supply chain planning platform is a **rolling loop**:

### 1. Connect and model

Data flows in from the ERP (or multiple ERPs): items, BOMs, stock on hand, open orders, sales history, suppliers. The organization's planning model is built and kept current — locations linked, BOMs verified, lead times and stocking policies set, items classified (for example, by velocity or criticality) so planning effort can be prioritized.

### 2. Generate and shape the demand plan

The system forecasts future demand per item and location from history. Planners review the forecast, focus on flagged exceptions, adjust where market knowledge contradicts the statistics, protect important adjustments from being regenerated away, and correct historical distortions after major events. In organizations running S&OP, the demand plan is also shaped by consensus: sales, marketing, and operations agree on one forward demand picture.

### 3. Derive the supply plan

From the demand plan, current and projected stock, and the planning parameters, the system computes planned orders — purchases, production, transfers — across the horizon. The same demand plan that drives finished-goods orders also drives component demand through the BOM, so raw materials are planned from the same forward picture.

### 4. Review, adjust, decide

Planners work through the recommendations: which suppliers and items need attention first, whether each recommended quantity makes sense given its policy context, what the projected stock position looks like over time. They use scenarios to test alternatives — pulling orders forward, changing a coverage policy, absorbing a demand spike — and compare the consequences before deciding. Trade-offs are explicit: service level against inventory cost against workload.

### 5. Release to execution

Approved orders are finalized and released — downloaded or transmitted to the ERP, where they become real purchase, production, or transfer orders. The planning system tracks what has been released and what is still pending.

### 6. Monitor and re-plan

Actuals flow back: sales, receipts, stock movements, supplier lead-time performance. KPIs and exception flags surface where reality diverges from plan — forecasts missing, orders aging unplaced, stockout or excess risk building. The horizon rolls forward, and the loop repeats.

### Capability tiers

- **Defining core** — network planning model; forward demand plan; derived supply plan; planner review and release to execution.
- **Standard in mature products** — statistical forecasting with accuracy measurement; safety-stock/policy machinery; scenario analysis; S&OP support; dashboards and exception flags; ERP integration; supplier monitoring.
- **Optional / variant** — multi-echelon inventory optimization; demand sensing and ML forecasting; DDMRP buffer management; deployment/allocation and available-to-promise; strategic network design; control-tower visibility; finite-capacity scheduling; execution modules (order management, transportation); retail merchandise planning; AI planning assistants.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Forecast workbench

The demand planner's home surface.

- Purpose: maintain the forward demand plan.
- Typical information: forecast per item × location × period, history, actuals, variance, accuracy measures, exception flags.
- Primary actions: adjust at item or group level, protect/revert adjustments, correct events, drill into demand streams, export/import for bulk work.

### Order / replenishment review screen

The supply planner's working surface.

- Purpose: review, adjust, and finalize planned orders before release.
- Typical information: recommended order quantities by item and supplier, urgency or risk indicators, policy context behind each recommendation, projected stock over time (opening/closing stock, demand, receipts, suggested order dates).
- Primary actions: filter and prioritize, create order schedules, adjust lines, apply top-up or target-filling logic, finalize, release/download, track release status.

### Supply plan / network view

The network-level view of the supply plan.

- Purpose: see the plan across locations, items, and time; spot imbalances.
- Typical information: planned supply vs demand by period, projected stock by location, capacity load indications, exception hotspots.
- Primary actions: drill down, rebalance, hand off to scenario analysis.

### Scenario manager

- Purpose: test alternatives before committing.
- Typical information: side-by-side scenario results (service, cost, inventory, capacity).
- Primary actions: copy a scenario, change assumptions, recompute, compare, promote a scenario to the working plan.

### S&OP / consensus views

- Purpose: reconcile demand, supply, and financial expectations across functions.
- Typical information: plan vs budget, volume and revenue views, rough-cut capacity, gaps and gaps-closed.
- Primary actions: align on one plan, record consensus decisions, hand the agreed plan to operational planning.

### Dashboards & KPIs

- Purpose: monitor plan health and planning performance.
- Typical information: forecast accuracy, stockout/excess risk, order book status, supplier lead-time drift.
- Primary actions: drill to exceptions, route to the responsible planner.

### Configuration & administration

- Purpose: maintain the planning model and access.
- Typical information: items, locations, BOMs, policies, classifications, users and roles, integration settings.
- Primary actions: configure policies and parameters, manage users, monitor data feeds.

## Important Rules / Behaviors

### Plans are time-phased and rolling

Everything is held in time buckets (typically weeks and months, finer near-term in some products). The horizon extends as time passes; each cycle re-plans from updated actuals. A plan is never "done" — it is a standing, revisable expectation.

### Recommendations age

A planned order is a snapshot of inputs at the moment it was computed. If it is not released promptly, demand, stock, and forecasts have moved on — the researched sample documents this staleness hazard explicitly, with products flagging unplaced orders and making regeneration from current data easy. Treat it as an operational hazard, not an edge case.

### Human adjustments can be protected

Forecast adjustments made by planners can be locked so that automatic regeneration does not erase them, and reverted when no longer wanted. The system thus distinguishes statistical output from human judgment — a structural feature, not a convenience.

### The demand plan drives the supply plan

The supply plan is derived, not independent: change the demand plan and the supply plan follows. In products built around this dependency, a change anywhere in the network propagates through the linked plans — the philosophy some enterprise platforms call concurrent planning. Even in batch-oriented products, the derivation order (demand → requirements → orders) is fixed.

### Coverage parameters become quantities through the forecast

Lead times, safety stock, and review cycles are held as time parameters and converted into units via the demand plan. If the forecast is wrong, the "right" policies still produce wrong orders — which is why forecast quality and policy quality are managed together.

### Planning and execution are separated

The planning platform recommends and releases; ERP/procurement/production execute and record. Released orders are tracked for confirmation; the planning system does not own the executed transaction. This separation is why ERP integration is structural: without the data feed and the release channel, the platform cannot operate.

### Exceptions are first-class work

Disruptions (demand shocks, supplier failures), excess stock, stockout risk, and stale orders are surfaced as managed exceptions with correction paths — for example, correcting one-off events out of forecast history, redistributing excess between locations, or ranking pending orders by urgency — rather than left to be discovered in reports.

## Variants

Common forms of the Type:

- **Enterprise concurrent-planning platforms** — whole-network models with real-time propagation of changes across demand, supply, inventory, and financial views; scenario analysis as the central interaction; typically global manufacturers.
- **Integrated business planning (IBP) suites** — the same planning core packaged with an explicit S&OP/IBP process layer that integrates financial planning views; often deployed by large enterprises standardizing on one planning stack.
- **Mid-market / enterprise planning suites** — broad module portfolios (demand, inventory optimization, supply, deployment, network design, manufacturing) sold as an end-to-end planning platform.
- **SMB replenishment-centric planning** — demand forecasting + stocking policies + recommended orders, tightly wrapped around one ERP; the planner-buyer reviews and releases orders in a short loop. The planning core is identical; the machinery is lighter.
- **MRP-centric manufacturing planning** — forecast-driven material requirements planning with make-to-stock/make-to-order handling and batch logic, positioned as the replacement for spreadsheet MRP.
- **Industry flavors** — retail/merchandise planning (seasonal, category-level), food & beverage (shelf-life, batch), process manufacturing, service parts; the core model holds, the parameter and forecast machinery specializes.
- **Deployment shape** — cloud SaaS is the current dominant delivery; historically on-premise and desktop products satisfied the same core.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Demand Planning | capability slice | produces the forward demand plan; the platform holds demand **and** the derived supply plan and the network model that joins them |
| Supply Planning | capability slice | produces the supply response; the platform integrates it with demand and the reconciliation loop |
| Advanced Planning & Scheduling / APS | adjacent, module-level overlap | APS assigns operations to finite capacity at operation-level time detail (schedulable shop sequences); supply chain planning works at bucketed, network level. Scheduling modules inside planning suites are APS territory |
| ERP | system of record vs system of forward plan | ERP records transactions and computes replenishment-level (MRP-style) plans on its transactional core; the planning platform adds forecast depth, optimization, scenarios, and network-wide reconciliation, consuming ERP data and releasing plans back |
| Inventory Management System | record vs plan | IMS holds stock records of what is and what moved; planning holds what will be needed. Replenishment suggestions can ride on IMS data; the forecast-driven network plan is the planning side |
| Warehouse / Transportation Management | downstream execution | WMS/TMS execute the storage and movement that the supply plan calls for; they do not compute the plan |
| Supply Chain Control Tower / visibility | observe vs decide | visibility platforms watch actuals and alert; planning platforms decide the future. Control-tower modules appear inside planning suites as optional layers |
| Financial Planning & Analysis | reconciled, not owned | S&OP reconciles demand/supply with financial targets, but the financial plan of record stays with FP&A; the planning platform owns quantities |
| Supplier Risk Management | risk vs plan | risk platforms monitor and evaluate the supplier base; planning platforms consume lead times and produce orders. Risk insight may feed planning parameters; the objects differ |

The closest structural neighbors are the two sibling leaves, Demand Planning and Supply Planning: in the market, standalone products exist for each slice, but the dominant product shape is the integrated platform that holds both plans and the network model in one reconcilable whole. The directory carries all three as separate leaves; this is flagged for joint review.

## Representative Products

- **Kinaxis (Maestro / RapidResponse)** — enterprise concurrent planning; whole-network model with real-time change propagation and scenario analysis.
- **SAP Integrated Business Planning (IBP)** — enterprise IBP suite: demand, response & supply, inventory, S&OP, DDMRP on a cloud planning core.
- **Logility** — end-to-end planning suite: demand, inventory optimization (MEIO), supply, deployment, S&OP/S&OE, network design.
- **GMDH Streamline** — SMB/mid-market integrated demand and inventory planning with MRP-style supply planning over ERP data.
- **Netstock** — SMB/mid-market supply and demand planning centered on forecasting, stocking policies, and recommended-order review, integrated with mid-market ERPs.

The defining core was checked against older and thinner shapes: MRP-era systems (item/BOM/inventory master data, master schedule from forecast, time-phased planned orders, planner action messages) and spreadsheet-era S&OP both satisfy the core without any modern machinery; paper-era reorder-point planning without a forward demand plan does not, and is treated as the thin ancestor rather than a member of the Type.

## Sources

Research date: **2026-09-08**

Official sources used:

- Netstock Help Center (operational documentation): https://help.netstock.com/en/ — including the Forecasting and Ordering & Replenishment collections and the articles "Understanding Order Creation and Review", "Demand Streams Explained: Sales, Distribution, & BOM", "Mastering Forecasting"
- Kinaxis: https://www.kinaxis.com/en , https://www.kinaxis.com/en/our-technique-concurrency , https://www.kinaxis.com/en/solutions/supply-planning
- SAP Integrated Business Planning: https://www.sap.com/products/scm/integrated-business-planning.html
- Logility: https://www.logility.com/ , https://www.logility.com/solutions/scenario-planning/sop/
- GMDH Streamline: https://gmdhsoftware.com/ , https://gmdhsoftware.com/solutions/manufacturing/

> Sourcing limitation: operational (Tier-1) documentation was directly accessible only for Netstock; Kinaxis and Logility detailed documentation is login-gated, SAP's help portal renders as a JavaScript-only shell, and GMDH Streamline's documentation paths were unreachable. Enterprise-product behavior is therefore described at process level from official product and solution pages, not at UI level, and no precise vendor-specific figures, defaults, or limits are asserted. Product-by-product observations, the cross-product comparison matrix, and the abstraction record are kept in the paired Research Notes.
