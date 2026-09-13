# Research Notes — Supply Chain Planning Platform

Research date: 2026-09-08
Slug: supply-chain-planning-platform
Directory leaf: Supply Chain Planning Platform (§10 Enterprise Operations & Administration)

## Research Goal

Understand what a Supply Chain Planning Platform actually is as an Application Type: what objects exist inside it, who operates it, how the planning work flows from data to plan to execution, what rules govern the plan, and where its boundary lies against ERP planning, APS, demand/supply planning siblings, inventory management, and execution systems (TMS/WMS).

## Initial Boundary

Working hypothesis at start:

- Core use: maintain a forward-looking plan for an organization's supply network — forecast demand, derive supply/replenishment plans, reconcile them (S&OP), release to execution.
- Users: demand planners, supply planners, inventory planners, S&OP leads, planner-buyers (SMB), supply chain managers, executives.
- Nearest neighbors: Demand Planning (§10 sibling), Supply Planning (§10 sibling), APS (§16), ERP (§10), Inventory Management System (§10), WMS/TMS (§10/§18), Supply Chain Control Tower / visibility, FP&A.
- Known flags from prior passes:
  - advanced-planning-scheduling-aps flagged joint review: "Production Planning, Demand Planning, Supply Planning, Supply Chain Planning Platform (§10 siblings) share objects (orders, resources, materials, calendars) with APS; the boundary is the finite-capacity operation-level time assignment."
  - enterprise-resource-planning-erp: "planning inside ERP is replenishment-level (MRP-style); dedicated planning Types center on optimization/forecasting depth."
  - inventory-management-system: "planning decides what will be needed (forward-looking); IMS records what is and what moved… remove the forecast machinery and the planning Types collapse into IMS."
- Open taxonomy question: is this leaf the integrated whole of which Demand Planning and Supply Planning (both separate §10 leaves) are slices? Both siblings unprocessed at time of research.

## Research Questions

1. What are the core objects? (planning model, forecast, supply plan, planned orders, scenarios, policies)
2. What is the canonical work loop? (data in → model → demand plan → derived supply plan → review → release → monitor)
3. What role does the ERP play? (data source + release target; planning system does not execute)
4. How do enterprise platforms (concurrent planning, IBP) differ from SMB replenishment-centric products — and what survives as Type-level structure?
5. Where exactly is the APS boundary (bucketed network planning vs operation-level finite scheduling)?
6. Where is the boundary against the Demand Planning / Supply Planning sibling leaves?
7. What is S&OP inside this Type — definitional or common mature structure?
8. Historical check: do MRP-era and spreadsheet-era planning satisfy the definition?

## Representative Products

Selected for market representation, documentation depth, product philosophy, and customer-tier diversity:

| Product | Tier / philosophy | Evidence depth obtained |
|---|---|---|
| Kinaxis (Maestro / RapidResponse) | Enterprise; concurrent planning; Gartner SCP MQ Leader | Tier 2 (product + technique + solution pages) |
| SAP Integrated Business Planning (IBP) | Enterprise; integrated business planning on HANA | Tier 2 (product page + FAQ); help portal JS-shell |
| Logility | Mid/enterprise; end-to-end planning suite | Tier 2 (root + S&OP solution page) |
| GMDH Streamline | SMB/mid-market; demand + inventory + MRP-style planning | Tier 2 (root + manufacturing solution page); docs 404 |
| Netstock | SMB/mid-market; replenishment-centric supply & demand planning | Tier 1 (public help center: collections + 3 full articles) |

Rejected/considered: Blue Yonder (docs login-gated), o9 (marketing-heavy, docs gated), ToolsGroup (demand-side specialist — would fit Demand Planning sibling better), Anaplan (platform, not SCP-specific).

## Sources

Tier 1 (operational documentation):
- Netstock Help Center — https://help.netstock.com/en/ (collections index)
  - Ordering & Replenishment collection — https://help.netstock.com/en/collections/18733735-ordering-replenishment
  - Forecasting collection — https://help.netstock.com/en/collections/18733700-forecasting
  - "Understanding Order Creation and Review" — https://help.netstock.com/en/articles/13158373-understanding-order-creation-and-review
  - "Demand Streams Explained: Sales, Distribution, & BOM" — https://help.netstock.com/en/articles/12457264-demand-streams-explained-sales-distribution-bom
  - "Mastering Forecasting" — https://help.netstock.com/en/articles/12528486-mastering-forecasting

Tier 2 (official product/positioning pages):
- Kinaxis — https://www.kinaxis.com/en ; concurrency technique — https://www.kinaxis.com/en/our-technique-concurrency ; supply planning — https://www.kinaxis.com/en/solutions/supply-planning
- SAP IBP — https://www.sap.com/products/scm/integrated-business-planning.html (incl. FAQ section)
- Logility — https://www.logility.com/ ; S&OP — https://www.logility.com/solutions/scenario-planning/sop/
- GMDH Streamline — https://gmdhsoftware.com/ ; manufacturing — https://gmdhsoftware.com/solutions/manufacturing/

Source-access limitations (recorded per evidence rules):
- SAP Help Portal (help.sap.com/docs/SAP_INTEGRATED_BUSINESS_PLANNING) returned a JS-only shell; SAP IBP product tour page is a JS demo shell. SAP evidence is therefore positioning/module/user-level only; no operational SAP mechanics are asserted anywhere.
- GMDH Streamline documentation paths 404'd (3 attempts: /documentation-supply-chain-planning-software/, /documentation/, /features/); abandoned per network rules. Streamline evidence is feature-vocabulary level from official product pages.
- Kinaxis operational docs (knowledge.kinaxis.com) are login-gated; evidence is positioning/philosophy level.
- Logility detailed docs gated; evidence is suite-structure + S&OP process level.
- Netstock is the only sample with directly observable operational mechanics; findings from it are marked product-specific where they may not generalize.

## Product Observations

### Kinaxis (Maestro / RapidResponse) — evidence layer A (product pages), positioning

- Positions as "the AI-powered platform for supply chain planning and decisioning," Leader in the 2026 Gartner MQ for Supply Chain Planning Solutions (discrete + process industries).
- Signature technique "concurrency": "a model that takes into view the whole supply chain network and aligns data and people so that a change in one area triggers corresponding changes and communications in the rest of the chain, in real-time." What-if scenarios with whole-network impact "in moments"; "instantly propagate the results across your supply chain."
- "Create and manage synchronized plans across time horizons, business processes and organizational boundaries at the same time, in real time, on one platform."
- Solution stack: Demand ("AI-powered demand sensing and forecasting to create realistic, consensus-based demand plans"), Supply ("agile supply plans for any scenario using advanced what-if scenario planning… and consequence analysis"; "go beyond simply balancing supply and demand"), Inventory ("deep inventory insights, event simulations and tradeoffs"), S&OP ("align functions and financial targets"), Scheduling (plant-specific), Control Tower (visibility), Order Management, Returns, TMS, Mid-Market "Planning One."
- Supply planning page: trade-off analysis (service levels vs costs vs inventory), unified real-time data, scenario analysis ("evaluate multiple options instantly, weigh trade-offs").
- Customer quote (Unilever): "convert those forecasts into a supply plan, then convert that supply plan into an execution plan, fulfillment, logistics, transport, warehousing, order management" — the plan-to-execution handoff chain.

### SAP Integrated Business Planning — evidence layer A (product page + FAQ), positioning

- "Cloud-based supply chain planning solution… integrates key aspects of the planning process including demand, supply, inventory, and sales and operations planning (S&OP)."
- Modules per vendor FAQ: demand management (historical data + market trends + predictive analytics → forecasts); response and supply planning ("takes capacity constraints, lead times, and inventory levels into account so that you can optimize production and distribution plans"); inventory management ("balancing the trade-offs between carrying costs, stockouts, and service levels"); S&OP ("unified platform for collaborative planning, allowing different departments to align on strategic goals and operational plans"); demand-driven replenishment (DDMRP buffers); supply chain control tower (real-time visibility).
- "Create an effective supply plan for your entire network by modeling across locations and multilevel bills of material."
- Capabilities: what-if simulations, alerts, supply chain analytics, ML/statistical models, demand sensing, outlier correction, rough-cut planning, response management, scenario comparison, performance monitoring.
- Named users: supply chain managers, demand planners, sales and operations planners, inventory managers, executives/decision-makers.
- S&OP: "Integrate financial and operational planning in one S&OP process. Run simulations of demand and supply changes."

### Logility — evidence layer A (root + S&OP page), suite structure

- "Single platform for planning, execution, and optimization"; end-to-end supply chain.
- Suite structure: Scenario Planning (Operational Scenario Planning, Decision Command Center, S&OP, S&OE), Demand Planning (DemandAI+, Demand Sensing), Inventory Optimization (InventoryAI+, MEIO, Automated Inventory Policies), Supply (Supply Optimization), Deployment (Intelligent Order Response, Allocation & Deployment), Supply Chain Design (Network Optimization), Manufacturing (Execution, Optimization), Supplier Management, Product (Merchandise Planning, PLM).
- S&OP page: "aligning plans across multiple divisions and locations with budgets and financial goals, track sales forecast and inventory performance over time and visualize true rough-cut capacity… build consensus among all stakeholders on critical changes to near-term forecasts and plans — providing instant insight into the effects on revenue projections, manufacturing capacities, and inventory levels… ensures the company operates on a unified plan."
- S&OE exists as a sibling process (short-horizon execution alignment).

### GMDH Streamline — evidence layer A (product pages), feature vocabulary

- "Integrated demand and inventory planning software for distributors, wholesalers, manufacturers, retailers, and ecommerce"; bi-directional ERP integrations (SAP, NetSuite, Dynamics, QuickBooks, Fishbowl, Odoo, etc.).
- Manufacturing features: material requirements planning ("automate MRP — streamline your material requirements plan and issue purchase orders on time"), flexible manufacturing (make-to-order / make-to-stock based on demand forecast), batch manufacturing (round up manufacturing orders to batch size), optimal inventory levels, demand forecasting (automatic, by product and customer), agile safety stock (materials, finished products, intermediates).
- Customer testimonials frame the before-state as Excel-spreadsheet planning of purchasing requirements — the product replaces manual forecast+MRP spreadsheets.

### Netstock — evidence layer A (Tier 1, directly observed operational mechanics)

Help-center structure (collections): ERP Integration & Data Management; Stocking Policies & Classifications; Forecasting; Supplier Management; Ordering & Replenishment; Dashboards & KPIs; Reports; Advanced Supply Chain ("create and manage regions & BOMs"); Configuration Settings; User Management; Security; IA Demand Planning.

Forecasting (directly observed):
- Demand streams per item per location: Sales (sells from the location in its own right), Distribution (location supplies branches — "the required supply for each branch, not the branch's sales forecast"), BOM (item is a component — "expected usage of the component in production"). Total demand used in orders = Sales + Distribution + BOM.
- The combined forecast converts lead time, safety stock, and replenishment cycle from days into units across the "cover-forward period" (LT + SS + RC); feeds the Recommended Order Quantity (ROQ) calculation.
- Forecast lifecycle: generated from history; adjusted at item or macro/group level; adjustments can be frozen (protected from regeneration) and defrosted (reverted); "Forecasts That Need Attention" flags; event correction after disruptions (pandemic/strike/supplier shutdown) corrects forecast and safety-stock inputs; forecast history and "shots" record past forecasts for accuracy measurement; forecast risk and offset feed safety stock.
- Advanced: multi-item manual adjustment, forecast disaggregation, group seasonal forecasting, extended planning horizon.

Ordering & replenishment (directly observed, 12-step documented workflow):
- Orders screen tabs: Order from suppliers (purchase orders) / Order from distribution centres (transfer orders) / Order from locations (source from internal locations) / Distribute excess (proactively redistribute surplus).
- Supplier urgency rating prioritizes review; filters/sorting by unsatisfied sales orders, urgency, value.
- Look Forward Days pulls future recommendations into today (with documented excess risk); Order Frequency / Review Period; Top-Up Orders for items between reorder point and order-up-to level; Solver to hit target value/volume/weight.
- Create Order → order schedule → review lines with Ordering Policy Panel (policy inputs behind each recommendation) → Item Inquiry / Projection tab (opening/closing stock, demand streams, suggested order dates and quantities, receipts and firm receipts, demand during lead time, safety stock, replenishment cycle).
- Finalize → download as CSV or send directly to ERP; download-status indicators (downloaded / partially downloaded / not actioned); Saved Orders snapshot inputs at creation — "if an order is not placed immediately, the recommendation may become outdated"; best practice: archive and regenerate.
- Watchouts documented by the vendor: outdated orders, overusing Look Forward Days creates excess, review frequency interactions.

Positioning: "Intelligent supply & demand planning… Turn ERP data into inventory intelligence"; dashboards for "supply, demand, and what you need to action next"; S&OP and Demand Planning sold as solution modules; 2,400+ customers, SMB/mid-market.

## Cross-product Comparison

| Structure | Kinaxis | SAP IBP | Logility | Streamline | Netstock | Reading |
|---|---|---|---|---|---|---|
| Planning model of the network (items × locations × supply links/parameters) | ✓ whole-network model | ✓ "across locations and multilevel BOMs" | ✓ divisions & locations | ✓ products/BOMs | ✓ items/locations/regions/BOMs | Universal → core |
| Time-phased forward demand plan (statistical + human adjustment) | ✓ consensus demand plans | ✓ demand management | ✓ Demand Planning | ✓ demand forecasting | ✓ forecast + adjustments/freeze | Universal → core |
| Derived supply/replenishment plan (planned buy/make/transfer) | ✓ supply plans | ✓ response & supply planning | ✓ Supply Optimization | ✓ MRP → purchase orders | ✓ ROQ → order schedules | Universal → core |
| Planner review/adjust before release to execution | ✓ scenario/trade-off | ✓ simulations | ✓ consensus | ✓ planner reviews MRP | ✓ 12-step review → export to ERP | Universal → core |
| ERP integration as data source + release channel | ✓ | ✓ | ✓ | ✓ bi-directional | ✓ bi-directional | Universal → core |
| S&OP / cross-functional consensus process | ✓ module | ✓ module | ✓ module (+S&OE) | marketed | ✓ module | Common (not in thin pole's documented core) |
| Inventory policy / safety-stock optimization | ✓ | ✓ | ✓ MEIO | ✓ safety stock | ✓ stocking policies | Common |
| What-if scenarios / simulation | ✓ signature | ✓ | ✓ | ✓ (dynamic simulation) | solver/targets (thin) | Common |
| Dashboards/KPIs/alerts | ✓ | ✓ | ✓ | ✓ KPIs | ✓ | Common |
| Demand sensing / ML forecasting | ✓ | ✓ | ✓ | "AI-powered" | AI pack | Common (era-current) |
| Control tower / real-time visibility | ✓ | ✓ | orchestration center | — | — | Optional |
| Multi-echelon inventory optimization | ✓ | ✓ | ✓ MEIO | — | — | Optional |
| DDMRP | — | ✓ | — | — | — | Optional |
| Deployment/allocation/ATP | — | ✓ (ATP adjacent) | ✓ Deployment | — | excess redistribution (thin) | Optional |
| Supply chain design / network optimization | — | — | ✓ | — | — | Optional |
| Finite-capacity operation-level scheduling | ✓ Scheduling module | separate SAP product | ✓ Manufacturing Optimization | batch rounding only | — | Optional module = APS seam |
| Execution modules (orders, TMS, returns) | ✓ | — | ✓ (Manufacturing Execution) | — | — | Optional, beyond planning |
| Supplier performance / lead-time monitoring | — | — | ✓ Supplier Management | — | ✓ | Optional |
| Merchandise/retail planning | — | — | ✓ | — | — | Optional (retail variant) |

## Canonical Model (L0–L3)

### L0 — Defining Invariant (minimal)

A Supply Chain Planning Platform is the organization's forward-planning system for its supply network. Three jointly-held structures:

1. **The supply network planning model** — the organization's items/SKUs, locations, and supply relationships (suppliers, bills of material, distribution links) held with planning parameters (lead times, stocking policies, batch/capacity parameters) as the substrate on which plans are computed.
   Remove → forecasting calculators and order calculators with no network to plan against.
2. **The maintained forward demand plan** — a time-phased expectation of demand per item × location (statistically generated, human-adjusted, revisable), answering "what will be needed, where, when."
   Remove → reorder-point replenishment on history alone (inventory-management territory); no forward-looking planning.
3. **The derived, planner-governed supply plan** — planned orders (what to buy, make, move, and when) computed from the demand plan against stock, policies, and network parameters; reviewed and adjusted by planners and released toward execution systems.
   Remove → demand planning only (sibling leaf); or a forecast archive with no supply response.

Jointly-held is load-bearing:
- 1 alone = a network data model / digital twin with no plans.
- 2 alone = Demand Planning (sibling leaf).
- 3 without 1+2 = reorder-point engine.
- 1+2 without 3 = forecasting tool.
- 1+3 without 2 = replenishment calculation without a forward demand picture (classic reorder-point MRP-lite).

### L1 — Common Mature Structure

- Statistical forecasting engine with accuracy measurement (forecast history, variance, accuracy shots)
- Safety stock / inventory policy machinery (service-level-driven targets; multi-echelon in enterprise products)
- What-if scenario analysis and simulation
- S&OP support: cross-functional consensus, reconciliation of demand/supply/financial views, rough-cut capacity
- Dashboards, KPIs, alerts, exception flags ("forecasts that need attention")
- ERP integration both directions (import master data/stock/orders; export released orders)
- Demand sensing / ML-era forecasting improvements
- Supplier lead-time and performance monitoring
- Role-based access and configuration layer (policies, classifications, users)

### L2 — Variant / Optional Structure

- S&OE (short-horizon execution alignment) as separate process tier
- Multi-echelon inventory optimization (MEIO)
- DDMRP buffer management
- Deployment / allocation / available-to-promise
- Supply chain design / strategic network optimization
- Control tower / real-time visibility layer
- Finite-capacity scheduling module (the APS seam — see Boundary Findings)
- Execution modules (order management, TMS, returns, manufacturing execution) in end-to-end suites
- Retail/merchandise planning flavor
- Batch-size rounding, container building, excess redistribution (SMB-oriented mechanics)
- AI agents / conversational planning assistants (era-current)

### L3 — Vendor-specific (research notes only)

- Kinaxis: "concurrency" architecture and in-memory simultaneous re-planning; Maestro branding; semantic graph/ontology; Planning One mid-market packaging.
- SAP IBP: HANA basis; module naming (S&OP, Demand, Response & Supply, Inventory, DDMRP, Control Tower); integration with SAP ERP/S4 and SAP ATP.
- Netstock: ROQ calculation, Cover Forward Period (LT+SS+RC), Look Forward Days, Top-Up Orders, Supplier Urgency Rating, Ordering Policy Panel, Saved Orders snapshots, Distribute Excess tab, Container Builder, Solver.
- GMDH Streamline: GMDH proprietary forecasting technology; free desktop edition; batch rounding; QuickBooks/Fishbowl positioning.
- Logility: DemandAI+/InventoryAI+ branding, LEA generative advisor, AppCentral, Orchestration Center, S&OE naming.

## Evidence → Assertion Mapping

- Layer A (directly observed): all Netstock mechanics (demand streams, freeze/defrost, ROQ inputs, 12-step order workflow, saved-order aging, download status); product-page feature claims of the other four (their own descriptions of their modules).
- Layer B (cross-product commonality): network planning model; demand plan; derived supply plan; planner review loop; ERP integration; S&OP; scenarios; dashboards — observed across 4–5 of 5 products.
- Layer C (canonical inference): the three-leg L0; the "planning system plans, execution systems execute" division; the bucketed-network vs operation-level seam against APS.

## Boundary Findings

1. **vs Demand Planning (§10 sibling, unprocessed)** — Demand planning is the forecast-producing slice of this Type's loop. Standalone demand-planning products exist (ToolsGroup-class). The platform leaf is defensible as the integrated whole (demand + supply + network + reconciliation under one plan), but the directory carries both siblings as separate leaves. **Flag for joint review**: either (a) platform = Type, siblings = capability slices documented as variants, or (b) all three are one Type family with the platform as the umbrella. This pass documents the platform as the integrated whole and records the sibling relationship.
2. **vs Supply Planning (§10 sibling, unprocessed)** — symmetric to #1 on the supply side. Same joint-review flag.
3. **vs APS (§16, processed)** — the APS pass's structural test holds from this side: SCP platforms plan at bucketed, network level (weeks/months, aggregate items, no operation-level time assignment). When an SCP vendor adds finite-capacity, operation-level scheduling (Kinaxis Enterprise Scheduling; Logility Manufacturing Optimization), that module belongs to the APS Type embedded in the suite. Resolves the APS pass's joint-review flag from this side: Type-level distinct, module-level overlap.
4. **vs ERP (§10, processed)** — consistent with the ERP pass: ERP planning is replenishment-level (MRP-style) on a transactional document core; the SCP platform is a dedicated forward-planning system centered on forecast depth, optimization, and scenario work. SCP consumes ERP data and releases plans back; it does not own the transactional documents of record. Suite vendors embed planning in ERP (L1 there), and SCP vendors integrate to ERP — the seam is "system of record vs system of forward plan."
5. **vs Inventory Management System (§10, processed)** — consistent with the IMS pass: IMS holds stock records of what is; SCP holds the plan of what will be needed. Replenishment suggestions can ride on IMS data; SCP's supply plan is forecast-driven and network-wide. The IMS leaf's "remove the forecast machinery and the planning Types collapse into IMS" test is exactly the L0 leg-2 removal.
6. **vs TMS / WMS (§10/§18)** — execution of movement vs planning what should move. SCP planned transfers/shipments may hand off to TMS; no shipment/warehouse objects are native to SCP.
7. **vs Control Tower / visibility platforms** — visibility observes actuals and alerts; SCP decides the future. Control-tower modules appear inside SCP suites (L2) but a visibility-only product is not this Type.
8. **vs FP&A / S&OP boundary** — S&OP inside SCP reconciles demand/supply/financial views, but the financial plan of record stays with FP&A systems; SCP owns quantities (units, orders, capacity), finance owns money. SAP's own framing ("integrate financial and operational planning in one S&OP process") describes integration, not ownership.
9. **vs supplier-risk-management (§10, processed)** — risk intelligence vs plan/execute; consistent with that pass's seam.

## Historical / Market-Sample Check (§24)

- 1970s–80s MRP: item master + BOM + inventory + MPS (from forecast and orders) + time-phased planned orders + planner action messages. Satisfies all three L0 legs (network model, demand plan as MPS, derived supply plan as planned orders, planner review). No cloud/AI/scenarios needed. ✓
- Spreadsheet-era S&OP: forecast rows + supply plan rows + reconciliation meetings on shared sheets. Satisfies the legs in manual form; the software Type is the systematized realization. ✓
- Paper-era reorder-point planning (EOQ/ROP cards): has policies and order quantities but no time-phased forward demand plan — correctly excluded as the thin ancestor (matches the IMS-with-replenishment shape). ✓
- Modern AI-era platforms: satisfy the legs with richer machinery; nothing era-specific is in L0. ✓

The definition survives the historical check; no re-abstraction needed.

## Uncertainties

1. Exact workflow mechanics are Tier-1-verified only for Netstock (SMB pole). Enterprise platforms' operational mechanics (e.g., Kinaxis scenario workflow internals, SAP IBP planning areas/key figures) could not be observed (login-gated/JS shells). Final doc therefore describes enterprise behavior at process level, not UI level.
2. The Demand Planning / Supply Planning sibling leaves are unprocessed; the slice-vs-variant decision is deferred to joint review (recorded in STATUS Boundary Issues).
3. Whether "S&OP" should be L1 or L0: held at L1 because the thin documented pole (Streamline's feature set; Netstock's core help structure) centers on demand→order mechanics, with S&OP as a marketed module. If the sibling passes show S&OP as the defining center, revisit.
4. Market-share/analyst claims (Gartner MQ positioning) are vendor-quoted and used only as market-representation evidence, not as structural evidence.
5. Netstock's "IA Demand Planning" collection suggests a newer AI demand module; not researched in depth (era-current, non-definitional).

## Final Synthesis

A Supply Chain Planning Platform is the organization's system for maintaining a forward-looking plan of its supply network. It holds a planning model of that network (items, locations, supply relationships, planning parameters), maintains a time-phased forward demand plan, derives from it a supply/replenishment plan (planned buy/make/transfer orders), and puts both under planner review and revision before releasing them to execution systems (ERP/procurement/production). Around this core, mature products add statistical forecasting depth, safety-stock and inventory policy optimization, scenario simulation, S&OP consensus support, dashboards/alerts, and rich ERP integration; enterprise suites extend into visibility, multi-echelon optimization, deployment, network design, and — crossing into the APS Type — finite-capacity scheduling. The Type is distinct from ERP (transactional system of record with replenishment-level planning), from IMS (stock records of what is), from APS (operation-level finite scheduling), and from execution systems (TMS/WMS). Its relationship to the Demand Planning and Supply Planning sibling leaves is slice-of-whole and is flagged for joint review.
