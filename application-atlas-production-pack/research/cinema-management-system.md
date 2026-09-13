# Research Notes — Cinema Management System

## Research Goal

Understand what a Cinema Management System actually is from real products: the system a movie-theatre operator runs its business on. Determine the defining core (what makes it "cinema management" and not generic ticketing or POS), the standard capability ring, the boundaries against neighboring Types (event ticketing, reserved seating, attraction ticketing, restaurant POS, venue management, broadcast scheduling), and the relationship to the cinema-industry "Theatre Management System" (projection-control) family, which is a naming hazard for this leaf.

## Initial Boundary

Working hypothesis at start:

- A Cinema Management System is the operator-side business system for a film exhibitor: it schedules films into the operator's own auditoriums as dated sessions, sells admission to those sessions across staffed and self-service channels, sells concessions on the same operational spine, and settles box office with film distributors.
- Nearest neighbors: Event Ticketing Platform (sells dated admission too), Reserved Seating Platform (the seat-level layer), Attraction Ticketing (admission to a place), Restaurant POS (concessions), Venue Management System (bookable spaces), Broadcast Management System (schedules content), Cinema Scheduling Application (sibling leaf — the scheduling slice).
- Known naming hazard: in cinema-industry jargon, "Theatre Management System (TMS)" means the projection/content-control system (digital cinema servers, playlists, KDMs), NOT the business system. Vendors of that family: Unique X (RosettaBridge TMS / RosettaNet CMS), Qube, GDC, Dolby. The directory leaf is assumed to be the business system; this must be verified against how vendors self-describe.
- Pre-hung seam from the reserved-seating-platform pass (2026-09-09): "cinema is the vertical where every ticket is a seat; seat allocation lives inside the cinema system's own model of screens and screenings" — this pass must discharge it.

## Research Questions

1. What is the central object model? Is the scheduled session (showtime) the spine, and what hangs off it?
2. How does film programming/scheduling work in real products (film records, session composition, publishing)?
3. How does ticket selling work (channels, ticket types, pricing machinery, seating modes)?
4. How deep does concessions/F&B go, and is it part of the same system?
5. What is the distributor-settlement (film hire / rental) machinery, and which products carry it?
6. What circuit/head-office structures exist for chains vs independents?
7. Where does the system end and the projection TMS begin? How do they integrate?
8. What varies by market segment (independent vs chain, reserved vs GA markets, drive-ins, dine-in)?
9. Historical check: would a paper-era or single-screen regional cinema's way of working still fit the definition?

## Representative Products

Selected for market position spread, documentation quality, and different product philosophies:

| Product | Position | Philosophy | Evidence layer |
|---|---|---|---|
| Vista (Vista Classic / Vista Cloud) | Global enterprise leader for chains; on-prem + cloud suite | Modular enterprise suite: Head Office + site operations + digital channels + BI | A (product pages + reachable help-centre articles) |
| Omniterm | North America, since 1978; independents to chains | POS-centric integrated all-in-one; Windows-based; hardware + software | A (product pages) |
| RTS (Ready Theater Systems) | US; independents, chains, drive-ins, dine-in, FECs | All features included in one package; operator-built selling screens | A (product pages) |
| Veezi (by Vista) | SaaS for independent cinemas | Cloud-first, self-serve, small-site tier | A (product pages) |

Boundary reference (not a sample of this Type): Unique X (RosettaBridge TMS / RosettaNet CMS) — the projection-operations family, used to establish the TMS boundary. Evidence A on vendor pages.

Rejected candidates: Gateway Ticketing "Galaxy" (attraction/amusement ticketing, NOT cinema — product-pollution trap avoided); Cinemark/Cinépolis (exhibitors, not software vendors); Arts Alliance Media (content services, migrating out per Cinépolis announcement).

## Sources

Research date: 2026-09-10. All sources fetched live this pass unless noted.

- Vista — Vista Classic product page (module catalog): https://vista.co/vista-classic
- Vista — Vista Cloud Product Guide: https://vista.co/cloud/product-guide (via search index)
- Vista Help Centre (Zendesk, reachable): https://help.vista.co/hc/en-nz
  - Films section: https://help.vista.co/hc/en-nz/sections/4408013935257-Films
  - Ticketing section: https://help.vista.co/hc/en-nz/sections/4408005502617-Ticketing
  - Article "Creating and publishing draft sessions in film manager": https://help.vista.co/hc/en-nz/articles/59102702457369
  - Article "Ticketing overview": https://help.vista.co/hc/en-nz/articles/6307256989337
  - Article "Calculating film hire": https://help.vista.co/hc/en-nz/articles/22877583573401
- Omniterm — Cinema Management Software (home): https://omniterm.com/
- Omniterm — Theatre Management: https://omniterm.com/theatre-management/
- Omniterm — Cinema POS: https://omniterm.com/cinema-pos/
- Omniterm — Cinema Ticketing Software: https://omniterm.com/cinema-ticketing-software/ (via search index)
- RTS — Cinema Point of Sale: https://www.rts-solutions.com/point-of-sale-1
- RTS — Operations: https://www.rts-solutions.com/operations-1
- RTS — Customer Experience: https://www.rts-solutions.com/customer-experience-1 (via search index)
- Veezi — home + features: https://veezi.com/ , https://www.veezi.com/features/cinema-management , https://www.veezi.com/features/film-programming
- Unique X (boundary reference) — RosettaNet CMS: https://uniquex.com/exhibitor-services/rosettanet/ ; Cinemark case study: https://uniquex.com/case_studies/cinemark/ ; Reel Cinemas Eco TMS news: https://uniquex.com/latest-news/reel-cinemas-uk-the-worlds-first-cinema-to-deploy-unique-xs-rosettabridge-eco-tms/ ; Cinépolis news: https://uniquex.com/latest-news/cinepolis-selects-uniquex/
- GoTab × RTS partnership press item (integration seam): https://gotab.com/latest/gotab-partners-with-ready-theatre-systems-to-unify-ticketing-and-dine-in-food-and-beverage-for-cinemas
- Prior passes relied on for boundaries: research/reserved-seating-platform.md + applications/reserved-seating-platform.md (2026-09-09); applications/event-ticketing-platform.md; applications/attraction-ticketing.md; applications/restaurant-pos.md; applications/venue-management-system.md

Galaxy Ticketing (galaxyticketing.com) was attempted as a fifth cinema sample; the fetch returned empty (1 failure) and was abandoned per the network rule. The sample stands at four products.

## Product A — Vista (Vista Classic / Vista Cloud)

### Key observations (evidence layer A unless noted)

**Self-positioning.** "Cinema management software" is Vista Group's own term for this product family; Vista Classic is the on-premise suite ("powering over 45,000 cinema screens worldwide" — vendor claim), Vista Cloud the next-generation cloud line. Vista also sells distributor-side (Maccs), box-office reporting (Numero), marketing/loyalty (Movio), and film-data distribution (movieXchange) — the exhibitor system is one ring of a wider film-industry group.

**Module catalog (Vista Classic page).** Experience: Web, Mobile, Kiosk, Digital Signage, Living Ticket, Loyalty, Subscriptions, CXM (personalization). Operations: Point of Sale, Cinema Manager, Cash Desk, Food & Beverage, Serve (in-auditorium ordering), InTouch (staff mobile app), Self-Scan (moviegoer self-scanning). Enterprise: Head Office, Horizon (BI), Film Manager, Cinema Intelligence (AI forecasting/scheduling), Group Sales, Vouchers & Gift Cards, movieXchange, Call Centre.

**Session scheduling workflow (help centre, Film Manager).** Sessions are created from a "film palette" in Draft mode; draft sessions are invisible to cinema managers; converting drafts to "Planned" and saving publishes them and makes them visible. Session status indicators (black dot, dotted border, status colour view). This documents a draft → planned → publish lifecycle with explicit visibility semantics.

**Showtime Manager.** A separate surface for per-session work: applying pricing rules to a session, applying ticket purchase rules to a session, changing views. Sessions are the object that pricing and purchase rules attach to.

**Film records.** Films section covers: film records with distributors; trailer and advertisement records; trailer scheduling; pre-show settings; marathons (multiple films under one session); prioritising films on digital sales channels; events (webpage) form. Film data (posters, trailers, ratings, synopses) is centrally stored and distributed to channels (Omniterm documents the same pattern independently).

**Pricing machinery (help centre, Ticketing overview).** Ticket types and ticket classes; price cards (base + derived, future versions, per-ticket-type prices, package ticket types, surcharges, minimum admission price); pricing rules (standard rules, pricing groups, ticket-type availability) applied in Showtime Manager per session; promotions/discounts/deals with selection lists; new-release price cards and surcharges; new-release period assigned to a film; area categories for uniquely priced seating; ticket fees and booking fees; restricting ticket types by day/time, by payment card, restricting swap/delete; movie format GL accounts (formats such as 3D priced via price cards rather than separate ticket types).

**Film hire / distributor settlement (help centre).** "Film hire is calculated and tracked for a given film, cinema, and week. A screen or film print can also be specified." Process: box office data uploaded to Head Office → film hire calculated (film hire records generated) → exported to financial reporting. Variables: Distribution Terms, Film Hire Contracts, House Costs and House Cost Exceptions (deducted before or included depending on terms), screen data. Net box office computed via "Formula Share" and "Minimum Distributor Share" algorithms; where both generate values, the higher is the Calculated Amount (product-specific detail). Film-hire contracts: creation in bulk, adjustment, payment terms; distributor invoices; film hire by ticket class; excluding zero-value tickets from calculations; Session Performance view for show-level data.

**Head Office.** "The hub of your cinema circuit": bulk operations across sites, cross-site sales/financial reports, film hire contract entry with automatic film-hire cost calculation, integrations for programming and stock.

**Sales channels.** POS (tickets + concessions, upsell-driven), Web (browsing + ticketing components, real-time updates from cinemas), Mobile (self-service refunds, in-seat delivery, loyalty), Kiosk (seat-first ordering, F&B, in-seat delivery), Call Centre (sell over phone, identify repeat customers), Group Sales (enquiry → quote → confirmation → self-service portal for group bookings/private screenings).

**Concessions/F&B.** Food & Beverage module: multiple F&B concepts at one site (self-service, lobby bar, restaurant, in-seat dining); kitchen communication; order status to guests; integrated with POS/Loyalty/Vouchers. Serve: mobile ordering for waitstaff in auditoriums.

**Admission control.** Self-Scan (moviegoers scan their own tickets), InTouch (staff scan tickets, look up seat maps, deliver food to seats).

## Product B — Omniterm

### Key observations (evidence layer A)

**Self-positioning.** "Cinema management software" / "our cinema management system"; solely dedicated to the cinema industry since 1978; thousands of screens in North America and worldwide (vendor claim); single-site independents to multi-location chains.

**Theatre Management features page.** Six named feature blocks:
- Centralized Management — taxes, employees, coupons, discounts, accounting, close-of-day from a single interface.
- Punch Clock — every station acts as a time clock; employees punch in / print schedules.
- Concessions Sales & Inventory — concession item menu, recipes, meals, combos, vendor management and purchasing.
- Reporting & Real-Time Data — detailed reporting, web-based sales monitoring, dashboard.
- Automated Film Settlement — "manage your relationships with distribution partners and calculate rental expenses. It includes automated reporting to distributors."
- Ticketing Control — central store of posters, trailers, ratings, synopses used by online ticketing, signage, POS, kiosks, website; "manage film scheduling, pricing, and seating."

**Cinema POS page.** Multi-Mode Point of Sale: tickets + concessions + bar/restaurant from one interface; redeem online-purchased concessions; upsell promotions/combos; gratuities, open tabs, food-order management. Omnichannel payments (multiple payment forms in one transaction). Automation Manager: "automated features that can update digital projection systems, LCD poster displays, box office marquees, and feed numerous online ticketing and social media sites." Loyalty & gift cards. Usher Point: Android app for paperless verification of online ticket purchases. Digital signage.

**Ticketing page (via search index).** Box office, kiosk, online selling; webstore; Ticketing Control for scheduling/pricing/seating; integrations with third-party internet ticketing providers (Fandango, The Boxoffice Company, Mobile Moviegoing — vendor-named).

## Product C — RTS (Ready Theater Systems)

### Key observations (evidence layer A)

**Self-positioning.** "Point-of-sale and cinema management solutions" for 30+ years; independents, large chains, drive-ins, FECs, live venues; 900+ cinemas (vendor claim via partner press); all features included in one package.

**Boxoffice selling screen.** Fast ticket sales; multiple payment options in one transaction; age verification; customizable graphic buttons; ticket comps, discounts, seat assignments; supports both general admission and reserved seating.

**Reserved seating.** Graphical seat layout; different seat types and pricing within the same auditorium; seat swaps; marking broken seats; seat history — all from the selling screen; in-person and online sales share it.

**Film & Schedule Management.** Add films, adjust showtimes, manage auditoriums; copy schedules across multiple days; different ticket rules for specific performances; real-time updates including film synopses and seat availability. Operations page adds: built-in film database with thousands of titles, graphics and metadata; drag-and-drop scheduler; **export schedule to TMS/LMS**; automatic updates to digital signage and websites via XML or API.

**Concessions.** Integrated ticket + concession sales on one interface; order routing to kitchen/bar prep stations; barcode-scanned item entry; combo upsells, discounts, restricted items (alcohol); inventory updated by every sale in real time; recipe tracking "down to the ounce".

**Enhanced F&B (dine-in).** Menu items, modifiers, special instructions; dynamic table management with visual layouts of dining areas or auditoriums; routing to KDS; tabs (open/split/transfer), pre-authorized cards. (GoTab partnership shows the seam: GoTab handles F&B ordering/kitchen, RTS keeps "box office, reserved seating, and film scheduling" — bi-directional sync of tickets, seat holds, refunds, inventory.)

**Operations.** Web reports (real-time sales, inventory, employee performance from any device); remote connections to office computers; enterprise multi-location management (aggregate data, centralized multi-location management, remote schedule updates); report suite: Sales Summary, Inventory Usage, Labor Costs, Advance Ticket Sales (by showtime/auditorium/date), Gift Card Activity, Loyalty Program.

**Customer experience.** Branded customer app (showtimes, tickets, loyalty, concessions, notifications); Usher App (scan/redeem printed and digital tickets, browser-based, real-time); kiosks (tickets, pick-up, concessions, gift-card reload); loyalty with tiers; digital signage (showtimes, menus, promotions).

## Product D — Veezi

### Key observations (evidence layer A)

**Self-positioning.** "Cinema software for independent cinemas", engineered by Vista; 100% cloud; fast set-up; free trial (self-serve SaaS motion).

**Cinema Management feature.** Cloud back office: manage ticket types, set and adjust price cards, add/alter concession rates; run promotions, create discounts, group order modifications. Performance Dashboard: real-time widgets — daily statistics, current film program, top selling items, spend per patron, sales by screen, online POS operators; customizable gadgets; used for decisions "such as switching out scheduled films".

**Film Programming feature.** Preloaded film database from movieXchange MX Film ("studio-official film database"): each film record carries run time, rating, synopsis, poster graphics; editable after import; custom film records for special events. Programming interface: drag-and-drop session creation; bulk copy schedules by day or week; per-session editing of: price cards, sales-channel availability, allocated vs unallocated seating toggle, extra time for trailers and cleanup, 'private' showings (limited access). Marathons/double features: scheduled and ticketed as a single session "while recording rental for each film" (settlement awareness inside scheduling).

**Other features (catalog).** Point of Sale, Kiosk, UsherPoint App, Digital Signage, Time & Attendance, Loyalty, Vouchers & Gift Cards, Inventory, Reporting, V-Tix internet ticketing, Web, Movie Mailer (email marketing). Testimonials confirm drive-in and film-festival usage.

## Cross-product Comparison

| Dimension | Vista | Omniterm | RTS | Veezi | Reading |
|---|---|---|---|---|---|
| Session/showtime scheduling as spine | Film Manager + Showtime Manager; draft→planned→publish | Ticketing Control ("film scheduling, pricing, seating") | Film & Schedule Management; drag-and-drop; copy across days | Film Programming; drag-and-drop; bulk copy | **All four**: the scheduled session is the central operational object |
| Film record with content metadata | Film records + trailers/ads + movieXchange studio data | Central store: posters, trailers, ratings, synopses | Film database, thousands of titles, metadata | MX Film preloaded: runtime, rating, synopsis, posters | **All four**: the film is a managed record reused across sessions and channels |
| Auditorium/screen estate | Sessions placed on screens; screen data in film hire | "manage film scheduling, pricing, and seating" | "manage auditoriums"; seat layouts | sessions placed per screen; sales by screen | **All four**: the operator's own screens are the placement capacity |
| Session-level pricing machinery | Price cards (base/derived/future), pricing rules per session, new-release surcharges | pricing in Ticketing Control | ticket rules per performance; seat-type pricing | price cards per session; concession rates | **All four**: pricing attaches to sessions, not just to a global list |
| Ticket types | ticket types + classes + restrictions | coupons/discounts; ticketing | comps, discounts, age verification | ticket types | **All four** |
| Seating modes | area categories; seat-first kiosk ordering | seating management | GA + reserved; seat swaps; broken seats; seat history | allocated vs unallocated toggle per session | **All four**: reserved seating is a per-session mode, not the identity |
| Sales channels | POS, Web, Mobile, Kiosk, Call Centre, Group Sales | POS, kiosk, online/webstore, third-party integrations | terminal, web, app, kiosk | POS, V-Tix, Web, Kiosk | **All four**: staffed + self-service + remote channels on one inventory |
| Concessions integrated | F&B module, Serve, combos upsell | concessions sales & inventory, recipes, combos | integrated selling, routing, recipes | concession rates, inventory, top-selling items | **All four**: second revenue line on the same spine |
| Distributor settlement | Film hire: contracts, formula/minimum share, per film/cinema/week | Automated Film Settlement; rental calculation; distributor reporting | not observed on fetched pages | rental recorded per film (marathons) | **3 of 4 documented** (RTS unobserved, not denied); industry-defining money flow |
| Head office / circuit | Head Office module; Horizon BI | Enterprise solution page | enterprise multi-location; web reports | single-site focus (dashboard per site) | **3 of 4**; scale-dependent |
| Admission validation | Self-Scan, InTouch | Usher Point | Usher App | UsherPoint App | **All four**: ticket checking is part of the estate |
| Schedule feeds projection/signage/web | Digital Signage; movieXchange showtime distribution | Automation Manager updates "digital projection systems… marquees… online ticketing" | Export to TMS/LMS; XML/API to signage + websites | (signage feature) | **All four**: the schedule is distributed outward, including to the TMS |
| Loyalty / gift cards / subscriptions | Loyalty, Vouchers & Gift Cards, Subscriptions | Loyalty & gift cards | loyalty + tiers, gift cards | Loyalty, Vouchers & Gift Cards | **All four** (subscriptions Vista-only among the sample) |
| Staff/time | InTouch; (managed upgrades) | Punch Clock; employees | Labor Costs report; employee performance | Time & Attendance | **All four** (depth varies) |
| Deployment | on-prem (Classic) + cloud (Cloud) | Windows on-prem + peripherals | on-prem + remote access | 100% cloud SaaS | variant, not identity |

## Abstraction

### L0 — Defining Invariant

Three jointly-held structures over one binding (the operator's own cinema site(s)):

1. **The session as the operational unit of record.** A scheduled screening — a film placed in one of the operator's own auditoriums at a date and time — is the object the whole system hangs off. Sessions are composed ahead of time (commonly by drag-and-drop or copy from a film palette/database), carry their selling configuration (pricing, seating mode, channel availability), become visible/buyable when published, and drive every downstream surface: box office, online channels, kiosks, signage, staff apps, and the projection layer. Remove → a ticketing tool with no cinema programme, or a scheduling tool with no selling.

2. **The two reference estates the session draws from.** (a) Films held as content records — title, runtime, rating, distributor, promotional media — created once and reused across many sessions, sites, and channels; the rating gates age-checked selling, the runtime shapes scheduling. (b) The auditorium/screen estate — the operator's own screens with capacity and seat layouts — into which sessions are placed. Remove the film estate → generic event ticketing; remove the auditorium estate → broadcast/content scheduling.

3. **Session-bound admission selling.** Tickets are sold against sessions — at the staffed box office and through self-service/remote channels — priced by session-level configuration (ticket types on price cards/rules), recorded as transactions that attribute every admission to its film, session, and (where present) distributor. Remove → scheduling software with no revenue loop (the sibling scheduling-application territory).

Jointly-held load-bearing analysis:
- 1 alone = a showtime calendar / scheduling tool (sibling leaf territory)
- 2 without 1 = a film list and a screen list with nothing scheduled
- 3 without 1+2 = generic admission selling with no cinema semantics
- 1+2 without 3 = programme planning with no box office
- 1+3 without 2 = selling admission to nothing in particular (event ticketing shape)
- 2+3 without 1 = inventory and a till with no programme

### L1 — Common Mature Structure

Present in essentially all mature modern products; makes the Type practical but does not define it:

- **Concessions/F&B as the integrated second revenue line** — concession items, combos/meals, recipes, inventory depletion on sale, order routing; upsell prompts at the POS; in modern products often extending to dine-in (tabs, KDS, table service).
- **Distributor settlement (film hire / rental)** — the exhibitor's contracted payment to film distributors computed from ticket sales, commonly per film per site per week, under contracted formulas (percentage shares, minimums, house-cost deductions), producing settlement records/reports. Documented explicitly in 3 of 4 sampled products; the industry's defining money flow.
- **Ticket-type / price-card machinery** — ticket types (adult/child/student…), price cards or rule sets attached to sessions, promotions/discounts/deals, surcharges (e.g., new-release or premium-format), fees.
- **Multi-channel selling on one inventory** — box office POS, web, mobile app, kiosk, call centre; real-time propagation of session/seat availability across channels.
- **Reserved seating as a per-session mode** — seat maps per auditorium, per-session seat states, seat-first selling; alongside unallocated/GA mode (the two coexist in products and markets).
- **Admission validation** — staff scanning apps and/or self-scanning; ticket state honored at the door.
- **Loyalty, vouchers, gift cards** (subscriptions in some products).
- **Reporting/BI** — sales by film/session/screen/day, concession performance, labor, advance sales.
- **Head-office/circuit management** for chains — centralized configuration, cross-site reporting, bulk operations.
- **Outward schedule distribution** — digital signage, websites, third-party listing/ticketing services, and the projection TMS.
- **Staff/time functions** — punch clock/time & attendance, labor reporting.

### L2 — Variant / Optional Structure

- Deployment: on-premise vs cloud SaaS; hardware bundles.
- Scale shape: single-site back office vs head-office circuit suite.
- Seating-market shape: reserved-seating-first vs GA-first markets; premium/area-priced seating.
- Dine-in cinema / expanded F&B (restaurant-level service inside the cinema).
- Drive-ins, festivals/repertory programming, marathons/double features, private screenings/group sales.
- Alternative content (events beyond films) scheduled and sold in the same spine.
- AI forecasting/automated scheduling; dynamic/personalized pricing; moviegoer engagement/CRM depth; subscriptions.
- Third-party distribution of showtimes/tickets (aggregators, internet ticketing providers).

### L3 — Vendor-specific (research notes only)

- Vista: Living Ticket (self-updating digital ticket), movieXchange/MX Film data distribution, Horizon BI, CXM personalization, Lumos channels, Cinema Intelligence AI, Formula Share + Minimum Distributor Share "higher value" rule, draft/planned session status labels, "45,000 screens" claim.
- Omniterm: Automation Manager naming, Usher Point naming, punch-clock-per-station, Windows platform, Fandango/The Boxoffice Company/Mobile Moviegoing integrations.
- RTS: all-features-included packaging, "keep all internet fees" positioning, GoTab partnership for dine-in F&B, "900+ cinemas" claim, export-to-TMS/LMS phrasing.
- Veezi: V-Tix, Movie Mailer, gadget-based dashboard, free-trial self-serve motion, MX Film preloaded database.

## Vendor-specific Findings

- Vista's film-hire calculation internals (Formula Share vs Minimum Distributor Share, higher-value rule; house-cost exceptions; per film/cinema/week grain; zero-value ticket exclusion) are product-documented specifics — the canonical claim is only "distributor share computed from ticket sales under contracted terms".
- Vista's draft→planned→publish session lifecycle is product-documented; the canonical claim is "sessions are composed before they become buyable and are published to channels".
- RTS's "Export to TMS/LMS" and Omniterm's Automation Manager "update digital projection systems" are two independent confirmations that the business schedule feeds the projection layer — the seam is cross-product even though the TMS itself is a different product family.
- Veezi's "recording rental for each film" inside marathon scheduling shows settlement awareness reaching into the scheduling surface in a second product.

## Boundary Findings

1. **vs Event Ticketing Platform (processed).** Both sell dated admission with ticket types. Difference: the event ticketing platform centers organizer-defined one-off events (an on-sale moment, a door time) and the sell→issue→validate loop; the cinema management system centers the operator's own continuously recomposed programme of sessions in its own auditoriums, with the film record, concessions, and distributor settlement as first-class context. A cinema system's selling surface is one ring around the session spine; remove the programme spine and the remainder is event ticketing. Keep-both; no directory change.

2. **vs Reserved Seating Platform (processed) — DISCHARGES the pre-hung "cinema seam".** The reserved-seating pass recorded: "cinema is the vertical where every ticket is a seat; seat allocation lives inside the cinema system's own model of screens and screenings". Confirmed from this side with direct evidence: RTS manages seat types/pricing, swaps, broken seats, and seat history inside its selling screen; Veezi toggles allocated vs unallocated seating per session; Vista prices seating areas via area categories and sells seat-first at kiosks. Reserved seating is a per-session mode inside the cinema system's own auditorium model — not a standalone layer here. The seam is discharged; keep-both stands (the reserved-seating leaf documents the cross-vertical seat-map layer; this leaf documents the cinema business system that carries it).

3. **vs Attraction Ticketing (processed).** Attraction ticketing sells operator-defined admission products (day/time-slot tickets) to a place and validates entry as the attendance record. Cinema sells admission to scheduled content screenings; the inventory unit is the session, not a capacity slot at a place; entry checking exists but the attendance record is not the defining loop. Distinct Types.

4. **vs Theatre Management System / Circuit Management System (projection-operations family; NO directory leaf).** Unique X's RosettaBridge TMS / RosettaNet CMS, and peers (Qube, GDC, Dolby), control digital cinema servers and projection/sound/HVAC: playlist assembly, KDM management, content delivery, automation driven by the schedule ("The film schedule drives the operation of the cinema" — Unique X). This is a genuinely different application type: its users are projection/technical operations, its objects are screens' playback devices and content playlists, and it has no selling, concessions, or settlement. The two families integrate through the schedule (RTS "Export schedule to TMS/LMS"; Omniterm Automation Manager "update digital projection systems"; Unique X TMS "POS integration"). **Taxonomy gap recorded**: the TMS/CMS family has no leaf in DIRECTORY.md. Naming hazard: "Theatre Management System" in cinema jargon = projection control, NOT the business system documented here.

5. **vs Cinema Scheduling Application (sibling leaf, unprocessed).** Film programming/scheduling is the spine module of this system (Vista Film Manager, RTS Film & Schedule Management, Veezi Film Programming, Omniterm Ticketing Control scheduling). The sibling leaf names the scheduling-focused application; this leaf names the whole business system. No claims made about the sibling's final disposition; seam noted for that pass.

6. **vs Restaurant POS (processed) / KDS.** Concessions inside the cinema system reuse F&B transaction semantics (items, combos, modifiers, routing, tabs in dine-in). The cinema system's F&B is session-bound and cinema-shaped (in-seat delivery, showtime-aligned service); generic restaurant POS remains a separate Type. The GoTab×RTS integration shows the modern seam: external F&B platforms can carry food service while the cinema system keeps "box office, reserved seating, and film scheduling".

7. **vs Venue Management System (processed).** VMS manages bookable spaces and their use by hirers; the cinema system runs the operator's own public programme with ticket sales. Private screenings/group sales (Vista Group Sales; Veezi private showings) are a variant inside the cinema spine, not a booking system.

8. **vs Broadcast Management System / Newsroom (§27 siblings).** Broadcast schedules content for transmission to an undifferentiated audience; cinema schedules sessions for individually ticketed admission in seated auditoriums. Different users, objects, and money.

9. **vs Film Distribution Management (distributor side, e.g., Vista Maccs).** The distributor-side system manages releases, contracts, and box-office reporting from the distribution end; the cinema system's film-hire module is the exhibitor-side mirror of the same money flow. Adjacent, opposite side of the relationship.

## Historical / Market-Sample Check (§24)

- Paper-era single-screen cinema: weekly programme (the film, the times) posted on the marquee; one auditorium; box office sells paper tickets; weekly settlement with the distributor ("film rental" percentage is as old as the industry). All three L0 structures present without any digital machinery — the definition does not over-fit the modern stack.
- Drive-ins (RTS and Veezi both serve them): same spine, per-car ticketing variant.
- Regional/platform-native differences: reserved-seating-first markets (much of Asia/Europe) vs GA-first markets (historically North America) both fit — seating mode is a per-session variant, not the identity.
- Older cinema POS systems (single-terminal box office + weekly settlement sheets) fit the L0 without loyalty, kiosks, or apps.

## Uncertainties

- RTS's distributor-settlement capability was not observed on the fetched pages (their report suite and POS pages do not name it). Given industry universality and 3-of-4 documentation, settlement is asserted at L1 with the RTS gap noted; not counted as cross-product unanimous.
- Whether a fifth independent vendor pole (e.g., European Cinetixx/Compeso class) would add structure beyond the four sampled is unknown; the four already repeat the same core structures, so sampling stopped per the stop conditions.
- Galaxy Ticketing (galaxyticketing.com), a known US cinema vendor, could not be fetched this pass; its absence from the sample is a sourcing limitation, not a market judgment.
- Exact session-state vocabularies beyond Vista's (draft/planned) are unknown; canonical publish semantics asserted at moderate strength.
- The precise split of scheduling responsibility between head office (programmers) and site managers is documented by Vista (programmers plan, managers adapt and approve) but asserted only for Vista; the general claim "programming and site operation are distinct roles" is moderate-strength.

## Final Synthesis

A Cinema Management System is the film exhibitor's business system of record. Its defining core is three jointly-held structures: the **session** (a film placed in one of the operator's own auditoriums at a time) as the operational unit of record that everything hangs off; the **film and auditorium estates** as the two reference structures sessions draw from; and **session-bound admission selling** across staffed and self-service channels with session-level pricing. Around that core, mature products standardly carry the integrated concessions line, distributor settlement (film hire), multi-channel selling, reserved/GA seating modes, admission validation, loyalty/vouchers, reporting, and — for chains — head-office circuit management, with the schedule distributed outward to signage, listing services, and the projection TMS. The projection-control TMS/CMS family is a distinct, adjacent type (currently absent from the directory); the sibling Cinema Scheduling Application names the scheduling slice of this same estate.
