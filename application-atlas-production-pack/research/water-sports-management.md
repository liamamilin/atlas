# Research Notes — Water Sports Management

## Research Goal

Understand the "Water Sports Management" Application Type from real products: what the operator's world consists of (objects, users, surfaces), how daily work flows through the system (configure → sell → onboard → run the day → close), which structures are definitional vs common vs variant vs vendor-specific, and where the boundaries sit against neighboring Types (Tour Operator Management System, Swim School Management, Sports Facility Management, Marina Management, Boat/Yacht Charter Platform, Digital Waiver Management, Event Registration Platform, generic rental/booking tools).

## Initial Boundary

- Directory position: §28 Sports, Fitness & Recreation, in the outdoor-recreation sibling cluster: Outdoor Recreation Discovery, Hiking / Trail Application (processed 2026-09-08), Ski Resort Recreation Application (processed 2026-09-09), **Water Sports Management**, Recreational Fishing Application (processed 2026-09-09), Recreation Center Management (processed 2026-09-09).
- **Naming-convention reading (the leaf's central interpretation decision):** across §28, "Management" leaves are operator-side systems of record (Gym Management System, Swim School Management, Golf Course Management, Sports Facility Management, Recreation Center Management, Marina Management in §18); participant-side leaves use "Application" or "Tracking" (Running Application, Cycling Application, Swimming Training Application, Workout Tracking Application, Golf Tracking / Handicap Application). "Water Sports Management" is therefore read as the **operator-side system of record for a water sports operation** — dive centers, surf/kite/windsurf/sailing schools, water sports centers, kayak/SUP/canoe and boat rental + tour operators, dive resorts/liveaboards. Participant-side water-sports apps (surf-session trackers, dive logbooks) are held as Workout Tracking / Swimming Training territory; no directory leaf exists for them and none is requested.
- No sibling pass left a boundary flag for this leaf (the hiking pass and fishing pass each recorded it only as a sibling name; the ski pass did not flag it).
- Working hypothesis before research: a dedicated vertical software family exists (dive-center management, surf/kite school management, water sports rental/tour operations), structurally distinct from generic tour/activity booking because of the equipment fleet, participant qualifications, and conditions-coupled daily replanning.

## Research Questions

1. What is the operation's sellable program (offerings) and how is each configured (capacity, staffing, pricing, prerequisites)?
2. What is the unit of daily operation — how do sessions/trips/lessons get scheduled, staffed, and resourced, and how are they replanned?
3. How do water conditions (tide, wind, swell, sea state) enter the product — as data, as schedule constraints, as replanning triggers?
4. How is equipment held — per-unit or category-level — and how do rental, assignment, damage, and maintenance work?
5. What participant records exist (certifications, medical clearance, swim-ability, waivers, gear sizes) and do they gate anything?
6. What staff machinery exists (instructor/guide assignment, ratios, availability, settlements/payroll)?
7. Through which channels does selling happen (online booking, walk-in POS, payment links, agents/OTAs)?
8. What money machinery exists (deposits, invoices, payouts, accounting exports, retail)?
9. Which structures are definitional vs common-mature vs variant vs vendor-specific?
10. Where are the boundaries: vs tour-operator systems, swim schools, facility systems, marinas, charter platforms, waiver systems, event registration, generic rental?

## Representative Products

Selected for market coverage across the Type's poles, different product philosophies, different customer layers, and different geographies:

| Product | Pole | Why sampled | Evidence status |
|---|---|---|---|
| Bloowatch | cross-water-sports platform (dive centers + surf/kite/sailing/windsurf schools + kayak/boat rental + outdoor centers; 30+ countries claimed) | the broadest "water sports management" pole; one product spanning the verticals | homepage fetched (Tier 1) |
| Dive Shop 360 | dive-retail POS incumbent (~20 years; US-rooted, worldwide customer quotes) | the established dive-shop pole: retail POS + courses/certifications + rentals + repairs | homepage fetched (Tier 1) |
| DiversDesk | dive-operations pole for tourism-driven locations (Bali/Thailand/Philippines/Belize client base) | operations-first dive center management: planner, paperless onboarding, payments | homepage fetched (Tier 1) |
| Thalassa | new-generation unified dive-industry platform (early access) | states the full workflow span explicitly (POS→booking→training→rental→maintenance→waivers→CRM); names the incumbent stack it replaces | homepage fetched (Tier 1) |
| SurfCloud | small-school European kite/wind/surf system (Polish/Croatian client base) | the small-school pole: calendar + rentals + instructor settlements + wind forecast; per-lesson pricing | homepage fetched (Tier 1) |

Boundary anchors (search-result captures of official pages; used for market-structure and boundary reasoning only, held at reduced strength):

- EquipDash (surf school + board rental; tide-window scheduling, ding logging, deposit holds, swim-ability declarations)
- SurfSlot (surf school booking; conditions monitoring, instructor auto-assignment)
- TIDEFORCE (self-described "Commerce & Operations Platform for Outdoor Sports Schools"; surf pole)
- OceanDojo (watersports schools: surf/kite/windsurf; site is a JS shell — not fetched, market-structure corroboration only)
- Dive Admin, ScubaCloud, DiverDash, DivePlanner Pro (further dive-center family members — corroborate the dive pole's population)
- Reservety, TWICE (generic rental/booking platforms marketing surf-school configurations — the generic-configured boundary pole)

## Sources

Research date: 2026-09-09.

Fetched official product pages (all vendor-authored):

- Bloowatch — https://www.bloowatch.com/en/homepage (fetched 2026-09-09)
- Dive Shop 360 — https://diveshop360.com/ (fetched 2026-09-09)
- DiversDesk — https://www.diversdesk.com/ (fetched 2026-09-09)
- Thalassa — https://thalassa.software/ (fetched 2026-09-09)
- SurfCloud — https://surfcloud.app/ (fetched 2026-09-09)

Search-result captures (official pages surfaced via web search; not directly fetched):

- EquipDash — https://equipdash.com/experience-tour-operator/surf
- SurfSlot — https://surfslot.eu/
- TIDEFORCE — https://tideforce.de/en/solutions/surf-schools
- OceanDojo — https://www.oceandojo.com/en/index.html (fetch returned JS shell only)
- Dive Admin — https://diveadmin.com/en ; ScubaCloud — https://scubacloud.co/ ; DiverDash — https://www.diverdash.com/ ; DivePlanner Pro — https://diveplannerpro.com/
- Reservety — https://reservety.com/solutions/surf-rental-software.html ; TWICE — https://www.twicecommerce.com/rent/surfboards

Cross-references: STATUS.md entries for tour-operator-management-system, swim-school-management, sports-facility-management, recreation-center-management, marina-management, boat-yacht-charter-platform, digital-waiver-management, event-registration-platform (all processed 2026-09-06…09).

Source-access limitations:

- No vendor help-center, user-guide, or manual article was fetched for any sampled product; all evidence is official product-page level. No precise operational defaults (numeric capacities, exact fee percentages, retention periods beyond vendor-stated claims) are asserted anywhere; vendor-stated figures are quoted as vendor claims.
- Thalassa is in early access — its workflow span is vendor-stated product scope, not market-proven deployment depth; claims kept at product-page strength.
- OceanDojo unreachable (JS shell) — market-structure corroboration only.
- EquipDash/SurfSlot/TIDEFORCE observations rest on search-result captures — reduced strength, used for market-structure and boundary reasoning only.

## Product Observations

### Bloowatch — evidence layer A (fetched homepage)

Positioning: "Booking & Management Software for Watersports & Dive Centers"; "The operational platform for dive centers, watersports centers, rental businesses, and outdoor activities worldwide"; "Bloowatch isn't just a booking tool. It's a complete operating system for activity centers." Audience pages: dive centers, surf schools, kitesurf schools, sailing schools, windsurf schools, outdoor centers (rafting & canyoning), ski schools; dive resorts, surf camps; kayak rental & tours, bike rental, boat rental & courses.

- **Sessions & resources on one live calendar**: "Keep every session, instructor, boat or gear unit in a live calendar. Drag, drop, and reschedule in seconds — built for ocean-based activities." "Specialized scheduling for dive & watersports activities"; "Instant access to clients data, waivers, and payments from your schedule"; "Role-based mobile access".
- **Capacity/ratio/resource control**: "Sell, schedule, and run ops—together; Capacity, ratios, staff, resources—controlled."
- **Multichannel selling**: "POS for onsite sales & remote payment links; Fast online checkout for activities and rentals. No Bloowatch commission; Agent access with tracked commissions + OTAs connectivity." Channel Manager product: "Availability & product syncing; Centralized reservations; 30+ connected OTAs" (vendor claim).
- **Product modules**: Activities platform (base), Rentals ("Full inventory management; Maintenance status and revision tracking; Drag-and-drop calendar; Sell rentals across channels"), Waivers ("Unlimited custom forms; Smart forms with conditional logic; Embedded across website, links and QR code"), Channel Manager. "Start with Activities, then add what you need: Rentals, Waivers, or Channel Manager—all connected to the same calendar, customers, payments, and reporting."
- **Automation**: "Digital waivers with validation & e-signatures; Automated confirmations, reminders, cancellations; End-of-day POS closure & reporting."
- **Conditions-coupling**: surf vertical — "Condition-ready scheduling for group and private lessons, levels, and tides"; kite vertical — "Wind-smart scheduling: drag-and-drop reshuffles for levels, groups, and instructors… When the wind shifts, your plan shifts too"; customer testimonial: "It perfectly handles our tide and weather constraints."
- **Dive vertical**: "Boat trips and shore dives in one calendar, with one-click manifests"; gear tracking.
- **Whitewater vertical**: "Guide-ready logistics: mobile run sheets with guest notes, sizes, and timing; per-participant waivers."
- Customer quotes: overbooking avoidance; "complete tool for scheduling, payments, online shop, and accounting"; tide/weather handling.

Observations: the calendar-of-sessions-with-resources is the spine; selling is multichannel with commission posture (no platform commission, agent commissions tracked); waivers/rentals/channel manager are attachable modules on one shared calendar/customer/payment/reporting core; conditions-coupling is foregrounded per sport.

### Dive Shop 360 — evidence layer A (fetched homepage)

Positioning: "ALL-IN-ONE DIVE SHOP POS"; "Manage your dive shop with a single solution"; "Designed with the input of thousands of dive professionals over the course of 20 years, Dive Shop 360 has become the leading dive solution in the world" (vendor claim).

- **Unified operations**: "Consolidated certification, course, rental, and repair management"; "Book trips and courses, rent out gear, process payments, and track repair tickets in the same system."
- **Certification integration**: "Integrate with PADI, SSI and SDI/TDI/ERDI/PFI to certify divers, and send out new certifications instantly via text or email."
- **Retail machinery**: "120+ preloaded vendor catalogs, complete with 15,000+ product images" (vendor claim); stock updates across sales channels.
- **Automated messaging**: course updates, receipts, work-status notifications via text/email; AI-powered text responses; promotions; Google review requests.
- **E-commerce**: custom website without developer; "List courses and trips, capping seats so you don't oversell"; "Let divers rent gear online."
- **Repairs**: "Use the work orders tool to create service tickets, track progress, and update customers automatically."
- **Trips & charter**: "List trips and courses online, reserve seats, and take payment in store, online, or by sending customers a secure payment link."
- Customer quotes: US/Caribbean/UK dive stores; QuickBooks import; cloud-based.

Observations: the dive-retail pole — POS/retail/inventory is the base, with trips/courses/rentals/repairs as dive-specific workflows on top; certification agencies are first-class integrations; seat-capped online selling of trips and courses.

### DiversDesk — evidence layer A (fetched homepage)

Positioning: "Dive Center Software, The Intuitive All-in-One Solution"; "Designed specifically for and in collaboration with dive centers"; client marquee is Southeast-Asian/Caribbean dive resorts and centers (Bali, Nusa Penida, Tioman, Thailand, Philippines, Belize).

- **Planning & scheduling**: "One view capacity insights in trips, staff, fleet and more; Seamless multi-trip and cross-location scheduling; Effortless boat and group swaps." Operations features: planning and scheduling, staff calendars, capacity insights, digital whiteboard.
- **Paperless onboarding**: "built-in custom registration forms, official waivers, and Diver Medical"; "Registration, Waivers & Diver Medical. Customizable and Multi-Language"; single booking URL handling "registration, waivers, and payments."
- **Payments**: "Pre-Payments, Billing & Invoicing"; payment-gateway integration (Xendit named in FAQ); bookkeeping integration; data exports.
- **Analytics**: "Metrics dashboard; Workdays, trips, and tank usage; Data exports"; "top trips by numbers and revenue, and customer trends."
- **Staff**: "different rights and permissions for staff members"; staff calendars.
- **Marketing**: white-label branding; filters & exports for email marketing.
- Pricing tiers by user-account counts and manager roles (vendor figures).

Observations: the dive-operations pole — the planner (trips × staff × fleet capacity, boat/group swaps) is the center; onboarding is paperless with the dive-specific medical form as a first-class document; tank usage as an analytics dimension (the trade's consumable); multi-location and staff permissions present.

### Thalassa — evidence layer A (fetched homepage; early access)

Positioning: "The operating system for dive businesses"; "replaces the fragmented stack of POS, booking, waivers, training, and CRM tools… built specifically for dive shops, charter operators, liveaboards, and dive resorts." Names the incumbent stack it replaces: FareHarbor, Dive Shop 360, Rain POS, Smartwaiver, WooCommerce.

- **POS & retail**: full POS (Stripe Terminal, split payments, gift cards, barcode scanning, thermal receipts); offline via a local hub device.
- **Trip & charter booking**: "Create trip types, schedule instances, manage capacity, and take bookings online or at the counter. Manifests pre-load to the hub device for offline dock check-in and in-water roll call."
- **Course & training management**: "Schedule sessions, track student progress, manage skill sign-offs, and submit certifications to PADI, SSI, NAUI, SDI/TDI, RAID, and CMAS."
- **Rental management**: "Track every piece of gear by serial number. Assign equipment to bookings, flag overdue returns, and block items under service. Size search for wetsuits, BCDs, and fins is built in."
- **Equipment maintenance & compliance**: "Track hydro dates, annual service intervals, and visual inspection schedules for every cylinder and regulator" with automated alerts (vendor-stated cadence: 30/7/1 day before due).
- **Digital waivers & forms**: drag-and-drop waiver templates; signing links by email/SMS; signed PDFs stored (vendor-stated: 10 years).
- **CRM**: "Every customer's certifications, dive log, booking history, rental history, and communications in one profile."
- **Online storefront**, **financial reporting** (QuickBooks/Xero exports, multi-currency), **staff mobile app** (offline-first: manifests, roll call, equipment fault reports), **liveaboard management** (vessels/cabins/voyages/onboard POS), **accommodation & resort** (rooms, folios, housekeeping, F&B linked to dive bookings), **B2B agent portal** (availability, option holds, commissions).
- Business-model posture: flat monthly subscription, "No per-booking fees" (contrast drawn with per-booking-fee platforms).

Observations: the most explicit statement of the Type's full workflow span — from inquiry to "certification card issued and equipment serviced and returned"; the equipment leg is per-unit (serial) with compliance machinery (hydro/service/inspection); the offline dock/vessel posture; the resort/liveaboard extension attaches accommodation to the same operation.

### SurfCloud — evidence layer A (fetched homepage)

Positioning: "A comprehensive tool for managing surfing schools"; "If you own wind, kite or surf school, we would like to help you grow your business." Client base: Polish/Croatian kite/windsurf/surf schools at camping spots.

- **Interactive calendar**: single-day and horizontally-scrolled week view; display all instructors or filter by discipline; drag-and-drop rescheduling; mark paid lessons; instructor absences/days off.
- **Customers database**: history of all lessons and rentals; personalized tags; total lesson duration.
- **Rentals management**: "Control rented equipment; Support for hourly, daily and weekly rentals; Mark entries when equipment has been returned or when rental has been settled."
- **Equipment occupancy timeline**: horizontal timeline of equipment occupancy, single day or upcoming 7 days, grouped by categories.
- **Automated SMS**: schedule changes/cancellations/reschedules notified to instructors and students; reminders to reduce no-shows.
- **Wind & weather forecast**: "Integrated WindGuru wind & weather forecast… wind speed, gusts, direction, temperature, cloud coverage, precipitation; Select your favourite spot; pull-out panel accessible in any app view."
- **Instructor settlements**: "summary of all lessons, their duration and payable amount based on the instructor's hourly rates; Track which lessons have been already settled."
- **Mobile apps** for instructors; per-lesson/per-rental pricing ("You don't pay when you don't teach (eg. off season or no wind)"); winter sibling product (SnowCloud) for ski/snowboard trips.

Observations: the small-school pole — calendar + customers + rentals + settlements + forecast panel; the wind forecast is embedded as a working panel next to the schedule; pricing follows usage (per lesson/rental), matching seasonal/no-wind reality; the same genus re-skinned for winter sports confirms the "activity school operations" genus beneath the water binding.

### Boundary anchors — reduced-strength observations (search captures)

- **EquipDash** (surf): "tide-aware scheduling ties each lesson slot to a tide state instead of a fixed hour"; board/wetsuit assignment by length/volume/size at check-in; ding logged at return opens a repair ticket with rate-card charge against a deposit hold; waiver + swim-ability declaration captured at booking; group/private lessons and board rentals in one flow with per-lesson-type instructor ratios.
- **SurfSlot** (surf): "configure ideal conditions (size, wind, tide). System auto selects the best spot"; instructor auto-assignment; equipment inventory; 0%-commission bookings.
- **TIDEFORCE** (surf/outdoor schools): "real-time whiteboard… drag sessions, regroup students and reallocate instructors"; "Wind and conditions are entered by your team — you stay in control of the call"; 12-type single-cart checkout (courses, camps, accommodation, rental, tours, shuttles, lockers); seasonal pricing; B2B provider roles; payroll bookkeeping from sessions.
- **Dive Admin / ScubaCloud / DiverDash / DivePlanner Pro** (dive): corroborate the dive pole's population — trips/courses/certifications/equipment/POS/payroll/commissions across independent vendors.
- **Reservety / TWICE** (generic configured): generic rental/booking platforms marketing surf-school configurations (board inventory, lesson scheduling, waivers) — evidence that the generic-configured pole exists at the Type's boundary.

## Cross-product Comparison

| Structure | Bloowatch | Dive Shop 360 | DiversDesk | Thalassa | SurfCloud |
|---|---|---|---|---|---|
| Activity program as configured offerings (sessions/trips/courses/rentals) | ✓ (activities platform; capacity/ratios) | ✓ (trips & courses, seat-capped; rentals) | ✓ (trips; planner) | ✓ (trip types + instances; course sessions; rentals) | ✓ (lessons; rentals) |
| Scheduled session on a live calendar as the operational hub | ✓ ("live calendar… drag, drop, reschedule") | partial (booking/seat reservation; calendar not foregrounded on page) | ✓ (planner, digital whiteboard, boat/group swaps) | ✓ (schedule instances; manifests) | ✓ (interactive calendar, drag-drop) |
| Staff (instructor/guide) assignment on sessions | ✓ | not foregrounded | ✓ (staff calendars, capacity in staff) | ✓ (staff app, assignments) | ✓ (filter by discipline; absences) |
| Participant roster / capacity control | ✓ (capacity, ratios) | ✓ (capping seats) | ✓ (capacity insights; participant counts) | ✓ (manage capacity; manifests, roll call) | implicit (lesson slots) |
| Equipment/craft as managed resources | ✓ (boats & gear units on calendar; rentals module) | ✓ (rentals, repair tickets) | ✓ (fleet in capacity insights; tank usage) | ✓ (per-serial rental; maintenance compliance) | ✓ (rentals; occupancy timeline) |
| Rental commerce (hourly/daily periods, return/settlement) | ✓ (rentals module) | ✓ | implied (fleet) | ✓ (overdue flags, service blocks) | ✓ (hourly/daily/weekly; return/settled marks) |
| Equipment upkeep (service/repair) | ✓ (maintenance status, revision tracking) | ✓ (work orders) | not foregrounded | ✓ (hydro/service/inspection schedules) | not foregrounded |
| Participant qualification records | waivers module | ✓ (certifications via agencies) | ✓ (waivers + Diver Medical) | ✓ (certifications + submission; dive log) | ✗ |
| Conditions/forecast coupling | ✓ (tide/wind scheduling; testimonial) | not foregrounded | not foregrounded | not foregrounded | ✓ (WindGuru panel) |
| Customer/participant profiles with history | ✓ | ✓ | ✓ (secure customer database) | ✓ (certs, dive log, booking+rental history) | ✓ (lessons+rentals history, tags) |
| Money loop (payments/invoices/deposits) | ✓ (POS, payment links, payments) | ✓ (payments, payment links) | ✓ (pre-payments, billing, invoicing) | ✓ (POS, invoices, accounting exports) | ✓ (paid-lesson marks; settlements) |
| Staff settlements/payroll | agent commissions tracked | not foregrounded | not foregrounded | not foregrounded on page | ✓ (instructor settlements) |
| Retail POS / shop inventory | ✓ (POS; end-of-day closure) | ✓ (core) | not foregrounded | ✓ (core) | ✗ |
| Multichannel distribution (agents/OTAs) | ✓ (channel manager, 30+ OTAs claim) | e-commerce website | white-label + exports | ✓ (B2B agent portal; storefront) | client self-booking option |
| Online customer booking | ✓ | ✓ | ✓ (booking URL) | ✓ | optional client booking |
| Automated messaging | ✓ (confirmations/reminders/cancellations) | ✓ (texts/emails, AI responses) | ✓ (pre-set messages; email notifications) | ✓ (signing links; notifications) | ✓ (SMS) |
| Multi-location | ✓ (resorts; multi-service centers) | not foregrounded | ✓ (cross-location scheduling) | ✓ (multi-location tier) | ✗ (single school) |
| Offline operation | role-based mobile access | not foregrounded | not foregrounded | ✓ (offline hub; offline-first staff app) | mobile preview |
| Accommodation/resort extension | ✓ (dive resorts, surf camps audience) | ✗ | ✗ | ✓ (liveaboard + accommodation modules) | ✗ |

Reading of the comparison:

- **Universal (5/5)**: the activity program as configured offerings; the scheduled session with staff/participant binding; equipment/craft as managed resources; the customer/participant record with history; the money loop.
- **Near-universal (4/5)**: rental commerce with return/settlement states; automated messaging; online customer booking.
- **Pole-dependent**: certification machinery (dive pole: DS360, DiversDesk, Thalassa; absent at SurfCloud, module at Bloowatch); conditions/forecast coupling (school pole: Bloowatch, SurfCloud + anchors; not foregrounded at the dive-retail pole); retail POS (dive-retail pole + platform pole); staff settlements (small-school pole foregrounded); multichannel/OTA distribution (platform pole); accommodation/resort extension (resort pole); offline operation (dock/vessel pole).
- **The trade's shape**: every sampled product mixes at least two of {instruction, guided trips, rental} on one calendar with one customer base and one money record; the dive-retail pole adds retail; the resort pole adds accommodation.

## Canonical Abstraction

### L0 — Defining Invariant

Four jointly-held structures. Remove any one and the product stops being recognizable as this Type:

1. **The water-activity program of record.** The operation's sellable water activities held as configured offerings — instructed sessions (lessons/courses, commonly multi-session and level-structured), guided trips/excursions on the water, and equipment rentals — each carrying capacity, staffing, and pricing. The instruction + guided-activity + rental mixture under one roof, bound to water sports, is the trade's shape. (Present in 5/5.) Remove → a price list / brochure / POS with nothing to deliver.

2. **The scheduled session as the unit of daily operation.** Dated instances of the program placed on a live calendar (realized as planner, day view, or digital whiteboard), binding assigned staff (instructors/guides) and participant rosters — and the boats/gear they use — worked and reshuffled through the day. (Present in 5/5; the calendar is the most consistently foregrounded surface.) Remove → a booking form or CRM; the operation stops being run in the system.

3. **The water-sports equipment and craft as managed resources.** The operation's gear and boats held as tracked units with availability state, assignment to sessions and rentals, and upkeep (service/repair where present). Depth varies from category-level occupancy timelines to per-serial tracking with compliance schedules; the managed-unit leg is the invariant. (Present in 5/5.) Remove → tour/class booking territory; the trade's material base leaves the system.

4. **The money loop.** Charges formed by the program (session fees, rental charges, retail where present) settled through payments/deposits and resolved into invoices/receipts — with staff-side settlement where instructors are paid per session. (Present in 5/5.) Remove → a free roster; the business stops existing in the system.

Joint load-bearing analysis:

```text
1 alone            → brochure / price list
2 alone            → generic calendar / booking widget
3 alone            → rental inventory tracker
4 alone            → payment terminal
1+2 without 3+4    → class/trip schedule with no gear and no money (booking-form territory)
1+3 without 2+4    → catalog + gear room nobody schedules
2+3 without 1+4    → ad-hoc scheduling of stuff for free
1+4 without 2+3    → commerce over nothing deliverable
2+4 without 1+3    → generic appointment booking with payments
3+4 without 1+2    → pure rental counter (generic rental territory)
1+2+3 without 4    → operations below the business bar
1+2+4 without 3    → tour/class booking with payments — the closest failure mode
                     (tour-operator / activity-operator territory)
```

Domain binding: the legs are held together by water-sports content — the activities are water sports, the resources are water gear and craft, the qualifications are swim/dive qualifications, and the schedule's moving constraint is often the water's condition. The structural genus ("activity school/center operations") also serves non-water verticals (ski schools at two sampled vendors); water is this leaf's binding.

### L1 — Common Mature Structure

Present in most sampled products; expected by the market; not definitional:

- Customer/participant profiles carrying water-sports content: certifications, medical clearance, gear sizes, lesson/rental/purchase history.
- Participant qualification & safety records: diver certifications (with agency submission at the deep pole), medical clearance forms, swim-ability declarations, liability waivers (embedded module — the waiver loop's own Type is separate).
- Conditions-awareness: forecast panels (wind/swell/tide), tide-window slot machinery, conditions-driven reshuffling of the day plan.
- Online customer booking (widget/booking page) beside walk-in POS and payment links; agent/OTA distribution and channel management at the platform pole.
- Automated messaging: confirmations, reminders, schedule-change and cancellation notices (SMS/email).
- Session-execution surfaces: manifests, check-in, roll call, run sheets with guest notes/sizes.
- Instructor/guide settlements: hourly rates or commissions per session, payout tracking, payroll exports.
- Reporting/analytics: revenue, occupancy, top trips, tank usage, instructor performance; accounting exports.
- Staff roles and permissions; multi-location support at the larger pole.
- Retail POS and shop inventory (dive-retail pole deep; platform pole via POS module).
- Repair/work-order tickets for gear.

### L2 — Variant / Optional Structure

- Sport-vertical mix: dive-only vs surf/kite/windsurf/sailing multi-discipline vs paddle/rental-led vs multi-activity outdoor center.
- Business posture: school/lesson-led vs trip/charter-led vs rental-led vs retail-led (dive shop) vs resort/liveaboard (accommodation attached to the same operation).
- Conditions-coupling depth: forecast panel beside the schedule ↔ tide-state slot machinery ↔ manual condition entry ↔ none (pool/indoor or retail-led operations).
- Certification machinery depth: agency-integrated submission and skill sign-offs ↔ simple level labels ↔ none.
- Distribution posture: direct-only ↔ agents/resellers with tracked commissions ↔ OTA channel management.
- Offline operation: dock/vessel offline hubs and offline-first staff apps ↔ cloud-only.
- Pricing models: per-lesson/per-rental usage pricing ↔ seasonal tier pricing ↔ deposits/pre-authorization holds ↔ subscriptions/memberships (occasional).
- Scale: single school/shop ↔ multi-location group ↔ resort.
- Commercial model of the software itself: flat subscription ↔ per-booking/usage pricing ↔ per-seat tiers.

### L3 — Vendor-specific (research notes only)

- Thalassa: Mode C offline hub (local hub device, ~60s resync claim), 10-year waiver storage claim, hydro-alert cadence (30/7/1 day), ECB rate locking, liveaboard module, named agency list (PADI/SSI/NAUI/SDI/TDI/RAID/CMAS), flat-fee positioning vs per-booking-fee incumbents.
- Dive Shop 360: 120+ preloaded vendor catalogs / 15,000+ product images (vendor claims), named agency integrations (PADI/SSI/SDI/TDI/ERDI/PFI), AI-powered text responses, Google review requests.
- SurfCloud: WindGuru integration; 600 free SMS/month with €0.17 overage (vendor figures); per-lesson/per-rental pricing ("don't pay when you don't teach"); SnowCloud winter sibling.
- DiversDesk: Xendit payment integration; Green Fins / Reef-World partnership discount; tank-usage analytics; plan structure (user-account counts, manager roles).
- Bloowatch: "30+ connected OTAs" claim; module split (Activities/Rentals/Waivers/Channel Manager) on one shared core; named customer logos; no-commission posture.

## Rejected Findings (anti-overfit)

- **"Certification/agency integration defines the Type."** Rejected: dive-pole-deep (DS360, DiversDesk medical, Thalassa submission); SurfCloud has none; Bloowatch carries it only as module depth. The participant-qualification layer is common-mature, not the invariant.
- **"Conditions/forecast integration defines the Type."** Rejected: strongly present in the school pole (Bloowatch, SurfCloud + anchors) but not foregrounded at the dive-retail pole; pool courses and retail-led operations do not depend on it. Characteristic of the trade, not definitional.
- **"It's just tour/activity operator software applied to water."** Rejected: the tour-operator core (§26, processed) is itinerary/package products + dated departures + passenger bookings; this Type's center is the recurring daily session program over an equipment fleet with instruction/rental mixture and participant qualifications. The overlap (dive boat trips) is real but the centers differ.
- **"It's just class management (swim-school genus)."** Rejected: rentals, boats, conditions, and walk-in/tourist clientele are not class semantics; the swim school's learn-to-swim pedagogy machinery (level progression + makeup) is absent here.
- **"Retail POS defines the Type."** Rejected: dive-retail pole only; SurfCloud and DiversDesk run without foregrounded retail.
- **"Membership entitlements define the Type."** Rejected: the trade is per-session/per-rental transaction-shaped; memberships appear only occasionally.
- **"Online booking defines the Type."** Rejected: admin-side floor exists (all sampled products are operator-first); the paper-era operation satisfies the core without any customer-facing digital surface.
- **"Per-unit serial tracking defines the equipment leg."** Rejected: category-level occupancy timelines (SurfCloud) satisfy the managed-unit leg; serial-grain tracking (Thalassa) is depth.
- **"Waivers define the Type."** Rejected: the waiver loop is its own processed Type; embedded waiver modules are packaging variants (consistent with the digital-waiver pass's own finding).
- Marketing counters (30+ countries, 30+ OTAs, catalog counts, pricing figures) — not promoted to operational facts.

## Boundary Findings

| Neighboring Type | Seam | "Remove what → becomes the other Type" |
|---|---|---|
| **Tour Operator Management System** (§26, processed) | tour operator centers its OWN itinerary/package-shaped travel products + dated departures + passenger bookings for travellers; water sports centers the recurring daily session program (instruction + trips + rentals) over an equipment fleet with participant qualifications and conditions-coupled replanning. Dive boat trips are tour-shaped, but the water sports operation's center of gravity is the daily program + gear + instruction, not travel packages. Water sports operators appear on the SUPPLY side of tour/activity distribution (OTAs connect to them). | Remove the equipment fleet and the instruction/rental mixture, center multi-day itinerary packages → tour-operator territory. |
| **Swim School Management** (§28 sibling, processed) | swim school = learn-to-swim lesson business in a pool facility (swimmer records on family accounts, level/skill progression + first-class makeup machinery, enrollment-driven lesson money); water sports = open-water activity operation (lessons + trips + rentals; walk-in/tourist clientele; conditions-coupled; gear fleets; boats). | Replace the open-water program/rentals/trips with pool-based learn-to-swim pedagogy and family-account enrollment → swim-school territory. Overlap edge: a water sports center that also runs kids' swim courses. |
| **Sports Facility Management / Recreation Center Management** (§28 siblings, processed) | those center rentable SPACES (courts/fields/rooms) and entry entitlements; water sports has no bookable space — the resources are mobile craft and gear, and the program is delivered on natural water. | Remove craft/gear, add rentable spaces and entry entitlements → facility territory. |
| **Marina Management** (§18, processed) | marina = berthing system of record (berth inventory, berthing agreements, occupancy, berth money); water sports = program delivery over mobile resources. Adjacent at the waterfront; a water sports center may sit inside a marina but the object worlds differ. | Center the berth inventory and berthing agreements → marina territory. |
| **Boat / Yacht Charter Platform** (§18, processed) | charter = whole-vessel time rental as a platform-mediated transaction (qualification gating, handover, deposits); water sports boat trips are operator-delivered sessions with staff and manifests, not charters of a vessel. | Make the whole-vessel time rental the mediated transaction → charter territory. |
| **Digital Waiver Management** (§26, processed) | the waiver loop's own system of record; embedded waiver modules inside water sports products are packaging variants (that pass's own finding). | Center the release-document/signing/archive loop → waiver territory. |
| **Event Registration Platform** (§26, processed) | registration centers per-event intake with the roster as output; water sports runs a continuous daily operation (calendar + gear + staff + money) across a season. | Reduce to one-off event intake with a roster → registration territory. |
| **Generic rental/booking tools** (TWICE/Reservety-class; no dedicated leaf) | pure equipment rental without program sessions, staff ratios, or qualifications = rental territory; water sports adds the session program and its staff. | Remove the session program and staff → generic rental. |
| **Gym / Fitness Studio Management** (§28) | membership-entitlement businesses with recurring dues vs per-session/per-rental transaction businesses with seasonal staffing. | Center membership dues and entry entitlements → gym territory. |
| **Genus note** | the same product genus serves ski schools (Bloowatch ski-school vertical; SurfCloud's SnowCloud sibling) — the structural spine is "outdoor activity school/center operations"; water is this leaf's domain binding. No ski-school leaf exists in the directory; none requested. | — |

## Historical / Market-Sample Check

- **Paper-era lineage satisfies the four-leg core with no software**: the dive center or surf school of the 1980s–90s ran a wall whiteboard/day sheet (sessions, trips, staff assignments), a paper rental log (gear out/in per unit), a cash box with receipt book (money loop), paper registration + liability release + diver medical forms, and an instructor tally sheet. All four legs present; nothing in the core requires cloud, OTAs, SMS, or forecasts.
- **Regional spread**: Southeast-Asian dive resorts (DiversDesk's client base), Polish/Croatian kite/windsurf schools at campsites (SurfCloud), US/Caribbean/UK dive retail (Dive Shop 360), French/Spanish multi-activity water sports centers (Bloowatch) — the four-leg core is region-neutral; conditions vocabularies (Mediterranean vs Baltic vs tropical), agency ecosystems (PADI/SSI/CMAS), and payment rails are regional content inside a stable structure.
- **Scale spread**: single-school (SurfCloud) to multi-location/resort (Thalassa, Bloowatch) — same core at different scopes.
- **Genus check**: the same genus re-skinned for winter (SnowCloud) and ski schools (Bloowatch vertical) confirms the spine is activity-school/center operations; the water binding (natural water, water gear, water conditions, swim/dive qualifications) is what makes this leaf.

## Uncertainties

- All evidence is official product-page level; no help-center or manual article was fetched for any sampled product. Workflow mechanics below the page level (exact booking-state machines, waiver-gating enforcement details, settlement calculation rules) are not evidenced and are not asserted.
- Thalassa is early access: its unusually explicit workflow span is vendor-stated scope; deployment depth unproven. Its claims were used to map the workflow space, not to assert market prevalence.
- The prevalence of membership/pass products in this market was not directly evidenced (only the gym-genus analogy suggests occasional use) — held as variant without prevalence claim.
- Certification-submission mechanics (what exactly flows to agencies, turnaround, error handling) not researched at article level.
- Whether the dive pole's "Diver Medical" is a fixed industry form or per-operator configurable could not be verified from the fetched layer (DiversDesk says "customizable"; Thalassa says custom waiver templates — the medical form's fixity is unverified).
- EquipDash/SurfSlot/TIDEFORCE observations rest on search captures — market-structure claims only.
- OceanDojo unreachable — its existence corroborates the school-pole population but contributes no structural evidence.

## Final Synthesis

Water Sports Management is the operator-side system of record for a business that delivers water sports — a dive center or dive shop, a surf/kite/windsurf/sailing school, a kayak/boat rental and tour operator, a water sports center or resort. Its defining core is four jointly-held structures: the water-activity program of record (lessons/courses, guided trips, and equipment rentals configured with capacity, staffing, and pricing — the instruction+trip+rental mixture being the trade's shape); the scheduled session as the unit of daily operation (dated instances on a live calendar binding instructors, participant rosters, and the boats/gear they use, reshuffled through the day); the water-sports equipment and craft as managed resources (tracked units with availability, assignment, and upkeep); and the money loop (session/rental/retail charges settled through payments and resolved into invoices and staff settlements). Around this core, mature products add participant qualification and safety records (certifications with agency submission at the deep pole, medical clearance, swim-ability, embedded waivers), conditions-awareness (forecast panels, tide-window scheduling, conditions-driven replanning), multichannel selling (online booking, walk-in POS, payment links, agents/OTAs), automated messaging, session-execution surfaces (manifests, roll call), instructor settlements, reporting, and — at the resort pole — accommodation attached to the same operation. The Type is separated from tour-operator systems by its center (daily session program + gear vs travel packages), from swim schools by its open-water program and rentals (vs pool pedagogy), from facility systems by its mobile resources (vs rentable spaces), from charter platforms by its operator-delivered sessions (vs mediated vessel rentals), and from generic rental tools by its session program and staff. The same structural genus also serves ski schools; water is this leaf's domain binding.
