# Research Notes — Golf Course Management

## Research Goal

Understand what golf course management software actually is as an Application Type: the operator-side system for running a golf course as a business. Extract the smallest defining structure, the standard mature capabilities around it, the variant poles (daily-fee vs membership-club), and the boundaries against adjacent leaves (Tee Time Booking Platform, Sports Facility Management, Sports Club Management, Restaurant POS, Golf Tracking / Handicap Application).

## Initial Boundary

Working hypothesis at start:

- Core use: manage playing capacity (tee times), sell and record rounds, serve golfers, run pro shop / F&B, administer memberships and events.
- Primary users: pro shop staff, golf operations manager / head pro, starter, F&B staff, GM/controller.
- Nearest neighbors: Tee Time Booking Platform (consumer demand side), Sports Facility Management / Sports Court Booking (generic rentable spaces), Sports Club Management (membership-org-first), Racquet Club Management (tennis analog), Restaurant POS (F&B outlet), Golf Tracking / Handicap Application (consumer-side).
- Suspected boundary: operator system of record vs booking channel.
- Unknowns: how deep POS/member billing sit inside the defining core; how much of the "club suite" is variant vs core; whether lotteries/restrictions are core or club-pole-specific.

## Research Questions

1. What is the tee sheet and how does it structure course capacity (slots, intervals, block-outs, start formats)?
2. What does a round reservation carry (party, players, rate basis, source, status) and what lifecycle does it move through?
3. Which booking channels write into the sheet (phone, walk-in, website engine, member portal, third-party marketplaces)?
4. How are rates configured and how do classifications (member, senior, junior…) interact with pricing and privileges?
5. How does membership work (plans, dues billing, minimums, member accounts, chits)?
6. What is the check-in / starter flow (paid status, start/turn/end recording, pace)?
7. How are events, outings, leagues and tournaments handled on the sheet?
8. What ancillary modules recur (POS, inventory, F&B, marketing, reporting, activity booking)?
9. What separates this Type from Tee Time Booking Platform / Sports Facility Management / Sports Club Management?
10. What would older / regional / pre-cloud products still require for the definition to hold?

## Representative Products

| Product | Positioning | Why sampled | Evidence tier |
|---|---|---|---|
| **Club Caddie** | All-in-one cloud golf management suite; daily fee & resort, semi-private, multi-course operators, indoor golf; Windows app + cloud (Azure); owned by Jonas Software (Constellation) | Course-first suite spanning both commercial poles; deep product-page detail on tee sheet + starter sheet | A (official product pages) |
| **Teesnap** | Cloud-native course platform; 400+ facilities across public, private, municipal, multi-course; mobile POS emphasis; Las Vegas | Daily-fee-heavy, independent (non-Constellation) corroboration of the core | A (official product pages) |
| **Jonas Club Software (The Sheet™)** | Club-first suite for private clubs; golf & tee times as "The Sheet" module within CRM/F&B/events/accounting suite; Markham, Ontario | Membership-club pole; club-suite packaging shape; restrictions/lottery depth | A (official product pages) |

Attempted but unreachable (source-access limitation, recorded per evidence rules):

- **Lightspeed Golf** (ex-Chronogolf) — lightspeedhq.com/golf/ returned 403; support.lightspeedhq.com transport error. Not used.
- **ForeUP** — foreup.com transport error ×2. Not used.
- **Clubessential** — 403. Not used.

Sample-structure caveat: Club Caddie's own site states it is "Owned by Jonas Software — part of the Constellation Software portfolio… Together, we service over 2,500 golf clubs in 20 countries." Two of three samples therefore share a corporate parent; cross-commonalities between those two are given reduced independent weight and are only treated as commonality where Teesnap independently corroborates.

## Sources

Fetched 2026-09-08 (all Tier 2 official product/marketing pages; no help-center KB article was reachable this pass):

- Club Caddie — https://clubcaddie.com/ (homepage, full solutions nav); https://clubcaddie.com/solutions/teesheet/ ; https://clubcaddie.com/solutions/starter-sheet/
- Teesnap — https://www.teesnap.com/ (homepage, platform nav); https://www.teesnap.com/our-platform/tee-sheet/
- Jonas Club Software — https://www.jonasclub.com/ (homepage, full solutions nav); https://www.jonasclub.com/the-sheet/

## Product Observations

### Club Caddie (course-first cloud suite)

Key observations [A = direct from official pages]:

- Nav structure itself declares the domain model: Tee Sheet, Starter Sheet, Activity Booking, Register & POS, Accounting & Reports, F&B, Customer Management, Member Management, Member Portal, Banquet & Event Management, Venue Management, Inventory Management. [A]
- Tee sheet: "book tee times over the phone, in person, online or optionally by… third party tee time distributor partner like PGA Tee Times, Golfback, Supreme Golf, Teeoff.com or GolfNow"; tee time types "Daily fee, member, annual pass holder, discounted senior"; "Book tee times for today, next year, next decade"; leagues (recurring, automatic tee sheet blocking, alternating front/back nines); outings/tournaments with integrated tee sheet blocking, F&B accounting, function sheets, online sign-ups, deposit management "recognizing revenue as a liability until the event day". [A]
- Booking channels unified into one sheet ("No matter the type of tee time, no matter how or when it is booked… keep your tee sheet organized"). [A]
- Customer profiles accessible "from the tee sheet, register, customer or members screens": personal info, birthdate, classification (senior, annual pass holder…), member plan and billing policy incl. discounts and mandatory minimums, rounds played / playing history, spend / purchase history, notes. [A]
- Starter Sheet: separate cloud surface "for rangers, volunteers, and starters"; "record start times, turn times, and end times"; "see who has paid"; check golfers in; communicate with the golf-shop tee sheet; works on tablet. [A]
- POS: golf shop, bev cart, full-service dining, bar, pool, half-way house, driving range, mobile; payment methods incl. cash, credit card, gift card, check, **membership ID**. [A]
- Member management: automated A/R, member billing, member minimums, member discounts, member tabs, member cards, à-la-carte plans, monthly/quarterly/annual billing, card/ACH tokenized. [A]
- Inventory unified across food, beverage, services, golf merchandise, hard goods; purchase orders. [A]
- Distribution: course website, social, custom mobile app; optional 3P networks; "Flash Price" drag-and-drop discounted rates in low-utilization periods; reports on booking trends, demographics, booking sources, average pricing for 9/18-hole rounds. [A]
- Reporting: G/L accounting, revenue, inventory, member A/R, golfer spend, rounds played, employee sales. [A]
- Marketing: customer classes/groups, email + SMS campaigns; websites & mobile apps with tee time reservations, event registration, online store, member portal. [A]

### Teesnap (cloud-native, daily-fee-heavy)

- Platform modules: Tee Sheet, Point of Sale, Reservations, Food & Beverage, Reporting, Website, Payments. [A]
- Tee sheet pitch: "one connected platform for booking, check-in, billing, and communication"; "Smart, profile-based pricing maximizes revenue and eliminates errors". [A]
- Online booking engine integrated with the sheet: booking flow, "smart controls to boost revenue and reduce no-shows", profile-based booking, flexible restrictions, pre-pay options, friend invites. [A]
- "Teesnap learns who plays together and automatically suggests player groups for staff and golfers." [A — vendor-specific flavor]
- POS: mobile, "run tabs or complete a transaction anywhere on the property… especially for our beverage cart service" (customer quote on official site). [A]
- Serves "public, private, municipal, and multi-course operations". [A]
- Marketing services arm (event marketing, social, paid ads, email, website management) — services wrapping the platform. [A]
- Operator-education blog topics: cancellation policies, dynamic pricing ("Why Dynamic Pricing is the Future of Public Golf"). [A — signals category concerns, not product claims]

### Jonas Club Software — The Sheet (club-first suite)

- Jonas suite spans: Golf & Tee Times (The Sheet), F&B (POS, KDS, online ordering, dining reservations, inventory), Events & Catering, Booking & Scheduling (courts, spa, classes, appointments), CRM & Member Management, Finance & Back Office (accounting, billing, payroll, PO), Operations (marina, hotel), member websites/app. [A]
- The Sheet: "configurable tee sheet, featuring shotguns and crossover starts"; "date-driven member and guest play restrictions"; "automated draw/lottery tee times point-based system for sought-after times"; "squeeze and start times to allow complete control of the first tee"; playing partners, guest lists, cart preferences saved for quick booking; "bag & cart tracking to enhance operations" (pace of play); custom email confirmations; prepaid rounds (nav). [A]
- "One-click billing with Jonas" — posting charges to member accounts from the sheet; "Integrated with your Point of Sale, it makes managing chits and fees effortless." [A]
- Member booking on web/mobile ("clean, web-based tee time interface… optimized for mobile"); member app shows tee times, dining, events, statements, "Waitlist Cleared" notification (waitlists exist). [A]
- Tournament integration with external systems "such as Golf Genius, GolfHits, Jonas, and clubsystems group"; members create "entries for the club's tournaments or instantly send a play notification to the club". [A]
- Historical note from client quote: a private club "for twenty-plus years operated without a tee time system" until the pandemic — evidence that sheet-centric software is a modern adoption even at clubs, while billing/accounting software predates it. [A]
- Lotteries/restrictions depth confirms the membership-club pole has governance mechanics largely absent from daily-fee positioning. [A]

## Cross-product Comparison

| Finding | Club Caddie | Teesnap | Jonas | Strength |
|---|---|---|---|---|
| Tee sheet as central operator surface | ✔ | ✔ | ✔ ("The Sheet") | Core (3/3, Teesnap independent) |
| Tee time = dated slot for a bounded party | ✔ | ✔ | ✔ | Core (3/3) |
| Round reservation lifecycle booked → checked-in/started → played/no-show | ✔ (starter sheet start/turn/end, paid status) | ✔ ("booking, check-in, billing") | ✔ (bag/cart tracking, play notification) | Core (3/3) |
| Golfer/customer profile w/ classification & history | ✔ (classification, rounds, spend) | ✔ (profile-based pricing/booking) | ✔ (playing partners, member CRM) | Core-adjacent (3/3) |
| Rate basis on booking (green fee per player, carts) | ✔ | ✔ (profile-based pricing) | ✔ (billing per booking) | Core (3/3) |
| Multiple booking channels into one sheet (phone/walk-in + online) | ✔ (+ 3P networks) | ✔ (booking engine) | ✔ (member web/app) | Core (3/3) |
| Play & revenue record (rounds played, revenue reporting) | ✔ (rounds played, booking sources) | ✔ (Reporting module) | ✔ (member activity, club accounting) | Core (3/3) |
| Own online booking engine / member portal | ✔ | ✔ | ✔ | Common (3/3) |
| POS for golf shop + F&B on same accounts | ✔ | ✔ | ✔ | Common (3/3) |
| Membership management (plans, dues billing, minimums, portal) | ✔ | weak evidence (private/municipal served; depth undocumented) | ✔ | Common in membership ops (2/3 strong) |
| Events/outings with sheet blocking, deposits, sign-ups | ✔ | ○ (event registration via website; marketing services) | ✔ (event mgmt + tournament integrations) | Common (2/3 strong) |
| Leagues as recurring bookings | ✔ (alternating nines) | ○ | ○ (weekly games sign-up) | Common (evidence strongest CC) |
| Booking restrictions (member/guest, date-driven, advance windows) | ✔ (types/classifications) | ✔ ("flexible restrictions") | ✔ (date-driven, lotteries) | Common (3/3) |
| Prepayment / no-show controls | ✔ ("prepayment enabled") | ✔ (pre-pay, reduce no-shows) | ○ (prepaid rounds in nav) | Common (2/3 strong) |
| Check-in/starter dedicated surface | ✔ (Starter Sheet) | ✔ (check-in in loop) | ✔ (first-tee control, play notification) | Common (3/3) |
| Third-party distribution to tee-time marketplaces | ✔ (named networks) | ○ (partners page exists, unfetched) | ○ (not prominent) | Optional, daily-fee pole |
| Dynamic/demand-based pricing | ✔ ("Flash Price") | ✔ ("profile-based pricing"; dynamic-pricing content) | ○ | Optional/Common-modern (2/3) |
| Lotteries/draws for prime times | ○ | ○ | ✔ (point-based draw) | Club-pole variant (1/3) |
| Bag & cart tracking | ○ (carts in booking) | ○ | ✔ | Club-pole variant (1/3) |
| Waitlists | ○ | ○ | ✔ (app notification) | Optional (1/3) |
| Suggested player groups (social learning) | ○ | ✔ | ○ | Vendor-specific (1/3) |
| Deposit revenue-as-liability until event day | ✔ | ○ | ○ | Product-specific (1/3) |
| Accounting/GL, payroll, inventory depth | ✔ | ○ (payments emphasis) | ✔ | Suite variant (2/3) |
| Marina/spa/court/hotel modules | ○ (venue mgmt) | ○ | ✔ | Club-suite variant (1/3) |
| Websites/mobile apps as channel surfaces | ✔ | ✔ | ✔ | Common (3/3) |

Legend: ✔ documented; ○ not documented on fetched pages (absence of evidence, not evidence of absence).

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately minimal)

Three jointly-held structures:

1. **The tee sheet — the course's playing capacity of record.** Playing capacity modeled as a dated, time-slotted schedule of starting positions (tee times) on the course's holes/nines, operator-configured (interval, bookable window, block-outs, start formats such as first-tee sequences; shotgun/crossover where documented). It is the single capacity hub all channels write into. Remove → generic appointment scheduling / capacity calendar, not golf course management.
2. **The round reservation — the booking of record.** A named party holding a specific slot, carrying player count, rate basis (green-fee type, carts), booking source and a status moving booked → checked-in/started → played (or no-show/cancelled), anchored to a golfer/customer profile. Remove → an empty capacity schedule.
3. **The play-and-revenue record of the golf operation.** The operation's own record derived from those bookings: rounds played (per day, slot, source, player class) and round charges raised and settled (prepaid, at the counter, or billed to a member account), feeding utilization/revenue reporting. Remove → a reservation widget with no management memory.

Jointly-held is load-bearing: sheet without bookings = capacity calendar; bookings without sheet = appointment list; records without 1–2 = POS/reporting with no golf scheduling semantics.

Historical/market-sample check (pre-freeze): a 1970s course running a paper tee sheet + reservation book + cash register + daily round-count sheet satisfies all three legs — no software-era artifacts in L0. DOS-era tee-sheet systems (sheet + bookings + rate tables, no internet booking) satisfy L0. Non-US membership and municipal courses satisfy L0 (governance and pricing differ; structure holds). Indoor simulator facilities satisfy the same skeleton with bays as slots (variant). Check passed.

### L1 — Common Mature Structure (not definitional)

- course-operated online booking engine + member portal/app writing into the same sheet
- golfer/customer profiles: identity, classification, contact, playing history, spend
- POS across golf shop and F&B outlets on shared customer accounts
- membership management: plans, dues billing cycles, spending minimums, member statements
- events/outings/leagues: sheet blocking, deposits, online sign-ups, recurring bookings
- booking restriction rule-sets (member/guest windows, advance windows, date-driven)
- check-in/starter surface (paid status, start/turn/end recording)
- reporting (rounds played, revenue by outlet/source/class, utilization, booking source)
- marketing machinery (customer groups, email/SMS, promotions)
- no-show countermeasures (prepay/deposit, cancellation policy, waitlists)

### L2 — Variant / Optional Structure

- third-party distribution to tee-time marketplaces (daily-fee pole)
- demand-based pricing / flash discounts (modern, both poles drifting)
- multi-course and resort contexts (cross-course inventory, hotel linkage)
- activity booking beyond the course: driving-range bays, simulator bays, lessons/clinics
- club-suite adjacents: accounting/GL, payroll, deep inventory, dining reservations, court/spa booking, marina/hotel (club pole)
- lotteries/point-draws for prime-time access, bag & cart tracking (club pole)
- tournament-scoring integrations (external tournament platforms)
- deployment shapes: cloud browser vs desktop/Windows app vs hosted; venue ops (pool, halfway house, bev cart) breadth

### L3 — Vendor-specific (kept out of final document)

- Jonas: "The Sheet" branding, point-based lottery specifics, "squeeze and start times", MembersFirst tee times, Golf Genius/GolfHits/clubsystems integrations, ClubHouse Online app
- Club Caddie: "Flash Price" drag-and-drop, Accountant Edition, "book… next decade" positioning, bev-cart/pool POS enumeration, Azure hosting claim, monthly changelog cadence
- Teesnap: flat-rate payments framing, suggested player groups (social learning), marketing-advisor service model, 400+ facilities figure
- Corporate structure: Club Caddie + Jonas both under Jonas Software/Constellation (sample caveat)

## Vendor-specific Findings

See L3. Additionally: revenue-as-liability treatment for event deposits documented only at Club Caddie (kept product-specific, not promoted). Suggested player groups documented only at Teesnap (vendor-specific).

## Boundary Findings

| Adjacent Type | Shared surface | Decisive difference | "Remove → becomes" test |
|---|---|---|---|
| **Tee Time Booking Platform** (separate leaf) | both show bookable tee times | booking platform is the consumer demand surface/channel; GCM is the operator's system of record (sheet configuration, check-in, profiles, play/revenue records). A GCM's own booking engine is a channel of the same system, not the Type. | Remove operator-of-record side → consumer booking platform |
| **Sports Facility Management / Sports Court Booking** | slot-based booking of a facility | golf's unit is a starting position on a shared course (per-player green fees, carts, round lifecycle, pace), not exclusive hourly rental of a space | Remove golf round/slot semantics → generic facility booking |
| **Sports Club Management** (leaf exists) | membership org management | club-first Type centers the member organization (any sport); GCM centers course capacity and rounds. Club suites (Jonas) contain golf operations as their golf spine — overlap zone, but the golf spine alone still satisfies GCM's core | — |
| **Racquet Club Management** | membership + booking | court-based hourly booking, no tee-time/round semantics | — |
| **Restaurant POS** | F&B transactions inside GCM | outlet POS is an attached venue surface; Restaurant POS as a Type centers restaurant service semantics | Remove sheet → venue POS |
| **Golf Tracking / Handicap Application** (separate leaf) | both touch rounds | consumer-side score/stat/handicap recording vs operator-side capacity & revenue management | — |
| **Tournament Management Platform** (leaf exists) | tournaments | competition scoring/formats is the other Type; GCM provides sheet blocks, deposits, logistics and integrates out to scoring products (documented at Jonas) | — |
| **Appointment Scheduling Application** | time-slot bookings | generic slots lack course-configured capacity, per-player pricing, round lifecycle, golf operation context | — |
| **Hotel PMS** (analogy only) | inventory-per-slot model resembles room nights | analogy useful in prose, different domain, different Type | — |

Taxonomy check: the leaf stands as an independent Type — the tee-sheet capacity model is unique in the directory; sibling leaves (Tee Time Booking Platform, Golf Tracking / Handicap) partition the domain cleanly. No directory change proposed.

## Uncertainties

- No help-center KB article was reachable this pass; all evidence is official product/marketing pages. Operational parameters (default slot interval, party-size caps, advance-window defaults, fee structures) were therefore NOT verified and are deliberately absent from the final document.
- Teesnap's membership/dues depth is undocumented on fetched pages (homepage claims public/private/municipal coverage) — membership claims in the final document are calibrated to the two products that document them and worded as membership-operations capabilities.
- Whether deposit-liability revenue treatment is industry-common is unknown (single-product evidence) — kept product-specific.
- The paper-era historical anchor is reasoned from the structure, not sourced from archival documentation — flagged as canonical inference.
- Third-party distribution breadth at Teesnap/Jonas unverified (partners page not fetched) — distribution kept as an optional daily-fee-pole capability with Club Caddie as the documenting sample.
- ForeUP/Lightspeed/Clubessential absence slightly narrows the daily-fee/SaaS sample; Club Caddie + Teesnap provide independent coverage of that pole.

## Final Synthesis

Golf Course Management is the operator-side business system of record for a golf operation. Its world is built on the tee sheet: the course's playing capacity laid out as dated starting slots. Every sales channel — the counter, the phone, the course's own website or app, the member portal, third-party marketplaces — writes round reservations into that one sheet. Each reservation carries a named party, a rate basis per player (green fee, cart) and moves through booked → checked-in → played (or no-show), generating the operation's rounds-and-revenue record. Around this core, mature products add the commercial periphery the course actually runs on: profiles with classifications, pro-shop and F&B point of sale, membership billing for clubs, events and leagues that re-shape the sheet, restriction rules that gate access, a starter surface for the first tee, reporting, and marketing. Two commercial poles organize the variants — daily-fee courses optimizing yield and demand acquisition, membership clubs optimizing governed access and member accounting — and the Type spans from standalone course-first platforms to the golf spine of wider club-management suites.
