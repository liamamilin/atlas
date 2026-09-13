# Freight Audit & Payment Platform

## Overview

A **Freight Audit & Payment Platform** is a shipper-side financial operations system that receives freight invoices from carriers, verifies every charge against the shipper's contracted rates and terms, resolves discrepancies with the carriers, settles the approved freight payables, and maintains the resulting shipment-level freight cost record for finance and analysis.

The problem it exists to solve: companies that ship freight — by parcel, LTL, truckload, ocean, or air — receive enormous volumes of carrier invoices, and a meaningful share of those invoices contain errors: rates that don't match the contract, misapplied fuel surcharges and accessorial fees, duplicate charges, dimensional-weight overcharges, and charges for service failures. Checking this by hand is slow, and errors either get paid or get recovered too late. The platform industrializes that check: it becomes the system of record for what the shipper owes its carriers, decides which amounts are legitimately payable, recovers what isn't, and pays the rest on time.

The defining loop has four parts, and the market's own definitions converge on them:

```text
Carrier freight invoices (shipment-level payable records)
  → charge-level verification against contracted rates & terms
      → pass → approved payable
      → exception → discrepancy resolution with the carrier
                    (claim/dispute → carrier response → credit or acceptance)
  → settlement of approved freight payables
  → shipment-level freight cost record (GL, accruals, analytics)
```

The boundary to keep in mind: this is not the system that moves the freight. Planning, rating, tendering, and tracking shipments belong to a Transportation Management System; this system takes over where a billable move turns into a payable one. It is also not generic invoice processing — its entire verification logic is freight-specific.

## Users & Context

The platform sits between a shipper's carrier network and its finance function.

Primary users:

- **Transportation / logistics operations** — freight audit analysts and payment specialists who work the exception queue, review flagged charges, file and track disputes with carriers, and maintain carrier and contract setup.
- **Finance / accounts payable** — controllers and AP staff who rely on the platform for freight accruals, GL coding and cost allocation, approval controls, and payment execution or payment-file handoff.

Secondary users and counterparties:

- **Carriers** — external counterparties: they submit invoices into the platform, receive dispute/claim communications, and receive payments with remittance detail.
- **Procurement / carrier managers** — consumers of the analytics: billing-accuracy scorecards, recovery evidence, and spend patterns used in carrier negotiations and contract reviews.
- **IT / integration teams** — set up the invoice feeds and ERP/TMS connections during onboarding.

Context: high invoice volumes across many carriers and modes, contracts complex enough that billing errors are routine, and a finance requirement that freight costs be coded, accrued, and paid under control. In the managed-service form of the Type, the provider's own audit specialists operate much of this loop on the shipper's behalf; in the software form, the shipper's team operates it directly.

## Core Model

The platform's world is built from a small set of objects. The **freight invoice** is the center; everything else either feeds its verification or records its outcome.

### Freight invoice (the unit of work)

A carrier's bill for one or more shipments, ingested from electronic feeds (EDI 210 is the standard electronic freight-invoice format), carrier portals, PDF uploads, or monitored email inboxes, and normalized into a single processing queue. Each invoice is held as a shipment-level payable record broken into **charge lines** — base linehaul, fuel surcharges, accessorial fees, adjustments. The invoice carries references that tie it back to the move: shipment or PRO/tracking numbers, dates, lanes, weights. Duplicate copies of the same invoice are detected and suppressed.

### Contract / rate reference (the audit baseline)

The shipper's negotiated agreements with each carrier, held as structured reference data: contracted rates and discounts, minimums, surcharge and accessorial rules, fuel-surcharge tables, and any caps or tier thresholds. This is what makes the audit freight-specific: a charge is not checked merely for arithmetic validity but for **compliance with the contract** — a residential surcharge on a commercial address, a fuel percentage applied to the wrong base, a discount that the contract entitles the shipper to but the invoice omits.

### Audit check and exception

The engine applies the contract rules — plus configurable tolerances (how much a rate may deviate before it counts as a mismatch), permitted-accessorial rules, approval limits, and documentation requirements such as proof of delivery — to every charge line. Charges that pass become approved payables. Charges that fail become **exceptions**: recorded discrepancies with the reason, the amount at stake, and the evidence attached.

### Dispute / claim

An exception that is recoverable is pursued with the carrier. The platform generates the claim, submits it through the carrier's billing channel, tracks the carrier's response, and — critically — **verifies that the agreed credit actually lands** against a future invoice. Claims are time-boxed: carriers allow refunds and disputes only within filing windows, which is why mature operations run the audit on a continuous (often weekly) cadence rather than in periodic sweeps. Not every exception becomes a claim; some are adjusted, some are accepted with a recorded reason.

### Approval and payment

Approved payables — those that passed the audit or whose disputes are resolved — move through an approval step (with dollar-based approval limits) into **settlement**. In the full-service form of the Type, the platform executes or drives the payment cycle to carrier terms: payment runs are prepared from approved invoice data, validated, and released, with remittance detail back to the carrier. Depending on the provider, funds may flow from the provider itself (bank-backed providers pay carriers and are reimbursed by the client) or the platform may drive the client's own payment systems.

### Cost allocation and the freight cost record

Every settled invoice is coded to the general ledger — account codes, cost centers, business units, often split across multiple allocations on one invoice. The accumulated shipment-level cost record supports accruals (what has been received but not yet invoiced, what is in dispute, what is approved but unpaid) and becomes the data layer for analytics: spend by carrier, mode, and lane; billing accuracy per carrier; recovered amounts; recurring error patterns.

### How the objects relate

```text
Carrier contracts / rate agreements
        ↓ (verification baseline)
Carrier invoice → charge lines → audit check (rules + tolerances)
        ├── pass ──────────────→ approved payable → payment run → carrier paid
        └── exception → dispute/claim → carrier response → credit verified
                                  ↓ (resolved)          ↓ (credits future invoices)
                          approved/adjusted payable → payment
        ↓ (all settled invoices)
Freight cost record → GL coding / allocation → accruals → spend analytics
```

## How It Works

### Onboarding: connect the pipes

The shipper's systems and carriers are connected to the platform: invoice feeds (EDI, portal, email, upload) are authorized, carrier contracts and rate terms are loaded as the audit baseline, GL coding and approval rules are configured, and ERP/financial-system integrations are established. Vendors in the researched sample describe implementations on the order of weeks, driven by the number of carriers and systems involved.

### The per-invoice loop

```text
Invoice arrives (any channel) → normalized into the queue, duplicates suppressed
→ matched to its shipment(s) and the applicable contract
→ every charge line checked against contracted rates and rules
→ within tolerance → approved
→ outside tolerance / unauthorized charge → exception with reason and evidence
→ exception worked: claim filed with carrier, response tracked, credit verified
→ resolved invoice → GL coding → approval → payment cycle
```

The design goal, stated across the sample, is that invoices which match the contract clear with minimal or no human touch, and human effort concentrates on the exceptions.

### The dispute loop

```text
Flagged charge → claim generated and filed with the carrier
→ carrier response tracked in the platform
→ credit agreed → verified against a future invoice (not just promised)
→ or charge adjusted / accepted with recorded reason
```

Filing windows make this loop time-critical; the weekly processing cadence exists to keep every recoverable item inside its window.

### The payment cycle

Approved payables accumulate into payment runs cycled to the carrier's payment terms. The platform validates each payment file; in managed-service forms, specialists coordinate and track the payment through to carrier confirmation. Remittance detail accompanies payment so carriers can apply cash against specific invoices — which also closes the loop on disputed items.

### The reporting cycle

Beyond the transaction loop, the platform continuously publishes the state of freight payables: accrued vs audited vs in-dispute vs approved-to-pay, recovery totals, carrier billing-accuracy scorecards, and recurring error patterns. This is the evidence base finance uses at close, and the evidence base procurement uses in carrier reviews.

### Capability tiers

**Defining core** — without these, the product is not a freight audit & payment platform:

- carrier freight invoices ingested as shipment-level payable records
- charge-level verification against contracted rates and terms
- discrepancy resolution loop with the carrier (claim → response → verified credit)
- settlement of approved freight payables
- the shipment-level freight cost record

**Standard capabilities** — present in essentially all mature products:

- multi-channel intake normalization and duplicate suppression
- contract/rate reference data as the audit baseline
- configurable tolerances, accessorial rules, approval limits, documentation requirements
- claim/dispute workflow with carrier-response tracking and credit verification
- GL coding, cost allocation, accrual support
- payment runs cycled to carrier terms with remittance detail
- spend analytics, carrier accuracy scorecards, recovery reporting
- ERP/TMS/WMS integrations over API/EDI/SFTP-class connections
- client web portal with work queues and dashboards

**Optional / variant** — depends on segment and posture:

- parcel-only vs multi-modal scope (parcel, LTL, TL, ocean, air, rail, intermodal)
- pre-audit (before payment) and/or post-audit (after payment, recovery) timing
- managed-service operation vs self-service software vs hybrid
- provider-funded payment (bank-backed pay-and-recover) vs client-side execution
- contingency pricing vs per-invoice fees vs subscription
- global multi-currency operation
- adjacent services: carrier contract negotiation and benchmarking, cargo-claim management, working-capital financing, published market indexes

## Interfaces

The surfaces below are described conceptually; exact layouts and names vary by product.

### Invoice / exception work queue

The operational home screen.

- Purpose: work everything that needs a decision.
- Typical information: invoices and exceptions with carrier, amount, discrepancy reason, age, and status.
- Primary actions: open an exception, approve, adjust, file/track a claim, reassign, annotate.

### Invoice detail (charge-level view)

The audit surface for a single invoice.

- Purpose: show what was billed, what the contract says, and what the engine decided.
- Typical information: charge lines with billed vs contracted amounts, tolerance results, matched shipment references, attached documents (proof of delivery, rate confirmations).
- Primary actions: accept/reject a line, dispute a charge, correct coding, view audit trail.

### Dispute / claim tracker

- Purpose: follow every recoverable charge from filing to verified credit.
- Typical information: claim status, carrier responses, amounts claimed vs credited, filing-window deadlines.
- Primary actions: file a claim, record carrier correspondence, confirm credit receipt, close or escalate.

### Payment run / approval

- Purpose: control what gets paid, when, and to whom.
- Typical information: approved payables grouped by carrier and terms, approval status, payment-file validation results.
- Primary actions: release or hold a payment run, apply approval limits, review remittance output.

### Dashboards / analytics

- Purpose: turn the cost record into decisions.
- Typical information: spend by carrier/mode/lane, accrual vs actual, billing accuracy by carrier, recovered savings, recurring error types.
- Primary actions: filter, drill down to invoices, export, prepare carrier-review evidence.

### Administration / configuration

- Purpose: own the audit baseline and controls.
- Typical information: carrier and contract setup, rate terms, tolerance and accessorial rules, approval limits, GL coding maps, user roles.
- Primary actions: load/update contracts, change rules, manage users and permissions.

### Carrier-facing touchpoints

Carriers interact as counterparties: they submit invoices into the feeds, receive claim/dispute correspondence, and receive payments with remittance advice. Some products expose a carrier portal for these exchanges.

## Important Rules / Behaviors

### Payment follows verification

In the pre-audit form, nothing is paid until it has passed the audit or its disputes are resolved. Exceptions block the payable. This is the control that distinguishes the Type from post-payment recovery alone; products commonly support both timings, with pre-payment audit as the control posture and post-payment audit as the recovery net.

### Tolerances decide what is human work

Configurable thresholds — rate-match tolerance, permitted accessorials, dollar or percentage deviation, approval limits, documentation requirements — determine which invoices clear automatically and which are held for review. Tightening a tolerance moves more invoices into the exception queue; loosening it speeds flow at the cost of control. The rules are the shipper's, configured per client.

### Claims are time-boxed

Carriers honor refund and dispute requests only within defined filing windows, and service-failure refunds have their own windows. The continuous processing cadence exists because a missed window converts a recoverable credit into a permanent overpayment.

### Credits must be verified, not promised

A carrier's agreement to refund is not the end of the dispute; the recovered credit is confirmed only when it appears against a future invoice. Mature workflows track claimed vs received amounts explicitly.

### Duplicates are a first-class error class

Duplicate invoices and duplicate charges are common enough — and costly enough — that duplicate detection across billing cycles is a standing audit check, not an edge case.

### The cost record must be finance-grade

Every settled invoice carries its GL coding and allocation, and the record must reconcile: accrued vs audited vs in-dispute vs approved-to-pay is the standard state visibility finance expects at close. Audit trails on decisions and rule changes support that grade.

### Exceptions end in human decisions

Automated engines flag, route, and draft; the resolution of a dispute — accept, adjust, pursue — is a recorded human decision, whether made by the shipper's team or the provider's specialists.

## Variants

- **Managed-service FAP** — the provider operates the whole function (invoice processing, audit, disputes, payment) on the shipper's behalf; the shipper consumes dashboards and reports. Historically the dominant form, often bank-affiliated for funds handling.
- **Self-service software** — the shipper licenses the platform and runs the audit with its own team; provider support is technical.
- **Hybrid platform + specialists** — software for visibility and workflow, with the vendor's specialists handling carrier-side claims and payment coordination.
- **Parcel audit (audit-only posture)** — focused on small-parcel carriers' weekly billing files; identifies errors and files refund claims (late-delivery guarantees, dimensional-weight reweighs, misapplied surcharges, duplicates) but does not settle payables; typically priced as a share of recovered refunds. Shares the audit machinery of the Type; lacks the settlement leg.
- **TMS-embedded settlements** — the same audit-and-pay loop shipped as a module of a Transportation Management System, matching carrier invoices against the TMS's own shipment and rate data; often also available standalone.
- **Multi-modal global FAP** — all modes and geographies, multi-currency, handling international charge structures.
- **Post-audit recovery** — periodic sweeps of already-paid invoices to recover overcharges; the recovery-only slice of the loop.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Transportation Management System / TMS | adjacent; FAP often embedded as a "settlements" module | TMS plans, rates, tenders, executes, and tracks shipments; FAP verifies and settles the freight payables those moves generate. Remove the payable audit-and-settlement loop and keep tender/rate/track → TMS. |
| Accounts Payable Automation / Invoice Processing Platform | adjacent | Generic supplier-invoice processing (capture, matching, approval, payment) without freight semantics: carrier rate contracts, mode-specific charge structures, carrier dispute channels, freight GL allocation. Remove the freight domain → generic AP automation. |
| Freight Brokerage Platform | different domain object | Brokerage moves freight (capacity, tender, carrier selection); FAP moves the money and documents about freight. |
| Shipment Visibility Platform | adjacent | Visibility tracks in-transit shipment state; FAP tracks payable state. Shipment data feeds the audit cross-reference but is not the system of record here. |
| Freight Claim Management (cargo claims) | adjacent capability | Cargo claims concern loss/damage of goods; billing disputes concern invoice accuracy. Some vendors offer both; a lost-package refund sits at the seam. |
| Spend Analysis Platform | broader/generic | Generic spend analytics lacks the payable lifecycle, contract-compliance machinery, and carrier dispute channels. |
| Expense Management Platform | broader/generic | Employee/expense-report oriented; no carrier invoice lifecycle. |

The two boundaries that matter most: against the **TMS** (execution of moves vs settlement of payables — contested territory, since TMS vendors embed this loop and FAP vendors argue it belongs outside the TMS), and against **generic AP automation** (the freight-specific contract, charge, and dispute semantics are the whole point of this Type).

## Representative Products

- **Cass Information Systems (Freight Audit & Payment)** — managed-service FAP at global-enterprise scale, bank-affiliated funds handling; defines the full audit + payment + accounting + BI form.
- **FreightOptics (Freight Audit and Payment)** — hybrid SaaS platform with managed specialists; audit, dispute, GL allocation, and payment execution in one workflow.
- **ShipSigma** — parcel invoice audit SaaS; the audit-only posture with contingency pricing and claims automation.
- **Shipwell (Settlements)** — the TMS-embedded form: invoice audit and payment as a module of (or standalone addition to) a transportation management system.

Together these cover the managed-service, hybrid-software, audit-only, and TMS-embedded postures of the Type.

## Sources

Research date: **2026-09-07**

- Cass Information Systems — https://www.cassinfo.com/ , https://www.cassinfo.com/freight-audit-payment , https://www.cassinfo.com/freight-audit-payment/services/freight-audit , https://www.cassinfo.com/freight-audit-payment/services/freight-payment
- FreightOptics — https://www.freightoptics.com/ , https://www.freightoptics.com/solutions/freight-audit-and-payment/
- ShipSigma — https://shipsigma.com/ , https://shipsigma.com/parcel-invoice-audit
- Shipwell — https://www.shipwell.com/ , https://www.shipwell.com/solutions/settlements

> Sourcing limitation: official product and solution pages were reachable for the four sampled products, but full help-center/user-manual depth was not available for any of them, and several prominent providers in this market (CTSI-Global, nVision Global, U.S. Bank Freight Payment, Oracle Transportation Management documentation, Loop) could not be reached from the research environment. Operational details that depend on that deeper documentation — funding-cycle mechanics, exact EDI transaction-set coverage, numeric tolerances and limits — are therefore described at the level the fetched sources support, and no precise numbers, defaults, or recovery-rate claims from vendor marketing are asserted as facts in this document.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
