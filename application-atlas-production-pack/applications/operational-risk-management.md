# Operational Risk Management

## Overview

An **Operational Risk Management (ORM) application** is the system of record for managing the risks that live in an organization's day-to-day operations — the risks of failed or inadequate internal processes, people, and systems, or of external events. It is the workbench of the operational-risk function (a second-line role): it holds the process-anchored risk register, runs the risk-and-control self-assessment campaigns that engage the front line, and captures the actual losses and incidents that feed evidence back into the ratings.

The defining structure is small:

```text
Process-anchored operational risk records
└── Risk-and-control self-assessment loop (first line assesses, second line reviews)
    └── Loss event capture, linked back to risks and controls
```

Everything commonly associated with mature ORM programs — key risk indicators with thresholds, control testing cadences, scenario analysis, appetite statements, board heat maps — is widespread in current products but is not part of the defining core. A loss register with paper self-assessments and a mapped control list fits this definition without any of those specifics.

The discipline is deepest in financial services (where "operational risk" has a regulatory definition and examination regime), but the same structure serves non-financial organizations that manage process failures and losses as a risk program. When the dominant surface shifts to the enterprise-wide roll-up of all risk categories to leadership, the product is drifting toward Enterprise Risk Management; when the objects are workplace hazards, job steps, and safety permits, it is a different product world entirely (EHS software that happens to share the name).

## Users & Context

ORM is organized around the **three-lines model**:

Primary users:

- **first-line process and business owners** — the managers who run the operations where risk lives; they complete self-assessments, confirm which risks and controls still apply, report losses, and execute controls
- **the operational risk function (second line)** — risk managers who define the taxonomy and methodology, scope and route assessment campaigns, review and challenge first-line ratings, investigate loss events, and aggregate the picture

Secondary users:

- **internal audit (third line)** — consumes the register and control records for risk-based assurance planning
- **executives and the board** — consume dashboards and reports on operational exposure
- **any employee** — commonly able to report a loss event through an intake form, often without a full system account

The typical context is a periodic operating cadence: annual (or more frequent) assessment cycles, ongoing loss reporting, indicator monitoring between cycles, and quarterly or board-level reporting. In financial institutions the cadence and outputs are shaped by regulatory examination expectations.

## Core Model

### The Defining Core

```text
Process-anchored operational risk records
└── Risk-and-control self-assessment loop
    └── Loss event capture, linked back to risks and controls
```

Three structures. If any one is removed, the product is no longer recognizable as ORM:

- **Process-anchored operational risk records** — a persistent register of risks arising from failed processes, people, and systems, or external events. Each record is attached to the business unit, process, or activity where the risk lives, carries a named accountable owner and a status, and is rated on the organization's standardized severity scales (typically likelihood × impact). The anchoring is what makes it *operational* risk: the record knows where in the business the risk lives. Without the anchor, the register becomes a generic enterprise risk list.
- **The risk-and-control self-assessment loop (RCSA)** — the characteristic workflow of the type. A campaign is scoped by unit or process; a self-assessment is generated for each scope and routed to the first-line owner; the owner confirms what still applies, reassesses what changed, and adds what is new — for both the risks and the controls that mitigate them; the second-line risk function reviews and approves the result. Risks are tied to the controls that cover them, so the register shows coverage rather than a list of worries. Without this loop, the register is a second-line artifact nobody in the business feeds.
- **Loss event capture linked back to risks and controls** — actual operational losses and incidents are recorded as first-class records (with dates, impact, and narrative), investigated for root cause, and linked to the risk records and controls involved. This is the feedback loop that puts evidence behind a rating instead of memory, and it is the structure that most distinguishes ORM from assessment-only risk tooling.

### Capabilities Shared by Mature Products

A typical modern ORM product carries most of these. They are not what makes the product ORM, but they make the program practical:

- **Key risk indicators (KRIs)** — metrics assigned to priority risks, reported by named metric owners on a set frequency, with red/amber thresholds that trigger alerts or escalation when breached.
- **Control testing** — controls documented with type (preventative/detective/corrective) and tested on a defined cadence; results feed reporting and the audit posture.
- **Inherent vs residual scoring** — the same risk rated before and after controls, with the second line challenging the residual rating.
- **Risk appetite and thresholds** — board-approved tolerance levels translated into measurable limits, with escalation paths when ratings or indicators exceed them.
- **Scenario analysis** — structured workshops estimating severity for severe, low-frequency risks where loss data is scarce.
- **Issue / corrective-action management** — findings from assessments, losses, and control failures tracked to closure.
- **Campaign rhythm and snapshots** — assessment cycles (commonly annual with periodic refresh on higher-risk processes) and snapshots showing how a rating moved since the last cycle.
- **Dashboards and reporting** — risk and loss dashboards, heat maps, and board-ready views; user-attributed audit trail throughout.
- **Open intake** — loss reporting forms that reach employees outside the core user base.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. Implementations vary:

```text
Concept:          Operational risk taxonomy
Implementations:  Basel event-type categories (banking), custom process-level taxonomies, two-level enterprise/intermediate structures

Concept:          First-line engagement
Implementations:  routed self-assessment campaigns, open loss-report forms, unlimited end-user licensing for assessors

Concept:          Loss record
Implementations:  loss event applications with root-cause workflow, incident/issues applications linked to risks
```

A reader who only encounters a banking-grade implementation should still be able to recognize a non-financial ORM program from the Core Model.

## How It Works

### Run an assessment cycle

```text
Scope the campaign by business unit or process
→ generate a self-assessment for each scope
→ route it automatically to the first-line process owner
→ the owner confirms what still applies, reassesses what changed, adds what is new
→ the risk function reviews and challenges the ratings
→ approve and snapshot the result
→ compare against the previous cycle
```

This is the type's defining interaction loop. The first line does the confirming; the second line does the challenging; the system carries the campaign from scope to approved snapshot.

### Capture and work a loss event

```text
A loss or incident occurs
→ anyone (or a provisioned user) logs it: dates, impact, narrative
→ the risk function investigates: root cause and impact analysis
→ the event is linked back to the risk record and the control involved
→ corrective actions are raised and tracked
→ the rating and control coverage are revisited in light of the evidence
```

### Monitor between cycles

```text
Metric owners report indicators on their assigned frequency
→ thresholds (red/amber) are evaluated
→ a breach alerts or escalates to the risk function
→ trends surface before a loss does
```

### Report

```text
Register + loss data + indicator status + control test results
→ aggregated by unit, process, and risk category
→ dashboards for managers, board-ready views for leadership
→ regulator-facing reporting where the segment requires it
```

### Core vs Common vs Optional

**Defining core** — without these, not ORM:

- process-anchored operational risk records with owners and standardized ratings
- the risk-and-control self-assessment loop (first line assesses, second line reviews/approves)
- loss event capture linked back to risks and controls

**Common mature structure** — present in most modern products:

- KRI monitoring with thresholds and alerting
- control testing on a cadence
- inherent/residual scoring and second-line challenge
- appetite thresholds and escalation
- issue/corrective-action management
- snapshots, trends, dashboards, board reporting
- open loss intake

**Variant / optional** — depends on segment, deployment, regulatory posture:

- Basel event-type taxonomy and regulator-facing reporting (financial services)
- scenario analysis as a first-class method (common where loss data is scarce)
- quantitative loss-exposure modeling
- operational-resilience linkage (BIA results feeding process-based assessments)
- AI assistance (linkage discovery, first-pass assessment, response-plan drafting)
- standalone tool vs module of a GRC/IRM suite

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Risk register

The system's center of gravity.

- lists operational risk records by unit, process, category, owner, rating, and status
- shows control coverage per risk
- primary actions: create/edit a risk, assign an owner, rate it, link controls, drill into detail

### Assessment campaign workspace

The second-line manager's campaign surface.

- campaign scopes, per-scope self-assessments, routing and progress tracking
- primary actions: scope a campaign, generate and route assessments, monitor completion, review and approve submitted assessments

### Self-assessment form

The first-line owner's surface.

- pre-populated with the scope's existing risks and controls
- primary actions: confirm what still applies, reassess ratings, add new risks or controls, submit for review

### Loss event log

The record of what actually went wrong.

- loss events with dates, impact, narrative, root-cause analysis, and links to risks and controls
- primary actions: log an event, investigate, link to risk/control, raise corrective actions, close

### Indicator / KRI view

The between-cycles monitoring surface.

- indicators with owners, reporting frequency, and threshold state
- primary actions: report a metric value, configure thresholds, acknowledge or escalate a breach

### Dashboards / reporting

- risk and loss dashboards for managers; heat maps, top-risk views, and trend comparisons for executives and the board
- primary actions: filter by unit/process/category, export or present board views

### Administration

- taxonomy and rating-scale configuration, campaign templates, roles and permissions, intake-form publishing

## Important Rules / Behaviors

### The first line assesses; the second line approves

The characteristic division of labor: process owners confirm and rate their own risks and controls, but the risk function reviews, challenges, and approves before a result becomes the record. A self-assessment is not the register until the second line has acted on it.

### Loss events are evidence, not just incidents

A loss event is not closed when the operational problem is fixed; it is worked to a root-cause conclusion and tied back to the risk and control records it touches. The linkage is what turns a rating into a defensible position.

### Every object carries a named owner

Risks, controls, indicators, and loss events each have an accountable owner and (commonly) a due date. Work lands with the person who can act on it.

### Ratings are comparable because the scales are shared

All units rate against the organization's common taxonomy and scales; customizing the scales is a supported (and consequential) administrative act, since it changes what every comparison means.

### The register is a living record, not a snapshot

Assessment cycles, indicator breaches, and loss events continuously update the register; snapshots preserve how exposure looked at each cycle so movement is visible.

### Attribution and audit trail

Who assessed, who approved, who reported a loss, and when — recorded and queryable. This matters because the register is consumed by internal audit and, in regulated segments, by examiners.

## Variants

- **Banking / financial-services ORM** — the deepest segment form: Basel event-type taxonomy, regulator-facing reporting cadences, scenario analysis, and examination-grade evidence; anchored to supervisory frameworks (FFIEC-style booklets, heightened standards, credit-union equivalents).
- **Non-financial enterprise ORM** — the same core without the regulatory overlay: process-level risk registers, self-assessments, and loss tracking for manufacturers, utilities, insurers, and other corporates.
- **Suite module vs standalone** — in the current market ORM is most often a solution or application inside a broader GRC/IRM platform (alongside ERM, compliance, audit, third-party, resilience); standalone ORM tools are the reduced case.
- **Combined ERM+ORM deployments** — one platform hosting both, with the operational-risk machinery (RCSA, losses) feeding the enterprise register.
- **Resilience-adjacent ORM** — business-impact-analysis results and continuity data rolled into process-based assessments.
- **AI-assisted ORM** — emerging: automated linkage discovery across risks, issues, and losses; first-pass assessment drafting; response-plan generation with human approval.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Enterprise Risk Management | closest sibling — shares risk records, controls, RCSA, loss events | ERM centers on the enterprise-wide register aggregated to leadership across all risk categories; ORM centers on the process level, first-line engagement, and the loss feedback loop. Remove the enterprise cross-category roll-up → ORM; remove the process/loss anchoring → ERM |
| Governance Risk & Compliance Platform | broader host | the suite (policy, compliance, audit, ethics) within which ORM usually ships as a module |
| Internal Controls Management | adjacent | anchored on the control library and its testing/compliance mapping; ORM is anchored on risks and losses, with controls as the mitigation linkage |
| Incident Management (IT/operational) | adjacent | restores service (detection→response→resolution); ORM loss events are risk-program records for root-cause and loss analysis feeding the register |
| Operational Resilience | adjacent | manages disruption preparedness for important business services (impact tolerances, recovery, testing); feeds and feeds on ORM but with different primary objects |
| Third-party Risk Management | adjacent | scopes the same risk machinery to vendor/counterparty relationships and their lifecycle |
| EHS / HSE Platform | name-collision only | "Operational Risk Management" is also used for workplace-safety hazard management (job safety analysis, lockout/tagout, permits to work) — different objects, users, and regulatory world |
| Financial Risk Management Platform | different domain | market/credit/liquidity risk with quantitative models for financial institutions; ORM covers process/people/system/external-event risk |

The boundary with Enterprise Risk Management is the most important one, because the two types share every building block. The structural difference is the center of gravity: ORM lives at the process level with the front line doing the assessing and losses as first-class evidence; ERM lives at the enterprise level, aggregating all risk categories for leadership.

## Representative Products

- Archer (Enterprise & Operational Risk)
- LogicGate Risk Cloud (Operational Risk Management)
- 360factors Predict360 (Operational Risk Management for financial institutions)

The Core Model was checked against a non-GRC use of the name (Origami Risk's EHS Operational Risk Management) to confirm the type boundary, and against the pre-Basel loss-register/RCSA pattern to avoid over-fitting to the current banking-regulatory implementation.

## Sources

Research date: **2026-09-10**

Primary vendor surfaces (product/use-case pages):

- Archer — https://www.archerirm.com/enterprise-operational-risk
- LogicGate — https://www.logicgate.ai/solutions/operational-risk-management/
- 360factors — https://www.360factors.com/products/operational-risk-management/
- Origami Risk (boundary probe) — https://www.origamirisk.com/solutions/ehs/operational-risk-management/

> Sourcing limitation: deep help-center articles (Archer Community KB, LogicGate KB, ServiceNow IRM docs, MetricStream) were not reachable from the research environment on 2026-09-10. Claims are calibrated to product-page and vendor-educational-page evidence; precise numeric limits, exact state names, and default settings are intentionally not stated. ServiceNow IRM and MetricStream — both significant in this market — could not be sampled; their absence may under-represent the workflow-platform-embedded form of the type.

Detailed evidence, product-by-product observations, cross-product comparison matrix, and the historical / market-sample breadth check are recorded in the paired Research Notes.
