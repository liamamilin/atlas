# Data Observability Platform

## Overview

A **Data Observability Platform** is the health-watching layer over an organization's data estate: it connects to the data systems a company already runs — warehouses, lakes, transformation tools, pipelines, BI platforms — and continuously evaluates the health of the data assets inside them (freshness, volume, schema, statistical distribution, and defined quality expectations). When something deviates, the platform raises the problem automatically, routes it to the people responsible, and tracks it as a stateful incident until it is resolved.

Its defining core is small:

```text
Connected external data estate
└── Monitored data assets (tables, files, dashboards, pipelines)
    └── Automated health evaluation (learned baselines and/or defined expectations)
        └── Detection
            └── Stateful incident record, worked to resolution
```

The purpose is to invert a familiar failure mode: instead of stakeholders discovering broken dashboards and stale numbers first, the data team is the first to know. The platform is a lens over data it does not own — it extracts metadata, statistics, and check results from source systems; it is not the system of record for the data itself.

## Users & Context

**Primary users** are the people who run the data platform:

- data engineers and analytics engineers — configure monitoring, respond to incidents, fix pipelines
- data platform / analytics leads — own the monitoring strategy, set priorities, review health overviews

**Secondary users**:

- analysts and BI/report owners — check whether an asset is healthy before trusting its numbers; receive incident notifications for data they consume
- data stewards or governance roles — attach ownership and domain structure so incidents reach the right team

The work context is the modern data stack: data lands in a warehouse or lakehouse, is transformed by tools such as SQL-based transformation frameworks, orchestrated by schedulers, and consumed through BI dashboards. Data observability sits alongside this stack rather than inside it, watching the whole chain — which is why the platform must connect outward to many independent systems.

## Core Model

### The connected data estate

The platform's world begins with **connections** to external data systems: cloud warehouses, databases, object storage, transformation frameworks, pipeline orchestrators, and BI tools. Connection is either direct (the platform queries the source with stored credentials) or through a small agent deployed in the customer's network for sources that must not be reached from outside. Across the estate, the platform maintains a registry of **monitored assets** — tables, views, files, dashboard objects, pipeline nodes. These records carry metadata (schema, owner, usage/popularity, tags, lineage position) and, crucially, a health state.

The platform never holds the underlying data. It extracts what it needs to judge health: schemas, row counts, timestamps of last update, column statistics, samples of failing rows, query and job metadata. This read-only posture is structural — it is what allows one product to watch an entire estate of systems it did not build.

### The monitor

The **monitor** (some products say check or rule) is the configured unit of evaluation: an expectation bound to an asset, run on a schedule, producing a tracked value over time. Two families coexist in mature products:

- **Learned evaluation** — the platform collects a statistic over time (row counts, freshness lag, percent of nulls, mean of a numeric column, cardinality of a categorical column), learns its normal range from history, and flags values that fall outside it. Users can usually tune sensitivity and, importantly, mark detections as real or false; the feedback tunes future detection.
- **Defined evaluation** — explicit expectations written as templates (a column must be unique; values must fall in a range; a timestamp must be fresher than its usual gap; two tables must agree) or as free-form SQL. Template libraries cover recurring checks — volume, freshness, schema change, distribution, nulls, uniqueness, value ranges, format conformance, referential integrity.

Both families report the same way: a run either stays within bounds or it does not. A monitor that cannot run at all (bad credentials, unreachable source) is itself reported as a failure — a silent dead monitor would be worse than a failing one.

### The incident

A **detection becomes an incident**: a persistent, stateful record representing a problem with specific assets. Incidents carry a status (conceptually: open → being worked → resolved/closed), one or more assignees, a severity, the affected assets, and a timeline of events — each out-of-bounds run, each status change, each comment. Related detections are consolidated into one incident (by shared root cause, proximity in the lineage graph, or grouping rules), so a single pipeline break that breaks ten downstream tables becomes one work item rather than ten alerts. When the underlying monitors return to normal, the incident closes; in some products it can also be auto-resolved after inactivity so stale entries don't hide new problems.

Notification machinery drives the loop: alerts go to chat channels, email, ticketing systems, and on-call tools, and can @-mention the monitor's owner. The alert is not the end product — the resolved incident and the recorded context (what failed, where, who fixed it, how) are.

### The estate view

Around this loop, the platform exposes the estate itself: a browsable inventory of assets with their health state, owners, usage, schema-change history, and lineage. Health is summarized — per asset, per schema, per team — so both engineers and consumers can answer "is this data trustworthy right now, and has it been stable?" without reading raw monitor output.

```text
Warehouse / lake / BI / pipelines
        │ connections (direct or agent)
        ▼
Monitored assets ── watched by ──▶ Monitors (learned + defined)
        │                              │ scheduled runs
        │                              ▼
        │                          Detections
        │                              │ grouped
        │                              ▼
        └── lineage ───────────▶ Incidents ──▶ Notifications ──▶ Resolution
                                       │
                                       └─▶ Health summaries (scorecards, statuses)
```

### One structure, many implementations

The core model is conceptual; products realize it differently:

```text
Concept:            Monitored asset
Implementations:    warehouse table/view, column, file or table-format object,
                    BI dashboard/report, transformation-framework model (e.g. dbt),
                    pipeline job, ERP-delivered KPI

Concept:            Evaluation unit
Implementations:    auto-thresholded metric, ML-trained anomaly model,
                    static template check, custom SQL rule, ingested pipeline test

Concept:            Detection record
Implementations:    issue + incident two-tier (symptoms merged under a root cause),
                    auto-grouped incident per failing monitor,
                    incident assembled from monitor and pipeline-test failures

Concept:            Alert delivery
Implementations:    Slack/Teams messages, email, Jira/ServiceNow tickets,
                    PagerDuty incidents, webhooks, in-app inbox
```

A reader who has only seen one product should still recognize the others from this table.

## How It Works

### Connect the estate

```text
Register a source connection (credentials or agent)
→ platform discovers schemas/tables/dashboards/pipeline nodes
→ transformation and BI tools attach context (models, tests, dashboards)
→ assets appear in the inventory with initial metadata
```

One warehouse connection is enough to start; transformation and BI integrations deepen lineage and asset context.

### Put assets under watch

```text
Select assets (individually, by schema, by tag, or by lineage)
→ apply monitor templates or enable learned monitors
→ set schedules, thresholds/sensitivity, owners
→ optionally: auto-monitoring suggestions, rollout along lineage,
  monitors-as-code for versioned configuration
```

Critical assets get explicit coverage; broad estates get rule-driven auto-coverage ("monitor every table in these schemas").

### The monitoring loop

```text
Scheduled monitor run
→ platform queries the source (metadata, counts, statistics, custom SQL)
→ value evaluated against learned bounds or defined expectation
→ within bounds: value recorded as history
→ out of bounds: detection raised
```

History is the point of the time series: yesterday's normal defines today's anomaly. Distribution shifts, seasonal patterns, and gradual drift are all judged against accumulated evidence rather than static guesses — though static expectations remain fully supported for known invariants (a key column must be unique, always).

### Work the incident

```text
Detection opens/updates an incident
→ notification routed (chat / ticket / on-call), owner mentioned
→ assign and label
→ investigate: monitor history, failing rows, debug queries,
  lineage impact (what's downstream, which dashboards are affected)
→ fix the upstream cause; monitors return to normal
→ resolve/close with notes; mark detections true/false
→ feedback improves future detection
```

Investigation is where lineage earns its place: the incident view shows what broke, what feeds it, and what depends on it — often expressed as "affected dashboards" so responders understand business impact, not just table impact. Stakeholders are kept informed through the same channels, and the incident timeline becomes the organization's memory of what happened and why.

### Report health to consumers

Data consumers rarely log in to fix anything; they consume trust. Health statuses on assets, scorecards over time, and incident broadcasts tell an analyst whether today's dashboard is fed by healthy data.

## Interfaces

Conceptual surfaces; names and layouts vary by product.

### Incidents list

- **Purpose**: triage everything currently wrong with the estate.
- **Typical information**: status, severity, assignee, affected assets, last failure time, affected-dashboard count.
- **Primary actions**: filter, assign, change status, comment, merge into related incidents, create a linked ticket.

### Incident detail

- **Purpose**: investigate and resolve one problem.
- **Typical information**: incident summary, member monitors with per-monitor status and failure history, lineage graph centered on the failing assets, impacted dashboards, activity feed with comments, notification destinations.
- **Primary actions**: update status/assignee, qualify detections as passing, add comments, open a Jira/ServiceNow ticket, review AI-generated root-cause notes where offered.

### Monitors / monitor editor

- **Purpose**: configure what is watched and how.
- **Typical information**: monitor type, bound asset, schedule, threshold or learned bounds, run history chart, owner.
- **Primary actions**: create from template or custom SQL, adjust sensitivity/thresholds, mute/snooze, run now, tag, apply in bulk via rules or code.

### Asset browser / health view

- **Purpose**: answer "what is this data and is it healthy?"
- **Typical information**: schema and columns, freshness/volume indicators, schema-change history, usage/popularity, owner, tags, current monitor coverage.
- **Primary actions**: search, favorite, set ownership, jump to monitors and incidents, view lineage.

### Lineage view

- **Purpose**: understand relationships and blast radius.
- **Typical information**: upstream/downstream graph around an asset, failing assets highlighted, dashboard consumers.
- **Primary actions**: trace upstream for root cause, expand downstream for impact, jump to affected monitors.

### Health dashboards / scorecards

- **Purpose**: summarize estate health for teams and leadership.
- **Typical information**: health per dimension over time (fresh, complete, schema-stable), open-incident trends, coverage (what is monitored vs not).
- **Primary actions**: filter by team/domain/tag, drill into incidents.

### Administration

- **Purpose**: run the platform itself.
- **Typical information**: connections and their status, teams, roles, notification rules.
- **Primary actions**: manage connections/agents, configure SSO/roles, set alert routing.

## Important Rules / Behaviors

- **The platform reads; it does not own.** Monitoring queries run against source systems; what travels back is metadata, statistics, and check results. This keeps the platform non-invasive but means its accuracy depends on its connections' access and scheduling.
- **Detection is platform-driven.** Checks execute on the platform's schedule, not by a human remembering to test. Schedules, calendars, and quiet windows shape when evaluation happens.
- **Alerts consolidate rather than stream.** While a detection is open, subsequent out-of-bounds runs update the same incident instead of spawning new ones, and related failures are grouped. This anti-fatigue behavior is the reason incident lists stay workable.
- **Feedback changes detection.** Labeling a detection as a real anomaly or a false alarm tunes learned models; products treat this loop as part of operating the system, not an advanced extra.
- **A failed monitor is itself an incident.** Infrastructure problems (expired credentials, unreachable source) surface as monitor failures distinct from data failures, so coverage degrades loudly, not silently.
- **Silenced means silent.** Muted or snoozed monitors do not re-alert until re-enabled or until their incident resolves; products handle staleness with auto-resolve or similar hygiene so long-dead incidents don't mask new ones.
- **Lineage defines blast radius.** Impact statements ("5 downstream tables, 3 dashboards affected") derive from the lineage graph; grouping and suggested merges use the same structure.
- **Ownership routes work.** Assets and monitors carry owners; notifications can @-mention them; severity usually inherits from the triggering checks. Teams, roles, and SSO gate who can see and change what, in keeping with how data organizations are structured.

## Variants

- **Detection philosophy** — ML-first "no-code" platforms that learn everything and ask users for feedback, versus template/rules-first platforms where engineers author explicit expectations, versus hybrids. The split is philosophical, not definitional; mature products support both.
- **Stack breadth** — warehouse-centric products (fast to adopt) versus "full data stack" products that map dependencies from ingestion through transformation to BI, including file storage and operational sources.
- **Catalog depth** — from a light inventory of monitored sources to an embedded governance-grade catalog with glossaries, domains, and data products.
- **Enforcement depth** — most products only watch and alert; some add shift-left previews (impact of a change before it merges) or pipeline enforcement (stopping flows when failures are detected).
- **Deployment posture** — multi-tenant SaaS; self-hosted or customer-VPC deployments for regulated data; native-app installs inside a warehouse; agent-based connections for private networks.
- **Segment** — fast-setup products aimed at small-to-mid data teams versus enterprise products with workspaces, SSO, audit trails, and industry tuning.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Data Quality Platform | the defined rule/test and its pass-fail result is the primary object (rule suites, rule engines); observability centers ambient health of the whole estate plus the incident loop. The two interlock — observability products embed quality rules as one monitor family |
| Data Lineage Platform | describes the structure of data flows (the graph, trace operations, impact-before-change); observability uses that structure but its primary object is runtime health. Lineage supplies the blast radius; observability supplies the failing node |
| Data Catalog | descriptive inventory + discovery loop (what data exists, what it means); observability answers whether it is healthy right now. Catalogs surface quality signals; observability platforms embed light inventories — packaging overlaps, primary objects differ |
| Observability Platform (infrastructure) | collects and inspects software telemetry — logs, metrics, traces of applications and infrastructure — for operations teams. Same word, different world: it watches software, this Type watches data |
| ML Model Monitoring | watches trained models' prediction performance and drift; observability watches the data feeding those models |
| ETL / ELT Platform | moves data and records its own runs; observability watches data health across systems it does not operate. Pipeline-native run monitoring is a partial realization of the observability loop |
| DataOps Platform | automates data-engineering practice (testing, CI/CD, deployment of pipelines); observability watches production health after deployment |
| Data Governance Platform | organizes policy, accountability, and governed processes over the data estate; observability contributes health evidence and consumes ownership/domain structure |

The most consequential seams are with the Data Quality Platform (rules as primary object vs health-plus-incident as primary object) and the Data Catalog (inventory vs health), because vendors increasingly bundle all of these; the primary object of work is the reliable test for whether a product belongs here.

## Representative Products

- Bigeye — metric-first enterprise observability with rules, reconciliation, and incident management
- Metaplane — warehouse-first monitors and incidents with trained anomaly detection and CI/CD impact previews
- Sifflet — full-stack observability with an embedded catalog, monitor template library, and governance structure
- Anomalo — no-code, ML-driven autonomous monitoring aimed at large enterprises

## Sources

Research date: **2026-09-07**

- Bigeye — What is Bigeye?, Metrics, Triaging an Issue, Declaring an Incident, Scorecard, documentation index: https://docs.bigeye.com/docs , https://docs.bigeye.com/docs/metrics , https://docs.bigeye.com/docs/issues , https://docs.bigeye.com/docs/incidents , https://docs.bigeye.com/docs/scorecard
- Metaplane — Welcome, Monitor types, Incidents, documentation index: https://docs.metaplane.dev/docs , https://docs.metaplane.dev/docs/monitor-types , https://docs.metaplane.dev/docs/incidents
- Sifflet — Overview, Incidents, documentation index: https://docs.siffletdata.com/docs , https://docs.siffletdata.com/docs/incidents
- Anomalo — product pages: https://www.anomalo.com/ (operational documentation was not reachable; statements from this vendor are correspondingly general)

> Sourcing limitation: the documentation site of the category's best-known vendor could not be fetched from the research environment (repeated transport failures), so that vendor is absent from this document's evidence; the incident-centric pattern it popularized is nonetheless confirmed independently by three other products. Precise plan-level capabilities, numeric defaults, and vendor-specific module names are intentionally not stated in this document; they remain in the paired Research Notes.

Detailed product-by-product observations, the cross-product comparison matrix, and boundary analysis against neighboring data-platform Types are recorded in the paired Research Notes.
