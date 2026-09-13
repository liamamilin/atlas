# Research Notes — Sports Facility Management

## Research Goal

Understand what "Sports Facility Management" software actually is from real products: the operator-side system used to run a sports facility (multisport complexes, ice arenas, turf/field houses, court facilities, batting cages, community venues) as a business. Determine the defining core, the standard capability set, the variant axes, and the boundary against neighboring Types — especially the seams left by processed sibling passes: Sports Court Booking (demand side), Recreation Center Management (Dash spans both), Sports Academy Management (capability slice), Racquet Club Management / Golf Course Management (sport-specific semantics), Gym/Climbing passes ("physical plant" characterization — to verify), League Management Platform, Facility Management System (§17), Amenity Booking Platform (§17), Parks & Recreation Administration (§24).

## Initial Boundary

- Hypothesis: operator-side system of record for a sports venue — rentable-space inventory (courts/ice/fields/rooms) + bookings/rentals + facility-run programming (leagues/camps/clinics) + money (fees, POS, invoicing) + reporting.
- Nearest neighbors (from sibling passes): Sports Court Booking (player demand side — its pass left an explicit forward flag: "proposed discriminator = operator side (generic rentable sports spaces' system of record) vs demand side"), Recreation Center Management (its pass left a forward flag: "Dash spans both Types on one platform — that pass should ratify the seam from its side; test: remove the membership/entry leg and the multi-activity community posture → sports-facility territory"), Sports Academy Management ("facility/resource scheduling is a bundled module inside academy software — capability-slice pattern"), Sports Club Management ("rentable-space inventory and booking channels; a club's facility bookings are one module"), Racquet Club Management ("generic rentable spaces (halls, rinks, fields); lacks racquet court semantics, member governance, and programming"), Golf Course Management ("generic rentable spaces by hour; lacks tee-time slot semantics, per-player green fees and the round lifecycle"), Gym Management System / Climbing Gym Management (both characterized this leaf as "manages the physical plant and its operations" — **this characterization needed verification**), League Management Platform, Facility Management System (§17), Amenity Booking Platform (§17), Parks & Recreation Administration (§24), Event/Venue Management (§26).
- Risk 1: collapse into Sports Court Booking (two sides of one transaction). Risk 2: collapse into Recreation Center Management (same vendor genus serves both). Risk 3: confusion with §17 Facility Management System (building maintenance) — the gym/climbing passes' "physical plant" wording points at §17 semantics; the market evidence must decide what this leaf's products actually manage.

## Research Questions

1. What is the space inventory model (resources, types, sub-resources, groups, blocking rules, availability configuration)?
2. What is the booking/rental lifecycle (request vs instant booking, approval, contracts, permits, invoicing, refunds, rollovers)?
3. How is money structured (products bound to bookings, flat vs hourly, seasonal date ranges, peak/off-peak, POS, passes, memberships)?
4. How does facility-run programming (leagues, classes, camps, clinics, parties) occupy the same resources, and how deep does the competition machinery go?
5. Who are the customers (individuals, families, organizations/teams) and how do accounts/governance work?
6. What interfaces exist (scheduling calendar/grid, booking manager, registration admin, customer portal, POS, displays, reporting)?
7. What rules matter (double-booking prevention, buffers, lead times, cancellation, role-based permissions)?
8. Where are the boundaries vs the sibling Types listed above — and does the "physical plant" characterization from the gym/climbing passes hold?

## Representative Products

| Product | Pole | Why sampled |
|---|---|---|
| **Dash** (DaySmart Recreation; US; 20+ years lineage) | full-suite sports facility management | self-labels "sports facility management" / "Recreation Facility Management Software"; deep Tier-1 help center (Booking Manager, Resources, Program Registration, Payments, Finance); spans multisport/ice/turf/court facilities AND community rec centers + parks & rec — the exact product the recreation-center pass flagged for seam ratification |
| **FinnlySport** (Minneapolis, US) | full-suite, ice-arena/sportsplex/municipal heritage | "Sports and recreation management software… on the field, on the ice, on the court and with your community"; facility scheduling grids, activity/team registration, rules-based league scheduling, membership/punch passes, POS, digital displays; industries span ice arenas, sportsplexes, municipalities, higher-ed |
| **AllBooked (by Skedda)** | booking-centric pole | "Booking platform for athletic facilities & community spaces"; spaces + rules/roles engine + pricing/payments + memberships + analytics — no programming suite, no POS; proves programming/POS are not definitional; multi-sport/golf simulators/batting cages/fields/courts verticals |

Rejected/abandoned samples (source-access limitations, see Sources): **EZFacility** (category-named "sports facility scheduling & management" vendor — all fetched paths 403 ×2; also unreachable in the racquet-club pass), **eSoft Planner** (403 ×2 on www and bare domain), **RAMP Interactive** (403 then timeout), **Bond Sports** (empty responses ×2). **Uplifter** fetched but is a club/association management platform (memberships/registrations for gymnastics/skating/cycling governing bodies) — Product Mismatch: belongs to the Sports Club / class-management family, not this Type; not sampled.

Boundary context: **CatchCorner** (demand-side rental marketplace, integrated into Dash as a channel), **SportNinja** (league scoring/standings, integrated), **RFAM** (facility & equipment maintenance, integrated), **LiveBarn** (streaming, integrated) — all appear in Dash's integration list, which is itself boundary evidence for what this Type does NOT natively do.

## Sources

Fetched 2026-09-09 (official vendor pages):

- Dash — homepage (https://www.dashplatform.com/), multisport vertical (https://www.dashplatform.com/facilities/multisport), community rec center vertical (https://www.dashplatform.com/solutions/community-rec-center-software/)
- Dash Help Center (https://help.dashplatform.com → https://help.daysmartrecreation.com/): Rental Booking collection; Initial Setup for Booking Manager (https://help.daysmartrecreation.com/en/articles/9301118); Booking Manager Admin Setup (https://help.daysmartrecreation.com/en/articles/9554631); Resources (Early Access) (https://help.daysmartrecreation.com/en/articles/9312273); Initial Setup collection listing (74 articles)
- FinnlySport — homepage (https://finnlysport.com/), solutions page (https://finnlysport.com/solutions)
- AllBooked — homepage (https://www.allbooked.com/)
- Sibling passes: research/sports-court-booking.md, research/racquet-club-management.md, research/golf-course-management.md, research/recreation-center-management.md, research/sports-academy-management.md, research/sports-club-management.md, research/gym-management-system.md, research/climbing-gym-management.md (seam flags recorded in STATUS.md)

Evidence layers used below: **A** = directly observed on an official page of a specific product; **B** = cross-product commonality across the sample; **C** = canonical inference from comparison + Type-boundary reasoning.

## Product A — Dash (DaySmart Recreation)

### Key observations (Layer A unless noted)

- Self-labels: homepage title "Recreation Facility Management Software"; hero "Unleash the potential of your sports facility — Simplify scheduling, streamline operations, and unlock new revenue opportunities"; multisport vertical: "All-In-One Sports Facility Management Software… all-in-one multisport facility scheduling and management software". Verticals: ice sports, multisport, parks & rec, soccer complexes (turf), athletic courts, community rec centers, higher-ed rec facilities, baseball facilities, athletic performance gyms, gymnastics, aquatics, driving ranges. "For over 20 years, we've evolved alongside our industry."
- **Centralized scheduling**: "Efficiently manage all of your fields, rinks, courts, and rooms in one centralized calendar. Simply schedule and set up spaces for sport-specific configurations, leagues, events, and more." "Easily customize schedules by sport with flexible configurations for hockey, soccer, basketball, and more." "Create your whole season of schedules, leagues, recurring classes… with season and program planning features." "Eliminate double bookings with automatic conflict checks built right into the system."
- **Resources** (help center, Tier 1): "The Resource Management tool allows you to create, customize, and organize assets like rooms, courts, fields, or equipment within your facility. Resources aren't only for rentals: they're also used to schedule program events like classes, camps, and games." Resource = "a specific bookable asset, like Court 1, Studio A, Feld 1, or Party Room"; rentable directly to customers OR assigned to program events. **Resource Type** = category (Basketball Courts, Indoor Fields) carrying shared Booking Options/T&C. **Resource Group** = cross-location collections ("All Ice Rinks across different facilities") for consolidated reports. **Sub-resources** = "split a field for multiple team practices" (admin-side only; not online-bookable). **Blocking Rules** = "block one or more resources when a specific resource has been booked" (e.g., an "Entire Facility" resource blocks all courts/rooms). Location required per resource; multi-location databases.
- **Booking Manager** (help center, Tier 1): "provides the ability to create customized rentals including contracts, as well as terms and conditions." Online Booking is an **add-on** (default portal name "Rentals"). Authorizations: Booking Create/Edit, Booking Delete. **Products**: "Every booking must be tied to a product… Products define what type of booking is being offered (such as court rental, birthday party, or private lesson) and control pricing, categories, and online visibility"; flat rate vs hourly. **Booking Options**: bookable type + online visibility; **date ranges** (seasonal pricing, recurring year over year); **availabilities** (start/end time, days of week, block size, buffer size, minimum booking duration); **fees** (products, flat/hourly, auto-add to cart, online-enabled). Online booking states: Disabled / Visible Only / **Request Only (Require Admin Approval)** / Request Only (hide price) / Book (signed in) & Request (not signed in) / Book Only (Force Purchase). Min/max lead times ("minimum days and/or hours in advance"). **Terms and Conditions** attachable at booking-option/event-type/resource level; customer initials recorded on the **Booking Contract**. **Event Types** for bookings (Wedding Event, Camp Site Rental, Indoor Field Rental, Outdoor Field Rental) with custom forms, event fee suggestions, invoicing toggle. Birthday-party packages as products. Resource contact gets reservation notifications + follow-up tasks.
- **Booking operations**: Availability Search ("find open time slots across your resources and create bookings directly from the results"); "Booking Events, Rollover, Editing and Invoices — Create, copy, edit, and invoice bookings… manage events, rollovers, and refunds"; **Permit Printing** ("print permits for reservations and rentals directly from the Event Search page"); passes can pay for online bookings; booking reports "track bookings, revenue, and utilization".
- **Registration/programming**: "Create different types of programming, including classes, camps, clinics, leagues, private lessons, and more"; "Enable individual, team, and family bookings as well as register and manage team rosters"; "Customize forms, waivers, and payment plans"; "set roster maximums and automatically activate waitlists". Program Types organize offerings. Events with rosters (add customers, collect payment, check in attendees, drop roster members); Event Capacity; make-ups; Event Import (CSV bulk upload of "events, games, and schedule blocks").
- **Revenue**: "Optimize your space and make more money per square foot with parties and one-off events… concessions and Point of Sale (POS) integrations as well as equipment and space rentals built right into the system"; "set peak/off-peak rules and seasonal rate adjustments"; memberships ("encourage repeat customers") and free trials; Touch Screen POS; cash drawer; gift cards; donations; tax rates; fund accounting (Product Funds); gratuity on invoices.
- **Customers**: Customer Types (participant/organization — "Organization Customer Type"), family members, customer tags for segmentation; marketing (email/SMS, Constant Contact, Twilio); Location Check-in; kiosks; Customer Player Cards; waiver management (expiry/renewal prompts); digital signatures (Dropbox Sign).
- **Staff**: Employee Setup, Roles & Authorizations; employee/instructor rates (hourly/flat/percentage); staff schedules (referees) displayed on the Calendar; task management.
- **Municipal flavor**: GIS Mapping ("import geographic zone boundaries, and set up residency areas to support resident pricing"), Residency Pricing (resident/non-resident rates) — parks & rec deployment features.
- **Integrations** (boundary evidence): SportNinja ("Generate real-time digital scoring and player stats with your leagues"; syncs season data, displays schedules and standings in the Customer Portal); RFAM ("Manage and maintain your assets and inventory management"; "connect facility & equipment management workflows with customer maintenance requests"); LiveBarn (streaming); **CatchCorner** ("List your space for rent on the largest marketplace for sport facility rentals"); Learn to Skate USA + USA Hockey (external membership verification at registration/check-in).
- Rec-center vertical page: "Manage Your Community Recreation Center and Members in One Platform… oversee all business operations and memberships at your recreation facility center" — memberships front-and-center in the rec-center posture; the same scheduling/resources/POS machinery underneath.

## Product B — FinnlySport

### Key observations (Layer A unless noted)

- Self-labels: "Sports and recreation management software that gives you more time where it matters most - on the field, on the ice, on the court and with your community." "We don't just power facilities, we support them."
- Solution set: **Facility Scheduling** ("Dynamic grids make scheduling a breeze"); **Activity Registration** ("Register online and check in digitally"); **Team Registration** ("Extend invitations and manage payments seamlessly"); **League Scheduling** ("Rules-based automated game scheduling"); **Membership Management** ("Punch passes, facility access control, digital check-ins and more"); **Point of Sale** ("Touch-based technology for check-ins or selling merchandise & concessions"); **Communications**; **FinnlyConnect / Mobile App**; **Digital Display** ("Communicate schedules, announcements & locker room assignments or use as a menu board").
- Facility scheduling detail (solutions page): "View all your spaces simultaneously, avoid double-bookings, and optimize facility usage with real-time availability"; visual drag-and-drop; **multi-facility management**; mass edit; "Slotted maintenance blocks between events"; repeating events; **batch invoice generation**; automatic locker-room assignment.
- Programming detail: "One system for all activity types, including drop-in/single sessions and general admission ticketed events"; "Sync everything to your Facility Schedule"; duplicate previous season's activities. Team registration: "Registered teams transfer directly to League Scheduling"; players register and pay online; digital waivers; roster invitations; "See who's paid and who needs a nudge".
- League scheduling detail: "powerful & customizable rules-based scheduling engine… multi-sport automated game scheduling"; blackout dates; "Integrate to nationally recognized team management & results sites"; custom stats & standings. — League machinery is native here (deeper than Dash's integrate-out posture).
- Membership detail: "Variety of membership types & frequencies"; QR code check-ins synced with POS; member photos at check-in; "Integrated USA Hockey and Learn to Skate USA verification".
- POS detail: front desk / pro shop / concessions; "Process multiple items - food, merchandise, rentals, sessions - in one simple transaction"; inventory tracking; tablet-compatible; shift-based sales tracking; daily close-out.
- Industries: Ice Arenas, Sportsplexes, Higher Education Sports Facilities, Municipalities, Parks & Recreation, Aquatic Centers, Sports Associations, Community Centers, Soccer Complexes, Fitness Facilities, Athletic Fields, Pickleball Courts. Testimonials: multi-location operator (Edge Sports Global), ice arenas (Brett Ice Arena — "scheduling, invoicing, digital displays, and online platform"), a Parks and Recreation Director (City of Marshall, MN), a Facility Manager (Warrior Ice Arena).

## Product C — AllBooked (by Skedda)

### Key observations (Layer A unless noted)

- Self-labels: "Booking platform for athletic facilities & community spaces"; "Bookings, payments, automation for any space"; "trusted by over 4,000+ venues for booking, memberships, payments, and automation". Powered by Skedda (login at app.skedda.com?product=ab).
- Sports verticals: Multi-sport, Golf Simulators, Baseball & Softball (batting cages), Fields & Pitches, Basketball Courts, Cricket Clubs, Badminton Courts, Tennis Courts, Rec Centers — plus non-sports (dance/music studios, coworking, therapy clinics, event venues): the booking machinery is space-generic, the sports market is one application of it.
- Core pitch: "Simple booking platform: Let customers easily book spaces online, manage schedules, and fill up available time slots"; "Monetize your spaces: Increase your revenue with rules-based pricing and integrated payments"; "Automate manual work: Create custom booking rules, quotas, integrations, repeat bookings, and more."
- **Rules & Roles engine**: booking conditions ("Coaches can reserve the gymnasium for basketball practice between 6 AM and 8 AM"); access & visibility rules (VIPs → premium rooms); add-ons (AV equipment, catering); memberships (advance-booking windows: "Book a soccer field no more than 2 weeks in advance"); buffer time rules ("30 minutes added between fitness classes for equipment sanitization"); quotas ("Limit event bookings to 4 hours per day per organizer"); repeat bookings ("Reserve the swimming pool every Thursday at 5 PM for team practice"); cancellation policies ("Allow event cancellations up to 48 hours before the booked time for a full refund"); check-in prompts.
- Pricing & payments: smart pricing rules ("dynamic pricing based on time, location, or demand"); payment timing options (upfront or after); Stripe Connect processing.
- Space showcasing: images, descriptions, tags, clear pricing & availability.
- Analytics: "Track usage patterns, revenue, and customer trends."
- Integrations: access management (automatic door access), lighting & HVAC (energy when unused), accounting systems.
- **No programming suite** (no leagues/classes/camps as managed objects), **no POS**, **no roster/check-in machinery for programs** — the booking-centric pole.

## Cross-product Comparison

| Structure | Dash | FinnlySport | AllBooked | Layer |
|---|---|---|---|---|
| Facility's spaces held as identified bookable units ("fields, rinks, courts, and rooms" / "all your spaces" / "any space") | ✓ (Resources, types, sub-resources, groups) | ✓ (facility scheduling grids, multi-facility) | ✓ (spaces with images/tags) | B |
| Operator-configured bookable time (availability windows, block sizes, buffers) | ✓ (Booking Options: availabilities, block size, buffer, min duration) | ✓ (dynamic grids, maintenance blocks between events) | ✓ (availability rules, buffer time rules) | B |
| Booking/rental as the unit of transaction with a lifecycle | ✓ (Booking Manager: request/approval states, contract, invoicing, refunds, rollovers, permits) | ✓ (scheduling + invoicing; team payments) | ✓ (booking + cancellation policies + check-in) | B |
| Charges raised against bookings/usage (time-based, seasonal/peak pricing) | ✓ (products flat/hourly, date-range seasonal fees, peak/off-peak rules) | ✓ (batch invoicing; POS transactions) | ✓ (rules-based/dynamic pricing, Stripe payments) | B |
| Revenue/utilization reporting | ✓ ("bookings, revenue, and utilization"; 60+ standard reports) | ✓ ("optimize facility usage"; reporting) | ✓ (usage patterns, revenue) | B |
| Conflict prevention machinery | ✓ (automatic conflict checks, blocking rules, buffers) | ✓ (avoid double-bookings, maintenance blocks) | ✓ (booking conditions, quotas, buffers) | B |
| Facility-run programming (leagues/classes/camps/clinics) occupying the same resources | ✓ (classes, camps, clinics, leagues, private lessons; rosters, waitlists) | ✓ (activity/team registration; rules-based league scheduling) | — (absent) | B (2/3) |
| Online customer self-service (portal/app: book + register) | ✓ (Customer Portal; online booking add-on) | ✓ (FinnlyConnect portal + mobile app) | ✓ (online booking is the product) | B |
| Memberships / passes | ✓ (membership products, required memberships, passes pay for bookings) | ✓ (punch passes, access control, QR check-in) | ✓ (memberships with booking privileges) | B |
| POS (concessions/pro shop/front desk) | ✓ (TSPOS, cash drawer) | ✓ (touch POS, inventory) | — | B (2/3) |
| Customer database with segments (individuals/families/organizations) | ✓ (customer types incl. Organization, tags) | ✓ (member accounts, team managers) | ○ (user roles) | B |
| Waivers / digital forms | ✓ (waiver management, custom forms, digital signatures) | ✓ (digital waivers on registrations) | ○ (custom fields/add-ons) | B (2–3/3) |
| Check-in / kiosk / access control | ✓ (location check-in, kiosks, player cards) | ✓ (QR check-ins, access control) | ✓ (check-in prompts; access-management integration) | B |
| Staff roles & permissions | ✓ (roles & authorizations: Booking Create/Edit/Delete, Resource Management) | ○ (implied) | ✓ (roles in rules engine) | B |
| League competition machinery depth | ○ (leagues as programs; scoring/standings via SportNinja integration) | ✓ (native rules-based game scheduling, stats & standings) | — | A→variant |
| Multi-location / multi-facility | ✓ (locations, resource groups) | ✓ (multi-facility management; multi-location testimonial) | ○ (venues) | B |
| Municipal/residency machinery (GIS, resident pricing) | ✓ (GIS mapping, residency pricing) | ○ (municipality industry listed) | — | A (1/3) — variant |
| External membership verification (USA Hockey, Learn to Skate) | ✓ | ✓ | — | B (2/3) |
| Demand-side marketplace distribution | ✓ (CatchCorner integration) | — | — | A (1/3) — optional |
| Asset/maintenance management | ○ (RFAM integration — external) | ○ ("maintenance blocks" as scheduling gaps only) | ○ (lighting/HVAC integration) | B — integrated out |
| Digital signage / locker-room assignment | — | ✓ (digital displays, auto locker-room assignment) | — | A (1/3) — optional |

## Canonical Model (L0–L3)

### L0 — Defining Invariant

The operator-side system of record for a sports facility, holding three jointly-needed structures:

1. **The facility's rentable-space inventory of record** — the venue's spaces (courts, ice, fields, turf, cages, rooms, simulators) held as individually identified bookable units over operator-configured bookable time (availability windows, block sizes), in one system, with conflict prevention over the shared calendar. Remove → a generic scheduler/CRM with no venue capacity of record.
2. **The booking as the unit of transaction** — a party (person, team, organization) holds a specific space for a specific time, carried through a lifecycle (request/reserved → confirmed/paid → used/completed, with cancellation/refund paths) and recorded in the facility's history. Remove → a directory or a bare embedded booking widget with no facility-side memory.
3. **The facility's money record** — charges raised against bookings and usage (fees structured by duration, season, day/time, peak rules), settled (invoiced, paid, POS) and accumulated into the facility's revenue and utilization record. Remove → a calendar with no business memory; the "management" in the Type name dies.

Jointly load-bearing: 1 alone = a space list; 2 without 1 = a booking widget over nothing; 3 without 1+2 = a payment terminal; 1+2 without 3 = a shared calendar below the Type; 2+3 without 1 = generic appointment scheduling; 1+3 without 2 = a rate card nobody books against.

### L1 — Common Mature Structure

- Facility-run programming occupying the same resources: leagues, classes, camps, clinics, private lessons, parties/tournaments — with registration (individual/team/family), rosters, capacity/waitlists, waivers, make-ups
- Online customer self-service: portal/app for booking rentals and registering for programs
- Memberships and passes (punch passes; memberships gating products/bookings)
- POS for front desk/concessions/pro shop; integrated payment processing; invoicing
- Customer database (individuals, families, organizations/teams) with tags/segments; marketing communications (email/SMS/push)
- Reporting/analytics: utilization, revenue by category, program performance
- Staff machinery: roles/authorizations, staff schedules (referees/instructors) on the calendar, pay rates, time clock
- Check-in (digital/kiosk/QR), player cards, access control
- Waivers and custom forms; contracts/terms acceptance
- Multi-location/multi-facility management

### L2 — Variant / Optional Structure

- Municipal/parks-&-rec deployment: residency pricing (GIS zones), fund accounting, permit culture
- Higher-ed recreation facilities
- Sport verticals (ice, turf/soccer, courts, baseball/softball, gymnastics, aquatics, driving ranges, golf simulators) — mostly packaging, not structure
- League machinery depth: native rules-based game scheduling + standings (FinnlySport) vs leagues-as-programs with scoring integrated out (Dash/SportNinja)
- Demand-side marketplace distribution (CatchCorner-style channel integration)
- External body membership verification (USA Hockey, Learn to Skate USA)
- Asset/maintenance management (RFAM-style integration), streaming (LiveBarn), lighting/HVAC/access hardware integrations
- Digital signage, locker-room assignment
- Booking-centric vs full-suite posture (AllBooked vs Dash/FinnlySport)

### L3 — Vendor-specific (research notes only)

- Dash: "Booking Options"/"Event Types"/"Resources" terminology; Booking Contract with authorized-signature text; permit printing from Event Search; Online Booking as paid add-on with default portal name "Rentals"; 730-day max booking window; 15-minute minimum block size; Request Only (hide price) state; fund accounting; GIS residency; Customer Player Cards; kiosk types; RFAM/SportNinja/LiveBarn/CatchCorner/Learn to Skate/USA Hockey integrations.
- FinnlySport: FinnlyConnect portal; digital displays as menu boards; automatic locker-room assignment; "FinnlyFamily" support positioning; batch invoice generation.
- AllBooked: Skedda lineage (app.skedda.com login); Stripe Connect; ROI calculator ("a typical AllBooked venue sees 15% more bookings" — marketing claim, not evidence); rules examples (coach 6–8 AM gymnasium, 48-hour cancellation).

## Vendor-specific Findings

- Dash's Online Booking is an **add-on** (paid, enabled per database) — online self-service is not structurally required even in the fullest suite; admin-side booking is the floor.
- FinnlySport natively automates league game scheduling (rules-based, blackout dates, standings); Dash delegates scoring/standings to SportNinja while managing leagues as programs. Same Type, two postures on competition machinery.
- AllBooked's rules engine expresses governance as booking conditions/quotas/membership privileges — a lighter-weight realization of the same access-governance idea that racquet-club products implement as member privilege rules.
- Dash's GIS/residency pricing and fund accounting are parks-&-rec deployment machinery riding on the same core — evidence that the municipal pole is a variant, not a separate Type.

## Boundary Findings

1. **vs Sports Court Booking (demand side) — RATIFIED from this side** (discharges that pass's forward flag). The proposed discriminator holds on evidence: Dash/FinnlySport/AllBooked are the venue operator's system of record (space inventory of record, booking lifecycle, money accumulation, staff machinery); Sports Court Booking is the player's demand-side loop where the venue is a third party. Direct vendor evidence of the seam: Dash integrates **CatchCorner** specifically to "list your space for rent on the largest marketplace for sport facility rentals" — the marketplace is a distribution channel of this Type, not this Type. Reciprocal test: add operator-of-record governance (inventory of record, staff, revenue accumulation) to a demand-side product → it becomes this Type; strip them → it is the demand side.
2. **vs Recreation Center Management — RATIFIED from this side** (discharges that pass's forward flag). One software genus (Dash serves both postures on one platform; FinnlySport lists both Community Centers and Sportsplexes as industries), two defining cores. Seam = the operated unit + the access relationship: the rec-center posture centers the facility's membership/entry relationship with its community (Dash's rec-center page: "oversee all business operations and **memberships**"); the sports-facility posture centers the venue's rentable capacity and its bookings/programming/revenue. Remove the membership/entry leg and the multi-activity community posture → sports-facility territory (the rec-center pass's own test, confirmed from this side). Reciprocal: remove the rentable-space/rental center → rec-center territory.
3. **vs Racquet Club Management** — confirmed from this side: racquet products center racquet-court semantics (play-shape booking types, member governance, pros); this Type's spaces are generic venue spaces (Dash: "fields, rinks, courts, and rooms"; AllBooked: multi-sport/cages/fields/courts). A suite's facility-booking module (Jonas: "meeting rooms, tennis courts, swimming lanes, golf simulators, you name it") is facility-generic — consistent with the racquet pass's reading.
4. **vs Golf Course Management** — golf's unit is a starting position on a shared course with per-player green fees and a round lifecycle; this Type rents exclusive time on a space. No tee-sheet semantics observed in any sampled product.
5. **vs Sports Academy Management** — capability-slice pattern confirmed: Dash and FinnlySport both carry class/camp/lesson programming, but as one capability of the venue system; academy software centers the athlete population + program portfolio + enrollment + tuition loop. Upper Hand (per that pass) bundles facility scheduling inside academy software. Keep-both with center-of-gravity seam.
6. **vs Sports Club Management** — the club is a member organization fielding teams; the facility is a venue selling time and programs. A club's facility bookings are one module (that pass's wording, consistent with evidence).
7. **vs League Management Platform** — facility-run leagues exist to fill the facility's spaces (house leagues as programming); the League Management Type administers competition between organizations (fixtures, results, standings as the center). FinnlySport's native league scheduling blurs the edge — the seam is center of gravity, and joint review with that pass is recommended if it processes later.
8. **vs Facility Management System (§17) — CORRECTION to sibling-pass characterization**: the gym-management and climbing-gym passes described this leaf as "manages the physical plant and its operations." The sampled evidence contradicts that wording: these products manage the venue's **commercial operation** (bookable inventory, bookings, programming, money) — physical-plant maintenance appears only as an external integration (Dash↔RFAM: "connect facility & equipment management workflows with customer maintenance requests") or as scheduling gaps ("slotted maintenance blocks between events" — FinnlySport). Building work orders/preventive maintenance belong to §17 Facility Management / Building Maintenance territory. The gym passes' seam (member relationship vs venue operation) still holds directionally, but the "physical plant" wording should be read as "venue operation," not building maintenance.
9. **vs Amenity Booking Platform (§17)** — amenity booking serves a closed residential population over a building's shared facilities; this Type serves an open renter/participant population over a sports venue's capacity. AllBooked spans both markets with one engine — the machinery is adjacent; the population and venue differ.
10. **vs Parks & Recreation Administration (§24)** — the department's season-cycled program catalog + community-wide facility inventory vs one operator's venue system of record. Dash's parks-&-rec vertical (GIS residency, fund accounting) shows the machinery overlapping at the municipal pole; the seam is the operated unit (department vs venue).
11. **vs Event/Venue Management (§26)** — parties and one-off events here are productized bookings against the venue's spaces (Dash: party packages as products; event types like Wedding Event); the §26 Type centers the event itself (attendees, agenda, registration at event scale).
12. **vs Appointment Scheduling Application** — generic appointments have no sport-typed space inventory, no venue mediation, no facility revenue record.

## Historical / Market-Sample Check (§24)

Paper-era sports facility (arena/field house/complex): a rental ledger book (who rented which rink/hall/field for which hour, at what fee, deposit taken), a wall calendar or booking board of committed times, program/camp sign-up sheets, a cash box and receipt book. This satisfies all three L0 legs — space inventory of record, bookings with lifecycle, money raised and accumulated — with no online booking, no POS, no memberships, no portals. Regional variants (Canadian ice-arena ice bookings and permits — Dash's permit printing echoes municipal permit culture; European multi-purpose halls; municipal athletic-field permits) fit the same core. The definition therefore does not depend on the current SaaS implementation: online self-service, POS, memberships, marketing, and check-in hardware are all era-current additions, not definitional.

## Uncertainties

- **EZFacility / eSoft Planner / RAMP Interactive / Bond Sports unreachable** (403/timeout/empty ×2 each) — these are category-named vendors (EZFacility and eSoft Planner explicitly market "sports facility management software"); their absence means the sample lacks two mid-market poles. Assertion strength kept at cross-product (B) for all common structures; nothing rests on those vendors.
- Precise operational parameters (block-size minimums, lead-time maximums, party-package mechanics) observed only in Dash's help center — held as Layer A product detail, not generalized.
- The exact market share/ordering of full-suite vs booking-centric postures is unknown; the sample suggests both exist (AllBooked claims 4,000+ venues) but relative weight is unverified.
- Whether native league-scheduling depth (FinnlySport) or integrate-out (Dash) is the market norm is unresolved — held as a variant axis.

## Final Synthesis

Sports Facility Management is the operator-side business system of record for a sports venue. Its defining core is three jointly-held structures: the facility's rentable-space inventory of record (identified spaces over operator-configured bookable time, with conflict prevention); the booking as the unit of transaction (a party holds a space for a time, through a request→confirmed→used lifecycle, recorded in facility history); and the facility's money record (charges structured by time/season/peak, settled and accumulated into revenue/utilization reporting). Around this core, mature products add the programming suite (leagues/classes/camps/clinics occupying the same resources), online self-service, memberships/passes, POS, customer CRM/marketing, staff machinery, check-in/waivers, and multi-location management. The Type's identity is the venue operator's side: strip the operator-of-record side and you have the demand-side booking Types; add membership/entry as the center and you drift to Recreation Center Management; add sport-specific court/tee semantics and you are in Racquet Club / Golf Course Management; add athlete-enrollment as the center and you are in Sports Academy Management. Building maintenance is NOT this Type (that is §17 Facility Management) — a correction to two sibling passes' wording. The leaf stands as an independent Type; no directory change proposed.
