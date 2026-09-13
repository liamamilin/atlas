# Research Notes — Restaurant Reservation Platform

## Research Goal

Understand what a Restaurant Reservation Platform actually is, from real products: what objects exist inside it, who acts on them, how a booking flows from a guest's device into the restaurant's reservation book and through service, what the restaurant configures and controls, and where the boundary lies against neighboring Types (Restaurant POS, Restaurant Online Ordering, Appointment Scheduling, Event Registration/Ticketing, Amenity Booking, Hotel PMS, review/discovery networks).

## Initial Boundary

Working hypothesis at start:

- The Type is the restaurant's **reservation book as a system of record**: reservations (party × date/time × table) held in a managed book, gated by the restaurant's seating capacity and service schedule, with a guest-facing booking surface as the intake channel.
- Most likely confused with: Restaurant POS (the transaction surface during service), Restaurant Online Ordering (food composition), Appointment Scheduling Application (generic provider-time booking), Event Registration / Ticketing (discrete ticketed events), Amenity Booking Platform (facility amenities), Hotel PMS (rooms/stays), and the diner-facing discovery networks (OpenTable/Resy class) that sit on top of the same booking machinery.
- Prior sibling passes already fixed several seams:
  - **restaurant-online-ordering** (2026-09-09): "Reservations commit a table at a time; ordering composes food for fulfillment. Some products bundle both (booking with food pre-orders) — different objects, different workflows."
  - **restaurant-pos** (example pass): POS is the operator-facing transaction surface (order → check → payment); the reservation precedes service.
  - **restaurant-management-system** (2026-09-09): the management layer is the plan-to-actual control loop; reservations are not the plan domains it holds.

## Research Questions

1. What is the unit of record? (the reservation: what fields, what identity, what lifecycle?)
2. What is the capacity model? (tables, areas, floor plan, service hours, slots, covers, turn times)
3. What does the guest-facing booking path look like (widget, hosted page, network app, third-party channels), and is it definitional?
4. What confirmation semantics exist (instant vs request-to-confirm)?
5. What happens during service (seating, table status, waitlist, walk-ins)?
6. How is no-show risk handled (deposits, card holds, no-show fees, cancellation policies)?
7. How far does the guest-data layer go (profiles, visit history, spend, marketing) — core or common?
8. Where are the boundaries: POS vs book; ordering vs booking; appointments vs table service; events vs experiences; network vs direct?

## Representative Products

Selected for market representation + documentation quality + different product philosophy + different customer tier. Note on sampling: the two best-known network-pole products (OpenTable, Resy) were unreachable from the research environment (see Sources); the network/channel layer is instead evidenced through the channel-integration surfaces of the sampled restaurant-side products and Tock's consumer site.

| Product | Form | Tier / philosophy |
|---|---|---|
| SevenRooms | restaurant-side guest-experience platform (reservation book + CRM + marketing), channel-connected | mid-market/enterprise groups; commission-free, data-ownership philosophy; a DoorDash company |
| Tock | reservation platform with prepaid/ticketed emphasis + own consumer discovery app | fine dining, wineries, hotels; flat rate, no cover fees; deposits-first no-show protection |
| ResOS | standalone lightweight booking + table management | SMB independents (cafés, bars, pubs); commission-free, free tier, paid add-ons |
| Tablein | standalone booking system with website builder | SMB independents and groups across 50+ countries; explicit paper-book-replacement framing |

## Sources

Evidence layers: **A** = directly observed on an official source for that product; **B** = cross-product commonality; **C** = canonical inference.

Fetched 2026-09-09:

- SevenRooms: sevenrooms.com root; /platform/reservations-waitlist/; /platform/table-management/; /platform/booking-channels/; sitemap.xml. (help.sevenrooms.com redirects to a login page — help-center articles not reachable.)
- Tock: tockhq.com root; exploretock.com (consumer site). (/reservations redirects to root; help center not fetched.)
- ResOS: resos.com root; resos.com/features. (/knowledge-base returned 404.)
- Tablein: tablein.com root.

Abandoned after failures (network-restricted environment):

- OpenTable: restaurant.opentable.com (timeout ×2), www.opentable.com (timeout), support.opentable.com (401), web.archive.org retry (timeout).
- Resy: business.resy.com (transport error), partners.resy.com (transport error), www.resy.com (empty app shell, no content).
- Yelp Guest Manager: business.yelp.com (403).

## Product Observations

### SevenRooms (evidence layer A)

- Positioning: "More than just reservations… helps restaurants increase sales, delight guests and keep them coming back." Product hubs: Marketing (CRM & Segmentation, Marketing Automation, Email/Text Marketing, Search/Social & Discovery), Guest Experience (Reservations & Waitlist, Events/Experiences & Add-ons, Private Line, Loyalty & Perks, Reputation Management), Operations (Table Management, Revenue Management, Online Ordering, Reporting, Event Management, Voice AI, Channel Connect, API). Serves restaurants, groups, hotels, membership clubs, nightclubs/bars, sports/entertainment, breweries/wineries.
- Reservations & Waitlist page: "Drive direct online bookings from your own channels, eliminate cover fees and streamline reservation and waitlist management." Booking channels: Google, DoorDash Reservations, Facebook, Instagram, own-site widgets; bookings in fourteen languages; "Capture birthday, dietary and preference data from every reservation directly into your CRM."
- Upsells at booking: prepaid add-ons (welcome drinks, personalized experiences) at the point of booking; dining experiences and events as bookable options alongside standard reservations; secure digital payments for events and large groups; POS data connected to reservation history.
- No-show machinery: real-time Priority Alerts to waitlisted guests when a slot opens; VIPs/regulars notified before the general waitlist; credit card holds and cancellation fees on high-demand slots.
- Multi-location: real-time availability across the portfolio; cross-selling reservations/events/tickets between sister venues in the booking flow; guest preferences and visit history carried across properties.
- Waitlist: walk-ins and reservations side by side in one floor view; SMS updates; QR-code and Google Reserve waitlist joining without staff; VIP spotting in the queue.
- Automated messaging: pre-arrival reminders, two-way SMS during the visit, post-dining surveys "triggered by guest behavior."
- Table Management page: AI-driven seating algorithm; predictive waitlists; "Reservations and availability in one place: manage the full floor right from your host stand"; real-time table status and spend; 65+ POS integrations attaching order history and spend to guest profiles; push alerts for check-ins, new reservations, cancellations and no-shows; 360° guest profiles with auto-tags (allergies, order preferences, reservation notes); two-way SMS; grid view shift planning; automated pre-shift reports (party size, open tables, peak hours); predefined filters (VIP experiences, special parties, cancellations, no-shows). A customer quote documents operator-definable table statuses ("we have one called Last Round").
- Booking channels page: Google (Search, Reservations, Maps), Facebook/Instagram/TikTok profiles, and a global network of reservation discovery partners (Capital One Dining, Chope, OpenRice, Tripadvisor, Dorsia) — "pull them into a single reservation book and track your most effective channels." Private Line: VIPs text to book tables or experiences.

### Tock (evidence layer A)

- Positioning: "Tock's comprehensive reservation platform has everything you need to drive revenue, increase covers, and turn guests into regulars." Platform structure: Booking (Reservations, Experiences, Events, Waitlist, Table & service management), Operations (Guest data & reports, Integrations, Tock support), Discovery.
- "Offer more than just reservations — Sell ordinary reservations alongside unique experiences, like a chef's counter, cocktail class, or happy hour."
- "Control the flow of your dining room with flexible floor plans, powerful waitlists, and customizable communication."
- No-show protection: "Use any combination of deposits, credit card holds, and prepayment to help reduce no-shows. With Tock, you can customize cancellation policies, and surrounding communications, to suit your needs."
- Guest data: "With Tock, you'll always own and have easy access to your guest data."
- Plans: Base Plan includes walk-in waitlist tools, table management, guest management, events, marketing tools, 2-way SMS; Essential adds reservations, a **reservation request waitlist**, experience essentials, and takeout.
- Consumer app: "Tock has a guest-facing booking app… users can easily find and explore new businesses, or save and share their favorites."
- POS integrations: Toast, WineDirect, Commerce7, Tripleseat, Upserve. Verticals: restaurants/bars, wineries, hotels/resorts, enterprise groups, pop-ups/breweries/distilleries.
- Business model: "one flat rate and don't charge cover fees."
- Consumer site (exploretock.com): search by reservation type (Dine in / Pickup / Delivery / Events / Wineries), date, time, party size (1–20); discovery surfaces (collections, trending, new & notable); iOS app. Banner: "Tock is now part of the Resy network."

### ResOS (evidence layer A)

- Positioning: "Resos is commission-free reservation software: an online booking and table-management system for restaurants, cafés, bars, and pubs. Take bookings directly from your website, social media and Reserve with Google. Run every service from one shared table management system."
- Product UI (documented in marketing screenshots): bookings listed with time, name, party size, table(s), and status — Accepted / Seated; pending bookings show Accept / Decline actions; floor-plan view shows tables (numbered, with capacity ranges such as 1-2, 1-4, 1-6, 1-8), current occupant, and "Next:" seating times; calendar view shows per-day booking and people counts; Booking/Walk-in toggle; an "Optimize" view.
- Setup: "Add your opening hours, areas, and floor plan using our easy drag-and-drop editor."
- Booking page: widget code snippet for any website builder (WordPress, Squarespace, Wix, custom); booking link for Instagram bio/Facebook/WhatsApp; Reserve with Google ("Reserve" button in Search/Maps; "Availability syncs automatically… No double-bookings"); custom design; 14 languages with automatic browser-language detection.
- Table management: visual floor plans with drag-and-drop; "Multiple areas and rooms — manage your terrace, dining room, and private room separately – each with its own capacity and rules"; see which tables are finishing up.
- Booking overview: calendar/list/floor-plan views; search by name, date, or booking number; rebook/edit with automatic guest notification; print and share daily reports.
- Automations: automatic booking confirmations; scheduled reminders where guests confirm, cancel, or reschedule; **auto or manual accept** ("Accept every booking automatically, or review each one before confirming"); **overbooking warnings** ("Resos flags potential overbookings before they happen").
- Reminders: email confirmations; SMS reminders; re-confirm links ("Guests who click confirm their spot – those who don't free it up for the waitlist").
- Revenue protection: deposits at booking (fixed amount or percentage per guest; rules by group size, weekend, event); no-show fees charged automatically to the card on file (per person or per booking; policy shown during booking); repeat no-show recognition; card-on-file capture during booking.
- Waitlist: when fully booked, guests join from the booking page/widget (staff can add manually); on a cancellation the operator chooses which waitlisted party gets the opening and the system converts the entry into a booking with confirmation.
- Guest chat: a message thread per booking; special requests (birthday cake, high chair, window seat) stay attached to the booking.
- Reviews: automated post-visit follow-up; positive feedback channeled to Google/TripAdvisor; low ratings routed to the operator's inbox.
- Reports: peak hour/day insights; booking-channel tracking (website, Google, social, walk-ins); table-turnover data.
- Custom fields: allergies, occasions, seating preferences collected at booking.
- Multi-location: one account, per-location hours/tables/booking rules. Data export/import (CSV). Add-ons (paid): Reserve with Google, custom design, online payments (prepayments/deposits/no-show fees), SMS, custom fields, waitlist, marketing & analytics, multiple locations, API, Facebook/Instagram booking, experiences ("Run paid events alongside your regular bookings – wine tastings, supper clubs, private dinners. Set the price, the seats, and the dates, and take payment up front").
- Pricing: tiers by bookings/month (free 25 → unlimited); "No contract. No commission. No cover fees." Publishes a "No-Show Index" benchmarking recorded no-show rates across millions of reservations.

### Tablein (evidence layer A)

- Positioning: "Table booking system for smart restaurants… Boost sales, enhance customer service, and minimize no-shows." Three-part framing: "Digital reservation book for the team / Online reservations for your clients / Data and reports for the manager."
- Explicit paper-book replacement: "Change the paper reservation book to a modern online tool… Everyone on your team can access and make real-time updates from any device… Your reservation data is stored securely in the cloud. Say goodbye to paper reservations!"
- Widget: "Easily add the reservation widget on your website, allowing visitors to book directly from your site, even when you're closed. Increase your bookings from Google, Facebook, Instagram, or even the Michelin Guide. Provide instant booking confirmations… Reduce no-shows with automated reminder messages or ask a deposit for bookings."
- Feature groups: Get & Manage reservations (digital reservation book, multichannel online reservations, seamless reservation management); Market & Grow (experiences/discounts/events, no-show fees/payments/deposits, website builder and food menus); Analyse & Improve (dashboards/reports, guest database and management, feedback management).
- Solutions: individual restaurants, restaurant groups, hotel restaurants, bars/pubs/clubs, events/weddings/catering, membership clubs.

## Cross-product Comparison

| Dimension | SevenRooms | Tock | ResOS | Tablein |
|---|---|---|---|---|
| Self-label | "restaurant reservation system" / guest-experience platform | "reservation platform" for hospitality | "commission-free reservation software: online booking and table-management" | "table booking system" / "digital reservation book" |
| Guest-facing booking surface | branded widgets on the restaurant's site + channel integrations | consumer app + business booking pages | booking widget + hosted booking page + link | reservation widget + hosted page |
| External booking channels | Google, DoorDash Reservations, Facebook, Instagram, TikTok, discovery partners (Capital One Dining, Chope, OpenRice, Tripadvisor, Dorsia) | own consumer app/discovery; POS and partner integrations | Reserve with Google, Facebook/Instagram (add-ons) | Google, Facebook, Instagram, Michelin Guide |
| Reservation record | party + date/time + table + guest data (birthday, dietary, preferences) + add-ons + payments | reservation/experience/event booking with prepaid terms | time, name, party size, table(s), status, notes/custom fields, message thread | booking with guest data, deposits, custom requests |
| Capacity model | floor plan, AI seating, pacing controls, cover forecasting | flexible floor plans, table & service management | floor plan (drag-and-drop), areas/rooms with own capacity and rules, tables with capacity ranges | "configure restaurant wisely to seat more clients, eliminate empty time slots" |
| Service schedule | shift/grid planning, pre-shift reports | service management | opening hours, booking schedule/limits, per-day calendar | opening hours; bookings accepted "even when your restaurant is closed" |
| Confirmation semantics | automated confirmations; card holds on high-demand slots | instant or request ("reservation request waitlist") | auto or manual accept (Accept/Decline); overbooking warnings | instant confirmations "without having to wait for manual approval" |
| Waitlist | virtual waitlist, QR/Google Reserve joining, priority alerts, conversion | waitlist module; reservation request waitlist | waitlist add-on; operator converts a waitlisted party into a booking | waitlist within booking system |
| No-show protection | credit card holds, cancellation fees, priority alerts | deposits, credit card holds, prepayment, customizable cancellation policies | deposits (fixed/percent), no-show fees to card on file, repeat no-show recognition | no-show fees, payments, deposits |
| Guest profiles | 360° profiles, auto-tags, spend via 65+ POS integrations, cross-property | guest data ownership, guest management | guest profiles, guest database and search | guest database and management |
| During service | table status (operator-definable), real-time spend, seating algorithm, SMS line | table & service management | statuses Accepted/Seated, drag bookings between tables, "Next:" times | digital book for the team during service |
| Communications | pre-arrival reminders, two-way SMS, post-dining surveys | 2-way SMS, customizable communications | confirmations, reminders, re-confirm links, per-booking chat | confirmations, reminders, email/chat replies, notifications |
| POS integration | 65+ POS integrations, spend attached to profiles | Toast, WineDirect, Commerce7, Tripleseat, Upserve | via Zapier/API (POS named as connectable) | not emphasized on fetched pages |
| Events/experiences | events, experiences, add-ons, ticketed events | experiences, events (complete event ticketing system) | Experiences add-on (paid events, prepaid tickets) | experiences, discounts, events; events/weddings/catering solution |
| Multi-location | portfolio availability, cross-venue selling, shared profiles | enterprise groups | multiple locations add-on (per-location rules) | restaurant groups solution |
| Reporting | reservation/waitlist trends, group reporting | guest data & reports | peak hours, channel tracking, table turnover | dashboards and reports for the manager |
| Business model | commission-free covers (vs cover-fee networks) | flat rate, no cover fees | free tier + paid add-ons, no commission/cover fees | subscription; paper-book replacement framing |

### What is universal (B-layer, all 4 sampled)

1. **The reservation (booking) is the unit of record**: an identified party (named guest + party size) committed to a seating at a specific date and time, held in a persistent book with a working state (accepted/confirmed, seated, cancelled, no-show all appear as named states or events across the sample).
2. **Capacity-gated availability**: bookings are accepted against the restaurant's seating inventory (tables, areas/rooms, floor plan) and its service schedule (opening/service hours, booking slots/limits); the system prevents or warns about overbooking (ResOS overbooking warnings; Google-sync "no double-bookings"; Tablein "eliminate empty time slots" configuration).
3. **A guest-facing booking path operated by the platform**: widget on the restaurant's website, hosted booking page, and/or third-party booking channels (Google, social, discovery networks) — guests initiate bookings against live availability without staff mediation; confirmation may be instant or staff-reviewed (both modes documented).
4. **The book is shared by the whole front-of-house team** and is the operational surface before and during service (digital reservation book framing at Tablein; host-stand view at SevenRooms; shared table-management system at ResOS).
5. **No-show is the central economic risk**, addressed with deposits, card holds, no-show fees, cancellation policies, reminders, and waitlist backfill — present in all four with different depth.

### What is common but not definitional

- Guest profiles/database with visit history, preferences, tags; spend data via POS integration (deep at SevenRooms/Tock; lighter at ResOS/Tablein).
- Automated communications: confirmations, reminders, two-way SMS/chat, post-visit feedback/review collection.
- Waitlist for walk-ins and fully-booked periods, with conversion into bookings.
- Table management during service: seating, table status, turn/pacing optimization (AI seating is era-current).
- Reporting: covers, channels, turnover, no-show rates.
- Events/experiences as bookable, often prepaid, offerings alongside standard reservations.
- Multi-location/portfolio management.
- POS integration (depth varies; ResOS treats it as connectable rather than native).
- Multi-language booking pages.

### Vendor-specific (L3 — stays here)

- SevenRooms: Auto-tags, Priority Alerts, Perks, Private Line, Voice AI, Revenue Management, Channel Connect; "a DoorDash company"; DoorDash Reservations as a channel; 65+ POS integrations claim; AI seating "10,000+ combinations" claim.
- Tock: flat rate/no cover fees positioning; "reservation request waitlist" as a plan feature; Product Advisory Council; consumer app discovery collections; "now part of the Resy network" banner; winery/hotel vertical packaging.
- ResOS: add-on pricing structure (Reserve with Google €7.99/mo etc.), bookings/month plan tiers, No-Show Index benchmark, 90-day money-back guarantee, "Optimize" view.
- Tablein: website builder and food menus as bundled features; Michelin Guide as a booking channel; Investopedia "Best Booking System 2023" badge; version 3.0 beta.

## Canonical Abstraction

### L0 — Defining Invariant (three jointly-held structures)

1. **The reservation as the unit of record.** A persistent, individually identified commitment binding a named party (guest + party size) to a seating at a specific date and time at the restaurant, carrying its own state through service (requested/confirmed → seated → completed, with cancelled and no-show as named outcomes). Remove → a table map or waitlist with no bookings, or a guest database with nothing booked.
2. **Capacity-gated availability.** The restaurant's seating inventory (tables and areas, commonly held as a floor plan) and its service schedule (service hours, bookable slots/limits) define the availability against which bookings are accepted; the system gates new bookings against that capacity (slot limits, overbooking warnings/double-booking prevention). Remove → a booking form that never checks availability (generic form builder) or a capacity planner with nothing booked.
3. **The guest-facing booking path.** Guests initiate reservations through a platform-operated booking surface — an embeddable widget, a hosted booking page, and/or third-party booking channels (search, social, discovery networks) — against live availability, without staff mediation for the booking act itself; confirmation may be instant or staff-reviewed. Remove → phone-only reservations entered by staff into a book (the paper-book lineage: a host tool, not a platform).

Jointly-held load-bearing tests:

- 1 alone = a list of bookings (diary/spreadsheet)
- 2 without 1 = floor plan / capacity planner with nothing booked
- 3 without 1+2 = a contact form
- 1+2 without 3 = a staff-entered digital book (digitized paper book) — a host tool below the platform bar
- 1+3 without 2 = booking requests with no capacity model (form-builder territory)
- 2+3 without 1 = availability display with no reservation record

### L1 — Common Mature Structure

- guest profiles/database: visit history, preferences, tags, dietary notes; spend attached via POS integration in deeper products
- automated communications: confirmations, pre-arrival reminders, re-confirm requests, two-way SMS/chat, post-visit feedback/review collection
- waitlist for walk-ins and fully-booked periods, with conversion of waitlisted parties into bookings
- no-show protection: deposits, card-on-file holds, automatic no-show fees, cancellation policies
- table management during service: seating, operator-definable table statuses, turn/pacing management
- reporting: covers, booking channels, table turnover, no-show rates
- events/experiences as bookable (commonly prepaid) offerings alongside standard reservations
- multi-location management with per-location rules
- multi-language booking surfaces

### L2 — Variant / Optional Structure

- channel mix: direct-first (own widget/page, commission-free philosophy) vs network-first (consumer app/discovery network) vs channel-aggregating (Google/social/marketplace/discovery partners) — a product-philosophy axis, not a Type boundary
- confirmation semantics: instant confirmation vs request-to-confirm (staff review)
- prepaid/ticketed bookings and experiences/events (straddles toward Event Registration/Ticketing machinery)
- booking scope beyond dine-in tables: pickup/delivery time slots, winery tastings, hotel restaurant service, private dining, membership clubs
- AI-era machinery: algorithmic seating/pacing, predictive waitlists, voice-AI call answering, automated marketing journeys
- vertical breadth: restaurants, bars/pubs/clubs, wineries, hotels, casinos/groups

### L3 — Vendor-specific

See Vendor-specific list above; none of it enters the canonical document.

## Historical / Market-Sample Check

- **The paper reservation book + phone reservations** (the documented predecessor): a host records phoned-in reservations in a book against table availability and service hours. It satisfies structures 1 and 2 but fails 3 (no guest-facing platform surface) — held as the conceptual ancestor, not the Type. Tablein's own marketing ("Change the paper reservation book to a modern online tool") documents this lineage explicitly. A staff-entered digital book without a guest-facing path (1+2 without 3) is a host tool below the platform bar. ✓
- **Early network-generation products** (the late-1990s electronic reservation book paired with a consumer network): restaurant-side book + guest-facing network booking — satisfies all three legs. Not directly fetched (sourcing limitation); held conceptually, no specifics asserted. ✓ (low confidence, no details claimed)
- **Regional products and channel ecosystems** (European SMB tools; Asian/global discovery channels such as Chope/OpenRice named by sampled vendors): fit the definition — channel mix is a variant axis, not the definition. ✓
- **Prepaid/ticketed reservation regimes** (deposits-first fine dining): fit — deposits/no-show fees are L1 machinery, not definition. ✓
- Conclusion: the definition is not over-fitted to the modern network-app era; the guest-facing booking path is the platform's defining act, while the specific surfaces (widget vs app vs channels) are implementations.

## Boundary Findings

1. **vs Restaurant POS** — the POS is the staff-mediated transaction surface during service (order → check → payment); the reservation platform commits seating before service and manages the book through it. Covers and guest data flow from the book into the POS (SevenRooms attaches POS spend to profiles; Tock integrates with Toast). Removal test: remove the transaction machinery → the reservation platform stands; remove the book → the POS stands. The two are commonly bundled in suites but are different objects.
2. **vs Restaurant Online Ordering** — ratified from the ordering side: "Reservations commit a table at a time; ordering composes food for fulfillment." Some products bundle both (booking with food pre-orders/deposits) — different objects, different workflows. Blur zone: time-slot bookings for pickup/delivery (Tock's consumer site lists Pickup/Delivery as reservation types) — the object is still a slot commitment, not a composed food order; when food composition begins, the product is in ordering territory.
3. **vs Appointment Scheduling Application** — both book a time. The seam is the capacity object and its semantics: appointment scheduling binds a person to a provider's calendar slot; the reservation platform binds a party to the restaurant's seating inventory (tables/areas/floor plan, party sizes, turns, service periods) with covers as the counted unit. Restaurant-specific machinery (floor plan, covers, no-show economics, service-stage table management) has no appointment-scheduling analog. Removal test: replace tables/covers with a provider's calendar slots → appointment scheduling.
4. **vs Event Registration Platform / Event Ticketing** — events are discrete dated occurrences with ticket inventory; reservations are per-service-time seating commitments recurring across the calendar. The straddle is real and productized: experiences/events modules (Tock Events "a complete event ticketing system", SevenRooms Events/Experiences, ResOS Experiences add-on, Tablein events/weddings) ride the reservation platform's booking and payment machinery. When ticketed discrete events become the center, the product is in event territory.
5. **vs Amenity Booking Platform** — amenity booking commits shared facility resources (courts, pools, rooms) for residents/members of a property; the reservation platform commits restaurant seating for diners under service semantics. Different domain objects and different operating context (host stand vs property management).
6. **vs Hotel PMS** — the PMS's unit is the room/stay with folio; the reservation platform's unit is the table/meal service. Hotel restaurants are a served segment (SevenRooms hotels vertical, Tablein hotel-restaurants solution) — the reservation platform operates beside the PMS, not as it.
7. **vs Review Platform / diner-facing discovery networks** — the network pole (consumer app, search, reviews, loyalty) is the acquisition layer that feeds the book; the book is the Type's center. Sampled vendors document this explicitly: SevenRooms "pull them into a single reservation book and track your most effective channels." The discovery surface without the book (a review/directory platform with a booking button handed to a third party) is not this Type.
8. **vs Waitlist management** — the waitlist is a module of this Type (walk-ins and full-booked periods), not a separate Type; a waitlist-only tool with no reservations sits below the Type's bar.
9. **vs CRM** — the guest database is a module grown from the book (every booking feeds the profile); the reservation remains the unit of record. A CRM without the book/capacity model is Customer CRM territory, not this Type.

## Uncertainties

- **Network-pole sourcing limitation**: OpenTable and Resy — the two largest diner-facing reservation networks — were unreachable from the research environment (timeouts/401/transport errors/empty app shell), as was Yelp's product page and the Internet Archive retry. The network/channel layer is therefore evidenced only through restaurant-side channel-integration pages (SevenRooms booking channels, ResOS Reserve with Google, Tablein's Google/Facebook/Michelin channels) and Tock's consumer site. Network-side mechanics (diner loyalty programs, network pricing/cover-fee models, diner profile portability) are NOT asserted anywhere in the canonical document.
- Help-center-level operational documentation was not reachable for any sampled product (SevenRooms help center login-walled; others not fetched before stop conditions were met). Evidence is product-page strength: lifecycle state names, rule parameters, and default behaviors are stated at conceptual level only.
- Exact reservation lifecycle state vocabularies vary by product (Accepted/Seated observed at ResOS; cancellations/no-shows as named events at SevenRooms; request states at Tock). The canonical lifecycle is asserted conceptually; exact labels are not claimed as industry standard.
- Numeric parameters (deposit amounts, reminder timing, party-size limits, slot intervals) are deliberately not asserted — no fetched source supports precise values, and ResOS's published no-show benchmark is a marketing statistic, not an operational rule.
- Whether "reservation request waitlist" (Tock's plan feature) is a common pattern or Tock-specific: held as variant; only one sampled product names it.
- POS-integration depth varies from native (SevenRooms 65+ integrations claim) to connectable (ResOS via API/Zapier); the canonical document treats POS integration as common capability, not definition.

## Final Synthesis

A Restaurant Reservation Platform is the restaurant's reservation book as a live system of record. Its defining core is three jointly-held structures: the reservation as the unit of record (a named party committed to a seating at a date and time, advancing through a service lifecycle); capacity-gated availability (the seating inventory and service schedule against which bookings are accepted, with overbooking guarded); and the guest-facing booking path (widget, hosted page, or third-party channels through which guests initiate bookings against live availability, with instant or reviewed confirmation). Everything else — guest profiles and CRM, automated communications, waitlists, deposits and no-show fees, service-stage table management, reporting, events/experiences, multi-location governance, AI seating — is common mature structure or variant capability, not definition. The Type sits between the transaction surface beside it (Restaurant POS), the food-composition channel it is often bundled with (Restaurant Online Ordering), the generic time-booking Type it must not be dissolved into (Appointment Scheduling), the ticketed-event machinery it partially carries (Event Registration/Ticketing), and the diner-facing discovery networks that feed it without being it.
