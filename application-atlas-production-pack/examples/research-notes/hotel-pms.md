# Research Notes — Hotel Property Management System / PMS

## Research Goal

Identify the stable operational structure of a Hotel PMS and explain why it is distinct from customer booking, central reservation/distribution, housekeeping-only and revenue-management systems.

## Initial Boundary

Target:

> Hotel Property Management System / PMS

Working hypothesis:

> Hotel PMS is the property's operational source of truth linking guest/reservation lifecycle to room inventory/readiness and guest financial/stay operations.

## Research Questions

- What is the relationship among Guest, Reservation, Room and Stay?
- Is Reservation the same thing as actual occupancy?
- How does room assignment work?
- What makes a room operationally ready?
- How does housekeeping state constrain front-desk work?
- What happens during check-in and check-out?
- What is a Folio / guest account?
- Which states belong to the reservation/stay versus the room?
- How is PMS different from Booking Platform, CRS, Channel Manager and RMS?

## Representative Products

| Product | Why selected |
|---|---|
| Oracle Hospitality OPERA Cloud | major enterprise hotel PMS reference |
| Mews Operations | modern cloud-native property-operations model |
| Cloudbeds PMS | broad independent hotel/hostel market reference |

## Sources

Research date: 2026-09-05

### Oracle OPERA Cloud

- Front Desk  
  https://docs.oracle.com/en/industries/hospitality/opera-cloud/25.4/ocsuh/ch_front_desk.htm
- Checking in reservations  
  https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.1/ocsuh/t_checking_in_reservations.htm
- Available room search  
  https://docs.oracle.com/en/industries/hospitality/opera-cloud/25.5/ocsuh/t_front_desk_available_room_search.htm
- Housekeeping Board  
  https://docs.oracle.com/en/industries/hospitality/opera-cloud/25.2/ocsuh/t_housekeeping_using_the_housekeeping_board.htm
- Room management / housekeeping  
  https://docs.oracle.com/en/industries/hospitality/opera-cloud/25.1/ocsuh/c_housekeeping_room_management.htm

### Mews

- Timeline overview  
  https://help.mews.com/s/article/The-Timeline-An-overview
- Check in a reservation  
  https://help.mews.com/s/article/check-in-a-reservation
- Create reservations from Timeline  
  https://help.mews.com/s/article/How-to-create-reservations-from-the-Timeline-in-Mews-Operations?language=en_US

### Cloudbeds

- Housekeeping  
  https://myfrontdesk.cloudbeds.com/hc/en-us/articles/25695101078427-Housekeeping-Everything-you-need-to-know
- Cloudbeds API overview  
  https://developers.cloudbeds.com/docs/about-cloudbeds-api

## Product Observations

### Oracle OPERA Cloud

Front Desk operations visibly organize around:

- arrivals
- in-house
- departures
- reservation/profile review
- room assignment/search
- folio/account
- housekeeping room status

Check-in confirms an important sequence:

```text
Reservation
→ review guest/profile
→ room assignment/readiness
→ payment requirements
→ check-in
```

Housekeeping documentation exposes distinct room-operational states such as:

- Clean
- Dirty
- Inspected
- Pickup
- Out of Order
- Out of Service

### Mews

Timeline combines **spaces/rooms** and **reservations** in a time/resource view.

This reveals that PMS operates over two axes:

```text
time / reservation
×
physical room / space
```

Check-in depends on reservation conditions and room readiness.

### Cloudbeds

Documentation exposes:

- reservations
- guests
- rooms
- housekeeping assignment
- clean/dirty/inspected room conditions

This reinforces the same coupled model.

## Cross-product Comparison

| Finding | OPERA | Mews | Cloudbeds | Canonical decision |
|---|---|---|---|---|
| guest/profile | yes | yes | yes | Core |
| reservation | yes | yes | yes | Core |
| room/space | yes | yes | yes | Core |
| availability/calendar/timeline | yes | yes | yes | Core |
| room assignment | yes | yes | yes | Core |
| check-in/check-out | yes | yes | yes | Core |
| housekeeping condition | yes | yes | yes | Core/Common |
| payment/folio/account | yes | yes in operational billing model | account resources | Core/Common |
| channel management | broader/integrated | integrated | broader/integrated | Adjacent |
| revenue optimization | separate/broader | integration | broader | Adjacent |

## Canonical Model

The key model is not a flat object list.

It is three coupled systems:

### A. Guest / Reservation / Stay lifecycle

```text
Guest
↕
Reservation
→ Check-in
→ Stay / In House
→ Check-out
```

### B. Room resource state

```text
Room
├── room type/category
├── availability
└── operational readiness
    ├── dirty / not ready
    ├── clean
    ├── inspected (where used)
    └── out of service/order
```

### C. Financial account

```text
Stay / Reservation
↔ Folio / Guest Account
↔ Charges / Payments
```

### Defining cross-object dependency

```text
Reservation ready for arrival
+
Room assigned
+
Room operationally acceptable
+
required financial conditions
→ Check-in can complete
```

This interaction is more defining than any single feature list.

## Vendor-specific / Rejected Findings

Do not define PMS core by:

- channel manager
- revenue management
- loyalty
- marketing
- mobile key
- guest messaging
- upsell modules

These are frequently integrated or bundled.

## Boundary Findings

### vs Hotel Booking Platform

Booking Platform is customer-side:

```text
search
→ compare
→ choose
→ book
```

PMS is operator-side:

```text
reservation
→ room assignment
→ arrival
→ in-house operation
→ departure
```

### vs CRS

CRS focuses on centralized reservation/inventory distribution across properties/channels.

### vs Housekeeping Management

Housekeeping focuses on room turnaround/cleaning. PMS coordinates that state with the wider stay lifecycle.

### vs Revenue Management

RMS optimizes rates/inventory decisions; PMS executes property operations.

## Uncertainties

- Reservation and Stay may be represented as one record or multiple concepts depending on vendor
- Folio/account depth varies
- exact room-status labels differ materially
- hostel bed-level inventory may materially alter the resource model

## Final Synthesis

Canonical Hotel PMS:

```text
property operations
=
guest/reservation/stay lifecycle
× room availability/readiness
× folio/payment context
```
