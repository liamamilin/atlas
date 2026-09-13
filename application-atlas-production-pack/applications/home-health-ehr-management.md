# Home Health EHR / Management

## Overview

A **Home Health EHR / Management** application is an agency-side system of record for delivering **skilled healthcare in patients' homes**. A home health agency — an organization whose clinicians (nurses, physical/occupational/speech therapists, home health aides) treat patients where they live — uses it to hold the patient's clinical record, organize care as physician-authorized episodes, document each visit at the point of care in the field, and convert that documented care into payer claims and quality/compliance reporting.

The defining core is small:

```text
Home-based patient of record
└── Episode of skilled care under an authorizing plan of care
    └── Scheduled visit, documented in the field
        └── Clinical record entry (assessment + care delivered)
    └── Revenue & compliance loop
        └── Claims to payers + quality/compliance reporting
```

Everything else commonly associated with these products — offline mobile charting, smart scheduling, assessment-instrument scrubbing, analytics dashboards, AI documentation assistants — is standard capability layered on that core, not what makes the product a home health system.

The boundary that matters most: this Type records **skilled clinical care** (nursing and therapy under a plan of care). When the delivered service is non-skilled personal/support care and the visit record is a service/attendance record rather than a clinical chart, the product belongs to **Home Care Agency Management** instead. When care happens in a facility rather than the patient's home, it belongs to facility-based Types (skilled nursing, long-term care).

## Users & Context

Primary users:

- **Field clinicians** (registered nurses, licensed practical nurses, physical/occupational/speech therapists, home health aides) — carry the day's visit schedule into patients' homes, perform and document care at the point of care, typically on a mobile device that keeps working without connectivity.
- **Intake coordinators** — convert inbound referrals into admissions: verify payer coverage, open the admission record, assemble the start-of-care paperwork.
- **Schedulers / dispatchers** — build and maintain the visit calendar, matching each visit to a clinician of the right discipline and territory.
- **Clinical supervisors / case managers** — own a panel of patients, review field documentation for completeness and clinical quality before it closes, manage the plan of care and physician communications.
- **Billing / revenue-cycle staff** — turn completed, documented care into claims, track what has been billed and what is stuck, post payments and follow up.

Secondary users:

- **Agency administrators** — configure the agency, staff, payers, and compliance settings; manage multi-branch structures.
- **Executives / directors of nursing** — work from dashboards: census, admissions and discharges, unbilled amounts, quality measures, staff productivity.

The work environment is two-sided. Office staff work in a web application from the agency. Field staff work in patients' homes, where connectivity is unreliable — so the field surface is a mobile application designed to capture documentation offline and synchronize it later. Agencies commonly operate several branches, and the system reflects that structure.

## Core Model

### The Defining Core

**The home-based patient of record.** The system's center is a persistent clinical record for one person receiving care at home. Unlike an office EHR, where the patient travels to the care site, here the agency's clinicians travel to the patient. The record holds demographics, coverage/payer information, clinical history, medications, and everything the agency documents over the course of care.

**The episode of skilled care.** Care is not an open-ended stream of encounters; it is organized as a bounded **episode**: the patient is admitted, a **plan of care** authorizes which skilled services are delivered and how often, care proceeds through scheduled visits, and the episode ends at discharge — or continues through a re-authorization (commonly called recertification) when continued care is justified. The episode is the unit that governs both clinical accountability and billing periods. In US Medicare practice this structure is mandatory and heavily regulated; the abstract structure — a bounded, authorized course of skilled care — is what the Type requires.

**The visit.** The unit of service delivery is the scheduled home visit: a dated, time-bounded appointment at a specific patient's home, assigned to a specific clinician of a specific discipline. Visits are generated from the plan of care's service pattern and constrained by clinician availability, geography, and continuity preferences (agencies try to send the same nurses to the same patients).

**Field-captured clinical documentation.** Each visit produces a clinical record entry captured in the home: assessment findings, vital signs, interventions performed, the patient's response, and — at episode boundaries — comprehensive assessments. In US practice these include standardized assessment instruments — the OASIS instrument is the best-known — which feed both payment and publicly reported quality measures. Documentation is captured at the point of care, commonly offline, and passes a supervisory review before the visit record is complete.

**The revenue and compliance loop.** Documented care converts into money and accountability:

- **Claims/billing** — the agency bills payers for delivered skilled care, organized around episodes and visits. Payer connectivity (clearinghouses, direct payer-system connections) and outsourced revenue-cycle services cluster around this leg. Work-in-progress is tracked explicitly — "unbilled episodes" are a standing agency metric.
- **Quality/compliance reporting** — the same clinical record feeds outcome measurement (improvement in mobility, bathing, transferring; prevention measures such as immunizations; utilization measures such as hospitalizations during care), regulatory submissions, and survey/audit readiness. Quality is not an add-on report; in regulated markets it is tied to payment and star ratings.

### How the Objects Relate

```text
Referral
  ↓ converted
Patient (home-based, of record)
  ↓ admitted into
Episode of care  ← governed by → Plan of care (authorizing services)
  ↓ generates
Scheduled visits  → assigned to → Clinician (by discipline)
  ↓ produces
Visit documentation (field-captured, reviewed)
  ↓ feeds
Clinical record ──→ Claims / billing → payment
       └──────────→ Quality & compliance reporting
```

The episode sits at the center of the workflow: it authorizes the visits, frames the documentation, defines the billing periods, and anchors the quality measurement.

### Standard Capabilities (common in mature products, not definitional)

- Referral intake funnel with conversion tracking and admission packets.
- Visit scheduling with discipline/territory matching, route awareness, and continuity-of-care preferences.
- Offline-capable mobile point-of-care documentation with monitored synchronization.
- Discipline-specific charting templates (nursing, PT, OT, SLP, aide) and structured assessment instruments.
- Plan-of-care and physician-order management with signature routing.
- Clinical review queues (supervisor review, correction workflows before documentation closes).
- Claims generation, payer/clearinghouse connectivity, payment posting, AR/unbilled tracking.
- Analytics: census, field productivity (time in home, drive time, documentation time), office productivity (backlog, hours to close), quality dashboards, staffing optimization.
- Multi-branch management, role-based access, clinician credential/compliance tracking.
- Patient/family engagement surfaces and interoperability connections to hospitals and physician practices.

### Optional / Advanced

- AI documentation assistance (ambient scribing), hospitalization-risk prediction, telehealth and remote-monitoring ingestion, hospital-at-home program support, outsourced billing and authorization services, family portals.

## How It Works

### 1. Referral → admission

A hospital, physician practice, or family refers a patient. Intake staff verify insurance/payer coverage, record the referral, and convert it into an **admission**: the patient of record is created, an episode opens, and the start-of-care paperwork packet is assembled. Referral-to-admission speed is a managed metric (agencies track "days to admit" and open-packet backlogs).

### 2. Start of care and the plan of care

The first visit is a comprehensive assessment in the home. From it, the agency establishes the **plan of care**: the skilled services to be delivered (e.g., nursing plus physical therapy), visit frequency and duration, and the patient's goals. The authorizing physician signs the plan; the agency's staff execute and communicate against it. In US Medicare practice, standardized assessment data is collected at this moment and anchors both payment and quality reporting.

### 3. Schedule and assign visits

The plan of care's service pattern becomes scheduled visits. Schedulers assign each visit to a clinician of the right discipline, balancing territory, workload, and continuity (the same clinician seeing the same patient builds trust and improves outcomes). The visit lands on the clinician's mobile schedule.

### 4. The field documentation loop

```text
Clinician opens mobile app
→ syncs the day's schedule
→ travels to the patient's home
→ performs the visit
→ documents at the point of care (offline-capable in mature products; syncs when connectivity returns)
→ submits the visit documentation
→ supervisor/clinical review
→ visit record complete
```

The field loop is the operational heart of the Type. Documentation happens in the living room, not at a desk, so the mobile surface must capture full clinical content without connectivity and reconcile it later. Sync success and documentation time are themselves monitored, because incomplete or late documentation stalls everything downstream.

### 5. Recertification, resumption, discharge

Episodes are bounded. If care must continue past the authorized period, the agency re-assesses and re-authorizes (recertification). If care is interrupted and resumes, the record reflects it. At discharge, a final assessment closes the episode and measures outcomes against the start of care.

### 6. Billing and payment

Completed, reviewed documentation becomes billable activity. Billing staff generate claims organized by episode and visit, submit them to payers through connected channels, track denials and outstanding balances, and post payments. The loop is governed by a hard dependency: **care that is not documented cannot be billed**, which is why unbilled-episode aging is a standing management view.

### 7. Quality and compliance

Assessment and visit data roll up into outcome measures (improvement in ambulation, bathing, transferring; immunization and prevention measures; hospitalization during care), regulatory submissions, and survey-readiness materials. Agencies run formal quality-improvement cycles on this data; in regulated markets the measures affect public ratings and payment.

### Capability tiers

- **Defining core**: home-based patient of record; episode under plan of care; field-documented visits; revenue-and-compliance loop.
- **Standard capabilities**: intake funnel, scheduling, offline mobile charting, review queues, claims connectivity, analytics, multi-branch administration.
- **Optional**: AI scribing, risk prediction, telehealth/RPM ingestion, outsourced revenue-cycle services, family portals.

## Interfaces

### Office web application

The agency's operational cockpit. Typical surfaces:

- **Patient chart / record** — the patient's demographics, coverage, clinical history, episode list, plan of care, medications, visit history, and documents. Primary actions: open an episode, review documentation, update the plan of care, message the care team.
- **Schedule / calendar** — the agency's visit calendar by day/week, filterable by clinician, discipline, branch. Primary actions: create, assign, reschedule, and confirm visits; spot uncovered visits.
- **Intake worklist** — inbound referrals with status (received → verified → admitted), conversion tracking. Primary actions: verify coverage, open admission, assemble the packet.
- **Clinical review queue** — documentation awaiting supervisory review, flagged by completeness or exception rules. Primary actions: review, correct, return to the field clinician, complete the visit record.
- **Billing / claims** — episode and visit billing status, claim batches, denials, payments, unbilled aging. Primary actions: generate claims, correct and resubmit, post payments.
- **Analytics dashboards** — census, admissions/recerts/discharges, referral conversion, productivity (field and office), quality measures, financial position. Primary actions: drill down to branch, payor, clinician, patient.
- **Administration** — staff and roles, payer setup, compliance/credential tracking, branch configuration.

### Field mobile application

The clinician's companion in the home:

- **Today's schedule** — visits with patient, address, discipline, and status.
- **Visit documentation forms** — discipline-specific assessment and note content, vitals, interventions, patient response; captured at the point of care, offline-capable in mature products.
- **Sync status** — the state of documentation awaiting synchronization; connectivity is an explicit, visible concern in products with offline capture.
- **Patient context** — history, medications, plan of care, prior visit notes, available at the bedside.

### Reporting surfaces for leadership

Census, quality, and financial dashboards consumed by executives and directors of nursing — the same data as office analytics, framed for management review.

## Important Rules / Behaviors

- **Documentation gates money.** A visit that is not documented and reviewed does not become a claim. Unbilled-episode aging is a first-class operational metric, and office productivity is measured in hours-to-close precisely because documentation backlogs directly delay payment.
- **The episode bounds the work.** Services are delivered and billed within the authorized episode; continuing care past its boundary requires re-assessment and re-authorization (recertification). The episode, not the calendar month, is the natural billing and reporting frame.
- **The plan of care authorizes the services.** What clinicians deliver in the home traces back to an authorized plan; changes to services route through the authorizing physician. Care outside the plan is a compliance exposure, not just a workflow deviation.
- **Field capture is offline-tolerant.** Homes have unreliable connectivity; the field surface must capture complete clinical content offline and synchronize later. Sync success is monitored because it gates the review-and-billing chain.
- **Review before completion.** Completed field documentation typically passes a supervisory/clinical review before the visit record closes — a quality and compliance control built into the workflow, not an afterthought.
- **Quality data and payment share a source.** The same assessments that support claims also feed outcome measures and regulatory reporting; errors in clinical documentation therefore propagate into both money and quality ratings.
- **Regulatory regimes shape the machinery, not the core.** In the US, standardized assessment instruments, episode payment models, visit-verification requirements in some state-funded contexts, and survey readiness drive substantial product machinery. These are regime-specific implementations; the underlying structure (authorized episode, documented visits, claims, quality reporting) is the Type itself.
- **Privacy and security are structural.** The system holds protected clinical records about identifiable patients, accessed by distributed field staff — access control by role and branch is a standing requirement.

## Variants

- **US Medicare-certified agency** — the canonical pole: full episode/certification structure, standardized assessments, payer claims, quality reporting, survey readiness.
- **Mixed / private-pay agencies** — smaller agencies blending skilled visits with private-pay services; lighter regulatory machinery, same core loop.
- **Multi-line post-acute platforms** — the dominant market packaging: one vendor platform offering home health alongside hospice, personal care, and facility lines as separate products or modules sharing infrastructure.
- **Therapy-heavy agencies** — organizations built around physical/occupational/speech therapy staffing, with discipline-specific workflows emphasized.
- **International equivalents** — community and district nursing services under national health systems organize the same abstract core (referred patient, authorizing care plan, visit records, funder reporting) under different regimes and vocabulary.
- **Scale variants** — single-branch independent agencies vs enterprise multi-branch providers with regional management layers.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Home Care Agency Management | closest sibling | non-skilled personal/support care; the visit record is a service/attendance record (tasks, time on site, visit verification), not a clinical chart; no physician plan of care, no clinical assessments, no clinical quality reporting |
| Hospice Management | adjacent sibling | end-of-life comfort care with its own machinery (interdisciplinary group meetings, bereavement); home health is restorative/maintenance skilled care with recertification cycles; same platform families, different workflow objects |
| Electronic Health Record (generic) | adjacent | records encounter-based care in offices/facilities; lacks the agency's in-home episode operations — field scheduling, offline field charting, per-episode payer billing, agency quality reporting |
| Skilled Nursing Facility Management / Long-term Care EHR | adjacent | facility-resident care with 24-hour on-site operations vs visit-based care in the patient's home |
| Healthcare Revenue Cycle Management | overlapping capability | the revenue loop here is one leg of an agency system fused to the clinical record, not a standalone claims factory |
| Remote Patient Monitoring | adjacent module | collects physiologic data between visits; may attach to this Type, but the record of care delivery remains the visit |
| Referral-growth CRM (post-acute) | adjacent, market-side | manages referral-source relationships and the referral funnel on the marketing side; terminates at handoff, holds no clinical or operational record |
| Care Coordination Platform | adjacent | coordinates transitions and shared care plans across organizations; does not hold the delivering agency's clinical record of in-home care |

The boundary with **Home Care Agency Management** is the most consequential one: the two share agencies, caregivers, scheduled home visits, visit-level records, and service-to-money translation. The seam is what the visit record *is* and what *authorizes* the care — a clinical note tied to a physician-directed plan of care makes it home health; a task/attendance record tied to a service authorization makes it home care.

## Representative Products

- **Homecare Homebase (HCHB)** — workflow-first home-based-care EHR; office web platform plus offline-capable Android field app; analytics and revenue-cycle services around the core.
- **Netsmart (myUnity / Home Health)** — post-acute continuum EHR family; home health as one community alongside hospice, senior living, and skilled nursing; assessment-compliance and payment analytics attached.
- **WellSky Home Health** — enterprise post-acute suite line within WellSky's home-and-post-acute catalog, alongside hospice, palliative, and personal care lines.

Axxess is another major vendor in this market; its site could not be reached during research and it was not sampled.

## Sources

Research date: **2026-09-08**

- Homecare Homebase — homepage https://hchb.com/ ; FAQ https://hchb.com/resources/faqs/ ; "Home Health Agency Analytics: Best Metrics to Track Staffing Utilization, Productivity and Patient Satisfaction" (2021) https://hchb.com/home-health/
- Netsmart — https://www.ntst.com/ (Home Health community and myUnity product descriptions; OASIS/PDGM analytics; EVV workforce modules)
- WellSky — https://www.wellsky.com/ (Home & post-acute solution family: Home Health, Home Health Therapy, DDE & Payer Connection)
- Brightree — https://www.brightree.com/ (reviewed; current positioning is HME/DME + pharmacy, not home health)
- Casamba / Net Health — https://www.casamba.net/ (reviewed; home health line not presented)
- PlayMaker Health / Trella Health — https://www.playmakerhealth.com/ (reviewed; referral-growth CRM, not a home health EHR)

> Sourcing limitation: vendor help centers and user guides (operational documentation) were not reachable from the research environment on 2026-09-08; product evidence comes from official product, support, and article pages. Axxess and CMS.gov were unreachable. Accordingly, this document states no precise regulatory parameters (assessment timepoints, payment-model details, verification rules) and calibrates workflow claims to the cross-product structure visible in the fetched sources.

Detailed evidence, product-by-product observations, the cross-product comparison, and the historical/market-sample check are recorded in the paired Research Notes.
