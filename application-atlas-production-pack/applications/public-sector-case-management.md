# Public Sector Case Management

## Overview

A **Public Sector Case Management** application is a government agency's caseworker-facing system of record for individual constituent matters. Each matter a person, household, or organization brings to the agency — a service request, a complaint, a benefit application, a report, an investigation, a service provision — is opened as a **case**: a persistent, identified record that is assigned to a responsible staff member, worked through a governed lifecycle, and closed with a recorded outcome.

The defining core is small:

```text
Constituent matter
└── Case (persistent unit of record)
    └── Responsible worker (caseload semantics)
        └── Governed lifecycle: intake → work → recorded resolution
            └── Accumulated record: notes, documents, communications, actions
```

Everything else commonly associated with these products — citizen portals, eligibility engines, SLA timers, GIS maps, inspection apps, AI assistance — is widespread in current implementations but is not what makes the product a case management system. Paper case files with a caseworker assignment and a case history satisfy the same structure.

When the sustained casework layer is removed and only citizen-facing intake, routing, and request tracking remain, the product is a 311 / citizen service request platform. When the matter-of-record is removed and only queue-resolved service items remain, it is a ticketing system.

## Users & Context

Primary users are the agency's frontline and supervisory staff:

- **Caseworker / case manager / officer** — holds a caseload of assigned cases; registers intakes, gathers information, conducts assessments or investigations, records notes and decisions, communicates with the constituent, and moves each case toward resolution.
- **Intake staff** — receive matters arriving by phone, email, web form, walk-in, or referral; perform initial screening and route them onward.
- **Supervisor / unit manager** — oversees the unit's caseload, redistributes assignments, reviews decisions, handles exceptions and escalations.

Secondary users:

- **Program administrators** — configure case types, workflows, forms, and deadlines; manage reporting.
- **Partner organizations** — service providers or other agencies that receive referrals or provide status updates in some deployments.
- **Constituents** — increasingly submit matters and check status through self-service portals, though the system's working surface belongs to staff.

The work environment is an agency office (or field work with mobile access), organized around a caseload: a worker's standing set of open cases that must each be advanced. The context is public accountability — cases are processed under the agency's service obligations, and the record may be reviewed by supervisors, auditors, elected oversight bodies, or the constituent.

## Core Model

### The Defining Core

**The case.** The center of the system is the case: a persistent, identified record of one constituent matter. A case is opened when a matter arrives (a complaint about a property, an application for assistance, a report of a concern, a request for service) and exists to hold everything about that matter: the people involved, what was reported or requested, what the agency found, what it decided, and what it did. Cases are typed — a complaint case, an application case, an investigation, a service request — and the type drives the workflow, forms, and rules that apply.

**The responsible worker.** A case is held by an identified staff member. Assignment may be made by a supervisor, by self-selection, or by automatic routing that considers staff capacity and case type; whatever the mechanism, the result is the same — some named person is responsible for advancing the case. The worker's caseload (their set of open cases) is a first-class working surface, and reassignment is itself a recorded event. This is the structural feature that separates case management from an anonymous ticket queue.

**The governed lifecycle.** A case moves through configured stages from intake to a recorded resolution — received, under review, in investigation, pending information, decided, resolved, closed. Exact stage names vary by product and agency; the governance is the point: transitions happen in a defined order, actions taken at each stage are recorded on the case, and closure is an explicit act that fixes the outcome (resolved, denied, withdrawn, referred elsewhere). The closed case remains as institutional memory: what the agency did, when, and why.

**The accumulated record.** Onto the case accumulate case notes, documents and attachments, tasks and their completion, communications with the constituent, status changes, and the audit trail of who did what when. The case is the agency's memory of the matter — the basis for handoffs when staff change, for supervisor review, and for accountability after the fact.

### Standard Capabilities

Mature products commonly add the machinery that makes casework practical:

- **Intake channels** — web forms and self-service portals, phone and email capture, walk-in registration, inbound referrals from other agencies, and citizen mobile reporting. Intake commonly includes screening questions and guided forms so the right information is captured up front.
- **Participant records** — the people and organizations involved, held as records with roles on the case (complainant, subject, beneficiary, household member). Person records persist across cases, so a returning constituent's history is visible and duplicate intakes can be recognized.
- **Tasks, checklists, and deadlines** — the steps a case must pass through, tracked as tasks with due dates; statutory or policy timelines are commonly tracked against the case.
- **Constituent communication** — letters, emails, and notifications generated from the case; portal visibility of status; requests for missing information.
- **Reporting** — caseload and backlog views, outcome and timeliness measures, and compliance reporting for funders, oversight bodies, or the public.
- **Access control and audit** — role-based visibility (constituent data is sensitive), and an audit trail over case actions.

### One Structure, Many Implementations

The core is written conceptually; implementations differ:

```text
Concept:   Constituent matter of record
Realized as:  complaint case, application case, service request,
              investigation, benefit case, enforcement case

Concept:   Responsible worker
Realized as:  named assignment, queue routing by capacity and case type,
              supervisor allocation

Concept:   Governed lifecycle
Realized as:  configurable status machines per case type, with
              agency-defined stages, gates, and closure outcomes
```

A reader who has only seen one implementation — say, a municipal service-request tool — should still be able to recognize a state benefits casework system as the same Type from the core.

## How It Works

### A matter becomes a case

```text
Matter arrives (web form / phone / email / walk-in / referral / field report)
→ intake staff register it and screen it (guided questions, initial assessment)
→ case is created (or an existing case is linked)
→ case is typed and prioritized
→ case is assigned to a responsible worker
```

Intake is a distinct skill in these systems: guided forms and screening questions ensure the agency captures what it needs before work begins. Some matters are resolved at intake; the rest become cases.

### The casework loop

```text
Worker opens the case from their caseload
→ reviews the accumulated record (notes, documents, history)
→ performs the next step: gather information, inspect, assess eligibility,
   investigate, correspond with the constituent
→ records what was done and found (notes, documents, task completion)
→ advances the case's status
→ repeats until a decision or outcome is reached
```

This loop is the daily work of the primary user. The caseload view tells the worker what is open, what is overdue, and what needs attention next; the case record tells them everything that has happened so far.

### Decision and resolution

```text
Worker (or reviewing authority) reaches the outcome:
  approve / deny / resolve / cite / refer / close-as-unfounded
→ outcome and rationale recorded on the case
→ constituent notified (letter, email, portal status)
→ case closed — the record is retained
```

Closure is explicit and gated: a case is not closed while required steps are incomplete or required information is missing. Some outcomes spawn follow-on cases (an appeal, a referral to another agency, an enforcement action).

### Oversight

Supervisors work from unit-level views: open caseloads per worker, aging cases, overdue deadlines, exceptions. Reassignment, escalation, and review are recorded on the case like any other action.

## Interfaces

The following surfaces are described conceptually; layouts and names vary by product.

### Caseload / case list

The worker's primary entry surface.

- lists the worker's (or unit's) open cases with type, status, age, and priority
- surfaces overdue items and recent activity
- primary actions: open a case, filter and sort, accept an assignment

### Case record

The center of the product — one screen (or a small set of tabs) holding the matter.

- overview: type, status, responsible worker, participants, key dates, outcome
- accumulated content: notes, documents, tasks, communications, history/audit
- primary actions: record a note, attach a document, complete a task, change status, reassign, communicate with the constituent, close

### Intake forms

Guided registration for new matters.

- structured questions per case type, screening logic, document upload
- primary actions: register the matter, create the case, route or assign it

### Constituent portal (where deployed)

The constituent-facing surface.

- submit a request or application, upload documents, view status, receive messages
- primary actions: submit, respond to agency requests for information

### Reporting / dashboards

Management and accountability surfaces.

- caseload distribution, backlog and aging, outcomes, timeliness, compliance
- primary actions: filter, export, schedule reports

### Administration / configuration

- case types, workflows and statuses, forms, deadlines, user roles and permissions

## Important Rules / Behaviors

### The case outlives the interaction

A case is not a session; it persists from intake to closure and beyond, and its history is retained. Staff turnover does not lose the matter — the record carries it.

### Assignment creates accountability

Every open case has a responsible worker. Unassigned cases are visible as exceptions; reassignment is recorded. This is the behavior that makes caseload management possible.

### Status transitions are governed

Cases move through their lifecycle in configured order. Required steps gate closure; a case cannot be closed with mandatory tasks incomplete. Exact stage vocabularies are agency-configured, not industry-standard.

### Timelines are tracked

Statutory or policy deadlines (response times, review periods) are commonly tracked against the case and surfaced as overdue. The specific timelines depend entirely on jurisdiction and program; the tracking is structural.

### Access is restricted and audited

Constituent data is sensitive. Visibility and edit rights follow role-based rules (by unit, program, or assignment), and actions on the case are auditable. In human-services variants, privacy obligations are stricter still.

### Duplicate matters are a real problem

The same person may contact the agency repeatedly, and the same issue may arrive through multiple channels. Mature products help staff recognize existing person records and related open cases rather than opening blind duplicates.

## Variants

The Type spans several recognizable poles. They share the core; they differ in the machinery added:

- **Social programs / benefits casework** — program catalogs, eligibility determination, enrollment, and benefit assignment bound to the case; common in state and local assistance agencies.
- **Human & social services casework** — care plans with goals and tasks for the constituent, service delivery tracking, and funder-facing outcome reporting; common in social services departments and funded providers.
- **Investigative & enforcement casework** — evidence handling, custody tracking, proceedings, violations, and enforcement actions bound to the case; common in regulatory and investigative agencies.
- **Municipal service & enforcement casework** — property/parcel-anchored cases, inspections, violations, and citations across departments like code enforcement, licensing, and animal control; common in cities and counties.
- **Packaging variants** — purpose-built department suites, human-services specialist platforms, and configurable platforms where the agency assembles case types on a shared foundation.

A variant remains a variant while the core applies. Where a pole adds structures so extensive that the generic core no longer describes the work — for example, court dockets and hearings, or child-welfare placement machinery — the directory treats it as its own Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| 311 / Citizen Service Request Platform | adjacent, upstream | citizen-facing intake, routing, and request tracking; lacks the sustained worker-held casework layer — its requests commonly become cases here |
| Social Services Case Management | domain specialization | same core plus social-services program machinery; directory lists it separately |
| Child Welfare Management | domain specialization | adds placement, safety-assessment, and regulatory machinery far beyond the generic core |
| Immigration Case Management | domain specialization | same core bound to immigration proceedings and statuses |
| Law Enforcement / Court / Prosecutor Case Management | domain specializations | justice-domain structures (dockets, hearings, charges) beyond the generic core |
| Business Case Management Platform | private-sector analog | same case machinery; matters are corporate (compliance, audit, investigation) rather than constituent matters under public obligations |
| Help Desk / Ticketing System | structurally distinct | queue-resolved service items without caseload-of-record semantics; speed-to-resolution is the center, not a governed matter lifecycle |
| Government Records Management | downstream | governs retention and disposition of official records; a closed case may become a record, but records management does not work the matter |
| Permit Management / Government Licensing / Code Enforcement | domain processing Types | permit, license, and enforcement structures of their own; in local government many "case management" deployments are actually these — the generic Type is what remains when the domain structures are removed |
| Constituent Relationship Management | broader | spans engagement and communication with constituents across channels; case management is the casework layer within it |

The most important boundary is with the 311 / service-request Type, because products increasingly bundle both. The structural test: if the sustained, worker-held processing of the matter to a recorded resolution is removed, what remains is the intake platform; if the citizen-facing intake surface is removed, what remains is this Type.

## Representative Products

- **Salesforce Public Sector Solutions** — configurable platform case management used by large city, state, and national agencies; documented data model spans complaints, referrals, applications, cases, programs, benefits, and care plans.
- **CaseWorthy (ClientTrack)** — purpose-built human-services case and program management platform used by nonprofits and local/state governments.
- **GovPilot** — municipal government platform whose department modules process resident-reported matters from report through resolution.
- **Comcate** — department-specific case tools for local government (code enforcement, animal control, CRM/311) organized around request-to-resolution workflows.

The largest pure-play government software vendor (Tyler Technologies) could not be included: its site was not reachable during research. The sample is US-weighted; the core is written jurisdiction-neutrally.

## Sources

Research date: **2026-09-10**

- Salesforce — Public Sector Solutions overview: https://www.salesforce.com/publicsector/
- Salesforce — Trailhead, Social Program Management Data Model in Public Sector Solutions (Case Management objects, participants and intake, cases/programs/benefits): https://trailhead.salesforce.com/content/learn/modules/social-program-management-data-model-in-public-sector-solutions
- Salesforce Help — Public Sector Documentation (incl. Managing Investigative Cases; Create Case from Complaint flow): https://help.salesforce.com/s/articleView?id=ind.psc_admin_concept_psc_welcom.htm&language=en_US&type=5
- Salesforce Developers — Data Model Gallery, Investigative Case Management: https://developer.salesforce.com/docs/platform/data-models/guide/justice-investigative-case-management.html
- CaseWorthy — home and platform pages: https://caseworthy.com/ , https://caseworthy.com/platform/caseworthy-platform/
- GovPilot — product site: https://www.govpilot.com/
- Comcate — product site: https://www.comcate.com/

> Sourcing limitation: Tyler Technologies' site returned access errors and ServiceNow's government pages timed out during research; neither product's documentation informed this document, and no claims are made about them. Comcate's evidence is limited to its public product site (its help center did not render). Precise operational details that were not directly verified — specific statutory timelines, exact status vocabularies, numeric limits — are intentionally not stated; lifecycle stage names in this document are conceptual, since agencies configure their own.

Detailed product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
