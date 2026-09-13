# IRT / RTSM

*(Interactive Response Technology / Randomization and Trial Supply Management — two industry names for one category of system)*

## Overview

An **IRT / RTSM** is the clinical trial's treatment-allocation and drug-supply system: the software that, at the moment a subject is enrolled at a trial site, decides and records what treatment that subject receives — and then manages the trial's investigational drug so that the right blinded medication kit is physically there to dispense, at that visit and every subsequent one, across every depot, site, and country the trial touches.

The defining structure is small:

```text
The study's allocation design
  (randomization scheme held and applied by the system —
   configured per protocol before go-live)
└── The subject's assignment
    (created by a site-side interactive transaction at enrollment:
     request in → treatment allocation out → recorded)
    └── The trial supply chain of blinded kits
        (identified medication units tracked from depot to site
         to subject, dispensed against assignments, reconciled
         through returns and destruction)
```

Everything else the category is known for — automated resupply algorithms, supply forecasting, direct-to-patient shipping, temperature-excursion handling, mid-study design changes, analytics — is standard equipment built on that core. The name itself encodes the two halves: *randomization and trial supply management* describes the function; *interactive response technology* describes the interaction heritage (sites first reached these systems by telephone — IVRS — then by web and mobile; the interaction, not the channel, is what the system is).

Its boundary is deliberate. Capturing the subjects' clinical data is the EDC's territory. Managing the trial's operations — sites, milestones, monitoring, budgets — is the CTMS's. Physically storing, packaging, and distributing the drug is the clinical supply chain's. The IRT/RTSM holds the one thing none of those hold: **the trial's allocation design and the blinded chain of custody that carries each assignment to the subject it belongs to.**

## Users & Context

The software serves a regulated global production process whose participants sit at different points in the trial:

- **Site staff (study coordinators, sometimes site pharmacists)** — the primary interactive users, and characteristically *occasional* users: they register subjects, request randomization, dispense kits, confirm shipment receipts, and record drug accountability at the moments the protocol assigns them. Products are explicitly designed for users who perform these transactions infrequently and must get them right the first time.
- **Sponsor / CRO study managers and clinical supply managers** — oversight users: enrollment progress against supply, inventory levels and expiry across depots and sites, shipment status, resupply parameters, alerts, reports. They also manage mid-study change.
- **Unblinded and safety roles** — investigators or designated study-leader roles who may break the code for a single subject in an emergency, and drug-safety functions who may unblind for safety reporting without affecting the subject's continued participation.
- **Depot and distribution partners** — receive, fulfill, and ship orders; typically integrated with the system rather than working in it directly.
- **Patients (edge case)** — in decentralized trials with direct-to-patient shipping, patients may confirm receipt of their medication through a patient-facing surface; home caregivers may act for them.

Context: pharmaceutical, biotech, and medical-device sponsors and their CROs; phases from first-in-human through post-market; the double-blind randomized trial is the archetype, but open-label trials use the same machinery for allocation and supply. The system is built per study by the vendor's or CRO's specialist teams — configuration, testing, user acceptance testing, and certification precede go-live — and runs under the trial's regulatory quality regime (attributable, auditable records throughout).

## Core Model

### The Defining Core

**1. The study's allocation design.** Before a trial opens, its randomization scheme — a pre-generated allocation list or an algorithm such as minimization, with its stratification and balance factors (for example site, sex, age band, disease severity), its cohorts, stages, and treatment ratios — is configured into the system as protected content. The system holds the mapping between allocation sequence and actual treatment; sites never receive it. The design is versioned as the protocol changes. This is what makes assignments statistically sound and centrally consistent across every site in the trial, and it is the reason the system cannot be replaced by a form: the design is knowledge the trial must hold somewhere, and this is where it lives.

**2. The subject's assignment.** When site staff register a subject's enrollment and request randomization — at or near the protocol's randomization visit — the system applies the design and returns that subject's allocation in real time: a treatment-arm assignment (expressed in blinded form where the trial is blinded) and, typically, the specific medication kit to dispense for it. The assignment is a persistent record: it anchors every later dispensing for that subject, every dose modification, and the subject's entire treatment history. Its creation is the *interactive response* the category is named for — a transaction, not a lookup.

**3. The trial supply chain of blinded kits.** The trial's drug exists in the system as identified, individually numbered units — kits — whose treatment content is unknown to the people handling them. The system tracks each kit through its life: released at a depot, shipped to a site (or directly to a patient), received and confirmed into site inventory, assigned and dispensed to a subject against that subject's assignment, and finally accounted for — returned, or destroyed — until every kit is reconciled. Kits are interchangeable: they are not labeled for particular patients but assigned at dispensing time, which is what allows site inventory to stay small, waste to stay low, and the blind to stay intact.

The three bind into one loop: **the assignment drives the dispensing; the dispensing draws down the inventory; the inventory drives the resupply; the resupply is shaped by the enrollment forecast and the visit schedule.** Remove any leg and the rest collapses into something else — a statistics tool, a warehouse system, or the sealed-envelope paper method this category replaced.

The **blinding thread** runs through all three: in a blinded trial, the system strictly controls who may see the treatment mapping (role-based blinding management), keeps site inventory and resupply parameters from revealing it, and provides a controlled, auditable emergency-unblinding path as the only sanctioned exception. In open-label trials the same structures operate without concealment — the machinery is the same; the mapping simply stops being sensitive.

### Standard Capabilities of Mature Products

Around that core, essentially all current systems carry a common set of machinery:

- **Allocation machinery** — stratified and site-stratified schemes; cohort, stage, and phase management; adaptive designs (patient replacement, re-randomization, crossover, subject roll-over, open-label extension); dose calculation, titration, modification, and interruption; dynamic cohort and dose management.
- **Supply machinery** — automated resupply logic driven by inventory triggers and/or visit-schedule prediction; initial supply triggered by site activation; expiry tracking with alerts so product does not expire in site stock; supply forecasting; drug pooling across studies and depots; direct-to-patient shipping; central pharmacy support; temperature-excursion management; controlled-substance handling.
- **Governance machinery** — role-based permissions and blinding management; automated emergency code break with audit trail and study-team notification; mid-study changes and protocol amendments applied to the running study; reports and data exports whose content respects the requesting user's blinding status.
- **Oversight surfaces** — real-time reporting on subjects, sites, drug inventory, depots, and shipments; alerts for low stock, unreceived shipments, and looming expiry; enrollment-versus-supply views for study and supply managers.
- **Integration machinery** — exchange with the EDC (enrollment and eligibility facts in; randomization number and kit data out — platforms that unify the two eliminate double entry between them), supply rollups to the CTMS, feeds from temperature loggers and depot distribution systems.
- **Service machinery** — specialist study build and testing teams; 24/7 multilingual helpdesk support, descending from the category's telephone heritage.

### One Structure, Many Implementations

```text
Concept:            The allocation design
Implementations:    pre-generated allocation list (list/scheme/schedule) ·
                    algorithmic assignment (e.g., minimization) ·
                    built-in list generators vs vendor/sponsor-generated lists

Concept:            The enrollment-moment transaction
Implementations:    telephone (IVRS heritage) · web portal · mobile ·
                    embedded in EDC platform vs standalone system

Concept:            The blinded kit chain
Implementations:    serialized numbered kits · bulk (unnumbered) supply ·
                    site dispensing vs depot-direct / direct-to-patient ·
                    trigger-based resupply vs prediction-based resupply
```

A reader who has only seen one shape — a web portal where a coordinator clicks "randomize" and the screen returns a blinded kit number — should still recognize a telephone-era voice-response system and a platform module unified inside an EDC as the same Type, and an inventory-only supply deployment as the same product family running with one leg reduced.

## How It Works

### Build and go-live

```text
Protocol arrives
→ the randomization methodology is chosen and specified
   (scheme/algorithm, strata, cohorts, kit types)
→ the allocation design is generated and loaded
   (or generated in-system), under controlled access
→ supply strategy configured: depots, site profiles,
   resupply parameters, kit definitions
→ configured system is tested; sponsor runs user acceptance
   testing; quality certification
→ sites are provisioned and activated; the study goes live
```

Build is where the trial's statistical integrity is fixed: every assignment the system will ever make traces back to the design configured here.

### The enrollment-moment transaction (the defining loop)

```text
Subject is screened and found eligible
→ site staff register the enrollment in the system
   (subject identifiers, stratification factors as required)
→ the system applies the allocation design and returns,
   in real time, the subject's allocation —
   and typically the kit to dispense for it
→ the assignment is recorded on the subject's record
→ site staff dispense that kit; accountability is updated
```

This transaction is the system's reason to exist. It replaces the sealed-envelope method (sequence-numbered envelopes paired with pre-labeled kits, chosen in order at the site), which was workable only for small, simple designs and carried the blind's exposure in paper form.

### The supply loop

```text
Site activation triggers an initial shipment from the depot
→ site staff confirm receipt in the system; kits become
  available for assignment
→ the system watches site inventory against projected demand
   (enrollment pace, visit schedule, treatment arm mix —
   without revealing it)
→ inventory reaching its configured level generates a
  resupply order to the depot; the closed loop repeats
→ expiry dates are tracked; expiring stock is used or
  replaced before it strands; alerts fire on low depot stock,
  overdue shipments, looming expiry
```

The design goal throughout: enough of the *right* blinded stock at each site — but only enough, because over-supply wastes drug and under-supply interrupts treatment.

### Continuing treatment

```text
Subject returns for each protocol visit
→ system indicates the dispensing due for that visit
   (kit type may change across visits; doses titrate)
→ site dispenses against the standing assignment
→ dose modifications and interruptions are recorded
   against the subject's treatment history
```

### Breaking the blind under control

```text
Medical emergency requires knowing the treatment
→ a permissioned role (investigator or delegate) performs
   the emergency code break in the system
→ the system reveals the assignment, records who/when/why,
   and notifies the study team
→ the unblinded subject is typically discontinued from
   further dosing; safety functions may unblind for safety
   reporting without ending participation
```

The automated code break replaces code-break envelopes and around-the-clock telephone lines with a controlled, auditable transaction — a deliberate structural feature, not an afterthought.

### Close-out

```text
Last subject completes
→ all kits reconciled: dispensed, returned, or destroyed
→ accountability reports assembled for inspection
→ the study's supply and assignment records archived
```

## Interfaces

Surfaces described conceptually; exact layouts and names vary by product.

### Site transaction screens

The interactive surface the category is named for, used by occasional users under time pressure.

- typical information: the site's subjects and their statuses, the pending transaction (enroll, randomize, dispense, confirm receipt), the site's blinded inventory
- primary actions: register a subject, request randomization, dispense a kit, confirm a shipment receipt, record accountability (used, damaged, returned)

### Sponsor / supply oversight views

The manager's picture of allocation and supply across the trial.

- typical information: enrollment by site and cohort, inventory by depot/site/kit type, shipments in flight, expiry horizon, resupply activity, alerts
- primary actions: adjust resupply parameters, add sites or countries, approve shipments or depot actions, run reports

### Reports and exports

- typical information: assignment histories, dispensing logs, accountability and reconciliation reports, shipment history
- primary actions: generate, schedule, export — with content filtered by the requesting user's blinding status

### Helpdesk

A human channel — phone and chat, multilingual, around the clock — reflecting the category's call-center heritage and the fact that site transactions cannot wait for business hours.

### Patient confirmation (direct-to-patient trials)

- typical information: pending shipment, receipt confirmation
- primary actions: confirm receipt of medication

## Important Rules / Behaviors

### The blind is structural, not cosmetic

Treatment mapping is withheld by design: sites see blinded kit numbers, never arms; inventory and resupply parameters are withheld from sites because inventory patterns themselves can leak the blind (a documented concern in the supply-methods literature); reports and exports are filtered by the user's blinding status. Breaking the blind is a permissioned, recorded transaction with defined consequences — never a side effect of browsing.

### Assignments come from the design, not from users

Site staff cannot choose a subject's treatment. The system applies the held scheme or algorithm; the site's transaction requests and receives. This is what makes the trial's randomization auditable and bias-free.

### Kits are interchangeable until dispensed

Blinded kits are not pre-allocated to patients. They are assigned at dispensing time from site inventory, which is what decouples supply from enrollment count, minimizes waste, and keeps site stock small.

### Resupply is algorithmic

Shipments are generated by the system's supply logic — triggered by inventory levels and/or predicted from visit schedules — not by site staff placing ad-hoc orders. The supply engine balances availability, expiry, and waste.

### Everything is attributable

Who randomized, who dispensed, who confirmed receipt, who broke a code, when and why — every transaction is recorded for the trial's regulatory inspection. The accountability chain must reconcile at close-out: every kit the trial made is either dispensed, returned, or destroyed, with a record.

### The system changes while the trial runs

Protocols are amended mid-study: new cohorts, changed doses, revised schedules. Mature systems apply such changes to the live study under governance — some by permissioned users directly, some through vendor change processes — without stopping enrollment, and without disturbing the assignments already made.

## Variants

- **Channel variants** — telephone (IVRS) heritage, web portals, mobile access; the function is channel-independent.
- **Blinding-posture variants** — double-blind trials (the archetype and the reason for most of the machinery); open-label trials using the same allocation and supply machinery without concealment.
- **Design-complexity variants** — simple two-arm trials; stratified multi-arm designs; adaptive and cohort-based designs; basket/umbrella and other master-protocol shapes concentrated in oncology and rare disease.
- **Deployment variants** — standalone specialist systems; modules embedded in an EDC platform (unified to eliminate double entry between randomization and data capture); modules of CRO technology suites; IRT bundled with physical supply-chain services.
- **Reduced deployments** — randomization-only use for trials with no investigational-product supply (the allocation design and assignment transaction without the kit chain); inventory-only supply deployments without randomization, offered by at least one vendor as a companion product.
- **Decentralized-trial variants** — direct-to-patient shipping from depot or site, patient receipt confirmation, home-caregiver users.
- **Therapeutic-area adaptations** — cold-chain and temperature-excursion emphasis for temperature-sensitive products; controlled-substance handling; documented adaptation guidance for oncology, CNS, rare-disease, and gene-therapy trial designs.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Electronic Data Capture / EDC | closest sibling; constant integration partner | EDC captures subjects' clinical data (forms per visit, validated, the trial's data record). IRT/RTSM decides treatment allocation and runs the drug chain. The enrollment event is shared turf — eligibility facts flow in, allocation data flows out — and platform vendors may unify the two in one system, but even then they remain separate products with separate builds and separate blinding models. Remove allocation+supply from a unified product and EDC remains; remove capture and IRT/RTSM remains |
| Clinical Trial Management System / CTMS | adjacent, integrated | CTMS manages trial operations — sites, milestones, monitoring, budgets — and may show supply rollups from the IRT/RTSM. It does not randomize subjects or manage kits; the assignment transaction and the kit chain of custody are not CTMS structures |
| ePRO / eCOA Platform | adjacent, often suite-bundled | patient-reported outcomes collected from subjects on their own devices; a different interaction (reporting symptoms) with a different object world (diaries, questionnaires). Both are "interactive" trial systems serving sites and patients; only one allocates treatment and manages drug |
| Clinical Trial Supply Chain Services | adjacent, complementary | physical logistics — packaging, labeling, depot storage, distribution, returns — and pre-trial supply forecasting/planning. The IRT/RTSM is the trial-conduct system of record for assignment and accountability; vendors demonstrate the seam by shipping forecasting/planning products separate from their RTSM systems |
| Pharmacy Management System | name-adjacent, different world | dispensing for patient care against prescriptions, in the open. Trial dispensing is blinded, protocol-driven, against a held allocation design; a "central pharmacy" function inside an IRT/RTSM is a module, not the pharmacy Type |
| Randomization Services / Tools | reduced sibling | systems that hold a design and produce assignments for trials without drug supply (common in academic and non-drug research, sometimes inside EDC products). The allocation design and assignment transaction without the supply chain — real, but thinner than the market category this leaf names |

## Representative Products

- **Suvoda IRT / RTSM** — standalone specialist; complexity-first positioning (oncology, CNS, rare disease); explicit mid-study configurability by permissioned users
- **4G Clinical Prancer RTSM** — productized RTSM family (full, Lite, and inventory-only deployments) with a separate supply-forecasting product
- **Almac IXRS³** — legacy market leader descending from the IVRS/IWRS era; expert-services and biostatistics-led build model
- **Medidata RTSM** — platform-embedded pole, unified with the vendor's EDC; live mid-study design editing; electronic supply accountability
- **IQVIA IRT** — CRO-suite-embedded; component-library build; 24/7 multilingual support heritage

The core model was checked against the category's own history (sealed-envelope method; telephone-era voice-response systems; the addition of dispensing and resupply to early phone randomization) and against open-label and reduced deployments, to avoid defining the Type by today's dominant web-platform shape.

## Sources

Research date: **2026-09-10**

- Suvoda — IRT product page: https://www.suvoda.com/products/irt ; RTSM (IRT) page: https://www.suvoda.com/rtsm-irt-clinical-trial
- 4G Clinical — home and technology pages: https://www.4gclinical.com/ , https://www.4gclinical.com/technology ; white paper "IRT. IVRS. IXRS. IWRS. RTSM." (history of the category's naming and function)
- Almac Clinical Technologies — "What is IRT and How Does it Impact Clinical Trials?" and "What is Randomisation and Trial Supply Management (RTSM)?" blog articles; supply-strategy white paper: https://www.almacgroup.com/clinical-technologies/
- Medidata — "What is RTSM? Randomization & Trial Supply Management 101" (blog) and RTSM product page: https://www.medidata.com/en/data-experience/rtsm/
- IQVIA — Interactive Response Technology fact sheet: https://www.iqvia.com/
- Independent academic literature — "Blinding properties of methods for supplying drug kits to investigational sites" (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC5935824
- Neutral sponsor-process sources — university/hospital SOPs on randomization, blinding, and code break (USF Health; UCL Joint Research Office; MCW Cancer Center), used only to corroborate the site-transaction and unblinding patterns

> Sourcing limitation: none of the sampled systems publishes its operational user manual — all run behind client logins as validated systems. Evidence rests on official product and educational pages, independent academic literature, and sponsor standard-operating-procedure documents. Precise operational parameters (resupply thresholds, buffer quantities, check cadences, allocation-list sizes, time windows) are therefore deliberately not stated in this document; workflow descriptions are kept at the level the sources support. Vendor-published metrics and claims (study counts, defect rates, component counts) were excluded. Detailed product-by-product observations, the cross-product comparison matrix, and boundary analyses are recorded in the paired Research Notes.
