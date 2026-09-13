# People Analytics Platform

## Overview

A **People Analytics Platform** integrates an organization's workforce data from its various source systems into one governed analytical model, and answers workforce questions — about composition, movement, cost, diversity, and outcomes — through metrics, trends, segments, and insights.

The defining core is small:

```text
Integrated workforce data layer (people records + their history)
└── Governed workforce metrics (consistent definitions)
    └── Analytical question → answer loop
        (filter by segment, trend over time, compare, drill)
```

Everything else commonly associated with the category — prebuilt connector libraries, out-of-the-box dashboards, benchmarks, attrition prediction, AI assistants, self-serve distribution to managers — is widespread in mature products but is not what makes the product a people analytics platform. Older warehouse-era HR analytics deployments and suite-embedded analytics modules also satisfy the core without any of those specifics.

The platform is analytical, not operational: it does not process hires, run payroll, or record performance. It reads the records those systems produce and turns them into workforce understanding. When the primary job shifts to running HR transactions, the product is an HRIS/HCM; when it shifts to forward-looking supply/demand planning, it is drifting toward Workforce Planning.

## Users & Context

**Builders** — people analytics teams and HR analysts. They connect source systems, maintain the data model and metric definitions, monitor data health, and build the analytical content others consume. Their work environment is the platform's modeling, integration, and exploration surfaces.

**Consumers** — CHROs and HR leadership, HR business partners, executives (often jointly with Finance), and line managers. They open the platform to answer questions: How is headcount trending? Where is turnover concentrated and why? Are we hiring to plan? Is pay equitable across groups? They typically consume dashboards, guided insights, or plain-language answers rather than building analyses.

**Data operations** — HRIS administrators and data engineers who own the source systems and the integration pipelines feeding the platform.

Typical occasions of use: monthly and quarterly workforce reviews, attrition investigations, diversity and pay-equity reporting, headcount and cost reviews with Finance, and board-level people reporting.

## Core Model

### The defining core

**Workforce data layer.** The platform's world is built on the organization's people records: identified employees carrying attributes (role, job, location, manager, demographics, compensation), plus the dated events that happen to them — hires, exits, promotions, transfers, pay changes. Records are integrated from one or more source systems (HRIS, payroll, applicant tracking, engagement surveys, performance, finance) into a single model that preserves history. History is essential: workforce questions are almost always asked about a point in time ("how many people did we have in Engineering last June?"), and people's attributes change as they move.

**Governed workforce metrics.** On top of the data layer sit quantified measures — headcount, hires, exits, turnover rate, internal mobility, span of control, compensation measures, and similar. What makes them analytics rather than spreadsheets is governance: each metric has a managed, shared definition, so that HR and Finance (for example) answer "what is our headcount?" with the same number. Mature products expose these definitions as inspectable, versioned objects rather than buried formulas.

**Segments.** Every workforce question is asked about a slice of the organization: by department, location, manager, tenure band, demographic group, or any attribute in the data layer. Segments are first-class — the same metric is computed for the whole company and for any subgroup.

**Time.** Metrics are computed over time: current state, trends across months and years, and comparisons between periods. The platform's ability to reconstruct the workforce "as of" a past date is a direct consequence of the historical data layer.

**Analytical answer surfaces.** The loop closes in surfaces that present answers: dashboards and storyboards, guided insight views organized around workforce questions, and increasingly conversational answers generated from the governed data.

```text
Source systems (HRIS · payroll · ATS · surveys · performance · finance)
        ↓  integrate
Workforce data layer (people records + events + history)
        ↓  compute
Governed metrics  ×  Segments  ×  Time
        ↓  present
Dashboards · guided insights · conversational answers
        → consumed by leaders, HRBPs, managers
```

### Standard capabilities of mature products

These are common across the researched market; they make the platform practical but do not define it:

- **Connector and intake machinery** — prebuilt integrations to major HRIS/payroll/ATS systems, file upload, and APIs for data in; export and API access for data out.
- **Prebuilt content** — libraries of ready-made metrics, questions, and analyses covering common workforce topics (headcount, retention, diversity, hiring, compensation), so customers start from expertise rather than a blank canvas.
- **Data-health tooling** — checks and repair workflows for the data quality the metrics depend on (missing start/end dates, hierarchy gaps, duplicates).
- **Self-serve distribution** — role-scoped dashboards and scheduled delivery so leaders and managers get answers without analyst intervention.
- **Benchmarks** — comparison of the organization's metrics against external or imported reference data.
- **Prediction** — attrition/turnover risk and similar forward-looking indicators computed from the historical layer.
- **AI assistance** — natural-language question answering over the governed data, with access permissions preserved.
- **Governance machinery** — audit logs, definition catalogs, and version control over the analytical model.

### One structure, many implementations

The core is written conceptually; products realize it differently:

```text
Concept:  Workforce data layer
Realized as:  proprietary analytic model with subjects and events ·
              governed data model over a warehouse/data-mesh architecture ·
              analytics layer inside an HCM suite over the suite's own data

Concept:  Governed metrics
Realized as:  documented metric libraries with formula languages ·
              shared definition catalogs co-owned by HR and Finance ·
              vendor-defined calculations with stated rules

Concept:  Answer surfaces
Realized as:  dashboards and storyboards · guided insight views per topic ·
              conversational AI answers
```

## How It Works

### 1. Connect and integrate

The platform is pointed at the organization's source systems. Employee records and events flow in through connectors, file uploads, or APIs, and are reconciled into the workforce data layer — identities matched across systems, attributes aligned, history preserved. Because organizational structures change constantly, the integration layer is built to keep answering point-in-time questions correctly as records change.

### 2. Model and define

Builders maintain the analytical model: which subjects exist (employees, and often candidates), which attributes and events they carry, and which metrics are computed from them. Metric definitions are configured and versioned here. Data-health tooling surfaces gaps — a missing termination date makes turnover uncomputable — before they silently distort results.

### 3. Analyze

The characteristic loop of the Type:

```text
Pick a workforce question (e.g., "why is turnover rising in Sales?")
→ scope it to a segment (Sales, or a subgroup)
→ read the metric over time (trend, comparison to other groups or benchmarks)
→ drill into contributing factors (engagement scores, tenure mix, manager, location)
→ arrive at an insight, and share it with the accountable leader
```

The same loop runs in different depths: a leader reads a prepared dashboard; an analyst drills interactively; a manager asks a conversational question. The platform's job is that all three draw on the same governed numbers.

### 4. Distribute

Insights reach consumers through shared dashboards, scheduled reports, embedded views, and conversational assistants. Distribution is role-scoped: each consumer sees the workforce through the lens of their own organization and permissions.

### 5. Govern

Because the data is people data, governance runs continuously: access follows the org chart as people move, sensitive attributes are protected at row and column level in the most mature products, and usage is auditable.

### Capability tiers

**Defining core** — without these, not a people analytics platform:

- integrated workforce data layer with history
- governed workforce metrics
- analytical question → answer loop over segments and time

**Standard in mature products:**

- connectors, prebuilt content, data-health tooling
- self-serve distribution, benchmarks, prediction, AI assistance
- access control and audit

**Optional / variant:**

- forward-looking planning modules (forecasting, headcount planning)
- embedded analytics offered to other software vendors
- proprietary benchmark datasets
- real-time data delivery (others refresh on schedules)

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Dashboards / storyboards

The primary consumption surface.

- Purpose: present governed metrics for a topic or audience.
- Typical information: headline metrics with trends, segment breakdowns, comparisons to prior periods or benchmarks.
- Primary actions: filter to a segment, change the period, drill into a metric, share or export.

### Guided insight views

Topic-centered pages organized around a workforce question (retention, diversity, hiring) rather than around charts.

- Purpose: walk a non-analyst from a headline number to its explanation.
- Typical information: the metric, its notable movements, statistically notable groups, contributing factors.
- Primary actions: inspect a highlighted group, add it as a filter, share the finding with the responsible leader.

### Data explorer / query

The analyst's surface.

- Purpose: free exploration beyond prepared content.
- Typical information: selectable metrics, segments, and time ranges from the data layer.
- Primary actions: compose a query or visual, refine iteratively, save as a new view.

### Conversational assistant

Increasingly common.

- Purpose: answer workforce questions in plain language, drawing only on the governed data.
- Primary actions: ask a question, refine it, receive an answer with links back to the underlying data.

### Integration and data-health administration

- Purpose: manage source connections, mappings, and data quality.
- Typical information: connection status, import history, quality issues.
- Primary actions: connect or re-authenticate a source, repair data, schedule refreshes.

### Security administration

- Purpose: control who sees which data and content.
- Typical information: roles and their access, sensitive-attribute protections, audit logs.
- Primary actions: grant or adjust access, review who saw what.

## Important Rules / Behaviors

### Access control is structural, not an add-on

People data is among the most sensitive data an organization holds. Access control in this Type is therefore part of the product's structure: permissions are defined over the data, over analytical content, and over consumption channels. In the most developed implementations, permissions reach row and column level, and access is dynamic — it updates automatically as people move, so a manager's view follows their current team, and compensation or performance data stays protected even as self-serve access expands.

### Metric definitions are governed

The platform's authority rests on one version of the numbers. Definitions of metrics like headcount or turnover are managed objects: changing one is a deliberate, versioned act, not a hidden edit. This is what lets HR and Finance share the same answer.

### Point-in-time semantics

Workforce questions are asked about moments in time. The platform preserves history so that today's report and last year's report both remain answerable, and reorganizations do not silently rewrite the past. Some products compute figures only as of a completed period; others deliver continuously updating data — the cadence varies, the point-in-time requirement does not.

### Data quality gates the answers

Analytics is only as good as the underlying records. Missing or wrong employment dates make turnover uncomputable; hierarchy gaps break manager-level views. Mature products expose data-health tooling and, in some cases, withhold or flag metrics whose inputs are incomplete rather than present misleading numbers.

### Small groups are statistically protected

Workforce analysis routinely slices into small groups, where individuals become identifiable and random variation dominates. Products commonly apply safeguards: minimum group sizes before group-level results are shown, statistical tests before a group is flagged as unusual, and confidentiality protections inherited from survey data. Exact thresholds are product-specific and configurable.

### The platform reads; it does not transact

The platform does not change employment records, approve anything, or execute HR processes. Its outputs are understanding — and, in some products, hand-offs toward planning or action in adjacent systems.

## Variants

- **Standalone pure-play platform** — an independent product whose whole job is people analytics over integrated sources; typically insight-led with prebuilt content and benchmarks.
- **Data-first platform** — leads with the governed data foundation (warehouse- or mesh-style architecture) and treats dashboards, stories, and AI as layers on top; often positions metric governance between HR and Finance as the core value.
- **Suite-embedded analytics** — an analytics module inside an HCM suite, analyzing the suite's own records (sometimes plus external sources); strongest where the suite is the single system of record.
- **Engagement-suite extension** — a survey/engagement vendor adding workforce analytics (typically turnover and its drivers) by combining synced HRIS data with its native survey data.
- **Org-platform layer** — a people-operations platform built around a living model of the organization, where analytics is one surface beside org charts, headcount planning, and compensation.
- **Embedded analytics** — the platform's analytical capability packaged for other software vendors to embed in their own products.

A variant remains a variant while the defining core holds. Where a variant's primary job changes — running HR transactions (HRIS), planning future workforce state (Workforce Planning), or authoring structure scenarios (Organization Design) — it becomes a different Application Type that bundles this one.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| HRIS / HCM | system of record; frequent source | operates HR transactions and holds the records; its native reporting reports on its own records, while people analytics integrates multiple sources into an analytical model with governed definitions |
| Business Intelligence Platform | adjacent, domain-generic | BI answers questions over any data domain; people analytics carries built-in workforce semantics (employee subjects, org hierarchy, tenure), HR metric definitions, people-data access rules, and HR benchmarks |
| Employee Engagement Platform | adjacent; frequent data source | engagement centers the survey measurement loop (programs, confidentiality, action); people analytics centers the integrated data layer — engagement scores are one input to it |
| Employee Survey Platform | capability relationship | survey platforms collect questionnaire responses for any audience; people analytics consumes results as one source among several |
| Workforce Planning Platform | forward-looking sibling | planning models future demand/supply, positions, and scenarios over a horizon; people analytics measures what is and has been; vendors commonly bundle both |
| Organization Design Platform | structure-focused sibling | org design authors and compares structure scenarios (units, positions, reporting lines); people analytics measures the workforce; both may share the same underlying org model |
| Employee Experience Platform | umbrella neighbor | experience platforms consolidate workforce-experience domains (communication, listening, service); people analytics is the measurement layer that some of them bundle |

The boundary with HRIS reporting is the most consequential one, because suite-embedded analytics modules carry the same name. The structural test is data scope and purpose: operational reporting on one system's records versus cross-system analytical modeling with governed definitions. The boundary with generic BI is drawn by domain: remove the workforce semantics, HR metric definitions, and people-data access rules, and only a BI platform remains.

## Representative Products

- **Visier** — standalone pure-play people analytics; documented analytic model (employee subjects, events, dimensions, metrics) with prebuilt content, benchmarks, and AI assistance.
- **One Model** — standalone data-first platform; governed HR data model over multi-source data with storyboards and AI assistance.
- **Culture Amp (People Analytics / Retention Insights)** — engagement-suite extension; turnover analytics combining synced HRIS employee data with native survey data.
- **ChartHop (Analytics)** — org-platform layer; analytics over a living model of the organization beside headcount planning and HR operations.

Suite-embedded analytics modules inside HCM suites (marketed under the same "people analytics" name by major HCM vendors) are a common packaging of the same Type; their internals were not verified from official documentation in this research pass and are therefore not characterized further here.

## Sources

Research date: **2026-09-06**

- Visier — Understand Visier's Analytic Model (documentation): https://docs.visier.com/developer/Analytic%20Model/analytic-model-overview.htm
- Visier — Platform: https://www.visier.com/platform/
- Visier — Security & Governance: https://www.visier.com/platform/security-model/
- Visier — Visier People: https://www.visier.com/products/visier-people/
- One Model — homepage: https://www.onemodel.co/
- One Model — Data Mesh: https://www.onemodel.co/products/data-mesh
- Culture Amp — People Analytics (support collection): https://support.cultureamp.com/en/collections/8949633-people-analytics
- Culture Amp — Retention Insights (support article): https://support.cultureamp.com/en/articles/7916907-retention-insights
- ChartHop — homepage (including product FAQ): https://www.charthop.com/
- ChartHop — Help Center: https://docs.charthop.com/

> Sourcing limitation: official operational documentation for suite-embedded people analytics (SAP SuccessFactors People Analytics; Workday) could not be reached from the research environment on 2026-09-06 (JS-rendered help portals; product-page 404s), and One Model / ChartHop evidence is product-page level rather than help-center level. Claims about those products are kept at positioning level only; precise operational details (thresholds, refresh intervals, state names) are stated only where directly documented, and product-specific examples are marked as such. Detailed evidence, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
