# Law Enforcement Case Management

## Overview

A **Law Enforcement Case Management** application — commonly called **investigative case management** — is an investigative agency's system of record for running investigations. It opens cases from reports, tips, complaints, and referrals; holds the investigation's people, organizations, vehicles, locations, weapons, and property as records linked into the case; organizes the investigative work — leads, tasks, interviews, surveillance, documented actions — into one supervised, auditable lifecycle; and ends each case in a recorded outcome: cleared, closed, or referred onward for prosecution.

The defining structure is small:

```text
Investigation case of record
  (opened from a report, tip, complaint, or referral)
└── Investigative entity web
    (people, organizations, vehicles, locations, weapons, property
     linked into the case with roles; connections surfaced across cases)
    └── Supervised investigative lifecycle
        (leads and tasks assigned and worked; actions documented;
         supervisor review; recorded disposition)
```

Everything else commonly associated with these products — task-force deconfliction, intelligence and link-analysis tools, informant registries, evidence custody integration, government-cloud security regimes, statistical reporting — is standard or optional capability layered on that core, not what makes the product an investigative case management system.

Two boundaries frame the Type. When the unit of record is the agency's report of incidents, arrests, and field documentation — kept for statutory and reporting purposes — that is the records side (a police records management system). When the unit of record is a held item with a chain of custody, that is the evidence side. This Type holds the case: the investigation that a report generates and the work that answers it.

## Users & Context

The primary user is the **investigator / detective** — the person to whom a case is assigned and who carries it forward: developing leads, conducting interviews, documenting actions, and building the case toward resolution.

Around the investigator:

- **Supervisors and command staff** — review case activity, approve at agency-defined checkpoints, monitor workload and stalled cases, and control access to sensitive material.
- **Multi-agency and task-force investigators** — work shared cases across organizational boundaries under the governing jurisdiction's rules.
- **Analysts** — search across cases, surface connections between entities, and support the investigation's intelligence picture.
- **Records and intake staff** — feed the case side from reports, tips, and complaints.
- **External partners, most commonly prosecutors** — in deployments that provide it, consult case materials through controlled review surfaces rather than full system access.
- **Administrators** — configure the agency's vocabulary, workflows, review checkpoints, roles, and integrations.

The operating context is the investigative unit of a police department, sheriff's office, state or federal agency, campus or specialized police force, or multi-jurisdictional task force. Cases typically outlive a single shift or officer — they run for weeks, months, or years, survive personnel changes, and accumulate documentation the whole time. The information is sensitive by nature: suspects, victims, juveniles, informants, intelligence sources. Access is therefore role-scoped, actions are logged, and the record is expected to remain complete and defensible for scrutiny by supervisors, courts, and oversight bodies.

## Core Model

### The Defining Core

Three structures, held together. If any one is removed, the product is no longer recognizable as law enforcement case management:

**1. The investigation case of record.** Every matter the agency investigates is a persistent, individually identified case: where it came from (a field report, a tip, a complaint, a referral from another agency or unit), what it concerns (its classification in the agency's offense or case-type vocabulary), who is assigned, what its current status is, and everything that has accumulated on it. The case — not the report, not the person, not the task — is the spine the investigation hangs on. A single report may generate a case; several related reports may be consolidated into one.

**2. The investigative entity web.** The who and what of the investigation are held as records in their own right — people (suspects, victims, witnesses, informants), organizations (gangs, crews), vehicles, locations, weapons, and property — and linked into the case with their role. Because entities are records rather than free text, the system can surface connections: the same person appearing under different aliases, the same location recurring across cases, the same vehicle linking two matters. This web is what turns a folder of narratives into an addressable investigation.

**3. The supervised investigative lifecycle.** Investigation is managed work. Leads and follow-up actions are assigned to named investigators as tasks; each investigative action is documented back into the case as it happens; the case advances through the agency's configured statuses under supervisory review and approval; and it ends in a recorded disposition — cleared, closed, inactive, or referred onward (most commonly to a prosecutor). Stalled cases are surfaced, not forgotten.

Remove any one and the Type collapses: without the case of record there is nothing to investigate or manage; without the entity web the case is a narrative document with no addressable who or what; without the supervised lifecycle it is a static case folder — the "management" gone.

### What Mature Products Add

These capabilities are widespread in current products and make the core operable, but they are not what defines the Type:

- **Case file documentation** — narratives, supplemental reports (interviews, surveillance, warrant activity, canvasses), notes, and attachments held in one organized, searchable case file, with timestamps on entries and, in some products, version tracking.
- **Task and lead machinery** — assignment of follow-up work with owners, deadlines, reminders, and completion tracking; investigators can document updates from the office or the field.
- **Supervision surfaces** — dashboards of open cases, assignments, workload, overdue tasks, and aging cases; approval workflows and review checkpoints configured to the agency's process.
- **Cross-case connections** — querying across the case population to discover shared suspects, vehicles, weapons, and locations; automatically assembled investigation timelines; link-analysis visualization in more analysis-heavy products.
- **Evidence linkage** — the case holds references to the property and evidence associated with it. Custody depth varies by packaging: some products embed evidence records with custody logging inside the case file, others link to a dedicated evidence management system.
- **Integration spine** — connections to records management (reports flow in), dispatch (incident context), evidence systems, and prosecution or court systems (case materials flow out); sharing surfaces for prosecutors and partner agencies.
- **Configurable vocabulary and workflow** — the agency's own case types, field labels, statuses, and review steps, configured during implementation rather than imposed by the vendor.
- **Security and auditability** — role-based permissions, comprehensive audit trails, strong authentication, and encryption; in the US market these systems are commonly operated under criminal-justice information security expectations.
- **Reporting and statistics** — caseload, clearance, and trend reporting across investigators, units, case types, and time.

### One Structure, Many Implementations

The core model is written conceptually. Current products realize each concept differently:

```text
Concept:   Case intake
Realized as:  RMS report conversion, tip and complaint forms,
              referral intake, triage queues with one-click promotion

Concept:   Entity web
Realized as:  agency-wide person/vehicle/location databases,
              gang and organization registries, informant files

Concept:   Investigative action
Realized as:  task assignments, lead tracking, supplemental reports,
              interview and surveillance documentation, warrant logs

Concept:   Supervision
Realized as:  review checkpoints, approval workflows, aging alerts,
              real-time workload dashboards

Concept:   Outcome
Realized as:  closure and clearance statuses, prosecutor handoff
              packages, controlled external review portals
```

A reader who has only seen a modern cloud product should still be able to recognize an older or differently packaged implementation from the core model alone — a paper-era detective case file (a folder per case, person cards linked to the case, lead sheets worked and signed, supervisor sign-off before closure) satisfies the same three structures without any of the modern machinery.

## How It Works

### Intake: becoming a case

```text
report, tip, complaint, or referral arrives
→ triaged and evaluated for investigative merit
→ promoted to a case: classified, prioritized, assigned
→ case opened with its identifier and structured record
```

Not everything becomes a case — triage is part of the intake design. Once promoted, the case exists as the persistent record that every later action attaches to.

### The investigative loop

```text
review the case and its linked entities
→ develop leads
→ assign follow-up tasks (interviews, canvasses, surveillance,
   records checks, lab or forensic submissions)
→ document each action as it happens: supplemental report, notes,
   attachments, timestamps
→ link newly surfaced entities into the case with their roles
→ re-evaluate: further leads, or move toward resolution
```

The loop is the heartbeat of the product: work is assigned, performed, and — critically — documented inside the case, so the case file continuously reflects the true state of the investigation. Because entities are linked rather than narrated, each new person or vehicle added becomes queryable, and connections to other cases surface automatically.

### Supervision and progression

```text
supervisor monitors case activity, workload, and aging
→ reviews and approves at agency-defined checkpoints
→ case status advances (active → suspended or inactive → cleared or
   closed; exact labels are the agency's own)
→ stalled or overdue cases surface for intervention
```

Supervision is structural rather than informal: approval steps, sign-offs, and aging alerts are configured into the workflow, and dashboards give supervisors a live view of the unit's caseload.

### Resolution and handoff

```text
investigation reaches an outcome
→ recorded disposition (cleared, closed, or referred onward)
→ case package assembled for the prosecutor: reports, evidence
   references, timelines
→ external review through a controlled surface where provided
→ case retained and searchable per agency rules
```

Closure is a governed act, not silence: the disposition is recorded, and in many deployments the end of the investigation is the beginning of the prosecutor's — the case management system's job is to hand over a complete, defensible record.

### Capability tiers

**Defining core** — without these, not this Type:

- investigation case of record opened from intake
- entity records linked into cases with roles
- managed, documented investigative work
- supervised progression to a recorded disposition

**Standard mature capabilities** — present in most current products:

- case file documentation with supplemental reports and timestamps
- task/lead assignment with deadlines and reminders
- supervisor dashboards, approvals, aging alerts
- cross-case entity connections and timelines
- evidence linkage
- RMS/dispatch/evidence integration and prosecution handoff
- configurable vocabulary and workflow
- role-based access and audit trails
- reporting and statistics

**Variant / optional** — depends on agency scale, segment, and jurisdiction:

- task-force and multi-jurisdiction sharing with deconfliction
- specialized configurations: narcotics, gangs, child-exploitation and human-trafficking units, criminal intelligence programs, confidential informant registries
- link-analysis visualization; intelligence database depth
- government cloud vs on-premises deployment; mobile field capture
- controlled external portals for prosecutors and partners

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Case workload list

The investigator's entry surface.

- typical information: assigned cases, status, priority, aging, last activity
- primary actions: open a case, pick up an assignment, filter by unit or status

### Case folder

The case's home — a structured file with everything attached to the matter.

- typical information: classification, status, assigned investigators, linked persons and entities, narrative and supplemental reports, evidence references, tasks, documents, history
- primary actions: document an action (add supplemental report or note), link an entity, create a task, attach files, change status

### Entity record

The record for one person, organization, vehicle, or location.

- typical information: identifiers and aliases, role appearances across cases, linked vehicles/locations/organizations, media
- primary actions: link to a case, search appearances across cases, update details

### Task / lead board

The unit's work queue.

- typical information: open tasks by case, owner, due date, age
- primary actions: assign, reassign, complete, flag overdue

### Timeline and link views

The investigation's shape at a glance.

- typical information: chronological events (actions, evidence collection, involvement), entity-relationship views
- primary actions: inspect an event, trace a connection, export for briefing

### Supervisor dashboard

- typical information: open cases, assignments and workload, overdue and aging cases, review queue
- primary actions: review and approve, reallocate, drill into a case

### Intake / triage surface

Where matters become cases.

- typical information: incoming tips, complaints, referrals, converted reports
- primary actions: evaluate, promote to case, reject or route

### External review surface (deployment-dependent)

- typical information: case materials exposed to prosecutors or partner agencies under controlled, sometimes time-limited, access
- primary actions: review documents and evidence references, request or acknowledge items

### Administration and configuration

- typical information: case types, statuses, field vocabulary, workflow and approval steps, roles and permissions, integration settings
- primary actions: configure vocabulary, define review checkpoints, manage users and access

## Important Rules / Behaviors

- **The case is the spine.** Reports, entities, tasks, evidence references, and outcomes all attach to the case; one entity may link to many cases, and related matters may be consolidated. Work that is not recorded against a case is, operationally, work that did not happen.
- **Documentation is append-oriented.** Investigative actions are documented as new, timestamped entries — supplemental reports and notes linked permanently to the case. Some products add version tracking. The record is expected to remain complete and defensible; history is preserved rather than rewritten.
- **Supervisory review is built into the workflow.** Approval checkpoints, sign-offs, and aging alerts are configured agency-side; a case does not quietly drift to closure — the disposition is a recorded, reviewed act.
- **Vocabulary is the agency's own.** Case types, statuses, roles, and field labels are configured per agency; nothing in the workflow depends on a universal terminology. Status labels differ substantially between agencies and products.
- **Access is role-scoped and audited.** Who can see and act on a case is governed by role, and the system's own usage is logged. Sensitive populations (juveniles, informants, intelligence sources) and multi-agency sharing operate under additional access discipline.
- **Evidence references vs evidence custody.** The case holds the links to property and evidence; the unbroken custody chain lives in the evidence side. Products differ in whether custody logging is embedded or delegated to a dedicated evidence system, but the case's job is the investigative record, not the custody ledger.
- **Closure is a disposition, not abandonment.** Whether cleared, closed, inactive, or referred for prosecution, the outcome is recorded and the case remains a searchable part of the agency's investigative memory.

## Variants

- **Standalone pure-play products** — dedicated investigative case management sold on its own, integrating to an existing RMS; common in agencies of all sizes and in task forces.
- **Modules inside police operational platforms** — investigation and crime management as a named module of an agency-wide records platform, alongside intelligence, property, custody, and case-preparation modules; common in large agencies.
- **Institutional public-safety deployments** — campus police, hospital and gaming security, and other organizations with sworn or quasi-sworn investigative functions running the same case machinery at smaller scale.
- **Task force and multi-jurisdiction operation** — shared cases, cross-agency access, and deconfliction under jurisdiction rules.
- **Specialized-unit configurations** — narcotics, gangs, child-exploitation, human trafficking, criminal intelligence (including informant registries), each adding domain-specific records and controls.
- **Deployment variation** — government cloud vs on-premises; browser-based vs mobile field capture; jurisdiction-specific security accreditations.

A variant should remain a **Variant**, not become a separate Type, unless it changes the users, core objects, workflow, or rules so much that the defining core no longer applies.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Police Records Management System | upstream sibling, interlocked | the RMS is the agency's record of incidents, arrests, and field reports kept for statutory and reporting purposes; this Type holds the investigation the report generates — leads, tasks, entity webs, supervised progression. Vendors state the distinction directly: the RMS records incidents and arrests; case management manages investigations. Suite platforms ship investigation management as a module inside the RMS — packaging, not identity |
| Evidence Management System | tightly interlocked | the evidence system of record is the held item — chain of custody, storage, authorized disposition; this Type holds the investigation's narratives, persons, and outcomes. Case links evidence; custody machinery does not live on the case side |
| Computer-aided Dispatch / CAD | upstream, time-separated | CAD is the real-time dispatch of status-tracked units to live incidents; incident data flows onward to records and then to investigation. No real-time unit status exists here |
| Prosecutor Case Management | downstream sibling | the prosecution phase — charges, court process — belongs to the prosecutor's office; this Type hands off a defensible case package and may expose review surfaces, but does not manage prosecution |
| Court Case Management System | downstream consumer | court-phase docket, hearing, and filing machinery; consumes outcomes, does not run investigations |
| Corporate Investigation Management | same machinery family, different domain | corporate matters with legal, HR, and compliance semantics and actors; this Type is criminal-justice framed — suspects, victims, offenses, clearance, prosecution handoff |
| Public Sector Case Management | different "case" | citizen-service request handling; the case is a service request, not an investigative matter |
| Code Enforcement Management | adjacent enforcement | civil, property-anchored enforcement (violation → notice → compliance/fines); no investigative entity web or clearance semantics |
| Digital Forensics Platform | feeding discipline | technical examination of devices and data producing findings; findings and artifacts flow into cases as evidence, but examination is not case management |

The most important boundary is with the **Police Records Management System**, because the two are designed to interlock and are often sold together. The test is the system of record: remove the investigation workflow and whatever remains is a records system; remove the statutory report-of-record role and add case lifecycle, entity webs, and supervised progression, and whatever remains is this Type.

## Representative Products

- **Case Closed Software** — standalone pure-play investigative case management for agencies and task forces; tip-to-disposition lifecycle, entity database, informant and intelligence modules, cloud or on-premises
- **Omnigo (Investigation Case Management)** — named ICM module within a public-safety platform; case files built from incident reports, cross-case connection queries, custody-aware evidence logging; municipal, campus, and institutional agencies
- **NicheRMS365 (Niche Technology)** — large-agency police operational platform whose module set includes Investigation & Crime Management alongside intelligence, property, custody, and case-preparation modules; strong UK and North American presence
- **Mark43 RMS** — cloud records management platform included as the records-side contrast: reports, arrests, and statutory compliance on one side; investigation workflow on the other

The defining core was checked against paper-era investigative practice (case folders, person cards, lead sheets, supervisor sign-off) and against differently positioned products (suite modules, institutional agencies, non-US forces), so the definition does not assume cloud delivery, link-analysis tooling, statutory reporting regimes, or any specific agency size.

## Sources

Research date: **2026-09-08**

- Case Closed Software — homepage and Law Enforcement Case Management product page: https://caseclosedsoftware.com/ , https://caseclosedsoftware.com/cms/
- Omnigo — Investigation Case Management solution page and Public Safety industry page: https://www.omnigo.com/solution/investigation-case-management-software/ , https://www.omnigo.com/industry/public-safety-software
- Niche Technology — NicheRMS365 homepage (module set and customer quotations): https://nicherms.com/
- Mark43 — Mark43 RMS product page: https://mark43.com/platform/mark43-rms/

> Sourcing limitation: vendor help-center articles and support portals were not reachable from the research environment on 2026-09-08 (blocked, 403, 404, timeout, or transport error across seven additional vendors attempted, including LeadsOnline, Motorola Solutions, Hexagon, Tyler Technologies, Zuercher, Unisys, and CrimePad). Evidence is therefore at the product-page structural level — named modules, capability descriptions, workflow claims, and vendors' own category definitions — rather than at the level of exact procedures, field lists, or numeric limits. No precise counts, durations, status vocabularies, or default settings are asserted in this document; the case lifecycle and entity roles are described at the conceptual strength their evidence supports.
