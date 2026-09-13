# Research Notes — Short-term Rental Management

Research date: 2026-09-09
Methodology: v1.1 (update-v1/)

## Research Goal

Understand the operator-side software for managing short-term rental (STR) / vacation rental portfolios: what its system of record is, how bookings enter, how stays are operated, and how money flows to owners. Produce a vendor-neutral canonical model and hold the boundary against three pre-flagged neighbors (hotel PMS §26, vacation rental marketplace §26, residential property management §17).

## Initial Boundary

Hypothesis at start:

- This is the **operator-facing back office** for short-term/vacation rentals — distinct from the demand-side marketplace (Airbnb/Vrbo class) already documented as `vacation-rental-marketplace` (§26, 2026-09-09).
- Likely core: unit portfolio + transient stay reservations + channel sync + guest comms + turnovers + owner economics.
- Nearest neighbors: Vacation Rental Marketplace (demand side), Hotel PMS (property-centric nightly-stay operation), Residential Property Management (periodic tenancies), Hostel/Campground management (niche lodging ops).

Pre-hung flags this pass must discharge:

1. hotel-property-management-system-pms (§26, 2026-09-08): "sampled PMS products serve vacation rentals/STRs directly... candidate seam = property-centric nightly-stay operation vs distributed owner-portfolio management with owner-settlement machinery."
2. residential-property-management (§17, 2026-09-09): "transient nightly stays vs periodic tenancies; Rent Manager lists Vacation Homes as a separate industry."
3. vacation-rental-marketplace (§26, 2026-09-09): "demand-side venue + host storefront here vs operator-side unit-portfolio system of record there (owner settlements, cleaning/access ops, direct-booking sites)."

## Research Questions

1. What is the system's primary record — listing, unit, reservation, guest, or owner?
2. How do reservations enter (OTA channels, direct booking, manual) and how is the calendar kept consistent across sources (double-booking prevention)?
3. What operational loops convert a reservation into a completed stay (messaging, turnovers/cleaning, check-in/access)?
4. How does money work: guest payments, and — at the management tier — owner statements/payouts? Where does trust/escrow accounting appear?
5. Who are the users, and how do the roles differ between a large PM company, a small host, a co-host, and the owner (read-only audience)?
6. Where exactly is the seam vs hotel PMS, vacation-rental marketplace, and residential PM?
7. Historical check: would pre-OTA / paper-era vacation rental agency practice still satisfy the minimal core?

## Representative Products

Selection: market representativeness + documentation depth + different philosophies + different customer tiers.

| Product | Posture | Tier |
|---|---|---|
| Guesty | "All-in-one AI powered vacation rental software"; PMS-suite for growth operators; Lite (1–3 listings) → Pro (4–199) → Enterprise (200+) | host → enterprise PMC |
| Hostaway | "AI vacation rental software" for vacation rental managers; channel-manager-first all-in-one | growing PMCs |
| OwnerRez | Power-user back office; ©2009 (pre-OTA-mainstream founding); per-property pricing "small homeowners and large PMs alike" | self-hosters → PMs |
| Lodgify | Direct-booking-centric ("Your website. Your rules. Zero commission") + channel sync; since 2012 | hosts & PMs, 180+ countries |
| Hospitable | Automation-first ("Simple at one door. Simple at one hundred"); personas Owner/Host/Co-Host/PM/Enterprise | small hosts → PMs (220+ properties) |

## Sources

Fetched 2026-09-09 (Layer A unless noted):

- Guesty — https://www.guesty.com/ (root, feature matrix, FAQ); https://help.guesty.com/hc/en-gb (Help Center home + category map incl. Owners category); Owners category https://help.guesty.com/hc/en-gb/categories/9982898635933-Owners
- Hostaway — https://www.hostaway.com/ (root; full-page capture parsed from saved output; feature groups incl. Owner Statements/Owner Portal/QuickBooks)
- OwnerRez — https://www.ownerrez.com/ (root); https://www.ownerrez.com/property-management (PM module page); https://www.ownerrez.com/support/articles/property-management-overview (support hub w/ full article-tree sidebar)
- Lodgify — https://www.lodgify.com/ (root, feature map, encyclopedia/academy links)
- Hospitable — https://www.hospitable.com/ (root); https://help.hospitable.com/en/ (Help Center collections); https://www.hospitable.com/personas/property-managers (PM persona page)
- Prior-pass context (read, not fetched): STATUS.md entries for hotel-property-management-system-pms, vacation-rental-marketplace, residential-property-management; research/hotel-property-management-system-pms.md §neighbors; research/vacation-rental-marketplace.md forward note.

Source-access limitations:

- Lodgify help center / owner-statements deep page: https://www.lodgify.com/owner-statements/ timed out ×1 — abandoned per network rule. Lodgify owner-statement mechanics are therefore NOT asserted; only the feature's existence (root-page naming) is used.
- Hostaway help center (Intercom) not fetched; Hostaway evidence is root-page Tier 2 only — kept at feature-name strength.
- No precise numeric claims (fees, payout windows, channel counts, plan limits) are carried from any single vendor into the final document except as explicitly quoted vendor self-description (e.g., tier banding).

## Product Observations

### Guesty (A)

- Self-description: "all-in-one AI powered vacation rental software designed for short-term rental hosts and property managers growing their portfolio, from a single listing to hundreds across multiple markets"; nav includes "Your first PMS" and a hotel-PMS solutions page (adjacency drift noted).
- **Multi-Calendar**: "Manage reservations from multiple channels within a single calendar"; testimonial: zero double bookings "ties directly to the Multi-Calendar"; "automated calendar rules prevents all of that" (combined units).
- **Channel Manager**: "Connect to Airbnb, Vrbo, Booking.com & 60+ booking channels"; FAQ: "All connections are direct API integrations — not iCal feeds — meaning availability and pricing update across every channel in real time"; "Sync your properties in real-time... Eliminate double bookings".
- **Unified Inbox** ("Bring every guest conversation together"); automation tools ("Automated end-to-end guest journey"); **Task Management** ("Organize cleaning, maintenance, and other tasks"); LocksManager (smart locks).
- **Financials**: Payment Solutions (Guesty Pay), Revenue management / dynamic pricing (PriceOptimizer), **Trust Accounting** ("Compliant vacation rental trust accounting"), reporting/analytics, bank-reconciliation AI.
- **Owners Management** (owners portal) as a first-class module; Help Center has an **Owners** category (Owners by Guesty App / Owner management / Owners Portal); article "Managing automated messages for guests, owners and team members" — automations target three audiences.
- Websites ("branded direct booking websites"), Direct Reservations, CRM, Guest App (guest portal + check-in forms), Damage protection, GuestVerify, Reviews management, Multi-Unit Management, Open API, Mobile App.
- Tiering by listing count: Lite 1–3 (from $9/mo), Pro 4–199, Enterprise 200+. Accommodation types marketed: vacation rentals, B&B/guesthouse, outdoor stays, urban rentals, aparthotel, serviced apartments.

### Hostaway (A — root page only)

- "AI vacation rental software... combining advanced AI, the industry's most reliable channel manager"; positioned around "vacation rental managers" / "vacation rental property managers".
- Channel Manager: "Reliable Direct API Connection, Airbnb, Vrbo, Booking.com, Google, Expedia, **Multi-Calendar**".
- Unified Inbox: "AI Replies, Automated Messages, WhatsApp, SMS, Email, Guest Portal, Upsells".
- Automation Tools: "Automated Messaging, Reviews, Tasks, Payments, Pricing, Smart Locks, **Owner Statements**".
- **Owner Statements**: "Professional Templates, **Owner Portal**, **Automated Delivery**, Bulk Actions, CoHost".
- Analytics: "Rental Activity, Occupancy, Financial Reports, Owner Statements, Owner Portal, QuickBooks".
- Direct Bookings: website builder + booking engine; Dynamic Pricing; Mobile App, Open API, User Permissions, User Management; "300+ integrations".

### OwnerRez (A)

- Root: "Vacation Rental Software for Property Managers... covers small homeowners and large PMs alike"; © 2009–2026. Feature set: Channel Management, Messaging, Websites, Accounting, Payment Processing, **Property Management (PM)**, CRM, Reporting, Rental Agreements, Automation.
- **PM module** (dedicated page): "Do you manage vacation rentals on behalf of other property owners?... charge a monthly commission"; "calculate commission and generate monthly statements for your owners... built directly into the booking system"; "follows the trust/escrow accounting model where it is assumed that you are collecting payments from guests as 'rents in trust' in a separate escrow bank account. We then provide 'payouts' statements, for both the owner and the vacation rental property manager (you!), ensuring that money is moved from escrow to the rightful party at periodic times"; expenses w/ receipts & reimbursement; **Portal Access** for owners, cleaners, maintenance staff, VRMs — separate logins, scoped to one or more properties, can view calendars, block off time, view owner statements.
- Support-wiki article tree = the object model: Bookings/Quotes/Inquiries (Instant Book vs Request-to-Book, pending bookings, blocking-off time, cancel/refund, extend, change charges, manual bookings, **moving a booking to a different property**, **mid to long term stays**, **owner bookings**, open rescheduling, **housekeeping scheduling**); payments (manual/split/scheduled); deposits; discounts (gap night, length-of-stay, early-bird, last-minute, promo); surcharges (cleaning, pet, extra guest, linen); taxes; rental agreements; security deposits (holds, refundable damage deposits); guest records + guest forms ("My Stay" guest portal, confirm & pay, security-deposit authorization, travel insurance); properties (add/disable/**snooze**, combined/lockoff properties, listing content: photos/amenities/rooms/descriptions/guest instructions, channel rules); rates (seasons/holidays, nightly rules, import/export); rules (min nights, lead time, check-in/out, cancellation policies, banned guests, gap management); tasks; team access (branded portal, staff access); reviews (store/respond/push).
- **Channel machinery**: API channel integrations (Airbnb, Vrbo, Booking.com, Google VR, Marriott Homes & Villas, HomeToGo, Hopper, Houfy, ~40 more) + iCal import/export per channel + **Channel Bridge** ("Bringing In Bookings From Channels") + third-party channel-manager support; per-channel rate adjustments, field-mapping quirks articles.
- Messaging: unified inbox; email/SMS/WhatsApp/channel messaging (Airbnb/Vrbo/Booking) with templates + triggers.
- Integrations: QuickBooks (incl. "Owner Payouts" sync article), accounting services (Topkey, VRPlatform, Clearing), dynamic pricing (PriceLabs, Beyond, RateGenie, Wheelhouse...), housekeeping services (Breezeway, Turno, TIDY...), door locks, insurance.

### Lodgify (A — root; deep pages not fetched)

- "Vacation rental software that syncs your calendars, powers direct bookings and automates guest communications. All in one place."; "#1 short-term rental PMS since 2012".
- Channel manager w/ partner-tier framing (Airbnb Preferred+ Software Partner, Vrbo Elite Partner, Booking.com Premier Connectivity Partner, Google API); "All your channels in one calendar. No double bookings... rates, availability and reservations will sync automatically across every channel."
- Direct-booking core: no-code website builder + booking engine + Lodgify Payments ("Your website. Your rules. Zero commission").
- Operations: unified inbox (AI), guest mobile app, guest management, task management ("Streamline your messages, turnovers and check-ins. Coordinate your team without group chats or spreadsheets"), AI co-host, automation, smart locks.
- **Owner statements** named as a feature (mechanics unverified — fetch timed out). Guest registration; damage protection by Safely; dynamic pricing integrations (PriceLabs, Beyond); integrations for cleaning coordination (Turno, Breezeway), guest experience (Enso Connect, Touch Stay), accounting (Clearing, VRPlatform).
- Audiences: Hosts and Property Managers; hosts in 180+ countries; solutions pages per property type (villa, cabin, serviced apartment, holiday home).

### Hospitable (A)

- "Simple at one door. Simple at one hundred... run your short-term rentals on autopilot"; 24,000+ hosts; personas: Owner / Host / Co-Host / **Property Manager** / Enterprise.
- Channel connections collection ("Connecting Airbnb, Vrbo and Booking.com to Hospitable", 40 articles); "Live calendar sync keeps all your listings, cleaners, and reviews safe across Airbnb, Vrbo, Booking.com, and your direct booking site."
- AI messaging core ("55,000+ AI-crafted replies sent every day"); unified inbox; reviews automation; Copilot (plain-language business Q&A over revenue/occupancy data).
- Tasks: "Automate cleaner and maintenance tasks, and pay them too"; PM page: "Turn bookings into automatic task schedules."
- Dynamic pricing built-in ("no additional software needed"); Direct Booking (own channel; 79 help articles); Smart Home Devices collection.
- **PM tier**: "Automated owner payments: Create clear, branded reports and invoices in just a few clicks. **Split revenue, track expenses, and pay owners directly through Hospitable with automated payouts**"; "owner dashboards and automated statements"; PM Marketplace ("Connect with property owners who are looking for professional management"); role-based permissions ("owners, cleaners, and team members access only to the information they need"); branding (owner portals, emails, direct site).
- Help Center collections include **Payments & Payouts** (72 articles) and **Operations** ("from day-to-day task management to accounting and owner relations"); QuickBooks integration; Rental Agreements, Security Deposits, Guest Vetting; upsells, trip insurance.

## Cross-product Comparison

| Structure | Guesty | Hostaway | OwnerRez | Lodgify | Hospitable |
|---|---|---|---|---|---|
| Unit portfolio w/ per-unit calendar | Multi-Calendar | Multi-Calendar | Properties + calendars | Unified calendar | Properties + calendar sync |
| Reservations from OTA channels + direct + manual | ✓ (60+ channels, direct API, Direct Reservations) | ✓ (direct API, direct engine) | ✓ (API + iCal + Channel Bridge + manual) | ✓ (API + booking engine) | ✓ (channels + direct) |
| Double-booking prevention as explicit concern | ✓ (headline; calendar rules) | ✓ (headline) | ✓ (channel-bridge/mapping docs) | ✓ (headline) | ✓ ("No double bookings. No manual changes") |
| Unified guest inbox across channels | ✓ | ✓ | ✓ | ✓ | ✓ |
| Turnover/cleaning tasks keyed to bookings | ✓ | ✓ | ✓ (housekeeping scheduling) | ✓ | ✓ (bookings→task schedules; cleaner pay) |
| Guest payment processing | ✓ | ✓ | ✓ | ✓ | ✓ |
| Owner statements / portal / payouts | ✓ (Owners portal module) | ✓ (templates, portal, automated delivery) | ✓ (commission, monthly statements, payouts, portal) | ✓ (feature named; mechanics unverified) | ✓ (automated payouts, dashboards) |
| Direct-booking website | ✓ | ✓ | ✓ | ✓ (center of gravity) | ✓ |
| Dynamic pricing (built-in or integrated) | built-in | built-in | integrated | integrated | built-in |
| Accounting export/integration | ✓ (+ trust accounting) | ✓ (QuickBooks) | ✓ (QuickBooks incl. owner payouts) | ✓ (integrations) | ✓ (QuickBooks) |
| Trust/escrow accounting | ✓ explicit | not observed | ✓ explicit (rents-in-trust model) | not observed | not observed |
| Rental agreements / deposits / guest vetting | ✓ | not observed at root | ✓ deep | ✓ (guest registration, damage protection) | ✓ |
| Smart locks / access | ✓ | ✓ | via integrations | ✓ | ✓ |
| Self-describes with PMS vocabulary | ✓ | ✓ (testimonials) | ✓ (root page: "vacation rental management platform"; support pages reference PMS in reviews) | ✓ ("#1 short-term rental PMS") | ✓ (customer quote: "a PMS like you guys") |

Reading: the first five rows are universal in the sample → definitional candidates. Owner economics appears in all five but is tier-dependent (see L1/L2). Trust accounting, vetting/deposits, locks are common-but-partial → optional.

## Canonical Model (Layered)

### L0 — Defining Invariant (jointly-held; minimal)

1. **The rental-unit portfolio as the operator's inventory of record.** A persistent registry of individually identified accommodation units — entire homes, apartments, cabins, rooms — under one operator's management, each carrying its own availability calendar, listing content, and rates. Units are privately-held dwellings (not a property-operated room block); ownership may sit with third-party owners or the operator. Remove → a single-property lodging system (hotel-PMS territory) or a bare unit register.
2. **The transient stay reservation as the central transaction of record.** Date-range × unit × guest bookings with per-stay pricing/terms, held on the unit's calendar, entering from multiple sources — OTA booking channels, the operator's own direct channel, manual entry — and kept consistent across those sources (the double-booking problem is the stated reason the calendar is the hub). Multi-channel API distribution is the dominant modern realization, not the definition; a reservation entering by any means and occupying unit-nights is the invariant. Remove → an operations tool with nothing booked, or a channel-sync utility with no operator record.
3. **The stay-operations loop that converts reservations into completed stays.** Guest communication (unified across the channels the booking came from), turnover/cleaning scheduling between stays, and arrival/access logistics — organized around the reservation calendar and delegated to cleaners/team members through tasks and scoped access. Remove → booking/calendar machinery with no operating loop (channel manager / booking-engine territory).

Jointly-held load-bearing: 1 alone = unit inventory; 2 alone = channel manager/calendar sync; 3 alone = cleaning/messaging utilities; 1+2 without 3 = calendar + sync machinery, no operations; 1+3 without 2 = operations over bookings that never arrive; 2+3 without 1 = guest comms over no managed inventory.

### L1 — Common Mature Structure (standard in the modern market, not definitional)

- Channel-manager machinery (API or iCal two-way sync, per-channel rate/fee adjustments, mapping of listing identities).
- Direct-booking channel: website builder + booking engine + payment processing under the operator's brand.
- Owner statements/portal/payouts at the management tier (see L2 note on tier dependence).
- Unified inbox + templated/automated guest messaging (email, SMS, WhatsApp, channel-native threads).
- Turnover/cleaning task generation from bookings, cleaner assignment, cleaner payout (some products).
- Rate management: seasons, nightly rules, minimum nights, lead time, gap handling; dynamic pricing built-in or via integration.
- Guest payment processing: scheduled/split payments, deposits, surcharges/fees (cleaning, pet, extra-guest), taxes.
- Guest-facing surfaces: portal/app, check-in forms/instructions, self check-in, guidebooks.
- Reporting/analytics: occupancy, revenue, per-unit performance; QuickBooks/accounting integrations.
- Reviews management (collection + response, some cross-channel pushing).
- Team access / role-based permissions incl. scoped portal logins for owners, cleaners, staff.

### L2 — Variant / Optional Structure (segment, geography, regime, business-model dependent)

- Owner-economics depth: simple payouts (small-host tier) → commission calculation + monthly statements + escrow/trust accounting + owner expense reimbursement (PM-company tier). Trust/escrow accounting is a regulatory/regime variant observed explicitly at two of five products.
- Property-type breadth: whole homes; rooms-in-homes; B&B/guesthouse; aparthotel/serviced apartments; outdoor stays (glamping/campground adjacency).
- Mid/long-term stays (monthly/snowbird) handled as bookings with adjusted rules rather than tenancies.
- Damage protection/waivers, travel insurance, guest screening/verification, rental agreements, security-deposit holds.
- Smart-lock/access integration and noise/occupancy sensors.
- Multi-unit / lockoff / combined-listing structures.
- Co-host and marketplace postures (platforms brokering owner→PM relationships).
- Historical realization: pre-OTA-era agency practice (owner contract + printed calendar + reservation diary + guest register + commission statement + cleaner schedule) satisfies the L0 core with none of the modern machinery — historical check passed at class level (OwnerRez ©2009 and Lodgify "since 2012" are vendor-declared pre-mainstream-OTA anchors).

### L3 — Vendor-specific (kept out of the final document)

- Guesty: tier names (Lite/Pro/Enterprise), "AI agents" suite, Guesty Pay/PriceOptimizer/Shield branding, bank-reconciliation AI.
- Hostaway: "AI CoHost", 300+ integrations claim, owner-statement bulk actions specifics.
- OwnerRez: Channel Bridge mechanics, "rents in trust" vocabulary, Quality Center, Rezzy AI, per-property pricing.
- Lodgify: partner-tier badges, Lodgify Payments/Capital, Safely damage protection bundle.
- Hospitable: Copilot, Smarty, cleaner-pay built-in, PM Marketplace matching, customer-funded story.

## Rejected Findings

- "STR management = channel manager + pricing" — rejected: channel sync and pricing are realizations/attachments; sample products without built-in pricing and iCal-only sync still belong to the Type.
- "Owner payouts are definitional" — rejected: the Host persona pole (self-managing owner, Hospitable/OwnerRez small-host posture; Guesty Lite) runs the full core without owner settlement machinery. Owner economics is the PM-tier's marker capability (L1/L2), not the Type's floor.
- "Multi-channel API distribution is definitional" — rejected per anti-overfitting rule: iCal-era and pre-OTA realizations satisfy the Type; the invariant is multi-source reservations reconciled on one unit calendar, channels being the dominant source today.
- "STR management is just residential PM for short stays" — rejected: no lease/tenancy-of-record, no leasing pipeline, no periodic rent cycle; per-night pricing, cleaning fees, min-nights and channel calendars are structurally different objects (see Boundary Findings).
- "This is the same Type as vacation-rental marketplace" — rejected: different record ownership (venue's market transaction vs operator's system of record); the marketplace pass itself recorded the seam.

## Boundary Findings

1. **vs Vacation Rental Marketplace (§26, discharged)** — keep-both RATIFIED. Marketplace = demand-side venue: host-published listings, traveler search, platform-executed booking transaction; its record is the market transaction and the listing storefront. STR management = operator-side system of record: the operator's portfolio truth (calendars, reservations, guests, turnovers, owner money), aggregating demand from marketplaces and the operator's own channel. Removal tests both directions: strip the operator's internal operating record (turnovers, comms, owner settlement, portfolio truth) and what remains is the marketplace's storefront+venue; strip the two-sided venue + traveler-side transaction and what remains is this Type. The operator's direct-booking site is this Type's own demand channel, not a marketplace.
2. **vs Hotel Property Management System (§26, discharged as joint review)** — keep-both RATIFIED with refinement. Candidate seam accepted (property-centric nightly-stay operation vs distributed owner-portfolio management) and refined from this side: the discriminator is (a) inventory character — scattered privately-held dwellings each with its own OTA listing identity and calendar vs one property's operated room pool; (b) no front-desk/folio-centered stay operation — STR operation centers on the reservation→turnover loop with remote/self arrival logistics; (c) owner-settlement machinery present at the management tier (absent in hotel PMS semantics). Refinement caveat: owner settlement is NOT definitional (small-host pole), so the seam rests on inventory character + operation shape, with owner economics as corroborating tier evidence. Adjacency drift noted: sampled STR suites market aparthotel/B&B/hotel-PMS pages, and the PMS pass recorded PMS products serving vacation rentals — the market straddles deliberately; both Types stand.
3. **vs Residential Property Management (§17 sibling, discharged)** — keep-both RATIFIED. RPM's record is the periodic tenancy (lease terms, monthly rent, application/screening pipeline, move-in/out); this Type's record is the transient nightly stay (per-night pricing, cleaning fees, min-nights rules, channel-synced calendars, guest vetting per stay). Overlap zone documented: OwnerRez handles "mid to long term stays" as bookings with adjusted rules — still reservations, not tenancies. The market separates them (residential-PM pass: Rent Manager lists Vacation Homes as a separate industry; Guesty/Hostaway/OwnerRez self-label vacation rental, not property management broadly).
4. **vs Hotel Channel Manager / booking-engine component slices** — the channel manager is a component of this Type's L1, not a rival Type in the directory; standalone channel managers exist but were not needed as directory nodes.
5. **vs Campground/RV Park Management, Hostel Management** — niche lodging operations with space/bed-grain inventory; adjacent, no further analysis required this pass.

## Uncertainties

- Lodgify owner-statement mechanics unverified (fetch timeout) — only feature existence asserted.
- Hostaway evidence is root-page Tier 2; operational depth (e.g., how owner statements are generated) not verified.
- Trust-accounting spread: explicitly observed at 2/5; whether other vendors carry equivalent capability under different names was not established.
- Historical check is class-level reasoning (paper-era agency practice) plus two vendor-declared founding dates; no legacy product's own documentation was fetched (Escapia/LiveRez class not sampled).
- Numeric facts (channel counts, listing-count tier bands, pricing) are vendor self-descriptions quoted as such; no cross-verification attempted, none carried into the final document as industry-wide claims.

## Final Synthesis

The Short-term Rental Management Application is the operator-side system of record for running a portfolio of short-term rental accommodations. Its defining core is three jointly-held structures: the rental-unit portfolio as managed inventory of record (individually identified privately-held units, each with its own calendar, listing content, and rates); the transient nightly-stay reservation as the central transaction of record (multi-source bookings reconciled on the unit calendar, with channel synchronization the dominant modern realization); and the stay-operations loop (unified guest communication, turnover/cleaning between stays, arrival/access logistics) that converts reservations into completed stays. Around that core, mature products add channel-manager machinery, direct-booking channels, rate/pricing tools, guest-payment processing, and — at the property-management tier — owner statements, portals, and payouts, with trust/escrow accounting as a regime variant. The Type holds its boundary against the vacation-rental marketplace (demand-side venue vs operator-side record), the hotel PMS (property-operated room pool vs distributed privately-held unit portfolio), and residential property management (periodic tenancies vs transient nightly stays).
