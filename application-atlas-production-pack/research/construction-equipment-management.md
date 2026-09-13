# Research Notes — Construction Equipment Management

Research date: 2026-09-07
Leaf: Construction Equipment Management (DIRECTORY §17 Construction, Real Estate & Facilities)
Slug: construction-equipment-management

---

## Research Goal

Understand what "Construction Equipment Management" software actually is as an Application Type: what the managed population is, what core objects exist, what users do with them, how the daily work flows, which rules and states matter, and where the boundary lies against neighboring Types (telematics platforms, road fleet management, CMMS/EAM, tool management, materials management, rental management).

## Initial Boundary (hypothesis before research)

- Hypothesis: contractor-side management of heavy mobile work machines (excavators, dozers, loaders, cranes, aerial platforms, generators, trucks, attachments) — a registry of machines, tracking of where they are and how much they work, allocation to jobsites, maintenance, and cost control.
- Likely confusions:
  - Vehicle Telematics Platform (data feed vs system of record)
  - Fleet Management System (road vehicles, driver-centric)
  - CMMS / EAM (maintenance-centric, stationary plant)
  - Tool Management (small tools)
  - Construction Materials Management (consumables vs reusable machines)
  - Equipment rental management (rental-company business systems)
- Unknowns at start: is allocation-to-jobs definitional? Is maintenance definitional? Is telematics definitional (historical check)? Does the rental-company perspective belong inside this Type?

## Research Questions

1. How is an individual machine recorded (identity, attributes, owned vs rented)?
2. How are location and usage captured (telematics, manual meter readings, scans, timesheets)?
3. How do machines get bound to work (jobsite assignment, dispatch, transfers, rental commitments)?
4. How is upkeep managed (inspections, PM triggers, work orders, mechanic execution, parts)?
5. How is utilization defined and measured (hours, idle vs active, PTO, benchmarks)?
6. How does cost flow (ownership cost, charge-out/job costing, rental billing, buy/rent/retire decisions)?
7. What interfaces exist (web fleet views, maps, schedulers, mobile apps for operators/mechanics)?
8. What alerts and rules matter (maintenance due, fault codes, geofence, idle, unauthorized movement)?
9. Where is the boundary against telematics-only products and OEM portals?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

1. **Tenna** — construction-specific "equipment management software" platform (asset tracking + maintenance + dispatch + safety + financials + proprietary tracker hardware). Mid-to-large contractors. Full-platform pole.
2. **EquipmentShare T3** — telematics-first construction fleet management & equipment tracking platform, tied to a large rental company; trackers, keypads, dash cams, work orders, rentals/billing. Tracking-first pole; serves contractors of many sizes.
3. **Assignar** — construction operations platform, scheduling-first: crews AND equipment scheduled onto work orders; timesheets, forms, job costing. Subcontractors (civil, crane, excavation, rail...). Scheduling-first pole.
4. **HCSS Equipment360** — maintenance-shop-first equipment fleet management for heavy civil contractors (PM, work orders, inspections, parts inventory, mechanic time cards). Maintenance-first pole; mid-to-large contractors.

Rejected / not sampled directly:
- **Trackunit** (telematics-first, OEM-agnostic, rental + construction): www.trackunit.com returned 403, developer.trackunit.com transport error — abandoned after 2 failures per network rule. Its rental-fleet perspective is underrepresented in this sample.
- **Caterpillar VisionLink / Komatsu KOMTRAX** (OEM-native telematics portals): cat.com 403, komatsu.com 404 (two URL variants), visionlinkonline.com is an unrelated squatted blog. Treated as a boundary observation with reduced evidence, not as a sampled product.
- **Equipment rental management systems** (rental-company ERP class): different Type; noted in boundary findings only.

## Sources

All fetched 2026-09-07 (Tier 1/2 official vendor surfaces):

- Tenna homepage: https://www.tenna.com/
- Tenna one-platform use case: https://www.tenna.com/use-cases/equipment-management-system/
- Tenna equipment management use case: https://www.tenna.com/use-cases/construction-equipment-management/
- Tenna equipment utilization: https://www.tenna.com/construction-asset-management/equipment-utilization/
- EquipmentShare homepage: https://www.equipmentshare.com/
- EquipmentShare T3: https://www.equipmentshare.com/t3
- T3 Help Center (collections index): https://help.estrack.com/en
- Assignar homepage: https://www.assignar.com/
- Assignar scheduling: https://assignar.com/scheduling-assigning/
- HCSS Equipment360: https://www.hcss.com/products/equipment360/

Source-access limitations:
- Trackunit and OEM portals (VisionLink, KOMTRAX) unreachable → the OEM-bound telematics pole and the rental-fleet-management perspective are covered only indirectly (via Tenna's OEM/AEMP integration documentation and T3's rental collections). Assertions about those products are NOT made in the final document.
- All fetched pages are marketing/product surfaces plus one help-center index; no per-feature help articles were fetched for T3/Assignar. Operational precision (exact defaults, numeric limits) is therefore avoided in the final document.

---

## Product A — Tenna (full-platform pole)

### Key observations (Evidence layer A unless noted)

- Self-positioning: "Equipment management software powering mixed fleet operations"; "one end-to-end solution"; "Built for construction".
- Vendor definition of the Type (FAQ): "Construction equipment management is the process of tracking, maintaining, and optimizing heavy equipment, vehicles, and construction assets to improve productivity, reduce costs, and ensure safety and compliance on construction projects."
- Vendor definition of an equipment management system (FAQ): "software that helps construction companies track, maintain, schedule, and analyze equipment across its entire lifecycle — including location, utilization, maintenance, and performance — in one centralized system."
- Managed population: "heavy and mid-sized equipment, heavy trucks and vehicles (on-road and off-road), mid-sized assets (with and without engines), attachments, parts, tools and small assets, inventory and consumables"; "Track owned, rented, and third-party assets from one place."
- Product modules: Asset Tracking & Management (sites/maps/geofences, utilization, analytics, mobile app); Maintenance (preventive maintenance, work orders, parts, mechanic time cards, cost codes); Cameras/Safety/Compliance (AI dash cam, driver & operations scorecards, custom inspections, DVIR/ELD/IFTA fleet compliance); Resource Management & Dispatching (schedule); Asset Financials ("equipment job costing and billing powered by telematics"); Integrations (accounting/ERP, construction software, OEM telematics & AEMP, fuel, parts procurement); Asset Trackers (CANbus, GPS, BLE beacon, QR, cameras).
- Asset detail hub: "comprehensive, searchable database of every piece of equipment... location, jobsite assignment, work history, cost, hours, and attachments in one central hub."
- Utilization data points: engine hours, mileage, PTO engagement, idle vs active time, GPS location. Configurable utilization parameters per asset category; custom benchmarks/thresholds by asset type/category/fleet-wide ("underutilized equipment is flagged against targets you've defined, not generic defaults").
- Utilization → decisions: reassign under-used equipment, reduce idle, right-size fleet, buy/rent/retire, bid rates, retirement timing.
- Utilization → maintenance: "Trigger maintenance tasks based on actual runtime hours, PTO engagement, or other usage thresholds"; "usage-based rather than just date-based".
- Utilization → billing: "For contractors renting out machines, this means easy gathering of utilization hours and proper billing of clients for equipment usage."
- Asset Financials questions: which assets generate value vs ownership cost; are equipment costs recovered on every job; buy/rent/redeploy/retire.
- Dispatching: "equipment requests, asset and crew scheduling, and transfers between jobsites using telematics."
- Mobile field app: "operators and foremen can check assets in and out, complete digital inspections, track hours, capture photos, and update equipment status."
- Alerts: "failed inspections, fault codes, maintenance schedules, geofence breaches, idle thresholds, unauthorized movement."
- Roles: Field / Shop / Office.
- Anti-boundary evidence: "How is Tenna different from fleet-only platforms like Samsara, Motive, or Verizon? Fleet-only platforms focus primarily on vehicles and compliance. Tenna is a system for managing complete construction fleets... mixed fleets, maintenance workflows, and asset data all in one place." Also OEM telematics & AEMP listed as INTEGRATIONS — OEM portals are data sources feeding the system, not the system itself.

## Product B — EquipmentShare T3 (tracking-first pole)

### Key observations

- Self-positioning: "T3 by EquipmentShare: Construction Fleet Management & Equipment Tracking"; "Modern Fleet Management powered by T3".
- T3 solutions: 1.0 Fleet management (asset location, maintenance, usage data); 2.0 Dash Cams; 3.0 Security & Theft Prevention ("monitor asset movement and jobsite entry/exit in real time; instant SMS or email alerts for use outside of business hours"); 4.0 Compliance & reporting (DOT and OSHA inspection needs); 5.0 Safety & Accountability.
- Asset trackers: "Real-time GPS tracking; machine monitoring including engine mileage, utilization and more; geofencing and custom SMS alerts."
- Cloud-connected keypad: "access control and security for heavy-duty equipment; monitor usage and operator history; restrict access to authorized users; reduce theft and engine run time."
- Bluetooth tags: location tracking for "tools, buckets, attachments".
- Homepage feature set: track equipment location; set service & fuel alerts; stop theft with keypads & cameras; GPS tracking to locate downed machines; alerts for service intervals; understand machine issues without being on-site.
- T3 Help Center collections (structure of the product): Tracking and Managing Fleet ("Rentals, Billing, Alerts, Geofences, Access Keypad, and Work Orders" — 56 articles); Reserving and Managing EquipmentShare Rentals (38); Analytics & Dashboards; Time Cards; Managing Inventory of Items (CostCapture/Inventory web apps, purchase orders); Link Mobile App ("asset location and servicing WO"); ELD Compliance with E-Logs; Asset Telematics Hardware; Dash Cam; Keypads & Keycodes; T3 Asset Insight (field equipment info); Integrations (14 articles).
- Dual posture: T3 runs EquipmentShare's own rental fleet AND is sold to contractors for their own assets; the "Reserving and Managing EquipmentShare Rentals" collection is the renter-side surface (renting-in), while fleet/work orders/billing serve owned fleets.
- Customer quote (Yates Construction): "real-time insights into asset location, maintenance, usage, and trade partner management".

## Product C — Assignar (scheduling-first pole)

### Key observations

- Self-positioning: "The construction platform that connects Field to Finance"; "unites your crews, compliance, and cash flow".
- Equipment as a schedulable resource: "See where your people and equipment are at a glance. Drag-and-drop qualified and available resources into the calendar to schedule them and notify them immediately. Extend orders and remove workers in just a click."
- Work order → scheduler: "When you create a work order in Assignar, it automatically populates into the Scheduler, ready to be filled with the resources that can do the job."
- Recommendation engine for qualified/available workers; jobsite app; text notifications; supervisors add/remove workers on shifts.
- Resource attributes: "Connect important details to your resources, including availability and certifications."
- Time tracking: mobile clock in/out, timesheets, activities, breaks; supervisors complete crew timesheets.
- Forms & field data for compliance; reporting & insights ("schedule to improve utilization"); job costing, pay rates, schedule of rates (T&M); ERP/accounting integrations.
- Industries: crane & rigging, heavy civil, excavation, traffic, demolition, concrete, asphalt & paving, rail, infrastructure, scaffolding.
- Note: maintenance of equipment is NOT a surfaced module in the fetched pages — this product represents the allocation-first realization where upkeep is handled outside or lightly. (Evidence limitation: only homepage + scheduling page fetched.)

## Product D — HCSS Equipment360 (maintenance-first pole)

### Key observations

- Self-positioning: "Equipment360 is a full-featured equipment fleet management system designed to run complete maintenance shop operations... built for mid-to-large enterprise contractors who manage fleets of 50 to 2,000+ heavy assets." (vendor marketing claim — product-specific)
- Modules: Inspections ("automate your work orders after an inspection"), Preventive maintenance ("automatic alerts for equipment certifications, work order due dates, inspections"), Work orders ("track equipment history, maintenance costs, and performance"), Inventory management ("track parts, purchases, and invoices; automatic alerts when it's time to stock up"), Maintenance requests ("put in repair orders straight from the field").
- PM triggers: "automatically tracks equipment usage and generates preventive maintenance schedules and work orders based on meter readings (hours/mileage) captured from telematics or manual field meter readings, or by set dates."
- Mechanic mobile app: "view work order assignments, enter shift time, add parts, upload photos, log corrective notes, and even trigger preventive maintenance services."
- Mechanic time cards & payroll: time against work orders; pay adjustments (per diem, travel, rig pay); syncs with payroll/accounting.
- Alerts: "certification and licensing for your equipment, due dates for your work orders, field requests, preventative maintenance, reorder level for your inventory items, skills for your employees, and warranties for your equipment... easily turned into work orders in three clicks." (product-specific phrasing)
- Customer narrative (Lecon): per-machine record ("pull up a particular machine... everything I need to know"), service alarms at hour thresholds, work orders with work items/repair/hours/photos "stored for future reference", mechanic assignment, accounting flow from mechanic entries.
- Suite context: HCSS Dispatcher (dispatching crews/equipment) and HCSS Telematics (GPS devices) and Fuel Management are separate sibling products; E360 integrates with HeavyJob (job costing) — maintenance data flows to job cost.
- Smaller-fleet sibling: "HCSS Fleet Maintenance is geared toward small-to-medium businesses needing simple preventive and light corrective repair tracking" — segment laddering inside one vendor.

---

## Cross-product Comparison

| Dimension | Tenna | EquipmentShare T3 | Assignar | HCSS Equipment360 |
|---|---|---|---|---|
| Self-label | equipment management software / one platform | construction fleet management & equipment tracking | construction operations platform (field→finance) | equipment fleet management system (shop operations) |
| Managed population | heavy/mid equipment, trucks, trailers, attachments, parts, tools, consumables; owned + rented + third-party | assets (equipment + vehicles), tools/attachments via BT tags; own + rented fleet | equipment as schedulable resource beside crews | heavy equipment fleet (register of machines) |
| Machine identity | searchable asset database: location, jobsite assignment, work history, cost, hours, attachments | asset records bound to trackers/keypads; operator history | resource records with availability/certifications | equipment records: make/model, work history, warranties, certifications |
| Location/usage capture | GPS/CAN/BLE/QR trackers + OEM telematics (AEMP) | GPS trackers, keypad, BT tags | timesheets/field data (no telematics emphasis) | telematics OR manual meter readings OR dates |
| Utilization | engine hours, mileage, PTO, idle vs active; configurable per-category benchmarks | utilization reports; access-control-based usage | scheduling utilization reporting | usage data drives PM |
| Allocation to work | dispatching: requests, asset+crew scheduling, transfers between jobsites | rentals (reserving/managing), billing | work orders → drag-drop scheduler (core) | via sibling Dispatcher product |
| Upkeep loop | PM, work orders, parts, mechanic time cards, cost codes | work orders, service & fuel alerts, service intervals | not surfaced | PM by hours/miles/dates, work orders, inspections, parts, mechanic time, field requests |
| Inspections/compliance | custom inspections, DVIR/ELD/IFTA, DOT/OSHA | ELD/E-Logs, DOT/OSHA | forms & compliance | inspections → work orders; certification alerts |
| Cost layer | Asset Financials: job costing + internal billing powered by telematics; TCO | billing (rental + fleet), CostCapture inventory | job costing, pay rates, T&M | maintenance costs per WO; HeavyJob/payroll sync |
| Alerts | failed inspections, fault codes, maintenance due, geofence, idle thresholds, unauthorized movement | service & fuel alerts, after-hours movement | schedule notifications | PM due, certifications, warranties, reorder levels |
| Mobile surfaces | operator/foreman app (check in/out, inspections, hours, photos, status) | Link app (asset location, servicing WOs) | field app (timesheets, forms) | mechanic app (WOs, time, parts, photos) |
| Integrations | ERP/accounting, project mgmt, OEM telematics/AEMP, fuel, parts procurement | integrations collection, ELD | ERP/accounting | HeavyJob/HeavyBid, payroll/accounting |
| Hardware bundling | yes (tracker family) | yes (trackers, keypad, cams, tags) | no | optional (HCSS Telematics) |

### Stable commonalities across the sample (Evidence layer B)

1. A persistent, searchable register of identified machines (with category, identity attributes, status, history).
2. Per-machine operating state over time: where it is and whether/how much it ran (hours/utilization), captured by telematics, manual meter readings, scans, or timesheets.
3. Binding machines to work over time: jobsite assignment / scheduling / dispatch / transfers; rental commitments where rentals are involved.
4. Utilization as the central performance question (active vs idle; per asset/category/jobsite).
5. Cost visibility tied to machines and jobs (ownership/operating cost, charge-out or job costing, rental billing).
6. Alerts/notifications on operational exceptions (maintenance due, fault codes, movement/geofence, idle).
7. Mobile field surfaces for operators/foremen/mechanics.
8. Integration outward: ERP/accounting, project management, OEM telematics.

### Divergences

- Upkeep depth: full shop management (E360, Tenna) vs alert-and-work-order (T3) vs not surfaced (Assignar).
- Allocation depth: core scheduler (Assignar) vs dispatch module (Tenna) vs rental commitments (T3) vs sibling product (HCSS Dispatcher).
- Hardware: bundled trackers/keypads/cams (Tenna, T3) vs software-only (Assignar) vs optional devices (HCSS).
- Road-vehicle compliance machinery (ELD/DVIR/IFTA): strong in Tenna/T3 (mixed fleets with trucks), absent in E360's shop focus.
- Safety/video telematics (dash cams, scorecards): Tenna, T3; not in E360/Assignar fetched surfaces.

---

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

1. **Equipment asset register** — persistent, identified records for the mobile work machines (and their attachments) the company owns or controls. The managed population is machines, not people, materials, or contracts.
2. **Tracked operating state over time** — for each machine: where it is and whether/how much it has been working (usage hours / utilization), captured by whatever means the era allows (telematics, manual meter readings, scans, timesheets).
3. **Allocation of machines to work over time** — binding machines to jobsites/jobs (or rental commitments) and moving them between them.

Rationale: remove (1) → nothing remains; remove (2) → a static asset ledger (fixed-asset register), not equipment management; remove (3) → a monitoring/telematics viewer, which the market treats as a data-feed product that equipment management systems integrate (Tenna lists OEM telematics/AEMP as integrations). Upkeep, cost, alerts, mobile apps are all near-universal but each is absent or thin in at least one sampled pole → L1.

### L1 — Common Mature Structure

- Upkeep loop: inspections, preventive maintenance (usage- or calendar-triggered), work orders, defects/requests, service history accumulating on the machine, parts/consumables.
- Utilization measurement & reporting: active vs idle time, per asset/category/jobsite, configurable benchmarks/thresholds.
- Cost layer: ownership/operating cost per machine, charge-out/job costing, internal billing, rental billing; buy/rent/retire (TCO) decisions.
- Alerts & notifications: maintenance due, fault codes, geofence breach, idle thresholds, unauthorized/after-hours movement.
- Mobile field surfaces: operator/foreman check-in-out, digital inspections, hours, photos; mechanic work-order execution.
- Operator management: assignment, operator history, certifications (where surfaced).
- Integrations: ERP/accounting, project management, OEM telematics (AEMP), fuel.

### L2 — Variant / Optional Structure

- Capture mechanism: OEM-embedded telematics vs aftermarket hardware vs manual readings vs timesheet-derived.
- Hardware-software bundling (trackers, keypads, dash cams, BLE/QR tags) vs software-only.
- Safety/video telematics: dash cams, driver/operator scorecards, coaching.
- Theft-prevention machinery: geofences, after-hours movement alerts, access keypads, immobilization.
- Road-compliance machinery for the on-road slice of mixed fleets: ELD, DVIR, IFTA.
- Owned-vs-rented posture: tracking rented-in assets; renting-out with utilization-based billing (some products).
- Segment packaging: SMB light tracking vs enterprise shop management (one vendor ladders both).
- Regional/industry tuning: AU/NZ vs North America; crane, civil, paving, rail, traffic variants.
- Fuel management depth; parts procurement; inventory of consumables.

### L3 — Vendor-specific (research notes only)

- Tenna: "Asset Financials" branded module; TennaBLE/TennaQR/TennaCANbus hardware names; "Built By Contractors For Contractors" positioning; configurable utilization benchmarks framing.
- EquipmentShare: T3 Cloud-Connected Keypad; T3 Asset Insight; Link app; CostCapture; dual rental-company/contractor posture; "6.4 billion data points" claim.
- Assignar: Milo AI assistant; recommendation engine; CraneOps/TrafficOps/InfraOps industry packages; Assignar Pay.
- HCSS: Equipment360 name; "three clicks" work-order creation; sibling products (Dispatcher, Telematics, Fuel Management, HeavyJob); "50 to 2,000+ assets" targeting claim; 65%/10% ROI marketing stats.

## Rejected Findings (not promoted)

- "Equipment management = GPS tracking" — rejected: manual meter readings and timesheet-derived usage satisfy the core (E360 explicitly supports manual readings; Assignar has no telematics emphasis). Telematics is the dominant modern capture mechanism, not the definition.
- "Equipment management includes dash cams / driver coaching" — rejected: only 2 of 4 sampled products; variant.
- "Equipment management = maintenance shop system" — rejected: Assignar pole functions without surfaced upkeep; upkeep is L1.
- "Utilization has industry-standard thresholds/percentages" — rejected: Tenna explicitly frames benchmarks as customer-configurable; no cross-product numeric standard observed.
- "The managed population is only heavy iron" — rejected: sampled products consistently include trucks, trailers, attachments, tools, consumables in mixed fleets; heavy machines are the center of gravity, not the whole population.

## Historical / Market-Sample Check (per workflow §24)

Pre-telematics, pre-cloud practice: equipment ledgers (identity, cost, depreciation), dispatch boards (which machine on which job), hour-meter logbooks (manual readings), maintenance logbooks, charge-out rate cards.
- Register ✓ (ledger), operating state ✓ (manual hours + "it's on Job X"), allocation ✓ (dispatch board).
- Telematics, cloud, mobile apps, configurable dashboards NOT required.
→ L0 survives the historical check. Modern implementations (GPS trackers, PTO signals, configurable benchmarks, OEM integrations) are L1/L2.

## Boundary Findings

| Neighboring Type | Distinction | "Remove what → becomes the other" |
|---|---|---|
| Vehicle Telematics Platform (§18) | telematics = live data capture/monitoring feed; equipment management = system of record consuming feeds for allocation/upkeep/cost decisions. OEM portals (VisionLink/KOMTRAX — not directly fetched) sit on the feed side; Tenna documents "OEM Telematics & AEMP" as integrations. | Remove allocation + upkeep + cost loop, keep live monitoring → telematics platform. |
| Fleet Management System (§18) | road-vehicle/driver-centric (routes, drivers, HOS); equipment management is machine/jobsite-centric (hours, utilization, attachments). Mixed-fleet products include an on-road slice with ELD/DVIR/IFTA as variant machinery. | Population becomes road vehicles and the loop becomes driver/route/compliance → fleet management. |
| CMMS / Maintenance Management (§16) | CMMS = maintenance operations for (often stationary) plant assets; equipment management = job-allocation/utilization-centric for a mobile fleet. E360 shows the maintenance pole can look CMMS-like but stays in-Type via mobile fleet + job-cost integration. | Population becomes stationary plant and allocation-to-jobs disappears → CMMS. |
| Tool Management (§16) | small tools vs heavy machines; mixed-fleet products track small tools as an adjacent population (BLE/QR tags). | Population becomes only small tools → tool management. |
| Construction Materials Management (§17) | materials are consumed against work; machines are durable, metered, reusable assets with hours/utilization. | Records become consumed quantities rather than metered machines → materials management. |
| Construction Field Management / Daily Log (§17) | field management runs site work execution; equipment management runs the machine population serving that work. | Primary object becomes the day's site work rather than machines → field management. |
| Mining Fleet Management (§20) | mining fleet systems are production-cycle-centric (loading/hauling); construction is job-allocation-centric. | Population/loop becomes mine production cycles → mining fleet management. |
| Farm Equipment Telematics (§20) | ag-specific telematics; same feed-vs-record seam as Vehicle Telematics. | — |
| Equipment rental management (rental-company ERP class; Trackunit's rental heartland) | when the primary user is the rental company managing outbound fleet + rental contracts → rental management Type. Contractor renting-in appears here only as asset posture ("owned, rented, third-party"). | Primary user becomes the rental business and the core object becomes the rental contract → rental management. |
| Equipment Administration Platform (§10) | generic enterprise equipment administration lacks jobsite/utilization/telematics semantics. | Remove construction/jobsite semantics → generic equipment administration. |
| Construction Project Management (§17) | project management runs the project; equipment management runs the fleet serving projects; the seam is the jobsite/cost-code reference. | Primary object becomes the project/schedule rather than machines → project management. |

## Uncertainties

- Trackunit unreachable → the OEM-agnostic telematics-first vendor perspective (and its rental-fleet framing) is inferred only from adjacent evidence; no claims about it appear in the final document.
- OEM portals (VisionLink/KOMTRAX) unreachable → their exact capabilities are NOT asserted anywhere; the feed-vs-record boundary rests on Tenna's integration documentation plus the sampled products' behavior.
- Assignar's equipment-maintenance depth unverified (only homepage + scheduling page fetched); treated strictly as the scheduling-first pole.
- Utilization formulas (e.g., run-time vs available-hours ratios) vary and are customer-configurable in at least one product; no numeric standard is claimed.
- Whether "renting-out with utilization-based billing" is common or rare across the market: observed in one product (Tenna Asset Financials) + T3 billing collection → kept as variant, not common structure.

## Final Synthesis

Construction Equipment Management is the contractor-side system of record for the machine fleet. Its defining core is small: a register of identified machines the company owns or controls; a tracked operating state per machine over time (where it is, whether/how much it ran); and the allocation of machines to work over time. Around that core, mature products add the upkeep loop (inspections, usage-triggered PM, work orders, mechanic execution, parts), utilization measurement against configurable benchmarks, a cost layer tying machines to jobs (charge-out, rental billing, buy/rent/retire decisions), exception alerts, mobile field surfaces, and integrations (ERP/accounting, project management, OEM telematics feeds). Telematics is the dominant modern capture mechanism but not the definition — manual meter readings and timesheet-derived usage satisfy the core, so the Type predates and survives beyond GPS hardware. The market realizes the Type through poles (tracking-first, scheduling-first, maintenance-first, full-platform) that each emphasize one L1 loop while keeping the same L0 skeleton.
