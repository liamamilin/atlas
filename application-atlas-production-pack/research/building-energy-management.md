# Research Notes — Building Energy Management

## Research Goal

Understand what "Building Energy Management" software actually is as an Application Type: what objects it manages, where its data comes from, what workflow it drives (measure → analyze → act → report?), who uses it, and where its boundary lies against neighboring Types — especially Building Management System / BMS (§17), IWMS / Facility Management System (§17), Energy Management System / EMS (§19, utility/grid domain), Demand Response Platform (§19), Customer Energy Management (§19), and Energy & Carbon Management (§21).

## Initial Boundary

Initial hypothesis: Building Energy Management (BEM; market terms: energy management software, energy monitoring & targeting, building energy analytics) is software that turns building energy consumption into managed data: it ingests consumption/cost data (utility bills, meters, submeters, BMS feeds), analyzes it (benchmarking, normalization, anomaly detection), drives action (identify waste, verify savings, optimize operation), and reports performance (energy, cost, carbon) over a building portfolio.

Expected hardest boundary: vs BMS/BAS. BMS controls plant in real time (sensors/controllers/actuators); BEM analyzes energy over time. Many BEM products read BMS data; some write back optimization — this "control creep" is the key thing to test.

Expected drift risks: (a) toward sustainability/carbon suites (ESG reporting), (b) toward utility-bill processing services (bill pay), (c) toward demand response/grid services, (d) toward equipment fault detection (FDD) as a standalone discipline.

## Research Questions

1. What are the core objects (buildings/sites, meters, bills, accounts, cost centers, channels, readings)?
2. Where does consumption data come from (bills, interval meters, BMS/BAS, IoT, manual entry) and how is it modeled?
3. What is the defining analysis loop (benchmark, normalize, compare, detect anomalies) and the action loop (alerts, work orders, optimization, M&V)?
4. How are cost and finance handled (bill audit, budgets, accruals, chargebacks, tenant billing) — core or variant?
5. How does savings verification work (baselines, weather normalization, cost avoidance, IPMVP-style M&V)?
6. Do products *control* equipment, or only measure/analyze? Where is the BMS seam?
7. What roles use it (energy manager, facility staff, finance, sustainability officer, service providers/ESCOs)?
8. What reporting/compliance outputs exist (energy reports, GHG/carbon, benchmarking regimes)?
9. What are the poles of the market (bill-accounting-led vs interval-analytics-led vs control-led vs suite-embedded)?
10. Historical check: would bill-only, pre-interval energy accounting (1980s–90s heritage) and regional M&T traditions fit the definition?

## Representative Products

| Product | Geography | Philosophy / pole | Customer tier | Evidence level |
|---|---|---|---|---|
| EnergyCAP | US (PA; Dublin office) | Utility-bill/energy accounting led: bills + interval data + finance + M&V; "energy and utility management platform" | Higher ed, government, K-12, healthcare, enterprise portfolios ("26,000 energy and utility professionals" claim) | Tier 1 (help center) + Tier 2 (product pages) |
| SkyFoundry SkySpark | US | Analytics-native: Haystack-tagged building/equipment data + automated analytics ("Find What Matters"), deployable edge-to-cloud | Integrators, FM/Cx service providers, enterprises ("15,000+ buildings", "1B+ sq ft" claims) | Tier 2 (detailed product pages) |
| GridPoint | US | Equipment-level control & optimization for multi-site chains; both sides of the meter (buildings + grid services) | Retail/convenience/food-service chains (many small sites) | Tier 2 (marketing/product pages only) |
| MRI Energy (eSight Energy heritage) | UK/US (MRI is global) | Suite-embedded energy management inside a real-estate software vendor; acquired eSight 2021 | Real estate portfolios, universities, telecom ("65,000 sites monitored" claim), ESCos | Tier 2 (product page + vendor FAQ) |

Unreachable candidates (see Sources): Schneider Electric EcoStruxure Resource Advisor (se.com 403 ×2), Lucid BuildingOS (lucidconnect.com 403 + 404). Recorded as source-access limitations; no claims made for them.

Peer-set confirmation: EnergyCAP positions across "energy managers / sustainability leaders / finance leaders"; MRI's FAQ gives a vendor-authored definition of the category; GridPoint and SkySpark mark the control-led and analytics-led poles respectively.

## Sources

All fetched 2026-09-06:

- EnergyCAP Help Center (Tier 1) — https://helpcenter.energycap.com/ (module index) and https://helpcenter.energycap.com/um/overviews/overview_of_everything ("EnergyCAP overview": Sites/Meters/Accounts/Bills/Interval data/Vendors & rate schedules/Users; two hierarchies; enter/verify data) — fetched successfully
- EnergyCAP Help Center — https://helpcenter.energycap.com/um/sa/interval_data_overview ("Interval Data overview": source/computed/summarized readings; interval-vs-bill table; use cases; meter status/data completeness; Trend Insights) — fetched successfully
- EnergyCAP product pages (Tier 2) — https://www.energycap.com/ (product family: Utility Management, Smart Analytics/Interval Data, Carbon Hub, Bill Capture, Bill Pay, Watts AI; features incl. chargebacks, accounting, BI reporting, auditing, benchmarking, ENERGY STAR, M&V), https://www.energycap.com/utility-bill-energy-management-software/ , https://www.energycap.com/energy-monitoring-software/features/ipmvp-energy-measurement-energy-verification/ (IPMVP Options B/C, baselines, routine adjustments, cost avoidance; ESCO/energy-performance-contract framing)
- SkyFoundry (Tier 2) — https://www.skyfoundry.com/ and https://www.skyfoundry.com/product (Collect/Store/Organize/Analyze/Visualize/Workflow/Report/Export/Distributed/Embeddable; Folio historian; Project Haystack tagging; Axon engine; 500+ functions; Spark/KPI/Energy/Historian/Weather/Rule apps; Arc workflow engine "identification to resolution"; Haystack REST API; on-prem/cloud/edge/desktop deployment)
- GridPoint (Tier 2) — https://www.gridpoint.com/ (positioning; data from "HVACs to refrigerators to lights"; GridPoint Intelligence automation; anomaly detection; HVAC health monitoring; advanced scheduling; solutions: Energy Efficiency, Operational Efficiency, Demand Management, Sustainability, Grid Services; industries: food & beverage, retail & convenience, auto/transportation)
- MRI Energy (Tier 2) — https://www.esightenergy.com/ (redirects to https://www.mrisoftware.com/products/energy-management-software/) — product page + vendor FAQ (definition of energy management software; dashboards; data collection/consolidation; carbon & sustainability tracking; tenant billing; alerts & anomaly detection; compliance: GHG Protocol/ISO 50001; data sources: IoT, BMS, oBIX, Modbus TCP/IP, OPC HDA via local iDC service); eSight acquisition news link (Nov 2021)

Failed fetches (source-access limitations):

- Schneider Electric EcoStruxure Resource Advisor — https://www.se.com/ww/en/... and https://www.se.com/us/en/... — HTTP 403 twice. Abandoned per retry rule; enterprise-suite pole under-documented here.
- Lucid BuildingOS — https://lucidconnect.com/ (403), https://www.lucidconnect.com/products (404). Abandoned; engagement/higher-ed pole under-documented here.

No help-center article bodies beyond EnergyCAP's were fetched; no numeric limits, default values, or pricing are asserted in the final document beyond vendor-public marketing stats (kept as claims in these notes only).

## Product A — EnergyCAP

### Key observations (Layer A unless noted)

- Self-definition (help center overview): "an energy and utility management platform that helps organizations track, analyze, and reduce their energy use and costs. It centralizes utility bill data, interval meter readings, and energy performance metrics—giving energy managers, facility teams, and finance staff a single source of truth for all their utility data."
- **Core objects**: Sites, Meters, Accounts, Utility bills, Interval data, Vendors and rate schedules, Users.
- **Two hierarchies over the same data** — "facilities view" (organizations → sites → meters; physical layout; used by building operations / energy management staff) and "accounting view" (accounts → cost centers; used by finance to review allocated costs). Stated rationale: use tracking assigned to physical locations doesn't change when financial grouping changes; meters stay constant even when vendor changes.
- **Data entry paths**: Bill Capture (automated processing), spreadsheets, manual entry, chargebacks. "Your data, including bills, stays in EnergyCAP indefinitely unless you remove it."
- **Verification**: Bill Audits (flagged items) + Reports.
- **Interval data** (add-on module; legacy "Smart Analytics", formerly Wattics): readings at 15-min/hour (or finer) intervals vs monthly bill totals; three reading types (source / computed / summarized); used for reports, "Powerviews", Trend Insights, dashboard widgets; uncovers operational inefficiencies, overnight/weekend waste, peak-demand issues, equipment running outside scheduled hours, unexpected spikes; supports tenant billing/chargebacks; collected from meters, submeters, files, APIs; monitor & alert on abnormal readings/data gaps; backfill missing data.
- Interval-vs-bill framing (help center table): bills = monthly totals, cost reporting/budgeting, "what you spent"; interval = time-based detail, operational analysis/demand management, "when and how energy was used". Both together = complete picture.
- **Finance side**: accounts/cost centers, bill accruals & budgets, accounting export, chargebacks & tenant rebilling, bill pay services.
- **Benchmarking**: facility benchmarking feature; ENERGY STAR integration (US benchmarking regime).
- **M&V (IPMVP)**: standardize energy-conservation projects per International Performance Measurement and Verification Protocol; create M&V projects with Option B (single measure, e.g. lighting retrofit) or Option C (whole building, multiple systemic improvements); specify conservation measures, set baseline and reporting period, include routine adjustments (e.g. weather); visualize savings; "cost avoidance calculations"; used with energy performance contracts and ESCO partners.
- **Emissions**: Carbon Hub module — "financial-grade scope emissions data" derived from the same utility data.
- **AI**: Watts AI / Watts chat — "turn your utility data into clear answers"; supports bill data capture, error detection, insights.
- Marketing stats (claims only): 3x value vs cost, 3% average bill savings, 26,000 professionals, "40+ years" heritage.
- API: developer.energycap.com; legacy Smart Analytics API (Wattics).

## Product B — SkyFoundry SkySpark

### Key observations

- Positioning: "a comprehensive software platform for connecting, storing, analyzing and visualizing data from smart devices and equipment systems"; "Find What Matters"; proven across verticals (intelligent buildings, industrial, agriculture, energy, government, healthcare); claims 15,000+ buildings / 1B+ sq ft.
- **Collect**: live links to automation systems (BAS) and smart meters, SQL databases, Excel/historical imports, utility web-service feeds.
- **Store**: Folio — high-performance historian + document/graph modeling for IoT data; billions of time-series records.
- **Organize**: Project Haystack semantic tagging — "unified models of your buildings, equipment, devices and sensors". (The building/equipment data model is explicit and first-class.)
- **Analyze**: Axon rule engine; 500+ built-in analytic functions; automatically generates visualizations, notifications, and reports showing issue, time, duration, frequency, **cost**.
- **Apps**: Spark (issues as timelines/bubbles/charts), KPI (candle charts), **Energy App** — "a comprehensive suite for analysis of energy resources including electrical demand, consumption, cost, water and gas usage", Historian, Weather (forecasts + historical weather applied to rules), Rule (custom rules → sparks).
- **Workflow**: Arc application — bundled workflow engine "to track work orders using the process best fit to your own organization"; explicit "identification to resolution" framing.
- **Report**: any view is a report (PDF, SVG, PNG, Excel); open Haystack REST API for export/integration.
- **Deployment**: on-premise, cloud, edge, desktop; distributed clustering (Arcbeam); OEM-embeddable down to small hardware.
- Note: SkySpark is broader than energy (fault detection, equipment analytics generally) but the Energy App + KPI + cost-on-sparks make building energy one of its primary uses; it anchors the analytics-led pole and the FDD overlap.

## Product C — GridPoint

### Key observations

- Positioning: "We use intelligent software to analyze data from HVACs to refrigerators to lights – pinpointing inefficiencies to help you save energy, save money, be more sustainable, and help the grid."
- "A single, unified platform that connects both sides of the meter" — serves businesses and utilities; grid-interactive buildings; demand management.
- Data: "real-time granular equipment level information, building performance, historical data, and utility grid status."
- **GridPoint Intelligence**: "interprets a high volume of data points and automates building operations to be most efficient" — i.e., closed-loop control/automation, not just dashboards.
- **Automated anomaly detection**: detects anomalies, identifies inefficiencies, makes recommendations.
- **HVAC health monitoring**: monitors/tests units enterprise-wide; facility managers identify/diagnose issues, troubleshoot remotely, prioritize by severity, validate repairs (energy platform overlapping equipment maintenance workflow).
- **HVAC advanced scheduling**: automation based on time-of-use schedules, hours, occupancy, sensors, daylight; "avoiding peak charges".
- Solutions nav: Energy Efficiency, Operational Efficiency, Demand Management, Sustainability, Grid Services.
- Industries: food & beverage, retail & convenience, auto/transportation — the many-small-sites chain pole.
- Marketing stats (claims): $1.5B energy savings, 10.6B+ kWh reduced, 18.5B+ lbs CO2 avoided.

## Product D — MRI Energy (eSight Energy heritage)

### Key observations

- Positioning: "Cut energy waste and control surging costs… total visibility across your portfolio." Sold inside MRI Software's real-estate suite (Facilities Management, IWMS, commercial property siblings).
- Vendor FAQ (useful vendor-authored definition of the category, Layer A for this vendor): "Energy management software is an automated system that collects data on energy usage and compiles it into a user-friendly application for further analysis and reporting. It's used by energy, facilities, and sustainability managers to better manage energy consumption and environmental footprint, … improve energy-related decision making and facility performance, and decrease operating costs while meeting compliance standards."
- Key features per vendor: **data collection** (centralize energy-related data "from any source, system, or format"), **energy analysis** (unified view to identify savings, drive accountability), **anomaly detection** (alerts on readings outside tolerated levels), **tenant billing** (automate billing for tenant utility usage; validate invoices against energy usage), **regulatory compliance / sustainability** (GHG Protocol, Net Zero, ISO 50001 reporting; carbon baselines).
- Data sources: IoT devices, BMS, oBIX-enabled devices, file-folder imports, Modbus TCP/IP, OPC HDA via a locally installed "MRI Energy iDC" service.
- Modules surfaced on product page: Energy dashboards (usage/trends, sustainability goals, site comparison); Energy data management (capture/consolidate/standardize); Carbon & sustainability tracking; Tenant billing; Alerts & anomaly detection.
- Customer quotes (evidence of usage patterns): monitor usage by building across campus and identify utility problems; "campus stakeholders can now see the energy impacts of their actions in near real-time"; configurable analysis templates + data quality tools; global use "based on collected data from a large number of remote building and plant management systems."
- Marketing stats (claims): $3.5M saved by a university; $2B saved by an ESCo's customers; 193% ROI year one; 65,000 sites monitored.
- Lineage: eSight Energy acquired by MRI Software (Nov 2021, per news link on the product page) — evidence that BEM exists both as standalone and as suite module. (eSight's pre-acquisition positioning is industry context; not evidenced on fetched pages.)

## Cross-product Comparison

| Dimension | EnergyCAP | SkySpark | GridPoint | MRI Energy (eSight) |
|---|---|---|---|---|
| Central managed substance | Utility bills + interval readings tied to site/meter records | Time-series data on Haystack-tagged building/equipment/device model | Equipment-level real-time data (HVAC, refrigeration, lighting) + building performance + grid status | Consumption data consolidated from bills, meters, BMS, IoT "from any source" |
| Building/portfolio structure | Organizations → sites → meters tree; separate accounts/cost-centers tree | Sites with unified building/equipment/sensor models | Fleet of small sites (stores) as replicable units | Portfolio of buildings/sites (real-estate shaped) |
| Primary analysis | Bill analysis, benchmarking (incl. ENERGY STAR), cost avoidance, M&V, interval pattern analysis | Automated rules → "Sparks" (issues with time/duration/frequency/cost); KPIs; energy demand/consumption/cost/water/gas | Anomaly detection, recommendations, automated optimization of schedules/setpoints | Analysis templates, dashboards, anomaly alerts, data quality tools |
| Action loop | Bill audit → flagged items → resolution; M&V projects; (control not observed) | Arc workflow: identification → resolution, work orders | Automated equipment control; remote troubleshooting; repair validation | Alerts → investigate/act; (control not observed) |
| Cost/finance layer | Deep: accounts, accruals, budgets, chargebacks/tenant rebilling, bill pay | Cost surfaced on issues; no finance suite | Savings-driven; peak-charge avoidance | Tenant billing, invoice validation |
| Reporting surface | Reports, dashboards, emissions module, BI reporting | Any-view-reports; KPI charts | Savings/sustainability reporting | Dashboards, compliance reports (GHG Protocol, ISO 50001) |
| Reads BMS/BAS | Via interval-data feeds (meters/submeters/files/APIs) | Yes — live links to automation systems (primary source) | Yes — equipment-level data primary | Yes — BMS, oBIX, Modbus, OPC |
| Writes control | Not observed | Not observed (analytics/notifications only on fetched pages) | Yes — automated building operations (its differentiator) | Not observed |
| Roles | Energy managers, facility teams, finance staff; sustainability leaders | Integrators/service providers configuring analytics; facility teams | Facility managers of chain sites; energy advisors | Energy/facilities/sustainability managers; campus stakeholders |
| Delivery | SaaS (+AI add-on) | On-prem/cloud/edge/desktop; OEM-embeddable | Managed platform + grid services | Suite module (cloud) |
| Customer tier | Large institutional portfolios (higher ed, government) | Integrator/service-provider-led deployments; enterprises | Multi-site chains (retail/QSR/convenience) | Real estate portfolios, campuses, global enterprises |

Stable commonalities (Layer B across all four):

1. Buildings/sites held as identified entities in a portfolio structure.
2. Energy consumption captured as data over time against those entities — either bill records, metered readings (interval), or equipment-level feeds.
3. Comparative/automated analysis over that data whose purpose is exposing waste, anomalies, peaks, and savings opportunities.
4. Performance made visible and actionable: dashboards/reports, alerts, and tracked outcomes (savings, issues, verified results).

Poles: bill/accounting-led (EnergyCAP) ↔ analytics-led (SkySpark) ↔ control-led (GridPoint) ↔ suite-embedded (MRI). All satisfy the common core above.

## Canonical Model

### L0 — Defining Invariant

The smallest structure without which the software stops being recognizable as Building Energy Management:

1. **Buildings as identified monitored entities** — sites/buildings exist as records (a portfolio structure, from one building to thousands).
2. **Consumption recorded over time against those buildings** — energy use enters the system as durable consumption records: utility bill records and/or metered readings (interval or aggregate), associated with the building and its meters. This consumption data is the substance everything else operates on.
3. **Comparative analysis that surfaces waste and opportunities** — the system analyzes consumption across time, across buildings, and against expectations (baselines, schedules, norms) to expose waste, anomalies, peaks, and savings opportunities. A passive data store with no analysis is not energy *management*.
4. **Energy performance made visible and reportable over time** — dashboards/reports and tracked results (savings, issues, verified outcomes) so the organization can manage energy as a managed discipline.

Remove the buildings → generic energy data platform (utility/grid analytics). Remove consumption records → property/FM software with nothing to manage. Remove analysis → a meter-data logger or bill repository. Remove performance visibility/reporting → a private historian, not a management tool. Add real-time control loops as the primary purpose → BMS/BAS.

### L1 — Common Mature Structure

- **Meter/submeter hierarchy with channels and units** under each site; meter identity kept stable across vendors.
- **Utility bill management**: bill capture (automated/manual/spreadsheet), bill audit with flagged items, rate schedules/vendors, cost reporting, accruals/budgets, accounting export.
- **Benchmarking** across buildings (and external regimes such as ENERGY STAR in the US).
- **Weather/degree-day normalization and baselines** for fair comparison over time.
- **Interval-data analytics**: load profiles, weekday/weekend patterns, peak demand, equipment running outside schedules; data-quality monitoring (gaps, backfill) and alerts.
- **Anomaly detection and alerting** on consumption above expected thresholds.
- **Targets, budgets, and cost tracking**; **measurement & verification of conservation measures** (baseline vs reporting period, routine adjustments, cost avoidance — IPMVP-style in mature products).
- **Dashboards and standard/scheduled reports** (energy, cost, demand; increasingly carbon/GHG derived from the same data).
- **Integration fabric**: BMS/BAS, meters/submeters, IoT sensors, file/API imports; open APIs.
- **Role-scoped access** spanning energy/facility users and finance users; multi-site portfolio hierarchies.
- **Action tracking**: alerts/issues carried to resolution (work orders or audit items).

### L2 — Variant / Optional Structure

- **Control/optimization posture** (control-led pole): automated equipment scheduling, setpoint optimization, peak-charge avoidance, demand curtailment (GridPoint). Blurs toward BMS/DR; most BEM products only read.
- **Grid services / demand-response participation** (GridPoint; adjacent to Demand Response Platform).
- **FDD depth** (analytics-led pole): equipment-level fault detection & diagnostics as a first-class discipline (SkySpark's general analytics).
- **Sustainability/carbon depth**: dedicated emissions modules with scope-level accounting (EnergyCAP Carbon Hub; MRI carbon tracking) — overlaps Energy & Carbon Management (§21).
- **Tenant billing / chargebacks depth** (EnergyCAP chargebacks; MRI tenant billing).
- **Compliance regimes**: ENERGY STAR benchmarking (US), ISO 50001 / GHG Protocol reporting (vendor-stated), regional energy-audit regimes (EU/UK traditions in eSight lineage) — regime depth varies by geography.
- **Engagement surfaces**: building/campus dashboards exposed to non-energy stakeholders (MRI campus quote; the higher-ed engagement tradition — Lucid's pole — under-documented here).
- **ESCo / energy-performance-contract support** (EnergyCAP M&V framing).
- **Delivery posture**: SaaS vs on-prem/edge (SkySpark) vs suite module (MRI) vs managed service (GridPoint).
- **Segment tunings**: institutional portfolios (higher ed/government), commercial real estate, multi-site chains, industrial sites.

### L3 — Vendor-specific (kept out of final document)

- EnergyCAP: Watts AI/Watts chat; Bill Capture/Bill Pay services; dual-hierarchy (sites/meters vs accounts/cost centers) as product architecture; source/computed/summarized reading pipeline; data-completeness thresholds (Good >95%, Fair 85–95%, Poor ≤85%, Insufficient <30 days — vendor defaults); "Powerviews", Trend Insights; Carbon Hub; developer API + Wattics legacy API; marketing stats (3x ROI, 3% bill savings, 26k professionals, 40+ years).
- SkySpark: Folio historian; Axon engine; Project Haystack tagging; 500+ function library; Spark/KPI/Energy/Historian/Weather/Rule app names; Arc workflow; Everywhere/Arcbeam clustering; OEM/edge/Raspberry-Pi-class deployment; claims (15k+ buildings, 1B+ sq ft, Frost & Sullivan award).
- GridPoint: GridPoint Intelligence; HVAC health monitoring; both-sides-of-the-meter framing; store-chain industries; pilot-program motion; claims ($1.5B savings, 10.6B kWh, 18.5B lbs CO2).
- MRI Energy: eSight acquisition lineage; iDC local service (Modbus TCP/IP, OPC HDA, oBIX); suite siblings (Facilities, Footfall, IWMS); claims ($3.5M university, $2B ESCo customers, 193% ROI, 65,000 sites).
- Schneider Resource Advisor, Lucid BuildingOS: candidates with inaccessible documentation — no vendor detail recorded beyond market existence.

## Boundary Findings

- **vs Building Management System / BMS (§17)** — the sharpest seam. BMS is the real-time control system of the building (sensors, controllers, actuators, HVAC/lighting loops). BEM is measurement, analysis, and management of energy over time. Evidence of the seam: MRI lists "BMS" as a *data source* for energy software; SkySpark collects from "an automation system or smart meter"; GridPoint is the control-creep pole (automates operations) and even there the pitch is energy outcomes. Test: remove analysis/reporting and make control loops primary → BMS. Keep measurement/analysis and only read BMS → BEM.
- **vs Facility Management System / IWMS (§17)** — FM/IWMS centers on space, maintenance, work orders, leases, real-estate operations; energy is one module (MRI ships Energy as a separate product beside Facilities/IWMS). Remove consumption data as the substance → FM/IWMS.
- **vs Energy Management System / EMS (§19)** — naming collision, different domain: §19 EMS is utility/grid-side (generation/transmission control, SCADA lineage). The directory keeps both; building scope (buildings/meters/bills, portfolio users) is the discriminator. Remove buildings, add grid assets → EMS (§19).
- **vs Demand Response Platform (§19)** — DR centers event-based curtailment participation in grid programs; BEM may *participate* (GridPoint's Demand Management/Grid Services) as a variant. Center on event dispatch/market participation → DR Platform.
- **vs Customer Energy Management (§19)** — consumer/home pole of energy data; BEM's users are organizations managing buildings. 
- **vs Energy & Carbon Management (§21)** — §21 centers organization-wide carbon/ESG accounting and decarbonization planning; BEM centers building consumption data and operational energy. Overlap: carbon from energy data (emissions modules). Center on enterprise carbon/ESG disclosure across all scopes → Energy & Carbon Management.
- **vs Building Condition Assessment / Building Asset Management (§17)** — condition/asset records vs consumption performance. (Prior siblings documented.)
- **vs Utility Bill Management** (no directory leaf) — bill processing/pay services exist as a pole inside BEM (EnergyCAP Bill Capture/Pay) and as standalone markets; recorded as a capability pole, not a separate Type here.
- **vs Building Analytics / FDD** (no directory leaf) — analytics-led BEM (SkySpark) extends into equipment FDD; FDD-first products are the same pole. Recorded as overlap, not boundary failure.
- **"去掉什么就变成另一个 Type" 判据**: remove buildings → utility/grid energy analytics; remove consumption records → FM/property; remove analysis → meter-data logger/bill repository; make real-time control primary → BMS; center on grid events → Demand Response; center on enterprise-wide carbon → Energy & Carbon Management (§21).

## Historical / Market-Sample Check (§24)

- **Pre-interval era**: 1980s–90s energy accounting ran on utility bills entered/spreadsheeted per building, with benchmarking and cost-avoidance math. EnergyCAP self-describes "40+ years of energy excellence"; its help center still treats bills as the primary record and interval as an add-on. Bill-only products satisfy the L0 (consumption records = bill records; analysis = bill-based benchmarking/normalization). ✔
- **UK/European M&T tradition** (monitoring & targeting): meter/bill data + degree-day normalization + variance reporting — fits the same core. Note: the "M&T heritage" characterization of eSight is industry context, not evidenced on the fetched MRI pages; the fetched evidence supports only the acquisition and the product's current positioning. ✔
- **Analytics-era products** (SkySpark) shift the substance from bills to interval/equipment time-series but keep the same loop (data → analysis → surfaced issues → resolution → reporting). ✔
- **Control-era products** (GridPoint) add automated optimization — classified as variant posture (control pole), not a redefinition, because the analysis/reporting core remains and the control pole still consumes/analyzes the same energy data. ✔
- No era- or region-specific implementation (interval data, ENERGY STAR, GHG scoping, IoT sensors) is required by the definition.

## Uncertainties

- Schneider (Resource Advisor) and Lucid (BuildingOS) documentation was unreachable (403/404) — the enterprise-sustainability-suite pole and the occupant-engagement pole are under-documented; their inclusion as variants is based on the reachable sample's edges (EnergyCAP emissions module; MRI campus-stakeholder quote) rather than direct product evidence.
- GridPoint and MRI evidence is Tier-2 (product pages + FAQ); operational depth (exact workflows, alert configuration, permission models) not verified against help centers.
- The exact market boundary between BEM and standalone FDD platforms, and between BEM and pure utility-bill-management services, is a continuum; no directory leaves exist for those, so both were handled as capability poles within this Type.
- Whether "control-led" products (GridPoint) should eventually split from BEM (toward BMS/grid-flexibility Types) is left as a joint-review observation; the current directory has no leaf for "building energy optimization/control software".
- No pricing, numeric limits, or default values asserted in the final document; all vendor stats kept as claims in these notes only.

## Final Synthesis

Building Energy Management software turns building energy consumption into a managed, analyzable, reportable asset. Its world is built from buildings/sites held as identified records, with energy consumption entering as durable records — utility bills and/or metered readings — against those buildings and their meters. The defining loop is comparative analysis over that consumption (across time, across buildings, against baselines and schedules) that surfaces waste, anomalies, peaks, and savings opportunities, made visible through dashboards, reports, and alerts and closed by tracked outcomes: audited bills, resolved issues, verified savings (baseline-and-adjustment measurement & verification), and increasingly derived carbon reporting. Mature products add meter hierarchies, bill management and finance integration (budgets, accruals, chargebacks, tenant billing), benchmarking regimes, interval-data analytics with data-quality monitoring, BMS/meter/IoT integration, and role-scoped access across energy, facility, and finance users. The market has four poles — bill/accounting-led (EnergyCAP), analytics-led (SkySpark), control-led (GridPoint), suite-embedded (MRI Energy / eSight) — all sharing the same core. The sharpest boundary is against Building Management Systems (measure/analyze/report vs real-time control), with further seams to FM/IWMS (operations vs consumption data), §19 utility EMS and Demand Response (grid domain vs building domain), and §21 Energy & Carbon Management (enterprise carbon vs building consumption).
