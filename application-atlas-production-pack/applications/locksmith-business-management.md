# Locksmith Business Management

## Overview

A **Locksmith Business Management** application is the business-management system of a locksmith (and often security-hardware) service company: it records customers and their service locations, carries each requested piece of lock, key, or security work as a durable job with a lifecycle, coordinates the locksmiths who perform the work in the field, and turns completed work into invoices and payments.

The defining core is small:

```text
Customer (with a service location)
└── Locksmith job — a requested piece of lock, key, or
    │   security-hardware work (emergency lockout, rekey,
    │   key work, lock repair or installation,
    │   electronic lock / access-control / key-control work)
    │   at that location, carried through a lifecycle
    │   (requested → scheduled → assigned → performed →
    │    completed → billed)
    └── Locksmith / technician as the executing role
        (assigned and coordinated by the office)
        └── Billing of the completed work (estimate → invoice → payment)
```

Everything else commonly associated with these products — dispatch boards, technician mobile apps, price books, customer notifications, service agreements, photo documentation, call tracking, dashboards — is standard capability that mature products add, not what makes the product a locksmith business management system. A one-van locksmith running on a job list, a calendar, and invoicing already satisfies the defining core; a multi-technician security company adds the coordination machinery on top.

The work happens where the lock or the customer is — a home, a business, a storefront, a facility, or the site of a lockout — so every job binds to a service address rather than to the locksmith's premises. The trade's own character shows in the work mix: locksmith companies live on emergency lockout calls (booked and dispatched in the moment, with speed and proximity mattering), rekeys, key work, lock repairs and installations, and — at the commercial pole — contracted security work on key control systems, master key systems, and electronic access control.

## Users & Context

Primary users:

- **Owner / operator** — configures services and pricing, monitors the job board and revenue, handles escalations. In small businesses this is often also the dispatcher and sometimes a locksmith.
- **Office staff / dispatcher** — answers calls (a large share of them urgent), creates customers and jobs, prepares estimates, schedules and assigns locksmiths, sends invoices, chases payments.
- **Locksmith / technician** — executes the work: receives assigned jobs, travels to the service location, performs the lockout, rekey, key work, lock installation, or security-hardware service, documents the work with notes and photos, collects signatures and payment.

Secondary participants:

- **Customer** — not an operator, but an active recipient of the system's output: appointment confirmations and reminders, estimates to approve, invoices to pay online, sometimes a self-service booking page or portal. At the commercial pole the customer-side actors include property managers, security officers, and HR teams who schedule jobs and review service history for the properties they manage.
- **Bookkeeper / accountant** — typically works through the accounting-system integration rather than the application itself.

Typical context: locksmith and security-service companies ranging from one-van owner-operators to multi-technician firms. Emergency lockouts and residential rekeys/lock work form the high-frequency rhythm; commercial accounts add contracted security work — key control, access control, master key systems — under service agreements and renewals. The office works in a web dashboard; locksmiths work in a mobile app; customers interact through calls, messages, payment links, and occasionally self-service surfaces.

## Core Model

### The Defining Core

**Customer.** A record of the person or business the work is for. Carries contact details, one or more service locations, notification preferences, and the history of past jobs and invoices. The service location matters structurally: locksmith work happens where the lock, door, or security hardware is installed — or where the locked-out customer is — so every job binds to an address. For property portfolios and commercial accounts, products commonly support a parent/sub-account structure — the company that owns or manages several properties is the billing parent, while each property is a service location with its own address and site information.

**Locksmith job (work order).** The unit of work and the center of the whole system. One job represents one engagement: what was requested, for whom, where, and its progress from request to billing. A job carries:

- the customer and service address
- the work description — what was requested and what the work involves (normally captured as job text, line items, photos, and notes rather than a structured model of the site's locks or keys)
- line items for services, parts, and hardware (locksets, deadbolts, rekeying, key work), priced from the business's price book
- schedule information and the assigned locksmith
- status (see Important Rules)
- the invoice and payments attached to it

Jobs fall into a recognizable trade mix: emergency lockouts (a locked-out home or business — urgent, same-day, often after hours), rekeys and key work (rekeying locks after a move or tenant turnover), lock repair and installation (failed locks, new locksets and deadbolts, electronic locks), and commercial security work (service and maintenance on security systems, key control systems, and access control, usually under contract). The researched market captures this work as job content — descriptions, line items, photos — rather than as a structured registry of the customer's locks or keys.

**Locksmith / technician (field technician).** The executing role. Jobs are assigned to field workers; the office coordinates them and the mobile app is their working surface. In a one-person business the assignment collapses to self-assignment, but the structure — a job has an executing role — remains.

**Billing.** Work beyond a simple service call is usually estimated first; the approved estimate converts into a job, and the completed job produces an invoice that collects payments (card, online, on-site). Deposits can be taken before work; accounting systems are kept in sync through integration.

### Standard Capabilities of Mature Products

These are near-universal in current products and make the core practical, but a product lacking some of them can still be recognized as this Type:

- **Estimates and proposals** — a quote object with line items, customer approval or e-signature, and one-step conversion into a job; multi-option estimates appear in the family's replacement-sales pattern.
- **Scheduling and dispatch** — a calendar of scheduled jobs and a board of job statuses; drag-and-drop rescheduling; assignment of technicians; live technician location and proximity-aware assignment in mature products — the capability the trade leans on hardest when a lockout call arrives.
- **Technician mobile app** — the field surface: assigned jobs, navigation, job details and customer history, photos, notes, signatures (often captured before and after the work), and on-site payment collection and invoicing.
- **Price book** — the business's catalog of services, parts, locks, and key work with prices, keeping quotes, invoices, and technician-created invoices consistent.
- **Customer notifications** — automated texts/emails for booking confirmation, day-of reminders, on-my-way alerts, and invoice delivery.
- **Multi-visit jobs** — one job spanning several visits, because locksmith work often requires a first visit to assess and a return visit once the right lock, key blank, or hardware arrives.
- **Recurring work** — recurring jobs and service agreements or memberships that generate scheduled visits and predictable revenue; at the commercial pole, contract renewals with performance summaries.
- **Reporting** — job lists, revenue, technician performance, and job profitability, filterable by job attributes such as service type, status, tag, and assigned technician.
- **Accounting sync** — integration with accounting software (in the North American small-business market, in practice QuickBooks).
- **Call handling (present in many current products)** — call routing and VoIP/text tooling; demand in this trade arrives by phone, and several products bundle phone-system features so urgent calls are captured and routed rather than missed.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:  Who the work is for
Implementations:  customer record with one location, customer with
                  multiple service locations, parent/sub-account
                  property hierarchies, commercial accounts with
                  property-manager/security-officer contacts

Concept:  What the work is
Implementations:  job description text + line items (locksets,
                  deadbolts, rekeying, key work), service types,
                  photos and notes; in some products a structured
                  site-equipment record with per-location service
                  history

Concept:  Job lifecycle
Implementations:  status columns on a job board, status fields,
                  appointments/work events scheduled against the job

Concept:  Technician coordination
Implementations:  dispatch board + mobile app, SMS job details,
                  GPS-backed proximity assignment; some products
                  route incoming calls by job type, priority, or
                  service area
```

Notably, the researched market usually captures the lock and key work itself as **job content** (description, line items, photos) rather than as a structured registry of keys, key codes, or master-key-system charts. Whether any product manages such key records as first-class objects could not be verified from reachable documentation and should not be assumed.

## How It Works

The canonical flow of a locksmith engagement:

```text
Call or booking request (often urgent; phone / web / repeat customer)
→ create or select customer + service location
→ create the locksmith job (describe the requested work)
→ [emergency] dispatch immediately — assign the nearest
   available locksmith; [non-urgent or larger work]
   send estimate → customer approves → convert to job
→ schedule the visit; assign a locksmith
→ customer receives confirmation and reminders
→ locksmith travels to the location; marks arrival
→ perform the work (open the lock, rekey,
   install or repair hardware, service the security system)
→ document: photos, notes, parts used, signature
→ invoice is generated from the job
→ payment collected on site or online
→ follow-up: contracted maintenance visit, or the next
   phase of a security installation
```

Four loops are worth distinguishing:

**The dispatch loop (daily, emergency-weighted).** The office sees the job board and calendar, balances the day's workload across locksmiths, and adjusts as calls come in. Status moves left to right — unscheduled → in progress → completed — with hold, cancellation, and rescheduling as side exits. The trade's signature behavior lives here: when the call is a lockout, the job is booked and dispatched in the same moment, assigned to the nearest available locksmith, with live location tracking and route guidance shaving arrival time. Some products route incoming calls by job type, priority, or service area so urgent calls reach the right person first.

**The multi-visit loop (per job).** Scheduling creates visits against the job. A job often needs a first visit to assess and a second to complete once the right lock, key blank, or hardware arrives; mature products keep one job open across its visits and only finalize the invoice when the work is complete.

**The money loop (per job).** Estimates become jobs; jobs become invoices; invoices collect payments; payments sync to accounting. Deposits can be collected at approval or before work; line items are priced from the price book, and on-site payment collection is standard because much of the trade's work is completed and paid for in one visit.

**The recurring loop (per plan).** Service agreements and memberships place scheduled visits on the calendar automatically — periodic lock service, security-system maintenance, and access-control checks, especially for commercial accounts — turning one-time customers into standing revenue, with contract renewals supported by performance summaries.

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Job board / dispatch board

The dispatcher's and owner's primary surface.

- jobs organized by status (commonly unscheduled → in progress → completed), with filters by service type, tag, technician, and time
- primary actions: create job, schedule/reschedule, assign locksmith, call or message customer, open a job

### Job detail page

The record of one engagement; the most information-dense surface.

- customer and service address, work description, line items, schedule and assigned locksmith, status, notes, photos, attached estimate, invoice and payments
- primary actions: edit details, add line items, schedule or add a visit, dispatch, add notes/photos, take a deposit, invoice, hold, cancel

### Schedule / calendar

- jobs and visits by day, week, or technician; drag-and-drop rescheduling; visit time slots
- primary actions: schedule a visit, reassign, adjust timing

### Customer profile

- contact details, service locations, job and invoice history, notification preferences; in some products site-equipment records with their service history
- primary actions: create a job for this customer, review history, message

### Estimate / proposal page

- line items, totals, approval/e-signature state
- primary actions: send, track approval, convert to job

### Technician mobile app

The field surface, organized around the locksmith's day.

- assigned jobs with details and customer history, navigation, status controls
- primary actions: start/complete visits, capture photos and notes, record parts used, collect signature, take payment, create and send an invoice

### Customer-facing surfaces

- appointment reminders and on-my-way messages (SMS/email)
- estimate approval and invoice payment links; in some products an online booking page (often positioned for round-the-clock requests) or a self-service portal with history and documents

### Reporting / dashboard

- job, revenue, and technician-performance views; job profitability by work type (lockout, rekey, install, contracted maintenance)

## Important Rules / Behaviors

### The job lifecycle is explicit and guarded

Jobs move through recognizable states — unscheduled, scheduled, in progress, completed — and the exits matter: unschedule (back to the pool), hold (paused), cancel (record kept, customer informed), complete (work finished, ready to bill). Mature products treat these as distinct actions with different consequences rather than one delete button, because each state change carries customer-facing and financial meaning.

### A job can span multiple visits

Scheduling creates visits against the job; the job stays open until its visits are done, and some products prompt whether all visits should close when the job is marked complete. Invoicing is typically finalized only when the work is complete — which is why assess-then-return (assess the door, order the lockset, return to install) work is modeled as one job with several visits, not several unrelated jobs.

### Estimates gate larger work

Work beyond a simple service call is usually estimated first; the customer's approval (often an e-signature) is what authorizes converting the estimate into a scheduled job. Deposits can be collected at approval, and the approved estimate — not a verbal agreement — is the record the invoice is built from.

### Pricing comes from the price book

Line items are normally drawn from the business's price book (services, parts, locks, key work), keeping quotes, invoices, and technician-created invoices consistent; custom line items remain possible for one-off situations.

### The service location and the billing entity can differ

Especially in commercial work, the place where work is performed (a property, a tenant space, a facility) is not necessarily the party that pays (an owner, a property manager, a corporate parent). Products that support this carry an explicit link between the two, and moving or severing that link affects historical invoices and payments.

### Documentation is part of the job

Photos, notes, parts used, and signatures are captured as part of completing a job — both as the business's record and as evidence shown to the customer. Some products structure this as signature capture before and after the work.

### Roles gate configuration

Day-to-day job work is open to office staff and locksmiths, while business-wide configuration — price book, service definitions, job forms and fields, employee records — is restricted to admin-level roles. Field locksmiths see and change their assigned jobs, not the business's settings.

## Variants

- **Emergency-led residential service** — the high-frequency segment; lockout calls booked and dispatched in the moment, rekeys and lock repairs for homeowners; consumer payments, review-driven reputation, and round-the-clock availability.
- **Commercial security service** — contracted work on key control systems, master key systems, and electronic access control for businesses and property portfolios; property managers and security officers as the customer-side actors; service agreements with renewals and performance summaries.
- **Locksmith-and-security businesses** — companies bundling locksmith work with alarm/security-hardware installation; the same job machinery carries both, and platforms package the adjacency either inside the locksmith trade page or as a separate security trade page.
- **Owner-operator (one van)** — the whole system collapses to one person: self-dispatch, simple job list, mobile-first usage.
- **Multi-technician / multi-location companies** — dispatch boards, technician performance reporting, business-unit or franchise structures.
- **Trade-agnostic tools configured for locksmiths** — the same structure is sold both as locksmith-labeled products and as general service-business tools that a locksmith company configures; the trade difference in the market is largely configuration and content, not a different model.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Small Business Field Service Management | closest sibling; same structural spine | generic service jobs vs locksmith-trade tuning (lock/key/security work content, emergency-heavy work mix with speed/proximity dispatch, commercial security contracts); vendors largely ship both as one product with trade configurations |
| Garage Door / HVAC / Plumbing / Electrical Service Management | trade siblings | same field-service spine with different trade objects and work content |
| Appliance Repair Management | trade sibling | that Type's distinguishing object is the customer's appliance as the unit of repair; here the unit of work is the lock, key, or security hardware at the site |
| Fire Protection / Elevator Service Management | trade siblings with a structural difference | those trades organize work around code-mandated recurring inspection programs with persistent deficiency records; locksmith work shows no such compliance loop |
| Fire and Security / alarm-business service | adjacent trade packaging | security-alarm installation is a sibling trade served by the same platforms; locksmith businesses frequently bundle access-control and security-hardware work, so the customer populations overlap — the boundary is trade content, not structure |
| Auto Repair Shop Management | different execution surface | automotive locksmith work (vehicle lockouts, vehicle key work) is field work at the vehicle's location as dispatched jobs, not shop-based repair orders against a customer vehicle record |
| Appointment Scheduling Application | fragment | booking is one capability here; this Type is the whole business operation (customers, jobs, technicians, billing) |
| Local Service Marketplace | demand-side adjacent | marketplace is consumer discovery/booking; this Type is operator-side execution and billing; a marketplace lead or an emergency call becomes a job here |
| CMMS / Enterprise Asset Management | different population | CMMS/EAM manages assets owned by the software's operator; this Type manages service work at customers' premises (customer-owned locks and access-control hardware appear, if at all, as optional site-equipment records) |
| Property Maintenance Management | different seat | property managers coordinate maintenance across their portfolios; this Type is the contractor's own business system — a property manager is a customer here |
| Physical access-control management systems | different software world | locksmiths install and service electronic access-control systems, but the systems that operate those locks day-to-day belong to the physical-security software world; this Type manages the service business around that work |

The most important boundary is with Small Business Field Service Management: the two share the entire structural spine, and the market largely sells locksmith business management as a configuration of field service products — one major home-services vendor serves the trade with no locksmith-specific package at all. The durable difference is semantic — lock, key, and security work content, the emergency-heavy work mix with speed/proximity dispatch, and the commercial security extension — and it is a gradient, not a wall.

## Representative Products

- **ServiceTitan** — flagship "software for the trades"; a commercial-focused Locksmith trade page over one platform
- **Service Fusion** — SMB–mid, all-in-one multi-trade field service suite with a dedicated "Locksmith" industry page ("locksmith and security business")
- **FieldPulse** — growing SMBs; dedicated Locksmith solution page with an emergency-call dispatch emphasis
- **Kickserv** — micro-SMB, simple and low-cost, trade-agnostic service business management (locksmith companies among many trades)
- **Housecall Pro** — micro-SMB home-services platform whose documented industry packages cover HVAC, electrical, and plumbing only; locksmith companies run the generic product

## Sources

Research date: **2026-09-08**

- ServiceTitan (Tier 2, official site): https://www.servicetitan.com/industries/locksmith-software
- Service Fusion (Tier 2, official site): https://www.servicefusion.com/locksmith-software
- FieldPulse (Tier 2, official site): https://www.fieldpulse.com/solutions/locksmith
- Kickserv Knowledge Center (Tier 1): https://kickserv.helpscoutdocs.com/article/32-jobs
- Housecall Pro Help Center (Tier 1): https://help.housecallpro.com/en/ — collection map incl. "Industry Packages"

> Sourcing limitation: Workiz (a major locksmith-marketing SMB vendor) was unreachable (HTTP 404 on two URL patterns, after earlier failures in a sibling pass) and was not retried; dedicated locksmith-vertical products (Locksmith Manager, The Professional Locksmith Software) could not be reached (connection failures), so the dedicated-vertical pole is unverified — whether any product manages key registries, key-code catalogs, or master-key-system records as first-class objects is deliberately not claimed. ServiceTitan, Service Fusion, and FieldPulse were reachable only at marketing/FAQ depth, not in help-center documentation, so claims drawn from them are limited to what their sites state. Precise numeric limits, plan-specific capabilities, and vendor-specific module names are intentionally not stated in this document. Market-wide statements are calibrated to the five researched products.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample breadth check are recorded in the paired Research Notes.
