# Research Notes — Higher Education Administration System

Research date: 2026-09-08
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1

## Research Goal

Understand, from real products, what a "Higher Education Administration System" actually is in the market: the institution-level administrative system of record for a college or university. Establish its defining core (the structure without which it stops being recognizable as this Type), the common mature structure around that core, the variant space, and the boundaries against neighboring Types (Student Information System, School Management System, ERP, Admissions/Enrollment Management, Course Registration System, Academic Timetabling, Curriculum Management, LMS, Financial Aid Management, Student Billing System).

## Initial Boundary

Initial hypothesis before research:

- This leaf most likely corresponds to what the market calls "higher education ERP", "student information system (higher ed)", "campus management system", or "university management system" — the integrated system that runs a higher-education institution's administration, with the student academic lifecycle as the spine.
- Risk: near-duplicate of the directory's separate `Student Information System / SIS` leaf (SIS was not yet processed at research time — no sibling document to align against; boundary recorded as an open taxonomy question).
- Neighbors in the same directory section (23) already carved out as separate leaves: Admissions Management, Enrollment Management, Course Registration System, Academic Timetabling, Curriculum Management, Financial Aid Management, Student Billing System, Academic Advising Platform, Transcript Management, Campus Housing Management, Campus Card Management, Alumni Management, University Advancement Platform, Learning Management System, ERP (section 10), HRIS/HCM (section 9). This leaf must be defined so that it is not merely the union of all of them.

## Research Questions

1. What objects constitute the system's world: student, program, course, section/offering, term/academic period, faculty, registration, academic history, results, degree/credential?
2. Which of these form the spine that every product shares, and which are modular add-ons?
3. How does the applicant → student conversion work, and where does this system's own responsibility start and end (vs Admissions Management)?
4. How does registration (course enrollment per term) work in real products?
5. What accumulates on the student record over time (grades, credits, progression, graduation), and who produces those entries (faculty grading, exam results)?
6. What administrative functions are bundled in suites (financial aid, student accounts, HR, institutional finance, advancement) and how integral are they?
7. What self-service surfaces exist (student portal, faculty portal, advisor workspace) and what can each do?
8. Which rules govern behavior: registration gates, holds, prerequisites, capacity, add/drop windows, grade overrides?
9. Would older / regional / differently-scoped products (1980s registrar mainframes, non-US university systems, K-12+HE dual products) still fit the definition?

## Representative Products

Selected for market representability + documentation accessibility + different product philosophies + different customer levels:

| Product | Pole | Customer level | Evidence quality |
|---|---|---|---|
| Ellucian Student (Banner / Colleague lineage) | dominant enterprise higher-ed vendor; SIS + platform with separate HCM/Finance products | large universities, community colleges | Tier 2 (product page; help center behind Ellucian Hub auth) |
| Jenzabar One / Jenzabar Student | mid-market suite; "most-selected SIS in higher ed" claim; modular ecosystem | small/private colleges, mid-size institutions | Tier 2 (product pages; support behind auth) |
| Workday Student Management | cloud enterprise suite; student system as industry module next to HCM/Financials | large institutions | Tier 2 (product/capability pages; community docs behind auth) |
| OpenEduCat | open-source education ERP on Odoo; global/regional market (universities, colleges, K-12); self-host or cloud | small-to-mid institutions worldwide | Tier 1 (full public end-user documentation) |

Rejected / unreachable samples (recorded for honesty):

- Populi (small-college all-in-one SaaS) — support center unreachable from research environment (2 attempts: timeout, transport error). Not directly observed.
- Anthology Student (formerly Campus Management CampusVue) — product pages 404 / site redirects to Blackboard teaching-and-learning portfolio. Not directly observed.
- Oracle PeopleSoft Campus Solutions — oracle.com paths 404 from research environment. Not directly observed (legacy large-institution pole inferred from market knowledge only; no precise claims made from it).

## Sources

Tier 2 (official product pages, fetched 2026-09-08):

- Ellucian Student — https://www.ellucian.com/products/student (also reached via https://www.ellucian.com/solutions/ellucian-banner)
- Jenzabar One — https://www.jenzabar.com/jenzabar-one
- Jenzabar Student — https://jenzabar.com/product/student
- Workday Student Management — https://www.workday.com/en-us/products/student/overview.html
- OpenEduCat — https://www.openeducat.org/

Tier 1 (official end-user documentation, fetched 2026-09-08):

- OpenEduCat Documentation — https://doc.openeducat.org/
  - Applications index (SIS / Enrollment / Exams / Gradebook / Timetable / Library / Student Portal / …)
  - Workflow of Registration — https://doc.openeducat.org/applications/enrollment/enrollment-workflow.html
  - Student — https://doc.openeducat.org/applications/openeducat/student-openeducat.html
  - Getting Started setup sequence — https://doc.openeducat.org/getting-started/getting-started.html

Market-category corroboration (visible on fetched pages): Gartner "Magic Quadrant for Higher Education SaaS Student Information Systems" (referenced on Ellucian's site); Jenzabar titles Jenzabar Student "higher education's most-selected Student Information System (SIS)"; Workday places "Student Management" under Industry Operations; OpenEduCat markets "Education ERP" with a University solution.

## Product A — Ellucian Student (Tier 2)

Key observations (evidence layer A for this product):

- Category framing: "higher ed's complete solution that powers the end-to-end student lifecycle"; explicitly positioned in the "Higher Education SaaS Student Information Systems" market (Gartner MQ reference on the page).
- Named solution areas around the student lifecycle: Recruiting & Admissions; Student Aid; Curriculum; Student Success; Lifelong Learning; Advancement; Student Management ("The SIS, Redefined").
- SIS core description: "Unite administrative processes… support learner success from enrollment through graduation"; unified system eliminating data silos; self-service "for students and faculty"; real-time student data; built-in controls for regulations and accreditation standards.
- Curriculum is a first-class module: program governance, catalog, approvals, degree-curriculum rules ("AI Rule Builder"), public course catalog for prospective students.
- Student Success module: degree planning, early alerts, DegreeWorks (degree-audit product lineage), credential discovery.
- Suite packaging: Ellucian HCM and Ellucian Finance are separate products ("Purpose-built ERP for higher education"); Platform (workspace, reporting, automation, integration, document management) is separate. I.e., institutional HR/finance are adjacent products, not the SIS.
- Advancement (alumni/fundraising) is a module of Student in current packaging — a suite-breadth signal, not a core signal.

Interpretation: even the dominant vendor treats the SIS/student system as the student-lifecycle spine, and institutional finance/HR as separate-but-bundled ERP components. "End-to-end student lifecycle: from recruiting through advancement" is the suite story; "enrollment through graduation" is the SIS story.

## Product B — Jenzabar One / Jenzabar Student (Tier 2)

Key observations (evidence layer A for this product):

- Jenzabar One positioned as "A Cloud ERP and SIS for Higher Education"; ecosystem tiles: Advancement, Analytics, Chatbot, Communications, eLearning, Finance, Financial Aid, HCM, Recruitment, Retention, Student, Workflow, Campus Marketplace.
- Jenzabar Student: "complete set of fully integrated modules that make it easier to manage your student information and services"; "designed exclusively for higher education".
- Named Student modules: **Registration** ("streamline and simplify the registration process and automate student record tracking"), **Advising** ("information and planning tools… manage academic progress"), **Student Life** ("centralized student records, student activity, student profiles"), **Events**.
- Registrar testimonial (University of Mary): "reduction of advising errors, mistakes, re-dos, subs, and waivers we've had to process" — direct evidence that registration/advising/override (waiver) mechanics and registrar workflows are the operational heart of the product.
- Financial Aid, Finance, HCM, Advancement are separate ecosystem modules, same as Ellucian's packaging.

Interpretation: same shape as Ellucian — SIS core (registration + records + advising) with aid/finance/HR/advancement as attachable modules.

## Product C — Workday Student Management (Tier 2)

Key observations (evidence layer A for this product):

- Product sits under "Industry Operations" alongside HCM/Financial Management/Supply Chain for Healthcare — i.e., the student system is the higher-education-specific industry component of an enterprise suite.
- Named capabilities: **Admissions**, **Advising**, **Financial Aid**, **Student Experience**, **Student Finance**, **Student Records**.
- "Student Records" and "Student Finance" as named capability areas confirm the record system + student money as distinct functional areas within one product.
- Industry page for Higher Education exists; suite story is HR + Finance + Student on one platform.

Interpretation: cloud-suite pole. Same functional decomposition as the others; packaged as an industry module of a broader ERP.

## Product D — OpenEduCat (Tier 1)

Key observations (evidence layer A, directly from public end-user documentation):

- **Setup sequence** (Getting Started): Create Database → Setting up Company → Accounting Setup → Install OpenEduCat → **Create Academic Year → Create Course → Create Subject → Create Batch → Create Faculty** → Fees and Fees Terms → **Create Admission Register** → Create Student User → Setup Classroom → **Setting Up TimeTable** → Allocating Assignments → Grading Assignments. The institutional skeleton (academic year, program/course, cohort) is configured before any student exists.
- **SIS application group**: Program Management, Course Management, Subject Management, Academic Plan Management, Student, Faculty, Convocation, Class Room Management, Fees Management, Student Feedback, Dashboard.
- **Enrollment group**: Admission Registers; Applications (registration forms); **Workflow of Registration**: an application record moves Draft → Submitted → Confirmed → Admission Confirm → Done (Enroll) → "Open Student Profile" — i.e., the admission decision converts the application into the student record. There is also a Dynamic Admission group (admission templates, admission register).
- **Student record** (Student page): identity/photo/name; personal information (gender, birth date, nationality, visa info, language, emergency contact, login user, addresses, PIN/badge ID, registration number, library card); **Educational tab: Course (current program of study), Batch (cohort), Roll Number (assigned per course)**; tabs for Fees Collection Detail, Achievements, Discipline, Activity Log, Assignments, Parents, Health, Job Post, Placements, Feedback, Skills, Alumni ("Is an Alumni" flag).
- **Exams application**: exam configuration, exam sessions, exam attendees, result templates, marksheet registers/lines, result lines — the results machinery that writes onto the academic record.
- **Gradebook application**: grade scales, grade tables, grade templates, grade books per course, grade override ("How To Override Grades"), grading reports, print grade report.
- **Secure Transcript** application: configuration + transcript generation.
- **Student Progression** application: progression tracking; **Student Withdrawal** application: managed exit; **Convocation**: graduation ceremony handling; **Thesis** application: thesis registration/progress/submission (graduate pole); **Placement** (campus recruiting) and **Alumni** groups.
- Around the spine: Timetable (sessions, constraints, generation), Library, LMS, Attendance, Assignments, Live Classroom, Campus facilities, Transportation, Placement, Parent/Student portals, plus Odoo ERP base (HR/payroll, accounting, e-commerce, CRM, marketing).
- Marketing: "One Education ERP to Run Your Entire Institution… From admissions to graduation"; modules include SIS, Course, Financial, Online Admission, Gradebook, Exam, LMS, Attendance, Timetable, Library, Faculty, CRM; serves universities, colleges, and K-12 schools (level-agnostic product family; university solution page exists).

Interpretation: the clearest end-to-end view of the machinery. The spine is exactly: configure the academic structure → run admissions into it → convert applicants to student records → register students into course/batch → schedule teaching → collect fees → run exams/gradebook → accumulate results → progression → convocation/withdrawal/alumni. Everything else is an attachable module.

## Cross-product Comparison

| Structure | Ellucian Student | Jenzabar One/Student | Workday Student | OpenEduCat | Layer |
|---|---|---|---|---|---|
| Academic structure of record (periods/terms, programs, courses, offered instances) | Curriculum module, catalog, governance | Registration module; departmental structure | Student Records capability | Academic Year + Course/Subject/Batch + Class Room + Timetable (Tier 1) | **Core candidate (L0)** |
| Student as central person of record, enrolled in a program | SIS core, "from enrollment through graduation" | Student Life: centralized student records/profiles | Student Records | Student record with Educational (Course/Batch/Roll Number) (Tier 1) | **Core candidate (L0)** |
| Applicant → student conversion (admission into the record) | Recruiting & Admissions module | Recruitment module + Student | Admissions capability | Admission Register + Registration workflow → student profile (Tier 1) | Core handoff (admissions machinery itself = separate Type) |
| Term/period registration of students into offerings | SIS core, self-service registration | Registration module (first named module) | Student Experience / Records | Enrollment + Timetable (Tier 1) | **Core candidate (L0)** |
| Accumulating academic record → progression → completion | "enrollment through graduation", DegreeWorks lineage | Advising on academic progress | Student Records | Exams/Marksheet/Result → Progression → Convocation; Secure Transcript (Tier 1) | **Core candidate (L0)** |
| Faculty administration (records, teaching assignment, grading) | faculty self-service | Advising; staff modules | HR (separate) | Faculty app + grading + timetable assignment (Tier 1) | Common (L1) |
| Advising / degree planning | Student Success module | Advising module | Advising capability | Academic Plan / Student Mentor | Common (L1) |
| Student money (student accounts/billing + aid) | Student Aid module | Financial Aid module | Financial Aid + Student Finance | Fees Management + Fees terms | Common (L1; separate leaf exists) |
| Institutional finance / HR (HCM) | separate products (Finance, HCM) | ecosystem modules | adjacent suite products | Odoo accounting/HR base | Common suite attach (L1/L2) |
| Advancement / alumni | Advancement module | Advancement module | — | Alumni app | Optional (L2) |
| Self-service portals (student, faculty) | "Self Service" pillar | omnichannel self-service claim | Student Experience capability | Student Portal + Parent Portal apps (Tier 1) | Common (L1) |
| Housing / campus card / events / library / placement / transport | via partners/platform | Student Life; Events; Campus Marketplace | — | Library, Campus, Placement, Transportation, Events apps | Optional (L2) |
| LMS / teaching delivery | eLearning in ecosystem (Jenzabar); LMS separate leaf | eLearning module | — | LMS app (separate from SIS group) | Optional (L2); separate Type |
| Reporting/analytics, compliance/accreditation controls | Reporting & Analytics; "Stay Compliant" | Analytics module | Analytics & Reporting | KPI Dashboard; FERPA-aligned claims | Common (L1) |

Reading: four poles (legacy enterprise suite, mid-market suite, cloud ERP suite, open-source regional) agree on the same four-part spine and disagree only on how much is bundled around it. No product's core is definable by its bundle.

## Canonical Model

### L0 — Defining Invariant (deliberately small)

The institution-level administrative system of record for a higher-education institution, held together by four jointly-held structures:

1. **The academic structure of record** — the institution's own academic skeleton, configured and maintained in the system: academic periods (years/terms), programs/credentials, courses, and the concrete teaching offerings of those courses in a period. Everything the system does hangs on this skeleton. (Remove → generic institution CRM/ERP with no academic semantics.)
2. **The student as the central person of record** — an individually identified person, admitted into and enrolled in a program of the institution, whose institutional life is administered through their record. (Remove → a course catalog site or a faculty/staff system.)
3. **Registration** — the period-by-period binding of the student to the academic structure: program enrollment and registration into course offerings, subject to the institution's rules. (Remove → a static student database with no term operations.)
4. **The accumulating academic record** — grades/results attaching to the student's completed offerings, accumulating into an academic history that is evaluated for progression toward the credential and closed out at completion/graduation (the transcript-bearing record). (Remove → registration tooling with no memory — the Course Registration System pole.)

Jointly-held is load-bearing:

- 1 alone = course catalog tooling.
- 2 alone = people database.
- 1+3 without 2+4 = Course Registration System (separate leaf).
- 2+4 without 1+3 = transcript/archive shelf.
- 1+2 without 3+4 = admissions/enrollment registry + directory.
- 3+4 without 1 = grade book unmoored from any catalog.
- 2+3 without 4 = roster administration with no academic history.

### L1 — Common Mature Structure

Present across the sampled market; expected in practice, not definitional:

- faculty/staff records with teaching assignments and grade-entry duties
- applicant→student conversion machinery (admission registers/pipelines; admissions itself is a separate directory leaf)
- advising and degree/academic planning against program requirements
- student financials: fee/billing structures and financial-aid processing (both have separate leaves)
- self-service portals: student (registration, schedule, records, finances) and faculty (rosters, grade entry)
- academic timetable construction against rooms and offerings
- reporting/analytics, compliance and accreditation-facing controls
- communication machinery (notifications, campaigns) attached to status changes

### L2 — Variant / Optional Structure

Depends on segment, geography, deployment, business model:

- suite breadth: institutional finance + HR/HCM + advancement/alumni + fundraising bundled (suite pole) vs unbundled integrations vs best-of-breed point systems around a lean core
- regional academic models: US credit-hour/term/transcript/GPA model vs academic-year + examination/marksheet model vs European campus-management models; thesis machinery at graduate institutions
- campus-life modules: housing, campus card, events, library, placement/career services, transportation, health
- LMS either bundled, integrated, or absent
- deployment: SaaS vs self-hosted/on-premise (open-source pole)
- education-level span: some products serve K-12 and higher education on one codebase; this leaf is the higher-education-scoped instance
- lifelong/professional-learning extensions (non-traditional learners, micro-credentials)

### L3 — Vendor-specific Structure (research notes only)

- Ellucian: DegreeWorks degree-audit lineage; Experience/Central Workspace platform; "AI-native" platform positioning; ScholarshipUniverse/SmartPlan branded AI modules; Colleague/Banner product lineage and SaaS migration story.
- Jenzabar: Jenzabar One ecosystem naming; Unity Platform (Boomi-powered iPaaS); Chatbot/Retention/Campus Marketplace tiles; marketing statistics (percentages).
- Workday: Student Management naming under Industry Operations; Workday Digital ID ecosystem; Sana/Agent positioning (outside student scope).
- OpenEduCat: Odoo framework base; LGPL-3.0 free edition; kiosk PIN/badge ID mechanics; specific app naming (Admission Register, Marksheet Registers, Convocation, Grievance, OBE/CBCS curriculum models).

## Vendor-specific Findings

- The clearest statement of suite-vs-core separation: Ellucian packages HCM and Finance as *separate products* ("Purpose-built ERP for higher education") while Student is the student-lifecycle system; Jenzabar mirrors this with ecosystem tiles; Workday mirrors it with Industry Operations. None of the three considers institutional finance/HR part of the student administration core.
- OpenEduCat is the only sampled product with fully public operational documentation; its enrollment workflow states and student-record tabs are direct (A-layer) evidence for the applicant→student conversion and record anatomy. Other vendors' equivalents are behind authenticated help centers, so the same mechanics are asserted for them only at market-category level (B/C layers).
- Jenzabar's registrar testimonial is the only sampled direct statement of override/waiver machinery ("re-dos, subs, and waivers"), supporting registration overrides as an operational reality rather than a definitional structure.

## Boundary Findings

| Neighboring Type | Relationship | Boundary judgment ("remove X → becomes Y") |
|---|---|---|
| Student Information System / SIS (not yet processed) | **near-overlap; taxonomy question** | In the sampled market the higher-ed administration system *is* marketed as the higher-ed SIS (Jenzabar Student's own tagline; Gartner category). Defensible scoping: SIS = student-record system across education levels; this leaf = the higher-education institution's administration system whose spine is the student academic lifecycle on the academic structure. Recorded in STATUS Boundary Issues for reconciliation at the SIS pass. |
| Admissions Management | upstream, separate leaf | The system receives admissions output and performs the *conversion into the student record*; the application-review pipeline itself is not this Type's defining machinery. Remove the student record + academic spine, keep the pipeline → Admissions Management. |
| Enrollment Management | upstream/parallel, separate leaf | Commitment/contract/deposit machinery for the coming period is enrollment management; this Type picks up the student once enrolled. |
| Course Registration System | narrow slice | Registration exists here but bound to the program/record/progression context. Keep only period registration with no record/progression → Course Registration System. |
| Academic Timetabling | capability/neighbor leaf | Timetable construction is common here (A-evidence in OpenEduCat) but is a scheduling discipline with its own Type; this system consumes/hosts schedules. |
| Curriculum Management | capability/neighbor leaf | Catalog + program governance is common (A-evidence at Ellucian: curriculum governance module; OpenEduCat: Program/Academic Plan apps) but deep curriculum workflow is its own Type. |
| School Management System | sibling by education level | K-12 school operations are organized around grade levels/classes/parent communication, not programs/terms/credits/credentials. A K-12-only product satisfies School Management, not this Type; dual-level products (OpenEduCat) span both. |
| ERP (generic) | supplier/adjacent | Generic ERP models students as customers/employees; it lacks the academic structure and academic record. The higher-ed ERP *bundle* includes this Type plus finance/HR; the bundle is not this Type. |
| Learning Management System | sharp boundary | LMS delivers instruction; this system administers the institution and records outcomes. Registration/roster/grade data flows between them; delivery vs administration is the seam. |
| Financial Aid Management / Student Billing System | embedded capability vs separate Type | Aid and student-finance processing appear as modules in every sampled suite, but each is its own operational discipline and directory leaf. |
| University Advancement Platform / Alumni Management | downstream attach | Alumni/advancement modules exist in suites (A-evidence: Ellucian Advancement; OpenEduCat Alumni app) but fundraising/donor operations are a different Type. |

## Uncertainties

- Registration gate mechanics (prerequisite checking, capacity/waitlists, holds from finance/academic standing, add/drop windows) are near-universal in market knowledge but were **not directly observed** in this pass for any sampled product (help centers behind auth; OpenEduCat's public docs cover the enrollment workflow but not detailed registration rule configuration). Assertions kept at moderate strength in the final document; no precise defaults, deadlines, or limits stated.
- Financial-aid and student-accounts depth varies by vendor packaging (e.g., aid is a named Workday capability and Jenzabar module; OpenEduCat's free edition has fees management; whether aid depth is native vs via partner is unverified per product).
- Degree-audit machinery (requirements evaluation against program rules) is strongly evidenced at Ellucian (DegreeWorks lineage) and OpenEduCat (Academic Plan, OBE attainment) but was not observed as a named capability at Workday/Jenzabar in this pass; treated as common-mature rather than core.
- The exact current scope of Anthology Student, Populi, and PeopleSoft Campus Solutions was not verified (sources unreachable); these poles inform variant breadth only and no claim rests on them.

## Historical / Market-Sample Check

- 1980s–90s registrar mainframe systems (course catalog + section offerings per term + registration + grade posting + transcript printing): satisfy all four L0 structures without portals, aid modules, HR/finance, or cloud. Definition holds.
- Non-US regional systems (academic-year + course + batch + examination marksheets; the OpenEduCat shape, documented): satisfy the same core with a different regional vocabulary. Definition holds.
- European campus-management systems (programs, semesters, course offerings, registrations, examinations, transcripts): same core. Definition holds.
- The L0 deliberately abstracts "term/period" (US quarter/semester vs academic year vs trimester), "program" (degree/major vs course-of-study), and "results" (grade points vs marksheets) — no single region's vocabulary is baked into the definition.

## Final Synthesis

A Higher Education Administration System is the institution-level system of record that runs a college's or university's academic administration on the institution's own academic structure: it configures the academic skeleton (periods, programs, courses, offerings), admits and enrolls students into it, registers students into offerings period by period under the institution's rules, and accumulates graded results into each student's academic history, evaluating progression toward and closing out with the credential. Around that spine, mature products add faculty administration, advising/planning, student money (billing + aid), self-service portals, timetabling, reporting/compliance machinery, and — in suite form — institutional finance, HR, advancement, and campus-life modules. The spine is the Type; the bundle is the vendor's packaging. The Type is nearly co-extensive with the market's "higher education SIS / higher-ed ERP student core" category; the relationship with the directory's separate SIS leaf is recorded as a boundary issue for reconciliation.
