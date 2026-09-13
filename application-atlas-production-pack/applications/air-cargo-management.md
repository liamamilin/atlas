# Air Cargo Management

## Overview

An **Air Cargo Management** application is the operational system used by airlines and airport cargo handlers to run the carriage of freight by air. It records each shipment under its **air waybill**, books and allocates it onto **scheduled flights**, steers its physical handling through the **cargo terminals** at both airports, tracks it across the **airport-to-airport journey** through status events exchanged between the parties, and computes the **charges** the carriage earns.

It answers a problem no other logistics application solves: an aircraft's payload is a scarce, weight-and-volume-limited resource sold in advance, the goods themselves must pass through security screening, dangerous-goods checks and customs at specific airports, and the shipment changes hands between an airline, a ground handler, a freight forwarder and a customs authority — all of whom must work from the same shipment record and the same milestone states.

The boundary of the Type is the air carriage itself. Managing a customer's door-to-door order across multiple modes belongs to freight forwarding systems; operating the aircraft belongs to airline operations; carrying parcels through an owned door-to-door network belongs to parcel/courier systems. Air Cargo Management begins when goods are tendered for an air waybill at an airport and ends when they are released for delivery at the destination airport.

## Users & Context

The Type is unusual in that no single organization operates the whole chain, so "the user" depends on which seat at the airport the product is installed in.

**Airline cargo division (belly-hold or freighter):**

- cargo sales staff: quote rates, accept bookings, manage allotments given to large customers and origin stations
- capacity and revenue analysts: forecast demand, optimize what gets loaded on each flight, set dynamic prices
- cargo operations staff: plan the transportation of accepted shipments across flight legs, monitor uplift, handle offloads and rebookings
- revenue accounting staff: rate completed carriage, invoice agents and interline partners, settle

**Ground handling agent / cargo terminal operator:**

- terminal operations staff: accept cargo, screen it, build it into unit load devices, store it, break down arrivals, hand it over
- warehouse supervisors: steer tasks and resources against flight departures and service-level commitments
- handling accounting staff: charge airlines for the handling services performed

**Freight forwarder (the airline's customer):**

- air freight operators: book capacity with airlines, issue house air waybills over master air waybills, track shipments, invoice their own customers. Forwarders run their own systems (see Related Application Types); the air module of those systems overlaps this Type.

The work context is defined by the flight departure: everything in the terminal is scheduled backwards from wheels-up times, and a missed connection is an operational exception with commercial consequences. The system is therefore used continuously through the day by back-office staff (booking, rating, documentation) and by warehouse staff on mobile or handheld scanning devices (physical handling).

## Core Model

### The Defining Core

```text
Air Waybill (AWB)
└── Shipment / consignment (the central managed record)
    └── Booking on flight(s) — allocation of aircraft capacity
        └── Airport-to-airport carriage lifecycle
            (accepted → built & staged → uplifted → arrived → released)
            recorded as status events shared between the parties
```

Three properties. If any one is removed, the product is no longer recognizable as Air Cargo Management:

- **Shipment under an air waybill.** The air waybill is the industry's standardized document for air freight; its number identifies the shipment, records the contract of carriage, and anchors all charging. A forwarder may issue a **house air waybill (HAWB)** for its customer's consignment and consolidate several of them under the airline's **master air waybill (MAWB)** — the layering differs, but every shipment in the system is identified by an AWB-family number. Without this, the product is a generic freight or warehouse system.
- **Flight capacity allocation.** The transport resource is the scheduled flight, whose capacity is measured in weight and volume terms and sold in advance. Bookings, allotments, load planning and offload decisions all exist because aircraft capacity is finite and contested. Without this, the product is a terminal or forwarding system with no airline in it.
- **Tracked airport-to-airport carriage lifecycle.** The shipment moves through named milestones — tendered and accepted at the origin terminal, built and staged, departed, arrived, released at the destination — and each milestone is recorded as a status event that the other parties can see. Without this, the product is a document store, not an operations system.

### Standard Capabilities

Mature products across all three operator seats carry most of the following. They are what makes the system commercially and operationally usable, but they do not define the Type:

- **Rating and charging.** Rate rules are applied to the shipment's measured characteristics (weight and volume, by lane, airline and commodity) to produce the charges for the carriage; on the airline side this extends into invoicing, revenue accounting and interline settlement. Every researched product includes charging in some form; it is the commercial backbone of the Type rather than part of its identity.
- **Terminal handling control.** The warehouse side of the airport: acceptance and check-in of tendered cargo, security screening, build-up of shipments into **unit load devices (ULDs)** — the pallets and containers that group shipments onto aircraft — storage, breakdown of arrivals, and handover. Executed with mobile/handheld scanning and task steering against flight departures.
- **ULD control.** Unit load devices are returnable assets that circulate between airlines and handlers; mature carrier and handler systems track ULD stock, movements with flight departures and arrivals, and loan/borrow transactions between parties.
- **Status messaging between parties.** The shipment record is shared across organizations through standardized electronic messages (the Cargo IMP message family and related airline–handler message standards in current use, with the industry's ONE Record data-sharing standard emerging as the successor). Pre-advice, delay and estimate changes flow the same way.
- **Compliance workflows.** Security screening status captured before uplift; dangerous-goods checks under the industry's Dangerous Goods Regulations, including the notification that travels with the flight crew (NOTOC); customs declaration linkage at borders.
- **Track and trace.** Internal views of shipment and flight status, plus customer-facing portals where shippers and forwarders follow their consignments, including map-based views of multi-leg journeys and split cargo.
- **Capacity management tooling.** On the airline side: demand forecasting, capacity availability by flight, allotment management for contracted customers, and load optimization.
- **Workflow and exception handling.** Task lists, milestones and alerts keyed to flight times; exception logs for missed cut-offs, delays, offloads and split shipments.

### One Structure, Three Seats

The same core model is operated from three different seats, which is why the market offers differently-shaped products:

```text
Concept:            Shipment under an air waybill
Airline seat:       sells and manages the carriage (booking, rating, uplift)
Handler seat:       executes the physical flow (accept, screen, build, break down)
Forwarder seat:     buys capacity and consolidates (HAWB over MAWB, tracking)

Concept:            Flight capacity
Airline seat:       the resource it sells and optimizes
Handler seat:       the deadline its tasks are steered against
Forwarder seat:     the resource it books from airlines
```

## How It Works

### The commercial loop (airline seat)

```text
Quote a rate (lane, airline, commodity, shipment characteristics)
→ accept a booking for capacity on a flight or routing
→ issue or capture the air waybill
→ plan the shipment's transportation across legs
→ monitor uplift; rebook if offloaded or missed
→ rate the completed carriage and invoice
→ settle (with agents and, for interline carriage, between airlines)
```

The booking is a promise against finite capacity, so the loop includes continuous re-planning: demand forecasting, allotment management for contracted customers, and — in the most advanced airline implementations — dynamic pricing that revalues remaining capacity as departure approaches.

### The terminal loop (handler seat)

```text
Receive pre-advice of an incoming shipment
→ accept and check in the tendered cargo (pieces, weights, measurements)
→ security screening and dangerous-goods checks
→ build shipments into ULDs; store or stage by flight
→ deliver built ULDs to the aircraft; record departure
→ on arrival: receive, break down, store
→ release against customs status and hand over for delivery
→ charge the airline for the handling performed
```

In transit-heavy terminals the same system is configured as a hub: tasks are auto-prioritized by when each shipment must meet its outbound booking or a product service-level commitment.

### The visibility loop (all seats)

Status events flow between the parties as standardized messages: a booking confirmed at the airline becomes a pre-advice at the handler; acceptance, departure and arrival events flow back to the forwarder and the shipper; delays and estimate changes propagate to everyone watching the shipment. Operators work from exception views — what missed a cut-off, what was offloaded, what was split across flights — rather than from raw message feeds.

### The document thread

The air waybill runs through everything: created at booking, completed with shipment detail, exchanged electronically between forwarder and airline (the industry's e-AWB program moves the paper document into an end-to-end electronic process), referenced in every status message, and used as the basis for rating and settlement. The industry's ONE Record standard extends this into a shared single record view of the shipment across all parties.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product and by operator seat.

### Booking / reservation console (airline)

- Purpose: sell and confirm capacity.
- Typical information: flight schedules and connections, available capacity by flight, rates by lane and commodity, customer allotments, shipment details.
- Primary actions: quote, book, modify booking, issue AWB, assign to a transportation plan.

### Shipment file / AWB record view (all seats)

- Purpose: the single operational record of a shipment.
- Typical information: AWB number (master and house layering), parties, pieces, weights and measurements, commodity and special-handling codes, routing and legs, current milestone status, attached documents.
- Primary actions: update details, record events, attach documents, message parties.

### Terminal / warehouse control (handler)

- Purpose: steer the physical flow in real time.
- Typical information: task queues by flight and deadline, shipment and ULD locations, screening and DG status, storage locations.
- Primary actions: accept, screen, build ULD, move, stage, load, break down, release — mostly executed on handheld scanners.

### ULD control (airline / handler)

- Purpose: manage the circulating asset pool.
- Typical information: ULD stock by station, movements against flights, loan/borrow positions.
- Primary actions: record transfers, reconcile stock, apply storage/demurrage charges.

### Track and trace (all seats, plus customer-facing portal)

- Purpose: follow shipments across legs and parties.
- Typical information: milestone timeline, current flight position, split-cargo parts, estimated times.
- Primary actions: search, watch, subscribe to alerts, share status with customers.

### Rating, invoicing and revenue accounting (airline / handler)

- Purpose: turn completed carriage and handling into money.
- Typical information: rate rules, chargeable quantities, invoices, interline billing, settlement status.
- Primary actions: rate, invoice, reconcile, settle.

### Messaging / integration monitoring

- Purpose: keep the inter-organizational message flows healthy.
- Typical information: message queues, failures, partner connectivity.
- Primary actions: re-send, repair, monitor compliance feeds.

## Important Rules / Behaviors

### A confirmed booking is not carriage

A confirmed booking reserves capacity but does not guarantee uplift. Physical acceptance, screening completion, build-up before cut-off, and the aircraft's actual weight and balance all sit between the booking and the departed event. Offloads and rebookings are normal operational events, not failures of the system — which is why exception handling is a first-class capability.

### The air waybill is contract, identifier and accounting basis at once

The AWB number keys the shipment operationally; the AWB document is the contract of carriage; the same record drives rating and settlement. House/master layering means several commercial shipments can travel under one airline document, and status events must work at both levels.

### Capacity is two-dimensional and contested

Aircraft capacity is consumed by both weight and volume; a shipment can be volume-limited before it is weight-limited. This is why charge computation is based on the shipment's measured characteristics rather than on gross weight alone, and why load optimization is a distinct airline capability. (Exact chargeable-quantity formulas are carrier- and tariff-specific and are not uniform across the industry.)

### Dangerous goods and security are gating conditions

Shipments declared as dangerous goods must satisfy the industry's Dangerous Goods Regulations before acceptance, and the flight crew must be notified of what is aboard (the NOTOC). Security screening status must be captured before uplift. Products embed these as workflow gates, not as paperwork afterthoughts.

### The shipment record is inter-organizational by design

No single party owns the whole chain. The airline, the handler at each airport, the forwarder and customs each hold a partial view, synchronized by standardized status messages. A milestone recorded by one party becomes visible to the others; missing or late messages are themselves operational exceptions.

### ULDs circulate and are charged

Unit load devices move between airlines and handlers continuously; systems track who holds what, and loan/borrow positions can carry storage or demurrage charges. ULD stock at a station is an operational resource with its own planning thresholds.

### Shipments can split

Cargo tendered under one air waybill may travel on different flights (split across legs or offloaded in part). Tracking, arrival handling and delivery must work per piece and per part, not only per document.

## Variants

- **Airline cargo division (belly-hold)** — cargo shares passenger aircraft; capacity depends on the passenger schedule; the cargo system consumes flight schedules from airline operations.
- **All-cargo carrier** — freighter networks where capacity is the product itself; typically deeper revenue-management and load-planning tooling.
- **Ground handling agent / cargo terminal operator** — the handler seat as the product's center of gravity: warehouse control, task steering, DG/NOTOC, handling charges; the commercial loop is reduced to charging the airline.
- **Forwarder air-freight module** — the buyer seat inside a forwarding platform: booking with airlines, house air waybills, tracking, customer invoicing; overlaps the Freight Forwarding System Type (see Related Application Types).
- **Mail carriage** — postal consignments handled under postal-union standards, with mailbag-level tracking and separate accounting; a dedicated module in some carrier platforms.
- **Special-product flows** — pharmaceutical cold chain, perishables, live animals, high-risk dangerous goods: same core model with additional handling, monitoring and compliance requirements.
- **Hub / transit-heavy terminals** — the terminal system configured to prioritize transit cargo against outbound connections and service-level commitments.
- **Airport cargo community platforms** — airport-wide data-sharing layers sitting above individual operator systems; adjacent infrastructure rather than a variant of this Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Freight Forwarding System | overlapping (buyer seat) | centers on the customer's multi-mode order — quote-to-invoice across air, ocean and road plus customs and warehousing; Air Cargo Management centers on the air carriage itself (capacity, flights, terminal handling). Remove flight capacity and airline-side handling and what remains is forwarding; remove the multi-mode customer-order layer and what remains is this Type |
| Ocean Freight Management | mode sibling | same structural pattern (shipment + booking + carriage lifecycle + charges) with ocean objects: vessels, containers, bills of lading, port terminals — not flights, ULDs and air waybills |
| Airline Reservation / Passenger Service System | passenger analog | manages persons, itineraries and tickets against seat inventory; cargo manages goods under air waybills against weight/volume capacity |
| Airline Operations Platform | upstream neighbor | operates the aircraft (dispatch, crew, fuel); the cargo system consumes its schedules and contributes payload data; neither replaces the other |
| Ground Handling Management | adjacent service domain | centers on passenger and ramp handling services; cargo terminal handling is the air-cargo-specific slice and is treated as a variant of this Type |
| Port Terminal Operating System | mode-sibling analog | the ocean-terminal counterpart of the cargo-terminal slice; different mode, different objects |
| Parcel / Courier Management | express neighbor | door-to-door single-piece networks with owned aircraft and vehicles; air cargo is airport-to-airport, consignment-based and multi-party, and does not own the door legs |
| Transportation Management System / TMS | shipper-side neighbor | plans and executes ground transportation for shippers; no air waybills, no flight capacity, no terminal handling |
| Shipment Visibility Platform | downstream layer | observes and aggregates status events; Air Cargo Management is the operational system of record that produces them |

The most important boundary is with **Freight Forwarding System**, because forwarder products contain a genuine air module and carrier products sell to forwarders. The structural test is the center of gravity: whose commercial and operational cycle does the system exist to run — the airline's capacity and the terminal's physical flow (this Type), or the forwarder's customer order across modes (forwarding)?

## Representative Products

- **CargoWise** (WiseTech Global) — forwarder-side global platform; air freight execution with direct airline eBooking connections, rate management, air waybill automation and live flight tracking
- **iCargo** (IBS Software) — carrier-side platform used by cargo airlines, belly-cargo divisions and ground handlers; sales/reservation, capacity and revenue management, terminal operations, ULD management, revenue accounting and mail
- **Hermes 5** (Hermes Logistics Technologies) — ground-handler cargo management system for airport warehouse import/export/transit processes, with hub configuration and compliance workflows
- **Magaya Supply Chain** (Magaya) — forwarder/3PL platform for the SMB–mid tier; air freight as a mode within quote-to-invoice forwarding workflows with air tracking and customs compliance

The defining core was checked across all three operator seats (airline, handler, forwarder) and against the industry-standard layer (IATA e-AWB, ONE Record, Cargo iQ route maps, Dangerous Goods Regulations) to avoid over-fitting to any single seat's implementation.

## Sources

Research date: **2026-09-06**

- CargoWise — Air Visibility (air freight solution): https://www.cargowise.com/solutions/cargowise-forwarding/air/
- CargoWise — platform overview: https://www.cargowise.com/
- IBS Software — Air Cargo solutions: https://www.ibsplc.com/product/air-cargo-solutions
- IBS Software — iCargo product page: https://www.ibsplc.com/product/air-cargo-solutions/icargo
- Hermes Logistics Technologies — Hermes 5 SaaS: https://hermes-cargo.com/products-services/hermes-5-saas/
- Hermes Logistics Technologies — overview: https://hermes-cargo.com/
- Magaya — platform overview: https://www.magaya.com/
- IATA — Cargo program: https://www.iata.org/en/programs/cargo/
- IATA — Digital Cargo (e-freight/e-AWB, ONE Record): https://www.iata.org/en/programs/cargo/e/
- Cargo iQ — Route Maps and performance management: https://www.cargoiq.org/

> Sourcing limitation: vendor help-center / user-guide documentation was not reachable for the sampled products; carrier-side vendors publish little operational documentation publicly, and one major carrier-side vendor (CHAMP Cargosystems) could not be reached at all. Product evidence is therefore drawn from official product/solution pages plus industry-standards bodies, and operational details are deliberately described at conceptual level. Precise numeric parameters (chargeable-quantity formulas, message-code vocabularies, time windows, stock thresholds) are intentionally not stated. Detailed observations, cross-product comparison and evidence calibration are recorded in the paired Research Notes.
