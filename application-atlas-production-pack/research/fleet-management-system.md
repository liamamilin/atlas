# Research Notes — Fleet Management System

Research date: **2026-09-06**
Methodology: `WORKFLOW_v1.1.md` + `WRITING_GUIDE_v1.1.md` (v1.1)

---

## Research Goal

Understand what a Fleet Management System (FMS) actually is as an Application Type: its core objects, the daily work it supports, its state/lifecycle rules, its user roles, and — critically — its boundaries against the many sibling leaves in DIRECTORY.md §18 (Vehicle Telematics Platform, Trucking Management System, Route Optimization Platform, Dispatch Management, Driver Management, Electronic Logging Device / HOS Platform, EV Fleet Charging Management, Autonomous Fleet Management) and against Enterprise Asset Management (§16).

## Initial Boundary (hypothesis before research)

- FMS = software for an organization that owns/operates a set of vehicles, to keep them visible, usable, compliant, and cost-controlled.
- Likely core: vehicle records + operational activity + fleet-side oversight.
- Most likely confusions: (a) telematics/GPS tracking products, (b) trucking/freight business systems, (c) route optimization, (d) generic asset management.
- Open question: is live GPS tracking definitional, or only the modern dominant implementation? (Historical check: pre-GPS fleet management existed as registers + maintenance logs.)

## Research Questions

1. What are the core objects (vehicle, driver, trip, event, alert, service record, inspection, fuel, compliance record)?
2. How does operational data enter the system (telematics device, driver mobile app, manual entry, integrations)?
3. What does a fleet manager do day-to-day (monitor → act loop)?
4. What does the driver do (mobile app loop)?
5. What vehicle lifecycle / status rules govern availability?
6. What rules matter (maintenance reminders, inspection grounding, HOS clocks, document renewal)?
7. Where is the FMS / telematics-platform boundary? FMS / TMS? FMS / route optimization? FMS / EAM?
8. Historical check: does the definition still fit pre-GPS, regional, government motor-pool fleet management?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / position | Tier |
|---|---|---|
| Samsara | Integrated fleet-operations cloud (safety/compliance/maintenance bundled with proprietary hardware) | Enterprise/mid-market |
| Geotab (MyGeotab) | Open telematics data platform; device-agnostic claims; SDK/marketplace | Enterprise + long tail via resellers |
| Fleetio | Fleet office / maintenance-records first; hardware-agnostic; telematics via integrations | SMB/mid-market |
| Motive | Driver- and compliance-first operations (ELD/HOS origin), trucking-heavy | SMB/mid-market trucking |

Verizon Connect was initially sampled (enterprise connectivity-derived vendor) but its official support surfaces returned 404 three times (`/help/`, `/support/`, `/knowledge-center/`); per the network-restriction rule it was dropped from the sample and no claims rely on it.

## Sources

Evidence layers: **A** = directly observed on an official source for a specific product; **B** = cross-product commonality; **C** = canonical inference.

Fetched successfully (all Layer A unless noted):

- Samsara Help Center — https://kb.samsara.com/ (help-center root; full section tree)
- Samsara — "Dashboard Menus" — https://kb.samsara.com/hc/en-us/articles/48621492984589-Dashboard-Menus
- Geotab — Fleet management software product page (Tier 2, marketing/product positioning) — https://www.geotab.com/fleet-management-software/
- Geotab — MyGeotab Product Guide (support.geotab.com/mygeotab/doc/product-guide; full documentation TOC)
- Fleetio Support Center — https://help.fleetio.com/ (root)
- Fleetio — Maintenance category — https://help.fleetio.com/en_US/maintenance
- Fleetio — Using Fleetio category — https://help.fleetio.com/en_US/using-fleetio
- Fleetio — Vehicle Overview — https://help.fleetio.com/en_US/vehicles/vehicle-overview
- Motive Help Center — https://help.gomotive.com/ (root)
- Motive — Driver App Overview — https://helpcenter.gomotive.com/hc/en-us/articles/31054123805853-Driver-App-Overview

Failed / abandoned:

- Verizon Connect — https://www.verizonconnect.com/help/ (404), /support/ (404), /knowledge-center/ (404) — abandoned after 3 attempts; Source-access Limitation recorded.

Not directly researched (see Uncertainties): European fleet-leasing systems, public-transit FMIS, standalone ELD products, TMS products.

---

## Product Observations

### Samsara (Layer A)

From Help Center root + "Dashboard Menus" article:

- Setup sequence documented as: set up organization in cloud → configure dashboard → download apps → activate hardware → install hardware. The product is organization-scoped from the first step.
- Dashboard menus (each gated by licenses and user role): **Overview** ("current location and status for fleet drivers and assets"), Workforce, **Safety** ("identify safety critical events and coach drivers"), **Compliance** ("track HOS logs and violations… ELD mandate"), **Maintenance** ("track DVIRs, establish preventive maintenance schedules, and view maintenance logs and real-time vehicle status"), **Dispatch** ("complete dispatch, create routes, and assign drivers"), Incident Center, **Fuel & Energy** ("fuel taxes and usage of drivers or vehicles"), Documents, Training, **Reports** ("location and utilization data of assets"), Workflows (digital forms), Issues.
- Hardware catalog: Vehicle Gateways, Asset Gateways (powered/unpowered), cameras, sensors, ID cards/tokens (driver assignment via QR/ID cards), engine immobilizer, satellite connectivity. Devices are activated and attached to vehicles from the dashboard.
- Driver App workflow sections: Start a Trip, HOS Compliance, End a Trip, Routes, Documents and Messages, Coaching and Training.
- Common help articles reference: "Admin Dashboard: Entering DOT Info", "Managing HOS Violations", "Driver App: Install & Login", "Editing HOS" — compliance is a first-class dashboard concern.
- Observation: the dashboard is organized by *management function* (safety / compliance / maintenance / dispatch / fuel), all operating over the same fleet of drivers + assets.

### Geotab / MyGeotab (Layer A for product guide TOC; Layer A/B for product page)

From MyGeotab Product Guide TOC (support.geotab.com):

- **Access and administration**: database setup, users, security clearances, system settings, audit log, rate plans. The fleet lives in a per-customer "database".
- **Device management**: device setup/removal, installation codes, device statuses and modes.
- **Managing users and vehicles**: users, drivers, **Assets (vehicles)**, asset types, archived assets, **assigning vehicles**, linked assets, work hours, Restricted Data Mode, Lost Mode.
- **Fleet activity**: **Map**, dispatching locations, **Trips** (Trips History, Trip Replay), **Routes** (planned routes), **Zones** (zone types, using zones on the map).
- **HOS and ELDs**: HOS setup, HOS rulesets, HOS logs.
- **Reports**: productivity, activity/trips summary, asset utilization, zone visits, route reports, maintenance reports, fault reports, mileage, safety (speeding, aggressive driving, idling, Driver Safety Scorecard), compliance (IFTA, time card, HOS logs, violations, driver availability), sustainability (fuel/energy usage, EV charging history).
- **Groups and rules**: groups, rules engine (rule conditions, custom rules, auxiliary rules), **rule-based maintenance automation**, notifications/distribution lists.
- **Maintenance and diagnostics**: asset maintenance, predictive maintenance insights, faults, measurements, **work order management** (work requests, work orders, maintenance jobs), maintenance schedules, asset inspections, engine hours.
- **Energy and sustainability**: fuel transactions, EV performance, EV charge monitoring.
- **Cameras and video**: camera management, video events, coaching.
- **Geotab Drive** (driver app): logging in, selecting/removing vehicles and trailers, HOS status page, HOS logs (editing a log), roadside checks, asset inspections (performing, certifying previous, repairing defects), co-drivers, messaging.

From the product page (Tier 2): MyGeotab described as "web-based fleet management software that provides a centralized view of your vehicle and driver data"; features: GPS vehicle tracking (near real-time + trips history + Privacy Mode), driver behavior management with Driver ID NFC, engine data reporting (RPM, engine light, seatbelt, odometer, engine hours, VIN, battery voltage), route optimization via zones, engine health and maintenance reminders, open data integration (SDK), device-agnostic software; software packages Basic/Regulatory/Pro/ProPlus; FAQ defines fleet management software as "a digital tool used to house data pulled from vehicles equipped with telematics devices".

Observation: Geotab's own FAQ frames FMS as the *management layer* over telematics data — useful for the telematics boundary.

### Fleetio (Layer A)

From Support Center + Using Fleetio + Vehicle Overview + Maintenance category:

- "**Vehicles are the heart of Fleetio.** A 'Vehicle' represents any asset or unit of equipment — moving or otherwise — managed in Fleetio." Examples include automobiles, farm equipment, trailers, construction equipment, boats, aircraft, rail cars, stationary engines/generators, cranes, forklifts. → the "vehicle" concept generalizes to powered equipment broadly.
- Vehicle record fields: unique **Name** ("in other systems… 'Asset ID', 'Vehicle ID', or 'Unit Number'"), year/make/model, VIN, license plate, specs, engine/transmission, tires, fluids, custom fields, financial info (price, purchase odometer, warranty), loan/lease details, vendors.
- Per-vehicle tracking objects: **Fuel Entries** (fuel transactions), **Service Entries** (completed service records), **Service Reminders** (PM schedule), **Issues** (general repairs), **Work Orders** (robust planning/tracking), **Meter Entries** (odometer/hour-meter history), **Renewal Reminders** (registrations, DOT inspections, emission tests), Tire Management, Warranty Management.
- Vehicles Index: saved views for **Assigned / Unassigned / Archived** vehicles; filter by Vehicle Type, Group, **Status**; bulk actions; import/export.
- Vehicle Details Page: fields card, open issues, service reminders, tabs for Telematics, Service History, Work Orders, Warranties; actions to add assignments, service/fuel/expense entries, work orders, issues, inspections.
- Maintenance module: Inspections, Issues/Faults/Recalls, Service Reminders & Schedules, Work Orders, Service Entries, Maintenance Categorization; explicit terminology article "Service Tasks vs. Issues, Service Entries vs. Work Orders"; Preventative Maintenance Compliance; **Faults imported from GPS tracking & telematics providers** (integrations).
- Other modules: Contacts/Users/Vendors ("Users in Fleetio are Contacts who have been granted access to log in"), Parts & Inventory, Purchase Orders, Tools, Fuel Entries, Expenses ("Total Cost of a fleet vehicle"), Analytics & Reports, Fleetio Go mobile app.
- Plan-gated: vehicle count limited by plan (e.g., Essential up to 100 vehicles); Work Orders on Professional/Premium.

Observation: Fleetio demonstrates that a fleet management product can exist with **no proprietary telematics hardware** — live data arrives via integrations; the register + maintenance + cost core stands alone.

### Motive (Layer A)

From Help Center root + Driver App Overview:

- Help center split by audience: **For drivers** (Driver App: connect to vehicles, edit logs), **For fleet managers** (Fleet Dashboard and Fleet App: "manage your vehicles, compliance, safety"), **For installers** (hardware: Vehicle Gateways, dashcams), plus Compliance / Safety / Motive Cards overviews.
- Driver App features: **HOS and compliance management** (HOS countdown clocks, proactive alerts, log signing, unidentified driving review, log edits); **connectivity to Vehicle Gateway** via Bluetooth (ELD; keeps logs/location without cellular); **vehicle inspections** (pre-trip and post-trip structured checklists, defect capture); **documents and qualifications** (forms, signatures, driver qualification documents); **dispatch management** (assignments, routes, stop workflows, status updates, proof-of-delivery); **driver safety performance** (training, safety event videos, self-coaching); **timecards**; **Motive Card** (fuel/expense spend); **messaging** with fleet managers.
- Trending topics: Safety Score, pairing mobile device to Vehicle Gateway (ELD), switching Cycle Rule, Personal Conveyance — compliance vocabulary dominates.

Observation: Motive shows the driver-side surface in its fullest form: the driver is a first-class user of the same fleet system, not just a data source.

---

## Cross-product Comparison

| Dimension | Samsara | Geotab MyGeotab | Fleetio | Motive |
|---|---|---|---|---|
| Organizational register of vehicles | Assets (vehicles + asset gateways) | Assets (vehicles), asset types, archived assets | "Vehicles are the heart"; any equipment | Vehicles on Fleet Dashboard |
| Vehicle identity fields | device-bound assets | VIN auto-read from engine data | Name/Unit Number, VIN, plate, specs, financials | vehicle records on dashboard |
| Vehicle status / availability | "real-time vehicle status" (Maintenance) | archived assets; assigning vehicles | Assigned/Unassigned/Archived views; Status filter | — (not directly observed) |
| Driver identity & attribution | Driver App + ID cards/QR tokens | Driver ID NFC; users w/ security clearances | Contacts/Users; vehicle assignments | Driver App login; unidentified driving review |
| Live location / map | Overview menu (location + status) | Map, Trip Replay | Telematics tab via integrations | Vehicle Gateway + Driver App |
| Trips history | Trips (driver workflow) | Trips History | via telematics integrations | — |
| Zones / geofences | not directly observed | Zones, zone types, zone visits | not directly observed | not directly observed |
| Rules / alerts / notifications | safety critical events | rules engine, custom rules, notifications | service reminders; faults | proactive alerts, safety score |
| Maintenance management | DVIRs, PM schedules, maintenance logs | work orders, schedules, faults, predictive maintenance | Inspections, Issues, Service Reminders, Work Orders, Service Entries (core) | driver-side inspections |
| Fuel / energy | Fuel & Energy (taxes, usage) | fuel transactions, EV charge monitoring | Fuel Entries, Expenses | Motive Card (fuel spend) |
| Compliance | HOS logs/violations, ELD, DOT info | HOS rulesets/logs, IFTA, violations reports | Renewal Reminders (registration, DOT inspections) | HOS clocks, cycle rules, roadside inspections |
| Driver mobile app | Driver App (trips, HOS, routes, docs, coaching) | Geotab Drive (HOS, inspections, roadside) | Fleetio Go | Driver App (fullest: dispatch, docs, timecards) |
| Reports / analytics | Reports menu | extensive report suite | Analytics & Reports | — |
| Roles / permissions | menus gated by licenses + role | security clearances | Account Owner/Admin/User permissions | manager vs driver surfaces |
| Telematics posture | proprietary hardware bundled | proprietary devices + device-agnostic claims | hardware-agnostic, integrations | proprietary hardware (ELD gateway) |
| Dispatch / routes | Dispatch menu (routes, assign drivers) | planned routes, dispatching locations | absent | dispatch in Driver App |

### What is universal (Layer B)

- An organization-scoped **register of vehicles** as individually identified, managed records.
- A **per-vehicle operational record** accumulated over time (usage/meters, trips/positions, events, service history, costs).
- A **fleet-side oversight role** distinct from the driver, with a monitor → act loop.
- **Vehicle status/assignment** as a first-class state (assigned/unassigned, archived, in/out of service).
- **Maintenance management** in some depth (reminders/schedules + records; work orders in 3 of 4).
- **Driver dimension** (records, assignment, identification) in all 4.
- **Compliance surfaces** (HOS/ELD in trucking-facing products; document renewal reminders in the maintenance-first product).
- **Reports/dashboards** over the accumulated record.
- **Role separation** between admin/manager, supervisor, maintenance, and driver.
- **Driver mobile app** in all 4 (depth varies).

### What varies (Layer B/C)

- Whether telematics hardware is proprietary-bundled, optional, or integration-based.
- Depth of maintenance (core in Fleetio; one menu among many in Samsara; work-order module in Geotab).
- Depth of compliance (defining concern for Motive; one module for others).
- Presence of dispatch/routing (optional module; absent in Fleetio).
- Platform openness (Geotab SDK/marketplace vs closed clouds).
- Energy/EV, video safety, spend cards — optional modules in some products.

---

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately minimal)

```text
Fleet register
  (one organization's vehicles as individually identified, managed records)
└── Per-vehicle in-service operational record
    (usage, status, events, service, cost accumulated over the vehicle's service life)
└── Operator oversight loop
    (fleet-side role monitors fleet state and acts on individual vehicles:
     assign, service, ground / return to service, report, dispose)
```

Three properties. Rationale:

- **Fleet register** — without identified vehicle records there is nothing to manage; the product is not fleet management.
- **Per-vehicle in-service operational record** — the vehicle record is a *living operational file*, not a static spec sheet. Without accumulated activity the product is a static asset list (Enterprise Asset Registry territory).
- **Operator oversight loop** — the "management" in fleet management: an organization-side role monitors and acts. Without it, the product is a telematics data feed or a driver tool, not a management system.

Deliberately **excluded from L0** (tested against §24 historical check):

- **Live GPS tracking / telematics** — pre-GPS fleet management (paper registers, garage maintenance ledgers, motor-pool checkout systems) is still recognizably fleet management; modern tracking is the dominant data-acquisition implementation, not the definition. Geotab's own FAQ frames FMS as the management layer over telematics data; Fleetio operates with telematics only via integrations.
- **Maintenance management** — near-universal in mature products, but tracking-only products are still marketed and recognized as fleet management; and historical FMS was often maintenance-led. It is the strongest L1 candidate, not definitional.
- **Driver records / HOS / compliance** — the driver dimension is extremely common (all 4 sampled products) but a fleet register + usage record + oversight can exist without per-trip driver attribution (e.g., motor-pool checkout by any employee); HOS/ELD is a regulatory-regime overlay (L2).
- **Fuel / cost modules, safety scores, dispatch, reports** — common or optional, not definitional.

### L1 — Common Mature Structure

- **Telematics data acquisition** — GPS/vehicle gateways, live map, trip history, engine data (odometer, engine hours, faults). Dominant modern implementation; may be proprietary hardware, third-party devices, or integrations.
- **Driver management** — driver records, vehicle–driver assignment, driver identification (NFC/QR/Bluetooth login), license/qualification documents.
- **Maintenance management** — service reminders / PM schedules (meter- or time-triggered), work orders, service entries, issues/faults, inspections (incl. driver DVIR-style inspections).
- **Compliance management** — HOS/ELD logs and violations (regulated trucking), IFTA/fuel-tax reporting, renewal reminders for registration/inspection/emission documents.
- **Fuel & cost tracking** — fuel entries/transactions, expenses, cost-per-vehicle / total-cost-of-ownership reporting.
- **Safety management** — safety events, driver scores, coaching workflows (often camera-backed).
- **Rules / alerts / notifications** — configurable conditions over fleet data with notification routing.
- **Fleet grouping** — groups/teams/vehicle types to structure large fleets and scope visibility.
- **Reports & dashboards** — utilization, mileage, idling, safety, maintenance, compliance reporting.
- **Roles & permissions** — admin/manager vs supervisor vs maintenance vs driver; license/plan gating of modules.
- **Driver mobile app** — driver-side surface for identification, inspections, logs, tasks, messaging.
- **Dispatch / routes / zones** — job assignment and planned-route features (present in some products, absent in others).

### L2 — Variant / Optional Structure

- **Segment variant**: trucking/compliance-heavy (ELD/HOS/IFTA dominate) vs corporate/service van fleets vs government/motor-pool vs mixed-equipment fleets (Fleetio's "vehicle" spans trailers, construction equipment, boats, aircraft, rail cars, generators).
- **Telematics posture**: proprietary hardware bundle vs hardware-agnostic/integration-based vs device-agnostic open platform.
- **Platform openness**: open SDK/API/marketplace (Geotab) vs closed integrated cloud.
- **Regulatory regime**: US FMCSA (ELD/HOS/IFTA/DOT inspections) vs other jurisdictions' rules; rulesets configurable per product.
- **Energy variant**: ICE fuel management vs EV energy/charging management.
- **Optional modules**: video-based safety/cameras, dispatch/documents/workflows, timecards, spend cards, parts inventory, engine immobilizer.
- **Deployment**: cloud SaaS is the current norm; historically on-prem/garage systems (L0 unaffected).

### L3 — Vendor-specific (Research Notes only)

- Samsara: Agent Studio, MEM (Mobile Experience Management), Ground Intelligence, Incident Center; specific hardware models (VG54/VG55, AT11–AT13 asset tags); license-gated menus.
- Geotab: MyGeotab MCP Connector, Data Connector, BAR-CTP, GO device line (GO7/GO8/GO9), IOX add-ons, software packages (Base/Regulatory/Pro/ProPlus), Predictive Maintenance Insights, Collision Risk.
- Fleetio: Maintenance Shop Network, Auto Integrate, Smart Uploads, AI Service Advisor (beta), plan limits (e.g., Essential ≤ 100 vehicles), Service Programs vs Service Reminders terminology.
- Motive: AI Coach, Savings Finder, Motive Card, Vehicle Gateway ELD hardware line, cycle-rule switching UI.
- None of these enter the final document except as neutral examples where useful.

---

## Vendor-specific Findings

- Geotab markets "device agnostic software" and an open SDK — a positioning claim (Tier 2) that distinguishes it from closed-stack competitors; treat as vendor positioning, not a Type property.
- Fleetio's generalization of "Vehicle" to boats/aircraft/rail cars/cranes shows one vendor drifting toward generic equipment management; other sampled products stay road-vehicle-centric. This is a vendor scope decision, not a Type requirement.
- Motive's Driver App bundles dispatch, documents, timecards, and spend cards — a trucking-operations bundle beyond the FMS core.
- Samsara gates dashboard menus by license + role — an implementation of module packaging, not a structural property.

## Boundary Findings

- **vs Vehicle Telematics Platform** (sibling, §18): telematics is the *data-acquisition/connectivity layer* (devices, data pipelines, APIs). FMS is the *management application* over fleet operations. Evidence: Geotab's FAQ ("fleet management software is a digital tool used to house data pulled from vehicles equipped with telematics devices"); Fleetio treats telematics providers as integrations that import faults/odometer. Test: remove the register + oversight loop and a telematics product remains; remove the raw data feed and a register-led FMS (Fleetio-style, historical FMIS) remains. Different Types; FMS commonly *bundles* telematics (L1).
- **vs Trucking Management System** (sibling, §18): TMS manages the freight *business* (orders, loads, carriers, billing); FMS manages the owned fleet as *assets in operation*. A trucking company typically runs both. Not directly researched with a TMS product in this pass — assertion kept at canonical-inference strength.
- **vs Route Optimization Platform** (sibling, §18): route optimization computes plans; FMS records and oversees execution. Some FMS include basic routes/zones (Geotab planned routes, Samsara Dispatch) as L1/L2 capability — the algorithmic planning product remains a different Type.
- **vs Dispatch Management** (sibling, §18): dispatch appears in sampled FMS products only as an optional module (Samsara Dispatch menu; Motive driver-app dispatch) and is absent in others (Fleetio). Job-dispatch-to-field-workers is its own Type; its presence in an FMS is a bundle.
- **vs Electronic Logging Device / HOS Platform** (sibling, §18): ELD/HOS is a regulatory-compliance capability (L1 in trucking-facing FMS; L2 overall). Standalone ELD products exist; the FMS contains compliance as one surface among several.
- **vs Driver Management** (sibling, §18): driver records/scores/assignments are L1 inside FMS; a standalone Driver Management Type would center the driver rather than the fleet. Boundary deserves a joint pass when that leaf is processed.
- **vs Enterprise Asset Management / Enterprise Asset Registry** (§16/§10): EAM spans all asset classes with lifecycle/work-order/depreciation machinery; FMS specializes in vehicles *in operation* with movement/usage telemetry and a driver dimension. Fleetio's equipment generalization shows the boundary is a gradient (mixed equipment fleets), not a wall.
- **vs EV Fleet Charging Management / Autonomous Fleet Management** (siblings, §18): energy/charging and autonomy are L2 overlays on the same core (Geotab EV charge monitoring inside MyGeotab); dedicated leaves likely behave as variants or as separate infrastructure Types (charging networks). Flag for joint review.
- **vs Robot / Mining / Marine Fleet Management** (siblings, §16/§18/§20): the same oversight pattern (register + activity + control loop) generalizes to non-road vehicle fleets, but those leaves carry domain-specific telemetry and operations. The road-vehicle FMS core model does not capture e.g. vessel/voyage or mine-site specifics; treat as related Types, flag for joint review.
- **"去掉什么就变成另一个 Type" 判据**: remove the *operator oversight loop* → telematics platform / driver app; remove the *fleet register* (vehicles as managed records) → route optimization or dispatch; remove the *vehicle-in-operation specialization* → generic EAM; remove the *organization scope* → consumer vehicle app (not in directory).

## Historical / Market-Sample Check (§24)

- Pre-GPS era: fleet management existed as paper/spreadsheet registers + garage maintenance logs + motor-pool checkout records (government FMIS tradition). These satisfy the L0 (register + operational record + oversight) with none of the modern telematics/driver-app/HOS machinery. → L0 survives.
- Regional check: the sampled products are North-America-centric (ELD/HOS/IFTA vocabulary). The L0 deliberately excludes US-regulatory specifics; compliance appears in L1 as "compliance management" with regime-specific rulesets in L2. European/Asian fleet-leasing and leasing-company systems were not directly fetched; the L0 is designed to accommodate them but this is not directly verified (see Uncertainties).
- Platform-native check: OEM-built vehicle apps (e.g., manufacturer fleet portals) were not sampled; they would satisfy the L0 if they maintain a register + operational record + oversight for an organization.

## Uncertainties

1. Verizon Connect official docs could not be fetched (3× 404). No claims rely on it. The enterprise-connectivity vendor perspective is therefore under-sampled.
2. Exact vehicle-status vocabularies differ per product (Active / In service / Out of service / Archived / Assigned / Unassigned). The document describes status conceptually and does not assert a universal state list.
3. Whether dispatch/routes belong in FMS core: evidence shows optional-module status; classified L1/L2, but the boundary with Dispatch Management deserves a joint pass when that leaf is processed.
4. Historical/regional products (public-transit FMIS, European leasing systems) were reasoned about abstractly, not fetched; the historical-fit claim for L0 is canonical inference (Layer C), not direct observation.
5. Zone/geofence features were directly observed only in Geotab's TOC; treated as L1 "common" rather than universal.

## Final Synthesis

A Fleet Management System is the organization-facing management application for a fleet of vehicles: it keeps a register of the organization's vehicles as individually identified managed records, accumulates each vehicle's in-service operational record (usage, status, events, service, cost), and gives fleet-side staff a continuous oversight loop — monitor the fleet, then act on individual vehicles (assign drivers, schedule and record service, ground or return vehicles, report, dispose). Telematics/GPS tracking, driver apps, maintenance modules, compliance (HOS/ELD), fuel/cost, and safety are the common mature structures that make modern FMS powerful, but none of them is individually definitional: historical register-led systems and integration-based products remain recognizably FMS without them. The Type is bounded against telematics platforms (data layer), TMS (freight business), route optimization (planning algorithms), dispatch (job assignment), ELD/HOS (compliance capability), and EAM (all-asset lifecycle) by its union of fleet register + per-vehicle operational record + operator oversight loop over vehicles in operation.
