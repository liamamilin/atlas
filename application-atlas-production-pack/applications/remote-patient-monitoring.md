# Remote Patient Monitoring

## Overview

A **Remote Patient Monitoring (RPM) platform** is the clinician-side system through which a care organization monitors enrolled patients outside the care facility — most often in their homes — using physiological measurements transmitted automatically from connected medical devices, and through which the care team continuously reviews that data, responds to alerts, and records the clinical actions taken.

The defining core is small:

```text
Enrolled monitored patient (outside the facility)
└── Device-originated physiological data stream
    └── Clinical surveillance loop
        └── Review against parameters → alert on exceptions → intervene and record
```

Everything commonly associated with modern RPM products — cellular-connected device kits, patient mobile apps, fulfillment logistics, condition-specific care plans, EHR-native integration, automated billing capture, AI-driven deterioration prediction — is widespread in current products but is not what makes the product an RPM platform. Earlier generations of home telemonitoring (phone-line transmission of home blood-pressure or weight readings to a nurse station) satisfy the same core without any of those specifics.

When the dominant surface shifts to the scheduled remote encounter, the product is drifting toward a Telehealth Platform; when it shifts to care-plan coordination and service time without physiological device data, toward Chronic Care Management; when data collection continues but no care team reviews or acts, the product has left the Type and become a consumer tracker or a device-data pipeline.

## Users & Context

The primary user is a **clinical monitoring team** — typically nurses, medical assistants, or care managers who watch a panel of enrolled patients, work through alert queues, contact patients, and document their activity. Physicians participate as the accountable clinical authority: they set or approve monitoring parameters, receive escalations, and adjust treatment.

The **patient** is a monitored subject rather than a primary operator. Their required participation is deliberately minimal in mature products: take the measurement with the issued device; the transmission happens without their effort. Many programs are designed so that patients who never install an app still participate fully.

Secondary users:

- **program/operations staff** — enroll patients, order and track devices, manage inventory and supplies
- **billing staff** — monitor documentation completeness and billing eligibility across the enrolled population
- **vendor-side clinical teams** — in fully-managed arrangements, the vendor's own nurses operate the surveillance loop on the care organization's behalf

The work context is a standing program, not a visit: a care organization (physician practice, health system, payer-sponsored program) enrolls a defined patient population — commonly chronic-condition patients (hypertension, diabetes, heart failure, COPD), maternity patients, or post-discharge patients — and carries the monitoring responsibility continuously for as long as the patient stays enrolled.

## Core Model

### The Defining Core

Three structures, jointly held. Remove any one and the product is no longer an RPM platform.

**1. The enrolled monitored patient as anchor of record.**
A patient formally enrolled in a monitoring program, located outside the care facility, with an assigned care team responsible for watching them. Enrollment is an explicit act: the patient is identified, a monitoring regimen is set, devices are ordered and bound to them, and a status (enrolled, active, ended) is tracked. Every reading, threshold, alert, intervention, and billing record attaches to this patient. Without the enrolled-patient anchor, the system is anonymous device telemetry.

**2. The device-originated physiological data stream.**
Connected medical devices — blood-pressure monitors, weight scales, glucose meters, pulse oximeters, thermometers, peak-flow meters, continuous sensors — capture physiological measurements at the patient's location and transmit them to the platform without a clinical encounter and, in modern products, without patient-side technical effort. The reading is the unit of data: timestamped, attributed to a device and patient, accumulated as a per-patient time series. This is what distinguishes RPM from encounter-based remote care: the data exists between and outside visits, produced by the body at home rather than by a clinician's examination.

**3. The clinical surveillance-and-intervention loop.**
The care team reviews the incoming data stream against defined parameters (thresholds and rules), is alerted to exceptions — out-of-range values, adverse trends, and missing readings — and intervenes: contacting the patient, adjusting the care plan, escalating to a physician, or in urgent cases directing the patient to emergency care. The intervention is recorded against the patient. Without this loop, the system is a passive data logger or a consumer tracker; the clinical accountability is what makes it a medical application.

### Standard Capabilities

Mature products commonly carry these capabilities. They make RPM programs practical; they do not define the Type.

- **Device logistics** — ordering, provisioning, shipping, activation tracking, replacement, and supply replenishment (test strips, cuffs, batteries), operated as a first-class workflow because devices must physically reach patients and keep working.
- **Threshold and protocol configuration** — per-patient and per-condition parameters that decide when a reading becomes an alert; increasingly pattern-aware (sustained episodes, multi-day trends, condition-specific patterns such as rapid weight gain).
- **Exception-first clinical worklist** — a prioritized alert/caseload queue so a care manager responsible for a large panel works the exceptions rather than scrolling raw feeds.
- **Patient engagement surface** — an app or portal with readings, reminders, education, and secure messaging; commonly optional for participation when devices transmit on their own.
- **Symptom and questionnaire capture** — patient-reported symptoms and wellness questions alongside device vitals.
- **Care plans** — condition-specific monitoring regimens (measurement frequency, thresholds, questionnaires, escalation rules) applied to enrolled patients.
- **Time capture and billing support** — automatic logging of clinical interaction time and surfacing of billing eligibility; in the US market this maps to a small set of RPM-specific billing codes (setup, device-supply-with-transmission-days, and monthly care-management time), with the platform tracking which patients meet which criteria.
- **EHR integration and APIs** — readings written into the clinical chart, alerts routed into clinician inboxes, charges into the revenue cycle; or data delivered programmatically into other clinical systems.
- **Adherence machinery** — missed-reading detection, reminders, and outreach, because a silent patient is both a clinical risk and a program-compliance problem.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:   Device-originated data stream
Realizations:  cellular device → vendor cloud;  Bluetooth device → home gateway → cloud;
               patient-app-paired device;  patient-owned device authorized by the patient;
               (historically) phone-line transmission from a home device

Concept:   Clinical surveillance surface
Realizations:  standalone RPM dashboard;  EHR-native views inside the chart;
               data delivered via API into the organization's own platform

Concept:   The surveillance workforce
Realizations:  the organization's own nurses;  a vendor-staffed monitoring team;
               any split of the two
```

A reader who has only seen the cellular-kit-plus-dashboard pattern should still be able to recognize app-paired, API-delivered, or phone-line-era implementations as the same Type.

## How It Works

### Enroll and equip the patient

```text
Identify eligible patient
→ enroll in the monitoring program (consent, regimen, responsible team)
→ order device(s) from the platform
→ kit ships to the patient's home (pre-configured where possible)
→ device activates on first reading; enrollment status updates automatically
→ patient educated on the regimen
```

The logistics loop is operational work the platform tracks end to end: shipment status, delivery, first successful reading ("connected"), replacement, and eventual un-linking when the patient leaves the program. Supplies that wear out (strips, cuffs, batteries) are replenished on usage triggers.

### The data stream

```text
Patient takes a measurement at home
→ device transmits automatically (cellular, gateway, or app-paired)
→ platform receives, validates, and stores the reading
→ reading appears in the clinical surface and (where integrated) the EHR chart
```

Transmission is designed to require nothing from the patient beyond taking the measurement. This is a deliberate design point across the sampled products: every removed setup step (Wi-Fi configuration, pairing, app installation) removes a failure point in adherence.

### The surveillance loop

```text
Reading arrives
→ evaluated against the patient's thresholds/protocol
→ in range: accumulates into trends and adherence history
→ out of range or pattern-positive: becomes an alert in the worklist
→ care manager reviews, contacts the patient, documents the interaction
→ resolved, or escalated to physician / urgent care
→ care plan or medication adjusted; monitoring continues
```

The loop runs continuously for the life of the enrollment. Two exception classes drive daily work: **clinical exceptions** (bad values, bad trends) and **compliance exceptions** (no readings — the patient has gone silent). Both surface in the same queue.

### Document and bill

```text
Clinical interactions occur (alert reviews, calls, messages, adjustments)
→ platform logs the time and content automatically
→ eligibility against billing criteria is tracked per patient per period
→ charges generated and pushed into the revenue cycle (where applicable)
```

In the US market, reimbursement is tied to documented device-transmission days and documented clinical-management time, which is why time capture is built into the workflow rather than reconstructed afterward. In other markets or value-based arrangements, the same documentation serves program reporting instead of fee-for-service billing.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Clinical dashboard / caseload worklist

The care team's primary entry surface.

- Purpose: work the monitored panel by exception.
- Typical information: patient list with latest readings, alert state, trend indicators, adherence status; filters by group, condition, priority, assignee.
- Primary actions: open a patient, work the alert queue, contact a patient, document an interaction.

### Alert queue

The exception stream.

- Purpose: surface readings and patterns that need human judgment, in priority order.
- Typical information: patient, triggering value or pattern (e.g., sustained hypertension, rapid weight gain, trending glucose, no reading for days), time since event.
- Primary actions: review context, acknowledge, contact patient, escalate, resolve with documentation.

### Patient detail view

The per-patient monitoring record.

- Typical information: reading history and trends per vital, device inventory and status, thresholds/protocol, symptoms and questionnaires, interaction history, enrollment status, billing/documentation status.
- Primary actions: adjust thresholds, update care plan, message or call, log time, manage devices.

### Patient-facing app / portal

The monitored person's surface — commonly optional.

- Typical information: latest readings, reminders, education content, care-plan tasks, symptom questionnaires.
- Primary actions: take/confirm readings (where the device is app-paired), answer questions, message the care team, view trends.

### Device logistics / inventory views

The operational surface.

- Typical information: orders, shipment and delivery status, activation state, inventory levels, supply-replenishment status.
- Primary actions: order devices, track shipments, replace devices, trigger supply reorders.

### Billing / documentation views

- Typical information: per-patient documentation status against billing criteria for the current period, generated charges, program-level compliance and revenue reporting.
- Primary actions: review eligibility, generate/submit charges, correct documentation.

## Important Rules / Behaviors

### Readings are device-originated and attributed

A reading carries its device, patient, and timestamp. This provenance matters clinically (device-measured values are treated differently from patient-reported ones) and for billing (transmission days are counted from device data). Patient-entered values, where supported, are distinguished from device readings.

### Missing readings are a signal, not an absence

The platform tracks whether expected readings occur. A patient who stops transmitting generates alerts and outreach — silence is treated as a clinical and program risk, not merely empty data.

### Thresholds are configurable and layered

Alerts are not fixed industry constants. Parameters are set per patient and/or per condition protocol, and mature products evaluate patterns (trends over multiple readings, sustained episodes, condition-specific rules) rather than single values alone. Who may change thresholds — nurse, physician, protocol — is a permission question each organization answers.

### The surveillance loop is accountable and documented

Reviews, contacts, and escalations are recorded as clinical activity against the patient. This documentation is simultaneously clinical record, coordination memory, and (in fee-for-service markets) billing evidence — which is why it is captured as work happens rather than reconstructed.

### Escalation has defined paths

Alerts route to the responsible monitoring staff; escalations route to physicians or urgent-care guidance. In fully-managed arrangements, the vendor's clinical team operates under the organization's protocols, with the organization's physicians remaining the clinical authority.

### Enrollment is a bounded state

Patients are enrolled into a program and eventually end enrollment (graduation, program end, device return/un-linking). Device data flow and billing eligibility follow enrollment state; un-linking a device stops the stream and the clock.

### Privacy and security posture

The platform handles protected health information: encrypted transmission and storage, access controls, audit logging, and formal data-processing agreements with the care organization are baseline requirements, and patient-facing support must operate within the same constraints.

## Variants

- **Chronic-condition programs** — the dominant form: hypertension, diabetes, heart failure, COPD, CKD, maternity monitoring, each with condition-specific protocols.
- **Post-acute and acute programs** — post-discharge monitoring and hospital-at-home: higher acuity, continuous or multi-parameter sensing, deterioration prediction, tighter escalation to physicians and in-home clinical services.
- **Service-model spectrum** — the organization runs monitoring with its own staff; the vendor runs it entirely; or any split. The same infrastructure supports all three; the variable is who staffs the surveillance loop.
- **Hardware posture** — vendor-issued cellular kits (no patient setup), Bluetooth devices with a home gateway, app-paired devices, patient-owned devices (e.g., authorized continuous glucose sensors), and legacy phone-line transmission.
- **Payer context** — US fee-for-service programs with RPM-specific billing codes; value-based and payer-sponsored programs where the same documentation serves risk and quality reporting; non-US systems where monitoring is a clinical service without dedicated billing codes.
- **Integration depth** — standalone platform, EHR-native operation (readings, alerts, and charges living inside the EHR's own surfaces), or API-first delivery into the organization's own software.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Telehealth Platform | primary surface is the scheduled remote encounter (audio/video); RPM's primary surface is the continuous device data stream and surveillance loop between encounters. Commonly bundled. |
| Chronic Care Management | organizes care-plan coordination and service time around a chronic condition, without physiological device data as the core object; the two are sibling programs often run on the same platform. |
| Patient Portal | patient-facing access to records, messages, and services; RPM's defining surface is clinician-side surveillance. An RPM patient app is an engagement surface of the program, not a portal. |
| Consumer wearable / fitness application | collects body data without enrollment, clinical thresholds, a responsible care team, or intervention accountability; no medical-grade device or clinical record. |
| In-facility patient monitoring | same physiological data, but the patient is in the facility and monitoring is bedside/real-time; RPM is defined by the patient's own environment. |
| Home Health EHR / agency management | organizes episodic visits, assessments, and agency operations per episode of care; RPM organizes continuous data surveillance per enrolled patient. |
| Population Health Management | works at registry/panel level (attribution, risk stratification, gap closure); RPM works at person level with a live data stream; population programs commonly consume RPM data. |
| ePRO / eCOA Platform | patient-reported data capture under trial protocols for research; RPM is clinical-care surveillance under a care program. |

The most important boundary is with **Telehealth**: both are "care at a distance," but telehealth is organized around encounters while RPM is organized around the continuous device data stream and the standing surveillance loop. The second is **Chronic Care Management**: both are standing programs with documented time, but CCM's object is coordination work while RPM's object is physiological data.

## Representative Products

- Tenovi — device-data infrastructure and cellular device kits for RPM programs (hardware/API-first pole)
- CoachCare — multi-program remote-care platform with optional outsourced clinical staffing (practice pole)
- CareSimple — end-to-end enterprise RPM with EHR-native integration and flexible staffing (health-system pole)
- Biofourmis — AI-driven monitoring across post-acute and acute/home-hospital programs (acute-care pole)

The Core Model was checked against an earlier-generation structural reference (Vivify Health, whose care-team-portal + patient-portal + devices architecture matches the core; the product is decommissioning and was used only as structural corroboration) and against the historical phone-line home-telemonitoring pattern to avoid over-fitting to the current cellular-kit implementation.

## Sources

Research date: **2026-09-09**

- Tenovi — "Remote Patient Monitoring Software: Guide to APIs and Integration" (https://tenovi.com/remote-patient-monitoring-software/); "8 Features to Look For in a Remote Patient Monitoring Dashboard" (https://www.tenovi.com/remote-patient-monitoring-dashboard/); Tenovi API Docs (https://docs.tenovi.com/); "Typical Dataflow" (https://docs.tenovi.com/hwi-api/typical-dataflow/)
- CoachCare — product overview (https://coachcare.com/); "Remote Patient Monitoring" program page (https://www.coachcare.com/programs/remote-patient-monitoring/)
- CareSimple — product overview (https://caresimple.com/); "Remote Patient Monitoring Platform" (https://caresimple.com/platform/)
- Biofourmis — product overview (https://www.biofourmis.com/); "Platform" (https://www.biofourmis.com/platform)
- Vivify Health — transition notice and system description (https://vivifyhealth.com/)

> Sourcing limitations: a primary regulator page (telehealth.hhs.gov RPM guide) was not reachable (HTTP 403) on the research date. Billing-code specifics in this document are therefore kept at the conceptual level (setup, transmission-day, and care-management-time machinery) with only widely-attested code identifiers referenced; exact rates, thresholds, and 2026 code changes observed on vendor pages were recorded in the Research Notes rather than asserted here. The sampled market is US-heavy; the clinical loop is corroborated against earlier-generation and non-billing-driven monitoring patterns, but non-US product structure was not directly sampled.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
