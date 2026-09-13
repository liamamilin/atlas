# Ticket Inventory Management

## Overview

A **Ticket Inventory Management** application governs the stock of admission rights for ticketed events: how many tickets exist for each occurrence and each ticket class, which portions are held back from general sale, when and through which channels each portion may be sold, and how remaining availability is reconciled as sales, pending orders, releases and refunds occur.

It is the control layer that sits over the stock being sold. The selling machinery itself — checkout, payment, ticket issuance, entry scanning — belongs to event ticketing; this layer decides, at any moment, how much stock exists, who may buy which portion of it, and what has actually happened to it. Tickets make this stock unusual: it is bounded by the venue's capacity, divided into classes, perishable (unsold stock expires with the occurrence and cannot be replenished), and its "units" are admission rights rather than physical goods.

The defining core is small:

```text
Admission stock (bounded, class-divided, perishable)
└── Controlled tranches (holds / gated classes with who-when-where rules)
    └── Live reconciliation (availability tracks sales, pending orders, releases)
```

Everything else commonly associated with the discipline — on-sale windows, access codes, channel restrictions, presale ladders, holds reporting, dynamic pricing — is standard machinery that mature products add, not what makes the layer what it is. A paper-era box office with numbered ticket blocks, outlet allotments, will-call holds and a reconciliation ledger satisfies the same core.

## Users & Context

Primary users are the people accountable for an event's stock:

- **Box office / ticketing operations** — create the stock for each occurrence, set holds and gated classes, open and close sales, reconcile counts during the sell period and at the door.
- **Event organizers and promoters** — plan how stock is divided: what goes on public sale, what is reserved for presales, partners, staff, artists and guests, and when each portion is released.
- **Group sales and partnership staff** — manage blocks of stock tied to group bookings, deposits or promotional partners.

Secondary users:

- **Venue and marketing staff** — adjust capacity, schedule on-sale moments, and run presale ladders tied to membership or fan segments.
- **Reseller and rightsholder operations** (an adjacent market reading of the same discipline) — manage stock they have acquired, distributed across resale marketplaces.

The work context is dominated by the sell period: the on-sale moment, the presale ladder, the slow-burn weeks before an event, and the final days when remaining stock is released, discounted, or written off. Decisions are made under scarcity — every ticket held back is a ticket not publicly sellable, and every release changes what buyers can see.

## Core Model

### The Defining Core

**1. The admission stock.** For each occurrence (a dated performance, session, or timed entry block) the system holds a bounded quantity of admission rights, divided into ticket classes — types, price bands, zones, or seats. Two bounds work together: each class carries its own quantity, and an overall capacity ceiling caps the total. The stock is perishable: when the occurrence ends, whatever remains is worthless and cannot be restocked.

**2. Controlled tranches.** Stock is partitioned into named, controlled portions that are removed from general sale or restricted in who can buy them. A tranche carries eligibility rules along three axes:

- **who** — a sales channel (online, box office, at the door), an access code, a customer segment (members, donors, subscribers), or a partner;
- **when** — on-sale windows (start and end dates per class, presale ladders, scheduled releases);
- **how many** — the tranche's quantity, or specific seats where a seat map exists.

Releasing a tranche — deleting a hold, lifting a lock, opening a window — returns its stock to general availability. This partition is what distinguishes inventory management from plain selling: without it, there is only one undifferentiated pile of tickets sold first-come.

**3. Live reconciliation.** As orders complete, orders pend, holds are released and settings change, remaining availability per class updates against the ceiling in real time, and the operator can see and steer it: sold-out diagnostics that explain *why* something shows as sold out (holds, per-class quantities, capacity, or per-order minimums), summaries of held stock, and direct steering actions (increase or reduce quantities, change capacity, extend or end sales). Without this, the partition is just an allocation plan nobody reconciles.

### Standard Capabilities

Mature products commonly add:

- **Scheduled on-sale windows** per ticket class, including scheduled publishing of an event's sale.
- **Code-gated inventory** — hidden ticket classes unlocked by access or promo codes, optionally carrying discounts, per-code quantity limits and their own validity windows.
- **Per-channel sales restriction** — a class sold online only, at the door only, or everywhere.
- **Per-order minimums and maximums** as stock-shaping rules (a class can appear sold out when remaining stock is below the order minimum).
- **Holds reporting** — summaries of what is held, where, and for whom.
- **Scaling actions** — raising or lowering class quantities, changing capacity, reopening ended sales.
- **Multi-occurrence views** — stock across dates, series, and recurring or timed-entry occurrences.
- **Seat-grain holds** where a seat map exists — the same tranche logic applied to specific seats and sections.
- **Sales reporting** by class, channel, and occurrence.

### One Structure, Many Implementations

The core is written conceptually; products realize each concept differently:

```text
Concept:            Ticket class (the stock's division)
Implementations:    ticket types, price bands, zones, seats, timed-entry blocks

Concept:            Controlled tranche
Implementations:    named holds (quantity or seat-based), locks, hidden classes
                    + access codes, channel-bound classes, presale segments

Concept:            Stock bounds
Implementations:    per-class quantity + total capacity; per-occurrence capacity
                    vs tickets actually made available for sale

Concept:            Reconciliation
Implementations:    sold-out diagnostics, pending-order return timers,
                    holds summaries, scheduled seat releases
```

A reader who has only seen one implementation — say, quantity-based holds on a general-admission event — should still recognize seat-based locks, channel-bound classes, and presale segments as the same discipline.

## How It Works

### The primary-market loop

**1. Create the stock.** For an occurrence, the operator defines ticket classes and their quantities under a capacity ceiling. The ceiling and the class quantities are distinct controls: raising a class's quantity cannot sell past the ceiling, and raising the ceiling reopens sales. Some products let an unfilled class quantity flow into the general pool up to the ceiling.

**2. Partition it.** The operator carves out controlled tranches: named holds (a quantity for general-admission stock, or specific seats and sections where a seat map exists), hidden classes gated behind access codes, classes bound to a single channel, or segments reserved for presales. Held stock is invisible or unpurchasable to general buyers.

**3. Open the sale.** On-sale windows are set per class — a presale opens first, the general sale follows, sales end on a scheduled date. A held tranche is opened to its intended audience through its access code, channel, or segment eligibility.

**4. Sell and decrement.** Completed sales consume stock from their class. Incomplete (pending) orders temporarily remove stock; if the buyer does not complete in time, the stock is automatically returned to availability. Availability is computed across all of it — held stock, class quantities, the ceiling, order minimums — which is why an event can show "sold out" while stock technically exists in holds.

**5. Steer.** Throughout the sell period the operator adjusts: releasing holds to the public, transferring stock between holds, raising quantities, changing capacity, extending or ending sales, hiding or revealing classes.

**6. Reconcile and close.** Final counts reconcile sold, held, returned and unsold stock per class and channel; unsold stock expires with the occurrence. Where subscriptions or seat rights exist, unrenewed seats can be released back to the pool on a schedule.

### The resale-pole loop (adjacent reading)

On the reseller/rightsholder side, the same discipline runs over *acquired* stock: listings are synced or uploaded from point-of-sale systems (with event and barcode data), distributed across marketplaces with prices and statuses kept in sync, and every sale is carried through fulfillment, transfer, payment and reconciliation. The stock is owned rather than created, and the "channels" are marketplaces rather than an event's own sale surfaces — but the underlying structure (bounded stock, controlled distribution, live reconciliation) is the same discipline applied to a different position in the market.

## Interfaces

### Stock setup surface

Where the stock is created and bounded.

- ticket classes with prices and quantities; the capacity ceiling
- primary actions: create/edit classes, set quantities, set capacity

### Holds / allocation board

Where stock is partitioned into controlled tranches.

- named holds with quantities (or assigned seats/sections on a seat map), gated classes, channel settings
- primary actions: add/edit/delete holds, assign or move seats, create access codes, transfer stock between holds

### Availability & sales status view

Where the operator sees what is happening to the stock.

- per-class and per-occurrence availability, sold/pending/held counts, sold-out and unavailable states with their causes
- primary actions: diagnose availability, adjust quantities or capacity, change sales status

### Access-code / gating manager

Where gated inventory is controlled.

- codes with optional discounts, quantity limits, validity windows, and the classes they unlock
- primary actions: create/edit/delete codes, share code links

### Reconciliation & reporting

Where the stock's story is told.

- holds summaries, sales by class/channel/occurrence, final reconciliation
- primary actions: export summaries, run reports

## Important Rules / Behaviors

- **Availability is computed, not counted.** Whether buyers see "on sale", "sold out" or "unavailable" is decided jointly by held stock, per-class quantities, the capacity ceiling, per-order minimums, sales windows, and channel settings. Held stock alone can make an event display as sold out.
- **Held stock is invisible to general buyers** until it is released or its gate (code, channel, segment) admits them. Releasing a hold returns its stock to public sale immediately.
- **Pending orders temporarily consume stock** and return it automatically if uncompleted within the order time limit — availability dips and recovers without operator action.
- **The stock is perishable.** Unsold stock has no value after the occurrence; there is no replenishment, only re-partitioning of what exists.
- **Capacity is a ceiling, not a sum.** Class quantities can be raised, but sales stop at the ceiling; the ceiling can be raised to reopen sales.
- **Channel rules bind stock to surfaces.** A class restricted to the door cannot be bought online, and vice versa — the same stock behaves differently per surface.
- **Releases are deliberate.** Whether a hold is deleted, a window opens, or unrenewed seats are auto-released on a schedule, stock re-enters general sale only through an explicit mechanism — never by accident of time alone (except the pending-order return).

## Variants

- **Self-serve organizer pole** — quantity-based holds, access codes, per-class windows and channel settings; the discipline in its most accessible form (e.g. Eventbrite, Purplepass).
- **Enterprise arts/venue pole** — locks and overlays over seat plans, channel-bound classes, box-office-only performances, presale segments for members and donors, scheduled release of unrenewed subscription seats (e.g. Spektrix, Tessitura).
- **Attractions / timed-entry pole** — capacity managed per time block and entry point rather than per performance.
- **Box-office-heavy pole** — counter, phone and door channels as first-class stock surfaces with comp and VIP classes.
- **Resale/rightsholder pole** — acquired stock managed across marketplaces with dynamic pricing, automated transfers and settlement (e.g. Victory Live One's ticketing inventory management).
- **Grain variants** — quantity-grain (general admission), seat-grain (reserved), zone-grain; all observed, none definitional.
- **Presale ladders and partner allocations** — fan-club/member/donor presales, group blocks with deposits, consignment arrangements; depth varies widely by segment.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Event Ticketing Platform | owns the sell loop — orders, payment, ticket issuance, entry validation — with the event as sellable inventory; this Type is the control discipline over that inventory (holds, gating, windows, reconciliation), usually realized inside a ticketing platform |
| Reserved Seating Platform | centers the seat-granular map and seat-level allocation; this Type centers the class/quantity grain, with seat-grain holds as one variant |
| Ticket Resale Marketplace | the consumer-facing venue where resold tickets are exchanged; the resale inventory pole documented here is the seller-side stock machinery feeding such marketplaces |
| Event Management Platform | centers the event lifecycle and registration records; inventory partitioning appears there only as shallow ticket-type quantity settings |
| Inventory Management System (operations) | manages persistent, replenishable physical goods; ticket stock is perishable, capacity-bounded, and made of admission rights — shared vocabulary, different object world |
| Attraction Ticketing | place-admission inventory (open or timed entry to a venue) rather than occurrence inventory; timed-entry capacity blocks border it |
| Venue Management System | manages spaces, bookings and venue operations; this Type manages the admission stock of occurrences in those spaces |
| Retail POS | transaction-first selling of physical goods; no capacity-bounded perishable stock discipline |

## Representative Products

- **Eventbrite** — self-serve primary ticketing; holds, access codes, per-class windows and channel settings documented in its help center.
- **Spektrix** — enterprise arts/venue ticketing; locks ("holds or kills"), capacity-vs-on-sale controls, channel-bound ticket classes.
- **Purplepass** — self-serve box-office ticketing; venue capacity and per-class quantity model.
- **Tessitura** — enterprise arts/museums/attractions suite; presale segments, exclusive inventory, scheduled seat release (feature-page evidence).
- **Victory Live (Victory Live One)** — the resale/rightsholder pole; a product line literally named "Ticketing Inventory Management System" over acquired stock across marketplaces.

The core was checked against the paper-era box office (numbered stock, outlet allotments, will-call holds, reconciliation ledger) to avoid over-fitting the definition to modern self-serve machinery.

## Sources

Research date: **2026-09-09**

- Eventbrite Help Center — "Create and manage holds"; "What to do when tickets aren't on sale"; "Creating an event" topic index — https://www.eventbrite.com/help/en-us/articles/779653/how-to-create-and-manage-holds/ , https://www.eventbrite.com/help/en-us/articles/434070/what-to-do-when-tickets-arent-on-sale/ , https://www.eventbrite.com/help/en-us/topics/creating-an-event/
- Spektrix Support Centre — "Introduction to Events and Instances" — https://support.spektrix.com/hc/en-us/articles/11012056320541
- Purplepass Help Center — "Setting venue capacity for your event"; Event Organizer category; Ticket Creation & Management section — https://help.purplepass.com/hc/en-us/articles/22027576296727-Setting-venue-capacity-for-your-event , https://help.purplepass.com/hc/en-us/categories/21570562726807-Event-Organizer
- Tessitura — "Ticketing & Admissions" feature page — https://www.tessitura.com/features/ticketing-admissions
- Victory Live — "Ticketing Inventory Management System" product page; corporate home — https://www.victorylive.com/products/inventory-management/ , https://www.victorylive.com/

> Sourcing limitations: Tessitura's operational documentation is gated, and Victory Live's evidence is product-page level — claims about both are held to feature-page strength. Large-scale promoter-side allocation tooling (e.g. Ticketmaster's organizer systems) is not publicly documented, so partner-allocation practices are described only in general terms. Spektrix's primary help domain was unreachable; its support-centre domain was used instead. Detailed evidence, per-product observations, and the cross-product comparison are recorded in the paired Research Notes.
