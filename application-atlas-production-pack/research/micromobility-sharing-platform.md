# Research Notes — Micromobility Sharing Platform

## Research Goal

Understand, from real products, what a Micromobility Sharing Platform is: the shared small-electric-vehicle service (e-scooters, e-bikes) where riders locate, unlock, ride, and release vehicles through an app, and what structures define the Type versus what is era/segment implementation.

Family context: this leaf was pre-flagged from the car-sharing-platform pass (2026-09-07): "free-floating car sharing and micromobility share the same loop (find nearby vehicle in zone → app unlock → one-way trip → end in zone → per-minute billing). Seam: vehicle class (car vs scooter/bike) and the driver-licensing/eligibility gate." This pass researches the micromobility side independently and ratifies or corrects that seam.

## Initial Boundary

- **What it probably is:** an app-mediated shared-fleet service for short urban trips on small electric vehicles (e-scooters, e-bikes), billed per use, with a rider-facing app and an operator-side fleet operation.
- **Nearest neighbors:** Car Sharing Platform (same loop, different vehicle class), Ride-hailing Platform (driver supplied), Vehicle Rental Platform (counter, per-day), Public Transit Passenger App (scheduled shared capacity), Fleet Management System (operator-side administration), Mobility-as-a-Service Platform (aggregator), Parking Application (rules overlap only).
- **Open questions going in:** how dock-based station systems (Citi Bike generation) relate to dockless scooters; whether hub/drop-off models (Donkey Republic) are the same Type; how deep the operator side goes; whether moped sharing is in-type.

## Research Questions

1. What is the unit of record — vehicle, ride/trip, or both? How do they relate?
2. How does a rider find, unlock, ride, and release a vehicle? What are the release rules (dock, hub, pin, zone)?
3. What is the access gate — identity, payment, age, license? How does it differ from car sharing's license gate?
4. How is pricing structured (unlock + per-minute, per-ride, passes, memberships)? What fees attach (city compliance, parking penalties)?
5. What in-ride rules exist (geofenced no-go/low-speed zones, parking rules, helmet guidance)?
6. What happens on failure: can't start, can't end, GPS drift, broken vehicle, overcharge, accident?
7. What does the operator side look like (charging/swapping, rebalancing, maintenance, retrieval)?
8. How do dock-based station systems and hub-based systems fit the same Type?
9. What interfaces exist (rider app map, ride screen, parking confirmation, support)?

## Representative Products

| Product | Why selected | Shape |
|---|---|---|
| **Lime** | global leader; richest Tier-1 help center | dockless scooters + bikes, zones + parking pins |
| **Bird** (with Spin) | US pioneer; Tier-1 help center | dockless scooters + e-bikes |
| **Dott / TIER** | European champion (merged 2024); different market regime | dockless scooters + bikes, in-house ops |
| **Veo** | US city-partner operator; seated scooters | dockless, city-partnership posture |
| **Donkey Republic** | different philosophy: bike-only, hub/drop-off, membership-first | hub-based bike share |
| **Citi Bike** (Lyft) | dock-based station-system variant for the historical/structural check | station docks + keys + kiosks |

## Sources

Fetched 2026-09-09:

- Lime Help Center (Zendesk) — root, Starting your ride, Ending your ride, Riding and parking zones, Ride costs and rates, Age verification — https://help.li.me/hc/en-us (articles fetched individually)
- Bird & Spin Support Center (Zendesk) — root, Getting Started category, Starting/ending your ride and parking your vehicle, Cost to ride — https://help.bird.co/hc/en-us
- Dott official site — root + Ride with us — https://ridedott.com/ , https://ridedott.com/ride-with-us/
- Veo official site — root + Rider Guide (How to Ride) — https://www.veoride.com/ , https://www.veoride.com/rider-guide-how-to-ride/
- Donkey Republic official site — root (How to Rent a Bike, memberships, cities) — https://donkey.bike/
- Citi Bike Help (Zendesk) — root, Taking a ride category, How to start a ride, How to dock a bike — https://help.citibikenyc.com/hc/en-us

Source-access limitations:

- https://www.li.me/ (marketing root) returned 403; Lime evidence rests on its help center (Tier 1) — acceptable.
- Bird "Ride zones" article returned 403 on first fetch; not retried. Zone mechanics documented via Lime (A-layer) + Bird's operational-zone mention in Cost to ride + Dott's zone mentions.
- Dott help center (help.ridedott.com) is JS-rendered; returned empty. Dott evidence is Tier-2 product page only.
- Wikipedia "Bicycle-sharing system" timed out twice; the pre-scooter dockless generation (ofo/Mobike) is kept as low-strength historical context, not asserted in detail.
- No operator-facing product documentation (fleet dashboards, swap-logistics tools) was fetched; operator side is documented structurally only.

## Product Observations

### Lime (evidence layer A unless noted)

From help.li.me:

- **Account**: "download the Lime app and create an account. You'll need to provide a valid phone number or email address and a form of payment." (Starting your ride)
- **Start**: locate vehicle on map → tap **Reserve** to hold it (10 minutes) → **Start ride** (one-tap in select cities) or **Scan to start** via QR code; fallback: enter the plate number if QR unreadable. (Starting your ride)
- **Age verification**: "In some cities, you must verify your age before you can ride" — scan a government-issued ID showing date of birth, or manual entry. City-dependent. (Age verification)
- **Ride zones** (Riding and parking zones): No Go zones (vehicle gradually stops; walk it out), Low Speed zones (vehicle slows; tap to see top speed), No Parking zones (app alerts, redirects to parking), Mandatory Parking zones (blue parking pins; must park there), No Locking zones (for cable-lock vehicles), Service Zone (the rideable area; exiting → vehicle gradually stops, walk back).
- **End**: ride to the parking pin → **End ride** → take a photo of the parked vehicle → park upright, kickstand down, not blocking pathways/entrances/driveways → "You may be subject to a warning or penalty if your vehicle is incorrectly parked." (Ending your ride)
- **End failures**: GPS accuracy (move closer to pin), internet connection, expired/insufficient payment card. (Ending your ride)
- **Pricing** (Ride costs and rates): "a fixed cost to unlock each vehicle and a per-minute rate while the vehicle is unlocked. Rates may vary across different locations and times of day. Ride time is rounded up to the nearest full minute." Passes/subscriptions change terms. Price shown in app before ride or by scanning QR. Price may include city permit fees/surcharges and rider liability insurance for third-party damages. "Your ride continues, and charges will apply, until the app confirms the ride has ended and the vehicle is locked."
- **Other surfaces** (section lists): Pausing your ride; Reserving a Lime vehicle; Using the cable lock; Starting a Group Ride; Using a parking station; parking-penalty charges; stolen-vehicle charge policy; LimePass subscription; Lime Cash; refund policy; accident article; Rules and regulations article.

### Bird (evidence layer A unless noted)

From help.bird.co:

- **Start**: "scan the QR code on the vehicle or manually enter the four- to five-digit code written beneath the QR code. Press 'Unlock.'" Scooter: kick-push to get moving, then throttle. E-bike: pedal to activate e-assist. (Starting/ending your ride and parking your vehicle)
- **End/park**: "review the local parking rules and verify you're in an approved parking location. The vehicle must not obstruct handicapped accessibility or pedestrian or vehicle traffic." Kickstand down. In-app tutorial includes local parking regulations per city. (same article)
- **Safety**: helmets, bike lanes, local traffic laws. (same article)
- **Pricing** (Cost to ride): pricing depends on city and local currency; taxes and compliance fees may apply; compliance fees "help cover city-imposed charges and costs related to keeping our fleet in compliance"; European/Middle-Eastern markets include taxes and fees in the final price; pricing visible in app within the "market and operational zone (shown in blue on the map)".
- **Other surfaces** (category lists): Where to find vehicles; Availability to ride; Reserve a ride; Ride zones (article 403 — title only); Pausing during a ride; Vehicle issue during ride; Where to ride; Riding in weather/rain; Preferred parking zones; How to park your vehicle; cable-lock issue; Can I unlock an additional vehicle for a friend; Which cities does Bird operate in; max speed / range FAQ; Bird+ / Ride Pass subscriptions (cancel article); overcharge/refund article; can't-login article; Community section; Safety section.

### Dott / TIER (evidence layer A for site claims; structure B)

From ridedott.com (Tier-2):

- TIER and Dott "joined forces in 2024"; "available in more than 400 cities across Europe and Middle East."
- Vehicles: "Shared bikes & scooters… custom, sustainable vehicles… brought in for regular maintenance… safety features, like extra bright front and rear lights, up to 50 km range swappable batteries, and large wheels."
- App: "Download the Dott app, sign up, unlock a ride & get rolling right away" — "Just scan & go."
- Pricing: "Explore Dott passes to save per day, week, or month – or earn free rides by referring your friends… See the price that applies in your area in the Dott app. We accept popular payment methods and all the local favorites too."
- Insurance: "complimentary insurance in eligible countries."
- Riding rules: no-go and low-speed zones per city ("Check them on the map or turn on notifications"); "Park in designated parking spots – don't block the sidewalk. Follow local rules to avoid any parking fines."
- Operations: "we do all our operations in-house" (root page, responsible-operations section).

### Veo (evidence layer A for site claims)

From veoride.com (Tier-2):

- How it works: **Search** (nearest ride on in-app map) → **Scan** (QR code on vehicle to unlock) → **Explore** → **Park** ("parked upright in accordance with your city's parking requirements. Follow in-app instructions to properly end your ride").
- Rider guide: find ride on map → scan QR between handlebars → helmet recommended; pre-ride check (throttle engages, brakes squeeze) → kick-start standing scooter or sit on seated scooter → park upright, out of pedestrian walkways; "Parking requirements vary from city to city, so be sure to check the rules on the Veo app before ending your ride."
- Fleet: standing scooters, seated scooters, bikes ("Something for everyone"; full-fleet image).
- VeoPlus: "a monthly subscription that offers discounted rides."
- Footprint: "over 50 cities from Los Angeles to New York City."

### Donkey Republic (evidence layer A for site claims)

From donkey.bike (Tier-2):

- "Rent a bike 24/7… Simply open the app, find a Donkey near you, and unlock it with your phone."
- How to rent: #1 find a bike in the app and choose rental option → #2 unlock with the app, start ride → #3 "End your trip by locking the bike at a Donkey drop-off shown in the app."
- Pricing posture: memberships (student discount up to 25%; "use my membership in all cities"), "just ride" pricing option, no-commitment framing.
- B2B: company memberships for employees; advertising on bike side panels.
- Footprint: "190+ cities"; bike-only fleet (ebikes + classic); Copenhagen-based.

### Citi Bike (dock-based variant; evidence layer A)

From help.citibikenyc.com:

- **Start** (How to start a ride): four paths — (1) app: tap station on map, scan bike QR, green light + "ding," lift from dock; (2) **bike key**: insert key into slot on the dock next to an available bike ("make sure you're at an online station"); (3) **kiosk**: insert credit/debit card, receive a 5-digit ride code, enter on dock keypad ("Each ride code is good for one single use"); (4) **Lyft app**: linked accounts, "Unlock a bike" purchase, scan QR or manually enter chainstay/bike number.
- **End** (How to dock a bike): "return your classic bike or ebike to any station with an open dock – you don't have to bring it back to the station where you picked it up." Line up the front triangle with the dock, insert, hold ~5 seconds; dock light green = "properly locked"; registration can lag minutes. "Please always make sure your bike is docked at a Citi Bike station when your ride is over; never leave it unattended."
- **Overflow parking** (ebikes): when docks full, park next to station, kickstand down, tap **End Ride**, take a photo of the ebike parked with the station in background; ebike locks until next rider.
- **Time rules** (section titles): "How long can I keep a bike out?", "What if I keep a bike out too long?" — time limits and over-time consequences exist (titles only; bodies not fetched).
- Receipts reviewable; station map at citibikenyc.com/explore; service-updates page for station status.

## Cross-product Comparison

| Dimension | Lime | Bird | Dott/TIER | Veo | Donkey Republic | Citi Bike |
|---|---|---|---|---|---|---|
| Fleet | scooters + e-bikes | scooters + e-bikes | bikes + scooters | standing + seated scooters, bikes | bikes (classic + e) | classic bikes + ebikes |
| Discovery | in-app map | in-app map | in-app map | in-app map | in-app map | station map (app + web) |
| Unlock | QR scan; plate-number fallback; one-tap start after reserve | QR scan or 4–5 digit manual code | "scan & go" | QR scan | unlock with phone (app) | QR scan / bike key / kiosk ride code / Lyft app |
| Reservation | Reserve holds vehicle (10 min) | Reserve a ride (article) | — | — | choose rental option in app | — (dock inventory is the "reservation") |
| Release | parking pin + end-ride photo; zones govern | approved parking location; kickstand; local rules | designated parking spots; fines | upright, per-city rules, in-app instructions | lock at Donkey drop-off shown in app | dock into any station (green light) or ebike overflow + photo |
| Geofencing | No Go / Low Speed / No Parking / Mandatory Parking / No Locking / Service zones | operational zone (blue) on map; Ride zones section exists | no-go and low-speed zones per city | per-city parking requirements | drop-off network | station network; overflow rules |
| Pricing | unlock + per-minute, rounded up; city fees/surcharges; insurance in price; passes | city-dependent; compliance fees; taxes included in EU/ME | per-area price in app; day/week/month passes; referrals | per-ride; VeoPlus monthly subscription | memberships (multi-city, student, company) + "just ride" | single ride / passes (membership); receipts |
| Eligibility | account (phone/email + payment); age verification in some cities (gov ID) | account; app tutorial | sign up | app download | app account | account / key / card at kiosk |
| Insurance | rider liability included in price (some locations) | — (not observed) | complimentary in eligible countries | — | — | — (not observed) |
| Pause a ride | yes (article) | yes (article) | — | — | — | — (dock = pause) |
| Group/friend | Group Ride article | unlock additional vehicle for friend | — | — | — | Riding with a Group article |
| Operator side | local teams retrieve broken vehicles; parking-station hardware | fleet compliance operations (fee framing) | in-house operations; swappable batteries; regular maintenance | city-partnership posture | drop-off network ops | station/dock network ops; service updates |
| Support | trouble starting/ending, overcharge, refund, accident, stolen-vehicle | trouble starting/ending, overcharge, cable lock, login | help center (JS-gated) | rider guide, safety 101 | help center | service updates, receipts |

## Canonical Model

### L0 — Defining Invariant

Four jointly-held structures. Remove any one and the product stops being a micromobility sharing platform:

1. **The shared micromobility fleet as the unit of supply.** A pool of small electric vehicles (e-scooters, e-bikes; seated scooters observed) owned and operated by the service, circulating among many riders in short successive turns. No rider owns the vehicle they ride. Remove → personal ownership or long-term rental.
2. **The rider account as the access gate.** A registered account binding identity and payment (age verification where regulation requires it); the gate is deliberately lighter than car sharing's license gate. Remove → anonymous public infrastructure, no user model, no billing.
3. **The self-service locate-unlock-ride loop.** The rider finds an available vehicle (map), unlocks it themselves (QR scan / code / phone / key), and operates it personally for one trip. No staffed handover, no driver supplied. Remove → staffed rental counter or guided-tour territory.
4. **The release-and-close act.** The rider ends the trip at a defined place and state (dock, hub/drop-off, parking pin, approved location) so the vehicle becomes available to the next rider, and the trip closes with usage-based charging (per-minute, per-ride, or plan-included). Remove → abandonment (fleet depletes); remove the per-trip commercial record → free public bike rack.

Jointly-held load-bearing checks:

- 1 alone = a vehicle catalog / inventory listing
- 2 without 1 = a payment account with nothing to ride
- 3 without 1+2 = borrowing a friend's bike
- 4 without 3 = drop boxes with no self-service access
- 1+2+3 without 4 = one-way abandonment; the fleet depletes and the service collapses
- 1+3 without 2 = unregistered open access (free-at-point-of-use city systems are the edge case; the platform software still registers riders — recorded as uncertainty)

### L1 — Common Mature Structure

- **Map as the primary discovery surface** — vehicle positions, battery/availability state, zones, parking pins/stations (all six products).
- **Ride reservation / hold** — Lime (10-minute hold), Bird (Reserve a ride); dock systems achieve the same via station inventory.
- **Geofenced ride zones** — no-go (vehicle stops), low-speed (vehicle slows), no-parking, mandatory-parking, service-zone boundary (Lime A-layer; Bird operational zone + zones section; Dott no-go/low-speed).
- **Parking confirmation** — end-ride photo (Lime, Citi Bike ebike overflow), pin proximity check (Lime), approved-location rules (Bird, Veo, Dott), dock green-light confirmation (Citi Bike).
- **Unlock + time-based pricing** with per-minute rounding (Lime explicit; Bird/Dott/Veo per-ride city pricing consistent with the pattern); city compliance fees/surcharges itemized (Lime, Bird).
- **Passes / subscriptions / memberships** — LimePass, Bird Ride Pass/Bird+, Dott day/week/month passes, VeoPlus, Donkey memberships, Citi Bike passes.
- **Insurance included** in eligible markets (Lime, Dott).
- **In-ride controls** — pause a ride (Lime, Bird), cable lock handling (Lime, Bird), vehicle-issue reporting during ride (Bird article; Lime "try another nearby vehicle… team… on their way to retrieve").
- **Safety layer** — helmet guidance (Bird, Veo, Dott), in-app tutorials with local rules (Bird), riding rules (Dott), rules-and-regulations article (Lime).
- **Group riding** — group ride (Lime), unlock for a friend (Bird), riding with a group (Citi Bike).
- **Support & money machinery** — trouble starting/ending, overcharge/refund, accident reporting, receipts/trip history (all).
- **Operator side** — fleet operations behind the rider surface: charging/battery swap (Dott swappable batteries), rebalancing, maintenance (Dott "brought in for regular maintenance"), retrieval of broken/mis-parked vehicles (Lime), station/dock network ops (Citi Bike service updates). In-house or contracted; productized to different depths.

### L2 — Variant / Optional Structure

- **Access geography**: dockless free-floating (Lime/Bird/Dott/Veo) vs dock-based station systems (Citi Bike) vs hub/drop-off network (Donkey Republic) vs hybrid (Lime parking stations; Citi Bike ebike overflow).
- **Access credential**: QR scan (all), manual code fallback (Lime plate number, Bird 4–5 digit code, Citi Bike chainstay number), phone-as-key (Donkey), physical bike key (Citi Bike), kiosk ride code (Citi Bike), transit/linked-app unlock (Lyft app).
- **Vehicle mix**: standing scooters, seated scooters (Veo), e-bikes, classic pedal bikes (Donkey, Citi Bike); moped-class vehicles at the edge (not in sample — uncertainty).
- **Pricing posture**: pure pay-per-ride, prepaid passes, monthly subscriptions, memberships (individual/student/company), plan-included rides.
- **Eligibility depth**: age verification city-dependent (Lime gov-ID scan); license requirements for faster/heavier vehicle classes unverified in-sample.
- **Regulatory posture**: city permits and per-city operating rules, compliance fees, insurance regimes, parking-fine regimes — all city-shaped.
- **B2B / institutional**: company memberships (Donkey), university/city programs (fee framing at Lime/Bird).
- **Integration surfaces**: ride-hailing super-app distribution (Citi Bike inside Lyft app); transit adjacency (Donkey blog content; MaaS aggregators out of scope).
- **Seasonality**: availability varies by season/weather (Bird FAQ titles).

### L3 — Vendor-specific (research notes only)

- **Lime**: 10-minute reserve hold; plate-number fallback; zone color scheme (red/yellow/blue/green shading); parking-penalty charge article; "Do I pay if the vehicle is stolen?" article; LimePass; Lime Cash; parking-station hardware article.
- **Bird**: 4–5 digit code beneath QR; mandatory kick-push/pedal start before motor engagement; Bird+ / Ride Pass; Retail Vehicle program; community forum topics; "Can I ride all year?" seasonality.
- **Dott/TIER**: 2024 merger ("European Champion of micromobility"); 400+ cities claim; "up to 50 km range swappable batteries" (vendor claim); in-house operations doctrine; day/week/month pass naming; referral free-rides.
- **Veo**: seated-scooter class; pre-ride throttle/brake check ritual; VeoPlus monthly subscription; 50+ cities claim; city-partnership positioning.
- **Donkey Republic**: drop-off network model; multi-city single membership; student discount; company memberships; bike-side-panel advertising business; 190+ cities claim; Copenhagen origin.
- **Citi Bike**: 5-digit single-use kiosk ride code; triangle-alignment dock insertion with ~5-second hold; dock green-light confirmation; ebike overflow parking with photo; Lyft-app linked accounts; $4.99 single-ride figure (vendor-specific, not generalized); Jersey City/Hoboken overflow pins.

## Vendor-specific Findings

- The operator side is real but unevenly productized in public docs: Dott makes in-house operations a brand pillar; Lime exposes it only through rider-facing traces ("our local team… on their way to retrieve the vehicle"); Citi Bike exposes it as station service updates. No sampled vendor publishes operator-tool documentation at the rider help center — the operator surface is a separate product layer this pass could not document in depth.
- Regulatory compliance is a first-class cost line, not an afterthought: Lime itemizes city permit fees/surcharges in the ride price; Bird names "compliance fees" for "keeping our fleet in compliance with local regulations"; Dott warns of parking fines. The city is effectively a third party in every ride.
- The same Type spans three release geographies (dock, hub, free-floating) — the market converged on the loop, not on the infrastructure.
- Insurance posture is market-shaped: included in price (Lime some locations), complimentary in eligible countries (Dott), not surfaced (Bird/Veo/Donkey pages fetched).

## Boundary Findings

1. **vs Car Sharing Platform (ratified from this side).** Same find-unlock-ride-release loop and per-use billing. Seam: (a) vehicle class — small electric two-wheelers vs cars; (b) eligibility gate — micromobility gates on account + payment + (city-dependent) age, with no driver's license for scooters/bikes, while car sharing verifies driving licenses; (c) trip scale — minutes-long urban one-way trips vs hours/days. Both leaves stand. The car-sharing pass's seam note is confirmed.
2. **vs Ride-hailing Platform (clean).** Ride-hailing supplies a driver; the rider is a passenger. Micromobility supplies a vehicle; the rider is the operator. No overlap in the core loop.
3. **vs Vehicle Rental Platform.** Rental: staffed counter handover, per-day pricing, multi-day durations. Micromobility: self-service unlock, per-minute/per-ride pricing, short turns. Donkey Republic's day/week rental options straddle the pricing vocabulary but remain self-service app-unlocked with a drop-off network — still in-type. The seam is access mode + fleet circulation, not duration alone.
4. **vs Public Transit Passenger App.** Transit = scheduled shared capacity operated by an authority; the passenger never operates the vehicle. Micromobility = self-operated vehicle on demand. Adjacent in the urban-trip journey, different object of work.
5. **vs Fleet Management System.** Fleet management is operator-side administration of vehicles (maintenance, telematics, compliance). Micromobility sharing's defining surface is rider-facing access; its operator side is supporting structure (same relationship as car sharing's).
6. **vs Parking Application / Parking Management.** Parking rules and pins live inside the ride loop, but finding/paying for parking is not the platform's purpose.
7. **vs Mobility-as-a-Service Platform.** MaaS aggregates multiple mobility services (transit, share, rental) into one planning/booking surface; a micromobility sharing platform operates its own fleet as the thing being consumed. MaaS may distribute micromobility (Lyft-app pattern is a light version of this).
8. **vs Bike-sharing public infrastructure (edge).** Free-at-point-of-use city systems without accounts would fail L0 leg 2; every sampled product registers riders. Recorded as an edge, not a Type split.

## Historical / Market-Sample Check

Would older, regional, platform-native products still fit the L0?

- **Dock-based station systems (Citi Bike, directly observed; the Vélib'/Hangzhou-generation smartcard-dock systems as conceptual lineage, low strength — not fetched):** shared fleet, registered member (key/card/account), self-service unlock at a dock, ride, return to any station dock (one-way), per-trip billing with time limits. Fits all four L0 legs — docks are release geography, not structure.
- **Dockless bike-share generation (ofo/Mobike era, mid-2010s; not directly fetched — Wikipedia timed out; kept as low-strength context):** app-unlock dockless bikes, per-ride billing, zone rules. Fits the same loop the scooter wave inherited. No precise claims made about these products.
- **Hub/drop-off model (Donkey Republic, observed):** fits — the drop-off network is the release geography.
- **Pre-smartphone bike share (conceptual lineage, low strength):** coin/SmartCard-dock systems satisfy the loop with card-at-dock unlock and dock release; the L0 requires no smartphone, no GPS, no geofencing.

The L0 deliberately excludes: smartphone apps, GPS/geofencing, QR codes, swappable batteries, per-minute rounding, city compliance fees, parking photos, subscriptions, seated scooters, dockless operation. All are era/segment/regime implementations.

## Uncertainties

- **Moped-class sharing** (seated, license-requiring vehicles, e.g. the moped-sharing segment) was not sampled; whether license-gated vehicles belong in-type is unverified. Kept out of the defining core; noted as an edge.
- **Operator-side tooling depth** (fleet dashboards, battery-swap logistics, rebalancing apps) documented only structurally; no operator product docs fetched. Claims kept structural.
- **Bird ride-zones mechanics** rest on Lime's A-layer article + Bird's operational-zone mention; Bird's own zones article was 403.
- **Dott help center** JS-gated; Dott evidence is Tier-2 product page only — its rider-loop details (reserve, pause, photo confirmation) are inferred as cross-product commonality (B-layer), not Dott-specific observations.
- **Free-at-point-of-use city systems**: whether a no-billing variant still satisfies "per-trip commercial record" is unresolved; all sampled products bill or gate via plans.
- **License requirements for faster vehicle classes** (e.g., seated scooters above speed thresholds in some markets): not researched; not asserted.
- No market-size, fleet-size, or pricing-level claims are made beyond what sampled pages state about themselves.

## Final Synthesis

A Micromobility Sharing Platform is a rider-facing mobility application built around a shared fleet of small electric vehicles that circulates among many riders in short successive turns. Its defining loop: a registered rider (account + payment, age-verified where regulation requires) finds an available vehicle on the map, unlocks it self-service (scan/code/phone/key), rides it personally through a geofenced city service area, and releases it at a defined place and state (dock, hub, parking pin, approved location) — closing the trip with usage-based charging and returning the vehicle to the pool. Around this loop, mature products add: zone machinery (no-go/low-speed/no-parking/mandatory-parking), parking confirmation (photos, pins, dock lights), unlock+time pricing with city compliance fees, passes/memberships, included insurance in eligible markets, pause/reserve/group-ride controls, safety guidance, support and refund machinery, and an operator side (charging/swapping, rebalancing, maintenance, retrieval). The Type's variants are structural: release geography (dockless / dock-based / hub), credential (scan / code / phone / key / kiosk), vehicle mix, and pricing posture. The ratified seam with Car Sharing is vehicle class + eligibility gate + trip scale; the clean separations are with Ride-hailing (driver supplied) and Transit (scheduled capacity, passenger never operates the vehicle).
