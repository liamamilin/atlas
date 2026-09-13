# ETL / ELT Platform

## Overview

An **ETL / ELT Platform** is the data team's pipeline platform for consolidating data from operational source systems into analytical destinations **through a designed transformation**. Its defining promise is not merely that data moves — it is that data arrives at the destination in the shape the pipeline's transformation logic designed: cleansed, joined, aggregated, typed, and modeled for analysis.

The two halves of the name describe where that transformation executes, and both are the same product:

- **ETL** (extract → transform → load): the transformation runs inside the platform's engine before the data is written to the destination.
- **ELT** (extract → load → transform): the raw data is written to the destination first, and the transformation runs afterwards, inside the destination.

Which placement a product uses is a design philosophy and an era marker — not a different kind of product. The same structures underlie both: a persistent, configured, re-runnable pipeline that connects systems the platform does not own, carries a managed transformation step, and is executed and monitored by the platform.

The platform is never the system of record for the data. Sources and destinations own their data; the platform owns the pipeline that moves and shapes it.

## Users & Context

Primary users are technical data-team roles:

- **Data engineers / analytics engineers** — build and maintain pipelines: connect sources, design transformation logic, manage schedules and environments.
- **BI developers / data warehouse developers** — shape data into the tables and views that reports and dashboards consume.
- **Data team leads** — own pipeline reliability, credentials, environments, and promotion between development and production.

Secondary consumers are the recipients of the pipeline's output — analysts, BI tools, data scientists, and increasingly AI/ML workflows — who read the destination tables the pipelines produce. They typically do not operate the platform itself.

The working context is the organization's analytical data stack: operational systems (databases, SaaS applications, files, event stores) on one side; a cloud data warehouse, data lake, or lakehouse on the other. The ETL/ELT platform is the machinery in between. It is operated continuously — pipelines run on schedules for years, accumulate run history, and evolve as sources and business logic change.

## Core Model

The platform's world is built around five structures. The first two together are what make the product an ETL/ELT platform rather than a generic mover or a pure transformation tool.

### The pipeline — a persistent, configured unit of shaped movement

The central object is the pipeline (called a *package*, *job*, *flow*, or *connection* depending on the product): a named, kept, editable unit that specifies what data is extracted from which source, how it is transformed, and how it lands in the destination. Pipelines are never one-shot; they are designed once and re-run on schedule for as long as the need exists. A pipeline's content is data moving **between external systems** — if the movement between systems is removed and only in-place transformation remains, the product category changes (see Related Application Types).

### The designed transformation — the pipeline's load-bearing step

Inside the pipeline sits transformation logic: mapping, cleansing, type conversion, joining, filtering, aggregating, pivoting, deduplication, and business-rule application. This logic is a first-class, managed artifact — authored on a visual canvas from component libraries, written as SQL or scripts, or orchestrated through destination-side transformation projects — and it is versioned, testable, and re-runnable like any other code. The transformation is what turns "a copy of my source data" into "the dataset my analysis needs". If the designed transformation is removed and only copying remains, the product becomes a pure data-movement or replication platform.

### Source and destination connections

Pipelines attach to external systems through connection objects that hold addresses, authentication, and credentials. Sources are databases, SaaS applications, APIs, files, and event stores; destinations are data warehouses, data lakes, databases, and analytical stores. Credentials are managed configuration — stored, rotated, and permissioned by the platform — never hardcoded into pipeline logic.

### Execution machinery

The platform runs pipelines: on schedules, on demand, on events, or chained after other runs. An orchestration layer composes pipelines into flows — dependencies, conditionals, loops, transactions, and run-transformation steps — so that multi-stage work (land raw data, then transform, then publish) executes in order. Every run is recorded: status, duration, logs, and errors, forming the run history the team operates from.

### The destination dataset — the shaped output

The pipeline exists to produce tables, views, or files in the destination that hold data in its designed shape. In the ELT placement, the destination also holds the raw landed data alongside the transformed data — a deliberate property, because it means a failed or rethought transformation can be corrected and re-run against the raw data without re-extracting from the source.

## How It Works

The typical working loop has five stages.

### 1. Connect sources and destination

The team registers the source systems and the destination store: connection details, authentication, credentials. In configuration-driven products this is a setup wizard per connector; in designer products it is connection objects created alongside the pipeline. The platform tests reachability and reads the source's schema.

### 2. Author the pipeline

The team selects what data moves (tables, streams, columns), then designs the transformation: dragging transformation components onto a canvas (join, filter, aggregate, calculator, pivot…), writing SQL or scripts, or configuring destination-side transformation models. Mapping decides how source fields become destination columns and where data lands (schemas, namespaces, naming). Many products include assertion or test components so the pipeline can verify its own output.

### 3. Schedule and orchestrate

The pipeline is scheduled (intervals, CRON, or manual runs) and, where orchestration exists, wired into a flow: run the load, then run the transformation, then refresh the published view — with conditionals, retries, and transaction boundaries around the steps.

### 4. Runs execute — extract, transform, load

At run time the platform extracts from the sources (full load on first run; incremental loads afterwards using cursors, watermarks, or change capture), applies the transformation (in its own engine, pushed down to the destination's engine, or in the destination after load), and writes the result. Failures are handled by machinery the product exposes: row-level error routing (failed rows diverted to an error path for inspection or alternate handling), checkpoints that let a failed run resume where it stopped, retries, and re-sync paths that reload data when incremental continuity breaks.

### 5. Monitor and evolve

The team watches run history, logs, and performance monitors; diagnoses failures; and fixes pipelines. Over time sources change — new fields appear, types change — and the platform's schema-drift machinery (design-time validation against captured schema snapshots, automatic type promotion, or drift policies) surfaces and absorbs the change. Pipeline definitions live under version control; environments separate development from production.

## Interfaces

The surfaces below are described conceptually; exact layouts and names vary by product.

### Pipeline designer / canvas

The authoring surface, in canvas-centric products: a workspace where sources, transformation components, and destinations are placed and wired into a flow, with per-component configuration dialogs, expression editors, and data previews. Configuration-driven products replace the canvas with setup wizards and forms per connector.

### Code and configuration surfaces

SQL and script components inside pipelines; full code-first authoring (transformation projects, SDKs, APIs, command-line and infrastructure-as-code control) in products that treat pipelines as code.

### Orchestration and scheduling surface

Where multi-step flows are composed: job lists, dependency wiring, schedule management, trigger configuration (event-based, run-after-completion).

### Monitoring surface

Run history with status and duration, logs per run, performance views, and increasingly lineage views tracing data from source to target. This is the surface operators live in when something breaks at 2 a.m.

### Administration surface

Users, roles, and permissions; credential and secret management; environments and projects; version-control integration; import/export of pipeline definitions; audit logs.

## Important Rules / Behaviors

- **The platform is a custodian, not a record-keeper.** Data at rest belongs to the sources and destinations. The platform holds pipeline definitions, credentials, and run history — not the business data.
- **Transformation placement determines where raw and shaped data live.** In the transform-before-load placement, only shaped data lands. In the transform-after-load placement, raw data lands first and stays — so transformations can be edited and re-run against raw data without re-extraction. Products differ visibly here, and the difference shapes how teams recover from transformation mistakes.
- **Schema drift is expected and surfaced.** Sources change under the pipeline. Products handle this with design-time schema snapshots validated against live sources, automatic type inference and lossless type promotion, or explicit drift policies — but some form of drift handling is structural, because pipelines outlive source schemas.
- **Error handling is a designed behavior, not an afterthought.** Row-level failures (type conversions, lookup misses, constraint violations) have explicit paths: fail the run, skip, or divert the row to an error output for separate handling. Run-level failures have checkpoints and retries. Teams design these paths as deliberately as the happy path.
- **Pipelines are designed to be re-run.** Re-running a pipeline should produce consistent results — incremental logic is cursor-based, transformations are written to be idempotent, and re-sync machinery exists for when continuity breaks.
- **Credentials are platform-managed configuration.** Connection secrets are stored, permissioned, and rotatable centrally; pipeline logic references them rather than embedding them.

## Variants

The Type spans several recognizable product forms:

- **Designer-era enterprise ETL** — on-premises, graphical package designers, transformation-rich, executed and managed through a server-side catalog; the historical form, still in production at many organizations.
- **Cloud pushdown ELT** — visual transformation designers whose components generate processing that executes natively inside a cloud data platform (warehouse or lakehouse), so data never leaves the destination platform.
- **Serverless cloud ETL** — visual job canvases over managed Spark-class engines, commonly paired with a data catalog and crawler-driven schema discovery, scheduled and triggered in chains.
- **Managed automation ELT** — configuration-driven, vendor-operated connectors that land raw data into cloud warehouses on managed schedules, with transformation offered as orchestrated destination-side models (pre-built models or SQL transformation projects) rather than in-flight logic. This pole is the closest to a pure movement platform; see Related Application Types.
- **Open-source connector-catalog platforms** — self-hosted or managed, built around large connector libraries and sync configuration, with post-load transformation integration.

A variant remains a variant while the two defining structures — movement between external systems and a designed transformation step — both hold.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Data Integration Platform | closest sibling; same family, broader contract | the generic pipeline/movement platform: managed pipelines between systems, with transformation as an optional capability rather than the load-bearing promise. Movement-first products used without their transformation surfaces behave as integration platforms |
| Data Replication Platform | sibling | promises a synchronized **copy** — the destination mirrors the source's state as-is; ETL/ELT promises a **designed shape**. Scheduled state-mirroring under ELT vocabulary is the documented overlap zone |
| Change Data Capture Platform | sibling | delivers the ordered stream of change events as the product; in ETL/ELT platforms CDC appears only as a sync mechanism feeding pipelines |
| Reverse ETL Platform | sibling, inverted direction | delivers from the consolidated analytical store **out to operational business tools**, writing business objects; ETL/ELT consolidates **into** data stores with table-load semantics |
| Event Stream Processing / Stream Analytics | adjacent | continuous computation over unbounded streams; ETL/ELT pipelines are bounded, scheduled movement. Streaming appears in ETL/ELT products only as an ingestion option |
| Data Warehouse / Lakehouse / Data Lake Platforms | destination, not mover | own the storage and compute the pipelines load into; ingestion into them is entry machinery, while pipeline building and running is this Type's center |
| Transformation tools (SQL-based transformation frameworks) | counter-shape | transform data in place in the warehouse with no extract/load surface — the market treats this as a distinct category; removing the movement from an ETL/ELT platform yields this, not this Type |
| Data Quality Platform | adjacent | governed data-quality discipline is its own Type; ETL/ELT platforms carry assertion and error-handling components in service of pipeline correctness |
| Workflow Automation / iPaaS | adjacent | record/event-level operations with business side effects (send email, close ticket) vs dataset-level bulk movement |
| Managed File Transfer | adjacent | files may be a pipeline's medium, but the managed object there is the transfer event, not the pipeline |

## Representative Products

- **SQL Server Integration Services (SSIS)** — designer-era enterprise ETL; packages composed of sources, transformations, and destinations, run and managed through a catalog.
- **Matillion** — cloud pushdown ETL/ELT for cloud data platforms; orchestration and transformation jobs built from components.
- **AWS Glue** — serverless cloud ETL; visual job canvases over a managed Spark engine with catalog integration.
- **Fivetran** — managed automation ELT; vendor-operated connectors landing raw data, with destination-side transformation orchestration.
- **Airbyte** — open-source connector-catalog platform; source→destination syncs with post-load transformation integration.

The definition was checked against the designer-era form (SSIS) and the movement-first form (Fivetran) to avoid over-fitting to any single era or philosophy, and against transformation-only tooling (dbt-class) to hold the movement boundary.

## Sources

Research date: **2026-09-10**

- SQL Server Integration Services — overview and Data Flow, Microsoft Learn — https://learn.microsoft.com/en-us/sql/integration-services/sql-server-integration-services , https://learn.microsoft.com/en-us/sql/integration-services/data-flow/data-flow
- Matillion — Data Productivity Cloud product page and Matillion ETL documentation structure — https://www.matillion.com/products , https://docs.matillion.com/metl/
- AWS Glue — What is AWS Glue?, AWS documentation — https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html
- Fivetran — Core Concepts (ETL vs. ELT, shared responsibility, transformations and mapping) and Transformations documentation — https://www.fivetran.com/docs/core-concepts , https://www.fivetran.com/docs/transformations
- Airbyte — Core Concepts documentation — https://docs.airbyte.com/using-airbyte/core-concepts
- dbt — What is dbt? (boundary evidence for the transformation-without-movement category) — https://docs.getdbt.com/docs/introduction

> Sourcing notes: Matillion's newer Maia documentation was not fetched; Matillion claims are limited to the product page and the Matillion ETL docs structure. Enterprise-suite vendors (Informatica, Talend) were not re-fetched this pass; no operational claims are made for them. Numeric limits, pricing figures, and product-specific defaults observed in vendor docs are recorded in the paired Research Notes and deliberately kept out of this document.

Detailed product-by-product observations, the cross-product comparison matrix, and the movement-family boundary rulings are recorded in the paired Research Notes.
