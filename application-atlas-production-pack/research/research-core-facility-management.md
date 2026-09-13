# Research Notes — Research Core Facility Management

Research date: 2026-09-09
Slug: research-core-facility-management
Directory leaf: Research Core Facility Management (Section 23 — Education, Research & Knowledge Institutions)

---

## Research Goal

Understand what a Research Core Facility Management application actually is, from real products:

- what objects exist inside it (facility, instruments, services, reservations, requests, users, groups, funds, rates, charges, invoices)
- who uses it and how the roles differ
- how the core workflows run (onboarding, instrument reservation, service request, usage capture, billing, reporting)
- which rules and states really drive behavior (financial approval, training gating, cancellation economics, rate tiers)
- where the boundary lies against LIMS, Scientific Instrument Management, Resource Calendar, and Research Animal Facility Management

## Initial Boundary

Initial hypothesis (before research):

- This is the software used to operate a shared research instrumentation/service facility ("core facility", "shared resource") at a university, research institute, hospital, or company.
- Its center is likely: shared instruments + a multi-lab researcher population + scheduling + training + usage tracking + recharge billing.
- Nearest neighbors: LIMS / Research LIMS (sample-centric), Scientific Instrument Management (asset lifecycle), Resource Calendar (generic booking), Research Administration Platform (grants), Research Animal Facility Management (sibling facility type), Calibration Management / CMMS (maintenance).
- Likely confusion: with LIMS (both live in labs) and with generic resource scheduling (both have calendars).

## Research Questions

1. What is the facility's "catalog" and how is it presented to researchers?
2. How does a researcher get access — registration, lab/group membership, training, qualification?
3. How does instrument reservation work (schedule, states, approval, conflicts, cancellation)?
4. How do service requests work (forms, quotes, phases, staff assignment)?
5. How is usage captured (booked time vs actual time; kiosk, interlock, card reader, workstation app)?
6. How does the recharge/billing loop work (rates, subsidies, funding sources, approval, invoices, ERP)?
7. What roles exist and what can each do?
8. What reporting does the facility run on (utilization, revenue, outcomes)?
9. What integrates with the institution (SSO, ERP, access-control hardware)?
10. Where is the boundary against LIMS, instrument management, and generic resource scheduling?

## Representative Products

Selected for market representation, documentation quality, different product philosophy, and different geographies/customer levels:

| Product | Vendor | Why selected | Angle |
|---|---|---|---|
| iLab Operations Software | Agilent | Dominant market leader in academic core facilities | Storefront + Fund/PI financial model; richest Tier-1 help docs |
| BookitLab | Prog4biz | Established competitor since 2007, universities + pharma | Modular platform framing (scheduling / access control / billing / requests / assets) |
| Stratocore PPMS | Stratocore | European leader, developed inside Institut Pasteur | Billing/project-centric framing; service-based vs instrument-based cores |
| Calpendo | Exprodo Software | UK, scheduling-first philosophy since 2008 | Calendar-centric configurable system; shows the "scheduling pole" of the type |

NEMO (a newer entrant frequently named in this market) was intended as a fifth sample but its site could not be fetched (see Uncertainties). Four products satisfy the sampling rules.

## Sources

Tier 1 (official operational documentation):

- Agilent iLab Help Site — https://help.ilab.agilent.com/
  - Key iLab Terms (glossary): https://help.ilab.agilent.com/en_US/99540-getting-started-with-ilab/261285-key-ilab-terms.html
  - Using a Core (index): https://help.ilab.agilent.com/en_US/37179-using-a-core.html
  - Request Services: https://help.ilab.agilent.com/en_US/37179-using-a-core/265959-request-services.html
  - Schedule Equipment: https://help.ilab.agilent.com/en_US/37179-using-a-core/264636-schedule-equipment.html
  - Using Kiosk: https://help.ilab.agilent.com/en_US/37179-using-a-core/266114-logging-into-kiosk.html
  - Payment Methods: https://help.ilab.agilent.com/en_US/37179-using-a-core/296846-payment-sources.html

Tier 2 (official product pages):

- BookitLab — https://www.bookitlab.com/ (home; module map: Core Facility Management, Lab Equipment Scheduling, Usage & Access Control, Request Management/LIMS, Enterprise Asset Management, Billing, Reporting, Integrations)
- Stratocore PPMS — https://www.stratocore.com/ (home) and https://www.stratocore.com/features (feature pages: Equipment Booking, User Access Management, Training Management, Service Ordering, Price & Subsidy Rules, Automated Invoicing, Usage Tracking, Stratobox, Maintenance, Asset Catalogue, Reporting, API)
- Calpendo — https://calpendo.com/ (home) and https://calpendo.com/calpendo-features (features: resources, bookings, projects, workflows, rules, permissions, CAR, reports, SSO, deployment)

Access limitations:

- Agilent's marketing product page for iLab (agilent.com) returned HTTP 403; iLab evidence rests on its official help site (which is the stronger source for operational structure anyway).
- NEMO: nemosoftware.com returned an empty response; nemolabs.com failed with a rendering error; search engines returned unrelated results (NVIDIA NeMo). Dropped after 2–3 attempts per the network-restriction rule. No claims in this research depend on NEMO.
- No Tier-3 sources were needed; official documentation was sufficient.

---

## Product A — iLab Operations Software (Agilent)

### Key observations (evidence layer A unless noted)

**Entity hierarchy** (glossary, Tier 1):

- Institution → contains Core Facilities / Shared Resources, Labs/Groups, Departments, Centers.
- "Core Facility / Shared Resource: an entity that offers services or access to resources for customers… each Core has an online store-front that customers can use to identify the offerings available and directly order products/services. For core administrators and staff, iLab provides workflows to help deliver services, manage resources, complete billing and generate reports."
- Lab/Group: users supervised by a PI and/or Lab/Group Managers; "typically used as the primary way to organize access to Funds and manage financial approvals for purchases at Core Facilities."
- Department: optional grouping of labs for escalated financial approvals and reporting.
- Center: grouping of labs and/or cores across institutional boundaries, used for special price types and subsidies.

**Roles** (glossary): Institutional Administrator; Principal Investigator (manages users, controls financial access/approvals); Lab/Group Manager (PI's delegate, similar rights); Lab/Group Member; Core Administrator (modifies core workflow, generates billing events and reports); Core Member (staff performing workflow functions — complete orders, deliver services); "Core Customer" (any user ordering services or securing resources — a role-in-context, not a separate account type).

**Fund** (glossary): "the general term used to describe a way for users to pay for services… a Fund may be known as a 'Grant number', 'Chart Field String', 'Speed Code', 'Account Number', 'Project ID'… Funds are allocated to Labs/Groups, and from there assigned to individual Lab/Group members by the PI or Lab/Group Managers. When a user orders a product/service from a Core, or looks to make a reservation, they will be able to choose from the Funds made available to them."

**Core objects** (glossary): Service request ("a customer request for a Core to perform various services"); Charge ("an individual 'line item' that corresponds to a specific product/service provided by a core"); Resource/Equipment ("something that a Core customer can make a (time-based) reservation against. Often represents a piece of equipment, but can also refer to other resources such as specific facility or time with specialists"); Schedule/Calendar ("a collection of the available and reserved time slots for a specific Resource/Equipment"); Reservation ("a claim on a specific time slot on a Schedule/Calendar").

**Financial approval** (glossary): "When services are ordered or resources are reserved, typically a financial approval step needs to be completed before the transaction can be completed. The Principal Investigator or a Lab/Group Manager designated as a financial contact will need to provide an explicit approval, unless the amount is below a configurable Approval Threshold (in which case the approval is performed automatically)."

**Integrations** (glossary): Financial Integration (automatic allocation of Funds to Labs/Groups; automatic upload of billing data to internal/external billing systems); ID integration (login with institutional credentials — SSO).

**Request Services workflow** (help article): customer browses the core's service list (categorized, searchable, optionally with prices) → initiates a request → completes required forms (per-form status Not started / In Progress / Completed; required fields enforced) → enters payment information (internal: Fund Number from the assigned list; external: PO number, wire transfer, credit card) → submits → core reviews and typically issues a quote (scope of work + estimated cost) → customer agrees or declines → financial approval by PI/Lab Manager (or departmental administrator in some cases) → only then can the core start work → customer tracks status in "View My Requests". Quote steps may be bypassed when cost is known at submission or there is no charge.

**Schedule Equipment workflow** (help article): resources listed with description and pricing toggles → per-resource calendar (day/week/month/multi-view; multi-view lists multiple physical instances of the same equipment) → color-coded events (your future reservations, your past reservations, unavailable time, pending core approval, approved, others' reservations, cancelled/no-shows) → reservation created by drag-and-drop; user selects the Lab/Group the reservation is made under → reservation details include: comments/activity, contacts/billing info, collaborators (can view/edit/start but not edit payment), required forms, linked schedules (reserve multiple resources at once; a required linked resource is auto-selected), repeating events, usage type (assisted vs unassisted — cost may depend on it), cost of reservation, additional service charges, payment information, link to an ongoing service project, email invites → change/delete/cancel subject to core-configured constraints (e.g., cannot change after approval; cutoff windows; delete becomes cancel near start time; cancellation fees may apply and must be accepted).

**Kiosk** (help article): "an advanced module that allows a facility to track users' time on instruments" — user logs in with credentials (or institutional AD), starts a scheduled reservation or creates a walk-up session on an open instrument; "in conjunction with interlock usage, a user will be required to login through the kiosk in order to gain access to the instrument"; session shows elapsed time, can be extended; starting/finishing powers devices on/off or locks/unlocks control applications; payment information and add-on charges adjustable during the session.

**Payment methods** (help article): Internal Funds (from the PI-assigned list; orange warning when a fund is within 30 days of its expiration date, if set); Split Charges (percentage allocation across funds, must total 100%); PO Number (external customers); Standing Purchase Orders (created in the system, routed for approval, shareable with group members); Subsidies (automatically applied by the core, shown as separate line items); Center Assigned Funds (special funds from Centers, assigned to labs for use at specific cores); wire transfer / check / credit card.

**Interpretation**: iLab's model is the cleanest statement of the type's economy: catalog (storefront) → identified customer in a lab/group → reservation or service request → financial approval → usage → charges → funds → billing upload. Evidence layer A for all specifics; the general shape is corroborated by the other products (layer B).

---

## Product B — BookitLab (Prog4biz)

### Key observations (evidence layer A; product-site tier)

Positioning: "helps research organizations manage scheduling, equipment, services, and access in one configurable platform"; "trusted by 100+ research institutions"; since 2007; 130,000+ users; customers include universities, research institutes, pharma (Stanford, NIH, Bosch, Unilever, Stryker…).

Module map (site navigation):

- **Core Facility Management**: "a unified platform for scheduling, billing, training, service catalogs, and access control across one or multiple facilities."
- **Lab Equipment Scheduling**: real-time availability, visual calendar/timeline, automated conflict detection (double-booking prevention), customizable reservation forms, booking/billing rules, approval workflows; "training, relationships, modes, pre-requisites, automatic billing, assemblies, custom notifications."
- **Usage & Access Control**: "enforce training requirements, monitor real-time usage, control equipment access via card readers or locks, and maintain complete compliance logs."
- **Request Management / LIMS**: service requests from submission to completion; custom submission forms, custom processing workflows, milestones, cross-assignments; sample and run tracking lifecycle (collection → testing → storage → disposal); communications, notifications, quotes, billing rules; processing loads management.
- **Enterprise Asset Management**: centralized asset database, lifecycle tracking (acquisition → retirement), maintenance alerts, work orders for maintenance and scheduled checks, calibration, incidents.
- **Billing**: "generate invoices based on equipment usage, service requests, and custom billing rules"; billing types one-time, recurring, usage-based; "chargebacks, rate structures, and reports ready for your finance team"; "track project-specific billing and grant spending."
- **Reporting**: custom dashboards (e.g., a "Genomics Core Overview" with instruments by operation type, availability, tables).
- **Integrations**: ERP/accounting (Unit4, PeopleSoft, SAP, QuickBooks, Oracle, Xero), identity (LDAP, Active Directory, Azure AD, OKTA), instrument access-control devices, door controllers, APIs/webhooks.

Customer testimonial (layer A as vendor-published quote; treat as marketing-adjacent): interdepartmental core facility with "over 150 research labs with 500 registered users"; goals: "monitor and control booking, usage and billing"; outcomes: "increased availability, fair user time allocation and overall financial management."

**Interpretation**: same object world as iLab (catalog, schedule, requests, training, billing), packaged as configurable modules; adds explicit asset-lifecycle and sample-tracking depth (LIMS-adjacent) and physical access control.

---

## Product C — Stratocore PPMS

### Key observations (evidence layer A; product-site tier)

Positioning: "the complete SaaS solution for running research operations"; "developed at the Institut Pasteur and refined with The Rockefeller University"; 250+ organizations; 191,000 researchers; 45,000 instruments/services/consumables; 20 countries. Solutions pages enumerate core types: service-based cores vs instrument-based cores; genomics, proteomics, bioinformatics, flow cytometry, light/electron microscopy, histology, metabolomics, mass spectrometry, sequencing, structural biology, vector, NMR cores. Also sells to pharma, biotech, CROs, and "Shared Laboratories" (incubators).

Feature pages:

- **Equipment Booking**: color-coded calendars with real-time availability; conflict resolution and intelligent restrictions; automated notifications; rules for advance bookings, recurring sessions, restricted user groups; "access tied to training validation and project status"; central or facility-level configuration.
- **User Access Management**: facility-specific control over user rights; permissions for equipment, services, bookings and pricing; rules per user, project, team or institution; multi-facility central dashboard; granular admin tiers.
- **Training Management**: "training workflows linked to access permissions"; define trainers, sessions, verification steps; log and track training history; "grant progressive access based on completed training"; multiple training levels and resource-specific rules.
- **Service Ordering & Tracking**: self-service ordering; dynamic pricing rules by user, affiliation or project; request forms with questionnaires; validation process; staff member assignment per service line; service phases management; sample manifests; record outcomes and link back to publications.
- **Flexible Price & Subsidy Rules**: pricing rules by user, service, affiliation or project; subsidies/rebates by eligibility; "apply different rules for internal, academic or commercial use"; exceptions and overrides.
- **Automated Invoicing**: "create automated invoices and journals by user, project or facility"; "link pricing to validated usage and bookings"; ERP and finance system integration; role-based financial permissions and approvals; PDF invoices with audit trails. Home page adds: unlimited price and subsidy rules; "financial permissions for PIs, Groups, Users and Projects"; "financial account managers/owners"; "financial account provisioning and validation"; "automated financial journals and PDF invoices."
- **Usage Tracking**: "lightweight application for instrument workstations"; track usage sessions in real time; "separate booked vs actual time for fair billing."
- **Stratobox Hardware Interlock**: PIN-based access for trained users; monitors power state and device usage; Ethernet install; integrated with equipment rules.
- **Maintenance & Incident Management**: log/prioritize/assign incidents; downtime with timestamped audit trails; internal and third-party maintenance scheduling; maintenance history reports.
- **Asset Catalogue**: "organise and promote your instruments, services and facilities in one searchable directory"; flexible hierarchy; filterable search by capability, location or service; visibility by user group or role.
- **Project Workflow & Milestone Management**: multi-step validation workflows; lifecycle tracking; files (reports, results, risk assessments, quotes); project roles.
- **Consumables & Inventory**: stock tracking, reorder alerts, barcode support, usage analytics by item/user/project.
- **Custom Reporting & Analytics**: reports by user, facility, project or service; export/Power BI/Tableau; KPIs across time, instruments, cost centres; "track and associate publications with specific projects or services."
- **API**: connect with LIMS, finance and reporting systems.

Customer testimonials (vendor-published): "monthly billing can be achieved by the click of a few buttons" (flow cytometry facility); "improving the speed and accuracy of our monthly invoicing" (14 core facilities, cancer research institute); "integration with our authentication, accreditation and billing systems" (university IT); "booking, user management, messaging, billing, statistics" (imaging facility).

**Interpretation**: PPMS makes the financial/project layer the spine (price rules, subsidy rules, financial permissions, journals) and treats scheduling, training, usage capture, and maintenance as the operational ring around it. Confirms service-based vs instrument-based cores as two recognized shapes of the same type.

---

## Product D — Calpendo (Exprodo Software)

### Key observations (evidence layer A; product-site tier)

Positioning: "intelligent and automated facility management system… streamlining their booking and resource management of instruments, staff, 3d printers, meeting rooms and much more"; since 2008; customers are universities, hospitals, research institutes, museums (imaging and MRI facilities dominate testimonials).

Products: Calpendo (Starter / Premium licences), Calpendo Enterprise (multiple interconnected facilities, cross-facility management), Calpendo Mobile, Calpendo Activity Recorder (CAR).

Features:

- **Calendar-centric**: "built around an intuitive Calendar interface to view and manage your bookings across multiple resources"; day/week/month/infinite-scroll views; bookings by status including cancelled; custom bookmarks.
- **Unlimited bookable resources**: "in addition to equipment such as an MRI or a microscope, you can also use Calpendo to book meeting rooms, technicians, or even a parking space" — the resource concept is generic, the facility applies it to research instruments.
- **Unlimited bookings** with optional limits on per-user booking volume.
- **Projects**: "digital bodies of work against which you can store top-level information… associated with specific bookings… used for reporting, billing, or to control access to certain resources"; can be customized or "not be used at all."
- **Workflow automation** (low-code "Workflows" engine): notifications; "automate training records and renewals"; "calculate booking costs for your bookings based on the parameters specific to your context."
- **Booking rules**: govern booking duration, frequency, timing; customisable error messages; target specific resources, user groups or projects. **Time templates**: opening-time slots with per-user-type booking rules.
- **Permissions system**: per-property, per-role; "make it look and behave quite differently for your users and user roles."
- **Custom properties / data structures**: "entire new data structures can be added to build bespoke inventory or training systems."
- **CAR (Activity Recorder)**: "a downloadable utility… installed on computers attached to certain instruments. CAR then records actual usage of the instrument, based on a user signing into the system. This data can then be transferred back to Calpendo for use in reporting."
- **Reports**: custom and scheduled reports; CSV export; API; full data import/export.
- **SSO**: Shibboleth and other tools; "we still provide the means to authorise users to use your system so that you have absolute control over who has access."
- **Deployment**: cloud (ISO 27001-certified providers) or on-site installation (for privacy-regulated data).

Customer testimonial (vendor-published, states the buyer checklist): "we were in the market for an integrated software solution that provides web scheduling, project/user management and billing capabilities."

**Interpretation**: Calpendo demonstrates the scheduling pole of the type: the calendar is the spine; billing, training, projects, and usage capture are configured around it. It also shows the type's edge: with billing and projects unused, it converges toward a generic resource calendar — the buyer testimonial shows that in this market, scheduling + projects/users + billing is the expected bundle.

---

## Cross-product Comparison

| Dimension | iLab | BookitLab | PPMS | Calpendo | Layer |
|---|---|---|---|---|---|
| Shared instrument/service catalog presented to researchers | "online store-front" per core; service list with categories/prices | "service catalogs" module | "Asset Catalogue… searchable directory" of instruments, services, facilities | resources incl. instruments; information pages | B |
| Time-based reservation on per-resource schedule/calendar | Schedule/Calendar per Resource; drag-and-drop; color-coded states | visual calendar/timeline; conflict detection | color-coded calendars; conflict resolution; queues/priorities | calendar is the product's spine | B |
| Reservation attributed to identified user + lab/group + payment source | select Lab/Group + Fund at reservation | reservation forms + billing rules | user budget codes; financial permissions for PIs/Groups/Users/Projects | bookings tied to users and projects | B |
| Service requests as a parallel track | service request with forms, quote, approval, status | Request Management/LIMS with forms, milestones, quotes | service ordering with questionnaires, validation, phases, staff assignment | possible via custom structures/workflows (weakest here) | B |
| Usage capture beyond the booking | Kiosk sessions (scheduled + walk-up); interlock | "actual usage" monitoring; card readers/locks | workstation usage app; "booked vs actual time" | CAR records actual usage at sign-in | B |
| Training/qualification gating access | required forms; core approval of reservations (training modules exist but not fetched in detail) | "enforce training requirements"; prerequisites | "access tied to training validation"; progressive access | "automate training records and renewals"; custom training structures | B |
| Rates, subsidies, price rules | pricing per resource; subsidies auto-applied; center funds | rate structures; chargebacks; billing rules | unlimited price & subsidy rules; internal/academic/commercial tiers | booking cost calculation via workflows | B |
| Charges → funding sources → invoices | Funds (grant/chart-field/speed code/account/project ID); split charges; POs; billing upload | invoices from usage/requests; grant spending; ERP connectors | automated invoices & journals; ERP integration; financial account provisioning | cost calculation + reports; billing via projects/workflows (thinnest of the four) | B |
| Financial approval before work | explicit PI/lab-manager approval; configurable auto-approval threshold | approval workflows | role-based financial permissions and approvals | approval via workflows/permissions | B |
| Maintenance & incidents | schedule banners; unavailable-time events | work orders, maintenance, calibration, incidents | incident assignment, downtime audit trails, maintenance scheduling | possible via custom structures | B |
| Reporting: utilization + revenue | billing events and reports per core | dashboards (usage, revenue, expenses) | usage, productivity, income metrics; Power BI/Tableau | custom & scheduled reports | B |
| Multi-facility institution | Institution contains many cores; institutional admins | "one or multiple facilities" | cross-facility coordination; central dashboard | Calpendo Enterprise cross-facility | B |
| SSO / identity integration | ID integration (institutional credentials) | LDAP/AD/Azure AD/OKTA | SSO | Shibboleth | B |
| External/commercial users | PO numbers, standing POs, credit card, wire | supported via billing rules | internal/academic/commercial price tiers | configurable | B |
| Publication / outcome tracking | not observed in fetched pages | not observed | publications linked to projects/services | not observed | A (single product → optional) |
| Sample manifests / sample tracking | service request forms (forms generic) | sample & run lifecycle | sample manifests | custom structures | B (present, depth varies) |
| Hardware interlock product | interlock integration with kiosk | card readers/locks | Stratobox PIN interlock | not observed (CAR is software-side) | B |

Stable commonalities (layer B) across all four: catalog/storefront; per-resource calendar booking; user+group attribution with payment source; service requests; training/qualification; rates/subsidies; charges→funding sources→invoices; financial approval; reporting; multi-facility; SSO; ERP integration; usage capture; maintenance.

Divergences (implementation posture, not type structure):

- Where the spine sits: iLab = storefront + fund model; PPMS = price/subsidy rules + projects; Calpendo = calendar; BookitLab = modular platform.
- How usage is captured: kiosk vs workstation app vs card reader vs PC sign-in utility vs booking-only.
- How deep sample tracking goes: from generic forms (iLab) to sample/run lifecycle (BookitLab) to manifests (PPMS).
- Whether billing is a core module or a configured capability (Calpendo's Premium workflows vs iLab/PPMS billing engines).

## Canonical Model

### L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being recognizable as this type:

1. **The shared facility catalog as the managed, rate-bearing offering.** The facility's shared research instruments and services held as managed objects — instruments bookable as time on schedules, services orderable as requests — each carrying description, visibility control, and pricing, presented to the researcher population as the facility's storefront/catalog.
   Remove → an asset registry or a rate list with no operation.

2. **Identified-user reservation/request with per-user, per-group usage attribution.** Researchers act as identified members of labs/groups: they reserve instrument time or submit service requests; every reservation/request is attributed to the identified user and their group and carries a payment source; access is commonly gated by qualification.
   Remove → an anonymous/public booking board; the accountability and the billing join-key disappear.

3. **The usage-to-recharge loop.** Recorded usage and completed work are priced at facility rates (with internal/external tiers and subsidies), accumulated as charges, and billed on a recurring cycle to funding sources (grants, departmental accounts, POs), producing invoices/statements and utilization/revenue reporting.
   Remove → a resource calendar / scheduling tool; the facility's economic operation disappears.

Jointly-held load-bearing tests:

- 1 alone = asset registry / rate list
- 2 without 1 = generic booking site
- 3 without 1+2 = billing shell over nothing
- 1+2 without 3 = resource calendar
- 1+3 without 2 = rate card with no attributable usage
- 2+3 without 1 = usage metering with no facility catalog

Anti-overfitting notes:

- **Training/certification gating is NOT definitional.** Observed in all four sampled products (layer B, near-universal), but a facility management system without training records is still this type — it is the access-gating mechanism, not the invariant. The invariant in leg 2 is identified-user attribution.
- **The specific billing cadence is NOT definitional.** "Monthly invoicing" appears repeatedly in customer testimonials (PPMS) but the invariant is the recurring recharge cycle, not the month.
- **Actual-usage capture (kiosk/interlock/CAR) is NOT definitional.** All four products have some form, but booking-based charging satisfies the loop; the capture mechanism is an implementation axis.
- **Service requests are NOT separately definitional.** An instrument-only self-service core (PPMS's "instrument-based cores") satisfies the type with reservations alone; service requests are the second arm of leg 2's "reservation/request".

### L1 — Common Mature Structure

Present in most mature products; makes the operation practical but does not define the type:

- training/qualification management (records, verification, progressive access, renewals)
- service request workflows (custom forms/questionnaires, quotes, validation, phases, staff assignment)
- actual-usage capture at the instrument (kiosk, workstation app, card readers, hardware interlock, walk-up sessions)
- maintenance & incident management (downtime, work orders, service scheduling)
- instrument/asset lifecycle records (acquisition → retirement; calibration)
- reporting & analytics (utilization, revenue, exports to BI tools)
- financial integrations (ERP upload, fund provisioning, journals)
- identity integration (SSO with institutional credentials)
- multi-facility institutional deployment (one institution, many cores, cross-facility oversight)
- notifications/messaging to users (confirmations, cancellations, downtime)
- consumables/inventory management

### L2 — Variant / Optional Structure

Depends on segment, funding model, deployment, customer scale:

- external/commercial user commerce (POs, standing POs, credit card, wire transfer)
- subsidy models (automatic subsidies, center-assigned funds, percentage split charges)
- publication/research-output tracking linked to facility usage
- scientific project management (milestones, multi-step validation)
- sample manifests / sample & run lifecycle tracking (LIMS-adjacent depth)
- lite ELN, animal facility management (module-level adjacencies in some products)
- deployment: cloud vs self-hosted (privacy-regulated data)
- software licensing posture (per-module, per-facility, all-inclusive)
- non-university operators (pharma internal facilities, biotech, CROs, incubator shared labs)

### L3 — Vendor-specific Structure

(Research Notes only; must not enter the final document as type structure)

- iLab: "Fund" terminology and its synonyms (grant number, chart field string, speed code…); Center Assigned Funds; configurable Approval Threshold; Kiosk module; orange fund-expiry warning at 30 days; Agilent ownership; "Core Facility / Shared Resource" naming.
- PPMS: "PPMS" name; Stratobox hardware interlock; developed-at-Institut-Pasteur lineage; "dynamic scenario pricing"; service-based vs instrument-based cores marketing taxonomy; Power BI emphasis.
- Calpendo: CAR utility; Starter/Premium/Enterprise licence tiers (e.g., booking-rule and custom-property limits per tier); low-code "Workflows" engine; time templates.
- BookitLab: Prog4biz company; module packaging (Core Facility Management / Lab Equipment Scheduling / Request Management-LIMS / EAM); "assemblies" and "modes" in reservation configuration; Lite ELN; animal facility module.

## Boundary Findings

**vs LIMS / Research LIMS.** LIMS is sample-centric: samples, assays, test runs, results, chain of custody. Core facility management is access/usage/economics-centric: who may use the shared instrument, when, and who pays. The two meet at service requests that carry samples (sample manifests, sample lifecycle appear in both). Test: remove the recharge/access loop and keep sample-assay workflows → LIMS territory. Remove sample workflows and keep scheduling+recharge → this type. PPMS's own API page names LIMS as an external system to connect to — the products themselves treat them as neighbors, not the same thing.

**vs Scientific Instrument Management.** Instrument registry, maintenance, calibration, lifecycle is one operational ring inside core facility management (all four products have some of it), but the center is the facility's service operation to a researcher population. Test: remove scheduling/billing/users and keep asset lifecycle → Scientific Instrument Management / CMMS territory.

**vs Resource Calendar (and generic resource scheduling).** A resource calendar has bookings on calendars but no facility-service economics: no rate-bearing catalog, no funding-source charging, no PI financial approval, no recharge reporting. Calpendo is the instructive pole: it is calendar-spined, but its market positioning ("Core Facility Management System") and its buyers' checklist (scheduling + project/user management + billing) show that the economics are what make it this type. Test: remove leg 3 → resource calendar.

**vs Research Administration Platform / Research Grant Management.** The Fund here is a payment vehicle (an account to charge), not a grant lifecycle object (application, award, reporting). Facility recharge reporting supports grant renewals but is not grants administration.

**vs Research Animal Facility Management.** Sibling type in a "shared research facility" family: both manage a shared institutional facility with per-user attribution and recharge-style billing, but the managed subject differs — animal colonies/cages/husbandry vs instruments/services. BookitLab shipping animal facility management as a separate module is direct evidence that the market treats them as siblings, not the same type.

**vs Enterprise Resource Scheduling Platform.** Generic resource scheduling lacks the research-facility semantics (qualification-gated instrument access, grant-funded payment, internal/external rate tiers). Overlap is real; the domain objects are the differentiator.

**"Remove what to become another type" summary:**

- remove the recharge loop → Resource Calendar
- remove the shared-facility/multi-lab context (single lab, no recharge) → lab scheduling tool / single-lab management
- remove scheduling/access and keep samples+assays → LIMS
- remove scheduling/billing and keep asset lifecycle → Scientific Instrument Management / CMMS
- replace instruments/services with animal colonies → Research Animal Facility Management

## Historical / Market-Sample Check

Paper-era core facility (pre-software): a sign-up sheet on the instrument (schedule/reservation), a usage logbook (per-user attribution), training given by the facility manager before keys were handed out (qualification gate), and monthly recharge invoices sent to grant numbers (usage-to-recharge loop). All three L0 legs are satisfied without any modern software — the software digitized an existing operational form, it did not invent it. ✓

Older/regional software generation (2000s homegrown schedulers and early commercial systems): scheduling + billing were the first two modules facilities bought; training and usage capture were added as systems matured. These earlier systems still fit the three-leg core. ✓

Non-university operators: PPMS explicitly sells to pharma, biotech, CROs, and incubator "shared laboratories" — the type is not university-specific, though universities dominate the customer logos across all four products. ✓

Non-charging facilities: a fully institution-subsidized facility still runs the same machinery (rates may resolve to zero or to 100% subsidy; iLab documents subsidies as automatic line items). The machinery is the invariant; whether and how much is charged is configuration. ✓

Conclusion: the L0 survives the historical and market-breadth check.

## Uncertainties

1. **Agilent marketing page inaccessible (HTTP 403).** iLab evidence rests entirely on its official help site. This is acceptable (help docs are the stronger tier for operational structure), but positioning-level claims about iLab's market share were not verified and are not made.
2. **NEMO not sampled.** Site unreachable (empty response / render error); search polluted by NVIDIA NeMo. A fifth product would add breadth but the four-product sample already shows stable commonalities; no claim depends on NEMO.
3. **Billing cadence.** "Monthly" appears in PPMS customer testimonials and is the folk default of the domain, but no fetched official doc states a universal cadence. The final document says "recurring cycle (commonly monthly)" — calibrated wording.
4. **iLab training module depth.** iLab's help site fetched pages show gating via required forms and core approval; its training/certification features were not directly fetched. The cross-product training claim is carried by BookitLab/PPMS/Calpendo (3/4 direct) and iLab's approval/form gating; wording in the final document reflects this.
5. **External-user share.** No evidence quantifies how much external/commercial usage is typical; no numbers are stated.
6. **Calpendo billing depth.** Calpendo's billing is workflow/config-driven rather than a named billing engine in the fetched pages; the comparison table marks it thinnest. This supports treating billing depth as a variant axis, not weakening the L0 (the buyer checklist still includes billing).
7. **Exact numeric limits** (booking-rule counts per licence tier, fund-expiry warning window, approval thresholds) are vendor-specific and stay in these notes only.

## Final Synthesis

A Research Core Facility Management application is the operating system of a shared research facility. Its defining core is three jointly-held structures:

1. the facility's shared instrument/service catalog as the managed, rate-bearing offering (the storefront);
2. identified-user reservations and service requests with per-user, per-group usage attribution (the accountability layer);
3. the usage-to-recharge loop that prices recorded usage at facility rates and bills it to funding sources, with invoices and utilization/revenue reporting (the economic loop).

Around this core, mature products add a standard ring: training/qualification gating, actual-usage capture (kiosks, interlocks, workstation apps), service request workflows with quotes and phases, maintenance and incident management, asset lifecycle records, reporting/analytics, and integrations with institutional identity and finance systems.

The type's neighbors are stable: LIMS (sample-centric), Scientific Instrument Management (asset-centric), Resource Calendar (booking without economics), Research Animal Facility Management (sibling shared-facility type), Research Administration (grant lifecycle). The type is one market with two recognized core shapes (instrument-based self-service cores and service-based cores) and one economic spine (recharge), realized across universities, research institutes, hospitals, and commercial shared labs.
