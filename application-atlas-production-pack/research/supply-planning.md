# Research Notes — Supply Planning

Research date: 2026-09-08
Slug: supply-planning
Directory leaf: Supply Planning (§10 Enterprise Operations & Administration)

## Research Goal

Understand what a Supply Planning application actually is as an Application Type: what objects exist inside it, who operates it, how the supply plan is computed, reviewed, and released, what rules govern it, and where its boundary lies against Demand Planning, the Supply Chain Planning Platform, Inventory Management Systems, APS/Production Planning, ERP, and execution systems.

This pass runs after the supply-chain-planning-platform pass (2026-09-08), which flagged this leaf for joint review as a possible capability slice. This pass researches the supply side independently and answers the flag from this side.

## Initial Boundary

Working hypothesis at start:

- Core use: maintain the forward-looking plan of supply actions (what to buy, make, and move, where and when) that satisfies anticipated demand across the organization's supply network, and hand it to execution.
- Users: supply planners, purchasing/buyers (SMB), inventory planners, production planners, supply chain managers.
- Nearest neighbors: Demand Planning (§10 sibling), Supply Chain Planning Platform (§10 sibling, processed), Inventory Management System (§10, processed), Production Planning / APS (§16), ERP (§10, processed), Purchase Order Management / Procurement (§10), WMS/TMS (§10/§18), S&OP (inside the platform leaf).
- Known flags from prior passes:
  - supply-chain-planning-platform: "vs Supply Planning (§10 sibling, unprocessed) — symmetric slice question; joint-review flag."
  - advanced-planning-scheduling-aps: "Production Planning, Demand Planning, Supply Planning, Supply Chain Planning Platform (§10 siblings) share objects with APS; the boundary is the finite-capacity operation-level time assignment."
  - inventory-management-system: "planning decides what will be needed (forward-looking); IMS records what is and what moved."
- Open question: is this leaf a Type in its own right (standalone supply-planning products exist) or only a slice of the platform Type?

## Research Questions

1. What is the supply plan as an object? (time-phased planned orders — purchase / production / transfer)
2. What inputs does the engine net? (forecast/demand plan, open orders, distribution requirements, BOM component requirements, stock on hand, allocations/back orders, on-order/in-transit supply, firm planned orders)
3. What planning parameters shape the plan? (lead times, lot sizes/MOQs/order multiples, safety stock/stocking policies, capacities, calendars)
4. What does the planner actually do? (review recommendations, validate against projections, adjust with justification, release to ERP)
5. How does the plan flow to execution, and what comes back? (firm → purchase/production/transfer orders; actuals flow back; re-plan)
6. Where is the boundary vs Demand Planning, vs the platform leaf, vs IMS replenishment, vs APS, vs ERP-embedded MRP?
7. Historical check: do MRP-era and spreadsheet-era supply planning satisfy the definition? Is the paper-era reorder point correctly excluded?
8. How do the poles differ (network optimization vs MRP netting vs forecast-driven replenishment vs probabilistic inventory optimization)?

## Representative Products

Selected for market representation, documentation depth, product philosophy, and customer-tier diversity:

| Product | Tier / philosophy | Evidence depth obtained |
|---|---|---|
| Kinaxis (Maestro / RapidResponse) | Enterprise; concurrent planning; supply planning as named application | Tier 2 (supply planning solution page) |
| SAP Integrated Business Planning (IBP) | Enterprise; integrated suite; "Response and Supply Planning" module | Tier 2 (product page + FAQ) |
| ToolsGroup (Decion / SO99+) | Mid-market; probabilistic inventory optimization | Tier 2 (root + solution navigation) |
| GMDH Streamline | SMB standalone; demand + MRP-style supply planning | Tier 2 (manufacturing solution page); docs unreachable |
| Netstock | SMB/mid-market; ERP-companion replenishment planning | Tier 1 (public help center: collection index + 2 full articles) |

Rejected/considered: Blue Yonder (docs login-gated per prior pass), o9 (docs gated, marketing-heavy), Microsoft Dynamics 365 master planning (learn.microsoft.com paths 404 ×3 — abandoned per network rules; would have been the ERP-embedded pole), Anaplan (platform, not supply-specific), EazyStock (replenishment-only, thinner than Netstock).

## Sources

Tier 1 (operational documentation):
- Netstock Help Center — Ordering & Replenishment collection — https://help.netstock.com/en/collections/18733735-ordering-replenishment
  - "The Recommended Order Quantity (ROQ) Calculation Explained" — https://help.netstock.com/en/articles/12458728-the-recommended-order-quantity-roq-calculation-explained
  - "How To: Review, Adjust, and Finalize an Order Schedule" — https://help.netstock.com/en/articles/12561059-how-to-review-adjust-and-finalize-an-order-schedule

Tier 2 (official product/positioning pages):
- Kinaxis supply planning — https://www.kinaxis.com/en/solutions/supply-planning
- SAP IBP — https://www.sap.com/products/scm/integrated-business-planning.html (incl. FAQ; fetched directly this pass)
- ToolsGroup — https://www.toolsgroup.com/ (Supply Planning solution category: MEIO / Replenishment / Production Planning / Supplier Collaboration)
- GMDH Streamline — https://gmdhsoftware.com/solutions/manufacturing/

Source-access limitations (recorded per evidence rules):
- SAP Help Portal (help.sap.com) is a JS-only shell (consistent with the platform pass and ERP pass); SAP evidence is positioning/FAQ level only. No SAP operational mechanics asserted.
- Kinaxis operational docs (knowledge.kinaxis.com) are login-gated; evidence is positioning level.
- GMDH Streamline webhelp (streamline.gmdh.space) transport-failed ×2; abandoned per network rules. Streamline evidence is feature-vocabulary level from official product pages.
- Microsoft Learn (Dynamics 365 master planning) 404 ×3 on attempted paths; abandoned. The ERP-embedded pole is therefore evidenced only indirectly (via SAP's "classic MRP" framing and Streamline's MRP vocabulary).
- Netstock is the only sample with directly observable operational mechanics; findings from it are marked product-specific where they may not generalize.

## Product Observations

### Kinaxis (Maestro / RapidResponse) — evidence layer A (supply planning solution page), positioning

- Supply planning positioned as "resilient and responsive planning": "Go beyond simply balancing supply and demand… aligns strategies, improves service, reduces inventory, and shifts your focus from reacting to proactively solving challenges."
- "Intelligent trade-off analysis": evaluate competing objectives — simultaneously maintain service levels, control costs, and optimize inventory.
- "Unified data for comprehensive visibility": real-time data from across the supply chain in a single platform; planners optimize decisions and align stakeholders.
- "Confidence in every choice": scenario analysis — "evaluate multiple options instantly, weigh trade-offs, and confidently choose the best path forward."
- Supply is one application beside Demand, Inventory, S&OP, Scheduling, Control Tower, Order Management, Returns, TMS on the Maestro platform.
- (Platform pass, same vendor family: customer quote describes the chain "convert those forecasts into a supply plan, then convert that supply plan into an execution plan, fulfillment, logistics, transport, warehousing, order management.")

### SAP Integrated Business Planning — evidence layer A (product page + FAQ), positioning

- Key benefit: "Empower planners with multilevel supply planning — Create an effective supply plan for your entire network by modeling across locations and multilevel bills of material. Boost agility with response management."
- Key-features group "Response and supply planning": multilevel planning, supply planning, rough-cut planning, response management.
- FAQ: "Response and supply planning: SAP IBP takes capacity constraints, lead times, and inventory levels into account so that you can optimize production and distribution plans and more efficiently meet customer demands."
- Module list: demand management; response and supply planning; inventory management; S&OP; demand-driven replenishment (DDMRP); supply chain control tower.
- Named users: supply chain managers, demand planners, sales and operations planners, inventory managers, executives.
- Related-solution seam: "Production planning and detailed scheduling — Move beyond classic MRP with production planning and scheduling software. Plan production, incorporate capacity and material constraints" — a separate SAP product (the APS seam, confirmed from the vendor's own navigation).

### ToolsGroup — evidence layer A (root + solution navigation), positioning

- "Supply Planning: Right-size stock across your entire network with multi-echelon optimization, balancing service levels against holding costs with probabilistic safety stock."
- Supply Planning capabilities: Multi-Echelon Inventory Optimization, Replenishment, Production Planning, Supplier Collaboration.
- Demand Planning is a separate solution category (probabilistic forecasting, demand sensing/shaping); Strategic Planning holds S&OP, S&OE and Response Planning, IBP, Network Design.
- Confirms the market itself sells "Supply Planning" as a named category whose content is: replenishment + inventory optimization + production planning + supplier collaboration.

### GMDH Streamline — evidence layer A (manufacturing solution page), feature vocabulary

- "Material requirements planning — Ensure that you have the right parts available on time and are able to ship finished goods to your customers as promised."
- "Automate MRP — streamline your material requirements plan and issue purchase orders on time."
- "Flexible manufacturing — Make to order or make to stock based on demand forecast."
- "Batch manufacturing — Round up manufacturing orders to batch size and account for minimum batch."
- "Optimal inventory levels — Avoid unnecessary overstock while ensuring you have sufficient levels of inventory to cover future demand on time."
- "Agile safety stock — Keep safety stock with materials, finished products, or intermediates."
- Demand forecasting "by product and customer" as the input side.
- Customer testimonials frame the before-state as manual Excel calculation of purchasing requirements; "supply planners" named as the users. The product replaces the forecast + MRP spreadsheet.

### Netstock — evidence layer A (Tier 1, directly observed operational mechanics)

**The recommendation engine (ROQ article, directly observed):**

- The Recommended Order Quantity (ROQ) is "a data-driven calculation, not a fixed value," computed per stocked item from demand forecasts, supplier performance, and stock positions. It answers: "How much must I order today to reach my target stock level for the cover forward period?"
- Three inputs: Ideal Levels in days on the Policy panel (safety stock, lead time, replenishment cycle); Net Stock on the Inventory Position panel; supplier constraints on the Status panel.
- Ordering levels in days: Reorder Point = SS + LT (when to order); Order Up To Level = SS + LT + RC (how much to order). Days convert to units via the forecast: Units = Days × Daily forecast.
- Multiple demand streams per item: Sales Forecast, Distribution Forecast (downstream branches' required supply), BOM Forecast (component usage in production).
- Net Stock = true inventory position: Available stock = Stock on hand − Back orders − Allocated stock; Net stock = Available stock + On order. "Net Stock is not Stock on Hand."
- Ideal order: if Net Stock < Reorder Point → ROQ = Order Up To Level − Net Stock; else ROQ = 0.
- Supplier constraints adjust the ideal order: Minimum Order Quantity (MOQ) and Order Multiple (OM) can raise the recommendation above the ideal (documented example: ideal 800 → recommended 1,080 under MOQ 1,000 / OM 120).
- Item-class logic: non-stocked items order only when Net Stock < 0 (target net stock = 0); obsolete items never receive recommendations.
- Watchouts documented by the vendor: reviewing only stock on hand misleads; constraints explain unexpectedly large orders; non-stocked/obsolete use different logic.

**The planner review-and-release loop (order schedule article, directly observed):**

- "Once an order schedule is created, your role shifts from setup to validation… This step bridges planning and execution."
- 9-step documented workflow: (1) orient on the order schedule overview (supplier, location, Look Forward Days, total value/units/volume/weight) — "if the order looks fundamentally wrong at a high level, stop and reassess the inputs rather than editing line by line"; (2) prioritize lines (highest value, largest quantities, unsatisfied sales orders, critical classifications); (3) validate before adjusting (expand line context, preview future projected order timing, open Item Inquiry Projection tab: opening/closing stock, demand streams, suggested order dates and quantities, receipts and firm receipts, demand during lead time, safety stock, replenishment cycle); (4) adjust only with clear justification — "adjustments should be intentional, not habitual"; legitimate reasons are execution decisions (consolidating small future quantities, top-ups); all input-related issues (wrong supplier constraints, inaccurate/outdated forecasts, missing promotions, incorrect lead times, overstated safety stock, wrong fill-rate settings) "must be corrected at the source, not overridden on the order schedule"; "if the same item requires adjustment repeatedly, this indicates an upstream data, forecast, or policy issue"; (5) add top-ups (items that will trigger before the next review, container/discount fillers); (6) use the Solver to reach a target value/volume/weight; (7) review the summary (app quantities vs amended quantities, value/volume/weight deltas); (8) download and finalize — export a file for ERP upload, send directly to the ERP, or both; "after download, the order moves from planning to execution"; (9) archive the order (prevents accidental reuse of outdated recommendations).
- Orders screen tabs: Order from suppliers (purchase orders) / Order from distribution centres (transfer orders) / Order from locations (internal sourcing) / Distribute excess (proactive redistribution of surplus).
- Watchouts: over-adjusting by habit; "quantities may look correct while delivery timing creates stockout exposure."

## Cross-product Comparison

| Structure | Kinaxis | SAP IBP | ToolsGroup | Streamline | Netstock | Reading |
|---|---|---|---|---|---|---|
| Supply-side planning model (items × locations × supply sources with parameters) | ✓ whole-network model | ✓ "across locations and multilevel BOMs" | ✓ network-wide | ✓ products/BOMs/suppliers | ✓ items/locations/suppliers/regions/BOMs | Universal → core |
| Forward demand requirements as the plan's target | ✓ (demand app upstream) | ✓ demand management module | ✓ demand planning category | ✓ demand forecast input | ✓ sales/distribution/BOM forecast streams | Universal → core |
| Time-phased planned orders (buy / make / move) | ✓ supply plans | ✓ "optimize production and distribution plans" | ✓ replenishment + production planning | ✓ MRP → purchase orders + manufacturing orders | ✓ ROQ → order schedules (supplier/transfer/internal tabs) | Universal → core |
| Netting against stock position (on hand − commitments + on order) | ✓ (implied by unified data) | ✓ "inventory levels into account" | ✓ | ✓ | ✓ explicit (Net Stock formula) | Universal → core |
| Planner review/adjust before release | ✓ trade-off/scenario | ✓ simulations | ✓ | ✓ planner reviews MRP | ✓ 9-step review workflow | Universal → core |
| Release to execution systems (ERP) | ✓ | ✓ | ✓ | ✓ bi-directional ERP integrations | ✓ download/send to ERP + download status | Universal → core |
| Safety stock / stocking policy machinery | ✓ | ✓ inventory module | ✓ probabilistic safety stock + MEIO | ✓ agile safety stock | ✓ SS in policy panel | Common |
| Supplier constraints (MOQ, order multiples, lead times) | ✓ | ✓ "lead times" | ✓ supplier collaboration | ✓ minimum batch | ✓ MOQ/OM explicit | Common |
| Exceptions/alerts/prioritization | ✓ | ✓ alerts | ✓ | ✓ | ✓ urgency rating, unsatisfied-demand sorting | Common |
| What-if scenarios / simulation | ✓ signature | ✓ | ✓ (strategic tier) | ✓ (dynamic simulation) | solver/targets (thin) | Common |
| Rough-cut capacity checks | ✓ | ✓ rough-cut planning | ✓ production planning | batch rounding only | — | Common (enterprise) |
| Multi-echelon inventory optimization | ✓ | ✓ | ✓ signature | — | — | Optional |
| DDMRP | — | ✓ module | — | — | — | Optional |
| Response management / short-horizon deployment | ✓ | ✓ response management | ✓ S&OE/Response category | — | ✓ distribute excess (thin) | Optional |
| Probabilistic/service-level-driven policy setting | — | — | ✓ signature | — | ✓ target fill rate (thin) | Optional (philosophy pole) |
| Finite-capacity operation-level scheduling | ✓ Scheduling module | separate SAP product | — | — | — | Optional module = APS seam |
| Supplier collaboration portals | — | — | ✓ | — | — | Optional |
| AI agents / automated planning | ✓ AI-infused | ✓ ML | ✓ agentic execution | "AI-powered" | AI pack | Common (era-current) |

## Canonical Model (L0–L3)

### L0 — Defining Invariant (minimal)

A Supply Planning application is the organization's supply-response planning system: it maintains the time-phased plan of what to buy, make, and move — across the supply network, against anticipated demand — and hands that plan to execution systems. Three jointly-held structures:

1. **The supply-side planning model** — the organization's items/SKUs, locations, and supply sources (suppliers, production/BOM links, transfer/distribution links) held with planning parameters (lead times, lot sizes/MOQs/order multiples, safety-stock/stocking policies, capacity parameters) as the substrate on which the supply plan is computed.
   Remove → order calculators with no network to plan against.
2. **The demand requirements it must satisfy** — a time-phased forward demand picture over the planning horizon (forecast from demand planning, plus open orders, distribution requirements, and component/BOM requirements), held or imported and maintained.
   Remove → reorder-point replenishment on history alone (inventory-management territory); no forward-looking supply response.
3. **The supply plan of record** — time-phased planned orders (buy / make / move) computed by netting demand requirements against stock, in-transit/on-order supply, and policies; reviewed and adjusted by planners; released to execution systems (ERP procurement/production/warehouse). The application plans; it never executes.
   Remove → demand planning only (sibling leaf); or a forecast archive with no supply response.

Jointly-held is load-bearing:
- 1 alone = a network parameter catalog with no plans.
- 2 alone = Demand Planning (sibling leaf).
- 3 without 1+2 = a reorder-point engine.
- 1+2 without 3 = network + forecast with no supply response.
- 1+3 without 2 = replenishment calculation without a forward demand picture (classic reorder-point MRP-lite).

### L1 — Common Mature Structure

- Netting engine over the inventory position (on hand − allocations/back orders + on order/in-transit) — the net-requirements calculation
- Safety stock / stocking policy machinery (service-level targets; multi-echelon in enterprise products)
- Supplier constraint handling (MOQs, order multiples, lead times, supplier calendars)
- Exception/alert surfaces and prioritization (shortages, late orders, expedites, urgency ratings)
- What-if scenario analysis and simulation
- ERP integration both directions (import master data/stock/orders; export released orders; download-status tracking)
- Dashboards/KPIs (projected stock, service risk, order value/volume)
- Rough-cut capacity checks (enterprise)
- S&OP handoff surfaces (aggregate supply vs demand reconciliation)
- AI/ML-era assistance (demand sensing feeding the plan, AI trade-off analysis, agentic execution)

### L2 — Variant / Optional Structure

- Multi-echelon inventory optimization (MEIO)
- Probabilistic/service-level-driven policy setting as the product's center of gravity
- DDMRP buffer management
- Response management / short-horizon deployment, allocation, available-to-promise
- Optimization-based vs rule-based (MRP-style) engine philosophies
- Production planning depth (BOM explosion, make-to-order vs make-to-stock, batch rounding)
- Distribution/transfer planning depth (deployment, excess redistribution)
- Supplier collaboration portals
- Control tower / real-time visibility adjacency
- Container building, batch rounding, excess redistribution (SMB-oriented mechanics)
- Finite-capacity scheduling module (the APS seam — see Boundary Findings)

### L3 — Vendor-specific (research notes only)

- Kinaxis: "concurrency" architecture; Maestro branding; trade-off analysis framing; Planning One mid-market packaging.
- SAP IBP: module naming (Response and Supply Planning); HANA basis; rough-cut planning; DDMRP module; separate PP/DS product for detailed scheduling; "classic MRP" framing for the ERP-embedded ancestor.
- ToolsGroup: probabilistic forecasting; MEIO as signature; Decion platform / Decy agent branding.
- GMDH Streamline: GMDH proprietary forecasting; batch manufacturing rounding; QuickBooks/Fishbowl positioning; free desktop edition.
- Netstock: ROQ calculation; Cover Forward Period (LT+SS+RC); Look Forward Days; Top-Up Orders; Solver; Supplier Urgency Rating; Ordering Policy Panel; Saved Orders snapshots; Distribute Excess tab; Container Builder; 9-step order-schedule workflow.

## Evidence → Assertion Mapping

- Layer A (directly observed): all Netstock mechanics (Net Stock formula, ROP/OUT levels, days→units conversion, demand streams, MOQ/OM constraint behavior, non-stocked/obsolete logic, 9-step review workflow, download/archive, watchouts); product-page feature claims of the other four (their own descriptions of their supply planning capabilities).
- Layer B (cross-product commonality): supply-side planning model; forward demand requirements; time-phased planned orders; netting; planner review loop; ERP release; safety-stock machinery; supplier constraints; exceptions; scenarios — observed across 4–5 of 5 products.
- Layer C (canonical inference): the three-leg L0; the "planning system plans, execution systems execute" division; the bucketed-network vs operation-level seam against APS; the forecast-consumes vs forecast-produces seam against Demand Planning.

## Boundary Findings

1. **vs Demand Planning (§10 sibling, unprocessed)** — the sharpest seam. Demand planning produces the forecast (what will be needed); supply planning produces the response (what to buy/make/move to satisfy it). The demand plan is supply planning's input, not its record of record; the supply plan is supply planning's record of record. Remove the supply response → Demand Planning. Remove the forecast ownership → Supply Planning. Standalone products exist on both sides (ToolsGroup-class demand specialists; Netstock/Streamline-class supply-side tools), and both poles are sold under the two names by the same vendors (ToolsGroup, Kinaxis, SAP all carry both as separate solution categories). Type-level distinct; jointly-held seam.
2. **vs Supply Chain Planning Platform (§10 sibling, processed)** — the platform pass's L0 holds all three legs (network model + demand plan + supply plan) in one reconcilable whole with S&OP consensus machinery. This leaf is the supply-response domain application: it holds legs 1+3 as its own record and consumes leg 2. The platform pass's joint-review flag is answered from this side: keep both — the platform as the integrated whole, Supply Planning as the supply-domain Type that also exists standalone (Netstock, Streamline, legacy MRP engines). The two Types interlock: platform supply modules ARE supply planning embedded in the whole.
3. **vs Inventory Management System (§10, processed)** — consistent with the IMS pass: IMS holds stock records of what is and what moved, with rule-triggered replenishment; supply planning holds the forward time-phased plan of what will be needed and computed supply actions. The L0 leg-2 removal test (no forward demand picture → reorder-point replenishment) is exactly the IMS boundary. Netstock itself demonstrates the seam: its engine is reorder-point-shaped (ROP/OUT) but is driven by a maintained forward forecast across multiple demand streams — the forecast is what makes it supply planning rather than IMS.
4. **vs Production Planning / APS (§16)** — supply planning produces aggregate, bucketed, network-level planned orders (what to make, roughly when); APS/production planning assigns operations to finite capacity at operation-level time inside the plant. SAP's own navigation confirms the seam: IBP does network supply planning; "production planning and detailed scheduling" is a separate product that "move[s] beyond classic MRP." Kinaxis ships Scheduling as a separate module. When an SCP vendor adds finite-capacity scheduling, that module is APS territory embedded in the suite (consistent with the platform pass's resolution of the APS flag).
5. **vs ERP (§10, processed)** — consistent with the ERP pass: ERP planning is replenishment-level (MRP-style) on a transactional document core; dedicated supply planning centers on forecast depth, network scope, optimization, and scenario work. ERP is both the data source and the release target: planned orders are firmed into ERP purchase/production/transfer orders, which the ERP executes. The ERP-embedded MRP is the historical ancestor implementation of the same planning logic (see Historical Check).
6. **vs Purchase Order Management / Procurement (§10)** — procurement executes buying (POs, suppliers, receiving); supply planning decides what and when to buy before any PO exists. The planned order becomes a PO only at release.
7. **vs WMS / TMS (§10/§18)** — execution of movement vs planning what should move. Planned transfers/shipments may hand off to TMS/WMS; no shipment/warehouse objects are native to supply planning.
8. **vs S&OP (inside the platform leaf)** — S&OP is the cross-functional consensus process reconciling demand/supply/financial views; supply planning feeds it the supply-side view. A consensus process is not a supply plan.
9. **vs Control tower / visibility platforms** — visibility observes actuals and alerts; supply planning decides the future. Visibility modules appear inside planning suites (L2) but a visibility-only product is not this Type.

## Historical / Market-Sample Check (§24)

- 1970s–80s MRP: item master + BOM + inventory records + master production schedule (from forecast and orders) + time-phased planned orders (planned purchase/production orders) + planner action messages and order release. Satisfies all three L0 legs (supply-side model, demand requirements as MPS, planned orders with planner review). No cloud/AI/scenarios needed. ✓ — MRP is the historical ancestor implementation of this Type's planning logic; SAP's own "classic MRP" framing and Streamline's "automate MRP" vocabulary confirm the lineage is still the market's reference point.
- Spreadsheet-era supply planning: forecast rows + netting formulas + planned-order rows + buyer review before ordering. Satisfies the legs in manual form; the software Type is the systematized realization (Streamline's testimonials document exactly this before-state). ✓
- Paper-era reorder-point planning (EOQ/ROP cards): has policies and order quantities but no time-phased forward demand picture — correctly excluded as the thin ancestor (matches the IMS-with-replenishment shape). ✓
- Modern AI-era platforms: satisfy the legs with richer machinery; nothing era-specific is in L0. ✓

The definition survives the historical check; no re-abstraction needed.

## Uncertainties

1. Exact workflow mechanics are Tier-1-verified only for Netstock (SMB pole). Enterprise platforms' operational mechanics (Kinaxis scenario workflow internals, SAP IBP planning areas/key figures, heuristic vs optimizer behavior) could not be observed (login-gated/JS shells). The final doc therefore describes enterprise behavior at process level, not UI level.
2. The Demand Planning sibling leaf is unprocessed; the slice-vs-variant decision for the platform/demand/supply trio is recorded for joint review (STATUS Boundary Issues). This pass answers the supply side: keep both, with the interlock documented.
3. Whether "response management" (short-horizon supply/deployment) belongs in this Type or is a separate response-planning Type: held at L2 (variant) because sampled vendors package it inside supply/response modules; no standalone response product was sampled.
4. Netstock's reorder-point-shaped engine raises a definitional nuance: a forecast-driven ROP/OUT engine still satisfies L0 (forward demand picture + network model + planner-governed plan). The seam against IMS is the maintained forward demand picture, not the engine's mathematical shape.
5. Market-share/analyst claims (Gartner MQ positioning) are vendor-quoted and used only as market-representation evidence, not as structural evidence.

## Final Synthesis

A Supply Planning application is the organization's supply-response planning system. It holds a planning model of the supply side (items, locations, supply sources, planning parameters), takes on a time-phased forward demand picture as the target (forecast plus open orders, distribution requirements, and component requirements), and computes from these a time-phased supply plan — planned purchase, production, and transfer orders — by netting demand against stock, in-transit supply, and policies. Planners review the plan (exceptions first, validated against projections, adjusted only with justification), then release it to execution systems, where it becomes real purchase/production/transfer orders. The application plans; it never executes. Around this core, mature products add safety-stock and policy machinery, supplier constraints, exception prioritization, scenario simulation, dashboards, and rich ERP integration; enterprise suites extend into multi-echelon optimization, response management, and — crossing into the APS Type — finite-capacity scheduling. The Type is distinct from Demand Planning (produces the forecast vs consumes it), from the Supply Chain Planning Platform (the integrated whole vs the supply-domain application), from Inventory Management Systems (records what is vs plans what will be needed), from APS (network-level bucketed orders vs operation-level finite scheduling), and from ERP/procurement (system of forward plan vs system of record and execution). Its relationship to the platform and Demand Planning siblings is interlocking slice-of-whole and is answered from this side as keep-both, with joint review recorded.
