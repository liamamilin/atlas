# Ocean Freight Management

## Overview

An **Ocean Freight Management** application is the cargo-side system of record for moving goods by sea: it manages ocean shipments as persistent records, executes them with ocean carriers (booking space, exchanging shipping instructions, obtaining the bill of lading), and follows the containers through the voyage until the cargo is delivered.

The defining core is small:

```text
Ocean Shipment (unit of record)
└── Carrier execution loop
    └── booking → shipping instructions → bill of lading
        └── Voyage follow-through
            └── container milestones + exceptions, gate-in to delivery
```

Everything else commonly associated with the category — rate management, invoicing, customer portals, customs filings, workflow automation — is a widespread addition that makes the system commercially complete, but does not define it. A product that only tracks containers, or only manages ocean rates, is not an ocean freight management system; each covers one stage of the lifecycle.

The mode binding is part of the definition: the record is made of ocean objects — containers, vessels and voyages, ports of loading and discharge, bills of lading, free time. Remove the ocean binding and the product becomes a generic freight-forwarding or transportation management system. Remove the execution loop and it becomes a shipment visibility platform.

## Users & Context

The users are the parties on the cargo side of ocean shipping — the ones arranging carriage of goods they do not themselves transport:

- **Freight forwarder operations staff** — create and manage shipments on behalf of customers: request bookings, prepare documentation, follow containers, keep customers informed.
- **NVOCCs (non-vessel-operating common carriers)** — buy vessel space from ocean carriers and issue their own house bills of lading to shippers; the system is their shipment and document engine.
- **Shippers / beneficial cargo owners** — importers and exporters managing their own ocean moves: booking directly or through agents, tracking containers, watching costs.
- **Documentation staff** — produce and amend shipping instructions, bills of lading, and manifests against carrier cut-off times.
- **Finance staff** — attach freight charges and surcharges to shipments, invoice customers, reconcile carrier invoices, handle demurrage and detention exposure.

The working context is defined by the mode itself: ocean shipments take weeks, span multiple organizations (shipper, forwarder/NVOCC, ocean carrier, ports, customs, trucking), and are document-heavy. The system is therefore an operations workspace used continuously over a shipment's life, not a point-of-action tool. Work is organized by shipment (often called a job or file), grouped by customer, trade lane, and direction (import/export).

## Core Model

### The Ocean Shipment as the Unit of Record

The center of the system is the **shipment**: a persistent, individually identified record of moving specific cargo by sea between named ports. Everything else hangs off it.

A shipment carries:

- **The route** — port of loading, port of discharge, and the vessel/voyage the cargo is expected to travel on; commonly with intermediate legs for transshipment.
- **The booking** — the confirmed arrangement with an ocean carrier for space on a vessel. The booking is the operational contract that sets the sailing the cargo is expected to make.
- **The containers** — the physical units holding the cargo. A shipment may involve one container (full container load) or several; containers carry identifiers, type, seal, and weight data, and are what ports, carriers, and trackers actually report on.
- **The documents** — shipping instructions, the bill of lading (the document of title that governs the cargo), manifests, and certificates; generated, amended, and exchanged against carrier deadlines.
- **The charges** — freight rates, surcharges, and local charges attached to the shipment, resolving into customer invoices and carrier cost (in products that carry the commercial layer).

### The Carrier Execution Loop

The shipment is executed through a loop with the ocean carrier:

```text
Booking request
→ booking confirmation (space on a vessel/voyage)
→ cargo gated in at the port of loading
→ shipping instructions exchanged with the carrier
→ bill of lading issued
```

An NVOCC sits inside the same loop twice: it books space from the carrier with a master bill of lading above it, and issues its own house bill of lading to its customer below.

### Voyage Follow-Through

From gate-in at origin to final delivery, the shipment's containers accumulate **milestones** — gated in, loaded, sailed, discharged, gated out, delivered — together with exceptions: delays, vessel diversions, rolled cargo, missed cut-offs, free time about to expire. The status truth is reported by the carriers, ports, and terminal systems; the cargo-side system consumes it, attaches it to the shipment, and turns it into work (alerts, tasks, customer notifications).

### Standard Capabilities

Mature products commonly add, on top of the defining core:

- **Rate and quote management** — search and compare ocean rates and surcharges, apply margins, turn quotes into bookings without re-entry.
- **Sailing schedule search** — compare carrier schedules and transit options when planning a shipment.
- **Freight charges and invoicing** — cost the shipment, invoice the customer, hand off to accounting.
- **Carrier connectivity** — electronic exchange (EDI/API) of bookings, shipping instructions, tracking events, and bill of lading data with carriers and ports.
- **Exception management** — a log of current and historical exceptions with alerts when deadlines are missed or nearing.
- **Customer portal** — self-service quotes, bookings, and tracking views for the shipper.
- **Consolidation handling** — combining multiple customers' cargo into one container (LCL) alongside full-container loads.
- **Regulatory touchpoints** — verified gross mass, port messaging, and customs filings as integrations.
- **Workflow automation** — configurable tasks and triggers per shipment type, trade lane, or customer.

## How It Works

The typical life of one shipment:

```text
Quote (rate + surcharges + margin)
→ Book space with the carrier
→ Confirm booking; plan cargo readiness against cut-offs
→ Gate containers in at the port of loading
→ Submit shipping instructions
→ Receive/issue the bill of lading
→ Follow the voyage: milestones and exceptions, leg by leg
→ Arrival, gate-out, delivery
→ Settle charges: invoice the customer, reconcile carrier costs
```

**Quote and book.** The user searches rates and sailing schedules for a trade lane, assembles a quote with surcharges and margin, and on acceptance converts it into a booking request to a carrier. The carrier returns a confirmation naming the vessel/voyage. In network-form products this loop is executed as standardized electronic transactions against many carriers at once.

**Prepare and document.** Cargo must reach the port and be gated in before carrier cut-offs. The user submits shipping instructions (the cargo description that will appear on the bill of lading), and the bill of lading is issued — by the carrier, or by the NVOCC itself for its customer. Amendments follow the same path. Documentation deadlines are hard operational constraints, not preferences.

**Follow the voyage.** Once containers are in the system, their milestones flow in from carrier EDI, port and terminal connections, and vessel-position data. The user works from exception views: what is delayed, what rolled, what is approaching free-time expiry. Statuses are consumed from the carriers — the cargo side records and reacts, it does not author the operational truth.

**Settle.** Charges accumulated on the shipment — freight, surcharges, local charges, demurrage/detention — resolve into customer invoices and carrier cost reconciliation. In products without the commercial layer, this step happens in separate finance systems.

## Interfaces

Exact layouts vary by product; the surfaces below are described conceptually.

### Shipment workspace (job screen)

The primary surface — one shipment, everything about it.

- Typical information: route and vessel/voyage, booking reference, containers with identifiers and weights, document status, charges, milestone history, tasks and exceptions.
- Primary actions: create/modify the shipment, attach containers, generate documents, record events, raise exceptions.

### Booking / booking request

Where space is arranged with carriers.

- Typical information: carrier, port pair, requested vessel/voyage, equipment type and count, cargo readiness date.
- Primary actions: create booking request, receive/inspect confirmation, amend or cancel.

### Rates and quotes

The commercial front end.

- Typical information: contract and spot rates, surcharges, free-time conditions, transit times, margins.
- Primary actions: search and compare rates, build a quote, convert quote to booking.

### Sailing schedules

Schedule planning surface.

- Typical information: carrier services by port pair, departure/arrival timing, transit time.
- Primary actions: search, compare, select a service for a booking.

### Documents

Where the paperwork of the mode is produced and exchanged.

- Typical information: shipping instructions, bill of lading drafts and issued versions, manifests, filing statuses.
- Primary actions: generate, amend, submit to carrier/port, distribute to parties.

### Tracking / milestone view

The follow-through surface.

- Typical information: per-container milestone timeline, current location/status, exceptions and alerts, estimated vs planned timing.
- Primary actions: refresh status, inspect an exception, notify parties, record resolution.

### Charges / costing view

The commercial back end of the shipment.

- Typical information: estimated vs actual charges, surcharges, demurrage/detention exposure, invoice status.
- Primary actions: cost the shipment, invoice, reconcile.

### Customer portal (common)

A shipper-facing surface for quotes, bookings, and shipment status, branded to the forwarder/NVOCC where present.

## Important Rules / Behaviors

- **Cut-offs are hard constraints.** Cargo readiness, documentation, and port submission each have deadlines set by the carrier and the port. Missing them risks the container being rolled to a later vessel or held — the central operational failure this software exists to prevent.
- **A confirmed booking is not a delivered service.** Space can be rolled, vessels can be delayed or diverted; the system's exception machinery exists precisely because the plan degrades.
- **The bill of lading governs the cargo.** Its issuance, amendment, and release are controlled operations; for an NVOCC, house and master bills layer two contractual relationships on the same boxes.
- **The carrier is the source of status truth.** Milestone statuses are reported by the vessel line, ports, and terminals; the cargo-side system consumes and acts on them rather than defining them.
- **Container identity is contextual.** Container numbers are not permanently unique — a box is reused across shipments — so tracking is anchored to the container in the context of a specific shipment/voyage, and ends when the carrier closes it.
- **One shipment, many containers.** A shipment may hold several containers; tracking, documents, and charges are managed at both shipment and container grain.
- **Free time has a cost clock.** Containers sitting at ports or with consignees accrue demurrage and detention once free time expires; mature systems surface the expiry as an alert because it is the most avoidable cost in the mode.
- **Exceptions are logged, not just surfaced.** Current and historical exceptions form an audit trail of what went wrong and who acted.

## Variants

- **By operator posture** — forwarder (arranges carriage for customers), NVOCC (buys space, issues own bills of lading), shipper/BCO (manages own ocean freight). The core model is the same; the commercial relationships around it differ.
- **By load type** — full container load (FCL), less-than-container load with consolidation (LCL), and niche flows such as roll-on/roll-off for wheeled cargo.
- **By direction** — export, import, and domestic legs of an international move.
- **By regional regulatory machinery** — verified gross mass submission, export filing regimes, tariff publication duties, and region-specific shipping-order procedures (for example, the shipping-order practice in North China).
- **By product form** — the same lifecycle is realized as: a standalone ocean-specific system; the ocean mode of a multi-modal forwarding platform (the dominant form among large forwarders); a neutral booking network between shippers/forwarders and many carriers; an ocean rate-management network; and a container-visibility data layer consumed by other systems. The first two forms carry the full defining core; the last three are specialist realizations of single lifecycle stages.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Freight Forwarding System | broader | the forwarder's multi-modal business system (air + ocean + road, customs brokerage, warehousing, agent network, accounting); ocean freight management is its ocean-mode slice and is often embedded in it |
| Transportation Management System / TMS | broader, adjacent | multi-modal transportation planning and execution (procurement, routing, load tendering); its ocean slice overlaps this Type, but lacks the ocean object set (bills of lading, vessel voyages, free time) as the center |
| Shipment Visibility Platform | downstream specialist | aggregates and standardizes container tracking events for consumption; holds no booking, no documents, no shipment of record, no execution loop |
| Vessel Operations Platform / Marine Fleet Management | carrier side | the shipping line's own operations (vessels, crews, container fleets); ocean freight management is the cargo side buying that capacity |
| Port Terminal Operating System | infrastructure side | runs the terminal's yard and vessel operations at a port; not shipment-of-record management for cargo owners |
| Air Cargo Management | mode sibling | the same cargo-side logic for air: air waybills, ULDs, flights instead of bills of lading, containers, vessels |
| Freight Audit & Payment Platform | downstream specialist | audits and settles freight invoices; ocean freight management carries charges on the shipment but audit/payment is a separate discipline |
| Customs Compliance Platform / Global Trade Management | adjacent | border filings and trade regulation; integrated as touchpoints (filings, port messaging) rather than defining the Type |

The most important boundary is with **Freight Forwarding System**: in the current market, ocean freight management is frequently delivered as the ocean module of a forwarding platform. The distinction is scope, not structure — the ocean shipment lifecycle stands on its own, and standalone ocean-specific products prove the Type exists outside the forwarding suite.

## Representative Products

- **CargoWise** (WiseTech Global) — ocean mode of a multi-modal forwarding platform; bookings, schedules, rates, carrier connectivity, container tracking for large global forwarders and NVOCCs
- **Magaya** — modular platform for mid-market forwarders and NVOCCs; bookings, shipping instructions, bill of lading generation, rate management, container tracking
- **INTTRA** (by e2open) — neutral ocean booking network; electronic booking, shipping instructions, and container status between shippers/forwarders and a large carrier community

The boundary was probed against two specialist forms: **CargoSphere** (ocean rate-management network — rates without shipments) and **Vizion** (container tracking API — visibility without execution). Both fail the defining core in opposite directions, which confirms the core rather than diluting it.

## Sources

Research date: **2026-09-09**

- CargoWise — Ocean: https://www.cargowise.com/solutions/cargowise-forwarding/ocean/ ; root: https://www.cargowise.com/
- Magaya — NVOCC: https://www.magaya.com/nvocc-software/ ; Container Tracking: https://www.magaya.com/container-tracking-software/ ; root: https://www.magaya.com/
- INTTRA — Ocean Trade Platform: https://inttra.com/shipper-solutions/ocean_trade_platform ; root: https://www.inttra.com/
- CargoSphere: https://www.cargosphere.com/
- Vizion: https://www.vizionapi.com/

> Sourcing limitation: evidence is drawn from official product and solution pages fetched on 2026-09-09; gated operational help centers were not accessible in the research environment. Precise operational figures (milestone name lists, free-time defaults, cut-off windows, numeric limits) are therefore intentionally not stated in this document; where a behavior is described, it is described at the strength the sources support.
