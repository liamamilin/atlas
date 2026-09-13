# KYC / KYB Platform

## Overview

A **KYC / KYB Platform** is an institution's customer-due-diligence compliance program made into software. For every person or business it intends to serve, the platform holds an accumulated due-diligence file, runs the institution's defined diligence steps against it — establishing identity, ownership, and background through verified evidence and screening — applies the institution's risk standards to reach a recorded decision on the relationship (approve, reject, or escalate to enhanced review), and keeps that file current and examinable for regulators across the whole life of the relationship.

KYC ("Know Your Customer") and KYB ("Know Your Business") are the two subject modes of the same program: KYC diligences an individual customer; KYB diligences a legal entity — its registry identity, its ownership structure, and its beneficial owners — and, in doing so, diligences the people behind it.

The defining core is deliberately small:

```text
Due-diligence case file of record (per person or business)
└── Diligence regime executed into the file
    │   (identity / registry / beneficial-ownership evidence + screening)
    └── Risk-based assessment → recorded relationship decision
        │   (approve / reject / enhanced due diligence)
        └── Standing, regulator-facing maintenance across the relationship
```

Everything else the category is known for — workflow builders, embedded capture SDKs, sanctions-list content, case queues, risk scores, registry integrations, event-driven refresh — makes the program practical at scale but is not what makes a product a KYC/KYB platform. A paper-era account-opening file with a certified ID copy, a list check, a risk note, a decision, and periodic-review stamps realizes the same core without any software.

This Type sits behind the neighbors it consumes: the identity verification act is one evidence step inside it; list screening is one regime step; transaction monitoring consumes its risk context downstream.

## Users & Context

The platform is operated by the organization that is obligated to know its customers — banks and fintechs foremost, but also marketplaces, crypto services, lenders, and any regulated or risk-bearing service business.

**Compliance and financial-crime staff** are the primary operators. Analysts work the files: inspect collected evidence, resolve screening hits, request more information, and record decisions. Senior reviewers own escalated files — the enhanced due diligence path for higher-risk subjects — and approve or reject with reasons. Team leads configure and supervise: which steps a file requires, which results auto-pass, which route to a human, and what the auditor will see.

**Integration and product engineers** connect the platform into the institution's own product: they trigger file creation from signup flows, embed the applicant-facing capture experience, and consume decisions and status changes through APIs and webhooks.

**The applicant** — the person or business being diligenced — is a user only at the capture surface: they enter company details, upload incorporation documents, complete questionnaires, or pass identity checks, usually inside the institution's own onboarding experience. In the corporate pole, outreach to the client (requesting documents and confirmations) is itself a managed part of the workflow.

**Typical contexts:** opening bank, payment, or brokerage accounts; onboarding corporate clients with layered ownership structures; admitting sellers, merchants, or borrowers to a platform; counterparty onboarding between institutions. The regulator-facing character is constant: the file exists so the institution can demonstrate, years later, that it knew who it served and why that was acceptable.

## Core Model

### The Defining Core

Four structures, jointly held. Removing any one leaves a product that is no longer this Type:

- **The due-diligence case file of record.** One persistent, individually identified compliance record per diligence subject — an individual customer or a legal entity — held by the relying institution. The file accumulates everything the program learns and does: declared information, verified identity and ownership evidence, collected documents, screening results, questionnaire answers, and the history of diligence actions. Without an accumulated file, the product is a set of one-shot checks that return results and remember nothing.
- **The diligence regime executed into the file.** The institution defines what must be established — who the subject is (identity documents, biometric or database verification, corporate registry data, beneficial ownership), and whether anything disqualifies them (sanctions, politically-exposed status, adverse media) — and the platform carries those steps out, recording each result into the file. Execution may be the platform's own checks, delegated data sources and verification vendors, or reviewer work; the invariant is that the regime runs as one orchestrated process on the file, not as disconnected tools the institution must stitch together.
- **Risk-based assessment producing a recorded relationship decision.** The institution's configured standards are applied to the assembled file to classify the risk the subject presents, and the outcome is a recorded decision on the relationship — approve, reject, or escalate to enhanced due diligence — attributed to a decision-maker with reasons. This is a judgment about the relationship, not merely a pass/fail on individual checks. Without it, the product is a collection utility.
- **Standing, regulator-facing maintenance.** The file does not close at approval. It is retained as compliance evidence, every action on it is attributed and timestamped, and it is refreshed as diligence obligations recur — periodic reviews, rescreening when lists change, re-review when registry or ownership facts change. Without standing maintenance, the product is a one-time onboarding act whose evidence lives somewhere else.

### What Mature Products Add

Around that core, mature products carry a stable set of standard capabilities:

- **Program configuration surfaces** — verification levels, inquiry templates, policies, or process-automation builders through which the institution defines the required steps, the automatic outcomes, and the exceptions that must reach a human.
- **Applicant-facing capture** — embedded SDKs, hosted flows, verification links, or structured client outreach that collect the evidence and declarations the regime requires.
- **Screening machinery** — sanctions, watchlist, PEP, and adverse-media data sources; fuzzy name matching; match resolution with true/false-positive dispositions recorded against the file.
- **Manual-review case machinery** — queues where flagged files are assigned, worked with notes and SLAs, and decided; escalation and hand-off between reviewers.
- **Risk scoring and rules** — computed risk scores or labels, country and channel rules, and the conditions that route low-risk subjects to straight-through approval while concentrating human attention on higher-risk ones.
- **Ongoing-monitoring machinery** — rescreening on list updates, monitoring of registry filings, bankruptcies, liens, and ownership changes, surfacing of what changed since the last review, and remediation or refresh campaigns over the existing book.
- **KYB structure machinery** — corporate registry sources, ownership-structure assembly, beneficial-owner determination against configurable ownership thresholds, and per-associated-party diligence with status synchronization into the company's outcome.
- **Audit and reporting** — decision trails, data lineage, and exportable, examiner-ready reports.

### One Structure, Many Implementations

The core is written conceptually; products realize it differently:

```text
Concept:  the diligence subject
Realized as: applicant profile (individual or company) · account grouping a person
or business's whole history · business object with associated people ·
corporate digital identity profile

Concept:  the diligence regime
Realized as: verification levels and workflow builders · inquiry templates with
report actions · ordered report catalog over a business object ·
process automation over registry data

Concept:  the recorded decision
Realized as: applicant approval statuses · inquiry approve/decline/needs-review ·
client approval on verification insights · audit-ready decision trails

Concept:  standing maintenance
Realized as: ongoing list rescreening · registry/bankruptcy/lien monitoring ·
recurring re-verification · event-triggered profile refresh (perpetual KYC)
```

A reader who has only seen one implementation — say, an API-first fintech verification stack — should still be able to recognize an enterprise corporate-onboarding platform as the same Type from this model.

## How It Works

### Open a file and run the regime

```text
Subject appears (signup, referral, outreach list)
→ file created and linked to the institution's own customer record
→ applicant completes capture steps (details, documents, identity checks)
→ platform gathers registry data and beneficial-ownership facts (KYB)
→ screening runs against sanctions / PEP / watchlists / adverse media
→ results assemble in the file
```

Low-risk files with clean results can pass automatically under the institution's configured rules. Anything incomplete, inconsistent, or flagged becomes a review case.

### Decide the relationship

```text
Reviewer (or automation) assesses the assembled file
→ screening hits resolved as true / false positives, with reasons
→ risk assessed against the institution's standards
→ decision recorded: approve · reject · escalate to enhanced due diligence
→ enhanced path gathers deeper evidence (source of funds, ownership detail,
   questionnaires) and ends in a recorded decision by a senior reviewer
→ decision communicated; the institution's systems admit or refuse the subject
```

The decision is the program's gate: it is attributed, reasoned, and retained on the file.

### Maintain the file over the relationship

```text
Approved file stays under standing diligence
→ list changes rescreen the subject; registry/ownership changes surface
→ material changes reopen the file (with a view of what changed since last review)
→ periodic reviews re-run the regime on schedule or on trigger
→ refreshed file re-decided; every step attributed and retained
```

The recurring cycle, not the one-time gate, is what makes the platform a *program* of record rather than an onboarding tool.

### KYB in the same loop

For a business subject, the same loop runs with the legal entity at the center: registry identity established and cross-checked against declared data, ownership structure assembled, beneficial owners determined against the institution's ownership thresholds, each associated party (directors, shareholders, representatives, UBOs) put through individual diligence, and the parties' outcomes synchronized into the company's overall decision — one rejected beneficial owner can reject the company, under the institution's configuration.

### Core vs Common vs Optional

**Defining core** — without these, not this Type:

- due-diligence case file of record per subject
- diligence regime executed into the file (identity/ownership evidence + screening)
- risk-based assessment with a recorded relationship decision
- standing, regulator-facing maintenance of the file

**Standard capabilities** — present across mature products:

- program configuration surfaces; applicant-facing capture
- screening content, matching, and match resolution
- manual-review cases; risk scoring; ongoing monitoring
- KYB registry/UBO machinery with associated-party synchronization
- audit trails and exportable reports; APIs and webhooks

**Common variants / optional** — depend on segment and posture:

- event-driven continuous refresh (perpetual KYC) as the modern maintenance model
- reusable verified identity across services; in-product transaction monitoring
- managed-service operation where the vendor runs review on the institution's behalf
- adjacent extensions (crypto travel rule, e-signature, fraud signals)

## Interfaces

Described conceptually; names and layouts vary by product.

### Case file / applicant profile

The spine of the product.

- purpose: hold everything known and decided about one subject
- typical information: declared details, verification and registry results, ownership structure, screening matches, documents, questionnaire answers, status, decision history
- primary actions: request checks, review results, resolve matches, add notes and documents, record a decision, change status

### Program configuration

Where compliance teams define the regime.

- purpose: express the institution's diligence standards as runnable configuration
- typical information: required steps per subject type or risk tier, automatic outcomes, routing rules, ownership thresholds, screening scope
- primary actions: compose steps and rules, set thresholds, version and publish configurations

### Review queue / case management

Where exceptions become decisions.

- purpose: work flagged or incomplete files to a recorded outcome
- typical information: prioritized list of open cases, assignment, SLA and aging, per-case evidence bundle
- primary actions: assign, investigate, resolve hits, escalate, decide, export

### Applicant capture surface

What the subject experiences.

- purpose: collect declarations, documents, and identity evidence with the least friction the regime allows
- typical information: step-by-step flow, status and resubmission requests
- primary actions: enter data, upload documents, complete identity checks, sign

### Monitoring / portfolio view

Where the standing program is watched.

- purpose: surface what changed across the approved book
- typical information: rescreening alerts, registry and ownership changes, review-backlog state, portfolio risk view
- primary actions: open affected file, assess what changed, re-decide or schedule review

### Audit / reporting surface

What the regulator and auditor see.

- purpose: demonstrate the program operated as configured
- typical information: per-file decision trail, data provenance, configuration history, exports
- primary actions: filter, export, retain

## Important Rules / Behaviors

### The file outlives the decision

Approval is not the end state. The file remains under standing diligence: list changes, registry changes, and scheduled reviews reopen it. In mature implementations a material change on an approved subject can strip the approval automatically until re-reviewed.

### The decision is a judgment, not a check result

Individual checks yield pass/fail signals; the relationship decision weighs them against the institution's risk standards. This is why clean checks can still end in rejection, and why failed checks can still end in a documented approval — always with recorded reasons.

### Subject identity is defended against duplication

Mature platforms link a subject's attempts over time (one person, one file) so patterns surface across onboarding and re-verification, and so a previously rejected identity cannot re-enter anonymously.

### KYB decision is synchronized with the people behind the business

A company's outcome depends on its associated parties' outcomes under configurable rules; ownership thresholds determine who must be diligenced, and skipped or unidentifiable parties are themselves a recorded, rule-governed outcome.

### Screening matches are resolved, not just reported

A screening hit is the beginning of a recorded disposition — true match, false positive, or escalation — attributed and retained. Unresolved hits block the decision under the institution's rules.

### Every action is attributable evidence

Because the file is regulator-facing, actions taken in the platform are recorded with actor, time, and reason. Data extracted from external sources carries its provenance, and conflicts between applicant-declared and registry-sourced data are preserved rather than silently overwritten.

### Automation is bounded by configuration

What passes automatically, what routes to review, and what declines outright is the institution's configuration, not the vendor's. Two institutions on the same platform run visibly different programs.

## Variants

Common shapes of the Type:

- **Full-program platforms** — KYC and KYB, screening, cases, and monitoring in one product, sold to fintechs and financial institutions of many sizes.
- **Orchestration-first platforms** — modular check and report building blocks with strong automation and API surfaces, letting the institution compose its own regime and mix external data sources.
- **KYB-first business-identity platforms** — the legal entity as the primary object, deep on registry and business-signal coverage (registrations, TIN/tax identifiers, liens, bankruptcies), with person-level diligence delegated to partners.
- **Enterprise corporate-onboarding platforms** — registry-data-led automation for banks onboarding complex, multi-jurisdiction corporate clients; beneficial-ownership depth, data lineage, and event-driven refresh (perpetual KYC) are the emphasis.
- **Subject-axis variants** — individual KYC, business KYB, or both in one program; the program model is shared.
- **Operating-posture variants** — self-operated review, managed service where the vendor's analysts work the files, and hybrid expert-assisted models for hard cases.
- **Regulatory-regime emphasis** — FATF-style risk-based CDD is the shared frame; regional regimes (US account-opening rules, EU AML directives) shape required steps and record formats rather than the program model.

A variant that stopped holding files, assessing relationship risk, or maintaining records — leaving only capture and checks — would have crossed into the Identity Verification Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Identity Verification | consumed step | centers the verification act — evidence capture, check evaluation, and a decision on a claimed identity, returned to the relying organization; here it is one evidence step inside an accumulated compliance file |
| Sanctions Screening Platform | consumed step / adjacent | centers the prohibited-party determination: lists brought in, a screened population, matches resolved to dispositions as the terminal artifact; here screening is one regime step whose results feed the file |
| AML Platform | downstream consumer | monitors customer *activity* and ends in suspicious-activity reports; it consumes the customer-risk context this Type produces; the terminal artifact differs (SAR/STR vs the recorded relationship decision) |
| Transaction Monitoring Platform | downstream consumer | detects suspicious behavior in the institution's transaction stream and ends at the dispositioned alert; no diligence file, no admission gate |
| Fraud Prevention Platform | adjacent | decides risky activity to prevent loss, with fraud economics as the feedback loop; this Type proves diligence to a regulator as the obligation |
| Background Check Platform | adjacent | screens a person's history for employment decisions; no relationship risk classification or standing compliance file |
| Government Digital Identity | adjacent | state-run identity issuance and federation; not an institution's private compliance program |
| Due Diligence Platform | naming neighbor, different object | diligence on a transaction or investment (M&A-grade documents and analysis), not on a customer relationship for regulatory admission |
| Customer Onboarding Platform | adjacent | orchestrates the onboarding journey and commercial steps; may call into this Type but does not hold the diligence regime or the compliance gate |
| CRM | adjacent | commercial customer records and activity history; no compliance evidence semantics, screening regime, or admission gate |

The boundary that matters most in practice is with **Identity Verification**: the same vendor often sells both, and "KYC" appears in the market as a packaged use case over verification machinery. The working distinction is object-model-shaped — if the center of gravity is the verification attempt, it is identity verification; if it is the accumulated diligence file with its risk decision, screening regime, and standing maintenance, it is this Type.

## Representative Products

- Sumsub — full-cycle compliance platform spanning KYC, KYB, screening, cases, and monitoring
- Persona — modular identity and compliance orchestration platform
- Middesk — KYB-first business identity and compliance platform
- Encompass — enterprise corporate-KYC automation (corporate digital identity, perpetual KYC)

These were chosen to span the market's poles: API-first fintech tooling, full-program suites, business-entity depth, and enterprise bank-grade corporate onboarding.

## Sources

Research date: **2026-09-08**

- Sumsub — documentation site: overview, business verification, verify-businesses, case management, AML screening, ongoing AML monitoring — https://docs.sumsub.com/
- Persona — developer documentation: API introduction, inquiries, accounts, cases, workflows, verifications — https://docs.withpersona.com/
- Middesk — developer documentation: how Middesk works, lifecycle of a business, verify a business (KYB), monitor business activity — https://docs.middesk.com/
- Encompass — official site and perpetual KYC product page — https://www.encompasscorporation.com/

> Sourcing limitations: Persona's KYC solution marketing page was not reachable (403); its KYC packaging is evidenced from its developer documentation. Encompass was studied at official product-page level, so its operational specifics are stated only conceptually. Precise regulatory figures (retention periods, review frequencies) are intentionally not asserted — no fetched source supported exact numbers. Detailed product-by-product evidence is in the paired Research Notes.
