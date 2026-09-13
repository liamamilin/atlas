# Research Notes — Camp Management System

Research date: 2026-09-06
Slug: camp-management-system
Directory location: §29 Home, Family, Personal & Local Services (siblings: Childcare Management System, Daycare / Preschool Management, After-school Program Management, Babysitting Marketplace). Note: the word "camp" also appears in §26 as Campground Booking Platform and Campground / RV Park Management — a different universe (lodging site rental), see Boundary Findings.

---

## Research Goal

Understand what a Camp Management System actually is as an Application Type: who operates it, what core objects exist inside it (sessions, campers, enrollments, groups/bunks, health records, seasonal staff, money, parent communication), how the season cycle works end to end (registration → forms → placement → daily operation → close-out), and where its boundary sits against the neighboring Types (After-school Program Management, Childcare Management, Event Registration, Course Registration, Campground/RV Park Management, Employee Scheduling).

This leaf also carries a **joint-review obligation** recorded in STATUS.md by the after-school-program-management pass: "after-school-program-management vs camp-management-system … same core spine; difference is schedule shape … flagged for joint review when Camp Management System is processed."

## Initial Boundary (pre-research hypothesis)

- Hypothesis: operator-side software for camps (day camps, overnight/summer camps, specialty camps, agency camps) that manages dated camp sessions, enrolls campers (usually minors) through guardians, and runs each session operationally: rosters, bunk/cabin groups, health & safety, seasonal staff, payments, parent communication.
- Primary users: camp directors, registrars/administrators, health staff (camp nurses), group leaders/counselors, staff coordinators; guardians as the self-service counterparty.
- Most likely confusions:
  - After-school Program Management (sibling; same enrollment spine, different schedule shape)
  - Childcare Management System / Daycare-Preschool Management (full-day licensed care, year-round)
  - Event Registration Platform (one-off dated events)
  - Course Registration System (registration transaction without camp operation)
  - Campground / RV Park Management (§26) — "camp" as lodging site rental, not youth program
  - Employee Scheduling Platform (camp staff scheduling is a module, not the center)
- Unknowns going in: whether bunk/cabin grouping is definitional or common; how deep the health machinery sits in the Type; whether "camp" products also handle off-season facility rentals; how the hybrid class+camp operators position camps; whether the residential (sleepaway) machinery is camp-defining or variant.

## Research Questions

1. What are the core objects (session/season, camper, guardian/household, enrollment, group/bunk, health record, staff record, charges/payments)?
2. How is the camp program calendar structured (sessions, date blocks, daily options, seasons)?
3. How does camper registration work (leads/inquiries, application, forms, deposits/payment plans, sibling handling)?
4. How central is bunk/cabin/group assignment, and who does it?
5. What health & safety machinery exists (health forms, medications, eMAR, incident reports, nurse role, access controls)?
6. How does seasonal staff hiring and management work (applications, references, background checks)?
7. What parent-facing surfaces exist during registration and during the session (portal, forms status, photos, messages)?
8. How does the season cycle close and repeat (reports, rollover, re-enrollment)?
9. Where are the boundaries with after-school, childcare, event/course registration, campground management, and off-season retreat/rental management?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Segment | Philosophy | Evidence quality |
|---|---|---|---|
| CampMinder | private summer camps (day + sleepaway), premium segment | full-suite camp operation: enrollment, health, staff, money, parent experience ("20+ camp-specific tools in one") | Strong (root + feature pages + Intercom help center) |
| UltraCamp | small/mid camps incl. faith-based, scout, agency camps | registration + session setup + health + retreat reservations + POS at accessible pricing | Strong (root + Zendesk help center) |
| CampDoc | camps + youth programs (incl. parks & rec, museums, universities, medical specialty camps) | health-first: camp EHR + registration + day-to-day operations, compliance posture (HIPAA/FERPA/SOC 2) | Strong (root/product pages; help center timed out) |
| iClassPro (camp object side) | youth activity centers running camps alongside classes | camp as a sibling object type inside a class-management product — joint-review anchor | Medium (official knowledgebase search index w/ titles/snippets; article pages 403) |
| Sawyer (from sibling research) | small children's activity businesses | Camp/Event as a schedule type inside activity registration — joint-review anchor | Recorded in research/after-school-program-management.md (glossary evidence) |

CampSite (second large US overnight-camp platform) was targeted but its site returned no content; dropped per source-access rules rather than replaced from memory.

## Sources

Tier 1 (official operational documentation):

- Campminder Help Center (Intercom): https://help.campminder.com/ — fetched 2026-09-06
  - Collection structure: Campminder Administration; Camper (Lead Management, Unified Person Record, Camper Enrollment and Management); Staff (Recruitment, Application, Management, Financials, Communication); Campminder Financials (Financial Admin and setup, billing, Payments, Reporting, Accounts, Fundraising); CampInTouch (Admin settings, Summer Services, page management); CampInTouch Summer Services (communication services for parents and campers); Medical Admin and The Health Center (Health Center Settings, Recording Treatments and Medications, Medical Reporting); Campanion (photos, push notifications, Letters, Microposts, camper forms); API
  - Note: public article coverage is shallow (1 article per collection); most operational documentation appears to be account-gated
- UltraCamp Help Center (Zendesk): https://help.ultracamp.com/ — fetched 2026-09-06 (first attempt transport error, second attempt succeeded)
  - Categories: Updates; Getting Started with UltraCamp; **Session Setup**; Forms and Questions; Account Management; Communication; **Health and Medical**; Reporting; Tools; **Retreat Reservations**; Integrations; Extra Services; General; Video Gallery
  - Promoted articles: "Should I use Activities or Options?"; "Transaction Summary"; SmugMug photo partnership (upload/sell photos); "Using UltraCamp to Collect Donations"; "Veritable Screening – Background Screening 101"; POS security updates
- iClassPro Support knowledgebase (Zendesk) search index for "camp": https://support.iclasspro.com/hc/en-us/search?query=camp — fetched 2026-09-06 (218 results)
  - Article titles/snippets: "How Do I Create a New Camp? (Camp Setup)"; "What are Camp Types?"; "How Do I Configure Camp Types and Pricing Schedules? (Camp Setup)"; "What is the CAMPS Page?" (Camp Name, Camp Dates, Instructors); "How Do I Duplicate a Camp?" (recurring camp offerings); "How Do I Make a Camp Inactive?" ("effectively cancels the remaining camp dates… future camp blocks"); "How Can I Use Camps for Events and Private Lessons?"; "What are the Camp Settings Options?" (camp enrollment, camp organization, camp billing); "What is the Camp Evaluation Form?"
  - Note: the individual article pages returned 403 on direct fetch; evidence is the official search index (titles + snippets)

Tier 2 (official product pages):

- CampMinder: https://www.campminder.com/ (root: FAQ, full feature module list) — fetched 2026-09-06
- CampMinder — Registration & Forms: https://campminder.com/features/registration-forms/ — fetched 2026-09-06
- CampMinder — Health Management: https://campminder.com/features/health-management/ — fetched 2026-09-06
- UltraCamp: https://ultracampmanagement.com/ (root/features served here) — fetched 2026-09-06
- CampDoc: https://www.campdoc.com/ — fetched 2026-09-06

Failed / limited sources:

- CampSite (campsiteapp.com): empty response → abandoned per source-access rules (second large US camp platform used only as market context, no claims)
- American Camp Association (https://www.acacamps.org/): 403 → industry-association terminology not directly citable; camp-operations framing rests on vendor documentation; UltraCamp lists ACA as a partner (badge only)
- CampDoc Help Center (https://support.docnetwork.org/hc/en-us/): timed out → operational health-workflow detail rests on product pages
- UltraCamp Session Setup category page (https://help.ultracamp.com/hc/en-us/categories/7087044793108-Session-Setup): timed out; category titles recorded from the help-center index instead
- iClassPro camp articles: 403 on direct article fetches; search-index titles/snippets used
- Cross-reference: research/after-school-program-management.md (fetched 2026-09-06 by the sibling pass) — Sawyer glossary ("Camps/Events — activity on consecutive days (e.g., Mon–Fri camp) or a one-off event"; Semester as the weekly-recurring alternative), iClassPro Class-vs-Camp sections, CourseStorm "class & camp registration" tagline

---

## Product Observations

### CampMinder (evidence layer A unless noted)

Positioning (Tier 2): "Summer Camp, Streamlined"; "20+ camp-specific tools in one"; "Day camps, sleepaway, from 20 campers to 2,000"; suites tiered by enrolled campers; 22 years in business; customer roster is overwhelmingly private/resident summer camps (plus some agency camps).

Full module list from root page (direct evidence of object machinery):

- Enrollment: Camper Application; Forms & Documents; Daily Options; Quick Application w/Multiple Siblings; Mobile Form & Document Scanner
- People: Unified Person Record (UPR); Household Management; Recruitment (leads)
- Staff: Staff Application; Integrated Background Checks; Applicant Tracking System
- Money: Integrated Financial Management; Automated Billing; Credit Card Reconciliation
- Operations: Daily Travel Assignments; Daily Attendance Reports; Group Requests; Drag-and-Drop Group Creator; Activity Scheduling & Elective Scheduling; Daily Activity & Schedule Reports
- Health: Health History; Health Center; eMar
- Parent experience: Web Photos & Videos; Letters & eLetters; Parent Mobile App (Campanion); Microposts; Facial Recognition; Photo Downloads; Email Marketing; Stylized Emails; Texting Integration
- Separate product: Gazebo — off-season events & rentals ("Can I use Campminder to run rentals and events in the off-season? … we have a whole separate solution for that")

Registration & Forms page (operational detail): online registration "automated yet flexible" (operator can let families self-register or keep manual control; discounts; personalized pricing); recurring payment plans; **"Form data is automatically coordinated with everything from bunking to health care to transportation."**

Health Management page: "integrated health care system"; "All health forms, from home and from the doctor's office, are collected into one Unified Person Record"; "Secure, organized records and reports of all health happenings for parents and directors"; "Health data is easily communicated across all operations from the kitchen to the cabins"; "care for all campers with any mental or physical health needs"; staff included: "We know your staff is your responsibility, too, so we count them in."

Help center structure (collection titles are direct evidence): lead management → UPR → camper enrollment; staff recruitment/application/management/financials; financials incl. **Fundraising**; CampInTouch = parent-facing portal with "Summer Services" (communication services for parents and campers); Medical Admin & The Health Center (settings, recording treatments and medications, medical reporting); Campanion = parent mobile app (photos, push notifications, letters, microposts, camper forms). Campanion described on root: "gives parents a smart photo feed that finds their kid using facial recognition."

Solutions by role (direct evidence of the role model): Owner & Director; Registrar; Camp Nurses; Staff Coordinator; Camp Families; Communications & Marketing; Business & Finance.

### UltraCamp (evidence layer A unless noted)

Positioning (Tier 2): "Summer Camp Management Software — Enjoy Camp Again"; "registration, reporting, staff management, and more"; targets small/mid camps ("very small camp… affordable… no huge upfront expense"; faith-based customers e.g. Camp Concordia, Camp Kulaqua).

Feature blocks (root page):

- **Session Management**: "create conditional registration options, ask questions, create payment plans, collect signatures, customize required waivers"
- **Health Management**: "track camper medications and distribution, incident reporting and everything else your camp nurse requires, all in one place"
- **Payments**: "automatic withdrawal payment plan"
- **Staff Management**: "streamline the Staff Application process with online forms, integrated background checks and third-party reference forms"
- **On-Site Management** and **Analytics & Reporting**: "report on virtually anything"
- **Communication Management** (customers, donors, prospects)
- **Donor Management** / **Finance Management** (nonprofit camp posture)
- **Conference & Retreat Management**: "create invoices and contracts for your groups, distribute usage calendar information across your team" — bundled, unlike CampMinder's separate product
- **Point of Sale Management**: "Seamless integration with our Store Deposits function allows you to charge your customers' house accounts directly at the register" (camp store/canteen against prepaid house accounts)

Help center (Tier 1): categories include **Session Setup**, Forms and Questions, Account Management, Communication, **Health and Medical**, Reporting, Tools, **Retreat Reservations**, Extra Services. Promoted articles confirm: Activities vs Options ("both offer additional choices…"), background screening integration (Veritable Screening), photo partnership (SmugMug: upload and sell photos), donation collection, POS.

Support posture: "UltraCamp customer support is limited to camp administrators only" — parents/campers are served by the camp, not the vendor.

### CampDoc (evidence layer A unless noted)

Positioning (Tier 2): "Camp and Youth Program Software Built for Registration, Health Management, and Day-to-Day Operations"; "Bring online registration, digital health records, payments, rosters, and reporting together… a safer day away from home"; "Powering 1,250+ camps, youth programs and school programs." Sister product SchoolDoc (schools) under parent DocNetwork.

Solution pillars (root page, direct evidence):

- **Online Registration**: signups and online payments; early registration, reservations, group signups; automatic confirmations, reminders, updates; reporting, exports, roster tools
- **Camp Health Records (EHR)**: digital health forms with conditional logic; uploads, reviews, and approvals; PHI access controls with permission profiles; incident reports and injury logs; **eMAR** for medication administration
- **Camp Management**: rosters and enrollment details in one place; attendance and day-of readiness; family communication and reminders; reporting across sessions and sites
- **Travel & Emergency Medical Protection** (protection plan) — vendor-specific service layer

Role surfaces: Directors & Operations (registration, sessions, communication, staffing, reporting, check-in/out & participant tracking); Health Staff (health forms & waivers, medication tracking & alerts, health history & allergies, incident & illness documentation); IT & Compliance (HIPAA & FERPA compliance, SOC 2 Type II, role-based PHI access, SSO, MFA).

Program-type breadth (direct evidence of the Type's market span): Day & Overnight Camps; Medical & Health Specialty Camps; Pre-College & University Programs; Parks & Recreation Programs; Aquarium, Museum & Zoo Programs; Sports & Athletics Camps; plus (site copy) after-school programs, childcare programs, YMCA camp, Girl Scouts, Scouting America, JCC camp, faith-based programs, school & auxiliary programs.

### iClassPro — camp object side (evidence layer A via official search index; article pages 403)

Knowledgebase structure confirms camp as a **sibling object type** to classes inside a class-management product:

- Camp setup dialog: camp details; **Camp Dates**; camp types (each camp assigned to one Camp Type; default type "Camp"); **pricing schedules per camp type**; general settings controlling "camp enrollment, camp organization, and camp billing"
- CAMPS page lists camps with name, dates, instructors — camps have their own assigned instructors
- "Duplicate a Camp" for recurring camp offerings (the season-repeat mechanism)
- "Make a Camp Inactive": "effectively cancels the remaining camp dates. Because those future camp blocks…" — camps are structured as **dated blocks**
- "How Can I Use Camps for Events and Private Lessons?" — the camp object doubles as a generic dated-offering container for non-class programming
- Camp Evaluation Form — printable per-camp skills list for instructors (specialty-camp variant)
- Footer shows sibling product iCampPro ("Camp Registration Software")

Cross-reference from the sibling pass (evidence layer A recorded in research/after-school-program-management.md): Sawyer glossary defines **Camps/Events** as "activity on consecutive days (e.g., Mon–Fri camp) or a one-off event" as a schedule type alongside **Semester** (weekly repeating); CourseStorm markets "class & camp registration"; iClassPro's marketing claims "over 100 million class & camp registrations."

---

## Cross-product Comparison

| Dimension | CampMinder | UltraCamp | CampDoc | iClassPro (camp object) |
|---|---|---|---|---|
| Operator self-term | camp management ("Summer Camp, Streamlined") | summer camp management software | camp and youth program software | camp section inside class management |
| Dated program unit | camp sessions + Daily Options; data flows "from bunking to health care to transportation" | **Session Setup** (conditional options, questions, signatures, waivers) | sessions; early registration; reservations; group signups | Camp = Camp Dates / dated blocks; Camp Types; per-type pricing schedules |
| Camper/guardian structure | Unified Person Record + Household Management; Quick Application w/Multiple Siblings | Account Management category; family accounts | family-facing workflows; confirmations/reminders | family/student accounts (sibling research) |
| Lead/recruitment | Recruitment + lead management collection | — (no lead module observed) | — (not observed) | — (not observed) |
| Forms machinery | Forms & Documents; Mobile Form & Document Scanner; flows into all operations | Forms and Questions; signatures; waivers; conditional registration options | digital health forms w/ conditional logic; uploads, reviews, approvals | camp settings for enrollment/billing; waivers (sibling research) |
| Health machinery | Health History; Health Center; eMar; nurse role; staff included; "kitchen to the cabins" | Health and Medical: medications & distribution, incident reporting, "camp nurse" | full camp EHR: health forms, med tracking & alerts, eMAR, incident/injury logs, PHI access profiles, HIPAA/FERPA | none (out of scope for that product) |
| Groups/bunks | Group Requests; Drag-and-Drop Group Creator; "from the kitchen to the cabins" | not observed on fetched pages | not observed on fetched pages | camp organization setting |
| Daily operations | Daily Attendance Reports; Daily Activity & Schedule Reports; Activity Scheduling & Elective Scheduling; Daily Travel Assignments; Transportation module | On-Site Management | attendance & day-of readiness; check-in/out & participant tracking | per-camp rosters/attendance (sibling research) |
| Seasonal staff | Staff Application; Integrated Background Checks; ATS; Recruitment; staff coordinator role | Staff Application process; integrated background checks; third-party references | staffing surface for directors | staff module (sibling research) |
| Money | Integrated Financial Management; Automated Billing; Credit Card Reconciliation; Fundraising | payments w/ automatic-withdrawal payment plans; donations; Finance Management | payments included | camp pricing schedules; camp billing settings |
| Camp store/canteen | — (not observed) | Store Deposits + POS against house accounts | — (not observed) | POS (sibling research) |
| Parent portal & session comms | CampInTouch + Summer Services; Campanion app: photos, facial recognition, letters & eLetters, microposts, push | Communication Management; SmugMug photo upload/sales | family communication and reminders | customer portal (sibling research) |
| Off-season/retreat use | Gazebo (separate product) | Conference & Retreat Management + Retreat Reservations (bundled) | — (not observed) | camps reused for events/private lessons |
| Reporting | Reporting module + role dashboards | "report on virtually anything"; Transaction Summary | reporting across sessions and sites | report library (sibling research) |
| Season cycle | historic data import at onboarding; annual enrollment | session copy/duplicate (setup orientation) | — | Duplicate a Camp for recurring offerings |
| Compliance posture | — (not observed on fetched pages) | — | HIPAA & FERPA, SOC 2 Type II, role-based PHI access, SSO/MFA | — |

### What is shared across the sample (candidate core)

1. A **dated session structure** as the sellable/runnable program unit (CampMinder sessions + daily options; UltraCamp Session Setup; CampDoc sessions; iClassPro camp dates/blocks).
2. **Camper enrollment through a guardian/family account** (household/sibling machinery in all sampled camp products).
3. **Rosters as the operating surface** for each session (attendance/day-of readiness across CampMinder, CampDoc; rosters implied by iClassPro camps page).
4. **Forms-and-documents machinery** wrapping enrollment (waivers, signatures, permissions, health forms; review/approval states in CampDoc; document scanning in CampMinder).
5. **Health & safety management** in all three pure camp products (health history, medications, treatment/incident logging, nurse role) — the most distinctive module of the Type.
6. **Seasonal staff hiring** with background checks (CampMinder + UltraCamp explicit; CampDoc staffing surface).
7. **Tuition money machinery** (billing, payment plans, refunds/reconciliation; donations for nonprofit camps).
8. **Parent communication** (portal, email/text, and during-session parent experience: photos, messages).
9. A **seasonal business cycle**: prepare months before, run compressed sessions, close out, repeat next year (duplicate/rollover machinery evidenced in iClassPro; onboarding data import in CampMinder).

### What varies (candidate variant axes)

- **Day vs overnight**: residential camps add bunks/cabins, canteen house accounts, parent photo/letter services; day camps (parks & rec, school auxiliary) run lighter: sessions-per-week patterns, daily options, check-in/out.
- **Operator type**: private independent camps (recruitment-heavy), agency camps (YMCA/Scouts/faith/JCC — membership context), municipal (parks & rec), school auxiliary/university pre-college (compliance-heavy), specialty (sports/arts/STEM/medical).
- **Object plurality**: pure camp suites vs camp-as-sibling-object inside class/activity products (iClassPro, Sawyer, CourseStorm).
- **Off-season posture**: bundled retreat/conference management (UltraCamp) vs separate product (CampMinder's Gazebo) vs absent.
- **Health depth**: full camp EHR (CampDoc) vs integrated health center (CampMinder) vs medications/incidents (UltraCamp) vs none (class-management camp objects).
- **Compliance posture**: PHI-grade controls appear in health-first products (CampDoc: HIPAA/FERPA/SOC 2/SSO/MFA).

---

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (minimal)

The Type is recognizable only if all three hold:

1. **Camp session calendar** — the operator defines its offering as dated camp sessions (consecutive-day program periods — day or overnight — with capacity, eligibility, and tuition), grouped into a seasonal business cycle. The session, not a recurring weekly class and not a one-off event, is the unit the whole system revolves around.
2. **Camper enrollment via a guardian account** — enrollment binds a specific camper (typically a minor) to a session through a guardian/family account; the camper carries the session-relevant profile (age/grade, forms, health).
3. **Roster-run sessions** — each session is operated from its roster of enrolled campers (attendance, supervision, daily programming, health/safety decisions).

Tests:
- Remove the session calendar → generic child/family CRM or membership system.
- Remove the camper/guardian enrollment shape → generic event registration (attendee, no minor-with-guardian relationship, no camp operation).
- Remove the roster → pure e-commerce booking with no operational surface.
- Remove the seasonal/session shape (keep everything else) → After-school Program Management (sibling Type).

Historical/market-sample check: a 2000s overnight-camp registration database (sessions, bunk lists, health forms, tuition), a scout-camp council system (week-long sessions, troops/campsites as groups), and a municipal day-camp module (weekly themed sessions, rosters, emergency forms) all satisfy these three structures without any modern SaaS specifics (parent apps, photo AI, donor CRM, eMAR). The L0 does not overfit to the current market.

Note on what was deliberately kept OUT of L0 despite near-universality in the sampled pure-camp products: bunks/groups (absent from some day-camp deployments; class-management camp objects lack them entirely), structured health modules (present in all three pure camp products but absent from hybrid camp objects), staff hiring, transportation, and parent photo services. These are L1/L2.

### L1 — Common Mature Structure (very common in mature camp products; not definitional)

- Guardian/family account with household and sibling handling (multiple campers, sibling applications, saved payment methods).
- Forms & documents machinery: registration packets, waivers/permissions/signatures, custom questions, document review/approval states, completion reminders; conditional logic on forms.
- Lead management / recruitment funnel for new families (private-camp segment).
- Health management: health history, allergies, medications; medication administration records (eMAR); treatment/incident logging; a health-staff (nurse) role; restricted health-data access.
- Bunk/cabin/group assignment for sessions (group-mate requests, drag-and-drop group building, staff-to-group assignment) — near-universal in residential deployments.
- Daily session operations: attendance/day-of readiness, activity and elective scheduling, daily schedule reporting, transportation/bus assignments, check-in/out.
- Seasonal staff machinery: applications, references, background checks, hiring/status tracking, staff-facing rosters.
- Tuition money machinery: billing cycles, payment plans with scheduled automatic payments, refunds/reconciliation; camp store/canteen against prepaid house accounts in some products; donation collection for nonprofit camps.
- Parent portal and session-time communication: forms/status, confirmations, email/text, photo sharing, one-way camper messaging in some products, mobile parent apps.
- Reporting: enrollment, financial, health, operational, retention; role-scoped dashboards.
- Season cycle: duplicate/rollover sessions, re-enrollment waves (returning-family early registration), end-of-season reporting.

### L2 — Variant / Optional Structure

- Overnight/sleepaway overlay: bunks/cabins as living units, canteen/store house accounts, laundry/packing-adjacent features, parent photo services (incl. face-based filtering in one product), one-way eLetters.
- Day-camp-only deployments (municipal/school): weekly session patterns, daily options (per-day enrollment), lighter forms.
- Off-season use: conference/retreat/facility-rental management — bundled in some products, sold as a separate product by others, absent in the rest.
- Hybrid operator posture: camps as sibling objects inside class/activity-registration products (class+camp under one roof); camp object reused as generic dated-offering container (events, private lessons).
- Specialty overlays: medical/specialty-needs camps (conditional health forms), skill/evaluation forms per camp, pre-college/university youth-program compliance posture.
- Compliance/IT posture: HIPAA/FERPA alignment, SOC 2, role-based PHI access, SSO/MFA (health-first products; institutional buyers).
- Donor/development machinery (nonprofit/agency camps).
- Photo monetization integrations; background-screening vendor integrations.

### L3 — Vendor-specific (research notes only)

- CampMinder: Unified Person Record, Campanion (facial-recognition parent photo feed), Microposts, CampInTouch/Summer Services, eMar, Daily Travel Assignments, Gazebo (separate off-season events/rentals product), "20+ tools" / camper-count tiering, 22-years positioning.
- UltraCamp: Activities-vs-Options registration choices, Store Deposits house accounts, SmugMug photo partnership, Veritable Screening integration, donation tools, admin-only support policy, "report on virtually anything" posture.
- CampDoc: protection plan (travel & emergency medical), DocNetwork/SchoolDoc family, 1,250+ camps claim, $355/month starting price, G2/Capterra ratings claims.
- iClassPro: camp setup dialog specifics, Camp Types + pricing schedules, camp evaluation form, iCampPro sibling product, "100 million class & camp registrations" marketing claim.
- Sawyer: Camps/Events schedule type, Sawyerspeak glossary terms (from sibling research).

---

## Vendor-specific Findings

See L3. None promoted to the canonical model. Two near-miss over-generalizations were checked and kept out of the core:

- **Bunk/cabin grouping** is highly characteristic of camps, but it is absent from day-camp deployments of registration-style products and from class-management camp objects; it is documented as standard camp machinery (L1) with an overnight/variant flavor (L2), not a defining invariant.
- **Health-center depth** varies from full camp EHR to simple medications/incident logging; the *presence of health-and-safety duty* is best treated as standard structure (L1) with depth as the variant axis, because the hybrid camp objects in the sample carry no health module at all.

---

## Boundary Findings

1. **vs After-school Program Management (§29 sibling; JOINT REVIEW COMPLETED)**: same core spine — operator program calendar + guardian-initiated child enrollment + per-offering/session roster. The difference is the **schedule shape and the operational overlay**: camps sell and run dated, consecutive-day sessions (often overnight) inside a seasonal annual cycle, with the camp-operation overlay that mature camp products carry (bunks/groups, health center, seasonal staff hiring, transportation, session-time parent services); after-school programs run recurring weekly school-year offerings. Direct evidence that the market treats them as sibling object types inside one product: iClassPro has separate Class and Camp sections; Sawyer's schedule types are Semester vs Camp/Event ("activity on consecutive days"); CourseStorm's tagline is "class & camp registration." Joint-review conclusion: **related Types sharing a core, not duplicates** — both directory leaves stand; each documents the seam from its own side.
2. **vs Childcare Management System / Daycare-Preschool Management (§29 siblings)**: full-day, year-round, licensed care organized by rooms/ratios/licensing vs seasonal session-based programs. CampDoc's own program-type list includes "childcare program" alongside camps — vendors span both; gradient on the care/licensing overlay, not a wall.
3. **vs Event Registration Platform (§26 area)**: a one-off event has attendees; a camp session has enrolled campers under guardian accounts plus forms/health/roster operation. Generic event-registration tools can process camp transactions, but they lack the camp-operation layer (health machinery, bunks, seasonal staff, session rosters). Camp products include one-off events only as optional objects (iClassPro reuses camps for events; Sawyer Camps/Events).
4. **vs Campground Booking Platform / Campground-RV Park Management (§26) — NAMESAKE, NOT A NEIGHBOR**: "camp" in §26 means lodging-site rental (campsites, RV hookups, nightly stays); here it means supervised youth-program sessions. No shared objects beyond the word (a campsite record vs a camper session). Recommend the §26 passes state the mirror-side distinction. (Same pattern as the advocacy-platform / customer-advocacy-platform name collision recorded in STATUS.md.)
5. **vs Course Registration System (§23)**: the registration transaction is the center there; here registration is the entry to operating a session. Registration-first products (CourseStorm) blur the edge when deployed for kids' camps — flagged in the sibling pass as well.
6. **vs Employee Scheduling Platform (§09)**: camp products hire and assign seasonal staff (applications, background checks, group/activity assignment), but scheduling there serves the camp session; labor-shift management as the center is a different Type.
7. **vs Off-season retreat/conference & facility rental management**: the camp's facility is rented to groups off-season; some products bundle this (UltraCamp Retreat Reservations), others split it into a separate product (CampMinder Gazebo) — evidence that group/rental management is an adjacent capability, not camp core.
8. **vs Hotel PMS (§26)**: both have "guests in dated stays," but the PMS centers room inventory + folio + occupancy; camp management centers program enrollment + roster + supervision. A residential camp's cabin inventory is organizational (bunking), not revenue-per-night lodging.

---

## Uncertainties

- **ACA (industry association)**: acacamps.org returned 403. The camp industry's professional-association framing (standards, health-form expectations) could not be directly cited; camp-operations structure rests on vendor documentation only. UltraCamp's ACA partner badge and CampDoc/CampMinder's health/staff-safety machinery corroborate the context indirectly.
- **CampSite**: unreachable (empty responses). The US overnight-camp market is often described as having two leading platforms; this pass rests on CampMinder as the residential-segment anchor, and cross-product claims for the residential segment are supported by at most two pure-camp products (CampMinder + UltraCamp) plus CampDoc.
- **Bunking workflow detail**: parent group-mate requests and drag-and-drop group creation are evidenced (CampMinder module names + feature-page phrasing "from bunking to health care"), but the full assignment workflow (approval, capacity per bunk) was not documented in reachable sources.
- **Session capacity/waitlist behavior** in camp products was not directly evidenced; kept generic (after-school machinery suggests the pattern but that is inference, not camp-specific evidence).
- **Deposits**: commonly associated with camp enrollment but not explicitly evidenced in fetched pages; not asserted in the final document.
- **Geographic scope**: sample is North American. International camp markets (UK multi-activity camps, holiday-camp providers, etc.) were not sampled; the L0 was kept implementation-neutral, but their regulatory overlays are unverified.
- **Public help documentation is thin** in this segment (CampMinder's help center is largely account-gated; CampDoc's timed out; iClassPro articles 403). Evidence skews to product pages + help-center indexes; precise operational parameters are correspondingly absent from the final document.

---

## Final Synthesis

A Camp Management System is operator-side software for running camps: seasonal, session-based programs — day or overnight — for children and young people. Its defining structure is small: a camp session calendar (dated, capacity-bounded, tuition-bearing consecutive-day sessions organized in a seasonal cycle); camper enrollment bound to sessions through guardian/family accounts; and session rosters as the operating surface. Around that core, mature camp products add the machinery that running a session actually requires: forms-and-documents packets with review/approval states, health management (health history, medications, eMAR, incident logging, nurse role), bunk/cabin/group placement, daily operations (attendance, activity scheduling, transportation, check-in/out), seasonal staff hiring with background checks, tuition billing with payment plans (plus camp-store house accounts and donations where applicable), a parent portal that extends into the session itself (photos, messages, forms), reporting, and the season-cycle machinery (duplicate/rollover, re-enrollment waves). The Type shares its enrollment spine with After-school Program Management — the joint review confirmed sibling Types distinguished by schedule shape and camp-operation overlay, with vendors shipping camps and classes as sibling object types in single products — and it shares nothing structural with the §26 "campground" Types beyond the word "camp."
