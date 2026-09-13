# Prosecutor Case Management

## Overview

A **Prosecutor Case Management** application is the case-file system of record used inside a prosecutor's office — district attorney, state's attorney, county attorney, solicitor-general, attorney general — to manage criminal prosecutions from the moment a law-enforcement agency refers a case until final disposition.

Its defining core is three structures held together:

```text
Law-enforcement referral
  → prosecution case of record (defendant × alleged offenses)
      → charging decision (accept / add / amend / reject charges)
          → charging documents filed
              → case moves through the court process
                  → disposition
```

- the **prosecution case of record** — a persistent, identified case file binding a defendant to alleged offenses, accumulating the office's documents, events, people, and money across the case's whole life
- the **charge as the managed object** — the office reviews the referral and exercises the charging decision, produces the charging documents, and keeps the charge history
- the **office's own tracking of the court process** — hearings, calendars, deadlines, case status, and final disposition, recorded on the case

Everything commonly associated with modern products — defense-facing discovery portals, victim portals, evidence repositories, court-system integrations, workflow automation — is widespread supporting structure, not the definition. Older prosecutor case-tracking programs (some in use for decades before cloud software existed) already had the case file, the charge management, and the court-process tracking, and would still be recognizable under this definition.

## Users & Context

The user population is an entire prosecutor's office, organized around the case:

- **Prosecutors / assistant prosecutors (attorneys)** — review referrals, make charging decisions, prepare and try cases; the case file is their working record in and out of court
- **Paralegals and legal support staff** — prepare charging documents, manage discovery compilation, maintain case records
- **Victim-witness coordinators** — manage victim contact, services, and notifications
- **Office investigators** — run follow-up investigations tied to cases
- **Administrators / office management** — configure workflows, assign cases, monitor caseload and office-wide statistics

The work context is a government legal office under statutory obligations: filing deadlines, speedy-trial constraints, discovery-disclosure duties to the defense, and victim-rights obligations. The system is used in the office, remotely, and in court. Security expectations are criminal-justice grade: role-based access, audit trails, and compliance with criminal-justice information security regimes.

## Core Model

### The Case of Record

The center of the system is the **case**: a persistent record binding one defendant (a person-centric record with identifiers, aliases, demographics) to one or more alleged offenses in a jurisdiction. Around it accumulate:

- **People** — defendant, co-defendants, victims, witnesses, officers, with their roles on the case
- **Charges** — the prosecutable objects (below)
- **Documents** — police reports, charging documents, motions, correspondence, evidence files, generated from templates or received from partner agencies
- **Events** — hearings, court dates, internal deadlines, tasks, and the office's actions on the case
- **Money** — restitution, fees, diversion-related amounts where applicable

A person-centric model matters: the same defendant, victim, or officer recurs across many cases, and office-wide questions ("all cases involving this person") are asked across the case population.

### The Charge

The charge is what makes this prosecution software rather than generic case tracking. A case typically enters as a **law-enforcement referral** — the system tracks which agency initiated the investigation or referred the charges. The office then reviews the referral and makes the charging decision:

```text
Referral received (police report, evidence)
  → review
  → charge decision: file / add / amend / reject charges
  → charging documents produced (complaint, indictment, etc.)
  → charge history retained as charges change over the case's life
```

Charging language is commonly selected from structured lists rather than typed freehand, and the charge record drives downstream documents and statistics.

### The Court-Process View

The office maintains its own operational view of the case's movement through the court process — pretrial, trial, and post-adjudication phases — tracking hearings and court events, calendars and deadlines, case status, and the final disposition. The court's own system remains the authoritative docket; the prosecutor's system exchanges data with it (docketing information, hearing requests, filed-charge data) rather than replacing it.

### Standard Capabilities

Mature products commonly add, on top of the core:

- **Discovery management** — compiling, organizing, redacting, and disclosing discovery to the defense; increasingly through a defense-facing portal that notifies opposing counsel when discovery is available and logs what was released
- **Evidence and media tracking** — physical and digital evidence bound to the case; media repositories for reports, photos, video, audio
- **Victim and witness management** — victim records, services provided, notifications, court-date communication, and statutory reporting (e.g., federal crime-victim-fund reporting in the US)
- **Document generation** — office templates auto-populated from case data: charging documents, subpoenas, motions, victim letters, hearing notices
- **Subpoena management** — generating and tracking subpoenas, including batch issuance
- **Financial tracking** — restitution, discovery fees, diversion-program money
- **Workflow automation** — task assignment by case type, deadline notifications, key-date-driven workflows
- **Integration with justice partners** — data exchange with law-enforcement records systems and court case-processing systems; calendar/email integration
- **Conflict checking** — checking attorney involvement and relationships when people are added to cases (present in some products; not universal in the researched sample)
- **Investigator support** — tools for the office's own investigators

## How It Works

### Case intake and charging

```text
Law-enforcement agency refers a case (report, evidence — often electronically)
→ office creates or auto-creates the case, linked to the defendant and the referring agency
→ prosecutor reviews the referral
→ charging decision: accept, add, amend, or reject charges
→ charging documents generated from case data and filed (electronically or on paper)
→ case enters the court process
```

The referral can also be rejected or diverted — rejection and diversion/deferred-prosecution outcomes are part of the charging decision, not failures of it.

### Case progression

```text
Court events scheduled (hearings, trial dates)
→ office calendar and deadlines maintained (including speedy-trial-type constraints)
→ discovery compiled, redacted, and disclosed to the defense as it becomes available
→ subpoenas issued for witnesses
→ motions and case documents produced and filed
→ status updated as the case moves through pretrial, trial, post-adjudication
→ disposition recorded (conviction, plea, dismissal, acquittal; diversion completion)
```

This is the standing interaction loop: staff and attorneys continuously update the case file as the court process advances, and the calendar/deadline layer keeps the office ahead of statutory constraints.

### Supporting loops

- **Discovery loop**: material arrives from law enforcement → organized against the case → reviewed/redacted → released to the defense → release logged; supplemental discovery repeats the loop
- **Victim loop**: victim identified on the case → services and rights obligations tracked → notifications sent at key events → statutory reports compiled
- **Supervision loop**: office management assigns cases, balances workload, and monitors caseload, deadlines, and outcomes across the office

## Interfaces

Exact layouts vary by product; the following surfaces are described conceptually.

### Case list / caseload view

The user's entry surface: the cases assigned to them or to the office, with status, next court dates, and pending tasks. Primary actions: open a case, search, filter by stage or deadline.

### Case file (single-case workspace)

The central surface — a one-screen view of everything on a case: defendant and people, charges and charge history, documents, evidence, events and calendar, money, and notes. Primary actions: update charges, add documents and events, generate documents, record activities.

### Charging / referral review

The surface where a referral becomes a case: reviewing the police report, selecting and editing charges (commonly from structured charging-language lists), and producing charging documents.

### Calendar / docket view

Office-wide and per-user views of court dates, hearings, and internal deadlines, with conflict prevention and deadline notifications.

### Discovery workspace

Compilation, organization, redaction, and release of discovery; in portal-based products, a release-management view showing what has been made available to the defense and what they have viewed or downloaded.

### Victim / witness management

Victim records, services provided, contact and notification history, and required reporting.

### Reporting / office dashboards

Caseload statistics, case-status breakdowns, outcome reporting, and statutory/grant reports for office management and government oversight.

### External portals (where offered)

Separate authenticated surfaces for law-enforcement agencies (submitting reports), defense counsel (receiving discovery), and victims (case updates, court dates, document signing).

## Important Rules / Behaviors

- **The charging decision is the gate.** A referral is not yet a prosecution; the case becomes a prosecution when charges are accepted and filed. Rejection and diversion are first-class outcomes of that decision.
- **The court's docket is authoritative; the office's view is operational.** The system exchanges hearing and docketing data with court systems rather than replacing them; discrepancies between the two are a known operational reality.
- **Discovery disclosure is a duty, not a courtesy.** The system tracks what has been disclosed, to whom, and when — and portal-based products log the defense's access. Recalling a released file is a supported, auditable action in some products.
- **Deadlines are structural.** Speedy-trial and filing deadlines drive calendars, notifications, and workflow triggers; missing them has legal consequences, so deadline tracking is a first-class behavior.
- **Access control is role-based and case-sensitive.** Criminal-justice data is restricted by role and often by case assignment; every significant action is auditable.
- **Charges change over a case's life.** Charges are amended, added, and dropped; the charge history is retained because the sequence of charging decisions is itself part of the record.
- **People recur across cases.** Person-centric records mean one defendant or victim may appear in many case files; conflict and involvement checks (where present) run when people are added to cases.

## Variants

- **Office scale**: large metropolitan DA offices with team-based caseload management and workload balancing vs. small offices on streamlined hosted editions
- **Prosecutor kind**: county/district attorneys, city attorneys, state attorneys general (some products offer attorney-general-specific configurations), solicitor-general offices handling lower-level criminal matters
- **Case-type scope**: general criminal; some systems add juvenile, grand-jury, traffic, and civil-forfeiture case types; some handle civil-side work alongside criminal
- **Deployment**: on-premise installations (the historical norm in this market) vs. hosted/SaaS; statewide or multi-agency shared deployments with cross-office search
- **Portal depth**: offices running without external portals (paper-era and minimal deployments) vs. full LEO/defense/victim portal ecosystems
- **Court integration depth**: manual re-entry vs. electronic filing and automated data exchange with court and police systems

## Related Application Types

| Application Type | Distinction |
|---|---|
| Police Records Management System / Law Enforcement Case Management | The police side originates investigations and refers cases; it holds no charging decision. The prosecutor system receives referrals and tracks which agency sent them. |
| Court Case Management System | The court owns the authoritative docket and hearing record; the prosecutor's system holds the prosecution's own case file and exchanges data with the court. Vendors typically sell them as separate products. |
| Public Defender Case Management | Mirror-image sibling: same case lifecycle, opposite party, plus defense-specific concerns (co-defendant conflicts, voucher billing). Separate products from the same vendors. |
| Legal Matter Management / Law Practice Management | Generic matters lack charge semantics, the referral→charging→disposition criminal lifecycle, and the statutory discovery duty to the opposing party. |
| eDiscovery Platform | In this Type, discovery is one support service bound to the prosecution case and driven by the disclosure duty; standalone eDiscovery is a general litigation tool. |
| Legal Docket Management | Docketing is one tracked surface inside the case file; docket management as a Type centers on the docket/calendar itself. |
| Court E-filing Platform | Handles the filing transaction to the court; the prosecutor's system produces the filings and may hand them off. |

The most important boundary is with the court case management system: both track the same court process, but the prosecutor's system is the office's case file and charging record, while the court's system is the docket of record.

## Representative Products

- PROSECUTORbyKarpel (Karpel Solutions)
- eProsecutor (Journal Technologies)
- prosecutorDATA (Justice Works)
- Case 365 (365 Labs)

The core model was checked against the pre-cloud lineage of this market (decades-old prosecutor case-tracking programs documented in office procurement records) to avoid over-fitting to the modern portal-and-integration layer.

## Sources

Research date: **2026-09-10**

- PROSECUTORbyKarpel — https://www.prosecutorbykarpel.com/ (product and feature pages)
- eProsecutor, Journal Technologies — https://www.journaltech.com/eprosecutor
- prosecutorDATA, Justice Works — https://www.justiceworks.com/prosecutor-data
- Case 365 Prosecution, 365 Labs — https://365labs.com/case365/prosecution
- SEARCH Group, Prosecutor Case Management System Functional Requirements — https://www.search.org/files/pdf/PCMS_Functional_Specifications.pdf
- Isabella County PAO software request (legacy-system and capability context) — https://www.isabellacounty.org/wp-content/uploads/2019/10/PAO_Karpel_Software.pdf
- Suffolk VA Commonwealth's Attorney, deployed-system description — https://www.suffolkva.us/306/Case-Management-System

> Sourcing limitation: the SEARCH.org functional-specification PDF could not be text-extracted in the research environment; its content is used only at the level of the indexed excerpt, and no precise numeric requirements are asserted from it. Product pages for two sampled products were available only via search-index excerpts of their official pages. Precise operational details (numeric limits, exact state names, specific integration partners) are intentionally not stated in this document; they remain in the Research Notes.
