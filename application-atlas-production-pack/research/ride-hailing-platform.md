# Research Notes — Ride-hailing Platform

Research date: 2026-09-09

## Research Goal

Understand what a ride-hailing platform actually is as an Application Type: its core objects, the request→match→ride lifecycle, both user populations (riders and drivers), pricing models, trust/safety machinery, and where its boundaries run against neighboring transportation Types (taxi dispatch, on-demand delivery, car sharing, micromobility, MaaS, employee/NEMT/school transportation, fleet management, transit).

## Initial Boundary

Working hypothesis before research: a ride-hailing platform is a two-sided consumer platform where a passenger requests an on-demand ride (origin → destination), the platform matches the request in real time to an available driver with a vehicle, the ride is tracked live, and the fare is accounted for by the platform. Expected confusions: taxi dispatch (fleet-operator side of the same world), on-demand delivery (same matching machinery, goods not people), car sharing / micromobility (vehicle supplied, no driver), employee transportation / NEMT / school transportation (closed eligible populations), MaaS (multi-provider aggregation), fleet management (supply-side asset view).

Known flags inherited from sibling passes (STATUS.md):

- **on-demand-delivery-platform** (processed 2026-09-09): "ride-hailing-platform (same real-time request→match→track machinery, people vs goods; Uber's own product split — Guest Trips vs Direct — documents the seam)" — to be discharged this pass.
- **employee-transportation-platform** (2026-09-08): closed employer population vs open public — ride-hailing named as the removal target.
- **non-emergency-medical-transportation-platform** (2026-09-09): "anonymous ride booking = ride-hailing/taxi territory".
- **car-sharing-platform / micromobility-sharing-platform**: ride-hailing supplies a driver (passenger posture); sharing Types supply the vehicle (member-driver posture).

## Research Questions

1. What is the canonical ride lifecycle and what states does a ride pass through?
2. What exactly happens at matching time (offer/accept, counteroffer, assignment)?
3. What are the pricing models (platform-set upfront, dynamic, negotiated bid, metered taxi fare)? Which of these is definitional?
4. Who are the users on both sides, and what does each side do?
5. How is driver supply onboarded and qualified?
6. How do passenger payment and driver compensation relate? Is cashless settlement definitional?
7. What trust/safety machinery is structural (mutual identification, tracking, ratings, emergency tooling)?
8. What rules govern cancellation, no-shows, and disputes?
9. Which capabilities are variants: scheduled rides, business accounts, multi-service super-app bundling, taxi-supply aggregation?
10. Where are the boundaries vs the neighboring Types listed above?

## Representative Products

Selection rationale: market representativeness across regions and postures, documentation completeness, deliberately different product philosophies, different market tiers.

| Product | Posture / philosophy | Why sampled |
|---|---|---|
| **Uber** | global archetype; algorithmic matching; super-app (Ride / Eats / Freight / Business / Health / Advertising) | the reference shape of the Type; official "How Uber works" flow |
| **Lyft** | North American #2; deep rider+driver help center | best article-level Tier-1 documentation of both sides (request flow, rate card, driver application) |
| **Bolt** | European mobility super-app; low-cost positioning | second super-app posture; explicit safety suite; fleet-partner portal |
| **inDrive** | passenger-bid pricing philosophy; self-described "online aggregator" | the pricing-philosophy counter-pole; article-level help center; proves what the core is without upfront pricing |
| **FREE NOW** | taxi-aggregation pole ("taxi app"): licensed taxis + private hire supply | proves the Type does not require crowdsourced private drivers or platform-set pricing |

## Sources

- Uber — Ride product page (uber.com/us/en/ride/), "How Uber works" (uber.com/us/en/about/how-does-uber-work/), Uber Help index (help.uber.com/riders) — accessed 2026-09-09
- Lyft — Help Center (help.lyft.com): "How to request a ride", "Rate card earnings", "How to apply to become a driver", Riding with Lyft category index, Lyft Help root — accessed 2026-09-09
- Bolt — bolt.eu/en/rides/, bolt.eu/en/ (services, safety, FAQ, fleet) — accessed 2026-09-09
- inDrive — indrive.com/en/ + help articles: how-to-request-an-indrive-ride, how-fares-are-calculated, how-to-cancel-a-ride, what-are-the-payment-methods-on-indrive, passengers help index — accessed 2026-09-09
- FREE NOW — free-now.com (rider/driver/business navigation, safety copy) — accessed 2026-09-09

Source-access limitations: Uber Help and Bolt Help centers render article content client-side and yielded only index/nav content; for those two vendors the reachable layer is product pages (Tier 2) plus the official "How Uber works" explainer. Lyft and inDrive yielded article-level Tier-1 content. FREE NOW reached at product-page level. Per evidence rules, precise operational numbers below are kept in these notes (not the final document), and claims in the final document are calibrated accordingly.

## Product Observations

### Uber

Evidence layer: A (directly observed, product-page tier + official explainer).

- Official 5-step flow ("How Uber works"): 1. rider enters destination, reviews ride options, selects, confirms pickup → 2. "A nearby driver accepts the rider's ride request. The rider is automatically notified as the driver gets close." → 3. pickup: "The driver and the rider verify each other's names and the destination. Then the driver starts the ride." → 4. trip (driver gets turn-by-turn directions) → 5. "At the end of each trip, drivers and riders can rate each other from 1 to 5 stars. Riders also have the option to tip directly in the app" (compliments in some countries).
- Request entry on web without the app ("request a ride online… from your computer or tablet") — form factor not app-bound.
- Reserve: rides bookable up to 90 days in advance (product-specific number).
- Ride options page: multiple vehicle/service classes; "some might not be available where you use the Uber app… look in the app for what rides you can request" — class availability is market-scoped.
- Uber Taxi: "Uber makes it easy to get a taxi nearby in the cities where Uber Taxi is available… you can use the Uber app or website to request a taxi" — licensed taxi supply inside the ride-hailing surface.
- Adjacent services in the same app/company: Eats, Rent (car rental), group rides, teen accounts, Uber for Business (business travel, courtesy rides), Freight, Health, Advertising, Bikes & Scooters.
- Help-center sections: Riders / Driving & Delivering / Eats / Merchants & Restaurants / Bikes & Scooters / Business / Freight / Fleet — Fleet is a distinct operator-side audience.

### Lyft

Evidence layer: A (article-level Tier 1).

- Request flow: "Tap 'Search destination'… Select your preferred ride type… Tap 'Select Lyft'… Confirm or change your pickup location before tapping 'Confirm and request'." Pickup auto-set from GPS; add a stop mid-ride; saved Home/Work; gate codes in pickup notes; contact driver by phone icon.
- "Request a ride for someone else": change rider from contacts; if the rider has no account they get an SMS link to create one — the requester holds the account, the passenger may differ.
- "I'm unable to request a ride" causes (direct rule evidence): payment method needs updating; not enough funds; no current drivers available in your area; account deleted/deactivated; connectivity issues. A failed payment authorization blocks requesting with that method.
- Ride types exist as a first-class selection; ride modes affect driver pay ("If you accept a Standard ride, you'll earn the standard rate… a premium ride, the premium rate").
- Payments: passenger charged an **upfront price** "based on the estimated time and distance of the ride, plus any applicable tolls", which "also includes Lyft's fees"; driver earnings decoupled from passenger charge ("These fees don't impact the amount you earn"); two driver pay models — Upfront Pay (most regions) vs rate card (base fare + time + distance); 100% of tips to driver (cash tips fine); bonuses (e.g., streak bonuses); weekly automatic payout + on-demand payout option; per-region minimum/maximum fares (max fare prevents requesting the ride); regional guaranteed-rate regimes (NYC, WA, MN, California).
- Cancellation/no-show fees exist (passenger-side); "Passengers may also be charged for cancellations and no-shows."
- Driver application: background check ("can take several weeks"), vehicle requirements, city/state-specific requirements (TNC permitting, vehicle inspection), mandatory Community Safety Education program before Driver Mode.
- Account/family structures: Lyft Family (linked accounts, shared payment, ride-detail sharing), Lyft Teen (region-scoped), Business profiles & Lyft Business, rider verification, passkeys.
- Payment instruments: cards, Lyft Cash (funds addable **with cash** at retail), gift cards, Price lock, promotions, Round Up & Donate.
- Safety: share ride details/location with trusted contacts, report accident/collision, report safety incident, audio recording (region-scoped), accessibility/anti-discrimination policies, service-animal policy.
- Rider side also: scheduled rides (separate article), coverage areas, airport information, Women+ Connect (region-scoped program).

### Bolt

Evidence layer: A for product-page claims (Tier 2).

- Self-label: "Bolt is your go-to ride-hailing app"; "Request in seconds, ride in minutes"; book in advance "up to 90 days ahead" (product-specific number).
- Pricing FAQ: "Ride prices vary based on the journey distance and ride-type you select, with an upfront price estimate provided once you enter your destination."
- Payment FAQ: "Add your credit/debit card for in-app payment. Depending on your location, options like Bolt Balance, cash, or mobile payments may also be available." — cash is an explicit in-type variant.
- Safety suite (feature-level, country-scoped): Emergency Assist button (alerts an emergency response team + safety team welfare call); Women-for-women ride type; Ride Check ("detect any unexpected and excessively long stops during rides"); share location ("Send the car's make, model, registration number, and live location to friends or family via a shareable link. All trips are also tracked and recorded."); masked phone numbers ("When you make a call via the Bolt app, your number remains hidden"); pickup codes ("you'll always get in the right car"); 24/7 support.
- Supply side: "Join over 4.5 million partners"; fleet partners: "Join Bolt with your fleet… manage your assets from one easy-to-use dashboard" — supply can be individual drivers or fleets.
- Super-app: Rides, Food delivery, Bolt Drive (car sharing), Bolt Market (groceries), Scooters/E-bikes, Business, Bolt Send (parcel). Self-label: "the first European mobility super-app."

### inDrive

Evidence layer: A (article-level Tier 1) — the pricing counter-pole.

- Request flow (city): enter pickup + destination → "Offer a fare that is right for you. Drivers may accept your offer or offer a higher fare." → tap "Find a driver" → "Choose a driver by their arrival time, rating, and fare offer." → see the driver's location on the map while waiting; can contact the driver.
- Fares: "There's a recommended minimum bidding fare… Passengers can offer the recommended amount or a higher one… Drivers can accept the fare or make a counteroffer." No limit on driver offers; the fare cannot change once the ride starts; "Drivers can't ask for more money, either in the app or in person, after they've accepted the fare"; tolls/airport fees are the passenger's, paid separately.
- Cancellation: free at any time before an offer is accepted; after acceptance discouraged; "If you cancel often, this can lead to lower ratings and temporary account blocking"; a reason must be chosen.
- Payment methods: "vary depending on your location. Drivers can accept multiple payment options, such as cash, card, or online digital wallets."
- Ratings bilateral ("How to check my rating"), ride history, receipts/invoices; scheduled rides; passenger limits; pet policy; special ride types (Comfort, XL); City-to-City (request form → wait for driver offers → call driver to confirm → rate) and Rideshare mode (join rides already on a route).
- Posture (footer, every page): "inDrive is an online aggregator. We do not participate in cooperations between our users: they create and perform all requests in our app on their own." — even the most disintermediated product still holds the request form, the offer exchange, the fare record, and the rating record in the app.

### FREE NOW

Evidence layer: A for product-page claims (Tier 2) — the taxi-aggregation pole.

- Self-label: "The fast, safe & reliable taxi app"; "1000s of taxis on tap across Europe"; "Europe's best taxi app, available in 150+ cities" (number product-specific).
- Supply: licensed taxis (black-cab imagery) **and** private hire vehicles — driver site splits "Taxi" vs "Private Hire" audiences, with separate help centers (support.free-now.com rider/taxi/PHV/business).
- "Know your driver": "you'll know your driver's details, rating, and driving experience" — identification + rating on the taxi pole.
- Payment: "Taxi trips without cash" — in-app payment emphasized over street-cash norm of taxis; Prebooking product; Business travel with expensing; Freenow PLUS subscription; eScooters/eBikes adjacency; on-cab advertising for drivers.

## Cross-product Comparison

| Aspect | Uber | Lyft | Bolt | inDrive | FREE NOW | Strength |
|---|---|---|---|---|---|---|
| Passenger-created on-demand request (origin→destination) | yes | yes | yes | yes | yes | Core (5/5, both poles) |
| Real-time matching to a specific driver+vehicle | yes | yes | yes | yes (offer/counteroffer, rider picks driver) | yes | Core (5/5, both poles) |
| Live tracking of the matched car / driver en route | yes | yes | yes (shareable live link) | yes (driver on map) | yes | Core (5/5) |
| Mutual identification of counterparties | yes (verify names) | yes (ride details sharing, driver details) | yes (make/model/registration, pickup codes, masked numbers) | yes (driver rating/arrival/fare visible pre-choice) | yes ("Know your driver") | Core (5/5) |
| Platform-recorded ride + fare accounting | yes | yes | yes ("All trips are also tracked and recorded") | yes (fare fixed in-app even when paid cash) | yes | Core (5/5) |
| Upfront platform-set pricing | yes (see prices) | yes (explicit upfront passenger price) | yes (upfront estimate) | **no — passenger bids, drivers counteroffer** | metered-taxi tradition + app payment | Common, NOT definitional |
| Dynamic/surge pricing | market practice (not evidenced on fetched pages) | implied by demand framing | not evidenced | absent by design | not evidenced | Variant — NOT definitional |
| Vehicle/service classes | yes | yes (ride types) | yes | yes (Comfort, XL) | taxi types + PHV | Common (5/5), class names vary |
| Scheduled / reserved rides | yes (Reserve) | yes | yes | yes | yes (Prebooking) | Common (5/5) |
| Two-way ratings | yes | yes | yes | yes | driver rating explicit | Common (5/5) |
| In-app/masked driver contact | yes | yes | yes (masked numbers) | yes | yes | Common |
| Cancellation rules + penalties | fees regime (inferred from Lyft-side symmetry; Lyft explicit) | explicit fees | pickup codes; country-scoped | explicit (reason required; repeat cancellations → rating/blocking) | not evidenced | Common |
| Driver qualification gates | help sections exist | explicit (background check, vehicle reqs, inspection, safety education) | registration | driver help center | taxi/PHV licensing | Common; depth varies by regime |
| Driver earnings visibility & payouts | yes | explicit (rate card / upfront pay, payouts, tips) | yes (driver earnings pages) | yes | yes | Common |
| Cashless in-app payment | yes | yes (+ cash top-up into Lyft Cash) | yes (+ cash variant) | cash/card/wallet per location | yes (no-cash emphasis) | Common with cash variant (3/5 explicit cash paths) |
| Safety emergency tooling | teen/follow features | share location, audio recording, incident reporting | Emergency Assist, Ride Check, pickup codes | safety pact, ride sharing | safety center | Common; exact tools vary |
| Business/corporate tier | Uber for Business | Lyft Business | Bolt for Business | (business delivery only) | Business travel | Common |
| Subscription/membership | Uber One | Lyft Pink/Pass | Bolt Plus | — | Freenow PLUS | Optional |
| Super-app bundling (food/scooters/rentals/parcels) | extensive | moderate (bikes/scooters) | extensive | moderate (delivery, intercity, money) | light (scooters/bikes) | Variant — NOT definitional |
| Supply = crowdsourced private drivers | yes | yes | yes | yes | **no — licensed taxis + PHV fleets** | Variant — NOT definitional |
| Fleet-partner operator portal | Fleet audience | — | fleet dashboard | fleet page | taxi/PHV fleets | Common as supply-side surface |
| Web (non-app) request | yes | — | yes ("in select regions") | app-first | app-first | Optional |

## L0 — Defining Invariant

The smallest structure without which the product is not recognizable as a ride-hailing platform. Four jointly-held properties:

1. **The on-demand ride request as the unit of work** — a requester creates a specific trip request (origin → destination) for near-immediate fulfillment through the platform. Remove → timetabled transit, rental booking, or a program shuttle.
2. **Real-time matching of the request to a specific available driver-and-vehicle** — the platform assigns or offers the request to live supply and both sides become bound to the match; the supply is driver-operated (private drivers, fleets, or taxis). Remove → a ride marketplace listing without matching (rental/aggregator), or a dispatch desk where the passenger creates no request (taxi dispatch).
3. **The tracked, mutually-identified trip lifecycle** — request → matched/accepted → driver en route with live location visible → pickup → on trip → completion; each side sees who and what vehicle they are dealing with. Remove → blind booking/reservations; remove identification → anonymous dispatch.
4. **The platform-priced, platform-recorded ride with mediated settlement** — the fare is computed/quoted/negotiated and recorded by the platform, and passenger charge and driver compensation are settled through instruments the platform manages (in-app payment; cash at the vehicle is a common realization of a still-platform-recorded fare). Remove → street hail / radio dispatch with no platform record, or a connection service with fully off-platform economics.

Jointly-held load-bearing analysis:

- 1 alone (2+3+4 without 1) = operator dispatch board / fleet ops (Taxi Dispatch territory).
- 2 alone = supply listing with no request lifecycle (rental marketplace).
- 3 without 1+2 = shipment-style tracking of nothing; without mutual identification = anonymous courier-style dispatch.
- 4 without 1–3 = accounting shell.
- 1+2 without 3 = a matching broker with no visible trip (early directory e-hail below the Type bar).
- 1+2+3 without 4 = ride-connection with fully off-platform payment (street-hail digitization, not a ride-hailing platform).

## L1 — Common Mature Structure

Present across the sample (and expected in the market) but not required to recognize the Type:

- Twin consumer surfaces: rider app + driver app (plus operator support and fleet-partner surfaces in platform-form products).
- Personal accounts on both sides; saved places; trip history; receipts.
- Vehicle/service classes (economy → premium; taxi; XL/large).
- Upfront fare estimate / see-price-before-request (pricing model varies, but fare visibility is common).
- Two-way star ratings and post-trip feedback; tipping.
- In-app contact with the counterparty, commonly with number masking.
- Cancellation and no-show rules with fees/penalties and required reasons.
- Driver-side earnings view, payout cycle, bonus/incentive mechanics.
- Driver qualification gates (background checks, vehicle requirements, regional permits/inspections, safety education).
- Live location sharing with trusted contacts; in-app emergency/safety tooling.
- Business/corporate profiles with expense-oriented billing.
- Scheduled/reserved rides.

## L2 — Variant / Optional Structure

- **Pricing philosophy**: platform-set upfront (sometimes dynamic) pricing ↔ passenger-bid negotiation (inDrive) ↔ metered taxi fare with app payment (FREE NOW). Not definitional.
- **Supply model**: crowdsourced private drivers ↔ licensed taxi fleets ↔ mixed/PHV ↔ fleet partners with own dashboards. Not definitional.
- **Settlement instruments**: card/wallet/balance; cash at the vehicle; cash top-up into app balance. Not definitional.
- **Regulatory shapes**: TNC permits, regional guaranteed driver pay, city-specific vehicle rules, region-scoped programs (women-drivers products, teen accounts).
- **Trip-shape variants**: scheduled/reserved; extra stops; ride-for-someone-else; group rides; shared/pooled rides; city-to-city/intercity; rideshare/carpool matching.
- **Adjacent-service bundling** (super-app): food delivery, groceries, scooters/bikes, car sharing, parcel send, advertising, credit/money services. Presence or absence does not change the Type.
- **Memberships/subscriptions** for riders; **autonomous-vehicle programs** (era-current).

## L3 — Vendor-specific Structure (research notes only)

- Uber: Reserve up to 90 days ahead; "How Uber works" 5-step public explainer; Product split Ride vs Eats vs Freight vs Health vs Advertising; guest/web request; Uber Taxi supply class.
- Lyft: Upfront Pay vs Rate Card duality; weekly Tuesday payouts + Express Pay; Lyft Cash cash top-up; Community Safety Education program gating Driver Mode; California guaranteed-rate regime; max-fare request blocking.
- Bolt: Emergency Assist + welfare call; Ride Check long-stop detection; pickup codes; Bolt Send; fleet dashboard; "first European mobility super-app" self-label; 850+ cities self-claim.
- inDrive: recommended-minimum bid; unlimited counteroffers; fare immutability after acceptance; "online aggregator" disclaimer; Rideshare on-route joining mode.
- FREE NOW: Taxi vs Private Hire driver audiences; The Knowledge Subsidy; on-cab advertising; "4 minutes on average" pickup claim; 150+/180+ city claims.

## Rejected Findings (not promoted)

- **Dynamic/surge pricing as definitional** — rejected: absent by design in one sampled product (inDrive) and not evidenced across the sample; it is a pricing-philosophy variant.
- **Upfront pricing as definitional** — rejected: inDrive negotiates, FREE NOW aggregates metered taxis.
- **Cashless payment as definitional** — rejected: explicit cash paths in 3/5 sampled products (Bolt FAQ, inDrive methods, Lyft Cash cash top-up).
- **Crowdsourced private drivers as definitional** — rejected: FREE NOW aggregates licensed taxi/PHV supply; Uber Taxi adds taxi supply inside the app.
- **Smartphone-app form factor as definitional** — rejected: Uber documents full web requesting; the defining surface is the request→match→track loop, not the device.
- **Two-way ratings as definitional** — held at L1: universal in the sample (5/5), but the Type is recognizable without them (early taxi e-hail); ratings are the mature trust layer, not the skeleton.
- **Super-app breadth as definitional** — rejected: presence spans "extensive" (Uber/Bolt) to "absent" (in-sample single-service poles); ride-hailing is the core even when bundled.

## Boundary Findings

- **vs Taxi Dispatch Platform (§18 sibling)**: the dispatch platform is operator-side machinery — a fleet/taxi operator manages incoming bookings, assigns drivers/vehicles as resources, runs the operation. The ride-hailing platform is passenger-side — the passenger creates the on-demand request and the platform matches it to live supply with passenger-visible tracking and platform-side fare accounting. The radio-dispatch room is the dispatch Type's lineage; the passenger-facing request→match→track loop is the ride-hailing Type's. Convergence: modern ride-hailing products dispatch taxis as a supply class (Uber Taxi; FREE NOW entirely), which is supply-mix inside the ride-hailing surface, not a Type change. Keep both; seam = who creates the request and whose operation the system manages.
- **vs On-demand Delivery Platform (§18 sibling)** — FLAG DISCHARGED: identical request→match→track machinery; the unit transported differs — people (passenger rides) vs goods (courier deliveries). The seam is vendor-drawn inside the archetype itself: Uber's own products split rides (passengers, e.g. Guest Trips) from Direct-style goods delivery, and Uber's ride FAQ routes "have an item delivered" to a package product rather than a ride. Keep both; the unit of transport is the boundary.
- **vs Car Sharing Platform / Micromobility Sharing Platform**: sharing Types hand the member the vehicle (member is the driver; passenger posture impossible); ride-hailing supplies the driver. Clean, ratified by both sibling passes.
- **vs Employee Transportation Platform / School Transportation / Non-emergency Medical Transportation**: those Types run closed eligible populations with program/employer/payer funding and (in NEMT) need/accommodation records. Ride-hailing's population is open to the public and anonymous-adjacent (one requester account; passenger may even differ). All three sibling passes name ride-hailing as the removal target — seam ratified from this side.
- **vs Mobility-as-a-Service Platform**: MaaS integrates multiple third-party providers behind one account for multimodal planning+booking; a ride-hailing platform operates its own (single-provider, single-network) supply and can itself be an integrated provider inside MaaS. Super-app bundling (food, scooters) inside a ride-hailing app is not multimodal integration.
- **vs Public Transit Passenger App**: scheduled public service vs on-demand private hire; transit app rides have no real-time driver matching.
- **vs Fleet Management System / Driver Management**: supply-side asset/crew management vs passenger-side matching and payment. Fleet-partner portals inside ride-hailing platforms (Bolt fleet dashboard, Uber Fleet audience) are supply-side adjacencies.
- **vs Food Delivery Marketplace**: goods vs people again, plus the marketplace's restaurant-aggregation core; the ride-hailing super-app that bundles food is bundling, not becoming.

## Historical / Market-Sample Check

Would older, regional, platform-native or differently positioned products still fit the L0?

- **Early taxi e-hail apps (Hailo-era, ~2011)**: passenger app requests, dispatch matches a licensed taxi, ride tracked via dispatch, platform records the ride and takes commission; fare metered, often paid in-cab. Fits L0 with metered pricing and taxi supply — therefore L0 must not require upfront pricing, dynamic pricing, or crowdsourced drivers. (Tier 3 class-level lineage reasoning; no live source fetched — recorded as inference, not observation.)
- **Regional players (Didi, Grab, Ola, Yango, Careem)**: same core loop with regional super-app wrapping. Fit L0; their breadth is L2 variant.
- **Radio dispatch / street hail**: no passenger-created digital request, no passenger-visible matching/tracking, no platform fare record — does NOT fit L0; this is the Taxi Dispatch Platform's ancestry, confirming the seam.
- **Corporate/car-service dispatch (black-car livery)**: account-based booking with scheduled pickups; when the service is pre-booked dispatch without an on-demand passenger request surface it sits on the dispatch side; when it offers the on-demand app loop it is ride-hailing with a premium fleet. L0 survives.

Conclusion: the L0 above is era- and region-robust; the modern smartphone + upfront + dynamic-pricing pattern is the dominant implementation, not the definition.

## Uncertainties

- Uber/Lyft/Bolt/FreeNow article-level rule details (exact cancellation fee windows, exact surge mechanics, exact driver-commission percentages) were not reachable; no precise numbers are claimed in the final document.
- Whether every market's ride-hailing product guarantees two-way (rider↔driver) ratings — FREE NOW's fetched page evidences driver ratings; bilateral rating is evidenced at Uber/Lyft/inDrive. Held as Common, not Core.
- Pooled/shared rides were not re-verified on live pages this pass; treated as a known variant (widely offered and later retired by some products) — no claims made.
- Regulatory naming (TNC, PHV) is region-specific vocabulary, not Type structure.

## Final Synthesis

A Ride-hailing Platform is a two-sided passenger-mobility platform. Its world is made of: **ride requests** (passenger-created, on-demand, origin→destination), **driver-and-vehicle supply** (individual drivers, fleets, or taxis, onboarded and qualified), **matching** (real-time assignment or offer/accept — with a negotiated-fare counter-pole), **the tracked trip** (live location, mutual identification, pickup→on-trip→completion), **the platform-recorded fare** (quoted, estimated, metered, or negotiated — settled in-app or recorded for cash), and **post-trip trust machinery** (two-way ratings, receipts, disputes, safety tooling).

The defining core is the four-property loop: on-demand passenger request + real-time matching to a specific available driver+vehicle + tracked mutually-identified trip + platform-priced/recorded ride with mediated settlement. Everything else — pricing philosophy, supply class, payment instruments, vehicle classes, scheduled rides, business tiers, super-app breadth — is variant structure. The Type ends where the requester stops being the public (program transportation), where the vehicle is handed to the member (car sharing / micromobility), where the unit becomes goods (on-demand delivery), where the passenger creates no request (taxi dispatch), or where many third-party providers are integrated behind one account (MaaS).
