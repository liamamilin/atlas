# Research Notes — Bed & Capacity Management

Research date: 2026-09-06
Slug: bed-capacity-management
Directory leaf: Bed & Capacity Management (Category 22 — Healthcare & Life Sciences)

---

## Research Goal

Determine what a Bed & Capacity Management application is as an Application Type: its defining core structure, its standard mature capabilities, its variant space, and its boundaries against adjacent types (Patient Flow Management, Hospital Management System / EHR, Patient Scheduling, ED Information System, IT Capacity Management).

## Initial Boundary (hypothesis before research)

- Hypothesis: hospital operational software that treats inpatient beds as a real-time operational resource: bed inventory with live status (occupied / dirty / clean / blocked), patient placement decisions binding patients to beds, housekeeping/transport task coordination around bed turnaround, and capacity visibility/forecasting to drive escalation.
- Likely users: bed managers/capacity managers, patient flow coordinators, charge nurses, admitting staff, environmental services (EVS), transport teams, transfer center staff, operations executives.
- Likely confusions: Patient Flow Management (broader, person-centric), EHR ADT modules (event source), Capacity Management in IT (category 14, different domain), Space Management (IWMS, facilities not care-driven).

## Research Questions

1. What are the core objects (bed, room, unit, bed status, placement, housekeeping task, transport task)?
2. What is the bed status lifecycle and who/what drives its transitions?
3. How are placement decisions made, and what constraints apply?
4. How far does "capacity" extend: boards only, or forecasting, escalation protocols, staffing demand?
5. What surfaces exist (bed board, housekeeping view, command center, mobile, unit whiteboards)?
6. How does the type integrate with EHR ADT events?
7. Where is the line vs Patient Flow Management — same products, different emphasis?

## Representative Products (sample rationale)

Chosen for market position + different product philosophy + different layer of the hospital IT stack:

1. **TeleTracking** (Operations IQ Platform; UK line named "Electronic Bed and Capacity Management") — the dedicated, archetype vendor for this category; operational-console philosophy.
2. **LeanTaaS iQueue for Inpatient Flow** — analytics-first philosophy (predictive/prescriptive capacity management layered over EHR data); KLAS-designated "Capacity Management" category leader (per vendor site).
3. **Oracle Health Clinical Operations (Patient Flow / Command Center Dashboard / Transfer Center / Clinical Operations Whiteboard / Clinical Location Awareness)** — the EHR-suite-embedded pole.
4. **CenTrak** — observed only as a boundary/enabler sample (RTLS sensing layer); current public solution catalog contains no dedicated bed-management product, which itself is a boundary finding.

Rejected as representative: MEDITECH Expanse Acute Care page (fetched; generic EHR marketing, no bed-management-specific evidence beyond an Expanse Transport mention); Epic Bed Planning (documentation not publicly accessible).

## Sources

Tier 2 official product/solution pages (fetch date 2026-09-06):

- TeleTracking US homepage — https://www.teletracking.com/ ✅
- TeleTracking Throughput solution page — https://www.teletracking.com/healthcare-operations-iq-platform/throughput/ ✅
- TeleTracking UK homepage — https://teletracking.uk/ ✅
- LeanTaaS homepage — https://leantaas.com/ ✅
- LeanTaaS iQueue for Inpatient Flow — https://leantaas.com/products/inpatient-flow/ ✅
- Oracle Health Clinical Operations — https://www.oracle.com/health/clinical-operations/ ✅
- CenTrak homepage — https://www.centrak.com/ ✅

Failed / abandoned (network-restricted rule: ≤2 attempts per source):

- https://leantaas.com/products/iqueue/ — 404 (root + /products/inpatient-flow/ succeeded)
- https://www.centrak.com/patient-flow — 404 (root succeeded)
- https://www.oracle.com/health/capacity-management/ — 404 (clinical-operations page succeeded)
- MEDITECH acute-care page fetched successfully but contained no bed-management-specific content.

Source-access limitation: none of the sampled vendors expose public Tier-1 operational documentation (help centers, user guides, manuals) for their bed/capacity modules. TeleTracking's customer portal (Knowledge Bridge) is login-gated; CenTrak's knowledge center is gated; LeanTaaS and Oracle Health expose marketing/solution pages only. All statements below are therefore calibrated to Tier-2 evidence; no precise operational parameters (state vocabularies, timers, limits, defaults) are claimed.

---

## Product Observations

### Product A — TeleTracking (Operations IQ Platform / UK "Electronic Bed and Capacity Management") — Evidence layer A

Observations (from official pages):

- Positioning: "The Operations Platform for Hospitals and Health Systems… Expanding the Capacity to Care." UK site: "Our Operations IQ Platform helps improve bed and capacity management, automating staff workflows, and improving patient flow."
- The UK solution line is literally named **"Electronic Bed and Capacity Management"** — direct confirmation of the category naming and its electronic-board heritage.
- Throughput module: coordinates "every step of the acute care journey, from admission to discharge"; "unifies all of these workflows into a single operational view" — teams named: **placement, discharge, transport, housekeeping, nursing**.
- **Patient Placement**: "Real-time care progression indicators keep admissions on pace with discharges, eliminating the lag between a bed becoming available and a patient reaching it."
- **EVS Management**: "Automated cleaning requests eliminate the gap between discharge and room readiness, accelerating turnaround."
- **Transport Management**: "Built-in zoning and a mobile-accessible interface keep transport teams deployed efficiently."
- **Discharge Workflows**: "automated triggers… so discharge doesn't stall waiting on a single point of action."
- **AutoDischarge**: "Real-Time Location Systems (RTLS) detects when a patient exits, automatically triggering notifications to EVS, reducing dirty bed times from hours to minutes." → confirms (a) an occupied→dirty→cleaned→ready readiness cycle, (b) task generation driven by status transitions, (c) RTLS-automated transitions as a variant.
- Capacity visibility: "You Can't Manage Capacity You Can't See"; "Systemwide Visibility… a single, real-time source of truth across the enterprise" (census picture for every unit/department).
- Metrics surfaced: LOS, boarding, discharges, bed turnaround.
- Platform framing: event-based ("Built on a foundation of more than 455 million events" — marketing figure, recorded here only); "Seamlessly integrated with the EHR"; cloud-hosted.
- UK: Co-ordination Centres "underpinned by our Electronic Bed and Capacity Management platform… from capacity to referrals, resource management, and staffing workflows"; outcome framing "reducing lost bed time between admissions."

### Product B — LeanTaaS iQueue for Inpatient Flow — Evidence layer A

Observations (from official pages):

- Positioning: "Make Every Inpatient Bed Count"; "Maximize healthcare capacity with AI and prescriptive analytics"; homepage badge shows KLAS "Best in KLAS Capacity Management" category (2026 per image alt text) → confirms the market calls this category **capacity management**.
- Scale claims (marketing, research-notes only): 100+ hospitals, 30+ health systems, 35k inpatient beds under management.
- Daily capacity management: "Anticipate capacity constraints, surface barriers, and coordinate action"; brings "updates, escalations, and operational concerns together before daily bed huddles, automatically capture key decisions and actions, and track follow-through so teams can resolve emerging constraints and **activate capacity protocols earlier**." → confirms capacity escalation protocols + bed huddles as product surfaces.
- Admission planning & placement: "Give the ED, PACU, transfer center, and bed management a **shared view of incoming demand and placement progress**, helping teams prioritize patients, coordinate appropriate admission options (e.g., hospital at home), and reduce boarding and downstream delays."
- Care progression: "surface patients and barriers requiring intervention, and focus multidisciplinary rounds"; screenshot shows discharge-stats widgets: "Likely DC Today", "Boarding >2 Hours", "Early DC Opportunity", "Needs EDD Review", "predicted discharge dates, linked to EHR" → confirms EDD (estimated discharge date) tracking and discharge prediction.
- Staffing alignment: "Use shift-level census and workload forecasts to identify staffing gaps or excess capacity, guide staff-allocation and incentive-pay decisions."
- Discharge predictability: "identify likely discharges and uncover clinical, social, and logistical barriers earlier, then coordinate follow-up across care management, ancillary teams, and discharge-lounge workflows."
- Data substrate: "using only a small amount of EHR data"; cloud-based, computer + mobile access → analytics overlay on EHR ADT data rather than an operational transaction system.

### Product C — Oracle Health Clinical Operations (Patient Flow / Command Center / Transfer Center / Whiteboard / Clinical Location Awareness) — Evidence layer A

Observations (from official page):

- Suite framing: "an integrated, near real-time suite of solutions that connect **situational awareness, throughput management, resource tracking, and monitoring**."
- **Patient Flow** product: "near real-time visibility into the inpatient journey, including **bed utilization, length of stay, transfers, and discharge details**… automating **bed selection, environmental services requests, and patient transportation**."
- **Command Center Dashboard**: "forecast capacity needs… enterprisewide visibility into **patient placement** and care transitions… anticipate throughput challenges, **optimize inpatient bed assignments**, and address bottlenecks before they impact care."
- **Transfer Center**: "centralizing assessments, communications, and documentation… initiates **pre-arrival bed reservations**, and automatically creates transfer cases from physician orders… Integrated with Oracle Health Patient Flow… automates interfacility transfers."
- **Clinical Operations Whiteboard**: "digital command center approach… near real-time visibility into patient flow, staffing… **Autopopulated clinical events** and predictive analytics… optimize bed utilization, length of stay, discharge planning, and resource management." → the digital replacement of the manual unit whiteboard.
- **Clinical Location Awareness**: RTLS delivering "near real-time visibility into the location of patients, clinicians, and equipment across your organization… EHR-agnostic… By automating patient-clinician assignments and equipment tracking…" → EHR vendor also sells the sensing layer.
- **Workload Management**: "uses near real-time data and predictive analytics to optimize staffing based on patient conditions" → staffing-demand linkage.
- **Digital Room Signage**: room-side display of "allergies, infection protocols, and **discharge status**" → room/bed status surfaced at the physical bed.

### Product D — CenTrak (boundary/enabler sample) — Evidence layer A

- Current public solution catalog (asset, safety, workflow, infection control, experience, environment) contains **no dedicated bed-management product**. Closest: "Clinical Workflow — automate the documentation of clinical milestones… analyze trends to help identify bottlenecks."
- Conclusion: RTLS vendors supply the **sensing layer** that automates status transitions (e.g., detect patient exit → notify EVS) and feed bed systems; they are enablers, not the bed & capacity management application itself. Corroborated by TeleTracking's own AutoDischarge RTLS integration and Oracle selling its own RTLS module.

### Product E — MEDITECH (rejected as representative) — Evidence layer A (weak)

- Acute-care page is generic EHR marketing; only tangential evidence (Expanse Transport module). Not used for any type-level claim.

---

## Cross-product Comparison

| Aspect | TeleTracking | LeanTaaS iQueue (Inpatient Flow) | Oracle Health Clinical Operations |
|---|---|---|---|
| Product form | dedicated standalone operations platform, EHR-integrated | standalone cloud analytics overlay on EHR data | module family inside EHR vendor suite |
| Bed inventory as managed object | yes (placement, EVS, turnaround) | yes (bed availability, per-bed ROI framing) | yes (bed utilization, bed assignments) |
| Per-bed occupancy/readiness cycle | explicit (discharge → EVS → ready; "dirty bed times") | implicit (care-progression & discharge focus; less bed-granular in public docs) | explicit (bed selection, EVS requests, discharge status signage) |
| Patient placement decisions | Patient Placement module | admission planning + placement prioritization for ED/PACU/transfer center/bed mgmt | bed selection automation + command-center placement oversight |
| Shared real-time operational view | "single operational view", systemwide census visibility | shared demand/placement view for multiple intake teams; bed huddles | whiteboard + command center dashboard |
| Housekeeping/EVS turnaround | EVS Management; AutoDischarge | not emphasized publicly | environmental services requests automation |
| Transport | Transport Management module | not emphasized publicly | patient transportation automation |
| Discharge machinery | discharge workflows, triggers | EDD review, predicted discharges, discharge lounges | discharge planning; discharge status surfaces |
| Capacity forecasting / prediction | Decision IQ (AI), enterprise analytics | core philosophy: predict surges, staffing forecasts | command center forecasting; predictive analytics |
| Escalation protocols | capacity decisions at scale (framing) | "activate capacity protocols earlier", huddle capture | "address bottlenecks before they impact care" |
| Staffing linkage | staffing workflows (UK co-ordination centres) | shift-level census/workload forecasts | Workload Management module |
| Inter-facility transfers | Transfer & Command Centers; network visibility | admission options incl. hospital-at-home | Transfer Center with pre-arrival bed reservations |
| Data substrate | event platform integrated with EHR | EHR data feed, ML | EHR-native + own RTLS |

Stable commonalities across all three representative products (evidence layer B): bed inventory as managed resource; occupancy + readiness state; placement decisions; shared real-time multi-department view; discharge machinery; capacity forecasting/prediction; EHR-ADT-derived data.

Polar differences (evidence layer A): operational-transaction pole (TeleTracking: tasks, EVS, transport, mobile) vs analytics-decision pole (LeanTaaS: predictions, huddles, staffing guidance) vs suite-embedded pole (Oracle Health). Mature products converge toward covering both operational and planning layers.

---

## Canonical Model — Abstraction Hierarchy

### L0 — Defining Invariant (deliberately small)

1. **Managed bed inventory** — the facility's inpatient beds held in the system as individually identified physical resources (organized in rooms/units). Without it there is nothing for the type to manage.
2. **Per-bed operational state** — a live, user-visible state per bed that distinguishes occupied from available-for-use and changes as care events occur (admission, discharge, cleaning/readiness, hold/blocking). Without live state driven by care events, the type collapses into pre-booked scheduling.
3. **Placement decisions** — binding a specific patient to a specific bed (assign at admission, move at transfer, release at discharge) in response to demand and bed suitability. Observed in all three representative products under different names.
4. **Shared real-time operational view** — a common live surface (board/dashboard) through which multiple departments (admissions/ED, bed management, nursing, EVS, transport, transfer center) see and act on this state. Without the shared surface, bed state remains an internal EHR ADT attribute rather than a management application.

Test against historical/regional samples: electronic bed boards (whiteboard replacements), NHS PAS bed modules, RTLS-driven boards — all satisfy L0 without forecasting, AI, EVS dispatch or command centers. L0 survives the historical check.

### L1 — Common Mature Structure

- EVS/housekeeping cleaning workflows: cleaning tasks generated by discharge events; turnaround timing; readiness confirmation (TeleTracking, Oracle Health)
- Patient transport task management with zoning/dispatch (TeleTracking, Oracle Health)
- Discharge machinery: expected/estimated discharge dates, predicted discharges, barrier surfacing, discharge lounges (all three, strongest in LeanTaaS)
- Care-progression / milestone tracking tied to admissions pacing (TeleTracking, LeanTaaS)
- Intake queues and boarding visibility for ED/PACU/transfer center (all three)
- Bed reservations/holds ahead of arrival (Oracle Health Transfer Center; common in the category per public materials)
- Capacity dashboards and KPIs: occupancy, length of stay, boarding, bed turnaround (all three)
- Demand/capacity forecasting and discharge prediction (LeanTaaS, Oracle Health; TeleTracking Decision IQ)
- Escalation machinery: capacity protocols, bed huddles, bottleneck alerts (LeanTaaS explicit; Oracle/TeleTracking framing)
- Staffing-demand linkage from census/workload forecasts (LeanTaaS, Oracle Health Workload Management, TeleTracking UK)
- Integration with EHR ADT events as the primary data substrate (all three)
- Mobile companion surfaces for EVS/transport/roving staff (TeleTracking; LeanTaaS mobile access)
- Placement suitability constraints (e.g., isolation, unit level of care) — implied by category practice; public documentation of these rule engines is limited, so mechanics are not asserted

### L2 — Variant / Optional Structure

- Product form: standalone platform vs EHR-embedded module vs analytics overlay (all three poles observed)
- Status-transition automation: RTLS-sensed transitions vs manual staff updates (TeleTracking AutoDischarge, Oracle Clinical Location Awareness)
- Delivery model: hospital-run vs vendor-operated centralized command/coordination center (TeleTracking Co-ordination Centres)
- Scope: single facility vs multi-facility network-wide capacity visibility (TeleTracking "boundaryless", Oracle enterprise)
- Peripheral room surfaces: digital room signage/whiteboards showing status at the bed (Oracle)
- Alternative placement pathways: hospital-at-home, discharge lounges, departure lounges (LeanTaaS)
- Regional vocabulary: UK "electronic bed management / lost bed time" vs US "throughput / capacity management" (TeleTracking UK vs US)
- AI decision-support depth (Decision IQ, prescriptive analytics)
- Adjacent bundled modules: patient observation video, nurse call, asset tracking (Oracle suite breadth; CenTrak) — these belong to neighboring types, only adjacent here

### L3 — Vendor-specific (research notes only)

- TeleTracking: module names Throughput / Access / Decision IQ / AutoDischarge; "455 million events" figure; UK ROI figures (£3m productivity gain etc.)
- LeanTaaS: iQueue branding; KLAS Best in KLAS Capacity Management claim; ROI claims ($10k/bed/year); "35k inpatient beds" scale claim; "Better Healthcare through Math" book
- Oracle Health: product names (Patient Flow, Command Center Dashboard, Transfer Center, Clinical Operations Whiteboard, Clinical Location Awareness, Digital Room Signage, Patient Observer, Workload Management); Patient Observer specifics (1 technician : 12 patients, 3D camera)
- CenTrak: Connect Pulse, TruView, Elpas series; case-study savings figures

---

## Vendor-specific Findings

See L3 above. None promoted to the canonical model.

## Boundary Findings

1. **vs Patient Flow Management** — the most porous boundary. Vendors market the same capability cluster under both names: TeleTracking's module is "Throughput — Integrated Patient Flow"; Oracle Health sells a product literally called "Patient Flow" whose features are bed utilization/selection/EVS; LeanTaaS calls its product "Inpatient Flow". Structural distinction adopted: **patient flow is person-centric** (the patient's journey through stages: ED → admission → care → discharge, with timing/blocked-flow analytics), **bed & capacity management is space/asset-centric** (the bed as a physical resource: state, readiness, placement, capacity). The bed & capacity type is the operational slice that patient flow depends on. Products routinely bundle both. If the per-bed state/placement core is removed and only the person-journey remains, the product is Patient Flow Management.
2. **vs Hospital Management System / EHR** — the EHR produces the ADT events (admit/discharge/transfer) that drive bed state; EHR suites increasingly bundle flow/capacity modules (Oracle Health). Distinction: EHR centers on clinical documentation of the patient; bed & capacity management centers on the operational state of the physical bed and placement decisions. Removing the operational bed-state/placement layer leaves EHR ADT.
3. **vs Patient Scheduling** — scheduling books patients into future time slots; bed placement binds patients to physical beds in the present, driven by live care events rather than pre-booked time.
4. **vs Emergency Department Information System** — ED systems manage ED-side care; ED boarding appears in bed & capacity systems as an intake queue and boarding metric.
5. **vs Capacity Management (category 14, IT)** — same English term, different domain: IT capacity management plans compute/infrastructure resources; nothing in this healthcare type. Disambiguation noted for the directory.
6. **vs Space Management / IWMS (category 17)** — IWMS plans and manages the facility space portfolio (floor plans, moves, maintenance); bed & capacity management operates the live care-driven state of beds inside that space. Different rhythm (facilities planning vs real-time care operations).
7. **RTLS vendors are enablers, not this type** — sensing layers automate status transitions and feed bed systems (CenTrak observation; TeleTracking/Oracle RTLS integrations).
8. **Command center / transfer center** — organizational delivery models commonly built on this software (TeleTracking Co-ordination Centres, Oracle Health Transfer Center), not separate application types.

## Uncertainties

- Exact bed-state vocabularies (occupied / vacant-dirty / vacant-clean / blocked / reserved etc.) could not be verified from public docs; only the occupied→dirty→ready cycle is supported (TeleTracking "dirty bed times", "gap between discharge and room readiness"; Oracle EVS requests). Final document describes the cycle conceptually without a canonical state list.
- Placement rule engines (gender, isolation, level-of-care, bed-cleaning-level rules) are widely believed standard but not publicly documented in the sampled evidence; kept in L1 with qualified wording.
- Whether analytics-only capacity products (LeanTaaS pole) should be inside this type or a separate analytics type: current call — inside, since they operate on the same object (bed/census state and placement/demand) and the market (KLAS) treats "capacity management" as one category; noted as a possible future split.
- UK NHS terminology (e.g., "lost bed days") was only partially evidenced via vendor pages; regional vocabularies documented as variants without detailed claims.

## Final Synthesis

A Bed & Capacity Management application is hospital operations software whose defining core is: a managed registry of the facility's inpatient beds, a live per-bed state distinguishing occupied from available-for-use that advances with care events (discharge → cleaning → ready), placement decisions that bind patients to specific beds as demand arrives, and a shared real-time operational view that lets admissions/ED, bed management, nursing, EVS and transport act on the same state. Mature products extend this core with EVS/transport task coordination, discharge prediction and EDD tracking, intake/boarding queues, capacity dashboards, demand forecasting, escalation protocols (huddles, capacity triggers), staffing-demand linkage, and EHR-ADT integration. The type spans an operational pole (task execution, turnaround) and a planning pole (prediction, escalation); form ranges from standalone platforms to EHR-embedded modules to analytics overlays. Its boundary against Patient Flow Management is person-journey (flow) vs bed-resource (state/placement/capacity); against the EHR it is the operational layer above ADT events; against scheduling it is live care-event state rather than pre-booked time.
