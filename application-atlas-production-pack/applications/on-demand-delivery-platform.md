# On-demand Delivery Platform

## Overview

An **On-demand Delivery Platform** is the delivery-machinery application that fulfills individual delivery requests in near-real time: a business requests a delivery, the platform matches that request to available delivery capacity at request time, and the requester follows the delivery live until it closes with proof of delivery.

The defining core is small:

```text
On-demand delivery request (pickup → drop-off, items, timing, terms)
└── Real-time matching to available delivery capacity
    └── Requester-facing live delivery loop
        └── Delivery confirmation with proof
```

"On-demand" describes how fulfillment is arranged, not only how fast: each request is priced, matched, executed, and confirmed as its own unit of work, with immediate (ASAP) fulfillment as the dominant mode and scheduled windows riding the same machinery. The platform is defined by this request loop — not by owning drivers, not by selling to consumers, and not by route planning. The same machinery serves a platform-operated courier network, a crowdsourced driver base, a merchant's own fleet, or third-party delivery services reached through a gateway.

When the center of gravity shifts to planning and sequencing a day's delivery tasks over routes, the product is drifting toward a Last-mile Delivery Platform; when it shifts to aggregating many sellers on a consumer surface, toward a Food Delivery Marketplace; when it adds customer accounts, contracted rates, and billing for a delivery operator's own business, toward a Courier Management Platform.

## Users & Context

The primary user is a **business that needs goods delivered to its customers now or within hours** — a retailer offering same-day delivery from stores, a restaurant delivering its own orders, an industrial distributor rushing a part to a job site, a pharmacy delivering prescriptions, an e-commerce brand embedding delivery into its checkout.

Typical reasons to open the application:

- request a delivery for an order that is packed and ready (or schedule one for a chosen window)
- see which requests are unassigned, in progress, or completed, and who is carrying them
- follow a specific delivery's progress and share live tracking with the end customer
- handle exceptions: reassign a request, cancel, record a failed delivery, trigger a return or refund

Secondary users:

- **couriers/drivers** — receive offered or assigned requests on a mobile app, pick up, deliver, capture proof
- **end customers** — receive a tracking link and status notifications; they do not operate the platform
- **store/branch staff** — hand items to couriers, contact them through anonymized contact channels
- **administrators** — configure locations, vehicle classes, verification requirements, roles, and commercial terms

The work environment is split between an operations dashboard (web), integration surfaces (API, webhooks, e-commerce/POS/ERP connectors), and mobile apps for couriers.

## Core Model

### The Defining Core

**The on-demand delivery request.** The unit of record is a persistent, individually identified request for one goods movement. It carries:

- **pickup point** — the store, restaurant, warehouse, or branch the items leave from, with contact and readiness time
- **drop-off** — the recipient and destination address, with contact details and delivery instructions
- **items/manifest** — what is being carried: item names, quantities, sizes/weights, declared value
- **timing commitment** — either ASAP (fulfill as soon as possible) or a scheduled window (pickup-ready and drop-off deadlines); both are attributes of the same request
- **commercial terms** — the price quoted for this delivery, commonly tips, and per-delivery fees
- **verification requirements** — what proof must be collected at pickup and drop-off (signature, photo, barcode scan, PIN, ID check), chosen per business and per vertical
- **status** — a real-time lifecycle from request through courier assignment, pickup, transit, to delivered, failed, or canceled

**Real-time matching to available delivery capacity.** When a request arrives, the platform matches it to an available courier or driver drawn from a supply pool. The pool varies by product — the platform's own or managed courier network, a crowdsourced driver base, the business's own drivers, or third-party delivery services reached through an integration gateway — but the matching act is the same shape: per-request assignment at request time (an offer a courier accepts, an automatic assignment by proximity and availability, or an assignment to a named third-party service after an estimate), with reassignment when a courier cancels. No pre-built route plan is the organizing object; a request may be batched with others on one courier, but batching serves the request, not a route.

**The requester-facing live delivery loop.** The requesting business initiates the delivery through the platform — an API call, a dashboard form, a bulk upload, or an automatic feed from its e-commerce/POS system — and then follows it: status events as they happen, the assigned courier's identity and (in mature products) live location, an ETA, and finally the proof of delivery. The end customer commonly receives a tracking link and notifications under the business's brand. The platform is the delivery channel of record for the request: what it says about the delivery is what the business and its customer rely on.

### Capabilities Shared by Mature Products

These make the request loop practical; they are not what makes the product an on-demand delivery platform.

- **Per-delivery quote/estimate** — price computed before commitment from distance, speed/urgency, item size and weight, and vehicle class; quotes carry a validity period
- **Courier/driver app** — offered or assigned requests, accept/decline, status progression, navigation, proof capture
- **Live telemetry and ETAs** — courier location streaming, arrival-imminent signals, per-stop ETAs
- **End-customer tracking page** — a shareable, commonly brandable URL showing courier progress and ETA
- **Proof of delivery** — signature, photo, PIN, barcode scan, or recipient ID check, with the evidence stored and returned to the requester
- **Batching and multi-stop** — several requests consolidated on one courier with an ordered stop sequence
- **Failure machinery** — failed-delivery states, undeliverable actions (commonly an automatic return leg), refunds/claims, cancellation reasons attributed to customer, courier, business, or platform
- **Merchant configuration** — organizations, stores/locations, roles, vehicle classes, verification defaults, order cut-off times
- **Integration spine** — e-commerce/POS/ERP intake, webhooks for status and courier events, SDKs
- **Tips and courier economics** — customer tips routed to couriers, commonly with increase-only rules and guarantees
- **Reporting** — spend, delivery performance, driver activity, forecasts

### One Structure, Many Implementations

```text
Concept:   Supply pool behind the matching act
Forms:     platform-operated courier network · crowdsourced driver base
           · the business's own fleet · third-party services via a gateway

Concept:   Requester surface
Forms:     API-first white-label · operations dashboard · bulk upload
           · e-commerce/POS/ERP integration

Concept:   Timing commitment
Forms:     ASAP (minutes-to-hours expectation) · scheduled windows
           · urgent/hot-shot specialization
```

A reader who has only seen one form — say, an API that dispatches a courier network on checkout — should still recognize a restaurant's own-driver dispatch console as the same Type from the core model.

## How It Works

### Request a delivery

```text
Order is packed and ready (or a future window is chosen)
→ the business creates the request
  (API call, dashboard form, bulk upload, or automatic feed from its commerce system)
→ carrying pickup, drop-off/recipient, items, timing, verification requirements
→ the platform prices it (instant quote or estimate)
→ the business commits (or the checkout commits on the shopper's behalf)
```

Pricing is per delivery: distance and speed, item size and weight, vehicle class, and optional handling services are the common factors. Quotes commonly expire within minutes, so commitment follows estimation closely.

### Match the request to a courier

```text
Request enters the matching pool
→ a courier is offered the request and accepts (network pole)
  · or the system auto-assigns the nearest available driver (own-fleet pole)
  · or the platform assigns the request to a named third-party
    delivery service after an estimate (gateway pole)
→ the assigned courier's identity becomes visible to the requester
→ if a courier cancels, the request returns to the pool and is reassigned
```

Matching is the organizing act of the Type. It happens per request, at request time, against real-time availability — not against a route planned earlier in the day.

### Execute and follow live

```text
Courier moves to the pickup point
→ status events flow to the business (and the end customer's tracking page)
  · courier assigned · en route to pickup · pickup complete
  · en route to drop-off · arriving · delivered
→ the courier's live location and ETA are visible in mature products
→ the business can still edit limited fields
  (drop-off notes, contact details) up to defined stages
→ store staff and couriers contact each other through
  anonymized, PIN-protected channels
```

Status events are the requester's window into execution. Mature products push them as webhooks into the business's own systems as well as showing them on dashboards and tracking pages.

### Close with proof

```text
Courier completes the drop-off
→ proof is captured per the request's requirements
  (signature / photo / PIN / barcode scan / recipient ID check)
→ the request closes as delivered, with evidence attached
→ fees and tips settle on the per-delivery terms
```

Failures close differently: a delivery may be recorded as failed, an undeliverable action taken (commonly an automatic return leg that creates a new request back to the sender), and a refund or claim raised — with the cancellation or failure reason attributed.

### Scheduled requests ride the same loop

A scheduled delivery is the same request object with future pickup-ready and drop-off deadlines instead of an ASAP expectation. It is still quoted, matched near its execution time, tracked live, and closed with proof. What the business does not get from this Type is a worked availability structure — offered slot grids, capacity calendars — which is the scheduling Type's center.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Operations dashboard

The business's command surface.

- live list and map of requests by state (unassigned, assigned, in transit, delivered, failed)
- courier availability and locations
- primary actions: create a request, assign or reassign, cancel, inspect a request's detail and evidence

### API, webhooks, and integrations

The integration-first pole's primary surface, and every mature product's connective tissue.

- create/quote/cancel/update requests programmatically; bulk import
- webhook events for status changes and courier updates
- connectors into e-commerce platforms, POS systems, ERPs, and TMSs

### End-customer tracking page

A shareable page, commonly under the business's brand.

- courier progress, ETA, status history; delivery confirmation and proof where shared
- primary actions: watch, contact (through mediated channels)

### Courier/driver app

The execution surface.

- offered or assigned requests with pickup/drop-off details and instructions
- status progression controls, navigation hand-off, proof capture (signature/photo/scan)
- primary actions: accept, start, pick up, deliver, report a problem

### Store/branch handoff surface

Where items change hands.

- request readiness, courier identification, anonymized contact with PIN verification
- primary actions: confirm handoff, contact the courier

### Administration & configuration

- organizations, stores/locations, roles and permissions
- vehicle classes, verification defaults, cut-off times, commercial terms

## Important Rules / Behaviors

### The request is stage-gated

Once a courier is assigned and moving, most of the request freezes: pickup details and items are typically locked, while drop-off notes and contact details remain editable until near arrival. Tips, where present, commonly move one-way (increase-only). The lifecycle, not the dashboard, decides what may still change.

### Matching is perishable

Quotes expire within minutes; courier acceptance is competitive; a courier cancellation throws the request back into the pool and reassignment changes its batch identity. The requester's commitment and the courier's acceptance are separate events, and the space between them is where the platform actively works.

### Proof requirements are vertical-aware

Verification is configured per request and per business: age-restricted goods (alcohol, tobacco, prescriptions) commonly require recipient ID checks, and products may force an alternative outcome such as a return when the check fails; high-value or fraud-prone deliveries lean on signature or barcode scans; leave-at-door deliveries lean on photos. The platform enforces what the business configures.

### Failures have defined exits

A delivery that cannot be completed is not silently dropped: it is recorded as failed with a reason, an undeliverable action is taken (commonly an automatic return request back to the sender), and the commercial consequences (refunds, claims, credits) follow defined paths. Cancellation reasons are commonly attributed to the party that caused them.

### The platform is the channel of record

What the platform reports — status, courier identity, ETA, proof — is what the business tells its customer. This is why branded tracking pages and notification content matter commercially, and why the platform's status events, not the business's own guesswork, drive customer communication.

### Contact is platform-mediated

Contact between couriers, store staff, and (in some products) end customers commonly runs through mediated channels — masked phone numbers, PIN-protected call connect — rather than raw personal numbers. The platform shields both sides' direct contact details as a structural privacy behavior, not a feature.

## Variants

- **Network-seller pole** — the platform operates (or manages) a courier network and sells fulfilled delivery as a service, commonly white-label and API-first, so the business's customer sees only the business's brand. Mega-platform arms and crowdsourced driver networks both live here.
- **Own-fleet pole** — the platform is dispatch software for the business's own drivers: assignment, live tracking, proof, and customer communication over a fleet the business employs. No network is operated.
- **Gateway/aggregator pole** — the platform holds no drivers of its own but routes each request to third-party delivery services, comparing estimates and passing through fees with its own service charge.
- **Orchestration hybrid** — one platform combining on-demand network delivery with the business's own fleet management and route planning; the live straddle toward last-mile territory.
- **Vertical packaging** — food/restaurant (order-feed intake, cash-on-delivery, tips), industrial distribution (vehicle-class ladders, liftgates and handling equipment, job-site delivery), pharmacy and regulated goods (ID verification), big & bulky (two-person handling, equipment add-ons), airline baggage recovery.
- **Customer tier** — enterprise commercial models (master agreements, service-level commitments, delivery guarantees) down to self-serve SMB subscriptions.
- **Timing specialization** — ASAP-dominant general delivery vs urgent/hot-shot services vs scheduled-window-heavy programs.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Last-mile Delivery Platform | closest sibling; shared execution machinery. There, the operator's delivery work is organized as planned, sequenced, batched route execution over a day, and near-now work is one mode in the mix; here, each request is matched to capacity at request time and no route plan is the organizing object. Products straddling both self-label with both names. |
| Food Delivery Marketplace | the marketplace aggregates many sellers on a consumer surface, owns the consumer order, and generates demand; this Type is the delivery machinery behind any seller and generates no demand. The same vendor commonly sells both as separate products (its marketplace and its white-label delivery arm). |
| Courier Management Platform | the courier operator's business system of record: customer accounts, contracted rates, billing, driver pay. This Type is the request→match→track service loop itself; the courier dispatch desk is their shared historical ancestor. |
| Delivery Scheduling Platform | owns the when-structure: offered windows, availability rules, the schedule as the worked object. Here timing is a request attribute (ASAP or window) riding the matching machinery; there is no availability structure being worked. |
| Dispatch Management | the transversal assignment loop (work queue × roster × assignment) for any field work. This Type adds delivery semantics: goods requests, per-delivery pricing, requester-facing tracking, proof closure. |
| Delivery Experience Platform | communicates delivery state assembled from carrier/fulfillment feeds under the brand's identity, with no execution machinery. This Type executes the delivery it tracks. |
| Ride-hailing Platform | the same real-time request→match→track machinery applied to people instead of goods; ride products and delivery products are commonly separate offerings of the same operator. |
| Proof of Delivery Platform | POD-centric capture-first products; here proof is the closing step of the request lifecycle, not the product. |
| Parcel Management Platform | shipper-side multi-carrier shipping management (rate shopping, labels, manifesting) before carrier handoff; here the platform is the on-demand capacity or dispatches it per request. |
| Shipment Visibility Platform | watches and normalizes shipment state for freight the tenant does not execute; this Type executes or dispatches the delivery itself. |

The boundary with the Last-mile Delivery Platform is the most important one, because the two Types share their execution substrate. The structural difference is the organizing act: per-request real-time matching versus planned route orchestration. The boundary with the Food Delivery Marketplace is the most commercially visible one, because the largest marketplaces operate both halves as separate products — and their own documentation draws the seam between managing presence on a marketplace and dispatching a courier for one's own orders.

## Representative Products

- **Uber Direct** — the mega-platform's white-label delivery arm: API-first on-demand (ASAP) and scheduled delivery dispatched to the operator's own courier network, with dashboard, webhooks, and per-vertical verification
- **Roadie (a UPS company)** — crowdsourced same-day delivery network sold to businesses; 2-hour/4-hour/end-of-day options, hot-shot urgency, big-and-bulky capability
- **Dispatch** — enterprise delivery orchestration for industrial distribution: on-demand network delivery combined with own-fleet management, ERP/TMS integrations, and SLA-backed commercial models
- **Shipday** — SMB delivery-management SaaS (restaurant-centric): dispatches a business's own drivers or third-party delivery services through one gateway, with branded tracking and proof capture

These four were chosen to span the Type's supply models (platform network, crowdsourced network, own fleet + gateway), sales forms (API-first, dashboard-first), customer tiers (mega-platform, enterprise, SMB), and vertical flavors (general parcels, retail/industrial, food).

## Sources

Research date: **2026-09-09**

Primary official sources (directly fetched):

- Uber Direct developer documentation — Overview, FAQ, Delivery Window guide, Proof of Delivery guide, Delivery Status Webhook — https://developer.uber.com/docs/deliveries/overview (and linked pages)
- Roadie — homepage and Same-Day Delivery solution page — https://www.roadie.com/ , https://www.roadie.com/solutions/same-day
- Dispatch — homepage and On-Demand Delivery platform page — https://www.dispatchit.com/ , https://www.dispatchit.com/platform/on-demand-delivery
- Shipday — homepage and API documentation (Delivery Order Object, on-demand Assign endpoint) — https://www.shipday.com/ , https://docs.shipday.com/

> Sourcing limitations: DoorDash Drive (developer and marketing surfaces) and Burq were unreachable after repeated attempts and are not cited anywhere in this document; a regional (Southeast Asia) on-demand product was likewise unreachable, so regional breadth is under-observed. Roadie and Dispatch evidence is product-page level (their help centers were not fetched), so operational details for those two products are stated only at the depth their pages support. Precise numeric limits, cadences, and retention windows observed in vendor documentation are kept in the paired Research Notes rather than asserted as Type-wide facts.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
