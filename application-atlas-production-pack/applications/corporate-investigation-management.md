# Corporate Investigation Management

## Overview

A **Corporate Investigation Management** application is the organization's system of record for internal investigations into alleged wrongdoing — misconduct, fraud, harassment and discrimination, policy violations, whistleblower reports, security incidents, and similar matters. It holds each investigation as a confidential case, moves the case through a managed lifecycle from intake and triage to a recorded determination, and accumulates the fact-finding record — evidence, interviews, notes, and tasks — that makes the outcome defensible to auditors, regulators, courts, and the organization's own leadership.

The problem it solves is structural: investigations are sensitive, legally consequential, and must be run consistently. Organizations that run them over spreadsheets, email, and shared drives cannot document decisions, control who sees what, or prove what happened from intake to closure. This application type exists to make the investigation itself — not just its outcome — a governed, attributable, retrievable record.

The boundary is important. The **reporting channel** through which concerns arrive (hotlines, anonymous web forms, speak-up apps) is its own neighboring type; this type centers the **handled case** — what happens after a report exists. The **evidence-analysis machinery** used when an investigation requires forensic collection of digital material is likewise a neighboring type; this type holds the case and its findings, not the forensic tooling. And the **program-level conduct registers** of an ethics program (conflict-of-interest disclosures, attestations) are a different object entirely; this type begins where an allegation needs fact-finding.

## Users & Context

Primary users are the people who conduct and manage investigations inside an organization:

- **Investigators and case managers** — in ethics & compliance offices, HR / employee relations, legal departments, corporate security, and fraud or financial-crime teams. They own cases, plan fact-finding, conduct interviews, record evidence, and write up findings.
- **Decision-makers** — compliance officers, HR leaders, general counsel, security leadership — who review findings, decide outcomes (discipline, remediation, escalation), and may be handed a case at determined points.
- **Program administrators** — who configure case categories, workflows, forms, routing rules, and access rights, often per department or region.

Secondary participants:

- **Reporters** — employees, and in some deployments third parties such as contractors and suppliers — who submit the concern through intake channels and may exchange follow-up messages with the case team, often anonymously.
- **Leadership, boards, and auditors** — as consumers of aggregate reporting rather than operators: case volumes, cycle times, substantiation rates, trends, and audit-ready exports.

The work context is episodic and high-stakes: a case may sit quiet for days while evidence is gathered, then intensify around interviews and deadlines. Multiple departments often share one system while seeing only their own slice. Everything in the system is presumptively sensitive: the people involved are identifiable, the allegations are unproven, and mishandling carries legal, regulatory, and reputational exposure.

## Core Model

### The Defining Core

The application's world is organized around three structures that exist together:

```text
Allegation / matter of concern
  └── Case of record  (confidential, identified, access-restricted)
        ├── Managed investigation lifecycle
        │     (intake/triage → assignment → fact-finding → resolution)
        ├── Fact-finding record
        │     (evidence, interviews, notes, tasks — attached to the case)
        └── Recorded determination
              (finding + outcome/actions, at closure)
```

- **The case of record.** Every investigation is a persistent, individually identified case carrying the allegation: what is alleged, against whom, when, under which policy or law, and reported by whom (or by an anonymous reporter). The case is confidential by construction — access is restricted by role, because its content concerns identifiable people and unproven allegations. Without the case object, the software degrades into a generic tracker.

- **The managed investigation lifecycle.** The case moves through an organization-defined path: intake and triage, assignment to an investigator, fact-finding, review, and resolution. The stages, routing rules, and states are configured by the adopting organization — per case type, department, or region — rather than fixed by the software. Without the managed lifecycle, the system is only an evidence archive.

- **The fact-finding record.** As the investigation proceeds, its substance accumulates on the case: documents and other evidence, interview plans and interview records, notes, tasks and milestones, and a log of actions taken. This record is the investigation's durable core — what makes the outcome reviewable and defensible later.

- **The recorded determination.** A case closes with a finding — in the substantiated / unsubstantiated class of determinations — and a recorded outcome: actions taken, remediation assigned, notifications made, escalations to authorities or leadership where warranted. The closure is itself part of the record.

Remove any one of the three and the type dissolves: without the confidential case, a workflow tool over allegations; without the lifecycle, a document store; without the fact-finding record and determination, an intake register.

### Standard Capabilities

Mature products commonly carry the following around that core. They make the type practical at organizational scale, but they are not what makes the product an investigation management system:

- **Multi-channel intake** — web forms, hotlines, email, mobile reporting, and system integrations feeding cases in, with anonymous-or-named reporting options and guided forms that capture consistent detail.
- **Routing and triage automation** — automatic assignment by case type, region, severity, or workload; notifications, reminders, escalations, and bulk actions.
- **Configurable workflows and forms** — case categories, questionnaires, and stage flows shaped per department, geography, or issue type, typically without code.
- **Two-way reporter communication** — case teams exchange messages with the reporter from within the case, including anonymous follow-up.
- **Case linking and pattern detection** — surfacing related cases and repeat subjects so investigators see patterns early.
- **Audit trail** — a complete, attributable history of case activity, including who viewed or edited what.
- **Analytics and reporting** — dashboards over case volumes, cycle times, outcomes, and trends; board- and regulator-ready exports; benchmarking in some products.
- **AI assistance** — increasingly common: case summaries, timeline building, drafting support, translation, related-case suggestions, and intake guidance.
- **Integrations** — HRIS and employee data for routing and subject identification, single sign-on, policy and training systems, and APIs.
- **A role model** — investigators/case managers, decision-makers, administrators; reporters as authenticated or anonymous external submitters.

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:      Case of record
Realizations: multi-type case engine shared across departments;
              department-specific case types under one system;
              a case born directly from a reporter's submission

Concept:      Lifecycle
Realizations: organization-configured stage workflows;
              vendor-named methodology frameworks layered on the same arc;
              simple fixed pipelines in lighter products

Concept:      Fact-finding record
Realizations: structured case fields + attachments + activity log;
              guided interview protocols and templates;
              centralized documentation stores with privilege marking
```

A reader who has only seen one implementation — say, a compliance suite's case module — should still be able to recognize a standalone HR investigation tool or a security team's case system as the same type.

## How It Works

### From concern to case

```text
Concern arrives (web form / hotline / email / integration / staff referral)
→ captured as a structured report or case
→ triaged: categorized, prioritized, checked for related cases
→ routed to the appropriate investigator or team
→ investigator notified; case clock starts
```

Intake commonly auto-converts a submitted report into a case, but cases can also be created directly by staff — a manager raising an employee-relations concern, an auditor referring a finding. The intake channel machinery is common but not the defining structure; the case is.

### Running the investigation

```text
Plan the fact-finding (scope, interview subjects, questions)
→ gather evidence (documents, records, system data, attachments)
→ conduct and document interviews
→ record notes, tasks, and actions on the case
→ reassess scope as facts emerge (expand, link related cases)
```

The case detail record is the workspace for all of this. Everything the investigator does — every attachment, note, interview record, status change — lands on the case and its audit trail. Some products guide this phase with structured interview protocols and planning templates; others leave the method to the team and hold the record.

### Determining and closing

```text
Review the fact-finding record
→ reach a finding (substantiated / unsubstantiated class)
→ determine the outcome: disciplinary action, remediation, policy change,
   escalation to authorities, no action
→ record the determination and actions on the case
→ close the case with its complete, audit-ready file
```

Closure does not erase the case. The closed file remains retrievable — for regulators, auditors, litigation, and the organization's own program analysis — subject to retention rules.

### After the case

Mature deployments loop the case data back into the program: trend analysis over case types and locations, repeat-issue detection, outcome and — where tracked — substantiation-rate reporting, and board-level program reporting. Some products extend into post-case care — supporting affected employees after difficult events — and into remediation tracking that verifies assigned actions complete.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Case list / queue

The investigator's and manager's primary entry surface.

- lists cases filtered by assignment, status, type, priority, age
- surfaces workload, overdue items, and unread updates
- primary actions: open a case, triage and assign, bulk-update, search

### Case detail (the investigation workspace)

The center of the application — one screen holding the whole investigation.

- allegation summary, parties, policy/law references, status and stage
- evidence attachments, interview records, notes, timeline of activity
- tasks and milestones with due dates; workflow stage controls
- primary actions: update status, add evidence/notes, record an interview, assign tasks, communicate with the reporter, document findings, close

### Intake forms (reporter-facing)

The submission surface, often reachable without an account.

- guided questions capturing what happened, who was involved, when, where
- anonymity options with follow-up mechanisms (reference numbers, secure messaging)
- primary actions: submit a report, add to an existing report, exchange follow-up messages

### Dashboards and reports

The program-management surface for supervisors and leadership.

- case volumes by type/region/status, cycle times, outcomes and substantiation
- trend and pattern views; repeat-issue indicators
- primary actions: filter, drill down, export board- or regulator-ready reports

### Administration / configuration

The setup surface for program administrators.

- case categories, workflows, forms, routing rules, access roles
- retention and visibility policies; integration settings

## Important Rules / Behaviors

### Confidentiality is structural

Access to a case is role-gated by default. The system exists precisely because not everyone may see an allegation. Mature products commonly include safeguards so that people implicated in a case cannot access its record — explicitly documented in one sampled product, and consistent with the role-based restriction universal in the sample. Separations between departments (HR seeing HR cases, security seeing security cases) are a standard configuration concern.

### Anonymity must survive the lifecycle

Where a reporter is anonymous, the system preserves that anonymity through triage, communication, and reporting — anonymous follow-up messaging is a common mechanism. Breaking the anonymity guarantee silently would defeat the intake channel feeding the system.

### The record is the defense

Investigations are run "defensibly": every action and decision is logged and attributable, documentation is standardized so similar cases follow the same fair process, and the closed file must stand up to audit, regulatory, or litigation scrutiny. This is why audit trails and structured documentation are load-bearing behaviors, not conveniences. Some products additionally provide privilege marking on documents for cases involving legal counsel.

### States are organization-defined

The lifecycle's stage names and transitions are configured per organization and product; conceptual states (received, under investigation, in review, resolved/closed) recur, but exact labels vary. A case generally cannot skip the fact-finding phase to a determination without the record showing why — the workflow enforces the process the organization has defined.

### Conflicts and fairness constraints

The subject matter imposes fairness rules: consistent process across similar cases, protection against retaliation for reporters, and handoffs to decision-makers at defined points so the investigator is not the sole judge of outcomes. These appear as workflow design (separation of investigation and decision roles) rather than as free-form behavior.

### Retention and export

Closed cases are retained as records — exportable in audit-ready form for regulators, boards, and legal proceedings — and subject to the organization's retention and privacy rules, which in some jurisdictions are set by whistleblowing and employment legislation.

## Variants

- **Department slices of one engine** — the same case structure configured for ethics & compliance, HR / employee relations, fraud, corporate security, Title IX, ombuds, and special-investigation-unit work. Multi-department products share one engine across these; department-specific products configure it for one.
- **Suite-embedded case management** — the case module of a broader governance-risk-compliance or ethics platform, connected to policy, training, disclosure, and risk modules on one data foundation.
- **Speak-up-led platforms** — products originating in anonymous reporting that grew a case-management hub; intake and case handling are tightly joined.
- **Pure-play investigation case management** — standalone systems sold to investigation teams across departments, competing on configurability and investigation-specific features.
- **Methodology-led products** — department products (notably in employee relations) that wrap the case system in a named investigation methodology with guided protocols.
- **Regulatory regimes as variants** — EU deployments shaped by whistleblowing-directive requirements (anonymity, data protection, timelines); US deployments shaped by employment-law and compliance-program expectations; the core case model is unchanged.
- **Hotline-bundled deployments** — intake sold as an operated service (live answer, multilingual) alongside the case system.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Whistleblowing / Speak-up Platform | upstream sibling | centers the reporting channel, reporter protection, and intake compliance; this type centers the handled case lifecycle. Vendors commonly bundle both; intake auto-converting to a case is the join |
| Employee Relations Case Management | HR-owned slice | same case/investigation pattern applied to workplace conduct between people, with employment-law fairness machinery; this type generalizes the subject and owner (fraud, bribery, security, regulatory) |
| Ethics & Conduct Management | program-level sibling | centers conduct-program registers (disclosures, attestations, gifts) with program-level review; hands deep investigation to this type |
| Internal Audit Management | adjacent discipline | audits are methodology-driven, program-scoped examinations producing standing assurance; investigations are allegation-driven fact-finding for a specific matter. Audit findings can intake as cases |
| eDiscovery Platform / Legal Hold Management | evidence machinery | collection, processing, and production of digital evidence for legal matters; no case-lifecycle object of record. Investigations feed eDiscovery when they become litigation |
| Legal Matter Management | downstream / adjacent | a matter is a legal engagement (litigation, dispute, transaction); an investigation may escalate into one. Different lifecycle endpoints |
| Retail Loss Prevention Platform | domain sibling | retail-loss investigations with ORC linking, recovery, and law-enforcement collaboration; same case machinery, different domain vocabulary and actors |
| AML Platform / Fraud Detection Platform | detection-centered neighbor | financial-crime work centered on transaction monitoring and alert decisioning with embedded case handling; this type is investigation-centered, with allegations as the primary origin |
| Cyber Incident Response Platform | technical sibling | security incidents as technical events (alerts, entities, artifacts) with response playbooks; overlap at insider-threat matters, but objects and workflows differ |
| HR Case Management | service-delivery sibling | frames the employee as a customer raising service requests resolved against SLAs; investigation management handles sensitive matters with fact-finding and confidentiality |
| Public Sector / Law Enforcement Case Management | government analog | same skeleton under statutory authority, public-record obligations, and prosecutorial workflow; corporate investigation management is internal and employment-law-bound |
| Business Case Management Platform | generic pattern | record + routing + lifecycle without allegation subjects, fact-finding records, findings, or confidentiality regimes |

The sharpest seam is with the whistleblowing sibling, because vendors bundle both and the market names overlap. The structural test: remove the case-handling lifecycle and a speak-up platform remains; remove the anonymous-channel machinery and investigation management remains.

## Representative Products

- **Case IQ** (formerly i-Sight) — pure-play, multi-department investigation case management (ethics, HR/ER, fraud, security, Title IX, complaints/ombuds/SIU)
- **NAVEX** (EthicsPoint / Whistleblowing & Incident Management) — suite-embedded case management within the largest ethics/compliance platform
- **Vault Platform** (now part of Diligent) — speak-up-led platform whose Resolution Hub is the case-management product
- **HR Acuity** — methodology-led workplace investigation management (employee-relations slice)

The core model was checked against the evidence-analysis pole (forensics-centered corporate investigation tooling) to confirm it belongs to a neighboring type rather than this one.

## Sources

Research date: **2026-09-07**

- Case IQ — home page and "Case Management Software for Every Investigation": https://www.caseiq.com/ , https://www.caseiq.com/product/case-management-software
- NAVEX — "Whistleblowing Software & Solutions" and "EthicsPoint Professional": https://www.navex.com/en-us/platform/whistleblowing-software-solutions/ , https://www.navex.com/en-us/platform/whistleblowing-software-solutions/ethicspoint-professional/
- Vault Platform — home page and "Resolution Hub": https://vaultplatform.com/ , https://vaultplatform.com/products/resolution-hub/
- HR Acuity — "HR Workplace Investigation Management Software": https://www.hracuity.com/platform/investigation-management/
- Exterro — "Corporate Investigations" use case (boundary-informing): https://www.exterro.com/use-cases/corporate-investigations

> Sourcing limitation: live help-center / user-guide documentation was not reachable for the sampled products; all evidence is official product, FAQ, and case-study pages. Precise operational details (exact lifecycle state names, field-level behavior, retention defaults, numeric limits) are therefore not stated in this document; conceptual states are described with the note that exact labels vary by product. One preferred sample (a corporate-security-focused case system) was unreachable and the security-department pole is represented only through case-type evidence.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis against sibling types are recorded in the paired Research Notes.
