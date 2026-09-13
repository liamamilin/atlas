# Research Notes — Boat / Yacht Charter Platform

## Research Goal

Understand what a Boat / Yacht Charter Platform actually is as an Application Type: what objects exist inside it, who uses it, how a charter booking flows from discovery to on-the-water handover and post-trip settlement, which rules (qualification, deposits, weather, cancellation) shape behavior, and where its boundary lies against Vacation Rental Marketplace, Vehicle Rental Platform, Marina Management, Cruise Operations, Tour & Activity Marketplace, and OTA.

## Initial Boundary (working hypothesis before research)

- Hypothesis: a two-sided platform where vessel owners/operators list boats available for time-based charter (bareboat or crewed), and charterers search, book, and pay; the platform mediates offer/payment and carries marine-specific semantics (licenses/skippers, security deposits, handover, weather).
- Nearest suspected neighbors: Vacation Rental Marketplace (same two-sided time-based rental shape), Vehicle Rental Platform (time-based vehicle rental), Marina Management (berth/operations, not charter), Cruise Operations Platform (scheduled voyages), Tour & Activity Marketplace (captained day trips), OTA (multi-vertical).
- Unknowns: how much of the market is P2P marketplace vs broker/agency vs operator; whether crewed luxury charter shares the same core model; how deposits/qualification are handled; booking-mode variance (instant vs request vs quote).

## Research Questions

1. What is the central object — the vessel listing, the charter booking, or the trip?
2. What does a listing contain (vessel identity, specs, capacity, base location, rates, options)?
3. What is the booking lifecycle (inquiry → offer → confirmation → payment → handover → post-trip)?
4. How do bareboat vs skippered/crewed charters differ inside the model?
5. Which qualification rules gate a booking (licenses, certificates, experience, crew lists)?
6. How is pricing structured (hour/day/week rates, extras, service fees/commissions, deposits)?
7. What are the two supply-side and demand-side surfaces?
8. How do cancellation, weather, damage, and deposit claims work?
9. How do P2P marketplace, broker/agency, and operator variants differ?
10. What distinguishes this Type from Vacation Rental Marketplace / Vehicle Rental / Marina Management / Cruise Operations / Tour & Activity?

## Representative Products

| Product | Model pole | Geography | Customer tier | Why sampled |
|---|---|---|---|---|
| GetMyBoat | P2P / open marketplace | Global (US-centric) | Mass market, day trips to yachts | Largest global boating marketplace; strong how-it-works + owner-side docs |
| Click&Boat | P2P marketplace + professional fleet path | Europe (FR origin) | Mass market to luxury | European leader; explicit request-to-book + instant reservation; license/skipper rules |
| GlobeSailor | Broker / travel agency | Europe (FR) | Mid to luxury, crewed/cabin cruises | Human-advisor charter agency with curated professional partners |
| Boatico | Broker / agency (charter-agency terms) | Europe (AT), global supply | Weekly sailing-vacation segment | Documents full charter mechanics: weekly cadence, certificates, offer validity, installments, handover checklist |

Rejected/abandoned samples: Sailo (403 ×2), Boatbookings (403 ×2), Borrow a Boat (403 ×2), 12knots (403), Dream Yacht Charter (403 ×2), Click&Boat Zendesk help center (transport error), GetMyBoat Zendesk (not fetched directly; FAQ content obtained from on-site pages).

## Sources

Research date: 2026-09-06. All observations below are from official product surfaces (Tier 1/Tier 2).

- GetMyBoat — homepage, How It Works (FAQ), For Owners: https://www.getmyboat.com , https://www.getmyboat.com/how-it-works/ , https://www.getmyboat.com/for-owners/
- Click&Boat — homepage (incl. FAQ section), Rent out your boat: https://www.clickandboat.com/en/ , https://www.clickandboat.com/en/rent-out-your-boat
- GlobeSailor — homepage: https://www.globesailor.fr/
- Boatico — homepage, FAQs: https://boatico.com/ , https://boatico.com/information/faqs/

Source-access limitations:

- Click&Boat's dedicated help center (help.clickandboat.com, Zendesk) was unreachable (transport error); Click&Boat observations rely on its homepage FAQ and owner-side landing page. Claims kept qualitative.
- Sailo, Boatbookings, Borrow a Boat, 12knots, Dream Yacht Charter returned 403 on all attempted URLs; no claims from these products.
- GetMyBoat's Zendesk help center was not fetched directly; its on-site FAQ/how-it-works/for-owners pages were used instead.
- No precise numeric claims are made for any product except where the product's own page states the number (recorded under Vendor-specific Findings).

## Product A — GetMyBoat

### Key observations (evidence layer A unless noted)

- Positioning: "Captained Yacht Charters and Boat Rentals Worldwide"; self-described "world's leading boating marketplace"; 9,400+ locations; 500,000+ reviews (marketing figures, layer A on-page but promotional).
- Supply breadth: yachts, sailboats, catamarans, pontoons, jet skis, kayaks, canoes, houseboats, fishing boats/charters, wake boats, tours, diving, snorkeling, whale watching, rafting. Watercraft listing policy excludes individual tubes/inflatables and non-water activities; since 2024, kayaks/canoes/rafts/SUP/jet skis accepted only from verified registered businesses (safety initiative).
- Listing unit observed on homepage: per-trip listings with vessel, location, guest capacity, and hourly price (e.g. "40 guests", "$/hour"). Pricing granularity is per hour/day for day trips; multi-day exists (houseboats).
- Renter flow (How It Works): 1) browse listings with verified reviews/photos → 2) send a booking inquiry, chat with owner to customize the trip → 3) owner sends an offer → renter accepts → card charged full amount → meet captain on the dock.
- Payment mechanics: full amount charged on offer acceptance; funds not transferred to owner until successful completion of the trip (platform-held); no partial payments; credit card only; off-platform payment prohibited (gratuities excepted).
- Service fee: renter pays 13% (USD) / 16% (other currencies), non-refundable except extenuating circumstances.
- Security allowance: shown in offer; never charged at booking; activated only if owner files a valid claim within 48 hours of trip completion; disputes assessed by platform with evidence from both parties.
- Owner side: free listing; inquiry management in one space; instant messaging; Google Calendar sync; custom trips of any kind; payouts processed within 48 hours after trip completion to bank/PayPal; cancellation policies honored; fraud protection; "Superowner" exposure program; payment tool for owners' own direct (off-marketplace) bookings at lower fee.
- Operator compliance: platform surfaces US Coast Guard federal requirements and per-state boating requirements (education/license) as reference links; compliance responsibility sits with operators/renters.
- Tipping: discretionary, 10–20% customary for charters (on-page guidance).

## Product B — Click&Boat

### Key observations

- Positioning: "leader in peer-to-peer yacht charters"; 55,000+ private yacht rentals and bareboat charters (on-page figure); press framing "Airbnb of the seas".
- Two search modes on homepage: (1) "Boat rentals" — place of departure + start/end dates + boat type + skipper with/without; (2) "Daily experiences / Activities with captain" — single date. This encodes the two trip shapes: multi-day bareboat/skippered charter vs single-day captained experience.
- Boat types: sailboats, motorboats, catamarans, RIBs, houseboats, jet skis, gulets, barges. Charter-type filters: "Without license", fishing charter, luxury charter.
- Renter flow (FAQ): create free account + nautical profile/CV → search with filters (destination, dates, boat type, passengers, activities) → request a quote and/or immediate reservation with extras (insurance, services) → "You will only be charged if your charter request is accepted by the owner" → validate → set sail. Human "cruise advisors" available free of charge.
- License rule (FAQ): in many regions license-free rental is limited to smaller engines (example given: under ~15 hp frequently exempt; framed as "always check local laws"); without a license, rent with a skipper. License-free boats are a first-class filter category.
- Inclusions (FAQ): bareboat and insurance included; cancellation insurance optional; extras (skipper, fuel, sports equipment, meal care, staff, provisioning) confirmed via listing/quote.
- Crewed charter (FAQ): crew usually includes skipper plus optionally cook, deckhand, hostess.
- Owner side (Rent out your boat): free listing creation; manage bookings/calendar/prices via web or app; chat with prospective renters; accept booking requests based on the renter's sailing experience and reviews from other owners (owner-side renter screening); payment via partner bank transferred to owner's account after each booking; optional comprehensive insurance (up to €8M, Allianz-branded on page) and security deposit; separate registration path for professional fleet owners; earnings estimator tool.

## Product C — GlobeSailor

### Key observations

- Positioning: charter agency ("agence") of ~50 nautical/tourism experts accompanying the customer "from booking to return from vacation" (on-page).
- Supply: professional charter companies ("loueurs professionnels certifiés") curated against the agency's criteria; partner portal login for loueurs; partner showcase.
- Product lines: bareboat boat rental; cabin cruises (per-cabin, crewed); crewed yacht charter; flotilla; river/barge cruises; thematic cruises (honeymoon, diving); sailing courses. This is the widest product-line spread in the sample.
- Booking mode: quote-driven ("Devis gratuit" / free customized quote); phone/WhatsApp contact prominent; travel-agency financial guarantee displayed.
- Reviews: 22,300+ verified client reviews; review content references check-in/check-out, briefing quality, base staff, early boarding, marina handover assistance — evidence that the marina handover ritual is a first-class part of the customer experience in the professional-fleet segment.
- Destination pricing shown as "from €X" per charter (weekly cadence implied by product lines; not explicitly stated on the fetched page).

## Product D — Boatico

### Key observations

- Positioning: yacht-charter agency (Vienna; "General Conditions for Austrian Yacht Charter Agencies"); 10,500 insured boat rentals across 50 countries; charter payment protection + financial guarantee displayed; insurance partner branding on page.
- Supply: professional operators' fleets; boat types include sail boat, catamaran, motor boat, motoryacht, gulet, houseboat, power catamaran, trimaran, motorsailer, wooden boat.
- Pricing cadence: weekly ("from €/week" per destination); deals include discounted weeks, short-term offers, one-way bookings (different embark/disembark bases).
- Booking flow (FAQ, 10 steps): choose destination (country / sailing area / marine base) → desired vacation time, noting boats "mainly booked from Saturday to Saturday" (deviations may cost extra) → boat type + length → bareboat requires skipper certificate and possibly a Short Range Certificate → otherwise book a skipper → specify extras (skipper, hostess, pet, safety net, dinghy, outboard) → "Get an offer" sends a non-binding inquiry → agency sends offer valid 3 days → confirmation creates payment obligation → some operators require a charter contract signed by agency + customer.
- Payment (FAQ): bank transfer; first installment within 5 days of booking confirmation; balance 30 days before trip; 100% upfront if trip starts within a month; invoice issued by the boat operator at the base. Cancellation: after first payment 50% of total; after second payment 100%.
- Deposit & damage (FAQ): security deposit required at handover (credit card or cash), amount stated in the first offer; damage reported immediately → operator writes a damage report (skipper/what-where-how/weather/photos) → repair invoice deducted from deposit; if a skipper was booked, the skipper is responsible for damage.
- Handover (FAQ): at the operator's office show passport, skipper ID, deposit; joint checklist walkthrough of the boat, confirm condition; report anything missing/broken immediately; same procedure at check-out; full deposit returned if all fine.
- Preparation (FAQ): full crew list due 30 days before trip; visa/vaccination guidance; weather/navigation/itinerary resources; safety guidance (nearest larger marina for serious illness/injury; skipper obligated to call emergency number and notify the charter operator).

## Cross-product Comparison

| Dimension | GetMyBoat | Click&Boat | GlobeSailor | Boatico |
|---|---|---|---|---|
| Supply side | Private owners + operators (open listing) | Private owners + professional fleet path | Curated professional charter partners | Professional operators (agency terms) |
| Demand side | Renters (day-trip to yacht) | Renters (day + week) | Clients (week, cabin, crewed, courses) | Clients (weekly sailing vacations) |
| Central bookable object | Trip listing on a specific boat | Boat listing (date-range or daily experience) | Charter product on partner fleet | Boat for a charter week |
| Booking mode | Inquiry → owner offer → accept (offer-based) | Quote request and/or instant reservation | Quote via human advisor | Non-binding inquiry → offer (valid 3 days) → confirm |
| Payment | Card, charged in full at acceptance, platform-held until trip completion | Charged only after owner accepts; payout via partner bank | Via agency (quote-based) | Bank transfer installments (deposit + balance 30 days out) |
| Platform revenue | Service fee both sides (renter 13/16%, owner 11.5/14.5% US/intl) | Commission on P2P charters (rate not stated on fetched pages) | Agency margin (not stated) | Agency margin (not stated) |
| Damage/deposit | "Security allowance" pre-authorized, claimed within 48h post-trip, platform adjudicates | Security deposit + optional insurance (up to €8M) | Not detailed on fetched page | Deposit at handover; damage report; deducted from deposit; skipper responsible if booked |
| Qualification | State-by-state boating requirements surfaced as links; verified-business rule for small craft | License filter; license-free limited to small engines; skipper option; nautical CV | Advisor-guided | Skipper certificate (+ SRC) mandatory for bareboat; crew list; skipper option |
| Handover | "Meet your captain on the dock" | At the harbour with owner | Briefing/check-in/check-out referenced in reviews | Formal checklist handover at operator's office |
| Human assistance | 24/7 support line | Cruise advisors | 50 advisors, phone/WhatsApp | Agency contact, phone/email |
| Trip-shape emphasis | Hourly/day trips dominant | Both day experiences and week charters | Week charters, cabin cruises, flotillas, courses | Charter weeks (Saturday-to-Saturday) |
| Craft scope | Kayaks/jet skis → mega yachts | RIBs → gulets/barges | Sail/catamaran/gulet/crewed yacht/river | Sail/catamaran/motor/gulet/houseboat |

### Stable commonalities (layer B, cross-product)

1. Vessel as the bookable inventory unit — every product's supply side is identified boats (type, size, capacity, base location) held by owners/operators.
2. Time-bound charter as the transaction unit — a specific boat reserved for a defined period (hours to weeks) with a party size.
3. Two-sided mediation with platform-held or agency-held money — the platform/agency sits between charterer and owner/operator for offer, payment, and payout; the money is administered by the intermediary rather than settled privately (payout timing varies by product: held until trip completion in one observed marketplace, transferred per booking in another, staged in installments in agency models).
4. Offer/quote-mediated booking — in all four, the charterer's commitment is created by accepting an offer/quote (instant reservation exists as an option, not the only path).
5. Extras as priced add-ons — skipper/crew, hostess/cook, fuel, provisioning, equipment, insurance are attached to the charter as options.
6. Marine qualification gating — bareboat (self-operated) charters are conditioned on licenses/certificates/experience; the skipper is the universal alternative path.
7. Security deposit / damage-settlement mechanism — a reserved amount backs potential damage/cleaning claims, with a defined claim/adjudication path.
8. Handover ritual at the base/dock — check-in/check-out with condition confirmation (documented most explicitly by Boatico; visible in GlobeSailor reviews; implied by GetMyBoat's "meet your captain" and Click&Boat's harbour meetings).
9. Two-sided reputation — reviews of boats/owners and (in P2P) of renters inform acceptance and ranking.
10. Cancellation/refund policy ladder — money-back conditions tied to how close to the trip cancellation happens.
11. Dual surfaces — a charterer-facing discovery/booking surface and a supplier-facing listing/calendar/inquiry management surface.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

```text
Vessel inventory (identified boats held by owners/operators, presented for selection)
  └── Time-bound charter booking (specific vessel × defined period × party)
      └── Mediated commercial transaction
          (platform/agency intermediates offer, payment, payout between the sides)
```

Three properties. Remove any one and the Type collapses:

- **Vessel inventory** — without identified bookable boats it is not a boat charter platform (it becomes a generic travel agency or directory).
- **Time-bound charter booking** — without a reservation of a specific vessel for a defined period there is no charter (it becomes media/content or a classified ad board).
- **Mediated transaction** — without platform/agency-intermediated offer-and-payment it is a listings directory or classifieds site, not a charter platform.

Note what is NOT in L0: P2P private owners (professional-fleet-only platforms qualify), instant booking (quote-driven brokers qualify), licenses/skippers (jurisdiction-dependent), deposits (not universal in form), weekly cadence (hourly day-trip platforms qualify), reviews, messaging.

### L1 — Common Mature Structure

Present across the researched sample; expected in mature products but not definitional:

- Discovery/search: destination/base, dates, boat type, length, capacity, price; charter-type filters (license-free, fishing, luxury)
- Inquiry → offer → confirmation lifecycle (with instant booking as an option in marketplace products)
- Pricing structure: base rate per hour/day/week + extras (skipper, crew, hostess/cook, fuel, provisioning, equipment, insurance) + platform service fee or agency margin
- Skipper/crew as bookable add-ons; bareboat vs skippered/crewed as the fundamental arrangement choice
- Qualification gating for self-operated charters (license/certificate/experience; crew list for week charters)
- Security deposit / security allowance with a claim-and-adjudication path
- Insurance products attached to the charter (liability/cancellation; deposit protection)
- Handover/check-in/check-out support (condition checklist, documents, deposit collection)
- Cancellation/refund ladder tied to time-to-departure; weather as a recognized contingency
- Two-sided reviews and reputation
- In-platform messaging between charterer and owner/operator (or advisor as intermediary)
- Supplier-side console: listing creation, calendar/availability, pricing, inquiry management, payout tracking
- Charter contract / booking confirmation as a document artifact (explicit in agency models)

### L2 — Variant / Optional Structure

- Supply model: open P2P private owners ↔ professional fleet operators ↔ curated broker partners
- Booking mode: instant book ↔ request-to-book ↔ quote/enquiry via human advisor
- Trip shape: hourly/day experiences ↔ multi-day point-to-point sailing vacations ↔ cabin cruises ↔ flotillas ↔ courses
- Craft scope: small craft (kayak/jet ski/pontoon) ↔ sailing yachts/catamarans ↔ motor yachts ↔ gulets ↔ houseboats/barges
- Payment mechanics: card-charged at acceptance with platform-held funds ↔ bank-transfer installments ↔ invoice at the base
- Regional cadence: Saturday-to-Saturday weekly (Mediterranean-style) ↔ hourly/day-trip markets
- Human-assistance depth: self-serve ↔ advisor-mediated agency
- Compliance posture: platform surfaces local regulations ↔ agency verifies certificates ↔ operator handles at base
- Adjacent product lines some platforms add: sailing courses, river/barge cruises, events/parties, fishing-specialized charters

### L3 — Vendor-specific (research notes only)

- GetMyBoat: renter service fee 13% USD / 16% other currencies; owner fee 11.5% US / 14.5% international; "Charge" tool for owners' direct bookings at 1.5%/3%; security-allowance claim window 48h post-trip; payouts within 48h after trip completion; Superowner program; 2024 verified-business requirement for kayaks/canoes/rafts/SUP/jet skis; no prepaid cards; tips 10–20% customary guidance.
- Click&Boat: nautical profile/CV for renters; Allianz-partnered comprehensive insurance up to €8M; Caisse d'Epargne as payout bank; "cruise advisors"; earnings estimator ("pricer"); license-free engine threshold example (~15 hp, jurisdiction-dependent); 55,000 listings figure.
- GlobeSailor: ~50 advisors; 22,300+ verified reviews; travel-agency financial guarantee; partner ("loueur") portal; product-line breadth (cabin cruises, flotillas, thematic cruises, sailing courses).
- Boatico: offer validity 3 days; cancellation ladder 50% after first payment / 100% after second; balance due 30 days before trip; 100% upfront if <1 month; Saturday-to-Saturday cadence with surcharge risk for deviations; crew list due 30 days before trip; charter contract signed by agency + customer; Austrian agency general conditions; Yacht-Pool branding; 10,500 boats / 50 countries figures.

## Vendor-specific Findings

See L3. The fee percentages, claim windows, offer-validity periods, and cancellation percentages are all product-specific published terms and must not be generalized into the canonical document.

## Boundary Findings

- **vs Vacation Rental Marketplace** — closest structural sibling: both are two-sided platforms renting an indivisible physical asset by time, with deposits, reviews, cancellation ladders, and owner-side consoles. The distinguishing test: the inventory is a *vessel that is operated* — which drags in marine qualification (license/certificate or skipper), damage-deposit settlement tied to operating the asset, handover rituals at a dock/base, crew lists, and weather as a structural contingency. Remove the vessel-operation semantics (no license/skipper dimension, no handover/deposit-for-operation) and the Type collapses into Vacation Rental Marketplace; add accommodation-style inventory and it *becomes* one. Kept separate.
- **vs Vehicle Rental Platform** — both rent an operated vehicle by time. Differences observed: boat charter platforms in this sample are marketplace/broker-shaped (many suppliers, offer-mediated, commission/fee-based), while vehicle rental is typically operator-fleet, counter/checkout-shaped; boat charters carry skipper/crew as a bookable alternative to self-operation and use weekly vacation cadences. A professional charter fleet listing on a marketplace is the overlap zone. Kept separate (different supply structure + marine qualification semantics).
- **vs Marina Management** — marina software manages berths, dockage, and marina operations for the marina operator; a charter platform sells time-use of vessels to the public. A marina may *host* charter bases; the systems do not merge.
- **vs Cruise Operations Platform** — cruise operations run scheduled voyages with cabins sold per passenger on a line-operated vessel; charter platforms sell an entire vessel's time to one party (or a cabin aboard a chartered crewed yacht as an agency product line — GlobeSailor's cabin cruises are the boundary case, sold as charter products with crew, not as scheduled line voyages).
- **vs Tour & Activity Marketplace** — captained day trips (fishing, sunset, party boats) overlap heavily. The distinguishing test: whether the platform's inventory model includes *self-operated* vessel use (bareboat with qualification, deposit, handover). A platform that only sells captained experiences is drifting toward Tour & Activity; the presence of the bareboat/qualification/deposit machinery is what keeps this a charter Type. Both poles coexist inside single products (GetMyBoat, Click&Boat), which is why the leaf covers "Boat / Yacht" as one Type.
- **vs OTA** — OTAs distribute flights/hotels/verticals; charter platforms are vertical specialists owning the marine transaction semantics. Some charter supply is distributed through OTAs/aggregators, but the charter platform is the merchant-of-record layer for the vessel transaction.
- **Historical / market-sample check (§24)** — pre-internet charter brokers (human-mediated offer, contract, deposit, handover) fit the L0 exactly: vessel inventory (their book), time-bound charter, mediated transaction. A local charter-fleet operator with paper contracts also fits (inventory + booking + direct transaction; mediation is thinner but the operator itself is the supply side). A *boat club* (membership-based access to a fleet) does NOT fit L0's per-charter transaction shape — it is a membership entitlement model and would be a separate Type/variant; not verified against a live product in this pass (Borrow a Boat unreachable), so recorded as an open question rather than a claim.

## Uncertainties

- Commission/fee structures for Click&Boat, GlobeSailor, Boatico were not stated on reachable pages; only GetMyBoat publishes its percentages. No canonical fee claims made.
- Whether instant booking is available on Boatico/GlobeSailor (their flows are quote-driven on the fetched pages); marketplace products show both modes.
- Boat-club/subscription variant (Borrow a Boat) could not be verified; its relationship to this Type is unresolved.
- The exact legal instrument set (charter contract vs platform terms) varies; Boatico documents a signed charter contract for some operators; GetMyBoat/Click&Boat pages fetched do not mention one. Kept as variant.
- Weather-cancellation specifics (who decides, refund depth) were not documented on fetched pages beyond "weather" appearing as a recognized contingency (damage reports, safety guidance); kept qualitative.
- Luxury crewed charter industry instruments (e.g., broker associations, standard terms, provisioning allowances) were not reachable (Boatbookings 403); deliberately not asserted.

## Final Synthesis

A Boat / Yacht Charter Platform is a two-sided (or agency-intermediated) booking platform whose supply side is identified vessels offered for time-based charter and whose demand side is charterers reserving a specific vessel for a defined period. The platform mediates the commercial transaction — inquiry/quote, offer, payment collected and administered through the platform, settlement of the supplier under the product's payment model — and carries a stable layer of marine-specific machinery: skipper/crew as bookable alternatives to self-operation, qualification gating (licenses/certificates, crew lists) for bareboat charters, security deposits with damage-claim settlement, base handover rituals, and cancellation/weather policies. The market implements this core in three recognizable postures — open P2P marketplace (private owners, service fees, offer-based booking), professional-fleet marketplace, and curated broker/agency (quote-driven, human-advised, charter contracts) — sharing one canonical model. The Type's boundary against Vacation Rental Marketplace is the sharpest: the same two-sided time-based rental skeleton, differentiated by vessel-operation semantics (qualification, deposits for operation, handover, weather).
