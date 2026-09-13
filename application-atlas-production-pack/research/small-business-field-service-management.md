# Research Notes — Small Business Field Service Management

Research date: 2026-09-09
Leaf: Small Business Field Service Management (DIRECTORY.md §29 Home, Family, Personal & Local Services — trade-business cluster)
Slug: small-business-field-service-management

## Research Goal

Understand what generic "Small Business Field Service Management" software actually is: the trade-agnostic spine that the §29 trade-business cluster configures. This leaf is the family anchor — eleven processed sibling passes (appliance-repair, cleaning, electrical, garage-door, handyman, HVAC, landscaping, lawn-care, locksmith, plumbing, plus structural siblings flooring/roofing/home-improvement/restoration/fire-protection) pre-hung joint-review flags expecting this pass to (a) define the generic spine and (b) ratify the trade-Variant family structure. The pass must also draw seams against Dispatch Management, Aftermarket Service Management, CRM, scheduling applications, marketplaces, CMMS/EAM, and the §19 utility/telecom field-service leaves.

## Initial Boundary

Working hypothesis at start (informed by the sibling passes):

- It is the operator-side business system of a small field/service business: customer + service location records, a job/work-order lifecycle, office→field technician coordination, and billing of completed work.
- The "small business" scope is a market-positioning statement (SMB/home-services segment), not a structural one — the spine is expected to hold at any scale; what changes at enterprise scale is the anchoring (installed base, entitlements, governance), which belongs to Aftermarket Service Management territory.
- Closest neighbors: the §29 trade siblings (same spine, trade semantics), Dispatch Management (one stage of the spine), Aftermarket Service Management (asset-centric superset), CRM (relationship-centric), Appointment Scheduling (booking fragment), Local/Home Services Marketplace (demand side), CMMS/EAM (owned assets), Utility/Telecom Field Service (§19, different operator).

## Research Questions

1. What is the minimal object world (customer, service location, job, technician, schedule, invoice, payment) and what binds them?
2. How does work flow from request to payment? What are the job's states and transitions?
3. What capabilities are standard in mature SMB products vs optional vs vendor-specific?
4. What do vendors themselves say the category is (vendor-articulated definitions)?
5. Where does the "small business" scope show up in positioning and structure?
6. Does the generic spine hold without any trade layer (the trade-agnostic pole)?
7. Ratification: are the trade siblings trade-Variants of this Type, and which siblings are structurally distinct instead?
8. Historical check: would paper-era, regional, or platform-native service operations still fit a minimal definition?

## Representative Products

Selected for market representation + documentation access + different product philosophies + different customer layers. All four are trade-agnostic platforms serving 50+ industries — exactly the pole this leaf must define:

| Product | Segment / philosophy | Evidence tier |
|---|---|---|
| Kickserv | micro-SMB; simple job-based service business management; the purest trade-agnostic pole | Tier 1 (Knowledge Center: Jobs, Customers and Contacts, Estimates articles) |
| Housecall Pro | micro-SMB residential home services; customer-communication/payments-first; help center documents industry packages only for HVAC/Electrical/Plumbing — everything else runs the generic platform | Tier 1 (Help Center: collection map, How to Create a Job, Unschedule/Cancel/Delete) |
| FieldPulse | growing SMB contractors; workflow-configuration philosophy; self-labels "Field Service Management Software"; G2 "Small Business Leader" badge | Tier 2 (site, Work Order Management feature page, FAQ) |
| Workiz | SMB home services; communication/dispatch-and-AI-first ("AI growth engine"); 50+ industries | Tier 2 (site, Job Scheduling feature page; help center unreachable) |

Attempted and abandoned per source-access rules: **Jobber** — the largest trade-agnostic SMB brand — help.getjobber.com 403 this pass; cumulative 403 ×4 across the electrical (×2), handyman (×1), and this pass. Workiz help center (help.workiz.com) timed out ×2 — Workiz held at Tier 2. ServiceTitan and Service Fusion were not re-fetched this pass; their generic-platform observations are carried from the garage-door and electrical passes as cross-pass evidence (Layer B).

## Sources

Fetched 2026-09-09:

- Kickserv (Tier 1): https://kickserv.helpscoutdocs.com/ (Knowledge Center map); /article/32-jobs (Jobs); /article/36-customers-and-contacts (Customers and Contacts); /article/31-estimates (Estimates); /category/14-the-basics (Kickserv Basics object map)
- Housecall Pro (Tier 1): https://help.housecallpro.com/en/ (collection map); /en/collections/74718-jobs-invoices-and-estimates (Jobs, Invoices, and Estimates collection); /en/articles/3181752-how-to-create-a-job; /en/articles/2865052-what-s-the-difference-between-unschedule-cancel-and-delete
- FieldPulse (Tier 2): https://www.fieldpulse.com/ (platform map + category self-label); /features/work-order-management; /resources/faq (vendor-articulated category definition)
- Workiz (Tier 2): https://www.workiz.com/ (product page, growth-engine loop, 50+ industries); /features/job-scheduling/

Cross-pass evidence (Layer B, documented in sibling research files): ServiceTitan trade pages + Dock & Door page (research/garage-door-service-management.md); Service Fusion ~29 clone industry pages (same file); Housecall Pro industry-package scope (plumbing/garage-door passes); Kickserv trade-agnostic pole (cleaning/landscaping/lawn-care passes).

## Product A — Kickserv

### Key observations (evidence layer A, Tier 1)

- **Jobs are the center**: "Jobs are the heart of the Kickserv workflow. Jobs are what your technicians are completing out in the field and the main way you'll keep track of business activity."
- **Job board**: left-to-right workflow Unscheduled → In Progress → Completed, with optional On Hold column ("Jobs can skip the On Hold column").
- **Job creation**: service type, internal job description ("will not be seen by the customer"), external scope of work ("will be seen by the customer"), contact drawn from customer records; custom data fields on jobs (Standard plans and above).
- **Conversion path**: "Many Jobs start out as an Opportunity that turns into an estimate. Once the estimate is approved by the customer, the Opportunity transforms into an unscheduled Job!"
- **Scheduling**: inside the job, "Schedule work" → date/time, description for technicians, task type, assign tech (or leave unassigned) → "Add Event" — a work event is a child of the job.
- **Execution states**: Start/Stop Job buttons move the job to In Progress; Mark Complete pops a confirmation to mark all work events complete.
- **Multi-visit**: "Depending on your industry, you might need to schedule several work events on a single job… keep the job open until all work events are completed, then send a final invoice."
- **Recurring jobs**: "Repeat this job" → frequency, day/date, end condition → repeating jobs added to the schedule.
- **Job filters**: service type, status, tag, assigned technician, time.
- **Endpoint**: "Congratulations! You've gone through the complete Jobs workflow. Now, it's time to send an invoice to your customers and get paid."
- **Customers and contacts**: contact can be person or company; name, phone, email; text-message opt-in; service address + billing address; a contact can be flagged "treated as a service location."
- **Service locations**: multiple locations per customer — a child record with a unique company name, linked to the main customer (parent); address geocoded to Google Maps "to ensure it is synced… and will work with GPS tracking"; billing can go to the parent, the service address, or a new address.
- **Customer Center**: customer self-service — request service, work history, approve estimates, pay invoices; link expires for security.
- **Work History**: all of a customer's jobs past and future, with details incl. address/contact, estimate, receipt, charges, notes, attachments.
- **Estimates**: "Estimates are Opportunities that have been scheduled or sent out"; Opportunity workflow New → Estimate Scheduled → Estimate Sent → Estimate Viewed → (approved → unscheduled Job) / Lost; two estimate paths (schedule a live-quote visit vs send a priced estimate); charge items with description/price/quantity/taxable/Job Charge Type; Detailed vs Summary document views; online payments, live signature, PDF; customer can request modification or approve; Stripe integration sends the estimate as a text too.
- **Object map** (Kickserv Basics): Settings, Customers and Contacts, Invoices, Jobs, Reminders, Estimates, Reports, Opportunities.
- Trade-agnostic throughout: nothing trade-specific anywhere in the fetched articles.

## Product B — Housecall Pro

### Key observations (evidence layer A, Tier 1)

- **Collection map** (whole-product structure): Account Settings, AI Team, App Store, Billing, Business Coaching, Checklists ("must be completed by employees before they can mark a job as finished"), Company Dashboard ("The main view into your business"), Customers, Customer Portal ("self-serve information on your history with them"), Employees ("Adding, managing, removing, or assigning jobs to an employee"), Franchise, Fleet Management, Getting Started, Google Calendar, Accounting, HCP Assist (AI), Document your work (annotated photos/video), HCP Money, HCP Payments (71 articles), Import & Export, **Industry Packages ("industry-specific Housecall Pro packages for HVAC, Electrical, and Plumbing Pros" — 4 articles only)**, Invoicing, Job Inbox ("Get jobs, leads, and opportunities delivered right to your Housecall Pro inbox"), Jobs/Invoices/Estimates (62 articles), Leads ("capture prospects, follow up easily, and convert opportunities into booked jobs"), Marketing Center, Mobile-Only Features, Multi-Day Jobs Appointments, Notifications, Payroll, Pipeline, Price Book (23 articles), Property Profile, QuickBooks Desktop/Online, Reporting, Sales Proposals, Scheduling, Service Plans ("Maintenance Plans, Planned Maintenance Programs, Care Clubs and Membership Plans"), Tasks, Tech Support Tips, Twilio 10DLC, Voice, Purchase Orders, Voice of the Customer.
- **Job creation** (How to Create a Job): New Job page — customer information, service line items, assign team members, notes/files, schedule; options: schedule, **dispatch an employee**, job template, line items, notes, checklists, job fields, tags, lead sources, attachments; after saving: add segments, deposit, edits to customer/job/invoice/dispatch/payments/schedule. If entering the Schedule page during creation, "you will be required to assign and dispatch a team member before saving."
- **Customer on the job**: adding a customer pulls name, service address, phone, email, notification preferences onto the job page; search by name/email/phone/address; inline new-customer creation; service address editable per job.
- **Line items**: type to search the Price Book; custom line items per invoice; edit within the invoice "will not change the item in your main price list."
- **Job states** (Unschedule/Cancel/Delete): Unschedule = removed from calendar, stays in Jobs tab, status "Unscheduled", no customer notification, appears in "Needs Attention" in the mobile app; Cancel = customer notified (text + email), removed from calendar, stays in records, status "Canceled"; Delete = removed from the customer profile (restorable), no notification; estimates deleted show "Pro canceled". Appointments: "a job created while Appointments are enabled can't be unscheduled" — appointments store date/time details.
- **Estimates collection**: deposits on estimates, send/create estimate, templates, multi-option estimates (web & mobile), approvals and signatures, copy or convert jobs and estimates, e-signatures, estimates on jobs, default expiration dates; "Automate Job Creation from Approved Estimates".
- **Jobs collection extras**: job inputs and flat-rate services, line items, commissions tracking, material inventory detail tracking, job costing, custom job signatures, photo reports, automated sales tax, job splits, tasks on jobs, progress invoicing, arrival windows, notes (customers/jobs/addresses), private notes, job fields, discounts, job templates, batch invoicing, invoice reminders vs auto invoicing, invoice email & SMS, recurring jobs, job segments (multi-segment jobs / multi-option estimates).
- The generic platform serves all trades; only three trades get packaged layers (HVAC/Electrical/Plumbing) — the trade-agnostic pole demonstrated from the vendor's own help center.

## Product C — FieldPulse

### Key observations (evidence layer A, Tier 2)

- **Category self-label**: homepage H1 "Field Service Management Software"; FAQ: "FieldPulse is a business management software for service businesses who need to better manage their customer data, schedule jobs for employees, create invoices and estimates, track payments, and have better insight into their business operations… This is also known as a Field Service Management application."
- **Platform map**: Scheduling & Dispatching, Work Order Management, Job Management, Estimates & Invoices, Mobile App, Project Management, Dashboards & Reporting, Custom Workflows, Inventory Management, Asset Management, Customer Communication, Customer Management, Customer Portal, Booking Portal, Maintenance Agreements; products: Operator AI (24/7 AI dispatching), ClearPath (guided job-stage workflows), Custom Forms, Pricebook, Engage (VoIP), Fleet Tracking.
- **Work order anatomy** (feature page): create screen with customer, work order title, assigned team members, tags, and **status workflow**; custom work order templates; instant assignments "with instant notifications sent directly to their mobile devices"; drag-and-drop scheduling with team views; live GPS tracking; real-time status monitoring; customer updates (progress, technician arrival times, completion); custom workflows with **task dependencies** ("make sure one phase of the job is completed before the next begins"); automated job updates triggering task hand-offs; reporting (custom dashboards, reports by service type/location).
- **Customer model** (FAQ): profiles store basic info (name, company, email, phone, address, notes) plus job records, invoice records, comments, invoice PDFs, photos, files — "the entire customer history"; "Customer profiles can also have related customers and locations."
- **Permissions** (FAQ): "I don't want certain employees to see certain financial/invoicing/billing information, can I control that?" — financial-visibility permissions exist.
- **Owner-operator pole** (FAQ): "I don't have any other employees. Will I benefit from using FieldPulse?"
- **SMB positioning**: G2 "Small Business Leader" badge; FAQ "Is work order software good for small businesses?"; comparison pages vs ServiceTitan, Jobber, FieldEdge, Service Fusion, Housecall Pro (the competitive set of this exact market).
- **Industry list**: HVAC, Electrical, Plumbing, Garage Door, Locksmith, Property Management, Appliance Repair, Commercial Equipment, Fire and Security, Contractors, Septic, A/V Installation, Glass — trades as solution pages over one platform.

## Product D — Workiz

### Key observations (evidence layer A, Tier 2)

- **Positioning**: "AI growth engine for home service businesses. Your team handles the work. Workiz handles the calls, fills the board, sends the invoices, and collects the payments." "Trusted by 120K+ home service pros in US and Canada." "Proud partner to home services in over 50 industries."
- **Growth-engine loop** (vendor's own articulation of the spine): Lead Capture (AI answers every call) → Book jobs (turn inquiries into scheduled jobs) → Dispatch ("The right tech on every job") → Sell (quote good-better-best on-site) → Collect payment ("Get paid on the spot") → Remarket (win repeat work).
- **Feature list**: Scheduling, Invoicing, Communication suite (embedded phone), Online payment, Inventory management, Lead management, Business reporting, Route planning, Service plans, Estimates, Pricebook, QuickBooks, Mobile app, Automations ("when this happens, do that" rules).
- **Scheduling** (feature page): drag-and-drop calendar with each tech's route; rearrange appointments to minimize windshield time; Genius scheduling (AI finds best time from techs' availability and skill sets); message clients from the calendar slot; emergency handling — dispatcher sees which tech is nearby and alerts about last-minute changes; automations notify pre-scheduled clients of delays.
- **Scheduling FAQ**: create jobs (customer information, job description, required resources); assign technicians "based on skills, location, and availability"; recurring tasks; real-time updates on job progress, technician location, schedule changes; mobile app (iOS/Android); calendar sync; automated customer notifications (confirmations, reminders, real-time updates via SMS and email).
- **Industries**: HVAC, Plumbing, Electrical, Locksmith, Appliance Repair, Garage Doors + "See all industries" — trades as industry pages over one platform.
- Help center (help.workiz.com) unreachable (timeout ×2) — operational detail held at Tier 2 strength.

## Cross-product Comparison

| Structure / capability | Kickserv | Housecall Pro | FieldPulse | Workiz | Assessment |
|---|---|---|---|---|---|
| Customer record with contact + billing address | ✓ (Customers & Contacts) | ✓ (Customers; pulled onto job) | ✓ (Customer Management; profiles with history) | ✓ (customer information on jobs) | Universal — core |
| Service location as a managed record | ✓ (service locations, child of parent, geocoded) | ✓ (service address per job; Property Profile) | ✓ ("related customers and locations"; Customer Sites Management) | ✓ (address-bound jobs; routes) | Universal — core |
| Job / work order as the unit of work with lifecycle | ✓ ("heart of the workflow"; board) | ✓ (Jobs; unschedule/cancel/delete states) | ✓ (work orders with status workflows) | ✓ (create/assign/manage jobs) | Universal — core |
| Office→field technician coordination (schedule/dispatch) | ✓ (assign tech; work events) | ✓ (dispatch an employee; scheduling) | ✓ (drag-drop dispatch board; GPS; mobile notifications) | ✓ (dispatch; skills/location/availability) | Universal — core |
| Invoice + payment collection on completed work | ✓ ("send an invoice… and get paid") | ✓ (Invoicing + HCP Payments, 71 articles) | ✓ (Estimates & Invoices; FieldPulse Payments) | ✓ (Invoicing; online payments; "collects the payments") | Universal — core |
| Estimate/quote → approval → job conversion | ✓ (Opportunity→Estimate→Job) | ✓ (estimates; automate job creation from approved estimates) | ✓ (estimates→invoices; Good/Better/Best) | ✓ (Estimates; good-better-best on-site) | Universal — standard |
| Price book / line-item pricing | ✓ (charge items; service types) | ✓ (Price Book, 23 articles) | ✓ (Pricebook product) | ✓ (Pricebook) | Universal — standard |
| Technician mobile app | ✓ (Mobile App collection; Technicians category) | ✓ (Mobile-Only Features; mobile job creation) | ✓ (Mobile App; instant assignment notifications) | ✓ (iOS/Android app) | Universal — standard |
| Customer notifications | ✓ (Reminders) | ✓ (Notifications collection; invoice email & SMS) | ✓ (customer updates; arrival times) | ✓ (automated confirmations/reminders via SMS/email) | Universal — standard |
| Multi-visit jobs / work events | ✓ (explicit: several work events per job) | ✓ (Multi-Day Jobs Appointments; job segments) | ✓ (task dependencies; phases) | — (not observed at fetched depth) | Common — standard |
| Recurring jobs | ✓ (Repeat this job) | ✓ (Recurring Jobs collection) | — (maintenance agreements imply) | ✓ (recurring tasks) | Universal — standard |
| Customer self-service (booking/portal) | ✓ (Customer Center: request service, approve, pay) | ✓ (Customer Portal; online booking) | ✓ (Booking Portal; Customer Portal) | ✓ (Reserve with Google; online booking) | Universal — standard |
| Job costing / commissions | — (not at fetched depth) | ✓ (job costing; commissions tracking) | ✓ (Job Costing feature) | — (reporting implies) | Common — optional |
| Equipment/asset records at sites | — | ✓ (Property Profile) | ✓ (Asset Management) | — | Optional — commercial pole |
| Maintenance agreements / service plans | — | ✓ (Service Plans collection) | ✓ (Maintenance Agreements) | ✓ (Service plans) | Common — optional |
| Inventory / purchase orders | — | ✓ (Purchase Orders; material inventory) | ✓ (Inventory Management) | ✓ (Inventory management) | Common — optional |
| Fleet GPS tracking | — (geocoding implies GPS-readiness) | ✓ (Fleet Management) | ✓ (Fleet Tracking) | ✓ (Route planning; tech location) | Common — optional |
| Payroll / time tracking | — | ✓ (HCP Payroll) | — (timesheets in testimonials) | — | Optional |
| Marketing / reviews / lead capture | — (Opportunities only) | ✓ (Marketing Center; Leads; Pipeline; Job Inbox) | — (lead sources on jobs) | ✓ (Lead management; Genius Marketing) | Common — optional |
| VoIP / call handling | — | ✓ (Voice) | ✓ (Engage VoIP) | ✓ (Genius Phone; communication suite) | Optional |
| Franchise / multi-location | — | ✓ (Franchise collection) | ✓ (Franchises segment) | ✓ (franchise testimonials) | Optional |
| AI assistants | — | ✓ (AI Team; HCP Assist) | ✓ (Operator AI; ClearPath) | ✓ (Genius Answering; Jessica) | Optional — era-current |
| Accounting sync | ✓ (QuickBooks 2-way) | ✓ (QuickBooks Online/Desktop) | ✓ (QuickBooks-class) | ✓ (QuickBooks) | Universal — standard |
| Permissions over financial visibility | — | — | ✓ (FAQ: control what employees see) | — | Common — optional |
| Trade layer realization | none (trade-agnostic) | industry packages for 3 trades only | trade solution pages over one platform | industry pages over one platform | The family's packaging pattern |

### What is actually generic (across sample)

1. **The four-leg spine** — customer+location → job lifecycle → office→field technician coordination → invoice/payment — is present and central in all four products, expressed in near-identical vocabulary (job/work order, schedule/dispatch, invoice, get paid). [Layer A ×4 + Layer B across sibling passes]
2. **The estimate as the priced upstream of the job** — every product carries a quote/estimate object that converts into a job on approval. [Layer A ×4]
3. **The price book as the pricing substrate** — line items drawn from a maintained list of services/materials. [Layer A ×4]
4. **The technician mobile app as the field surface** — assigned jobs, photos, notes, signatures, on-site payment. [Layer A ×4]
5. **Customer communication as a built-in layer** — confirmations, reminders, arrival updates, invoice delivery. [Layer A ×4]
6. **The trade layer is packaging, not structure** — Kickserv ships no trade layer at all; Housecall Pro packages only 3 of its trades; FieldPulse and Workiz ship trade solution/industry pages over one platform. The same platform serves 50+ industries. [Layer A ×4; Layer B: ServiceTitan ~20 trade pages, Service Fusion ~29 clone pages]

No sampled product showed a structurally distinct generic-FSM object beyond the spine: no entitlement/contract-of-coverage object (that is the aftermarket seam), no dispatch-optimization engine as the center (that is Dispatch Management), no owned-asset registry (that is CMMS/EAM).

## Canonical Model

### Level 0 — Defining Invariant (deliberately minimal)

1. **Customer with a service location** — work is performed at the customer's premises (home, building, facility, site), so jobs bind to addresses; the customer may be a person, a business, or a parent record with multiple service locations.
2. **The job (work order) as the unit of work** — a requested piece of service work at that location, carried through a managed lifecycle (requested → scheduled → assigned → performed → completed → billed), with explicit cancellation/reschedule semantics.
3. **The field technician as the executing role, coordinated by the office** — jobs are assigned to field workers through scheduling/dispatch; the office plans, the field executes, and status flows back.
4. **Billing of completed work** — the job resolves into an invoice and payment collection (estimate/quote upstream of larger work).

Remove the customer/location → generic task tracking. Remove the job lifecycle → an address book or invoicing tool. Remove technician coordination → pure invoicing or a booking tool. Remove billing → a dispatch board only. All four legs are jointly held: customer records alone = CRM/contact database; jobs without customers = free-floating task list; customer+job without field coordination = booking/scheduling tool; the first three without billing = a dispatch board with no money; billing without jobs = pure invoicing.

Historical check: a paper-era service business — customer card file with addresses, handwritten job tickets, a dispatch board, an invoice book — satisfies all four legs with no modern machinery. 1990s–2000s dedicated field-service products satisfy them. Trade-agnostic cloud products configured by any trade satisfy them (all four sampled products demonstrate the trade-agnostic pole directly). Mobile apps, GPS, price books, notifications, portals, recurring series, AI — none is definitional. The check passes.

### Level 1 — Common Mature Structure

- Estimates/quotes with line items drawn from a price book; customer approval (often e-signature); conversion into jobs
- Scheduling calendar + dispatch board; drag-and-drop assignment; GPS-backed technician views in mature products
- Technician mobile app: assigned jobs, navigation, job details and customer history, photos, notes, signatures, on-site payment, invoice creation
- Price book of services and materials with prices
- Customer notifications: booking confirmations, day-of reminders, on-my-way alerts, invoice delivery
- Multi-visit jobs (work events/appointments under one job; multi-day appointments)
- Recurring jobs / recurring series
- Customer self-service: online booking pages, customer portals (request service, approve estimates, pay invoices, view history)
- Reporting/dashboards: jobs, revenue, technician performance, lead sources
- Accounting sync (QuickBooks in the North American SMB market)
- Job costing and commissions tracking in the deeper products

### Level 2 — Variant / Optional Structure

- Equipment/asset records at customer sites with service history — commercial-service pole
- Maintenance agreements / service plans / memberships (recurring revenue programs)
- Project machinery (phases, task dependencies, budgets, job costing) — larger-job pole
- Inventory, purchase orders, truck stock
- Fleet GPS tracking; route planning
- Payroll / time tracking
- Marketing automation, review management, lead capture/pipeline (Job Inbox-class)
- VoIP/call tracking embedded in the platform
- Franchise / multi-location structures
- Consumer financing at the point of sale
- Financial-visibility permissions (who sees invoicing/billing data)
- AI assistants (call answering, scheduling, note cleanup) — era-current

### Level 3 — Vendor-specific (kept out of the canonical document)

- Kickserv: "Opportunity" object naming for the pre-estimate stage; Customer Center link expiry; Stripe estimates sent as text messages
- Housecall Pro: HCP Payments/Payroll/Money module names; Job Inbox; HCP Assist; AI Team; Alexa skill; Twilio 10DLC registration; "Pro canceled" status label; industry packages (HVAC/Electrical/Plumbing only)
- FieldPulse: Operator AI (24/7 AI dispatching); ClearPath guided job-stage workflows; Engage VoIP; Field Intelligence; 78% year-over-year growth claim; G2 badges
- Workiz: Genius suite (Answering/Marketing/Phone/Scheduling); Jessica AI assistant; "120K+ pros" claim; Automations "when-this-happens" rules

## Vendor-specific Findings

See Level 3. Notable patterns: (1) the competitive set is closed — FieldPulse's own comparison pages list ServiceTitan, Jobber, FieldEdge, Service Fusion, Housecall Pro, confirming one market; (2) vendors articulate the category identically ("field service management application" — FieldPulse FAQ; "comprehensive field service management software" — Workiz FAQ); (3) the SMB scope is positioning, not structure — FieldPulse carries a "Small Business Leader" badge and a "good for small businesses" FAQ, Workiz counts "120K+ home service pros", yet the object world is scale-independent.

## Rejected Findings

1. **"Small business" as a structural property** — no sampled product carries an SMB-specific structure; the spine is identical at the owner-operator pole (FieldPulse FAQ: "I don't have any other employees") and at the franchise pole. The leaf name marks the market segment this leaf carries, not a different data model. Rejected as definitional.
2. **Dispatch optimization as the defining center** — dispatch is one stage of the spine; the sampled products center the job lifecycle, not the routing engine. Rejected (Dispatch Management territory).
3. **Entitlement/contract-of-coverage as a core object** — absent from all four samples; service plans/maintenance agreements exist but as optional recurring-revenue machinery, not as coverage entitlements gating work. Rejected (Aftermarket Service Management seam).
4. **Owned-asset registry as the center** — equipment records in these products describe customer-owned assets at sites, not the operator's own asset base. Rejected (CMMS/EAM seam).
5. **Phone-first identity or communication as definitional** — embedded VoIP/AI answering is era-current optional machinery; the spine functions without it. Rejected.

## Boundary Findings

1. **vs the §29 trade siblings — FAMILY RATIFICATION (the pass's central deliverable).** Eleven sibling passes found the identical spine (customer+location → job lifecycle → technician/crew coordination → invoice/payment) with trade semantics as the difference, and vendors themselves ship trades as labeled pages/configurations over one platform while trade-agnostic products (Kickserv, Housecall Pro for unpackaged trades) serve trades with no trade layer. **Ratified: the trade-tuned siblings (appliance-repair, cleaning, electrical, garage-door, handyman, HVAC, landscaping, lawn-care, locksmith, plumbing, pest-control, pool-service) are trade-Variants of this Type** — distinct directory leaves by trade semantics, one structural family. **Structurally distinct siblings (NOT variants, kept separate):** fire-protection (code-mandated inspection program + deficiency records + compliance reporting), restoration (payer-review payment path + evidentiary job file), roofing (measured-roof quantity basis + job-bound material procurement + sale-driven production), flooring (dealer vertical: measured-area basis + material sourcing/allocation + material+labor sale), home-improvement (sale-driven multi-step production project shape). **Junk-removal:** the per-job junk-removal pole runs on generic FSM products (this pass's sample includes junk-removal businesses on Workiz/FieldPulse), so that leaf's distinctness rests on the dedicated hauler structures (containers, rounds, disposal legs, weight/volume billing) — consistent with the junk-removal pass's own holding.
2. **vs Dispatch Management** — dispatch is one stage of this Type's spine; this Type runs the whole customer→job→invoice→payment loop. Confirms the seam recorded in research/dispatch-management.md.
3. **vs Aftermarket Service Management** — this Type is generic job dispatch (jobs for any customer, equipment as incidental detail); aftermarket is the asset-centric superset (installed base + entitlement anchoring). Gradient, not a wall; confirms research/aftermarket-service-management.md's proposed test. Enterprise FSM products (Salesforce Field Service, IFS, SAP FSM, ServiceMax class) sit on the aftermarket side; this leaf carries the SMB trade/home-services market.
4. **vs CRM** — CRM centers on relationship/pipeline records; this Type centers on executed work at locations resolving into money. FSM products carry CRM-lite (customer records, lead capture, pipelines — Housecall Pro Leads/Pipeline, Workiz lead management) but the job + field execution + invoice is the center.
5. **vs Appointment Scheduling Application** — booking is one fragment (online booking pages exist in all four samples); this Type is the whole business operation around the booked work.
6. **vs Local Service Marketplace / Home Services Marketplace** — demand-side matching among independent external providers vs operator-side execution of the business's own workforce; a marketplace lead becomes a job here (Job Inbox-class lead capture is the seam's concrete form).
7. **vs CMMS / Enterprise Asset Management** — CMMS/EAM manages assets owned by the operator; this Type manages service work performed at customers' premises. Site-equipment records here are customer-owned asset registries.
8. **vs Utility Field Service Management / Telecom Field Service (§19)** — utility/telecom-side workforce dispatch against network assets owned by the software operator's organization vs contractor-side business management serving customers. Different operator, different object, different money flow.
9. **vs Invoicing Application / Accounting Software** — money-only tools vs the whole work loop; the QuickBooks sync is the integration seam (FieldPulse FAQ explicitly answers "How is this different than QuickBooks?").
10. **vs Employee Scheduling Platform (§09)** — scheduling employees into shifts vs scheduling jobs for customers; the schedule here is job-centric and the employee assignment serves the job.
11. **vs To-do List / Task Management Application** — tasks without customers, locations, field execution, or billing.
12. **vs Property Maintenance Management (§17)** — property managers coordinate maintenance across portfolios they operate; this Type is the service business's own system; the property manager appears here as a customer.

## Uncertainties

1. **Jobber** — the largest trade-agnostic SMB brand; unreachable (403 ×4 across passes). Its absence is a market-coverage gap, not a structural one: three sibling passes independently recorded the same gap, and the four researched products already repeat the spine. Assertions calibrated to the four researched products + cross-pass evidence.
2. **Workiz operational depth** — help center unreachable (timeout ×2); Workiz held at Tier 2. Its scheduling/FAQ pages still document the spine explicitly.
3. **Regional markets** — the sample is North America–dominant (QuickBooks-centrism, US SMS/payment mechanics, Twilio 10DLC). Regional variance (e.g., EU VAT-invoicing norms, non-QuickBooks accounting) could not be verified; the canonical document avoids region-specific claims.
4. **Enterprise FSM boundary precision** — the aftermarket-side seam is documented from this side (generic job dispatch) and from the aftermarket pass (asset-centric anchoring); the exact gradient midpoint (e.g., mid-market commercial service contractors) was not sampled this pass and is recorded as a gradient, not a wall.
5. **Historical dedicated FSM products** (1990s–2000s on-premise dispatch/service software) — asserted from the historical check's structural reasoning, not from fetched period documentation; the claim is kept at the abstract level (the spine predates the cloud), not product-named.

## Final Synthesis

Small Business Field Service Management is the trade-agnostic business-management system of a small field service business: it records customers and the locations where work happens, carries each requested piece of work as a durable job with a lifecycle, coordinates the technicians who perform the work in the field through scheduling and dispatch, and turns completed work into invoices and payments. The defining core is exactly this four-leg spine; everything else commonly associated with these products (estimates, price books, mobile apps, notifications, recurring series, portals, GPS, payroll, marketing, AI) is standard or optional capability layered on that spine. The market realizes the Type as one family: vendors ship 50+ trades as labeled pages or configurations over one platform, trade-agnostic products serve any trade with no trade layer at all, and eleven processed sibling passes independently found the identical spine under trade-specific packaging — making this leaf the anchor of the §29 trade-business cluster and the trade-tuned siblings its trade-Variants, while the structurally distinct siblings (fire protection, restoration, roofing, flooring, home improvement) carry defining structures this spine lacks.
