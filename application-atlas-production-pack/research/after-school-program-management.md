# Research Notes — After-school Program Management

Research date: 2026-09-06
Slug: after-school-program-management
Directory location: §29 Home, Family, Personal & Local Services (siblings: Childcare Management System, Daycare / Preschool Management, Camp Management System, Babysitting Marketplace)

---

## Research Goal

Understand what "After-school Program Management" software actually is as an Application Type: who operates it, what core objects exist inside it, how the registration→enrollment→roster→attendance→billing loop works, and where its boundary sits against the neighboring childcare / daycare / camp / class-registration Types.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: operator-side administration software for organizations that run scheduled out-of-school-time programs for children (after-school care, enrichment classes, tutoring, clubs, sports clinics).
- Primary users: program administrators/coordinators at youth activity businesses, school-district community education departments, and childcare providers offering school-age care; guardians (parents) as the self-service counterparty.
- Most likely confusions:
  - Childcare Management System / Daycare-Preschool Management (full-day licensed care)
  - Camp Management System (seasonal sessions)
  - Course Registration System / Event Registration Platform (registration transaction without ongoing child-program relationship)
  - Tutoring Platform (instruction delivery vs operator administration)
  - Student Information System (school of record)
- Unknowns going in: whether billing is definitional; whether attendance is definitional; how strongly the market ties this Type to the "class management software" term used by youth-activity vendors; how the district/community-education segment differs structurally.

## Research Questions

1. What are the core objects (program/class/activity, schedule/semester/session, family/student, enrollment/booking, roster, attendance, charges/payments)?
2. How does registration work: enrollment windows, priority registration, capacity, waitlists?
3. How is the schedule structured (sessions vs rolling enrollment vs semesters vs camps)?
4. How does attendance/check-in work (staff-recorded, kiosk, sign-in/out)?
5. How does billing work (tuition cycles, autopay, discounts, payment plans, refunds, ledger)?
6. What roles exist (admin, site coordinator, instructor, guardian) and what can each see/do?
7. What parent/guardian-facing surfaces exist (portal, widget, mobile app)?
8. Where is the boundary with childcare/daycare management, camp management, event registration, course registration?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Segment | Philosophy | Evidence quality |
|---|---|---|---|
| iClassPro | youth activity centers (gymnastics/cheer/swim/dance) | class+camp+party+POS all-in-one operator platform | Strong (Zendesk knowledgebase + deep articles) |
| Sawyer (Sawyer for Business) | small children's activity businesses; marketplace-listed providers | registration + parent experience + marketplace discovery | Strong (Intercom help center + official glossary) |
| CourseStorm | community education / arts orgs / kids programs (incl. districts) | "impossibly simple" registration-first, catalog+roster+payments | Medium (marketing feature pages; help portal not article-fetched) |
| Jackrabbit (Jackrabbit Class) | youth activity centers (gym/dance/swim/cheer/music verticals) | class management for youth activity centers | Weak (root/product pages only; help center unreachable) |
| Procare Solutions | child care centers + explicit "Before and After School Programs" segment | childcare management suite (care-context anchor for boundary) | Weak-medium (root page; segment page not fetched) |

Eleyo (school-district community education / school-age care) was targeted as a fifth sample but its support guide (learn.eleyo.com) timed out twice and the corporate site is a stub; abandoned per source-access rules. District-segment evidence therefore rests on CourseStorm's community-education positioning plus Procare's before/after-school segment page.

## Sources

Tier 1 (official operational documentation):

- iClassPro Support knowledgebase (Zendesk): https://support.iclasspro.com/hc/en-us/categories/202704148-Knowledgebase — fetched 2026-09-06
  - "How Do I Manage Sessions and Rolling Sessions?" — https://support.iclasspro.com/hc/en-us/articles/35267806398871
  - "How Do I Manage Families in the Office Portal?" — https://support.iclasspro.com/hc/en-us/articles/218570418
- Sawyer for Business Support (Intercom): https://help.hisawyer.com/ — fetched 2026-09-06
  - "Sawyerspeak Terminology" — https://help.hisawyer.com/en/articles/14646321-sawyerspeak-terminology
  - "How to Create an Activity" — https://help.hisawyer.com/en/articles/11105792-how-to-create-an-activity
  - "Schedules and Listings" collection index (70 articles: Booking Management/Rosters, Cancellation Policies, Free Trials, Appointments, Online Activities, Waitlists, Listings, Form Fields, Semesters, Camps/Events, Editing Schedules)

Tier 2 (official product pages):

- iClassPro: https://www.iclasspro.com/ — fetched 2026-09-06
- Jackrabbit Technologies: https://www.jackrabbittech.com/ — fetched 2026-09-06
- Sawyer for Business: https://www.sawyertools.com/ (alias of hisawyer.com/for-business) — fetched 2026-09-06
- CourseStorm: https://coursestorm.com/ and https://coursestorm.com/class-management-features — fetched 2026-09-06
- Procare Solutions: https://www.procaresoftware.com/ — fetched 2026-09-06

Failed / limited sources:

- Eleyo: https://www.eleyo.com/ (stub page only); https://learn.eleyo.com/ timed out twice → abandoned. District/school-age-care segment documented via CourseStorm + Procare instead.
- Jackrabbit help center (help.jackrabbittech.com): transport error → Jackrabbit evidence limited to positioning-level product pages.
- 6crickets: homepage is JS-rendered, no content extractable → not used.
- hisawyer.com root: 403; sawyertools.com used instead.

---

## Product Observations

### iClassPro (evidence layer A unless noted)

Positioning (Tier 2): "Class Management Software for Gymnastics, Cheer, Swim, and Dance Schools — Manage Classes, Camps, Private Lessons, Birthday Parties, Events, Student Attendance, Staff, Waivers, Email, SMS and more." Since 2008; "over 100 million class & camp registrations".

Knowledgebase structure (section titles are direct evidence of module existence): General, Getting Started, Account Setup, Administrator, Portals/Kiosks, Appointments, Autopilot (automated billing workflows), Billing Settings, Camp, Charges and Payments, Class, Communications, Customer Portal/Mobile App, Ledger, Makeup Tokens, Pages & Filters, Party Booking Management, Point of Sale, Policies, Punch Passes, Report, Skill Tracking, Staff, Time Clock, Data Warehouse (Pro Insights), Enterprise Portal, Payment Services.

Key operational findings:

- **Family/Student structure**: Family account holds guardians (primary + secondary, configurable relationship types) and attached students. New Family Wizard collects guardian details, emails (primary email used for portal login and statements; duplicate primary email blocked), phones (opt-in/out for texts), addresses, referral source, flags, special discounts, keywords, custom fields. Family profile tabs include Students, Enrollments, Ledger, Autopay, Keywords, Notes, Custom Fields, Policies, Billing.
- **Primary guardian semantics**: changing the primary guardian (or family merge) revokes all secondary portal access, voids all policy acceptances (re-acceptance forced at next portal login), and removes payment information associated with the guardian. Only the primary payment method linked to the primary guardian is used in recurring billing. Up to three payment methods per guardian; recurring-billing authorization is an explicit opt-in with notification emails.
- **Family suspension**: "Suspend Family" blocks Customer Portal/Mobile App logins.
- **Class + Session model**: classes are recurring offerings; Sessions have fixed start/end dates — enrollments automatically drop when the session ends and families must re-enroll; Rolling Sessions use recurring date ranges (e.g., every 4–6 weeks) and enrollments continue until a manual drop date. Session type cannot be changed after assignment (requires duplicate class + transfer enrollments + inactivate original). Registration Start/End dates control when classes linked to a session are visible for registration in the Customer Portal; Priority Registration windows exist for families carrying a priority keyword.
- **Billing**: class tuition charges by session, monthly, or weekly cycles; automated billing workflows (Autopilot) chain tuition charges → credits → payment capture; discounts and promo codes; anniversary charges; ledger of charges and payments; financial reports (bank deposit, program deposit split); payment services with merchant portal, disputes, payouts, eCheck returns.
- **Attendance & check-in**: staff record attendance in the Staff Portal; check-in kiosk app (iPad, guided access) with QR codes for student/staff check-in; front-desk and staff attendance.
- **Camp as sibling object**: separate Camp section — camp types, pricing schedules, camp enrollment wizard, group enrollment; camps are distinct from classes.
- **Enrollment operations**: enrollment wizard, edit/drop enrollment with configurable drop reasons, group transfer tool, future absences, makeups (makeup tokens, auto-generated scheduling, portal requests), trial requests, punch passes, appointments (1:1), party booking (birthday parties with time slots), POS (products, returns).
- **Skill tracking**: disciplines → skill levels → skill events; student evaluation forms; automatic email on level "Passed"; certificate designer. (Youth-activity segment specific.)
- **Staff**: staff portal app, "My Schedule", substitutes for absent instructors, time clock with payroll service integration, staff permissions.
- **Communications**: Messenger Center, email blasts (scheduled), SMS with compliance logs, custom templates.
- **Policies**: family/student/transactions policies accepted electronically in the Customer Portal; photo waiver; staff can manually accept with permission.
- **Customer Portal**: families create accounts, add students, register, submit trial/makeup requests; branded app option.
- **Enterprise Portal**: multi-location oversight, subgroups/users, dashboards, embedded Power BI.
- **Pro Insights** (vendor-specific analytics): conversion rate, average family spend, family tenure, net family gain, waitlisted-only students, quarterly performance.

### Sawyer (evidence layer A unless noted)

Positioning (Tier 2): "registration and management software for children's activity businesses"; industries: art, academics, cooking, dance, sports & fitness, nature, music, STEM, language, play space, theater; business types explicitly include **Camps, After School, Small Business, Franchise**. Marketplace: "the world's leading marketplace for children's activities, camps and classes".

Official glossary ("Sawyerspeak" — direct evidence of the vendor's object model):

- **Activity** — "The class, camp, or program you offer for customers to book."
- **Appointment** — 1:1 activity, one instructor + one student, per-slot booking.
- **Booking** — "A single reserved spot for a student in an activity or appointment."
- **Camps/Events** — activity on consecutive days (e.g., Mon–Fri camp) or a one-off event.
- **Drop-in** — purchasable single day of class.
- **Instance** — "a single scheduled date and time for an activity (like one class date in a multi-week series)."
- **Marketplace** — where families find and register for classes offered by Sawyer providers.
- **Provider** — "An organization (usually a small business but sometimes a non-profit, a school, or a private tutor) that runs out-of-school-time activities for children." ← vendor's own definition of the operator role; strong confirmation of the Type's domain framing.
- **Rush Registration** — short high-demand registration window.
- **Schedule** — the time frame (Semester or Camp/Event) defining the date range a program runs.
- **Scheduled Activity** — the specific class/session inside that schedule (e.g., "Monday 4pm" within a Semester).
- **Semester** — set date range for weekly, repeating activities.
- **Widget** — registration interface embedded in the provider's website.
- **Widget Tags** — filter which activities appear in a given widget.

"How to Create an Activity" (operational detail):

- Activity = listing with name, color, category (marketplace search facet), in-person/online type, summary, class requirements, skills learned, what to bring, photos (primary photo drives marketplace/widget display).
- Audience definition: "Who can register?" — Children Only (default) / Adults Only (18+) / Mixed Ages; age range or grade range; adult presence/participation (none/optional/required).
- Optional details: grades/assessments (none / pass-fail / letter grades), homework, pod learning flag, additional notes, notes for confirmation email, hashtags.
- Scheduling is separate from listing: Schedules tab → Semesters (timeframes) → add activities; copy schedule; per-day capacity edits ("single instance" edits); holiday/closing marking on a time frame; rescheduling classes; close registration early; hide from widget.
- Help-center collections confirm module existence: Booking Management (roster details/view, viewing student info on roster, editing/removing student enrollment, class notes, transfer audit history, single-day and multi-day transfers, transfer email confirmations), Cancellation Policies, Free Trials, Appointments, Online Activities (Zoom), Waitlists (Waitlist 2.0: add customer, invite to register, management notifications, reporting), Listings (locations, dynamic location capacity), Form Fields (policies and waivers, e-signature agreements, responses), Semesters, Camps/Events, Payment Plans, Reporting Hub, For Instructors, Orders and Financials, Marketplace.

### CourseStorm (evidence layer A for feature pages; positioning is Tier 2)

Positioning: "class & camp registration" software; customer segments: Arts & Culture, **Community Ed**, Continuing Ed & Workforce, **Kids Activities & Camps**; "550+ organizations"; used by arts centers and community education programs.

Class-management feature page (direct evidence):

- **Dynamic rosters**: real-time signups; view student details and payment status; transfer a student; issue refunds; message individual students or a full roster.
- **Waitlists**: trigger automatically when a class reaches its cap; one-click registration invite link to the top of the waiting list.
- **Payment plans**: automated installment plans for pricier offerings.
- **Instructor admin portal**: instructors/teaching artists see up-to-date student rosters and take attendance from their phones; they cannot see or control payment status (admin-only).
- **Custom forms**: custom questions per class (e.g., kids-class intake questions).
- Registration features (root page): catalog building, website widget embedding, registration data to CRM, API; abandoned-cart emails; low-enrollment alerts; class recommendations; "Just Ask" AI reporting assistant.

### Jackrabbit (evidence layer A for positioning only; Tier 2 source)

- "The #1 Cloud-Based Class Management Software for Youth Activity Centers — Gymnastics • Dance • Swim • Cheer • Music"; also serves theater, horse riding, art, martial arts, ninja gyms.
- Value framing (Tier 2, marketing): optimize class schedules and management, automate billing, communicate with customers, reporting; integrations marketplace; 99.9% uptime framing.
- Vertical editions (Jackrabbit Class/Dance/Swim/Cheer/Music) indicate the same core sold per youth-activity vertical.
- No operational documentation reachable in this environment → no operational claims recorded for Jackrabbit.

### Procare Solutions (evidence layer A for positioning; boundary anchor)

- "The Leader in Child Care Management Software"; solutions list includes **"Before and After School Programs"** and "Youth Organizations" alongside Child Care Centers, Head Start.
- Capabilities: family information, attendance tracking, tuition automation, family engagement, payment processing, classroom management, enrollment planning (RoomRunner), ratios (customer review mentions "dashboard that shows student ratio per classroom").
- Confirms that the childcare-management family of products sells into the before/after-school segment — i.e., the two Types share vendors and much machinery, differing in care context.

---

## Cross-product Comparison

| Dimension | iClassPro | Sawyer | CourseStorm | Jackrabbit | Procare (boundary anchor) |
|---|---|---|---|---|---|
| Operator term for self | class management software | Provider ("runs out-of-school-time activities for children") | class registration for community ed/arts/kids | class management software for youth activity centers | child care management (before/after-school segment) |
| Program object | Class (+ Camp, Appointment, Party, POS) | Activity (+ Appointment; Camps/Events as schedule type) | Class/camp (course catalog) | Class (per vertical editions) | Classroom/child (care context) |
| Schedule container | Session / Rolling Session (+ registration windows, priority registration) | Semester / Camp-Event schedule; Instance = one date | class sessions; catalog terms | sessions (per positioning; not operationally verified) | rooms + care days (full-day context) |
| Enrollment unit | enrollment of a student in a class/camp | Booking ("a single reserved spot for a student") | registration of a student | enrollment (implied) | child enrolled in care |
| Family structure | Family = guardians (primary/secondary) + students; portal login via primary guardian email | family profiles; saved family profiles speed checkout | student records; guardian registration (implied by kids segment) | family/customer accounts (implied) | family records; parent engagement app |
| Roster | per-class/camp rosters; staff portal attendance; kiosk check-in w/ QR | roster details/view; edit/remove enrollment; transfers (single/multi-day) | dynamic real-time rosters; instructor attendance from phone | rosters (positioning) | attendance tracking (care-grade) |
| Waitlist | yes (waitlisted-only students metric) | Waitlist 2.0 (invite flow, notifications) | auto-trigger at cap + one-click invite | (not verified) | (not verified) |
| Billing | tuition by session/monthly/weekly; autopay workflows; discounts/promos; ledger; payment services | payment processing; payment plans; gift cards; trials; cancellation policies | registration payments; payment plans; refunds | automated billing (positioning) | tuition automation; payment processing |
| Enrollment changes | drop w/ reasons, group transfer, makeups/tokens, trials, punch passes, drop-ins | transfers (single/multi-day) w/ audit + confirmations; drop; free trials; drop-ins | transfers, refunds | (not verified) | (not verified) |
| Instructor role | staff portal: attendance, student details, substitutes, time clock | For Instructors collection; instructor-facing guides | instructor portal: rosters + attendance, no payment visibility | (not verified) | classroom staff |
| Guardian surfaces | Customer Portal + mobile app + branded app | widget on provider site + marketplace + parent experience | embedded catalog widget + registration flow | parent portal (positioning) | parent app |
| Communication | email blasts, SMS w/ compliance, templates, Messenger Center | automatic emails, confirmations, notes | messaging rosters, abandoned-cart, low-enrollment alerts | communication (positioning) | family engagement |
| Multi-site | Enterprise Portal (subgroups, dashboards) | locations; dynamic location capacity | (org-level) | (not verified) | multi-center/franchise |
| Segment-specific extras | skill tracking, party booking, POS, time clock | marketplace, pod learning, online activities, hashtags | AI reporting, donor/CRM integrations | vertical editions | ratios, licensing, daily reports (care context) |

### What is shared by all (candidate core)

1. An operator-defined catalog of scheduled programs for children (with capacity, age/grade eligibility, schedule).
2. Child-specific enrollment created by/for a guardian (family account as the enrollment's owner; child as the participant).
3. Per-offering rosters of enrolled children that staff work from (attendance/check-in recorded against them).
4. A guardian-facing registration surface (portal/widget) plus operator-facing administration.
5. Money movement tied to enrollment (tuition/fees, payment plans, refunds) — present in every sampled product, though not required for free programs.
6. Enrollment-change machinery: waitlist, transfer, drop, makeup/trial.
7. Staff/instructor role with restricted visibility (rosters/attendance yes; payments no — explicit in CourseStorm, implicit in iClassPro staff permissions).

### What varies (candidate variant axes)

- Schedule philosophy: fixed sessions with re-enrollment (iClassPro Sessions) vs rolling/continuous enrollment (iClassPro Rolling Sessions) vs semester timeframes (Sawyer) vs catalog terms (CourseStorm).
- Care context: enrichment classes (no custody semantics) vs school-age care (sign-in/out, ratios, licensing — Procare segment).
- Object plurality: classes + camps + parties + appointments + POS under one roof (iClassPro) vs activity+schedule purity (Sawyer) vs registration-first simplicity (CourseStorm).
- Discovery model: operator-run registration only vs marketplace listing (Sawyer).
- Customer tier: single-site small business vs franchise/multi-site enterprise (Enterprise Portal) vs district/community-ed (CourseStorm; Eleyo unreachable).
- Content model: skill progression/evaluations (iClassPro skill tracking; Sawyer pass-fail/letter grades) vs none.

---

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (minimal)

The Type is recognizable only if all three hold:

1. **Operator program catalog** — the operator (a program organization, not the child's school of record) defines a catalog of scheduled offerings for children, each with schedule, capacity, and eligibility (age/grade).
2. **Guardian-initiated child enrollment** — participation is recorded as an enrollment binding a specific child, registered by a guardian, to a scheduled offering. The child is the participant; the guardian is the contracting/communication counterparty.
3. **Per-offering roster** — the operator works from rosters of enrolled children per offering/session; the roster is the operational basis for supervision and attendance.

Tests:
- Remove the catalog → generic CRM (no programs).
- Remove the child/guardian enrollment → generic event registration or adult course registration.
- Remove the roster → pure e-commerce booking with no operational supervision surface.
- Remove "children enrolled by guardians" → adult community education / continuing ed (a different audience, served by the same vendors but outside this leaf).

Historical/market-sample check: a 2000s district community-ed system (printed catalog digitized + registration + rosters), a YMCA program-registration system, and a single-site gymnastics gym system all satisfy these three structures without any modern SaaS specifics (marketplace, kiosk, branded app). The L0 does not overfit to the current market.

### L1 — Common Mature Structure (very common; not definitional)

- Family/guardian account: multiple children per account, primary vs secondary guardians, portal login, saved payment methods, communication opt-ins, policy/waiver acceptance.
- Session/semester/term containers with registration windows (incl. priority registration) and re-enrollment cycles; rolling-enrollment alternative.
- Attendance: staff-recorded attendance on rosters; kiosk/QR check-in; (care variants: sign-in/out with authorized-pickup semantics).
- Tuition billing: recurring charges by billing cycle (monthly/session/weekly), autopay with explicit recurring-billing authorization, discounts/promo codes, payment plans, refunds, ledger of charges and payments.
- Waitlists with automatic trigger at capacity and invite-to-register flow.
- Enrollment operations: transfer (incl. single-day/multi-day), drop with reasons, makeups, trials, drop-ins, punch passes.
- Staff/instructor records and an instructor-facing surface (rosters + attendance; payment data withheld); substitutes.
- Guardian communication: confirmations, announcements/email blasts, SMS, templates.
- Reporting/dashboards: enrollment, revenue, retention.
- Locations (multi-site) and, at scale, enterprise oversight portals.

### L2 — Variant / Optional Structure

- Care-context overlay for school-age care: sign-in/out custody rules, authorized pickups, room/ratio tracking, licensing compliance, daily activity reports (childcare-adjacent; Procare segment).
- Skill progression: disciplines/levels/evaluations/certificates (sports/swim/martial-arts segments); optional grades/assessments on listings (Sawyer).
- Sibling object types inside one product: camps, one-off events, parties, private-lesson appointments, POS merchandise, punch passes/memberships.
- Marketplace discovery: provider listings on a parent-facing marketplace (Sawyer); widget embedding as the registration surface.
- Online/virtual activities; pod learning.
- Subsidy/agency payments, dependent-care tax statements (district/care segments; not directly verified in this sample — inferred from segment, treat as unverified).
- District/community-ed specifics: school-year calendar alignment, free/subsidized offerings, facility-use programs (Eleyo unreachable; partially evidenced by CourseStorm's community-ed positioning).
- Deployment/positional variants: standalone operator platform vs module of a childcare suite vs registration-first SaaS.

### L3 — Vendor-specific (research notes only)

- iClassPro: Autopilot workflow chain (tuition charges → apply credits → capture payments), Makeup Tokens, Anniversary Charges, Pro Insights metric definitions (family tenure, net family gain), Messenger Center, Alerts Hub, iCampPro sibling product, Gymnastics Australia club import report.
- Sawyer: Sawyerspeak terminology, widget tags, rush registration, dynamic location capacity, Waitlist 2.0, custom branded app, marketplace provider pages.
- CourseStorm: "Just Ask" AI reporting assistant, abandoned-cart emails, low-enrollment alerts, donor/CRM integrations, ROI calculator.
- Jackrabbit: vertical editions (Class/Dance/Swim/Cheer/Music), benchmark reports.
- Procare: RoomRunner (AI-assisted enrollment planning), ChildPlus (Head Start), ratio dashboards.

---

## Vendor-specific Findings

See L3 above. None of these are promoted to the canonical model. The strongest candidate for accidental over-generalization was the **session-based schedule**: iClassPro's Sessions auto-drop enrollments at session end, but iClassPro itself ships the Rolling-Session alternative, and Sawyer uses Semester timeframes — so "fixed sessions with forced re-enrollment" is a common implementation, not an invariant.

## Boundary Findings

1. **vs Childcare Management System / Daycare-Preschool Management (§29 siblings)**: the two Types share the entire spine (family/child records, enrollment, attendance, billing, guardian app). The difference is care context and schedule shape: full-day, licensed, room/ratio-organized care with daily reports vs scheduled part-day programs (classes/sessions) around the school day. Vendors span both (Procare sells one suite into both segments; iClassPro/Sawyer/CourseStorm do not carry the care overlay). Structural test: remove rooms/ratios/licensing/daily-reports and keep scheduled session programs → after-school program management; remove scheduled sessions and keep full-day rooms → childcare management. Boundary is a gradient on the care overlay, not a wall. Flag for joint review when Childcare Management System and Daycare / Preschool Management are processed.
2. **vs Camp Management System (§29 sibling)**: same spine; difference is schedule shape and season (consecutive-day seasonal sessions, often overnight, bunks/cabins) vs recurring weekly school-year programs. Direct evidence that vendors treat them as sibling object types inside one product: iClassPro has separate Class and Camp sections; Sawyer's Schedule types are Semester vs Camp/Event; CourseStorm's tagline is "class & camp registration". This supports treating Camp Management as a related Type sharing the core, not a duplicate.
3. **vs Course Registration System (§23 sibling)**: registration-first products (CourseStorm) serve both adult community education and kids programs; the registration transaction is the center there, while this leaf centers the ongoing child-program relationship (rosters, attendance, supervision, guardian account). Overlap is real: a CourseStorm deployment for a kids' program arguably satisfies this leaf's core. Flag for joint review when Course Registration System is processed.
4. **vs Event Registration Platform**: one-off events lack the recurring program, the ongoing guardian relationship, and roster-based supervision. After-school products include one-off events/camps as optional object types (Sawyer Camps/Events; iClassPro events/parties), which is L2, not the core.
5. **vs Tutoring Platform**: instruction delivery/tutor matching is primary there; here the operator administers programs (tutoring may be one program's content). Sawyer's provider definition explicitly includes "a private tutor" as one operator type — evidence that the same management structure serves solo tutors, but the tutoring-platform Type centers the learning delivery, not program administration.
6. **vs Student Information System (§23)**: the school of record keeps enrollment/grades/transcripts for schooling; this Type's operator is not the school of record (Sawyer's optional pass/fail/letter-grades field is an L2 nicety, not a transcript system).
7. **Market terminology**: in the youth-activity-business segment this Type is marketed as "class management software" (Jackrabbit, iClassPro). No separate "Class Management" leaf exists in the directory for youth activities, so no conflict — recorded as terminology observation.

## Uncertainties

- **District/school-age-care segment depth**: Eleyo (the leading district community-ed/school-age-care platform per market presence) could not be fetched. Claims about district-specific structures (subsidy/agency payments, school-year alignment, facility use) are only partially evidenced (CourseStorm community-ed positioning; Procare segment page) and are marked as such.
- **Jackrabbit operational behavior**: help center unreachable; all Jackrabbit statements are positioning-level.
- **Attendance depth in care variants**: sign-in/out custody semantics (authorized pickup) are standard in the childcare family but were not directly verified in the fetched pages of this sample (iClassPro kiosk/QR check-in verified; pickup authorization not). Kept qualified in the final document.
- **Free-program billing**: all sampled products are payment-centric; whether a purely free district program deployment drops billing entirely was not directly observed. Billing is therefore kept out of the defining core.
- **Geographic scope**: the sample is heavily North American. Regional products (e.g., UK/EU out-of-school clubs, Japanese gakudo systems) were not sampled; the L0 was deliberately kept implementation-neutral to accommodate them, but their specific regulatory overlays are unverified.

## Final Synthesis

After-school Program Management is operator-side software for organizations that run scheduled out-of-school-time programs for children. Its defining structure is small: an operator-defined catalog of scheduled children's programs; guardian-initiated enrollment binding a specific child to a scheduled offering; and per-offering rosters the operator works from. Around that core, mature products add the family/guardian account, session/semester scheduling with registration windows, attendance/check-in, tuition billing and payment machinery, waitlists and enrollment changes, instructor-facing surfaces, guardian communication, and reporting. The Type shares its spine with childcare/daycare management and camp management — the boundaries are care context (full-day licensed care vs scheduled part-day programs) and schedule shape (recurring school-year programs vs seasonal camp sessions) — and vendors themselves ship these as sibling object types or sibling segments of single product lines.
