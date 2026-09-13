# Public Defender Case Management

## Overview

A **Public Defender Case Management** application is a defense agency's system of record for representing people who cannot afford an attorney. It anchors all work on the **represented client**, organizes that work into **defense cases** identified by the court's own case number (cause/docket number), paces the work by **court events**, and manages it through **assignment** of each case to a responsible defender whose caseload is visible and reportable.

It solves a specific institutional problem: public defense agencies carry high-volume criminal caseloads under statutory deadlines, with court hearings setting the rhythm of work, ethical conflict rules constraining which cases the office may take, and government funders demanding workload accountability — while the clients themselves pay nothing. The software exists to keep that work organized, timely, defensible, and measurable.

Its boundary is the defense-side party perspective on a court process. It is not the court's neutral docket, not the prosecution's mirror-image system, and not a billing-driven private law-office system.

## Users & Context

Primary users:

- **Public defenders (attorneys)** — carry the case: meet the client, review discovery, prepare motions, appear at hearings. Each case is assigned to a responsible attorney; the attorney's caseload is the unit of workload management.
- **Defense investigators** — work assignments from attorneys (witness interviews, evidence location); some products track investigator tasks, time, and reports as a first-class workstream.
- **Supervisors / chief defenders** — assign and transfer cases, monitor caseloads against benchmarks, review case status.
- **Office / agency administrators** — configure workflows, manage intake and eligibility processing, produce statistical and funding reports.

Secondary users and surfaces:

- **Social workers and specialists** in agencies practicing holistic defense (housing, immigration advice, mental-health advocacy alongside the legal case).
- **Clients** — through communication channels (messages, portals) in some products.
- **Justice partners** — courts, jails/sheriff systems, and other agencies, usually reached through integrations rather than direct use.

The work environment is a government agency — a county public defender office, a statewide defense commission with many trial offices, or a defender nonprofit under government contract. Appellate, post-conviction, and juvenile divisions often run in the same system as trial work.

## Core Model

### The Defining Core

Four structures, jointly held. Remove any one and the system stops being a public defender case manager:

```text
Represented Client (person of record)
└── Defense Case (one court proceeding, identified by the court's cause number)
    ├── Court Events / Hearings (the case's rhythm)
    ├── People in Roles (co-defendants, victims, witnesses — conflict-relevant)
    ├── Work Product (notes, documents, discovery/evidence, investigation, time)
    └── Assignment (responsible attorney + office/program)
        └── Caseload (the attorney's visible, reportable case population)
```

- **Represented client of record** — a persistent person record for an indigent person facing criminal charges (or another loss of liberty) to whom the agency owes representation. The client is the anchor: one client may have several cases, and case history, communications, and documents accumulate against the person as well as the case.
- **Defense case as the unit of work** — the office's record of one court proceeding in which it defends a client. The case carries the court's own identifier (the cause/docket number) as a first-class field, the charges being defended, and the people involved in roles. It is the hub to which everything else attaches: events, notes, documents, evidence, time, and assignments.
- **Court-event-driven work rhythm** — hearings and court deadlines are tracked per case, commonly synchronized from court systems (electronic docket feeds or automated docket searches). Events pace the work: between hearings, the defense team works the case — reviewing discovery, drafting documents, investigating, preparing.
- **Assignment and caseload** — every case is owned by a responsible attorney within the agency's office/program structure. Assignment is load-bearing in daily operation: in mature products, notifications and calendar entries route through the assigned defender, and caseload reporting is organized per attorney. Caseload per attorney — how many cases, of what type, against what benchmark — is the central management quantity of public defense.

A structural consequence worth noting: because clients pay nothing, there is **no client billing** anywhere in this application type. Time is tracked per case, but it feeds workload statistics and funding reports, not invoices.

### Standard Capabilities

Mature products commonly add the following. They make the system practical; they are not what makes it a public defender case manager.

- **Conflict-of-interest checking** — screening the people on a case (co-defendants, victims, witnesses, related parties) against the agency's other cases, so the office does not represent conflicting interests. Near-universal in the sampled products; ethically mandated; mechanics vary by product.
- **Document management and generation** — template-driven generation of pleadings, motions, and letters (commonly via word-processor merge), with generated documents automatically filed to the case; scanning and text recognition for incoming paper.
- **Case notes** — attributed, dated notes attached to cases (and often to clients), forming the office's institutional memory.
- **Discovery and evidence handling** — tracking what was received from the prosecution, assigning items for review, redaction, and disclosure; integration with digital-evidence platforms in some products.
- **Investigation support** — investigator task assignment, subpoena generation and tracking, investigator time and reporting (present in some products as a dedicated workstream).
- **Timekeeping** — per-case time entries ("timeslips") with verification workflows, feeding workload and funding accounting.
- **Reporting and dashboards** — caseload by attorney and case type, workload against benchmarks, case-status pipelines, outcomes, and grant/funding reports for oversight bodies.
- **Justice-partner integration** — pulling court dockets and calendar events, monitoring warrant and arrest databases, exchanging data with courts and jails through APIs or automated feeds.
- **Security regime** — role-based access control, audit logging, and criminal-justice data-handling compliance (CJIS-family requirements in the United States), reflecting the sensitivity of defense files.
- **Organizational structure** — multiple offices, programs, and specialized units (trial, appeals, post-conviction, juvenile, conflict/contract services) inside one system, matching how larger agencies are organized.

### Concept vs Implementation

The core is conceptual; implementations differ:

```text
Concept:  case identified by the court's number
Implementations:  a dedicated cause-number field promoted to the primary
                  identifier; the court's docket pulled into the system;
                  internal case IDs alongside the court number

Concept:  court events pacing the work
Implementations:  electronic docket feeds from the court system; automated
                  daily searches of online dockets creating calendar events;
                  manual entry

Concept:  assignment
Implementations:  a mandatory primary advocate plus office and program;
                  additional assignments (co-counsel, investigator, intern)
                  with start/end dates and transfer-only primary changes
```

## How It Works

### A case enters the office

A case typically begins when the court appoints the office (or the agency screens an applicant for eligibility, depending on the jurisdiction). The office creates or reuses the **client** record, records the court's **cause number**, opens the **case**, and — before or shortly after — runs a **conflict check** over the involved people. Conflict screening gates acceptance: if the office already represents a co-defendant or an adverse party, the case must be declined or reassigned.

### The case is assigned and worked

The case is assigned to a responsible attorney (with office and program). The assigned defender and their team then work the case between court events:

```text
Appointment / intake
→ client record + case record (court cause number)
→ conflict check over involved parties
→ assignment to responsible attorney
→ discovery received, reviewed, redacted, tracked
→ investigation tasks and subpoenas
→ notes, documents generated from templates and filed to the case
→ time recorded per case
```

### Court events pace the work

Hearings arrive from the court — pulled from an electronic docket feed, created by automated docket searches, or entered manually. Each event attaches to the case and appears on the assigned attorney's calendar. The daily operating loop is event-driven: prepare for the hearing, appear, record what happened, produce the follow-up work before the next event.

### The case reaches disposition and closes

When the proceeding resolves (dismissal, plea, verdict, or other disposition), the office runs its close-case process. Closure is a controlled transition, not a field edit: systems commonly gate it behind a defined process, record who closed the case and when, and lock down the closed record so historical information cannot be altered without formally reopening the case.

### The office manages the caseload

Parallel to the per-case loop, supervisors and administrators work the population view: caseload per attorney against benchmarks, case-status pipelines, aging reports, outcomes, and funding/grant reports. Time entries roll up into workload statistics; case counts roll up into the reports the agency owes its funders.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Case profile (the primary workspace)

- Purpose: everything about one defense case in one place.
- Typical information: client and involved people in roles, charges, court cause number, case status and history, upcoming and past court events, documents, notes, discovery items, time entries, assignments.
- Primary actions: add note, upload/generate document, record event, assign/transfer, change status, close case.

### Caseload / assignment views

- Purpose: the attorney's and supervisor's working queue.
- Typical information: assigned cases with next events, statuses, ages; caseload counts against benchmarks.
- Primary actions: open a case, filter by status/type, reassign, review workload.

### Calendar

- Purpose: the court-event rhythm across the office.
- Typical information: hearings and deadlines per case, per attorney, per courtroom.
- Primary actions: view by day/week/attorney, create or confirm events, navigate to the case.

### Client profile

- Purpose: the person of record across cases.
- Typical information: identity and contact details, associated cases, communication history, alerts.
- Primary actions: open a case, record communication, review history.

### Conflict checking surface

- Purpose: screen people against the agency's case population.
- Typical information: candidate matches between a new case's parties and existing records.
- Primary actions: run check, review matches, record the determination.

### Reporting / dashboards

- Purpose: management and funder accountability.
- Typical information: caseload by attorney/type, status pipelines, time summaries, outcomes, grant utilization.
- Primary actions: run and export reports, configure views.

## Important Rules / Behaviors

- **The lifecycle is gated, not free-form.** A case moves through defined transitions (opened → worked → disposition → closed), and closure is a process with recorded actor and timestamp. Closed cases are commonly locked against editing unless formally reopened.
- **Two layers of state are common.** A system-controlled lifecycle stage (which the user cannot set directly) coexists with an agency-defined working status (a workflow tool with values the agency controls, where every change is recorded with date, user, and note).
- **Conflict rules gate acceptance.** Representation must be screened against existing clients and adverse parties; conflict status can itself be a tracked state ("pending conflict determination") before a case is accepted.
- **Assignment is structural.** Every case has a responsible attorney; primary assignments are transferred rather than deleted, and assignment history is retained — because workload accounting and notification routing depend on it.
- **Time is accountability, not billing.** Time entries attach to cases and feed workload and funding reports; no product in the researched sample bills clients.
- **The court's identity travels with the case.** The cause number is the cross-system key linking the office's record to the court's record; integrations (docket feeds, warrant checks, e-filing) key on it.
- **Security is criminal-justice grade.** Defense files are highly sensitive; role-based access, audit logging, and compliance with criminal-justice information regimes are standard expectations, and hosting choices (government cloud regions, on-premises) follow from them.

## Variants

- **By agency shape** — county offices; statewide agencies with many trial offices plus appellate, post-conviction, and juvenile divisions; defender nonprofits under contract; conflict/contract services units that assign cases to panel attorneys.
- **By case type** — adult criminal trial; appellate and post-conviction; juvenile and dependency; civil commitment and other liberty-threatening proceedings.
- **By intake regime** — court-initiated appointments vs agency-run eligibility screening; the weight of indigency determination varies by jurisdiction.
- **By defense model** — traditional legal representation vs holistic defense, where social-work and civil-legal support are managed alongside the criminal case.
- **By deployment** — on-premises vs government-cloud hosting; a vendor positioning axis, not a difference in kind.
- **By client-facing surface** — staff-only systems vs products exposing messages, portals, or online intake to clients.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Prosecutor Case Management | sibling / opposite party | Same court ecosystem and object vocabulary, but the prosecutor initiates charges and represents the state; this Type represents the accused client. Vendors ship them as separate sibling products. |
| Court Case Management System | adjacent / neutral record | The court's system is the neutral docket of record for all parties; this Type is one party's working system built around its clients and defenders' caseload. |
| Law Practice Management System | adjacent / different economics | Private firms acquire and bill clients; timekeeping drives invoices. Here clients are indigent, the government funds the office, and time drives workload and funding reports. |
| Legal Matter Management | adjacent / different user | Matter management for corporate legal departments tracking outside counsel and spend; not defense of indigent persons. |
| Public Sector Case Management | genus | Generic government case management (permits, benefits, requests) lacks the legal-proceeding structure: charges, court events, conflicts, discovery, cause numbers. |
| Social Services Case Management | adjacent / different object | Social-services cases are service needs; these cases are court proceedings. Holistic defense brings social work inside the agency, but the case core stays legal. |
| Law Enforcement Case Management / Evidence Management System | adjacent / other side | Police-side records and evidence custody; the defender's evidence tracking is about receiving, reviewing, and disclosing discovery. |
| Legal Docket Management / Legal E-filing Platform | capability-adjacent | Docket tracking and e-filing appear as integrations inside this Type, not as its center. |

The most important boundary is the party perspective: prosecutor and court systems share this Type's vocabulary (cases, events, people, evidence), but only here does everything hang off a **represented indigent client** and a **defender's caseload**.

## Representative Products

- DEFENDERbyKarpel (Karpel Solutions) — dedicated defender-side criminal case management for public defender offices
- LegalServer (Network Ninja) — configurable platform built for civil legal aid, public defense, and government law offices; used by statewide agencies and county offices
- eDefender (Journal Technologies) — public defender product within a justice suite alongside court and prosecutor systems

## Sources

Research date: **2026-09-09**

- LegalServer Help (official operational documentation) — https://help.legalserver.org/ — Case Status, Disposition and Case Status Compared, Case Assignments, Case Profile Pages, Lead and Member Cases, Client Intake, Closing a Case, Cause Number, Timekeeping, Optional Modules (accessed 2026-09-09)
- DEFENDERbyKarpel (official product pages) — https://www.defenderbykarpel.com/ (accessed 2026-09-09)
- Journal Technologies eDefender (official product page) — https://www.journaltech.com/edefender (accessed 2026-09-09)
- LegalServer customer stories — Kentucky Department of Public Advocacy selection; Travis County warrant-notification integration (accessed 2026-09-09)

> Sourcing limitation: several other vendors in this market (Tyler Technologies, CSG, MTG "Defender Data", CaseWorks) could not be reached from the research environment (blocked or offline domains), and general web search was largely unavailable. The researched sample is therefore three products, two of which are evidenced at product-page depth rather than help-documentation depth. Claims in this document are calibrated accordingly: structural statements rest on cross-product commonality; product-specific mechanics are stated only where directly documented. Precise operational details (exact status vocabularies, numeric limits, compliance certifications) are intentionally not asserted.
