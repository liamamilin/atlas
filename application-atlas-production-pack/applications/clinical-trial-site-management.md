# Clinical Trial Site Management

## Overview

**Clinical Trial Site Management** software is operated by the organization that *conducts* clinical trials — the research site — to run its trials operationally and as a business. A research site (a dedicated research clinic, a site network or site management organization, a hospital or health-system research department, an academic medical center or cancer center) simultaneously executes many studies on behalf of many different sponsors and CROs. This software is the site's system of record for that work: the studies it has won and is running, the participants it recruits and sees, the visits and staff work performed against each protocol, the regulatory documents it must keep inspection-ready, and the money — what each study's budget promises, what the site has billed, what has been paid, and what it owes its participants.

The defining core is small:

```text
The research site organization (the operator whose business is being run)
└── Study portfolio (externally sponsored studies, each in the site's own
    lifecycle: feasibility → contract & budget → start-up → conduct → close-out)
    └── Per-study record of conducted operation
        (participants screened/enrolled, visits due and done, staff work performed)
        └── The site's side of the money (budget → billed → paid; stipends out)
```

Everything else the market associates with the category — patient databases and recruitment funnels, protocol-window visit scheduling, two-way participant texting, stipend payment rails, document exchange with monitors, network-level dashboards — is standard equipment in mature products built on top of this core. Remove the site as the subject and the software becomes a trial-operational CTMS view; remove the sponsor-originated study portfolio and it becomes clinic scheduling; remove the money record and only a document-enablement or visit-tracking tool remains.

## Users & Context

The operator is the research site itself, in one of several common forms: an independent dedicated site, a site network or site management organization running many locations, a hospital or health-system research office, or an academic medical center / cancer center conducting dozens to hundreds of active trials. A single deployment typically serves one operator organization at any scale; network deployments centralize many sites under one roof.

Typical roles:

- **Study site coordinator (CRC)** — the daily operator: recruits and screens participants, schedules and conducts visits, follows up on tasks, records what happened.
- **Principal investigator** — accountable for the conducted studies; recipient of notifications and sign-offs in many workflows.
- **Recruitment staff** — work the site's participant database, advertising and pre-screening funnels.
- **Regulatory specialist** — maintains the site's essential documents and inspection readiness per study.
- **Site finance staff** — negotiate and track study budgets, raise invoices against sponsors, reconcile reimbursements, manage participant stipends.
- **Site/network management** — pipeline of study opportunities, staff and site performance, portfolio financials across all studies and locations.

The context is regulated research: records are expected to be attributable and audit-ready, sponsors and monitors inspect site documentation, and institutional deployments add billing-compliance obligations that tie research procedures to the correct payer.

## Core Model

### The Defining Core

**The site as the operating subject.** The system is organized around the site organization and its own resources — locations, staff, participant panel, money — not around one trial. Even a single-site deployment models the operator explicitly: its rooms and locations, its staff roster, its database of people. This is the seat inversion that distinguishes the category: a trial-management system is organized around a study with sites as resources; site-management software is organized around the site with studies as its portfolio.

**The study portfolio as demand.** Studies arrive from outside — pharmaceutical sponsors and CROs — and the site tracks each one through its own lifecycle: opportunity and feasibility, contract and budget negotiation, start-up, conduct, close-out. Many studies from many sponsors run at once, each with its own budget, document obligations, and visit schedule. The portfolio — not a single study — is the managed object.

**Conducted operation recorded per study.** For each study, the system records the actual work: who was pre-screened, who was enrolled, which visits are due and which were completed, which staff did what. Visit scheduling derives from the protocol's visit schedule, with target dates and windows calculated automatically in mature products. This operational record is shared ground with trial-management software — it is the same study × participant × visit skeleton, seen from the site's side of the table.

**The site's side of the money.** Every study carries the site's financial relationship with its sponsor: the negotiated budget (often with visit- or procedure-level amounts and caps such as screen-failure allowances), what has been earned and billed, what the sponsor has paid, and what remains uncollected. The money record is inseparable from the operational record — visits and milestones trigger billing — and flows the other way too: stipends and reimbursements paid out to participants. Across the researched products this financial machinery is as fundamental as the visit record; a site that cannot see unbilled work is not being managed.

### Standard Capabilities of Mature Products

These are common across the researched sample and expected in the market; they make the core practical.

- **Participant panel / patient database** — a site-owned, persistent roster of people, reused across studies: people who inquired, screened out, or completed earlier trials become the starting pool for the next study. Recruitment-oriented products make this database the centerpiece; institutional deployments lean more on per-protocol registration.
- **Recruitment machinery** — website and landing-page integration listing enrolling studies, advertising-channel and recruitment-vendor integrations, pre-screening questionnaires (phone or digital), funnel tracking from inquiry to enrollment, and re-marketing the database to each new study via email/text campaigns.
- **Visit operations** — protocol-derived target dates and window calculations, calendar scheduling (with room/location assignment in some products), reminders and two-way texting to reduce no-shows, overdue-visit surfacing, task and follow-up alerts, electronic visit logs.
- **Regulatory-document coordination** — the site's essential-document obligations per study (the investigator site file), delegated to companion eRegulatory products or modules, with audit trails and inspection readiness; document exchange with sponsors/CROs and remote-monitor access is the standard seam.
- **Participant engagement & payments** — reminders, portals, eConsent, and stipend/incentive payments through card-based rails, with year-end reporting.
- **Financial operations** — budget and contract tracking per study, visit/procedure/milestone-level receivables, invoice and payment-voucher generation, sponsor reimbursement reconciliation, expenses, and financial reporting up to company level.
- **Staff & performance management** — staff productivity and workload visibility; site performance metrics (enrollment speed, start-up turnaround, visit adherence) that sites also use commercially, to demonstrate capability to sponsors and win future studies.
- **Reporting & dashboards** — from a single study's visit list to portfolio-level enrollment, cycle-time, and revenue pictures.
- **Network / enterprise tier** — for multi-site operators: centralized management of all sites, studies, personnel, and finances; aggregate reporting and BI; single sign-on and centralized user administration; distribution of new study opportunities out to sites with structured response capture.
- **Integrations** — EMR/EHR (demographics, billing-compliance routing in institutional settings), eSource/EDC, eRegulatory, IRB/eIRB systems, general ledger, and sponsor/CRO-side systems.

### One Skeleton, Two Seats

The studied products make one thing explicit: site management and trial management share the same underlying skeleton — studies, participants, visits, budgets — but seat the operator differently.

```text
Trial-operational seat (CTMS):   one study → its sites → its milestones → its monitoring
Site-business seat (this Type):  one site organization → its study portfolio → its people and money
```

Many products self-label as CTMS while serving this seat; the market uses "CTMS," "Site CTMS," and "site operations management" for the same population of software. The distinction that holds is the operator object, not the label.

## How It Works

### Win the study (portfolio loop)

```text
A trial opportunity arrives from a sponsor/CRO (lead, feasibility questionnaire)
→ the site assesses feasibility and responds
→ contract and clinical trial budget are negotiated and recorded
→ award received; the study enters the site's portfolio
```

Larger operators track this pipeline explicitly — leads, outreach, turnaround times — and use historical performance metrics (start-up speed, enrollment track record) to win the next opportunity. Network organizations distribute opportunities to their sites inside the platform and capture structured interest responses.

### Start the study

```text
Track start-up milestones (agreement, regulatory submission, site activation)
→ coordinate essential documents and IRB/ethics submissions
→ configure the protocol's visit schedule and budget in the system
→ assign staff; prepare rooms/resources (where resource scheduling exists)
```

### Recruit and enroll

```text
Search the participant database against the study's criteria
→ run outreach (website leads, campaigns, calls/texts from within the system)
→ pre-screen (questionnaire; prescreening visit)
→ enroll eligible participants into the study
```

### Run the visit loop

```text
System computes each participant's next visit with target date and window
→ coordinator schedules the visit (calendar, room), sends reminders
→ visit is conducted and recorded in the visit log
→ tasks and follow-ups alerted; overdue visits surface to management
```

This loop is the daily heartbeat of the site.

### Bill and collect

```text
Completed visits/procedures and milestones accumulate as earned work
→ the system generates invoices/payment vouchers against the study budget
→ sponsor reimbursements are recorded and reconciled
→ unbilled or unpaid work is surfaced as recoverable revenue
→ participant stipends are paid out and reported
```

In institutional settings, the same machinery connects to the EMR so that research procedures are billed to the correct payer — the sponsor rather than routine insurance — under billing-compliance rules.

### Support oversight and close out

```text
Monitors access study documents remotely (via the site's document system)
→ findings and audit requests are answered from the audit-ready record
→ final visits complete; final invoices settled
→ the study closes out and its records are archived
```

## Interfaces

Exact layouts and names vary by product; these surfaces are common.

### Home / portfolio dashboard

The operator's entry point: the study portfolio with status and progress, today's visits, overdue items, pending tasks, and financial summaries. Primary actions: drill into a study, a participant, or a financial view; work pending tasks.

### Participant database & recruitment funnel

The site's roster with search (including feasibility-criteria searches), inquiry and lead capture, pre-screening questionnaires, funnel stages, and communication history. Primary actions: add/import people, match to studies, contact (call/text/email), book a screening.

### Visit schedule / calendar

Day and week views of scheduled participant visits with time, visit label, assigned room, and status; side-by-side with upcoming/overdue lists and task alerts. Primary actions: schedule, reschedule, record completion, message participants.

### Participant & study records

Per-participant history across studies (screenings, enrollments, visits, stipends) and per-study operational record (visit schedule, enrollment log, tasks, documents). Primary actions: record events, upload documents, review history.

### Financial views

Study budgets, earned vs billed vs paid, invoices and payment vouchers, receivables, sponsor reimbursements, participant stipends, and company-level financial reports. Primary actions: generate invoices, record payments, reconcile, report.

### Document / regulatory workspace

The site's essential documents per study with audit trails and version control — frequently delivered as a tightly integrated companion product. Primary actions: file, version, share with monitors, prepare for inspection.

### Administration

Sites/locations, staff, roles and permissions, calendars, budget templates, integration configuration. Restricted to administrative roles; network tiers add centralized user management and cross-site configuration.

## Important Rules / Behaviors

- **Visits have protocol windows.** Scheduling works from protocol-derived target dates and windows computed by the system; visits drifting outside their window — or missed entirely — become visible operational problems, and in mature products they also register as compliance-relevant events.
- **Operational events gate money.** Billing is triggered by the operational record — a completed visit, a procedure performed, a milestone achieved. Work that is done but not billed ("unbilled" work) is a first-class financial risk that the system is expected to surface; recovering it is one of the category's headline values.
- **Budget terms constrain compensation.** Agreed caps and ratios (for example, screen-failure allowances) are tracked against actuals, so the site knows when a study's compensation terms are being breached by reality.
- **Money flows both directions.** The site is a payor as well as a payee: participant stipends and reimbursements are issued and tracked with the same care, including year-end reporting.
- **The record must survive inspection.** Operational and financial records are attributable and audit-ready; regulatory documents follow version-controlled, audit-trailed lifecycles; sponsors and auditors are expected to review them.
- **The participant panel outlives studies.** People remain in the site's database between studies, and contacting them for new studies is a governed, expected behavior — the panel is a business asset.
- **Role separation matters.** Coordinators, recruitment, regulatory, finance, and management see and do different things; in network deployments, central teams oversee while local teams operate.
- **The site coordinates, others capture and archive.** Clinical data capture belongs to eSource/EDC, the master regulatory files to eRegulatory/eTMF systems, randomization and drug supply to IRT/RTSM. Site management holds their operational and financial shadow — what is due, what happened, what it is worth — usually via integration.

## Variants

- **Dedicated research site / independent clinic** — the classic user: recruitment- and finance-heavy, small staff wearing many hats.
- **Site network / SMO** — many locations under central management: pipeline and opportunity distribution, standardized processes, enterprise reporting, central billing.
- **Hospital / health-system research office** — EMR-centric; billing compliance and payer-correct routing of research procedures become first-class machinery.
- **Academic medical center / cancer center** — large portfolios (dozens to hundreds of active protocols), institutional governance, protocol-lifecycle and accrual analytics, deep EMR and ledger integration, sometimes biospecimen modules.
- **Phase I units** — dense subject and resource scheduling within a single unit.
- **Decentralized-trial-enabled sites** — remote consenting, remote visits, and shipped-treatment coordination layered onto the same core.

A variant stays a variant unless it changes the defining core; all of the above keep the site as subject, the portfolio as demand, and the operation-plus-money record at the center.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Clinical Trial Management System / CTMS | sibling; same skeleton, other seat | CTMS is organized around one study with sites as its resources (milestones, monitoring, plan-vs-actual); site management is organized around the site organization with studies as its portfolio (people, rooms, receivables). The market mostly ships one product per vendor covering both readings, labeled CTMS either way. |
| Clinical Trial Recruitment Platform | adjacent, partial overlap | recruitment platform's subject is the study-as-demand-object with a candidate funnel ending in referral to enrollment; here recruitment is one capability of the site's operation and the pipeline object is the study portfolio, not the candidate funnel. |
| Electronic Data Capture / eSource | adjacent, integrated | captures the clinical/source data of visits; site management runs the operation and the business around those visits. |
| eRegulatory / eISF, eTMF | adjacent, integrated | document systems for essential-document files; site management coordinates them and holds the operation and money, typically by integration or bundled module. |
| IRT / RTSM | adjacent, integrated | randomization and trial-supply logistics; not the site's business system. |
| Patient Scheduling / Practice Management | different domain | care-delivery scheduling lacks protocol windows, visit-schedule procedures, stipends, and sponsor-side billing; the EMR appears here as an integration partner. |
| Research Administration / Grant Management | adjacent (institutional) | pre-award and funding administration; site management starts where a sponsored study is being conducted. |

The sharpest seam is with CTMS: the two labels cover overlapping products, and the working distinction is the operator object — the trial or the site. Readers should treat the two documents as two seats at the same table.

## Representative Products

- RealTime-CTMS / SOMS (RealTime eClinical Solutions) — dedicated sites, site networks, SMOs, AMCs and health systems; suite-bundled site-operations platform
- Site CTMS (CRIO) — site-centric platform bundling eSource, eConsent, eRegulatory and site operations
- Clinical Conductor (Advarra) — research sites, site networks, hospitals and health systems
- OnCore (Advarra) — academic medical centers and cancer centers

The model was checked against a site-enablement platform (Florence eBinders/feasibility — document workflows, sponsor exchange, feasibility response without visit operations or site finances), which sits outside this Type and marks its boundary, and against the paper-era pattern of site operations (binders, paper visit logs, invoice-by-hand), which satisfies the minimal definition without any modern accretion.

## Sources

Research date: **2026-09-07**

- RealTime eClinical Solutions — company homepage, CTMS solution page, Devana product page: https://realtime-eclinical.com/ , https://realtime-eclinical.com/solutions/ctms/ , https://realtime-eclinical.com/solutions/devana/
- CRIO — company homepage and Site CTMS product page (including annotated scheduling screenshot): https://clinicalresearch.io/ , https://clinicalresearch.io/products/site-ctms/
- Advarra — Clinical Conductor CTMS page and OnCore CTMS page: https://www.advarra.com/solutions/sites/ctms/clinical-conductor/ , https://www.advarra.com/solutions/sites/ctms/oncore/
- Florence Healthcare — company homepage and Florence for Sites page (boundary sample): https://www.florencehc.com/ , https://www.florencehc.com/florence-for-sites/

> Sourcing limitation: deep user manuals for all management products are customer-gated; evidence is official product pages, vendor FAQs, and annotated screenshots, so precise operational parameters (exact window rules, invoice defaults, permission details) are intentionally not asserted. Vendor-published scale and ROI claims were excluded. The sponsor/CRO-side reading of "site management" (modules inside enterprise trial-management suites) was not directly fetchable and is handled through the paired CTMS document.

Detailed evidence, cross-product comparison, abstraction levels, and boundary analyses are recorded in the paired Research Notes.
