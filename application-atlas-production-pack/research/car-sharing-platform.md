# Research Notes — Car Sharing Platform

## Research Goal

Understand what a Car Sharing Platform actually is as an Application Type: its core objects, the member-facing usage loop, the operator/host-facing administration surface, the rules that govern shared-vehicle use, and the boundaries against the neighboring mobility Types (Vehicle Rental, Ride-hailing, Micromobility Sharing, Fleet Management).

## Initial Boundary

Working hypothesis before research:

- Core use: a member books and self-drives a shared vehicle (operator fleet or a peer's car) for a short bounded period, pays usage-based charges, and returns the vehicle to a defined state.
- Likely users: urban residents without car ownership; also businesses.
- Nearest neighbors: Vehicle Rental Platform (counter handover, per-day pricing), Ride-hailing Platform (driver provided), Micromobility Sharing Platform (same loop, different vehicle class), Fleet Management System (operator-side administration).
- Known unknowns: how P2P marketplaces fit the Type; whether "reservation" is definitional given free-floating products; how access technology varies; where the rental boundary really sits.

## Research Questions

1. What is the core object model? (vehicle, member, reservation, trip, station/zone, pricing)
2. What is the trip lifecycle from search to billing settlement?
3. How does vehicle access work across products (app unlock, card/fob, key handover, lockbox)?
4. What fleet-ownership models exist (operator fleet vs peer-to-peer vs hybrid)?
5. What rules matter (fuel/charge state, cleanliness, late return, damage, eligibility)?
6. What interfaces exist for members, and for operators/hosts?
7. How does billing work (time-based rates, distance allowances, fees, protection plans)?
8. What exceptions occur (vehicle unavailable, late return, accident, access failure, no-show)?

## Representative Products

Selected for market representativeness, documentation quality, and distinct product philosophies:

| Product | Model | Why selected |
|---|---|---|
| Zipcar | Operator-owned fleet, round-trip station-based, membership plans | The category's founding template; deep official help center |
| Turo | Peer-to-peer marketplace (hosts list cars; guests book) | The P2P marketplace pole; full guest + host documentation |
| Getaround | Peer-to-peer with instant self-service access (connected hardware) + key-exchange mode | The P2P instant-access pole; both handover modes documented |
| Communauto | Hybrid: one-way free-floating (FLEX) + round-trip station-based | The free-floating pole and a regional strong-player; hybrid model in one product |

Attempted but abandoned: **SHARE NOW** (free-floating, operator-owned) — sharenow.com returned empty responses twice; **MILES Mobility** — 403 twice. Abandoned per network-limitation rule. The free-floating pole is covered by Communauto's FLEX service instead. No claims about SHARE NOW or MILES are made anywhere.

## Sources

### Zipcar (official, Tier 1)

- Support center home: https://support.zipcar.com/hc/en-us (categories: Join / Book / Drive / My Account & More)
- How do I book a Zipcar: https://support.zipcar.com/hc/en-us/articles/220333888
- How do hourly & daily rates work: https://support.zipcar.com/hc/en-us/articles/220676347
- What's included with my Zipcar trip: https://support.zipcar.com/hc/en-us/articles/360023451054
- What do I need to know before my first Trip: https://support.zipcar.com/hc/en-us/articles/360025161813
- Drive category (sections: Accidents and Insurance / Starting Your Trip / During Your Trip / Ending Your Trip / Common Issues / Electric Vehicles): https://support.zipcar.com/hc/en-us/categories/115000212788-Drive
- How do I end my Zipcar trip: https://support.zipcar.com/hc/en-us/articles/220623087
- What happens if I return late: https://support.zipcar.com/hc/en-us/articles/115001108487

Note: zipcar.com marketing pages returned 403; the Zendesk support center was fully reachable.

### Turo (official, Tier 1 via help-center markdown endpoints)

- Help center sitemap: https://help.turo.com/sitemap.xml (article pages are JS-rendered; each article exposes a `.md` markdown alternate — used for all fetches)
- Booking a car in the US: https://help.turo.com/en_us/booking-a-car-in-the-us-H1gxVVeE9.md
- Trip check-in guide (guests): https://help.turo.com/en_us/trip-check-in-guide-guests-HkZfVVe49.md
- Returning a vehicle and checking out: https://help.turo.com/en_us/returning-a-vehicle-and-checking-out-SymM4ExE9.md
- Protection plans in brief (US guests): https://help.turo.com/en_us/summary-and-cost-of-protection-plans-or-us-guests-BJSgBNgVq.md
- Sitemap also confirms host-side article inventory (host no-shows, invoices, reimbursements, cancellations, payouts)

Note: turo.com/support returned 403; help.turo.com root exceeded size limits; sitemap + per-article `.md` endpoints were the working path.

### Getaround (official, Tier 2 product page + Tier 1 help-center structure)

- How it works: https://getaround.com/how-it-works (both Connect and key-exchange flows, full trip loop)
- Help center index: https://help.getaround.com/hc/en-us (full driver-side and owner-side section structure)
- Note: individual help articles are JS-rendered and return the index page (2 attempts); article-level claims are therefore limited to the index's article titles plus the how-it-works page. The how-it-works page is server-rendered and detailed.

### Communauto (official, Tier 1)

- City site (Toronto): https://toronto.communauto.com/ and https://toronto.communauto.com/how-it-works/
- FAQ — FLEX vehicles category: https://faq.communauto.com/en/categories/one-way-vehicles-available-without-reservation-flex/
- FAQ — Starting my trip (FLEX): https://faq.communauto.com/en/support/starting-my-trip-flex/
- FAQ — Driving, Parking, and Ending a Trip (FLEX): https://faq.communauto.com/en/support/driving-parking-and-ending-a-trip-flex/

Research date: 2026-09-07.

## Product Observations

### Zipcar

Evidence layer: A (directly observed, official support articles).

**Positioning & membership**
- Membership-based: personal/family accounts; "approved members"; family-account admins manage drivers and their damage-protection coverage. Membership can be paused/cancelled/reactivated (promoted articles).
- Damage protection coverage is chosen per driver; optional insurance purchase offered at booking.

**Booking**
- Flow: sign in → "Book a car" page → search criteria → Search → select car → optional insurance → "Book this car". Filters for vehicle type/model; "My time is flexible" includes currently-unavailable cars in results.
- Booking from web or mobile app.

**Pricing**
- Hourly and daily rates, varying by day of week; hourly charges cap at the daily rate (system quotes the cheaper of the two); some vehicles hourly-only; some flat-rate-only. Rates vary over time (discounts, availability, holidays); "other fees may apply".

**Trip inclusions**
- Gas included (fuel card in every car); mileage included per day (US 200 mi / Canada 200 km figures stated, "may depend on your membership plan"); free designated parking spot (home location); 24-hour roadside assistance.

**Access**
- Mobile app locks/unlocks the car (requires Location and Bluetooth permissions); keys always stay inside the vehicle; some members have a physical Zipcard that also locks/unlocks.

**Trip discipline**
- Before driving: inspect inside and out, report problems via app; check-in photos exist ("Why are check-in photos important").
- During: edit/extend booking from the Drive screen (if the car is available); only approved account drivers may drive; keys stay in the car.
- Ending: return to the car's home location (any of its spots), ≥1/4 tank, cleaned, keys out of ignition, doors closed, lock via app/Zipcard, take end-trip photos; end via app (Drive → End Trip). Unused time is not refundable; trip ends automatically if not manually ended.
- Late return: extra-time charge plus tiered late fee ($50 / $100 / $150 by minutes late); 3 late fees in 12 months triggers account review and possible suspension.
- Early return: supported (articles on early return and refunds exist).
- Community rules: keep it clean; cannot use a Zipcar as a taxi or rideshare vehicle.
- Accidents: documented accident process, damage fee, damage protection coverage, additional liability insurance (ALI).
- Electric Vehicles section exists in the Drive category.

### Turo

Evidence layer: A (directly observed, official help articles via markdown endpoints).

**Positioning & marketplace structure**
- Marketplace: hosts list vehicles; guests book trips. Host-side inventory includes listing, calendar, pricing/earnings, cancellations, compensation requests, refueling invoices, payouts, host no-shows.
- Guest can book without a pre-existing account (checkout collects name, email, phone, payment method).

**Booking**
- Age minimums by vehicle class (18 standard; 21 for vehicles >$20k; 25 Deluxe; 30 Super Deluxe/Classic/Specialty); young-driver fee for 18–24.
- License rules: physical (not digital) valid license required; temporary/interim licenses conditionally accepted; learner's permits and online-purchased "international licenses" rejected.
- Protection plan selection at booking (Premier / Standard / Minimum / Decline, plus optional supplemental liability); plans are contracts limiting out-of-pocket physical-damage responsibility ($0 / $500 / $3,000 / unlimited respectively, US figures); liability insurance included at state minimum (secondary except NY).
- Overlap rule: one vehicle at a time; new trip cannot overlap an existing booking.
- Free cancellation period; post-booking checklist (phone verification, license upload, protection choice) must complete ≥2 hours before trip start or the trip is cancelled.

**Check-in**
- Can begin up to 24 hours before start: upload license photo + selfie with license (identity verification); contactless check-in vs in-person (present the physical license to the host).
- Host must hand over keys or provide access (even with remote-locking vehicles); document vehicle condition with time-stamped in-app photos (protects against pre-existing-damage and cleaning/smoking claims).
- Early start possible up to 1 hour before schedule with host agreement and completed in-app check-in.

**Return / checkout**
- Follow host's return instructions; return on time or request extension in app; return to correct location (airport approved locations where Turo holds permits; garages/lots with photo + space number; legal street parking for next 24 hours); secure keys (key bag, lockbox); respond to messages within 2 hours of trip end.
- Checkout: in-app photo prompts — exterior condition, interior condition, fuel or charge level, mileage; completing checkout ends the trip. Improper-return fee (US$50; localized amounts given for AU/CA/FR/UK).

**During trip**
- Messaging with host; extras; adding a driver; reimbursement requests from host; dispute invoices.

### Getaround

Evidence layer: A for the how-it-works page (official product page, server-rendered); A− for help-center structure (official index reachable; article bodies JS-gated — article titles observed, bodies not).

**Positioning**
- "Peer-to-peer car rental" (its own logo alt text) / "largest car-sharing service in Europe" (about text). The product itself straddles the sharing/rental vocabulary — recorded as a boundary finding.
- Two access modes: **Getaround Connect** (self-service 24/7 via app) and **key exchange** (meet the owner).

**Connect flow (self-service)**
- Before: choose a nearby Connect car (filter by type, price, features); verify profile once (license + ID photos).
- During: in-app check-in, unlock the car with one tap in the app, keys are inside; included distance (stated: 10 mi/hour up to 200 mi, then 200 mi/day); secondary drivers included; trips covered by insurance and 24/7 support; optional Plus/Premium protection plans.
- After: in-app check-out ends the trip; leave keys inside, lock with phone; rental price automatically adjusted if driven further than included or fuel not refilled.

**Key-exchange flow (Meet Owner)**
- Before: find a car, filter, send a rental request; owner accepts (Instant Booking cars confirm automatically).
- During: meet the owner; owner verifies license, ID, and the credit card used.
- After: return the car; price adjusted with the owner for extra distance / missing fuel.

**Owner side (from help-center structure)**
- Listing my car (delivery offering, Car Status, search-result placement), Getting started as an owner (listing quality, calendar/settings, pricing), Rental price (pricing/owner earnings, discounts), Managing a rental (cancellations, Key Exchange start/finish, compensation requests after a rental), Payments (payout timeframes, social contributions, invoices), Getaround Connect (installation, costs), Getaround for professionals (business registration, invoicing drivers, business insurance).
- Driver side: eligibility, profile verification, secondary drivers, fuel charges/refunds, cleanliness rules, payments, insurance/roadside assistance, accident steps, breakdowns.

### Communauto

Evidence layer: A (directly observed, official city site + FAQ).

**Positioning & membership**
- Carsharing operator; mission framing ("fewer cars on the road"). Membership plans: Open (free), Open Plus, Value plans; gas, insurance, and maintenance always included in rates.
- Eligibility gate: minimum age (19 in Ontario unless family membership), license class (Ontario G/G2), relatively clean 3-year driving record, good credit record; application processed within about two business days; approval email unlocks usage.
- Membership works across cities/provinces (and France) — cross-market membership portability.

**Two services in one product**
- **FLEX (one-way, free-floating)**: no reservation; trips start and end inside a city's FLEX Zone; release the car anywhere in the zone that respects FLEX parking rules (including resident-permit zones where the city's carsharing program grants privileges); FLEX drop-off points exist outside the zone; temporary stopovers allowed (keep the key; trip auto-closes if key is left in the holder).
- **Station-based (round-trip, by reservation)**: pick up and return at the same station; bookable up to a month in advance; station info (reserved spots, Green P lots, "Station Zones" — small return areas with FLEX-like parking privileges) surfaced in the app.

**Access**
- Start trip: app "Start trip" button, or key fob / registered RFID card on the windshield reader. Regional specifics: Quebec members link transit cards (OPUS, STO Multi, STS) to their account and use them as access keys.
- Physical car key retrieved from the glove-box key/card holder; must be returned to it at trip end (USB stick/plug inserted, gas cards returned; holder light confirms).
- End trip: app "End trip" (locks doors, rearms immobilizer, releases vehicle) or RFID key on reader (also ends the trip, unlike reservation-based vehicles). Zone light near the steering wheel warns when outside the FLEX zone.

**Trip economics**
- FLEX duration billed from access to release; credits granted for snow clearing, refueling, or relocating a vehicle to a higher-use area.
- Gas included; fuel credit cards in vehicles; return with at least 1/4 tank ("rule of courtesy toward other members").

**Parking**
- City carsharing programs grant parking privileges (e.g., Toronto: release in "EXCEPT BY PERMIT" zones); per-city FLEX parking guides; parking permits not valid across cities; drop-off points with map availability info.

**Fleet & rules**
- Vehicle categories (compact / mid-size / family / utility / minivan) with category surcharges; search by category and accessories; all vehicles non-smoking.
- Insurance included (collision + third-party liability); Damage Protection Plan options determine the maximum damage fee per event.
- Report (damage, cleanliness) form; lost and found; invite-a-friend referrals; business plans.

## Cross-product Comparison

| Dimension | Zipcar | Turo | Getaround | Communauto |
|---|---|---|---|---|
| Fleet ownership | Operator-owned | Peer-owned (hosts) | Peer-owned | Operator-owned |
| Access geography | Round-trip, station-based | Pickup/delivery points set by host | Connect: any approved location; key exchange: meet owner | FLEX: one-way in zone; station-based: round-trip |
| Reservation model | Reservation required | Reservation required | Reservation required (Connect instant; key exchange request/Instant Booking) | FLEX: no reservation; station-based: reservation |
| Access mechanism | App (Bluetooth) / Zipcard; keys inside car | Host handover or lockbox | App unlock (Connect hardware) / owner handover | App / RFID fob / linked transit card; key in glove-box holder |
| Pricing basis | Hourly + daily rates, capped; plans | Per-trip price set by host; young-driver fee; protection plans | Per-trip price; owner-set; auto-adjustments | Per-minute/hour FLEX + reservation rates; membership plans |
| Distance | Included per day (plan-dependent) | Included per trip (host-set) | Included (hourly accrual to cap, then per-day) | Included (gas always included) |
| Fuel/charge policy | Fuel card in car; return ≥1/4 tank | Refuel/recharge to check-in level; host invoices shortfall | Auto price adjustment for missing fuel | Fuel cards in car; return ≥1/4 tank |
| Condition documentation | Check-in + end-trip photos | Time-stamped trip photos; checkout photos (exterior/interior/fuel/mileage) | In-app check-in/check-out | Damage/cleanliness report form |
| Identity/eligibility | Approved members; license check at signup | License photos + selfie per trip; age minimums by vehicle class | Profile verification (license + ID) once | Application review: age, license class, driving record, credit |
| Protection | Damage protection options + ALI | Included liability + tiered damage contracts | Included insurance + Plus/Premium plans | Included insurance + damage-fee plan options |
| Late/early | Late fees tiered; early return supported | Extension requests; improper-return fee | Price auto-adjustment | Billed to release; credits for service actions |
| Operator/host admin | Fleet operations KB (internal categories visible) | Full host toolset | Full owner toolset + professionals | Fleet ops + city-level parking guides |
| Business offer | Family accounts | — | Getaround for professionals | Business plans |

## Canonical Abstraction

### L0 — Defining Invariant

The shared-vehicle usage loop. A Car Sharing Platform is recognizable only if all of these hold:

1. **Shared vehicle inventory** — vehicles owned by an operator or listed by individual owners, circulating among many users in successive turns. Remove it and there is nothing to share.
2. **Member account with verified driving eligibility** — the gate through which access is granted (license/record verification). Without it, vehicles cannot be handed to strangers.
3. **Access to a specific vehicle for a bounded usage period** — granted either by reservation (station-based, P2P) or by on-demand claim (free-floating). Note: reservation itself is NOT definitional — Communauto FLEX runs without it.
4. **Self-drive usage** — the member is the driver. Remove it and the Type collapses into ride-hailing/taxi.
5. **Return + usage-based closure** — the trip ends with the vehicle returned to a defined location/state and billed by usage (time-based, with distance/fuel adjustments). Without return discipline the shared fleet cannot circulate.

### L1 — Common Mature Structure

Present across the sample; expected of mature products but not definitional:

- Mobile app as the primary surface (map/search, booking, trip control, support)
- Vehicle/station map with real-time availability; search filters (category, features, price)
- Trip machinery: extend, early return, late-return consequences, automatic trip end
- Condition documentation: check-in/check-out photos, damage/cleanliness reporting
- Fuel/charge policy: fuel or charge cards in vehicle, minimum return level, shortfall billing
- Included extras: liability insurance, distance allowance, roadside assistance, parking privileges
- Tiered pricing display (hourly/daily or per-trip) and membership/plan structures
- Damage protection plan options layered on included insurance
- Incident channels: accident process, breakdowns, lost items
- Community rules: cleanliness, no smoking, no commercial/rideshare use
- Operator/host administration: fleet operations, listing/calendar/pricing/earnings tools

### L2 — Variant / Optional Structure

- **Fleet-ownership model**: operator-owned B2C vs peer-to-peer marketplace vs hybrid (Communauto runs both poles in one product)
- **Access geography**: round-trip station-based vs one-way free-floating zone vs P2P pickup/delivery
- **Access technology**: app/Bluetooth unlock, RFID fob/card (including linked transit cards), physical key handover, lockbox, connected-car hardware
- **Membership/pricing posture**: membership plans + rate cards vs per-trip host pricing; young-driver fees; credits/incentives
- **Vehicle-class structure**: categories with surcharges; EV fleets; luxury/specialty classes with higher age gates
- **Business/B2B layer**: professional accounts, business plans, invoicing
- **Regional parking regimes**: city carsharing permit privileges, per-city parking guides, drop-off points
- **Transit integration**: transit-card access, MaaS app distribution
- **Insurance regime**: jurisdiction-dependent liability/damage structures

### L3 — Vendor-specific (research notes only)

- Zipcar: Zipcard physical access card; tiered late fees ($50/$100/$150); 3-late-fees-in-12-months suspension rule; hourly-cap-at-daily-rate quoting; "My time is flexible" search; flat-rate-only vehicles; 200 mi/day US figure
- Turo: protection plan names and out-of-pocket limits (Premier $0 / Standard $500 / Minimum $3,000); vehicle classes with age gates (18/21/25/30); young-driver fee; one-vehicle overlap rule; 2-hour pre-trip checklist deadline; 24-hour check-in window; 1-hour early start; $50 improper-return fee; airport permit locations
- Getaround: Getaround Connect hardware; Instant Booking; 10 mi/hour-to-200-mi-then-200 mi/day distance accrual; $15 referral credits; Plus/Premium plan names; Car Status; social-contribution guidance for owners
- Communauto: FLEX zone mechanics; drop-off points; Station Zones; OPUS/STO transit-card access; credits for snow clearing/refueling/relocation; glove-box key/card holder with insert-detection light; 1/4-tank courtesy rule; Green P garage roof-parking instructions; two-business-day application processing

## Vendor-specific Findings

- Zipcar's internal support center exposes operator-side knowledge-base categories (BPO Support, Fleet Operations) — evidence that the same product family carries a substantial operator/fleet-operations surface behind the member app.
- Turo's help center is organized per-country (US/Canada/UK/France/Australia) with per-jurisdiction protection plans and license rules — the regulatory layer is a first-class dimension of P2P car sharing.
- Getaround's own logo alt text reads "Peer-to-peer car rental" while its about-text claims "largest car-sharing service in Europe" — the market itself uses sharing and rental vocabulary interchangeably for the P2P segment.
- Communauto's FLEX credits (snow clearing, refueling, relocation) are an operator-logistics incentive mechanism unique in the sample.

## Boundary Findings

1. **vs Vehicle Rental Platform (sharpest seam).** Rental: staffed counter handover, per-day pricing, longer durations, vehicle-class booking. Car sharing: self-service access (operator fleet) or platform-mediated peer handover, short time increments (minutes/hours), specific vehicles, membership gate. The P2P segment straddles: Turo/Getaround trips are often multi-day and Getaround self-describes as "peer-to-peer car rental". Structural tests that keep them distinct: (a) the fleet circulates among many users in short successive turns in car sharing, vs sequential multi-day rentals in rental; (b) access is app/self-service or peer-handover, never a rental counter; (c) pricing is time-metered with short increments, not per-day rate cards. **Flag for joint review with vehicle-rental-platform.**
2. **vs Ride-hailing Platform.** Clean: ride-hailing provides a driver (passenger posture); car sharing hands the member the vehicle (driver posture). No overlap in the core loop.
3. **vs Micromobility Sharing Platform.** Structurally the closest sibling: free-floating car sharing and micromobility share the same loop (find nearby vehicle in zone → app unlock → one-way trip → end in zone → per-minute billing). Seam: vehicle class (car vs scooter/bike) and the driver-licensing/eligibility gate (cars require verified licenses; micromobility typically does not). Same family, different vehicle class — both leaves stand.
4. **vs Fleet Management System.** Fleet management is operator-side administration of vehicles (maintenance, telematics, compliance); car sharing's defining surface is member-facing access. Car sharing products do contain an operator side (fleet ops KBs, host tools) but that is supporting structure, not the Type's center.
5. **vs Taxi Dispatch Platform.** Dispatch assigns drivers to requests; car sharing assigns vehicles to members who drive themselves.
6. **vs Parking Application / Parking Management.** Parking privileges are an L2 feature of car sharing (city programs), not the core; parking applications center on finding/paying for parking.

## Historical / Market-Sample Check

Would older, regional, platform-native products still fit the L0?

- **Mobility Switzerland (1997, station-based round-trip, pre-smartphone)**: shared fleet, member eligibility gate, reserved access for a bounded period, self-drive, return + time-based billing. Fits.
- **Early Zipcar (2000, phone reservations + Zipcard)**: fits — the L0 requires none of the app machinery.
- **car2go (2009, free-floating pioneer)**: fits — on-demand claim replaces reservation; the L0 explicitly allows either.
- **Regional transit-card access (Communauto Quebec/OPUS)**: fits — the access credential is an implementation, not the structure.

The L0 deliberately excludes: smartphone apps, GPS/telematics, free-floating zones, P2P marketplaces, membership tiers, EVs. All are era/segment implementations.

## Uncertainties

- Getaround help-article bodies were JS-gated; owner-side mechanics (payout timing, compensation rules) are known only at the level of article titles + the how-it-works page. Claims about Getaround internals are kept at that strength.
- SHARE NOW and MILES (European free-floating operators) unreachable; the free-floating pole rests on Communauto FLEX alone. Free-floating mechanics common across European operators (per-minute billing, zone rules, fuel/charge cards) are asserted only as observed in Communauto.
- Turo host-side economics (fee splits, payout schedules) not fetched in detail; host-side described structurally, not numerically.
- Zipcar marketing pages 403; membership-plan specifics (plan names, prices) not asserted.
- No claims about current fleet sizes, city counts, or market positions beyond what sampled pages state about themselves.

## Final Synthesis

A Car Sharing Platform is a member-facing mobility application built around a shared vehicle inventory that circulates among many users in short successive turns. Its defining loop: a member with verified driving eligibility gains access to a specific shared vehicle for a bounded period (by reservation or on-demand claim), drives it personally, returns it to a defined location/state, and is billed by usage. Around this loop, mature products add: map/search discovery, trip machinery (extend/early/late), condition documentation, fuel/charge handling, included insurance + optional damage protection, community rules, and an operator/host administration side (fleet ops or listing/calendar/pricing/earnings). The Type's variants are structural, not cosmetic: fleet ownership (operator vs peer), access geography (round-trip station vs one-way zone vs P2P delivery), and access technology (app, card, key handover). The sharpest boundary is with Vehicle Rental (counter handover, per-day pricing, class booking); the P2P segment straddles that seam and is flagged for joint review. The clearest separations are with Ride-hailing (driver provided) and Micromobility Sharing (same loop, different vehicle class).
