# Curriculum Management

## Overview

A **Curriculum Management** application is the institution-side system that governs what an educational institution teaches. It maintains the institution's curriculum — its programs and courses (in higher education) or its units and lessons mapped to standards (in schools) — as structured records, routes every change to those records through an institutional review-and-approval process, and publishes or synchronizes the approved result as the authoritative version of the curriculum that the rest of the institution relies on.

The defining core is small:

```text
Curriculum records
└── Governed change (proposal → review → approval, tracked)
    └── Curriculum of record, published / synchronized outward
```

Everything else commonly associated with these products — dynamic proposal forms, SIS synchronization, impact analysis, learning-outcome mapping, catalog sites, marketing coordination, study planners — is standard capability that mature products add to make the loop workable at institutional scale. It is not what makes the software a curriculum management application.

When the software starts managing enrolled students, delivering live courses to learners, or placing activities in rooms and time slots, it has crossed into a different Application Type (Student Information System, Learning Management System, Academic Timetabling).

## Users & Context

The primary users are institutional staff who own or change the curriculum — never the learners themselves. Students and parents appear only as readers of published output.

Typical roles in higher education:

- **faculty proposer** — authors a new-course or course-change proposal
- **department chair / dean** — reviews and endorses proposals from their unit
- **curriculum committee members** — deliberate and approve at committee stages
- **registrar / academic affairs staff** — operate the process, guard data accuracy, and connect approvals to the systems that schedule and record courses
- **catalog / communications staff** — publish approved curriculum for prospective and current students

Typical roles in schools and districts:

- **teacher** — authors units and lessons within the school's curriculum structure
- **principal / school leadership** — reviews and approves what is planned and delivered
- **curriculum director** — oversees coverage and coherence across grades and subjects
- **district leadership / board** — consumes district-wide views and alignment reports

The work context is committee-based academic governance: proposals move through defined bodies with formal approval authority, on institutional calendars, with downstream deadlines (catalog publication, term setup, accreditation reporting).

## Core Model

### Curriculum records

The system's center is the curriculum itself, held as structured, governed records rather than as free documents:

- **Program / course records** (higher education) — each course and program carries governed attributes: title, description, credits, requirements, prerequisites, and related policies. Programs contain courses; courses relate to each other (equivalencies, cross-listings, requirement roles).
- **Unit / lesson records** (schools) — instruction is described as units containing lessons, each mapped to the standards the school follows. Units sit inside courses or grade-subject structures.

These records are the object every other part of the system acts upon. If the software only routes forms about curriculum without maintaining the curriculum data itself, it is a workflow tool, not a curriculum management application.

### Change proposals

A **proposal** is a tracked change to a curriculum record — a new course, a course revision, a program change, a new unit. Proposals are made on institution-configured forms that typically pre-fill from existing records, show exactly what is being changed, and can carry supporting documents. The proposal, not the record, is what moves through review.

### Review and approval workflow

Each proposal is routed through an institution-defined sequence of stages, each with designated participants who review, comment, and approve or return the proposal. Workflow logic is configured by the institution, so different kinds of changes take different paths. Participants see the proposal's status; the system notifies them when action is needed.

### Curriculum of record

An approved change does not simply overwrite history: the curriculum exists as versions effective for particular academic periods (terms or catalog years in higher education; school years in K-12), and past versions remain retrievable — downstream processes such as degree audits depend on the requirements that were in force at a given time. The approved, currently-effective curriculum is the institution's reference version.

### Publication and synchronization

The curriculum of record is communicated outward to the people and systems that consume it:

- the **academic catalog** (higher education) — the published, student-facing presentation of programs and courses
- a **public curriculum site** (schools) — what families and the community can see is being taught
- **downstream systems** — scheduling, registration, degree audit, syllabi, and the student information system are kept in step with approved curriculum, so every downstream process starts from the same authoritative data

### Outcomes and standards mapping

Curriculum records commonly carry links to learning outcomes (higher education) or educational standards (schools), so the institution can see what each course or unit is meant to achieve and analyze coverage, gaps, and redundancies across the whole curriculum.

### One structure, many implementations

The model is conceptual; realizations differ by segment:

```text
Concept:       Curriculum record
Realizations:  program / course record (higher-ed) · unit / lesson record (schools)

Concept:       Effective versioning
Realizations:  catalog year / effective term (higher-ed) · school year (K-12)

Concept:       Publication surface
Realizations:  academic catalog (higher-ed) · public curriculum site (schools)
```

## How It Works

The defining loop runs from idea to published, effective curriculum:

```text
Maintain curriculum records
→ propose a change (dynamic form, pre-filled, edits tracked)
→ route through review and approval (configured stages, alerts, comments)
→ approve
→ change becomes effective for an academic period
→ publish / synchronize (catalog, public site, student systems)
→ periodically review and revise
```

**Propose.** A faculty member or teacher opens a proposal form for the record they want to create or change. The form is configured by the institution and pre-populated with current data; edits are visibly tracked, so reviewers see precisely what is proposed.

**Route and approve.** The system knows which workflow applies and routes the proposal accordingly, alerting each stage's participants. Reviewers comment, request changes, or approve. Because the rules are configured in advance, proposers do not need to know the approval path themselves. Mature products show the blast radius of a change — which programs, requirements, courses, or standards are affected — before final approval.

**Land the change.** Approval does not change the live record immediately: the change takes effect for a designated term or catalog year, and prior versions persist for students already studying under them. Only then does the approved curriculum flow outward — into the catalog, the public site, and the systems that schedule, register, and audit.

**Keep it alive.** Beyond individual changes, institutions run periodic review cycles (quality assurance, program review) in which the curriculum as a whole is examined, mapped to outcomes or standards, and revised — restarting the same propose-approve-publish loop at larger scale.

### Capability tiers

**Defining core** — without these, not curriculum management:

- structured curriculum records (courses/programs or units/lessons)
- governed change: proposal → review → approval with tracked status
- approved curriculum maintained as the institution's authoritative record and communicated outward

**Standard capabilities** — present in most mature products:

- dynamic proposal forms with pre-population and tracked edits
- configurable multi-stage workflows with alerts, comments, and status visibility
- change history and versioning by effective academic period
- impact analysis of proposed changes
- integration with the student information system and other academic systems
- learning-outcome / standards mapping
- catalog or public-site publication
- role-based permissions across proposer, reviewer, approver, and administrator
- reporting and audit trails
- periodic review cycles

**Optional / variant** — depends on segment and institution:

- syllabus management; marketing-content coordination alongside approval
- micro-credentials; cross-listed course handling; system-wide common course numbering
- student-facing study planners; labor-market data overlays
- AI assistance; professional-learning services

## Interfaces

### Proposal form

The authoring surface for change.

- Purpose: create or modify a curriculum record under governance.
- Typical information: record identity, governed fields (title, description, credits, requirements; or unit details and standards), attached documents, tracked edit highlighting.
- Primary actions: submit proposal, save draft, attach supporting material.

### Workflow inbox / proposal status

Where reviewers and proposers live day to day.

- Purpose: show which proposals await whose action and where each stands.
- Typical information: proposal list with stage, owner, age, and pending tasks.
- Primary actions: open, comment, request changes, approve, return, delegate.

### Curriculum browse / record view

The read surface over the whole curriculum.

- Purpose: inspect what the institution currently teaches and its history.
- Typical information: course/program pages or unit/lesson structures, versions by period, relationships (equivalencies, requirements, standards).
- Primary actions: search, browse, compare versions, start a change.

### Publication surface

- Purpose: present approved curriculum to its audience.
- Typical information: catalog program/course pages or the public curriculum view.
- Primary actions: publish, schedule publication, preview.

### Mapping and analytics

- Purpose: connect curriculum to outcomes/standards and expose coverage.
- Typical information: outcome↔course or standard↔unit matrices, gap and redundancy views, review reports.
- Primary actions: map records, run coverage analysis, export reports for accreditation or governance bodies.

### Administration / configuration

- Purpose: shape the system to institutional governance.
- Typical information: workflow definitions, form templates, roles, integration settings.
- Primary actions: configure forms and workflows, manage users and permissions, set up integrations.

## Important Rules / Behaviors

- **Approval is the only path to change.** The live curriculum of record changes only when a proposal completes its review process; direct edits to published curriculum are not the model.
- **Effective-dating governs activation.** Approved changes apply to a designated term or catalog year; current students remain under the requirements of their entry version. Prior versions persist and remain consultable.
- **The record has history.** Proposals, edits, comments, and approvals are retained as an auditable trail; institutions must be able to show what the curriculum was, when, and who approved it.
- **Roles gate actions.** Who may propose, review, approve, configure, and publish is institution-defined and enforced; the same change may require different bodies depending on its type or scope.
- **The student system is a neighbor, not the same system.** Curriculum approvals typically synchronize with the student information system rather than replacing it; keeping the two aligned is one of the product's central jobs and a common source of operational risk when it fails.
- **Publication is downstream of governance.** What students and families see is generated from approved records; stale or divergent catalogs are precisely the failure mode these products exist to prevent.

## Variants

- **Higher-education governance platform** — programs and courses as governed records, catalog-year versioning, committee workflows, catalog publication, SIS synchronization; the dominant market realization.
- **School / district curriculum planning platform** — units and lessons mapped to standards, leadership review, district-level coverage analytics, public transparency site, teacher-facing lesson planning built on the same records.
- **Workflow-first module** — a proposal-and-approval tool that leans on the student system for record storage and focuses on routing and compliance.
- **Academic-operations suite module** — curriculum as one component beside catalog, scheduling, registration, and syllabus products sharing the same data core.
- **System / state-scale deployment** — multi-institution governance with shared course numbering and cross-institution course management.
- **Micro-credential and non-degree extension** — shorter, faster-cycle offerings run through the same governance loop.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Student Information System / SIS | holds student records and registration; curriculum management governs the offering data upstream and synchronizes approved changes into it |
| Course Registration System | the student act of enrolling in offered sections; consumes the published curriculum rather than governing it |
| Academic Timetabling | places teaching activities in time and rooms using approved course data; scheduling is downstream of curriculum approval |
| Learning Management System / LMS | delivers the live, section-level course to enrolled learners; curriculum management governs what the course is across terms and has no learner-facing delivery |
| Academic Accreditation Management | runs standards-compliance and outcomes-assessment loops; consumes curriculum maps and outcome data as evidence |
| Institutional Effectiveness Platform | broader planning/assessment/improvement cycles; curriculum data may feed it, but the curriculum object is not its center |
| Lesson Planning Application | the individual teacher's authoring surface; K-12 curriculum management is the institutional layer of records, review, and publication around it |
| Transcript Management | the record of what individual students completed; curriculum management governs what could be completed |
| Workflow / Approval Platforms | route forms and tasks generically; they lack the curriculum data model and the published curriculum of record |

The sharpest seam is with the SIS: the two systems exchange the same course and program data, but the SIS is organized around students while curriculum management is organized around the curriculum and its governance.

## Representative Products

- CourseLoop — end-to-end curriculum management platform for universities (UK/AU/US)
- Modern Campus Curriculum (formerly Curriculog) — workflow-centered curriculum management within a connected-curriculum suite (US higher ed)
- CourseLeaf CIM — SIS-integrated forms-and-workflow curriculum management within an academic-operations platform (US higher ed)
- Coursedog — unified academic-operations platform spanning curriculum, catalog, syllabus, and scheduling (US higher ed)
- Atlas — curriculum management and lesson planning for schools and districts (K-12 / international schools)

The defining core was checked against the K-12 realization and against pre-software practice (paper curriculum-committee approvals, printed catalogs and curriculum guides) to avoid defining the Type by the current higher-ed SaaS pattern.

## Sources

Research date: **2026-09-07**

- CourseLoop — https://courseloop.com/
- Modern Campus — Curriculum product page: https://moderncampus.com/products/curriculum-management/ ; support overview: https://support.moderncampus.com/curriculum/
- CourseLeaf — https://www.courseleaf.com/ ; CIM product page: https://www.courseleaf.com/software/cim/
- Coursedog — https://www.coursedog.com/
- Atlas — https://www.onatlas.com/

> Sourcing limitation: detailed customer-only documentation (Modern Campus user manual; Coursedog knowledge base) and one Atlas process page were not accessible from the research environment on 2026-09-07. Product evidence therefore rests on official public product and support pages, including named institutional testimonials. Precise operational details (workflow step names, numeric limits, defaults, state names) are deliberately not stated in this document; they remain in the paired Research Notes.

Detailed product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
