# Sports Facility Management

## Overview

A **Sports Facility Management** application is the operator-side business system of record for running a sports facility — a multisport complex, ice arena, turf/field house, court facility, batting-cage center, or similar venue — as a business.

Its defining core is small:

```text
The facility's rentable-space inventory of record
└── Bookings (a party holds a specific space for a specific time)
    └── The facility's money record (charges raised, settled, accumulated)
```

Everything else commonly associated with these products — online self-service booking, leagues and camps, memberships and passes, point of sale, marketing, check-in hardware — is widespread in current products but is not what makes the product a sports facility management system. A booking-centric product with none of those additions, and a paper-era arena with a rental ledger and a wall calendar, both sit inside the Type.

When the center of gravity shifts to the player booking a venue as a third party, the product is a different Application Type (Sports Court Booking). When it shifts to membership and entry as the core relationship, it drifts toward Recreation Center Management. When it shifts to administering competition between organizations, it drifts toward League Management Platform.

## Users & Context

The primary user is the **facility operator** — the business or organization that runs the venue:

- **facility/general manager**: owns the schedule, pricing, and revenue picture
- **scheduler / front-desk staff**: create and modify bookings, check parties in, take payments
- **program coordinator**: builds seasons of leagues, classes, camps, and clinics and fills them with registrants

Secondary users:

- **customers** (renters, participants, parents, team managers): book space, register for programs, pay, and manage their own bookings through a self-service portal where offered
- **bookkeepers / owners**: consume revenue and utilization reporting

The work environment is the venue itself: a scheduling calendar that staff keep open all day, a front desk with a point of sale, and — in mature deployments — a customer-facing portal. Facilities are frequently multi-location (several venues under one operator), and the same system often serves a mixed portfolio (an ice sheet plus courts plus rooms).

## Core Model

### The Defining Core

**1. The facility's rentable-space inventory of record.**
The venue's spaces — courts, ice sheets, fields, turf, cages, lanes, rooms, simulators — are held as individually identified, bookable units. Each space carries operator-configured bookable time: when it can be reserved, in what increments, with what buffers between uses. Spaces are commonly grouped into types (all courts, all fields) that share settings, subdivided (a field split into halves for simultaneous practices), and organized across locations. Because many spaces share one calendar, the system prevents conflicts: booking one space can automatically block dependent spaces (renting the "entire facility" blocks every court and room in it).

**2. The booking as the unit of transaction.**
A booking is a party — a person, family, team, or organization — holding a specific space for a specific time. It is the atom of the whole system: rentals, parties, private lessons, league games, and camp sessions are all bookings (or booking-like events) placed against the inventory. A booking carries a lifecycle: requested → confirmed → paid → used → closed, with cancellation and refund paths. The facility keeps the record: who booked what, when, at what price, under what terms.

**3. The facility's money record.**
Charges are raised against bookings and usage. Pricing is structured by the nature of the space and the time: hourly or flat rates, different rates for different seasons, days, or peak windows, add-on fees (equipment, furniture, catering). Charges are settled — paid online, invoiced, or rung up at the desk — and accumulate into the facility's revenue and utilization record, which reporting turns into the operator's business picture (which surfaces and programs make money, where the open capacity is).

These three are jointly load-bearing. An inventory without bookings is a space list; bookings without an inventory are a widget over nothing; money without both is a payment terminal; inventory plus bookings without money is a shared calendar, not a business system.

### The Surrounding Structure

Mature products wrap the core in a consistent set of structures:

- **Programming** — the facility's own offerings: leagues, classes, camps, clinics, private lessons, birthday parties, tournaments. Programs occupy the same spaces as rentals (a league's games are events on the same calendar as rentals), are configured with schedules, capacity, waitlists, and prices, and are filled through registration.
- **Customers** — a database of the people and organizations that transact with the venue: individuals, families, organizations/teams. Accounts carry contact details, payment methods, purchase and booking history, and (where used) memberships and passes.
- **Staff** — role-based permissions decide who can create, edit, or delete bookings, manage resources, or process refunds; staff schedules (referees, instructors, coaches) can be placed on the same calendar as the events they staff.

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:   Rentable-space inventory
Realized as:  named resources on a calendar grid; spaces with availability rules;
              courts/fields/rooms grouped by type, split into sub-units

Concept:   Booking lifecycle
Realized as:  instant paid booking; request-then-approve; contract with accepted terms;
              permit issued; invoice; refund

Concept:   Money record
Realized as:  products bound to bookings (flat/hourly, seasonal date ranges, peak rules);
              integrated payments; POS transactions; batch invoicing
```

## How It Works

### Configure the venue

```text
Define locations
→ add each rentable space (court, rink, field, room, cage)
→ group spaces into types, split large surfaces into sub-units
→ set bookable time: availability windows, block sizes, buffers
→ attach pricing (rates by duration, season, day, peak window) and terms
→ set conflict rules (what blocks what)
```

This configuration is the facility's capacity of record. Everything else writes against it.

### Take bookings

```text
A party requests or books a space for a time
→ (admin-side: staff find open time via availability search and create the booking)
→ (self-service: the customer picks a space and slot in the portal —
   instantly, or as a request the operator approves)
→ terms accepted / contract or permit produced
→ charges raised (paid now, invoiced, or paid at the desk)
→ the time is blocked; conflicts are prevented automatically
→ the booking is used, adjusted, or cancelled under the facility's rules
```

Bookings can be copied, repeated, rolled over, and edited; refunds and cancellations are recorded against the original. The facility's booking history is searchable and reportable.

### Run programming

```text
Build a season of programs (leagues, classes, camps, clinics)
→ publish for registration (individual, team, or family)
→ registrants sign up, pay, sign waivers; rosters fill to capacity with waitlists
→ sessions are scheduled onto the same spaces as rentals
→ attendance is checked in; the program's revenue accumulates
→ next season is cloned from the last and adjusted
```

Leagues sit at the intersection of programming and competition: the facility creates them, registers teams or players, schedules their games into its own spaces, and — depending on the product — either computes schedules and standings natively or hands scoring to an integrated competition tool.

### Operate the day and resolve money

```text
Today's schedule on the calendar/grid
→ check-ins at the desk, kiosk, or gate
→ walk-in sales (concessions, pro shop, drop-ins) at the point of sale
→ payments, invoices, refunds recorded against bookings, programs, and sales
→ close-out; revenue and utilization reporting by category, space, and program
```

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Scheduling calendar / grid

The center of the product. All spaces as columns (or rows) against time, showing every booking, program session, league game, and maintenance block; drag-and-drop creation and movement; conflict warnings; mass edit for seasons.

- typical information: spaces, times, booking type, party, status, color coding by kind
- primary actions: create/move/resize bookings, block time, check conflicts, jump to a booking's detail

### Booking manager / booking detail

The record behind each booking: party, space, time, charges, terms, contract or permit, payment state.

- primary actions: edit, copy, roll over, invoice, refund, cancel, print permit/contract

### Registration administration

The programming side: program catalog, seasons, rosters, capacity and waitlists, waivers, payment plans.

- primary actions: create/duplicate programs, open registration, manage rosters, check in attendees, issue refunds

### Customer portal / mobile app

The customer-facing surface where offered: browse bookable spaces and programs, see real-time availability, book and pay, sign waivers, view upcoming bookings and registrations.

### Point of sale

Front-desk selling: admissions, drop-ins, concessions, pro shop, rentals — in one transaction, tied to the same customer accounts and revenue record.

### Reporting

Utilization (which spaces are used when), revenue by category (rentals, programs, POS), program performance, customer trends; the operator's business picture.

### Settings

Spaces, types, availability, pricing, terms, roles and permissions, integrations.

## Important Rules / Behaviors

### Conflict prevention is structural

The inventory is shared: one space, many claimants. The system prevents double-booking automatically, and related-space rules extend this (booking a whole-facility block bars its parts; buffers keep turnaround time between uses). This is not a convenience feature — it is what makes a shared calendar into a capacity of record.

### Booking is not always instant

Self-service booking commonly supports a spectrum: instant paid booking, request-then-approval (the time is not held until staff confirm), request with hidden pricing, and login-required booking. The operator chooses per space or booking type. A confirmed request behaves like any other booking once approved.

### Pricing follows time

Charges are a function of the booking's shape: duration (hourly vs flat), season (date ranges with their own rates), day and time (peak/off-peak), and add-ons. Changing the time changes the price; the money record reflects the booking, not a menu price alone.

### Money is recorded, not just collected

Every charge — booking fee, program tuition, POS sale, refund — lands in the facility's revenue record against its category. Cancellations and refunds adjust the record rather than erasing history. Utilization and revenue reporting are two views of the same underlying bookings.

### Access is governed

Role-based permissions decide who can create, edit, or delete bookings and resources; customers book only what the operator has exposed; memberships or passes, where used, can gate what a customer may book or buy. Terms and conditions accepted at booking are retained with the record.

### The facility keeps its history

Bookings, programs, payments, and check-ins accumulate as the venue's operating record — searchable by date, space, party, and type — feeding permits, invoices, and reports after the fact.

## Variants

- **Full-suite multisport / ice / turf / court facilities** — the complete picture: rentals + programming + POS + memberships + marketing (the dominant posture among dedicated venue products)
- **Booking-centric venues** — spaces, availability rules, pricing, payments, and memberships only, without a programming suite or POS; common for single-purpose venues (simulators, cages, courts) and as lightweight tools
- **Municipal / parks & recreation deployments** — the same core plus residency-based pricing, fund accounting, and permit workflows; the operator is a public department and the venue is community inventory
- **Higher-education recreation facilities** — campus recreation posture on the same core
- **Sport-vertical packaging** — ice, soccer/turf, baseball/softball, gymnastics, aquatics, driving ranges, golf simulators: mostly the same structure with sport-specific vocabulary and integrations
- **Multi-location operators** — several venues under one database, with cross-location reporting and (optionally) cross-location booking

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Sports Court Booking | two sides of one transaction | that Type is the player's demand-side loop with the venue as a third party; this Type is the venue operator's system of record; a marketplace channel integrated into a facility system remains the demand side |
| Recreation Center Management | sibling genus, different center | the rec-center posture centers membership/entry and the multi-activity community relationship; this Type centers rentable capacity, bookings, and revenue; one platform can serve both postures |
| Racquet Club Management | sport-specific sibling | racquet products center court-time play shapes, member governance, and pro programming; this Type's spaces are generic venue spaces without racquet semantics |
| Golf Course Management | sport-specific sibling | golf's unit is a starting position on a shared course (tee sheet, per-player green fees, round lifecycle); this Type rents exclusive time on a space |
| Sports Academy Management | capability slice | academy software centers the athlete population, program portfolio, enrollment, and tuition loop; facility scheduling appears there as a bundled module, not the center |
| Sports Club Management | different operated unit | the club is a member organization fielding teams; the facility is a venue selling time and programs; a club's facility bookings are one module |
| League Management Platform | adjacent | facility-run leagues exist to fill the facility's spaces; that Type administers competition between organizations (fixtures, results, standings) as its center |
| Facility Management System (building operations) | name collision, different object | building maintenance, work orders, and preventive maintenance are not this Type; physical-plant upkeep appears here only as integrations or scheduling gaps |
| Amenity Booking Platform | adjacent machinery | amenity booking serves a closed residential population over a building's shared facilities; this Type serves an open renter/participant population over a sports venue's capacity |
| Parks & Recreation Administration | adjacent at the municipal pole | the department's season-cycled catalog and community-wide inventory vs one operator's venue system of record; residency pricing machinery overlaps |
| Event Management Platform | adjacent | parties and one-off events here are productized bookings against venue spaces; that Type centers the event itself (attendees, agenda, registration at event scale) |
| Appointment Scheduling Application | generic neighbor | no sport-typed space inventory, no venue mediation, no facility revenue record |

## Representative Products

- **Dash** (DaySmart Recreation) — full-suite sports facility management spanning multisport, ice, turf, and court facilities, plus community rec center and parks & rec verticals
- **FinnlySport** — full-suite venue management with ice-arena, sportsplex, municipal, and higher-education heritage; native rules-based league scheduling
- **AllBooked (by Skedda)** — booking-centric venue platform for athletic facilities and community spaces: spaces, rules, pricing, payments, memberships

Category-named vendors whose documentation could not be reached during research (EZFacility, eSoft Planner) are recorded in the Sources note below.

## Sources

Research date: **2026-09-09**

- Dash — https://www.dashplatform.com/ (homepage, multisport and community rec center verticals); Dash Help Center — https://help.daysmartrecreation.com/ (Rental Booking collection; Initial Setup for Booking Manager; Booking Manager Admin Setup; Resources; Initial Setup collection)
- FinnlySport — https://finnlysport.com/ (homepage, solutions page)
- AllBooked — https://www.allbooked.com/ (homepage)

> Sourcing limitation: several category vendors (EZFacility, eSoft Planner, RAMP Interactive, Bond Sports) were unreachable from the research environment (blocked or empty responses after repeated attempts). Findings rest on the three sampled products plus previously processed sibling passes; common structures are stated as cross-product commonality within that sample, and no precise operational parameters (numeric limits, default settings) are asserted. Detailed product-by-product observations are recorded in the paired Research Notes.
