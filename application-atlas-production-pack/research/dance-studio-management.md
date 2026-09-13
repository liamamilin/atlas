# Research Notes — Dance Studio Management

## Research Goal

Understand what "Dance Studio Management" software is as an Application Type: what the system's world is made of, who operates it, how the recurring class business actually runs through it, and where its boundary lies against adjacent Types (fitness studio management, after-school program management, sports registration, membership/billing platforms) and against its obvious siblings in the directory (gymnastics club, swim school, martial arts school management).

## Initial Boundary

Working hypothesis at start:

- Operator-side software for a dance studio / dance school business: the owner, front-desk staff, and instructors are the primary users; parents/guardians and dancers use a portal.
- Core loop: publish a schedule of recurring dance classes → families enroll children → tuition is billed and collected → attendance is taken → the studio organizes dance-specific events (recitals, costumes, competition teams).
- Nearest neighbors: Fitness Studio Management, After-school Program Management, Childcare Management, Sports Registration Platform, Membership Management.
- Likely confusion: this leaf may be "just a vertical variant" of a generic class-management product family — vendors literally sell the same product with vertical skins (Jackrabbit Dance / Class / Swim / Cheer / Music; The Studio Director industries; Studio Pro dance/cheer/gymnastics/theatre; iClassPro gymnastics/cheer/swim/dance).

## Research Questions

1. What is the unit of scheduling — class, session, season, term? How do classes recur?
2. What is the customer record — student, guardian, family account? How do multi-child families work?
3. How does enrollment work (online registration, trials, policies/waivers, eligibility by skill/level)?
4. How is tuition charged (recurring monthly, per session, prorating, registration fees, non-tuition charges)?
5. What machinery is dance-specific: costume management, recital/show management, competition teams?
6. How do attendance, absences, and makeups work?
7. What portals exist (parent, staff/instructor) and what can each side do?
8. What adjacent revenue machinery exists (private lessons, parties, camps, retail/POS, tickets)?
9. Where is the boundary vs fitness studio management and after-school program management?
10. Does the definition survive historical/regional checks (paper-era studios, non-US markets)?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer tiers:

| Product | Positioning | Why sampled |
|---|---|---|
| Jackrabbit Dance | Vertical edition of a multi-vertical class-management vendor (Jackrabbit Class/Swim/Cheer/Music/Dance); since 2004; 7,000+ businesses; enterprise tier | The "same core, vertical skin" pole; strong feature documentation |
| The Studio Director | Dance-first studio management software now sold into dance, cheer, gymnastics, fitness, martial arts, music, pilates, yoga, youth sports | The multi-industry generalist pole; dance as first-listed industry |
| Studio Pro (formerly DanceStudio-Pro) | Dance-first software, 7,000+ dance studios, now also cheer/gymnastics/theatre/martial arts; flat plan tiers | The dance-specialist pole; deepest recital/costume machinery; help center directly accessible |
| iClassPro | Cross-vertical class management (gymnastics, cheer, swim, dance, music/art) since 2008; 100M+ registrations | The "class management platform where dance is one industry" pole; contrast for dance-specific machinery |

## Sources

All fetched 2026-09-07. Evidence layer per observation noted as A (directly observed on the cited page) or B (cross-product commonality from multiple directly observed pages).

- Jackrabbit Dance — home page; Studio Management (class management) feature page; Costume & Recital Management feature page — jackrabbitdance.com
- The Studio Director — home page — thestudiodirector.com
- Studio Pro — home page; Tuition & Payments feature page — gostudiopro.com; Help Center home; Seasons/Classes category — dancestudiopro.zendesk.com
- iClassPro — home page; Dance Studio Software Features page — iclasspro.com

Sourcing limitation: for Jackrabbit Dance, The Studio Director, and iClassPro, only product/feature pages were fetched (help-center article bodies not retrieved; Studio Pro help center was reachable and used for structure confirmation and selected article titles). Therefore precise operational parameters (billing cycle defaults, exact state names, numeric limits, plan-specific feature gating) are NOT asserted anywhere. All claims in the final document are calibrated to this evidence strength.

## Product Observations

### Jackrabbit Dance (A = directly observed on jackrabbitdance.com pages)

- Self-positioning: "Dance Studio Management Software"; "premier class and payment management software" — the vendor itself pairs class management + payment as the two pillars.
- Feature modules: Studio Management (class management), Billing & Payment Processing (Jackrabbit Pay / ePayments), Costume & Recital Management, Online Registration, Parent & Family Experience, Reporting, Appointments, mobile app ("Jackrabbit Plus"), Enterprise (multi-location), Partner Marketplace (integrations), Zapier automation.
- Studio Management page: Activity Calendar for classes, events, appointments — "avoid double booking rooms and instructors"; customized policies "specific to classes, sessions, levels or programs" with parents "only presented with the policies that apply to their student's enrollment"; electronic attendance via Staff Portal on any device; makeups scheduled by families from the Parent Portal "based on parameters you've set"; private lessons managed by room and teacher availability.
- Costume & Recital page: printable costume measurement worksheets; auto-sizing "based on girth measurements from your vendor's sizing chart"; costume fees (deposits and payments) collected through the platform; recital lineup assistant ensuring "dancers have enough time to change between routines"; recital program book export to Microsoft Word.
- Policies tailorable "by class or recreational and competitive levels" — the recreational vs competitive split is explicit.
- Sells separate vertical editions (Class/gymnastics, Swim, Cheer, Music, Dance) — same core per vertical; also an Australian-market page.

### The Studio Director (A)

- Self-positioning: "Studio Management Software for Dance, Gymnastics, & More"; dance is the first industry listed.
- Feature cards: Communication (text/email, group emails, drip-marketing "for birthdays, prospects and new students", templates, open tracking); Virtual Classrooms (class location with online class link, launched from the customer portal); Events & Recitals ("organize your performances, ticket sales, charge for your recitals", "automatically order performances to avoid any back-to-back conflicts"); Accept Payments (card/bank info on file, PCI-compliant); Online Enrollment (parent portal: account access, schedule view, register for classes, "request a trial or makeup class", online documentation, "purchase inventory", pay); Reporting (dashboard/detail/summary; accounting records, student information, class schedules, attendance); Costume Management (costume order forms, "pre-loaded with size charts for most major vendors", automatic costume sizing for children and adults from measurements).
- Billing: "Automatic prorating, tuition calculations, online payments, recurring credit card and electronic check payments, costume and event management."
- Web-based; "stores all your information on a secure internet server"; mobile-ready access.

### Studio Pro / DanceStudio-Pro (A)

- Self-positioning: "The dance software partner…"; "trusted dance software for over 7,000 dance studios"; solutions for dance, cheer, gymnastics, theatre, martial arts; Australian market page.
- Feature pillars: Lead Management (prospective dance families, trials→enrollment); Registration, Classes & Scheduling ("set up your fall, winter, and summer dance sessions", "automate liability waivers", "enroll in skill-appropriate classes based on your curriculum"); Tuition & Payments (Auto-Pay on demand, monthly tuition, "separate invoices for competition fees, guest master classes, costume deposits"); Communication (announcements, competition team rehearsal schedules, recital reminders); Recitals & Ticketing (Recital Wizard: build recital lineup, "recital playbook with visual stage flows and Quick Change Warnings", assign stage and act managers, stage-grid system; Costume Console: assign/track costumes per class or act, student measurements by class, "Robo-Sizer™ to get recommended sizes for popular costume vendors", costume sales, payments, order tracking, labels, distribution).
- Tuition & Payments page: credit cards, direct deposit, eCheck, ACH, in-person terminal; Auto-Pay on demand for balances or tuition; reattempt failed transactions; punch cards / prepaid passes; POS with barcode scanning and real-time stock, orders tied to each student; online ticket sales through the custom-branded portal (real-time card payments, purchase limits, print-at-home, scan at venue, ad space on tickets); Stripe-powered processing.
- Pricing structure: flat monthly plans (Essentials/Premier/Elite), unlimited students and classes on every plan.
- Help center (Tier 1) category structure confirms the object model: Tuition/Auto-Pay; Parents/Students; Seasons/Classes; Teachers/Staff; Online Registration/Parent Portal; Tickets/Events; Costumes; Online Store/Point of Sale; Merchant Services; plan-tier categories (Elite, Premier).
- Help center articles (A, titles/summaries): add a season; copy a season; Registration Mode setting on the season; separate rates for certain classes; view old-season classes; import/add/copy classes; "Class Suggestions vs Class Eligibility"; "One-off Classes and Camps"; holding online classes (external meeting tools).

### iClassPro (A)

- Self-positioning: "Class Management Software For Gymnastics, Cheer, Swim, and Dance" — "Manage Classes, Camps, Private Lessons, Birthday Parties, Events, Student Attendance, Staff, Waivers, Email, SMS and more"; dance is one industry page.
- Dance page: Office Portal (manage ballet/tap/hip-hop/jazz classes, enrollment, billing, customer accounts; dashboards, live calendar, reporting); Staff Portal (instructors view planned student absences, record attendance, track skill progress; clock-in/out with geographic coordinates); Customer Portal (enroll in classes, account management, payments, 24/7 "ProShop" access, studio news); Integrated Websites; Branded App (dedicated app-store listing on premium plans).
- Automation: "Autopilot Billing" ("simplifies tuition billing from setup to payment"); Autopilot Workflows (marketing/communication); QuickBooks on Autopilot (accounting sync).
- Class-side features: Skill Tracking (evaluate dancer skills in real time in the staff portal; custom certificates with automatic delivery); Makeup Lessons ("makeup tokens", automated or manual allocation, parents schedule makeups); Punch Passes (family or individual, attend "on occasion"); Enrollment Wizard ("easy sign-up and auto-charge scheduling"); Check-In Kiosk (iPad self-check-in for attendance).
- Adjacent offerings: Appointments & Private Lessons (instructor availability, reminders); Party Booking Management (birthday parties, packages/add-ons); Events & Camps ("summer ballet intensives, hip hop workshops, lyrical masterclasses, drill team camps").
- Pro Insights: enrollment, retention, financial dashboards; Welcome Page metrics (new accounts, dropped enrollments, class transfers, new enrollments).
- Multi-location: FAQ states customers operate as multi-location organizations; plan ladder Signature/Elite/Premium/Enterprise.
- Not observed on the dance page: costume management, recital lineup/show-order machinery (its "events" machinery is generic camps/events, not recital production).

## Cross-product Comparison

| Structure | Jackrabbit Dance | The Studio Director | Studio Pro | iClassPro | Evidence |
|---|---|---|---|---|---|
| Family/guardian account holding students | Parent & Family Experience | customer accounts / parent portal | Parents/Students (HC category) | Customer Portal, customer accounts | B: all 4 |
| Scheduled recurring class as central object | Studio Management / Activity Calendar | flexible class scheduling | Seasons/Classes | Class Management | B: all 4 |
| Period container (season/session/term) | sessions (policies per session) | not directly labeled on fetched page | Seasons (HC: add/copy season, Registration Mode) | not directly observed | A in 2 products; abstraction at C |
| Enrollment (student ↔ class, persisted) | Online Registration | Online Enrollment | registration feature; Class Eligibility | Enrollment Wizard | B: all 4 |
| Tuition billing + payments on the family account | Jackrabbit Pay / billing | streamlined billing; recurring card/eCheck | Tuition/Auto-Pay | Autopilot Billing; auto-charge scheduling | B: all 4 |
| Attendance recording | Staff Portal attendance | attendance reports | (attendance via staff surfaces; not fetched in detail) | Staff Portal + kiosk | B: 3–4 |
| Absences & makeups | Parent Portal self-scheduling | request a makeup class (portal) | makeup requests (portal) | makeup tokens | B: all 4 |
| Parent/customer portal | Parent Portal | customer portal | Parent Portal | Customer Portal | B: all 4 |
| Staff/instructor portal | Staff Portal | (not directly observed) | Teachers/Staff (HC) | Staff Portal | B: 3–4 |
| Trials | (not directly observed) | request a trial | trials→enrollment focus | (not directly observed) | A in 2 products |
| Policies & waivers scoped by class/session/level | policies per class/session/level/program; recreational vs competitive | (not directly observed; waivers not on fetched page) | automate liability waivers; agreement text | waivers in feature list | B: 3–4 |
| Skill/level tracking | (not directly observed) | (not directly observed) | Class Suggestions/Eligibility; curriculum | Skill Tracking + certificates | A in 2 products |
| Costume machinery (measurements → vendor size charts → sizing → orders/fees) | measurement worksheets; auto-size by girth from vendor chart; costume fee deposits | pre-loaded vendor size charts; auto-size; order forms | Costume Console; Robo-Sizer (vendor sizes); deposits; distribution | not observed | B: 3 of 4 (dance-first products) |
| Recital/show machinery (lineup, change-time logic, tickets) | recital lineup assistant (change-time); program book export | events & recitals; ticket sales; performance ordering | Recital Wizard; Quick Change Warnings; stage grid; ticket platform; venue scanning | not observed | B: 3 of 4 |
| Competition teams | recreational vs competitive levels | (not directly observed) | competition fees invoices; team rehearsal schedules | (not directly observed) | A in 2 products |
| Private lessons | private lessons mgmt (room/teacher) | (not directly observed) | (not directly observed on fetched pages) | Appointments/private lessons | A in 2–3 products |
| Camps/one-off events | events in calendar | (not directly observed) | one-off classes and camps | Events & Camps | A in 2–3 products |
| Birthday parties | (not directly observed) | (not directly observed) | (not directly observed) | Party Booking Management | A in 1 product — optional |
| Retail / POS / dancewear | (not directly observed) | purchase inventory (portal) | Online Store/POS (HC); barcode stock | ProShop; POS | B: 3–4 |
| Punch cards/passes | (not directly observed) | (not directly observed) | punch cards/prepaid passes | Punch Passes | A in 2 products |
| Communication (email/SMS, announcements, automation) | customer engagement; Zapier | email/SMS; drip marketing | Communication; Robo-Mailer (HC) | email/SMS; Autopilot Workflows | B: all 4 |
| Reporting/dashboards | Reporting | Reporting | (HC: reporting surfaces not fetched) | Pro Insights; Welcome Page | B: 3–4 |
| Accounting integration | Partner Marketplace | (not directly observed) | (not directly observed) | QuickBooks on Autopilot | A in 2 products |
| Multi-location | Enterprise | (not directly observed) | (testimonial: 13 locations) | FAQ: multi-location supported | A in 2–3 products — common at larger tiers |
| Online/virtual classes | (not directly observed) | virtual classrooms | online classes (HC) | (not directly observed) | A in 2 products |

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the product stops being recognizable as dance studio management:

1. **Family account holding students** — the customer record is a guardian/family account containing one or more students (dancers); the family is the paying unit. Remove it and the system cannot represent who is being taught and who pays.
2. **Scheduled class offerings** — recurring, calendar-placed classes (day/time pattern, instructor, room/studio, over a defined period). Remove it and the system is generic billing/CRM.
3. **Enrollment** — a persisted registration of a specific student into a specific class offering; the roster-forming record that drives rosters, capacity, attendance, and charges. Remove it and the system is a scheduling or marketing tool.
4. **The tuition money loop** — enrollment-driven tuition charges posted to the family account and payments collected (with stored payment methods / autopay in modern products; manual collection historically). Remove it and the system is a class-registration website rather than the studio's business system.

Historical check (§24 method): a paper-era or regional studio — family ledger card with children, a posted weekly schedule, registration forms, monthly tuition checks, a roll book — satisfies all four invariants without any software machinery. The definition does not depend on the modern implementation. The historical check passes.

Deliberately NOT in L0 (common today but not defining): parent portal, autopay, attendance, costumes, recitals, skill tracking — all pass the "older product without it is still this Type" test.

### L1 — Common Mature Structure

Present in essentially all sampled products; expected of a mature modern product:

- online self-service registration (families enroll via a portal)
- parent/customer portal (account, class schedule, payments, communication, makeups)
- staff/instructor portal (rosters, attendance; skill tracking in some products)
- attendance recording, with absences and makeup scheduling (family-facing)
- payment processing with stored payment methods and autopay; failed-payment reattempts
- enrollment-related policies and liability waivers scoped by class/session/level (recreational vs competitive)
- trials and class-capacity management
- communication: email/SMS announcements, notifications, automated reminders; marketing automation in several products
- reporting/dashboards: enrollment, retention, revenue
- skill/level or curriculum tracking, with eligibility/suggestions for class placement
- private lessons booked against instructor/room availability
- season/session tooling: create/copy periods, separate rates, registration modes
- calendars that guard against room/instructor double-booking

### L2 — Variant / Optional Structure

Depends on business model, scale, region, performance culture:

- **Costume management** — measurements per student, sizing against costume-vendor size charts (auto-sizing), orders, deposits/fees, distribution tracking. Present in the three dance-first products; not observed in the cross-vertical product.
- **Recital/show management** — lineup/show order with quick-change-time logic, stage/act managers, stage-grid/floor mapping, program-book output, ticket sales (branded portal, limits, venue scanning). Same 3-of-4 pattern.
- **Competition team management** — competitive-level class structures, team rehearsal scheduling, competition-fee invoicing.
- events/camps (ballet intensives, workshops, one-off classes), birthday-party booking (one product)
- retail/POS for dancewear (leotards, tights, shoes), inventory
- punch cards/prepaid passes; drop-in flexibility
- lead management and marketing automation (prospects, drip campaigns)
- integrated websites; branded mobile apps
- accounting integration (QuickBooks)
- online/virtual class delivery
- multi-location/enterprise management; staff time clock (with geolocation in one product)
- plan/edition tiering and per-feature gating

### L3 — Vendor-specific (Research Notes only)

- Studio Pro: Recital Wizard, Quick Change Warnings, stage-grid taping, Costume Console, Robo-Sizer™, Robo-Mailer, Magic Menu, plan names.
- Jackrabbit Dance: auto-sizing by girth measurement from vendor sizing chart, recital lineup assistant, program export to Word, Jackrabbit Pay, Jackrabbit Plus mobile app, Zapier connector.
- iClassPro: Autopilot Billing/Workflows, Pro Insights, ProCal, makeup tokens, geolocated clock-in, ProShop, Branded App (one-time setup fee + monthly, plan-gated).
- The Studio Director: drip-marketing presets, virtual classroom links per class location, pre-loaded vendor size charts.

## Vendor-specific vs Type Findings

- The costume + recital machinery is the signature **dance-vertical extension** of the shared class-management core; it is not the core itself (the cross-vertical product runs dance studios without it, and every vertical sells the same core).
- The recreational-vs-competitive split and competition-fee machinery is dance/GymDance-family culture, not generic class management.
- Flat unlimited-student pricing (Studio Pro) vs plan/feature gating (iClassPro, Jackrabbit) is business-model difference, not Type structure.

## Boundary Findings

1. **vs Fitness Studio Management** (directory sibling): fitness products center adult members, memberships, drop-in booking and class packs; dance studio products center guardian-child family accounts, season-enrollment tuition, and performance machinery. The product family straddles: The Studio Director sells into yoga/pilates/fitness, and dance products carry punch passes. Discriminator: who the customer record represents (family/guardian-child vs individual adult member) and the revenue model (season tuition vs membership/drop-in).
2. **vs After-school Program Management** (processed sibling in this repo): the two share the family-enrollment-attendance-billing spine. After-school centers scheduled out-of-school programs/care rosters per term; dance centers recurring weekly classes with tuition and performance machinery. Structural test: remove rosters/care framing → dance; remove weekly class + tuition model → program management.
3. **vs Sports Registration Platform**: one-shot registration transactions for programs/seasons vs the ongoing class relationship (roster, attendance, recurring tuition, portal) that the studio system manages year-round.
4. **vs Gym Management System**: membership-driven gym operations (access control, membership billing, check-ins) vs class-enrollment tuition operations.
5. **vs Membership Management / Billing Platforms**: generic membership logic is embedded here but enrollment-driven tuition is the billing trigger, not a membership tier.
6. **vs Childcare Management System**: care context (rooms, ratios, custody check-in/out) vs scheduled class business.
7. **vs School Management / SIS**: commercial studio business vs educational institution records.
8. **Taxonomy note (family problem)**: Dance Studio Management, Martial Arts School Management, Swim School Management, Gymnastics Club Management, Fitness Studio Management — the market evidence shows one product family (class management software for children's activity businesses) realized per vertical. The class-management spine (family account, scheduled classes, enrollment, tuition, attendance, portals) is identical across verticals; verticals differ in their signature extensions (dance: costumes/recitals/competition teams; swim: skill levels/makeups emphasis; gymnastics: skill tracking/meets). Keep this leaf as the dance realization and record for joint review whether the directory wants separate vertical leaves at all.

## Uncertainties

- Exact mechanics of tuition posting (per-cycle invoice generation, prorating rules, multi-class discounts) were not fetched at help-center depth for 3 of 4 products; no numeric parameters asserted anywhere.
- Waitlists: not directly observed in the sample; capacity management observed but waitlist behavior left unclaimed.
- The Studio Director's season/term model was not directly confirmed on the fetched page (its portal/billing features were); the season container is confirmed at A-strength only for Studio Pro and indirectly for Jackrabbit ("sessions").
- Payroll was not observed in the sample (time clock exists in one product); payroll is NOT claimed as part of this Type.
- iClassPro's lack of costume/recital machinery is an absence-of-evidence observation on one page, not proof the capability doesn't exist elsewhere in the product.

## Final Synthesis

Dance Studio Management is the operator-side business system for a dance studio: it organizes the studio's world into family accounts (guardians + student dancers), a calendar of recurring class offerings grouped in seasons/sessions, enrollments of students into classes, and the tuition money loop over the family account — then layers on the operational and dance-specific machinery that running a dance studio actually requires: attendance and makeups, portals for parents and staff, policies and waivers, recital and costume production, competition teams, and adjacent revenue (private lessons, camps, parties, dancewear retail). The class-management spine is shared with sibling verticals; the dance realization is distinguished by its performance machinery (costumes, recitals, competition culture) and the recreational-vs-competitive structure of its offer.
