# Last-mile Delivery Platform

## Overview

A **Last-mile Delivery Platform** is the orchestration system for the final leg of goods delivery — the stretch from the point where a business hands its goods over to transport (a store, warehouse, kitchen, pharmacy counter, or regional hub) to the end recipient's door. The platform holds every final-leg delivery as a managed record, organizes that pool of work into routes and assignments across the delivery capacity available to the business — its own drivers, contracted drivers, or integrated third-party delivery networks — and drives each delivery through field execution to a captured delivery confirmation.

The defining core is deliberately small, three structures that have to be present together:

```text
Order flow (commerce systems)
  ↓ intake
Delivery task (recipient/destination + timing + status)
  ↓ orchestration (route / assign / dispatch)
Delivery capacity (own drivers · contracted · third-party networks)
  ↓ field execution
Delivery confirmation (signature / photo / timestamp)
  ↓
Recipient layer (notifications · live tracking · ETA)
```

Everything else commonly associated with the category — route optimization, branded tracking pages, on-demand delivery networks, courier/3PL billing machinery, AI assistance — is a capability layer that mature products frequently carry, not what makes the product this Type. A business running its own final-leg delivery with nothing but a task list, a dispatcher, and driver phones still fits the Type; a product that only shows delivery status without orchestrating execution does not.

## Users & Context

The primary users are the people responsible for completing a business's own final-leg deliveries:

- **Dispatcher / delivery manager** — works from the orchestration console: watches the incoming delivery queue and the live map, builds and adjusts routes, assigns or reassigns work to drivers, intervenes in exceptions, and answers delivery questions using the same records customers see.
- **Driver** — executes the work from a mobile app: receives the assigned task list, navigates stop to stop, updates status on arrival and completion, scans items where required, and captures proof of delivery.
- **Recipient (end customer)** — not an operator but a first-class participant: receives delivery notifications and follows a live tracking page with the estimated arrival.
- **Administrator / operations manager** — configures teams, areas, and integrations, manages the driver roster, and reads delivery performance reports.

The tenant is whoever is responsible for the final leg: retailers and e-commerce operators, restaurants and food brands, grocery, florists, liquor stores, distributors and wholesalers, parts suppliers, pharmacies, and also courier and 3PL delivery companies. This tenant breadth is a structural feature of the Type: the same execution machinery serves a business delivering its own goods and a delivery company fulfilling client work, and the platform's core does not change between them. The work environment is dominated by a web console for dispatch and a mobile app for the field, with recipients reached on their own phones.

## Core Model

### The delivery task — the unit of record

The system's world is organized around the **delivery task**: one final-leg movement of goods to an end destination, held as a persistent record from creation to closure. A task carries:

- **Destination and recipient** — a validated street address (or explicit coordinates), plus the recipient's name and contact details. The recipient is the person the delivery-layer communications bind to; a task can exist without a recipient, in which case the recipient-facing layer is suppressed for it.
- **Items and instructions** — what is being delivered (quantities, reference numbers, barcodes where used) and handling notes, including notes that persist on the recipient rather than the single task.
- **Timing commitments** — an expected time or a completion window (deliver after / before a given time), set by the business or inherited from the order; the platform measures live progress against it.
- **Status** — a lifecycle that advances through execution: created (unassigned) → assigned to a driver → in transit → delivered or failed. Statuses are attributed and time-stamped, producing the delivery's event history.
- **Paired legs** — deliveries are commonly accompanied by pickup tasks (collecting goods, returning items), held in the same task model.

### Delivery capacity — the executing side

The second pole is the **capacity** the platform orchestrates: the driver roster (employees or contractors), each with an identity, contact channel, shift/availability state, and — during work — a live position and a current task sequence. Where the tenant blends capacity, integrated third-party delivery networks appear as additional, interchangeable executors of the same task records.

### The execution plan — routes and assignments

Between the task pool and the capacity sits the **plan**: stops sequenced into routes (per driver, per shift) under the business's constraints — time windows, priorities, quantities, service times, areas. Planning may be performed by an optimization engine, by the dispatcher by hand, or both; the plan is continuously revisable, and the gap between plan and reality (delays, new tasks) is what the dispatcher manages.

### The execution record and its confirmation

Each delivery accumulates an **execution record**: who was assigned, when work started, when the driver arrived, when the delivery was completed, and — crucially — the field-captured **proof of delivery** (signature, photos, geolocation, timestamp) that closes the task. This record is simultaneously the operational source of truth, the customer's visibility feed, and the business's dispute evidence.

### The recipient layer

Delivery progress is surfaced to the recipient: automatic notifications across messaging channels, a live tracking view of the driver's approach, and an ETA derived from actual execution. The layer is bound to the task's recipient record — it exists because the record advances, not as a separate communication product.

```text
Delivery task
  ├── recipient / destination / items / timing commitments
  ├── status: unassigned → assigned → in transit → delivered / failed
  ├── assigned to → driver (own / contracted) or third-party network
  ├── sequenced into → route / plan (constraints: windows, priority, capacity)
  ├── closes with → proof of delivery (signature / photo / time / location)
  └── surfaces to → recipient (notifications, tracking, ETA)
```

## How It Works

The core operational loop runs once per delivery day, per location:

**1. Intake.** Deliveries enter the platform from the tenant's own order systems — e-commerce platforms, point-of-sale, ERP, marketplaces — through integrations, APIs, or scheduled imports, or are created by hand at the dispatch console. The order reference stays on the record, connecting the delivery to the sale that produced it.

**2. Orchestration.** The dispatcher reviews the unassigned queue on a map-plus-list console. Routes are built from the task pool — by an optimization engine where the product offers one, or manually — and tasks are assigned to drivers individually or in batches. Many products offer automatic assignment by proximity, capacity, or rules. Assignment is a managed, reversible act: work can be unassigned and resequenced at any point before completion.

**3. Dispatch, including to third-party networks.** Work is dispatched to the tenant's own or contracted drivers. Where a platform integrates delivery networks, the same task can be dispatched outward instead — commonly with a per-delivery comparison of providers' prices and delivery times, and with rules that automate the choice. Status updates from third-party providers flow back into the same record, so mixed own-and-outsourced fleets remain one operational picture.

**4. Field execution.** The driver works from the mobile app: the assigned task list in sequence, navigation to each stop, arrival and completion actions, barcode scans where the workflow uses them. Completing a delivery captures proof — signature, photos, timestamp, location — directly from the field.

**5. Recipient communication.** Execution events drive the recipient layer automatically: confirmation and tracking messages go out, the live tracking page follows the driver, and the ETA updates as reality diverges from plan. Delayed deliveries are flagged internally while customers are kept informed.

**6. Closure and exceptions.** A delivery closes as succeeded or failed, with the captured evidence attached. Reality intrudes in known ways, and the products build for it: a driver who cannot complete in the app (device dead, order canceled mid-run), a completion status that turns out to be wrong, a recipient who is unavailable. Mature products give the dispatcher explicit override machinery — force-completing work with notes, correcting a recorded outcome after the fact, returning work to the queue or converting it to a pickup/return task. Failed deliveries, cancellations, and reassignments are first-class operations, not side effects.

**7. Oversight.** Managers read the day through dashboards and reports: on-time performance, delivery success rates, driver activity, delay patterns, and — where networks are used — provider performance and cost.

## Interfaces

**Dispatch console (map + queue).** The dispatcher's working surface. A live map showing drivers and delivery pins colored by status, alongside a sidebar or table of tasks grouped by state and by driver; filters and search across the day's work; task detail with history, evidence, and actions (assign, reassign, reorder, force-complete, correct status). This is where the work×capacity×progress picture is maintained.

**Driver mobile app.** The field surface. Assigned tasks in sequence, navigation, status actions per stop, item scanning where used, proof-of-delivery capture, and a channel back to the dispatcher. Designed for one-handed, in-transit use.

**Recipient tracking view.** A page (link delivered by message channel) showing the delivery's state, the driver's live position on approach, and the ETA; commonly brandable to the business. Notification messages accompany the milestones.

**Reports and dashboards.** Management surface over the accumulated records: delivery volumes, on-time and success rates, driver performance, delay analytics; provider analytics where third-party networks are used.

**Administration and integrations.** Setup surfaces for the driver roster, teams and areas, task templates, notification settings, and the connection points to the tenant's commerce systems; API and webhooks for order intake and status distribution are a first-class surface in most products.

## Important Rules / Behaviors

**Status is attributed, time-stamped, and overridable.** Field events drive the lifecycle, but the dispatcher holds governance: an in-transit task can be force-completed with notes when the driver cannot act, and a completion status can be edited after the fact with the change recorded. The system trusts the field but does not depend on it.

**Timing commitments are measured, not decorative.** When a task carries a completion window, the platform compares projected arrival against the commitment and surfaces at-risk or delayed work to the dispatcher — the same data that drives customer ETA messages. A delivery whose window has passed is still delivered, but the miss is visible everywhere it matters.

**Addresses are structured.** Destination entry is validated (street-level geocoding, with coordinate entry as the fallback), because the downstream machinery — routing, navigation, ETAs — depends on geocodable destinations.

**The recipient binding controls the communications layer.** Recipient notifications can only go out when the task carries the recipient's contact details; products commonly allow a task to proceed without any recipient, in which case the recipient-facing layer is suppressed for that delivery. The recipient layer is a consequence of the record, which keeps customer communication consistent with operational reality.

**Assignment is reversible until execution closes it.** Work can be unassigned, moved between drivers, and resequenced throughout the day; the third-party option extends the same reversibility to outsourced capacity. Only a closed completion (or a dispatcher's recorded override) fixes the outcome.

**Proof of delivery is the closing evidence.** Signature, photo, timestamp, and location are captured at the point of completion and retained against the record — the basis for dispute resolution and for the recipient-facing delivery confirmation.

**Mixed fleets produce one picture.** When work is dispatched to third-party networks, provider status updates land in the same task record as driver updates; operational and customer-facing views do not fork.

## Variants

- **By tenant**: businesses delivering their own goods (retail, food, grocery, pharmacy, distribution) versus delivery operators (couriers, 3PLs) running client work on the same substrate. Courier/3PL business machinery — client accounts and portals, rate tables, delivery billing, contractor commissions — appears in some products as an optional suite rather than the core.
- **By work mix**: routed, planned rounds (distribution-style, day-planned) versus near-now on-demand work (restaurant and same-day flows) versus a blend; the same task model carries both.
- **By capacity model**: own-fleet only; own fleet plus third-party networks with per-delivery price/time comparison and automated network dispatch; third-party-led operation.
- **By packaging**: standalone delivery platforms versus suites that add returns automation, telematics, or courier-client modules; API-first platforms (the API as the primary surface) versus UI-first self-serve tools.
- **By vertical emphasis**: food operations (pickup–delivery pairing, order contents and fees on the record), B2B distribution (route-heavy, business recipients, multi-stop days), regulated goods (evidence-heavy confirmations).
- **By scale and posture**: self-serve SMB products priced per driver, up to multi-location and enterprise deployments with role-based access and contracted integrations.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Courier Management Platform | The closest sibling. A courier management platform is the delivery *company's business system*: courier orders belonging to external client accounts, every order priced against contracted rates, completed work becoming billed revenue. Remove that business frame and the same execution machinery remains — a last-mile delivery platform. Courier machinery reappears here only as optional suites; conversely, a courier company can run this Type's machinery as its operations tool while its business frame lives elsewhere. |
| Dispatch Management | The transversal assignment machinery (work queue × resource roster × assignment act × live picture) that this Type embeds. Generic dispatch serves any field workforce — service jobs, freight, deliveries — without delivery-specific semantics (delivery windows, proof of delivery, recipient layer, delivery networks). Remove the delivery semantics and orchestration scope, and only the dispatch machinery remains. |
| Delivery Scheduling Platform | Owns the *when-structure* of delivery: offered times, windows and slots, admission rules, the schedule as the worked object. Here, timing commitments are attributes of tasks and schedule surfaces are secondary. Remove execution orchestration and the scheduling product remains a scheduler; remove the when-structure center and a scheduling product becomes this Type. |
| Delivery Experience Platform | Owns the consumer-facing post-purchase presentation and communication of delivery — and holds no execution machinery. This Type produces the delivery state that the experience layer would present. Remove execution orchestration and only the experience layer remains; the experience layer never gains execution by adding surfaces. |
| Route Optimization Platform | Centers on the optimization engine and its solves. Here, optimization is a common capability — some products gate it behind higher tiers, and manual dispatch remains fully workable without it. |
| Proof of Delivery Platform | Centers on capture and management of delivery confirmation itself. Here, proof of delivery is the closing step of the delivery lifecycle, not the product's whole object. |
| On-demand Delivery Platform | A consumer-facing instant-delivery marketplace with its own demand generation. Near-now work exists inside this Type as a work-mix mode, but no sampled last-mile platform generates consumer demand or mediates a consumer marketplace. |
| Shipment Visibility Platform | Aggregates and normalizes delivery state for freight the tenant does *not* execute, across carrier networks. This Type executes the final leg over its own or blended capacity. |
| Parcel Management Platform | Shipper-side multi-carrier shipping execution (rate shopping, labels, manifesting) before handoff to carriers. This Type orchestrates final-leg completion after that decision, typically for goods the tenant delivers itself or via local networks. |
| Food Delivery Marketplace | A consumer marketplace mediating restaurants and diners. Products of this Type serve as a food business's own delivery operations layer behind any storefront, without consumer demand generation. |
| Transportation Management System | Runs the freight business: loads, carriers, tendering, audit and payment. The unit of work here is the final-leg delivery to an end recipient, and the freight business frame is absent. |
| Fleet Management System | Owns vehicles and telematics (maintenance, fuel, compliance) as the system of record. Here vehicles are executing resources; the delivery task is the record. |

## Representative Products

- **Onfleet** — API-first last-mile platform built around a task model with dispatcher, driver, and developer surfaces; ships an optional courier/client suite
- **Shipday** — self-serve delivery operations layer for restaurants and local delivery businesses, blending own drivers with third-party delivery services
- **Elite EXTRA** — last-mile software suite for distributors and delivery operations, combining routing and dispatch with an integrated third-party delivery network
- **Detrack** — POD- and tracking-first delivery management for couriers, 3PLs, and businesses making their own deliveries, global SMB footprint

## Sources

Research date: **2026-09-08**

- Onfleet — Support Center: dispatcher documentation (task creation, task status, task management, routing and route optimization, driver management, task import); Courier and Courier Client category. https://support.onfleet.com/hc/en-us
- Shipday — Product site (features, use cases, integrations, FAQs) and API documentation (Delivery Order Object, API reference). https://www.shipday.com/ , https://docs.shipday.com/
- Elite EXTRA — Product site: suite overview, Routing & Dispatch, Delivery Network. https://eliteextra.com/
- Detrack — Product site: overview, features, industries, integrations, pricing. https://www.detrack.com/

> Sourcing limitations: the Onfleet and Bringg marketing sites were unreachable (HTTP 403; Bringg also unreachable in earlier sibling research), and one additional candidate product was dropped after repeated fetch failures. Evidence for Onfleet was drawn from its reachable support-center documentation; the enterprise delivery-orchestration pole of the market (delivery-window promises at scale) could not be directly verified and is characterized only at the level the sampled products document. Precise operational details (exact status vocabularies, numeric limits, plan-level feature gating beyond what is quoted) are intentionally not stated; product-by-product observations are recorded in the paired Research Notes.
