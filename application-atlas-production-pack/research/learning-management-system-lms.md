# Research Notes — Learning Management System / LMS

## Research Goal

Understand what an education-sector Learning Management System (LMS) is as an Application Type: what its defining structure is, how teaching actually flows through it, which capabilities are standard versus optional, and where its boundaries sit against the many sibling Types in directory section 23 (SIS, Virtual Classroom, MOOC Platform, Curriculum Management, Assignment Management, Assessment/Examination, ePortfolio, eLearning Authoring Tool, Educational Content Platform, LXP) and against Corporate LMS in section 09.

## Initial Boundary

The directory contains both "Learning Management System / LMS" (§23 Education) and "Corporate LMS" (§09 HR). Prior passes already established:

- corporate-lms pass: education LMS is "same engine, different frame" (students/terms/grades/transcript vs employees/jobs/compliance/HR file); keep-both ratified from that side.
- assignment-management pass: LMS is "the broader container" — assignment management is one loop inside it.
- assessment-platform pass: LMS centers course delivery with quiz engines as capability slices.
- examination-platform pass: LMS centers course content + gradebook; exam occasion is the other Type's whole product.
- curriculum-management pass: LMS delivers the live section-level course; curriculum management governs the course across terms with no learner-facing delivery.
- eportfolio-platform pass: LMS is course-centered; ePortfolio centers the learner-owned cross-course evidence record.
- classroom-management pass: LMS hosts courses/content over time; classroom management operates the live class.
- student-information-system-family passes: LMS delivers instruction and assesses learning; the SIS keeps the official student record; roster/grade data flows between them.
- elearning-authoring-tool pass left a flag: when processing LMS, apply the "publishable-deliverable / full-authoring-environment" test to the authoring/LMS seam.
- learning-experience-platform-lxp pass: LXP's content model reduces to "org-authored course catalog — the plain-LMS content model" when the learner-directed layer is removed.

Working hypothesis: the education LMS is a course-centric teaching platform — persistent course containers, rostered students, teacher-assembled course delivery, and a per-student assessed-performance record (gradebook) that feeds the institution's official record.

## Research Questions

1. What exactly is "a course" inside these products — what does the container carry?
2. How do students get into a course (rostering, SIS sync, self-join, codes, invitations)?
3. How does a teacher build a course (content types, organization, packaging imports)?
4. How does the assessment loop work (assignments, quizzes, submissions, attempts)?
5. How does grading work (gradebook structure, categories/weights, posting/hiding, audit)?
6. What is the course lifecycle (unpublished → available → concluded; term rollover, copy/import)?
7. What roles exist (teacher/student/TA/designer/observer/admin/guest) and what do they gate?
8. What is the record's downstream consumer (transcript via SIS grade passback)?
9. What is common mature structure vs variant vs vendor-specific (modules, LTI, analytics, outcomes, AI)?
10. Where do the boundaries hold, and does the definition survive historical/older/regional products?

## Representative Products

Chosen for market representation, documentation depth, product philosophy spread, and client-level spread:

| Product | Vendor | Frame | Why sampled |
|---|---|---|---|
| Canvas LMS | Instructure | SaaS, higher ed + K-12 (+ business/gov tiers) | North-American #1 (vendor-claimed); best-documented (API + full instructor guide) |
| Blackboard Learn | Anthology | Enterprise incumbent, higher ed + K-12; Ultra (current) + Original (legacy) views | Historical lineage anchor; full help center accessible |
| D2L Brightspace | D2L | Cloud SaaS, K-12 → higher ed → corporate | Third object-model data point via official API reference |
| Moodle | Moodle Pty (open source) | Self-hosted / open source, global, 2002-era lineage | Historical/regional check anchor — **docs unreachable, see limitations** |
| Google Classroom | Google | Free lightweight classroom layer for K-12/Google-schools | Lightweight pole / boundary case — **docs unreachable, see limitations** |

## Sources

Directly fetched (2026-09-08):

- Canvas LMS REST API Documentation — Courses (objects: Course, Term, Enrollment, CourseProgress; workflow_state unpublished/available/completed/deleted; SIS fields; grade_passback_setting) — https://canvas.instructure.com/doc/api/courses.html
- Canvas Instructor Guide (category index: Announcements, Assignments, Attendance (Roll Call), Calendar, Chat, Collaborations, Commons, Conferences, Course Analytics, Course Import Tool, Course Navigation, Course Pacing, Courses and Sections, Dashboard, Discussions, External Apps (LTI), Grades, Groups, Inbox, Modules, New Quizzes, Outcomes, Pages, People, Portfolios, Quizzes, Rich Content Editor, Rubrics, Settings, SpeedGrader, Enhanced Rubrics, Improved Outcomes Management) — https://community.canvaslms.com/t5/Instructor-Guide/tkb-p/instructor (index saved in tool output)
- Instructure product page — Canvas positioning, tiers (K-12 / higher ed / business & government), non-negotiables, SpeedGrader/Gradebook/Blueprint/mobile apps (Student/Teacher/Parent), ecosystem partners (Turnitin, BigBlueButton, Google/Microsoft, Inspera, FeedbackFruits), Studio/Catalog/Career add-ons — https://www.instructure.com/canvas
- Blackboard Learn help center (Ultra + Original) — full navigation: Course and Content Management (set-up, course roles, enrollment, content types, SCORM packages, content market, learning modules, content release conditions, content collection, course copy/export/import), Interact with Students (roster, messages, discussions, announcements, groups, journals, email, Google Meet, badges), Assessments (assignments, tests, forms, question types, question banks/pools, QTI, proctored, access codes, time limits), Grading (gradebook, grade calculation, categories/columns/schemas, attendance, accommodations, rubrics, anonymous/delegated/parallel grading, grade history, offline grade work, Grade Export/Grades Journey), Plagiarism (SafeAssign, Turnitin), Migration (terminology maps from Canvas/D2L/Moodle), Analytics (course activity, goals, Blackboard Outcomes), Original course view (organizations, blogs, wikis, portfolios) — https://help.blackboard.com/Learn/Instructor/Ultra/Course_Content (nav tree)
- D2L Brightspace Developer Platform — API reference contents: org units (departments, semesters), enrollments and auditors, course offerings and templates, course content, dropboxes, grades, quizzes, surveys, assessments and rubrics, groups and sections, release conditions, news, calendar, learning outcomes, course competencies, intelligent agents, learning repository objects, LTI Advantage/legacy, ePortfolio objects, IPSIS SIS-integration, accommodations — https://docs.valence.desire2learn.com/reference.html (and /index.html)

Indirect official evidence for unreachable vendors:

- Canvas Instructor Guide: "How do I import content from Moodle into Canvas?", "...from Blackboard 6/7/8/9/Ultra...", "...from Desire 2 Learn (D2L)...", "How do I import content from Common Cartridge into Canvas?" — confirms these products expose course packages whose content maps into Canvas courses.
- Blackboard help: "Migrate from Moodle", "Migrate from D2L Brightspace", "Migrate from Canvas" with per-vendor terminology mapping tables — confirms course/content/grade vocabulary across the four products is mappable.

Unreachable (network rules applied, abandoned after failures):

- Moodle: docs.moodle.org (403 ×2), moodle.org (403 ×1).
- Google Classroom: support.google.com (timeout), developers.google.com (timeout).

## Product Observations

### Canvas LMS (Instructure) — evidence layer A

Object model (API): **Course** carries id/name/course_code, SIS id, workflow_state (`unpublished → available → completed → deleted`), account, **enrollment_term**, grading standard, syllabus body, default view, enrollments. **Enrollment** links user ↔ course with type `teacher / student / ta / observer / designer` and state `active / invited_or_pending / completed`. **Sections** subdivide a course (cross-listing supported). **CourseProgress** is computed from module `requirement_count` / `requirement_completed_count`. SIS integration is first-class: `sis_course_id`, SIS Imports resource, `grade_passback_setting` (e.g. nightly sync). Grading machinery: assignment **groups** (weightable), **grading periods**, **grading standards/schemes**, late policy, moderated grading, rubrics, what-if grades, custom gradebook columns, gradebook history, grade change log.

Instructor surface (guide): course home/navigation (configurable default view: modules / assignments / syllabus / activity feed); **Modules** (items of any content type, prerequisites, requirements, lock-until-date, assign to sections/tags/students, mastery paths conditional release); **Pages, Files** (rich content editor); **Assignments** (types, due vs availability dates, attempts, differentiated assignment to individuals/tags/sections, anonymous grading, moderated multi-grader, peer review, extra credit, SCORM import as assignment, external-app assignments — Google Assignments LTI, cloud docs, SIS submission); **Quizzes / New Quizzes** (question banks, groups/randomization, QTI import); **Grades** (gradebook: grading periods, filters, total column, non-submission columns, notes column, posting policies — post/hide manually or automatically, inactive/concluded enrollments visible); **SpeedGrader** (submission-by-submission grading with annotation); **Announcements, Discussions** (graded discussions, group discussions, analytics), **Inbox** (course-bound messaging), **Calendar, Dashboard/To-do**; **People** (add users, resend invitations, context cards, last-attendance, section restriction, roles, differentiation tags); **Groups** (student groups); **Attendance (Roll Call)**; **Conferences** (in-course web conferencing); **Collaborations** (Google/Microsoft docs); **Outcomes** (course/institution outcomes, mastery); **Rubrics**; **Commons** (cross-institution shared content repository); **Course Import Tool** (copy course, import from Moodle/Blackboard/D2L/Angel, Common Cartridge, QTI; date shifting on import); **Settings** (course-level feature toggles); **Course Analytics** (activity, submissions, grades; message-students-who); **Portfolios** (adjacent). Product page: three tiers (K-12/higher-ed/business-gov), Blueprint-style scaled curriculum positioning, Canvas for Elementary (Homeroom/Subjects), Parent app (observer posture), Studio/Catalog/Career add-ons, 1000+ LTI partners (Turnitin, BigBlueButton, etc.).

State/lifecycle evidence: publish/unpublish course and items; conclude course at term end; delete. Term structure via enrollment terms. Blueprint courses: master → child sync with locked objects (product-specific branding of the template-course concept).

### Blackboard Learn (Anthology) — evidence layer A

Two product generations in one product: **Ultra** (current) and **Original** (legacy) course views, with a migration/terminology section connecting them. Ultra surface: course set-up (banner, roles, settings, **enrollment management**, student preview); content types (documents, files, **SCORM packages**, content market [Cengage/McGraw-Hill/Macmillan/Kaltura], course links, web links, video studio, learning object repository, eReserves); **learning modules** as content containers; **content release conditions**; batch edit; copy from other courses; export/archive and import course packages; institution-level **Content Collection** file repository with permissions/metadata/reusable-objects catalog. Interaction: roster, student overview, messages, announcements, discussions (graded, group, analytics), journals, groups, email, Google Meet integration, badges/achievements. Assessment: **assignments, tests, forms**; settings (due date, prohibit late submissions, attempts, grading & submission options, access code, **proctored assessments**, location restriction, time limit, collect submissions offline); question types (essay, MC, matching, calculated, hotspot, etc.); question banks/pools, QTI import, align questions to goals. Grading: **Gradebook** (items, categories, overall/total/calculation columns, grading schemas, extra credit); **attendance** as gradebook item; **accommodations** (course- and item-level); rubrics; **anonymous / delegated / parallel grading with reconciliation**; attempt logs; Bb Annotate inline grading; override grades; submission receipts; post/hide grades; offline grade work (download/upload, grade history); **Grade Export / Grades Journey** — approve and submit grades to the SIS. Plagiarism: SafeAssign, Turnitin. Analytics: course activity, student activity log, goals, Blackboard Outcomes (key assessments, mastery calculation). Legacy Original view adds: organizations (non-credit/non-course containers), blogs, wikis, self-and-peer assessment, portfolios, surveys, guest and observer access. Observer role for parents; course roles list.

### D2L Brightspace (D2L) — evidence layer A (API-level)

Org model: **org units** typed as departments, **semesters**, course offerings; **course offerings and templates** (template = master content course; offering = the taught instance); **enrollments and auditors**; groups **and sections**. Course machinery: **content** (topics/modules), **dropboxes** (assignment submission), **quizzes**, **surveys**, **grades** (grade objects/values), **assessments and rubrics**, **release conditions** (rule-based content release), **news** (announcements), calendar, course checklists, course updates. Pedagogy layer: **learning outcomes**, **course competencies**, intelligent agents (rule-driven automation/messaging). Content reuse: **learning repository objects** (institutional shared content). Interop: LTI Advantage and legacy LTI. Adjacent: ePortfolio object suite (artifacts/reflections/collections/presentations). Accommodations as user-level data. **IPSIS** SIS-integration configuration.

### Moodle — evidence layer B (indirect, degraded)

No official surface reachable. Indirect official evidence: both Canvas ("import content from Moodle") and Blackboard ("Migrate from Moodle" + terminology map) document course-to-course content migration from Moodle, implying the same container vocabulary (courses with content/activities and grades) that all migration machinery targets. No operational claims made; Moodle serves as the open-source/self-hosted, 2002-era lineage check and is known in-market as a full LMS (courses, activities, enrolments, gradebook), but those specifics are treated as background knowledge, not asserted with precision.

### Google Classroom — evidence layer B (indirect, degraded)

No official surface reachable (support + developer hosts timed out). Market-positioned as a free lightweight classroom platform layered on Google Workspace for Education for K-12; included as the lightweight pole and boundary case. No operational claims made for it in this pass beyond its recognized market position.

## Cross-product Comparison

| Structure | Canvas | Blackboard | Brightspace | Assessment |
|---|---|---|---|---|
| persistent course container | Course (+ Sections) | Course (Ultra/Original views) | Course offering (+ template) | **universal — A evidence ×3** |
| identified rostered participants per course | enrollments: teacher/student/ta/observer/designer; state active/invited/completed | enrollment management; course roles; observer | enrollments and auditors; roles | **universal — A ×3** |
| teacher-assembled course content | Pages/Files/RCE; Modules | documents/files; learning modules; content collection | content topics; learning repository | **universal — A ×3** |
| structured organization of content | Modules (prereqs, requirements) | learning modules + release conditions | modules + release conditions | universal as *concept*; "modules" as common implementation |
| assignment/submission machinery | Assignments (+ online submission, attempts) | Assignments (+ Bb Annotate, offline) | Dropboxes | **universal — A ×3** |
| quiz engine | Quizzes/New Quizzes; banks; QTI | Tests; question banks/pools; QTI | Quizzes; question library (market-known) | **universal — A ×3** |
| per-student grade record (gradebook) | Gradebook; categories/weights; posting policies; history | Gradebook; categories/columns/schemas; grade history | Grades (objects/values) | **universal — A ×3** |
| grading depth features | anonymous, moderated, peer review, rubrics, accommodations (guide) | anonymous/delegated/parallel + reconciliation, rubrics, accommodations | rubrics/assessments; accommodations (API) | common mature — A ×3 |
| communication layer | announcements/discussions/inbox/calendar | announcements/discussions/messages/journals | news/discussions/calendar | universal — A ×3 |
| course lifecycle + reuse | publish/unpublish/conclude; copy/import/export; blueprints | available/unavailable; copy/export/archive/import | offering vs template; semester org | universal — A ×3 |
| institutional integration | SIS imports, grade passback, SSO | Grades Journey → SIS, SSO | IPSIS SIS integration | universal — A ×3 |
| external tool interop | LTI (EduAppCenter, 1000+ partners) | content market + LTI | LTI Advantage/legacy | universal — A ×3 (LTI as common implementation) |
| integrity tooling | Turnitin-class partners | SafeAssign + Turnitin | (market-known integrations) | common |
| web conferencing in course | Conferences (BigBlueButton) | Google Meet integration | (Virtual Classrooms, market-known) | common |
| outcomes/competency mastery | Outcomes + mastery | goals + Blackboard Outcomes | learning outcomes + competencies | common (deeper in higher-ed deployments) |
| conditional/adaptive release | Mastery Paths; requirements | release conditions | release conditions | common |
| content sharing repository | Commons | learning object repository / reusable objects | learning repository | common |
| attendance as graded item | Roll Call | attendance in gradebook | (market-known) | common |
| template/master course → child sync | Blueprint courses | (course copy; Original structures) | course templates | common concept, vendor naming varies |
| ePortfolio adjacency | Portfolios (adjacent surface) | portfolios (Original) | ePortfolio object suite | adjacent — the separate Type |
| non-course containers | (groups/homerooms) | organizations | departments | common |
| parent/observer visibility | observer enrollment + Parent app | observer role | auditors | common in K-12-heavy deployments |
| AI assistance (era-current) | IgniteAI (summaries, translations, smart search) | AI Design Assistant, AVA | (era-current, market-known) | era-current layer, not definitional |

## Abstraction Hierarchy

### L0 — Defining Invariant (candidate)

Three structures held jointly:

1. **The course as the managed container of record** — a persistent, individually identified course site (typically course/section × term) staffed by a teacher and populated by identified students whose enrollment in that course is maintained as state under institutional/teacher control (rostered from registration systems, added by teacher/admin, or governed self-join by code — not open discovery at internet scale). Remove → a class-roster/section tool or nothing managed.
2. **In-course teaching delivery** — the course's teachers (or designers) assemble and publish the teaching material and learning activities inside that container for the enrolled students: documents/pages/media, organized structure, embedded external material, plus course-scoped interaction spaces. Remove → a course content website/library.
3. **The assessed-performance record in the course** — student work is collected and evaluated within the course (assignment submissions, quiz attempts, offline/observed work entered), and the resulting grades/feedback accumulate into a per-student, per-course grade record (the gradebook), which is the record the institution's official record (transcript) is fed from. Remove → a content site with no learning record; remove the course binding → standalone assessment/gradebook tooling.

Jointly-held load-bearing tests:
- 1 alone = roster/section management (SIS-lite), no teaching, no record.
- 2 without 1+3 = course website / content library.
- 3 without 1+2 = gradebook/assessment tool (the Digital Gradebook / Assessment siblings).
- 1+2 without 3 = a course site with material but no evaluated learning — not recognized in the market as an LMS.
- 1+3 without 2 = roster + grades with nothing taught — SIS + gradebook.

### L1 — Common Mature Structure

- sections within course; term/calendar anchoring (enrollment terms, semesters)
- structured content organization: modules/learning modules/topic sections; requirements, prerequisites, release conditions (conditional/adaptive release)
- in-product authoring (rich content editors) + file/document pages; course links
- package interop: SCORM (import), QTI (quiz import), Common Cartridge / course copy / export-archive-import between systems
- quiz engine depth: question types, banks/pools, randomization, attempts, time limits, accommodations
- grading depth: categories, weighting, grading periods, schemas, extra credit, drop rules (market-known), posting/hiding policies, grade history/audit, offline grade work, override grades
- rubrics; peer review; anonymous/delegated/moderated grading
- attendance as gradebook item
- communication: announcements, discussions (gradable), course-bound messaging/inbox, course calendar
- groups (student work groups); group assignments/discussions
- roles: teacher/instructor, student, TA, designer, observer, admin, guest; section-scoped interactions
- course lifecycle: unpublished/draft → available → concluded/archived; term rollover; course copy; blueprints/templates
- SIS integration: roster in, final-grade passback out; SSO
- LTI/external tools; plagiarism/academic-integrity integrations; in-course web conferencing
- outcomes/competencies (mastery); course and student analytics
- shared content repositories (Commons / learning object repositories)
- mobile apps (student/teacher/parent); accessibility; multi-language

### L2 — Variant / Optional

- sector packaging: K-12 (parent portals, elementary homeroom/subject frames), higher ed (term/section machinery, outcomes), business/government re-use of the same engines
- delivery posture: supplement to face-to-face, blended, fully online (official Canvas framing of this spectrum)
- deployment: SaaS multi-tenant vs open-source self-hosted (Moodle pole)
- mastery/competency-based-education packaging; video platform add-ons; course-catalog/continuing-ed storefronts; non-degree/career learning
- proctored assessments, access codes, location restriction; offline submissions; moderated exam machinery
- AI-era layers: AI design assistants, AI summaries/translation/search (era-current, all sampled vendors ship something)
- monetization/packaging: tiered editions, add-on modules

### L3 — Vendor-specific (research notes only)

SpeedGrader; Blueprint Courses; Commons; Mastery Paths; IgniteAI; Canvas for Elementary Homeroom/Subjects; Studio; Catalog; Canvas Career; Portfolium. Blackboard: Ultra vs Original views; Bb Annotate; Grades Journey; SafeAssign; AVA; AI Design Assistant; Content Market; Content Collection; Blackboard Outcomes/Key Assessments; Examity proctoring integration. Brightspace: Dropboxes; News; Intelligent Agents; Learning Repository; Auditors; IPSIS; course offering/template split. Moodle: (unreachable — plugin/activity ecosystem and enrolment methods known in-market but not asserted here).

## Historical / Market-Sample Check

The L0 is deliberately free of: SCORM/LTI (1990s-2000s standards), cloud/SaaS, modules-as-named-objects, outcomes/mastery, analytics, AI, mobile, parent portals. A late-1990s/2000s-generation LMS (course shell per term, rostered students, content areas/materials, assignments/tests, gradebook, announcement/discussion boards) satisfies all three legs. Open-source self-hosted and regional/heritage products satisfy the same core. The thin ancestor — an institution's public course web pages plus email — fails leg 1 (no managed rostered container) and leg 3 (no learning record). Course mailing lists fail the same way. The definition survives the historical check.

## Vendor-specific Findings

See L3. Notable: Brightspace's "Dropboxes" for assignments and "News" for announcements, and its explicit offering/template split; Blackboard's dual-generation product (Ultra/Original) with an in-product migration surface and vendor-published terminology maps from Canvas/D2L/Moodle — strong market evidence that all four products share one course/content/grade structure; Canvas's Commonsis a cross-institution shared-content marketplace (unique in the sample); Canvas's `grade_passback_setting: nightly_sync` and Blackboard's Grades Journey both show SIS grade hand-off as an approved administrative act.

## Boundary Findings

- **SIS**: the LMS consumes rosters and returns final grades; the SIS keeps the official student record (registration, transcript). Remove rostering + official record from the SIS side, or remove delivery/assessment from the LMS side — each Type survives without the other's core. Hand-off points (SIS imports, grade passback/approval) are documented in all three deep samples.
- **Corporate LMS**: same engine (container, enrollment link, record), different frame — population (students vs employees), record consumer (transcript vs HR/compliance file), pedagogy owner (academic staff vs L&D), calendar (terms vs compliance cycles). Several vendors sell the same engine into both frames. Keep both Types; the directory alias question (LMS vs Corporate LMS vs Employee Learning Platform) is already recorded from the corporate-lms pass.
- **MOOC Platform**: remove institutional enrollment control (open self-service at internet scale, learner-directed, certificate-oriented) → MOOC/content-platform territory.
- **Virtual Classroom**: live synchronous teaching surface; integrates into the LMS course (documented integrations in all deep samples). Remove the persistent course container → virtual classroom.
- **Assignment Management / Assessment Platform / Examination Platform / Digital Gradebook**: each is one loop or one deep slice of the L0; established from their own passes.
- **Curriculum Management**: governs what the course *is* across terms (outcomes, mapping, approval) with no delivery; LMS delivers the live course.
- **ePortfolio Platform**: learner-owned cross-course record vs course-bound record; documented as adjacent surfaces inside LMS products.
- **eLearning Authoring Tool** (discharges the recorded flag): the publishable-deliverable test — LMS-native building creates objects that live inside and are delivered through the course container; authoring tools produce portable standards packages (SCORM/QTI) whose purpose is delivery *elsewhere*. LMS products are heavy importers of those packages (documented: SCORM assignments, QTI imports, Common Cartridge, cross-vendor course imports). LMS products bundling full authoring environments are a packaging gradient, not a Type merge. Boundary holds.
- **Educational Content Platform**: content without rostered courses/graded records.
- **Classroom Management**: live class operations; hosts no content (established from its pass).
- **Institutional Effectiveness / Accreditation**: LMS is an assessment-results substrate feeding those systems (established from their passes).

## Uncertainties

- Moodle and Google Classroom official documentation was unreachable; claims about them are held at market-recognition level with no operational precision. Moodle's structural role was corroborated only indirectly (vendor migration/interop documentation).
- Precise numeric limits (file sizes, question counts, enrollment caps), default values, and exact state-name sets are intentionally not asserted beyond what was directly fetched (Canvas API state lists are the only exact-state claims).
- Market-share claims (e.g. "Canvas is #1 in North America") are vendor positioning, kept out of the canonical document.
- Corporate-frame LMS products (Brightspace, Moodle, Canvas) blur the education/corporate boundary commercially; the two-frame split is conceptual, and edge products (association LMS, CE-credit LMS) sit on the seam with Certification Management (established from that pass).

## Final Synthesis

The education LMS is the institution's course-teaching platform of record. Its defining core is three jointly-held structures: the course container with institution-controlled rostered participants; in-course teaching delivery assembled by the course's teachers; and the per-student assessed-performance record (gradebook) that accumulates inside the course and feeds the institution's official record. Everything else the market associates with LMS — modules, LTI, analytics, outcomes, AI, parent apps, mastery paths — is standard mature structure or variant layering on that core. The definition passes the historical check (1990s-generation products satisfy it) and the cross-frame check (the same engine re-instantiates as Corporate LMS with a different population and record consumer).
