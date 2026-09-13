# Research Notes — Energy & Carbon Management

Research date: 2026-09-08
Slug: energy-carbon-management
Directory leaf: Energy & Carbon Management (§21 Environment, Sustainability & Climate)

## Research Goal

Understand what "Energy & Carbon Management" software actually is as an Application Type: what its center of gravity is, what objects and data it holds, what its defining loop is, what is definitional vs merely common in the current market, and where its boundaries sit against neighboring Types.

This pass must also discharge the adjacency flag recorded in STATUS.md by the decarbonization-planning-platform pass: "energy-carbon-management (§21 sibling, unprocessed) ... proposed seam: energy-carbon-management centers the energy/carbon data-operations layer (consumption, metering, optimization) while this Type centers the managed reduction program (plan + levers + tracked delivery); the energy-carbon-management pass should apply the program-object test and treat research/decarbonization-planning-platform.md §Boundary Findings as counterparty."

## Initial Boundary (hypothesis before research)

- What: organization-side software that manages an energy-buying organization's energy consumption data and the carbon emissions derived from it — utility bills, interval meter data, energy cost/consumption analytics, energy-derived carbon reporting. Distinct working hypothesis from prior passes: the center is the data-operations layer, not the strategic reduction program and not the all-scopes accounting-of-record.
- Users: energy managers, sustainability leads, finance/utility-billing staff, facility/site operators as data providers.
- Nearest neighbors: Building Energy Management (§17, processed — building-scoped operational energy), Carbon Accounting Platform (§21, processed — all-scopes inventory of record), Decarbonization Planning Platform (§21, processed — managed reduction program; counterparty), Energy Management System (§19, unprocessed — grid/operator side), Meter Data Management System (§19, unprocessed — utility side), Customer Energy Management (§19, processed — household/customer side), Sustainability/ESG Management Platform (§21, unprocessed — broader), Resource Efficiency Management (§21, unprocessed — wider resource scope), District Energy Management (§19, processed — thermal network operator), Utility Billing Platform (§19, unprocessed — utility's own billing).
- Unknowns: does the market product carrying this leaf's name have a stable core distinct from BEM and carbon accounting? Is carbon energy-derived or full-scope? Where do bill payment/procurement and program tracking sit? What is the regional shape (US ENERGY STAR regime vs UK M&T/SECR heritage)?

## Research Questions

1. What data does the platform hold as its system of record (bills? interval meters? other resources)? What does a consumption record carry?
2. How does the energy side work: consolidation, validation, normalization, variance analysis, savings measurement?
3. How does the carbon side relate to the energy data — derived from it, co-equal, or separate accounting machinery?
4. What is managed as "performance": comparisons, benchmarks, baselines, targets, compliance?
5. What roles use it (energy manager, sustainability, finance, facility)?
6. What outputs exist (reports, disclosure, dashboards)?
7. Where do targets sit vs the decarbonization plan/program object (program-object test)?
8. Where do bill payment, procurement, rebates sit (transaction layer)?
9. What is the seam against BEM, carbon accounting, and ESG suites?
10. Historical check: do bill-accounting / M&T-era practices (pre-interval, pre-cloud) satisfy the same core?

## Representative Products (sample rationale)

| Product | Pole | Philosophy | Customer level |
|---|---|---|---|
| IBM Envizi | enterprise ESG suite with a full energy module family | data-platform-first: one governed data spine feeding energy analytics, emissions, reporting, planning | global enterprise / multinational (Ikano, Downer, GPT Group, BanFast) |
| EnergyCAP | bill-led energy & utility management product suite | utility-workflow-first: bills as the primary record, analytics and carbon as add-on layers | institutional + commercial (higher ed, government, healthcare, retail, manufacturing) |
| Arcadia (acquired ENGIE Impact, 2026-05) | managed-service energy intelligence platform | data-foundation + expert advisory + execution (payments, procurement, audits, rebates) | Fortune-500-class multi-site enterprises |
| MRI Energy (eSight lineage) | suite-embedded enterprise energy management | enterprise energy/carbon reporting inside an IWMS-adjacent suite | enterprise real estate / ESCo / multi-site (carried over from the 2026-09-07 BEM pass) |

Schneider EcoStruxure Resource Advisor (the product most explicitly branded "energy and carbon management") was attempted this pass and returned 403; same failure in the BEM pass (2026-09-07). Abandoned per network rules; recorded as a sourcing limitation. No claims about it are promoted.

## Sources

Fetched 2026-09-08:

- IBM Envizi (root) — https://www.ibm.com/products/envizi
- IBM Envizi Utility Bill Analytics — https://www.ibm.com/products/envizi/utility-bill-analytics
- EnergyCAP (root) — https://www.energycap.com/
- EnergyCAP Emissions / Carbon Hub — https://www.energycap.com/carbon-accounting-software/
- Arcadia (root) — https://www.arcadia.com/ (fetched as engieimpact.com redirect target — ENGIE Impact's site now serves Arcadia branding)
- Arcadia Energy Management — https://www.arcadia.com/energy-management
- Arcadia Carbon Management — https://www.arcadia.com/carbon-management

Carried-over evidence (prior passes, same production pack):

- MRI Energy — research/building-energy-management.md (fetched 2026-09-07, product/FAQ pages)
- EnergyCAP operational context — research/building-energy-management.md (2026-09-07; includes its reachable help center)
- Envizi Decarbonization module family — research/decarbonization-planning-platform.md (2026-09-07)
- Envizi ESG/emissions modules — research/carbon-accounting-platform.md (2026-09-07)

Sourcing limitations:

- All evidence this pass is Tier 2 (official product/marketing surfaces). No product help center or user manual was fetched this pass. Operational internals (exact validation rules, workflow states, permission models) are therefore stated at moderate strength only; no precise numeric claims promoted to the final document.
- Schneider Resource Advisor unreachable (403, second failure across passes) — the "pure-play branded ECM" pole is under-documented.
- Arcadia vendor stats ($30B payments, 4.5M meters, 100M monthly bill calculations, 25% of Fortune 500, $100B spend under management) are marketing figures, recorded here only.
- ENGIE Impact's own surfaces were not separately fetched; the sampled evidence for the managed-service pole comes from Arcadia's pages (which now carry the combined story and the "30+ years of enterprise energy management" heritage claim).

## Product Observations

### IBM Envizi — Evidence layer A (direct, official product pages)

- Root positioning: ESG data platform — "Strengthen reporting, reduce risk and accelerate decarbonization with trusted, AI-assisted sustainability data management." Modules in three families:
  - Emissions Management: Scope 1/2 GHG Accounting + Reporting ("emissions calculation engine built on the GHG Protocol"), Scope 3, Emissions API, Emissions Calculations in Excel, Scope 3 Financed Emissions, Supply Chain Intelligence.
  - ESG Reporting: ESG Reporting Frameworks, **Building Ratings + Benchmarks** ("Capture building footprint and utility data, calculate ratings and benchmark and track building performance in one place"), Surveys + Assessments.
  - Decarbonization: Planning Analytics, Sustainability Program Tracking, **Utility Bill Analytics**, **Interval Meter Analytics**, **Target Setting + Tracking** ("consumption-, energy- and emissions-reduction targets").
- Data foundation features (root page): automated data capture from ERP, IoT and metering platforms, utility providers, spreadsheets, supplier portals; consistent data tagging; flexible organizational hierarchy ("regions, sites, assets, product lines, and joint ventures") with roll-ups; data health checks + full audit trails ("finance-grade validation and auditability").
- Utility Bill Analytics page (the energy-operations module): "Consolidate and analyze all your utility billing data in one place to identify anomalies and reduce costs and consumption." Mechanics: ELT capture of billing data into "a single, integrated record"; automated conversions/calculations; normalization of energy performance "for weather and KPI metrics"; outlier/variance identification; savings "comparing actual consumption against historical baselines adjusted for weather". Named features: Utility performance analysis ("Analyze and report utility cost, consumption and **emissions** across different geographical regions, facility types and groups"), Metrics conversion engine, Utility variance analysis, Integrated regression modeler ("normalizes energy performance for weather and KPI metrics so you can measure and verify savings over time"), advanced filtering, Power BI-embedded reporting.
- Use case "Decarbonization": "Consolidate energy data and drive improved energy management across your organization."
- Case studies (vendor claims): Ikano >15K data types for CSRD; Downer Scope 3 categorization error −45%; GPT Group manages "emissions, energy and waste data", $20M annual energy+water savings; BanFast energy performance insight.
- Pricing: data-volume based (vendor page).

### EnergyCAP — Evidence layer A (direct, official product pages; operational context from the 2026-09-07 BEM pass)

- Root positioning: "Expert-driven energy and utility management software" — "EnergyCAP® brings energy, utility, and emissions data into one integrated platform—with AI that supports the full utility workflow, from bill data capture and error detection to faster insights and on-time payments."
- Product architecture: "Start with **Utility Management** [utility bill data management], then customize with helpful add-ons": **Interval Data** ("Real-time energy analytics"), **Emissions** (Carbon Hub — "Financial-grade scope emissions data"), **Bill Capture** ("Audit and vendor management"), **Bill Pay** ("Utility bill payment services"). Features: Watts AI/chat; chargebacks and tenant rebilling; accounting bundle; BI reporting; utility bill auditing; facility benchmarking; ENERGY STAR integration; measurement & verification (IPMVP-framed page).
- Roles: "Energy Managers, Sustainability Leaders, Finance Leaders" — "cross-functional teams". Industries: higher ed, K-12, government, healthcare, commercial campuses, hotels, retail, grocery, manufacturing (incl. automotive), utility vendors.
- Carbon page: "Carbon accounting software **built on your utility data**" — "brings your Scope 1, 2, and 3 emissions into the same centralized, verified platform as your utility bills; no spreadsheets, no duplicate entry, no silos. Just powerful utility-based carbon tracking, streamlined GHG reporting tools, and lower administrative load."
- From the BEM pass (2026-09-07): bill audit with flagged items, rate schedules/vendors, accruals/budgets, accounting export; benchmarking; weather/degree-day normalization; interval analytics with data-quality monitoring; M&V with cost avoidance; dual hierarchy (sites/meters vs accounts/cost centers) as product architecture; data-completeness grading; "40+ years of energy excellence".

### Arcadia (incl. ENGIE Impact) — Evidence layer A (direct, official pages)

- Root positioning: "The leading energy intelligence platform | Arcadia" — "Energy management to save money, mitigate risk, and cut carbon. ... One place to pay utility bills, buy energy, and advance sustainability. We combine unified data, AI-powered analytics, and expert advisory..."
- Three pillars: Utility Expense Management ("Centralize, validate, and pay utility invoices across your entire portfolio"), Energy Management & Procurement ("Execute procurement strategies aligned to your risk tolerance"), Sustainability Advising ("Accurate, audit-ready emissions data for reporting and disclosure backed by expert advisory").
- Platform: Data Platform ("foundational data layer consolidates various sources of energy data into a unified model ... standardize diverse inputs, fill data gaps, and reconcile anomalies to create a definitive source of truth that powers everything else"); Utility Bill & Interval Data; Tariff & Energy Rate Calculator; Solar & Storage Analysis; Applied AI.
- Energy Management page: "Turn utility data into an efficiency roadmap" — "Arcadia processes, validates, and monitors energy data across your full portfolio — catching billing errors, detecting anomalies, tracking compliance, and identifying efficiency opportunities. Backed by a team of Professional Engineers, Certified Energy Managers, and energy analysts built to execute at enterprise scale." Functions: centralized utility data collection, bill processing, account management across every site and market ("a single source of truth for consumption, costs, and performance without manual data entry"); site and remote audits, efficiency scenario modeling, business cases "prioritized by ROI"; ENERGY STAR Portfolio Manager benchmarking ("40,000 sites monthly") + building-performance-standard compliance tracking; interval-data anomaly monitoring; historical bill audits recovering overpayments; rebate/incentive lifecycle management. Framed as "a continuous program for cost reduction and performance improvement". "30+ years of enterprise energy management" (ENGIE Impact heritage).
- Carbon Management page: "Turn carbon data into strategy" — "Arcadia starts with the data foundation — accurate, audit-ready emissions inventories across Scope 1, 2, and 3. Expert advisors and AI-powered analytics translate data into prioritized action." Functions: verified GHG Protocol-aligned Scope 1/2/3 baseline; hotspot analysis + scenario modeling; "Reduction pathway modeling, target development, and a structured decarbonization roadmap"; Scope 3 value-chain modeling + supplier strategies; disclosure support (GRI, SASB, TCFD, CSRD, CDP "and evolving state and regional mandates").
- Market context: Axios (2026-05-01) — Arcadia acquired ENGIE Impact. Vendor stats (marketing): $30B utility payments processed annually; 25% of the Fortune 500 served; 1,500+ enterprise customers; 4.5M meters under management; $100B utility spend under management; 100M monthly bill calculations.

### MRI Energy (eSight lineage) — carried-over observations (BEM pass, 2026-09-07)

- Enterprise energy management suite: energy, carbon, and sustainability reporting for multi-site organizations; local data collection (Modbus TCP/IP, OPC HDA, oBIX-class integrations); suite siblings (Facilities, IWMS); ESCo/higher-ed/real-estate customers. Carbon reporting rides on the same energy data as consumption analytics (emissions modules).
- Used here only for cross-product commonality context; details in research/building-energy-management.md.

## Cross-product Comparison

| Dimension | IBM Envizi | EnergyCAP | Arcadia (+ENGIE Impact) | MRI Energy |
|---|---|---|---|---|
| System of record | utility billing data + interval meter data on a governed data spine (org hierarchy: regions/sites/assets) | utility bills as primary record; interval as add-on; dual hierarchy (sites/meters, accounts/cost centers) | unified utility bill + interval data layer across the portfolio ("definitive source of truth") | energy data collected from sites (meters/BMS-class integrations) |
| Record substance | cost + consumption (+ emissions) per record | cost + consumption per bill/reading | consumption, costs, performance | consumption + cost + derived carbon |
| Validation machinery | data health checks, audit trails, finance-grade | bill auditing, error detection, data-completeness grading | validation, anomaly reconciliation, historical bill audits | data-quality monitoring |
| Analysis loop | variance analysis, outliers, weather/KPI normalization, regression modeler, M&V vs adjusted baselines | benchmarking, degree-day normalization, M&V (IPMVP-framed), anomaly alerts | audits, efficiency scenario modeling, ROI-prioritized opportunities, anomaly monitoring, ENERGY STAR benchmarking | analytics + reporting on consumption/carbon |
| Carbon side | emissions engine on the same spine (S1/2/3, financed, supply chain) | "built on your utility data"; S1/2/3 in the same platform as the bills | audit-ready S1/2/3 on the same data foundation (advisory-delivered) | carbon reporting from energy data |
| Targets | Target Setting + Tracking (consumption/energy/emissions) | targets/budgets tracking (BEM-pass context) | target development (advisory) | targets (suite context) |
| Managed program object (plan/levers/roadmap) | separate modules (Planning Analytics, Program Tracking) — not the energy core | not observed as core | advisory-delivered decarbonization roadmap — service layer, not the data core | not observed as core |
| Transaction layer | — | Bill Capture + Bill Pay services | bill payment + energy procurement + rebates (first-class) | — |
| Extended resources | energy, waste, water (case studies) | utility scope (electric/gas/water-class) | waste + telecom expense products beside energy | energy focus |
| Delivery posture | enterprise SaaS suite (data-volume pricing) | product suite + managed bill services | platform + managed service/advisory | suite module |
| Regional regime flavor | CSRD-era disclosure (EU case studies), global | US (ENERGY STAR), institutional | US (ENERGY STAR, building performance standards) + global disclosure | UK/EU + global enterprise |

### Stable commonalities (cross-product, layer B)

1. **Portfolio-wide energy data of record** — every sampled product's foundation is the organization's utility/energy data consolidated across many sites/accounts as durable records carrying consumption and cost. "Across your portfolio" / "across your full portfolio" / "across every site and market" is the recurring scope language.
2. **Validation and data-quality discipline** — bill/error auditing, anomaly detection, completeness checks, audit trails. The data is treated as report-grade (Envizi "finance-grade"; EnergyCAP "financial-grade"; Arcadia "audit-ready"), not as telemetry.
3. **A managed performance loop over the data** — normalization (weather/KPI/regression), comparison (variance, benchmark, baseline), surfacing of outliers/anomalies/opportunities, and tracked outcomes (savings vs adjusted baselines, resolved errors, compliance status).
4. **Carbon as a co-equal managed output of the same platform** — all four carry emissions computation and GHG reporting on the same data foundation as the energy data; the bill-led vendor's own words are "carbon accounting software built on your utility data". Energy-derived carbon is the foundation; full Scope 1/2/3 breadth is common in current products.
5. **Cost as a first-class managed quantity beside consumption** — utility cost, budgets, savings, and (in two products) tenant chargebacks.
6. **Multi-stakeholder seat model** — energy managers + sustainability leaders + finance leaders (EnergyCAP names all three; Envizi and Arcadia pitch the same cross-functional triangle).
7. **Reporting/disclosure outputs** — energy & carbon reports upward and outward (frameworks/regimes named at three of four).
8. **Target tracking on consumption/energy/emissions KPIs** — present in all four in some form.

### Product-specific / weaker-evidence observations

- Transaction layer (bill payment, energy procurement, rebate capture): first-class at Arcadia; services at EnergyCAP (Bill Capture/Pay); absent from Envizi's and MRI's energy-module presentation. Optional pole.
- Managed-service delivery (advisors/CEMs/PES executing the loop): Arcadia's identity; Envizi/EnergyCAP/MRI are software-led. Delivery-posture variant.
- Regression/normalization depth: Envizi names a regression modeler; EnergyCAP documents degree-day normalization; Arcadia claims scenario modeling; MRI not detailed. Common-in-sample, depth varies.
- Extended resources (water, waste, telecom expense): present at Envizi (case studies) and Arcadia (separate products); drift toward Resource Efficiency Management / spend-management territory. Variant.
- ENERGY STAR Portfolio Manager integration: US-regime implementation of benchmarking (EnergyCAP, Arcadia, Envizi "Building Ratings + Benchmarks"); benchmarking as a concept is common, the specific regime is regional.
- Building-performance-standard compliance tracking: Arcadia names it; US BPS regime context. Variant of the compliance-tracking commonality.
- Decarbonization program modules: Envizi carries Planning Analytics + Sustainability Program Tracking as distinct Decarbonization-family modules; Arcadia delivers roadmaps as advisory. Both keep the plan/program object outside the energy-data core.

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

An Energy & Carbon Management platform is recognizable only if all of the following hold:

```text
The organization's estate-wide energy data of record
  (utility bills and/or meter readings captured, consolidated, and validated
   as durable records across the organization's sites/accounts,
   each record carrying consumption and — for billed supply — cost)
        ↓
Carbon computed and maintained on the same foundation
  (the platform's own emissions records for the organization, reported as
   greenhouse-gas output; the energy data is the substrate)
        ↓
The managed performance loop
  (analysis over the data — normalization, comparison, variance, benchmark —
   surfaced and tracked to managed outcomes: actions, verified savings,
   targets, compliance, and energy & carbon reporting)
```

Three properties held jointly. Removal tests:

- Remove the carbon side → energy-management/utility-analytics software (the BEM/EMIS family), not an "energy & carbon" product.
- Remove the energy-data foundation and keep all-scopes activity×factor accounting of record → Carbon Accounting Platform.
- Remove the managed performance loop → a utility-data repository or bill archive (data-feed poles), not management.
- Remove cost/consumption record substance → a disclosure shell or BI layer.
- Make a managed reduction plan/levers object the center → Decarbonization Planning Platform.
- Scope the discipline down to buildings-and-their-systems operations with facility-seat ownership → Building Energy Management.

Historical / market-sample check: the energy-data leg descends directly from decades-old practice — utility-bill accounting per site and the UK monitoring-&-targeting tradition (meter/bill data + degree-day normalization + variance reporting) satisfy the data-of-record and performance-loop legs without interval data, cloud, or dashboards. The carbon leg joined the same systems with the GHG-reporting era; it is constitutive of the Type as named (remove it and the leaf collapses into energy management), so the pre-carbon era is recorded as the Type's lineage rather than a counterexample. No era-specific implementation (interval data, ENERGY STAR, cloud, AI, specific disclosure frameworks) is required by the definition. ✔

### L1 — Common Mature Structure

Very common in mature products, not required for recognition:

- interval meter data analytics beside bills (load profiles, anomalies, data-quality monitoring)
- normalization and baselines: weather/degree-day adjustment, KPI normalization, regression modeling
- benchmarking across sites and against external regimes (ENERGY STAR Portfolio Manager in the US implementation)
- savings measurement & verification against weather-adjusted baselines (IPMVP-class framing)
- targets on consumption/energy/emissions with tracking
- utility cost machinery: budgets, accruals, rate/tariff analysis, chargebacks and tenant rebilling, accounting export
- bill capture/auditing services and utility account administration
- ingestion fabric: utility feeds, meters/submeters, BMS/IoT, ERP, file import; APIs
- reporting: dashboards, scheduled/standard reports, disclosure support (frameworks/regimes)
- organizational hierarchy (regions/sites/assets) with roll-ups and role-scoped access across energy/sustainability/finance users
- AI assistance over the utility data (era-current)

### L2 — Variant / Optional Structure

- delivery posture: software-led product suite vs managed-service/advisory-led platform (engineers/CEMs executing the loop)
- transaction layer: bill payment, energy procurement (incl. renewables), rebate/incentive lifecycle — first-class in the managed-service pole
- carbon breadth: utility-derived Scope 1/2 as foundation, extending to full Scope 1/2/3, financed emissions, supply-chain categories in suite products
- decarbonization program modules (planning analytics, program/initiative tracking) — adjacency to Decarbonization Planning Platform
- extended resource data (water, waste, telecom expense) — drift toward Resource Efficiency Management / spend management
- building-ratings depth (ratings capture, benchmark score tracking, building-performance-standard compliance) — overlap with BEM
- regional regimes: US (ENERGY STAR, building performance standards), UK/EU (M&T heritage, SECR/ESOS lineage, CSRD-era disclosure)
- segment tuning: institutional portfolios (higher ed/government), commercial real estate, multi-site retail/chain, manufacturing/industrial
- pricing shape: data-volume-based vs tiered subscription vs bundled service

### L3 — Vendor-specific (kept out of the final document)

- IBM Envizi: module names (Utility Bill Analytics, Interval Meter Analytics, Planning Analytics, Sustainability Program Tracking, Target Setting + Tracking, Building Ratings + Benchmarks), Emissions API, Emissions Calculations in Excel, PowerReports/Power BI embedding, data-volume pricing, Verdantix Enterprise Carbon Management Software 2026 leader claim, case-study metrics (Ikano >15K data types; Downer −45% Scope 3 categorization error; GPT $20M savings).
- EnergyCAP: Watts AI/chat branding; Carbon Hub product naming (now "Emissions"); Bill Capture/Bill Pay services; dual hierarchy (sites/meters vs accounts/cost centers) as product architecture; data-completeness grading bands (BEM-pass notes); vendor stats (26,000 professionals, 40+ years, "3x ROI"/"3% bill savings" class claims from the BEM pass).
- Arcadia: platform stats ($30B payments/year, 4.5M meters, 100M monthly bill calculations, 25% of Fortune 500, $100B spend under management); 40,000 sites/month ENERGY STAR uploads; $4M/$1M savings claims; product names (Utility Expense Management, Rate Monitoring & Optimization, etc.); ENGIE Impact acquisition (Axios, 2026-05-01) and the "30+ years of enterprise energy management" heritage claim.
- MRI: eSight acquisition lineage; iDC local-service protocol list (Modbus TCP/IP, OPC HDA, oBIX); suite siblings; ESCo claims.
- Schneider Resource Advisor: no detail recorded — documentation unreachable (403 in two passes).

## Rejected Findings (considered, not promoted)

- "ECM products only account energy-derived (Scope 1/2) carbon" — rejected: all three freshly sampled products document Scope 1/2/3. The invariant is carbon maintained on the same platform/foundation as the energy data; scope breadth is an implementation axis.
- "Interval meter analytics is definitional" — rejected: EnergyCAP ships bills-first with interval as an add-on; bill-only products (and the bill-accounting lineage) satisfy the core.
- "Bill payment / procurement is definitional" — rejected: first-class only in the managed-service pole; absent from two products' core presentation. Optional.
- "The Type centers a decarbonization program" — rejected by the program-object test (see Boundary Findings): the plan/levers object is an extension or advisory layer, not the center.
- "Extended resources (water/waste) are part of the Type" — rejected for the core: present as extensions; centering them would be Resource Efficiency Management.
- "ENERGY STAR benchmarking is definitional" — rejected: US-regime implementation of the common benchmarking concept.
- "ECM is just BEM at enterprise scale" — rejected: see boundary finding; the carbon-co-equal output and the sustainability/finance seat model differ structurally, not just in scale.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (what makes it a different Type) |
|---|---|---|
| Carbon Accounting Platform (§21, processed) | complementary layers, commonly one suite at the enterprise pole | The center differs: this Type's center of gravity is the energy/utility data engine (bill & meter acquisition, validation, cost/consumption operations, performance loop) with carbon as an output; carbon accounting's center is the organization-wide activity×factor inventory of record with audit-grade accounting discipline across all scopes. Vendor's own wording marks the seam ("carbon accounting software built on your utility data"). Remove the energy-data engine → carbon accounting; remove the all-scopes accounting-of-record discipline → this Type. |
| Building Energy Management (§17, processed) | sibling discipline, shared products (EnergyCAP, MRI) | BEM's monitored entities are buildings and their systems, with a facility/energy-manager operational seat and M&V of conservation measures as the signature; this Type's substance is the organization's whole utility/energy estate with carbon as a co-equal output and sustainability+finance seats in the user model. Center on building operations → BEM; center on enterprise energy+carbon data & reporting → this Type. The blend is real and documented. |
| Decarbonization Planning Platform (§21, processed) — counterparty flag | adjacent; program-object test APPLIED this pass | Applied result: the managed plan/levers/roadmap object is NOT the center of the sampled ECM products. ECM tracks performance against energy/carbon targets (a KPI trajectory); decarbonization planning governs a structured program of reduction interventions (plan artifact, levers, tracked delivery). Where the program object becomes the center, the product extends into the sibling Type (Envizi's Decarbonization-family modules; Arcadia's advisory roadmaps). Keep-both ratified from this side; the decarbonization pass's proposed seam (data-operations layer vs managed program) is confirmed. |
| Sustainability / ESG Management Platform (§21, unprocessed) | broader suite | ESG suites manage wider environmental/social/governance data and disclosure; this Type's center is energy + carbon operations. Envizi is the drift case (full ESG suite whose distinctive engine is energy data). Center-of-gravity seam; flag stands for the unprocessed leaves. |
| Resource Efficiency Management (§21, unprocessed) | adjacent (wider resource scope) | extended resource data (water, waste) appears in ECM products as variants; when water/waste/other resources become the managed center, the leaf is the sibling Type. Recorded as a flag for that pass. |
| Energy Management System / EMS (§19, unprocessed) | naming collision, different domain | §19 EMS is grid/utility-operator side (generation/transmission control lineage); this Type is the energy-buying organization side. Same seam wording as the BEM pass. |
| Meter Data Management System (§19, unprocessed) | data-layer neighbor | MDMS administers the utility's meter data estate; this Type is the customer-side system of record for the organization's own energy/carbon position. |
| Customer Energy Management (§19, processed) | consumer-side sibling | the operator is an energy customer acting on their own premises (household/single customer); this Type is an organization managing a multi-site estate with corporate reporting obligations. |
| Utility Billing Platform (§19, unprocessed) | counterparty billing | the utility bills its customers; this Type consumes/validates those bills on the customer side (bill auditing, cost analysis, payment). |
| Demand Response Platform / Energy Forecasting Platform / Virtual Power Plant (§19) | adjacent machinery | grid-event participation, forecasting, and flexibility aggregation are capabilities/adjacent Types; not this Type's center. |
| Utility Bill Management (no directory leaf) | capability pole | bill processing/audit/pay services exist as a pole inside this Type (EnergyCAP Bill Capture/Pay; Arcadia UEM), same handling as the BEM pass recorded. |

Removal tests (summary): remove carbon → energy management (BEM family); remove the energy-data engine → carbon accounting; remove the managed loop → data repository; add the managed plan object as center → decarbonization planning; center wider resources → resource efficiency; center the grid → EMS/DR; center the customer-of-one → customer energy management.

## Uncertainties

1. All evidence this pass is Tier 2 (official product/marketing pages). Help-center depth was not fetched this pass; operational internals (validation rule specifics, workflow states, permissions) are stated at moderate strength only.
2. Schneider Resource Advisor — the most explicitly branded "energy and carbon management" product — unreachable (403, two passes). Its pole is evidenced only through the market's naming and the sampled suite products.
3. The ENGIE Impact heritage (30+ years) is vendor-framed on Arcadia's pages; the managed-service pole rests on Arcadia's combined pages alone this pass.
4. Whether a standalone pure-play "energy & carbon" product exists outside suite/bill-led/service poles is unverified; the sampled carriers all bundle additional families (ESG modules, bill services, advisory).
5. MRI observations are carried over from the BEM pass (its own pages fetched there); not re-fetched here.
6. Vendor numeric claims (payments processed, meters managed, sites benchmarked, savings figures) are marketing figures recorded in these notes only; none promoted.

## Flag Discharge (decarbonization-planning-platform joint review)

The flag recorded by the decarbonization pass is **discharged from this side**: keep-both ratified.

- The program-object test was applied: across the sampled products, the energy/carbon data-operations layer (utility bills, interval data, validation, variance/normalization, energy cost management) is the center; the managed reduction program (plan artifact + levers + tracked delivery) appears only as separate modules (Envizi Decarbonization family) or advisory services (Arcadia carbon strategy). Target tracking on energy/carbon KPIs is common in this Type and does not constitute the program object.
- The decarbonization pass's proposed seam ("energy/carbon data-operations layer vs managed reduction program") is confirmed by direct observation.
- Secondary adjacency stands: the enterprise-suite pole blends the two (Envizi ships both under one spine) — a center-of-gravity seam, not a contradiction.

## Final Synthesis

Energy & Carbon Management software is the energy-buying organization's system of record for its energy data and the carbon derived from it. Its world: the organization's estate held as sites/accounts, with utility bills and meter readings captured, consolidated, and validated as durable records carrying consumption and cost; carbon emissions computed and maintained on that same foundation as a managed, reportable output; and a managed performance loop that normalizes, compares, and tracks the data into outcomes — verified savings against adjusted baselines, resolved billing errors, benchmark and compliance status, targets, and energy & carbon reporting for corporate and disclosure audiences. The defining core is small (energy data of record + carbon on the same foundation + the managed performance loop); interval analytics, normalization machinery, benchmarking regimes, cost/chargeback machinery, ingestion fabric, and reporting outputs are the common mature structure; delivery posture (software-led vs managed-service), transaction layers (payment, procurement, rebates), carbon scope breadth, extended resources, and regional regimes are variants. The Type is bounded against carbon accounting (energy-data engine vs all-scopes inventory of record), building energy management (enterprise estate + carbon co-equal vs building operations), decarbonization planning (data-operations layer vs managed program — program-object test applied and discharged), ESG suites (center of gravity), customer-side and utility-side energy Types (operator seat), and resource-efficiency management (extended-resource center).
