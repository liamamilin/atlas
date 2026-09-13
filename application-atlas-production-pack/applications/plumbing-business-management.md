# Plumbing Business Management

## Overview

A **Plumbing Business Management** application is the business-management system of a plumbing service and installation company: it records customers and their service locations, carries each requested piece of plumbing work as a durable job with a lifecycle, coordinates the plumbers who perform the work in the field, and turns completed work into invoices and payments.

The defining core is small:

```text
Customer (with a service location)
└── Plumbing job — a requested piece of work
    │   (service call, repair, maintenance visit,
    │    or fixture/equipment replacement-installation)
    │   at that location, carried through a lifecycle
    │   (requested → scheduled → assigned → performed →
    │    completed → billed)
    └── Plumber as the executing role
        (assigned and coordinated by the office)
        └── Billing of the completed work (estimate → invoice → payment)
```

Everything else commonly associated with these products — dispatch boards, plumber mobile apps, price books, customer notifications, maintenance memberships, photo documentation, dashboards — is standard capability that mature products add, not what makes the product a plumbing business management system. A one-van plumbing business running on a job list, a calendar, and invoicing already satisfies the defining core; a multi-truck company adds the coordination and selling machinery on top.

The work happens where the water systems are — a home, a commercial building, a facility — so every job binds to a service address rather than to the contractor's premises. The trade's own character shows in the work mix and the money: service calls, repairs, and maintenance visits sustain the day-to-day, much of it urgent; fixture and water heater replacements are product sales with high ticket values, sold through multi-option proposals and commonly financed; and recurring maintenance is packaged and sold as memberships whose covered visits include inspections, tank cleanings, and filter changes.

## Users & Context

Primary users:

- **Owner / operator** — configures services and pricing, monitors the job board, revenue, and membership counts, handles escalations. In small businesses this is often also the dispatcher and sometimes a plumber.
- **Office staff / dispatcher** — answers calls (including after-hours emergencies), creates customers and jobs, prepares estimates, schedules and assigns plumbers, sells and renews memberships, sends invoices, chases payments.
- **Plumber (field technician)** — executes the work: receives assigned jobs, travels to the service location, performs service calls, repairs, maintenance visits, or installations, documents the work with notes and photos, makes service recommendations, collects signatures and payment. Installation work may be performed by dedicated crews.

Secondary participants:

- **Customer** — not an operator, but an active recipient of the system's output: appointment confirmations and reminders, proposals to approve, invoices to pay online, membership benefits and renewal notices, sometimes a self-service booking page or portal.
- **Bookkeeper / accountant** — typically works through the accounting-system integration rather than the application itself.

Typical context: plumbing companies ranging from one-van owner-operators to multi-truck firms with multiple business units. Residential service and replacement is the dominant rhythm; light-commercial and commercial plumbing adds larger facilities, service agreements, and installation projects. Demand is strongly event-driven — failed water heaters and burst pipes do not wait for business hours — which makes call capture and schedule flexibility first-class concerns. The office works in a web dashboard; plumbers work in a mobile app; customers interact through messages, payment links, and occasionally self-service surfaces.

## Core Model

### The Defining Core

**Customer.** A record of the person or business the work is for. Carries contact details, one or more service locations, notification preferences, and the history of past jobs, invoices, and memberships. For property portfolios and commercial accounts, products commonly support a parent/sub-account structure — the company that owns or manages several properties is the billing parent, while each property is a service location with its own address and site information.

**Plumbing job (work order).** The unit of work and the center of the whole system. One job represents one engagement: what was requested, for whom, where, and its progress from request to billing. A job carries:

- the customer and service address
- the work description — what was requested and what the work involves (normally captured as job text, line items, photos, notes, and optionally a link to the equipment or fixture serviced)
- line items for services, parts, and materials, priced from the business's price book
- schedule information and the assigned plumber
- status (see Important Rules)
- the invoice and payments attached to it

Jobs fall into a recognizable trade mix: service calls (leaks, clogs, no hot water, running toilets), repairs (parts and labor on existing systems and fixtures), maintenance visits (often under a membership), and replacement-installation (a new water heater, softener, sump pump, or fixture set; larger repipes and remodel work — a product sale plus an installation, usually quoted with multiple priced options before the customer commits). Commercial work adds service-agreement visits and larger installation projects.

**Plumber (field technician).** The executing role. Jobs are assigned to field workers; the office coordinates them and the mobile app is their working surface. In a one-person business the assignment collapses to self-assignment, but the structure — a job has an executing role — remains.

**Billing.** Work beyond a simple service call is usually estimated first; the approved proposal converts into a job, and the completed job produces an invoice that collects payments (card, financing, online, on-site). Deposits can be taken before work; accounting systems are kept in sync through integration.

### Standard Capabilities of Mature Products

These are near-universal in current products and make the core practical, but a product lacking some of them can still be recognized as this Type:

- **Estimates and proposals** — a quote object with line items, commonly multiple priced options (good-better-best is the trade's normal presentation for replacement work), customer approval or e-signature, one-step conversion into a job, and follow-up automation on unsold estimates.
- **Scheduling and dispatch** — a calendar of scheduled jobs and a board of job statuses; drag-and-drop rescheduling; assignment of plumbers, in mature products weighted by skills, location, and availability; GPS-backed technician location.
- **Plumber mobile app** — the field surface: assigned jobs, navigation, customer and job history, photos, notes, service recommendations, signatures, on-site payment collection, and invoice creation.
- **Price book** — the business's catalog of services, parts, and materials with prices. A common trade implementation is flat-rate pricing: parts and labor bundled into client-ready single-price items, so every plumber quotes the same way; some products also tie per-line-item commissions to what each technician sells.
- **Maintenance memberships / service agreements** — recurring plans that place covered visits (inspections, tank cleanings, filter changes) on the calendar automatically and bill on a cadence; plan-selling at the customer's table or in the field is a standard sales motion, and membership counts are a first-class reporting figure.
- **Customer notifications** — automated texts/emails for booking confirmation, day-of reminders, on-my-way alerts, and invoice delivery.
- **24/7 call capture** — live or AI answering so emergency calls outside business hours are booked rather than lost; online booking pages that accept requests anytime.
- **Multi-visit and multi-day work** — one job spanning several visits (diagnose, then return with parts), and larger installations run as multi-day jobs with sections, costs, materials, and milestone billing.
- **Purchase orders and parts inventory** — purchase orders tied to a job's material line items, tracking what gets ordered, from which supplier, and when; stock-level visibility.
- **Reporting** — jobs, revenue, technician performance, membership counts, and job profitability, filterable by service type, status, and technician.
- **Accounting sync** — integration with accounting software (in the North American small-business market, in practice QuickBooks).
- **Seasonal and replacement-cycle marketing** — campaigns over the customer base for maintenance visits and replacement timing, keeping the schedule full between emergencies.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:  Who the work is for
Implementations:  customer record with one location, customer with
                  multiple service locations, parent/sub-account
                  property hierarchies

Concept:  What the work is
Implementations:  job description text + line items, service types,
                  photos, notes, checklists; in some products a
                  structured serviced-equipment record (make, model,
                  serial number, warranty, installation date and
                  location, per-unit service history)

Concept:  Job lifecycle
Implementations:  status columns on a job board, status fields,
                  work events/appointments scheduled against the job,
                  sections and phases on larger installation jobs

Concept:  Recurring maintenance
Implementations:  recurring jobs on a schedule, membership plans
                  with covered visits and billing cadences,
                  commercial service agreements

Concept:  Technician coordination
Implementations:  dispatch board + mobile app, SMS job details,
                  GPS-backed status views; assignment weighted by
                  skills, location, and availability in mature products
```

The serviced-equipment record deserves a note. Some products maintain a registry of the equipment the company has installed or serviced at each location — identity (make, model, serial number), warranty information, installation date and placement, and a per-unit service history. In this trade the most consequential such unit is the water heater: vendors publish replacement-lifespan benchmarks for it and support outreach to customers whose units are approaching the end of their expected life. The depth varies by product — some make it a first-class registry feeding replacement-timing offers and warranty disputes; others capture the same facts as job content. It should not be assumed to be part of the core, but it is one of the trade's most characteristic optional structures.

## How It Works

The canonical flow of a plumbing engagement:

```text
Request (phone — often urgent / web / repeat customer / membership due)
→ create or select customer + service location
→ create the plumbing job (describe the requested work,
  link equipment if known)
→ [optional] send estimate / proposal (often good-better-best
  for replacement work) → customer approves → convert to job
→ schedule the visit; assign a plumber
→ customer receives confirmation and reminders
→ plumber travels to the location; marks arrival
→ perform the work (service call, repair, maintenance, installation)
→ document: photos, notes, parts used, signature
→ invoice is generated from the job
→ payment collected on site or online (card / financing)
→ follow-up: membership sold or renewed, next maintenance visit
  scheduled, or the next phase of an installation
```

Four loops are worth distinguishing:

**The dispatch loop (daily).** The office sees the job board and calendar, balances the day's workload across plumbers, and adjusts as calls come in — with emergency calls (burst pipes, sewage backups, no water) taking priority and displacing scheduled work. Status moves left to right — unscheduled → in progress → completed — with hold, cancellation, and rescheduling as side exits. The plumber's app mirrors this: today's jobs, navigation, and status changes.

**The visit loop (per job).** Scheduling creates visits (appointments or work events) against the job. A repair often needs a first visit to diagnose and a second to fix once the right part arrives; a larger installation may span several non-consecutive days. Mature products keep one job open across its visits and only finalize the invoice when the work is complete.

**The money loop (per job).** Proposals become jobs; jobs become invoices; invoices collect payments; payments sync to accounting. Replacement work is commonly quoted with several priced options and financed; the chosen option becomes the invoice's basis. Parts for a job may be purchased through purchase orders tied to the job's line items. Flat-rate price books keep what different plumbers quote consistent.

**The membership loop (per plan).** Maintenance memberships place covered visits on the calendar automatically and bill on their cadence, turning one-time customers into standing revenue. The plan is also a selling surface: plumbers offer memberships at the customer's table during a job, and the office runs renewal and slow-season campaigns over the plan roster.

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Job board / dispatch board

The dispatcher's and owner's primary surface.

- jobs organized by status (commonly unscheduled → in progress → completed), with filters by service type, status, tag, technician, and time
- primary actions: create job, schedule/reschedule, assign plumber, call or message customer, open a job

### Job detail page

The record of one engagement; the most information-dense surface.

- customer and service address, work description, linked equipment, line items, schedule and assigned plumber, status, notes, photos, attached proposal, invoice and payments
- primary actions: edit details, add line items, schedule or add a visit, dispatch, add notes/photos, take a deposit, invoice, hold, cancel

### Schedule / calendar

- jobs and visits by day, week, or technician; drag-and-drop rescheduling; visit time slots
- primary actions: schedule a visit, reassign, adjust timing

### Customer profile

- contact details, service locations, job and invoice history, memberships, notification preferences; in some products the serviced-equipment registry for each location
- primary actions: create a job for this customer, review history, message, manage memberships

### Proposal / estimate page

- line items, commonly multiple priced options, totals, approval/e-signature state
- primary actions: send, track approval, convert to job, follow up on unsold proposals

### Equipment record

Where the product maintains one: a per-unit view of an installed water system or fixture.

- make, model, serial number, warranty information, installation date and location, service history
- primary actions: log a service visit against the unit, update details, register third-party equipment

### Plumber mobile app

The field surface, organized around the plumber's day.

- assigned jobs with details and customer history, navigation, status controls
- primary actions: start/complete visits, capture photos and notes, record parts used, present good-better-best options, collect signature, take payment, create and send an invoice

### Customer-facing surfaces

- appointment reminders and on-my-way messages (SMS/email)
- proposal approval and invoice payment links; in some products an online booking page or a self-service portal with history, documents, and memberships

### Reporting / dashboard

- job, revenue, and technician-performance views; membership counts; job profitability by work type (service, repair, maintenance, replacement, installation)

## Important Rules / Behaviors

### The job lifecycle is explicit and guarded

Jobs move through recognizable states — unscheduled, scheduled, in progress, completed — and the exits matter: unschedule (back to the pool), hold (paused), cancel (record kept, customer informed), complete (work finished, ready to bill). Mature products treat these as distinct actions with different consequences rather than one delete button, because each state change carries customer-facing and financial meaning.

### A job can span multiple visits and days

Scheduling creates visits against the job; the job stays open until its visits are done. Invoicing is typically finalized only when the work is complete — which is why diagnose-then-return repairs and multi-day installations are modeled as one job with several visits or sections, not several unrelated jobs.

### Proposals gate larger work

Work beyond a simple service call is usually estimated first; the customer's approval (often an e-signature) is what authorizes converting the proposal into a scheduled job. The approved proposal — not a verbal agreement — is the record the invoice is built from. Good-better-best presentation is the trade's normal sales motion for replacement work, and unsold proposals are commonly worked through follow-up automation.

### Pricing comes from the price book

Line items are normally drawn from the business's price book (services, parts, materials), keeping proposals, invoices, and plumber-created invoices consistent. Flat-rate bundling — one client-ready price covering parts and labor — is a common trade implementation for consistency across plumbers; custom line items remain possible for one-off situations.

### Membership visits are scheduled, not remembered

A membership's value is that its covered visits appear on the calendar automatically on their cadence and its covered terms apply at billing. Selling a membership mid-job (one signature, one payment) and renewing it on cycle are standard flows; lapsed memberships commonly become marketing targets rather than deleted records.

### Emergency calls displace the schedule

Plumbing demand is heavily event-driven. Mature products in this trade capture calls around the clock (live or AI answering, always-on booking pages) so emergency work is booked rather than lost; some products explicitly support an incoming emergency displacing already-scheduled work, with the displaced job rescheduled rather than dropped.

### The service location and the billing entity can differ

Especially in commercial work, the place where work is performed (a property, a facility, a tenant space) is not necessarily the party that pays (an owner, a property manager, a corporate parent). Products that support this carry an explicit link between the two.

### Documentation is part of the job

Photos, notes, parts used, and signatures are captured as part of completing a job — both as the business's record (including the warranty-dispute paper trail when equipment history is kept) and as evidence shown to the customer.

### Roles gate configuration

Day-to-day job work is open to office staff and plumbers, while business-wide configuration — price book, service definitions, forms and fields, employee records, commission settings — is restricted to admin-level roles. Field plumbers see and change their assigned jobs, not the business's settings.

## Variants

- **Residential service and replacement** — the dominant segment; emergency calls, repairs, maintenance visits, and water heater/fixture replacement sold to homeowners through good-better-best proposals and financing; memberships and review-driven reputation.
- **Light-commercial and commercial plumbing** — larger facilities and portfolios; service agreements; client portals; job costing.
- **Installation-led companies** — revenue weighted toward repipes, remodels, and new-construction plumbing; multi-day jobs with sections, milestone billing, and crew coordination; convergence with construction project machinery at this pole.
- **Adjacent-trade bundling** — plumbing companies commonly sell water treatment (softeners, filtration — filter changes are plan-covered work in sampled products), and co-market HVAC; vendors serve these as sibling trade configurations of the same platforms.
- **Owner-operator (one van)** — the whole system collapses to one person: self-dispatch, simple job list, mobile-first usage.
- **Multi-truck / multi-location companies** — dispatch boards, plumber performance and commission reporting, business-unit or franchise structures.
- **Trade-agnostic tools configured for plumbing** — the same structure is sold both as plumbing-labeled products and packages and as general service-business tools that a plumbing company configures; the trade difference in the market is largely configuration and content, not a different model.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Small Business Field Service Management | closest sibling; same structural spine | generic service jobs vs plumbing-trade tuning (emergency-heavy demand, water heater replacement economy, flat-rate pricing culture, membership plans); vendors largely ship both as one product with trade configurations |
| HVAC / Electrical Service Management | trade siblings | same field-service spine with different trade objects and regulations; HVAC shares the equipment-replacement economy (furnace/AC ≈ water heater), electrical shares the trade-page packaging |
| Appliance Repair Management | trade sibling | that Type's distinguishing object is the customer's appliance as the unit of repair; here the unit of work is the building's fixed water systems and fixtures — the water heater sits near this boundary but is installed building equipment |
| Water Treatment / Septic Service Management | trade siblings on the same platforms | adjacent trades plumbing companies often bundle; vendors ship them as separate labeled configurations of one product |
| Fire Protection / Elevator Service Management | trade siblings with a structural difference | those trades organize work around code-mandated recurring inspection programs with persistent deficiency records; plumbing maintenance is voluntary and sold, with no such compliance loop observed |
| CMMS / Enterprise Asset Management | different ownership side | CMMS/EAM manages assets owned by the software's operator; any equipment records here are a registry of customer-owned equipment maintained for service purposes |
| Construction Project Management | adjacent at the installation pole | construction projects run on a project container with schedules, contracts, and cost control; this Type centers on the dispatched service loop; installation-led companies bundle project machinery but the service spine remains the center |
| Utility Field Service Management | different operator entirely | utility-side workforce dispatch against network assets owned by the utility vs contractor-side business management for plumbing companies |
| Appointment Scheduling Application | fragment | booking is one capability here; this Type is the whole business operation (customers, jobs, plumbers, memberships, billing) |
| Local Service Marketplace / Home Services Marketplace | demand-side adjacent | marketplaces are consumer discovery/booking; this Type is operator-side execution and billing; a marketplace lead becomes a job here |
| Property Maintenance Management | different seat | property managers coordinate maintenance across their portfolios; this Type is the contractor's own business system — a property manager is a customer here |

The most important boundary is with Small Business Field Service Management: the two share the entire structural spine, and the market largely sells plumbing business management as a configuration of field service products — one major home-services vendor serves the trade through a preconfigured package built entirely from generic capabilities, and another class of tools serves it with no trade layer at all. The durable difference is semantic — the emergency-heavy demand pattern, the water heater replacement economy, flat-rate pricing culture, the replacement sales motion, and membership plans — and it is a gradient, not a wall.

## Representative Products

- **ServiceTitan** — flagship "software for the trades"; plumbing as a headline trade across residential, commercial, and construction poles on one platform, with the deepest trade content (estimating tooling, platform-data research on replacement cycles)
- **FieldEdge** — trades-heritage product for SMB and mid-market multi-truck operations; flat-rate pricing and service-agreement selling as named product pillars
- **Workiz** — SMB home-services platform with a dedicated plumbing industry page; documents explicit emergency-call handling and plumbing-specific plan work (tank cleanings, filter changes)
- **Housecall Pro** — micro-SMB home-services platform whose help center documents a dedicated preconfigured Plumbing package (one of only three industry packages)
- **Kickserv** — micro-SMB, simple and low-cost, trade-agnostic service business management (plumbing companies among many trades)

The Core Model was checked against a trade-agnostic sample (Kickserv) and a multi-trade clone-page vendor (Service Fusion) to avoid over-fitting to one vendor's trade packaging.

## Sources

Research date: **2026-09-09**

- ServiceTitan (Tier 2, official site): https://www.servicetitan.com/industries/plumbing-software — plumbing industry page incl. FAQ; https://www.servicetitan.com/industries/plumbing-software/estimating — estimating sub-page; https://www.servicetitan.com/toolbox/state-of-the-trades/trends/residential-water-heater-replacement-seasonal-trends — platform-data trends article
- FieldEdge (Tier 2, official site): https://fieldedge.com/plumbing-software/ — plumbing page incl. FAQ
- Workiz (Tier 2, official site): https://www.workiz.com/industries/plumbing-software/ — plumbing industry page incl. FAQ
- Housecall Pro Help Center (Tier 1): https://help.housecallpro.com/en/collections/19689640-industry-packages (Industry Packages), https://help.housecallpro.com/en/articles/15936858-plumbing-package-overview (Plumbing Package Overview)
- Kickserv Knowledge Center (Tier 1): https://kickserv.helpscoutdocs.com/article/32-jobs — "Jobs"
- Service Fusion (Tier 2, official site): https://www.servicefusion.com/plumbing-software — plumbing industry page incl. FAQ

> Sourcing limitation: Jobber, Simpro, ServiceTrade, and Successware — major players serving plumbing companies — could not be accessed (HTTP 403 / WAF rejections, this and prior research passes), so market coverage is calibrated to the six researched products. ServiceTitan, FieldEdge, Workiz, and Service Fusion were reachable only at marketing/FAQ depth, not in help-center documentation, so claims drawn from them are limited to what their sites state. Trade practices suspected but not directly documented (backflow-testing records, drain-camera/jetting tooling, licensing and permit structures, regional markets outside North America) are deliberately omitted, and no precise numeric limits, plan tiers, or vendor-specific module names are stated in this document.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample breadth check are recorded in the paired Research Notes.
