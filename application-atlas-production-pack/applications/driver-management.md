# Driver Management

## Overview

A **Driver Management** application is the operator-side system of record for the *people who drive* for an organization. It maintains, for each driver, a persistent record of driving credentials and evidence; derives from that record a governed state — whether this person is currently entitled and fit to drive for the organization; and keeps that state current through an ongoing loop of record checks, expiry monitoring, alerts, and remediation.

The defining core is small:

```text
Driver of record
└── Credentials & evidence (licence, qualifications, medical, documents, check history)
    └── Driving entitlement state (entitled / action required / not entitled)
        └── Maintenance loop (checks → alerts → remediation → restored entitlement)
```

Everything else commonly associated with the category — risk scoring, training administration, driver self-service apps, hiring intake, continuous monitoring, telematics-derived behavior data — is widespread in current products but is not what makes the product a Driver Management application. Paper driver-qualification files maintained by a clerk, and telephone-era licence checking, satisfy the same core without any of those capabilities.

The Type manages the *person*. It is distinct from Fleet Management Systems (which manage vehicles as assets), from dispatch and trucking systems (which manage freight and assign drivers to work), and from hours-of-service platforms (which manage duty time). The boundary questions are treated under Related Application Types.

## Users & Context

Primary users:

- **Safety / compliance manager** — owns the driver records; watches credential expiries and check results; responds to alerts; assembles and maintains qualification files; produces audit evidence. This is the persona the whole loop is built around.
- **Fleet or risk manager** — at smaller organizations often the same person as above; oversees the overall entitlement and risk picture of the driving workforce, and decides interventions (retraining, restriction, removal from driving duty).

Secondary users:

- **Hiring / onboarding staff** — create the record from an applicant: identity, licence, endorsements, medical certification, background and driving-record checks, signed consents.
- **Drivers themselves** — participate through self-service surfaces: uploading documents, granting consent for record checks, completing assigned training, reporting collisions, inspecting vehicles, viewing their own status or score.

Typical contexts: trucking carriers and delivery/distribution operators; corporate fleets whose employees drive for sales, service, or field work (including employees driving their own vehicles); and any employer with a legal duty of care over people who drive on its behalf — a responsibility that applies even when only one person drives for the organization. Organization sizes range from owner-operators with a handful of drivers to global workforces across many countries.

## Core Model

### The Defining Core

**1. Driver of record.** A persistent, individually identified person who drives for the organization. The record carries identity and employment context plus a set of *driving-specific* credentials and evidence: licence class, status and expiry; restrictions and endorsements where the regime has them; medical or occupational fitness certification; participation in required programs; driving-related documents; and the history of checks run against the person. Two structural properties matter:

- The record is attached to the **person**, not to a vehicle or a job. The same record stands whether the person drives a company truck, a delivery van, or their own car (in which case documents about that vehicle — insurance, roadworthiness — join the person's record as evidence, without the application becoming a vehicle-asset system).
- The credential set is *driving-specific*. This is what separates the Type from generic employee records: no HR system natively models licence classes, driving-record checks, or medical certification to drive.

**2. Time-bound driving entitlement as a governed state.** The record aggregates its evidence into a state that answers the operational question: *may this person drive for us right now?* The state is derived, not declared — it follows from the validity of credentials and the results of checks. Mature products express it as a status (current / action required / expired or not entitled) and often add a risk rating on top. The essential property is that **entitlement expires**: licences lapse, medical certificates run out, new violations appear. An entitlement state that never decays would not need this application.

**3. The maintenance loop.** The "management" in the Type's name is this loop, which keeps entitlement current:

```text
check / re-validate  →  detect expiry or change  →  alert the organization
        →  remediate (renew, re-train, restrict, re-check)  →  entitlement restored
```

The loop runs against two clocks: the **calendar** (scheduled re-validations and expiring documents) and **events** (new violations, suspensions, or status changes surfaced by record checks between scheduled dates). Automation depth varies across products — from calendar reminders to continuously monitored records — but the loop itself is definitional. Remove it and the product is a static snapshot of documents, not management.

### Standard Capabilities of Mature Products

These are common across mature products and expected by the market, but they make the core practical rather than defining it:

- **Credential calendar and expiry alerts** — per-driver visibility of what is valid, what is expiring, and what has lapsed.
- **External record checks** — pulls of official driving records (motor vehicle records, national licence-check services). Products differ on rhythm: periodic re-checks, event-triggered follow-up checks, or continuously monitored records. The conceptual capability is the same.
- **Per-driver risk rating or score** — derived from record data (violations, licence status) and, in some products, from observed driving behavior fed by telematics or a driver app; used to focus attention on the riskiest drivers.
- **Training and coaching administration** — assigned courses and completion records with reminders; interventions targeted at drivers whose state or score requires action.
- **Driver self-service surface** — the driver as an active participant: document upload, consent, training, collision reporting, vehicle condition checks, view of own status.
- **Onboarding intake** — the path from applicant to qualified driver: capture licence data at application, run pre-employment checks, assemble the initial record.
- **Organizational scoping and roles** — driver populations grouped by site, division, or program; manager-facing consoles separated from driver-facing surfaces.
- **Audit and evidence reporting** — demonstrable completeness of records and documented audit trails; in regulated regimes this is a primary purchase reason, not a nice-to-have.

### One Structure, Many Implementations

```text
Concept:            External record check
Implementations:    periodic MVR pulls; continuous licence monitoring; national licence-check services

Concept:            Governed entitlement state
Implementations:    audit-ready qualification file; low/medium/high risk rating; permit-to-drive artifact

Concept:            Remediation
Implementations:    renewal tasks and deadlines; assigned training or coaching; restriction of driving duty
```

A reader who has only seen one implementation — for example a US qualification-file product — should still be able to recognize a licence-checking service or a corporate driver-risk program as the same Type from this table.

## How It Works

The Type is not a transaction flow but a standing loop. The typical working rhythm:

### 1. Establish the record

```text
Driver or applicant enters the population
→ capture identity, employment context, licence data (often from the licence itself)
→ run baseline checks (driving record, background where applicable) under the driver's consent
→ collect qualification documents (medical certification, endorsements, program enrollment)
→ assemble the initial record and determine the first entitlement state
```

### 2. Determine entitlement

The record's evidence is evaluated against the organization's requirements and the applicable regime. The result is the governed state — entitled, action required, or not entitled — usually with enough granularity (which credential, which gap) to act on.

### 3. Monitor

```text
calendar clock:  scheduled re-checks and expiring credentials surface as forward-looking alerts
event clock:     new violations, suspensions, or status changes arrive from record checks
```

Products differ on how continuously the event clock runs; every product runs the calendar clock.

### 4. Remediate

An alert carries the required action: renew a licence, complete a medical, finish assigned training, restrict the person from driving duty until resolved. Completion is tracked; where appropriate a follow-up check confirms the fix. The state returns to entitled — or the person leaves the driving population.

### 5. Evidence

Managers report on file completeness, check history, training records, and audit trails — demonstrating, to an auditor, an insurer, or a client, that the organization governs the entitlement of its drivers.

### Core vs Common vs Optional

**Defining core** — without these, not Driver Management:

- driver of record with driving-specific credentials and evidence
- time-bound, evidence-derived entitlement state
- the maintenance loop (checks, alerts, remediation)

**Common mature structure** — present in most modern products:

- expiry calendar and alerting
- external record checks (periodic or continuous)
- risk rating / scoring
- training and coaching administration
- driver self-service
- onboarding intake
- organizational scoping with manager/driver roles
- audit and evidence reporting

**Variant / optional** — depends on regime, segment, and product philosophy:

- continuous (event-stream) monitoring as opposed to periodic checks
- behavioral scoring fed by telematics or driver apps
- drug & alcohol program administration
- grey-fleet support (documents for driver-owned vehicles)
- hiring and recruiting depth
- gamification and rewards

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Driver roster

The manager's entry surface.

- all drivers with their current state — entitled, action required, expired/not entitled — often with risk indicators
- primary actions: open a driver, filter by status or group, work the alert queue

### Driver detail / qualification file

The record of one person.

- credentials with validity dates, check history, documents, training records, notes
- primary actions: upload or request documents, run a check, assign training, record a decision, view history

### Monitoring and alerts console

The loop's control surface.

- upcoming expiries, overdue items, and new events requiring action
- primary actions: acknowledge, assign the remediation task, escalate, re-check

### Training administration

- course catalog and assignments, completion status per driver, deadline reminders

### Reporting / evidence

- completeness summaries, compliance posture, audit trails exportable for auditors, insurers, or clients

### Driver portal / app

The driver-facing surface.

- outstanding tasks (documents, consents, training), own status or score, collision reporting, vehicle checks where applicable

### Intake / onboarding

- applicant capture (licence data at application), consent collection, baseline checks, file assembly

## Important Rules / Behaviors

- **Entitlement expires by design.** Lapses are expected events with a pre-built handling path, not system errors. The application's value is measured in lapses caught before they became violations or crashes.
- **The state is derived from evidence.** Managers do not declare a driver "compliant"; the state follows from credentials and check results. A state without current evidence decays.
- **Record checks are consent-governed.** Pulling an individual's driving record is regulated in most regimes; sampled products build consent capture and mandated notices into the workflow. The specifics are regime-dependent.
- **Alerts carry actions.** An alert is not informational — it names the required remediation and is tracked to closure. Unresolved alerts accumulate as risk.
- **The record outlives active employment in regulated regimes.** Qualification files and audit trails are retained as historical artifacts; retention specifics vary by regime and are not universal.
- **Entitlement is job-independent.** The governed state exists regardless of whether work is assigned today; dispatch and scheduling systems are expected to *assume* it, not manage it.

## Variants

- **Regulatory-compliance pole (US-style)** — qualification files as the spine; drug & alcohol program administration and registry queries as first-class structures; audit readiness as the purchase driver. Heavy in trucking and regulated carriage.
- **Corporate driver-risk pole** — continuous monitoring plus behavioral scoring and coaching for large employee-driver populations, often across many countries; duty-of-care and liability framing.
- **Duty-of-care compliance pole (UK/EU-style)** — automated licence checks, driver-owned-vehicle ("grey fleet") document checks, an explicit permit-to-drive artifact, and mandated driver training with records.
- **Hiring-led vs monitoring-led packaging** — some products lead with applicant-to-qualified-driver intake; others lead with standing monitoring of the existing population.
- **Cross-industry spread** — trucking, delivery and distribution, waste and utilities, construction, corporate sales/service fleets; the core loop is identical, the credential vocabulary changes.

A naming caution: the phrase "driver management" is also used loosely for the driver module inside fleet or dispatch products (rosters, assignments, scores). That usage is a capability of those Types, not this Application Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Fleet Management System | closest sibling, complementary | vehicle-asset system of record: maintenance, fuel, telematics; driver data attaches to vehicles. Strip the drivers from an FMS and it still manages vehicles; strip the vehicles from Driver Management and the person's record and loop remain fully functional |
| Trucking Management System | adjacent | freight/order system of record; drivers appear as assigned resources, with schedules and pay/settlement; entitlement is assumed rather than governed |
| Dispatch Management | adjacent | assigns live work to mobile resources; the driver's qualification state is a prerequisite input, not the managed object |
| Electronic Logging Device / HOS Platform | adjacent | governs duty time through logged records-of-duty-status; the driver is the subject of the log, not a qualification record |
| Airline Crew Management | aviation sibling | crew records and qualifications, but the core loop is pairing/rostering and duty legality rather than standing entitlement maintenance |
| Applicant Tracking / HR systems / LMS | crossing | generic person lifecycles without driving-credential semantics (licence classes, driving-record checks, medical-to-drive) and without a governed entitlement state; overlap exists at the hiring and training edges |
| Last-mile / On-demand Delivery Platforms | adjacent via the driver app | those apps execute assigned delivery work; here the driver-facing surface serves the driver's own record and entitlement |

The most important boundary is with the Fleet Management System: the two share a roster-and-vehicles substrate, and the same vendor may sell both. The structural discriminator is which entity is the system of record — the vehicle (asset lifecycle) or the person (entitlement lifecycle).

## Representative Products

- Foley — driver qualification files, screening, and credential monitoring for transportation and adjacent industries (US compliance pole)
- eDriving (a Solera company) — digital driver risk management with continuous licence monitoring and behavioral scoring for global corporate fleets
- TTC Group (Continuum; Licence Bureau is now part of TTC) — licence checks, grey-fleet compliance, permit to drive, and driver training on one platform (UK duty-of-care pole)

The defining core was checked against pre-digital realizations (paper driver qualification files maintained by clerks; telephone-era licence checking) and across the three regime poles above to avoid over-fitting to any one market's vocabulary.

## Sources

Research date: **2026-09-07**

- Foley — https://www.foleyservices.com/ , https://www.foley.io/compliance/driver-files/
- eDriving — https://www.edriving.com/ , https://www.edriving.com/driver-risk-monitoring/
- TTC Group — https://www.thettcgroup.com/fleet-driver-management/ (reached via https://www.licencebureau.co.uk/)

> Sourcing limitation: several additional vendors in the driver-recruiting and fleet-platform space (DriverReach, Tenstreet, J. J. Keller Encompass, Motive, Samsara driver-app pages) were unreachable from the research environment on 2026-09-07 (access-denied or not-found responses). The recruiting-led packaging variant is therefore described only in general terms. Precise regulatory mechanics — exact required-document lists, retention periods, check frequencies, and consent-notice timings — were not researched and are intentionally not stated. Detailed product-by-product evidence, the cross-product comparison matrix, and the boundary analysis against neighboring Types are recorded in the paired Research Notes.
