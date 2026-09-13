# Reinsurance Management System

## Overview

A **Reinsurance Management System** is the insurance industry's system of record for reinsurance business — the risk-sharing contracts that insurance companies write with each other. An insurer that buys reinsurance (the **cedent**) uses the system to hold its reinsurance agreements, allocate its own policies, premiums, and claims to them, report the allocated amounts to its reinsurers, and settle the money in both directions. A reinsurer uses the same structures from the other side (**assumed** business): the treaties it has accepted and the cedents' business inuring under them.

It answers the reinsurance operation's operating question: *which agreements cover which business, what does each party owe the other under those agreements, and where does every ceded premium and recovered claim stand?*

The defining core is small:

```text
Reinsurance agreement (treaty / facultative placement)
  └── Allocation of underlying business to agreements (cession / inuring)
        └── Counterparty financial loop
            (balances → bordereaux & technical accounts → settlement → ledger)
```

Everything else commonly associated with these products — reinsurance claims surfaces, contract lifecycle states, statutory reporting, multi-currency and intercompany accounting, analytics — is standard equipment that mature products add around the core. A treaty ledger with manually prepared bordereaux and a settlement cash sheet satisfies the same core structure, as does a life insurer's periodic allocation of benefits to its treaties.

The system holds this record for the operator's **own reinsurance position**: the authoritative record of what the operator has ceded or assumed, with whom, on what terms, and for how much. That is the seam against the policy administration system (which holds the direct policies with policyholders) and against claims systems (which hold the losses; reinsurance takes the recovery side).

## Users & Context

The operator is an insurance company (ceded side), a reinsurer (assumed side), or both — large insurance groups commonly run ceded and assumed programs in one system. Primary users:

- **Ceded reinsurance managers** — structure and maintain the reinsurance program: which treaties exist, what they cover, how layers and inuring arrangements stack, what the current exposure position is.
- **Reinsurance accountants / technical accounting staff** — process cessions, produce bordereaux and technical accounts, track balances, execute and reconcile settlements, and pass results to the general ledger.
- **Recovery specialists** — match claims against contracts, compute recoverable amounts, and pursue collections; the "claims leakage" problem (recoveries that go unclaimed) is the discipline's signature failure mode.
- **Assumed-side administrators** (at reinsurers and in groups writing assumed business) — account for inwards treaties, process cedents' bordereaux, and settle with cedents.
- **Finance, actuarial, and regulatory reporting teams** — consumers of the system's outputs: statutory schedules, IFRS 17 data, consolidated risk and liability views.

The work context is contractual and financially precise: treaty terms are binding commitments, cession calculations must match contract wording exactly, counterparties reconcile every figure, and regulators audit the reinsurance entries in statutory filings. Volume ranges from a handful of large treaties at a reinsurer to hundreds of treaties and millions of ceded transactions at a global carrier.

## Core Model

### The Defining Core

**The reinsurance agreement.** The organizing object is the agreement between the operator and its reinsurance counterparties. It comes in two forms:

- **Treaty** — a standing agreement that automatically covers a defined class of the operator's business (a book, a line, a region) for a period.
- **Facultative placement** — a one-off agreement covering a single risk or defined parcel of business.

The agreement carries its scope (which underlying business it applies to), its financial terms — a proportional share (quota share, surplus) or a non-proportional structure (excess of loss, stop loss) with attachment points and limits — its commissions, its period, and its status. Proportional and non-proportional are term configurations of the same object, not different objects. An agreement can span multiple legal entities, and programs are commonly built as **layers** that inure to one another (the output of one agreement feeding the next).

**The cession.** The system's unit of work is the allocation of underlying business to the agreements that cover it. Units of the operator's own business — policies, premiums, claims (or, in life business, benefits and their premiums) — are attached to the applicable agreements, and each party's share is computed under the agreement's terms:

- **Premium cessions** — the portion of premium ceded to (or, on the assumed side, inuring to) each counterparty, together with the commission due back or payable.
- **Loss cessions and recoveries** — the portion of each claim recoverable from reinsurers, computed per risk, per occurrence, or under catastrophe/aggregate terms as the contract provides.

The computation is governed by the agreement's wording — shares, attachments, limits, exclusions, inuring order — and every computed amount is posted against both the underlying business item and the agreement, so the position of any policy, claim, or treaty can be inspected at any time.

**The counterparty financial loop.** The computed shares accumulate into balances with each counterparty: premium payable to reinsurers, recoverable receivable from them. The system produces the documents the relationship runs on — **bordereaux** (periodic statements of ceded premium and losses), technical accounts, and settlement statements — tracks the resulting receivables and payables through cash handling and credit control, and passes the results to the general ledger. The loop is two-directional: the cedent pays ceded premium and collects recoveries; the reinsurer collects inwards premium and pays losses.

### Standard Capabilities of Mature Products

These capabilities are common across the researched market. They make the core practical; they do not define the Type.

- **Reinsurance claims machinery** — a claims surface on the reinsurance side: claims and loss events linked to contracts, recovery computation per claim, status tracking, billing and status-request correspondence with counterparties, and recovery-maximization controls that review every claim against applicable contracts. Products vary in whether this surface is built in; the recovery computation itself is universal, running over claim data fed from the claims system either way.
- **Contract lifecycle management** — agreements carried through states from creation and negotiation through signed, in-force, run-off, and commutation; renewals created by carrying an expiring agreement's terms forward into a new period.
- **Statutory and regulatory reporting** — reinsurance schedules for statutory filings (in the US, Schedule F and annual-statement data links), IFRS 17 data support, and audit trails behind every figure.
- **Multi-entity, multi-currency, and intercompany accounting** — programs spanning legal entities, currencies, and affiliated companies, with intercompany treaties handled alongside external ones.
- **Integration with the insurance core** — standard interfaces that pull policy, premium, and claims data from policy administration and claims systems, and push results to the general ledger and statutory reporting.
- **Analytics** — consolidated views of ceded positions, exposures, and liabilities across the whole program; KPIs for reinsurance managers.
- **Placement simulation / what-if analysis** — modeling how proposed contract terms would have affected ceded results, used in negotiations.
- **London Market machinery** — outwards reinsurance standards integration (LORS) and broker-facing outputs where the market requires them.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:  The agreement of record
Realized as:  a dedicated treaty module with lifecycle states,
              a contract register inside a suite platform,
              a centralized treaty table in an automation tool

Concept:  The allocation computation
Realized as:  an embedded calculation engine applying contract terms in real time,
              rule-based allocation configured by business users,
              batch calculation cycles (common in life business)

Concept:  The counterparty financial loop
Realized as:  a full technical-accounting ledger with cash management,
              settlement tracking with credit control,
              journal output to an external accounting system
```

A product can satisfy the defining core with any of these realizations — which is why a system without an embedded claims surface, or one that outputs journals instead of holding a settlement ledger, may still be recognizably the same Type.

## How It Works

### Run the ceded program (the primary flow)

```text
Define the program
  → treaties and facultative placements configured
    (scope, share/limits/attachment, commissions, period, counterparties)
→ underlying business arrives from policy and claims systems
→ cession processing: each policy, premium, and claim
   attached to the agreements that cover it
→ shares computed under each agreement's terms
   (premium cessions, loss cessions, recoveries)
→ bordereaux and technical accounts produced per counterparty
→ balances tracked; settlements executed and reconciled
→ results passed to the general ledger and statutory reporting
```

This is the loop the system exists for. In mature products the allocation and calculation steps run automatically against configured contract terms; staff work the exceptions, the settlements, and the reporting.

### Recover on a claim

```text
Claim data arrives from the claims system
→ system matches the claim against applicable agreements
  (per risk, per occurrence, or catastrophe/aggregate terms)
→ recoverable amount computed under contract terms and clauses
→ recovery billed to the reinsurer; status tracked to collection
→ unclaimed recoveries surfaced for review (leakage control)
```

The recovery side is where reinsurance systems earn their keep financially: a claim that is not matched to the right contract is money silently lost, so mature products review every claim against every applicable agreement.

### Renew, run off, and commute

```text
Expiring agreement → renewal created by carrying its terms forward
→ new period configured (terms adjusted as negotiated)
→ expired agreements move to run-off
  (no new cessions; outstanding balances still settle)
→ commutation where agreed: the parties close the account
  for a negotiated single payment
```

Run-off can last years — old agreements keep generating settlement activity long after new business stopped ceding to them.

### Account for assumed business

```text
Treaty accepted (underwriting decision made upstream)
→ cedents' bordereaux and claim advices received
→ inwards premium and losses accounted under the treaty's terms
→ balances with each cedent tracked
→ settlements executed; results passed to the ledger
```

The assumed side mirrors the ceded loop from the opposite seat. Products vary in how deeply they support it; groups that both cede and assume commonly run both sides in one system.

### Defining core vs standard vs optional

**Defining core** — without these, not a reinsurance management system:

- the reinsurance agreement (treaty / facultative) as the managed contract of record
- allocation of underlying business to agreements with computed shares (cessions, recoveries)
- the counterparty financial loop (balances, bordereaux/technical accounts, settlement, ledger hand-off)

**Standard capabilities** — present in most modern products:

- reinsurance claims machinery, contract lifecycle states, statutory reporting (Schedule F / IFRS 17 class), multi-entity/multi-currency/intercompany accounting, core-system integration, audit trails, analytics, placement simulation

**Common variants / optional** — depends on side of the market, line of business, and region:

- assumed-side and retrocession processing
- life-business allocation cycles vs P&C occurrence/catastrophe machinery
- London Market machinery (LORS, broker outputs) vs US statutory machinery
- hosting posture (cloud SaaS is the current market default; legacy estates persist)

## Interfaces

The surfaces below are described conceptually; exact layouts and names vary by product.

### Program / contract management view

The system's map of the reinsurance program.

- typical information: treaties and facultative placements with their scope, layers and inuring structure, financial terms, counterparties, periods, status; financial position per agreement
- primary actions: create or copy an agreement, configure terms and layers, renew, move to run-off, commute, inspect the program structure

### Cession / allocation workbench

Where the allocation computation is configured, run, and reviewed.

- typical information: incoming policy/premium/claim data, allocation results per agreement, calculation exceptions, posting status
- primary actions: run allocation cycles, review and correct exceptions, post computed cessions, adjust under control

### Claims & recoveries view

The recovery side of claims.

- typical information: claims and loss events linked to contracts, computed recoverable amounts, recovery status per claim and per counterparty, unclaimed-recovery indicators
- primary actions: match a claim to agreements, compute or recompute recoveries, bill a reinsurer, track collection, raise status requests

### Accounting & settlement

The money surface.

- typical information: balances per counterparty, bordereaux and technical accounts, receivables and payables, cash applications, currency and entity dimensions
- primary actions: produce accounts, execute settlements, apply cash, reconcile, close accounting periods, hand off to the general ledger

### Reporting & statutory output

- typical information: bordereaux per reinsurer/broker, premium and loss statements, statutory schedules (Schedule F class), IFRS 17 data extracts, audit trails
- primary actions: generate and distribute partner reports, produce regulatory outputs, export data

### Analytics / program overview

- typical information: ceded positions and exposures across the program, liabilities by counterparty and agreement, KPIs
- primary actions: drill into positions, compare periods, export for planning

## Important Rules / Behaviors

### Contract terms drive every computation

The agreement's wording — share, attachment, limit, commission, exclusions, inuring order — is the sole authority for what is ceded and what is recovered. The system's calculation engine exists to apply that wording mechanically; manual overrides are controlled exceptions, not the norm.

### Inuring order matters

Programs are stacks: one agreement's output can feed another (a quota share ceding into an excess-of-loss layer). The order of application is part of the program's configuration, and getting it wrong changes every computed figure.

### The money runs in both directions

Ceded premium flows out to reinsurers; recoveries flow back in. The system tracks both directions per counterparty, and settlement nets and reconciles them. A system that only computes cessions but cannot track the resulting receivables and payables is missing half the discipline.

### Claims leakage is the signature failure mode

A claim not matched to an applicable contract is a recovery silently lost. Mature products institutionalize the counter-measure: every claim is reviewed against the contracts, and unclaimed recoveries are surfaced as a managed worklist.

### Agreements outlive their periods

Expired agreements enter run-off rather than disappearing: outstanding balances continue to settle, late claims still recover, and audits still reach back. Commutation — the negotiated single-payment closure of an account — is the formal end, and even then the record remains.

### Renewal continues the relationship, not a new object

A renewed treaty carries its terms forward into a new period as a continuation of the same program structure, keeping the program's history inspectable across underwriting years.

### Every figure must survive reconciliation

Counterparties reconcile bordereaux line by line; regulators audit statutory reinsurance entries; finance reconciles to the general ledger. The system maintains audit trails behind every computed and posted amount — traceability is a structural requirement, not a feature.

### The system consumes the insurance core and feeds finance

Policy, premium, and claims data arrive from the policy administration and claims systems, which remain the record of the direct business; reinsurance results flow out to the general ledger and statutory reporting, which remain the record of the money. The reinsurance system holds the layer in between — the ceded/assumed position — and does not re-create either neighbor's record.

## Variants

- **By side of the market** — ceded-side systems for insurers (the largest population), assumed-side processing for reinsurers, and combined systems for groups that do both; retrocession (reinsurance of reinsurance) handled by the same structures where supported.
- **By line of business** — P&C machinery (per-risk, per-occurrence, and catastrophe/aggregate recoveries; statutory schedules) vs life machinery (periodic allocation of benefits and premiums to treaties; weekly or monthly bordereaux cycles). The core model holds across both; the cadence and computation shapes differ.
- **By regional machinery** — US statutory practice (Schedule F, annual-statement links), London Market practice (Lloyd's syndicates, outwards reinsurance standards, broker-facing outputs), and multi-country/multi-currency programs for global groups.
- **By packaging** — a dedicated reinsurance management platform; a beyond-core module inside an insurance suite (purchasable standalone or with the suite); a dual-deployment product that runs standalone against external policy systems or natively inside its vendor's suite; a finance-automation overlay that carries the treaty table and calculations on top of existing systems.
- **By scale posture** — mid-market carrier deployments vs large multi-national programs with intercompany treaties, pools, and affiliates on one platform.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Insurance Policy Administration System | upstream sibling | holds the **direct policies** sold to policyholders (parties × coverage × premium × period, governed lifecycle); this Type holds the **reinsurance agreements** between insurers and allocates PAS business to them. The cession is the bridge: PAS feeds policy/premium/claims data in. Suites ship them as separate products |
| Insurance Claims Management | downstream sibling | owns the loss lifecycle (FNOL → adjudication → payment); this Type consumes claim data and owns the **recovery** side — matching claims to contracts and collecting from reinsurers. A reinsurance claims surface inside this Type is the recovery view, not the adjuster's view |
| Broker Management Platform | different principal | reinsurance brokers place business and process bordereaux **on behalf of** cedents/reinsurers; this Type manages the insurer's or reinsurer's **own** treaty, cession, and settlement record. Same market, different seat |
| Insurance Underwriting Platform / Underwriting Workbench | decision-layer neighbor | assumed-side treaty underwriting decides which reinsurance contracts to write; this Type administers the agreed business (allocation, accounting, settlement). Placement simulation here is a capability, not the decision machinery |
| Actuarial Modeling Platform | model-vs-record neighbor | actuarial platforms model risk, pricing, and reserves (reinsurance appears as a management action inside models); this Type holds the contractual and financial record of actual reinsurance business |
| Billing Platform | money-execution neighbor | general billing executes invoices and payments; reinsurance settlement runs on treaty-driven technical accounts with two-directional balances — a distinct accounting discipline, though both hand off to the general ledger |
| Finance Process Automation platforms | thin-pole neighbor | an automation platform can carry a treaty table, allocation rules, and bordereaux output on top of existing systems; it becomes this Type when the agreement of record and the counterparty financial loop live inside it |

The boundary that matters most in practice is the master-record seam against policy administration: the same software families sell policy administration and reinsurance management as separate products precisely because the records differ — the direct contract with the policyholder versus the risk-sharing contract with other insurers.

## Representative Products

- **Sapiens ReinsurancePro** — dedicated cloud reinsurance management system for P&C carriers; ceded, assumed, and retroceded; treaty and facultative; from contract definition through statutory reporting
- **Sapiens ReinsuranceMaster** — the same family's platform for large and multi-national reinsurance programs; multi-country, multi-currency, intercompany; London Market requirements
- **Duck Creek Reinsurance** — beyond-core reinsurance management module on the Duck Creek platform; contract/partner management, claims, accounting, and reporting pillars; ceded and assumed (QBE reference deployment)
- **Sequel Re (Verisk Specialty Business Solutions)** — end-to-end outward reinsurance system for Lloyd's syndicates and London Market insurers; real-time calculation engine over outwards policies and inwards data
- **SolveXia** — finance-process automation platform applied to reinsurance (centralized treaty tables, bordereau calculations, recoveries) — the thin-pole realization that runs the allocation and reporting loop as an overlay on existing systems

## Sources

Research date: **2026-09-10**

- Sapiens — ReinsurancePro product page: https://sapiens.com/us/reinsurance/reinsurancepro/
- Sapiens — ReinsuranceMaster product page: https://sapiens.com/us/reinsurancemaster/
- Sapiens ReinsurancePro — Microsoft Marketplace listing: https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sapiens.sapiensreinsurancepro
- Duck Creek — Reinsurance product page: https://www.duckcreek.com/product/reinsurance/
- Duck Creek — Reinsurance Management brochure (2024) and data sheet (2023): https://www.duckcreek.com/wp-content/uploads/2024/06/20013_DuckCreek_Brochure_Reinsurance_Management_2024.pdf , https://www.duckcreek.com/wp-content/uploads/2023/01/Reinsurance_Data-Sheet.pdf
- Duck Creek — Reinsurance launch blog and press release (April 2026): https://www.duckcreek.com/resource/blog/modern-reinsurance-starts-here-introducing-duck-creek-reinsurance-with-active-delivery/
- Verisk Specialty Business Solutions — Sequel Re v5 announcement: https://www.verisksequel.com/news/latest-sequel-re-upgrade-enhances-competitive-advantages-for-lloyd-s-london-market-underwriters/
- SolveXia — financial services solutions page and reinsurance case studies: https://www.solvexia.com/solutions/financial-services , https://www.solvexia.com/case-study/reinsurance-bordereaux , https://www.solvexia.com/case-study/insurance-reinsurance-recoveries

> Sourcing limitation: vendor product pages, one vendor's marketplace listing, and vendor case studies were the directly fetched layer; the Duck Creek brochure/data-sheet content was taken from the search layer's verbatim extraction of the official-domain PDFs (direct fetch returned unparseable binary). No in-product help centers or user guides were reachable for any sampled product. The lifecycle and financial-loop descriptions here are calibrated to what those sources directly support; precise operational facts (exact state vocabularies, numeric limits, default settings, screen-level workflows) are deliberately not stated. The assumed-side workflow is described at the level of generality the sources support — assumed processing is evidenced as supported, but no sampled page details it at ceded-side depth.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical / market-sample breadth check are recorded in the paired Research Notes.
