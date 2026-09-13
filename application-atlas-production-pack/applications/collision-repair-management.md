# Collision Repair Management

## Overview

A **Collision Repair Management** system is the operator-side business system for a collision repair (auto body) shop. It manages accident-damaged vehicles as jobs: a line-item damage estimate defines the work, the estimate is authorized by the party who will pay for it, and an authorized repair order carries the vehicle through the shop's departments and stages while the system tracks parts procurement, technician labor, paint and materials, sublet work, customer communication, and final settlement across the repair's paying parties — the customer and, for most volume, an insurance company.

Its defining core is small:

```text
Damaged vehicle (identified object of work)
  └── Damage estimate (line-item: labor / parts / materials)
      └── Authorized repair order (job file carried through shop stages)
          └── Settlement across paying parties (customer / insurer)
```

Everything else commonly associated with this software — insurance-claim records, supplement handling, parts-ordering networks, production boards, technician flagging, customer status portals, accounting integration, cycle-time analytics — is standard capability that mature products add, not what makes the product a collision repair management system.

The type is distinct from general auto repair shop management: the work is defined by an accident-damage estimate rather than by customer-requested service, the paying-party structure is persistently split between customer and insurer, and the shop model is department-and-stage based (body, paint, frame) rather than bay-based.

## Users & Context

The system is operated by the body shop's staff, on behalf of a vehicle owner whose car was damaged in a collision — often in cooperation with that owner's insurance company.

Primary users:

- **Estimator / appraiser** — assesses damage, works with the estimate, photographs the vehicle, explains the repair to the customer, submits the estimate to the insurer when one is involved.
- **Service writer / front office** — checks vehicles in, captures damage and pre-existing condition, obtains customer authorizations, keeps the customer informed through the repair.
- **Production manager / shop foreman** — moves vehicles through stages and departments, schedules work against shop capacity, watches for parts shortages and bottlenecks.
- **Parts manager** — orders, receives, returns, and invoices parts; tracks missing parts against the production schedule.
- **Technicians (body techs, painters)** — perform the work, record time against operations, update vehicle location and status, document quality checks.
- **Bookkeeper / office manager / owner** — manages invoices, receivables (customer and insurer), accounting, and profitability reporting.

External parties interact with the system's outputs rather than operating it: the customer receives status updates, photos, documents, and payment requests; the insurance adjuster or appraisal network receives the estimate, supplements, and repair-status updates, and pays its share.

The work environment is a physical shop with departments (teardown/inspection, body, paint and refinish, reassembly, detailing) and specialized equipment; the software mirrors that floor plan as a sequence of stages the vehicle moves through. Because a typical repair spans days and depends on parts deliveries and insurer approvals, the system's center of gravity is tracking and coordination rather than a same-hour transaction.

## Core Model

### Vehicle and job file

The center of the system is the **repair order** — the job file for one damaged vehicle's repair. It holds the vehicle identification, the customer, the estimate and its revisions, the parts ordered, the labor performed, photographs and documents, internal notes and communications, and the money. One repair order can carry more than one insurance claim for the same vehicle (for example, damage from two separate incidents), and products differ on whether the claim or the vehicle is the container — conceptually, the repair order is the job, and claims attach to it.

### The damage estimate

The estimate is the artifact that defines the work. It is a line-item document: labor operations with hours (grouped by labor type — body, refinish, frame, mechanical), parts (OEM, aftermarket, recycled, or reconditioned), paint and materials, and sublet (work sent to outside vendors such as glass, upholstery, or towing). Estimates are authored in specialized **estimating systems** backed by vehicle data — OEM labor hours, parts catalogs and diagrams, repair procedures — and the management system consumes their output: importing an estimate is the dominant way a job enters the system. The estimate is not frozen: teardown frequently reveals damage that was not visible at appraisal, and estimates get revised (supplemented) during the repair. Mature products import estimate revisions, track price changes against the original, and reclassify estimate lines into the shop's own labor and parts categories.

### Authorization and paying parties

Who pays is a first-class structure. A repair may be entirely customer-pay, entirely insurance-pay, or split (a customer deductible on an insurer-paid repair; unrelated prior damage the customer covers themselves). The system records, per repair order, what each paying party is responsible for, collects authorizations before work proceeds, tracks payments received against amounts due, and manages receivables — including receivables owed by insurers, which settle on their own timelines. Authorization is not a single event: the initial estimate is authorized before the repair starts, and supplements typically require additional authorization from the insurer before the added work is performed.

### Production stages and departments

The shop is modeled as an ordered set of stages or departments that the vehicle moves through. Conceptual stages run from intake (opportunity or scheduled drop-off) through teardown/inspection, body work, refinish, reassembly, quality control, ready-for-delivery, and finally completion of delivery and billing. Exact stage names, counts, and order vary by product and shop — mature products make the stage set configurable — but the structure is stable: a production view shows every vehicle, its current stage or department, its holds and flags (waiting on parts, waiting on insurer approval), and its key dates. Vehicle location within the facility and department changes are tracked directly, and a department change can itself trigger customer or carrier status updates.

### Parts and procurement

Parts are managed as purchase orders bound to the repair order. A part progresses through a lifecycle — needed, ordered, received, invoiced — with rejection, return, and credit paths alongside. Expected delivery dates, missing parts, and back-ordered items are surfaced on the production view because parts availability gates the schedule. Orders are sent to dealers and vendors directly, or through parts-procurement services that quote OEM, aftermarket, recycled, and alternate-OE availability and price. Vendor invoices, credits, and returns reconcile against the purchase orders and flow into accounting.

### Labor, materials, and sublet cost

The repair order accumulates cost as the work happens: technician hours booked against operations (captured via time clocks or flagging, and compared with the hours the estimate allows), paint and materials charges, body supplies, and sublet invoices from outside vendors. Towing is commonly handled as a service cost line. This accumulated cost, compared against the estimate's authorized amounts, feeds job costing and profitability analysis.

### Settlement

The repair order resolves into invoices and payments: the insurer's payment (or direct payment arrangements), the customer's payment (including deductible and any customer-pay work), and reconciliation of what was authorized against what was actually billed. Closed repair orders feed sales records, receivables, and financial reporting.

## How It Works

The typical repair flows through the system as follows:

```text
Lead / assignment
  → damage estimate (authored in an estimating system)
  → estimate imported into the management system as a job
  → vehicle check-in (photos, condition, customer contact)
  → authorization obtained (customer and/or insurer)
  → scheduled for drop-off
  → teardown / inspection
      ↘ additional damage found → supplement → re-authorization → revised estimate
  → parts ordered against the estimate lines
  → vehicle moves through body / refinish / reassembly stages
      ↘ status updates flow to customer and insurer at stage changes
  → quality-control checks documented (with photos)
  → vehicle delivered
  → invoices issued and settled across paying parties
  → receivables closed
```

Several properties of this loop distinguish it from generic job-shop software:

- **The job begins as an estimate, not a request.** Intake tools capture leads (including online photo estimates submitted from the shop's website), but the binding artifact is the estimate, imported from the estimating system or recreated in the management system.
- **Work is gated by authorization.** The repair does not proceed — or does not proceed past teardown — without recorded approval from the party paying.
- **Supplements are a designed loop, not an exception.** Re-estimation after teardown, with re-authorization and estimate revision, is built into the workflow; the system tracks the revision history and the added amounts.
- **Parts availability is production-critical.** Scheduling and stage progression explicitly account for parts lead times; missing parts are visible against every affected job.
- **Status communication is continuous and outward-facing.** Stage changes, photos, and completion dates flow to the customer (text, email, portal) and to the insurer's systems without manual re-entry.
- **The loop closes in accounting.** Labor, parts, materials, and sublet costs accumulate on the job; invoices and payments settle it; the results feed accounting and profitability reporting by department and labor type.

## Interfaces

Surfaces observed across mature products (names and layouts vary):

- **Production board / vehicle center** — the shop's main screen. Purpose: see every job's stage, location, holds, missing parts, and key dates. Typical information: vehicle, customer, stage/department, flags, promised date, claim status. Primary actions: move stage, update location, add holds/flags, open the job file, filter and group views.
- **Repair order / job file** — the job's record. Purpose: hold everything about one repair. Typical information: vehicle and customer details, estimate lines and revisions, claim references, parts and their statuses, labor booked, documents and photos, notes, communications. Primary actions: import/create estimate, add supplement, record authorization, attach documents, print work orders and worksheets.
- **Estimate / supplement view** — the line-item work definition with labor types, parts, materials, sublet; supports revision tracking and price changes against the original.
- **Purchasing / parts assistant** — the parts desk. Purpose: order and track parts for all open jobs. Typical information: POs by vendor, part status (not ordered → ordered → received → invoiced), expected delivery dates, returns and credits, missing-parts view. Primary actions: create/send PO, receive, reject, return, request credit.
- **Scheduling** — capacity planning for drop-offs and work. Typical information: production capacity by day, jobs scheduled against it, parts lead times. Primary actions: schedule drop-off, balance load, manage delays.
- **Time clock / technician flagging** — technician-facing time capture against operations, feeding efficiency and payroll.
- **Quality control checklist** — department-level inspection points with photo documentation and recorded sign-off.
- **Customer communication surfaces** — SMS/email templates, appointment reminders, status updates with photos, a customer-facing repair-status portal, document e-signature, and online payment.
- **Reporting / analytics dashboard** — cycle time, throughput, labor efficiency, gross profit by parts/labor/materials, target-profit and receivables reporting; multi-site roll-ups for groups.
- **Accounting linkage** — sales and payables records passed to bookkeeping, whether through a built-in ledger or an interface to external accounting software.
- **Mobile app** — stage updates, photos, notes, and QC from the shop floor.

## Important Rules / Behaviors

- **Authorization precedes work.** Repair work — especially work beyond the initial estimate — is performed only after recorded approval from the responsible paying party. The estimate's authorized amounts define what the shop may bill.
- **The estimate is revisable, and revisions are tracked.** Supplements add lines and amounts after teardown; the original estimate, the supplement, and who approved each remain distinguishable on the job.
- **Stage and department changes are events.** They update the production view, can trigger automatic status messages to customers and carriers, and anchor the job's timeline.
- **Paying-party attribution is per line and per amount.** Customer-pay, insurer-pay, and deductible amounts are tracked separately on the same job, and receivables distinguish customer balances from insurer balances.
- **Parts state gates production.** A job waiting on parts is visible as such; scheduling accounts for parts lead times, and missing parts are surfaced against affected jobs rather than discovered on the floor.
- **Booked labor is compared against estimated labor.** Technician flagging and efficiency measurement exist because the estimate's hours anchor what the shop bills for each operation; the difference between booked and estimated hours is the shop's productivity picture.
- **Records are auditable.** Quality checks, authorizations, and communications are recorded with timestamps and user identity, supporting both insurer requirements and dispute resolution.
- **Customer-pay work fits the same model.** A self-pay repair runs the same estimate → authorize → repair → settle loop with the insurer simply absent; the claim machinery is common, not mandatory.

## Variants

Common shapes of this type:

- **Independent collision shops** — the general case; one or few locations, mixed customer-pay and insurer-pay work.
- **Insurer-program (DRP) shops** — shops that receive repair assignments from carrier programs; the intake increasingly arrives as a carrier-side assignment or a pre-written estimate, and carrier-facing status/payment reporting is heavier. (The dispatch and estimate-review machinery itself lives on the insurer's side.)
- **Dealership collision centers** — collision repair inside a dealership, with integration to the dealer's management system for vehicle, customer, and repair-order data, and OEM certification requirements.
- **Multi-site operators (MSOs)** — groups of shops run centrally; corporate-level production, performance, and accounting views across locations.
- **Estimating-suite bundles** — management sold together with an estimating product from the same vendor; the estimate is authored and consumed inside one suite.
- **Specialty scopes** — glass-focused shops, paintless dent repair, commercial-truck and specialty-vehicle collision work; regional deployments with different labor-rate and regulatory postures.
- **AI-assisted intake** — photo-based preliminary estimates and virtual appraisals feeding the same repair-order pipeline.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Auto Repair Shop Management | closest sibling | same generic repair-order pattern, but work is defined by internally-created service requests and inspections rather than an imported accident-damage estimate; customer/warranty payment rather than a persistent customer-vs-insurer split; bay-based rather than department/stage-based; no supplement loop or estimating-system dependency. Vendors ship separate products for the two markets. |
| Insurance Claims Management | opposite side of the seam | the insurer-side system adjudicates and settles the claim; the collision system executes the repair and reports into the claim. Claim records here are attachments to repair orders, not adjudication records. |
| Collision estimating systems (product family) | tightly coupled upstream | estimate authoring against OEM labor-hours and parts databases is a distinct instrument; management systems import its output, track revisions, and check compliance. Bundled by some vendors, separate by others. |
| Car Wash / Detailing Management | sibling service business | appearance services with package pricing; no damage estimate, authorization chain, or claim machinery. |
| Fleet Management System | different population | manages an organization's own in-service vehicles; collision management runs a service business on customers' vehicles. Fleet owners appear only as customers. |
| Towing Dispatch / Roadside Assistance | upstream service | towing appears here as a sublet or service cost line; dispatching tow trucks is a different type. |
| Appointment Scheduling Application | module slice | scheduling is one capability inside the shop operation, not the type. |

The sharpest boundary is with Auto Repair Shop Management. The structural test: remove the accident-damage estimate as the job-defining artifact, the paying-party split, and the department/stage production model, and the remaining software is general auto repair shop management; add them, and it is no longer generic. They share a repair-business pattern, not a definition.

## Representative Products

- **CCC ONE** (CCC Intelligent Solutions) — market-leading estimating and management suite for collision repair (referenced as a market anchor; primary documentation was not reachable during research)
- **Mitchell Cloud Repair / Mitchell RepairCenter** (Mitchell, an Enlyte company) — cloud and established management suites from an estimating-data incumbent
- **Solera AutoFocus / Audatex Qapter** (Solera) — shop management and estimating inside a claims-ecosystem vendor
- **Nexsyis Collision** — independent all-in-one body shop management with integrated accounting

## Sources

Research date: **2026-09-07**

Official vendor product documentation (Tier 2 product pages; no help-center articles were reachable for any sampled product):

- Nexsyis Collision — product pages (Repair Management, Production Tracking, Purchasing, CRM): https://www.nexsyiscollision.com/
- Mitchell (Enlyte) — Collision Repairers, Mitchell Cloud Repair, Mitchell RepairCenter, Mitchell Cloud Estimating, Loss Profiling & Dispatch: https://www.mitchell.com/
- Solera — Claims & Collision product pages (AutoFocus Shop Management, Qapter, AutoWatch, APU): https://www.claims.solera.com/
- Enlyte — corporate overview (Mitchell APD / PartsTrader structure): https://www.enlyte.com/

> Sourcing limitation: cccis.com (market-leading vendor) returned access errors on every attempt and is cited only as a market anchor, not as evidence. No Tier-1 help-center or training documentation was reachable for any sampled product in this pass; all workflow descriptions above are drawn from official product pages, and no numeric limits, default settings, or exact status/permission semantics are asserted. Detailed observations, the cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
