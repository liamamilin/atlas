# Research Notes — CMMS / Maintenance Management

Research date: 2026-09-07
Slug: cmms-maintenance-management
Directory leaf: CMMS / Maintenance Management (§16 Engineering, Manufacturing & Industrial)

---

## Research Goal

Understand what a CMMS (Computerized Maintenance Management System) actually is as an Application Type: its core objects, the work order lifecycle, how planned (preventive) and unplanned (reactive) maintenance are managed, how technicians execute work, how spare parts and vendors participate, and where the Type's boundary sits against EAM, facility management, fleet, reliability, and IT service systems.

## Initial Boundary (hypothesis before research)

- Core use: manage maintenance work on physical assets/equipment — asset register, work orders, preventive maintenance schedules, maintenance history, technician execution, spare parts.
- Primary users: maintenance managers, technicians, planners, plus non-maintenance requesters.
- Nearest neighbors: Enterprise Asset Management / EAM, Enterprise Asset Registry, Reliability Management, Facility Management System / IWMS, Property Maintenance Management, Fleet Management System, Aircraft Maintenance Management, ITSM, Tool Management, Calibration Management, Field Service Management.
- Likely boundary: CMMS = maintenance work management; EAM adds the asset financial/lifecycle layer (procurement, depreciation, capital planning, disposal); Registry = assets without work management.
- Unknowns: exact work order field/status models, PM trigger mechanics, request→WO conversion rules, inventory linkage, metrics vocabulary, permission models.

## Research Questions

1. What does an asset/equipment record contain, and how are assets organized (locations, hierarchies, parent/child)?
2. What is a work order: fields, lifecycle, who creates/assigns/executes/closes it, what closure requires?
3. How is preventive maintenance defined and triggered (calendar/time, meter/runtime, conditional)? How do PM templates generate work orders?
4. How do work requests from non-maintenance people enter the system, and how are they triaged (dedupe, approval, conversion)?
5. How do technicians execute work (mobile, checklists, labor hours, parts consumption, photos, signatures)?
6. How does MRO spare-parts inventory link to work orders (reservations, thresholds, reorder, purchasing)?
7. What metrics do these systems surface (backlog, completion, PM compliance, downtime, MTTR/MTBF)?
8. What roles and permissions shape the workflow?
9. Where exactly is the CMMS/EAM seam, per vendor articulation and per structure?
10. Would older / on-premise / non-cloud products still fit the definition (historical check)?

## Representative Products

Selected for market representation + documentation quality + different philosophies + different customer tiers:

| Product | Positioning | Tier reached | Notes |
|---|---|---|---|
| Limble CMMS | SMB/mid-market cloud CMMS | Tier 1 (help center, 5 pages) | Task model = PMs, WOs, WRs explicitly |
| UpKeep | Mobile-first CMMS, SMB→enterprise, "asset operations platform" | Tier 2 (root + CMMS product page + FAQ) | Pricing tiers reveal capability layering |
| eMaint (Fluke) | Mid-market→enterprise CMMS/EAM, regulated industries | Tier 2 (root + WO management page + support center) | Strong audit/compliance + condition-monitoring evidence |
| FTMaintenance (FasTrak) | SMB/mid-market, cloud AND on-premise, perpetual license option | Tier 2 (root + PM page + WO page) | Cleanest canonical feature taxonomy; deployment variant |

Attempted but unreachable (recorded as source-access limitation):
- Fiix (Rockwell): help.fiix.io transport error ×1; fiix.com/support 404; www.fiix.io transport error → abandoned.
- IBM Maximo (enterprise EAM heritage): ibm.com/docs 403 ×2 → abandoned. Would have been the enterprise/historical anchor.
- Odoo Maintenance (open source, ERP-embedded): odoo.com/documentation 403 ×2 → abandoned.
- help.emaint.com: transport error ×1; used www.emaint.com pages instead.

## Sources

Tier 1 (official operational documentation):
- Limble CMMS Help Center: https://help.limblecmms.com/en/ (home), collections "Tasks (PMs, WOs & WRs)" (…/1736591), "Assets, Parts & Vendors" (…/9707910), "PM Schedule Options & Configuration" (…/9707940), article "Types of Tasks in Limble" (…/2982304)

Tier 2 (official product pages):
- UpKeep: https://upkeep.com/ (root + FAQ), https://upkeep.com/product/cmms-software/
- eMaint: https://www.emaint.com/ (root), https://www.emaint.com/work-order-management, https://www.emaint.com/customer-support-center
- FTMaintenance: https://ftmaintenance.com/ (root), https://ftmaintenance.com/cmms-features/preventive-maintenance/, https://ftmaintenance.com/cmms-features/work-order-management/

All fetched 2026-09-07.

---

## Product Observations

### Limble CMMS (Tier 1 — directly observed)

Evidence layer: A (official help center articles).

- **Task taxonomy is explicit**: "Types of Tasks in Limble" defines PM (Planned/Preventive Maintenance, recurring schedule), WO (Work Order — planned and unplanned), WR (Work Request), and Part Threshold Tasks. Tasks divide into "planned" (PMs, planned WOs, part-threshold tasks) vs "unplanned" (work requests, unplanned WOs).
- **PM semantics**: recurring schedule tasks; examples given: greasing a bearing monthly, replacing an air filter every 3,000 miles (i.e., both calendar and usage-based). PM templates; bulk import; "check for missing PMs on assets" (coverage audit); QR codes for PMs; **linking readings to assets** (meter readings); AI-powered PM builder. PM schedule options collection: basic, advanced, **conditional PM schedules** (incl. holiday conditions), **stack PMs**, **reschedule PM based on completion**.
- **Work request semantics**: "typically created by people who are not part of the maintenance team"; submitted via online form accessible by URL or QR code; **anyone in the company can submit, even without a Limble account**; requester can see "my work requests"; settings for review and **approval**; **duplicate avoidance** and **merging work requests**; emails to requesters (status loop).
- **WO semantics**: WO templates (incl. default template); intermittent tasks; multiple people can work a single task; task timer and logging time spent; comments; **task status configuration** (statuses are configurable); editing completed tasks is a controlled operation.
- **Instruction system**: instruction sets; basic and advanced instruction types; option list; "Assign PM", "Start Work Order", "Request Approval", "Verify Location" as instruction types inside tasks (i.e., tasks can embed procedures and even spawn other work).
- **Assets**: organizing assets; bulk import from Excel; move assets between locations; **view asset fields from a task** (task↔asset linkage); **asset depreciation schedule** (EAM-leaning capability present); **retiring assets**; asset location and asset maps; asset templates; "Asset Snap" (create asset via photo/AI); **tools** tracked in Limble.
- **Parts**: global & location-based part settings; add part to task; **associate assets and parts**; **inventory thresholds**; **reserving parts and minimum thresholds**; part logs; transfer parts between locations; **cycle counts** to audit inventory; part price field; "Smart Parts" creation.
- **Vendors**: manage vendors; **share a task with a vendor**; associate parts with vendors.
- **Other collections**: Reports & Dashboards; "Manage Work" (planning); Manage Users & Teams (permissions); Manage Locations; **Purchasing** (POs); Mobile App; Additional Features; FAQ.

### UpKeep (Tier 2 — official product pages + FAQ)

Evidence layer: A for product-page statements about UpKeep itself; vendor definitions used as corroboration only.

- Root positioning: "CMMS platform … to bring work orders, compliance and preventive maintenance together"; "a sensor reading opens a work order … and lands in the asset's history" (sensor→WO→asset history chain stated explicitly).
- CMMS product page: "A CMMS … is the system of record for every maintenance team. UpKeep's CMMS software brings work orders, preventive maintenance, asset management and parts inventory together in one mobile-first platform."
- Capabilities enumerated: Work Order Management ("create, prioritize, and track work orders in real time; automatically assign to the right technician with mobile push notifications"); Preventive Maintenance ("schedule recurring PMs by time, meter readings, or AI-recommended intervals"); Asset Management ("complete asset lifecycle tracking with maintenance history, warranties, depreciation, real-time condition monitoring"); Parts & Inventory ("track parts quantities, automate reorder points, manage purchase orders, eliminate stockouts"); Analytics & Reporting; Mobile CMMS ("works offline, syncs automatically").
- **Pricing-tier layering (strong structural evidence)**: Essential ($24) = unlimited work orders + unlimited locations + AI; Premium adds **PM scheduling**, custom checklists, parts & inventory with costing, time & labor tracking; Professional adds mobile offline mode, **external request portal**, full analytics history, **asset lifecycle tracking**, signature capture; Enterprise adds multi-site module support, workflow automation, reliability & downtime tracking, **PO management**, API, SSO & custom roles. → Work orders + assets are the entry floor; PM, parts, requests portal, lifecycle, purchasing are layered on top.
- "Unlimited free Requester seats so anyone in your organization can submit work orders" — requester/technician seat distinction is structural.
- FAQ (vendor articulation of the CMMS/EAM seam): "A CMMS centralizes maintenance data and automates day-to-day maintenance during the active part of an asset's lifecycle. An EAM includes all CMMS capabilities plus inventory management, multi-site management, accounting and purchasing. Every EAM contains a CMMS."
- FAQ defines CMMS: "software that centralizes work orders, preventive maintenance schedules, asset records, parts inventory, and technician activity."
- Fleet variant: "Schedule service by mileage or hours, track every vehicle's history" (fleet maintenance page nav).
- Platform family (L3 breadth): Safety/EHS (permits, lockout/tagout, inspections on the same work orders), Learn (LMS), Edge (IIoT sensors), Nova AI, Providers, Production, Quality, Procurement, Workforce, Projects, Facilities, Capital Planning, Field Service, Vendor Management, Contracts, Tool Tracking, Inspection Forms, Request Portal, SOP Library.

### eMaint (Fluke) (Tier 2)

Evidence layer: A for statements about eMaint itself.

- Nav taxonomy: CMMS Software; Work Order Management ("Plan, assign, track to completion"); Preventive Maintenance ("Schedule recurring work, avoid failures"); Predictive Maintenance ("Act on sensor and condition data"); Mobile App; Asset Management ("Hierarchies, history, total cost of ownership"); Analytics & Reporting ("KPIs, custom dashboards, exports"); Parts & Inventory ("Stockroom control, reorder, cycle counts"); Regulatory Compliance ("Audit trails, validation, signatures"); EAM Software; Integrations ("ERP, IIoT, SSO, open APIs"); Condition Monitoring (Fluke sensors); Multi-Site & Enterprise; Vendor Management ("Contractor access, work approvals").
- Work order management page: "Work order management is at the core of your operation … create, assign, and close work orders from any location."
- **Request intake channels**: "Anyone on your team can submit a work request through the portal, email, mobile app, or voice call." Auto-routing "based on priority, skillset, location, and workload"; escalation when work is unassigned or overdue; **duplicate flagging** "based on asset, location, and description keywords" with coordinator merge/link/confirm.
- **Approval workflows**: "configure approval workflows that require manager sign-off before work starts, especially for high-cost repairs or contractor work."
- **Closure gate**: "the system won't let technicians close work orders without proper documentation"; "everything's timestamped."
- Mobile: native app, offline ("work in dead zones, sync when connected"), **QR code scanning on equipment pulls up work orders and asset history**, photo/video documentation, digital signatures.
- Audit trail: "Full audit trail with timestamps, user tracking, and change history"; dashboards "open/overdue work, backlog, and completion metrics"; "hour and cost tracking tied to work orders"; compliance-ready reports (life sciences: GxP, 21 CFR Part 11, validation).
- Condition monitoring chain: "Fluke sensors gather vibration, temperature, and ultrasound data … The moment a threshold is crossed, the CMMS triggers a prioritized work order. The technician receives it on their device — with asset history, linked manuals, and spare-parts availability already attached."
- Vendor claims (kept out of canonical doc): "60 seconds to create and assign work", "100% audit trail compliance", customer "97% on-time PM completion".

### FTMaintenance (FasTrak SoftWorks) (Tier 2)

Evidence layer: A for statements about FTMaintenance itself.

- Feature taxonomy (cleanest canonical set): Work Order Management; Asset Management ("service history, relationships to other assets, assigned work orders"); Inventory Management ("tracking MRO inventory and spare parts, vendors, and purchasing"); Preventive Maintenance; Maintenance Reports; Maintenance Requests ("online application … manage incoming requests, document history, and communicate with internal and external customers"); Mobile Accessibility.
- **PM page (trigger mechanics, directly stated)**: "Schedule preventive maintenance using time-based or meter-based intervals"; "Create a unique preventive maintenance schedule for each asset"; "Eliminate redundant data entry with multi-asset work orders"; PM work order templates; PM checklists ("master list of tasks … step-by-step instructions … time estimates per task … track the time and costs"); PM calendar ("view all scheduled preventive maintenance work orders at a glance, with the flexibility to reschedule or reassign").
- **WO page (lifecycle, directly stated)**: "Track work orders through the entire process, from initial request to completion and history." Creation: "Create work orders directly from work requests"; "Assign multiple assets to a single work order"; "Generate work orders for on-demand or scheduled maintenance activities"; procedures/instructions; attachments. Tracking: "Easily view work order status"; "Search for work orders by asset, priority, and due date"; "Plan work in advance to ensure parts and materials are on hand when needed"; "Schedule maintenance when assets and labor are available"; **"Trigger maintenance based on calendar date or runtime"**; reports for overdue/incomplete work. History: "Close work orders in seconds"; "Automatically create a comprehensive, historical maintenance record"; "Document what work was done, how long it took, and who did it"; **"Reopen work orders to make corrections or add more detail"**; **"Set field requirements for closing work orders to capture all desired information"** (closure gate). Mobile: full WO list, update, create WOs and service requests from mobile, access history in the field.
- **Deployment variant**: On-Premise Deployment and Cloud Deployment both offered; pricing includes a **perpetual license** (one-time purchase) alongside SaaS tiers (LITE = "work order-focused", LITE+ = "standard CMMS", FULL SCALE).
- Roles: Executives / Maintenance Managers / Maintenance Technicians.
- Industries: manufacturing, facilities, food & beverage, power/energy, construction, mining, government, education, oil & gas, fleet, healthcare, hospitality, property management, public works, wastewater, pharmaceuticals.

---

## Cross-product Comparison

| Structure | Limble | UpKeep | eMaint | FTMaintenance | Verdict |
|---|---|---|---|---|---|
| Asset/equipment register with fields, locations, import | ✔ (assets, locations, maps, templates, retire) | ✔ (asset management, lifecycle) | ✔ ("hierarchies, history, TCO") | ✔ (asset mgmt, relationships) | Universal → Core |
| Work order bound to asset, with lifecycle | ✔ (WO task type, statuses) | ✔ (WOM capability) | ✔ ("create, assign, close") | ✔ ("request → completion → history") | Universal → Core |
| Persistent maintenance history on asset | ✔ (asset fields viewable from task; history implied by task-asset link) | ✔ ("lands in the asset's history") | ✔ ("hierarchies, history") | ✔ ("automatically create a comprehensive, historical maintenance record") | Universal → Core |
| PM scheduling engine (time/calendar-based) | ✔ (PM templates, schedules) | ✔ (Premium tier) | ✔ ("schedule recurring work") | ✔ (time-based intervals) | Universal → Common (not definitional: UpKeep gates it at Premium; FTMaintenance LITE is WO-only) |
| PM meter/runtime-based triggers | ✔ (readings linked to assets; 3,000-mile example) | ✔ ("by time, meter readings") | (via condition monitoring) | ✔ (meter-based intervals; "calendar date or runtime") | Common |
| Work request intake from non-maintenance staff | ✔ (WR portal, URL/QR, no account needed) | ✔ (unlimited requester seats; external portal at Professional) | ✔ (portal, email, mobile, voice) | ✔ (maintenance requests app) | Common (not definitional: FTMaintenance LITE is WO-focused) |
| Request triage: dedupe/merge, approval, conversion to WO | ✔ (merge, review/approval) | (portal) | ✔ (duplicate flagging, approval workflows) | ✔ (create WO from request) | Common |
| Task/procedure templates & checklists | ✔ (instruction sets, WO templates) | ✔ (custom checklists, Premium) | ✔ (procedures) | ✔ (PM checklists, master task lists) | Common |
| MRO parts inventory linked to WOs/assets | ✔ (thresholds, reservations, logs, cycle counts) | ✔ (reorder points, costing) | ✔ (stockroom, reorder, cycle counts) | ✔ (MRO inventory, spare parts) | Common |
| Vendors/contractors | ✔ (share task with vendor) | (vendor mgmt product) | ✔ (vendor portal, contractor approvals) | ✔ (vendors in inventory) | Common |
| Labor & cost tracking on WOs | ✔ (task timer, time logging) | ✔ (time & labor tracking, Premium) | ✔ (hour and cost tracking) | ✔ (time/costs per PM task) | Common |
| Metrics/dashboards (backlog, completion, overdue) | ✔ (reports & dashboards) | ✔ (analytics & reporting) | ✔ (backlog, completion metrics) | ✔ (maintenance reports, overdue/incomplete) | Common |
| Mobile technician app (offline, QR, photos) | ✔ (mobile app collection) | ✔ (mobile-first, offline) | ✔ (native, offline, QR, signatures) | ✔ (mobile accessibility) | Common (historical desktop CMMS lacked it) |
| Multi-location / multi-site | ✔ (locations, transfers) | ✔ (unlimited locations; multi-site at Enterprise) | ✔ (multi-site & enterprise) | ✔ (multi-location inventory) | Common |
| Audit trail / timestamps | (task comments/history) | (audit trails at Enterprise) | ✔ (full audit trail, compliance) | (field requirements, records) | Common; compliance-grade depth is variant |
| Roles/permissions | ✔ (users & teams) | ✔ (SSO & custom roles, Enterprise) | ✔ (roles, governance) | ✔ (role-based solutions) | Common |
| Sensor/condition-based (predictive) triggers | (readings) | ✔ (Edge sensors; AI-recommended intervals) | ✔ (Fluke sensors → prioritized WO) | — | Optional/variant |
| Purchasing/POs | ✔ (purchasing collection) | ✔ (PO management, Enterprise) | (integrations) | ✔ (purchasing in inventory) | Optional/variant |
| Asset depreciation / lifecycle financials | ✔ (depreciation schedule) | ✔ (asset lifecycle tracking, Professional) | ✔ (TCO; EAM product) | — | Optional/variant (EAM-leaning) |
| On-premise / perpetual license | — | — (cloud-only per FAQ) | — (SaaS) | ✔ (on-premise + perpetual) | Variant |
| Regulated-industry compliance (GxP, Part 11, signatures) | — | (signature capture, Professional) | ✔ (life sciences) | (pharma industry page) | Variant |
| AI assistance | ✔ (AI PM builder, Asset Snap, Smart Parts) | ✔ (Nova) | ✔ (eMaint AI) | — | Era-common variant |

## Canonical Abstraction

### L0 — Defining Invariant (smallest stable structure)

```text
Maintainable Asset Register          (the physical things maintenance is performed on)
└── Work Order bound to an Asset     (a managed maintenance work item with a lifecycle:
                                      created → assigned → executed → closed with a record)
    └── Persistent Maintenance History (closed work orders accumulate on the asset as a
                                      queryable record of what was done, by whom, how long)
```

Three properties. Tests:
- Remove the asset register → generic task/ticketing system, not a CMMS.
- Remove the work order lifecycle → an asset registry (a different directory Type), not maintenance management.
- Remove persistent history → a dispatch/communication tool; the "management system of record" quality disappears.

Deliberately NOT in L0 (each fails the "remove it and it's still a CMMS" test):
- **PM scheduling** — UpKeep sells CMMS (Essential) without PM scheduling; FTMaintenance's LITE tier is explicitly "work order-focused"; reactive-only shops run CMMSs. PM is the most market-defining *capability* but not a definitional *structure*.
- **Work request portal** — same tier evidence; requests can be optional.
- **Parts inventory** — minimal CMMSs exist without it.
- **Mobile app** — desktop-era CMMSs had none.
- **Cloud delivery** — FTMaintenance ships on-premise with perpetual license.

### L1 — Common Mature Structure

- PM scheduling engine: recurring schedules per asset, time/calendar intervals and meter/runtime intervals, PM templates that auto-generate work orders, PM calendar/planner views, rescheduling (including reschedule-from-completion).
- Work request intake: forms/portals (URL/QR/email/voice), requesters without licenses, triage (duplicate detection/merge), optional review/approval, conversion into work orders, status feedback to requesters.
- Task templates, procedures, checklists with step instructions and time estimates.
- MRO spare-parts inventory: stock levels per location, reservations/allocations to work, minimum thresholds/reorder points, part logs, cycle counts, parts associated with assets and tasks.
- Vendor/contractor records; sharing work with vendors; contractor approvals.
- Labor and cost tracking on work orders (time logging, hourly rates, parts cost → work order cost).
- Planning surfaces: backlog views, calendars, technician workload, priority and due-date search.
- Metrics & dashboards: work order completion, overdue work, backlog, PM compliance, asset downtime; KPI vocabulary (MTTR/MTBF) marketed by vendors.
- Mobile technician app: work queue, offline capture, QR/barcode asset lookup, photos, signatures.
- Multi-location support; asset location hierarchies/maps.
- Audit trail: timestamps, user attribution, change history.
- Roles: administrator, maintenance manager, technician, requester (license-free).

### L2 — Variant / Optional Structure

- Condition-based/predictive triggers: sensor/IIoT integrations, threshold-crossing auto-work-orders, AI-recommended PM intervals.
- Approval workflows (manager sign-off for high-cost or contractor work).
- Purchasing/PO management tied to inventory.
- Asset financial/lifecycle depth: depreciation, warranties, total cost of ownership, capital planning (EAM-leaning).
- Regulated-industry compliance depth: GxP/21 CFR Part 11, validation, e-signatures.
- Deployment: cloud SaaS vs on-premise; subscription vs perpetual license.
- Failure/cause/downtime coding and reliability analytics.
- Multi-asset work orders; asset BOMs.
- Industry tuning: fleet (mileage/hours service), facilities, food & beverage sanitation, healthcare/biomedical, government/public works.
- External-customer request portals (property/facility contexts).
- AI assistance (era-common).

### L3 — Vendor-specific (research notes only)

- Limble: Part Threshold Tasks as a task type; conditional PM schedules with holiday logic; stack PMs; reschedule-PM-on-completion; instruction types ("Assign PM", "Start Work Order", "Verify Location"); AI PM Builder; Asset Snap; Smart Parts; "80% planned" best-practice claim; task status configuration.
- UpKeep: Nova AI + Nova credits; Studio no-code apps; Learn (LMS); Safety/EHS product; Edge sensors; Providers; "asset operations management" positioning; unlimited-requester-seat pricing framing; Forrester ROI claims.
- eMaint: X4/X5 product versions; Fluke condition-monitoring pairing ("only-in-market combo" claim); voice-call request intake; auto-routing by skillset/workload; "60 seconds to create and assign" claim; eMaint University; customer claims (97% PM completion, 90% reactive-work reduction).
- FTMaintenance: LITE/LITE+/FULL SCALE/one-time-purchase tiers; PM calendar color-coding; runtime-cycle trigger phrasing.

## Rejected Findings

- **"PM scheduling is definitional"** — rejected. UpKeep's entry tier is a CMMS without PM scheduling; FTMaintenance LITE is work-order-focused. PM is the most common headline capability, not the defining structure.
- **"A work request portal is definitional"** — rejected on the same tier evidence; also historical CMMSs ran without request portals.
- **"Parts inventory is definitional"** — rejected; minimal/reactive deployments exist without inventory modules.
- **"CMMS = cloud/mobile software"** — rejected; FTMaintenance ships on-premise with a perpetual license; desktop-era CMMSs had no mobile.
- **"CMMS includes EAM financials (depreciation, capital planning)"** — rejected as definitional; present in several products (Limble depreciation, UpKeep Professional lifecycle tracking, eMaint EAM) but as an extension layer, and UpKeep's own FAQ frames EAM as the superset.
- **"Work orders are IT tickets"** — rejected; the binding to physical maintainable assets and maintenance semantics (repair/inspect/lubricate, PM recurrence, parts) is what distinguishes the Type.

## Boundary Findings

- **vs Enterprise Asset Management / EAM**: the strongest overlap. Both vendors articulate the seam the same way: EAM = all CMMS capabilities + asset financial/lifecycle governance (procurement, accounting, capital planning, depreciation, multi-site governance, end-of-life). UpKeep FAQ: "Every EAM contains a CMMS." eMaint sells both under one platform. Canonical discriminator: if the system carries the full asset financial/lifecycle layer as a first-class structure, it is EAM; if it centers on maintenance work management, it is CMMS. In the market the two are converging (CMMS vendors add lifecycle features; EAM vendors embed CMMS cores), so the boundary is a gradient, not a wall. Recorded as a taxonomy observation, not silently resolved.
- **vs Enterprise Asset Registry**: registry = asset records without work management. The "remove the work order" test separates them cleanly.
- **vs Reliability Management**: reliability engineering (RCM/FMEA, failure analysis, condition-monitoring programs, strategy optimization) consumes CMMS data; CMMS may add predictive triggers (L2) but deep reliability strategy is its own Type.
- **vs Facility Management System / IWMS**: FM/IWMS centers on buildings, space, leases, occupancy, and service contracting; building maintenance inside FM is typically served by a CMMS(-like) module. The CMMS core (assets/WO/PM/parts) is what the CMMS Type owns.
- **vs Property Maintenance Management**: tenant/lease/unit orientation with rent-side workflows; request intake overlaps, but the organizing spine differs (tenancy vs maintenance operations).
- **vs Fleet Management System**: vehicles/telematics/routing/compliance spine; CMMS principles apply to vehicle service (UpKeep Fleet, FTMaintenance fleet industry page) but telematics-driven fleet operations are a distinct Type.
- **vs Aircraft Maintenance Management**: airworthiness/regulatory MRO with its own compliance spine; a domain-specific cousin of maintenance management.
- **vs ITSM / Incident Management**: IT services and incidents vs physical maintenance; asset registers overlap conceptually (CMDB), but work semantics, PM recurrence, and parts consumption differ.
- **vs Tool Management / Calibration Management**: narrow specializations that commonly ride inside a CMMS (Limble documents tools; calibration is a sibling directory leaf).
- **vs Field Service Management / Aftermarket Service Management**: dispatching technicians to external customers vs maintaining the organization's own operations. Some CMMSs serve external requesters (FTMaintenance "internal and external customers"), which is a variant posture, not the core.

## Historical / Market-Sample Check

- Desktop-era and on-premise CMMSs (Maximo heritage since the 1980s, MP2 in the 1990s, FTMaintenance's perpetual-license on-premise edition today) all center on assets + work orders + PM schedules + history. They lack mobile, QR, AI, and IIoT — all of which sit in L1/L2 here. The L0 holds.
- The L0 does not depend on cloud delivery, phone-based identity, or any modern UI pattern. Regional/open-source CMMSs (not directly reachable in this pass) are structurally described by the same trio in secondary literature; treated as inference, not direct evidence.
- Conclusion: the definition is not over-fitted to the current mobile/cloud market.

## Uncertainties

- Exact work order status vocabularies (e.g., specific status names and allowed transitions) were not verified at Tier 1 for any product except Limble's "task status configuration" (statuses are configurable; exact defaults unknown). The final document therefore describes conceptual states, not vendor status names.
- Whether every product enforces closure gates (required fields at close) was directly observed only at eMaint and FTMaintenance; generalized with moderate wording.
- MTTR/MTBF as in-product metrics: vendors market these KPIs, but no Tier 1 page in this pass enumerated them as built-in reports; kept as vendor-marketed vocabulary.
- Fiix, IBM Maximo, and Odoo could not be reached; the enterprise/EAM-heritage pole and the open-source pole are therefore evidenced indirectly (eMaint's enterprise positioning; UpKeep/eMaint EAM pages) rather than by direct observation.
- Requester "license-free" status: directly observed at UpKeep ("unlimited free Requester seats") and Limble ("even if they do not have a Limble account"); generalized with moderate wording.

## Final Synthesis

A CMMS is maintenance operations software whose defining structure is small: a register of maintainable physical assets, work orders bound to those assets and carried through a managed lifecycle, and the persistent maintenance history that closed work orders leave on each asset. Around that core, mature products add the same recognizable layer: preventive maintenance scheduling (calendar and meter/runtime triggers generating work orders), request intake from non-maintenance staff, task templates and checklists, MRO spare-parts inventory linked to work, vendor/contractor handling, labor and cost tracking, planning surfaces (backlog, calendars, workload), metrics and dashboards, mobile technician apps, multi-location support, audit trails, and role-based permissions. Variants extend the Type toward condition-based/predictive triggers, purchasing, asset financial lifecycle (the EAM seam), regulated-industry compliance, on-premise deployment, and industry tuning (fleet, facilities, food & beverage, healthcare). The CMMS/EAM boundary is a gradient acknowledged by vendors themselves; the canonical discriminator is whether the asset's full financial/lifecycle governance is a first-class structure or an extension.
