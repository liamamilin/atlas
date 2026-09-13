# Research Notes — Gymnastics Club Management

Research date: **2026-09-10**

## Research Goal

Understand what software sits under the directory leaf "Gymnastics Club Management" (§28 Sports, Fitness & Recreation): what objects the system manages, what the gymnastics club's operating loop is, how the class-management family spine is realized for gymnastics, and where the boundary lies against the already-processed sibling leaves (Dance Studio Management, Martial Arts School Management, Swim School Management, Sports Academy Management, Sports Club Management, Recreation Center Management, Fitness Studio Management, Climbing Gym Management, Gym Management System).

Context entering this pass — explicit forward flags to discharge:

- The **swim-school-management pass** (2026-09-09) left a FORWARD FLAG: gymnastics predicted as "the last closest sibling (skill-tracking/meets signature) — document with the same spine-first discipline, check the time-structure seam, and check whether meet/competition machinery differs structurally from swim's makeup/evaluation emphasis."
- The **sports-club-management pass** (2026-09-09) left a flag: "club" word collision — gymnastics-club software predicted to belong to the children's class-management family (instruction business) while Sports Club Management is the member organization; the Thrive4 brand split was vendor-side corroboration; confirm at this pass.
- The **martial-arts-school-management pass** (2026-09-08) predicted swim + gymnastics as the closest siblings and required the time-structure seam check per vertical.
- The **dance-studio-management pass** (2026-09-07) recorded the vertical-family taxonomy flag (one product family realized per vertical); keep-both-with-seam has been ratified by the martial-arts and swim passes.
- The **climbing-gym-management pass** recorded the segment-sibling pattern (vertical leaves extend a shared business core with activity-specific structures).
- The **school-management-system pass** left a watch-item: commercial class businesses run without school-of-record semantics; boundary holds; watch for swim/gymnastics passes.

## Initial Boundary (hypothesis before research)

- Expected core users: club owner/manager, program coordinator, coaches/instructors, front desk; parents (guardians) as portal users; children/teens as the taught population.
- Expected core: the class-management family spine — gymnast records on family accounts, scheduled recurring class offerings, enrollment, tuition money loop.
- Expected gymnastics signature (per sibling predictions): skill tracking (skill charts per apparatus/level), level progression (e.g., national federation level schemes), and competitive-team machinery (pre-team → competitive teams; meets).
- Expected neighbors: Swim/Martial Arts/Dance siblings (same family), Gym Management System (facility-membership core), Recreation Center Management (facility-first), Sports Club Management (member organization), Sports Meet Management (meet/competition operations), Sports Registration Platform (one-shot transactions), Childcare Management, School Management / SIS.
- Open questions: is the time structure session-based (dance pole) or continuous monthly (martial-arts pole) or dual-mode (swim pole)? Is skill tracking definitional or a standard extension? Does meet/competition machinery exist as a first-class structure in club products, or does competition ride the class/event machinery? How strong is the association/governing-body linkage (club↔federation)?

## Research Questions

1. What is the population of record — gymnasts? family accounts? members? How are minors handled?
2. How are class offerings modeled — recreational classes, levels, team practices, private lessons, clinics, camps? What is the time structure?
3. How does enrollment work — self-service, approval modes, capacity, waitlists?
4. What is the money model — tuition, team fees, competition fees, memberships, punch passes? How does billing couple to enrollment?
5. How are skills, levels, evaluations, certificates, and progress reports modeled? Is skill tracking a first-class structure?
6. How is the competitive layer handled — team practices, meet entries, competition fees? Is meet machinery present in club products?
7. What attendance/check-in machinery exists?
8. What surfaces exist (admin, coach/staff, parent portal/app, kiosk)?
9. How much membership/facility machinery rides on the same system — core or pole-dependent?
10. Where does this Type end and the sibling verticals / Gym Management System / Recreation Center / Sports Meet Management / Sports Club Management begin?
11. Would an older/paper-era gymnastics club still fit the model?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers. Four reachable poles plus packaging evidence from a fifth vendor:

| Product | Pole | Why sampled |
|---|---|---|
| **iClassPro** | class-management family platform where gymnastics is the first-listed industry ("#1 Class Management Software for Gymnastics, Cheer, Dance and Swim Schools") | The children's-activity class pole; gymnastics-first positioning; deepest gymnastics-vertical documentation of the reachable sample; direct test of the family flag |
| **Uplifter** | gymnastics-specialist club platform (also sells an association/governing-body product line) | The purpose-built-for-gymnastics club pole; "designed specifically for how gymnastics clubs operate"; shows the club↔association packaging seam from one vendor |
| **Amilia** | municipal/community recreation platform (YMCA/JCC/parks & rec) with a dedicated Gymnastics industry page | The community-aquatics/rec pole: gymnastics as one program line of a multi-program operation; contrast for the pedagogy layer |
| **The Studio Director** | multi-industry studio generalist (dance first, gymnastics second-listed) | The multi-industry generalist pole; documents skill charts and competitions on its gymnastics page; shows the companion-product pattern for skill tracking |

Packaging evidence (layer A on the corporate site; vertical page unreachable): **Jackrabbit Technologies** — "Jackrabbit Class: Gymnastics Gym Management Software" listed as the first of five vertical editions (Class/Dance/Swim/Cheer/Music).

Rejected / unreachable (recorded as sourcing limitations):

- **Jackrabbit Class gymnastics page** (jackrabbitclass.com/gymnastics/) — HTTP 403 this pass; the same domain returned 403 in the dance and swim passes. The edition's existence is A-evidence (corporate product map); its gymnastics-specific capability depth could not be directly verified.
- **EZFacility** — 403 on all fetched paths in two prior passes (sports-facility, racquet-club); not retried per network rules.

## Sources

All fetched 2026-09-10. Official product pages (Tier 2); no help-center article bodies retrieved this pass.

- iClassPro — home: https://www.iclasspro.com/
- iClassPro — gymnastics vertical page: https://www.iclasspro.com/gymnastics-software-features
- Uplifter — home: https://uplifterinc.com/
- Uplifter — gymnastics club page: https://uplifterinc.com/gymnastics
- Amilia — home: https://www.amilia.com/
- Amilia — gymnastics industry page: https://www.amilia.com/industry/gymnastics-registration-software
- The Studio Director — home: https://www.thestudiodirector.com/
- The Studio Director — gymnastics page: https://www.thestudiodirector.com/gymnastics/
- Jackrabbit Technologies — corporate home (product map confirming Jackrabbit Class = gymnastics edition): https://jackrabbittech.com/

Prior-pass sources reused as layer B: research/sports-academy-management.md (iClassPro class-management operational page: monthly/session/rolling-session class models, auto-approve/request-only enrollment, priority registration, waitlists, trials, drop-ins, punch passes, blackout closures with prorated billing, makeup tokens), research/swim-school-management.md (iClassPro skill-tracking page: Skill Trees, real-time evaluation, certificates, progress reports; family spine synthesis), research/dance-studio-management.md, research/martial-arts-school-management.md, research/climbing-gym-management.md, research/sports-club-management.md (STATUS entries).

Evidence layers: **A** = directly observed on an official page of this product this pass; **B** = cross-product commonality (including prior-pass observations); **C** = canonical inference.

## Product Observations

### iClassPro (all observations layer A unless noted)

- Positioning: "The #1 Class Management Software for Gymnastics, Cheer, Dance and Swim Schools" — gymnastics listed first on the home page and in the industries nav. Gymnastics page: "The #1 Class Management Software for Gymnastics Clubs Worldwide"; "The #1 Gymnastics Software for Gymnastics clubs across the globe."
- Gymnastics scope named verbatim: "Manage recreational classes, gymnastics clinics, private lessons, group lessons, **competitive individual and team practices**, birthday parties, events, student and staff schedules, waivers, email, SMS, and more." Team practices are named as a managed offering alongside recreational classes.
- Office Portal: manage classes, billing, customer accounts from one centralized location; customizable dashboards, live calendar, reporting; Welcome Page metrics (new accounts, dropped enrollments, class transfers, new enrollments).
- Staff Portal: coaches/front desk "view planned student absences, record attendance, and track skill evaluations" on mobile; time clock with geolocation.
- Customer Portal + Branded App: families book "classes, clinics, team practices, private lessons, and more"; account management, payments, 24/7 ProShop, club news. Branded App plan-gated (one-time setup fee + monthly; pricing stated on page).
- **Skill Tracking** (gymnastics page): "Evaluate student skills in real-time, entering the new skill directly into the staff portal. Celebrate your athletes' accomplishments with custom certificates that offer easy layout options, branding capabilities, and automatic delivery." (Skill Trees with videos/images and parent-visible progress reports documented A-strength on the skill-tracking page in the swim pass — layer B here.)
- **Makeup Lessons** (gymnastics page): "Manage missed classes by offering makeup tokens. Choose to automate or manually track and allocate makeup classes for your gymnasts… Parents can schedule makeup classes at their convenience, reducing administrative costs and helping to improve athlete retention."
- Punch Passes: families purchase a set number of passes for classes or clinics; family or individual athlete passes.
- Appointments & Private Lessons: "private lessons, individual choreography sessions, small group lessons"; coach availability customization, automated reminders (plan-gated: Elite and higher).
- Events & Camps: "camps, open gyms, parents' night out, and other special events with online registration and enrollment."
- Party Booking Management: birthday parties with customizable packages and add-ons.
- Check-In Kiosk: gymnasts "check themselves in for class, clinics, practice, or appointments."
- Point of Sale / ProShop; Payment Processing; Autopilot Billing ("simplifies tuition billing from setup to payment"); Autopilot Workflows (email/SMS/push); QuickBooks on Autopilot; Pro Insights dashboards; Integrated Websites.
- Enrollment control (class-management page — layer B via sports-academy pass): class models "monthly, session, or rolling session classes. Bill hourly, flat rate, or by time slot"; request-only vs auto-approve enrollment; priority registration; prorated billing; trials; waitlists; drop-ins; blackout schedules with prorated billing.
- Industry anchoring: partner logos of **USA Gymnastics** (usagym.org), **Gymnastics Clubs Australia**, GAT (gymnastics association of Texas), The Summit education summit; testimonials from gymnastics club owners (WEN Gymnastics, Westside Gymnastics, All Around Gym, Flipside Gymnastics).
- Multi-location: FAQ confirms multi-location organizations; Enterprise Plan for 3+ locations. Four plans (Signature/Elite/Premium/Enterprise).

### Uplifter (all observations layer A)

- Positioning: "Connecting every level of sport. Whether you run a club or oversee an entire sport, Uplifter brings memberships, registrations, payments, events, and administration together in one connected platform." Two product lines: For Clubs and For Associations (NGBs/governing bodies — separate solution surface).
- Gymnastics club page: "Outgrown your current gymnastics software? Manage registrations, payments, scheduling, and communication in one platform designed specifically for gymnastics clubs." "Built for gymnastics — designed specifically for how gymnastics clubs operate, not generic software that needs workarounds."
- Workflows named for gymnastics clubs (numbered list): "01 **Track athlete skills and progression across levels**; 02 Manage payments and billing without extra tools; 03 See real-time performance and attendance data; 04 Run your entire club from one connected platform." Skill/progression tracking is the first-listed workflow.
- Portals: **Coach portal** ("manage attendance, schedules, and athlete progress without extra admin"); **Family & Athlete Portal** ("register, pay, and stay updated without contacting the office"); **Administrator Portal** ("oversee registrations, finances, and reporting from one place"); all on any device.
- "Volunteers and waitlists, handled automatically — spend less time coordinating volunteers and filling cancelled spots."
- Communication: automated reminders for registrations and payments, emergency alerts and real-time updates, targeted messages to specific groups or families, email and SMS in one system.
- Billing: "Automate billing and reduce missed or late fees"; white-glove migration of "data, members and history."
- Pricing: plans starting at $129/mo; "no per-athlete fees"; "unlimited athletes"; 30-day free trial.
- Scale: "From small programs to multi-location clubs." Stats (vendor-claimed): 2,500+ sports clubs, 200+ sports associations, millions of athletes; Gymnastics Ontario is a named customer (testimonial from its operations lead).
- Association line (context, not sampled in depth): "Gain full visibility over your members, with compliance and board-ready data built in" — the governing-body surface is a separate product line sold to the same sports.

### Amilia (all observations layer A)

- Positioning: recreation & membership platform ("Software that moves communities forward") for YMCA/JCC/parks & rec/community centers; dedicated Gymnastics industry page: "Leading Gymnastics Management Software… more than just online registration… powerful tools to help gymnastics clubs manage and grow."
- Gymnastics-page capability claims: **Online registration** ("Registration restrictions, Waitlists, **Mandatory Memberships**, Flexible Payment Options"); **flexible scheduling** ("different days of the week at different times, with different locations and staff requirements… custom schedules for all your classes and activities"); **athlete data** ("Collect and store all the information you need on your athletes… customizable forms and activity reporting").
- FAQ defines the category: "Gymnastics management software helps clubs manage various aspects of their operations, including registration, billing, scheduling, attendance tracking, and communication with clients and staff."
- No skill-tracking/level/certificate machinery visible on the gymnastics page — the community/municipal pole serves registration + scheduling + athlete data + money without the pedagogy layer.
- Platform (SmartRec): Membership CRM, Programs & Activities, Facilities, Reporting & Analytics, Accounting & Finance; capabilities: Online Registration, Multi-Location, Payments (recurring installments, payment recovery), Staff, Access Management, Forms, Attendance, Private Lessons, Calendar Management.
- Gymnastics customers: Kyle Shewfelt Gymnastics (Olympic gold medalist owner), Langley Gymnastics (case study). Industries list includes Gymnastics beside Cheerleading, Dance, Soccer, Swim School, Martial Arts — direct cross-vertical family packaging.
- Bilingual EN/FR (Montreal-based); platform stats (vendor-claimed, notes only): 8,200 locations, $1B+ annual transactions.

### The Studio Director (all observations layer A)

- Positioning: "Studio Management Software for Dance, Gymnastics, & More" — "Catered specifically to dance studios or gymnastics business!" Gymnastics is second-listed industry (dance first); industries list spans dance, cheerleading, fitness, gymnastics, martial arts, music, pilates, yoga, youth sports.
- Gymnastics page: "Gymnastics Class Management Software — manage gymnastics classes, registration, payments and more with one simple solution."
- Key features named for gymnastics: **Online Registration** ("register for classes, **competitions**, and events online"); **Integrated Payments**; **Class Management** ("Create and organize gymnastics schedules. Manage waitlists, **skill charts**, private lessons, track attendance, and more"); **Communications** (text/email, drip campaigns, parent portal).
- **Skill tracking via companion product**: partnership with **MySkillChart** — "Track student progress with customizable, skill-tracking software." The generalist product delivers the gymnastics skill layer through an integration, not a native module — the same companion-product pattern the climbing pass documented for routesetting.
- Other integrations: Google (register from search), Zapier.
- Home page features (shared platform): communication, virtual classrooms, events & recitals, payments (card/bank on file), online enrollment (parent portal: register, request trial or makeup class, purchase inventory), reporting, **costume management** (dance machinery on the same product), automatic prorating, tuition calculations, recurring card/e-check payments.
- Cross-vertical FAQ: "Can this gymnastics software help any class-based studio business? Yes! … martial arts centers, dance studios, cheerleading classes, music schools, and more."
- Gymnastics-adjacent customer: Great Lakes Kids Energy Zone (testimonial).

### Jackrabbit Technologies (packaging only — layer A)

- Corporate product map: "Jackrabbit Class — Gymnastics Gym Management Software" is the first of five vertical editions (Class/Dance/Swim/Cheer/Music); corporate home: "The #1 Cloud-Based Class Management Software for Youth Activity Centers — Gymnastics • Dance • Swim • Cheer • Music" (gymnastics first). Capability depth not verifiable (403).

## Cross-product Comparison

| Structure / capability | iClassPro (gym page) | Uplifter (gym page) | Amilia (gym page) | The Studio Director (gym page) | Layer |
|---|---|---|---|---|---|
| Gymnast/athlete records centralized (children; family context) | ✓ customer/student profiles; parent portal | ✓ athlete records; family & athlete portal | ✓ "all the information you need on your athletes" | ✓ student records | B |
| Family/guardian as paying unit (parents book and pay) | ✓ customer portal books & pays | ✓ family portal registers & pays | ✓ "families and athletes" register | ✓ parent portal enrolls & pays | B |
| Scheduled recurring class offerings (recreational classes) | ✓ recreational classes, group lessons, clinics | ✓ scheduling named; classes implied | ✓ custom schedules for classes/activities | ✓ gymnastics schedules | B |
| Classes organized around skill levels / progression | ✓ Skill Tracking + certificates (skill trees per swim pass, layer B) | ✓ "Track athlete skills and progression across levels" (first-listed workflow) | not visible on gym page | ✓ "skill charts" named; MySkillChart companion | A×3 (one via companion), absent at community pole |
| Enrollment with capacity/waitlists | ✓ waitlists, request/auto-approve modes (class page, layer B) | ✓ waitlists handled automatically | ✓ waitlists + registration restrictions | ✓ waitlists | B (strong) |
| Money loop: tuition/fees billed against enrollment | ✓ Autopilot Billing; billing from Office Portal | ✓ automated billing; payments | ✓ billing; flexible payment options; recurring installments (platform) | ✓ tuition calculations, recurring billing, prorating | B (strong) |
| Competitive team practices as managed offerings | ✓ "competitive individual and team practices" named; bookable in portal | not visible on page | not visible | not visible (competitions named instead) | A (single) |
| Competitions as registration events | not on page | not visible | not visible | ✓ "register for classes, competitions, and events online" | A (single) |
| Meet-entry / scoring machinery | not visible | not visible | not visible | not visible | — (none of the sampled public surfaces) |
| Makeup machinery | ✓ makeup tokens, auto or manual, parent self-scheduling | not visible on page | not visible on gym page | ✓ "request a trial or makeup class" (parent portal) | A×2 + family precedent |
| Attendance / check-in machinery | ✓ staff portal attendance; kiosk (class/clinic/practice/appointments) | ✓ coach portal attendance; real-time attendance data | ✓ attendance (platform capability) | ✓ attendance tracking | B (strong) |
| Private lessons | ✓ Appointments module (plan-gated) | not visible on page | ✓ Private Lessons (platform capability) | ✓ private lessons in class management | B |
| Memberships alongside classes | punch passes (prepaid attendance), not membership-led | memberships named in platform framing | ✓ "Mandatory Memberships" (community pole) | not on gym page | B (pole-dependent) |
| Waivers at registration | ✓ waivers | not visible on page | ✓ customizable forms (platform) | ✓ online documentation | B |
| Communication (email/SMS/push, automation) | ✓ Autopilot Workflows | ✓ email/SMS, automated reminders, emergency alerts, targeted messages | ✓ communication (platform) | ✓ text/email, drip campaigns | B (strong) |
| Events beyond classes (camps/parties/open gym) | ✓ camps, open gyms, parents' night out, parties | events named in platform framing | camps (platform) | events & recitals | B |
| Coach/staff portal | ✓ staff portal (attendance, evaluations, time clock) | ✓ coach portal (attendance, schedules, athlete progress) | ✓ staff (platform) | front-desk framing | B |
| Session container (fixed terms) | ✓ available ("monthly, session, or rolling session" — layer B) | not specified on page | ✓ sessions + recurring installments | tuition per term framing | B — dual-mode |
| Continuous monthly enrollment | ✓ "monthly" first-class (layer B) | automated recurring billing | ✓ recurring installments | recurring billing | B — dual-mode |
| Reporting (enrollment, retention, revenue) | ✓ Pro Insights; Welcome Page metrics | ✓ real-time performance data; reporting in admin portal | ✓ activity reporting; analytics (platform) | ✓ dashboard/detail/summary reports | B |
| POS/retail | ✓ ProShop / Point of Sale | not visible on page | not on gym page | ✓ purchase inventory in portal | B |
| Multi-location | ✓ Enterprise Plan 3+ locations | ✓ multi-location clubs named | ✓ multi-location (platform) | not on gym page | B |
| Association/governing-body linkage | — (industry association partnerships only) | ✓ separate NGB/association product line | — (YMCA/JCC are multi-program orgs) | — | A (single, packaging seam) |

Four structural notes from the comparison:

1. **The gymnastics signature layer is skill/level progression tracking — and it is the family's most consistently documented signature.** iClassPro (skill trees, real-time evaluation, certificates), Uplifter ("track athlete skills and progression across levels" as the first-listed club workflow), and The Studio Director ("skill charts" in class management; MySkillChart companion) all document it; Amilia's community pole does not show it — the same facility/community-pole absence the swim pass observed with Dash. Notably, The Studio Director delivers the skill layer through a companion product (MySkillChart) rather than a native module — the same pattern the climbing pass documented for routesetting walls. The signature is standard for the vertical, not present in every product that touches the market, and not definitional.
2. **Meet/competition machinery is NOT a first-class structure in the sampled club products' public surfaces.** The swim pass predicted a "skill-tracking/meets signature" for gymnastics. The research answer: competition appears in two forms — (a) competitive team practices as bookable class-like offerings (iClassPro), and (b) competitions as registration events (The Studio Director). No sampled product documents meet-entry, meet-hosting, or scoring workflows on its public pages. Full meet management/scoring sits in an adjacent market (parallel to swim-team management products), and the directory already has a separate Sports Meet Management leaf for that territory. This discharges the swim pass's structural question: meet machinery does not differ structurally from swim's makeup/evaluation emphasis because it is not part of the club-management core at all — the competitive layer rides the class and event machinery.
3. **Time structure is dual-mode in gymnastics, joining swim's camp.** iClassPro documents "monthly, session, or rolling session" class models as equal choices (layer B, A-strength source page); Amilia sells sessions with recurring installments; The Studio Director bills per term with recurring card/e-check. Gymnastics does not force either the dance pole (season/session container) or the martial-arts pole (continuous membership only). This discharges the martial-arts and swim passes' time-structure seam check for gymnastics: the seam exists inside gymnastics, not between gymnastics and the family.
4. **Membership machinery is pole-dependent, and the "club" word collision is confirmed.** Amilia's community pole sells "Mandatory Memberships" beside gymnastics classes; iClassPro reaches membership-like entitlements via punch passes; Uplifter names memberships in its platform framing. And the sports-club pass's flag is confirmed from this side: gymnastics-club software is an instruction business (recreational classes, skill progression, tuition) — the member-organization core (teams, seasons, volunteers, board) belongs to Sports Club Management. Uplifter is vendor-side corroboration: one company sells clubs a class/registration platform and sells associations/governing bodies a separate membership/compliance platform — the same brand-split pattern as Thrive4.

## Canonical Model

### Level 0 — Defining Invariant (minimal)

```text
Gymnast record (identified learner/athlete, commonly a minor,
        held on a family/guardian account)
└── Scheduled class offerings (the club's offer:
    recurring gymnastics classes — recreational programs
    organized by level/age — plus team practices and
    private lessons; placed on the calendar)
    └── Enrollment (persisted gymnast↔class registration
        under capacity/waitlist, forming the roster)
        └── Class money loop (enrollment-driven tuition/fees
            posted to the family account, settled by payment,
            arrears actionable)
```

Four jointly-held structures. Removal test:

- Remove the gymnast record → a contact/CRM database; nobody is being taught.
- Remove scheduled class offerings → a billing engine or a people database, not a club.
- Remove enrollment → a class directory or a sign-up form; no roster, no "who trains when".
- Remove the money loop → a roster app; the club stops being run as a business in the system.

Deliberately NOT in L0 (each fails the "would it still be the same Type" or the historical test):

- **Skill/level progression machinery** (skill charts/trees, evaluations, certificates, progress reports, level-up placement) — the gymnastics signature, documented by three of four sampled products (one via companion product), absent from the community pole's public surface, and satisfied by a paper-era club's paper skill chart. Standard, not definitional — same treatment as martial-arts ranks and swim levels.
- **Competitive team programs / competition machinery** — team practices ride the class machinery (iClassPro); competitions appear as registration events (The Studio Director); meet-entry/scoring workflows are absent from every sampled public surface and belong to the adjacent meet-management market. Standard/optional, not definitional.
- **Makeup machinery** — documented for the class-pole product (A, gymnastics page) plus family precedent (dance/swim); the core loop survives without it. Standard emphasis, not definitional.
- **Attendance/check-in, portals, communication, waivers, POS, private lessons, clinics, camps/parties/open gyms** — common mature structure across the family sample.
- **Memberships** — pole-dependent (community/municipal operators); not definitional.
- **Facility scheduling of the gym floor** — load-bearing for club-owned facilities but not the record here; the gymnastics-club record is the class business, not the building.
- **Session container OR continuous billing as the time structure** — both are first-class in the same products; the invariant is only that class offerings recur on a calendar and money follows enrollment.

Historical / market-sample check: a paper-era gymnastics club (registration card per child under the guardian's family file, a posted schedule of level classes, enrollment list per class, tuition collection, attendance roll, a paper skill chart per apparatus) satisfies every L0 element with zero software machinery. A single-site gym, a club renting gym time, a municipal rec-center gymnastics program, and a multi-location gymnastics chain all fit. L0 holds across eras and operator shapes.

### Level 1 — Common Mature Structure

- Enrollment machinery: online self-service registration by parents, capacity limits, waitlists, enrollment approval modes (request-approve vs auto-approve), trials, priority registration, prorated billing.
- Skill/level progression layer (the gymnastics signature): classes organized in progressive level/age schemes; per-gymnast skill records against the club's skill charts/trees (often per apparatus — floor, bars, beam, vault); coaches recording evaluations in real time from a coach/staff portal; progression outputs — certificates, parent-facing progress reports; evaluation data feeding placement in the next level. Sometimes delivered via a companion skill-tracking product.
- Makeup machinery: absence-recorded classes generate eligibility (tokens/credits) that parents redeem by booking into makeup-approved classes; automatic or manual allocation.
- Attendance/check-in: coach attendance from rosters; self-service check-in kiosks (class, clinic, practice, appointments).
- Money machinery: recurring billing/autopay on the family account, payment recovery, one-time charges, refunds; payment processing bundled or partnered; tuition calculations and prorating.
- Parent/family portal + mobile app: book classes and makeups, pay, view skills/progress, receive notifications.
- Coach/staff machinery: coach schedules, staff portal (rosters, attendance, evaluations), time clocks (sometimes geolocated).
- Communication: email/SMS/push announcements and automated workflows (enrollment confirmations, reminders, emergency alerts, cancellations).
- Private lessons: appointment-style booking against coach availability (sometimes plan-gated).
- Events beyond classes: camps, birthday parties, open gyms, parents' night out, clinics — with registration and payment.
- Waivers/medical-information collection at registration.
- Reporting: enrollment, retention, revenue, class-occupancy dashboards.
- Multi-location management for larger organizations.

### Level 2 — Variant / Optional Structure

- Operator shape: independent gymnastics club vs municipal/community program (gymnastics as one program line) vs club inside a multi-activity organization vs cheer/tumbling/ninja-adjacent facilities; the same family spine serves all, with membership machinery swelling at the community poles.
- Time structure: session-based enrollment (fixed terms) vs continuous monthly enrollment with autopay vs rolling sessions — dual-mode across and within products.
- Revenue mix: recreational tuition core vs competitive-team-led (team tuition, competition fees) vs camps/parties/open-gym secondary revenue; punch passes/prepaid attendance; drop-ins.
- Competitive bridge: pre-team/development groups and competitive teams riding the same class machinery; competitions as registration events; full meet management/scoring as an adjacent market (separate directory leaf exists).
- Association/governing-body linkage: club↔federation member registration and compliance flows as an integration edge (one sampled vendor sells a separate NGB product line); not part of the club Type's core.
- Curriculum source: club-defined skill charts vs national federation level schemes (e.g., US-, AU-, CA-context bodies appear as industry partners); degree of software support for specific schemes not directly verified — weak evidence, not asserted.
- Region: North America dominant in the sample, with Australian presence (industry association partners, vendor offices); bilingual operation (EN/FR) at the municipal pole.
- Scale: single location → multi-location; branded apps/integrated websites; plan/edition gating.

### Level 3 — Vendor-specific (research notes only)

- iClassPro: makeup-token mechanics; Skill Trees; Autopilot Billing/Workflows; QuickBooks on Autopilot; Pro Insights; Welcome Page metrics; iPartyPro party booking; ProShop; geolocated time clock; Branded App pricing (one-time setup fee + monthly, stated on page); four named plans (Signature/Elite/Premium/Enterprise; Enterprise for 3+ locations); USA Gymnastics / Gymnastics Clubs Australia / GAT / Summit partner roster; Inc. 5000 and "100 Million Class & Camp Registrations" claims; iCampPro sibling product.
- Uplifter: no-per-athlete pricing model; plans from $129/mo; 30-day free trial; white-glove migration; unlimited athletes; separate NGB/association product line ("compliance and board-ready data"); Gymnastics Ontario customer; 2,500+ clubs / 200+ associations claims; Capterra/GetApp ratings displayed.
- Amilia: SmartRec platform naming; "Mandatory Memberships" pattern; social-equity capability; EN/FR bilingual product; open API; 99.99% uptime claim; usage stats (8,200 locations, $1B+ annual transactions, 80% self-serve); Amilia University; Kyle Shewfelt Gymnastics and Langley Gymnastics customers; industries list spanning gymnastics/cheer/dance/swim/martial arts/soccer.
- The Studio Director: MySkillChart companion integration for skill tracking; costume management (dance machinery on the same product); recitals/events machinery; virtual classrooms; drip marketing; Google-search registration integration; Zapier; 2,000+ studios claim; Great Lakes Kids Energy Zone customer.
- Jackrabbit: five vertical editions (Class=gymnastics/Dance/Swim/Cheer/Music); 99.9% uptime guarantee; B-Corp; (gymnastics capability depth unreachable — 403).

## Rejected Findings

- **"Gymnastics club management = gym/fitness membership software with gymnastics branding"** — rejected as a definition. The sampled gymnastics products lead with the class-management spine (classes, enrollment, tuition, skill progression), not the facility-membership core (door entitlements, dues for access). The Gym Management System segment-sibling pattern applies: the gymnastics leaf is class-led, not door-led.
- **"Skill tracking is definitional"** — rejected: absent from the community pole's public capability surface, satisfied by paper skill charts historically, and delivered by a companion product in one sample; same treatment as martial-arts ranks and swim levels (signature standard extension).
- **"Meet/competition management is part of the club Type"** — rejected on the sampled evidence: no product documents meet-entry/scoring on public surfaces; competition rides class machinery (team practices) and event registration. Full meet operations are adjacent-market territory with a dedicated directory leaf (Sports Meet Management).
- **"Session/term container is definitional"** (dance pattern) — rejected: monthly/rolling models are first-class in the same products.
- **"Continuous membership is the time structure"** (martial-arts pattern) — equally rejected: sessions are first-class.
- **"Family account is definitional"** — rejected per family precedent: the invariant is the gymnast record; family/guardian grouping is the dominant implementation for a minor-dominated market.
- **"Memberships are part of the gymnastics-club Type"** — rejected: membership machinery is how community/municipal operators bundle gymnastics with other programs, not what makes the system a gymnastics-club system.
- **"Gymnastics club software = sports club software"** — rejected (word collision): the instruction business vs the member organization; vendor brand splits corroborate.
- **"Precise parameters (token expiry, billing cycles, level counts, class ratios, coach-certification rules)"** — rejected to notes: no help-center evidence retrieved; nothing asserted.

## Boundary Findings

- **vs Swim School / Martial Arts School / Dance Studio / Sports Academy Management (processed siblings, same family)**: identical spine (student/athlete records on family accounts, scheduled recurring offerings, enrollment, tuition loop, attendance, portals). Signatures: dance = season/session + performance machinery (costumes/recitals/competition); martial arts = rank/testing/promotion layer + continuous memberships + strong lead funnels; sports academy = program portfolio (lessons/camps/teams) over an athlete population; swim = level/skill progression with evaluations/certificates + first-class makeup machinery; **gymnastics = skill/level progression tracking (skill charts, often per apparatus) with competitive team programs riding the class machinery**. Removal test: strip gymnastics' skill-chart emphasis and add recital machinery → dance; add ranks/testing and continuous-only → martial arts; add makeup-first emphasis → swim. Keep-both posture ratified; this pass discharges the swim pass's forward flag (gymnastics confirmed as the closest sibling; the predicted "meets" half of the signature is NOT a first-class club structure — competition rides class/event machinery) and the time-structure seam check (gymnastics is dual-mode, joining swim's camp).
- **vs Sports Club Management (processed sibling) — "club" word collision DISCHARGED**: gymnastics-club software belongs to the children's class-management family (instruction business: recreational classes, skill progression, tuition); the sports club here is a member organization (teams, seasons, volunteers, board governance). Vendor-side corroboration: Uplifter sells clubs a class/registration platform and associations/governing bodies a separate membership/compliance platform — the same brand-split pattern as Thrive4 (Grassroots vs Activities). The seam is the center of gravity: instruction/tuition-led vs membership/competition-led.
- **vs Gym Management System (processed sibling, segment pattern)**: the gym core is facility-membership-led (member of record, standing entitlement, door check-in, dues); the gymnastics club is class-enrollment-led (student records, scheduled classes, rosters, tuition). A generic gym product can run a gymnastics facility's memberships, but the sampled gymnastics products center the class business. Segment-sibling relationship consistent with the climbing pass's pattern.
- **vs Recreation Center Management (processed sibling)**: recreation centers hold the facility-operations core with gymnastics as one program line; the gymnastics-club Type centers the instruction business itself. The same products (Amilia) serve both sides — the seam is the center of gravity, as the swim pass found with aquatics.
- **vs Sports Meet Management (directory sibling)**: meet/competition operations (entries, sessions, scoring, results) are a separate Type; the gymnastics club's competition activity touches it only at the edges (team practices, competition registration events). No sampled club product centers meet machinery.
- **vs Sports Registration Platform**: one-shot registration transactions vs the ongoing class relationship (roster, recurring tuition, progression, portal).
- **vs School Management System / SIS**: commercial instruction business vs educational institution records — no grade levels, no official academic transcript, no institutional enrollment statuses (family precedent; watch-item discharged).
- **vs Childcare Management System**: care context (rooms, ratios, custody check-in/out) vs scheduled classes.
- **vs Membership Management System / Membership Billing**: generic dues/lifecycle engine; the gymnastics Type instantiates dues against a level-organized class schedule.
- **vs Climbing Gym Management (processed sibling)**: climbing's identity rests on waiver-gated participation, certification flags at entry, and the perishable wall inventory over a facility-membership core; gymnastics' identity rests on skill/level progression over a class-enrollment core. Different cores despite both being "gyms."
- **Family taxonomy note (reconfirmed, fourth vertical)**: the gymnastics pass adds a fourth independent confirmation of the vertical-family structure (iClassPro sells the same platform to gymnastics/cheer/dance/swim with gymnastics first; Jackrabbit sells a dedicated gymnastics edition beside Dance/Swim/Cheer/Music; Amilia lists Gymnastics beside Swim/Martial Arts/Dance/Cheer industries; The Studio Director lists gymnastics beside dance/cheer/martial arts and states its software serves any class-based studio business). Whether the directory wants per-vertical leaves is a taxonomy question for joint review; this pass keeps the leaf as the gymnastics realization, spine-first.

## Uncertainties

- **Jackrabbit Class gymnastics depth unverified**: the edition's existence is A-evidence (corporate product map); its gymnastics-specific capability set could not be fetched (403 this pass and in prior passes). No capability attributed to Jackrabbit Class.
- **Meet/competition machinery depth**: the finding "meet machinery is not a first-class club structure" rests on the sampled products' public pages; deeper product capability (e.g., meet-entry modules behind login) was not verifiable. The pass asserts only what the public surfaces show and marks the adjacent-market disposition accordingly.
- **Skill charts as a distinct data object**: "skill charts" is named verbatim by one product; skill trees/progression by two others; the implementation shape (per-apparatus charts, level hierarchies) is strongly implied by the gymnastics context but was not verified as a distinct object in every product. The final document phrases this conceptually.
- **Makeup machinery evidence**: A-strength for one product this pass (iClassPro, gymnastics page) plus one generalist's parent-portal makeup requests (The Studio Director) plus family precedent; not claimed as universal.
- **Payment-state gating at check-in** (documented for martial arts) was not observed for gymnastics products this pass; not claimed.
- No vendor help-center article bodies retrieved; no precise operational parameters asserted anywhere.
- Uplifter's association/NGB product line was observed only at packaging level; its internal structure belongs to the Sports Club/Federation territory and was not sampled.
- Coach-certification tracking (observed for swim at Amilia) was not observed on the gymnastics pages; not claimed.

## Final Synthesis

A Gymnastics Club Management application is the operator-side business system for running a gymnastics club (a gymnastics instruction business). Its defining core is four jointly-held structures: **gymnast records** (identified learners/athletes, commonly minors, held on family/guardian accounts), **scheduled class offerings** (recurring gymnastics classes — recreational programs organized by level/age — plus team practices and private lessons, placed on the calendar), **enrollment** (persisted gymnast↔class registrations under capacity/waitlist, forming rosters), and the **class money loop** (enrollment-driven tuition and fees posted to the family account and settled by payment). Around that core, mature products add the gymnastics signature layer — **skill/level progression tracking** (skill charts, often per apparatus, with coach-recorded evaluations, certificates, parent-visible progress reports, and level-up placement; sometimes delivered via a companion skill-tracking product) and a **competitive layer that rides the class machinery** (pre-team/development and competitive team practices as bookable offerings; competitions as registration events — while full meet management/scoring remains an adjacent market) — plus the family-wide operating machinery: attendance/check-in, parent and coach portals, recurring billing with recovery, makeup lessons, private lessons, communication automation, waivers, camps/parties/open gyms, and reporting. The Type's market straddles operator shapes: independent clubs run exactly this core; municipal/community organizations run it alongside memberships and other programs on the same platform; the time structure is dual-mode (continuous monthly enrollment and fixed sessions are both first-class in the same products), and the "club" in the name is the instruction business, not the member organization of the Sports Club Management Type.

Taxonomy disposition: keep the leaf as the gymnastics realization of the class-management family; keep-both-with-seam ratified against all processed siblings; swim pass forward flag discharged (gymnastics confirmed as the closest sibling; meets not a first-class club structure); sports-club pass "club" word-collision flag discharged (confirmed; Uplifter brand-split corroboration); time-structure seam check discharged (dual-mode, joining swim's camp); school-management watch-item discharged (no school-of-record semantics in the sampled surfaces).
