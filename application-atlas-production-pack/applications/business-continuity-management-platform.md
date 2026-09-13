# Business Continuity Management Platform

## Overview

A **Business Continuity Management Platform** is an organization's system of record for its continuity program: it holds the organization's own business functions as an owned inventory, analyzes how long the organization can operate without each of them, and maintains the plans for recovering them when disruption strikes.

The problem it solves is structural, not informational. Continuity knowledge — which functions matter most, what each depends on, who recovers what and how — is normally scattered across spreadsheets, binders, and the heads of process owners, where it ages quickly and cannot be acted on during an incident. The platform turns that knowledge into connected, maintained records: a business function inventory, impact analyses that produce recovery objectives, and continuity plans bound to the functions they protect.

The defining core is deliberately small:

```text
Business function inventory (owned, criticality-bearing)
└── Impact analysis per function
    ├── impact of disruption over time
    ├── dependencies (people, facilities, technology, suppliers)
    └── recovery objectives (recovery-time / recovery-point class)
        └── Continuity plan of record
            └── recovery strategies + response/recovery procedures
                maintained, approvable, activatable
```

Everything else commonly associated with the category — dependency graphs, exercise management, risk registers, crisis-management modules, notification, compliance reporting — is standard capability that mature products add around this core. When the center of gravity shifts to coordinating a live response to an unfolding event, the product has moved into a different Application Type (Emergency Management, Crisis Management); when it shifts to executing technical recovery of IT systems, that is Disaster Recovery.

## Users & Context

Primary users:

- **BCM / resilience program manager** — owns the program: defines the methodology, launches impact-analysis campaigns, monitors plan currency and exercise coverage, reports readiness to leadership.
- **Business process / function owners** — the people who run the functions being analyzed. They answer impact-analysis questionnaires, own plans for their functions, keep recovery details current, and participate in exercises.
- **Executives and board stakeholders** — consume readiness reporting: which functions are covered, where gaps remain, what remediation is in progress.

Secondary users:

- **IT disaster recovery managers** — perform technical impact analysis for the applications and infrastructure that business functions depend on, and maintain IT DR plans as sibling plan types.
- **Crisis / incident response teams** — consume plans at the moment of activation during a disruption.
- **Auditors and regulators** — consume the program's evidence: impact analyses, approved plans, exercise records, corrective actions.

The work context is a standing organizational program, not a project: functions change, dependencies change, people change, so the inventory, analyses, and plans are continuously refreshed on review cycles. The platform is used intensively during program rollouts and refresh campaigns, periodically during exercises and reviews, and — at the moment that justifies the whole program — during a disruption, when responders need the current plan immediately.

## Core Model

### The Defining Core

**Business function / process (the continuity subject).** The unit the whole program hangs from: a business function or process the organization performs — payments processing, order fulfillment, patient admission, payroll — held as a persistent record with an owner and critical attributes. Products organize these in a business-process hierarchy or library. The inventory answers "what is it that must continue?" Without it, plans and analyses float free of anything real.

**Impact analysis (the business impact analysis, BIA).** A structured assessment attached to a function record. Its inputs are questionnaires answered by the function's owners (and, for technical elements, IT owners); its subject matter is threefold:

- *impact over time* — what happens to the organization (financially, operationally, reputationally, regulatorily) as the function stays down for longer;
- *dependencies* — what the function needs to operate: people, facilities, technology and applications, suppliers and third parties;
- *recovery objectives* — the time-based targets the analysis produces: how quickly the function must recover (recovery time objective) and, for its data, how much loss is tolerable (recovery point objective).

In mature products the BIA is a computed record, not a document: the platform calculates recovery objectives from questionnaire responses against admin-defined impact ratings, and the analysis carries a lifecycle of its own (draft → review → approved, with approved versions read-only). The BIA is what makes recovery prioritization a decision rather than a guess.

**Continuity plan of record.** The operational response attached to the analyzed function: recovery strategies (workarounds, alternate sites, alternate suppliers, manual procedures) and the concrete steps, roles, contacts, and resources needed to execute them. The plan is a maintained record — owned, versioned, reviewed on a cycle, approved through workflow — not a static document. Plans are written against the recovery objectives the BIA established, and they are what responders open when disruption occurs.

These three are jointly load-bearing:

- an inventory without analyses and plans is a process list nobody acts on;
- analyses without plans are surveys with no operational consequence;
- plans without the inventory and analyses are the shelf-ware binders the category exists to replace — documents with no recovery priorities behind them.

### Standard Capabilities Around the Core

Mature products commonly add:

- **Dependency mapping** — the function's dependencies held as first-class relationships (upstream and downstream across people, processes, places, systems, third parties), often visualized and increasingly auto-refreshed from asset/configuration data.
- **Risk assessment** — threats and vulnerabilities assessed against functions (a continuity risk register), feeding mitigation steps into plans.
- **Exercise management** — plans validated through walkthroughs, tabletops, and scenario simulations; scenarios defined by loss type (facility, people, technology, supplier); results recorded as findings and lessons learned.
- **Gaps and corrective actions** — shortfalls between recovery objectives and actual capability, and between exercise findings and plan reality, tracked to remediation.
- **Plan lifecycle machinery** — approval workflows, review scheduling, versioning, PDF/Word generation, electronic distribution, mobile access for responders.
- **Recovery strategy library** — reusable strategies associated with multiple plans.
- **Notification and call trees** — contact data, call-tree initiators and recipients, emergency notification integration.
- **Program governance** — dashboards and readiness reporting for program managers and executives; audit trails.
- **Compliance support** — alignment with continuity standards (ISO 22301 is the standard most often cited across the sampled products) and evidence production for regulators and auditors.
- **Incident/crisis integration** — escalation of incidents to crisis events, plan activation during events, recovery-task tracking while a plan is live.

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:  continuity subject
Realized as:  business process, business function, business service,
              product/service line — organized in a process hierarchy or library

Concept:  recovery objectives
Realized as:  calculated RTO/RPO from questionnaires, criticality tiers,
              impact tolerances (regulated-industry form)

Concept:  plan of record
Realized as:  structured plan records with approval workflow,
              template-driven plan documents, or live data-connected plans
```

A reader who has only seen one implementation — say, questionnaire-driven BIAs with computed RTO/RPO — should still recognize a template-driven mid-market product or a paper-era program as the same Type.

## How It Works

The program runs as a continuous loop. The typical flow:

### 1. Establish the inventory

The program team (often with executives) defines the business-process structure and registers the organization's functions with owners. Existing process libraries or org structures seed the inventory.

### 2. Analyze impact

```text
Select functions for analysis (often as a campaign across a division)
→ owners receive impact-analysis questionnaires
→ impact categories rated; dependencies identified
→ platform computes recovery objectives (RTO/RPO class)
→ analysis reviewed and approved
→ functions ranked by criticality
```

The output is a prioritized picture: which functions are most critical, how long each can be down, what each depends on, and where the recovery objectives are most demanding.

### 3. Define strategies and build plans

For each critical function: choose recovery strategies (workarounds, alternates, manual modes) that can meet the recovery objectives, then build the plan that executes them — activation triggers, roles and responsibilities, contacts and call trees, step-by-step recovery procedures, resource requirements. Plans are bound to the analyzed functions and linked to the BIA results, dependencies, and risks behind them.

### 4. Maintain

Plans and analyses age with the business. Products drive currency through review cycles, ownership tracking, change alerts (a dependency changed, a review date passed, an analysis is due for refresh), and — in some platform implementations — automatic dependency refreshes from asset data.

### 5. Validate

```text
Design an exercise (walkthrough / tabletop / simulation)
→ define the disruption scenario (loss of facility / people / technology / supplier)
→ activate the relevant plans into the exercise
→ record results: what worked, what failed, whether objectives were achievable
→ findings become corrective actions tracked to closure
```

Exercises are how the program proves readiness and finds the gaps that reviews miss.

### 6. Respond

When a real disruption occurs, the plan is activated — from the continuity platform itself or from an integrated crisis-management capability. Responders get the current plan, recovery tasks are tracked as they are completed, and the platform records what was activated and how recovery actually went against the objectives.

### 7. Govern and report

Throughout, the program manager works from dashboards: analysis coverage, plan currency, exercise history, open gaps, remediation progress. This is also the layer auditors and regulators consume.

## Interfaces

Described in conceptual terms; exact layouts vary by product.

### Function / process inventory

The program's backbone surface.

- the registered business functions with owners, criticality, and analysis/plan status
- primary actions: register a function, assign an owner, launch an analysis, check coverage

### Impact-analysis workspace

Where BIAs are created, answered, and approved.

- questionnaire tabs for impact categories and dependencies; dependency grids or trees; computed recovery objectives; state and approval status
- primary actions: create analysis from template, answer/validate assessments, submit for review, approve or return

### Plan library / plan editor

Where plans live.

- plan records bound to functions, with sections for strategies, roles, contacts, procedures, and resources; version and review status; export to document formats
- primary actions: create plan (often from template), link strategies and dependencies, route for approval, publish/distribute, open on mobile

### Exercise workspace

Where validation happens.

- exercise records with type, scenario, loss types, activated plans, participants, timeline
- primary actions: schedule exercise, select plans to test, record results, raise findings, convert findings to actions

### Dashboards / reporting

The governance surface.

- analysis coverage, plan currency, exercise coverage, open gaps and remediation status, criticality rankings
- primary actions: filter by division/function, export reports, drill into a function

### Mobile plan access

A responder-facing surface: current plans, contacts, and procedures on a phone, available when facilities and networks are not.

## Important Rules / Behaviors

### The BIA gates the plan

Plans are built against analyzed functions. The analysis establishes the recovery objectives the plan must meet; without it, plan content has no prioritization basis. In products with formal lifecycles, an analysis must reach its approved state before it anchors plan content, and approved analyses become read-only.

### Recovery objectives drive everything downstream

The recovery time and recovery point objectives produced by the analysis are the yardstick for strategy choice, plan content, exercise evaluation (did the recovery meet the objective?), and gap identification (capability falls short of objective).

### Plans must stay current

A plan that no longer matches the business is the category's founding anti-pattern. Products therefore enforce or encourage review cycles, ownership currency, and dependency freshness — some automatically updating plan dependencies when upstream asset data changes.

### Exercises produce obligations

Exercise findings are recorded and converted into corrective actions with owners; an unremediated finding is visible program debt. Exercise results also update the plan's validation history.

### Activation is recorded

When a plan is activated for a real event or an exercise, the activation itself is a tracked record — which plan, which event, which strategies and tasks were used, and how the outcome compared to objectives. This history feeds the next review cycle.

### Access follows program roles

Function owners see and edit their own functions' analyses and plans; the program team sees everything and controls methodology; executives see readiness reporting. Mobile plan access exists precisely so that current plans remain reachable when normal systems and workplaces are not.

## Variants

- **Dedicated resilience suite** — BCM as the foundation product of a resilience platform, flanked by IT disaster recovery, crisis management, third-party risk, and operational risk products sharing one data model.
- **GRC-suite module** — BCM as an application or solution area inside a governance-risk-compliance suite, sharing the suite's risk register, issues, workflow, and reporting machinery.
- **Platform module** — BCM as an application on a broader workflow platform, with dependency data fed from configuration-management databases and crisis/notification handled by sibling platform capabilities.
- **Consulting-led / template-driven** — mid-market products (and service arms of all vendors) that ship methodology, plan templates, and done-for-you analysis services; the software enforces a repeatable pipeline rather than deep configuration.
- **Operational-resilience regulatory pole** — financial-services-shaped deployments organized around important business services, impact tolerances, and scenario testing against regulatory expectations, alongside or instead of classic BIA/RTO machinery.
- **Public-sector / COOP variant** — continuity-of-operations plan templates and doctrine, sometimes with incident-command elements; the same core structures under government terminology.
- **IT-DR-heavy variant** — deployments where application and infrastructure recovery planning dominates, with business-function analysis thinner; the plan-type distinction (business continuity vs IT disaster recovery) is explicit in most products.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Governance, Risk & Compliance Platform | umbrella | GRC suites ship BCM as a module; the GRC umbrella's core is the risk × control × requirement machinery, not the function→BIA→plan continuity spine |
| Enterprise / Operational Risk Management | feeds-in | risk registers identify and score disruption risks; BCM holds the continuity response (analyses, plans, exercises) to those risks |
| Emergency Management Platform | event-side sibling | EM coordinates a response to an unfolding event (incident container, shared picture, tracked work); BCM owns the standing plan-of-record that EM-style response consumes at activation |
| Disaster Recovery Platform | technical sibling | DR executes technical recovery of IT workloads (replication, failover, recovery points); BCM plans recovery of business functions and may include IT DR plans as plan types |
| Incident Management | escalation source | incidents are logged and managed in their own lifecycle; escalation to a crisis is what triggers plan activation |
| Crisis Management | activation context | crisis management coordinates people and communication during the event; the plan being executed belongs to BCM |
| Compliance Management Platform | driver/output | obligations and regulatory change live there; BCM produces the continuity evidence those regimes demand |
| Business Case Management Platform | namesake only | "business case" = investment proposal appraisal; no shared object or workflow |

The most important boundary is the plan/event seam: **BCM owns the plan-of-record for continuing organizational functions; event-coordination Types own the event-of-record.** Products bundle both under one platform, but the structures remain distinct — and each is recognizable without the other.

## Representative Products

- **Fusion Framework System** (Fusion Risk Management) — dedicated enterprise-resilience suite with BCM as its foundation
- **Business Continuity Management** (ServiceNow) — BCM application on the ServiceNow platform, CMDB-integrated
- **Business Continuity & IT Disaster Recovery Planning / Resilience Management** (Archer) — BCM as a solution area of the Archer GRC suite
- **Business Continuity Software** (Quantivate, an Ncontracts company) — mid-market, template-driven BCM application in a GRC suite for financial institutions
- **Business Continuity Management** (Riskonnect) — consulting-led BCM within an integrated risk management suite

The defining core was checked against mid-market and institutional deployments (university continuity programs) and against the paper-era program shape to avoid over-fitting the definition to modern SaaS implementations.

## Sources

Research date: **2026-09-10**

- Fusion Risk Management — Business Continuity Management product page: https://www.fusionrm.com/solutions/business-continuity-management/ ; platform overview: https://www.fusionrm.com/what-is-fusion-risk-management
- ServiceNow — Business Continuity Management product page: https://www.servicenow.com/products/business-continuity-management.html ; official docs (BCM overview, create BIA, BIA workspace, RTO/RPO calculation, RTO/RPO and recovery tiers, release notes) under https://www.servicenow.com/docs/
- Archer — Resilience Management solution and Business Continuity & IT Disaster Recovery Planning use-case documentation: https://help.archerirm.cloud/ ; Business Impact Analysis articles: https://community.archerirm.com/
- Quantivate — Business Continuity Software product page: https://www.quantivate.com/business-continuity-software/
- Riskonnect — Business Continuity Management product pages and fact sheets: https://riskonnect.com/solutions/business-continuity-management-software/ ; https://go.riskonnect.com/hubfs/Riskonnect/BCR___Business_Continuity_Management_Fact_Sheet.pdf
- Carnegie Mellon University, Disaster Recovery and Business Continuity Services — Fusion Framework deployment description (third-party deployment evidence): https://www.cmu.edu/drbc/bc/index.html

> Sourcing limitations: the ServiceNow documentation site is a JavaScript application that could not be fetched directly; its evidence comes from verbatim search-engine excerpts of the official docs pages, so field-level precision is reduced. Riskonnect pages returned only images on direct fetch; evidence comes from official product pages and fact sheets via search excerpts. Fusion's customer help center is login-gated; official product pages and a third-party deployment description were used. Standards and regulatory regime texts (ISO 22301, financial-services operational resilience rules) were not fetched directly and are described only as the sampled products present them. Precise numeric limits, default values, and plan-template details are intentionally not stated in this document; they remain in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
