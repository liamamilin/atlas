# Attraction Management System

## Overview

An **Attraction Management System** is the operator-side system of record for a visitor attraction's admission business. It lets the operator of a theme park, zoo, aquarium, museum, water park, family entertainment center, or similar paid-entry venue define what grants entry, sell it through every sales channel against bounded capacity, issue admission entitlements, validate those entitlements at the point of entry, and manage the guest relationship and on-site spending around the visit.

The defining core is small:

```text
Operator-defined admission products
└── Sale through the system's channels
    └── Recorded transaction (booking/order) issuing admission entitlements
        └── Entry validation (redemption) producing the attendance record
```

Everything else commonly associated with these products — timed entry and session capacity, season passes and memberships, on-site food-and-retail POS, kiosks, guest CRM, promotions, reseller distribution, cashless wristbands, waivers — is standard mature capability or segment-specific extension, not what makes the system an attraction management system. A small regional attraction that sells open-dated tickets at a counter and scans them at the door still fits the defining core; remove entry validation and the product collapses into generic e-commerce; remove operator-defined admission products and it is no longer selling admission at all.

## Users & Context

Primary users are the attraction's own staff:

- **Box office / admissions clerks** — sell and adjust bookings, redeem tickets, take payments, handle refunds and reschedules.
- **Gate / entry staff** — validate tickets and passes at entry points, with scanners, turnstiles, or handheld devices.
- **Food & beverage / retail clerks** — sell on-site items against the same guest and transaction records.
- **Membership / guest-relations staff** — sell and renew memberships, verify members, resolve entitlement questions.
- **Marketing and group-sales staff** — run promotions, segments, and school/tour-group bookings.
- **Administrators / management** — configure products, capacity, schedules, roles; monitor sales and attendance.

Guests are secondary but active users: they buy online, receive tickets, reschedule bookings, sign waivers, and use kiosks and self-service portals without staff involvement.

The work environment is a live venue: sales happen continuously across online channels and on-site counters, while entry validation happens in real time at gates. The system must hold up under peak-day load, because capacity decisions and entry throughput are its core subject matter.

## Core Model

### The Defining Core

Three structures. If any one is removed, the product is no longer recognizable as an attraction management system:

- **Operator-defined admission products** — the attraction defines its own catalog of what grants entry: ticket types (typically with price variations such as adult/child), passes, and memberships, each carrying a price and validity rules (which day, which time, how long it stays redeemable). Without this, the system is not selling admission.
- **Sale → transaction → entitlements** — a purchase through any channel is recorded as a transaction (a booking or order) that holds line items, the purchaser, and payment state, and that issues redeemable admission entitlements — individual tickets, or validity on a pass or membership. Without this, there is no commercial record of the visit.
- **Entry validation producing attendance** — an entitlement is validated (scanned, redeemed, checked in) at the attraction's entry point, and that redemption event is what the system counts as attendance. Without this, the system is just a storefront.

### Standard Capabilities

Mature products across the researched sample carry most of the following. They make the admission business operable but do not define the Type:

- **Capacity and session control** — admission inventory bounded by capacity: timed-entry slots, time blocks, entry points, session schedules tied to operating hours, advance booking windows, live capacity monitoring, and the ability to block or reduce capacity for a day or session.
- **Passes and memberships** — season/annual/multi-visit passes and memberships with validity periods, renewal and upgrade, member benefits (typically discounts), and member recognition at entry (photos, IDs, cards, digital membership cards).
- **On-site POS** — counter selling for walk-ups, adjustments to existing bookings, split payments, refunds, and manager approval for sensitive actions; often extended to food, retail, parking, and other on-site spend.
- **Self-service kiosks** — unattended selling, waiver signing, ticket pickup, and member recognition.
- **Guest records** — purchaser identity, visit and purchase history, segments for marketing, flags (including banned-guest handling), and online guest accounts for self-management.
- **Promotions and pricing rules** — peak/off-peak and early-bird pricing, discount codes, purchase limits.
- **Group sales** — school and tour groups and party bookings: adjusted headcounts, deposits or payment plans, group-level check-in.
- **Gift cards and stored value** — prepaid value redeemable on-site.
- **Reseller and OTA distribution** — selling through third-party marketplaces and agents, with voucher redemption back on-site.
- **Reporting and finance** — sales, attendance, and membership reporting; revenue categorization; tax handling.
- **Staff roles and permissions** — role-governed access to selling, redemption, refunds, and configuration.
- **Access hardware integration** — barcode/QR/RFID scanners, turnstiles and gates, wristbands.

### One Structure, Many Implementations

The core model is conceptual. Different products realize each concept differently:

```text
Concept:              Admission product
Implementations:      ticket types with variations, session passes, standard/day passes,
                      season/annual passes, multi-visit passes, memberships, packages

Concept:              Capacity container
Implementations:      capacity-carrying resources or areas, timed sessions/time blocks,
                      entry points, per-day capacity

Concept:              Transaction
Implementations:      booking with line items, order, cart-based purchase

Concept:              Admission entitlement
Implementations:      per-person ticket (QR/barcode), pass validity, membership validity,
                      composite ticket covering a package

Concept:              Entry validation
Implementations:      staff redemption at POS, handheld/mobile check-in,
                      gate/turnstile scan, self-service scan
```

A reader who has only seen one implementation — say, mandatory timed-entry tickets at a large theme park — should still be able to recognize a small museum selling open-dated tickets at a counter from the same core model.

## How It Works

### Configure the admission business

```text
Define the venue and its operating hours
→ create admission products (ticket types, passes, memberships) with prices and validity rules
→ attach capacity (areas, time blocks, entry points) and session schedules
→ open sales channels (online checkout, counters, kiosks, resellers)
→ set staff roles and permissions
```

Configuration is an ongoing loop: products and schedules change with seasons, exhibitions, and events; capacity rules change with demand.

### Sell admission

```text
Guest or staff starts a purchase
→ selects products for a date/time (or open-dated)
→ applies promotions, memberships, or group terms
→ pays (in full, or deposit for groups)
→ system records the transaction and issues entitlements (tickets/pass validity)
→ guest receives tickets (email, app, print) or entitlement is loaded onto a card/wristband
```

The same transaction model serves every channel: the attraction's own online checkout, the on-site counter, self-service kiosks, phone/back-office sales, and reseller vouchers redeemed on arrival.

### Arrive and enter

```text
Guest presents entitlement (QR/barcode/card/wristband) or is found by name
→ system validates it against its rules (right day? already used? waiver signed? member active?)
→ redemption is recorded — this is the attendance count
→ exceptions route to staff: wrong-day tickets (offer reschedule), missing waivers (block until signed),
   banned guests (require approval), groups (check in the whole order at once)
```

Redemption is normally once per ticket; multi-visit products redeem repeatedly within their validity. Membership validation both admits (where applicable) and applies member benefits to purchases.

### During the visit

```text
On-site spend: food, retail, parking, photos, upgrades — sold at POS against the same records
→ stored value (gift cards, cashless cards/wristbands) drawn down where offered
→ membership benefits applied to qualifying purchases
→ upgrades and add-ons attached to the existing booking
```

### Run the operation

```text
Monitor live capacity and redemptions for today
→ adjust capacity (block/reduce) or open overbooking deliberately
→ reconcile sales, attendance, and membership activity in reports
→ feed revenue categories to accounting; handle regional tax/fiscal requirements
→ market to guests based on visit history and segments
```

### Core vs Common vs Optional

**Defining core** — without these, not an attraction management system:

- operator-defined admission products with validity rules
- multi-channel sale producing recorded transactions that issue entitlements
- entry validation producing the attendance record

**Standard capabilities** — present in most mature products:

- capacity/session control (timed entry), operating hours
- passes and memberships with renewal and member recognition
- on-site POS and add-on spend
- kiosks
- guest records/CRM
- promotions and pricing rules
- group sales
- gift cards / stored value
- reseller/OTA distribution
- reporting, roles, access-hardware integration

**Optional / segment-dependent** — present in some products or segments:

- digital waivers for risk activities (common in water parks and active FECs; product-dependent)
- cashless wristbands and game cards (FEC posture)
- virtual queuing (vendor-specific extensions)
- dynamic/demand-based pricing
- donations and fundraising with donor conversion (cultural institutions)
- education/class/camp registration (zoos, museums, science centers)
- seated event ticketing on the same platform (arts/culture dual nature)
- regional fiscal compliance packs (e-invoicing, fiscal devices)
- guest mobile apps and digital wallet passes

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Administration console

The operator's configuration and oversight surface.

- product catalog, capacity/session setup, operating hours, channel and integration settings
- booking search and adjustment, guest records, membership management
- dashboards for today's sales, attendance, and capacity
- primary actions: create/edit products and schedules, adjust capacity, manage bookings and guests, configure roles

### Point of sale (counter)

The staffed selling and arrival surface.

- product tiles/menus, booking lookup, cart with variations and promotions
- primary actions: sell, adjust an existing booking, redeem tickets, apply membership benefits, take payment (incl. split), refund with approval, reschedule

### Online checkout

The guest-facing purchase surface, embedded in the attraction's site or standalone.

- product selection by date/time with live availability, cart, promotions, membership prompt
- primary actions: buy, manage an existing booking (reschedule, where offered), sign waivers

### Entry / check-in surface

Where entitlements become attendance.

- scan-based validation (handheld, counter, gate/turnstile) with clear accept/deny outcomes
- primary actions: redeem ticket, verify member, handle exceptions (reschedule, approval, waiver)

### Self-service kiosk

Unattended sales and preparation surface.

- product selection and payment, waiver signing, ticket/booking lookup and pickup, member recognition

### Guest self-service portal / account

Where guests manage their own relationship.

- upcoming bookings and tickets, passes and memberships, reschedule and payment-plan options (where offered)

## Important Rules / Behaviors

### An entitlement is valid only within its rules

A ticket carries its validity (date, time slot, expiry) and is redeemable within it. Wrong-day tickets are a routine exception: products commonly still allow redemption, and many offer a reschedule path — in some products with any price difference applied — rather than silently honoring the wrong day.

### Redemption is the attendance record

Attendance figures are derived from entry validations, not from sales. A sold-but-unredeemed ticket is revenue but not a visit; multi-visit products redeem many times within validity. Some products report both total redemptions and unique visits separately.

### Membership is identity plus benefit

A membership both identifies the member (verified at entry or purchase, sometimes with photo) and acts as a pricing instrument — its discounts apply to qualifying purchases, with usage frequency governed by product-specific rules. Membership redemption and ticket redemption are separate events.

### Capacity is enforced, with a deliberate override

Sales and bookings are bounded by configured capacity; in some products a deliberate overbooking override exists for staff. Capacity can also be temporarily blocked or reduced for closures and events.

### Waivers can gate entry

Where activities carry liability, a signed waiver is attached to the ticket and redemption is blocked until it is signed — some products add bulk handling so large groups are not held at the gate. This is product- and segment-dependent.

### Sensitive actions are permission-gated

Refunds, banned-guest redemption, and certain overrides require manager approval or elevated roles. Past-date bookings are commonly restricted from casual editing or refunding.

### Money follows the transaction

Refunds, exchanges, and reschedules operate against the recorded transaction; stored value (gift cards, cashless balances) is a separate ledger that can also receive refunds. Some products additionally restrict editing or refunding of past-date bookings.

## Variants

Common shapes of the same Type:

- **Family entertainment center / water park posture** — parties and packages, game credits and cashless cards, waivers, high session turnover.
- **Theme park posture** — high-volume capacity management, season passes, meal deals and parking, dynamic pricing, gate hardware at scale.
- **Cultural institution posture (museums, zoos, aquariums, gardens)** — timed entry with entry-point capacity, memberships with strong renewal mechanics, donations and donor conversion, education programs, deep patron CRM.
- **Regional small attraction posture** — counter sale plus scan validation, open-dated tickets, minimal capacity machinery.
- **Ski / outdoors posture** — season passes and gate scans dominate; often the same vendors with adjusted emphasis.
- **Arts/culture dual posture** — the same platform also runs seated event ticketing and subscriptions alongside admissions.

A variant remains a variant while the defining core holds. When the inventory unit changes to seats at performances or to itinerary departures, the product has crossed into a neighboring Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Attraction Ticketing | slice of the same domain | the sell-and-validate slice only; the management system adds capacity operations, memberships, on-site spend, guests, and reporting |
| Event Ticketing Platform | most confusable neighbor | inventory unit is performances and seats (seat maps, one-off events); here it is admission capacity to a place, with no seat map as the primary unit |
| Tour Operator Management System | adjacent | sells itinerary departures with guides/resources and often multi-day scope; here the product is place admission |
| Theme Park Management | adjacent, complementary | ride operations, queue, maintenance, safety — the park's physical operations, not the commercial admission layer |
| Museum Visitor Experience Platform | adjacent, complementary | visitor-facing interpretation and experience layer, not the admissions business |
| Cashless Venue Platform | slice | the stored-value payment capability in isolation |
| Digital Waiver Management | slice | waiver capture and compliance in isolation |
| Hotel Booking Engine / Restaurant Reservation Platform | distant | date/time inventory exists, but the product is lodging or tables, not admission; no entry-validation semantics |
| Amenity Booking Platform | distant | bookable amenities for a property's residents/guests, not a public admission business |
| E-commerce Platform | underlying capability | online checkout is one channel; without admission products and entry validation it is generic e-commerce |

The boundary with Event Ticketing is the sharpest: arts and culture platforms often contain both models, so the distinguishing question is which inventory model is primary — seats at performances, or admission capacity to a place.

## Representative Products

- **ROLLER** — cloud all-in-one for FECs, theme/water parks, zoos; deep public help center
- **Tessitura** — unified CRM platform for arts, culture, museums, zoos/aquariums; admissions alongside seated ticketing
- **accesso Passport** — e-commerce-first SaaS sales platform for high-volume attractions (theme/water parks, zoos, museums, ski)
- **Blackbaud Altru** — ticketing, membership, and fundraising suite for museums, zoos, aquariums, and cultural organizations

The defining core was checked against segment extremes (small regional counter-sale attractions vs high-volume theme parks) and against the arts/event-ticketing boundary (Spektrix) to avoid over-fitting to any one segment's implementation.

## Sources

Research date: **2026-09-06**

- ROLLER Help Center — glossary; "Get started with products, resources and schedules"; "How guest and member check-in works" — https://mysupport.roller.software/
- Tessitura — product site; "Ticketing & Admissions" feature page — https://www.tessitura.com/
- accesso — product site; accesso Passport product page — https://accesso.com/
- Blackbaud Altru — product page — https://www.blackbaud.com/products/blackbaud-altru
- Spektrix Support Centre (boundary sample) — https://support.spektrix.com/hc/en-gb

> Sourcing limitation: public operational documentation for accesso Passport and Blackbaud Altru was not reachable from the research environment on 2026-09-06; claims about those products are held at product-page strength. Tessitura detail is feature-page level. Precise operational specifics (numeric capacity limits, validity windows, refund rules, default settings) are intentionally not stated in this document; they remain in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
