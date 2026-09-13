# Research Notes — Advanced Planning & Scheduling / APS

## Research Goal

Understand from real products what an Advanced Planning & Scheduling (APS) application actually is and how it works: its core objects, how a production schedule is produced, how planners interact with it, how it connects to ERP/MES, and where its boundary lies against Production Planning, MES, Manufacturing ERP, and generic resource-scheduling Types.

## Initial Boundary (hypothesis before research)

- Core use: generate executable production schedules for finite-capacity factory resources (machines, work centers, labor, tooling) under constraints (capacity, calendars, setup/changeover, materials, due dates), and let a planner inspect/adjust/regenerate that schedule.
- Likely users: production planners / schedulers / master schedulers; plant management secondary; IT/integration staff for connections.
- Nearest neighbors: Production Planning (MRP-style, bucketed, often infinite capacity), Supply Planning / Demand Planning, MES (execution recording), Manufacturing ERP (system of record), Shop Floor Management, Resource Calendar / Enterprise Resource Scheduling (generic booking), Construction Scheduling (project domain).
- Unknowns: how deep material feasibility goes; whether "optimization" is definitional or optional; whether older 1990s finite-capacity schedulers fit the same definition; suite vs standalone packaging.

## Research Questions

1. What objects exist (order/job, operation, resource, calendar, constraint, schedule) and how do they relate?
2. How is the schedule generated — finite capacity, forward/backward, rules, optimization objectives?
3. What input data is required (orders, routings/operations, calendars, inventory, setup rules)?
4. How does the planner interact with the generated schedule (Gantt editing, manual assignment, what-if)?
5. How does the schedule reach execution (dispatch lists, publish back to ERP/MES)?
6. What is Common vs Optional (setup matrices, material feasibility, alternates, skills, multi-plant)?
7. Where are the boundaries vs Production Planning / MES / ERP / generic scheduling?
8. Historical check: do 1990s-era finite-capacity schedulers (e.g. Asprova since 1994, Preactor lineage) fit the definition?

## Representative Products

| Product | Vendor type | Why selected | Docs quality reached |
|---|---|---|---|
| PlanetTogether APS (CAI) | dedicated US APS vendor, mid/large manufacturers | dedicated APS positioning, very explicit process description | Tier 2 (product/education pages; support KB gated) |
| Asprova | dedicated Japanese APS vendor (since 1994), strong in Asia | regional leader, module-split architecture, detailed feature pages; historical depth | Tier 2 (product pages; online help login-gated, KB unreachable) |
| frePPLe | open-source planning/scheduling vendor, SMB-friendly | fully public Tier-1 docs: data model, UI screens, workflows | Tier 1 (model reference, user interface, day-in-the-life) |
| Siemens Opcenter APS (ex-Preactor) | industrial-suite vendor | intended as suite-vendor + 1990s FCS lineage sample | **not reachable** (two 404s on official hosts) — dropped per source-access rules |

## Sources

- frePPLe 9.19 documentation: https://frepple.com/docs/current/ (index); /docs/current/a-day-in-the-life/index.php; /docs/current/model-reference/; /docs/current/model-reference/domain-model.php; /docs/current/user-interface/; /docs/current/user-interface/plan-analysis/plan-editor.php
- PlanetTogether: https://www.planettogether.com/ (root); /aps-software/what-is-advanced-planning-scheduling
- Asprova: https://www.asprova.com/en/ (root); /en/asprova/asprova_ms.html; /en/asprova.html; /en/asprova/equipped_with_advanced_and_highly-flexible_scheduling_logic.html
- Attempted, failed: https://plm.sw.siemens.com/en-US/operations-management/opcenter-aps/ (404); https://www.sw.siemens.com/en-US/products/operations-management-software/opcenter-aps/ (404); http://lib.asprova.com/onlinehelp/en/AS2003HELP00001000.html (login wall); https://knowledge.asprova.com/hc/en-us (transport error)

Research date: 2026-09-06.

## Product A — frePPLe (open source; Tier 1 evidence)

### Key observations (Layer A, directly observed)

- **Data model (model reference + domain model)**: entities with documented dependency order — customers, setup matrices, skills, calendars/calendar buckets, locations, suppliers, **resources**, items, **operations**, sales orders, buffers, operation dependencies, **operation resources**, **operation materials**, resource skills, setup rules, **manufacturing orders**, purchase orders, distribution orders, inventory detail, resource detail.
- **Operation types**: fixed time, time per, alternate, split, routing — i.e. an order's work is modeled as operations, optionally chained as a routing, with alternates.
- **Resource types**: default, time-buckets, quantity-buckets, **infinite** — capacity is modeled per resource; calendars supply availability; skills link workers to operations.
- **Production planner workflows ("day in the life")**: update plan when a machine breaks down; reassign a manufacturing order's resource; identify orders to expedite; prioritize a sales order; enter operator shifts/holidays; review late orders; track bottleneck resources; review **unconstrained capacity requirements** vs constrained plan; measure rush-order impact; "optimize my plan in the GANTT chart plan editor"; review critical items. Material planner workflows: approve MO/PO/DO, stockout risk, excess inventory.
- **Plan editor (Gantt)**: interactive chart over resources / sales orders / item inventory; drag a manufacturing order to a new date; edit quantity/dates/status; assign to an **alternate resource**; interactive replanning of sales orders: *unplan* (removes plans; only manufacturing orders in 'proposed' status can be removed), *backward planning* (deliver as close to due date as possible), *forward planning* (ASAP). Color schemes: by feasibility (capacity overload, material shortage, lead-time constraints), criticality (critical path), delay, priority, inventory status. Explicit permission list (change/create/delete operationplan; view resource/demand/buffer/location).
- **What-if scenarios**: separate scenario copies of the model with their own access rights.
- **Screen set**: home/cockpit, plan analysis (plan editor, problem report, **constraint report**, resource reports, order summaries), execution screen, report manager.

## Product B — PlanetTogether (dedicated APS; Tier 2 evidence)

### Key observations (Layer A for structure, from official pages)

- **Vendor definition**: APS "helps manufacturers create realistic production schedules around capacity, materials, labor, routings, changeovers, setup times, and due dates"; "checks the schedule against real manufacturing constraints... see whether work can actually run on available machines, crews, materials, and work centers before committing to dates."
- **Five-step flow (official)**: 1) pull master data from ERP or Excel; 2) "determine what a good schedule means" — optimization factors weight a rules engine; 3) generate the optimized schedule; 4) manual adjustments (machine offline, expedite an order); 5) **publish** the schedule / send scheduling data back to ERP so the shop floor can act.
- **ERP/MRP/MES/APS table (official)**: ERP manages business records; MRP plans materials; MES tracks execution; "APS acts as the scheduling layer"; APS does **not** replace ERP. Inputs from ERP (orders, inventory, routings, items, due dates), MRP (demand, material requirements), MES/shop floor (status, completions, downtime), WMS/inventory (availability), labor systems (shifts, skills, crews). Outputs back: updated schedules, planned start/finish dates, resource assignments, sequencing updates, constraint alerts, production priorities.
- **Data needed (official list)**: orders/demand/due dates; materials & inventory; routings & work centers (machines, lines, tools); capacity & calendars (shifts, downtime, holidays, maintenance); setup & changeover rules (sequence-dependent changeovers, cleaning, batch/allergen/campaign rules); shop-floor status.
- Use-case framing: daily production scheduling, finite capacity scheduling, capacity visibility, schedule optimization; industries discrete + process (chemical, food, pharma, aerospace, packaging...); multi-site framing.

## Product C — Asprova (regional leader since 1994; Tier 2 evidence)

### Key observations (Layer A for structure, from official pages)

- **Positioning**: "APS system that creates production schedules at high speed for multiple items and multiple processes, fully integrating sales, manufacturing, inventory and purchase plans"; finite capacity scheduling at "ultra-high speed"; visual management showing "the schedule stretching from the current state of the shop floor to several months in the future."
- **Module split (official)**: Asprova APS (mid/long-term planning), **Asprova MS = "short term scheduler — create detailed schedules using FCS"** (finite capacity scheduling), MS Light, Asprova MRP (separate module), **Asprova SED (schedule editor)**, Asprova MES, BOM, NLS/DS, SCM. Options: Resource Lock, Time Constraint Max, Event, Group Assign, Optimization, Sales, Purchase, KPI.
- **MS scheduling features (official)**: external setup; time constraints between processes (ESE, EES, ESSEE, SSEEE); pegging methods (N-to-N, 1-to-1, inventory+1-to-1); inventory expiration date; synchronization of short-term with mid/long-term schedules; parametric BOM; **skill map** (worker skills matrix used in scheduling).
- **Scheduling logic list (official)**: automatic task division; load-leveling allocation; resource prioritization; workers/jigs/molds settings; merging/branching allocation; batch-furnace grouping; setup-time minimization item summaries; raw-material restrictions by time period with linked inventory and safety stock; **forward/backward allocation with buffer time**; **dispatch settings allocating by priority**; skill charts; automatic order supplementation (replenishment) considering inventory; lot summarization; automatic order linking; extensive setup-time customization (off-time setup, setup switching, pre/post-setup processes); simulations with several parameters.
- Historical depth: "since its introduction in 1994" (22 years at page publication) — a 1990s-generation finite-capacity scheduler still in the same product family.

## Cross-product Comparison

| Structure | frePPLe (A) | PlanetTogether (A) | Asprova (A) | Verdict |
|---|---|---|---|---|
| Production orders / manufacturing orders as schedulable jobs | yes (MO entity) | yes (work orders, customer orders) | yes (orders, order supplementation) | Core |
| Order decomposed into operations/steps bound to routings | yes (operation entity, routing subtype) | yes (routings, routing steps) | yes (processes, merging/branching, parametric BOM) | Core |
| Finite-capacity resources with calendars/shifts | yes (resource + calendar + skills; "infinite" resource only as modeling exception) | yes (machines, crews, work centers, shift calendars, downtime) | yes (FCS explicitly; resource capacity master data) | Core (the differentiator vs MRP) |
| System computes a time/resource assignment (the schedule) | yes (plan; constrained planning) | yes (step 3, optimized schedule) | yes (FCS output schedule) | Core |
| User-visible, editable schedule (Gantt) | yes (plan editor: drag, edit, recolor) | yes (scheduling board; manual adjustments step 4) | yes (visual management; SED schedule editor module) | Core as "user-visible adjustable schedule"; Gantt specifically = common presentation |
| Replan loop on events (breakdown, rush order, priority change) | yes (machine-breakdown workflow, expedite, prioritize) | yes (step 4; "respond faster to change") | yes (simulations, rescheduling) | Core |
| Integration in (orders/routings/inventory) and out (schedule/priorities) | yes (ERP integration guide, Odoo connector; approve & export) | yes (5-step data in → publish out) | yes (differential data import/export; linkage packages) | Core as data pattern; exact mechanism varies |
| Proposed vs firm/locked schedule elements | yes ('proposed' status; only proposed can be unplanned) | yes (manual adjustments then publish) | yes (Resource Lock option) | Common |
| Forward / backward scheduling modes | yes (plan editor commands) | implied by "checks each job against..." (not explicit) | yes (forward/backward allocation) | Common |
| What-if scenarios | yes (scenario screens) | yes ("test what-if scenarios") | yes (simulations with parameters) | Common |
| Setup/changeover modeling (incl. sequence-dependent) | yes (setup matrices/rules) | yes (changeover rules, cleaning, campaigns) | yes (external setup, setup switching, setup minimization) | Common |
| Material availability in the scheduling decision | yes (operation materials; feasibility coloring includes material shortages) | yes (materials as input data) | yes (raw-material restrictions, inventory+1-to-1 pegging) | Common (not all deployments use it; capacity-only scheduling exists) |
| Alternate resources / multi-resource operations | yes (alternate operation/resource; split) | yes (resource assignments; lines/tools/crews) | yes (group assign, workers/jigs/molds) | Common |
| Optimization objective weighting | no evidence (heuristic/replan focus) | yes ("optimization factors weight the rules engine") | partial (Optimization option module; load leveling; setup minimization) | Optional / product-specific |
| Bottleneck / late-order / expedite analytics | yes (bottleneck, late orders, expediting screens) | yes ("bottlenecks discovered too late" framing) | partial (visual management) | Common |
| Mid/long-term + short-term planning tiers | yes (planning + scheduling in one model) | yes (supports scenario planning; framing mostly scheduling) | yes (APS module vs MS module, synchronized) | Common; depth varies |
| Multi-plant / multi-site | yes (locations; network inventory) | yes (multi-site framing) | yes (SCM module extends) | Optional |
| Skills/labor scheduling | yes (skills, resource skills) | yes (labor as data source; Shiftboard integration) | yes (skill map/skill charts) | Common |
| Industry-specific constraints (batch furnace, tank cleanup, allergen, expiry) | — | yes (chemical/food/framing) | yes (batch furnace, tank, inventory expiration) | Optional (industry overlay) |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

1. **Production orders** — schedulable jobs for items to be produced (customer, forecast, or planner-created).
2. **Operations** — each order's work decomposed into one or more steps.
3. **Finite-capacity resources with availability calendars** — machines/work centers/labor/tooling whose usable time is limited and time-bounded.
4. **A computed schedule** — the system assigns operations to resources over wall-clock time respecting those limits; this schedule is the central working object.
5. **Review–adjust–regenerate loop** — the planner can inspect the schedule, adjust it, and have the system recompute as orders, priorities, or conditions change.

Removing finite capacity → infinite-capacity MRP-style production planning (different Type). Removing the computed time/resource assignment → a reporting or record system (ERP/BI). Removing the loop → a black-box calculator, which no sampled product is; interactive adjustment predates optimization (1990s FCS lineage) and is what makes it a planner's tool.

### L1 — Common Mature Structure (very common, not definitional)

- Gantt schedule board as the primary surface (near-universal presentation of the L0 schedule).
- Constraint/problem reporting (overload, shortage, late orders, bottleneck identification, criticality).
- What-if scenarios / simulations; forward & backward scheduling modes.
- Setup/changeover modeling (including sequence-dependent) and setup minimization.
- Material availability feeding the schedule decision; pegging order↔material.
- Alternate resources; skills/labor; multi-resource and batch operations.
- Proposed vs firm/locked schedule elements.
- Integration: import orders/routings/calendars/inventory from ERP/MES; export schedules/dates/priorities back (dispatch lists, publish).
- Due-date quoting, priority rules, load leveling; KPI/reporting dashboards.

### L2 — Variant / Optional Structure

- Planning-horizon breadth: short-term shop scheduler only vs integrated mid/long-term + short-term tiers.
- Optimization posture: rule/dispatching heuristics with manual control (older/simpler products) vs weighted-objective optimization engines (newer/complex deployments).
- Scope: single plant vs multi-plant/network (overlaps Supply Chain Planning territory).
- Industry overlays: process manufacturing (batch furnaces, tank cleanup, campaigns, expiry, allergen), regulated industries, high-mix job shops.
- Deployment & business model: on-prem Windows-era clients vs cloud/web; commercial vs open source; standalone vs suite module vs ERP-coupled.
- Labor dimension: crews, skill matrices, shift workforce scheduling integration.

### L3 — Vendor-specific (Research Notes only)

- PlanetTogether: "Five Steps" onboarding narrative; "optimization factors weight the rules engine" phrasing; named integrations (SAP, NetSuite, Kinaxis, AVEVA, Aptean Ross, Shiftboard); APS Readiness Score.
- frePPLe: operation subtypes (fixed_time/time_per/alternate/split/routing), resource subtypes incl. infinite; plan-editor color schemes (feasibility/criticality/delay/priority/inventory); Odoo connector; superuser-shared color config.
- Asprova: module names (APS/MS/MS Light/MRP/SED/MES/BOM/NLS/DS/SCM); pegging method names (N-to-N, 1-to-1, inventory+1-to-1); time-constraint mnemonics (ESE, EES, ESSEE, SSEEE); parametric BOM; Resource Lock / Group Assign / Event options; Japan market-share claim (Techno Systems Research 2011, vendor-cited).

## Rejected Findings

- **"APS = optimization/AI engine"** — rejected as defining. Manual-first interactive editing + rule-based dispatching is a fully legitimate form (frePPLe plan editor emphasizes manual replan commands; Asprova's lineage since 1994 and its "MS" scheduler are rule/heuristic-based; optimization is an option module or a weighting layer). Optimization posture is L2.
- **"APS must model materials"** — rejected as definitional. Material feasibility is common (all three expose material data) but capacity-only scheduling deployments exist; directory already separates Demand/Supply Planning.
- **"APS includes MRP"** — rejected. Asprova ships MRP as a separate module; PlanetTogether's own table says MRP plans materials and APS *uses* its output.
- **"APS replaces ERP/MES"** — rejected; directly contradicted by vendor material (PlanetTogether FAQ: "No"; Asprova sells MES/MRP as separate sibling modules).
- **"Gantt chart is the definition"** — rejected as L0; Gantt is the dominant presentation (L1). A dispatch-list or timeline-list surface would still be the same Type; but every sampled product presents the schedule on a time axis, so it stays a standard capability.
- **"Multi-plant/S&OP is core"** — rejected; L2 scope variant; overlaps Supply Chain Planning / Demand Planning leaves.

## Boundary Findings

- **vs Production Planning**: production planning works bucketed (days/weeks), typically infinite or rough-cut capacity, and explodes demand into orders/materials. APS consumes orders and assigns them operation-by-operation onto finite resources in wall-clock time. Test: remove per-resource finite time assignment → production planning remains; remove demand explosion → APS remains. (Evidence: frePPLe exposes "unconstrained capacity requirements" as a separate review from the constrained plan; PlanetTogether table positions MRP as material planning.)
- **vs MES**: MES records execution (completions, downtime, actual progress); APS decides what *should* run when. They exchange data (APS consumes MES status; publishes priorities). Evidence: PlanetTogether table; Asprova ships Asprova MES as a separate module.
- **vs Manufacturing ERP**: ERP is the system of record for orders, inventory, routings, items; APS is the scheduling/decision layer using that data. Same evidence.
- **vs Shop Floor Management**: shop-floor surfaces execute/visualize the current day's work; APS owns the schedule generation across the horizon.
- **vs generic Resource Calendar / Enterprise Resource Scheduling**: those book arbitrary resources for appointments/events; APS binds scheduling to manufacturing semantics (operations, routings, BOMs, setup rules, order quantities). Test: remove manufacturing routing/order semantics → generic resource scheduling.
- **vs Construction Scheduling**: project network of activities (critical-path tradition) vs recurring production orders on factory resources with routings/setup rules. Different object model even though both are "scheduling".
- **Taxonomy note — "Advanced" in the name**: it is a market-era label (positioning vs MRP/infinite-capacity planning and spreadsheets), not a structural test. The definition deliberately centers on finite-capacity scheduling so that 1990s-generation schedulers (Asprova since 1994; Preactor-lineage products) still fit; a future joint review of Production Planning should confirm the capacity-model split.
- **Sibling-overlap flag**: Production Planning, Demand Planning, Supply Planning, Supply Chain Planning Platform (§10 siblings) share objects (orders, resources, materials, calendars) with APS; the boundary is the finite-capacity operation-level time assignment. Flagged for joint review when those leaves are processed.

## Uncertainties

- Siemens Opcenter APS documentation unreachable (two 404s); suite-vendor packaging claims for it rest on general market knowledge and are **not** asserted in the final document. It is retained here only as a candidate product that could not be researched.
- Asprova online help is login-gated and its knowledge center was unreachable; Asprova observations are limited to official product pages (Tier 2). Detailed default rules (dispatch rule defaults, engine internals) therefore stay unstated.
- PlanetTogether's support KB is gated; its product behavior is documented at the positioning/flow level, not screen level.
- No precise numeric claims (plan horizons, speed figures, market shares) were carried into the final document; vendor-cited figures (e.g. Asprova market share, PlanetTogether case-study percentages) are marketing figures and remain here only.
- Exact automation degree of each engine (exhaustive search vs heuristics) is not documented publicly in the reachable material; the final document speaks of "scheduling logic/rules/optimization" generically.

## Final Synthesis

An APS is the plant's finite-capacity scheduling layer. It holds a constraint model of the factory — production orders decomposed into operations, resources with calendars and capacities, setup/changeover rules, (commonly) material availability — and computes a wall-clock schedule assigning operations to resources. That schedule is the application's central object: presented on a time axis (Gantt), editable by the planner (drag, reassign, lock, expedite, prioritize), regenerable (forward/backward, rules, optionally weighted optimization), explorable in what-if scenarios, and publishable back to ERP/MES as dated, sequenced, resource-assigned work for the shop floor. Integration is bidirectional and continuous: plans go in, the schedule and priorities come out; events (breakdowns, rush orders, material delays) trigger replanning. The defining core is small and era-proof; everything else — optimization weighting, scenario tooling, setup matrices, skills, multi-plant scope, industry rules — is mature structure or variant, and ERP/MRP/MES execution and record-keeping remain outside the Type.
