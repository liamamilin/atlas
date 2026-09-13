# Progress Billing

## Overview

A **Progress Billing** application manages the recurring billing cycle on a construction contract: the periodic, cumulative billing document — commonly called a pay application, progress billing, progress claim, or application for payment — through which a performing party bills the paying party for work completed to date.

On a construction contract, money is not owed per delivery; it is earned gradually as the work progresses. Each billing period, the contractor (or subcontractor) prepares an application that states how much of the contract's value has been earned so far, deducts everything already billed on previous applications, withholds the contract's retainage, and submits the result to the paying party — who reviews it, often line by line, rejects or accepts it, and certifies the amount that becomes payable. This application is the system of record for that cycle: the series of billing documents, the computation behind each one, and the back-and-forth that turns a claim of earned value into a certified, payable amount.

Its boundary: it is not the contract record itself (that is contract administration), not the change-order process (though it bills approved changes), not generic invoicing (the amount due is computed from contract progress, not stated per transaction), and not collections (which begin after certification).

## Users & Context

Progress billing is inherently two-sided, and the same cycle runs at every tier of a construction project — a subcontractor bills the general contractor, the general contractor bills the owner, and each party sits on the billing side of one cycle and the reviewing side of another.

Primary users:

- **Project accountants, billing specialists, and A/R staff** (contractors and subcontractors) — prepare each period's pay application: enter completed work against the payment breakdown, attach backup, submit, and chase revisions; the day-to-day operators of the cycle.
- **Project managers** — supply the completion figures for their scope, review billing values before submission, and track unapproved change orders that are not yet billable.
- **Reviewing-party staff** — owner's representatives, owner project accountants, and construction-manager accounting teams who receive applications, review them against the work and the contract's terms, reject or approve line items, and certify the amount to be paid.
- **Controllers and CFOs** — oversee billing accuracy, billing health (billed vs unbilled, over/under-billing), and cash-flow forecasts built from the billing pipeline.
- **Subcontractors and vendors** — external parties who submit their own pay applications through portals, or whose paper applications are entered on their behalf by the receiving party.

The setting is commercial, industrial, infrastructure, and public construction, with lighter-weight variants among residential builders and trade contractors. The work is characteristically monthly, tied to contract-defined billing periods, and deadline-driven — a late or rejected application directly delays payment.

## Core Model

### The Defining Core

The application is built on three properties. Remove any one and what remains is no longer progress billing:

- **The pay application as unit of record.** Each billing cycle produces a numbered, dated application document bound to a specific contract and to a billing period. The applications form a series that spans the contract's life — application one, two, three… through the final account — and each one remains on the record after it is paid. Without the recurring document series, there is no billing cycle to manage.
- **Cumulative, contract-anchored computation of the amount due.** The amount due is computed, not stated. The contract's payment breakdown — the schedule of values (line items with amounts, or quantities with unit prices) or, on cost-reimbursable work, the applicable rate schedule — is the arithmetic backbone. For each line, the application records work completed to date (entered as dollars, percentages, or measured quantities), adds billable items the contract allows (stored materials, approved change orders), subtracts the totals of all previous applications, and carries the contract's withholdings (retainage). Every application arithmetically continues the previous ones; the system, not the user, maintains the carry-over. Without this computation, the product is a generic invoice generator.
- **The two-party submission–review–certification cycle.** The billing party prepares and submits the application; the paying party (or its reviewing representative) examines it — characteristically line by line against the payment breakdown — and approves or rejects it; rejected items are corrected and resubmitted; the approved application becomes the certified, payable record. Both sides of this exchange are modeled in the system, with statuses, comments, and an audit trail. Without the counterparty's review and certification, there is submission but no billing cycle.

### Standard Capabilities

Around that core, mature products add the machinery that makes the cycle workable at construction scale:

- **Schedule of values management.** Building and maintaining the line-item payment breakdown (by cost code or trade); vendors may author the schedule of values for their own contracts; lines may be amount-based or unit/quantity-based.
- **Retainage machinery.** Withholding calculated per the contract's terms on each application, tracked separately (commonly split between retainage on completed work and on stored materials), and released through later applications or separate release invoices when contract conditions are met.
- **Stored materials billing.** Billing for materials delivered or stored but not yet installed, with supporting documentation and tracking as the materials are consumed.
- **Change-order incorporation.** Approved changes added to the payment breakdown and billed in the correct period, with warnings when a change is billed in the wrong period; unapproved changes tracked separately as not-yet-billable exposure.
- **Billing periods.** Configured periods per project — with start, end, and submission due dates — that gate when applications may be submitted; generated manually or automatically.
- **Compliance documents in the payment flow.** Lien waivers and insurance certificates collected alongside the application; missing or expired documents hold up review and payment.
- **Multi-party collaboration.** Portals where vendors submit their own applications; "invite to bill" flows; entry on behalf of parties who bill on paper; status notifications, comments, and revision tracking.
- **Form generation and export.** The application rendered in the form the receiving party requires — standardized industry forms (in North America, the AIA G702/G703 tradition), customer-specific forms reproduced digitally, or branded PDFs — with digital signatures where used.
- **Payment recording and status.** Payments issued and received recorded against applications; per-application status (submitted, in review, approved, paid, disputed); accruals and aging views.
- **ERP/accounting synchronization.** Certified billings exported or synced into corporate accounting — commonly only after approval, so that revisions never churn the general ledger.
- **Billing-health reporting.** Billed versus unbilled revenue, over/under-billing relative to costs, A/R aging, and cash-flow forecasts derived from the billing pipeline.

### One Structure, Many Implementations

The core is written conceptually; products realize it differently. The computation basis varies by contract type: a lump-sum contract bills percentages or dollars against schedule-of-values lines; a unit-price contract bills measured quantities against unit rates; time-and-materials or cost-plus work bills captured costs against contract rate schedules with markups — some suites even carry these bases in separate products. The document's name follows the speaker's seat and region: owner invoice (upstream), subcontractor invoice (downstream), progress billings (specialty-contractor seat), progress claim (Australian usage), application for payment, interim application. The structure underneath — recurring application, cumulative computation, counterparty certification — does not change.

## How It Works

### Set up billing on the contract

```text
Contract executed (with its payment terms)
→ Build the payment breakdown
    (schedule of values by cost code or trade; vendor may author their own)
→ Record the retainage terms
→ Establish billing periods (start, end, due date)
→ Grant submission rights (vendor self-service, or internal entry on their behalf)
```

The contract must be in effect before billing begins; products gate the first application on an approved contract or commitment.

### Run each billing period

```text
Billing period opens
→ Enter completed work per line
    (dollars, percentages, or measured quantities)
→ Add billable items: stored materials, approved change orders
→ System computes: completed to date
    − previous applications
    = amount due this period, less retainage withheld
→ Attach backup (lien waivers, compliance documents, quantity or timesheet support)
→ Submit to the paying party (portal, email, or required form)
```

The carry-over from previous applications is system-maintained: the user enters this period's progress, and the arithmetic of the series stays consistent.

### Review and certify

```text
Paying party reviews the application
    (characteristically line by line against the payment breakdown)
→ Reject items with comments → billing party revises and resubmits
→ Repeat until all lines are approved
→ Application certified/approved → becomes the payable record
→ Payment recorded against the application
```

Review is the counterparty's control point: the reviewer checks claimed completion against the work and the contract, and the revision loop continues until the amount is agreed.

### Close the contract's billing

```text
Work reaches completion
→ Final application (final account)
→ Release of remaining retainage
    (through the final application or a separate release invoice)
→ Billing series complete; certified history retained
```

### When the normal flow breaks

- **Rejected application** — line items come back with comments; the billing party corrects and resubmits; the revision trail is kept.
- **Unapproved change orders** — work performed under a not-yet-approved change is tracked as exposure but is not billable until the change is approved and lands in the correct period.
- **Missing compliance documents** — an absent lien waiver or expired insurance certificate holds up review; reminders flag it before it blocks payment.
- **Over-billing** — billing ahead of actual cost is visible (and sometimes necessary for cash flow), but it is a monitored exposure, not a hidden one.
- **Disputed amounts** — an application can sit in review or be marked disputed; the record keeps the submissions, comments, and evidence for resolution.

## Interfaces

The surfaces below are described conceptually; exact layout and naming vary by product.

### Billing register / home

The operator's entry surface: every pay application across projects and customers with its period, status, and amounts; filters by status, project, or party. Primary actions: open an application, create a new one for the open period, export.

### Pay application editor

The work surface for one application: the payment breakdown as a grid — line items with contract amounts, work completed this period and to date, stored materials, previously billed totals, and the computed amount due — plus retainage rows, change-order lines, and attachments of backup. Primary actions: enter progress, add stored materials or change orders, preview the required form, sign, submit.

### Review / approval surface

The receiving party's control surface: the submitted application with per-line approve/reject, comments, and the revision history; compliance documents checked alongside. Primary actions: review lines, reject with comments, approve, certify, record payment.

### Billing period configuration

Administrator controls: period calendar (start, end, due dates), automatic period generation, submission windows, numbering schemes.

### Compliance and lien waiver collection

The trust surface around payment: lien waivers (from the billing party and its lower tiers), insurance certificates, and other required documents, with status and reminders. Primary actions: request, collect, verify, attach.

### Reporting and dashboards

The management view: billed vs unbilled revenue, over/under-billing against costs, A/R aging of certified applications, retainage balances awaiting release, cash-flow forecasts from the billing pipeline.

## Important Rules / Behaviors

- **The series must stay arithmetically consistent.** Each application deducts all previous applications; the system maintains the cumulative totals, so a correction to one period propagates forward rather than silently diverging.
- **Billing follows an approved contract.** Applications are created against an executed contract or commitment; products gate the first application on approval.
- **Billing periods gate submission.** Applications belong to defined periods with due dates; billing outside the open period is prevented or warned.
- **Only approved changes are billable.** A change order enters the payment breakdown — and the next application — once approved; billing an unapproved change, or an approved one in the wrong period, is blocked or flagged.
- **Review is line-item granular.** The reviewer accepts or rejects individual lines; the application is approved only when all lines pass, and rejected lines return for revision.
- **Retainage follows the contract's terms.** The withheld portion is calculated per application, tracked across the series, and released only when the contract's conditions are met — commonly through a later application or a dedicated release invoice.
- **Compliance documents accompany the money.** Lien waivers and certificates are collected with the application; missing documents hold review and payment.
- **Certification creates the payable record.** The approved application — not the submitted one — is what syncs to accounting and what payment settles against; revisions before certification stay out of the general ledger.
- **Each application is private to its parties.** In multi-party products, a billing relationship is visible to its two parties, not the whole project.

## Variants

- **By billing basis.** Lump-sum contracts billed against schedule-of-values lines (percent or dollar entry); unit-price contracts billed on measured quantities; time-and-materials and cost-plus contracts billed from captured costs against contract rate schedules and markups; milestone or payment-schedule billing on defined events.
- **By operating seat.** General-contractor-side (billing the owner upstream while reviewing subcontractor bills downstream), owner-side (reviewing and certifying contractor applications), subcontractor-side (billing general contractors to each one's required forms and portals), specialty-contractor-side (the same cycle under the name "progress billings").
- **By regional form regime.** The North American AIA G702/G703 tradition; customer-specific forms reproduced digitally; statutory progress-claim regimes (for example Australia and New Zealand); UK-style interim applications. The document structure stays stable while the required forms and statutory rules vary.
- **By packaging.** A tool family inside a multi-party construction platform; a standalone billing module of a project-controls suite; a standalone billing product serving one side of the exchange (subcontractor-side or GC-side); a billing module inside a construction ERP; a finance feature of a small-contractor platform.
- **By money-adjacent extensions.** Electronic payments between the parties, pay-application advances/financing, lien-rights management, collections workflows, and WIP reporting — present in some products, adjacent to the core cycle.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Construction Contract Administration | upstream anchor | holds the contract record the billing attaches to (contract value, schedule of values as contract structure, retainage terms, payment status); this Type owns the recurring billing cycle and the application documents themselves |
| Generic Invoicing Application | adjacent generic sibling | states an amount due for a delivered transaction; progress billing computes the amount due from contract completion against a payment breakdown, cumulatively, with counterparty certification |
| Billing Platform | adjacent generic sibling | bills standing commercial commitments (subscriptions, usage) on the vendor's own terms; no contract-completion computation or counterparty certification cycle |
| Change Order Management | upstream feeder | owns the change instrument's lifecycle; approved changes land in the payment breakdown and are billed through this Type's applications |
| Construction Claims Management | the disagreement path | shares vocabulary ("progress claim" in Australian usage names a pay application, not a dispute); claims assert payment when agreement is absent, while applications bill agreed earned value |
| Project Controls Platform | cost-side mirror | measures cost and schedule performance against a baseline; this Type converts progress into certified billings — shared vocabulary, opposite flow |
| Accounts Receivable Management | downstream sibling | begins where certification ends: aging, collections, and cash application on certified amounts; sub-side billing products commonly extend into it |
| Construction Cost Management | cost mirror | owns budget, forecast, and actuals; over/under-billing visibility connects the two, but the budget is a different object |
| Subcontractor Management | adjacent | manages the vendor population and its compliance posture; this Type is the money machinery for the contracted work |
| Construction Closeout Management | terminal phase sibling | owns project-end acceptance and deficiencies; the final application, final retainage release, and final account are this Type's terminal documents |

The sharpest boundary is with generic invoicing: both produce documents that request payment. What makes this Type its own thing is that the amount due is computed from the contract's completion state against a payment breakdown, each application continues a cumulative series, and the counterparty's review and certification — not the issuer's say-so — creates the payable record.

## Representative Products

- **Procore** — multi-party construction platform; the Invoicing tool family manages owner invoices and subcontractor invoices with billing periods, invite-to-bill, line-item review, retainage set/release, and seat-relative naming (the same tools appear as "Progress Billings" for specialty contractors).
- **InEight (Contract + Billings)** — enterprise project-controls suite; Contract carries schedule-of-values pay applications (current/previous/cumulative, retainage, vendor portal) while the separate Billings product handles time-and-materials and cost-plus billing with rate tables and markups.
- **Siteline** — standalone subcontractor-side billing platform; pay applications generated to each general contractor's required forms and portals, with system-maintained carry-over, lien waiver and compliance collection, and A/R extensions.
- **GCPay (Autodesk)** — GC-side pay-application exchange platform automating the application workflow between general contractors and subcontractors, with lien waivers, compliance documents, and electronic payments.
- **Knowify** — small trade-contractor platform with G702/G703 pay-application generation, retainage tracking by phase, change-order period warnings, and QuickBooks synchronization.

The core model was checked against pre-digital practice — typed pay applications and certificates, quantity-surveyor interim valuations, and hand-prepared progress claims — to confirm the definition is not over-fitted to current cloud platforms.

## Sources

Research date: **2026-09-10**

Primary sources (product documentation and official product pages):

- Procore Support Center (Tier-1 operational documentation):
  - Invoicing tool (tutorials: Billing Periods; Subcontractor Invoices — create, invite to bill, on behalf, SSOV, review, revise & resubmit, retainage; Owner Invoices — create, edit, review, payment received; point-of-view dictionary Invoicing ↔ Progress Billings) — https://support.procore.com/products/online/user-guide/project-level/invoicing
  - About Subcontractor Invoices — https://support.procore.com/products/online/user-guide/project-level/invoicing/tutorials/about-subcontractor-invoices
- InEight — InEight Billings product page — https://ineight.com/products/ineight-billings/
- InEight — Software Capabilities of InEight Billings — https://ineight.com/software-capabilities-of-ineight-billings/
- InEight — Billings knowledge-library start page — https://learn.ineight.com/Billings/Content/Categories/TopicsStartPage.htm
- InEight — Software Capabilities for InEight Contract (Progress Payment Invoicing; Subcontractor Invoice Portal) — https://ineight.com/software-capabilities-for-ineight-contract/
- Siteline — homepage and Pay App Management feature page — https://www.siteline.com , https://www.siteline.com/feature/construction-payment-application-software
- GCPay — homepage — https://www.gcpay.com
- Knowify — AIA billing page — https://knowify.com/aia-billing/

> Sourcing limitations: the residential-builder pole (Buildertrend) could not be reached (blocked/timed out), so that variant is described without product-specific claims; one sampled vendor's computation detail (GCPay) is evidenced at product-page level rather than in operational documentation; owner-side certification authority (architect vs owner's representative) is described conceptually rather than from a fetched source. Regional machinery beyond the documented North American and Australia/New Zealand evidence is not asserted. No numeric limits, percentages, or timing rules from vendor marketing are stated in this document; such figures remain in the research notes.

Detailed product-by-product observations, the cross-product comparison matrix, and boundary analysis against neighboring Types are recorded in the paired Research Notes.
