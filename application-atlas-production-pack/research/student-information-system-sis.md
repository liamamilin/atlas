# Research Notes — Student Information System / SIS

Research date: **2026-09-09** · Leaf: `Student Information System / SIS` (DIRECTORY §23, line 1637) · slug: `student-information-system-sis`

---

## Research Goal

Understand what a "Student Information System (SIS)" is as an Application Type — and, critically, place it against three already-processed sibling leaves that surround it:

- **School Management System** (processed 2026-09-09) — left a NEAR-OVERLAP / NAMING-TRADITION SPLIT flag with a proposed center-of-gravity seam and an explicit request: "joint review recommended when SIS is processed".
- **Higher Education Administration System** (processed 2026-09-08) — left a NEAR-DUPLICATE TAXONOMY NOTE deferring the SIS-vs-HEAS consolidation/scoping decision to this pass.
- **Capability-slice siblings** (student-attendance-system, student-behavior-management, student-billing-system, student-case-management, special-education-management, parent-portal, digital-gradebook, academic-timetabling, curriculum-management, enrollment-management, admissions, financial-aid, transcript-management, LMS, campus-card, campus-housing, school-transportation) — nearly all of which already describe the SIS in their own Related-Types sections as "the system of record for enrollment, demographics, official records".

This pass must also **discharge** the pending joint-review flags rather than create new ambiguity.

## Initial Boundary

Hypothesis before research:

1. The SIS is the education institution's **student-record system of record**: identity/demographics, enrollment, scheduling, attendance, academic outcomes, official documents.
2. The directory names "Student Information System", "School Management System", and "Higher Education Administration System" cover one heavily-overlapping market with different naming traditions (US K-12 "SIS"; international "school management / school ERP"; UK "MIS"; higher-ed "SIS / campus management / higher-ed ERP").
3. The SIS is the **data backbone** for a long list of specialist education Types.

Risks: over-fitting to the modern US-district shape (portals, state reporting, integration standards); double-counting structures that sibling leaves already claimed as their own L0.

## Research Questions

1. What do products actually named "SIS" contain, and what is their center of gravity?
2. How do vendors themselves use "SIS" vs "school management system" vs "school ERP" naming?
3. What is the SIS's structural relationship to the higher-education administration frame?
4. What does the SIS own versus hand off, relative to the capability-slice Types (attendance, gradebook, behavior, billing, special programs, portals)?
5. What is the smallest structure without which a product stops being recognizable as an SIS?
6. Does the definition survive older, regional, and non-US realizations (mainframe-era district systems, UK MIS, examination-marksheet systems, paper-era registers)?

## Representative Products

Sampled this pass (all directly fetched 2026-09-09):

| Product | Pole | Why sampled |
|---|---|---|
| **PowerSchool SIS** | US K-12 district; "connected products" philosophy; market leader | The clearest SIS-naming anchor; sells Enrollment/Communications/ERP/HR as separate connected products |
| **Infinite Campus** | US K-12 district; "all-in-one" philosophy | Second major US district SIS; opposite packaging philosophy from PowerSchool |
| **RosarioSIS** | Open-source, self-hosted, K-12-primary but cross-level | Vendor itself equates SIS = SMS = school ERP; complete public module documentation (Tier-1) |
| **Ellucian Student** | Higher-ed enterprise suite | Higher-ed SIS pole; Gartner category naming evidence; end-to-end lifecycle framing |

Inherited evidence from sibling passes (documented in their research files and STATUS flags, not re-fetched): Fedena, QuickSchools, Gibbon, Skyward (school-management-system pass — the naming-tradition evidence); Canvas LMS / Blackboard SIS-integration documentation (LMS pass); Jenzabar / Gartner category naming (HEAS pass); TADS product-family structure (enrollment-management, student-billing-system passes); special-education demographic-sync evidence (special-education-management pass); BusRight SIS-sync (school-transportation-management pass).

Rejected candidates this pass: Populi (transport error ×2 — abandoned), Classter (403, consistent with the school-management pass), Anthology Student (vendor rebranded to Blackboard; SIS product not reachable at fetched paths — recorded as market-structure note only).

## Sources

This pass (Tier 1 where reachable):

- PowerSchool — https://www.powerschool.com/products/student-information/sis/ (SIS product page: unification claim, reporting scope, family portal, PowerTeacher Pro, integrations, configurability, payments; also the all-products page https://www.powerschool.com/solutions/student-information-system-sis/ for the connected-products taxonomy)
- Infinite Campus — https://www.infinitecampus.com/products/student-information-system (SIS-as-core product page; all-in-one claim; add-on product wheel; parent app scope; statewide SIS product listed in nav)
- RosarioSIS — https://www.rosariosis.org/ (root: SIS=SMS=school-ERP naming claim, module list, level claim) and https://www.rosariosis.org/discover/ (module-by-module operational detail: School/Scheduling/Grades/Attendance/Discipline/Billing/Food Service/Moodle plugin, rollover, add-ons)
- Ellucian — https://www.ellucian.com/products/student (Ellucian Student: "The SIS, Redefined", lifecycle modules, HCM/Finance as sibling products) — page title "Ellucian Student transforms the student information system"; on-page press release names the Gartner® Magic Quadrant™ category "Higher Education SaaS Student Information Systems"

Inherited (see sibling research files for full URLs and dates): Fedena (root + /student-information-system-sis), QuickSchools, Gibbon docs, PowerSchool (earlier URLs), Skyward — school-management-system pass, 2026-09-09; Canvas API docs, Blackboard help — LMS pass; Jenzabar One/Student — HEAS pass, 2026-09-08.

**Source-access limitations (this pass):**

- PowerSchool help center (help.powerschool.com / PowerTeacher / admin guides) not fetched — product-page evidence only; no operational detail below that level is asserted for PowerSchool.
- Infinite Campus "Campus Community" documentation not fetched — product-page evidence only.
- Ellucian help/documentation sits behind authenticated portals (consistent with the HEAS pass) — product-page evidence only.
- Populi (transport error ×2), Classter (403 ×2 across passes), Anthology Student (rebrand; 404) — not sampled; the small-college higher-ed pole is evidenced only indirectly via Ellucian and the HEAS pass's Jenzabar/OpenEduCat evidence.
- RosarioSIS is the only sample with directly fetched operational (module-level) documentation; it therefore anchors the operational model, and cross-product generalization is calibrated accordingly.

Per the evidence rules: no precise numeric limits, default settings, or timing windows are asserted anywhere in the final document from this research; vendor marketing figures observed this pass are recorded below as product-specific claims only.

---

## Product A — PowerSchool SIS (US K-12 district, connected-products philosophy)

### Key observations (evidence layer A — directly observed on official pages)

- Product page: "PowerSchool SIS unifies student data, reporting, and family access in one platform".
- The all-products taxonomy places **SIS** under "Home Connections / Student Information" alongside **Enrollment**, **Special Programs**, **Communications (SchoolMessenger)**, **Attendance Support** as *separate products*; Learning Management (Schoology), Assessment, MTSS, Behavior Support, Curriculum & Instruction, ERP, HR are separate products under other areas. The SIS is described as "the secure, interoperable foundation that brings together communications, enrollment, special programs, analytics, and data intelligence in one connected system."
- "PowerSchool centralizes student information into one accurate record, so every stakeholder is working from the same source" / "one reliable source of student truth" (Student Information Solutions framing).
- SIS reporting scope (product page): "state and provincial reporting with powerful ad hoc tools… Access data instantly on attendance, behavior, health, graduation progress, assets, and student demographics—all protected by strict regulatory standards".
- Family surface: "visibility into academic performance, attendance, schedules, school bulletins, and real-time notifications with PowerSchool's Parent/Student Portal and a mobile app".
- Teacher surface: "PowerTeacher Pro. Straightforward management of grades, attendance, assignments, and data entry for both standards-based and traditional grading."
- Interoperability: "interoperable by design… custom API partnerships… interoperability standards certified by organizations such as the Ed-Fi Alliance and 1EdTech"; "75+ Certified Integrations" (marketing figure).
- Configurability: "Admins can modify any part of the interface, add or adjust SIS pages, and extend existing pages with new tables and fields—without custom development."
- Payments: "Families can pay fees, add meal funds… in the PowerSchool SIS mobile app."
- Marketing figures observed (product-specific, not generalized): 5300+ districts, 17M+ students served, 20M+ active users, 56 states and provinces supported.

Reading: the SIS pole is the **student record as single source of truth**, with everything else sold around it. The district buys the record; the operations are attachable products.

## Product B — Infinite Campus (US K-12 district, all-in-one philosophy)

### Key observations (layer A)

- "Our all-in-one solution and the #1 SIS for K12 modernization" — the SIS *is* the product; breadth is folded *into* it.
- "With over 1,500 tools, our all-in-one solution…" and "You'll not only get an SIS, but the option to use Infinite Campus as an all-in-one solution: SIS, LMS, Food Service, Communication, Online Registration, Payment Processing, Dropout Prevention, Activity Registration, School Stores, and much more within a single login." (figures are vendor marketing; the structural claim is one login / one system.)
- Product wheel graphic: "1500+ core tools in the Student Information System" at the center; add-on products around it (Campus Online Registration, Food Service POS, Payments, Messenger with Voice, Data/Workflow/Analytics/Learning suites, Report Translation Module).
- Roles: "Tools for everyone… staff, teachers, students, parents, technology, administrators."
- Parent surface: "Parents and guardians only need ONE app for everything: grades, assignments, attendance, food service, announcements, school stores, fees, activity registration."
- Nav also lists a **Statewide Student Information System** product (district-of-districts scale).
- 13 releases/year, 99% renewal (marketing figures; not structural).

Reading: the opposite packaging philosophy from PowerSchool — but the *center* is still the SIS ("1500+ core tools **in the Student Information System**"), and the add-ons are still *add-ons to the SIS core*. Same market, different packaging.

## Product C — RosarioSIS (open-source, cross-level, self-hosted)

### Key observations (layer A — richest operational evidence)

- Naming claim on the root page: "RosarioSIS is a free and open source **Student Information System (SIS), also known as School Management System (SMS) or even school ERP**." — direct vendor-level evidence that the three directory names are used as synonyms for one product.
- Level claim: "Primarily designed for K-12 schools, it will easily adapt to any educational institution such as a university, academy, or institute." — the level-generic frame is asserted by the vendor.
- Module map (Discover page):
  - **School**: schools; "Setup marking periods, school periods and grade levels"; calendar; "Rollover: roll data and promote students to the next school year."
  - **Students**: "Add new students and edit their information (enrollment, demographic information, photo, addresses and contacts, medical…)"; "Create parent users from student contacts."
  - **Users**: administrators/teachers/parents; user profiles and permission configuration.
  - **Scheduling**: "Schedule your students. Possibility to work with requests and the scheduler." "Organize your school's subjects, courses and course periods." Print schedules, class lists, "face-books", requests; spot incomplete schedules.
  - **Grades**: teachers create assignments, enter gradebook and final grades; "Print report cards, transcripts and honor roll certificates"; GPA reports; configure report card grades/comments.
  - **Attendance**: teachers take attendance; absences and comments; attendance codes; summaries and teacher-completion reports.
  - **Activities**: athletic/academic eligibility computed from gradebook.
  - **Discipline**: "Add, edit and consult discipline referrals."
  - **Accounting and Student Billing**: school incomes/expenses, staff salaries, "student fees and payments", balances, statements.
  - **Food Service**: menus, serving meals, student/staff food-service accounts, transactions.
  - **Moodle plugin**: "Students, parents and teachers are automatically created, updated and deleted in Moodle. Subjects, courses and course periods are automatically created… Automatically schedule or drop students from a course period in Moodle." — the SIS as provisioning authority for the LMS.
  - Add-ons: Library, Hostel, Messaging/Email/SMS, imports, Student ID Card, **Certificate of Enrollment**, Lesson Plan, Quiz.
- Deployment: self-hosted PHP/PostgreSQL-or-MySQL web application; translated into 12 languages (regional breadth).

Reading: a complete, minimal, self-contained SIS. The module map is the cleanest Tier-1 confirmation of the candidate L0: students (+enrollment) → structure (marking periods/grade levels/course periods) → scheduling → grades/attendance → report cards/transcripts → rollover/promotion — with everything else (billing, food service, discipline, library) as modules beside that spine, and the LMS as a *consumer* the SIS provisions.

## Product D — Ellucian Student (higher-ed enterprise suite)

### Key observations (layer A)

- Page title: "Ellucian Student transforms the **student information system**"; nav label "Student"; the SIS section on the page: "**The SIS, Redefined** — Unite administrative processes, improve data accuracy, and deliver seamless student and faculty experiences that support learner success **from enrollment through graduation**. Student Information System."
- Lifecycle framing: "higher ed's complete solution that powers the end-to-end student lifecycle" — modules: Recruiting & Admissions; Student Aid; Curriculum (governance, catalog); Student Success (advising, early alerts, DegreeWorks degree planning); Lifelong Learning; Advancement; plus "Student Management / The SIS" (self-service, real-time data, compliance "adherence to regulations and accreditation standards").
- Enterprise-suite shape: Ellucian HCM and Ellucian Finance are sibling products ("Student, HCM, and Finance operate as one AI-native platform") — the money/people sides are separate products unified at platform level, mirroring PowerSchool's connected-products shape at higher-ed scale.
- Category evidence: on-page press release — "Ellucian Named a Leader in the Gartner® Magic Quadrant™ for **Higher Education SaaS Student Information Systems**" — the analyst-category name for this exact market is "Student Information Systems".
- Cross-pass corroboration: the HEAS pass recorded Jenzabar Student marketed as SIS and the same Gartner category; the LMS pass recorded SIS roster-in/grade-passback as the institutional counterpart.

Reading: in higher education the same product is called SIS (Ellucian, Gartner) and "higher education administration / campus management" (HEAS pass evidence). The higher-ed realization carries the same spine — person of record → program/term structure → registration → accumulating record → graduation — under an institution-level umbrella.

---

## Cross-product Comparison

| Structure / capability | PowerSchool SIS | Infinite Campus | RosarioSIS | Ellucian Student | Strength |
|---|---|---|---|---|---|
| Student population of record (identity/demographics/contacts; guardians where minors) | ✓ ("one accurate record") | ✓ (staff/teacher/student/parent tools) | ✓ (Students module; "create parent users from student contacts") | ✓ (person of record across lifecycle) | **All 4 — core** |
| Enrollment binding into academic structure (year/term → grade level or program) | ✓ (graduation progress; district operations) | ✓ | ✓ (School module: grade levels, marking periods; Students: enrollment info) | ✓ (enrollment through graduation) | **All 4 — core** |
| Scheduling into classes/sections (student schedule) | ✓ (schedules in portal) | ✓ | ✓ (Scheduling module, requests/scheduler) | ✓ (curriculum/registration side) | **All 4 — core** |
| Attendance recording | ✓ (attendance in reporting + portal) | ✓ (parent app: attendance) | ✓ (Attendance module, codes, summaries) | (not explicit on page — higher-ed attendance is thin) | **3/4 — core at K-12 grain** |
| Academic outcomes → official record (report cards / transcripts / degree progress) | ✓ (reporting on graduation progress) | ✓ (grades in parent app) | ✓ (report cards, transcripts, GPA) | ✓ (lifecycle "through graduation"; DegreeWorks planning) | **All 4 — core** |
| Teacher gradebook / entry surfaces | ✓ (PowerTeacher Pro) | ✓ | ✓ (Grades module: assignments, gradebook, final grades) | ✓ (faculty self-service) | **All 4 — standard** |
| Guardian/family + student self-service surfaces | ✓ (Parent/Student Portal + app) | ✓ (one parent app) | ✓ (parent users; portal notes; registration) | ✓ (student/faculty self-service) | **All 4 — standard** |
| Official/authority reporting (state/provincial, compliance) | ✓ ("state and provincial reporting"; 56 states/provinces) | ✓ (Statewide SIS product; Report Translation add-on) | (exports; regional by installation) | ✓ ("compliance… regulations and accreditation") | **Common; depth is regional** |
| Integration hub / provisioning (LMS, partners, standards) | ✓ (Ed-Fi, 1EdTech, 75+ integrations) | ✓ (add-on suites around core) | ✓ (Moodle plugin: users+courses provisioned) | ✓ (platform data orchestration) | **All 4 — standard (modern layer)** |
| Fees / payments / food service | ✓ (pay fees, meal funds in app) | ✓ (payments, food service) | ✓ (Billing + Food Service modules) | (aid side; billing in suite ecosystem) | **Common; varies by segment** |
| Discipline / health data in the record | ✓ (behavior, health in reporting) | (in-tool; not page-evidenced) | ✓ (Discipline module; medical fields) | (not page-evidenced) | **Common; not core** |
| Packaging | connected products around SIS core | all-in-one around SIS core | modules in one web app | enterprise suite around SIS core | **Variant axis** |
| Education level | K-12 (US) | K-12 (US, incl. statewide) | K-12-primary, cross-level claim | higher ed | **Variant axis** |

Layer-B synthesis (cross-product commonality): all four sampled products organize the world around **student records → structure → enrollment/schedule → recorded outcomes → official record served outward**. The packaging, the level vocabulary, and the breadth of bundled operations differ radically; the spine does not.

---

## Canonical Model

### L0 — Defining Invariant (deliberately small)

The SIS is the education institution's **system of record for its students' official data**. Three jointly-held structures:

1. **The student population of record** — persistent, identified student records (identity, demographics, contacts; guardianship/family links where the population is minors) held as the institution's authoritative registry, persisting across years/terms.
   *Remove → a people/CRM database with student rows but no institutional registry role.*
2. **The enrollment binding into the institution's academic structure** — each student is bound, per school year or academic term, into the structure (grade level and classes/sections at K-12 grain; program and registered course sections at higher-ed grain), with enrollment status as first-class state (conceptually expected → enrolled → left) gating rosters, records, and reporting.
   *Remove → demographics database, or timetable machinery with nobody in it.*
3. **The accumulating official academic record** — attendance and academic outcomes recorded against the enrollment accumulate per student into the official history; consolidated into official documents (report cards, transcripts) and official standing (promotion/progression, graduation, exit); corrections are controlled; the record survives exit.
   *Remove → enrollment registry with no institutional memory; the record side alone (without 1+2) is free-floating transcript/gradebook tooling = Transcript Management / Digital Gradebook territory.*

Jointly-held load-bearing analysis:

- 1 alone = demographics/CRM database
- 2 without 1 = enrollment grid / timetable with nobody in it
- 3 without 1+2 = free-floating gradebook/transcript archive
- 1+2 without 3 = registry with no record of what students did (not "information" in the institutional sense)
- 1+3 without 2 = transcript archive unbound to living enrollment
- 2+3 without 1 = anonymous roster sheets with marks

### L1 — Common Mature Structure

Present in essentially all mature products; makes the Type practical but does not define it:

- teacher entry surfaces (attendance taking, gradebook, final-grade submission)
- guardian/family and student self-service surfaces (portals, mobile apps)
- scheduling support from section assignment up to automated master-schedule construction
- the integration layer: roster feeds/provisioning out to LMS and specialist systems, write-backs in, interoperability standards (Ed-Fi / 1EdTech observed at one vendor; treat standards specifically as that product's evidence)
- official and statutory reporting (depth is regional — see L2)
- health/medical and discipline data held as part of the record
- fees/payments surfaces (depth varies by segment)
- role-based access (staff by function, teachers by class, guardians by recorded guardianship, students by self)

### L2 — Variant / Optional Structure

- **Level shape** — K-12 (grade levels, form/homeroom groups, guardians as first-class actors, daily attendance) vs higher-ed (programs/terms, credits, registration machinery, adult students as account holders). Same spine, different vocabulary; one vendor explicitly claims cross-level adaptability.
- **Packaging** — connected products around an SIS core (PowerSchool pole); all-in-one single system (Infinite Campus pole); module-based open-source (RosarioSIS); enterprise suite at platform level (Ellucian).
- **Segment** — public district (statutory reporting central, minimal fees) vs private/international (admissions-driven, fee-driven); statewide/multi-district scale exists as a product shape.
- **Regional machinery** — US state/provincial reporting; UK MIS tradition; examination-marksheet systems; translated multi-country installs.
- **Bundled operations** — food service, transport, hostel, library, communications, alumni — bundled in some markets, integrated or absent in others.

### L3 — Vendor-specific (research notes only)

- PowerTeacher Pro (PowerSchool gradebook product name); PowerSchool's Ed-Fi/1EdTech certifications; "56 states and provinces", "5300+ districts", "17M+ students", "20M+ active users", "75+ certified integrations" (marketing figures).
- Infinite Campus "1,500+ tools", "13 releases each year", "99% renewal rate"; Campus add-on product names (Campus Food Service, Campus Messenger with Voice…); Statewide SIS product.
- RosarioSIS add-on catalog (Library, Hostel, Entry and Exit, Meeting, Jitsi Meet integration, Certificate of Enrollment…); 12-language claim; GPL v2 / PHP / PostgreSQL-or-MySQL stack.
- Ellucian DegreeWorks, ScholarshipUniverse ("17,000 scholarships"), "$1B+ SaaS R&D", "21M+ students served", "74% of HBCUs"; the AI-agent marketing layer.

### Rejected Findings (anti-overfitting)

- **"SIS = state-reporting machine"** — rejected as definitional; reporting depth is regional machinery (a translated open-source install in a non-reporting jurisdiction is still an SIS). Held as L2.
- **"SIS = gradebook"** — rejected; the gradebook is a term-scoped working ledger feeding the record (consistent with the digital-gradebook pass's own seam). Gradebook depth varies; the *official record* is the invariant.
- **"SIS must include fees/billing"** — rejected; public-district and higher-ed poles hold money outside the SIS product (PowerSchool ERP separate; Ellucian Finance separate). Held as L2/common.
- **"SIS = K-12 product"** — rejected; the higher-ed market's own category name is "Student Information Systems" (Gartner via Ellucian), and the open-source sample claims cross-level fit. The SIS frame is level-generic.
- **"SIS = integration hub"** — the hub role is universal *today* (all 4 samples) but it is the modern realization of "serving the record outward"; older mainframe-era district systems satisfied the Type by serving transcripts and official extracts without modern integration standards. Held as L1.
- **"SIS = the whole school operation"** — rejected as the *SIS* definition (that is the School Management System pole's center of gravity); the SIS pole treats operations as modules/connected products around the record. See Boundary Findings.

### Historical / Market-Sample Check (per §24)

Would older, regional, platform-native products still fit the L0?

- **Mainframe-era district student-records systems** (pre-web US districts): student records + enrollment + scheduling + attendance + grades + transcripts + state extracts — fits all three structures with no portals, no integration standards, no mobile.
- **UK MIS tradition** ("management information system"): same population + structure + record under a different name — fits.
- **Examination-marksheet regional university systems**: person of record + program/term structure + registration + accumulated results — fits (vocabulary differs).
- **Paper-era school office** (admission register, roll books, mark sheets, transcript files): the same three structures in paper; the SMS pass already used this pole for its leaf, and the SIS's record-keeping role is a subset of the same office. Fits.
- The L0 deliberately excludes: portals, mobile apps, integration standards, state-reporting depth, payments, food service, discipline/health data as required elements, guardianship as required (the higher-ed pole is self-owned adult records). None of these would break the historical check if required — but requiring them would fail it. They stay in L1/L2.

## Boundary Findings

### 1. vs School Management System — JOINT REVIEW (discharges school-management-system pass flag)

The school-management pass proposed: keep-both on a **center-of-gravity seam** — "the student's official record (identity, enrollment, academic history, statutory reporting) vs the school's whole administrative operation (record + money + logistics + staff + communication); products span both, center of gravity decides."

**This pass RATIFIES that verdict.** New direct evidence supporting it:

- RosarioSIS root page: "a free and open source **Student Information System (SIS), also known as School Management System (SMS) or even school ERP**" — a vendor selling *one product* under the directory's two different leaf names, in one sentence.
- (Inherited) Fedena sells one product under both names (root page "School Management Software…" + a dedicated "Student Information System SIS" page for the same product); QuickSchools calls its student database "the centerpiece of our student information system"; Skyward titles K-12 "School Management Software" while describing "Student information system and school ERP" as two suites.
- PowerSchool pole: the SIS product's own page is entirely record-centric (data, reporting, family access, integrations); money (ERP, Financial Strategy), HR, communications, learning are *separate connected products*. — SIS center of gravity.
- Infinite Campus pole: all-in-one, but structured as "1500+ core tools **in the Student Information System**" with add-ons around it — the record spine remains the center even when packaging is maximal.
- The school-management leaf's own L0 (population + academic structure + operational loop *including fees, communication, admissions as first-class job*) is the whole-operation pole; the SIS leaf's L0 (population + enrollment binding + official record) is the record pole.

Seam wording adopted for the final document: one heavily-overlapping market, two naming traditions; the shared spine is the student record; the SIS entry centers the official student record and treats money/logistics/staff/communication as modules or connected products; the School Management System entry centers the whole administrative operation and treats the record as one leg of the job. Products span both; center of gravity decides. **No directory change.**

Secondary naming note (from the school-management pass, confirmed here by RosarioSIS's self-description): a third regional tradition — "school management information system (MIS)" (UK/state-system vocabulary) — maps to the same population.

### 2. vs Higher Education Administration System — JOINT REVIEW (discharges HEAS pass deferred decision)

The HEAS pass defined its leaf as institution-wide higher-ed administration (academic-structure spine + student lifecycle + accumulating academic record), noted vendors market the same products as both SIS and higher-ed ERP/campus management, and deferred the consolidation decision here, recommending "keep-both with level-scope seam".

**This pass RATIFIES keep-both with the level-scope seam:**

- The higher-ed market's own category name is "Student Information Systems" (Gartner MQ category, quoted on Ellucian's page; Jenzabar evidence inherited from the HEAS pass); Ellucian's page title is "transforms the student information system". So the *population* of the two leaves overlaps almost completely at the higher-ed level.
- The SIS leaf is the **level-generic student-record frame** — its defining population spans K-12 through higher-ed (RosarioSIS claims cross-level fit explicitly; the L0 is written level-neutrally).
- The HEAS leaf is the **institution-level higher-ed frame** — its core is the same spine realized at university scale, framed with the institution's whole academic administration (programs, registration machinery, progression, credential award).
- Practical seam: SIS's higher-ed realization ≈ HEAS's core (both passes' evidence shows the same products); SIS additionally carries the K-12 (and cross-level) shapes HEAS does not; HEAS additionally carries the institution-level framing (structure/registration as the operating heart). Both remain recognizable under their own centers of gravity. **No directory change** (consolidation would require one; recorded, not executed).

### 3. vs capability-slice Types (multiple passes' flags confirmed from this side)

- **Student Attendance System**: attendance is universally an SIS capability at K-12 grain (3/4 samples page-evidenced; RosarioSIS module-documented); the standalone Type centers the *attendance operation* (capture, reconciliation, absence resolution, statutory attendance reporting) and lives beside or inside the SIS. Consistent with that pass's seam.
- **Digital Gradebook**: the gradebook is the term-scoped working ledger; the SIS holds the official record it feeds (that pass's own seam; RosarioSIS documents both sides in one product: gradebook entry → report cards/transcripts).
- **Student Behavior Management** (discharges that pass's record-ownership flag): the SIS stores discipline data *for the official record and official reporting* (RosarioSIS Discipline module: add/edit/consult referrals beside the record; PowerSchool reporting includes behavior data); the real-time school-wide conduct loop (framework + response + measurement) is that Type's center. SIS behavior modules = packaging variant of that Type's loop.
- **Special Education Management** (confirms that pass's seam from this side): the SIS owns the population and feeds demographics into the special-programs case system; the regulated process never migrates into the SIS core.
- **Student Billing System**: money loop over the account population is its own Type; SIS billing modules (RosarioSIS Accounting/Student Billing; PowerSchool in-app payments) are packaging variants. Consistent with that pass's forward note.
- **Parent Portal**: the guardian-facing disclosure layer *over* the SIS's records; ships overwhelmingly from SIS vendors (that pass sampled PowerSchool/Infinite Campus/Skyward portals as its products). SIS keeps the staff-side record administration.
- **Academic Advising / Campus Card / Campus Housing / School Transportation / Sports Eligibility / After-school**: all document the SIS as their population/enrollment/record supplier (inherited seams — academic-advising, campus-card, campus-housing, school-transportation, sports-eligibility, after-school-program entries). The SIS entry acknowledges the hub role without claiming their loops.
- **LMS**: rosters in, final grades out; the SIS keeps the official record (LMS pass's seam; RosarioSIS's Moodle plugin documents the provisioning direction concretely).
- **Transcript Management**: the official-document slice; the SIS generates transcripts from the accumulating record but transcript production/exchange as a discipline is its own Type.
- **Admissions Management / Enrollment Management**: upstream; the boundary moment is the conversion of the committed applicant into the student of record (enrollment-management pass's "enrollment handoff (student of record)"; Ellucian packages Recruiting & Admissions as a lifecycle module feeding the SIS).
- **Alumni Management**: downstream; the record hands off at graduation (alumni pass's seam).

### 4. What destroys the Type

- Remove record ownership (demographics/grades live elsewhere) → student recruitment CRM / marketing platform.
- Remove the enrollment/structure binding → contact database.
- Remove the academic record → attendance registry or scheduling tool.
- Move the center to teaching delivery → LMS. To money → Student Billing. To the whole operation → School Management System pole.

## Uncertainties

1. **The SIS/SMS seam is a center-of-gravity judgment, not a bright line.** Products genuinely span both (Infinite Campus all-in-one; Fedena dual-named). The final document states the seam honestly rather than pretending a clean partition. A future directory consolidation of the two leaves (plus HEAS) remains conceivable; recorded here, not executed.
2. **Higher-ed operational depth is product-page level only.** Ellucian's operational documentation is behind authentication (as in the HEAS pass); the higher-ed realization of the L0 leans on the HEAS pass's evidence (including OpenEduCat's public docs) plus this pass's page-level evidence.
3. **Populi, Classter, Anthology Student unsampled** (transport errors / 403 / rebrand). The small-college pole is the thinnest part of the sample; no claims specific to it.
4. **Infinite Campus's "1,500+ tools" and similar figures** are vendor marketing; treated as product-specific claims, never generalized.
5. **PowerSchool operational documentation not fetched** — no claim below product-page level is made about PowerSchool mechanics.
6. Whether the K-12 "attendance is core" leg should also bind at the higher-ed grain: higher-ed SIS products de-emphasize attendance; the final document therefore states attendance as part of the official record *where the institution's model requires it* (K-12 grain), avoiding a false universal.

## Final Synthesis

The **Student Information System (SIS)** is the education institution's system of record for its students' official data. Its defining core is three jointly-held structures: the student population of record; the enrollment binding of each student into the institution's academic structure (year/term → grade level or program → schedule of classes/sections), with enrollment status gating everything; and the accumulating official academic record (attendance and outcomes → history → official documents and standing), which survives exit and is corrected only by controlled action.

Around that spine, mature products add teacher entry surfaces, guardian/student portals, scheduling engines, statutory reporting, health/discipline data, fees, and — ubiquitously today — the integration hub role (provisioning the LMS and specialist systems, receiving write-backs). None of these is definitional; older mainframe-era, UK-MIS, examination-marksheet, and paper-era realizations satisfy the core without them.

The Type is the level-generic, record-centric frame of a market whose other leaves carry the whole-operation frame (School Management System, K-12) and the institution-level higher-ed frame (Higher Education Administration System). Vendors themselves sell single products under several of these names; the atlas keeps the leaves distinct on center-of-gravity and level-scope seams, both ratified by this pass's joint reviews.

One-line L0: *the education institution's system of record for its students' official data — student population of record + enrollment binding into the academic structure (status-gated) + accumulating official academic record (history → official documents/standing, surviving exit).*
