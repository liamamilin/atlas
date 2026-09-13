# Research Notes — Power Plant Management

Research date: 2026-09-09
Slug: power-plant-management (DIRECTORY §19 Energy, Utilities & Telecommunications)

## Research Goal

Understand what "Power Plant Management" is as an Application Type: what the market actually sells under generation/plant-management vocabulary, what the plant-side management layer contains, who operates it, how the production–availability–accounting loop works, and how it separates from the grid control-room family (EMS/SCADA/ADMS), the maintenance family (CMMS/EAM/APM), the commercial family (energy trading / scheduling & settlement), and the renewable asset-management family.

## Initial Boundary

- The leaf sits at the head of §19, before the renewable asset-management leaves (Renewable/Solar/Wind/BESS — unprocessed) and the grid-operations family (EMS, ADMS, OMS, DERMS — processed).
- Pre-hung flags from processed sibling passes:
  - **grid-operations-platform pass**: "Power Plant Management / Generation Management = plant-level member family — manages generation assets/fleets (operation, maintenance, market participation); the umbrella's family operates the network those plants serve. Vendor product splits (EMS vs GMS) mark the seam." Also explicitly rejected "Grid Operations Platform = Power Plant Management".
  - **EMS pass**: "AspenTech explicitly splits 'Energy Management System' and 'Generation Management System' as separate products on one platform (EMS = grid transport; GMS = plant fleet management incl. market participation) — useful boundary evidence that grid-level EMS ≠ plant-level generation management."
- Known naming hazards recorded upfront:
  (a) marine/industrial "power management" = gen-set paralleling control hardware (DEIF-class);
  (b) "Power Management System" = the site/microgrid energy-orchestration pole (flagged by the EMS pass — one control-room vendor deliberately sells that seat as a "Power Management System");
  (c) "power plant management" also names an O&M outsourcing **service** (staffing/operating plants on the owner's behalf) — not software;
  (d) the plant software **estate** as a whole (control + data + maintenance + performance + commercial) is sometimes framed as "power plant software" without a single management product.
- Working hypothesis at intake: the leaf is the generation-side **management layer** (GMS-class), not an umbrella and not control. The research must either confirm a distinct structure or resolve the leaf as an umbrella/alias.

## Research Questions

1. What do products sold as generation management / power plant management actually contain?
2. Is there a distinct management-layer structure, or is the leaf an umbrella over control + data + maintenance + commercial component Types?
3. What is the core operational loop (plan → operate → record → keep available → account/report)?
4. Which functions are defining vs common vs optional (AGC/dispatch, forecasting, outage management, performance/heat-rate, market participation, accounting/compliance)?
5. Where are the seams vs EMS, SCADA/DCS, CMMS/EAM, APM, energy trading, energy scheduling & settlement, DERMS/VPP, and the renewable asset-management leaves?
6. Does the definition survive the historical check (paper-era plants, regulated-era utilities, regional MIS products)?

## Representative Products

Selection rationale: market representativeness + reachable official documentation + different product philosophies (dispatch/commercial-centric vs asset/performance-centric) + different customer levels (utility fleet operators, IPPs, market aggregators vs renewable portfolio operators) + boundary probes for the name-collision poles.

| Product | Vendor | Pole | Customer level | Doc access |
|---|---|---|---|---|
| AspenTech OSI Generation Management System (GMS) | AspenTech | fleet generation dispatch/commercial management (operations-centric) | generation operators, IPPs, market aggregators; "750 GW of traditional and renewable generation" | good (product page + webinar page with named feature inventory) |
| Unity suite (APM + Asset Oversight + FSM + SCADA/PPC/EMS) | Power Factors | renewable asset/performance management (asset-centric) | renewable IPPs/operators, 600+ customers, site-to-fleet | excellent (homepage + deep APM page) |
| GE Vernova power-generation software estate | GE Vernova | estate framing + plant performance/reliability vocabulary (no single management product) | power generators globally | good (industry page + FAQs) |
| PPM 300 | DEIF | marine/industrial "power management" control hardware (boundary probe) | marine/offshore, genset OEMs | good (product page) |
| HyCon / OnCare.Health / HyService | Voith | hydro OEM estate: control + condition monitoring + services (boundary probe) | hydro plant owners | good (hydropower page) |

Not sampled after access failure (network-restricted rule, 1–2 attempts then abandon): Siemens Energy (404 on guessed plant-solutions URLs), Mitsubishi Power (403), Hitachi Energy (unreachable across three prior sibling passes), ANDRITZ (navigation-only page). DuckDuckGo search timed out twice — search engines unusable this pass. Wärtsilä Energy page fetched for estate context only. All limitations recorded; no memory-filled precision.

## Sources

All fetched 2026-09-09:

- AspenTech — OSI Generation Management System product page: https://www.aspentech.com/en/products/dgm/aspentech-osi-generation-management-system
- AspenTech — GMS webinar registration page ("Unlocking Generation Efficiency with AspenTech OSI Generation Management System"): https://www.aspentech.com/en/resources/live-events-and-webinars/dgm-unlocking-generation-efficiency-with-aspentech-osi-gms
- Power Factors — homepage: https://powerfactors.com/
- Power Factors — Unity Asset Performance Management page: https://www.powerfactors.com/unity/asset-performance-management
- GE Vernova — Power Generation software industry page: https://www.gevernova.com/software/industry/power-generation
- GE Vernova — Software & Services products page: https://www.gevernova.com/software/products/
- DEIF — PPM 300 product page: https://www.deif.com/products/ppm-300
- Voith — Hydropower solutions page: https://www.voith.com/corp-en/industry-solutions/hydropower.html
- Wärtsilä — Energy page (estate context): https://www.wartsila.com/energy

Sibling-pass sources reused as corroboration (not re-fetched): AspenTech Digital Grid Management suite page (grid-operations-platform pass), EMS/ADMS/DERMS/DR/trading/scheduling/forecasting research notes.

Evidence layers used below: A = directly observed on an official source this pass; B = cross-product commonality across the sampled set; C = canonical inference from comparison + boundary reasoning.

## Product Observations

### Product A — AspenTech OSI Generation Management System (GMS)

Key observations:

- Positioning (A): "Comprehensive solution suite for managing regulated and deregulated power generation assets including forecasting, optimization, scheduling, real-time operation, market participation, accounting and compliance."
- Headline promise (A): "Optimize Power Generation Resources to Meet Load Demand and Enable Economic Objectives with Market Participation."
- Scale claim (A): "Feature-rich solution with global install base managing over 750 GW of traditional and renewable generation."
- Audience (A): "generation operators, independent power producers and market aggregators"; brochure-landing blurb: "Generation utilities, independent power producers and energy market participants use AspenTech generation management applications to meet optimal system performance and regulatory compliance."
- Named feature inventory (A, webinar page): Automatic Generation Control (AGC); Economic and Transmission Constrained Dispatch; Reserve Calculations; Renewables Forecasting and Management; Energy Storage Resource Management including Co-located and Hybrid modeling; Generation Fleet / Resource Optimization; Advanced Transaction Scheduling; Accounting and Compliance Assessment.
- Webinar promise (A): "real-time generation control, accurate forecasting, optimized scheduling and planning, production efficiency, renewables integration and precise energy accounting."
- Family context (A): GMS is one named product in the Digital Grid Management suite beside monarch (SCADA platform), EMS, ADMS, DERMS, CHRONUS Historian, Cimphony Network Model Management, Microgrid Management System — the vendor's own plant-vs-grid product split.
- What the fetched pages do NOT claim: maintenance work management, outage planning, condition monitoring (AspenTech sells those in a separate Asset Performance Management suite) — pole asymmetry noted, not filled from memory.

### Product B — Power Factors Unity (renewable pole)

Key observations:

- Positioning (A): "Renewable Energy Management Software"; "Unity, powered by REMI: Renewable Energy Management Intelligence"; "Every megawatt optimized. Every decision backed by intelligence."; "Get more out of every asset, from site level to fleet level."
- Suite decomposition (A): three layers — Monitoring & Control (SCADA, **Power Plant Controller (PPC)**, EMS); Technical Asset Management (Asset Performance Management, Advanced Insights, Field Service Management); Commercial Asset Management (Asset Oversight, Invoice Management). Control products are separate suite members — the management layer consumes them.
- APM functional depth (A):
  - Portfolio performance: "single source of truth for solar, wind, and storage data"; "unified portfolio view of energy yield, losses, and trends. From the fleet level down to individual inverters or turbines"; multi-asset benchmarking; "Compare baselines across multiple stakeholders and contracts to compare actual vs expected production."
  - Data integrity: "Always-ready system-of-record data set for downstream analytics like KPIs and reporting"; validation/correction, backfill after outages, anomaly detection, "Transparent audit trails linking KPIs to raw sensor data."
  - Event & loss management: "Automated classification of downtime, curtailment, and underperformance"; "Loss walks and analysis to trace financial and energy impact"; root-cause timelines.
  - Performance models: "Configurable performance models: Apply OEM specific assumptions and resource-adjusted baselines to validate expected vs. actual output."
  - Predictive maintenance: condition-based maintenance scheduling driven by asset health; OEM-tailored failure models.
  - Reporting: "Investor and compliance-ready outputs (ex: NERC GADS)"; widget-based reporting for asset management/O&M/executive views.
- Integration edges (A): SCADA & controls ingestion ("Ingest real-time signals from any SCADA or control system"); OEM-agnostic compatibility; **Market Interfaces** ("Integrate with existing market platforms for dispatch, bidding, and compliance"); **CMMS** ("Bridge insights to execution by integrating with any work management system. For Unity FSM users, APM events automatically connect to work orders to optimize maintenance schedules and close the loop from insights to action"); Commercial/Enterprise Asset Management ("directly link asset health with financial outcomes").
- Scale/customer claims (A): 600+ global customers; REMI "trained on operational data from more than 310 GW of renewable energy assets"; customers are renewable IPPs/operators (Repsol, Engie, EDF Renewables, BP, ACEN Australia, Origis, European Energy, METLEN…).
- What the fetched pages do NOT claim: real-time dispatch/AGC inside APM (that lives in the suite's separate SCADA/PPC/EMS products) — pole asymmetry noted.

### Product C — GE Vernova power-generation software estate (market-structure evidence)

Key observations:

- No single "power plant management" product exists in the portfolio (A): flagship lines are Asset Performance Management (Meridium/SmartSignal), GridOS, HMI/SCADA (CIMPLICITY/iFIX), MES (Plant Applications), Proficy, CERius emissions.
- Estate FAQ (A): "Which software is used in power plants?" answers with a decomposition, not one product: (1) "Computerized Maintenance Management Systems (CMMS) and enterprise management (EAM). These are used to modernize work orders, scheduling, tracking and purchase order management"; (2) "Simulation and analysis tools are commonly used for Grid commercial teams to handle unit commitment, economic dispatch and transmission reliability requirements"; (3) security software; (4) power engineering software; (5) "Asset Performance Management to avoid unplanned downtime and optimize maintenance strategies"; (6) "Asset Optimization software to reduce fuel and emissions"; (7) carbon emission management.
- Plant performance vocabulary (A): "Power plant performance monitoring is a critical practice to continuously track and evaluate the behavior of various parameters related to plant operation… comparing observed values with expected behavior based on models, digital twins, historical data, or correlations. Heat Balance Analysis and Data Analytics are used…"; "Data Reconciliation techniques detect and resolve inconsistencies"; "Predicted vs. Actual Performance… Predicted Performance can come from Advanced Pattern Recognition (APR) correlations"; "Fault Detection and Optimization helps identify faults, improve maintenance cycles and optimize processes."
- Performance parameters (A): "Power plant output; Power plant heat rate; Power plant auxiliary consumption…; Energy Performance Index (EPI); Compensated Performance Ratio (CPR) — typically used for renewable power plants…; Power Performance Index (PPI)…; Yield and Performance; Business Intelligence (BI) dashboard."
- Plant reliability (A): "For the power industry… plant reliability focuses on ensuring the power plants consistently generate electricity without unplanned outages and that the plant(s) are optimized to provide availability. Key aspects include equipment maintenance, performance monitoring, and outage management."
- Optimization scope (A): "optimization at the plant and fleet level for improved efficiency."

### Boundary probes

**DEIF PPM 300** (A): "Protection & power management PPM 300" — a **controller** product (controller rack + display unit) for marine/offshore gen-set paralleling, being replaced by the "iE 350 Marine… intelligent energy controller". Case studies: "Automated power management system increases safety aboard full-rigged ship", "Subsea IMR vessel blackout prevention", "Boost mode for heavy fishing". → The marine/industrial sense of "power (plant) management" is automatic gen-set control hardware (load sharing, synchronizing, protection, blackout prevention). Control territory, not a management application. Name-collision pole confirmed at official-product level.

**Voith hydropower** (A): portfolio = components (turbines, generators), automation systems (HyCon Control System — "Excellence in plant control"; HyCon Digital Turbine Governor; HyCon Thyricon Excitation), digital monitoring ("OnCare.Health Hydro — Monitoring, analysis and diagnosis"), and services (HyService maintenance). No management-layer product. → The hydro OEM estate = control + condition monitoring + services.

**Wärtsilä Energy** (A): engine power plants + energy storage + lifecycle services ("services for the whole lifecycle of our installations"; "Over 35% of our operating installed base is under service agreements"; 81 GW installed). No management product on the fetched page. → engine-plant OEM = equipment + services; the O&M-service sense of "plant management" is a service contract, not this software Type.

## Cross-product Comparison

| Dimension | AspenTech OSI GMS | Power Factors Unity | GE Vernova estate | DEIF / Voith probes |
|---|---|---|---|---|
| What the product is | generation fleet dispatch/commercial management suite | renewable asset/performance management suite | component portfolio (APM, SCADA, emissions…) — no single management product | control hardware / control+monitoring+services |
| Asset population | "traditional and renewable generation", 750 GW, incl. storage & hybrid | wind, solar, storage portfolios, site→fleet | power generators broadly | gen-sets / hydro units (equipment-level) |
| Production vs expectation | forecasting + optimized scheduling/planning + AGC/dispatch + fleet/resource optimization | expected vs actual output via configurable performance models; loss walks | "Predicted vs. Actual Performance"; heat balance; performance tests | absent (control only) |
| Availability | reserve calculations; real-time generation control (unit states implicit) | downtime/curtailment/underperformance classification; predictive maintenance; CMMS work-order loop | "equipment maintenance, performance monitoring, and outage management" | blackout prevention (control sense) |
| Accounting/compliance | "precise energy accounting"; "Accounting and Compliance Assessment"; advanced transaction scheduling | investor & compliance-ready reporting (NERC GADS); market interfaces for "dispatch, bidding, and compliance"; invoice management | emissions management; performance reporting | absent |
| Real-time control | inside the product (AGC, dispatch) | delegated to suite siblings (SCADA, PPC, EMS) | separate HMI/SCADA products | the whole product (control) |
| Maintenance execution | not claimed on fetched pages | FSM module + CMMS integration | CMMS/EAM named as the plant's work-order system | HyService (services) |
| Customer seat | generation operators, IPPs, market aggregators | renewable asset-management/O&M teams | plant reliability/performance teams | vessel/offshore crews; hydro owners |

### What is common (B) across the management-layer evidence

- A persistent, identified **asset population** (plants and their generating units) held as the system of record — GMS "managing… power generation assets"; Unity "system-of-record data set"; GE Vernova's estate presumes the plant's asset base.
- **Production held against expectation**: forecast/schedule/performance expectation vs actual, with the gap made visible and attributable (GMS forecasting+scheduling+optimization; Unity expected-vs-actual + loss classification; GE Vernova predicted-vs-actual + heat balance).
- **Availability as a managed record**: outages, derates and curtailment recorded and classified; maintenance coordinated against production (Unity explicit; GE Vernova "outage management" as a reliability key aspect; GMS structurally requires unit availability for dispatch/reserves — thinner direct wording, marked as such).
- **Production resolved into accounting and compliance**: energy accounting, settlement/invoicing where market-participating, regulatory/investor reporting (GMS "Accounting and Compliance Assessment"; Unity NERC-GADS-class outputs + invoice management; GE Vernova emissions management).
- Integration edges rather than containment: plant control systems (SCADA/PPC/DCS) and work-management systems (CMMS) are **neighboring systems** the management layer consumes or hands off to — both poles document the integration explicitly.

### What is product-specific (A-only) or vendor-packaging

- GMS module naming (AGC, Economic and Transmission Constrained Dispatch, Reserve Calculations, Advanced Transaction Scheduling); monarch/CHRONUS platform family; 750 GW claim.
- Unity/REMI branding; REMI training-data claim (310 GW); suite layer naming (Monitoring & Control / Technical AM / Commercial AM); NERC GADS as a named output.
- GE Vernova product names (SmartSignal, CERius, Proficy, Meridium); FAQ framings.
- DEIF PPM 300 / iE 350 naming; Voith HyCon/OnCare.Health/HyService naming; Wärtsilä service-agreement statistics.

## Abstraction Hierarchy

### L0 — Defining Invariant

Power Plant Management is the generation owner's management system of record for its power plants, defined by four jointly-held structures:

1. **The generation asset population as the unit of record** — persistent identified records for the owner's power plants and their generating units (traditional, renewable, storage, hybrid), carrying operational state, capability and history, at single-plant to fleet scope. Remove → a generic asset registry, or a trading book with no assets.
2. **Production managed against expectation** — what the assets should produce (production forecast for variable resources, dispatch schedule or bid award, performance expectation) is held against what they actually produce, with the gap classified and attributed. Remove → a monitoring dashboard or a production spreadsheet; no management.
3. **The availability record and its restoration** — each asset's available/derated/out state is held as the constraint on production; outage and curtailment events are recorded and classified (planned vs forced); maintenance is coordinated against production commitments (work-order execution itself remaining CMMS territory). Remove → production analytics with no availability discipline; generic CMMS territory.
4. **Production resolved into accounting and compliance** — generation, availability and events are accounted (energy accounting reconciling metered production with schedules/awards; settlement/invoicing where market-participating) and reported to the parties that rely on them (market/system operator, regulator, owner/investor). Remove → operations with no commercial/compliance closure.

Jointly-held is load-bearing: 1 alone = asset registry; 2 without 1 = production spreadsheet; 3 without 1+2 = generic CMMS; 4 without 1–3 = accounting shell; 1+2 without 3 = production statistics with no availability management; 1+3 without 2 = EAM with an availability ledger and no production loop; 1+2+3 without 4 = a SCADA+CMMS estate with no commercial closure; 2+3+4 without 1 = free-floating production/maintenance/accounting records.

### L1 — Common Mature Structure

- Forecasting of variable generation feeding the expectation side (GMS "Renewables Forecasting and Management"; the standalone Energy Forecasting Platform Type exists beside it).
- Dispatch/optimization depth where the pole includes it: AGC, economic and transmission-constrained dispatch, reserve management, fleet/resource optimization (GMS explicit; the renewable pole delegates control to suite siblings).
- Performance engineering: heat rate/heat-balance analysis, performance tests, data reconciliation, loss waterfalls, benchmarking (GE Vernova vocabulary; Unity loss walks).
- Loss/curtailment accounting as a first-class record class (Unity explicit).
- Maintenance integration: CMMS/work-order integration, condition-based maintenance triggers, field-service coordination (Unity explicit; GE Vernova estate).
- Market interfaces: bidding/dispatch/settlement connectivity (Unity "Market Interfaces"; GMS "Advanced Transaction Scheduling").
- Data-integrity machinery: validation, gap-filling/backfill, audit trails from KPI to raw sensor (Unity explicit).
- Compliance/regulatory reporting outputs (NERC GADS named at Unity; "Compliance Assessment" at GMS; emissions management in GE Vernova's estate).
- Storage and hybrid (co-located) resource modeling (GMS explicit; Unity BESS capacity claims).
- Mobile/remote access to fleet intelligence (Unity mobile app).

### L2 — Variant / Optional

- Asset population mix: thermal / hydro / nuclear / wind / solar / storage / hybrid — the structure is asset-class-neutral; renewable-only and traditional-only populations are both in-sample.
- Scope: single plant ↔ fleet/portfolio ("site level to fleet level"; "plant and fleet level").
- Pole emphasis: dispatch/commercial-centric (GMS) vs asset/performance-centric (Unity) — which leg is deep is a product philosophy, not the Type.
- Real-time control inclusion: supervisory dispatch + AGC inside the product vs delegated to plant SCADA/PPC/EMS products.
- Customer seat: utility generation division, IPP, market aggregator, O&M service provider (the service sense of "plant management" consumes this software class).
- Market context: regulated (report to utility/system operator) vs deregulated (market participation, settlement) — GMS explicitly claims both.
- Delivery: on-premises OT-adjacent vs cloud SaaS.
- Regional compliance machinery (e.g., NERC GADS-class availability reporting) — regional variant, not definitional.

### L3 — Vendor-specific (research notes only)

- AspenTech: monarch platform, CHRONUS historian, Cimphony model management, GMS module names, 750 GW claim, JPS case study.
- Power Factors: Unity/REMI branding, REMI 310 GW training claim, suite layer names, customer logo wall, Mubadala investment news.
- GE Vernova: SmartSignal/Meridium/CERius/Proficy naming, Forrester/Verdantix citations, Xcel Energy/RWE stories, FAQ statistics.
- DEIF: PPM 300/iE 350/DU 300 naming, marine case studies.
- Voith: HyCon/OnCare.Health/HyService naming, brochure library.
- Wärtsilä: 81 GW / 130+ storage / 35% service-agreement statistics.

## Vendor-specific Findings

Two vendor statements are structurally informative:

- **AspenTech's own product split** (EMS vs GMS on one platform) is first-hand vendor evidence that grid-level balancing and plant/fleet generation management are different products — the seam the EMS and grid-operations-platform passes predicted.
- **Power Factors' suite decomposition** (SCADA, PPC, EMS as separate products beside APM/FSM/CAM) is first-hand vendor evidence that real-time control is a neighboring layer the management layer consumes — control is not contained in the management Type.

## Rejected Findings

- "Power plant management = the plant control system (DCS/SCADA)" — rejected; control is the substrate the management layer supervises through. The DEIF and Voith probes show the *control* sense of "power management" is a different product class (controllers, governors, protection).
- "Power plant management = CMMS/EAM for power plants" — rejected; maintenance execution is one integration edge. The production and commercial legs are outside CMMS (Unity's own CMMS-integration framing: "bridge insights to execution").
- "Power plant management = energy trading for generators" — rejected; the trading Type's record is the commercial book (deals/positions/risk — per that pass's own-book definition); this Type's record is the asset population and its production. Asset-bidding sits at the seam (the trading pass itself held the automated asset-bidding pole at its edge).
- "Power plant management = EMS" — rejected on the vendor's own product split (AspenTech EMS = grid transport; GMS = generation assets).
- "Power plant management = renewable asset management only" — rejected; GMS explicitly manages "traditional and renewable generation"; asset population is a variant axis.
- "The leaf is an umbrella with no structure (grid-operations-platform pattern)" — rejected; unlike the control-room umbrella, a coherent management-layer product family exists (GMS-class, renewable-AM-class) with a shared four-leg structure. The estate framing (GE Vernova FAQ) describes the surrounding components, not the Type.
- "AGC/dispatch is definitional" — rejected; the asset/performance pole runs the same Type with control delegated to sibling products.
- "Market participation is definitional" — rejected; regulated-era plants accounted and reported production to the utility/system operator without markets. Accounting/reporting to relying parties is the invariant; market participation is its current dominant form.
- "Renewables forecasting is definitional" — rejected; it is the variable-resource leg of the expectation structure, inapplicable to dispatchable-only fleets.

## Boundary Findings

| Neighbor | Relationship | Distinction / removal test |
|---|---|---|
| Energy Management System / EMS (processed) | grid-side counterpart | EMS balances the NETWORK (supervision + network model + generation-to-load balancing at control centers); this Type manages the GENERATION ASSETS (production, availability, accounting). AspenTech's own EMS/GMS product split marks the seam. GMS's AGC serves the grid's balancing signal from the generator side. |
| SCADA / DCS (§16) | substrate | Point/process control executes setpoints; this Type plans, records, accounts and coordinates above it. Remove the management legs → control system; add them → this Type. Power Factors ships SCADA/PPC as separate suite products. |
| Industrial Historian (§16) | data component | Time-series memory beside the management layer; no production/availability/commercial semantics of its own. |
| CMMS / EAM (§16) | maintenance-execution neighbor | Work orders, schedules, parts. This Type holds production and availability and coordinates maintenance against them; work-order execution stays in the CMMS (Unity's integration framing is the vendor-drawn seam). |
| Reliability Management / APM (§16) | component/neighbor | Condition monitoring, predictive analytics, failure models feed the availability record; they do not hold production or commercial resolution. |
| Energy Trading Platform (processed) | commercial neighbor | Own-book deals/positions/risk vs asset operations. This Type's market interface serves the assets' production (transaction scheduling, dispatch compliance, energy accounting); the trading Type's record is the book. Consistent with that pass's asset-bidding edge note. |
| Energy Scheduling & Settlement (processed) | market-facing neighbor | Market submissions/settlement statements/reconciliation vs participant-asset-side production accounting. The two interlock at settlement data. |
| Energy Forecasting Platform (processed) | module vs standalone | Forecast production for energy quantities is a standalone Type; inside this Type it feeds the expectation side. |
| DERMS (processed) | resource layer, grid seat | DERMS coordinates DER behavior within distribution-grid constraints for the grid operator; this Type is the owner's seat over its own generation assets. |
| Virtual Power Plant Platform (unprocessed) | **flag** | Fleet-optimization overlap at the renewable/storage edge (GMS "Generation Fleet / Resource Optimization" + storage/hybrid modeling vs VPP's continuous multi-value optimization of aggregated DER fleets). Proposed discriminator: utility-scale owned generation fleets (this Type) vs aggregated distributed-resource portfolios (VPP); center-of-gravity per the derms pass's purpose discriminator. Joint review recommended. |
| Renewable / Solar / Wind / BESS Asset Management (unprocessed) | **flag** | Same management structure over renewable asset populations (Power Factors is the living overlap; GMS spans both). Likely asset-population variants of this Type; the renewable leaves may instead carry deeper portfolio/commercial machinery (Unity's commercial AM/invoice layer). Joint review recommended at those passes. |
| Utility Asset Management (unprocessed) | different asset class | Network assets (T&D plant) registry/maintenance vs generation production management; no production semantics there. |
| MES / Factory Operations Management (§16) | domain analog | The plant-as-factory pattern (production orders → execution → as-built record) recurs, but the objects differ: dispatch schedules and generating units vs production orders and lots. Domain seam, not a duplicate. |
| Marine/industrial "power management" (DEIF-class) | name collision | Automatic gen-set paralleling control hardware (load sharing, sync, protection, blackout prevention). Shares the words, not the seat — control territory. |
| "Power Management System" (site/microgrid EMS pole) | name collision | Per the EMS pass's flag: site/microgrid energy orchestration sold as "PMS" by one vendor. Site energy seat vs generation-asset seat. |
| O&M service providers (NAES/EthosEnergy-class) | service sense | "Power plant management" as an outsourced operating service; this Type is the software system of record such services run on. Not a software competitor. |
| Plant design/engineering tools (§16 CAD/CAE) | different lifecycle phase | Design/construction of the plant vs operation of the built plant. |

**Umbrella criterion check**: unlike grid-operations-platform, this leaf owns a structure of its own (the four-leg management layer) that survives every removal test — the estate's components (control, historian, CMMS, APM) are neighboring Types, not members absorbed into this one. The leaf is documented as a Type, with the estate decomposition recorded as family context.

## Historical / Market-Sample Check

- **Paper-era plant** (first half of the 20th century through the 1980s): shift logs and unit log books, outage and repair ledgers, heat-rate/performance test reports, generation reports to the utility or system operator, fuel/energy ledgers, maintenance schedules and overhaul plans — satisfies all four legs (asset records; production vs dispatch order and design performance; outage/maintenance records; accounting/reporting). No software machinery in the core.
- **Regulated-era utility plant MIS** (vertically integrated utilities, regional markets): plant information-management systems tracking generation, availability, maintenance and reporting to the utility — satisfies; market participation absent, accounting/reporting present.
- **Platform-native / OEM-bundled**: management modules bundled with plant control systems (DCS-vendor suites) — satisfies with bundling as variant.
- **Modern renewable IPP**: portfolio APM suites — satisfies with the renewable asset population.
- The phrase "power plant management" also names an O&M outsourcing service; the software Type is the system of record for that function — the service sense passes the check as a consumer of the Type, not a different structure.
- §24 verdict: the definition does not depend on cloud, AI, renewables, or any current-era machinery. The four legs are the plant's oldest management disciplines (produce to order, keep it available, account for it).

## Uncertainties

- Large thermal-OEM plant-management documentation unreachable (Siemens Energy 404, Mitsubishi Power 403, Hitachi Energy unreachable across three sibling passes, ANDRITZ nav-only): the thermal-plant pole rests on GE Vernova's estate/vocabulary pages plus AspenTech GMS. Assertions about OEM-bundled plant management are calibrated accordingly; no precise module inventories claimed for unreachable vendors.
- GMS's maintenance/availability depth is not directly documented on the fetched pages (inferred from dispatch/reserve logic); marked as the Type's softest joint leg at that pole. The availability leg is strong at the Power Factors and GE Vernova poles.
- No analyst category named exactly "power plant management" was found (search engines unreachable); the Type claim rests on vendor product families (GMS, Unity) and the sibling passes' recorded seams, not on a market-research category name. If a taxonomy pass finds such a category with a different definition, revisit.
- Nuclear outage/work-management depth (a distinctive plant-management discipline — refueling outages, work control, configuration management) was not directly sampled; recorded as uncertainty, not claimed.
- Whether the taxonomy should keep the renewable asset-management leaves separate or fold them as variants of this Type — flagged for joint review, not decided here.
- Hydro-specific water management (reservoir/dispatch optimization against water availability) is plausibly part of the expectation side for hydro fleets but was not directly evidenced in fetched pages (Voith pages are equipment/service-level); recorded as uncertainty.

## Final Synthesis

**Power Plant Management is the generation owner's operations-management system of record for its power plants** — at single-plant or fleet scope, over traditional, renewable, storage or hybrid asset populations. Its defining structure is four jointly-held legs: the generation asset population as the unit of record; production managed against expectation (forecast/schedule/performance expectation vs actual, gap attributed); the availability record and its restoration (outages/derates/curtailment recorded and classified, maintenance coordinated against production commitments); and production resolved into accounting and compliance (energy accounting, settlement/invoicing where market-participating, regulatory/grid/investor reporting). The Type sits above the control substrate (DCS/SCADA/PPC — neighboring Types), beside the data layer (historian) and the maintenance-execution layer (CMMS), and interfaces to the commercial layer (trading, scheduling & settlement) and regulators. The market realizes it in two poles — dispatch/commercial-centric (GMS-class) and asset/performance-centric (renewable-AM-class) — which differ in which leg is deep, not in the structure. Name-collision poles (marine/industrial gen-set "power management" control hardware; site/microgrid "Power Management System") are excluded by the seat test. The historical check passes: the paper-era plant's log books, outage ledgers, performance test reports and generation reports satisfy all four legs with no era machinery.
