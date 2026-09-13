# Data Quality Platform

## Overview

A **Data Quality Platform** is software that defines, executes, and manages **quality rules against an organization's data** — recorded checks that state what the data should satisfy (complete, valid, unique, consistent, accurate, fresh) — and turns every execution into **recorded pass/fail results** that teams review, communicate, and act on.

The problem it solves: data in warehouses, databases, files, and business applications silently degrades — values go missing, formats drift, duplicates appear, pipelines load partial data — and the people downstream of that data discover the damage only when a report or model breaks. A data quality platform makes the expectations about data **explicit and testable**, evaluates them **continuously and at scale**, and keeps the **evidence** (what failed, when, which records) so problems can be triaged and fixed.

The defining core is deliberately small:

```text
Defined quality rules (the primary object)
└── executed against the organization's data
    └── producing recorded pass/fail results
        └── attributed to data and rule, retained as history
```

Everything else commonly associated with the category — quality-dimension taxonomies, profiling, scorecards, alerting, incident tracking, remediation, machine-learning anomaly detection — is standard capability that mature products add, not what makes the product a data quality platform. The platform evaluates data; it is **not the system of record** for that data. When a product starts owning and mastering the data itself, it has drifted toward Master Data Management; when its center shifts from authored rules to ambient anomaly watching, it has drifted toward Data Observability.

## Users & Context

Primary users are the people responsible for making data trustworthy:

- **Data engineers** author rules alongside the pipelines that produce the data, wire checks into orchestration and CI/CD, and fix what the rules catch.
- **Data stewards / data quality analysts** define quality requirements in business terms, organize rules by subject area, review recurring results, and drive issues to resolution.
- **Analytics engineers and BI developers** validate the tables their dashboards depend on before consumers are affected.

Secondary users:

- **Data owners / business domain experts** — declare what "good data" means for their domain (often through no-code authoring surfaces or contracts) and consume the resulting quality scores.
- **Governance and compliance teams** — consume quality evidence as part of data governance programs and audits.
- **Platform administrators** — manage connections, roles, notifications, and deployment.

The work environment is the organization's data estate: warehouses, lakehouses, operational databases, object storage, and business applications. The platform is a **custodian layer over data it does not own** — it connects to these systems (or stages working copies for processing), evaluates the data there, and reports back. Typical contexts: analytics teams protecting reporting reliability; data teams operating pipelines; regulated or governance-mature organizations needing demonstrable quality evidence; migration and integration programs comparing source and target data.

## Core Model

### The Defining Core

**The quality rule.** The central object is a named, reusable, governed condition that states what the data should satisfy — an expectation, check, or rule. A rule targets something specific (a table, a column, a group of datasets, a business term applied to data) and expresses a testable condition: values must be non-null, must match a format, must be unique, must fall in a range, must reference valid values elsewhere, must arrive on time, must match a source count. Rules are defined once, kept, versioned, and reused — the rule library, not any single run, is what the product centers on. Without the rule as a managed object, the product is just ad-hoc test code.

**The data under evaluation.** Rules are executed against the organization's actual data. The platform connects to data systems it does not own — or stages working copies of the data for processing — and evaluates the data where it lives. The authoritative data stays in the organization's systems; the platform holds rules, results, and metadata, not the data of record. This custodian posture is what separates the Type from platforms that master data.

**The evaluation run.** An execution event that applies a set of rules to a defined scope of data — triggered manually, on a schedule, by an orchestrator, inside a pipeline, or continuously. Runs are first-class: they can be configured, scheduled, retried, and audited.

**The result record.** Every evaluation produces durable results attributed to the data and rules involved: which dataset, which rule, passed or failed (or a measured value against a threshold), when, and — critically — **which records failed**. Results accumulate into history, making quality comparable over time and drillable from a summary score down to individual failing rows.

```text
Data system (owned by the organization)
   ↓ connected / staged
Dataset or column under evaluation
   ↓ evaluated by
Quality rule(s)          ← the rule library
   ↓ during
Evaluation run
   ↓ produces
Result record (pass/fail, score, failed records)
   ↓ accumulates into
History · scores · reports
```

### Standard Capabilities

Mature products commonly add the following around that spine. They make the platform practical; they do not define it.

- **Quality dimensions** — an organizing vocabulary that classifies rules and results by what they test: completeness, validity, uniqueness, accuracy, consistency, timeliness, and similar. Products differ in shape: some expose dimensions as configurable objects with named pass/fail outcomes that roll up into an overall quality percentage; others express the same idea as families of metric checks or categories in an expectation library. The dimension *concept* is common; any fixed taxonomy is not.
- **Profiling** — computing dataset and column statistics (distributions, null rates, value patterns, uniqueness) to understand data before writing rules, and often to suggest rules from observed patterns.
- **Scorecards, dashboards, and reports** — aggregated views of quality per dataset, domain, or the whole estate, with per-dimension breakdowns and trends, published to stewards and management.
- **Failed-record drill-down** — samples of the actual failing rows attached to results, so a failure can be diagnosed without leaving the platform.
- **Scheduling and orchestration** — managed execution (hosted runners, monitoring projects, scheduled scans) plus integration with pipeline orchestrators so checks run as part of data production.
- **Alerting and notifications** — failed results routed to chat channels, ticketing systems, or webhooks where teams already work.
- **Issue / incident tracking** — confirmed failures become tracked records with an owner, status, severity, and resolution outcome, linked to the check results that triggered them.
- **Reusable standards** — rule templates and shared rule sets applied across many datasets at once, so common requirements (e.g., "every table's primary key is unique") are written once.
- **Catalog and glossary integration** — quality results surfaced on catalog entries; rules attached to business terms so they apply wherever the term appears.
- **Roles, permissions, and audit** — who can author rules, run evaluations, manage issues, and view which data; audit trails of changes and access.
- **Programmatic control** — APIs, CLIs, and configuration-as-code for defining rules and running evaluations outside the UI.

### One Structure, Many Implementations

The core model is conceptual; products realize each piece differently:

```text
Concept:  Quality rule
Forms:    code-defined checks in a DSL or Python · visual rule builders ·
          pattern/indicator libraries · rules attached to business terms

Concept:  Data under evaluation
Forms:    direct queries against warehouses/databases · staged processing copies ·
          pushdown into the warehouse engine · in-memory frames in CI

Concept:  Result record
Forms:    check results with failed-row samples · validation documents ·
          quality percentages per record set · analysis reports with history
```

## How It Works

The operational loop has five recurring phases. Products differ in emphasis, but the loop itself is the Type's signature.

### 1. Connect and register targets

The team connects the platform to data systems (warehouses, databases, lakes, applications) and registers the datasets — or whole schemas/sources — that will be under quality management. Connections carry credentials and scope; registered targets become the addressable units for rules and results.

### 2. Understand the data (commonly via profiling)

Before rules are written, teams typically profile the data: distributions, null rates, formats, cardinality. Profiling turns "we think emails look like X" into evidence, and in several products profiling results can be converted directly into draft rules.

### 3. Define rules

The team authors expectations and attaches them to targets:

```text
Choose target (dataset / column / term / dataset group)
→ state the condition (non-null · format · uniqueness · range ·
   reference-validity · freshness · custom expression/SQL)
→ classify it (dimension / metric family / expectation type)
→ set thresholds and severity
→ save to the rule library (versioned, often review-governed)
```

Authoring style is a philosophy axis: developer-first products define rules as code (a domain-specific checks language or a Python API) that lives in version control; steward-oriented products offer visual builders and no-code editors; most mature products support both.

### 4. Execute evaluations

Rules run against the data:

- **on demand** (ad-hoc validation during development or investigation),
- **on schedule** (managed runners or monitoring projects re-evaluating critical data),
- **in-pipeline** (orchestrated as a step in data production, or embedded as components inside transformation jobs, or evaluated inside the warehouse itself),
- **in CI/CD** (validating data or rule changes before deployment).

Execution may query the source directly, push evaluation down into the warehouse engine, or stage data into a processing environment — the platform's posture, not the user's concern.

### 5. Review results and respond

Results land in the platform's review surfaces: scores and pass/fail states per dataset and dimension, trends over time, and drill-down into the failing records. From there the loop closes:

```text
Failure observed
→ alert routed (chat / ticketing / webhook)
→ confirmed as an issue or incident (owner, status, severity)
→ investigated via failed-record samples and history
→ fixed at source (or remediated/cleansed where the product supports it)
→ re-evaluated; result history records the recovery
```

Some organizations stop at watching and alerting; others enforce — failing a pipeline stage, blocking deployment, or gating warehouse writes when quality rules fail. Enforcement depth is a configuration choice, not a Type boundary.

## Interfaces

The surfaces below are described conceptually; names and layouts vary by product.

### Rule authoring surface

Where expectations are created and maintained.

- code editor or visual builder; rule list organized by target, dimension, or domain
- typical information: rule name, condition, target, threshold, dimension, owner, version
- primary actions: create/edit/disable a rule, attach to targets, apply a template or standard, version/publish

### Results and dashboards

The review surface for quality state.

- quality scores per dataset/domain with per-dimension breakdowns; pass/fail states per check; trends over time
- typical information: dataset, rule, result, timestamp, failed-record count, history
- primary actions: filter and sort results, drill into a failing check, open failed-record samples, create an issue, mute or adjust a rule

### Failed-record explorer

The diagnostic surface attached to results.

- samples of the rows that failed each rule, with the failing values visible
- primary actions: inspect samples, export them, route them to remediation

### Issue / incident view

Where confirmed problems are worked.

- tracked issues with owner, status, severity, linked check results, resolution notes
- primary actions: create from a failed check, assign, update status, resolve with a documented outcome

### Profiling explorer

Statistics about registered data.

- column distributions, null rates, patterns, uniqueness; often the entry point for drafting rules
- primary actions: run profiling, inspect statistics, create a rule from a finding

### Administration

Connections, credentials, schedules, notification rules, roles, audit trails, deployment settings.

## Important Rules / Behaviors

- **The platform evaluates; it does not own.** The data of record stays in the organization's systems. Results, rules, and metadata live in the platform; corrections, where supported, are written back or staged — the platform does not become the master copy.
- **A rule failure is evidence, not auto-correction.** By default the platform records and reports the failure; fixing the data happens at source, through remediation workflows where the product offers them, or through pipeline logic. Silent self-healing is not the defining behavior.
- **Results are comparable over time.** The value of a result comes from its history — a failing check matters differently on its first failure than after a hundred clean runs. Mature products retain result history and trend it.
- **How results roll up is product-specific.** Some products compute an overall quality percentage from record-level pass/fail outcomes (with explicit handling for rules that do not apply to every record); others report per-check states without a single score. No universal scoring formula exists.
- **Rule changes are governed at platform depth.** Editing a rule changes what "good" means for the data it covers; mature products version rules and route changes through review or publish workflows, with audit trails.
- **Enforcement is a dial.** The same rule set can run watch-only (alert on failure) or enforcing (fail the pipeline, block the deploy, gate the warehouse write). Products support different points on this dial.
- **Sensitivity of results matters.** Failed-record samples contain real data; products provide controls over what is sampled, stored, and displayed, and where samples are routed.

## Variants

- **Authoring philosophy** — code-first (rules as code in version control, CI-native) vs UI-first (visual builders for stewards and business owners); most mature products blend both.
- **Deployment posture** — SaaS control plane with hosted execution; self-hosted or hybrid (processing in the customer's environment, management in the cloud); evaluation pushed down into the warehouse engine; open-source library form with no hosted layer.
- **Enforcement depth** — watch-only monitoring → pipeline gates and embedded cleansing components → CI/CD shift-left validation → in-warehouse quality functions.
- **Remediation depth** — none (report only) → export of failing records → stewardship task queues → in-platform fix-and-reevaluate.
- **Embedded observability** — several products add machine-learning anomaly detection and ambient monitoring as a second detection mode alongside authored rules; some keep it explicitly separate from the rule-based quality score.
- **Data contracts** — a producer–consumer framing in which expectations are packaged as versioned, testable agreements; currently led by a subset of products, with others expressing the same need through gates and shared standards.
- **Reference-data validation** — specialized validation against external reference data such as postal address directories; often regional and packaged as add-ons.
- **Reconciliation** — source-vs-target comparison as a first-class check type, offered by several products and used heavily in migration and integration programs.
- **Segment and tier** — developer-first open-source tools; mid-market data-team platforms; enterprise steward-oriented suites bundled with catalog, governance, or integration fabrics.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Data Observability Platform | closest sibling; interlocks | observability centers ambient health evaluation (learned baselines, anomaly detection) over the whole estate plus the incident loop; this Type centers the authored rule and its recorded pass/fail result. The two ship together increasingly — observability products embed rules as one monitor family, and quality products embed anomaly detection as a second mode — but the primary object of work separates them. |
| Data Governance Platform | consumer / umbrella | governance platforms integrate quality as one governed dimension feeding compliance and health views; this Type owns the rule/evaluation machinery itself. |
| Data Catalog | signal exchange | the catalog surfaces quality signals on entries for discovery; this Type produces those signals. A catalog does not execute quality rules as its center. |
| Master Data Management | opposite custody | MDM is the system of record creating golden master records; this Type evaluates data it does not own. They interlock (quality rules validating master data), but custody separates them. |
| ETL / ELT Platform | pipeline seam | integration platforms move and transform data; this Type evaluates it. The seam is pipeline-embedded quality (checks as pipeline steps, cleansing components inside jobs) — a capability relationship, not a merge. |
| DataOps Platform | workflow neighbor | DataOps orchestrates the data-development lifecycle; quality rules are one input to its pipelines and CI/CD gates. |
| Software Test Management / Test Automation | same pattern, different object | both express verifiable assertions and record pass/fail; software tests verify code behavior, quality rules verify data condition. Different users, result semantics, and lifecycle. |
| dbt-class test frameworks | capability, not platform | in-pipeline test definitions express the same assertion pattern but lack the managed layer (cross-source connections, result history, stewardship surfaces, scorecards, issue workflow); quality platforms commonly ingest such external test results. |

The most consequential boundary is with the Data Observability Platform, because vendors increasingly bundle both. The reliable test: if the product's center of gravity is **authored expectations with recorded pass/fail results**, it is a data quality platform; if it is **ambient health watching with an incident-response loop**, it is data observability — and many organizations run both.

## Representative Products

- **Soda** (Soda Core / Soda Cloud) — checks-as-code with a cloud collaboration layer; leads with data contracts and embeds ML observability as a second mode
- **Great Expectations (GX Core)** — open-source expectations-as-code validation framework; the developer-first minimal pole
- **Ataccama ONE (Data Quality & Catalog)** — unified enterprise platform combining quality rules, catalog, glossary, and an explicitly separate observability module
- **Talend Data Quality** (Qlik Talend) — suite module with profiling analyses and cleansing components embedded in integration jobs
- **Oracle Enterprise Data Quality** — legacy on-prem enterprise quality environment with address-verification specialization

The defining core was checked against older and differently positioned products (on-prem enterprise suites, OSS-heritage tooling) to avoid over-fitting to the current cloud/ML market shape.

## Sources

Research date: **2026-09-07**

- Soda — https://docs.soda.io (product overview; data testing & data contracts; incidents; documentation index)
- Great Expectations — https://docs.greatexpectations.io/docs/home ; GX Core overview (components and workflows)
- Ataccama — https://docs.ataccama.com/one/latest/ (DQ&C overview; Data Quality Overview; Data Quality Dimensions)
- Talend / Qlik — https://help.qlik.com/talend/en-US/ (Talend Studio User Guide: Data Profiling and Data Quality)
- Oracle — https://docs.oracle.com/en/middleware/fusion-middleware/enterprise-data-quality/14.1.2/ (Get Started / positioning)

> Sourcing limitation: the operational documentation of one major enterprise DQ vendor (Informatica) was not reachable from the research environment (access denied on repeated attempts) and that vendor is absent from direct evidence; the enterprise-suite pole is covered by the sampled products above plus observations recorded in earlier passes over adjacent Types. One legacy vendor's (Oracle) evidence is limited to its positioning page. Precise numeric limits, default thresholds, and plan-specific capabilities are intentionally not stated in this document; they remain in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis (including the seam with Data Observability) are recorded in the paired Research Notes.
