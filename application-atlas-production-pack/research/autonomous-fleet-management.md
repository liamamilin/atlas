# Research Notes — Autonomous Fleet Management

Research date: **2026-09-06**
Methodology: `WORKFLOW_v1.1.md` + `WRITING_GUIDE_v1.1.md` (v1.1)

---

## Research Goal

Understand what "Autonomous Fleet Management" actually is as an Application Type: the core objects, the daily operational work, the roles, the state/lifecycle rules, and — critically — the boundary against the sibling leaf **Fleet Management System** (§18), whose research pass flagged this leaf as a probable Variant ("energy/charging and autonomy are L2 overlays on the same core … dedicated leaves likely behave as variants or as separate infrastructure Types"). This pass must resolve that flag with real product evidence.

Also required: boundary against Robot Fleet Management (§16), Mining Fleet Management (§20), Ride-hailing Platform (§18), EV Fleet Charging Management (§18), and the un-leaved "AV development platform" category.

## Initial Boundary (hypothesis before research)

Three possible readings of the leaf name:

1. **Fleet management for autonomous vehicles** — software to operate fleets of self-driving trucks/shuttles/robotaxis (mission dispatch, remote supervision, teleoperation, autonomy health). Sits naturally next to EV Fleet Charging Management in §18.
2. **Autonomous (AI-automated) management of conventional fleets** — marketing usage by traditional FMS vendors. Not the directory's apparent intent given placement.
3. **Teleoperation-as-a-service** — remote driving centers as the management mechanism.

Working hypothesis: reading 1. Open questions: does a distinct application exist (vs FMS applied to AVs), and is the oversight loop's *object* (autonomy execution vs human drivers) enough to make a distinct Type?

## Research Questions

1. What is the unit of work? (mission / load / trailer move / ride) Who executes it?
2. What does the "driver" role become? Remote operator? Attendant? Nothing?
3. What does the oversight loop monitor, and when/how do humans intervene?
4. What vehicle states/lifecycle stages exist (deployment readiness, in-mission, charging, maintenance, safe state)?
5. What rules govern operations (validated operating conditions/lanes, safe states, emergency override, safety case, permits)?
6. How do products integrate with the customer's existing operations (TMS/YMS/warehouse, human-driven legs)?
7. Is the fleet-management software a standalone product, a bundled component of the autonomy system, or an operated service?
8. Boundary tests: vs FMS (remove autonomy execution), vs Robot Fleet Management (remove road-vehicle context), vs Ride-hailing (remove passenger surface), vs AV development platforms (remove operations).

## Representative Products

Selected for market representation + different product philosophies + different customer tiers:

| Product | Philosophy / position | Tier / segment |
|---|---|---|
| Einride (Saga AI) | Full-stack autonomous electric freight operator; named fleet-operations OS (Saga) spanning autonomous + human-driven trucks + charging | Large shippers (Europe/US/Middle East) |
| Aurora | "Driver as a Service" — virtual driver (Aurora Driver) integrated into customer fleets; Command Center + remote assistance | US trucking carriers |
| Kodiak AI | Turnkey autonomy platform (Kodiak Driver + OpsCenter + OnTime + Network) for trucking/defense/industrial missions | Energy/industrial + trucking |
| Outrider | Site-specific autonomous yard operations system (management software + AVs + site infrastructure) | Logistics hubs (CPG/retail/manufacturing/parcel/intermodal) |

Boundary/negative samples (fetched, used only for boundary evidence): May Mobility, WeRide, Zoox (AV technology / rider-facing companies — fleet-ops software not the marketed product), Applied Intuition (AV development platform vendor).

## Sources

Evidence layers: **A** = directly observed on an official source for a specific product; **B** = cross-product commonality; **C** = canonical inference.

Fetched successfully (all official product/marketing surfaces — Tier 2):

- Einride — root — https://www.einride.tech/
- Einride — Saga AI — https://www.einride.tech/saga-ai
- Einride — Autonomous — https://www.einride.tech/autonomous
- Einride — Electric road freight — https://www.einride.tech/freight
- Aurora — root — https://aurora.tech/
- Aurora — Freight — https://aurora.tech/freight
- Aurora — Safety — https://aurora.tech/safety
- Aurora — Newsroom: "The Road Never Sleeps: Aurora's Trucks Go Driverless Day and Night" — https://aurora.tech/newsroom/the-road-never-sleeps-auroras-trucks-go-driverless-day-and-night
- Outrider — root — https://www.outrider.ai/
- Outrider — System — https://www.outrider.ai/system/
- Outrider — Solutions — https://www.outrider.ai/solutions/
- Kodiak AI — root — https://kodiak.ai/
- Kodiak AI — Technology — https://kodiak.ai/technology
- Kodiak AI — Trucking — https://kodiak.ai/industry/trucking
- May Mobility — root — https://www.maymobility.com/ (boundary evidence)
- WeRide — root — https://www.weride.ai/ (boundary evidence)
- Zoox — root — https://zoox.com/ (boundary evidence — rider-facing only)
- Applied Intuition — root — https://www.appliedintuition.com/ (boundary evidence — AV development platform)

Failed / abandoned (per network-restriction rule, 2 attempts each):

- BestMile — https://www.bestmile.com/ and https://bestmile.com/ — transport error ×2 — abandoned. (Historically positioned as fleet-management software for autonomous shuttle fleets; **unverified in this pass**, no claims made.)
- Vay — https://vay.ai/ and https://www.vay.ai/ — transport error ×2 — abandoned. (Teleoperation-as-a-service; **unverified**, no claims made.)

**Source-access Limitation:** none of the sampled products exposes a public help center / user guide for its fleet-operations software (these are enterprise deployments, not self-serve products). All evidence is official product-page level (Tier 2). Consequently: no precise operational parameters (state names, numeric limits, session mechanics, permission matrices) are asserted anywhere; autonomy-state vocabularies are described conceptually.

---

## Product Observations

### Einride — Saga AI (Layer A)

- Platform = four pillars: **Autonomous** (cabless, AI-powered trucks approved for public roads), **Electric road freight**, **Charging**, **Saga AI**.
- Saga: "the operating system which connects the parts and makes them work as one. By continuously collecting data, Saga manages, monitors and optimizes road freight, all powered by AI."
- Saga product highlights: battery health and charging predictions; real-time route planning/management; charging on demand; connected emissions reporting; "smart, automated truck usage"; CO2 monitoring; "track vehicle status"; integrations.
- **Transport Suite**: "The ultimate planning and management software for electric freight. Monitor operations, vehicles, drivers, chargers, emissions, and shipments in one place." **Charging Suite**: "monitor chargers, energy use, emissions, and charging sessions in one place."
- Autonomous page: "Einride's licensed, expert teams continuously oversee autonomous operations via Saga, Einride's AI-powered operating system." Mixed fleets: "cabless autonomous fleets, software, and human-driven electric trucks."
- Deployment path (5 steps): 1 Selecting the right lane ("high-volume, repetitive routes where autonomy delivers…") → 2 Assess & prepare → 3 Validate in simulation → 4 Deploy & integrate → 5 Scale.
- Safety: "living safety case, built to the strictest international standards and independently audited"; SAE Level 4 purpose-built trucks; "full-system redundancy".
- Freight page: end-to-end service "takes care of everything from drivers, routes, trucks, to charging"; Saga connects "shipment, vehicle, charging, and driver data"; planning algorithms process "transportation demand and driver information to vehicle and charging telematics"; "Fleet overview — Whether you want electric trucks, autonomous vehicles or a mix of the two".

### Aurora (Layer A)

- Product = **Aurora Driver** (virtual driver: Side Pods, Center Pod, Onboard Computer) + "Aurora Services" suite. Positioning: "the Aurora Driver integrates the benefits of autonomy into your fleet"; "Driver as a Service" model — haul freight for carriers, later "customers will be able to purchase and operate their own vehicles".
- Fleet visibility: "The suite of Aurora Services provides unprecedented visibility into your fleet — down to individual trucks and road events. The **fleet intelligence** shared by these trucks makes them collectively and automatically smarter about road conditions and traffic patterns."
- **Command Center** (Safety page): "The Aurora Driver safely handles the driving. If the truck or the fleet needs input, our US-based remote assistance team is always ready."
- Safety governance: **Safety Case Framework** (published, GSN-structured), long-form **Safety Report**, SMS audited by TÜV SÜD.
- Night-ops article: HOS contrast — "Human drivers have a 14-hour window to drive a maximum of 11 hours, due to hours-of-service limitations. Aurora's autonomous trucks don't get fatigued and aren't subject to these rules… more than doubling a truck's utilization potential." Validation: collisions recreated in simulation before capability release; "**Crawl, Walk, Run** philosophy… demonstrating consistent performance before expanding the Aurora Driver's capabilities, areas of operations, and scale." Lanes: Dallas–Houston, Fort Worth–El Paso → Phoenix; trailer types: 53' dry vans, reefers, intermodal containers. Earlier phase: "autonomously hauling customer freight at night, with vehicle operators present, for years" → now driverless.
- Customer quotes confirm hybrid model: Werner — "hybrid model of Werner professional drivers and the Aurora Driver"; C.R. England (Kodiak quote, below) analogous.

### Kodiak AI (Layer A)

- Product = **Kodiak Driver** ("combines AI, modular hardware, and offboard services into a single, integrated platform") + modular hardware (**SensorPods** — "field-swappable in minutes… quicker than changing a tire, with no specialized training") + redundant compute/power/steering/braking.
- Trucking page: "Our support service offerings enable you to operate autonomous trucks as part of your fleet." Solution stack: **Kodiak Driver** + **Kodiak OnTime** + **Kodiak Network** + **Kodiak OpsCenter** (fleet-operations software component).
- Utilization framing: "Kodiak AI trucks are able to drive nearly 24/7, stopping only to refuel, receive **self-diagnosed maintenance**, and pick up new loads."
- Human role: "Autonomous technology doesn't eliminate drivers. It complements them… offering them critical roles that allow them to stay close to home while leveraging their experience to drive in the most complicated environments." Commercial network: "partnerships enable access to an extensive network of hubs, providing services and facilitating the **exchange from local human-driven trucks to long-haul automated trucks**." C.R. England: "our valued drivers will take over to interface with customers and consignees at either end of the load."
- Operational safety pillar: "From driver hiring and training to human-machine interface and regulatory compliance… Our **24/7 monitoring** ensures all operations run smoothly, be it inspections, maintenance, or our incident response processes."
- Deployment: **Partner Deployment Program** (6 steps): 360° Discovery → Network and Value Assessment → End-to-End Solution Definition → Fleet and System Integration → Customer Success Definition → Rollout and Scale.
- Industries: trucking, defense, industrial (driverless ops in the Permian Basin for Atlas Energy; triple-trailer hauling).

### Outrider (Layer A)

- Positioning: "Autonomous yard operations" — "Outrider automates yard operations for logistics hubs with an integrated system": **Management software** + **Autonomous vehicles** (electric yard trucks) + **Site infrastructure**.
- Execution: "Outrider's electric autonomous vehicles consistently execute yard tasks, moving trailers between dock doors and parking spots. This includes backing, hitching, and connecting brake lines." 100,000+ autonomous trailer moves.
- Planning: "plans optimal routes for trailer moves and safely navigates around stationary and moving objects, always adhering to the yard's regulations."
- Integration: "The System easily integrates with your existing workflow, allowing you to **dispatch both manual and autonomous yard trucks**. It provides **real-time trailer inventory tracking**, **automatically re-queues moves**, and **requests support when needed**."
- Safety: obstacle monitoring (multiple sensors); "designed to enter a **safe state** when it encounters a potentially hazardous situation"; **emergency override** — "multiple emergency stop buttons in and around the vehicle, the autonomy system can easily be disabled and the vehicle operated manually."
- Support: "Your system and site personnel are backed by Outrider's **24×7 remote monitoring and support**. Using real-time alerts from the system, engineering experts keep your autonomous site operations running smoothly."
- Context (Solutions page): yard ops sit between warehouse operations and over-the-road transport; industries: CPG, retail/eCommerce, manufacturing, package delivery, intermodal rail.

### Boundary samples (Layer A, negative evidence)

- **May Mobility**: AV technology vendor (MPDM autonomy stack); site markets ride-hail technology and partnerships (Lyft/Uber); no fleet-management product surface.
- **WeRide**: AV technology vendor; "WeRide One" platform + product portfolio (robotaxi GXR, robobus, robovan, robosweeper); "Fleet Size 3000+, Public Operation Almost 6 years" — operations exist but the marketed product is the autonomy platform, not fleet-management software.
- **Zoox**: pure rider-facing surface (how to ride, where to ride); fleet operations not publicly documented.
- **Applied Intuition**: AV development platform ("Dana… for building, testing, deploying, and operating intelligent machines"; SDS, Vehicle OS) — development/deployment tooling for autonomy programs, including a mining-fleet-management-system industry page, but not an operator's fleet-oversight application.

---

## Cross-product Comparison

| Dimension | Einride | Aurora | Kodiak | Outrider |
|---|---|---|---|---|
| Named operations software | Saga AI (Transport Suite + Charging Suite) | Aurora Services + Command Center | Kodiak OpsCenter (+ OnTime, Network) | Management software (component of "the System") |
| Fleet composition | cabless autonomous trucks + human-driven electric trucks | autonomy-enabled OEM Class 8 trucks (Volvo/PACCAR) | retrofitted Class 8 trucks (SensorPods) | electric autonomous yard trucks (+ manual yard trucks dispatchable) |
| Unit of work | shipments on selected lanes | loads on highway lanes | loads hub-to-hub; industrial missions | trailer moves between docks and parking spots |
| Who executes | vehicle's autonomy system (SAE L4, cabless) | Aurora Driver (driverless since 2025; earlier with vehicle operators present) | Kodiak Driver (driverless in Permian ops) | vehicle autonomy in mixed-traffic yard |
| Oversight | "licensed, expert teams continuously oversee autonomous operations via Saga" | Command Center; "if the truck or the fleet needs input, our remote assistance team is always ready" | 24/7 monitoring; incident response; inspections | 24×7 remote monitoring and support; "requests support when needed" |
| Dispatch/planning | planning algorithms over demand + driver + vehicle/charging telematics | lanes (fixed routes) | OnTime + Network hubs; exchange human↔autonomous legs | dispatch manual + autonomous trucks; automatic re-queue of moves |
| Vehicle health | battery health, charging predictions, vehicle status | fleet intelligence (shared road events) | self-diagnosed maintenance; field-swappable SensorPods | obstacle monitoring; safe-state design |
| Safety governance | living safety case, independently audited | Safety Case Framework (GSN) + Safety Report + TÜV-audited SMS | 4-pillar SMS + Safety Report | safe state + emergency override → manual operation |
| Deployment methodology | 5-step path (lane → assess → simulate → deploy → scale) | Crawl-Walk-Run; simulation validation before release | 6-step Partner Deployment Program | yard-readiness checklist/whitepaper; rapid site deployment |
| Energy | electric + smart charging infrastructure (Charging Suite) | diesel (fuel-efficiency framing) | diesel | electric |
| Customer integration | end-to-end service (Einride runs the operation) | integrate into customer's freight operations (DaaS) | "operate autonomous trucks as part of your fleet" + support services | integrates into existing yard workflow |
| Human-driven component | human-driven electric trucks in mixed fleets | hybrid model with customer drivers | hub handoffs to human-driven local trucks | manual yard trucks dispatched by the same system |

### What is universal (Layer B)

1. A **fleet of autonomy-operated vehicles** managed as identified units (register with per-vehicle state).
2. **Missions executed by the vehicle's autonomy system** — the unit of work is performed by software, not an in-vehicle human driver.
3. **Continuous central/remote monitoring** of operations (24/7 or equivalent; named ops surfaces in all 4).
4. A **human intervention path** when the vehicle or mission needs input (remote assistance; support requests; emergency override).
5. **Vehicle health & maintenance management**, including vehicle-reported diagnostics (self-diagnosed maintenance; battery health; field-swappable hardware).
6. **Safety governance**: safe-state behavior, override mechanisms, safety management systems / safety cases, incident response.
7. **Integration with the customer's broader operations** (freight/yard workflow; hybrid human-driven legs).
8. **Staged deployment methodology** (assess → validate in simulation → deploy → scale) — every product documents a structured path.
9. **Hybrid human + autonomous operations** in all four samples (human-driven legs persist somewhere in the operation).
10. **Reporting/analytics** over operations (emissions, utilization, fleet intelligence).

### What varies (Layer B/C)

- **Who runs the operation**: vendor-operated end-to-end service (Einride) vs autonomy supplier whose customer operates the fleet with vendor support (Aurora, Kodiak) vs site-system vendor with 24×7 support (Outrider).
- **Mission type & environment**: public-road highway lanes vs closed logistics yards vs (outside sample) passenger districts.
- **Vehicle posture**: purpose-built cabless vs retrofitted OEM trucks vs yard tractors.
- **Energy & charging depth**: charging as a first-class suite (Einride) vs conventional fuel.
- **Intervention mechanism depth**: remote assistance while autonomy keeps driving (Aurora's framing) vs full manual override (Outrider) vs (unverified) full teleoperation.
- **Regulatory regime**: US state-level driverless permits vs EU road approvals (kept generic — not directly researched).

---

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately minimal)

```text
Autonomous fleet register
  (vehicles as individually identified managed units,
   each operated by its own autonomy system)
└── Autonomy-executed missions
  (units of transport work — a load, a trailer move, a ride —
   performed by the vehicle's autonomy system within the
   operating conditions it is validated for)
└── Supervisory oversight & intervention loop
  (a fleet-side role continuously monitors autonomy execution
   and intervenes when the vehicle or mission needs input:
   remote assistance, safe-state recovery, re-queue, pull from service)
```

Three properties. Removal tests:

- Remove the **register** → there is no fleet to manage; only an autonomy stack remains (AV development platform territory).
- Remove **autonomy execution** (humans drive the vehicles again) → the oversight loop re-attaches to human drivers; the product is a Fleet Management System.
- Remove the **supervisory loop** → autonomy running with no management; the product is a vehicle/robot system, not fleet *management*.

Deliberately **excluded from L0** (tested against §24 historical check):

- **Remote assistance / teleoperation as a specific mechanism** — the dominant modern implementation of intervention, but Outrider shows on-site manual override as the safety floor and earlier AV operations used on-board safety operators; the invariant is the *intervention path*, not its mechanism.
- **Validated-operating-condition (ODD) machinery** — inherent to autonomy execution (an autonomy system can only execute where validated) but implemented variously (approved lanes, geofenced sites, weather/time restrictions); folded into the mission property rather than named as a separate object.
- **Charging/energy management** — first-class in electric samples (Einride Charging Suite, Outrider electric yard trucks), absent in diesel samples (Aurora, Kodiak). Variant, not definition.
- **Safety case / SMS artifacts** — universal in the sample but a governance overlay whose form varies by regime; safety *behavior* (safe state, override) is captured in the oversight property; documentation regimes are L1/L2.
- **Hybrid human+autonomous operations, hub handoffs, deployment programs, simulation validation, reporting** — common mature structure (L1), not definitional.

### L1 — Common Mature Structure

- **Mission dispatch & scheduling** — assigning units of work to vehicles under operating constraints; automatic re-queueing (Outrider); planning algorithms over demand/vehicle/energy data (Einride); lane-based load assignment (Aurora, Kodiak).
- **Remote monitoring / operations center** — continuous 24/7 supervision of vehicles and missions (all 4).
- **Remote assistance & intervention** — operator support when the vehicle or fleet "needs input"; support-request mechanics; emergency override to manual operation.
- **Autonomy & vehicle health monitoring** — vehicle-reported diagnostics, sensor/compute health, battery health, self-diagnosed maintenance triggers.
- **Vehicle lifecycle management** — deployment readiness, inspections, maintenance, charging/fueling, field-swappable hardware.
- **Safety management** — safe-state design, obstacle monitoring, SMS/safety-case governance, incident response.
- **Customer-operations integration** — operating AVs "as part of your fleet"; integration with existing freight/yard workflow and systems.
- **Hybrid human + autonomous operations** — human-driven first/last-mile legs, manual vehicles dispatchable by the same system, hub exchange points.
- **Staged deployment & capability expansion** — structured deployment programs; simulation-based validation before release; staged expansion of operating conditions (Crawl-Walk-Run pattern).
- **Reporting & analytics** — utilization, emissions, fleet intelligence, operational reports.

### L2 — Variant / Optional Structure

- **Segment variant**: hub-to-hub highway freight / closed-site yard & terminal operations / passenger robotaxi-shuttle operations / urban delivery / defense-industrial missions.
- **Business-model variant**: full-stack transport operator (vendor runs the operation) vs autonomy supplier with fleet-integration services (customer runs the fleet) vs site-automation system vendor.
- **Vehicle posture**: purpose-built cabless vehicles vs retrofitted OEM trucks vs electric yard tractors.
- **Energy variant**: electric fleets with charging-infrastructure management vs conventional fuel.
- **Human-role mix**: remote assistance only / on-board safety operators during rollout / on-site attendants / hybrid human-driven legs / (full teleoperation — unverified in this sample).
- **Regulatory regime**: US state-level driverless permits vs EU road approvals; permit and reporting specifics not directly researched.

### L3 — Vendor-specific (Research Notes only)

- Einride: Saga AI, Transport Suite, Charging Suite, Smartcharger stations, cabless pod truck design, "5.2 million data points per second", Fraunhofer/REWE TCO study, IonQ quantum-optimization partnership, 85%/54% planning-efficiency claims.
- Aurora: Aurora Driver 2, FirstLight FMcw lidar (450 m+ range claims, "34-second advantage"), Command Center, Safety Case Framework (GSN), TÜV SÜD SMS audit, Crawl-Walk-Run, Dallas–Houston / Fort Worth–El Paso–Phoenix lanes, trailer-type list, I-45 collision-recreation study.
- Kodiak: Kodiak Driver, SensorPods, OpsCenter, OnTime, Network, Partner Deployment Program (6 named steps), 20,000+ mile commercial network, Atlas Energy Permian driverless operations, triple-trailer hauling, AMD compute collaboration, PRA risk quantification.
- Outrider: "the System" (software + AVs + site infrastructure), 100,000+ autonomous trailer moves, yard design checklist & 3Ps whitepaper, emergency-stop button placement, Bishop Consulting quote.
- None of these enter the final document except as neutral examples.

---

## Vendor-specific Findings

- Einride is the only sampled vendor that *operates* the whole transport service end-to-end (drivers, routes, trucks, charging) — a business-model posture, not a Type property.
- Aurora explicitly frames its product as "driver capacity" sold into customer fleets (DaaS) — the fleet-management surface (Aurora Services / Command Center) is the support layer around that.
- Kodiak names its operations software (OpsCenter) as one component of a four-part solution — the clearest "fleet-ops software as a named product component" evidence in the sample.
- Outrider is site-scoped: its "fleet" is the yard trucks of one logistics hub, and its management software dispatches manual and autonomous vehicles together — the strongest evidence that the oversight loop can span mixed human/autonomous fleets.
- Aurora's remote *assistance* framing (autonomy keeps driving; humans answer questions/inputs) contrasts with full-teleoperation services (Vay — unverified); intervention depth is a spectrum, not a standard.

## Boundary Findings

- **vs Fleet Management System (§18 sibling; resolves the flag from research/fleet-management-system.md)**: the two Types share a substrate — fleet register + per-vehicle operational record + oversight loop — and the prior FMS pass hypothesized this leaf might be an L2 overlay on that core. This pass finds the overlay reading is only half right: the *substrate* is shared, but the **object of oversight changes structurally**. In FMS, vehicles are driven by human drivers; management centers on drivers (behavior, hours-of-service, assignment, licensing) and the oversight loop acts by scheduling service and assigning people. In AFM, vehicles drive themselves; management centers on autonomy execution — mission dispatch under validated operating conditions, remote supervision, intervention when autonomy needs input, safe-state recovery — and the "driver management" module is replaced by remote-operator supervision plus autonomy-performance and safety-case governance. Removal test: replace autonomy execution with human drivers → FMS; remove the register → autonomy stack; remove the supervisory loop → unmanned autonomy, not management. **Verdict: distinct sibling Type sharing the FMS substrate** — same family pattern as Robot Fleet Management generalizing the register+oversight skeleton to a different execution model. Flag resolved; no taxonomy change.
- **vs Robot Fleet Management (§16 sibling)**: same family pattern (register + executed tasks + oversight) for non-road robots (AMRs, arms, drones). AFM carries road-traffic specifics: public-road permits, mixed traffic, highway speeds, passenger interaction. Different Types; joint awareness when that leaf is processed.
- **vs Mining Fleet Management (§20 sibling)**: autonomous haulage trucks in mines satisfy the same L0 pattern, but the leaf carries mine-site specifics (pit operations, haul profiles, dispatch systems). Related Type; the road-vehicle AFM core does not capture mine-site operations.
- **vs Ride-hailing Platform (§18 sibling)**: passenger-facing booking/matching/dispatch vs operator-facing fleet oversight. A robotaxi operator typically runs both surfaces; the passenger app is a different Type. Robotaxi fleet-ops software was not directly documentable in this pass (see Uncertainties) — the passenger-ops variant is described at canonical-inference strength.
- **vs EV Fleet Charging Management (§18 sibling)**: consistent with the FMS pass — charging appears as a module inside the fleet platform when the fleet is electric (Einride Charging Suite; Outrider electric yard trucks). Network-scale charging infrastructure management remains a separate infrastructure concern.
- **vs Trucking Management System / Yard Management System (§18/§10 siblings)**: TMS/YMS manage the freight business and the yard space; AFM manages the autonomous vehicles and their missions. Kodiak's hubs and Outrider's yard integration show the integration seam: the AFM consumes/feeds business systems but its object of work is the autonomous fleet.
- **vs Vehicle Telematics Platform (§18 sibling)**: telematics is the data-acquisition layer; AFM is the operations application over autonomy execution. Same relationship as FMS↔telematics in the prior pass.
- **vs AV development platforms (no directory leaf; Applied Intuition observed)**: tooling for building/validating autonomy (simulation, toolchains, vehicle OS) vs operating deployed fleets. Simulation appears in both (Einride "validate in simulation", Aurora's simulation pipeline) but in AFM it is a deployment-gate step, not the product. Different Types; no directory conflict.
- **Naming-collision note**: "autonomous fleet management" can be misread as "AI-automated management of conventional fleets". In the researched market the term maps to operating autonomous-vehicle fleets; no sampled traditional-FMS vendor was observed using the term for AI-automated FMS. Recorded as a naming note; no taxonomy change.
- **"去掉什么就变成另一个 Type" 判据**: remove autonomy execution (humans drive) → FMS; remove the fleet register → autonomy stack / AV development platform; remove the supervisory-intervention loop → unmanned autonomy system, not management; remove the road-vehicle context → Robot Fleet Management; remove the operator side (passenger-facing only) → Ride-hailing Platform.

## Historical / Market-Sample Check (§24)

- The Type is young (commercial driverless operations ~2024–2026 in the sample). Older analogues: factory AGV systems, airport automated people movers, and automated mining haulage — all satisfy the L0 pattern (autonomy-executed missions + supervisory control) without modern cloud remote-assistance machinery. → L0 survives the historical check.
- Platform/regional check: automated-mining haulage (Caterpillar/Komatsu class) fits the pattern but lives under the Mining Fleet Management leaf; European shuttle deployments (BestMile lineage — unverified this pass) would fit the same core. The L0 does not depend on US regulatory specifics.
- The sample is entirely current-generation AV companies; no "legacy" AFM exists. The historical check is therefore canonical inference (Layer C), not direct observation.

## Uncertainties

1. **Passenger robotaxi/shuttle fleet-ops software not directly documented**: Zoox is rider-facing; May Mobility and WeRide market the autonomy stack; Waymo not fetched. The passenger-operations variant is reasoned at canonical-inference strength only.
2. **BestMile and Vay unreachable** (transport error ×2 each, abandoned per network rules): the "standalone AV fleet-management software vendor" shape and the "teleoperation-as-a-service" shape are under-sampled; no claims made about either.
3. **Fleet-ops software is always bundled or operated**: in every sampled product the management surface ships as a component of the autonomy system or as a vendor-operated service. Whether a standalone, autonomy-agnostic AFM product category exists is unverified (BestMile would have been the test case).
4. **Autonomy-state vocabularies** (engaged/disengaged/minimal-risk-condition etc.) not directly observed on official pages; described conceptually only.
5. **Regulatory mechanics** (permits, disengagement reporting, incident-notification duties) not directly researched; kept generic in all documents.
6. **Intervention-mechanism spectrum** (remote guidance vs teleoperation) evidenced only at the "remote assistance" and "manual override" endpoints; middle forms unverified.

## Final Synthesis

Autonomous Fleet Management is the operator-facing application for running a fleet of self-driving vehicles. Its defining core is small: a register of autonomy-operated vehicles; missions executed by the vehicles' own autonomy systems within the conditions they are validated for; and a supervisory loop in which fleet-side staff continuously monitor that execution and intervene — remote assistance, safe-state recovery, re-queue, pull from service — when the vehicle or mission needs input. Everything else that makes modern products distinctive — mission dispatch under lane/geofence constraints, 24/7 remote operations centers, vehicle self-diagnostics and field-swappable hardware, safety cases and staged capability expansion, charging infrastructure management, hybrid human-driven legs, and customer-operations integration — is mature structure layered on that core, varying by segment (highway freight, closed yards, passenger districts), business model (vendor-operated vs customer-operated with vendor support), and energy posture. The Type shares its substrate with Fleet Management System but is distinguished by who executes the work: when the driver is software, driver management becomes remote supervision, dispatch becomes mission orchestration under autonomy constraints, and the safety regime becomes autonomy safety governance. That difference is structural, not cosmetic — it changes the objects, the roles, the states, and the rules — so the leaf stands as a distinct sibling Type, resolving the variant hypothesis recorded in the FMS pass.
