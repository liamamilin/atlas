# Research Notes — Recreation Center Management

## Research Goal

Understand what software sits under the directory leaf "Recreation Center Management" (§28 Sports, Fitness & Recreation, line 2049, between "Recreational Fishing Application" and "Sports Marketplace"): what the operated unit is, who uses the software, what objects exist inside it (facility, members, entitlements, activities, rentals, money), how the daily operating loop works, and where the boundary lies against the already-processed neighbors — above all **Parks & Recreation Administration (§24)**, whose pass documented the same software genus from the department angle and listed "memberships/passes with scan entry" as capability-not-core and "community center deployments" as variant. Five processed §28 siblings (gym-management-system, fitness-membership-management, fitness-class-booking, fitness-studio-management, climbing-gym-management) each pre-hung an "adjacent/institutional" boundary flag pointing at this leaf; this pass discharges them.

## Initial Boundary (hypothesis before research)

- Hypothesis: the recreation center (community/municipal center, YMCA/JCC, university campus rec, private multi-activity facility) as an OPERATED FACILITY — the software's center of gravity is the building and its population (members), not a department's community-wide program catalog. Expected core: facility + membership/access + scheduled activities + rentals.
- The sharp question: is this a distinct Type or a deployment variant of Parks & Recreation Administration? The parks pass explicitly said "the same software family is also deployed by YMCAs, universities, HOAs, and community centers; the products are multi-market." Evidence must decide whether the rec-center deployment has structures the parks core lacks (expected: membership/entitlement validated at entry) and whether parks structures (season cycle, residency, community-wide reservation inventory) are absent/optional here.
- Other neighbors: Gym Management System (commercial membership business), Fitness Membership Management, Fitness Class Booking, Fitness Studio Management, Climbing Gym Management (single-activity verticals), Sports Facility Management (unprocessed), Amenity Booking Platform (§17), Membership Management System (§25), Facility Management System (§17), Event Registration Platform (§26).

## Research Questions

1. What is the operated unit — the facility, the membership base, the program catalog, or the department?
2. How is access to the facility granted, validated, and recorded? What entitlement objects exist (memberships, passes, daily admissions, guest privileges, fee-exempt eligibility)?
3. What is the entitlement lifecycle (sell, renew, freeze/hold, cancel, expire) and where is it administered?
4. How do scheduled activities (classes, programs, camps, leagues, drop-ins) relate to the facility's spaces and to memberships?
5. How do space rentals/reservations work, and how do they conflict-control against activities?
6. What role does the front desk / check-in loop play (visits, occupancy, identity checks)?
7. Which structures are municipal-only, nonprofit-only, campus-only — i.e., variant machinery, not Type identity?
8. Where exactly is the seam to Parks & Recreation Administration, and can each Type exist without the other's machinery?

## Representative Products

| Product | Vendor | Segment / posture | Philosophy | Evidence tier reached |
|---|---|---|---|---|
| Daxko Operations | Daxko | YMCAs, JCCs, Boys & Girls Clubs (nonprofit community centers) | membership-first nonprofit CRM + operations | Tier-2 product/capability pages (help center JS-blocked) |
| nextRec (Xplor Recreation; formerly PerfectMind) | Xplor Technologies | municipal rec centers + parks & rec + YMCAs/JCCs | all-in-one cloud suite | Tier-2 homepage + feature pages (KB JS-blocked) |
| Fusion | InnoSoft Canada | university/campus recreation + municipalities | access-control-first rec management | Tier-2 product pages (KB SSO-blocked) |
| Dash | DaySmart Recreation | private sports facilities + community rec centers + higher-ed rec | business-oriented facility operations | Tier-2 solution pages + **Tier-1 help center** |
| RecTrac | Vermont Systems | municipal departments AND rec centers (genus anchor; parks pass's product) | classic module family | **Tier-1** Pass Module Guide (HelpTrac KB) |

Selection rationale: four customer tiers (nonprofit community, municipal, university, private/commercial), different philosophies (membership-first, suite, access-first, business-first), plus RecTrac as the Tier-1 genus anchor already deeply documented by the parks pass — reused here only for the membership/access machinery the parks pass held out of its core.

## Sources

- Daxko — daxko.com (home; /products/daxko-operations; /capabilities/facility-access) — fetched 2026-09-09
- nextRec / Xplor Recreation — nextrec.com (home; /features/membership-management; /features/facility-management-software) — fetched 2026-09-09
- InnoSoft Fusion — innosoftfusion.com (home; /fusion) — fetched 2026-09-09
- Dash / DaySmart Recreation — daysmartrecreation.com (home; /solutions/community-rec-center-software/) + help.daysmartrecreation.com (help center home + Initial Setup collection incl. Memberships/Passes/Location Check-in/Residency/Resources articles) — fetched 2026-09-09
- Vermont Systems RecTrac — vermont-systems.helpjuice.com (HelpTrac home; Pass Module Guide + Level 1 Build the pass + Level 3 Scan them in) — fetched 2026-09-09
- Parks & Recreation Administration pass (research/parks-recreation-administration.md, applications/parks-recreation-administration.md) — seam alignment
- Boundary-table lines from processed neighbors: gym-management-system, fitness-membership-management, fitness-class-booking, fitness-studio-management, climbing-gym-management

**Blocked / abandoned (network rule):** esoftplanner.com (403 ×2 — dropped); help.daxko.com and community.perfectmind.com (Salesforce communities render "CSS Error" — JS-required); innosoftfusion.screenstepslive.com (ADFS SSO redirect). Consequence: Daxko/nextRec/Fusion operational detail rests on Tier-2 official product pages; Tier-1 depth comes from RecTrac and Dash.

## Product Observations

### Product A — Daxko Operations (nonprofit community centers)

Positioning: "Nonprofit Community Center Management Software"; "Simplify your nonprofit operations, from memberships to programs to finance"; "Comprehensive member management and operational tools designed for any size community or nonprofit center." Customers: YMCAs, JCCs, Boys & Girls Clubs (logo wall), plus a separate fitness family (Club Automation, Zen Planner…) for commercial gyms — the vendor itself splits community-center software from gym software.

Key observations (evidence layer A unless noted):

- **Membership as the organizing relationship**: "Centralize Membership — a system built to manage your unique memberships, discounts, fees, scheduling, communications"; "Create, adapt, and manage flexible membership offerings and add-ons"; flexible memberships and trials with self-service add-ons; **Request a Hold/Termination** (lifecycle states); payment plans.
- **People across facilities and programs**: "Easily track people across your facilities and programs with a **Capacity Tracker**" — occupancy/usage as a first-class concern.
- **Programs & childcare**: "Manage programs, camps, and events"; profiles and rosters in one place; authorized-pickup notifications; sibling discounts — childcare machinery present (variant layer).
- **Group exercise**: "Communicate and control instructor scheduling with a seamless **GroupEx Pro Integration**" — class scheduling as an integrated capability.
- **Area Rentals**: "Offer and manage **Area Rentals** with ease" — space rental inside the same system.
- **Facility access (capability page)**: "Welcome people into their space around the clock, with secure and convenient access"; "Set custom protocols to govern who enters and when"; "Control interior & exterior spaces including doors, parking garage"; "Leverage facility tracking for insights into usage"; access cards; customer quote: "going 24/7… Daxko's Mobile Pass that connects with Operations… provide a safe and secure environment for our members to access any time of the day" — entry validation tied to the membership record.
- **Nonprofit money layer**: donations at checkout, recurring membership donations, online donation history, grant tracking, tax statements; **automated registered sex-offender screening** ("Serve safely and securely") — safety screening as a nonprofit-posture capability.
- **Periphery**: marketing automation (Engage), branded mobile app, performance analytics, accounting, league management (Playerspace), websites.

### Product B — nextRec / Xplor Recreation, formerly PerfectMind (municipal + community)

Positioning: "Frictionless, All-In-One Parks and Recreation Management Software"; solutions for "Cities, municipalities, **community centers**, YMCAs and JCCs"; own copy: "Thousands of the world's most innovative **recreation centers** and fitness clubs are scaling… by building their businesses on nextRec." Same genus as parks products, deployed at centers.

Key observations:

- **Membership management (feature page)**: "Sell multiple memberships under the same profile… groups, family and multiple membership options"; feature list: multi-program memberships, **membership renewal**, ongoing membership support, **freeze or hold membership**, group membership options, sell memberships online, membership fees, **manage per station access**, **time-limited punch passes**, class membership options — the full entitlement vocabulary.
- **Contacts and accounts**: 360 activity views; **group and family accounts**; duplicate account system; **account credits and overdues**; **subsidy allocation approval** (assistance machinery); online customer access.
- **Calendar and bookings (homepage)**: "Easily create single or recurring **classes, courses, drop-ins, and programs**, with full conflict management. Our online booking software allows your customers to easily discover and register for activities, private and group classes."
- **Facility management (feature page)**: "Manage bookings, schedules, and rentals for indoor and outdoor facilities, parks, fields, campgrounds, meeting spaces, party venues"; feature list: advance booking management, facility contract amendments, **dependent facility management**, **conflict management system**, rental asset management, **facility capacity management**, maintenance management, sell equipment/add-ons, questionnaires and waivers, configurable facility contract templates, **overnight and recurring booking management**; interactive calendar + map with clickable pins, color-coded availability; automated lighting integration with configurable lighting fees.
- **POS**: on-site/online POS plus a **Citywide POS** consolidation feature (municipal posture).
- **Periphery**: marketing automation, mobile app, kiosks ("Empower in-person self-service"), Queue-it virtual waiting room, staff management (timeclock, payroll, availability, volunteers, role-based permissions), document management (certificates, tax receipts, digital signatures).

### Product C — Fusion / InnoSoft (campus recreation)

Positioning: "Pro-Level Rec Management"; "Our software and services empower **recreation departments** of all sizes to get the most out of their facilities"; "Fusion is revolutionizing **campus recreation**"; stats: 320+ schools/colleges/municipalities, 500K daily check-ins, 5M active users. Product page names six pillars — the cleanest capability enumeration in the sample:

- **Robust Registration**: "Create, schedule and manage programs, courses and classes with a tailored registration process."
- **Point of Sale**: sales acceleration, inventory, discounts, "over 60 sales and accounting reports."
- **Access Control**: "Granular access control manages **who gets in, when and where**. **Passback violations**, forgotten ID tracking and **automatic waiver checks** ensure everyone follows the rules."
- **Equipment Rentals**: check-out linked to the member, payment or damage waiver, overdue follow-up.
- **Memberships**: "Unlimited membership options… Supported by **guest or multi-visit passes**… **Fee exempt groups such as students or staff are managed by Fusion's powerful import tool** so records are always up-to-date" — institutional eligibility (not purchased) as a first-class entitlement source.
- **Facility Reservations**: "Facility bookings and rentals, program schedules, and court reservations are **all funneled through Fusion's calendar**. Color code bookings your way, define what appears online, manage staff privileges."
- Family: Fusion Wave (digital signage), FusionGO (mobile), Fusion Play (league management), Fusion Club.
- Testimonials confirm the operational loop: student staff at counters, patron web portal, facility-usage data "to tell our story to upper administration."

### Product D — Dash / DaySmart Recreation (private facilities + community rec centers)

Positioning: "Recreation Facility Management Software"; dedicated solution page "**Community Rec Centers** — Making It Easier To Support Community Wellness… oversee all business operations and **memberships** at your recreation facility center"; verticals span ice, multi-sport, courts, turf, baseball, gymnastics, aquatics, driving ranges, parks & rec, higher-ed rec — one product family across the facility universe.

Solution-page observations: memberships; scheduling and resource management; POS; marketing; sign-ups for events and programs; guest admission tickets for one-off events; **digital check-in stations** ("track program, league, and event attendance… keep up with **liability procedures**"); calendar to "book resources and confirm rentals"; mass scheduling of programs/leagues/events; registrations collecting emergency contacts and waivers; payments for "rentals, concessions, tickets, and memberships"; **recurring payment plans for community memberships**; facility-usage reporting ("over 60 standard reports… track finances and facility usage").

Help-center observations (Tier-1, Intercom KB):

- **Memberships collection**: "Memberships — create, manage, and sell membership products with customizable settings"; "**Required Memberships for Products** — set membership requirements for products, **prompting customers to buy memberships before checkout** if needed" — entitlement gating purchases.
- **Passes collection**: "Passes — create pass types, add redeemable products, sell and redeem passes, manage passes on customer profiles, and **reverse pass usage**."
- **Location Check-in**: "Track customer arrivals, configure check-in alerts, and review detailed check-in activity by customer or location."
- **Kiosks**: "share or tag kiosks for events and customer check-ins"; **Customer Player Cards** (design/print); **Taking Customer Profile Pictures** via webcam — identity at the door.
- **Auto Renew Memberships**: recurring billing incl. GoCardless, member-side cancellation.
- **Waiver Management**: waiver validity periods, renewal prompts at login, email reminders.
- **Calendar/Events**: Event Capacity limits registration; Events with a Roster (add customers, collect payment, check in attendees, drop roster members); make-ups for missed classes/camps; Event Import (CSV bulk).
- **Resources**: Resource Types; **Resource Blocking Rules — "define relationships so booking one resource auto-blocks related ones — avoiding overlaps or double bookings"** (same shared-space conflict semantics the parks pass documented as facility trees).
- **Rental Booking** collection (8 articles).
- **Municipal machinery present too**: **GIS Mapping + Residency Pricing** ("set up resident and non-resident pricing… based on each customer's GIS residency status") and **Fund Accounting** ("create Product Funds… organize revenue by designated financial categories") — proof that residency/fund machinery appears INSIDE a rec-center product; it is deployment machinery, not a parks discriminator.
- Also: customer types (participants/organizations), family members (linked accounts), gift cards, donations, free trials, employee roles/rates, task management, restaurant POS/KDS add-on, LiveBarn/SportNinja/RFAM/Learn-to-Skate integrations.

### Product E — RecTrac (Vermont Systems) — Tier-1 genus anchor

The parks pass's product, sampled here ONLY for the Pass/visit machinery (which the parks pass held as capability-not-core). HelpTrac "The Pass Module, from the front desk in" (published 2026-09-03):

- Framing: "**A pass is the simplest promise your organization makes. Someone pays, and then they get to come in.** Everything in the Pass Membership Module exists to keep that promise: to say **who has paid, what they paid for, how long it lasts, and whether the person at the door today is really them**."
- Module arc: "**Build → Sell → Scan → Report → After.** That is the whole module."
- **Three kinds of pass** (Level 1): **standard membership** ("has a beginning and end date, or a set duration. The annual gym membership, the summer pool pass"), **punch pass** ("deducts one punch per visit from a defined total. Ten yoga classes"), **daily pass** ("a single day of facility entry, for the walk-in who is not a member at all"). Standard+punch built with Add Membership Passcode; daily with a different button.
- Membership record: passcode with prefix convention; status (active/inactive — "the polite way to retire a membership without deleting its history"); **dates OR rolling period** ("runs twelve months from whenever the patron buys it"); punch-pass switch; photo and cross-reference prompts; Continued tab: **Track visit sign out** ("gives you a live count of who is actually in the building"), **Track class attendance** ("checks an incoming scan against your active programs, so a patron is recorded as attending a specific class rather than just entering the building"), **Display photo during visits**.
- Fees: revenue **G/L code** required; resident/non-resident pricing driven off family-member fee codes; quantity fees multiplying by head/visit/punch count.
- Questions: asked at purchase (pass-level) vs household questions ("asked once and kept" — ethnicity, language); waivers with print frequency.
- **Cross references**: "the number behind the barcode on a member card or key fob. Scan it at the door and RecTrac knows who they are without anyone typing a name"; lives on the **family member**; separate toggles for purchase/renewal/transfer.
- **Level 3 — Scan them in**: the **Visit profile** is "the screen that decides whether the door opens." Two lists per location: **Valid Pass List** (standard+punch) and **Daily Pass List**; "**A pass omitted from the list is not broken, it is refused**" — per-location entitlement validity. Process types: attended / unattended / background / access control. Settings: Select First Valid Pass (list order as business decision); **Prompt for Daily Visit with Invalid pass** ("when a member scans with a pass that is expired, suspended, or simply not on this profile Valid list, it offers your daily pass codes instead of a dead end. **That turns a refusal into a sale**"); **Prompt for Renewal On Expired Passes** ("an expired pass at the door offers **Renew Pass**"); Auto Complete (no-fee visits skip payment; fee visits always go through payment); **Use Family Member Swipe In Logic** ("shows the whole household when one person scans, so a parent and three children become four visits from one swipe"); Visit Purpose List; photo display with hold time ("staff can check that the card and the face match").
- **Guest visits**: Max Guest Visits on the pass + Update Guest Count on the Visit profile; "guest visits are not retroactive"; distinct from the walk-in "guest household."
- **Drop-ins**: Activity Drop-Ins live mostly in the Visit profile; location must match the section; Activity Visit Options (enrollments only / drop-ins only / both); Allow Class Drop Ins with Daily Visits; drop-in window in minutes before/after start; requires Track class attendance on the pass.
- Level 5 (After the sale): "Freezing, fixing, refunding, cancelling, and reminding people their pass is about to run out."
- Hardware: background visit processing via scanner (unattended door; Auto Complete forced on).

## Cross-product Comparison

| Structure | Daxko Operations | nextRec (PerfectMind) | Fusion | Dash | RecTrac |
|---|---|---|---|---|---|
| Facility as operated unit (spaces, capacity, calendar) | facilities + Capacity Tracker + Area Rentals + Facility Access | facility management: bookings/rentals, conflict system, dependent facilities, capacity, interactive calendar/map | facility reservations "funneled through Fusion's calendar" | resources + resource blocking rules + rental booking + calendar | Facility module + facility trees (parks pass) |
| Entitlement objects | flexible memberships, holds/terminations, access cards, Mobile Pass | memberships (renewal, freeze/hold, punch passes, per-station access, class memberships) | unlimited memberships, guest/multi-visit passes, fee-exempt imports | memberships (+required-for-products gating, auto-renew), passes (redeemable, reversible) | standard / punch / daily passes, guest visits |
| Entry validation & visit records | access hardware, custom protocols, 24/7, usage insights | kiosks, per-station access | access control: who/when/where, passback violations, waiver checks, ID tracking | location check-in, kiosks, player cards, profile photos, check-in alerts | Visit profile, scan-in, sign-out (live in-building count), household swipe-in, photo match |
| Scheduled activities + registration | programs/camps/events, rosters, GroupEx Pro classes | classes/courses/drop-ins/programs with conflict management | programs/courses/classes registration | program registration, events with rosters + capacity, make-ups | Activity module + drop-ins into classes |
| Space rentals | Area Rentals | facility rentals (contracts, overnight/recurring) | facility bookings/rentals, court reservations | rental booking + resources | Rental module |
| POS / payments | payments, accounting, payment plans | POS + Citywide POS | POS + integrated payments | TSPOS, cash drawer, fund accounting, recurring plans | POS module, G/L-coded revenue |
| Money lifecycle on entitlements | payment plans, hold/terminate | renewal, freeze/hold, credits/overdues | (not surfaced at this tier) | auto-renew, member-side cancel, pass reversal | renew (incl. at the door), freeze, refund, cancel, expiry reminders |
| Residency pricing | — | — | — | **GIS residency pricing ✓** | resident/non-resident fees ✓ |
| Season/session cycle | "seasonal trends" (programs) | not surfaced | not surfaced | program sessions/make-ups | Year/Season machinery (parks pass) |
| Nonprofit/institutional extras | donations, sex-offender screening, childcare | subsidy allocation approval | student/staff imports | donations, fund accounting, liability check-in | scholarships ("scholarshipped" sales) |
| Public self-service | branded mobile app, self-service add-ons | mobile app, online booking | web portal | customer portal, online registration | WebTrac |

Reading of the table:

- The **entitlement + entry-validation machinery** is present and elaborated in ALL five products — including the two (Fusion, Dash) with no municipal posture. It is the most consistently elaborated structure in the sample.
- The **facility-as-operated-unit** (spaces + capacity + one calendar) is present in all five.
- The **activity/registration machinery** is present in all five; the **rental machinery** in all five.
- **Residency pricing** appears in RecTrac AND Dash — a municipal capability that crosses the genus; NOT a Type discriminator at product level.
- **Season cycles** surface strongly only in the municipal genus products (RecTrac; parks pass) — held as deployment machinery here.
- No sampled product is membership-ONLY (that is the gym/fitness-membership territory) or booking-ONLY (amenity/court territory); every product carries the whole bundle.

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant (three jointly-held structures)

1. **The operated recreation facility** — the center (a building or site holding multiple activity spaces — gymnasium, pool, fitness floor, studios, courts, rooms) held as the software's persistent operating unit; its spaces are schedulable and bookable with capacity and conflict control. Remove → a membership CRM or booking tool with no facility of record.
2. **The member's entitlement relationship, validated at entry** — identified people (canonically organized in household/family accounts) hold access entitlements — memberships, punch passes, daily admissions, guest privileges, fee-exempt eligibility — and the center validates those entitlements at entry (scan, desk check-in, kiosk), recording visits (and, in mature products, live occupancy); the entitlement lifecycle (sell/renew, freeze/hold, cancel, expire) is administered in the same records. Remove → program registration and bookings over anonymous registrants — the parks-administration/class-booking shape; the standing relationship is gone.
3. **The programmed schedule of the facility's time** — the center's calendar: scheduled activities (classes, programs, camps, leagues, drop-ins) that participants register or drop into, and rentable spaces that groups book, all conflict-controlled against the same spaces and time. Remove → a pure membership/access operation (door system); the center's program life is gone.

Jointly-held load-bearing:

- 1 alone = venue list / room-directory shell
- 2 without 1+3 = membership billing CRM (fitness-membership / gym territory)
- 3 without 1+2 = generic scheduling/booking calendar
- 1+2 without 3 = an access-controlled building with no program life (door system)
- 1+3 without 2 = the parks-administration shape (programs + bookings, no standing entitlement) — the §24 seam
- 2+3 without 1 = class booking + memberships without a multi-space facility of record (fitness-studio/class-booking territory)

### L1 — Common Mature Structure

- Household/family accounts linking members (RecTrac household swipe-in; nextRec family accounts; Dash family members; Daxko household-centric) — common implementation of "identified people," not the invariant (Fusion imports individual students/staff).
- Public self-service portal / mobile app (registration, bookings, membership self-service) — dominant modern channel; staff system remains system of record.
- POS and integrated payments on the same records (all five).
- Waivers, questions, and documents bound to sales/registrations (RecTrac, nextRec, Dash; Fusion automatic waiver checks at the door).
- Capacity limits on activities and spaces (Dash Event Capacity; nextRec facility capacity; RecTrac head/visit counts).
- Communications and marketing (email/SMS campaigns, reminders) — all five.
- Reporting/analytics: enrollment, revenue, facility usage, check-in activity (all five).
- Staff management: roles/permissions, scheduling, (some) payroll/timeclock (nextRec, Dash).
- Access hardware integrations (scanners, cards, fobs, gates) as the common realization of entry validation (Daxko, RecTrac, Fusion, Dash kiosks).
- Guest privileges (member brings a guest) — RecTrac, Fusion.
- Profile photos at check-in for identity match — RecTrac, Dash.

### L2 — Variant / Optional Structure

- **Operator posture** — nonprofit community (YMCA/JCC/BGC), municipal, university campus, private/commercial. Shapes the money and eligibility machinery but not the core.
- **Municipal machinery** — residency pricing + GIS validation, fund/GL-coded revenue, citywide POS, subsidy/financial-assistance approval, season/session cycles with registration windows. Present in municipal deployments AND in rec-center products serving them (Dash proves residency/funds appear in this Type); NOT definitional.
- **Nonprofit machinery** — donations at checkout, recurring giving, grant tracking, tax statements, safety screening (sex-offender checks).
- **Campus machinery** — fee-exempt eligibility via roster imports, student/staff populations, intramural/club programming.
- **Childcare/camps modules** (authorized pickups, custody-style check-in) — module or sibling product.
- **League management modules** (Fusion Play, Daxko Playerspace, Dash leagues).
- **Vertical facility packs** — aquatics, ice rinks, courts, turf, golf.
- **Equipment rental desks** (Fusion equipment rentals; RecTrac rental module) — distinct from space rentals.
- **Digital signage, kiosks, queue systems, lighting control** — facility-operations periphery.
- **Access-control depth** — from attended desk check-in to unattended 24/7 gate hardware; depth varies, entitlement validation is the invariant.

### L3 — Vendor-specific (research notes only)

- RecTrac: Visit profile mechanics (Valid/Daily Pass Lists per location, Select First Valid Pass ordering, Prompt for Daily Visit with Invalid Pass, Prompt for Renewal On Expired, Auto Complete, Family Member Swipe In Logic, Visit Purpose List); cross-references living on the family member; clone-with-tabs; background processing via Honeywell scanner; guest household vs guest visits distinction; "Build → Sell → Scan → Report → After" module arc.
- Daxko: product-family naming (Operations/Core/Club Automation/Zen Planner/…), GroupEx Pro, Playerspace, Engage, FrontDesk AI, Mobile Pass, Capacity Tracker, sex-offender screening.
- nextRec: Queue-it virtual waiting room, dawn/dusk lighting fees, Citywide POS, dependent facility management, PerfectMind→nextRec/Xplor rebrand.
- Fusion: family naming (Wave/GO/Play/Club), 500K daily check-ins / 5M users / 320+ institutions marketing figures, passback-violation wording, fee-exempt import tool.
- Dash: TSPOS touch-screen POS, PrintNode printing, GoCardless auto-renew, Event Types "Early Access", Resources "Early Access", LiveBarn/SportNinja/RFAM/Learn-to-Skate integrations, restaurant POS/KDS add-on, Customer Player Cards.

## Vendor-specific Findings

See L3. Notable for boundary work: (1) RecTrac's Visit profile proves entry validation is a governed, configurable RULE SURFACE (per-location pass validity, refusal→daily-pass conversion, renewal-at-the-door), not just a card reader; (2) Dash's GIS residency + fund accounting prove municipal machinery lives inside rec-center products — deployment machinery, not Type identity; (3) Fusion's fee-exempt imports prove the entitlement can be institutionally granted rather than purchased — the invariant is the entitlement relationship, not the sale.

## Boundary Findings

1. **vs Parks & Recreation Administration (§24) — the joint review; DISCHARGED from this side: keep-both RATIFIED.** One software genus, two operational postures, two defining cores. The parks core = the department's program catalog (season cycle) + participant enrollment + the community's bookable facility inventory, under a public-agency posture (residency the signature). This Type's core = the operated facility + the membership/entitlement relationship validated at entry + the in-facility activity/rental schedule. Reciprocal remove tests hold: strip the membership/entry leg from a rec-center product → program registration + bookings = the parks shape (the parks pass's own historical check — the paper department office — has NO membership/entry machinery, confirming it is not definitional there); conversely, a campus rec center (Fusion) or a private facility (Dash) satisfies THIS Type with no residency, no season-cycle catalog, no community-wide reservation inventory — proving those are not definitional here. Product-level overlap is acknowledged and documented: RecTrac, ACTIVENet, and nextRec serve both postures; the parks pass itself held "memberships/passes with scan entry" as capability-not-core and "community center deployments" as variant — this pass holds the exact reciprocal. The seam is the operated unit (department's offerings+inventory vs the center's members+facility) and the access relationship (fee-per-enrollment vs standing entitlement validated at entry).
2. **vs Gym Management System (§28, processed)** — RATIFIES that pass's flag ("adjacent (institutional)… this Type is the commercial membership business"): the gym is a single commercial fitness business (membership revenue + classes + retail); the rec center is a multi-activity community/institutional facility whose membership entitles use of many spaces and programs, with rentals and (commonly) public/institutional funding shapes. Shared machinery (memberships, check-in, POS) is genus-level.
3. **vs Fitness Membership Management (§28, processed)** — RATIFIES its flag: the membership record is that Type's center; here membership is one of three jointly-held legs beside the facility and the programmed schedule.
4. **vs Fitness Class Booking (§28, processed)** — RATIFIES its flag: the class-booking loop is that Type's whole product; here it is one loop inside facility operations.
5. **vs Fitness Studio Management (§28, processed)** — RATIFIES its wording ("multi-sport, multi-program operations for clubs and municipalities rather than one commercial class-led business").
6. **vs Climbing Gym Management (§28, processed)** — RATIFIES its wording ("sibling (public sector)… municipal multi-activity centers; broader program mix, different funding and registration model"): the climbing gym adds activity-specific machinery (route setting, grading, safety certifications) this Type lacks.
7. **vs Sports Facility Management (§28, unprocessed) — forward flag**: sports-facility products center bookable sports venues (courts/turf/ice) with rentals, leagues, camps; this Type centers the membership-based multi-activity community facility. Dash spans both (verticals for multisport facilities AND community rec centers on one platform) — that pass should ratify the seam (test: remove the membership/entry leg and the multi-activity community posture → sports-facility territory).
8. **vs Amenity Booking Platform (§17, processed)** — booking a closed resident/tenant population's amenities is that Type's whole product; here booking is one loop beside membership and programming.
9. **vs Membership Management System (§25, processed)** — there the membership is the organizational relationship (associations/clubs) with benefits/renewals as the center; here the entitlement is specifically the right to USE a facility and is validated at its door.
10. **vs Facility Management System (§17, processed)** — building-estate maintenance/work center vs recreation service operations; maintenance appears here only as module/integration (nextRec maintenance management, Dash RFAM integration).
11. **vs Event Registration Platform (§26, processed)** — single-event intake with roster output vs standing year-round operations of a facility and its member base.
12. **vs Camp Management System** — camps appear here as a program type/module (Daxko camps, Dash camps/make-ups); dedicated camp machinery (sessions, bunks, guardianship) is the sibling Type's center.

## Historical / Market-Sample Check

Paper-era recreation center: a membership card file and punch cards at the front desk, a daily admission log, a class schedule board with sign-up sheets, a rental book for rooms and courts, a cash box. This satisfies all three legs — operated facility (the building and its spaces), entitlement validated at entry (cards checked, admissions logged), programmed schedule (classes + rentals) — with no software, no scanners, no portals. The mid-century YMCA (membership cards, class registrations) and the pre-software university rec center (student ID check-in, intramural sign-up sheets, court reservation book) fit the same way. The definition therefore names no cloud deployment, no hardware, no app, no residency, no season cycle. Check passed.

Conversely, the sample's most-marketed modern layers (AI front desk, marketing automation, digital signage, 24/7 unattended access) are correctly outside the core.

## Uncertainties

- Tier-1 operational docs unreachable for Daxko (Salesforce community CSS error), nextRec/PerfectMind KB (same), Fusion KB (ADFS SSO) — those three products are documented at Tier-2 strength; Tier-1 depth rests on RecTrac and Dash. No precise numeric limits, defaults, or state names asserted for the Tier-2 products.
- eSoft Planner — a significant private-facility vendor — unreachable (403 ×2), dropped; the private/commercial pole is carried by Dash.
- Waitlist machinery: not directly evidenced in this sample (parks-genus evidence only); not asserted as part of this Type's standard structure.
- "Open session" scheduling (open gym / lap swim as scheduled drop-in objects): plausible and consistent with drop-in evidence (RecTrac drop-ins, nextRec drop-ins) but not directly documented as a distinct scheduled-object type; held as unverified.
- Membership billing failure/dunning mechanics not researched; recurring billing evidenced (Dash auto-renew, Daxko payment plans) but depth not asserted.
- Whether "recreation center" deployments inside municipal departments constitute a distinct sub-market: product overlap documented (RecTrac/nextRec serve both); the type-level seam is held on defining-core differences, not on product populations.
- Access-control hardware depth (gate brands, credential types) not researched; held as "common realization" only.

## Final Synthesis

Recreation Center Management software is the recreation center's operating system of record. Its world is organized around three jointly-held structures: (1) the operated facility — the center and its activity spaces held as persistent, capacity-bearing, conflict-controlled records; (2) the member's entitlement relationship — identified people (canonically in household accounts) holding memberships, passes, daily admissions, guest privileges, or fee-exempt eligibility, validated at entry and administered through a sell/renew/freeze/cancel lifecycle with visits recorded; (3) the programmed schedule of the facility's time — activities (classes, programs, camps, leagues, drop-ins) participants join and spaces groups rent, all against one calendar. Around this core, mature products add the public portal/app, POS and payments, waivers and questions, capacity and waitlist-style controls, communications, reporting on enrollment/revenue/usage, staff management, and access hardware. Operator posture (nonprofit, municipal, campus, private) selects the variant machinery — donations and screening, residency and fund coding, roster imports, business analytics — but none of it defines the Type. Remove the entitlement/entry leg and the software collapses into program registration and bookings (the parks-administration shape); remove the facility and it collapses into membership billing; remove the programmed schedule and it collapses into a door system. The Type is the facility-operations sibling of Parks & Recreation Administration: one genus, two postures, two cores.
