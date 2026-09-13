# Research Notes — Tour & Activity Marketplace

## Research Goal

Understand what a Tour & Activity Marketplace actually is as an Application Type: what exists inside it, who uses which side, how a booking flows from discovery to voucher to payout, and where its boundaries lie against OTAs, attraction ticketing, tour-operator management systems, and review platforms.

## Initial Boundary

Tentative hypothesis before research:

- Core use: travelers discover and book tours, activities, and experiences in a destination; local operators list and sell them through the platform.
- Likely users: travelers (consumer side), tour/activity operators and suppliers (supply side), platform customer support.
- Nearest neighbors: Online Travel Agency / OTA (lodging/transport focus), Attraction Ticketing, Tour Operator Management System (supplier side), Vacation Rental Marketplace, Event Ticketing, Travel Review Platform.
- Unknowns: is instant confirmation definitional? Is the platform-held payment (intermediation) definitional vs lead-gen? Where does attraction admission fit? How do supplier-side integrations relate?

## Research Questions

1. What is the unit of record on the supply side — what does a "product" consist of?
2. How does a booking flow: search → product page → option/date → checkout → confirmation → voucher → the day of the activity?
3. Instant confirmation vs on-request (reconfirmation) — is one of them definitional?
4. How does money move: who charges the traveler, how does the supplier get paid, what is the commission model?
5. What cancellation/refund machinery exists and who enforces it?
6. What supplier-side surfaces exist (portal, listing management, booking management, redemption)?
7. What trust/review structures exist?
8. Where is the boundary vs OTA, attraction ticketing, event ticketing, and the supplier-side management system?

## Representative Products

Chosen for market representability, documentation quality, and different product philosophies / customer tiers:

- **Viator** (Tripadvisor company) — largest long-standing tours-and-activities marketplace; strong traveler + travel-agent + supplier documentation.
- **GetYourGuide** — major global experiences marketplace; excellent two-sided documentation (traveler Help Center + Supply Partner Help Center + connectivity API docs).
- **Klook** — Asia-origin travel/experiences platform with a broader travel bundle (trains, hotels, eSIM); documents instant vs on-request confirmation explicitly; merchant portal documented.
- **Airbnb Experiences** — different philosophy: individual hosts, vetted application-based listing, inside a stays platform; documents host-side flow and fee model.

## Sources

- GetYourGuide Supply Partner Help Center (supply.getyourguide.support): Managing bookings, Canceling Bookings (Single and Batch), Understanding Cancellation Reasons, Understanding Bookings for Payout, Navigating the Supplier Portal; GetYourGuide connectivity FAQ (getyourguide.supply); traveler Help Center topic list (getyourguide.com/contact); General Terms and Conditions.
- Viator Agent Resource Center (agentcenter.viator.com): Making a Booking, Manage Bookings, Commissions & Payments, Bookings and Commission Reports; Viator Help Center index (viator.com/help); supplier Management Center references via integration docs (Xola, Ventrata, Bokun articles).
- Klook Help Center / FAQ (klook.com/help-center, klook.com/faq): confirmation timing, open-date vs fixed-date bookings, booking changes & refunds, merchant introduction page (merchant.klook.com).
- Airbnb Help Center: How booking works for hosts of services and experiences (article 1560), Sign up to host an Airbnb Experience (article 3888), Services and Experiences standards and requirements (article 1451), hosting tips (article 3151), host/experiences landing page (fee disclosure).

Research date: 2026-09-10. All key claims below were directly observed in these official sources unless marked otherwise.

## Product A — Viator

### Key observations (evidence layer A)

- Traveler/agent booking flow: search by destination or attraction → filter (operator name, dates, price, duration, rating; specials such as free cancellation, likely to sell out, skip-the-line, private tour) → product detail page with structured sections (tour operator, price and availability, activity details, departure/return logistics, user reviews, traveler photos, inclusions/exclusions, cancellation policy, other important details) → select a **variation** of the product (start times, optional additions, per date and traveler count) → cart → finalize itinerary → confirm → email confirmation.
- "Reserve Now & Pay Later": eligible products can be reserved without immediate payment, payment completed by a listed date.
- Booking management: edit dates, add/remove travelers, change tour option ("different options for the same tour… different start times, inclusions, pickup locations"), cancel, access tickets, contact the tour operator.
- Money: commission calculated from Gross Booking Value, paid the month after the activity is completed; no commission on cancelled bookings; commission on no-shows not cancelled. Commission model implies Viator holds the booking value relationship.
- Supplier side: operators list products via a Supplier Management Center; listing submission fee and per-booking commission reported by a third-party article (layer B, not vendor-primary); reservation-system connectivity (Ventrata/Xola) syncs availability, pricing, bookings, cancellations, voucher/ticket issuance.
- Product catalog scale claims (300,000+ products, 2,500 destinations) appear in marketing surfaces — recorded as vendor claims, not structural facts.

## Product B — GetYourGuide

### Key observations (evidence layer A)

- Supplier onboarding: registration and verification ("Application criteria, documentation"), then creating and managing products ("uploading, editing, product options, quality checks") in a Supplier Portal.
- Booking management: Bookings tab with reference codes and filters; supplier can request cancellation (single or bulk) choosing a reason from defined categories: ordinary operational reasons (guide/driver unavailable, vehicle out of order, activity not accessible, **minimum participants not reached**, activity not offered as described), force majeure (severe vs isolated impact), customer cancellation requests.
- After a supplier cancellation: customers are informed via email and app notification and can **reschedule to a new date or receive a full refund**.
- Payout: "Bookings for Payout" page; suppliers paid monthly or bi-weekly by invoice; payout includes "all active bookings that have traveled" plus cancellation compensations — i.e., payment flows through the platform after travel.
- Connectivity API: availability check → reserve → cancel reserve → book → cancel booking; reservation held for a defined period then auto-released; booking reference persists from reservation through confirmation. This confirms the platform mediates inventory and booking state with the supplier's own system.
- Traveler Help Center topics: plan/search/book, activity information, booking confirmation/voucher/tickets, meeting point and pickup, on the day of the activity, booking management, cancellation, payment and refunds.
- Terms: cancellation conditions live in the supplier's own T&Cs for the activity, the activity description on the platform, or the voucher/ticket — cancellation policy is per-product, surfaced by the platform.

## Product C — Klook

### Key observations (evidence layer A)

- Confirmation model explicitly two-mode: activities with **instant confirmation** (confirmation email within minutes) vs **without instant confirmation** (confirmation within a stated window, e.g. 24–48 hours). The per-activity confirmation mode is shown on the booking/activity page ("Check the package details > Confirmation section").
- Open-date vs fixed-date bookings are a documented distinction.
- Voucher: confirmed bookings produce a voucher; some vouchers are non-transferrable and tied to the guest details entered at booking; in some cases the voucher is issued later by the event organizer after confirmation (fraud prevention).
- Merchant side: merchant.klook.com — activity management (status, content, inventory), booking management (confirm and manage bookings), redemption (validate voucher usage on merchant app or web). Merchant categories: "Things to do" (tours of many types, cruises, costume rentals, indoor/outdoor activities, spas, massages, attractions, theme parks, seasonal leisure), and separately Events (concerts, exhibitions, shows, festivals, marathons); other categories (car rentals, WiFi/SIM, dining, transport) routed to a separate form.
- Traveler side also sells trains, hotels, buses, ferries, eSIM — the experiences marketplace is embedded in a broader travel platform (packaging observation).
- Reviews earn KlookCash (incentivized review layer).

## Product D — Airbnb Experiences

### Key observations (evidence layer A)

- Supply is **application-based and vetted**: host submits listing (type, description, photos, itinerary, pricing) → quality review process → identity verification required before publishing → licenses/insurance proof required for certain activities/locations. Standards require sequenced itinerary activities, minimum photo counts, host expertise, safe venue.
- Booking: guests book available dates; host receives email with guest profile/contact; a **group message thread** is auto-created between host and guests; guests review host requirements before reserving; primary booker may need ID verification within a deadline or the reservation auto-cancels.
- Private groups: booker can reserve all spots; host earns minimum price regardless of group size. Group-size caps documented (private 30, public 200 — vendor-specific numbers, layer A for Airbnb only).
- Money: Airbnb deducts a service fee (stated as 20% on the host landing page) from the payout of every booked experience; host payments/calendar/messages/reservations in one app.
- Experiences live inside the stays platform; experiences can be suggested to guests with upcoming stays (cross-sell surface).

## Cross-product Comparison

| Dimension | Viator | GetYourGuide | Klook | Airbnb Experiences |
|---|---|---|---|---|
| Unit of record on supply side | product with variations (times/options) | product with options; availability via portal or API | activity with packages; confirmation mode per activity | experience listing with sequenced itinerary + calendar |
| Supplier onboarding | supplier Management Center; reservation-system connectivity | registration + verification; product quality checks | merchant registration; category gating | application + vetting + identity verification + licenses/insurance |
| Confirmation model | instant for eligible; Reserve Now & Pay Later variant | booking confirmed via portal/API flow; reserve→book API | instant vs on-request (24–48h window) documented | booking on available dates; auto-cancel if ID not verified |
| Proof artifact | ticket/voucher accessible after confirmation | voucher/ticket; sample voucher documented | voucher, sometimes issued later by organizer | confirmation with meeting details; group message thread |
| Money | platform commission on GBV, paid after travel | payout by invoice after travel; cancellation compensations | platform payment; merchant redemption tooling | platform deducts service fee from host payout |
| Cancellation | per-product cancellation policy surfaced on page | supplier-requested with categorized reasons; customer reschedule-or-refund | booking changes & refunds category; per-activity policy | host requirements; reservation lifecycle in host tools |
| Reviews | user reviews on product page | reviews as product-performance topic | incentivized reviews (KlookCash) | review system inherited from platform |
| Scope drift | travel-agent channel; Tripadvisor integration | connectivity API as first-class supply channel | trains/hotels/buses/eSIM bundled | stays platform cross-sell |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

Three jointly-held structures:

1. **The experience listing of record** — a supplier-authored, bookable description of a tour/activity/experience: what happens, where, how long, what is included, meeting/logistics, pricing per participant, and bookable options (dates/times/variants) with availability. Remove → the supplier's own booking site or a brochure.
2. **The intermediated booking** — a traveler books and pays through the platform; the platform holds the transaction relationship: confirmation flow (instant or on-request), issuance of a voucher/ticket as proof for the day of the activity, policy-governed cancellation/refund, and settlement to the supplier net of the platform's fee. Remove → a review site, a directory, or a lead-gen listing service.
3. **Multi-supplier aggregation with traveler-side discovery** — many independent operators' experiences aggregated in one venue, browsed/searched by destination, category, date; with review/trust surfaces. Remove → a single operator's direct booking channel.

Jointly-held load-bearing: 1 alone = supplier's own reservation system (Tour Operator Management System territory); 2 without 1+3 = generic checkout; 3 without 1 = review/directory platform; 1+3 without 2 = bookable directory with no transaction (lead-gen); 2+3 without 1 = generic travel marketplace selling anything (OTA territory).

Binding: the product sold is a **scheduled experience delivered at a place and time by a local operator** — not lodging, not transport, not arbitrary goods.

### L1 — Common Mature Structure

- Instant confirmation as the dominant mode (with on-request mode retained for supply that must confirm manually).
- Voucher/ticket with redemption scanning (QR codes, ticket scanners in supplier portals/apps).
- Per-product cancellation policies surfaced at booking time; platform-mediated refunds and rescheduling.
- Reviews with ratings on product pages; review incentives in some products.
- Supplier portals: listing/content management, booking management, payout/invoice tracking.
- Wishlist/favorites, traveler messaging with the operator, meeting-point instructions.
- Connectivity integrations with supplier reservation systems (availability/reserve/book/cancel APIs).

### L2 — Variant / Optional Structure

- Supply philosophy: professional tour operators/aggregators (Viator, GetYourGuide, Klook) vs vetted individual hosts (Airbnb Experiences).
- Confirmation timing windows, open-date vs fixed-date tickets.
- Travel-agent/reseller channels (Viator Travel Agent Program with commission tracking).
- Platform bundling: experiences embedded in broader travel platforms (Klook's trains/hotels/eSIM; Airbnb's stays; Tripadvisor's reviews feeding Viator).
- Attraction/theme-park admission tickets and event tickets as product categories inside the marketplace.
- Private-group booking, minimum-participant thresholds, seasonal/force-majeure cancellation handling.

### L3 — Vendor-specific (Research Notes only)

- Viator: Reserve Now & Pay Later; product quality levels and "Improve" tooling; $29 listing submission fee (third-party reported); commission thresholds and payout methods for agents.
- GetYourGuide: bulk cancellation flow with per-reason automatic customer replies; >120-bookings batch limit detail; bi-weekly vs monthly invoice cadence; Easy Acknowledgement button.
- Klook: KlookCash review incentives; eSIM activation flows; category-gated merchant registration form.
- Airbnb: 20% service fee figure; 30/200 group-size caps; co-hosting machinery; ATTA-based outdoor-activity rules.

## Vendor-specific Findings

See L3. None promoted to the canonical core.

## Boundary Findings

- **vs Online Travel Agency / OTA**: OTA's center of gravity is lodging/transport/flights inventory; the tour & activity marketplace binds to scheduled local experiences. Klook straddles by bundling — packaging variant, keep both Types. Remove the experience binding and the intermediated-booking core over aggregated activity supply → generic OTA.
- **vs Attraction Ticketing**: attraction/theme-park admission appears as a product category inside every sampled marketplace (Klook explicitly; Viator sells attraction tickets). Dedicated attraction-ticketing products exist with dated, capacity-based admission inventory as the center of gravity. The marketplace treats admission as one listing type; keep both, flag the overlap zone.
- **vs Tour Operator Management System**: supplier-side system of record (reservations, resources, scheduling, payouts across channels) vs the traveler-facing marketplace. The seam is the connectivity integration (Bokun, Ventrata, Xola sync availability/bookings into the marketplace). Remove the traveler-side discovery/aggregation and you have the supplier system.
- **vs Vacation Rental Marketplace**: stays (per-night lodging inventory) vs scheduled experiences. Airbnb carries both cores in one product — packaging seam, keep both.
- **vs Event Ticketing**: Klook routes events (concerts, shows, festivals) to a merchant category; event ticketing's center of gravity is dated event inventory with seating/entry control, not operator-authored experience itineraries. Overlap zone: ticket experiences for attractions/events.
- **vs Travel Review Platform**: reviews exist in all sampled products but reviews alone (no intermediated booking) = review platform. The intermediated booking leg is what separates them.
- **Decisive test**: remove multi-supplier aggregation → single-operator booking site; remove intermediated payment/booking → directory or review platform; remove the experience binding → generic OTA/marketplace.

## Historical / Market-Sample Check

- The Type is internet-era by origin (aggregation requires a digital venue). Pre-digital analog: destination desks, hotel concierges, and local agencies selling operator vouchers — a listing + on-request confirmation + paper voucher satisfies the core (instant confirmation is not definitional; the on-request pole is in-sample in Klook's own documentation).
- Older/regional products: regional marketplaces and agency-run excursion desks fit the three-leg core without apps, instant confirmation, or review incentives.
- Platform-native variants (Airbnb inside stays; Tripadvisor feeding Viator) fit the core with the marketplace as one surface of a larger product.

## Uncertainties

- Exact commission rates, payout thresholds, and confirmation windows are vendor-specific and time-varying; only Airbnb's 20% service fee and Klook's 24–48h on-request window were directly observed, and both are treated as vendor facts, not Type facts.
- The precise split between "marketplace of record" vs "merchant-of-record" legal posture (who contracts the traveler) varies by vendor and was not uniformly documented; the canonical model deliberately says "platform holds the transaction relationship" without asserting a single legal pattern.
- Viator's listing fee and catalog-scale numbers come from third-party/marketing surfaces — recorded, not relied upon.

## Final Synthesis

A Tour & Activity Marketplace is a two-sided application that aggregates many independent operators' bookable tours, activities, and experiences into one traveler-facing venue, and intermediates each booking: the traveler discovers an experience listing, books a dated option for a party, pays the platform, receives confirmation and a voucher/ticket, and the platform later settles the supplier net of its fee, enforcing per-product cancellation policies along the way. The defining core is the triple: experience listing of record + intermediated booking + multi-supplier aggregation with discovery. Instant confirmation, reviews, scanning redemption, supplier portals, connectivity APIs, agent channels, and platform bundling are common mature or variant structures, not the definition.
