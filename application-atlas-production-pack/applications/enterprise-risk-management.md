# Enterprise Risk Management

## Overview

An **Enterprise Risk Management (ERM) application** is the organization-wide system of record for the risks an organization manages as a whole. It holds a central **risk register** — structured records of identified risks, each describing an uncertain event or condition that could affect organizational objectives — and manages each risk through a standard loop: assignment to a named owner, rating on the organization's shared likelihood-and-impact scales, a recorded management response, and roll-up across business units into comparative views used to report exposure to executives and the board.

The defining core is small:

```text
Enterprise risk register (organization-wide, taxonomy-classified, owned)
  → standardized assessment (shared likelihood × impact scales)
    → recorded management response (treat / accept / avoid / transfer)
      → enterprise aggregation & board-level reporting
```

Everything else commonly associated with ERM software — assessment campaigns, control libraries, key risk indicators, loss-event intake, quantitative modeling, AI assistance — is standard or optional structure that makes the register operable, but a product without the four-part core above is not an ERM system: it is either a narrower tool (a bare list, a process-level tracker) or a different type. The "enterprise" part is definitional: what distinguishes the type is one shared taxonomy and one register spanning business units, so that risk exposure becomes comparable and aggregable across the organization — the exact thing spreadsheets and per-silo tools cannot sustain.

## Users & Context

ERM software serves an organization's risk governance function rather than a single department's daily transactions. Typical users:

- **Risk program owners / risk managers** (enterprise risk, or CRO office): configure the risk taxonomy, rating scales, and organizational scoping; design and launch assessment campaigns; review and approve incoming assessments; maintain the register; produce leadership reporting.
- **Risk owners and control owners** (business-side managers): named individuals accountable for specific risks; complete assessment forms, confirm or update ratings, log loss events, and carry out mitigation tasks inside their area.
- **Executives and board members**: consume aggregated views — heat maps, top-risk rankings, trend summaries — usually without doing data entry.

The surrounding context is periodic governance: quarterly or annual risk cycles, board and audit-committee reporting, and alignment with frameworks such as COSO ERM or ISO 31000 that many programs use to structure their taxonomy and assessment method. Risk data often arrives from people who do not work in the platform day-to-day (front-line managers completing a self-assessment, employees reporting a loss), so intake is commonly designed to reach occasional users through simple forms or shared links.

## Core Model

### The risk register

The center of the system is the **risk register**: the persistent, organization-wide population of risk records. A **risk** represents an identified uncertain event or condition with potential impact on the organization's objectives — operational failures, financial exposures, compliance breaches, strategic or reputational harm, technology and third-party dependencies. A typical risk record carries:

- **Description** of the risk event and its potential impact
- **Classification** in the organization's risk taxonomy — categories (strategic, operational, financial, compliance, technology…) and often two levels, enterprise risks with intermediate sub-risks beneath them
- **Organizational scope** — the business unit, location, process, or entity the risk belongs to
- **Owner** — the named person accountable for the risk
- **Assessment fields** — likelihood and impact ratings on the organization's shared scales, commonly recorded before mitigation (*inherent*) and after (*residual*)
- **Response decision** — how the organization will handle the risk
- **Status and history** — assessment state, changes over time, attributed audit trail

### The structures that make the register comparable

Three structures distinguish an ERM register from a per-silo risk list:

- **Shared risk taxonomy.** All units classify and rate risk against one structure defined once by the risk function, so "high" means the same thing in every division and cross-unit comparison holds up.
- **Organizational hierarchy.** Risks attach to entities — business units, locations, processes — forming the dimension along which the register rolls up.
- **Standardized scales.** Rating scales (typically likelihood × impact, qualitative or numeric) are organization-wide and configurable; a rating change or a re-assessment is recorded against the same scale as the previous cycle.

### The connected objects

Mature products surround the register with objects that give assessments evidence and give responses follow-through:

- **Controls** — the mitigating mechanisms mapped to the risks they cover, so the register shows coverage rather than a list of worries.
- **Mitigation / treatment plans** — the actions pursuing the chosen response, with owners and due dates.
- **Key risk indicators (KRIs)** — measurable signals assigned to risks, tracked on a cadence against alert thresholds.
- **Loss / incident events** — occurrences linked back to the risks they materialized and the controls that were involved, feeding root-cause analysis and rating changes.
- **Assessments** — the instrument instances (campaign-based self-assessments, or one-off evaluations) that produce and refresh the ratings on the record.

### One structure, many implementations

The model is conceptual; products realize it differently:

```text
Concept:            Standardized assessment
Implementations:    qualitative ordinal scales, numeric matrices,
                    configurable rating factors, financial quantification

Concept:            Assessment instrument
Implementations:    campaign-based risk-and-control self-assessments,
                    ad-hoc evaluation workflows, agent-drafted first passes

Concept:            Enterprise roll-up
Implementations:    heat maps, top-risk rankings, unit-vs-unit comparison,
                    board report packs, dashboard trend lines
```

## How It Works

The life of the register runs through four loops. Exact sequence and naming vary by product; the loops themselves recur across the researched sample.

### 1. Identify and intake

```text
Risk surfaced (campaign question, front-line submission, loss event, executive concern)
→ recorded as a risk record with description, category, and scope
→ assigned to a named owner
→ enters the register
```

Intake is commonly organized as **campaigns**: the risk function scopes an assessment round by business unit or process, generates assessment instruments for each, and routes them to the responsible owners. Organizations that already keep a register can seed the system by importing it; many programs start from a list of business units with owners and a first-pass taxonomy.

### 2. Assess

```text
Owner receives an assessment instrument
→ rates likelihood and impact on the shared scales
→ confirms or updates existing risks, adds new ones
→ submits
→ risk function reviews and approves
→ register ratings updated; residual position recorded
```

This is the loop that makes the register comparable: every unit rates against the same taxonomy and scales. Ratings are commonly captured before and after mitigation (inherent and residual), and the system keeps the history so a rating can be compared against the previous cycle.

### 3. Respond

```text
Review the assessed risk against appetite and thresholds
→ record the response decision: mitigate / accept / avoid / transfer
→ if mitigating: define treatment plan, assign tasks, map covering controls
→ track tasks and control coverage to completion
→ re-rate to the residual position
```

Risks exceeding appetite or threshold are flagged or escalated. Where indicators are in use, a KRI crossing its alert threshold pulls attention back to the risk before a loss occurs; where a loss does occur, it is logged, analyzed for root cause, and linked back to the risk and control involved.

### 4. Aggregate and report

```text
Register ratings roll up across the organizational hierarchy
→ heat map by category × rating, rankings of top risks, unit comparisons
→ trend view: how ratings and indicators moved since the last cycle
→ board / executive reporting pack
→ feeds the next assessment cycle
```

The output of this loop is the type's purpose: leadership sees current, comparable exposure across the whole organization rather than a collection of unit-local spreadsheets, and can ask — and answer — "what are our top risks, and what covers them" between cycles.

### Capability tiers

**Defining core** — without these the product is not an ERM system:

- organization-wide risk register with owned, taxonomy-classified risk records
- standardized assessment on shared scales producing comparable ratings
- recorded management response per risk
- enterprise-level aggregation and reporting across organizational units

**Standard capabilities** in mature products:

- assessment campaigns / self-assessments routed to owners, with review and approval
- inherent and residual scoring; appetite/threshold flagging
- treatment plans with tasks, due dates; linked control library showing coverage
- KRI monitoring with alert thresholds
- loss/incident intake linked back to risks and controls
- organizational-entity scoping, assessment statuses, period-over-period history
- dashboards, heat maps, board reporting; document attachments; audit trail
- role-based access for program owners, risk/control owners, and executives; intake forms reaching occasional users

**Optional / advanced**, depending on segment and maturity:

- quantitative financial-exposure modeling and scenario analysis
- deep integration with sibling GRC applications (policy, compliance, audit, third-party, continuity)
- AI assistance for intake triage, first-pass assessments, and report drafting
- BI-tool integrations and custom analytics

## Interfaces

Surfaces are described conceptually; layouts and names vary by product.

### Risk register view

The primary working surface for the risk function.

- typical information: risk list with category, scope (unit/location/process), owner, current and residual ratings, status, control coverage
- primary actions: create/import risks, filter and group by entity or taxonomy, open a record, launch or monitor assessment activity

### Risk record detail

The single-risk workspace.

- typical information: description, taxonomy placement, owner, inherent/residual ratings and their history, response decision, linked controls, mitigation plan and tasks, related indicators and loss events, change log
- primary actions: edit classification or scope, reassign owner, update ratings, record the response, link controls or events, review history

### Assessment form (owner-facing)

The instrument a risk or control owner completes.

- typical information: the risks in scope for that unit or process with their current data, rating scales with guidance
- primary actions: confirm what still applies, update ratings, add new risks, submit for review

Deliberately simple — most completers are occasional users, and campaign completion rates are the main adoption constraint of the whole program.

### Campaign / assessment management

The risk function's control surface for a cycle.

- typical information: scope (units/processes), routed instruments, submission status, review queue
- primary actions: define scope, generate and route assessments, nudge or escalate, review and approve submissions, snapshot results

### Heat map and dashboards

The aggregation surface.

- typical information: risks plotted by likelihood and impact, category breakdowns, top-risk rankings, unit comparisons, KRI status against thresholds, trend lines across cycles
- primary actions: drill into underlying records, configure views, export or distribute board reporting

### Administration / configuration

- typical information: risk taxonomy, rating scales and factors, organizational hierarchy, appetite thresholds, roles and permissions, intake form design
- primary actions: configure taxonomy and scales (a first-class activity, not a one-time setup), manage scoping and roles, design intake forms

## Important Rules / Behaviors

- **Comparability is the point of the shared scale.** Ratings are only meaningful across units because every unit assesses against the same taxonomy and scales; products therefore make scale definition an explicit, organization-governed configuration rather than a per-team choice.
- **Assessment answers are attributed and reviewable.** Owner submissions carry the submitter's identity and flow through review/approval by the risk function before they change the register; the register keeps a user-attributed audit trail.
- **A rating has a before-and-after.** Mature products distinguish the position before mitigation (inherent) from the position after controls and treatment (residual), and keep cycle-over-cycle history so movement is visible; the register is a living profile, not a static snapshot.
- **Every risk has an owner and a decision.** A risk record without a named owner or a recorded response is an incomplete record in this model; accountability ("who owns the response") is one of the clearest functional boundaries between an ERM system and a static register.
- **Thresholds drive attention.** When a rating or a monitored indicator exceeds its threshold, the system surfaces or escalates it — attention is threshold-driven rather than purely calendar-driven.
- **Events close the loop.** Losses and incidents are not isolated records; they link back to the risks they materialized and the controls involved, informing root cause and re-rating.
- **Aggregation respects structure and permissions.** Roll-up views compute across the organizational hierarchy, and who sees which risks (unit-level vs enterprise-level) is governed by role.

## Variants

- **Module of a GRC/IRM platform** — the dominant delivery in the current market: ERM as the risk-centered application of a broader suite alongside policy, compliance, audit, third-party, and resilience modules, sharing one data core.
- **Standalone ERM tool** — a focused register-plus-assessment product, common in mid-market and smaller organizations; reduced integration breadth, same core model.
- **RMIS-heritage suites** — vendors from the insurance/risk-management-information-system tradition, where the ERM register sits alongside claims, incident, and continuity management.
- **Segment tiers** — Fortune-500-scale platform deployments (long implementations, deep configuration, on-prem or SaaS) vs mid-market SaaS (fast implementation, concurrent access, methodology guidance bundled).
- **Program style** — qualitative taxonomy-driven programs (the common case) vs quantitative programs that translate exposures into financial terms via dedicated quantification capabilities.
- **Industry overlays** — financial services (regulatory operational-risk expectations shape the register and control testing), healthcare, energy/utilities, and public-sector variants.
- **AI-augmented ERM** — emerging: agents triage intake, draft first-pass assessments against the defined framework, and assemble executive reporting, with humans as final approvers.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Governance Risk & Compliance Platform | surrounding suite | GRC adds policy, obligation, control-compliance, and audit machinery on a shared data core; ERM is its risk-centered application — remove compliance/policy/audit scope and ERM still stands; remove the register and its assessment loop and it is not ERM |
| Operational Risk Management | closest sibling | shares risk records, controls, risk-and-control self-assessments, loss events, but centers on operational processes, control failures, and front-line operations; ERM centers on the enterprise-wide roll-up of top risks to objectives across all categories |
| Third-party Risk Management | scoped sibling | the same risk machinery applied to vendor/counterparty relationships and their lifecycle (due diligence, monitoring), not to the organization's whole risk population |
| Financial Risk Management Platform | different domain | market/credit/liquidity risk with quantitative models, specific to financial institutions; ERM is cross-category and mostly qualitative |
| Business Continuity Management | adjacent | manages disruption preparedness (impact analysis, recovery plans, exercises); risk data feeds it, but its primary objects are continuity plans, not the register |
| Compliance Management Platform | adjacent | anchored on regulatory obligations and their evidence, not on risks to objectives; the register may link risks to obligations |
| Internal Audit Management | adjacent consumer | audit plans and engagements provide assurance over risks and controls; audit consumes the register for risk-based planning but does not own it |
| Project Risk Management | scoped analog | risk lists bounded to a project's delivery, inside project tooling; not an enterprise-wide system of record |

The most important boundary is with the GRC Platform: in the live market ERM is almost always delivered inside one, and the two are easy to conflate. The ERM application is identifiable by its register-centric core — taxonomy, shared assessment, ownership, response, enterprise roll-up — while governance, compliance, and assurance applications organize different primary objects around it.

## Representative Products

- Archer (Archer IRM) — enterprise GRC platform; ERM delivered within a combined enterprise & operational risk use case
- LogicGate Risk Cloud — no-code GRC platform; ERM as a preconfigured workflow application with agent-assisted first passes
- Riskonnect — integrated risk suite with RMIS heritage; ERM register, assessments, heat maps, and KRIs
- LogicManager — mid-market SaaS ERM with a taxonomy-first methodology

The definition was checked against spreadsheet-era and register-style ERM practice to avoid over-fitting to any current platform pattern.

## Sources

Research date: **2026-09-06**

- Archer — Enterprise & Operational Risk Management (use-case page): https://www.archerirm.com/enterprise-operational-risk ; company/product root: https://www.archerirm.com/
- LogicGate — Enterprise Risk Management solution: https://www.logicgate.ai/solutions/enterprise-risk-management/ ; ERM Application: https://www.logicgate.ai/platform/applications/enterprise-risk-management-application/ ; platform root: https://www.logicgate.com/ ; Help Center structure: https://help.logicgate.com/
- Riskonnect — ERM Software (product page and FAQ): https://riskonnect.com/solutions/enterprise-risk-management/
- LogicManager — site navigation and methodology material: https://www.logicmanager.com/erm-software/

> Sourcing limitation: deep help-center articles (Archer Community knowledge base, LogicGate help-center articles, LogicManager University) and several vendor documentation sites (ServiceNow IRM, MetricStream, IBM OpenPages) were not reachable from the research environment on 2026-09-06. Evidence for the sampled products is therefore product-page and help-structure level. Claims in this document are calibrated accordingly: no precise numeric limits, scale sizes, default frequencies, or exact state names are asserted, and lifecycle descriptions are stated at the conceptual level.

Detailed product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
