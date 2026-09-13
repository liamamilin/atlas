# Research Notes — Renewable Energy Asset Management

Research date: 2026-09-09

## Research Goal

Understand what "Renewable Energy Asset Management" is as an Application Type: what the market actually sells under renewable asset-management vocabulary, what the system holds, who operates it, how the production–availability–reporting loop works, and — critically, because of the joint-review flag from the sibling power-plant-management pass — whether this leaf is a distinct Type, an asset-population variant of Power Plant Management, or a seat-defined sibling sharing that pass's four-leg generation-management spine.

## Initial Boundary

- The leaf sits in §19 between Power Plant Management (processed 2026-09-09, joint-review flag on this leaf) and the sibling renewable leaves Solar / Wind / Battery Energy Storage Asset Management (unprocessed).
- The power-plant-management pass recorded: its four-leg core (generation asset population · production vs expectation · availability record & restoration · accounting & compliance) spans traditional AND renewable populations (AspenTech GMS "traditional and renewable generation"; Power Factors' renewable suite holds the same production/availability/accounting core); its recorded test is "remove the renewable-asset specialization → this Type"; its counter-possibility is that the renewable leaves carry deeper portfolio/commercial machinery (Power Factors' commercial asset management / invoice layer) that would ratify a separate Type.
- Neighbors named in the directory: Energy Forecasting Platform, Energy Trading Platform, Energy Scheduling & Settlement, SCADA, DERMS, Virtual Power Plant Platform, Renewable Energy Certificate Management, Enterprise Asset Management/CMMS.

## Research Questions

1. What does a renewable asset management system hold as its system of record? (portfolio, plants, assets, contracts?)
2. What is the "expectation" side of production for weather-driven assets, and who/what generates it?
3. How is availability defined, computed, and used — especially against O&M providers, OEMs and contracts?
4. What money resolution exists (invoicing, budgets, investor reporting) and is it core or pole-specific?
5. Who is the seat — plant/dispatch operations (power-plant-management's seat) or owner-side asset management?
6. What machinery is renewable-distinct vs shared with the generation-management spine?
7. What are the seams vs SCADA, CMMS/FSM, forecasting, trading/settlement, DERMS/VPP, REC management?
8. Does the market's own vocabulary (TAM/CAM split, "asset management", "performance management") reveal the Type's internal structure?

## Representative Products

| Product | Vendor | Philosophy / pole | Customer tier | Docs quality |
|---|---|---|---|---|
| Unity suite (Monitoring & Control: SCADA/PPC/EMS; Technical Asset Management: APM/Advanced Insights/FSM; Commercial Asset Management: Asset Oversight/Invoice Management) | Power Factors | full-suite owner/operator platform, control → TAM → CAM | utility-scale IPPs, asset managers (Repsol, EDF Renewables, BP, Lightsource bp, Arevon, Origis…) | excellent (homepage + CAM page + APM page via sibling pass) |
| Bazefield | Bazefield AS (Norway) | owner's operating platform: monitoring + analysis + operations management, multi-vendor SCADA integration | wind/solar/hydro owners & operators (Invenergy Services, SSE Renewables, W3 Energy, TruBoard India) | good (product page with per-application detail) |
| PowerTrack | AlsoEnergy (Stem) | monitoring-led clean energy portfolio management, edge-to-cloud, controls as sibling product | utility, C&I, aggregated residential solar+storage (200,000+ sites, 25+ GW) | good (homepage + PowerTrack page) |
| Clir (Portfolio / Enhance / Associate) | Clir Renewables | investor/asset-manager analytics: reporting, contractual availability reconciliation, budget/reforecast | infrastructure funds, investment managers, asset managers (350+ GW wind/solar/BESS) | good (homepage with named capability blocks) |

Selection rationale: market representation (category leader + independent platform + #1-ranked solar monitoring vendor + investor-analytics pole), different product philosophies (full suite / operator platform / monitoring-led / analytics-led), different customer tiers (IPP suite buyers, operators, distributed portfolios, funds), reachable official documentation. Probes that failed or were abandoned: 3megawatt (Blade) — 3megawatt.com now redirects to powerfactors.com (vendor consolidated into Power Factors; not independent evidence); PowerHub — powerhub.app domain is for sale (product not verifiable); DNV — software page is a generic digital-solutions estate, no renewable-AM platform product page reachable.

## Sources

- Power Factors — homepage (self-label "Renewable Energy Management Software"; Unity suite decomposition Monitoring & Control / Technical Asset Management / Commercial Asset Management): https://powerfactors.com/
- Power Factors — Unity Commercial Asset Management page (Asset Oversight + Invoice Management detail): https://www.powerfactors.com/unity/commercial-asset-management
- Power Factors — Unity Asset Performance Management page (fetched by the sibling power-plant-management pass, quoted in its research notes): https://www.powerfactors.com/unity/asset-performance-management
- Bazefield — homepage ("the global market's fastest-growing and most comprehensive off-the-shelf renewable energy asset management system"; Invenergy/SSE/W3/TruBoard announcements): https://bazefield.com/
- Bazefield — product page (Monitoring / Analysis / Operations Management / interfacing): https://bazefield.com/product/
- AlsoEnergy — homepage ("clean energy portfolio management"; edge-to-cloud; segments; roles): https://www.alsoenergy.com/
- AlsoEnergy — PowerTrack page ("actual versus weather-adjusted energy production"; PowerTrack SCADA/PPC as siblings): https://home.alsoenergy.com/powertrack/
- Clir Renewables — homepage (investor-grade reporting, contractual availability reconciliation, budget reconciliation & reforecast, performance monitoring): https://www.clir.eco/
- Boundary probes: https://www.3megawatt.com/ (redirects to powerfactors.com), https://www.powerhub.app/ (domain for sale), https://www.dnv.com/software/ (generic estate)
- Sibling-pass context: research/power-plant-management.md and applications/power-plant-management.md (AspenTech OSI GMS pages quoted there)

## Product A — Power Factors Unity (full-suite pole)

Evidence layer A (directly observed on vendor pages) unless noted.

- Self-label: homepage title "Renewable Energy Management Software"; suite promise "Every megawatt optimized. Every decision backed by intelligence… Turn real-time data into faster decisions and better financial outcomes".
- Suite marketecture — three named pillars:
  - **Monitoring & Control**: SCADA ("Predictable delivery, global compliance"), Power Plant Controller ("Ensure compliance with grid and market demands"), Energy Management System ("Intelligent orchestration for market participation, real-time optimization, and grid support").
  - **Technical Asset Management**: Asset Performance Management ("Optimize asset availability and yield at scale with sophisticated monitoring, analysis, and intuitive workflows"), Advanced Insights, Field Service Management ("work order management, personnel scheduling, inventory management and maintenance KPIs").
  - **Commercial Asset Management**: Asset Oversight ("Portfolio-level view of assets to provide a comprehensive system of record and enable oversight of operations, service providers, and revenue") + Invoice Management ("Centralized and automated management of invoices to enable cashflow management, streamlined reporting, and accurate financial management").
- The vendor uses the industry's TAM/CAM division explicitly — "Technical Asset Management" and "Commercial Asset Management" are the two non-control pillar names.
- CAM page detail — Asset Oversight:
  - Portfolio management: "Oversee plants, contracts, and inventories in a single platform, configurable by user role"; "Centralized data hub for portfolio health"; "Plant-to-contract drilldowns"; "Components, spare parts, and warehouse inventory tracking".
  - Contract and compliance oversight: "Centralize contracts and automate compliance tasks"; "Automated recurring compliance workflows with reminders"; "Custom tagging and rule-based task generation"; "Audit-ready logs".
  - Risk and incident management: "Commercial event logging for incidents like outages, accidents, or curtailments"; "Revenue/energy loss impact calculations and related claim tagging"; "End-to-end warranty and insurance claim management"; "Transparent audit trails".
  - Reporting: "Drag-and-drop custom report builder"; "Scheduled PDF reports with notifications to stakeholders"; "KPI tracking".
- CAM page detail — Invoice Management:
  - "Automate invoicing using contract-linked rates and escalation schedules"; "Automated invoice generation using templates and multi-level location tax rules"; "Efficient recurring billing workflows".
  - "Monthly, quarterly, and annual financial statement generation"; "Budget vs. actual performance comparisons"; "Utility statement reconciliation against generation data"; "Portfolio-to-plant variance analysis".
  - "Bi-directional API integration with ERP and financial systems".
- CAM integrations (the suite's own seam map):
  - SCADA & production data: "Reconcile gross vs. net generation automatically by linking SCADA and monitoring inputs with financial workflows".
  - APM: "Tie asset performance insights directly to revenue and contract obligations for faster root-cause and financial impact analysis. Unity APM translates performance issues into commercial impact, helping teams protect availability, compliance, and revenue."
  - ERP & accounting: "Push invoices, settlements, and financial statements into ERP and accounting platforms via bi-directional APIs".
  - Compliance & regulatory systems: "Automate compliance workflows and generate audit-ready reports that align with regional and market standards".
  - OEM-agnostic compatibility: "Manage contracts, invoices, and compliance obligations across mixed fleets with diverse asset types and vendors".
- Customer voice (A): testimonials from renewable asset-management roles — "Director of Asset Management, Vesper Energy" ("manage contractual risks and build a high-performing clean energy portfolio"), "Senior Asset Manager, Strata Solar" (">$1 billion in our solar portfolio"), "Co-founder, Lodestar" ("understand the value of our assets and the financial impact of each decision").
- From the sibling pass's notes (context, layer A there): APM page carries expected-vs-actual availability/yield machinery, loss accounting, NERC-GADS-class compliance reporting, REMI AI ("trained on operational data from more than 310 GW of renewable energy assets"), 600+ customers.

## Product B — Bazefield (operator platform pole)

- Self-label (A): "the global market's fastest-growing and most comprehensive off-the-shelf renewable energy asset management system"; customer claim "Celebrating 30 GW of wind and solar managed"; technology claim "Solar, Wind and Hydro plants — all your data in one place".
- Product structure (A, product page) — three named layers:
  - **Monitoring**: portfolio overview ("monitor and visualize power plants across the entire portfolio, view production data, warnings, alarms and other key metrics in real-time"); power plant overview ("production values, availability measures, capacity factor or other user identified KPI's… substation mimics, met masts, forecasts"); assets overview ("typically used as a 'control room' function for everyday operation… identify and isolate the root cause for stopped and under-performing assets").
  - **Analysis**: power curve analyzer ("detect abnormalities or sudden unexpected changes in your power curves… compare power curves before and after an OEM software upgrade"); alarm statistics (frequency/duration, root-cause filters); trending ("regardless of where the data originates, and whether it is a measured value or a calculated value"); **availability analytics** ("generate your own availability calculations based upon your contractual categorization or based upon other measures such as IEC-61400… this provides you a much stronger negotiation position with your OEM in availability meetings"); 2D/3D plotter.
  - **Operations management**: weather forecasting ("a great tool especially when combined with the availability planner"); **availability planner** ("In order to have accurate Production Forecasting, you need to have control over availability planning (service, repair, substation or grid outage etc.)… manually schedule both corrective and planned maintenance, and it can be integrated to a maintenance system if required"); HSE and site activity ("planning and tracking service activities and personnel for sites and turbines… contacts and companies management including safe passes and site inductions, work orders, turbine controls and general site access tracking… handle and report on HSE related information").
- Interfacing (A): built-in turn-key support for turbine models "Vestas, Siemens, Senvion, Nordex, Gamesa, Enercon, GE"; integrations "transmission and substation, production metering, MET mast and LIDAR, weather forecast, power forecast, CMMS, ERP, document- and HSEQ systems"; data standards "OPC standard is mostly used… IEC 60870-5-101/104, FTP/files, historians like OsiSoft PI"; "The system data model are based on the IEC 61400-25 standard as default"; SDK with .NET and RESTful APIs.
- Positioning (A, intro video text): "a comprehensive, technology-agnostic software platform designed to reduce plant downtime, increase runtime efficiency, and strengthen users' negotiation power with vendors and suppliers alike. Through the implementation of a centralized, scalable data historian and smart, event-driven algorithms… This allows investors, asset managers, and operators for any type of renewable asset to focus their efforts on addressing root cause issues, as opposed to cleaning and manipulating data."
- Customer evidence (A, news): Invenergy Services — "a digital platform that will increase efficiency and improve customer experience for wind, solar, and storage asset owners… expected to top 25-gigawatts by 2025" ("Data-Driven Owner's Platform"); SSE Renewables — "onshore wind control room solution"; W3 Energy (Swedish O&M/operations company) — "implements the Bazefield operating system in the business"; TruBoard Partners (India) — "third-party independent asset management services for renewable assets".
- Note: no invoicing/contract-compliance machinery on the fetched pages — the commercial leg is not this product's depth. Its money-adjacent machinery is availability-under-contract and reporting.

## Product C — AlsoEnergy PowerTrack (monitoring-led pole)

- Self-label (A): "PowerTrack, AlsoEnergy's flagship application that is now on Stem's Athena platform, is the all-in-one application to meet the needs of commissioning, monitoring, optimizing, and controlling your clean energy portfolio or fleet"; homepage title "Solar Energy Monitoring and Control | Edge to Cloud"; scale "over 200,000 sites reaching 25+ GWs in 50 countries".
- Feature blocks (A):
  - Monitoring and operations: "Diagnostics and events", "Remote troubleshooting".
  - Data analysis: "Customized reporting", "Descriptive and performance analytics", "Supervisory dashboards", "System of record".
  - Energy management and controls: "Battery energy storage system", "Power plant controller configuration", "Remote control".
  - Integrate and monetize: "Non-native data ingest", "Overlays/Portfolio aggregation", "Agency and financial reporting", "CMMS integration", "APIs for workflow integration".
- Weather-adjusted expectation (A, PowerTrack page): "The Site Overview dashboard shows current production plus past performance comparisons… It also allows you to see actual versus weather-adjusted energy production so you can tell if your site is performing at its peak."
- Portfolio loss ranking (A): "The Portfolio View allows you to zoom out for a higher-level look at your entire portfolio. Identify and prioritize sites that are experiencing the most severe energy losses and address the causes."
- Light commercial layer (A): "Easy access to site documents and contracts in one folder with controlled permissions" — documents/contracts as a folder, not the deep CAM machinery of Power Factors.
- Controls as sibling product (A): "PowerTrack SCADA that enables real-time monitoring, control, and analysis… fully and seamlessly integrates with PowerTrack, ensuring data continuity"; "power plant controllers can be efficiently managed and programmed" for "local grid code compliance".
- Hardware/segment breadth (A): "hardware agnostic application… supports non-native data ingest from 3rd-party vendors"; segments utility / C&I / aggregated residential; roles asset owner, EPC, field services, control center, performance engineering; "Ranked #1 solar and storage monitoring and control vendor" (Guidehouse Insights Leaderboard, vendor-quoted).

## Product D — Clir Renewables (investor/asset-manager analytics pole)

- Self-label (A): "The AI behind high-performance renewable portfolios"; "Built On 350+ GW of Assets Across Solar, Wind & BESS"; audience "asset and investment managers" (Who We Serve: Asset Managers, Investment Managers, Corporate Offtakers).
- Four named capability blocks (A):
  - **Investor Grade Portfolio Reporting and Intelligence**: "Clir AI automates portfolio reporting across renewable energy assets, giving a clear, consistent, and comparable view of portfolio performance, industry benchmarking and reforecast projections. This allows asset managers investment managers and C-suite to effectively explain to their board which assets are over or underperforming, understand why, and make confident decisions about budgets and strategy."
  - **Contractual Availability Reconciliation**: "Clir's AI investigates performance availability data, reconciles OEM calculations, and generates dispute-ready reports. This saves significant time compared to manual log reviews and offline calculations, ensures consistency across sites, and gives in-house analysts and teams confidence with proven intelligence to challenge inflated bonus claims or conservative liquidated damage claims."
  - **Budget Reconciliation & Reforecast Energy Yield**: "Clir AI uses real operating data to enable advanced data labelling and benchmarking to reforecast long-term energy yield, replacing outdated and inaccurate estimates which budgets and valuations are often based off of. This makes budgets, cash flow projections, and valuations more accurate and credible. It also helps restore trust with investors and lenders by explaining underperformance and reducing the frequency of missed targets."
  - **Portfolio Performance Monitoring**: "enables investment managers, asset managers and site teams to actively monitor their portfolio in real time, benchmark performance, and quickly diagnose issues using standardized data and anomaly detection."
- Product decomposition (A): Clir Portfolio ("Fully integrated APM platform that unifies portfolio-wide data, enabling effortless data management, detailed reporting, benchmarking, proactive issue detection, and future risk forecasting"); Clir Enhance ("Vastly improves secondary SCADA systems by enriching data with Clir data model to enable portfolio level strategic decision making"); Clir Associate ("Optimizes executive level workflows").
- Demo promise (A): "Leverage Clir's AI on Your Wind, Solar, and BESS Portfolio for — Investor grade portfolio reporting and intelligence; Service provider oversight and contractual availability; Budget reconciliation and operational energy yields; Portfolio performance monitoring."
- Note: no control, no field service, no invoicing — the deepest evidence that the financial-reporting/reconciliation machinery can be a product's center of gravity, and that monitoring+analytics alone is a coherent renewable-AM product shape.

## Cross-product Comparison

| Dimension | Power Factors Unity | Bazefield | AlsoEnergy PowerTrack | Clir |
|---|---|---|---|---|
| Renewable asset population as system of record | plants + contracts + inventories, "comprehensive system of record", plant-to-contract drilldowns (A) | portfolio → power plant → asset hierarchy, "all your data in one place" (A) | "System of record"; portfolio/site/hardware drill-down (A) | "unifies portfolio-wide data" (A) |
| Production vs resource-driven expectation | availability & yield vs expectations (APM, sibling pass notes) (A) | power curve analysis; weather forecasting; capacity factor; expected performance (A) | "actual versus weather-adjusted energy production" (A) | benchmarking; reforecast energy yield vs budget (A) |
| Gap attribution / losses | "Revenue/energy loss impact calculations and related claim tagging" (A) | root-cause isolation for "stopped and under-performing assets"; alarm statistics (A) | "identify and prioritize sites that are experiencing the most severe energy losses and address the causes" (A) | "which assets are over or underperforming, understand why" (A) |
| Availability record | availability machinery in APM (sibling pass notes) (A) | availability analytics "based upon your contractual categorization or… IEC-61400"; availability planner (service, repair, substation or grid outage) (A) | downtime via diagnostics/events (A) | "Contractual Availability Reconciliation… reconciles OEM calculations… dispute-ready reports… bonus claims or liquidated damage claims" (A) |
| Maintenance / service coordination | FSM: work orders, personnel scheduling, inventory, maintenance KPIs (A) | availability planner (corrective + planned maintenance); work orders; site activity incl. HSE, safe passes, inductions; CMMS integration (A) | "CMMS integration"; field-services role (A) | "Service provider oversight" — oversight without execution (A) |
| Money / commercial resolution | deepest: contract-linked invoicing, escalation schedules, financial statements, budget vs actual, utility statement reconciliation, ERP push (A) | not in evidence on fetched pages (A-absent) | "Agency and financial reporting"; contracts as documents folder (A) | budget reconciliation, cash-flow projections, valuations, investor reporting (A) |
| Reporting to stakeholders | scheduled stakeholder PDFs, KPI tracking, audit-ready logs (A) | custom dashboards; reporting expense reduction claim (A) | customized/templated reports on performance and health; agency reporting (A) | "Investor Grade Portfolio Reporting" as the product's core promise (A) |
| Multi-vendor / multi-OEM data integration | "OEM-agnostic compatibility… mixed fleets with diverse asset types and vendors" (A) | turn-key turbine models (Vestas, Siemens, Nordex, GE…); OPC; IEC 61400-25 data model; historian integration (A) | "hardware agnostic… non-native data ingest from 3rd-party vendors" (A) | "secondary SCADA systems… enriched with Clir data model" (A) |
| Control (SCADA/PPC/EMS) | suite siblings SCADA/PPC/EMS ("market participation, real-time optimization, grid support") (A) | turbine controls + site access; no market dispatch seat in evidence (A) | PowerTrack SCADA + PPC programming as sibling products; "remote control" (A) | none (A-absent) |
| Customer seat | finance and asset-management teams; operations (testimonials) (A) | "investors, asset managers, and operators" (A) | asset owners, EPCs, field services, control centers, performance engineers (A) | "asset managers investment managers and C-suite"; boards/investors/lenders as audience (A) |

Reading: all four instantiate the same four structures — population record; production vs resource-driven expectation with attributed gap; availability/downtime events with maintenance coordination; production resolved into money and stakeholder reporting. The depth distribution differs per pole; no product's defining evidence sits outside the four.

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant (minimal)

Renewable Energy Asset Management is the owner-side management system for a portfolio of renewable generation assets. Four jointly-held structures; remove any one and the product stops being recognizable as this Type:

1. **The renewable asset portfolio as the system of record** — persistent, identified records for the owner's renewable plants and their producing assets across sites (commonly multi-technology and multi-vendor/OEM), each plant carrying its contracts and counterparties. Remove → a monitoring dashboard or an asset registry with no portfolio memory.
2. **Production managed against resource-driven expectation** — the system holds what the assets *should* have produced given the weather/resource that actually occurred (expected energy from resource models, power curves, performance ratios) and commonly what was budgeted/valued, against what they *did* produce, with every gap attributed (equipment downtime vs curtailment vs weather vs underperformance). Remove → a production statistics view; for weather-driven assets, no other expectation anchor exists.
3. **The availability record and its restoration** — downtime, derates and curtailment recorded and classified (commonly under defined availability computations), and maintenance coordinated against production commitments through work-order coordination and service-provider oversight. Remove → performance analytics with no availability discipline.
4. **Production resolved into money and stakeholder reporting** — metered production reconciled to offtake/settlement and invoicing where contracted, and periodic reporting to owners, investors, lenders and regulators at portfolio grain. Remove → an operation with no economic or accountability closure.

### L1 — Common Mature Structure

Present across most of the sample; expected in the market but not definitional:

- multi-vendor/multi-OEM data integration (SCADA-agnostic ingestion, normalization, gap-filling; OPC/IEC-style standards; historian connectivity) — the everyday substrate problem of the Type (4/4)
- monitoring & alerting as the standing loop: portfolio → site → asset drill-down, alarms/events, remote troubleshooting, a "control room" function for everyday operation (4/4)
- loss attribution & weather adjustment machinery: loss classification, energy-loss ranking across the portfolio, weather-normalized comparisons (4/4)
- availability computed under selectable definitions — contractual categorization, IEC-style standards — with reconciliation against OEM/service-provider calculations (deep at 3/4: Bazefield, Clir, Power Factors; light at AlsoEnergy)
- maintenance coordination: availability planners, work orders, CMMS/FSM integration, site activity incl. HSE/site access (3–4/4)
- performance engineering: power-curve analysis, PR/yield metrics, trending, benchmarking across assets and against industry datasets (4/4)
- scheduled, templated, audit-ready stakeholder reporting (monthly/quarterly/annual investor and owner reports; agency/compliance reporting) (4/4)
- forecasting (weather/power) feeding expectation and planning (3–4/4)

### L2 — Variant / Optional Structure

Depends on pole, segment, and business model:

- **Commercial asset management depth**: contract storage & compliance automation, warranty/insurance claim management, invoice management (contract-linked rates, escalation schedules, recurring billing), financial statements, budget-vs-actual, ERP integration — deep ONLY at the full-suite pole (Power Factors); partial at Clir (budget reconciliation); absent/light at monitoring-led poles. NOT definitional — this discharges the sibling pass's counter-possibility.
- controls: PPC configuration/programming, remote control, SCADA/EMS as sibling products (Power Factors, AlsoEnergy) — the management layer supervises, control ships beside it
- storage/hybrid modeling and BESS-specific KPIs (Power Factors, Clir, AlsoEnergy)
- market participation/optimization depth via EMS sibling (Power Factors)
- AI assistance / automated diagnosis / anomaly detection (Power Factors REMI, Clir AI) — era-current
- segment breadth: utility / C&I / aggregated residential (AlsoEnergy); wind/solar/hydro vs wind/solar/BESS technology mix
- deployment: cloud SaaS vs in-house installation (Bazefield offers both)
- owner-obligation machinery beyond the plants: land leases, community engagement, permitting — PowerHub territory (unreachable this pass; not sampled)

### L3 — Vendor-specific (Research Notes only)

- Power Factors: Unity suite decomposition and pillar naming; REMI AI assistant; GW/GWh counters; customer logo wall; product-sheet PDFs.
- Bazefield: SDK (.NET + REST), IEC 61400-25 default data model, ISO/IEC 27001 certification, named partnerships (Invenergy Services, SSE Renewables, W3 Energy, TruBoard), Porsgrunn HQ.
- AlsoEnergy: PowerTrack on Stem's Athena platform; edge-to-cloud platform framing; Guidehouse #1 ranking quote; distributor ordering flow.
- Clir: product names (Portfolio/Enhance/Associate); "350+ GW" dataset claim; $250K anti-reflective-coating recovery story; SOC/AICPA badge.

## Vendor-specific Findings

- Power Factors' TAM/CAM pillar naming mirrors the industry's technical/commercial asset-management division of labor — useful as evidence of the Type's internal structure, but the pillar names themselves are vendor vocabulary.
- Bazefield's IEC 61400-25-based data model and turbine-vendor turn-key support are implementation choices, not Type structure.
- Clir's "dispute-ready" contractual availability reconciliation is the sharpest articulation of machinery that is present-but-lighter elsewhere; treat as L1 depth, not L0.
- 3megawatt (Blade), a former independent TAM/CAM platform for renewables, is no longer independently verifiable (site redirects to Power Factors) — consolidation evidence only.

## Rejected Findings

- "Renewable AM = monitoring dashboards." Rejected: every sampled product carries availability/maintenance/reporting structures beyond monitoring; vendors themselves frame "management" and "oversight", not just monitoring.
- "Commercial asset management (invoicing/contracts) is the defining difference vs plant management." Rejected: CAM machinery is deep at one pole (Power Factors), partial at Clir, absent at Bazefield/AlsoEnergy — coherent products without it. It is L2 pole depth, not L0.
- "Contractual availability computation is definitional." Held at L1: strong at 3/4 products but the monitoring-led pole (AlsoEnergy, 200k sites) operates with light availability machinery; a definition requiring contractual-availability depth would exclude a major market pole.
- "Renewable AM is structurally a different Type from Power Plant Management." Rejected at the structure level: all four legs map onto the generation-management spine the sibling pass defined; the sampled renewable products pass the recorded test "remove the renewable-asset specialization → this Type". The differences are seat, expectation anchor, counterparty, and pole depth (see Boundary Findings).
- "Solar-only / wind-only portfolios are a different Type." Rejected: technology mix is a population axis, not a structural one (Bazefield wind-heavy, AlsoEnergy solar-heavy, Clir/PF multi-tech — same structure).
- "A production forecast engine is part of this Type." Held as L1: forecasting feeds the expectation side; standalone forecast production is the Energy Forecasting Platform territory.

## Boundary Findings

- **vs Power Plant Management (the joint-review seam).** Shared: the four-leg generation-management spine (population · production-vs-expectation · availability & restoration · accounting/compliance). Different seat and center of gravity:
  - PPM's pole = the plant/dispatch-operations seat: expectation anchored on dispatch schedules, market awards and system-operator compliance; depth in dispatch/AGC/transaction scheduling and regulatory availability reporting; counterparty = system operator/market.
  - REAM's pole = the owner's asset-management seat: expectation anchored on the resource (weather-normalized expected energy) and the budget/valuation; depth in contractual availability reconciliation with OEMs/O&M providers, portfolio-scale reporting to investors/lenders, and (at the full-suite pole) commercial asset management; counterparties = O&M providers/OEMs, offtakers, investors/lenders.
  - Market populations are disjoint (no vendor overlap between GMS-class and renewable-AM-class); the sampled renewable products carry no dispatch/scheduling seat (control ships as sibling products where present at all).
  - Resolution: **keep both as seat-defined siblings sharing the spine** (webmail/email-client precedent). Remove the owner-asset-management seat and its expectation anchor → Power Plant Management's pole; add a dispatch/scheduling seat as the center of gravity → PPM.
- **vs SCADA / Power Plant Controller / DCS**: the control substrate executing setpoints and grid-code compliance; renewable AM supervises, records and reports above it. Power Factors and AlsoEnergy ship control as separate sibling products — first-hand vendor evidence of the seam. Remove the management legs → SCADA.
- **vs CMMS / EAM / Field Service Management**: work-order execution and maintenance logistics; renewable AM coordinates maintenance against production and availability and hands work over. Bazefield "can be integrated to a maintenance system if required"; AlsoEnergy "CMMS integration"; Clir does oversight only.
- **vs Energy Forecasting Platform**: standalone forecast production; inside this Type forecasting feeds the expectation side (Bazefield weather/power forecast integration; Clir reforecast).
- **vs Energy Trading Platform / Energy Scheduling & Settlement**: the commercial book and market-facing settlement vs this Type's asset-side revenue resolution (invoicing where contracted, budget-vs-actual). Power Factors pushes "invoices, settlements, and financial statements" to ERP — integration, not the trading book.
- **vs DERMS / Virtual Power Plant Platform**: the grid operator's coordination layer over distributed resources, and aggregated-DER fleets optimized for market value vs this Type's owned portfolio seat.
- **vs Renewable Energy Certificate Management**: certificates/claims machinery vs asset operations; adjacent leaf.
- **vs Utility Asset Management / Enterprise Asset Management**: network-asset or generic-industrial registries and maintenance without production-vs-expectation semantics.
- Remove-X criteria: remove legs 2–4, keep record+monitoring → monitoring portal/historian dashboards; remove resource-driven expectation and attribution → asset registry with production stats; remove availability/maintenance coordination → pure performance analytics (forecasting/analytics territory); remove money/reporting resolution → monitoring + O&M coordination with no closure; remove the renewable asset population and its resource anchor → generic plant management (PPM pole).

## Historical / Market-Sample Check

- Paper-era wind-farm ownership (1990s): turbine log sheets and downtime logs against an OEM contract's availability guarantee; monthly production compared against expected energy computed from wind measurements; PPA invoices to the offtaker; owner reports. Satisfies all four L0 legs with no software, no cloud, no AI.
- Early solar monitoring-portal generation (late 2000s): portfolio monitoring, performance-ratio/expected-energy comparisons, downtime events, templated reports — fits the L0 legs at monitoring-led depth (AlsoEnergy's own heritage pole).
- Regional FIT-era technical asset managers (Germany/Southern Europe): monitoring + FIT/grid compliance reporting + O&M contract oversight — fits (regulatory reporting inside leg 4).
- Verdict: the definition does not depend on cloud, AI, controls, or CAM/invoicing machinery; the four legs are the owner's oldest disciplines (know what you should have produced, keep it available, account for it).

## Uncertainties

- PowerHub (owner-side land/community/lease machinery) unreachable — the land-management depth of renewable asset ownership is unsampled; noted as adjacent/variant, not characterized.
- The precise boundary of "market participation" machinery at the renewable pole (Power Factors EMS) is documented only at marketing depth; dispatch-side claims were not verified beyond product-page language.
- Whether the sibling solar/wind/BESS leaves will ratify as population variants of this Type is left to their passes; this pass records the expected resolution (same spine, population-level seams) without pre-empting their findings.
- Availability-definition standards (contract-specific formulas, IEC 61400-26-series conventions) are referenced by vendors but not documented in reachable detail; no precise formula claims are made.

## Final Synthesis

**Renewable Energy Asset Management is the renewable portfolio owner's asset-management system of record.** Its defining structure is the four-leg generation-management spine — renewable asset population · production managed against resource-driven (and budgeted) expectation with attributed gap · availability record with maintenance coordination · production resolved into money and stakeholder reporting — held at the owner's asset-management seat, where the expectation anchor is the weather/resource and the budget rather than a dispatch schedule, the availability discipline is contractual as well as operational, and the reporting audience is owners, investors and lenders. The market realizes the Type in four observable poles — full-suite owner platform (control→TAM→CAM), operator platform, monitoring-led portfolio management, investor-analytics — which differ in which leg is deep, not in the structure. Commercial asset management (contracts, invoices, claims) is real but pole-specific depth, not the definition. The Type shares its spine with Power Plant Management (kept as a seat-defined sibling: dispatch-operations seat vs asset-management seat) and differs from control (SCADA/PPC), maintenance execution (CMMS/FSM), forecasting, trading/settlement, DERMS/VPP and REC management by object and seat, not by vocabulary.
