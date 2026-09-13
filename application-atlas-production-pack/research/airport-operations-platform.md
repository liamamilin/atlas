# Research Notes — Airport Operations Platform

Research date: 2026-09-06
Slug: `airport-operations-platform`
Directory leaf: "Airport Operations Platform" (Section 18 Transportation, Mobility & Logistics)

---

## Research Goal

Understand what software the *airport operator* (and the airport operational community) uses to run the airport's own day-to-day operations: the airport's flight picture, the allocation of the airport's physical operational resources (stands/gates, terminal positions, baggage systems), real-time status management, and coordination among airlines, ground handlers and ATC-adjacent stakeholders. Produce a vendor-neutral model of this Application Type.

## Initial Boundary (working hypothesis before research)

- Core use hypothesis: the airport-side counterpart to airline operations systems. The unit of organization is the airport, not an airline network. Flights are observed as movements *at this airport*; the scarce objects are the airport's own physical resources.
- Likely users: airport operations control center staff, duty managers, airside/apron and terminal operations staff; secondarily airline station staff and ground handlers as consumers of the shared picture.
- Likely adjacent Types: Airline Operations Platform, Ground Handling Management, Flight Planning Application, Airline Reservation / Passenger Service System, Air Cargo Management, Port Terminal Operating System, Public Transit Operations Platform.
- Known market vocabulary expected: AODB (Airport Operational Database), Resource Management System (RMS), FIDS (Flight Information Display System), A-CDM (Airport Collaborative Decision Making), turnaround, stand/gate allocation.
- Unknowns: exact module structure; whether stakeholder information sharing is definitional or only common; how flight data arrives; precise A-CDM content; how far these platforms extend into ground handling.

## Research Questions

1. What does the system treat as a "flight" from the airport's perspective (schedule, leg, operational times, actuals)?
2. Which physical resources are allocated to flights, and how (rules, daily/seasonal planning, scenario planning)?
3. What is the operational-day loop (plan → day-of-operations monitoring → adjustment → post-operation)?
4. What statuses, event times, predictions and alerts does the system track, and who consumes them?
5. How is information shared with airlines, handlers and ATC, and is sharing definitional or common?
6. What surfaces exist (control-room views, allocation boards, FIDS output, partner portals, admin)?
7. Where is the boundary vs airline operations, ground handling systems, flight planning, ATC systems, and FIDS-only products?

## Representative Products

Selected (market representation + reachable official documentation + different philosophies + different layers):

| Product | Vendor | Why selected | Evidence strength |
|---|---|---|---|
| SITA Airport Management (Operations Manager, Fixed Resource Manager, Mobile Resource Manager, CDM modules) | SITA | Large incumbent; suite philosophy; explicitly positioned around shared real-time data, flight operations, fixed+mobile resources, CDM | A (official product/module pages) |
| ARINC AirPlan (Airport Database & Resource Management) | Collins Aerospace | Large incumbent; AODB+RMS packaged as one product; predictive data (FlightAware) integration; named admin tasks (billing, staff scheduling) | A (official product page) |
| CORTEX Apron (Apron Management System: Apron Manager, Apron 360, Apron FOD, RIDS) | ADB SAFEGATE | Different philosophy: sensor/apron-centric turnaround management vendor; used as boundary sample rather than full platform sample | A (official product pages) |

Rejected / not usable as samples (recorded per workflow escalation rules):

- **Amadeus Airport Operations** — blocked by bot protection on two attempts (industry-recognized major vendor; excluded → noted as source-access limitation; no memory-based claims made about it).
- **AeroCloud** — transport errors on both root attempts (cloud-native mid-market candidate; excluded).
- **Zafire (FirstFlight)** — timeouts (mid-market candidate; excluded).
- **Skyplan** — reachable, but on inspection is a flight-planning / trip-support service provider (airline/trip-support side). Product mismatch; used only as boundary context (see Boundary Findings).
- **Eurocontrol A-CDM pages** — 404 on two URL attempts; A-CDM concept content therefore only used as reported through vendor pages (SITA, ADB), not from the authority source.

## Sources

| # | Source | URL | Status |
|---|---|---|---|
| 1 | SITA — Operations at Airports (solution overview) | https://www.sita.aero/solutions/sita-at-airports/sita-operations-at-airports/ | fetched 2026-09-06 |
| 2 | SITA — Airport Management (product page) | https://www.sita.aero/solutions/sita-at-airports/sita-operations-at-airports/sita-airport-management/ | fetched 2026-09-06 |
| 3 | SITA — Operations Manager (module page) | https://www.sita.aero/solutions/sita-at-airports/sita-operations-at-airports/sita-airport-management/sita-operations-manager/ | fetched 2026-09-06 |
| 4 | SITA — Fixed Resource Manager (module page) | https://www.sita.aero/solutions/sita-at-airports/sita-operations-at-airports/sita-airport-management/sita-fixed-resource-manager/ | fetched 2026-09-06 |
| 5 | SITA — Collaborative Decision Making (module page) | https://www.sita.aero/solutions/sita-at-airports/sita-operations-at-airports/sita-airport-management/sita-collaborative-decision-making/ | fetched 2026-09-06 |
| 6 | Collins Aerospace — Airport Database & Resource Management (ARINC AirPlan product page) | https://www.collinsaerospace.com/what-we-do/industries/airports/airport-operations/airport-database-and-resource-management | fetched 2026-09-06 |
| 7 | ADB SAFEGATE — Apron Management System (CORTEX Apron) | https://www.adbsafegate.com/products/apron/apron-management-system/ | fetched 2026-09-06 |
| 8 | ADB SAFEGATE — corporate/solution root (Airside 4.0 framing) | https://www.adbsafegate.com/ | fetched 2026-09-06 |
| 9 | Skyplan — root (mismatch check) | https://www.skyplan.com/ | fetched 2026-09-06 |

Source-access limitations:
- Amadeus official pages unreachable (bot check). AeroCloud, Zafire, Amorph unreachable. Eurocontrol concept pages 404.
- SITA Airport Management brochure PDF exceeds fetch size limit (5 MB); only HTML pages used.
- Consequence: no numeric capacities, timings, limits, or milestone lists are asserted anywhere below unless directly present in a fetched source. Claims rest on the three reachable vendors only; single-vendor findings are marked as such.

---

## Product observations

### SITA Airport Management (vendor: SITA)

Key observations (evidence layer A unless noted):

- Solution cluster "Operations at Airports" contains: AirportVision Evolved (flight information display platform), **Airport Management** (the ops platform), Passenger Information, Airside Optimizer. FIDS is a *separate sibling product*, i.e., display output is outside the ops platform proper.
- Positioning sentence: "helps airport stakeholders efficiently manage flight operations, optimize fixed and mobile resources as well as facilitate collaborative decision making"; "single source of data in real time across your operations"; supports multi-airport operations; 190+ airports claimed.
- **Operations Manager** module:
  - "receiving, processing, and distributing consolidated data, providing a consistent view of operations in a complex multi-user environment".
  - Explicitly contrasted with "traditional Airport Operational Databases (AODBs) that offer basic flight movement tracking": Operations Manager "also manages the quality and accuracy of the movement information", using the "most confident" source at a given time; users validate data and "manage and resolve the conflict between concurrent users and calculations".
  - Real-time configurable KPIs; "act on alert capability" ("Deliver information proactively to avoid domino effects… early decisions make for better decisions"); "most accurate and reliable single point of truth" for all stakeholders incl. IROPS (irregular operations) response.
- **Fixed Resource Manager** module: "scheduling, capacity planning, and resource management"; "manage resources to handle operational flight planning, daily scheduling, and post-operation processes"; "Multi-rule and variable configuration"; "Fully integrated planning for day of operations" with "a real-time view of the apron, resource usage, and availability statistics"; "Scenario-based planning and capacity management" via "'what if?' simulations in a sandboxed environment"; "simple color-coded action boards" and "one-click decision support".
- **Mobile Resource Manager** module: "management of mobile resources for ground handling and capacity planning"; optimization algorithms; personnel management; turnaround management.
- **Collaborative Decision Making** module: "integrated CDM platform that provides shared, accurate information… better On-Time-Performance (OTP)"; "A-CDM concept element support"; "Pre-departure sequencing" (runway/pad capacity, engine-start-to-departure); "Departure Manager for ATC sequencing" ("Reduce ATFM Slot wastage… sequence the exact order for take-off").
- Disruption framing: "Unexpected events like weather, flight cancellations, or geopolitical events can disrupt the whole ATI ecosystem… robust mitigation plans to minimize the impact of irregular operations".

Cross-cutting reading: SITA's structure = flight data core (with quality arbitration) + fixed resource allocation + mobile resource allocation + collaboration/sequencing layer; FIDS as adjacent output product.

### ARINC AirPlan (vendor: Collins Aerospace)

Key observations (evidence layer A):

- Named category on the page: "An all-in-one **Airport Operational Database (AODB) and Resource Management System (RMS)**, AirPlan can be configured with multiple rules to meet your specific business requirements." This is direct vendor evidence that the Type is described in the market as AODB + RMS.
- "AirPlan gives you full visibility of all your airport resources in real time – across one dashboard. Manage **gates, check-in areas and baggage systems** more efficiently, while using enhanced data sources and integration tools to **power flight screens, manage security checkpoints, streamline alerts** and simplify administrative tasks, such as **billing and staff scheduling** – on a daily basis or by season."
- "A single source of truth for sharing data collaboratively"; "Faster turnarounds; more accurate ETAs"; "Improved resource scheduling; better billing data"; "More time for mitigating irregular operations".
- Data formats: "Support for Type-B, AFTN, AIDX and other message formats" (industry message standards for flight data exchange).
- Predictive layer (via FlightAware Foresight / Firehose feeds): machine-learning predictions of gate-arrival and runway-arrival times ("IN/EIBT", "ON/ELDT") and taxi-out duration between gate departure and runway departure ("OUT/AOBT", "OFF/ATOT"); "Taxi-Out predictions are continually updated… providing awareness to things like blocked stands".
- Permissions: "A granular permission system lets you grant access to features as needed"; "Personalized views, reports, and access".
- Integrations: third-party flight/weather tracking; sibling Collins products (AirVue FIDS, MUSE passenger processing, VeriPax).
- Operational context framing: "the way airports, airlines and ground crews carry out day-to-day operations… from the curbside to the runway".

Cross-cutting reading: Collins structure = AODB (flight data core) + RMS (stands/gates, check-in, baggage, security) + feeds/predictions + outputs (FIDS) + admin (billing, staff scheduling, permissions).

### CORTEX Apron (vendor: ADB SAFEGATE) — boundary sample

Key observations (evidence layer A):

- ADB SAFEGATE's core business is airside hardware/systems (airfield lighting, docking guidance, tower systems, weather sensors) — not a full airport ops platform. Its "Apron Management System" (CORTEX Apron) is "a holistic, intelligent approach to managing apron activities from landing to takeoff… optimize taxiing, docking and pushback procedures and improve the efficiency and elasticity of ground handling operations".
- **Apron Manager**: "the natural intelligent hub for controlling, merging, storing, analyzing and predicting for operational performance… provides situational awareness to all stakeholders involved in the aircraft turn."
- **Apron 360**: "Monitor and manage all aircraft turnaround activities from landing to take off… uses an agnostic approach to data gathering… to predict events and create recommendations to mitigate irregularities and avoid disruptions."
- **RIDS (Ramp Information Display System)**: "integrates with airline and airport systems to communicate real-time, critical flight information to flight and ground crew to support airport collaborative decision making (A-CDM) on the apron."
- **Apron FOD**: sensor-based foreign-object-debris detection (hardware-coupled, AI + sensors).

Cross-cutting reading: confirms (1) the *turnaround* as the operational unit of airside ground activity, (2) prediction/recommendation and stakeholder situational awareness as shared goals, (3) the porosity between airport ops platforms and turnaround/apron management systems. ADB does not evidence terminal resource planning (check-in/baggage) or flight-data core ownership — that absence is itself boundary-relevant.

### Mismatch / rejected sample notes

- **Skyplan**: service provider for flight planning, trip support, fuel, permits, dispatch — the *airline/operator trip-support* world. Directly useful as a boundary contrast: flight planning happens before the aircraft ever reaches the airport's operating day and does not allocate airport resources. Its inclusion in "Flight Planning Application" leaf territory confirms that leaf is a different Type.
- **Amadeus**: acknowledged major vendor of airport operations software; unreachable in this environment. No claims made about its product structure.

---

## Cross-product Comparison

| Dimension | SITA Airport Management | Collins AirPlan | ADB CORTEX Apron | Classification |
|---|---|---|---|---|
| Airport-scoped flight picture with live updates | Operations Manager: consolidated flight movement data, quality-managed, single point of truth | AODB: flight data core with FlightAware feeds | Apron 360/Apron Manager: flight and turnaround activity monitored landing→takeoff | Shared by all three → **defining** |
| Allocation of airport physical resources to flights | Fixed Resource Manager (multi-rule config, daily scheduling, what-if scenarios); Mobile Resource Manager | RMS: gates, check-in areas, baggage systems; rule-configured; daily/seasonal | not evidenced (no terminal/fixed-resource planning) | Shared by both platform vendors; absent in apron-only sample → **defining for the platform, and the absence marks the apron product as adjacent** |
| Day-of-operations management loop | operational flight planning → daily scheduling → post-operation processes | daily basis or by season; alerts; real-time adjustments | turnaround monitoring + recommendations | Shared → **defining loop** |
| Single shared operational picture across stakeholders | "single point of truth"; CDM module; multi-user consistency | "single source of truth for sharing data collaboratively" | "situational awareness to all stakeholders involved in the aircraft turn" | Shared by all three, but small/older deployments may be internal-only → **common mature structure, expected but not definitional** |
| Alerts / KPIs / disruption handling | KPIs, act-on-alert, domino effects, IROPS | alerts, irregular-operations mitigation | recommendations to mitigate irregularities | Shared → **common** |
| Predicted operational times | (prediction implied via CDM sequencing; explicit ML claims not made on fetched pages) | explicit ML ETA/taxi predictions (FlightAware) | "predict events and create recommendations" | Shared intent, differing depth → **common** |
| CDM / sequencing exchange with ATC | A-CDM elements, pre-departure sequencing, Departure Manager for ATC sequencing | not evidenced on fetched page | RIDS "support A-CDM on the apron" | Common in European/CDM context → **variant-flavored common (regime-dependent)** |
| FIDS as output | separate sibling product (AirportVision Evolved) | "power flight screens" via integration | RIDS displays on ramp | Universal as *output surface*, not core → **common integration** |
| Admin modules: billing, staff scheduling | not evidenced on fetched pages | evidenced ("billing and staff scheduling", "better billing data") | not evidenced | Single-vendor → **optional/variant** |
| Granular permissions | multi-user environment with concurrent-user conflict resolution | "granular permission system"; personalized views | not evidenced | Common problem; specifics single-vendor → **common (structure), detail product-specific** |
| Data exchange standards (Type-B, AFTN, AIDX) | implied via consolidated feeds (standards not named on fetched pages) | named explicitly | "agnostic approach to data gathering" | Single-vendor naming → **implementation substrate (L2)** |
| Sensor hardware coupling (docking guidance, FOD) | not evidenced | not evidenced | core business | Single-vendor → **vendor-specific to apron variant** |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

An Airport Operations Platform is the airport operator's operational system of record that provides:

1. **Airport-scoped operational flight picture** — the scheduled flights that will arrive at / depart from *this* airport, kept current with live operational updates and event times as the day progresses (planned vs actual/predicted).
2. **Flight-to-resource allocation over the airport's own operational resources** — stands/gates and other fixed or mobile operational assets exist as allocable objects and are bound to flights over time windows, under configurable allocation rules.
3. **Real-time day-of-operations management** — operations staff monitor the flight picture and allocations, receive alerts on deviations, and adjust both during the operating day, with the day's outcome recorded (post-operation).

Test: remove (1) → it is not about this airport's flights at all (becomes a generic scheduling or tracking tool). Remove (2) → per SITA's own contrast, it collapses into "basic flight movement tracking" / a flight-information feed, not an operations platform. Remove (3) → it is a schedule database, not an operations tool. All three are required for the Type to be recognizable.

Historical check (per §24 reasoning): "traditional AODBs" described by SITA as offering "basic flight movement tracking" still sat at the center of the airport's flight picture + allocations + day-of-ops management, even without CDM modules, ML predictions, or stakeholder portals. Older/regional products therefore still fit L0. Modern market features (shared community picture, predictions, mobile resource optimization) are not needed for recognition.

### L1 — Common Mature Structure

Very common in mature modern products; not part of the definition:

- **Shared single operational picture** across airlines, ground handlers and the airport ("single source of truth" in both platform vendors' own words).
- **Alerting and KPI monitoring** with configurable indicators; disruption (IROPS) support framing.
- **Predicted operational times** (arrival/taxi/departure estimates) feeding resource decisions.
- **Turnaround as an operational unit** — the ground activity window per aircraft stop, monitored/managed (SITA Mobile Resource Manager; ADB Apron 360).
- **Scenario/what-if planning and capacity management** around the allocation.
- **FIDS integration** as the standard output surface (either as sibling product or integration).
- **Pre-departure sequencing / departure sequencing** support where collaborative decision-making applies.
- **Multi-airport (group) operation** support.

### L2 — Variant / Optional Structure

Depends on region, scale, regime, deployment:

- **Regulatory/regional CDM regimes** (A-CDM elements evidenced; depth varies by region).
- **Data-exchange substrate**: industry message standards (Type-B, AFTN, AIDX named by one vendor), flight-data feeds, sensor feeds.
- **Administrative extensions**: billing of airlines/handlers based on movements and allocations; staff scheduling; named by one vendor.
- **Mobile-resource optimization depth** (ground-handling workforce/equipment optimization — overlaps toward Ground Handling Management).
- **Deployment posture**: on-premise vs cloud/hosted; managed-service framing (service-excellence monitoring described by one vendor).
- **Airport scale variants**: hub vs regional; single airport vs multi-airport groups.
- **Apron/airside sensor coupling** (docking guidance, FOD detection) — present in the apron-management variant.

### L3 — Vendor-specific Structure (research notes only)

- SITA module names: Operations Manager ("most confident source" arbitration of conflicting flight data; color-coded action boards; one-click decision support), Fixed/Mobile Resource Manager, Departure Manager for ATC sequencing, AirportVision Evolved.
- Collins naming and bundling: ARINC AirPlan; FlightAware Foresight/Firehose integration with named IATA event abbreviations (IN/EIBT, ON/ELDT, OUT/AOBT, OFF/ATOT); integration with AirVue (FIDS), MUSE, VeriPax; 30–50% accuracy claims for predictions (marketing claim, not independently verified).
- ADB naming: CORTEX Apron, Apron 360, Apron FOD, Safedock A-VDGS, RIDS.
- Vendor scale claims (190+ airports, 150+ deployments, 3,000+ airports as customers) — marketing figures, not used in the final document.

## Vendor-specific Findings

- The "most confident source" data-quality arbitration for conflicting flight information is documented only by SITA (product-specific emphasis of a general problem: multiple feeds and concurrent users produce conflicts).
- Billing and staff scheduling as explicit administrative capabilities documented only by Collins.
- Named message-format support (Type-B, AFTN, AIDX) documented only by Collins.
- ML taxi/ETA prediction productization documented only by Collins (FlightAware).
- Sensor-coupled apron management (docking guidance, FOD detection) is ADB's model.

## Boundary Findings

- **vs Airline Operations Platform**: an airline ops system centers on *one carrier's* network — its fleet, crews, OCC, disruption recovery across airports. An airport ops platform centers on *one airport's* infrastructure serving *all* carriers. Test: remove the airport's own physical-resource allocation and re-scope the flight picture to a single airline's network → airline operations. The shared boundary surface is the flight's operational times (both sides track the same flight differently).
- **vs Ground Handling Management**: handler systems manage contracted service delivery (service orders per flight, staff/equipment rosters, service records, billing to carriers). Airport platforms allocate *airport-owned* resources and coordinate. The boundary is porous in modern products: SITA's Mobile Resource Manager optimizes "mobile resources for ground handling", and ADB's apron suite manages turnaround execution — evidence that turnaround coordination is a shared zone. Test: remove the airport infrastructure/flight-picture core and keep per-flight contracted service delivery → Ground Handling Management.
- **vs Flight Planning Application**: flight planning (routes, fuel, permits, dispatch — Skyplan sample) belongs to the airline/trip-support world before the operating day; no airport resources exist in that world. Test: no airport-scoped resource allocation → not this Type.
- **vs FIDS / display products**: both platform vendors treat flight displays as output surfaces (sibling product at SITA; integration target at Collins; RIDS on the ramp at ADB). A display-only product consumes the picture; it does not maintain the picture or allocate resources. Test: consume-only flight data + public displays → narrower display Type.
- **vs ATC/Tower & ATFM systems**: movement-area control (runways, taxiways, sequencing, slots) is the ANSP's domain; SITA's Departure Manager is explicitly positioned "for ATC sequencing" — i.e., the airport platform *exchanges* sequencing intent with ATC but does not control the movement area. Test: authority over runway/taxi movement → ATM, not this Type.
- **vs Port Terminal Operating System**: structural analog across modes (vessel↔berth↔container vs flight↔stand↔baggage) but different domain objects, stakeholders and rules; the analogy should not be read as sameness.
- **Observation on the directory**: "Airport Operations Platform" is a coherent Type anchored by the AODB+RMS pairing named by vendors themselves. No evidence was found that this leaf is merely a Variant/Alias of Airline Operations Platform or Ground Handling Management.

## Uncertainties

- Amadeus (a leading vendor) could not be researched; the model may under-represent alternative suite structures (no claims made).
- Mid-market / cloud-native segment (AeroCloud, Zafire) unreachable; small-airport variant structure inferred only weakly from SITA's "airports of all sizes" display-product framing — final document avoids claiming specific SMB-oriented shapes.
- Precise A-CDM milestone lists, numeric limits, and timing standards were not reachable from an authority source; none are asserted.
- The exact division between "airport platform" and "ground handler system" features (mobile resources, turnaround execution) varies by product; final document describes this as a shared zone rather than a hard line.
- Whether stakeholder *sharing* is definitional was resolved conservatively: treated as common mature structure (all three samples describe it, but older/internal deployments still fit the Type).

## Final Synthesis

The Airport Operations Platform is the airport operator's system of record for its own operating day. Its defining structure is: the airport-scoped flight picture (scheduled movements at this airport, kept live with event times), the airport's own operational resources as allocable objects (stands/gates, check-in areas, baggage systems; fixed and mobile) bound to flights under configurable rules, and a real-time day-of-operations loop (plan → monitor/alert → adjust → post-operation record). Around this core, mature products add a shared single operational picture across airlines and handlers, alerting/KPIs, predicted operational times, turnaround management, scenario planning, sequencing exchange with ATC, and FIDS output. Region, scale, deployment and admin extensions (billing, staff scheduling, data-exchange standards) are variants. The Type sits between airline operations (network-side), ground handling (service-side), ATC (movement-area authority), and display systems (output-only), and is distinguished from each by the combination of airport-owned resource allocation + operator-side day-of-operations management.
