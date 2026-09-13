# Research Notes — Hotel Front Desk Application

Research date: **2026-09-08**
Leaf: Hotel Front Desk Application (DIRECTORY §26 Travel, Hospitality, Food Service & Events)
Slug: hotel-front-desk-application

---

## Research Goal

Understand what a "front desk application" for hotels actually is when derived from real products: what the desk works on, what objects exist, what the working loop is, where the money lives, and how this leaf relates to its very close neighbors — especially Hotel Property Management System (PMS), from which the market's "front desk" language is inseparable.

## Initial Boundary (hypothesis before research)

The directory already contains several lodging leaves processed or pending:

- Hotel Property Management System / PMS (pending)
- Hotel Central Reservation System / CRS, Hotel Booking Engine, Hotel Channel Manager (pending — distribution)
- Hotel Housekeeping Management (pending — room servicing operations)
- Hotel Guest Experience Platform, Digital Concierge (pending — guest-facing)
- Hotel CRM / Loyalty Platform (processed — guest profile + loyalty program)
- Hostel Management System (processed 2026-09-08) — its notes **pre-hung a seam to this leaf**, calling "hotel-front-desk-application + hotel-housekeeping-management" *operational slices* of the operator-side lodging software structure, and recommending joint review when Hotel PMS is processed.

Prior hypothesis: "front desk application" may be (a) a real operational-slice Type (like Kitchen Display System within restaurant ops), (b) a mere alias for small-hotel PMS (much of the market sells "front desk software" that is really a small PMS), or (c) only a module name inside PMS. The pass must decide which and record evidence either way.

## Research Questions

1. What is the desk's unit of work? (Reservation? Guest? Room? Stay?)
2. What is the arrival → departure loop, step by step, as products document it?
3. Where does guest money live? Is a running guest account (folio) definitional?
4. What does the desk see about rooms (occupancy, service status) and what does it do with it?
5. What arrives at the desk from elsewhere (booking engine, channel manager, OTA) and what does the desk itself originate (walk-ins, day-use)?
6. What is handled at the desk but NOT part of it (housekeeping operations, rates/distribution, night audit, marketing)?
7. Do older / regional / platform-native "front office" systems satisfy the same core? (historical check)
8. Is this leaf a defensible Type, an operational slice with two product shapes, or an alias of Hotel PMS?

## Representative Products

Selected for market representation, documentation accessibility, different product philosophies and customer tiers:

| Product | Segment / philosophy | Why sampled |
|---|---|---|
| **Mews** (Mews Operations) | Cloud PMS, mid-market, modern; unusually rich public glossary/concept docs | Tier-1 operational definitions of check-in, check-out, bill≡folio, cashier |
| **WebRezPro** (World Web Technologies) | Cloud PMS sold with a dedicated "Hotel Front Desk Software" feature page; long-established, independents + groups | Desk-featured product framing; detailed desk-loop semantics |
| **Yanolja Cloud Solution (YCS, eZee lineage)** | Cloud "agentic" PMS for small independents; vendor's historical on-premise product was literally named **eZee FrontDesk** (legacy domain now redirects to YCS) | Desk-role framing (front-desk managers as a named audience) + AI-era check-in/self-service |
| **HotelDruid** (DigitalDruid.Net) | Free/open-source property management for B&Bs/vacation rentals up to large hotels | Micro-property / open-source pole; shows the minimal desk+assignment+documents core |

Attempted but not usable as evidence: Oracle OPERA Cloud (release index fetched; user-guide TOC is JS-rendered, full PDF exceeds fetch limits — deep operational pages unreachable), Cloudbeds (product URLs restructured, 404s), Little Hotelier (help-centre locale paths 404). Recorded under Source-access Limitations.

## Sources

Fetched 2026-09-08:

- Mews Open API documentation — Glossary: https://docs.mews.com/getting-started/glossary.md (Tier 1)
- Mews docs — Concepts index: https://docs.mews.com/connector-api/concepts.md (Tier 1)
- Mews docs — Guest Services use case page: https://docs.mews.com/use-cases/business-use-cases/guest-services.md (Tier 1, thin)
- Mews docs — docs index / readme with ask-query: https://docs.mews.com/ (Tier 1; one ask query succeeded, one timed out)
- WebRezPro — "Hotel Front Desk Software": https://www.webrezpro.com/front-desk/ (Tier 2, detailed)
- WebRezPro — "Hospitality Housekeeping Software": https://www.webrezpro.com/housekeeping/ (Tier 2)
- Yanolja Cloud Solution — PMS product page: https://yanoljacloudsolution.com/ (Tier 2 marketing; ezeefrontdesk.com redirects here)
- Yanolja Cloud Solution — "Front Desk Managers" solutions page: https://yanoljacloudsolution.com/solutions/front-desk-managers (Tier 2 marketing)
- HotelDruid — product home / description: https://www.hoteldruid.com/en/ (Tier 2)
- Oracle Hospitality docs index + OPERA Cloud 26.3 Get Started / Books pages: https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.3/ (Tier 2 — index level only)

Not fetched / unreachable (limitations):

- OPERA Cloud User Guide operational chapters (JS TOC; PDF >5 MB fetch limit)
- Cloudbeds help center / product pages (site restructure; 404s)
- Little Hotelier help centre (locale 404s)
- No historical front-office system docs fetched; historical reasoning below uses industry-standard vocabulary that is *additionally corroborated by fetched modern glossary text* (Mews defines Bill ≡ folio, Paymaster including "City Ledger Paymaster", Cashier — the classic front-office accounting vocabulary).

Background context (not fetched, used only for framing, marked C): "front office" is the classic hotel-industry term for the front desk function, historically opposed to "back office" (accounting); legacy front-office systems (e.g., Fidelio, HIS, RoomMaster lineage) centered on the room rack, registration cards, guest ledger/city ledger, cashier and night audit. Modern products' own glossaries preserve this vocabulary (see Mews evidence), which is the fetched corroboration used here.

---

## Product Observations

### Mews (Tier 1 — glossary + concepts; evidence layer A for its own definitions)

Key observations:

- **Check-in** (A): "the process of registering a Customer's arrival at a Property at the beginning of their stay, although this may be performed in advance of their physical arrival on site, using an online check-in process"; the API names this "start reservation" — i.e., the reservation turns into the started stay.
- **Check-out** (A): "the process of registering a Customer's departure from a Property at the end of their Stay … implying that the Bill has been settled and therefore it can be processed and closed."
- **Bill ≡ folio** (A): "A Bill is a financial account for a Customer or Company, synonymous with 'folio'. It can contain a mix of Order items and Payment items. A Bill can be 'open' … or 'closed', i.e. closed to further changes. A closed Bill is assumed to be balanced … and 'settled'."
- **Guest accounting carries classic front-office structure** (A): *Cashier* ("a role for handling payments. Multiple cashiers can be configured for a Property, and Employees allocated against them"), *Paymaster* (compiles charges into a single bill; "City Ledger Paymaster" for companies invoiced for multiple guests' bookings; "Lobby Bar Paymaster" for non-resident customers), *Deposit*, *Preauthorization* (hold to secure the bill).
- **Charges flow to the guest's account from around the property** (A): *Additional Services* are "additional or extra to the main service, and can be purchased on-site and added to a guest's Bill. Examples include room service, airport transfer and spa services." Closed bills remain editable within a configurable *Editable History Window*, then become frozen historical records (A, product-specific window concept).
- **Reservation** (A): "a contract between a Property and a named Customer or agent to set aside a category of Space and/or provide some hospitality Service for a specified period of time … also contain a Price and terms and conditions."
- **Space / Resource** (A): guest rooms are modeled as bookable Spaces; Mews is extending "rooms" toward spaces/resources (SpaceTime project).
- **Front-of-house role context** (A): Departments include "Housekeeping or Front of House"; Employees/Tasks assigned per department. Front-desk staff also handle loyalty membership enrollment/linking for arriving customers (from the ask response — front desk staff as the operating hands of membership mechanics).
- **Scope neighbors** (A): Channel Manager passes ARI (Availability, Rates, Inventory) to channels and receives Reservations — i.e., reservation intake is a separate, explicitly named subsystem feeding the property system; Booking Engine is customer-side.

### WebRezPro (Tier 2 — dedicated "Hotel Front Desk Software" feature page + housekeeping page; layer A for product claims, B when compared)

Key observations (front-desk page):

- The vendor itself frames the market category (A): "From pre check-in to post check-out, WebRezPro hospitality software offers a complete set of **hotel front desk software** features" — the desk spans the whole reservation cycle.
- **Check-in / check-out as the desk's daily shape** (A): "Simply enter the guest's name or confirmation number to retrieve their reservation, or see the list of all arrivals / departures due for the day"; check-in/check-out receipts can be printed in advance (even alphabetically).
- **Paperless / contactless check-in** (A): digital guest agreements completed before arrival, self-check-in instructions auto-sent, completed agreement "automatically attached to the reservation folio"; e-signature capture on mobile devices for registration cards/receipts.
- **The folio is the desk's money object** (A): Folio Splitting ("Split reservation folios at the click of a button for separate invoicing… Incidental charges can be applied to a particular folio … or distributed evenly"); Payments ("Whether by cash, credit card, cheque or debit card, payments, deposits and refunds can all be applied directly through the reservation folio"); Guest Charges (ancillary charges "applied to multiple reservations at once … or from within the guest folio").
- **Posting from around the property** (A): POS Purchases — "During a guest's stay, ancillary charges (like restaurant, gift shop and activity charges) can be applied to reservation folios manually, or automatically through an interface with your POS system"; POS invoices also exist for purchases not attached to a reservation (non-residents, post-check-out).
- **The guest ledger** (A): "Providing a clear view of current balances due, the guest ledger shows all in-house guests and their balances owing, as well as advance payments from future guests and any outstanding invoices" — i.e., the desk's money view is organized by in-house guests and their accounts.
- **Guest profiles auto-created from reservations** (A), used to identify repeat guests; **House Accounts** for non-stay customers buying on account.
- **Day-use / hourly reservations** exist as a front-desk capability (A, optional module).
- **Group handling at the desk** (A): group folios, room blocks, rooming lists, master invoice, "quick and easy group check-in/out".
- **Desk alarm/reminder layer** (A): "alarm calendar … where you'll find all active front desk and maintenance alarms and reminders for the day"; reservation folios carry notes/pop-up reminders; VIP flags.
- Housekeeping page (A): "Integrated with front office, WebRezPro's housekeeping software displays room status and occupancy in real time"; room status vocabulary: *dirty, clean, inspected, in service (housekeeper in room), do-not-disturb*; housekeeping zones, checklists, bulk status updates, maintenance alarms. Housekeeping and Front Desk are **separate named feature areas** of the same product.
- Caveat: portions of the fetched page contain garbled auto-generated text (e.g., an "adjoining/virtual units" and "waitlist" section); only clean sections are used.

### Yanolja Cloud Solution / YCS — eZee lineage (Tier 2 marketing; layer A for product claims, B when compared)

Key observations:

- Lineage note (A, observed via redirect): the legacy product domain ezeefrontdesk.com (the vendor's historically named on-premise "eZee FrontDesk" front-desk system) now redirects to the YCS platform site; support links reference ezeetechnosys infrastructure. The *desk-named product* population is real market history; the current product is a cloud platform.
- Desk role as named audience (A): a dedicated "Front Desk Managers" solutions page — "One platform keeps the front desk moving… every reservation, room assignment, and guest request flows into action."
- Desk loop semantics (A, marketing framing): "Check-ins… AI handles ID verification, payment, and room assignment. Self-service kiosks keep peak arrivals moving"; "Room status, housekeeping, and guest requests unified. Reservations, billing, and room changes stay connected"; digital keys; role-based access "keeps every team focused."
- Stay services and folio (A, FAQ): "Room charges, dining transactions, services, and payments remain connected throughout the stay in a single guest folio"; "Reservations, room assignments, guest profiles, and payments are available from one interface."
- In-stay desk operations (A): "Room moves, stay extensions, day-use bookings, and express checkout are all done in clicks, and folios stay clean" (PMS page); "Most arrivals are checked in on the guest's phone before they reach the lobby."
- Intake breadth (A): "Reservations from your website, OTAs, walk-ins, phone, group blocks, corporate accounts, and travel agents, all auto-allocated, confirmed, and visible across the property."
- Housekeeping seam (A, FAQ): "Room status updates in real time, keeping housekeeping and front desk teams aligned throughout the day."
- Night audit exists as a separate named function (A) — not the desk's daytime loop.
- Marketing stat claims (e.g., "80% faster check-ins") are vendor performance claims — recorded here but **not** promoted anywhere else.

### HotelDruid (Tier 2 product description; layer A for product claims)

Key observations:

- Self-description (A): "free and open source program for hotel management (property management software) … from bed & breakfasts or vacation rentals with few apartments to hotels with hundreds of rooms."
- Core features (A): configurable rooms/periods/rates; **automatic assignment of the rooms with user-defined rules**; extra costs, special offers and restrictions attached to rates; **customized documents for receipts, invoices, emails, forms**; multi-user with privileges; POS for bars/restaurants; comparative statistics; website availability pages; booking engine and channel manager as add-on modules; group bookings; drag-and-drop calendar.
- Interpretation (C): at the micro-property pole the product's substance is the same skeleton — rooms + assignment + documents (registration/receipts/invoices) — with distribution modules bolted on; the desk loop is nearly the whole product.

---

## Cross-product Comparison

| Structure | Mews | WebRezPro | YCS/eZee | HotelDruid | Verdict |
|---|---|---|---|---|---|
| Rooms as individually assignable units ("Space"/"unit"/"room") | A | A | A | A | universal in sample |
| Live room/occupancy status visible to desk | A (spaces, status states) | A (housekeeping report "integrated with front office"; dirty/clean/inspected/in-service/DND) | A ("room status, housekeeping… unified") | C (assignment rules imply state; no explicit status language fetched) | core-adjacent; status seam to housekeeping is cross-product |
| Registration/check-in with room assignment; arrivals list | A (check-in defined; "start reservation") | A (arrivals due today; retrieve by name/confirmation) | A (one-click check-in; pre-arrival mobile check-in) | C (assignment + documents; no explicit check-in word in fetched text) | core in sample |
| Walk-ins / reservation-less arrivals | A (implied; reservation contract can exist without pre-booking? not explicit) | A (front desk makes reservations) | A ("walk-ins" named as intake) | A (booking pages aside, manual entries supported) | common; walk-in explicitly named at YCS |
| In-house stay maintenance (room moves, extensions) | A (implied by reservation lifecycle) | C (implied by folio/charges model) | A (explicit: room moves, stay extensions, day-use, express checkout) | C (drag-and-drop calendar implies move/extend) | core by abstraction; strongest named at YCS |
| Check-out with settlement | A (check-out = bill settled → closed) | A (departures due today; receipts) | A (express checkout; e-receipt) | C (invoices/documents) | core in sample |
| Guest folio as running account | A (Bill ≡ folio, open/closed, settled) | A (reservation folio, folio splitting, guest ledger with in-house balances) | A ("single guest folio" through the stay) | A (invoices/receipts documents; extra costs) | universal → definitional |
| Charges posted from property outlets (POS/spa/room service) | A (Additional Services added to Bill; Paymaster) | A (POS purchases posted to folios; non-resident POS invoices) | A (dining transactions in folio) | A (POS module; extra costs) | common mature structure |
| Deposits / prepayment handling | A (Deposit, Preauthorization defined) | A (deposits and refunds applied through folio) | A (payment leg of check-in) | C | common mature structure |
| Cashier / cash-drawer accountability | A (Cashier role, multi-cashier) | C (receipts printing; implied) | C | C | product-specific prominence (Mews); concept historically standard — keep common, not definitional |
| Guest ledger view (in-house balances + deposits from future guests) | C (profile billing) | A (explicit "Guest Ledger") | C | C | classic front-office structure; common |
| Group / block handling at the desk | A (Group/Availability Block concepts) | A (group folios, rooming lists, group check-in/out) | A (group blocks as intake) | A (group bookings) | common |
| Guest profile created/maintained | A (Customer Profile, exists independent of reservation) | A (auto-created with reservations) | A (guest profiles at one interface) | C | common; deep profile/loyalty belongs to CRM leaf (processed) |
| Housekeeping operations (zones, checklists, inspections) | A (Tasks/Departments) | A (own named feature area) | A (task lists; work orders) | C | belongs to Hotel Housekeeping Management; status feeds the desk |
| Reservation intake machinery (booking engine, channel manager, OTA sync) | A (explicit subsystems) | A (add-on modules) | A (platform modules) | A (add-on modules) | belongs to distribution leaves; the desk consumes intake |
| Rate/pricing management | A (Rate, Rate Group concepts) | A (own Rate Management feature) | A (Revenue Management platform) | A (rates with offers/restrictions) | belongs to PMS/rate management; not desk-defining |
| Night audit / end-of-day | C (accounting reports) | C | A (named function, automated) | C | adjacent PMS function; NOT the desk loop itself |
| Self-service / mobile / kiosk check-in | A (online check-in in definition) | A (contactless check-in; guest agreements) | A (kiosk, phone check-in, digital keys) | C | era-current capability layer |
| AI handling of arrivals/requests | C | C (AI marketing module exists, elsewhere) | A (AI ID verification/payment/room assignment; AI concierge) | C | era-current, product-specific prominence |

## Canonical Model (abstraction)

### Level 0 — Defining Invariant

The desk-facing operational application for the guest stay, whose defining core is exactly three jointly-held structures:

1. **The property's rooms as live, individually assignable inventory.** The application holds the property's bookable accommodations as concrete units with current occupancy and readiness state, and the desk works against that live state (assign, move, release). Remove it → a reservation manager / distribution tool with nothing to assign.
2. **The stay operated from arrival to departure.** Guests are registered into rooms (check-in, whether from a reservation or a walk-in), maintained in-house (room moves, extensions, services rendered during the stay), and departed (check-out). The stay — not the reservation, not the room alone — is the desk's unit of work. Remove it → a room-status board or a housekeeping tool.
3. **The guest folio with posting and settlement.** Each stay carries a running guest account onto which room and on-property charges post, deposits/payments settle, and against which the balance is closed at departure (the guest ledger being the desk's money view over in-house accounts). Remove it → a registration system with no money, below the Type.

Jointly-held is load-bearing: 1 alone = room inventory system; 2 without 1 = abstract check-in choreography with nothing to assign; 3 without 1+2 = a payments terminal with stays.

### Level 1 — Common Mature Structure

- arrivals/departures lists as the desk's daily work queues
- guest profiles (auto-created from reservations; repeat-guest recognition)
- reservation handling at the desk (make/modify/cancel; walk-in creation)
- deposits, preauthorizations, refunds; receipts (print/email)
- posting of ancillary/on-property charges to the folio (POS, spa, room service, phone), house accounts, paymaster-style compiled billing for companies
- folio splitting / multiple folios per stay; guest ledger balances view
- group/block handling at the desk (rooming lists, group folios, group check-in/out)
- desk reminders/alarms, VIP flags, reservation notes
- housekeeping-status integration for room readiness (status consumed; operations elsewhere)
- multi-user with role/privilege structure; cashier-style money accountability appears in mature products
- night-audit / end-of-day reporting adjacency (in fuller products)

### Level 2 — Variant / Optional Structure

- self-service surfaces: online/mobile check-in, kiosks, digital keys, contactless guest agreements, e-signature
- day-use / hourly room bookings
- guest messaging/request tracking at the desk (vs dedicated guest-experience leaves)
- ID/document capture and statutory registration-card compliance (jurisdictional)
- AI-assisted arrivals (ID verification, payment, assignment) — era-current
- property-type breadth (hostel bed-level semantics, B&Bs, vacation rentals — per processed Hostel Management System pass, hostel semantics are inventory configuration within the same desk loop)
- on-premise vs cloud deployment (both poles exist: legacy on-prem "FrontDesk" products and cloud platforms)

### Level 3 — Vendor-specific Structure (Research Notes only)

- Mews: "start reservation"/"process reservation" API naming; Bill open/closed with Editable History Window; Paymaster (Lobby Bar / City Ledger); Space/Resource "SpaceTime" broadening.
- WebRezPro: alarm calendar; hourly reservations module; POS invoice separation for non-residents; garbled-page features (adjoining/virtual units, waitlist) observed at low confidence.
- YCS: "agentic" Pulse AI layer; kiosk mode with QR self-check-in; specific marketing performance stats (noted, not used).
- HotelDruid: automatic assignment by user-defined rules; SES Hospedajes document localization (Spain).

## Historical / Market-Sample Check

Question: would older, regional, platform-native products fit the three-part core?

- Paper-era front desk: room rack/board (live room state, leg 1), registration cards + room keys on a rack (arrival/in-house/departure, leg 2), guest folio ledger book and city ledger with a cashier window (leg 3). Fits. (C — reasoning from the classic front-office model; its vocabulary is corroborated as still current by fetched Mews glossary definitions of Bill≡folio, Cashier, Paymaster incl. City Ledger Paymaster.)
- 1980s–90s on-premise front-office systems (Fidelio-class; eZee FrontDesk lineage): screen room rack, check-in/check-out, guest ledger posting, night audit. Fits.
- Cloud-era PMS front-desk modules and desk-first cloud products (all four sampled products). Fits.
- What does NOT fit: booking engines / CRS / channel managers (sell before arrival; no in-house stay to operate, no settlement of a folio at departure — money is a booking payment, not a stay folio); pure housekeeping systems (room status without guest registration or money); guest-messaging/concierge surfaces (no folio of record).

The core therefore does not over-fit the current mobile/self-service era: self check-in, kiosks, digital keys, AI assistance are era-current capability layers, not invariants.

## Vendor-specific Findings

See Level 3 above. Also: WebRezPro's page is itself evidence that vendors sell "front desk software" as a named category ("hotel front desk software") while shipping it as one feature area of a PMS — the category word is real, the product population is mostly PMS products with a desk-first emphasis.

## Boundary Findings

| Neighbor | Seam | Remove-what-to-become test |
|---|---|---|
| **Hotel Property Management System / PMS** | PMS is the property's whole system of record: reservations & distribution coordination, rates/inventory, housekeeping operations, front desk, guest accounting, reporting/night audit, multi-property. The front desk application is the **desk-facing operational slice**: the arrival→in-house→departure loop with folio settlement. Every sampled PMS names Front Desk as one feature area among others (WebRezPro nav: Front Desk / Rate Management / Housekeeping & Maintenance / Groups / Accounting…; YCS platforms list; Mews concept docs). | Take a PMS and remove distribution/rates/housekeeping-operations/reporting — what remains (desk loop + folio) is this Type. Take a front desk application and add those as first-class managed structures — it becomes a PMS. |
| **Hotel CRS / Booking Engine / Channel Manager** | Distribution is pre-arrival selling: ARI distribution and reservation capture. The desk operates the stay after arrival. | Remove the stay/folio/settlement → distribution system. |
| **Hotel Housekeeping Management** | Housekeeping owns room servicing operations (zones, checklists, inspections, work orders). The desk consumes room status and hands rooms over for service. | Remove guest registration/folio → housekeeping management. |
| **Hotel Guest Experience Platform / Digital Concierge** | Those are guest-facing surfaces (guest's phone, chat, portal). The front desk application is staff-facing at the desk. Self-check-in/kiosk features straddle: same stay record, opposite seat. | Remove the desk-side system of record role → guest-facing app. |
| **Hotel CRM / Loyalty Platform** (processed) | CRM/loyalty holds the guest profile of record and the loyalty program across properties/stays; the desk application touches profiles at arrival but does not own the relationship or program. | Remove stay/folio loop → CRM/loyalty territory. |
| **Hostel Management System** (processed) | Same desk loop; hostel leaf adds bed-as-unit / per-person rate semantics as its structural delta. Consistent with this leaf treating property-type semantics as variants. | — |
| **Reservation / check-in kiosk self-service** | Kiosk mode is a delivery surface of the same desk loop in some products (observed at YCS), a separate self-service product in others. Held as variant/adjacent, not resolved — worth noting. | — |

### Taxonomy judgment

The market does **not** maintain a cleanly separate product population sold only as "front desk applications" — the search category is served by small-property PMS products (desk-first emphasis) plus the front-desk modules of full PMS suites. The leaf is nonetheless defensible as an **operational-slice Type** (same pattern as Kitchen Display System within restaurant operations): its unit of work (in-house stay), its loop (arrival→departure), and its money object (folio) are stable and nameable, and every PMS vendors' own nav/documentation isolates them as a "Front Desk" area. Two product shapes therefore exist: desk-first small-property systems (where the desk loop is most of the product) and the front-desk module inside full PMS. **Recommend joint review with hotel-property-management-system-pms when that leaf is processed** — consistent with the pre-hung seam recorded by the hostel-management-system pass.

## Uncertainties

- Whether a front desk application without any folio/accounting could still be recognized as such — none observed in the sample (all four carry money structures); folio remains definitional under this evidence.
- Enterprise-tier desk workflows (very large properties: multi-room suites, traces, complex splits, VIP protocols) were not directly observed (OPERA docs unreachable); assertions about them kept generic.
- Exact room-status vocabularies vary by product (WebRezPro: dirty/clean/inspected/in-service/DND; others unnamed in fetched text); canonical status expressed abstractly.
- WebRezPro page contained garbled sections; adjoining-units and waitlist handling treated as present-but-low-confidence and excluded from the canonical model.
- Whether self-service check-in belongs here or to Hotel Guest Experience Platform — unresolved; noted for joint review.

## Final Synthesis

A Hotel Front Desk Application is the staff-facing operational application of a lodging property's front office: it holds the property's rooms as live assignable inventory, moves each guest stay through registration (check-in) → in-house service (moves, extensions, posted charges) → departure (check-out with settled folio), and keeps the guest folio — the stay's running account — as the desk's money record, with the guest ledger as the view over in-house accounts. Everything else the market associates with the desk — walk-ins, groups, deposits, profiles, housekeeping-status coordination, night-audit adjacency, self-service surfaces, messaging — is common mature structure or variant capability layered on that core, and the type exists in the market either as a desk-first small-property product or as the front-desk module of a full PMS.
