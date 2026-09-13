# Electrical Service Management

## Overview

An **Electrical Service Management** application is the business-management system of an electrical service company: it records customers and their service locations, carries each requested piece of electrical work as a durable job with a lifecycle, coordinates the electricians who perform the work in the field, and turns completed work into invoices and payments.

The defining core is small:

```text
Customer (with a service location)
└── Electrical job — a requested piece of electrical work
    │   (service call, repair, installation, or larger project)
    │   at that location, carried through a lifecycle
    │   (requested → scheduled → assigned → performed →
    │    completed → billed)
    └── Electrician as the executing role (assigned and
        coordinated by the office)
        └── Billing of the completed work (estimate → invoice → payment)
```

Everything else commonly associated with these products — dispatch boards, technician mobile apps, price books, customer notifications, recurring service plans, photo documentation, purchase orders, dashboards — is standard capability that mature products add, not what makes the product an electrical service management system. A one-truck electrical business running on a job list, a calendar, and invoicing already satisfies the defining core; a multi-crew company adds the coordination machinery on top.

The work happens where the electrical system sits — a customer's home, building, or facility — so every job binds to a service address rather than to the contractor's premises.

## Users & Context

Primary users:

- **Owner / operator** — configures services and pricing, monitors the job board and revenue, handles escalations. In small businesses this is often also the dispatcher and sometimes an electrician.
- **Office staff / dispatcher** — answers requests, creates customers and jobs, prepares estimates, schedules and assigns electricians, sends invoices, chases payments.
- **Electrician / field technician** — executes the work: receives assigned jobs, travels to the service location, performs service, repair, or installation, documents the work with notes and photos, collects signatures and payment.

Secondary participants:

- **Customer** — not an operator, but an active recipient of the system's output: appointment confirmations and reminders, estimates to approve, invoices to pay online, sometimes a self-service portal or booking page.
- **Bookkeeper / accountant** — typically works through the accounting-system integration rather than the application itself.

Typical context: electrical contractors and service companies ranging from one-van owner-operators to multi-crew firms. Residential and light-commercial service is the dominant rhythm (service calls, repairs, installations billed to consumers or small businesses); commercial electrical service adds recurring maintenance contracts, larger sites, and — in some companies — installation projects managed alongside service work. The office works in a web dashboard; electricians work in a mobile app; customers interact through messages, payment links, and occasionally self-service surfaces.

## Core Model

### The Defining Core

**Customer.** A record of the person or business the work is for. Carries contact details, one or more service locations, notification preferences, and the history of past jobs and invoices. The service location matters structurally: electrical work happens where the electrical system is, so every job binds to an address. For property portfolios, products commonly support a parent/sub-account structure — the company that owns or manages several properties is the billing parent, while each property is a service location with its own address and site information.

**Electrical job (work order).** The unit of work and the center of the whole system. One job represents one engagement: what was requested, for whom, where, and its progress from request to billing. A job carries:

- the customer and service address
- the work description — what was requested and what the work involves (normally captured as job text, line items, photos, and notes rather than a structured model of the building's electrical system)
- line items for services and materials, priced from the business's price book
- schedule information and the assigned electrician
- status (see Important Rules)
- the invoice and payments attached to it

**Electrician (field technician).** The executing role. Jobs are assigned to electricians; the office coordinates them and the mobile app is their working surface. In a one-person business the assignment collapses to self-assignment, but the structure — a job has an executing role — remains.

**Billing.** Work beyond a simple service call is usually estimated first; the approved estimate converts into a job, and the completed job produces an invoice that collects payments (card, ACH, online, on-site). Deposits can be taken before work; accounting systems are kept in sync through integration.

### Standard Capabilities of Mature Products

These are near-universal in current products and make the core practical, but a product lacking some of them can still be recognized as this Type:

- **Estimates and proposals** — a quote object with line items, commonly multiple priced options, customer approval or e-signature, and one-step conversion into a job.
- **Scheduling and dispatch** — a calendar of scheduled jobs and a board of job statuses; drag-and-drop rescheduling; assignment of electricians; visit time slots.
- **Technician mobile app** — the field surface: assigned jobs, navigation, job details and customer history, photos, notes, signatures (often captured before and after the work), and on-site payment collection and invoicing.
- **Price book** — the business's catalog of services and materials with prices. Flat-rate pricing entries (a fixed price per job rather than time-and-materials) are a common pattern in the electrical trade, and some products support per-line-item sales commissions for technicians.
- **Customer notifications** — automated texts/emails for booking confirmation, day-of reminders, on-my-way alerts, and invoice delivery.
- **Multi-visit jobs** — one job spanning several visits (work events or appointments), because electrical work often requires a diagnosis visit, a return visit for parts, or phased installation work.
- **Recurring work** — recurring jobs and service plans, memberships, or service agreements that generate scheduled visits and predictable revenue.
- **Reporting** — job lists, revenue, and technician performance, filterable by job attributes such as service type, status, tag, and assigned technician.
- **Accounting sync** — integration with accounting software (in the North American small-business market, in practice QuickBooks; larger commercial operations integrate with construction-oriented ERPs).
- **Purchasing machinery (common in mature products)** — purchase orders tied to a job's material line items, and sometimes parts inventory, so that materials ordered for a job are tracked from supplier to invoice.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:  Who the work is for
Implementations:  customer record with one location, customer with
                  multiple service locations, parent/sub-account
                  property hierarchies

Concept:  What the work is
Implementations:  job description text + line items, service types,
                  photos and notes; in some products a structured
                  site-equipment record (panels, generators, other
                  installed equipment) with per-location service history

Concept:  Job lifecycle
Implementations:  status columns on a job board, status fields,
                  appointments/work events scheduled against the job

Concept:  Technician coordination
Implementations:  dispatch board + mobile app, SMS job details,
                  GPS-backed status views; some commercial-oriented
                  products match dispatch by technician certification
                  and skill
```

Notably, the researched market usually captures the electrical work itself as **job content** (description, line items, photos) rather than as a structured registry of the customer's electrical installation. A structured site-equipment record with service history per unit is a common optional structure — more prevalent in commercial-oriented products — and should not be assumed to be part of the core.

## How It Works

The canonical flow of an electrical engagement:

```text
Request (phone / web / repeat customer)
→ create or select customer + service location
→ create the electrical job (describe the requested work)
→ [optional] send estimate / proposal → customer approves → convert to job
→ schedule the visit; assign an electrician
→ customer receives confirmation and reminders
→ electrician travels to the location; marks arrival
→ perform the work (service call, repair, installation phase)
→ document: photos, notes, materials used, signature
→ invoice is generated from the job
→ payment collected on site or online
→ follow-up: recurring maintenance visit, or the next phase of the work
```

Four loops are worth distinguishing:

**The dispatch loop (daily).** The office sees the job board and calendar, balances the day's workload across electricians, and adjusts as calls come in. Status moves left to right — unscheduled → in progress → completed — with hold, cancellation, and rescheduling as side exits. The technician's app mirrors this: today's jobs, navigation, and status changes. In commercial-oriented products the same loop may weigh technician certifications and skills against what the job requires.

**The multi-visit loop (per job).** Scheduling creates visits (appointments or work events) against the job. A job often needs a first visit to diagnose and a second to install or repair once parts arrive; mature products keep one job open across its visits and only finalize the invoice when the work is complete.

**The money loop (per job).** Estimates become jobs; jobs become invoices; invoices collect payments; payments sync to accounting. Deposits can be collected at approval or before work; larger engagements can be billed in phases. Materials for a job may be purchased through purchase orders tied to the job's line items.

**The recurring loop (per plan).** Service plans, memberships, and agreements place scheduled visits on the calendar automatically — preventive maintenance for panel inspections, generator service, or contract-mandated checks — turning one-time customers into standing revenue.

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Job board / dispatch board

The dispatcher's and owner's primary surface.

- jobs organized by status (commonly unscheduled → in progress → completed), with filters by service type, tag, technician, and time
- primary actions: create job, schedule/reschedule, assign electrician, call or message customer, open a job

### Job detail page

The record of one engagement; the most information-dense surface.

- customer and service address, work description, line items, schedule and assigned electrician, status, notes, photos, attached estimate, invoice and payments
- primary actions: edit details, add line items, schedule or add a visit, dispatch, add notes/photos, take a deposit, invoice, hold, cancel

### Schedule / calendar

- jobs and visits by day, week, or technician; drag-and-drop rescheduling; visit time slots
- primary actions: schedule a visit, reassign, adjust timing

### Customer profile

- contact details, service locations, job and invoice history, notification preferences; in some products site-equipment records with their service history
- primary actions: create a job for this customer, review history, message

### Estimate / proposal page

- line items, commonly multiple priced options, totals, approval/e-signature state
- primary actions: send, track approval, convert to job

### Technician mobile app

The field surface, organized around the electrician's day.

- assigned jobs with details and customer history, navigation, status controls
- primary actions: start/complete visits, capture photos and notes, record materials used, collect signature, take payment, create and send an invoice

### Customer-facing surfaces

- appointment reminders and on-my-way messages (SMS/email)
- estimate approval and invoice payment links; in some products an online booking page or a self-service portal with history and documents

### Reporting / dashboard

- job, revenue, and technician-performance views; in trade-tuned products, prebuilt dashboards for electrical business metrics (revenue, jobs, memberships, team performance)

## Important Rules / Behaviors

### The job lifecycle is explicit and guarded

Jobs move through recognizable states — unscheduled, scheduled, in progress, completed — and the exits matter: unschedule (back to the pool), hold (paused), cancel (record kept, customer informed), complete (work finished, ready to bill). Mature products treat these as distinct actions with different consequences rather than one delete button, because each state change carries customer-facing and financial meaning.

### A job can span multiple visits

Scheduling creates visits against the job; the job stays open until its visits are done, and some products prompt whether all visits should close when the job is marked complete. Invoicing is typically finalized only when the work is complete — which is why diagnose-then-return and phased installation work are modeled as one job with several visits, not several unrelated jobs.

### Estimates gate larger work

Work beyond a simple service call is usually estimated first; the customer's approval (often an e-signature) is what authorizes converting the estimate into a scheduled job. Deposits can be collected at approval, and the approved estimate — not a verbal agreement — is the record the invoice is built from.

### Pricing comes from the price book

Line items are normally drawn from the business's price book (services, materials, flat-rate job prices), keeping quotes, invoices, and technician-created invoices consistent; custom line items remain possible for one-off situations. Per-line-item commissions and surcharging rules, where supported, attach to the same price book.

### The service location and the billing entity can differ

Especially in commercial work, the place where work is performed (a property, a site, a tenant space) is not necessarily the party that pays (an owner, a property manager, a corporate parent). Products that support this carry an explicit link between the two, and moving or severing that link affects historical invoices and payments.

### Documentation is part of the job

Photos, notes, materials used, and signatures are captured as part of completing a job — both as the business's record and as evidence shown to the customer. Some products structure this as signature capture before and after the work.

### Roles gate configuration

Day-to-day job work is open to office staff and electricians, while business-wide configuration — price book, service definitions, job forms and fields, employee records — is restricted to admin-level roles. Field technicians see and change their assigned jobs, not the business's settings.

## Variants

- **Residential / light-commercial service** — the dominant segment; in-home and small-building service calls, repairs, and installations; consumer payments, memberships, and review-driven reputation.
- **Commercial electrical service** — larger customers and facilities; recurring maintenance contracts; multi-site work; site-equipment histories; purchase orders and tighter documentation; ERP integration instead of standalone accounting sync.
- **Electrical construction / installation projects** — some commercial contractors run larger installations (buildouts, fit-outs) alongside service work; products serving this pole add project machinery (quotes-to-contract, budgets, work-in-progress cost tracking, phased or progress billing). This drifts toward construction project management and is treated there as a separate Type.
- **Owner-operator (one truck)** — the whole system collapses to one person: self-dispatch, simple job list, mobile-first usage.
- **Multi-crew / multi-location companies** — dispatch boards, technician performance reporting, business-unit or franchise structures.
- **Trade-agnostic tools configured for electrical** — the same structure is sold both as electrical-labeled products and as general service-business tools that an electrical company configures; the trade difference in the market is largely configuration and content, not a different model.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Small Business Field Service Management | closest sibling; same structural spine | generic service jobs vs electrical-trade tuning (electrical work content, electrical pricing mechanics, trade-tuned dashboards, commercial electrical machinery); vendors largely ship both as one product with trade configurations |
| HVAC Service Management / Plumbing Business Management | trade siblings | same field-service spine with different trade objects and regulations |
| Appliance Repair Management | trade sibling | that Type's distinguishing object is the customer's appliance as the unit of repair; here the unit of work is the electrical work in the building's system |
| Construction Project Management | adjacent at the commercial pole | construction projects run on a project container with schedules, contracts, and cost control; this Type centers on the dispatched service loop; commercial electrical products bundle project machinery but the service spine remains the center |
| Utility Field Service Management | different operator entirely | utility-side workforce dispatch against grid assets owned by the utility vs contractor-side business management for electrical service companies |
| Appointment Scheduling Application | fragment | booking is one capability here; this Type is the whole business operation (customers, jobs, technicians, billing) |
| Local Service Marketplace | demand-side adjacent | marketplace is consumer discovery/booking; this Type is operator-side execution and billing; a marketplace lead becomes a job here |
| CMMS / Enterprise Asset Management | different population | CMMS/EAM manages assets owned by the software's operator; this Type manages service work at customers' premises (customer-owned infrastructure appears, if at all, as optional site-equipment records) |
| Fire Protection Service Management / Elevator Service Management | trade siblings | same field-service family with different regulated-trade objects |

The most important boundary is with Small Business Field Service Management: the two share the entire structural spine, and the market largely sells electrical service management as a configuration of field service products. The durable difference is semantic — electrical work content, electrical pricing and payment mechanics, and the commercial electrical extension — and it is a gradient, not a wall.

## Representative Products

- **Housecall Pro** — micro-SMB, residential and light-commercial electrical via an explicitly electrical-preconfigured package over its home-services core
- **Service Fusion** — SMB–mid, all-in-one multi-trade field service suite with a dedicated electrical edition
- **Kickserv** — micro-SMB, simple and low-cost, trade-agnostic service business management (electricians among many trades)
- **BuildOps** — commercial electrical service contractors; service, projects, and financials on one platform
- **ServiceTitan** — flagship "software for the trades" for residential and commercial electrical, one platform with a dedicated electrical edition

## Sources

Research date: **2026-09-07**

- Housecall Pro Help Center (Tier 1): https://help.housecallpro.com/en/ — collection map; "Industry Packages" collection; article "Electrical Package Overview": https://help.housecallpro.com/en/articles/15936816-electrical-package-overview
- Service Fusion (Tier 2 product page): https://www.servicefusion.com/electrical-contractor-software
- Service Fusion Support Center (Tier 1): https://servicefusion.zendesk.com/hc/en-us — root and featured-articles list; article "Customer Creation and Linking a Parent Account": https://servicefusion.zendesk.com/hc/en-us/articles/360024040551
- Kickserv Knowledge Center (Tier 1): https://kickserv.helpscoutdocs.com/ — "Kickserv Basics" category; article "Jobs": https://kickserv.helpscoutdocs.com/article/32-jobs
- BuildOps (Tier 2, official site with operational FAQ): https://buildops.com/industries/electrical
- ServiceTitan (Tier 2, official site): https://www.servicetitan.com/ and https://www.servicetitan.com/industries/electrical-software

> Sourcing limitation: Jobber — a major SMB generalist serving electricians — could not be accessed (HTTP 403 on two attempts) and is absent from the sample. Housecall Pro's electrical marketing page returned 403 (its help center was used instead). ServiceTitan and BuildOps were reachable only at marketing/FAQ depth, not in help-center documentation, so claims drawn from them are limited to what their sites state. Precise numeric limits, plan-specific capabilities, and vendor-specific module names are intentionally not stated in this document; trade practices suspected but not directly documented (permit tracking, electrical-code tooling) are deliberately omitted. Market-wide statements are calibrated to the five researched products.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample breadth check are recorded in the paired Research Notes.
