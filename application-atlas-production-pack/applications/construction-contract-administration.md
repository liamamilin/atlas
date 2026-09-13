# Construction Contract Administration

## Overview

A **Construction Contract Administration** application is the system of record for the executed contract file of a construction project. Every construction project runs on a set of signed agreements — the contract with the party funding the work, and the subcontracts and purchase orders with the parties performing it — and every one of those agreements carries a value that changes as the work changes, payments that accumulate against it, amounts withheld under its terms, and documents that prove it was properly executed. This application holds each of those agreements as a structured record (parties, value, scope, dates), keeps the record's value current as changes are executed, attaches the payment machinery directly to it (payment applications, payments issued and received, retainage), and moves the record through a managed lifecycle from drafting and signature to completion and closure.

Its boundary: it is not the change process itself (change records have their own machinery), not the full budgeting and forecasting system, not a dispute-resolution tool, and not a document store — it is the contract record that all of those hang from.

## Users & Context

Contract administration is inherently multi-party: every contract has a paying side and a performing side, and the same project usually carries mirrored contract families — the contractor administering the owner's contract while administering subcontracts to its vendors, the owner administering contracts with each of its primes, the specialty contractor administering its client contract and its own purchase orders.

Primary users:

- **Contract administrators and project engineers** (general contractors and construction managers) — create and maintain contract records, assemble schedules of values, route contracts for approval and signature, process payment applications, track retainage; the day-to-day operators of the contract file.
- **Project and program managers** — monitor contract status, values, and pending actions across a project or portfolio.
- **Owners and owner's representatives** — run the same machinery from the receiving side: reviewing and approving contracts and payment applications, tracking funding sources, holding vendors to insurance and documentation requirements.
- **Finance and accounting staff** — receive executed contracts, changes, and invoices into corporate accounting, directly in an ERP or through integrations.
- **Subcontractors and vendors** — external collaborators who see their own contract, submit payment requests, and upload compliance documents through a portal.

The setting is capital construction — commercial, industrial, infrastructure, and public work — with lighter-weight variants in residential building. Compliance and audit stakeholders use the same records to answer "who approved what, when, and on what authority" years later.

## Core Model

### The Defining Core

The application is built on four properties. Remove any one and what remains is no longer construction contract administration:

- **Contracts as structured project records.** Each executed agreement on the project is a system-owned record — identified counterparties, contract value, scope, dates — not a filed document. Together the records form the project's money skeleton: agreements that bring money in (with the funding party or client) and commitments that send money out (to subcontractors and suppliers). In mature products these are administered as one object family; the label changes with the operator's seat (prime contract, client contract, funding, commitment, subcontract, purchase order), the structure underneath does not.
- **Live value on the record.** The system maintains the contract's sum over time: the original value, the changes executed against it, the resulting revised value, and the pending movement not yet agreed. The contract's number is a computed, current result — which is what makes the record trustworthy as the basis for billing and reporting.
- **Contract-relative money movement.** Payments against the contract are requested, reviewed, and recorded on the record: payment applications and invoices reference the contract and accumulate against its schedule of values, payments issued and received are tracked against it, and amounts withheld under the contract's terms (retainage) are carried by the record until they are released.
- **Managed contract lifecycle.** The record moves through states — drafted, routed for review, approved and executed (with the signature recorded), active during the work, completed and closed at the end — and the system keeps an audit trail of who did what to it along the way.

### Standard Capabilities

Around that core, mature products add the machinery that makes administering a contract file workable at construction scale:

- **Schedule of values.** A line-item breakdown of the contract sum — unit prices, quantities, amounts per line — against which progress is billed and earned amounts are computed. Vendors may author the schedule of values for their own contracts in multi-party flows.
- **Retainage machinery.** Per-contract withholding terms applied to each payment, tracked in the record, and released when contract-defined conditions are met; some products keep a dedicated retainage ledger and regional rule variants (for example, sliding-scale retention regimes in Australia and New Zealand).
- **The commitment structure and its cascade.** Downstream subcontracts and purchase orders administered like the upstream contract, with approved changes on one tier reflected in the contracts below (the change machinery itself belongs to Change Order Management).
- **Contract documents and execution.** Attachments for the executed agreement, exhibits, and addenda; electronic signature on the contract record; templates and auto-fill for generating contracts and purchase orders; conversion of an awarded bid into a contract record.
- **Approval workflows with signing authority.** Multi-step routing by role, department, or dollar threshold; recorded approvals; enforcement of who may sign what.
- **Vendor compliance documents.** Insurance certificates, licenses, and bonds tracked against vendors and their contracts, with reminders for expirations and missing documents; lien waivers collected in the payment flow.
- **Payment status tracking.** Where each payment application sits — submitted, in review, approved, paid, disputed — plus accruals and aging views.
- **Registers and contract summaries.** A project-level list of all contracts with statuses and values, filterable by status, party, and vendor, with totals: original sum, approved changes, pending changes, revised sum.
- **ERP and accounting integration.** Executed contracts, changes, and invoices exported or synchronized into corporate accounting, often gated by an accounting-acceptance step.
- **Multi-party access.** External collaborators see and act on their own contracts through portals; each contract is private to its parties by default.

### One Structure, Many Implementations

The core is written conceptually; products realize it differently. The upstream contract is a "prime contract" to a general contractor, a "client contract" to a specialty contractor, and a "funding" on the owner's side — the same object administered from different seats. The schedule of values may live inside the contract record, in a separate billing module, or in the ERP's job-cost ledger. Compliance documents may be a certificate register inside the tool or a dedicated compliance module. Where a product draws the line between contract record, billing, and cost control varies — but the contract record with its live value, payments, and lifecycle is present in all of them.

## How It Works

### Set up the contract file

```text
Award decision
→ Create the contract record
    (counterparties, value, dates, scope; from a template,
     auto-filled from entered data, or converted from the winning bid)
→ Build the schedule of values
    (line items by cost code or trade; vendor may author their own)
→ Attach contract documents (agreement, exhibits, insurance certificates)
→ Route for review and approval (by value, role, or department)
→ Record approval and signature
→ Contract is executed; its value enters the project's money skeleton
```

An unsigned contract is visible as pending action; dashboards commonly surface unsigned contracts and outstanding approvals so the file does not silently stall.

### Administer the money during the work

```text
Performing party submits a payment application
    (against the schedule of values, often from a vendor portal,
     with supporting backup)
→ Review against work performed and contract terms
→ Approve (multi-step, threshold-based where configured)
→ Payment recorded against the contract (issued or received)
→ Retainage withheld per the contract's terms, tracked on the record
→ Release retainage when contract conditions are met
    (commonly through a later payment application)
```

Payment status is visible on the contract: what has been billed to date, what has been paid, what is outstanding, and what is being held as retainage.

### Absorb change

When the parties agree to change the work, the change instrument is processed by the change machinery and its approved effect lands here: the contract's revised value is updated with a full history — every amendment with its date, amount, and approval recorded — and subsequent payment applications are computed against the new sum. Pending (not yet agreed) changes are kept visible separately from executed ones, so exposure and committed reality stay distinguishable.

### Close the contract

```text
Work reaches completion
→ Final payment application and settlement
→ Release of remaining retainage
→ Final waivers / closure documentation recorded
→ Contract marked completed/closed, its audit trail retained
```

Contract-level closure is the counterpart of project closeout: the closeout process proves the work is done and accepted; contract administration settles the money and retires the record.

### When the normal flow breaks

- **Unagreed change** — the value stays split between executed and pending until agreement; work performed before agreement is a commercial risk the record makes visible rather than hides.
- **Disputed payment** — a payment application can sit in review or be marked disputed; the record keeps the conversation's evidence (submissions, comments, attachments).
- **Compliance gaps** — an expired insurance certificate or missing document can hold up review; reminders flag it before it blocks payment.
- **Revisions after execution** — executed contracts are protected records; corrections happen through tracked revisions, not silent edits.

## Interfaces

The surfaces below are described conceptually; exact layout and naming vary by product.

### Contracts register

The operator's home surface: every contract on the project (upstream and downstream) with its number, parties, status, and values; filters by status, contractor, or vendor; expandable rows revealing the change orders on each contract; grand totals across all contracts. Primary actions: open a contract, create a new one, export the list.

### Contract detail

The work surface for one contract: header information (parties, dates, value), the schedule of values, tabs or sections for its change orders, payment applications, payments issued or received, retainage, attached documents, signatures, and change history with audit trail. Primary actions: edit while draft, route for approval, record approval/signature, update the schedule of values, add documents.

### Payment application surface

Where money moves: the current billing against the schedule of values (previous, current, and cumulative amounts), retainage withheld, attachments of supporting evidence, and the review decision. Vendors see their own version through a portal and submit from there. Primary actions: submit, review, approve, dispute, record payment.

### Compliance and document views

The trust surface: insurance certificates, licenses, and bonds on file per vendor or contract, with expiry dates and reminders for missing or lapsing documents. Primary actions: upload/replace documents, set requirements, chase exceptions.

### Dashboards and reporting

The management view: contract statuses across the portfolio, original vs revised vs pending values, committed versus uncommitted amounts, unbilled and unpaid exposure, retainage balances awaiting release, aging of unpaid invoices.

### Settings

Administrator controls: permission templates per tool, configurable fields, numbering schemes for financial records, privacy defaults for new contracts, approval-workflow templates, accounting-integration behavior.

## Important Rules / Behaviors

- **Status gates the value.** Drafted, rejected, and pending records do not move the contract's sum; only executed changes do. The revised value is a consequence of recorded decisions, not a hand-editable number — which is what makes it trustworthy.
- **Executed contracts are protected.** Once approved and signed, the record becomes a contract document: products restrict casual edits and require revisions, preserving the audit trail that disputes and audits later rely on.
- **Payment follows the schedule of values.** Applications are computed line by line against the contract's payment breakdown; the breakdown, not the invoice, is the arithmetic backbone.
- **Retainage is a contract term, not an accounting preference.** The withheld portion follows the terms recorded on the contract, is tracked on the record through the project, and is released through the payment process when the contract's conditions are met.
- **Compliance documents accompany the money.** Vendors' certificates and bonds are tracked against their contracts; lapses surface as reminders and can hold payment review.
- **Each contract is private to its parties.** In multi-party products, a commitment is visible to the contractor and that vendor, not the whole project; privacy is a deliberate per-record setting.
- **The file mirrors across tiers.** The same physical work usually appears in the owner's contract, the contractor's subcontracts, and vendors' purchase orders; keeping those records coherent — value, changes, and payment state — is part of the operator's job and, in some products, automated.
- **Accounting has a gate.** Where contracts synchronize with corporate ERP systems, synchronization is commonly subject to an accounting-acceptance step; the project record and the books meet deliberately, not automatically.

## Variants

- **By operating seat.** General-contractor-side (the full file: owner contract above, commitments below), owner-side capital programs (contracts with primes, funding sources tracked as parallel objects, stronger compliance posture), specialty-contractor-side (client contract plus the contractor's own purchase orders), and residential builder-side (lighter client-contract handling).
- **By packaging.** A tool family inside a multi-party construction platform; a standalone contract-management module of a project-controls suite; or contract objects embedded in a construction ERP where approval propagates directly into accounting and vendor records.
- **By segment weight.** Formal capital-program administration with multi-tier registers, funding objects, and signature requirements; lighter flows on smaller work.
- **By regional machinery.** Retention and payment-notice regimes differ by jurisdiction (documented examples include sliding-scale retention and statutory payment schedules in Australia and New Zealand); the record structure stays stable while the rules attached to it vary.
- **By compliance depth.** A certificate register inside the contract tool, or a dedicated compliance capability (prequalification, licensing, bond tracking) beside it.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Business Contract Administration / Contract Lifecycle Management | adjacent generic sibling | manages any contract type as record + lifecycle + obligations; lacks the construction money machinery (schedule of values, retainage, payment attachment, commitment structure) and is sold into legal/procurement, not project teams |
| Change Order Management | owned instrument | owns the change lifecycle (identify → price → approve → execute); this Type holds the contract file the changes modify and carries their effect into the value |
| Progress Billing | downstream cycle | owns the periodic billing/pay-application cycle in detail; this Type holds the contract-side anchor (value, schedule of values, retainage terms, payment status) the billing attaches to |
| Construction Cost Management | sibling consumer | owns budget, forecast, and cash flow; contracts feed it as committed cost, but the budget is a different object |
| Construction Claims Management | the disagreement path | claims assert payment/time when agreement is absent; this Type records agreed contract reality |
| Construction Closeout Management | terminal phase sibling | owns project-end deficiencies, deliverables, and acceptance; contract-level final payment, retainage release, and closure live here |
| Construction Document Management | adjacent | stores project files; this Type maintains structured, value-bearing records that documents attach to |
| Subcontractor Management | adjacent | vendor prequalification and performance are vendor-centric; the vendor directory here serves the contract record and its compliance documents |
| Purchase Order Management | adjacent generic | manages the procurement order lifecycle in office/procurement contexts; in construction, POs appear as commitments within this file |
| Construction Project Management | broader container | schedules, RFIs, submittals, drawings, and financials all live in the platform; none of them is the contract file itself |

The sharpest boundary is with generic contract lifecycle management: both manage contracts through approval, signature, and amendment. What makes this Type its own thing is that the contract is a live money object on a project — its sum is computed from recorded changes, its payments and withheld amounts accumulate on the record, and its family extends down to the vendors actually building the work.

## Representative Products

- **Procore** — multi-party construction platform; the Prime Contracts and Commitments tools administer the whole file (upstream contracts, subcontracts, purchase orders, fundings) with schedules of values, retainage, invoices, and audience-relative naming for GC, owner, and specialty-contractor seats.
- **InEight Contract** — standalone contract-management module of a project-controls suite for capital construction; contracts with schedules of values, retention ledgers, vendor compliance documents, pay applications, and ERP integration from procurement to closeout.
- **Kahua** — owner- and delivery-team platform; contracts, commitments, change orders, pay requests, and approvals administered as one connected project record with a preserved audit trail.
- **CMiC** — construction ERP where subcontracts and owner contracts are financial objects in the same database as accounting; approved changes propagate automatically into vendor contracts.

The core model was checked against pre-digital practice — the contract administrator's paper file of contract documents, measured work against the schedule of values, payment certificates, and the retention account — to confirm the definition is not over-fitted to current cloud platforms.

## Sources

Research date: **2026-09-07**

Primary sources (product documentation and official product pages):

- Procore Support Center (Tier-1 operational documentation):
  - Glossary of Terms (Contract Administration, Prime Contract, Client Contract, Commitment, Subcontract, Purchase Order, Funding, Retainage, Retention, Schedule of Values, Lien Waiver, Performance Bond, Insurance Manager, AIA Billing, G702/G703) — https://support.procore.com/references/construction-management/glossary-of-terms
  - Prime Contracts tool — https://support.procore.com/products/online/user-guide/project-level/prime-contracts
  - Commitments tool — https://support.procore.com/products/online/user-guide/project-level/commitments
  - About the Prime Contracts Tool — https://support.procore.com/products/online/user-guide/project-level/prime-contracts/tutorials/about-the-prime-contracts-tool
  - Enable Retainage on a Purchase Order or Subcontract — https://support.procore.com/products/online/user-guide/project-level/commitments/tutorials/enable-retainage-on-a-purchase-order-or-subcontract
- InEight — InEight Contract product page and FAQ — https://ineight.com/contract
- InEight — Software Capabilities for InEight Contract — https://ineight.com/software-capabilities-for-ineight-contract/
- Kahua — Construction Contract Management Software (Change & Contract Management) — https://www.kahua.com/solutions/contract-management
- CMiC — Construction Financials / Accounting — https://www.cmicglobal.com/products/construction-financials/accounting
- CMiC — Change Order Management — https://www.cmicglobal.com/products/business-needs/change-order-management

> Sourcing limitations: official documentation for Oracle Primavera Unifier (a long-standing owner-side capital-contract system) could not be retrieved (unreachable docs), and residential-segment vendors were unreachable in this and prior passes; the owner-side structure is supported by owner-operated evidence from the sampled platforms, and the residential variant is described without product-specific claims. Exact default status lists for contract records were not directly verified and are described conceptually. Regional payment machinery beyond the documented Australia/New Zealand examples was not source-verified and is not asserted. No numeric limits, percentages, or timing rules are stated in this document; vendor-stated figures remain in the research notes.

Detailed product-by-product observations, the cross-product comparison matrix, and boundary analysis against neighboring Types are recorded in the paired Research Notes.
