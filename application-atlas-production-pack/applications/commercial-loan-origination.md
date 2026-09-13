# Commercial Loan Origination

## Overview

A **Commercial Loan Origination** application is the lending institution's staff-side system for carrying a business credit request from intake to a funded, booked loan.

The defining structure is small:

```text
Business borrower (with related parties: principals, guarantors, affiliates)
└── Credit request / deal in a managed lender-side pipeline
    └── Credit assessment built on the borrower's financial information
        └── Approval decision under the institution's credit policy
            └── Execution to funding, ending in a booking handoff
                (or a recorded decline / withdrawal)
```

Everything else commonly associated with modern loan origination — automated financial spreading, digital borrower portals, scoring models, e-signature, document automation, covenant monitoring — is widespread in current products but is not part of the defining core. A lender running on paper credit memos, hand-spread financial statements, and a loan committee operates the same process; the software digitizes, enforces, and records it.

When the system's center of gravity shifts to the funded loan book — payments, interest accrual, balances, payoff — the product is drifting toward a different Application Type (Commercial Loan Management). When it shifts to observing the book after booking, it becomes portfolio monitoring.

## Users & Context

The primary users are the lending institution's own staff. Commercial credit is negotiated and analyzed by people, and the software is their pipeline and record system:

- **Commercial lenders / relationship managers** — originate and structure requests, own the borrower relationship, move deals through the pipeline.
- **Credit analysts** — spread and analyze financial statements, compute cash-flow and coverage measures, draft the credit memo.
- **Credit officers / approvers** — review the analysis, make or recommend the credit decision within delegated authority.
- **Loan operations** — assemble closing documentation, track outstanding conditions and exceptions, complete booking.

Secondary users include risk and executive roles (policy oversight, portfolio visibility) and, where the product offers one, the borrower at the intake edge (application forms, document upload). Institutions range from community banks and credit unions to large regional and corporate banks and finance companies.

## Core Model

### The Defining Core

```text
Business borrower (+ related parties)
└── Credit request / deal in a managed pipeline
    └── Credit assessment from financial information
        └── Approval decision under credit policy
            └── Execution to funding / booking handoff
```

Five properties. If any one is removed, the product is no longer recognizable as commercial loan origination:

- **The business borrower as subject** — the population under assessment is organizations and their related parties (owners, guarantors, affiliates), not individual consumers. This is what makes the Type commercial.
- **The credit request as a managed pipeline object** — each request exists as a staged, institution-defined deal in a lender-side pipeline, and the system is the record of in-flight credit work. Without a managed pipeline, the product is a point tool.
- **Credit assessment from the borrower's financial information** — the decision rests on analyzed evidence of the borrower's financial condition. In commercial lending the characteristic form is spreading the borrower's financial statements into comparable form and analyzing cash flow and coverage; the general invariant is evidence-based assessment of financial capacity.
- **The approval decision under credit policy** — the request receives a recorded decision (approve, decline, or approve with conditions) through the institution's approval machinery. Policy rules govern routing and may auto-decide simple requests. Without policy-governed approval, the product is a generic application tracker.
- **Execution to funding** — approved requests are assembled into closable loans: terms structured, closing documentation produced and executed, outstanding conditions tracked. The process ends with the loan booked and handed to the servicing system — or with a recorded decline or withdrawal. Without this terminal credit execution, the product drifts toward CRM or a standalone decision engine.

### Standard Capabilities

Mature products carry most of the following. They are not what makes the product an origination system, but they are how the process is actually operated:

- **Financial spreading** — extraction and standardization of tax returns and financial statements into analyzable form, with controlled templates and traceability back to source documents. Automation of spreading is the modern realization; manual spreading is the degenerate case.
- **Global cash-flow / coverage analysis** — borrower-level analysis aggregating income across entities and sources, producing coverage-style measures that support the decision.
- **Credit memo** — the structured analysis document that supports the decision, commonly fed directly from the spread data; in current products sometimes drafted by AI for reviewer refinement.
- **Scoring and risk-rating models** — scorecards, stress-testing, and in-house or vendor-supplied models; policy parameters that determine which requests are auto-approved, auto-declined, or routed for manual review.
- **Task routing and approval workflow** — requests routed to reviewers and approvers with notifications, reassignments, and visible status.
- **Tickler / exception tracking** — tracked outstanding items (conditions to close, documents awaited, insurance, filings) that persist until cleared.
- **Document management and generation** — a repository with audit trail, generation of closing documents from the loan's data, and e-signature.
- **Covenant setup at underwriting** — covenants defined on the credit while it is being structured, with due-date tracking and notifications once booked.
- **Relationship view** — one view of the borrower relationship spanning credit and non-credit products, commonly fed from the institution's core systems.
- **Peer benchmarking** — borrower performance compared against industry peer data.
- **Integration spine** — connections to core banking/booking systems, credit bureaus, e-signature, identity verification, and document-capture services.
- **Audit trail and compliance reporting** — every analysis, decision, and document change is recorded; reports for regulators and auditors.

### One Structure, Many Implementations

```text
Concept:   Credit assessment from financial information
Forms:     automated spreading from documents, manual entry onto analysis
           templates, model-scored small-business applications

Concept:   Approval under credit policy
Forms:     multi-reviewer workflows, policy rules with auto-decisioning,
           committee-style review in larger institutions

Concept:   Execution to funding
Forms:     in-suite document generation, integration to a dedicated
           document engine, closing checklists with exception tracking
```

## How It Works

### Take in the request

```text
Borrower or lender starts a credit request
→ capture the borrower (entity, related parties, existing relationship)
→ record the request and purpose
→ policy screens the request (including, in some products,
   identity/KYC screening at intake)
→ the deal enters the pipeline at its first stage
```

Simple requests may be auto-approved or auto-declined by policy parameters; the rest proceed to analysis.

### Analyze the borrower

```text
Collect financial statements and tax returns
→ spread them into comparable form (automated or manual)
→ compute cash-flow and coverage measures, run projections
→ optionally score the request against models and peer data
→ draft the credit memo from the analysis
```

This is the step that most distinguishes commercial from consumer origination: the evidence base is the borrower's business financials, not a bureau score alone (though scored small-business variants exist — see Variants).

### Decide under policy

```text
Route the deal to reviewers and approvers per credit policy
→ reviewers assess analysis, structure, and risk
→ record the decision: approve (with terms and conditions),
   decline, or request more information
→ the decision, its basis, and its approvers are recorded
   for audit
```

### Close and book

```text
Structure the approved terms
→ generate closing documents from the loan's data
→ track outstanding conditions and documents until cleared
→ execute signatures (commonly e-signature)
→ book the loan and hand it to the servicing/booking system
```

The handoff is the boundary: from booking onward, the funded loan belongs to loan management (servicing). Origination systems do not run payment application, accrual, or the servicing ledger.

### Core vs Common vs Optional

**Defining core** — without these, not commercial loan origination:

- business borrower and related parties
- managed pipeline of credit requests
- credit assessment from financial information
- approval decision under credit policy
- execution to funding with a booking handoff

**Standard capabilities** — present in most mature products:

- spreading and global cash-flow analysis; credit memos
- scoring models and policy-based auto-decisioning
- approval workflows and task routing
- tickler/exception tracking; document generation and repository
- covenant setup; relationship views; audit trails; integrations

**Optional / variant** — depends on segment, geography, product family:

- digital borrower self-service intake; pricing/profitability analysis
- scored small-business machinery; government-guaranteed programs
- specialty asset-class editions; AI drafting and spreading

## Interfaces

The following surfaces are described in conceptual terms; exact layouts and names vary by product.

### Pipeline / deal list

The operator's work queue.

- lists in-flight requests with stage, owner, and status
- primary actions: open a deal, advance or reassign it, filter by stage or role

### Deal workspace

The request's record.

- borrower and related parties, requested terms, linked documents, workflow history
- primary actions: update terms, add parties or documents, move stages, record notes

### Spreading / financial-analysis worksheet

The analyst's bench.

- borrower financials in standardized form, calculated ratios and cash-flow measures, projections, peer comparison
- primary actions: import or extract statements, adjust classifications, run analysis, push results to the credit memo

### Credit memo

The decision document.

- structured analysis and narrative supporting the request
- primary actions: author or generate, attach evidence, submit for approval

### Approval queue

The approver's surface.

- pending decisions with analysis attached
- primary actions: approve, decline, set conditions, escalate, return for more information

### Tickler / exception list

The closing and post-approval tracker.

- outstanding conditions, documents, and filings with owners and due status
- primary actions: record receipt, clear or escalate items

### Document library

- repository of request, analysis, and closing documents with audit trail
- primary actions: upload, generate, send for signature, retrieve

### Dashboards / reporting

- pipeline throughput, approval status, compliance reporting for management, auditors, and regulators

## Important Rules / Behaviors

### Credit policy governs the pipeline

The institution's credit policy is embedded as configuration: routing rules, approval requirements, and auto-decision parameters. Requests that fit policy parameters can move without manual review; requests outside parameters are routed to people. This machinery — not the borrower — drives workflow behavior.

### Approval is recorded and attributable

A credit decision is an institutional act: who decided, on what analysis, under what conditions. The audit trail of analysis and approvals is a first-class record, not a byproduct — regulators and auditors are an assumed audience.

### Funding waits on conditions

An approved request does not fund itself. Closing proceeds while conditions and documents remain outstanding; the tickler/exception machinery exists because commercial closings are completed against tracked checklists. Covenants set at underwriting persist into the booked loan's life.

### The pipeline ends at booking

Origination's natural terminus is the booked loan handed to servicing. Covenant reminders or portfolio alerts may continue from origination-side records, but payments, accrual, and balance maintenance belong to the servicing system.

### Roles separate duties

Lending, credit, and operations are distinct roles with distinct permissions: the person who wins the relationship is commonly not the person who approves the credit, and closing is typically an operations function. This separation is structural in commercial credit, not incidental.

## Variants

- **Mid-market / community-bank LOS** — the classic commercial LOS: deal management, spreading, memos, ticklers, document management in one system sized for community banks and credit unions.
- **Relationship-platform suites** — origination as one workflow on a broader relationship platform whose deal object spans a borrower's credit and non-credit products.
- **Analytics-led suites** — origination built around models, scorecards, and vendor-supplied risk data; often packaged by asset class (commercial real estate, agriculture, small business).
- **Documentation specialists** — the closing-documentation layer as a standalone product: compliance-governed document generation fed by data from upstream origination systems.
- **Small-business scored lending** — high-volume, score-driven SMB variants (including scored, judgmental, and government-guaranteed program handling in the US market), sharing the same core with lighter analysis.
- **Specialty asset classes** — commercial real estate and agriculture editions with domain-specific analysis.
- **Borrower-self-service depth** — from secure document exchange to full digital application journeys.
- **Deployment and packaging** — cloud SaaS, vendor-hosted, or on-premise heritage; preconfigured editions for faster go-live.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Commercial Loan Management | owns the funded loan book — payment application, accrual, servicing ledger, life-of-loan changes; origination ends at the booking handoff |
| Loan Origination System (generic) | same pipeline family at sector-neutral scope; the commercial leaf is distinguished by business borrowers, financial-statement analysis, and credit-policy approval machinery |
| Consumer Lending Platform | individual borrowers, bureau-scored high-volume decisioning; no business-financial analysis machinery |
| Mortgage Origination Platform | residential-real-estate amortizing machinery (escrow, disclosures, investor workflows); commercial real estate lending is a variant of commercial origination, not of this |
| Credit Decisioning Platform | a standalone decision engine (rules/models as a service); origination embeds decisioning inside a full pipeline with analysis, memos, and closing |
| Credit Risk / Portfolio Monitoring platforms | observe the book after booking; covenant *setup* belongs to origination, ongoing covenant *management* and early-risk detection sit on the monitoring side |
| Commercial Banking Platform | the bank's client-facing relationship channel (surfacing held credit to the organization); origination is bank-staff pipeline work on prospective credit |
| CRM | manages relationships and opportunities generically; origination adds credit-policy approval, financial analysis, and closing execution that CRM lacks |
| Underwriting Workbench (insurance) | same word, different domain — insurance risk selection rather than credit approval |
| Deal Management for Private Equity / VC | manages investment deals and ownership economics, not credit requests under lending authority |

The boundary that matters most is funding: everything before booking is origination; the servicing ledger after booking is loan management.

## Representative Products

- nCino (Commercial Lending / CLOS)
- Baker Hill (UN/FY commercial lending suite)
- Moody's Lending Suite (Loan Origination)
- Finastra LaserPro / Originate Business Loans

The defining core was checked against this spread of poles — cloud platform, mid-market specialist, analytics-led suite, and documentation specialist — and against pre-digital practice (paper credit memos, hand-spread statements, loan committees, tickler files) to avoid defining the Type by any single era, region, or vendor pattern.

## Sources

Research date: **2026-09-07**

Primary vendor surfaces (product pages only):

- nCino — https://www.ncino.com/solutions/commercial-lending
- Baker Hill — https://bakerhill.com/commercial-lending , https://bakerhill.com/statement-spreading
- Moody's — https://www.moodys.com/web/en/us/solutions/lending.html , https://www.moodys.com/web/en/us/solutions/lending/loan-origination.html
- Finastra — https://www.finastra.com/lending/solutions/laserpro , https://www.finastra.com/lending

> Sourcing limitation: live fetch of vendor help centers and user guides was not possible in this research pass (login-walled source class); one major competitor in this category was unreachable (repeated server errors) and is unrepresented. All claims rest on official product pages; precise operational details — approval thresholds, stage counts, document templates, tickler-state names — are intentionally not stated. Some structures common in the industry (for example, collateral recording at underwriting) were not visible in the reachable documentation and are deliberately omitted rather than assumed.

Detailed evidence, product-by-product observations, the cross-product comparison, and the boundary analysis (including the funding seam established jointly with the Commercial Loan Management research pass) are recorded in the paired Research Notes.
