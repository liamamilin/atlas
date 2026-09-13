# Appliance Repair Management

## Overview

An **Appliance Repair Management** application is the business-management system of an appliance repair operation: it records customers and their service locations, carries each requested repair as a durable job with a lifecycle, coordinates the technicians who perform the repairs in the field, and turns completed repairs into invoices and payments.

The defining core is small:

```text
Customer (with a service location)
└── Repair job — a requested repair of an appliance at that location,
    │   carried through a lifecycle (requested → scheduled → assigned →
    │   performed → completed → billed)
    └── Technician as the executing role (assigned and coordinated by the office)
        └── Billing of the completed repair (invoice → payment)
```

Everything else commonly associated with these products — estimates, dispatch boards, technician mobile apps, price books, customer notifications, photo documentation, recurring maintenance plans, GPS tracking, parts inventory — is standard capability that mature products add, not what makes the product an appliance repair management system. A one-van repair business running on a job list, a calendar, and invoicing already satisfies the defining core; a multi-technician company adds the coordination machinery on top.

The work happens where the appliance sits — a customer's home or business — which is what separates this Type from shop-based repair management: the software's center of gravity is dispatching people to places, not managing bays that things arrive at.

## Users & Context

Primary users:

- **Owner / operator** — configures services and pricing, monitors the job board and revenue, handles escalations. In small businesses this is often also the dispatcher and sometimes a technician.
- **Office staff / dispatcher** — answers requests, creates customers and jobs, schedules and assigns technicians, sends estimates and invoices, chases payments.
- **Technician** — executes the repair in the field: receives assigned jobs, travels to the service location, diagnoses and repairs the appliance, documents the work with photos and notes, collects signatures and payment.

Secondary participants:

- **Customer** — not an operator, but an active recipient of the system's output: appointment confirmations and reminders, "on my way" messages, estimates to approve, invoices to pay online.
- **Bookkeeper / accountant** — typically works through the accounting-system integration rather than the application itself.

Typical context: small service businesses (one to a few dozen technicians) working from vans; residential appliance repair is the dominant segment, with commercial equipment service (e.g., food-service equipment) as a common extension. The office works in a web dashboard; technicians work in a mobile app; customers interact through messages, payment links, and occasionally a self-service portal.

## Core Model

### The Defining Core

**Customer.** A record of the person or business the repair is for. Carries contact details, one or more service locations, notification preferences, and the history of past jobs. The service location matters structurally: the repair happens where the appliance sits, so every job binds to an address, not to the business's premises.

**Repair job (work order).** The unit of work and the center of the whole system. One job represents one repair engagement: what was requested, for whom, where, and its progress from request to billing. A job carries:

- the customer and service address
- the work description (what appliance, what problem) — normally captured as job text, line items, photos, and notes rather than a structured equipment registry
- line items for services and materials, priced from the business's price book
- schedule information and the assigned technician
- status (see Important Rules)
- the invoice and payments attached to it

**Technician.** The executing role. Jobs are assigned to technicians; the office coordinates them and the mobile app is their working surface. In a one-person business the assignment collapses to self-assignment, but the structure (a job has an executing role) remains.

**Billing.** The completed job produces an invoice, and the invoice collects payments (card, online, on-site). Deposits can be taken before work; accounting systems are kept in sync through integration.

### Standard Capabilities of Mature Products

These are near-universal in current products and make the core practical, but a product lacking some of them can still be recognized as this Type:

- **Estimates** — a quote object with line items, optional multiple options, customer approval or e-signature, and conversion into a job.
- **Scheduling and dispatch** — a calendar of scheduled jobs and a board of job statuses; drag-and-drop rescheduling; assignment of technicians; arrival windows.
- **Technician mobile app** — the field surface: assigned jobs, navigation, job details and history, photos and notes, signatures, and on-site payment collection.
- **Price book** — the business's catalog of services and materials with prices; flat-rate pricing entries (a fixed price per repair job rather than time-and-materials) are a common pattern in repair trades.
- **Customer notifications** — automated texts/emails for booking confirmation, day-of reminders, on-my-way alerts, and invoice delivery.
- **Multi-visit jobs** — one job spanning several visits (appointments or work events), because a repair often requires a diagnosis visit and a return visit once a part is obtained.
- **Photo documentation** — photos (often before and after the work) attached to the job, both for records and for customer communication.
- **Callbacks** — tracking of return visits for repairs that did not hold; a repair-trade concept that some products expose as a job attribute or report filter.
- **Recurring work / service plans** — recurring jobs and maintenance or membership plans for repeat preventive service.
- **Reporting** — job lists, revenue, and technician performance, filterable by job attributes.
- **Accounting sync** — two-way integration with accounting software (in practice, QuickBooks in the North American market).

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:  What was repaired
Implementations:  job description text, line items, photos,
                  custom job fields; in some products a structured
                  equipment/appliance record (make, model, serial)

Concept:  Job lifecycle
Implementations:  status columns on a job board, status fields,
                  appointment-based scheduling

Concept:  Technician coordination
Implementations:  dispatch board + mobile app, SMS job details,
                  GPS-backed status views
```

Notably, the researched market segment usually captures the appliance as **job content** (description, photos, parts as line items) rather than as a structured per-customer equipment registry. A structured appliance record with service history per unit is a common optional structure — more prevalent in enterprise-oriented products — and should not be assumed to be part of the core.

## How It Works

The canonical flow of a repair engagement:

```text
Request (phone / web / repeat customer)
→ create or select customer + service location
→ create the repair job (describe the appliance and problem)
→ [optional] send estimate → customer approves → convert to job
→ schedule the visit; assign a technician
→ customer receives confirmation and reminders
→ technician travels to the location; marks arrival
→ diagnose; perform the repair (or order a part and schedule a return visit)
→ document: photos, notes, parts used, signature
→ invoice is generated from the job
→ payment collected on site or online
→ follow-up: callback if the repair failed, warranty-period handling,
   or recurring maintenance scheduling
```

Three loops are worth distinguishing:

**The dispatch loop (daily).** The office sees the job board and calendar, balances the day's workload across technicians, and adjusts as jobs come in. Status moves left-to-right: unscheduled → in progress → completed, with hold and cancellation as side exits. The technician's app mirrors this: today's jobs, navigation, and status changes.

**The repair loop (per job).** Diagnosis may reveal the need for a part; the job then spans multiple visits — the first visit to diagnose, a second to install. Mature products model this with multiple appointments or work events on one job, keeping the job open until all visits are done and only then finalizing the invoice.

**The money loop (per job, batched).** Estimates become jobs; jobs become invoices; invoices collect payments; payments sync to accounting. Deposits can be collected up front; progress invoicing can bill a long job in stages.

## Interfaces

### Office dashboard / job board

The dispatcher's and owner's primary surface.

- today's and upcoming jobs, technician assignments, job statuses
- primary actions: create job, schedule/reschedule, assign technician, call or message customer, open a job

### Job detail page

The record of one repair engagement; the most information-dense surface.

- customer and service address, work description, line items, schedule and assigned technician, status, notes, photos, attached invoice and payments
- primary actions: edit details, add line items, schedule or add a visit, dispatch, add notes/photos, take a deposit, invoice, cancel or delete

### Customer profile

- contact details, service locations, job and invoice history, notification preferences
- primary actions: create a job for this customer, review history, message

### Estimate page

- line items, options, totals, approval/e-signature state
- primary actions: send, approve/decline tracking, convert to job

### Schedule / calendar

- jobs and visits by day, week, or technician; drag-and-drop rescheduling
- primary actions: schedule a visit, reassign, set arrival windows

### Technician mobile app

The field surface, organized around the technician's day.

- assigned jobs with details and customer history, navigation, status controls
- primary actions: start/complete visits, capture photos and notes, collect signature, take payment, create an invoice

### Customer-facing surfaces

- appointment reminders and on-my-way messages (SMS/email)
- estimate approval and invoice payment links; in some products a self-service portal or online booking page

## Important Rules / Behaviors

### The job lifecycle is explicit and guarded

Jobs move through recognizable states — requested/unscheduled, scheduled, in progress, completed — and the exits matter: **unschedule** (back to the pool), **cancel** (record kept, customer informed), **delete** (removed, usually restorable). Mature products commonly treat these as distinct actions with different customer-facing consequences — for example, notifying the customer when a job is canceled but not when it is merely unscheduled or deleted.

### A job can span multiple visits

Scheduling creates visits (appointments or work events) against the job; the job stays open until its visits are done. Invoicing is typically finalized only when the work is complete — which is why multi-visit repairs (diagnose, then return with the part) are modeled as one job with several visits, not several jobs.

### Estimates gate larger work

Work beyond a simple service call is usually estimated first; the customer's approval (often an e-signature) is what authorizes converting the estimate into a scheduled job. Deposits can be collected at estimate approval.

### Pricing comes from the price book

Line items are normally drawn from the business's price book (services, materials, flat-rate repair prices), keeping quotes and invoices consistent; custom line items remain possible for one-off situations.

### Roles gate configuration

Day-to-day job work is open to office staff and technicians, while business-wide configuration — price book, service definitions, job fields, employee records — is restricted to admin-level roles. Field technicians see and change their assigned jobs, not the business's settings.

### Documentation is part of the job

Photos (frequently before and after the work), notes, and signatures are captured as part of completing a job — both as the business's record and as evidence shown to the customer. This matters especially where work is performed under warranty.

### Callbacks are tracked, not hidden

A return visit for a repair that did not hold is recorded against the job history (as a callback attribute or linked job), because repeat failures drive both cost and reputation in repair trades.

## Variants

- **Residential appliance repair** — the dominant segment; in-home service, consumer payments, review-driven reputation.
- **Commercial / specialized equipment service** — restaurants, laundromats, medical and vending equipment; longer service agreements, purchase-order billing, tighter response-time expectations.
- **Warranty-authorized service agents** — shops doing manufacturer warranty work; jobs are priced and documented to the manufacturer's rules, and scheduling is driven by warranty obligations.
- **Owner-operator (one van)** — the whole system collapses to one person: self-dispatch, simple job list, mobile-first usage.
- **Multi-technician / multi-location companies** — dispatch boards, technician performance reporting, business-unit or franchise structures.
- **Installation-and-removal work** — some appliance businesses do deliveries, installations, and haul-aways alongside repairs; the job model stretches to cover non-repair visits.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Small Business Field Service Management | closest sibling; same structural spine | generic service jobs vs repair-trade semantics (diagnosis, callbacks, warranty-period work, parts, flat-rate repair pricing); vendors ship both as one product with trade wrappers |
| HVAC / Plumbing / Electrical Service Management | trade siblings | same field-service spine with different trade objects and regulations; appliance repair's distinguishing object is the customer's appliance as the unit of repair |
| Auto Repair Shop Management | adjacent repair management | shop-based (vehicle brought to bays; work order lives at the shop) vs field-based (technician travels to the appliance); dispatch/routing central here, bay logistics there |
| Appointment Scheduling Application | fragment | booking is one module here; this Type is the whole business operation (customers, jobs, technicians, billing) |
| Local Service Marketplace | demand-side adjacent | marketplace is consumer discovery/booking; this Type is operator-side execution and billing; a marketplace lead becomes a job here |
| CMMS / Enterprise Asset Management | different population | CMMS/EAM manages assets owned by the software's operator; this Type manages a service business whose work objects are customers' appliances |
| Customer Service Platform / Ticketing | different object | tickets track issue resolution conversations; repair jobs track field work that is scheduled, dispatched, performed, and billed |
| Inventory Management System | optional module | parts inventory appears inside some products of this Type, but the Type's center is the job lifecycle, not stock |

The most important boundary is with Small Business Field Service Management: the two share the entire structural spine, and the market largely sells appliance repair as a configuration of field service products. The durable difference is semantic — repair economics and repair-specific record-keeping — and it is a gradient, not a wall.

## Representative Products

- **Housecall Pro** — micro-SMB, customer-experience and payments-first; serves appliance repair through its general home-services core
- **Service Fusion** — SMB–mid, all-in-one multi-trade field service suite with a dedicated appliance-repair edition
- **Kickserv** — micro-SMB, simple and low-cost, trade-agnostic service business management

Other major products serving this market (Jobber, ServiceTitan, Workiz, FieldPulse) could not be researched from official documentation in this environment; see Sources.

## Sources

Research date: **2026-09-06**

- Housecall Pro Help Center (Tier 1): https://help.housecallpro.com/en/ — collections "Jobs, Invoices, and Estimates", "Scheduling", "Price Book", "Service Plans", "Invoicing", "HCP Payments"; articles "How to Create a Job", "The Job Details page Overview with Progress Invoicing and Appointments", "What's the difference between Unschedule, Cancel, and Delete?", "Get Started with Job Fields"
- Service Fusion (Tier 2 product pages): https://www.servicefusion.com/appliance-repair-software , https://www.servicefusion.com/field-service-management-software
- Kickserv Knowledge Center (Tier 1): https://kickserv.helpscoutdocs.com/ — "Kickserv Basics" category; article "Jobs"

> Sourcing limitation: official documentation for Jobber (help center and site returned 403), ServiceTitan (site JS-rendered, API docs unreachable), Workiz and FieldPulse (404) could not be accessed on 2026-09-06. Claims in this document are calibrated to the three researched products; market-wide statements are limited to structures observed across that sample. Precise numeric limits, plan-specific capabilities, and vendor-specific module names are intentionally omitted.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
