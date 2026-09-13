# Home Infusion Management

## Overview

A **Home Infusion Management** application is the system of record for a home infusion therapy provider — typically a licensed infusion pharmacy — running its therapy-delivery business: taking physician referrals for infusion therapy, verifying coverage, holding the patient's therapy plan of record, preparing and dispensing each dose, coordinating delivery of drugs and supplies to the home, arranging nursing administration and clinical monitoring, and billing payers for the therapy delivered.

Home infusion itself is the administration of medication through a needle or catheter outside a hospital or medical facility — most commonly in the patient's home, sometimes in the provider's own infusion suite. The provider behind it is, in the industry's own definition, a pharmacy: a state-licensed, accredited pharmacy specializing in infusion therapies, staffed by pharmacists and nurses who together coordinate coverage verification, therapy planning, sterile preparation and delivery, nursing services, education, lab monitoring, around-the-clock support, and coordination with the prescribing physician.

The software exists because that business is unusually coordination-heavy: a single course of therapy binds a prescriber, a payer, a compounding pharmacy, a courier, an infusion nurse, and a patient who must all land on the same day, repeatedly, for weeks. The application's defining core is small:

```text
Referral / coverage intake
└── Home infusion therapy of record (the physician-ordered plan)
    └── Dose preparation & dispense (the pharmacy's production)
        └── Home delivery & administration coordination
            └── Therapy-to-revenue loop (billing & collection)
```

Everything commonly associated with modern products — sterile-compounding workflow modules, infusion-pump fleets, electronic visit verification, patient engagement apps, AI triage, accreditation documentation — is widespread in current products but is not what makes the application what it is. A paper-era infusion pharmacy running the same four structures on paper, phone, and fax was still running home infusion.

## Users & Context

The customer of this software is a **home infusion therapy provider**: an independent locally owned infusion pharmacy, a regional or national home-infusion company, a hospital-affiliated or health-system pharmacy offering home infusion, or a specialty pharmacy with an infusion line. The provider's staff all work in one system across several environments — the pharmacy (intake, clinical review, compounding), the warehouse and courier fleet, the field (nurses in patients' homes), and the back office (billing).

Primary users and their relationship to the system:

- **Intake / benefits staff** — capture referrals from prescribers and hospital discharge planners, verify insurance coverage, run benefits investigations, and manage prior authorizations before therapy starts.
- **Pharmacists** — clinically review each prescription, design and adjust the therapy plan, verify doses, and oversee preparation; they are the clinical authority inside the system.
- **Pharmacy technicians** — prepare and fill doses under the pharmacist's verification, work the task-based fulfillment queues.
- **Delivery / shipping staff** — schedule and execute delivery of doses, supplies, and equipment to homes, with proof of delivery.
- **Infusion nurses** (employed by the provider or working for a contracted nursing agency) — perform first-dose teaching and ongoing home visits; document care at the point of care.
- **Billing / collections staff** — turn delivered therapy into claims and payments, work denials and receivables.

Secondary participants:

- **The patient and caregiver** — recipients of education, delivery confirmations, and secure communication; in many therapies, trained self-administrators.
- **The referring prescriber / hospital discharge planner** — external; sends referrals and receives status updates.
- **Contracted nursing agencies** — external; receive visit referrals and return documentation.

The work environment is deadline-driven and continuity-critical: infusion therapy has no grace period, so the system's job is to keep doses, deliveries, visits, and payments moving without interruption.

## Core Model

### The Defining Core

Four structures, held jointly. Remove any one and the product stops being recognizable as home infusion management.

**1. The home infusion therapy of record.** The anchor object: a physician-ordered parenteral medication therapy for an identified patient, designed as a plan — drug, dose, schedule, duration, administration route and device — to be administered outside a facility. A therapy is a *course*, not a single fill: a course of daily IV antibiotics for weeks, nightly parenteral nutrition, monthly immunoglobulin infusions, factor replacement on a prophylaxis schedule. The therapy plan is what the pharmacy designs, what the nurse teaches to, what labs are reviewed against, and what billing attaches to. Without it, the system is a prescription ledger or a visit scheduler with no therapy to manage.

**2. Dose preparation & dispense.** The provider's pharmacy prepares and dispenses each dose of the therapy — commonly by sterile compounding (parenteral nutrition, factor, chemotherapy, many antibiotics), sometimes by dispensing manufactured products (immunoglobulin, premixed bags). Each dose advances through a task-based fulfillment workflow with pharmacist verification before it leaves the pharmacy. This is the production signature that separates home infusion from nursing-only home services: the provider does not just arrange care, it *makes the medication*. Without it, the system is a home health or nursing-agency tool.

**3. Home delivery & administration coordination.** The provider coordinates getting each dose into the patient's hands and getting it administered. Delivery means courier runs or shipped parcels of drugs, supplies, and (where the therapy requires) infusion devices, with proof of delivery and route management. Administration means infusion nurses — employed or contracted — performing first-dose teaching and ongoing visits, or a patient/caregiver trained to self-administer. The two must be synchronized: the drug and the clinician arrive together, or the dose is missed. Without this leg, the system is a retail, mail-order, or specialty pharmacy.

**4. The therapy-to-revenue loop.** The delivered therapy is billed to payers and the money is tracked to collection. Home infusion reimbursement is distinctive: most commercial plans treat it as a medical service under the *medical benefit*, paying a per diem for clinical services, supplies, and equipment with separate payments for drugs and nursing visits — while other payers and therapies route through the *pharmacy benefit*. The system therefore verifies benefits, obtains and tracks authorizations, generates claims in the right benefit channel, and works denials and receivables against the therapy. Without it, the system is a clinical coordination tool with no business loop.

```text
Referral (prescriber / hospital discharge)
  ↓ captured, benefits verified, authorized
Home infusion therapy of record
  ↓ doses scheduled across the course
Dose preparation & dispense (pharmacy production)
  ↓
Home delivery (drugs + supplies + devices)
  ↓ synchronized with
Administration (nurse visit / trained self-administration)
  ↓ documented, monitored (labs, response)
Therapy-to-revenue loop (per-diem / drug / nursing claims → payment)
  ↺ refills, re-authorization, plan adjustments until discharge
```

### Capabilities Shared by Mature Products

These are widespread in current products and make the core practical, but they do not define the Type:

- **Referral intake funnel** — electronic referral capture (including e-prescribing network feeds), document intake, benefits investigation, and prior-authorization tracking as the gate before the first dose.
- **Task-based fulfillment worklists** — role-shaped queues (intake, pharmacist, technician, billing) that advance each order through defined stages, with backlog and error monitoring.
- **Clinical chart** — per-patient medication profile, care plan, assessments, progress notes, lab tracking, and automated follow-up; the pharmacist's and nurse's shared record of the therapy.
- **Nursing scheduling and point-of-care documentation** — visit scheduling matched to the dose calendar, mobile documentation in the home, and (in US implementations) electronic visit verification.
- **Delivery management** — route planning, courier and carrier integration, real-time tracking, electronic signature and proof of delivery, delivery-visit synchronization.
- **Perpetual inventory** — counted, barcode-tracked stock of drugs, supplies, and equipment across warehouse, pharmacy, and delivery vehicles, with lot and expiry control and controlled-substance accountability.
- **Dual-benefit claims machinery** — adjudication in both pharmacy-benefit and medical-benefit transaction formats, payer-specific rule handling, denial and appeal management, and receivables metrics (days outstanding, aging, cost of goods).
- **Patient engagement surfaces** — secure messaging, on-demand education, e-signatures, delivery tickets, satisfaction surveys, and pre-refill check-ins.
- **Compliance and accreditation documentation** — sterile-compounding documentation, labels, controlled-substance reporting, and survey-ready records, because commercial payers generally require accreditation.
- **Analytics and reporting** — operational and financial dashboards, from workflow throughput to revenue-cycle metrics.

### One Structure, Many Implementations

The core model is conceptual; products realize each leg differently:

```text
Concept:   Therapy of record
Realized as:  prescription + care plan + dose schedule (pharmacy-first products);
              medication management integrated from a separate pharmacy system
              (nursing-side products)

Concept:   Dose preparation
Realized as:  sterile compounding with labels and batch documentation (TPN, factor,
              chemo); dispensing of manufactured products (IVIG, premixes)

Concept:   Administration coordination
Realized as:  employed-nurse scheduling + mobile charting; contracted nursing-agency
              referral networks; patient/caregiver self-administration after teaching

Concept:   Therapy-to-revenue
Realized as:  per-diem medical-benefit claims + separate drug and nursing-visit
              payments; pharmacy-benefit adjudication; outsourced billing services
```

A reader who has only seen one implementation should still be able to recognize the others from the core model.

## How It Works

The application's work moves through one repeating lifecycle — the therapy course — with a dose-level loop inside it.

### Start a therapy

```text
Referral arrives (prescriber, hospital discharge planner, e-prescribing network)
→ intake captures patient, insurance, and clinical information
→ benefits investigation: what does the payer cover, what does the patient owe
→ prior authorization obtained and recorded
→ pharmacist reviews the prescription and designs the therapy plan
→ patient assessment and home assessment confirm the patient is a candidate
→ first dose scheduled: drug, supplies, device, and nurse land together
→ nurse teaches the patient (or caregiver) to self-administer where applicable
```

The referral-to-start window is the provider's competitive battleground — referral sources route to whoever starts therapy fastest — so intake speed and authorization tracking are first-class concerns, not back-office afterthoughts.

### Run the dose loop

For each dose across the course:

```text
Dose due per the therapy schedule
→ pharmacy prepares and verifies the dose (compounded or dispensed)
→ delivery scheduled and routed; supplies and device included
→ nurse visit scheduled in sync (first dose, routine care, site care, blood draws)
→ delivery confirmed; visit documented at the point of care
→ labs and patient status reviewed; plan adjusted if needed
→ charges captured: per diem / drug / nursing visit as the payer model requires
```

The loop repeats daily, weekly, or monthly depending on the therapy, and every pass must leave documentation — payment flows only when the record proves the plan of care was followed.

### Sustain and complete the course

```text
Refills generated from the therapy schedule (with pre-refill patient check-ins)
→ re-authorization before coverage windows close
→ clinical monitoring: labs, response to therapy, adverse reactions
→ plan adjustments routed back through pharmacist review
→ therapy completes or changes → discharge from service, or transfer to another therapy
```

Around the lifecycle sits the 24/7 obligation: patients on infusion therapy are supported around the clock, so after-hours triage — pump alarms, side effects, delivery problems, new referrals — is part of the operating model the system must evidence.

### Core vs Common vs Optional

**Defining core** — without these, not home infusion management:

- home infusion therapy of record (physician-ordered, course-shaped, home-administered)
- dose preparation & dispense by the provider's pharmacy
- home delivery & administration coordination (delivery synchronized with nursing or trained self-administration)
- therapy-to-revenue loop (benefits/authorization → claims → collection against the therapy)

**Common mature structure** — present in most modern products:

- referral intake funnel with benefits investigation and prior authorization
- task-based fulfillment worklists with role views
- clinical chart (medication profile, care plan, assessments, notes, labs, follow-up)
- nursing scheduling + point-of-care documentation
- delivery management with proof of delivery
- perpetual inventory of drugs, supplies, and equipment
- dual-benefit claims adjudication, denials, AR
- patient engagement surfaces
- compliance/accreditation documentation and analytics

**Variant / optional** — depends on therapy mix, business model, regime:

- sterile-compounding depth (batch compounding, IV workflow integration)
- infusion-pump and equipment fleet management (therapy-dependent)
- nursing model (employed vs contracted agency vs self-administration)
- ambulatory infusion suite / infusion-center services alongside home delivery
- therapy specialization (anti-infectives, nutrition support, factor, immunology, oncology, hydration, pain)
- regime machinery (US Medicare home-infusion benefit rules, visit verification, specific accreditation bodies)
- consumer-pay mobile IV services

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Referral / intake worklist

The front door. Lists incoming referrals with their stage (received, benefits pending, authorized, scheduled).

- typical information: patient, referral source, therapy, payer, authorization state, start target
- primary actions: capture referral, request records, run benefits check, initiate prior authorization, accept and schedule

### Patient / therapy chart

The clinical record of one patient's therapy.

- typical information: medication profile, therapy plan, assessments, progress notes, lab results and trends, care-team communications
- primary actions: review and adjust the plan, record assessments and notes, track labs, message the care team, schedule follow-up

### Fulfillment worklists

The pharmacy's production queues.

- typical information: doses due, stage of each order, assignments, warnings and backlogs
- primary actions: advance a dose through preparation and verification, assign tasks, flag errors, print labels and documentation

### Delivery / shipping management

The logistics surface connecting pharmacy and field.

- typical information: deliveries and shipments by day, routes, carrier status, proof-of-delivery state
- primary actions: plan routes, dispatch, confirm delivery, capture signature/photo proof, sync with the nursing visit

### Nursing schedule & point-of-care documentation

The field clinical surface.

- typical information: visit calendar matched to doses, patient list per nurse, visit documentation forms, visit verification
- primary actions: schedule and complete visits, document care in the home, report back to the pharmacy

### Billing / claims / receivables

The money surface.

- typical information: billable therapy days and doses, claim status by payer and benefit type, denials, aging balances
- primary actions: generate and submit claims, post payments, work denials and appeals, collect patient responsibility

### Patient engagement surface

The patient-facing channel (in-app or companion product).

- typical information: schedule and delivery confirmations, education content, surveys, secure messages
- primary actions: confirm deliveries and visits, complete check-ins and assessments, sign forms, ask for help

### Analytics / reporting

Management view across patients, workflow, and money.

- typical information: throughput, backlog, revenue metrics, receivables aging, therapy-mix and outcomes reporting
- primary actions: run and schedule reports, drill into exceptions

## Important Rules / Behaviors

### Therapy continuity is the governing constraint

Infusion therapy has no grace period: a missed delivery, an unanswered door, or a supply gap is an interruption of treatment. The system therefore treats delivery-visit synchronization — drug and clinician arriving together — as a structural requirement, and pre-refill confirmation (has anything changed — hospitalization, dose change, discontinuation?) as a gate before expensive doses ship.

### Authorization gates the start and the continuation

Benefits investigation and prior authorization precede the first dose; re-authorization precedes course extensions. The authorization state is a first-class field on the therapy, and work stalls visibly when it is missing.

### Billing follows the payer's model, and the model varies

The same therapy may bill under a medical benefit (per diem for services, supplies, and equipment, with separate drug and nursing-visit payments) or a pharmacy benefit, depending on payer and therapy. Mature systems adjudicate both transaction types and keep the benefit routing explicit per patient and payer.

### Documentation proves the service

Payment for professional services depends on the record showing that the visit, training, and monitoring occurred as planned. The system's documentation — point-of-care notes, delivery proof, education delivery, time-stamped coordination records — is the provider's audit and accreditation evidence, not just clinical memory.

### The pharmacist is the verification gate

Doses leave the pharmacy only after pharmacist review and verification; plan adjustments (often driven by lab results) route back through pharmacist authorization. The workflow encodes this professional accountability.

### Controlled substances and sterile preparation carry heightened accountability

Controlled-substance dispensing triggers per-state reporting; sterile preparation carries documentation obligations (compounding records, labels, storage conditions) that the system must produce on demand for surveys and audits.

### The 24/7 obligation is structural

Qualified providers furnish professional services around the clock, every day. The system supports and evidences this — on-call routing, after-hours contact capture, and documentation of every response.

## Variants

- **Pharmacy-first home infusion provider** — the dominant form: a licensed infusion pharmacy that produces, delivers, and coordinates nursing (the sampled system-of-record products are built for this pole).
- **Nursing-agency participant** — organizations providing infusion nursing under contract to pharmacies; they run the administration leg (scheduling, point-of-care documentation, visit verification) with pharmacy systems holding production. Tools serving them cover a subset of the core.
- **Infusion-center extension** — providers operating ambulatory infusion suites or centers alongside home delivery; chair-based scheduling and on-site administration join the same therapy object.
- **Therapy-specialized providers** — anti-infective (the largest single therapy class), nutrition support/parenteral nutrition, factor and bleeding disorders, immunoglobulin and immunology, oncology, hydration, pain management; specialization shapes the compounding, nursing, and billing mix.
- **Business-model variants** — independent local pharmacies, regional and national companies, hospital/health-system-affiliated pharmacies, specialty-pharmacy-attached infusion lines.
- **Regime variants** — the US commercial per-diem medical-benefit model dominates the sampled market; Medicare's partial coverage creates distinct billing paths; other countries run home infusion through different service and payment arrangements (not sampled in depth).
- **Consumer-pay mobile IV** — wellness-oriented infusion services without payer billing; the delivery/administration machinery applies, the revenue loop changes shape.
- **Overlay products** — patient-engagement, delivery-logistics, and revenue-cycle services sold alongside the system of record rather than replacing it.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Pharmacy Management System | adjacent; machinery is embedded | PMS manages the dispense transaction at the pharmacy (prescription → fill → dispense of packaged products); home infusion management binds a course of parenteral therapy with production, home delivery, administration coordination, and course-level billing |
| Home Health EHR / Management | adjacent (shares home-visit machinery) | home health delivers skilled nursing/therapy visits under a plan of care with no drug production or dose dispense; remove dose production and delivery from home infusion and it collapses into home health |
| Home Care Agency Management | distant | non-skilled personal/support care; no clinical therapy, no drug production |
| Durable Medical Equipment Management | adjacent (same platform families) | DME's billable product is the equipment itself (rental/sale, custody movement); in home infusion the drug therapy is the anchor and pumps/supplies are subordinate delivery equipment |
| Dialysis Center Management | adjacent (both are therapy-delivery operations) | dialysis manages prescribed treatment sessions at a station (or home dialysis with patient-side capture); the dose object is a dialysis treatment, not a dispensed/compounded medication |
| Medication Management Platform | adjacent (shared regimen-driven dispense) | medication management is one care organization's internal medication-use process across its points of care; home infusion is one provider's therapy-delivery business to patients' homes, with delivery logistics and a payer money path |
| Healthcare Revenue Cycle Management | embedded vs standalone | home infusion's billing leg is therapy-specific (per diem, dual benefit, authorization-gated) and embedded in the delivery workflow; RCM is the generic provider money pipeline |
| Clinical Communication Platform | overlay, not the record | engagement/coordination products for home infusion work alongside the system of record; they hold no therapy, production, or billing state of their own |
| Remote Patient Monitoring | different anchor | RPM anchors on device-originated physiological data streams; home infusion may include monitoring but anchors on the therapy and its doses |
| Electronic Prescribing | upstream feed | e-prescribing delivers prescriptions into the intake leg; it does not run the therapy business |

The most important boundary is with **pharmacy management**: the same product family literally serves both markets, and a home infusion pharmacy's system contains pharmacy-dispensing machinery. The distinction is the managed object — the dispense transaction versus the home therapy course with its delivery, administration, and money loop.

## Representative Products

- WellSky CareTend — dedicated home infusion and specialty pharmacy system of record
- Brightree Pharmacy (Home Infusion) — pharmacy business management platform with a home infusion line
- Universal Software Solutions HDMS — home infusion/specialty pharmacy management with dual-benefit adjudication
- Keycentrix Newleaf — pharmacy management with infusion-specific modules
- AlayaCare — home infusion software from the nursing-coordination side
- WeInfuse — infusion-center platform expanded to home infusion and specialty pharmacy

Adjacent overlay products studied for boundary purposes: QliqSOFT and CitusHealth (patient engagement and coordination layers that work alongside the system of record).

## Sources

Research date: **2026-09-10**

- NHIA (National Home Infusion Association) — "What is home infusion?": https://nhia.org/about-home-infusion/
- NHIA — Home Infusion 101 (curriculum overview): https://nhia.org/education-ce/open-access-education/home-infusion-101/
- NHIA — 2025 Products & Services Guide: https://nhia.org/wp-content/uploads/2024/09/2025-Products-and-Services-Guide.pdf
- WellSky — CareTend Home Infusion Software: https://wellsky.com/home-infusion-software/
- WellSky — "Get to know CareTend" brochure: https://info.wellsky.com/rs/596-FKF-634/images/WS-HC071-CareTend_Brochure%5BWEB%5D.pdf
- Brightree — Home Infusion Pharmacy: https://www.brightree.com/home-infusion-pharmacy/
- Universal Software Solutions — HDMS Infusion Pharmacy Software: https://universalss.com/infusion-pharmacy-software/
- Keycentrix — Newleaf: https://keycentrix.com/newleaf/
- AlayaCare — Home Infusion Software: https://alayacare.com/home-infusion-software/
- WeInfuse — Infusion Center Software: https://weinfuse.com/infusion-center-software/
- QliqSOFT — Home Infusion: https://www.qliqsoft.com/industries/home-infusion/

> Sourcing limitation: evidence is drawn from official vendor product/solution pages, one vendor brochure, and the industry association's definitional pages. Vendor help-center/user-guide articles were not reachable this pass, so precise operational details (numeric limits, exact workflow stage names, default settings, compounding-module internals) are intentionally not asserted. Claims are calibrated to cross-product commonality where multiple vendors agree, and kept conceptual where only one vendor's framing is available.

Detailed product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
