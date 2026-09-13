# Research Notes — School Management System

Research date: 2026-09-09
Slug: school-management-system (DIRECTORY §23 Education, Research & Knowledge Institutions)

---

## Research Goal

Understand what a School Management System actually is as an Application Type: what objects exist inside it, who operates it, what the recurring operational loop is, and where its boundaries lie against the dense cluster of neighboring education Types (SIS, Higher-Ed Administration, LMS, Parent Portal, capability slices like attendance/gradebook/timetabling/billing, and the commercial class-management siblings).

The pressing taxonomy question going in: **School Management System vs Student Information System / SIS** — both leaves exist in the directory, and the market uses the names with heavy overlap.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: a School Management System is the K-12 school's whole-administration system of record — people (students/guardians/staff) + academic structure (years, grade levels, classes) + the daily/term/annual operational loop (attendance, marks, fees, communication).
- Likely confusions: SIS (near-synonym in much of the market), Higher-Ed Administration (level shape), LMS (teaching vs administration), Parent Portal (guardian-facing layer), childcare/commercial class management (business vs institution).
- Unknowns: whether the SIS/School-Management split is a real structural seam or a naming-tradition split; how deep money/HR/transport go in the definitional core; whether US district SIS products and international "school ERP" products are one population or two.

## Research Questions

1. What objects does the system hold? (students, guardians, staff, years/terms, grade levels, classes/sections, subjects, attendance, marks, fees, timetable…)
2. How is the academic skeleton configured, and what binds a student into it?
3. What is the recurring operational loop (daily / term / annual)?
4. What roles exist and what surfaces does each get?
5. What money machinery exists, and is it definitional or market-dependent?
6. What school↔home communication exists, and is it definitional?
7. Where is the seam vs SIS, vs Higher-Ed Administration, vs LMS, vs the commercial class-management siblings?
8. Would older / regional / non-cloud products still fit the definition?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Philosophy / tier | Why sampled |
|---|---|---|
| Fedena (Foradian, India-origin) | International "school ERP" — all-in-one, fee-driven, self-hosted + cloud, 40,000+ institutes claim | The international school-management pole; also sells the same product under an "SIS" page (alias evidence) |
| QuickSchools (SaaS) | Small/private schools, ease-of-use, modular | Small-school SaaS pole; explicitly lists "SIS" as a feature of its school management software |
| Gibbon (open source) | Free, self-hosted "school platform", teacher-led | Open-source/free pole; only sampled product with fully public Tier-1 operational docs |
| PowerSchool SIS | US district SIS-first, student-record-centric, modular "connected OS" | US district pole; the SIS-naming tradition at its strongest |
| Skyward | US district "School District Management Software" = SIS suite + ERP suite | US integrated-administration pole; page literally titled "K-12 School Management Software" |

Rejected/abandoned: Classter (www.classter.com returned 403 on two attempts — root and /product/; abandoned per network rule; recorded as a sourcing limitation).

## Sources

All fetched 2026-09-09 unless noted.

- Fedena — https://fedena.com/ (root; "School Management Software & School Management System"), https://fedena.com/student-information-system-sis , https://fedena.com/feature-tour/school-fees-management-system , https://fedena.com/feature-tour/exam-management-system
- QuickSchools — https://www.quickschools.com/ (root), https://www.quickschools.com/quickschools/features/student-information-system
- Gibbon — https://gibbonedu.org/ (root), https://gibbonedu.org/features/ , https://docs.gibbonedu.org/administrators/getting-started/getting-started-with-gibbon/ , https://docs.gibbonedu.org/tutorials/school-setup/school-structure , https://docs.gibbonedu.org/tutorials/school-setup/student-enrolment , https://docs.gibbonedu.org/guides/modules/user-admin/rollover
- PowerSchool — https://www.powerschool.com/products/student-information/sis/ , https://www.powerschool.com/products/ (all-products page; the /solutions/... SIS URL redirected here)
- Skyward — https://www.skyward.com/k-12 (page title "K-12 School Management Software"; first attempt at /k-12/school-management-software 404'd, root K-12 path succeeded)

Evidence layers used below: **A** = directly observed on the cited page of that product; **B** = cross-product commonality across the sample; **C** = canonical inference from comparison + boundary reasoning.

---

## Product Observations

### Fedena (Layer A)

- Self-labels: "School Management Software & School Management System" (page title), "All-In-One College and School Management Software", "school ERP", "online school management system".
- FAQ definition (vendor's own): school management software "holds all institute data in one place" and manages "online admission, student attendance, online fee payment, timetable, parent communication, examination management, payroll, and online learning"; users are "students, teachers, parents, admin and other staff members".
- Headline modules: Exam & Gradebook, Student Admission, Parents Collaboration, Timetable & Attendance, Fees Management, Online Classes (video-conferencing integration), "+50 other modules"; HR & Payroll named in FAQ key features.
- **SIS alias evidence**: a separate page titled "Student Information System SIS | Student Management Software" describes the SAME product: "Fedena is a complete Institute Management System… By bringing the SIS & ERP feature under the same brand our goal is to make it easier for you to understand how various features under one roof work together." The SIS page's feature list = Student Data Management, Report Generation, Admission Management, Online Fees Payment, Transport Management, Attendance Management, Examination Management, Hostel Management, Library Management, Alumni Management, Communication System, Mobile App.
- Fees machinery (Layer A, fees page): fee structures per institution type; scheduled collection dates; fee setup by student category or course; master particulars & discounts; fee receipt templates; invoices for pre-scheduled fees (general/hostel/transport); advance fee collection; defaulter reports with SMS/email reminders; payment-gateway integration; tax slabs (VAT/GST); late fees/fines; fee refund/revert gated to privileged roles; staff salaries + payslips; donations; controlled access to finance.
- Exam machinery (Layer A, exam page): exam scheduling per batch/class; marks entry by teachers (editable); final-grade calculation across an exam group; report generation per grading system (vendor names CCE, ICSE, CWA, GPA, CBSE presets); customizable report-card fields; result alerts to parents; gradebook with student/subject/consolidated reports; skill-based mark entry; mobile mark entry with submission status.
- Attendance (root + SIS page): subject-wise or day-wise marking; biometric/RFID integration; instant alerts to parents.
- Multi-school management product line; branded mobile apps for parents/teachers/students; integrations (biometric, location/GPS, payment gateway, video conferencing).

### QuickSchools (Layer A)

- Self-labels: "Online School Management Software"; "A School Management System that is shockingly easy to use".
- Hero bullets: customizable gradebook; homework & assignments; **"Powerful Student Information System (SIS)"**; classroom and attendance management; parents portal; admissions management platform.
- SIS feature page: "The student database is the centerpiece of our student information system. It is fully integrated with all other features…"; the database holds address, siblings, parents, contacts, billing/accounts, medical history; "Teachers submit information about grades, homework, attendance, discipline, and achievements into the same electronic file so that a student's records are always complete and up to date"; parents update information, monitor accounts, pay school billings online, track grades/attendance/homework.
- Scheduling: specify how many times each course is taught per week; automated scheduler distributes classes into time slots "completely conflict free"; a master-scheduler product (named Orchestra — vendor-specific) for precise schedules.
- Gradebook: weighted assignments/assessments, multiple grading scales, custom formulas, progress reports and report cards "a click away". Transcripts: courses/grades auto-populated, customizable templates.
- Fee tracking + online payment; messaging via email/text/voice; admissions; teacher management; report creator.
- Segments: elementary, high schools, adult education, language schools; customer stories span US, faith-based, Catholic, online schools, Costa Rica, Pakistan.

### Gibbon (Layer A — richest, Tier-1 docs)

- Self-labels: "The Flexible School Platform"; "free, open source"; "Student Centred… collates student information"; "Teacher Led"; "Unified Access: Teachers, students, parents and administrators all access Gibbon from the same web-based platform, with highly configurable levels of access". Used by "international schools, public schools, home schools, and refugee schools". Testimonials call it "school management software system", "school platform", "sistema informativo scolastico" (Italian: school information system), and one calls it a VLE.
- Core modules (features page), grouped by the vendor itself:
  - **Learn**: Planner (lesson plans, units, homework, class attendance), Departments, Resources, Timetable, Activities, Individual Needs (learning plans), Library.
  - **People**: Students (Student Profile aggregating academic/behavioural/medical/SEN alerts), Application Form (public online applications; auto-creates user accounts and family links for accepted students), Attendance (form-group and per-student; absence history/patterns; future absences; evacuation reports; parent view), Behaviour (positive/negative notes with descriptors/severity/follow-up), Data Updater (staff/parents submit data updates into an admin queue), Staff (job openings → staff records; directory; contract details; HR/payroll access), Form Groups.
  - **Assess**: Markbook (continuous academic record across subjects, shared to students/parents), Rubrics, Tracking (graphs from Markbook + Formal Assessment), Formal Assessment (internal/external tests, school-wide scale conversion, value-added scores), Crowd Assessment.
  - **Other**: Messenger (email/SMS/Message Wall to flexible groups; daily bulletin), Finance (fees, billing schedules, invoicees; invoices/receipts/payment reminders; outstanding-payment lists; expense requests/approval).
  - **Admin**: School Admin (school years, year groups, form groups, houses, terms, school days), System Admin, User Admin (users, families, student enrolment, medical data), Timetable Admin (courses, classes, enrolment).
- School Structure setup (Tier-1 tutorial):
  - School Years: "almost all of Gibbon's functionality is reliant on the concept of a school or academic year"; system needs a "Current" year, plus any number of "Past" and "Upcoming" years; each has a sequence number.
  - Days of the Week (on/off + start/end times); Terms ("if your school year is divided into terms or semesters… otherwise, just create a single term the same length as your school year"); Special Days (holidays/closures — "helps determine whether things like school attendance should be enabled on any given day").
  - Year Groups ("the way that schools divides students on the basis of age"; ships preset Years 7–13; sequence number); Form Groups ("aka roll groups, home room, tutor groups — the groups in which students have their attendance taken and/or receive pastoral care"; single-year or mixed); Departments (learning areas or administrative staff groupings); Facilities (classrooms, labs, offices, sports facilities — used in the timetable).
- Student Enrolment (Tier-1 tutorial): Admissions module manages enrolment in the current school year and accepts application forms; forms built in a Form Builder; "Active" flag controls whether applications are still accepted; "Public" flag controls whether login is required — "Schools can use this feature to determine when student application process to the school ends / when application to the school closes to the public."
- **School Year Rollover** (Tier-1 guide): "Gibbon's tool for moving your installation from one school year to another, updating various records in one go." Backup warning: "Without a backup, there is no way to undo this process." Steps: add the next year; prime "Expected" users; enrol new students (status Expected → enrolled; parents set to Full; non-enrolled set to "Left"); enrol already-full new students (often via the online application form, possibly pre-enrolled in next year); re-enrol other students (non-re-enrolled → "Left"); set final-year students to "Left" (unless repeating); register new staff (unregistered → "Left"). Form-group progression can be pre-set ("Copy All To Next Year") or per-student via next-year enrolment. Users must log out/in to enter the new year.
- Integrations: Moodle connection documented (docs: "Connecting To Moodle"), Google/Microsoft integration.

### PowerSchool (Layer A — product pages; help center not fetched)

- Product named "PowerSchool SIS": "One Connected Student Information System for K-12"; "unifies student data, reporting, and family access in one platform".
- Feature blocks: state/provincial reporting (ad-hoc reports on attendance, behavior, health, graduation progress, assets, student demographics); Parent/Student Portal + iOS/Android app (academic performance, attendance, schedules, school bulletins, real-time notifications); PowerTeacher Pro (grades, attendance, assignments; standards-based and traditional grading); payments collected in the SIS mobile app (fees, meal funds); highly configurable setup (admins can modify interface, add pages/tables/fields without custom development); interoperability (Ed-Fi Alliance, 1EdTech certifications; 75+ certified integrations claimed).
- Company framing: "K-12 Connected Operating System" with three areas — Home Connections (SIS, Enrollment, Special Programs, Communications/SchoolMessenger, Attendance Support), Student Achievement (LMS/Schoology, Assessment, Curriculum & Instruction, MTSS, Behavior Support, CCLR/Naviance), Operational Excellence (Financial Strategy/Allovue, ERP Systems, Predictive Enrollment, Recruiting & HR, Educator Support).
- Reading: in the US district market the SIS is the student-record product; enrollment/registration, communications, finance/HR, LMS are separate products connected to it.

### Skyward (Layer A — product page)

- Page title: "K-12 School Management Software | Skyward". H1: "School District Management Software — Student information system and school ERP". "More than 2,000 districts… with one or both of our software suites."
- Two suites: **Student Information System** (feature categories: Office & Administration, Classroom Tools, Family Engagement, Student Services) and **Enterprise Resource Planning** (Human Resources, Fiscal Management, Payroll & Timeclock, Employee Portal, Asset Management).
- Page source icon vocabulary (Layer A, leaked asset names — strong domain-object evidence): Attendance, AttendanceType, AutoSchedule, CourseRequest, Demographics, Discipline, Diploma, Enrollment, FamilyAccess, Fee, FoodService, GradeBook, GradPlanReq, GraduationRequirements, Guidance, Health, ReportCard, ScheduleBuilder, Section504, SpecialEducation, StateReporting, StudentProfile, StudentSchedule, TestScores, Payroll, Budgeting, Bus, ActivityAccess, EmergencyContact, Impersonate, YearEnd…
- External category evidence: the page links to Capterra with the product named "Skyward School Management" — the review-site category for this market is literally "school management".

---

## Cross-product Comparison

| Structure / capability | Fedena | QuickSchools | Gibbon | PowerSchool SIS | Skyward | Reading |
|---|---|---|---|---|---|---|
| Student records w/ guardians-family links | A (student+parent records; guardian details) | A (parents/siblings in student database; family links) | A (families, guardianship via application auto-links) | A (demographics; family portal) | A (FamilyAccess, Demographics, EmergencyContact) | **B — universal** |
| Staff records | A (HR & payroll module) | A (teacher management) | A (Staff module, contracts, absences, substitutes) | separate product (Recruiting & HR) | separate suite (ERP/HR) | B — universal as records; HR/payroll depth varies |
| Academic year/terms as master clock | A (academic-year import/setup; "new academic year" setup) | A (marking periods in gradebook) | A ("almost all functionality reliant on school year"; Current/Past/Upcoming) | A (school-year context; graduation progress) | A (YearEnd icon) | **B — universal** |
| Grade levels / year groups + classes/sections | A (courses/batches; class allocation) | A (courses, classes) | A (year groups, form groups/roll groups/homerooms) | A (school types; student schedules) | A (Levels, Section, StudentSchedule) | **B — universal** (naming varies: batch/section/form group/roll group/homeroom) |
| Enrollment binding student → structure | A (admission → student; course/batch assignment) | A (admissions; student linked to classes) | A (student enrolment per year; Expected/Full/Left statuses) | A (Enrollment as adjacent product; SIS holds enrolled students) | A (Enrollment icon; NewStudentImport) | **B — universal** (US districts often split intake into a separate enrollment product) |
| Daily attendance | A (subject-wise/day-wise; biometric/RFID; parent alerts) | A (classroom & attendance management) | A (form-group + per-student; patterns; parent view; school-day calendar gates it) | A (PowerTeacher Pro attendance; attendance reports) | A (Attendance, AttendanceType) | **B — universal** |
| Assessment → report cards/transcripts | A (exams, gradebook, report cards, grading-system presets) | A (gradebook, report cards, transcripts) | A (Markbook, Formal Assessment, Reports cycles → proofreading → publishing) | A (PowerTeacher Pro grades; graduation progress) | A (GradeBook, ReportCard, TestScores, GraduationRequirements, Diploma) | **B — universal** |
| Timetable / scheduling | A (timetable module; classroom/subject/teacher allocation) | A (automated conflict-free scheduler) | A (Timetable + Timetable Admin; facilities) | A (implied; student schedules in portal) | A (AutoSchedule, ScheduleBuilder) | B — universal in sample; scheduling depth varies (auto-generation vs display) |
| Fees / money | A (deep: structures, invoices, receipts, defaulters, tax, refunds) | A (fee tracking + online payment) | A (Finance module: fees, billing schedules, invoices, receipts, reminders) | A (payments in mobile app: fees, meal funds) | A (Fee, FoodService icons; deep finance in ERP suite) | B — universal at some depth; **depth varies by market** (fee-charging vs public/district) |
| School↔home communication | A (SMS/email alerts; parents collaboration) | A (email/text/voice messaging) | A (Messenger: email/SMS/Message Wall; notifications) | A (portal notifications; Communications as separate product) | A (Family Engagement category) | **B — universal** |
| Parent/guardian + student portals | A (students/parents login; mobile app) | A (parents portal) | A (same platform, configurable access; parents docs section) | A (Parent/Student Portal + app) | A (FamilyAccess, Family Toolkit) | **B — universal** |
| Admissions/application intake | A (admission module; enquiries, forms, document verification) | A (admissions platform) | A (Application Form; active/public flags) | separate product (Enrollment) | A (NewStudentImport; Enrollment) | B — universal; **packaging varies** (module vs separate product) |
| Behavior/discipline | (not prominent on fetched pages) | A (discipline in student file) | A (Behaviour module) | A (behavior reports; Behavior Support separate product) | A (Discipline icon) | B — common |
| Health/medical | (not prominent) | A (medical history in student database) | A (medical data, medical alerts, Data Updater) | A (health reports) | A (Health, IHP icons) | B — common |
| Roles & permissions | A (user management; controlled finance access) | A ("powerful access right controls") | A ("highly configurable levels of access"; roles & permissions tutorial) | A (admin/teacher/parent/student surfaces) | A (SecurityAccess, TeacherAccess, StudentAccess, AdminAccess icons) | **B — universal** |
| Transport / hostel / library | A (transport w/ GPS; hostel; library) | absent from fetched pages | A (Library; no transport/hostel in core) | absent | A (Bus icon; FoodService) | **Variant — regional/optional** (strong in South-Asian school ERP; absent/minimal in US district SIS) |
| State/statutory reporting | absent from fetched pages | A (reports "for the school districts we serve" — supplemental org) | absent | A (state/provincial reporting) | A (StateReporting icon; State & Federal Reporting service) | **Variant — regulated-market machinery** |
| HR/payroll | A (HR & payroll module) | absent | A (staff contracts; HR/payroll detail access; no payroll run) | separate product | separate suite | **Variant — packaging axis** |
| Multi-school management | A (multi-school product line) | absent | absent | A (district = many schools, one SIS) | A (district-wide) | B — common at scale |
| LMS / online classes | A (video-conferencing integrations) | A (homework/assignments) | A (Planner/homework; Moodle integration) | separate product (Schoology) | absent from fetched page | B — common; **integration seam, not core** |
| Deployment | A (cloud + self-hosted "Custom ERP") | A (SaaS only) | A (self-hosted open source) | A (cloud) | A (hosted/on-prem historically) | Variant axis |

## Canonical Abstraction

### Level 0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **The school's population of record** — students (each linked to guardians/family) and staff held as persistent identified records in the school's own registry. *(Remove → a contact/CRM database.)*
2. **The school's academic structure of record** — school years/terms and the school's divisions of students (grade levels / year groups; classes / sections / form groups), with **enrollment** binding each student into that structure for a year. *(Remove → a generic people database or org chart.)*
3. **The school's operational loop** — the recurring recording operations run against enrolled students on the school's calendar: daily attendance and academic-outcome recording (marks/grades), consolidated and reported outward (report cards / transcripts to students and guardians), carried across years by an annual year-transition (rollover/promotion) that advances the population and preserves the record. *(Remove → a static enrollment registry; remove the year-transition → a term-scoped tool with no institutional memory.)*

Jointly-held load-bearing:

- 1 alone = people/CRM database
- 2 alone = academic catalog / org structure
- 3 without 1+2 = free-floating attendance/grade sheets
- 1+2 without 3 = enrollment registry with no operations
- 1+3 without 2 = class-record tooling with no school structure (commercial/tutoring class-management territory)
- 2+3 without 1 = timetable machinery with nobody in it

### Level 1 — Common Mature Structure

Present across the sample (Layer B), expected in any modern product, not definitional:

- Timetable / class scheduling (display at minimum; auto-scheduling in several)
- Fee collection & billing (fee structures, invoices, receipts, defaulter tracking, online payment) — depth varies by market
- School↔home communication (announcements, SMS/email/app notifications)
- Parent/guardian portal + student portal (web + mobile)
- Report cards / transcripts generation and publication
- Admissions / application intake (module here, separate product there)
- Behavior/discipline notes; health/medical data
- Roles & permissions (admin / teacher / student / parent + specialized staff roles)
- Reporting/analytics; multi-school/district scale; mobile apps

### Level 2 — Variant / Optional Structure

- **Market packaging**: international "school ERP" (fees + HR/payroll + transport + hostel + library bundled) vs US district "SIS + ERP" (student record in one product; finance/HR/enrollment/communications in connected separate products) vs open-source school platform
- **Regional machinery**: state/statutory reporting (US/regulated markets); transport w/ GPS and hostel/dorm (South Asia, boarding schools); food service/meal funds (US); biometric/RFID attendance
- **Segment**: public/district (no fees, state reporting) vs private/international (admissions-driven, fee-driven) vs faith-based vs online schools vs adult/language schools
- **Deployment**: cloud SaaS vs self-hosted vs open-source
- **Scale**: single school vs multi-school group vs district

### Level 3 — Vendor-specific (kept out of the final document)

- Fedena: "Connect Exam" final-grade feature; course/batch model; CCE/ICSE/CWA/GPA/CBSE grading presets; master particulars; branded school apps; OEM/custom-ERP program
- QuickSchools: Orchestra master scheduler; report creator app-store item
- Gibbon: Smart Blocks; Crowd Assessment; SEN/academic/behavioural/medical alert system; houses; Data Updater queue; "sound an alarm"; value-added scores from Formal Assessment
- PowerSchool: PowerTeacher Pro; Ed-Fi/1EdTech certifications; "Connected OS" framing; Allovue/SchoolMessenger/Naviance product names
- Skyward: Qmlativ platform; Family Access; icon vocabulary as domain evidence

## Rejected Findings (not promoted)

- **"School management = fees + transport + hostel + library + HR"** — rejected as definitional. This is the international school-ERP packaging (Fedena-strong). US district SIS products (PowerSchool, Skyward) run schools without bundling transport/hostel, and keep deep finance/HR in separate ERP products. Held as variant.
- **"School management = SIS + ERP suites"** (Skyward shape) — rejected as definitional; it is one packaging of the same operations.
- **"The student database is the centerpiece"** (QuickSchools' own framing) — partially rejected as the *sole* center: it describes the SIS-pole emphasis. In the school-management pole the school's *operations* (fees, timetable, communication) are co-equal. The student record is the spine, the operations loop is the job.
- **"Automated conflict-free scheduling"** — common mature capability, not definitional (Gibbon's core Timetable renders/inputs; generation depth varies).
- **"Biometric/RFID attendance"** — regional implementation detail.
- **"State reporting"** — regulated-market machinery, not definitional (Gibbon serves refugee/home schools with none).

## Boundary Findings

### 1. vs Student Information System / SIS (§23 sibling, UNPROCESSED) — NEAR-OVERLAP / NAMING-TRADITION SPLIT — flag for joint review

Evidence that the two names cover one heavily-overlapping population:

- Fedena sells ONE product under both names (root = "School Management Software & School Management System"; separate page = "Student Information System SIS"; vendor text: "By bringing the SIS & ERP feature under the same brand…").
- QuickSchools: "Online School Management Software" whose hero bullets include "Powerful Student Information System (SIS)".
- Skyward: page titled "K-12 School Management Software"; content = "Student information system and school ERP"; Capterra category "Skyward School Management".
- Gibbon: testimonials call the same platform "school management software system" and "sistema informativo scolastico".
- PowerSchool: names its product "SIS" and treats school-management-adjacent operations (enrollment, communications, finance/HR) as separate connected products.

Reading (Layer C): "School Management System/Software" and "SIS" are two naming traditions over the same K-12 administrative-software population — "school management" the broader umbrella (whole-school operations incl. money/logistics/staff/communication), "SIS" used both as a synonym (Fedena, QuickSchools) and as the narrower student-record product name (PowerSchool; Skyward's SIS suite beside its ERP suite). This pass keeps both directory leaves and documents School Management System as the **whole-school-operations-centered** realization; the proposed seam for the SIS pass's joint review: **center of gravity** — the student's official record (identity, enrollment, academic history, statutory reporting) vs the school's whole administrative operation (record + money + logistics + staff + communication). Products span both; center of gravity decides. Consistent with the higher-education-administration pass, which already recorded a SIS near-overlap note and a "vs School Management (level shapes)" seam.

### 2. vs Higher Education Administration System (§23, processed) — level shapes

K-12 school shape: age-based grade levels, classes/form groups as attendance-and-pastoral units, guardians as first-class actors, term/annual fee machinery, promotion through year groups. Higher-ed shape: programs/credentials, credit courses/sections, adult students as their own account holders, registration machinery. The higher-ed pass recorded "vs School Management (level shapes)" — confirmed from this side. Boundary holds.

### 3. vs Learning Management System / LMS (§23, processed) — administration vs teaching

LMS delivers teaching inside rostered course containers and produces the assessed-performance record handed to the official record; the school management system administers the school (people, structure, attendance, fees, communication) and consumes/produces official records. Hand-offs documented: LMS pass ("roster-in/grades-out"); Gibbon ships a Moodle-connection guide (integration seam from this side). Boundary holds.

### 4. vs Parent Portal (§23, processed) — layer split

Parent portal = the guardian-facing access layer over the school's records (guardianship-derived access, school-governed disclosure). School management system = the staff-side system of record those records live in. The parent-portal pass documented the portal as shipping "overwhelmingly as the parent-facing layer of an SIS product" — consistent: the portal is a surface of this Type's record base, kept a separate leaf on users/access-model grounds. Boundary holds.

### 5. vs capability-slice siblings (§23): Student Attendance System, Digital Gradebook, Academic Timetabling, Student Billing System, Admissions Management, Student Behavior Management, Special Education Management, Transcript Management

Each is a capability slice that ships as a module inside a school management system and also exists as a standalone specialist Type. The school management system is the integrating whole: it holds the population and structure the slices operate on. Evidence: every sampled product contains attendance + gradebook + scheduling + fees + admissions as modules (comparison table). Boundary: slice Types center their own loop (e.g., digital-gradebook pass: "term working ledger feeding final grades"; timetabling pass: "constructs institution-side supply"); the school management system centers the school. Boundary holds; the slices' passes should confirm.

### 6. vs commercial class-management siblings (§28/§29 processed): Dance Studio, Martial Arts School, Childcare/Daycare/After-school, plus unprocessed Swim/Gymnastics

The dance and martial-arts passes recorded "vs School Management/SIS (commercial studio vs institution records)". Confirmed from this side: the commercial siblings run a business (family accounts, memberships/tuition for scheduled classes, attendance, progression) **without school-of-record semantics** — no grade levels/promotion through an institutional structure, no official academic record/transcripts, no institutional enrollment statuses. The religious-education pass flagged the same seam ("full-time parochial schools/madrasas are school territory"). Boundary holds; watch-item for swim/gymnastics passes.

### 7. vs School ERP framing — packaging variant, not a separate Type

"School ERP" (Fedena's term) = this Type with deeper back-office bundling (HR/payroll/finance/assets). ERP-ness is a packaging/market variant. No separate directory leaf exists; no action.

### 8. Naming-tradition note (no directory change)

A third regional naming tradition exists for the same population — UK/state-system "Management Information System (MIS)" — noted as general market context; not directly evidenced in this sample's fetches, so held as a low-strength naming observation only.

## Historical / Market-Sample Check

- **Paper-era school office**: admission register, class registers/roll books, timetable board, mark sheets/report cards, fee ledger, staff records — satisfies all three L0 structures with no software machinery (the operational loop ran on paper; the year-transition was the annual promotion). The definition names no portals, SMS, apps, biometrics, or cloud. **Passes.**
- **1980s–90s desktop school-administration generation** (school-office software holding student records, scheduling, attendance, grades on a local machine): satisfies the core with no internet/portals. Asserted generically (generation-level reasoning, no specific product fetched). **Passes.**
- **Regional products** (Indian/SEA school ERP; UK MIS tradition; open-source platforms): all realize the same people+structure+operations core with different packaging. **Passes.**
- Anti-overfit check per the shared-implementation rule: fees (universal in the fee-charging sample but absent/shallow in public-education poles), transport/hostel (regional), state reporting (US), portals/apps (era-current) — all held OUT of the defining core.

## Uncertainties

1. **SIS seam** — the single largest uncertainty; resolved only jointly with the SIS pass. This pass's evidence shows synonym usage (Fedena, QuickSchools) AND narrower-product usage (PowerSchool, Skyward suites). Flagged in STATUS.md.
2. **Classter unreachable** (403 ×2) — a prominent "all-in-one school management" vendor is unsampled; the international all-in-one pole rests on Fedena + QuickSchools + Gibbon. Assertion strength for "all-in-one is the dominant international packaging" held moderate.
3. **Operational depth** — Tier-1 operational docs only for Gibbon; Fedena/QuickSchools/PowerSchool/Skyward evidenced at product-page/feature-page level. No numeric limits, defaults, or precise workflow parameters asserted anywhere in the final document.
4. **UK MIS naming** — general market context, not directly evidenced; held as low-strength observation.
5. **Public/district fee machinery** — US district SIS products show fees/food-service payment surfaces (PowerSchool app payments; Skyward Fee/FoodService icons) but deep student-financials machinery in the district market may differ from the international fee-invoicing loop; held as variant, not asserted further.

## Final Synthesis

A **School Management System** is the school's whole-administration system of record. Its defining core is three jointly-held structures: the school's population of record (students linked to guardians, plus staff), the school's academic structure of record (school years/terms, grade levels, classes/sections — with enrollment binding each student into the structure for a year), and the school's operational loop over that population and structure (daily attendance and academic-outcome recording, consolidated into report cards/transcripts reported to families, carried across years by an annual rollover/promotion). Around that core, mature products add the timetable, fee collection, school↔home communication, guardian/student portals, admissions intake, behavior and health notes, and role-based access for admins, teachers, students, and parents. The Type's market realizes three packaging shapes of one population — international school ERP (everything bundled), US district SIS+ERP (record product + connected operations products), and open-source school platform — and shares that population with the directory's SIS leaf under two naming traditions; the seam (student-record center vs whole-school-operations center) is flagged for joint review with the SIS pass.
