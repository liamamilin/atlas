# Long-term Care EHR

## Overview

A **Long-term Care EHR** is the system of record for facilities where people **live** while receiving ongoing care — nursing homes, skilled nursing facilities, assisted living and care homes, rehabilitation and continuing-care settings. It holds each **resident's** complete health-and-care record for the whole of their stay, organizes the facility's work through an assessment → care plan → daily care loop, and captures care as it is delivered, shift by shift, including the administration of medications.

The defining structure is small:

```text
Resident (person living in the facility)
└── Standing record spanning the entire stay (medical + functional + social content)
    └── Assessment → Care Plan → everyday care, continuously re-assessed
        └── Shift-based care documentation, including a Medication Administration Record
```

What makes this a distinct Application Type rather than "an EHR" is the care model it records. A hospital record is organized around episodes of treatment; a long-term care record is organized around a person's standing residency — often lasting months or years — during which the facility's staff deliver planned, recurring, multidisciplinary care as part of everyday life. When the organizing subject becomes a per-visit patient in their own home, the product is drifting toward Home Health; when it becomes program-shaped end-of-life care, toward Hospice Management; when the clinical record disappears and only services and operations remain, toward Senior Living operations software.

## Users & Context

The primary users are the facility's care staff, who work with the system continuously rather than occasionally:

- **nurses** — assess residents, carry out and document clinical care, manage treatments, and administer medications in scheduled rounds
- **care assistants / carers** — deliver and document most everyday personal care (washing, dressing, eating, mobility), usually at the bedside with handheld devices
- **assessment / care-plan coordinators** — run structured assessments and keep care plans current

Secondary users:

- **prescribers and visiting practitioners** — review residents, sign off orders and plans, often remotely
- **therapists, dietitians, social services and activities staff** — document their disciplines against the same resident record
- **shift leads and the director of nursing** — monitor the floor in real time: what has been done, what is late, what needs escalation
- **administrators and billing staff** — manage census, payer programs, and resident financial matters
- **quality/compliance staff** — assemble evidence for regulators and internal audits

The work environment is facility-based and continuous: the record must be current around the clock because care is continuous. Documentation happens at the point of care — in rooms, corridors, medication rooms — typically on shared mobile devices and workstations, not after the fact in an office.

## Core Model

### The resident record

The center of the system is the **resident**: an individually identified person who has been admitted to live in the facility. Unlike a clinic's patient, the resident is a *standing* member of the operation — the system tracks them across rooms, units and care levels for the duration of their stay, which may span years. The record deliberately combines two kinds of content that hospital records usually keep apart:

- **medical content** — diagnoses, allergies, orders, medications, vitals and weights, treatments, immunizations, lab and imaging results
- **functional and social content** — personal-care needs, cognition and behavior, risk factors (falls, skin, nutrition, swallowing), preferences, family contacts, activities

Both kinds of content are first-class. A resident's diet texture, mobility level, and preference for a shower over a bath are as operational as their medication list — care staff act on them every shift.

### The assessment → care plan loop

The organizing mechanism of the whole application is a repeating cycle:

```text
Admission / change in condition
→ structured assessment of needs and risks
   (functional status, cognition, skin, nutrition, mobility, behavior …)
→ care plan: the resident's problems/needs
   each with goals and planned interventions, assigned to disciplines
→ care delivered and documented against the plan, every shift
→ reassessment on schedule or on any significant change
→ plan updated …
```

The **care plan** is the resident's operational contract: it converts assessed needs into directed, schedulable everyday care. It is multidisciplinary by construction — nursing, personal care, therapy, diet, social and activity interventions live on one plan. In the US market this loop is tightly coupled to regulator-defined assessment instruments (the Minimum Data Set tradition); in other jurisdictions the same loop exists with different or lighter instruments. The loop itself is the defining structure; the specific instruments are regional realizations.

### Medication orders and the administration record

Medication has its own loop inside the record:

```text
Prescriber order (or pharmacy-reconciled order)
→ scheduled on the Medication Administration Record (MAR/eMAR)
→ medication pass: staff administer doses in scheduled rounds,
   verifying right drug / dose / route / time / person
→ each administration (or omission: refused, held, unavailable) is documented
→ stock and reorder signals flow to the supplying pharmacy
```

Mature products realize this as an integrated or tightly coupled eMAR with barcode verification, resident photographs, interaction warnings, and pass-completion dashboards. The paper-era MAR/TAR binder it replaces was already part of the nursing home record — the medication administration record is part of the Type, while the specific technology (barcode, photos) is a modern implementation.

### Stay, census and the facility

The resident sits in a facility context that the system maintains as a live picture:

- **census and stay** — admissions, room/bed assignment, transfers between units, discharges, returns from hospital, leave of absence
- **units/rooms** — the physical structure care staff work in

This census layer is what connects the record to the facility's business: occupancy, payer coverage, and (in the US) regulatory bed certification and billing all key off the resident's stay. The census machinery is standard in mature products, but it is the record's context, not its substance — a long-term care record without billing or bed management is still recognizable; one without residents, care plans and care documentation is not.

### Structure summary

```text
Facility (units / rooms / beds)
└── Census / Stay  (admission → transfer → discharge)
    └── Resident — standing record
        ├── Assessment  (needs, risks, status)
        ├── Care Plan   (problems → goals → interventions, per discipline)
        ├── Orders      (treatments, medications)
        ├── Medication Administration Record
        ├── Care documentation (shift notes, ADL/personal care, observations, charts)
        └── Results & documents (labs, imaging, referrals, external records)
```

## How It Works

### Admit a resident

```text
Referral arrives (often from a hospital)
→ intake: demographics, history, medications, allergies, payer/coverage
   (mature products import and reconcile much of this from the referral source)
→ admission: assign room/bed, open the standing record
→ initial assessments within the facility's required schedule
→ first care plan established
→ orders entered; medications scheduled on the MAR
```

The intake moment is a defining interaction with the outside world: the system pulls in the hospital's discharge information (documents, medication lists, diagnoses), identifies active medication orders that carry over, and lets staff accept, change or continue them — because what a new resident is already taking is directly relevant to their first days in the building.

### Run the assessment → plan → care cycle

```text
Assessment coordinator completes structured assessments
   (on admission, on schedule, and whenever condition changes)
→ findings generate/refresh care-plan problems and interventions
→ interventions appear in each discipline's work
→ staff deliver care and document at the point of care during the shift
→ coordinators and managers review completion and quality
→ reassessment closes the loop
```

This is the interaction loop the application exists for. It is continuous rather than transactional: on any given day, every resident has plan-driven care being delivered and documented, and the plan is only current if assessment keeps pace with the resident's actual condition.

### The daily care cycle (a shift)

```text
Staff start shift → see their residents and what is due
→ deliver care: personal care, treatments, observations, vital signs
→ document at the bedside/room as care happens
   (prompt-driven entries; abnormal values flagged)
→ handover: the record shows what was done and what is outstanding
```

Point-of-care documentation is the norm, not an aspiration — the record is expected to reflect care as it is given, and managers treat the currency of documentation itself as a monitored signal.

### The medication pass

```text
Scheduled administration round opens (by resident and pass time)
→ for each order due: verify the five administration checks
   (barcode/photograph aids; warnings surface interactions)
→ give or withhold (refused / held / unavailable — each documented)
→ complete the pass; supervisors see late or missed passes in real time
→ pharmacy loop: reorder signals, order changes flow back
```

### Discharge and transfer

```text
Resident leaves (hospital transfer, another facility, death)
→ final documentation and summaries produced for the receiving provider
→ census updated; record retained as the facility's legal record
→ (in the US) stay-level billing and assessment reporting conclude
```

### Capability tiers

**Defining core** — without these, it is not a long-term care EHR:

- resident standing record spanning the whole stay, combining medical and functional/social content
- assessment → care plan → everyday care loop, with reassessment
- shift-based point-of-care care documentation
- medication orders with an administration record
- facility context: admission and census as the record's container

**Standard capabilities** — present in most mature products:

- census/occupancy and bed/room management, leave-of-absence handling
- regulatory assessment instruments maintained as content, with submission to regulators where the regime requires (US: MDS-class)
- eMAR with order-verification aids (barcode scanning and resident photographs are common implementations) and pass-completion dashboards
- interoperability intake from hospitals/referral sources with reconciliation; pharmacy order exchange; lab/imaging results
- oversight dashboards (late/missed care and medications), incident reporting, audit trails
- billing/revenue-cycle machinery coupled to census and payer programs (US-centric)
- practitioner remote engagement and e-prescribing
- group/chain-level reporting across multiple homes

**Optional / variant** — depends on segment, regime, and vendor packaging:

- resident trust-fund/personal-allowances accounting
- therapy, nutrition/dining, activities/wellbeing modules
- AI-driven risk detection and predictive analytics
- hospice or assisted-living flavors of the same record
- standalone eMAR products serving smaller settings

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Census / resident list

The floor-level picture of who lives where.

- purpose: orient every user to the current population
- typical information: resident name/photo, room/bed, unit, payer or care level, alerts (falls, infection, skin)
- primary actions: open a resident chart, admit, transfer, discharge

### Resident chart

The standing record for one person.

- typical information: demographics, diagnoses, allergies, orders, MAR, care plan, assessments, notes, results, documents
- primary actions: document care, review/refresh the care plan, enter or act on orders, review history

### Care plan workspace

Where assessment output becomes directed care.

- typical information: problems/needs, goals, interventions by discipline, review dates, completion status
- primary actions: update from an assessment, assign interventions, mark progress, schedule review

### Point-of-care documentation app

The handheld/bedside surface carers and nurses live in during a shift.

- typical information: today's residents, due care, prompts for observations and ADLs
- primary actions: record care as delivered, capture vitals/weights, flag changes in condition

### eMAR / medication pass screen

The administration surface for scheduled rounds.

- typical information: due medications per resident and pass time, warnings, administration status
- primary actions: administer (with verification), document refusal/hold, see missed/late doses

### Assessment workspace

The structured-assessment surface (strongest in the US variant).

- typical information: assessment instruments in progress, due dates, submission status
- primary actions: complete sections, validate, submit to the regulator where applicable

### Oversight dashboards

Management surfaces across the home or group.

- typical information: care completion, late/missed medications, incidents, occupancy, quality measures
- primary actions: drill down to a resident or task, run reports, assemble inspection/audit evidence

## Important Rules / Behaviors

### The record is a legal record

Everything documented — care given, medications administered or withheld, assessments, order changes — is part of the facility's legal record and is retained after discharge. Entries carry authorship and time; corrections and late entries are recorded as such rather than erased. Products are expected to support audits and regulator inspections directly from the record.

### Medication administration is rule-bound

The administration loop enforces the discipline of the medication record: a dose is documented as given, refused, held or unavailable — never silently skipped. Verification against the order (drug, dose, route, time, person) is built into the pass workflow, and supporting documentation (for example, vitals or notes required with certain medications) is prompted rather than left to memory.

### The care plan drives, and only current assessments keep it honest

Care is supposed to trace back to an assessed need. A change in a resident's condition is both a documentation event and a reassessment trigger — products structure the record so that the plan, the assessments and the daily documentation form one continuous story rather than three silos.

### Census changes ripple

Admission, transfer, discharge and leave-of-absence events affect occupancy, payer status, assessment schedules and (in the US) billing. The clinical record and the facility's business are coupled through the stay, which is why census accuracy is treated as a shared clinical/administrative responsibility.

### Roles follow discipline and seniority

Permissions mirror the facility: care assistants document personal care but do not administer medications; nurses administer and assess; coordinators manage plans and assessments; administrators see business surfaces. Because a large share of daily users are non-clinical carers, the point-of-care surfaces are deliberately simple and prompt-driven.

### Outside data must be reconciled, not just received

Information arriving from hospitals, pharmacies and GP systems (demographics, medications, allergies, diagnoses, documents) is reconciled into the resident record rather than filed alongside it — in documented implementations this includes surfacing active medication orders for continuation or change and avoiding duplicate records — because the record remains the facility's authoritative document for the resident's care.

## Variants

- **Skilled nursing / post-acute pole** — short-stay rehabilitation after hospital care, tightly coupled to payer programs and assessment-driven reimbursement (dominant in the US market).
- **Long-stay custodial pole** — nursing homes and residential care where the stay is indefinite and the record emphasizes daily living, risks and quality of life.
- **Assisted living / senior living pole** — lighter clinical depth, more wellness and service coordination; several vendors package it as a sibling product to their nursing EHR.
- **Regional/regime variants** — the US realization (MDS-class assessments, payer claims, trust funds) vs the UK "digital social care record" realization (care plans, daily notes, eMAR, CQC inspection evidence, GP-record access) vs other jurisdictions; the same core structure under all of them.
- **Packaging variants** — a dedicated long-term care suite from a specialist vendor; a multi-setting care-continuum suite; or a long-term care setting inside a hospital EHR platform.
- **Scale variants** — single homes vs large chains (group-level reporting and standardization across homes), and lightweight eMAR-first products for smaller settings.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Electronic Health Record / EHR | same family, different care model | organized around episodic encounters/treatment for patients; the LTC EHR is organized around a resident's standing life in the facility and the daily-care loop |
| Home Health EHR / Management | adjacent post-acute | care delivered per visit in the person's own home; no facility census/bed context; different assessment and billing machinery |
| Hospice Management | adjacent program | centers on an end-of-life care program (IDT, plan of care, bereavement) across settings rather than a facility's standing population |
| Skilled Nursing Facility Management | sibling leaf, heavy overlap | the facility's operational/administrative bundle (finance, census operations); in the US market usually sold as the same platform that carries the LTC EHR — the seam is the clinical record of record vs the business/operations layer |
| Care Plan Management | capability inside this Type | care planning is a defining structure of the LTC record, not a standalone application here |
| Nursing Information System | overlapping heritage | nursing documentation is one layer of the LTC record; the LTC EHR spans the whole facility and the whole resident, not nursing alone |
| Senior Living operations software | adjacent when clinical content drops | marketing/move-in/dining/retail services for senior communities without a care record of record |

The most consequential boundary is with the generic EHR: when a hospital EHR platform serves long-term care, it must still carry the resident standing record, the care-plan loop and the medication administration machinery — confirming that these, not vendor branding, are what make the Type.

## Representative Products

- **PointClickCare** — EHR for Skilled Nursing Facilities (North America; dedicated long-term care suite with a large integration ecosystem)
- **MatrixCare (ResMed)** — Skilled Nursing Software within a multi-setting care-continuum suite
- **MEDITECH Expanse (Post-Acute care setting)** — long-term care delivered as a setting inside an acute-care EHR platform
- **Person Centred Software — mCare** — UK "digital social care record" for care homes (regional pole without US assessment/billing machinery)

The defining core was checked against the UK regional pole and against the paper-era nursing home chart (admission record, orders, care plans, ADL flow sheets, MAR/TAR binder) to avoid over-fitting the definition to the current US regulatory implementation.

## Sources

Research date: **2026-09-08**

- PointClickCare — "EHR for Skilled Nursing Facilities" — https://pointclickcare.com/products/skilled-nursing/
- PointClickCare — "Electronic Medication Administration Record (eMAR)" — https://pointclickcare.com/products/emar/
- MatrixCare — "Skilled nursing software" — https://www.matrixcare.com/skilled-nursing-software/
- MatrixCare — "Interoperability for post-acute and long-term care" — https://www.matrixcare.com/skilled-nursing-interoperability/
- MEDITECH — "Post-Acute Care" — https://ehr.meditech.com/ehr-solutions/post-acute
- Person Centred Software — "Digital Care Planning System (mCare)" — https://personcentredsoftware.com/products/digital-care-system
- Person Centred Software — home page — https://personcentredsoftware.com/

> Sourcing limitation: vendor help centers (operational manuals) were not reachable from the research environment on 2026-09-08 (login-gated), and one acute-EHR vendor's product pages were blocked (HTTP 403), so the acute-EHR-embedded pole is evidenced by a single vendor. All product observations above come from official product pages fetched on the research date. Precise operational details (assessment windows, numeric limits, submission schedules, plan-specific capabilities) are intentionally not stated; such details remain in the paired Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison, and the historical / regional breadth check are recorded in the paired Research Notes.
