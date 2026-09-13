# Research Notes — Cleaning Business Management

Research date: 2026-09-07
Slug: `cleaning-business-management`
Directory leaf: "Cleaning Business Management" (DIRECTORY.md line 2104, §29 Home, Family, Personal & Local Services)

---

## Research Goal

Understand what "Cleaning Business Management" is as an Application Type: the business-management software used by cleaning companies (residential maid services and commercial janitorial contractors). Identify its core objects (client, service location, visit/job, recurring schedule, crew, checklist, invoice), the visit lifecycle, who operates it, which structures are cleaning-trade-specific, and where its boundary lies against Small Business Field Service Management, other §29 trade leaves, appointment-based service business management, hotel housekeeping management, and marketplaces.

## Initial Boundary (pre-research hypothesis)

- Core hypothesis: operator-side system of record for a cleaning service business; FSM-family spine (client → job → schedule/dispatch → staff → invoice → payment) with cleaning-specific trade semantics (recurring cadence, per-property checklists, crew execution, property access, quality verification).
- Nearest types: Small Business Field Service Management (generic sibling, §29), other trade service leaves (Landscaping, Lawn Care, Pest Control, Pool, HVAC, Plumbing…), Appointment-based Service Business Management (§29), Hotel Housekeeping Management (§26 — in-house, room-centric), Home Services Marketplace / Local Service Marketplace (demand side), Property Maintenance Management (§17 — owner side), Household Chore Application (consumer side).
- Prior art in this production: `research/appliance-repair-management.md` already established that §29 trade leaves share the FSM spine and are probable trade Variants of one family; flagged for joint review when Small Business Field Service Management is processed. This leaf should follow the same convention.
- Unknowns going in: Is recurring scheduling definitional or merely dominant? Is the checklist definitional? How different is the commercial janitorial pole (shifts, inspections, supplies) from the residential pole (booking, quotes, scorecards)? Does the commercial pole include billing?

## Research Questions

1. What objects exist: client, location/property, quote, job/visit, recurring series, checklist/task list, crew/staff, invoice/payment, inspection, supplies?
2. How does a cleaning visit flow from lead to payment, in each pole?
3. How is recurrence modeled (series, occurrences, skip/reschedule, series cancellation)?
4. What is cleaner-facing vs office-facing (mobile app contents)?
5. What is commercial-janitorial-specific (shifts vs jobs, inspections, specs, supplies, workloading/bidding)?
6. What is residential-specific (online booking, pricing models, scorecards, tips, access/entry)?
7. What billing patterns exist (per-visit, batch, card-on-file auto-charge, pre-authorization)?
8. Boundary: what separates this Type from generic FSM structurally vs semantically?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Pole | Segment | Evidence tier reached |
|---|---|---|---|
| Kickserv | horizontal field service management (generic spine) | small SMB service businesses incl. cleaning | Tier-1 (Knowledge Center articles) |
| ZenMaid | cleaning-specific, scheduling-first | small residential maid services | Tier-2 (product site; help center unreachable) |
| Launch27 | booking-first maid service software | small/growing residential maid services | Tier-2 (product site; docs 403) |
| MaidCentral | residential scale platform (CRM+payroll+quality) | mid-size residential cleaning companies | Tier-2 (product site, deep feature pages) |
| Swept | commercial janitorial operations | commercial cleaning companies | Tier-2 (product site, deep feature pages) |

Rejected/considered: Jobber (help center + industry page both 403 — abandoned after 2 failures), Housecall Pro (403), Service Fusion (not fetched; appliance-repair notes already cover it as multi-industry re-skinner), CleanGuru/Janitorial Manager (not fetched; Swept covers the janitorial pole).

## Sources

Fetched 2026-09-07 (all official vendor surfaces):

- Kickserv — Knowledge Center (Help Scout docs): root TOC, "Kickserv Basics" category, "Jobs" article — https://kickserv.helpscoutdocs.com/ , /category/14-the-basics , /article/32-jobs ; product root — https://kickserv.com/
- ZenMaid — product root (features, FAQ "What is Maid Service Software?") — https://zenmaid.com/
- Launch27 — product root (booking features, pricing models, workflow comparison) — https://www.launch27.com/
- MaidCentral — product root, "Intelligent Scheduling" page, "Features and Benefits" page — https://maidcentral.com/ , /intelligent-scheduling/ , /maidcentral-feature-benefits/
- Swept — product root, "Janitorial Inspection Software" page, "Commercial Cleaning Scheduling Software" page, "Janitorial Checklist Software" page — https://sweptworks.com/ , /janitorial-inspection-software , /scheduling-software-for-janitors , /features/janitorial-checklist-software

Source-access limitations:

- Jobber: help.getjobber.com and getjobber.com industry page both returned 403 (2 attempts) — abandoned; no Jobber claims.
- Housecall Pro: housecallpro.com 403 — abandoned; no claims.
- ZenMaid: help.zenmaid.com transport error; feature pages /cleaning-service-scheduling-software and /cleaning-business-app 404 (with and without trailing slash) — ZenMaid evidence is root-page level only.
- Launch27: docs.launch27.com 403 — booking-flow internals not verified beyond root page.
- MaidCentral: /quality-measurement/ 404 (wrong path guess); quality evidence taken from the Features and Benefits page instead.
- Swept: billing/invoicing surface not present on any researched page — recorded as unobserved, not claimed absent.

Consequence: no precise numeric limits, prices (except vendor-published plan prices, kept as vendor claims), time windows, or default values are asserted in the final document.

---

## Product Observations

### Kickserv (horizontal FSM — generic spine) — Tier-1

Evidence layer: A (directly observed in official Knowledge Center).

- Positioning: "Field Service Management Software — Manage customers, schedule jobs and get paid." Industries list: plumbing, restoration, HVAC, technology services, construction, landscaping, electrician (cleaning not in footer list, but Kickserv serves cleaning businesses as part of its generic market).
- Core objects (Knowledge Center "Kickserv Basics" category): Customers and Contacts, Estimates, Jobs, Invoices, Reminders, Reports, Opportunities, Settings.
- Jobs article (Tier-1):
  - "Jobs are the heart of the Kickserv workflow… the main way you'll keep track of business activity."
  - Jobs page is a left-to-right workflow: Unscheduled → (scheduled) → In Progress → On Hold (optional) → Completed.
  - Many jobs start as an Opportunity → estimate → customer approval → transforms into an unscheduled Job. Jobs can also be created directly.
  - Job fields: service type, internal job description (not customer-visible), external scope of work (customer-visible), contact, custom data fields (plan-gated).
  - Scheduling: date/time work event, description for technicians, task type, assign to a specific tech or leave unassigned.
  - Start Job / Stop Job / On Hold / Mark Complete; a job can hold several work events (multi-visit jobs); marking complete can mark all work events complete.
  - Recurring Jobs: "Repeat this job" → frequency dropdown → customize by date or day of week → end condition → generates repeating jobs on the schedule.
  - After completion: send invoice and get paid.
- Product root: Customers (customer view, job history, messaging, Customer Center), Estimates (signature approval, customer pipeline), Jobs (notifications, expenses, photos/documents/notes), Invoices (receivables, online payments), Mobile (job schedule, GPS & time tracking, digital signatures, onsite credit card payment), Integrations (QuickBooks Online/Desktop 2-way sync, Stripe, Mailchimp, Podium).
- Plans published: Start $60/mo (5 users), Run $119/mo (10 users), Scale $199/mo (20 users) — vendor claim.

Observation: this is the generic FSM spine with no cleaning-specific structures (no checklists-as-cleanlists, no property access records, no inspections). Useful as the "remove the trade semantics" control sample.

### ZenMaid (cleaning-specific residential, scheduling-first) — Tier-2

Evidence layer: A for the root page's own claims; product-level only (help center unreachable).

- Positioning: "Maid service software… for residential home cleaning businesses", "designed by maid service owners". FAQ defines the category: scheduling, invoicing & card processing, automated email/SMS communications, online booking.
- Scheduling: drag-and-drop calendar; create/view/edit jobs; once scheduled, customers and cleaners are instantly notified.
- Automated communications: appointment reminders, automated appointment confirmations, on-my-way notifications; messages to clients, managers, and cleaners.
- Booking: instant booking form hosted on the company's website or as a standalone link; customizable and branded.
- Invoicing & billing: branded invoices, billing reminders & follow-ups, payment history and lifetime value.
- Credit card processing: cards on file; Stripe and Square integrations; automatic charging implied by "let you charge their card automatically".
- Cleaner mobile app: check schedules anywhere, track time with one tap, photos and job notes.
- Free migration/import of client data (vendor service claim).
- Target community: solo-to-small maid service owners (case studies: solo cleaner → 15-person team).

Observation: the residential pole in its purest form — calendar + recurrence + automated comms + card-on-file + cleaner app. No inspections, no supplies, no shift machinery observed.

### Launch27 (booking-first residential) — Tier-2

Evidence layer: A for root-page claims; docs 403.

- Positioning: "Maid Service Software — More cleaning jobs, less scheduling, pre-verified payment."
- Online booking: clients see real-time availability and self-schedule without calling.
- Pricing models offered to clients at booking: number of bedrooms and bathrooms, hourly, square feet/meters, custom pricing.
- Payments: pre-authorize credit cards at booking; charge when the cleaning service is complete.
- No-show reduction: automatic text and email reminders before each job.
- Feedback: automatic post-job rating email per job.
- Recurring: "sets up recurring appointment" listed as the automated alternative to manual upsell.
- The marketing contrast table frames the automated loop: instant estimate → customer books online → auto reminders → card stored on file → charge when you want → auto rating email → recurring appointment.
- Help docs exist at docs.launch27.com but returned 403.

Observation: the demand-capture pole — the booking form and payment pre-verification are the product's center of gravity; office-side depth (crews, checklists) not observed on the researched page.

### MaidCentral (residential scale platform) — Tier-2, deep

Evidence layer: A for the fetched pages' claims.

- Positioning: "The only platform built to scale residential cleaning companies", "built by cleaning professionals, for cleaning professionals". FAQ explicitly: intelligent cleaning scheduling software is "a subtype of field service management software used specifically for cleaning companies" — vendor's own family placement.
- Feature map (root + features page):
  - CRM & Sales: "complete lifecycle CRM for the house cleaning industry"; lead capture, lead source reporting, drip campaigns, automated review generation, coupons/gift cards.
  - Online quoting & booking: online quotes, booking tied to company availability settings, embeddable booking tool.
  - Scheduling: intelligent scheduling (proximity + employee efficiency), master schedule, drag-and-drop job scheduler (view day's jobs by teams/members/time/customer; flag jobs by employee preference; custom tags for customer preferences; hover for full customer details), zones ("create zones… maximize efficiency with route planning"), skills/tags/zones, availability calendar, revenue production planning, client preference management, property management.
  - Service sets: "Think of a service set as a unique job rotation for a specific property" — multiple service sets per property; multiple homes per customer account (dedicated how-to).
  - Dispatching: team monitor, in-app notifications, behind-schedule notices, exception notifications, productivity & variance reports, 2-way tech SMS; scheduling-rule violation warnings ("warns you when you are violating scheduling rules for clients in terms of times, teams, and other key parameters").
  - Recurrence semantics: "MaidCentral uses the word cancel to mean two different things… cancel the selected job and all future jobs" — series-level vs occurrence-level cancellation documented.
  - 52-week schedule concept promoted as the foundation of a profitable cleaning business (blog).
  - Employee engagement: technician dashboard; clock in/out for the day; job worksheet with notes/photos/reminders; time spent on jobs, travel time, breaks visible; time-off requests + doctor's excuse upload; office managers view schedule requests and add blackout days; GPS nav + reporting; scorecards.
  - Payroll reporting: pay commission, job ticket hour, hourly, and more; client tips captured via scorecards flow to employee pay; PTO + sick time; performance pay.
  - Quality measurement: automatic scorecard requests after each job; scores track trends per job and per employee; tips tied to satisfaction.
  - Finance: batch billing & invoicing ("one click billing all of your customers for the day"), automated credit card processing, accounts receivable, rate variance reports, rate increase automation, multi-location reporting, KPIs, company health.
  - Integrations: QuickBooks (accounting), Paystri (payroll), Twilio (communications), Zapier, API.
  - Customer portal: customers update contact/payment info, access their home's service details and cleaning notes, set notification preferences, see pricing and invoices.
  - Onboarding: dedicated success coach, multi-step setup, training (vendor service claim; "6 to 8 weeks" learning-curve claim — vendor claim, not asserted in final doc).

Observation: the residential pole at scale — adds CRM/marketing automation, payroll/performance pay, quality scorecards, rate management, multi-location. Client preferences and rule-based scheduling warnings are distinctive depth.

### Swept (commercial janitorial) — Tier-2, deep

Evidence layer: A for the fetched pages' claims.

- Positioning: "Workforce Management for Commercial Cleaning Businesses" / "All-in-one janitorial software". Plans: Launch (time tracking, scheduling, compliance), Optimize (quality control), Scale (client communication, supplies, cost control) — plan prices published ($30/mo start; Optimize from $150/mo; Scale from $225/mo — vendor claims).
- Scheduling (dedicated page):
  - Unit of scheduling is the **shift**, bound to a **location** ("Catalina Building C", "Dodgers Stadium" in product screenshots), assigned to named cleaners (crews shown as "Jenna Lim +1").
  - "Recurring schedules that match your contracts": daily/weekly/custom recurring shifts; assign cleaners to locations; one-time work orders for extra work; real-time map views.
  - Weekly attention flags: unassigned shifts, pending time-off requests, missed shifts, late arrivals, scheduled-overtime risk (flag when scheduled over 40 hours — product-specific threshold, vendor claim).
  - Views: Calendar / Location / Team; agenda; map.
  - Time off: cleaners request from mobile app; managers see affected shifts before approving; approval removes cleaner from affected shifts.
  - Schedule variance: scheduled vs actual hours across locations; break/lunch tracking for compliance and payroll; payroll exports.
  - Location records: "Store entry codes, supply lists, and approved cleaners for each location so the right information reaches the right people automatically."
  - GPS-verified clock-ins confirm cleaners started shifts.
- Cleaner checklists (dedicated page):
  - Location-based: "Required checklists are available at the location of their shift"; required vs optional tasks labeled.
  - Multilingual: tasks translated into 100+ languages based on cleaner's language setup; translate button.
  - Photo proof: one optional image per completed checklist task; images reviewed in Checklist Result Report; client-ready PDF.
  - Progress: start/pause/complete, auto-save.
  - Reporting: filter by date, location, cleaner, completion rate.
- Inspections (dedicated page):
  - Client-specific inspection templates: checkpoints organized by area; require photos/notes on critical items; clone templates across clients; tailor to medical facilities, corporate offices, specialty sites.
  - Mobile inspections: supervisors walk sites, rate checkpoints, timestamped photos (tamper-proof timestamp embedded), offline mode syncs later; guided workflows in English/Spanish/Portuguese.
  - Quality scores per inspection; inspection history dashboards; trend tracking.
  - Client reporting: email, secure link, or downloadable PDF; positioned as contract-retention tool ("protect every contract").
- Other: supply management (track usage, avoid over-ordering), job costing tool (bid confidently on job costs & target margin), profitability reports (which jobs make money), client & cleaner messaging (replaces WhatsApp/email), time tracking with GPS.
- Billing/invoicing: NOT observed on any researched page (uncertainty recorded).

Observation: the commercial pole — shift-based scheduling against contract locations, attendance/coverage management, location-borne access/supply/spec records, checklist execution with photo proof, supervisor inspections with client-facing reports, cost/profitability control. Client-facing quality proof is a contract-retention weapon.

---

## Cross-product Comparison

| Structure | Kickserv (horizontal) | ZenMaid (residential) | Launch27 (booking-first) | MaidCentral (residential scale) | Swept (commercial) |
|---|---|---|---|---|---|
| Client records | ✔ customers & contacts | ✔ | ✔ | ✔ CRM, multiple homes per account | ✔ clients |
| Service location as record | job address on customer | ✔ client homes | ✔ client address | ✔ property management, service sets per property | ✔✔ location-centric (entry codes, supplies, approved cleaners) |
| Quote / estimate | ✔ opportunities → estimates → approval | booking form captures info | instant online pricing (beds/baths, hourly, sqft, custom) | online quoting + accurate quoting | job costing / bidding support |
| Visit / job unit | ✔ jobs w/ lifecycle + work events | ✔ calendar jobs | ✔ appointments | ✔ jobs; service sets as rotation | shifts (recurring) + one-time work orders |
| Recurring scheduling | ✔ "repeat this job" w/ end condition | ✔ core pattern | ✔ recurring appointments | ✔ 52-week, series vs occurrence cancel | ✔ contract-matched recurring shifts |
| Staff assignment | ✔ assign tech (or unassigned) | ✔ assign cleaners | implied (availability) | ✔ teams, zones, skills, preferences | ✔ shift assignment, crews ("+1") |
| Cleaner/tech mobile app | ✔ (schedule, GPS/time, signatures, payments) | ✔ (schedule, time, photos, notes) | not observed | ✔ (dashboard, clock in/out, worksheets) | ✔✔ (schedule, clock-in, checklists, time-off) |
| Checklist / task list per visit | not observed | job notes/checklists (marketing level) | not observed | ✔ job worksheets; service sets | ✔✔ location checklists, required/optional, translations, photo proof |
| Clock in/out / time tracking | ✔ GPS & time tracking | ✔ one-tap time tracking | not observed | ✔ clock in/out, travel, breaks | ✔✔ GPS-verified, variance, breaks |
| Invoicing / payments | ✔ invoices, online payments | ✔ invoices, Stripe/Square cards-on-file | ✔ pre-auth + charge after service | ✔ batch billing, auto CC, AR | not observed on researched pages |
| Quality feedback loop | not observed | not observed | ✔ post-job ratings | ✔ scorecards per job/employee, tips | ✔✔ inspections w/ scores, photos, client reports |
| Customer self-service | ✔ customer center | not observed | booking form | ✔ customer portal | client messaging + shared reports |
| Payroll linkage | not observed | not observed | not observed | ✔ payroll reporting, performance pay, PTO, tips | ✔ time exports to payroll, break tracking |
| Supplies management | — | — | — | — | ✔ |
| Marketing/sales automation | integrations (Mailchimp) | — | — | ✔ lead capture, drip, review generation | — |
| Multi-location ops | — | — | — | ✔ multi-location reporting | ✔✔ multi-site by design |

Legend: ✔ observed on official pages; ✔✔ central/emphasized; "not observed" = not found on researched pages (not claimed absent); "—" = out of product's observed scope.

### Reading of the comparison

- The spine (client+location → scheduled visit → assigned staff → billing) is present across the residential and horizontal samples; Swept shows the spine with the commercial vocabulary (clients/locations → shifts → cleaners → [billing unobserved]) and emphasizes cost/profitability instead.
- Recurring scheduling is present in all five products in some form — but as an option in the horizontal product (Kickserv "repeat this job") and as the dominant pattern in cleaning-specific products. Cross-product commonality (layer B), not definitional by the removal test (one-time cleaning businesses exist and all products support one-time jobs/work orders).
- The per-visit checklist/task structure is central in cleaning-specific products (Swept, MaidCentral worksheets/service sets, ZenMaid job notes) and absent in the horizontal control (Kickserv). It is the most distinctive cleaning-trade structure observed — layer B across the cleaning-specific sample, product-differentiated against the generic spine.
- The commercial pole adds objects the residential pole lacks (inspection, supply, contract-shift machinery); the residential pole adds objects the commercial pole lacks (online booking/pricing models, scorecards+tips, batch consumer billing). These are segment variants over one Type, not two Types — both share client/location/visit/staff/billing.
- Quality verification exists in both poles but with different instruments: residential = customer scorecards/ratings after each job; commercial = supervisor inspections with photo proof and client-ready reports. Common (layer B), not definitional (absent in Kickserv and ZenMaid evidence).

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the software stops being recognizable as cleaning business management:

```text
Client records with the service locations cleaned for them
└── Cleaning visit — the unit of work: a scheduled service event
    bound to client + location + time (one-time or part of a series)
    └── Assigned staff — the cleaners/crew who perform the visit
        └── Billing — the visit resolves into money (invoice/charge)
```

Four properties:

1. **Client + service location as records** — cleaning is delivered at the client's site; the location (home or facility) is a managed record bound to the client, carrying service context. Remove it → generic invoicing/calendar tool.
2. **The cleaning visit as the durable unit of work** — a scheduled service event with a lifecycle (scheduled → performed → completed → billed). Remove it → pure contact manager.
3. **Assigned staff as the executing role** — the office coordinates who cleans; without any performer assignment it is a booking widget, not business management.
4. **Billing of the service** — visits resolve into invoices/charges. Remove it → scheduling app only.

Operator-side framing: the system is the cleaning business's system of record for selling and delivering cleaning — not a consumer booking surface (that is one interface among several).

Removal test vs neighbors: remove the trade semantics below and the generic FSM spine remains (→ Small Business Field Service Management); remove the operator-side business record (keep only the bookable catalog + appointment) → Appointment-based Service Business Management.

### L1 — Common Mature Structure

Present in most mature products researched; expected by the market but not definitional:

- **Recurring service schedules** — the dominant deployment pattern in both poles (weekly/biweekly residential; contract-based commercial). Modeled as a series generating occurrences, with skip/reschedule and series-vs-occurrence cancellation semantics.
- **Quoting/estimating** — residential: instant online quotes priced by home size (beds/baths, square footage) or hourly; horizontal: estimate → approval → job.
- **Online booking / booking forms** — client self-service capture tied to real-time availability (residential pole).
- **Cleaner mobile app** — today's schedule, job details, clock in/out (often GPS-verified), checklist/worksheet execution, photos, notes, time-off requests.
- **Automated client communications** — booking confirmations, appointment reminders, on-my-way notifications, post-visit follow-ups (email/SMS).
- **Invoicing + stored payment** — per-visit invoices, batch billing, cards on file with auto-charge, pre-authorization at booking.
- **Visit execution record** — worksheet per visit: time spent, travel time, breaks, photos, notes.
- **Quality feedback loop** — residential: customer scorecards/ratings per job (sometimes tied to tips); commercial: supervisor inspections with rated checkpoints, timestamped photos, quality scores, client-ready reports.
- **Crew/team assignment** — teams of cleaners dispatched together; team boards; employee preferences/flags.
- **Time tracking → payroll linkage** — clock data feeding payroll reporting/exports; tips; performance pay (depth varies).
- **Reporting/dashboards** — job costing, profitability per client/contract, KPIs, schedule variance.
- **Customer portal / self-service** — clients manage contact/payment info, preferences, bookings, invoices.
- **Notifications to staff** — schedule changes, new/late/missed shift alerts.

### L2 — Variant / Optional Structure

Depends on segment, scale, geography, business model:

- **Segment poles**: residential maid service (booking, quotes, per-home checklists, tips, scorecards) vs commercial janitorial (contract shifts, inspections, supplies, workloading, multi-site by design).
- **Scheduling philosophy**: drag-and-drop calendar (ZenMaid, MaidCentral) vs shift-based contract scheduling (Swept) vs rule-based "intelligent" scheduling with violation warnings (MaidCentral) vs simple job scheduling (Kickserv).
- **Pricing models**: fixed per visit, hourly, by bedrooms/bathrooms, by square footage, custom (observed in Launch27's booking options).
- **Property access handling**: entry codes, lockbox/key notes, approved-cleaner lists per location (observed in Swept; residential access notes implied by job notes) — depth varies.
- **Supplies management** (commercial), **workloading/job costing for bidding** (commercial).
- **Payroll depth**: time exports vs payroll reporting with commission/job-ticket-hour/hourly pay, PTO, tips distribution.
- **Marketing/sales automation**: lead capture, drip campaigns, review generation (suite expansion in scale-focused products).
- **Multi-location/multi-branch operations** (multi-location reporting; branch comparison).
- **Integrations**: accounting (QuickBooks class), payroll, SMS/communications, Zapier/API.
- **Plan-tier packaging** (capability gating by plan observed in Kickserv custom fields and Swept Launch/Optimize/Scale).
- **Multilingual crew support** (checklist translations — observed in Swept; likely era-common in commercial, single-product evidence in sample).
- **Marketplace/consumer-app posture**: some residential products expose consumer-facing booking apps; others are operator-side only.

### L3 — Vendor-specific (research notes only)

- Kickserv: "Norman" mascot branding; plan names Start/Run/Scale with user counts and prices; custom fields plan-gating; Help Scout knowledge base structure; Opportunity → estimate → job transformation naming.
- ZenMaid: free client-data migration service; "maid service software" category education; Stripe+Square dual integration claim; Maid Summit community/courses; magazine content.
- Launch27: pre-verified payment framing; themes marketplace; Bitbucket API docs; 14-day trial framing.
- MaidCentral: "service set" terminology; PCI (Professional Cleaning Index) report from 150K+ cleanings/month; success-coach onboarding; Paystri/Twilio integrations; "6 to 8 weeks" onboarding claim; Inc 5000 customer marketing; rate increase automation; 52-week schedule doctrine; blackout days.
- Swept: Launch/Optimize/Scale plan names and prices; 100+ language translation claim; tamper-proof photo timestamps; overtime flag at 40 hours (product-specific threshold); English/Spanish/Portuguese inspection workflows; Halifax branding; "save 7 hours a day" / "91% better retention" marketing claims.

## Rejected Findings (considered and not promoted)

- **"Recurring scheduling is definitional"** — rejected by removal test: one-time cleaning (move-out, post-construction) is a supported first-class pattern in the horizontal sample (Kickserv one-off jobs; Swept one-time work orders) and Launch27's loop works for single bookings. Promoted to L1 as the dominant pattern instead.
- **"Checklists are definitional"** — rejected: the horizontal control product lacks them yet serves cleaning businesses; checklist depth varies (marketing-level vs core). Promoted to L1 as the most distinctive trade structure, with segment-dependent depth.
- **"Inspections are definitional"** — rejected: residential pole uses scorecards instead; single-pole evidence. L1 (quality loop) with pole-specific instruments.
- **"GPS-verified clock-in is definitional"** — rejected: observed in 3 of 5 products with varying emphasis; era-common implementation of time tracking, not the invariant.
- **"Cleaning software is a separate Type from FSM"** — not supported: the spine is identical; the vendor's own positioning (MaidCentral FAQ) calls cleaning scheduling "a subtype of field service management software". Trade-variant relationship recorded instead.
- **"Swept lacks billing"** — not claimable: billing simply was not on the researched pages; recorded as unobserved.

## Boundary Findings

1. **vs Small Business Field Service Management (§29 sibling)** — sharpest seam. The researched sample shows the identical structural spine (client+location → job/visit lifecycle → staff dispatch → invoice/payment) in both. The difference is trade semantics: cleaning visits are (a) predominantly recurring, (b) executed by crews rather than single technicians, (c) specified by per-property checklists/task lists, (d) performed via client-property access (entry codes, approved cleaners), and (e) verified by a quality loop (scorecards/inspections). Structural test: remove the cleaning trade semantics → generic FSM remains; remove nothing structural → cleaning business management remains. Probable trade-Variant relationship rather than two independent Types — consistent with the appliance-repair precedent; flagged for joint review when Small Business Field Service Management is processed.
2. **vs other §29 trade leaves (Landscaping, Lawn Care, Pest Control, Pool, HVAC, Plumbing…)** — same family relationship; one product family, many industry pages (MaidCentral's own FAQ places cleaning software inside FSM). Cleaning's distinguishing semantics vs outdoor/repair trades: indoor recurring visits, unoccupied-premises access, crew execution, no parts/equipment.
3. **vs Appointment-based Service Business Management (§29 sibling)** — appointment businesses are client-travels-to-provider with a bookable service catalog at a place of business; cleaning is provider-travels-to-client with quotes, crews, property access, and recurring contracts. The online booking surface overlaps, but the managed business model differs structurally.
4. **vs Hotel Housekeeping Management (§26)** — in-house hotel housekeeping manages rooms/room status inside a PMS context for one property; cleaning business management serves external clients across many properties and bills them. Different core objects (room inventory vs client contracts).
5. **vs Home Services Marketplace / Local Service Marketplace (§29)** — demand-side discovery/booking vs operator-side business management. Marketplace posture appears only as an optional L2 surface (booking widgets), not the Type.
6. **vs Property Maintenance Management (§17)** — property-owner-side maintenance of owned assets vs service-business-side client billing for cleaning work.
7. **vs Household Chore Application (§29)** — consumer-side family chore tracking vs business-side cleaning service operations.
8. **vs Employee Scheduling Platform (§09)** — shift scheduling exists inside this Type but bound to cleaning contracts/locations/checklists, not as standalone workforce management.

## Uncertainties

- ZenMaid evidence is root-page level (help center unreachable): cleaner-app details (checklist depth, time-tracking mechanics) not verified beyond marketing claims.
- Launch27 docs 403: office-side depth (crew assignment, checklists) unverified; only the booking/payment loop is evidenced.
- Swept billing: not observed on researched pages; whether Swept includes invoicing/contract billing is unknown. L0's billing leg rests on 4 of 5 products directly; for Swept it is inferred from the Type's frame (profitability reports presuppose revenue) — flagged, not asserted.
- Jobber/Housecall Pro unreachable: the horizontal pole is covered by Kickserv alone; other horizontal products' cleaning-specific features unverified.
- Payroll depth varies (reporting vs full payroll); per-product payroll mechanics not deeply verified.
- Residential products' commercial capabilities (and vice versa) not exhaustively probed; segment separation observed at the level of emphasis, not absolute exclusion.
- No numeric limits/defaults asserted anywhere (per evidence rules); plan prices kept as vendor claims only.

## Final Synthesis

Cleaning Business Management is the operator-side business management application of a cleaning service company. Its defining core is small: clients with the service locations cleaned for them; the cleaning visit as the durable unit of work (scheduled, bound to client+location+time, one-time or recurring); assigned cleaners/crews as the executing role coordinated by the office; and billing that resolves visits into money. Around this spine, mature products add the standard machinery of the trade: recurring series management (the dominant pattern in both segments), quoting and online booking, cleaner mobile apps with clock-in and checklist execution, automated client communications, invoicing with stored payments, quality verification (customer scorecards residentially, supervisor inspections commercially), time-to-payroll linkage, and reporting. The Type is best understood as the cleaning trade variant of field service management — structurally identical to generic FSM, differentiated by cleaning semantics: recurrence as the dominant cadence, crew-based execution, per-property task specifications, unoccupied-premises access handling, and quality proof as a contract-retention instrument. The residential and commercial poles emphasize different parts of the same structure (booking/quotes/scorecards vs shifts/inspections/supplies) and are segment variants, not separate Types.
