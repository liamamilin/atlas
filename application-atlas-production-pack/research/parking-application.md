# Research Notes — Parking Application

Slug: parking-application
Research date: 2026-09-10
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what a driver-side Parking Application is as an Application Type: its core objects (driver account/vehicle identity, parking places, sessions/bookings, payment), its defining workflows (find/identify a place, start a paid session or reserve, extend/stop, pay), who uses it, which interfaces it presents, which rules and states matter, and where its boundary lies against neighboring Types — above all the §18 sibling Parking Management Platform (processed 2026-09-09, which hung a coordination note for this pass), plus EV Charging Network Management, navigation/map surfaces, and workplace/space management (employee parking allocation).

## Initial Boundary

Initial hypothesis (pre-research):

- Core use: a driver uses a mobile app (or web/phone channel) to find parking, start/stop/extend a paid parking session, reserve spaces in advance, and pay — without feeding a meter or taking a ticket.
- Users: drivers/parkers (consumer primary; business/fleet drivers secondary).
- Nearest neighbors: Parking Management Platform (operator-side sibling), EV Charging apps, navigation/map apps, transit apps, workplace parking allocation.
- Unknowns: is map-based discovery definitional? Is a persistent account definitional? Is reservation/pre-booking definitional or a variant? Where exactly is the seam with the operator platform? Does a fee-free workplace parking allocation app exist as a standalone population?

## Research Questions

1. What objects make up the driver's parking world (place/zone/facility/space, vehicle, session, booking, payment)?
2. How does the driver identify the place — signage zone number, map selection, search?
3. What is the session lifecycle (start, extend, stop early, expiry, reminders)?
4. What can and cannot be changed during an active session?
5. How does payment work (prepaid, post-paid, guest checkout, saved cards)?
6. How does the driver's action reach the operator/enforcement side?
7. Are reservations/pre-booking part of the core or a variant?
8. What varies by operator/zone vs what is fixed by the app?
9. Where is the boundary vs the operator platform, vs EV charging, vs navigation?

## Representative Products

Selected for market representation, documentation quality, and philosophical/geographic spread:

1. **PayByPhone** (North America, UK, Europe) — pay-by-phone session app; documents app + web + phone/IVR channels (the IVR channel is a built-in historical check)
2. **Passport Parking** (US municipal) — zone-number session app with a rich public help center (Tier-1 operational evidence)
3. **Parkster** (Sweden, Germany, Austria) — Nordic map-first pay-by-phone app; account packages incl. a no-account Express mode; EV charging and resident permits in the same app
4. **Parkopedia** (global) — discovery/data + reservations pole; explicitly does not manage any car parks
5. **HONK** (North America) — operator platform with a driver app channel (operator-native app pole)

Attempted and unreachable (403/transport errors, 1–2 attempts each, then abandoned per network rules): ParkMobile, EasyPark, RingGo, SpotHero, JustPark, ParkWhiz, BestParking, parking.com, APCOA driver app pages. The pure reservation-marketplace pole (SpotHero/JustPark class) is therefore documented only through Parkopedia's reservations FAQ; no numeric claims are made about that pole.

## Sources

- PayByPhone — https://www.paybyphone.com/ (root) ; https://www.paybyphone.com/drivers/how-it-works (Tier-1 operational: app, web, phone flows)
- Passport Parking — https://www.passportparking.com/ (driver site, How It Works) ; https://helpcenter.passportinc.com/en (Help Center; General collection and articles: pay flow, zone number, enforcement visibility, active-session actions, zone rules)
- Parkster — https://www.parkster.com/se/sv/ (root; Så fungerar det / how-it-works; offer packages)
- Parkopedia — https://www.parkopedia.com/ (root) ; https://www.parkopedia.com/faq/ (Tier-1 FAQ: service definition, reservations mechanics)
- HONK — https://www.honkmobile.com/ (root) ; https://www.honkmobile.com/drivers/ (driver page)

## Product Observations

### PayByPhone (evidence layer A)

- Positioning: cashless parking payment for drivers; "available in more than 1,000 cities throughout North America, UK & Europe" (root); universities included.
- Three documented channels for the same transaction (how-it-works, Tier-1):
  - **App**: download → enter the location number found on parking signage → enter duration → check details → confirm → extend session in-app "from wherever you are without having to rush back to your car".
  - **Website**: log in / create account → Park menu → location number from signage + duration → card security code → manage vehicles/payment in account page.
  - **Phone (automated line)**: call the number displayed on meters/signage → prompts for the location number and duration → confirmation that parking has started → call again to extend or start a new session; new users guided through registration by phone.
- Registration: "less than 30 seconds"; connect credit/debit card; Google Pay/Apple Pay where available.
- Business/fleet registration is a separate offering (fleets page).
- Observation: the phone channel proves the core transaction needs no app, no map, no smartphone — only a place identifier, a duration, and a payment account.

### Passport Parking (evidence layer A)

- Driver site how-it-works: download → create/register/verify account → find the unique zone number on Passport signs and decals → enter session information & choose payment method → receive alerts and email receipts → add time from phone.
- Help center (Tier-1, dated 2026-02):
  - Pay flow: app or web (park.passportparking.com); enter zone number from nearby signage or meters; enter vehicle license plate; choose duration; review; confirm and submit payment; "you'll see an active session with a clear end time"; extensions "if extensions are allowed in your location".
  - Enforcement visibility: "Once you start a session, your parking information is instantly sent to parking enforcement. Officers confirm payment by checking your license plate and zone digitally using handheld devices. There's nothing you need to display on your dashboard or at the meter."
  - Zone rules vary by location: whether you can extend or stop early, whether validations are accepted, which payment methods are available, rates and convenience fees, time limits and enforcement rules. "Passport Parking provides the technology to pay for parking, but local parking rules always apply."
  - Active session: view session ID, zone, vehicle or space, start/end time, payment method; extend (if allowed); stop early (if supported); add a validation code before the session ends; set up automatic receipts; email a one-time receipt. Cannot change vehicle, space number, zone, or payment method mid-session.
  - Guest Checkout: pay without an account; extensions possible for guest sessions; receipts/confirmation provided.
  - Other documented surfaces: multiple cars per account; parking history and receipts; map behavior; "maximum time reached"; "why can't I start parking in this zone right now" (time-of-day rules); quote expiry during checkout; what happens if the app is deleted; location-tracking privacy question.

### Parkster (evidence layer A)

- Nordic/German pay-by-phone app. How-it-works: open the app and find parking on the map ("we are often present even where no sign is visible") → choose duration and payment method, add vehicle, start parking → stop or extend in the mobile; "you only pay for the time you are actually parked."
- EV charging paid in the same app ("park and charge in the same app").
- Resident permits (boendetillstånd): apply for a residence permit and park where you live.
- Business mode keeps private and work-related parking separate.
- Family account collects the household's parking on one account.
- Account packages: Express (no login, pay per transaction via Swish/card/Apple Pay, fee per transaction), Komplett (all value-added services), Neutral (bare minimum, pay afterwards monthly). Overpayment protection listed across packages.
- Coverage framed as cities/towns across Sweden plus Germany/Austria.

### Parkopedia (evidence layer A)

- Self-definition (FAQ): "a service that allows drivers to find the closest parking to their destination, tells them how much it will cost and whether the space is available. Parkopedia also allows drivers to pay for parking online, through a mobile app and in-car."
- Data layer: detailed information on parking spaces globally (address/entrance-exit coordinates, area shape, opening hours, full price list, total spaces, operator contact details, security info, payment methods accepted, height restrictions, EV charging); real-time availability in a subset of cities. Explicitly: "Parkopedia does not manage any car parks."
- Reservations FAQ (Tier-1): booking guarantees a space for the booking duration; a parking pass is emailed and presented at the facility (e-pass on phone or printed, provider-dependent); cancellation policies vary per location; no amendments — cancel and rebook; no in/out privileges unless expressly indicated; arriving early → charged by the operator's tariff until the reservation starts; overstaying past the booked exit time and grace period → some locations auto-charge the overstay at the provider's tariff; vehicle license plate required because "parking operators require it to identify the cars which have reserved a space."
- Private parking: spaces provided by individuals renting out garages/driveways.
- Observation: the discovery/data layer alone (no transaction) is explicitly a data-licensing service; the driver-facing product adds reservations and payment on top.

### HONK (evidence layer A/B)

- Operator platform first (Daily Parking Manager, Permit Manager, Validation Manager, Reservation Manager, Control Center); driver app as the connected channel: "Effortlessly pay and manage your spots"; account login gives "parking history, manage payments and navigate parking"; "Skip the meter and manage your parking right from your phone. Pay with a digital wallet or credit card"; web pay surface (parking.honkmobile.com/parking).
- Driver sessions/permits created in the app are records inside the operator products (Daily/Permit/Reservation managers); the driver app integrates with enforcement (T2 VMC, Passport, Genetec, gtechna) and PARCS (Flash, TIBA, Amano, Parkonect, T2) stacks.
- Observation: the operator-native pole — one vendor ships both the operator system and the driver window; the two remain structurally distinct surfaces.

## Cross-product Comparison

| Dimension | PayByPhone | Passport Parking | Parkster | Parkopedia | HONK (driver side) |
|---|---|---|---|---|---|
| Primary posture | session pay-by-phone | session pay-by-phone | session pay-by-phone | discovery + reservations + payment channel | operator-native driver channel |
| Place identification | location number from signage | zone number from signage/decals | map-first (plus signage) | map/search over a global database | operator's locations |
| Unit of action | paid session (start/extend) | paid session (start/extend/stop early where allowed) | paid session (start/stop/extend) | booking with parking pass; payment channel | session/permit inside operator products |
| Account | registered account; phone-channel registration | account or Guest Checkout | account packages incl. no-account Express | sign-in for reservations; anonymous browse | driver account |
| Payment | card/wallets; web security code | payment method per session; validations | Swish/card/Apple Pay; post-paid package | payment for reservations/online pay | digital wallet or card |
| Money path direction | driver pays | driver pays | driver pays (prepaid or monthly) | driver pays | driver pays |
| Enforcement linkage | implicit (operator program) | explicit: plate+zone sent to enforcement, nothing displayed | implicit | plate required for reservations | integrates enforcement stacks |
| Extend/stop | extend documented | extend/stop early zone-dependent | stop and extend both first-class | no amendments (cancel+rebook) | via operator rules |
| EV charging | not observed on fetched pages | not observed on fetched pages | in the same app | listed as data attribute | not observed |

Cross-product commonalities (layer B): every product's action binds to a specific operator-defined place; every product carries a driver-side money path for the parking right; the session (or booking) is the unit of action; vehicle identity (plate) is required; rules (extend/stop/rates/max time) are set by the place's operator, not the app vendor.

## Canonical Model (four-level abstraction)

### L0 — Defining Invariant (driver's seat)

Four jointly-held structures:

1. **Driver-side transactional posture** — the user acts as the driver/parker for their own vehicle, presenting vehicle identity (plate) and a payment instrument. Persistent account is the common form; guest/one-off checkout is a documented variant (Passport Guest Checkout, Parkster Express). Remove → operator back office or anonymous meter hardware.
2. **Operator-defined parking places as the object of service** — every action binds to a specific place managed by someone else (a zone number on signage, a facility, a listed space). The app is a window onto operators' parking; it never owns the inventory. Remove → generic payments app or navigation.
3. **The bounded parking right as the unit of action** — the driver starts, extends, stops, or reserves a bounded right to park (a session at a zone/facility, or an advance booking). At least one realization required; session and reservation are both in-type realizations. Remove → parking information app or a timer.
4. **The driver's payment executed through the app** — the app charges the driver for the parking right (prepaid session, booking prepayment, or post-paid billing). Remove → free finder/directory.

Jointly-held load-bearing: 1 alone = payment wallet; 2 alone = parking directory/data service; 3 without 2+4 = parking timer; 4 without 2+3 = generic payment tool; 2+3 without 1+4 = anonymous browsing of bookable places; 1+2 without 3+4 = account with a coverage map and nothing to transact.

### L1 — Common Mature Structure

- Map-based discovery with search/filter (absent in signage-number flows — not invariant)
- Live availability / rate information feeds
- Session reminders/alerts before expiry; remote extend (zone-permitting); stop early (where supported)
- Receipts (automatic email, one-time) and parking history
- Multiple vehicles per driver; saved payment methods
- Zone-rule visibility (rates, max time, free periods, upcoming rate changes)
- Nothing-to-display enforcement linkage (plate+zone checked digitally)

### L2 — Variant / Optional

- Discovery surface: signage zone number vs map-first vs search
- Posture: session-first vs reservation-first vs hybrid
- Identity: persistent account vs guest/express one-off; family accounts
- Payment timing: prepaid vs post-paid monthly
- Scope: multi-operator city networks vs single-operator (airport/garage brand) apps
- EV charging bundled in the same app
- Resident/business permit purchase and renewal via the app
- Fleet/business mode separating work parking
- Citation lookup/payment; validation codes
- Business model: per-transaction convenience fees, package tiers
- Channel breadth: app + web + phone/IVR

### L3 — Vendor-specific (research notes only)

- Parkster package names/pricing (Express 5 kr/transaction, Komplett, Neutral), overpayment protection, Swish support
- Passport session mechanics: session ID, quote expiry at checkout, "maximum time reached", app-deletion behavior
- PayByPhone IVR details (4–5 digit location numbers, card security code on web)
- Parkopedia coverage figures (90M spaces, 20k+ cities, real-time in 4k+ cities)
- HONK module names and integration partner lists

## Historical / Market-Sample Check

- PayByPhone documents a **phone/IVR channel** as a current, first-class channel: call the number on the signage, enter location code + duration, receive confirmation, call again to extend. This satisfies the entire L0 without an app, a map, or a smartphone — so none of those belong in the definition.
- Nordic SMS-parking services (the pre-smartphone generation of the same service) satisfy the core identically: place code + duration via SMS, extend by another SMS.
- Coin-feeding a meter is operator hardware, not a driver-side application — outside the Type, confirming that the driver-side transactional posture (leg 1+4) is what distinguishes the Type from merely parking somewhere.
- Map-first discovery (Parkster) and signage-number entry (PayByPhone/Passport) coexist in the current market → discovery surface is a variant axis, not the core.
- Conclusion: the definition holds across phone-era, SMS-era, and app-era realizations. Historical check passed.

## Vendor-specific Findings

See L3 above. Also: Passport's validation-code attachment to active sessions and its explicit "cannot change vehicle/zone/payment mid-session" rule are product documentation of a general pattern (session immutability) but the exact rule set is vendor-specific; Parkopedia's no-amendment/cancel-rebook reservation rule is provider-dependent per its own FAQ.

## Boundary Findings

- **vs Parking Management Platform (§18 sibling)** — the decisive seam, RATIFIED keep-both from this side (discharges the coordination note hung by the parking-management-platform pass 2026-09-09): the platform is the operator's system of record (inventory of record + stay/permission records + revenue-control loop); the Parking Application is the driver's window (find/identify, start/extend/stop, pay). The two interlock: driver-app sessions and permits are records inside operator platforms (HONK, Passport, PayByPhone all operate both sides as separate surfaces). Remove the operator's inventory + revenue loop → only the driver app remains; remove the driver's transactional posture → only the operator platform remains.
- **vs EV Charging Network Management** — unit of record is the energy-delivery session (per kWh/time) vs the parking stay; Parkster bundles charging into the same driver app — bundling, not identity.
- **vs Navigation / map applications** (adjacent consumer surface, not a §18 leaf) — directions and routing vs the parking transaction; map surfaces in parking apps serve place identification and payment, not navigation.
- **vs Space Management / Workplace Management** — employee parking allocation for one's own workforce lives inside workplace suites as one resource class among desks/rooms, without a vehicle-stay revenue loop; the Parking Application is vehicle-centric across public operators with a driver money path. The fee-free workplace-allocation pole was not sampled as a standalone driver-app population (see Uncertainties).
- **vs Ride-hailing / transit passenger apps** — moving people vs storing vehicles.
- **Discovery-only data services** (Parkopedia's data licensing) sit below the Type: a capability the driver product may consume, not the transactional window itself.

## Uncertainties

- The pure reservation-marketplace pole (SpotHero/JustPark/ParkWhiz class) could not be fetched (403 ×2 each); reservation mechanics are documented via Parkopedia's reservations FAQ only. No numeric claims made about that pole.
- Fee-free workplace parking allocation via a standalone driver app (the sibling pass's secondary uncertainty) was not sampled; boundary held via the vehicle-centric + operator-money legs, flagged for any future workplace-parking pass.
- Gateless drive-in/drive-out driver-side enrollment (plate-linked auto-payment) is known from the sibling platform's research (Flash Express Pay) but was not directly observed on driver-app documentation in this pass; treated as a variant realization of the payment leg.
- Precise numeric rules (grace periods, max session lengths, fee schedules) are operator-configured and vendor-specific; none asserted.

## Final Synthesis

The Parking Application is the driver's transactional window onto other parties' parking: the driver, acting for their own vehicle with a payment instrument, transacts a bounded parking right — start/extend/stop a paid session or reserve a bounded right — against a specific place defined and ruled by a parking operator, paying through the app. Map discovery, live availability, reminders, receipts, accounts, reservations, EV charging, and citation payment are the mature market's standard or optional layers; the phone-call and SMS-era forms satisfy the same core without any of them. The Type is the driver-side sibling of the Parking Management Platform: the platform holds the inventory and the revenue loop; the app is where the driver meets it.
