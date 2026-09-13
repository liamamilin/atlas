# Health Plan Administration System

## Overview

A **Health Plan Administration System** is the health plan's (payer's) operating system of record: it holds the plan's enrolled population and their coverage, administers enrollment and eligibility, keeps each benefit product as a configured rulebook, determines what the plan owes for the care its members receive, and settles those obligations — while carrying the plan's premium administration and regulatory posture.

Its defining core is small:

```text
Member & Coverage of Record
└── Enrollment & Eligibility Administration
    └── Benefit Plan Configuration (the plan's rulebook)
        └── Benefit Execution & Settlement (what the plan owes, claimed and paid)
```

Everything else commonly associated with payer software — premium billing, provider and member portals, claims-operations depth, utilization management, appeals and grievances, government file exchanges, care management — is standard mature structure or variant machinery, not what makes the system a health plan administration system. Market names for this Type include *core administrative processing system (CAPS)* and *core administration system (CAS)*.

## Users & Context

The primary users are the health plan's own operations staff:

- **enrollment and eligibility processors** — turn applications, employer files, and government eligibility files into effective-dated member coverage, and keep it current
- **claims examiners and benefit processors** — work the plan's obligation determination and settlement (where the adjudication engine is part of the system)
- **benefit configuration analysts** — maintain the plan's products: coverage rules, cost sharing, network applicability
- **billing and reconciliation staff** — run premium invoicing, payments, and account reconciliation (where premiums exist)
- **member services representatives** — answer coverage, benefit, and account questions using the member's record
- **compliance and audit roles** — regulatory reporting, file exchanges, appeals and grievances oversight

Two external user groups face the same record through portals: **members** (coverage, costs, payments, changes) and **provider office staff** (eligibility verification, claim submission, authorization status).

The operating context is high-volume, regulation-heavy administration: commercial carriers, regional plans, Medicare Advantage and Part D plans, Medicaid managed-care plans, third-party administrators (TPAs) running self-funded employer plans, dental and vision carriers, and provider-sponsored plans all run this machinery.

## Core Model

### The Defining Core

```text
Member & Coverage of Record
└── Enrollment & Eligibility Administration
    └── Benefit Plan Configuration
        └── Benefit Execution & Settlement
```

Four structures. If any one is removed, the product is no longer recognizable as a health plan administration system:

- **Member & coverage of record** — every covered person is an individually identified member (a subscriber with dependents under a group master contract, or an individual enrollee) carrying effective-dated coverage under one of the plan's benefit products. The member — not the contract document — is the anchor: coverage is continuous across plan years, segmented by effective dates, and every change is tracked against the same person. Without this, the product is a transaction processor with no population.
- **Enrollment & eligibility administration** — membership is never static. Coverage is established, changed, and ended through recorded enrollment events (member applications and elections, employer eligibility files, government eligibility files), each validated against eligibility rules and enrollment windows, producing effective-dated eligibility segments. Current eligibility is continuously answerable in real time — to plan staff, to providers, and to members. Without this, the record is a static roster.
- **Benefit plan configuration** — each of the plan's products exists in the system as an operative rulebook: which services are covered, at what member cost (service-level amounts, periodic thresholds the member must meet, network-tier rules), what requires prior authorization, and for which effective period. Plans are versioned and configurable by business staff, not hard-coded. Without this, the system holds members but no benefit semantics.
- **Benefit execution & settlement** — when care is received, the plan's obligation is determined by applying the benefit rulebook to the service — checking eligibility as of the date of service, applying cost sharing and network rules, respecting authorization status — and settled by payment to the provider (or reimbursement to the member), with the results accumulated back onto the member's record. This is what makes the system the administration of a *plan* rather than an eligibility registry. Whether the adjudication engine is built into the system or the system orchestrates a connected claims platform is a packaging choice, not a definitional difference.

Premium administration is deliberately **not** part of the defining core: Medicare Advantage plans collect premiums from government rather than from members, and TPAs administering self-funded employers collect none at all — yet all operate the same core.

### Standard Capabilities of Mature Products

Mature products commonly carry most of the following. They make health plan administration practical; they do not define the Type.

- **Premium billing & receivables** — invoicing for individual and group accounts, configurable billing cycles, remittance models, government payment files integrated into balances, reconciliation, and delinquency handling
- **Provider data & settlement seam** — a provider master with directories; a provider portal for claim submission, eligibility verification, and authorization management; remittance outputs to providers
- **Claims-operations machinery** — intake, editing, repricing, coordination of benefits, adjustments, and payment-integrity hooks (in products where adjudication is bundled)
- **Utilization-management linkage** — prior authorizations captured or received, and honored as adjudication inputs; UM suites often ship as separate products
- **Appeals & grievances** — tracked end-to-end with regulatory-compliance workflows, deepest in government-program products
- **Member servicing** — member portal (coverage, balances, payments, change requests), ID cards and welcome materials, correspondence templates, customer-service case management
- **Regulatory transaction machinery** — standardized enrollment, eligibility, claim, and payment transactions; automated government file submission and import; encounter data submission; audit readiness
- **Financial reconciliation** — premiums, payments, and government files reconciled against balances
- **Document generation** — plan materials, explanation documents, letters
- **Configuration, roles, audit** — no-code configuration of benefit rules, plan designs, and workflows; role-based access; audit trails
- **Reporting, analytics, integrations** — membership/claims/financial reporting; standards-based APIs
- **Pharmacy benefit linkage** — formulary configuration and PBM integration
- **Clinical-suite adjacency** — care management, quality, and risk-adjustment suites sometimes bundled, often separate products

### One Structure, Many Implementations

The core model is written conceptually. Implementations vary:

```text
Concept: Covered population
Implementations:  group subscribers + dependents, individual enrollees,
                  government-program beneficiaries

Concept: Enrollment event
Implementations:  employer eligibility/census files, marketplace or government
                  eligibility files, member applications/elections (electronic
                  or paper), TPA onboarding of employer groups

Concept: Eligibility answer
Implementations:  electronic inquiry/response transactions, portal lookups,
                  API calls, call-center scripts over the same record

Concept: Benefit rulebook
Implementations:  benefit package tables, plan-year versions,
                  network-tiered cost sharing, riders and carve-outs

Concept: Obligation determination & settlement
Implementations:  integrated adjudication engine, connected claims platform,
                  manual examination queues for exceptions
```

A reader who has only seen one implementation — for example a fully bundled claims-included core — should still be able to recognize a modular deployment that runs a separate claims engine, or a government-program plan with no member premium, from the same core model.

## How It Works

### Establish coverage (the enrollment flow)

```text
Enrollment event arrives
  (member application / employer eligibility file / government eligibility file)
→ validate and check eligibility rules and enrollment windows
→ determine eligibility and the applicable benefit product
→ create the member's coverage segment with effective dates
→ issue identifiers and materials (member ID, welcome kit)
→ downstream activation: billing, directories, servicing
```

Coverage never "just appears": every segment traces to a recorded event, a determination, and an effective date.

### Keep eligibility current (the maintenance loop)

```text
Change event
  (life event, address change, premium adjustment, plan transfer, disenrollment)
→ re-validate against eligibility rules and permitted change windows
→ re-determine eligibility; close the old segment, open the new one
→ propagate: billing, provider directories, member materials
```

In parallel, the standing question — "is this person covered, for what, as of this date?" — is answered in real time to providers, members, and internal users. Mature products automate a large share of these transactions without human touch; vendor claims about exact automation rates vary and are not asserted here.

### Execute benefits (claim to settlement)

```text
Care received
→ claim/encounter arrives (from provider, member, or another payer)
→ validate member eligibility as of the date of service
→ apply the benefit rulebook: coverage, cost sharing, network rules,
  accumulated amounts, authorization status
→ determine the plan's obligation and the member's responsibility
→ settle: pay provider / reimburse member / communicate the decision
→ accumulate results back onto the member's record
```

This loop is the economic heart of the Type. In bundled products it runs inside the same system; in modular deployments the administration system hands the claim to a connected claims platform and receives the outcome — but the obligation determination and settlement remain the plan's record.

### Collect premiums (where they exist)

```text
Billing cycle
→ calculate premiums (individual and/or group accounts, subsidies, government rates)
→ invoice; receive payments and government files
→ reconcile balances; handle shortfalls and adjustments
```

### Stay compliant (the regulatory loop)

Government-program and regulated-market products continuously exchange standardized files — enrollment and disenrollment, eligibility, encounter data, payments — with regulators and exchange administrators, track appeals and grievances under compliance workflows, and keep the record audit-ready. The depth of this machinery varies by regime; its presence is a market constant.

### Core vs Common vs Optional

**Defining core** — without these, not a health plan administration system:

- member & coverage of record
- enrollment & eligibility administration (including real-time eligibility answers)
- benefit plan configuration
- benefit execution & settlement

**Standard mature structure** — present in most current products:

- premium billing & receivables (where premiums exist)
- provider portal & provider data management
- claims-operations machinery depth
- UM / prior-authorization linkage
- appeals & grievances
- member portal & servicing case management
- regulatory transaction machinery & reconciliation
- document generation, configuration tooling, roles & audit, reporting, integrations, pharmacy linkage

**Variant / optional** — depends on segment, regime, and packaging:

- government-program machinery depth (election periods, government file exchanges, encounter data, audit posture)
- individual-market machinery (shopping/quote/enroll, subsidies, open enrollment, retention)
- TPA/self-funded posture (no premiums, employer-funded)
- dental/vision/behavioral line shaping; pharmacy carve-in/carve-out
- bundled care/quality/risk-adjustment suites
- delivery posture (software license vs the vendor running the operation as a service)

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Enrollment & eligibility workbench

The operations staff's primary surface for the enrollment flow.

- work queues of incoming applications and files, validation errors, pending determinations
- primary actions: validate, determine eligibility, activate/terminate coverage segments, generate member materials

### Member record ("member 360")

The single view of one member's world.

- demographics, identifiers, coverage segments and their effective dates, benefit product, accumulated amounts, claims and payments history, documents, service cases
- primary actions: process a change, correct data, view eligibility, generate correspondence

### Claims / benefit execution workspace

Where obligation determination happens (in bundled products) or where connected-claim outcomes are examined.

- claim detail, member eligibility snapshot at service date, benefit-rule application results, authorizations, payment/remittance status, adjustment paths
- primary actions: examine, apply/correct rules decisions, approve payment, adjust, correspond

### Billing & receivables

- account lists by individual/group, invoices, payment and government-file postings, balances, reconciliation status
- primary actions: run billing cycle, post payment, reconcile, adjust

### Configuration console

- benefit products, plan versions, coverage and cost-sharing rules, network tiers, workflow and letter templates
- primary actions: configure, version, deploy; typically usable by business staff without IT involvement in mature products

### Member portal

Self-service face of the same record.

- coverage and benefits, costs and balances, claims history, ID card, payments (one-time and recurring), change requests
- primary actions: view, pay, request changes

### Provider portal

- eligibility verification, claim submission and status, authorization submission and management, remittances
- primary actions: verify, submit, track

### Transaction & file exchange surfaces

- batch interfaces for standardized enrollment/claim/payment transactions, government file submission and import, API endpoints
- primary actions: monitor, resubmit, reconcile

### Reporting & compliance dashboards

- membership, claims, financial, and regulatory-compliance views; audit extracts

## Important Rules / Behaviors

### Everything is effective-dated

Coverage segments, benefit products, and plan versions all carry effective dates, and the system can show the member's coverage and benefit terms as they stood at any point in time. Retroactive and future-dated changes are normal operations, not exceptions.

### Eligibility at service time governs

Benefit execution checks the member's eligibility as of the date the care was received, not merely today's status. A member can be enrolled today and still have a claim adjudicated against an earlier (or later) coverage segment.

### Enrollment windows gate changes

Coverage can generally begin or change only within permitted enrollment periods — new-hire and open-enrollment windows for group business, qualifying life events for individuals, defined election periods for government programs. Validating the window is part of validating the event.

### Changes preserve continuity

A change closes one coverage segment and opens another against the same member; disenrollment ends coverage but does not erase the member. Continuity of coverage across plan transitions is an explicit design concern in the individual and government markets.

### Authorization status is an adjudication input

Where a service requires prior authorization, the authorization record participates in the obligation determination. Authorization capture may live in the administration system or in a connected UM product; the check itself sits in the execution path.

### Regulatory timeliness and auditability shape operations

Government-program plans operate under prescriptive file-exchange and timeliness regimes; products in this segment automate daily submission/import cycles, track appeals and grievances under compliance workflows, and treat "reportable field" coverage and audit readiness as first-class features. The specific regimes vary by program; the operational posture is common.

### One record, many readers

Portals, call-center tools, adjudication, billing, and UM all read the same member and benefit record. Vendors stress the "single source of truth" posture precisely because divided records are the classic failure mode of this software.

## Variants

- **Bundled full core (CAPS posture)** — claims adjudication, enrollment, provider management, and financial coordination consolidated in one system; the classic "core administration" architecture
- **Modular suites around separate cores** — market-side suites (enrollment, member maintenance, billing, reconciliation, portals) and care-side suites (UM, care, quality) running beside a claims core; common where plans modernize one layer at a time
- **Government-program pole** — Medicare Advantage / Part D and Medicaid managed-care machinery: election periods, government file exchanges, payment-file integration, encounter data, audit posture
- **Individual-market pole** — marketplace/exchange shopping, quoting, enrollment, subsidy handling, billing, and renewal/retention machinery
- **Commercial group pole** — employer eligibility feeds, group master contracts, group billing
- **TPA / self-funded (ASO) posture** — the same machinery run on behalf of self-funded employers; no premiums, employer-funded obligations
- **Provider-sponsored plans (payvider)** — provider organizations operating plans on the same administrative machinery
- **Line shaping** — dental, vision, behavioral, pharmacy-specific deployments
- **Regional regimes** — outside the US-shaped sample, statutory-fund and national-insurance administrations realize the same core with different eligibility and settlement mechanics (lower-confidence variant, inferred)
- **EHR-adjacent platform-native** — administration delivered inside an EHR vendor's ecosystem (documented as a market variant; vendor documentation was not reachable in this research)
- **Operations-as-a-service** — the vendor runs enrollment/billing/claims operations on the platform rather than licensing software alone

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Insurance Policy Administration System | same family (health instantiation) | policy admin centers the *contract* lifecycle (issue → endorse → renew → cancel as effective-dated transactions on a policy); health plan administration centers the *member population and benefit execution* (enrollment events, eligibility segments, benefit rulebooks) |
| Payer Claims Processing | execution seam | claims processing is the adjudication *machinery* (intake → edit → adjudicate → pay → adjust), whether embedded in a full core or shipped standalone; health plan administration is the system of record for members, eligibility, benefit plans, premiums, and the plan's obligations |
| Benefits Administration Platform | employer-side counterpart | the employer system holds the plan catalog and elections and hands off effectuation (enrollment files) to the carrier; this Type receives and administers the resulting membership |
| Provider Network Management | adjacent, provider-side | contracting, credentialing, fee schedules, and network adequacy machinery vs the administration core's provider master and settlement seam |
| Utilization Management / Prior Authorization Platform | adjacent, clinical gate | clinical-review machinery; authorization status feeds benefit execution, but the review process is a separate discipline and often a separate product |
| Payer Care Management | adjacent, clinical layer | care plans, quality measures, risk adjustment — the clinical-program layer above the administration record; no enrollment/premium/claims of record |
| Healthcare Revenue Cycle Management / Provider Claims Management | opposite side of the claim | provider-side billing and submission vs payer-side obligation determination and settlement |
| Patient Portal | surface | generic patient-facing portal; the member portal here is a servicing surface of the administration record |
| Public Benefits Management | government-agency-side | agency-run benefit programs; state-run Medicaid systems are the government-operated variant of similar machinery, while health plan administration stays insurance-side |
| Pension Administration Platform | structural neighbor | both are governed member registries with rule-based benefits and payment runs; pension entitlement accrues from scheme participation, health coverage is event-driven enrollment with per-service obligation determination |

The boundary that matters most within healthcare is the **system of record vs processing machinery** seam: this Type is what the plan knows (who is covered, under what rules, what it has owed and paid); the claims, UM, and care Types are what the plan does operationally on top of that record.

## Representative Products

- **HealthAxis (AxisCore)** — cloud-native core administrative processing system for health plans and TPAs; the bundled-CAPS posture (adjudication, enrollment, provider management, financial coordination in one core)
- **MHK (MedHOK — MarketProminence / CareProminence)** — modular payer suites with Medicare Advantage / Part D depth; the modular posture around existing claims cores
- **Softheon (ACA Marketplace Cloud / All-in-One)** — individual-market health plan operations: shopping, enrollment, billing, renewals across ACA, ICHRA, and Medicare Advantage
- **Medecision** — payer-side care, utilization-management, quality, and risk platform; included as the boundary anchor for the clinical-program layer adjacent to this Type
- **DXC Technology (payer services)** — services vendor whose "Core Administration System" modernization practice independently documents the market category and the long-lived legacy-core reality

The dominant legacy core platforms (TriZetto QNXT/Facets) and the leading cloud challenger (HealthEdge) are widely cited market anchors; their documentation was not reachable during this research, and no product-specific claims about them are made here.

## Sources

Research date: **2026-09-08**

- HealthAxis — homepage, AxisCore product page, platform capabilities: https://healthaxis.com/ , https://healthaxis.com/our-solutions/axis-core , https://healthaxis.com/platform-capabilities
- MHK (MedHOK) — homepage, Enrollment & Member Maintenance, Premium Billing: https://mhk.com/ , https://mhk.com/solutions/mhk-marketprominence/enrollment-member-maintenance/ , https://mhk.com/solutions/mhk-marketprominence/premium-billing/
- Softheon — homepage and For-Health-Plans navigation: https://www.softheon.com/
- Medecision — homepage: https://www.medecision.com/
- DXC Technology — Healthcare industry page: https://www.dxc.com/us/en/industries/healthcare

Boundary-consistency context: the paired research notes for insurance-policy-administration-system (family seam and group/health scope evidence), and the processed documents for benefits-administration-platform, pension-administration-platform, and electronic-health-record-ehr.

> Sourcing limitation: several major vendors' documentation could not be fetched during this research (TriZetto QNXT/Facets and HealthEdge returned access errors; Epic, Conduent, Gainwell, and official Medicaid MMIS pages were unreachable or blocked). The canonical description therefore rests on the reachable sample above plus cross-family context. Precision-dependent details — exact cost-sharing mechanics such as accumulator rules, specific transaction identifiers, response-time guarantees, and any numeric limits — are intentionally not stated; where cost sharing and automation are described, they are described conceptually.
