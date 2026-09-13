# Court Case Management System

## Overview

A **Court Case Management System** is the court's own system of record: the register in which a court opens identified cases, binds the parties, maintains the official chronological record of everything that happens in each case (the docket), schedules cases into hearings on the court's calendars, records the structured outcomes of judicial decisions, and follows through on the financial consequences (fines, fees, restitution).

Its defining core is small:

```text
Case (identified by case/docket number, classified by case type)
└── Parties bound to the case
    └── Official case register (docket): dated entries of filings, proceedings, orders
        ├── Filings and documents attached to the case
        ├── Hearings scheduled on the court's calendars
        └── Recorded outcome (disposition / judgment / result)
```

It is operated by the court — clerk's-office staff run the day-to-day register, judicial officers decide what gets recorded — and it is the authoritative record of the court's own process, not the record of any single agency around the courtroom. Everything commonly associated with modern court software — electronic filing machinery, online payment portals, inter-agency data exchange, statewide shared platforms, cloud delivery — is widespread standard capability or an implementation variant, not what makes the product a court case management system. A pre-digital court running on paper case files, a docket book, and a printed calendar exercises the same core structure.

## Users & Context

The work environment is a court — a trial court of general or limited jurisdiction, an appellate court, or a specialty court — and the users form three concentric groups.

**Primary operators — the clerk's office / court registry.**

- Clerks and deputy clerks register cases, docket events, accept or reject filings, manage documents, collect and receipt fees, and prepare calendars. They are the system's power users and its day-to-day custodians.
- Court administrators and managers use the same record for caseload reporting, resource planning, and statistics about pending and disposed cases.

**Decision users — judicial officers.**

- Judges and equivalent officers consume the case record in a bench-oriented view: the parties, the charges or claims, outstanding bonds or warrants, prior events and dispositions, and what is on today's calendar. They record outcomes into the system; in mature implementations those recorded outcomes drive the generation of the court's official output documents.

**External users with controlled access.**

- Attorneys of record file documents, receive notices of activity in their cases, and review the docket and filed documents.
- Litigants, including self-represented parties, check case status, calendars, and amounts owed.
- Justice partners — prosecutors, public defenders, law enforcement, probation, motor-vehicle agencies — exchange case data with the court (in statewide deployments they may work directly inside the shared platform).
- The public searches case records and calendars through public-access surfaces, subject to the court's access rules.

## Core Model

### The defining core

**Case.** The container everything hangs from. A case is opened in the court's registry under a **case type** — civil, criminal, family, probate, traffic, appellate, or a specialty category — and carries an identifier (commonly called the case or docket number) that follows the case through its whole life. The case type matters structurally: it determines which events, forms, fees, and stages apply. Each court typically configures its own case-type vocabulary, so the same product is configured differently in different courts, and legislative changes are absorbed by re-configuration.

**Parties.** The identified people and organizations on each side of the case — in a criminal matter, the defendant and the prosecuting authority; in civil matters, plaintiffs, petitioners, and respondents; in family matters, the parties whose status the case concerns. Parties have roles, and role determines what notices they receive and what they may do. Attorneys attach to cases as representatives of parties.

**The docket / case register.** The official, chronological record of the case's events: filings received, proceedings held, orders entered, and their dates. This is the heart of the system. In one canonical description, the court's main record is *the case file, which contains the docket sheet and all documents filed in the case*; a docket is conventionally understood as the list of a case's proceedings, filings, and deadlines, identified by its docket number and treated as a public record. Filing a document typically creates a docket entry — in modern electronic-filing implementations the entry is created automatically and the docket sheet updates immediately.

**Hearings and calendars.** Court proceedings are scheduled occasions on which the court considers a case. Scheduling — matching cases to dates, courtrooms, and the people required — is a distinct working discipline inside the court, supported by calendar surfaces for clerks and judicial officers. Cases move onto and between calendars as their process advances; continuances and rescheduling are normal operations.

**Recorded outcomes.** What the court decides is recorded as a structured result — a disposition, judgment, or outcome — attached to the case and, where the jurisdiction's procedure attaches results to charges, to the specific charge or party. Structure matters: recorded outcomes are actionable, driving which documents are produced, how fees and fines are assessed, what statistics report, and when the case terminates. The catalogue of possible outcomes is maintained as reference data that changes over time, so the outcome recorded is tied to the definitions in force when it was entered.

### Structures attached to the core

**Filings and documents.** Every document that enters or leaves the case is registered against it — submitted filings, generated orders, notices, and warrants. Systems manage versions and preserve the document as filed; some additionally verify over time that filed documents have not been altered. The case file (register + documents) is the durable object of record.

**The financial layer.** Court work carries money: filing fees, fines, restitution, and administrative charges. The system assesses amounts against the case, accepts payments (at the counter and through online portals), tracks payment plans and installment schedules, runs collections on unpaid amounts, and routes money to the appropriate government accounts. In criminal matters the financial record follows the disposition — a sentence that includes a fine creates a payable obligation on the case.

**Reference data and configurability.** Offence/charge definitions, outcome catalogues, event codes, fee schedules, case-type templates, and court and agency details are held as managed reference data. Courts differ, laws change, and the system's behavior is expected to follow the data rather than a code release — which also means historical questions ("what outcome definitions applied then?") are answered date-sensitively.

### One structure, many vocabularies

The core model holds across jurisdictions, but the vocabulary varies with legal tradition — the same concepts appear as *docket / disposition* in one tradition and *listing / results / notices-orders-warrants* in another. The structure stays the same: an identified, typed case; bound parties; an official event register; scheduled proceedings; recorded structured outcomes. Exact stage names, event labels, and outcome catalogues are each court's own configuration, not industry-wide constants.

## How It Works

A case moves through the system in a repeating loop of registration, scheduling, decision, and recording.

### 1. A case is opened

```text
Civil: a party files an initiating document (paper or e-filing)
Criminal: the prosecuting authority sends the case to the court
Traffic/limited: a citation arrives and becomes a case
→ clerk registers the case: assigns case type + case/docket number
→ binds parties, counsel, and (criminal) charges to the case
→ assesses initial fees; case enters the register
```

Filing may happen at the counter or electronically. Electronic filing passes through a review gate: the submission is prepared, fees assessed automatically, routed to court staff, then **accepted or rejected** by a clerk before it enters the record. Only accepted filings become part of the case file and create docket entries.

### 2. Work is docketed as it happens

Every event in the case's life is entered into the register with a date: documents received, orders signed, proceedings held, judgments entered. Modern electronic-filing systems create these entries automatically when documents are filed, update the docket sheet immediately, and notify every registered participant in the case. The docket is simultaneously a working tool (what happened, what is next) and the official account (what the court did, and when).

### 3. The case is scheduled

Clerks match pending matters to dates, courtrooms, and required participants, and build the court's calendars. Judicial officers see their own calendars; attorneys and the public commonly see public calendar views. Conflicts, continuances, and rescheduling are ordinary operations, and the calendar state of every case is visible in the case record.

### 4. The hearing happens and results are recorded

At the hearing the judicial officer works from the case record — parties, charges or claims, bonds or warrants outstanding, prior events. What the court decides is then recorded into the system as structured results, attached to the case (and, where procedure attaches results to charges, to the charge or defendant). From the recorded results the system generates the court's output documents — orders, judgments, notices, warrants — rather than having staff type them afterwards; a single hearing may generate several, addressed to different recipients.

### 5. Disposition closes the judicial phase

When the court's decision is fully recorded, the case reaches a disposition: dismissed, decided, convicted, judgment entered — with the exact terminal states defined per case type by each court. The disposition is the pivot to everything that follows: statistical reporting (caseload figures reported to court administration), records retention, appeals (which proceed as their own cases in the higher court), and the financial follow-through.

### 6. Money follows the case

Fines, fees, restitution, and costs assessed on the case become tracked obligations with their own lifecycle: payment in full or in installments, receipts issued and applied to the case, reminders and collections on unpaid balances, and reporting of relevant outcomes to external registries (most commonly motor-vehicle agencies in traffic and criminal matters — e.g., license suspensions and reinstatements tied to recorded dispositions). Payments arrive at the counter, through online payment portals, or at courtroom terminals, and reconcile against the county's or court's accounts.

### 7. Access loops run continuously

Throughout the case's life: attorneys receive electronic notices of every filing and can review the docket and documents; justice partners exchange data with the court under defined standards; the public searches case records and calendars (in some jurisdictions freely, in others through fee-based access — with opinions and calendars commonly free to view); and clerks keep working the register. The system's permissions are role-based and its actions are logged for audit.

## Interfaces

### Case management workstation

The clerk's primary surface. Purpose: register cases, docket events, process filings, manage documents and money.

- Typical information: case queues, pending filings to accept/reject, event entry forms, fee and payment screens.
- Primary actions: open/register a case, docket an event, accept or reject a filing, attach documents, assess fees, receipt payments, schedule or reschedule.

### Case detail / docket view

The single-case surface every role touches in some form. Purpose: show the case and its whole history.

- Typical information: case number and type, parties and counsel, charges or claims, the chronological docket of entries, attached documents, financials, upcoming hearings.
- Primary actions: open a document, add an entry, view financials, jump to the calendar entry.

### Calendar / listing surface

Purpose: build and manage the court's schedules.

- Typical information: courtrooms and dates, cases listed per session, required participants, conflicts and status flags.
- Primary actions: list a case, move or continue it, assign a courtroom or officer, publish the public calendar.

### Judicial bench view

Purpose: give the decision-maker the case at a glance.

- Typical information: parties and counsel, charges/claims, outstanding bonds or warrants, prior dispositions, calendar position, documents relevant to the decision.
- Primary actions: record results/outcomes, sign or enter orders, continue a matter.

### Public portal

Purpose: let the public and parties interact with the record without coming to the courthouse.

- Typical information: case search by number, name, or date; public calendars; case status; documents subject to the court's access rules; amounts due.
- Primary actions: search cases, view calendars, submit filings (where offered), pay fines and fees. Public access itself is funded differently across jurisdictions — free in many courts, fee-based in others.

### Partner and reporting surfaces

Purpose: share the record with authorized agencies and summarize the court's work.

- Typical information: partner-scoped case views; caseload, age-of-pending, and disposition statistics; configurable dashboards.
- Primary actions: exchange case data under agreed standards; generate reports.

## Important Rules / Behaviors

### The docket is the official record — and it is mostly public

The register of case events is not internal notes; it is the court's account of what it did, and court dockets are generally treated as public records, subject to court orders and access policies in individual cases. This public-record character shapes the whole design: entries are attributed and dated, documents are preserved as filed, and integrity is verified over time.

### Filings enter the record through a gate

Electronic submissions are reviewed and accepted or rejected by court staff before they become part of the case file; fee assessment and routing happen automatically along the way. The accepted filing creates its docket entry immediately and triggers notice to registered participants.

### Recorded outcomes drive what happens next

Results are recorded as structured data, not free text, precisely so they can act: generating the court's orders and notices, assessing financial obligations, feeding statistics, and determining the case's status. Because outcome definitions live in reference data that changes over time, an outcome is interpreted against the definitions in force when it was recorded.

### Privacy and access are role-gated with audit

Access to case data follows role and need: clerks work the record, judges see bench views, partners see scoped views, the public sees what policy allows. Personal identifiers are commonly subject to redaction rules — in some jurisdictions the responsibility sits with the filer, who must acknowledge the rules before filing. Every consequential action is logged for audit, and case files are governed by records-retention schedules that determine how long each record class is kept.

### Case types carry procedure

The events, forms, fees, and terminal states of a case follow from its case type as configured by the individual court. Two courts on the same product can run materially different procedures; the same court's procedures change as legislation changes. This configurability is a structural expectation of the Type, not an add-on.

### The case outlives the courtroom

A disposition ends the judicial phase but not the record's work: payment plans and collections run on, statistical reporting aggregates closed cases, appeals open linked cases in higher courts, and retention schedules hold the file for its mandated life.

## Variants

- **Court level and jurisdiction mix.** Unified trial courts running many case types side by side; limited-jurisdiction courts (municipal, traffic) running high-volume simple matters; appellate courts managing review cycles above trial-court records; specialty courts (drug, problem-solving) with program-shaped progressions.
- **Single court vs statewide platform.** One product instance per court is the classic shape; statewide shared platforms put hundreds of courts on one system so that partners and the public see consistent data everywhere. The shared-platform pole turns the court CMS into the case-data hub of the justice system.
- **Commercial vendor vs government-built.** The market includes long-established commercial suppliers and judiciary-built national systems; both realize the same core structure.
- **Regional process vocabulary.** Jurisdictions name and sequence stages differently (docket/disposition vs listing/results; different charge, notice, and warrant machinery), while the underlying structure — case, parties, register, hearings, outcomes — holds.
- **Public-access funding.** Free public portals vs fee-based per-document access, with opinions and calendars commonly free either way.
- **Where the filing machinery lives.** Integrated into the CMS, or delivered as a separate filing product that integrates with the court's system (with interchange standards governing the connection).
- **Deployment.** Long-lived on-premises installations persist alongside cloud and hosted offerings; migration off legacy systems is a common driver of replacement.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Court E-filing Platform | The intake channel, not the record: prepares, routes, and reviews submissions; without a case register, calendars, or dispositions it remains a filing system. May be a separate product integrated with the court CMS, or bundled inside one program. |
| Jury Management System | Centers on jurors (summons, qualification, panels, juror pay), not cases. Sold as a separate product line by the same suite vendors even though jury fees appear in court financials. |
| Prosecutor Case Management | Agency-side record of prosecution decisions over matters it brings; the case crosses into the court CMS when sent to the court. Different operator, different objective. |
| Public Defender Case Management | Defense-side record of representation; consumes the court's record through partner access but keeps its own caseload system. |
| Legal Docket Management | Same word, different object: tracks a law firm's filing deadlines and obligations; the court CMS's docket is the official public register of case events. |
| Probation & Parole Management | Supervision of persons after adjudication; the court CMS records the sentence and stops; supervision caseloads are a separate Type (also sold as a separate product by court-suite vendors). |
| Public Sector Case Management | Generic tracked-case container without judicial structures; remove the official docket, hearings/listing, and structured dispositions and a court CMS degrades into it. |
| Corrections Management System | Custody operations: tracks court events but never adjudicates; the court CMS adjudicates and never manages custody. |
| Police Records Management System | Pre-charge records of incidents and arrests; criminal cases begin in the court CMS from charges referred or filed, not from police records. |
| Law Practice Management / Legal Matter Management | Private-practice matters and client work; the court CMS is the register of the court's own judicial work. |
| Government Transparency Portal | Publishes records outward; the court CMS manages the records and exposes them through its own controlled public-access surfaces. |

## Representative Products

- **Journal Technologies eCourt** — court CMS for trial and appellate courts across the US, Canada, and Australia; deep court-specific configuration; the vendor ships filing (eFile-it) and payments (ePay-it) as separate integrated products, and prosecutor/defender/supervision systems as separate products on the same framework.
- **Neumo (FullCourt Enterprise)** — cloud court platform deployed as a statewide shared system (Montana: 192 trial courts on one platform); case, hearing, and collections management with justice-partner access, DMV disposition feeds, and integrated payments; jury and probation sold as separate product lines.
- **CM/ECF + PACER (US federal judiciary)** — government-built Case Management/Electronic Case Files program covering district, bankruptcy, and appellate courts; the case file (docket sheet + all filed documents) as the canonical record, with electronic filing, automatic docketing, participant notification, and fee-based public access through PACER.
- **HMCTS CJS Common Platform (UK)** — government-built criminal-justice case platform whose published domain language — prosecution case, defendant, charge, hearing, listing, structured results, generated notices/orders/warrants, reference-data-driven behavior — makes its case model unusually explicit.

Other major incumbents (notably Tyler Technologies, widely cited as the largest US supplier) were not directly researched in this pass and are mentioned here only as market context, without product claims.

## Sources

Research date: **2026-09-07**

- Journal Technologies — product pages: eCourt (https://www.journaltech.com/ecourt), Public Access Solutions / eFile-it / ePay-it (https://www.journaltech.com/public-access-solutions)
- Neumo — Justice Solutions / Court (https://neumo.com/products/justice-solutions/court/) and Montana Supreme Court case study (https://neumo.com/resources/montana-supreme-court-unifies-courts-on-shared-platform/)
- United States Courts (Administrative Office of the US Courts) — Court Records (https://www.uscourts.gov/court-records) and FAQs: Case Management / Electronic Case Files (https://www.uscourts.gov/court-records/file-a-case-cm-ecf/faqs-case-management-electronic-case-files-cm-ecf)
- HMCTS — The domain language, CJS Common Platform (https://hmcts.github.io/cjs-common-platform/architecture/domain-language.html)
- Cornell LII Wex — docket; court docket (https://www.law.cornell.edu/wex/docket, https://www.law.cornell.edu/wex/court_docket)

> Sourcing limitation: commercial vendors' help centers and operational manuals were not reachable in this pass (Tyler Technologies and other attempted vendor pages returned errors and were abandoned after repeated attempts). Assertions above are calibrated accordingly: structural claims rest on directly observed official descriptions of four systems across two countries; no precise numeric limits, stage lists, or default settings are asserted, and vendor-published performance figures are recorded only in the paired Research Notes.
