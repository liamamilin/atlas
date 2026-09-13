# Building Condition Assessment

## Overview

A **Building Condition Assessment** application is the system of record for quantified building condition. It organizes a building portfolio into assessable systems and components, captures structured field observations of each element's condition — ratings, deficiencies, photos, remaining useful life — translates those observations into repair and replacement costs, and aggregates them into condition indices, a deferred-maintenance backlog, and multi-year capital renewal plans.

The practice it supports is commonly known as a facility condition assessment (FCA): a structured evaluation of a building's components and systems to determine their condition, remaining useful life, and estimated cost to repair or replace them, used to support budgeting, capital planning, and deferred-maintenance analysis.

The defining core is small:

```text
Assessed building elements (portfolio → buildings → systems/components as identified records)
└── Structured condition observations (rating, deficiency, photos, location, recommended action)
    └── Condition-to-cost translation (repair/replacement estimates → condition indices,
        needs backlog → capital renewal plan)
```

Everything else commonly associated with the category — mobile offline capture, floor-plan guidance, industry cost databases, dashboards, funding scenarios, "living" continuously refreshed data, vendor-conducted assessment services — is standard capability that mature products add around this core. Remove the cost-quantified outcome and what remains is an inspection checklist tool; remove the structured observations and what remains is a static asset register; remove the building elements themselves and what remains is a generic survey form.

## Users & Context

Primary users:

- **field assessors** — walk the buildings and record what they see: condition, deficiencies, photos, recommended actions. They may be the owner's in-house staff or engineers/assessors from an AEC or facilities-services firm hired to produce the assessment as a client deliverable.
- **facility managers / capital planners** — own the resulting data; review and validate findings, organize needs, set priorities, and build the capital plan.
- **executives, boards, and funding authorities** — consume the aggregated outputs: condition indices, backlog figures, funding scenarios, and the defensible case for capital investment.

Secondary users:

- **maintenance teams** — receive work arising from assessment findings and, in integrated deployments, feed completed-work data back to keep the assessment current.
- **consultants and analysts** — run scenarios, benchmark costs, and prepare reports.

The work environment is split between the field (tablet or smartphone capture, often without reliable connectivity, moving through buildings room by room) and the office (data validation, cost analysis, prioritization, plan building, reporting). Typical customers are portfolio owners — school districts, universities, state/local/federal government agencies, healthcare systems, housing authorities, and commercial property owners — plus the engineering and facilities-services firms that serve them. Assessments are typically conducted portfolio-wide on a recurring cycle, with increasing emphasis on keeping the data continuously current rather than re-surveying from scratch every few years.

## Core Model

### The Defining Core

**Assessed building elements.** The portfolio is decomposed into identified, assessable records: building systems (HVAC, electrical, plumbing, vertical transport, envelope, structural) and their components (boilers, air handlers, roofs, doors, flooring, and so on). Each element record carries its identity, location within the building, functional use, age — and often renovation age, since a replaced component resets the clock. The granularity is a deliberate choice: a project-level assessment catalogs nearly every component; a portfolio-level assessment may evaluate major systems only.

**Structured condition observations.** Attached to each element are the observations from the field: a condition rating, observed deficiencies, photos, notes pinned to a location, remaining useful life, and a recommended action — repair or replace. The observations are evidence-backed; defensibility is the point, because the output will be used to justify spending. Standardized checklists and component taxonomies keep different assessors consistent across a large portfolio.

**Condition-to-cost translation.** Observed condition is expressed in financial terms. Each finding carries a cost estimate — commonly drawn from an industry-standard construction cost database, adjusted for the building's location and complexity — and a repair-vs-replace recommendation. Findings roll up into a needs repository or deferred-maintenance backlog, and into condition indices per building and per portfolio. The most widely recognized index is the Facility Condition Index (FCI), used as an unbiased measure for channeling capital to facilities. Exact index definitions and rating scales vary by product and practice.

### Standard Capabilities

Mature products commonly add:

- **Survey machinery** — assessment project setup, standardized component taxonomies and checklists, baseline data import (from asset registers, drawings, or prior assessments).
- **Mobile field capture** — tablet/phone apps that work offline, capture photos and notes, and pin them to locations; digital floor plans with element pins that guide the assessor through the building.
- **Cost data libraries** — industry-standard unit-cost databases connected directly into the estimation step, with location/complexity adjustment tools.
- **Needs and backlog management** — a living repository of needs across physical assets; repair-vs-replace analysis; remaining-useful-life and deterioration modeling.
- **Prioritization and planning** — needs ranked by risk, urgency, cost, and impact (with configurable business rules in some products); multi-year capital plans; funding scenarios showing what different budget levels do to portfolio condition; cash-flow projection per project.
- **Dashboards and reporting** — condition indices, backlog trends, renewal costs at a glance; role-configured views; report builders that assemble the client or board deliverable.
- **Integration** — connections to facility/asset management, maintenance (CMMS), financial/ERP, and GIS systems, so assessment data feeds work execution and operational data keeps the assessment current.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:   Assessed element records
Implementations:  component-level catalogs, major-systems evaluations, modeled (statistical) building profiles

Concept:   Structured condition observations
Implementations:  digital checklists, floor-plan-pinned photos/notes, tag-scanning capture apps, expert walk-downs

Concept:   Condition-to-cost translation
Implementations:  integrated cost databases, unit-cost libraries, square-foot costing models, in-house rates
```

A reader who encounters only one implementation — say, a consultant producing a component-level FCA report — should still recognize an owner's in-house, systems-level self-assessment as the same Type.

## How It Works

### Prepare the assessment

```text
Define scope (buildings, systems, depth)
→ set up or reuse the component taxonomy and checklists
→ import baseline data (asset lists, floor plans, prior assessments, ages)
→ assign assessors
```

Depth is a first-class decision: portfolio-level funding decisions may need only modeled estimates, while execution-level planning needs component-level detail.

### Survey the buildings

```text
Walk the building (guided by floor plans / checklists)
→ for each element: record condition, deficiencies, photos, notes
→ capture remaining useful life and a recommended action (repair or replace)
→ data syncs when connectivity returns (offline capture is standard)
```

The field loop is optimized for speed and consistency — every extra step costs assessor time, and standardization is what makes results comparable across buildings and assessors.

### Quantify

```text
Attach cost estimates to findings (from a cost database or in-house rates, adjusted for location/complexity)
→ classify each need: repair vs replacement, urgency, system, facility
→ project remaining useful life and deterioration where modeled
```

### Aggregate and plan

```text
Roll findings up per building and per portfolio
→ compute condition indices and the deferred-maintenance backlog
→ prioritize (risk, urgency, cost, impact, facility/component priority)
→ build funding scenarios and a multi-year capital plan with cash-flow projection
→ generate the report / funding case for executives and stakeholders
```

The output is a defensible investment strategy — a plan whose entries can be traced back to the documented needs that justify them (some products make this traceability explicit).

### Keep it current

Two postures exist side by side:

- **Snapshot** — the assessment is a periodic event; data is re-collected on a multi-year cycle.
- **Living** — the assessment dataset is connected to the owner's facility/maintenance system; completed work orders, inspections, and condition updates flow back so the assessment stays current without starting over.

Integrated deployments increasingly favor the living posture, but the snapshot survey remains the common form, especially for consultant-produced assessments.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Assessment project setup

Purpose: configure a survey run. Typical information: scope, buildings, component taxonomy, checklists, assigned assessors, imported baseline data. Primary actions: create/clone an assessment, configure templates, import data.

### Mobile field capture

Purpose: record observations in the field. Typical information: element list for the current room/area, condition ratings, deficiency entries, photo attachments, location pins on the floor plan. Primary actions: select element, record condition/deficiency, attach photo, add note, set recommended action. Works offline.

### Element / deficiency detail

Purpose: the record for one assessed element or finding. Typical information: identity, location, age, condition rating, photos, remaining useful life, recommended action, cost estimate. Primary actions: edit observation, attach evidence, assign cost, classify need.

### Cost estimation view

Purpose: attach and adjust money to findings. Typical information: unit costs from the cost library, quantities, location/complexity adjustments, repair-vs-replace comparison. Primary actions: pull cost data, adjust, approve estimate.

### Condition dashboards

Purpose: portfolio-level understanding. Typical information: condition indices per building, backlog totals and trends, renewal costs, elements past expected life, most expensive replacements. Primary actions: filter, drill down to buildings/systems, export.

### Capital plan / scenarios

Purpose: turn needs into a fundable plan. Typical information: prioritized project list, multi-year phasing, funding scenarios, cash-flow requirements, traceability from projects to needs. Primary actions: prioritize, model budget levels, phase projects, generate plan documents.

### Report builder

Purpose: assemble the deliverable for clients, boards, or funding authorities. Typical information: executive summary, condition indices, findings with photos, cost tables, recommended plans. Primary actions: drag-drop sections/charts, generate, export.

## Important Rules / Behaviors

- **Observations are evidence-backed.** Photos, notes, and locations accompany findings because the output must survive scrutiny from boards, funding authorities, and auditors. An unsupported rating undermines the whole deliverable.
- **Condition is expressed in physical AND financial terms.** A rating alone is not an assessment outcome; the cost translation and aggregation are what make the data decision-ready.
- **Standardization enables comparison.** Shared taxonomies, checklists, and cost data are what make conditions comparable across buildings, assessors, and years — the basis for portfolio-level indices.
- **Assessment data has a shelf life.** Buildings age and get repaired; a stale assessment misleads capital decisions. Products address this with re-assessment cycles or living updates fed from maintenance systems.
- **Repair-vs-replace is the recurring decision.** Each finding carries a recommendation; cost history, condition, and remaining life are the inputs.
- **Depth is a scope decision, not an accident.** Modeled estimates, systems-level evaluations, and component-level catalogs serve different decisions; mixing them up produces either overpriced surveys or under-powered plans.
- **Costs are planning-grade.** Estimates from cost libraries support budgeting and prioritization; they are not construction bids.
- **Separation of observation and decision.** Field assessors record; planners prioritize; executives fund. Role-configured views reflect this division.

## Variants

- **Software-only (self-assessment)** — the owner's trained staff conduct assessments in the product; suited to mature capital-planning organizations.
- **Service-led** — the vendor's or a firm's assessors conduct the survey and deliver the report; software is the backbone. Some vendors productize this as explicit depth tiers, from statistical modeled assessments (no site visit) through building-level evaluations to project-level assessments that also document code compliance, life/safety, modernization, and resilience.
- **Assessor-firm pole** — AEC and facilities-services firms use the software to produce FCAs as client deliverables, often priced per seat and by area surveyed.
- **Owner-operator pole** — owners run assessments in-house, ideally as living datasets connected to their facility management stack.
- **Segment tunings** — K-12 and higher education (deferred maintenance, bond funding), government (public accountability, multi-year appropriations), healthcare (critical systems), commercial real estate (portfolio condition and reserves), public infrastructure owners (broader asset classes beyond buildings).
- **Regional vocabulary** — US practice centers on FCA/FCI terminology; UK practice speaks of stock condition surveys; Australian/public-asset practice uses ISO 55000-flavored condition assessment vocabulary. The underlying structure is the same.
- **Scope extensions** — energy assessments, accessibility surveys, seismic and life-safety evaluations, due-diligence inspections, equipment tagging/inventory — sold by some vendors as add-on assessment types sharing the same machinery.
- **Packaging** — standalone assessment/capital-planning platforms vs assessment modules inside broader facility or asset management suites.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Building Asset Management | sibling; downstream record keeper | maintains the continuous care loop (work orders, service history) on asset records; condition assessment is periodic data production that feeds it. Suite vendors often ship them as separate modules |
| Property Inspection Application | adjacent; transaction context | point-in-time inspection of a single property for a real-estate transaction (buyer/lender due diligence) vs portfolio condition survey for capital renewal planning |
| Building Commissioning Platform | adjacent; verification vs condition | verifies that systems perform per requirements through tests; condition assessment surveys what state existing facilities are in |
| CMMS / Building Maintenance Management | downstream executor | executes maintenance work; assessment findings may raise work orders, but the care loop is not this Type's object |
| Capital Improvement Planning | downstream consumer | public-sector capital program planning/approval; consumes condition indices and needs as input drivers |
| Facility Management System / IWMS | broader suite | real-estate/space/lease estate is the center; condition assessment is at most one feed |
| Property Assessment System | false friend | tax valuation of property; shares only the word "assessment" |
| Construction Quality Management | different phase | work compliance during construction vs condition of existing buildings |
| Building Energy Management | adjacent scope | optimizes consumption/performance; energy audits measure use, not physical deterioration (some vendors bundle energy assessment as an add-on) |
| Environmental Site Assessment | false friend | contamination due diligence vs physical condition; different object entirely |

The most important boundary is with **Building Asset Management**: both hold building-element records with condition, and market products blur them. The structural difference is the center of gravity — the assessment deliverable and the capital decision it supports versus the continuous care loop on the asset record. Remove the cost-quantified capital outcome from this Type and it collapses into an inspection tool; remove the care loop from asset management and it collapses into an assessment registry.

## Representative Products

- AkitaBox FCA — digital FCA capture/cost/insights/reporting; dual audience (AEC assessors and owner/operators); "living FCA" integrated with the vendor's facility management platform
- Intellis FOUNDATION — pure-play facility condition assessment and capital planning platform (Conditions / Needs / Projects / Plans); education, government, housing, corporate
- Gordian — Assessments and Capital Planning: tiered FCA services (modeled → self-assessment → building-level → project-level) built on an industry-standard construction cost database and a cloud planning platform
- Brightly Assetic — boundary anchor: condition assessments as a module inside a public-infrastructure asset management suite (Australia/regional)

## Sources

Research date: **2026-09-06**

- AkitaBox — FCA Software product page: https://home.akitabox.com/software/akitabox-fca/
- Intellis — FOUNDATION product page: https://www.intellis.io/foundation/ (and https://www.intellis.io/)
- Gordian — Assessments and Capital Planning product page: https://www.gordian.com/products/assessment-and-planning/
- Gordian — "The Facility Condition Assessment: Gordian's Options for Data Collection": https://www.gordian.com/solutions/facility-condition-assessment/
- Brightly (Siemens) — Assetic product page: https://www.brightlysoftware.com/products/assetic
- Accruent — Products index (market observation only): https://www.accruent.com/products

> Sourcing limitation: evidence comes from official vendor product and resource pages; in-product help-center documentation was not fetched in this pass. Accordingly, no field-level record schemas, exact rating scales, index formulas, numeric limits, or default settings are asserted in this document. The long-standing FCA product line of one major vendor no longer appears in that vendor's public product index (observed 2026-09-06); related market-consolidation observations are recorded in the Research Notes only. Detailed product-by-product observations, the cross-product comparison, and the historical/market-sample check are recorded in the paired Research Notes.
