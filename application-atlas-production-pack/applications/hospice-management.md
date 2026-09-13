# Hospice Management

## Overview

A **Hospice Management** application is a hospice provider's system of record for delivering and operating end-of-life care. It holds the terminally ill patient's comfort-focused clinical record, organizes care as an admitted episode that normally ends in a recorded death, coordinates an interdisciplinary team around one shared plan of care, keeps the family inside the care unit with support continuing after the patient dies, and converts documented care into payer revenue and quality/compliance artifacts.

The defining structure is small:

```text
Terminally ill patient of record (comfort-focused care)
└── Admitted end-of-life episode
    │   (authorizing admission → periodic re-authorization → discharge,
    │    most often by death)
    └── Interdisciplinary team loop around a shared plan of care
        ├── Family as part of the care unit
        │   (support continues after death — bereavement)
        └── Revenue-and-compliance loop
            (per-diem/claims billing + quality reporting)
```

Everything else commonly associated with hospice software — mobile point-of-care charting, predictive decline analytics, caregiver portals, volunteer hour tracking, US benefit machinery — is widespread in current products but is not what makes the product a hospice system. Older, non-US, and paper-era hospice programs fit the same definition without any of those specifics.

When the comfort orientation, the death-bounded episode, or the family/bereavement continuation is removed, the product drifts toward a different Application Type — most importantly the Home Health EHR, whose platform families often sell both lines side by side.

## Users & Context

The operator is a hospice organization — an agency or program whose care team reaches patients where they live (private homes), where they are placed (nursing homes, assisted living), or in dedicated inpatient hospice units.

Primary users — the interdisciplinary care team:

- **hospice nurse / case manager** — admits and assesses patients, manages symptoms, coordinates the case, writes the largest share of visit documentation
- **home health aide** — delivers personal care visits under the plan of care
- **social worker** — psychosocial assessment, family support, community resources
- **spiritual counselor / chaplain** — spiritual assessment and support for patient and family
- **bereavement counselor** — supports the family before and after the death
- **volunteer coordinator and volunteers** — organized volunteer visits and administrative support
- **medical director / attending physician** — certifies eligibility, signs orders, participates in team review

Secondary users — the agency's operating staff:

- **intake / referral coordinator** — manages the referral funnel into admission
- **scheduler** — builds and maintains visit schedules across disciplines and geography
- **clinical supervisor / QA reviewer** — reviews completed documentation, rejects or returns deficient documents
- **biller / revenue-cycle staff** — eligibility checks, claims, appeals
- **administrator / executive** — users, permissions, form configuration, census and financial dashboards

The family caregiver is not a login user in most products but is a first-class *record subject*: caregiver contacts, family teaching, and caregiver experience are part of the chart, and after the death the family continues as a service recipient.

## Core Model

### The Defining Core

Five structures, held together in one system. If any one is removed, the product is no longer recognizable as hospice management:

- **The terminally ill patient of record under comfort-focused care.** A persistent, identified clinical record for a person receiving end-of-life care whose goal is comfort and quality of remaining life — symptom and pain management, psychosocial and spiritual support — not cure or restoration. The comfort orientation is the deepest discriminator: it changes what is assessed (symptoms, beliefs and values, treatment preferences), what is treated, and what "outcome" means. Without it, the record is a restorative-care chart.

- **The admitted end-of-life episode.** Care is organized as a bounded stay in the program: a formal admission gated by eligibility and consent (in the United States, terminal-prognosis certification and election of the hospice benefit), periodic re-authorization/recertification, and a recorded discharge. The discharge is most often a **death discharge** — death is a normal, recorded episode ending, not an error state — but live discharges (revocation, transfer) exist, and readmission is a first-class path back into the program. Without the bounded episode, the system is an unbounded caseload list; without the death-ending frame, it is home health.

- **The interdisciplinary team loop around a shared plan of care.** Care is planned, delivered, and reviewed by a multi-discipline team — nursing, aide, social work, spiritual care, volunteers, physician — working from one shared plan of care that the team formally reviews and updates on a recurring cycle (the interdisciplinary group meeting, "IDG", in US vocabulary). The plan of care is the coordination object; the recurring team review is the coordination rhythm. Without this loop, charting becomes discipline-siloed notes.

- **The family as part of the care unit, with support continuing after death.** Family members and caregivers are recorded as part of the care unit — caregiver contacts, family teaching, caregiver burden and experience — and after the patient's death the family remains a service recipient (bereavement support) while the patient record closes. The record's care unit outlives the patient. No other clinical Application Type holds this structure; it is the clearest structural signature of hospice records.

- **The revenue-and-compliance loop.** The admitted episode and its documented care convert into payer-facing money — per-diem/level-of-care billing, claims, eligibility checks — and into quality/compliance artifacts: assessment-based quality reporting, family-experience surveying, and survey/audit readiness. Without this loop, the product is a documentation tool with no agency business.

### Capabilities Shared by Mature Products

A typical modern hospice product carries most of these capabilities. They are not what makes the product a hospice system, but they make hospice operations practical:

- **Referral intake funnel** — referral sources, conversion tracking, admission packets.
- **Scheduling and assignment** — visit scheduling across disciplines, with continuity of care (how many different caregivers see a patient) tracked as a managed metric.
- **Mobile point-of-care charting** — native apps on phones/tablets, offline fallbacks (downloadable forms or full-chart PDFs, paper forms scanned and auto-filed on reconnect), real-time sync, electronic signing including bulk sign-off.
- **Discipline-specific charting** — templates and checklists per discipline; the researched sample shows dedicated charting for nurses (start-of-care and ongoing visits), aides, social workers, spiritual counselors, bereavement counselors, and volunteers.
- **Medication management** — oriented to palliative and symptom-control medications related to the terminal diagnosis.
- **Physician-order and face-to-face/recertification tracking** — signature workflows and deadline visibility.
- **Facilities master list** — the nursing homes, assisted-living communities, and inpatient units where patients are placed, with per-facility patient placement and room-and-board handling.
- **Document review and correction** — supervisor review, document rejection with comments, amend/correct with a recorded reason.
- **Death and discharge processing** — recorded death discharge, live discharge, readmission.
- **Analytics** — census, length of stay, visits and missed visits, revenue per day, caregiver optimization (right-skill discipline per visit), continuity of care, payment-vulnerability monitoring.
- **Quality reporting** — assessment-based quality measures (including treatment preferences and beliefs/values addressed), family/caregiver experience surveying, QAPI-class improvement loops, survey readiness.
- **Volunteer program management** — volunteer qualification, hours, and visit charting.
- **Timesheets, mileage, and payroll** for field staff.
- **Patient/caregiver portals**, **predictive decline analytics**, and **AI documentation assistance** in current-generation products.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. Specific regimes and products realize each concept differently:

```text
Concept:   Authorizing admission (eligibility + consent)
Implementations:  US election statement + physician certification + benefit periods;
                  other regimes' eligibility criteria and referral/contracting paths

Concept:   Episode economics
Implementations:  US per-diem rates by level of care (e.g. routine home care,
                  continuous home care, general inpatient);
                  other funding and contracting models

Concept:   Quality reporting
Implementations:  US HIS-class item sets, CAHPS-class hospice surveys,
                  accreditation standards; other regimes' quality frameworks

Concept:   Care settings
Implementations:  patient's own home, nursing facility / assisted living
                  (room & board), inpatient hospice unit
```

A reader who only knows one implementation (e.g. only US Medicare-certified hospice) should still be able to recognize older or differently-funded hospice systems from the Core Model.

## How It Works

### Admit a patient into the program

```text
Referral arrives
→ intake screens eligibility and consent requirements
→ admission recorded: face sheet, diagnosis/prognosis, location,
  caregiver contacts, initial assessments
→ plan of care started; disciplines assigned
→ episode begins
```

Admission is the gate that turns a referral into a managed episode. The admission packet and its completeness are themselves audited (admission-audit reporting exists in mature products).

### Deliver care as documented visits and contacts

```text
Scheduler builds the visit schedule across disciplines
→ clinician travels to the patient (home, facility, or unit)
→ documents at the point of care: assessment, interventions,
  symptom status, time in/out attributed to that patient
→ medications and orders updated
→ document submitted, reviewed, and filed in the chart
```

Care is visit- and contact-based. Each entry carries the time of the activity (not the time of charting), attributed to one patient — in facilities, several patients seen in one block are documented as separate, non-overlapping time segments. Field charting works on mobile apps with offline fallbacks; completed documents flow through review before closing.

### Review care as a team, on a cycle

```text
Interdisciplinary team meets on its recurring cycle
→ each discipline's findings reviewed against the plan of care
→ plan of care updated; goals and interventions revised
→ recertification/re-authorization tracked and completed on schedule
```

The team review is the coordination heartbeat. The plan of care is the shared object every discipline reads and writes against; the IDG dashboard in mature products surfaces which patients are due for review and which documentation is outstanding.

### Move the patient across settings and levels of care

```text
Condition or placement changes
→ level of care adjusted (e.g. routine home care ↔ inpatient care)
→ facility placement recorded against the facilities master list
→ billing follows the level of care and setting
```

The episode accommodates transfers between the patient's home, facilities, and inpatient units without ending the episode; the money model follows.

### Close the episode — most often with death

```text
Patient dies (or is revoked/transferred)
→ death discharge recorded; episode closes
→ family transitions to bereavement support
→ bereavement contacts charted against the family record
→ readmission possible if care is later resumed
```

Death discharge is the normal ending and is a first-class recorded event. The family's bereavement support continues under the same system after the patient record closes.

### Convert documented care into money and quality artifacts

```text
Eligibility checked against payer systems
→ claims generated from the episode and documented care
→ claim status and appeals tracked
→ quality measures computed from the same record
→ survey/audit readiness maintained
```

The revenue loop reads the same record the clinicians write. Payment-vulnerability monitoring (length-of-stay patterns, level-of-care mix) and quality reporting draw on the identical data foundation.

### Core vs Common vs Optional

**Defining core** — without these, not hospice management:

- terminally ill patient of record under comfort-focused care
- admitted end-of-life episode with death discharge as the normal ending
- interdisciplinary team loop around a shared plan of care
- family as part of the care unit, with support continuing after death
- revenue-and-compliance loop

**Common mature structure** — present in most modern products:

- referral intake, scheduling with continuity management
- mobile point-of-care charting with offline fallbacks
- discipline-specific charting incl. bereavement and volunteer disciplines
- medication and physician-order management
- facilities master list and room-and-board handling
- document review/rejection and amend-with-reason correction
- analytics (census, LOS, visits, caregiver optimization, payment-vulnerability)
- quality reporting and survey readiness
- volunteer program management, timesheets/payroll
- portals, predictive decline analytics, AI assistance

**Variant / optional** — depends on regime, segment, and packaging:

- US benefit machinery (election, benefit periods, level-of-care set, HIS-class item sets, CAHPS, DDE)
- palliative-care sibling mode
- multi-line platform packaging vs hospice-only standalone
- pediatric programs, non-US funding models

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Patient census / dashboard

The agency's working overview.

- lists active patients with location, level of care, and status flags
- surfaces admissions, discharges, upcoming recertifications, and overdue documentation
- primary actions: open a chart, work the intake funnel, follow up on exceptions

### Patient chart

The center of the product.

- face sheet (identity, diagnosis/prognosis), location and placement, caregiver contacts
- documents organized by discipline and type (assessments, visit notes, orders, medications, care plans)
- primary actions: start a form, complete and sign, review/reject, amend with reason, update care plan and medications

### Documentation forms (web + mobile)

The point-of-care surface.

- discipline-specific templates with required-field marking and free-text narrative
- save-and-resume for unfinished forms; time in/out per patient
- offline fallbacks: downloadable forms/chart, paper forms scanned and auto-filed
- primary actions: fill, sign, submit; scan-and-upload; bulk e-signing from dashboards

### IDG / team review dashboard

The coordination surface.

- patients due for interdisciplinary review, per-discipline documentation status
- plan-of-care updates and recertification tracking
- primary actions: record team review outcomes, update the plan of care, chase outstanding items

### Scheduling

- visit calendar across disciplines and geography; continuity-of-care visibility
- primary actions: schedule, assign, reschedule, record missed visits

### Billing / revenue workspace

- eligibility checks against payer systems, claim generation and status, appeals tracking
- level-of-care and room-and-board handling for facility placements
- primary actions: verify eligibility, generate/submit claims, work denials and appeals

### Reports / analytics

- census, length of stay, visits and missed visits, revenue per day, caregiver optimization, continuity of care
- quality workbooks (outcome measures, treatment preferences, family experience) and payment-vulnerability monitoring
- primary actions: review against budget/quality goals, drill down to patient or branch

### Administration

- users, roles, and permissions; facilities master list; form/template customization; volunteer and staff qualification records

## Important Rules / Behaviors

### The episode is bounded and re-authorized

Care does not continue indefinitely by default. The admission authorizes a defined period; recertification/re-authorization must be completed on schedule for care to continue, and the deadline is tracked by the system.

### Death is a normal, recorded episode ending

The system treats death discharge as the expected closure path — recorded, reported, and analyzed (length-of-stay and discharge-pattern analytics) — alongside live discharges (revocation, transfer) and readmission.

### Documentation is per-discipline and time-attributed

Each visit or contact is documented by the discipline that delivered it, with the time of the activity attributed to that specific patient. Overlapping or split time across patients is prohibited by convention and often by validation.

### Corrections are amend-with-reason, not silent overwrites

Completed, signed documents are corrected through a formal amend/correct flow that records what changed and why; the change history stays visible in the chart. Documents can also be rejected by reviewers with comments and returned for rework.

### The family remains a service recipient after death

Bereavement support is charted against family records after the patient's episode has closed — the only place in clinical software where the record's subjects routinely outlive the patient record.

### Compliance is built into the record

Required fields, validation layers, quality item sets, and admission-audit reporting are part of the chart itself, because hospice agencies operate under survey and audit regimes. The same record feeds quality reporting and payment-vulnerability monitoring.

### Care goals are comfort, not restoration

Assessments and plans are oriented to symptom control, psychosocial and spiritual needs, treatment preferences, and beliefs/values — a different definition of "outcome" than restorative care, reflected throughout the record.

## Variants

- **Multi-line platform vs hospice-only standalone** — the dominant market packaging is a post-acute platform selling home health, hospice, personal care, and facility lines side by side; a distinct pole is the hospice-only EMR built exclusively for hospice (typically serving independent agencies).
- **Home-dominant vs facility-heavy agencies** — agencies differ in the mix of private-home patients, facility placements, and inpatient-unit censuses; the facilities master list and room-and-board machinery matter more in the facility-heavy pole.
- **US benefit regime vs other funding models** — US products carry election/benefit-period, level-of-care, and quality-item-set machinery; non-US hospice and community palliative services organize the same core under different eligibility and funding regimes.
- **Palliative sibling mode** — several products carry a separate palliative-care mode (serious-illness care alongside treatment, visit-coded rather than per-diem), sold as a sibling line by the same vendors.
- **Customer tier** — enterprise chains vs independent agencies (the latter often on flat per-user pricing rather than census-based pricing).
- **Pediatric hospice** — a population variant with its own assessment and family dynamics.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Home Health EHR / Management | closest sibling | restorative/maintenance skilled care in bounded episodes with recertification; no death-ending frame, no IDG machinery, no bereavement continuation; same platform families sell both lines |
| Home Care Agency Management | adjacent | non-skilled personal/support care; service/attendance records, no clinical chart, no plan of care, no death/bereavement frame |
| Palliative care lines | sibling line | comfort-focused care for serious illness alongside treatment; not bounded by terminal prognosis or a death-ending episode; often a separate mode in the same products |
| Skilled Nursing Facility Management / Long-term Care EHR | adjacent | facility-resident care as the operating system of a building; hospice manages patients across settings, with the facility as a placement record |
| Electronic Health Record (generic) | genus | encounter-based clinical record without the program's admission-to-death operations, per-diem billing, bereavement caseload, or survey machinery |
| Healthcare Revenue Cycle Management | adjacent | the money layer across settings; here the revenue loop is one leg fused to the clinical record, not a standalone claims factory |
| Care Coordination Platform | adjacent | manages handoffs and tasks between parties; holds no clinical record of record and no money loop |
| Pastoral Care Management | name-adjacent | congregation-facing ministry administration; chaplains inside hospice are disciplined staff of the care team, not ministry constituents |

The boundary with **Home Health EHR** is the most important one, because the two Types share platform families, visit-based delivery, and episode billing. The structural difference is the care frame: restorative goals with recertification cycles versus comfort goals with an admission that normally ends in death — plus the interdisciplinary review loop and the family/bereavement continuation that only hospice holds. The market itself testifies to the seam: hospice-only vendors exist because agencies found "tweaked home health EMR systems" inadequate for hospice work.

## Representative Products

- Homecare Homebase (HCHB) — workflow-first home-based-care platform; hospice one of its served lines; enterprise pole
- WellSky Hospice & Palliative — enterprise "total agency solution" combining software, analytics, and services
- Netsmart (myUnity Hospice) — post-acute continuum EHR family with hospice as one community
- Hospice Tools — hospice-only EMR and billing for independent agencies; SMB pole

The Core Model was checked against the market's multi-line packaging (three of four sampled vendors bundle hospice with sibling lines) and against the hospice-only pole, to avoid defining the Type by either packaging.

## Sources

Research date: **2026-09-08**

Primary vendor surfaces:

- Homecare Homebase — https://hchb.com/who-we-serve/hospice/ (hospice agency analytics article), https://hchb.com/resources/faqs/
- WellSky — https://wellsky.com/hospice (product page), https://www.wellsky.com/hospice/ (ONC-Health IT certification announcement)
- Netsmart — https://www.ntst.com/ (site navigation incl. hospice community and myUnity descriptions)
- Hospice Tools — https://www.hospicetools.com/ (homepage), https://www.hospicetools.com/hospice-tools-help-guide/ (help-guide index), https://www.hospicetools.com/edocs-faq/ (operational FAQ)

> Sourcing limitation: no vendor help-center screen walkthroughs were readable this pass (Hospice Tools' PDF manuals returned binary content and were used at title/index level only). A major vendor (Axxess) was unreachable and unsampled. US regulatory mechanics are named at concept level only (election, benefit periods, levels of care, quality item sets, surveying); no precise regulatory parameters (periods, rates, timepoints, field lists) are asserted, as the regulator's own documentation was not reachable. Claims calibrated accordingly.

Detailed evidence, product-by-product observations, cross-product comparison, and the historical/market-sample check are recorded in the paired Research Notes.
