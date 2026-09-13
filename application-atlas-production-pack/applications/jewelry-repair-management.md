# Jewelry Repair Management

## Overview

A **Jewelry Repair Management** application is the shop-side system of record for repair work performed on customer-owned jewelry. When a customer hands over a ring, necklace, watch band, or heirloom piece to be fixed, the application captures that handover as an identified repair job — customer, item, condition, and requested work — then carries the job through the shop's repair process to a billed return of the piece.

The defining core is small:

```text
Customer brings in an item
  → repair job of record (customer × item × requested work, recorded at handover)
    → managed lifecycle (received → in progress → ready → completed)
      → return and settlement (item given back, job billed, history retained)
```

Everything else that modern products commonly carry — photos, estimates and approval states, deposits, labor and materials pricing, technician assignment, text notifications, barcoded tickets — is standard capability layered on that core, not what makes the category what it is. A pre-computer repair shop's handwritten repair envelope with a claim check satisfied the same three structures, and older or regional products fit the definition without any of the modern additions.

Repair management usually ships as a module inside a broader jewelry business system (point of sale, inventory, customers) rather than as an isolated product; that packaging is a variant, not the definition.

## Users & Context

The setting is a jewelry store with a repair counter, a dedicated repair shop, or a trade shop doing work for other stores.

Primary users:

- **Counter / sales staff** — take items in, record what was dropped off and what was requested, quote the estimate, notify customers when work is ready, and hand items back against payment.
- **Bench jeweler / technician** — performs the actual work (sizing, stone setting, soldering, polishing, replating); reads the job's description, notes, and photos before touching the piece.
- **Owner / shop manager** — watches the job board, sets prices and service offerings, manages statuses and templates, and keeps the repair history.

Secondary participants: sales representatives credited on jobs, and in some workflows an external repair shop or specialist that receives a copy of the ticket.

The work environment is a counter-and-bench business: intake happens face to face, the piece stays in the shop's custody (in a drawer, envelope, or bin) while work proceeds, and the customer returns to collect it. The application's job is to make that custody traceable and the work billable.

## Core Model

### The Repair Job of Record

The center of the system is the **repair job** (called a repair ticket or work order depending on the product). One job covers work on a single item and binds together:

- **the customer** — an existing customer record or one created at intake; the job is reachable later from the customer's record alongside their past jobs;
- **the item** — described in enough detail to identify and protect it: what it is, its metal and stones where relevant, its condition at drop-off, and any accessories received with it (box, band, extra links) so there is no dispute about what was handed over;
- **the requested work** — one or more service lines drawn from the shop's service catalog (labor-based services such as ring sizing or stone tightening) plus any materials or parts the work consumes, each line carrying its own notes where needed;
- **photos and documents** — images taken at intake and during the job, serving as condition evidence and as a visual brief for the bench;
- **dates** — when the item was received and when the shop promises completion;
- **status** — where the job stands in the shop's process.

A job typically covers work on a single item; several pieces dropped off together become several jobs, each tracked separately with its own details and status under the same customer record.

### The Lifecycle

The job's status is how the shop tracks where every piece is. Products differ in exact labels, but the conceptual progression is consistent:

```text
Received  →  In Process  →  Ready for Pickup  →  Completed
                ↑   ↑
     pending approval   waiting for parts
```

- **Received** — the estimate and ticket have been given to the customer and the item is officially in the shop's custody; no work has begun.
- **In Process** — work is underway. Some products give the two recurring interruptions their own states: work paused **pending customer approval** (something more is needed that adds to the price) and **waiting for parts** (ordered components not yet arrived); others track them in job notes.
- **Ready for Pickup** — the work is done; the customer is notified.
- **Completed** — payment has been taken and the item has been picked up; the job leaves the active list and becomes history.

Many products let the shop define additional sub-statuses (for example a quality-check step) that attach to one of the core phases, so the shop's own process vocabulary is preserved without breaking the underlying flow.

### Estimate, Pricing, and Settlement

Repair work is priced from the job's service and material lines. At intake the shop typically provides an **estimate**; if any line is quoted as estimated rather than fixed, the job total is treated as an estimate until the work is finalized. When work reveals additional needs, the job can be paused for **customer approval** before the price grows. **Deposits** can be collected up front in some products and are deducted from the balance at pickup. Final settlement happens when the customer collects the piece: the job's charges are loaded into the point-of-sale transaction, discounts applied, payment taken, and the receipt itemizes the work, any deposit already paid, and care notes for the item.

### History

Completed jobs do not disappear. They accumulate as the customer's repair history — and, by extension, the item's service record — retained for years. This history is both a service tool (what was done to this piece before?) and a business record (how much repair revenue does this customer generate?).

## How It Works

### Take in a repair

```text
Customer arrives with a piece
→ open or create the customer record
→ create the repair job: describe the item, log accessories, photograph it
→ add service lines (from the catalog or free-form) and materials
→ quote the estimate, set the promised date
→ print or send the ticket (customer copy; bench copy)
→ place the item in its envelope/bin; record the holding location
```

The intake step is deliberately fast — shops process many take-ins at busy times — so products standardize it: preset lists of common repair wording, reusable job templates bundling typical services and parts, and single-screen entry.

### Work the job

```text
Bench jeweler opens the job
→ reads description, notes, and photos
→ performs the work, adding parts/materials actually used
→ photographs the result if needed
→ updates the status (in process → ready)
```

If the work uncovers something the customer must approve — a cracked shank needing more work, a stone that must be replaced — the job moves to a pending-approval state and the shop contacts the customer before proceeding. If a part must be ordered, the job waits in a parts state.

### Notify and complete

```text
Job marked ready
→ the customer is notified the piece is ready (in many products the system
  sends the text/email when the status changes to ready)
→ customer arrives
→ load the job into the register/checkout
→ apply discounts, take payment (deposit deducted)
→ hand over the piece; job closes into history
```

Completion is the conjunction of two facts: the customer has paid and the item has left the shop. Only then does the job count as completed and leave the active queue.

### Core vs standard vs optional capabilities

**Defining core** — without these, it is not jewelry repair management:

- repair job of record binding customer, item, and requested work, captured at handover
- managed lifecycle with status the shop advances
- return-and-settlement closure: item returned, job billed, history retained

**Standard capabilities** — present in most mature products:

- item-level intake detail: description, condition, accessories, photos
- estimates and an approval loop for added work
- labor-based service catalog plus materials pricing
- technician/bench assignment
- customer notification at readiness (text/email)
- printed or emailed tickets for customer and bench; barcoded labels for item identification
- per-customer repair history over years
- deposits and POS-integrated payment at pickup

**Optional / variant** — depends on the business and product:

- custom work and special orders sharing the same job machinery
- trade-shop workflows (ticket copies for an external repair shop)
- multi-location and bin-location tracking, RFID item tracking
- customer portal visibility of job status
- appraisal documents, metal buying, layaways — adjacent modules of the wider jewelry suite

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Intake / job screen

The single most-used surface. Purpose: capture a take-in completely and fast. Typical information: customer, item description, accessories, photos, service and material lines with per-line notes, estimate flags, promised date, holding location. Primary actions: create job, add services/materials, attach photos, print or email the ticket, save.

### Job list / board

The shop's overview of everything in custody. Typical information: job ID, customer, item, status, promised date, technician, unread customer messages. Primary actions: filter by status/date/technician, open a job, bulk actions, export. This is the manager's answer to "where is every piece right now?"

### Job detail (working view)

The bench-facing surface for one job: full description, photos, notes, status control, and — where supported — a two-way message thread with the customer. Some products also separate staff-only internal comments from customer-visible notes that print on the receipt.

### Checkout / register completion

The payment surface. The job's charges load as line items; deposits already paid are itemized and deducted; the receipt prints with the work performed and care notes. In suite products this is the same register used for retail sales.

### Customer-facing surfaces

Notification messages (typically text) at readiness; in some products, the customer's website account shows the status of their open jobs.

### Settings

Service catalog and pricing, job templates, status vocabulary (including custom sub-statuses), technicians, locations, ticket/form printing.

## Important Rules / Behaviors

### Custody is documented at handover

The intake record is the shop's protection: what the item is, its condition, and what came with it are logged before work begins, and this documentation prints on the ticket. Disputes about scratches or missing accessories are answered from the intake record and photos.

### The estimate is not the final price until the work is done

Jobs can start from estimated lines; added work discovered mid-job is gated behind customer approval rather than silently billed. The final charge is settled at pickup.

### Completion requires both payment and pickup

A finished job that has not been paid and collected stays in the active queue. The completed state is the conjunction, not just the end of the work.

### Status names are the shop's own vocabulary

The conceptual progression (received → in process → ready → completed) is stable across products, but exact labels and the ability to add sub-statuses vary. Shops configure the vocabulary to match their process.

### History persists

Repair records are kept for years, per customer and per item. The job archive is a working record, not a transient queue.

### The item is a single identifiable physical object

Jobs reference one item each; multiple pieces mean multiple jobs, commonly taken in during a single visit. Barcodes or labels may be printed to keep similar-looking pieces from being confused.

## Variants

- **Store with an in-house bench** — repair management as a module of the store's POS/inventory suite; counter staff and bench share one system. The dominant packaging in the researched sample.
- **Dedicated repair shop** — repairs are the whole business; the same job machinery without heavy retail inventory. Served segment for at least one long-established product.
- **Trade shop** — performs repairs for other stores; ticket copies for the sending store and workflow around outbound/inbound pieces.
- **Repairs merged with custom work** — some products run custom fabrication and repairs on the same work-order machinery; others keep special orders as a separate module.
- **Regional / international suites** — the same pattern appears in jewelry business software across markets, alongside region-specific modules (gold buying, hallmarking-adjacent workflows, factory-side polish and plating).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Appliance Repair Management / Auto Repair Shop Management | sibling | same abstract job-shop shape (custody intake → lifecycle → billed return), different domain: household appliances or vehicles rather than individually valuable jewelry worked at a bench |
| Ticketing System / Help Desk | adjacent | routes service requests to an organization; no physical custody of a valuable item, no estimate-at-intake trade pricing, no pickup-and-return settlement |
| Retail POS | adjacent | centers on selling owned inventory; repair management centers on custody of the customer's item and the job lifecycle; payment machinery is shared in suite products |
| Appointment-based Service Business Management | adjacent | appointment-led scheduling vs custody-led job tracking; the unit of work is the job, not the appointment slot |
| Custom Order / Special Order Management | adjacent | producing a new piece vs restoring an existing customer item; products often share machinery, and some merge the two |
| Inventory Management | supporting | parts and materials (stones, findings) support the work; jobs reference them but are not inventory records |
| Field Service Management | distinct | work dispatched to customer sites; jewelry repair happens at the shop's own bench |

The most important boundary is with the other repair-shop verticals: the defining shape is shared, and what makes this a distinct Type is the jewelry domain — individually valuable customer items, trade-specific services and vocabulary, and bench-based custody workflows.

## Representative Products

- **Jewelry Shopkeeper** (Compulink) — long-established Windows suite for jewelers and repair shops; repair take-in with standardized repair wording, photos at take-in and during the job, customizable tickets for customer and repair shop, multi-year repair history, customer texting.
- **Jewel360** — modern cloud jewelry POS with repair and custom-work management built in: work orders with statuses, estimates, deposits, technician assignment, photos, two-way texting, register-completed payment, customer-visible status.
- **The Jewel Software** — international jewelry business suite (cloud or on-premise) listing repairs management among its retail modules alongside gold and diamond inventory, special orders, and production-side polish and plating management.

## Sources

Research date: **2026-09-08**

- Jewelry Shopkeeper — homepage (repair-tracking module description): https://www.jewelryshopkeeper.com/
- Jewel360 — product pages: https://jewel360.com/ , https://jewel360.com/custom-work-and-repairs
- Jewel360 Knowledge Base (operational documentation): https://knowledge.jewel360.com/article/work-orders , https://knowledge.jewel360.com/article/custom-work-order-statuses , https://knowledge.jewel360.com/modules
- The Jewel Software — homepage: https://thejewelsoftware.com/

> Sourcing limitation: several well-known vendors in this category (The Edge/Edge Retail, Affinity by Stuller, GemEasy, GemVision Liberty) could not be reached from the research environment, and general web search was unavailable. Claims in this document are calibrated accordingly: workflow and lifecycle detail rests primarily on the one product whose operational documentation was reachable, cross-product commonalities are stated only where at least two products' surfaces support them, and product-specific mechanics (exact status names, deposit timing rules, numeric limits) are not presented as industry standards. Standalone repair-shop-only products and trade-shop workflow details could not be verified and are described as variants without precise claims.
