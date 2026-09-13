# Research Notes — Aircraft Maintenance Management

Research date: 2026-09-06
Slug: aircraft-maintenance-management
Directory leaf: Aircraft Maintenance Management (Section 18 — Transportation, Mobility & Logistics)

## Research Goal

Understand what an Aircraft Maintenance Management application really is from real products: what objects exist inside it, who uses it, how maintenance work is scheduled, executed, recorded, and proven, and where its boundary lies against generic maintenance software (CMMS/EAM), road-fleet management, airline operations, and MRO business systems.

## Initial Boundary (hypothesis before research)

- Hypothesis: this is the aviation-specialized sibling of CMMS/EAM. The core is not "work orders on equipment" but the **airworthiness regime**: an approved maintenance program per aircraft, due points computed from usage (flight hours / cycles / calendar), mandatory compliance items (ADs/SBs), serialized component accountability, and a durable per-aircraft technical record that proves compliance to a regulator.
- Likely confusions:
  - CMMS / Maintenance Management (generic industrial maintenance)
  - Enterprise Asset Management / EAM (broader asset lifecycle)
  - Fleet Management System (road vehicles; same "fleet + oversight loop" family)
  - Airline Operations Platform (flies the schedule; maintenance keeps aircraft available)
  - Aftermarket Service Management / MRO business systems (commercial wrapper around maintenance work for customer aircraft)
- Unknowns going in: how due lists are actually computed and forecast; how defect/MEL deferrals are handled; how component tracking relates to the airframe record; how the small-operator tracking tier differs from airline M&E; whether the MRO commercial layer is part of the Type or a variant.

## Research Questions

1. What is the central object — the aircraft, the maintenance program, or the work order?
2. How is maintenance scheduled? What drives "due" (hours, cycles, calendar, events)?
3. What is the per-aircraft record, and what role does it play (logbook, audit evidence, resale)?
4. How are defects and deferrals (MEL) handled, and by whom?
5. How are components/parts tracked, and how do they relate to the aircraft record?
6. How is regulatory compliance (ADs/SBs, program revisions, sign-off/release) represented?
7. Who are the users and roles (maintenance control, planning, mechanics, engineering, quality, stores, pilots)?
8. What interfaces exist (fleet status, due list, work packages, mobile execution, records vault)?
9. How does the small-operator / business-aviation tracking tier differ from airline M&E?
10. Where does this Type end and CMMS / EAM / FMS / Airline Ops / MRO-business begin?

## Representative Products

Selected for market representativeness, different product philosophy, and different customer tier:

| Product | Vendor | Tier / philosophy |
|---|---|---|
| AMOS | Swiss AviationSoftware (Swiss-AS) | Large airline/MRO enterprise M&E; deep integrated maintenance-engineering-logistics; airline-born |
| eMRO | TRAX | Airline/MRO web ERP; "system of record" positioning; 21 modules + role-based mobility suite |
| Ramco Aviation | Ramco Systems | Aviation edition of an ERP suite; M&E vs MRO vs Fleet Technical Management split; defense/heli/UAS reach |
| Veryon Tracking (+ Work Center, Diagnostics, Publications) | Veryon (ex ATP/FlightDocs) | Tracking-first suite for business & general aviation up to commercial; e-logbook emphasis |
| CAMP MTX | CAMP Systems | Business-aviation maintenance tracking as a managed service (analyst team + tools); OEM-recommended |

Dropped / not fetched: Aables (small-operator tracker; site unreachable twice), TRAX eMRO detail page (404 twice), Veryon support center (401). Verizon-style gaps recorded under Sources.

## Sources

Fetched 2026-09-06 (all official vendor surfaces):

- Swiss-AS — AMOS home: https://www.swiss-as.com/ ; AMOS Modules: https://www.swiss-as.com/amos-modules ; Core & Optional Modules: https://www.swiss-as.com/core-optional-modules ; Planning: https://www.swiss-as.com/modules/planning ; Maintenance Control: https://www.swiss-as.com/modules/maintenance-control
- TRAX — Products: https://www.trax.aero/products/
- Ramco — Aviation: https://www.ramco.com/aviation (product pages for MRO / M&E / Fleet Technical Management listed from nav)
- Veryon — Home: https://www.veryon.com/ ; Tracking / Maintenance Tracking: https://veryon.com/products/veryon-tracking/maintenance-tracking
- CAMP — Home: https://www.campsystems.com/ ; CAMP Maintenance (MTX): https://www.campsystems.com/maintenance

Failed sources (abandoned per network rule): support.veryon.com (401), trax.aero eMRO detail page (404/transport error ×2), aables.com (transport error ×2), swiss-as.com/en/amos (404, root worked).

**Source-access limitation:** vendor help centers / user guides are customer-gated in this market; evidence is from official product and module pages (Tier 2) plus AMOS module descriptions (closest to Tier 1). Precise operational details (exact due-list formulas, tolerance rules, state label sets, numeric limits, specific certificate names/forms) are NOT publicly documented in the fetched pages and are therefore not asserted in the final document.

## Product Observations

### AMOS (Swiss-AS) — evidence layer A (directly observed)

Positioning: "integrated MRO software solution for aviation operations"; "comprehensive aircraft maintenance and engineering system trusted by airlines and MRO providers"; "supports maintenance, engineering and logistics processes across the entire operation while ensuring full regulatory compliance"; "built-in regulatory compliance … full airworthiness and audit readiness at all times."

Editions/categories on the modules page: Airline / MRO / Component MRO / CAMO / Rotor Wing.

Core modules (8 core + optional):
- **Material Management** — "control the aviation supply chain from procurement to consumption… parts availability, stock levels… data-driven logistics."
- **Engineering** — "support continuing airworthiness with engineering capabilities that manage compliance, modifications and reliability data."
- **Planning** — "the hub of the system": preparation of scheduled and unscheduled maintenance events "from short-term tasks to long-term checks"; forecasting of upcoming events; creation of "complete work packages with all required information" (tasks, materials, resources); "what-if" simulations showing "alternative maintenance opportunities based on planning preferences and regulatory limits."
- **Production** — "execute Line and Base Maintenance with clear handovers, real-time progress tracking and flexible digital workflows… paperless completion of work packages."
- **Maintenance Control** — "central tool for monitoring fleet reliability and ensuring uninterrupted airworthiness"; "operational link between flight crews and maintenance teams, first point of contact when technical issues arise"; defect resolution via Event Tracking, Deferred Defects, **MEL items**, troubleshooting; root-cause analysis.
- **Component Maintenance** — "component shop maintenance with full visibility of projects, capacity and **serialised parts**… quality, traceability and throughput across the entire repair and overhaul cycle."
- **Human Resources** — workforce, skills, licences, labour costs, compliance.
- **Quality Assurance** — audits, compliance, corrective actions, staff licences and training, "regulatory readiness."
- Optional: **Financial Management** (billing, warranty tracking, cost allocation, accounting, stock valuation), **AMOSmro** (MRO commercial: "from quotation to hangar planning and delivery"), **Commercial** (CRM + quotation), **Rotor Wing Excellence** ("mission-specific counters, precise weight and balance"), AMOSsim (flight simulators), Financial Multi-Entity.

Companion surfaces:
- **AMOSeTL** — "digitise the technical logbook and connect flight operations with maintenance in real time… structured defect reporting."
- **AMOSmobile/EXEC** — "live AMOS data directly to the aircraft… guided, paperless task execution and real-time documentation" for "line and base maintenance."
- **AMOSmobile/STORES** — mobile warehouse transactions.

### eMRO (TRAX) — evidence layer A

Positioning: "web-based ERP… unifies every aspect of aircraft maintenance into a single, real-time system. eMRO integrates engineering, planning, production, inventory, quality, documentation, technical records, and financial processes." "Our solutions help create the **system of record required by airlines, lessors, and regulatory authorities**." "21 modules for aircraft and component maintenance, fleet and inventory management, and financial control." **eMobility**: "14 role-based iOS and web-based applications… from cockpit to cabin, ramp to hangar, shop to AOG field operations."

### Ramco Aviation — evidence layer A

Product split (nav): **Maintenance, Repair and Overhaul** ("Line, Component, Engine, Hangar, Heavy maintenance, and OEM aftermarket services"), **Maintenance & Engineering** ("managing diverse fleets, from fixed-wing to rotor-wing… paperless operations and regulatory compliance"), **Defense Asset Management** ("fleet readiness and availability for tactical missions"), **Flight Operations**, **Fleet Technical Management** ("airworthiness management and aftermarket service operations throughout the fleet lifecycle… meeting industry compliance and airworthiness standards"). Industries: airlines, MRO, heli operators, UAS/drones, defense. Marketing mentions "from contract to cash" (MRO commercial), "Smart Wrench" (mobile execution), CAMO/tech-records automation webinar title.

### Veryon (Tracking / Work Center / Diagnostics / Publications) — evidence layer A

Positioning: "Aviation Software for maintenance tracking, MRO management, technical publications, defect analysis, reliability management, guided troubleshooting." Audiences: Business & General Aviation, Commercial Aviation, Helicopter Operations, MROs, OEMs. Fleet Management solution described as "Track airworthiness and compliance, plus plan maintenance events."

Veryon Tracking — Maintenance Tracking features observed: **eLogbooks** ("fully compliant electronic logbooks"), **eSignature**, **non-routine work**, **work orders** ("assign, manage, update, and review work orders in real time from your desktop or mobile app"), **AD and SB monitoring** ("automated updates for Airworthiness Directives and Service Bulletin revisions"); task list: View Due List, Add Non-Routines, Create Maintenance Items, Report Times, Update Utilizations, Update Availability, Add Compliance, Manage Logbooks, Create Work Orders, View Completed Work, View Reliability Reports, View History, Sign-off Electronically, Create Checklists. Mobile app: "Pilots and crew can view and update maintenance data, submit non-routine maintenance reports, sign off checklists." Dashboards: "real-time data on maintenance status, discrepancies, logbooks, and work orders."

Veryon Work Center (MRO tier): "Manage work orders, parts, tooling, labor, quoting, and billing." Diagnostics: defect analysis, reliability, guided troubleshooting. Publications: "aircraft maintenance manuals and regulatory libraries."

Customer-voice evidence (Director of Maintenance, Wing Aviation): "I've gone from having to review logbooks for 27 airplanes every morning to looking at one electronic dashboard."

### CAMP MTX — evidence layer A

Positioning: "Know you're airworthy, compliant and ready to fly." "Track, plan, and manage scheduled and predictive maintenance for your aircraft." Audiences: Corporate Flight Department, Owners & Pilots, Managed Fleets, CAMO Services, Helicopter Operation.

Observed capabilities:
- **Due List** ("Smart Due Lists"): "Whether you're planning a heavy maintenance event, a routine inspection, or you just want to know **'can I fly on that day?'**… Change time window, filter task types, or alter your **aircraft utilization assumptions**. You can even project **penalty driven due times based on specific events** such as firefighting or partial engine shutdowns."
- **Work Order**: "a convenient container for planning, cost-tracking and execution… in-house, or send it to a service center… Go paperless with ezSign."
- **Maintenance Program Manager**: "ensures your AMP, AAIP or Maintenance Program is accurate and up to date"; "CAMP automatically applies all OEM revisions to your aircraft or makes them available for your approval"; "version management… release maintenance plans in accordance with your SOP."
- **AD/SB Manager**: "viewing and managing authority and OEM AD/SB applicability, implementation strategy and status in a single tool"; analyst team "will review, assess and apply Service Bulletins and Airworthiness Directives for you."
- **iCAMP mobile**: "airworthiness status from virtually anywhere."
- **Analyst service**: "Our analysts, with years of experience in your aircraft model, act as your second set of eyes."
- Integrated modules: **EHM** (engine health monitoring/trending), **Flight Scheduling** ("a flight scheduling system that can't see upcoming MTX due items is unreliable"), **IMS** inventory ("wheels, rotables or an entire stockroom… search stock, create a requisition, or purchase parts while updating maintenance tasks").
- Records posture: "traceable, transparent maintenance records… secure digital information and ensures its un-alterability"; ezVault (records vault); Document Manager; Checklists; Observations; MTX Calendar; Fleet Analytics.

## Cross-product Comparison

| Dimension | AMOS | eMRO (TRAX) | Ramco Aviation | Veryon Tracking | CAMP MTX |
|---|---|---|---|---|---|
| Aircraft register (tail-numbered fleet) | yes (fleet mgmt core) | yes ("aircraft and component maintenance, fleet…") | yes (M&E / Fleet Technical Mgmt) | yes (fleet dashboards, per-aircraft) | yes (per-aircraft, per-tail status) |
| Airworthiness/compliance as central concern | "uninterrupted airworthiness", "audit readiness" | "system of record required by… regulatory authorities" | "airworthiness management… compliance and airworthiness standards" | "track airworthiness and compliance" | "know you're airworthy, compliant and ready to fly" |
| Maintenance program → due list | Planning module: forecast, work packages, "regulatory limits" | planning modules (21-module suite) | Fleet Technical Mgmt | "View Due List", maintenance items, AD/SB monitoring | Smart Due List; "can I fly on that day?"; utilization assumptions; penalty events |
| Usage capture feeding schedule | AMOSeTL (e-techlog), flight-ops link | eMobility roles | Flight Operations product | Report Times, Update Utilizations, Flight Operations | Flight Scheduling integration; utilization assumptions |
| Work orders / work packages | work packages (Planning→Production) | production modules | MRO work orders | Work Orders (desktop+mobile) | Work Order container (planning/cost/execution) |
| Defects / non-routine / deferral | Maintenance Control: deferred defects, MEL items | AOG field ops roles | MRO ops | Non-routines, defect analysis | Observations |
| AD/SB management | Engineering compliance | engineering modules | compliance | AD and SB monitoring (automated updates) | AD/SB Manager (applicability, strategy, status) |
| Serialized components / rotables | Component Maintenance (serialised parts, traceability) | component maintenance modules | Component MRO | Inventory Management | IMS (rotables, requisitions) |
| Records / logbook / sign-off | paperless completion, audit readiness | "technical records", system of record | paperless | eLogbooks, eSignature, sign-off, history | ezVault, ezSign, traceable un-alterable records |
| Mobile execution at aircraft | AMOSmobile/EXEC | eMobility (14 roles) | Smart Wrench / Anywhere Apps | mobile app (crew + mechanics) | iCAMP mobile |
| Inventory / materials | Material Management, mobile STORES | inventory modules | supply chain | Inventory Management | IMS |
| Reliability / analytics | reliability data, root-cause | analytics | analytics | Diagnostics (defect analysis, reliability) | Fleet Analytics, EHM trending |
| Financial / commercial layer | Financial Mgmt, Commercial, AMOSmro | financial control | contract-to-cash | Work Center quoting/billing | cost-tracking in work orders |
| Human analyst service | no (software + services org) | no | no | no (explicitly contrasts: "no more lengthy waits for analysts") | yes (core of the offering) |
| Primary segment | airlines + MROs | airlines + MROs + lessors | airlines, MRO, defense, heli, UAS | B&G aviation → commercial, heli, MRO, OEM | business aviation, CAMO services, heli |

Layer B (cross-product commonality) findings:

1. Every product is organized around a **per-aircraft (per-tail) record** — the aircraft is the spine; components, work, usage, and costs all attach to it.
2. Every product frames its purpose as **airworthiness/compliance**, not merely maintenance work management.
3. Every product has a **due/forecast mechanism**: scheduled requirements whose due points are computed from usage (hours/cycles/calendar) and adjustable assumptions — not fixed calendar dates alone.
4. Every product has an **execution container** (work order / work package) that bundles tasks, materials, labor, and costs.
5. Every product handles **unscheduled work** (defects/non-routines) alongside scheduled work, with deferral tracking (MEL named explicitly in AMOS; deferral concept present across).
6. Every product maintains **AD/SB compliance** as a first-class tracked object.
7. Every product carries **serialized component / rotable accountability** (component shops, rotables, traceability).
8. Every product produces a **durable, attributed, sign-off-capable record** (e-logbook / records vault / "system of record") positioned as regulator-facing evidence.
9. Every product has a **mobile surface at the aircraft** and a **flight-usage input** (tech log or flight-schedule integration).
10. Inventory/materials and reliability analytics are present across the sample but as attached layers, not the spine.

Layer C (canonical inference) is developed in the L0–L3 abstraction below.

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

```text
Identified aircraft register (tail-numbered aircraft as individually managed, individually certified records)
└── Usage-driven maintenance program → per-aircraft due list
│   (scheduled requirements from the operator's program + authority/OEM mandates;
│    due points computed from accumulated usage: flight hours, cycles, calendar time)
└── Recorded maintenance events → per-aircraft airworthiness record
    (completed tasks, findings, defects and their disposition, sign-offs — the durable technical record)
└── Compliance oversight loop
    (an accountable maintenance organization monitors due vs done and acts:
     plan → execute → record → release/return to service)
```

Four properties. Remove any one and the product stops being an aircraft maintenance management system:

- **Aircraft register** — without identified per-tail records there is nothing to keep airworthy; it becomes generic asset maintenance.
- **Usage-driven program → due list** — without hours/cycles/calendar-driven due computation from a defined maintenance program, it is a generic CMMS with work orders, not aircraft maintenance.
- **Airworthiness record** — without the accumulated, attributed per-aircraft record, there is no compliance evidence; the product is a scheduling tool, not a system of record.
- **Compliance oversight loop** — without an accountable role acting on due status (plan, execute, record, release), it is a data store, not management.

Deliberately NOT in L0 (checked against the historical/market-sample test):

- **Work orders/work packages** — the dominant execution container in every sampled product, but paper-era and minimal tracking products schedule and record work without a formal work-order object; a minimal tracker remains recognizable without it.
- **Component/parts tracking** — near-universal and deep in mature products, but a minimal airframe-compliance tracker (register + program + due list + records) is still recognizably this Type; component accountability is the first thing added as products mature.
- **AD/SB management, MEL/deferral machinery, inventory, reliability programs, financial/commercial layers, mobile execution** — common or optional structures (L1/L2).
- **Specific check taxonomy (line vs base, letter checks)** — industry convention; observed only as "short-term tasks to long-term checks" and "Line and Base Maintenance" (AMOS); not definitional.

Historical / market-sample check (§24-style): the definition holds for paper-era practice (register + program + due list + logbook records, translated into software), for the EASA CAMO flavor and the FAA DOM flavor (both are the accountable-oversight role), for single-aircraft owner-operators (CAMP "Owners & Pilots" audience), for helicopter operators (usage counters differ, structure identical), and for defense fleets (readiness framing over the same structure). The definition does not depend on any single era, region, or vendor pattern.

### L1 — Common Mature Structure

Present in essentially all mature products (layer B):

- work orders / work packages as execution container (tasks, materials, labor, costs, progress)
- defect / non-routine reporting and deferral tracking (MEL-based deferral in regulated regimes)
- AD/SB compliance management (applicability, implementation status, revision tracking)
- serialized component tracking (component records with their own usage/history; rotables; shop visits)
- parts inventory / materials management (stock, requisitions, purchasing)
- electronic logbooks / records vault with e-signature and sign-off/release
- mobile execution at the aircraft (task cards, checklists, documentation)
- flight-usage capture (electronic technical logbook, utilization updates, flight-schedule integration)
- reliability / defect analytics (repeat-defect analysis, reliability programs, engine health trending)
- roles & permissions across maintenance control, planning, mechanics, engineering, quality, stores
- fleet status dashboards, due-list reports, cost reporting

### L2 — Variant / Optional Structure

- **Operating side**: operator-owned M&E vs third-party MRO business system (quotes, contracts, hangar planning, billing, customer portals — AMOSmro/Commercial, Veryon Work Center, Ramco "contract to cash") vs tracking-only for small fleets vs CAMO/records service posture.
- **Regulatory regime**: FAA vs EASA (CAMO) vs other authorities; program flavors (AMP/AAIP named by CAMP); regime shapes records and release vocabulary.
- **Segment**: airline fixed-wing, business/general aviation, helicopter/rotor-wing (mission-specific counters), defense (readiness framing), UAS/drones, ground support equipment (adjacent).
- **Check structure**: line vs base maintenance; short-term tasks through long-term checks; exact check taxonomy varies by operator program.
- **Engine/condition programs**: engine health monitoring, condition-trending, predictive maintenance (CAMP EHM, Veryon Diagnostics, AVIATAR ecosystem).
- **Technical publications**: integrated manual/regulatory libraries (Veryon Publications; ecosystem partners).
- **Deployment**: cloud SaaS vs hosted/on-prem enterprise; multi-entity financial management.
- **Service model**: pure software vs managed analyst service (CAMP) vs 24/7 support desk (Veryon).
- **Flight-ops coupling**: integrated flight scheduling vs third-party integration vs none.

### L3 — Vendor-specific (Research Notes only)

- AMOS: module names (AMOSeTL, AMOSmobile/EXEC, AMOSmobile/STORES, AMOSmro, AMOSsim), Failure Case Manager, Rotor Wing Excellence, edition categories (Airline/MRO/Component MRO/CAMO/Rotor Wing), Lufthansa-ecosystem partners (AVIATAR, flydocs).
- TRAX: eMRO/eMobility branding, "21 modules", "14 role-based applications", lessor positioning.
- Ramco: Aviation 6.0, Smart Wrench, flyMORE, "4000+ aircraft / 24000+ users" claims, G2 badges.
- Veryon: AIRE AI layer ("100m+ real-world maintenance events"), Tracking/Tracking+/Work Center/Diagnostics/Publications/GSE packaging, "25% of the worldwide commercial airline fleet" claim, FlightDocs app lineage.
- CAMP: MTX/EHM/IMS/FS/AHM naming, analyst service model, ezVault/ezSign/iCAMP, "5% resale price premium" claim, OEM-recommended positioning, CESCOM/AVTRAK legacy brands.

## Vendor-specific Findings

- CAMP's **human analyst service** is a genuinely different product philosophy (managed compliance service + tools), not an industry-wide structure; Veryon explicitly markets against it ("No more lengthy waits for analysts").
- Veryon's **AI layer (AIRE)** and Ramco's **Smart Wrench** are current-generation differentiators, not Type structure.
- AMOS's **edition taxonomy** (Airline vs MRO vs Component MRO vs CAMO) is a useful map of the market's sub-segments but is vendor packaging.
- TRAX's **lessor** positioning (records as lease/asset-value evidence) and CAMP's **resale-value** claim point to a real secondary job (records → asset value) that no other sampled vendor states as bluntly; treat as segment emphasis, not core.

## Boundary Findings

- **vs CMMS / Maintenance Management**: a generic CMMS manages equipment + work orders + PM schedules. Aircraft maintenance management is defined by the airworthiness regime: an approved maintenance program per aircraft, due points computed from flight usage (hours/cycles/calendar), authority/OEM mandates (ADs/SBs), serialized component accountability, and regulator-facing sign-off records. **Test: remove the airworthiness regime (program + usage-driven due + compliance record) and a CMMS remains.**
- **vs Enterprise Asset Management / EAM**: EAM spans asset classes with lifecycle/financial machinery; aircraft maintenance management is the aviation-specialized case with its own regulatory record structure. Gradient, not wall (Ramco sells both; AMOS has financial/HR modules). **Test: EAM's asset register is class-agnostic; here the register is tail-numbered aircraft under an airworthiness program.**
- **vs Fleet Management System (road)**: same family (fleet of mobile assets + oversight loop). FMS centers on vehicles-in-operation: drivers, telematics, dispatch, duty status. Aircraft maintenance centers on the airworthiness program and compliance record; there is no driver loop and no dispatch core. **Test: remove the airworthiness program/record and add drivers+telematics → FMS; conversely a tracking-only bizav product with no telematics is still aircraft maintenance management.**
- **vs Airline Operations Platform**: ops flies the schedule (crew, dispatch, passengers); maintenance keeps aircraft available. The handoff is the technical logbook / AOG state. **Test: remove flight schedule/crew/dispatch and keep the compliance loop → still this Type.**
- **vs Aftermarket Service Management / MRO business systems**: the MRO commercial wrapper (quotes → contracts → work → billing for customer-owned aircraft) sits on top of the same maintenance core. **Test: remove quotes/billing/customer accounts and the airworthiness core remains; that core is this Type.**
- **vs Inventory Management System**: parts inventory is a supporting module here; the spine is the aircraft + program + record. Standalone inventory systems lack the airworthiness loop.
- **vs Reliability Management**: reliability/defect analytics is an attached layer (L1), not the defining structure.

## Uncertainties

- Exact due-list mechanics (forecast windows, tolerance/penalty rules, hard vs soft limits) vary by product and are not publicly documented; the final document describes the mechanism generically.
- Specific certificate/form names for release-to-service were not observed in fetched pages; the document speaks of sign-off/release records generically.
- "Letter checks" (A/C-check) terminology is industry convention but was not directly observed in the fetched pages; only "short-term tasks to long-term checks" and "Line and Base Maintenance" (AMOS) were. The final document uses the observed phrasing.
- MEL deferral was directly observed only in AMOS; the deferral concept is cross-product. The final document phrases deferral generically with MEL as a named example from regulated regimes.
- The small-operator tier (sub-5-aircraft operators) was not directly sampled (Aables unreachable); CAMP's "Owners & Pilots" audience and Veryon's small-operator case studies provide indirect evidence that the same core structure scales down.
- Pricing, plan gating, and deployment details were not researched (not needed for the Type definition).

## Final Synthesis

An Aircraft Maintenance Management application is the **system of record for keeping a fleet of aircraft airworthy**. Its world is built on four structures: (1) a register of individually identified, individually certified aircraft; (2) each aircraft's maintenance program rendered as a usage-driven due list (hours / cycles / calendar, with forecast and assumptions); (3) a durable, attributed per-aircraft airworthiness record accumulating every completed task, finding, defect disposition, and sign-off; and (4) an accountable compliance loop — maintenance control / planning / CAMO / DOM — that monitors due vs done and drives work to completion and release. Around this spine, mature products add work packages, defect/MEL handling, AD/SB management, serialized component accountability, inventory, mobile execution, reliability analytics, and financial/commercial layers. The Type's boundary against CMMS/EAM is the airworthiness regime; against road-fleet management it is the absence of a driver/dispatch loop and the presence of the program/record; against airline operations it is the split between flying the schedule and keeping aircraft available; against MRO business systems it is the commercial wrapper around the same core.
