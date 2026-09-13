# Research Notes — Attraction Management System

Research date: 2026-09-06
Slug: `attraction-management-system`
Directory position: Section 26 Travel, Hospitality, Food Service & Events (siblings: Attraction Ticketing, Theme Park Management, Family Entertainment Center Management, Zoo / Aquarium Visitor Operations, Museum Visitor Experience Platform, Cashless Venue Platform, Digital Waiver Management)

---

## Research Goal

Understand what an Attraction Management System actually is as an Application Type: the operator-side software that runs a visitor attraction's admission business. Determine its defining core, its standard mature capabilities, its segment variants, and its boundaries against neighboring Types (Attraction Ticketing, Event Ticketing, Tour Operator Management, Theme Park Management, Museum Visitor Experience, Cashless Venue Platform, Hotel Booking Engine, Amenity Booking).

## Initial Boundary (pre-research hypothesis)

- Core use: sell and control admission to a physical place/experience (theme park, zoo, aquarium, museum, water park, family entertainment center, observation tower), validate entry, and manage the visit commercially (passes, memberships, on-site spend, groups).
- Primary users: attraction operator staff (box office, gate/admissions, F&B/retail, membership, marketing, management) plus guests acting self-service (online purchase, kiosks, self-reschedule).
- Nearest neighbors: Attraction Ticketing (ticketing slice), Event Ticketing Platform (seat/performance inventory), Tour Operator Management System (itinerary/departure inventory), Theme Park Management (ride/park operations), Museum Visitor Experience Platform (visitor experience layer), Cashless Venue Platform (stored-value slice), Hotel Booking Engine (lodging inventory).
- Unknowns: is capacity/timed entry defining or merely common? Are memberships/passes defining or common? Is on-site POS part of the Type? Where exactly does the boundary with Attraction Ticketing sit?

## Research Questions

1. What objects exist in the system's world (products, sessions, capacity, bookings, tickets, passes, memberships, guests)?
2. How are admission products defined (validity rules, pricing variations, time binding)?
3. How does capacity control work (timed entry, sessions, resources, entry points)?
4. Which sales channels exist (online checkout, box office POS, kiosk, phone/back office, resellers/OTA)?
5. How does entry validation work (scan, redemption, gates/turnstiles, re-entry)?
6. How are passes/memberships modeled (validity, renewal, benefits, member recognition)?
7. Is on-site spend (F&B/retail POS, stored value) inside the Type?
8. What roles and permissions matter (box office clerk, gate staff, manager approvals)?
9. What are the key lifecycles and exceptions (refunds, reschedule, wrong-day ticket, capacity full, banned guest, missing waiver, group check-in)?
10. What distinguishes this Type from Event Ticketing and Tour Operator systems?

## Representative Products

| Product | Segment focus | Customer tier | Product philosophy | Evidence level |
|---|---|---|---|---|
| ROLLER | FECs, trampoline parks, mini golf, VR, theme/water parks, zoos | SMB–mid | Cloud all-in-one: ticketing + POS + passes/memberships + marketing + payments | A (deep help center, Tier 1) |
| Tessitura | Museums, science centers, zoos/aquariums/gardens, performing arts | Mid–enterprise, cultural/nonprofit | Unified CRM at the center; ticketing & admissions + fundraising + membership on one patron record | B (feature pages, Tier 2) |
| accesso Passport | Theme & water parks, zoos & aquariums, museums, ski | Enterprise, high-volume | E-commerce-first SaaS sales platform + POS/scanning; sibling products for queuing/distribution | B (product pages, Tier 2) |
| Blackbaud Altru | Museums, zoos, aquariums, arts & cultural | Mid, nonprofit/cultural | Ticketing + membership + fundraising/donor conversion in one system | B (product page, Tier 2; operational docs unreachable) |
| Spektrix | Arts & culture ticketing (boundary sample) | Mid | Event + seating-plan centric ticketing with memberships/donations | B (support center index, Tier 2) |

Selection rationale: market representation across attraction segments (FEC/theme park vs cultural), different philosophies (operations-first cloud suite vs CRM-first vs e-commerce-first vs fundraising-first), different customer tiers, and one boundary sample (Spektrix) to test the edge toward Event Ticketing.

## Sources

- ROLLER Help Center (Tier 1): https://mysupport.roller.software/ — index (llms.txt), ROLLER glossary, "Get started with products, resources and schedules", "How guest and member check-in works". Fetched 2026-09-06.
- Tessitura (Tier 2): https://www.tessitura.com/ — home, "Ticketing & Admissions" feature page. Fetched 2026-09-06.
- accesso (Tier 2): https://accesso.com/ — home, Passport product page, Siriusware product page. Fetched 2026-09-06.
- Blackbaud Altru (Tier 2): https://www.blackbaud.com/products/blackbaud-altru — product page. Fetched 2026-09-06. Operational documentation at web.blackbaud.com unreachable from research environment (transport errors, 2 attempts) — Altru-specific operational claims kept weak.
- Spektrix Support Centre (Tier 2): https://support.spektrix.com/hc/en-gb — category index. Fetched 2026-09-06.

Source-access limitation: no public operational help center was reachable for accesso Passport or Blackbaud Altru. Claims about those products are held at product-page strength; no precise operational mechanics (limits, defaults, exact flows) are asserted for them.

---

## Product Observations

### ROLLER (evidence layer A — directly observed in official help center)

Positioning: cloud platform for venues/attractions (trampoline parks, mini golf, VR, escape rooms, theme parks, water parks, zoos). Admin surface "Venue Manager"; operational surfaces: POS (staff register), Self-Serve Kiosk, Waiver Kiosk, Mobile Check-in app, online Checkout (embedded or standalone, built with a checkout builder), and access gates via the Alvarado turnstile integration.

Core object model (from the official glossary and concept docs):

- **Venue** — "a physical park or attraction where bookings are redeemed". Venue group = multiple venues under one login.
- **Product** — "anything guests can buy": session pass, standard pass (day pass / event ticket / season pass), multi-pass, membership (recurring or fixed-price), party package, package, add-on, stock (retail/F&B), gift card, cashless card, wallet, donation, open-price product.
- **Pass** — product type giving access; **Ticket** = "manifestation of a pass"; **ticket type / variation** = child component defining price/resource variations (adult/child/concession).
- **Resource** — "defines the capacity of physical areas in a park to prevent overselling"; also rooms, classes, animal encounters, staff. Booking rules: single-booking vs multiple-booking; sharing rules (multiple products / single product / single ticket type); resource groups auto-allocate to smallest fitting resource. Booking rule is immutable once linked to a product.
- **Schedule / Session** — schedule = "reusable configuration of days on which a product is sold"; session = "an interval of time when an activity occurs". Schedules can link to venue operating hours (standard / temporary / future-dated), with session frequency, max booking window, exclusion dates.
- **Booking** — "order placed by a guest to be used at a venue containing booking items, purchase information and guest details"; statuses include draft / pending / confirmed / complimentary; booking holder; activity stream; notes; parked bookings at POS.
- **Redemption / check-in** — "checking a guest in means marking their ticket as used (redeemed)… it's what your attendance figures count". Ticket redemption: once per ticket unless the product allows multiple redemptions (multi-pass); happens on arrival; at POS, Mobile Check-in app, or access gate (scan wristband/barcode/QR via Alvarado). Membership redemption: applies member discounts, once per day per membership, at POS/online checkout/Venue Manager/gate; "a membership works much like a discount code".
- **Membership** — pass defining member benefits; member records with photos, custom IDs, printed cards; renewal; upgrade; entitlement-level redemption reports (date, member, booking, product, home vs away venue for multi-venue).
- **Waiver** — legal document set per product, attached to individual tickets; a ticket cannot be redeemed until its waiver is attached (exception: mass redemption for large groups); waiver kiosks; expiry reminders.
- **Guests/CRM** — guest/contact/company records, merge, export, guest flags (banned guests with POS approval prompt), segments, mailing lists, online guest accounts (self-manage bookings/passes/memberships).
- **Pricing & promotions** — price rules (quantity-based, time-based, early bird), discount codes (percentage / fixed amount / flat price / buy-and-get), purchase limits, product tags to target discounts.
- **Stored value** — gift cards (digital/physical, balances, refunds to gift card), cashless cards (with third-party arcade-cashless integrations: Sacoa, Intercard, Amusement Connect), wallet products.
- **Channel management** — OTA/reseller integrations: Viator/Tripadvisor, Tiqets, Klook, GetYourGuide, Civitatis, Trip.com, Groupon (voucher redemption at POS).
- **Payments** — gateways (e.g. Adyen, WorldPay), split payments, refunds (incl. refund-to-gift-card), invoices, payment request links, incomplete-payment handling, stored-card charges.
- **Staff & governance** — staff roles with per-feature permissions, POS PINs, manager approval for POS actions (refunds, banned-guest redemption, ticket-redemption approval setting), MFA for Venue Manager.
- **Reporting & finance** — sales/attendance/membership reports; attendance counted as redemptions (total vs unique); guest analytics counts one visit per guest per day; reporting categories/GL codes; tax & fees; regional fiscal compliance packs (Germany fiskaly/DATEV, Norway/Sweden/Spain EFSTA, UK VAT).
- **API** — booking API and reporting API.

Workflows observed:

- Setup: venue settings → products (+variations, waivers, upsells) → resources (+booking rules) → schedules (linked to operating hours) → channels → staff roles.
- Sale: online checkout / POS / kiosk → booking created → tickets issued (email/PDF, QR), booking confirmation.
- Arrival: find booking → redeem tickets (POS / mobile check-in / gate scan) → waiver check → membership redemption → settle any balance. Wrong-day ticket still redeems; POS offers reschedule with price difference applied. Banned guest requires approving POS PIN. Missing waiver blocks redemption (except mass group redemption).
- Capacity operations: monitor daily capacity and redemptions; temporarily block or reduce resource capacity; overbooking override exists.
- Exceptions: refunds (incl. after past date restrictions), parked bookings, split payments, reschedule, cancel/reactivate booking, restricted past-booking edits.

### Tessitura (evidence layer B — official feature pages)

Positioning: "one platform built to run your whole arts & culture organization" — markets include museums & galleries, science centers, zoos/aquariums/gardens, history & culture, plus performing arts. Modules: Unified CRM, Ticketing & Admissions, Fundraising, Memberships, Digital & E-commerce (TNEW), Education, Marketing, Reporting & Insights, Payment Processing, Retail, Ticket Scanning & Access Control, Cloud Hosting.

Admissions model (feature page):

- General & timed admission: "use timed admission to help visitors plan their journey"; "streamlined tools to manage capacity for time blocks and entry points"; "preset entry periods and locations with timed tickets for straightforward access control"; "sell in advance for a specific date or time, and sell both current and advance tickets at the door".
- Combos & bundles: plan-your-day packages; add-ons such as parking, dining, audio guides; membership prompt at purchase with "member benefits apply immediately to items in the cart"; composite tickets — "scan one barcode for entry to all elements of a package".
- Event ticketing (seated, seat maps) coexists on the same platform — the arts/culture dual nature.
- Group sales: tour groups and school groups; adjust ticket counts anytime; payment plans and deposit-only saved orders; automated discounts and complimentary tickets; "streamlined group check-in lets you scan a single barcode for the whole order and update attendance in real time"; book rooms and resources for the group visit; print agenda.
- Education: classes, workshops, camps registration; member early registration/discounts.
- Kiosks (partner KIS): sell tickets, capture customer info, automated ticket pickup, member recognition via card scan/number; PCI/EMV.
- Ticket Scanning & Access Control as a named capability.
- CRM-centered: attendance history, membership activity, donations tracked on the patron record; fundraising and membership conversion are first-class goals.

### accesso Passport (evidence layer B — official product pages)

Positioning: "end-to-end SaaS sales platform" for high-volume venues; "connected management of tickets, season passes, parking, meal deals and more".

- Smart pricing and capacity tools: "auto-adjust prices by date, demand or inventory and keep operations manageable in real time".
- Self-service portal: "let visitors reschedule tickets and manage payment plans without a phone call".
- "Integrate sleek POS stations, client-branded kiosks and modern Android scanning for instant validation. From purchase to entry."
- Sibling products (same vendor suite): LoQueue (virtual queuing), ingresso (distribution), Mobile App, Intelligence (analytics/AI), Paradox (ski), Horizon (ticketing), Siriusware (legacy on-prem POS for attractions/ski).
- Markets: theme & water parks, zoos & aquariums, tours & experiences, museums, cultural institutions, ski, live entertainment, hospitality.

### Blackbaud Altru (evidence layer B — official product page; operational docs unreachable)

Positioning: "Ticketing, Fundraising, and Membership – All In One" for museums, zoos, aquariums and experiences (arts & cultural organizations).

- "Online, in-person, and back-office sales" in one system.
- "Ticketing, memberships, donations and group sales provide a 360 view".
- "Track all interactions, attendance history, membership activity, and donations" per supporter.
- "Report on both earned and contributed revenue".
- Guest experience: "seamless ticketing and entry process with special considerations for members, advanced purchase, timed entry, and more".
- "Seamlessly integrated technology for your point-of-sale system… to accept and process payments of tickets, memberships, and donations".
- Partner-ecosystem extensions: self-serve kiosks, branded microsites/event calendars/donor portal, digital membership cards (wallet), "modern, convenient access control systems".
- Explicit goal: "turn first-time ticket buyers into members and donors".

### Spektrix (boundary sample — evidence layer B)

Support-center structure shows an event-centric ticketing model: Events, Seating Plans, Tickets, Pricing, Offers, Commissions, Subscriptions, Merchandise; box-office hardware (printers, scanners, PIN pads); payments; reporting; customer records/lists/tags; email campaigns; donations/Gift Aid/membership schemes; agents selling on behalf; website integration. No timed-entry/capacity-block admission model surfaced at index level — consistent with an arts/event ticketing platform rather than an attraction admission system, though its membership/donation machinery overlaps the cultural-attraction segment.

---

## Cross-product Comparison

| # | Finding | ROLLER | Tessitura | accesso Passport | Altru | Strength |
|---|---|---|---|---|---|---|
| 1 | Operator-defined admission products (ticket types with price variations; passes; memberships) | ✓ products/ticket types/variations | ✓ admission products & prices | ✓ tickets, season passes | ✓ ticketing + memberships | B — cross-product |
| 2 | Multi-channel sale: online checkout + on-site POS/box office + kiosk + phone/back office | ✓ checkout/POS/SSK/Venue Manager | ✓ online/door/kiosk/back office | ✓ e-commerce/POS/kiosks | ✓ online/in-person/back-office | B — cross-product |
| 3 | Sale produces a recorded transaction (booking/order) holding items + purchaser | ✓ booking/booking items | ✓ orders | ✓ cart/order | ✓ sales | B — cross-product |
| 4 | Capacity control over admission (timed entry / sessions / time blocks / entry points) | ✓ resources+sessions+operating hours | ✓ time blocks & entry points | ✓ real-time capacity tools | ✓ timed entry | B — cross-product (mechanism depth varies; open-dated tickets also exist) |
| 5 | Admission entitlement validated at entry (scan → redemption → attendance) | ✓ redemption at POS/mobile/gate | ✓ scanning & access control; composite barcode | ✓ Android scanning "instant validation" | ✓ access control systems | B — cross-product |
| 6 | Passes/memberships with validity, renewal, benefits, member recognition | ✓ memberships/annual/season/multi-pass, photos, renewal | ✓ memberships + digital cards + renewal | ✓ season passes | ✓ memberships + digital cards | B — cross-product |
| 7 | Guest/patron records & repeat-visit relationship | ✓ guest CRM, segments, flags | ✓ unified patron CRM (center of product) | ◐ self-service accounts (weak) | ✓ supporter 360 | B — cross-product (depth varies by segment) |
| 8 | On-site spend beyond admission (F&B/retail/add-ons) | ✓ stock/add-ons/cashless/gift cards | ✓ retail + parking/dining/audio add-ons | ✓ parking, meal deals | ◐ POS for tickets/memberships/donations | B — cross-product (depth varies) |
| 9 | Group sales (school/tour/party groups) | ✓ group passes/party packages | ✓ purpose-built group sales | not evidenced | ✓ group sales | B — cross-product |
| 10 | Promotions/pricing rules (peak/off-peak, early bird, discount codes) | ✓ price rules + discount codes | ✓ offers + dynamic pricing | ✓ smart pricing (date/demand/inventory) | not evidenced | B — cross-product |
| 11 | Reporting on attendance + revenue (+ GL/tax) | ✓ attendance/sales/GL/fiscal packs | ✓ business insights | ✓ Intelligence (analytics) | ✓ earned + contributed revenue | B — cross-product |
| 12 | Reseller/OTA distribution | ✓ channel mgmt (Viator, Tiqets, Klook, GYG, Groupon…) | ✓ agents interface | ✓ ingresso distribution | not evidenced | B — cross-product |
| 13 | Waivers for risk activities | ✓ (deep: per-product, blocks redemption, kiosks) | not evidenced | not evidenced | not evidenced | A — product-level; Optional |
| 14 | Donations/fundraising | ◐ donation product type | ✓ fundraising module | not evidenced | ✓ core positioning | Segment variant (cultural) |
| 15 | Education/classes/camps registration | ◐ recurring passes for classes | ✓ education module | not evidenced | not evidenced | Optional |
| 16 | Virtual queuing | not evidenced | not evidenced | ✓ LoQueue (sibling product) | not evidenced | Vendor-specific |
| 17 | Cashless/stored-value wristbands & game cards | ✓ cashless cards/wallets + arcade integrations | not evidenced | not evidenced | not evidenced | Optional (FEC posture) |
| 18 | Seated event ticketing on the same platform | not evidenced | ✓ (coexists) | ◐ (live-entertainment products exist in suite) | not evidenced | Segment variant (arts/culture dual nature) |
| 19 | Regional fiscal compliance (e-invoicing/fiscal devices) | ✓ DE/Nordics/ES/UK packs | not evidenced | not evidenced | not evidenced | Regional variant |

Legend: ✓ observed; ◐ partially/weakly observed; "not evidenced" = not found in reachable sources (absence of evidence, not evidence of absence).

---

## Abstraction Levels

### L0 — Defining Invariant (minimal)

An Attraction Management System is an operator-side system for a visitor attraction in which:

1. **Operator-defined admission products** — the attraction defines what grants entry (ticket types, passes, memberships) as catalog products carrying price and validity rules.
2. **Sale → transaction → issued admission entitlements** — purchases through the system's channels are recorded as transactions (bookings/orders) that issue redeemable admission entitlements (tickets / pass validity).
3. **Entry validation producing attendance** — entitlements are validated/redeemed at the attraction's point of entry, and that redemption is the system's attendance record.

Historical/market-sample check (§24-style): a small museum or regional attraction selling open-dated paper-equivalent tickets at a counter and scanning them at the door still satisfies all three properties — no timed entry, no memberships, no OTA distribution, no cashless wristbands required. Conversely, remove entry validation and it collapses into generic e-commerce; remove operator-defined admission products and it is not selling admission at all. The three properties hold.

### L1 — Common Mature Structure

Present across the researched sample; expected in mature modern products but not required for recognition:

- Capacity & session management: timed entry, time blocks/entry points, session schedules tied to operating hours, max booking windows, capacity monitoring, block/reduce capacity.
- Passes & memberships: season/annual/multi-visit passes; memberships with renewal, upgrade, benefits (discounts), member recognition (photos/IDs/cards), digital membership cards.
- On-site POS: box-office selling, F&B/retail add-ons, split payments, refunds, manager approvals.
- Self-service kiosks: selling, waiver signing, ticket pickup, member recognition.
- Guest records/CRM: purchaser identity, visit history, segments, banned-guest flags, online guest accounts.
- Promotions: price rules (peak/off-peak, early bird, quantity), discount codes, purchase limits.
- Group sales: school/tour/party groups, deposits/payment plans, group check-in (single barcode for whole order).
- Gift cards / stored value.
- Reseller/OTA distribution and voucher redemption.
- Reporting: sales, attendance (redemptions), membership; GL codes; tax handling.
- Staff roles & permissions; manager approval for sensitive POS actions.
- Access hardware integration: scanners, turnstiles/gates, RFID/wristbands.

### L2 — Variant / Optional Structure

Depends on segment, geography, deployment, business model:

- Segment shape: FEC/water park (parties, game credits, waivers, cashless) vs theme park (high-volume capacity, season passes, meal deals) vs museum/zoo/aquarium (timed entry, memberships, donations/fundraising, education, patron CRM depth) vs ski (season passes, gates) vs regional small attraction (counter sale + scan only).
- Timed-entry strictness: mandatory time slots vs open-dated tickets; per-entry-point capacity.
- Cashless/stored-value posture: wristbands/game cards (often via third-party arcade systems).
- Dynamic/demand-based pricing.
- Virtual queuing.
- Education/class/camp registration.
- Donations/fundraising and donor-conversion tooling (cultural segment).
- Seated event ticketing coexisting on the same platform (arts/culture dual nature).
- Deployment: cloud SaaS vs legacy on-prem; multi-venue/venue groups; home-vs-away membership redemption.
- Regional fiscal compliance packs (e-invoicing, fiscal devices, VAT handling).
- Guest mobile apps, digital wallet passes.

### L3 — Vendor-specific (kept out of the final document)

- ROLLER: Venue Manager/POS/Playground naming; resource booking rules (single vs multiple booking, product-sharing rules); party package machinery; POS PIN/manager codes; Alvarado gate integration; named OTA integrations; Playground training environment.
- Tessitura: TNEW e-commerce; patron-centric unified CRM spanning ticketing+fundraising+membership; seated subscriptions coexisting with admissions; KIS kiosk partnership.
- accesso: product-family split (Passport/Horizon/Paradox/Siriusware/LoQueue/ingresso); LoQueue virtual queuing; Intelligence AI/analytics.
- Blackbaud Altru: Blackbaud fundraising ecosystem integration; donor-propensity tooling; earned+contributed revenue framing.

---

## Boundary Findings

| Neighboring Type | Relationship | Distinction (what to remove/add to flip the Type) |
|---|---|---|
| Attraction Ticketing (sibling leaf) | slice of the same domain | Ticketing is the sell+validate slice (products, channels, entitlements, gates). The Management System spans the whole admission business: capacity/session operations, memberships, on-site spend, guests, reporting. Remove the operational breadth and only the ticketing slice remains. |
| Event Ticketing Platform | adjacent, most confusable | Event ticketing's inventory unit is performances/seats (seat maps, one-off events); attraction's inventory unit is admission capacity to a place (no seat map as primary unit). Arts/culture platforms (Tessitura, Spektrix) contain both models — the Type boundary is the primary inventory model, not the vendor. |
| Tour Operator Management System | adjacent | Tour systems sell departures/itineraries (multi-day, guide/resource assignment, per-departure capacity); attraction systems sell place admission. Timed entry resembles a departure slot, but there is no itinerary/guide model. |
| Theme Park Management | adjacent, complementary | Park operations (ride availability, queue, maintenance, safety) vs the commercial admission layer. A theme park runs both; they are different Types. Remove the commercial admission layer and only park operations remain. |
| Museum Visitor Experience Platform | adjacent, complementary | Visitor-facing experience layer (interpretation, guides, wayfinding) vs commercial admissions layer. |
| Cashless Venue Platform | slice | Stored-value payment slice of the on-site spend capability. |
| Digital Waiver Management | slice | Waiver capture/compliance slice (deep in ROLLER, absent in others' reachable docs). |
| Hotel Booking Engine / Restaurant Reservation Platform | distant | Date/time inventory exists, but the product is lodging/tables, not admission to an attraction; no entry validation semantics. |
| Amenity Booking Platform | distant | Bookable amenities for a property's residents/guests; not a public admission business. |
| E-commerce Platform | underlying capability | Online checkout is one channel; without operator-defined admission products + entry validation it is just e-commerce. |

Taxonomy observation (for STATUS Boundary Issues): the directory places Attraction Ticketing, Theme Park Management, Family Entertainment Center Management, Zoo / Aquarium Visitor Operations, Museum Visitor Experience Platform, Cashless Venue Platform, and Digital Waiver Management as siblings of Attraction Management System. Research indicates several of these are slices or segment variants of the same underlying admission-business Type rather than fully independent Types; they deserve their own research passes to confirm (not rewritten here).

---

## Uncertainties

- Altru operational mechanics (timed-entry configuration, membership model details, gate hardware behavior) — product-page evidence only; operational docs unreachable. All Altru-specific claims kept at positioning level.
- accesso Passport operational mechanics (capacity tool behavior, self-service portal scope) — product-page evidence only.
- Tessitura admissions mechanics — feature-page level; detailed documentation is behind member login. Composite-ticket and group check-in behaviors are quoted from official feature copy but not observed step-by-step.
- Whether "group ticket" (one ticket admitting multiple people) is a common pattern — observed in ROLLER only; treated as product-level.
- Exact capacity mechanics differ per product (resource-based vs time-block vs entry-point); no precise numeric limits asserted anywhere.
- Re-entry rules, validity windows, refund windows: product-dependent; not generalized.

## Final Synthesis

The Attraction Management System is the operator-side system of record for a visitor attraction's admission business. Its defining core is small: the attraction defines admission products; selling them through the system's channels produces recorded transactions that issue admission entitlements; entitlements are validated at entry, and that validation is the attendance record. Around this core, mature products add a stable ring of capabilities: capacity/session control (timed entry), passes and memberships with renewal and member recognition, on-site POS and stored value, kiosks, guest CRM, promotions, group sales, reseller distribution, reporting, and role-governed operations. Segment shapes (FEC vs theme park vs cultural institution) change which ring capabilities dominate — parties and cashless for FECs; donations, patron CRM and education for cultural institutions; high-volume capacity and season passes for theme parks — but the defining core and the capability ring stay the same. The Type's sharpest boundary is with Event Ticketing (seat/performance inventory vs admission/capacity inventory) and with its own sibling slices (Attraction Ticketing, Cashless Venue, Digital Waiver), which are parts of this whole.
