# Research Notes — Banquet Management

Research date: 2026-09-06
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what the "Banquet Management" Application Type actually is in the real hospitality/events software market: what core objects exist (function spaces, bookings, menus, BEOs), what lifecycle a banquet booking follows from inquiry to settlement, how the sale is handed off to kitchen/banquet operations, and how this Type differs from adjacent leaves (Catering Management, Venue Management System, Event Management Platform, Hotel PMS, Restaurant Reservation Platform).

## Initial Boundary

Initial hypothesis (before research): operator-side software for venues that sell and execute catered functions (weddings, galas, corporate dinners, receptions) in their own function spaces. Expected core: function diary/space availability, event/booking record, menus & packages, guest counts, banquet event orders (BEOs), staffing, deposits/invoicing. Nearest neighbors: Catering Management (off-premise food production/delivery), Venue Management System (space booking focus), Event Management Platform (planner-side), Hotel PMS (rooms), Restaurant Reservation Platform (single-meal table bookings). Key risk: the node may collapse into either Catering Management or Venue Management System; the BEO/sales-to-operations handoff is the suspected distinguishing structure.

## Research Questions

1. What is the central record (booking/event/function) and what does it aggregate (client, space, time, menu, counts, charges)?
2. How do function spaces and the function diary work (availability, holds, tentative vs definite, conflict prevention)?
3. What is the sales lifecycle (inquiry → proposal → contract → deposit → confirmed → executed → billed)?
4. What exactly is a BEO, which audiences get which version, and how is it produced and kept current?
5. How do menus/packages/pricing work (per-person packages, F&B minimums, gratuity, taxes)?
6. How are guest counts handled (expected vs guaranteed; what depends on the count)?
7. How do floor plans / seating / table management participate?
8. How is banquet staffing handled (shifts, captains, conflict tracking)?
9. What kitchen-facing outputs exist (kitchen sheets, kitchen displays, recipes, packing lists)?
10. How does settlement work (deposits, invoices, payment links, master accounts)?
11. What roles use the system (sales, catering/ops, kitchen, banquets staff, accounting, management)?
12. Where are the boundaries against Catering Management / Venue Management / Event Management / Hotel PMS / Restaurant Reservation?

## Representative Products

Chosen for market representation + documentation quality + different product philosophies + different customer tiers:

| Product | Position | Philosophy |
|---|---|---|
| Tripleseat | SaaS for restaurants, hotels, venues running private events (large installed base, US-centric) | sales-pipeline-first: capture → book → plan → grow; documents generated from the event record |
| Caterease | standalone catering & event management (desktop heritage + web hub), caterers and venue foodservice | catering-operations-first: menus, recipes, production, staffing, prints |
| Planning Pod | mid-market venue-first end-to-end platform (venues, country clubs, museums, restaurants) | venue-business-first: booking calendar + BEOs + payments + client portals in one place |
| Event Temple | hotel sales & catering software (1,400+ hotels, 45+ countries; independent → chains) | hotel-group-first: leads/RFPs, room blocks, GRC & event diary, BEOs, PMS integration |

Note: the classic enterprise hotel tier (Amadeus Sales & Event Management / Delphi, Oracle Hospitality S&C) could not be fetched (bot-blocked); Event Temple serves the same hotel S&C structure and was used as the hotel-tier sample. See Sources for the limitation record.

## Sources

Official product pages fetched 2026-09-06:

- Tripleseat — home: https://www.tripleseat.com/ ; Proposals/Contracts/BEO feature page: https://tripleseat.com/features/proposals-contracts-beo/ ; Plan platform page: https://tripleseat.com/platform/plan/
- Caterease — home: https://www.caterease.com/ ; features: https://caterease.com/features (help/documentation surfaced at https://help.caterease.com)
- Planning Pod — home: https://www.planningpod.com/ ; dedicated BEO page: https://planningpod.com/banquet-event-orders
- Event Temple — home: https://www.eventtemple.com/ ; Events & Catering feature page: https://www.eventtemple.com/events-and-catering (help center surfaced at https://intercom.help/eventtemple/en/)

Access limitations:
- Amadeus (amadeus.com, two URLs) returned bot-interstitial pages twice; abandoned per network rules. Enterprise hotel S&C tier therefore evidenced only indirectly (via Event Temple, which occupies the same hotel sales & catering category).
- EventPro (eventpro.io, two URL forms) returned empty responses twice; abandoned.
- Function Tracker (functiontracker.com) returned HTTP 403; abandoned.
- Deep help-center articles were not individually fetched for any vendor; research relies on official product/feature pages. Per evidence rules, no precise numeric limits (guarantee cutoff windows, deposit percentages, capacity numbers) are asserted anywhere; moderate claim strength used throughout.

## Product Observations

### Tripleseat (evidence layer: A — directly observed on official pages)

- Positioning: "all-in-one event management software for restaurants, hotels, and venues"; platform pillars Capture (inquiry inbox, lead capture) → Book (proposals, budgets, payments) → Plan (floor plans, staffing, coordination) → Grow (insights/revenue).
- Documents are generated from the event record, not authored separately: "Proposals, banquet event orders, contracts, and invoices generate from your event details, update in real time as things change."
- Two audiences, two document layouts from one event record: guest-facing proposal (branding, pricing, gratuity selector) vs internal BEO ("strips out the financial detail and surfaces the logistics your staff actually need: headcounts, menus, room configuration, and staff instructions").
- Billing logic inside documents: F&B minimums "configured to track against specific menu categories, add unmet amounts to the grand total, and apply taxes and fees to shortfalls"; gratuity selectors at signature; line items/fees/taxes calculate inside the document "so the invoice matches the proposal."
- Role framing on the BEO page: Sales (send proposal in the same workflow as capturing the inquiry), Operations (internal BEO generated from the same event record), FOH/BOH ("the document your front- and back-of-house team works from on event day is the same document that was updated when the guest changed their menu").
- Plan page: shared calendars ("filter by room, date, or manager"), floor plans (2D diagramming, 3D walkthroughs, interactive layouts, client collaboration), automated tasks, table management integrations, guest portal (sign, pay, review plans, communicate).
- Hotels package: room blocks, group sales, multi-day events, PMS integration. Industries include restaurants, hotels, bars/nightclubs, catering, wedding venues, event & banquet venues, breweries, wineries, schools, enterprise.
- AI layer ("Tripleseat Intelligence") positioned on top of platform workflows.

### Caterease (evidence layer: A)

- Positioning: "the complete software solution for catering and events"; customers include off-premise caterers and venue/institutional foodservice (hospitals, hotels, universities in testimonials).
- Event Booking Wizards: "create custom wizards for each type of event you book and even make fields conditionally required — so all information is entered consistently every time."
- Dynamic Menu Building: "incremental searching, automatic menu packages, linked or minimum quantities" for building event menus.
- Customizable Prints: "a custom library of back-of-house or front-of-house prints using flexible templates" — the BEO/kitchen-sheet family in catering vocabulary.
- Shifts & Staffing: "assign shifts and even specific employees to work those shifts — with automatic tracking of all potential scheduling conflicts."
- Recipes & Packing Lists: "detailed recipes and packing lists associated with each menu item… automatically compiled and quantified as you build event menus" (production-side depth).
- Client Management: contact details, history, "total event number and value" per client.
- Task Management: pop-up reminders, history notes, checklists.
- Horizon Hub (web/mobile companion): AI assistant (Cai), Event Portals (internal team review + client portal), dashboard widgets, calendar (day/week/month, grouping/filtering), custom & scheduled reports, Kitchen Display ("listing all items needed for the day's events even highlighting recent changes"), Sign & Send (e-signature templates), Industry Trends (anonymized benchmarking).
- Payment processing: tokenized cards, payment links (Mosaic). Testimonials name proposals, BEOs, contracts, invoices, menus, reporting, accounts receivables, group meal reservations.

### Planning Pod (evidence layer: A)

- Positioning: venue-first ("if you sell, book, and host events out of a space you operate"); FAQ explicitly contrasts with planner-side tools: "Honeybook and Aisle Planner… don't handle BEOs, floor plans, or venue-side operations."
- Venue & Catering toolset: Booking Calendar, Floor Plans, Banquet Event Orders, Food & Beverage, Tour Scheduling, Equipment Management.
- BEO page defines the artifact: "A banquet event order (BEO) is the document that tells your staff, kitchen, and client exactly how an event will run — menus, headcounts, timing, setup, and payments."
- BEOs auto-generate from the event record: "event dates and times, contacts, locations and spaces, headcounts, pricing, timelines, and payments all flow in automatically"; "change a booking date, headcount, room, or catering item anywhere… and that information syncs to the BEO automatically — so the document in the kitchen is never out of date."
- Audience-specific BEO layouts: 7 pre-built layouts (client-facing, front-of-house, kitchen, bar, deliveries); modular panels (event overview, F&B, schedule, A/V, setup, linked proposals/invoices, special requirements, signatures); custom fields.
- F&B packages dropped into BEOs "complete with descriptions, pricing, serving portions, dietary notes, and serving times."
- E-signatures on BEOs (email link or client portal); signed-BEO version history ("who signed off on what, and when").
- PDF downloads individually or in batches "by meal type and serving date/time"; email directly from CRM/communications.
- Schedule panel syncs with the Itinerary tool; floorplan + setup panel syncs from the Floorplans tool; linked invoices/contracts pull proposal totals, invoice balances, contract signature status into BEOs.
- Business side: lead capture forms, pipeline automation, proposals, contracts & e-signatures, integrated payments, invoices with installment schedules, embedded event insurance; client portals; workflows & triggers; custom reporting/dashboards.
- Pricing model based on number of events under management (volume-based).

### Event Temple (evidence layer: A)

- Positioning: "sales and catering software purpose-built for hotels"; users named: Directors of Sales, GMs, Sales & Catering Managers, revenue leaders; scales from single independents to portfolios (~200 properties on one account).
- Vendor's own category definition (FAQ): "the system a hotel's sales team uses to capture inquiries, manage group and event bookings, build proposals and contracts, block guest rooms, and produce banquet event orders."
- Platform parts: Leads & Pipeline (intake forms, inquiry parsing → structured leads; pipeline stages shown as New Lead → Proposal → Signed → Paid); Bookings & Room Blocks (room blocks, packages, and events in one booking record; pickup against allotment); **GRC & Event Diary** ("live function space availability at a glance. Check the GRC, hold space, and catch conflicts before they become double-bookings"); Proposals & Contracts (branded digital, signed online, details auto-pull from the booking); **BEOs & Documents** ("banquet event orders and event documents that stay in sync with the booking, so the kitchen, banquets, and AV always work from the latest version"); Payments (deposits, invoices, online payments inside the booking); meeting-space Booking Engine; Dashboard; Reporting (pipeline, pace, production); Multi-Property/Chain Management.
- Events & Catering page: function diary "shows all of your tentative and definite bookings in a single, grid-style calendar view" (one event space or fifty); "create banquet event orders and kitchen sheets with the click of a button. Our BEO routing makes it easy to create complex BEOs for any type of event or booking"; "update banquet event orders, log tasks and easily track orders, payments."
- PMS integrations (Mews, Stayntouch, Cloudbeds, Opera Cloud, Apaleo): two-way real-time sync of availability, rates, guests, room blocks — "so sales and front office always read from the same page."
- Contrast framing vs generic CRM: "A generic CRM does not understand room blocks, function space, banquet event orders, or group pickup."

## Cross-product Comparison

| Dimension | Tripleseat | Caterease | Planning Pod | Event Temple | Commonality |
|---|---|---|---|---|---|
| Central record | event record | event | event/booking record | booking (group + events) | B — same concept, different names |
| Lead intake | inquiry inbox, capture forms | booking wizards, online orders/inquiries | lead capture forms, pipeline automation | intake forms, inquiry parsing, RFPs | B (mechanism varies) |
| Sales pipeline | Capture→Book pillars | client mgmt + tasks/reminders | pipeline automation | sales CRM with stages (lead→proposal→signed→paid) | B |
| Function space & diary | calendar filterable by room | calendar views (day/week/month) | booking calendar + floor plans | function diary (grid), tentative vs definite, hold space, conflict/double-booking prevention | B — universal |
| Documents from record | proposals/contracts/BEOs/invoices auto-generated, real-time sync | proposals/BEOs/contracts/invoices; BOH/FOH print library | BEOs auto-generated, real-time sync | proposals/contracts/BEOs/kitchen sheets, stay in sync with booking | B — universal; single-source-of-truth pattern |
| Audience-specific document views | guest proposal vs internal BEO | front-of-house vs back-of-house prints | 7 layouts (client/FOH/kitchen/bar/delivery) | BEO routing to kitchen/banquets/AV; kitchen sheets | B — universal |
| Menus & packages | F&B minimums tracked per menu category | dynamic menu building, packages, linked/minimum quantities | F&B packages (descriptions, pricing, portions, dietary notes, serving times) | packages in booking record | B |
| Guest counts | headcounts on BEO | event details | headcounts sync to BEO | headcounts | B |
| Floor plans / seating | 2D/3D floor plans, table mgmt integrations | (prints) | floorplans tool + seating charts; setup panel into BEO | (event diary focus) | B — common, depth varies |
| Staffing | Plan pillar (staffing) | shifts & staffing with conflict tracking | (tasks/checklists) | (banquets team consumes BEO) | B — common, depth varies |
| Kitchen outputs | FOH/BOH day-of document | kitchen display (day's items, change highlighting), recipes, packing lists | kitchen BEO layout | kitchen sheets | B |
| Client collaboration | guest portal (sign, pay, review, communicate) | event/client portals | branded client portals | e-signature + online payment | B |
| Payments & settlement | payments feature, deposits | tokenized cards, payment links, AR | integrated payments, invoices & installments | deposits, invoices, online payments in booking | B |
| Billing logic | F&B minimums, gratuity selectors, taxes/fees in document | invoices, AR | invoice balances linked into BEO | deposits/invoices | B (depth varies; Tripleseat most explicit) |
| Reporting | insights | custom/scheduled reports, industry trends | custom reporting, dashboards | pipeline/pace/production reports | B |
| Tasks/workflows | automated tasks | task mgmt, reminders, checklists | workflows & triggers, tasks | tasks, workflows | B |
| Room blocks / PMS | hotels package (room blocks, PMS integration) | (hotel testimonials) | (hotels industry page) | room blocks + GRC + two-way PMS sync | A-per-product — hotel variant, not universal |
| Multi-property | enterprise package | (multi-location implied) | multi-venue operators | chain management, portfolio reporting | B — scale variant |
| Online booking / marketplace | Direct Book, Venue Marketplace | online orders/inquiries | web forms | meeting-space booking engine | B — optional channel |
| AI assistance | Tripleseat Intelligence | Cai assistant | (not emphasized) | (not emphasized on fetched pages) | A-per-product — optional |
| Registration/ticketing | Tickets feature | (not emphasized) | registration & ticketing tools | (not emphasized) | A-per-product — optional crossover |

## L0 / L1 / L2 / L3

### L0 — Defining Invariant

A venue-operated function business run as records: **sold catered functions (bookings) that occupy schedulable function-space time, carry a committed menu/package offering sized by guest count, are handed off to the operating departments as executable instructions, and settle commercially against committed terms.**

Components:

1. **Function booking as central record** — a client-committed dated occasion (banquet/function/event) that aggregates everything: client, date/time, space, offering, counts, charges; it moves through a sales-to-execution-to-settlement lifecycle.
2. **Function-space scheduling substrate** — the operation's function spaces as a managed inventory with availability; bookings occupy time slots; conflicting occupancy is prevented (function diary).
3. **Committed food-and-beverage offering sized by guest count** — menus/packages with per-person or itemized pricing and a headcount; the banquet is fundamentally a catered function sold in advance.
4. **Sales-to-operations handoff** — the sold booking must become executable instructions for kitchen, service, and support departments; the BEO (banquet event order) is the canonical artifact, with audience-specific variants (client-facing vs internal; kitchen/FOH/bar sheets).
5. **Commercial settlement** — the booking carries committed commercial terms (price, minimums, deposits) that resolve into invoices/payments.

Why this is minimal: remove the function-space substrate and only generic catering/CRM remains (→ Catering Management); remove the committed F&B offering + counts and only a space-booking calendar remains (→ Venue Management); remove the operational handoff and it is a sales CRM with a calendar; remove settlement and it is not a sold function business. The paper tradition — a function diary book, typed BEO sheets distributed to kitchen and banquet departments, a deposit ledger — already satisfies all five components, which is the historical floor (§24 check passes).

### L1 — Common Mature Structure

Present across most sampled mature products; expected by the market, not definitional:

- **Lead intake & sales pipeline** — inquiry capture (forms, inboxes, RFP parsing), lead stages, follow-up automation/reminders.
- **Proposal & contract generation** — branded documents auto-filled from the booking record; e-signature; version currency.
- **Function diary / booking calendar views** — grid calendar by room/day; tentative vs definite holds; filtering by room/date/manager.
- **Menu & package management** — menu libraries, packages, linked/minimum quantities, dietary notes, serving times.
- **Guest count machinery** — expected vs guaranteed counts driving production and billing (guarantee mechanics widely practiced; exact cutoff windows not verified).
- **Floor plans & seating** — 2D/3D room diagrams, table management, setup instructions synced into BEOs.
- **Staffing** — shift assignment to specific employees, scheduling-conflict tracking, banquet team consumption of the BEO.
- **Kitchen production outputs** — kitchen sheets/displays of the day's items with change highlighting; recipes and packing lists compiled from menus (deepest in catering-heritage products).
- **Client portal / collaboration** — review details, sign, pay, communicate in one branded place.
- **Payments & invoicing** — deposits, installment invoices, payment links, online payment; balances linked into documents.
- **Billing logic** — F&B minimums tracked against menu categories, gratuity, taxes/fees computed inside documents.
- **Task management & workflows** — reminders, checklists, BEO routing to departments, triggered automations.
- **Reporting** — pipeline/pace/production revenue reports, dashboards, scheduled reports.
- **Integrations** — PMS (hotels), POS/table management (restaurants), accounting, e-mail/calendar.

### L2 — Variant / Optional Structure

Depends on segment, venue type, or business model:

- **Hotel group layer** — room blocks, group rooms pickup, GRC (group room control), master-account posting, two-way PMS sync.
- **Multi-property / chain management** — portfolio-wide templates, pipeline, and reporting.
- **Online booking channels** — 24/7 meeting-space booking engines, venue marketplaces, direct-book with approval gates.
- **Event-registration/ticketing crossover** — tickets, registration, attendee tools for public events run in the same spaces.
- **Equipment/AV/rentals management** — inventory of banquet equipment, A/V panels in BEOs.
- **Tour scheduling** — site-visit appointments in the sales loop.
- **Off-premise/delivery variants** — transport, packing lists, venue addresses (catering crossover).
- **Benchmarking** — anonymized industry trend data.
- **AI assistance** — assistants over events/clients/reports; AI-drafted documents.
- **Embedded insurance**, financing, and other commerce add-ons.

### L3 — Vendor-specific Structure

- Tripleseat: Capture/Book/Plan/Grow pillar naming; Direct Book; Venue Marketplace; package tiers (incl. Tripleseat Hotels); F&B-minimum billing widget specifics; gratuity selector at signature; Tripleseat Intelligence.
- Caterease: Horizon Hub; Cai assistant; CaterOS workspace; Mosaic payment processing; Sign & Send; Industry Trends; event booking wizards with conditionally required fields.
- Planning Pod: 7 pre-built BEO layouts; modular BEO panels; 40+ tools framing; volume-based pricing (by events under management); embedded event insurance; comparisons vs Tripleseat/HoneyBook/Aisle Planner.
- Event Temple: GRC (Group Room Control) naming; BEO routing; Smart Mail; chain management; PMS marketplace (Mews/Stayntouch/Cloudbeds/Opera Cloud/Apaleo); HotelTechAwards positioning; unlimited-users option.

## Vendor-specific Findings

- Tripleseat's "two documents, one event record" framing (guest proposal vs internal BEO) is the clearest articulation of the audience-split document pattern; Planning Pod and Event Temple implement the same pattern with layout/panel systems and routing.
- Caterease is the only sampled product with first-class recipes/packing lists compiled from menus — production depth inherited from off-premise catering.
- Event Temple is the only sampled product exposing the hotel group layer (GRC, room-block pickup, PMS two-way sync) as a first-class structure.
- Planning Pod prices by event volume under management rather than seats — a business-model detail, not structure.
- Caterease's Industry Trends (anonymized cross-customer benchmarking) is unique in the sample.

## Rejected Findings

- "Banquet Management = event management software" — rejected. Event management platforms center on the planner side (registration, agenda, attendee apps, marketing); banquet management centers on the venue operator selling and executing catered functions. Planning Pod's own FAQ draws this line (planner tools "don't handle BEOs, floor plans, or venue-side operations").
- "Banquet Management = generic CRM with a calendar" — rejected. Event Temple explicitly contrasts with generic CRM: room blocks, function space, BEOs, and group pickup are structures a generic CRM does not carry.
- "The BEO is just a printable document" — rejected. Across all four products the BEO is a live, synced projection of the booking record with audience-specific views, version/signature history, and department routing; the document is the interface, the record is the substance.
- "Guest counts are a single number" — rejected as a structural claim. The expected-vs-guaranteed distinction is industry practice, but exact cutoff windows and over/under-billing rules vary and were not verified; the document must not assert precise timing.
- "Banquet software always includes floor plans/seating" — rejected as definitional. Floor plans are common (Tripleseat, Planning Pod) but Event Temple's fetched pages center on diary/BEO, and Caterease's strength is production prints; seating depth varies widely.
- "Room blocks are part of banquet management" — rejected as L0. Room blocks belong to the hotel variant (L2); restaurant/banquet-hall products run fully without them.

## Boundary Findings

- **vs Catering Management**: catering centers on food production and delivery service (recipes, production quantities, packing lists, transport, off-premise staffing); banquet management centers on the booked function in the venue's own function space (diary, room setup, BEO, on-premise service). Remove the function-space substrate and on-premise execution → Catering Management. Products span both (Caterease, Tripleseat's catering industry page); the directory keeps both leaves, and the boundary is where the operational center of gravity sits.
- **vs Venue Management System**: VMS centers on the space inventory and its booking calendar for any use (meetings, rentals, coworking, events); banquet management adds the catered-function lifecycle (committed menus, counts, BEO, kitchen). Remove the F&B/BEO layer → Venue Management. (Venue Management leaf not yet produced; boundary recorded for that pass.)
- **vs Event Management Platform**: planner-side vs operator-side. Event platforms serve the organizer running an event program (registration, agendas, attendees, marketing); banquet management serves the venue selling and executing functions. Remove the operator/sales/BEO side and center on attendees → Event Management.
- **vs Hotel PMS**: PMS centers on guest rooms, stays, and folios; hotel sales & catering centers on function space and events. The integration seam is room blocks (group rooms attached to event bookings) and posting banquet charges to guest/master folios. Event Temple's PMS sync (availability, rates, guests, room blocks) documents this seam.
- **vs Restaurant Reservation Platform**: a reservation is a single table/meal occasion for a diner; a banquet booking is a contracted private function with menus, guarantees, BEO, and deposits. Private dining is the bridge — restaurants use banquet software for their private-events business (Tripleseat's restaurant segment).
- **vs Event Registration Platform / Attendee Management**: those manage the population of people attending an event; banquet management manages the function as a sold, produced, and settled engagement. Guest lists may attach late in the banquet lifecycle but are not the core.
- **Naming**: "sales & catering software" (hotel usage), "banquet software", "event venue management software", "catering & event management software", "BEO software" — a synonym cluster around one structure. The BEO is the industry's shibboleth: products advertising BEO handling are in this Type.

## Uncertainties

- Exact lifecycle state vocabularies per product: only Event Temple's fetched pages name states (tentative vs definite bookings; lead→proposal→signed→paid pipeline stages). Other products' internal state names were not verified at article level; final document describes lifecycle conceptually.
- Guarantee mechanics (cutoff windows for final guest counts, over/under-guarantee billing rules) are industry practice but were not verified in fetched sources; no precise windows asserted.
- Enterprise hotel tier (Amadeus Delphi, Oracle S&C) unreachable; assume structural similarity to Event Temple's hotel pattern but record as unverified for the enterprise tier specifically.
- Depth of seating/place-card features per product not fully verified (Tripleseat mentions table management integrations; Planning Pod lists seating charts; neither fetched page details place-card mechanics).
- Master-account/folio posting mechanics (hotel) inferred from PMS-sync framing, not verified at article level.
- Off-premise logistics depth in Tripleseat/Planning Pod (delivery routing etc.) not verified; Caterease carries the clearest production/delivery evidence.

## Final Synthesis

Banquet Management is the venue-operator-side Type whose world is: **function spaces scheduled through a function diary → sold functions (bookings) that commit a client, a date/time, a space, a menu/package offering, and a guest count → the booking handed off to kitchen/service/support as audience-specific, always-current BEOs → the function executed (setup, staffing, production, service) → the booking settled (deposits, invoices, minimums, payments).** The defining core is the booking record + function-space scheduling + committed catered offering with counts + the sales-to-operations handoff (BEO) + commercial settlement. Mature products wrap it in lead pipelines, proposals/contracts with e-signature, menu/package libraries, floor plans and seating, staffing, kitchen outputs, client portals, payments, reporting, and integrations. The hotel variant adds room blocks/GRC/PMS sync; the catering variant adds production/delivery depth; scale variants add multi-property management. What separates this Type from neighbors is the operator-side sale-and-execution of catered functions in the venue's own spaces — planner-side event tools, space-only booking tools, and food-production-first catering tools each lack a different piece of this core.
