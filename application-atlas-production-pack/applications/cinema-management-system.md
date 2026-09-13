# Cinema Management System

## Overview

A **Cinema Management System** is the business system of record for a movie-theatre operator. Its center is the **session** — a film placed in one of the operator's own auditoriums at a date and time. The operator composes a rolling programme of sessions, sells admission to them from the box office and from self-service channels, sells concessions on the same operational spine, and settles the box office with film distributors.

The defining core is small:

```text
Film record (title, runtime, rating, distributor, promotional media)
        +
Auditorium / screen estate (the operator's own screens, with capacity and seat layouts)
        ↓ placed into
Session (film × auditorium × date/time — the scheduled screening)
        ↓ published to
Session-bound admission selling (box office, web, mobile, kiosk, call centre)
```

Everything else commonly associated with running a cinema — concession stands and recipes, loyalty programs, kiosks and mobile apps, head-office circuit control, digital signage, staff time clocks — is standard mature capability built around that spine, not what makes the system a cinema management system. A single-screen cinema that keeps its weekly programme, sells paper tickets at one till, and settles a rental percentage with the distributor each week satisfies the same core without any of the modern machinery.

Two naming cautions. First, in cinema-industry jargon a "Theatre Management System" (TMS) is a different product entirely: the projection-side system that controls digital cinema servers and automates playback from the schedule. This document covers the business system, not the TMS. Second, "cinema ticketing software" names the selling surface of this estate; the selling surface is one ring around the session spine, not the whole.

## Users & Context

The users are the cinema operator's own staff, in layers:

- **film programmer / booker** — decides which films play and composes the session schedule, commonly weeks ahead; in chains this role sits at head office and site managers adapt the plan locally
- **cinema / site manager** — runs one site: adjusts the schedule, sets session pricing, manages stock, cash, and staff, watches the day's performance
- **box-office cashier** — sells tickets (and often concessions) at the counter, applies comps and discounts, handles exchanges and refunds
- **concession staff** — sells food and drink, prepares and routes orders
- **ushers / floor staff** — checks tickets at the auditorium door, delivers food to seats where offered

Secondary users sit outside the site: **head-office staff** for chains (circuit-wide configuration, cross-site reporting, distributor settlement), **marketing staff** (loyalty, promotions, showtime distribution to listing services), and the **film distributor** as the external counterparty the system computes payments toward. The **moviegoer** is the buyer-facing side: browsing showtimes, picking seats, paying, receiving a ticket, and having it checked at the door.

The work environment is a live venue running a continuous programme: sessions sell across online and on-site channels while earlier sessions are playing, the schedule changes propagate to every channel in near real time, and each day closes with cash reconciliation and reporting.

## Core Model

### The Defining Core

Three structures, held together. Remove any one and the product stops being a cinema management system:

- **The session as the operational unit of record.** A session is a scheduled screening: one film, in one auditorium, at one date and time. It is the object the entire system hangs off — ticket inventory, pricing, seating, signage, staff apps, and the projection layer all read from it. Sessions are composed ahead of time (typically by placing films from a film list into auditorium time slots, by drag-and-drop or by copying days and weeks), and they become visible and buyable when published. Until then the schedule is a working plan, not yet on sale.
- **The two reference estates.** (a) **Films** are held as content records — title, runtime, rating, synopsis, poster and trailer media, and the distributor the film is hired from — created once and reused across many sessions, screens, and channels. The runtime shapes how sessions fit together; the rating gates age-checked ticket sales; the media feeds websites, apps, and signage. (b) **The auditorium/screen estate** is the operator's own set of screens, each with its capacity and seat layout. Sessions are placed into these screens; the same screen hosts different films across the day and the week.
- **Session-bound admission selling.** Tickets are sold against sessions — at the staffed box office and through web, mobile, kiosk, and call-centre channels — with prices configured at session level. Every completed sale is a recorded transaction that attributes the admission to its film, session, and screen; that attribution is what later feeds distributor settlement.

### Standard Capabilities Around the Core

Mature products commonly carry most of the following. They make the system practical; they are not what defines it:

- **Concessions as the integrated second revenue line.** Concession items, combos and meals, recipes, and inventory that depletes with every sale, sold from the same point of sale as tickets — with upsell prompts, order routing to preparation stations, and, in dine-in cinemas, table service with tabs and kitchen displays.
- **Distributor settlement (film hire).** The exhibitor's contracted payment to film distributors, computed from ticket sales per film and site under contracted terms (share formulas, minimum amounts, deductible house costs), producing settlement records and reports to distributors.
- **Ticket-type and pricing machinery.** Ticket types (adult, child, student, senior), price cards or pricing rules attached to sessions, promotions and discounts, surcharges for new releases or premium formats, booking and ticket fees.
- **Multi-channel selling on one inventory.** Box office, website, mobile app, kiosk, and call centre all selling the same sessions, with availability updating across channels in real time.
- **Reserved and unallocated seating as per-session modes.** A seat map per auditorium with per-session seat states when reserved seating is on; plain capacity counting when it is off. The two modes coexist across sessions, markets, and products.
- **Admission validation.** Staff scanning apps and, in some products, moviegoer self-scanning; the ticket's current state is honored at the auditorium door.
- **Loyalty, vouchers, and gift cards** (subscriptions in some products), redeemable across all channels.
- **Reporting and dashboards** — sales by film, session, screen, and day; concession performance; labor; advance sales.
- **Head-office / circuit management** for chains — centralized configuration, bulk updates across sites, cross-site reporting, and settlement consolidation.
- **Outward schedule distribution** — digital signage and marquees, the cinema's own website, third-party listing and internet-ticketing services, and the projection-side TMS.

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:   Session (scheduled screening)
Implementations:  "session", "showtime", "performance", "screening"

Concept:   Film record
Implementations:  in-system film databases; studio-official data feeds imported into the system

Concept:   Session pricing
Implementations:  price cards assigned per session; pricing rules applied per session; per-performance ticket rules

Concept:   Distributor settlement
Implementations:  "film hire" contracts and calculations; automated film settlement with distributor reporting; rental recorded per film
```

## How It Works

### Programme the schedule (the weekly loop)

```text
Select films (from the system's film database or an imported studio data feed)
→ place sessions into auditorium time slots (drag-and-drop; copy days/weeks)
→ set per-session configuration: price card, seating mode (reserved/unallocated),
   channel availability, trailer and cleanup time, private flag
→ publish the schedule
→ sessions appear on every channel: box office, web, app, kiosk, signage,
   listing services, and the projection system's playlist
```

Programming and site operation are distinct layers in chain deployments: programmers plan centrally, site managers adapt and approve locally. A schedule change — adding a session to a selling-out film, swapping screens — propagates to all channels in near real time.

### Sell a ticket (the transaction loop)

```text
Pick a session (at the counter, kiosk, web, app, or call centre)
→ choose ticket types (and seats, when the session runs reserved seating)
→ apply deals, vouchers, or loyalty
→ take payment
→ issue the ticket (printed, digital, or self-updating)
→ check it at the auditorium door
```

The same selling screen commonly also sells concessions, so one transaction can carry tickets and popcorn; age-restricted tickets are checked against the film's rating at the point of sale.

### Sell concessions (the second revenue loop)

```text
Ring items / combos on the POS (or receive a kiosk/app order)
→ route preparation orders to the right station
→ inventory depletes with the sale (recipes track ingredients)
→ redeem online-purchased concessions at the counter
```

### Settle with distributors (the money loop)

```text
Box office data consolidates (per site, rolled to head office in chains)
→ film hire calculated per film and site under contracted terms
   (share formulas, minimums, house-cost deductions)
→ settlement records generated and exported to financial reporting
→ reports and payments to distributors
```

### Run the day

Close-of-day functions reconcile cash per till and per shift, produce the day's sales and inventory reports, and feed labor and performance dashboards. Punch-clock or time-and-attendance functions track staff hours from the same estate.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Film programming / scheduler

The programmer's surface for composing the programme.

- auditorium time-slot grid or calendar; film palette / database with runtime, rating, and media
- primary actions: create, move, copy, and edit sessions; set per-session pricing, seating mode, and channel availability; publish

### Session / showtime manager

The per-session configuration and monitoring surface.

- session list or grid with sell-through and seat availability
- primary actions: apply pricing rules and purchase rules, adjust ticket-type availability, monitor sales

### Box-office point of sale

The staffed selling surface, built for speed at peak times.

- session lookup, ticket-type and seat selection, concession items and combos, payment in multiple forms
- primary actions: sell, comp, discount, exchange, refund, verify age, open tabs (dine-in)

### Concession / F&B surface

The food-and-drink selling and fulfillment surface.

- item and combo buttons, modifier entry, order routing to prep stations or kitchen displays
- primary actions: sell, route, comp or discount items, track restricted items

### Back office / manager surface

The site manager's daily workspace.

- close-of-day and cash management, stock and inventory, staff time records, day's reports
- primary actions: reconcile, count stock, adjust prices and items, run reports

### Head-office / circuit console (chains)

The circuit-wide control surface.

- cross-site configuration and bulk updates, consolidated sales and settlement reporting, film-hire contracts
- primary actions: push settings, compare sites, run settlement

### Buyer channels

Web, mobile app, kiosk, and call centre — browsing showtimes, selecting seats, paying, receiving tickets, managing bookings.

### Validation surface

Handheld or fixed scanning at the auditorium door; some products let moviegoers self-scan.

### Reporting / dashboard

Real-time and periodic views: sales by film, session, screen, and day; concession and inventory performance; labor; advance sales.

## Important Rules / Behaviors

### Nothing sells before the session exists and is published

The session is the gate for all selling. Sessions composed ahead of time are not buyable until published; publishing makes them visible across every channel at once. Schedule changes propagate in near real time, and cancellation or removal pulls the session out of the selling channels.

### Pricing attaches to sessions

Ticket prices are configured at session level — through price cards or pricing rules assigned to the session — so the same film can carry different prices by time, day, format, or release window. New-release periods and premium formats commonly carry surcharges.

### Seating mode is a per-session choice

The same auditorium can run reserved sessions (seat map, per-session seat states, seat-first selling) and unallocated sessions (capacity counting). When reserved, one seat is held or sold to one buyer per session; broken seats can be marked out and seat history is inspectable from the selling screen.

### The film's rating gates the sale

The rating held on the film record surfaces at the point of sale for age-checked tickets — the content record and the transaction are linked, not separate worlds.

### Every ticket attributes its sale

A ticket sale carries its film, session, and screen identity. That attribution is what makes distributor settlement computable per film and per week — and what makes combined programmes (double features, marathons) settle correctly when several films share one ticketed session.

### Comps, discounts, and refunds are operator actions under control

Complimentary tickets, discounts, and post-sale refunds are staff actions that mature systems gate by role and record in reporting, because each one changes both revenue and the settlement base.

### The schedule is distributed, not just stored

The published schedule feeds outward: signage and marquees, the cinema's website, third-party listing and internet-ticketing services, and the projection-side system that assembles each screen's playlist. The business schedule is the upstream source for the projection layer.

## Variants

- **Single site vs circuit.** Independents run the site back office; chains add the head-office layer (central configuration, cross-site reporting, consolidated settlement).
- **Reserved-seating-first vs unallocated-first markets.** Regional market practice differs; products support both as per-session modes.
- **Deployment.** On-premise suites with vendor hardware; cloud SaaS aimed at independents; hybrid lines from the same vendor.
- **Dine-in and expanded F&B.** Cinemas with restaurant-level service run tabs, table management, and kitchen routing inside (or alongside) the cinema system.
- **Drive-ins.** The same spine with per-car admission.
- **Festivals and repertory.** Dense short-run programming, marathons and double features ticketed as single sessions, private showings.
- **Alternative content.** Live broadcasts and special events scheduled and sold through the same session spine.
- **Engagement depth.** Loyalty and gift cards as the baseline; subscriptions, moviegoer CRM, and AI-assisted forecasting/scheduling as the advanced tier.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Event Ticketing Platform | adjacent | both sell dated admission; ticketing centers organizer-defined one-off events and the sell→issue→validate loop, while the cinema system centers the operator's own continuously recomposed session programme with film, concession, and settlement context. Remove the programme spine and the remainder is event ticketing |
| Reserved Seating Platform | layer relationship | the seat-map layer exists inside the cinema system's own model of auditoriums and sessions (per-session seat states, seat-first selling); in cinema it is a mode, not a standalone product |
| Attraction Ticketing | adjacent | sells operator-defined admission products (day/time-slot tickets) to a place with entry validation as the attendance record; no film programme, no session spine, no distributor settlement |
| Cinema Scheduling Application | sibling slice | the film-programming/scheduling function as a standalone focus; inside this system it is the spine module (the scheduler surface) |
| Theatre Management System (TMS) / Circuit Management System | adjacent, different family | the projection-side system controlling digital cinema servers, playlists, and content delivery; it consumes the business schedule ("the film schedule drives the operation of the cinema") but has no selling, concessions, or settlement. A distinct application type despite the overlapping "theatre management" naming |
| Restaurant POS / Kitchen Display System | adjacent module boundary | generic F&B transaction semantics; the cinema system's concession module is session-bound and cinema-shaped; dine-in cinemas may pair the cinema system with an external F&B platform while keeping box office, seating, and scheduling in the cinema system |
| Venue Management System | adjacent | manages bookable spaces and their use by hirers; the cinema system runs the operator's own public programme. Private screenings and group sales are a variant inside the session spine, not space booking |
| Broadcast Management System | adjacent, different domain | schedules content for transmission to an undifferentiated audience; the cinema system schedules individually ticketed admission in seated auditoriums |
| Film Distribution Management | opposite side of the same money flow | the distributor-side system for releases, contracts, and box-office reporting; the cinema system's film-hire module is the exhibitor-side mirror |

The boundary with the Event Ticketing Platform is the most important one, because both sell dated admission with ticket types. The structural difference is whether the system's center is the organizer's one-off event or the exhibitor's continuously recomposed programme of sessions in its own auditoriums — with the film record, concessions, and distributor settlement carried as first-class context.

## Representative Products

- **Vista (Vista Classic / Vista Cloud)** — the global enterprise suite for chains: Head Office, Film Manager, Showtime Manager, POS, digital channels, film-hire settlement, BI
- **Omniterm** — North American cinema software since 1978: POS-centric integrated system with theatre management, automated film settlement, and ticketing control
- **RTS (Ready Theater Systems)** — US all-included package for independents, chains, drive-ins, and dine-in cinemas: box office, reserved seating, film & schedule management, concessions and F&B
- **Veezi (by Vista)** — cloud SaaS for independent cinemas: film programming, price cards, concessions, internet ticketing, dashboards

The defining core was checked against paper-era practice (weekly programme, one screen, box-office till, weekly distributor rental settlement) and against drive-in and single-screen variants, to avoid over-fitting the definition to the current multi-channel stack.

## Sources

Research date: **2026-09-10**

Primary vendor surfaces:

- Vista — Vista Classic product page: https://vista.co/vista-classic ; Help Centre: https://help.vista.co/hc/en-nz (Films section, Ticketing section; articles "Creating and publishing draft sessions in film manager", "Ticketing overview", "Calculating film hire")
- Omniterm — Cinema Management Software: https://omniterm.com/ ; Theatre Management: https://omniterm.com/theatre-management/ ; Cinema POS: https://omniterm.com/cinema-pos/
- RTS — Cinema Point of Sale: https://www.rts-solutions.com/point-of-sale-1 ; Operations: https://www.rts-solutions.com/operations-1
- Veezi — home and feature pages: https://veezi.com/ ; https://www.veezi.com/features/cinema-management ; https://www.veezi.com/features/film-programming
- Unique X (boundary reference for the projection-side TMS/CMS family): https://uniquex.com/exhibitor-services/rosettanet/ ; https://uniquex.com/case_studies/cinemark/

> Sourcing limitations: evidence for Vista's scheduling, pricing, and settlement internals comes from its reachable help-centre articles; the other three vendors document their systems at product-page level, so operational specifics for them are asserted only where their pages state them. One additional US cinema vendor (Galaxy Ticketing) could not be fetched this pass and is absent from the sample. Precise operational details (screen counts, fee structures, hold durations, exact state names beyond those documented) are intentionally not stated in this document; such details remain in the Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
