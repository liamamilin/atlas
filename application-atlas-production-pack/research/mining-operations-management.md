# Research Notes — Mining Operations Management

Research date: 2026-09-10
Slug: mining-operations-management
Directory leaf: Mining Operations Management (§20 Agriculture, Food & Natural Resources)

## Research Goal

Understand, from real products, what "Mining Operations Management" is as an Application Type: the mine's whole-operations production layer. What objects exist inside it (material movements, stockpiles, production records, plans, resource models), what the operational loop is (capture → balance → reconcile → report → feed back), which roles operate which surfaces, which states and rules matter, and where its boundaries sit against Mine Planning (upstream), Mining Fleet Management (fleet-level execution), Quarry Management (§20 sibling), MES / production accounting (cross-industry analogs), SCADA/historians (data substrate), and ERP (finance).

Special duties — three inherited flags to discharge:

1. **mining-fleet-management (processed 2026-09-10)**: "probable broader whole-mine sibling — hypothesis: whole-mine operations (production accounting, planning reconciliation, cost, compliance) vs fleet-level execution loop — joint review when that leaf is processed."
2. **mine-planning-application (processed 2026-09-09)**: "plan-of-record vs execution records; compliance-to-plan/reconciliation the handoff; Deswik.OPS short-term-planning+shift-execution sits ON the seam — boundary case left to that pass."
3. **quarry-management (processed 2026-09-09)**: "quarry management = product-sales loop…; mining operations software expected to center extraction/production reporting… — confirm the seam (and whether weighbridge-ticket machinery is shared-family capability) when that leaf is processed."

## Initial Boundary

Working hypothesis before research:

- Core use: software that holds the mine's **production system of record** — what was actually mined, moved, and processed — and reconciles it against the plan and the geological resource model, producing the trusted numbers the mine reports (daily/shift/monthly, corporate, audit).
- Market labels observed: "Mining Operations Management (MOM)" (Rockwell Automation's own category name), "mine production management and reconciliation" (GEOVIA's own category label for InSite), "Mine Reconciliation & Production Accounting" (Datamine page title), "Material tracking & reconciliation systems" (Maptek), "mine information management platform" (Datamine Centric).
- Likely users: mine geologists, surveyors, mine planners/engineers, metallurgists, production supervisors, mine controllers, technical services managers, executives.
- Nearest types: Mine Planning Application (upstream plan-of-record), Mining Fleet Management (live fleet execution), Quarry Management (aggregates product-sales loop), MES (manufacturing analog), SCADA/Industrial Historian (plant data substrate), ERP (finance), EHS (safety/environmental).
- Unknowns: is shift execution/SIC definitional or common? Is metal accounting definitional or metals-only? Where exactly does the FMS seam run (Pitram straddles it)? Is the resource-model reference (geological estimate) part of the core or a variant? Does cost management belong here?

## Research Questions

1. What are the core objects — material movements, stockpiles/stocks, production records, plans, resource model, reconciled measures?
2. What is captured, from which sources (fleet management/dispatch, plant control/historians, laboratories, surveys, manual entry)?
3. How does the material/metal balance work (stocks, additions/depletions/adjustments, genealogy source→destination)?
4. How does reconciliation work — what is compared (estimated/planned/mined/processed/reported), at what cadence, producing what (variances, reconciled measures)?
5. What roles use it and what surfaces exist (dashboards, movement screens, reconciliation workbenches, shift boards, reports)?
6. What rules matter (preservation of original records, audit trail, mass-balance conservation, source-data change propagation, approval workflows)?
7. How deep is shift execution / short interval control, and is it definitional?
8. How does the money dimension work (production accounting, inventory valuation, financial reporting feed)?
9. Boundaries: vs mine planning, mining fleet management, quarry management, MES, SCADA, ERP, EHS.

## Representative Products

Selected for market representation, documentation reachability, different product philosophies (specialist reconciliation vs tracking suite vs integrated platform vs automation-platform MOM), and different positions on the FMS seam:

| Product | Vendor / family | Pole | Evidence reached |
|---|---|---|---|
| Production Solutions (Centric + MineMarket + Reconcilor + Production Accounting) | Datamine | integrated "mining operations" suite; reconciliation/ore-accounting center; shift execution leg (Centric Ops) | A (multiple official pages + FAQ) |
| Maptek Resource Tracking (MaterialMRT / StockpileMRT / PlantMRT) | Maptek | material tracking & reconciliation specialist; resource-model connection | A (official product pages) |
| GEOVIA InSite | Dassault Systèmes | "mine production management and reconciliation"; plan-vs-actual KPI bridge; shift management | A (official datasheets, press release, blogs; product page 404) |
| Mining Operations Management Suite (MOM) | Rockwell Automation | automation-platform MOM; mining-dedicated modules (production/metal reporting, inventory/storage balances, SIC, downtime accounting) | A (official category blog + product references) |
| Pitram (Material Management + reconciliation) | Micromine | boundary case: FMS (mining-fleet-management Type) whose material/reconciliation modules reach into this Type | A (official blog + pages; FMS core evidenced in the mining-fleet pass) |

Market anchors named but not directly documentable this pass: Hexagon HxGN MineOperate OP Pro / MineEnterprise (403 + transport errors, consistent with the mine-planning and mining-fleet passes' records), Honeywell PAR and AspenTech AORA (cross-industry production accounting/reconciliation — adjacent capability pole), K-MINE (reconciliation + ERP integration), Deswik.OPS (short-term planning + shift execution — sits ON the planning seam; evidenced in the mining-fleet pass).

Rejected/considered: "Voxis/Vizari" — researcher memory artifact; search shows VOXI is a Geosoft geophysical inversion product, unrelated. SAP S/4HANA mining (ERP pole — related Type, not sampled).

## Sources

Tier 2 (official vendor surfaces) unless noted; all fetched 2026-09-10:

1. Datamine — Production Solutions: https://dataminesoftware.com/solutions/production (page title "Mine Reconciliation & Production Accounting Software")
2. Datamine — Reconcilor: https://dataminesoftware.com/reconcilor-by-datamine
3. Datamine — Reconcilor brochure (PDF): https://dataminesoftware.com/wp-content/uploads/2025/01/Reconcilor-brochure_EN_251701.pdf (via search)
4. Datamine — Centric documentation portal: https://docs.dataminesoftware.com/Centric/index.htm (via search)
5. Datamine — "Real-time mining decisions from a central hub": https://dataminesoftware.com/real-time-mining-decisions-from-a-central-hub (via search)
6. Datamine — "From Patchwork to Proactive" blog (Reconcilor product owner): https://dataminesoftware.com/from-patchwork-to-proactive-blog-series/ (via search)
7. Maptek — Resource Tracking: http://maptek.com/products/resource_tracking
8. Maptek — Smart material tracking: https://www.maptek.com/products/resource_tracking/material_mrt (via search; title "From in-ground resource to balance sheet")
9. Dassault — GEOVIA InSite datasheet (services PDF): https://www.3ds.com/fileadmin/PRODUCTS-SERVICES/GEOVIA/PDF/datasheet/About-Geovia.pdf (via search)
10. Dassault — GEOVIA services case study PDF (InSite implementation): https://www.3ds.com/fileadmin/PRODUCTS-SERVICES/GEOVIA/PDF/datasheet/GEOVIA-Services-Mining-Projects-0617.pdf (via search)
11. Dassault — press release, MINExpo 2012 (InSite 4.2): https://www.3ds.com/newsroom/press-releases/dassault-systemes-announces-new-capabilities-five-key-geovia-mining-applications-minexpo-2012 (via search)
12. Dassault — blog "InSite – Bridging the gap between Mine Planning KPI's and actual/event KPI's": https://blog.3ds.com/brands/geovia/insite-bridging-the-gap-between-mine-planning-kpis-and-actual-event-kpis (via search)
13. Dassault — blog "6 Steps to Effective Mine Production Management": https://blog.3ds.com/brands/geovia/6-steps-effective-mine-production-management-and-why-its-important (via search)
14. Rockwell Automation — "Mining's Digital Revolution: World-Class Operations Management": https://www.rockwellautomation.com/en-us/company/news/blogs/world-class-mining-operations-management.html
15. Micromine — "How Much Are Your Reconciliation Errors Really Costing?" (Pitram reconciliation): https://www.micromine.com/how-much-are-your-reconciliation-errors-really-costing
16. Micromine — Pitram product/Material Management pages (fetched in the mining-fleet pass, 2026-09-09; reused as cross-pass context)

Unreachable / limitations:

- 3ds.com GEOVIA InSite product page — 404 (1 attempt, abandoned). InSite evidence rests on other official 3ds.com surfaces (datasheets, press release, blogs).
- Hexagon Mining — not re-attempted; 403 + transport errors recorded by two prior passes (mine-planning 2026-09-09, mining-fleet 2026-09-09). Named anchor only.
- No Tier-1 help-center articles reached for any sampled vendor. All operational claims rest on Tier-2 official product pages, FAQs, and vendor blogs. Precise numeric limits, algorithm parameters, and default settings are NOT claimed anywhere.

## Product A — Datamine Production Solutions (Centric + MineMarket + Reconcilor + Production Accounting)

### Key observations (evidence layer A unless noted)

- Page title: "Mine Reconciliation & Production Accounting Software". Positioning: "Production Bundles bring together connected solutions across mining operations, processing, logistics and commercial workflows in one ecosystem."
- **Mining Operations Bundle** (the vendor's own packaging of this Type): "Bring day-to-day mine operations, material tracking and reconciliation into one connected workflow so mine geologists, supervisors and engineers can see performance, validate movements, and act earlier on deviations." Checklist: daily operations management and shift execution; production operations and performance metrics capture and analytics; material tracking, inventory management and blending support; mine and material reconciliation with plan compliance visibility. Includes MineMarket Inventory Management & Tracking, Reconcilor, Centric Ops, Centric Enterprise/Analytics.
- Production Applications menu: "Track and reconcile — Ore accounting, analytical and corrective reconciliation: Ore tracking and accounting; Stocks management; Mine and production reconciliation" (MineMarket, Centric, Reconcilor); "Perform to plan — Short interval control and performance to plan monitoring: Shift-by-shift planning and goal setting; End of shift handover management; Work progress and risk monitoring" (Centric); "Balance and reconcile — Plant metals reconciliation and accounting: Metals reconciliation and balancing; Plant performance monitoring; Metals recovery" (Production Accounting, Reconcilor, Centric); plus Logistics and Contracts (MineMarket), Enterprise Reporting (Centric), Information management (Scenario).
- FAQ — scope: "manage the flow of production information from operational execution through to processing, reconciliation, logistics, commercial reporting and decision-making"; workflows "across short interval and shift execution, material tracking, stockpile and inventory management, mine and plant reconciliation, metallurgical accounting, plant performance reporting, transport and shipment management, contract-linked material visibility and executive reporting."
- FAQ — the record: "production information including tonnes, grades, material movements, stockpiles, plant feed and final production results can be captured, validated and shared through governed workflows."
- FAQ — plan vs actual: "connecting operational plans with actual production data as work is executed… whether planned tonnes, grades, material movements, stockpile changes, plant feed, recoveries, shift activities and production KPIs are being achieved, rather than relying only on delayed end-of-period reports… use actual performance data to improve future plans."
- FAQ — reconciliation: "connecting geological models, mine plans, production activities, material movements and plant outcomes. By comparing estimated, planned, mined, processed and reported values."
- FAQ — trust machinery: "validation, traceability, auditability and approval workflows that help teams understand where production figures originate and how they were calculated."
- **Reconcilor** (reconciliation specialist): "centralises geology, mining, and processing data to deliver accurate, auditable production reconciliation across the entire mining value chain"; "tracks material movements from resource models and mine planning through drilling, blasting, hauling, stockpiling, and processing, giving full visibility from orebody to final metal production"; "highlights differences between planned and actual tonnes, grades, and production, helping teams pinpoint and reduce dilution, ore loss"; "consolidates data from multiple mines to provide standardised reconciliation and consistent corporate reporting"; integrates "geological databases, mine planning systems, fleet management systems, and plant control systems"; data sources "SQL databases, web services, REST APIs, Excel, and CSV files"; "configurable dashboards and reporting tools for daily, weekly, and monthly production reports"; web-based, on-premises today (SaaS "due 2026-27" per its own FAQ); users "Geologists, mine planners, mining engineers, metallurgists, and management teams."
- Reconcilor brochure: "continuum screen provides a complete, easy-to-understand view of your mining process, from resource extraction to the final product"; inputs "Geological models, Mine plans, Dispatch, Plant movements and sampling, Optionally: transport and shipping, Surveys"; "Geological model reconciliation"; "Built-in data validation"; "compare tonnes, grades, and metal at each handover point, trace discrepancies"; "audit-ready outputs… into every workflow"; JORC framing ("The upcoming JORC Code updates are expected to formally make mine reconciliation a core reporting requirement"; blog: "JORC Clause 10.1? Covered").
- **Centric** (mine information management platform): "used by supervisors, operators, geologists, engineers, planners, managers, and executives… integrates existing systems into a unified decision support network, providing real-time visibility of KPIs and operational metrics from pit to port"; "delivers sustainable ore accounting, operational reporting, and analytics, allowing users to monitor performance, analyze non-compliance, and take corrective actions"; "Centric Enterprise… unifying disconnected mining systems and manual processes into a single, governed source of truth across the entire mining value chain"; "Centric Ops adds shift planning, activity metrics, equipment status, operational events and handover context. Centric Mobile supports field data capture, including offline use."
- Timesheet/activity recording: "implementing your own business rules in timesheet data entry… automated payroll and incentives" (why-choose section).
- Processing bundle references AMIRA P754 ("Metals balancing and accounting aligned to AMIRA P754") — the industry metal-accounting code of practice, vendor-referenced.
- Customer quote (Fortescue): "we've built a transparent, trusted data pipeline that gives us full visibility from the resource model to the crusher, and soon, all the way to shipping."

## Product B — Maptek Resource Tracking (MRT)

### Key observations (evidence layer A unless noted)

- Label: "Material tracking and reconciliation systems"; sits in Maptek's **Operations** stage ("Improve performance by tracking materials and monitoring production with pinpoint precision to close the loop between plan and execution").
- "Accurate, real-time production performance tracking and visualisation… through load and haul, stockpiling and plant processes by connecting each of these processes with your resource model and reconciliation between each stage."
- "close the loop with effective, real time reconciliation of inventory and qualities through the mining, blending and processing stages."
- "Measuring and validating actual material movements near-live at every stage of the mine value chain."
- "accurately reconcile production performance with the strategic mine plan and resource model"; "Reconcile tonnes and quality, and track compliance to plan across your operation."
- "Improved stockpile planning, management and reconciliation; Reconciliation against the resource model and strategic mine plan."
- Problem framing: "Traditional material tracking systems are disconnected from the resource model and planning systems… A disconnected set of systems tracking production activity and performance introduces latency, inaccuracy and ambiguity."
- Three components (deployable individually or as "an integrated enterprise system with centralised, live reporting"):
  - **MaterialMRT** — "tracking quality and inventory of discontinuous material flows from in situ rock to ROM stockpiles and plant feed. Connects resource model, mine plans, fleet management, on-belt analysers, survey and laboratory results. Web-based 3D visualisation, live dashboards and interface to data warehousing."
  - **StockpileMRT** — "managing quality and quantity of discrete stockpiles."
  - **PlantMRT** — "managing continuous material flows for processing plants. Connects SCADA historian, planning and laboratory information systems."
- "single source of truth for material movement reconciliation" (Forge article).
- material_mrt page title: "Smart material tracking — From in-ground resource to balance sheet."
- Case studies: coal/waste/rejects placement compliance (Meandu); "real-time reconciliation of material quantity and quality" at an iron ore mine (Sishen); stockpile stage-cycle scheduling ("better manage space, grade and inventory").
- Companion: PETRA MAXTA ("predicted performance, optimisation and recommendations based on the actual behaviour of your mine and plant using machine learning") — add-on, not core.
- Historical note (cross-pass): Maptek's older MineSuite was explicitly labeled an **MES** ("production execution, management and reporting solutions with the MineSuite MES", 2008) — the same seat has migrated from MES vocabulary to tracking/reconciliation vocabulary.

## Product C — GEOVIA InSite (Dassault Systèmes)

### Key observations (evidence layer A unless noted; official 3ds.com surfaces)

- GEOVIA's own category label: **"mine production management and reconciliation"** — "GEOVIA InSite™ collates progress of production activities against the plan. Advanced reconciliation tools allow mining operations to address and understand the cause of variance." (About GEOVIA datasheet)
- Press release (InSite 4.2): "mine production management application that records and evaluates data for service, support and production activities from the mine through to saleable product"; "improved material balance and stockpile management to streamline reconciliation and end-of-month processes."
- Services case study: "implemented the InSite mine production management solution… centralize data storage and site analysis… compare actual, planned and forecasted data."
- Blog "6 Steps": "provides up-to-date information for improved visibility into production activities, enabling in-shift control and support of material reconciliation across the mining value chain… real-time data analytics to support decisions and enables conformance to plan"; "Delivering auditable transactions and master data management, InSite centralizes Operational Technologies."
- Blog "Bridging the gap": "core design, architecture, and intent is for 'bridging the gap' between mine planning KPIs and actual/event KPIs"; KPI = value + attributes (who/when/where); planned and actual KPIs configured for "apples to apples" comparisons at the lowest workable detail (by pit phase, material type, crew, fleet — where the plan's granularity allows); "Mine + Plant manufacturing production and management software"; dashboards "MTD Budget/Actual payload by day… or as a real-time display in a control room"; "month-end reconciliation report."
- Customer quote (Agnico-Eagle Kittilä): "Thanks to InSite, our stockpile balances can be accurately calculated and we have the ability to report on numbers we can rely on."
- Deployment shape (CIM Magazine on Chelopech): control room supervisor uses InSite shift management software; shift-by-shift schedule for seven days; SIC against targets checked "at short-term intervals throughout the working shift."

## Product D — Rockwell Automation Mining Operations Management (MOM)

### Key observations (evidence layer A unless noted)

- The vendor's own category definition: "a Mining Operations Management (MOM) solution connects disparate systems and aggregates data – and delivers a single version of truth by providing information in the same context across the mining operation… delivers fit-for-purpose applications designed for mining that interact, share and cooperate on the same platform."
- Problem framing (why the Type exists): "inherent measurement errors throughout the value chain… To mitigate these errors, the industry employs reconciliation and adjustment processes. These processes require solutions that not only facilitate such adjustments but also deliver clear documentation of both the original and modified values… transparency regarding who made the changes and when they were made."
- Data-substrate realities the product must handle: network/power outages with locally buffered data; many source systems (historians, control systems, LIMS) with timestamp correlation ("LIMS data may only become available a day or more after the sample was taken… it still needs to be accurately correlated with the truck, train, flowmeter, or belt-weight"); source-data changes ("Fleet Management Systems are notorious for this… changing the load and unload locations, resulting in different stockpile balances and weighted grades"); manual entry ("some data… must be manually entered by operators… field staff during operator rounds on mobile devices").
- MOM attributes: integration; **genealogy** ("relating downstream material movements to upstream sources — from ship to mine"); single data model ("data changes are reflected across all models and calculations simultaneously").
- Mining-dedicated modules: **OEE/Asset Utilization KPIs**; **Downtime/Loss Accounting** ("business impact of planned and unplanned stoppages… rate losses"); **Short Interval Control** ("alerts operators when the circuit is not functioning as required… meaningful changes within a shift"); **Production Reporting** ("actual feedstock blends, throughputs, consumption of reagents… in the context of where they are consumed, produced, recovered or recirculated"); **Metal Reporting** ("aligns sample results with material movements to calculate the constituent quantities of the various elements within the overall ore flow. Recoveries and losses can be calculated separately for each mineral"); **SPC**; **Inventory Management and Storage Balances** ("net balance in stockpiles, stockpile partitions, silos, tanks… based on metered additions, depletions, and survey adjustments. Tracks the grade from source to destination, allowing predictions of load out grade based on source stockpile ratios before the lab results are available. Materials and grades can be tracked by either physical or virtual models").
- "single source of truth for operational and enterprise decision-making"; ERP connectivity "for production reporting"; responsive web + mobile ("self-service facilities for mobile field operators, field technicians").

## Product E — Micromine Pitram (boundary case; FMS core evidenced in the mining-fleet pass)

### Key observations (evidence layer A)

- Pitram is the mining-fleet-management Type's product ("Fleet management and mine control") — its FMS core (equipment, assignments, load-grain production) is documented in research/mining-fleet-management.md.
- This pass adds its **reconciliation functionality** (official blog, 2026-01): "segregating the material flow into logical stages called **envelopes**… An envelope represents a stage in material transportation – underground stockpiles form one envelope, surface stockpiles another, crusher and bunkers another. Material movements are tracked between envelopes, with tonnage and grades calculated at each stage."
- Reconciliation mechanics: "the reconciliation process works backward through the envelopes. The system compares recorded inflow and outflow for each stage against the mill report. If discrepancies exist, they can be identified down to individual material movements, not just bulk totals."
- Claimed-vs-actual balancing: "The system displays claimed tonnage for each envelope and allows comparison against mill-reported actuals. Discrepancies can be distributed proportionally across all source locations, or geologists can manually allocate them… Locations can be locked if their measurements are known to be accurate… The discrepancy is then allocated to other locations where measurement uncertainty is higher… while maintaining mathematical balance."
- Grades: "Mill assay results provide actual grades for delivered material. The system works backward through envelopes, adjusting grades while maintaining proper mass balance."
- Output: "reconciled tonnes, reconciled grades, reconciled metal content that can be reported alongside original measurements."
- Data integrity rule: "never modifies original movement data. All actual movements recorded in the system remain unchanged, providing a permanent audit trail."
- Stakes framing: "Revenue recognition becomes uncertain… Inventory valuation becomes problematic… Operational decisions suffer… Trust erodes between departments."
- Material Management module (from the mining-fleet pass): ore/waste/development classification at point of loading; "complete chain of custody spanning heading, stockpile and processing plant"; "Align production data with geological expectations in real time" (reconciliation).

## Cross-product Comparison

| Structure | Datamine Production Solutions | Maptek MRT | GEOVIA InSite | Rockwell MOM | Pitram (boundary) | Strength |
|---|---|---|---|---|---|---|
| Attributed production record (actual movements: tonnes, grades, source, destination, time) | "material movements… captured, validated and shared through governed workflows"; Reconcilor movement tracking "every tonne, every shift" | "Measuring and validating actual material movements near-live at every stage" | "records and evaluates data for… production activities from the mine through to saleable product" | Production Reporting "in the context of where they are consumed, produced, recovered or recirculated" | movements tracked between envelopes | B (all five) |
| Aggregation from execution systems + manual entry | integrates "fleet management systems, and plant control systems"; SQL/APIs/Excel/CSV | "Connects resource model, mine plans, fleet management, on-belt analysers, survey and laboratory results"; "Connects SCADA historian, planning and laboratory information systems" | "centralizes Operational Technologies"; reads "spreadsheets, databases, and existing systems" | historians, control systems, LIMS, FMS + "manually entered by operators" | integrates autonomous fleets, weighbridges, conveyors (FMS pass) | B (all five) |
| Material/metal balance with stocks as managed state | "Stocks management"; "stockpile and inventory management"; MineMarket inventory | StockpileMRT "quality and quantity of discrete stockpiles"; "inventory and qualities through the mining, blending and processing stages" | "material balance and stockpile management"; "stockpile balances can be accurately calculated" | "net balance in stockpiles… based on metered additions, depletions, and survey adjustments" | envelopes hold stockpile stages; chain of custody heading→stockpile→plant | B (all five) |
| Genealogy source→destination | "where material originated, how it moved through the operation" | material tracked "from in situ rock to ROM stockpiles and plant feed" | KPI attributes who/when/where | "relating downstream material movements to upstream sources — from ship to mine" | chain of custody; backward tracing through envelopes | B (all five) |
| Reconciliation vs plan AND resource model | "comparing estimated, planned, mined, processed and reported values"; "Geological model reconciliation" | "reconcile production performance with the strategic mine plan and resource model" | "collates progress of production activities against the plan"; planned-vs-actual KPIs; "cause of variance" | reconciliation/adjustment processes with documented changes (resource-model reference implicit in mining modules) | "Align production data with geological expectations"; claimed vs mill actuals | B (all five; resource-model reference explicit in Datamine/Maptek/Pitram) |
| Reconciled measures + variance analysis | "pinpoint and reduce dilution, ore loss"; variances investigated | "real time reconciliation of inventory and qualities" | "address and understand the cause of variance" | downtime/loss accounting; recoveries and losses per mineral | "reconciled tonnes, reconciled grades, reconciled metal content" alongside originals | B (all five) |
| Production reporting (daily/weekly/monthly, corporate) | "daily, weekly, and monthly production reports"; "standardised… corporate reporting" | live dashboards; case-study compliance reporting | "month-end reconciliation report"; "report on numbers we can rely on" | Production Reporting module; ERP connectivity | shift dashboards; month-end closings (FMS pass) | B (all five) |
| Audit trail / data governance | "validation, traceability, auditability and approval workflows"; JORC framing | "single source of truth for material movement reconciliation" | "auditable transactions and master data management" | "clear documentation of both the original and modified values… who made the changes and when" | "never modifies original movement data… permanent audit trail" | B (all five) |
| Shift execution / SIC | Centric Ops "shift planning, activity metrics… handover"; SIC tools | not centered (near-live tracking instead) | "in-shift control"; shift management software (Chelopech) | SIC module | Shift Planner + SIC (FMS pass) | B common — NOT definitional (Reconcilor/MRT lack it) |
| Equipment/downtime machinery | Centric "equipment status… utilisation and downtime reporting" | not centered | not evidenced in fetched pages | OEE, Downtime/Loss Accounting modules | Time Usage Model (FMS pass) | B common — NOT definitional |
| Metal accounting (recovery, constituents) | Production Accounting; AMIRA P754 alignment | qualities through processing | "from the mine through to saleable product" | Metal Reporting module | reconciled metal content | B common — metals-form; coal/bulk balance tonnes/quality |
| Plan consumption (schedule/targets as reference) | "connecting operational plans with actual production data" | "compliance to plan" | planned KPIs from planning | SIC thresholds; plan context | shift plans (FMS pass) | B (all five) |
| Multi-site / corporate roll-up | "consolidates data from multiple mines" | multi-site case studies | enterprise deployments | enterprise decision-making | multi-roster (FMS pass) | B common |
| Resource-model construction | NO — consumes models | NO — connects to model | NO | NO | NO | — (consumption seam, all five) |

## Canonical Model (abstraction ladder)

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures over one binding. The Type is recognizable only when all three are present:

1. **The mine's attributed production record.** What was actually mined, moved, and processed, held as attributed movement records — tonnes, grades/material identity, source, destination, time — captured at operational grain (shift/day) and aggregated from the mine's execution systems (fleet management/dispatch, plant control/historians, laboratories, surveys) and manual entry. Remove → planning territory (a plan with no actuals) or raw telemetry/dispatch reports with no governed record.
2. **The material/metal balance across the mine's value chain.** The flow from resource (in-ground) through mining, stockpiles, and processing to product, held as a balanced ledger: stocks (stockpiles, bins, tanks) as managed state carrying quantity and quality, updated by metered additions/depletions and survey adjustments, with genealogy linking downstream movements to upstream sources. Remove → KPI dashboards and disconnected reports; inventory valuation and blending lose their basis.
3. **Reconciliation against plan and resource model.** The systematic comparison of estimated/planned vs mined/processed/reported values (tonnes, grades, metal), producing variances and reconciled measures — with adjustments documented against preserved originals — that feed back into model confidence, plan compliance, and the numbers the mine reports. Remove → production logging or fleet management with no standard of judgment; the "management" in the Type's name loses its object.

Jointly-held is load-bearing:

- 1 alone = production logging / dispatch reporting
- 2 without 1+3 = a stockpile spreadsheet
- 3 without 1+2 = reconciliation over imported numbers with no record behind them (the spreadsheet era the products market against)
- 1+2 without 3 = material tracking with no standard of judgment (no plan/model comparison)
- 1+3 without 2 = variance reports that never reconcile to stocks
- 2+3 without 1 = accounting over aggregates nobody can trace to movements

**Binding**: the mine's own extraction-to-product chain (orebody → mine → plant → product), with the geological resource model as the reference estimate the actuals are reconciled against. Remove the binding → generic production accounting / manufacturing MES (Honeywell PAR, Aspen AORA are the cross-industry forms of the same machinery). The resource-model reference is the mining signature: manufacturing MES compares plan vs actual, but nothing in manufacturing reconciles against a geological estimate of what is in the ground.

### L1 — Common Mature Structure (standard in modern products, not definitional)

- shift execution / short interval control (shift plans, targets, handover, in-shift deviation alerts) — present in Centric Ops, InSite, Rockwell SIC, Pitram; absent from Reconcilor/MRT centers
- equipment utilisation / downtime and loss accounting (OEE-class KPIs)
- metal accounting for processing (recoveries, constituent quantities; AMIRA P754-class alignment) — the metals form; coal/bulk operations balance tonnes and quality
- grade control / ore control support (material classification, dilution reduction)
- blending support (ROM/reclaim/blend profiles to hit plant feed targets)
- data-validation and approval workflows; governed "single source of truth"
- source-data change propagation (reprocessing dependent results when FMS/LIMS correct source records)
- timestamp correlation across heterogeneous sources (lab assays correlated with truck/belt/flowmeter data)
- multi-site consolidation and corporate reporting
- ERP connectivity (production reporting into finance); mobile field capture (operator rounds, offline tolerance)
- compliance/audit framing (JORC-class code expectations; audit-ready outputs)

### L2 — Variant / Optional Structure

- commodity form: metals (metal accounting, recovery) vs coal/bulk (tonnes/quality, placement compliance) vs industrial minerals
- scope pole: reconciliation specialist (Reconcilor) vs tracking suite (MRT) vs integrated operations platform (Centric, InSite, MOM suite) vs FMS-embedded modules (Pitram Material Management/reconciliation)
- value-chain span: mine-only vs mine-to-mill vs mine-to-port (logistics/commercial bundles at Datamine's outer poles)
- environment: open pit vs underground (movement shapes, envelopes)
- cadence emphasis: near-live tracking vs monthly reconciliation ritual (both current; not era markers)
- deployment: on-premises dominant today (Reconcilor's own FAQ), cloud-ready emerging
- physical vs virtual stock models (Rockwell)
- ML/AI companions (Maptek MAXTA/PETRA) — add-on

### L3 — Vendor-specific (kept out of the final document)

Datamine: bundle names (Mining Operations/Processing/Logistics/Commercial/Shift & Equipment), Centric Enterprise/Ops/Analytics/Mobile split, MineMarket, MPX, Commit Works acquisition, AMIRA P754 and JORC marketing framings, ~12-week implementation claim. Maptek: MaterialMRT/StockpileMRT/PlantMRT names, PETRA MAXTA, Vestrex/MDS/MCF/MOE platform names, MineSuite MES heritage. Dassault: InSite KPI-configuration doctrine, "6 Steps" framing, Chelopech/Kittilä quotes. Rockwell: module names (OEE, Downtime/Loss Accounting, SPC, Metal Reporting, Inventory Management and Storage Balances), FactoryTalk lineage, "companies use less than 1% of available data" claim. Pitram: envelopes terminology, PRIS, Pitram Vision. All vendor outcome claims and module names stay here.

## Anti-overfitting Notes

- **Real-time is NOT definitional.** The classic cadence is the monthly reconciliation meeting (Pitram blog: "a familiar ritual"); Reconcilor ships daily/weekly/monthly reports; MRT and Rockwell emphasize near-live. Both cadences are current product forms; the invariant is the comparison discipline, not its tempo.
- **Shift execution/SIC is NOT definitional.** Reconcilor and MRT — the two clearest reconciliation products — do not center it. It is the execution leg that products closer to the FMS seam carry.
- **Metal accounting is NOT definitional.** It is the metals form of the balance; coal/bulk operations balance tonnes and quality without metal.
- **The geological model is consumed, not constructed.** No sampled product builds the resource model; all connect to it as the reconciliation reference (same consumption seam the mine-planning pass ratified for planning).
- **Specific integration substrates are NOT definitional.** FMS, SCADA historians, LIMS, surveys are the common sources, but manual entry is first-class in every account (Rockwell: operator rounds; Pitram: radio-era logging in the FMS pass).
- **Cloud/SaaS is NOT definitional.** Reconcilor is on-premises today per its own FAQ.
- **AI/ML is NOT definitional.** Present as add-ons (MAXTA) or era-current marketing; the core runs without it.
- **JORC/regulatory framing is NOT definitional.** It is a jurisdiction-dependent driver (Datamine's marketing angle); the audit-trail structure is general.

## Historical / Market-Sample Check (§24 workflow)

- Paper era: daily shift reports and tonnage/grade tally sheets (production record), stockpile survey books and hand-tallied stocks (balance), monthly reconciliation statements comparing survey/assay/mill figures against plan and reserve estimates (reconciliation) — all three legs present with no software. Passes.
- The reconciliation discipline itself predates software: industry literature describes mine reconciliation as a long-standing practice with "no agreed industry standard" (OneMine 2024 paper); the metal-accounting code of practice (AMIRA P754) codified existing practice in the early 2000s. The products themselves market against the spreadsheet era ("reducing manual spreadsheets" — Reconcilor; "Spreadsheet-based reconciliation compounds these problems" — Pitram blog), direct evidence the core predates the current product generation.
- The Maptek lineage shows vocabulary migration (MineSuite "MES" 2008 → Resource Tracking "material tracking & reconciliation" today) without structural change — the seat is old; the label is fashion.
- Conclusion: L0 survives the historical check; real-time, SIC, cloud, AI, and regulatory codes are era machinery.

## Vendor-specific Findings (L3, not for the final document)

See L3 list above. None promoted to the canonical document.

## Rejected Findings

- "Mining Operations Management = Mining Fleet Management at larger scope" — rejected: the FMS's center is the live assignment loop over mobile machines; the MOM center is the whole-chain production record + balance + reconciliation. The FMS appears in MOM accounts as a *data source* (Reconcilor integrates FMS; Rockwell: "Fleet Management Systems are notorious for this"). Keep-both.
- "Cost management is definitional" — rejected: cost/financial management is ERP territory; the production record feeds it (ERP connectivity "for production reporting"; inventory valuation consequences). Downtime/loss accounting (business impact of stoppages) is the closest in-type money machinery — held common-mature.
- "Safety/environmental compliance is definitional" — rejected: appears as modules (Centric Mining Systems' original suite listed "health and safety, environmental metrics"); EHS is a separate §21 Type.
- "Weighbridge ticketing is part of the core" — rejected: scale/weighbridge data appears as an input among others; the ticketed-sale loop is the quarry-management Type's center (see Boundary Findings).
- "Voxis/Vizari as a reconciliation vendor" — rejected: memory artifact; VOXI is Geosoft geophysical inversion, unrelated.

## Boundary Findings

| Type | Relationship | Distinction / removal test |
|---|---|---|
| Mine Planning Application (§20, processed) | upstream, plan-of-record | Planning authors the future plan (design, reserves, schedule); this Type holds the actuals and reconciles them against that plan and the resource model. The reconciliation is the handoff — in both directions (plan compliance monitored; "use actual performance data to improve future plans" — Datamine). **Discharges the mine-planning pass's seam note: CONFIRMED.** Deswik.OPS (short-term planning + shift execution, "managing compliance to plan") remains a boundary case sitting ON the seam — its center is the plan/shift-execution loop, not the balance/reconciliation record; left as documented boundary case, no directory change. |
| Mining Fleet Management (§20, processed) | downstream data source + sibling execution Type | FMS = live assignment loop + machine/load-grain production record for mobile equipment; this Type = whole-chain production record + material balance + reconciliation. FMS output is a primary input ("Dispatch" listed as a Reconcilor source; Rockwell's FMS-change propagation problem). **Discharges the mining-fleet pass's forward flag: hypothesis CONFIRMED — broader whole-mine sibling; keep-both RATIFIED.** Pitram straddles: FMS core with Material Management/reconciliation modules reaching into this Type — evidence that the seam is real and that vendors bundle across it. |
| Quarry Management (§20, processed) | §20 sibling, different revenue object | Quarry = product-sales loop (produce → stockpile → sell → weighbridge ticket → invoice) over aggregate commodities; this Type = extraction-production chain reconciled against the geological model. None of the sampled mining-ops products centers customer sales/invoicing (Datamine's commercial leg is a separate bundle). Weighbridge/scale machinery is shared-family bulk-materials capability appearing as an input, not the center. **Discharges the quarry pass's seam question: seam CONFIRMED at stronger-than-center-of-gravity strength; weighbridge-ticket machinery held shared-family, not definitional; keep-both.** |
| Manufacturing Execution System / MES (§16) | cross-industry analog | MES executes and records factory production; this Type is the mining analog (Rockwell's MOM is explicitly built on manufacturing-operations concepts; GEOVIA calls InSite "Mine + Plant manufacturing production and management software"; Maptek's heritage product was literally labeled MES). The mining signature: reconciliation against the geological resource model (MRMR-class governance), orebody-to-metal chain, measurement-uncertainty machinery (surveys, moisture, dilution, locked locations). Remove the resource-model reference and geological chain → MES/production accounting. |
| Production accounting engines (Honeywell PAR, AspenTech AORA) | adjacent capability pole | Cross-industry material/energy balance and statistical reconciliation — the same balancing machinery without the mining chain or resource-model reference. Related capability, not this Type's center. |
| SCADA / Industrial Historian (§16) | data substrate | Control systems run the plant and hold the historian; this Type consumes their data (PlantMRT "Connects SCADA historian"; Rockwell's timestamp-correlation problem). Substrate vs management application. |
| ERP (§08/§10) | finance consumer | ERP holds finance; the production record feeds it ("modern connectivity with ERP systems for production reporting" — Rockwell). Money management is out of type; the operational record is the in-type object. |
| Geological Modeling Platform (§20, processed) | upstream, model-of-record | The resource model is constructed there and consumed here as the reconciliation reference (same consumption seam ratified by the mine-planning pass). |
| EHS / Environmental (§21) | module adjacency | Safety/environmental metrics appear as modules in some suites; a separate Type with its own object world. |
| EHS-adjacent compliance reporting | consequence | The reconciliation record serves public/code reporting (JORC-class) — a consequence of the audit-grade record, not a separate structure. |

"Remove what → becomes another Type" judgments: remove the production record → mine planning (plan with no actuals) or telemetry; remove the balance → dashboards/reports; remove reconciliation → fleet management or production logging; remove the mine binding (resource-model reference, orebody-to-product chain) → manufacturing MES / generic production accounting.

## Uncertainties

- **Hexagon HxGN MineOperate OP Pro / MineEnterprise unreachable** (403/transport, consistent with two prior passes). Major market anchor; module structure NOT independently verified. No operational claims drawn from it.
- **GEOVIA InSite product page 404** — InSite evidence rests on official datasheets, press release, and blogs; current packaging (post-2012) not independently verified beyond those surfaces.
- **No Tier-1 help-center documentation reached** for any sampled vendor; all claims are feature-level from official product pages/FAQs/blogs. Precise numeric limits, cadences beyond those quoted, and defaults are deliberately not claimed.
- **Cost-management depth** (whether any sampled product holds cost-per-tonne as a first-class object) — not evidenced; held out of type.
- **Underground-coal / bulk placement compliance** evidenced at one site (Meandu case study) — held as variant, not generalized.
- **Whether Deswik.OPS-class products should eventually sit under this Type or Mine Planning** — left as documented boundary case (both passes agree it sits ON the seam).
- **Regional market breadth** (Chinese/Russian/CIS mining-ops products, e.g. K-MINE) — only lightly reached; no structural claims drawn.

## Final Synthesis

Mining Operations Management is the mine's production system of record: it holds what the operation actually mined, moved, and processed as attributed movement records; maintains the material/metal balance across the mine's value chain (stocks as managed state, genealogy from source to destination); and reconciles those actuals against the mine plan and the geological resource model, producing variances, reconciled measures, and the audit-grade numbers the mine reports upward. Its defining core is the jointly-held triple (production record + material balance + plan/model reconciliation) bound to the mine's own extraction-to-product chain — the resource-model reference being the mining signature that separates it from manufacturing MES and generic production accounting. Around that core, mature products add shift execution/SIC, equipment/downtime accounting, metal accounting, blending support, governed data workflows with preserved originals, multi-site corporate reporting, and ERP connectivity. The Type sits between Mine Planning (whose plan it reconciles against) and Mining Fleet Management (whose dispatch records it consumes), ends where the product-sales loop begins (Quarry Management), and crosses into manufacturing only when the geological reference is removed.
