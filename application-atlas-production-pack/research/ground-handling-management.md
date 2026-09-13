# Research Notes — Ground Handling Management

Research date: 2026-09-08
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what Ground Handling Management software actually is from real products: what objects exist inside it, who operates it, how a ground handler's working day flows through it, what rules constrain the work, and where the Type's boundary sits against Airport Operations Platform, Airline Operations Platform, generic Workforce Management, and passenger-processing / baggage products that handlers also use.

## Initial Boundary

- Hypothesis: this is the **handler-side operational software** — the software a ground handling organization (independent GHA, airline self-handling unit, or airport handling unit) uses to plan, allocate, direct and record its staff and ground support equipment (GSE) against the contracted services it owes per flight.
- Nearest neighbors: Airport Operations Platform (airport owns airport resources), Airline Operations Platform (airline owns fleet/crew/network), Workforce Management Platform (generic shift planning), Airline Reservation / PSS & DCS (passenger processing execution), Air Cargo Management (cargo terminal handling — sibling pass assigned cargo-terminal systems there), Airline Crew Management (flight-crew duty object set).
- The sibling pass (airport-operations-platform, processed 2026-09-06) already drew a preliminary seam: "handler systems manage contracted service delivery (service orders per flight, staff/equipment rosters, service records, billing to carriers). Airport platforms allocate *airport-owned* resources and coordinate. Test: remove the airport infrastructure/flight-picture core and keep per-flight contracted service delivery → Ground Handling Management." This pass tests that seam from the handler side.
- Unknowns: whether a single "GHA system of record" product shape dominates or handlers assemble the stack from components; depth of billing/load-control modules; delay-code workflow documentation.

## Research Questions

1. What is the unit of service work — the flight, the turn, the shift, the task?
2. What resources does the handler plan: staff only, staff + GSE, stands?
3. How does demand get computed (from what flight picture)?
4. What constraints shape rosters and allocation (qualifications, labor rules, SLAs)?
5. How is live execution directed and recorded (dispatch, mobile, task logging)?
6. How do delays/irregularities get handled (re-assignment, quick-turn decisions, knock-on prediction)?
7. Does the system carry the commercial seam (service records → billing/charging, SLA performance)?
8. Where is the boundary vs airport ops platforms, airline ops platforms, generic WFM, and passenger-processing/baggage products?

## Representative Products

Selection principles: market representation + documentation accessibility + different product philosophies + different customer levels. The search-engine layer was largely unreachable this pass (DuckDuckGo, Bing CN, Mojeek, Ecosia all failed or redirected), so products were sampled by direct fetch of vendor domains.

| Product | Vendor | Angle | Role in sample |
|---|---|---|---|
| GroundStar (Ground Handling Resource Management; Aircraft Turnaround Management) | INFORM (Germany) | optimization suite for handler/airline ground operations: staff + GSE planning → allocation → turnaround control → analytics | Core sample A — handler-side resource management (deep, 4 pages) |
| Ground handlers portfolio + Mobile Resource Manager | SITA (Switzerland) | global aviation-IT vendor selling the handler stack as components (passenger processing, baggage, resource management, messaging) | Core sample B — handler-facing components + airport-suite module that optimizes ground handling resources |
| ApronAI / TurnaroundControl | Assaia (Switzerland) | AI + computer-vision turnaround visibility sold to airports/airlines; handlers are monitored partners | Boundary sample C — buyer-side turnaround monitoring pole |
| IATA Ground Operations program | IATA | industry association: domain context (IGOM, ISAGO, GSE, de-icing, labor shortage, safety) | Domain reference (Tier 3 context) |

Rejected / unreachable samples:

- **Zafire (First Handling)** — known handler-side ground operations vendor; zafire.com timed out twice (direct + industry page). Abandoned per source-limitation rule. NOT used for any claim.
- **Logipad** — fetched logipad.aero: it is an **Electronic Flight Bag** product (flight crews, eForms, flight folder). **Product Mismatch** — not ground handling. Rejected.
- **Ramco** — fetched ramco.com: aviation suite is MRO/maintenance & engineering (MRO, engine MRO, flight ops, fleet technical). **Product Mismatch** — no ground handling product line on the fetched pages. Rejected.
- **Global Load Control** — globalloadcontrol.com timed out. Abandoned (candidate for the load-control-service variant pole; not used).

## Sources

Fetched 2026-09-08 (all directly reachable):

- INFORM — Ground Handling Resource Management: https://www.inform-software.com/en/solutions/aviation-ground-operations/ground-handling-resource-management
- INFORM — GroundStar product page: https://www.inform-software.com/en/software/groundstar
- INFORM — Ground handlers industry page: https://www.inform-software.com/en/industries/aviation/ground-handlers
- INFORM — Aircraft Turnaround Management: https://www.inform-software.com/en/solutions/aviation-ground-operations/aircraft-turnaround-management
- SITA — Mobile Resource Manager (module of SITA Airport Management): https://www.sita.aero/solutions/sita-at-airports/sita-operations-at-airports/sita-airport-management/sita-mobile-resource-manager/
- SITA — Ground Handlers industry page: https://www.sita.aero/industries/ground-handlers/
- Assaia — root/product overview: https://assaia.com/
- IATA — Ground Operations: https://www.iata.org/en/programs/ops-infra/ground-operations/

Reused boundary context from sibling passes (already in repo):

- research/airport-operations-platform.md (SITA / Collins / ADB observations; ground-handling seam)
- applications/airport-operations-platform.md (Related Types table)

Unreachable / failed: zafire.com (×2), globalloadcontrol.com, web.archive.org snapshot of Zafire, lite.duckduckgo.com, bing.com (CN-localized noise), mojeek.com (captcha), ecosia.org (redirect to Bing CN).

## Product A — INFORM GroundStar

Vendor positions GroundStar as "the complete software solution for airports, airlines, and ground handlers" optimizing "ground handling staff and equipment, stands and terminal resources across all operational phases – from planning to analytics". Three solution lines: Airport Resource Management (gates/stands/baggage belts/check-in counters — airport side), **Ground Handling Resource Management** (handler side), Aircraft Turnaround Management. "End-to-end software solution covering both passenger and ramp services." On-premise or cloud. Customers cited: dnata, Groundforce, SATS, Air France, Lufthansa, Acciona Airport Services (handlers/airlines); Fraport, flydubai, TAP, DUS, STARLUX across the three lines.

### Key observations (Ground Handling Resource Management)

- "designed to support the complete **planning, scheduling, allocation, and post-operational allocation analysis of ground staff and ground support equipment (GSE)**" — the four-phase loop (plan → schedule → allocate → post-op analysis) named by the vendor.
- "enables customers to reduce the unnecessary use of GSE and attain lower energy consumption and emissions" — GSE as an equipment pool with utilization/energy consequences.
- "prediction of optimal future resource demand, **calculation of staff requirement based on qualifications and availabilities**, and management of operations when flight disruptions arise".
- Rosters built from "demand requirements, workplace regulatory mandates, **individuals' qualifications and preferences**, and schedules"; "dynamic roster maintenance" covers "absences, vacation and shift swaps"; "Identify reasonable absences quotas".
- Handler challenges named: "multitude of diverging operational requirements… cover specific requirements with minimum resources and **meet Service Level Agreements (SLAs)**"; "Predict future demand for employees and equipment"; "Optimize shift planning and **prioritize most cost-efficient equipment**"; "Resolve the impact of flight irregularities automatically"; "higher transparency on **task status** ensuring optimal resource utilization".
- Day-of-ops: "real-time data and powerful decision support… improved situational awareness gained on the Day-of-Ops facilitates seamless control of all activities even as flight irregularities challenge their completion".
- Post-op: "analyzing resource allocation and performance data from planning and allocation phases, you can adjust future plans in cases of over- or under-performance"; "forecasting of critical situations".

### Key observations (Aircraft Turnaround Management)

- "real-time overview of all major **clearance activities**" per turnaround; "quick intervention options to proactively avoid potential delays and disruptions".
- Decisions: "Deciding to perform a **quick turnaround instead of a standard one** or **assigning more resources to a specific activity** to expedite it, can be evaluated and implemented by the Turnaround Manager."
- "reliable **delay predictions** by calculating potential **knock-on effects** of delays throughout the legs of the affected aircraft and assess their cost impact"; "Reliable **target off-block time** calculation"; "Cost model and decision support to reduce transfer times and save connections".
- Page framed toward airlines ("airlines must achieve higher aircraft utilization") — same suite serves airline self-handling and hub control.

### Key observations (GS TeamWork news item)

- "enables **frontline managers at airlines or ground handling companies to manage task allocation on the apron or within the terminal**, reducing the workload for back-office allocators" — two-level allocation reality (back-office allocator + ramp/terminal frontline), and evidence the same software category serves both airline self-handling and GHAs.

## Product B — SITA (Ground handlers portfolio + Mobile Resource Manager)

### Ground Handlers industry page (handler-facing stack as components)

- "we offer solutions for ground handlers that exploit the latest technologies for **passenger services, aircraft loading and dispatch, and mobility for management of staff schedules, duties and resources**. Our solutions increase staff productivity, automate processes and improve passenger handling for ground handlers worldwide."
- Products listed *for* ground handlers: **Bag Manager** ("real-time baggage management and reconciliation system to help airlines, airports and ground handlers reconcile, track, and manage baggage"), **WorldTracer** (mishandled baggage reporting/tracing), **Airport Management** (flight operations, fixed and mobile resources, CDM), **SITA Flex** ("cloud-based, open API platform enabling mobility and low-touch operations" — passenger processing), **Messaging** (Type B / Type X / AMHS-AFTN network access), plus security/service-management/network services.
- Reading: the handler IT stack is frequently **assembled from component vendors** — passenger-processing platform, baggage reconciliation, resource management, messaging — rather than one monolith. This pass treats that as a market-structure finding, not a definition carrier.

### Mobile Resource Manager (module of SITA Airport Management — sold to airports, aimed at ground handling resources)

- "Optimizing the management of **mobile resources for ground handling** and capacity planning."
- "connect **mobile wireless devices in the hands of employees** with the back-office systems and people needed to make things happen. Real-time updates improve and accelerate decision-making as events unfold."
- "**Automatic task logging increases the accuracy of billable services**, boosting revenue generation, and **dramatically reducing time spent on charging disputes**." — the service-record → charging seam, documented by a second vendor.
- "Calculate **capacity requirements based on flight schedules**, optimizing **work plans, shifts, and rosters** for long-term planning."
- "Use human resources efficiently, **in line with union agreements and labor laws**."
- "Turnaround management: …linking activities and events centered on the turn of a flight. **Predict delayed milestones and their domino effects**."

## Product C — Assaia (ApronAI / TurnaroundControl) — boundary pole

- Positioning: "Visibility to optimize the turnaround. Get the complete picture with **AI & computer vision**"; "built to optimize the KPIs **Airlines and Airports** are obsessed to improve" — buyers are airports and airlines, not handlers.
- Capabilities on the page: real-time turnaround visibility and milestone prediction ("Predicted Off Block Time"), "comprehensive **auditing of service-level agreements**" (turnaround operations), safety-violation detection (SafetyControl), APU/CO₂ monitoring (EmissionsControl), "ResourceManager" (stand/gate management).
- Buyer quotes: BER ("Providing this transparency and live visibility to our **ground handling partners**"); United ("Turnaround 2.0 uses AI… to boost our **zone controllers' efficiency**… manage multiple gate activities with more focus on handling exceptions"); GTAA (feeds A-CDM); FCO (POBT for A-CDM).
- Marketing figures (L3, not reused): "2,895,340 turnarounds monitored", "31 airports", "507 airlines", 17% OTP increase, 5 min ground-delay reduction, 50% unsafe-behavior decrease. Handler logos (dnata, Menzies, Swissport) appear among customers — the monitoring layer is also consumed by/for handlers.
- Boundary reading: Assaia **observes and predicts** the turn from external sensors/feeds; it does not hold the handler's rosters, staff qualifications, GSE pool, or the handler's own task allocation. It audits handler SLAs from the buyer side. This marks one edge of the Type: monitoring/visibility ≠ management of the handler's resources.

## Domain context — IATA Ground Operations

- "Ground handling is an integral part of airline operations. Ramps are busy places, confined areas in which aircraft, **Ground Support Equipments (GSE)**, and people are in constant motion in all weathers."
- "Current challenges include **safe and on time performance as well as labor shortages**."
- Standards layer: **IATA Ground Operations Manual (IGOM)** for "worldwide operational consistency and safety"; **ISAGO** audits ("implementation of Safety Management System (SMS) by ground handlers"); dedicated programs for **GSE**, **de-icing (DAQCP)**, baggage, Operational Portal.
- Reading: the domain's own standards frame ground handling around per-flight operational execution, a GSE-heavy physical environment, safety/audit regimes, and a chronic labor-availability problem — all of which the software Type absorbs as constraints (qualification/mandate-driven rosters, task records, SLA performance).

## Cross-product Comparison

| Dimension | INFORM GroundStar | SITA (handler portfolio + MRM) | Assaia (ApronAI/TurnaroundControl) | Classification |
|---|---|---|---|---|
| Managed subject: handler's staff + GSE against per-flight service demand | "planning, scheduling, allocation… of ground staff and GSE" | MRM: "mobile resources for ground handling… work plans, shifts, rosters"; stack covers "passenger services, aircraft loading and dispatch, mobility for staff schedules, duties and resources" | not managed (observed) | Shared by both handler-side vendors → **defining** |
| Flight/turnaround as the service event | per-flight demand; turnaround clearance activities; target off-block | "capacity requirements based on flight schedules"; "the turn of a flight" | the turn is the entire object of visibility | Shared → **defining** |
| Resource pool held as plannable objects with attributes | qualifications, availabilities, preferences; equipment cost-efficiency | union agreements, labor laws; employee mobile devices | no | Shared → **defining** |
| Plan → allocate → execute → record loop | four-phase loop named by vendor | long-term rosters + day-of allocation + task logging | only observe/record side | Shared (3 of 3, different depths) → **defining loop** |
| Real-time task status / mobile direction | "transparency on task status"; GS TeamWork frontline allocation | "mobile wireless devices… real-time updates"; "automatic task logging" | real-time visibility (sensor-derived) | Shared → **common mature structure** |
| Delay/disruption management | irregularity resolution, quick-turn decisions, knock-on cost prediction | "predict delayed milestones and their domino effects" | delay prediction, POBT, exception focus | Shared intent → **common** |
| Demand forecasting / optimization of rosters | central pitch (AI/OR optimization) | "optimization algorithms" named | no | Shared by both resource-management vendors → **common** (not definitional: manual allocation still is the Type) |
| Service record → charging/billing | post-op allocation/performance analysis (billing not named on fetched pages) | "automatic task logging increases the accuracy of billable services… reducing charging disputes" | SLA auditing (buyer side) | Billing seam evidenced by one vendor → **common; billing module held variant** |
| SLA/contract framing | "meet Service Level Agreements (SLAs)" | SLA implicit via billing accuracy | SLA auditing explicit (buyer side) | Shared framing → **common** |
| Airport resources (stands/gates/belts) | separate solution line (Airport Resource Management) — airports are a different buyer | Airport Management suite context | ResourceManager (stand management) | NOT this Type's core — marks the airport-side seam |
| Passenger processing / baggage reconciliation | not on fetched pages | sold as separate products (Flex, Bag Manager, WorldTracer) | no | **Adjacent components** handlers procure, not defining |
| Computer-vision / sensor-derived milestone data | no | no | core | **Vendor-specific** to the monitoring pole |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

Ground Handling Management is the ground-handling organization's operational system of record, providing:

1. **Flight-bound contracted service demand** — the services the handler owes its airline customers, held per scheduled flight movement / aircraft turnaround at the station (the unit of service work is the flight, not the day or the job).
2. **The handler's own operational resources as plannable objects** — staff (with qualifications/availabilities) and ground support equipment, held as an allocable pool.
3. **Allocation of that pool onto the flights' service tasks** — rosters/shifts and per-flight task assignments, computed against the flight schedule and constrained by qualification, availability and labor rules.
4. **Recorded execution feeding performance and charging** — task completion and times recorded (directly or via integration) so service delivery becomes an accountable, reportable, chargeable record.

Jointly-held is load-bearing: (1) without (2)(3) = a flight information consumer; (2)(3) without (1) = generic workforce management; (4) without (2)(3) = a monitoring/audit layer; (3) without (4) = a static roster tool.

Historical check (§24 reasoning): the pre-digital handler station — contract/service agreement per airline, flight schedule + whiteboard/radio task allocation, staff roster built on who was qualified for pushback/loading/check-in, equipment assignments, handwritten service and delay records feeding invoices — satisfies all four legs with no AI, mobile apps, cloud, or optimization algorithms. Older and regional products therefore still fit L0. (Analog framing is conceptual — no historical product page was fetched; assertion kept at conceptual strength.)

### L1 — Common Mature Structure

- Demand forecasting from flight schedules; what-if / scenario capacity planning
- Optimization of shifts/rosters and equipment assignments (AI/OR-class in current marketing)
- Qualification/certification-driven staffing; labor-agreement and regulatory constraints on rosters
- Mobile devices for staff with live task updates; automatic task logging
- Turnaround monitoring with milestone tracking, delay prediction and knock-on/cost impact
- SLA/KPI reporting and post-operation analysis feeding the next planning cycle
- Multi-station / network views (handlers operate many airports)
- Integration with airline/airport flight data and with adjacent execution products (passenger processing, baggage)

### L2 — Variant / Optional Structure

- **Operator-identity variants**: independent GHA vs airline self-handling (same suite marketed to airlines' ground ops) vs airport-company handling arms
- **Stack assembly**: integrated suite (INFORM-style) vs component stacks (SITA sells Flex / Bag Manager / WorldTracer / Airport Management / messaging separately)
- **Airport-side resource modules** (stands/gates/terminal) packaged by the same vendors for airport buyers
- **Billing/charging depth** (service-record-driven invoicing of airlines; dispute reduction)
- **Load control / dispatch functions** (prevalence unverified this pass — Zafire unreachable)
- **Baggage reconciliation, passenger processing** — adjacent products handlers procure
- **GSE fleet depth** (utilization, energy/emissions, maintenance depth unverified)
- **Safety/audit program support** (SMS/ISAGO-adjacent evidence is domain-level, product depth unverified)
- Deployment: on-premise vs cloud; monitoring/sensor integrations (computer-vision turnaround observation)

### L3 — Vendor-specific Structure (research notes only)

- INFORM: GroundStar naming; GS Planning / GS TeamWork (decentralized task allocation) / myStaff (mobile) / GroundStar Academy (e-learning); Airport Resource Management as separate line; customer references (dnata, Groundforce, SATS, Acciona, Air France, Lufthansa, flydubai, STARLUX, TAP, Fraport, DUS).
- SITA: Mobile Resource Manager as a module *of SITA Airport Management* (airport-suite placement); "USD 4M savings per year for a Major Asian carrier" (marketing claim); Bag Manager / WorldTracer / Flex / SITATEX / Type X naming.
- Assaia: ApronAI, TurnaroundControl, ResourceManager, SafetyControl, EmissionsControl names; CCTV/AI-derived milestone detection; POBT; "2,895,340 turnarounds monitored / 31 airports / 507 airlines"; 17% OTP / 5 min / 50% claims — marketing figures, not reused.

## Vendor-specific Findings

- Automatic task logging explicitly tied to billing accuracy and dispute reduction: documented by SITA MRM only → keep as common seam, billing module as variant.
- Two-level allocation (back-office allocator vs frontline manager task assignment): INFORM GS TeamWork only → structure plausible market-wide but held as single-source observation.
- Computer-vision turnaround observation: Assaia only (monitoring pole).
- Union-agreement/labor-law constraint named explicitly: SITA MRM; INFORM names "workplace regulatory mandates" — cross-supported at conceptual level.

## Boundary Findings

- **vs Airport Operations Platform** (sibling pass): airport platform allocates *airport-owned* resources (stands/gates/belts) and hosts the shared picture; handler system allocates the *handler's own* staff/GSE against contracted per-flight services. Porosity documented both directions: SITA sells Mobile Resource Manager inside the airport suite ("mobile resources for ground handling"), and INFORM sells Airport Resource Management to airports as a separate line. Test: remove airport-infrastructure ownership and the shared-picture role; keep contracted per-flight service delivery with own workforce/equipment → this Type.
- **vs Airline Operations Platform** (sibling pass): airline ops centers on the carrier's network/fleet/crew across airports; this Type centers on delivering services at stations. Airline self-handling uses this Type for station ground ops (INFORM turnaround page is airline-framed; GS TeamWork names airlines as users). Test: fleet/crew/network-control object set → airline ops.
- **vs Workforce Management Platform (generic)**: same scheduling machinery, different demand object. Here demand is *flight-shaped* (computed from the flight schedule, per-flight tasks, GSE coupling, turnaround deadlines) and records feed service charging. Test: remove flight/turnaround demand shape and GSE → generic WFM (INFORM itself sells WorkforcePlus for non-aviation workforce management — same vendor, separate product line, useful seam evidence).
- **vs Turnaround monitoring / apron systems (airport- or buyer-side)**: monitoring products observe/predict the turn from sensors and feeds (Assaia; ADB CORTEX Apron per sibling pass) and audit handler SLAs from the buyer side; they hold no handler rosters, qualification pools, or task allocation. Test: observe-only + buyer-side owner → monitoring variant of airport/apron territory, not this Type.
- **vs Air Cargo Management** (sibling pass): cargo-terminal handling systems (Hermes-class) manage AWB/ULD flows and were assigned to the cargo Type; this Type's center is passenger/ramp service delivery per flight (ramp loading of baggage/cargo is a service task here, not a warehouse flow). Test: AWB/ULD consignment machinery → Air Cargo Management.
- **vs Airline Reservation / PSS & DCS and passenger-processing platforms**: check-in/boarding *execution* platforms (SITA Flex, DCS) are tools the handler's staff operate; this Type plans/resources/records the delivery of those services and does not manage tickets, PNRs or the passenger journey.
- **vs Airline Crew Management**: similar rostering machinery, different subject (flight-crew legal duty pairings vs ground-staff labor pool + GSE). Kept brief; no directory implication.

## Observation on the directory

"Ground Handling Management" is a coherent Type anchored by the handler-side resource/service-delivery loop, independently confirmed by two reachable vendor families (INFORM, SITA) plus the buyer-side monitoring pole (Assaia) and the airport-ops sibling pass's own seam test. No evidence found that this leaf is merely a Variant/Alias of Airport Operations Platform or Airline Operations Platform. Note for taxonomy owner (recorded, no action taken): the leaf name's gerund form ("Ground Handling Management") matches the industry's own vocabulary ("ground handling" as the service; "ground handler" as the operator) — no alias issue.

## Uncertainties

1. **Billing-module depth**: only SITA documents the billing seam on fetched pages; handler billing/ERP back-office depth is inferred as industry practice, not product-documented in this sample → final doc keeps charging at "service records feed charging/performance" strength.
2. **Load control & dispatch functions**: known market feature of handler suites (e.g., weight & balance services) but NOT evidenced this pass (Zafire/Global Load Control unreachable) → not asserted as core; recorded as uncertain variant.
3. **Delay-code workflows**: industry-standard practice (delay attribution to airlines), but no fetched page documents product implementation → not claimed.
4. **"One system of record" vs component stacks**: SITA's page suggests handlers commonly assemble the stack from component vendors; INFORM sells a suite. Final doc describes the Type functionally and flags stack assembly as a variant, not a definitional posture.
5. **GSE maintenance/fleet management depth**: GSE utilization/energy reduction documented (INFORM); maintenance machinery unverified → variant only.
6. **Safety/SMS productization**: IATA documents SMS/ISAGO at domain level; product-level safety modules not sampled → domain context only.

## Final Synthesis

Ground Handling Management is the ground-handling organization's operational system of record. Its defining structure is: the handler's contracted services held as per-flight (turnaround-bound) service demand; the handler's own staff (with qualifications) and ground support equipment held as a plannable pool; the allocation of that pool onto flights' service tasks under qualification/labor/SLA constraints; and recorded execution that turns service delivery into an accountable, reportable, chargeable record. Around this core, mature products add forecasting and optimization, mobile task direction, delay/knock-on prediction, SLA/KPI reporting and multi-station network management. The Type sits between the airport side (which allocates airport-owned resources and hosts the shared picture), the airline side (which owns the network and the operation), and the buyer-side monitoring layer (which observes the turn without managing the handler's resources); it is flight-shaped workforce-and-equipment management, not generic shift planning, and not passenger processing.
