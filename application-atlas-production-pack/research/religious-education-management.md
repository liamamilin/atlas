# Research Notes — Religious Education Management

## Research Goal

Understand what "Religious Education Management" software actually is in the market: what objects and loops a congregation's religious education program (Sunday school, Catholic CCD / faith formation, synagogue religious school, madrasa-class programs) is run on in software, who operates it, how enrollment → class → attendance → milestone works, and how the Type differs from adjacent Types (ChMS, school management/SIS, LMS, ministry scheduling, childcare management, check-in systems, event management).

## Initial Boundary

Working hypothesis at start:

- The center is the **program administration loop** of a congregation's religious education program: students (children of member families) enrolled into classes, teachers (often volunteers) assigned, sessions held on a program-year calendar, attendance recorded, fees collected, milestones (sacraments / b'nei mitzvah) tracked, parents communicated with.
- Nearest confusions: Church Management System (is this just a module?), School Management / SIS (is this a school?), LMS / educational content (is this teaching content?), Ministry Scheduling (teacher volunteers), Childcare Management, children's check-in systems, Event Management (VBS).
- Key unknown: does a standalone product population exist, or is the Type realized only as a ChMS module? (The ChMS pass listed this leaf among "capability slices that exist both as ChMS modules and as standalone specialists".)

## Research Questions

1. What objects exist: student, family, class, teacher/catechist, session, term/program year, registration, fee, milestone/sacrament, attendance?
2. How does enrollment work (registration → class placement → roster)?
3. How does attendance work (per-session, against what structure)?
4. What is the family linkage (students as children of member families)?
5. What is the program-term structure and how does year-to-year rollover work?
6. What role do volunteers play as teachers/catechists?
7. What money machinery exists (fees, family caps, discounts, payment routing)?
8. What milestone machinery exists (sacramental prep, b'nei mitzvah, confirmation)?
9. Standalone vs module: do standalone products exist?
10. Boundary vs SIS/school management: what is absent (transcripts, state reporting, academic grading)?
11. Boundary vs LMS/content: is content delivery part of the center?
12. Boundary vs check-in: what separates program administration from children's check-in?

## Representative Products

| Product | Pole | Why sampled | Evidence tier |
|---|---|---|---|
| ParishSOFT (Faith Formation / Religious Education module) | Catholic parish ChMS with a dedicated religious-education module — the strongest named realization of the leaf | Vendor's own module is literally named "Religious Education" (legacy) / "Faith Formation" (new platform); fact sheet PDF named "Religious Education.pdf" | Tier 1 (Zendesk help-center articles fetched directly) + Tier 2 (product pages) |
| CatholicBrain | Catholic faith-formation **content/curriculum platform** with a class-management layer — the content pole | Self-labels "A Premier Religious Education Learning Program"; carries admin portal, attendance, homework, DRE roles | Tier 2 (product page) |
| KidCheck | Standalone children's **check-in** specialist — the adjacent-Type boundary test | Entire product is check-in/security; customer quote documents switching between ChMS check-in and KidCheck | Tier 2 (product page) |
| Planning Center Check-Ins | Church-suite check-in product — second boundary test | "Sunday School" appears as an attendance-report event type; grade promotion; no enrollment/class machinery | Tier 2 (product page) |
| Churchteams / Servant Keeper / Church Windows / PowerChurch / Breeze-Tithely | Protestant ChMS poles — how Sunday school is realized **without** a dedicated education module | Module lists inspected on home pages: groups + check-in + attendance, no education module | Tier 2 (home pages) |

Unreached poles (see Uncertainties): ShulCloud and ChaverWeb (synagogue management with religious-school modules), madrasa/Islamic supplementary-school software.

## Sources

- ParishSOFT product pages — https://www.parishsoft.com/ , https://www.parishsoft.com/faith-formation/ (fetched 2026-09-09)
- ParishSOFT Faith Formation fact sheet — https://6060861.fs1.hubspotusercontent-na1.net/hubfs/6060861/Catholic%20Brands%20Files/Fact%20Sheets/Religious%20Education.pdf (fetched; PDF binary only, not text-extractable in this environment)
- ParishSOFT support center (Zendesk, fetched 2026-09-09):
  - Navigate the Religious Education Module — /hc/en-us/articles/14634798083867
  - Settings for Faith Formation (Terms, Rooms, Grades etc.) — /hc/en-us/articles/33087818833307
  - Add a class — /hc/en-us/articles/14636192408091
  - Taking Attendance in Faith Formation — /hc/en-us/articles/32696573159963
  - Set up online registration and fee payment — /hc/en-us/articles/26758984567067
  - Adding Volunteers to Faith Formation — /hc/en-us/articles/33086609037851
  - About the Classes & Sessions Page — /hc/en-us/articles/40851421207835
  - About the Group Sacraments Page — /hc/en-us/articles/40832996950299
  - Register and pay for a class using My Own Church — /hc/en-us/articles/14631638954779
- CatholicBrain — https://www.catholicbrain.com/ (fetched 2026-09-09)
- KidCheck — https://www.kidcheck.com/ (fetched 2026-09-09)
- Planning Center Check-Ins — https://www.planningcenter.com/check-ins (fetched 2026-09-09)
- Churchteams — https://www.churchteams.com/ (fetched 2026-09-09)
- Servant Keeper — https://www.servantpc.com/ (fetched 2026-09-09)
- Church Windows — https://churchwindows.com/ (fetched 2026-09-09)
- PowerChurch — https://www.powerchurch.com/ (fetched 2026-09-09)
- Breeze ChMS / Tithely — https://www.breezechms.com/ (fetched 2026-09-09)
- Search engines: Bing (regional redirect, results degraded), DuckDuckGo HTML (timeout) — used for madrasa/standalone-product discovery, inconclusive

## Product A — ParishSOFT Faith Formation / Religious Education module

### Key observations (Layer A — Tier 1 unless noted)

**Identity of the module (Tier 2 + support):**
- Product page: "ParishSOFT Faith Formation is your trusted solution for **managing religious education**. Easily organize leaders, track attendance, and schedule classes with confidence using our built-in calendar of national and religious holidays."
- Support center: "**Faith Formation** is the **Religious Education module** from the Legacy system." The vendor treats the two names as one module.
- Positioning: "Purpose-Built for Catholic Parishes: Designed specifically for managing religious education programs."
- Scope statement: "All-in-One Program Management: Streamline the administration of **Religious Education, Adult Faith Formation, and Vacation Bible School (VBS)** in one centralized location."
- Integration statement: "Integrated Parish Records: Seamlessly manage families, members, and sacraments in one unified system."
- Reports named on the product page: "attendance records, catechist lists, class rosters, parent information, labels, name tags."

**Configuration building blocks ("Lookups"):**
- Lookup categories: **Term, Building, Room, Department, Grade, Volunteer Role**.
- Term = "the broadest timespan classes are held throughout the year", with a from/to date range; "The software uses a combination of term and session information to generate an initial class schedule for classes"; a "Use Sessions" option; a "Show in Online Registration" option.
- Room requires a Building; optional Capacity ("the number of seats in the classroom or the number of people that the room can hold").
- Once a lookup is used in a class/session, editing is limited; used terms cannot be deleted, only deactivated.
- General settings switches: **My Education, Online Payments, Online Registration**.

**Class model:**
- "Adding a class in ParishSOFT helps organize **faith formation, sacramental prep, or ministry groups**."
- Build order: lookups → sessions → classes → students. Session information becomes "Meeting Times" on the Classes page.
- Class record (Classes & Sessions page): name, session, **leader** (the volunteer with the Leader checkbox, marked with a star), other volunteers, grade, **capacity**, enrollment count, roster.
- Class tasks: add, **copy class to a different term** ("Copy classes with all details (except students) to the next term"), export CSV, enroll students, "**transferring or promoting students to a new class**".
- Session record: name, meeting day, time, volunteers, number of classes, start/end dates. Sessions can be copied from one term to another.

**Students & volunteers:**
- Default page of the module: **Students & Volunteers**, filterable by session/class/grade.
- "Only members added to the **Family Directory** can be selected when adding a new student." (Taking Attendance article)
- "Only volunteers who are populated in the **Member List of the Family Directory** will be available to add here." (Adding Volunteers article)
- Volunteers carry roles (lookup) and can be filtered by class, department, role.

**Attendance:**
- Attendance page with filters; per-student marks: **Present (green check) / Absent (red X)**, plus **Tardy** and **Excused** options; "Mark All → Present" bulk action.
- "If a student's enrollment date is OUTSIDE of the exact date parameters set for the SESSION, the student will NOT appear in the Attendance List."
- "If your class has no meeting dates or is not affiliated with a session, you **cannot take attendance** for the class."
- Once recorded, the attendance record persists; statuses can be changed (Present↔Absent, →Excused, →Tardy) but not un-recorded.
- Printable **attendance sign-in sheets** and blank attendance sheets; attendance reports by date/grade.

**Online registration & fees (family portal "My Own Church"):**
- "With My Own Church, users can conveniently register their children for Religious Education classes and make payments in one place… pay the class fees via their My Own Church portal in the **My Education** tab."
- Registration is enabled **per term**, per session, with **Registration Start & End Dates**.
- Family-side flow: log in → Religious Education tab → Online Registration → **Review Current Family Details** (update family record) → Select Enrollment Term → Add Students (form captures **Special Learning Needs** and **Health or Medical Needs**; **1st, 2nd, and 3rd class choices**) → Pay and Submit.
- Fee structures: **Flat Fee** per student; **Additional Student Discount** (tiered per-child pricing); **Fee Cap** ("limits the amount a family will be charged when registering their students"); **Discounts** (per-student amount, percentage off total, flat total discount).
- Payment routes into a **Giving Fund** (ParishSOFT Giving) or an **External Link**; a "No payment option" also exists.
- Outcome emails: registration received → payment receipt → "**registration has been accepted or rejected if the class was full**" — class capacity gates acceptance.

**Sacrament/milestone machinery:**
- Sacrament types in the module: **Baptism, Reconciliation Prep, First Eucharist, Confirmation**.
- Sacrament records live on member records and are searchable by **Prep Year, Term, Class, Grade, Age Range**.
- **Group Sacraments** bulk entry/edit: select a set of members (e.g., a confirmation class) and set shared values — Completed checkbox/date, **Prep Year**, Place, **Celebrant**.
- Permissions: View / Add-Edit / Print; "**Sacrament records cannot be deleted**."
- Class naming supports sacramental prep classes (e.g., a class named "1st Communion" appears in the sacrament search's class filter).

**Adjacent modules in the same suite (packaging evidence):** Families (census), Giving, Tuition ("If your parish charges for religious education, faith formation, or school tuition…"), Ministry Scheduler (separate module), Safe Environment (background screening), ParishCast (communication), Intelligent Query (report builder).

## Product B — CatholicBrain

### Key observations (Layer A — Tier 2)

- Self-labels: "Discover the #1 Pre-K to 8th Grade **Faith Formation Program**"; "A Premier **Religious Education Learning Program**".
- Center is **content/curriculum**: "1,000+ videos, games, and lessons", "USCCB-approved curriculum", quizzes, eBooks, lesson plans, seasonal programs (Advent, Lent, VBS), interactive Bible.
- Management layer riding on the content: "**Teachers, Catechist & Parent Portal** — Tools for lesson planning, reporting, and student management"; "**Homework & Attendance** — Manage tasks…"; "**Progress Tracking** — Visual dashboards for teachers and parents"; "**Admin Portal for Teachers Catechists and DREs**"; "Classroom Management and Communication Tools"; "Student Progress, Report Card and Homework Tracking"; "First Communion and Reconciliation Program".
- Roles at signup: Parent, Volunteer, Catechist, Priest, Teacher, Principal, Administrator, **Director of Religious Ed**.
- Membership plans: Family / Parish / School; school-code based student signup.
- Gamification: points, rewards, badges, classroom leaderboards.

Reading: the content pole carries a class-management layer (attendance, homework, progress, DRE admin) but its center of gravity is curriculum delivery — the inverse emphasis of the ParishSOFT pole.

## Product C — KidCheck

### Key observations (Layer A — Tier 2)

- Entire product is "**Easy, Fast, Secure Children's Check-In**": security features, mobile Express Check-In, reports, Roster Check-In, communication tools, Admin Console, YouthCheck, volunteer scheduling.
- Pricing per month; check-in stations and label printing.
- Boundary evidence in the vendor's own customer quote: "We decided to try the check-in with our church management system. We quickly realized this was a huge mistake… we switched back to KidCheck." — check-in is a distinct product population from both ChMS and education management.
- No enrollment, classes, terms, grades, fees, or milestone machinery anywhere on the page.

## Product D — Planning Center Check-Ins

### Key observations (Layer A — Tier 2)

- "Keep children safe, give parents peace." Check-in stations, custom name tags/security labels, classroom checklist stations, emergency texting to parents, medical notes on tags, live class lists, multicampus, secure checkout (label matching, trusted-people verification).
- Attendance reports: "Filter attendance reports by event type—**like Sunday School or VBS**—date, classroom, grade, and more" — Sunday school appears as an **event type**, not as a persistent enrolled class structure.
- "**Grade promotion**: Move children from one grade to another with just one click" — grade as a people attribute, not a class placement.
- Companion products: Registrations ("Organize your signups for VBS, camps, and midweek groups… then use your stations to check children into the event"), Services (volunteer scheduling), People (households), background checks via Checkr integration; free Headcounts app for quick attendance.
- Pricing by number of daily check-ins.

## Product E — Protestant ChMS poles (Churchteams, Servant Keeper, Church Windows, PowerChurch, Breeze/Tithely)

### Key observations (Layer A/B — Tier 2 home pages)

- **Churchteams** feature list: People & App, Check-In, Volunteers, Text-to-Church, Communication, **Groups**, Giving, Events & Forms, Automation, Websites. No education module; Sunday school would live in Groups + Check-In.
- **Servant Keeper** pillars: Church Management, Communications, **Child Check-In**, Online Giving, Sites/Apps/Livestream; a "Children's Ministry" team page framed around check-in and volunteer coordination. No education module.
- **Church Windows** modules: Membership, Scheduler, Donations, Accounting, Payroll; attendance tracked inside Membership ("tracking attendance trends"). No education module.
- **PowerChurch Plus**: Membership, Contributions, Accounting, Events Calendar, plus a separate Check-In product. No education module.
- **Breeze (rebranded Tithely Church Management)**: People, Groups, Events, Service Planning, Forms, "Check-in & Name Tags". No education module.

Reading: the Protestant market realizes Sunday school through **groups + check-in + attendance** inside a general ChMS; no dedicated religious-education module is visible at any of the five poles inspected.

## Unreached poles

- **ShulCloud** (synagogue management; markets a religious-school module): www 403 ×2, non-www 403, archive.org timeout ×2 — abandoned per source-access rules.
- **ChaverWeb** (synagogue management; religious-school module): transport error ×3 (www, non-www, http) — abandoned.
- **Madrasa / Islamic supplementary-school software**: Bing returned a regional results set with no software products; DuckDuckGo HTML timed out; no verifiable product found this pass.

## Cross-product Comparison

| Structure | ParishSOFT (Catholic module) | CatholicBrain (content pole) | KidCheck / PCO Check-Ins (check-in) | Protestant ChMS poles |
|---|---|---|---|---|
| Enrolled students of record in a program | ✓ (students from Family Directory, enrolled per term) | partial (students under parish/school accounts, class rosters) | ✗ (per-event attendees) | partial (groups with members; no program enrollment) |
| Classes with assigned teacher/catechist | ✓ (leader + volunteers, capacity, roster) | ✓ (classes under DRE/teacher portal) | ✗ (locations/rooms at events) | groups with leaders (generic) |
| Recurring meeting schedule within a program term | ✓ (term → session → meeting times) | partial (lesson plans; schedule depth unverified) | ✗ (events/dates) | group events |
| Per-session attendance against the roster | ✓ (Present/Absent/Tardy/Excused, sign-in sheets, reports) | ✓ (attendance feature) | ✓ (but per-event, security-centered) | ✓ via groups/check-in (generic) |
| Family/member-record substrate | ✓ structural (students AND volunteers must be Family Directory members) | ✓ (parent accounts, family plans) | households (for security) | ✓ member database |
| Program term + year-to-year rollover | ✓ (copy classes/sessions to next term; promote/transfer students) | unverified | ✗ | ✗ |
| Online registration with windows + class choices | ✓ (start/end dates, 1st/2nd/3rd choices, special needs) | ✗ (membership signup) | ✗ (Registrations is a separate PCO product) | registration products (generic events) |
| Fee machinery (per-student, family cap, discounts) | ✓ | membership pricing | n/a | giving-centric, not program fees |
| Milestone/sacrament tracking | ✓ (4 sacrament types, prep year, celebrant, non-deletable) | ✓ (First Communion/Reconciliation programs) | ✗ | ✗ |
| Curriculum/content delivery | ✗ (administration only) | ✓ (the center) | ✗ | ✗ |
| Security check-in (labels, checkout matching) | ✗ (separate Safe Environment module is screening, not check-in) | ✗ | ✓ (the center) | via check-in modules |

**Conclusions from the comparison:**
- The **enrollment → class → attendance loop over a congregation's families** appears wherever a dedicated religious-education realization exists (ParishSOFT fully; CatholicBrain partially).
- Check-in products share attendance but lack enrollment/classes/terms — attendance alone does not make education management.
- Content platforms share the class layer but center on curriculum.
- The dedicated-module realization is Catholic-market-led; the Protestant market realizes the same practice through generic groups + check-in.

## Canonical Model

### L0 — Defining Invariant

Three jointly-held structures, bound to the congregational domain:

1. **The enrolled student of record** — a persistent enrollment binding a person (typically a child of a family in the congregation) to the congregation's religious education program for a defined program term. The enrollment is the unit of record: created at registration, placed in a class, carried through the term, accumulating the student's program history. Remove → event signup or check-in tool with no program memory.
2. **The class as the taught unit** — students organized into classes within the program, each class carrying an assigned teacher/catechist drawn from the congregation and a recurring meeting schedule within the term. Remove → enrollment registry / flat roster.
3. **The session-attendance record** — attendance recorded per meeting date against the class roster, accumulating as each student's participation history in the program (the class register). Remove → enrollment without a participation record; the program's ongoing life is unmanaged.

**Domain binding:** the program is the congregation's own religious education — catechesis, faith formation, religious school — administered by the congregation over its own families; students and teachers come from the congregation's people records. Remove the congregational binding → generic children's-activity / class management.

**Jointly-held load-bearing:**
- 1 alone = enrollment registry
- 2 without 1 = class catalog with no students
- 3 without 1+2 = attendance log with no roster
- 1+2 without 3 = enrollment system with no participation record
- 1+3 without 2 = attendance with no class structure
- 2+3 without 1 = per-event attendance = check-in territory

### L1 — Common Mature Structure

- Program term / program-year container with **rollover** (copy classes and sessions to the next term; promote or transfer students between classes/grades).
- **Online registration** with enrollment windows, class choices (commonly ranked preferences), and special-needs/medical capture.
- **Fee machinery**: per-student fees, multi-child discounts, family caps, discounts; payment routed into the congregation's giving funds or an external processor.
- **Grade levels** as the placement vocabulary.
- **Rooms/locations** for classes (building → room, capacity).
- **Program lines** in one place: children's religious education, adult formation, vacation Bible school.
- **Milestone/sacrament tracking**: preparation year, completion date/place/celebrant, group completion for a class, permanent (non-deletable) records.
- **Reporting**: class rosters, catechist lists, attendance reports (by date/grade/class), parent lists, mailing labels, name tags.
- **Communication**: email/message students and parents, email volunteers.
- **Volunteer roles** for catechists/teachers.
- **Family portal** for self-service registration and payment.

### L2 — Variant / Optional Structure

- **Tradition shape**: Catholic sacramental-prep machinery (the deepest realization); Protestant Sunday school (often realized as groups + check-in inside a ChMS, no dedicated module); synagogue religious school (market context only this pass); madrasa/Quran school (unverified).
- **Child-safety machinery**: check-in integration, background screening / safe-environment compliance.
- **Curriculum/content delivery**: the content-platform pole (CatholicBrain) — content center with a class-management layer.
- **Paid vs free programs** (fee machinery present or absent).
- **Deployment**: desktop-installed vs cloud; module vs standalone product.

### L3 — Vendor-specific Structure (Research Notes only)

- ParishSOFT: Term/Session/Class three-level hierarchy with Lookups; My Own Church portal with My Education tab; Group Sacraments bulk entry; "sacrament records cannot be deleted"; enrollment-date gating of attendance lists; fee-cap mechanics; three-email confirmation flow (received → receipt → accepted/rejected if class full); built-in calendar of national and religious holidays; Intelligent Query; Safe Environment module; separate Tuition module for school/RE fees.
- CatholicBrain: points/rewards/badges/leaderboards; USCCB-approved curriculum branding; report cards; school-code student signup; 11-day vs 30-day trial funnels.
- KidCheck: security labels, Express Check-In, Check-In Station Pro, YouthCheck.
- Planning Center: Headcounts app, one-click grade promotion, Checkr background-check integration, pricing by daily check-ins, Church Center self check-in.

## Vendor-specific Findings

- The "Faith Formation" name is ParishSOFT's rebrand of its own "Religious Education" module (vendor-documented); the market phrase for the leaf remains "religious education".
- ParishSOFT's sacrament vocabulary (Baptism, Reconciliation Prep, First Eucharist, Confirmation) is Catholic-specific machinery.
- KidCheck's customer quote about leaving ChMS check-in and returning is single-source boundary evidence, used only to document the check-in/ChMS seam.
- CatholicBrain's gamification and USCCB branding are product-specific.

## Boundary Findings

1. **vs Church Management System (ChMS)** — module↔standalone spectrum. ParishSOFT ships Religious Education/Faith Formation as a named module of its Family Suite (the vendor's own docs call it "the Religious Education module"); Protestant ChMS products realize Sunday school via groups + check-in without any dedicated module. The standalone pole is **not verified**: CatholicBrain is standalone but content-centered. This leaf holds as a Type centered on the education-program loop, with the module realization dominant — the same spectrum the ministry-scheduling pass documented. If future passes also fail to verify an independently-sold standalone specialist whose center is program administration, the leaf should be revisited as a ChMS-family module Type.
2. **vs School Management System / SIS** — no academic transcripts, no state/district reporting, no academic gradebook; the program is congregational catechesis, not a school. Full-time parochial day schools and full-time madrasas are school-management territory. The seam: remove the congregational-catechesis framing and add academic-record machinery → school management.
3. **vs LMS / Educational Content Platform** — content delivery vs program administration. CatholicBrain straddles: content center + class-management layer. The seam: what is the center of gravity — the curriculum being delivered, or the program being administered?
4. **vs Ministry Scheduling** — teacher-volunteer scheduling (positions × occasions × assignments) vs the class/enrollment/attendance loop. ParishSOFT ships both as separate modules (Faith Formation + Ministry Scheduler) — packaging evidence that they are distinct centers.
5. **vs Childcare Management** — custody/care operations (capacity-limited care inventory, per-stay billing) vs catechesis program administration.
6. **vs Event Management** — VBS is administered as a program line inside the education module (ParishSOFT documents VBS in the same place); the event's money/logistics economy is not the center here.
7. **vs children's check-in products (KidCheck, Planning Center Check-Ins)** — check-in centers security/attendance per event with no enrollment, classes, or terms; education management centers the enrolled student's program life. The two interoperate (check-in against class rosters) but neither subsumes the other.
8. **vs Course Registration System (§23)** — the registration transaction as center vs the ongoing program relationship as center.
9. **vs Nonprofit Program Management (§25)** — generic program-delivery machinery (program → planned elements → delivery records) vs the congregational education grammar (enrollment, classes, grades, attendance, milestones). Different object grammars; keep both.
10. **vs Classroom Management (§23)** — K-12 classroom instruction/behavior tools vs congregational program administration.

## Historical / Market-Sample Check

- **Paper-era Sunday school (Raikes-era, 1780s onward)**: class registers/rolls, teachers, superintendents, annual enrollment, per-Sunday attendance marks, milestone/confirmation classes — satisfies all three L0 legs with paper. ✓
- **Catholic parish CCD programs (pre-software)**: registration cards, class rosters, attendance sheets, sacramental-preparation records — satisfies. ✓
- **Hebrew school / cheder and madrasa class rolls**: enrollment, classes, teachers, attendance, milestone preparation — satisfies conceptually. ✓
- The definition names no software surface, no cloud, no online registration, no fees, no grade levels-as-school-grades — all era or market machinery.

## Anti-overfit Checks

- **Term/Session/Class three-level hierarchy NOT definitional** — ParishSOFT's implementation; the conceptual invariant is classes meeting on a recurring schedule within a program period.
- **Grade levels NOT definitional** — placement by level/cohort is the concept; grades are the dominant realization (grade promotion exists even in check-in tools).
- **Fees / online payment NOT definitional** — ParishSOFT documents a "No payment option"; free programs are common.
- **Online registration NOT definitional** — paper registration satisfies the core.
- **Sacrament/milestone tracking NOT definitional** — tradition-specific; absent from Protestant Sunday-school realizations.
- **Attendance status vocabulary (Present/Absent/Tardy/Excused) NOT definitional** — the per-session mark is the concept; vocabularies vary.
- **"Family Directory" as a named object NOT definitional** — the congregational people-record substrate is the binding; object names vary by product.

## Uncertainties

1. **Synagogue religious-school modules unverified** — ShulCloud (403 ×3, archive timeouts ×2) and ChaverWeb (transport errors ×3) unreachable; the Jewish pole rests on market context only. No operational claims drawn from it.
2. **Madrasa / Islamic supplementary-school software unverified** — search engines degraded; no product confirmed.
3. **Standalone (non-module) program-administration products not verified** — CatholicBrain is the nearest standalone but is content-centered. The module↔standalone spectrum therefore rests on the ministry-scheduling precedent plus this pass's module evidence.
4. **"Faith Formation" naming generality** — verified only as ParishSOFT's rebrand; whether other vendors use the term is unverified.
5. **CatholicBrain's schedule/term depth** — product page shows attendance/homework/progress but term/rollover machinery is unverified (no help-center access this pass).

## Final Synthesis

Religious Education Management is the congregation's education-program administration system. Its defining core is three jointly-held structures over the congregation's own families: the **enrolled student of record** (a person enrolled in the program for a term), the **class as the taught unit** (students grouped with an assigned catechist/teacher and a recurring meeting schedule), and the **session-attendance record** (per-meeting participation marks accumulating as each student's program history). Mature products add the standard machinery of the practice: program terms with year-to-year rollover and student promotion, online registration with family fee structures, grade placement, rooms, program lines (children's religious education, adult formation, vacation Bible school), milestone/sacrament tracking with permanent records, rosters/attendance/label reporting, and family-facing self-service. The market realizes the Type predominantly as a **module of church management systems** (the Catholic parish pole is the deepest and the only one verified at Tier 1), with a **content-platform pole** (curriculum center with a class-management layer), adjacent **check-in specialists** (different Type), and a Protestant market that realizes Sunday school through generic groups + check-in without a dedicated module. The synagogue and madrasa poles were unreachable this pass and are recorded as uncertainties, not claims.
