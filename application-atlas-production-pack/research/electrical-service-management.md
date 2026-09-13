# Research Notes — Electrical Service Management

Research date: 2026-09-07
Leaf: Electrical Service Management (DIRECTORY.md §29 Home, Family, Personal & Local Services)
Slug: electrical-service-management

## Research Goal

Understand what "Electrical Service Management" software actually is in the real market: what objects it manages, how electrical work flows through it, what is electrical-trade-specific versus generic field-service structure, and where its boundaries lie with neighboring Application Types (generic small-business field service management, trade siblings like HVAC/plumbing/appliance repair, construction project management, utility field service).

## Initial Boundary

Working hypothesis at start:

- It is the business-management system of an electrical contractor / electrical service company (residential service, commercial service, and electrical installation work).
- Core objects likely: customer + service location, job/work order with lifecycle, estimate, schedule/dispatch, technician (electrician), invoice/payment, price book.
- Closest neighbors: Small Business Field Service Management (generic FSM — likely the same structural spine), HVAC Service Management / Plumbing Business Management / Appliance Repair Management (trade siblings), Construction Project Management (commercial electrical installation projects), Utility Field Service Management (different operator entirely).
- Key open question: does the electrical trade carry any *structurally* distinct object (permits, panels/equipment registries, certification-aware dispatch), or is "electrical" purely a content/packaging layer over generic FSM?

## Research Questions

1. What objects make up the system (customer, location, job, estimate, appointment/visit, technician, equipment, invoice, payment, price book)?
2. How does an electrical job flow from inquiry to payment? Multi-visit? Service call vs install/project?
3. What is electrical-specific in the market: pricing catalogs, permits/compliance, panel/equipment records, certification-aware dispatch, trade-tuned reporting?
4. How do scheduling and dispatch work across products?
5. How does the residential/light-commercial pole differ from the commercial pole?
6. What recurring-work machinery exists (service plans, memberships, agreements)?
7. Which interfaces do users actually operate (office dashboard, schedule, job detail, mobile app, customer-facing surfaces)?
8. Historical check: would older, regional, trade-agnostic, or paper-era operations still fit a minimal definition?

## Representative Products

Selected for market representation + documentation access + different product philosophies + different customer layers:

| Product | Segment / philosophy | Evidence tier |
|---|---|---|
| Housecall Pro | micro-SMB; residential & light-commercial electrical; customer-experience/payments-first; ships an explicit "Electrical Package" | Tier 1 (help center) |
| Service Fusion | SMB–mid; all-in-one multi-trade suite with a dedicated Electrical industry page (~30 clone industry pages over one product) | Tier 2 (product pages) + Tier 1 (Zendesk KB) |
| Kickserv | micro-SMB; simple, low-cost, trade-agnostic service business management (electricians among many trades) | Tier 1 (knowledge center) |
| BuildOps | commercial service contractors (electrical flagship vertical); service + projects + financials on one platform | Tier 2 (site + rich FAQ) |
| ServiceTitan | flagship "software for the trades", residential + commercial; Electrical is one of ~20 trade pages over one platform | Tier 2 (site + electrical page) |

Jobber (a major SMB generalist heavily marketed to electricians) was attempted twice (2026-09-06 and 2026-09-07; HTTP 403 both times) and abandoned per source-access rules.

## Sources

Fetched 2026-09-07:

- Housecall Pro Help Center (Tier 1): https://help.housecallpro.com/en/ — collection map; "Industry Packages" collection; article "Electrical Package Overview" (https://help.housecallpro.com/en/articles/15936816-electrical-package-overview)
- Service Fusion (Tier 2): https://www.servicefusion.com/electrical-contractor-software ; https://www.servicefusion.com/support
- Service Fusion Support Center (Tier 1): https://servicefusion.zendesk.com/hc/en-us — root + featured articles list; article "Customer Creation and Linking a Parent Account" (https://servicefusion.zendesk.com/hc/en-us/articles/360024040551)
- Kickserv Knowledge Center (Tier 1): https://kickserv.helpscoutdocs.com/ — "Kickserv Basics" category; article "Jobs" (https://kickserv.helpscoutdocs.com/article/32-jobs)
- BuildOps (Tier 2): https://buildops.com/industries/electrical — positioning + extensive FAQ on electrical operations
- ServiceTitan (Tier 2): https://www.servicetitan.com/ — feature/trade map; https://www.servicetitan.com/industries/electrical-software — Electrical trade page
- Failed: https://www.getjobber.com/for-electricians/ (403), https://www.housecallpro.com/industries/electrical-software/ (403), https://www.servicetitan.com/electrical (404, wrong path), https://www.buildops.com/electrical-contractor-software/ (404, wrong path)

## Product A — Housecall Pro

### Key observations (evidence layer A unless noted)

- The Electrical Package is described as "Housecall Pro built specifically for residential and light-commercial electrical businesses. It comes preconfigured with the tools, workflows, and settings electrical Pros use every day" — direct vendor statement that the electrical product is a preconfigured trade layer over the general platform. [Layer B support: Service Fusion and ServiceTitan show the same one-platform-many-trades pattern.]
- Package tiering (Basic / Essentials / MAX) over the core plan; electrical-specific exclusives per tier:
  - Electrical KPI Dashboard — revenue, jobs, team performance, memberships, no setup; plus a Tech Leaderboard
  - Purchase Orders — "tied to a job's material line items", single place to manage what gets ordered, from which supplier, when
  - Credit-card surcharging with no added fees (compliance-aware payment mechanics)
  - Selling Membership Plans on jobs and estimates (one signature, one payment) — recurring-revenue sales from the field
  - Price Book Commissions — per-line-item commissions so techs are paid for what they sell
  - AI Pricing Insights (MAX) — live pricing benchmarks from jobs across the Housecall Pro community, built into the price book
  - Pipeline (MAX)
- Bundled tools listed in the package: Photo Reports (photo/video reports from the job), Checklist Automations (auto-add checklists based on tags, job fields, or line items), editable checklists on jobs, tasks on jobs/estimates, Job Splits (allocate credit across the team), Automated Sales Tax (by location and line item), marketing dashboard, QuickBooks Online sync.
- Standard tools confirmed: scheduling, estimates, invoicing, payments, online booking, reporting.
- Help center collection map (whole-product structure): Company Dashboard, Customers, Customer Portal, Employees, Franchise, Fleet Management (GPS via partner), Getting Started, Jobs / Invoices / Estimates (62 articles), Job Inbox (jobs/leads/opportunities delivered to an inbox), Leads, Pipeline, Price Book (23 articles), Scheduling, Service Plans ("Maintenance Plans, Planned Maintenance Programs, Care Clubs and Membership Plans"), HCP Payments (71 articles), Invoicing, Notifications, Reporting, Checklists, Purchase Orders, Payroll, Multi-Day Jobs Appointments, Voice, HCP Assist (AI), App Store.
- No electrical-specific structural object observed in the help center: the electrical differentiation is preconfiguration, dashboards, pricing/payment mechanics, and POs — all standard FSM objects tuned to the trade.

## Product B — Service Fusion

### Key observations

Electrical industry page (Tier 2):

- "Electrical contractor software (aka electrical job management software) may include any combination of customer management, fleet tracking, estimate creation, invoice management, and payment processing tools designed for the field service industry" — vendor's own category definition; note it is entirely generic FSM vocabulary.
- Flow claims: create estimates and jobs quickly with pre-populated product/service line items; convert estimates to jobs with one click; prioritize jobs and assign; schedule on-site visits; track call sources linked to jobs/estimates.
- Scheduling/dispatch: all jobs and estimates in one place, drag-and-drop editing, send job info to field via text or call, jobsite activity visibility.
- Mobile app (field workers): receive dispatched job and estimate assignments, map/driving directions, job photos, notes, pre-work and post-work signatures, create and send invoices for completed work.
- Customer side: customer web booking portal, automated pre-job text notifications, ServiceCall.ai (call/text management with call-reason tracking, recording/transcription), payments in the field (Stripe M2 reader; Apple Pay/Google Pay/card), homeowner financing (Acorn).
- Payments platform: credit/debit/ACH; payment history; PDF/CSV export.
- QuickBooks: bi-directional sync of customers, products, services; automatic sync of job deposits, invoices, payments.
- GPS fleet tracking built into the suite.
- The Electrical page is one of ~30 clone industry pages (HVAC, plumbing, appliance repair, locksmith, pool, roofing, …) over the same suite — trade layer as packaging.

Zendesk knowledge base (Tier 1):

- Customer accounts: unique names (with QuickBooks sync-conflict warnings), customer tags, activity feed, advanced search, batch edit/delete, merge.
- Parent/Sub-account linking: "beneficial in situations where a company owns multiple properties with their own addresses and customer information… the management company would need to be associated for billing purposes" — multi-property customers where the service location and the billing entity differ; historical data (invoices, payments) attaches to the link, so severing it affects history.
- Customer section links to "Using Equipment" (equipment records under customers) and "Customer Service Agreement Tracking" — service agreements as first-class objects.
- Featured KB articles confirm additional machinery: Estimate Options "Good/Better/Best", Progressive Billing, Recurring Invoices, Worker App Offline Capability, job completion notes (Notes+ with AI cleanup), Comprehensive Reports Dashboard, Data Import templates, Fleet Tracking 2.0 dashboard.
- Nothing electrical-specific in the KB; the KB serves all trades identically.

## Product C — Kickserv

### Key observations (evidence layer A)

- "Jobs are the heart of the Kickserv workflow. Jobs are what your technicians are completing out in the field and the main way you'll keep track of business activity."
- Jobs page is a left-to-right workflow board: Unscheduled → In Progress → Completed, with an optional On Hold column ("Jobs can skip the On Hold column").
- Job creation: service type, internal Job description ("will not be seen by the customer"), external Scope of work ("will be seen by the customer"), contact from customer records or new contact; custom data fields on Jobs (Standard plans and above, via Settings → Forms & Fields → Jobs).
- Conversion path: "Many Jobs start out as an Opportunity that turns into an estimate. Once the estimate is approved by the customer, the Opportunity transforms into an unscheduled Job!"
- Scheduling: inside the job, "Schedule work" → date/time, description for technicians, task type, assign to a specific tech (or leave unassigned and assign later) → "Add Event". So a schedule event ("work event") is a child of the job.
- Start/Stop Job buttons move it to In Progress; Mark Complete pops a confirmation: "mark all the work events on the Job as complete" — multi-visit support documented with guidance: "Depending on your industry, you might need to schedule several work events on a single job… You would want to keep the job open until all work events are completed, then send a final invoice."
- Job filters: service type, status, tag, assigned technician, time — applied on any tab.
- Recurring Jobs: "Repeat this job" → frequency, day/date, end condition → repeating jobs added to the schedule.
- Workflow ends "send an invoice… and get paid" — invoice article linked from the Jobs article.
- Other basics: Customers and Contacts, Invoices, Estimates, Reminders, Reports, Opportunities, Settings; QuickBooks two-way sync ("Our industry-leading 2-way sync with QuickBooks"); technician mobile app section.
- Trade-agnostic: nothing electrical-specific anywhere in the KB; electricians are one of many trades served.

## Product D — BuildOps

### Key observations (Tier 2, official site + FAQ)

- Positioning: "One system for the full scope of commercial electrical. From switchgear and tenant buildouts to data center installs, BuildOps connects service, projects, and financials." Explicit commercial-electrical focus ("Commercial work isn't an add-on. Most platforms started in residential and stretched to fit. BuildOps starts with the complexity of commercial work.")
- Problem/solution framing (electrical operations):
  - paper time entries / untracked materials / slow invoices → "Techs log time, parts, and photos on mobile — synced to the office the moment the work order closes."
  - wrong technician without the right certifications → "Certification-based dispatch: Match every dispatch to the right electrician based on skills, certs, and availability."
  - discovering project loss after final AIA billing → "Real-time WIP guard: Live labor and material tracking flags margin drift while the job is still active."
- Platform modules: Service Management (Work Order Closeout, Asset Management, Preventative Maintenance, Schedule & Dispatch, Purchasing & Inventory), Project Management (Field Execution, Resource Planning, Document Control, Materials & Subcontracts, Project Financials), Financials (Invoicing, Procurement & Inventory, Time Tracking), Sales & CRM (Quote to Contract, CRM, Sales Pipeline, Pull Through Work, Sales-to-Operations Handoff), plus OpsAI (AI across field/service/finance/sales; PO scanning; voice notes → structured field notes).
- Electrical FAQ specifics:
  - Asset history: "Generators, panels, replacement parts, and anything else you need is logged by techs, with full history for every job, every location, every multi-site project. You retain digital proof of all work done since day 1."
  - Customizable workflows: "Use built-in forms that contractors work through step by step on the jobsite, so electrical industry requirements and compliance are followed to the letter, and job work is closed out instantly when the workflow is completed."
  - Smart dispatch: "based on who has what skills, who's available, or who is closest to the site."
  - Reporting: "build your own reports using every single data input in the platform."
  - Service + projects on one platform: "The same board that dispatches your electrical contractors to the jobsite talks to the dashboard that covers your recurring maintenance contracts."
  - Recurring maintenance contracts; multi-location, multi-site projects.
  - ERP integration (Sage Intacct, Viewpoint Vista/Spectrum, NetSuite, QuickBooks): "BuildOps syncs field data (time tracking, POs, invoicing, etc.) directly with your ERP's job costing and payroll modules."
  - Role-based permissions (contractors, dispatchers, office admin, leadership, owners), SOC 2 compliance claim.
  - AIA billing reference (construction-style progress billing) for project work.
- Customer stories are all electrical contractors (Service 1st, Classic Electric, Jolma Electric, RBT Electric, Holmes Electric, JL Minter, Dane Electric, Layer One, Paragon).

## Product E — ServiceTitan

### Key observations (Tier 2, official site + electrical trade page)

- "AI software for commercial and residential trades"; Electrical is one of ~20 trade pages (/industries/electrical-software) over one platform.
- Platform feature map: CRM, Call Booking, Dispatch, Field Mobile App, Payments, Customer Experience, Estimates, Proposal Builder, Service Agreements, Customer Portal, Accounting, Purchasing & Inventory, Reporting, Job Costing, Client Pricing ("Automatically keep up with price changes"), Progress Billing, Crew Management, Project Management, WIP Reporting, Dynamic Forms ("Be consistent across every job with automated forms").
- Electrical trade page re-labels the same features for the trade: "Electrical Proposal Software", "Job Costing — Track job costs and grow commercial electrical profits", "Pricing — Maintain profitability with electrical pricing software", "Billing — Offer electrical customers phased billing, easy payments", "Crew Management — Manage electrical techs", "Inventory — Maintain inventory with precision for any electrical job", "Estimating — Build simple estimates that convert into profitable jobs", "WIP Reporting", "Project Management — Accurately track real-time costs, job progress, and profit margins for electrical construction projects".
- Residential-electrical vs commercial-electrical split on the same page (residential: marketing/booking/estimates/dispatch/mobile/invoicing/accounting; commercial: proposals/job costing/CRM/reporting/service agreements/pricing/client portal).
- 70+ pre-built integrations (ServiceChannel, XOi, Viewpoint Spectrum, Sage, Ferguson…).
- Customer stories from electrical contractors (Mid-America Electric, Absolute Power, Streamline Electric).
- Trade layer is labeling/tuning; the structural objects are the platform's standard ones. [Layer B: same pattern as Service Fusion's clone pages and Housecall Pro's package.]

## Cross-product Comparison

| Structure / capability | Housecall Pro | Service Fusion | Kickserv | BuildOps | ServiceTitan | Assessment |
|---|---|---|---|---|---|---|
| Customer record with service location(s) | ✓ (Customers) | ✓ (incl. parent/sub property accounts) | ✓ (Customers & Contacts) | ✓ (CRM, multi-site projects) | ✓ (CRM) | Universal — core |
| Job / work order with lifecycle | ✓ (Jobs board) | ✓ (jobs; statuses) | ✓ ("heart of the workflow"; board columns) | ✓ (work orders; closeout) | ✓ (job management) | Universal — core |
| Office→field technician coordination (dispatch) | ✓ (Employees, scheduling) | ✓ (dispatch board, text/call) | ✓ (assign tech; work events) | ✓ (Schedule & Dispatch) | ✓ (Dispatch) | Universal — core |
| Estimate/quote → approval → job conversion | ✓ (Estimates, Sales Proposals) | ✓ (one-click conversion; eSign; Good/Better/Best) | ✓ (Opportunity→estimate→Job) | ✓ (Quote to Contract) | ✓ (Proposals→agreements) | Universal — core-adjacent (standard) |
| Invoice + payment on completed work | ✓ (Invoicing, HCP Payments) | ✓ (invoices, FusionPay, deposits) | ✓ (Invoices; "get paid") | ✓ (Invoicing, Payments+) | ✓ (Invoicing, Payments) | Universal — core |
| Technician mobile app (photos/notes/signatures/payment) | ✓ (mobile-only features; Photo Reports) | ✓ (dispatch receipt, photos, notes, pre/post signatures, invoices) | ✓ (mobile app; technicials section) | ✓ (time/parts/photos at closeout) | ✓ (Field Mobile App) | Universal — standard |
| Price book / line-item pricing | ✓ (Price Book; commissions; AI pricing insights) | ✓ (pre-populated line items; Flat Rate integration) | ✓ (estimates/service types) | ✓ (materials; parts logging) | ✓ (Client Pricing; Pricebook Pro) | Universal — standard |
| Customer notifications | ✓ (Notifications) | ✓ (pre-job texts; booking portal) | ✓ (Reminders) | ✓ (implied) | ✓ (Customer Experience) | Universal — standard |
| Multi-visit jobs / work events | ✓ (Multi-Day Jobs Appointments) | ✓ (scheduling; visits) | ✓ (explicit: several work events per job; keep open → final invoice) | ✓ (jobs span days/projects) | ✓ (project phases) | Universal — standard |
| Recurring work (service plans / memberships / agreements) | ✓ (Service Plans; membership selling) | ✓ (Recurring Invoices; Service Agreement Tracking) | ✓ (Recurring Jobs) | ✓ (Preventative Maintenance; recurring maintenance contracts) | ✓ (Service Agreements) | Universal — standard |
| Reporting / dashboards | ✓ (Reporting; Electrical KPI Dashboard) | ✓ (Reports Dashboard) | ✓ (Reports) | ✓ (custom dashboards; WIP) | ✓ (Reporting; WIP) | Universal — standard |
| Accounting / ERP sync | ✓ (QuickBooks Online; QBD) | ✓ (QuickBooks bi-directional) | ✓ (QuickBooks 2-way) | ✓ (ERP: Sage, Viewpoint, NetSuite, QB) | ✓ (Accounting; 70+ integrations) | Universal — standard |
| Equipment / asset records per site | — (not in fetched docs) | ✓ ("Using Equipment" KB) | — | ✓ (panels, generators, switchgear with per-location history) | ✓ (implied via asset history claims? not fetched — treat cautiously) | Optional; commercial pole stronger |
| Purchasing / POs / inventory | ✓ (Purchase Orders in Electrical Package; PO collection) | ✓ (Inventory Management Dashboard) | — (not observed) | ✓ (Purchasing & Inventory; PO scanning) | ✓ (Purchasing & Inventory) | Common/optional |
| Job costing / WIP / profitability | ✓ (marketing dashboards; KPIs) | ✓ (financial attributes in customer history) | — (lighter) | ✓ (real-time WIP guard) | ✓ (Job Costing; WIP Reporting) | Optional; commercial pole |
| Project machinery (bids, document control, subcontracts, progress billing) | — (light: proposals) | ✓ (Progressive Billing) | — | ✓ (full project suite; AIA billing) | ✓ (Project Management; Progress Billing) | Optional; commercial pole only |
| Certification/skills-aware dispatch | — | — | — | ✓ (certification-based dispatch) | — | Product-specific (BuildOps) |
| Compliance forms/workflows on jobs | ✓ (Checklists automations — generic) | — | ✓ (custom fields/forms — generic) | ✓ ("electrical industry requirements and compliance" via built-in forms) | ✓ (Dynamic Forms — generic) | Common as generic forms; electrical-specific framing only BuildOps |
| GPS fleet tracking | ✓ (Fleet Management, partner-powered) | ✓ (built-in) | — | ✓ (Fleet+ add-on) | ✓ (Fleet Pro) | Optional |
| Payroll / time tracking | ✓ (Payroll) | ✓ (implied via KB? not fetched — cautious) | — | ✓ (Time Tracking; payroll sync) | ✓ (Crew Management) | Optional |
| Customer self-service (portal / booking / financing) | ✓ (Customer Portal; online booking) | ✓ (web booking portal; Acorn financing) | — | — | ✓ (Customer Portal; financing) | Optional |
| AI assistants | ✓ (HCP Assist; AI Pricing Insights) | ✓ (Notes+ note cleanup; AI call answering) | — | ✓ (OpsAI) | ✓ (AI Virtual Agent; Atlas) | Optional; era-typical |
| Trade layer realization | explicit "Electrical Package… preconfigured" | Electrical page over suite | none (trade-agnostic) | commercial-electrical product identity | Electrical trade page over platform | The Type's packaging pattern |

### What is actually electrical-specific (across sample)

1. **Trade-tuned packaging and configuration** — all sampled multi-trade vendors sell "electrical" as a preconfigured variant of one platform (Housecall Pro's own words). [Layer A ×3 vendors]
2. **Electrical-tuned pricing and sales mechanics** — price book commissions, flat-rate pricing integrations, pricing benchmarks, material-markup content (ServiceTitan publishes electrical material-markup guides), phased billing for electrical customers. [Layer A/B]
3. **Commercial electrical machinery** — certification-based dispatch, panel/switchgear/generator asset histories, electrical compliance forms, project/AIA billing (BuildOps). [Layer A, product-specific to BuildOps for certs and compliance framing; asset records also in Service Fusion KB as generic equipment]
4. **Electrical-branded dashboards** (KPI dashboard). [Layer A, Housecall Pro]

No sampled product showed a *structurally distinct* electrical object (no permit registry, no load-calculation object, no code-compliance engine) in reachable documentation. The trade difference is configuration + content + a few trade-specific features, not a different data model.

## Canonical Model

### Level 0 — Defining Invariant (deliberately minimal)

1. **Customer with a service location** — work is performed at the customer's premises (home, building, facility), so jobs bind to addresses; the customer may be a person, a business, or a property-management hierarchy.
2. **Electrical job (work order)** — a requested piece of electrical work (service call, repair, installation, or larger project) at that location, carried through a managed lifecycle (requested → scheduled → assigned → performed → completed → billed).
3. **Electrician / field technician as the executing role** — jobs are assigned to field workers and coordinated by the office (scheduling/dispatch).
4. **Billing of completed work** — the job produces an invoice that collects payment (estimate/quote upstream of larger work).

Remove the customer/location → generic task tracking. Remove the job lifecycle → an address book or invoicing tool. Remove technician coordination → pure invoicing. Remove billing → a dispatch board only. Remove "electrical work" as the job's content → the generic Small Business Field Service Management Type.

Historical check: a paper-era electrical contractor (job tickets, a dispatch board, a price book, invoices) satisfies all four properties; 1990s–2000s dedicated field-service products for electrical contractors satisfy them; trade-agnostic products configured by an electrical business satisfy them. None of the modern machinery (mobile apps, GPS, memberships, portals, cert-tracking, AI) is definitional. The check passes.

### Level 1 — Common Mature Structure

- Estimates/quotes with multiple options, customer approval (often e-signature), conversion into jobs
- Scheduling calendar + dispatch board; assignment of technicians; arrival windows
- Technician mobile app: assigned jobs, navigation, job details/history, photos, notes, signatures, on-site payment, invoice creation
- Price book: services and materials with prices; flat-rate pricing entries common in the trade
- Customer notifications: booking confirmations, day-of reminders, on-my-way, invoice delivery
- Multi-visit jobs (several work events/appointments on one job; job stays open until visits complete)
- Recurring work: recurring jobs, service plans/memberships/service agreements
- Reporting: jobs, revenue, technician performance; job filters/tags/custom fields
- Accounting sync (QuickBooks in the North American SMB market; ERPs at the commercial pole)

### Level 2 — Variant / Optional Structure

- Site equipment/asset records (panels, generators, switchgear) with per-location service history — commercial pole
- Purchase orders tied to job material lines; material purchasing; inventory
- Certification/skills-aware dispatch — product-specific today
- Compliance/documentation form workflows on jobs
- Job costing / WIP / profitability reporting; progress/phased billing — commercial pole
- Customer self-service: booking pages, portals, financing
- GPS fleet tracking; payroll/time tracking; marketing/review management; call tracking/VoIP
- Parent/sub-account customer hierarchies (property-management billing)
- Franchise/multi-location structures; AI assistants (era-typical)

### Level 3 — Vendor-specific (kept out of the canonical document)

- Housecall Pro: fee-free surcharging, AI Pricing Insights (community benchmarks), Job Splits, Tech Leaderboard, Electrical KPI Dashboard
- Service Fusion: ServiceCall.ai VoIP/call tracking, Notes+ AI note cleanup, Acorn homeowner financing, built-in GPS fleet tracking
- BuildOps: OpsAI (role-specific AI), PO scanning, voice-note-to-field-notes, WIP guard
- ServiceTitan: Pro product tier (Pricebook/Dispatch/Fleet Pro…), Convex sales prospecting, Atlas
- Kickserv: "Opportunity" object naming for the pre-estimate stage

## Vendor-specific Findings

See Level 3. Also: Housecall Pro is the only sampled vendor that explicitly documents an "Electrical Package" with tier-gated electrical exclusives; BuildOps is the only sampled vendor whose product identity is commercial-electrical (with certification dispatch and electrical compliance forms); Service Fusion and ServiceTitan both realize the trade as marketing/configuration pages over one suite; Kickserv demonstrates the trade-agnostic pole (the same structure serves electricians without any electrical awareness).

## Boundary Findings

1. **vs Small Business Field Service Management** — the structural spine is identical (customer+location → job lifecycle → technician dispatch → invoice/payment; verified across five products). Vendors themselves ship "electrical" as a preconfigured trade layer of one product (Housecall Pro: "preconfigured" package; Service Fusion: ~30 clone industry pages; ServiceTitan: ~20 trade pages). Probable trade-Variant relationship rather than two independent Types — consistent with the appliance-repair-management and cleaning-business-management passes; the durable difference is trade semantics (electrical work content, electrical pricing mechanics, commercial electrical machinery). Joint review with Small Business Field Service Management recommended.
2. **vs HVAC Service Management / Plumbing Business Management (trade siblings, unprocessed)** — same family pattern; the trade wrapper differs, the spine does not. Cross-reference recommended when those leaves are processed.
3. **vs Appliance Repair Management (processed)** — appliance repair's distinguishing object is the customer's appliance as the unit of repair; here the unit of work is electrical work in the building's electrical system (service/repair/install/project), with site electrical infrastructure (panels, generators) as an optional asset record rather than the defining object.
4. **vs Construction Project Management (§17, processed)** — commercial electrical contractors run installation *projects* (tenant buildouts, data centers); sampled commercial-pole products bundle project machinery (bids/quotes-to-contract, document control, subcontracts, WIP, AIA-style progress billing). The service-management center remains the dispatched service loop (job → tech → invoice); project machinery belongs to the construction side. Convergence at the commercial pole noted as drift, not identity.
5. **vs Utility Field Service Management (§19)** — utility-side workforce dispatch against grid/network assets owned by the software operator's organization vs contractor-side business management of an electrical service company serving customers. Different operator, different object, different money flow.
6. **vs Appointment Scheduling Application** — booking is one fragment (customer self-service booking exists in several products); this Type is the whole business operation.
7. **vs Local Service Marketplace** — demand-side discovery/booking vs operator-side execution and billing; a marketplace lead becomes a job here.
8. **vs CMMS / Enterprise Asset Management** — CMMS/EAM manages assets owned by the operator; this Type manages service work performed at customers' premises. The site-equipment record (panels, generators) is a customer-owned asset registry, not an owned-asset registry.
9. **vs Fire Protection Service Management / Elevator Service Management (§26 trade siblings, unprocessed)** — expected same family pattern; cross-reference when processed.

## Uncertainties

1. **Permit/inspection tracking for electrical work** — strongly suspected in the trade (permits/AHJ coordination are standard electrical-contractor practice), but no fetched document showed a dedicated permit object; BuildOps only documents "electrical industry requirements and compliance" via generic form/workflow machinery. Not claimed in the canonical document.
2. **Load calculations / electrical-code references as software objects** — not observed in any fetched source; not claimed.
3. **Certification-aware dispatch** — single-product evidence (BuildOps); marked product-specific/optional, not canonical.
4. **ServiceTitan operational depth** — only Tier 2 marketing pages were reachable; no help-center detail fetched this pass, so ServiceTitan claims are limited to what its site states.
5. **Jobber** — major SMB player serving electricians; inaccessible (403 ×2). Market-coverage gap acknowledged; assertions calibrated to the five researched products.
6. **Regional markets** — the sample is North America–dominant (QuickBooks-centrism, US payment/financing mechanics). Regional variance (e.g., UK/EU electrical certification paperwork) could not be verified; the canonical document avoids region-specific claims.

## Final Synthesis

Electrical Service Management is the business-management system of an electrical service company: it records customers and their service locations, carries each requested piece of electrical work as a durable job with a lifecycle, coordinates the electricians who perform the work in the field, and turns completed work into invoices and payments. The defining core is the field-service spine with electrical work as the job's content; everything electrical-flavored beyond that (electrical pricing mechanics, electrical KPI dashboards, panel/asset histories, certification-aware dispatch, compliance forms, project machinery at the commercial pole) is trade tuning layered on a shared structure that vendors themselves ship as one platform configured per trade. The leaf is best understood as the electrical trade instantiation of the field-service-management family — a distinct directory leaf by trade semantics, with a probable trade-Variant relationship to Small Business Field Service Management that should be ratified in joint review.
