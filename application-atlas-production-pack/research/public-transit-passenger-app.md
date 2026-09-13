# Research Notes — Public Transit Passenger App

## Research Goal

Understand what a rider-facing public transit passenger app actually is as an Application Type: what objects exist inside it (network, lines, stops, timetables, real-time vehicle state, journeys, tickets/fares, alerts), what the rider's central loop is (plan → ride → pay), whose app it is (agency-branded vs independent vs white-label platform), which capabilities are definitional vs common vs variant, and where the boundaries lie against neighboring Types (Mobility-as-a-Service Platform, Public Transit Operations Platform, Rail Booking & Ticketing, Ride-hailing/Micromobility, general mapping products).

This pass also discharges two inherited flags:
1. **MaaS joint-review flag** (mobility-as-a-service-platform, processed 2026-09-09): confirm the removal tests from this side; the MaaS pass held Moovit in-type at the planner-heavy pole and asked this pass to confirm "remove the multi-provider booking/account layer → transit passenger app".
2. **Ops-platform seam** (public-transit-operations-platform, processed 2026-09-09): the ops pass named this leaf as the rider-facing counterpart that *consumes* the real-time data the ops platform *produces*; confirm the seam from this side.

## Initial Boundary

- **What it probably is:** the passenger's companion application for using a scheduled public transport network — plan journeys on the network, follow them in real time, and (commonly) pay/ride with tickets or fare accounts.
- **Users:** transit riders (commuters, occasional riders, visitors). The *publisher* of the app varies: the agency/authority itself, an independent company, or a platform vendor white-labeling for the agency.
- **Nearest neighbors:** Mobility-as-a-Service Platform (multi-provider booking under one account), Public Transit Operations Platform (operator side of the same data), Rail Booking & Ticketing (long-distance rail commerce), Ride-hailing / Micromobility / Car Sharing (on-demand or self-operated modes), Parking Application, general mapping/navigation products (no dedicated leaf).
- **Unknowns going in:** Is ticketing definitional or variant? Is real-time definitional or a layer over the schedule? Is journey planning definitional (vs arrivals-only utilities)? Where do pure journey planners sit? Does the white-label platform layer change the Type?

## Research Questions

1. What are the core objects (network/lines/stops/timetables, journey/itinerary, real-time vehicle state, tickets/fares, alerts, favorites)?
2. What is the central interaction loop, step by step?
3. What does journey planning concretely consist of (inputs, option comparison, time constraints, itinerary structure)?
4. What real-time information is surfaced, and what happens when real-time is unavailable?
5. How does fare payment/ticketing work where present (buy, activate, display/validate, capping, accounts)? Is it present in all products?
6. Whose app is it — official agency app, independent multi-city app, white-label platform — and how does that change content and rules?
7. What rider-side extras exist (crowdsourcing, feedback to agencies, accessibility, subscriptions)?
8. Where are the boundaries — MaaS, ops platform, rail booking, ride-hailing, general maps, arrivals-only utilities?
9. Historical check: do schedule-only planners, arrivals-only apps, and info-only official apps still fit the definition?

## Representative Products

| Product | Publisher posture | Shape in sample |
|---|---|---|
| **Citymapper** | independent company (now part of Via); multi-city consumer app + "Citymapper for Cities" B2B | planner-heavy consumer pole |
| **Moovit** | independent company; consumer app + MaaS solutions arm (branded apps, fare payments) | planner + select-city wallet/tickets + white-label |
| **Transit** | independent company; consumer app + official-app platform for 220+ agency partners | planner + agency ticketing + crowdsourcing |
| **Umo (Cubic Transportation Systems)** | fare-collection vendor's passenger app platform for agencies | ticketing-heavy, white-label, multi-system |
| **BVG Fahrinfo** | official app of Berlin's transit authority (BVG) | official single-network app, full fare media |
| **Transport for NSW apps (Opal Travel, Trip Planner)** | official apps of the Australian state authority | official authority apps, planning + real-time + fare account |

Selection rationale: market representation (the three global independent planners are the category's consumer face; Umo/Cubic and BVG represent the agency/fare side), documentation completeness (Transit's help center is deep operational documentation), different product philosophies (independent planner vs official authority app vs fare-vendor platform), different customer levels (rider-direct vs agency-as-customer), and regional spread (Israel/global, UK/EU, North America, Germany, Australia).

## Sources

- Citymapper — root: https://citymapper.com/ ; news: https://citymapper.com/i/2809/making-bus-rides-better ; B2B (Via): https://ridewithvia.com/solutions/citymapper
- Moovit — app features: https://moovit.com/features/ ; branded apps: https://moovit.com/maas-solutions/branded-apps/ ; root: https://www.moovit.com/
- Transit — root: https://transit.app/ ; help center: https://help.transitapp.com/ with articles 93 (how to use), 94 (plan a trip), 91 (GO crowdsourcing), 445 (track departures), 389 (buy tickets), 392 (fare capping), 107 (manage transit options)
- Umo — riders: https://umomobility.com/riders/ ; agency app: https://umomobility.com/transit-agencies/umo-app/ ; root: https://umomobility.com/
- BVG — Fahrinfo app: https://www.bvg.de/en/subscriptions-and-tickets/all-apps/fahrinfo-app
- Transport for NSW — transport apps: https://transportnsw.info/apps
- Inherited (not re-fetched, cited as prior-pass evidence): research/mobility-as-a-service-platform.md (Moovit Mobility Wallet detail, Jelbi/BVG MaaS pattern); research/public-transit-operations-platform.md (RTPI production, GTFS-class seam)

Research date: 2026-09-09.

**Source-access limitations:**
- TfL (tfl.gov.uk/apps) and MTA (new.mta.info/apps) returned HTTP 403 — two prominent official authority apps could not be fetched. The info-only official pole is therefore evidenced indirectly (Transit's documented schedule-only cities; TfNSW's planning-only Trip Planner app; the historical generation). No MTA/TfL-specific claims are made.
- Moovit's "Long Distance Tickets" page and Umo's "Explore, Pay, Go" page returned 404; Moovit's long-distance-ticket offering is evidenced only by its navigation label, and Umo evidence rests on two official marketing pages plus the existence of its rider support portal.
- Citymapper's /cities page is JS-rendered (no content); Citymapper consumer evidence comes from the root page, one news post, and Via's B2B page.

## Product Observations

### Citymapper (Layer A unless noted)

- Positioning: "The Ultimate Transport App" / "Making Cities Usable"; "All the major transit cities of the world, managed by our unique data factory, maintaining the highest quality information". [A]
- B2B: "we work with cities and agencies to offer award winning journey planning, plus unique rider insights and tools to optimise transport networks". [A]
- Via's Citymapper-for-Cities page: "co-branded, award-winning MaaS app that attracts and retains riders by helping them easily discover, navigate, and pay for transit"; agencies get "aggregated user data — from demand patterns to bus stop usage" and "real-time, geo-fenced disruption alerts as well as personalized updates about your network". [A]
- Consumer features (news post): live bus locations on the map ("updated every minute"), live traffic updates re-timing journeys, route diversions on the map showing "which stops are skipped" and "where the bus rejoins its normal route"; earlier London bus pilot 2017. [A]
- News titles evidence: AI route choice (CLUB beta), iOS Lock Screen Navigation ("Track GO trips"), calendar sync ("plan trips to calendar events"), "pick the best time to leave", "Best Section" (train direction), CLUB features opened to all, Citymapper joined Via. [A]
- No consumer ticketing documented for the general app in this pass's sources; "pay for transit" appears in the co-branded MaaS-app framing. [A — absence claim limited to fetched pages]

### Moovit (Layer A)

- Positioning: "One Mobility App: All Your Local Transit Options — A seamless journey to get anywhere in your city"; self-described "#1 commuter app" with scale claims (1.7 billion users, 3,500 cities, 112 countries — marketing figures, L3). [A]
- App features page organized in four pillars: [A]
  1. **Plan Your Journey** — "multimodal trip planner shows all the mobility possibilities"; real-time arrival info ("know your lines ETA ahead of time"); favorite lines/stations/places; real-time service alerts ("construction, delays, and other disruptions"); bike routes & docking-station info.
  2. **Pay For Your Ride** — Mobility Wallet account ("purchased tickets, ride history, payment details and billing history"); rider/pass profiles with discounts; "Purchase Your Public Transport Tickets … buy as many tickets as you need and board with multiple people"; "Validate Your Digital Pass — show the driver your digital pass or scan the barcode to activate"; "* Available in select cities".
  3. **Get Guidance on Your Way** — live navigation ("step-by-step directions with live guidance from A-to-B"); Way Finder AR to locate the stop; offline map PDFs; "Never Miss Your Stop — receive automatic notifications on when to get off".
  4. **Powered by the Wisdom of the Crowd** — report line changes, report wrong data, add station photos, edit station information.
- Accessibility commitment: VoiceOver/TalkBack, larger hit targets, wheelchair-/stroller-accessible routes in the planner. [A]
- Branded apps (B2B): white-label app ("Multimodal trip planning, Real-time arrivals, Customized micro-mobility integrations, Innovative payment integration options" — Android, iPhone, web) + co-branded app + Transit Data Manager ("GTFS editor" + service-alert creation and real-time rider notifications). [A]
- Testimonials confirm deployments: JAUNT/First Transit, Boston University shuttle, Academy Bus (with Masabi ticketing), ATAF (Florence), Community Living Toronto. [A]
- Navigation also exposes "Long Distance Tickets" and a Web App item (page not fetched — 404). [A — label only]

### Transit (Layer A — deepest operational documentation in sample)

- Positioning: "the best app for buses and trains"; "See nearby transit, Real-time data, Plan a trip, GO"; 1000+/1200+ supported cities (marketing figure). [A]
- Main screen: "a map with your location and a list of nearby transit lines including their next departure time"; swipe a line to switch direction; "Real-time departures are marked with radio waves"; tap a line → later departures, nearest stop, track the vehicle. [A]
- Trip planning: search bar → destination (typed, map point, favorite, calendar/contacts address) → "Compare your options using public transport and other modes" → trip details → GO. Time constraints: "Leave Now", "Leave at", "Arrive by". Instant-ETA predictions to likely destinations (work/home). Calendar integration. [A]
- **GO** — "Transit's personal trip companion": "timely notifications for when it's time to leave, to change lines, and to get off the bus or the train"; using GO "anonymously shares your bus or train's location with other users, improving the accuracy of real-time info in your city"; crowdsourced vehicles shown with an avatar; fills real-time gaps (Vancouver SkyTrain example: "routes that are otherwise missing real-time information"). [A]
- **Departure states** (tracking article): real-time (pulsating waves) vs scheduled (greyed-out posted schedule) vs "Skips this stop" vs "Cancelled" (agency-reported) vs "Likely cancelled" (Transit's own inference from missing real-time data). Crowding information from agency sensors and from Rate-My-Ride answers. Detour detection (beta): "Temporary stop" labels, skipped stops x-ed out, factored into trip plans. [A]
- **Where real-time comes from** (vendor's own explanation): "Transit agencies use GPS trackers … they send this new arrival time to us and we display it in the app! … we don't actually operate the transit system." If the agency has no real-time, riders are asked to crowdsource via GO. [A]
- **Rate-My-Ride**: anonymized feedback on accessibility, crowding, timeliness; agencies can add custom follow-up questions (safety, driver interactions, cleanliness); leaderboard gamifies GO contributions; ghost mode. [A]
- **Tickets and fares** ("available in select cities only"): Buy ticket → select agency/ticket type → accept ticket rules → sign in to Transit account → payment (Apple Pay/Google Pay/card) → activate now or later; "You will need to be connected to the internet to activate your ticket"; "Show to display the activated pass to the driver"; scan barcode; redeem codes from agencies/organizations into the wallet; **fare capping** ("after purchasing enough single passes that equals a day pass, you will get fare capped and upgraded"); "Tickets bought through Transit cannot be transferred to any other apps". [A]
- **Mode management**: disable transportation options (they drop out of nearby list and trip planner); toggle transit map layer. [A]
- Agency partnership (B2B): 220+ agency partners; "We tailor the app to fit your riders' needs. We fix hyperlocal data issues, add your branding, let riders buy fares, and support your on-demand and bikeshare systems"; agencies "broadcast" detours/network changes/service problems; rider feedback tools (stop cleanliness, safety, passups). Montreal, Austin, Toronto, Santa Monica, Orange County, Connecticut, Miami, Baltimore, Columbus, Chicagoland, Ottawa, Twin Cities, Las Vegas named; TTC and Metro Vancouver team-ups announced 2026. [A]
- Royale: paid premium tier ("free for anyone to use … features you can pay for with Royale"); agencies can gift Royale to riders. [A]

### Umo (Cubic) (Layer A)

- Positioning: "integrated mobility platform … making travel effortless for riders and operations seamless for transit agencies"; "built on Cubic's 50 years of public transit expertise"; cloud platform integrating "all transportation modes—from buses and trains to scooters and bikes". [A]
- Umo App (rider side): "A transit mobility app for riders to plan their end-to-end journeys"; benefits: **Trip Planning** ("plan your trip, pay for fares, and track your transit in a single, easy-to-use app"), **Real-time Notifications** ("arrival times and service alerts"), **Mobile Ticketing and Contactless Payments** ("debit or credit card, QR code, or a reloadable smart card"), **Connect Across Systems** ("one app for all participating transit systems in your region and beyond"). [A]
- Features: integrated trip planning ("best routes across buses, trains and more with step-by-step directions"), real-time notifications ("live transit schedules and instant service alerts"), contactless payments ("buy passes or load value to your account"), personal preferences ("save your favorite routes and stops"). [A]
- Agency side: rapid implementation, **automated fare capping** ("promote ridership and ensure fair pricing"), open API integration, **custom branding / white-label**, mobile ticketing, community engagement ("targeted notifications, in-app surveys, and route-based messaging in their preferred language"), built-in accessibility (VoiceOver/TalkBack, 40 languages). [A]
- Sibling machinery: ScanRide (QR-code fare validation), handheld reader, open payments — the fare-collection stack around the app. [A]

### BVG Fahrinfo (Layer A)

- Positioning: "From finding the best connection to buying your ticket – it's all there"; "We'll show you the fastest route to your desired destination and provide you with the option to directly purchase the corresponding ticket." [A]
- Flow as the vendor documents it: download → register (BVG account or e-mail + SEPA/credit card) → choose stop (favorites supported) → select connection ("choose between different ride services to customize your route"; alarm informs "if anything changes on your planned route"; "live timetable display … view your vehicle position in the route details"; "live navigation … gets you to your destination quickly and without detours"). [A]
- Ticket catalog: 24-hour, single, short-trip, 4-trip, extension, 24-hour small group, WelcomeCard, CityTourCard, bicycle tickets, monthly tickets (tariff zone AB). [A]
- Payment: Apple Pay, Google Pay, SEPA direct debit, PayPal, credit card. [A]
- Accessibility statements for Android/iOS linked. [A]
- BVG also ships **Jelbi** (its MaaS app, separate product) and a **Ticket-App** — the authority operates multiple rider-facing apps with different scopes. [A]

### Transport for NSW (Layer A)

- Official apps page lists: **Opal Travel app** ("manage payments, top up and track your Opal card or contactless payments; plan your journey with options for driving, public transport, walking, and cycling; check real-time departure times and service updates; save favourite trips and locations; receive personalised travel alerts and accessibility notifications; get notified with stop alighting reminders and low balance alerts"), **Trip Planner** ("plan your trips from door to door with real-time updates; check service capacity, track your service, and get alerts about changes"), **Live Traffic** (road domain), plus kids' and driver-aid apps. [A]
- "Transport for NSW endorsed apps": the authority reviews and approves third-party apps — the official/third-party boundary is managed by the authority. [A]

## Cross-product Comparison

| Dimension | Citymapper | Moovit | Transit | Umo | BVG Fahrinfo | TfNSW apps |
|---|---|---|---|---|---|---|
| Journey planning | ✓ (core product) | ✓ (pillar 1) | ✓ (category + planner) | ✓ (benefit 1) | ✓ ("finding the best connection") | ✓ (dedicated Trip Planner app) |
| Network reference (lines/stops/timetables) | ✓ (data factory) | ✓ (lines/stations) | ✓ (nearby lines, schedules) | ✓ (routes) | ✓ (stops/timetables) | ✓ (services) |
| Real-time departures/vehicles | ✓ (live bus locations, traffic) | ✓ (ETA, alerts) | ✓ (waves, states, crowding, detours) | ✓ (arrival times, alerts) | ✓ (live timetable, vehicle position) | ✓ (real-time departures, track service) |
| Riding guidance | ✓ (GO trips, lock-screen) | ✓ (live navigation, get-off alerts, AR) | ✓ (GO: leave/change/get off) | ✓ (step-by-step directions) | ✓ (live navigation) | ✓ (alighting reminders) |
| Service alerts/disruptions | ✓ (geo-fenced, diversions) | ✓ (service alerts, crowd reports) | ✓ (pinned-line alerts, cancelled states) | ✓ (instant service alerts) | ✓ (route-change alarm) | ✓ (service updates, personalised alerts) |
| Tickets/fares in-app | not documented for general app (pay framing in co-branded MaaS app) | ✓ "in select cities" (Mobility Wallet, validate pass) | ✓ "in select cities only" (buy/activate/show, capping) | ✓ (ticketing + contactless + stored value, capping) | ✓ (full fare media catalog) | ✓ (Opal card top-up/management) |
| Account | ✓ (CLUB membership) | ✓ (wallet account) | ✓ (account for tickets; Royale) | ✓ (fare account, account linking) | ✓ (BVG account) | ✓ (Opal account) |
| Favorites/pins | ✓ (calendar sync, best-time) | ✓ (favorite lines/stations/places) | ✓ (pinned lines, favorite locations) | ✓ (favorite routes/stops) | ✓ (favorite stops) | ✓ (favourite trips/locations) |
| Multi-modal beyond transit | ✓ (bike, etc.) | ✓ (bike routes/docks; carpool/on-demand in wallet) | ✓ (bikeshare, scooters, ridehail) | ✓ (scooters/bikes in platform copy) | ✓ ("different ride services") | ✓ (driving/walking/cycling options) |
| Crowdsourcing/feedback | — (not observed) | ✓ (community editing) | ✓ (GO, Rate-My-Ride, leaderboards) | ✓ (in-app surveys — agency-initiated) | — (not observed) | — (not observed) |
| Publisher | independent (Via) | independent | independent (+ agency platform) | fare vendor for agencies | the agency itself | the authority itself |
| White-label/official-app platform | ✓ (Citymapper for Cities, co-branded) | ✓ (branded apps) | ✓ (220+ agency partners, branding) | ✓ (white-label) | n/a (is the official app) | n/a (is the official app; endorses third-party apps) |
| Premium subscription | ✓ (CLUB) | — (not observed) | ✓ (Royale) | — (not observed) | — (not observed) | — (not observed) |

Reading of the table:
- **Journey planning + network reference + rider-facing orientation: 6/6** — the only rows with no gaps. Everything else varies.
- **Real-time: 6/6 in the current market**, but Transit's own documentation shows the app functioning on schedule-only data (greyed-out times, "likely cancelled" inference, GO crowdsourcing to fill gaps) — real-time is a layer over the schedule, not the invariant.
- **Ticketing: 4/6 documented, and the two independent planners gate it explicitly ("in select cities")** — common mature capability, not definitional.
- **Accounts: 6/6** but of different kinds (fare accounts, membership, ticket wallet) — the account is common, its meaning varies; not definitional by itself.

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant

Three jointly-held structures:

1. **Rider-facing orientation** — the user is a passenger using the service, not the operator running it. The app's job is to get a person through their day on transit. Remove → operator-side territory (Public Transit Operations Platform) or a generic map product.
2. **The scheduled transit network as the reference frame** — the app's world is the scheduled public transport service of the network(s) it covers: lines/routes, stops/stations, timetables. Remove → generic navigation (transit as one mode filter) or generic travel planning.
3. **Journey planning as the central act** — the rider states an origin and destination and the app assembles itineraries from the network's scheduled services (times, transfers, modes, commonly fares). The journey is the unit of work. Remove → a stop-departure/arrivals utility (below the Type).

Jointly-held load-bearing tests:
- 1 alone = operator tool or generic map.
- 2 without 3 = "when's my bus" arrivals board (below the Type).
- 3 without 2 = generic multimodal navigator (a maps product with a transit mode).
- 1+2 without 3 = arrivals utility.
- 1+3 without 2 = generic travel/navigation product.
- 2+3 without 1 = the ops platform's planning view (operator-facing).

### L1 — Common Mature Structure

- **Real-time layer over the schedule**: live departures distinguished from scheduled times (with skipped/cancelled/likely-cancelled states), live vehicle positions on the map, crowding where available, automatic and pinned-line service alerts, detour/diversion handling.
- **Riding guidance**: step-by-step navigation of the chosen itinerary; leave-now / change-lines / get-off notifications; live re-timing.
- **Personal layer**: favorite lines/stops/locations, pinned lines with alert subscriptions, recent/saved trips, calendar integration (some products).
- **Fare payment / ticketing**: in-app purchase of agency fares, ticket wallet, activation shortly before boarding, display/scan for inspection, fare capping, stored value / card top-up, contactless payment options. Present in most mature products but explicitly "in select cities" for the independent planners; standard for agency apps.
- **Accessibility support**: screen readers, accessible-route options, accessibility notifications.
- **Multi-modal extension**: bikeshare/scooters/ridehail (and walking/cycling/driving comparisons) as planning options beside the transit network.

### L2 — Variant / Optional Structure

- **Publisher posture**: official agency/authority app vs independent multi-city app vs white-label/co-branded platform powering official apps.
- **Network scope**: single network/region vs multi-city aggregation.
- **Ticketing depth**: none (info-only) → partnership tickets in select cities → full fare media catalog + stored value + contactless account management.
- **Crowdsourcing & feedback machinery**: rider-reported vehicle locations, community data editing, ride ratings/surveys — present in some products, absent in others.
- **Premium subscription** for the consumer app.
- **Form factor**: native app (iOS/Android), web planner, watch/lock-screen companions.
- **Regional fare regimes**: QR validation, reloadable smart cards, account-based capping, card top-up — jurisdiction-dependent.
- **Agency channel depth**: targeted notifications, in-app surveys, route-based messaging (agency-facing side of the same surface).

### L3 — Vendor-specific (Research Notes only)

- Transit: GO leaderboard/ghost mode, battery/data figures (~5% per 20-min trip, <100 kb), "likely cancelled" inference as a named state, Royale gifting by agencies, ticket non-transferability warning, Masabi/Token/VidaPay/VanillaDirect fare integrations named in help articles.
- Moovit: Way Finder AR, Transit Data Manager (GTFS editor), "1.7 billion users / 3,500 cities / 112 countries" marketing claims, Long Distance Tickets nav item, Low Carbon Commute program.
- Citymapper: CLUB membership, AI route-choice beta, "35% more accurate than official sources" claim, London bus pilot 2017, Via acquisition, UChicago partnership.
- Umo: ScanRide QR validation, handheld reader, account linking, 40-language support claim.
- BVG: specific ticket catalog (WelcomeCard, CityTourCard, 4-trip, extension tickets), SEPA/PayPal payment set, separate Jelbi and Ticket apps.
- TfNSW: Opal card mechanics, Live Traffic as a sibling app, endorsed-apps program.

## Rejected Findings (considered, not promoted)

- **"Ticketing is definitional"** — rejected: the independent planners gate it "in select cities"; the info-only generation and schedule-only planners satisfy the Type without it; the MaaS pass's own historical check treats single-agency ticketing as insufficient for MaaS. Fare payment is the strongest common-mature capability, not the invariant.
- **"Real-time is definitional"** — rejected: Transit documents schedule-only operation (greyed-out times) and crowdsourced gap-filling; the historical web-planner generation was schedule-only. The invariant underneath is the schedule-based network reference.
- **"One agency's network only" (inherited from the MaaS pass's seam phrasing)** — refined: the sample's independent planners aggregate many networks informationally while remaining clearly transit passenger apps. The seam vs MaaS is transactional multi-provider integration under one account, not network count. See Boundary Findings 1.
- **"Account is definitional"** — rejected as stated: accounts exist 6/6 but mean different things (fare wallet, membership, ticket account); the info-only and schedule-only generations had none. What the account carries (fares) is L1; the account itself is not load-bearing for the Type.
- **"Crowdsourcing is definitional"** — rejected: 2/6 strong, 1/6 agency-side only, 3/6 absent. Optional.

## Boundary Findings

1. **vs Mobility-as-a-Service Platform — JOINT REVIEW DISCHARGED, keep-both RATIFIED.** The MaaS pass held the seam as "one-network-center vs multi-provider-integration-under-one-account" and held Moovit in-type at the planner-heavy pole. This pass confirms the removal tests from the transit side: (a) remove the multi-provider booking/account layer from a MaaS platform → a transit passenger app (Moovit, Citymapper, and Transit are exactly this at their planner-heavy poles — their ticketing is per-agency and "in select cities", not multi-provider booking); (b) add partner booking under one account to a transit app → it grows into MaaS. Decisive seam evidence: **BVG ships both products side by side** — Fahrinfo (the transit passenger app: network + tickets for BVG's own network) and Jelbi (the MaaS app: multi-provider booking under one account). The same authority operates both sides of the seam as separate products. Refinement of the MaaS pass's phrasing: the transit passenger app centers the *scheduled transit network* (one agency's or several agencies' networks aggregated informationally); MaaS centers *transactional integration of multiple providers under one account*. Informational multi-network aggregation (Citymapper/Moovit/Transit) stays in this Type; transactional multi-provider booking (Whim/Jelbi) is MaaS.
2. **vs Public Transit Operations Platform** — rider-facing consumes vs operator-facing produces. The ops pass's wording is confirmed from this side: the passenger app *consumes* the real-time data (agency GPS → predictions → feed) the ops platform *produces*; Transit's own "where real-time comes from" article documents the consumption end ("they send this new arrival time to us and we display it"; "we don't actually operate the transit system"). Remove the operator side → passenger app; remove the rider side → ops platform. The feed (GTFS-RT-class standards) is the seam.
3. **vs Rail Booking & Ticketing** — long-distance rail commerce (intercity tickets, seat reservations, journey-priced products) vs urban/regional scheduled transit usage (fare media for a network). Adjacent and sometimes brokered inside a transit app (Moovit's "Long Distance Tickets" nav item — label-level evidence only); DB Navigator-class products are the rail-booking Type.
4. **vs Ride-hailing / Micromobility Sharing / Car Sharing** — those operate or supply vehicles on demand; the transit passenger app serves scheduled shared capacity where the passenger never operates the vehicle (micromobility pass's own seam wording, confirmed). Transit apps integrate these modes as planning options (informational or hand-off), but the center stays the network.
5. **vs general mapping/navigation products (no dedicated leaf)** — a general map with a transit mode filter is NOT this Type: its center is places/driving, transit is one option. The center here must be the transit network itself. This resolves the MaaS pass's "pure journey planners have no leaf" observation from this side: a *dedicated* transit journey planner (web or app, plan-only) is the thin pole of THIS Type; general-purpose maps with transit routing are a different (unlisted) product class. Recorded as a taxonomy observation for the owner, not a directory change.
6. **Arrivals-only / stop-departure utilities** — below the Type: they serve a stop, not a journey (no planning leg). Recorded as a boundary observation; no directory change made.
7. **vs Parking Application** — parking appears as a mode/destination detail inside planning (driving comparisons), never the center.
8. **The B2B platform layer** (Moovit Branded Apps, Transit's agency platform, Umo, Via's Citymapper for Cities) — the supply side of the same rider surface: white-labeling, data management, fare back office, agency messaging. The Type is defined by the rider-facing surface; the platform layer is how it reaches agencies, not a different Type.

## Historical / Market-Sample Check

- The Type is digital-native: the paper-era ancestors are the timetable leaflet and the paper ticket (conceptual lineage only — no app-shaped ancestor). The check therefore asks whether the definition over-fits the *current smartphone + real-time + mobile-ticketing* packaging.
- **Schedule-only generation** (web journey planners of the 2000s, planner-first regional portals): satisfy L0 (rider-facing + network + planning) with no real-time and no ticketing. ✔
- **Info-only official apps** (agency apps with planning + arrivals but no in-app fares): satisfy L0; ticketing stays L1. ✔ (Direct fetch of two prominent examples blocked — see Source-access limitations; the pole is evidenced by Transit's documented schedule-only cities and TfNSW's planning-only Trip Planner app.)
- **Arrivals-only utilities** (next-bus clients): fail leg 3 (no journey planning) — held below the Type, consistent with the journey as unit of work. Recorded as a boundary observation.
- **Ticketing-heavy official apps** (BVG Fahrinfo, Umo-powered agency apps): satisfy L0 with ticketing as L1 depth. ✔
- **Multi-network independent planners** (Citymapper/Moovit/Transit): satisfy L0 with network scope as a variant axis. ✔
- The definition does not accidentally swallow MaaS (transactional multi-provider booking fails the network-center test) or the ops platform (operator-facing fails leg 1). ✔

## Uncertainties

1. **MTA and TfL official app pages unreachable (403)** — the info-only official pole is evidenced indirectly; no MTA/TfL-specific claims made.
2. **Citymapper consumer depth** — documented from root, one news post, and Via's B2B page; no help-center articles fetched. Citymapper's consumer ticketing status is unknown from this pass's sources (absence claimed only for fetched pages).
3. **Moovit "Long Distance Tickets"** — navigation label only (page 404); the rail-booking adjacency is recorded at label strength.
4. **Umo rider-loop operational detail** — the "Explore, Pay, Go" page 404'd; Umo evidence rests on two official marketing pages plus the support portal's existence. Ticket activation/validation mechanics for Umo are not documented here.
5. **Whether arrivals-only utilities constitute a distinct market population** worth a leaf — taxonomy-owner question, recorded in Boundary Issues.
6. **Offline ticket activation** — documented for Transit (internet required to activate); other products' offline behavior not researched; held product-specific.
7. **Scale figures** (Moovit's 1.7B users/3,500 cities; Transit's 1,200+ cities; Via's "hundreds of cities") are vendor marketing claims, recorded but not asserted as Type facts.

## Final Synthesis

A Public Transit Passenger App is the rider-facing companion to a scheduled public transport network. Its defining core is three jointly-held structures: **rider-facing orientation** (the passenger using the service, not the operator running it), **the scheduled transit network as the reference frame** (lines/routes, stops, timetables of the network(s) covered), and **journey planning as the central act** (origin→destination itineraries assembled from the network's scheduled services — the journey is the unit of work). Around that core, mature products standardly add the real-time layer over the schedule (live departures with skipped/cancelled states, vehicle positions, disruption alerts, detours), riding guidance (step-by-step navigation, leave/change/get-off notifications), the personal layer (favorites, pinned lines, saved trips), fare payment and ticketing (buy → activate → display/scan, fare capping, accounts — "in select cities" for independent planners, standard for agency apps), accessibility support, and multi-modal extensions (bike/scooter/ridehail as planning options). The market realizes the Type across a publisher spectrum (official agency app, independent multi-city app, white-label platform powering official apps) and a ticketing-depth spectrum (info-only → select-city tickets → full fare media). The boundaries are held against MaaS (transactional multi-provider booking under one account — ratified with the MaaS pass, with BVG's side-by-side Fahrinfo/Jelbi as the decisive seam evidence), against the ops platform (produces vs consumes the real-time feed), against rail booking (long-distance commerce), against on-demand mobility Types (scheduled capacity, passenger never operates the vehicle), and against general maps (transit as mode filter ≠ the center). The definition survives the historical check: schedule-only planners and info-only official apps satisfy the core without any of the modern machinery.
