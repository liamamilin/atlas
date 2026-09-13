# Research Notes — Pest Control Management

## Research Goal

Understand what "Pest Control Management" is as an Application Type: the operator-side business management software used by pest control companies (structural pest control — treating homes, buildings, and other structures against insects, rodents, termites and other pests). Identify the core objects (customer, serviced structure/property, service visit, technician, chemical application records, monitoring devices, inspection findings, service plans, billing), the visit lifecycle, who operates it, which structures are pest-trade-specific, and where the boundary lies against the closest siblings (Small Business Field Service Management, Lawn Care Business Management, Pool Service Management, Cleaning Business Management) and adjacent types (Crop Protection Management, Animal Control Management, Home Inspection, marketplaces).

## Initial Boundary

- This is a §29 trade-cluster leaf: the business-management software of one service trade, operator-side (the pest control company's system), not consumer-side.
- Nearest types: Small Business Field Service Management (generic sibling), Lawn Care Business Management (chemical-application sibling, processed 2026-09-08 — pre-hung JOINT REVIEW flag for this leaf), Pool Service Management (chemical sibling, unprocessed), Cleaning Business Management (processed — recurring indoor visits), other §29 trade leaves.
- Adjacent but different domains: Crop Protection Management (§20 — agricultural pest control on crops/fields), Animal Control Management (§24 — government animal control), Home Inspection Application (§29 — inspection-only, real-estate transactions), Property Maintenance Management (§17 — owner side), Home Services / Local Service Marketplaces (§29 — demand side).
- Known pre-hung flag (from lawn-care pass): route-based recurring visits + chemical records + licensing on both sides; seam = structures/interiors pest regime vs turf treatment; joint review recommended.

## Research Questions

1. What is the unit of work — what exactly does a pest control "service" look like as a record?
2. What recurring revenue structures exist (service plans, frequencies, renewals, termite protection renewals)?
3. What trade-specific records does the software carry — chemical/pesticide application records, monitoring devices (bait stations/traps), inspection findings, WDO/termite inspection reports?
4. How does regulation shape the software (state pesticide usage reports, licensing, records retention, paperwork display)?
5. How do residential vs commercial accounts differ (multi-unit buildings, facility device compliance)?
6. What is the office↔field loop (scheduling, routing, technician mobile app, offline)?
7. How does selling work (leads, estimates, proposals, bundled packages, e-signature)?
8. What billing patterns exist (per-visit, subscription/autopay, collections)?
9. Boundary: what separates this Type from generic FSM structurally; what separates it from Lawn Care/Pool (chemical siblings); what separates it from Crop Protection (agricultural pest)?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

1. **PestPac (by WorkWave)** — the long-standing pest-dedicated leader; enterprise tier (Terminix, Arrow Exterminators, Truly Nolen); "AI-powered" positioning; residential + commercial lines.
2. **FieldRoutes (a ServiceTitan company)** — pest-dedicated Operations Suite aimed at growth-oriented pest companies (Aptive, Fox Pest Control, Moxie, Greenix); routing/scheduling/billing core with WDO compliance tooling.
3. **GorillaDesk** — pest-first multi-trade platform for small operators; founded by former pest control operators; richest public feature documentation (chemical tracking, device tracking, diagramming, multi-unit).
4. **Briostack (EverCommerce)** — pest-dedicated, founded by a pest control company's CEO; pest + lawn; offline-capable tech app; sales/leaderboard culture.
5. **Kickserv** — horizontal field service management used by service trades; the generic-spine control sample (Tier 1 help-center documentation).

Dropped: ServSuite (ServicePro) — unreachable (two transport errors); PestRoutes = FieldRoutes (same product, former name).

## Sources

Research date: 2026-09-09. All fetches from the research environment.

- PestPac — product root — https://www.pestpac.com/
- PestPac — Residential Pest Control Software feature page — https://www.pestpac.com/features/residential-pest-control-software
- FieldRoutes — product root — https://www.fieldroutes.com/
- FieldRoutes — Pest Control Software solution page — https://www.fieldroutes.com/solutions/pest-control-software
- GorillaDesk — product root — https://www.gorilladesk.com/
- GorillaDesk — Chemical Tracking Software feature page — https://gorilladesk.com/features/chemical-tracking-software/
- GorillaDesk — Device Tracking Software feature page — https://gorilladesk.com/features/device-tracking-software/
- GorillaDesk — Pest Control Software industry page — https://gorilladesk.com/industries/pest-control-software/
- Briostack — product root — https://www.briostack.com/
- Kickserv — Knowledge Center, "Jobs" article — https://kickserv.helpscoutdocs.com/article/32-jobs (Tier 1)

> Sourcing limitation: no Tier-1 help-center documentation could be reached for any of the four pest-dedicated products (GorillaDesk's Intercom help center timed out; PestPac/FieldRoutes/Briostack help centers were not reachable in this pass; ServSuite returned transport errors twice and was dropped). Evidence for the pest-dedicated products is therefore official product/industry/feature-page level (Tier 2); only the horizontal control product is documented at help-center level (Tier 1). Claims below are calibrated accordingly: workflow mechanics are described at the level the sources state, precise numeric limits and defaults are avoided, and vendor marketing metrics are excluded.

## Product Observations

### PestPac (WorkWave) — evidence layer A

- Positioning: "AI-powered pest control software that unifies field, finance and back office operations"; "Enterprise pest control is complex, margin driven, and built on results." Schema.org featureList: Scheduling, Routing, CRM, Mobile App, Reporting, Accounting, Customer Portal, Customer Communication, **Chemical Tracking**, **Termite Inspection**, Custom Forms, Website Builder, Marketing, API & Integrations.
- Separate **Residential** and **Commercial** pest control software lines; trusted-by logos are national enterprise operators (Terminix, Arrow, Truly Nolen).
- Residential feature page (Tier 2, directly observed):
  - Self-service tools: customers "get estimates, place orders and pay for services", "make payments and manage their stored payment methods for recurring payments", "review and sign proposals and contracts".
  - Customer notifications: "send service reminders or let customers know when you're on the way via call, text or email"; renewals and promotions; review requests.
  - Mobile app: "Access map and location details in the field"; "Document **activity, findings and material applications** with GPS maps and Sketch tool"; "Add additional service orders when upselling during a visit"; "Complete service orders, set follow up visits and print or email reports and invoices".
  - Scheduling: "Set **service frequencies** to accommodate customers' date and time preferences"; "Schedule services a month ahead, one day at a time or on-demand as needed"; technician settings including "vacation and holiday time, start/end locations and **skill levels**"; "Adjust schedules on the fly".
  - RouteOp route optimization: "Honor customer commitments and requests"; "Adjust routes based on technician settings like max production value, time to leave, scheduled days/hours and more".
  - Communication Center: chat/text/email with customer records and service histories in one place.
- Marketing metrics on the page (21% more jobs, 30% less drive time, 55% faster growth) — vendor claims, excluded from findings.

### FieldRoutes (ServiceTitan) — evidence layer A

- Positioning: "Field service management software that fuels growth"; Operations Suite = routing, scheduling, billing, dashboards, mobile app, payments, API; Industries: Pest Control, Commercial pest control, Other field-service industries. Customer logos are growth-stage pest companies (Aptive, Fox, Aruza, Ecoshield, Moxie, Greenix).
- Pest control solution page (Tier 2, directly observed):
  - Scheduling: "Drag & drop onto routes — FieldRoutes highlights customers needing service so managers can build technician routes by clicking, dragging, and dropping"; "scheduling automation for **ongoing contracts**"; "smart schedules… algorithms evaluate variables, including customer preferences, weather conditions, and **service due dates**".
  - Routing: "Generate optimized schedules based on the best days, times, and stop sequences for thousands of stops across multiple routes in a single batch"; "Assign **skillsets** to technicians so specialized jobs are assigned to routes with the team members able to do them"; routes consider "drive time, fuel efficiency, and vehicle wear".
  - Collections: payment reminders on autopilot, online payment portal, AutoPay.
  - Reporting: real-time operational metrics; "**WDO reporting and compliance** — FieldRoutes makes maintaining compliance with **California Branch 3** and tracking **WDO inspections** easy"; "**NPMA-33** access" via "the integrated Sentricon system makes tracking **wood-destroying organism inspections** easy while maintaining compliance and **license renewals**".
  - CRM "designed for the pest control industry": customer data "including locations, balances due, and service requests".
  - Bundled packages: "combine different services together… general pest treatment plus more specialized offerings like termite and spider services… create, sell, schedule, service and bill multiple services together".
  - FAQ names the category's tool set: "Inventory management for pesticides, chemicals, and more; CRM with sales pipeline visibility; automated appointment reminders; scheduling, route optimization, and invoicing; client portal with credit card payment"; "Commercial and Multi-Unit Pest Control".
- Testimonial (customer voice on vendor page): "Even the reports to send to the **AG Department**. You guys have everything." — the state agriculture department as pesticide regulator is part of the software's reporting surface.
- Blog (vendor's own industry content): "reservice rates" as a tracked pest-control metric (return visits when pests persist); "Route Economics… every pest control stop"; cost-per-stop as the trade's unit of margin.

### GorillaDesk — evidence layer A

- Positioning: "#1 Field Service Software for Pest, Lawn, & Cleaning Businesses"; "We were once field service pros just like you, running a growing pest control and lawn business." Industries grouped: **Pest & Wildlife** (pest control, wildlife control, mosquito control, termite control), Green (lawn, landscaping, tree, fertilization, irrigation, snow), Cleaning, Contracting (incl. pool, fire safety, handyman).
- Chemical Tracking page (Tier 2, directly observed — the richest trade-specific documentation in the sample):
  - **Chemical Data**: account "comes pre-populated with a robust list of standard materials"; add "the name, manufacturer, **EPA registration number, active ingredients, and dilution rates**"; when recording usage "specify the actual **quantity, unit of measure, application method, and device used**"; "record the **targeted pests and the exact areas treated** on your customer's property".
  - **Templates**: "service templates, which ensure your team follows the **label instructions** for every chemical being applied"; sync to mobile app.
  - **Material Use Reports**: "if your business is located in a state that requires **pesticide usage logs**, GorillaDesk can generate these for you"; report "segmented by **county** or by each individual job".
  - **Paperwork Display**: "chemical use data is included with every invoice and work order (unless you choose not to) so customers know which chemicals were used and where"; available in Customer Portal.
  - **Record Keeping**: "Many states require that chemical use be tracked and stored for up to **seven years**" (vendor's characterization of state rules); "download your entire chemical application history"; export CSV/Excel.
- Device Tracking page (Tier 2, directly observed):
  - "Scan and track any device with a barcode (**mouse traps, live traps, glue boards, bait blocks, and more**)" using the mobile app; manage "area list, device types, device status, and activity level" in the field.
  - Device data: "name, barcode #, coordinates, device type, area, **check-in time, status, and activity levels** of all your **traps and bait stations**"; synced in real time.
  - Digital logbook: "view device recordings in real-time, print, or email work orders with device data, and meet state requirements regarding material tracking".
  - Paperwork display: "If your business is located in a state that requires you to include device details on your paperwork, GorillaDesk can automatically add these sections to your invoices and work orders."
  - Positioning: "If you want to drive more **commercial and facility management** business, you'll need proper reporting and tracking." Pro-plan feature.
- Pest control industry page (Tier 2): scheduling & dispatching (drag-and-drop calendar, push notifications), invoicing & payments (templates, batch invoicing, automatic payments), chemical tracking & reporting, customer communications (confirmations, reminders, "On My Way" texts), digital documents (e-signatures, 100+ template document library), plus: **Diagramming** ("draw an accurate graph of a site, a room, or any other object while you're in the field"), **Multi-Unit Buildings** ("keeping track of individual units at the same address"), device management ("Work with facilities requiring device tracking"), CRM, credit card processing, customer portal, QuickBooks sync, route optimization, technician GPS tracking.
- FAQ (vendor's own category framing): basic features = job scheduling, route optimization, billing & invoicing, reporting, **material tracking**, email & SMS, confirmations/reminders, GPS, mobile app; advanced = customer portal, review engine, subscription billing, commission tracking, **device tracking**, documents, e-signature.

### Briostack (EverCommerce) — evidence layer A

- Positioning: "Brio was created by a pest control company out of the need for a better software solution. Since pest and lawn care go hand in hand, we developed an all-in-one software…"; "Trusted by 3,700+ Pest Control and Lawn Care Companies"; "Pest Management Professionals".
- Solutions: CRM, Sales & Lead Management, Scheduling & Routing, **Bids & Diagramming**, Marketing Add On, Public API. Industries: Pest Control, Lawn Care.
- Brio Office: "Automate scheduling and routing"; "Streamline customer communications"; "Simplify **postal mail delivery of invoices & statements**"; QuickBooks integration.
- Brio Tech (mobile): "allows your techs to work efficiently — **even without data connectivity**"; "View service history, customer information, and work orders"; "Optimize routes with turn-by-turn directions"; "**Track and report on chemical usage**"; "Schedule and reschedule appointments"; "Sell to new pest control and lawn care customers".
- Brio Sales: leaderboards, sales territories, customer sign-up streamlining, marketing campaigns, lead generation — a sales-culture product pole.
- Marketing metrics (2x revenue growth, 30+ hours saved, 20-30% reduced drive time) — vendor claims, excluded.

### Kickserv (horizontal control) — evidence layer A, Tier 1

- Help center "Jobs" article: "Jobs are the heart of the Kickserv workflow… the main way you'll keep track of business activity." Workflow columns: **Unscheduled → In Progress → On Hold (optional) → Completed**.
- Jobs start as an **Opportunity** that becomes an **estimate**; customer approval turns it into an unscheduled Job. Job carries service type, internal description, external scope of work, contact, custom fields.
- Scheduling: date/time event, task type, assign to a tech (or leave unassigned). Start/Stop/On Hold/Mark Complete actions; multiple work events per job possible.
- **Recurring Jobs**: "set up a recurring series of Jobs… select how often… by date or day of week, and when you'd like the repeating Jobs to end."
- After completion: send invoice and get paid.
- No trade-specific structures anywhere in the Jobs model — no chemicals, devices, licensing, structures, or WDO forms. This is the generic spine the trade leaves differentiate from.

## Cross-product Comparison

| Structure | PestPac | FieldRoutes | GorillaDesk | Briostack | Kickserv (control) |
|---|---|---|---|---|---|
| Customer records (residential + commercial) | ✓ (separate residential/commercial lines) | ✓ ("Commercial and Multi-Unit Pest Control") | ✓ (multi-unit buildings feature) | ✓ | ✓ (contacts) |
| Serviced property/structure as record | ✓ (locations, GPS maps, Sketch) | ✓ (locations; WDO inspections per property) | ✓ (site/room diagramming; units at same address) | ✓ (work orders per customer/location) | generic job address only |
| Service visit / work order as unit of work | ✓ ("complete service orders, set follow up visits") | ✓ (stops/jobs on routes; service due dates) | ✓ (jobs; device data captured within a job) | ✓ (work orders) | ✓ (Jobs — Tier 1) |
| Recurring service plans / frequencies | ✓ ("set service frequencies") | ✓ ("ongoing contracts"; service due dates) | ✓ (subscription billing; recurring route work) | ✓ (automated scheduling/routing for plan base) | ✓ (recurring jobs — generic) |
| Route optimization | ✓ (RouteOp; technician settings) | ✓ (batch optimization; skillsets) | ✓ | ✓ (turn-by-turn) | — (not core) |
| Assigned technician w/ skill/licensing | ✓ (skill levels in tech settings) | ✓ (skillsets gate specialized jobs; "license renewals") | ✓ (techs; device/chemical recording per tech) | ✓ | ✓ (assign to tech — no licensing semantics) |
| Chemical/material application records | ✓ (featureList "Chemical Tracking") | ✓ (FAQ "inventory management for pesticides, chemicals") | ✓✓ (EPA reg #, active ingredients, dilution, quantity, method, device, target pests, areas treated) | ✓ ("track and report on chemical usage") | — |
| Regulatory reporting (pesticide usage logs) | implied (custom forms; reports) | ✓ ("reports to send to the AG Department"; CA Branch 3) | ✓ (material use reports by county/job) | ✓ ("report on chemical usage") | — |
| Monitoring device tracking (bait stations/traps) | not observed on sampled pages | not observed on sampled pages | ✓✓ (barcode, status, activity, digital logbook, paperwork display) | not observed on sampled pages | — |
| Inspection findings capture | ✓ ("document activity, findings") | ✓ (WDO inspections; NPMA-33) | ✓ (diagramming; photos) | ✓ (bids & diagramming) | — |
| WDO/termite inspection reporting | ✓ (featureList "Termite Inspection") | ✓✓ (NPMA-33, California Branch 3, Sentricon) | ✓ (termite control industry line) | not observed on sampled pages | — |
| Sales pipeline (leads → estimate → proposal → e-sign) | ✓ (estimates, proposals & contracts) | ✓ ("convert more leads into signed contracts") | ✓ (quotes & estimates, e-signatures, document library) | ✓✓ (Brio Sales, leaderboards, territories) | ✓ (Opportunity → estimate → Job — Tier 1) |
| Technician mobile app | ✓ | ✓ | ✓ | ✓ (offline-capable) | ✓ (mobile app collection) |
| Billing & payments | ✓ (stored payment methods, recurring payments) | ✓ (AutoPay, collections) | ✓ (batch invoicing, automatic payments, card processing) | ✓ (postal mail invoices; QuickBooks) | ✓ (invoice after completion — Tier 1) |
| Customer communications/portal | ✓ (reminders, OMW, portal, chat) | ✓ (automated reminders; customer portal; trend reporting for multiple properties) | ✓ (confirmations, OMW texts, portal) | ✓ | ✓ (reminders — generic) |
| Accounting sync | ✓ (featureList "Accounting") | ✓ (QuickBooks Online) | ✓ (QuickBooks Online sync) | ✓ (QuickBooks) | ✓ (QuickBooks integration) |
| Bundled service packages | not observed on sampled pages | ✓ (general pest + termite + spider) | not observed on sampled pages | ✓ (pest + lawn integration) | — |

Legend: ✓ = directly observed on the product's official pages; ✓✓ = observed with unusual depth; — = not observed on sampled pages (absence of observation, not proof of absence).

## Canonical Abstraction

### L0 — Defining Invariant

Four jointly-held structures. Remove any one and the software stops being a pest control business management system:

1. **Customer with serviced structure(s)/property(ies)** — pest control work is delivered at the customer's building or property; the structure is a managed record bound to the customer, carrying site context (layout/diagram, access notes, units, pest/service history). Residential homes, commercial facilities, and multi-unit buildings (per-unit tracking at one address) are all realizations.
2. **The pest service visit as the unit of work** — a scheduled visit bound to customer + structure + time, with a lifecycle (scheduled → performed → completed → billed) and canonical shapes: recurring plan service, one-time/initial treatment, reservice (return visit), inspection (incl. wood-destroying-organism inspection). This visit record is the hub: findings, applications, devices, and billing all attach to it.
3. **Assigned technician** — the office decides who performs the work; the visit is assigned to a technician whose qualifications gate which work they can take (licensing/skill as routing constraint). Assignment is an office-managed act, distinct from the customer's agreement to service.
4. **Billing of the work** — completed visits resolve into money: per-visit invoices, recurring plan/subscription billing, autopay/card-on-file, collections.

Jointly-held load-bearing:
- 1 alone = contact/property list; 2 without 1 = free-floating work orders; 1+2 without 3 = self-service booking; 1+2+3 without 4 = dispatch board; 3+4 without 1+2 = generic payroll/billing pipeline.
- The trade context lives inside the objects (serviced structure, pest service visit) — the same family pattern as the sibling trade leaves. The specialized records below are the trade's standard capabilities, not the definition.

### L1 — Common Mature Structure

Present across the researched sample; expected in practice; additions to the core:

- **Recurring service plans** — service frequencies (e.g., monthly/bi-monthly/quarterly per PestPac's "service frequencies") generating visit occurrences; ongoing contracts with automated scheduling (FieldRoutes); subscription billing (GorillaDesk); renewals.
- **Route optimization** — batch-optimized stop sequences honoring drive time, technician settings (max production, time to leave, start/end locations), customer preferences, weather, and service due dates (PestPac RouteOp, FieldRoutes, GorillaDesk, Briostack).
- **Chemical/material application records** — master material list (name, manufacturer, EPA registration number, active ingredients, dilution rates), per-application capture (quantity, unit, method, device, target pests, areas treated), material use reports for state pesticide usage logs (by county or job), chemical data displayed on invoices/work orders (GorillaDesk deepest; PestPac, FieldRoutes, Briostack all carry it).
- **Monitoring device tracking** — bait stations, traps, glue boards as individually tracked devices (barcode, type, area, coordinates, check-in time, status, activity level), digital logbook, device data on paperwork for state compliance; positioned for commercial/facility business (GorillaDesk; not observed on the other products' sampled pages — treat depth as variable).
- **Inspection & findings capture** — activity, findings, GPS-mapped documentation, sketch/diagram tools (PestPac Sketch tool, GorillaDesk diagramming, Briostack bids & diagramming).
- **WDO/termite inspection reporting** — wood-destroying organism inspections with compliance forms (NPMA-33, California Branch 3 named by FieldRoutes; "Termite Inspection" in PestPac's featureList; termite industry line at GorillaDesk).
- **Sales pipeline** — leads, estimates/quotes, proposals with e-signature, bundled service packages (general pest + termite + spider at FieldRoutes), upsell from the field.
- **Technician mobile app** — day's route, job details, service history, chemical recording, photos/notes, upsell orders, payments; offline capability explicitly at Briostack.
- **Customer communications & portal** — reminders, on-my-way texts, review requests, portal with invoices/paperwork/chemical data.
- **Payments & collections** — card-on-file, autopay, payment reminders, batch invoicing.
- **Reporting/dashboards** — route productivity, collections, reservice rates (FieldRoutes blog), per-customer profitability.
- **Accounting sync** — QuickBooks across the sample.

### L2 — Variant / Optional Structure

- **Commercial/facility pole** — device-level compliance reporting, multi-unit buildings, facility-management-oriented paperwork (GorillaDesk device tracking positioning; FieldRoutes commercial/multi-unit; PestPac commercial line).
- **Termite/WDO as a specialized service line** — with baiting-system integrations (FieldRoutes + Sentricon) and real-estate-driven inspection reports.
- **Adjacent service lines on the same platform** — wildlife, mosquito (GorillaDesk); lawn care (Briostack, GorillaDesk, FieldRoutes' other industries); the clone-industry-page pattern.
- **Sales-culture machinery** — leaderboards, sales territories, commission tracking (Briostack, GorillaDesk growth plan).
- **Offline field capability** — explicit at Briostack; mobile apps generally.
- **Marketing automation / website builder / AI layers** — PestPac (Wavelytics, website builder), FieldRoutes (Marketing Pro), GorillaDesk (AI agents, review engine).
- **Postal mail fulfillment** of invoices/statements (Briostack).
- **Regulatory artifacts are variant-level, not core** — NPMA-33, California Branch 3, EPA registration numbers, county-level usage logs are US realizations of the generic concepts "compliance form" and "regulated application record". Regional products outside the US fit the Type without them.

### L3 — Vendor-specific (Research Notes only)

- PestPac: RouteOp (routing engine name), Wavelytics (AI decision-intelligence layer), WorkWave Forms, WorkWave integrated payments, marketplace.
- FieldRoutes: Sentricon system integration, Marketing Pro / Fleet Pro (ServiceTitan cross-sell), "legendary growth" positioning, PCT Top 100 growth claims.
- GorillaDesk: 150+ document library, VoIP & SMS plan, review engine, Pro-plan gating of device tracking, "13.3 hours/week" claim, account freeze for seasonal businesses.
- Briostack: Brio Office / Brio Tech / Brio Sales product split, leaderboards, postal mail service, EverCommerce parentage.
- Kickserv: On Hold as optional workflow column; Opportunity→estimate→Job naming.

## Rejected Findings (anti-overfit)

- **"Chemical tracking is the definition"** — rejected as L0. It is the most trade-distinctive *capability*, but it is a recorded content layer of the visit, present with varying depth (GorillaDesk gates device tracking to Pro; chemical tracking on all plans; Kickserv proves a pest company can run on a system with none of it). The visit loop, not the chemical record, is what the software orchestrates. Chemical records are L1 standard capability.
- **"Recurring quarterly plans are the definition"** — rejected. Recurring series exist generically (Kickserv Tier 1 recurring jobs); the plan is the trade's dominant revenue shape but one-time treatments, reservices, and inspections are also canonical visit shapes. Recurrence is L1.
- **"Route optimization is the definition"** — rejected. Routes are the trade's economics but a scheduling implementation layer; Kickserv has none and is still used by trades. L1.
- **"US regulatory forms (NPMA-33, CA Branch 3, EPA reg #) are the definition"** — rejected as era/region-specific realizations. The invariant is "application/treatment records supporting regulatory reporting", not any specific form. L2.
- **"Device tracking is the definition"** — rejected. Observed in depth at one product (GorillaDesk, Pro plan); commercial-pole capability. L1/L2.
- **Marketing metrics** (21%/30%/55%, 13.3 hrs/week, 2x growth, 3,700+ companies) — vendor claims, excluded entirely.
- **"Pest control software = field service software with a pest logo"** — rejected in the other direction: the sampled pest-dedicated products accumulate trade semantics (chemical records + regulatory reporting + devices + WDO + multi-unit + licensing) that the horizontal control lacks; the leaf is defensible as a trade variant with its own semantics.

## Historical / Market-Sample Check

Would older, regional, or differently positioned products still fit the L0?

- **Paper-era pest control office (1980s–90s)**: route cards/service tickets per customer address, technician assignment, handwritten treatment records, billing ledger for quarterly plans — customer + structure + visit + technician + billing all present with no cloud, GPS, or optimization engines. Fits.
- **Regional/non-US pest control businesses**: service visits + treatment records + billing under whatever local regime applies; no NPMA-33/EPA machinery needed. Fits — confirming US regulatory artifacts are variant-level.
- **Franchise/national operators** (PestPac's enterprise logos): same four structures at scale with branches and acquisitions. Fits.
- **Solo operator with a phone** (GorillaDesk's pole): same four structures, minimal machinery. Fits.

The definition names no protocol, form number, regulator, chemical database, deployment shape, or business model.

## Boundary Findings

- **vs Small Business Field Service Management (generic sibling)** — identical structural spine (customer → visit → dispatch → invoice; Kickserv documents it at Tier 1). Pest control differentiates by accumulated trade semantics: chemical/material application records with regulatory reporting, monitoring-device tracking, WDO/termite inspection reporting, multi-unit structures, licensing-gated routing, bundled pest packages. Removal test: remove the trade semantics and the generic FSM spine remains → generic Type; keep them and the pest leaf stands.
- **vs Lawn Care Business Management (chemical-application sibling; JOINT REVIEW flag discharged this pass)** — both are route-based recurring-visit businesses with chemical application records and applicator licensing; several vendors serve both as separate industry lines of one platform (GorillaDesk pest + lawn industries; Briostack pest + lawn; FieldRoutes pest + other field-service industries). The seam is the work object and regulatory regime: pest control treats **structures/interiors** for pests under structural pest control regulation (state agriculture/pesticide regulators; WDO inspection forms; monitoring devices at facilities), lawn care treats **turf** (fertilization/weed-control programs) under EPA-style pesticide reporting. Neither leaf's defining core contains the other's trade semantics. **Keep-both ratified as sibling trade variants of the FSM family.**
- **vs Pool Service Management (chemical sibling, unprocessed)** — same route + chemical + recurring pattern; seam = water chemistry/pool equipment vs pest treatment of structures. Flag for that leaf's pass.
- **vs Cleaning Business Management** — recurring visits, but indoor at unoccupied premises with no chemical/device/regulatory machinery; pest control's regulated chemical work is the structural difference.
- **vs Crop Protection Management (§20)** — agricultural pest control: customers are farms/growers, objects are fields/crops/applications under ag regimes; not the operator-side service-business system. Different Type despite shared word "pest".
- **vs Animal Control Management (§24)** — government/municipal animal control operations; different user, mandate, and record.
- **vs Home Inspection Application** — inspection-only, real-estate-transaction context, no treatment or recurring service loop. WDO inspection reporting in pest software serves the treatment business, not standalone inspection commerce.
- **vs Home Services / Local Service Marketplace** — demand-side discovery/booking across providers; this Type is one company's operator-side system of record.
- **vs Property Maintenance Management (§17)** — owner/landlord side of maintenance; pest control appears there as a procured trade, not the operator's system.
- **vs Enterprise Field Service Management (§14-adjacent)** — asset-intensive enterprise FSM; the §29 trade cluster is small-business operator-side. PestPac's enterprise tier shows the trade leaf scaling up without becoming that Type.

## Uncertainties

- No Tier-1 help-center documentation for any pest-dedicated product in this pass; workflow mechanics (exact visit states, exact chemical-record fields at other vendors, device workflows outside GorillaDesk) are described at the level vendor product pages state. GorillaDesk's help center timed out; ServSuite unreachable.
- Device tracking depth at PestPac/FieldRoutes/Briostack unverified (not observed on sampled pages; likely present given commercial positioning, but not asserted).
- Whether reservice (free return visit) is a first-class visit type across products — observed as a tracked metric in FieldRoutes' industry content only; described as a canonical visit shape with moderate confidence.
- Exact licensing-check behavior (hard gate vs soft flag) in routing — FieldRoutes names skillsets and license renewals; the enforcement depth is not documented in sampled sources.
- Termite protection renewal machinery (annual renewal fees common in the trade) — not directly observed in sampled pages; not asserted.

## Final Synthesis

Pest Control Management is the operator-side business management system of a pest control company. Its defining core is four jointly-held structures: customers with the structures/properties serviced for pests; the pest service visit as the unit of work (recurring plan service, one-time treatment, reservice, or inspection) with a scheduled→performed→completed→billed lifecycle; the assigned (licensed) technician; and billing. Around that core, mature products add the trade's standard machinery: recurring service plans with route-based scheduling, chemical/material application records with regulatory reporting, monitoring-device tracking, inspection findings and WDO/termite reporting, a sales pipeline with e-signed proposals and bundled packages, technician mobile apps, customer communications/portals, payments/collections, reporting, and accounting sync. The Type is a trade variant of the field-service family: remove the trade semantics and the generic FSM spine remains; the pest semantics (structures treated for pests under a regulated chemical regime) are what make the leaf.
