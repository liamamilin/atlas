# Utilization Management

## Overview

A **Utilization Management** application is the health plan's — or its delegated utilization-management organization's — standing clinical review program: the software through which care proposed or delivered under the plan's coverage is reviewed against medical-necessity and coverage criteria, and each review resolves into a recorded determination.

It exists because a health plan does not simply pay for every service a provider orders. The plan operates a permanent clinical review operation that asks, service by service, whether the care is medically necessary and appropriate under the plan's rules — before the care is delivered (the prior-authorization face), while an admission or episode is in progress, and after the fact. The application is the system of work for that operation: it holds the program's configuration, the inventory of cases under review, the criteria the reviewers apply, the determinations they record, and the compliance machinery that keeps the program within its regulatory turnaround obligations.

The defining core is deliberately narrow. Everything else commonly seen around it — provider portals, fax automation, AI recommendations, criteria-content integrations, delegation routing, claims reconciliation — is mature add-on structure. When the center of gravity shifts to the multi-party request document and its durable authorization of record, the product is a Prior Authorization Platform; when it shifts to the plan's enrolled-population care programs, it is Payer Care Management; when it shifts to paying claims, it is claims processing.

## Users & Context

Primary users — the plan's (or delegated entity's) clinical review staff:

- **Utilization management nurse reviewers** — perform the first-level clinical review of each case: read the submitted clinical documentation, apply the plan's criteria, and record a determination or escalate.
- **Physician reviewers / medical directors** — take the cases that do not meet criteria, conduct physician-level review (including peer-to-peer conversations with the requesting provider), and make or uphold the final clinical determination.
- **UM program and operations managers** — configure the program (which services, which review modes, which criteria, which turnaround rules per line of business), balance case inventory across reviewers, and monitor throughput.

Secondary users:

- **Delegated UM organizations** — vendor clinical teams that operate some or all of the program on the plan's behalf, working in the same machinery under the plan's oversight.
- **Providers** — as counterparties rather than operators: submitting requests and clinical documentation, tracking status, responding to information requests, and scheduling peer-to-peer reviews through the plan's provider-facing surfaces.

The working context is a regulated payer clinical-operations department. Review volume is high, deadlines are externally imposed, every determination is potentially audited, and the same case may move between nurse, physician, and delegated reviewer. The discipline predates software: it was run for decades with paper criteria manuals, faxed admission notifications, and committee-documented determinations, and those operations satisfy the same core without any modern machinery.

## Core Model

### The defining core

The application rests on three structures that only work jointly:

```text
Review program of record
  (standing configured operation: service scope, review modes,
   criteria sources, reviewer staffing, lines of business)
└── Criteria-based clinical review, case by case
    (nurse-first review against the plan's criteria →
     recorded, reasoned determination →
     physician escalation when criteria are not met)
└── Coverage across the care timeline
    (prospective · concurrent · retrospective modes
     over one program machinery)
```

- **The review program of record.** The plan's utilization-management program is a standing configured operation, not a pile of one-off approvals: which service types are subject to review, under which review modes, against which criteria, executed by which reviewer staffing structure, across the plan's lines of business (commercial, government programs, behavioral health, pharmacy under the medical benefit). Service types, workflows, and categories are configurable — the program is the plan's own policy made operational. Remove the program structure and only scattered request processing remains — the machinery of a prior-authorization gate with no review operation behind it.

- **Criteria-based clinical review to a recorded determination.** Each case — a specific member's specific care — is evaluated against medical-necessity and coverage criteria: the plan's medical policy and the criteria content it references, increasingly held in the system as executable logic. Routine cases that clearly meet criteria can be resolved automatically by rules; the rest receive clinical review. The determination is recorded with its reasoning — meets-criteria/approve, not-met/deny, partial approval, or pending more information — and a case that does not meet criteria escalates to physician-level review before it becomes a denial. The content of the work is the application of clinical criteria to an individual patient's circumstances; remove that and what remains is administrative approval routing. A related invariant follows from this: decision support may recommend, but the determination act — especially any adverse determination — remains with the plan's reviewers, with visible override paths.

- **Coverage across the care timeline.** One program machinery operates in several review modes: **prospective** review before service is delivered (the prior-authorization face of the program), **concurrent** review of care already in progress — active inpatient stays reviewed for continued stay and appropriate level of care — and **retrospective** review of care after delivery. This span is what makes the operation a program rather than a pre-service gate: remove the concurrent and retrospective modes and what remains is prior-authorization request machinery, a different application type.

All three are load-bearing together. A program without clinical determinations is a schedule; determinations without a program are one-off reviews; a program and determinations confined to pre-service requests are prior authorization, not utilization management.

### The review case

The unit of work is the **review case**: a persistent, individually identified record binding a member to the care under review, the clinical documentation assembled for the review, the reviewer(s) who handled it, and its status as it advances through intake, review, escalation, determination, and closure. Cases accumulate into the program's working inventory — what reviewers work from, what operations managers balance, what compliance machinery measures, and what auditors later examine. In concurrent review, the case commonly stays open across the life of the stay, with repeat determinations as the episode progresses.

### Criteria: one structure, several substrates

The criteria layer is conceptually one thing — the rules the review applies — and several implementations:

```text
Concept:        the criteria a determination is made against
Implementations: the plan's own medical policy documents
                 referenced third-party criteria sets and medical-review services
                 public program coverage rules
                 client-defined business rules
                 digitized policy — criteria rendered into executable,
                 explainable decision logic
```

Mature products keep the criteria visible inside the review workflow — side by side with the clinical evidence — so the reviewer applies the rule and records why, rather than switching to separate applications. Policy digitization (parsing written policy into decision trees that both machines and reviewers can follow) is an increasingly common implementation of the same structure.

### Standard capabilities

Around the defining core, mature products commonly add:

- multi-channel intake — provider portals, fax automation that extracts and structures incoming requests, electronic transactions and standard APIs, EHR-embedded submission — with clinical documentation assembly (attachments, evidence extraction, chart summaries)
- auto-approval logic and decision support — rules engines and AI recommendation engines that resolve routine meets-criteria cases in near real time, surface evidence for human reviewers, and capture outcomes to improve future recommendations, with human exception handling preserved
- reviewer work queues, intelligent routing, case prioritization, and inventory management
- provider self-service — submission, status tracking, real-time updates, document upload, appeals submission, peer-to-peer scheduling
- delegation support — routing work to or from delegated review vendors, supporting insourced, outsourced, and hybrid operating models
- compliance machinery — turnaround-time monitoring and alerts per line of business and contract, deadline-driven case prioritization, audit trails, and regulatory reporting
- appeals and grievances linkage — a denied determination can be contested and re-reviewed through a recorded workflow
- authorization-vs-claims reconciliation — in some products, matching what was authorized against what was claimed
- operational dashboards — case volumes, inventory, handle times, throughput, turnaround performance

None of these individually defines the type; a program run on paper had intake, review, determination, and compliance without any of them.

## How It Works

### Configure the program

UM leadership defines, per line of business: which services require review, which review modes apply, which criteria and policy documents govern, the reviewer staffing model, and the turnaround rules the program must meet. This configuration is the program of record; everything below operates against it.

### Intake and case assembly

A care decision triggers a case: a provider submits a request (portal, fax, electronic transaction, or from the EHR), or an admission notification opens a concurrent-review case. The system checks eligibility and benefits, determines what clinical documentation the criteria require, and assembles the case — requesting records where needed, extracting and highlighting the clinically relevant evidence from what arrives. Cases that lack required information are pended back to the provider.

### Determine

Each case resolves through the program's determination machinery:

```text
Case assembled
→ meets criteria clearly?
   → yes: automatic/rules-based approval (routine cases), or fast-track reviewer sign-off
   → no or unclear: nurse-level clinical review against criteria
       → criteria met: approve (with scope/duration where applicable)
       → criteria not met: physician review — peer-to-peer with the
         requesting provider, then final determination
→ determination recorded with reasoning
→ provider and affected parties notified
```

Auto-approval handles the routine; clinical review handles the rest; physician escalation guards the adverse end. Every step attaches to the case, and the determination — including what was approved, for what scope, and why — is recorded and consumable downstream.

### Review care in progress

Concurrent review runs against active admissions: admission notifications — in some products fed directly from hospital admission/discharge/transfer data — open or update cases, reviewers assess whether the ongoing stay continues to meet criteria for its level of care, and repeat determinations follow the episode — including toward discharge and care-transition decisions. This is the mode with no counterpart in pre-service request machinery.

### Review after the fact and reconcile

Retrospective review evaluates care already delivered — post-service requests and reviewed claims-adjacent cases — under the same criteria machinery. Separately, where the platform provides it, the program's outputs are reconciled with payment: what was authorized is matched against what was claimed, so review decisions and claim outcomes stay accountable to each other, and denied or narrowed authorizations surface early in the payment pipeline.

### Run the operation

Underneath every case, the program runs as an operation: turnaround clocks tick per line of business and contract, cases are prioritized against deadlines, queues are balanced across reviewers, dashboards expose inventory and throughput, and audit and regulatory reports are produced from the recorded determinations. Delegated vendors work inside the same machinery, with the plan monitoring performance and compliance through the same surfaces.

## Interfaces

The following surfaces are described in conceptual terms; names and layouts vary by product.

### Reviewer worklist / case queue

The reviewer's entry surface. Purpose: present the cases awaiting action, prioritized by deadline, urgency, and mode. Typical information: member and care context, review mode, deadline state, assigned reviewer. Primary actions: open a case, claim or reassign, prioritize, escalate.

### Case review workspace

Where the review actually happens. Purpose: let a reviewer apply criteria to an individual case and record the outcome. Typical information: the submitted clinical documentation with extracted and highlighted evidence, the applicable criteria and policy side by side, decision-support recommendations with their reasoning, the case's history. Primary actions: approve/deny/partial/pend, request more information, escalate to physician review, record rationale, schedule peer-to-peer.

### Provider portal

The counterparty surface. Purpose: let providers submit and manage requests without calls and faxes. Typical information: request status, required documentation, determination results, authorization details. Primary actions: submit a request, upload records, track status, respond to information requests, submit an appeal, schedule a peer-to-peer review.

### Program administration

The configuration surface. Purpose: hold the program of record. Typical information: service types under review, review modes, criteria and policy assignments, workflow and routing rules, turnaround rules per line of business, reviewer roles. Primary actions: configure scope and rules, manage criteria versions, define workflows.

### Operations dashboard

The management surface. Purpose: run the program as an operation. Typical information: case volumes and inventory, turnaround performance against deadlines, throughput and handle times, staffing load, compliance alerts. Primary actions: rebalance queues, intervene on at-risk cases, produce compliance and audit reports.

### Delegated-vendor views

Where work is delegated: surfaces for routing cases to delegated review vendors — in either direction — so that insourced, outsourced, and hybrid operating models run inside the same program machinery, with the delegated work remaining visible to the plan's compliance and reporting surfaces.

## Important Rules / Behaviors

- **Determinations are recorded, reasoned, and auditable.** The determination — including denial reasoning — attaches to the case and survives into appeals and audits. The audit trail is not an add-on; it is the program's institutional memory.
- **Decision support recommends; the plan decides.** Automated logic may resolve routine meets-criteria cases, but recommendation engines expose their reasoning, are overridable, and do not make final adverse determinations. Complex and not-met cases move to human clinical review.
- **Criteria discipline with physician escalation.** Reviewers apply the criteria as written; when criteria are not met, the case escalates to physician-level review — including dialogue with the requesting provider — before an adverse determination stands.
- **Turnaround compliance is a first-class constraint.** Deadlines are externally imposed and vary by line of business and contract; the system tracks them per case, prioritizes against them, and reports on them. Missing them is a compliance event, not merely a service problem.
- **Concurrent review is bound to the live episode.** Cases track the stay as it progresses, with repeat determinations; the review window closes with the episode, and its findings feed discharge and transition decisions.
- **Outcomes flow downstream.** An authorization determination is consumed by claims adjudication as an input; reconciliation machinery keeps authorizations and claims mutually accountable. Appeals re-open determinations through their own recorded workflow rather than silently overwriting them.
- **Delegation distributes the work, not the oversight.** When review is delegated to vendor organizations, the plan commonly retains visibility through the same compliance and reporting machinery; routing work to a delegated vendor does not remove the program's obligation to run to its rules.

## Variants

- **Dedicated UM suite** — a standalone product whose whole subject is the review program (workflow depth, compliance machinery, criteria integration at the center).
- **Module of a payer platform family** — UM as one named solution beside care management, pharmacy, and appeals within a payer platform; the deepest packaging commonly unifies them on one member record.
- **Delegated UM with platform** — a vendor that both operates specialty review (imaging, musculoskeletal, cardiovascular, and similar programs) on the plan's behalf and supplies the software the plan's in-house teams use.
- **Decision-support / intake layer** — a UM-branded product that digitizes intake and recommends determinations, integrating to the plan's UM platform rather than replacing it; the market explicitly models these as separate layers.
- **Care-suite use-case solution** — UM as one use-case solution within a broader payer clinical-suite family.
- **Operating-model variants** — in-house, delegated, hybrid, and API-embedded deployments of the same program.
- **Scope emphasis** — prior-authorization-centric suites versus full-timeline programs; medical versus behavioral health; specialty program lines; pharmacy under the medical benefit.
- **Regulatory depth** — in the United States, standardized electronic transactions, FHIR-based prior-authorization APIs, and mandated turnaround rules shape the machinery; the defining core holds without any of it (paper-era and regional programs satisfy the same structures), and other regulatory regimes remain a variant axis rather than part of the definition.

One adjacent product family deserves explicit mention: the **provider-side utilization review** operation. Hospitals run their own utilization-management software — reviewing their active admissions against level-of-care and medical-necessity criteria, making inpatient-versus-observation status decisions, and documenting necessity to withstand payer review and audit. It shares the discipline, the criteria-based review machinery, and the nurse-plus-physician staffing model, but it is the mirror seat: the provider defending the status of its own care rather than the plan deciding coverage. It is treated here as a related operation, not the center of this type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Prior Authorization Platform | the multi-party request machinery: request as unit of record, intake → determination → durable authorization of record → status, whichever side hosts it; UM is the standing review program of which prospective review is one mode; packaging overlaps heavily in both directions, and the concurrent-review machinery belongs to UM |
| Payer Care Management | the plan's care-program portfolio and care loop (identify, enroll, assess, plan, intervene) over its member population; UM appears in the market as a sibling suite/module beside it, performing review determinations rather than care interventions |
| Health Plan Administration System | the payer's system of record — member, eligibility, benefit rulebook (including which services require authorization); UM operates the review program against that rulebook and holds no enrollment, premium, or claims record of its own |
| Payer Claims Processing | claims-operations machinery: intake → adjudication → settlement on the claim; an authorization determination is an input claims adjudication consumes, and reconciliation keeps the two accountable |
| Healthcare Revenue Cycle Management / Provider Claims Management | provider-side billing and claim management; the provider-side utilization-review operation (status and medical-necessity review of the provider's own admissions) sits beside it as clinical-integrity machinery, distinct from billing itself |
| Healthcare Quality Management | measures, gaps, and quality programs; UM's subject is necessity and appropriateness of care against coverage criteria, not quality measurement |
| Referral Management | routing and tracking of care relationships; a referral may be one reviewed service type inside a UM program, but referral management does not run the criteria-based determination program |
| Population Health Management | population-level analytics and segmentation; UM works case by case on care under the plan's coverage |

The boundary with the Prior Authorization Platform is the most consequential, because the market packages prior authorization inside UM offerings and vice versa. The stable distinction is between the request and the program: the prior-authorization platform is the machinery through which an advance-approval request is submitted, decided, recorded, and tracked by both parties; utilization management is the standing clinical review operation — criteria program, reviewer staffing, care-timeline coverage, compliance and delegation machinery — that the request machinery feeds into and draws upon.

## Representative Products

- MHK — CareProminence Utilization Management Suite
- ZeOmega — Jiva Utilization Management / Smart UM Suite
- Cohere Health — Utilization Management suite
- Availity — Intelligent Utilization Management
- Medecision — Utilization Management

The defining core was checked against a provider-seat utilization-review product (a hospital-side UR suite), older paper-era utilization-review practice, and delegated-UM operating models to avoid over-fitting the definition to the current US payer-suite implementation. One packaging pattern recurs and is deliberate: several products named "utilization management" are prior-authorization-centric layers or suites; the boundary section above explains why the request machinery and the review program remain distinct types.

## Sources

Research date: **2026-09-09**

Primary vendor surfaces (official product pages):

- MHK — CareProminence Utilization Management Suite: https://mhk.com/solutions/mhk-careprominence/utilization-management-suite/
- ZeOmega — Healthcare Utilization Management: https://www.zeomega.com/solutions/healthcare-utilization-management and Smart UM Suite: https://www.zeomega.com/solutions/smart-um-suite
- Cohere Health — homepage and Utilization Management suite: https://coherehealth.com/ , https://coherehealth.com/utilization-management-suite/
- Availity — Intelligent Utilization Management: https://www.availity.com/intelligentum/
- Medecision — Utilization Management: https://www.medecision.com/solutions/utilization-management/
- Waystar — Utilization Management (provider-seat boundary sample): https://www.waystar.com/our-platform/clinical-integrity-revenue-capture/utilization-management/

Context from the project's own sibling research: Prior Authorization Platform, Payer Care Management, and Health Plan Administration System passes (including official X12 transaction-set documentation fetched in the prior-authorization pass, which names "utilization management" entities among the expected users of health-care services review transactions).

> Sourcing limitations: legacy enterprise payer platforms and the major criteria-set vendors were not directly documented (their role is evidenced through integrations referenced by the sampled products); no non-US utilization-management product was sampled, so the definition deliberately names no country-specific machinery; vendor performance figures on the fetched pages are marketing claims and are not reproduced here. Detailed observations, the cross-product comparison matrix, and boundary evidence are recorded in the paired Research Notes.
