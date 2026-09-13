# Airline Reservation / Passenger Service System

## Overview

An **Airline Reservation / Passenger Service System** is the airline-side commercial system of record for selling and delivering its own seats to its own passengers. It holds the airline's scheduled flights as availability-controlled sellable inventory, records each passenger's booking against that inventory, converts the booking into a confirmed right to travel by applying the fare and recording payment, services the booking through every change before travel, and processes passengers through check-in and boarding on the day of travel.

The industry carries two historical names for this Type — "airline reservation system" (the selling and ticketing lineage) and "Passenger Service System" (PSS). In current industry usage the two are one thing: vendors and buyers describe a PSS as an integrated suite of reservations plus departure control. This document treats the reservation/commercial spine as the defining core and day-of-travel processing as the standard second half, which is also how the products themselves are built: one shared passenger record runs from the first search to the boarding gate.

The boundary of the Type is the airline's own passenger commerce. Searching across many airlines and shopping for the best fare belongs to consumer-side flight search and booking platforms; controlling the day-of-operation (aircraft, delays, cancellations) belongs to the airline operations platform; deciding what inventory and prices to offer belongs to revenue management; carrying freight belongs to air cargo systems. Remove the airline's own flight inventory, or the committed sale of it, and what remains is a different Application Type.

## Users & Context

**Airline staff:**

- **Reservations and booking agents** (call centers, ticket offices): create, change, and service bookings on behalf of customers — availability, seat selection, fare quotes, rebooking, refunds, special services.
- **Airport check-in and gate staff**: process passengers on the day of travel — document checks, seat assignment, bag drop and bag tags, boarding-pass issuance, boarding, and the exceptions (passengers without reservations, unpaid bookings, excess bags).
- **Revenue management and pricing analysts**: set what inventory may be sold at which conditions — allocation levels per flight and fare class, fare strategies; the reservation system holds the resulting inventory and records the sales (in some deployments the optimization itself runs in a connected external system that pushes inventory levels back).
- **Fares, distribution and e-commerce staff**: administer fare rules, branded fares, promotions, ancillary products, and the airline's direct booking engine.
- **System administrators**: users, offices, security levels, and configuration across sales and airport environments.

**External parties working through the system rather than in it:**

- **Travel agents and global distribution systems (GDS)**: sell the airline's inventory in real time through standardized connectivity, including e-ticketing.
- **Partner airlines**: interline and codeshare sales, where one carrier sells seats on another's flights.
- **Handling agents at outstations**: process the airline's passengers at airports where the airline has no staff, working from passenger lists the reservation system sends them.
- **Consumers**: book, pay, select seats, buy ancillaries, check in, and receive boarding documents through the airline's website and mobile app.

The work context has two rhythms. The **selling rhythm** runs continuously from months before departure down to minutes before it: demand arrives through every channel against a shrinking, perishable pool of seats. The **day-of-travel rhythm** is concentrated and time-critical: a flight's passengers must be identified, checked in, bagged, boarded, and reconciled against the tickets sold, in a bounded window before departure.

## Core Model

### The Defining Core

```text
Airline flight schedule (from the airline's schedule planning)
  ↓ instantiated as
Sellable flight inventory (flight × date, availability controlled by fare class / allocation)
  ↓ sold through multiple channels
Passenger reservation record (named passengers ↔ flight segments + services + price)
  ↓ commercial commitment (fare applied + payment recorded)
Confirmed right to travel (ticket / order / booking confirmation)
  ↓ day of travel
Check-in and boarding (the confirmed passenger becomes a boarded passenger)
```

Three properties make up the defining core. If any one is removed, the product is no longer recognizable as this Type:

- **Sellable flight inventory.** The airline's own scheduled flights are held as controlled inventory: seats are offered under distinct classes or allocations, availability decrements as they are sold, and unsold seats perish at departure. Without inventory holding, the product is a shopping front-end that does not own what it sells.
- **Passenger reservation record.** Identified passengers are bound to specific flight segments in a record that is maintained over time — names added and corrected, flights changed, services and seats attached, cancellations processed. Without it, there is nothing to sell or service.
- **Policed commercial commitment.** The reservation's transition from held demand to confirmed entitlement — fare applied, payment recorded — is the moment the sale becomes real, and it is actively policed: bookings that are not confirmed within their allowed hold window expire automatically and their seats return to inventory. Without the commitment step, the system is an enquiry engine, not a selling system of record.

The confirmed entitlement is best understood abstractly, because its document form is changing: the industry-standard **electronic ticket** remains widespread, partner-airline and agency selling still runs on e-ticket infrastructure, and newer retailing paradigms (offer/order models) replace the ticket with an order — while serving the same role. Older, smaller, and differently positioned carriers may issue no separate ticket document at all, with the booking confirmation itself serving as the travel record.

### Standard Capabilities

Mature products across the researched sample carry most of the following. They make the system commercially and operationally complete, but they do not define the Type:

- **Multi-channel distribution of one inventory.** Direct web and mobile booking engines, call-center and ticket-office agent consoles, travel agencies through GDS connectivity, interline and codeshare partners, and API-based distribution — all selling against the same availability state. Inventory may be partitioned into channel-specific allocations (agency allotments, tour-operator contracts) while remaining one record.
- **Fares management.** A fares database and rules engine that prices the inventory — fare families or branded fares, promotional codes, change and refund service fees; increasingly continuous or dynamic pricing and algorithmically priced ancillaries.
- **Ticketing infrastructure.** Electronic ticketing with settlement-oriented data flows: ticket records that can be issued through agencies and GDS, interline e-ticketing with partner airlines, and standardized exports of sales and used-ticket data to revenue accounting and settlement processes.
- **Seat management.** Seat maps shared between selling and check-in — the same seat that was selected (or paid for) at booking is the seat assigned at check-in; paid and free seat selection is a standard ancillary.
- **Ancillary retailing.** Bags, seats, and non-air products (hotels, cars, transfers, insurance) sold alongside the flight, before and during travel.
- **Departure control.** Airport check-in with seat assignment, bag tags and boarding passes; web and mobile check-in on the same record; through-check-in across connecting flights; boarding and its reconciliation.
- **Queue-based agent workflow.** Expiries, unconfirmed bookings, and follow-ups land in agent queues rather than requiring staff to hunt for them.
- **Passenger profiles and loyalty integration.** Recognizable repeat customers and frequent-flyer accrual/redemption attached to bookings — commonly integrated, sometimes delivered by adjacent products.
- **Reporting and downstream feeds.** Sales, ticketing, and boarding data flowing to revenue accounting, settlement, and management reporting; government passenger data (e.g., advance passenger information) transmitted where regimes require it.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:            Commercial commitment
Implementations:    IATA-style e-ticket; interline e-ticket; offer/order records
                    (modern retailing); booking-confirmation-as-travel-record
                    (small/LCC carriers)

Concept:            Inventory control
Implementations:    class-based availability ladders priced by published fares;
                    dynamic/continuous pricing over the same inventory;
                    channel allocations and partner allotments carved from one record

Concept:            Departure control
Implementations:    integrated DCS on the same database; third-party airport DCS
                    receiving passenger lists and returning used-ticket data;
                    online check-in sharing the same record

Concept:            Deployment
Implementations:    vendor-hosted dedicated instance; cloud-native platform;
                    (historically) airline-owned in-house systems
```

A reader who has only seen a flagship hosted platform at a network carrier should still be able to recognize a small charter operator's reservation system from the core model — and vice versa.

## How It Works

### Put flights on sale

```text
Schedule published by schedule planning
→ flights instantiated as sellable inventory (flight × date)
→ availability opened by fare class / allocation per revenue-management direction
→ fares and conditions attached; direct channels and partner connectivity switched on
```

Inventory decisions come from the airline's revenue management function — how many seats to expose at which class levels, over what horizon. The reservation system is where those decisions become sellable reality.

### Sell a seat

```text
Availability requested (agent console / GDS / booking engine / partner API)
→ matching flights offered with class-appropriate fares
→ booking created: named passengers bound to flight segments (the reservation record)
→ payment taken and fare applied → confirmation issued (ticket or order)
→ if the booking is not confirmed within its hold window, it expires and the seat returns to inventory
```

The hold-and-expire step is the economically distinctive part: agents and consumers can hold demand without paying, so the system actively enforces the confirmation deadline — expired space is automatically returned to sale and the expired booking lands in an agent queue. Without this policing, speculative bookings would strand perishable seats.

### Service the booking

```text
Change request (new flight, name correction, seat, ancillary, special service)
→ fare rules and service fees evaluated → reprice / reissue as required
→ refund or travel credit where applicable
→ every change is made on the same reservation record across all channels
```

Because all channels work one shared record, a change made by a call-center agent is immediately visible to the website, the airport, and partner systems.

### The day of travel

```text
Passenger list prepared for each flight (from the reservation record)
→ check-in: identity and entitlement verified, seat assigned on the shared seat map,
  baggage accepted and tagged, boarding pass issued (airport, web, or mobile)
→ deviations handled: passengers with no reservation on file, unpaid or unconfirmed
  bookings, last-minute changes, excess bags
→ boarding: passengers reconciled against the flight's records
→ after departure: used-ticket data flows to revenue accounting and settlement
```

The check-in surface is bound to the same record as the sale: a passenger who checked in online is visible to airport staff instantly, and the ticket's lifecycle closes with a reconciliation loop (sold → confirmed → used → settled). In many jurisdictions the process also includes collecting and transmitting government-required passenger data (passport/APIS details), typically captured at booking or check-in.

### Work with partners

```text
Agency/GDS sales arrive through standardized real-time interfaces (availability, sell, ticketing)
→ interline: the selling airline confirms seats on the operating airline's flights
→ codeshare: the marketing carrier sells flights operated by its partner
→ outstations without airline staff: passenger name lists and change messages are sent
  to a handling agent's airport system, which processes the flight and returns used-ticket data
```

The message-based split is the clearest evidence of the Type's seams: the passenger record belongs to the airline's reservation system even when another organization performs the physical check-in.

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Agent booking console

The reservations agent's primary workspace (call center, ticket office, and often the same console used by the airline's own e-commerce back office).

- typical information: availability and fare options per flight, the reservation record (passengers, segments, seats, services, price and payment state), queues of pending items
- primary actions: create/modify/cancel bookings, quote fares, select seats, add ancillaries and special services, issue confirmations (ticket/order), process refunds, work queues

### Availability and seat map displays

Shared by agents and direct channels alike.

- typical information: flights by date/route with class-level availability; the cabin seat map with occupied/available/held seats
- primary actions: choose flight and class, select seats (free or paid), proceed to payment

### Inventory control console

The commercial control room for what may be sold.

- typical information: per-flight and per-class allocation levels, booking/sales progress, channel and partner allotments, hold-expiry activity
- primary actions: adjust availability and allocations, close/open classes, manage partner allotments (in deployments where revenue management runs externally, these adjustments arrive from that system)

### Fares and retailing administration

- typical information: fare rules and conditions, fare families/branded fares, promotions, ancillary product catalog, service fees
- primary actions: load and maintain fares, configure offers and ancillaries, publish to channels

### Internet booking engine / mobile app (consumer)

The airline's direct storefront.

- typical information: search results with fares, fare-family comparisons, seat maps, ancillary offers, the traveler's own bookings and check-in state
- primary actions: book, pay, manage booking, select seats, buy ancillaries, check in, obtain the boarding document

### Airport check-in and boarding surfaces

The day-of-travel workspace.

- typical information: the flight's passenger list with booking and confirmation state, the shared seat map, bag and document requirements, government-data flags
- primary actions: check in passengers, accept/tag bags, handle exceptions (no reservation on file, unconfirmed booking, reroutes), issue boarding passes, board and reconcile the flight

### Queue manager

- typical information: expired holds awaiting decision, unconfirmed payments, follow-ups and exceptions routed to owning offices
- primary actions: claim, resolve, escalate

### Administration and configuration

- typical information: users and offices, security levels, system parameters, channel and partner connectivity settings
- primary actions: grant access, configure rules and parameters, audit transactions

## Important Rules / Behaviors

### Inventory is perishable and availability is dynamic

A seat unsold at departure is gone — unlike a hotel room, it cannot be resold later. Availability shown to any channel reflects real-time sales across all channels, and the same flight is offered at different prices under different classes/conditions simultaneously. (Exactly how many allocation levels exist and how they are named varies by product and carrier.)

### The hold-to-confirmed transition is policed

Unpaid holds (from agents or consumers) expire automatically at the end of their allowed window; the space returns to inventory and the expired booking moves to an agent queue for processing. Hold windows are configured by the airline — globally, per market or booking window, and per flight in some products — because a scarce, fast-selling flight needs shorter holds than a slow one. This revenue-integrity mechanism exists to keep speculative bookings from stranding perishable seats.

### One record runs from sale to boarding

The reservation record, its confirmation state, seat assignments, and check-in status live on one shared data core in modern products. Web check-in state is immediately visible at the airport; a seat paid for at booking is the seat assigned at check-in. When check-in is performed by a third-party airport system, the sharing happens through standardized passenger-list messages rather than a shared database — but the record's ownership stays with the airline's system.

### Confirmation state gates the airport

Check-in verifies the confirmed entitlement: unpaid or expired bookings are not checked in, and passengers whose state doesn't match the plan (present with no reservation on file, or arriving without having completed the expected pre-travel step) are handled as explicit exception flows, not errors.

### Fare rules and service fees govern change

Changes and refunds are evaluated against the fare's conditions and the airline's fee schedule: rebooking into available classes, repricing, penalty or service fees, refunds or travel credits. The system enforces what the fare promises; it does not decide commercial policy by itself.

### Operational changes arrive as passenger consequences

Delays and cancellations are decided in the airline's operations control environment, not here — but their passenger consequences (rebooking, refunds, re-accommodation) are executed here, on the passenger records. The reservation system is where an operational decision becomes what each affected passenger experiences.

### The system records; it does not optimize alone

How much inventory to open, at which classes, with what overbooking posture, is a revenue-management decision (possibly computed in a connected external system). The reservation system holds and executes the resulting availability and records what actually sold — which is also why its sales data feeds settlement and revenue accounting downstream.

### Access is structured and audited

Agent activity spans sensitive commercial powers (override holds, refund, reissue), so mature products gate functions behind user security levels and office assignments, and log transactions for audit. Governments' passenger-data requirements add further regulated flows (passport/APIS capture and transmission) in many markets.

## Variants

- **Full-service network carrier** — the fullest form: interline and codeshare selling, cabins and fare families, agency/GDS-heavy distribution, through-check-in, deep loyalty integration.
- **Low-cost carrier** — direct-channel-centric, single-cabin, ancillary-led retailing, minimal interline; the booking confirmation and order often take the place of traditional tickets; fast, dynamic-pricing-driven availability.
- **Hybrid / regional / charter** — mixtures of the above; charter carriers add tour-operator contract and allotment management on the same inventory as seat-only sales.
- **Staff and non-revenue travel** — airline employees fly under separate rules; some vendors deliver this as a dedicated module in the passenger-services family.
- **Deployment models** — vendor-hosted dedicated instance (traditional), cloud-native platform (current), and the historical airline-owned system; the hosted model is why the passenger record can outlive any one airline's IT department.
- **Confirmation paradigm** — e-ticket-based selling (still the interline/agency backbone) coexisting with offer/order retailing; products differ in how far they have moved.
- **Regional regimes** — government passenger-data transmission, security-document checks, and settlement-plan arrangements vary by market and add region-specific flows.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Flight Search / Booking Platform (and OTA) | consumer-side counterpart | searches and shops across many airlines and initiates bookings into the airline's system through distribution interfaces; holds no airline inventory of its own and never tickets, checks in, or boards. Remove the airline's own inventory and confirmation from this Type and what remains is the search/booking platform |
| Airline Operations Platform | coupled counterpart (operational side) | holds the same flights as operational objects (legs, aircraft, delays) and decides operational changes; this Type holds them as sellable inventory and executes the passenger consequences. A delay decision is made there and consumed here |
| Airline Revenue Management | upstream optimizer | computes availability/allocations/pricing strategy; this Type holds the inventory, sells it, and records the sales. Optimization without execution vs execution without optimization |
| Airline Crew Management | sibling (people vs passengers) | manages crew and rosters under legality rules; this Type manages passengers and bookings under fare rules |
| Air Cargo Management | freight analog | air waybills, weight/volume capacity, terminal handling vs tickets, seat classes, check-in; the two never share a record |
| Airport Operations Platform | organizational seam | airport-side resources (stands, gates, turnarounds for all airlines) vs airline-side passenger processing; handling-agent message exchange marks where one ends and the other begins |
| Hotel Central Reservation System / Hotel PMS | structural analog (different economics) | same shape (inventory → reservation → confirmation → check-in) but rooms are length-of-stay inventory with no fare-class ladder, no ticket document, no interline/codeshare, no government security-data regime. Remove the airline flight semantics and this Type collapses into the hotel pattern — which is why they are separate Types |
| Reserved Seating / Event Ticketing | seat-selling analog | sells numbered seats with inventory controls, but without fare-rule repricing, multi-carrier interline, or a day-of-travel document/bag process |
| Loyalty Program Management | adjacent module | frequent-flyer accrual/redemption commonly integrates with bookings; the program itself is a separate system |

The most important boundary is with the **consumer-side flight search / booking platform**, because both are "where flights are booked". The structural test is inventory ownership and delivery: the booking platform shops across airlines and hands the booking to the airline's system; this Type owns the airline's perishable seats, commits the sale, and delivers the passenger to the aircraft.

## Representative Products

- **iFly RES** (IBS Software) — cloud-native PSS positioning: omnichannel retailing, reservations, servicing and end-to-end passenger processing with integrated departure control; offer/order (NDC / One Order) capabilities alongside traditional GDS/interline/codeshare selling; LCC and hybrid carriers prominent among customers.
- **VRS** (Videcom) — traditional IATA-compliance-first reservation system with integrated departure control, hosted as dedicated instances for smaller carriers; explicit documentation of ticket-time-limit policing, GDS/interline e-ticketing, and third-party-DCS message exchange.

The researched sample spans different philosophies (cloud-native retailing platform vs compliance-first hosted system) and different customer tiers. Several major enterprise PSS providers — including the two largest global distribution-linked platforms and two further PSS specialists — could not be reached during research and are excluded from the sample (see Sources).

## Sources

Research date: **2026-09-06**

Primary vendor surfaces (official product pages and case study):

- IBS Software — Airline Passenger Solutions (iFly): https://www.ibsplc.com/product/airline-passenger-solutions
- IBS Software — iFly RES product page: https://www.ibsplc.com/product/airline-passenger-solutions/ifly
- IBS Software — Fly Gangwon PSS migration case study: https://www.ibsplc.com/case-studies/airline-passenger-solutions/opening-new-skies-for-fly-gangwon-with-an-agile-pss-migration
- Videcom — Airline Systems Overview: https://www.videcom.com/airline-system.aspx
- Videcom — Ticket Time Limits: https://www.videcom.com/airline-ticket-time-limits.aspx
- Videcom — Departure Control System: https://www.videcom.com/airline-departure-control-system.aspx
- Videcom — module index: https://www.videcom.com/
- Accelya — product catalog (industry-structure reference only): https://www.accelya.com/

> Sourcing limitation: vendor help-center / user-guide documentation was not reachable for any sampled product, and the enterprise-flagship tier (Amadeus, Sabre) plus two further PSS specialists (Radixx, Hitit) could not be reached at all — official pages bot-blocked, unavailable, or unrelated domains. Evidence is drawn from official product pages and one official case study of two vendors at different market tiers, cross-checked where possible against industry-standard structures. Accordingly: precise operational parameters (exact hold-window values, allocation schemes, message-format detail, settlement mechanics) are deliberately not stated; claims that rest on a single product's documentation are marked product-dependent in the paired Research Notes, and enterprise-tier-only behavior is not asserted. Detailed observations, the cross-product comparison, and evidence calibration are recorded in the paired Research Notes.
