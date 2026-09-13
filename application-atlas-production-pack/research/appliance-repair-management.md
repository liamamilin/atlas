# Research Notes — Appliance Repair Management

Research date: **2026-09-06**
Methodology: `WORKFLOW_v1.1.md` + `WRITING_GUIDE_v1.1.md` (v1.1)

---

## Research Goal

Understand what "Appliance Repair Management" is as an Application Type: the business-management software used by appliance repair companies. Identify its core objects (customer, repair job, technician, billing), the repair job lifecycle, who operates it, which structures are trade-specific (callbacks, warranty work, parts, flat-rate repair pricing), and where its boundary lies against Small Business Field Service Management, other trade service management leaves, Auto Repair Shop Management, appointment scheduling, and local service marketplaces.

## Initial Boundary

Initial hypothesis (before research):

- Core use: back-office + field-coordination software for appliance repair businesses — book repair jobs against customers and their appliances, schedule and dispatch technicians, track the repair (diagnosis, parts, possible second visit), invoice and collect payment.
- Primary users: owner/operator, office staff/dispatcher, field technicians.
- Nearest types: Small Business Field Service Management (generic sibling under §29), other trade service management leaves (HVAC, Plumbing, Cleaning…), Auto Repair Shop Management (shop-based repair), Appointment Scheduling Application (fragment), Local Service Marketplace (demand side), CMMS/EAM (asset maintenance for asset owners, not service businesses).
- Unknowns: whether the appliance itself is a structured first-class object (equipment registry with make/model/serial) or just job text; how warranty work and parts are modeled; how multi-visit repairs are handled; how deep repair economics (service call fee, flat-rate books) go.

## Research Questions

1. What objects constitute the system (customer, job/work order, technician, invoice) and how do they relate?
2. What is the repair job lifecycle (states, transitions, cancellation semantics)?
3. How are estimates/quotes handled, and how do they convert into jobs?
4. How does scheduling/dispatch work (calendar, drag-drop, assignment, notifications)?
5. What does the technician's mobile surface do (job details, photos, signatures, payments)?
6. How is the repaired appliance captured — structured equipment record vs job text/photos?
7. What repair-specific structures exist: callbacks, warranty-period work, parts/materials, flat-rate pricing books, multi-visit jobs?
8. How does billing work (invoice from job, deposits, payment collection, accounting sync)?
9. What roles and permissions exist (office vs field vs admin)?
10. Where is the boundary against generic field service management and against shop-based repair management?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Tier / philosophy | Why selected |
|---|---|---|
| Housecall Pro | Micro-SMB; customer-experience and payments-first; appliance repair is one served vertical | Best accessible Tier-1 help center; exposes full job model and lifecycle |
| Service Fusion | SMB–mid; all-in-one multi-trade FSM suite with a dedicated appliance-repair vertical page | Confirms the "same suite, trade wrapper" pattern; warranty-period scheduling mention |
| Kickserv | Micro-SMB; simple, low-cost, generic service business | Minimal-core sample; exposes the plain job workflow (columns → completed) |

Market anchors considered but not researchable in this environment (access blocked, recorded as limitation): Jobber (help center + site 403), ServiceTitan (JS-rendered site, API docs 404), Workiz (404), FieldPulse (404). These are major appliance-repair-market products; their exclusion reduces sample breadth, not the validity of the observed core.

## Sources

### Housecall Pro (official help center — Tier 1)

- Help center root (collection inventory): https://help.housecallpro.com/en/
- Jobs, Invoices, and Estimates collection (article inventory): https://help.housecallpro.com/en/collections/74718-jobs-invoices-and-estimates
- How to Create a Job (full article): https://help.housecallpro.com/en/articles/3181752-how-to-create-a-job
- The Job Details page Overview with Progress Invoicing and Appointments: https://help.housecallpro.com/en/articles/1153614-the-job-details-page-overview-with-progress-invoicing-and-appointments
- What's the difference between Unschedule, Cancel, and Delete? (full article): https://help.housecallpro.com/en/articles/2865052-what-s-the-difference-between-unschedule-cancel-and-delete
- Get Started with Job Fields (full article): https://help.housecallpro.com/en/articles/5610489-get-started-with-job-fields
- Referenced collections (inventories only, not individually fetched): Scheduling, Price Book, Service Plans, Invoicing, HCP Payments, Customers, Employees, Reporting, Multi-Day Jobs Appointments, Checklists, Job Inbox, Leads, Pipeline, Customer Portal, Purchase Orders, Franchise.

### Service Fusion (official product pages — Tier 2)

- Root: https://www.servicefusion.com/
- Appliance Repair vertical page (incl. FAQ): https://www.servicefusion.com/appliance-repair-software
- Field Service Management feature page (incl. FAQ): https://www.servicefusion.com/field-service-management-software
- Limitation: merchant help center / support portal not reachable in this environment; operational UI detail inferred from product pages only.

### Kickserv (official knowledge center — Tier 1)

- Knowledge center root (category inventory): https://kickserv.helpscoutdocs.com/
- Kickserv Basics category (article inventory): https://kickserv.helpscoutdocs.com/category/14-the-basics
- Jobs (full article): https://kickserv.helpscoutdocs.com/article/32-jobs
- Referenced titles (not individually fetched): Customers and Contacts, Invoices, Estimates, Reminders, Reports, Opportunities, Settings.

### Blocked sources (limitation record)

- Jobber: https://help.getjobber.com/hc/en-us → 403; https://www.getjobber.com/features/ → 403 (2 failures; abandoned).
- ServiceTitan: https://developer.servicetitan.io/ → JS-rendered empty; https://developer.servicetitan.io/api/ → 404 (abandoned).
- Workiz: https://www.workiz.com/industries/appliance-repair-software/ → 404; https://www.workiz.com/appliance-repair-software/ → 404 (abandoned).
- FieldPulse: https://fieldpulse.com/appliance-repair-software → 404; https://fieldpulse.com/industries/appliance-repair → 404 (abandoned).
- Housecall Pro marketing site: https://www.housecallpro.com/appliance-repair-software/ → 403 (help center used instead).

---

## Product A — Housecall Pro

### Key observations (evidence layer A — directly observed)

- **Object model**: Customer profile (name, service address, phone, email, notification preferences) → Job (customer, service address, schedule, dispatch, line items, notes, checklists, tags, job fields, lead source, attachments, deposit) → Invoice; Estimates as a parallel object convertible into jobs. Job Details page is organized into customer, job, invoice, dispatch, payments, and schedule sections.
- **Job creation flow (web + mobile)**: Create → Job → New Job page: search/select existing customer or create new; set service address; schedule; dispatch an employee; add line items from the Price Book (services and materials) or custom line items; add notes, checklists, job fields, tags, lead sources, attachments; save. Job templates can pre-populate job information. If entering the Schedule page during creation, a team member must be assigned and dispatched before saving.
- **Job lifecycle states**: three distinct actions with different semantics — **Unschedule** (removed from calendar, stays in customer's Jobs tab, status "Unscheduled", no customer notification, appears in mobile "Needs Attention"; not available for jobs that include appointments), **Cancel** (customer receives text + email notification; stays in records with status "Canceled"), **Delete** (removed from customer profile, restorable; no notifications). Jobs can also be restored after deletion.
- **Multi-visit structure**: an "Appointments" feature stores date/time details on a job (progress invoicing + appointments); a job with appointments cannot be unscheduled — appointments must be deleted first. Separate "Multi-Day Jobs Appointments" collection exists. "Job Splits" article exists (splitting jobs). Multiple appointments per job = the multi-visit repair pattern.
- **Repair-specific field**: the **Callback** job field — "if a previously scheduled job resulted in a callback, this field can be used to capture which jobs are callbacks." Callbacks are filterable/reportable. This is direct evidence that rework-on-repair tracking is a first-class concept in this market.
- **Job fields & permissions**: Job type, Business unit, Callback available by default; values editable only by Admins and Office staff with "update company info" permission; fields usable as report filters and drill-down columns.
- **Estimates**: multi-option estimates, approvals and e-signatures, expiration dates, deposits on estimates, conversion of estimates to jobs (manual or automated from approved estimates), estimate templates.
- **Invoicing/payments**: auto-invoicing, invoice reminders, batch invoicing, progress invoicing, invoice email/SMS, customer invoice history; HCP Payments collection (71 articles); deposits; discounts; automated sales tax.
- **Pricing**: Price Book collection (services + materials, 23 articles); "Job Inputs and Flat Rate Services" article — flat-rate pricing exists as a first-class concept.
- **Recurring work**: recurring jobs; Service Plans collection ("Maintenance Plans, Planned Maintenance Programs, Care Clubs and Membership Plans", 22 articles); property profile items can be attached to service plans (equipment-like linkage exists at the service-plan level).
- **Other surfaces**: Company Dashboard, Job Inbox (leads/opportunities), Pipeline, Customer Portal (self-service), Marketing Center, Reporting (custom reports, drill-down), QuickBooks Online/Desktop sync, Google Calendar, app store, fleet tracking (partnered), payroll, franchise support.
- **No structured appliance/equipment registry observed** in the help-center inventory: the appliance is captured via job text, line items, photos/videos ("Document your work" collection: annotated photos and video uploads; "Photo Report on Jobs"), and optionally property-profile items attached to service plans. No "Equipment" or "Appliance" collection exists.

## Product B — Service Fusion

### Key observations (evidence layer A for positioning/FAQ; UI detail not directly observed)

- **Positioning**: "Appliance Repair Software" is the same all-in-one FSM suite marketed per trade; the site ships ~30 identical industry pages (HVAC, plumbing, electrical, appliance repair, locksmith, pool, cleaning…). The appliance FAQ defines the category: "Appliance repair business software may include any combination of customer management, fleet tracking, estimate creation, invoice management, and payment processing tools designed for the field service industry… sold as a subscription-based software offering."
- **Trade-specific statement (appliance)**: "FSM software is crucial for appliance repair companies in scheduling service visits, particularly during warranty periods." Also: technicians take and save photos before and after appliance repair work. This is direct vendor evidence that warranty-period scheduling and before/after photo documentation are part of the appliance-repair usage pattern.
- **Core feature spine (all trades)**: scheduling & dispatch (drag-and-drop, job info to field via text/call, real-time notifications, on-the-way alerts), estimates (up to five options, one-click convert to jobs, eSign within estimates), customer management (multiple contacts, multiple service locations, communication preferences, referral sources, service history), technician mobile app (receive dispatched jobs, map/directions, accept payments with card reader, job photos, notes, pre/post-work signatures, create/send invoices, take payment), invoicing & payments (auto-generate invoices from completed jobs; materials, labor, taxes, discounts; online + field payments; QuickBooks sync), GPS fleet tracking, VoIP call tracking (call reasons/outcomes, recording), flat-rate integration, homeowner financing, online booking portal, automated pre-job text notifications.
- **Workflow (vendor's own "How it works")**: 1) Create & assign jobs (work orders in one click, drag-drop schedule, assign technicians) → 2) Dispatch & send reminders (techs view job details, navigate, capture payments; customer reminders on the day of the work order) → 3) Track status (locations and status of all technicians, in-app communication).
- **Business model**: subscription, no per-user fees; three pricing plans; QuickBooks Solution Provider.
- **No structured appliance/equipment registry claimed** on the appliance page; parts inventory appears only in the HVAC usage example ("manage parts inventory"). Warranty appears only as scheduling context. Equipment-record depth unverified.

## Product C — Kickserv

### Key observations (evidence layer A — directly observed)

- **Object model**: Customers and Contacts → Jobs ("the heart of the Kickserv workflow… what your technicians are completing out in the field") → Invoices; Estimates and Opportunities feed jobs ("Many Jobs start out as an Opportunity that turns into an estimate. Once the estimate is approved by the customer, the Opportunity transforms into an unscheduled Job").
- **Job record**: service type, internal job description (not customer-visible), external scope of work (customer-visible), saved contact, custom data fields (Settings → Forms & Fields → Jobs).
- **Job lifecycle (Jobs page columns, left to right)**: **Unscheduled → In Progress → Completed**, with optional **On Hold** between In Progress and Completed ("Jobs can skip the On Hold column"). Actions: Start Job, Stop Job, On Hold / Remove On Hold, Mark Complete (with confirmation to mark all work events complete).
- **Multi-visit structure**: scheduling creates **work events** (date/time, description for technicians, task type, assigned tech); "Depending on your industry, you might need to schedule several work events on a single job… keep the job open until all work events are completed, then send a final invoice." Direct evidence of multi-visit jobs as a structural pattern.
- **Recurring jobs**: repeat a scheduled job by frequency/date/day-of-week with an end condition.
- **Filters**: jobs filterable by service type, status, tag, assigned technician, time.
- **Other surfaces**: Reminders (automated customer messaging), Estimates (signature approval), Invoices (receivables, online payments via Stripe/Apple/Google Pay), Customer Center (customer self-service), mobile app (schedule, GPS & time tracking, digital signatures, onsite card payment), QuickBooks 2-way sync, Reports, Opportunities pipeline.
- **No structured appliance/equipment registry observed** in the knowledge center inventory.

---

## Cross-product Comparison

| Structure | Housecall Pro | Service Fusion | Kickserv | Assessment |
|---|---|---|---|---|
| Customer record w/ service location + history | Customer profile, service addresses, notification prefs | Multiple contacts, multiple service locations, referral sources, service history | Customers and Contacts, saved contacts | Core (all 3) |
| Repair job / work order as unit of work | Job (rich: line items, fields, checklists, attachments, deposits) | Work order/job ("created in a single click") | Job ("the heart of the workflow") | Core (all 3) |
| Technician assignment/dispatch | Dispatch employee; required if scheduling during creation | Drag-drop assign; dispatch; status tracking | Assign tech to work event; unassigned allowed | Core (all 3) |
| Job lifecycle states | Unscheduled / Canceled / Deleted(+restore); appointments variant | Create → dispatch → track status; job statuses | Unscheduled → In Progress → (On Hold) → Completed | Core (all 3; labels vary) |
| Estimate → job conversion | Estimates (multi-option, eSign, auto-convert) | Estimates (up to 5 options, one-click convert) | Opportunity → Estimate → approved → Job | Core (all 3) |
| Scheduling calendar | Schedule page; arrival windows; appointments | Drag-drop calendar; reminders | Calendar of work events | Core (all 3) |
| Technician mobile app | Create jobs, photos/videos, signatures | Dispatched jobs, maps, payments, photos, notes, signatures, invoices | Schedule, GPS/time tracking, signatures, onsite payments | Core (all 3) |
| Invoice from job + payment collection | Auto-invoicing, progress invoicing, batch, reminders; HCP Payments | Auto-generate invoices from completed jobs; field + online payments | Invoices; online payments; receivables | Core (all 3) |
| Price book / service catalog | Price Book (services + materials); flat-rate services | Pre-populated service line items; flat-rate integration | Service types; custom templates | Common |
| Customer notifications | Texts/emails (job, invoice, cancel) | Pre-job texts, day-of reminders, on-my-way alerts | Reminders, job notifications | Common |
| Multi-visit jobs | Appointments on jobs; job splits; multi-day jobs | (implied by job statuses; not explicit) | Multiple work events per job (explicit) | Common |
| Callback tracking | Callback job field (explicit) | — (not observed) | — (not observed) | Product-specific in sample; repair-trade relevant |
| Warranty-period work | — (not observed) | Explicit (scheduling "particularly during warranty periods") | — (not observed) | Product-specific in sample |
| Before/after photos | Photo report; document-your-work collection | Explicit (pre/post-work photos) | Photos, documents, notes on jobs | Common |
| Recurring jobs / service plans | Recurring jobs; Service Plans | Service agreements (eSign) | Recurring jobs | Common |
| Accounting sync | QuickBooks Online/Desktop | QuickBooks (bi-directional) | QuickBooks 2-way sync | Common |
| GPS fleet tracking | Partnered fleet tracking | Built-in GPS fleet tracking | GPS in mobile app | Optional |
| VoIP / call tracking | Voice collection | ServiceCall.ai | — | Optional |
| Online booking portal | Customer Portal; web booking (Service Fusion) | Customer web booking portal | Customer Center | Optional |
| Financing | — (not observed) | Homeowner financing | — | Optional |
| Structured appliance/equipment registry | Not observed (property-profile items only) | Not claimed on appliance page | Not observed | **Not universal — see finding below** |
| Parts/materials inventory | Material line items; material inventory detail tracking; purchase orders | Mentioned in HVAC example only | — | Optional |
| Lead capture / marketing | Job Inbox, Leads, Pipeline, Marketing Center | Call tracking, referral sources | Opportunities | Optional |
| Payroll / commissions | Payroll; commissions on jobs | — | — | Optional |
| Franchise / multi-location | Franchise collection | — | — | Optional |

### Key finding — the appliance is usually not a structured registry object

In all three researched products, the repaired appliance is captured as **job content** (description, line items, photos, notes, custom fields), not as a first-class structured equipment/appliance record with make/model/serial. Housecall Pro's closest structure is "Property Profile" items attachable to service plans; Kickserv has none; Service Fusion does not claim one on its appliance page. Structured equipment registries exist in the broader field-service market (and in enterprise FSM), but in this sample they are not the defining structure of the Type. The canonical concept is therefore "the repair job carries what was repaired," with the equipment registry as an optional/variant structure.

### Key finding — the trade overlay is semantic, not structural

All three products are multi-trade or trade-agnostic FSM platforms; the appliance-repair edition differs by: repair semantics (diagnose → repair → possibly callback), warranty-period scheduling context, before/after photo documentation, flat-rate repair pricing, parts as line items, and service-call economics. The structural spine (customer → job → schedule/dispatch → technician → invoice → payment) is identical to generic field service management.

---

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

The smallest structure without which the software stops being an appliance repair management application:

```text
Customer (with a service location)
└── Repair job / work order — a requested repair of an appliance
    │   at that location, carried as a record with a lifecycle
    │   (requested → scheduled → assigned → performed → completed → billed)
    └── Technician as the executing role (assignment/dispatch)
        └── Billing of the completed repair (invoice → payment)
```

Four properties:

1. **Customer with service location** — the repair is performed where the appliance sits (home or business), so the job binds to a place, not a shop bay.
2. **Repair job as the unit of work** — a durable record of one repair engagement with a lifecycle that survives between booking and billing.
3. **Technician execution** — the work is performed by an assigned field technician; the system coordinates office ↔ field.
4. **Billing of the repair** — the completed job produces an invoice and a payment record.

Remove the repair-job lifecycle → generic contact/invoicing software. Remove the technician/field coordination → pure invoicing. Remove billing → dispatch log only. Remove the customer/location binding → internal task tracker. In each case the Type is no longer recognizable.

### L1 — Common Mature Structure

Present in essentially all mature modern products, but not required to recognize the Type:

- estimate/quote object with approval and conversion into a job
- scheduling calendar + dispatch board (drag-drop, assignment, status columns)
- technician mobile app (job details, navigation, photos, notes, signatures, payment capture)
- invoicing generated from the job; card/online payment collection; accounting (QuickBooks) sync
- price book / service catalog (services + materials; flat-rate pricing entries)
- automated customer notifications (booking confirmation, reminders, on-my-way, invoice links)
- job status board with lifecycle columns/states; cancel/hold/delete semantics
- multi-visit jobs (appointments / work events on one job)
- before/after photo documentation of the repair
- recurring jobs / service or maintenance plans
- reporting (job lists, revenue, technician performance)
- callbacks (return visits for failed/incomplete repairs) — repair-trade semantics, explicit in one sampled product, conceptually general to repair trades

### L2 — Variant / Optional Structure

Depends on segment, scale, region, business model:

- structured appliance/equipment registry (make/model/serial per customer location)
- parts/materials inventory management and purchase orders
- warranty-claim processing against manufacturers (warranty-period scheduling is evidenced; full claim workflows unverified in sample)
- GPS fleet tracking; VoIP/call tracking; AI phone answering
- customer self-service booking portal / customer portal
- homeowner financing; membership plans; lead capture/marketing modules
- payroll, commissions, job costing depth
- franchise/multi-location; multi-business-unit reporting
- commercial vs residential specialization (e.g., commercial food equipment service)

### L3 — Vendor-specific Structure

(Research Notes only)

- Housecall Pro: HCP Assist (AI), HCP Money, HCP Payroll, Alexa skill, Emitrr integration, Superpro, "Needs Attention" mobile section, industry packages (HVAC/electrical/plumbing).
- Service Fusion: ServiceCall.ai, Acorn homeowner financing, Service Nation, Notes+ (AI note cleanup), Stripe M2 reader bundle, no-per-user-fee pricing model, ~30 clone industry pages.
- Kickserv: "Norman" mascot/branding, Customer Lobby integration, Start/Run/Scale plan names, HelpScout-based knowledge center.

---

## Historical / Market-Sample Check (§24)

Question: would older, regional, or differently positioned appliance repair operations still fit the L0?

- **Pre-software practice**: paper job tickets/ticket books (customer, address, appliance, complaint), whiteboard or wall-card scheduling, phone dispatch, handwritten invoice. This satisfies the L0 exactly: the ticket is the repair job record with a lifecycle; the whiteboard is the schedule; the technician assignment is dispatch; the invoice is billing. The L0 does not depend on cloud, mobile apps, GPS, or SMS.
- **Regional**: appliance repair is a global trade (residential and commercial); nothing in the L0 is US-specific (no warranty-program regimes, no tax rules, no phone-number identity).
- **Platform-native / differently positioned**: a one-van owner-operator using only a calendar + invoicing tool satisfies the L0 without a dispatch board (assignment collapses to self-assignment); a warranty-authorized factory service agent satisfies it with warranty semantics as L2 overlay.
- Conclusion: the L0 survives the historical check. Modern implementations (cloud sync, mobile apps, notifications, GPS, payments rails) are L1/L2, not definition.

---

## Vendor-specific Findings

See L3 above. Additionally:

- Housecall Pro's appliance-repair service is delivered through its generic core (no appliance-specific package observed; its "Industry Packages" collection covers HVAC, Electrical, Plumbing — not appliance repair).
- Service Fusion's appliance page is a re-skinned clone of its FSM page with appliance-specific FAQ entries — strong evidence that vendors treat this Type as a trade wrapper around one FSM product.
- Kickserv's docs are trade-agnostic entirely; appliance repair is one of many served trades.

## Boundary Findings

1. **vs Small Business Field Service Management (sibling §29)**: the researched sample shows the same L0 spine (customer → job → schedule/dispatch → technician → invoice → payment) in both. The difference is trade semantics: repair-oriented jobs (diagnosis, callbacks, warranty-period work, parts, flat-rate repair pricing, before/after documentation) vs generic service jobs. Structural test: remove the repair semantics → generic FSM remains; remove nothing structural → appliance repair management remains. Probable trade-Variant relationship rather than two independent Types — flagged for joint review when Small Business Field Service Management is processed.
2. **vs other trade service management leaves (HVAC, Plumbing, Cleaning, etc., §29)**: same relationship — trade variants of one FSM family. Vendors themselves ship one product with many industry pages (Service Fusion ships ~30).
3. **vs Auto Repair Shop Management (sibling §29)**: both are "repair management," but the execution surface differs — auto repair is shop-based (vehicle brought to bays; work order lives at the shop), appliance repair is field-based (technician travels to the appliance's location). Dispatch/routing is central here, bay/vehicle-lift logistics there.
4. **vs Appointment Scheduling Application (§03.09)**: scheduling is one module inside this Type; the Type is the whole business operation (customers, jobs, technicians, billing), not a booking surface.
5. **vs Local Service Marketplace (§29)**: demand-side discovery/booking vs operator-side business management. A marketplace may hand off a lead that becomes a job in this system.
6. **vs CMMS / EAM (§16)**: CMMS/EAM manages assets owned by the organization running the software; this Type manages a service business whose "objects of work" are customers' appliances. Different population, different economics.
7. **vs Job Board / Lead Generation**: lead capture exists as an optional module (Job Inbox, Opportunities); the Type's center is job execution and billing, not demand generation.

## Uncertainties

- **Equipment registry depth**: structured appliance/equipment records (make/model/serial, service history per unit) are common in the broader FSM market and in enterprise FSM, but were not observed in this sample's documentation. Kept out of the defining core; recorded as optional/variant.
- **Warranty-claim workflows**: warranty-period scheduling is directly evidenced (Service Fusion); full manufacturer warranty-claim processing (claim submission, authorization numbers, reimbursement tracking) was not verifiable in this sample. Kept as unverified optional structure.
- **Parts inventory depth**: materials as line items are evidenced (Housecall Pro); full parts inventory/purchasing is common in the market but only partially evidenced here.
- **Enterprise tier**: ServiceTitan (the enterprise anchor for appliance repair) was not researchable; enterprise-specific structures (price-book governance, membership programs, asset management, reporting depth) are unverified.
- **Job status label variance**: lifecycle labels differ per product (Unscheduled/In Progress/Completed vs statuses vs columns); canonical states are conceptual, exact labels vary.

## Final Synthesis

Appliance Repair Management is the business-management application of an appliance repair operation. Its defining core is small: a customer with a service location, a repair job as the durable unit of work with a lifecycle from request to billing, a technician as the executing role coordinated by the office, and billing of the completed repair. Around this core, mature products add the standard field-service machinery: estimates, scheduling/dispatch boards, technician mobile apps, invoicing and payments, price books, notifications, multi-visit handling, photo documentation, recurring maintenance, and reporting. The appliance itself is normally captured as job content (description, photos, parts line items) rather than a structured registry; equipment registries, parts inventory, warranty-claim processing, GPS, financing, and marketing modules are optional/variant structures. The Type is best understood as the appliance-repair trade variant of field service management: structurally identical to generic FSM, differentiated by repair semantics (callbacks, warranty work, flat-rate repair pricing, parts) and by the fact that the work happens at the customer's location on the customer's appliance.
