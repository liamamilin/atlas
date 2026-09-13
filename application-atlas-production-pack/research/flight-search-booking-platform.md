# Research Notes — Flight Search / Booking Platform

Research date: **2026-09-08**

---

## Research Goal

Understand, from real products, what a Flight Search / Booking Platform is: what objects its world is built from, how a traveler moves from "I need to fly from A to B" to a booked ticket, what happens after booking, and where this Type ends and its neighbors (OTA, hotel booking platform, airline reservation systems, metasearch) begin.

## Initial Boundary

Hypothesis before research:

- Core use: search over scheduled air services across multiple airlines/sellers, compare priced itineraries, and convert a selection into a booking (or a directed handoff to a seller).
- Primary users: individual travelers planning and purchasing their own air travel.
- Nearest neighbors:
  - Online Travel Agency / OTA (flights as one vertical among hotels/cars/packages)
  - Hotel Search / Booking Platform (same architecture, different inventory)
  - Metasearch Engine / Vertical Search Engine (§02.02 general-leaf family — search without domain booking path)
  - Airline Reservation / Passenger Service System (airline-side operator system; different seat)
  - Travel Package Booking Platform (bundle as one priced unit)
  - Rail Booking & Ticketing (same pattern, different transport domain)
- Known unknowns:
  - Is the leaf meant to cover both metasearch-style referral and direct booking? (Leaf name's slash suggests both.)
  - What does the platform actually own post-booking when it books (ticket, PNR, change rights)?
  - Is multi-supplier aggregation definitional, or would single-airline storefronts count?

## Research Questions

1. What does a flight search query consist of, and what does it return?
2. What is a flight "offer" — how are itineraries, segments, fares, and prices structured?
3. Who sells the ticket: the platform, an airline, an agent? What seller-of-record models exist?
4. What happens at booking time (passenger data, payment, confirmation, ticket issuance, PNR)?
5. What post-booking surfaces exist (manage booking, changes, cancellation, refunds, check-in)?
6. How do airline fare rules interact with platform-level fare/ticket-type overlays?
7. What breaks the normal flow (price change, payment decline, delayed confirmation, carrier disruption, self-transfer)?
8. Where is the boundary to metasearch-only products, to OTA, and to airline direct channels?

## Representative Products

Selected for: market representativeness + documentation completeness + different product philosophies (referral vs booking) + different poles of the Type.

| Product | Pole / philosophy | Documentation accessed |
|---|---|---|
| Skyscanner | flight search-first, booking handed to airline/agent partners | help center root + 1 article (server-rendered) |
| Kiwi.com | booking platform, agency-of-record model, virtual-interlining philosophy | help center, 4 articles |
| Opodo | European OTA, flight-centric docs, agency-of-record model | help center, 3 pages + 2 articles |

Attempted but not accessible (recorded as source-access limitations; no memory-filled claims used for them):

- Google Flights — support.google.com timed out twice → abandoned.
- Expedia — support/service pages returned 429 → abandoned.
- Kayak — bot-verification wall. Trip.com — transport error.

The sample is consequently tilted toward the European market and toward the two seller-model poles (referral and agency booking). No merchant-model direct evidence was obtained; merchant-model claims are therefore kept weak in the final document.

## Sources

Official surfaces used (all fetched 2026-09-08):

- Skyscanner Help Pages — https://help.skyscanner.net/hc/en-gb (home; "Flights/Stays/Car Hire" split; referral statement)
- Skyscanner — Find partner contact details — https://help.skyscanner.net/hc/en-gb/articles/360002778378-Find-partner-contact-details-
- Kiwi.com Help — https://www.kiwi.com/en/help (structure: product & services / payment & booking confirmation / changing booking / baggage-seating-extras / check-in & boarding / disruptions)
- Kiwi.com — How does Kiwi.com book trips? — https://www.kiwi.com/en/help/how-kiwi-com-works-257/article/how-does-kiwi-com-book-trips-300/
- Kiwi.com — What's unique about Kiwi.com? — https://www.kiwi.com/en/help/how-kiwi-com-works-257/article/what-s-unique-about-kiwi-com-66/
- Kiwi.com — Change and cancellation options based on your ticket type — https://www.kiwi.com/en/help/how-kiwi-com-works-257/article/change-and-cancellation-options-based-on-your-ticket-type-200/
- Opodo Help Center — https://help.opodo.com/ (full category tree)
- Opodo — What is the status of my booking? — https://help.opodo.com/hc/en-150/articles/18970963173522-What-is-the-status-of-my-booking
- Opodo — What are airline booking details? — https://help.opodo.com/hc/en-150/articles/27673147751826-What-are-airline-booking-details

Evidence layers: **A** = directly observed in an official source for a named product; **B** = observed across ≥2 sampled products; **C** = canonical inference from comparison + boundary reasoning. Claims in the final document are calibrated to these layers.

---

## Product observations

### Skyscanner

- [A] Self-description: "Skyscanner is a travel search engine that helps you find the best travel options. Once you have found what you're looking for, you are redirected to the airline or travel agent's site where you make your booking directly." → the pure referral pole: the platform is the discovery-and-comparison layer; the seller completes the purchase.
- [A] Seller set is explicitly plural: "one of the many airlines, hotels, car hire companies or travel agents that sell through our site" — flights plus other verticals sold through the same search surface.
- [A] The platform is not the seller of record: "Unsure who you bought your travel from? Check your credit card statements to see who took your payment." Booking questions are routed to the airline/agent ("They are therefore best placed to help with any questions about your booking"), and the platform maintains a directory of partner contact details.
- [A] Help taxonomy: Searching / Prices / Bookings / Travelling (+ About; separate help sites for Stays and Car Hire) — search, price transparency, booking handoff, and travel-time topics are the four canonical concern areas.
- [B, with Kiwi/Opodo] Price is a first-class help category → price transparency and price-change handling are a standing concern of the Type (category-level evidence only; article content not retrieved).
- Not observed: any platform-side booking management; consistent with referral pole.

### Kiwi.com

- [A] Site scope: nav = Flights / Cars / Hotels / Extras / Last minute — flight-centric product with adjacent verticals; "Manage your trips, set up price alerts, use Kiwi.com Credit" in account pitch.
- [A] Agency-of-record booking model: "we make a reservation with the airlines on your behalf… we create a unique temporary email address and payment details for your booking to ensure we can manage your reservation, add extras, and alert you if anything changes." The platform interposes itself between traveler and carrier: it authorizes receiving all carrier communications on the traveler's behalf and notifies by email/SMS/push.
- [A] Reservation mechanics: traveler accesses airline reservation "using only your name and the carrier reservation number (PNR)"; some carriers need more credentials, which the platform may not disclose → those operations (online check-in, refunds) must run "through your Kiwi.com account."
- [A] Refund plumbing: "Since we pay for your trip from our account, most carriers will also send any potential refunds… back to us… we have to forward it to you." Refund-for-whole-itinerary rule; refund alternatives offered as "disruption services."
- [A] Platform fare-condition overlay: 3 ticket types (Saver / Standard / Flexi) unify change-and-cancel conditions across carriers — e.g., change = pay only fare difference; cancel handled "according to airline rules"; change possible only once under Standard/Flexi then Saver rules apply; cancellation cut-off expressed in hours before trip start; refund fee per traveler/flight without the guarantee product; Flexi cancels the whole booking for all passengers with a percentage refund of airline-ticket price and airline services, platform fees non-refundable. (Specific percentages/fees/numbers are product-specific → Research Notes only.)
- [A] Partial cancellation: under Saver/Standard the traveler "can cancel specific flights" and select which ones; Flexi is whole-booking only.
- [A] Virtual interlining / self-transfer: "our unique travel hacks. Whether that looks like combining separate flights that are cheaper than a carrier connection, or getting off during your layover instead of the final destination because it's cheaper than a direct flight"; "Our Kiwi-Code checks all available routes and their combinations." Consequence: carriers don't cooperate on self-transfer disruptions → platform sells a protection service ("disruption services… help you reach your final destination or get a refund").
- [A] Post-booking service bundle: platform check-in "for all of your flights, so you don't have to do it manually with each airline"; baggage/seating handled at reservation; processing fees may apply to post-booking changes "depending on the service options you pick during booking"; third-party extras (travel insurance, compensation services).
- [A] Booking confirmation is a distinct step: related article "What if my booking confirmation is delayed?" — "You'll find the booking status in your account and we'll keep you posted."
- [A] Search breadth framing: "find and book cheap itineraries that you won't find with other search engines or carriers"; "adjust our search options"; price alerts referenced.

### Opodo

- [A] Scope: help tree covers Cancellation (Flight / Refunds / Flight+hotel), Modification (Flight / Changes by the airline / Flight+Hotel), Baggage (allowance, special, add-baggage, airport), Check-in (per-carrier pages incl. a carrier-specific one, Seats, Online check-in), Hotel, Trains, Cars, Booking status, Flight details, Payment, Insurance, Prime (subscription), Special assistance, Travel documents.
- [A] Booking statuses (traveler-visible): **Confirmed booking** / **Booking request received** ("we will send you a confirmation within 24 hours") / **Booking cancelled or payment declined** ("problems processing your payment or issuing your ticket… email with clear instructions").
- [A] Ticket issuance is a separate post-payment step: tickets "issued within a period of 24 hours after payment has gone through. In most cases, tickets are issued within minutes of payment being received, unless you have selected a special service that may require the confirmation of the airline (e.g. special assistance… travelling with a pet)"; security/fraud checks "can delay the issuance of your tickets for a few hours"; failed checks → contact by email. (24h window is product-specific detail.)
- [A] Agency-of-record pattern (independent confirmation of Kiwi's): "These are a set of booking details we create to book flights on your behalf… Your assigned details will include an email address and the airline reference number, or a password… the email address is different from your personal email"; per-flight credential sets when multiple carriers; used "to retrieve or manage your booking on the airline's website"; updates still arrive in the personal email.
- [A] Booking-management surface: "Manage my booking" / "My Trips" — login by email + booking reference; check status, flight details, baggage allowance.
- [A] Post-booking flows exist as first-class categories: flight modification, name-change article, Flight/Travel Credit instrument, flexible-dates product, refunds, airline-initiated changes ("Changes by the airline"), add-baggage, seats, online check-in.
- Not observed: referral-mode behavior; Opodo sells and tickets itself (agency pole).

---

## Cross-product Comparison

| Dimension | Skyscanner | Kiwi.com | Opodo | Strength |
|---|---|---|---|---|
| Domain objects | flights across airlines + agents | itineraries incl. self-transfer combinations of separate tickets | flights (plus hotel/train/car) | B |
| Search-first | yes, explicitly | yes | yes (search/booking product) | B |
| Who books | redirected to airline/agent | platform books with airlines "on your behalf" | platform books "on your behalf" (assigned credentials) | B (two poles: referral vs platform-booked) |
| Seller of record | partner (check card statement) | platform (pays from own account; refunds route back) | platform | A per product |
| Airline credentials | n/a | virtual email + PNR; may withhold carrier login | assigned email + airline reference/password, per flight | B (agency pattern) |
| Booking confirmation as distinct step | n/a (happens at partner) | yes (status in account; delayed-confirmation article) | yes (3 statuses; issuance window; security checks) | B |
| Post-booking management surface | none (partner handles) | account trip page: changes, cancel, refund, check-in service | My Trips: status, modification, name change, add-baggage, check-in | B |
| Fare-condition layer | partner's own conditions | platform ticket types unifying carrier rules | carrier rules + platform options/credit | B (overlay only where platform books) |
| Change/cancel governed by | partner policies | airline rules + platform overlay + fees | airline rules + platform flows | B |
| Carrier disruption handling | partner | platform disruption services; notifies on carrier changes | "Changes by the airline" category | B |
| Ancillaries | via seller | platform-managed (bags, seats) + extras | platform-managed (bags, seats, insurance) | B |
| Check-in | partner | platform can check in for all flights | online check-in help incl. carrier-specific quirks | B |
| Price concerns | Prices category | price alerts | pricing/payments category, flexible dates | B (category-level) |
| Verticals beyond flights | stays + car hire via separate help sites | cars/hotels/extras | hotels/trains/cars | B (drift, not defining) |
| Subscription/bundle programs | — | Kiwi.com Guarantee, Disruption Protection, Kiwi Credit | Prime | L3 |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (jointly held; smallest structure)

1. **Scheduled-flight inventory as the domain.** The platform's world is built from scheduled air services between airports — segments with carriers and times — presented as priced fare options. Remove → the product is no longer about flights at all.
2. **Multi-supplier aggregation.** Options are drawn from more than one airline and/or more than one ticket seller, brought side by side in one place. Remove → it becomes an airline's own direct sales channel (a supplier's storefront, not a platform).
3. **Structured trip search.** A query keyed by route, dates, and traveling party produces a comparable, ranked set of priced itineraries. Remove → a browsing catalog or fare-information page, not a search platform.
4. **Selection-to-booking path.** Selecting an offer leads either to a booking completed through the platform (passenger data → payment → confirmation → ticket issuance) or to a directed handoff to the named seller that will complete it. Remove → a price/schedule information service.

The leaf name's slash ("Search / Booking") corresponds to poles 4a and 4b; both satisfy L0. What both poles share is that the platform is where the *selection* happens and the traveler leaves the platform only toward a specific purchase.

Jointly-held is load-bearing: 1+3 without 2 = flight information/fare-tracking site; 2+3 without 1 = generic metasearch/shopping; 1+2 without 3 = supplier catalog; all without 4 = travel media.

### L1 — Common Mature Structure (not definitional)

- Result comparison machinery: filtering and sorting by stops, times, duration, price, carrier, airport.
- Fare-condition visibility: what the price includes (baggage, cabin/fare family), summary of change/cancel conditions.
- Date-flexibility and price-discovery tools: price calendars/month views, price alerts/monitoring, flexible-date options, saved/recent searches.
- Trip query shapes: one-way, round-trip, multi-city; traveler counts/types; cabin profile.
- Booking management surface ("my trips / manage booking"): booking reference, status, flight details, e-ticket documents.
- Passenger-data capture at booking: names per travel documents, contact details, special requirements, loyalty numbers.
- Ancillary selection: seats, baggage, travel insurance.
- Change/cancel/refund flows with cut-offs, fees, and refund routing.
- Check-in support: pointers, reminders, or platform-run check-in.
- Agency-intermediation pattern (where the platform books): platform-controlled airline contact credentials; carrier communications received on the traveler's behalf; refunds routed through the platform.
- Carrier-disruption communication flows (airline changed/canceled → platform notifies and offers options).

### L2 — Variant / Optional Structure

- Seller-model pole: referral/metasearch vs platform-booked (agency-of-record vs — asserted weakly, not directly sampled — merchant/consolidator buying-and-reselling).
- Flight-only vs multi-vertical (drift toward OTA: hotels, cars, trains, packages).
- Virtual interlining: itineraries assembled from separately ticketed flights; self-transfer risk and platform protection products.
- Platform fare/ticket-type overlays (branded condition tiers) — only meaningful when the platform is the seller.
- Corporate/business booking postures.
- Regional realizations: payment rails, currencies, languages, jurisdiction-specific consumer rules.
- Subscription programs ( Prime-style free-shipping-style analogues for travel), guarantee/protection add-ons.
- Adjacent pole outside the Type: airline direct storefront (single supplier).

### L3 — Vendor-specific (kept out of final document; listed for evidence)

- Kiwi.com: Kiwi-Code, Kiwi.com Guarantee, Disruption Protection (Premium), Kiwi.com Credit, travel-hacks framing (throwaway/hidden-city style), Saver/Standard/Flexi exact terms (48h cut-off, change-once, €30 fee, 80% Flexi refund), virtual email/payment mechanics.
- Opodo: Prime subscription, Flight/Travel Credit, Flexible Travel Dates, exact status names and 24-hour issuance language, carrier-specific check-in pages (one low-cost carrier), "airline booking details" naming.
- Skyscanner: "Everywhere"-style discovery framing (marketing pages not fetched), separate help sites per vertical.
- Google Flights / Expedia / Kayak: no official docs retrieved; no vendor claims recorded.

## Rejected Findings (candidates that failed the tests)

- "Price forecasting" as a Type capability — single-source marketing claim class, not documented in sample → rejected from core (L3 at best).
- "24-hour ticketing window" as a Type rule — one product's specific SLA; the *separation of payment from issuance* is the B-layer finding; the number is L3.
- "Metasearch is a different Type" — rejected for this leaf: the leaf name covers both poles, and the referral pole shares the full flight-domain structure; the true boundary is against domain-agnostic vertical search (see Boundary Findings).
- "The platform owns the ticket" — false in general; the ticket/PNR belongs to the carrier world; the platform owns the *booking relationship* and service overlay. Kept as an Important behavior, not ownership.
- "Multi-city / error-fare / hack features" — vendor features or marketing framings; not structural.

## Boundary Findings

- **vs Online Travel Agency / OTA.** Same market space, different center of gravity. A flight search/booking platform's inventory and its search/book/manage loop are built around the flight domain; an OTA's center of gravity is multi-product travel retail (flights are one vertical). In practice many flight platforms expand into OTA and most OTAs have flight verticals — the seam is which inventory the search/book/manage loop is organized around. The two poles observed here both sit on the flight side; the sampled "OTA" (Opodo) still documents its flight loop with flight-domain objects. Record as a relationship, recommend joint-review with the OTA pass.
- **vs Hotel Search / Booking Platform.** Same architecture (query → priced offers → book/manage), different domain inventory (room-nights at properties vs air segments; no PNR/e-ticket analogue; different disruption semantics). The flight leaf is not a generic "travel booking" leaf: the air-domain structures (segments, PNR, ticket issuance, carrier rules, disruption) carry its rules.
- **vs Metasearch Engine / Vertical Search Engine (§02.02 family).** A referral-pole flight platform is *also* a vertical search — but this leaf requires the flight-domain inventory plus the selection-to-booking path and the travel-service responsibilities (fare-condition visibility, partner routing). A product that only ranks links to flight pages without the booking path would belong to §02.02. Removal test: remove the booking/handoff path → vertical search engine.
- **vs Airline Reservation / Passenger Service System.** The PSS is the airline-side operator system of record; the platform writes reservations into it (via PNRs) but never owns it. An airline's own website is that system's consumer channel — a single-supplier storefront. Removal test: remove multi-supplier aggregation → airline direct channel (PSS family), not this Type.
- **vs Travel Package Booking Platform.** Packages price flight+accommodation (etc.) as one unit; here the air leg is priced as its own object. Bundles exist as optional add-ons without moving the Type.
- **vs Rail Booking & Ticketing / other transport verticals.** Same consumer pattern over a different domain inventory (rail tariffs/seat reservations vs air fares/PNRs).
- **vs Corporate Travel Management Platform.** Org-side managed travel (policy, approval, duty of care) vs traveler-facing self-serve search/book. B2B variants of flight platforms exist but keep the same core loop.
- **"去掉什么就变成另一个 Type" summary:** remove flight-domain inventory → generic OTA/metasearch; remove multi-supplier → airline direct channel; remove trip search → supplier catalog; remove booking/handoff path → fare information service.

## Historical / Market-Sample Check (per §24 reasoning)

- Would older products fit? Web-era flight booking platforms from the early 2000s (one sampled product's lineage dates to that era) already exhibit: search over multiple airlines, priced itineraries, platform-booked ticketing, manage-booking, airline-rule-driven changes. Referral pole likewise predates direct booking features. The four L0 structures hold without any modern feature (price alerts, AI, dynamic bundles).
- Regional products (Asian, Middle East, Latin American OTAs/flight platforms) are structurally identical per the same L0; the sampled documentation is European, which is a sample bias, not a structure.
- Platform-native/single-supplier pole (airline direct) was deliberately placed outside the Type; this matches the directory, which keeps Airline Reservation / PSS as a separate leaf.
- The check passed without weakening L0; no further abstraction was needed.

## Uncertainties

1. **Merchant model under-documented.** No sampled product documented buying-and-reselling (merchant) terms directly; final document mentions seller-model variety with weak wording.
2. **Google Flights / Kayak / Expedia / Trip.com inaccessible.** Search-side features (price insight/graphs, forecasting) could not be evidence-checked; the final document avoids claiming them.
3. **Price-change mechanics between search and booking.** Supported at category level (Prices categories; booking-status flows) but no article explicitly documented "price changed at checkout"; final document states only that searched prices are not held offers and the binding confirmation happens at booking time.
4. **Skyscanner article depth.** Only home + one article server-rendered; its search-feature inventory (alerts, saved searches) is asserted only as "commonly offered by such products," not as Skyscanner-specific fact.
5. **Corporate/B2B variant** not sampled; recorded as variant with no structural claims.

## Final Synthesis

A Flight Search / Booking Platform is the traveler-facing application layer for air travel acquisition. Its defining core is jointly held: (1) an inventory of scheduled flights offered as priced itineraries, (2) aggregated across multiple airlines/sellers, (3) reached through structured trip search producing comparable results, and (4) closed by a selection-to-booking path that either completes the booking in the platform or hands the traveler to the named seller. Everything else — comparison machinery, price tools, fare-condition display, agency-intermediation credentials, change/cancel/refund machinery, check-in support, disruption handling, ancillaries, extra verticals — is mature-market structure layered on that core, and specific vendor terms (ticket tiers, guarantee products, subscription programs, exact windows and fees) remain vendor detail.
