# Research Notes — Production Planning

Research date: 2026-09-09
Slug: production-planning
Directory leaf: Production Planning (§16 Engineering, Manufacturing & Industrial)

## Research Goal

Understand from real products what a Production Planning application actually is as an Application Type: what objects exist inside it, what the planning computation is, how planners work the plan, how it hands orders to execution, and where its boundaries lie against the already-processed §16/§10 siblings — APS, Manufacturing ERP, MES, Demand Planning, Supply Planning — plus Manufacturing Supplier Collaboration (computation-vs-exchange flag) and the unprocessed Shop Floor Management.

This pass carries four pre-hung joint-review obligations from earlier passes:

1. **advanced-planning-scheduling-aps**: "vs production-planning / demand-planning / supply-planning / supply-chain-planning-platform — all share orders/resources/materials/calendars; the structural test is finite-capacity operation-level time assignment (remove it → bucketed network/demand planning remains; keep it → APS remains)"; also "a future joint review of Production Planning should confirm the capacity-model split."
2. **manufacturing-execution-system-mes**: "production-planning / advanced-planning-scheduling passes should ratify the planning-vs-execution seam from their side."
3. **manufacturing-erp**: "production-planning and advanced-planning-scheduling passes should confirm the planning-depth seam from their side" (ERP: "replenishment-level suggestions vs constraint optimization"; ERP planning deliberately rough-cut).
4. **manufacturing-supplier-collaboration**: "vs production-planning/advanced-planning-scheduling — seam is computation (internal plans) vs exchange (supplier-addressed demand signals)."

## Initial Boundary (working hypothesis before research)

- Core use: convert demand (orders + forecast) into a time-phased production plan — master schedule and/or planned orders exploded through bills of material — and carry that plan into firm, scheduled, released production orders for the floor.
- Users: production planners / master schedulers; production managers; purchasing (for the planned-buy side); shop floor as downstream recipient.
- Nearest neighbors: APS (finite-capacity scheduling), Manufacturing ERP (owns the orders/BOM/costing record), MES (executes released orders), Demand Planning (produces the forecast), Supply Planning (network-level buy/make/move plan), Inventory Management System (stock record + reorder points), Shop Floor Management (event-response).
- Unknowns at start: is capacity (rough-cut) definitional or common? Is the MPS as a named artifact definitional, or only one realization? Is auto-creation of orders definitional? How cleanly does the infinite-capacity MRP pole separate from the APS pole in Tier-1 documentation? Is this leaf a Type in its own right or a slice of Manufacturing ERP?

## Research Questions

1. What objects exist (requirements, planned orders, production orders, build definitions, resources, buckets) and how do they relate?
2. What exactly does the planning computation do (netting, explosion, lot-sizing, lead-time offsetting, scheduling)?
3. What capacity model does the planning layer assume — infinite, rough-cut, finite? (The APS split test.)
4. What does the planner actually do — review, adjust, firm/commit, release, re-plan? What are action/exception messages?
5. How does the plan reach execution, and what comes back?
6. Which structures are common-but-not-definitional (capacity views, Gantt, what-if, pegging, ATP)?
7. Where are the boundaries vs APS / Manufacturing ERP / MES / Demand Planning / Supply Planning?
8. Historical check: does 1960s–70s MRP (no capacity dimension) still fit the definition? Does the paper-era planning board?

## Representative Products

| Product | Tier / philosophy | Evidence obtained |
|---|---|---|
| Microsoft Dynamics 365 Business Central (manufacturing planning) | enterprise/SMB ERP with a deep, fully documented planning engine | Tier 1 — two Learn articles fetched (planning functionality; MPS/MRP runs) |
| Odoo Manufacturing | modular open-core app; interactive MPS grid; suggest-then-commit philosophy | Tier 1 — official docs repository rst (Master Production Schedule) fetched |
| MRPeasy | standalone SMB MRP; explicit "Production planning" module; period-grid MPS with rough-cut capacity | Tier 1 — user manual (getting started, Production Schedule page, MPS enterprise-function page) fetched |
| Katana | modern SaaS, inventory-first positioning, priority-queue scheduling | Tier 1/2 — knowledge-base Make-screen article + Manufacturing collection + product root fetched |
| SAP (market anchor only) | enterprise suite; PP/DS split from classic MRP | not fetched this pass (prior passes: help portal JS shell; manufacturing pages 404) — positioning evidence via the supply-planning pass's fetch of SAP's own navigation |

Considered/rejected: frePPLe and Asprova (already sampled by the APS pass — used as cross-reference only, not re-sampled); Epicor Kinetic (Tier-2 only, already characterized by the manufacturing-erp pass); Siemens Opcenter (unreachable in APS pass).

## Sources

Fetched 2026-09-09 (Tier 1 unless noted):

- Microsoft Learn — Dynamics 365 Business Central:
  - "About planning functionality" — https://learn.microsoft.com/en-us/dynamics365/business-central/production-about-planning-functionality
  - "Run Full Planning, MPS, or MRP" — https://learn.microsoft.com/en-us/dynamics365/business-central/production-how-to-run-mps-and-mrp
- Odoo documentation repository (github.com/odoo/documentation, master branch):
  - applications/inventory_and_mrp/manufacturing/workflows/use_mps.rst — raw fetch: https://raw.githubusercontent.com/odoo/documentation/master/content/applications/inventory_and_mrp/manufacturing/workflows/use_mps.rst
- MRPeasy user manual:
  - Getting started — https://www.mrpeasy.com/resources/user-manual/
  - Production Schedule — https://www.mrpeasy.com/resources/user-manual/production-planning/production-schedule/
  - Master Production Schedule (MPS) — https://www.mrpeasy.com/resources/user-manual/settings/system/enterprise-functions/master-production-schedule-mps/
- Katana:
  - "How to use the Make screen (Schedule)" — https://support.katanamrp.com/en/articles/5914378-how-to-use-the-make-screen-schedule
  - Manufacturing collection — https://support.katanamrp.com/en/collections/3312515-manufacturing
  - Product root (Tier 2, positioning) — https://katanamrp.com/
- Internal cross-references (prior passes, same pack): research/advanced-planning-scheduling-aps.md (frePPLe, PlanetTogether, Asprova; capacity-model test), research/manufacturing-erp.md (BC/Odoo/MRPeasy/Epicor; build-definition and production-order record; "rough-cut schedule" quote), research/manufacturing-execution-system-mes.md (planning-vs-execution seam; released orders), research/demand-planning.md (forecast of record; APS sibling flag discharge), research/supply-planning.md (network planned orders; SAP "production planning and detailed scheduling — move beyond classic MRP" navigation quote).

Failed fetches (per network rules, abandoned after 1–2 attempts): odoo.com rendered docs paths (404 ×1 on management/master_production_schedule.html; raw.githubusercontent 17.0 branch 404 ×1 — master branch succeeded); mrpeasy.com/user-manual (404 ×2 — /resources/user-manual/ succeeded); raw.githubusercontent odoo manufacturing.rst overview (timeout ×2 — abandoned; Odoo manufacturing overview covered by manufacturing-erp pass); help.katanamrp.com (transport error ×1 — support.katanamrp.com succeeded).

## Product Observations

### Product A — Microsoft Dynamics 365 Business Central (evidence layer A, Tier 1)

- **The planning system definition (verbatim)**: "The planning system takes all demand and supply data into account, nets the results, and creates suggestions for balancing supply to meet demand." Demand = "any kind of gross requirement" (sales/service orders, component need for production orders, transfers, blanket orders, forecast); supply = "any kind of replenishment" (inventory, purchase/production orders, inbound transfers).
- **MPS vs MRP (verbatim)**: "MPS is the calculation of a master production schedule based on actual demand and the demand forecast… used for end items that have a forecast or a sales order line." "MRP is the calculation of material requirements based on actual demand for components and the demand forecast on the component level. MRP is calculated only for items that aren't MPS items. The purpose of MRP is to provide timed, formal plans to supply the appropriate quantity of the item at the appropriate time and location." Both can run together ("Combined MPS/MRP Calculation").
- **The computation**: "The basis of the planning routine is in the gross-to-net calculation. Net requirements drive planned order releases, which are scheduled based on the routing information (manufactured items) or the item lead time (purchased items)." Planning parameters on items/SKUs control "when, how much, and how to replenish" (reordering policies, reorder point, maximum inventory, time bucket, lot accumulation period, safety stock, safety lead time, min/max order quantity, order multiple).
- **Capacity assumption (verbatim — the APS seam)**: "With each planned method, Business Central generates worksheet entries that assume infinite capacity. When you develop schedules, work center and machine center capacity isn't considered." (Separately, the ERP pass recorded BC's shop-calendar/work-center capacity model and BC's own "rough-cut schedule" boundary sentence.)
- **Multilevel explosion**: sales order or forecast → planning run reads the production BOM → for each produced component a separate planned production order at the next BOM level → recursion until purchased items → "Lower-level orders are scheduled to finish in time for the parent order to start." Worksheet shows Planning Level (0 = finished item) and MPS Order (master-schedule item vs dependent component).
- **Planner loop**: planning lines on a worksheet; **action messages** = "suggestions to create a new order, change an order (quantity or date), or cancel an order" (New / Change Qty. / Reschedule / Resched. & Chg. Qty. / Cancel); planner accepts (Accept Action Message) then **Carry Out Action Message** creates planned or firm planned production orders, assembly, purchase, or transfer orders. Dampeners restrict messages to changes exceeding quantity/day thresholds.
- **Plan states**: planned orders are deleted on the next regenerative run; **firm planned orders survive**; released orders accept actual consumption/output. Planning Flexibility Unlimited/None marks supply as adjustable vs firm.
- **Run methods**: Regenerative Plan (full re-plan), Net Change Plan (only changed items), Order Planning (order-by-order for MTO/one-off demand), Requisition Worksheet (purchase/transfer replenishment for a separate purchasing team).
- **Warnings**: Emergency (negative inventory / back-dated events), Exception (projected inventory below safety stock), Attention (planning start before work date; change to a released order) — lines with warnings are not auto-accepted; "the planner is expected to further investigate these lines."
- **Order tracking**: links between demand and supply visible on the Order Tracking page (pegging).

### Product B — Odoo Manufacturing (evidence layer A, Tier 1)

- **MPS positioning (verbatim)**: "In Odoo Manufacturing, the Master Production Schedule (MPS) is used to plan long-term replenishment for products against a manually-adjustable demand forecast." For "products or components with long lead times or variable seasonal demands… longer-term planning against an expected future demand."
- **Suggest-not-commit philosophy (verbatim)**: "Adding a product to the MPS does **not** automatically create a purchase or manufacturing order… The MPS only suggests the amount of product to be replenished, requiring the user to actually create the replenishing POs/MOs." Reordering rules should not be combined with MPS products.
- **The MPS grid**: periods as columns (yearly/monthly/weekly/daily; configurable count), per product rows: starting stock, **Forecasted Demand** (manual), **Indirect Demand Forecast** ("the forecasted demand for the component from existing MOs" — appears when the product is a component of another product), **+ Replenishment** (suggested from Safety Stock Target − Starting Stock + Forecasted Demand + Indirect Demand; manually adjustable with reset), **= Forecasted Stock** (recomputed per the period equation; carries into the next period's starting stock).
- **Replenishment trigger options**: Manual / Automatic / Never. **Order button** creates the replenishing document by route: Buy → RfQ (Purchase app), Manufacture → MO (Manufacturing app). BoM selection pulls components into the MPS.
- **Forecast assistance**: "Suggest Forecasted Demand" populates demand from history — actual demand one year ago, previous year, or 30/90/365-day averages prorated to the period, with a scaling factor (e.g. 110% growth).
- **Status indicators**: replenishment cells colored green (ready), gray (ordered = suggested), yellow (ordered < suggested), red (ordered > suggested); filters: To Replenish, Replenishment Too Low/High, Forecast Too Low (actual > forecast), Manually/Automatically Replenished.
- **ATP row option**: Available to Promise replaces Forecasted Stock (Starting Stock − Actual Demand + Replenishment; minus indirect demand for components).
- (Manufacturing-order machinery — BoM types, one/two/three-step manufacturing, work centers, shop-floor tablets, MO cost vs real cost — is documented in the manufacturing-erp pass and used here as cross-reference only.)

### Product C — MRPeasy (evidence layer A, Tier 1)

- **Product shape**: standalone MRP for small manufacturers ("suitable for both make-to-stock and make-to-order"); eight sections, of which **"Production planning — production planning and management"** is the planner's home (Manufacturing Orders, Production Schedule, Workstations, Workstation Groups, Bills of Materials, Routings, Statistics). A separate section, "Production Reporting — For Worker," is the shop-floor surface (My Production Plan, Internet-kiosk) — the planner/floor split is a top-level product structure.
- **MO creation paths (MTS)**: manual; from reorder point (Stock → Critical on-hand); from the Forecasting function. (MTO): auto-generate one MO per customer-order line, one MO across multiple COs, or manual MO booked to the CO. Items are **booked** to MOs from current stock **or from planned supply** (future PO/MO); unavailable items generate demand automatically.
- **Production Schedule surface**: "shows all the Manufacturing Orders that have been scheduled" in **Calendar and Gantt chart views**; drag-and-drop rescheduling of MOs and operations; "The software will not allow overbooking a workstation" (calendar view); "If materials will not be available by the time, a pop-up appears, asking whether to move MO start"; "Started or finished operations cannot be rescheduled"; Gantt views by Manufacturing Orders or **Workstations load**; backdrop color = progress (not started/in progress/paused/finished/overdue); text color = parts availability/status; mass **Rebook parts for planned MOs** (FIFO, or FEFO with expiry).
- **MPS (Enterprise function) — verbatim purpose**: "a powerful inventory and production planning tool that focuses on medium and long-term demand projections. It helps to: make a period-by-period plan for the foreseeable future; plan production against a sales forecast and firm orders; plan material purchases; plan inventory levels; test what-if scenarios; **perform rough cut capacity planning**; **separate the planning and scheduling processes**."
- **MPS view**: per product × period rows — Starting inventory, **Sales forecast** (manual or linked to the Sales Forecasting function), **Firm orders** (confirmed COs), **Production plan** (manual), **Scheduled already** (MOs in New/Scheduled/In progress), **= Ending inventory** (formula: Starting − GREATER OF(forecast, firm orders) + GREATER OF(production plan, scheduled MOs)); color coding vs reorder point (green/yellow/orange-negative). Current period is not editable (only actuals). Up to 5 years of periods.
- **Required Capacity view**: per workstation group × period — Total capacity (working hours, manually overridable to simulate) vs Required hours (routings × production plan, setups ignored); min/max load % highlighting (light blue / orange); "Scheduled already values from the MPS are ignored. This allows simulating what-if scenarios."
- **Procurement Schedule view**: per part × period — Starting inventory, **Demand by MPS** (Σ BOM quantity × GREATER OF(production plan, scheduled MOs) over all products where the part appears), Planned quantity (manual), Ordered quantity (open POs), Ending inventory with color coding. Multi-level BOMs: subassemblies' capacity and material requirements included automatically.
- **Tiering**: MPS, Backward Production Scheduling, Sales Forecasting, Multi-stock/production sites are Enterprise functions; subcontracting, matrix BOM, parallel operations are Professional functions (packaging evidence).

### Product D — Katana (evidence layer A for the Make screen; Tier 2 for positioning)

- **Positioning shift noted**: the root page now markets Katana as "Cloud Inventory Management Software… real-time inventory control" with Manufacturing as one core capability ("Get end-to-end manufacturing visibility. Track production as work moves… materials, progress, and finished goods"); knowledge base retains a Manufacturing collection (38 articles) and a Planning and Forecasting collection.
- **Make screen / Schedule tab (verbatim fragments)**: "Displays all your manufacturing orders, both Make-to-Order (MTO) and Make-to-Stock (MTS)"; "a centralized view to manage all production jobs in a single queue"; "adjust the priority of MOs by dragging and dropping them within the list"; "Production should commence with MOs at the top of the list, proceeding downwards."
- **Columns/state**: ingredient availability ("in stock, expected, or not available"), production status (Not started / Work in progress / Done), production deadline (estimated completion), **delivery deadline** for SO-linked MOs ("helping identify any conflicts between production schedules and customer commitments").
- **Order linkage model**: MTO MOs "permanently linked" to their SOs (reprioritizing the MO moves the SO); MTS MOs "not permanently linked" — commitments to SOs "based on order priority and may be recalculated if an MO or SO is reprioritized." Open vs Done tables; Done MOs get a completion date and can be reverted.
- **Execution hand-off**: a Tasks tab breaks production into tasks per resource/operator; operators receive tasks in the **Shop Floor App** ("view and complete tasks, report consumed ingredients, record manufactured products"). Subassembly MOs can be created automatically; routings/operations and operation costs documented in the collection (cross-reference level).
- Capacity signals: a "weekly throughput" setting per company (article title) — a light capacity parameter, not a finite scheduler.

### Product E — SAP (market anchor only; evidence via prior passes)

- Not fetched this pass (SAP Help Portal JS shell per ERP/SCP passes; manufacturing pages 404 per ERP pass). Held as the enterprise-suite anchor. Seam evidence from the supply-planning pass's fetch of SAP's own navigation: "Production planning and detailed scheduling — Move beyond classic MRP with production planning and scheduling software. Plan production, incorporate capacity and material constraints" — i.e., SAP itself separates classic MRP-class planning (inside the ERP) from capacity-constraint production planning/scheduling (PP/DS, the APS pole).

## Cross-product Comparison

| Structure | Business Central | Odoo | MRPeasy | Katana | Reading |
|---|---|---|---|---|---|
| Time-phased production requirements from orders + forecast | ✓ (demand side incl. forecast; planning horizon with ending date) | ✓ (MPS grid periods; forecast rows) | ✓ (MPS periods; sales forecast + firm orders) | partial (deadlines; SO-driven queue; forecasting collection) | **core** (MTO-heavy SMB poles hold it implicitly) |
| Netting against stock and open supply (planned receipts) | ✓ explicit gross-to-net | ✓ (starting stock, forecasted stock equation) | ✓ (ending-inventory equation; ordered quantity from open POs) | ✓ (ingredient availability: in stock / expected) | **core** |
| Explosion through build definitions into planned production orders | ✓ multilevel, per-level orders, parent/child timing | ✓ (BoM adds components; indirect demand from MOs) | ✓ (multi-level BOM in MPS; Demand by MPS × BOM) | ✓ (multi-level BOM; auto subassembly MOs) | **core** |
| Planned orders as the plan's working objects (make + buy) | ✓ planning worksheet lines → carry out | ✓ replenishment row → Order button | ✓ production plan + procurement planned quantity | ✓ MOs (auto-create for subassemblies) | **core** |
| Planner review/adjust/commit loop with suggestion states | ✓ action messages, accept, warnings not auto-accepted | ✓ suggest-only MPS, manual Order, reset, status colors | ✓ manual production-plan/procurement rows vs scheduled actuals | ✓ drag-drop priority; availability states | **core** |
| Firm vs planned distinction (commitment survives re-plan) | ✓ firm planned orders; Planning Flexibility None | partial (manual values vs suggestion reset) | ✓ production plan vs scheduled already (orange when unequal) | ✓ MTO permanent links | common |
| Time-bucketed horizon (period grid / planning horizon) | ✓ ending date + time buckets | ✓ yearly→daily periods | ✓ weekly/monthly/quarterly, up to 5 years | implicit (queue + deadlines) | **core** (granularity varies) |
| Capacity model at planning level | **explicitly infinite** in worksheet entries | none in MPS | rough-cut (Required Capacity view vs workstation groups) | light (weekly throughput) | capacity views **common, not definitional** |
| Order scheduling surface (calendar/Gantt/priority) | ✓ planned order release dates (scheduling from routing/lead time); replan | ✓ (manufacturing planning via MO dates; MPS Order button) | ✓ calendar + Gantt drag-drop; workstation-load Gantt; backward scheduling (paid) | ✓ priority queue + deadlines | common (presentation varies) |
| Exception/attention messaging | ✓ Emergency/Exception/Attention warnings; dampeners | ✓ status colors + filters | ✓ color coding; load highlighting | ✓ availability states; deadline conflicts | common |
| Pegging demand↔supply | ✓ Order Tracking | ✓ indirect demand from MOs; MTO links | ✓ booking from planned supply | ✓ MTO permanent links / MTS recalculated commitments | common |
| ATP / order promising | ✓ (order promising documented elsewhere in BC docs; ATP not fetched this pass) | ✓ ATP row option | — (delivery-date estimation at CO) | — | optional |
| What-if scenarios | ✓ (replan; override capacity simulation not explicit) | — | ✓ explicit (override capacity hours; Scheduled-already ignored) | — | optional |
| Auto-creation of orders | option (carry out creates orders) | **explicitly not** from MPS (trigger Manual/Automatic/Never) | ✓ ROP-driven MO creation | ✓ auto subassembly MOs | variant (automation posture) |
| MTO + MTS modes | ✓ (Order Planning vs MPS/MRP) | ✓ (MTO route vs MPS) | ✓ explicit both | ✓ explicit both | common |
| Forecast assistance from history | forecast as input (Use Forecast) | ✓ Suggest Forecasted Demand (year-ago, averages, scaling) | ✓ link Sales Forecasting | forecasting collection | common |
| Held-in-system build definitions | ✓ (production BOMs + routings as master data) | ✓ (BoM on product; selected in MPS) | ✓ (BOM + Routing sections inside Production planning) | ✓ (recipes/operations on items) | common (ownership location varies) |
| Where the planner's surface lives | ERP area (planning worksheet) | app module (Manufacturing → Planning) | standalone product's top-level section | SaaS screen (Make) | variant |

## Canonical Model (L0–L3)

### L0 — Defining Invariant (minimal)

Production Planning is the manufacturer's demand-to-production-order planning system. Three jointly-held structures:

1. **The makeable planning substrate** — the manufactured items with their build definitions (bills of material, with operations/routings where scheduling depth exists), stock positions and open supply (scheduled receipts), supply sources (make/buy), and planning parameters (lead times, lot sizes, safety stocks, planning horizons, working calendars) held as the model the plan is computed against. Remove → an order-entry or stock tool with nothing makeable to plan.
2. **The requirements-explosion computation** — the system nets forward requirements (orders, forecasts, stock policies) against on-hand and open supply and explodes them through the build definitions into time-phased **planned production and purchase orders**, scheduled across the planning horizon in time buckets (typically assuming infinite or rough-cut capacity). Remove → reorder-point replenishment (inventory territory) or a scheduler with no requirements logic.
3. **The planner's commit-release loop** — the computed suggestions are worked by a planner: reviewed and adjusted (with action/exception messages distinguishing create / change quantity / reschedule / cancel), firmed into real production and purchase orders, placed on the production schedule against resources and dates, and released toward shop-floor execution; the plan is re-run as demand, supply, or actuals change. Remove → a suggestion feed nobody commits (calculator pole), or manual dispatch boards.

Jointly-held is load-bearing:

- 1 alone = master data + stock lists (no plan).
- 2 alone = an MRP calculator (thin pole: spreadsheet MRP, suggestion-only utilities).
- 3 without 1+2 = manual production scheduling / dispatch boards.
- 1+2 without 3 = an auto-suggestion engine nobody works (below the Type).
- 1+3 without 2 = order scheduling without requirements explosion (approaches generic scheduling).
- 2+3 without 1 = transaction processing with no makeable model (ERP order handling).

Note on the master schedule: the MPS as a named, editable top-level grid (Odoo, MRPeasy) is one prominent realization of leg 2's requirements picture. Make-to-order shops that run order-by-order planning (BC Order Planning; MTO generation from sales orders in all four samples) satisfy the Type without a standing MPS artifact. The MPS is therefore held as a common structure, not the invariant.

### L1 — Common Mature Structure

- Production-order pipeline with status lifecycle (planned/scheduled → in progress → done), linked to the plan that generated it.
- Order scheduling surfaces: calendar / Gantt / priority-queue presentations of scheduled orders, with drag-and-drop or reordering; forward and backward scheduling modes.
- Rough-cut capacity views: required vs available hours per resource group over periods; load highlighting (common; explicitly NOT the finite-capacity scheduler — see Boundary Findings).
- Exception/attention machinery: warnings (emergency/exception/attention class), color coding, filters, dampeners to suppress noise.
- Pegging / order tracking between demand and supply; booking/reserving materials from stock or from planned supply.
- Firm vs planned elements; frozen current periods; planning-flexibility flags protecting committed supply from the next run.
- MTO and MTS modes; MO generation from sales-order lines; MTS generation from forecast/reorder points.
- Forecast assistance: linking or suggesting demand from sales history (year-ago patterns, averages); sales-forecast linkage.
- ATP / available-to-promise views; delivery-date estimation against planned supply.
- Subcontracting of operations; multi-site/multi-warehouse planning; multi-level BOM handling including kits and subassemblies.
- Automation options: reordering rules, automatic subassembly MOs, auto-creation triggers (manual/automatic/never).
- Integration both directions: master data, stock, orders, and actuals exchanged with the ERP/inventory core; export of released orders to execution surfaces.

### L2 — Variant / Optional Structure

- Where planning lives: deep area of an ERP (Business Central), module of a modular suite (Odoo), standalone SMB MRP product (MRPeasy), inventory-first SaaS screen (Katana) — packaging is a variant axis, not the Type.
- Planner surface philosophy: engine-worksheet (calculate → review lines → carry out) vs interactive grid (period rows edited by hand) vs prioritized queue (drag-drop) — all realizations of the same loop.
- Automation posture: suggest-only (Odoo MPS explicitly does not auto-create) vs auto-triggered creation (reordering rules, ROP-driven MOs) vs batch carry-out (BC).
- Engine methods: regenerative vs net-change vs order-by-order runs; combined MPS/MRP.
- Horizon and granularity: weekly/monthly/quarterly buckets up to years (MRPeasy) vs daily (Odoo option) vs date-precise worksheets (BC).
- Capacity depth: none in the plan run (BC explicitly) → rough-cut views (MRPeasy) → separate capacity-constraint scheduling product (SAP PP/DS = APS pole).
- Production mode flavors: make-to-stock / make-to-order / engineer-to-order; discrete vs process vocabulary (per manufacturing-erp pass, one build-definition structure spans both).
- What-if/scenario tooling depth; multi-site scope; industry overlays (expiry/FEFO booking, matrix BOMs).

### L3 — Vendor-specific (research notes only)

- Business Central: field vocabulary (Dampener Period/Quantity, Overflow Level, Lot Accumulation Period, Rescheduling Period, Planning Flexibility, Missing SKU Planning Policy, Combined MPS/MRP Calculation, Respect Planning Parameters for Exception Warnings); worksheet/report names (Planning Worksheet, Requisition Worksheet, Order Tracking, Planning Error Log); warning classes; Regenerative/Net Change/Order Planning naming.
- Odoo: MPS row set and equation; Suggest Forecasted Demand options (Actual Demand Y-1/Y-2, Last 30/90/365 days, scaling factor); replenishment cell colors (green/gray/yellow/red); trigger values Manual/Automatic/Never; feature checkbox + Default Time Range/Number of Periods configuration; ATP row; route-driven RfQ vs MO creation.
- MRPeasy: three MPS views (MPS / Required Capacity / Procurement Schedule); GREATER OF ending-inventory formula; Demand by MPS = Σ(BOM qty × GREATER OF(production plan, scheduled MOs)); min/max workstation-load % settings; 5-year period scroll; current-period non-editability; Rebook parts (FIFO/FEFO); "My Production Plan" / Internet-kiosk worker surfaces; Enterprise/Professional function gating (MPS, backward scheduling, sales forecasting paid).
- Katana: Make screen (Schedule + Tasks tabs); single prioritized queue; ingredient-availability states; MTO-permanent vs MTS-recalculated commitment model; Shop Floor App; weekly throughput; add-ons (Advanced Manufacturing, Manufacturing Management); inventory-first repositioning.
- SAP: PP/DS as the separate "beyond classic MRP" product line (via navigation quote in supply-planning pass).

## Rejected Findings

- **"Production planning includes finite-capacity operation-level scheduling"** — rejected. BC's planning runs "assume infinite capacity" (verbatim); MRPeasy separates rough-cut capacity views from scheduling and sells deeper scheduling features separately; the APS pass's structural test stands. Finite-capacity scheduling is the APS Type; where bundled, it is suite packaging.
- **"The MPS artifact is definitional"** — rejected. It is one realization of the requirements picture; MTO order-by-order planning satisfies the Type without a standing MPS.
- **"Auto-creation of orders is definitional"** — rejected. Odoo's MPS explicitly only suggests; MRPeasy creates from ROP; BC's carry-out is planner-initiated. Automation posture is a variant.
- **"Production planning owns BOM/routing master data"** — rejected as definitional. The invariant is that the plan explodes *through* build definitions; whether they are held in the same product, a sibling module, or an upstream system varies (all four samples hold them, but the planning logic consumes rather than defines them).
- **"Production planning = MRP = purchasing requirements"** — rejected. Component/purchase explosion is inside the Type, but the production-order pipeline, resource/schedule context, and release-to-floor loop distinguish it from pure replenishment planning (Supply Planning / Inventory Management System territory).
- **"Capacity planning is definitional (MRP II closed loop)"** — rejected for L0. Pure MRP (no capacity dimension) still plans production; the historical check confirms capacity entered the discipline later (closed-loop MRP II) and appears here only as common rough-cut views.

## Boundary Findings

1. **vs Advanced Planning & Scheduling / APS — JOINT REVIEW DISCHARGED (keep-both RATIFIED from this side).** The APS pass's structural test (finite-capacity operation-level time assignment) is confirmed by fresh Tier-1 evidence: BC worksheet entries "assume infinite capacity"; MRPeasy's own MPS copy names "rough cut capacity planning" and "separate the planning and scheduling processes" as distinct concerns; rough-cut views compare totals per period rather than assigning operations to resources in wall-clock time. Remove finite-capacity operation-level assignment → this Type remains; add it → APS. Suite vendors bundle both (frePPLe spans planning and scheduling; Asprova sells MRP as a separate module beside its scheduler; SAP separates classic MRP from PP/DS "beyond classic MRP").
2. **vs Manufacturing ERP — planning-depth seam CONFIRMED from this side.** The ERP pass holds MRP-class planning as common (non-definitional) structure and the production order as costing/execution unit of the business record; this pass holds the planning loop itself as the defining core. The same products instantiate both Types (BC/Odoo/MRPeasy sampled by both passes); the seam is center-of-gravity: business record + costing vs planning decisions. Remove the planning loop → a Manufacturing ERP remains (with rough-cut planning as a feature); remove the business/financial spine → a production-planning tool remains. Standalone planning products exist (MRPeasy self-labels "MRP software"; APS vendors ship MRP modules), so the Type is not merely an ERP slice.
3. **vs MES — planning-vs-execution seam RATIFIED from this side (discharges the MES pass's forward flag).** Planning decides what to make, how much, and roughly when, at order grain over a horizon, before execution; MES takes **released** orders and executes them at operation/step grain, producing the as-built record. Fresh evidence: BC's status ladder makes Released the boundary at which actual consumption/output recording begins; MRPeasy structurally separates the planner's "Production planning" section from the worker's "Production Reporting" surfaces; Katana hands tasks to the Shop Floor App for execution. Execution sequencing observed at planning level is order placement (dates), not operation-level dispatch optimization.
4. **vs Demand Planning — consistent with that pass's flag discharge.** Demand planning produces and works the forecast of record; production planning consumes forecasts as one requirements stream among orders and stock policies (BC "Use Forecast"; MRPeasy links Sales Forecasting; Odoo forecast rows; Katana forecasting collection). Demand planning holds no planned orders or build definitions.
5. **vs Supply Planning — seam refined (one-sided sibling statement updated).** The supply-planning pass phrased the §16 seam as "APS/production planning assigns operations to finite capacity at operation-level time inside the plant" — correct for APS, overstated for production planning, which (per this pass) is bucketed and typically infinite-capacity. Refined seam: supply planning computes the **network-wide** supply response (buy/make/move across locations/echelons, aggregate make quantities, inventory policy); production planning owns the **make-side plan inside the production domain**: explosion through build definitions into production orders, the production schedule against plant resources, and firming/release. The MRP netting computation is shared machinery realized at both grains; integrated suites realize them as layers of one system (network plan → master schedule → detailed scheduling).
6. **vs Manufacturing Supplier Collaboration — RATIFIED.** Production planning computes internal plans; supplier collaboration exchanges buyer-addressed demand signals and responses with counterparties. A forecast or schedule inside planning is a computation input/record; shared outward, it becomes the collaboration Type's exchange record.
7. **vs Inventory Management System — consistent with the IMS pass's record-vs-forecast line.** The thin shared edge is reorder-point-driven MO creation (MRPeasy Critical on-hand); what elevates it into production planning is the explosion through build definitions and the production-order pipeline, not the reorder rule itself.
8. **vs Shop Floor Management (unprocessed)** — held consistent with the MES pass's framing: event-and-response loops on the floor (andon, dispatch, issue handling) vs the plan-and-order pipeline that feeds the floor. To be confirmed by that pass.
9. **Taxonomy / naming note.** The market label "production planning" also attaches to shop-scheduling products (MRPeasy sells a separate "Production Scheduling Software" page; Katana titles its queue "master scheduling"; the APS market grew out of "production planning and scheduling"). The Type boundary must remain structural (requirements explosion + planner commit loop), not label-based. Recorded for the taxonomy pass.

## Historical / Market-Sample Check

- **1960s–70s MRP**: item master + BOM + inventory records + (optional) master production schedule + time-phased planned orders via netting and explosion + action/exception messages + planner firming and release. Satisfies all three L0 legs — with **no capacity dimension at all**, confirming capacity is not definitional. ✓
- **1980s closed-loop MRP II**: adds rough-cut capacity planning (RCCP), capacity requirements planning, and shop calendars — the classic full shape; still satisfies the legs with rough-cut (not finite) capacity. ✓
- **Spreadsheet era**: an MPS grid with netting formulas, a manually exploded material list, and a planner committing orders — MRPeasy's period-grid MPS and Odoo's equation-driven grid are literal software realizations of that worksheet; Streamline's testimonials (supply-planning pass) document the same before-state. ✓
- **Paper-era planning office**: master schedule sheets and exploded material requirement lists on the planning board, with the scheduler writing firm orders — satisfies the shape in manual form; reorder-point cards without any explosion remain the thin ancestor (inventory edge). ✓
- **Definition hygiene**: the L0 names no cloud, no Gantt, no drag-drop, no AI, no specific algorithm brand, no capacity model, no MPS artifact. All four sampled products (1990s-heritage ERP engine, open-source modular app, Estonian SMB MRP, 2020s SaaS) and the MRP lineage satisfy it. **Verdict: passed; no re-abstraction needed.**

## Uncertainties

1. **Enterprise suite depth under-sampled.** SAP unreachable (inherited limitation); SAP held as market anchor via prior passes' positioning evidence. The enterprise pole's L0 realization is asserted only at the pattern level (classic MRP vocabulary), corroborated by SAP's own "beyond classic MRP" navigation quote.
2. **Katana's planning depth is queue-shaped.** Its Schedule tab is a priority queue rather than a bucketed requirements engine; explosive/forecast machinery exists in the product (multi-level BOMs, auto subassembly MOs, forecasting collection) but was verified only at collection/article-title level, not article level. Katana is retained as the SaaS pole with its planning depth calibrated accordingly ("light capacity parameter", not a scheduler).
3. **Odoo evidence covers the MPS surface, not the full MRP engine.** Odoo's reordering-rule MRP and procurement planning were documented in the manufacturing-erp pass; this pass's fresh evidence is the MPS rst (master branch). The rendered docs site paths 404'd; the repository fetch succeeded — recorded as a sourcing note, not a content limitation.
4. **ATP / order-promising depth** verified only in Odoo (ATP row) and referenced in BC (order promising exists in the docs family but was not fetched this pass) — held as optional/optional-common, not asserted as universal.
5. **Whether some production-planning products lack any pegging/booking machinery** — all four sampled products carry some demand↔supply linkage; held as common rather than definitional on sample strength (four of four, but the sample is documentation-reachable products).
6. **Forecast-assistance depth varies** (from manual entry to linked statistical forecasts); no assertion is made about any product's forecasting algorithms.

## Final Synthesis

A Production Planning application is the manufacturer's demand-to-production-order planning system. It holds a makeable model of the operation — items with build definitions, stock and scheduled receipts, supply sources, planning parameters — and computes from it, by netting forward requirements (orders, forecasts, stock policies) against supply and exploding the net through the build definitions, a time-phased plan of planned production and purchase orders across the planning horizon, typically assuming infinite or rough-cut capacity. The plan is not self-executing: a planner works it — reviewing suggestions, acting on create/change/reschedule/cancel messages, correcting exceptions — then firms planned orders into real production and purchase orders, places them on the production schedule against resources and dates, and releases them toward the shop floor, with the whole loop re-run as demand, supply, and actuals change. Around that core, mature products add order-lifecycle pipelines, calendar/Gantt/priority scheduling surfaces, rough-cut capacity views, exception and warning machinery, pegging and material booking, MTO/MTS modes, ATP, subcontracting, multi-site scope, and automation triggers. The Type is distinct from APS (no finite-capacity operation-level scheduling — the seam its own vendors name: "infinite capacity", "rough cut", "separate the planning and scheduling processes"), from Manufacturing ERP (planning loop vs business-and-costing record; MRP-class planning is that Type's common structure but this Type's center), from MES (plan grain vs released-order execution and as-built record), from Demand Planning (consumes the forecast vs produces it), from Supply Planning (make-side plan inside the plant vs network-wide buy/make/move response), and from Supplier Collaboration (internal computation vs cross-party exchange). It is the bucketed middle layer of the manufacturing stack: below the network and forecast plans, above the floor.
