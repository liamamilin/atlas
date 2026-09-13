# Research Notes — Garage Door Service Management

Research date: 2026-09-08
Leaf: Garage Door Service Management (DIRECTORY.md §29 Home, Family, Personal & Local Services — trade-business cluster)
Slug: garage-door-service-management

## Research Goal

Understand what "Garage Door Service Management" software actually is in the real market: what objects it manages, how garage door work flows through it, what is garage-door-trade-specific versus generic field-service structure, and where its boundaries lie with neighboring Application Types (generic small-business field service management, trade siblings like HVAC/electrical/appliance repair, fire protection and elevator service with their compliance loops, construction project management, yard/warehouse management).

Family context carried into this pass: the fire-protection-service-management pass found a structurally distinct trade object (code-mandated recurring inspection program + persistent deficiencies + outward compliance reporting), while the electrical pass found none (trade difference = configuration/content over the generic FSM spine). The open question for garage door: does the trade carry a structurally distinct object (door catalogs, door-measurement/spec records, warranty objects, inspection loops), or is it a trade-tuned variant of the field-service spine?

## Initial Boundary

Working hypothesis at start:

- It is the business-management system of a garage door / overhead door service company (residential service and replacement, commercial overhead and dock-door service).
- Core objects likely: customer + service location, job/work order with lifecycle, estimate, schedule/dispatch, technician/installer, invoice/payment, price book.
- Trade-specific candidates to test: door/openers as installed equipment records, door product catalogs and quoting, door measurements/specifications, warranty tracking, spring/parts inventory, commercial preventive-maintenance agreements.
- Closest neighbors: Small Business Field Service Management (likely the same structural spine), trade siblings, Fire Protection / Elevator Service Management (compliance-loop siblings), Construction Project Management (commercial install projects), Yard Management / Warehouse software (name collision on "dock").

## Research Questions

1. What objects make up the system (customer, location, job, estimate, appointment/visit, technician, equipment, invoice, payment, price book)?
2. How does garage door work flow from inquiry to payment? What is the work mix (service call, repair, door/opener replacement-install, commercial maintenance)?
3. What is garage-door-specific in the market: door/openers product sales, door catalogs/specs, equipment records, warranty, install phases, commercial PM agreements?
4. How do scheduling and dispatch work across products?
5. How does the residential pole differ from the commercial overhead/dock-door pole?
6. What recurring-work machinery exists (maintenance plans, agreements)?
7. Which interfaces do users actually operate (office dashboard, schedule, job detail, mobile app, customer-facing surfaces)?
8. Historical check: would older, regional, trade-agnostic, or paper-era operations still fit a minimal definition?

## Representative Products

Selected for market representation + documentation access + different product philosophies + different customer layers:

| Product | Segment / philosophy | Evidence tier |
|---|---|---|
| ServiceTitan | flagship "software for the trades"; residential Garage Door trade page + separate commercial Dock & Door trade page over one platform | Tier 2 (site + trade pages) |
| Service Fusion | SMB–mid; all-in-one multi-trade suite with a dedicated "Overhead & Garage Door" industry page (~29 clone industry pages over one product) | Tier 2 (product page) |
| FieldPulse | growing SMB; workflow-configuration philosophy; dedicated Garage Door solution page; overhead-door customer story | Tier 2 (site + garage door page) |
| Kickserv | micro-SMB; simple, low-cost, trade-agnostic service business management | Tier 1 (knowledge center) |
| Housecall Pro | micro-SMB residential home services; help center documents industry packages for HVAC/Electrical/Plumbing only — demonstrates garage door companies running the generic platform | Tier 1 (help center) |

Attempted and abandoned per source-access rules: Successware (garage-door-dealer-heritage mid-market product; root URL WAF-rejected), XOLogic (suspected garage-door-dealer software; 403), Housecall Pro garage door marketing page (403; help center used instead), Jobber (403 ×2 in the electrical pass; not retried).

## Sources

Fetched 2026-09-08:

- ServiceTitan (Tier 2): https://www.servicetitan.com/industries/garage-door-software — Garage Door trade page; https://www.servicetitan.com/industries/dock-and-door-software — commercial Dock & Door trade page (supplementary, same vendor)
- Service Fusion (Tier 2): https://www.servicefusion.com/garage-door-software — "Overhead & Garage Door" industry page with FAQ
- FieldPulse (Tier 2): https://www.fieldpulse.com/ — platform map; https://www.fieldpulse.com/solutions/garage-door — Garage Door solution page
- Kickserv (Tier 1): https://kickserv.helpscoutdocs.com/article/32-jobs — "Jobs" article (Kickserv Knowledge Center)
- Housecall Pro (Tier 1): https://help.housecallpro.com/en/ — help-center collection map incl. "Industry Packages" collection description

## Product A — ServiceTitan

### Key observations (evidence layer A unless noted)

- Garage Door is one of ~20 residential trade pages over one platform (same one-platform-many-trades pattern as the electrical pass observed). [Layer B support: Service Fusion and FieldPulse show the same pattern.]
- Residential pole features re-labeled for the trade: Call Booking, Estimates ("multi-option estimates… close more garage door installation jobs at a higher average ticket"), Scheduling, Mobile App ("garage door service techs… complete customer history… multi-option estimate templates… payment processing workflow in the field"), Invoicing ("get paid sooner with residential garage door software"), Accounting (QuickBooks Online + Desktop), Marketing, Customer Experience.
- Installers named alongside techs: "updates from your garage door installation team, such as estimates, invoices, credit card payments, and more, automatically appear on the office side."
- Dispatch: "Dispatchers get pop-up reminders to assure a technician's skills match the job's requirements."
- Commercial pole (same page): Proposal Builder ("multi-option proposals… automatically convert to agreements as soon as your commercial customer signs"), Service Agreements ("roll up automation for commercial garage door agreements"), Pricing ("price commercial garage jobs accurately and profitably"), Client Portal, Project Tracking, Crew Management, Inventory, Dynamic Forms, WIP Reporting.
- Customer story: A1 Garage Door Service (revenue growth claim).
- No garage-door-specific structural object on the page; the trade layer is labeling + tuning of platform features.

### Supplementary — ServiceTitan Dock & Door page (commercial overhead/dock-door pole, same vendor)

- Category definition: "business management software built for contractors who install, service, and maintain commercial doors, loading docks, and access systems."
- Trade-built features: Equipment Scanning ("Automated Equipment Scanning & Asset Tracking"); "Gain complete asset history, from warranty status to past repairs"; skill/certification/territory-based dispatch matching; Projects ("Manage Dock & Door Installation Projects"); "Customizable Dock & Door Checklists"; Maintenance Plans ("Streamlined Preventive Maintenance Agreements"); Customer Portal ("24/7 Access to Jobs, Invoices & Equipment").
- FAQ: work order management "with customizable job types and phases"; "preventive maintenance scheduling and asset tracking for doors, docks, and lifts"; commercial maintenance contracts (service agreements → scheduled preventive maintenance → work orders → job history/parts/labor → billing/reporting).
- Explicit vendor-drawn boundary: "Is Dock & Door software different from Yard Management or Warehouse software? Yes. Dock & Door software focuses specifically on managing door-level operations… rather than managing warehouse inventory or yard logistics."

## Product B — Service Fusion

### Key observations (evidence layer A)

- "Overhead & Garage Door" is one of ~29 clone industry pages (HVAC, plumbing, electrical, appliance repair, locksmith, pool, …) over the same suite — trade layer as packaging.
- FAQ category definition: "Overhead & garage door software (aka garage door management software) may include any combination of payment processing, fleet tracking, job management, inventory management, estimate creation, invoice management, and customer management tools designed for the field service industry" — entirely generic FSM vocabulary.
- Flow: estimates and jobs "in seconds with pre-populated products, service line items"; scheduling & dispatching with overlap avoidance; mobile app (job/estimate assignments, map/directions, job photos, notes, inventory check, add products to jobs, invoices, payments via Stripe M2 reader, pre/post-work signatures).
- Customer side: automated pre-job text notifications, customer web booking portal, ServiceCall.ai VoIP (call/text, call-reason tracking, recording/transcription).
- QuickBooks bi-directional sync (customers, products, services; job deposits, invoices, payments); GPS fleet tracking built in.
- Pricing FAQ mentions "residential and commercial overhead & garage door software" — both poles served by the same product.
- Nothing garage-door-specific in structure; the page is the generic suite with trade wording.

## Product C — FieldPulse

### Key observations (evidence layer A)

- Dedicated Garage Door solution page; footer: "Garage and Overhead Door Business Software."
- FAQ definition: "Garage door business software helps garage door companies manage scheduling, dispatching, customer information, invoicing, and payments, all in one place" — again generic FSM vocabulary.
- Trade-labeled platform sections: Garage Door Scheduling ("schedule jobs on a visual calendar, dispatch the right techs"; drag-and-drop; GPS tracking; "dispatch the closest crew"); Garage Business Project Management ("Break down installs, repairs, or tune-ups into clear phases that guide your crews from start to finish"; timeline tracking; crew/task coordination; material and cost tracking); Garage Door CRM (full customer profiles, job history, automated follow-ups); Garage Door Invoicing (built-in pricebook with pre-set labor and material rates; estimates converted to invoices with one click; card/mobile payments); Garage Door Reporting (job profitability: "which garage door installs, repairs, or maintenance jobs are most profitable"); Garage Door Field Service App (on-site estimates, add-ons, payments).
- Product imagery alt-text: dispatch card for a "Garage Door Installation" with On-The-Way state; estimate for a residential garage door job with itemized line items; project record for a garage door job with related jobs and a completion-percentage slider; homepage job card "Garage Door Replacement."
- Platform features beyond the trade page: work order/job management, estimates & invoices with Good/Better/Best options, pricebook, project management, maintenance agreements, customer portal, booking portal, custom forms, asset management, inventory, fleet tracking, Operator AI (24/7 AI dispatching), ClearPath (guided job-stage workflows).
- Customer story: J.A.G. & Sons Overhead Door.
- No garage-door-specific structural object; trade layer is labeling + the install-phases framing.

## Product D — Kickserv

### Key observations (evidence layer A, Tier 1)

- "Jobs are the heart of the Kickserv workflow. Jobs are what your technicians are completing out in the field and the main way you'll keep track of business activity."
- Jobs page: left-to-right workflow board Unscheduled → In Progress → Completed, with optional On Hold column ("Jobs can skip the On Hold column").
- Job creation: service type, internal job description ("will not be seen by the customer"), external scope of work ("will be seen by the customer"), contact from customer records; custom data fields on jobs (Standard plans and above).
- Conversion path: "Many Jobs start out as an Opportunity that turns into an estimate. Once the estimate is approved by the customer, the Opportunity transforms into an unscheduled Job!"
- Scheduling: inside the job, "Schedule work" → date/time, description for technicians, task type, assign tech (or leave unassigned) → "Add Event" — a work event is a child of the job.
- Start/Stop Job buttons move it to In Progress; Mark Complete pops a confirmation to mark all work events complete; multi-visit guidance: "Depending on your industry, you might need to schedule several work events on a single job… keep the job open until all work events are completed, then send a final invoice."
- Recurring Jobs: "Repeat this job" → frequency, day/date, end condition → repeating jobs added to the schedule.
- Workflow ends "send an invoice… and get paid."
- Trade-agnostic: nothing garage-door-specific anywhere; garage door companies are among the trades served.

## Product E — Housecall Pro

### Key observations (evidence layer A, Tier 1 — help-center collection map)

- "Industry Packages: Learn about industry-specific Housecall Pro packages for HVAC, Electrical, and Plumbing Pros" (4 articles) — no garage door package documented. Garage door companies run the generic platform.
- Whole-product structure (generic): Company Dashboard, Customers, Customer Portal, Employees, Franchise, Fleet Management, Jobs / Invoices / Estimates (62 articles), Job Inbox (jobs/leads/opportunities delivered to an inbox), Leads, Pipeline, Price Book (23 articles), Scheduling, Service Plans ("Maintenance Plans, Planned Maintenance Programs, Care Clubs and Membership Plans"), Payments (71 articles), Invoicing, Notifications, Reporting, Checklists, Purchase Orders, Payroll, Multi-Day Jobs Appointments, Voice, HCP Assist (AI), App Store.
- Confirms the trade-agnostic pole: the same structure that serves electricians serves garage door companies without any garage-door awareness.

## Cross-product Comparison

| Structure / capability | ServiceTitan | Service Fusion | FieldPulse | Kickserv | Housecall Pro | Assessment |
|---|---|---|---|---|---|---|
| Customer record with service location | ✓ (CRM) | ✓ | ✓ (CRM, customer sites) | ✓ (Customers & Contacts) | ✓ (Customers) | Universal — core |
| Job / work order with lifecycle | ✓ (job management) | ✓ (jobs) | ✓ (work order/job management) | ✓ ("heart of the workflow"; board) | ✓ (Jobs) | Universal — core |
| Office→field technician coordination (dispatch) | ✓ (Dispatch; skill-match reminders) | ✓ (scheduling & dispatching) | ✓ (dispatch map, GPS) | ✓ (assign tech; work events) | ✓ (Employees, scheduling) | Universal — core |
| Estimate/quote → approval → job conversion | ✓ (multi-option estimates; proposals→agreements) | ✓ (pre-populated line items) | ✓ (estimates→invoice one click; Good/Better/Best) | ✓ (Opportunity→estimate→Job) | ✓ (Estimates, Sales Proposals) | Universal — core-adjacent (standard) |
| Invoice + payment on completed work | ✓ (Invoicing, Payments) | ✓ (invoices, FusionPay, Stripe reader) | ✓ (FieldPulse Payments) | ✓ (Invoices; "get paid") | ✓ (Invoicing, HCP Payments) | Universal — core |
| Technician/installer mobile app | ✓ (Mobile 2.0) | ✓ (photos, notes, signatures, payments, inventory) | ✓ (job details, on-site estimates/payments) | ✓ (mobile app section) | ✓ (mobile-only features) | Universal — standard |
| Price book / line-item pricing | ✓ (Pricing; Pricebook Pro tier) | ✓ (pre-populated line items) | ✓ (built-in pricebook) | ✓ (service types) | ✓ (Price Book) | Universal — standard |
| Customer notifications | ✓ (Customer Experience) | ✓ (pre-job texts; booking portal) | ✓ (reminders, arrival updates, follow-ups) | ✓ (Reminders) | ✓ (Notifications) | Universal — standard |
| Multi-visit jobs / work events | ✓ (job types and phases) | ✓ (scheduling; visits) | ✓ (job phases; project with related jobs) | ✓ (explicit: several work events per job) | ✓ (Multi-Day Jobs Appointments) | Universal — standard |
| Install/replacement work as a job class | ✓ ("garage door installation jobs"; installers) | ✓ (implied; estimates→jobs) | ✓ (installs/repairs/tune-ups in phases; "Garage Door Installation"/"Replacement" job cards) | — (generic jobs) | — (generic jobs) | Common — trade-typical work mix |
| Multi-option estimates to raise ticket | ✓ (explicit) | — | ✓ (Good/Better/Best) | — | ✓ (Sales Proposals) | Common |
| Recurring work (plans/agreements) | ✓ (Service Agreements; commercial garage door agreements) | ✓ (recurring invoices; agreements in KB per electrical pass) | ✓ (Maintenance Agreements) | ✓ (Recurring Jobs) | ✓ (Service Plans) | Universal — standard |
| Equipment/asset records with history | ✓ (Dock & Door: asset history incl. warranty status; equipment scanning) | ✓ (equipment records in KB — generic) | ✓ (Asset Management platform feature) | — | — | Optional; commercial pole stronger |
| Preventive maintenance agreements (commercial) | ✓ (Dock & Door PM agreements) | — | ✓ (Maintenance Agreements) | — | ✓ (Service Plans) | Common/optional |
| Project machinery (phases, budgets, WIP) | ✓ (Project Tracking; WIP) | ✓ (Progressive Billing per electrical-pass KB) | ✓ (Project Management; material/cost tracking) | — | — (light) | Optional; commercial pole |
| Purchasing / inventory | ✓ (Purchasing & Inventory) | ✓ (inventory check in app) | ✓ (Inventory Management) | — | ✓ (Purchase Orders) | Common/optional |
| GPS fleet tracking | ✓ (Fleet Pro) | ✓ (built-in) | ✓ (Fleet Tracking) | — | ✓ (Fleet Management) | Optional |
| Accounting sync | ✓ (QuickBooks; ERPs) | ✓ (QuickBooks bi-directional) | ✓ (QuickBooks-class integrations) | ✓ (QuickBooks 2-way) | ✓ (QuickBooks Online/Desktop) | Universal — standard |
| Reporting / dashboards | ✓ (Reporting) | ✓ (Reports Dashboard) | ✓ (job profitability reports) | ✓ (Reports) | ✓ (Reporting) | Universal — standard |
| Certification/skills-aware dispatch | ✓ (skill-match pop-ups; Dock & Door certs/territories) | — | — | — | — | Product-specific (ServiceTitan) |
| AI assistants | ✓ (AI Virtual Agent; Atlas) | ✓ (AI call answering; Notes+) | ✓ (Operator AI) | — | ✓ (HCP Assist) | Optional; era-typical |
| Trade layer realization | Garage Door + Dock & Door trade pages over one platform | "Overhead & Garage Door" clone page over suite | Garage Door solution page over platform | none (trade-agnostic) | no garage door package (generic platform) | The Type's packaging pattern |

### What is actually garage-door-specific (across sample)

1. **Trade-tuned packaging and configuration** — all sampled multi-trade vendors sell "garage door" (or "overhead & garage door") as a labeled variant of one platform; Housecall Pro documents no garage door package at all, demonstrating that the generic platform serves the trade. [Layer A ×4 vendors]
2. **The work mix: service + repair + door/opener replacement-installation** — install/replacement jobs are a named, ticket-raising job class ("close more garage door installation jobs at a higher average ticket"; "installs, repairs, or tune-ups"; "Garage Door Replacement" job card); installers named alongside technicians. [Layer A ×3 vendors]
3. **Multi-option estimates as the trade's sales motion** — multi-option estimate/proposal builders to raise average ticket on door replacement. [Layer A ×2 vendors]
4. **Commercial overhead/dock-door machinery** — equipment/asset records with warranty status and repair history, equipment scanning, preventive maintenance agreements, installation projects with phases (ServiceTitan Dock & Door; FieldPulse asset management + maintenance agreements + projects). [Layer A; commercial pole]

No sampled product showed a *structurally distinct* garage-door object in reachable documentation: no door catalog/product configurator, no door-measurement/spec record, no spring-sizing object, no code-mandated inspection/deficiency loop. The trade difference is configuration + content + the install-heavy work mix, not a different data model.

## Canonical Model

### Level 0 — Defining Invariant (deliberately minimal)

1. **Customer with a service location** — work is performed at the customer's premises (home, building, warehouse, storefront), so jobs bind to addresses; the customer may be a person, a business, or a property hierarchy.
2. **Garage door job (work order)** — a requested piece of garage door work (service call, repair, door or opener replacement/installation, or commercial door maintenance) at that location, carried through a managed lifecycle (requested → scheduled → assigned → performed → completed → billed).
3. **Door technician / installer as the executing role** — jobs are assigned to field workers and coordinated by the office (scheduling/dispatch).
4. **Billing of completed work** — the job produces an invoice that collects payment (estimate/quote upstream of larger work).

Remove the customer/location → generic task tracking. Remove the job lifecycle → an address book or invoicing tool. Remove technician coordination → pure invoicing. Remove billing → a dispatch board only. Remove "garage door work" as the job's content → the generic Small Business Field Service Management Type.

Historical check: a paper-era garage door company (job tickets, a dispatch board, a door price list, invoices) satisfies all four properties; 1990s–2000s dedicated field-service products satisfy them; trade-agnostic products configured by a garage door business satisfy them (Kickserv and Housecall Pro demonstrate the trade-agnostic pole directly). None of the modern machinery (mobile apps, GPS, memberships, portals, asset scanning, AI) is definitional. The check passes.

### Level 1 — Common Mature Structure

- Estimates/quotes with line items — commonly multiple priced options in this trade — customer approval, conversion into jobs
- Scheduling calendar + dispatch board; assignment of technicians/installers; GPS-backed status views in mature products
- Technician mobile app: assigned jobs, navigation, job details/history, photos, notes, signatures, on-site payment, invoice creation
- Price book: services, parts, and door/openers with prices
- Customer notifications: booking confirmations, day-of reminders, on-my-way alerts, invoice delivery
- Multi-visit jobs (diagnosis visit, return with parts, phased installation)
- Recurring work: recurring jobs, maintenance plans/service agreements
- Reporting: jobs, revenue, technician performance, job profitability
- Accounting sync (QuickBooks in the North American SMB market)

### Level 2 — Variant / Optional Structure

- Site equipment/asset records (doors, openers, dock equipment) with per-location service history and warranty status — commercial pole
- Preventive maintenance agreements for commercial door programs
- Installation project machinery (phases, budgets, material/cost tracking, WIP) — commercial pole
- Purchase orders / parts inventory / truck stock
- Certification/skills-aware dispatch — product-specific today
- Customer self-service: booking pages, portals, financing
- GPS fleet tracking; payroll/time tracking; marketing/review management; VoIP/call tracking
- Franchise/multi-location structures; AI assistants (era-typical)

### Level 3 — Vendor-specific (kept out of the canonical document)

- ServiceTitan: Pro product tiers (Pricebook/Dispatch/Fleet Pro…), Atlas, Convex sales prospecting, skill-match dispatch pop-ups, Dock & Door equipment scanning, A1 Garage Door growth claims
- Service Fusion: ServiceCall.ai VoIP/call tracking, Notes+ AI note cleanup, Acorn homeowner financing, built-in GPS, Stripe M2 reader specifics, "1,000% ROI" fleet claims
- FieldPulse: Operator AI (24/7 AI dispatching), ClearPath guided job-stage workflows, Engage VoIP, Field Intelligence, 78% revenue-growth claim
- Kickserv: "Opportunity" object naming for the pre-estimate stage
- Housecall Pro: HCP Assist, HCP Payments/Payroll module names, Job Inbox

## Vendor-specific Findings

See Level 3. Notable patterns: ServiceTitan is the only sampled vendor that ships a separate commercial trade page (Dock & Door) alongside the residential Garage Door page — evidence that the market splits the trade's residential and commercial poles at the marketing level while running them on one platform. Housecall Pro is the counter-example that proves the trade layer is optional: its help center documents industry packages only for HVAC/Electrical/Plumbing, so garage door companies run the undifferentiated product.

## Rejected Findings

1. **Door catalogs / product configurators as a defining object** — suspected in the trade (door dealers quote by model/size), but no fetched source documented a door catalog or configurator object. Rejected as canonical; recorded as an uncertainty.
2. **Door-measurement/specification records** (width/height, spring type, track size) — not observed in any fetched source. Not claimed.
3. **Warranty as a distinct managed object** — only "warranty status" appears as an attribute of asset history in one vendor's commercial-pole claims (ServiceTitan Dock & Door). Held as an optional attribute, not an object.
4. **Code-mandated inspection/deficiency loop (fire-protection-style)** — no evidence anywhere in the sample; garage door work is not organized around a compliance inspection program in any fetched source. Rejected.
5. **"Overhead door" as a separate Type from "garage door"** — the market uses the labels interchangeably (Service Fusion: "Overhead & Garage Door"; FieldPulse: "Garage and Overhead Door"); one trade, one Type.

## Boundary Findings

1. **vs Small Business Field Service Management** — the structural spine is identical (customer+location → job lifecycle → technician coordination → invoice/payment; verified across five products). Vendors ship "garage door" as a preconfigured trade layer of one product (ServiceTitan trade page; Service Fusion clone page; FieldPulse solution page), and Housecall Pro demonstrates the trade running with no trade layer at all. Probable trade-Variant relationship rather than two independent Types — consistent with the electrical, cleaning, and appliance-repair passes; the durable difference is trade semantics (door/openers work content, install-heavy work mix, multi-option estimate sales motion, commercial door machinery). Joint review with Small Business Field Service Management recommended.
2. **vs trade siblings (HVAC, plumbing, electrical, appliance repair, locksmith)** — same family pattern; the trade wrapper differs, the spine does not. Cross-reference when those leaves are processed.
3. **vs Fire Protection Service Management / Elevator Service Management** — those siblings carry a structurally distinct trade object (code-mandated recurring inspection program, persistent deficiencies, compliance reporting). Garage door shows no such loop in any fetched source; it is a trade-tuned variant like electrical, not a compliance-loop trade like fire protection. This resolves the fire-protection pass's family question for this leaf from this side.
4. **vs Appliance Repair Management** — appliance repair's distinguishing object is the customer's appliance as the unit of repair; here the unit of work is the door/opening system installed in the building (service, repair, replacement-installation), with installed doors/openers appearing as optional site-equipment records rather than the defining object.
5. **vs Construction Project Management (§17)** — commercial door installation (dock systems, sectional/rolling doors at scale) is project work; commercial-pole products bundle project machinery (phases, budgets, WIP). The service-management center remains the dispatched service loop; project machinery belongs to the construction side. Convergence at the commercial pole noted as drift, not identity.
6. **vs Yard Management System / Warehouse Management System (§10)** — name collision on "dock." ServiceTitan's own FAQ draws the line: dock & door software manages "door-level operations" (scheduling, dispatch, service tracking, equipment performance) for contractors, not trailer movement, yard space, or warehouse inventory. Vendor-confirmed Type separation.
7. **vs Utility Field Service Management (§19)** — utility-side workforce dispatch against network assets owned by the software operator's organization vs contractor-side business management serving customers. Different operator, different object, different money flow.
8. **vs Appointment Scheduling Application** — booking is one fragment (customer self-service booking exists in several products); this Type is the whole business operation.
9. **vs Local Service Marketplace** — demand-side discovery/booking vs operator-side execution and billing; a marketplace lead becomes a job here.
10. **vs CMMS / Enterprise Asset Management** — CMMS/EAM manages assets owned by the operator; this Type manages service work performed at customers' premises. The door/equipment record is a customer-owned asset registry, not an owned-asset registry.
11. **vs Property Maintenance Management (§17)** — property managers coordinate maintenance across their portfolios; this Type is the contractor's own business system. A property manager is a customer here.

## Uncertainties

1. **Door catalogs / dealer quoting** — garage door dealers (showroom sales of doors and openers) are a real market segment, and dealer-specific software (Successware heritage, XOLogic) is suspected to carry door product catalogs and configuration-based quoting. Both sources were unreachable (WAF/403), so this pole is not evidenced and is not claimed in the canonical document.
2. **Door measurement/spec fields** — strongly suspected in the trade (measure-then-order workflows), but not documented in any fetched source; not claimed.
3. **Fire-rated door drop testing / commercial door compliance** — commercial door trade practice, not observed in fetched sources; not claimed.
4. **ServiceTitan operational depth** — only Tier 2 marketing/FAQ pages were reachable; no help-center detail fetched this pass, so ServiceTitan claims are limited to what its site states.
5. **Jobber, Workiz, Successware** — major SMB players serving garage door companies; inaccessible (403/WAF). Market-coverage gap acknowledged; assertions calibrated to the five researched products.
6. **Regional markets** — the sample is North America–dominant (QuickBooks-centrism, US payment mechanics). Regional variance could not be verified; the canonical document avoids region-specific claims.

## Final Synthesis

Garage Door Service Management is the business-management system of a garage door / overhead door service company: it records customers and their service locations, carries each requested piece of door work as a durable job with a lifecycle, coordinates the technicians and installers who perform the work in the field, and turns completed work into invoices and payments. The defining core is the field-service spine with garage door work as the job's content; the trade's own color is the install-heavy work mix (service calls, repairs, and door/opener replacement-installations sold through multi-option estimates), plus commercial overhead/dock-door machinery (equipment histories, preventive maintenance agreements, installation projects) at the commercial pole. Everything else commonly associated with these products (dispatch boards, mobile apps, price books, notifications, recurring plans, GPS, AI) is standard or optional capability layered on a shared structure that vendors themselves ship as one platform configured per trade — and that at least one major vendor ships to this trade with no trade layer at all. The leaf is best understood as the garage-door trade instantiation of the field-service-management family — a distinct directory leaf by trade semantics, with a probable trade-Variant relationship to Small Business Field Service Management that should be ratified in joint review.
