# Business Case Management Platform

## Overview

A **Business Case Management Platform** is an organization-side system of record for investment proposals. Its center is the **business case**: a persistent, identified record in which a sponsor argues for a contemplated investment or change — the need or problem, the proposed solution or options, the money and resources it will take, and the benefits it promises — and through which the organization makes a governed fund-or-don't-fund decision.

The defining core is deliberately small:

```text
Business case record (justification narrative bound to a sponsor)
└── Structured financial appraisal (time-phased costs and benefits → computed value metrics)
    └── Governed decision lifecycle (review → approve/reject by accountable decision-makers)
```

Everything else commonly associated with the category — portfolio scoring and prioritization, benefits-realization tracking, templates, resource estimates, risk registers, document libraries, AI drafting — is standard capability that mature products add around this core, not what makes the product a business case management platform.

The platform sits between strategy and execution: above it are strategic objectives and budget cycles; below it are the projects, programs, and capital investments that approved cases become. In the current market it is usually delivered as a module of a broader project-portfolio or strategic-portfolio management suite, sometimes as a dedicated decision platform — most visibly in public-sector capital governance.

## Users & Context

Primary users:

- **Sponsor / initiative owner** — authors the case: describes the need, proposes the solution, owns the promise. Usually a business leader, product owner, IT demand owner, or program sponsor.
- **Investment board / steering committee / approvers** — review cases against criteria and thresholds, and record the approve/reject decision. In public-sector and capital settings this is often a formal governance body.
- **Finance / FP&A analysts** — validate the financial appraisal: cost and benefit forecasts, discounting assumptions, value metrics.
- **PMO / transformation office / portfolio manager** — owns the process: templates, scoring criteria, intake, pipeline hygiene, portfolio-level comparison and reporting.

Secondary users:

- **Delivery/resource leads** — contribute early resource and capacity estimates for the proposed work.
- **Benefits owners** — accountable for realizing the promised benefits after approval.
- **Executives** — consume portfolio-level views of pending and approved investments.

Typical context: annual and in-year planning/budgeting cycles, IT demand intake, capital expenditure governance, transformation program gating, and public-sector investment appraisal. The work is committee-shaped: cases are written by one party, challenged by others, and decided by a third, which is why the record — not a document on someone's laptop — is the center.

## Core Model

### The Defining Core

**Business case record.** A persistent, identified proposal for a contemplated investment or change. It carries at minimum: a name and identity, a sponsor/owner, a status, and a justification narrative — the business need or problem being addressed, and the proposed solution approach or options being considered. Cases are typically created from organization-defined templates so that proposals arrive in a comparable shape. The record is versioned and survives the whole life of the proposal; it is not a one-shot document.

**Structured financial appraisal.** Attached to the record is a time-phased model of what the investment will cost and what it will return: costs (often split into phases such as pre-project, delivery, and run/operate) and benefits (commonly classified — for example revenue, cost reduction, cost avoidance) laid out across future periods, often several years. From this structure the system computes comparative value metrics — return, ROI, payback period, and where supported, discounted measures such as net present value and internal rate of return. The appraisal is what makes cases comparable to each other and challengeable by finance; it is the structural difference between a business case and a well-written memo.

**Governed decision lifecycle.** The record moves through review and decision states. Reviewers and approvers are named and accountable; the approve/reject decision is a recorded event on the record, often with conditions, milestones, and change control attached. Approval typically gates funding and the right to proceed to execution. Rejection, deferral, and rework are normal outcomes — the pipeline exists precisely because most proposals do not get approved as first submitted.

### Standard Capabilities Around the Core

Mature products commonly add:

- **Portfolio and pipeline context.** Cases live in a shared pipeline where they are scored against strategic criteria, compared with each other, and prioritized. Common machinery includes weighted scoring models, strategic-alignment assessments, value-versus-cost-versus-risk views, what-if scenarios, and in some products mathematical optimization of the funding allocation.
- **Template and methodology governance.** Configurable case templates, section structures, scoring criteria, and approval workflows, so that every proposal is built and evaluated the same way. Vendors in this space consistently emphasize that a shared, visible methodology is what makes cross-case comparison credible.
- **Resource estimates.** Early-stage estimates of the people and capacity the investment would need, sometimes time-phased, feeding portfolio capacity checks before approval.
- **Benefits realization tracking.** After approval, the promised benefits are tracked against actuals over time, closing the loop between what was argued and what was delivered. Some products also keep a lookback history of how the case itself changed between approval and closure.
- **Risk and supporting records.** Risks, issues, assumptions, linked investments, reference documents, status reports, and conversations attached to the case.
- **Conversion to execution.** An approved case converts into a project, program, or capital investment — in some products as a first-class "convert" action, in others as a phase transition — carrying its approved financial plan forward as the budget of record.
- **Reporting.** One-click case reports for governance packs, portfolio dashboards, and analytics over the pipeline (pending value, approval rates, benefit delivery).
- **AI assistance.** Increasingly common: drafting case narratives from prompts or prior data, summarizing, and surfacing insights.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:  Business case record
Implementations:  dedicated tabbed case record; "idea"/"demand" record in a PPM suite;
                  innovation opportunity in a stage-gate system; initiative in a strategy-execution system

Concept:  Financial appraisal
Implementations:  multi-year cost/benefit forecast with discounting; cost plans → approved budget plans;
                  benefit plans vs actual transactions; revenue-stream models

Concept:  Governed decision
Implementations:  committee approval with recorded outcomes; stage gates; approval workflows;
                  financial-plan approval rights distinct from authoring rights
```

A reader who has only seen one implementation — for example, an IT demand module that turns ideas into projects — should still be able to recognize a public-sector capital appraisal tool or an innovation stage-gate system as the same Type from the core model.

## How It Works

### The case lifecycle

```text
Intake
→ a proposal enters the pipeline (often from a template), bound to a sponsor
→ Develop
→ sponsor completes the narrative: need, options/solution approach
→ finance and delivery contribute: time-phased cost & benefit forecast, resource estimates
→ Appraise
→ system computes value metrics; case is scored against strategic criteria
→ Review / Decide
→ reviewers challenge; approvers record approve / reject / defer (with conditions)
→ Fund & Convert
→ approved case funds; converts into a project/program/capital investment
→ Deliver & Track benefits
→ promised benefits tracked against actuals; case changes logged
→ Close / Look back
→ post-implementation review against the original case
```

Two loops run continuously around this lifecycle:

**The portfolio loop.** While individual cases move through their lifecycle, the portfolio owner compares them: scoring against strategy, value analysis (benefit vs cost vs risk), scenario comparison, and selection of the fundable set within budget and capacity constraints. A case's fate depends on its own merit *and* on the company it keeps.

**The challenge loop.** Between submission and decision, the case is typically revised — estimates sharpen, options are added or dropped, benefits are re-based. Mature products support progressive elaboration: the case starts light and deepens as better information arrives, with each material change visible in the record's history.

### The financial core in practice

The appraisal is usually maintained as structured, time-phased plans rather than free-form spreadsheets:

- cost plans are drafted, one is marked as the plan of record, and submitted for approval;
- in many products, an approved cost plan becomes the budget of record for the investment;
- benefit plans record what the investment promises to deliver, by class (for example revenue, cost reduction, cost avoidance), over time;
- after approval, actual transactions and realized benefits are recorded against the same structure, so plan-versus-actual is a native view rather than a reconciliation exercise.

### Who does what

The sponsor authors and defends; finance validates the numbers; the PMO runs the process and the pipeline; the board decides; delivery leads estimate and later execute; benefits owners answer, after the fact, for the promise. Permission models reflect this: the right to author a case, the right to approve it, and the right to approve its financial plans are distinct grants in the products that expose them.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Case workspace / editor

The author's primary surface: the business case as a structured document with sections or tabs — need, solution approach, forecast, results, governance, attachments.

- typical information: narrative fields, time-phased financial grids, computed metrics, status, owner
- primary actions: complete sections, attach evidence, submit for review, respond to challenges

### Financial plan grids

Time-phased spreadsheets-like grids for costs, benefits, and (post-approval) actuals.

- typical information: periods (months/quarters/years), cost and benefit classes, totals, computed metrics
- primary actions: enter/adjust figures, mark plan of record, submit for approval, compare versions

### Pipeline / prioritization views

The portfolio owner's surface over the population of cases.

- typical information: scored list or board of cases, strategic-alignment scores, value metrics, status, owner, requested funding
- primary actions: score, filter, compare, run scenarios, promote/defer/reject

### Decision / governance views

The approver's surface: a case (or a batch of cases) with the appraisal, scores, and recommendation in view.

- typical information: case summary, financials, scores, risks, conditions
- primary actions: approve, reject, defer, attach conditions, record decision rationale

### Portfolio dashboards & reports

Executive and governance-pack surfaces.

- typical information: pipeline value, approval outcomes, benefit delivery vs promise, portfolio composition
- primary actions: drill into cases, export reports

## Important Rules / Behaviors

- **Approval gates execution.** In mature products, an approved case (and often an approved financial plan) is the precondition for funding and for converting the proposal into a project or program. The approval is recorded on the record, with the approver and outcome visible.
- **The approved plan becomes the budget of record.** Where the product supports plan approval, an approved cost plan typically becomes the investment's budget; later changes go through re-approval or change control rather than silent edits.
- **Benefits are tracked against the approved case.** The promise made at approval is the baseline; realized benefits are recorded against it, which is what makes post-investment review meaningful.
- **Authoring and approving are different rights.** The person who writes a case is not the person who approves it; financial-plan approval is frequently a separate permission from case-level approval.
- **Comparability is enforced by structure.** Templates, fixed section structures, and shared scoring criteria exist so that unlike cases can be compared; free-form proposals are the exception, not the rule.
- **The record remembers.** Material changes to a case — re-baselined forecasts, scope changes, condition updates — are visible in the record's history in products that support lookback/audit views.
- **Most proposals do not get approved as submitted.** Rejection, deferral, and rework are first-class outcomes; the pipeline's value comes from disciplined selection, not from approving everything.

## Variants

Common variants of the Type:

- **IT investment / demand-management flavor** — cases originate as ideas or demand requests in an IT portfolio; strong idea→project conversion machinery, fiscal-period time-phasing, technology cost-pool taxonomies.
- **Public-sector / capital appraisal flavor** — formal appraisal standards, and in some products hurdle or threshold rates with pass/fail indicators, location mapping of investments, contract/acquisition planning, or grants; often a dedicated decision platform for agencies and municipalities.
- **Innovation stage-gate flavor** — cases are opportunities moving through front-end-of-innovation workflows and gates; graduation criteria and NPD process modules; benefits framed as growth and revenue streams.
- **Capital program flavor** — CAPEX portfolios with capital stage gates; cases are capital projects within multi-year capital plans.
- **Strategy-execution flavor** — cases/initiatives tightly linked to OKRs, KPIs, and strategy maps; the appraisal is one view inside a broader goal-cascade system.
- **Decision-science-led flavor** — weighted decision models (for example analytic-hierarchy-process-style scoring), consensus measurement, and solver-based optimization of the fundable portfolio.

A variant remains a variant of this Type as long as the defining core — proposal record + financial appraisal + governed decision — is intact. Where a product's center of gravity moves fully to project execution, idea generation, or goal cascading, it becomes a neighboring Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Project Portfolio Management Application | sibling / suite neighbor | PPM's center is executing a portfolio of projects (schedules, resources, delivery); business case management's center is the pre-execution investment decision. Usually sold together; the objects and loops differ. |
| Capital Improvement Planning | adjacent (public sector) | aggregates many investments into multi-year capital plans and budgets; the business case is the per-investment justification feeding that aggregation |
| Financial Modeling Application | adjacent | computes NPV/ROI-style models without a governed record lifecycle, approval, or portfolio context |
| Approval Workflow Platform | adjacent | routes requests for approval but carries no investment-appraisal structure (time-phased costs/benefits, value metrics) |
| Business Process Management Platform | naming-overlap only | BPM "case management" handles operational case instances (requests, incidents); a business case is an investment proposal, not an operational instance |
| Business Continuity Management Platform | namesake trap | continuity plans, impact analysis, exercises — a different domain despite the adjacent directory position and the shared word "business" |
| Idea Management / Product Discovery Platform | upstream neighbor | generates and collects ideas; the seam is financial appraisal + governed approval. Front-end-of-innovation modules bridge the two |
| OKR / Goal Management Platform | upstream neighbor | cascades goals and KPIs; investment proposals are one object inside some strategy-execution systems, not the center |
| Enterprise Request Management | adjacent | intake and fulfillment of requests without appraisal or benefits semantics |

The most important boundary is with Project Portfolio Management: the two share vendors, data, and workflows, but the test is directional. Remove execution management (tasks, schedules, timesheets) and business case management still stands; remove the case, the appraisal, and the approval gate, and what remains is PPM.

## Representative Products

- **Definitive Pro** (Definitive Business Solutions) — decision-centric platform with a dedicated, tab-structured business case module; strong in public-sector capital governance (federal/state/municipal) and commercial portfolios.
- **Planview Portfolios** — enterprise PPM/SPM suite in which business cases are a first-class object within investment prioritization and financial planning.
- **Clarity** (Broadcom) — ITBM/PPM platform whose Ideas workspace captures, develops, and approves initiatives with full financial plans before conversion to projects.
- **Triskell Software** — enterprise PPM with a demand-management hub: capture, score, approve, and convert requests.
- **Wellspring Accolade** (formerly Sopheon) — innovation stage-gate pole: front-end-of-innovation workflows that vet and graduate opportunities into execution, with portfolio and capex management.

Adjacent context examined during research: i-nexus (strategy execution — initiatives linked to goals and savings), which sits between goal management and this Type.

## Sources

Research date: **2026-09-07**

- Definitive Pro — Business Cases (feature page) — https://definitiveinc.com/definitive-pro/business-cases/
- Definitive Pro — product homepage — https://definitiveinc.com/
- Planview Portfolios — product page — https://www.planview.com/products-solutions/products/planview-portfolios/
- Planview Customer Success Center — Planview Portfolios → Outcomes → Business Cases (documentation structure; article bodies require sign-in) — https://success.planview.com/Planview_Portfolios/Outcomes/Business_Cases
- Broadcom TechDocs — Clarity 16.4.2 → Capture, Develop, and Approve New Ideas — https://techdocs.broadcom.com/us/en/ca-enterprise-software/business-management/clarity-project-and-portfolio-management-ppm-on-premise/16-4-2/using/new-user-experience-capture-develop-and-approve-new-ideas.html
- Broadcom TechDocs — Clarity 16.4.2 → Manage Idea Financials — https://techdocs.broadcom.com/us/en/ca-enterprise-software/business-management/clarity-project-and-portfolio-management-ppm-on-premise/16-4-2/using/new-user-experience-capture-develop-and-approve-new-ideas/New-User-Experience--Manage-Financial-Module-in-Idea.html
- Triskell Software — Demand Management — https://triskellsoftware.com/solutions/demand-management/
- Wellspring — Accolade — https://www.wellspring.com/en-us/accolade
- i-nexus — https://www.i-nexus.com/

> Sourcing limitations: Planview's Business Cases help articles are sign-in gated; only the object's documented structure (sub-pages for screen basics, scenarios, publishing, permissions, and a portfolio business case report) is used. ServiceNow SPM and the dedicated benefits-realization vendors Amplify Now and Wovex could not be reached from the research environment; no claims are made for them, and benefits-realization findings rest on the reachable sample. Precise numeric limits, default settings, and vendor-specific state names are intentionally not asserted in this document; they are recorded, where observed, in the paired Research Notes.

Detailed product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
