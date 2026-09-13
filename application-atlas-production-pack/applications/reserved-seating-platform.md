# Reserved Seating Platform

## Overview

Reserved seating is the seat-level selling layer of event ticketing: selling admission to **specific, assigned seats** rather than to an event at large. Its defining structure is small:

```text
Seat map (a designed, persistent chart of sections / rows / seats,
          plus tables, pods, and general-admission areas)
└── Seat-level allocation (specific seats assigned to specific buyers —
    by the buyer's own selection or by best-available assignment)
    └── Seat-bound ticket (the issued ticket names the seat)
```

In the current market this layer is realized in two product forms, and the distinction matters for understanding the leaf:

- **As a built-in capability of ticketing platforms.** In the events and venues domain, the products that sell assigned seats end-to-end — chart design, seat selection, checkout, tickets, entry — are event ticketing platforms, with reserved seating as one selling mode alongside general admission. Vertical systems (cinema, arts subscriptions, sports season ticketing) carry the same seat-level layer inside their own domain models.
- **As a dedicated seat-map component.** A separate product family supplies exactly the seat-map layer — chart design tools, an interactive buyer-facing map, and real-time seat-availability management — for ticketing platforms to embed. These components explicitly do not sell tickets or take payments; the embedding platform does.

No standalone end-to-end "reserved seating platform" product family was found in the market: the seat map is always either a mode inside a selling system or a component serving one. This document therefore describes the seat-level layer itself — what it consists of, how it works, and where its boundaries sit — as it exists across the market.

## Users & Context

The operator side is the primary user:

- **seating or box-office manager** — designs and maintains the seat map, sets per-seat pricing, manages holds and blocked seats
- **ticketing staff / box office** — sells specific seats to buyers, including over the counter and by phone
- **event organizer or promoter** — decides the layout, pricing tiers, and selling order for a production or season

The buyer side is the ticket buyer, who picks seats on an interactive map (or accepts best-available assignment) and receives a ticket that names a specific seat.

Typical contexts: theaters and performing arts, concerts and arenas, sports (especially season seats), cinemas, gala dinners and banquets (table layouts), comedy clubs and cabarets. The work is venue-shaped: the chart mirrors a physical room, and the same room hosts many events over time.

## Core Model

### The Defining Core

Three structures. If any one is removed, seat-level selling stops being recognizable:

- **The seat map as managed inventory.** A persistent, designed, seat-granular structure — sections, rows, and individually identified seats, plus bookable tables, pods, and general-admission areas — with a state on every seat. The chart is an asset of the venue or organizer: it is built once, maintained, and reused across events. Without it, selling is capacity counting.
- **Seat-level allocation.** Specific seats are assigned to specific buyers. Assignment happens either interactively (the buyer picks seats on a map) or automatically (the system assigns the best available seats, often the best seat at the buyer's price point). Every allocation changes seat states. Without it, nothing is "reserved."
- **Seat-bound entitlements.** The issued ticket names the specific seat — section, row, and seat number, or a table — and the seat is the unit of the commercial record: orders, refunds, exchanges, and entry all reference seat identity. Without it, the ticket is anonymous admission.

### The Event as Availability Container

The seat map and the event are distinct objects. One chart serves many events: each dated performance, match, or screening runs its own seat states against the same chart. A seat sold for one event remains free for the next. This chart-reuse across events is what makes the seat map an inventory structure rather than a one-off drawing.

### Seat States

A seat carries a small set of states, managed in real time:

- **available** — selectable by buyers
- **held** — temporarily reserved (for a buyer mid-checkout, for a VIP, or for a group allocation), commonly with an expiry after which the hold releases back to public sale
- **sold / booked** — allocated to a buyer
- **blocked / not-for-sale** — removed from sale (house seats, production holds, inaccessible seats), sometimes hidden entirely or released gradually

State changes propagate live: when a seat is held or booked, every buyer viewing the same event's map sees it become unavailable.

### Per-Seat Pricing

Pricing attaches to seats, not just to ticket types. Common machinery:

- **price tiers or bands mapped to seats** — a selection of seats (a row, a section, a block) carries a price level; premium locations carry premium tiers
- **demographic price points per seat** — the same seat sold at different prices for adult, student, senior, child, or veteran buyers
- **selling-order control** — which seats sell first (best available first is the common default; some products let the operator control the release order)
- **seat-level dynamic pricing** — in sports- and arts-scale products, seat prices that reprice as inventory sells

### Holds at Seat Grain

Holds are the operator's inventory-control surface at seat level:

- **private holds** — seats held back for VIPs and special guests, released through a link, with an expiry date
- **group or pool allocations** — a set of seats, rows, or sections available only to members of a defined group, each member picking a seat inside the allocation
- **locks / kills** — seats removed from sale for a specific performance
- **not-for-sale blocks** — seats or entire sections disabled from sale, sometimes released gradually to manage demand

### Seat Rights Across Events

In the arts and sports poles, the seat becomes a durable commercial object in its own right: a **season seat** or **seated subscription** holds one specific seat across a whole series of events. A seat sold at the series level is unavailable for individual events, and vice versa. Renewal cycles let holders keep "their seats" year over year; unrenewed seats are released back to sale on a schedule.

### Standard Capabilities

Mature implementations of the layer commonly carry most of the following. They are not what makes reserved seating what it is, but they make it practical:

- interactive chart design tools (drag-and-drop builders, templates, scanning a floor-plan image into an interactive chart, validation against double-bookable mistakes)
- buyer-facing interactive, shoppable seat maps that work on mobile
- best-available assignment, including price-point-aware assignment
- seat views (view-from-seat imagery to build buying confidence)
- seat attributes (accessible and wheelchair positions, restricted-view flags)
- mixing reserved and general-admission areas in one map
- tables and pods as bookable objects (per-seat or whole-unit)
- real-time availability updates
- seat-level reporting (sales by section, row, and price tier)

## How It Works

### Build and reuse the chart

```text
Design the seat map (sections, rows, seats; tables, pods, GA areas)
→ validate it
→ reuse it across many events
```

The chart is drawn once per venue configuration and persists. Operators maintain a library of maps — one per hall, configuration, or layout — and attach events to them.

### Run a seat-level on-sale

```text
Attach an event to the chart
→ set per-seat pricing (tiers, demographic price points, selling order)
→ place holds (private, group, not-for-sale)
→ open the sale
→ buyers pick seats on the map, or receive best-available assignment
→ seat states update in real time as seats are held and sold
→ each completed order issues tickets naming the assigned seats
```

The interaction loop is the same for staffed box-office selling, except the operator picks the seats: search the event, select specific seats for the customer, take payment, issue seat-named tickets.

### Hold and release

```text
Hold seats (link-based private holds, group allocations)
→ holders pick their seats inside the allocation
→ unclaimed holds expire and release back to public sale
```

### Carry seats across a season

```text
Define a series of events on one chart
→ sell a seat at the series level (season seat / subscription)
→ the seat is blocked for individual sale across the series
→ renewals keep the seat year over year
→ unrenewed seats release back to per-event sale
```

### Defining core vs standard capabilities vs variants

**Defining core** — without these, not reserved seating:

- the seat map as managed, reusable inventory
- seat-level allocation (selection or best-available)
- seat-bound tickets

**Standard capabilities** — present in most mature implementations:

- interactive chart design; buyer-facing shoppable maps; best-available assignment
- seat holds (private, group, locks, not-for-sale); per-seat pricing; seat views; real-time updates; seat attributes; GA mixing; tables and pods

**Common variants** — depend on segment, scale, or product form:

- seat rights across event series (seasons, seated subscriptions, renewals)
- seat-level dynamic pricing and repricing
- seat-level resale (relisting booked seats)
- product form: built-in ticketing mode vs embeddable seat-map component
- pod layouts with whole-pod purchase rules

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Chart designer (operator)

The authoring surface for the seat map.

- venue layout: sections, rows, seats; tables, pods, GA areas; non-seat objects (stage, bar); labels and legends
- primary actions: draw and edit the map, validate it, save it as a reusable chart

### Seat-map settings (operator)

The per-event configuration surface.

- pricing tiers mapped to seats; demographic price points; selling order
- holds: private holds with expiry, group allocations, not-for-sale blocks
- primary actions: assign prices, place and release holds, open or adjust the sale

### Buyer-facing seat map

The interactive selling surface.

- live availability colors, section/row/seat identity, prices on selection, seat views
- primary actions: pick seats (or request best available), hold them through checkout, complete purchase

### Box-office seat-selling view

The staffed selling surface.

- event and chart lookup, seat picking on behalf of the customer, payment, ticket issuance
- primary actions: sell specific seats, print or deliver seat-named tickets, exchange seats

### Season / renewal management (vertical poles)

The seat-rights surface in arts and sports implementations.

- series definition, seat holdings per holder, renewal status, release of unrenewed seats
- primary actions: renew, release, reassign seats

## Important Rules / Behaviors

### One seat, one buyer

Real-time state management is the layer's core discipline: only one buyer can hold or book a given seat for a given event at a time. Holds time out; bookings are exclusive. This is what prevents double selling.

### The chart outlives the event

Seat maps persist and are reused across events; seat states are per event. A seat's sale for one event never affects its availability for another — except when the seat is sold at a series level (season seats), where the series-level sale blocks per-event sale and vice versa.

### Seat identity travels with the record

The seat (section/row/seat or table) is part of the order, the ticket, and the entry record. Exchanges and refunds work at seat grain: a returned seat returns to that event's availability.

### Blocked inventory is managed, not deleted

Not-for-sale seats, locks, and hidden sections remove inventory from public sale without destroying it; gradual release is a common demand-shaping tool.

### Whole-unit objects

Tables and pods can be bookable as units: some products require the buyer to purchase all seats within a pod, so the layout rule constrains the sale.

## Variants

The layer is realized in distinct market forms:

- **built-in mode in self-serve ticketing platforms** — reserved seating as one selling mode beside general admission, with chart builders aimed at organizers (theaters, auditoriums, arenas)
- **embeddable seat-map component** — the layer factored out as a product: chart designer, interactive renderer, and seat-availability API for ticketing platforms to integrate; no selling or payment of its own
- **arts & culture depth** — seat maps as building blocks for any seated venue, select-your-own-seat maps, seated subscriptions with renewal cycles and release rules
- **sports depth** — season seats, seat-level pricing with frequent repricing, fan-side transfer/sell/renew of seat-named digital tickets
- **cinema** — the vertical where every ticket is a seat; seat selection per screening is the default buying experience (covered by its own application type)
- **table-based venues** — gala dinners, banquet halls, cabarets: tables as the bookable unit, per-seat or whole-table

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Event Ticketing Platform | the selling system this layer lives in | ticketing centers the whole sell → issue → validate loop over ticketed events; reserved seating is one of its selling modes. Remove the seat map and a ticketing platform still stands (general admission); remove the selling system and the seat map has nothing to allocate against |
| Event Registration Platform | adjacent sibling | registration centers the sign-up flow and the registrant roster; no seat-granular inventory |
| Attraction Ticketing / Attraction Management System | adjacent, structural | inventory unit is admission capacity to a place (day/time-slot tickets); no seat map as primary unit |
| Cinema Management System | adjacent vertical | every ticket is a seat there, but seat allocation lives inside the cinema system's own model of screens and screenings |
| Airline Reservation / Passenger Service System | adjacent, different domain | seat selection exists there, inside fare/inventory/departure-control machinery; not event admission |
| Venue Management System | adjacent | manages bookable spaces and their use; here the seat map is a selling asset, not a bookable space |
| Ticket Inventory Management | sibling slice | allocation/holds/on-sale discipline at ticket-type grain vs the seat-granular map machinery documented here |
| Ticket Resale Marketplace | sibling slice | seat-level resale appears here as a capability; the marketplace type centers the secondary market |
| Event-planner seating-chart tools | market adjacency (no directory leaf) | planner-side layout design for private events, with no selling or allocation to ticket buyers |

The boundary with the Event Ticketing Platform is the defining one: reserved seating is the seat-level inventory layer of ticketing, not a competing whole. The market expresses this structurally — the layer appears as a mode inside every ticketing platform that supports it, and the one dedicated seat-map product family supplies the layer to such platforms rather than replacing them.

## Representative Products

- **Seats.io** — the dedicated seat-map component: floor-plan designer, interactive renderer, and real-time seat-availability API for ticketing platforms
- **Eventbrite** — self-serve ticketing platform with reserved seating as a named selling mode (seating chart maker, shoppable venue maps)
- **TicketSpice** — self-serve ticketing platform with a dedicated reserved-seating feature (chart builder, pricing tiers, holds and pool holds, tables and pods)
- **Tessitura** — arts & culture platform: seat maps as building blocks, select-your-own-seat, seated subscriptions with seat rights
- **Paciolan** — college athletics / performing arts / arenas ticketing: interactive seat maps, seat-level pricing with repricing, season renewals

The defining structure was checked against paper-era box-office practice (printed house charts, seat-named tickets, paper season-seat records) to avoid over-fitting to the current interactive-map implementation.

## Sources

Research date: **2026-09-09**

Primary vendor surfaces:

- Seats.io — homepage, features page, and support centre articles (What is Seats.io?; How does it work?; What is an Event?; Season tickets and multi-day events): https://www.seats.io/ , https://www.seats.io/features , https://support.seats.io/en/articles/2007394-what-is-seats-io , https://support.seats.io/en/articles/2069669-how-does-it-work , https://support.seats.io/en/articles/2096454-what-is-an-event , https://support.seats.io/en/articles/2096431-season-tickets-and-multi-day-events
- Eventbrite — organizer feature page "Reserved Seating": https://www.eventbrite.com/organizer/features/reserved-seating/
- TicketSpice — reserved seating feature page: https://www.ticketspice.com/features/reserved-seating-event-ticketing-system
- Tessitura — Ticketing & Admissions feature page: https://www.tessitura.com/features/ticketing-admissions
- Paciolan — ticketing solutions page: https://www.paciolan.com/ticketing-solutions
- Spektrix — seating-plan and order evidence carried from the paired event-ticketing-platform research (2026-09-07, official support centre)

> Sourcing limitations: the seats.io documentation site is a JavaScript application and could not be fetched; its support-centre articles were used instead. Two self-serve candidates (a theater-focused product and SimpleTix) and one legacy seat-map vendor were unreachable (blocked or missing) and were dropped from the sample. Help-centre documentation for the arts and sports platforms is behind a login, so evidence for those two is product-page level; no operational specifics are asserted from them. Whether a second standalone seat-map component vendor exists could not be verified. Precise operational details (hold durations, chart-size limits, fee structures) are intentionally not stated in this document; such details remain in the Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
