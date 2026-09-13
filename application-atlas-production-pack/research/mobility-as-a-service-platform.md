# Research Notes — Mobility-as-a-Service Platform

## Research Goal

Understand what a Mobility-as-a-Service (MaaS) Platform actually is as an Application Type: what objects exist inside it (journeys, providers, accounts, bookings, tickets), how the plan→book→pay loop works across multiple transport providers, what "integration" concretely means in these products (deep vs shallow), who operates such services and on what platforms, and where the boundary lies against neighboring Types (Public Transit Passenger App, journey planners, Ride-hailing, Car Sharing, Micromobility Sharing, OTA/travel planners).

Directory context: leaf "Mobility-as-a-Service Platform", section 18 (Transportation, Mobility & Logistics). Research date: 2026-09-09.

## Initial Boundary (working hypothesis before research)

- Hypothesized core: one digital service that integrates multiple mobility providers (public transit, shared bikes/scooters/mopeds/cars, taxi/ride-hail, rental) so a traveler can plan a journey across modes, then book and pay for the chosen services through a single account.
- Suspected confusions:
  - Public Transit Passenger App (§18 sibling): one agency's network, plan + tickets for that network only.
  - Pure journey planners (no dedicated directory leaf): planning without booking/payment.
  - Ride-hailing / Car Sharing / Micromobility Sharing Platforms (§18 siblings): single-provider operators; MaaS aggregates them.
  - Online Travel Agency / Travel Itinerary Planner (§26): multi-day travel commerce, not urban door-to-door mobility.
  - Corporate Travel Management (§10): employer-side; MaaS mobility budgets touch this seam.

## Research Questions

1. What is the central object — the journey, the booking, the account, or the provider integration?
2. How does a journey go from search → option selection → booking → payment → usage → receipt?
3. What does "one account" mean concretely (registration, verification, per-provider connection, payment methods)?
4. What is integrated: planning only, booking, payment, tickets, support, rules?
5. Where does integration visibly stop (app-scoped purchases, per-provider support, per-provider cancellation rules)?
6. Who operates MaaS services (transit agency, city, private startup, corporation) and how is the software delivered (own brand, white label, API)?
7. What commercial models exist (pay-as-you-go, subscription bundles, mobility budgets, vouchers)?
8. What does the operator side look like (back office, analytics, data management)?
9. Boundary: what exactly separates MaaS from a journey planner, from a transit app, from a single-provider app?

## Representative Products

| Product | Operator posture | Form | Philosophy pole |
|---|---|---|---|
| Jelbi (BVG Berlin, powered by Trafi) | public transit authority-led city service | consumer app | city-partnership MaaS, pay-as-you-go + tickets |
| Trafi | B2B platform vendor (acquired by Enghouse 2025) | white-label platform + back office | turnkey city deployments (Jelbi, Floya, Breeze, MVG, yumuv, Vilnius) |
| Moovit | global private tech (Intel-owned lineage) | consumer app + B2B MaaS solutions arm | planner-first, global scale, wallet + tickets |
| SkedGo (TripGo) | B2B platform vendor | API/SDK/white-label/web planner | API-first, project-tailored deployments (TfGM, ODIN PASS, placie, Feonix, Optus) |
| Whim (MaaS Global) | private startup, Helsinki | consumer app | subscription-bundle archetype — UNREACHABLE, market anchor only |

Selection rationale: two consumer-facing services with different operator postures (authority-led Jelbi vs global-tech Moovit) and two B2B platform vendors with different delivery philosophies (turnkey white-label Trafi vs API-first SkedGo). Whim was selected for the subscription-bundle pole but its official surfaces were unreachable (see Sources).

## Sources

Fetched 2026-09-09 (all official vendor surfaces):

- Jelbi — https://www.jelbi.de/en/home/ (root), https://www.jelbi.de/en/jelbi-app-2/ (app page incl. video transcripts), https://www.jelbi.de/en/faq/ (FAQ — Tier 1)
- Trafi — https://www.trafi.com/ (root), https://www.trafi.com/white-label-product (product page)
- Moovit — https://moovit.com/ (root), https://moovit.com/features/ (app features), https://moovit.com/maas-solutions/ (B2B platform)
- SkedGo — https://skedgo.com/ (root), https://skedgo.com/what-is-mobility-as-a-service-maas/ (definitional article, quotes MaaS Alliance)

Unreachable (recorded per evidence rules):

- Whim — https://whimapp.com/ (transport error), https://support.whimapp.com/hc/en-gb (transport error), https://maas.global/ (transport error), App Store listing (redirected to store front page). No Whim-specific claims are made anywhere in this research.
- HSL HOP — https://www.hsl.fi/en/hop (403), https://hop.hsl.fi/ (transport error). Abandoned after 2 failures.

Evidence layers used below: **A** = directly observed on one product's official source; **B** = cross-product commonality; **C** = canonical inference from comparison + boundary reasoning.

## Product Observations

### Jelbi (BVG Berlin, powered by Trafi) — evidence layer A

From the official site (root, app page, FAQ):

- Self-definition: "Berlin's entire public transport and sharing services in just one app. Register once to use all: bus, train, e-moped, e-scooter, bike, car and taxi." Flow: "Sign up on Jelbi. Validate your documents and add a payment method. Enter a destination to see available routes. Then, choose your preferred mobility mode. Ride, enjoy, arrive, and pay. All in one app!"
- Positioning: "from journey planning to booking and payment. All in the Jelbi app."
- Partners bookable in-app: public transport (VBB tickets, zones A/B/C), free-floating car sharing (MILES, SIXT share), bike sharing (nextbike, Bolt, Lime), e-moped sharing (emmy), e-scooter sharing (Bolt, Voi, Lime), taxi (Taxi Berlin). Some partners present at Jelbi stations but NOT yet bookable in-app (Cambio carsharing, Cargoroo cargo bikes) — station presence ≠ in-app booking.
- Registration: BVG account reuse (Tickets/Fahrinfo apps share credentials) or new sign-up: email + confirmation link, personal information, mobile number verified by 4-digit SMS code, payment method (card/SEPA/PayPal; later Google Pay/Apple Pay), and — for license-requiring modes — driving licence + ID verification through a third-party ID provider (Veriff). EEA/CH/UK documents only.
- **Partner "Connect" model**: after registration, the user sees all partner services in their profile and clicks "Connect" per partner. "You don't need to connect with all partners – just the ones you actually want to use." Connections to car/scooter partners are blocked until licence verification completes. Data protection: "Only those partners you actively connect to … will receive the data they need in order to provide you with your journey."
- Booking: two entry paths from the home screen — (1) "Where to?" destination search returning "the best routes with prices, travel times, and available services", then choose and confirm; (2) tap a mode icon directly. "The app guides you through the booking process step by step, providing you with everything you need, e.g. a PIN to unlock a bicycle."
- Tickets: a "Tickets" tab sells VBB public transport tickets (nearly all BVG Tickets app fares; a few exceptions named); Deutschland Ticket can be displayed in-app; "My Tickets" holds purchased tickets.
- Trips and money: "My trips" lists all journeys with dates, prices, services used; per-journey invoice download (provider-specific quirks: nextbike invoices monthly; Lime invoices via the provider's own support page); a confirmation email per completed journey.
- Payment: "you save your payment information once and can then use all the services available in the Jelbi app." PSP migration (LogPay→Adyen) documented with no data migration; outstanding-payment blocking with automatic retry over a defined window, then the account stays blocked.
- Vouchers: prepaid voucher selected as payment type BEFORE booking; no retroactive use; overage auto-deducted from the private payment method; campaign rules may exclude transit ticket purchases.
- Cancellation rules are per-provider: emmy/MILES/TIER/nextbike bookings cannot be cancelled (just end them); BerlKönig and taxi rides can be cancelled in-app with fees shown.
- Provider rules surface inside Jelbi: MILES best-price principle (per-km vs day/hour packages auto-compared), minimum amounts, EV charge thresholds gating trip end, rookie fees; SIXT PIN requirement, reservation limits, age restrictions per vehicle class (reservation button greyed out when unmet); Bolt per-second billing.
- Support routing: "Please contact the partner with whom you booked the trip/ticket. You can call the provider from within the app." General Jelbi questions go to BVG support. Invoice/complaint routing is per-provider.
- Account lifecycle: 18+; licence re-verification cycle (from April 2024 every three years, with email notice 28 days ahead and in-app banners; status "Verified"→"Expired" after a grace window, blocking car/moped services only).
- App-scoped purchases: tickets bought in the BVG Tickets app are NOT available in Jelbi ("tickets are only available in the apps in which you bought them"); third-party subscriptions/packages bought elsewhere are not usable in Jelbi; "Each app shows you only what you bought in that app."
- Jelbi stations: physical hubs at rail stations concentrating sharing services — "the analogue twins of the digital app"; book, return, charge there; in parts of central Berlin micromobility drop-off is restricted to Jelbi locations ("Jelbi points").
- Accessibility: step-free route toggle "for anyone with accessibility needs."
- Referral program with reward caps; account deletion via app or email.

### Trafi (B2B white-label MaaS platform) — evidence layer A

From the official site (root, product page):

- Self-definition: "B2G multi-modal and fully integrated journey planning technology platform"; white-label app includes "the ability to find, book, and pay for rides on the full range of public transport and new mobility (MSP) modes."
- **Register-once principle**: "the user will only need to register his/her account once, validate the driver's license once, and add payment method once to use it for all journeys with all transport modes. No need for re-registration with each individual mobility provider."
- Intermodal routing: "reflects specific user constraints and preferences, allowing for combinations of different transport modes. All recommendations are based on the schedules, real-time vehicle position and availability and pricing." Disruption notifications "layered on top of routing."
- Booking: "Reserve and unlock any vehicles with a single app without the need to register first on the vehicle provider site. Single-Click access to any of the integrated modes using the universal QR code scanner on the home screen."
- Support obligation: "The promise to provide find, book, pay and ride capabilities in a single app brings with it the often forgotten obligation to also provide support and help screens for all the integrated modes" — per-provider/mode help content plus access to the provider's customer support.
- Back office (operator side): respond to user-reported issues, detect likely fraudulent transactions, restrict access to specific vehicles (e.g. expensive shared cars), generate financial and usage reports, run marketing/information campaigns, manage promotions, monitor performance in real time. "GDPR compliant by design… tools they need to operate a MaaS scheme day to day."
- Data tools: Data API, BI (data warehouse, reporting, dashboards); clients own their data. Data categories: user info/activity, travel habits, feedback, transactional data, transit infrastructure data, schedules, integrated providers' fleet distribution and utilization.
- Mobility Intelligence Platform: static data management — "refine and enhance public transport data such as stop locations, schedules, shapes as well as fares."
- Mobility Budgets: employer console to generate/assign budgets and control costs + an extra payment option in the white-label app for employees.
- Extensions: Margento (ticketing hardware validators, ABT) as a sibling product line.
- Deployments named: Berlin (Jelbi/BVG), Brussels (Floya/STIB), Solent (Breeze), Munich (MVG), Zurich/Basel/Bern (yumuv), Vilnius (Trafi), Nottingham & Derby (Ride). Acquired by Enghouse Transportation April 2025.

### Moovit (consumer app + MaaS solutions arm) — evidence layer A

From the official site (root, features, MaaS solutions):

- Consumer app positioning: "One Mobility App: All Your Local Transit Options"; multimodal trip planner showing "all the mobility possibilities available."
- Planning features: route choice across modes, real-time arrival info, favorite lines/stations/places, real-time service alerts (construction, delays, disruptions), bike routes + shared-bike docking-station availability.
- **Mobility Wallet**: "Create an account and choose your preferred way to pay for mobility options around you – Public Transit, Carpool and On-Demand services. Your purchased tickets, ride history, payment details and billing history are available here." Fare types; rider/pass profiles with discounts; buy multiple tickets for multiple people; validate digital pass (show or scan) — "Available in select cities."
- Guidance: live step-by-step navigation, AR "Way Finder" stop location, offline map PDFs, get-off notifications.
- Crowdsourcing: report line changes, wrong data, add station photos, edit station info.
- Accessibility: VoiceOver/TalkBack, larger hit targets, wheelchair- and stroller-accessible route options.
- MaaS Solutions (B2B): "modular MaaS platform" — branded apps, fare payments, urban mobility analytics, on-demand solutions, real-time bus info (TimePro), public transit APIs, transit data manager (GTFS editor). Assets: multimodal trip planner, transit data repository (7,000+ agencies claimed), people's-movement data.
- Vendor scale claims: planner connected to 360+ micromobility providers in 270 metros; service in 3,500 cities / 112 countries. (Marketing figures — recorded, not generalized.)

### SkedGo (TripGo API-first platform) — evidence layer A

From the official site (root, MaaS article):

- Self-definition: "Integrated Mobility Solution and Mobility-as-a-Service (MaaS) Platform Provider"; "Our mobility platform lets you create apps and solutions providing seamless and personalised door-to-door trips using any public, private or commercial mode of transport. This includes real-time data as well as integrated bookings and payments. It's a single API connecting you to thousands of transport providers around the globe."
- Platform capabilities: door-to-door trip planning with any mix of public/private/commercial modes incl. ride and car shares; real-time results (predicted times, GPS positions, alerts; update cadence varies by region); parking & location support; **booking & payment** ("Mobile ticket purchase straight through the app… Integrated wallets and mobility budget configurations"); data analytics; agenda/calendar integration (auto-planning trips around calendar events).
- Delivery forms: API, SDK, white label, journey-planner widget, showcase app (TripGo).
- Definitional article (quoting the European MaaS Alliance): "put the users at the core of transport services, offering them tailor made mobility solutions based on their individual needs… easy access to the most appropriate transport mode or service will be included in a bundle of flexible travel service options for end users."
- Before/after framing: without MaaS users "plan, book and pay all transport options separately"; with MaaS "getting from A to B becomes a more fluid, integrated experience."
- Commercial models described: **'Plan'** (monthly subscription suited to transport needs — urban commuter, family, business, casual — including transit, taxi, rental, car share) and **'Pay on demand'** (pay for the whole multimodal trip in one go, independent of transport means).
- Deployment spectrum (case studies on the same pages): web journey planner embedded in an authority's website (TfGM — buses/trains/trams, CO₂ per journey, prioritize by carbon/time/convenience/cost); plan + book + pay + employer travel declaration (PON, Netherlands); subscription MaaS trial with 8 modes (ODIN PASS, Queensland); city web planner including taxis, Uber, car rentals, school buses, wheelchair-accessible services (Transport Canberra); one-stop app comparing pricing across taxi and ride-hailing providers with in-app booking and payment (placie, Australia); accessibility-first apps for underserved populations with mobility wallets and admin dashboards for providers without ride-scheduling technology (Feonix, US); corporate white-label employee app with calendars, SMS alerts, closed user group (Optus); DRT + public transport door-to-door (ITOCHU/Shotl, Japan); active-travel city planner with cost/calories/carbon per journey (Leicester).

## Cross-product Comparison

| Structure | Jelbi | Trafi | Moovit | SkedGo | Layer |
|---|---|---|---|---|---|
| Multimodal journey planning across multiple providers | A: destination search → routes with prices/times/services across transit + 6 sharing/taxi partners | A: intermodal routing combining modes, schedules + real-time + pricing | A: multimodal trip planner "all mobility possibilities" incl. micromobility providers | A: door-to-door planning, any mix of public/private/commercial modes | B |
| Single account across providers (register once) | A: one Jelbi account; per-partner Connect; no re-registration per provider | A: register once, validate licence once, add payment once — all modes | A: Mobility Wallet account pays for transit/carpool/on-demand | A: integrated wallets; single API relationship behind the app | B |
| Booking/purchasing through the platform | A: book rides in-app; buy VBB tickets in Tickets tab; guided booking (unlock PINs) | A: reserve and unlock any vehicle; universal QR scanner | A: purchase tickets, pay for rides; pass validation (select cities) | A: integrated bookings; mobile ticket purchase through the app | B |
| Unified payment | A: payment method entered once, used for all services; vouchers; blocked-account handling | A: add payment once for all modes | A: wallet holds payment details + billing history | A: integrated payments, wallets, budget configurations | B |
| Real-time information on planning | A: "real-time routing information and available services" | A: real-time vehicle position/availability; disruption notifications | A: real-time arrivals + service alerts | A: real-time data incl. GPS positions, alerts | B |
| Option comparison at planning time | A: compare by price, travel time, weather, occasion, mood | A: recommendations based on schedules/real-time/pricing | A: choose journey that fits needs | A: TfGM/Leicester deployments compare cost/time/CO₂/calories | B |
| Public-transport ticketing in-product | A: Tickets tab, Deutschland Ticket display | A: via Margento extension (validators/ABT) | A: fare payments module; tickets in select cities | A: mobile ticket purchase | B |
| Trip history + receipts | A: My trips + per-journey invoices + confirmation email | A: financial/usage reports (operator side) | A: ride history + billing history in wallet | A: transactional data captured | B |
| Per-provider rules/instructions in-product | A: extensive per-provider FAQ content (PINs, pricing principles, EV thresholds) | A: help screens per provider/mode | — (not observed) | — (not observed) | A→B (2/4 observed, treated common-mature) |
| Support routed to booked provider | A: contact/call the partner from within the app | A: access to provider's customer support | — | — | A→B (2/4) |
| Credential verification tiers | A: licence + ID verification gates car/scooter connections; periodic re-verification | A: validate driver's licence once | — | — | A→B (2/4) |
| Accessibility | A: step-free routes | — | A: wheelchair routes, screen readers | A: accessibility features headline; Feonix deployments | B |
| Operator back office | (BVG operates; not exposed) | A: full back office (support, fraud, reports, campaigns, monitoring) | A: analytics module | A: admin dashboards (Feonix) | B (platform-form products) |
| Data/analytics for the operator | — | A: Data API, BI, data warehouse | A: urban mobility analytics | A: granular mobility data analytics | B (platform-form) |
| Subscription bundles / plans | — (pay-as-you-go + tickets) | — (budgets instead) | — | A: ODIN PASS subscription; 'Plan' model described | A (SkedGo-described + ODIN PASS) — variant |
| Employer mobility budgets | A: Mobility Budget page exists (B2B offer) | A: Mobility Budgets module | — | A: mobility budget configurations | B (3/4) — variant |
| Physical stations/hubs | A: Jelbi stations/points | — | — | — | A — product-specific |
| Crowdsourced data editing | — | — | A: report/edit station data | — | A — product-specific |
| Agenda/calendar integration | — | — | — | A: agenda integration | A — product-specific |
| CO₂/sustainability metrics | — | A: climate-goals framing | A: sustainability program | A: CO₂ per journey (TfGM, Leicester) | B — variant |
| DRT integration | — | A: DRT management mentioned | A: on-demand solutions | A: DRT + MaaS (Japan POC) | B — variant |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Three jointly-held structures (evidence layer C, supported by B across all four products):

1. **Multimodal journey planning across multiple integrated transport providers** — the traveler enters origin/destination and receives route options that combine modes offered by more than one provider (scheduled transit plus shared, on-demand, or commercial modes). Remove → a single-provider app (transit passenger app, ride-hailing, car sharing, micromobility) or a read-only journey planner.
2. **The single mobility account as the access substrate** — one registration binding identity and payment that works across the integrated providers, so the user does not re-register with each provider; mode-gated credential verification (e.g. driving licence) attaches to the account where modes require it. Remove → per-provider apps; the "as-a-Service" integration collapses into a link farm.
3. **Booking and payment executed through the platform** — the chosen option is transacted in-product (ticket purchase, vehicle reservation/unlock, ride booking) and charged to the unified payment arrangement, producing a platform-side trip/transaction record. Remove → planning-only journey planner, or a per-transaction link-out aggregator.

Jointly-held tests:

```text
1 alone                          → journey planner (information only)
2 alone                          → fare card / payment wallet
3 without 1+2                    → a set of booking forms
1+2 without 3                    → planner with saved payment, no transactions
2+3 without 1                    → booking portal without discovery
1+3 without 2                    → guest checkout per provider — below the Type
                                   (the standing account is what makes it a service)
```

Anti-overfit notes:
- **Subscription bundles are NOT definitional.** The subscription-bundle archetype (Whim) was unreachable; the sampled set contains a pay-as-you-go + tickets pole (Jelbi), a subscription trial (ODIN PASS on SkedGo), and employer budgets (Trafi/Jelbi/SkedGo). Commercial model is a variant axis.
- **Real-time is NOT definitional.** Trafi's own wording bases recommendations on "schedules, real-time vehicle position and availability and pricing" — schedules alone are the floor; real-time is common-mature.
- **Mobile app form factor is NOT definitional.** SkedGo powers web journey planners embedded in authority websites (TfGM, Canberra, Darwin); the account + booking layer can be web.
- **"Platform" in the leaf name covers both faces**: the traveler-facing service (defining surface) and the operator-facing machinery (back office/integrations) that platform vendors deliver as the product. The traveler face is what makes the Type recognizable; the operator face is common structure for platform-form products.

### L1 — Common Mature Structure

- Real-time information layered on planning (arrivals, vehicle positions/availability, service alerts/disruption notifications).
- Option comparison at planning time (price, duration; commonly CO₂, comfort, accessibility).
- Public-transport ticketing in-product (purchase + display/validate).
- Trip history with receipts/invoices and confirmation communications.
- Per-provider rules, instructions and support routing surfaced in-product (the platform carries each provider's operating quirks — unlock PINs, pricing principles, vehicle-condition rules — and routes support to the booked provider).
- Credential verification tiers (licence/ID for vehicle-operating modes), including periodic re-verification and expiry states.
- Accessibility support (step-free/wheelchair routing, screen-reader support).
- Operator-side machinery for platform-form products: back office (user-issue handling, fraud controls, vehicle-access restrictions, financial/usage reporting, campaigns, real-time monitoring), data analytics/APIs, static transport-data management.

### L2 — Variant / Optional Structure

- Commercial model: pay-as-you-go vs subscription bundles/plans vs employer mobility budgets vs prepaid vouchers/wallets.
- Operator posture: transit authority/city-led (Jelbi/BVG pattern), private startup, global tech, corporation (employee mobility), nonprofit/equity programs (Feonix).
- Delivery form: own-brand consumer app vs white-label app vs API/SDK/widget vs embedded web planner.
- Scope: single city vs region vs multi-city; urban vs regional/rural (DRT integration).
- Physical mobility hubs/stations binding the digital service to places.
- Sustainability metrics (CO₂ per journey), agenda/calendar integration, crowdsourced data editing, corporate travel declaration, tourism/lifestyle add-ons.

### L3 — Vendor-specific (Research Notes only)

- Jelbi: Jelbi stations/points, Veriff as ID provider, LogPay→Adyen PSP switch, 3-year licence re-verification cycle with 28-day notice, MILES best-price principle details, SIXT PIN/reservation limits, referral caps (10), BerlKönig termination handling, nextbike monthly invoicing.
- Trafi: Margento extension, "Mobility Intelligence Platform" branding, Enghouse acquisition, named deployment list.
- Moovit: TimePro, Transit Data Manager, Way Finder AR, provider/metro/city counts (marketing claims), crowdsourcing editor.
- SkedGo: TripGo branding, 10–60s update cadence, named case-study deployments.

## Vendor-specific Findings

See L3 above. None of these enter the canonical core.

## Boundary Findings

1. **vs Public Transit Passenger App (§18 sibling)** — the transit passenger app centers ONE agency's network: plan + tickets + service info for that network. MaaS centers the integration of MULTIPLE providers, with transit as one option among several. Removal test: remove the multi-provider booking/account layer from a MaaS platform → a transit passenger app; add partner booking to a transit app → it grows into MaaS. Moovit sits near this seam: planner-first consumer app whose booking/payment layer (Mobility Wallet, tickets "in select cities") is thinner than Jelbi's — held in-type at the planner-heavy pole because the account+payment layer exists; a planner with NO account/booking layer would fall below the Type. **Flag for joint review when public-transit-passenger-app is processed.**
2. **vs pure journey planners (no dedicated directory leaf)** — planning is one leg of MaaS, not the whole. A planning-only product (no account, no booking, no payment) is upstream capability, not this Type. The directory currently has no leaf for standalone journey planners; their closest anchors are Public Transit Passenger App and this leaf. Recorded as a taxonomy observation, not resolved here.
3. **vs Ride-hailing Platform / Car Sharing Platform / Micromobility Sharing Platform (§18 siblings)** — those operate a fleet/service; MaaS is the intermediary that plans, books and pays across such operators. The micromobility pass already recorded this seam from the operator side ("aggregator vs operator"). Removal test: remove the multi-provider integration → the product becomes one of the operators.
4. **vs Taxi Dispatch Platform** — single-provider dispatch vs multi-provider integration; taxi is one bookable service inside MaaS (Jelbi books Taxi Berlin).
5. **vs Online Travel Agency / Travel Itinerary Planner (§26)** — OTA centers multi-day travel commerce (flights, hotels, packages) with a different unit of sale; MaaS centers urban/short-range door-to-door mobility consumed as individual trips or subscriptions. Different provider class, different trip grain.
6. **vs Corporate Travel Management Platform (§10)** — employer-side authorization/booking/reporting for business travel vs traveler-facing mobility service. The seam is mobility budgets: the employer funds, but the MaaS account and the plan-book-pay loop remain the traveler's.
7. **vs Smart City Operations Platform (§24)** — city-side operations/analytics vs traveler-facing service; the MaaS operator back office (Trafi-style) is the platform's own administration, not city operations.
8. **What MaaS is NOT despite marketing**: fare/media integration alone (a multi-operator transit card without planning/booking) is fare integration, not MaaS — it fails legs 1 and 3. This gives the historical check its edge case.

## Historical / Market-Sample Check

- The Type is young (the term and the archetype services date from the mid-2010s), so the check asks whether the definition over-fits the current smartphone-app implementation:
  - Form factor: web-embedded planners with accounts and booking (SkedGo deployments) satisfy the core without a native app. ✔
  - Real-time: schedule-based planning satisfies the floor (Trafi's own wording). ✔
  - Commercial model: pay-as-you-go (Jelbi, placie), subscription (ODIN PASS), budgets (Trafi) all satisfy — no single model required. ✔
  - Operator posture: authority-led, private, corporate all satisfy. ✔
  - Pre-MaaS analogs: multi-operator fare cards fail legs 1+3 → correctly excluded; single-agency transit apps with tickets fail leg 1's multi-provider requirement → correctly excluded. The definition does not accidentally swallow them.
- Regional spread in-sample: Germany (Jelbi), Lithuania/Europe-wide platform (Trafi), Israel/global (Moovit), Australia/UK/US/Japan deployments (SkedGo). Not Europe-only. ✔

## Uncertainties

1. **Whim unreachable** — the subscription-bundle archetype could not be verified from official sources. The subscription variant is therefore evidenced indirectly (SkedGo's ODIN PASS case study and its 'Plan' model description). No Whim-specific claims are made.
2. **Depth-of-integration spectrum** — how deeply booking is integrated varies (Jelbi: full in-app transaction with per-provider quirks; Moovit: wallet + tickets "in select cities"). The floor (in-product transaction + unified payment) is held as L0; the ceiling is product-specific. Whether a "planner + wallet only, no booking" product exists in the market is unverified.
3. **Public Transit Passenger App seam** — flagged for joint review; this pass records the removal tests but does not resolve the sibling's definition.
4. **Pure journey planners** — no directory leaf exists; whether the taxonomy needs one is a taxonomy-owner question, recorded in Boundary Issues.
5. **Provider-count/scale figures** (Moovit's 360+ providers, 7,000 agencies, 3,500 cities) are vendor marketing claims, recorded here but not asserted as Type facts.

## Final Synthesis

A Mobility-as-a-Service Platform is a traveler-facing mobility service whose defining structure is three jointly-held legs: **multimodal journey planning across multiple integrated transport providers**, **one account binding identity and payment across those providers** (register once, connect per provider, verify credentials where modes require), and **booking and payment executed through the platform** (tickets, vehicle reservations/unlocks, ride bookings — transacted in-product, recorded as platform-side trips with receipts). Everything else commonly associated with MaaS — real-time information, price/CO₂ comparison, subscription bundles, employer mobility budgets, physical stations, operator back offices and analytics — is common mature structure or variant, not definition. The Type is realized across a delivery spectrum (own-brand app, white-label app, API/SDK, embedded web planner) and an operator spectrum (transit authority, city, private operator, corporation), with platform vendors (Trafi, SkedGo, Moovit's MaaS arm) supplying the machinery behind authority- and city-branded services. The boundary is sharpest against single-provider mobility Types (the operator siblings of §18) and against planning-only journey tools; the seam with the Public Transit Passenger App is flagged for joint review.
