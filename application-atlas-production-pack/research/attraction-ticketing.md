# Research Notes — Attraction Ticketing

Research date: 2026-09-06
Slug: `attraction-ticketing`
Directory position: Section 26 Travel, Hospitality, Food Service & Events (siblings: Attraction Management System, Theme Park Management, Family Entertainment Center Management, Zoo / Aquarium Visitor Operations, Museum Visitor Experience Platform, Cashless Venue Platform, Digital Waiver Management; nearby: Event Ticketing Platform, Ticket Inventory Management, Ticket Resale Marketplace, Tour & Activity Marketplace, Tour Operator Management System)

Predecessor context: the sibling leaf `attraction-management-system` was processed the same day and flagged this cluster in STATUS Boundary Issues — its hypothesis was that Attraction Ticketing is the "sell+validate slice" of the same underlying admission-business Type. This pass was run to confirm slice-vs-variant-vs-independent-Type status with direct evidence from products marketed under the "attraction ticketing" name.

---

## Research Goal

Understand what the market actually sells under the name "attraction ticketing": the operator-side software for selling admission to visitor attractions and controlling entry. Determine its defining core, its standard mature capabilities, its product philosophies, and — the central question — its structural relationship to the Attraction Management System Type researched the same day.

## Initial Boundary (pre-research hypothesis)

- Core use: sell tickets to a physical attraction (theme park, zoo, aquarium, museum, observation deck, heritage site, seasonal event) online and on-site, issue barcoded/electronic tickets, and validate them at entry.
- Primary users: attraction operator staff (ticketing/box office, gate staff, marketing, management) plus guests acting self-service; resellers/OTAs as connected distribution partners.
- Nearest neighbors: Attraction Management System (whole admission business), Event Ticketing Platform (performances/seats), Tour Operator Management System (departures/itineraries), Tour & Activity Marketplace (consumer-side distribution), Ticket Resale Marketplace (secondary market).
- Central unknown: do "attraction ticketing" products implement a structurally narrower system (pure sell+validate) than attraction management systems, or are they the same system under a ticketing-centric name?

## Research Questions

1. What objects exist (products/tickets, orders/bookings, entitlements, vouchers, customers, resources, capacity)?
2. How is admission inventory defined and bounded (availability, time slots, seasons, closures, capacity)?
3. Which sales channels exist (own web checkout/ticket shop, on-site POS, kiosks, back office, resellers/OTAs)?
4. How does the sale→ticket→validation chain work (voucher vs ticket, scanning, turnstiles, challenges, two-stage redemption)?
5. How does reseller/OTA distribution work (API standards, reseller vouchers, commissions, credit, invoices)?
6. Which commercial machinery surrounds the ticket (promotions, gift cards, deposits, ledgers, tax)?
7. Do ticketing-branded products carry management breadth (memberships, waivers, donations, merchandise, reporting, roles)?
8. What roles and governance exist (users, roles, sellers, shifts, cash reconciliation)?
9. Where are the boundaries: Event Ticketing (seats), Tour Operator (departures), Marketplace (consumer side), E-commerce (no admission semantics)?
10. Is "Attraction Ticketing" an independent Type, a slice, a variant, or an alias of Attraction Management System?

## Representative Products

| Product | Segment focus | Customer tier | Product philosophy | Evidence level |
|---|---|---|---|---|
| Ventrata | Attractions, observation decks, museums/heritage, hop-on hop-off, sightseeing tours | Mid–enterprise, global | Ticketing + distribution platform: API-first connectivity (OCTO), reseller network, own POS terminals | A (deep Intercom help center + glossary, Tier 1) |
| Regiondo | Tours, activities, attractions (amusement parks, zoos, museums, escape rooms), DMOs — Europe | SMB–mid | All-in-one booking system + own ticket shop + OTA distribution + mobile POS + validation | A (Zendesk help center, Tier 1) + Tier 2 product pages |
| Bookingkit | Attractions: amusement parks, museums, zoos, sights, DMOs — Europe | Mid–enterprise | Ticketing/orchestration hub over existing third-party POS & turnstile systems + channel management | B (product pages, Tier 2) |
| DigiTickets | UK visitor attractions: theme parks, zoos, museums, historic houses, heritage railways, seasonal events | SMB–mid, UK | Attraction-first full stack: ticketing + EPOS + kiosks + channel management + staff scheduling | B (product pages, Tier 2; support site unreachable) |

Selection rationale: all four market themselves under the "attraction ticketing / ticketing for attractions" banner; they span geographies (UK / Europe / global), customer tiers (SMB to enterprise), and four distinct philosophies (full stack, distribution-first, booking-system+marketplace, orchestration hub). Tiqets was sampled as the consumer-marketplace boundary probe but its supplier documentation was unreachable (see Sources).

## Sources

- Ventrata Help Center (Tier 1): https://support.ventrata.com/en/ — home index; Dashboard collection (221 articles); Ventrata Glossary. Fetched 2026-09-06.
- Ventrata product site (Tier 2): https://www.ventrata.com/ — home; features-and-solutions. Fetched 2026-09-06.
- Regiondo Help Center (Tier 1): https://support.regiondo.com/hc/en-us — category index; "Manage Products" category; "Tickets & Barcodes" category. Fetched 2026-09-06.
- Regiondo product site (Tier 2): https://www.regiondo.com/ (pro.regiondo.com) — home. Fetched 2026-09-06.
- Bookingkit product site (Tier 2): https://bookingkit.com/ — home (solutions, features, industries, POS partners, customers). Fetched 2026-09-06.
- DigiTickets product site (Tier 2): https://www.digitickets.co.uk/ — home; "Ticketing Solutions" page. Fetched 2026-09-06.
- Tiqets supplier help center (boundary probe): https://suppliers.tiqets.com/ — returned JS shell only; https://www.tiqets.com/en/business/ returned 404. Abandoned after 2 attempts.

Source-access limitations:
- DigiTickets support site (support.digitickets.co.uk) timed out twice — abandoned; DigiTickets claims held at product-page strength.
- Tiqets supplier documentation unreachable (JS-rendered shell; one 404) — abandoned; the marketplace boundary is established structurally (via Ventrata's documented reseller-connection model) rather than by direct observation of Tiqets.
- Bookingkit evidence is product-page level; no operational help-center articles were fetched. No precise operational mechanics asserted for Bookingkit.

---

## Product Observations

### Ventrata (evidence layer A — directly observed in official help center)

Positioning: "Booking & Ticketing system for tour operators & attractions". Markets: hop-on hop-off, sightseeing tours, observation decks, attractions & leisure, museums/cultural/heritage. Claims dynamic pricing, multi-channel booking, hardware (POS, kiosk, turnstiles), 24/7 support; OCTO API founding member; 120+ reseller connections (Viator, GetYourGuide, Expedia, Tiqets, Klook, Groupon, CityPASS, Go City, Headout, TUI Musement…), 30+ operator connections (FareHarbor, PeekPro, Merlin, Vivaticket…).

Object hierarchy (Bookings collection): "An order is the top layer of the booking hierarchy in that an order can have multiple bookings, while a booking can contain multiple tickets." Bookings table "houses all of your reservations, item or gift purchases, and keeps record of your customers and resource allocations". Supporting tables: tickets, extra upgrades ("non-booking items… always sold with a booking"), item purchases ("retail items have no travel date, expiry or capacity descriptors"), adjustments (price adjustments), customers, households, gifts (gift cards), resource allocations.

Glossary definitions (Tier 1, quoted):
- **Ticket** — "grants customers one-time entry to an attraction at a particular time".
- **Pass** — "also known as a city pass, grants customers access to multiple attractions within a city for a set period of time… from the first use".
- **Voucher** — "the document — printed, emailed, or digital — that represents an entitlement to a product; redeeming it typically issues the customer a ticket".
- **Reseller Voucher** — "prepaid codes sold by resellers to customers, used to redeem products; when a voucher is redeemed, typically customers receive a ticket in return".
- **Scanning** — "process of validating vouchers, city passes, or tickets".
- **Counters** — "track and limit how many people enter and leave an attraction, especially when using turnstiles or scanners".
- **Challenges** — "verification prompts that appear during ticket redemption to ensure certain conditions, such as age restrictions or validating promotional eligibility, are met before granting entry".
- **Capacity** — "total available seats/spots per resource or attraction".
- **Resources** — "assets or capacities, such as vehicles, guides, seating arrangements, or accommodations, used to manage product availability".
- **Memberships** — "access-based products that offer exclusive benefits—such as hidden tickets or automatic discounts—for a set validity period".
- **Households** — "a way to link all memberships and booking/redemption activity from one household".
- **Ledgers** — "accounting entries automatically created for every booking transaction, used to reconcile revenue against your ERP; each entry is tagged with a Ledger Code".
- **Shifts** — "a seller's tracked working session on a terminal or portal, from login to reconciliation/cash-up".
- **Waivers** — "legal documents that customers must sign to release your operation from liability".
- **Manifests** — "list of bookings/passengers/units for a departure or event".
- Positions: **Supplier** (source of products, dashboard account), **Seller** (staff selling on-site), **Operator** (suppliers operating 3rd-party products via API), **Reseller** (intermediary e.g. OTA earning commission), **Agent** (person employed by reseller).

Channels (glossary): Web Checkout (self-service website, widgets, Manage-My-Booking portal), Backoffice (dashboard), Terminal app, Direct API (OTA connection), Concierge ("sales portal for sellers, agents and operators"), Sales Kiosk. Terminal modes: Attended Sales (ticket office with staff) vs Unattended Sales (self-service kiosk).

Products & availability: products table; availabilities ("dates and times when a product is available for booking"); closures ("close availability for products for select periods"); seasons ("define peak and off-peak times… adjust offering and prices"); rates; stocks ("inventory management for limited products"); items; categories; brands; destinations ("split your operation into several separate ones"); questions (booking-time customer prompts); notices; promotions ("configurable discounts… individual tickets or entire bookings"); combinations (cross-sell) / comparisons (up-sell); tax rates + seasonal tax rates; waitlists ("sign up for a notification when a spot opens on a sold-out date").

Validation machinery: scans table ("information about ticket or voucher scans made by sellers"); counters (turnstile in/out); challenges; two-stage redemption ("for products where attendance needs to be recorded before a ticket is used").

Reseller machinery: bands ("reseller tiers… shared commission or wholesale scheme"), topups ("prepaid amount of credit the reseller must load in advance"), credit limit, batches ("collections of vouchers which can be redeemed by customers"), vouchers table ("a set of allocated barcodes resellers can use to sell your products"), reseller invoices, rewards (concierge points), portals.

Finance: transactions, transfers, disputes, ledgers + ledger codes, payment gateways, payment methods (Adyen cards, Google Pay, Klarna BNPL, terminal card/cash/gift-card, split payments, gratuity), deposits (checkout deposit — pay part online, balance at attraction; hotel deposit — sold at hotel, redeemed on-site), operator invoices.

Operations: calendar (availabilities, bookings, manifests, resource allocations); pickups/dropoffs/routes/dispatches; duties ("sets of identifiers for drivers"); booking emails; templates (voucher/receipt/email); campaigns via Klaviyo/Mailjet/Postmark/Twilio; donations with Gift Aid (UK).

Governance & data: users, roles ("group users with similar responsibilities… each equipped with a set of permissions"); WorkOS SSO admin portal; GDPR customer-data clearing; charts/reports, saved searches, reporting/export API endpoints; PAX / Net PAX / Active PAX metrics.

### Regiondo (evidence layer A for help-center structure; B for positioning)

Positioning: "all-in-one booking software made for tours, activities, and destinations that lets you sell tickets online, manage bookings, and connect with leading OTAs". Industries: tours (boat/bus/city/walking), activities (outdoor, rafting, zipline, cooking, sports, spa), attractions (amusement parks, indoor playgrounds, escape rooms, laser tag & VR, museums & events, zoos & aquariums), destinations (DMOs & DMCs). Feature blocks: payments (multi-currency, cash/card/PayPal), sales reports, website builder, POS ("receive bookings on-site using mobile devices like smartphones and tablets"), distribution ("control all of your sales channels in one place — including your website, social media, OTAs, and resellers"), integrations.

Help-center category map (Tier 1): Getting started / News / Manage Products / Bookings / Settings / Online Sales / Billing / Sales Channels / Calendar / **Tickets & Barcodes** / Customers & Communication / Connectivity / Statistics / **POS** / Website Builder / Regiondo App / Developers / Partner Account.

Manage Products category: offers (create/change), categories, offer bundles, appointments, opening hours, cut-off times, offer-status lifecycle ("Deactivate, Reactivate, Archive, and De-archive"), 2-year availability limit, order options (what customer information is collected), EU right of withdrawal for online bookings (+ withdrawal-form hosting), merchandising (merchandise products, shipping, invoicing), packages, resources ("What are resources?").

Tickets & Barcodes category: ticket customization (logo, pictures, address), day tickets; vouchers (value vouchers, gift certificates, validity changes, redemption); **Validation** ("How to validate tickets and vouchers", "How to control if a ticket is already validated", "For how long am I able to validate tickets"); discount codes (creation, redemption limits, export, on-the-fly via URL parameter).

### Bookingkit (evidence layer B — official product pages)

Positioning: "The One Platform For Attractions" — "Europe's leading attractions use bookingkit to sell more tickets and simplify operations". Customers include Kölner Zoo, Städel Museum, Europa-Park, Movie Park Germany, Kölner Dom, Wilhelma, European Hansemuseum.

Solution blocks:
- **AI-Powered Webshop** (booking generation): conversion-optimized webshop, one-click payments (Apple Pay/Google Pay), AI guest support, "stop losing margins to OTA fees".
- **Channel Management**: "intelligent capacity management", "maximize venue occupancy", "deep connectivity to Google & OTAs", 50+ partner networks; "list once, sell everywhere".
- **Central Ticketing & Operations**: "One platform for ticketing, POS, and entry management"; "Unify your webshop, on-site POS, and entry management into one frictionless flow"; "Ensure all sales channels share the same inventory data, eliminating manual friction and double data entry"; "central intelligent system to manage complex ticket types and inventory".
- **Seamless Integrations**: "Direct POS & turnstile sync"; "Connect bookingkit with Europe's leading point-of-sale and access control systems" — named POS partners Beckerbillett, Megara, HKS, Toucantix, Axess; "No queues, no overbooking. Since all channels share a single source of truth, your availability is perfectly synced across your webshop and on-site ticket counters in real time"; "automated accounting flow"; multi-site management.

Features list: Booking Calendar; B2B Reseller Platform (bookingkit reach); Checkout Widget (ticket shop); NEXT Webshop Widget; Vouchers & Coupons; Resource Management; Analysis & Optimization; Email Automation; Security and Service; AI Sales & Support Agent. Industries include museums ("Pre-purchasing and on-site validation of time-slot tickets made simple"), amusement parks ("Integrate any entry management or turnstile system"), zoos ("keep a constant view on your capacity"), group bookings (Movie Park testimonial: "handling all group bookings via bookingkit… managed centrally").

### DigiTickets (evidence layer B — official product pages; support site unreachable)

Positioning: "Integrated Ticketing, Visitor Management & EPOS Solutions for Attractions, Tours & Events"; "over 1,000 venues across the leisure industry in the UK & beyond". Industries: theme parks, farm parks, historic houses & gardens, Christmas events, Halloween events, seasonal events, heritage railways, museums, distillery & brewery tours, zoos & aquariums, underground attractions, festivals.

Solution lines (navigation): Ticketing; Point of Sale (EPOS); Self Service Kiosks; Staff Scheduling; Payment Services; Web Design & Build; Channel Management.

Ticketing page: "manage your entire ticketing operation, before, during and after the customer visit". Software abilities listed: "Set up tickets, events, and capacities"; "Configure pricing & discounts"; "Add products"; "Set up automated emails"; "Manage, edit, and refund orders"; "View customer information"; "Benefit from a wide array of reports, and much more".

Channel management: OTAs/marketplaces as distribution (case study: cross-channel booking experience for a city-tower attraction; news: Day Out With The Kids integrated as a Marketplace via Experience Bank). Case study evidence of access control + self-service kiosks deployed with the platform (Folly Farm).

---

## Cross-product Comparison

| # | Finding | Ventrata | Regiondo | Bookingkit | DigiTickets | Strength |
|---|---|---|---|---|---|---|
| 1 | Operator-defined admission products (tickets with price variations & validity) | ✓ products/rates | ✓ offers | ✓ "complex ticket types" | ✓ tickets/products/pricing | B — cross-product |
| 2 | Availability & capacity control (time slots, closures, seasons, resources, cut-offs) | ✓ availabilities/closures/seasons/resources/capacity | ✓ appointments/opening hours/cut-offs/resources | ✓ capacity management/booking calendar/resource mgmt | ✓ capacities | B — cross-product |
| 3 | Own online sales surface (web checkout / ticket shop / widget) | ✓ web checkout + CMS | ✓ ticket shop + website builder | ✓ webshop + checkout widget | ✓ online ticketing + web design | B — cross-product |
| 4 | On-site attended POS | ✓ terminal app (attended sales) | ✓ POS (mobile) | ✓ POS (own or partner) | ✓ EPOS | B — cross-product |
| 5 | Self-service kiosk | ✓ kiosk mode | not evidenced (reachable pages) | not evidenced (partner hardware) | ✓ | B (3 of 4) |
| 6 | Recorded order/booking issuing tickets | ✓ order→booking→ticket | ✓ bookings/tickets | ✓ bookings centrally managed | ✓ manage/edit/refund orders | B — cross-product |
| 7 | Entry validation (scan/validate/redeem) | ✓ scanning/scans/counters/challenges/two-stage | ✓ validation section | ✓ entry management/turnstile sync | ✓ access control | B — cross-product |
| 8 | Reseller/OTA distribution | ✓ 120+ connections, OCTO | ✓ distribution channels | ✓ channel mgmt, 50+ networks | ✓ channel management | B — cross-product |
| 9 | Reseller voucher → ticket redemption on-site | ✓ explicit | ✓ voucher redemption | ✓ vouchers & coupons | not evidenced | B (3 of 4) |
| 10 | Promotions / discount codes | ✓ promotions | ✓ discount codes | ✓ vouchers & coupons | ✓ pricing & discounts | B — cross-product |
| 11 | Customer records | ✓ customers table | ✓ customers & communication | not evidenced (page level) | ✓ view customer information | B (3 of 4) |
| 12 | Payments & finance (gateways, gift cards, ledgers) | ✓ deep (ledgers/disputes/deposits) | ✓ payments/billing | ✓ one-click payments/accounting flow | ✓ payment services | B — cross-product |
| 13 | Reporting / statistics | ✓ charts/reports/export API | ✓ statistics | ✓ analysis & optimization | ✓ reports | B — cross-product |
| 14 | Users / roles / permissions | ✓ roles | not evidenced (index level) | not evidenced | not evidenced | A — product-level |
| 15 | Memberships (+ households) | ✓ memberships/households | not evidenced | not evidenced | not evidenced | A — product-level in this sample; standard in the management-branded sibling sample (ROLLER/Tessitura/Altru) |
| 16 | Waivers | ✓ waivers | not evidenced | not evidenced | not evidenced | A — product-level; Optional |
| 17 | Donations / Gift Aid | ✓ | not evidenced | not evidenced | not evidenced | A — product-level (cultural segment) |
| 18 | Merchandise / retail items | ✓ items/stocks/extras | ✓ merchandising | not evidenced | not evidenced | B (2 of 4) |
| 19 | Tour-side machinery (pickups/manifests/routes/duties) | ✓ | ✓ (tours focus) | not evidenced | title only | B (2 of 4) |
| 20 | Website builder / CMS | ✓ CMS | ✓ website builder | ✓ webshop activation | ✓ web design & build | B — cross-product |
| 21 | Orchestration-hub posture over third-party POS/turnstiles | ◐ operator connections | not evidenced | ✓ explicit hub positioning | not evidenced | A — product-level posture |
| 22 | AI sales/support agent | not evidenced | not evidenced | ✓ | not evidenced | Vendor-specific |
| 23 | Staff scheduling module | not evidenced | not evidenced | not evidenced | ✓ | A — product-level |
| 24 | Waitlists for sold-out slots | ✓ | not evidenced | not evidenced | not evidenced | A — product-level |
| 25 | City / multi-attraction passes | ✓ Pass definition | not evidenced | not evidenced | not evidenced | A — product-level |

Legend: ✓ observed; ◐ partially observed; "not evidenced" = not found in reachable sources (absence of evidence, not evidence of absence).

---

## Abstraction Levels

### L0 — Defining Invariant (minimal)

An Attraction Ticketing system is operator-side software for a visitor attraction in which:

1. **Operator-defined admission products** — the attraction defines what it sells: ticket types (typically with price variations such as adult/child), day or time-slot tickets, and passes, each carrying a price and validity rules (which day/time, how long redeemable).
2. **Sale through the system's channels → recorded order → issued tickets** — purchases (own web checkout/ticket shop, on-site counter POS, kiosk, back office, resellers) are recorded as orders/bookings that issue redeemable admission entitlements — barcoded/QR/electronic tickets, or voucher documents redeemed for tickets.
3. **Ticket validation at entry** — issued entitlements are validated (scanned/redeemed/checked) at the attraction's point of entry, and that validation is the system's attendance record.

Historical/market-sample check: a small museum selling open-dated barcoded tickets at a counter and scanning them at the door satisfies all three properties — no timed entry, no memberships, no OTA distribution, no kiosks required. Conversely: remove entry validation and the product collapses into generic e-commerce; remove operator-defined admission products and it is not selling admission; remove issued tickets and there is no admission control at all. The three properties hold.

### L1 — Common Mature Structure

Present across the researched sample; expected in mature modern products but not required for recognition:

- Availability & capacity control: time slots/sessions/availabilities, closures, peak/off-peak seasons, capacity-carrying resources, cut-off times, capacity monitoring; waitlists in one product.
- Multi-channel selling: own web checkout/ticket shop (embedded, widget, white-label, CMS-hosted), attended on-site POS, self-service kiosks, back-office/phone order entry, seller/concierge portals.
- Reseller & OTA distribution: API connectivity to marketplaces (industry standard OCTO in one product), reseller/agent management, commissions and wholesale tiers, prepaid credit/topups, reseller vouchers redeemed on-site for tickets, reseller invoicing.
- Order/booking management: edit, refund, upgrade, reschedule, payment links for balance-due bookings, deposits, tasks/notes.
- Promotions: discount codes (with redemption limits), cross-sell and up-sell attachments, price adjustments.
- Customer records: purchaser database, booking emails/communication, privacy tooling (GDPR clearing in one product).
- Payments & finance: gateways, payment methods (cards, wallets, BNPL, cash, gift cards), split payments, deposits, ledgers/ledger codes for ERP reconciliation, disputes, tax rates (incl. seasonal).
- Validation machinery: scan apps and scan logs, turnstile counters, redemption challenges (age/promotional eligibility), two-stage redemption, validation windows.
- Reporting/statistics: sales, attendance (per-person counts), redemptions, charts/reports, export APIs.
- Staff & governance: users, roles/permissions, sellers, terminals/locations, shifts with cash reconciliation.
- Templates: ticket/voucher designs, receipts, booking emails.

### L2 — Variant / Optional Structure

Depends on segment, geography, deployment, business model:

- Memberships & households (observed in one sampled product; standard in the management-branded sibling sample).
- Digital waivers for risk activities.
- Donations / Gift Aid (cultural segment, UK).
- Merchandise/retail items and stock, shipped or on-site.
- Tour-side machinery: pickups/dropoffs/routes, manifests, driver duties, guides — the tours/activities half of dual-market products.
- City passes / multi-attraction passes (sightseeing-pass market).
- Website builder / CMS and content pages.
- Marketing automation/campaigns via external platforms.
- Orchestration-hub posture: ticketing/channel hub syncing third-party POS and turnstile systems instead of providing its own hardware stack.
- AI sales/support agents.
- Staff scheduling (module in one product).
- Regional compliance: EU right of withdrawal for online bookings, Gift Aid, seasonal tax rates.
- Multi-site / destination / DMO operations (destinations splitting an operation; multi-venue management).

### L3 — Vendor-specific (kept out of the final document)

- Ventrata: OCTO founding membership; Terminal app naming; Supplier/Operator/Reseller/Agent position model; PAX/Net PAX/Active PAX metrics; WorkOS SSO portal; hotel-deposit flow; concierge mode; duties; two-stage redemption as a named feature.
- Regiondo: "offers"/"appointments" terminology; 2-year availability limit; withdrawal-form hosting tooling; Regiondo App; partner-account side.
- Bookingkit: "reach" B2B reseller platform; AI Sales & Support Agent; named POS/access partners (Beckerbillett, Megara, HKS, Toucantix, Axess); Leisure Market Index publication.
- DigiTickets: My DigiTickets backoffice; staff scheduling as a sold module; web design & build service; industry microsites; Day Out With The Kids / Experience Bank marketplace integration.

---

## Boundary Findings

| Neighboring Type | Relationship | Distinction (what to remove/add to flip the Type) |
|---|---|---|
| Attraction Management System | same underlying Type, different emphasis | Both implement the identical defining core (admission products → sale → entitlements → entry validation). Ticketing-branded products center the sell–issue–validate loop and distribution reach; management-branded products extend further into on-site operations breadth (cashless, memberships, donations, patron CRM, education). But the rings overlap: the ticketing-branded sample carries POS, kiosks, memberships, waivers, ledgers, reporting; the management-branded sample carries OTA channel management. Probable Alias — the market uses both names for the same software category. |
| Event Ticketing Platform | adjacent, sharpest structural boundary | Event ticketing's inventory unit is performances and seats (seat maps, one-off events); here it is admission capacity to a place (day/time-slot tickets, no seat map as primary unit). Sampled products serve seasonal events (Christmas/Halloween attractions) but remain admission-shaped. |
| Tour Operator Management System | adjacent, porous in market | Tour systems center itinerary departures (multi-day scope, guides, per-departure capacity); attraction ticketing centers place admission. The sampled products are largely dual-market (tours AND attractions) — Ventrata's manifests/pickups/duties, Regiondo's tour industries — so the boundary is the primary inventory unit of a deployment, not the vendor. |
| Tour & Activity Marketplace / OTA | opposite side of the market | Consumer-facing distribution platforms connect to this Type as resellers (API or voucher allocation); they do not run the operator's admission business. |
| Ticket Resale Marketplace | different object and side | Secondary-market resale of already-issued tickets; this Type issues and validates first-sale entitlements. |
| Ticket Inventory Management | capability slice | The availability/capacity machinery is one capability ring inside this Type, not a standalone product category in the researched market. |
| Cashless Venue Platform | capability slice | Stored-value payment machinery appears as gift cards/wallets inside this Type; the dedicated leaf covers the cashless-payment slice. |
| Digital Waiver Management | capability slice | Waiver capture appears as a gated pre-entry step in (some) products of this Type. |
| E-commerce Platform | underlying capability | The web checkout is one channel; without operator-defined admission products and entry validation it is generic e-commerce. |
| Attraction Management System siblings (Theme Park Management, FEC Management, Zoo/Aquarium Visitor Operations, Museum Visitor Experience Platform) | segment/layer variants of the shared domain | Physical-operations and visitor-experience layers, not the commercial admission layer researched here. |

Taxonomy conclusion (for STATUS Boundary Issues): the predecessor hypothesis ("Attraction Ticketing = the sell+validate slice") is refined by this pass. Products marketed as "attraction ticketing" implement the same defining core as Attraction Management System AND most of its capability ring (POS, kiosks, memberships, waivers, ledgers, reporting, roles). No product family was found that implements only the sell+validate slice as a standalone category. The two directory leaves are best understood as two names for one Type with an emphasis gradient (distribution-reach-first vs on-site-operations-first). Probable Alias; no taxonomy change made unilaterally.

---

## Uncertainties

- DigiTickets operational mechanics (product configuration depth, validation hardware behavior, membership support) — support site unreachable; product-page evidence only. No precise claims made.
- Bookingkit operational mechanics (booking object model, validation flows, reseller voucher mechanics) — product-page evidence only; no help-center articles fetched.
- Regiondo memberships, kiosks, roles: not evidenced in the reachable help-center index; absence of evidence, not evidence of absence.
- Whether memberships are standard in ticketing-branded products: directly observed in one (Ventrata); standard in the management-branded sibling sample; held as common-mature for the underlying Type with an emphasis note.
- Exact capacity mechanics differ per product (resources vs availability slots vs turnstile counters); no numeric limits asserted anywhere.
- Re-entry rules, validity windows, refund windows: product-dependent; not generalized.
- Tiqets supplier-side behavior: unreachable; the marketplace boundary rests on the operator-side reseller-connection evidence.

## Final Synthesis

"Attraction Ticketing" is the market's ticketing-centric name for the operator-side admission system of a visitor attraction. Its defining core is small and identical to that of the Attraction Management System: the operator defines admission products with prices and validity rules; selling them through the system's channels (own web checkout, on-site counters, kiosks, back office, resellers/OTAs) produces recorded orders that issue redeemable entitlements (barcoded/electronic tickets, or vouchers redeemed for tickets); entitlements are validated at entry, and that validation is the attendance record. Around this core, mature products add a stable ring: availability/capacity control, multi-channel selling, reseller/OTA distribution with voucher redemption and commission machinery, promotions, customer records, payments and ledgers, validation machinery (scans, counters, challenges), reporting, and role-governed staff operations. The four sampled products differ mainly in philosophy — attraction-first full stack (DigiTickets), distribution-first platform (Ventrata), booking-system + marketplace posture (Regiondo), orchestration hub over third-party POS/turnstiles (Bookingkit) — and in how far they reach into the management-branded sibling's territory (memberships, waivers, donations, merchandise). The Type's sharpest structural boundary is with Event Ticketing (seat/performance inventory vs admission/capacity inventory); its most consequential taxonomy relationship is the probable alias with Attraction Management System.
