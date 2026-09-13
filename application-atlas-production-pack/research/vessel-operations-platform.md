# Research Notes — Vessel Operations Platform

## Research Goal

Understand what "Vessel Operations Platform" is as an Application Type: what software a vessel operator runs to *operate* its vessels — voyage planning and execution, operational reporting, live fleet operations monitoring, performance and emissions — and how it differs from Marine Fleet Management (asset administration), Ocean Freight Management (cargo business), Port Terminal Operating System (terminal side), vessel tracking (data layer), and weather-routing advisory services.

## Initial Boundary

- Leaf: Vessel Operations Platform (§18 Transportation, Mobility & Logistics, between Marine Fleet Management and Ocean Freight Management).
- Hypothesis at start (from the marine-fleet-management pass's forward flag): the voyage-execution/operations center — voyage lifecycle, onboard operational reporting, fleet operations monitoring — vs Marine Fleet Management's fleet-as-asset administration center.
- Pre-hung flags to discharge this pass:
  1. **marine-fleet-management (§18, processed 2026-09-09)** — forward flag: seam hypothesis from inside one vendor family (ShipPalm = "operational data foundation and workflow management" vs SMARTShip = "monitor performance and ensure voyages execute as planned") and SERTICA's own product split (Maintenance/Procurement/HSQE/Crewing vs Performance/VRS/Logbook) — expect voyage-execution/operations center vs fleet-as-asset administration center.
  2. **fisheries-management (§20, processed 2026-09-08)** — vessels as authorized participants inside the fishery's record world vs vessels as logistics/crew/maintenance assets (already discharged from the marine side; confirm from this side).
  3. **ocean-freight-management (§18, processed 2026-09-09)** — that pass held "move to the carrier side → Vessel Operations Platform"; confirm the cargo-vs-carrier seam from this side.
  4. **port-terminal-operating-system (§18, processed 2026-09-09)** — ship-side vs terminal-side seam; confirm from this side.
- Family frame from the rail-operations-platform pass: Airline/Airport/Port-TOS/Vessel Operations Platforms are domain parallels sharing the "plan + live running + ops control" pattern.
- Not this Type: terminal operations, cargo booking/chartering, marina berthing, cruise passenger operations, vessel tracking services, fisheries governance.

## Research Questions

1. What is the unit of operational record — the voyage? the vessel? the report?
2. What does a "voyage" carry: plan (route/schedule/speed/fuel) and execution (positions, reports, events)?
3. How does the ship–shore operational data loop work: noon/arrival/departure reports, automated sensor acquisition, validation, consolidation?
4. What is the shore operations side's work: live fleet picture, deviation handling, re-optimisation, voyage instructions?
5. Which capabilities are definitional vs common vs optional: voyage optimization, performance monitoring, emissions/compliance reporting, charter-party machinery, weather intelligence, advisory services, bunker procurement?
6. Where is the seam vs Marine Fleet Management (asset admin), Ocean Freight Management (cargo), Port TOS (terminal), tracking (data), weather-routing advisory (service)?
7. Historical check: does the definition survive the paper-era ops desk (voyage orders + noon reports + wall chart)?

## Representative Products

| Product | Vendor | Why sampled | Evidence tier reached |
|---|---|---|---|
| ZeroNorth platform (Voyage Optimisation, SMARTShip, Vessel Reporting, Emission Analytics; ShipPalm as sibling ERP) | ZeroNorth (Denmark) | AI-native SaaS voyage/performance optimization vendor; documents the ops-vs-ERP seam from the inside; owner/operator/charterer customer tiers | A (root + Voyage Optimisation page) |
| Fleet Optimisation Solution (FOS) (+ Navi-Planner, SmartLog, Voyage Frontier, Eniram) | Wärtsilä (Finland) | OEM/bridge-systems-led voyage + performance + nautical platform; onboard-to-shore breadth; voyage-vs-fleet distinction in own FAQ | A (marine root + FOS product page) |
| SERTICA Performance + VRS + Logbook (+ Fleet) | RINA / SERTICA (Denmark/Italy) | Class-society modular suite where operations is a product line *beside* fleet management — the seam evidence inside one vendor; deepest module-level documentation | A (Performance page + VRS page) |
| StormGeo shipping (s-Planner, s-Routing, s-Log, Vessel Performance, Fleet Performance Center) | StormGeo (Norway, Alfa Laval) | Weather-service-led voyage planning/routing + performance monitoring; service+software hybrid posture | A− (official pages via search excerpts; direct fetch 403 ×2) |

Considered and dropped: helmops.com (now a yacht-management product — wrong pole, not sampled further); Kongsberg / Danaos / ABS NS / DNV / BASS (unreachable in the marine-fleet pass, not retried per network rules — no claims made); Veson/ChartCo and IMOS (chartering/freight-side pole, belongs to the ocean-freight seam, not sampled this pass).

## Sources

- ZeroNorth — https://zeronorth.com/ (fetched 2026-09-10) — platform map, user poles, FAQ
- ZeroNorth — Voyage Optimisation — https://zeronorth.com/voyage-optimisation (fetched 2026-09-10) — voyage plan lifecycle, CP adherence, live VOP, fleet view, platform connections, FAQ
- Wärtsilä — Marine products — https://www.wartsila.com/voyage (fetched 2026-09-10) — offering map, FOS FAQ
- Wärtsilä — Fleet Optimisation Solution — https://www.wartsila.com/marine/products/fleet-optimisation (fetched 2026-09-10) — FOS definition, modules, onboard/onshore benefits, FAQ, Carisbrooke case
- SERTICA — Performance — https://www.sertica.com/performance/ (fetched 2026-09-10) — ship performance monitoring, modules, FAQ (noon-report entry path, data flow, geofencing, KPIs)
- SERTICA — Vessel Reporting System — https://www.sertica.com/vessel-reporting-system/ (fetched 2026-09-10) — sequenced reports, validation, compliance reports, standalone/integrated packaging
- StormGeo — https://stormgeo.com/shipping ; /shipping/vessel-performance ; /shipping/voyage-planning-and-navigation ; /shipping/weather-routing-and-voyage-optimization ; /products/fleet-performance-center ; press releases (G2 Ocean 2025-02-06, TORM 2026-04-21) ; insight article (vessel efficiency) — **official pages accessed via search excerpts 2026-09-10; direct fetch returned 403 on both www and non-www (2 attempts, abandoned per network rules)**

Prior-pass context (not refetched): research/marine-fleet-management.md (seam hypothesis + ShipPalm/SMARTShip split), research/ocean-freight-management.md (carrier-side seam), research/port-terminal-operating-system.md (ship-side vs terminal-side), research/fisheries-management.md (vessel-as-participant), research/rail-operations-platform.md (§18 operations-platform family frame), research/fleet-management-system.md + research/vehicle-telematics-platform.md (road family pattern).

## Product A — ZeroNorth

### Key observations [A — direct]

- Self-label (root): "Maritime intelligence platform for shipping"; "Optimise fleet performance. ZeroNorth's AI-powered platform helps shipping companies make data-driven decisions to maximise efficiency, save on fuel, and stay compliant."
- Platform map: **Vessel** (SMARTShip "Onboard data acquisition and reporting"; Charter Select "Find the right vessel for every voyage"), **Voyage** (Voyage Optimisation "Plan the most efficient route, every time"; Vessel Reporting "Automated noon and arrival reports"; Emission Analytics "CO₂ tracking across your fleet"; Scope 3 "Charterer emissions reporting"), **Fuel** (Bunker Procurement, Bunker Pricer, eBDN), **ERP** (ShipPalm "Maritime ERP for fleet management and operations").
- User poles: vessel owner ("Turn every vessel into a high-performing asset that boosts your bottom line and CII rating"), commercial operator ("Optimise your voyage for maximum returns and efficiency"), charter manager (forecast emissions/costs before contract), bunker platform.
- FAQ: "ZeroNorth provides an AI-driven maritime intelligence platform that optimises voyages, vessel performance, compliance, and emissions"; "used by shipowners, operators, charterers, and commercial teams managing fleets at scale"; "What is voyage optimisation? …determining the most efficient route and speed for a vessel by analysing weather conditions, ocean currents, vessel performance, fuel consumption, and operational constraints."
- Voyage Optimisation page: "Continuously refine routing, speed and fuel use with vessel-specific fuel models and real-time weather intelligence, cutting fuel, lowering emissions and sharpening every decision. Voyage optimisation, weather routing and speed optimisation, in one platform."
- **Real-Time Weather Optimisation**: "Receive regularly updated weather forecasts, with alerts when shifting conditions call for a re-optimisation. Evaluate route adjustments based on weather exposure, cost impact, and emissions performance before making operational changes."
- **Charter Party Adherence**: "Build voyage plans that stay within Charter Party speed bands, consumption clauses and weather routing windows from the outset. Voyage Optimisation factors CP terms into routing calculations so the recommended plan is commercially defensible before the voyage begins, not contested after it ends."
- **AI-powered Fuel Models**: "vessel-specific fuel predictions… naval architecture, machine learning and historical vessel data."
- **Live VOP**: "Access a live voyage plan in your browser, reflecting the latest weather data and every approved re-optimisation — ensuring decisions reflect current conditions, not outdated assumptions."
- **Voyage-level Fleet View**: "Track routes, destinations, speed recommendations and in-voyage performance for every active voyage in a single view. For full operational state across sensors, AIS and asset health, SmartShip is the source of truth."
- Mechanics: "Routing simulation at scale — Every voyage scored on bunker cost, time and emissions exposure before the order goes out"; "Live weather integration — Forecasts refresh continuously throughout the voyage. When weather windows shift, a re-optimisation is triggered for review and approval — so the plan stays current rather than stale"; "Connected across the platform — Routing decisions flow into SmartShip for execution monitoring, into Bunker Procurement for stem planning, and into Emission Analytics for compliance evidence. No re-keying."
- Testimonials (user roles): "A very useful tool for master and operator. Creates a safe and optimum passage plan" (Operations Manager); "The route suggestions have been accurate and practical, and the interface is easy to work with during daily operations" (Senior Vessel Operator, Maersk Tankers); "All-in-one portal, from weather routing, to integration to IMOS, to EU-ETS, and many more" (IINO Lines); "clarity and confidence… in our daily operational decisions" (Operations Manager, Millenia Maritime).
- Marketing numbers (L3): 93.8% median fuel-model accuracy; 2.7M+ voyages optimised; 5.2M+ MT CO₂ saved since 2022; 5,500+ vessels; 200+ owners/operators/charterers; FAQ: forecasts updated every six hours; 3–10% fuel reduction per voyage; TCE improvement framing.

## Product B — Wärtsilä Fleet Optimisation Solution (FOS)

### Key observations [A — direct]

- Marine root: offering category "Voyage and fleet optimisation — Fleet optimisation solution (FOS), voyage planning, marine navigation solutions, vessel performance management." FAQ: "Wärtsilä's Fleet Optimisation Solution (FOS) is a holistic data analysis, voyage planning and fleet performance management package, integrated with nautical services and navigation solutions. FOS lets you monitor, manage and optimise onboard and onshore processes. The system uses navigational, technical and operational data together and gives you deeper insights into your fleet operations."
- FOS page definition: "FOS is a digital platform that combines navigational, operational and technical vessel data to help operators improve fleet performance, optimise voyages, monitor efficiency and support better operational decision-making." / "How it works: FOS collects and analyses data from vessels and fleet operations, combining performance monitoring, voyage optimisation, compliance reporting and operational analytics into a single platform that supports both onboard and shore-based teams."
- Users: "fleet performance managers, technical managers, operations teams and vessel operators."
- Modules:
  - **Hull and machinery performance** — "monitors the status of the vessel's hull and propeller and the condition of the engines… advanced algorithms… will notice deviations from normal system behaviour and you will get a notification"; hull/propeller degradation assessment, engine condition assessment, virtual fuel consumption modelling.
  - **Emissions compliance** — EU Emissions Compliance application (EU ETS, EUA cost calculation); CII Dashboard ("Maintain and manage ship or fleet CII ratings in real time"); SmartLog ("Streamline the reporting process and reduce the admin burden on crews using data from your ECDIS").
  - **Voyage optimisation** — Voyage Optimiser tool ("a shore-side application that helps you optimise voyages, routes, sailing speeds and port stays… uses weather data, safety parameters and commercial efficiency considerations… will also monitor the progress of your voyage against the plan"); Wärtsilä Voyage Frontier ("combines advanced digital tools with 24/7 maritime expertise to help you plan, monitor and adjust routes in real time. From pre-voyage checks to post-voyage reviews… reducing risk, improving efficiency, and supporting charter-party compliance").
  - **Nautical compliance / navigation** — Navi-Sailor ECDIS; Navi-Planner ("a cyber-secure onboard system for voyage planning, optimisation and monitoring"; shore side: "empowers your onshore operators to track individual vessels and entire fleets in real time… Ship and route tracking including playback and play-ahead functionalities… chart backgrounds and overlays (e.g., weather, regulatory zones)… Zone management and notifications (e.g., MARPOL, ECAs, risk)… Ship-to-shore commenting on notifications and issues"); BridgeMate; FOS downloads (charts/publications to ECDIS).
- Benefits onboard: faster route planning "in minutes"; "the system identifies the safest, most efficient route based on the latest navigational charts, built-in weather optimisation, and advanced fuel-efficiency algorithms"; "Automatic alerts draw attention to unusual ship behaviour or anomalies"; "Ship-to-shore reporting is simpler and faster, with most of the data already pre-filled"; "ETA information shared with connected ports enables just in time arrivals."
- Benefits onshore: "Track vessels in real time from any location"; "Access vessel operational data for post-voyage analytics"; "Improve voyage performance management and make better decisions with access to real-time vessel data including charter party compliance alerts"; "Save time with automatic stakeholder and statutory reports."
- FAQ distinctions: "Voyage optimisation focuses on improving the performance of individual voyages through route planning, weather routing and operational decisions. Fleet optimisation looks more broadly across multiple vessels and voyages, helping operators compare performance, identify trends and prioritise improvement actions at fleet level." Data needed: "voyage information, fuel consumption, vessel speed, weather conditions, engine performance and operational reporting."
- Case: Carisbrooke Shipping — FOS across 31 vessels, 600 tons CO₂ reduction, 5–7% fuel savings (marketing numbers — L3).
- Eniram by Wärtsilä — "tailored software solution for cruise ships, complex merchant ships and other specialised vessels… real-time insight, powerful post-voyage analytics."
- Deployment: "Available with hardware deployment or as a software-only solution"; cloud upgrades; "24/7 expert advice on hand from the FOS consultancy team."

## Product C — SERTICA Performance / VRS / Logbook / Fleet (RINA)

### Key observations [A — direct]

- Performance page self-label: "Ship Performance Monitoring System | SERTICA Performance"; "SERTICA Performance turns ship data into lower fuel costs and clearer decisions. Crews and shore see the same live picture, with geofencing and timely alerts that keep attention where it matters. Dashboards confirm the impact so improvements carry across the fleet."
- Modules: Advanced Analytics (KPIs, dry dock analysis); Data Collector ("Collect data from the systems and sensors onboard the vessels"); Geofencing & Rules Editor ("Enhance safety and compliance with alerts on specific operating conditions and locations"); Propulsion Assistant ("Monitor your propulsion efficiency depending on the condition of the hull, propeller and engine"); Reporting & Dashboards; Trim Assistant; Voyage ("Predicts fuel usage effectively under changing conditions, helping you choose the most efficient route").
- Before/after framing: "Before a monitoring system, answers depended on call chains, email threads, and sending someone onboard for days to collect readings. SERTICA Performance replaces this with a shared, live view for ship and shore, so decisions move in minutes instead of days."
- FAQ — product-family seam: "Pair Performance with Vessel Reporting System (VRS) for structured voyage reporting and SERTICA Logbook for manual entries, so what crews record feeds directly into the same operational picture. For a high-level view of how these capabilities scale across many vessels, see SERTICA Fleet."
- FAQ — entry path: "You can start on noon reports. It works offline and syncs when connected. Adding sensors later makes guidance more precise. This hybrid path is typical for operators adopting ship performance monitoring for the first time."
- FAQ — data flow: "Data flow from ship to shore uses local buffering onboard and synchronization in 5-minute aggregates to Microsoft Azure when connectivity is available. You get one view for ship and shore. If the link is weak, data queues locally and syncs when the connection returns."
- FAQ — geofencing/alerts: "area- and condition-based rules that route targeted notifications by vessel, area, role and severity. Typical use cases include ECA fuel discipline, generators in port, boiler usage, speed targets and standstill events."
- FAQ — KPIs: "Some standard KPIs include speed, shaft power, RPM, fuel t/h, SFOC and trim angle. In SERTICA, KPIs are grounded in collected signals and manual entries with plausibility checks, and can be reviewed with references to their underlying inputs."
- FAQ — interfaces: "connects to navigation/automation systems and direct sensors via NMEA, Modbus and OPC, with optional manual inputs (e.g., fuel type, drafts)… It connects through these interfaces and sits alongside your existing routing and logging tools."
- FAQ — seam to maintenance: "When performance trends point to technical follow-ups, many operators coordinate work in maintenance system to plan inspections and interventions based on the insights."
- Case: Grimaldi — "optimizes routes and speeds for fuel efficiency and timely arrivals with high-frequency data through integration and monitoring with SERTICA Performance."
- VRS page: "Simplify compliance by centralizing all vessel reporting in one system"; "All-in-one reporting system that connects ship and shore… Access vessel reports and synchronize templates with reliable data transfer, automatic data validations and calculations between ship and shore. Offline functionality… External integration with applications through API, Excel, and analytics reporting tool."
- VRS — customizable reports: "Configure vessel specific parameters for your input data validation and consistency check. Use pre-configured reports or create your own custom reports assisted by the powerful report designer… No development needed."
- VRS — sequenced reports: "Simplify the reporting process for your crew… by letting them know which ship reports to fill out and when with sequenced reports. As the crew enters new data, the system automatically performs real-time quality checks… raises warning or error messages if any anomalies are found." Example sequence (FAQ): "Departure report → BOSP/COSP report → Noon reports → EOSP report → Arrival/Berthing report."
- VRS — compliance: "covering all noon reporting needs as well as standard reports for EU MRV, IMO DCS, CII and Performance"; CII Simulator; Decarbonization Reports; Performance Reports; "crew members can complete and submit vessel reports to all stakeholders with just one submission, avoiding unnecessary duplication of effort."
- VRS — packaging: "The VRS works both as a stand-alone solution and as an integrated part of SERTICA Ship Management System"; web-based, "no need for extra hardware installation onboard."
- Users (testimonials): Fleet Manager (Argenmar — flag-authority reporting), Performance Manager / Performance Engineer (Technomar — CII/biofuel reporting sequences "that align naturally with each voyage").
- Product-family context (from the marine-fleet pass, same vendor): SERTICA's product line = Maintenance, Procurement, HSQE, Crewing (fleet-as-asset) **plus** Performance, VRS, Logbook, Fleet (operations) — "All SERTICA products integrate with each other, providing your fleet with a complete and comprehensive management system."

## Product D — StormGeo

### Key observations [A− — official pages via search excerpts; direct fetch 403 ×2]

- Shipping root: "Get a holistic overview of your voyage planning, route, and fleet performance all from a single platform, and chart new waters with data-driven, domain-tailored advice"; "12,000+ ships rely on StormGeo software or services for navigational planning, route optimization, weather and fleet performance"; "75,000 voyages routed per year including voyage performance analysis"; "5,800 vessels with installed software for route optimization"; "2,900 vessels with chart and publication subscriptions."
- Solution areas: **Voyage Planning & Navigation** ("A complete e-navigation solution to enable safe voyages, transparent ship-to-shore communication, optimized performance, and process automation"); **Emissions Reporting & Compliance**; **Weather Routing & Voyage Optimization**.
- Vessel Performance: "full overview of voyage, hull and propeller, engine and system performance to identify cost-saving measures. The Fleet Performance Center team will also validate and help you interpret your data"; "Ship-to-shore transparency — By sharing commercial and technical performance data on one platform, the crew onboard, fleet manager and operator can make joint decisions to optimize energy efficiency and reduce costs"; "Hardware independent — s-Suite works with all major systems on the shipping market."
- Products: **s-Log** ("Simplify ship-to-shore communication by aggregating all important voyage data in a single data stream"); **Commercial Performance** ("Monitor and optimize your fleet's commercial performance for safer, profitable and sustainable operations"); **Technical Performance** ("Reduce vessel costs by monitoring the efficiency of your hull, propeller, engine, and auxiliary systems"); **Fleet Performance Center** ("comprehensive and customizable fleet monitoring services for efficiency and cost savings" — expert support pole).
- Voyage Planning & Navigation: **s-Planner** ("Integrate route optimization and weather insights with up-to-date ENCs and Publications for accurate navigational planning"); **Publications** (digital library of accredited publications); **Seakeeping** ("Reduce the impact of severe weather on your crew and cargo safety"); "Instant access to digital charts and publications… ENCs and publications automatically updated"; "Our hurricane and typhoon center issues timely updates ahead of most models."
- Weather Routing & Voyage Optimization: "empowers onboard and shoreside teams to plan and execute optimized, compliant voyages by combining AI-driven insights, advanced technology, and weather intelligence — all guided by the expertise of experienced maritime professionals"; "24/7 support from experienced route analysts"; **s-Routing** ("Our seasoned route analysts use StormGeo's state-of-the-art technology to advise, and guide you through, the safest most cost-effective route"); **Voyage Optimization** ("Manage total voyage cost both pre-voyage and en route, while quickly incorporating changes in the market and/or Required Time of Arrival"); **Classic Routing** ("Expert-driven routing for optimal fuel and voyage performance").
- G2 Ocean press release (2025-02-06): Voyage Optimization deployed across 120 vessels; "combines robust features such as onboard voyage planning, routing advisory, speed optimization, emissions monitoring and reporting, commercial and technical performance optimization based on High-Frequency sensor data, and advanced APIs"; "support at every stage of the voyage"; "over 300 operational support professionals."
- TORM case (2026-04-21): s-Planner across ~90 vessels; "provides TORM's bridge and shore-based teams with a shared platform for voyage planning, weather insight, and route evaluation, supporting consistent and informed decision-making"; "TORM conducts its own weather routing in-house and maintains a strong operational setup" — routing can be in-house while the planning platform is bought.
- Insight article: "StormGeo manages about 5,500 routes each month, covering virtually every vessel type"; "StormGeo aligns different data sources such as manually reported voyage data, performance snapshots and high frequency sensor data"; Fleet Performance Center "provides this expertise to a full scope" for owners who prefer external support; "Purchasing voyage optimization and fleet decision support software for onboard and onshore usage may not yield a quick return on investment if owners neglect to provide adequate training for crews."

## Cross-product Comparison

| Dimension | ZeroNorth | Wärtsilä FOS | SERTICA Perf/VRS | StormGeo | Layer |
|---|---|---|---|---|---|
| Voyage as unit of operational record (plan + execution accumulation) | ✔ (voyage plans, Live VOP, "every active voyage in a single view") | ✔ (voyage plans; "monitor the progress of your voyage against the plan") | ✔ (VRS sequenced voyage reports: departure → BOSP/COSP → noon → EOSP → arrival) | ✔ ("75,000 voyages routed per year"; pre-voyage/en-route/post-voyage) | A×4 — core |
| Voyage plan: route / schedule / speed / fuel | ✔ (routing + speed + fuel models) | ✔ (Voyage Optimiser: routes, speeds, port stays) | △ (Voyage module predicts fuel/route) | ✔ (s-Planner onboard planning; s-Routing) | A×3+△ — core |
| Ship–shore operational data flow (reports and/or automated acquisition) | ✔ (Vessel Reporting automated noon/arrival; SMARTShip acquisition) | ✔ (SmartLog from ECDIS; "reporting… pre-filled") | ✔ (VRS + Logbook + Data Collector; offline + sync) | ✔ (s-Log "single data stream"; manual + sensor alignment) | A×4 — core |
| Live fleet operations picture | ✔ (voyage-level fleet view; SmartShip "source of truth") | ✔ (Navi-Planner real-time tracking; FOS monitoring) | ✔ ("crews and shore see the same live picture"; live map) | ✔ (fleet monitoring; Fleet Performance Center) | A×4 — core |
| Deviation surfacing → direction back to vessel | ✔ (weather re-optimisation alerts; "review and approval") | ✔ (anomaly alerts; CP compliance alerts; ship-to-shore commenting) | ✔ (geofencing + rules by role/severity; guidance to crews) | ✔ (24/7 route analysts; re-routing advice) | A×4 — core |
| Voyage/route/speed optimization | ✔ (core product) | ✔ (Voyage Optimiser) | ✔ (Voyage module; "complements existing voyage optimization tools") | ✔ (core: software + analyst service) | A×4 — common-strong |
| Performance monitoring & analytics (fuel/hull/engine) | ✔ (fuel models; in-voyage performance) | ✔ (Hull & machinery module; benchmarking) | ✔ (Propulsion/Trim Assistants; Advanced Analytics) | ✔ (Technical Performance; Commercial Performance) | A×4 — common |
| Emissions/regulatory reporting (CII, MRV/DCS, EU-ETS-class) | ✔ (Emission Analytics, Scope 3) | ✔ (CII Dashboard, EU Emissions app, statutory reports) | ✔ (MRV/DCS/CII reports, CII Simulator) | ✔ (Emissions Reporting & Compliance area) | A×4 — common (era layer) |
| Charter-party machinery | ✔ (CP-aware planning: speed bands, consumption clauses) | ✔ (CP compliance alerts; Voyage Frontier CP support) | — not observed | △ (RTA/market changes; commercial performance) | A×2+△ — variant-leaning |
| Weather intelligence integration | ✔ (integrated forecasts, re-optimisation triggers) | ✔ (built-in weather optimisation; overlays) | △ (optional weather layers on map) | ✔ (core heritage; hurricane/typhoon center) | A×3+△ — common |
| Onboard bridge planning surface | △ (browser Live VOP; master testimonial) | ✔ (Navi-Planner onboard; ECDIS integration) | △ (web-based VRS onboard) | ✔ (s-Planner onboard) | mixed — common |
| Human advisory/monitoring service | — not observed | ✔ (Voyage Frontier 24/7; FOS consultancy) | △ (RINA naval architects support) | ✔ (route analysts; Fleet Performance Center) | A×2+△ — variant posture |
| Bunker/fuel procurement machinery | ✔ (Bunker Procurement/Pricer/eBDN) | — | — | — | A×1 — optional |
| Chartering/vessel-selection intelligence | ✔ (Charter Select — separate product) | — | — | — | A×1 — optional (seam) |
| Maintenance/crew/procurement (fleet administration) | — (ShipPalm = separate ERP product) | — (lifecycle services = separate line) | ✔ sibling products in same suite | — | seam evidence |
| Noon-report-only entry tier | implied (Vessel Reporting) | ✔ (SmartLog) | ✔ (explicit FAQ: "start on noon reports") | ✔ (s-Log manual entries) | A×3 — entry form |
| Sensor/NMEA-class automated acquisition | ✔ (SMARTShip) | ✔ (hardware or software-only) | ✔ (Data Collector; NMEA/Modbus/OPC) | ✔ (high-frequency sensor data) | A×4 — common |
| Port ETA sharing / JIT arrival | — not observed | ✔ ("ETA information shared with connected ports") | — | — | A×1 — optional |
| Post-voyage analytics & stakeholder/statutory reports | ✔ (Emission Analytics evidence) | ✔ ("post-voyage analytics"; "automatic stakeholder and statutory reports") | ✔ (dashboards; audit-ready reports) | ✔ (voyage performance analysis) | A×4 — common |
| Deployment: cloud SaaS / onboard hardware / hybrid | ✔ (SaaS) | ✔ (hardware or software-only; cloud upgrades) | ✔ (web-based, no extra hardware; Azure sync) | ✔ (installed software + services) | A×4 — variant |

## Canonical Abstraction

### L0 — Defining Invariant

Vessel Operations Platform is the vessel operator's voyage-execution system of record. Its defining core is exactly three jointly-held structures:

1. **The voyage as the unit of operational record** — each commercial voyage (berth-to-berth: departure → sea passage → arrival, including port stays) exists as a persistent identified record carrying its plan (route, schedule/ETA, speed and fuel intentions) and accumulating its execution (positions, reports, events, consumption). Remove → performance dashboards or tracking maps with no voyage object; there is no voyage to operate.

2. **The ship–shore operational data loop** — the vessel's operational data reaches the shore operations side continuously, through crew-entered voyage reports (departure/noon/arrival-class, validated and sequenced) and/or automated onboard data acquisition, and is consolidated into the voyage record; operational direction (route/speed instructions, re-optimisations, voyage orders) flows back to the vessel. Remove → a shore analytics archive the vessel never feeds, or an onboard logbook with no operations function.

3. **The fleet operations control surface** — the operator's continuously refreshed picture of every active voyage against its plan (position, progress, speed, fuel, ETA), from which the operations side monitors the fleet, surfaces deviations as alerts, and directs corrections. Remove → batch reporting with no live operations function, or a position map with no voyage semantics (tracking territory).

Jointly-held load-bearing:
- 1 alone = a voyage file/archive (logbook store)
- 2 without 1 = a data pipe / reporting tool with nothing to organize
- 3 without 1+2 = a tracking map (vessel-tracking territory)
- 1+2 without 3 = a reporting archive nobody operates from
- 1+3 without 2 = a picture with no data flow behind it
- 2+3 without 1 = live tracking + feeds with no voyage record
- Domain binding: the operated objects are commercial vessels in service and their voyages; remove the voyage/maritime semantics and the remainder is generic fleet-operations/telematics machinery.

### L1 — Common Mature Structure

Present in essentially all mature products; expected by the market but not definitional:

- Voyage/route/speed optimization with weather integration and continuous re-optimisation loops (approval steps on plan changes)
- Performance monitoring and analytics: vessel-specific fuel models, hull/propeller/engine condition, trim guidance, KPI dashboards, sister-vessel benchmarking, post-voyage analysis
- Emissions and regulatory reporting: CII-class rating tracking, MRV/DCS-class reporting, EU-ETS-class compliance evidence, voyage-level emissions accounting
- Charter-party adherence machinery (speed bands, consumption clauses, required time of arrival) in tramp/chartered trades
- Weather intelligence: forecast integration, overlays, hurricane/typhoon-class centers
- Automated onboard data acquisition (sensor integration, ECDIS-data reuse, NMEA-class interfaces) augmenting or replacing manual reports
- Geofencing and rules-based alerting routed by vessel/area/role/severity
- Sequenced, validated voyage reporting with one-submission-to-many-stakeholders distribution
- Port ETA sharing / just-in-time arrival support
- Onboard bridge planning surfaces (ECDIS-adjacent) and shore-side planning tools
- Post-voyage analytics and automatic stakeholder/statutory reports
- Roles separating onboard and shore; approval steps on plan changes; plausibility checks making KPIs traceable to inputs

### L2 — Variant / Optional Structure

- Bunker procurement / fuel purchasing machinery (fuel-supply business adjacent to voyage execution)
- Chartering/vessel-selection intelligence (commercial seam with ocean freight)
- Segment shapes: tramp/charter-party-driven (tankers, bulk, breakbulk) vs schedule-driven liner operations; cruise/complex-ship performance editions
- Service-attached deployments: outsourced fleet monitoring and 24/7 route-advisory centers (vendor-run ops desks)
- Packaging: standalone operations products vs module-level operations lines inside ship-management suites vs operations products layered over a fleet-record ERP
- Entry tier (noon-report-only, no sensors) vs fully sensor-instrumented fleets
- Charterer-side deployments (emissions/scope-3 reporting from the charterer's seat)
- Deployment shape: cloud SaaS, onboard hardware + shore cloud, hybrid

### L3 — Vendor-specific (kept out of the final document)

- ZeroNorth: Propel agent, product names (SMARTShip, Charter Select, Live VOP, eBDN), marketing numbers (93.8% fuel-model accuracy, 2.7M+ voyages, 5.2M+ MT CO₂, 5,500+ vessels, 200+ customers), FAQ cadences (6-hour forecast refresh, 3–10% savings), customer quotes (Maersk Tankers, IINO Lines, Millenia, CMB.TECH)
- Wärtsilä: product names (Navi-Planner, Navi-Sailor ECDIS, SmartLog, Voyage Optimiser, Voyage Frontier, BridgeMate, Eniram, FOS downloads), Carisbrooke numbers (31 vessels, 600 t CO₂, 5–7%), FOS consultancy framing
- SERTICA: module names (Data Collector, Geofencing & Rules Editor, Propulsion/Trim Assistant, CII Simulator), 5-minute Azure aggregates, NMEA/Modbus/OPC specifics, Grimaldi/Technomar/Argenmar cases, FuelEU simulator lead-gen
- StormGeo: s- naming (s-Planner, s-Routing, s-Log, s-Suite), scale numbers (12,000+ ships, 75,000 voyages/yr, 5,800 vessels, 5,500 routes/month, 300+ professionals, 5M+ MT fuel saved), TORM/G2 Ocean cases, Alfa Laval ownership

## Rejected Findings (anti-overfit)

- **AI/algorithmic voyage optimization is NOT definitional** — the paper-era ops desk and the noon-report software generation satisfy the core with no optimization engine; SERTICA documents the noon-report entry path explicitly ("You can start on noon reports… Adding sensors later makes guidance more precise"). Optimization is the modern differentiator (L1).
- **Live sensor/AIS telemetry is NOT definitional** — crew-entered reports are the minimal data flow; automated acquisition is the common modern augmentation. A tracking feed without voyage records is a different Type (leg-3-alone test).
- **Emissions/CII/MRV/EU-ETS machinery is NOT definitional** — era-current regulatory layer, uniformly present in the 2026 sample but absent from the Type's history; the invariant is that voyage data is reported onward, not any specific regime.
- **Weather routing is NOT definitional** — it is a capability (software) and a service posture (analyst desks); TORM "conducts its own weather routing in-house" while buying the planning platform; routing-only advisory without voyage records is not this Type.
- **Charter-party machinery is NOT definitional** — tramp-trade emphasis; owned/liner fleets operate without CP clauses; observed strongly in 2/4 products.
- **Human advisory/monitoring services are NOT definitional** — a service posture (StormGeo Fleet Performance Center, Wärtsilä Voyage Frontier), not a structure; some operators buy software only.
- **Bunker procurement is NOT definitional** — adjacent fuel-supply business (ZeroNorth pole only).
- **"Platform" suite packaging is NOT definitional** — the Type is realized standalone (ZeroNorth voyage products, StormGeo), as modules inside a ship-management suite (SERTICA), and as an OEM platform (Wärtsilä).
- **Specific KPI sets, cadences, thresholds are NOT definitional** — product-specific facts (5-minute aggregates, 6-hour forecasts, KPI lists) stay in Research Notes.

## Boundary Findings

1. **vs Marine Fleet Management (§18 — DISCHARGES the marine pass's forward flag; keep-both RATIFIED)**: the seam is the object of work. This Type centers **voyage execution** (the voyage as unit of record, the operational data loop, the fleet operations picture); Marine Fleet Management centers **fleet-as-asset administration** (fleet register, equipment-structured per-vessel technical record, maintenance/crew/procurement/compliance workflows). Evidence from inside two vendor families: SERTICA ships both as separate product lines (Maintenance/Procurement/HSQE/Crewing vs Performance/VRS/Logbook/Fleet — "All SERTICA products integrate with each other"); ZeroNorth splits ShipPalm ("operational data foundation and workflow management") from SMARTShip/Voyage products ("monitor performance and ensure voyages execute as planned"); SERTICA's own FAQ documents the handoff ("when performance trends point to technical follow-ups, many operators coordinate work in maintenance"); Wärtsilä separates FOS from its lifecycle/maintenance services line. The two Types share the ship–shore loop *pattern*, but what flows differs: maintenance jobs/work vs voyage data/orders; and the record differs: equipment-structured technical file vs voyage-execution file. Removal tests: remove the voyage object + ops loop, keep the equipment-structured technical record + maintenance loop → marine fleet management; remove the equipment/technical record, keep voyage record + ops loop → this Type. Suites bundle both; standalone products exist on both sides. Hypothesis confirmed.
2. **vs Ocean Freight Management (§18 — confirms that pass's seam from this side)**: the cargo business (bookings, chartering fixtures, bills of lading, containers, demurrage) vs the vessel business (voyage execution). The charter party is made on the commercial side; operations *consumes* CP terms as constraints (ZeroNorth CP-aware planning; Wärtsilä CP compliance alerts). ZeroNorth's Charter Select (vessel selection for voyages) sits on the seam as a separate product. Keep-both.
3. **vs Port Terminal Operating System (§18 — confirms from this side)**: the terminal operator's facility-side production (berth, yard, gate; the vessel call as *the terminal's* unit) vs the vessel operator's voyage-side execution. ETA sharing to ports (Wärtsilä "ETA information shared with connected ports enables just in time arrivals") is an interface between the two Types, not a merge. Keep-both.
4. **vs Vessel tracking / telematics data layer**: tracking services acquire and publish position data (often for third-party ships); this Type holds the operator's own voyage records and directs execution. AIS/sensor feeds are inputs. A live map without voyage records and the ops loop = tracking territory (leg-3-alone test). Consistent with the road telematics pass's data-engine framing.
5. **vs Weather-routing / voyage-advisory services**: routing advisory can be a human service (StormGeo route analysts, Wärtsilä Voyage Frontier 24/7 desks) — the same vendor can ship both software and service. A pure advisory service with no voyage record, no fleet picture, no reporting loop is not this Type; the service posture is a variant deployment of it when attached to the platform.
6. **vs Fisheries Management (§20 — DISCHARGES the flag from this side; keep-both confirmed)**: here the vessel is the operator's voyage-executing asset and the record world is voyages/reports/performance; in fisheries the vessel is an authorized participant inside the fishery's frame and the record world is catch/effort/entitlements. No shared record objects. A fishing company could run both.
7. **vs Cruise Operations Platform (§18 sibling, unprocessed — forward flag left)**: cruise operations centers the passenger/cruise program (voyages as guest itineraries, cabins, onboard services); this Type centers voyage execution of the vessels (nautical/technical/performance). For cruise fleets, vessel-operations machinery runs alongside guest operations (Eniram cruise edition noted). Flag left for that pass; this-side evidence only.
8. **vs Flight Planning Application (§18 sibling)**: aviation parallel (route planning for flights); different domain machinery (airways, NOTAMs, fuel-burning at altitude). The §18 operations-platform family (rail/airline/airport/port-TOS/vessel) shares the plan + live running + ops control pattern (per the rail pass); each is domain-bound. Related Type.
9. **vs road Fleet Management System / Vehicle Telematics Platform (§18, processed)**: family pattern (plan + live running + ops control). Road FMS centers drivers (behavior, HOS, dispatch); telematics is the data engine. Marine ops centers voyages and the ship–shore operational loop with crew-entered reporting as the classic data source. Related Types.
10. **vs Marina Management / Boat-Yacht Charter Platform (§18, processed)**: facility side and demand-side marketplace respectively; no shared record objects with voyage execution. No action.

## Historical / Market-Sample Check (§24)

- **Paper-era operations desk**: the operator issued voyage orders/instructions to the master; the master sent daily noon reports by radio/telex (position, course and speed, weather, fuel remaining on board, distance run); departure/arrival (and BOSP/EOSP-class) reports were filed; deck and engine logbooks recorded the passage; the ops desk plotted positions on a wall chart and compared progress against the plan; weather routing advice arrived from meteorological services by radio. All three L0 legs are satisfied with no software, no AIS, no sensors: voyage record (the voyage's report file), ship–shore loop (reports up, orders down), operations picture (the chart, refreshed at the data cadence). → L0 survives.
- **The noon report is the historical anchor** of the operational data flow; the wall chart is the historical anchor of the ops picture. Modern products automate both (Vessel Reporting "automated noon and arrival reports"; live maps) without changing the structure.
- **1980s–90s software generation**: shore-side fleet-operations systems ingesting telex/email noon reports; early weather-routing services (service posture); ECDIS-generation bridge systems feeding shore. Satisfies the core.
- **Regional/segment breadth**: the sample is European/Nordic-vendor-weighted (Denmark ×2, Norway, Finland) but the customer base spans Greek management (Technomar, Millenia, Ionic), Japanese (IINO Lines), American (Argenmar), Danish/Norwegian owners (TORM, G2 Ocean), UK (Carisbrooke), Italian (Grimaldi). The definition names no flag state, no trade, no regulation set, no connectivity level.
- **Platform-native check**: no sampled product requires AIS, sensors, or real-time connectivity to satisfy the core; the noon-report-only path is explicitly documented (SERTICA FAQ; StormGeo s-Log manual entries; Wärtsilä SmartLog). → tracking-free, sensor-free form is first-class.

## Uncertainties

1. **StormGeo direct fetch blocked** (403 on www and non-www, 2 attempts, abandoned per network rules). Evidence comes from official stormgeo.com pages via search excerpts: content is official but page-level detail (full FAQs, feature lists) was not captured; StormGeo-specific assertions are held at positioning strength and none of its numbers are promoted beyond L3.
2. **Workboat/tug/ferry and offshore marine-coordination poles not sampled** — no reachable dedicated vendor for small-workboat voyage operations or offshore-wind marine coordination this pass; whether those segments realize this Type or a dispatch/scheduling-shaped sibling is unverified. (helmops.com, probed, is now a yacht-management product.)
3. **Liner/schedule-driven operations pole under-evidenced** — the tramp/charter-party pole dominates the sample (CP machinery in 2/4 products); liner berth-window/schedule-reliability operations appear only indirectly (schedule-reliability wording in SERTICA; a liner customer quote at ZeroNorth). Held as a variant with weaker evidence.
4. **Exact report schemas, alert thresholds, forecast cadences** are product-specific FAQ/marketing facts — recorded at L3, not promoted.
5. **Cruise Operations Platform seam** left as a forward flag (leaf unprocessed).
6. **Kongsberg / Danaos / ABS NS / DNV / BASS remain unreachable** (consistent with the marine-fleet pass) — no claims made about them; the Greek ship-management ERP pole and class-society-vendor pole are therefore absent from this sample too.

## Final Synthesis

Vessel Operations Platform is the vessel operator's voyage-execution system of record. Its defining core is three jointly-held structures: the voyage as a persistent operational record carrying its plan (route, schedule, speed, fuel) and accumulating its execution (positions, reports, events, consumption); the ship–shore operational data loop through which the vessel's voyage data — crew-entered reports (departure/noon/arrival-class) and/or automated onboard acquisition — reaches the office and operational direction (instructions, re-optimisations) flows back to the vessel; and the fleet operations control surface — a continuously refreshed picture of every active voyage against plan, with deviations surfaced as alerts and corrections directed back to the ship. Around that core, mature products add voyage/route/speed optimization with weather integration, performance monitoring and analytics (fuel models, hull/engine condition, benchmarking), emissions and regulatory reporting, charter-party adherence machinery, geofenced alerting, port ETA sharing, onboard bridge planning surfaces, and optional human advisory desks. The Type is realized standalone (optimization-first SaaS), as an operations product line inside ship-management suites, and as OEM platforms bridging bridge systems and shore. It is bounded against Marine Fleet Management (asset administration — the seam both vendor families confirm by shipping both), Ocean Freight Management (cargo business), Port TOS (terminal side), vessel tracking (data layer), and pure weather-routing advisory (service posture). The paper-era ops desk — voyage orders, noon reports, wall chart — satisfies the core with no software, so the definition is era-proof.
