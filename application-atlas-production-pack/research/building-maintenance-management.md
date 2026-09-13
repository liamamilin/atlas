# Research Notes — Building Maintenance Management

Directory location: §17 Construction, Real Estate & Facilities (between "Building Condition Assessment" and "Building Management System / BMS")

## Research Goal

Understand what "Building Maintenance Management" software actually is as an Application Type: what objects exist inside it, who uses it, how maintenance work flows, which structures are defining (L0), which are common mature structure (L1), which are variant/optional (L2), and which are vendor-specific (L3). Resolve the dense seam neighborhood: CMMS (§16), Facility Management System (§17), Property Maintenance Management (§17), Building Asset Management (§17), BMS (§17), Building Condition Assessment (§17), IWMS (§17 sibling, unprocessed), trade field service.

## Joint-review obligations inherited from prior passes

This leaf carries four pre-hung flags recorded in STATUS.md by processed sibling passes. All are discharged in Boundary Findings below:

1. **facility-management-system (§17, processed 2026-09-08)** — "JOINT REVIEW RECOMMENDED with cmms-maintenance-management (§16, processed) and building-maintenance-management (§17, unprocessed) … expected maintenance-slice sibling — flag for that pass to draw the maintenance-slice-vs-full-facility-operations seam."
2. **property-maintenance-management (§17, processed 2026-09-09)** — "working seam recorded: building maintenance centers a building's physical plant/systems (building-scoped, asset-leaning) vs property maintenance centers portfolio-wide upkeep across tenancies and resident relationships; removal test: strip the tenancy/resident/vendor context → building maintenance; joint review recommended when that leaf is processed."
3. **building-management-system-bms (§17, processed)** — "shares the fault→action seam (BMS flags off-normal behavior, the maintenance system owns the work order) — joint review when that sibling is processed."
4. **building-asset-management (§17, processed)** and **building-condition-assessment (§17, processed)** — seams recorded from their sides (center-of-gravity; assessment-vs-execution), to be confirmed here.

## Initial Boundary

- Hypothesis: Building Maintenance Management = the maintenance-operations system of record for a building operator's physical plant — the CMMS-shaped care loop (work orders + preventive maintenance + history) bound to the building's equipment/systems and organized by the building/location structure.
- Neighbors expected: CMMS (domain-generic machinery), FMS (whole facility-operations service span), property maintenance (tenancy/resident spine), building asset management (asset-lifecycle center of gravity), BMS (control loop), building condition assessment (assessment events), IWMS (suite packaging), trade FSM (contractor's own business).
- Key taxonomy question: is this leaf a distinct Type, or the buildings-scoped variant of CMMS / the maintenance slice of FMS? The directory keeps CMMS (§16) and this leaf (§17) as separate nodes; the FMS pass already acknowledged the gradient ("1+2 without 3 = a buildings-scoped maintenance tool").

## Research Questions

1. What are the core objects? (buildings/locations, plant/equipment, work orders, PM schedules, requests, technicians, contractors, parts, inspections, costs)
2. What is the center of gravity: the work order, the asset, or the building?
3. How does the building/location structure enter the model (site → building → floor/room; equipment under buildings)?
4. What building-specific semantics exist (building systems vocabulary, life-safety/compliance obligations, occupant request intake, contractor coordination)?
5. Who uses it (maintenance techs, building engineers, facility/maintenance managers, chief engineers)?
6. What are the main workflows (reactive repair, PM program, inspections, contractor work, emergency)?
7. What separates this Type from a generic CMMS, from FMS, from property maintenance, from building asset management, from BMS?
8. Is there a distinct "building maintenance" market segment with its own vocabulary and products?

## Representative Products

| Product | Pole | Segment / customers |
|---|---|---|
| UpKeep | mobile-first CMMS marketed to facility/building maintenance; self-serve SMB | facilities teams, property/storage operators, multi-site brands, non-profits |
| Fiix (Rockwell Automation) | enterprise CMMS with facilities as a first-class hierarchy element | mid-market to enterprise, multi-site, manufacturing + facilities |
| Accruent Maintenance Connection | enterprise CMMS/EAM inside a real-estate/facilities suite family | enterprise, multi-industry (healthcare, retail, education, pharma), SaaS or on-prem |
| Eptura Asset (Hippo CMMS lineage) | building-maintenance-marketed product now inside a workplace/facility platform | mid-market to enterprise, facility/asset teams, multi-site |

Boundary anchors (no full pass needed): processed sibling passes for CMMS, FMS, property maintenance, building asset management, BMS, building condition assessment.

## Sources

- UpKeep — https://upkeep.com/ (root/product structure); https://upkeep.com/solutions/facility-management/ (facilities solution page incl. vendor FAQ); https://upkeep.com/industries/building-maintenance-software/ (building industry page); https://help.onupkeep.com/ (help center home); Work Orders collection (http://help.onupkeep.com/en/collections/3653439-upkeep-work-orders); Locations collection (http://help.onupkeep.com/en/collections/3653443-upkeep-locations)
- Fiix — https://fiixsoftware.com/cmms/features/ (features page); https://helpdesk.fiixsoftware.com/hc/en-us (help center home); Maintenance category (work orders v5/v6, calendar, task groups, scheduled maintenance, work request portal, operator portal, maintenance settings); Assets category (asset hierarchy, facilities, meters, QR codes); "Set up buildings and facilities" article; "About the asset hierarchy" article. Note: the fiix.com domain currently serves unrelated lead-gen content; the official product domain is fiixsoftware.com (Rockwell Automation).
- Accruent — https://www.accruent.com/products/maintenance-connection (product page; /products/maintenance-connection-cmms 404 — URL guess, not a domain failure); https://help.accruent.com/mc/Content/MCUserGuide/get_started/mc_overview.htm (Tier-1 overview)
- Eptura — https://eptura.com/hippocmms/ (Hippo CMMS lineage page); https://eptura.com/our-platform/eptura-asset/ (product page with FAQ)
- Processed sibling passes (STATUS.md + research files): cmms-maintenance-management, facility-management-system, property-maintenance-management, building-asset-management, building-management-system-bms, building-condition-assessment

Research date: 2026-09-10

## Product A — UpKeep

### Key observations

- Self-label: "CMMS & AI Maintenance Management Software"; platform = CMMS + Safety + Learn + Nova AI + Edge sensors + Fleet + Providers. Facilities is one industry solution among many (manufacturing, facility management, healthcare, property management, hospitality, schools, government, churches, restaurants, fitness…). (A)
- Facilities solution page framing: "One queue for every building request. Work requests, preventive maintenance, and building systems across every property you look after, with anyone able to report a problem from a phone." Tags: "Free request submission", "Multi-building by default", "Works on a phone". (A)
- Vendor FAQ definition of the facility-maintenance slice: "It is the system a facilities team uses to take in requests, schedule preventive maintenance on building systems, and keep the record of what was done to each asset. The defining requirement is intake: most facilities work starts with someone who is not on the maintenance team reporting a problem…" (A)
- Vendor-articulated CMMS vs IWMS layering: "A CMMS maintains the equipment and the building. An IWMS takes a wider view of the real estate itself, leases, space planning, occupancy, and portfolio strategy. UpKeep covers the maintenance side in full and handles space and occupancy through Facilities." (A)
- Request intake: "Anyone can submit a request from a phone or by scanning a QR code, with no account and no paid seat. The building, room, and asset come attached, so the request does not need chasing." Requesters are free; pricing is per user (people creating/closing work orders), not per building or square foot. (A)
- Building-systems PM: "PMs on HVAC, boilers, and life safety are scheduled work with a visible overdue list"; PM triggers "on dates, meter readings, or hours run". Air-handler workflow: PM triggers on runtime hours → filters/belts pulled against the work order → "the service history stays on the asset for the next condition assessment". (A)
- Contractor workflow: "The work order is assigned to the contractor rather than emailed to them. Required certificates and safety sign-offs are checked before the work starts. What they did lands on the asset record, so the building history has no gap." Providers product = "Outside contractors working in the same system, with their work visible alongside your own." (A)
- Cost accountability: "Cost and repeat failures roll up by building and by asset from the work your team already closed." (A)
- Multi-building: "Assets are organized by location, so cost, open work, and PM compliance can be viewed for one building or across the whole portfolio, using one naming scheme." Implementation framing: "Most teams start with one building: import the asset list, set PMs on the systems that cause the most disruption, and open request intake to occupants. Additional buildings reuse the same templates." (A)
- Help center (Tier-1): collections for Locations (locations & sub-locations, interactive floor plans, import), Assets, Work Orders (create/process, photos, tasks/checklists, time recording, labor cost calc, signature capture, closeout notes, duplicate, link WOs, templates, custom statuses, custom fields, categories, import/export history), Requests, Preventive Maintenance, Parts & Inventory, Meters, Purchase Orders, Scheduler, Providers & Network, Analytics, Safety, Edge, Fleet, Learn, Integrations, Customers. (A)
- Work-order invoicing exists ("create an invoice … by billing your customer for a work order") — the external-customer/provider pole. (A)
- Building industry page: "stay on top of preventive building maintenance and inspections, all in one mobile destination"; asset downtime/lifetime/ROI claims (vendor marketing figures — recorded, not generalized). (A)

## Product B — Fiix (Rockwell Automation)

### Key observations

- Self-label: "Fiix's features are built for modern maintenance"; "industry-leading CMMS"; cloud-based, AI-powered CMMS; "Whether you're managing one or one hundred facilities, Fiix keeps all your asset information in one place." (A)
- Asset hierarchy (Tier-1, "About the asset hierarchy"): locations and assets arranged by category into a hierarchy "that shows where they're located and how they're related… assets live under locations… The goal of the asset hierarchy is to match the way your assets are laid out in real life." Categories: Regions → Sites → **Facilities** → Equipment / Tools / Parts. "Facilities are the buildings or rooms that your assets live in." Equipment can nest under equipment. Multi-site setups for Professional/Enterprise tiers. (A)
- Buildings setup (Tier-1, "Set up buildings and facilities"): the location/facility is created as an asset ("Select Locations or Facilities… As a new location, and enter the address information. This action will create this asset as a top-level facility"), with files (photos, PDF manuals) and associated personnel receiving email notifications relating to the asset. (A)
- Work orders (Tier-1, v5/v6 sections): create, edit, assign, cost information, miscellaneous costs; task groups; inspection tasks within work orders (add/complete); work-order filters; calendar (view/reschedule/reassign work orders, assigned hours). (A)
- Scheduled maintenance (Tier-1): triggers section (date/time, meter readings, event and alarm-based triggers per features page), nested PMs, multi-asset scheduled maintenance, examples. (A)
- Work request portal (Tier-1): "About the work request portal", guest permissions configuration (v5/v6 user management), list-view configuration, sign-in requirements — non-licensed requesters submit work requests. (A)
- Operator portal (Tier-1): operators search/view assets, view and change work-order status, complete tasks — a restricted execution surface for non-maintenance staff. (A)
- Maintenance settings (Tier-1): work-order completion controls, failure codes + failure hierarchy, custom priorities, custom maintenance types. Metrics: MTBF, MTTR. Work-order insights dashboards (active/closed, risk scores). (A)
- Mobile app: technicians access work orders, update tasks, view instructions "from anywhere—even when they're offline"; QR code scan to asset information. (A)
- MAX (Fiix Maintenance Assistant Experience): AI assistant chat over CMMS data. (A)
- Industries: oil & gas, heavy equipment, food & beverage, manufacturing — facilities is not a headline industry page on the current site, but the facilities hierarchy and request portal are first-class product structures. (A)

## Product C — Accruent Maintenance Connection

### Key observations

- Self-label (Tier-1 overview): "Maintenance Connection (MC) is a computerized maintenance management system (CMMS) that helps you to manage work orders, organize and execute preventive maintenance, predict asset maintenance, and manage enterprise assets and equipment inventory." (A)
- Application suite (Tier-1): MRO Work Center (main application for administrators/managers/supervisors — "the most functionality for managing the lifecycle of each asset"); Technician Work Center (technicians view assigned work, create work orders); Reporter (view/create/edit/run reports); Service Requester ("Submit work requests, view the status of requests, and provide feedback"). (A)
- Additional apps (Tier-1): MC Compliance (ISO 27001 / FDA 21 CFR Part 11 — electronic signatures, audit trails, procedure versioning); MC Express (web-based mobile technician app); MC Kinetic (native mobile app — offline mode, geolocation mapping, full technician functionality). (A)
- Product page (Tier-2): "purpose-built, multi-site CMMS and EAM solution"; work order management, mobile-friendly CMMS (offline, barcode & QR scanning), actionable reporting/analytics (work-order completion rates, labor costs), inventory; "Simplify facility management, streamline asset tracking"; SaaS or on-premises ("on-premises model is useful for companies that demand local data control and must meet specific regulatory requirements"). (A)
- Vendor-articulated category layering (Tier-2 FAQ): CMMS (maintenance tasks/schedules) vs EAM (asset lifecycle) vs ERP vs APM vs "FM (Facility Management Software): Designed to manage building systems and facilities" vs IoT-enabled maintenance. (A)
- Suite context: integrates ERP (SAP, Oracle, Microsoft Dynamics…), EDMS (Accruent RedEye/Meridian), energy/IoT remote monitoring (Accruent Observe); Accruent positions MC inside "facility asset management" solutions alongside FAMIS 360 (public sector, CRE, education). (A)
- Industries (Tier-1): manufacturing, pharmaceutical/life sciences, food & beverage, health care, retail, education "and more". (A)

## Product D — Eptura Asset (Hippo CMMS lineage)

### Key observations

- Lineage: "HippoCMMS.com is now Eptura.com… Hippo, the simple maintenance solution to manage work orders, schedule and track preventive maintenance, and control inventory… Hippo CMMS is evolving into Eptura Asset." (A) — Hippo was historically a "building maintenance software" marketing pole; the product now sits inside the Eptura workplace/facility platform.
- Self-label: "Facility maintenance and asset management"; "Move from reactive maintenance to predictable operations with the simplicity of EAM built to scale." FAQ: "Eptura Asset is EAM built to scale. It combines CMMS simplicity with enterprise lifecycle management, inventory, purchasing, and condition monitoring, plus governance and multi-site support without the overhead of traditional EAM suites." (A)
- Capabilities (Tier-2): smart work orders + preventive schedules ("keep maintenance predictable at scale"); asset lifecycle ("Track assets from commissioning through retirement with complete history and lifecycle cost visibility"); mobile technician app with offline access; standardized inspections + automated records ("simplify compliance and reviews"); inventory, purchasing, kitting; dashboards/reporting across sites. (A)
- Platform context: one of four platform apps (Asset / Engage / Workplace / Visitor) plus Archibus (FedRAMP IWMS) and Serraview; "Eptura Asset connects asset and maintenance data across the Eptura Platform so teams manage assets, spaces, and people together." Integrations: Autodesk Tandem/Revit/AutoCAD (BIM/digital twin → maintenance workflows), ERP finance sync, sensors/condition data, fleet telematics. (A)
- Hosting: cloud SaaS on Microsoft Azure. (A)
- AI: Eptura Assistant for Maintenance (conversational AI in Microsoft Copilot over live work orders/asset history/schedules); Technician Copilot (voice-enabled work capture); ML early-risk detection (fleet/telematics). (A)

## Cross-product Comparison

| Dimension | UpKeep | Fiix | Accruent MC | Eptura Asset | Strength |
|---|---|---|---|---|---|
| Building/location structure (site→building→floor/room; equipment under buildings) | Locations & sub-locations; floor plans; "multi-building by default"; assets organized by location | Regions→Sites→Facilities→Equipment/Tools/Parts; "Facilities are the buildings or rooms that your assets live in"; facility created as top-level asset | multi-site CMMS; asset lifecycle per organization | multi-site support; assets across facilities | **L0** (all four) |
| Maintained objects = building plant/equipment with histories | assets with PM on HVAC/boilers/life safety; history stays on asset | equipment receive maintenance; asset events; downtime tracker | manage work orders + PM + enterprise assets | assets from commissioning through retirement | **L0** (all four) |
| Work orders through a managed lifecycle | create/process, tasks/checklists, time, cost, closeout notes, custom statuses | create/assign/costs, task groups, inspection tasks, completion controls | MRO + Technician work centers; work-order management | smart work orders | **L0** (all four) |
| Preventive maintenance scheduling | PM triggers on dates/meters/hours; overdue list | scheduled maintenance: date/meter/event-alarm triggers; nested & multi-asset PMs | organize and execute preventive maintenance | preventive schedules | **L1** (all four; cmms pass showed entry tiers can ship without) |
| Request intake from non-maintenance people | free request submission, QR/phone, no paid seat; building/room/asset attached | work request portal with guest permissions & sign-in requirements | Service Requester app (submit, view status, feedback) | (occupant portal in platform siblings) | **L1** (3/4 direct; dominant pattern) |
| Mobile technician execution | mobile-first; offline mode; photos; signature capture | mobile app offline; QR scan | MC Express / MC Kinetic (offline, geolocation) | mobile app offline | **L1** (all four) |
| Parts/inventory against work | parts pulled against WO; reorder points | parts & supplies; stock records; purchasing | equipment inventory; inventory management | inventory, purchasing, kitting | **L1** (all four) |
| Contractors/vendors in the same system | Providers; certificates checked; work lands on asset record | assign work orders (users/groups); vendors | vendors/contractors (cmms-substrate standard) | (platform-level) | **L1** |
| Cost tracking & roll-up | cost per WO; roll-up by building and by asset | cost info + misc costs per WO; asset costs | labor costs; completion rates | lifecycle cost visibility | **L1** (all four) |
| Inspections | building maintenance & inspections; safety inspections | inspection tasks in WOs | compliance apps (regulated industries) | standardized inspections, audit-ready records | **L1** |
| Metrics/dashboards | analytics; PM compliance by building | dashboards; MTBF/MTTR; work-order insights | Reporter; completion/labor dashboards | dashboards across sites | **L1** (all four) |
| Space/occupancy modules | Facilities product (space, occupancy, building systems) | — (not in sampled surface) | FAMIS 360 sibling | Eptura Workplace sibling | **L2** (suite drift toward FMS/IWMS) |
| Capital planning / condition feed-out | Capital Planning product; history "for the next condition assessment" | — | — | lifecycle cost, repair-vs-replace decisions | **L2** (drift toward building-asset-management) |
| Compliance programs (regulated) | Safety product (OSHA recordkeeping) | failure codes/hierarchy | MC Compliance (ISO 27001, FDA 21 CFR Part 11) | audit-ready inspections | **L2** (industry/regime-dependent) |
| BMS/IoT/sensor integration | Edge sensors → auto work orders | event/alarm-based PM triggers; FactoryTalk Optix | Accruent Observe integration | sensors/condition data; telematics | **L2** (the BMS seam) |
| AI assistants | Nova (builds apps, voice WOs) | MAX; work-order insights risk scores | (predict asset maintenance) | Assistant for Maintenance; Technician Copilot | **L2** (era-current) |
| Deployment | cloud SaaS, per-user pricing, free requesters | cloud SaaS; free tier; multi-site on higher tiers | SaaS or on-premises | Azure SaaS | **L2** |
| External-customer billing | invoice per work order | — | — | — | **L2** (provider pole) |

Reading: the three L0 rows hold across all four poles with radically different packaging (mobile-first self-serve / enterprise CMMS / suite-embedded enterprise EAM / platform app). Everything else varies by pole and tier.

## Canonical Model

### L0 — Defining Invariant

The building operator's maintenance-operations system of record for its physical plant. Three jointly-held structures over one binding:

1. **The building plant register.** The building's physical plant — its equipment and systems (HVAC/air handling, boilers, electrical, plumbing, elevators, life-safety class) — held as maintainable records organized by the building/location structure (site → building → floor/room, with equipment hierarchies under buildings). The building is itself a record in the system (Fiix creates the facility as a top-level asset; UpKeep organizes assets by location with sub-locations and floor plans). Remove → a generic equipment registry, or a building registry with no maintainable content.
2. **The maintenance work loop.** Work orders — corrective (from reports/requests/failures) and preventive (from schedules) — bound to plant records and carried through a managed lifecycle: raised → triaged/prioritized/assigned → executed (procedures/checklists, labor time, parts, photos) → closed with a record. PM schedules generate recurring work on building systems. Remove → a plant list nobody works, or a dispatch board with no lifecycle.
3. **Persistent maintenance history.** Closed work accumulates on each plant record and rolls up by building — what was done, when, by whom, at what cost — as the queryable basis for troubleshooting, compliance evidence, and condition/renewal decisions. Remove → work log with no memory.

**Binding:** the operator's own building plant (the buildings the organization operates and maintains), organized in building terms. Remove the binding → the generic CMMS core (§16). This binding is what makes the leaf "building" maintenance rather than maintenance in general.

Jointly-held load-bearing:
- 1 alone = building/equipment registry
- 2 without 1 = free-floating work orders (generic ticketing)
- 3 without 1+2 = a log with nothing to attach to
- 1+2 without 3 = dispatch with no memory
- 1+3 without 2 = stale archive
- 2+3 without 1 = work log with no plant identity
- 1+2+3 without the building binding = the generic CMMS

### L1 — Common Mature Structure

- Preventive maintenance scheduling (calendar/date + meter/runtime triggers auto-generating work orders; overdue visibility)
- Request intake from non-maintenance people (occupants/staff submit from phone/QR, typically without a paid seat; building/room/asset attached; triage into the same queue as scheduled work)
- Task templates/checklists; failure codes; custom priorities/statuses
- Mobile technician apps (offline, photos, QR/barcode scan, signature capture, time recording)
- MRO parts inventory linked to work (thresholds, reorder, consumption against work orders)
- Vendors/contractors coordinated inside the same system (assignment, certificates, work recorded on the asset)
- Cost tracking (labor/parts per work order; roll-up by building and by asset)
- Planning surfaces (calendar, backlog, workload)
- Metrics/dashboards (completion, PM compliance, MTBF/MTTR, cost by building)
- Inspections feeding work orders
- Multi-building portfolio operation with one naming scheme

### L2 — Variant / Optional Structure

- Space/occupancy modules (the FMS/IWMS drift — UpKeep Facilities product; Eptura Workplace sibling; Accruent FAMIS 360 sibling)
- Capital planning / condition-assessment feed-out (the building-asset-management drift — replacement forecasting, lifecycle cost, FCA handoff)
- Building compliance programs (life-safety/fire/elevator inspection regimes; regulated-industry compliance packs — MC Compliance)
- BMS/IoT/sensor integration (the BMS seam — sensor readings opening work orders, event/alarm PM triggers)
- AI assistants (conversational answers, voice work capture, risk scoring, auto-generated work)
- Provider marketplaces / external-customer billing (the contractor-side pole)
- Deployment: cloud SaaS vs on-premises; per-user vs per-building pricing; free-requester models
- Industry tunings: education, healthcare, senior living, government, retail chains, storage, non-profits
- Floor-plan mapping as the work-location surface

### L3 — Vendor-specific Detail (Research Notes only)

- UpKeep: Nova AI (builds custom apps, voice→work orders), Providers Network, Edge IIoT sensors, Learn (LMS built from work orders), Safety (OSHA 300/300A/301), per-user pricing with free requesters, work-order number start count, work-order invoicing, bookmark/offline mode.
- Fiix: v5/v6 work-order generations, MAX AI assistant, operator portal, work-order insights (risk scores/diagnosis definitions), nested PMs, multi-asset scheduled maintenance, task groups, rotating assets/tool crib, FactoryTalk Optix condition-based link, multi-site on Professional/Enterprise tiers, free Lite tier.
- Accruent: MRO Work Center / Technician Work Center / Reporter / Service Requester suite decomposition; MC Express vs MC Kinetic; MC Compliance (ISO 27001, FDA 21 CFR Part 11, e-signatures, procedure versioning); Accruent Observe (IoT), RedEye/Meridian (EDMS) integrations; SaaS-or-on-prem posture; FAMIS 360 sibling for public sector/CRE/education.
- Eptura: Asset as one app of the Eptura platform (Engage/Workplace/Visitor/Archibus/Serraview); Assistant for Maintenance in Microsoft Copilot; Technician Copilot voice capture; Autodesk Tandem/Revit BIM integration; Azure hosting; Hippo→ManagerPlus→Eptura Asset lineage.

## Vendor-specific / Rejected Findings

- **Rejected as definitional:** PM scheduling (the cmms pass documented entry tiers shipping without it; reactive-only building maintenance remains in-type), request portals (UpKeep's FAQ calls intake "the defining requirement" for *facility maintenance software* as it markets it, but the sampled evidence shows staff-created and PM-generated work as first-class too — intake is the dominant channel, not the invariant), parts inventory, mobile apps, cloud delivery, AI, floor plans, space modules, capital planning, compliance packs, provider marketplaces.
- **Rejected:** "Building Maintenance Management = FMS module list." The maintenance slice stands alone (UpKeep and Fiix sell it without the FMS service span; Eptura sells Asset as one app beside workplace apps).
- **Rejected:** "Occupant request intake is what makes it building maintenance." Generic CMMS ships request portals too (cmms pass: work-request intake standard); the invariant is the building plant binding, not the intake channel.
- **Rejected:** "Life-safety/compliance machinery is definitional." A minimal reactive+PM building maintenance operation without formal compliance programs satisfies the core; compliance depth is regime/industry-dependent (L2).
- **Rejected:** "This leaf is only an IWMS module." Standalone poles dominate the sample (UpKeep, Fiix, Hippo lineage); suite-embedded is one packaging.

## Boundary Findings

1. **vs CMMS / Maintenance Management (§16, processed) — DISCHARGES the FMS pass's joint-review recommendation (which named both leaves).** The two Types share the care-loop core (plant register + work orders + history + PM + parts). Seam = the domain binding: CMMS is domain-generic maintenance machinery (equipment work management as the center, any industry); this leaf is the **buildings-scoped member of that family** — the maintained objects are a building operator's physical plant and the organizing frame is the building/location structure (site→building→floor/room) with building-systems vocabulary. Removal tests: strip the building binding from this Type → the generic CMMS remains; add the building binding to a CMMS deployment → it operates as building maintenance. This mirrors the building-asset-management pass's family framing ("buildings-scoped member of the asset-management family"). **Taxonomy disposition: keep-both ratified** — the directory keeps CMMS (§16) and this leaf (§17); the seam is recorded rather than merged. Consistent with the cmms pass's own recorded seam ("FM/IWMS centers buildings-space-leases with CMMS-like maintenance modules") and its "industry tuning: facilities" variant note — this leaf is where that tuning becomes the organizing subject.
2. **vs Facility Management System (§17, processed) — DISCHARGES the FMS pass's flag.** FMS = the whole facility-operations service span: the estate of places + the place-anchored work loop + **the service loop with the occupying organization** (requests from the served population, accountability with cost/quality visibility, facility programs, vendor coordination as a first-class posture). This leaf = the maintenance slice: the care loop over the physical plant, without the served-org service posture or the facility-operations span as definitional structures. The FMS pass itself recorded the gradient ("1+2 without 3 = a buildings-scoped maintenance tool"). Removal tests: add the served-org service posture + facility-operations span → FMS; strip to the plant care loop → this Type. The two Types share the work-order substrate; the seam is the service posture and span, not the machinery.
3. **vs Property Maintenance Management (§17, processed) — DISCHARGES that pass's flag.** Property maintenance centers portfolio-wide upkeep across tenancies and resident relationships (property/unit + residents/owners/vendors spine; charge-back economics; unit turns). This leaf centers the building's physical plant/systems (building-scoped, asset-leaning; the plant record is the spine). Removal test (recorded by that pass): strip the tenancy/resident/vendor context → building maintenance. Reverse: add the tenancy/resident spine and portfolio-of-properties framing → property maintenance. In practice a property operator's maintenance module may contain building-maintenance machinery; the organizing subject decides the Type.
4. **vs Building Asset Management (§17, processed) — confirms that pass's seam from this side.** Center of gravity: here the work order/maintenance program is the central object and the plant record accumulates history; there the durable asset record with location + condition + lifecycle economics is central and work orders are evidence advancing each asset's state. Feed-out exists (UpKeep: service history "stays on the asset for the next condition assessment"; Eptura: lifecycle cost visibility) — a documented hand-off, not an overlap of centers. Remove the renewal/lifecycle layer → this Type; add it as the center → building asset management.
5. **vs BMS (§17, processed) — DISCHARGES the BMS pass's joint-review note.** Control loop vs care loop: BMS executes and records what the plant does (sensors/actuators, automated control sequences, live supervision); this leaf governs the human/contracted work on the plant (work orders, PM programs, history). The fault→action seam: a BMS flags off-normal behavior; the maintenance system owns the resulting work order. Sensor→work-order integrations (UpKeep Edge, Fiix event triggers, Accruent Observe) are the documented bridge — integration, not identity.
6. **vs Building Condition Assessment (§17, processed) — confirms that pass's seam.** No work execution in assessment; assessment findings raise work orders here (the care loop lives in this Type).
7. **vs trade field-service management (§ family)** — the contractor's own business system (its customers, jobs, billing) vs the building operator's seat coordinating contractors inside its own maintenance record. UpKeep's Providers and work-order invoicing serve the operator/contractor-coordination pole; the contractor's own FSM remains a different seat.
8. **vs IWMS (§17 sibling, unprocessed)** — IWMS = the enterprise-suite packaging integrating real estate + space + maintenance + capital + sustainability as named modules. This leaf's machinery appears as the maintenance module inside such suites (Eptura Asset inside the Eptura platform; Accruent MC beside FAMIS 360). Note for the IWMS pass: the maintenance module inside an IWMS is an instance of this Type's machinery; the suite packaging is the IWMS's defining structure.
9. **vs Enterprise Asset Management / EAM (§16, processed)** — EAM adds whole-life financial governance (depreciation, TCO, capital planning) as first-class. Building maintenance products at the EAM pole (Eptura Asset's self-description, Accruent's "CMMS and EAM") sit on the same gradient the cmms pass recorded; the canonical discriminator is whether lifecycle financial governance is the center or an extension.

## Historical / Market-Sample Check

- Paper-era building engineering office: a plant/equipment ledger and boiler-room log, a maintenance request book at the front desk, a PM calendar on the wall, work tickets with labor/parts notes, contractor invoices filed per building — satisfies all three L0 legs with no software. The Type predates its software labels.
- On-prem 1990s–2000s facility/building maintenance systems (work orders + PM on a building portfolio, no cloud/mobile/AI/QR) satisfy the core.
- The check passes: no cloud, mobile apps, QR codes, request portals, AI, or compliance packs in the core. Regional products were not directly sampled, but nothing in the core is US-specific (building-systems vocabulary and the site→building→floor structure are global; compliance regimes vary and sit in L2).

## Uncertainties

- Fiix's fiix.com domain now serves unrelated lead-gen content; the official product domain is fiixsoftware.com (verified via Rockwell Automation's product page and Fiix's own help center). Recorded as a sourcing note, not a product finding.
- Accruent's /products/maintenance-connection-cmms URL 404'd (URL guess); the correct product page (/products/maintenance-connection) and the Tier-1 help overview were fetched. No claims rest on the 404'd URL.
- Eptura Asset evidence is product-page level (Tier-2); the Eptura knowledge center was not fetched — no article-level workflow claims made for Eptura.
- UpKeep's "Facilities" product (space/occupancy/building systems) was observed at product-page level only; its depth vs the FMS seam is recorded as L2 drift without module-level claims.
- Exact per-product work-order status vocabularies were not exhaustively verified (UpKeep ships custom statuses; Fiix v5/v6 differ); the final document describes conceptual states only.
- Whether any sampled product enforces building-specific statutory inspection regimes (e.g., elevator certificates) as structured objects was not directly observed; compliance machinery is recorded as L2 without regime-specific claims.

## Final Synthesis

Building Maintenance Management is the building operator's maintenance-operations system of record for its physical plant — the buildings-scoped member of the CMMS/maintenance-management family. Its defining structure is the care loop bound to the building: a register of the building's plant and systems organized by the building/location structure (site → building → floor/room, equipment hierarchies under buildings); work orders — corrective and preventive — bound to those plant records and carried through a managed lifecycle from report/request to recorded closure; and persistent maintenance history accumulating per plant record and per building as the basis for troubleshooting, compliance evidence, and condition decisions. Around that core, mature products add the same recognizable layer: PM scheduling with calendar and meter/runtime triggers, free request intake from occupants (phone/QR, building/room/asset attached), task templates and failure codes, mobile technician apps with offline/photos/QR, parts inventory consumed against work, contractors working in the same system with their work landing on the asset record, cost tracking rolled up by building and asset, planning surfaces, metrics, and inspections feeding work. Variants extend the Type toward space/occupancy modules (the FMS drift), capital planning and condition feed-out (the building-asset drift), compliance packs, BMS/IoT integration (the BMS seam), AI assistants, provider marketplaces, and industry tunings. The Type holds from a self-serve mobile CMMS at a storage-operator portfolio to an enterprise suite-embedded EAM. The seams are all recorded and jointly reviewed: CMMS (domain-generic machinery — the binding is the seam; keep-both ratified), FMS (the served-org service posture and facility-operations span), property maintenance (the tenancy/resident spine), building asset management (the asset-lifecycle center of gravity), BMS (control loop vs care loop), building condition assessment (assessment vs execution), and IWMS (suite packaging vs the maintenance machinery inside it).
