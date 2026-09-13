# Change Order Management

## Overview

A **Change Order Management** application (in construction) is the system of record for changes to executed construction contracts. Construction contracts are signed with a fixed scope of work, but real projects rarely follow the drawings: owners ask for additions, designs contain errors, site conditions surprise everyone, materials get substituted. Every one of those changes has to be documented, priced, agreed by the party who must pay for it, and folded back into the contract's value — otherwise someone performs work with no contractual basis, and disputes follow. This application manages that process end to end: it captures identified changes to a contract, itemizes their cost and schedule impact, routes them through review to the counterparty's recorded approval, and executes the approved change into the contract amount and the project's budget and billing.

Its boundary: it is not the whole project cost system (budgeting, forecasting, and cash flow belong to broader cost management), it is not the billing application itself, and it is not a dispute-resolution tool — it manages the *agreement* path that keeps changes out of dispute.

## Users & Context

Change order management is inherently multi-party: a change usually involves the party who wants or must perform the work, the party who prices it, and the party who must approve paying for it.

- **Project managers and project engineers** (general contractors and construction managers) — identify changes, document them, drive them through pricing and review; the day-to-day operators of the register.
- **Cost engineers / contract administrators** — price changes, maintain line-item detail, keep the contract sums and budgets consistent, manage revisions and signatures.
- **Owners and owner's representatives** — review and approve changes to their contracts with contractors; on owner-side deployments they run the same machinery from the receiving side.
- **Subcontractors and vendors** — respond to quote requests for changes, and receive approved changes against their own contracts (subcontracts, purchase orders).
- **Specialty contractors** — run the machinery on their own client contracts, initiating and pricing changes against the contractor above them.

The setting is capital construction: commercial buildings, infrastructure, industrial and public projects, and — with a lighter-weight flavor — residential building and remodeling, where the "counterparty" is the homeowner.

## Core Model

### The Defining Core

The application is built on four properties. Remove any one and what remains is no longer change order management:

- **Change records attached to contracts.** A change is a discrete, documented object bound to a specific contract on the project — the contract with the client (prime contract / owner contract / funding agreement) or a downstream contract (subcontract, purchase order). The same project may carry parallel change records on the upstream contract and on downstream contracts for the same underlying work.
- **Itemized commercial impact.** Each record itemizes what is changing in the scope and what it costs — typically as line items valued against the contract's schedule of values — accumulating to a revised contract amount. Schedule (time) impact is tracked alongside cost in mature implementations; a change can affect time without cost or cost without time.
- **Counterparty approval gate.** A record advances from *proposed* to *executed* only through a recorded review and approval — normally by the party who must pay or accept the change. Unapproved, it remains potential; nothing about it is yet contractual.
- **Execution into project money.** When approved, the change updates the contract/committed amount and flows into the project's financial machinery: budget values, downstream commitments, and subsequent billings reflect the new contract sum.

### Standard Capabilities

Around that core, mature products add the machinery that makes the process workable at construction scale:

- **Identification-stage records.** A precursor object — commonly called a potential change, change event, or issue — captures a change that has been *recognized* but not yet agreed: its description, cause, scope, and responsible party, preparing the team for a cost before it becomes an actual cost. Some products also use this stage to record cost recoveries a party owes another (for example, holding back money to fix another party's defective work).
- **Quote solicitation.** The change can be sent to the vendors who would perform the work as a request for quote; their responses — including cost and schedule impact documentation — feed the pricing of the change. A general contractor may also enter a quote on a subcontractor's behalf.
- **Staged progression and grouping.** The path from identified change to executed contract change commonly has multiple stages: potential changes are created first, may be grouped into a request package for review, and are ultimately consolidated into one change order for approval and signature. Products typically let each contract type be configured with fewer or more of these steps (a direct change order, or an intervening review stage or two).
- **Status model.** Each record carries a lifecycle status: a draft state while being assembled; a pending family distinguishing "being reviewed", "being priced", and (in some products) whether work is proceeding before approval, plus a revised state after rework; and terminal states — approved, rejected, voided/withdrawn, or recorded as having no charge (a scope-only change).
- **Pending vs approved money.** Budget views in mature implementations reflect changes as two distinct layers — pending (proposed, not yet agreed) and approved (contractual). This split is the application's core financial honesty: everyone can see exposure that is not yet agreed.
- **Revisions, documents, and audit trail.** Records are revised rather than silently rewritten; attachments, correspondence, and signatures are kept with the record; who did what and when is traceable — the evidence base if a change is later disputed.
- **Change reasons.** Records are classified by why the change exists (owner request, design error or omission, unforeseen site conditions, substitutions), which supports both workflow routing and later analysis.
- **Register and totals.** A project-wide list of all change records with statuses and values, and the net effect on each contract: how much has been approved, how much is pending, and where aging items sit.
- **Cascade across tiers.** One root change is priced *up* to the client and *down* to the affected vendors; some products automatically generate or link the downstream changes when the upstream one is approved.

### One Structure, Many Implementations

The core is written conceptually; products realize it differently. The identification stage is a "change event" in one product, an "issue" in another, a "potential change" in a third. The grouping stage exists as explicit package objects in some products and as a simple two-step flow in others. The counterparty sees the change through a collaborator portal in platform products, or receives it as a paper/PDF document from products that only manage the contractor's side. The terminology itself is audience-relative: the same machinery is labeled after the contract it changes — a change order on the owner contract, on a funding agreement, or on a client contract, depending on who is operating the software.

## How It Works

### The main flow — from noticed change to changed contract

```text
Change is noticed (owner request, design issue, site condition, substitution)
→ Record it as an identified/potential change
    (description, cause, scope, responsible party)
→ Solicit pricing from the vendors who would do the work
    (quote request with cost + schedule impact responses)
→ Build the change record's line items and revised value
→ Submit for review by the counterparty
→ Negotiate / revise if needed
→ Recorded approval (and signature, where the contract form requires it)
→ Execute: contract amount and budget updated; change flows into billing
```

The loop's output is a contract that always reflects the work actually being performed — the defining job of the application.

### The cascade — one change, several contracts

When a client-approved change affects work performed by subcontractors, parallel change records are created against the downstream contracts, priced by each vendor, and approved by the contractor — so the money flows coherently on both sides of every contract. In ERP-embedded products this propagation can be automatic; in platform products it is performed by linking records created from the same identified change.

### When agreement fails

The approval gate is the application's honest core: if the parties do not agree, the change does not execute. It stays pending (perhaps with work proceeding at the performer's risk, which some products track explicitly), gets rejected or withdrawn, or — where the owner has the contractual right — proceeds under a directive instrument rather than a mutually agreed change. Changes that harden into assertions of payment or time without agreement belong to the claims process, outside this application.

### Recovery changes

The same machinery records money owed *to* the operator's side: a backcharge-style change documents work a vendor was contractually obligated to perform (or damage they caused), itemizes the cost, and executes it against the vendor's contract as a deduction.

## Interfaces

The surfaces below are described conceptually; exact layout and naming vary by product.

### Change register (list)

The operator's home surface: every change record for the project (or for one contract) with its number, title, reason, status, value, and age; filters by status and contract; totals of pending and approved change amounts. Primary actions: open a record, create a new change, group items into a package for review.

### Change record detail

The work surface for one change: header information (contract, parties, reason, dates), the itemized scope and pricing (often structured against the schedule of values), schedule impact, status history with audit trail, linked documents and related items (RFIs, drawings, quotes), and the action buttons appropriate to the current status (submit, revise, approve, reject, void). Primary actions: edit while draft, record pricing, route for review, record approval decision.

### Quote / response surface

Where vendors see the change they are being asked to price: the scope description, the response form for cost and schedule impact, and their submitted quote documents. Primary actions: submit a response, review received responses, convert responses into the change record's pricing.

### Approval / signature surface

The counterparty-facing step: the consolidated change order with its revised contract amount, the review decision (approve, reject, request revision), and where required, the formal signature that makes the change contractual. Primary actions: review, decide, sign.

### Budget / change view

The financial reflection: contract and budget values with pending changes and approved changes shown as separate columns or views, so reviewers can distinguish exposure from committed reality. Primary actions: drill from a change amount back to the underlying records.

### Dashboard / reporting

Portfolio or project level: counts and values of changes by status, aging pending items, net contract movement, and reason breakdowns — the management view that surfaces drift early.

## Important Rules / Behaviors

- **Approval makes extra work contractual.** Work outside the signed scope performed before approval is at the performer's risk; the whole application exists to shrink that window by making changes fast to document, price, and agree.
- **Status gates the money.** Draft, rejected, voided, and no-charge records carry no financial effect; pending records surface as pending money; only approved records change the contract sum and flow into billing.
- **The workflow shape is fixed early.** Products commonly lock the number of review stages per contract once changes exist on it, because records already in flight depend on that structure; the configuration is therefore a deliberate early decision.
- **Approved records are protected.** A signed change order is a contract document; products restrict casual edits after approval, using revisions instead — preserving the audit trail that disputes later rely on.
- **Not every change costs money.** Scope-only changes are recorded as no-charge items so the contract documents stay faithful to what is being built; time-only impact is recorded similarly against the schedule.
- **Both directions of money.** The same structure handles additions the owner pays for and deductions owed by vendors (recoveries for defective or omitted work); a change's sign is data, not a different process.
- **Multi-party reality.** Records exist per contract, not per project; the same underlying work can and usually does appear in a change on the client contract and changes on several vendor contracts, and coherence across those records is part of the operator's job (and, in some products, automated).

## Variants

- **By operating party.** Contractor-side (the general contractor driving changes both up and down), owner-side capital programs (the owner administering change control across its contractors, often with funding-source approvals), specialty-contractor-side (changes against the contractor above), and residential builder-side (changes against the homeowner).
- **By packaging.** A module of a construction management platform; a standalone change management module attached to an existing cost/contract system; or embedded in a construction ERP where approval automatically ripples into accounting and subcontract records.
- **By delivery form.** Formal multi-stage registers with signature requirements on large commercial and public projects; lighter client-approval flows on residential work, where a client-facing approval — sometimes organized around design selections and their budget effect — plays the role of the multi-tier register.
- **By pricing treatment.** Depending on the contract form, changes are priced as agreed sums, unit-priced work, or documented actual costs; markup and contingency treatment follows the contract. (Pricing mechanics vary widely by product and contract; the application enforces whatever the contract defines rather than imposing one method.)
- **By vocabulary.** Change order, variation, change request, potential change — market and contract form determine the label; the structure described here is stable underneath.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Construction Cost Management | broader sibling / usual host | spans budget, commitments, forecasting, cash flow; change order management is the contract-change machinery within or beside it |
| Construction Contract Administration | broader | covers the whole contract file (payments, insurance, bonds, compliance); change orders are one instrument it administers |
| Progress Billing | downstream consumer | converts work-in-place and approved changes into periodic bills; it does not create, price, or approve changes |
| Construction Claims Management | the disagreement path | claims assert payment/time when agreement is absent; this Type manages the agreement path that prevents claims |
| RFI Management | adjacent | an RFI asks a question and may surface a change, but carries no price, contract attachment, or approval-to-execute |
| Construction Project Management | broader container | schedules, RFIs, submittals, drawings, and the change register all live there; none of the others is contract-relative money machinery |
| Purchase Order Management | adjacent | manages the procurement order lifecycle; changes to vendor contracts (including POs) are this Type's objects |
| Engineering Change Management | same word, different world | changes product/design data (parts, BOMs, revisions) in manufacturing; no commercial contract counterparty or payment consequence |
| Approval Workflow Platform | generic capability | routes items for approval but lacks contract-relative records, itemized impact, and execution into project money |

The sharpest boundary is with claims: a change order records what the parties *agreed*; a claim is what one party asserts when they did not. Directive-style instruments sit deliberately between the two — owner-commanded work performed before agreement, recorded here only where the product supports them.

## Representative Products

- **Procore** — multi-party construction platform; the change machinery spans change events, potential change orders, and change orders on prime contracts, commitments, funding, and client contracts, with configurable review stages and audience-specific terminology.
- **InEight Change** — standalone change order management module (also part of a project-controls platform) aimed at capital construction; issue-based capture with integrated cost and schedule impact analysis.
- **CMiC** — construction ERP with change order management embedded in its single-database financials; approval automatically propagates changes into subcontracts.

Additional market presence (not source-verified this pass): Autodesk Construction Cloud, Buildertrend (residential), Kahua, Trimble e-Builder, Oracle Primavera Unifier.

## Sources

Research date: **2026-09-07**

- Procore Support Center (Tier-1 operational documentation):
  - "What is a change order?" — https://support.procore.com/faq/what-is-a-change-order
  - "What is a change event?" — https://support.procore.com/faq/what-is-a-change-event
  - "What are the default statuses for change orders in Procore?" — https://support.procore.com/faq/what-are-the-default-statuses-for-change-orders-in-procore
  - "What are the different change order tier settings in Project Financials?" — https://support.procore.com/faq/what-are-the-different-change-order-tier-settings-in-project-financials
  - "What tool names and terms are different in Procore for general contractors, owners, and specialty contractors?" — https://support.procore.com/faq/what-tool-names-and-terms-are-different-in-procore-for-general-contractors-owners-and-specialty-contractors
  - Glossary of Terms (Change Event, Change Order, Change Order Request, Potential Change Order, Construction Change Directive, Changed Condition, Backcharge, Schedule of Values) — https://support.procore.com/references/construction-management/glossary-of-terms
- InEight — "InEight Change" product page and FAQ — https://ineight.com/change
- CMiC — "Change Order Management" — https://www.cmicglobal.com/products/business-needs/change-order-management
- BuildBook — public feature pages (residential market context) — https://buildbook.co/

> Sourcing limitation: official documentation for Autodesk Construction Cloud, Buildertrend, Kahua, Trimble e-Builder, Oracle Primavera Unifier, JobProgress, and CoConstruct could not be retrieved from the research environment (JS-rendered help sites, timeouts, or blocked responses). The residential/SMB and owner-side segments are therefore under-sampled relative to their market weight, and vendor product claims from those vendors are absent. Pricing-form details (lump-sum / unit-rate / actual-cost handling, markups, contingency) were not directly source-verified and are described only in qualified terms. No numeric limits, default thresholds, or precise timing rules are asserted in this document; product-specific status labels and configuration mechanics are described conceptually, with the researched products as the evidence base.
