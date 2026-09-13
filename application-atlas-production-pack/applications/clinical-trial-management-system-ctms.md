# Clinical Trial Management System / CTMS

## Overview

A **Clinical Trial Management System (CTMS)** is the operational system of record for organizing, running, and tracking the execution of clinical trials. Where an EDC captures the clinical data of trial participants and an eTMF archives the regulatory documents, the CTMS manages the conduct of the trial itself: which studies exist, which sites and people are executing them, which participants have been enrolled, which protocol visits and milestones are due or overdue, what monitoring has occurred, what deviations have been logged, and what the trial has earned and owed.

Its defining core is small:

```text
Clinical Study (the protocol-defined trial)
└── Sites & study personnel (the operational network executing it)
    └── Protocol-anchored operational events
        (milestones, visit schedules, activation steps — planned vs actual)
        └── Recorded operational history of conduct
            (enrollments, visits, monitoring, deviations — auditable)
```

Everything else commonly associated with the category — participant visit tracking, budgets and milestone payments, monitoring reports, deviation logs, dashboards, integrations with EDC/eTMF/RTSM/EMR systems — is standard equipment in mature products but is built on top of this core. Remove the protocol-anchored operational tracking and the product becomes a generic project manager; remove the study-site structure and it becomes a CRM; keep only the data capture and it is an EDC; keep only the documents and it is an eTMF.

## Users & Context

A CTMS is used by organizations that operate or oversee clinical trials. The market has two stable poles that share one structure:

- **Sponsors and CROs** — pharmaceutical/biotech companies and contract research organizations running multi-site trials across countries. Their CTMS tracks study-level progress, site activation, monitoring visits, milestone deliverables, and payments owed or earned per site.
- **Research sites and institutions** — dedicated research sites, site networks, hospitals, health systems, and academic medical centers/cancer centers conducting trials on behalf of sponsors. Their CTMS manages the study portfolio, participant visits, staff workloads, regulatory-document coordination, and the business side: budgets, billing, and revenue capture.

Typical roles inside the system:

- **Study manager / clinical operations lead / project manager** — owns the study plan, timelines, and overall progress.
- **Clinical Research Associate (CRA) / monitor** — visits sites (on-site or remotely), reviews conduct, writes monitoring reports, raises action items.
- **Study coordinator (CRC)** — runs the day-to-day at a site: participant screening and enrollment, visit scheduling, task follow-ups.
- **Principal investigator** — accountable investigator; recipient of notifications and approvals in many workflows.
- **Finance / grants management staff** — budgets, milestone invoicing, expenses, receivables.
- **Regulatory / compliance staff** — deviations, IRB/ethics notifications, audit readiness.
- **Executives / department heads** — portfolio dashboards: enrollment, accrual, cycle times, financials across all studies.

The work context is regulated research: records are expected to be attributable and audit-ready, and the system typically runs under quality/compliance regimes (e.g., 21 CFR Part 11 posture in US-facing products).

## Core Model

### The Defining Core

**The study.** The central object is the clinical study (also called a trial or protocol): an identified effort with a protocol ID, planned phases, and a defined timeline — from trial initiation through site activation, enrollment, and conduct, to database lock and close-out. Everything in the system hangs off a study record.

**The site & personnel network.** Trials are executed at sites — hospitals, clinics, dedicated research centers — each activated into a study with its own team (investigator, coordinators, monitors). The system models sites as managed records with activation status and assigns personnel to studies and sites. Even a single-site deployment models the site explicitly.

**Protocol-anchored operational events.** The protocol translates into an operational plan inside the system: study milestones (site activation, first participant enrolled, interim checkpoints, database lock), participant visit schedules with target dates and window calculations, and monitoring activities. The essential behavior is **planned-versus-actual tracking**: the system always shows what was supposed to happen by now against what has happened, and flags deviations from the plan.

**Recorded operational history.** Conduct events — enrollments, completed visits, monitoring visits and their reports, protocol deviations, correspondence — are recorded as attributable, time-stamped operational records. This history is the shared memory that managers, monitors, auditors, and finance staff all work from, and it is what makes the CTMS a system of record rather than a planning tool.

### Standard Capabilities of Mature Products

These capabilities are common across the researched sample and expected in the market; they are what make the core practical.

- **Participant tracking** — screening logs, enrollment status per site, scheduled and completed visits, overdue-visit views, enrollment-versus-target progress. Depth varies: site-centric systems track each participant's visit journey; some sponsor-side systems track enrollment more at aggregate level.
- **Budget & payment machinery** — study/site budgets, milestone-based invoicing (a milestone being marked achieved triggers the billing workflow), expense submission and approval (including vendor expenses), receivables and payables tracking, participant stipend handling in site-centric products.
- **Monitoring machinery** — CRA visit scheduling (pre-site-selection, site-initiation, interim monitoring, close-out), monitoring reports and standard correspondence, findings and action items with owners, priorities, and due dates that carry forward until closed.
- **Protocol deviation logging** — a centralized log of recorded deviations, each classified by level (site, subject, or visit) and severity, with corrective/preventive actions and records of IRB/ethics notification.
- **Operational documents & correspondence** — visit reports, activation and follow-up letters, and study correspondence generated and tracked in the system (distinct from the eTMF regulatory archive).
- **Dashboards & analytics** — enrollment metrics, screen-failure rates, milestone status, staff productivity, accrual, financial reconciliation; drill-down from portfolio to study to site.
- **Governance** — role-based access, multi-level approval workflows (reports, expenses, milestones, deviations), automated notifications and reminders, and audit trails across operational and financial records.
- **Integrations** — EDC (enrollment/visit data), eTMF/eRegulatory (document status), IRT/RTSM (supply rollups), EMR/EHR (demographics, billing-compliance data in institutional settings), IRB systems, and general-ledger/ERP systems.

### One Structure, Two Poles

The same skeleton is implemented from two directions:

```text
Sponsor/CRO-centric:   study → sites → milestones → monitoring → invoicing
Site/institution:      portfolio → studies → participants → visits → billing
```

A sponsor-centric CTMS is strongest on milestones, monitoring, and payments owed to sites; a site-centric CTMS is strongest on participant visit operations, recruitment, and the site's own revenue. Both remain recognizably the same Type.

## How It Works

### Set up the study

```text
Create the study (protocol identity, plan)
→ decompose the protocol into milestones and a visit schedule
→ add candidate sites → select and activate sites
→ assign personnel (investigator, coordinator, monitor, project manager)
→ configure budgets and payment terms per site
```

The operational calendar (working days, holidays) and approval hierarchies are configured so that target dates and routing behave correctly for the organization.

### Activate and enroll

```text
Site completes activation steps (tracked against the plan)
→ participants are screened (screening log; screen failures counted)
→ eligible participants are enrolled (status recorded per site)
→ enrollment progress is compared against targets continuously
```

### Run the visit loop

```text
System computes each participant's next visit and its target date/window
→ coordinators schedule and complete visits (visit log updated)
→ reminders reduce missed visits; overdue visits are surfaced
→ monitoring views show upcoming/overdue visits and pending actions
```

This loop is the daily heartbeat of a site-centric CTMS.

### Monitor the trial (sponsor/CRO loop)

```text
Schedule a monitoring visit to a site (on-site or remote)
→ conduct the visit → the system prompts required outputs
(monitoring report, confirmation/follow-up correspondence)
→ reports route through approval levels
→ findings become action items with owners and due dates
→ open action items carry forward until explicitly closed
```

### Record and handle deviations

```text
A protocol deviation occurs → recorded in the deviation log
→ classified (level, severity, category)
→ corrective and preventive actions documented
→ ethics/IRB notification recorded
→ reviewers/roles notified; deviation visible in dashboards
```

### Settle the money

```text
Milestone marked achieved → billing workflow triggered
→ invoice raised against the study/site budget
→ expenses submitted (site staff, vendors) and approved through hierarchy
→ receivables/payables tracked; reconciliation reported
```

In institutional deployments the same machinery extends into billing-compliance workflows tied to the EMR, ensuring research procedures are billed correctly.

### Close out

```text
Final visits and monitoring complete → database lock milestone
→ site close-out visits → outstanding payments settled
→ study archived as a completed operational record
```

## Interfaces

Exact layouts and names vary by product; the following surfaces are common.

### Study dashboard

The entry surface per user. Typical panels: study information (name, protocol ID, sites), enrollment progress, upcoming and overdue visits, protocol deviation counts, milestone status, financial summaries. Primary actions: drill into a study, site, or participant; work pending tasks.

### Study workspace (milestone tracker)

The study's plan-versus-actual view: milestone list with planned and actual dates, activation steps per site, timeline from initiation to database lock. Primary actions: update milestone status, flag plan deviations, review progress.

### Site list / site record

The managed network: each site with status (candidate, in activation, active, closed), personnel, and performance. Primary actions: add/select sites, advance activation, view site-level enrollment and visits.

### Participant / visit tracker

The operational log of participants and their visits: screening status, enrollment, visit history, next visit with target date/window, overdue indicators. Primary actions: record visits, schedule, log reasons for missed visits, message/remind participants (in site-centric products).

### Monitoring workspace

The monitor's surface: visit calendar, visit types, assigned CRAs, report and letter generation after each visit, approval routing status, open action items. Primary actions: create visit records, produce reports/correspondence, add action items, approve.

### Deviation log

A filterable register of recorded deviations with classification, actions, and notification status. Primary actions: record a deviation, classify, attach actions, record notifications, review.

### Financial views

Budgets per study/site, milestone-based invoices, expense claims in approval, receivables/payables, participant payments, reconciliation reports. Primary actions: raise invoices, approve expenses, run financial reports.

### Administration & configuration

Master data (studies, sites, personnel, financial entities), approval hierarchies, notification rules, calendars. Restricted to administrative roles.

## Important Rules / Behaviors

- **Plan versus actual is always exposed.** The system continuously compares planned milestones and visit dates against actual progress; falling behind is a first-class visible state, not a report someone runs occasionally.
- **Milestones gate money.** Invoicing is tied to milestone achievement — the financial workflow is triggered by the operational record, which keeps payments anchored to documented progress.
- **Visits have windows; deviations are recorded.** Visit scheduling works from protocol-derived target dates and windows; a visit outside its window, or any protocol non-adherence, becomes a recorded, attributable deviation with defined follow-up (corrective actions, ethics notification).
- **Work is routed through governed approvals.** Reports, letters, expenses, and milestone confirmations pass configured multi-level approval chains; approval is a distinct, recorded act with comments and revert loops.
- **Action items persist until closed.** Monitoring findings become tracked items with owners and due dates that carry forward into subsequent visits/reports — they do not silently disappear.
- **Records are audit-facing.** Operational and financial history is time-stamped and attributable; dashboards and logs are expected to withstand sponsor and regulatory audits. Correspondence generation after visits is commonly enforced within required timelines.
- **Role separation matters.** Coordinators, monitors, managers, finance, and administrators see and can do different things; notifications fan out to the roles accountable at each step (coordinator, monitor, project manager, investigator).
- **The CTMS tracks, but does not capture or archive.** Clinical data lives in the EDC; the regulatory document file lives in the eTMF; randomization and drug-supply logistics live in IRT/RTSM. The CTMS holds their operational shadow — status, counts, and due/done — not their contents.

## Variants

- **Sponsor/CRO-centric CTMS** — study- and milestone-centric, monitoring-heavy, invoice generation toward sites, integration-first with EDC/RTSM/eTMF.
- **Site / institution-centric CTMS** — participant-visit-centric, recruitment and retention features, site financials (budgets, billing, stipends), regulatory-document coordination, billing-compliance machinery in hospital settings.
- **Enterprise / network deployments** — centralized management of many sites, studies, and finances with aggregate reporting, roll-up dashboards, and organization-wide identity/security controls; common for site networks, health systems, and universities.
- **Academic medical center / cancer center flavor** — deep EMR integration, billing-compliance workflows, institutional portfolio reporting; optional modules such as biospecimen management.
- **Phase I unit flavor** — dense visit/subject scheduling within a single unit.
- **Adjacent capabilities sold as separate products in the same suites** — eSource/EDC, eRegulatory/eTMF, participant portals and payments, site-selection/pipeline analytics. Their presence varies; their absence does not make a product less of a CTMS.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Electronic Data Capture / EDC | adjacent, integrated | captures clinical/subject data per protocol (CRFs); CTMS manages operational conduct — who, where, when, how much |
| Electronic Trial Master File / eTMF | adjacent, integrated | regulatory document archive and filing structure; CTMS tracks operational correspondence but not the master regulatory file |
| IRT / RTSM | adjacent, integrated | randomization and trial-supply logistics; CTMS may show supply rollups but does not randomize or manage kits |
| Clinical Trial Recruitment Platform | adjacent, partial overlap in site products | managed object is the candidate funnel and pre-screening; CTMS's object is the full study×site×participant operation |
| Clinical Trial Site Management | sibling leaf, boundary to review | site-business operations framing; in practice many "site CTMS" products (self-labeled CTMS) sit between the two labels |
| Clinical Data Management | different function | cleaning, validation, and query resolution of captured data after the fact |
| Project & Work Management | structural look-alike | generic tasks/projects; lacks protocol-anchored events, site/subject structure, deviation/monitoring semantics, and regulated audit/approval behavior |
| Practice Management / EHR | different domain | care delivery records; appears in CTMS land only as an integration partner (demographics, billing) |

The sharpest seams are with EDC and eTMF: all three are clinical-trial systems that coexist in the same suites, are sold as separate products by the same vendors, and are integrated but not merged.

## Representative Products

- RealTime-CTMS (RealTime eClinical Solutions) — site/network pole, suite-bundled
- OnCore (Advarra) — academic medical center / cancer center pole
- Clinical Conductor (Advarra) — research sites, networks, hospitals, health systems
- Clinion CTMS (Clinion) — sponsor/CRO pole, suite-integrated with EDC/RTSM/eTMF

The core model was checked across all four poles (sponsor/CRO, institutional, site network, single-site) and against the historical pattern of desktop-era study trackers, which satisfy the minimal definition without any modern accretion.

## Sources

Research date: **2026-09-07**

- RealTime eClinical Solutions — company homepage and CTMS solution page: https://realtime-eclinical.com/ , https://realtime-eclinical.com/solutions/ctms/
- Advarra — company homepage, OnCore CTMS page, Clinical Conductor CTMS page: https://www.advarra.com/ , https://www.advarra.com/solutions/sites/ctms/oncore/ , https://www.advarra.com/solutions/sites/ctms/clinical-conductor/
- Clinion — company homepage and CTMS product page (including product screenshots of dashboard, milestones, deviations, reports & letters, invoices, workflow configuration): https://www.clinion.com/ , https://www.clinion.com/clinical-trial-management-system/

> Sourcing limitation: the largest enterprise eClinical suites' CTMS documentation (Veeva Vault CTMS, Medidata, Oracle Clinical One) and Castor's help center could not be fetched in the research environment (transport errors / 404s after retries); the sponsor/CRO pole rests on Clinion plus cross-product comparison. Fetched evidence is predominantly official product pages and screenshots rather than deep user manuals; precise operational defaults (exact window rules, payment-trigger conditions, state-machine details) are therefore intentionally not asserted. Vendor-published metrics and claims were kept out of this document.

Detailed product-by-product observations, cross-product comparison matrix, evidence layers, vendor-specific findings, and boundary analyses are recorded in the paired Research Notes.
