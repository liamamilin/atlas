# Medical Device Post-market Surveillance

## Overview

A **Medical Device Post-market Surveillance** application is the medical-device manufacturer's post-market safety system of record: it holds the marketed device as a managed subject, captures safety events from the field — complaints, adverse events and incidents, malfunctions, and other user feedback — as individually identified records, assesses each event against the applicable device-reporting regime, produces and tracks regulator-facing reports for reportable events, trends events across the device population to surface emerging risks, and feeds the findings back into risk management and corrective action.

Its purpose is the regulatory and clinical half of life after launch: once a device is on the market, the manufacturer is obligated to know what is happening to it in real use, to decide which events must be reported to authorities, to report them, and to keep evidence that it did so. The defining core is small:

```text
Marketed device (surveillance subject of record)
└── Field safety events (complaints / adverse events / malfunctions / feedback)
    └── Assessment & reportability determination
        └── Regulator-facing reports, tracked to acknowledgement
    └── Trending / signal analysis across the device population
        └── Findings fed back into risk management & corrective action
```

Everything else commonly associated with the discipline — multi-channel intake, structured adverse-event case processing and exchange formats, periodic summary reports, post-market clinical follow-up (PMCF) studies, statistical signal detection, AI-assisted intake — is widespread in current products but is the standard capability layer, not what makes the software this Type.

The boundary: when the center of gravity is the quality-event loop (deviations, nonconformances, CAPAs as the quality system's evidence), the product is a Life Sciences QMS; when it is the device's design-control record chain, it is Medical Device Lifecycle Management; when the same surveillance loop runs over medicinal products, it is a Pharmacovigilance Platform; when complaints are handled as customer service with no regulatory safety loop, it is Complaint & Escalation Management.

## Users & Context

Primary users sit in the manufacturer's post-market organization:

- **Complaints / post-market specialists** — receive field events from every channel, log them, run investigations and evaluations, and document decisions.
- **Vigilance / medical-safety staff** — assess events for reportability, prepare regulator-facing reports, and manage submission and acknowledgement status.
- **Quality and regulatory affairs** — own the procedures the events flow through, escalate systemic issues into CAPA, and keep the record base inspection-ready.

Secondary users:

- **Product development / R&D** — consume field experience as input to root-cause work and design improvements.
- **Management** — read trend dashboards and risk exposure across product groups.

The operating context is a device (or device family) already cleared or certified and in commercial distribution, under a device-reporting regime (for example FDA medical-device reporting in the US, vigilance under the EU Medical Device Regulation in Europe). Events arrive from outside the manufacturer — users, healthcare providers, distributors, call centers, field representatives, literature, registries — which is why intake surfaces and channel handling are part of the product. The work is deadline-sensitive and audit-facing: records must be attributable, traceable, and defensible years later.

## Core Model

### The Defining Core

**1. The marketed device as the surveillance subject of record.**
A persistent, individually identified record of the device or device family under surveillance. Every complaint, incident, report, and post-market data point attaches to it; reporting tools aggregate feedback by product group; post-market surveys can be linked to specific device profiles. Without it, the software is a complaint log or a safety case system with nothing device-shaped at the center.

**2. The field safety event of record.**
The unit of surveillance: a complaint, adverse event or incident, malfunction, or piece of field feedback, held as an individually identified record with its source channel, the affected device, an investigation, and an assessment. Complaints and adverse-event cases are commonly linked (a complaint that involves an adverse event connects to the safety case built on it). Without it, there is nothing to surveil.

**3. The regulatory safety loop over events.**
Each event is assessed against the regime's reportability criteria, and the determination is documented. Reportable events produce regulator-facing reports, whose generation and submission are tracked through to regulatory acknowledgement. Across events, the system trends complaints and incidents — by product group, over elapsed time, against thresholds — so that emerging safety signals surface at population level, and the findings route into risk management and corrective action. Without it, the software is customer-service complaint handling; without the trending half, it is per-event case processing with no surveillance.

These three are held jointly. A device registry without events is a product master; events without the regulatory loop are a complaint desk; the loop without events is a rules engine with nothing to report on; events and loop without the device subject are a generic safety case system.

### Standard Capabilities of Mature Products

- **Multi-channel intake** — capture of events from email, call centers, field representatives, web portals, and mobile reporting forms; automated case creation from captured data, with duplicate detection in some products.
- **Adverse-event case processing** — structured case files with medical coding, follow-up, and exchange in regulated formats (E2B-class for safety reporting); some products add device-specific data gateways.
- **Reportability machinery** — configurable rules or matrices that route each case to the required reporting path per market; some products automate report labeling and submission.
- **Periodic summary reporting** — regime-dependent periodic reports summarizing events over a period (device-regime templates in EU guidance alongside drug-regime report classes in multivigilance products).
- **Trend and signal analysis** — threshold-based routing of events into investigation, statistical signal detection, dashboards tracking complaints by product group, elapsed times, and pending regulatory acknowledgements.
- **Quality-loop linkage** — escalation of systemic events into CAPA; interlinking of complaints with the device's design and risk records so field experience reaches the people who can change the product.
- **PMCF data collection** — post-market clinical follow-up surveys and studies aligned to EU MDR expectations, often built on clinical-grade machinery (validated study builders, subject validation, e-consent, device-linked or anonymous participation).
- **Literature and registry monitoring** — systematic capture of published safety information as events.
- **Regulated-record posture** — attributed, time-stamped, audit-trailed records with electronic-signature approval workflows, validated to recognized compliance frameworks.
- **AI assistance** — automated complaint classification, detection of adverse events inside complaints, narrative drafting (era-current).

### One Structure, Many Implementations

```text
Concept:  Marketed device as surveillance subject
Implementations:  product/device-family records; product groups; device profiles linked to surveys

Concept:  Field safety event of record
Implementations:  complaint records (eQMS pole); adverse-event cases (safety pole); linked complaint↔case pairs

Concept:  Reportability determination
Implementations:  documented per-event decisions with report-generation tasks; rules-based reportability matrices

Concept:  Regulator-facing reporting
Implementations:  generated reports sent to authorities with acknowledgement tracking; structured exchange via gateways

Concept:  Population-level surveillance
Implementations:  threshold routing; trend dashboards; statistical signal detection (PRR/ROR-class)
```

A reader who has only seen one packaging (for example, complaints inside a quality system) should still be able to recognize a standalone device-vigilance case system as the same Type from this model.

## How It Works

### Receive and log a field event

```text
Event arrives (call center / email / field rep / portal / literature)
→ logged as an identified record against the affected device
→ source, device identity, and initial details captured
→ duplicates checked
```

Intake is deliberately multi-channel because events originate outside the manufacturer; some products let reporters submit directly through web or mobile forms.

### Investigate and assess

```text
Assign the event for review
→ investigate (sample returns, technical evaluation, root cause where systemic)
→ assess severity and whether an adverse event is involved
→ link to the adverse-event case where applicable
→ document the assessment
```

The event record accumulates its own history; linked records (design, risk, prior complaints for the same device) are reachable from it.

### Determine reportability and report

```text
Assess the event against the regime's reporting criteria
→ document the determination (reportable / not reportable) and its basis
→ if reportable: generate the regulator-facing report
→ submit through the required channel
→ track to regulatory acknowledgement
```

Rules engines or reportability matrices automate the routing decision per market; the decision itself remains a documented, attributable act. Timelines and escalation requirements are tracked by the system.

### Watch the population

```text
Events accumulate per device / product group
→ trend views (counts, rates, elapsed times, pending acknowledgements)
→ thresholds or statistical signals flag unusual patterns
→ flagged patterns route into investigation or CAPA
```

This is the "surveillance" half: individual events become a population-level picture, and the picture drives action.

### Close the loop into quality and design

```text
Systemic issue identified
→ escalate to CAPA (corrective/preventive action process)
→ update the device's risk management file
→ feed design improvements
→ post-market clinical follow-up (where applicable): surveys/studies collect
   outcome, usability, and safety data from device users over time
```

### Collect post-market clinical evidence (where the regime requires it)

```text
Define a post-market survey or study for the device
→ distribute to users (email / SMS / QR)
→ collect outcome, safety, and usability data, device-linked or anonymous
→ results join the device's post-market evidence base
```

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Event intake surfaces

- Purpose: turn field reports into records.
- Typical information: reporter, channel, affected device, event description, dates.
- Primary actions: log event, attach files, create linked adverse-event case.

### Event / case workspace

- Purpose: the working surface for one event's life.
- Typical information: event record, linked device, investigation steps, assessment, tasks, decision documentation.
- Primary actions: assign, investigate, assess, determine reportability, escalate to CAPA, close.

### Reporting / submission view

- Purpose: manage regulator-facing obligations.
- Typical information: reportable events, report status, submission records, pending acknowledgements, elapsed time against requirements.
- Primary actions: generate report, submit, record acknowledgement, escalate overdue items.

### Trend / analytics dashboards

- Purpose: population-level oversight.
- Typical information: complaint and event counts by product group, trends over time, signal flags, ageing and response-time views.
- Primary actions: drill into events, configure thresholds, export for review.

### Post-market survey / study builder (where present)

- Purpose: run PMCF data collection.
- Typical information: study definition, questions, distribution plan, response status per participant/device.
- Primary actions: build survey, distribute, monitor responses, export data.

### Administration / configuration

- Purpose: adapt the system to the manufacturer's procedures and markets.
- Typical information: workflows, reportability rules, thresholds, coding lists, user roles.
- Primary actions: configure workflow stages, edit reportability rules, manage users.

## Important Rules / Behaviors

- **Reportability is a documented determination, not an automatic label.** The system may propose or route, but the decision that an event is (or is not) reportable is recorded with its basis, because regulators and auditors will read it later.
- **Reporting obligations have deadlines and acknowledgement states.** The system tracks events pending regulatory acknowledgement and elapsed times; overdue or unacknowledged reports are visible exceptions.
- **Systemic events escalate.** A single complaint is handled as an event; a pattern or systemic issue escalates into CAPA. Thresholds make this routing systematic rather than discretionary.
- **Complaints and adverse-event cases are distinct records, and mature products link them.** A product-quality complaint that involves an adverse event connects to the safety case processed for reporting; safety-platform products document this linkage explicitly so quality and safety oversight stay coordinated.
- **Records are regulated records.** Attributed authorship, time-stamped history, approval signatures, and audit trails are structural: the record base must survive inspection years after the fact.
- **The device subject anchors everything.** Trending, reporting, and post-market evidence are all organized by device or product group; removing the device binding dissolves the Type.

## Variants

- **eQMS-embedded** — post-market surveillance realized as complaint records, quality-event escalation, and PMCF surveys inside the manufacturer's quality management system; the dominant shape for small and mid-size device companies.
- **Enterprise QMS add-on** — post-market surveillance as a named module of a broader regulated-manufacturing suite, unified with document control, CAPA, risk, and manufacturing records.
- **Standalone safety platform** — case-processing-centered systems with structured exchange, reportability matrices, and signal detection, serving large manufacturers and, in some cases, health authorities.
- **Multivigilance platform** — one platform configured for several vigilance domains (medicinal products, medical devices, cosmetics, nutrition, blood); the device domain shares the case machinery with the others.
- **Regime emphasis** — FDA-reporting-centric, EU-MDR-vigilance-centric, or multi-regime deployments; periodic-report and PMCF depth follows the regime.
- **Device class** — hardware devices, IVDs/diagnostics, software as a medical device, and combination products each stress different identifiers and data.
- **Scale** — self-service deployments priced for small case volumes through enterprise deployments processing high case volumes.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Life Sciences QMS | adjacent, overlapping on complaints | eQMS centers the quality-event/action loop (deviations, NCs, CAPAs, audits) as the quality system's evidence of record; here the center is the field-safety-event → reportability → surveillance loop over marketed devices. Complaints are one quality-event class there; the primary safety record class here. |
| Medical Device Lifecycle Management | upstream sibling | that Type holds the device's design-control record chain and controlled change (concept → design → market); this Type holds the vigilance loop over the marketed device. Post-market linkage connects them: field events feed design and risk; the centers of gravity are distinct record worlds. |
| Pharmacovigilance Platform | same-loop sibling, different object | the same case → reportability → reporting → signal loop run over medicinal products with drug-regime artifacts; multivigilance products realize both domains as configurations of one platform. The device subject and device-regime artifacts are the seam. |
| CAPA Management | downstream process | CAPA is the corrective-action process this Type feeds; systemic events escalate into it. CAPA Management centers the action process itself, not the field-event surveillance loop. |
| Complaint & Escalation Management | adjacent, unregulated pole | generic customer-service complaint handling (service recovery, escalation) for any industry; here complaints are a regulated safety record class whose assessment drives regulator-facing reporting. Remove the regulatory safety loop and this Type collapses into that one. |
| Regulatory Information Management | adjacent | RIM holds the registration/dossier/submission estate; this Type produces safety reports from its event record world that may be filed through regulatory channels, but does not hold the dossier. |
| Clinical Trial Management / EDC | capability overlap | PMCF studies and post-market surveys may run on clinical-grade machinery (validated study builders, GCP-style conduct); the surveillance loop, not clinical trial operations, is this Type's center. |

## Representative Products

- **Greenlight Guru** — device-native eQMS; post-market realized as complaint management, quality-event escalation, and post-market clinical surveys (PMCF).
- **MasterControl** — enterprise regulated-manufacturing suite; post-market surveillance as a named add-on unified with core quality processes.
- **ArisGlobal LifeSphere (MultiVigilance, Product Complaints)** — enterprise safety platform; case processing with complaint-to-adverse-event linkage.
- **AB Cube SafetyEasy Suite** — multivigilance platform with an explicit medical-device vigilance domain, device data gateway, and device-regime report templates.

## Sources

Research date: **2026-09-08**

Official vendor product/solution pages:

- Greenlight Guru — "Managing Postmarket Quality" (https://www.greenlight.guru/postmarket-surveillance-medical-device), Complaint Management (https://www.greenlight.guru/complaint-management-software), Post-Market Survey (https://www.greenlight.guru/post-market-survey)
- MasterControl — Postmarket (https://www.mastercontrol.com/postmarket/)
- ArisGlobal — LifeSphere MultiVigilance (https://www.arisglobal.com/lifesphere/safety/multivigilance-system/), Product Complaints (https://www.arisglobal.com/product-complaints/)
- AB Cube — SafetyEasy Suite (https://www.ab-cube.com/), SafetyEasy Vigilance (https://www.ab-cube.com/vigilance/)

> Sourcing limitation: vendor help centers / user guides were not reachable in this research pass; evidence is product- and solution-page depth (feature lists, FAQ statements, module descriptions). Precise operational details — exact reporting deadlines, specific form identifiers, numeric thresholds, plan-gated capabilities — are intentionally not stated in this document. One additional vendor (Oracle safety product) was unreachable and abandoned; one candidate sample lacked a device-vigilance surface and was dropped. Detailed observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
