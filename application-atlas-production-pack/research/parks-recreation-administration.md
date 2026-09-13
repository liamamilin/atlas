# Research Notes — Parks & Recreation Administration

## Research Goal

Understand what software a community's parks & recreation provider — canonically a municipal or county parks & recreation department — actually runs day to day: what objects exist in its system, who operates it, how a season of recreation programming is built and sold, how facilities are reserved, and where the money goes. Produce a vendor-neutral Application Document.

## Initial Boundary

Working hypothesis before research:

- This is the government department's **operations system of record** for recreation services: program/activity administration (classes, camps, leagues, events), participant registration, facility/amenity reservations (pavilions, fields, rooms, pools), memberships/passes, point of sale, and revenue handling.
- Likely confused with: Amenity Booking Platform (reservation-only), Event Registration Platform (one-event intake), After-school Program Management (child-specific), Membership Management System (membership-centered), Facility Management System (estate/maintenance-centered), Government Service Portal (front door), Public Works / Public Asset Management (park land and upkeep), Campground Management (parks-run campgrounds), League Management Platform (league as center).
- Unknowns: is facility reservation definitional or just common? Is membership definitional? Is the public-facing portal definitional or a modern surface? How is residency (resident vs non-resident) treated?

## Research Questions

1. What is the structure of a recreation "program" in these systems? (activity vs offering/section)
2. What does a participant registration look like? What is the participant record (individual, household)?
3. How do facility reservations work? What prevents double-booking? How do public requests get approved?
4. What role do fees, residency rules, and payments play?
5. What is the seasonal cycle of administration?
6. What modules exist beyond the core (passes, POS, leagues, childcare, maintenance, BI)?
7. What do staff use vs what do residents use?
8. Where does this Type end and its neighbors begin?

## Representative Products

| Product | Vendor | Pole | Evidence tier |
|---|---|---|---|
| RecTrac 3.1 | Vermont Systems | long-dominant municipal/enterprise classic (cities, counties, military, universities) | Tier-1 training guides + KB (HelpTrac) |
| ACTIVENet | ACTIVE Network | enterprise recreation & membership management (parks & rec, YMCA, universities) | Tier-2 official product pages |
| RecDesk | RecDesk LLC (Xplor) | small/mid-municipality all-inclusive cloud SaaS | Tier-1 Zendesk knowledge base |
| MyRec.com | MyRec.com | budget-conscious small-department SaaS | Tier-2 official product/features pages |

CivicRec (CivicPlus) was considered as a municipal-suite pole but civicplus.com returned 404 then 403 on two attempts and was dropped per source-abandonment rule; no claims based on it.

## Sources

- Vermont Systems: vermontsystems.com (root, product nav); vermont-systems.helpjuice.com — HelpTrac KB home; The RecTrac Lab; Activity Training Guide (overview + Level 1 · Build the program); FastTrac: Facility Records (with full transcript)
- ACTIVE Network: activenetwork.com (root); activenetwork.com/activenet (product page)
- RecDesk: recdesk.com (root); recdesk.zendesk.com/hc/en-us (KB home); KB categories: Programs (Activities/Sessions) Management; Facility Management
- MyRec.com: myrec.com (root); myrec.com/features/
- Research date: 2026-09-08

## Product A — RecTrac (Vermont Systems)

### Key observations (evidence layer A unless noted)

- **Module structure**: RecTrac is an all-in-one recreation management system; KB "How To" module sections are: Activity, Facility, Pass, POS, Rental, Golf, League, Financial/Billing/Payments, Reports/Receipts/Printing, E-Mail/SMS. Companion products: WebTrac (patron-facing portal), PayTrac (payments), InteliTrac (BI), MainTrac (maintenance), GolfTrac, CampBrain (camps), Campground management, CYMS (child & youth), Contract Management. Markets: municipalities, colleges/universities, camps & campgrounds, military.
- **Activity vs Section (the defining program structure)**: "RecTrac splits every program into two pieces." The **Activity** is the idea of a program ("Swim Class Beginner"): name, category (Type/Subtype/Category), waiver, rules, questions — "no date, no time, no price. It is a folder." The **Section** is the real scheduled class people sign up for: carries "when, where, how-many and how-much" — schedule, facility, capacity, waitlist, price, instructor; Year and Season are required and "drive archiving later." Sections are cloned; custom schedules add make-up dates and holiday skip dates.
- **The operational loop**: "Build → Sell → Run → Report → Maintain. That is the whole module." Enrolling is selling and "it all happens in Global Sales" — a single transaction surface; Global Sales payment/dialog and Purchase History are core processing concepts (most-popular field-level help articles: GlobalSalesDialog, GlobalSalesPayment, GlobalSalesLookup, SAHOUSEHOLDUpdate, ProcessingPrompts).
- **Households**: Chapter 5 of the RecTrac Lab is "Household Management"; households are the families who enroll; household category drives fee criteria (resident/non-resident pricing via criteria).
- **Facility records**: "The facility records are the actual items that you'll be processing within the database… available for reservations and… available for you to link to your activity sections." Built from class + location + unique code. Fees hang at class or facility level (deposit, resident hourly rate, non-resident hourly rate); internal-use reservations carry a fee line that "reduces all fees down to zero." Rules "control the who, what, when, where and how your facilities can be reserved, requested or canceled" — age restrictions, min/max days in advance, dates/times. **Facility trees** link parent/child/sibling spaces (a divisible room; a field usable for soccer or baseball) so shared physical space cannot be double-booked.
- **Activity–facility link**: a section picks a facility — "This reserves the space." Activities "lean on" facilities, fees & G/L codes, waivers, rules, questions, instructors & households.
- **Rules and eligibility**: activity/section rules decide "who is allowed in: ages, prerequisites, residency, gender, membership" (rules can live at activity or section level).
- **Questions at sign-up**: Question Management links questions to activities so they prompt during the transaction (t-shirt size, emergency contact).
- **Pass module** (entry/membership): guide levels: build the pass → sell it at the counter → scan them in → read the numbers → after the sale. Entry validation via scanning.
- **Seasonal cycle**: Year/Season on sections drive archiving; bulk changes and cloning carry programs "from one season into the next."
- **Patron portal**: WebTrac — "Your patrons see the parts you choose to expose out on WebTrac." Optional exposure, staff system is primary.
- Financial/billing/payments include installment billing and receipt drawers (cash receipting) — evidence from KB section names and how-to articles.

## Product B — ACTIVENet (ACTIVE Network)

### Key observations (Tier-2 product pages)

- Positioning: "Recreation management software for YMCAs and parks & rec"; "the world's most powerful facility, registration and membership management software"; "Streamline programs, processes and participation in a single system with a modern, customizable online registration experience."
- Pillars on the product page: **Membership Management** (members "from their first guest visit through years of participation," recurring payments, online access, auto-generated notifications; quote: "simple to track memberships and associate them to each person"); **Facility Management** ("3-step facility reservation and easy modifications… Simplify scheduling, manage equipment lending, eliminate double-bookings and assign locker rentals" — reservation checkout image covers room, lockers, equipment); **Child Care Management** (online and in-person registration, calendars, flexible payment plans, auto pay, check-in/check-out via the Connect app); **Point of Sale** ("registering for a class, booking a room, renting pool toys or buying an energy bar… payments anywhere within your facilities"); **Data & Insights** (reporting for departmental decisions); **AI + Automation**.
- Audience icons: Government, Parks, Sports Facilities, Universities, YMCA. Case customers include Seattle Parks & Recreation, City of Fort Worth, City of Manhattan Beach, Phoenix, Denver Parks and Recreation.
- Payment Manager marketed separately as "One, easy to navigate online payment portal for all your city or county's needs" — cross-department payment layer.
- Drop-in activities are a named capability (2026 product news).

## Product C — RecDesk

### Key observations (Tier-1 Zendesk KB structure + article titles)

- KB categories: Getting Started; **Member Management** ("manage members/households"); **Programs (Activities/Sessions) Management**; **Facility Management** ("create facilities/make reservations"); FlexForms; **Membership Management**; **Point of Sale Management** ("sell miscellaneous items at concession stands/remote locations or in-house"); **Finance and Money Management** ("invoices, payments, payment plans, and refunds"); **League Management**; CRM+; Reports; General/Tech; RecDesk Payments; Accessibility; Engage App.
- **Programs (Activities/Sessions)**: sections named Programs, Program Registrations, Wait Lists, Working with Rosters, Drop In Programs. Articles: create/edit/copy/bulk-copy programs, private programs; register a person for a program (staff-side) and FlexReg programs; shopping cart hold; add/approve/remove waitlisted people; roster list and roster actions; update or cancel a program registration; cancel a program; custom-question responses on a registration; drop-in programs.
- **Facility Management**: sections named Facilities, Reserving a Facility in FlexScheduler, FlexCalendar, Check-Ins/Check-Outs, Online Reservations & Requests, Best Practices. Articles: create/edit facility; facility tags; advanced facility search; photos/videos on facilities; **facility permit**; fee schedule for FlexScheduler; create/view/edit facility reservations; reservation search; **online reservation requests with approve/deny and processed-request views**; attended and self check-in/check-out; "future rolling online availability schedules."
- Positioning: cloud recreation software for parks & recreation departments, aquatic centers, education, HOA, community centers; "all modules included" subscription; RecDesk now under Xplor vertical recreation branding.
- Other site features: GIS/Residency Management, Local Access Control, Lighting Control, Digital Signage, Instructor Access, Instructor Compensation, Billing & Invoicing, Custom Financial Extract (financial-system integration), Online Registration, Reservation Approval, League Management.

## Product D — MyRec.com

### Key observations (Tier-2 features pages)

- "Assists municipal, government, and private organizations… cloud-based solution"; 550+ departments; supports "registration, facilities, finances, and more"; independently owned, staffed by "park and recreation professionals."
- **Real-time availability** group: remaining items (ticketed event, sports uniform, art supplies), roster updates (additions, cancellations, assignments update for management, coaches, instructors), facility schedules ("no conflicts… updates the calendar and availability immediately to your public"), **seat checks** ("applied registration requirements like number of seats remaining, age, grade and residency").
- **Program management**: simple activity setup (create or clone), **team management** (team registration, auto draft, game scheduling, coach assignment, scores/standings reporting), registration options (daily/weekly/monthly pricing options in one activity), reporting (seat caps, demographics, schedules, rosters, sign-ins).
- **Member connection**: targeted email blasts (by account, activity, reservations, balances due), text blasts, social sharing, account messaging.
- **Paperwork**: custom form builder, document uploads (held on the member's account), disclaimer tracking (global & custom; missing-signature resolution), digital attendance (staff, coaches, instructors).
- **Facilities**: **self-service booking** (public-side reservations with or without security deposits), rental requests (public submits; management reviews), **real-time conflict checking** ("your public can't overbook"), approval process (multi-approver before booking).
- Payments: integrated processing, EMV terminals for in-person transactions.

## Cross-product Comparison

| Structure / capability | RecTrac | ACTIVENet | RecDesk | MyRec | Layer |
|---|---|---|---|---|---|
| Program catalog of scheduled offerings (activity → sections/sessions) | A (Activity/Section, explicit) | A (registration programs) | A (Programs/Activities/Sessions) | A (activity setup/clone) | A+B core |
| Enrollment/registration with roster & capacity | A (Global Sales, rosters) | A | A (registrations, rosters) | A (seat checks, rosters) | A+B core |
| Household/account participant model | A (Household Management) | A (membership/person records) | A (members/households) | A (accounts) | A+B common |
| Fees & payment collection on registrations/reservations | A (fees, GL, installment billing, drawers) | A (recurring payments, Payment Manager) | A (finance: invoices, payment plans, refunds) | A (payment processing, EMV) | A+B core-half |
| Facility/amenity reservation inventory with calendars & conflict control | A (facility records, trees) | A (3-step reservation, eliminate double-bookings) | A (FlexScheduler, FlexCalendar) | A (real-time conflict checking) | A+B core |
| Public-facing online registration/booking portal | A (WebTrac, optional exposure) | A (modern online registration) | A (online reservations & registration) | A (self-service booking) | A+B common |
| Reservation request → approval flow | A (rules on request/cancel; email notifications) | not directly observed | A (approve/deny requests) | A (approval process) | B common |
| Seasons/sessions cycle & archiving | A (Year/Season drive archiving) | not directly observed | B (session-shaped programs) | B (registration options) | B common |
| Residency handling (rates/rules/validation) | A (residency fee criteria & rules) | not directly observed | A (GIS/Residency Management) | A (residency seat checks) | B common (public-agency signature) |
| Waivers/forms/questions at sign-up | A (waivers, questions) | not directly observed | A (FlexForms) | A (forms, disclaimers, uploads) | B common |
| Membership/pass module with entry scan | A (Pass module: sell → scan in) | A (membership pillar) | A (Membership Mgmt) | A (membership pages) | B common |
| Point of sale | A | A | A | A (remaining items, ticketed) | B common |
| League/team management module | A (League module) | not directly observed | A (League Management) | A (team management, standings) | B common/optional |
| Attendance / check-in on offerings | A (run the class) | A (childcare check-in/out via app) | A (check-ins/outs, roster) | A (digital attendance) | B common |
| Waitlists | A (section waitlist counts) | not directly observed | A (Wait Lists section) | B (seat caps) | B common |
| Childcare-specific machinery | separate product (CYMS) | A (Child Care Management pillar) | not observed | not observed | B optional/variant |
| Maintenance/work orders on park assets | separate product (MainTrac) | not observed | not observed | not observed | B optional/variant |
| Communications (email/SMS blasts) | A (E-Mail/SMS module) | A | A (marketing tools) | A (email/text blasts) | B common |
| Reporting/BI | A (reports + InteliTrac) | A (Data & Insights) | A (Reports) | A (reporting) | B common |

## Canonical Model (abstraction levels)

### L0 — Defining Invariant (deliberately small)

The community recreation provider's administration system of record. Three jointly-held structures, plus an operator posture:

1. **The program offering structure of record** — the operator's recreation offerings held as a persistent catalog of scheduled, enrollable offerings (classes, camps, leagues, clinics, events, drop-ins), organized in a season/session cycle; each offering carries schedule, capacity, eligibility rules, and fee configuration. (The offering, not a transaction and not a facility, is the organizing record of the Type.)
2. **Participant enrollment against offerings** — identified participants (canonically held in household/family accounts) are enrolled into offerings, ordinarily for fees that the system assesses and collects, with the enrollment roster as the working surface. Participation, payment, and the offering bind in one record.
3. **The facility/amenity reservation inventory** — the places the community plays (parks facilities, fields, courts, pavilions, rooms, pools) held as persistent bookable records with availability calendars, conflict prevention across shared space, and fee rules; reservations bind booker × facility × time and are commonly request-then-approved.

Operator posture: the operator is a community recreation provider — canonically the parks & recreation department of a municipality, county, or special district exercising public stewardship of recreation. This frames residency-based fees/rules and public-facing service.

Jointly-held is load-bearing:

- 1+2 without 3 = an activity/class registration platform (community-education / youth-activity software)
- 1+3 without 2 = a brochure + booking calendar with nothing administered
- 2+3 without 1 = amenity booking with attendee lists (Amenity Booking Platform / venue scheduling territory)
- 3 alone = amenity/facility booking tool
- 2 alone = event registration intake
- 1 alone = a program brochure/website

### L1 — Common Mature Structure (very common, not defining)

- Household/family account as the participant registry's organizing unit
- Season/session cycle with seasonal roll-over, cloning of prior seasons, archiving
- Capacity, waitlists, eligibility rules (age, residency, membership, prerequisites) enforced at enrollment
- Public-facing self-service portal (register, reserve, pay, view schedule) — modern dominant surface, optional in the classic back-office framing
- Reservation request → staff approval flow with deny reasons
- Pass/membership selling with scan-based entry validation at facilities
- Point of sale (concessions, retail, tickets) on the same revenue spine
- League/team management (drafts, schedules, standings) as a module
- Attendance/check-in on offerings
- Custom forms, waivers, document uploads, sign-up questions
- Resident/non-resident rate and rule distinctions (GIS/address validation as implementation)
- Email/SMS communications tied to accounts, offerings, reservations
- Reporting/analytics; GL-coded revenue and financial extract toward the government finance system
- Receipts, refunds, payment plans, installment billing

### L2 — Variant / Optional Structure

- Childcare/day-camp machinery (payment plans, custody-style check-in/out) — packaged as module (ACTIVENet pillar) or separate product (CYMS)
- Park asset maintenance & work orders (MainTrac; CMMS territory when central)
- Campground/camping operations inside a parks system
- Golf operations (GolfTrac), ticketing partnerships, rental equipment/lenders/lockers
- Cross-department payment portals (Payment Manager)
- Access control, lighting control, digital signage integrations
- GIS/residency engines, instructor compensation schemes, CRM additions, donation/scholarship handling (varies by product)
- Private-operator deployments (YMCA, HOA, community centers, universities, military installations) — same software genus, non-government operator

### L3 — Vendor-specific (research notes only)

- RecTrac Activity/Section/Global Sales terminology; ZZDefault Activity default-record pattern; fee "linking levels" (class-level fees inherited by facilities); facility trees with parent/child/sibling overlap semantics; Year/Season-driven archiving; "Enroll By Day"/drop-ins as optional section add-ons; PayTrac/InteliTrac/MainTrac/CYMS product names; Pass module 5-level guide structure
- RecDesk FlexScheduler/FlexCalendar/FlexForms/CRM+ brand names; "future rolling online availability schedules"; facility permits as first-class objects; shopping-cart hold
- ACTIVENet "3-step facility reservation"; Connect/Captivate apps; Easy Screen; Payment Manager cross-department portal; "40% of North American cities" marketing figure
- MyRec fee calculator (annual price from department revenue); all-inclusive pricing posture; disclaimer-tracking missing-signature resolution; Constant Contact partnership

## Vendor-specific Findings

See L3. Notable for boundary work: RecTrac's facility trees (shared-space conflict semantics) show the reservation inventory is genuinely space-management, not just calendar booking; RecDesk's "facility permit" shows reservation→document generation exists but sits adjacent to Permit Management.

## Boundary Findings

- **vs Amenity Booking Platform (§17)**: that Type's core is operator-defined bookable amenities for a closed resident/tenant population (building/association context), booking as the whole product. Here booking is one of three legs; the booker population is the open public; and the programming/registration legs dominate the working day. Remove program+registration legs → amenity booking.
- **vs Event Registration Platform (§26)**: single-event intake with roster as output vs standing administration of an entire offering catalog across seasons with persistent participant relationships.
- **vs After-school Program Management / Childcare (§29)**: child+guardian care context with custody/ratios vs all-ages community recreation; the rec department's childcare usage is a variant packaging. Registration+roster spine shared; facility-reservation leg absent there.
- **vs Membership Management System (§25)**: membership record as the center vs enrollment/reservation center; memberships here are a common capability layer (passes/pool passes), not the organizing record.
- **vs Facility Management System (§17)**: estate + work/maintenance center vs recreation service center; maintenance exists here only as optional module (MainTrac), and the "estate" is the bookable/venue inventory.
- **vs Government Service Portal (§24)**: jurisdiction front door for all services vs one department's operations system of record; the rec portal is departmental self-service.
- **vs 311 / Citizen Service Request (§24)**: request→response loop vs administration of offerings, reservations, and memberships.
- **vs Public Works Management / Public Asset Management (§24)**: park land, grounds, and asset upkeep are different Types; parks & rec administration treats the park as venue, not as maintained asset (except optional maintenance modules).
- **vs Permit Management (§24)**: reservations may generate facility permits (documents confirming use), but permits authorizing proposed work/uses are a different record; standalone rec systems don't run permit programs.
- **vs League Management Platform (§26)**: league-as-competition-container (fixtures/standings center) vs program offering among many; league machinery appears as a module here.
- **vs Campground / RV Park Management (§17/§26)**: camping inventory/lifecycle machinery is its own Type; parks departments that run campgrounds either integrate a vertical product or use the campground module — variant.
- **vs Government Inspection Management (§24)**: that pass already lists parks as one agency family among inspection programs; inspections of facilities are adjacent, not this Type's center.
- **"Parks" in the name**: the Type's defining content is recreation *service administration*; park land itself (ecology, trails, asset condition) is not part of the core. A community-center-only deployment satisfies the core; the park appears as the venue inventory of leg 3.

## Historical / Market-Sample Check (§24 reasoning)

Paper-era parks & recreation department office: seasonal program brochure (the catalog), household registration cards with fee receipts and a receipt ledger, eligibility and resident/non-resident rate sheets, a facility reservation book at the front desk with deposit slips and a facility-use permit pad, season-to-season rollover of the same programs. This satisfies all three legs with no cloud, no online portal, no POS, no GIS, no AI. The definition therefore names no deployment surface, no online self-service requirement, and no payment rails. Check passed.

Conversely the modern sample's most-marketed surfaces (AI, cross-department payment portals, mobile apps) are correctly outside the core.

## Uncertainties

- ACTIVENet evidence is Tier-2 product pages only; its operational model (activity/section naming, season archiving, approval states) is inferred, not directly documented. All ACTIVENet-specific claims kept at positioning/pillar strength.
- CivicRec dropped (404/403 ×2) — the "municipal website-suite bundle" pole is unsampled; no claims about that packaging.
- RecDesk Member Management category timed out; household/member observations rest on category titles + site copy.
- Season archiving observed explicitly in RecTrac only; seasonality as a cycle is cross-product but archiving as a mechanism is single-product.
- Scholarship/fee-assistance handling common in the domain but not directly observed in the sample; not asserted.
- Numeric limits (transaction volumes, section sizes, fee caps) not researched; none asserted.

## Final Synthesis

Parks & Recreation Administration software is the community recreation provider's system of record. Its world is organized around three jointly-held structures: (1) a catalog of scheduled program offerings across a season cycle, (2) participant enrollment from household accounts against those offerings, ordinarily fee-bearing, and (3) a bookable facility/amenity inventory with calendars, conflict control, and fee rules — all operated by a public community recreation agency whose residency logic and public self-service surfaces shape the system. Around this core, mature products add the seasonal cycle machinery, waitlists, waivers/forms, memberships/passes with entry scanning, POS, league modules, communications, reporting with GL-coded revenue, and optional verticals (childcare, camping, golf, maintenance). Remove any one leg and the software becomes a neighboring Type: registration platform, amenity booking, or event intake.
