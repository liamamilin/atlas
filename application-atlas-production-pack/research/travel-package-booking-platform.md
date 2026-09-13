# Research Notes — Travel Package Booking Platform

Research date: **2026-09-09**

## Research Goal

Understand what a Travel Package Booking Platform actually is as an Application Type: what the unit of sale is, what objects make up its world, how a package booking flows from search to travel documents, what rules govern it, and where its boundaries lie against component booking (OTA), activity booking, and operator-side tour systems.

## Initial Boundary (hypothesis before research)

- Core use: consumers book a **pre-assembled bundle of travel components** (accommodation + transport, or accommodation + guided/tour content) as **one product at one price**, for a specific departure date and a traveler party.
- Likely users: leisure travelers (a lead booker organizing a party).
- Nearest neighbors: Online Travel Agency / OTA (component booking), Tour & Activity Marketplace (single experiences), Tour Operator Management System (operator-side), Vacation Rental Marketplace (single accommodation), Travel Itinerary Planner (no transaction).
- Suspected boundary: **the unit of sale** — bundle vs single component.
- Unknowns: how dynamic packaging (OTA-style flight+hotel bundles) realizes the model; payment schedules; document issuance; change/cancel rules; whether escorted-tour operators and dynamic-packaging OTAs share one core.

## Research Questions

1. What exactly is a "package" in each product — which components, how is it defined, what does the price include?
2. How is pricing structured (per person vs per room, occupancy/share logic, supplements)?
3. What is a "departure" — a dated instance of a package? What availability states exist?
4. What does the booking contain and how does it flow (search → configure → book → confirm → pay → documents)?
5. What payment terms exist (deposit + balance, holds/options, pay-in-full)?
6. What travel documents are issued, when, and gated on what?
7. How do changes, cancellations, and add-ons work (deadlines, component rules)?
8. What surfaces exist (catalog, package detail, dates & pricing, checkout, manage-booking, agent portal)?
9. What do vendors themselves treat as NOT a package (à-la-carte components)?
10. Do fixed-departure escorted tours and dynamic flight+hotel bundles share the same core structure?

## Representative Products

Selected for market representation + different product philosophy + different customer tier:

| Product | Pole | Customer tier | Evidence tier reached |
|---|---|---|---|
| G Adventures | small-group escorted tour operator (fixed departures, land packages) | consumer direct + agent channel | Tier 1 (FAQs: general + booking) |
| Trafalgar | premium escorted guided-vacation operator (fixed departures, flight-optional) | consumer direct + agent channel | Tier 1 (FAQs: before-you-book + before-you-travel) |
| Delta Vacations | airline-led vacation packages (flight + hotel + car/activities, dynamically composed) | consumer, loyalty members | Tier 2 (official product pages) |
| Air Canada Vacations | tour-operator/wholesaler packages (all-inclusive, tour, flight & hotel, flight & cruise) | consumer, loyalty members, advisor channel | Tier 2 (official product pages; sub-pages redirect) |
| Trip.com | global OTA carrying packages alongside components | consumer | Tier 2 (help/contact page + site navigation structure) |

Deliberately attempted and blocked: TUI (403 ×1 + domain-level block), Costco Travel (403 ×2), Jet2holidays (timeout ×2), Expedia support (transport error + 429 ×2), On the Beach (403), Loveholidays (403). See Source-access Limitation below.

## Sources

- G Adventures — General FAQs: https://www.gadventures.com/faqs/ ; Booking FAQ: https://www.gadventures.com/faqs/booking-related/ (fetched 2026-09-09)
- Trafalgar — FAQ hub: https://www.trafalgar.com/en-us/frequently-asked-questions ; Before you book: https://www.trafalgar.com/en-gb/frequently-asked-questions/before-you-book ; Before you travel: https://www.trafalgar.com/en-gb/frequently-asked-questions/before-you-travel (fetched 2026-09-09)
- Delta Vacations — official product site (homepage + Why Choose / SkyMiles sections): https://www.deltavacations.com/ → delta.com/us/en/delta-vacations (fetched 2026-09-09)
- Air Canada Vacations — official product site: https://www.aircanadavacations.com/en (fetched 2026-09-09; FAQ/manage-booking sub-paths serve the SPA homepage to the fetcher)
- Trip.com — help/contact page: https://www.trip.com/help/ (fetched 2026-09-09; site navigation shows package vs component taxonomy)

**Source-access Limitation:** the large dynamic-packaging OTA products (Expedia, Loveholidays, On the Beach) and the two largest integrated European operators (TUI, Jet2holidays) refused automated access. Findings about the dynamic flight+hotel bundle shape therefore rest on weaker evidence (Tier 2 vendor positioning from airline-led and OTA-carried packages) and are flagged where relevant. No precise operational details for those poles are asserted.

---

## Product A — G Adventures (small-group escorted tour operator)

### Key observations (Layer A unless noted)

- The product of record is the **trip/tour**: a named multi-day itinerary with a defined route, duration, inclusions ("Included Highlights" listed per trip page), and a Trip Details document (packing list, tour-specific info).
- **Land-only package**: "Do your tours include international airfare? …it is not possible to include international airfare in our prices. We would be happy to help you arrange flights. Just ask for an air quote when making your booking." → flights are an optional add-on quote, not part of the package.
- **Group-size and per-person twin-share pricing culture**: group sizes bounded (≤15 typical); solo travelers share rooms with same-sex travelers; optional "My Own Room" add-on at extra cost; single supplements on some tours.
- **Departure-based availability with confirmation lag**: "availability listed on our website is updated regularly, however on some tours we must confirm arrangements with our local operations on the ground, a process which usually takes no more than 24 to 72 hours. When you book online you will receive a follow-up email confirming your arrangements… We strongly recommend that you do not make any other non-refundable travel arrangements until you receive confirmation." → booking request vs confirmed state.
- **Guaranteed departures**: every departure "guaranteed to run" once booked and paid (vendor-specific policy: G Adventures states all departures are guaranteed).
- **Booking hold mechanism**: "Holding an Option" = reserve space without payment for up to 48 hours; expires and space released unless confirmed; booking reference number issued at option time.
- **Booking data set**: full passport name, passport number/expiry/place of issue, nationality, mailing address, date of birth, occupation, emergency contact name and phone, medical/dietary requirements, credit card → per-traveler identity data required to confirm.
- **Deposit + balance**: "The most up to date information on deposit amounts and full payment dates can be found on our Booking Terms and Conditions" → scheduled payments keyed to booking terms; pay-in-full allowed.
- **Documents**: all documentation electronic; "Shortly after we receive your payment we will send you your initial documents. Final documentation will be sent by email no later than two weeks prior to the departure." Starting/ending hotels listed on the **travel voucher**.
- **Add-ons with amendment windows**: extra services can't be added within 10 days of departure; recommended adding ≥30 days prior; amendment fees apply 30–10 days out (product-specific numbers). Extra pre/post tour hotel nights bookable outside 30 days of departure.
- **Insurance requirement**: medical travel insurance with minimum evacuation coverage required; proof checked on Day 1 (product-specific policy).
- **Participation rules**: cannot join late / leave early without own arrangements and costs; age minimums; medical questionnaire for pre-existing conditions.
- **Agent channel**: dedicated travel-agent booking path ("have your agent give us a call"; agent login/registration portal).
- Cancellation possible with penalties per booking T&Cs.

## Product B — Trafalgar (premium escorted guided vacations)

### Key observations (Layer A unless noted)

- **Per-person twin-share pricing**: "The price listed is per person twin-share (two guests sharing a room…)… If you're travelling solo, solo pricing will be displayed during the first step of the booking process once you select your departure on our website." → occupancy resolved inside the booking flow.
- **Inclusions/exclusions as the package definition**: included = all accommodation, meals per itinerary, Travel Director + Driver for the journey, porterage and restaurant gratuities, hotel tips/charges/taxes, sightseeing per itinerary, complimentary scheduled coach transfers; not included = flights to/from start (bookable through them), pre/post hotel nights (addable during booking), Optional Experiences (paid on tour), visas, insurance.
- **Departure availability states** shown on dates & pricing: **'Definite departure'** (minimum guests reached, guaranteed to go), unmarked (may change), **'Call Us'** (almost fully booked; must confirm availability by phone/agent), **'On Request'** (continue with booking request; "highly likely… confirmed within 24-72 hours") → the same request→confirm lag pattern as G Adventures.
- **Booking hold**: "free courtesy hold your booking for up to 3 days" for most departures; Last Minute Deals or bookings inside the full-payment window must be paid in full at booking.
- **Room configuration rules by party composition**: children 5–17; triple rooms for two adults + one child; family of four needs two twin rooms; three adults recommended two rooms (third bed is rollaway); room options shown per group size on Trip Overview.
- **Solo handling**: solo room share (same-gender twin share, regional availability) vs solo room with supplement.
- **Flights as optional attachable component**: "you can add flights to your booking during the booking process (subject to availability)"; changes subject to airline rules and fees; airline seat selection subject to airline T&Cs; some itineraries include internal flights in the package.
- **Transfers as add-on**: complimentary shared coach transfers bookable at booking or later via portal "no later than 21 days before your arrival" → add-on amendment deadline.
- **Pre/post nights as add-on**: extra hotel nights before/after the tour addable at booking or later via portal/agent.
- **Deposit + balance keyed to trip level**: "Your trip deposit amount depends on your trip level" (Trip Deposit Levels page); payment dates and amounts appear on the **invoice** after booking; deposit and full-payment terms may vary for special offers.
- **Deposit protection**: tour-only deposits non-refundable but reusable toward a future trip within five years (product-specific).
- **Payments**: balance paid in My Trafalgar Travel Portal; one-time secure payment links; phone; agent portal for agents. Payment methods listed (cards, PayPal).
- **Changes/cancellations keyed to payment milestones**: "You're able to change your travel plans up until your final payment is due. However, if you're within your booking's cancellation period, additional charges will apply." Airline component has separate policies. Name changes: tour-only by email; tour+flights by phone (airline rules). Bookings non-transferable; new guests treated as new bookings.
- **Mandatory guest portal + data completion gates documents**: "We require all guests to create and complete their own personal My Trafalgar Travel Portal Account" (passport, contact details, emergency contact); "Your Travel Documentation cannot be issued until all details within your account are complete." Children's details attach to the lead booker.
- **Document issuance timing**: e-travel documents available ~21 days/3 weeks before departure in the portal; transfer meet details in travel documents; Travel Director introduction ~10 days before, final meet details ~3 days before (product-specific timings).
- **Optional Experiences**: on-tour paid add-ons, not pre-bookable (product-specific policy).
- **Group booking variant**: groups of 9+ get group modes — book spaces on existing tours, exclusive departure, or custom itinerary (15+); past-guest loyalty discount across sister brands; newsletter travel credit with combinability restrictions.
- **Insurance**: recommended; purchasable at booking ("automatically added to your booking") or after.
- **Advisor channel throughout**: every operation (booking, payments, transfers, extra nights) documented for both direct guests and travel agents; Agents Login portal.

## Product C — Delta Vacations (airline-led vacation packages)

### Key observations (Tier 2 — official product pages)

- Positioning: "Book vacation packages all in one place while you unlock savings, earn miles and more." Package = "a curated selection of hotels, rides and activities, paired with your Delta® in-flight experience… booked all in one place."
- **Explicit internal boundary**: "Not Looking for a Vacation Package? Find what's right for you with a-la-carte travel products." → Delta Stays (hotels only), Delta Cars (cars only), Delta Cruises as separate surfaces. The vendor itself separates package sale from component sale.
- Loyalty integration: earn miles + MQDs (Medallion status credit) on packages; use miles to pay; status-attainment marketing tied to package purchase (product-specific).
- Support promise spans pre-trip choice, changes, and on-trip help ("From choosing the right vacation to making changes or getting help on your trip").
- Travel-agent channel exists (agency site link).
- Curated-vacation-itineraries (e.g., 7-day Maui itinerary) as inspiration content feeding bookable packages.

## Product D — Air Canada Vacations (tour-operator packages)

### Key observations (Tier 2 — official product site)

- Package family taxonomy in the booking nav: **All-inclusive, Tour packages, Flight & Hotel, Flight & Cruise, Groups, Special event trips** — while **Flights** and **Car rentals** are external-site links and **Hotels** has its own booking option. Again the vendor's own split: package types vs component/adjacent booking.
- Per-person/per-pair promotional pricing culture: "Up to 50% off the 2nd traveller", "Save $600 per pair", "$200 off per pair", "1st child stays free at select resorts" → party-composition-sensitive pricing.
- Loyalty: Aeroplan points earn on flight-inclusive packages; online points redemption for packages (product-specific).
- "Manage your booking", "Booking History" for logged-in users; **Advisor access** with Travel Agent sign-in and **Group Quoting Tool** → agent channel + group quoting as a distinct operation.
- Payment flexibility marketed: "Book now, pay over time" (flexible payment options page); "Cancel with a full refund" tied to travel protection (product-specific packaging).
- Inclusion marketing: "1st checked bag + 1 carry-on included & more" → inclusions (baggage) as package content.
- Long stays, collections (Luxury/Adults only/Family), brochure culture ("Sun Guide").

## Product E — Trip.com (global OTA carrying packages)

### Key observations (Tier 2 — help/contact page + navigation structure)

- Site navigation separates **"Flight + Hotel"** (a /packages/ surface) and **"Private Tours" / "Group Tours"** (/package-tours/) from à-la-carte Hotels, Flights, Trains, Cars, Attractions & Tours → the vendor's own package-vs-component taxonomy.
- Support lines distinguish "Flight & hotel bookings" from "Other bookings" in several regions' phone support hours → packages treated as a distinct booking category operationally (evidence of separation, not of internal mechanics).
- No operational package-booking detail reachable in this pass (help center did not expose package articles to the fetcher).

## Cross-product Comparison

| Structure | G Adventures | Trafalgar | Delta Vacations | Air Canada Vacations | Trip.com | Strength |
|---|---|---|---|---|---|---|
| Package as named unit of sale with defined inclusions | trip with "Included Highlights" | tour with included/not-included list | "curated selection… paired with your in-flight experience… all in one place" | All-inclusive / Tour packages / Flight & Hotel / Flight & Cruise | "Flight + Hotel" + Private/Group package tours | Core (A+B direct, C+D+E positioning) |
| Multi-component bundle sold as ONE product at one price | yes (land package; flights quoted separately) | yes (flights optional add-on) | yes (flight+hotel+car/activities) | yes (flight+hotel, all-inclusive) | yes (flight+hotel; escorted group tours) | Core |
| Dated departure as bookable instance | fixed departures; guaranteed-to-run policy | fixed departures with availability states | date range search (dynamic) | date-driven deals/packages | date-driven bundles | Core (A+B direct; C/D/E implied by date search) |
| Availability states incl. request-based confirmation | website availability + 24–72h ground confirmation | Definite / Call Us / On Request | not observed (Tier 2) | not observed | not observed | Common (A+B); request-lag unobserved at bundle poles |
| Traveler party + occupancy config (rooms, adults/children, supplements) | twin-share, My Own Room, single supplement | per-person twin-share, triple/room rules, solo options | not directly observed | per-pair/2nd-traveller promos, child pricing | not directly observed | Common (A+B strong; D pricing promos) |
| Deposit + balance payment schedule | deposit + full-payment dates in T&Cs; pay-in-full allowed | trip-level deposits; invoice with payment dates; balance in portal | not observed | "Book now, pay over time" marketed | not observed | Common (A+B strong) |
| Booking hold/option before payment | "Hold an Option" 48h | courtesy hold up to 3 days; full-payment-window exceptions | not observed | not observed | not observed | Common (A+B) |
| Per-traveler data collection (passport, contact, emergency, medical/dietary) | full list to confirm booking | mandatory portal account; documents gated on completion | not observed | not observed | not observed | Common (A+B) |
| Documents issued before travel (confirmation/vouchers/e-docs) | initial docs after payment; final ≤2 weeks out; travel voucher | e-docs ~21 days out; gated on data completion | not observed | "Manage your booking" present | not observed | Common (A+B) |
| Optional add-ons attachable (flights, transfers, pre/post nights, insurance) | flights quote, transfers extra, pre/post nights | flights, transfers (21-day deadline), pre/post nights, insurance | car/activities within package | baggage/insurance/protection, flexible pay | — | Common (A+B strong; C/D show in-package extras) |
| Change/cancel with fee schedule; component (airline) rules | penalties per T&Cs; amendment windows for extras | free changes until final payment due; airline separate policies; non-transferable | support promise | protection-driven refund marketing | not observed | Common (A+B strong) |
| Agent/advisor booking channel | encouraged; agent portal | documented for every operation; Agents Login | agency link | Advisor access + Group Quoting Tool | — | Common |
| Escort/guide as part of package | tour leader on trips | Travel Director + Driver | no | some tour packages | private/group tours | Variant (tour pole only) |
| Loyalty/points integration | own loyalty club (light) | past-guest discount, sister brands | miles + MQD earn/burn | Aeroplan earn/redeem | Trip.com Rewards | Variant/Common (all 5, different mechanisms) |
| Vendor separates packages from à-la-carte components | agent flight quotes outside package | flight booking vs tour price distinction | explicit "a-la-carte travel products" | external links for flights/cars | separate nav sections | Boundary evidence (C+D+E explicit; A+B consistent) |

## Canonical Model (working)

```text
Package          the product of record: a named pre-assembled bundle of ≥2 travel
                 components (accommodation + transport and/or guided/tour content),
                 defined by its inclusions and exclusions, sold at one price
Departure        a dated, capacity-bounded instance of a package (fixed-departure tour
                 or date-range availability), with availability states
Traveler Party   the people configuration the booking is made for: adults/children,
                 rooms and room types, share/solo handling — the price basis
Booking          ONE transaction covering the whole package for the party on a
                 departure; carries traveler data, payment schedule, add-ons, and
                 confirmation state (instant or request-confirmed)
Payments         deposit → balance schedule keyed to booking terms/milestones;
                 holds/options before commitment; pay-in-full variants
Travel Documents invoice → confirmation → pre-travel documents (vouchers, e-tickets,
                 e-docs) issued before departure, gated on traveler-data completion
Add-ons          optional components attached to the booking: flights (when not
                 included), airport transfers, pre/post nights, insurance, on-tour
                 extras — each with its own rules and amendment deadlines
```

## L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **The package as the unit of sale** — a pre-assembled bundle of multiple travel components (typically accommodation plus transport or guided/tour content) whose price content is defined by its inclusions, sold as ONE product at ONE price. Remove → component-by-component travel booking (OTA / flight / hotel territory).
2. **The dated departure + traveler-party booking** — a booking binds the package to a specific departure date and a traveler party with occupancy configuration (who travels, in what rooms). One booking covers the whole bundle. Remove → a catalog/brochure, or generic retail.
3. **The booking lifecycle resolving into confirmed travel documents** — confirmation (instant or request-based), a deposit→balance payment schedule, and travel documents (confirmations/vouchers) issued before travel. Remove → enquiry/lead-generation with no completed sale.

Jointly-held load-bearing analysis:

- 1 alone = package catalog/brochure site (no transaction)
- 2 without 1 = component booking platform (OTA territory)
- 3 without 1+2 = payment/confirmation machinery over nothing
- 1+2 without 3 = brochure with booking request and no completed sale (lead-gen)
- 1+3 without 2 = dated-less bundle purchase — not a travel booking
- 2+3 without 1 = flight/hotel/component booking (OTA territory)

## L1 — Common Mature Structure (not definitional)

- Departure availability states visible to the booker (guaranteed/definite; on request; near-full) with request-based confirmation lag on some inventory
- Booking holds/options (reserve space before payment, with expiry)
- Per-person occupancy pricing culture (twin-share, single/solo supplements, child pricing); per-pair/2nd-traveller promotions
- Inclusions/exclusions as a first-class display on package pages
- Manage-my-booking portal: balance payments, traveler-data completion, document access, add-on management
- Traveler-data completion (passport, contacts, emergency, dietary/medical) required and gating document issuance
- Optional add-ons attachable at booking or later with amendment deadlines
- Change/cancel rules keyed to payment milestones, with component-level rules (airline T&Cs) for transport add-ons
- Travel agent / advisor channel as a parallel booking path with its own portal

## L2 — Variant / Optional Structure

- Package shape: fixed-departure escorted tours (land packages) vs dynamic flight+hotel bundles vs all-inclusive resort packages vs flight & cruise
- Flights: included in package vs land-only (flight quotes as add-on) vs internally-included segments
- Escort: escorted (leader/director onboard) vs self-guided/independent
- Loyalty integration mechanisms (airline miles, points, past-guest discounts, sister-brand programs)
- Membership/regional gating and consumer-protection packaging (not directly observed in sample — see Uncertainties)
- Group booking modes (spaces on existing departures, exclusive departures, custom itineraries) and group discounts
- Deposit protection / pay-over-time offerings

## L3 — Vendor-specific (Research Notes only)

- G Adventures: 48-hour "Hold an Option"; all departures guaranteed; mandatory medical insurance with minimum coverage checked on Day 1; "My Own Room"; extra-services 30/10-day amendment windows; Trip Details document; Sherpa agent portal
- Trafalgar: trip-level deposit amounts; 5-year deposit protection; 3-day courtesy hold; 'Definite departure'/'Call Us'/'On Request' labels; Optional Experiences paid on tour (not pre-bookable); Specific Requirements form; sister-brand loyalty discount; product-specific luggage limits; Travel Director pre-trip emails; e-docs at ~21 days
- Delta Vacations: SkyMiles/MQD earn and status-attainment packaging; Medallion-marketing
- Air Canada Vacations: Aeroplan earn/redeem incl. Flight & Cruise; Advisor Group Quoting Tool; 2nd-traveller discount promos; travel-protection refund marketing
- Trip.com: Trip.Planner; private vs group tour split; region-specific support-line separation of package bookings

## Vendor-specific / Rejected Findings

- "All departures guaranteed to run" — G Adventures policy; Trafalgar has 'Definite departure' per-departure instead. Guaranteed-departure as universal property REJECTED for the Type.
- "Optional Experiences cannot be pre-booked" — Trafalgar only. REJECTED as Type-level.
- Deposit-protection (5-year reuse) — Trafalgar only. Variant.
- Insurance mandate with minimum coverage — G Adventures only. Variant.
- Miles/MQD status earn — airline-led poles only. Variant.
- Fixed group sizes (≤15 / 40–52 by region) — tour-pole product specifics. Not Type-level.
- ATOL/bonding-style financial protection presentation — NOT observed in fetched sample; no claim made.

## Boundary Findings

- **vs Online Travel Agency / OTA**: the boundary is the **unit of sale**. OTA's primary sale is a single component (a flight, a hotel room, a car). This Type's primary sale is a multi-component bundle as one product at one price. The vendors themselves maintain the split (Delta: "a-la-carte travel products"; Air Canada Vacations: flights/cars as external booking options; Trip.com: separate package nav sections). A package capability inside an OTA (bundle deals) shares this substructure — the directory keeps both leaves, with the seam at what the platform primarily sells. Remove the bundle-as-unit-of-sale (sell only components) → this becomes an OTA/booking platform.
- **vs Tour & Activity Marketplace**: unit is a single experience/activity (hours to a day, no accommodation/transport bundle as the unit of sale). Remove the multi-component trip bundle and keep single experiences → Tour & Activity territory.
- **vs Tour Operator Management System / Travel Agency Management System / DMC Platform**: those are operator-side systems of record for building and operating packages (contracting, allotments, costing, back-office). This Type is the traveler-facing (and agent-facing) booking surface. Same domain object (package), opposite side of the counter.
- **vs Vacation Rental Marketplace / Hotel Search & Booking / Flight Search & Booking**: single-component or single-accommodation sale; no bundle-of-components unit, no multi-day guided content.
- **vs Cruise booking**: cruise packages bundle cabin+meals+entertainment aboard a vessel with its own structure; both Delta Vacations and Air Canada Vacations present cruise as a separate booking mode from packages (supporting evidence that vendors treat it as distinct).
- **vs Travel Itinerary Planner**: planning/organizing without the sale.

**"去掉什么就变成另一个 Type" 判据**: remove the multi-component bundle as the unit of sale → OTA / component booking. Remove the transaction (booking lifecycle) → brochure/catalog or itinerary planner. Remove the operator's package definition (inclusions as price content) and sell raw inventory → marketplace/booking-engine territory.

## Historical / Market-Sample Check (per §24)

The classic 20th-century package holiday — operator brochure listing flight+hotel at one inclusive price, booked at a travel agency counter with a deposit, balance paid weeks before departure, tickets and vouchers issued beforehand — satisfies all three L0 structures with no online search, no dynamic pricing, no portals, no loyalty. Charter-package wholesalers and escorted motorcoach tours fit equally. The definition is therefore not over-fitted to the modern dynamic-packaging implementation. Conversely, modern dynamic flight+hotel bundles satisfy the same three structures (bundle-as-unit, dated party booking, confirmation+payment+documents), so the definition spans both realizations.

## Uncertainties

- **Dynamic-packaging OTA internals** (how OTA bundles un-bundle at cancellation, price blending of components, per-component confirmations) were not directly observed — Expedia/Loveholidays/On the Beach refused access. Bundle-pole claims are limited to vendor positioning (Tier 2). Confidence in the L0 core is high; confidence in L1/L2 detail at that pole is lower.
- **Availability-state vocabulary at the bundle poles** (whether dynamic bundles present "on request" states or always confirm instantly) — unobserved; only tour poles show request-based confirmation directly.
- **Regional consumer-protection/bonding presentation** (e.g., flight-plus packaging rules in regulated markets) — not observed in sample; not asserted.
- **Per-room vs per-person pricing at hotel-led bundle poles** — per-person twin-share observed strongly at tour poles; per-pair promos at ACV; hotel-led poles not directly observed. Treated as a pricing-implementation variant.
- TUI / Jet2holidays / Costco Travel could not be sampled; the largest integrated-operator pole is represented only by airline-led and wholesaler products.

## Final Synthesis

A Travel Package Booking Platform is the traveler-facing booking application whose unit of sale is the **travel package**: a pre-assembled bundle of multiple travel components defined by its inclusions and sold as one product at one price. Its world model is: **Package → Departure (dated instance with availability states) → Traveler Party (occupancy configuration) → Booking (one transaction for the whole bundle) → Payments (deposit→balance schedule) → Travel Documents (confirmations/vouchers issued before travel)**, with optional add-ons (flights, transfers, pre/post nights, insurance) attaching to the booking under their own rules. The defining structure is small: bundle-as-unit-of-sale + dated party booking + a booking lifecycle resolving into confirmed travel documents. Everything else — dynamic composition, escort, loyalty, holds, portals, agent channels — is common mature or variant structure. The boundary against the OTA is the unit of sale (bundle vs component); against operator-side systems it is the side of the counter; against activity marketplaces it is the multi-component trip as the thing sold.
