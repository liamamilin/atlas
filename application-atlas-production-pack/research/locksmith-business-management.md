# Research Notes — Locksmith Business Management

Research date: 2026-09-08
Leaf: Locksmith Business Management (DIRECTORY.md §29 Home, Family, Personal & Local Services — trade-business cluster)
Slug: locksmith-business-management

## Research Goal

Understand what "Locksmith Business Management" software actually is in the real market: what objects it manages, how locksmith work flows through it, what is locksmith-trade-specific versus generic field-service structure, and where its boundaries lie with neighboring Application Types (generic small-business field service management, trade siblings like garage door/HVAC/electrical/appliance repair, fire protection and elevator service with their compliance loops, security-alarm installation, auto repair).

Family context carried into this pass: the §29 trade-business cluster has been resolved as two-poled — a trade-tuned pole (electrical, HVAC, garage door, handyman, appliance repair: trade difference = configuration/content + work mix over the generic FSM spine, no structurally distinct trade object) and a compliance-loop pole (fire protection: code-mandated recurring inspection program + persistent deficiencies + outward compliance reporting). The garage-door pass explicitly listed locksmith among trade siblings to cross-reference. The open question for locksmith: does the trade carry a structurally distinct object (key records, key-code catalogs, master-key-system charts, automotive key data, a licensing/inspection loop), or is it a trade-tuned variant of the field-service spine?

## Initial Boundary

Working hypothesis at start:

- It is the business-management system of a locksmith (and often security-hardware) service company: emergency lockouts, rekeying, key duplication, lock repair/installation, automotive key work, safes, and commercial access-control/key-control work.
- Core objects likely: customer + service location, job/work order with lifecycle, estimate, schedule/dispatch, locksmith/technician, invoice/payment, price book.
- Trade-specific candidates to test: key/lock registries, key-code or master-key-system records, automotive vehicle/key lookup, emergency after-hours dispatch machinery, licensing/bonding compliance objects.
- Closest neighbors: Small Business Field Service Management (likely the same structural spine), trade siblings, Fire and Security / alarm installer packaging, Auto Repair Shop Management (automotive pole), Appointment Scheduling Application.

## Research Questions

1. What objects make up the system (customer, location, job, estimate, appointment, technician, invoice, payment, price book)?
2. How does locksmith work flow from call to payment? What is the work mix (emergency lockout, rekey, key duplication, lock repair/install, commercial security/access-control work)?
3. What is locksmith-specific in the market: key/lock records, key codes, master key systems, automotive key data, emergency dispatch emphasis, security-business bundling?
4. How do scheduling and dispatch work, especially for emergency calls (speed/proximity)?
5. How does the residential pole differ from the commercial security pole?
6. Is there any compliance/inspection loop (licensing, code inspections) organized by the software?
7. Which interfaces do users actually operate (office dashboard, schedule, job detail, mobile app, customer-facing surfaces)?
8. Historical check: would older, regional, trade-agnostic, or paper-era locksmith operations still fit a minimal definition?

## Representative Products

Selected for market representation + documentation access + different product philosophies + different customer layers:

| Product | Segment / philosophy | Evidence tier |
|---|---|---|
| ServiceTitan | flagship "software for the trades"; commercial-focused Locksmith trade page over one platform | Tier 2 (site + trade page) |
| Service Fusion | SMB–mid; all-in-one multi-trade suite with a dedicated "Locksmith" industry page (~29 clone industry pages over one product) | Tier 2 (product page) |
| FieldPulse | growing SMB; workflow-configuration philosophy; dedicated Locksmith solution page with emergency-call emphasis | Tier 2 (site + locksmith page) |
| Kickserv | micro-SMB; simple, low-cost, trade-agnostic service business management | Tier 1 (knowledge center) |
| Housecall Pro | micro-SMB residential home services; help center documents industry packages for HVAC/Electrical/Plumbing only — demonstrates locksmith companies running the generic platform | Tier 1 (help center) |

Attempted and abandoned per source-access rules: Workiz (a heavy locksmith marketer per sibling-pass observations; /industries/locksmith-software/ and /locksmith-software/ both 404 this pass, after 404 ×2 in the handyman pass — abandoned), Locksmith Manager (dedicated locksmith-vertical product; transport error), The Professional Locksmith Software (dedicated locksmith-vertical product; transport error). LockPro (lockpro.io) was fetched but is a Shopify B2B access-control app — a product mismatch, not locksmith business software; discarded.

## Sources

Fetched 2026-09-08:

- ServiceTitan (Tier 2): https://www.servicetitan.com/industries/locksmith-software — "Commercial Locksmith Software" trade page
- Service Fusion (Tier 2): https://www.servicefusion.com/locksmith-software — "Locksmith Software" industry page with FAQ
- FieldPulse (Tier 2): https://www.fieldpulse.com/solutions/locksmith — "Locksmith Scheduling Software" solution page (platform map observed in nav/footer)
- Kickserv (Tier 1): https://kickserv.helpscoutdocs.com/article/32-jobs — "Jobs" article (Kickserv Knowledge Center)
- Housecall Pro (Tier 1): https://help.housecallpro.com/en/ — help-center collection map incl. "Industry Packages" collection description

## Product A — ServiceTitan

### Key observations (evidence layer A unless noted)

- A dedicated Locksmith trade page exists at /industries/locksmith-software, titled "COMMERCIAL LOCKSMITH SOFTWARE" — the commercial pole is the page's framing ("Unlock every tool needed to grow your commercial locksmith business"). Notably, Locksmith does not appear in the page footer's main Industries nav lists (HVAC, Plumbing, Electrician, Garage Door, Chimney Sweep, Water Treatment, Landscape, Pool, Septic, Pest Control, Lawn Care, Roofing) — a lower-prominence trade page, consistent with the handyman-pass observation about lower-prominence trade pages.
- Category definition: "Locksmith software provides you the tools needed to be more efficient and profitable. It puts tools such as locksmith dispatch software, project and inventory tracking, and other pivotal tools at work for your business."
- Locksmith work content named directly: the mobile app "equips locksmith technicians to arrive at each job fully informed, whether it's for lock rekeying, an emergency lockout, electronic lock service and maintenance, and more."
- Commercial scope named: "Whether your commercial locksmith business performs installation, repair, rebuilding and adjusting services for security systems, or lock management for key control systems…" and "door and access control for field technicians" — key control systems and access control named as the trade's commercial work.
- Commercial customers named: "Property managers, security officers, or HR teams can schedule jobs, review service calls, access invoice history and work orders, view GPS tracking of a tech's location, and submit online payments" (Customer Portal).
- Membership Renewals: "performance summary of each member agreement or long-term contract shows revenue, costs, the number of completed visits planned and unplanned, recurring services" — recurring commercial security contracts.
- Platform features re-labeled for the trade: Pricebook + Mobile Estimates ("present more options, follow up on proposals, and close more deals in the field"), multi-option estimate builder ("helped technicians close more jobs… at a higher average ticket"), Marketing Pro Reputation, Follow up on Estimates, Job Costing ("real-time insights into your costs and profits on every job and project"), Scheduling, Mobile App, WIP Reporting, Payroll, Inventory, Invoicing, Accounting.
- No locksmith-specific structural object on the page; the trade layer is labeling + tuning + the commercial security framing. Key control systems appear as work the locksmith performs, not as a software-managed key registry.

## Product B — Service Fusion

### Key observations (evidence layer A)

- "Run your locksmith and security business from anywhere with enterprise-level features, at a small business price." — the locksmith-and-security-business framing.
- "Locksmith" is one of ~29 clone industry pages (HVAC, plumbing, electrical, appliance repair, overhead & garage door, locksmith, irrigation, pool, …) over the same suite — trade layer as packaging.
- FAQ category definition: "Locksmith software may include any combination of payment processing, fleet tracking, job management, inventory management, estimate creation, invoice management, and customer management tools designed for the field service industry and most often sold as a subscription-based software offering." — entirely generic FSM vocabulary.
- Features: scheduling & dispatching ("Easily shift times and dates to avoid scheduling overlaps"); connected workforce ("view converted estimates, job statuses, payments"); estimates & jobs "in seconds with pre-populated products, service line items"; QuickBooks bi-directional sync (customers, products, services; job deposits, invoices, payments); Service Fusion Payments + portable Stripe M2 reader for field payments; mobile app (dispatched job/estimate assignments, map/directions, job photos, notes, pre/post-work signatures, invoices, payments); customer web booking portal; automated pre-job text notifications; ServiceCall.ai VoIP (call/text, auto-route calls, call-reason tracking, recording/transcription); GPS fleet tracking with "Track My Tech".
- Pricing FAQ: "The cost of residential and commercial locksmith software varies…" — both poles served by the same product.
- Customer testimonial: "Secure Lock and Alarm" — a locksmith-and-alarm business.
- Nothing locksmith-specific in structure; the page is the generic suite with trade wording.

## Product C — FieldPulse

### Key observations (evidence layer A)

- Dedicated Locksmith solution page; headline: "Locksmith Scheduling Software That Boosts Your Revenue — Whether it's a lockout or a rekey, speed matters."
- Emergency/speed framing throughout: "Book and dispatch locksmith jobs the moment they come in. Assign the nearest tech and keep your schedule full without chaos"; "Offer online booking so customers can request service 24/7… FieldPulse makes you available when they need you most."
- Locksmith Scheduling: "Keeping up with rekeys, installs, and maintenance work shouldn't feel like a juggling act" — drag-and-drop scheduling, automated notifications to technician apps, multi-team scheduling views filtered by technician/job type/team.
- Locksmith Service Call Software: "Turn Lockout Calls Into Scheduled Jobs Instantly" — call routing ("automatically direct incoming locksmith service calls to the right person based on job type, priority, or service area"), real-time scheduling ("Book jobs directly on your live calendar during the call and lock in a time slot based on real-time technician availability"), job tracking ("Track each job from call to completion with notes, status updates, and a full timeline in one place").
- Locksmith Dispatch: live technician tracking ("assign incoming jobs based on proximity and availability"), smart route optimization, conflict alerts (overlaps, double-bookings, routing delays).
- Locksmith Mobile App: full schedule with job times/addresses/customer notes, instant job notifications, on-site job management ("start jobs, log notes or photos, and mark jobs complete").
- Locksmith CRM: full customer profiles ("contact info, service history, site notes, and preferences"), two-way messaging, appointment reminders.
- Locksmith Invoicing and Estimate Software: pre-set service pricing ("Select from pre-approved locksmith services"), built-in pricebook, customizable invoices; product imagery alt-text: an estimate for "a residential door lock hardware set listing lockset, deadbolt, and rekeying line items" with a Sign and Accept panel; a "lock repair job with an arrival window"; a "lock replacement job card" with status options "New Job, On The Way, In Progress, Pending, Completed, and Canceled".
- Locksmith Reporting: custom widgets, profitability reports ("job costs, materials, and revenue… identify low-margin services"), technician performance reports.
- FAQ: "Locksmith scheduling software helps locksmith businesses organize and manage job appointments, technician assignments, and service calls from one system. It helps track schedules, assign the nearest available locksmith, and keep daily operations running smoothly." / "FieldPulse is a field service management platform made for locksmith businesses with 5–200 employees."
- Platform beyond the trade page: work order/job management, estimates & invoices, pricebook, project management, maintenance agreements, customer portal, booking portal, custom forms, asset management, inventory, fleet tracking, Operator AI (24/7 AI dispatching), ClearPath, Engage VoIP.
- Nav shows a separate "Fire and Security" solution page alongside Locksmith — security-alarm installation packaged as its own trade page over the same platform.
- No locksmith-specific structural object; the trade layer is work content (lockouts, rekeys, installs) + the emergency speed/proximity emphasis.

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
- Trade-agnostic: nothing locksmith-specific anywhere; locksmith companies are among the trades served.

## Product E — Housecall Pro

### Key observations (evidence layer A, Tier 1 — help-center collection map)

- "Industry Packages: Learn about industry-specific Housecall Pro packages for HVAC, Electrical, and Plumbing Pros" (4 articles) — no locksmith package documented. Locksmith companies run the generic platform.
- Whole-product structure (generic): Company Dashboard, Customers, Customer Portal, Employees, Franchise, Fleet Management, Jobs / Invoices / Estimates (62 articles), Job Inbox (jobs/leads/opportunities delivered to an inbox), Leads, Pipeline, Price Book (23 articles), Scheduling, Service Plans ("Maintenance Plans, Planned Maintenance Programs, Care Clubs and Membership Plans"), HCP Payments (71 articles), Invoicing, Notifications, Reporting, Checklists, Purchase Orders, Payroll, Multi-Day Jobs Appointments, Voice, HCP Assist (AI), App Store.
- Confirms the trade-agnostic pole: the same structure that serves electricians serves locksmith companies without any locksmith awareness.

## Cross-product Comparison

| Structure / capability | ServiceTitan | Service Fusion | FieldPulse | Kickserv | Housecall Pro | Assessment |
|---|---|---|---|---|---|---|
| Customer record with service location | ✓ (CRM) | ✓ | ✓ (CRM; "site notes") | ✓ (Customers & Contacts) | ✓ (Customers) | Universal — core |
| Job / work order with lifecycle | ✓ (job management) | ✓ (jobs) | ✓ (job tracking "from call to completion"; status cards) | ✓ ("heart of the workflow"; board) | ✓ (Jobs) | Universal — core |
| Office→field technician coordination (dispatch) | ✓ (Dispatch) | ✓ (scheduling & dispatching) | ✓ (dispatch, live tracking, proximity assignment) | ✓ (assign tech; work events) | ✓ (Employees, scheduling) | Universal — core |
| Estimate/quote → approval → job conversion | ✓ (multi-option estimates; Pricebook + Mobile Estimates) | ✓ (pre-populated line items) | ✓ (pre-set service pricing; estimate→invoice) | ✓ (Opportunity→estimate→Job) | ✓ (Estimates, Sales Proposals) | Universal — standard |
| Invoice + payment on completed work | ✓ (Invoicing, Payments) | ✓ (invoices, FusionPay, Stripe reader) | ✓ (estimates→invoices, on-site payment) | ✓ (Invoices; "get paid") | ✓ (Invoicing, HCP Payments) | Universal — core |
| Technician mobile app | ✓ (Mobile App) | ✓ (photos, notes, signatures, payments) | ✓ (schedule, notifications, on-site completion) | ✓ (mobile app section) | ✓ (mobile-only features) | Universal — standard |
| Price book / line-item pricing | ✓ (Pricebook) | ✓ (pre-populated products/service line items) | ✓ (built-in pricebook; pre-set locksmith services) | ✓ (service types) | ✓ (Price Book) | Universal — standard |
| Customer notifications | ✓ (Customer Experience) | ✓ (pre-job texts; booking portal) | ✓ (reminders, two-way messaging) | ✓ (Reminders) | ✓ (Notifications) | Universal — standard |
| Multi-visit jobs / work events | ✓ | ✓ | ✓ (arrival windows; job timeline) | ✓ (explicit: several work events per job) | ✓ (Multi-Day Jobs Appointments) | Universal — standard |
| Emergency-call emphasis (speed/proximity dispatch, 24/7 availability) | ✓ ("emergency lockout" work content) | — (generic dispatch) | ✓ explicit ("lockout or a rekey, speed matters"; "the moment they come in"; nearest tech; 24/7 booking; priority call routing) | — | — | Common — trade-typical work mix (2/5 explicit) |
| Locksmith work content named (rekey, lockout, lock install, key/security hardware) | ✓ (rekeying, emergency lockout, electronic lock service, key control systems, access control) | ✓ ("locksmith and security business") | ✓ (lockout, rekey, installs, lockset/deadbolt/rekeying line items) | — (generic jobs) | — (generic platform) | The trade's content layer |
| Recurring work (plans/agreements) | ✓ (Service Agreements; Membership Renewals for commercial contracts) | ✓ (agreements per KB) | ✓ (Maintenance Agreements) | ✓ (Recurring Jobs) | ✓ (Service Plans) | Universal — standard |
| Commercial security pole (property managers/security officers, access control, key control) | ✓ explicit (commercial page framing; portal for property managers/security officers/HR) | ✓ ("residential and commercial locksmith software"; "Secure Lock and Alarm") | partial (commercial segment page exists platform-wide) | — | — | Common at the commercial pole |
| Equipment/asset records | — (not on locksmith page) | ✓ (equipment records in KB — generic) | ✓ (Asset Management platform feature) | — | — | Optional |
| Purchasing / inventory | ✓ (Inventory) | ✓ (inventory in app) | ✓ (Inventory Management) | — | ✓ (Purchase Orders) | Common/optional |
| GPS fleet tracking | ✓ (Fleet Pro) | ✓ (built-in; Track My Tech) | ✓ (Fleet Tracking) | — | ✓ (Fleet Management) | Optional |
| VoIP / call tracking | — (Pro contact center) | ✓ (ServiceCall.ai) | ✓ (Engage; call routing) | — | ✓ (Voice) | Optional; strong in this trade's sample (call-driven demand) |
| Accounting sync | ✓ (QuickBooks; ERPs) | ✓ (QuickBooks bi-directional) | ✓ (QuickBooks-class integrations) | ✓ (QuickBooks 2-way) | ✓ (QuickBooks Online/Desktop) | Universal — standard |
| Reporting / dashboards | ✓ (Reporting; job costing) | ✓ (Reports Dashboard) | ✓ (profitability, tech performance) | ✓ (Reports) | ✓ (Reporting) | Universal — standard |
| AI assistants | ✓ (Atlas; AI Virtual Agent) | ✓ (AI call answering; Notes+) | ✓ (Operator AI) | — | ✓ (HCP Assist) | Optional; era-typical |
| Trade layer realization | Commercial Locksmith trade page (lower-prominence in nav) | "Locksmith" clone page over suite | Locksmith solution page over platform | none (trade-agnostic) | no locksmith package (generic platform) | The Type's packaging pattern |

### What is actually locksmith-specific (across sample)

1. **Trade-tuned packaging and configuration** — all sampled multi-trade vendors sell "locksmith" as a labeled variant of one platform (ServiceTitan commercial locksmith page; Service Fusion clone page; FieldPulse solution page), and Housecall Pro documents no locksmith package at all, demonstrating that the generic platform serves the trade. [Layer A ×4 vendors]
2. **The work mix: emergency lockouts + rekeys + lock/key/security-hardware work** — lockout calls, rekeying, lock installation/repair, key duplication, electronic lock service, and (commercial) security-system/access-control/key-control work are the named job content. [Layer A ×3 vendors: ServiceTitan, Service Fusion framing, FieldPulse]
3. **Emergency speed/proximity dispatch emphasis** — the lockout call is an emergency work class: "speed matters," book-and-dispatch "the moment they come in," assign the nearest tech, 24/7 booking availability, call routing by priority. [Layer A ×2 vendors explicit: FieldPulse, ServiceTitan work content; Service Fusion's VoIP/call-tracking emphasis is consistent]
4. **Commercial security contracts** — property managers, security officers, and HR teams as customers; key control systems and access control as work; membership/contract renewals with performance summaries. [Layer A ×1 explicit at page level (ServiceTitan commercial framing); Service Fusion confirms residential+commercial pricing split]

No sampled product showed a *structurally distinct* locksmith object in reachable documentation: no key registry, no key-code catalog, no master-key-system chart object, no automotive vehicle/key lookup, no code-mandated inspection/deficiency loop. The trade difference is configuration + content + the emergency-heavy work mix, not a different data model.

## Canonical Model

### Level 0 — Defining Invariant (deliberately minimal)

1. **Customer with a service location** — work is performed at the customer's premises (home, business, storefront, facility) or wherever the locked-out customer is, so jobs bind to addresses; the customer may be a person, a business, or a property/commercial hierarchy.
2. **Locksmith job (work order)** — a requested piece of lock, key, or security-hardware work (emergency lockout, rekey, key work, lock repair or installation, electronic lock / access-control / key-control work) at that location, carried through a managed lifecycle (requested → scheduled → assigned → performed → completed → billed).
3. **Locksmith / technician as the executing role** — jobs are assigned to field workers and coordinated by the office (scheduling/dispatch; emergency calls dispatched on speed and proximity).
4. **Billing of completed work** — the job produces an invoice that collects payment (estimate/quote upstream of larger work).

Remove the customer/location → generic task tracking. Remove the job lifecycle → an address book or invoicing tool. Remove technician coordination → pure invoicing. Remove billing → a dispatch board only. Remove "locksmith work" as the job's content → the generic Small Business Field Service Management Type.

Historical check: a paper-era locksmith shop (job tickets, a dispatch board, a key/lock price list, invoices) satisfies all four properties; a 24/7 emergency lockout service run on paper and a phone tree satisfies them; 1990s–2000s dedicated field-service products satisfy them; trade-agnostic products configured by a locksmith business satisfy them (Kickserv and Housecall Pro demonstrate the trade-agnostic pole directly). None of the modern machinery (mobile apps, GPS, memberships, portals, AI) is definitional. The check passes.

### Level 1 — Common Mature Structure

- Estimates/quotes with line items — customer approval, conversion into jobs; multi-option estimates carried over from the family's replacement-sales pattern
- Scheduling calendar + dispatch board; assignment of technicians; proximity/speed-aware assignment and live technician location in mature products
- Technician mobile app: assigned jobs, navigation, job details/history, photos, notes, signatures, on-site payment, invoice creation
- Price book: services, parts, locks/hardware, and key work with prices
- Customer notifications: booking confirmations, day-of reminders, on-my-way alerts, invoice delivery
- Multi-visit jobs (diagnosis visit, return with parts or hardware)
- Recurring work: recurring jobs, service agreements/memberships (commercial security contracts at the commercial pole)
- Reporting: jobs, revenue, technician performance, job profitability
- Accounting sync (QuickBooks in the North American SMB market)

### Level 2 — Variant / Optional Structure

- Commercial security machinery: key control systems, master key systems, and access control as contracted work; property-manager/security-officer customers; contract renewals with performance summaries
- Site equipment/asset records (locks, access-control hardware) with per-location service history — commercial pole
- Purchase orders / parts inventory / truck stock
- VoIP/call tracking with call-reason capture — strong in this trade's sample because demand is call-driven
- Customer self-service: booking pages (24/7 availability emphasized), portals, financing
- GPS fleet tracking; payroll/time tracking; marketing/review management
- Franchise/multi-location structures; AI assistants (era-typical)
- Emergency after-hours coverage machinery (on-call scheduling, after-hours answering) — implied by the trade's 24/7 posture, not documented as a distinct structure in fetched sources

### Level 3 — Vendor-specific (kept out of the canonical document)

- ServiceTitan: Pro product tiers (Pricebook/Dispatch/Fleet Pro…), Atlas, Convex, Titan Intelligence; commercial-locksmith page framing; membership performance summaries
- Service Fusion: ServiceCall.ai VoIP/call tracking, Notes+ AI note cleanup, Acorn homeowner financing, built-in GPS, Stripe M2 reader specifics, "1,000% ROI" fleet claims, no-per-user pricing
- FieldPulse: Operator AI (24/7 AI dispatching), ClearPath guided job-stage workflows, Engage VoIP, Field Intelligence, 78% revenue-growth claim, "5–200 employees" positioning
- Kickserv: "Opportunity" object naming for the pre-estimate stage
- Housecall Pro: HCP Assist, HCP Payments/Payroll module names, Job Inbox

## Vendor-specific Findings

See Level 3. Notable patterns: ServiceTitan is the only sampled vendor whose locksmith page is explicitly commercial-framed ("Commercial Locksmith Software") — and the page sits outside the footer's main trades nav, a lower-prominence trade page like handyman. FieldPulse is the only sampled vendor whose locksmith page leads with the emergency-call motion (lockout → instant scheduling → nearest tech). Service Fusion frames the trade as "locksmith and security business," bundling the security-alarm adjacency into the trade page, while FieldPulse ships a separate "Fire and Security" page — the same adjacency packaged differently.

## Rejected Findings

1. **Key/lock registries as a defining object** — suspected in the trade (locksmiths track keys cut, key codes, restricted keyways, master-key-system pinning charts), but no fetched source documented a key registry or key-code catalog object. The software captures key/lock work as job content (line items, descriptions), not as a managed key inventory. Rejected as canonical; recorded as an uncertainty.
2. **Automotive key data (vehicle make/model lookup, transponder programming records)** — a real locksmith specialization, but not observed in any fetched source. Not claimed.
3. **Code-mandated inspection/deficiency loop (fire-protection-style)** — no evidence anywhere in the sample. Locksmith licensing/bonding is a business credential held by the company, not a recurring inspection program organized by the software. Rejected; locksmith belongs to the trade-tuned pole, not the compliance-loop pole.
4. **Safe-work objects** — safe service is a locksmith trade activity, but no safe-specific structure appeared in any fetched source. Not claimed.
5. **"Security business" as a separate Type from locksmith** — the market bundles them (Service Fusion: "locksmith and security business"; FieldPulse: separate "Fire and Security" page over the same platform; ServiceTitan: security systems within the locksmith page). One spine; the security-alarm installer trade is a sibling trade page, not a different structure.
6. **LockPro (lockpro.io)** — fetched candidate that turned out to be a Shopify B2B access-control app; a name collision, not locksmith business software. Discarded.

## Boundary Findings

1. **vs Small Business Field Service Management** — the structural spine is identical (customer+location → job lifecycle → technician coordination → invoice/payment; verified across five products). Vendors ship "locksmith" as a preconfigured trade layer of one product (ServiceTitan trade page; Service Fusion clone page; FieldPulse solution page), and Housecall Pro demonstrates the trade running with no trade layer at all. Probable trade-Variant relationship rather than two independent Types — consistent with the electrical, cleaning, appliance-repair, garage-door, and handyman passes; the durable difference is trade semantics (lock/key/security work content, emergency-heavy work mix with speed/proximity dispatch, commercial security contracts). Joint review with Small Business Field Service Management recommended.
2. **vs trade siblings (garage door, HVAC, plumbing, electrical, appliance repair, handyman)** — same family pattern; the trade wrapper differs, the spine does not. This pass discharges the garage-door pass's trade-sibling cross-reference for locksmith from this side: locksmith belongs to the trade-tuned pole (electrical/garage-door/handyman pole), not the compliance pole.
3. **vs Fire Protection Service Management / Elevator Service Management** — those siblings carry a structurally distinct trade object (code-mandated recurring inspection program, persistent deficiencies, compliance reporting). Locksmith shows no such loop in any fetched source; it is a trade-tuned variant like electrical and garage door.
4. **vs Fire and Security / alarm-business packaging** — security-alarm installation is a sibling trade served by the same platforms (FieldPulse "Fire and Security" page; Service Fusion "Alarm" industry page). Locksmith businesses frequently bundle access-control and security-hardware work, so the customer populations overlap; the software spine is identical. The boundary is trade content, not structure.
5. **vs Appliance Repair Management** — appliance repair's distinguishing object is the customer's appliance as the unit of repair; here the unit of work is the lock/key/security hardware at the site (or the locked vehicle), with no appliance-style equipment registry observed as definitional.
6. **vs Auto Repair Shop Management** — automotive locksmith work (car lockouts, vehicle key work) happens in the field at the vehicle's location as dispatched jobs, not as shop-based repair orders against a customer vehicle record; no automotive-shop structure was observed in the sampled locksmith packaging. Noted as a pole to watch, not a boundary conflict.
7. **vs Appointment Scheduling Application** — booking is one fragment (24/7 online booking exists in several products); this Type is the whole business operation.
8. **vs Local Service Marketplace** — demand-side discovery/booking vs operator-side execution and billing; a marketplace or emergency-call lead becomes a job here.
9. **vs CMMS / Enterprise Asset Management** — CMMS/EAM manages assets owned by the operator; this Type manages service work performed at customers' premises. Locks and access-control hardware are customer-owned assets, appearing (if at all) as optional site-equipment records.
10. **vs Property Maintenance Management (§17)** — property managers coordinate maintenance across their portfolios; this Type is the contractor's own business system. A property manager is a customer here (explicitly named as a portal user in the commercial pole).
11. **vs physical access-control / electronic security management systems** — locksmiths install and service electronic access-control systems, but the systems that operate those locks day-to-day belong to the physical-security software world; this Type manages the service business around that work, not the access-control operation itself.

## Uncertainties

1. **Dedicated locksmith-vertical software** — products marketed specifically to locksmiths (Locksmith Manager, The Professional Locksmith Software) were unreachable (transport errors ×2). Whether such products carry key registries, key-code catalogs, or master-key-system chart objects remains unverified; not claimed. This is the pass's main evidence gap.
2. **Workiz** — a major SMB player that markets heavily to locksmiths (per sibling-pass observations); unreachable (404 ×2 this pass, after 404 ×2 in the handyman pass). Market-coverage gap acknowledged.
3. **Key control / master key system records** — strongly suspected in the trade (locksmiths maintain pinning charts and key hierarchies for commercial customers), but not documented in any fetched source; not claimed.
4. **Automotive locksmith pole** — car lockouts and vehicle key work are a large trade segment; not observed in fetched sources; not claimed.
5. **Licensing/bonding compliance features** — locksmith licensing varies by jurisdiction; no licensing-compliance feature was observed in fetched sources; not claimed.
6. **Regional markets** — the sample is North America–dominant (QuickBooks-centrism, US payment mechanics). Regional variance could not be verified; the canonical document avoids region-specific claims.
7. **ServiceTitan operational depth** — only Tier 2 marketing/FAQ pages were reachable; no help-center detail fetched this pass, so ServiceTitan claims are limited to what its site states.

## Final Synthesis

Locksmith Business Management is the business-management system of a locksmith (and often security-hardware) service company: it records customers and their service locations, carries each requested piece of lock, key, or security work as a durable job with a lifecycle, coordinates the locksmiths who perform the work in the field — with the trade's signature emphasis on speed and proximity when the call is an emergency lockout — and turns completed work into invoices and payments. The defining core is the field-service spine with locksmith work as the job's content; the trade's own color is the emergency-heavy work mix (lockout calls booked and dispatched in the moment, rekeys, lock installs, key and security-hardware work) plus commercial security machinery (key control systems, access control, property-manager customers, contract renewals) at the commercial pole. Everything else commonly associated with these products (dispatch boards, mobile apps, price books, notifications, recurring plans, GPS, VoIP call tracking, AI) is standard or optional capability layered on a shared structure that vendors themselves ship as one platform configured per trade — and that at least one major vendor ships to this trade with no trade layer at all. The leaf is best understood as the locksmith trade instantiation of the field-service-management family — a distinct directory leaf by trade semantics, with a probable trade-Variant relationship to Small Business Field Service Management that should be ratified in joint review. The dedicated locksmith-vertical software pole (key registries, master-key-system records) remains unverified and is deliberately not claimed.
