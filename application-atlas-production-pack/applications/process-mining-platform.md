# Process Mining Platform

## Overview

A **Process Mining Platform** is an analysis platform that reconstructs how an organization's business processes *actually* run, by extracting the event data that operational IT systems record as people and systems execute work — and deriving the process structure from that data rather than from interviews or hand-drawn diagrams.

The defining core is small:

```text
Event log from operational systems
└── Automated discovery of the actual process from those events
    └── Case- and variant-level analysis of frequency and time
```

Around this core, mature products add a governed data pipeline, conformance checking against designed process models, root cause analysis, dashboards for business users, and an action loop that turns findings into alerts, automation triggers, or tracked improvement opportunities.

The platform is observational by nature: it watches executed work through event data and quantifies the gap between designed intent and actual behavior. It does not itself execute the process (that is a BPM system's role), it does not perform the automation it may recommend (that is an RPA platform's role), and its unit of analysis is not generic aggregated data (that is BI's role) but the ordered event history of individual process instances.

## Users & Context

**Primary users:**

- **Process analysts / operational excellence teams** — configure the data pipeline, shape the event log, build and maintain process analyses, investigate bottlenecks and deviations. They are the platform's power users.
- **Business users / process owners** — consume published dashboards ("process apps") to monitor their process: KPIs, trends, deviations. They drill down, filter, and in some products trigger follow-up actions directly from the dashboard.

**Secondary users:**

- **Internal audit / compliance teams** — test whether actual executions follow required controls (e.g. approval sequences, segregation-of-duties constraints, service-level agreements).
- **Transformation / automation program teams** — use discovered facts to prioritize improvement and automation investments, and to measure whether changes produced the intended effect.

Typical context: medium and large organizations running established transactional systems (ERP, CRM, ITSM, workflow, order management) where processes span departments and systems, so that no single person can see how the end-to-end process really behaves. Common process domains include purchase-to-pay, order-to-cash, production, service management, and claims handling. Work is typically organized as an ongoing program: an analyst establishes an analysis for a process, business users monitor it continuously, and findings feed improvement or automation initiatives.

## Core Model

### The Event Log

The substrate of everything is the **event log**: transactional records extracted from the source systems, where each record is an **event** — a step that actually happened. An event carries, at minimum:

- a **case identifier** — which process instance the step belongs to (one purchase order, one customer order, one insurance claim, one service ticket);
- an **activity** — what was done (created, approved, changed, shipped, invoiced...);
- a **timestamp** — when it happened.

Events commonly also carry **resources** (who or what performed the step), **costs**, and other business attributes. The log is not a fixed format the analyst types into; it is assembled by mapping whatever the source systems record onto these semantics. That mapping is a deliberate analytical act — deciding what counts as a case and what counts as an activity largely determines what every later analysis can show.

### Case

A **case** is one instance of the process running through its lifecycle: the ordered sequence of events sharing one case identifier. It is the platform's unit of analysis. Cases may be complete (the process finished) or in flight (still executing).

### Variant

A **variant** is a distinct path that cases take through the process. Real processes never run one way; the same process typically has a handful of dominant variants and a long tail of exceptional ones. Comparing variants — which are frequent, which are slow, which violate rules — is one of the platform's signature analyses.

### Discovered Process Model

From the event log the platform derives a **process model** — usually visualized as a process graph or process map showing activities as nodes and observed transitions as edges, annotated with frequencies and durations. This model is *mined*, not drawn: it changes when reality changes. Some products also express the discovered structure in a standard modeling notation (e.g. BPMN), and allow switching between simplified maps and richer models.

### Designed Model

Many organizations also bring a **designed process model** — the to-be process as documented in a modeling tool or repository. The designed model is the reference against which actual behavior is compared (see conformance below). Unlike the discovered model, it represents intent, not observation.

### Measures and KPIs

All measures are computed from the same event data:

- **Frequencies** — how often an activity occurs, how many cases follow a variant, how often a step is repeated (rework).
- **Durations** — how long the whole case takes (throughput time), how long an activity itself takes (cycle/processing time), and how long is spent waiting between steps. The distinction between processing time and waiting time is standard and matters: bottlenecks usually hide in waiting, not working.

KPIs are tracked against configurable **thresholds** that define acceptable versus problematic performance.

### Analysis Artifacts and Actions

The platform's outputs are persistent, governed artifacts:

- **Process apps / dashboards** — curated views combining a process graph, KPI panels, and charts, configured by an analyst and consumed by business users.
- **Findings** — deviations, bottlenecks, root causes, non-compliant cases.
- **Actions** — alerts or triggered follow-ups (including, in some products, launching an automation on a flagged case) and tracked improvement opportunities.

```text
Source systems (ERP / CRM / ITSM / workflow / logs)
        ↓  extract, transform, enrich
Event log (case · activity · timestamp · resource · attributes)
        ↓  automated discovery
Actual process model  +  variants
        ↓  annotate & compare
Measures · KPIs · conformance vs designed model · root causes
        ↓  publish
Process apps / dashboards for business users
        ↓  act
Alerts · automation triggers · improvement opportunities
```

## How It Works

A process mining engagement follows a recurring loop. The first pass establishes the analysis; every later pass refreshes it with new data.

### 1. Connect and extract

The platform connects to source systems — enterprise suites, databases, data warehouses, or file exports — through connectors or extract-transform-load pipelines. Ingestion is commonly scheduled (for example weekly or monthly); some products also support more continuous refresh. A single analysis usually draws from one or a few systems that jointly record the process.

### 2. Transform and enrich

Raw extracts rarely form a clean event log, so the analyst works in a data preparation layer: cleaning records, joining related tables, and — critically — mapping columns to the case / activity / timestamp semantics. Business logic is added at this stage: rules that reflect how the organization defines its process (which steps count as the same activity, which attributes matter, what the happy path should be). This is where the platform incorporates organizational knowledge, and it is the step where analysis quality is decided.

### 3. Discover the actual process

The platform computes the process structure from the transformed log: the activities that really occur, the order in which they occur, the loops, rework paths, and handovers between people and systems. The result is presented as a process graph or map, sized or colored by frequency and time. The analyst can usually simplify the view (hide noise, focus on the dominant variants) and switch perspectives (for example, analyze by performer or role instead of by activity).

### 4. Analyze

With the actual process on screen, the recurring analytical moves are:

- **Performance analysis** — where time goes: total case duration, activity durations, and waiting times between activities; comparison against thresholds and targets.
- **Variant analysis** — which paths exist, how often each is taken, and how they differ in outcome and duration.
- **Conformance checking** — replaying actual cases against the designed model to find deviations: steps skipped, steps done out of order, forbidden sequences, missing approvals. Some products formulate the expected behavior as explicit rules (order constraints, time limits, resource constraints) and test every case against them.
- **Root cause analysis** — statistically relating case attributes (supplier, region, team, document type...) to slow or non-compliant outcomes, and comparing compliant against non-compliant cases.
- **Drill-down** — moving from the aggregate model to a specific case's event history to understand exactly what happened.

### 5. Publish and monitor

The analyst packages the analysis as a process app: dashboards with KPI panels, the process graph, charts, and saved filters. Business users open the app, filter to their area of interest, and monitor how the process performs as fresh data is loaded. Views are shareable; changes in KPIs against thresholds surface problems without anyone having to re-run an investigation.

### 6. Act and track

Findings turn into work: flagged cases can raise alerts or — where the platform integrates with an automation environment — trigger a follow-up automation or task for the specific case. Improvement opportunities and the value realized from them can be tracked in the platform so the program's impact stays measurable. After a change is implemented, the same analysis shows whether the process actually moved.

### Advanced extensions

Products extend the loop with some of the following, depending on their strategy:

- **Simulation / what-if** — building a simulation model of the process (in some products discovered automatically from the log) and testing the impact of changes — added resources, removed steps, different arrival rates — before committing to them.
- **Predictive monitoring** — machine-learned predictions on running cases, such as expected remaining time, next activity, likely outcome, or risk of breaching a service level. Offered by some products.
- **Task mining** — capturing user-level interaction with desktop applications to see the manual work inside process steps that system logs do not record. Some platforms offer this as a companion capability or separate product.
- **Conversational AI assistance** — asking questions about the process in natural language instead of building every view by hand. An emerging addition, not present everywhere.

## Interfaces

### Data pipeline workspace *(analyst side)*

- **Purpose:** turn source-system extracts into a well-formed event log.
- **Typical information:** source connections, extraction schedules, transformation steps, column-to-semantics mappings, data quality indicators.
- **Primary actions:** configure connectors, define transformations and business logic, run or schedule data refresh, validate the result.

### Process discovery / explorer view

- **Purpose:** show the discovered actual process.
- **Typical information:** activities as nodes, transitions as edges, frequency and duration annotations, variant summary, simplification controls.
- **Primary actions:** zoom/simplify, switch metric or perspective, open a variant, drill into cases.

### Conformance / comparison views

- **Purpose:** confront actual behavior with the designed model or explicit rules.
- **Typical information:** deviations by type and frequency, non-compliant case lists, model-to-model differences where a designed model is maintained.
- **Primary actions:** configure rules or select a reference model, quantify deviation impact, filter to non-compliant cases.

### Process app / dashboards *(business-user side)*

- **Purpose:** governed, continuously refreshed monitoring of one process.
- **Typical information:** a KPI bar (current values against previous period and thresholds), the process graph, supporting charts (distributions, trends, top variants or attributes).
- **Primary actions:** filter and select data (selections usually propagate across charts), drill down to case details, share the current view, and — where available — trigger an action or automation on selected cases.

### Case detail view

- **Purpose:** the lowest level of analysis — the full event history of one process instance.
- **Typical information:** ordered events with timestamps, performers, durations between events, attribute values.
- **Primary actions:** inspect the timeline, launch a follow-up action on the case.

### Modeling and simulation workspace *(where offered)*

- **Purpose:** author or import designed process models; maintain a simulation model.
- **Typical information:** model diagrams, model repository, simulation parameters, scenario results.
- **Primary actions:** create/edit/share models, run what-if scenarios, compare scenarios.

## Important Rules / Behaviors

### The analysis is only as true as the log

Every insight is bounded by the analyst's mapping decisions: what constitutes a case, which events were captured, and how activities were normalized. Two differently configured analyses of the same process can legitimately show different pictures. Configuration is therefore a substantive, governed activity — not a setup detail.

### Actual and designed processes diverge by default

A central, recurring finding of process mining is that real behavior differs from documentation. The platform's job is to expose the divergence precisely (which variant, how often, what it costs), not to prevent it. Deviations are evidence for human decisions, not automatic faults.

### Observational, not transactional

The platform does not create or advance process instances; it reads the trail other systems leave. Consequences: the analysis can never be fresher or more complete than the source systems' recording; and steps performed outside recorded systems (offline work, informal approvals) are invisible unless separately captured (for example via task mining or manual event data).

### In-flight cases are partial

Cases still executing show only their events so far. Duration measures for in-flight cases are incomplete by construction, so analyses typically distinguish completed from running cases.

### Analyst and business user are deliberately separated

Data pipeline configuration and app building require skilled roles; consumption is designed for domain experts with no technical background. Published apps are governed artifacts: what a business user sees is shaped by the analyst's configuration, and sensitive fields can be restricted from view by data policies in some products.

### Measures have precise definitions

Time measures are defined on the event data — for example, the time between the end of one event and the end of the previous one versus the time actually spent inside one event — and these definitions (processing vs waiting time) determine whether a bottleneck is visible. Thresholds that separate acceptable from problematic performance are organization-defined, not built into the platform.

### The action loop stays accountable

Where the platform triggers automations or tasks from flagged cases, the trigger conditions are configured by the analyst and evaluated against the case data, and the resulting actions run in external automation systems. The platform records what was flagged and what was triggered, keeping the observation→action chain traceable.

## Variants

- **Pure-play process intelligence platforms** — the mining core surrounded by a broad analysis/action platform (data extraction at scale, app building, opportunity tracking, automation orchestration). Typically sold to large enterprises as a transformation capability.
- **Automation-suite modules** — process mining embedded in an RPA/automation platform, where the distinguishing emphasis is the direct path from discovered inefficiency to triggered automation.
- **ERP-suite modules** — mining embedded in an enterprise software vendor's stack, emphasizing pre-integration with that vendor's systems and process templates.
- **Model-centric / research-origin platforms** — emphasize standards-based process models (BPMN), model repositories, conformance, and simulation alongside mining; historically rooted in the academic process mining community.
- **By deployment** — cloud SaaS, self-hosted enterprise suites, standalone installations, and (in some lineages) open-source cores.
- **By process domain** — horizontal platforms versus prebuilt applications/templates for specific domains (purchase-to-pay, order-to-cash, service management...), where the event-log mapping and KPIs arrive preconfigured.
- **By program posture** — one-off diagnostic studies (often with consultants) versus continuously monitored production analyses embedded in operations.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Business Process Management Platform | adjacent / converging | BPM *designs and executes* process definitions — the model drives the work. Mining *derives* models from already-executed work. Suites increasingly bundle both, but the cores are model-driven execution vs event-driven observation. |
| Task Mining Platform | sibling / complementary | Task mining captures user-level desktop interactions to reconstruct tasks inside process steps; process mining reconstructs the business process from system-level event logs. Task mining explains what happens *inside* a mined step. |
| Robotic Process Automation Platform | adjacent | RPA *performs* automation of rule-based work; process mining *identifies* where automation pays off and (in some products) triggers RPA workflows on flagged cases. Observation vs execution. |
| Business Intelligence Platform | adjacent | BI aggregates data into reports and dashboards; process mining's unit of analysis is the ordered event history of a case, and its distinctive output is derived process structure (flows, loops, handovers, variants) that generic aggregation does not produce. |
| Application Performance Monitoring / Observability | different layer | APM observes the health of software systems (latency, errors); process mining observes the behavior of business processes (flows, rework, throughput of cases). Different substrate, different questions. |
| Enterprise Resource Planning / transactional systems | data source | Operational systems are where the event data comes from; they run the business, the mining platform explains how the running actually proceeds. |

## Representative Products

- **Celonis** — pure-play market-leading process intelligence platform
- **SAP Signavio (Process Mining)** — process mining embedded in an enterprise software suite
- **UiPath Process Mining** — process mining as part of an automation platform
- **Apromore** — research-origin, model-centric full-spectrum process intelligence platform

## Sources

Research date: **2026-09-06**

- UiPath — Process Mining user guide: Introduction to Process Mining; Working with dashboards and charts; Setting up Automation integration — https://docs.uipath.com/process-mining/
- Celonis — Platform and Analyze Processes product pages — https://www.celonis.com/platform/ , https://www.celonis.com/platform/analyze-processes/
- Apromore — Home and Key Features product pages — https://apromore.com/ , https://apromore.com/key-features/
- Wikipedia — "Process mining" (definitional grounding: event log, discovery/conformance/enhancement, category history) — https://en.wikipedia.org/wiki/Process_mining

> Sourcing limitation: Celonis technical documentation is access-restricted (authentication-gated), and SAP Signavio documentation could not be retrieved during research. Claims about those vendors are therefore kept at the level of product positioning and named capabilities from official product pages; no operational details are asserted for them. Where a capability is documented for only a subset of the researched products, the document says "some products" or "commonly" rather than generalizing.
