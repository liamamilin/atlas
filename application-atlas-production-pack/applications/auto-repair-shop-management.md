# Auto Repair Shop Management

## Overview

An **Auto Repair Shop Management** application is the business-management system of a vehicle repair shop: it keeps structured records of customers and their vehicles, carries each service engagement as a repair order with a lifecycle from write-up to payment, composes the work as labor and parts, coordinates the front-counter staff who sell and administer with the technicians who fix the vehicles, and closes the money loop with invoices and payments.

The defining core is small:

```text
Customer
└── Vehicle — identified, structured record of the vehicle being serviced
    │   (identity + per-vehicle service history)
    └── Repair order — the unit of work binding customer × vehicle × requested service,
        │   carried through a lifecycle (written up → estimated → authorized →
        │   worked → completed → invoiced → paid)
        └── Labor and parts as the substance of the priced work
        └── Shop-side execution — front counter writes up and manages,
            technicians perform and document the work in the shop
```

Two properties separate this from neighboring repair-management types. First, the work happens **at the shop**: customers bring or send vehicles in, and the shop's bays and technicians are the capacity — so the software coordinates a building, not a fleet of vans. Second, the **vehicle is a first-class record**: repairs bind to a specific vehicle whose identity and service history persist across visits, which is what lets a shop answer "what did we do to this car, and when, and at what mileage" years later.

Everything else commonly associated with these products — digital inspections, appointment calendars, parts catalogs, pricing matrices, technician time tracking, text approvals, reporting — is standard capability that mature products add, not what makes the product a shop management system. A two-bay garage running repair orders from a job list, an estimate sheet, and an invoice already satisfies the core; a twelve-bay shop layers coordination, inventory, and pricing controls on top.

## Users & Context

Primary users:

- **Service advisor / service writer** — the front counter. Greets the customer, creates or finds the customer and vehicle, writes up the repair order from the customer's concerns, builds and sends estimates, obtains authorizations, keeps the customer informed while work progresses, and checks out and invoices at the end. In small shops this is often the owner.
- **Technician** — performs the work in the bays. Receives assigned repair orders, inspects the vehicle, documents findings (often with photos and video), performs approved work, and records the time spent. A shop has several; a shop owner may also be the only one.
- **Parts / inventory staff** — manage the parts room: stock levels, ordering from suppliers, receiving, issuing parts to repair orders, cores and returns. In small shops this role collapses into the service advisor or owner.

Secondary participants:

- **Owner / manager** — sets labor rates and parts pricing, watches the workflow board and reports, manages staffing and performance.
- **Bookkeeper / accountant** — typically works through the accounting-system integration rather than the application itself.
- **Customer** — not an operator, but an active recipient: receives estimates and inspection reports to approve, progress updates, and the final invoice with payment options. **Fleet operators** (businesses owning several vehicles) are a recurring customer type with their own billing patterns.

Typical context: independent repair shops, tire shops, quick-lube shops, and heavy-duty truck shops, ranging from one bay to multi-location groups. The front counter works in a web or desktop application; technicians work from tablets or phones in the bays; customers interact through texts, approval links, and payment links.

## Core Model

### The Defining Core

**Customer.** The person or business paying for the work. Carries contact details, communication preferences, and the history of past repair orders. A customer may have one vehicle or many; businesses may have dozens (fleet accounts).

**Vehicle.** The object of repair and the anchor of the shop's institutional memory. A structured record — commonly year/make/model, VIN or license plate, mileage/odometer — that persists across visits. Every repair order attaches to a specific vehicle, and the vehicle's history (every visit, service, and odometer reading) accumulates on the record. This is why the vehicle is structural and not just text on a ticket: parts must fit the vehicle, services are recommended by mileage, and warranty claims depend on knowing what was done and when.

**Repair order (RO).** The unit of work and the center of the whole system. One repair order represents one service engagement: the customer and vehicle, the reported concerns, the inspected findings, the approved work, and its progress from write-up to payment. A repair order carries:

- the customer and vehicle (with odometer at check-in)
- the work description — reported symptoms and inspection findings
- **labor line items** — services priced as time × rate (often from a labor guide's book time for the operation)
- **parts line items** — drawn from the shop's inventory or ordered from supplier catalogs
- status and assignment (which technician is on it, where it sits in the shop's workflow)
- the invoice and payments attached to it

**Labor and parts.** The substance of priced work. Labor is sold as defined operations with times and rates; parts are physical stock with costs, prices, and supply chains. The repair order is where they meet — which distinguishes a repair order from a flat-price service transaction.

**Shop-side execution.** A front-counter role administers (writes up, estimates, invoices); technicians execute (inspect, repair, document). The system's job is to keep these two sides synchronized — what was promised, what was found, what was approved, what was done, what is owed.

### Standard Capabilities of Mature Products

These are near-universal in current products and make the core practical, but a product lacking some of them can still be recognized as this Type:

- **Appointments and reminders** — a calendar of scheduled visits, confirmation and reminder messages, and increasingly online booking.
- **Estimates with authorization** — the estimate lists proposed labor and parts; the customer approves (often per line, increasingly with an e-signature or a text approval). Declined lines are kept on record so the shop can follow up later; some products track "recommended" or "deferred" services as first-class objects.
- **Digital vehicle inspections (DVI)** — technician-performed multi-point inspections using templates, with photos, videos, and markups, sent to the customer to justify recommendations. Inspection templates can map findings to pre-defined services that flow onto the repair order.
- **Workflow board** — the shop's status at a glance: repair orders arranged by stage (estimates, vehicles dropped off, work in progress, ready for pickup, invoiced). The board is the daily operating surface of the whole shop.
- **Technician assignment and time tracking** — work is assigned to technicians; technicians clock on and off jobs; the system compares clocked time against billed labor time to measure efficiency.
- **Labor operations** — a catalog of services with book times and prices ("canned services"), so a common job builds in a click instead of being re-assembled.
- **Parts inventory and supplier catalogs** — stock levels with minimums and restocking suggestions; direct ordering from integrated supplier catalogs with price and availability comparison; purchase orders; reservations of parts to specific jobs; returns; and tracking of cores (returnable old parts that carry a refundable charge).
- **Pricing controls** — labor rates, parts markup matrices or multi-level price lists, and margin warnings, so quoted prices stay consistent and profitable.
- **Per-vehicle history and mileage-based reminders** — odometer recorded per visit; services recommended by mileage; reminders generated from the vehicle's history.
- **Invoicing and payments** — the invoice generated from the approved work (parts, labor, taxes, shop supplies); deposits; counter, online, and text-to-pay collection; statements for account customers.
- **Warranty attribution** — work can be attributed as customer-pay, warranty (manufacturer or extended), or internal, with different documentation requirements; the performing technician and odometer are recorded because warranty follow-ups depend on them.
- **Reporting and accounting sync** — sales, technician productivity, inventory usage, receivables; integration with accounting software.
- **Two-way customer messaging** — approvals, updates, and payments by text/email without phone tag.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:  Vehicle identity
Implementations:  manual entry, VIN decode, license-plate lookup,
                  VIN/barcode scanning from a mobile app

Concept:  Repair-order lifecycle
Implementations:  status columns on a workflow board; separate order
                  documents (estimate → repair order → invoice) with
                  conversion actions; posted/unposted accounting states

Concept:  Labor content
Implementations:  labor-operation codes with guide times, freeform
                  labor lines, pre-composed service bundles

Concept:  Parts sourcing
Implementations:  in-house stock, multi-supplier catalog comparison
                  with one-click ordering, special orders, transfers
                  between locations

Concept:  Customer authorization
Implementations:  e-signature, text-message approval, verbal
                  approval recorded by the advisor
```

Notably, the researched market treats **labor as sold time measured against a guide** and **parts as managed stock tied into external supply chains** — both far more structured than the "materials as line items" pattern of smaller trade businesses. Matrix or multi-level parts pricing and book-time labor are the category's pricing backbone.

## How It Works

The canonical flow of a service engagement:

```text
Customer request (walk-in, phone, online booking, or fleet order)
→ create or select customer + vehicle (VIN/plate lookup; record odometer)
→ write up the repair order (customer concerns, requested services)
→ vehicle received ("dropped off"); technician assigned
→ inspect (often a digital inspection with photos/video)
→ build the estimate (labor operations + parts)
→ send for authorization; customer approves — or declines — line by line
→ check stock; order missing parts from supplier catalogs (PO)
→ technician clocks onto the job; performs and documents the work
→ work completed and quality-checked
→ invoice generated from approved work (parts + labor + taxes + supplies)
→ payment collected (counter, online link, text-to-pay, or account)
→ follow-ups: declined work, mileage-based reminders, warranty callbacks
```

Four loops are worth distinguishing:

**The front-counter loop (per visit).** The advisor moves the engagement from request to estimate to authorization to invoice. The estimate is the gate: work is performed only after authorization, and declined work stays in the system as a future sales opportunity rather than disappearing.

**The back-shop loop (per vehicle in the shop).** The workflow board shows every vehicle and its stage; the manager dispatches work to technicians based on their current load; technicians clock on, inspect, document, and communicate findings back to the front counter (a work-in-progress channel on the RO is common). When diagnosis reveals new work, the estimate loop repeats mid-visit.

**The parts loop (per job, continuous).** Jobs source parts from inventory, reserved to the specific repair order; missing parts are ordered through integrated supplier catalogs; received parts are checked in; removed cores go back for credit. The inventory record updates with every RO.

**The money loop (per job, batched).** Deposits can be taken up front; invoices are generated from approved work; payments are collected in whatever channel the customer uses; accounting systems are kept in sync. Fleet and account customers may settle on statements rather than per-visit.

A fifth loop runs across visits: **retention** — declined and deferred work, mileage-based service reminders, and the vehicle's history make the next visit easier to sell and to serve.

## Interfaces

### Workflow / job board

The shop's daily operating surface for everyone.

- every open repair order as a card or row, arranged by stage (estimates, dropped off, in progress, ready, invoiced); vehicle, customer, assigned technician, and status at a glance
- primary actions: create repair order, move stage, assign technician, open the RO

### Repair order page

The record of one engagement; the most information-dense surface.

- customer and vehicle (with odometer), concerns and findings, labor and parts line items with prices, estimates and authorizations, assigned technician and clocked time, inspection results, invoice and payments
- primary actions: add/modify labor and parts, build estimate, request approval, order parts, assign or transfer technician, document notes and photos, invoice, unpost or adjust

### Estimate builder and inspection surface

- estimate: line items from labor operations and the parts catalog, totals, approval status and customer response
- inspection: template-driven checklists performed from a tablet or phone, with photos, videos, and notes; results sent to the customer; approved findings flow onto the RO

### Technician view (mobile/tablet app)

- assigned jobs with the vehicle and work details, today's sequence, inspection and documentation tools, clock-in/clock-out per job
- primary actions: start/stop work, record findings, capture photos and signature, message the front counter

### Calendar / appointments

- visits by day/week, technician or bay load, arrival times
- primary actions: book, reschedule, confirm, send reminders

### Customer and vehicle profile

- contact details, all vehicles owned, each vehicle's complete service history (visits, services, odometer, declined recommendations), invoices and payments
- primary actions: create an RO for this vehicle, review history, message, take payment

### Inventory / parts

- stock list searchable by part number, brand, or bin; quantities, price levels, minimums
- primary actions: order from supplier catalogs, receive POs, reserve parts to jobs, record returns and cores

### Reports and settings

- reports: sales, technician efficiency, inventory usage, receivables, inspectable by date range and staff
- settings: labor rates, parts pricing matrices, taxes and shop-supply fees, inspection templates, user roles and permissions

## Important Rules / Behaviors

### The vehicle anchors history — and the odometer comes with it

Every visit records the vehicle's odometer. This is not bookkeeping decoration: mileage-based service recommendations, warranty-parts tracking, and the customer's resale documentation all depend on it. The vehicle's history is the shop's memory, and in multi-location groups it follows the vehicle across stores.

### Work is authorized before it is performed — and declined work is kept

The estimate gates the work; approvals (and declines) are recorded per line. Declined or deferred recommendations remain attached to the vehicle so the shop can follow up at the next visit. Inspections exist largely to produce this evidence: a photo of the worn part converts "trust me" into a visible decision.

### The repair order moves through guarded states

Estimates convert into repair orders, repair orders into invoices — either manually or automatically when payment completes. Finalized invoices can typically be adjusted only through explicit reversal (unpost) actions rather than silent edits, because posted work feeds accounting. Deleting a paid or posted record is constrained; refunds and line-item reversals are their own recorded operations.

### Labor is billed on book time; actual time is measured against it

The customer is quoted and billed the guide time for an operation at the shop's labor rate, while the technician's actual clocked time is tracked separately. The ratio between them (efficiency) is a managed performance metric — it drives dispatching, coaching, and pay in many shops, but it is a measurement layer, not the billing itself.

### Parts are accountable stock

Parts on a repair order come from inventory (reserved and issued) or from a purchase order; returns go back to stock; cores come back for credit. This keeps job costs real and prevents the quiet leak of shop inventory.

### Money has attribution categories

Lines and payments are attributed as customer-pay, warranty, or internal. Warranty work carries extra documentation (the performing technician, the odometer, the failed part) because warranty reimbursements and callbacks are contested after the fact.

### Roles gate configuration and money

Day-to-day work is open to advisors and technicians; business-wide configuration — labor rates, pricing matrices, taxes, user accounts — and financial adjustments are restricted to manager/admin roles. Technicians see their assigned work, not the shop's books.

## Variants

- **General mechanical repair** — the core case: diagnostics, maintenance, and repairs on consumer vehicles.
- **Tire shops** — high-volume fitment work; tire inventory and fitment data are prominent; the RO lifecycle is compressed.
- **Quick lube** — very high volume, standardized services; repair orders are generated in seconds from the vehicle (some products build an oil-change RO from the last-service sticker); inspections thin but upsell-driven.
- **Heavy-duty / truck shops** — commercial vehicles and fleet customers; larger jobs, statement billing across many vehicles, stricter compliance documentation.
- **Fleet-centric shops** — service businesses whose customers are companies with vehicle pools; batch invoicing and account statements replace per-visit payment.
- **Multi-location groups** — the same core multiplied: cross-location vehicle history, consolidated reporting, shared pricing standards, parts transfers between stores.
- **Mobile mechanics** — an edge variant that drifts toward field service management, since the shop travels to the vehicle; the repair-order core survives, the shop-side coordination does not.

A variant remains a variant of this Type as long as the vehicle-anchored repair order with labor-and-parts economics still describes it; when the shop stops being the fixed place of work, the Type boundary is crossed.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Collision Repair Management | closest sibling | same repair-order spine, but estimating from accident damage against insurance claims, with paint/materials and frame work; insurer-pay attribution dominates over customer-pay |
| Appliance Repair Management | repair-pattern sibling | field-based (technician travels to the appliance; dispatch/routing central; job binds to a location) vs shop-based (vehicle brought in; job binds to the shop); appliance captured as job content vs vehicle as a structured record; book-time labor and parts stock vs service-call economics |
| Fleet Management System | different population | manages vehicles owned by the software's operator (telematics, drivers, routes); this Type serves customers who own the vehicles; fleet accounts here are customers, not managed assets |
| Vehicle Inspection / Diagnostic Application | fragment | the digital inspection is one module inside this Type; standalone inspection/diagnostic products are technician instruments without the business lifecycle |
| Car Wash / Detailing Management | adjacent sibling | appearance services with package pricing and quick turnover; no diagnostic labor-and-parts composition |
| Appointment Scheduling Application | fragment | booking is one module; this Type is the whole shop operation (ROs, parts, technicians, money) |
| Small Business Field Service Management | different execution surface | field service dispatches people to customer locations; this Type receives vehicles at a fixed shop |
| Retail POS / Invoicing | different object | a POS sale is composed and paid at one moment; a repair order is scheduled work with authorization gates, parts supply, and labor measurement before any payment |

The most important boundary is the pair with Appliance Repair Management (field-based repair) and Collision Repair Management (insurance-driven body work): all three are repair-business management, and they share the job → execution → billing spine. The durable differences are structural — where the work happens (shop vs field), what the object of record is (vehicle vs location-bound appliance), and who pays (consumer vs insurer).

## Representative Products

- **Tekmetric** — cloud-native; SMB through multi-location groups; inspection- and efficiency-driven with strong service-writer/technician workflow documentation
- **Shopmonkey** — cloud-native; SMB all-in-one; explicit estimate → repair order → invoice order model; serves auto repair, tire, quick lube, heavy duty, and detail shops
- **R.O. Writer** — legacy incumbent (decades old, now cloud); parts-catalog- and pricing-centric with deep supplier integrations and matrix pricing
- **Shop-Ware** — professional/mid-market; workflow- and analytics-driven; multi-shop (MSO) and capacity-management focus

Other major products serving this market (Mitchell 1 Manager SE, AutoLeap, MaxxTraxx, Shop Boss) could not be researched from official documentation in this environment; see Sources.

## Sources

Research date: **2026-09-06**

- Tekmetric Help Center (Tier 1): https://support.tekmetric.com/hc/en-us — articles "Repair Order Workflow Overview for Service Writers", "Repair Order Workflow for Technicians"; product pages: /feature/shop-management, /feature/digital-vehicle-inspection, /feature/inventory
- Shopmonkey Help Center (Tier 1): https://support.shopmonkey.io/hc/en-us — Features category; articles "Workflow Views", "Convert Estimates to Invoices"; product page: https://www.shopmonkey.io/
- R.O. Writer (Tier 2 product pages): https://www.rowriter.com/ and https://www.rowriter.com/features/
- Shop-Ware (Tier 2 product pages): https://shop-ware.com/

> Sourcing limitation: Mitchell 1 Manager SE (major legacy incumbent) was unreachable (site transport errors on 2026-09-06); one Tekmetric help-center article (Core Tracking) returned 403 and is evidenced only by its linked title. R.O. Writer and Shop-Ware documentation is product-page depth (marketing + feature descriptions), not operational help centers. Claims in this document are calibrated to the four researched products; market-wide statements are limited to structures observed across that sample, and vendor performance claims (approval rates, average repair order figures) are treated as marketing metrics, not structures. Precise numeric limits, plan-specific capabilities, and vendor-specific module names are intentionally omitted.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
