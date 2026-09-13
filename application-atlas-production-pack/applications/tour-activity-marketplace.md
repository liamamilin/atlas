# Tour & Activity Marketplace

## Overview

A **Tour & Activity Marketplace** is a two-sided application that aggregates many independent operators' bookable tours, activities, and experiences into a single traveler-facing venue, and intermediates each booking between traveler and operator.

The defining structure has three parts that only work together:

```text
Experience listing of record (operator-authored, bookable)
        ↓ discovered through
Multi-supplier aggregation + traveler-side discovery
        ↓ realized as
Intermediated booking (pay the platform → confirmation → voucher/ticket → settlement to operator)
```

- Remove the aggregation and it becomes a single operator's own booking site.
- Remove the intermediated booking and it becomes a review site or a lead-gen directory.
- Remove the experience binding (scheduled local experiences delivered at a place and time) and it becomes a generic online travel agency selling lodging and transport.

Everything commonly associated with these platforms — instant confirmation, review scores, QR-code vouchers, supplier portals, mobile apps, travel-agent channels — is widespread in current products but is not what makes the product this Type.

## Users & Context

Two primary user populations face each other through the platform:

**Travelers** — people planning or already on a trip, looking for things to do in a destination. They search or browse by destination, category, and date, compare options, book and pay, and arrive at the activity with a voucher or ticket. Their typical moments: planning at home, deciding on the ground, managing a booking (reschedule, cancel), and using the voucher on the day.

**Operators and suppliers** — tour and activity companies (walking tours, day trips, adventure operators, attraction admissions, classes, hosts of local experiences) who list their products to reach travelers they could not reach alone. They author listings, keep availability and pricing current, confirm bookings, and get paid through the platform.

**Secondary roles**: platform customer support (handling cancellations, refunds, disputes), and in some products travel agents or resellers who book on behalf of clients for commission.

The characteristic context is trip planning: the traveler's decision is destination-bound and date-bound, and the operator's delivery happens offline, in person, at a meeting point.

## Core Model

### The experience listing of record

The supply-side unit is the **listing**: an operator-authored, bookable description of one experience. A listing carries, in structured form:

- what the experience is — title, description, photos, sequenced itinerary or activity outline
- what is included and excluded
- logistics — meeting point or pickup, duration, start times
- pricing — per participant, often with participant types (adult/child) and private-group options
- bookable options — dates, time slots, or variants of the same product (different start times, inclusions, or pickup points), each with availability
- the operator's identity and the product's cancellation policy

The listing is persistent and maintained by the operator through a supplier-side surface; the platform reviews or vets listings before they go live, with requirements varying from content quality checks to identity verification, licenses, and insurance for certain activities.

### The intermediated booking

The transaction unit is the **booking**: a specific traveler party (participants), a specific listing option, a specific date and time. The platform holds the transaction relationship end to end:

- the traveler pays the platform at booking (some products allow reserving now and paying later)
- the booking is confirmed — immediately for supply with real-time availability, or after the operator confirms manually for supply that must reconfirm
- the traveler receives a **voucher or ticket** — the proof-of-purchase presented on the day, sometimes with a scannable code
- cancellation and refund follow the listing's policy, surfaced before booking and enforced through the platform
- the operator is paid by the platform after the activity takes place, net of the platform's fee

### Multi-supplier aggregation and discovery

The traveler-facing venue aggregates listings from many independent operators and makes them discoverable: search by destination or attraction, filters (date, price, duration, rating, free cancellation, private tour), category browsing, and product detail pages that present the listing's structured content — operator, availability, inclusions, logistics, reviews, cancellation policy — side by side across operators. Review and rating surfaces let later travelers evaluate earlier ones' experiences.

### How the pieces relate

```text
Operator ──authors──▶ Listing (options × availability × pricing)
                          │
                          ▼ aggregated with many other operators' listings
                    Marketplace venue (search / browse / compare / reviews)
                          │
Traveler ──books──▶ Booking (party × option × date)
                          │
                    Payment to platform → Confirmation → Voucher/ticket
                          │
                    The day: redemption at the meeting point
                          │
                    Cancellation/refund per policy  ·  Settlement to operator
```

## How It Works

### Operator side: from listing to payout

```text
Register and verify
→ create the listing (content, photos, itinerary, meeting point, inclusions)
→ configure options, pricing, availability, cancellation policy
→ submit for platform review / quality check
→ listing goes live in the venue
→ bookings arrive (real-time or as requests to confirm)
→ run the activity; travelers redeem vouchers
→ cancellations handled with categorized reasons when the operator must cancel
→ payout by invoice cycle for bookings that have traveled
```

Operators commonly keep availability in sync with their own reservation systems through integrations, so that a booking on the marketplace blocks the slot elsewhere and vice versa.

### Traveler side: from discovery to the day of the activity

```text
Search or browse a destination / category
→ compare product pages (what's included, logistics, reviews, cancellation policy)
→ choose a date, time, and party size
→ book and pay (or reserve-now-pay-later where offered)
→ receive confirmation and voucher/ticket
→ arrive at the meeting point; redeem the voucher
→ optionally review the experience afterwards
```

### Confirmation: two modes

Both modes are standard in the market and a single product commonly carries both:

- **Instant confirmation** — real-time availability; the booking is confirmed and the voucher issued immediately.
- **On-request confirmation** — the platform forwards the request; the operator confirms within a stated window; the voucher follows confirmation.

### Cancellation and change

Cancellation policies are per listing and shown before booking. Travelers cancel or reschedule through the platform within policy; operators can also cancel (operator unavailability, weather, minimum participants not reached, force majeure), in which case travelers are notified automatically and offered rescheduling or a refund. Refunds and compensations are processed through the platform, not directly between traveler and operator.

## Interfaces

### Marketplace front end (traveler)

- **Search / browse** — destination- and category-based entry; filters and sorting; the primary discovery surface.
- **Product detail page** — the listing's full presentation: photos, itinerary, inclusions/exclusions, meeting point, availability and pricing per option, reviews, cancellation policy; primary actions: choose an option, book, message the operator, save to a wishlist.
- **Checkout** — party details, payment, policy acceptance; produces the booking.
- **My bookings** — list of bookings with status; primary actions: view voucher/ticket, reschedule, cancel, contact support or the operator.
- **Voucher / ticket view** — the proof-of-purchase for the day, with meeting-point details and scannable code where supported.

### Supplier portal (operator)

- **Listing management** — create and edit products, options, pricing, availability; submit for quality review.
- **Booking management** — incoming bookings with references and filters; confirm requests; cancel single or multiple bookings with categorized reasons.
- **Payout / invoices** — earnings for bookings that have traveled, payout cycles, balances.
- **Redemption tooling** — scan or validate traveler vouchers on the day (app or web).

### Review and trust surfaces

Ratings and written reviews on product pages; traveler photos; operator identity and, in some products, vetting badges or verification markers.

## Important Rules / Behaviors

- **The listing's cancellation policy governs refunds.** The policy is part of the listing, shown before booking, and enforced through the platform's refund machinery. Exact terms vary per product and per listing.
- **Confirmation is a distinct state, not automatic.** For on-request supply, a paid or submitted booking is not yet a guaranteed place until the operator confirms; the platform communicates the confirmation window.
- **Vouchers may be person-bound.** Some vouchers are tied to the guest details entered at booking and are non-transferrable; traveler details are collected at checkout for this reason.
- **Operator cancellations trigger automatic traveler remedies.** When the operator cancels (weather, minimum participants, unavailability), travelers are notified through the platform and offered rescheduling or refund — the traveler does not negotiate with the operator directly.
- **Settlement follows travel.** Operators are paid for bookings that have taken place, per the platform's payout cycle; cancellations and compensations adjust the payout.
- **Listings are gated.** Platforms review or vet listings before publication — from content quality checks to identity verification and license/insurance proof for activities that require them — and can suspend listings that violate standards.

## Variants

- **Professional-operator marketplaces** — supply from tour companies and activity providers at scale; the dominant pattern.
- **Vetted individual-host marketplaces** — supply from individuals who apply and are vetted (identity, expertise, itinerary standards); experiences offered alongside another product's core inventory.
- **Instant-confirmation-first vs on-request-heavy** — varies with how digitized the supply's inventory is.
- **Marketplace inside a broader travel platform** — experiences bundled with hotels, transport, or attraction tickets in one travel app; the experiences core is intact but embedded.
- **Agent/reseller channels** — some marketplaces expose a booking surface for travel agents with commission tracking.
- **Open-date vs fixed-date tickets** — some listings sell dated slots; others sell vouchers redeemable on a chosen day.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Online Travel Agency / OTA | center of gravity is lodging and transport inventory; the tour & activity marketplace binds to scheduled local experiences; one product may bundle both |
| Attraction Ticketing | dedicated dated-admission inventory for attractions is the center of gravity; admission tickets appear inside marketplaces as one listing category |
| Tour Operator Management System | the operator-side system of record (reservations, resources, scheduling, channel management); the marketplace is a sales channel it connects to |
| Vacation Rental Marketplace | per-night lodging inventory vs scheduled experiences; some products carry both cores |
| Event Ticketing | dated event inventory with entry/seating control vs operator-authored experience itineraries; events may appear as a marketplace category |
| Travel Review Platform | reviews without intermediated booking = review platform; the booking transaction is the separating structure |
| Travel Itinerary Planner | planning and organizing trips vs transacting bookings |

The most important boundary is with the OTA: both aggregate travel supply and intermediate bookings. The difference is what is sold — scheduled local experiences delivered by an operator at a place and time, versus lodging and transport.

## Representative Products

- Viator (a Tripadvisor company)
- GetYourGuide
- Klook
- Airbnb Experiences

## Sources

Research date: **2026-09-10**

- GetYourGuide — Supply Partner Help Center (managing bookings, cancellations and reasons, payouts, supplier portal): https://supply.getyourguide.support/hc/en-us ; connectivity FAQ: https://www.getyourguide.supply/connectivity/faqs-search-results ; traveler Help Center: https://www.getyourguide.com/contact ; General Terms and Conditions: https://www.getyourguide.com/c/general-terms-and-conditions
- Viator — Agent Resource Center (making a booking, managing bookings, commissions and payments): https://agentcenter.viator.com/resources/making-a-booking , https://agentcenter.viator.com/resources/manage-booking , https://agentcenter.viator.com/resources/commission-and-payments ; Help Center: https://www.viator.com/help
- Klook — Help Center and FAQ (confirmation timing, open-date vs fixed-date, refunds): https://www.klook.com/help-center , https://www.klook.com/faq/category-51 ; merchant introduction: https://merchant.klook.com/introduction
- Airbnb — Help Center (how booking works for experience hosts, hosting requirements and standards): https://www.airbnb.com/help/article/1560 , https://www.airbnb.com/help/article/3888 , https://www.airbnb.com/help/article/1451 ; host landing page: https://www.airbnb.com/host/experiences

> Sourcing note: exact commission rates, payout thresholds, and confirmation windows are vendor-specific and time-varying; only figures directly stated in official sources were recorded, and none are treated as properties of the Type. Detailed product-by-product observations are in the paired Research Notes.
