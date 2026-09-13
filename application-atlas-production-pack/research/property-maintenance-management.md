# Research Notes — Property Maintenance Management

## Research Goal

Understand what a Property Maintenance Management application actually is as a software Type: its core objects, the workflow that drives it, its rules and states, and — critically — how it differs from its nearest neighbors (Residential/Commercial Property Management, CMMS, Facility Management/IWMS, Building Maintenance Management, Property Inspection Application, Tenant/Resident Portal, trade field-service management, HOA/Community Association Management, consumer Home Maintenance Application).

## Initial Boundary

- The leaf sits in DIRECTORY §17 (Construction, Real Estate & Facilities), between Tenant / Resident Portal and Property Inspection Application, inside the property-management cluster.
- Working hypothesis entering research: the property manager's / landlord's maintenance operations system — maintenance requests and work orders bound to a managed property portfolio, coordinated across in-house staff and external vendors, with cost resolution toward owners/tenants.
- Prior sibling passes recorded boundary clues this pass must honor or discharge:
  - CMMS pass: "property-maintenance centers tenancy… request intake overlaps, but the organizing spine differs (tenancy vs maintenance operations)."
  - Commercial Property Management pass: "work orders are one module here; that Type makes maintenance the primary object."
  - Property Inspection pass: "work execution is the center (work orders, technicians, completion); there the examination event and its evidence are the center."
  - Trade-FSM family ratification: "property managers coordinate maintenance across their portfolios; this Type is the contractor's own business system — a property manager is a customer here."
  - Hotel Housekeeping pass: "asset-repair work orders vs room-readiness servicing."
  - Home Maintenance Application pass: "the professional/landlord operations system (work orders, vendors, tenants, portfolios); different subject of record and user."

## Research Questions

1. What is the unit of work (request vs task vs work order), and what lifecycle does it carry?
2. Who initiates work — residents/tenants, staff, inspections, recurring schedules? Is resident intake definitional?
3. How is execution organized — in-house maintenance staff, external vendors, or both? Is vendor coordination definitional?
4. What binds work to the portfolio (property → unit → lease/tenant/owner)?
5. What money machinery exists (estimates, approvals, invoices, charge-back to tenants/owners, accounting connection)? Is it definitional?
6. What distinguishes this Type from CMMS (asset spine) and from property-management suites (tenancy/rent spine)?
7. What interfaces exist (manager dashboard, resident intake/status, vendor portal, technician mobile app, owner approvals)?
8. What rules matter (priority/emergency handling, approval gates, entry/access, charge-back responsibility, recurring series)?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophy, and different customer tiers:

1. **Property Meld** — dedicated maintenance-operations platform for property management companies (the purest pole: maintenance only, integrates with PM accounting suites). Markets: single-family, multifamily, HOA, student housing.
2. **Buildium** (RealPage) — all-in-one residential PM suite; maintenance as a module (tasks, work orders, projects, calendar, inspections). Mid-market; US/Canada.
3. **AppFolio** — larger PM platform; maintenance module with in-house leg, vendor network, AI coordinator. Multifamily/SF/student/affordable/association/commercial.
4. **Propertyware** (RealPage) — single-family-focused PM suite; maintenance sold as a separately-loginable add-on ("Propertyware Maintenance"). Small-operator pole.
5. **Rent Manager** (London Computer Systems) — highly customizable PM platform; deep maintenance machinery (service issues, work-order billing with charge-back, make-ready boards). Mixed portfolios incl. commercial, associations, manufactured housing.

## Sources

Fetched 2026-09-09 (all official vendor surfaces):

- Property Meld — homepage, Our Software, FAQ, Scheduling, Communication: https://propertymeld.com/ , /our-software/ , /frequently-asked-questions/ , /scheduling-efficiency/ , /maintenance-communication/
- Buildium — homepage, maintenance feature page, Help Hub: https://www.buildium.com/ , https://www.buildium.com/features/maintenance-request-management/ , https://www.buildium.com/help-hub/
- AppFolio — homepage, maintenance page: https://www.appfolio.com/ , https://www.appfolio.com/property-manager/maintenance
- Propertyware — homepage, maintenance page: https://www.propertyware.com/ , https://www.propertyware.com/property-maintenance-software/
- Rent Manager — homepage, maintenance page: https://www.rentmanager.com/ , https://www.rentmanager.com/maintenance/

Source-access limitations:

- Buildium's knowledgebase (help.buildium.com) is a JavaScript-rendered Salesforce site; direct fetch returned a CSS error. Tier-1 help articles were not reachable; Buildium evidence rests on its official feature/marketing pages (Tier 2).
- Property Meld's help center / Meld Academy was not fetched; evidence rests on official product/FAQ pages (Tier 2).
- No non-US dedicated property-maintenance vendor was sampled; regional regimes are inference, not observation.
- No Tier-1 work-order status vocabulary was verified for any product; conceptual states only.

## Product Observations

### Property Meld (dedicated maintenance-operations platform)

Key observations (evidence layer A unless noted):

- Self-labels "property maintenance software / property maintenance operations platform" for property management companies. Homepage counts "Melds (work orders) completed" — the work order is the central object, branded "Meld."
- Stakeholder model (FAQ): residents submit maintenance issues and are kept informed of work-order status; vendors and technicians communicate directly with residents to schedule; property managers and coordinators have "complete oversight and visibility of all open work orders"; brokers and investors "approve maintenance costs and see how much is spent on maintenance projects."
- Markets: single-family, multi-family, HOA, student housing (dedicated market pages).
- Software pillars: Communication, Scheduling, Oversight & Data, MAX Intelligence (AI), TrueCost (cost).
- FAQ explicitly differentiates from "ticket management to track work orders": intake → technician productivity → resident satisfaction → renewals chain; "PMCs need more than just status updates. They need visibility… insights."
- Integration posture: "integrated with top accounting softwares to eliminate working out of two systems… AppFolio, Buildium, Rent Manager, Propertyware, Yardi and Rentvine" — the dedicated platform deliberately does not replace property accounting.
- Intake: resident web/SSO submission; MAX On-Call AI phone intake "listens, captures details, creates a work order instantly, and only escalates true emergencies based on your rules."
- Scheduling: automated scheduling; segmented cycle-time metrics (speed to schedule, speed to assign, jobs per day); per-vendor/per-technician scheduling speeds; resident-and-vendor self-scheduling; Scheduler 2.0.
- Communication: tracked per work order — resident responses, vendor follow-up, investor approvals; engagement metrics (interaction volume, response speed).
- Vendor side: dedicated Vendor Hub; Vendor Nexus program connects PMCs with pre-screened vendors.
- Technician mobile app for field work orders.
- Web-based; single sign-on for residents.

### Buildium (PM suite, maintenance module)

Key observations:

- Maintenance is a named key feature ("Maintenance Requests — Managing work orders has never been easier") inside an all-in-one PM platform whose other pillars are accounting, payments, leasing, screening, resident experience.
- Maintenance feature page arc: "From the first resident request to the final invoice."
- Core maintenance features enumerated: Task Management, Work Orders, Projects & Templates, Staff Time Tracking, Maintenance Calendar, Property Inspections (powered by HappyCo).
- Task management: "Capture and manage resident requests submitted through Resident Center"; "Create property maintenance tasks for staff with clear ownership and due dates"; "Schedule recurring work like lawn care or seasonal inspections"; time-stamped updates.
- Work orders: "Track the progress of work being performed and expected costs"; "Assign work orders to your staff or vendors"; "Enter quotes or estimates for the work before it's performed"; "Generate a bill directly from a work order" — maintenance activity "connected to your accounting."
- Projects & templates: group related tasks into projects; templates for "unit turns or recurring repairs."
- Maintenance Contact Center: 24/7 resident call capture "creating work orders in Buildium" (RealPage service).
- Marketplace: lists Property Meld as "Maintenance Operations Platform" integration — suite vendors themselves treat dedicated maintenance platforms as complementary.
- Vendor blog uses the leaf's exact name: "The role of Property Maintenance Management systems."
- Portfolios: residential, community associations, mixed-use, single-family, multifamily, commercial, student housing, enterprise.

### AppFolio (PM suite, maintenance module)

Key observations:

- Maintenance is one product pillar ("Maintenance") beside accounting, leasing, resident experience.
- "Track Work Orders From Beginning To Finish": "residents can submit work orders and expect immediate attention… with the ability to track and communicate progress."
- Included capabilities: Online Maintenance Requests, Work Orders, Unit Turn Board, Inspections, Common Area Maintenance (CAM), Mobile Violations & Tracking, In-House Maintenance.
- Money leg: "Pay Your Bills, Owners, and Vendors" — "Automate billing and PO approvals, and approve payments from your mobile app"; "Instantly generate custom invoices for owners using pre-set rules and adjustments."
- Realm-X Maintenance Performer (agentic AI): "reply to residents, analyze images, troubleshoot, prioritize emergencies, and dispatch work to the right technician"; can "dispatch from the Lula Vendor Network to fully automate vendor outsourcing"; drag-and-drop calendar scheduler for in-house technicians.
- Auditing Center: "itemized history of maintenance activities and edits… who performed them."
- Separate portals: Resident Portal, Owner Portal, Vendor Portal (plus investor) — four-sided access structure.
- Association pole: CAM requests/tracking/reconciliation, mobile violations, architectural reviews, board member roles.

### Propertyware (PM suite, maintenance as separately-loginable add-on)

Key observations:

- Single-family-focused PM suite; maintenance has its own product login (app.propertywaremaintenance.com) — maintenance sold as an add-on module with independent access.
- "Propertyware Manages the Entire Maintenance Lifecycle… every job from service request to completion."
- "One work order, multiple vendors": "work with multiple vendors, dispatching, tracking and invoicing—all from one work order."
- "Standardized maintenance tasks": "an endless list of standardized tasks and pricing, allowing for work orders to be created faster… with consistency."
- "Integrated vendor invoicing": "managing your vendors, dispatching work orders, tracking time/expense, invoicing tenants/owners."
- Mobile app: inspection pictures in real time, "snap, tag & go."
- Maintenance Contact Center: call/email answering by agents "who become an extension of your staff."
- Client quote: "feed information to my maintenance vendors in the field… gives my vendors all the information they need to complete and log more jobs in a single day."

### Rent Manager (PM platform, deep maintenance customization)

Key observations:

- Maintenance section: Service Issues, Maintenance Scheduling, Issue Checklists, Service Tech Map, Work Orders, Inspections, Make Ready Boards, Utilities Management, Project Management.
- Service issues: statuses ("New, Work in Progress, Resolved, etc."); field completion via rmAppSuite Pro with "tenants can electronically sign off on completed work"; memorized service issues for repeat tasks; assignment to users with automated notifications.
- Maintenance scheduling: coordinator workflows grouping "properties and technicians"; working hours; Tech View mobile; "residents can use… Tenant Web Access (TWA) portal or the rmResident mobile app to select time slots to schedule service requests"; automated notifications "when requests are created, scheduled, confirmed, and closed."
- Issue checklists: multi-step processes; "advance the issue to another user in the process."
- Service Tech Map: GPS check-in/out per service issue.
- Work Orders & Integrated Billing: "integrate billable expenses into work orders… charge back expenses to tenants or owners in the form of invoices, and optionally add a markup amount."
- Inspections: customizable templates; video inspections; "create service issues for any items that require attention" from inspection results.
- Make Ready Boards: unit-turnover work with color-coded statuses for service issues and inspections.
- Industries: residential, commercial, manufactured housing, associations, student housing, RV/campgrounds, self-storage, affordable, vacation homes.

## Cross-product Comparison

| Dimension | Property Meld | Buildium | AppFolio | Propertyware | Rent Manager |
|---|---|---|---|---|---|
| Packaging | dedicated maintenance platform | module of PM suite | module of PM platform | separately-loginable add-on of PM suite | module of customizable PM platform |
| Unit of work | "Meld" (work order) | task + work order | work order | work order | service issue + work order |
| Bound to | property/unit (via PM-suite sync) | property/unit | property/unit | property/unit | property/unit |
| Resident intake | web/SSO + AI phone (MAX On-Call) | Resident Center | online requests + contact center | contact center + portals | TWA portal / rmResident app time-slot pick |
| In-house execution | technician mobile app | staff tasks + time tracking | In-House Maintenance leg | staff/tech dispatch | rmAppSuite Pro techs, GPS check-in |
| Vendor execution | Vendor Hub + Nexus network | assign to vendors | Lula Vendor Network dispatch | multi-vendor per work order | assign + billable expenses |
| Scheduling | automated, resident+vendor self-schedule | maintenance calendar | drag-drop calendar | dispatch | coordinator schedules + resident slots |
| Cost machinery | cost approval (brokers/investors), TrueCost, accounting sync | quotes/estimates → bill from work order → accounting | billing/PO approvals, owner invoices | vendor invoicing, time/expense, invoice tenants/owners | billable expenses → charge-back invoices to tenants/owners + markup |
| Inspections | (via partners/Nexus) | HappyCo integration | mobile inspections | snap-tag-go mobile | templates + video → create service issues |
| Turns/make-ready | — | project templates for unit turns | Unit Turn Board | — | Make Ready Boards |
| Recurring work | — | recurring tasks (lawn care, seasonal) | — | standardized tasks | memorized issues |
| Status communication to requester | core pitch (tracked engagement) | 24/7 status tracking | residents track progress | owners/tenants informed | notifications at created/scheduled/confirmed/closed + e-sign-off |
| Money resolution posture | approval + integration with PM accounting | built-in (bill from WO) | built-in (bills, POs, owner invoices) | built-in (vendor invoicing, tenant/owner invoices) | built-in (charge-back invoices) |
| AI layer | MAX / MAX On-Call / MAX Intelligence | Lumina AI Maintenance Agent | Realm-X Maintenance Performer | — | Orion AI (platform-level) |
| Portfolio breadth | SF / MF / HOA / student | residential + association + commercial + student | SF / MF / student / affordable / association / commercial | single-family | residential / commercial / MH / associations / student / RV / storage / affordable / vacation |

Cross-product commonalities (evidence layer B):

1. Every product centers on a work item bound to a property/unit in a managed portfolio (work order / service issue / meld / task).
2. Every product carries the same lifecycle arc: intake → triage/assignment → scheduling → performance → completion/closure, with status recorded at each step.
3. Every product supports both executing parties: in-house maintenance staff AND external vendors (weight varies; either satisfies).
4. Resident/tenant self-service intake with status visibility is present in all five — the dominant intake channel — but staff-created tasks, inspection-generated issues, recurring upkeep, and turn work are also first-class in the sample.
5. Cost attaches to the work item in all five (estimates/quotes, bills, charge-back, approvals); built-in invoicing/charge-back is suite-common, while the dedicated pole resolves money through approval + accounting integration.
6. Inspections feed work items in four of five (Property Meld via partners — not directly observed).
7. Unit-turn/make-ready machinery appears in three of five (Buildium templates, AppFolio Unit Turn Board, Rent Manager Make Ready Boards).
8. Communication automation at state changes (created/scheduled/confirmed/closed) appears in all five in some form.
9. Contact-center / call-answering services (human or AI) appear in four of five as an intake augmentation.
10. AI intake/triage/dispatch layers are era-current in three of five.

## Canonical Model

### L0 — Defining Invariant (jointly-held, minimal)

The Type stands on three jointly-held structures:

1. **The managed property portfolio as the work's stage.** Properties — and their units/spaces — held as persistent records to which maintenance work binds; the work's address is a property/unit, not an abstract ticket queue. Remove → generic work-order/ticket system.
2. **The maintenance work item as the unit of record.** A persistent, individually identified work order / request / task bound to a property (commonly a unit), carrying its issue, requester context, priority, status, and completion record, carried through an intake → assignment → scheduling → performance → completion lifecycle. Remove → property database / contact list with no work memory.
3. **Manager-side coordination of executing parties.** The operator (property manager / landlord / association) triages and assigns each work item to an executing party — in-house maintenance staff and/or external vendors — and completion is recorded back against the work item. Remove → request inbox / static log nobody executes.

Jointly-held load-bearing tests:

- 1 alone = property/unit database
- 2 without 1 = free-floating work orders (generic ticketing)
- 3 without 1+2 = staff scheduling with no work record
- 1+2 without 3 = work log nobody is mobilized to execute
- 1+3 without 2 = dispatch board with no per-job memory

### L1 — Common Mature Structure

- Resident/tenant request intake (portal/app/phone) with self-service submission and status visibility
- Vendor management: vendor records, dispatch, vendor-facing portals/hubs, vendor communication
- Scheduling machinery: maintenance calendars, technician schedules, resident-picked time slots
- Mobile field apps for technicians/staff: photos, check-in/out, completion evidence, resident sign-off
- Recurring/scheduled upkeep (seasonal, grounds, routine inspections)
- Inspections feeding work items
- Cost machinery on the work item: quotes/estimates, approval gates, bills/invoices, charge-back to tenants/owners, markup
- Connection to property accounting (built-in in suites; integration in dedicated platforms)
- Unit turn / make-ready coordination
- Standardized task catalogs / templates with pricing
- Communication automation at state changes
- Oversight metrics: cycle times (speed to schedule/assign), costs, vendor/technician performance, backlog
- Priority/emergency handling (after-hours escalation rules)

### L2 — Variant / Optional Structure

- Contact center / call-answering services (human agents or AI) as intake augmentation
- AI intake/triage/dispatch agents (era-current)
- Pre-screened vendor networks / marketplaces
- Commercial/association shapes: CAM tracking & reconciliation, violations tracking, architectural review
- Utility billing/metering riding inside (adjacent capability)
- Built-in accounting vs integration-only money posture (dedicated-platform pole)
- HOA/association-specific workflows
- Regional regimes (US-centric sample; UK/AU equivalents inferred, not observed)
- Tier/plan packaging of maintenance depth

### L3 — Vendor-specific (research notes only)

- Property Meld: "Meld" as work-order brand; MAX, MAX On-Call, MAX Intelligence; TrueCost; Vendor Nexus; Scheduler 2.0; "Ladder of Maintenance Excellence"; benchmark stats (90% resident adoption, 12-second support replies, cycle-time claims).
- Buildium: Lumina AI Maintenance Agent; Maintenance Contact Center (RealPage service); HappyCo inspection integration; Resident Center; marketplace framing of Property Meld as "Maintenance Operations Platform."
- AppFolio: Realm-X Maintenance Performer; Lula Vendor Network; Unit Turn Board; Auditing Center; "Performance Platform" framing.
- Propertyware: separately-loginable Propertyware Maintenance; "snap, tag & go"; AssetProtect insurance; standardized-task pricing lists.
- Rent Manager: rmAppSuite Pro; Service Tech Map; Make Ready Boards; Tenant Web Access (TWA); memorized service issues; Orion AI; 450+ reports framing.

## Rejected Findings

- **"Resident/tenant request intake is definitional"** — rejected. Staff-created tasks (Buildium), inspection-generated issues (Rent Manager, Buildium), recurring upkeep (Buildium), and turn/make-ready work (AppFolio, Rent Manager) are first-class across the sample; vacant-unit work has no resident requester. Resident intake is the dominant channel, not the invariant.
- **"External vendor dispatch is definitional (vs in-house)"** — rejected. AppFolio ships a named In-House Maintenance leg; Buildium assigns work orders to staff or vendors; either executor satisfies. The invariant is assignment to an executing party.
- **"Built-in invoicing/charge-back is definitional"** — rejected. The dedicated-platform pole (Property Meld) resolves money through cost approval plus accounting integrations rather than built-in invoicing. Cost-on-the-work-item is standard; built-in billing is suite-common.
- **"CMMS machinery (asset registers, meter-triggered PM, parts inventory) belongs in this Type's core"** — rejected. Recurring upkeep exists, but the organizing spine across all five products is property/unit + people (residents, vendors, owners), not maintainable assets. No sampled product leads with parts inventory or meter-based PM triggers.
- **"This Type is just a property-management suite"** — rejected. The dedicated-platform pole proves maintenance operations stands alone; suite vendors themselves sell maintenance as a separately-loginable add-on (Propertyware) and list dedicated maintenance platforms as integration partners (Buildium Marketplace).
- **"AI intake/dispatch is definitional"** — rejected as era-current; three of five products ship it, two do not lead with it.

## Boundary Findings

1. **vs Residential / Commercial Property Management (§17 siblings)** — the PM suite's spine is tenancy, rent, leasing, and property accounting; maintenance is one module there (Commercial PM pass: "work orders are one module here"). This Type makes the maintenance work item the primary object of record. The market itself draws the seam: dedicated maintenance platforms integrate with PM accounting suites, and suites sell maintenance as separately-loginable add-ons. Remove maintenance-work primacy → PM suite; add tenancy/rent/leasing spine → PM suite.
2. **vs CMMS / Maintenance Management (§16, processed)** — CMMS organizes around maintainable assets (asset register, work orders bound to assets, PM schedules, parts). Property maintenance organizes around properties/units and the people attached to them (residents, owners, vendors); the CMMS pass recorded the mirror seam ("property-maintenance centers tenancy"). Request intake overlaps; the spine differs. Remove the property/tenancy binding and add asset/PM/parts machinery → CMMS.
3. **vs Facility Management System / IWMS (§17)** — FM/IWMS is occupier-side operations of an organization's own estate (space, leases, occupancy, services); property maintenance is manager/landlord-side over managed/income properties with resident/owner relationships. (FMS pass recorded the same seam from its side.)
4. **vs Building Maintenance Management (§17 sibling, unprocessed)** — working seam recorded for the future pass: building maintenance centers a building's physical plant/systems (building-scoped, asset-leaning); property maintenance centers portfolio-wide upkeep across tenancies and resident relationships. Flag for joint review when that leaf is processed.
5. **vs Property Inspection Application (§17, processed)** — there the examination event and its evidence are the center, consumed by the operator's processes; here work execution is the center. Inspections feed work orders (Rent Manager: "create service issues" from inspections; Buildium: HappyCo → maintenance workflow) — a documented feed-out, not an overlap of centers.
6. **vs Tenant / Resident Portal (§17 sibling, unprocessed)** — the portal is the resident-facing surface (payments, requests, status); property maintenance is the operator-side system the portal feeds. Resident intake/status surfaces are standard capabilities of this Type, not the whole of it.
7. **vs trade field-service management (§29 family, processed)** — the contractor's own business system (customer acquisition, job billing to external clients) vs the manager seat coordinating work on its own managed portfolio; the property manager appears as the *customer* in FSM. Multiple trade passes recorded this seam from their side.
8. **vs HOA / Community Association Management (§17 sibling, unprocessed)** — association governance/billing/communications spine vs maintenance operations; HOA maintenance is a served market of this Type (Property Meld HOA market page; AppFolio CAM/violations). Flag for joint review when that leaf is processed.
9. **vs Home Maintenance Application (§29, processed)** — the homeowner's upkeep of their own home (consumer, one home) vs professional maintenance operations over a managed portfolio. The home-maintenance pass recorded the mirror seam.
10. **vs generic Task/Work-order management** — remove the property/unit binding, the resident/owner/vendor context, and the charge-back economics, and only a generic ticket system remains; those bindings are what make the Type.

## Historical / Market-Sample Check

- Paper-era property management office: a card file of properties/units, a work-order log per building (tenant call → ticket → vendor phone dispatch → completion note → invoice filed → owner statement). All three L0 structures hold with no software: portfolio records, work items with lifecycle, staff/vendor coordination. Resident portals, mobile apps, AI, contact centers are all absent — correctly L1/L2.
- Early desktop-era PM software (Propertyware/Buildium generation, 2004–2008) carried work orders and vendor billing without AI, mobile-first design, or vendor networks — in-type.
- The L0 does not depend on cloud delivery, resident portals, AI, or contact centers. Regional (non-US) products were not directly sampled, but nothing in the core is US-specific (no US-form machinery in the core; charge-back regimes vary by market and sit in L1/L2).
- Conclusion: the definition is not over-fitted to the current AI/communication-heavy market.

## Uncertainties

- Exact per-product work-order status vocabularies were not verified at Tier 1 (Buildium help center unreachable; Property Meld help center not fetched). The final document describes conceptual states only.
- Whether Property Meld generates invoices in-product or only approves costs and syncs to accounting: TrueCost's exact mechanics were not fetched; held as uncertainty, not asserted.
- HOA pole: evidenced by market pages (Property Meld HOA; AppFolio CAM/violations/architectural review) but no association-dedicated maintenance product was sampled.
- Regional (UK/AU) dedicated property-maintenance products not sampled; regional regime differences (e.g., statutory repair timeframes) not asserted.
- Property Meld's inspection capability: not directly observed (Nexus/partner framing only); held as uncertainty.
- Recurring preventive maintenance depth varies (Buildium recurring tasks observed; meter/usage-triggered PM not observed in any sampled product) — recorded, not generalized.

## Final Synthesis

A Property Maintenance Management application is the property operator's maintenance-operations system of record. Its defining structure is small and jointly-held: a managed property portfolio (properties and their units/spaces) as the stage; the maintenance work item (request/task/work order) bound to a property/unit and carried through an intake → assignment → scheduling → performance → completion lifecycle; and manager-side coordination of executing parties — in-house maintenance staff and/or external vendors — with completion recorded back. Around that core, mature products add the same recognizable layer: resident/tenant self-service intake with status visibility, vendor management and portals, scheduling machinery, technician mobile apps with photo/sign-off evidence, recurring upkeep, inspections feeding work, cost machinery (estimates, approvals, bills, charge-back to tenants/owners) connected to property accounting, unit-turn coordination, standardized task catalogs, communication automation, oversight metrics, and emergency handling. Variants extend the Type by packaging (dedicated platform vs suite module vs separately-loginable add-on), execution mix (in-house-heavy vs vendor-heavy), portfolio segment (single-family, multifamily, commercial, associations, student), intake augmentation (contact centers, AI agents), and money posture (built-in billing vs approval-plus-integration). The Type's boundaries hold against CMMS (asset spine vs property/tenancy spine), PM suites (maintenance primacy vs tenancy/rent primacy), facility management (occupier vs manager seat), property inspection (examination vs execution), resident portals (resident surface vs operator system), and trade FSM (contractor seat vs manager seat).
