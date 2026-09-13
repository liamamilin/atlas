# Employee Relations Case Management

## Overview

An **Employee Relations Case Management** application is the system HR and employee relations teams use to handle sensitive workplace people-matters — complaints, grievances, allegations of harassment, discrimination or retaliation, conflicts, policy violations, and disciplinary issues — as **confidential case records** that are tracked from first report through fact-finding to a documented resolution.

The defining core is deliberately small:

```text
Reported workplace people-matter
└── Confidential case record
    ├── The people involved (reporter, subject, witnesses) and the organizational context
    ├── An assigned owner moving the case through a defined handling process
    └── A retained, attributable history ending in a documented outcome
```

Everything else commonly associated with these products — anonymous reporting hotlines, two-way anonymous messaging, triage rules, interview templates, privilege flags, trend dashboards, benchmarking — makes the work practical and defensible but does not define the Type. Remove confidentiality, party linkage, the managed process, or the recorded outcome, and the software stops being employee relations case management: it becomes a service-desk queue, a generic issue tracker, or a document store.

## Users & Context

The primary users are the people inside an organization whose job is to receive and resolve employee problems:

- **Employee relations specialists and HR business partners** — the core handlers. They receive reports, triage them, conduct or coordinate fact-finding, make determinations, and document outcomes. In larger organizations this is a dedicated ER function; in smaller ones, generalist HR staff.
- **Investigators** — often the same HR people, but in sensitive or complex matters may be specialist investigators, external counsel, or a cross-functional team. Investigation-heavy deployments treat the product as their primary working tool.
- **ER / HR leaders** — not hands-on with every case, but responsible for oversight: are cases being handled consistently, what trends are emerging, what is the exposure.

Secondary users shape the surrounding workflow:

- **Line managers** — the most common way issues enter the system (they hear about problems first), and increasingly a supported user group with their own guided surfaces for raising and handling lower-level issues.
- **Employees** — as reporters, either openly or anonymously through web forms or hotlines; some products also let them ask for support without filing a formal report.
- **Legal, ethics, and compliance functions** — interested parties for privileged, regulated, or escalatory matters; they may own cases outright in some deployments.

The work context is defined by three pressures that shape the whole software category: matters are **sensitive** (careers, reputations, legal exposure), they must be handled **consistently and fairly** (similar cases should get similar treatment), and the organization must later be able to **prove** how it handled them (audits, regulators, tribunals, litigation).

## Core Model

### The Case as the Central Object

Everything in this Type of application hangs off a **case**: a discrete, structured record of one reported matter. A case is not a conversation thread or a ticket in a support queue; it is a confidential file about a specific situation between specific people at a specific part of the organization.

A case record typically carries:

- **The matter itself** — what was reported or observed, categorized by issue type (for example: harassment, discrimination, retaliation, interpersonal conflict, grievance, policy violation, performance or conduct concern).
- **The parties** — who reported it (if known), who it concerns, who witnessed it, and who is handling it. Anonymity is modeled explicitly: the reporter may be unidentified, with the case still fully functional.
- **The organizational context** — business unit, location, and other attributes used for routing, conflict awareness, and later analysis.
- **The handling history** — every note, conversation record, document, task, decision, and status change, attributed and time-stamped.
- **The outcome** — how the matter was resolved and what was decided.

### The Handling Process

A case moves through a process rather than sitting as freeform notes. Conceptually the lifecycle runs:

```text
Report / issue raised
→ Case created and categorized
→ Triage: routed, prioritized, owner assigned
→ Handling: fact-finding, conversations, investigation steps
→ Determination: findings and decision
→ Resolution: documented outcome
→ Follow-up: check-ins and aftercare (where the product supports it)
```

Exact stage names and the number of states vary by product and by how the organization configures it. Two structural properties are more consistent than any particular state list: the process is **enforced** (the system tracks which steps are complete and which are open), and it is **documented as it happens** (the record grows with the work, not reconstructed afterwards).

### Parties and Anonymity

The people model is unusual among case-management Types. A case binds together people in different roles — reporter, subject, witness, handler — and the software must respect different constraints for each:

- The reporter may be **anonymous** while the case remains fully workable; mature products support two-way messaging that preserves anonymity, so handlers can ask follow-up questions without learning the identity.
- The **subject** of a case is a person whose standing and career may be affected by the record; access to information about them is restricted accordingly.
- **Handlers** see only the cases assigned to them or their role; case visibility is deliberately narrow.

### Standard Capabilities Around the Core

Mature products commonly add:

- **Multi-channel intake** — employee web forms and portals, manager-raised entries, integrations, and anonymous reporting channels (web and hotline). Intake feeds the case engine directly: a submitted report becomes a structured case record rather than an email to be re-typed.
- **Triage and routing rules** — automatic categorization, routing by issue type / region / severity / workload, risk-based prioritization of the most serious matters, and immediate owner assignment.
- **Task machinery** — tasks with owners and due dates, reminders, notifications, and escalation when work stalls.
- **Fact-finding support** — interview planning and question templates, secure storage of evidence and documents, chronology-building, and structured notes. Depth varies: investigation-centric products are much deeper here.
- **Access and privilege controls** — role-based permissions with per-case visibility, and the ability to mark a matter as legally privileged so even its existence is visible only to the right people.
- **Time-stamped audit trail** — every action, update, and decision recorded automatically, forming the defensible history of the case.
- **Process templates** — configurable workflows per case type, department, or geography, so that the organization's own response process is enforced rather than merely described.
- **Case linking and pattern detection** — connecting related incidents and surfacing repeat names or behaviours across reports.
- **Aggregate analytics** — trends by issue type, unit, geography, and time; hotspots; resolution metrics; exportable reports for leadership, boards, and regulators.
- **HR-system integration** — employee and organizational data synchronized from the HR information system, so cases bind to a current picture of the workforce; single sign-on for handlers.

### What the Case Engine Is Not

The case record is not the employment record. Employee master data — jobs, compensation, employment status — lives in the HR information system; the case application typically syncs from it. And the case is not a service request: it is not "how do I change my address" but "this person reports this happened." That distinction drives the access model, the process design, and the stakes.

## How It Works

### From report to case

A matter enters through whatever channels the organization has enabled:

```text
Employee submits a web form (named or anonymous)
→ or a manager raises an issue on someone's behalf
→ or a hotline call is captured by an intake specialist
→ or HR creates the case from a conversation that already happened

→ the system creates a structured case record
  (categorized, time-stamped, bound to the parties and context it knows)
```

With anonymous reporting, the reporter typically receives a way to return — a reference or secure sign-in — and can exchange messages with the handler without revealing identity. Some products require the reporter's consent before an anonymous report is converted into a formal, actionable case.

### Triage and assignment

The new case is triaged: categorized, checked for related prior cases, routed to the right team or person (by issue type, region, severity, or current workload), prioritized against risk, and given an owner. The most serious matters are pushed to the front. The owner now has a file with everything intake captured, and the clock of tasks and deadlines begins.

### Handling the matter

What "handling" means depends on the matter. For a straightforward interpersonal issue it may be a few documented conversations and a resolution. For a harassment or discrimination allegation it is a formal workplace investigation:

```text
Plan the fact-finding (what needs to be asked, of whom, in what order)
→ conduct interviews (guided by templates/protocols; documented in the case)
→ collect and store evidence
→ build the chronology
→ analyze findings
```

Throughout, notes, documents, and decisions accumulate on the record under access controls. If legal risk warrants it, the matter can be marked privileged. Related matters — same subject, same pattern — can be linked so the organization sees the history, not just the incident.

### Determination and resolution

The handler (or, in governed processes, an approver above the handler) records findings and the decision that follows: whether the concern was substantiated, what action will be taken, and what is communicated to whom. The case moves to a resolved or closed state with that outcome on the record. The completion of the process is itself documented — who determined what, and when.

### After the case

Mature deployments do not treat closure as the end. Some products add deliberate follow-up — for example, checking in with the reporter to watch for retaliation, or structured aftercare for the people involved. More universal is feeding the case into the aggregate picture: what is trending, where, and what should change. The analytics layer — trends by issue type, unit, geography, and time; hotspots; repeat patterns — exists precisely so that individual cases add up to prevention.

## Interfaces

The surfaces below are described conceptually; names and layouts vary by product.

### Case queue / dashboard

The handler's home.

- Purpose: see the active caseload and what needs attention.
- Typical information: case list with status, owner, issue type, age/time open, priority; overloaded-workload signals; counts of open vs overdue.
- Primary actions: open a case, accept an assignment, filter by type/team/status, escalate.

### Case detail (the case file)

The center of gravity of the whole application.

- Purpose: hold everything about one matter in one secured place.
- Typical information: parties and context, the report narrative, categorized issue type, notes, documents and evidence, tasks with deadlines, interview records, the running audit history, current stage.
- Primary actions: add notes/documents, create and complete tasks, change status, record decisions, adjust access, link related cases.

### Intake / reporting form

The employee-facing front door.

- Purpose: let someone raise a concern — or ask for support — safely.
- Typical information: structured, guided questions (what happened, who was involved, when, where), chosen level of anonymity, consent to be contacted.
- Primary actions: submit the report; afterwards, return via a secure reference to add information and follow progress.

### Investigation workspace

Where fact-finding is organized (deepest in investigation-centric products).

- Purpose: structure the inquiry so it is thorough, fair, and consistent.
- Typical information: investigation plan, interview list with question templates, evidence library, chronology/timeline.
- Primary actions: plan and log interviews, upload evidence, record findings, generate the investigation summary/report.

### Analytics and reporting

- Purpose: turn case data into organizational insight for ER leaders, HR leadership, and the board.
- Typical information: volumes and trends by issue type / unit / geography / time, resolution and timeliness metrics, hotspots and repeat patterns, comparisons against peer benchmarks where offered.
- Primary actions: configure views, drill down, export or share reports.

### Administration / configuration

- Purpose: encode the organization's own process.
- Typical information: case categories, workflow definitions per case type/region, routing and escalation rules, permission roles, retention settings.
- Primary actions: configure workflows and forms, manage roles and access, maintain templates.

## Important Rules / Behaviors

**Confidentiality is structural, not a setting.** Case data is visible only to the people who need it for that case. This is the load-bearing rule of the Type: employees report through it, subjects' careers depend on it, and the organization's legal position rests on it. Role-based access with per-case visibility is how products implement it; some add an explicit privilege marker for legally sensitive matters.

**The history is the defense.** Every action, note, and decision is recorded, attributed, and time-stamped, and the record is not meant to be edited away. When a case is challenged months or years later, the audit trail is what the organization produces. Vendors position this against the spreadsheet/email alternative, and it drives documentation behavior throughout the process.

**Anonymity must survive the process.** If a reporter is anonymous, the system must let the case proceed — including follow-up questions — without unmasking them. Two-way anonymous messaging and secure status references exist for this reason; breaking anonymity is treated as a design failure.

**Similar cases should be handled similarly.** Enforced workflows and templates exist to reduce variation in how comparable matters are treated — consistency is both a fairness requirement and a legal one. Configurability per case type/region exists within this frame: organizations encode their own process, then the system holds them to it.

**Prioritization reflects risk.** Triage is not first-come-first-served; the most serious matters (potential harassment, safety, retaliation) are flagged and moved to the front, with escalation when work stalls.

**The case outlives the incident.** Records are retained as organizational history; repeat names and patterns across matters are surfaced deliberately, and in some products follow-up (such as retaliation check-ins with the reporter) extends past resolution.

## Variants

Common shapes of the same Type:

- **Pure-play ER platform** — case management purpose-built for employee relations teams, often bundled with anonymous reporting, investigation methodology, aftercare, and ER-specific analytics. The ER team is the whole world of the product.
- **Multi-department investigation platform** — the same case engine shared by HR/ER, ethics and compliance, security, fraud, and other investigative functions. ER is one configured use among several; process templates and permissions separate the populations.
- **Reporting-first misconduct platform** — intake and safe reporting are the headline (anonymous/named reporting, support requests), with case management ensuring every disclosure is handled and documented; common in UK and education-sector deployments, where regulatory-evidence framing is strong.
- **Sector deployment: education** — universities run the same report-and-handle pattern for student as well as staff misconduct, with advisors rather than investigators as the primary handlers in many cases.
- **Embedded module** — the capability appearing inside broader HR service-delivery or compliance suites, sharing the platform's identity, access, and integration machinery.

A variant remains a variant of this Type as long as the core holds: a confidential case about a workplace people-matter, moved through an enforced process to a documented resolution. When the "case" population changes fundamentally — customers instead of employees, corporate legal matters instead of workplace conduct — the deployment is drifting toward a different Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| HR Case Management (HR service delivery) | closest sibling | Employees raise **service requests** (questions, transactions) resolved against SLAs with knowledge bases; the employee is a customer. ER case management handles **sensitive matters between people** with investigation logic, privilege, and defensibility. A help-desk queue has no privilege marking, no guided investigation process, and no per-case access isolation for sensitive matters. |
| Whistleblowing / Speak-up Platform | upstream intake sibling | Speak-up platforms center on **safe disclosure**: anonymity guarantees, channel coverage, reporting regulation. ER case management centers on the **handled case**. The two are frequently bundled — a hotline feed auto-converting into cases — but the defining object differs: the disclosure channel vs the case lifecycle. |
| Corporate Investigation Management | same pattern, different owner | The same case/investigation structure applied to fraud, bribery, security, and other corporate-legal matters, owned by legal/ethics/security. Multi-department products literally share one engine across both; ER case management is the HR-owned, workplace-conduct slice. |
| HRIS / Employee Record System | process layer over the record | The HRIS is the system of record for employment data (jobs, status, compensation). ER case management syncs employee data from it and manages **matters about people**, not the employment record itself. |
| Complaint & Escalation Management | analogous shape, different population | Customer complaint handling shares the case pattern, but the parties are customers and companies, and the employment-law fairness regime is absent. |
| Business Case Management Platform | generic pattern | Generic case management supplies record + routing + lifecycle without the ER subject matter, the party/fairness semantics, or the confidentiality regime. ER case management is a domain instantiation of that pattern. |
| Case Law / Litigation-oriented legal systems | downstream context | Litigation and eDiscovery tools may later consume ER case records as evidence, but they operate on legal matters and holds, not on the live handling of workplace issues. |

The two boundaries worth internalizing: against **HR service-delivery case management** (service request vs sensitive matter — different objects, different access regime, different stakes) and against **speak-up platforms** (disclosure channel vs handled case — usually bundled, conceptually distinct).

## Representative Products

- HR Acuity — pure-play employee relations and HR case management platform (intake, investigations, aftercare, analytics)
- Case IQ — configurable investigation case management spanning HR/ER, ethics, fraud, security, and Title IX, with bundled hotline intake
- Culture Shift — UK reporting-first misconduct platform (named/anonymous reporting + case management + analytics), strong in higher education and public sector

These three were chosen for different product philosophies (ER-specialist vs multi-department investigator tool vs reporting-first platform) and different market segments (US enterprise, North America multi-sector, UK/education). The defining core was checked against this spread to avoid over-fitting to any single packaging or region.

## Sources

Research date: **2026-09-06**

- HR Acuity — Employee Relations & HR Case Management: https://www.hracuity.com/platform/hr-case-management/
- HR Acuity — Workplace Investigation Management: https://www.hracuity.com/platform/investigation-management/
- HR Acuity — Anonymous Workplace Reporting: https://www.hracuity.com/platform/anonymous-employee-reporting/
- HR Acuity — corporate site / platform overview: https://www.hracuity.com/
- Case IQ — Case Management Software: https://www.caseiq.com/product/case-management-software
- Case IQ — corporate site and FAQ: https://www.caseiq.com/
- Culture Shift — Case Management: https://www.culture-shift.co.uk/case-management
- Culture Shift — corporate site (Report + Support™ platform): https://www.culture-shift.co.uk/

> Sourcing limitation: vendor help-center documentation (step-by-step operational guides) was not reachable from the research environment on 2026-09-06; attempts to fetch a hotline/incident vendor (NAVEX) and suite-embedded HR service-delivery documentation (ServiceNow) failed and were abandoned. All findings rest on official product pages and FAQs. Accordingly, this document describes structure and behavior conceptually and deliberately avoids precise state names, numeric limits, and configuration details; such specifics were not directly observed.
