# Social Services Case Management

## Overview

A **Social Services Case Management** application is a government social-services agency's casework system of record: it holds identified records for the people and households the agency serves, opens a case for each person under a public social-service program, gates that case on the agency's recorded determination of the person's eligibility or need against the program's public rules, and carries the case through assessment, planning, service delivery, and review to a recorded closure — with the whole casework record documented and reported upward for public accountability.

The defining structure is small:

```text
Served person / household of record
└── Public-program casework episode
    (gated by an eligibility/need determination against public program rules,
     carried by an accountable caseworker)
    └── Documented casework record
        └── Public accountability (oversight reporting, compliance, audit)
```

Everything else commonly associated with these systems — configurable assessments, service plans, billing and personal budgets, client portals, mobile field work, AI documentation — is widespread in current products but is not what makes the system this Type. The same casework spine also exists in mission-driven private organizations; what separates this Type is the **public operator and public mandate**: the case exists under a government program whose rules determine who may be served, and the record answers to public oversight rather than to private funders.

## Users & Context

The primary users are caseworkers and social workers employed by public social-services agencies — city, county, and state human-services departments, local-authority adult social care teams, and municipal social-services offices. Their daily work is people-and-paperwork: meet or contact a person, gather and verify information, assess need, decide what the program can provide, arrange and track services, and document everything so the decision can be defended later.

Secondary users shape the system around them:

- **supervisors and managers** — oversee caseloads, distribute work, review decisions and deadlines
- **eligibility and finance staff** — run determinations, budgets, charges, and benefit-program linkages
- **program directors and agency leadership** — monitor performance, funding, and compliance
- **compliance and audit staff** — produce the reports oversight bodies require
- **administrators** — configure programs, forms, workflows, and permissions
- **clients (the people served)** — increasingly through portals: submit forms and documents, explore services, communicate with their caseworker

Partner agencies (health providers, contracted service providers, other authorities) participate through controlled contribution and referral channels rather than full access.

The work environment is a mix of office and field: caseworkers visit homes, meet people in community settings, and need access to the case record wherever the work happens.

## Core Model

### The Defining Core

```text
Served person / household of record
└── Public-program casework episode
    └── Documented casework record
        └── Public accountability
```

Four properties. If any one is removed, the system is no longer recognizable as this Type:

- **Served person / household of record** — every case is about an identified person, usually within a household or family context. The person record persists across programs and episodes, so the agency's history with a person is addressable. Without this, the system is a people registry or a CRM.
- **Public-program casework episode** — a case is opened for a person under a specific government social-service program, and it is **gated by a determination**: the agency records whether the person meets the program's eligibility or need rules before services flow. The case is assigned to an accountable caseworker and advances through a tracked lifecycle to a recorded closure. Without the public-program gate and government mandate, the same machinery is private/mission-driven casework (a different Type); without the episode container, it is an eligibility engine with no casework memory.
- **Documented casework record** — dated, attributed notes, assessments, determinations, plans, and service records accumulate on the case as the person's service history. The documentation is not an afterthought: it is the evidence that the agency's decisions were proper. Without it, the system is an empty case shell or a task tracker.
- **Public accountability** — the record exists to answer to oversight: funding-body reporting, compliance with program requirements, audits, and mandated response windows. Without this leg, the system is private casework documentation with no oversight loop.

### Standard Capabilities

A typical modern product carries most of these. They make the Type practical; they do not define it.

- **Intake and referral handling** — contacts, applications, and referrals captured from multiple channels, screened, and routed to the right team or worker.
- **Assessment machinery** — configurable forms and assessment instruments; many products provide assessment designers so agencies can encode their own program rules and practices.
- **Service / care planning** — a plan of services or support recorded on the case, with goals where the program calls for them.
- **Service delivery and authorization tracking** — what services were authorized, delivered, to whom, by which provider, with what result; utilization and outcomes tracked across programs.
- **Caseload and work management** — worktrays or work queues per worker and team, deadlines and due-date tracking, supervisor visibility into caseloads.
- **Referral and multi-agency machinery** — referrals to internal or external providers; controlled contribution by partner agencies to assessments and plans.
- **Money layer** — benefit-program linkage, billing or claims to funding programs, personal budgets, charges, and financial assessments. Depth varies strongly by regime and program.
- **Reporting and analytics** — standard and ad-hoc reports for funders, oversight bodies, and agency leadership; audit-ready output.
- **Security and confidentiality** — role-based access over sensitive personal data; program-scoped visibility.
- **Client self-service** — portals where clients submit forms and documents, explore services, and contact their caseworker.
- **Mobile and offline field work** — assessments and notes captured away from the office, with or without connectivity.

### One Structure, Many Implementations

The core model is conceptual. Products realize it differently:

```text
Concept:   Public-program gate
Realized as: eligibility determination at intake (economic-assistance style),
             needs assessment with eligibility rules (adult-social-care style),
             screening + assessment (protective-services style)

Concept:   Service authorization
Realized as: benefit decisions, purchased service arrangements, provider
             commissioning, personal budgets, vouchers, or direct service
             scheduling — depending on the program and regime

Concept:   Public accountability
Realized as: funder/program reporting, statutory returns, audit files,
             mandated response-window tracking
```

A reader who has only seen one implementation (say, a US county economic-assistance case file) should still be able to recognize a UK adult-social-care system or a state aging-services system from the core model.

## How It Works

### The casework loop

The defining workflow is a loop from first contact to recorded closure:

```text
Contact / application / referral
→ register or retrieve the person (and household)
→ open a case under a program
→ gather information; verify documents
→ assess need; determine eligibility against the program's rules
→ plan services (and authorize them)
→ deliver / arrange services; track delivery
→ review progress; reassess as circumstances change
→ close the case with a recorded outcome
```

Two features distinguish this loop from generic workflow:

- **The determination gate.** Services do not flow until the agency has recorded a determination — eligibility, need, or risk — against the program's public rules. The determination is itself part of the documented record.
- **Continuous documentation.** Every step (contact, verification, assessment, decision, delivery) is recorded on the case with author and date. The record is the case's defensible history.

### Caseload management

Around the loop runs a management layer: work is distributed to caseworkers as caseloads; deadlines and mandated response windows are tracked; supervisors monitor caseloads, due dates, and case statuses; overdue or stalled work is visible. The unit of management is the case, not the task.

### Multi-agency contribution

Where services depend on other organizations, the system supports controlled collaboration: sections of an assessment or plan can be delegated to partner professionals, who contribute without gaining access to the wider record; referrals move work to providers; provider responses return to the case.

### The money path

Depending on the program, the case carries a money dimension: benefit-program linkage and claims/billing to funding programs, personal budgets and charges (with financial assessments), or purchased-service arrangements with providers. The money layer attaches to the case and its services — it does not replace them.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Caseload / work queue

The worker's primary entry surface.

- lists the worker's (or team's) cases with status, deadlines, and pending actions
- primary actions: open a case, work an item, reassign, record progress

### Person / household record

The served person's persistent record.

- identity and demographics, household/family composition, program history across episodes
- primary actions: register a person, start a case, view history, update details

### Case record

The episode's workspace — the center of the system.

- the case's program context, status, assigned worker, and its accumulated documentation: notes, forms, assessments, determinations, plan, services, documents
- primary actions: record notes, complete forms/assessments, record a determination, build or update the plan, authorize or record services, upload documents, change status

### Assessment / form surfaces

Program-specific instruments rendered as guided forms.

- structured questions, validation, and program rules embedded in the flow
- primary actions: complete, submit for review, delegate sections to partner agencies

### Service plan / delivery view

What the program will provide and what was provided.

- planned services, authorizations, providers, delivery records, utilization, outcomes
- primary actions: plan a service, authorize, record delivery, review outcomes

### Supervisor / management views

Oversight surfaces for managers and leadership.

- caseload distribution, deadlines and overdue work, case statuses, program performance, funding and compliance reporting
- primary actions: assign and redistribute work, review decisions, generate reports

### Client portal (where offered)

The served person's own surface.

- forms and document submission, service exploration, communication with the caseworker

## Important Rules / Behaviors

### No services without a recorded determination

The gate is structural: the case's progression to service depends on a recorded eligibility/need determination against the program's rules. The determination is retained as part of the record.

### The record must be defensible

Documentation is the system's core behavior, not an administrative chore: dated, attributed entries accumulate on the case so that any decision can be traced and defended in audit or review. Products commonly enforce structured forms and validation for exactly this reason.

### Deadlines and mandated windows are first-class

Public programs carry response windows and processing deadlines. The system tracks them per case and surfaces overdue work to workers and supervisors.

### Access is role-based and program-scoped

Sensitive personal data is protected by role-based permissions; visibility is commonly scoped by program, team, and need. Partner-agency contribution is mediated (delegation, portals) rather than open.

### Cases close, people persist

A case ends in a recorded closure, but the person's record persists — later episodes can build on the agency's history with that person, and cross-program views reduce the need for clients to repeat their stories.

### Exact state vocabularies vary

Case-status labels, determination categories, and lifecycle stage names differ across products and regimes. The conceptual progression — intake → assessment → determination → plan → delivery → review → closure — is the stable structure; the labels are not.

## Variants

The Type is program-agnostic; its variants are mostly program areas and regimes:

- **economic assistance casework** — high-volume application/verification/eligibility work across benefit programs (cash assistance, food assistance, energy assistance, medical assistance), documentation- and deadline-heavy
- **aging and disability services** — intake, assessment, care planning, and service arrangement for home- and community-based services; often with provider networks and funding-program billing
- **adult protective services** — report-driven casework for vulnerable adults: screening, investigation, and protective service arrangements
- **adult social care (UK-style statutory regime)** — contacts, needs assessments, care and support planning, personal budgets, safeguarding, and commissioning under statutory obligations
- **vocational rehabilitation / employment services casework** — assessment, plan, and service delivery toward employment outcomes
- **housing and homelessness assistance casework** — assistance administration as casework (distinct from operating housing stock)
- **multi-program unified platforms** — one system carrying many program areas with shared person records and cross-program visibility; the dominant modern posture, but single-program implementations satisfy the Type equally

Operator realization is a gradient, not a wall: government-operated agencies are the center; government-commissioned providers administering public programs with public eligibility rules sit inside the Type; mission-driven organizations running their own programs sit outside it (Nonprofit Case Management).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Nonprofit Case Management | closest sibling (shared casework spine) | cases open under the organization's own defined programs with funder accountability, not under government programs gated by public eligibility rules; the same products often sell into both worlds — a context line, not a feature line |
| Child Welfare Management | statutory specialization | adds the child-protection loop: protected minor, mandated-report screening, safety assessment with legal force, placement and permanency machinery, need-to-know confidentiality; the generic Type requires none of these |
| Probation & Parole Management | sibling with legal authority | adds court/parole authority, ordered conditions, and sanction/revocation consequence machinery; supportive casework without those is this Type |
| Public Sector Case Management | generic parent (adjacent leaf) | generic government intake→route→work→close without the served-person/household model or program eligibility determination |
| Public Benefits Management | program-side neighbor | benefit-centric: eligibility rules, benefit calculation, issuance, and recertification at program scale; here the determination happens inside a person's casework episode and the case is the unit of record |
| Housing Assistance Management | program-area neighbor | assistance administration as casework sits here as a workflow variant; operating program-restricted housing stock is the other Type |
| Public Employment Service Platform | adjacent | labor-market intermediation (vacancy pool, jobseeker registration, placement); employment services delivered as public casework is a program-area variant of this Type |
| Immigration Case Management | adjacent | adjudication of immigration requests (decision made in the system); settlement/assistance casework for immigrants is a program-area variant here |
| Care Plan Management / Care Coordination (health) | adjacent | clinical/assessed-needs records without the public-program eligibility gate and public-accountability framing; behavioral-health and disability verticals straddle toward health EHR |
| Beneficiary Management | registry neighbor | centers the served population registry (registration, delivery, participation) without the accountable casework episode |

## Representative Products

- CaseWorthy (incl. ClientTrack, ServTracker, MediSked) — multi-program human-services platform serving nonprofits and local/state governments
- WellSky Human Services (Aging & Disability and related state-program solutions) — state agencies and community-based organizations
- Liquidlogic Adults Case Management (System C) — UK local-authority adult social care
- Northwoods Traverse — US county social-services casework across adult & aging and economic assistance program areas

The core model was checked across government tiers (state, county, local authority) and regimes (US federal/state programs, UK statutory adult social care) to avoid over-fitting to any single program area or country's machinery.

## Sources

Research date: **2026-09-09**

Primary vendor surfaces (official product pages):

- CaseWorthy — https://caseworthy.com/ , https://caseworthy.com/who-we-serve/government-and-public-sector/ , https://caseworthy.com/platform/caseworthy-platform/
- WellSky — https://wellsky.com/ , https://wellsky.com/human-services-software/ , https://wellsky.com/aging-disability/
- System C / Liquidlogic — https://www.systemc.com/ , https://www.systemc.com/local-government/adult-social-care/
- Northwoods — https://www.teamnorthwoods.com/traverse/traverse-program-areas/ , https://www.teamnorthwoods.com/traverse/traverse-program-areas/traverse-for-economic-assistance/

> Sourcing limitation: live fetch of vendor help-center / operational documentation was not possible from the research environment on 2026-09-09 (support centers exist but were not reachable at documentation depth; several additional vendors were unreachable and are recorded in the Research Notes). All structural claims rest on official product pages; precise operational details (case-state vocabularies, numeric limits, default settings, timing rules) are intentionally not stated in this document.

Detailed evidence, product-by-product observations, cross-product comparison, and the boundary/joint-review record are in the paired Research Notes.
