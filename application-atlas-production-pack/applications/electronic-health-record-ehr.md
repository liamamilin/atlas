# Electronic Health Record / EHR

## Overview

An **Electronic Health Record (EHR)** is a clinician-facing clinical record system that maintains a longitudinal medical record for each identified patient and is used by authorized care providers, in the flow of care, to document encounters, review patient history, and record orders and results.

The defining structure is small:

```text
Identified Patient
└── Longitudinal clinical chart
    ├── Problems / diagnoses
    ├── Medications
    └── Clinical notes / observations
└── Encounter/visit as the organizing unit of documentation
└── Authenticated, attributed documentation by authorized care providers
```

Everything commonly associated with a modern EHR deployment — patient portals, e-prescribing networks, integrated billing, decision-support engines, FHIR APIs, regulatory certification, cloud hosting — is widespread in current products but is not part of the defining core. Open-source ambulatory systems, global program-oriented record systems, and low-resource hospital composites all satisfy the definition without any of those specifics.

When the dominant surface shifts to scheduling and billing operations, the product is drifting toward a Practice Management System; when it shifts to running a laboratory or imaging department, it is a departmental system (LIS/RIS/PACS) that feeds results into the chart; when it serves patients rather than clinicians, it is a Patient Portal.

> Terminology note: the market uses "EMR" (electronic medical record) and "EHR" (electronic health record) largely interchangeably. The historical distinction — a single-organization record versus an interoperable cross-organization record — describes an interoperability posture (a Variant), not two different structures. This document treats them as one Application Type.

## Users & Context

The EHR is the working record of care delivery. Its users are defined by their role in care, and their role determines what they can see and do.

Primary users:

- **Physician / prescriber** — reviews the chart, documents the encounter, diagnoses, orders treatments and investigations, prescribes medications.
- **Nurse** — records vitals and observations, documents care activities, manages visit flow and queues, documents medication administration where in scope.
- **Medical assistant / front-desk staff** — registers patients, maintains demographics, manages appointment and queue context in which encounters happen.

Secondary users:

- **Pharmacist / dispensing staff** (in settings where dispensing is in scope) — dispenses against medication orders.
- **Billing / coding staff** (where revenue-cycle functions are bundled) — codes encounters and produces claims from the recorded clinical data.
- **Administrator / informatics staff** — configures users, roles, forms, templates, and terminology bindings.

The work environment is the point of care: consultation rooms, wards, nursing stations, triage desks. The chart must be available during the encounter — this is what distinguishes an EHR from an archive or a reporting database. In low-connectivity settings, products may be designed to operate on-site or offline; in large organizations, the same record is touched continuously by many roles across a shared patient population.

## Core Model

### The Defining Core

```text
Identified Patient
└── Longitudinal clinical chart (the record of care over time)
    ├── Problems / diagnoses
    ├── Medications
    └── Clinical notes / observations
└── Encounter/visit as the organizing unit of documentation
└── Authenticated, attributed documentation by authorized care providers
    (role-restricted access)
```

Four invariants. If any one is removed, the product is no longer recognizable as an EHR:

- **Identified patient as the record anchor** — every entry in the system belongs to a specific, identified person. The system maintains the patient's identity record (demographics, identifiers). Without this, there is no medical record.
- **Longitudinal chart with core clinical data domains** — the chart accumulates over time and carries, at minimum, the problem/diagnosis list, the medication record, and clinical notes/observations. These three domains are present in every researched product. Other familiar domains (allergies, immunizations, vitals as structured flowsheets) are near-universal additions, not definitional: at least one mature open-source reference implementation shipped with its allergies and immunizations modules still immature or under rework while remaining unambiguously an EMR.
- **Encounter/visit as the organizing unit** — care is documented in the context of an encounter or visit; observations, orders, and notes attach to it. The encounter is what turns a pile of data into a record of care delivered at a time, by someone, for a reason. Without it, the system is a registry or data warehouse, not a working record.
- **Authenticated, attributed documentation under role-restricted access** — users sign in; entries carry the identity of their author and a timestamp; what a user may see and do depends on their role. This is the medico-legal character of the record: it is the legal documentation of care, so authorship and access are structural, not features.

### Capabilities Shared by Mature Products

A typical modern EHR carries most of these capabilities. They are not what makes the product an EHR, but they make it practical.

- **Allergy / intolerance list** — near-universal chart domain, and the anchor for prescribing safety checks where supported.
- **Immunization record** — vaccination history as structured data.
- **Vitals & measurements** — structured observations (e.g., blood pressure, temperature, weight) with trend views.
- **Order entry and the results loop** — recording requests for medications, laboratory tests, imaging, referrals, procedures; results and reports flow back into the chart for review. Medication ordering is the most universal form; broader order sets vary by product and setting, and in some deployments laboratory or imaging orders are handled by departmental systems whose results still land in the chart.
- **Basic clinical decision support** — configurable reminders, alerts, and quality-measure calculations built on the recorded data.
- **Structured documentation tooling** — note templates, configurable observation forms, and specialty or program-specific forms.
- **Patient search with duplicate awareness** — finding the right patient and surfacing similar existing records, because duplicate charts are a real clinical risk.
- **Work lists / queues** — visit lists, flow boards, and service queues that tell staff who is waiting, who is next, and what is pending.
- **Reporting & quality measurement** — aggregate views over the recorded clinical data (encounters, diagnoses, measures, program indicators).
- **Audit trail of record access** — recording who accessed or changed what; regulation-driven in many markets and implemented to different depths across products.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. The Variants section below enumerates how specific implementations realize each concept.

```text
Concept:            Patient identity
Implementations:    internal patient ID, national/program health number,
                    name+DOB matching, master person indexes

Concept:            Clinical data domains
Implementations:    fixed relational tables, entity-attribute-value storage
                    driven by a concept dictionary, hybrid

Concept:            Terminology binding
Implementations:    ICD, SNOMED CT, LOINC, RxNorm, CPT/HCPCS, local dictionaries

Concept:            Encounter documentation
Implementations:    structured forms, template-driven notes, free-text notes,
                    configurable observation forms

Concept:            Orders & results
Implementations:    in-EHR order entry, departmental systems (LIS/RIS/PACS)
                    feeding results back, scanned/document results
```

A reader who only knows one implementation (e.g., a large certified US platform) should still be able to recognize a small-practice open-source EMR or a program-oriented record system from the Core Model alone.

## How It Works

The EHR's work moves through a repeating clinical loop around the chart. There is no single linear pipeline; the loop below is the defining interaction pattern.

### Register and identify the patient

```text
Search for an existing patient (with duplicate-record awareness)
→ if none: register the patient (demographics, identifiers)
→ a chart comes into existence
```

Registration is the gate to everything else: no chart, no documentation. Mature products invest heavily in helping staff distinguish similar patients, because documenting on the wrong chart is a safety event.

### Bring the patient into an encounter context

```text
Schedule or queue the patient (where scheduling is in scope)
→ check in / start the visit
→ the encounter becomes the active documentation context
```

In settings without integrated scheduling, the encounter is started directly at the point of care. The encounter is the container that the following steps attach to.

### Review the chart

```text
Open the patient chart/dashboard
→ scan problems, medications, allergies, recent results, recent notes
→ trends and historical views where structured data exists
```

Review precedes action: the chart is consulted before it is extended.

### Document the encounter

```text
Record vitals and observations (often by nursing/triage staff first)
→ capture history and findings via forms or a note
→ record or update diagnoses
→ the documentation accumulates in the chart, attributed to its authors
```

Documentation is the medico-legal heart of the product. Entries are attributed and timestamped; corrections are handled as amendments or invalidations rather than silent deletions (explicitly so in products whose data model voids clinical data instead of deleting it).

### Order and prescribe

```text
Create orders (medications; where supported: labs, imaging, referrals, procedures)
→ medication orders carry drug, dose, route, frequency, instructions
→ safety checks where supported (allergies, reminders, rules)
→ orders become visible to the people who fulfill them
```

In some deployments the order is fulfilled inside the same system (in-house dispensing, in-house lab); in others it crosses to a pharmacy or a departmental system, and the **result** returns to the chart.

### Receive and review results

```text
Results/reports arrive (discrete values, reports, images)
→ they attach to the patient's chart (often against the originating order)
→ the ordering clinician reviews them
→ review may trigger new orders or a diagnosis update — the loop repeats
```

This order → result → review loop is the operational engine of the EHR. It may run entirely inside one product or span the EHR plus departmental systems; the chart is where the loop closes either way.

### Close the encounter and continue longitudinally

```text
Documentation for the visit is completed (finalization/sign-off steps vary by product)
→ the encounter becomes part of the permanent chart
→ the next encounter starts from everything recorded before it
```

The chart is longitudinal: each encounter inherits the whole history. Reporting and quality measurement run continuously over the accumulated record.

### Core vs Common vs Optional

**Defining core** — without these, not an EHR:

- identified patient as record anchor
- longitudinal chart with problems, medications, notes/observations
- encounter-based documentation
- authenticated, attributed, role-restricted access

**Common mature structure** — present in most modern products:

- allergies, immunizations, structured vitals
- order entry + results review loop
- basic decision support
- structured documentation tooling
- duplicate-aware patient search
- work lists / queues
- reporting & quality measurement
- audit trail

**Variant / optional** — depends on market, setting, regulation, scale:

- scheduling & front-office operations
- billing / revenue cycle
- patient portal
- e-prescribing network transmission
- interoperability posture (FHIR, document exchange, HIE, PACS integration)
- deployment model (self-hosted, hosted, offline-capable)
- regulatory certification context
- care-setting specialization

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Patient search / registration

The entry surface for creating and finding charts.

- search results with identifying attributes; similar-patient comparison to avoid duplicates
- registration form: demographics, identifiers, contact information
- primary actions: search, register new patient, open an existing chart

### Patient chart / dashboard

The clinician's home surface for one patient — the summary of the longitudinal record.

- configurable summary of problems, medications, allergies, vitals, recent results, recent notes, program/specialty views
- primary actions: open a domain (problems, meds, results…), start documentation, place an order

### Encounter / documentation surface

Where the visit's clinical content is captured.

- structured forms and note editors (observations, history, findings, diagnoses)
- previously recorded data recallable for review and update
- primary actions: fill/complete forms, write or amend notes, record diagnoses

### Order entry

Where requests for treatment and investigation are recorded.

- medication order composition (drug, dose, route, frequency, instructions), often with search over a drug formulary and reusable regimen templates
- order sets for labs, imaging, referrals where supported
- primary actions: create order, revise, stop/discontinue, refill

### Results review

Where returning data is read.

- discrete result views with trends and reference ranges; report and image viewers where integrated
- primary actions: review, filter by domain/date, act on abnormal findings (new order, diagnosis update)

### Work lists / queues

The operational surface for visit flow.

- waiting/active visit lists, task and result-pending lists
- primary actions: pick up next patient, update visit status, hand off

### Reporting / administration

Aggregate and configuration surfaces.

- reports over encounters, diagnoses, measures, program indicators
- user/role/privilege administration; form, template, and terminology configuration

### Patient portal (where present)

A patient-facing companion surface (bundled module or separate product) for viewing record data, messaging, and appointments. It reads from and writes into the record but is not the record itself.

## Important Rules / Behaviors

### The record is medico-legal

Entries are attributed to a named author with a timestamp. The chart is the legal documentation of care — which is why attribution and access control are structural, and why corrections are typically handled as amendments or invalidations rather than silent deletion. In at least one well-documented open-source data model, clinical data is explicitly *voided* (invalidated, retained) while configuration metadata is *retired*; deletion is not the normal way data leaves the record.

### Access is role-restricted

What a user may see and do follows from their role. Permissions are typically fine-grained (action-level privileges such as adding or updating records, grouped into roles, sometimes with inheritance). This is a structural property of the Type, not an enterprise add-on: even small-practice products ship per-user access controls.

### The chart is longitudinal and cumulative

Each encounter starts from the whole prior history. Nothing "expires" out of the chart in normal operation; the record grows over the patient's lifetime with the organization.

### Patient identity is a safety surface

Duplicate or mismatched charts are a clinical hazard. Patient search therefore behaves as both a lookup tool and a safety check, surfacing similar existing records before a new chart is created.

### Orders and results form a closed loop

An order exists to be fulfilled and answered. Results attach back to the chart (often against the originating order), and unreviewed results are an operational liability — which is why result-pending lists and review workflows are common structure.

### Terminology binding is what makes data computable

Diagnoses, tests, and drugs are recorded against coded terminologies (disease classifications, clinical terminologies, lab observation codes, drug vocabularies), often via an internal concept dictionary mapped to external standards. This binding is what enables decision support, reporting, and interoperability — and it is why record systems invest in dictionary/terminology configuration surfaces.

### Documentation depth varies by role and setting

The same encounter may be documented across several roles (triage observations, clinical findings, prescriptions). What each role may document is governed by the same role-restriction rules that govern visibility.

## Variants

The EHR Type is implemented in many shapes. Common variants:

- **Ambulatory / practice EHR** — encounter-driven, often bundled with scheduling and billing; the classic small/mid-practice shape.
- **Acute / hospital EHR** — inpatient stays, continuous nursing documentation, medication administration, and deeper departmental integration; usually part of a wider platform suite.
- **Program / disease-oriented record systems** — organized around care programs (e.g., HIV, TB, NCD follow-up) with program enrollment and indicator reporting; common in global public health deployments.
- **Low-resource / offline-capable deployments** — on-site hosting, offline operation, paper-printable outputs, minimal training surfaces.
- **Certified-suite deployments (US-style)** — regulatory certification, quality-measure reporting, e-prescribing networks, integrated revenue cycle, patient portals.
- **Setting-specific records** — behavioral health, long-term care, home health: same core model with setting-specific documentation and regulatory overlays (the directory carries separate leaves for some of these; they are best understood as setting variants of this Type).

A variant remains a **Variant** unless it changes the core users, objects, or rules so much that the Core Model no longer applies.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Practice Management System | adjacent, often bundled | owns scheduling, front-office registration operations, billing/claims; no clinical chart. Remove clinical documentation from an EHR bundle and what remains is PM. |
| Patient Portal | companion surface | patient-facing view into the record; the EHR is the clinician-facing system of record. Vendors ship portals as separate products or bundled modules. |
| Clinical Documentation Platform | capability / feeder | produces documentation content (templates, scribes); the EHR is the system of record that holds and governs it. |
| CPOE / Clinical Order Management | capability | order entry is a standard capability inside the EHR; standalone order-entry products exist in some markets. |
| Clinical Decision Support System | capability | decision rules operate on EHR data; in the researched sample CDS operates as a standard capability of the EHR, with standalone CDS as a niche. |
| Electronic Prescribing | capability / variant | recording medication orders is a standard capability; transmission to external pharmacies is a regional network capability. |
| Medication Management Platform | adjacent | pharmacy-side medication lifecycle; the EHR holds the patient's medication record and orders. |
| LIS / RIS / PACS | departmental systems | run laboratory/imaging workflows; their results and reports flow into the chart. The EHR holds results; it does not run the modality or the lab. |
| Hospital Management System | broader suite | administrative operations (registration, billing, inventory, pharmacy stock) around the clinical record; the EHR is the clinical core inside such suites. |
| Health Information Exchange / HIE | infrastructure | moves records between organizations; the EHR is where a record lives and is used. |
| Telehealth Platform | visit modality | conducts remote visits; the resulting documentation lives in the EHR. |
| Population Health Management | analytical layer | aggregates across charts for panels and programs; the EHR is the per-patient record. |

The most important boundary is with **Practice Management**: the two are so often bundled that "EHR" is colloquially used for the whole bundle. Structurally, the clinical chart is the EHR; scheduling and billing are adjacent operations that may or may not share the deployment.

## Representative Products

- **OpenEMR** — free open-source EHR + practice management for ambulatory practices; ONC-certified; fully public documentation.
- **OpenMRS** — open-source medical record system built by a global community; widely deployed in program-oriented and low-resource settings; fully public documentation.
- **Bahmni** — open-source EMR & hospital system for low-resource settings, composed from OpenMRS (records), Odoo (billing/inventory), OpenELIS (lab), and PACS integration; fully public documentation.
- **Oracle Health (Cerner Millennium)** — commercial platform suite for large health systems; public documentation index only (detailed docs login-gated); included as a market anchor and for its product-taxonomy boundary evidence.
- **Epic** — widely referenced acute-care EHR platform; public operational documentation was not accessible during research; included as a market anchor only, with no product-specific claims made.

The Core Model was checked against open-source, program-oriented, and low-resource samples (OpenMRS, Bahmni, OpenEMR) specifically to avoid defining the Type by the current US certified-suite pattern.

## Sources

Research date: **2026-09-06**

- OpenEMR Project Wiki — Features: https://www.open-emr.org/wiki/index.php/OpenEMR_Features
- OpenMRS Documentation — Technical Overview: https://openmrs.atlassian.net/wiki/spaces/docs/pages/25476856/Technical+Overview
- OpenMRS Documentation — Data Model: https://openmrs.atlassian.net/wiki/spaces/docs/pages/25477157/Data+Model
- OpenMRS Documentation — EMR Features: https://openmrs.atlassian.net/wiki/spaces/docs/pages/26938068/OpenMRS+EMR+Features
- OpenMRS: https://openmrs.org/
- Bahmni: https://bahmni.org/ , https://bahmni.org/clinical-services/
- Oracle Health documentation index: https://docs.oracle.com/en/industries/healthcare/index.html
- ONC Health IT (context only): https://www.healthit.gov/

> Sourcing limitation: Epic (`open.epic.com`, `www.epic.com`), athenahealth (`docs.athenahealth.com`, `www.athenahealth.com`), and Practice Fusion (`help.practicefusion.com`) were not reachable from the research environment on 2026-09-06; ONC's EHR definition pages returned 404. No product-specific operational claims are made for those vendors, and no precise operational facts (numeric limits, defaults, timings) appear in this document. Detailed evidence and per-product observations are recorded in the paired Research Notes.
