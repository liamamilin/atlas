# Shipment Visibility Platform

## Overview

A **Shipment Visibility Platform** is an operational system that lets a shipper or logistics service provider watch freight that other parties are carrying. It holds each in-transit movement as a persistent shipment record, assembles a live picture of that movement — location, milestones, status, predicted arrival — from data supplied by the parties executing the transport (carrier systems, telematics feeds, driver apps, tracking devices), and turns deviations from plan into alerts that a team can triage, resolve, and share onward.

It solves a problem every supply-chain organization has: once freight leaves the dock, the organization that owns the goods neither drives the truck nor sails the ship. Without this kind of system, its teams learn shipment status by making check calls, reading individual carrier portals, and chasing emails — one shipment at a time. The platform replaces that with one normalized picture of every shipment, across carriers and transport modes, watched continuously against plan.

Its boundary is the absence of execution: the platform watches, normalizes, and distributes transport information; it does not rate, tender, book, dispatch, or purchase the carriage itself. When a product's center of gravity shifts to committing carriage, to the cargo's environmental condition, to the vehicle rather than the consignment, or to the consumer's post-purchase tracking page, it has become a different kind of application.

## Users & Context

The tenant is typically the party that owns or orchestrates the freight rather than the party that moves it.

**Primary users:**

- **Shipper logistics and supply-chain teams** — monitor inbound and outbound freight across sites and modes against plan; this is the core "control tower" audience. They watch the map and exception queues, and act when shipments drift from schedule.
- **3PL / logistics service provider operations** — run the same watch loop on behalf of customers, with visibility over the freight they orchestrate and the performance of the carriers they use.
- **Customer service and order-management teams** — answer "where is my order" questions from live shipment status instead of phone calls, and proactively warn downstream customers of delays.

**Contributing users (data providers, not watchers):**

- **Carriers** — connect their systems so their freight's status flows into their customers' picture; they are on-boarded, governed, and (in mature deployments) scored.
- **Drivers** — in some deployments supply location and milestone confirmations through a mobile app.

**Downstream consumers:**

- **Receivers and site teams** (plants, warehouses, stores) — plan docks, labor, and shelves around predicted arrivals.
- **Enterprise systems** (ERP, order management, planning) — consume the live shipment picture through integrations rather than people.

The work context is continuous monitoring: a logistics team starts the day with an exception queue, keeps a map of in-transit freight on the wall, and reacts to alerts as they arrive. It is a standing operational loop, not a transactional workflow.

## Core Model

The application's world is built around three structures. Everything else it does grows out of them.

### The shipment of record

The unit of record is **the shipment** — one identified freight movement being carried by transport parties. A shipment record persists: it is created (by a user, an API, or an upstream system) before or as the movement begins, and it accumulates everything that happens to that movement. It carries:

- **Identity and references** — a shipment identifier, plus mode-specific transport references that anchor it to the outside world (a container number, an air waybill, a carrier's shipment reference).
- **Route** — origin, destination, and where the journey has legs, an ordered set of legs, each with its own mode, carrier, and endpoints.
- **Plan** — scheduled departure and arrival, expected milestones.
- **Parties** — the carrier(s) on each leg; often the shipper and receiver locations.
- **Accumulated history** — every location update, milestone event, status change, and alert the shipment generates, retained after completion for audit and analysis.

The shipment is cargo-agnostic: the same record shape covers a truckload of retail goods, an ocean container of components, an air consignment of pharmaceuticals. It is also consignment-anchored, not order-anchored: an order or purchase order may be *linked* to shipments as an upstream reference, but the thing being watched is the movement, not the commercial commitment.

### Sourced signals, normalized

The platform's picture of a shipment is **assembled from data sources the platform itself does not execute**. This is the defining property of the type: the platform is a consumer and normalizer of transport signals, not a transport executor. Conceptually there is one idea — the executing parties' own systems report what is happening — realized through several mechanisms:

```text
Concept:      Transport-party-sourced tracking signals
Realizations: carrier systems via API / EDI integrations
              carrier telematics feeds
              carrier TMS integrations
              driver mobile apps
              dedicated tracking devices placed with the freight
              mode-specific references (container ID, air waybill) queried
              against carrier / vessel / airline data
```

Whatever the source, the platform's job is the same: fold heterogeneous carrier data into one **normalized picture per shipment** — a common milestone model (for example: picked up, departed, arrived, delivered), a live location, a status, and a **predicted arrival time** that is re-estimated as new signals arrive. Normalization across carriers and modes is what makes the map meaningful: without it, the user is back to a folder of per-carrier tracking pages, each speaking its own dialect.

Because the picture is only as good as its sources, data quality is itself a managed property of the system: which carriers are connected, whether a shipment is fully tracked from loading to delivery or only partially covered, whether a feed has gone stale.

### The watch-and-act loop

The platform continuously compares each shipment's live progress against its plan and surfaces deviations — a slipping ETA, a milestone that has not arrived, a stop that is running long, a route that leaves the expected path — as **alerts and exceptions**. These are managed work items, not passive log entries: they have states (new, being worked, resolved), they can carry comments and assignments, and they drive the daily operational loop — triage the queue, contact the responsible party, update downstream stakeholders, close the exception. When the shipment reaches its destination the record completes and locks into history, where it feeds carrier and lane performance analysis.

### One structure, many implementations

```text
Concept:                  Shipment of record
Implementations:          created by users in the platform, pushed in via API,
                          or imported from connected systems

Concept:                  Transport-party-sourced signals
Implementations:          carrier API/EDI networks (the multi-carrier network pole),
                          carrier telematics integrations, driver apps,
                          shipper-deployed tracking devices (the hardware pole),
                          mode-specific transport references

Concept:                  Predicted arrival
Implementations:          carrier-provided ETAs, platform-computed statistical
                          or machine-learning ETAs, or a blend
```

A reader who has only seen one implementation — say, a carrier-network product with no hardware — should still be able to recognize the hardware-first product as the same type: both hold shipments as records and normalize externally sourced signals onto them.

## How It Works

The standing operational cycle of a shipment visibility deployment looks like this:

### 1. Connect the network

Before any shipment can be watched, the transport parties must be connected: carriers on-boarded onto the platform, their systems linked (API, EDI, telematics, or driver app), tracking devices registered where they are used, and the organization's own systems (TMS, ERP, order management) wired in so shipments flow in and visibility flows out. Mature products treat this as a first-class, ongoing operation — connection health and data completeness are monitored, because a visibility platform with silent feed gaps produces confident wrong answers.

### 2. Shipments enter the record

A shipment enters the platform when the movement is planned or begins — created by hand, pushed in from an upstream system, or registered by referencing its transport identifiers. It is configured with its route and legs, scheduled timing, carrier(s), and the alert rules that should apply to it. From that moment it occupies one of the standing states of the record: **upcoming** (planned, not yet moving), **in transit** (live, receiving signals), or **completed** (arrived, locked into history).

### 3. Signals flow and are normalized

While the shipment moves, the attached sources stream data: location pings, milestone events, carrier status updates, device readings. The platform normalizes each into the shipment's common picture — updating location, advancing milestones, re-computing the predicted arrival — so that a road leg on one carrier and an ocean leg on another read as one continuous journey with one timeline.

### 4. Watch, detect, resolve

Users watch through the map and list; the platform watches continuously. When reality diverges from plan, an alert is raised on the shipment. The operational loop:

```text
alert raised
→ triage (see it in the exception queue / color-coded on map and list)
→ investigate (shipment detail: timeline, location history, sensor or
  event data, contact and reference information)
→ act (contact carrier or driver, update downstream stakeholders,
  adjust receiving plans)
→ resolve (mark the alert worked/resolved, with notes; auto-resolution
  when readings or timing return to normal)
```

### 5. Share the picture

Visibility that stays in the platform is only half the value. Live status is distributed outward: shared views or portals that give a customer or receiver access to a shipment's progress, notifications pushed to stakeholders when milestones or exceptions occur, and APIs that feed the same normalized data into the organization's ERP, order management, and planning systems. The platform becomes the single agreed answer to "where is it?" for everyone in the chain.

### 6. Complete and learn

At arrival the shipment completes — typically derived from the shipment reaching its destination (for example, entering the destination's configured area) rather than from a human marking it done — and its record locks as a permanent history. Completed shipments accumulate into analysis: on-time performance by carrier, reliability by lane, recurring exception patterns. That analysis loops back into carrier selection, routing, and the next planning cycle.

## Interfaces

The surfaces below are described in conceptual terms; exact layouts and names vary by product.

### Live map

The signature surface.

- **Purpose:** see the whole in-transit population at a glance, geographically.
- **Typical information:** shipments as moving markers or clustered pins, colored by exception status; traffic, routes, and site locations as context.
- **Primary actions:** drill into a shipment or a cluster, filter the population, spot the red entries.

### Shipment list / exception queue

The operational desk.

- **Purpose:** monitor and prioritize shipments, especially those needing attention.
- **Typical information:** shipment identity, route, carrier, current status, predicted arrival, exception/alert state per shipment; powerful search on any reference; saved views.
- **Primary actions:** filter (by route, mode, alert type, arrival timing, on-time status), sort, open a shipment, work its alerts.

### Shipment detail

The single-movement workspace.

- **Purpose:** understand and manage one shipment end to end.
- **Typical information:** milestone timeline (planned vs actual), live location and track, predicted arrival, legs with carriers, attached references, device or sensor readings where present, event/alert history, documents such as delivery confirmation where collected.
- **Primary actions:** edit limited details while upcoming/in transit, update alert status, add comments and assignments, share or generate a report.

### Alert / exception workbench

The resolution surface.

- **Purpose:** turn deviations into managed work.
- **Typical information:** each alert's type, trigger point, shipment context, and resolution state.
- **Primary actions:** take ownership, annotate, assign next steps, mark in-progress/resolved.

### Network & data-quality console

The supply-side surface that makes everything else trustworthy.

- **Purpose:** onboard and govern the carriers, connections, and devices feeding the platform.
- **Typical information:** connected carriers and their integration status, tracking coverage and completeness per carrier, feed freshness.
- **Primary actions:** invite/on-board a carrier, configure an integration, investigate data gaps.

### Sharing & communication

- **Purpose:** push the picture outward to people who do not hold seats.
- **Typical information:** shared shipment views/portals; notification templates and channels (email, SMS, messaging apps).
- **Primary actions:** share a shipment with a collaborator or recipient, configure milestone/exception notifications, publish a branded tracking view.

### Analytics

- **Purpose:** learn from the completed-shipment history.
- **Typical information:** on-time performance by carrier and lane, exception patterns, dwell and transit-time trends.
- **Primary actions:** compare carriers, drill into a lane, export for business reviews.

## Important Rules / Behaviors

### The platform watches but does not execute

Nothing in the core commits carriage. Rating, tendering, booking, dispatching, and postage purchase belong to other systems (transportation management, dispatch, parcel shipping) — which are also, usually, this platform's data sources. A deployment can therefore pair a TMS and a visibility platform from different vendors; the visibility layer consumes the execution side's signals. If a product's center shifts to committing carriage, it has stopped being this type.

### The record is permanent and forward-only at completion

Shipment records are durable: they are not deleted, and once completed they are locked as historical fact. Corrections happen while a shipment is upcoming or in transit; the completed record is the audit trail that analytics stand on. This durability is what distinguishes a visibility platform from a transient tracking widget — the record outlives the movement.

### Status is derived, not self-declared

Location, milestones, completion, and predicted arrival come from signals, not from users keying them in. Completion typically derives from the shipment reaching its destination as defined by configured locations/areas, and milestones derive from carrier events or geospatial transitions. Users steer the derivation (accurate locations, correct references, sensible completion timing) rather than the states themselves. Where inputs are missing, the platform's honest state is a gap — and exposing data coverage and feed quality is part of the product's job, precisely because silent gaps produce confident wrong answers.

### Alerts are managed work items

An alert has a lifecycle: raised, worked, and resolved — automatically (conditions returned to normal) or manually (a person closed the loop, with notes). The resolution state is visible at population scale, so a team's exception posture — what is red, what is being worked, what is clean — reads directly off the map and list. Alert definitions are configurable per shipment or per template: what constitutes a delay, a deviation, or a threshold breach is the tenant's operational policy, expressed in the product.

### Sharing is permissioned

Live visibility is commercially sensitive. Who may see a shipment — internal roles, external collaborators, downstream customers — is controlled per shipment or per relationship; externally shared views typically expose the movement, not the tenant's whole book. The platform is therefore both an information product and an access-control surface over it.

### The unit of watch is the consignment, not the goods

The platform tracks the movement of freight as a whole. It does not track individual lots or items through transformations, and it does not own the commercial order behind the movement — those live in traceability and order-management systems respectively, and link in as references. When the question is "what happened to this batch" or "what is the state of this order," another system of record is the authority; the visibility platform supplies the movement layer of the answer.

## Variants

- **Network/API pole** — visibility assembled purely from carrier-system connections at scale; the multi-modal, multi-carrier network is the product's moat; typical of enterprise shipper and 3PL deployments.
- **Hardware-first pole** — visibility anchored on dedicated tracking devices placed with the freight, which supply location and condition signals directly; strong in high-value, sensitive, or perishable freight; carrier data used as a complement.
- **Road-freight regional pole** — deep road coverage through carrier telematics and driver apps, common in regional (e.g., European) truckload markets, extended toward other modes.
- **Control-tower suites** — the visibility layer embedded in a broader mirror of the supply chain (orders, inventory, facilities, assets) with automation and AI agents acting on the signals (chasing ETAs, rescheduling appointments, answering status inquiries).
- **Condition-sensitive deployments** — pharmaceutical, food, and chemical freight where sensor-derived condition alerts (temperature and similar) ride on the same watch loop alongside location and timing.
- **Seat variants** — shippers, 3PLs, and logistics service providers all run this type; some vendors serve them from one platform, others have split the LSP-facing business from the shipper-facing product.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Transportation Management System | complementary execution system | TMS rates, tenders, books, and manages carriage; the visibility platform watches the movements the TMS (and carriers) execute. Vendors package them as separate product families, and the execution system is the visibility platform's data source |
| Delivery Experience Platform | adjacent consumer-facing type | the delivery-experience type serves the shopper under the brand's identity (branded tracking page, proactive post-purchase comms); the visibility platform serves logistics operations watching consignments. Vendors that sell both ship them as separate product lines |
| Cold Chain Transportation Monitoring | adjacent condition type | cold-chain monitoring answers "did the cargo environment hold against a defined requirement," with the evidence record that follows; shipment visibility answers "where is the consignment and is it on schedule." Condition alerts may ride on the visibility watch loop when sources carry sensors, but the condition-of-record is the cold-chain type's center |
| Courier / Last-mile Delivery / On-demand Delivery / Parcel Management Platforms | execution-side cluster | those types dispatch drivers, match capacity, or purchase postage/labels — they create and execute deliveries; this type watches shipments (including theirs) without executing anything, and holds no operator-business frame (no client-account rating/billing) |
| Vehicle Telematics Platform | data-source adjacency | telematics centers the vehicle/asset (health, behavior, driver); this type centers the consignment being carried. Telematics feeds are one of the data sources feeding the shipment picture |
| Order Management System | upstream record | OMS owns the customer order and its fulfillment lifecycle; the visibility platform owns the shipment movement. Orders link to shipments as references; "where is my order" is answered from the shipment layer, but the order's state is the OMS's authority |
| Food Traceability Platform | different unit of record | traceability tracks lots/batches through transformations across partners; this type tracks cargo-agnostic consignments through movements. No lot identity or transformation model here |
| Freight Forwarding System | orchestration vs watching | the forwarder's system of record is the multi-leg consignment with documents and the multi-party charge ledger; the visibility platform may watch those consignments but holds no document/charge machinery |
| Transportation Exception Management | capability vs type seam | alert/exception triage is a standard capability inside every visibility product; a dedicated exception-management type would center the exception case workflow itself. Boundary to be confirmed by that leaf's own research pass |

The load-bearing boundary is the execution seam: **remove the watching layer's independence from carriage execution and this type collapses into a TMS or dispatch system; remove the external data sourcing and it collapses into nothing at all** — a shipment register without a pulse. Every other boundary follows from what the shipment record is anchored to: movement (this type), condition (cold chain), order (OMS / delivery experience), vehicle (telematics), lot (traceability), consignment-with-documents (forwarding).

## Representative Products

- **project44** — multi-modal visibility network for enterprise shippers and LSPs; ships visibility as a product family distinct from its transportation-management and consumer e-commerce logistics families
- **FourKites** — enterprise control-tower platform layering shipment visibility beneath order/inventory/facility twins, with automated follow-up actions on ETAs, appointments, and proof of delivery
- **Shippeo** — European road-first real-time visibility with carrier-network onboarding, data-completeness governance, and recipient communication surfaces
- **Tive** — hardware-first visibility: dedicated tracking devices feeding a shipment platform, with condition alerting and completed-shipment analytics

The type is recognized by the market's own category naming for real-time transportation visibility platforms; the four sampled products deliberately span the network pole, the hardware pole, the regional road pole, and the suite pole.

## Sources

Research date: **2026-09-09**

- Tive — External Knowledge Base (help center): support hub; Creating Shipments; Shipment List and Map; Tive Reveal Overview; Sharing Data — https://support.tive.com/
- Shippeo — official product pages: Platform Overview (platform marketecture, network operations, communication, derived solutions); Real-Time Visibility; company root (category recognition) — https://www.shippeo.com/
- project44 — official product pages and site navigation: platform families (Transportation Management / Visibility / Yard Management / eCommerce Logistics), visibility sub-families by mode, carrier connection types and onboarding, customer references — https://www.project44.com/
- FourKites — official product pages: platform overview, Order/Shipment digital twins, digital-worker capabilities, outcomes catalog — https://www.fourkites.com/

> Sourcing limitations: project44's developer/operational documentation was unreachable from the research environment (transport error), and the Shippeo help center is login-gated, so both vendors are evidenced at the official-product-page level only; no operational UI or numeric details are asserted for them. FourKites evidence is product-page level. Tier-1 operational detail in this document comes from the sampled help-center documentation of one product; where a capability is known only from that product it is written as "typically/where present" or omitted. All network-scale statistics seen on vendor pages were treated as marketing claims and are not repeated as facts.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis against neighboring types are recorded in the paired Research Notes.
