# Research Notes — Reserved Seating Platform

## Research Goal

Determine what "Reserved Seating Platform" is as a directory leaf: whether the seat map constitutes a distinct Application Type (the seat map as the primary managed object of a product family), or whether reserved seating is a capability mode inside event ticketing — and document the seat-level inventory layer either way.

This pass must discharge the joint-review flag left by the event-ticketing-platform pass (2026-09-07): "reserved-seating-platform (seat map as primary managed object vs capability mode inside event ticketing — all four sampled products implement reserved seating as a mode)."

## Initial Boundary

- Leaf: Reserved Seating Platform (§26 Travel, Hospitality, Food Service & Events; listed between Event Ticketing Platform and Ticket Inventory Management).
- Working hypothesis: reserved seating = selling admission to specific, assigned seats rather than to an event at large. The seat map (chart of sections/rows/seats) is the inventory structure; the seat is the sellable unit.
- Nearest neighbors: Event Ticketing Platform (the selling system this capability lives inside — the flagged boundary counterparty), Ticket Inventory Management (allocation/holds discipline), Ticket Resale Marketplace (secondary market), Attraction Ticketing / Attraction Management System (place-admission inventory, processed), Cinema Management System (§27, unprocessed — every ticket is a seat), Venue Management System (unprocessed — spaces vs seats), Airline Reservation / PSS (processed — seat selection in another domain), event-planner seating-chart tools (market adjacency, no directory leaf).
- Known unknowns at start: does a standalone end-to-end reserved-seating product family exist? Is the seat map ever the primary managed object of a whole product? What form does the seat-map layer take when factored out of ticketing? How do verticals (arts subscriptions, sports season seats, cinema) realize seat rights?

## Research Questions

1. What objects does the seat-level layer consist of (chart, sections, rows, seats, tables, pods, areas)?
2. What states does a seat carry, and who changes them?
3. How does seat-level allocation work (buyer selection vs best-available)?
4. How does per-seat pricing work (tiers/price bands mapped to seats)?
5. What do holds look like at seat grain (private holds, pool/group holds, locks, not-for-sale)?
6. How does the seat map relate to the event (one chart, many events; seasons)?
7. What does the issued ticket carry (seat identity)?
8. Is there a standalone product whose center is the seat map? Platform or component?
9. How do verticals realize seat rights across event series (seasons, subscriptions, fixed series)?
10. Where is the boundary vs Event Ticketing Platform — does the candidate split hold?

## Representative Products

Selected for market representation, documentation completeness, and distinct product poles:

- **Seats.io** — the seat-map-as-product pole: a dedicated seating-chart component (designer + renderer + seat-state API) sold to ticketing platforms. The purest test of "seat map as primary managed object."
- **Eventbrite** — self-serve ticketing platform; reserved seating as a named feature (mode pole, marketplace distribution).
- **TicketSpice (Webconnex)** — self-serve ticketing platform with a dedicated reserved-seating feature page (mode pole, own-channel).
- **Tessitura** — arts & culture platform: seated events + subscriptions with seat rights (vertical depth pole, arts).
- **Paciolan** — college athletics / performing arts / arenas ticketing suite (vertical depth pole, sports).

Plus **Spektrix** observations carried from the event-ticketing-platform pass (2026-09-07, Tier-1 support-centre evidence, same research program) — used as cross-product corroboration, not re-fetched.

## Sources

Research date: **2026-09-09**

- Seats.io — homepage, features page, support centre (Intercom): What is Seats.io?; How does it work?; What is an Event?; Season tickets and multi-day events; collection index. https://www.seats.io/ , https://www.seats.io/features , https://support.seats.io/en/articles/2007394-what-is-seats-io , https://support.seats.io/en/articles/2069669-how-does-it-work , https://support.seats.io/en/articles/2096454-what-is-an-event , https://support.seats.io/en/articles/2096431-season-tickets-and-multi-day-events , https://support.seats.io/en/collections/1174675-getting-started
- Eventbrite — organizer feature page "Reserved Seating": https://www.eventbrite.com/organizer/features/reserved-seating/
- TicketSpice — homepage and dedicated reserved-seating feature page: https://www.ticketspice.com/ , https://www.ticketspice.com/features/reserved-seating-event-ticketing-system
- Tessitura — homepage and Ticketing & Admissions feature page: https://www.tessitura.com/ , https://www.tessitura.com/features/ticketing-admissions
- Paciolan — homepage and Ticketing solutions page: https://www.paciolan.com/ , https://www.paciolan.com/ticketing-solutions
- Spektrix — carried from research/event-ticketing-platform.md (2026-09-07, Tier-1 support centre).
- research/event-ticketing-platform.md — the flagged counterparty pass (Boundary Findings §7).

Source-access limitations:
- docs.seats.io is a JS-rendered app (root fetch returned only the title); the Intercom support centre was used instead — Tier-1 support articles were reachable.
- ThunderTix (self-serve theater pole candidate): 403 — abandoned after one attempt.
- SimpleTix: root and /support/ both 404 — abandoned.
- SeatAdvisor (candidate second seat-map component vendor): 403 — abandoned after one attempt; the component-layer population beyond Seats.io is therefore unverified.
- Tessitura and Paciolan help-centre/community documentation is behind login; evidence for both is product-page level (Tier 2). No operational specifics asserted from them.
- Ticketmaster organizer-side tooling not publicly documented (carried limitation from the ticketing pass); no organizer-side claims.

## Product Observations

### Seats.io — evidence layer A (Tier 1 support centre + Tier 2 product pages)

- Self-positioning: "The ultimate seating chart solution. For ticketing technology companies and venue owners. We make reserved seating easy." Homepage: "Integrate seating charts into your platform in days."
- "What is Seats.io?": "a set of tools that allows online ticketing platforms to add reserved seating capabilities to their offering. In short, you can: 1. simply design floor plans of any shape and size; 2. embed them in your ticketing pages, so that ticket buyers can select their seats on a beautiful, interactive and mobile-friendly seat map; 3. manage availability in realtime, using the seats.io API." **"Note: Our tools are meant to be integrated into an existing ticketing platform: Seats.io itself does not offer any ticketing or payment capabilities."**
- Product structure (features page): **Floor plan designer** (draw any venue — theaters, stadiums, race tracks, gala dinners, comedy clubs, dance floors; white-label embed so platforms can let their customers draw charts inside their app; "Scan a chart" — turn a floor plan image into an interactive chart; validation to catch mistakes and prevent double bookings; colorblind-safe palettes; **Areas for general admission or fixed occupancy; Tables bookable by seat or as a whole**) + **Floor plan renderer** (buyer-facing interactive chart, mobile and desktop) + seat-state management.
- "How does it work?" (integration steps): 1. Design your floor plan (in-browser Designer, point/click/drag). 2. Create an event — "An event is what Seats uses to keep track of seat availability. You can create multiple events for a single seating chart. This allows you to re-use the same floor plan for multiple events." 3. Render the floor plan (embed chart.js in a div). 4. Let buyers select and book — client-side selection; server-side status-change API call ("typically /book"); "Whenever you update availability for a seat, seats.io will push this update out to every other ticket buyer that has the floor plan open for that given event… they'll see seats become unavailable in realtime." Best-available automatic assignment is optional ("Seats can automatically assign the best available seats too; you don't have to let your ticket buyers select their spot").
- "What is an Event?": "If you sell the seats in a venue one time, that's what we call an event. So an event is a single performance of a show, a single football match or a single concert. A group of events is what we call a season."
- Season tickets and multi-day events: two mechanisms — **seasons** (fixed event set, e.g. a club's home games: season pass holders buy a single seat for the whole season; "Seats that are sold on the season level are made unavailable for individual events. And vice-versa: if a seat is sold on at least one event, it's not available for the season") and **event groups** (buyer-specific event lists, e.g. multi-day combos; all-or-nothing booking across the list; all events must share one chart).
- Seat-picking machinery (features page): best available ("Automatically suggest or assign the best available seats"); "No single empty seats" (occupancy optimization when buyers pick their own); "Hold seats. Seats are held for the ticket buyer while making a selection, until they are booked or time out"; "Avoid double bookings. Real-time updates ensure only one ticket buyer can hold or book a unique place"; view-from-seat.
- Organize machinery: live bookings across multiple events; **workspaces** ("Serve multiple customers in isolated environments"); **Not For Sale** ("Disable seats. Hide sections or entire floors. Increase availability gradually to ticket buyers"); **Resale** ("Put booked seats up for sale again, with unique price tags").
- Scale claims (marketing, recorded not asserted): 7M+ seats booked monthly; 200M+ yearly impressions; 70% bookings on mobile; 3M+ events gone live; 99.99% uptime claim.

### Eventbrite — evidence layer A (Tier 2 feature page)

- "Reserved Seating Software for Your Events" — a named feature page under the organizer "Event Creation" feature family (alongside Event Page Builder, Event Registration, Event Payments, Timed Entry Ticketing, Sell Tickets Online).
- "Reserved seating software enables event creators to sell tickets for specific, assigned seats. With an event seating chart maker, you can design custom layouts for your venue, offer tiered pricing for premium spots, and provide attendees with an interactive, shoppable map for a seamless checkout experience."
- Seating chart maker: drag-and-drop; ticket tiers; sections, rows, and tables from a template.
- Venue Maps: "clickable, shoppable floor plans"; "add reserved ticketed areas like sections or tables, include objects like stages or bars, and add custom text."
- Selling order: "Our technology automatically sells the best available reserved seats first, but you can customize your layout and charge more for different seating areas to maximize your return."
- FAQ topics: how to create a reserved seating event; how to use venue maps; choosing a layout; chart size; managing the event after launch.
- Cross-pass corroboration (event-ticketing-platform pass, 2026-09-07, Tier-1 help centre): reserved seating management in event setup; "venue map for reserved seating" in the create-event flow; assigned seating with custom charts, legends, stage photos from seats, handicap/wheelchair icons.

### TicketSpice — evidence layer A (Tier 2 feature page)

- Reserved Seating is a named top-level feature: "Create seating charts, layouts, and pods"; "Design seating arrangements, layouts, and pods to match the unique setup of your event."
- Interactive seating chart builder: "Create your own seating chart in minutes using our simple web interface… our drag and drop reserved seating chart creator helps you recreate your venue to near perfection. Mix reserved seating with open general admission areas. Add VIP tables and build in social distancing pods… No matter how complex or crazy the seat naming is, you can customize every row and seat assignment easily."
- Pricing tiers: "customizing your pricing tiers for any selection of seats within a section. Set senior, student, child, and veteran price points for a given seat with ease. And should you desire to control the selling order, TicketSpice's reserved seating sales platform lets you control how seats are sold and in which order." ("Set unlimited pricing tiers and assign them to any seat, row, or section in the venue.")
- Seat view preview: "upload seat view images from any section so that ticket buyers know what to expect."
- Seat holds: "hold back any number of seats with a special link that lets your guest instantly reserve them. Set an expiration date for when the hold gets released back to the public."
- Pool holds (groups): "define a set of seats, rows, or sections which will only be available to members of the group. Using a special link, each member of the group can select their seat within the allocation ensuring they will be seated next to other members of their group."
- Tables and PODs: "Create table seating layouts or pods with just a few clicks… Mix reserved seating with PODs, tables, and general admission to let buyers choose their event experience. PODs layouts are designed to honor any social distancing guidelines so that members of the same party or household are seated together. When PODs are used, the buyer will be required purchase all seats within the pod."
- Mobile: "From finding the best available seats to hand selecting seats in a particular section…"
- Framing on the same page: "Reserved seating is just one reason why TicketSpice is the best event ticketing platform on the market today."

### Tessitura — evidence layer A (Tier 2 feature pages)

- Positioning: "ONE PLATFORM built to run your whole arts & culture organization" — CRM, Ticketing & Admissions, Fundraising, Memberships, Marketing, Education, Digital & E-commerce, Reporting.
- Event Ticketing: "From intimate cabarets to sold-out arenas, historic houses to flexible black-box spaces, Tessitura lets you manage any seated and capacity-controlled venue." "Building blocks to manage capacity and seating in any space with no limitation on the number of maps you can create." Select-your-own seat map with legend (screenshot: "select your own seat map with legend"). "Define the best seating for your venue and different kinds of programming. Then Tessitura can automatically find the best seat at your patron's price point." "Take advantage of pod seating, not-for-sale seat indicators, and other features to enable physically distanced seating." Member/donor presales and exclusive inventory.
- Subscriptions & Renewals: "Renewable seated subscriptions in single or multiple venues"; "Patrons can keep 'their seats' for every performance or combine assigned seats with general admission events"; "Calculate suggested contributions to include in your renewal notices"; "Automatically release unrenewed seats on your timeline, or release them one by one as needed."
- Also carries General & Timed Admission (daily admission, timed entry, capacity for time blocks) — dual inventory models (seated events + place admission) on one platform, consistent with the arts/culture dual nature recorded by the attraction pass.

### Paciolan — evidence layer A (Tier 2 product pages)

- Positioning: "ticketing, fundraising, marketing solutions, and customer engagement" for college athletics ("#1 TICKETING PROVIDER IN COLLEGE ATHLETICS", "over 160 college clients"), performing arts, arenas & pro sports; "over 500 live entertainment organizations… more than 120 million tickets" (vendor claims, recorded not asserted).
- Ticketing page: "Pack the House — Make every seat count. Our features include dynamic capabilities that respond to market demand." "Discover Seats — Our interactive seat map ensures they get the best seat for the right price." Fan account: "your fans and patrons can easily transfer, sell, renew, and manage their own digital tickets." Mobile delivery (text/wallet).
- Customer quote (Kansas Athletics, Associate Athletics Director): "Seat-level pricing is a home run, especially when we're all pushing for revenue. I can't believe how easy it was to use. We can reprice multiple times daily to respond to how the inventory sells."

### Spektrix — evidence layer A (carried from the event-ticketing-platform pass, 2026-09-07, Tier 1 support centre)

- Seating plans: **Reserved** (visual seat map, one or more Areas), **Unreserved** (no map; customer picks quantity), **Multi-area** (mix). Overlays per instance: Layout Overlay (hide seats), Price Band Overlay (assign pricing level per seat; colors on reserved plans), Lock Overlay (locks = holds/kills on specific seats), plus seat attributes, view-from-seat, info overlay, best-available overlay.
- Fixed Series: buy tickets and hold seat rights across a series of instances.
- Order items carry seat location, seat number/row, barcode, printed/scanned state with scan history.

## Cross-product Comparison

| Dimension | Seats.io | Eventbrite | TicketSpice | Tessitura | Paciolan | Spektrix (prior pass) |
|---|---|---|---|---|---|---|
| Product form | component (designer + renderer + API) | ticketing platform feature | ticketing platform feature | arts platform module | ticketing suite module | ticketing platform capability |
| Chart design | dedicated Designer; white-label embed; scan-from-image; validation | seating chart maker; venue maps with objects | drag-and-drop builder; tables/pods; custom seat naming | building blocks; unlimited maps | interactive seat map (buyer side observed) | reserved/unreserved/multi-area plans |
| Seat states | available / held (timed) / booked; real-time push | shoppable map availability | holds with expiry; pool holds | not-for-sale indicators; pod seating | seat-level inventory, repriced | layout/price-band/lock overlays |
| Allocation | buyer selection or best-available | best-available first, then custom | best available or hand-pick | best seat at patron's price point | best seat for the right price | best-available overlay |
| Per-seat pricing | (pricing left to the embedding platform) | tiered pricing per area | tiers per seat/row/section; demographic price points; selling-order control | price points; dynamic pricing | seat-level pricing, repriced multiple times daily (customer quote) | price bands per seat via per-instance price list |
| Seat-bound entitlement | booking = seat state (ticketing left to platform) | reserved ticket | reserved ticket | seated subscription = seat across performances | transfer/sell/renew digital tickets | order items carry seat row/number |
| Multi-event seat rights | seasons; event groups | not observed | not observed | renewable seated subscriptions; release of unrenewed seats | season renewal (fan "renew") | fixed series |
| GA mixing | Areas for GA / fixed occupancy | sections/tables | mix reserved + GA + tables + pods | combine assigned seats with GA events | not observed | multi-area plans |
| Selling / checkout / payments | explicitly none ("does not offer any ticketing or payment capabilities") | yes | yes | yes | yes | yes |

Convergent observations (candidate common structure):

1. The seat-level machinery is remarkably consistent across all sampled products: chart design → seat states → allocation (selection or best-available) → per-seat pricing → seat-named entitlements. (B)
2. The layer never appears as a standalone end-to-end selling system. It is either a capability mode inside a ticketing platform (Eventbrite, TicketSpice, Tessitura, Paciolan, Spektrix — plus the ticketing pass's four products) or a component sold to such platforms (Seats.io). (B)
3. Seat-grain holds are universal machinery: private holds with expiry links, pool/group allocations, locks/kills, not-for-sale blocks, gradual release. (B)
4. Per-seat pricing (tiers/price bands mapped to seats; demographic price points per seat; dynamic seat repricing) is present across all poles. (B)
5. Multi-event seat rights (one seat held across a series — seasons, seated subscriptions, fixed series) appear in the arts/sports poles and the component pole; not observed in the self-serve poles. (B — variant)
6. Mixing reserved and unreserved areas in one map is supported across poles. (B)
7. Buyer-facing interactive maps (select-your-own-seat) with seat views are common mature structure. (B)

## Canonical Model

### L0 — Defining invariant of the seat-level layer

1. **The seat map as managed inventory** — a persistent, designed, seat-granular structure (sections/rows/seats; also tables, pods, and general-admission areas) with per-seat identity and states, maintained by the operator and reusable across events. Remove → capacity-count selling; the layer disappears.
2. **Seat-level allocation** — specific seats are assigned to specific buyers (interactive selection or best-available), with per-seat states driving availability. Remove → capacity selling; nothing is "reserved."
3. **Seat-bound entitlement** — the issued ticket names the specific seat (section/row/seat or table), and the seat is the unit of the commercial record. Remove → anonymous admission ticketing.

Historical / market-sample check: the paper-era box office satisfies all three — a printed house chart or seating plan, assigned seats written on tickets (row/seat), season-seat holders tracked on paper. Interactive shoppable maps, real-time availability push, hold links, pods, seat views, dynamic seat pricing are era machinery, not invariants. The layer's definition is era-independent.

### L1 — Common mature structure

- interactive chart design tools (drag-and-drop builders, templates, image scanning, validation)
- buyer-facing interactive/shoppable seat map (select-your-own-seat)
- best-available assignment (including price-point-aware best available)
- seat holds (private holds with expiry, pool/group allocations, locks/kills, not-for-sale, gradual release)
- per-seat pricing (tiers/price bands mapped to seats; demographic price points per seat)
- seat views (view-from-seat imagery)
- real-time availability updates
- seat attributes (accessible/wheelchair seating, restricted view)
- GA areas mixed with reserved areas; tables/pods as bookable objects (per-seat or whole-unit)

### L2 — Variant / optional structure

- multi-event seat rights (seasons, seated subscriptions, fixed series; renewal cycles; release of unrenewed seats)
- seat-level dynamic pricing / repricing
- seat-level resale (relist booked seats with new price tags; fan resale carrying seat identity)
- delivery form: built-in mode vs embeddable component (designer/renderer/API); white-label designer embedding
- pod / social-distancing layouts; whole-pod purchase rules
- multi-tenant workspaces (component pole)

### L3 — Vendor-specific structure (research notes only)

- Seats.io: hold tokens; chart.js embed; seasons vs event groups distinction; /book status-change endpoints; server SDKs (PHP/Java/Python/Ruby/.NET); workspaces; "no single empty seats" selection validator; scan-a-chart from image.
- TicketSpice: pool holds via special links with hold release date/time; pods require full-pod purchase; selling-order control.
- Tessitura: suggested contributions in subscription renewal notices; timeline-based or one-by-one release of unrenewed seats; unlimited seat maps as "building blocks."
- Paciolan: seat-level repricing "multiple times daily" (customer quote); fan-side transfer/sell/renew of digital tickets.
- Spektrix: per-instance overlay system (layout / price band / lock); price list matrix (ticket type × price band).
- Eventbrite: venue maps with non-seat objects (stages, bars); best-available-first selling order.

## Vendor-specific Findings

See L3. The most consequential vendor-specific fact is Seats.io's explicit boundary statement — the component pole exists precisely because the seat-map layer can be factored out of ticketing, and that vendor deliberately does not sell tickets or take payments.

## Boundary Findings

1. **vs Event Ticketing Platform — the flagged candidate split. DISCHARGED: the split does NOT hold as a full Type split.**
   - Reserved seating never appears without the ticketed event and the sale machinery around it. Every end-to-end product that sells assigned seats is an event ticketing platform (Eventbrite, TicketSpice, Tessitura, Paciolan, Spektrix — plus the ticketing pass's four samples).
   - The seat-map layer CAN be factored out — Seats.io proves it — but only as a component that explicitly does no selling ("Seats.io itself does not offer any ticketing or payment capabilities"). The component serves selling systems; it does not replace them.
   - Removal tests both ways: remove the seat map from a ticketing platform → it remains a full ticketing platform (general admission is first-class everywhere; the ticketing pass already recorded seat maps as NOT definitional). Remove the selling system from around the seat map → the seat map has nothing to allocate against (the component pole exists precisely to serve selling systems).
   - Verdict: Reserved Seating is the **seat-level inventory layer of event ticketing** — a real, structurally distinct layer with its own machinery (chart design, seat states, allocation, holds, per-seat pricing, seat rights) — realized in the market as (a) a capability mode inside ticketing platforms, (b) a dedicated embeddable component layer, (c) deep vertical machinery in arts/sports platforms (seated subscriptions, season renewals, seat-level dynamic pricing). It is NOT a standalone end-to-end Application Type. Recommend the leaf be treated as a capability-layer page documenting this layer; folding it into Event Ticketing Platform or keeping it as a documented layer page is a taxonomy-owner decision. No directory change made from this side.
2. **vs Attraction Ticketing / Attraction Management System (processed)**: place-admission capacity (day/time-slot tickets) vs seat-granular inventory; no seat map as primary unit there. Held; consistent with both prior passes.
3. **vs Cinema Management System (§27, unprocessed)**: cinema is the vertical where every ticket is a seat; seat allocation per screening is core there but inside the cinema system's own model (screenings, auditoria). Adjacent vertical; no claims made (leaf unprocessed).
4. **vs Airline Reservation / PSS (processed)**: seat selection exists there but inside fare/inventory/departure-control machinery; that pass already recorded the seam. Different Type.
5. **vs Venue Management System (unprocessed)**: venue booking/space management vs seat-level selling inventory; the seat map here is a selling asset, not a bookable space.
6. **vs event-planner seating-chart tools (AllSeated/Prismm/Social Tables class — no directory leaf)**: planner-side layout design for private events without selling/allocation to ticket buyers — a different software category observed in the market; recorded as adjacency, not a directory conflict.
7. **vs Ticket Inventory Management (unprocessed sibling)**: allocation/holds/on-sale discipline at ticket-type grain vs seat-granular map machinery; sibling slices of the same value chain. Flag stands for that pass.
8. **vs Ticket Resale Marketplace (unprocessed sibling)**: seat-level resale (relist booked seats; fan resale carrying seat identity) appears here as a capability; the marketplace Type centers the secondary market. Flag stands for that pass.

## Uncertainties

- Whether a second standalone seat-map component vendor exists: SeatAdvisor unreachable (403, one attempt); the component-layer population beyond Seats.io is unverified. The component-pole finding rests on one verified vendor (single-source for that pole; the pole's existence is nonetheless directly observed).
- Whether any venue operator uses Seats.io directly without a ticketing platform: positioning mentions "venue owners," but the product does no selling — direct use would be chart design only; unverified.
- Tessitura and Paciolan operational documentation is gated (community login); evidence for both is product-page level. No operational specifics asserted from them.
- Cinema pole not sampled (separate unprocessed leaf); the "every ticket is a seat" characterization is structural reasoning, not sampled evidence.
- Vendor scale claims (7M+ seats booked monthly; 120M tickets/year; 160+ college clients) are marketing numbers, recorded not asserted.
- Whether self-serve poles support multi-event seat rights (seasons) was not observed either way; recorded as "not observed," not "absent."

## Final Synthesis

The research discharges the event-ticketing-platform pass's joint-review flag: the candidate split does not hold as a full Type split. "Reserved Seating Platform" names the **seat-level inventory layer of event ticketing** — the seat map as a managed, stateful, reusable inventory structure; seat-level allocation of specific seats to specific buyers; seat-bound entitlements; and the machinery surrounding them (chart design, holds at seat grain, per-seat pricing, seat views, seat rights across event series). The market realizes this layer in three forms: as a capability mode inside ticketing platforms (universal — confirmed across nine products over two passes), as a dedicated embeddable component (Seats.io — verified, explicitly not a selling system), and as deep vertical machinery in arts/sports platforms (seated subscriptions, season renewals, seat-level dynamic pricing). No standalone end-to-end reserved-seating platform family was found. The layer's defining structure is era-independent (the paper box office satisfies it), and its machinery is remarkably consistent across all sampled products.
