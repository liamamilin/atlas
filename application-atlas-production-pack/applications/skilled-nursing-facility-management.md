# Skilled Nursing Facility Management

## Overview

A **Skilled Nursing Facility Management** system is the facility's business-operations system of record. It holds the facility's resident population as persistent census state, generates and manages the money that the census produces under each resident's payer or funding category, and runs the recurring assessment-and-reporting cycle that determines payment levels and satisfies regulator obligations.

The defining core is three structures held together:

```text
Census of record
└── Census-driven payer money path
    └── Reimbursement-coupled assessment & compliance cycle
```

The resident clinical record — care plans, point-of-care documentation, medication administration — is the sibling Long-term Care EHR core. US platforms commonly bundle both cores in one product, but the clinical record is not what makes this Type: the money path can be delivered without any clinical record (as an outsourced billing operation), and the clinical record can exist without the payer machinery (as in UK-style care home software).

## Users & Context

The primary users are the facility's administrative and business staff, not care-delivery staff:

- **administrator / executive director** — watches occupancy, payer mix, and financial health; the census and receivables dashboards are their daily surface
- **business office / billing staff** — generate claims and invoices by payer category, work receivables, handle denials and appeals, manage resident trust funds
- **admissions / referral coordinator** — converts hospital referrals into admissions and validates insurance coverage before the resident enters the census
- **assessment coordinator** (in US facilities, the MDS coordinator role) — runs the recurring structured assessments that drive payment level and regulator reporting
- **regional / multi-facility managers** — oversee chains of facilities through consolidated census, financial, and quality views

Secondary users include directors of nursing (staffing and compliance surfaces), staff schedulers, and accountants using the facility's general-ledger and payables functions.

The work context is a licensed 24/7 nursing facility whose revenue arrives largely from public payers on a per-day basis (in the US, Medicare and Medicaid). The system's economics follow the census: every resident-day under a payer category is billable business.

## Core Model

### The Defining Core

**1. The census of record.** The facility's resident population held as persistent census state over time: who is admitted, admitted-when, discharged or transferred-when, which bed or unit they occupy, and — critically — each resident's payer or funding category. Occupancy and bed state are derived from it. The census is the master operational object; every other structure hangs off it. Without it, the product is an admissions tracker or bed board with no population memory.

**2. The census-driven payer money path.** Billing and receivables generated from census days under each resident's payer category: per-diem claims or invoices to public payers, managed care, and private payers; coverage and authorization tracking; denial and appeal handling; receivables managed through to collection. Without it, the product is a census tracker with no economics — or, if the census is absent too, generic healthcare claims processing.

**3. The reimbursement-coupled assessment & compliance cycle.** The recurring structured assessments and regulator reporting bound to the census that determine payment level and satisfy reporting obligations. In the US this is realized as the case-mix assessment cycle (the MDS instrument) driving payment under the current payment model, plus staffing-hour and quality reporting. Without it, the product is generic billing with no skilled-care payment coupling.

The three structures are jointly load-bearing:

```text
census alone                          → occupancy/bed board
money path without census             → generic healthcare billing/RCM
assessment cycle without the others   → compliance reporting utility
census + money, no assessment cycle   → lodging-style per-diem billing
census + assessments, no money path   → census with no economics
money + assessments, no census        → payer-side claims processing
```

### One Structure, Many Regimes

The core is written in funding-regime-neutral terms. The dominant market realization is US-shaped, but the concepts instantiate elsewhere:

```text
Concept:      payer/funding category on each resident
US form:      Medicare / Medicaid / managed care / private / resident-liability categories
UK form:      local-authority funding, private fees, self-funders (where surfaced)

Concept:      reimbursement-coupled assessment cycle
US form:      the recurring case-mix assessment instrument driving per-diem payment level
UK form:      regulator-evidence machinery (inspection-readiness records) rather than payment-driving assessments

Concept:      census-day billing
US form:      per-diem claims to public payers
Other forms:  periodic invoicing to funding authorities or private payers
```

### Standard Capabilities (Common in Mature Products)

These are widespread in mature products but do not define the Type:

- **bundled clinical record** — care plans, point-of-care documentation, medication administration record; universal in US software suites, absent where the money path is delivered as a standalone service
- **resident trust funds** — resident personal funds held in custody with transaction records (US-common)
- **general ledger / accounts payable / multi-facility accounting** — the facility's books inside the same system
- **payroll and staff scheduling** — including staffing-need forecasting
- **referral / admissions pipeline** — CRM-shaped intake from hospitals
- **analytics dashboards** — census, receivables, quality, readmissions
- **interoperability** — exchange with hospitals, pharmacies, and labs

## How It Works

### The money loop (the defining workflow)

```text
Referral received (commonly from a hospital discharge)
→ admission: resident enters the census with a payer/funding category
→ coverage/insurance validated
→ census days accumulate under that payer category
→ billing run: claims/invoices generated per payer category's rules
→ claims submitted, tracked; payments posted to receivables
→ denials identified → appeals pursued
→ receivables worked to collection; month-end close over census + AR
```

The census day is the unit of economic time. Everything in the money path keys off it: what is billed, to whom, at what rate basis, and what remains collectable.

### The assessment & compliance cycle

```text
Recurring assessment schedule per resident
→ structured assessment completed (assessment coordinator)
→ assessment drives the payment level for that resident's stay
→ regulator reporting generated from census + assessment + staffing data
→ submission tracked; changes in the payment model handled as system updates
```

The assessment is the shared object on the seam with the clinical record: its content is clinical, but its role in this Type is payment-driving and regulator-facing.

### Occupancy management

```text
Current census and bed state
→ projected discharges and admissions
→ referral pipeline worked to fill open capacity
→ occupancy and payer-mix watched as the facility's headline economics
```

### Capability tiers

**Defining core** — census of record; census-driven payer money path; reimbursement-coupled assessment & compliance cycle.

**Standard capabilities** — bundled clinical record; trust funds; GL/AP and accounting; payroll/scheduling; referral pipeline; analytics; interoperability.

**Variant / optional** — ancillary and therapy management; dining/nutrition; resident engagement; retail; AI insight layers (predictive staffing, payment coaching); outsourced delivery of the money path as a managed service.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Census / occupancy dashboard

The operator's headline surface.

- current census, occupancy, bed state, payer mix, admissions/discharges in flight
- primary actions: review status, drill into a resident's census and billing standing, watch projected capacity

### Billing / receivables worklist

The business office's primary surface.

- claims and invoices by payer category, payment postings, aging receivables, denials and appeals in progress
- primary actions: generate/submit claims, post payments, work denials, appeal, adjust

### Assessment workbench

The assessment coordinator's surface.

- assessment schedule per resident, due/overdue state, completion status, submission tracking
- primary actions: complete or review an assessment, track its payment impact, generate regulator reporting

### Referral / admissions pipeline

The intake surface.

- incoming referrals (commonly hospital-originated), status through evaluation to admission, insurance validation
- primary actions: accept/reject referral, schedule admission, validate coverage

### Financial / accounting surfaces

- general ledger, accounts payable, multi-facility consolidation, trust-fund ledgers
- primary actions: post, reconcile, close period, report

### Analytics

- census trends, AR health, quality measures, readmissions, staffing levels
- primary actions: review, compare facilities, export

## Important Rules / Behaviors

- **The census day is the unit of economic time.** Billing, receivables, and payment levels all key off resident-days under a payer category — not off encounters or visits.
- **Payer category governs the money path.** Each resident's funding category determines what is billed, to whom, on what basis, and under which rules. A change in payer category (e.g., a stay segment covered by a different payer) changes the billing path.
- **Assessment determines payment level.** In case-mix regimes, the recurring structured assessment is not merely compliance paperwork — it sets the payment level for the resident's stay. Missed or late assessments have direct revenue consequences.
- **Coverage is validated before the census commitment.** Admissions workflows commonly include insurance/coverage validation as a gate before or at admission.
- **Trust funds are custody money.** Resident personal funds held by the facility are tracked as segregated ledgers with transaction-level records (US-common; a compliance-sensitive surface).
- **The clinical record is a sibling core, not this Type's definition.** Where bundled, the management system consumes clinical events (e.g., assessment content) but its own record of record is the census and the money path.

## Variants

- **US Medicare/Medicaid per-diem regime** — the dominant realization: per-diem claims, case-mix assessment machinery, staffing-hour and quality reporting, consolidated-billing-style rules
- **UK / regional care home analog** — record-led: care record plus operations tooling plus regulator-evidence machinery (inspection readiness), with funding/invoicing thin or absent from the product surface; sits closer to the Long-term Care EHR territory
- **fully private-pay markets** — census + invoicing without public-payer claims machinery
- **single facility vs multi-facility chains** — the chain form adds consolidated accounting and portfolio-level census/quality views
- **software vs outsourced revenue-cycle services** — the money path delivered as a managed operation (central business office services) rather than software; strong evidence that the payer-driven revenue cycle is a defining leg independent of any clinical record

## Related Application Types

| Application Type | Distinction |
|---|---|
| Long-term Care EHR | the resident-centered clinical record of record (standing record, care-plan loop, shift documentation, medication administration); US platforms bundle both cores in one product, but the seam is record-of-record vs operations-of-record |
| Healthcare Revenue Cycle Management | processes claims for providers generally, without holding a facility's census, occupancy, or payer-mix state; a claims engine without the census is RCM territory |
| Hospital Management / Bed & Capacity Management | encounter-driven acute flow (admit→discharge→transfer throughput); the SNF census is long-stay, per-diem, payer-categorized, and coupled to case-mix assessment — different unit of economic time |
| Practice Management System | ambulatory scheduling and fee-for-service billing around encounters; no facility census, no per-diem public-payer machinery |
| Home Health EHR / Management | care delivered per-visit in the patient's own home vs a facility residency |
| Hospice Management | a care program vs a facility population |
| Employee Scheduling / Payroll | staffing is a common module here (and a regulatory reporting input in the US), but staffing products lack census, money path, and assessment machinery |
| Senior Living operations | private-pay, services/hospitality-shaped operations vs payer-driven skilled care |

The most important boundary is with the Long-term Care EHR: the two Types overlap in one bundled product across the US market, and the recurring assessment instrument is the shared object on the seam — clinical content inside the EHR, payment-driving compliance object inside the management system.

## Representative Products

- PointClickCare (EHR for SNF platform + billing/referral/PDPM add-ons)
- MatrixCare Skilled Nursing
- WellSky Long-Term Care (platform) and WellSky Revenue Cycle Services (the outsourced-services pole)
- Person Centred Software (UK care home analog — the record-led regional pole)

## Sources

Research date: **2026-09-09**

- PointClickCare — Products hub: https://pointclickcare.com/products/ ; EHR for Skilled Nursing Facilities: https://pointclickcare.com/products/skilled-nursing-platform/
- MatrixCare — Skilled Nursing Software: https://www.matrixcare.com/skilled-nursing-software/
- WellSky — Long-Term Care: https://wellsky.com/long-term-care/ ; Revenue Cycle Services for Skilled Nursing: https://wellsky.com/services/revenue-cycle-services/skilled-nursing/
- Person Centred Software — https://www.personcentredsoftware.com/

> Sourcing limitation: all reachable evidence is official product/marketing pages (Tier-2). Vendor help centers are login-gated and no operational user guides or billing manuals were reachable. Precise operational facts (claim submission windows, billing-cycle mechanics, payment-model rates, month-end close rules, numeric limits) are deliberately not stated in this document. Two additional candidate products (a legacy finance-led vendor and a UK invoicing-focused product) were unreachable and are recorded in the Research Notes as a sampling limitation; assertions are calibrated to the four-product reachable sample.
