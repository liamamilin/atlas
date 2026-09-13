# Third-party Cyber Risk Platform

## Overview

A **Third-party Cyber Risk Platform** is the buying organization's system of record for the cybersecurity risk posed by its third parties — the vendors, suppliers, and service providers it depends on. It keeps a standing population of vendor records, evaluates each vendor's security posture from evidence, and manages every evaluation result to a recorded resolution with the vendor.

The problem it solves: organizations exchange sensitive data and operational access with hundreds of external parties, and each party's security weaknesses become the organization's own risk. Manual approaches — spreadsheets, email questionnaires, ad hoc reviews — cannot keep a defensible, current picture across a whole vendor ecosystem. The platform turns that practice into a managed program: know your vendors, know their security standing, and resolve what you find.

The defining core is small:

```text
Third-party population under cyber assessment
└── Per-vendor security evaluation → comparable security standing
    └── Decision-and-resolution loop → recorded closure
```

Everything else the market commonly ships — continuous monitoring, tiering machinery, questionnaire engines, vendor portals, discovery, compliance mapping — makes the program practical but is not what makes the product this Type.

## Users & Context

Primary users sit in the buying organization's security function:

- **TPRM / vendor risk analysts** — run the day-to-day program: add and tier vendors, send assessments, review results, chase findings to resolution
- **Security engineers / CISO office** — consume the aggregated picture, set risk policies and thresholds, own escalations
- **Business owners** (product, HR, finance, IT teams who actually use a given vendor) — nominate vendors at intake and hold relationship context such as business impact and data shared

Secondary participants:

- **Vendor-side contacts** — the assessed party. They receive questionnaires, remediation plans, and evidence requests, and respond through the platform or by email. Their participation is a designed surface of the product, not an afterthought.
- **Executives, auditors, regulators** — consume program-level reporting: portfolio risk views, audit trails of decisions, evidence of due diligence.

The work context is a standing program, not a one-off project: vendors enter and leave continuously, evaluations refresh on a cadence, and findings accumulate. Regulated industries (financial services, healthcare) run the most formalized deployments, but the Type is industry-neutral.

## Core Model

### The Defining Core

Three structures, held jointly. Remove any one and the product stops being this Type.

**1. The third-party population under cyber assessment**

A persistent, identified record for each external vendor or service provider, held as the standing population the program runs on. Each vendor record carries **relationship context** alongside its security data:

- business criticality / impact (how badly a vendor disruption would hurt the organization)
- data shared with the vendor (personal, health, financial, sensitive categories)
- internal owner and business unit
- lifecycle stage (newly added → being assessed → responding → monitored)
- commonly: contract dates, tags, portfolios, custom fields

Without the standing population, the product is a ratings feed or a one-off assessment service with no program memory.

**2. Per-vendor security evaluation producing a comparable standing**

Each vendor carries a security evaluation assembled from evidence about that vendor's posture, assessed against the vendor's business context. Evidence flows through two channels:

- **externally observed signals** — the platform (or its rating engine) scans and rates the vendor's internet-facing footprint from outside: exposed services, weak encryption, known vulnerabilities, breach history
- **vendor-attested evidence** — what the vendor declares and supplies: security questionnaires, certifications, policy documents, audit reports

The evaluation yields a **per-vendor security standing** — a rating, grade, or risk level that makes vendors comparable to each other and trackable over time. Mature products commonly merge both channels with the vendor's inherent-risk profile (what the vendor does, what data it holds) into one composite standing.

Without the evaluation, the product is a vendor inventory; without the standing population, it is a raw signal feed.

**3. The decision-and-resolution loop over vendor cyber risk**

Evaluation results resolve into recorded decisions and tracked actions:

- **remediate** — a remediation request or plan is sent to the vendor, with prioritized steps, deadlines, and progress tracking
- **compensate** — the organization records compensating controls instead of vendor fixes
- **accept / waive** — the organization records a risk-acceptance or exception decision, with reason and approver

Each finding or risk carries its state — open, in remediation, resolved, accepted — with owners, due dates, messages, and evidence attached, and the trail is retained for audit. The vendor is the dominant counterpart in this loop: they receive the requests, respond, upload evidence, and commit to remediation dates. Without the loop, the product is an assessment report or a monitoring feed nobody acts on.

### One Structure, Many Implementations

The core model is conceptual; products realize each piece differently:

```text
Concept:  Evidence about the vendor's security posture
Realized as:  external attack-surface scanning and ratings  /  security
              questionnaires  /  document and certification review  /
              a merge of several channels into one composite rating

Concept:  Comparable per-vendor standing
Realized as:  standardized platform-scale grades  /  customer-relative
              risk levels  /  composite scores blending posture,
              questionnaires, and business impact

Concept:  Vendor participation in the resolution loop
Realized as:  vendor portal accounts  /  email invitations with free
              accounts  /  plan tasks inside the platform  /
              connection-based collaboration
```

A reader who has only seen one implementation — say, a ratings-led product — should still recognize a questionnaire-led product as the same Type from the core model.

## How It Works

### Bring a vendor into the program

```text
A vendor enters the population by:
→ manual add (by domain or name), singly or in bulk
→ automatic discovery (the platform detects vendors actually in use)
→ an internal intake form (business partners nominate a vendor; answers
  populate the vendor record and compute an inherent-risk tier)
→ import from another system
```

On entry the vendor gets its relationship context (impact, data shared, owner) and an initial tier that determines how deeply it will be assessed.

### Evaluate the vendor

```text
Tier determines depth and frequency
→ external signals are collected (scanning/ratings run continuously or on schedule)
→ questionnaires are sent to the vendor (template chosen by tier)
→ documents and certifications are collected and reviewed
→ results merge into the vendor's security standing
```

Evaluation is refreshed over time — continuously for externally observed signals, periodically for vendor-attested evidence (re-assessment cycles are a standard program stage).

### Resolve what the evaluation finds

```text
Findings/risks surface with severity and context
→ decide: require vendor remediation / apply compensating controls / accept
→ if remediating: send the vendor a request or plan with steps and deadlines
→ vendor responds: commits to dates, uploads evidence, messages the buyer
→ progress is tracked; re-testing or re-scanning verifies claimed fixes
→ the finding closes with a recorded decision and retained evidence
```

This loop is the platform's reason to exist: identifying vendor risk is half the job; driving it to a documented, defensible resolution is the other half.

### Run the program

Above individual vendors, the program layer aggregates: portfolio views of risk across the vendor base, tier-based work prioritization, alerts when a vendor's posture changes or a breach touches a vendor, and reporting for executives and auditors — including the audit trail of every acceptance and remediation decision.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Vendor list / portfolio view

The program's primary surface.

- lists the vendor population with security standing, criticality, monitoring status, and lifecycle stage
- primary actions: add vendors, filter and search, open a vendor, organize into portfolios/folders, bulk edit

### Vendor detail / profile

Everything known about one vendor relationship.

- relationship context (impact, data shared, owner, contract dates), security standing with factor breakdown, findings, questionnaires and their responses, documents, contacts, notes, history of requests
- primary actions: edit relationship details, send a questionnaire, create or send a remediation request, record a decision, add contacts and notes

### Findings / remediation workspace

Where the resolution loop lives.

- findings with severity, source, status (open / in remediation / resolved / accepted), owner, due date, and message thread
- primary actions: set review status, assign remediation with deadline, message the vendor, attach evidence, accept or waive with reason

### Assessment / questionnaire surface

The vendor-attestation channel.

- template libraries organized by framework, questionnaire builder, send-and-track state, response review with per-question evidence
- primary actions: build or choose a template, send to a vendor, review and score responses, convert answers into findings

### Monitoring / alerts

The externally observed channel.

- portfolio-level risk views, posture-change alerts, breach intelligence mapped to affected vendors
- primary actions: review alerts, triage by severity, convert alerts into findings or tickets

### Program reporting

- portfolio risk summaries, tier compliance, remediation progress over time, executive and audit-ready reports

### Vendor-facing surface

What the assessed party sees: assigned questionnaires, remediation plans with tasks and deadlines, evidence upload, message threads with the buyer. Implementation varies (portal account, emailed link, in-platform tasks) but the surface exists in mature products.

## Important Rules / Behaviors

### The vendor is a counterpart, not just a data source

The resolution loop is designed around vendor participation: vendors receive requests, respond with dates and evidence, and their responses become part of the record. Non-response is itself a managed condition (reminders, escalation, and the buyer's own re-verification by scanning rather than waiting).

### Decisions are recorded, not just made

Every resolution path — remediated, compensating controls, accepted, waived — is recorded with reason, owner, and evidence against the original finding. This audit trail is what makes the program defensible to auditors and regulators, and it is a structural behavior of the Type, not an optional nicety.

### Tiering gates the program's effort

Vendors are tiered by criticality and inherent risk; the tier drives assessment depth, questionnaire choice, and monitoring frequency. A low-risk vendor may get a light questionnaire and periodic review; a critical one gets continuous monitoring and full assessment. The specific scales vary by product; the gating behavior is standard.

### Evaluation standing is refreshed, not one-shot

The per-vendor standing is a living measurement: externally observed signals update on the platform's cadence, and vendor-attested evidence is refreshed through re-assessment cycles. A stale evaluation is a program failure the product is designed to prevent.

### Relationship context shapes risk interpretation

The same technical finding means different things for a vendor holding production personal data versus one with no data access. Business impact and data-shared context are first-class fields on the vendor record precisely because the evaluation is assessed against them.

### Monitoring status can be partial

Products commonly distinguish vendors under full evaluation from those only partially tracked (e.g., discovered but not yet formally onboarded). Upgrading a vendor to full monitoring is an explicit program action.

## Variants

- **Ratings-led** — the platform's own external rating engine is the primary evidence channel; questionnaires and vendor collaboration are modules around it. Typical of the large enterprise ratings vendors' TPRM offerings.
- **Questionnaire-led** — vendor-attested evidence is the primary channel; external scanning is absent or light. Typical of assessment-first vendor risk products and of programs in jurisdictions or industries where attestation and certification review dominate.
- **Merged composite** — external signals, questionnaires, inherent-risk profile, and the customer's own risk policies are fused into a single per-vendor rating. A common current-market shape.
- **Program-suite embedding** — the cyber-lens capability sold as one module of a broader third-party risk or GRC suite (multi-domain relationship programs). The cyber center remains, but the surrounding program is wider.
- **Regulatory-regime variants** — deployments shaped by financial-services regimes (operational-resilience and third-party oversight rules) with deeper compliance mapping and reporting.
- **Managed-service variants** — the vendor (or its partners) operates parts of the program on the customer's behalf, with the platform as the system of record.
- **Scale variants** — self-serve tiers for smaller security teams through enterprise suites with portfolio-scale deployments.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Security Ratings Platform | sibling, adjacent | the rating artifact and its computation for any organization (own posture, third parties, insurance, national programs); no vendor-relationship lifecycle or resolution loop. Ratings are one evidence input here |
| Third-party Risk Management | sibling, adjacent | the multi-domain third-party relationship program — financial, legal, compliance, ESG, operational, with cyber as one domain among several; center is the relationship and its program, not the vendor's security posture. Cyber-led deployments belong to this Type |
| Supplier Risk Management | adjacent | procurement-side risk over the supplier base and supply market — supply continuity is the operating frame, not the security program |
| Security Compliance Platform | adjacent | the organization's framework-compliance program; vendor security appears as one evidence object inside it, not as the per-vendor center |
| Attack Surface Management | adjacent | the organization's own external attack surface as the analyzed subject; here third parties' surfaces are an evidence channel |
| Vendor Management / procurement tools | adjacent | vendor master data, contracts, SLAs, sourcing; here those appear only as relationship context around the cyber evaluation |
| Cyber Risk Quantification | adjacent | computes financial exposure from cyber risk; this Type manages the vendor population and its resolution loop |

The most important boundary is with **Security Ratings Platform** and **Third-party Risk Management**, because vendors themselves bundle all three. The structural seams: the ratings platform owns the rating artifact without a vendor program; the TPRM program owns the multi-domain relationship; this Type owns the vendor's security posture as a managed, resolved object.

## Representative Products

- SecurityScorecard
- BitSight
- Panorays
- UpGuard

The core model was checked against a multi-domain TPRM product (Prevalent) to avoid absorbing the broader third-party relationship program into this Type's definition.

## Sources

Research date: **2026-09-09**

- SecurityScorecard — Help Center: Third-party risk and Vendor management categories; "What is third party monitoring?", "Manage your vendors using All Companies", "Use Action Plans to collaborate with your vendors", "About the vendor intake workflow" — https://support.securityscorecard.com/
- BitSight — Knowledge Base: Continuous Monitoring and Bitsight VRM categories; "VRM App: Vendors", "Vendor Profile: Findings", "Vendor Profile: Tiering", "Life Cycle Stages" — https://help.bitsight.com/
- Panorays — "How It Works", "Remediation Plans for Third-Party Vulnerabilities", platform pages — https://panorays.com/
- UpGuard — Vendor Risk product pages incl. "Remediation & Exceptions" — https://www.upguard.com/
- Prevalent (boundary probe) — product page — https://www.prevalent.net/

> Sourcing limitation: UpGuard and Panorays evidence was drawn from official product pages rather than deep help-center articles; operational claims in this document are kept at the strength those pages support. Precise vendor mechanics (rating scales, scoring algorithms, plan-generation internals) are intentionally not stated; they remain in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis against sibling Types are recorded in the paired Research Notes.
