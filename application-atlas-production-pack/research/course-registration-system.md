# Research Notes — Course Registration System

Research date: 2026-09-07
Slug: course-registration-system (DIRECTORY §23 Education, Research & Knowledge Institutions)

## Research Goal

Understand what a Course Registration System is from real products: what objects exist inside it, who operates it, how a student gets from "interested in a course" to "enrolled", what rules gate that transaction, how the registration is maintained across the term, and where the boundary lies against neighboring Types (SIS, Academic Timetabling, Curriculum Management, Academic Advising, After-school Program Management, Event Registration Platform, LMS).

## Initial Boundary (hypothesis before research)

- Core use: the student-side enrollment transaction — students select course offerings/sections from a published catalog and the system validates and records the enrollment.
- Primary users: students (self-service), registrar/registration staff (administration), advisors (approval), instructors (roster consumers).
- Nearest neighbors: SIS (system of record; registration often a module), Academic Timetabling (supply-side construction), Curriculum Management (catalog structure), Academic Advising (plan/approve), After-school Program Management (kids-program operation), Event Registration Platform (one-off events), LMS (learning delivery).
- Unknowns: module-vs-standalone packaging; waitlist mechanics variance; consent/approval models; continuing-ed vs higher-ed structural differences; payment posture.

## Research Questions

1. What are the core objects (course, section, term/session, registration/enrollment record, cart/plan, waitlist)?
2. What is the registration workflow (browse → plan/request → register → validate → enrolled → add/drop → withdraw)?
3. What rules gate registration (capacity, restrictions, conflicts, holds, approvals, credit limits)?
4. What states does a registration pass through?
5. What interfaces exist (student portal, cart/planner, admin console, advisor surface, instructor roster)?
6. How does data flow to/from SIS / curriculum / timetabling / advising / payment?
7. What variants exist (higher-ed vs continuing-ed vs community-ed; self-serve vs batch; waitlist; consent)?
8. Where is the boundary vs SIS, timetabling, advising, after-school/camp, event registration?

## Representative Products

| Product | Segment | Philosophy | Why selected |
|---|---|---|---|
| Workday Student | Higher-ed enterprise SIS (cloud) | modern cloud suite; registration inside Student Records | Tier-1 product page with explicit registration features (appointments, reserve capacity, waitlists, eligibility preview) |
| UniTime | Higher-ed open source (Apereo) | solver-first sectioning satellite of timetabling; SIS remains system of record | deepest official documentation (Student Scheduling Manual); defines the demand-side machinery and its SIS boundary |
| CourseStorm | Community ed / arts / kids / workforce (standalone) | registration-first, "impossibly simple", consumer-grade checkout | the standalone pole; proves the Type exists outside the SIS; serves the after-school overlap zone |
| Ellucian (Student / Anthology Student) | Higher-ed enterprise SIS (dominant market share) | suite SIS; registration as core module | market-weight anchor; positioning-level evidence only (docs gated) |

Coverage: enterprise vs mid-market vs standalone vs open-source; degree vs non-degree education; self-serve vs batch; US-centric sample.

## Sources

- Workday — Student Management overview https://www.workday.com/en-us/products/student/overview.html (fetched 2026-09-07)
- Workday — Student Records (Student Academic Records System) https://www.workday.com/en-us/products/student/student-records.html (fetched 2026-09-07)
- UniTime — Student Scheduling Manual https://help.unitime.org/manuals/student-scheduling (fetched 2026-09-07)
- CourseStorm — homepage https://coursestorm.com/ (fetched 2026-09-07)
- CourseStorm — Registration Features https://coursestorm.com/registration-features (fetched 2026-09-07)
- CourseStorm — Class Management Features https://coursestorm.com/class-management-features (fetched 2026-09-07)
- Ellucian — homepage https://www.ellucian.com/ (fetched 2026-09-07)
- Ellucian — Student Information Systems https://www.ellucian.com/products/student/student-information-systems (fetched 2026-09-07)
- Ellucian — Ellucian Student https://www.ellucian.com/products/student (fetched 2026-09-07)
- Anthology — product redirect page https://www.anthology.com/ (fetched 2026-09-07; Anthology Student SIS/ERP now sold by Ellucian)
- Anthology Student Documentation Suite index https://help.anthology.com/Content/DocSets/CNSDocSet.htm (fetched 2026-09-07)

### Source-access Limitations

- Populi (populi.com, support.populiweb.com): timeout + transport errors on 2026-09-07 → abandoned after 2 failures; mid-market SIS pole evidenced only structurally.
- Anthology Student end-user help tiles (help.anthology.com/CNS/...): 403 on content pages → module index observed, operational detail not verified.
- Oracle PeopleSoft Campus Solutions docs: docs.oracle.com paths 404 → abandoned.
- Ellucian operational documentation (Banner/Colleague registration manuals) not reachable from public site → Ellucian evidence is positioning-level (Tier 2); no operational claims based on Ellucian internals.
- No precise numeric limits, default settings, or deadline semantics are asserted in the final document beyond what fetched sources state.

## Product A — Workday Student (evidence layer A: direct, product-page level)

Positioning: "Student records built for students and admins alike. Curriculum, registration, academics, student info—it's a lot to manage. Workday brings it all together."

Student Records key capabilities (official list): course catalog and scheduling management; registration prep and analytics; leave of absence questionnaires; grading and GPA calculations; transfer credit; full-lifecycle engagement plans; AI-generated prompt recommendations.

Registration-specific statements (official):

- "Set up registration appointments, define reserve capacity, and set wait-listing policies to match how your institution works."
- "Let students see if they're eligible for a course ahead of time so they can register smoothly. And troubleshoot quickly when problems arise."
- "Students can plan and save schedules before registration. Registering takes just a few clicks, whether from a saved schedule or their academic planner."
- "Give students the good news and let them know they're off the wait-list with a push notification. Then allow them to register on the spot."
- Curriculum management: concurrent academic lifecycles, stackable credentials, program-of-study relationships; academic planner; "total visibility into the academic planner so you can understand course demand and plan faculty staffing accordingly."

Interpretation: registration is a named capability inside the SIS's Student Records pillar; the registrar configures appointments/reserve capacity/waitlist policies; students plan → save → register; eligibility is previewed before registration; waitlist release is student-notified (not auto-enrolled).

## Product B — UniTime (evidence layer A: direct, manual-level)

Official definition: "Student scheduling, sometimes called *student sectioning*, involves assigning students to classes (course sections) based on their individual course demands… modeled as an assignment of student course requests with enrollments, i.e., valid combinations of classes that the student needs to take to enroll in a course."

### Object model (manual)

- **Course structure**: course → configurations (e.g., face-to-face vs online) → scheduling subparts (lecture/lab) → classes (sections); student requesting a course gets one class of each subpart of a single configuration; parent-child relations between classes; each class has a limit.
- **Reservations**: reserve a number of seats in a course/component for a particular student group (e.g., by study program). **Restrictions**: no space reserved, but students must follow them (e.g., online-program students restricted to the online configuration).
- **Course requests**: ordered by priority; alternatives per course; substitute courses (can substitute any request except No-Sub-marked ones); free-time requirements (act as unavailability or soft preference depending on position); class/instructional-method preferences (optionally required).
- **Priorities**: advisor-marked **vital** courses; student priority groups (Priority/Senior/Junior/Sophomore/Freshmen/Normal); students near graduation (100+ credits) and seniors (60+ credits) named in the manual as priority tiers.
- **Consent**: "Enrollment Approval — Consent has been approved or denied" notification; Online Scheduling Dashboard roles include "scheduling deputies (can approve consent)" and "course coordinators (can approve consent of the instructor)".

### Workflow (manual)

- **Batch mode**: pre-registration via Student Course Requests page (or XML import) → Student Scheduling Solver computes schedules for all students simultaneously (optimization: maximize assigned requests under hard constraints — class/configuration/course limits, time conflicts, reservations, linked sections; weights for priority, distance, section balancing, MPP change-minimization) → published runs → dashboards/reports.
- **Online mode**: Student Scheduling Assistant — students build/modify their schedule; dedicated online scheduling server "allowing for prompt responses even when the Student Scheduling Assistant page is used by hundreds of students at the same time."
- **Advisor Course Recommendations**: advisors provide course lists, change student status; PDF generated for signature; audit record kept ("what students requested versus what they have been advised").
- **Access control**: Student role needs "Student Scheduling Can Register" permission; student statuses must allow Registration/Assistant/Student Enroll; statuses can open/close wait-listing and re-scheduling by date window with fallback statuses; course types and departments can be excluded from student selection; Student Scheduling Rules adjust availability.
- **Custom validation**: CourseRequestsValidationProvider "checking a student's eligibility to submit their course requests… used at Purdue University to check the student's ability to register for the selected courses and to request overrides for any potential registration errors."
- **Wait-listing**: per-course toggle (Enabled / Re-Scheduling Enabled / Disabled; default Disabled); wait-list position visible to students; ordering by vital-first → student priority → first-choice-before-alternatives → timestamp (customizable); wait-list for a swap or a different section; alternatives auto-enrolled if space opens first; automatic enrollment when a class is added or a limit increases.
- **Re-scheduling**: students auto-moved when their class is cancelled, when a time conflict becomes disallowed, or when enrollment becomes invalid; students **not** moved when limits decrease; dropped students wait-listed with the original enrollment timestamp (order preserved).
- **Notifications**: student/admin request & enrollment changes, enrollment approval (consent), course schedule changes, waitlist/re-scheduling-driven enrollment changes, failed/external enrollment changes; instructor notifications configurable.
- **SIS boundary (explicit)**: "Students cannot be entered directly in UniTime; the expectation is that they will be imported from an external Student Information System" (Students XML / Student Course Requests XML); integration providers exist for "student eligibility checking and enrollment changes" (StudentEnrollmentProvider) and "approval workflow for various registration errors" (SpecialRegistrationProvider). Student scheduling "requires that the course timetabling be already completed with the course timetabling solution(s) saved and committed."

Interpretation: UniTime implements the full demand-side registration machinery (requests → validation → enrollment → waitlist → change) as a satellite of timetabling, with the student record and eligibility authority deliberately left to the SIS. This is the strongest available proof that the enrollment transaction is separable from the student-record system.

## Product C — CourseStorm (evidence layer A: direct, product-page level)

Positioning: "Impossibly simple class registration software" for arts & culture, community education, kids activities & camps, continuing ed & workforce training. "550+ organizations."

Registration features (official):

- Catalog: "Create or duplicate catalogs and launch classes in just a few steps"; **Sessions** ("a single class with shared info but distinct schedules"); "Embed your classes directly into your site with our customizable widget or use our out-of-the-box catalog site"; membership purchase alongside classes.
- Data collection: custom registration forms per class/camp; private (encrypted, admin-only) questions; **age restrictions** "to make sure the right age groups register for the right offerings."
- Demand control: **Registration launch control** ("post class or camp details before you open registration"); **flash sale protection** for catalogs that "sell out in minutes."
- Signup experience: mobile-friendly, no app; **friends & family registration** ("sign multiple people up for multiple classes in a single transaction"); **auto waitlists** and **payment plans**; abandoned-cart emails.
- Class management: dynamic rosters with payment status; transfer a student; issue a refund; message individual students or a full roster; **waitlists trigger automatically when a class reaches its cap**; "Send a registration invite link to the top person on your waiting list with a single click."
- Instructor portal: rosters, attendance from phones, roster messaging; "They cannot see or control payment status; that information is for admins only."
- Growth/marketing: personalized class recommendations, low-enrollment alerts, "Just Ask" AI reporting assistant.
- Integrations: embeddable catalog widget, registration data into CRM, API; ticketing and donor-management platforms named.

Interpretation: the standalone pole. The enrollment transaction is the product's center; class management (rosters, attendance) exists but is lightweight; payment is integral to the transaction (checkout semantics, refunds, payment plans); no academic structure (no credit, no prerequisites, no degree context).

## Product D — Ellucian / Anthology Student (evidence layer A for positioning; layer B only)

- Ellucian Student: "higher ed's complete solution that powers the end-to-end student lifecycle"; "trusted by over 1,400 institutions"; modules: Recruiting & Admissions, Student Aid, Curriculum, Student Success, Lifelong Learning, Advancement. Curriculum module: "Public Catalog — enable open browsing of course offerings for prospective students"; AI rule builder for degree curriculum rules; workflow-controlled curriculum governance.
- SIS page: "485% decrease in student registration processing time" (customer claim, marketing).
- Anthology Student (now Ellucian): documentation suite modules include Academic Records, Admissions, Financial Aid, Student Accounts, Student Experience, Student Services — registration lives under Academic Records (module index observed; content pages 403-gated).
- Interpretation: the dominant market packaging is registration-as-SIS-module. No operational registration detail asserted from Ellucian sources.

## Cross-product Comparison

| Dimension | Workday Student | UniTime | CourseStorm | Ellucian/Anthology |
|---|---|---|---|---|
| Packaging | SIS module (Student Records) | standalone sectioning satellite of timetabling | standalone registration-first product | SIS module (Academic Records) |
| Segment | higher-ed enterprise | higher-ed (research universities) | community ed / arts / kids / workforce | higher-ed enterprise |
| Offering structure | course catalog + scheduling | course → configurations → subparts → classes with limits | classes/camps with sessions; catalogs | course catalog (module index) |
| Catalog ownership | in-suite (curriculum management) | imported from timetabling side; SIS supplies students | built in-product; embeddable widget | in-suite |
| Registration mode | self-serve (plan → save → register) | batch solver + online assistant | self-serve checkout | (not verified) |
| Time gating | registration appointments | status-based date windows | launch control (post-then-open) | (not verified) |
| Capacity | reserve capacity | class/configuration/course limits + reservations | class caps | (not verified) |
| Eligibility | preview eligibility ahead of time | restrictions + reservations + custom validation (Purdue overrides) | age restrictions | (not verified) |
| Waitlist | policies + push notification → student registers | full machinery (position, ordering, swap, auto-enroll; default off) | auto-trigger at cap → invite link to top | (not verified) |
| Approval | (advising capability separate) | advisor recommendations; consent approval (deputies/coordinators) | none observed | (not verified) |
| Payment | not presented at registration | not presented | integral (checkout, refunds, payment plans) | (not verified) |
| Rosters | (implied via faculty access) | instructor notifications; dashboards | dynamic rosters + instructor portal + attendance | (not verified) |
| Change management | troubleshoot problems quickly | re-scheduling rules; drops → waitlist with original timestamp | transfer/refund | (not verified) |
| System of record | registration inside student record system | enrollment held in UniTime; students imported from SIS | registration is the system of record for its segment | registration inside SIS |

### Stable commonalities (layer B, cross-product)

1. **Published offering catalog for a term/session** — all products present enrollable offerings (courses/sections/classes/camps) with schedule and capacity.
2. **Identified students** — enrollment binds to a specific student/person record.
3. **Validated enrollment transaction** — selection is checked against rules (capacity, eligibility restrictions, time conflicts) and granted or refused; all four products express this (Workday eligibility preview; UniTime restrictions/reservations/conflicts; CourseStorm age restrictions + caps; Ellucian registration processing as institutional function).
4. **Registration maintained over the term lifecycle** — changes (add/drop/transfer/swap), cancellations, and waitlist promotion all operate on the existing registration record.
5. **Student self-service surface** — all sampled products expose a student-facing registration experience (portal/planner/assistant/catalog).
6. **Registrar/admin configuration surface** — windows, caps, policies, and rules are configured by staff, not hard-coded.
7. **Waitlist/queue management** — present in all three products with operational detail (mechanism varies: auto-enroll vs invite vs notify).
8. **Notifications** — registration/enrollment changes are communicated (email/push).
9. **Roster output** — the enrollment record produces class rosters consumed by instructors/admins.
10. **Integration seams** — SIS (student data in, enrollment out), curriculum/catalog upstream, payment/billing, CRM/marketing (community-ed pole).

### Product-specific findings (layer A, single-product)

- Workday: registration appointments; reserve capacity; waitlist push notification with on-the-spot registration; leave-of-absence questionnaires; AI prompt recommendations.
- UniTime: batch solver with published runs; MPP re-solve; waitlist ordering rules and swap waitlists; re-scheduling semantics (moved on cancellation/conflict/invalidity, not on limit decrease; dropped students keep original waitlist timestamp); consent approval roles (deputies, course coordinators); students imported from SIS (never entered directly); online scheduling server for concurrency; Purdue-specific eligibility/override validation.
- CourseStorm: friends & family multi-person single-transaction registration; flash sale protection; launch control; abandoned-cart emails; payment plans; instructor portal without payment visibility; memberships; "Just Ask" AI reporting.
- Ellucian: Anthology Student acquisition (SIS/ERP business); DegreeWorks (degree audit) in Student Success; marketing claims (485% registration processing time, 1,400 institutions).

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the Type stops being recognizable:

1. **A published catalog of enrollable offerings for a term/session** — the supply side presented for selection (courses/sections/classes/camps with schedule and capacity). Ownership of the catalog is a variant; presentation for enrollment is not.
2. **Identified students as the enrolling parties** — every registration binds to a specific student identity.
3. **The enrollment record created by a rule-checked transaction** — the student's selection is validated against capacity and eligibility rules and either granted (seat recorded) or refused (with the reason); the resulting student × offering binding is the system's central record.
4. **Registration maintained through the term lifecycle** — the record can be changed or cancelled under controlled conditions (add/drop/transfer/withdraw; waitlist promotion), not frozen at first creation.

Test: remove the catalog → nothing to register for (a bare student database); remove student identity → anonymous sign-up sheet; remove validation → a form, not a registration system; remove the enrollment record → no system of record; remove lifecycle maintenance → a one-shot sign-up tool, not academic registration. All four are needed.

Deliberately NOT in L0: payment (community-ed checkout vs degree-billing linkage — variant), waitlists (common, default-off in one sampled product), advisor approval/consent (segment-dependent), prerequisites as a named rule type (the rule machinery is L0; specific rule vocabularies are L1/L2), self-service portals (batch/assisted registration still qualifies), cloud delivery, notifications, rosters.

### L1 — Common Mature Structure

- Registration time gating: appointments/windows/launch control (all sampled products express this)
- Capacity management: section caps, reserve capacity, seat reservations for groups
- Waitlists with position and promotion (mechanism varies: auto-enroll / invite / notify)
- Planning artifacts before registration: saved schedules, course requests/carts, wish lists
- Eligibility rules: restrictions on who may take an offering (program/level/cohort restrictions; age restrictions in the community-ed pole; prerequisites commonly in degree education)
- Approval/override machinery: advisor recommendations, consent approval, registration-error overrides
- Student self-service portal + registrar/admin console + monitoring dashboards
- Rosters and instructor-facing views; attendance in the community-ed pole
- Notifications of enrollment changes and schedule changes
- Integration: SIS exchange (students in, enrollments out), curriculum/catalog upstream, timetable supply-side input, payment/billing, CRM/marketing
- Reporting/analytics: registration prep, demand monitoring, enrollment counts

### L2 — Variant / Optional Structure

- Segment shape: degree-education registration (sections, credit, prerequisites, degree context) vs non-degree class registration (community ed/arts/kids/workforce; checkout semantics, custom forms, age limits)
- Packaging: SIS-embedded module vs standalone registration-first product vs open-source sectioning satellite attached to timetabling
- Registration mode: self-serve online vs batch/assisted (solver-computed schedules; historical phone/in-person registration)
- Consent posture: open enrollment vs advisor-gated vs instructor/course consent
- Payment posture: checkout-integrated (pay to enroll) vs billing-linked (enrollment feeds tuition billing) vs free
- Catalog ownership: built in-product vs imported from curriculum/timetabling
- Concurrency machinery for peak registration (dedicated servers, queue/flash-sale protection)
- Custom data collection at registration (forms, private questions)
- Academic policy depth: credit-load limits, repeat rules, holds (common in degree education; not directly evidenced in fetched sources — kept general)

### L3 — Vendor-specific (research notes only)

- UniTime: solver weight scheme (0.501^n priority weighting), MPP/Initial/Projection solver modes, published runs, WaitListComparatorProvider, `unitime.*` configuration properties, 15-minute inactivity default, lunch-break/travel-time/workday schedule-quality criteria, Purdue customizations.
- Workday: push-notification waitlist release, leave-of-absence questionnaires, AI-generated prompt recommendations, engagement plans.
- CourseStorm: "Just Ask" AI reporting, abandoned-cart emails, flash-sale protection, friends & family registration, memberships, 3–6 week implementation claim, "+18% first-year growth" claim.
- Ellucian: "485% decrease in registration processing time" and "1,400 institutions" claims; DegreeWorks; Higher-Ed Knowledge Graph AI framing; Anthology Student acquisition.

## Historical / Market-Sample Check

Would older, regional, or differently positioned products still fit the L0?

- Pre-digital practice: a published course offering list, students identified by registrar records, enrollment granted against capacity/eligibility rules, drop/add forms changing the record — all four L0 properties present without any software.
- 1980s–90s telephone/IVR and batch mainframe registration: same transaction (request → validation → enrollment record → add/drop), no web portal, no cart, no push notifications.
- Regional variants (e.g., European "inscription"/module enrollment, UK module selection): same structure with different vocabulary.

The L0 therefore survives the historical check; self-service portals, carts, waitlist notifications, integrated payments, and analytics are era/market additions (L1/L2), not definitional.

## Boundary Findings

1. **vs Student Information System / SIS (§23)**: the dominant higher-ed packaging is registration-as-SIS-module (Workday Student Records; Ellucian Student; Anthology Student Academic Records). But the Type is defined by the enrollment-transaction function, not packaging: UniTime proves the machinery runs as a satellite with students imported from the SIS and eligibility/enrollment delegated back via integration providers. Test: remove registration → the SIS remains a student-record system; remove student records → a registration system still functions (UniTime). Related, packaging-overlapping, not duplicates.
2. **vs Academic Timetabling (§23 sibling)**: registration captures student-side demand (who takes which sections); timetabling constructs institution-side supply (when/where sections meet). UniTime ships both and documents the dependency: student scheduling "requires that the course timetabling be already completed." Confirms the sibling pass's finding — related Types sharing a data flow, not duplicates. Flag discharged.
3. **vs Curriculum Management (§23 sibling)**: curriculum defines what courses/programs exist and their rules (catalog structure, program requirements); registration executes who takes what this term. Curriculum is an upstream input (Workday curriculum management feeds registration; Ellucian public catalog browsing). Capability/input relationship.
4. **vs Academic Advising Platform (§23 sibling)**: advising collaborates on plans and approves; registration executes the enrollment. UniTime's Advisor Course Recommendations pre-populate student requests but students still submit; Workday lists Advising as a separate capability. Confirms the advising pass's finding — registration remains a separate system of record. Flag discharged.
5. **vs After-school Program Management (§23 sibling)**: overlap confirmed at product level — registration-first products (CourseStorm) serve kids programs with the same catalog+registration+roster machinery. Distinguish by center of gravity: this leaf centers the enrollment transaction against a course catalog; that leaf centers the ongoing child-program relationship (attendance, supervision, guardian accounts, session operation). A CourseStorm kids-program deployment satisfies this leaf's core; whether it satisfies the after-school core depends on program-operation depth. Joint-review note recommended, not a merge.
6. **vs Event Registration Platform (§26)**: shared transaction machinery (catalog → register → pay → roster) but different object world: one-off events vs term-based academic offerings with sections, credit, prerequisites, and add/drop rules. CourseStorm's own customer quote ("the ticketing service for education… just never quite fits") marks the seam. The boundary blurs for non-degree education; kept as adjacent Types.
7. **vs LMS (§23 sibling)**: the enrollment record feeds LMS rosters; the LMS delivers learning and does not grant seats. Handoff relationship.
8. **Naming**: "Course Registration System" matches market usage (higher-ed "registration", community-ed "class registration software"). No alias problem.

## Uncertainties

- Populi and Anthology Student operational documentation inaccessible → the mid-market SIS pole is evidenced structurally (via UniTime's SIS-boundary documentation and Ellucian positioning), not directly.
- Prerequisite/co-requisite enforcement specifics were not directly observed in fetched sources (UniTime documents "restrictions"; Workday documents eligibility preview; the word "prerequisite" appears in the sample only in unrelated contexts) → the final document names prerequisites only as a hedged common example.
- Add/drop deadline semantics (census dates, withdrawal grading, tuition-refund interplay) not directly evidenced → kept general.
- K-12 course registration (scheduling modules of K-12 SIS) not researched; the sample covers higher-ed and community/continuing ed.
- Credit-load limits, registration holds (financial/advising), and repeat-course rules are common in degree education but were not directly evidenced in the fetched sample → kept general or omitted.
- Whether waitlist auto-enrollment or student-notified promotion is market-dominant: mechanisms differ across the sample (UniTime auto-enrolls; Workday notifies; CourseStorm invites) → treated as variant.

## Final Synthesis

A Course Registration System is the enrollment-transaction application for education: it presents a published catalog of enrollable offerings for a term, binds selections to identified students, validates each selection against capacity and eligibility rules at the moment of registration, records the resulting enrollment, and maintains that record through the term's add/drop/waitlist lifecycle under registrar-configured windows and policies. The market realizes the Type in three packagings — as a module inside higher-ed SIS platforms (dominant for degree education), as standalone registration-first products for community/continuing/kids education (checkout-centered), and as open-source sectioning satellites attached to timetabling systems (with the SIS retaining the student record). The defining core is deliberately minimal: catalog + identified students + validated enrollment record + lifecycle maintenance; everything else (windows, waitlists, approvals, payments, portals, analytics) is common mature structure or variant.
