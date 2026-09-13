# Research Notes — EV Fleet Charging Management

## Research Goal

Understand what an "EV Fleet Charging Management" application actually is as an operator-side software type: what its system of record is (vehicles, chargers, or both), what its unit of work is (sessions, schedules, readiness), how it connects to vehicles and chargers, what its daily operational loop looks like, and where it ends relative to the three pre-identified neighbors: Fleet Management System (§18 sibling, processed), EV Charging Network Management (§19 sibling, processed), and EV Charging Billing & Roaming (§19 sibling, processed).

Pre-hung joint-review obligations held in this pass:

1. `fleet-management-system` (processed 2026-09-08, STATUS Boundary Issues): "EV energy/charging and autonomy appear as L2 overlays on the same FMS core (charge monitoring inside a fleet platform), suggesting Variant status; network-scale charging management may still be an independent infrastructure Type — flagged for joint review when those leaves are processed." This pass must discharge the EV half of that flag.
2. `ev-charging-network-management` (processed 2026-09-08): its boundary finding states "Infrastructure operator's chargers are the managed subject here; the fleet operator's vehicles, missions and charging costs are the subject there. Depot CPMS deployments overlap in features (priority charging, depot load strategies) but the organizing subject differs; if the vehicle fleet, not the charger fleet, is the system of record, it is the other Type." This pass must hold that seam symmetrically.

## Initial Boundary

- Hypothesis: this Type is the **fleet operator's side** of EV charging — the vehicles are the managed subject, charging is the operational focus. The CPO side (charger fleet as subject) is the already-processed EV Charging Network Management.
- Nearest neighbors: Fleet Management System (vehicle fleet ops, charging as monitoring overlay), EV Charging Network Management (charger-fleet operations), EV Charging Billing & Roaming (session money), Energy Management System / DERMS / VPP (site/grid energy), Route Optimization / Dispatch (duty plans as inputs), Autonomous Fleet Management (§18 sibling, unprocessed).
- Market category names observed: "Fleet Charging Management" (Nuvve's own product-page title), "EV Fleet Solutions for Charging Management Systems" (Ampcontrol), "EV fleet charging software" (EV Connect), "fleet solutions" inside a charging platform (ChargePoint). Industry shorthand: depot charging management / smart charging for fleets.

## Research Questions

1. What is the system of record — vehicles, chargers, or both? How are vehicles represented (battery, SoC, assignments)?
2. What is the unit of work — a charging session, a charging plan/schedule, or a vehicle's readiness for duty?
3. How does the system connect to vehicles (telematics/OEM APIs) and to chargers (OCPP)? Does it command chargers or only observe them?
4. What does the daily operational loop look like (vehicles return → plug in → schedule → charge → ready → depart)?
5. How do energy constraints enter the model (site power caps, demand charges, time-of-use tariffs, solar/BESS)?
6. What roles exist (depot/charging operations manager, energy manager, driver)?
7. What are the failure modes (vehicle not charging as planned, charger fault, missed departure, connectivity loss)?
8. Where does it end vs FMS (routes, drivers, maintenance), vs CPO charging network management (network serving), vs billing (money), vs energy management (grid)?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer levels:

| Product | Philosophy / pole | Customer level | Evidence tier |
|---|---|---|---|
| Ampcontrol | Pure-play depot charging + energy orchestration ("fleet centric" platform, AI scheduling) | Large depot fleets: logistics (Lidl), transit (AlphaStruxure), school buses (First Student), trucks (WattEV), charging hubs (Revel) | A (product pages + FAQ, operationally detailed) |
| Nuvve (FLEETBOX) | V2G-first: fleet charging + grid services revenue | School buses (K-12), commercial fleets | A (product page) |
| EV Connect (fleet) | Take-home fleet variant: residential chargers + public roaming + reimbursement | Take-home fleet operators (bp pulse co-marketing) | A (product page + FAQ) |
| ChargePoint (fleet) | Incumbent CPO/CMS's fleet offering — charger-network-centric with fleet telematics module | Mixed: company cars, delivery, passenger transport | A (product pages; boundary specimen) |
| Geotab (EV fleet management) | FMS pole: EV overlay = monitoring/insight, no charger control | Any telematics fleet | A (product pages; boundary specimen) |

Rejected/unreachable: The Mobility House (ChargePilot — energy-management-first European vendor; site unreachable ×2), Synop (unreachable ×2), SWTCH fleet page (404), AMPECO (timeout ×2). These are recorded as source limitations; no claims rely on them.

## Sources

Fetched 2026-09-08:

- Ampcontrol — https://ampcontrol.io/ (root), https://ampcontrol.io/products/platform (Platform Overview + FAQ), https://ampcontrol.io/products/vehicle-telematics (EV Telematics Fleet Management System)
- Nuvve — https://nuvve.com/ (root), https://nuvve.com/fleet-charging-management/ (FLEETBOX)
- EV Connect — https://www.evconnect.com/fleet (EV Charging for Take-Home Fleets + FAQ)
- ChargePoint — https://www.chargepoint.com/businesses/fleet (fleet solutions), https://www.chargepoint.com/fleet/software (redirected to platform software page)
- Geotab — https://www.geotab.com/fleet-management-software/ (MyGeotab), https://www.geotab.com/fleet-management-solutions/electric-vehicles/ (EV fleet management)

Sibling research notes consulted (internal): research/fleet-management-system.md, research/ev-charging-network-management.md, research/ev-charging-billing-roaming.md (via STATUS.md summary).

## Product Observations

### Ampcontrol (pure-play depot charging + energy orchestration)

Evidence layer A. Key observations:

- Self-description: "AI-driven charging and energy management system designed to orchestrate electric vehicle fleet operations alongside on-site microgrid assets. Operating as a cloud-based Charge Point Management System (CPMS)... The software automates daily depot workflows, monitors equipment health, prevents grid bottlenecks, and minimizes overall energy expenses by continuously balancing vehicle charging demands with total site power availability." (Platform FAQ)
- **AutoScheduler**: "ingests live operational data—such as vehicle State of Charge (SoC), GPS location, arrival times, and target departure requirements—directly from Transport Management Systems (TMS) or route plan uploads. Using this operational context alongside site energy constraints, AutoScheduler automatically generates and updates individualized charging schedules to guarantee that every vehicle is fully charged for its next assignment." — the clearest single statement of the Type's unit of work: per-vehicle charging schedules oriented to departure/duty.
- Named feature blocks: "Ensure On-Time Departure — smart charging software uses telematics integration and route data"; "Avoid Vehicle Downtime — instant notifications if a vehicle is delayed or shows untypical behavior"; "Reduce Energy Costs — track truck or bus energy consumption"; "Yard Management — allocate vehicle to charger, increase depot throughput"; "Manual Override — allow the ground operator to make ad-hoc adjustments"; "Trickle Charging — avoid vehicle sleep modes by giving minimum power"; "Fail-Safe — avoid unwanted fast-charging even if the internet connection is down"; "Variable Capacity — shift charging to a specific time of the day that reduces costs or peak demand."
- Charger control: "Send real-time commands to charging stations"; OCPP 1.6J/2.0.1 certified (OCA); hardware-agnostic ("tested with over 40 charger manufacturers and 60 models" — marketing number, L3); AC L2, DCFC (CCS1/CCS2), MCS.
- Energy side: Dynamic Load Management (DLM) allocating power across chargers in real time factoring solar, BESS, building meters; peak shaving; demand-charge avoidance; "oversubscription" (site power sold beyond grid capacity); AmpEdge local controller (Modbus/MQTT to BESS/inverters/meters/chargers, offline fallback with local static load management, buffered telemetry).
- Telematics integrations: Geotab, Webfleet, Samsara, Volvo, Scania; open REST API + PubSub event streams.
- Payment & reimbursement module: driver payment app, roaming partners, home charging credits (L2).
- Industries: transport & logistics, transit buses, school buses, ports, rideshare/taxi, food & beverage. Customers: Lidl NL (distribution centers), AlphaStruxure (transit depot microgrid), WattEV (trucks), Revel (public hubs + fleet), First Student (school buses), Electrada (charging-as-a-service).
- Audience list includes Fleet Operator, Solution Company, Utility, Vehicle Manufacturer, Charging Point Operator — the platform is sold to fleet operators first.

### Nuvve FLEETBOX (V2G-first)

Evidence layer A. Key observations:

- Product-page title is literally "Fleet Charging Management — Nuvve FLEETBOX™ — Intelligent electric vehicle monitoring and control."
- "Nuvve's software platform provides the ability to manage and optimize site-level electric vehicles charging and behind the meter solar and battery storage. These hubs can operate as microgrids and/or be aggregated across multiple sites to participate in ancillary and grid services markets. Fleet operators save money, electrify fleets faster and optimize capital asset life."
- "Remotely monitor and manage your electric vehicle (EV) fleet in real-time with the Nuvve FLEETBOX™ web-portal or mobile app. It offers real-time dashboards for vehicles and chargers to allow you to view connectivity status, battery charge level, power flows..."
- "Fully Automated Optimization — Just tell us what your vehicles' schedules are and Nuvve FLEETBOX™, connected to our aggregation platform, will manage the charging for you. We'll make sure that your mobility needs are prioritized while your electricity costs are optimal. This may also include extra revenue if you are using our bidirectional hardware and signed up for our grid services management program (where available)."
- Reading: vehicle schedules are the input; charging is managed automatically; mobility needs prioritized over cost; V2G revenue is an optional extension requiring bidirectional hardware + a grid-services program.

### EV Connect (take-home fleet variant)

Evidence layer A. Key observations:

- Page: "EV Charging for Take-Home Fleets — Simplify EV charging for your take-home fleet drivers while maintaining full visibility and cost control with turnkey solutions that combine premium residential chargers, expert installation and powerful management software."
- "Monitor all home and public charging activity in one intuitive dashboard"; "Track home and public charging in real time... so you know exactly when, where and how much your fleet is charging."
- "Enable En-Route Charging — Give your drivers access to 140,000+ public charging stations... through the EV Connect Network and our extensive roaming partnerships." (number = marketing, L3)
- "Ensure Accurate Reimbursement — With our vehicle recognition technology, you'll always know which car is charging—at home or en route. That ensures you're only paying for your fleet vehicles to be charged." (vehicle recognition = vendor-claimed mechanism, product-specific)
- "Control Energy Costs — Manage when your drivers charge to take advantage of less expensive time-of-use rates and other utility company programs."
- "24/7 Monitoring for Reliable Operations — Intelligent monitoring works around the clock to detect issues early."
- Home chargers arrive "preconfigured for EV Connect Software+™"; installation via Qmerit partner network; driver call-center support.
- Reading: the take-home variant keeps all three core structures — fleet's vehicles as subject (vehicle recognition), charging operation oriented to duty + cost (when drivers charge), control over charging (its own provisioned smart chargers, ToU scheduling) — but the charger estate is distributed residential units plus roaming public access instead of a depot.

### ChargePoint fleet (CPO/CMS incumbent — boundary specimen)

Evidence layer A. Key observations:

- Fleet page: "Manage ICE and electric vehicles through a single dashboard. Monitor vehicle status and charging in real time. Reduce energy costs with automated charging schedules and energy management software. Make informed decisions with comprehensive fleet analytics and insights."
- Platform page (the software core): station management, access groups (employees/visitors/public), dynamic pricing by driver group/session length/energy cost/time of use, Waitlist queues, dashboards/reports/AI Data Assistant, OCPP third-party hardware support, roaming, driver app, building-management and distributed-energy-management integrations.
- Separate "Telematics" module: "Monitor vehicle health and take the guesswork out of managing your EVs."
- Reading: ChargePoint's center of gravity is the charging station network (its CMS: stations, pricing, access, driver app, roaming). The fleet offering wraps that CMS with vehicle dashboard + automated charging schedules + a telematics module. The vehicle fleet appears as a managed population, but the organizing subject remains the charging program/stations. This is the CPO-side shape reaching toward the fleet side — confirms the seam is real and that bundled products ship both centers.

### Geotab (FMS pole — boundary specimen)

Evidence layer A. Key observations:

- MyGeotab core (FMS): vehicle/driver data, tracking, driver behavior, engine health, maintenance, compliance, routes/zones, benchmarking. EV support appears in Pro plan ("engine and accelerometer data as well as EV support").
- EV fleet management page: "Get the most out of your EVs by monitoring and optimizing their use... map overlays, real-time location and state of charge"; "Track EV performance with reports on battery degradation, range capability and energy usage"; "Assign EVs to appropriate routes based on real-world range capability."
- **Monitor EV charging in real time**: "Streamline your EV charging: get notifications when something needs your attention and ensure EVs are charged and ready for their next job. Get notified when vehicles are not charging as planned. Manage a queue of vehicles waiting to charge. Make informed dispatch decisions, based on when vehicles will be done charging."
- "Measure energy consumption... Track energy consumption by vehicle or location. Review charging logs to reimburse drivers who charge at home."
- EVSA (Electric Vehicle Suitability Assessment): electrification planning (which ICE vehicles to replace, cost/CO2 forecasts, model recommendations).
- Reading: Geotab covers the *observational and planning* surface of fleet charging — SoC visibility, not-charging-as-planned alerts, charge queues, home-charging reimbursement logs, electrification planning — but nowhere commands chargers or manages site power. No OCPP charger control, no load management, no charging schedules that execute. This is exactly the "L2 overlay on the FMS core" the FMS pass described. The line between this overlay and the present Type is the control leg.

## Cross-product Comparison

| Capability | Ampcontrol | Nuvve FLEETBOX | EV Connect (take-home) | ChargePoint fleet | Geotab (FMS pole) |
|---|---|---|---|---|---|
| EV fleet as managed population (vehicles with SoC/charging state) | ✓ (SoC, GPS, efficiency per vehicle) | ✓ (battery charge level, connectivity) | ✓ (vehicle recognition; which car is charging) | ✓ (vehicle status + charging dashboard) | ✓ (SoC, battery health, energy use) |
| Charging operation oriented to vehicle duty (schedules vs departure/mobility needs) | ✓ (AutoScheduler vs target departures; on-time departure) | ✓ ("mobility needs prioritized"; vehicle schedules as input) | ✓ (charging fitted to driver/home patterns; readiness implicit) | ✓ (automated charging schedules) | partial (not-charging alerts, charge queues, dispatch decisions — no schedule execution) |
| Executed control over charging (commands chargers / allocates power) | ✓ (real-time charger commands, DLM, trickle, override) | ✓ ("will manage the charging for you") | ✓ (own smart chargers, ToU scheduling) | ✓ (station software load management; automated schedules) | ✗ (monitor + notify only) |
| Charger estate registry (depot/home/public, OCPP or proprietary) | ✓ (OCPP server, hardware-agnostic) | ✓ (site chargers + bidirectional hardware) | ✓ (provisioned home L2 + public roaming) | ✓ (own + OCPP third-party) | ✗ (no charger registry) |
| Telematics/OEM vehicle-data integration | ✓ (Geotab, Webfleet, Samsara, Volvo, Scania) | implied (vehicle dashboards) | partial (vehicle recognition) | ✓ (telematics module) | ✓ (native telematics) |
| Site power / load management | ✓ (DLM, peak shaving, oversubscription, AmpEdge offline) | ✓ (site-level optimization; solar/BESS) | partial (ToU windows for home charging) | ✓ (built-in station load management) | ✗ |
| Energy cost management (tariffs, ToU, demand charges) | ✓ (cost optimization, peak prices) | ✓ ("electricity costs are optimal") | ✓ (ToU rates, utility programs) | ✓ (energy management software) | partial (charging-cost opportunities) |
| Solar / BESS / microgrid orchestration | ✓ (BESS, solar, building meters; microgrid services) | ✓ (behind-the-meter solar + storage; microgrid hubs) | ✗ | partial (distributed-energy-management integrations) | ✗ |
| Readiness / departure assurance | ✓ (named: on-time departure; fully charged for next assignment) | ✓ (mobility needs prioritized) | implicit (fleet readiness) | partial (vehicle status) | ✓ as monitoring (charged and ready for next job) |
| Alerts (vehicle not charging, charger faults, low SoC) | ✓ (Alert Center, low-SoC alerts) | ✓ (connectivity status) | ✓ (24/7 intelligent monitoring) | ✓ (proactive monitoring) | ✓ (not-charging-as-planned notifications) |
| Charging session / energy reporting per vehicle | ✓ (session reports, KPIs per vehicle, cost tracking) | ✓ (power flows, dashboards) | ✓ (when/where/how much; reimbursement) | ✓ (fleet analytics) | ✓ (charging logs, energy by vehicle/location) |
| V2G / grid services | partial (OpenADR cert; microgrid) | ✓ (bidirectional hardware + grid services program) | ✗ | ✗ (roaming ≠ grid services) | ✗ |
| Electrification planning (EVSA/TCO/feasibility) | ✓ (TCO/ROI reports, simulation) | ✗ (funding/financing instead) | ✗ | ✓ (assessments, consulting) | ✓ (EVSA) |
| Driver-facing surface | partial (driver payment app) | ✓ (mobile app) | ✓ (driver support call center; app) | ✓ (driver app/portal) | ✓ (driver app — FMS side) |
| Public-access/payment at chargers | ✓ (payment module, RFID/credit card/Plug&Charge) | ✗ | ✓ (roaming network access) | ✓ (core CMS strength) | ✗ |
| Home-charging reimbursement | ✓ (home charging credits module) | ✗ | ✓ (core of the variant) | ✗ | ✓ (charging logs for reimbursement) |

Reading: the first three rows (fleet population + duty-oriented charging operation + executed control) co-occur in every product that the market itself calls fleet charging management (Ampcontrol, Nuvve, EV Connect) and in the CPO incumbent's fleet wrap (ChargePoint). The FMS pole (Geotab) holds rows 1 and partially 2/3-as-monitoring but fails the control leg — and Geotab does not market itself as charging management. Charger estate, telematics integration, load management, cost management, alerts, reporting are common mature structure. V2G, microgrid depth, electrification planning, public access, home reimbursement are variant/optional.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (minimal)

Three jointly-held structures. Remove any one and the product stops being recognizable as this Type:

1. **The operator's EV fleet as the charging population of record.** Persistent, individually identified vehicles held with their charging-relevant state — battery/SoC, charging status, duty assignments — as the fleet operator's own managed assets. Remove it → charger-network management (the CPO Type, chargers as subject) or a generic fleet register (FMS).
2. **The charging operation as the managed unit of work, oriented to vehicle duty.** Charging is planned and executed per vehicle so the fleet is ready for its assignments — departure times, routes, mobility needs are the requirements the charging must satisfy, with energy cost and site power as constraints to work within (not the goal itself). Remove it → charger operations for the network's sake (CPO Type) or site energy management.
3. **Executed control over the charging itself.** The system acts on the charging process — commands chargers, allocates power across them, starts/stops/shifts charging, manages load — rather than merely observing and alerting. Remove it → the FMS's EV monitoring overlay (observe + notify + plan, no control).

Jointly-held is load-bearing:

- 1 alone = fleet register (FMS territory)
- 2 alone = a charge-planning spreadsheet/tool with nothing executing it
- 3 alone = charger/site control (CPO CMS territory)
- 1+2 without 3 = monitoring/planning overlay (the Geotab pole — still FMS-shaped)
- 1+3 without 2 = depot charger operations with vehicle telemetry but no duty orientation (drifts toward the CPO/depot-CPMS shape)
- 2+3 without 1 = anonymous load management (energy management territory)

The charging session appears here as the fleet's energy-logistics event (per vehicle, feeding readiness and cost), not as a commercial transaction; session money (public tariffs, multi-party settlement, roaming) belongs to EV Charging Billing & Roaming.

### L1 — Common Mature Structure

Present across the researched sample without being definitional:

- **Charger/depot estate registry** — the chargers the fleet operator uses (owned depot chargers, provisioned home chargers, hub chargers), commonly OCPP-connected and hardware-agnostic; identified, grouped by site.
- **Two live integration planes** — charger connection (OCPP-class: status in, commands out) and vehicle-data connection (telematics/OEM APIs: SoC, location, arrival/departure data; TMS/route-plan imports).
- **Smart charging / load management** — site power caps, power allocation across chargers, peak shaving, oversubscription of constrained grid connections, charging-window control.
- **Energy cost management** — time-of-use shifting, demand-charge avoidance, tariff awareness; solar/BESS/building-load orchestration where present.
- **Readiness monitoring & alerts** — charged-by-departure tracking, not-charging-as-planned notifications, low-SoC alerts, charger fault alerts, charge queues.
- **Charging session & energy records** — per-vehicle/per-site session history, energy delivered, cost per vehicle / per mile, feeding reimbursement and reporting.
- **Unified dashboard** — vehicles + chargers + power flows in one operational picture; yard/depot views (vehicle-to-charger allocation).
- **Manual override** — operator ad-hoc adjustment of automated schedules (ground-operator control).
- **Roles** — charging/depot operations manager, energy/facilities manager, driver (notification + support surface).
- **APIs/integrations** — telematics providers, TMS, utilities, energy systems.

### L2 — Variant / Optional Structure

- **Deployment context**: centralized depot (majority pole) vs distributed take-home (residential chargers + roaming + reimbursement) vs public-facing charging hub (adds access control and payment) vs mixed.
- **V2G / grid-services extension**: bidirectional charging, aggregation into grid/ancillary markets — requires bidirectional hardware and a grid-services program (Nuvve pole); seam toward VPP/DERMS.
- **Microgrid depth**: solar, BESS, building meters orchestrated together with charging (Ampcontrol pole); local edge controllers for offline resilience.
- **Electrification planning**: EVSA/TCO/feasibility/charger-sizing tools (pre-operational phase; Geotab EVSA, Ampcontrol TCO, ChargePoint assessments).
- **Home-charging reimbursement machinery** for take-home drivers (EV Connect core; Geotab logs; Ampcontrol credits module).
- **Public access & payment at fleet chargers** (RFID, credit card, Plug&Charge) where depots/hubs serve outside drivers.
- **Compliance/incentive programs**: LCFS-style carbon-credit generation (Ampcontrol module).
- **Charging-as-a-service packaging** (Electrada-class operators running the software for fleet customers).
- **FMS-embedded monitoring overlay** (Geotab-class): the observational slice of this Type shipped inside a fleet platform — a capability, not this Type.

### L3 — Vendor-specific (Research Notes only)

- Ampcontrol: AutoScheduler, AmpEdge (local controller), DLM/SLM terminology, Alert Center, Hardware Diagnostics, "40+ manufacturers / 60 models", "3 million sessions optimized per year", "99.995% uptime", ISO 27001/SOC 2 certifications, LCFS module, Microgrid Services, TCO Calculations.
- Nuvve: FLEETBOX™ branding, grid services management program, bidirectional hardware line, K-12/school-bus focus, funding & financing services.
- EV Connect: Software+™ platform name, vehicle recognition technology, Qmerit installation partnership, Shield™ protection plans, "140,000+ public stations", bp pulse co-marketing, 24/7 call center.
- ChargePoint: CMS Suite, Waitlist, AI Data Assistant, Installer Toolkit, "8K+ connected fleet vehicles", "406K+ activated ports" scale claims.
- Geotab: MyGeotab, EVSA, "300+ EV models", Pro/ProPlus plan gating of EV support, OEM data platform.

None of these may define the Type. Marketing precision (counts, uptime percentages, model counts) deliberately excluded from the final document.

## Vendor-specific Findings

See L3. Additionally:

- Ampcontrol sells to CPOs and utilities as well as fleet operators — the same platform serving multiple audiences; the fleet-operator deployment is the one that instantiates this Type.
- ChargePoint's fleet offering demonstrates a CPO-native vendor reaching toward the fleet side while keeping the station network as the organizing center — evidence that the two Types interlock in bundled products (same pattern as the Driivz/Virta/LMS module splits recorded in the sibling pass).
- Geotab's EV overlay demonstrates a telematics-native vendor covering the observational slice without the control leg — evidence that the FMS/this-Type boundary is the control leg, not the data.

## Boundary Findings

- **vs Fleet Management System (§18 sibling) — JOINT REVIEW DISCHARGED.** The FMS pass hypothesized EV charging might be an L2 variant of FMS. This pass finds two distinct Types with an interlocking seam:
  - FMS core = fleet register + per-vehicle in-service operational record + operator oversight loop over the vehicle's whole service life (usage, maintenance, drivers, compliance, cost). Its EV capability is observational: SoC/range/energy visibility, not-charging-as-planned notifications, charge queues, dispatch decisions, EVSA planning (Geotab directly observed).
  - This Type's core = the charging operation itself as managed work, with executed control over chargers/power and duty-readiness as the goal.
  - Split test: remove charger/charging control → what remains is the FMS EV overlay (Geotab demonstrates it stands alone as a capability). Add the full vehicle-operations span (maintenance, drivers, compliance) → FMS. The two interlock: FMS/TMS hands over schedules, routes, SoC; this Type returns readiness and energy/cost data (Ampcontrol's TMS/telematics ingestion documents the inbound direction).
  - Verdict: keep both as separate Types. The FMS's EV monitoring is a capability overlay, not this Type; this Type is not a variant of FMS because its system of work (charging orchestration under power constraints) has no counterpart in the FMS core.
- **vs EV Charging Network Management (§19 sibling) — seam held symmetrically.** CPO side: charger fleet is the system of record; the goal is the network serving (uptime, utilization, driver sessions); sessions are operational events of the network. This Type: vehicle fleet is the system of record; the goal is duty readiness; charging is the fleet's energy logistics. Depot CPMS deployments overlap in features (priority charging, depot load strategies — the sibling pass recorded this as its L2 seam), but the organizing subject differs. Split test: remove the vehicle fleet as subject → CPO Type; remove the charger network as subject (chargers become merely the actuated estate) → this Type. Bundled products (ChargePoint fleet; Ampcontrol selling to CPOs too) ship both centers as modules/poles.
- **vs EV Charging Billing & Roaming (§19 sibling).** Session money — public tariffs, CDR pricing, multi-party settlement, roaming — is the sibling's center. Here money appears as energy cost management (ToU, demand charges) and take-home reimbursement (cost recovery for the operator), not as session commercialization. EV Connect's reimbursement is the deepest money feature observed here and it is operator-cost recovery, not settlement.
- **vs Energy Management System / DERMS / Virtual Power Plant (§19).** Site power management inside this Type serves vehicle charging (protect the connection, allocate power, fit duty windows). Grid-market participation, DER orchestration, battery dispatch are other Types; V2G aggregation (Nuvve) is an L2 seam explicitly gated on bidirectional hardware + a grid-services program.
- **vs Route Optimization Platform / Dispatch Management (§18 siblings).** Route plans and departure times are *inputs* to this Type (Ampcontrol ingests TMS/route plans); computing them is the other Type. No evidence of this Type computing routes.
- **vs Autonomous Fleet Management (§18 sibling, unprocessed).** Different overlay on the fleet-operations space (autonomy vs energy). Not directly researched here; assertion kept at canonical-inference strength. The FMS pass's flag should stay hung for that leaf's own pass.
- **Remove/keep summary:** remove the vehicle fleet as subject → CPO charging network management; remove charging control → FMS EV overlay; remove duty orientation → site energy management / depot CPMS; add session commercialization → billing sibling; add grid-market dispatch → VPP/EMS territory.

## Historical / Market-Sample Check (§24)

- The Type is young (EV fleets are young), so the check is run against *thin ancestors* rather than old market eras: early depot charging practice — timer/contactor-based charger sequencing on depot circuits, manually tracked vehicle charging state (clipboard/spreadsheet), duty rosters requiring buses ready for morning pull-out — satisfies the abstract core: vehicles as identified charging subjects, charging planned against duty, control executed on the charging (even if electro-mechanical + manual). The modern OCPP/telematics/AI machinery is L1. This is canonical inference (Layer C): no historical product was directly fetched.
- Regional check: the sampled pure-plays span US/EU depots (Ampcontrol: DE/ES/US offices; Lidl NL case), US V2G (Nuvve), US take-home (EV Connect). No regional pattern is load-bearing in the core. European energy-management-first vendors (The Mobility House) were unreachable — recorded as a limitation; the L0 is designed to accommodate an energy-first pole (cost/constraints as first-class inputs) but this is not directly verified.
- Platform-native check: OEM/manufacturer fleet-charging portals (e.g., vehicle-maker charging tools) were not sampled; they would satisfy the L0 if they hold the operator's vehicles with charging state and execute charging against duty. Not verified.

## Uncertainties

1. No help centers / user guides were reachable for any sampled product; all observations rest on product pages and FAQs. All final-document assertions are calibrated to that level — no numeric limits, default timings, exact state names, or protocol message details are claimed.
2. The Mobility House (ChargePilot) and Synop — both frequently cited fleet-charging/depot-energy vendors — were unreachable (×2 each). The energy-management-first and charging-as-a-service poles are therefore under-sampled; the L0's constraint leg (energy cost/power as constraints) rests on Ampcontrol + Nuvve + EV Connect evidence.
3. V2G/grid-services mechanics observed only at product-page level (Nuvve); no operational detail verified.
4. EV Connect's "vehicle recognition technology" (identifying which car charges on a home charger) is vendor-claimed; mechanism not verified; held product-specific.
5. The exact split of duties between this Type and a depot CPMS in bundled products (e.g., a CPO platform running a depot) is a packaging fact; the subject-of-record test is the discriminator, but real deployments may blur it (recorded in Boundary Findings).
6. Take-home fleets' public-en-route charging (roaming) sits close to the billing sibling's roaming territory; here it appears as driver access + reimbursement, held L2.

## Final Synthesis

EV Fleet Charging Management is the fleet operator's system for running the charging of its electric vehicles. Its defining core is three jointly-held structures: the operator's EV fleet as the charging population of record (vehicles held with battery/SoC and charging state); the charging operation as the managed unit of work, oriented to vehicle duty (charging planned and executed per vehicle so the fleet is ready for its assignments, with energy cost and site power as constraints); and executed control over the charging itself (the system commands chargers and allocates power rather than merely observing). Mature products add the charger/depot estate registry, two live integration planes (OCPP-class charger connection; telematics/OEM vehicle data), smart charging and load management, energy cost optimization (ToU, demand charges, solar/BESS), readiness monitoring and alerts, per-vehicle session/energy reporting, unified vehicle+charger+power dashboards, manual override, and driver surfaces. Variants span depot (dominant), take-home (residential chargers + roaming + reimbursement), public-facing hubs, V2G/grid-services extensions, microgrid depth, and electrification planning. The Type is bounded against Fleet Management System (whose EV capability is observational overlay without control), EV Charging Network Management (charger fleet as subject, network serving as goal), EV Charging Billing & Roaming (session money), and EMS/VPP (grid-market dispatch) by its union of vehicle-fleet-as-subject + duty-oriented charging operation + executed charging control.
