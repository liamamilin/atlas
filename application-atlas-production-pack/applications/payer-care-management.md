# Payer Care Management

## Overview

A **Payer Care Management** platform is the health plan's clinical-program operating layer: the software a health plan (payer) uses to run care-management programs over its member population — finding the members who need support, enrolling them into programs, assessing their needs, planning and coordinating their care, intervening, and documenting that work — with quality-measure and risk-adjustment machinery attached.

Its defining core is small:

```text
Member as care subject
└── Care program portfolio (identify → stratify → enroll)
    └── Documented care-management loop
        (assess → care plan → intervene & coordinate → document → track to resolution)
```

Everything else commonly associated with this software — risk-stratification analytics, quality-measure gap closure, risk-adjustment coding support, utilization-management workflow, member apps, provider portals, social-needs referral — is standard mature structure or variant machinery, not what makes the product a payer care management platform.

The boundary that defines the Type: a payer care management platform holds **no enrollment, premium, or claims record of its own**. It operates on top of the plan's administration record; the members it manages are the plan's already-enrolled population. When a product's center is that coverage-and-benefit record instead, it is a health plan administration system.

## Users & Context

The primary users are the health plan's own care teams and adjacent clinical staff:

- **care managers and case managers** — carry a panel of enrolled members, run assessments, build and maintain care plans, and work interventions to resolution; the teams commonly blend nursing, social-work, and behavioral-health professionals
- **disease-management and program coordinators** — work defined chronic-condition programs across large member groups
- **social workers and community-health staff** — address social needs, refer to community services, support long-term-services populations
- **quality and risk-adjustment teams** — work care-gap and coding-gap worklists derived from the same member picture
- **program administrators** — configure program criteria, pathways, assessments, and workflows

Secondary users: utilization-management nurses (when UM ships as a sibling module of the same platform), member-services staff reading the same member picture, and staff of delegated vendors who run programs on the plan's behalf.

External surfaces face two more groups: **members** (apps and portals through which programs reach and engage them) and **provider office staff** (portals and handoff channels for care coordination).

The operating context is health plans under value-based-care pressure: commercial plans managing at-risk populations, Medicare Advantage plans (including special-needs plans) working quality stars and risk scores, Medicaid managed-care plans under state-specific rules, and third-party administrators running the same machinery for employer groups.

## Core Model

### The Defining Core

```text
Member as care subject
└── Care program portfolio
    └── Documented care-management loop
```

Three structures. If any one is removed, the product is no longer recognizable as payer care management:

- **Member as care subject** — the plan's enrolled population held as identified members, each carrying an assembled care picture: conditions, risk level, utilization history, medications, quality gaps, and often social factors — built by combining claims, clinical, pharmacy, and assessment data from multiple sources. The member is held here as a *care subject*, not as a coverage record: the platform holds no enrollment, premium, or claims-adjudication record. Without this, the product is a member analytics dashboard.
- **Care program portfolio** — the plan's defined clinical programs (case management, disease or chronic-care management, utilization management, transitions of care, long-term services and support, behavioral health, maternity) held as configurable structures with identification and eligibility criteria. Members are matched to programs by stratification rules, referrals, or outreach responses. Without this, the product is an ad-hoc outreach tool.
- **Documented care-management loop** — per-member work executed by the plan's care teams: assessment → an individualized care plan with goals and interventions → outreach, intervention, and coordination with members, providers, and community resources → documentation of every step → tracking of progress to resolution, goal attainment, or graduation from the program. The documentation is compliance-grade and audit-ready. Without this, the product is a reporting layer with no operational loop.

The three structures are jointly load-bearing: a member picture without programs and the loop is analytics; programs without the member picture have nothing to act on; the loop without both is generic care coordination — the provider-side territory of a different Application Type.

### Standard Capabilities of Mature Products

Mature products commonly carry most of the following. They make payer care management practical; they do not define the Type.

- **Risk stratification & predictive identification** — analytics over the assembled member data that surface rising-risk and high-risk members and suggest "next best actions" for the care team
- **Care-gap worklists & quality-measure machinery** — gaps derived from quality-measure engines (HEDIS- and Stars-class in US government programs), worked to closure through member outreach and provider engagement
- **Risk-adjustment support** — identification of uncaptured or suspect diagnosis codes, chart-review workflows, and coding-gap outreach (government-program machinery)
- **Utilization-management workflow as a sibling module** — prior authorization and concurrent review commonly co-deployed on the same platform; UM activity also serves as an identification source for care programs
- **Member engagement surfaces** — member apps and portals, outreach campaigns, scheduled check-ins, secure messaging, and digital health-risk assessments that feed program enrollment
- **Provider-facing seam** — provider portals, clinical data exchange, and structured handoffs for transitions and care coordination
- **Social-needs (SDOH) machinery** — social-needs assessment and closed-loop referral to community services
- **Pharmacy machinery** — medication reconciliation, drug-utilization review, adherence work
- **Appeals & grievances linkage** — tracked alongside care activity where the regime requires it
- **Work-queue automation** — case assignment, bulk assignment, task generation, and workflow routing
- **Compliance & audit machinery** — documentation standards, regulatory timelines, audit-readiness monitoring
- **Reporting & dashboards** — program performance, quality scores, utilization and cost views

### One Structure, Many Implementations

The core model is written conceptually. Implementations vary:

```text
Concept:  Member care picture
Implementations:  claims + clinical + pharmacy data assembly, health-risk
                  assessments, program assessments, external data feeds

Concept:  Care program
Implementations:  named program modules (case management, disease management,
                  transitions, LTSS, behavioral), configurable pathways and
                  criteria, evidence-based protocol libraries

Concept:  Care plan
Implementations:  goal/intervention libraries with auto-recommendation,
                  configurable templates, free-form plans with goal tracking

Concept:  Intervention & coordination
Implementations:  task queues, outreach campaigns, scheduled check-ins,
                  secure messaging, provider handoffs, community referrals

Concept:  Quality & risk machinery
Implementations:  embedded measure engines and gap worklists, standalone
                  analytics products feeding the workflow platform
```

A reader who has only seen one implementation — for example a workflow platform with embedded HEDIS machinery — should still be able to recognize an analytics-first product that only assembles the member picture and hands worklists to the plan, or a government-program deployment with deep regulatory timelines, from the same core model.

## How It Works

### Identify and stratify

```text
Member data assembled (claims, clinical, pharmacy, prior assessments)
→ analytics score risk and predict need
→ members surface as candidates for programs
→ care teams review, prioritize, and act
```

Identification is continuous: new claims, new clinical data, and new utilization events re-stratify the population and can trigger program candidacy at any time.

### Enroll into a program

```text
Candidate member matched against program criteria
→ referral or outreach (campaign, call, digital health-risk assessment)
→ eligibility confirmed; consent obtained where required
→ member enrolled; a case opens under the program
```

Programs are the unit of organization: the same member can sit in several programs at once (for example, case management plus a quality-gap program).

### Assess, plan, and work the loop

```text
Assessment completed (clinical and social needs)
→ individualized care plan created (goals + interventions, commonly from
  evidence-based libraries with recommended defaults)
→ plan generates work: outreach, education, provider communication,
  transitions support, community referrals, medication follow-up
→ every contact and action documented against the case
→ progress tracked toward goals; plan updated as needs change
→ case closes at resolution, goal attainment, or graduation — with the
  full documented history retained
```

This loop is the operational heart of the Type. Care managers live in it daily; automation screens noise and surfaces next actions, but the documented human work is what the system exists to organize.

### Work the quality and risk loops (where the regime pays for it)

```text
Measure engine computes care gaps and coding gaps from member data
→ gap worklists assigned to care teams
→ closure pursued through member outreach (schedule the visit, complete
  the assessment) and provider engagement (records, chart review)
→ closure documented; measure performance tracked
```

In government-program deployments a parallel risk-adjustment loop pursues accurate risk scores through chart review and coding-gap outreach. These loops attach to the same member picture and reuse the same outreach machinery; their depth varies by market and regime.

### Core vs Common vs Optional

**Defining core** — without these, not payer care management:

- member as care subject (assembled multi-source care picture, no coverage record)
- care program portfolio (criteria-based identification and enrollment)
- documented care-management loop (assess → plan → intervene → document → track)

**Standard mature structure** — present in most current products:

- risk stratification & predictive identification
- care-gap worklists & quality-measure machinery
- risk-adjustment support
- UM workflow as sibling module
- member engagement surfaces
- provider-facing seam
- SDOH referral machinery
- pharmacy/medication machinery
- work-queue automation, compliance/audit machinery, reporting

**Variant / optional** — depends on segment, regime, and packaging:

- government-program depth (special-needs plans, long-term services and support, state-specific Medicaid rules)
- behavioral-health program depth
- delegated operation (a vendor runs the programs on the plan's behalf)
- member mobile apps with two-way messaging
- analytics-first vs workflow-first posture
- regional regimes outside the US-shaped sample

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Care manager workbench / member view

The care team's primary surface — one member's assembled world.

- care picture: conditions, risk level, utilization, medications, gaps, program participation, recent contacts
- primary actions: open a case, complete an assessment, update the care plan, document a contact, work a task

### Work queues

The team's daily work organizer.

- assigned cases and tasks by program, priority, and due state; bulk-assignment controls for supervisors
- primary actions: accept, work, reassign, escalate, document

### Care plan editor

Where the individualized plan lives.

- goals, interventions, target dates, progress notes; recommended content from evidence-based libraries
- primary actions: create/update plan, add goals and interventions, track progress

### Assessment forms

Structured intake of member needs.

- clinical and social assessment instruments, including digital health-risk assessments completed by members
- primary actions: conduct/score assessment, feed results into the care picture and program eligibility

### Quality-gap and risk-adjustment worklists

The measure-driven work surfaces.

- gap lists by measure and member; chart-review queues for coding gaps
- primary actions: pursue closure (outreach, provider engagement), document evidence, report performance

### Member app / portal

The member-facing face of the programs.

- program-related tasks, appointments, medication reminders, secure messaging, check-ins
- primary actions: respond to outreach, complete assessments, communicate with the care team

### Provider portal / handoff surfaces

- care-team requests, transition handoffs, clinical-data requests
- primary actions: respond, exchange documentation

### Program configuration

- program criteria, pathways, assessments, workflow rules, letter templates — maintained by plan staff
- primary actions: configure, version, deploy

### Dashboards & reports

- program performance, quality scores, utilization and cost views for plan leadership

## Important Rules / Behaviors

### Program criteria gate enrollment

Membership in a program is not arbitrary: members enter through defined identification and eligibility criteria (risk thresholds, condition registries, referrals, event triggers). The criteria are configuration, and enrollment against them is recorded.

### The care plan drives the work

Interventions and tasks are generated from the care plan; documentation attaches to the case the plan belongs to. A care action performed outside the plan-and-case structure is, from the system's perspective, invisible work.

### Documentation is compliance-grade

Every contact, assessment, and intervention is documented to audit standards. In government-program deployments, regulatory timelines and documentation requirements are first-class constraints the workflow enforces — missed timelines are visible operational failures.

### The member picture is assembled, not owned

The platform combines claims, clinical, pharmacy, and assessment data from external sources. It does not originate the coverage record or the claim; when source data is missing or stale, the care picture is visibly incomplete — a known operational risk of the Type.

### Gaps persist until closed

Quality and coding gaps remain on worklists until closed with evidence or aged out by the measure cycle. Closure is an event with documentation, not a checkbox.

### UM decisions are a separate discipline

Where utilization management is co-deployed, authorization status is consumed by care workflows, and in some products UM activity also serves as a source for program identification — but the review machinery (medical-necessity criteria, determinations, appeals) is its own discipline and commonly its own module or product.

### Engagement is an operational concern, not a guarantee

Programs reach out across risk tiers and track engagement; members may not participate. Outreach and engagement are actively managed, and non-response is a documented outcome that care teams work around.

## Variants

- **Standalone care-management suite** — an independent platform sold to plans as their care-operations system
- **Module inside a payer platform family** — care management as one suite beside utilization management, pharmacy, and appeals within a vendor's payer portfolio
- **Bundled inside a core administration system** — care-management capabilities shipped as modules of the plan's system of record
- **Delegated clinical services** — the vendor operates the programs with its own care staff on the plan's behalf
- **Government-program pole** — special-needs plans, long-term services and support / managed long-term care, and state-specific Medicaid machinery, with deep compliance timelines
- **Commercial pole** — employer-group populations, condition and lifestyle programs, utilization-focused outreach
- **Payvider deployment** — provider organizations running payer-style programs on their attributed populations using the same machinery
- **Analytics-first pole** — data products that assemble the member picture and produce gap/risk worklists, feeding a workflow platform (or the plan's own teams) rather than carrying the full loop
- **Behavioral-health and LTSS carve-outs** — program families with their own assessment and service-referral machinery
- **Regional regimes** — statutory-insurance chronic-disease programs realize the same structures with different machinery (lower-confidence variant, inferred)

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Health Plan Administration System | system of record vs clinical layer | administration holds the member/coverage/benefit/premium/claims record; payer care management runs clinical programs on top of that population and holds no enrollment/premium/claims record of its own |
| Utilization Management | sibling discipline | UM is the review machinery (prior authorization, concurrent review, medical necessity); payer care management is the broader program portfolio in which UM appears as one program type and a sibling module |
| Care Coordination Platform | same machinery, other owner | provider-side delivery of coordinated care vs payer-side oversight of members; products deploy on both sides |
| Chronic Care Management | program overlay, other owner | provider-side delivery of chronic-care programs (often under a billing regime) vs the plan's own member programs |
| Population Health Management | analytics layer | risk models, segmentation, and measure reporting vs the operational program loop; commonly bundled, separable in the market |
| Value-based Care Platform | contract layer | payer↔provider contract, payment, and quality-reporting machinery vs the plan's own member-facing care operations |
| Care Plan Management | artifact vs loop | care-plan management centers the plan artifact's lifecycle; here the care plan is one object inside the program loop |
| Patient Engagement Platform | capability vs center | engagement surfaces (campaigns, apps, check-ins) are capabilities of this Type, not its center |
| Referral Management | narrow slice | routing referrals between parties vs running programs that generate and work referrals |
| Provider Network Management | different object | contracting, credentialing, and network adequacy vs member-level care programs |

The boundary that matters most within healthcare is the **system of record vs clinical-program layer** seam: the administration system is what the plan knows (who is covered, under what rules, what has been paid); payer care management is what the plan's care teams do about the health of the people under that coverage.

## Representative Products

- **ZeOmega (Jiva platform)** — workflow-first payer care management platform; ranked Best in KLAS for Payer Care Management Solutions 2022–2025; commercial, Medicare Advantage, Medicaid, and ACO deployments
- **Medecision** — payer-and-provider care, utilization-management, quality, and risk platform on a unified data layer; care management, LTSS, and complex-care coordination category
- **MHK (CareProminence Care Management Suite)** — modular payer suite, care side; Medicare Advantage / special-needs-plan and long-term-services depth, unified with UM, pharmacy, and appeals suites
- **Inovalon (Payer Cloud)** — the analytics-first pole: quality-measurement, risk-score, and member-outreach data products; included as the boundary anchor for the data/analytics layer adjacent to this Type

Widely cited market participants whose documentation was not reachable during this research (Altruista Health, HealthEdge, Casenet, TriZetto) are recorded in the research notes without product-specific claims.

## Sources

Research date: **2026-09-08**

- ZeOmega — homepage and Care Management solution page: https://www.zeomega.com/ , https://www.zeomega.com/solutions/care-management-solution
- Medecision — homepage and Care Management solution page: https://www.medecision.com/ , https://www.medecision.com/solutions/care-management/
- MHK — CareProminence Care Management Suite and Utilization Management Suite: https://mhk.com/solutions/mhk-careprominence/care-management-suite/ , https://mhk.com/solutions/mhk-careprominence/utilization-management-suite/
- Inovalon — Payer Cloud navigation and provider-cloud care-management page (boundary anchor): https://www.inovalon.com/products/payer-cloud/care-management/

Boundary-consistency context: the paired research notes and processed documents for health-plan-administration-system, care-coordination-platform, and chronic-care-management (each of which recorded a boundary flag resolved in this pass).

> Sourcing limitation: several market participants' documentation could not be fetched during this research (Altruista Health and HealthEdge returned access errors; Casenet was unreachable). The canonical description therefore rests on the reachable sample above plus cross-pass context from the sibling healthcare leaves. Precision-dependent details — specific program eligibility thresholds, measure lists, turnaround-time rules, and any numeric limits — are intentionally not stated; where programs, gaps, and compliance are described, they are described conceptually.

Detailed evidence, product-by-product observations, cross-product comparison, and the historical / market-sample check are recorded in the paired Research Notes.
