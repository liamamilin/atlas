# Research Notes — Hotel Search / Booking Platform

Research date: **2026-09-08**

---

## Research Goal

Understand, from real products, what a Hotel Search / Booking Platform is: what objects its world is built from, how a traveler moves from "I need a place to stay in X for these nights" to a confirmed booking and an honored stay, what happens when things fail (cancellation, no-show, no room on arrival), and where this Type ends and its neighbors begin (OTA, hotel booking engine, PMS/CRS, metasearch, hostel/vacation-rental siblings, review platforms).

This leaf is the same-architecture sibling of Flight Search / Booking Platform (processed 2026-09-08), whose notes record: "vs Hotel Search / Booking Platform — same architecture (query → priced offers → book/manage), different domain inventory." This pass verifies that claim from the hotel side and establishes what is *hotel-domain-specific* in the shared architecture.

## Initial Boundary

Hypothesis before research:

- Core use: search over bookable accommodation stays across multiple properties/sellers, compare priced stay offers, and convert a selection into a booking (or a directed handoff to a seller).
- Primary users: individual travelers planning and purchasing their own accommodation.
- Nearest neighbors:
  - Online Travel Agency / OTA (multi-product travel retail; hotels often the largest vertical — overlap risk is higher than in the flight case)
  - Flight Search / Booking Platform (same architecture, air inventory)
  - Hotel Booking Engine / Hotel CRS (operator-side component slices — single-property/supplier-side distribution)
  - Hotel Property Management System / PMS (operator-side system of record; demand side writes into it)
  - Metasearch Engine / Vertical Search Engine (§02.02 — search without a booking/handoff path)
  - Hostel Booking Platform (bed-level shared-accommodation semantics, ratified as separate leaf 2026-09-08)
  - Vacation Rental Marketplace / Campground Booking Platform (inventory-character siblings, unprocessed)
  - Travel Review Platform (review/curation without transacted booking)
  - Travel Package Booking Platform (bundle as one priced unit)
- Known unknowns:
  - Does the leaf cover both referral (metasearch-style) and platform-booked poles? (Leaf name's slash suggests both, mirroring the flight leaf.)
  - How does pay-at-property differ structurally from prepaid, and is either definitional?
  - Is booking confirmation a distinct state (booking ≠ confirmed booking)?
  - What does the platform own vs the property (inventory, rate terms, cancellation policy, check-in)?

## Research Questions

1. What does a stay search query consist of (destination, dates, occupancy), and what does it return?
2. What is a stay "offer" — room types, rates, meal plans, cancellation conditions, payment models?
3. Who is the seller of record: the platform (agency/merchant), the property, or a partner? What seller-model poles exist?
4. What happens at booking time (guest data, payment vs guarantee, confirmation, what the property receives)?
5. What is the relationship between booking, confirmation, and arrival (voucher, check-in, no room on arrival)?
6. How do property-set terms (cancellation schedule, payment location, currency) interact with platform-level overlays (reschedule products, guarantees, credits)?
7. What breaks the normal flow (no-show, receptionist can't find booking, property overbooked, dual charges, unpaid prepaid booking)?
8. Where are the boundaries: vs OTA, vs single-property booking engine, vs metasearch-only, vs review-only, vs hostel/vacation-rental siblings?

## Representative Products

Selected for: market representativeness + documentation completeness + different poles/philosophies + different regional layers. Accessibility heavily constrained this pass; see Sources and Uncertainties.

| Product | Pole / layer | Documentation accessed |
|---|---|---|
| Traveloka | generalist travel platform (SEA), hotels as major vertical; platform-booked; strong "Pay at Hotel" support | Help Center — Hotels section: full category tree + article titles (server-rendered); article bodies not individually fetched |
| Trip.com | global generalist OTA (Trip.com Group); platform-booked; hotel & homes vertical | Service Guarantee page (full text: Hotels & Homes guarantees), service pages, site scope |
| Booking.com | global accommodation-centric platform (largest); platform-booked | Official developer portal root (API family taxonomy) only; all content paths consent-walled |

Attempted but not accessible (recorded as source-access limitations; no memory-filled claims used for them):

- Booking.com consumer help + developer docs content — domain-wide PIPL consent wall (same wall recorded by the hostel-booking-platform pass on 2026-09-08).
- Agoda — `/help` 404; `help.agoda.com` rendered empty (JS SPA) three times → abandoned.
- Trivago — `www.trivago.com/en/help` 403; `support.trivago.com` transport error; `company.trivago.com` 403 → abandoned (kills the planned dedicated referral-pole sample).
- Hotels.com — 404/429 (Expedia Group infra; Expedia itself 429'd in the flight pass) → abandoned.
- MakeMyTrip — timeouts ×2 → abandoned. Wego — 403. HotelsCombined — bot wall. Google support/travel — timeout.

The sample is consequently: two strong platform-booked generalist samples (Asia-Pacific + global) plus one limited accommodation-centric giant at portal level. **No referral-pole vendor's consumer help docs were reachable**; the referral pole is evidenced indirectly (see Booking.com observation and Boundary Findings) and is written with reduced assertion strength in the final document.

## Sources

Official surfaces used (all fetched 2026-09-08):

- Traveloka Help Center — Hotels — https://www.traveloka.com/en-en/help/hotel (category tree: Accommodation Booking → Pre Booking / Booking / Post Booking; Product Information → Hotel Information / Villa Information / Pay at Hotel)
- Traveloka Help Center root — https://www.traveloka.com/en-en/help (product taxonomy: Hotels / Flights / Villas / Apartments / Car Rental / Airport Transfer / Xperience / travelokaPay / Insurance / Cruise; "Register Your Accommodation" supply-side link)
- Trip.com — Customer Service Guarantee — https://www.trip.com/pages/customer-service/ (full text: General Service Guarantee; Hotels & Homes — confirmed-booking coordination + Room Guarantee terms; Change and Cancellation Guarantee; Flight-Hotel Cancellation Guarantee; vertical guarantees)
- Trip.com — Service overview — https://www.trip.com/pages/service/ ("once your payment is confirmed, we'll do our best to guarantee your trip"; hotel check-in failure support)
- Trip.com — site scope — https://www.trip.com/ (nav: Hotels & Homes / Flights / Trains / Cars / Attractions / Flight+Hotel packages / Trip.com Rewards; "List your property", "Become a Supplier")
- Booking.com — For developers portal — https://developers.booking.com/ (Demand API; Connectivity APIs — "Enable property owners to manage their properties on Booking.com"; Metasearch Connect API — "Enables metasearch providers to integrate Booking.com's inventory into their products"; Data Portability API)

Evidence discipline:

- **[A]** = directly observed in an official source for a named product (full text).
- **[A-t]** = article/category title directly observed in an official source, body not fetched (title-level evidence: establishes the mechanism's existence, not its parameters).
- **[B]** = observed across ≥2 sampled products.
- **[C]** = canonical inference from comparison + boundary reasoning.

Claims in the final document are calibrated to these layers. Precise numbers (first-night caps, compensation deadlines) stay here in Research Notes only.

---

## Product observations

### Traveloka

Site scope [A]: generalist travel platform — Hotels / Flights / Villas / Apartments / Car Rental / Airport Transfer / Things to Do / travelokaPay / Insurance / Cruise; supply side: "Register Your Accommodation" (tera.traveloka.com landing) [A]; Help Center splits into per-product trees, Hotels being one of the largest [A].

Help Center — Hotels structure [A]: three journey categories — **Pre Booking / Booking / Post Booking** — plus product-information categories (Hotel Information, Villa Information, **Pay at Hotel**). The journey split itself is a structural statement: pre-booking questions (search, price, terms), booking questions (what the price includes, whether the card is charged), post-booking questions (status, voucher, check-in, cancel/reschedule/refund).

Key observed items:

- [A-t] "How to Book a Hotel" — the booking loop is a documented traveler task.
- [A-t] "What does each price include?" (Booking category) — price-inclusion transparency is a standing concern.
- [A-t] "Will my credit card get charged during booking?" + [A-t] "Is it safe to enter my Credit Card details when I book?" (Pre Booking/Booking) — card capture at booking time is part of the flow; the *charge-timing* question exists as a distinct traveler concern → settlement at booking is not the only model.
- [A-t] Pay at Hotel category: "How to Make a Hotel Booking with Pay at Hotel" + "My Credit Card/Debit Card/PayLater Should not be Deducted" → a named pay-at-property model exists in which the card (or PayLater commitment) is captured at booking **but not deducted**; payment happens at the property. The platform documents the "should not be deducted" expectation explicitly — card-as-guarantee semantics.
- [A-t] "Can I pay for my booking by cash at the accomodation?" → cash-at-property is a supported question class (title-level; parameters unknown).
- [A-t] "If I book an overseas accommodation in my country's currency, what currency will I be charged in when I pay for my stay at the accommodation?" → pay-at-property charges occur at the property, in the property's own currency context — booking currency ≠ stay payment currency is a modeled case.
- [A-t] "What does non-refundable or free cancellation mean?" (Pre Booking) → cancellation-condition tiers (free cancellation vs non-refundable) are a first-class rate attribute surfaced pre-booking.
- [A-t] "What will happen if I don't show up at the accommodation during my stay period?" → no-show is a modeled failure class.
- [A-t] "Am I guaranteed to stay at the accommodation that I've booked?" → stay-guarantee framing exists platform-side.
- [A-t] "Requesting an Extra Bed", "How to Make a Special Request… (airport transfer, room with beach view, extra bed)", "Booking a Smoking Room", "Late Check-in", "Hotel Early Check-in", "Breakfast Info for Hotel Booking" → requests/preferences attach to the stay and route to the property (title-level; fulfillment guarantees unknown).
- [A-t] "Room Availability Info", "Choosing Different Room Types in One Booking" → room-type-level inventory; multi-room/multi-type bookings supported.
- [A-t] "Hotel Room for Hourly Usage" → hourly/day-use stays exist as a product form.
- [A-t] "Making a Booking for Villa and Apartment" + Villa Information category → villa/apartment inventory sold through the same hotel-shaped loop.
- [A-t] Post Booking: "Checking Your Booking Status"; "Hotel Voucher Not Received"; "How to Get My Hotel Voucher and Receipt"; "I have successfully obtained my voucher. How can I use it to check in at the hotel?" → the platform issues a **voucher** (plus receipt) that is the check-in instrument at the property.
- [A-t] "Hotel Receptionist Couldn't Find My Booking" → property-side relay failure is a modeled case; platform supports resolution.
- [A-t] "Checking In to a Hotel Booked Under a Different Name"; "I forgot to bring the credit card that I used to make my reservation. Is this OK?" → the stay is anchored to the booker's name and (in pay-at-property cases) the guarantee card; mismatches are real check-in failure modes.
- [A-t] "How to Cancel and Get a Refund for My Hotel Booking"; "Refund Hotel Booking for Non Refundable Policy"; "How to Reschedule My Hotel Booking"; "Hotel Rescheduling Fees"; "How to Reschedule a Non-refundable Hotel Booking"; "How to check refund status"; Easy Reschedule articles → post-booking change machinery with fee/refund semantics and a branded reschedule product.
- [A-t] "Can I transfer my accommodation booking to someone else?" → guest-change path exists (title-level).
- [A-t] "I've made a payment, but the accommodation charged me with some additional fees to my credit card. What should I do?" → **dual-charge disputes** (platform paid + property charged) are a modeled money-conflict case.
- [A-t] "I have booked a Flight + Hotel package and changed my flight schedule. Will the changes be automatically applied to my hotel booking?" → cross-vertical (package) linkage exists.
- [A-t] Product Information — Hotel Information: "Submitting a Hotel Review", "Writing a Helpful Review", "Posting a Photo Review", "Review Moderation by Traveloka", "Review Not Published" → review system exists with moderation; (review gating to completed stays not verifiable from titles alone — kept weak).
- [A-t] "StayGuarantee Claim" → branded stay-guarantee product exists.
- [A] "How to Register My Property on Traveloka" → supply-side onboarding is an official flow (property registration portal).

Not observed: referral/handoff-mode behavior; Traveloka books its own inventory (platform-booked pole).

### Trip.com

Site scope [A]: global generalist — Hotels & Homes / Flights / Trains / Cars / Attractions & Tours / Flight+Hotel packages / Trip.Planner; loyalty program (Trip.com Rewards); supply side: "List your property", "Become a Supplier" [A].

Service Guarantee — Hotels & Homes [A, full text]:

- **Confirmed-booking coordination**: "If your booking is changed after it is confirmed, Trip.com will do its best to coordinate your stay." If "after a stay booking has been confirmed but before you arrive at the property, the property can no longer arrange check-in" → platform notifies the traveler, works with the property for a room "of the same or higher standard", compensates cost differences up to the first night's room fee; if no room at the original property, arranges a nearby property of the same standard with the same cap.
- **No room on arrival (Room Guarantee)**: if the booking is confirmed but no room at arrival → contact platform immediately; platform negotiates same-or-better room / nearby property; pays differences up to first night's rate; compensation processed within one working day after check-out on verified claims (numbers = product-specific, kept out of the final document).
- Room Guarantee exclusion conditions [A — each is a structural fact about the model]:
  - "Your booking has **not been confirmed** by Trip.com by the time you arrive" → **a booking exists separately from its confirmation**; confirmation is a distinct state with arrival-time significance.
  - "Your booking is a **prepaid** booking and you have not completed payment" → prepaid settlement requires completed payment; a non-prepaid (pay-at-property) class exists by contrast.
  - "You do not arrive at the hotel by the arranged time" → arrival by the arranged time matters (no-show-adjacent).
  - "You changed booking information, such as room type or check-in/out dates, without getting confirmation from Trip.com" → self-made changes without platform confirmation void protections → **modifications route through the platform**.
  - Upgraded free of charge by platform/hotel → guarantee discharged.
  - Force majeure → excluded.
  - "Bookings with transaction security issues": fake bookings, resale bookings excluded; "the supplier reserves the right to require the user to provide a **guarantee amount** for bookings when there are issues or abnormalities with the user information, user account, or number of transactions. If the guarantee amount cannot be provided, Trip.com reserves the right to **cancel the user's booking on behalf of the supplier**" → supplier-side risk posture; the platform can cancel on the supplier's behalf.
- **Change and Cancellation Guarantee** [A]: "Trip.com does not earn profits from or add additional charges to change and cancellation fees. If you need to cancel your booking, Trip.com will communicate with the hotel to try to reduce your cancellation charges as much as possible." → cancellation charges originate in the **hotel's** terms; the platform mediates.
- **Flight-Hotel Cancellation Guarantee** [A]: involuntary flight change preventing arrival on check-in date → free hotel cancellation before/on check-in date → cross-product linkage as a productized guarantee.
- General [A]: 24/7 support with dedicated "flight and hotel" specialists; "once your payment is confirmed, we'll do our best to guarantee your trip"; "If you find yourself unable to check-in for your hotel because of an issue with Trip.com or one of our suppliers, reach out to us" → the platform stands behind the property-side delivery of the stay.

Not observed: referral-mode behavior; Trip.com books its own inventory (platform-booked pole).

### Booking.com (limited — portal-level only)

- [A] Official developer portal documents the platform's API families, which mirror the Type's structure from the operator's mouth:
  - **Demand API** — "Unlock a world of travel through Booking.com's extensive supply of experiences and offerings" → demand-side distribution of aggregated supply.
  - **Connectivity APIs** — "Enable property owners to manage their properties on Booking.com" → property-side connection (inventory/rates/reservation exchange), confirming that the property retains and manages its own inventory and that the platform is the demand intermediary.
  - **Metasearch Connect API** — "Enables metasearch providers to integrate Booking.com's inventory into their products" → official confirmation that **referral/metasearch surfaces exist in the hotel domain and point into the same platform inventory** (the referral pole's supply side), even though no referral-pole vendor's consumer docs were reachable this pass.
- [A] Self-description: "making it easier for everyone to experience the world" (positioning-level only).
- Source-access limitation [recorded]: every content path (`/demand/docs`, `open-api/about-api-references`, consumer help, customer-service pages) is behind a domain-wide PIPL consent wall; identical wall recorded by the hostel-booking-platform pass. No consumer-operational claims are made for Booking.com in the final document beyond portal-level facts.

---

## Cross-product Comparison

| Dimension | Traveloka | Trip.com | Booking.com (portal) | Strength |
|---|---|---|---|---|
| Domain objects | hotels + villas + apartments (room types, stay dates) | hotels & homes (stays) | accommodation supply ("extensive supply") | B |
| Multi-property aggregation | yes (booking platform across properties) | yes | yes | B |
| Platform-booked pole | yes (voucher issued; platform payment flows) | yes (payment-confirmed guarantee; compensation) | yes (Demand API = its own booking distribution) | B |
| Referral pole | not observed | not observed | Metasearch Connect API: metasearch providers integrate Booking.com inventory | A (supply-side existence only) — weak for consumer side |
| Search query shape | destination + dates + occupancy implied by help topics (room types, availability) | stays implied; not article-documented this pass | portal only | A-t (weak) |
| Booking ≠ confirmation | booking status article; receptionist-can't-find case | explicit: guarantee void if "booking has not been confirmed by the time you arrive" | — | B |
| Prepaid vs pay-at-property | "Pay at Hotel" named model; card "should not be deducted"; cash-at-property; property-currency charging | "prepaid booking and you have not completed payment" exclusion (implies non-prepaid class); payment-confirmed guarantee | — | B |
| Card at booking | card entry safety + forgotten-card check-in case | supplier may require guarantee amount | — | B |
| Voucher/check-in instrument | voucher + receipt articles; check-in with voucher | check-in proof requirements in guarantee terms | — | B |
| Property-set cancellation terms | free-cancellation vs non-refundable tier article; reschedule fees; non-refundable reschedule case | "communicate with the hotel to try to reduce your cancellation charges" (charges originate with hotel) | — | B |
| Platform stands behind property delivery | stay-guarantee framing; dual-charge dispute path; receptionist-can't-find support | confirmed-booking coordination; Room Guarantee; check-in failure support | — | B |
| No-show | dedicated article | "do not arrive by the arranged time" exclusion | — | B |
| Stay-anchored reviews | submit/moderation/not-published articles (titles) | not sampled | — | A-t (single product; weak) |
| Special requests to property | extra bed / view / transfer / smoking / late check-in (titles) | not sampled | — | A-t (single product; weak) |
| Multi-room / room-type choice | different room types in one booking (title) | not sampled | — | A-t (single product; weak) |
| Hourly/day-use | dedicated article (title) | not sampled | — | A-t (single product; weak) |
| Supply-side onboarding | "Register My Property" article | "List your property", "Become a Supplier" links | Connectivity APIs for property owners | B |
| Cross-vertical drift | flights/villas/cars/insurance/pay | flights/trains/cars/attractions/packages | Demand API covers "experiences and offerings" | B |
| Loyalty program | travelokaPay ecosystem adjacent (not hotel-loyalty-specific in sample) | Trip.com Rewards | — | A per product (variant) |
| Branded guarantees/products | StayGuarantee; Easy Reschedule | Room Guarantee; Flight-Hotel Cancellation Guarantee; Special Circumstance coverage | — | A per product (variant/L3) |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (jointly held; smallest structure)

1. **Accommodation-stay inventory as the domain.** The platform's world is built from properties offering bookable stays — room types/units available for stay dates, priced as rates. Remove → the product is no longer about accommodation at all.
2. **Multi-property aggregation.** Offers are drawn from more than one property and/or more than one seller, brought side by side in one place. Remove → it becomes a single property's own direct sales channel (hotel booking engine territory), not a platform.
3. **Structured stay search.** A query keyed by destination, stay dates, and occupancy produces a comparable set of priced stay offers. Remove → a browsing catalog, directory, or fare/price-information page.
4. **Selection-to-booking path.** Selecting an offer leads either to a booking completed through the platform (guest data → payment or payment/guarantee terms → confirmation → reservation record delivered toward the property) or to a directed handoff to the named seller that will complete it. Remove → a price-comparison/review surface.

The leaf name's slash ("Search / Booking") corresponds to the two poles of leg 4 (referral vs platform-booked); both satisfy L0. What both poles share: the platform is where selection happens, and the traveler leaves it only toward a specific purchase.

Jointly-held is load-bearing: 1+3 without 2 = single-property booking engine; 2+3 without 1 = generic metasearch/shopping; 1+2 without 3 = directory/listings; all without 4 = review/comparison media.

### L1 — Common Mature Structure (not definitional)

- Comparison machinery: filtering and sorting by price, rating, location, amenities, property class/type.
- Price-inclusion transparency: what the rate includes (taxes, breakfast/meal plan) as a standing display concern.
- Room-type-level offer display within a property; multi-room/multi-type bookings.
- Guest-data capture at booking: guest names, contact, arrival information; special requests attached to the booking (view, transfer, extra bed, late check-in) — requests, with property-dependent fulfillment.
- Booking-status surface; confirmation as a distinct tracked step; platform-issued voucher/receipt used at check-in.
- Post-booking change machinery: modify dates/room types (through the platform), cancel per the rate's cancellation schedule (free-cancellation tiers vs non-refundable), refund status tracking.
- Payment/guarantee capture at booking (card entry), with prepaid vs pay-at-property settlement models.
- Support surfaces for stay-time failures: booking not found at the property, no room on arrival, dual charges, check-in name/card mismatches.
- Stay-anchored review system with moderation.
- Supply-side onboarding/property portal (the demand platform's complement).
- Cross-vertical drift: flights, cars, attractions, insurance, payment wallets on the same platform.

### L2 — Variant / Optional Structure

- Seller-model pole: platform-booked (agency-of-record or — asserted weakly, not directly sampled — merchant/consolidator) vs referral/metasearch handoff.
- Settlement-model mix: prepaid-dominant vs pay-at-property-dominant (market- and product-dependent); cash-at-property in some markets; property-currency charging for overseas stays.
- Property-type breadth: hotels as the core; villas, apartments, homes, resorts commonly included (hostels and campgrounds are separate sibling Types by their unit semantics).
- Day-use/hourly stays.
- Loyalty/subscription programs operated by the platform (widespread among the largest products, absent in many others).
- Branded guarantee/reschedule products and platform credits.
- Regional realizations: payment rails, currencies, languages, jurisdiction-specific consumer rules.
- Corporate/B2B booking postures (not sampled; recorded as variant with no structural claims).
- Adjacent poles outside the Type: single-property direct channels (booking engine); review-only platforms; pure metasearch without a booking/handoff path (§02.02).

### L3 — Vendor-specific (kept out of final document; listed for evidence)

- Trip.com: Room Guarantee exact terms (first-night cost cap, one-working-day compensation window, contact-immediately requirement, exclusion list), Flight-Hotel Cancellation Guarantee, Special Circumstance Cancellation coverage, Trip.com Rewards, "Hotels & Homes" naming.
- Traveloka: Pay at Hotel naming and "should not be deducted" article, Easy Reschedule, StayGuarantee, Clean Accommodation program, travelokaPay, hourly-usage product, villa/apartment verticals.
- Booking.com: Demand API / Connectivity / Metasearch Connect API naming; Genius loyalty (not sampled this pass).
- All specific numeric limits, deadlines, fee schedules, and program names — not asserted in the final document.

## Rejected Findings (candidates that failed the tests)

- "Reviews are definitional" — rejected. Review-only surfaces exist (Travel Review Platform) without transacted booking; the discriminator for this Type is the booking path, not reviews. Reviews stay L1, and single-product here (A-t).
- "Pay-at-property is definitional" — rejected. Prepaid-only and pay-at-property-dominant realizations both exist; settlement model is L2. What is structural is that *payment/guarantee terms are captured at booking and settlement may occur at the property* — i.e., the property is a money-handling party to the stay. (Trip.com + Traveloka [B].)
- "The platform owns the room inventory" — false. The property retains and manages its own inventory (Booking.com Connectivity APIs [A]; property-set terms [B]). The platform holds bookable offers and relays reservations. Kept as an Important behavior, not ownership.
- "The platform sets the cancellation policy" — false as stated: charges originate in the property's rate terms; the platform displays, enforces mechanically, and mediates (Trip.com "communicate with the hotel to reduce your cancellation charges" [A]). Platform overlays (branded tiers) exist only where the platform books.
- "Map search / price alerts are definitional" — no direct evidence fetched this pass; common-market assumptions only → excluded from the final document.
- "Hotel metasearch is a different Type" — rejected for this leaf, mirroring the flight pass: the leaf name covers both poles, and the referral pole shares the full accommodation-domain structure; the true boundary is against domain-agnostic vertical search without a booking/handoff path (§02.02).

## Boundary Findings

- **vs Online Travel Agency / OTA.** Same market space; center-of-gravity seam, exactly as the flight pass recorded for its own sibling. A hotel search/booking platform's search/book/manage loop is organized around accommodation stays; an OTA's center of gravity is multi-product travel retail (hotels one vertical, often the largest). In practice the sampled generalists (Traveloka, Trip.com) are OTAs whose hotel verticals exhibit the full hotel-domain structure — the Type is realized inside them. **Joint review recommended from the OTA pass (leaf unprocessed).**
- **vs Flight Search / Booking Platform.** Same architecture (query → priced offers → book/manage), different domain inventory and different stay semantics: room-type × stay-dates × occupancy instead of air segments; no PNR/e-ticket analogue — instead a voucher honored at a physical property; no ticket issuance — instead booking confirmation distinct from payment and from the stay itself; disruption is property-side (no room, can't find booking) rather than carrier-side; settlement can land at the property.
- **vs Hotel Booking Engine / Hotel CRS.** Single-property (or single-supplier) selling surfaces — the "1+3 without 2" case. The PMS pass (2026-09-08) already held CRS/booking-engine/channel-manager as component slices with the ARI-out/reservations-in hand-off; this leaf is the multi-property demand side that those slices feed. Remove multi-property aggregation → booking engine. **Joint review note for the unprocessed hotel-booking-engine and CRS leaves.**
- **vs Hotel Property Management System / PMS.** Operator-side system of record (inventory truth, stay operation, folio) vs traveler-facing demand side. The platform's reservation *arrives into* the PMS/CRS world; it never operates the stay.
- **vs Metasearch Engine / Vertical Search Engine (§02.02 family).** The referral pole is *also* vertical search, but this leaf requires accommodation-domain inventory plus the selection-to-booking path and stay-service responsibilities (cancellation/status/voucher support). A product that only ranks accommodation offers without a booking/handoff path belongs to §02.02 — consistent with the metasearch pass's ratification ("travel metasearch… realized under §26 leaves when [domain objects + booking/handoff paths] are present"). Removal test: remove the booking/handoff path → metasearch engine.
- **vs Hostel Booking Platform.** Hostel leaf centers the shared dorm bed sold per bed to individuals (bed-level semantics ratified 2026-09-08). This leaf centers room/unit-level stays at properties. Generalist hotel platforms carry hostel properties without moving the Type; bed-level specialization is the sibling.
- **vs Vacation Rental Marketplace / Campground Booking Platform (unprocessed).** Traveloka/Trip.com sell villas, apartments, and "homes" through the same hotel-shaped loop [B] — so "alternative accommodation sold hotel-style" sits inside this Type. The sibling leaves presumably center individually-hosted units (owner-host relations, site-level inventory). **Flag for joint review when those passes run** — the seam candidate is "property-operated accommodation sold by rate" vs "individually hosted units / owner-mediated stays."
- **vs Travel Review Platform.** Reviews without a transacted booking are a different Type. Stay-anchored reviews inside a booking platform are L1 structure.
- **vs Travel Package Booking Platform.** Packages price flight+accommodation as one unit; here the stay is priced as its own object (cross-vertical linkage and package products exist without moving the Type [B]).

**"去掉什么就变成另一个 Type" summary:** remove accommodation-domain inventory → generic OTA/metasearch; remove multi-property aggregation → hotel booking engine; remove structured stay search → directory/listings; remove booking/handoff path → metasearch or review platform.

## Historical / Market-Sample Check (per §24 reasoning)

- Would older products fit? Web-era hotel booking platforms from the late 1990s onward (the largest accommodation-centric platform itself dates to 1996) already exhibit all four L0 structures: multi-property search by destination and dates, priced room offers, platform booking with confirmation, property-set cancellation terms, prepaid and pay-at-property settlement. The referral pole (hotel metasearch, mid-2000s) likewise predates modern features. None of reviews, loyalty programs, map search, mobile apps, or wallets is required — all are later layers.
- GDS-era and call-center/agency hotel reservation systems are operator/agent-side ancestors, correctly outside this traveler-facing Type (same exclusion shape as the flight pass's airline-direct exclusion).
- Regional products (the sampled Asia-Pacific generalists are exactly this) fit the same L0; the missing European/American consumer docs are a sample bias, not a structural doubt.
- The check passed without weakening L0; no further abstraction was needed. The only structural risk — overfitting to the platform-booked pole — is handled by the leaf-name slash (both poles satisfy leg 4), mirroring the flight pass.

## Uncertainties

1. **Referral pole under-evidenced on the consumer side.** Trivago, Wego, HotelsCombined, Kayak, Google all unreachable; the pole is evidenced by Booking.com's official Metasearch Connect API (supply-side existence) and the metasearch pass's ratification. Consumer-side referral behaviors (how handoff pages work, price-comparison UX) are written weakly in the final document.
2. **Booking.com consumer documentation unreachable** (domain-wide consent wall; same as hostel pass). Its market-shape claims (largest accommodation platform) are common knowledge but were not re-evidenced this pass; the final document uses it only as a representative-product name plus portal-level facts.
3. **Merchant vs agency model under-documented.** No sampled product documented buying-and-reselling terms directly; seller-model variety is mentioned with weak wording.
4. **Search-result mechanics** (ranking, map views, price display with/without taxes) not article-documented; no precise claims made.
5. **Review gating** (reviews only after completed stays) suspected but not verifiable from titles; kept weak ("stay-anchored review system with moderation" — moderation is [A-t], gating is inference).
6. **Special-request fulfillment**, **hourly stays**, **multi-room bookings** — Traveloka title-level only; written as variants/options without parameters.
7. **Corporate/B2B variant** not sampled.

## Final Synthesis

A Hotel Search / Booking Platform is the traveler-facing application layer for accommodation acquisition. Its defining core is jointly held: (1) an inventory of bookable accommodation stays — room types at properties, available for stay dates, priced as rates; (2) aggregated across multiple properties and/or sellers; (3) reached through structured stay search keyed by destination, dates, and occupancy; and (4) closed by a selection-to-booking path that either completes the booking on the platform (guest data → payment or guarantee → confirmation → reservation delivered toward the property, commonly with a voucher) or hands the traveler to the named seller. What is hotel-domain-specific in this shared architecture: the property is a party to the stay (it sets the rate's cancellation/payment terms, receives the reservation, honors the stay at check-in); settlement may land at the property (prepaid vs pay-at-property); confirmation is a distinct state between booking and arrival; the platform stands behind property-side delivery with guarantees/mediation; and the stay-anchored post-stay layer (voucher, reviews, dispute paths) closes the loop. Everything else — comparison machinery, price-inclusion display, loyalty programs, branded guarantee/reschedule products, day-use, cross-vertical drift — is mature-market structure layered on that core, and specific vendor terms remain vendor detail.
