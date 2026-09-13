# Research Notes — Resource Efficiency Management

Research date: 2026-09-09

## Research Goal

Understand what a "Resource Efficiency Management" application is as an Application Type: what its system of record is, who operates it, what the efficiency discipline consists of concretely, and where its boundaries run against the heavily adjacent §21 sustainability family (Energy & Carbon Management, Carbon Accounting, Sustainability/ESG Management, Waste types, Circular Economy) and against Building Energy Management (§17).

## Initial Boundary

Working hypothesis at start: the Type covers software through which an organization manages the consumption of its physical resources (energy, water, waste, materials) as the center, with the goal of using them more efficiently. Energy is one resource among several, not the center.

Nearest neighbors at start:

- **Energy & Carbon Management** (§21, processed 2026-09-08) — left an explicit flag for this leaf: extended resource data (water, waste) appears in ECM products as variants; "when wider resources become the managed center the boundary is that sibling Type — apply the resource-center test." This pass must discharge that flag.
- **Building Energy Management** (§17, processed 2026-09-06) — building-scoped operational energy; shared products observed (EnergyCAP, MRI Energy serve both §17 and §21).
- **Carbon Accounting Platform** (§21, processed) — all-scopes inventory of record as center.
- **Sustainability Management Platform / ESG Management Platform / ESG Reporting Platform** (§21, sustainability-management-platform and esg-management-platform still UNPROCESSED; esg-reporting processed) — naming-cluster flag exists for the ESG siblings; this Type must hold a seam against the ESG-program/disclosure center.
- **Waste Management Platform / Hazardous Waste / Recycling Operations / Waste Hauling** (§21; waste-management-platform still UNPROCESSED) — waste as operational stream vs waste as one resource flow.
- **Circular Economy Platform** (§21, processed) — material loops and multi-party circulation; its measurement pole vs this Type's own-estate efficiency loop.
- **Environmental Management System** (§21, UNPROCESSED) — ISO 14001-style management-system machinery.
- **Environmental Data Platform** (§21, UNPROCESSED) — generic environmental data infrastructure.
- **Telecom Expense Management / Spend Management** (§14/§10) — spend-only management of resource-like expense lines without a consumption-efficiency center.

## Research Questions

1. What is the unit of record? (What exactly is recorded, against what, at what cadence?)
2. What does "resource" mean concretely in these products — which classes, and is multi-class breadth load-bearing?
3. What is the efficiency loop? (Baseline/normalize → compare → act → verify? Which objects carry it?)
4. Where do cost/bills sit relative to consumption?
5. Where does carbon sit — definitional or derived?
6. How does the Type relate to the ESG/sustainability program center and the energy-data center? (the two boundary risks)
7. What regime machinery rides on top (ISO 14001/50001, building benchmarking, ordinances)?
8. Historical check: does the core hold without cloud, interval data, or AI?

## Representative Products

Selected for market representation, documentation reachability, and different product philosophies / customer tiers:

| Product | Pole | Customer tier | Evidence reached |
|---|---|---|---|
| Quentic — Environmental Management module | European EHS-suite resource-tracking module; ISO-driven industrial | Mid-market/enterprise industry | Tier-2 module page (deep) |
| IBM Envizi | Enterprise ESG data-management suite with resource data operations | Global enterprise | Tier-2 product page (rich) |
| Measurabl | Real-estate sustainability data platform (energy/water/carbon; portfolio grain) | Real estate owners/operators/investors | Tier-2 root + Optimize product pages |
| Arcadia | Energy/utility-data platform — boundary specimen (energy center; waste/telecom as separate expense products) | Enterprise | Tier-2 root page |
| Intelex — Sustainability Management | EHS-suite sustainability program module — boundary specimen (ESG program center; water/waste as separate applications) | Enterprise/regulated industry | Tier-2 product page |

Deliberately probed but unreachable (see Source-access Limitation):

- **Schneider Electric Resource Advisor** — the market's literal anchor product name for this category ("energy and sustainability resource management"); 403 in the ECM pass (×2) and again this pass (×2 paths). Its structure is NOT asserted anywhere in this research.
- **ENERGY STAR Portfolio Manager** (free government-native building tool for energy/water/waste) — transport errors ×2. Its specifics are NOT asserted.

## Sources

All fetched 2026-09-09:

- Quentic — https://www.quentic.com/ and https://www.quentic.com/software/environmental-management/ (Tier-2; module page deep)
- IBM Envizi — https://www.ibm.com/products/envizi (Tier-2)
- Measurabl — https://www.measurabl.com/ and https://www.measurabl.com/optimize/ (Tier-2)
- Arcadia — https://www.arcadia.com/ (Tier-2)
- Intelex — https://www.intelex.com/products/sustainability-management/ (Tier-2)
- Cross-pass corroboration (not re-fetched): research/energy-carbon-management.md (ECM seam + Resource Advisor 403 record), applications/energy-carbon-management.md (Related Types), STATUS.md boundary entries for circular-economy-platform, recycling-operations-management, carbon-accounting-platform.

**Source-access Limitation:** No Tier-1 help centers / user manuals were reachable for any sampled product (IBM docs envizi-esg-suite → 403; Measurabl help center not fetched after Tier-2 pages sufficed; Quentic fact-sheet PDF not fetched). Two market anchors (Schneider Resource Advisor, ENERGY STAR Portfolio Manager) unreachable. Per evidence rules: no precise operational details (numeric limits, default settings, turnaround windows, exact interval cadences) are asserted in the final document; vendor numeric claims observed on pages stay in these notes only.

## Product A — Quentic Environmental Management (module)

### Key observations (Layer A — direct, quoted from module page)

- Module tagline: "Track resources and costs in real time". Page promise: "Reduce wastage & emissions and improve energy performance".
- "Our environmental management software enables you to monitor electricity, gas, and water consumption, thus improving energy efficiency and waste management performance."
- "With Quentic Environmental Management software, you have current consumption values and cost trends for every resource at your fingertips. Using automatically calculated key figures and powerful evaluations, we make instant overviews and further analyses easy."
- "Providing stable ground for your ISO 14001 environmental management system and a firm foundation for sustainable success." Certified suitable for ISO 14001 AND ISO 50001 management systems.
- Four documented feature areas:
  1. **Resource monitoring** — "Track your consumption of energy, water, and other resources, as well as associated costs. Keep an eye on wastewater and long-term emissions."
  2. **Environmental reports** — "benchmark different sites and carry out target/actual comparisons… document your findings and publish them in your next environmental report."
  3. **Waste management** — "a structured register for waste classification and verifiable documentation of waste treatment. Key waste management figures such as costs, revenues and recycling rates are available on demand."
  4. **Environmental indicators** — "automatically calculating key figures according to individual specifications so you can correlate different environmental management data and make positive improvements."
- Customer quote (energy manager + HSE coordinator, automotive supplier): "One of our main requirements was to record our whole energy management across all locations in a centralized system. With Quentic, we were finally able to generate useful indicators."
- Internal seam: Quentic ships a SEPARATE "Sustainability" module (carbon accounting, climate disclosure, climate modeling, ESG analytics & insights, Scope 3) beside the Environmental Management module — the suite itself distinguishes resource-consumption management from ESG-program/disclosure management.
- Vendor scale claims on page (1,200+ customers etc.) — positioning, not asserted.

## Product B — IBM Envizi

### Key observations (Layer A — direct)

- Declared center: ESG data management ("compliance ready solution for ESG data… analytics, reporting and planning").
- Decarbonization module family (the resource-operations face of the suite):
  - **Utility Bill Analytics**: "Consolidate and analyze all your utility billing data in one place to identify anomalies and reduce costs and consumption."
  - **Interval Meter Analytics**: "Automatically capture and analyze interval meter data to inform and accelerate energy efficiency initiatives across facilities."
  - **Target Setting + Tracking**: "Set and track the performance of your consumption-, energy- and emissions-reduction targets."
  - Planning Analytics and Sustainability Program Tracking sit beside (program/planning objects — decarbonization-planning territory per that pass's seam).
- Data foundation: automated ingestion from "ERP systems, IoT and metering platforms, utility providers, spreadsheets, and supplier portals"; consistent data tagging; "flexible organizational modeling… regions, sites, assets, product lines, and joint ventures"; "data health checks & audit trails… finance-grade, traceable data".
- Case-study evidence of the multi-resource record (Layer A for what customers do with it): GPT Group "manage emissions, energy and waste data" and "$20M annual cost savings on energy and water costs" — vendor-claimed figure, NOT asserted as fact.
- Building Ratings + Benchmarks module (building footprint + utility data, ratings, benchmarking) — building-regime capability inside the suite.
- Suite pole: energy, water, waste live inside the ESG data platform; the declared center is the ESG data/program, not the resource ledger. Center-of-gravity straddle documented.

## Product C — Measurabl

### Key observations (Layer A — direct)

- Positioning: ESG platform for real estate; audiences: owners, operators, lenders, investors/indexes.
- Platform data-type list ("Quantum Cloud"): Bill Data, Building Data, Emissions, Ratings, Meter Interval Data, Benchmarks, Estimates, Equipment Data, Certifications, Ordinances, Physical Climate Risk Data, Projects, Audits. (Waste NOT explicitly named on fetched pages — not asserted.)
- Multi-resource evidence: **Comply** — "Track utility data, energy and water use for compliance in multifamily properties." Water is first-class; energy + water = multi-class on one platform.
- Efficiency loop (from Optimize page): "Gain real-time visibility into energy usage, cost, and carbon across your portfolio — so you can identify inefficiencies, improve operations, and drive measurable ROI."
  - Interval data captured continuously through system integrations or delivered daily through utility connections; hardware optional ("start fast" via utility data, "go deeper" with meters).
  - Surfaces: **Performance** ("Evaluate real-time data against historical trends to identify areas of opportunity"), **Explore** ("Access time series meter data through a fast and flexible query tool"), **Measures** ("Act on recommendations to optimize energy consumption and reduce carbon emissions").
  - Team machinery: "set accurate budgets, track variance"; automated data collection/verification.
- Navigate family: Data Manager (data quality), Insights, Decarb (scenarios + projects + measure impact), Disclosure (SFDR, GRESB).
- Regime machinery: Ordinance Filing product, ESGx Benchmarks, building ratings; vendor is a repeat ENERGY STAR Partner of the Year (positioning).
- Grain: the building portfolio (sites = buildings/assets), owner/operator/investor seats — distinct customer tier from Envizi/Quentic.

## Product D — Arcadia (boundary specimen)

### Key observations (Layer A — direct)

- "Arcadia is the energy intelligence platform for businesses. One place to pay utility bills, buy energy, and advance sustainability."
- Utility Expense Management: "Centralize, validate, and pay utility invoices across your entire portfolio." Data model: utility bill & interval data, tariff calculator, AI standardization ("fill data gaps, reconcile anomalies").
- **Extended resources exist as SEPARATE product lines, not a unified multi-resource center**: "Waste Expense Management", "Telecom Expense Management", "Waste Advising Services" listed beside energy products (Utility Expense Management, Energy Procurement, Rate Monitoring, Renewable Energy…).
- Confirms the ECM pass's observation from this side: even when an energy-centered platform carries waste/telecom lines, the center remains the utility/energy spend-data engine. The resource-center test separates this from the REM Type.

## Product E — Intelex Sustainability Management (boundary specimen)

### Key observations (Layer A — direct)

- Declared center: sustainability DATA for reporting and risk — "collecting and analyzing real-time sustainability data… reporting to major frameworks, including ESRS, GRI, CDP and SASB"; emissions-factor library + calculation engine; Datamaran materiality/risk; Power BI/Snowflake analytics.
- Resource operations appear as SEPARATE applications: "Water Quality Management", "Waste Management", "Inspection Management" listed under "Improve Organizational Efficiency"; sustainability page itself centers emissions + frameworks + risk.
- Confirms the ESG-program center vs resource-consumption center seam from the ESG side.

## Cross-product Comparison

| Dimension | Quentic Environmental Management | IBM Envizi | Measurabl | Arcadia | Intelex Sustainability |
|---|---|---|---|---|---|
| Unit of record | consumption values + cost trends per resource per location | utility/interval data records per site/asset in org hierarchy | bill + interval + equipment data per building | validated utility bill/interval records per account/meter | sustainability metrics per org (emissions-centered) |
| Resource classes | electricity, gas, water, other resources, wastewater, waste | energy (bills + interval), water, waste (case study) | energy, water, emissions (waste unobserved) | energy/utility (waste & telecom as separate products) | emissions, air emissions, waste (via separate apps) |
| Multi-class center? | YES — explicit ("every resource") | YES within suite, center = ESG data | YES (energy + water) | NO — energy center | NO — ESG center |
| Capture | module data management (entries), "real time" claims | bills, interval, ERP/IoT/utility feeds, spreadsheets | utility delivery, integrations, meters/hardware | utility feeds, AI standardization | predefined forms, mobile, offline |
| Cost co-management | yes — "consumption values and cost trends" | yes — bill analytics "reduce costs and consumption" | yes — usage, cost, budgets/variance | yes — pay/audit invoices | incidental |
| Efficiency loop | target/actual comparisons, site benchmarking, indicators/key figures | anomalies, efficiency initiatives, consumption/energy/emissions targets | performance vs historical, recommendations→measures, budgets/variance | audit/anomaly, rate optimization (energy) | process efficiency framing, not a resource loop |
| Carbon | "long-term emissions" watched; separate Sustainability module for carbon | computed from same data (emissions engine) | emissions across portfolio | carbon management as separate line | the center itself |
| Regime packaging | ISO 14001 / ISO 50001 | building ratings & benchmarks, frameworks | GRESB/SFDR, ordinance filing, ENERGY STAR heritage | procurement/market side | ESRS/GRI/CDP/SASB |
| Verdict vs Type | IN — resource-led module | IN at suite pole (straddles toward ESG) | IN at real-estate pole | OUT — Energy & Carbon Management pole | OUT — Sustainability/ESG pole |

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures. Removing any one dissolves the Type:

1. **The multi-resource consumption record of record.** Persistent recorded consumption of physical resources — quantities of a resource class, bound to an identified site/asset, accumulated over periods, drawn from meter readings, bills, manual entries or estimates. This is the organization's resource ledger. Remove → an expense tracker / program tracker with no resource record.
2. **Resource-class breadth as the managed center.** More than one resource class managed on an equal footing — the class set is configured per organization (energy carriers, water, waste streams, other inputs) and the system's discipline is the resource flow itself. Energy is one resource among several. Remove (one class becomes the whole center) → Energy & Carbon Management, Building Energy Management, waste or water operational Types.
3. **The efficiency loop.** The record is operated: normalize/compare (site-vs-site benchmarks, target-vs-actual, intensity indicators), surface waste and inefficiency, and track reductions in consumption (and commonly its cost) against targets. Remove → a passive resource archive — a ledger nobody works from.

Jointly load-bearing:
- 1 alone = consumption data warehouse / utility ledger.
- 2 alone = a resource taxonomy with nothing in it.
- 3 without 1+2 = generic performance analytics over nothing.
- 1+2 without 3 = resource archive; the "management" and the "efficiency" die.
- 1+3 without 2 = the single-medium Types (energy-led → ECM; waste-led → waste ops).
- 2+3 without 1 = efficiency ambitions with no record to operate on.

### L1 — Common Mature Structure (evidence: cross-product, Layer B)

- Capture fabric: utility bills + meter/interval feeds + manual entries + integrations, with validation/completeness machinery and correction handling (Envizi health checks/audit trails; Measurabl Data Manager; Arcadia AI standardization; Quentic data management).
- Cost managed beside consumption (every positive specimen).
- Carbon/emissions computed from the same resource data as a derived output (Envizi engine; Measurabl; Quentic "long-term emissions").
- Targets on consumption/cost/emissions with tracking (Envizi Target Setting + Tracking; Quentic target/actual; Measurabl budgets/variance).
- Benchmarking and intensity indicators across sites (Quentic site benchmarks; Envizi Building Ratings + Benchmarks; Measurabl Benchmarks).
- Organizational hierarchy/portfolio with roll-ups and multi-seat access (sustainability/energy/finance seats).
- Periodic reporting outputs — environmental reports, ESG framework disclosures, compliance/benchmark filings.
- Data-quality/audit machinery where the record feeds corporate reporting.

### L2 — Variant / Optional Structure

- Cadence: bill-cycle-led records vs interval/real-time-led (both poles in-sample; ledger-era practice precedes both).
- Grain: enterprise multi-site estate vs real-estate building portfolio vs industrial/manufacturing sites.
- Packaging: standalone platform vs module inside an EHS suite (Quentic) vs module inside an ESG suite (Envizi) vs service-led posture (directly evidenced at Arcadia: advisory teams beside the platform; the unreachable anchor product's own service-led class unverified).
- Resource-class mix and depth per class (energy-deep vs balanced vs waste-deep; waste-depth ranges from a register to full waste ops).
- Regime packaging: ISO 14001/50001 evidence (European industrial); US building benchmarking/ordinance regimes (real estate); voluntary/mandatory ESG framework outputs.
- Extensions: procurement/transaction layers (Arcadia), mobile/offline frontline collection (Intelex), project/measure management (Measurabl Measures; Envizi Program Tracking), AI anomaly detection.
- Cost-led expense flavor at the edge (waste/telecom expense management without a consumption loop) — the drift direction toward spend management.

### L3 — Vendor-specific (research notes only)

- Quentic module naming and its Environmental-Management-vs-Sustainability module split; ISO certification badges.
- Measurabl product branding (Quantum Cloud, Navigate, Optimize, ESGx, Comply), interval claim "every 5–15 minutes", the "up to 33%" estimate-inflation marketing claim, ENERGY STAR Partner of the Year count.
- Envizi module names (Utility Bill Analytics etc.), pricing-by-data-volume, Verdantix placement claim, case-study figures (GPT $20M, ↓45% Downer error rate).
- Arcadia's UEM/Automated Bill Payment/Budgets product family, acquisition history (ENGIE Impact 2026, RPD Energy 2025), scale figures ($30B payments, 4.5M meters).
- Intelex's Datamaran partnership, eshAI, content packs (EPA OOOOa/Subpart W/SARA Tier II/SPCC), 20,000 pre-loaded emission factors claim.

## Vendor-specific Findings (not promoted)

All L3 items above. None of these entered the canonical core.

## Boundary Findings

Removal-test judgments, each tied to sampled evidence:

- **vs Energy & Carbon Management (§21, processed):** ECM's center is the energy/utility data engine with carbon riding it; extended resources appear there as variants. Here the center is the multi-resource record itself. **Resource-center test applied and DISCHARGED as that pass requested:** Arcadia (energy center + waste/telecom product lines) demonstrates an energy-centered product is NOT this Type; Envizi/Quentic demonstrate multi-resource-centered products are. Keep-both; the seam is the center of gravity, not feature lists. Consistent with that pass's recorded flag.
- **vs Carbon Accounting Platform (§21, processed):** there the all-scopes emissions inventory of record is the center; here carbon is a common derived output of the resource record. Emissions computed from resource data do not make a product carbon accounting. Confirms that pass's seam from this side.
- **vs Sustainability / ESG Management Platform (§21, sustainability-management-platform + esg-management-platform UNPROCESSED):** the ESG-program center (framework data, materiality, disclosure programs) vs the physical-resource-consumption center. Evidence both directions: Intelex is ESG-centered despite shipping water/waste applications; Quentic ships Environmental Management (resources) and Sustainability (ESG) as separate modules of one suite; Envizi straddles at the suite pole. **Flag for both unprocessed siblings:** apply the center-of-gravity test; enterprise suites will straddle.
- **vs ESG Reporting Platform (§21, processed):** disclosure-production center vs consumption-efficiency center; reporting appears here as an output surface only. Consistent with that pass's collect-once-report-many framing.
- **vs Waste Management Platform (§21, UNPROCESSED):** waste-as-one-resource-flow (quantities, costs, recycling-rate figures, a classification register) vs waste-operations record (hauling/disposal lifecycle). Quentic's waste register is the light pole inside a resource module. **Flag for that pass:** the waste leaf holds the operations center; REM holds waste as one managed flow among several.
- **vs Recycling Operations Management (§21, processed):** recovery ledger with commodity-out leg vs own-estate consumption record. No conflict; disjoint centers.
- **vs Circular Economy Platform (§21, processed):** material loops and multi-party circulation (exchange/traceability/outcome accounting) vs own-estate efficiency loop. Confirms that pass's umbrella from this side; REM is not one of its five poles.
- **vs Building Energy Management (§17, processed):** building-operations seat (systems, setpoints, operational energy) vs organization-level resource position across the estate. Real-estate-pole REM products (Measurabl) sit at portfolio/data grain, not building-system operations grain; shared-product overlap pattern mirrors the §17/§21 ECM note.
- **vs Decarbonization Planning Platform (§21, processed):** the managed reduction program (plan/levers/roadmap object) vs the efficiency loop over the record. Targets-and-tracking is performance machinery here; where the plan object becomes the center, the product extends into that Type. Consistent with that pass's program-object test.
- **vs Environmental Management System (§21, UNPROCESSED):** ISO 14001-style management-system cycle (aspects/impacts, compliance evaluation, management review) vs the resource-consumption record + efficiency discipline. Quentic evidences both living in one suite (EMS module family + resource module; resource module claims to provide "stable ground" for ISO 14001). **Flag for that pass:** candidate seam = management-system machinery vs resource data/efficiency loop.
- **vs Environmental Data Platform (§21, UNPROCESSED):** generic environmental data infrastructure vs the resource-consumption-specific record + efficiency discipline. **Flag recorded.**
- **vs Telecom Expense Management / Spend Management (§10/§14):** spend-only management of resource-like expense lines without a consumption record or efficiency loop is spend management, not this Type (Arcadia's telecom/waste expense lines illustrate the shape).

## Historical / Market-Sample Check

Would older, regional, platform-native products still fit the L0?

- The three-leg core is era-neutral: a plant engineer's ledger of meter readings (electricity, gas, water, waste tickets) with monthly indicator sheets (consumption per unit of output, target-vs-actual, site comparisons) satisfies all three legs with no cloud, interval data, or AI. Quentic's own framing ("record… across all locations in a centralized system… generate useful indicators") is the direct descendant of that practice.
- Regional spread holds: European ISO-driven industrial practice (Quentic, explicit ISO 14001/50001 framing), US real-estate benchmarking practice (Measurabl — ordinance filing, benchmarks, ratings), global enterprise ESG practice (Envizi). No single regime defines the core.
- The free public-tool pole (ENERGY STAR Portfolio Manager class) is unreachable this pass, so its fit is reasoned, not evidenced: as a consumption-per-building tracker with benchmarking it matches the core shape; no specifics asserted.
- Anti-overfit guard: "real-time/interval" is NOT definitional (bill/ledger cadence in-type); "carbon" is NOT definitional (derived output); "multi-site cloud platform" is NOT definitional (the core survives the ledger test).

## Uncertainties

1. The market's literal anchor product (Schneider Resource Advisor) was unreachable across two passes (403 ×4 total paths). The category-naming evidence therefore rests on the directory leaf + sampled products; that product's structure is unverified and unasserted.
2. ENERGY STAR Portfolio Manager unreachable — the government-native free-tool pole is reasoned, not evidenced.
3. Measurabl waste tracking: implied by its disclosure surfaces (GRESB-class) but not directly observed on fetched pages — waste not asserted for that product.
4. Industrial material-input efficiency (raw materials/packaging as managed resource flows) appears plausible but no sampled product documents it in depth — recorded as a possible variant, not asserted.
5. No Tier-1 help centers reached for any product — operational specifics (units handling, estimation defaults, factor management depth, role models) stay unasserted.
6. The boundary between REM and the unprocessed sustainability-management-platform / esg-management-platform / environmental-management-system / environmental-data-platform / waste-management-platform leaves is held by reasoning + module-split evidence, not yet joint-reviewed with those passes.

## Final Synthesis

A Resource Efficiency Management application is the consuming organization's system of record for the physical resources it uses, held as a multi-resource consumption ledger (quantities per resource class per site per period, commonly with cost) and operated through an efficiency loop — normalize, benchmark, target/actual compare, surface waste, track reductions. Its identity is the multi-resource center: energy one resource among several, carbon a derived output, reporting an output surface, cost a co-managed attribute. The Type is bounded by the resource-center test against Energy & Carbon Management (energy-data engine center), by the program-object test against Sustainability/ESG platforms and Decarbonization Planning (program/disclosure centers), by the inventory-of-record test against Carbon Accounting, by the operations test against waste/water operational Types, and by the system-cycle test against Environmental Management System. The market realizes the Type as standalone resource platforms (real-estate pole), resource modules of EHS suites (European industrial pole), and the resource-data face of enterprise ESG suites (suite pole); a service-led platform class exists (anchor unreachable). Historical ledger-era practice fits the core without modern machinery.

Verdict: the leaf stands as an independent Type. No directory change requested.
