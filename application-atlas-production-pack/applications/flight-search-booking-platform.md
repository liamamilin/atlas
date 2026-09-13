# Flight Search / Booking Platform

## Overview

A **Flight Search / Booking Platform** is a traveler-facing application for finding and buying air travel. It gathers scheduled flights offered by multiple airlines and ticket sellers into one searchable inventory of priced itineraries, lets the traveler compare those itineraries on price and travel practicality, and turns a chosen itinerary into a booked trip — either by completing the booking itself or by handing the traveler directly to the seller that will.

The defining core is deliberately small:

```text
Scheduled-flight inventory (segments, carriers, fares, prices)
└── aggregated across multiple airlines / sellers
    └── structured trip search (route, dates, travelers)
        └── comparable ranked offers
            └── selection → booking (platform-booked, or handoff to a named seller)
```

Everything else commonly associated with these products — filters, price calendars, alerts, fare-condition summaries, manage-booking areas, check-in helpers, disruption handling, hotels and cars alongside flights — is standard market structure built on top of that core, not what makes the product a flight search/booking platform. If the inventory stops being flights, or the aggregation stops spanning multiple sellers, or the search-and-book loop disappears, the product becomes something else: a general travel-retail site, an airline's own storefront, or a fare information service.

## Users & Context

The primary user is an individual traveler organizing their own air travel: choosing where and when to fly, comparing what different carriers and sellers charge, paying, and then managing the trip until they fly.

Typical sessions:

- searching a route and date range to see what exists and what it costs
- comparing alternatives (nonstop vs connecting, carrier, baggage included, departure times)
- booking the selected itinerary for themselves or a small group (family, colleagues)
- returning after booking to check status, download tickets, add bags or seats, change or cancel

Secondary context: travel planners booking on behalf of others, and small businesses using the same consumer-shaped flow for work trips. The platform is used before and between trips, mostly from a phone or browser; the traveler returns to it repeatedly over the life of a booking rather than living in it continuously.

## Core Model

### The Defining Core

The application's world is organized around five connected things.

```text
Trip Query
→ Flight Offer (Itinerary)
→ Seller
→ Booking
→ Post-booking surface
```

- **Trip query** — the search request: a route (origin and destination airports), travel dates, the traveling party (number and type of travelers), commonly a cabin/baggage profile, and a trip shape (one-way, round-trip, multi-city). The query is the entry point to everything; every result and booking traces back to one.
- **Flight offer (itinerary)** — the priced, bookable unit. An itinerary is one or more **flight segments** (departure and arrival airports, times, carrier, flight number), sold as a **fare** at a **price**. Offers differ on stops, duration, times, carrier, and what the fare includes. This object — not the destination, not the traveler — is the center of the system: search produces offers, comparison ranks offers, booking consumes one.
- **Seller** — the party that will actually sell the ticket. In mature products this is realized as more than one model: an airline selling its own flights, a travel agency booking with carriers on the traveler's behalf, or another seller reached through the platform. Which model applies decides what the platform is responsible for after selection (see How It Works).
- **Booking** — what a completed purchase becomes: a reservation for named passengers on the sold itinerary, with a booking reference, a status (requested → confirmed, or failed/declined), and issued tickets. The booking, not the search, is what the traveler returns to.
- **Post-booking surface** — the traveler-facing area where the booking lives: status and documents, changes and cancellation, refunds, ancillaries (bags, seats), and check-in support. When the platform books, this surface is where the platform acts as the traveler's representative toward the carriers.

The three middle concepts deserve one more clarification, because they are where this Type is most often confused with neighbors:

- The **offer** is flight-structured: it decomposes into air segments and fare rules, which is why disruption, refunds, and check-in in this Type follow *air-carrier* logic.
- The **seller** is multiple by construction: the value of the platform comes from putting several airlines and sellers into one comparison.
- The **booking** bridges two worlds: the platform's own record (status, documents, service requests) and the carrier's reservation world (reference number, ticket, check-in). The platform mediates between them; it does not replace the carrier's system.

### Standard Capabilities

Mature products commonly add:

- **Comparison machinery** — filtering and sorting results by stops, times, duration, price, carrier, and alternative airports; cheapest/best-style ranking.
- **Fare-condition visibility** — what the price includes (carry-on/checked baggage, cabin or fare family) and a summary of change and cancellation conditions, so offers are comparable beyond raw price.
- **Price-discovery tools** — flexible-date calendars or month views showing how price varies by day; price alerts that watch a route; saved or recent searches.
- **Passenger capture at booking** — names exactly as on travel documents, contact details, optional loyalty numbers and special requirements.
- **Ancillaries** — seat selection, baggage, travel insurance and similar add-ons, purchasable at booking and usually afterwards.
- **Change / cancellation / refund flows** — with cut-offs before departure, fee rules, and refund routing.
- **Check-in support** — reminders, links or instructions per carrier, and in some products the platform performing online check-in on the traveler's behalf.
- **Disruption communication** — notifying the traveler when a carrier changes or cancels a flight, and presenting options.

How much of this a given product carries depends on its seller model: several of these capabilities (booking management, ancillary handling, change flows, check-in service) exist *because* the platform sold the ticket, and shrink or disappear when it merely refers the traveler to a seller.

## How It Works

### Search → compare → select

```text
Enter route, dates, travelers
→ results: ranked priced itineraries
→ filter / sort / adjust dates
→ open an itinerary: segments, times, carrier, fare conditions, baggage, price
→ select it
```

The searched price is a snapshot, not a held offer: fares are capacity-controlled and change continuously, so the platform treats the final price as binding only when the booking is confirmed.

### Two seller models

**Platform-booked.** The traveler enters passenger details, chooses ancillaries, and pays the platform. The platform then makes the reservation with the carrier(s). Products that book this way commonly document a characteristic pattern: they create platform-controlled credentials for the carrier reservation (a platform-run email address and the carrier reference number, sometimes a password), so that carrier communications — schedule changes, cancellations, refund decisions — arrive at the platform, which notifies the traveler and manages the response. Consequences of this intermediation:

- the traveler can usually reach the carrier's own reservation with their name plus the carrier reference number, but some carrier-side operations (online check-in, refunds) may only work through the platform;
- carrier refunds tend to be paid to the platform, which forwards them to the traveler;
- the platform can offer a unified condition layer on top of differing carrier rules — for example condition tiers (a stricter cheaper tier, a more flexible pricier tier) that normalize what changing or canceling costs across carriers.

**Referral.** The traveler selects an offer and is redirected to the airline or travel agent that sells it; the purchase, payment, ticketing, and all subsequent service happen with that seller. The platform's responsibility ends at the handoff: it routes booking questions to the seller, and its own help material tells travelers to identify the seller of record (even suggesting checking the card statement, since the platform showed the offer but did not sell it).

Both models satisfy the Type; what distinguishes them is who owes the traveler the ticket.

### Confirmation and ticketing are distinct steps

Booking does not end at payment. Products expose traveler-visible booking status — received and processing, confirmed, or failed (payment declined, ticket issuance problems; exact labels vary by product) — and issue tickets after payment, usually quickly but with legitimate delays: airline confirmation for special services (assistance, pets), security/fraud checks, or high booking load. The traveler's protection here is a status they can check and a promise of notification, not instant ticketing. A failed payment or failed ticket issuance cancels the booking rather than leaving it half-alive.

### Managing the trip

After confirmation the traveler lives in the post-booking surface:

- check status, view flight details and documents (e-ticket, receipt/invoice)
- change the trip (new dates/flights, paying the fare difference; subject to cut-offs and once-only or per-tier rules), change or correct passenger details (name changes are typically restricted), add bags or seats
- cancel and request a refund — whole booking or, depending on conditions, individual flights — with refund amounts governed by carrier rules plus any platform condition tier
- prepare to fly: check-in guidance or platform-run check-in, baggage rules, travel documents

### When the airline disrupts the trip

Carriers change schedules and cancel flights; when the platform books, it is positioned to receive that news first and notify the traveler with options (rebooking, refund, alternatives). A special case is itineraries assembled from separately ticketed flights: no carrier covers the connection between them, so a missed self-transfer is the traveler's risk unless the platform has sold protection for it. This risk, and the protection products sold against it, are a direct consequence of the platform's ability to compose offers the carriers themselves do not sell.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Search form

Purpose: express the trip. Typical information: origin/destination, dates or date flexibility, one-way/round-trip/multi-city, travelers, cabin. Primary actions: run search, adjust trip shape.

### Results list

Purpose: compare what the market offers for the query. Typical information: ranked itineraries with times, stops, duration, carrier, and price; indicators of what the fare includes. Primary actions: filter, sort, change dates, open an itinerary.

### Itinerary detail

Purpose: evaluate one offer fully before committing. Typical information: segment-by-segment schedule, carrier, aircraft/cabin where available, baggage and fare conditions, total price and its parts. Primary actions: select and continue to booking, or return to results.

### Booking flow

Purpose: convert the selected offer into a paid reservation. Typical information: passenger details per travel document, contact, ancillaries, price recap, payment. Primary actions: enter/verify details, add extras, pay.

### Manage booking / my trips

Purpose: the booking's home after purchase. Typical information: booking reference, status, flight details, documents, purchased ancillaries. Primary actions: check status, change or cancel, request refund, add services, reach support.

### Price tools

Purpose: help decide *when* and *where* to fly, not just which flight. Common implementations: flexible-date price calendars or month views, price alerts on a route, saved/recent searches. Availability varies by product.

### Check-in and travel-preparation support

Purpose: bridge from booking to the airport. Typical information: check-in windows and links per carrier, baggage and document reminders. Primary actions: open carrier check-in or request platform-run check-in where offered.

## Important Rules / Behaviors

- **Searched prices are not held.** Because fares change continuously, the price that binds is the one confirmed at booking, and products handle the gap as a normal part of the flow rather than an exception.
- **Payment ≠ ticket.** A paid booking can still be processing; ticket issuance is a separate step that can be delayed by airline confirmation of special services or by security checks, and it can fail — in which case the booking is cancelled and the traveler is told. Booking status is always traveler-visible.
- **The ticket lives in the carrier's world.** The booking reference that matters at the airport and at check-in is the carrier's; the platform holds its own booking record alongside it. Where the platform books as agent, it may deliberately keep the carrier-facing credentials and communications to itself, making the platform the traveler's channel to the carrier.
- **Airline rules govern the ticket; the platform may overlay its own.** Change and refund entitlements ultimately follow the carrier's fare rules. Platforms that sell add their own condition tiers, fees, and cut-offs on top, which can unify or (in cheaper tiers) restrict what the traveler may do; referral platforms instead hand the traveler to the seller's conditions entirely.
- **Responsibility follows the seller model.** After a referral handoff, booking problems are the seller's; after a platform booking, they are the platform's. The platform's help material makes this split explicit, because the traveler's intuition ("I searched here, so you help me") is not automatically correct.
- **Passenger identity is anchored to travel documents.** Names must match documents; corrections are possible, full name changes are typically treated as restricted operations.
- **Combined-ticket itineraries have no carrier protection.** Where the platform assembles itineraries from separately ticketed flights, connections between the tickets are the traveler's risk; some platforms sell explicit protection for this case.
- **Refunds can route through the platform.** When the platform paid the carrier, carrier refunds may arrive at the platform and be forwarded to the traveler — a structural consequence of agency intermediation that affects how fast money returns.

## Variants

- **Search-first / referral pole** — the product's identity is search and comparison; every booking is handed to an airline or agent. Deepest investment goes to coverage, ranking, and price tools.
- **Platform-booked pole** — the product sells and tickets itself as the traveler's agent; it owns the post-booking relationship, intermediates carrier communication, and sells condition tiers and protection products.
- **Multi-vertical drift** — the same search/book/manage loop extended to hotels, cars, trains, or packages; the flight loop usually remains the most rule-heavy and most deeply integrated.
- **Itinerary-composition specialists** — products that combine separately ticketed flights to build cheaper itineraries than any carrier sells, carrying the self-transfer risk and protection products that follow.
- **Corporate/business postures** — the same consumer-shaped loop packaged for work travel with reporting and policy controls around it.
- **Regional realizations** — payment rails, currencies, languages, and jurisdiction-specific consumer rules vary; the core loop does not.
- **Adjacent, not a variant: the airline's own storefront.** A single carrier's website shares the booking flow but has no multi-supplier aggregation; it is the supplier's channel (the airline-side reservation system family), not this Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Online Travel Agency / OTA | multi-product travel retail (flights one vertical among hotels/cars/packages); the seam is which inventory the search/book/manage loop is organized around — many market products genuinely straddle both |
| Hotel Search / Booking Platform | same architecture over a different domain inventory (room-nights at properties); no air-segment/PNR/ticket structures, different disruption semantics |
| Metasearch Engine / Vertical Search Engine | general-purpose search ranking; a flight search/booking platform additionally carries the flight-domain offer structure and a booking/handoff path with travel-service responsibilities — remove those and only a vertical search remains |
| Airline Reservation / Passenger Service System | airline-side operator system of record; the platform writes reservations into it (reference numbers, tickets) but never owns it |
| Travel Package Booking Platform | prices flight + accommodation as one bundled unit; here the air leg is priced as its own object |
| Rail Booking & Ticketing | the same consumer loop over rail tariffs and seat reservations rather than air fares and PNRs |
| Corporate Travel Management Platform | organization-side managed travel (policy, approval, duty of care) versus traveler-facing self-serve search and booking |
| Travel Itinerary Planner | organizes and documents trips the traveler already has; does not sell the flights |
| Flight Planning Application | aviation-operations tool for pilots/dispatch planning a flight's route and fuel — unrelated despite the name overlap |

## Representative Products

- Skyscanner — search-first referral pole
- Kiwi.com — platform-booked agency pole with itinerary composition
- Opodo — European online travel agency with a flight-centric booking loop

These three anchor the defining core and the two seller-model poles; other widely known products exist in both poles and in the multi-vertical middle.

## Sources

Research date: **2026-09-08**

- Skyscanner Help Pages — home ("redirected to the airline or travel agent's site where you make your booking directly") — https://help.skyscanner.net/hc/en-gb
- Skyscanner — Find partner contact details — https://help.skyscanner.net/hc/en-gb/articles/360002778378-Find-partner-contact-details-
- Kiwi.com Help — help center structure and booking-model articles — https://www.kiwi.com/en/help
- Kiwi.com — How does Kiwi.com book trips? — https://www.kiwi.com/en/help/how-kiwi-com-works-257/article/how-does-kiwi-com-book-trips-300/
- Kiwi.com — What's unique about Kiwi.com? — https://www.kiwi.com/en/help/how-kiwi-com-works-257/article/what-s-unique-about-kiwi-com-66/
- Kiwi.com — Change and cancellation options based on your ticket type — https://www.kiwi.com/en/help/how-kiwi-com-works-257/article/change-and-cancellation-options-based-on-your-ticket-type-200/
- Opodo Help Center — category tree — https://help.opodo.com/
- Opodo — What is the status of my booking? — https://help.opodo.com/hc/en-150/articles/18970963173522-What-is-the-status-of-my-booking
- Opodo — What are airline booking details? — https://help.opodo.com/hc/en-150/articles/27673147751826-What-are-airline-booking-details

> Sourcing limitation: several widely used products in this category (including a leading search-first product and two large OTAs) could not be reached from the research environment on 2026-09-08 — request timeouts and bot walls. The sampled documentation is therefore tilted toward the European market and toward the referral and agency-booking poles; the merchant/buy-and-resell seller model is described only in general terms. Precise operational figures (issuance windows, fees, refund percentages, cutoff times) are intentionally not stated in this document; they are recorded in the paired Research Notes.

Detailed product-by-product observations, the cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
