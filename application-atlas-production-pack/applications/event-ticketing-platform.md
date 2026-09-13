# Event Ticketing Platform

## Overview

An **Event Ticketing Platform** is organizer-side software for selling admission to events: the organizer defines ticketed events with priced ticket inventory, the platform sells that inventory to the public, each completed sale issues tickets as checkable entitlements to attend, and the organizer manages the resulting sales — orders, refunds, entry, and reporting — in the same system.

The defining structure is small:

```text
Ticketed event (dated occurrence + ticket types with price and quantity)
└── Sale → recorded order
    └── Ticket issued as a distinct, checkable access artifact
        └── Organizer-side management of the sale lifecycle
            (on-sale control, orders, refunds, reporting, entry)
```

Everything commonly associated with modern ticketing — consumer marketplaces, seat maps, mobile-wallet tickets, scanning hardware, presales and queues, dynamic pricing, fan resale — is widespread in current products but is not part of the defining core. A box office selling paper tickets against an event allocation, with stubs taken at the door, satisfies the same structure without any of those specifics.

When the center of gravity shifts from selling tickets to collecting sign-ups into a roster, the product is drifting toward a different Application Type (Event Registration Platform); when it shifts to running the whole event lifecycle, toward an Event Management Platform; when the inventory unit becomes admission capacity to a place rather than dated occurrences, toward Attraction Ticketing.

## Users & Context

The primary user is the **event organizer** — the person or organization putting on the event and selling access to it:

- **promoter or event creator** — defines the event, sets up ticket types and prices, opens and monitors the on-sale
- **box-office or door staff** — sells at the venue, prints or scans tickets, handles walk-ups
- **event manager** — works orders and refunds, answers buyer questions, watches sales reports

Secondary concerns sit with the **ticket buyer**, who is the consumer-facing side: browsing the event page, selecting tickets, paying, receiving tickets, and presenting them at entry. The buyer surface can be the platform's own marketplace, the organizer's own website, or a box-office window — the Type works through all three.

Typical contexts: concerts and live music, performing arts and theater, festivals and fairs, nightlife, sports, community and charity events, conferences with paid admission. The work is deadline-shaped: an on-sale moment, a sales window, a door time.

## Core Model

### The Defining Core

Three structures. If any one is removed, the product is no longer recognizable as event ticketing:

- **The ticketed event as sellable inventory.** The organizer defines, inside the system, a dated event occurrence — or a set of occurrences (multi-day, recurring, timed entry) — carrying **ticket types**: admission options with a name, a price (which may be zero), and a quantity. The system tracks availability against sales. Without dated admission inventory, the product is generic e-commerce or a sign-up form.
- **The ticket as the sold access artifact.** Each completed order issues **tickets** — distinct, individually checkable entitlements to attend, delivered electronically or printed, carrying a scannable or otherwise verifiable identity. The ticket is the product being sold, not a receipt for a registration. Without the ticket artifact and its inventory semantics, the product is a registration platform.
- **Organizer-side management of the sale lifecycle.** The organizer controls the on-sale (publish, open and close sales, set capacity and pricing windows) and works the resulting sales in the same system — searching orders, issuing refunds and exchanges, reading reports. Without this, the product is a bare listing or checkout, not a ticketing platform.

Two deliberate exclusions keep the core honest:

- **Payment is not part of the core.** Free ticketed events are a standard mode (zero-priced ticket types), and deferred payment exists (reserve now, pay at the door). What defines the Type is the sale of a ticket artifact, which can be free or settled later.
- **Entry-validation machinery is not part of the core.** Scanning apps and hardware are the modern standard, but the checkable ticket predates them — a paper stub torn at the door is the same structure. The machinery is a standard capability, not the definition.

### Standard Capabilities

Mature products commonly carry most of the following. They are not what makes the product a ticketing platform, but they make ticketing practical:

- **Event page / listing** — the public sales surface: name, date and time, venue, description, imagery, and the ticket picker.
- **Ticket-type pricing machinery** — price tiers, early-bird windows, promo and discount codes, automatic or time-based price changes.
- **Capacity control** — caps at the event, section, or occurrence level; holds (blocks of inventory reserved from public sale); waitlists.
- **Payment processing** — integrated card processing, fee handling (buyer pays, organizer absorbs, or split), refunds.
- **Order management** — search and inspect orders, edit details, resend tickets, refund.
- **Ticket delivery** — electronic tickets in an app or wallet, print-at-home, will-call pickup at the box office.
- **Entry validation** — scan-based check-in (mobile apps or dedicated scanners), check-in time windows, scan history, fraud checks.
- **Door sales** — an on-site selling channel alongside online sales, including zero-value and complimentary tickets.
- **Sales reporting** — revenue, attendance, channel breakdown, real-time dashboards.
- **Buyer records** — order and attendee information, custom questions at checkout.
- **Multi-occurrence structures** — multi-date, recurring, and timed-entry events from one setup.
- **Team roles** — permissions over who can create events, manage tickets, and work orders.

### One Structure, Many Implementations

The core model is written in conceptual terms. The Variants section below enumerates how specific market poles realize each concept.

```text
Concept:          Ticketed event as inventory
Implementations:  single dated event, multi-date event, recurring schedule,
                  timed-entry slots, performance series

Concept:          Ticket as access artifact
Implementations:  QR/e-ticket in an app, mobile-wallet pass, print-at-home PDF,
                  thermal-printed stock, will-call pickup, paper stub

Concept:          Sales channel
Implementations:  platform marketplace, organizer's own website widget,
                  box-office counter, door/tablet sales, agents and resellers
```

A reader who only encounters one implementation (e.g., only marketplace-sold mobile tickets) should still be able to recognize a box-office-window ticketing operation from the core model.

## How It Works

### Set up the event and its ticket inventory

```text
Create the event (name, date/time, venue, description)
→ define ticket types (name, price, quantity; free/paid/donation where supported)
→ set sales windows, visibility, per-order limits, delivery methods
→ optionally add holds, sections, or a seat map
→ publish and open the on-sale
```

The ticket type is the unit of inventory: its quantity, sales window, and visibility rules determine what the public can buy and when. Changes to price or name typically apply to future sales only; a ticket type that has sold usually cannot be deleted, only retired.

### Sell and issue

```text
Buyer opens the event page (marketplace, organizer site, or box office)
→ selects ticket type and quantity (and seats, if reserved)
→ completes checkout (payment, or zero-value, or reservation for later payment)
→ order is recorded
→ tickets are issued and delivered (app, wallet, email PDF, print, will-call)
```

The order is the commercial record; the tickets are the access artifacts it issues. In box-office-oriented products the same loop is driven by staff: search the event, pick tickets, take payment (card, cash, or account terms), print tickets, and the order history accumulates sales, reservations, returns, and exchanges under one order number.

### Validate at entry

```text
Attendee arrives with a ticket (phone, printout, or paper)
→ staff scan or check the ticket's identity
→ the system marks it used (with scan history)
→ invalid or already-used tickets are flagged
```

Some products bound check-in to time windows, so a ticket is only valid during its assigned entry period. Door sales run through the same machinery: sell a ticket on the spot, issue it, and scan it.

### Work the sales

```text
Monitor sales in real time (revenue, attendance, channels)
→ search and inspect orders
→ refund or exchange as needed
→ adjust inventory (release holds, add capacity, change prices)
→ report after the event
```

### Core vs Common vs Optional

Capabilities fall into three tiers:

**Defining core** — without these, not event ticketing:

- ticketed event as sellable inventory (dated occurrence + ticket types with price and quantity)
- sale recorded as an order
- ticket issued as a distinct, checkable access artifact
- organizer-side management of the sale lifecycle

**Standard capabilities** — present in most mature products:

- event page, pricing machinery, capacity control with holds and waitlists
- integrated payments with fee handling and refunds
- order management, ticket delivery, entry validation, door sales
- reporting, buyer records, multi-occurrence structures, team roles

**Common variants / optional** — depends on segment, scale, or business model:

- consumer marketplace discovery vs own-channel distribution only
- reserved seating and seat maps vs general admission
- deep box-office operations (staffed counter selling, reservations and deposits, group bookings, ticket-printing hardware)
- subscription and pass products (fixed-series seat rights, season and flex passes, memberships)
- presales, on-sale queues, per-order ticket limits, anti-fraud controls
- fan-to-fan resale and transfer policies
- dynamic pricing; add-ons and merchandise; donations; virtual/live-stream tickets
- agent/reseller distribution with commission machinery

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Event setup / ticket configuration

The organizer's primary authoring surface.

- event details (name, dates, venue, description), ticket types with their settings, capacity and holds
- primary actions: create event, add/edit ticket types, set sales windows and visibility, publish

### Sales dashboard

The organizer's monitoring surface during the on-sale.

- real-time sales and attendance figures, channel breakdown, remaining inventory
- primary actions: inspect orders, refund, resend tickets, adjust inventory, message buyers

### Order detail

The record of one sale.

- buyer, items (tickets with event/date/seat where applicable), payments, fees, ticket delivery and print/scan state
- primary actions: refund, exchange, resend, edit details, view scan history

### Event page (buyer-facing)

The public sales surface.

- event information, ticket picker with prices and availability, checkout
- primary actions: select tickets, pay, receive tickets

### Box-office / door interface

The staffed selling and entry surface.

- event and occurrence search, quick sale, payment capture, ticket printing
- scanning view: scan tickets, validate attendees, handle exceptions (already used, wrong day), sell zero-value tickets at the door

### Reporting

- sales by ticket type, channel, and time; attendance; refunds; settlement summaries

## Important Rules / Behaviors

### The ticket type is governed inventory

A ticket type's quantity, sales window, and visibility rules determine what can be sold and when. In some products, hidden ticket types are revealed by promo codes, and sales windows can chain to other ticket types (early bird ends when the next tier opens). Holds remove inventory from public sale without deleting it.

### Sold inventory is durable

A ticket type that has had sales typically cannot be deleted — it can be edited for future sales or retired. This protects the integrity of the order and attendance record.

### The ticket is distinct from the receipt

The order confirmation proves the purchase; the ticket proves the right to attend. Mature products keep them separate: a buyer can hold a valid ticket without a paid order (free and comp tickets) and an order without tickets (registration-style events in products that support both modes). The ticket carries the checkable identity that entry validation consumes.

### Refunds and exchanges are organizer-side operations

Whether and how buyers can get refunds is governed by the organizer's policy; the mechanics (refund to original payment, to account credit, or exchange to another occurrence) are executed in the platform, and the returned tickets return to inventory or are voided.

### Transfer and resale are policy surfaces

Whether a ticket can be transferred to another person, resold, or resold only at face value is a per-event policy in mature products, with enforcement at the artifact level (transferable barcodes, locked tickets, restricted resale channels).

### Entry validation is stateful

A scanned ticket is marked used; re-presentation is flagged. Scan history is retained and visible on the order. Check-in windows bound when a ticket is valid.

## Variants

The Type is realized in distinct market poles. Common variants:

- **self-serve with consumer marketplace** — organizers publish into a discovery marketplace that also sells their tickets; distribution and demand generation are bundled (e.g., Eventbrite)
- **self-serve, own-channel only** — organizers sell through their own pages and widgets; no consumer marketplace (e.g., Purplepass)
- **box-office / arts platform** — deep staffed-selling machinery: counter and phone channels, reservations with deposits, group bookings, ticket printers and scanners, subscriptions and fixed-series seat rights, memberships and donations (e.g., Spektrix)
- **dominant large-scale primary ticketing** — presales with signups and queues, per-order ticket limits, mobile-wallet entry, official resale exchanges, league/tour-scale operations (e.g., Ticketmaster)
- **segment flavors** — festivals (multi-day, wristband handoffs), performing arts (series and subscriptions), nightlife and clubs (door-heavy), fairs and fairs-seasonal, sports (season tickets)

A variant should remain a **Variant**, not become a separate Type, unless it changes the core objects, workflow, or rules so much that the defining core no longer applies. Reserved seating, ticket-inventory allocation discipline, and secondary-market resale each move the center of gravity enough that the directory holds separate leaves for them — see Related Application Types.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Event Registration Platform | closest sibling — ratified seam | registration centers the sign-up flow and its output, the registrant record/roster; ticketing centers sellable ticket inventory and issues the ticket as the sold artifact. In registration products a ticket (if present) is a receipt; in ticketing products the ticket is the product. Products can support both modes side by side |
| Event Management Platform | broader | centers the whole event lifecycle (setup → publish/promote → register → manage → run → closeout) with ticketing as one capability |
| Attraction Ticketing / Attraction Management System | adjacent, sharpest structural boundary | inventory unit is admission capacity to a place (day/time-slot tickets, no seat map as primary unit); here it is dated performances/occurrences, often seat-mapped |
| Attendee Management | adjacent | centers the roster and presence recording; the person record is a byproduct of the ticket sale here |
| Reserved Seating Platform | sibling, unprocessed | candidate split: the seat map as the primary managed object vs the ticketed event with seat maps as one capability mode |
| Ticket Inventory Management | sibling, unprocessed | candidate split: the allocation/holds/on-sale discipline as the center vs the full sell → issue → validate loop |
| Ticket Resale Marketplace | sibling, unprocessed | candidate split: the secondary market (fans reselling) vs the primary sale; resale appears inside this Type as a capability |
| Convention / Exhibition Management | adjacent | monetizes participation (exhibitors pay for space/services); this Type monetizes admission (attendees pay for access) |
| Cashless Venue Platform | adjacent | sells admission entitlements vs stored-value spending accounts and on-site payments; festivals bundle both |
| E-commerce Platform | adjacent | sells undated products with shipping vs dated admission inventory issuing access entitlements validated at entry |
| Airline Reservation / Passenger Service System | adjacent | sells numbered seats with inventory controls, but ticketing has no fare-rule repricing, interline, or day-of-travel document/bag process |
| Restaurant Reservation Platform | adjacent | books a table/cover at a hospitality time slot vs selling admission to a dated event |
| Event Agenda Management | adjacent | centers the program-of-record (sessions/schedule); lineup fields on ticketed event pages are descriptive content, not a program |
| Event Credential / Badge Management | adjacent | ticket = paid admission entitlement (transaction object); credential = persistent on-site identity and category privileges; tickets commonly become badges at the door |

The boundary with the Event Registration Platform is the most important one, because the two Types overlap on checkout flows, capacity, and confirmations. The structural difference is what the sale produces: a sold, checkable ticket backed by inventory semantics, or a registrant record feeding a roster.

## Representative Products

- Eventbrite — self-serve organizer ticketing with a consumer discovery marketplace
- Purplepass — self-serve ticketing with own-channel distribution
- Spektrix — arts & culture box-office ticketing platform
- Ticketmaster — large-scale primary ticketing with an official resale marketplace

The defining core was checked against box-office-era and paper-ticket practice (window sales, stubbed paper tickets) to avoid over-fitting to the current mobile-marketplace implementation.

## Sources

Research date: **2026-09-07**

Primary vendor surfaces:

- Eventbrite — Help Center (Creating an event; Create and edit ticket types; registration-only mode): https://www.eventbrite.com/help/en-us/topics/creating-an-event/ , https://www.eventbrite.com/help/en-us/articles/644100/how-to-create-custom-ticket-types/ , https://www.eventbrite.com/help/en-us/articles/250995/how-to-set-up-an-event-that-doesn-t-require-tickets-registration-only/ ; organizer product and pricing pages: https://www.eventbrite.com/organizer/overview/ , https://www.eventbrite.com/organizer/features/sell-tickets/ , https://www.eventbrite.com/organizer/features/organizer-check-in-app/ , https://www.eventbrite.com/organizer/pricing/
- Purplepass — features and help center: https://www.purplepass.com/learn/ , https://www.purplepass.com/learn/event-types/ , https://www.purplepass.com/learn/ticket-types/ , https://help.purplepass.com/hc/en-us/categories/21570562726807-Event-Organizer
- Spektrix — Support Centre (Events and Instances; Orders and Transactions; hardware and scanning): https://support.spektrix.com/hc/en-gb , https://support.spektrix.com/hc/en-us/articles/11012056320541-Introduction-to-Events-and-Instances , https://support.spektrix.com/hc/en-us/articles/360018263917-Introduction-to-Orders-and-Transactions
- Ticketmaster — main site and fan help center: https://www.ticketmaster.com/ , https://help.ticketmaster.com/hc/en-us

> Sourcing limitations: two candidate samples (a flat-fee self-serve product and a full-service agency product) were unreachable (blocked after repeated attempts) and were replaced in the sample; their poles are covered structurally by the sampled products. One sampled product's organizer-side tooling is not publicly documented — its evidence is consumer-side only, and no organizer-side claims about it are made. Precise operational details (fee percentages, exact state names, numeric limits, queue mechanics) are intentionally not stated in this document; such details remain in the Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
