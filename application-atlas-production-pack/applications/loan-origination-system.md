# Loan Origination System

## Overview

A **Loan Origination System (LOS)** is the lender's staff-side system for carrying a credit request from intake to a funded loan. It keeps each application as a persistent case, moves it through the lender's own origination stages, assembles and verifies the evidence the decision rests on, evaluates the applicant under the lender's credit policy, records the decision — approve with terms, decline with reasons, or refer — and executes approved applications to funding, ending in a booking handoff to the loan record that the servicing side will carry forward.

Its defining structure is small:

```text
Credit application (case of record)
└── Lender-side origination pipeline
    └── Credit evaluation under the lender's policy
        └── Recorded decision executed to funding
            (booking handoff — or recorded decline / withdrawal)
```

Everything else commonly associated with modern loan origination — digital borrower portals, e-signature, credit-bureau APIs, open-banking data pulls, AI decision engines, document generation — is widespread in current products but is not part of the defining core. A lender running on paper application forms, desk-to-desk loan files, a policy manual, and minuted committee approvals operates the same process; the software digitizes, enforces, and records it.

The Type is deliberately segment-neutral. The same core holds for a consumer lender auto-deciding small personal loans, a credit union processing personal and auto applications, and a bank running committee-governed commercial facilities. What changes with the borrower population is the evidence class and the surrounding machinery — not the structure. Sector-scoped siblings (commercial, mortgage, consumer-lifecycle) are documented as separate Application Types.

## Users & Context

The primary users are the lending institution's own staff:

- **Processors / intake staff** — capture applications, chase outstanding information, keep the case moving through early stages.
- **Verification and data staff** — confirm identity and documents, enter or validate financial data, run the checks the policy requires before evaluation.
- **Underwriters / credit officers** — assess the evidence, apply or exercise the credit policy, and make or recommend the decision within their delegated authority.
- **Closing / funding operations** — complete the approved application: documents generated and signed, conditions cleared, funds disbursed, loan booked.

Secondary users include administrators (who configure loan products, application flows, and decision parameters), risk and compliance roles (audit and regulator-facing reporting), and the **borrower**, who in many products appears at the intake and notification edge — applying online, uploading documents, tracking status, signing, and cancelling. Some products add third-party channels: agents, brokers, or dealers who originate applications on the borrower's behalf.

Typical operators span banks, credit unions, consumer and commercial finance companies, fintech lenders, microfinance institutions, and embedded/point-of-sale finance providers. The work context is a pipeline: applications arrive continuously through multiple channels, and the institution's daily credit work is organized around moving them to a decision and, for the approved, to funding.

## Core Model

### The Defining Core

```text
Credit application (case of record)
  one persistent, individually identified case per request for credit,
  carrying the applicant (person or organization), the requested credit,
  and the evidence file — reachable from every intake channel
└── Lender-side origination pipeline
    the case advances through the lender's own defined stages from intake
    toward funding; the system is the record of in-flight credit work —
    status, ownership, history
└── Credit evaluation under the lender's policy
    applicant data assembled from defined sources and verified — identity,
    financials, credit history, bank data, collateral — then assessed against
    the lender's credit policy through configurable machinery: automated
    rules/scores/models, human underwriting, or hybrid routing
└── Recorded decision executed to funding
    approve with final terms / decline with reasons / refer — recorded with
    basis and actor as an audit-ready institutional act; approved cases are
    completed as fundable loans (agreement, conditions, disbursement) and
    handed to the loan record; decline, withdrawal and cancellation are
    recorded terminal outcomes
```

Four properties. If any one is removed, the product is no longer recognizable as a loan origination system:

- **The application as case of record** — each request for credit exists as an individually identified, persistent case, whatever channel it arrives through (borrower self-service, staff entry, agent or broker submission). Without a case, the product is a set of disconnected point tools.
- **The lender-side pipeline** — the case is tracked through the institution's own stages, and the system is the authoritative record of in-flight credit work: what stage each application is at, who owns it, what has happened to it. Without a managed pipeline, the product is a decision service or a form tool.
- **Evaluation under the lender's credit policy** — the decision rests on evidence: data assembled from the applicant and external sources, verified, then assessed against policy. The machinery is configurable — automated rules, scores, and models; human underwriters; or a hybrid that routes by policy parameters. Without policy-governed evaluation, the product is a generic workflow tracker.
- **The recorded decision executed to funding** — the decision is an institutional act (outcome, terms or reasons, actor, basis), retained for audit; approved applications are carried through agreement execution, conditions, and disbursement to the booking handoff. Without the funding execution, the product drifts toward a standalone decision engine; without the recorded decision, it is paperwork software.

### Standard Capabilities

Mature products carry most of the following. They are not what makes the product an origination system, but they are how origination is actually operated:

- **Digital borrower application** — online application forms, document upload, status tracking, notifications, and cancellation; commonly mobile-first and configurable per product.
- **Data assembly and verification** — identity verification and KYC/AML checks, credit-bureau reports, bank-account and bank-statement data, fraud rules and blacklists, open-banking pulls; failures in data collection can terminate or pause the application.
- **Contract and document machinery** — agreement generation from templates, e-signature, a document repository bound to the case, and conditions/exception tracking that persists until cleared.
- **Configurable loan products** — amount, term, rate, and fee structures defined as data that drives application forms, offers, and decision parameters.
- **Collateral handling** — collateral requirements, verification, and valuation measures (such as loan-to-value) at approval for secured products.
- **Task and queue management** — verification, financial-data, and decision tasks routed to staff by role, with reassignment and escalation.
- **Reporting and analytics** — funnel throughput, decision outcomes, and portfolio metrics; pricing and rate adjustments.
- **Audit and compliance surfaces** — time-stamped decision and configuration logs, policy-linked document trails, and regulator/auditor-facing reports.
- **Integration spine** — credit bureaus, identity/fraud services, e-signature, payment rails, core banking/booking systems, and external decisioning or scoring services.
- **Third-party origination channels** — agent/broker portals, dealer (indirect) submission, and partner networks that create applications on borrowers' behalf.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. Implementations differ in how each concept is realized:

```text
Concept:   Evaluation machinery
Forms:     AI/ML decision engines scoring instantly · policy rule sets with
           auto-approve / auto-decline / manual-review parameters ·
           human underwriters and committees working recorded cases

Concept:   The pipeline
Forms:     configured stage sequences with per-stage tasks · policy
           parameters that skip stages for simple requests · committee
           review for large or exceptional ones

Concept:   Intake channels
Forms:     borrower self-service portals · staff-entered applications ·
           agent/broker/dealer submissions · embedded point-of-sale flows

Concept:   Execution to funding
Forms:     in-suite agreement generation and e-signature · document-engine
           integrations · disbursement through payment rails · booking
           into a servicing system or the institution's core
```

A reader who has only seen one implementation (for example, an instant-decisioning consumer lender) should still be able to recognize a committee-driven commercial origination desk as the same Type from the Core Model.

## How It Works

### Take in the application

```text
Borrower, staff member, or partner channel starts an application
→ capture the applicant and the requested credit
→ collect the required data (identity, financials, bank account,
  collateral where applicable)
→ run intake checks (identity, blacklist, duplicates)
→ the application becomes a tracked case in the pipeline
```

Products commonly converge every channel onto the same case structure, so an application started by a borrower online and one entered by staff on their behalf look the same to the pipeline. Duplicate handling is part of intake hygiene: in some products a fresh application supersedes the borrower's still-open previous one.

### Assemble and verify the evidence

```text
Pull or collect the data the policy requires
→ credit-bureau report, bank data, financials, collateral details
→ verify identity and documents
→ record what was checked, when, and with what result
```

The evidence file is built before evaluation, and its assembly is itself tracked: some products treat verification as a configurable stage (skipped for simple products, staffed for others), and a failure in data collection can terminate the application as an error case.

### Evaluate and decide

```text
Run the policy-configured evaluation
→ automated checks and screening first (policy screens, stop rules)
→ scoring and credit-limit computation where configured
→ routing per policy parameters:
     auto-approve on the requested terms, or
     send to an underwriter, or
     auto-decline
→ underwriter decision: approve (final amount, term, rate, product),
  decline (with reason), or return for more information
```

The same institution can run some products fully automatically and others through human underwriting — the routing is configuration, not architecture. In commercial-flavored deployments, evaluation is anchored in the borrower's business financials; in consumer-flavored ones, in bureau scores and verified personal data. The structure — evidence assessed under policy, decision recorded — is the same.

### Complete, fund, and book

```text
Record the approval with final terms
→ generate the agreement and obtain signatures
→ clear outstanding conditions (documents, insurance, filings)
→ disburse funds
→ book the loan and hand it to the loan record
```

The booking handoff is the boundary: from funding onward, the loan belongs to the servicing side (loan management). Origination systems track conditions to completion and may keep covenant reminders from origination-side records, but payment application, accrual, and balance maintenance are not origination work.

### Terminal outcomes

Not every application funds. Decline (with recorded reasons, whether automatic or human), borrower cancellation, withdrawal, and lapse (an offer not taken up in time) are all recorded outcomes of the same pipeline — the system of record for the institution's credit decisions, not only its approvals.

### Defining core, standard capabilities, and variants at a glance

**Defining core** — without these, not a loan origination system:

- application as case of record
- lender-side pipeline
- evaluation under the lender's credit policy
- recorded decision executed to funding

**Standard capabilities** — present in most mature products:

- digital borrower application and notifications
- data assembly and verification (identity, bureau, bank data, fraud)
- contract/document machinery and conditions tracking
- configurable loan products and process flows
- collateral handling; task queues; reporting; audit surfaces; integrations

**Variant** — depends on segment, channel, and packaging:

- decisioning philosophy (instant AI decisioning vs policy rules vs committee)
- third-party channels (agents, brokers, dealers, embedded)
- regulatory regime machinery (disclosures, adverse-action outputs)
- packaging depth (standalone origination vs end-to-end lending suite)

## Interfaces

The following surfaces are described in conceptual terms; exact layouts and names vary by product.

### Pipeline / application queue

The staff work surface.

- lists in-flight applications with stage, owner, status, and age
- primary actions: open a case, work its next task, reassign, filter by stage or channel

### Application workspace (case record)

The case's home.

- applicant details, requested credit, evidence file, documents, verification results, workflow history, notes
- primary actions: update data, add documents or parties, run checks, record notes, advance or return the case

### Decision surface

The underwriter's bench.

- the case's evidence and analysis with pending decision
- primary actions: approve with final terms, decline with reason, request more information, escalate

### Configuration console

The administrator's machinery.

- loan products (amount/term/rate/fee structures), application flows and forms, decision rules and routing parameters, scoring-model settings, document templates, notification templates
- primary actions: create or edit products and flows, adjust decision parameters, publish changes

### Borrower application surface

The borrower's window on the pipeline.

- application form, document upload, status tracking, requested and final conditions, agreement signing, cancellation
- primary actions: apply, respond to information requests, sign, cancel

### Partner / channel surface

The third-party originator's window (where offered).

- application creation on behalf of borrowers, case visibility, commission or performance views
- primary actions: submit an application, track its progress

### Reporting and dashboards

- funnel and decision analytics, throughput, portfolio metrics, compliance reports for management, auditors, and regulators

## Important Rules / Behaviors

### Credit policy drives the pipeline

The institution's credit policy is embedded as configuration: routing rules, verification requirements, auto-decision parameters, and stop rules. Applications that fit policy parameters can move without manual review; applications outside parameters are routed to people. This machinery — not the applicant — decides how work flows.

### The decision is a recorded institutional act

Who decided, on what evidence, under which policy configuration, with what terms or reasons — all retained and commonly time-stamped. The audit trail is a first-class record for regulators and auditors, not a byproduct. Automated decisions are logged with the same care as human ones, including the inputs and model versions that produced them.

### An approval is not yet a funded loan

Between approval and funding stand the agreement, signatures, outstanding conditions, and (for secured products) collateral valuation. Products track these as explicit completion steps, and disbursement waits on them; in some products the proposed repayment schedule is validated before approval, and a schedule that fails validation declines the application. Offers can lapse if not taken up in time.

### The pipeline ends at booking

Origination's natural terminus is the funded loan handed to the loan record. Covenant reminders or portfolio alerts may continue from origination-side records, but the servicing loop — billing, payment application, accrual, balance maintenance — belongs to the servicing system.

### Roles separate duties

Intake, verification, underwriting, and closing are distinct functions with distinct permissions: the person who wins the relationship is commonly not the person who approves the credit, and funding is typically an operations function. This separation is structural in lending, not incidental.

### Every exit is recorded

Declines carry reasons (whether set by policy or by a person); cancellations and withdrawals are recorded with their cause; error cases leave a trace. The origination system is the institution's record of credit decisions, including the ones it did not make.

## Variants

- **Consumer direct-lending LOS** — high-volume, digitally self-served applications, bureau-anchored evaluation, instant or near-instant decisioning; common in personal, auto, BNPL, and microfinance lending.
- **Commercial origination LOS** — staff- and deal-mediated intake, financial-statement evidence, structured approval chains and committee review; the sector-scoped sibling is documented separately.
- **Bank/credit-union multi-line LOS** — one origination environment spanning personal, auto, card, home-equity, business, and indirect lines, often as the lending core of a broader digital-lending platform that also connects deposit account opening.
- **End-to-end lending suite** — origination packaged together with loan servicing and collections on one platform; the origination core is unchanged, but the product spans the funded life of the loan as well.
- **Indirect and embedded origination** — dealer, broker, agent, and point-of-sale channels originating on borrowers' behalf, with the lender operating the decision and funding machinery behind the channel.
- **Deployment and regional editions** — cloud SaaS is dominant in the current market, with vendor-hosted and on-premise heritage forms persisting; regional regulatory machinery (disclosure documents, adverse-action outputs, jurisdiction-specific checks) varies by market without changing the core.

A variant remains a **Variant** unless it changes users, core objects, workflow, or rules so fundamentally that the Core Model no longer applies — in which case it is documented as its own Application Type (as the commercial and mortgage siblings are).

## Related Application Types

| Application Type | Distinction |
|---|---|
| Loan Management System | owns the funded loan book — billing, payment application, accrual, life-of-account changes; origination ends at the booking handoff. End-to-end suites package both; the documented pre-funding pipeline is what makes a product an LOS |
| Consumer Lending Platform | borrower-segment-scoped lifecycle platform (origination through servicing and collections for individual borrowers); the generic LOS is stage-scoped and segment-agnostic |
| Commercial Loan Origination | sector-scoped sibling: business borrowers, financial-statement assessment machinery, committee-style approval; same pipeline family at commercial depth |
| Mortgage Origination Platform | sector-scoped sibling built around residential-real-estate amortizing machinery (escrow, disclosures, investor workflows); the generic LOS carries no collateral-regime machinery of its own |
| Credit Decisioning Platform | the evaluation engine invoked at decision points — rules, models, and strategies as a service; an LOS embeds evaluation inside a full case pipeline with documents, conditions, and funding |
| Credit Scoring Application | produces a credit measure; the LOS consumes measures among other evidence and produces the recorded decision |
| Credit Management Platform | ongoing trade-credit governance (limits, reviews, holds) over customers buying on open account — not the origination of credit requests |
| CRM | manages relationships and opportunities generically; origination adds credit-policy evaluation, evidence-based assessment, and funding execution that CRM lacks |
| KYC / Identity Verification and Fraud Prevention platforms | point checks consumed inside the pipeline; the LOS is the pipeline they feed |
| Underwriting Workbench (insurance) | same word, different domain — insurance risk selection rather than credit approval |
| Financial Aid Management | records and certifies awards from set-aside funds; origination evaluates and holds credit for repayment |

The boundary that matters most is funding: everything before booking is origination; the servicing ledger after booking is loan management. The boundary that matters most architecturally is evaluation: decisioning and scoring are capabilities inside the pipeline; standalone, they are different Types.

## Representative Products

- MeridianLink (loan origination software; consumer, mortgage, business, and indirect lines for banks and credit unions)
- TurnKey Lender (segment-neutral cloud lending platform with an explicitly named loan origination system)
- HES LoanBox (configurable multi-segment lending platform; one engine across personal and business borrowers)
- nCino (commercial loan origination system for banks)

The defining core was checked against this spread of poles — bank/credit-union, segment-neutral SaaS, configurable fintech SaaS, and enterprise commercial — and against pre-digital practice (paper application forms, desk-to-desk loan files, policy manuals, minuted committee approvals) to avoid defining the Type by any single era, region, or vendor pattern.

## Sources

Research date: **2026-09-08**

Primary vendor surfaces (product pages, FAQ, and one official product-documentation portal):

- MeridianLink — https://www.meridianlink.com/solutions/loan-origination-software/ (solution page incl. FAQ)
- TurnKey Lender — https://www.turnkey-lender.com/loan-origination-system/ , https://www.turnkey-lender.com/
- HES FinTech — https://hesfintech.com/loan-origination-software/ ; https://docs.hesfintech.com/ (documentation portal: application process, loan origination process step-by-step)
- nCino — https://www.ncino.com/solutions/commercial-lending

Corroborating sibling research passes (same repository): commercial-loan-origination, consumer-lending-platform, loan-management-system, credit-decisioning-platform, credit-scoring-application, commercial-loan-management.

> Sourcing limitation: vendor help centers and client knowledge bases for the sampled products are login-walled support surfaces and were not reachable in this pass (consistent with the earlier lending-family passes). Claims therefore rest on official product pages, vendor FAQs, and one Tier-1 product-documentation portal. Precise operational parameters — stage counts, timeout defaults, limit formulas, document-template specifics — are intentionally not stated; vendor performance figures quoted in marketing are treated as claims, not facts.

Detailed evidence, product-by-product observations, the cross-product comparison, and the boundary analysis (including the funding seam established jointly with the Loan Management System and Commercial Loan Management research passes) are recorded in the paired Research Notes.
