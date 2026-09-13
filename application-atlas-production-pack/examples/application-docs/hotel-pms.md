# Hotel Property Management System / PMS

## Overview

A **Hotel Property Management System (PMS)** is the operator-facing system that coordinates the daily operational life of a lodging property: reservations, guests, rooms, arrivals, in-house stays, departures, housekeeping readiness and guest financial records.

The most important insight is that PMS is not simply “reservation software.”

It coordinates several states at once:

```text
Guest / Reservation / Stay lifecycle
            ×
Room availability & operational state
            ×
Folio / payment context
```

For example, a guest may have a valid reservation and be due to arrive, while the assigned room is still dirty. The PMS exists partly to reconcile exactly these kinds of cross-object operational conditions.

A consumer Hotel Booking Platform, a CRS, a Channel Manager and a Revenue Management System may all exchange data with a PMS, but they are different Application Types.

## Users & Context

Primary users commonly include:

- **front desk / receptionist** — manages arrivals, room assignment, in-house guests and departures
- **reservations staff** — creates and modifies reservations
- **guest services staff** — works with current guest/stay information

Secondary users commonly include:

- **housekeeping supervisor / housekeeper** — updates room readiness and service status
- **duty manager / hotel manager** — handles overrides and operational exceptions
- **night audit / finance staff** — works with folio/financial close processes
- **system administrator** — manages configuration and permissions

The PMS is the operational system used when a reservation becomes a real stay occupying a real physical room.

## Core Model

### Guest

A **Guest/Profile** represents the person associated with reservations and stays.

The guest record may preserve history and preferences across multiple visits.

### Reservation

A **Reservation** represents a planned stay.

It commonly carries:

- dates
- guest/profile
- room type/category
- rate
- occupancy information
- reservation status
- payment/guarantee context

A Reservation is not automatically the same thing as actual physical occupancy.

### Room / Space

A **Room** is a physical resource.

It has at least two different kinds of state:

1. commercial availability for a date/time
2. operational readiness for occupancy

A room can therefore be sellable/assigned in one sense while still being operationally not ready in another.

### Stay

A **Stay** is the actual in-house occupancy lifecycle that begins around check-in and ends around check-out.

Some products may not expose a separate “Stay” object, but the conceptual distinction is useful:

```text
Reservation = planned occupancy
Stay = actual occupancy
```

### Folio / Guest Account

The **Folio** or guest account holds financial activity associated with the reservation/stay:

- charges
- payments
- outstanding balance

### Housekeeping / Room Operational State

Housekeeping status is a defining cross-functional part of PMS operation.

A canonical abstraction is:

```text
Not Ready / Dirty
→ Clean
→ Inspected / Ready (where used)
```

with exceptional states such as:

```text
Out of Service
Out of Order
```

### The coupled model

The central PMS relationship can be represented as:

```text
Guest
  ↕
Reservation
  ↓ assigned to
Room ──────── Room Operational State
  ↓
Check-in
  ↓
Stay
  ↔ Folio / Account
  ↓
Check-out
  ↓
Room turnover / Housekeeping
```

This coupled model is more important than any individual feature list.

## How It Works

### Reservation to arrival

```text
Reservation exists
→ arrival date approaches
→ review guest/reservation
→ find or confirm suitable room
→ verify room readiness
→ confirm required payment/guarantee context
→ complete check-in
→ guest becomes in-house
```

A reservation can be valid while the expected room is not yet operationally ready.

### Room turnover

```text
Room requires service
→ room marked not ready / dirty
→ housekeeping work assigned/performed
→ room becomes clean
→ optional inspection
→ room becomes acceptable for assignment/check-in
```

This workflow interacts directly with front-desk work.

### In-house operation

During the stay, staff may:

- inspect reservation/stay details
- change room
- add or correct guest information
- post/manage charges
- respond to guest requests
- coordinate room status or operational tasks

### Departure

```text
Open in-house stay
→ review folio/charges
→ settle required balance
→ complete check-out
→ guest becomes departed
→ room enters turnover
```

### Core vs common vs optional

**Core**

- reservation search/create/update
- guest/profile management
- room/space availability
- room assignment/change
- check-in
- in-house tracking
- check-out
- room readiness/status
- folio/payment context

**Common**

- reservation calendar/timeline
- housekeeping board
- room moves
- group reservations
- guest notes/preferences
- out-of-order room handling
- registration documents
- operational tasks/messages

**Optional / adjacent suite capabilities**

- online check-in
- mobile key
- channel management
- revenue management
- loyalty
- guest marketing/messaging
- upsells

## Interfaces

### Reservation Calendar / Timeline

A time-resource view combining rooms/spaces with reservations.

It helps staff understand:

```text
when
×
which room/space
×
which reservation
```

Typical actions:

- inspect occupancy
- create reservation
- assign/change room
- move reservation
- find availability

### Reservation Detail

The central planned-stay record.

Typical information:

- guest
- dates
- room type / assigned room
- rate
- reservation status
- notes/preferences
- financial context

### Arrivals / Check-in

Shows expected arrivals and guides staff from reservation to actual occupancy.

### In-house

Shows guests/stays currently occupying the property.

### Departures / Check-out

Shows expected departures and supports settlement and final checkout.

### Room Assignment / Availability

Searches and filters physical rooms according to date, category, assignment and operational suitability.

### Housekeeping Board

Shows physical room readiness and cleaning/inspection work.

### Folio / Account

Shows charges, payments and outstanding balance associated with the guest/stay.

## Important Rules / Behaviors

### Two linked lifecycles

A PMS must coordinate at least:

```text
Reservation / Stay lifecycle
+
Room operational lifecycle
```

These are not the same lifecycle.

### Reservation / stay lifecycle

A safe conceptual abstraction is:

```text
Reserved / Confirmed
→ Arriving
→ Checked In / In House
→ Checked Out / Departed
```

Alternative outcomes include:

- cancelled
- no-show

Vendor labels differ.

### Room operational lifecycle

A safe abstraction is:

```text
Not Ready / Dirty
→ Clean
→ Ready / Inspected
```

with exception states such as:

```text
Out of Service
Out of Order
```

### Cross-object constraints

Normal check-in may depend on:

- valid reservation conditions
- an assignable room
- acceptable room readiness
- required payment/guarantee conditions

### Permissions

Role-based permissions commonly affect:

- reservation editing
- room reassignment/override
- rate override
- check-in/check-out
- housekeeping status changes
- folio/payment actions
- system configuration

### Important edge cases

- room not ready at arrival
- overbooking
- room move during stay
- early arrival
- late departure
- cancellation
- no-show
- room becomes out of order
- guest extends stay
- settlement failure
- group/multi-room reservation

## Variants

Common variants include:

- full-service hotel PMS
- limited-service hotel PMS
- resort PMS
- multi-property PMS
- hostel-oriented PMS

A hostel may approach a specialized Type when bed-level inventory materially changes the resource and assignment model.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Hotel Booking Platform | traveler-side search/comparison/booking is primary |
| Hotel Central Reservation System / CRS | centralized reservation/inventory distribution is primary |
| Hotel Booking Engine | direct customer booking capture is primary |
| Hotel Channel Manager | OTA/channel inventory and rate synchronization is primary |
| Hotel Revenue Management System | demand/rate optimization is primary |
| Hotel Housekeeping Management | room-cleaning and turnover operation is primary |

## Representative Products

- Oracle Hospitality OPERA Cloud
- Mews
- Cloudbeds

## Sources

Research date: **2026-09-05**

Primary research sources:

- Oracle OPERA Cloud — Front Desk  
  https://docs.oracle.com/en/industries/hospitality/opera-cloud/25.4/ocsuh/ch_front_desk.htm
- Oracle OPERA Cloud — Checking in reservations  
  https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.1/ocsuh/t_checking_in_reservations.htm
- Oracle OPERA Cloud — Available room search  
  https://docs.oracle.com/en/industries/hospitality/opera-cloud/25.5/ocsuh/t_front_desk_available_room_search.htm
- Oracle OPERA Cloud — Housekeeping Board  
  https://docs.oracle.com/en/industries/hospitality/opera-cloud/25.2/ocsuh/t_housekeeping_using_the_housekeeping_board.htm
- Mews — Timeline overview  
  https://help.mews.com/s/article/The-Timeline-An-overview
- Mews — Check in a reservation  
  https://help.mews.com/s/article/check-in-a-reservation
- Cloudbeds — Housekeeping  
  https://myfrontdesk.cloudbeds.com/hc/en-us/articles/25695101078427-Housekeeping-Everything-you-need-to-know

See the paired Research Notes for detailed cross-product evidence and canonicalization decisions.
