# Student Case Management

## Overview

A **Student Case Management** application is an education institution's system for handling concerns about individual students as **cases**: a staff member reports, refers, or flags a specific issue regarding a specific student; the institution opens a persistent case for it, assigns a responsible staff member, works it over time — recording notes, contacts, tasks, plans, and referrals — and closes it with a recorded outcome. Each student's cases and related records accumulate into a retrievable history that staff use for context, continuity of care, and accountability.

The defining structure is deliberately small:

```text
Student of the institution (population fed by the student record system)
└── Case of record (opened for a specific concern, assigned to a responsible staff member)
    └── Worked case file (dated, attributed casework accumulating on the case)
        └── Recorded resolution (lifecycle carried to closure)
            └── Student's cross-case history (cases, incidents, and interactions accumulate per student)
```

Anything that is not a case about a student — the school-wide conduct-event loop, the regulated special-education process, the ongoing advisor–student relationship, or population-level retention analytics — belongs to a neighboring Application Type, even though the same institutions and often the same staff work across all of them.

## Users & Context

The primary users are the staff who carry cases:

- **case owners** — deans of students, conduct officers, safeguarding or child-protection leads, case managers, counselors, or members of care and safety teams who are responsible for individual cases from assignment to resolution
- **team members** — staff who contribute to a case (recording observations, completing assigned tasks, joining coordinated responses) without owning it

Secondary users:

- **supervisors and institutional leaders** — who oversee caseloads, monitor open cases and follow-up, and review patterns across schools or departments
- **reporting staff** — faculty, residential staff, and other employees who submit concerns but do not work cases
- **external parties** — other institutions and agencies that receive referrals or, in some configurations, securely share case information

Students themselves may submit reports and may see some interactions through a portal in some products, but the casework is a staff-side activity: the student is the subject of the record, not its operator.

Typical contexts: a university conduct or student-affairs office working discipline, wellbeing, and misconduct cases; a K-12 district safety team running threat-assessment casework; a school safeguarding team maintaining welfare concern records; a student-support office coordinating care across departments. What these contexts share is a concern about one student that requires sustained, documented staff response — not a one-time transaction.

## Core Model

### The Defining Core

Three structures. Remove any one and the product stops being student case management.

**1. The student case of record.** A case is a persistent, individually identified record about a specific concern regarding a specific identified student. It is opened through intake — a report, a referral, a logged concern, or an alert — and it binds the student, the concern, and (in many configurations) other parties such as reporting staff, witnesses, or affected persons. A case is assigned to a responsible staff member and moves through a tracked lifecycle toward a recorded resolution. Without the case container, concerns remain unstructured events; without the assignment, cases are an unowned queue.

**2. The worked-and-documented case file.** A case is not a ticket that resolves on reply; it is worked. Dated, attributed casework accumulates on the case as staff act: narrative notes, records of contacts and meetings, completed forms, uploaded documents, tasks and follow-ups with owners, actions taken, referrals made, and coordination with other offices or external agencies. The file is the institution's evidence of what was done, by whom, and when — the property that makes the case auditable and the response defensible.

**3. The student's cross-case record.** Cases bind to the institution's enrolled-student population — in practice fed from the student record system (SIS/MIS), which supplies identity, enrollment, schedules, and often attendance and incident context. Across cases, each student accumulates a history: prior cases, linked incidents, interventions, communications, and outcomes, commonly surfaced as a chronology or "full student story" on the student's profile. This per-student accumulation is what lets staff see context behind a new concern, maintain continuity when staff or schools change, and demonstrate institutional accountability.

```text
Staff concern
  ↓ intake
CASE (student × concern × parties)
  ↓ assigned
Responsible staff member
  ↓ worked over time
Case file: notes · contacts · tasks · forms · documents · plans · referrals
  ↓ resolved
Recorded outcome, case closed — retained
  ↓ accumulates
Student's cross-case history (chronology)
```

### Standard Capabilities

Mature products commonly add the machinery that makes casework practical at institutional scale. These are standard across the market but are not what makes the product this Type:

- **Intake forms and routing** — configurable report/concern forms (web and mobile), routed automatically by content, concern type, or the students involved
- **Task and follow-up management** — follow-up actions with clear owners and due dates, checklists, reminders, and oversight of outstanding tasks
- **Plan machinery on the case** — support, care, intervention, or response plans recording the agreed course of action and its progress
- **Multi-party records** — representation and communication for the people involved in a case (reporting party, affected parties, witnesses, families/guardians)
- **Need-to-know access control and audit trails** — role-based, often case-level restrictions on who can see what; every entry and action time- and user-stamped
- **Reporting and oversight** — dashboards and reports on case volumes, categories, trends, and outcomes, from caseload grain up to district/institution grain
- **Student record system integration** — the student population substrate, often with attendance, behavior, and academic context pulled in
- **Communication tools** — letters and notifications to parties and staff, with delivery confirmation in some products

### One Structure, Many Implementations

The core model is written conceptually. Implementations differ most in the grammar by which a case comes to exist:

- **Case-first** — every report becomes a case, typed by workflow (conduct, wellbeing, misconduct, and so on)
- **Escalation-first** — low-level concerns and incidents are logged and time-stamped first; a case is opened by escalation when sustained management is needed, and prior and future incidents are linked to it
- **Protocol-first** — a guided assessment flow (for example, a formal threat-assessment or risk-screening instrument) structures the evaluation, and the outcome generates the case's tasks and plan

Similarly, the "plan" on a case is realized variously as a care plan, support plan, intervention plan, or response plan depending on the concern domain. The structures are shared; the vocabulary is segment-specific.

## How It Works

### The casework loop

```text
Concern arises (staff observation, disclosure, incident, alert)
→ report / referral / concern submitted through an intake form
→ routed by type, content, or parties involved
→ case opened; responsible staff member assigned
→ casework loop:
      record notes and contacts
      assign and complete tasks
      coordinate with offices or refer to external agencies
      apply and adjust the support plan
→ resolution recorded (outcome, actions, classification)
→ case closed — retained in the student's history
```

Two properties distinguish this loop from neighboring Types. First, **the case is worked over time by an accountable owner** — a conduct event closed by administrative action, or an alert acknowledged and cleared, is not casework. Second, **the record is the deliverable**: a defensible, auditable account of concern → response → outcome that survives staff turnover and institutional review.

### Concern-to-case escalation

In escalation-first implementations, staff log low-level concerns and incidents directly — fast, mobile, sometimes anonymously. Logged concerns accumulate on the student's record; when severity, repetition, or pattern warrants, any incident is escalated into a case, which then links the related incidents and becomes the container for sustained casework. The concern log and the case layer are distinct structures serving one record.

### Coordination across offices and agencies

A student concern commonly exceeds one office. Cases support multi-party, multi-office work: staff collaborate on the same case file, delegate sections, refer the student to campus or external services, and — particularly in safeguarding configurations — share defined portions of the record with other institutions or agencies. Where referrals leave the institution, the receiving agency's casework happens in its own system; the handoff is recorded, not owned.

### Core vs Common vs Optional

**Defining core** — without these, not this Type:

- persistent case of record about an identified student concern
- assigned responsible staff member and tracked lifecycle to recorded resolution
- documented casework accumulating on the case
- per-student accumulation of cases and interactions inside the institution

**Standard capabilities** — present in most mature products:

- intake forms with routing; task/follow-up management; plan machinery; multi-party records; need-to-know access with audit trails; reporting/oversight; student-record-system integration; communication tools

**Optional / variant** — depends on segment, region, and product:

- anonymous intake channels; records transfer when students move between institutions; multi-agency data-sharing portals; regional accountability reporting; AI assistance for drafting or categorizing; protocol-guided evaluation flows; standalone products vs suite modules

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Caseload / case list

The staff member's working surface.

- lists assigned and team-visible cases with status, age, and outstanding follow-ups
- surfaces new reports and alerts requiring triage
- primary actions: open a case, reassign, escalate, record actions

### Case detail (the case file)

The center of the product.

- the student and parties involved, the concern and its classification, lifecycle state
- the accumulated file: notes, contacts, forms, documents, tasks, plans, referrals, event/change logs
- primary actions: record a note or contact, assign/complete a task, upload a document, update the plan, communicate with parties, record the resolution

### Intake form

The entry surface, often the widest-reach surface in the institution.

- structured report/concern forms tailored by purpose, completable on mobile
- primary actions: identify the student and parties, describe the concern, attach evidence, submit for routing

### Student profile / chronology

The student-level view that ties cases together.

- the student's institutional context and the accumulated chronology of concerns, cases, incidents, interventions, and communications
- primary actions: open related cases, review history for context, prepare records for transfer (where supported)

### Oversight dashboards

For supervisors and institutional leaders.

- open cases, caseload distribution, follow-up completion, trends and patterns across categories, schools, or time
- primary actions: filter, drill into cases, export reports

### Configuration

- concern categories and classifications, intake forms and routing rules, roles and access permissions, workflow stages, plan templates

## Important Rules / Behaviors

### Need-to-know privacy is structural, not cosmetic

Student cases hold some of the institution's most sensitive records. Access control is therefore part of the case model itself: role-based and often case-level restrictions determine who may see which cases and even which entries within a case; selected staff can be alerted to read specific entries; every view and action is logged in an audit trail. Institutions frame this under their student-privacy regimes (FERPA-class in the US; comparable duties elsewhere).

### The system records judgment; it does not replace it

Products structure the process and preserve the evidence, but the judgment — risk classification, response, outcomes — remains with trained staff. Even where products implement formal assessment instruments as guided flows, the instrument guides documentation and consistency; staff make the determinations. This is a consistent vendor stance across the sampled market.

### Cases are durable and cumulative

A closed case is not deleted; it is retained in the student's history. Prior incidents can be linked to later cases, and the chronology follows the student — in some configurations even across institutions (for example, safeguarding history transferring with a pupil's consent when they change schools). The value of the record grows with accumulation, which is why retention and audit discipline are first-class behaviors.

### Follow-up accountability

Open loops are tracked: tasks carry owners and due dates, forms can embed checks (whether a family has been notified, whether assigned tasks are complete), and leadership surfaces can monitor follow-through. The characteristic failure mode these products exist to prevent is the concern that was seen but never acted on.

### The case is the container; the incident is not

Where both structures exist, incidents are recorded events and cases are worked containers. Repeated incidents may prompt intervention processes, but the incident loop itself closes by administrative resolution; when sustained casework is needed, the incident is escalated into — and linked to — a case.

## Variants

The Type is concern-domain-agnostic. Common segment realizations:

- **higher-education conduct and student-affairs casework** — discipline, academic integrity, sexual misconduct, complaints, and wellbeing/care cases handled by conduct offices, deans of students, and care teams
- **K-12 safeguarding and welfare (UK-style)** — child-protection and welfare concern recording with chronologies, referrals to statutory agencies, and inspection-ready record keeping
- **K-12 student safety casework (US-style)** — behavioral threat assessment and suicide-risk screening casework, commonly protocol-guided and connected to broader student-support (MTSS) workflows
- **wellbeing/CARE casework** — students-of-concern monitoring, care plans, and cross-office follow-up in higher education
- **suite-module deployment** — case management as a shared capability inside an SIS or CRM platform rather than a standalone specialist product

Common variant axes: case-first vs escalation-first vs protocol-first grammar; institution-defined categories vs formal assessment instruments; standalone specialist products vs platform modules; regional accountability machinery (federal campus-safety reporting in US higher education; inspection regimes in UK schools).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Student Behavior Management | adjacent, most easily confused | the school-wide conduct-event loop: events of record against a school-defined framework, closed by administrative resolution, accumulated for pattern measurement — no assigned case owner, no worked container; incidents escalate into cases when sustained casework is needed |
| Special Education Management | regulated specialization | the regulated per-student process — evaluation and eligibility gate, legally-mandated plan content, compliance timelines; generic student casework has none of this machinery |
| Academic Advising Platform | adjacent | relationship-driven (ongoing advisor–student bond, appointments, notes); case-like objects exist inside advising but are not its center |
| School Counseling Management | adjacent | counselor caseloads, appointments, and ongoing support relationships; counselors commonly participate as caseworkers, but the center is the relationship, not the case |
| Social Services / Nonprofit Case Management | same machinery family, different mandate | external clients or beneficiaries served under public-program or organization-program mandates with recorded eligibility determinations; student casework serves the institution's own enrolled students |
| Child Welfare Management | statutory counterpart | the child-protection agency's system with legal authority, placement, and court-anchored processes; school-side safeguarding records concerns and refers out |
| HR Case Management | same machinery, population swap | employee cases and workplace concerns instead of student cases |
| Student Success Platform | converging surface | population-level retention analytics and intervention measurement at institutional scale; may embed case objects — center-of-gravity seam |
| Student Services Portal | neighboring surface | student-facing service requests and self-service; transaction resolution rather than sustained staffed casework |

The most important boundary is with **Student Behavior Management**: both record student incidents, and the same institution often runs both. The discriminator is the shape of the response loop — an event loop closed by administrative action (behavior) versus an assigned owner working a case over time (case management). The boundary with **Special Education Management** is the legal machinery: the evaluation→eligibility gate, the mandated plan, and the regulatory timelines that generic casework never carries.

## Representative Products

- Maxient — higher-education conduct and care records management (US)
- Symplicity Advocate — student conduct, Title IX, and behavioral-intervention case management (US/international)
- Branching Minds Canopy — K-12 student-safety case management with guided assessment protocols (US)
- CPOMS StudentSafe — K-12 safeguarding and welfare concern recording and case management (UK/international)
- Salesforce Education Cloud — platform-suite pole; case management as a shared capability within student success (US/international)

The defining core was checked across higher-education and K-12 segments, two regions (US, UK), and both standalone-specialist and platform-suite deployments.

## Sources

Research date: **2026-09-09**

Primary vendor surfaces (official product pages):

- Maxient — https://www.maxient.com/
- Symplicity — https://www.symplicity.com/ ; https://www.symplicity.com/higher-ed/solutions/advocate
- Branching Minds — https://www.branchingminds.com/ ; https://www.branchingminds.com/student-safety-software
- CPOMS — https://www.cpoms.co.uk/ ; https://www.cpoms.co.uk/cpoms-studentsafe-software/
- Salesforce — https://www.salesforce.com/education-cloud/

> Sourcing limitation: vendor help centers and operational documentation were not reachable from the research environment on this date; all direct evidence is positioning/feature-surface level from official product pages. Consequently this document deliberately states no precise operational facts (exact case-status names, numeric limits, timing rules, or default configurations). Lifecycle and structures are described conceptually; capability claims are calibrated to that evidence level.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analyses are recorded in the paired Research Notes.
