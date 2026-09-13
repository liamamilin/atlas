# Home Care Agency Management

## Overview

A **Home Care Agency Management** application is a home care agency's operating system for delivering scheduled personal and support care in clients' own homes. It holds the agency's two-sided population — the clients who receive care and the caregivers who deliver it — plans recurring home visits against each client's care needs, captures a record of every delivered visit at the point of care, and turns those delivered visits into the agency's money: invoices or claims to the people who pay for care, and paychecks for the caregivers who provided it.

The defining core is small:

```text
Client (care recipient at home)  +  Caregiver (agency staff)
        └── Scheduled home visit (recurring, assigned)
              └── Delivered-visit service record (time on site + care given)
                    ├── Billed to the payor / client
                    └── Paid to the caregiver
```

Everything else the market associates with this software — care plans, EVV check-in/out, family portals, AI matching, compliance tracking — is a standard capability layered on this core, not what makes the software what it is. A pre-digital agency running on paper visit logs signed by clients, a wall schedule, and an invoice book satisfies the same structure; today's products digitize it.

When the center of gravity shifts to physician-ordered skilled clinical care under Medicare conditions of participation, the product has crossed into **Home Health EHR / Management**, a neighboring type that vendors themselves keep separate.

## Users & Context

The software serves one organization — a home care agency — across an office and the field:

**Primary users:**

- **Schedulers / care coordinators** — build and maintain the visit schedule, match caregivers to clients, fill open shifts, react to same-day disruptions (call-offs, weather, running-late caregivers). This is the busiest seat; the schedule is their daily workspace.
- **Agency administrators / office managers** — own client intake, caregiver records, compliance status, and agency settings across one or many branches.
- **Caregivers** — the field workforce. They receive their schedule on a personal mobile app, travel to clients' homes, clock in and out at the client's home, complete the assigned care tasks, write visit notes, and submit their time.
- **Billing staff** — turn verified visits into invoices and payer claims, chase remittances, work denials, and reconcile payments.

**Secondary users:**

- **Clients and their families** — through a portal or family app: see who is coming and when, read shift notes, sometimes pay invoices.
- **Executives / directors** — dashboards over hours delivered, revenue, caregiver utilization, and compliance exposure.
- **Payors (in some deployments)** — Medicaid programs and managed-care organizations may receive visit and verification data directly from the platform, and in one observed posture even operate payer-side screens over the same network.

The work context is distinctive: the "workplace" being managed is distributed across hundreds of private homes, the workforce is large, mobile, high-turnover, and often non-office-workers, and every delivered hour must be evidenced because someone else — a family, an insurer, a government program — is paying for it.

## Core Model

### The defining core

**Client.** The care recipient: an identified person, served in their own home, carrying contact and address details, care-relevant attributes (needs, preferences, mobility, pets, language), payor arrangement(s), and — in payer-funded contexts — an authorization of the hours or services they may receive. The client's home is the place of service; the client record is the anchor for everything scheduled and delivered there.

**Caregiver.** The agency staff member who delivers care: an identified worker with availability, preferred weekly hours, skills and certifications, assigned clients, and pay rates. Caregiver records carry compliance state (credentials, training, screening) because agencies are responsible for who they send into homes.

**Visit.** The unit of service delivery and the hub of the whole model. A visit is a dated, time-bounded appointment at a specific client's home, assigned to a specific caregiver, generated from a recurring pattern (e.g., "every weekday 8–12") and constrained by the client's care needs and authorized hours. Visits have a lifecycle: planned → assigned → (reassigned / open) → delivered → verified → billed and paid. The schedule is the calendar of visits; nearly every other object hangs off one.

**Delivered-visit service record.** The per-visit evidence that service actually happened: actual clock-in and clock-out times captured at the client's home (in current US products, electronically with location verification — EVV; historically, a paper timesheet signed by the client), plus what was done during the visit — tasks completed from the care plan, notes, sometimes the client's signature. This record is the agency's authoritative service record: billing and payroll are both derived from it, so its integrity is the integrity of the agency's revenue and its labor cost.

**The money translation.** Two directions off the same records:

- *Revenue side* — delivered visits are grouped and billed to whoever pays: an invoice to a private-pay client or family, or a claim to a payer (Medicaid, a managed-care organization, long-term-care insurance, veterans programs) with claim submission, remittance matching, and denial handling in payer contexts.
- *Cost side* — verified visit hours are computed into caregiver pay (regular hours, overtime, holiday, adjustments) and exported to payroll.

Remove any one of the four structures and the type collapses into something else: no two-sided population → generic employee scheduling; no home visit → facility or appointment scheduling; no delivered-visit record → a calendar with nothing to bill against; no money translation → a documentation tool that doesn't run a business.

### Standard capabilities mature products add

These are near-universal in current products but are not what defines the type:

- **Care plan** — the client's individualized plan of care: objectives, tasks and interventions (bathing, dressing, meal preparation, medication reminders, companionship), often organized in reusable libraries. The care plan is what turns a visit from "an hour at Mrs. Smith's" into "these specific tasks at Mrs. Smith's"; caregivers see the plan on the visit in their app and check off what they did.
- **Client–caregiver matching** — selecting the right caregiver for a visit using skills, certifications, location and driving distance, availability, preferred hours, continuity of care, and personal preferences on both sides. Increasingly assisted by automated recommendations.
- **Open-shift machinery** — when a visit loses its caregiver, the unassigned visit can be broadcast to a pool of qualified caregivers (by text, email, or app) who accept it; caregivers can also swap shifts and set availability.
- **Alerts** — late or missed visits, no-show reminders, clock-in/out reminders, caregivers approaching overtime, medication reminders; a real-time operations feed for coordinators.
- **Family / client portal** — visibility of the care calendar, caregiver arrival, and shift notes; sometimes invoice payment.
- **Compliance tracking** — caregiver credentials, certifications with expiry, training, screening; flags before an uncompliant caregiver is scheduled.
- **Authorization management** — tracking authorized hours or services against scheduled and delivered hours, with utilization views so the agency neither over-serves (unpaid overage) nor under-serves (lost revenue).
- **Reporting and dashboards** — hours delivered, visit completion, punctuality, revenue, caregiver utilization.
- **Intake and assessment** — structured onboarding of a new client from referral to first schedule.

### One structure, many implementations

The core is conceptual; products realize it differently:

```text
Concept:  Delivered-visit service record
          US Medicaid context:  electronic clock-in/out with GPS + EVV data elements,
                                sometimes telephony; state aggregator integrations
          Private-pay context:  app check-in/out + notes + client signature
          UK homecare:          carer app visit logs + timesheets (no EVV regime)
          Historical practice:  paper timesheet signed by the client

Concept:  Revenue side of the money translation
          Private pay:          client invoices + online payment
          Payer-funded:         claims (e.g., 837 files) → remittance (835) → denials/AR
          Mixed agencies:      both, split per client by payor
```

## How It Works

### The intake-to-income loop (the defining workflow)

```text
Referral / inquiry
→ intake & assessment (client record, needs, payor, authorization of hours)
→ care plan authored (tasks per visit)
→ recurring visits scheduled against the care plan and authorization
→ caregiver assigned (matched by skills, location, availability, continuity)
→ caregiver delivers the visit:
     clock in at the client's home (time + location captured)
     → complete care-plan tasks, write notes
     → clock out
→ visit verified (auto-verified when data matches rules; exceptions reviewed by office)
→ visit billed (client invoice or payer claim; remittance matched; denials worked)
→ caregiver paid (verified hours → pay computation → payroll export)
```

This loop is the reason the software exists: every leg feeds the next, and the delivered-visit record is the pivot on which both revenue and payroll turn.

### The daily operations loop (the coordinator's workflow)

```text
Review today's schedule and alerts
→ handle disruptions: caregiver call-off, client cancellation, running-late visits
→ broadcast open visits to qualified caregivers / reassign
→ monitor clock-ins (missed clock-in = potential missed visit → intervene)
→ review exceptions after the day: unverified visits, overtime, gaps in coverage
```

Home care scheduling is continuous, not a set-and-forget plan: caregiver absence and client changes are daily events, and a single unfilled visit is both a care failure and unbilled revenue.

### The billing cycle (payer-funded context)

```text
Verified visits accumulated per payor period
→ pre-billing checks (visit complete? EVV valid? within authorization?)
→ claim file generated and sent to the payer
→ remittance received and matched against claims
→ denials corrected and resubmitted; balances worked
```

Private-pay billing is the same translation with a simpler tail: invoice → family portal payment → reconciliation.

## Interfaces

### Agency web console (the office surface)

- **Schedule / calendar** — the primary workspace: days and weeks of visits across clients and caregivers, color-coded by state (assigned, unassigned, completed, missed); drag-and-drop reassignment; open-visit highlighting.
- **Client records** — demographics, address, care plan, authorizations, visit history, documents, family contacts.
- **Caregiver records** — profile, availability, skills/certifications with expiry, assigned clients, hours and pay setup.
- **Billing / claims workspace** — billing batches per payor, claim status, remittances, denials, client invoices and payments.
- **Dashboards / reports** — operations and revenue overviews, compliance status, authorization utilization.

### Caregiver mobile app (the field surface)

The caregiver's entire workday: upcoming visits with client address and directions, clock in/out (with location capture), the visit's care-plan tasks and client notes, task check-off, visit notes, client signature where used, timesheets, open-shift offers, shift swaps, availability, and messaging to the office. Designed for a non-office workforce: simple flows, offline tolerance, reminders.

### Family / client portal

Read-mostly view of the care calendar, who is coming, completed-visit notes, and — in some products — invoice payment. Reduces office call volume and builds family trust.

### Admin mobile app

A companion for managers on the move: schedule oversight, reassignment, alerts.

## Important Rules / Behaviors

- **The delivered-visit record gates the money.** Visits are not billed and caregivers are not paid from the plan — they are billed and paid from the verified record of what actually happened. In payer-funded US contexts, claims require valid verification data (the EVV elements: who, what, for whom, when, where, start/end); a visit that fails verification is a claim at risk. This is the software's central discipline.
- **Verification is rule-driven with human exceptions.** Products auto-verify visits whose captured data matches configured tolerances and route only exceptions (late clock-in, wrong location, missing data) to office staff for review or correction.
- **Authorizations bound the schedule.** Scheduled and delivered hours are measured against the client's authorized hours; over-delivery risks non-payment, under-delivery loses revenue — utilization views exist to manage exactly this edge.
- **Compliance gates assignment.** Caregiver credentials, training, and screening state determine who may be scheduled to whom; expired credentials surface as scheduling blocks or warnings.
- **Missed visits are first-class events.** A visit with no clock-in by its start window raises an alert; the coordinator must fill or cancel it, and the outcome (missed visit, make-up visit) is recorded because it affects both care and billing.
- **Payor rules vary and are configuration.** Each payor (Medicaid program, MCO, LTC insurer, VA program) carries its own billing rules, rates, and verification requirements; agencies configure pay-and-bill rates per client, service, and authorization. In the US, EVV itself varies by state (open vs closed vendor models, aggregator integrations).
- **Privacy is structural.** Client data is health-adjacent and protected (HIPAA framing in the US); caregiver visibility of client details is permission-scoped, and family portals expose only appropriate slices.

## Variants

- **Private-pay / personal care agencies** — the classic non-medical agency: hourly companion and personal care, invoice-and-card billing to families, client signatures, lighter payer machinery.
- **Payer-funded agencies (Medicaid / MCO-centric)** — visits funded by government or managed-care programs: authorizations, EVV compliance, claim files, remittances and denials dominate; some platforms even operate payer-side products over the same network.
- **Mixed-payor agencies** — the common case: one client base billed across private pay, LTC insurance, VA, and Medicaid simultaneously, split per client.
- **IDD / self-direction programs** — the same visit-and-verification machinery pointed at disability services, with person-centered plans and public-program funding.
- **Skilled-care extension** — personal-duty nursing add-ons (plan-of-care certification, practitioner orders, vitals, wound care) riding on the visit engine; the drift zone toward Home Health EHR.
- **Regional variants** — UK/EU homecare ("homecare"/"domiciliary care"): rostering, finance, and regulator-facing quality/compliance packaging (e.g., CQC inspection readiness) instead of EVV/Medicaid machinery.
- **Franchise / multi-branch** — one brand, many locally operated branches; consolidated reporting with branch-scoped operations.
- **AI-era assistance** — automated caregiver matching, AI care summaries, ambient documentation of visits, AI-drafted care plans from assessment conversations — current-generation additions across the sample, not yet definitional.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Home Health EHR / Management | nearest neighbor, frequently confused | skilled clinical care under physician-ordered plans of care and Medicare conditions (assessments, certification periods, clinical visit documentation); home care is non-medical/personal care on hourly visit schedules with agency-authored care plans. Vendors sell them as separate products or add-on modules |
| Hospice Management | adjacent clinical-home type | terminal-illness interdisciplinary care under the hospice benefit; different objects (volunteers, bereavement) and rules |
| Employee Scheduling Platform / Workforce Management | overlapping capability | generic staff scheduling has no care recipients, care plans, service verification, or payor billing; home care scheduling is client-need-driven |
| Staffing Agency Management System | adjacent business model | staffing places workers into client organizations' shifts (recruitment/placement-centric); home care delivers recurring personal-care services to individuals at home |
| Patient Scheduling | adjacent scheduling | books patient appointments with providers at facilities; home care schedules staff into clients' homes |
| Care Coordination Platform | adjacent care-delivery type | cross-provider orchestration of a patient's journey from payer/provider view; not the agency's own operating system of record |
| Skilled Nursing Facility / Long-term Care systems | different place of service | facility-based care; the visit at the client's home, not the bed or unit, is the operating unit here |
| Non-emergency Medical Transportation | adjacent service | transport to care, not delivery of care in the home |

The boundary that matters most is **Home Health EHR / Management**: the two share clients-with-care-plans and even vendors, but the regulatory regime (physician orders vs agency care plans), the documentation (clinical assessment vs task completion), and the billing shape (episode/period-of-care vs hourly visits) differ. If the software's center of gravity is physician-ordered clinical care, it is home health; if it is the scheduled-visit operating loop for personal care, it is this type.

## Representative Products

- **AxisCare** — US all-in-one personal-care/private-duty platform, scheduling-first, SMB through enterprise
- **HHAeXchange** — US payer/Medicaid/EVV-centric platform connecting providers, payers, and caregivers
- **WellSky Personal Care** — large US incumbent for non-medical private duty (ex-ClearCare lineage)
- **Birdie** — UK homecare platform (rostering, finance, quality & compliance; CQC context)

The model was checked against a regional non-US sample (Birdie, UK) and against the paper-era practice the vendors themselves name (paper timesheets, paper logs) to avoid defining the type by the current US EVV implementation.

## Sources

Research date: **2026-09-08**

- AxisCare — product and feature pages: https://axiscare.com/ , https://axiscare.com/features/scheduling/ , https://axiscare.com/features/electronic-visit-verification/ , https://axiscare.com/features/billing/ , https://axiscare.com/features/caregiver-app/ , https://axiscare.com/features/care-plans/
- HHAeXchange — product pages: https://www.hhaexchange.com/ , https://www.hhaexchange.com/solutions/providers/scheduling , https://www.hhaexchange.com/solutions/providers/billing-payroll
- WellSky Personal Care — https://wellsky.com/personal-care-software/
- Birdie — https://www.birdie.care/

> Sourcing limitation: vendor help centers and two candidate products (AlayaCare, ShiftCare) were not reachable from the research environment on 2026-09-08; evidence is drawn from official product/feature pages rather than operational help documentation. Precise operational parameters (exact verification tolerances, state-specific EVV rules, claim-format details, payroll export field lists) are therefore intentionally not stated. Product-by-product observations and the cross-product comparison are recorded in the paired Research Notes.
