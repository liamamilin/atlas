# Research Notes — Family Entertainment Center Management

Research date: 2026-09-07

## Research Goal

Understand what Family Entertainment Center (FEC) Management software is as an Application Type: its defining core, its standard capability ring, its variants, and its boundaries — especially against the sibling leaf Attraction Management System, whose research pass (2026-09-06) flagged FEC Management as a probable "segment posture" of the admission-business Type. This pass must confirm or refine that flag: is FEC Management an independent Type with its own defining core, a segment variant, or a slice?

## Initial Boundary (pre-research hypothesis)

An FEC is a multi-activity entertainment venue (arcade, trampoline park, laser tag, bowling, mini golf, go-karts, soft play, sometimes F&B-heavy "eatertainment"). Hypothesis before research: FEC Management software is the operator-side whole-venue system whose center of gravity is (a) the arcade/play-card economy, (b) birthday-party/group-event operations, (c) unified POS across admissions/games/F&B/retail/prizes — and which differs from Attraction Management System's dated-admission/entry-validation center. Nearest neighbors: Attraction Management System, Attraction Ticketing, Cashless Venue Platform, Digital Waiver Management, Event Ticketing/Registration, Restaurant POS, Gym Management.

## Research Questions

1. What objects does the system manage? (games, attractions, cards, parties, prizes, checks…)
2. What is the unit of sale — admission, play value, session, party, or all?
3. How is access to activities controlled and validated?
4. What is the party/group-event machinery, exactly?
5. How does the arcade heritage (game cards, prize redemption) show up in the software structure?
6. How do F&B and retail fit — add-on or first-class revenue center?
7. What accounting behaviors exist around stored value (deferred revenue)?
8. How do products differ by segment (arcade vs trampoline vs karting vs bowling vs eatertainment)?
9. Where is the boundary with Attraction Management System, and with the slice Types (Cashless Venue, Digital Waiver)?
10. What is vendor-specific vs common mature structure?

## Representative Products

Selected for market representability, documentation quality, different product philosophies, different customer tiers and geographies:

| Product | Philosophy / position | Tier & geography |
|---|---|---|
| Embed | Game-card/cashless-first FEC specialist; integrated hardware+software ecosystem | Global chains (Dave & Buster's-class) to single arcades; 59+ countries |
| Semnox Parafait | Full-stack FEC suite (card system + POS + parties + CRM); vendor splits FEC (Parafait) vs water/theme parks (Tixera) vs F&B (Deliko) into separate product lines | Global mid-market; 60+ countries; chain HQ management |
| CenterEdge Software | US mid-market all-in-one venue suite, POS-centric, payments-integrated | US FECs/waterparks/adventure parks; single sites to regional chains |
| ROLLER | Cloud-first self-serve venue platform (products/bookings model); serves FECs, trampoline parks, play centers, attractions | SMB-to-enterprise; global SaaS |
| Clubspeed | Karting-heritage FEC venue management (race timing, competitions, fleet) | Karting chains + multi-activity FECs; 1,800+ venues, 70+ countries |

ROLLER was also sampled by the Attraction Management System pass (evidence continuity). Embed's help centre (apps.helixleisure.com) and Clubspeed's detailed feature list are access-gated; their evidence is product-page level.

## Sources

Tier 1 (operational documentation):
- ROLLER Help Center (mysupport.roller.software): index/llms.txt, glossary, "Get started with cashless cards", "Create party package products". Fetched 2026-09-07.

Tier 2 (official product pages):
- CenterEdge: homepage, FEC industry page, Admissions & Attractions, Event Bookings, Redemption add-on. Fetched 2026-09-07.
- Semnox Parafait: FEC industry page, Party Bookings, Inventory & Redemption Management; Semnox corporate site. Fetched 2026-09-07.
- Embed: homepage, Software Solutions (TOOLKIT). Fetched 2026-09-07.
- Clubspeed: homepage, main product page. Fetched 2026-09-07.

Source-access limitations: no public operational help-center articles were reachable for Embed, Semnox, CenterEdge, or Clubspeed (login-gated or absent). All non-ROLLER claims are therefore product-page level; no precise operational specifics (numeric limits, exact state names, default values) are asserted for those products. ROLLER-only operational details are marked product-specific.

## Product Observations

### ROLLER (evidence layer A — directly observed in official help center)

- Glossary (canonical vocabulary): **Party** = "session-based group booking that occurs across multiple resources at a venue"; **Resource** = "defines the capacity of physical areas in a park to prevent overselling"; single-booking vs multiple-booking resources; **Session pass** (time-restricted activity), **Standard pass** (no specific duration), **Multi-pass**, **Recurring pass** (classes), **Membership**; **Runsheet** = grid of session-based bookings at booking-item level; **Redemption** = exchanging a pre-purchased pass for a booking (entry sense — distinct from arcade prize redemption); **Waiver/Minor/Waiver kiosk**; **Venue/Venue group/HQ**; **Reporting category (GL code)**; **Manager code/POS PIN**.
- Products model: session passes (cited for mini golf, VR, escape rooms), game-based per-guest session passes, standard passes, multi-passes, recurring passes, memberships (recurring-payment and fixed-price; booking agreements; member photos; click-to-cancel compliance), party packages, cashless game cards, wallets, gift cards, stock, add-ons.
- Cashless cards (integration-based): providers Sacoa, Amusement Connect, Intercard; **one provider per venue**; card values in cash, time (minutes), or activities; sell online/in-venue/bundled in party packages; assign physical RFID cards at POS; card cash balance usable as POS payment method for food/drinks/tickets/merch; top-up; balance check; full card transaction history at POS; bulk-assign sequential cards to group bookings; balance merge for lost cards (Sacoa/Intercard); kiosk sales sync (Sacoa); HQ product sharing across venues.
- Party machinery: party package product with per-guest or per-party pricing; variations (Classic/Premium/Additional Guest); **party program** = itinerary of resources in sequence with start/end times (e.g. 60 min trampoline → 60 min party room); buffer time after party for cleanup/reset (blocks the room); book-out of multi-booking resources for exclusive party use; party name; guest list/invitations managed by booker online; deposits (percentage or fixed); waiver gating + waiver reminder emails; booking reminders; custom forms (dietary); itemized tickets; party packages not directly sellable at POS but editable there; run sheets; downloadable party summary for the day; party-room double-booking prevention; party reports (average party size/value, ancillary party spend).
- Check-in & access: POS, self-serve kiosk, Mobile Check-in app (barcode/NFC); redeem tickets/memberships; wristband allocation; member photo verification; banned-guest flags with approval flow; manager approval setting for ticket redemption.
- Capacity: resources with capacities, operating hours, block/reduce capacity, overbooking override, daily capacity view.
- Pricing & promotions: time-based/early-bird/quantity price rules; discount codes (percentage/fixed/flat/buy-get); peak/off-peak guidance.
- Reporting: reporting categories/GL codes; accrual revenue tracking for gift cards; membership revenue recognition; fiscal compliance packs (Germany fiskaly/DATEV, EFSTA Norway/Sweden/Spain, UK VAT).
- Multi-venue: HQ account, shared products/pricing/permissions/reporting.
- Other: online waivers (deep: pre-arrival, QR, kiosk, expiry, per-product gating), online checkouts, POS (split payments, park bookings, tabs), integrations (OTAs Viator/Tiqets/Klook/GYG/Civitatis/Trip.com, Groupon, Alvarado gates, Workforce.com, CashGuard), ROLLER Payments/Capital, Intelligence (iQ, Activity Center, Guest Experience Agent — AI-era).

### CenterEdge (evidence layer B — official product pages)

- Suite: Advantage Sales (Ticket & Retail Sales; Food & Beverage; Admissions & Attractions; Guest Hub), Advantage Console (System Setup; Inventory; Cash Control & Accounting; Messaging; Team Management incl. staff scheduling; Reporting & Analytics), Advantage Events (Event Bookings; Event Communications; Event Planning; Event Processing), hardware (POS stations, tablets, kiosk, printers), CenterEdge Payments, add-ons (Redemption, Digital Signage, Integrations), CenterEdge Play (integrated cashless: kiosks, readers, unattended payments).
- FEC positioning: "one solution for your entire facility"; activity list spans rides, arcade, batting cages, bowling, bumper cars, restaurants, kart racing, laser tag, mini golf, redemption games, roller skating, VR, water slides; sells "attraction tickets, player cards, concessions, combos and season passes"; loyalty programs.
- Admissions & Attractions: online tickets with barcodes (print or scan from mobile; Apple Wallet); headcounts auto-tally on scan; waivers (online/kiosk/mobile; required and verified at check-in per attraction or park-wide; expiration; attached to guest records); access control (unattended scanners; works with tickets, passes, memberships, or stored value; turnstiles; lockers; combinable with cashless hardware); capacity management (attraction/rental/class capacities and schedules; timed attractions with durations; tickets removed from capacity in real time; series classes sold as packages).
- Event Bookings: event/party packages bundling attractions, admissions, F&B, gameplay; adjust passes, capacity, discounts, gameplay, card values on the fly; special events (one-off or recurring series; capacities; individual tickets for concerts/movies; nonprofit tax exemption); reserved areas (party rooms, VIP lounges, cabanas; graphical display; online selection; automatic double-booking prevention); upgrades/add-ons per person or per event; add game-card value instantly even while card in use.
- Redemption add-on: arcade prize counters and redemption stores; winner accounts; ticket tallying; scan-based actions with barcode sheets; custom denominations/collectible cards; prizes in the same unified inventory as F&B with separate reporting; frequent-player rewards program (tiers; redemption tickets as rewards).
- Cashless integrations: sell and reload attraction and game cards from POS; "post usage from cards as sales to allow for true revenue-deferred reporting".
- F&B: quick-service and full-service; recipes; kitchen printers and display systems; inventory.

### Semnox Parafait (evidence layer B — official product pages)

- FEC suite modules: wireless RFID debit card readers (tap-to-play); POS ("weaves all transaction points and services — from F&B sales to party bookings — into a single channel"); self-service kiosks (purchase RFID cards, check balance, recharge); RFID cards/wristbands; party/event reservations; slot-based bookings (time management with Radian wristband check-in/check-out); waiver management (online, POS, kiosk, staff tablets); inventory & redemption; online booking module; SmartFun branded mobile app (purchases, recharge, balance); digital signage; mobile POS; 360° CRM; BizInsights analytics ("sales, game trends, operations").
- Party bookings: guests check available slots, reserve party halls, make group bookings, customize and schedule, pay online (credit card/PayPal); multi-channel sales (web app + POS); **party host assignment with checklists of items to execute before, during, and after the party**; combo packages as upsell; reschedule per-attraction (override one attraction instead of cancelling the whole reservation); real-time sync across channels to avoid double bookings.
- Inventory & redemption (eZee): "covers the entire cycle — from issuing the ticket to redemption to remainder-value management"; HQ + distribution centers; BOM; perishables/LOTs; auto-generated purchase orders; multi-screen POS serving up to 6 customers at once; pause an individual redemption while the guest chooses; barcoded items for redemption and gift tracking; reports on items redeemed, stock in hand, below-minimum stock.
- Multi-location: manage a chain from Corporate HQ; card roaming across locations (client testimony).
- Vendor splits segments into separate product lines: Parafait (FEC/arcades/trampoline/laser tag/indoor playgrounds/bowling) vs Tixera (water/theme parks/museums/aquariums) vs Deliko (F&B).
- Clients include large FEC chains (Chuck E. Cheese-class RFID rollout; Play Pass game-performance metrics).

### Embed (evidence layer B — official product pages)

- Ecosystem: hardware (smartTOUCH arcade debit card readers — tap/swipe; KIOSK+ self-service kiosks; custom game cards & wearables on Playwave® contactless technology, roaming across locations) + software TOOLKIT.
- TOOLKIT Core Bundle ("FEC essentials"): Mobile Wallet (Apple/Google certified mobile payment — pay and play from phones), SALES (POS), PRIZES (ticket and redemption management), REPORTS (real-time data, multi-location, automated scheduling).
- Pro add-ons: BOOKINGS (reservations online or in-venue with e-waiver integration), STATS (BI dashboard), CGM (Central Games Management — one interface for all games, pricing, and promotions across all locations; remote game pricing).
- GURU: back-of-house configuration (inventory, pricing, promotions, users, reader configurations).
- Hybrid tickets (physical + e-tickets); kiosks that take old tokens in exchange for credits; unattended payments.
- Industries: amusement parks & indoor parks, bowling centers, cinemas, eatertainment, FEC & arcades, route operators.
- Chain tier customers (Dave & Buster's, TEEG, Six Flags, Bandai Namco-class logos).

### Clubspeed (evidence layer B — official product pages)

- Features: touchscreen POS (registration, book events, schedule activities, merchandise, gift cards, food); CRM; cashless card systems (purchase or recharge gaming cards); online booking; gift card module; loyalty programs (points/gifts); waivers (adults add minors with one click; family registration in minutes); inventory management (auto-generated orders, shrinkage, reorder points); **garage management** (kart fleet maintenance, parts cost, preventative maintenance); **race timing ProSkill™** (integrates timing hardware; run races, assign karts, grid by ProSkill, manage tournaments); gamification with real-time leaderboards (race results, positions); online customer portal (stats/history/skills); memberships (auto-bill, member pricing); automated marketing (birthday emails, coupons by last visit/DOB/purchase history); operational alerts; customizable reporting (fiscal printers); API (leaderboards, third-party displays); 24/7/365 support.
- Industries: karting, trampoline, FEC, golf, amusement park, arcade, axe throwing, batting cages, bowling, escape room, laser tag, obstacle course, rope course, zip line.
- Scale claims: 1,800+ venues, 70+ countries, 300M+ competitions ranked, 25K daily activities.

## Cross-product Comparison

| # | Finding | Embed | Parafait | CenterEdge | ROLLER | Clubspeed | Strength |
|---|---|---|---|---|---|---|---|
| 1 | Venue's games/attractions/activities configured as chargeable products (per play / per time / per session) | ✓ game pricing (CGM) | ✓ slot-based + game pricing | ✓ timed attractions, capacities | ✓ session/standard/game-based passes | ✓ activities + races | B |
| 2 | Play entitlement carried on a guest credential (card/wristband) with cash/time/activity value; tap-to-play | ✓ native (readers+cards) | ✓ native (readers+cards) | ✓ (Play native + integrations) | ✓ via provider integrations (Sacoa/Amusement Connect/Intercard) | ✓ via cashless integrations | B |
| 3 | System-mediated access validation at activities (reader tap, scanner, check-in, heat assignment) | ✓ readers | ✓ access control + readers | ✓ access control, unattended scanners | ✓ check-in/redemption, wristbands, gates | ✓ registration, race heats | B |
| 4 | One transaction system across revenue centers (admissions, play, F&B, retail) | ✓ SALES | ✓ single-channel POS | ✓ Advantage Sales | ✓ POS + checkouts | ✓ POS | B |
| 5 | Party/group-event booking as a first-class business line | ◐ Pro add-on (BOOKINGS) | ✓ flagship module | ✓ flagship module (Events) | ✓ flagship (party packages/program) | ✓ booking wizard | B (near-universal; not in Embed core) |
| 6 | Party resource management (rooms/areas, double-booking prevention, itineraries, buffers) | not evidenced | ✓ halls, per-attraction override, real-time sync | ✓ reserved areas, auto double-booking prevention | ✓ party program, buffers, book-out, runsheets | ◐ scheduling calendar | B (depth varies) |
| 7 | Prize/redemption management (arcade tickets → prizes) | ✓ core (PRIZES) | ✓ module (e-ticket cycle, remainder value) | ✓ add-on (counters/stores, winner accounts) | not evidenced natively (delegated to card providers) | not evidenced | B with placement variance |
| 8 | Online booking/checkout | ✓ BOOKINGS | ✓ online booking module | ✓ online event booking | ✓ progressive checkouts | ✓ Club Booking | B |
| 9 | Self-service kiosks | ✓ KIOSK+ | ✓ | ✓ | ✓ SSK | ✓ registration kiosk | B |
| 10 | Digital waivers | ◐ e-waivers in BOOKINGS | ✓ module | ✓ integrated, per-attraction or park-wide | ✓ deep (pre-arrival/QR/kiosk/expiry) | ✓ family/minor registration | B |
| 11 | Passes/memberships with renewal & recognition | ◐ loyalty via cards | ✓ CRM | ✓ season passes/memberships | ✓ deep (recurring, photos, agreements) | ✓ auto-bill memberships | B |
| 12 | Guest CRM/records | ✓ guest data | ✓ 360 CRM | ✓ Guest Hub | ✓ guest records/segments/flags | ✓ CRM | B |
| 13 | Loyalty/rewards programs | ✓ via cards | ✓ | ✓ frequent-player tiers | ✓ loyalty module | ✓ points/gifts | B |
| 14 | F&B as revenue center | ◐ via SALES | ✓ (sister product Deliko) | ✓ deep (recipes, KDS) | ✓ F&B checkouts/POS | ✓ food logging | B (depth varies) |
| 15 | Inventory management | ✓ GURU | ✓ eZee (BOM, perishables, auto-PO) | ✓ unified incl. prizes | ✓ stock products | ✓ auto-PO, shrinkage | B |
| 16 | Reporting with revenue centers/GL; attendance | ✓ REPORTS | ✓ BizInsights | ✓ cash control & accounting | ✓ GL codes, fiscal packs | ✓ custom reports, fiscal printers | B |
| 17 | Multi-location / chain management | ✓ CGM, roaming cards | ✓ corporate HQ, card roaming | ◐ (not evidenced) | ✓ HQ/multi-venue | ✓ (1,800+ locations) | B |
| 18 | Deferred-revenue treatment of stored value | not evidenced | not evidenced | ✓ explicit ("post usage as sales… revenue-deferred") | ✓ accrual gift-card/membership revenue | not evidenced | B (2 products) |
| 19 | Race timing / kart heat & fleet management | not evidenced | not evidenced | not evidenced | not evidenced | ✓ ProSkill, garage mgmt | product-specific (karting segment) |
| 20 | Mobile app / mobile wallet | ✓ Mobile Wallet (Apple/Google) | ✓ SmartFun app | ◐ Apple Wallet tickets | ✓ online accounts, wallet passes | ◐ customer portal | B |
| 21 | AI-era assistance | not evidenced | not evidenced | not evidenced | ✓ Intelligence (iQ, Guest Experience Agent) | not evidenced | product-specific (era-typical) |

Legend: ✓ observed; ◐ partially/weakly observed; "not evidenced" = not found in reachable sources (absence of evidence, not evidence of absence).

## Abstraction Levels

### L0 — Defining Invariant (minimal)

A Family Entertainment Center Management application is an operator-side whole-venue management system for a multi-activity entertainment center in which:

1. **The venue's play is a configured, chargeable catalog** — the operator defines what play costs and how it is accessed: game plays, attraction time, sessions, admission — as products carrying price and access rules.
2. **Play entitlements are issued, carried, and validated by the system** — guests hold value or rights (credits, minutes, sessions, passes) on a credential or booking, and the system validates that entitlement at the moment of play, per activity, throughout the visit.
3. **One transaction system spans the venue's revenue centers** — admissions, play, food & beverage, retail (and prizes) ring through the same selling surface and land in one operational record for the venue.

Removal tests:
- Remove (1) → a generic retail/restaurant POS or booking tool; no play semantics.
- Remove (2) → an uncontrolled honor-system floor or a pure payment system; the venue cannot meter or gate what guests play.
- Remove (3) → disconnected point tools (an arcade card system alone = the Cashless Venue Platform slice; a restaurant POS alone = Restaurant POS); the Type's "whole-venue" identity collapses.

Historical/market-sample check: the token-and-paper-ticket era FEC (coins at each machine, paper redemption tickets, one cash register, a party book) satisfies the same three structures conceptually — play was chargeable, access was mediated by the machines' mechanisms, and selling ran through one register. The RFID card/wristband is the modern implementation of the play entitlement, not the definition. Regional and chain variants (card roaming across sites, HQ management) sit above the core.

### L1 — Common Mature Structure

Present across the researched sample; expected in mature products but not required for recognition:

- **Play-value credential economy**: cards/wristbands loaded with cash, time, or activity entitlements; purchase/reload at counter, kiosk, or app; balance usable as payment at venue POS; balance check and transaction history; lost-card replacement with balance merge.
- **Party & group-event operations**: bookable party packages (per-guest or per-party pricing, variations), party rooms/reserved areas with double-booking prevention, party itineraries across resources with transition buffers, deposits, guest lists/invitations, party-day run sheets and summaries, host assignment with pre/during/post checklists (single-product direct), rescheduling.
- **Prize redemption**: winner accounts, ticket/point tallying (custom denominations), prize inventory (often unified with general inventory but separately reported), scan-based counter operations, remainder-value management.
- **Admissions, passes & memberships**: session/standard/multi-visit passes, season passes, recurring memberships with renewal, member recognition (photos/cards).
- **Digital waivers**: online/kiosk/mobile capture, minor/guardian handling, expiry, verification at check-in, per-activity or venue-wide gating.
- **F&B and retail POS with inventory**: quick/full service, recipes, kitchen displays, unified inventory with auto-purchasing.
- **Self-service kiosks**: card purchase/recharge, waiver signing, check-in, registration.
- **Guest CRM & loyalty**: guest records, visit history, segments, rewards programs, birthday marketing.
- **Pricing & promotions**: time-based/peak-off-peak rules, early bird, discount codes, bundles.
- **Reporting**: sales by revenue center, attendance/headcounts, GL-code export, cash control; deferred-revenue treatment of stored value (documented in 2 of 5 products).
- **Multi-location**: HQ/chain management, shared configuration, cross-site card roaming.
- **Online booking/checkout and guest mobile apps/wallets**.

### L2 — Variant / Optional Structure

Depends on segment, geography, deployment, business model:

- **Card-system packaging**: native card system (own readers/cards) vs integration with a third-party cashless provider; some platforms constrain a venue to one provider (product-documented in 1 of 5).
- **Segment postures**: arcade/redemption-centric; trampoline/session-centric (waiver-heavy, timed sessions); karting (race timing, heat/grid assignment, kart fleet maintenance — single-product evidence); bowling (lane operations — not directly evidenced); eatertainment (full-service dining dominant); soft play/kids clubs.
- **Deferred-revenue accounting depth** for stored value and memberships.
- **Regional fiscal compliance** (e-invoicing/fiscal devices/VAT packs).
- **Unattended payments, digital signage, RFID lockers, virtual queuing** (not evidenced in this sample).
- **AI-era assistance** (insights, guest-experience agents — 1 of 5).
- **Deployment**: cloud SaaS vs on-prem heritage; browser-based vs dedicated devices.

### L3 — Vendor-specific (kept out of the final document)

- Embed: TOOLKIT/SALES/PRIZES/BOOKINGS/STATS/CGM/GURU module names; Playwave® media; Apple/Google-certified Mobile Wallet positioning; token-exchange kiosks.
- Semnox: Parafait/Tixera/Deliko product-line split; SmartFun app; Radian wristband; BizInsights; eZee inventory; multi-screen redemption POS details.
- CenterEdge: Advantage Sales/Console/Events naming; Guest Hub; CenterEdge Play; dual-pricing payments program.
- ROLLER: Venue Manager/Playground naming; party program/buffer/book-out mechanics detail; one-provider-per-venue rule; named integration catalog; Intelligence/iQ/Activity Center.
- Clubspeed: ProSkill™ race grading; garage management; online customer portal stats; competition-ranking claims.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (what to remove/add to flip the Type) |
|---|---|---|
| Attraction Management System (sibling leaf) | closest sibling; shared DNA | AMS centers **dated admission to a place**: admission products → sale → entitlement → entry validation = attendance record. FEC Management centers the **venue's internal play economy**: chargeable play per activity, credentialed play value spent across the visit, parties as a business line, prizes; many FEC visits have no dated admission at all (walk in, load a card, play). Remove the play economy + party machinery and only the admission slice remains (→ AMS posture); add dated-admission capacity as the primary inventory and it becomes AMS. Vendors overlap heavily (several sampled products serve both segments; one vendor splits FEC vs theme-park into separate product lines). |
| Attraction Ticketing (sibling leaf) | slice | Sell+validate slice of the admission business; FEC Management spans the whole venue's revenue operations. |
| Cashless Venue Platform (sibling leaf) | slice | The stored-value payment loop (credential + account + spend points) is one layer of FEC Management. A standalone arcade card system without whole-venue POS/parties/prizes is that Type, not this one. |
| Digital Waiver Management (sibling leaf) | slice | Waivers are a standard capability here; the dedicated specialist market is its own Type (confirmed by its own pass). |
| Event Ticketing Platform | adjacent | Inventory unit is performances/seats for one-off events; FEC inventory is play value, activity capacity, and party resources on an ongoing venue. |
| Event Registration Platform | adjacent | Roster/intake-centric (who is coming); FEC Management is venue-revenue-centric (what they play, spend, and party). |
| Restaurant POS | adjacent | F&B is one revenue center of the FEC, not the whole; FEC POS rings admissions/play/retail/prizes alongside F&B. |
| Theme Park Management | adjacent, complementary | Park physical operations (ride availability, queue, maintenance) vs the venue's commercial operations; a large FEC/park runs both. |
| Gym Management / Climbing Gym Management | adjacent (membership-business cousin) | Membership-dues + check-in business core; FEC is walk-in play economy + parties + prizes, with memberships as one stream among several. |
| Retail POS | underlying capability | Retail is one revenue center; without play semantics and activity access, it is just retail. |

Taxonomy observation (for STATUS Boundary Issues): the Attraction Management System pass (2026-09-06) flagged FEC Management as a probable "segment posture" of the admission-business Type. This pass **refines** that flag: FEC Management is documented as its own Type with a distinct defining core (chargeable play catalog + validated play entitlements + whole-venue transaction unification), while sharing the admission-business DNA with AMS. The two Types are best understood as siblings with different centers of gravity, not parent/variant. Vendor overlap is real (multi-segment platforms) but does not collapse the boundary: the segment postures change which structures dominate (parties + play value + prizes for FEC; timed admission + capacity + passes for attractions).

## Uncertainties

- Embed, Semnox, CenterEdge, Clubspeed operational documentation was not reachable (login-gated help centres or none public). All non-ROLLER observations are product-page level; no precise operational specifics asserted for those products.
- Prize/redemption machinery in ROLLER and Clubspeed was not found in reachable sources — likely delegated to integrated card systems (ROLLER documents provider integrations) or simply undocumented; absence of evidence, not evidence of absence.
- Bowling lane/league management machinery not directly evidenced in any sampled product's reachable docs; bowling appears only as an industry label.
- Deferred-revenue accounting documented explicitly in only 2 of 5 products; likely common in mature deployments but not generalized here.
- "One cashless provider per venue" is a ROLLER-documented rule; unknown whether other platforms impose the same constraint.
- Party machinery depth varies widely (Embed ships it as a Pro add-on; ROLLER/CenterEdge treat it as flagship); the minimal party capability set is not precisely bounded by evidence.
- Exact capacity mechanics differ per product (resource-based, session-based, timed-attraction); no numeric limits asserted anywhere.

## Final Synthesis

FEC Management is the operator-side whole-venue management system for a multi-activity entertainment center. Its defining core is small: the venue's play is a configured chargeable catalog; guests carry system-issued play entitlements (value or rights on a credential or booking) that the system validates when they play; and one transaction system spans the venue's revenue centers — admissions, play, food & beverage, retail, prizes. Around that core, mature products add a stable ring: the play-value card economy (cash/time/activities on cards and wristbands, kiosks, balance-as-payment, balance merge), party and group-event operations (packages, party rooms, itineraries, deposits, run sheets), prize redemption (winner accounts, ticket tallying, prize inventory), passes and memberships, digital waivers, F&B and retail with unified inventory, guest CRM and loyalty, pricing rules, reporting with revenue centers and GL codes, and multi-location management. Segment postures (arcade, trampoline, karting, bowling, eatertainment, soft play) change which ring capabilities dominate — race timing and kart fleets for karting; sessions and waivers for trampoline parks; prizes and game management for arcades; dining for eatertainment — but the defining core and the capability ring stay the same. The sharpest boundary is with Attraction Management System: the sibling Type centers dated admission to a place and entry validation as the attendance record, while FEC Management centers the venue's internal play economy and its party business; the two share vendors and the admission slice, and several products serve both postures from one platform.
