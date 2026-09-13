# Payer Claims Processing

## Overview

A **Payer Claims Processing** system is the claims-operations machinery of a health plan (payer): the software that takes requests for payment for health care services — claims — and drives them, under the plan's configurable rules, to recorded determinations and settled outcomes, with adjustment and appeal loops afterwards.

Its defining core is small:

```text
Claim (request for payment for health care services)
└── Rule-driven adjudication → recorded determination (pay / deny / pend)
    └── Settlement output (payment + explanation to the claimant)
        └── Adjustment loop (adjust / void / reprocess / appeal)
```

Everything else commonly associated with this software — AI auto-adjudication, standardized electronic transactions, government-program reporting, payment-integrity programs, provider portals — is standard mature structure or variant machinery, not what makes a product a payer claims processing system. A paper-era claims department operating with mailed forms, clerical examination against the benefit certificate, hand-written payment registers, and re-examination on appeal satisfies the same core.

The boundary that defines the Type: the machinery **determines and settles the plan's obligations for care received**. It does not, by itself, hold the plan's membership, enrollment, eligibility, benefit-plan, or premium record — that is the health plan administration system. In the market the two sit in various arrangements: the claims machinery may be bundled inside a core administration system, shipped standalone, or operated as a modular suite against an external core. The arrangement is packaging; the machinery is the Type.

## Users & Context

The primary users are the health plan's claims operations staff:

- **claims examiners / adjudicators** — work claim queues, resolve exceptions, apply judgment where automated evaluation routes work to them, and record determinations
- **claims operations supervisors** — manage queues by aging and priority, reassign work, monitor throughput and quality, handle escalations
- **configuration and analyst staff** — maintain the rule layers the machinery applies: edit libraries, benefit logic, fee schedules, payer policies
- **review specialists** — clinical coders, nurses, and medical reviewers who examine itemized bills, validate diagnoses and coding, and support expert pre- or post-payment review
- **provider services and member services staff** — answer claim-status inquiries and explain what was paid or denied and why
- **finance staff** — run payment cycles, reconcile payments against determinations, and process recoveries

The machinery is operated in several settings: by health plans themselves (commercial, Medicare Advantage, Medicaid managed care), by third-party administrators running the same machinery for self-funded employer plans, by delegated vendors running claims operations on a plan's behalf, and — in government variants — by state programs operating equivalent machinery for their populations.

## Core Model

### The Defining Core

```text
Claim as the unit of record
└── Rule-driven adjudication to a recorded determination
    └── Settlement output & the adjustment loop
```

Three structures. If any one is removed, the product is no longer recognizable as payer claims processing:

- **Claim as the unit of record** — a persistent, individually addressable request for payment for health care services, submitted by a provider (or another claimant) against a member's coverage. A claim carries the member reference, the servicing provider, and coded service lines — procedures, diagnoses, dates of service, submitted charges — and moves through explicit statuses from receipt to finalization. The machinery's memory lives in the claim: every evaluation, determination, payment, and adjustment attaches to it. Without a held claim there is nothing to adjudicate, adjust, or audit.
- **Rule-driven adjudication to a recorded determination** — the claim is evaluated against the payer's configurable rule layers, and the evaluation produces a recorded outcome: payment in whole or in part, denial, or a hold pending missing information or another party's action. Whether the evaluation is fully automated, fully human, or a hybrid is a design choice; the rules-against-claim evaluation with a recorded determination is the invariant. Without it, the product is a claim data-entry shell.
- **Settlement output & the adjustment loop** — a finalized determination settles into financial output: payment is released (or the denial is communicated), and an explanation of what was paid or denied, and why, is returned to the claimant. Finalized claims can re-enter the machinery through adjustment, voiding, reprocessing, and appeal, with each adjustment recorded against the claim's history. Without settlement, the product is a decision engine whose outcomes never move money; without the adjustment loop, it is a payment factory with no memory and no way to correct itself.

The three structures are jointly load-bearing: a claim store without adjudication is a registry; adjudication without a claim record is a rules test harness; settlement without both is a disbursement factory; adjudication plus settlement without a claim record is anonymous transaction processing in which nothing can be tracked, corrected, or appealed.

### The adjudication rule stack

The evaluation leg applies layers of payer-configurable rules. Mature products commonly organize them along these lines:

- **Submission validity & edits** — is the claim complete, internally consistent, and free of coding and duplicate problems? Failing claims are returned for correction and resubmission rather than adjudicated
- **Eligibility & coverage** — was the member covered on the dates of service, and is the member/provider relationship valid for this plan?
- **Benefit coverage** — does the plan's benefit rulebook cover these services, and at what member cost sharing?
- **Authorization status** — do the services carry the review authorization the plan requires?
- **Pricing** — what is the allowed amount under the applicable fee schedule or contract?
- **Coordination of benefits** — when another payer shares responsibility, how is the payment responsibility divided? This layer depends on other payers' determinations and commonly suspends the claim until they are available

A determination may pass through all layers automatically, or an exception at any layer may route the claim to a human reviewer with the evaluation's reasoning attached. Both are standard realizations; the split between automated clearing and human review is a design point, not a boundary.

### Standard capabilities of mature products

Mature products commonly carry most of the following. They make claims operations practical; they do not define the Type.

- multi-channel intake: standard electronic claim transactions (in the US, the 837-class submission, direct or via clearinghouses), portal entry, batch feeds, and paper conversion
- front-end claim editing ("claim scrubbing") before or at the start of evaluation, including duplicate detection and payer-specific policy edits — in-system or delivered by separable edit services
- real-time eligibility and coverage verification at intake
- claims work queues organized by status, aging, and exception type, with throughput measures such as clean-claim rate and cycle time
- coordination-of-benefits machinery, including exchange of prior adjudication detail between payers
- payment generation and standardized remittance/explanation output to providers (in the US, the 835-class payment-and-remittance transaction)
- provider-facing claim status inquiry and notification (276/277-class exchanges), solicited or unsolicited
- adjustment/void/reprocessing machinery with standardized adjustment-reason vocabularies
- appeals and grievances intake and tracking
- payment-integrity hooks: expert pre-payment review (itemized bill review, coding validation) and post-payment review, audit, and recovery — commonly delivered by separable products
- operations reporting and dashboards (denial patterns, aging, first-pass rates)
- roles, permissions, audit trails, and configuration tooling for the rule layers
- encounter-data handling and government-program reporting where the regime requires it

### One structure, many implementations

The core model is written conceptually. Implementations vary:

```text
Concept:  Claim record
Implementations:  standard electronic transaction sets, portal data entry,
                  scanned paper conversion, encounter records

Concept:  Rule layers
Implementations:  in-system edit libraries, gateway edit services,
                  payer-supplied policy rules, contracted fee schedules,
                  program-specific code policies

Concept:  Decision split
Implementations:  fully automated straight-through clearing, hybrid with
                  AI scoring and human exception queues, predominantly
                  manual examination

Concept:  Settlement output
Implementations:  electronic payment with remittance, check with an
                  explanation-of-benefits statement, denial notices with
                  reason codes

Concept:  Adjustment
Implementations:  standardized adjustment reason codes, revised claims
                  tied to the original, appeal case tracking, recovery
                  and post-payment audit loops
```

A reader who has only seen one implementation — for example an AI-assisted core with automated clearing — should still be able to recognize a manual examination department, a government program's claims engine, or a modular suite riding an external core as the same Type.

## How It Works

### Intake and registration

```text
Claim arrives (electronic transaction / portal / batch / paper)
→ registered as the plan's claim record (member, provider, service lines)
→ front-end validation and acknowledgement
→ errors returned to the claimant for correction and resubmission
```

Intake is the machinery's front door and a quality gate: many mature operations deliberately shift error detection as early as possible — some even evaluate claims on the network before they enter the plan's processing environment — so that correctable problems never become denials.

### Validation and editing

```text
Coding checks, completeness rules, duplicate detection
→ payer-specific policy edits
→ clean claims advance to adjudication
→ failing claims return to the claimant with specific correction guidance
```

### Adjudication

```text
Eligibility confirmed for the dates of service
→ benefit rulebook applied (coverage, cost sharing, network rules)
→ authorization status checked
→ allowed amount priced
→ coordination of benefits resolved where other payers are involved
→ recorded determination: pay (whole/part), deny, or pend
```

The determination is recorded against the claim with its reasons. Claims that clear every layer automatically are settled without human touch; exceptions land in reviewer queues with the evaluation's reasoning attached, and the reviewer's judgment becomes part of the claim's record.

### Settlement and remittance

```text
Payment released (or denial communicated)
→ remittance/explanation produced for the claimant:
  what was paid, what was denied, why (standardized reason vocabularies)
→ member-facing explanations where the plan provides them
→ payment and determination posted to the plan's financial records
```

### Adjustment, appeal, and reprocessing

```text
Provider disputes a determination / member appeals / error discovered
→ claim re-enters the machinery as an adjustment, void, or reprocessed claim
→ re-adjudicated and re-settled
→ every adjustment recorded against the claim's history
```

Finalization is not the end of the claim's life. Correcting a finalized claim is itself an operation of the machinery — done by adjusting with a recorded reason, not by overwriting the original determination — which is what makes the claim record auditable.

### Core vs standard vs variant

**Defining core** — without these, not payer claims processing:

- claim as the unit of record (persistent, identified, status-carrying)
- rule-driven adjudication to a recorded determination
- settlement output with the adjustment loop

**Standard mature structure** — present in most current products:

- multi-channel intake with front-end editing
- eligibility verification at intake; work queues and exception routing
- remittance/explanation output; status inquiry; standardized adjustment vocabularies
- appeals handling; payment-integrity hooks; operations reporting; audit trails

**Common variants** — depends on segment, regime, and packaging:

- bundled in a core administration system vs standalone vs modular
- government-program machinery depth (encounter data, program reconciliation, audit readiness)
- TPA/self-funded operation; dental, vision, and pharmacy line shaping
- automation posture (straight-through processing, AI scoring, prevention-first gateway editing)
- delegated/BPO operation; paper-era and regional realizations

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Claims work queue / operations dashboard

The operation's primary surface.

- claim inventory by status, age, and exception type; throughput and quality measures (clean-claim rate, cycle time, volume)
- primary actions: open a claim, filter and prioritize, reassign, escalate, monitor aging

### Claim detail / adjudication view

One claim's entire world.

- member and provider identification, service lines with codes and charges, edit results, rule-evaluation outcomes, determination with reasons, payment and adjustment history
- primary actions: review evaluation results, record or change a determination with reasons, request information, adjust or void

### Reviewer workbench

Where human judgment enters the loop.

- exception claims routed from automated evaluation, with the evaluation's reasoning attached
- primary actions: accept or overturn the proposed outcome, document the judgment, release or deny

### Intake and transaction monitoring

- submission channels, acknowledgement status, rejection reasons, correction-and-resubmission loops
- primary actions: monitor feeds, trace rejected submissions, manage resubmissions

### Configuration workbench

- edit libraries, benefit logic, fee schedules, payer policies, workflow routing rules
- primary actions: configure, version, and deploy rule changes

### Remittance and explanation output

- payment/remittance records and explanation documents produced for claimants, with standardized reason vocabularies
- primary actions: generate, distribute, reconcile against payments

### Status inquiry surfaces

- provider-facing claim status (portal or standardized transactions) and the machinery's own status notifications and information requests

### Appeals and adjustments

- dispute intake, adjustment/void processing, appeal tracking, recovery workflows

### Reporting and analytics

- denial patterns, aging, first-pass rates, program reporting where the regime requires it

## Important Rules / Behaviors

### Determinations are recorded, not overwritten

Correcting a finalized claim produces a new recorded event — an adjustment with a reason — tied to the claim's history. The original determination, the payment, and every subsequent change remain inspectable. This is the machinery's audit spine.

### The rule stack decides; the claim remembers

Eligibility, benefit coverage, authorization status, pricing, and coordination of benefits together decide whether and how much is paid. Which layer stops a claim determines its route: edit failures go back to the claimant for correction; coverage or authorization questions go to reviewers; coordination-of-benefits claims may wait on other payers' determinations.

### Pend states suspend rather than resolve

A claim held pending missing information, additional documentation, or another payer's action is neither paid nor denied; the machinery tracks it, and mature products support solicited or unsolicited requests for the missing information. The claim stays alive and answerable to status inquiry throughout.

### Status is externally visible

Claimants can ask where a claim stands and receive an answer — through portals or standardized status exchanges — at summary or service-line level. The claim's status vocabulary is shared machinery, not an internal implementation detail.

### Automation splits the queue

Clean claims clear themselves; exceptions route to humans with reasoning attached. The proportions are a design and maturity choice — straight-through processing is a common target — but both halves exist in real operations, and pushing evaluation upstream (preventing errors before adjudication) is a widespread modern practice.

### Coordination of benefits is an external dependency

When another payer shares responsibility, this machinery's determination can depend on that payer's determination. Mature machinery exchanges prior adjudication detail between payers and manages the waiting state explicitly.

### The regime shapes the machinery where government programs are served

Encounter data submission, program reconciliation, program-specific edit libraries, and audit-readiness requirements attach to the same claim machinery in Medicare- and Medicaid-serving operations — regime machinery of real operational weight, but not part of the definition.

## Variants

- **Bundled core administration** — the machinery ships inside a core administrative processing system alongside enrollment, eligibility, provider management, and financial coordination; the most common full-core posture in the market
- **Standalone/connected claims engine** — the machinery deployed as its own system, connected to a plan's administration record
- **Modular suite around an external core** — payer suites that cover enrollment, member, and care operations while riding separate claims cores
- **Government-program pole** — Medicare Advantage / Medicaid managed-care machinery with encounter data, program reconciliation, and audit posture
- **TPA / self-funded operation** — the same machinery run for employer-funded plans
- **Line shaping** — dental, vision, pharmacy (PBM), and behavioral claims with their own code sets and edit libraries
- **Automation-posture variants** — AI-assisted clearing with reviewer routing, prevention-first network gateway editing, predominantly manual examination
- **Delegated operation** — vendor staff run the machinery on the plan's behalf
- **Historical and regional realizations** — paper-era examination departments, mainframe adjudication engines, state-run program machinery, and non-US statutory insurers' bill-review operations all realize the same core with different machinery (the non-US fit is an inferred abstraction; the researched sample is US-shaped)

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Health Plan Administration System | system of record vs machinery | the administration system holds the plan's member, eligibility, benefit-plan, premium, and obligation record ("who is covered, under what rules, what has the plan owed and paid"); claims processing runs the operations that produce and change those obligations (intake → edit → adjudicate → pay → adjust). In bundled products the machinery sits inside the system of record; the centers remain distinct |
| Provider Claims Management | opposite seat on the same claim | provider-side claim production and submission management vs payer-side determination and settlement |
| Healthcare Revenue Cycle Management | opposite side of the financial flow | provider-side revenue machinery (from charge capture to post-payment follow-up) vs payer-side obligation machinery |
| Medical Coding Platform | upstream producer | coding produces the coded service lines; claims processing evaluates the coded request. Expert coding review appears here only as a review function |
| Prior Authorization Platform / Utilization Management | input discipline | authorization status is an adjudication input; the review machinery (medical necessity, review determinations) is its own discipline |
| Payment Integrity / FWA solutions | separable programs | preventive pre-adjudication editing and corrective post-payment review are realized as adjacent products and services; the machinery consumes their outputs |
| EDI Platform / Clearinghouse | transport vs determination | transaction routing and validation vs obligation determination; a gateway may validate claims before they enter the machinery but never determines or settles them |
| Insurance Claims Management (P&C) | same family, different object | property & casualty claims center on loss events and adjuster investigation against policies; payer claims center on coded health service lines adjudicated against benefit rulebooks and fee schedules |
| Claims Adjuster Platform | different discipline | the P&C adjuster's investigation workbench vs the payer's examination and determination machinery; no loss-investigation loop exists here |
| Public Benefits Management | government-operated variant | state-run program claims machinery is the government-operated realization of similar machinery; this Type remains payer-side regardless of who funds the plan |

The boundary that matters most within healthcare is the **machinery vs system of record** seam with the health plan administration system: the administration system is what the plan knows (who is covered, under what rules, what has been owed and paid); claims processing is what the plan's claims operation does about requests for payment against that record. Market packaging blurs the seam — full cores bundle both — which is precisely why the two Types are documented separately.

## Representative Products

- **HealthAxis (HealthOS CAPS)** — AI-native bundled core administrative processing posture: claims adjudication, eligibility, and provider management on one shared record; claims workspace independently deployable; Medicare/Medicaid/commercial/TPA poles
- **Availity** — the connectivity/gateway pole: national claim-transaction network with pre-adjudication claim editing delivered before claims enter the plan's processing environment (boundary anchor for the intake and edit layers)
- **Zelis** — the payer-side claims cost-management services pole: claims editing, expert bill review, DRG validation, claims pricing, and payment delivery on behalf of payers and TPAs (boundary anchor for the edit, pricing, and payment-integrity layers)

Widely cited market participants whose documentation could not be reached during this research — HealthEdge (HealthRules Payer), Cognizant TriZetto (Facets/QNXT), Pega — are recorded in the research notes as market anchors without product-specific claims.

## Sources

Research date: **2026-09-08**

- HealthAxis — HealthOS CAPS: https://healthaxis.com/healthos/caps ; HealthOS Plan: https://healthaxis.com/healthos/plan
- Availity — homepage: https://www.availity.com ; Payment Accuracy: https://www.availity.com/payment-accuracy/
- Zelis — homepage: https://www.zelis.com ; Payment Integrity: https://www.zelis.com/solutions/payment-integrity/
- X12 (standards body) — Transaction Sets and code lists: https://x12.org/products/transaction-sets (official definitions of the health care claim, payment/remittance, status, review, and coordination transactions, and of the claim status and claim adjustment code vocabularies)

Boundary-consistency context: the paired research notes and processed documents for health-plan-administration-system and payer-care-management (the §22 sibling passes whose boundary flags this pass discharges).

> Sourcing limitation: the two dominant legacy claims engines (TriZetto Facets/QNXT, HealthEdge HealthRules Payer), the BPM-based claims-processing pole (Pega), and Optum/Change Healthcare payment-management pages were not reachable from the research environment (access errors across two research passes). The canonical description therefore rests on the reachable sample above plus cross-pass context from the sibling healthcare leaves, and precision-dependent details — specific determination state sets, turnaround-time and payment-timeliness rules, interest provisions, and numeric limits — are intentionally not stated. Where the claim lifecycle, rule layers, and adjustment machinery are described, they are described conceptually; the standardized transaction names cited are those of the X12 standards body's own public documentation.

Detailed evidence, product-by-product observations, cross-product comparison, and the historical / market-sample check are recorded in the paired Research Notes.
