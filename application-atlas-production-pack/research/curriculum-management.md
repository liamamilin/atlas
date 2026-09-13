# Research Notes — Curriculum Management (§23 Education, Research & Knowledge Institutions)

Research date: 2026-09-07

## Research Goal

Understand what "Curriculum Management" means as an Application Type: what real products in
this category actually manage, what the core objects and workflows are, and how the Type
differs from the adjacent education leaves that share its vocabulary (SIS, Course
Registration, Academic Timetabling, LMS, Academic Accreditation Management, Institutional
Effectiveness Platform, Lesson Planning Application).

Working hypothesis at start: a curriculum management application is the institution-side
governance system for what the institution teaches — it maintains the structured curriculum
(programs, courses; units, lessons), routes changes through committee-style approval, and
publishes the approved curriculum as the institution's reference (catalog / curriculum site),
feeding downstream systems.

## Initial Boundary

- The leaf sits between the SIS (student/records system of record) and the LMS (delivery of
  live courses). Prior sibling passes already reference it:
  - research/academic-accreditation-management.md: "vs §23 Curriculum Management (sibling) —
    curriculum management runs the curriculum change process and catalog; here curriculum
    mapping appears as *evidence* for accreditation. A curriculum product may feed this
    Type; it is not this Type."
  - research/academic-timetabling.md: timetabling consumes curriculum data (activities with
    curriculum attachment) to schedule; scheduling is downstream.
- Potential boundary problems identified up front:
  1. Could collapse into an SIS module (course master data often lives in the SIS).
  2. The K-12 market realization ("curriculum mapping / planning", e.g. Atlas) looks
     structurally different from the higher-ed governance realization — same Type or not?
  3. Catalog publishing has no separate directory leaf — does it belong inside this Type?
  4. Overlap with workflow/BPM tools (proposal + approval) that are not curriculum-aware.

## Research Questions

1. What is "the curriculum" as an object in these systems? (program, course, unit, lesson,
   learning outcome, standard, catalog)
2. What is the end-to-end governance loop? (propose → review → approve → publish → periodic
   review/revision)
3. How is versioning/effective-dating handled (effective term, catalog year, change history)?
4. What does publication look like (academic catalog, public curriculum site, marketing)?
5. What roles participate (faculty proposer, chairs, committees, registrar, catalog staff,
   curriculum director, principal)?
6. What integrations exist (SIS, LMS, degree audit, scheduling, registration)?
7. What interfaces do users actually operate (forms, workflow inboxes, catalogs, mapping
   matrices/canvases, analytics)?
8. Do the higher-ed and K-12 realizations share one defining core, or are they two Types?
9. Historical check: does pre-software curriculum governance still fit the definition?

## Representative Products

Selected for market representativeness, different product philosophies, different customer
levels, and coverage of the higher-ed governance / K-12 planning spectrum:

1. **CourseLoop** (courseloop.com) — pure-play end-to-end curriculum management platform for
   higher education (UK/AU/US; founded 2016; acquired by TechnologyOne in 2024). Modular
   philosophy: data management + governance + review + mapping + publishing as separate
   modules around one curriculum data core.
2. **Modern Campus Curriculum** (formerly Curriculog; moderncampus.com) — US higher-ed
   incumbent (claimed 325+ institutions). Workflow-first philosophy: proposal/approval
   machinery as the product's own self-definition; bundled in a "Connected Curriculum" suite
   with Catalog, Schedule, Navigate, Syllabus products.
3. **CourseLeaf CIM** (LeepFrog Technologies; courseleaf.com) — US higher-ed incumbent
   (claimed 500+ colleges/universities, two decades). Forms-to-catalog philosophy: dynamic
   SIS-integrated forms + configurable workflow + archive, inside an academic-operations
   platform (CIM/CAT/CLSS/PATH/SYL).
4. **Coursedog** (coursedog.com) — modern SaaS challenger (claimed 500+ campuses). Unified
   academic-operations philosophy: curriculum, catalog, syllabus, scheduling, assessment on
   one platform with real-time SIS sync.
5. **Atlas** (onatlas.com; Rubicon West LLC / Faria Education Group) — K-12 and international
   schools pole (claimed 6,000+ schools/districts). Instructional-planning philosophy:
   unit/lesson planning mapped to standards, with leadership review and public publication.

## Sources

All accessed 2026-09-07 unless noted.

- CourseLoop — root (module overview, positioning, customer list):
  https://courseloop.com/
- Modern Campus — Curriculum product page:
  https://moderncampus.com/products/curriculum-management/
- Modern Campus Support — Curriculum (Tier-1 product definition; links to auth-gated
  Zendesk manual): https://support.moderncampus.com/curriculum/
- CourseLeaf — root (platform/module structure): https://www.courseleaf.com/
- CourseLeaf — CIM product page (forms, workflow, SIS Sync, archive, FAQ):
  https://www.courseleaf.com/software/cim/
- Coursedog — root (platform structure, integrations, institutional case-study quotes):
  https://www.coursedog.com/
- Atlas — root (features, stakeholder journeys, publishing): https://www.onatlas.com/
- Atlas — Curriculum Creation and Review Process page (JS-gated; content not retrievable):
  https://www.onatlas.com/curriculum-creation-review-process

Failed/abandoned sources (per network rules, 1–2 attempts each):
- https://www.coursedog.com/solutions/curriculum (404); Coursedog knowledge base
  (coursedog.my.site.com — Salesforce CSS error)
- https://support.moderncampus.com/curriculog/ (404; correct path /curriculum/ found instead)
- https://www.rubicon.com/ (different company — waste services; Atlas lives at onatlas.com)
- Modern Campus Curriculum detailed user manual: auth-gated (customer Zendesk portal)
- Atlas help center (onatlas.zendesk.com): not fetched; product evidence rests on the
  official marketing site

Evidence layers used below: **A** = directly observed on an official source of a named
product; **B** = cross-product commonality; **C** = canonical inference.

## Product Observations

### Product 1 — CourseLoop (higher-ed, UK/AU/US)

Key observations (A, courseloop.com):

- Positioning: "end-to-end curriculum management… the golden thread, connecting every
  element of your curriculum, from ideation to publication"; the platform is offered as the
  "definitive source of truth" for curriculum data. Curriculum framed as "at the heart of
  every higher education institution".
- Modular product architecture (module names are vendor-specific, capabilities informative):
  - **Curriculum Data Management** — "integrity and accuracy of your curriculum data";
    single source of truth; UI screenshot described as "status of curriculum proposals".
  - **Curriculum Governance** — "dynamic workflows and automation to approve and govern
    proposals faster"; UI shows "status of proposals and tasks".
  - **Curriculum Review** — "close the loop on your quality assurance processes"; UI shows
    "status of multiple Curriculum Reviews" (periodic review cycle as a product surface).
  - **Curriculum Mapper** — "visualisation for better design and the assurance of learning";
    a "mapping canvas" for "curriculum relationships".
  - **Curriculum Publisher** — "dynamic publishing to help you bring your curriculum to
    life"; a course-catalogue UI is shown as publisher output.
  - **Curriculum Marketer** — marketing content "create[d] and approve[d]… in parallel with
    your curriculum"; "approve marketing and curriculum information in parallel, making
    promotion to prospective students low-effort and error-free".
  - **Student Study Planner** — student-facing extension: staff create drag-and-drop study
    plans; students plan learning journeys against the curriculum.
- Problem framing (evidence of what it replaces): "Spreadsheets, sticky notes, and relying
  on the know-how of individual staff members are commonplace"; disjointed curriculum data
  "reduces integration capability"; institutions want "curriculum agility" and support for
  "innovations such as micro-credentials".
- Customer base: predominantly UK/AU universities (Monash, QUT, King's College London,
  Liverpool John Moores, Queen Mary, UTS, Newcastle, Murdoch) plus UCLA.

### Product 2 — Modern Campus Curriculum (higher-ed, US)

Key observations (A, moderncampus.com + support.moderncampus.com):

- Tier-1 support-site definition: "Modern Campus **Curriculum** is a workflow software tool
  that enables your staff to review and approve milestones in the curriculum development
  process." (support.moderncampus.com/curriculum/)
- Product page: "manage every aspect of the curriculum lifecycle. From proposal submission
  to final approval"; claims of reduced manual processes, transparency, "full compliance
  with academic standards".
- Named key capabilities:
  - **Automated Curriculum Workflow** — "Manage curriculum proposals, revisions, and
    approvals with automated workflows… all stakeholders can review, comment, and approve
    changes in real-time."
  - **Centralized Curriculum Repository** — "a single source of truth for all curriculum
    data. With our centralized repository, updates are reflected across all systems."
  - **Accreditation and Compliance Support** — "built-in tools for documentation, reporting,
    and audit trails" against "institutional and accreditation requirements".
- Suite framing: part of the **Connected Curriculum suite** with Catalog ("dynamic solution
  for managing and updating program details, ensuring students have accurate and accessible
  information"), Schedule (class schedule management), Navigate (student schedule
  optimization), and a Syllabus partnership (Concourse). "Ensures that course and program
  data is always accurate and up-to-date across all student-facing platforms… from initial
  proposal to final publication."
- Users: "faculty, staff, and administrators… track proposal statuses, add comments, and
  make approvals from any device."
- Detailed user manual is auth-gated for customers — operational specifics (exact workflow
  steps, state names) not verifiable; no precise claims made.

### Product 3 — CourseLeaf CIM (higher-ed, US)

Key observations (A, courseleaf.com):

- Category definition in the vendor's own FAQ (closest to a market definition):
  "Curriculum management software, sometimes called curriculum workflow software, helps
  colleges and universities **create, review, approve, and maintain academic courses and
  programs**. It replaces manual spreadsheets, email approvals, and paper forms with
  automated workflows that improve governance, accuracy, and collaboration across academic
  affairs."
- Dynamic forms: "forms that are easy to use, configured to align with your campus policies,
  and pre-populate with content from your student information system"; departments "propose
  new courses, modify existing courses, submit forms for the right approvals, and attach
  critical documents"; "Forms automatically track and color-code edits"; conditional logic;
  typically one form per object type (one for courses, one for programs, one for
  miscellaneous curriculum items such as micro-credentials).
- Intelligent workflow: "You get to tell CIM who participates in each stage of the workflow;
  automated email alerts let them know when it's time to take action"; "users never need to
  know the right workflow for a specific course or program – CIM knows automatically"; CIM
  "recommends approval workflows when courses are added or changed".
- Impact analysis: "CIM identifies and allows you to view each department, program
  requirement, and course impacted by a proposed curriculum change."
- SIS integration: "advanced bi-directional integration… SIS Sync™ validation ensures course
  and program information remains accurate and aligned"; SSO login.
- Archive: "History is never lost with CIM; it tracks and color-codes edits and comments,
  letting you view the evolution of course development and approval and utilize historic
  content for future course and program development."
- Complexity handling named explicitly: "cross-listed courses, effective terms, reserved
  seats, multi-career courses, and learning outcomes mapping".
- Downstream framing: "Every approved course, program, and policy change influences the
  academic catalog, course scheduling, student planning and registration, degree audits,
  syllabi, and other campus systems. CourseLeaf CIM connects these processes by managing
  curriculum changes at the source and sharing approved data across the CourseLeaf platform
  and other higher education software, including student information systems (SIS), learning
  management systems (LMS), degree audit solutions, and event and room scheduling platforms."
- CIM↔catalog division of labor: "Approved program changes flow directly from CourseLeaf CIM
  to CourseLeaf CAT, while approved course changes synchronize through your student
  information system (SIS) to keep catalog content accurate."
- Platform siblings: CIM (curriculum), CAT (catalog publication), CLSS (academic scheduling),
  PATH (advising/registration), SYL (syllabi management).
- Users named in FAQ: "Faculty, department chairs, curriculum committees, registrars, and
  academic leaders."
- Extra capabilities: micro-credentials, common course numbering (state-wide systems:
  Florida, California AB 1111, Oregon SB 233, Louisiana).

### Product 4 — Coursedog (higher-ed, modern SaaS)

Key observations (A, coursedog.com — platform structure + named institutional quotes):

- Positioning: "the Intelligent Academic Operations Platform, unifying how higher ed manages
  scheduling, curriculum, catalogs, assessment, and more."
- Curriculum Cloud groups: Curriculum Management ("Accelerate Curricular Innovation"), Labor
  Market Insights ("Connect Curriculum to Careers"), Catalog & Handbook ("Connect Students to
  Courses"), Syllabus Management.
- Institutional case-study quotes (registrar/curriculum-leader voices, valuable workflow
  evidence):
  - St. Cloud State University (University Curriculum Coordinator): "flexible workflow logic
    to have certain proposals and certain requests only go to the steps needed… we're able
    to add fields into forms and the course and program templates any time we want."
  - Parker University (Senior Director and Registrar): "the Coursedog curriculum pulls
    directly out of our SIS and… it is the one place that I need to update. Now with changes
    going into a workflow, approved changes are now correct in the SIS and Coursedog for the
    catalog." Contrast with before: "the curriculum council disbursed word documents… they
    didn't always get updated in every place."
  - Pratt Institute (Registrar): "the Coursedog catalog is what the catalog should be… a
    front end to the curriculum. With everything being dated in Coursedog, we can see when a
    course is live and when it goes into the catalog, and it's already there waiting for
    us." (Direct evidence of effective-dating + catalog-as-publication-of-curriculum.)
  - Brigham Young University (Curriculum and Class Scheduling Specialist): "Coursedog is
    instantly validating our rules, and showing the conflicts… the data reports – it's live
    data."
- SIS integration list: Banner, Colleague, DegreeWorks, Ethos, PowerCampus, PeopleSoft,
  Workday Student, Jenzabar, homegrown/third-party SIS; SSO.
- Role pages: Provosts, Registrars, CIOs, Accreditation. Institution types: systems,
  community colleges, universities, liberal arts, technical/special focus.
- Vendor efficiency claims (LCCC "seven hours per change to three hours") are projections —
  not asserted as fact anywhere in the final documents.

### Product 5 — Atlas (K-12 / international schools)

Key observations (A, onatlas.com):

- Positioning: "Curriculum Management with Atlas… Develop, review, refine, analyze and share
  standards-aligned curriculum and lessons"; described as a "curriculum management and
  lesson planning platform" for schools and districts.
- Feature set: Unit Planning ("customized for your curriculum journey", "browsing your
  school-wide curriculum", "course at a glance"), Lesson Planning, Analytics, Integrations,
  Atlas AI, FariaLearn (professional learning).
- Stakeholder model (per-role journeys described by the vendor):
  - **Teacher** — builds "lesson plans based off the curriculum unit he and his team
    created"; "align his units and lessons to the standards that his school is adhering to".
  - **School Principal** — "up to date reports on the curriculum planned and delivered";
    "review and approve submitted lessons and provide feedback on the curriculum".
  - **Curriculum Director** — "review what curriculum is taught at the district level, and
    to ensure state standards are covered. The advanced analytics allows her to view the
    progression of skills between subjects and grades, as well as the gaps and redundancies
    in the curriculum."
  - **Superintendent** — "comprehensive view of district wide curriculum"; shows the school
    board "how the district curriculum is aligned to state requirements".
  - **Community/Public** — parents see "curriculum published by his school via the Atlas
    public site function… what their children are learning, when it's happening".
- Customer quotes: "customizable templates… adjustable unit calendar tool"; "curriculum
  mapping is for teachers as well as administrators. It gives teachers a plan for
  instruction and administrators the information… to know what teachers are teaching and
  assessing."
- Integrations: SSO/rostering ecosystem (Google, Office 365, Clever, ClassLink) and content
  partners; the Faria education ecosystem (ManageBac, OpenApply, SchoolsBuddy).
- The dedicated review-process page was JS-gated (no content) — the review/approve evidence
  comes from the stakeholder journeys on the main page (principal reviews/approves).

## Cross-product Comparison

| Dimension | CourseLoop | Modern Campus Curriculum | CourseLeaf CIM | Coursedog | Atlas |
|---|---|---|---|---|---|
| Segment | higher-ed (UK/AU/US) | higher-ed (US) | higher-ed (US) | higher-ed (US) | K-12 / international schools |
| Curriculum object | curriculum data core (courses/programs, relationships) | proposals & revisions over course/program records | course & program records with SIS-prepopulated forms | courses/programs synced with SIS | units & lessons mapped to standards |
| Governed change | Curriculum Governance (workflows, automation, proposal/task status) | proposal submission → final approval; review/comment/approve | configurable multi-stage workflow, alerts, recommendations | flexible workflow logic routing proposals to needed steps | principal/leadership review & approval of units/lessons |
| Source-of-truth posture | "definitive source of truth" for curriculum data | "single source of truth… updates reflected across all systems" | bi-directional SIS Sync; changes managed "at the source" | approved changes "correct in the SIS and Coursedog for the catalog" | school/district-wide curriculum browse; rostering integrations |
| Publication | Curriculum Publisher (course catalogue), Marketer for parallel marketing approval | Catalog suite product ("initial proposal to final publication") | CAT catalog fed from CIM/SIS | Catalog & Handbook ("a front end to the curriculum") | public curriculum site for parents/community |
| History/versioning | proposal/review status; review cycles | repository with audit trails | comprehensive archive, color-coded edit history | "everything… dated… when a course is live and when it goes into the catalog" | school-wide curriculum browse; unit calendar |
| Outcomes/standards | Curriculum Mapper (assurance of learning) | accreditation & compliance documentation, audit trails | learning outcomes mapping | accreditation role support; assessment cloud sibling | standards alignment; gaps/redundancies analytics |
| Impact analysis | curriculum relationships/mapping | — (not observed) | "each department, program requirement, and course impacted" | rule validation, conflicts shown | gaps & redundancies between grades/subjects |
| Users | registry/academics/IT; students as planner consumers | faculty, staff, administrators | faculty, chairs, committees, registrars, academic leaders | registrars, provosts, curriculum coordinators | teachers, principals, curriculum directors, superintendents, parents (read) |
| Notable extensions | study planner, marketer module | syllabus partnership, navigate (schedule optimization) | micro-credentials, common course numbering, cross-listing | labor market insights, syllabus management | lesson planning, AI, PD (FariaLearn) |

### Cross-product synthesis (B-layer)

- **All five** maintain structured curriculum records and route changes to them through an
  institution-defined review/approval process with tracked status.
- **All five** publish or synchronize the approved curriculum outward (catalog, curriculum
  site, SIS sync) — the approval output is always consumed by someone downstream.
- **All five** are staff-facing; students (or parents) appear only as readers of published
  output (CourseLoop Study Planner, Atlas public site), never as managers.
- **All five** connect curriculum to outcomes/standards in some form; depth varies.
- **Four of five** (higher-ed) couple to an SIS as the adjacent system of record; the K-12
  product couples to rostering/SSO instead.
- **Four of five** bundle or partner a syllabus/catalog surface adjacent to the workflow.
- Segment split: higher-ed products center on *programs/courses and catalog-year governance*;
  the K-12 product centers on *units/lessons and standards coverage*. The governance loop
  and publication loop are the same shape; the record vocabulary and downstream consumers
  differ.

## Canonical Model (C-layer synthesis)

```text
Curriculum records
  (institution's educational offering/instruction described as structured,
   governed records: programs/courses in higher-ed; units/lessons in schools)
        │  change proposed
        ▼
Curriculum change proposal
  (dynamic, institution-configured form; edits tracked against the record)
        │  routed through
        ▼
Review & approval workflow
  (institution-defined stages, roles, alerts, comments; tracked status + history)
        │  approved
        ▼
Curriculum of record
  (versioned by effective academic period; authoritative for the institution)
        │  published / synchronized
        ▼
Downstream consumers
  (academic catalog, public curriculum site, SIS, scheduling, registration,
   degree audit, syllabi, parents/community)
```

### L0 — Defining Invariant

Deliberately minimal; tested against the historical check below:

1. **Curriculum records** — the institution's educational offerings/instruction exist as
   structured, maintained records inside the application (not just documents about them).
2. **Governed change** — changes to those records move through an institution-defined
   review-and-approval process, with the proposal's status tracked.
3. **Curriculum of record communicated outward** — the approved curriculum is published or
   synchronized as the authoritative version for the people and systems that consume it.

Rationale: remove (1) and the product is a generic forms/BPM tool; remove (2) and it is a
catalog/documentation tool; remove (3) and it is a task-routing tool that never lands the
change anywhere. All three together are the smallest structure every sampled product — and
the pre-software practice — exhibits.

### L1 — Common Mature Structure

- dynamic proposal forms with validation, conditional fields, and pre-population from
  existing records (SIS in higher-ed)
- configurable multi-stage workflows with alerts, comments, role-based participation,
  conditional routing, status visibility
- change tracking (diffs/color-coded edits) and a durable change history/archive
- impact analysis (which departments/programs/courses/standards a change touches)
- bi-directional SIS synchronization (higher-ed); integration with catalog, scheduling,
  registration, degree audit, LMS
- learning-outcome / standards mapping (outcome↔course; standard↔unit)
- academic catalog publication (year-versioned) or public curriculum site
- roles/permissions across proposer/reviewer/approver/administrator
- reporting, audit trails, analytics
- periodic curriculum/program review cycles (quality assurance)

### L2 — Variant / Optional Structure

- segment realization: higher-ed governance suite (programs/courses, catalog years,
  cross-listing, common course numbering, micro-credentials) vs K-12 instructional planning
  platform (units/lessons, standards coverage, district analytics, public transparency site)
- catalog depth: full dynamic catalog site vs lighter publication; marketing-content
  coordination alongside curriculum approval
- student-facing extensions (study planners); labor-market data overlays
- suite embedding (curriculum as one module of an academic-operations platform) vs
  standalone workflow tool
- syllabus management adjacency; assessment/accreditation evidence linkage
- AI assistance; professional-learning services
- institution scale features: system/state-wide common course numbering, multi-career
  courses, reserved seats

### L3 — Vendor-specific (research notes only)

- CourseLoop module names (Curriculum Marketer, Student Study Planner, Curriculum Mapper),
  TechnologyOne acquisition, UCISA award
- Modern Campus "Connected Curriculum" suite naming, Curriculog heritage, Concourse Syllabus
  partnership, claimed stats (325+ institutions, 50% approval-time reduction, 76% data
  consistency)
- CourseLeaf SIS Sync™ branding, LUC user community, LeepFrog Technologies, named state CCN
  programs (Florida, California AB 1111, Oregon SB 233, Louisiana), CourseLeaf 10 migration
- Coursedog cloud groupings (Curriculum/Scheduling/Assessment Cloud), Coursedog Intelligence,
  ClassRanked acquisition, Starchart whitepaper, institutional efficiency claims
- Atlas: Faria Education Group ecosystem (ManageBac, OpenApply, SchoolsBuddy, Pamoja),
  FariaLearn PD, IB-aligned positioning, 6,000-schools claim, Atlas AI

## Vendor-specific Findings

See L3 above. None of these belong in the canonical core. Notably, "Curriculum Marketer"
(parallel marketing approval) and "Student Study Planner" are single-vendor modules;
syllabus management appears as a separate product in three vendors (CourseLeaf SYL, Coursedog
Syllabus Management, Modern Campus Concourse partnership) and is treated as an adjacent
capability, not part of the defining core.

## Boundary Findings

1. **vs Student Information System / SIS** — the SIS is the student-and-records system of
   record (enrollment, transcripts, registration); curriculum management governs the
   offering data upstream and synchronizes approved changes into the SIS (CourseLeaf:
   bi-directional "SIS Sync"; Coursedog: "approved changes are now correct in the SIS").
   Seat test: staff governing what is taught vs staff/students interacting with who is
   enrolled. Curriculum management without students = this Type; SIS without governance =
   records system.
2. **vs Learning Management System / LMS** — the LMS delivers the live, section-level
   course to enrolled students (content, activities, grades); curriculum management governs
   what the course *is* across terms. No learner-facing delivery exists in any sampled
   curriculum product; students appear only as consumers of published reference output.
3. **vs Academic Timetabling** — timetabling places teaching activities in time and rooms,
   consuming approved course/program data (the timetabling pass recorded curriculum
   attachment as the seam). Scheduling decisions are downstream; a timetable change is not a
   curriculum change.
4. **vs Course Registration System** — registration is the student act of enrolling in
   offered sections; it consumes the published curriculum and offered sections. Reverse
   test: remove students/enrollment and keep governed offering records → this Type.
5. **vs Academic Accreditation Management / Institutional Effectiveness Platform** — those
   Types run standards-compliance and outcomes-assessment loops and consume curriculum maps
   as *evidence* (per the accreditation pass). Curriculum management owns the curriculum
   object and its change process; accreditation is a consumer/reporting neighbor.
6. **vs catalog publication** — the directory has no separate catalog leaf; every higher-ed
   sampled product either bundles catalog publishing (CourseLeaf CAT, Coursedog Catalog &
   Handbook, Modern Campus Catalog) or treats it as the publisher module (CourseLoop).
   Catalog is therefore recorded as the standard publication surface *inside* this Type.
   Observation: if catalog tooling were split out as its own leaf, the two would be tightly
   coupled siblings (curriculum = governance of record; catalog = published view), not
   duplicates. Recorded in STATUS Boundary Issues for the taxonomy maintainers.
7. **vs Lesson Planning Application (§23 sibling)** — the K-12 realization shades into
   lesson planning (Atlas: unit + lesson planning). Distinction: lesson planning is the
   individual teacher's authoring surface; curriculum management is the institution-level
   layer of records, review, standards coverage, and publication *around* that authoring.
   The two are adjacent layers, frequently shipped together in K-12. Flagged in STATUS for
   possible joint review when Lesson Planning Application is processed.
8. **vs generic workflow/BPM platforms** — proposal-plus-approval alone does not make this
   Type; the defining difference is the maintained curriculum data model (programs, courses,
   outcomes/standards; units, lessons) and the publication/synchronization of the approved
   record. Anti-overfitting: workflow machinery is universal in the sample but is not the
   defining structure — a BPM tool with a curriculum form is not a curriculum management
   application.

### "去掉什么就变成另一个 Type" 判据

- Remove the curriculum records (keep forms/approvals) → generic workflow/approval platform.
- Remove governed change (keep records + publication) → catalog / documentation tool.
- Remove publication/sync (keep records + change) → internal drafting tool that never lands
  changes in student-facing systems; no longer the institution's curriculum of record.
- Add students as first-class managed actors (enrollment, records) → SIS territory.
- Add section-level delivery to enrolled learners → LMS territory.
- Add time/room placement of activities → Academic Timetabling territory.

## Historical / Market-Sample Check (§24)

Pre-software practice: course and program changes were proposed on paper forms routed
through curriculum committees for approval; approved changes were printed into the annual
catalog/faculty handbook (higher-ed) or curriculum guides and binders (schools) — the
curriculum of record communicated outward. K-12 curriculum mapping predates software as
standards-alignment binders. Both fit the L0 (records + governed change + published record)
without SIS sync, dynamic forms, effective-term automation, or catalogs as software. Older
and regional realizations (UK/AU program validation documents, European modular catalogs,
state common-course-numbering systems) fit as well. The definition therefore does not
over-fit to the current US higher-ed SaaS pattern.

## Uncertainties

- Exact workflow stage names, state machines, and numeric limits per product are unverified
  (Modern Campus manual auth-gated; Atlas help center not fetched; Coursedog knowledge base
  unreachable). The final document deliberately avoids precise step lists and numbers.
- Whether periodic quality-assurance "curriculum review" cycles are universal: observed
  directly at CourseLoop; plausible elsewhere but only asserted as common, not definitional.
- The K-12 realization (Atlas-style) vs higher-ed governance: treated as one Type with two
  realization families because the governance/publication loop is identical in shape; a
  maintainer could alternatively split them. Flagged in STATUS Boundary Issues.
- Catalog publication is treated as inside this Type because no catalog leaf exists; if one
  is created later, this document's boundary section already describes the split.
- Evidence base for Coursedog rests on the marketing site including named institutional
  quotes (registrar/coordinator roles) rather than a help center; operational specifics
  kept out of the final document.

## Final Synthesis

A Curriculum Management application is the institution-side system that keeps the
institution's curriculum alive as governed data: structured records of what the institution
teaches (programs/courses in higher education; units/lessons in schools), a proposal →
review → approval process that is the only path by which those records change, and
publication/synchronization of the approved curriculum as the authoritative version consumed
by catalogs, student-facing systems, staff, and (in schools) families. Everything else —
dynamic forms, SIS sync, impact analysis, outcome mapping, catalog sites, review cycles,
marketing coordination, study planners — is mature machinery built around that loop, and
segment (higher-ed vs K-12) decides which machinery dominates.
