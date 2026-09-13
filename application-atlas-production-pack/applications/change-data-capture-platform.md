# Change Data Capture Platform

## Overview

A **Change Data Capture Platform** (CDC) continuously captures row-level changes made in a source system of record — almost always a database — and delivers them, in the order they were committed, as change events to downstream systems: other databases, data warehouses and lakehouses, search indexes, caches, message buses, or event-store tables.

The defining core is small:

```text
Source system of record
  └── capture through the source's own change mechanism
      └── change event (row-level insert / update / delete)
          └── ordered, continuous delivery to downstream destination(s)
              └── resumable capture position
```

Two boundary statements follow from this definition. First, the capture mechanism is a source property, not a property of the Type: reading the database transaction log is the dominant modern implementation, but trigger-written change tables and change-tracking queries are older, still-valid implementations of the same idea. Second, the product's promise is the **event stream itself**. When the promise is instead "the target stays an exact copy of the source," the product is a data replication platform; when the promise is "the destination reflects the source as of each scheduled sync," it is an ETL/ELT platform. Both neighbors reuse the same capture machinery, which is why the market's best-known products often describe themselves with all three words at once.

## Users & Context

Primary users are technical:

- **Data engineers** build and operate pipelines that feed warehouses, lakehouses, and search systems with fresh operational data instead of nightly batch extracts.
- **Platform / infrastructure engineers** run capture as a shared service, wiring operational databases to event buses and consumer teams.
- **Database administrators / DBAs** configure the source side — the log settings, privileges, and replication artifacts a database must expose before its changes can be captured — and watch the load the capture adds.
- **Application engineers** consume change streams to keep caches, indexes, and downstream services consistent with the database of record, or to integrate microservices through an outbox-style flow.

Typical scenarios: keeping an analytics store continuously up to date; feeding a message bus with database changes; invalidating caches and search indexes on write; replicating data between heterogeneous engines; and migrating a live system to a new database with a cutover window measured in minutes rather than weekends. The work is operational and long-running: a capture pipeline is configured once and then runs indefinitely, so most daily interaction is monitoring, not building.

## Core Model

### The defining core

Four structures. Remove any one and the product stops being a CDC platform:

- **Source of record with a change mechanism.** The platform attaches to a source system — a relational database, sometimes a NoSQL store — and reads changes from a mechanism that system already produces: its transaction or redo log, a logical replication stream, trigger-written change tables, or change-tracking queries. The platform does not ask the application to double-write or stamp every row; it observes what the source itself records. (Log-based capture is favored in modern products because it catches every change — including deletes — with low delay and no schema changes; the same products explicitly name polling and dual writes as the alternative approaches they displace.)

- **Change event.** The unit of delivery. One event represents one row-level change: the operation type (insert, update, or delete), the table and record identity, the new row state (and, depending on the source's capabilities, the previous state and metadata such as transaction identity). Events are the currency of the whole Type — everything downstream consumes events, not tables.

- **Ordered, continuous delivery.** Events flow to one or more destinations in the order the source committed them. A transaction's changes are delivered as a unit, after the transaction commits — uncommitted work never leaks downstream. "Continuous" is the operative word: capture runs for the life of the pipeline, not on a schedule.

- **Resumable capture position.** The platform records how far it has read into the source's change stream — a log position, a system change number, a checkpoint, or a cursor. After a crash or restart, capture resumes from that position rather than re-reading or skipping changes. This is what makes the pipeline a durable stream rather than a repeated one-off extract.

### Standard capabilities around the core

Mature products add a consistent set of structures that make the core usable in practice:

- **Initial snapshot / backfill.** A running database's history usually exceeds what its logs still hold, so products offer an initial load of existing data — with capture running concurrently so no change is lost between the snapshot and the live stream — and then hand off to streaming. Snapshot behavior is configurable (for example, re-snapshotting individual tables while the stream keeps running).
- **Selection and filtering.** Include/exclude lists over schemas, tables, and columns; masking of sensitive column values.
- **Mapping and routing.** Per-table decisions about where events land: which target schema or topic, which name, and how source names map to target names.
- **Lightweight transformations.** In-flight filtering, routing, renaming, flattening of event structure, and value masking. This is deliberately modest — reshaping events for delivery, not general-purpose computation.
- **Schema-change handling.** Structural changes in the source (new columns, changed types) surface as schema-change events alongside the data events, and each product defines a policy for how — or whether — they propagate to targets.
- **Monitoring and recovery.** Task status, source- and target-side latency measures, logs, notifications; restart from the recorded position; error capture (rejected events, diagnostics) rather than silent loss.
- **Connector libraries.** The commercial substance of a "platform": supported source engines on one side, supported target types on the other, spanning databases, warehouses, messaging systems, and files.
- **Administration surfaces.** A management console and/or CLI/API; role-based access control in enterprise products.

## How It Works

A CDC pipeline has one build phase and one indefinitely long run phase.

### Build: define the pipeline

```text
Register the source (connection + capture settings)
→ register the destination(s)
→ select tables / columns; set filters, mappings, transformations
→ define snapshot behavior and start position
→ create the task / pipeline
```

The unit of configuration is the **task** (also called pipeline or connector deployment): one source, one or more destinations, a selection of tables, and the rules for the journey between them. Before a task can run, the source usually must be prepared — the database must be producing a readable change stream (log settings enabled, required privileges granted, and in some engines replication artifacts created). Products enforce and check these prerequisites when the connection is tested.

### Run: snapshot, then stream

```text
Start task
→ initial snapshot of existing data (optional, configurable)
   while changes are buffered so nothing committed during the load is lost
→ handoff: apply buffered changes from the snapshot point onward
→ steady state: continuous capture
   source commit → event → (filter / transform / route) → deliver → apply or store
→ on interruption: resume from the recorded capture position
```

Two details of this loop carry most of the Type's behavior:

- **The snapshot-to-stream handoff.** The initial load and the change stream must meet without a gap or an overlap. Products solve this by capturing changes while the snapshot runs and applying them afterward, or by recording a precise start position in the source's log and beginning the stream there. The start position is typically recorded when the task is created; in some products it is fixed from then on, so changing it means starting a new task.
- **Backpressure and latency.** Capture can outrun delivery when a target applies changes slowly. Products buffer in-flight changes (in memory, spilling to disk under pressure) and expose the growing gap as a latency measure — how far the delivered stream lags the source. Operators watch this number the way a mail-server operator watches a queue depth.

### Ongoing operations

Day-to-day work is monitoring (task health, latency, throughput, errors), responding to source schema changes, adding or re-selecting tables (sometimes without restarting the stream, via runtime-triggered re-snapshots), and recovering failed tasks from checkpoints. Some products also support running capture once and feeding many targets from the staged stream, and a minority support bidirectional flows between two databases with explicit protection against changes echoing back and forth.

## Interfaces

Surfaces are described conceptually; exact layouts and names vary by product.

### Management console

The primary surface in GUI-led products (and an optional add-on in framework-led ones).

- **Task list** — pipelines with status (running / stopped / failed), type (initial load, ongoing change capture), and health at a glance. Primary actions: create, start, stop, resume, delete.
- **Task detail / monitoring** — live counts of events read and applied, source and target latency, current capture position, per-table progress during initial load, recent errors. Primary actions: inspect metrics, view logs, resume/restart from checkpoint.
- **Endpoint / connection editors** — forms for source and target connections (engine type, server, credentials, engine-specific capture settings) with a connection test that validates reachability and capture prerequisites.
- **Task designer** — table/view selection with include/exclude filters, column selection, table mappings, transformation rules, and snapshot/start-position settings.

### Configuration as code

Framework-style products are configured declaratively (connector configuration with filter lists, mapping, and snapshot mode), managed through the runtime's API or CLI, and deployed like any other service. Managed cloud services expose the same controls through console, CLI, and API. Both styles coexist across the market; several GUI products also expose everything programmatically.

### Metrics and alerting

Latency (source-side and target-side), throughput, and error counters, exposed through the console and/or standard metrics channels, with notifications on task failure or stall. This is where CDC is actually operated.

## Important Rules / Behaviors

- **The source must cooperate.** Capture depends on source-side settings: the change log must be readable and retained long enough, the capture account needs specific privileges, and some engines require explicit artifacts (supplemental logging, row-level logging, replication slots or publications). If logs are purged before capture reads them, changes are lost — which is why log retention is a first-class operational concern.
- **Only committed work is delivered.** Events reflect committed transactions, delivered at the commit boundary and in commit order. In-flight, rolled-back, or partially applied transactions never appear downstream.
- **Ordering is part of the contract.** Consumers rely on receiving a table's changes in source order; the platform preserves it per stream. (How ordering maps onto a target's own parallelism — e.g., topic partitions — is product-specific.)
- **Delivery guarantees are product-dependent.** The working baseline across products is at-least-once delivery with recovery from the recorded position; some products document stronger exactly-once or idempotent-apply modes as configurable options. Downstream targets are therefore commonly designed to tolerate re-delivery.
- **Deletes are first-class events.** Unlike timestamp-based extraction, a proper change stream carries deletes explicitly — one of the practical tests of a real CDC implementation.
- **Schema changes are events too.** Structural changes arrive as their own event class; whether and how they reshape the target is governed by per-product policy, and is a routine operational decision rather than an automatic given.
- **Capture adds load to the source.** Reading logs, maintaining replication artifacts, and buffering consume source resources; sizing and monitoring the capture footprint is part of running the pipeline.
- **Latency is honest, not magical.** End-to-end freshness depends on source workload, network, and target apply rate; products expose it as a measured lag rather than promising a fixed figure.

## Variants

Common shapes of the same Type:

- **By deployment form** — open-source connector frameworks run on a streaming runtime; client-managed replication servers with a design console; fully managed cloud services; and managed ELT platforms that embed change capture inside scheduled pipelines (the last shades toward the ETL/ELT neighbor — see Related Types).
- **By destination style** — apply-to-mirror (keep another database in sync), publish-to-bus (events onto Kafka-class infrastructure for many consumers), land-in-warehouse (analytics ingestion), and store-the-events (changes persisted as event/audit tables for later replay or inspection).
- **By primary job** — integration-first (permanent pipelines feeding analytics and services) versus migration-first (change capture as the bridge during a near-zero-downtime cutover, retired after go-live). The same machinery serves both; products differ in which job leads their design.
- **By topology** — unidirectional (the norm), capture-once-serve-many staging, and bidirectional flows with loopback protection (explicitly not full multi-master conflict resolution in the products researched).
- **By scope** — database-to-database replication engines, database-to-bus stream publishers, and broad connector platforms spanning both.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Data Replication Platform | closest sibling; same machinery, different contract | replication promises a synchronized target *copy* (state-oriented: apply, failover, compare, repair); CDC promises an *event stream* to consumers. Remove the event-delivery contract and only state-sync remains → replication; remove continuous capture and only batch full-state movement remains → ETL/ELT. Flagship products often serve both contracts. |
| ETL / ELT Platform | adjacent; overlaps in connectors and destinations | ELT moves full state on a schedule (initial + incremental syncs with cursors; destination reflects source as of each sync). CDC is continuous and event-contract-shaped. Managed ELT products use CDC-like capture internally for database sources, but their delivery contract and cadence differ. |
| Event Stream Processing Platform | downstream neighbor | stream processing *computes* over event streams (windows, joins, aggregates); CDC *produces and delivers* the stream. CDC output commonly feeds stream processors; vendors ship them as separate products. |
| Reverse ETL Platform | opposite direction | reverse ETL moves warehouse data back into operational tools; CDC sources are the operational systems of record themselves. |
| Message Queue Management | infrastructure neighbor | CDC platforms publish into and consume from brokers, but the managed object is the change stream, not the queue infrastructure. |
| Database Management Console / Database IDE | source-side neighbor | those operate the database (schema, sessions, queries); CDC observes and streams its changes. Overlap only in source preparation (log settings, replication artifacts). |
| Data Integration Platform | umbrella sibling | broader family covering batch, API, and application connectors; CDC is the continuous, change-stream specialization for systems of record. |

The replication boundary deserves emphasis because the market blurs it: the best-known products in this space are branded as replication or migration tools. The structural test is the promise made to the user — "your target stays in sync" (replication) versus "your consumers receive the changes, in order, as they happen" (CDC).

## Representative Products

- **Debezium** — open-source, log-based source connectors for change capture into Kafka-class infrastructure; the clearest statement of the event-delivery contract.
- **Oracle GoldenGate** — long-established enterprise platform for transactional change capture and heterogeneous replication, in on-premises and managed-cloud forms.
- **Qlik Replicate** — enterprise, console-driven replication and CDC across a wide endpoint matrix.
- **AWS DMS** — fully managed cloud service whose ongoing-replication mode is a widely used managed CDC implementation.
- **Fivetran** — included as the boundary anchor: a managed ELT platform whose scheduled, state-oriented sync model shows exactly where the ETL/ELT neighbor begins.

## Sources

Research date: **2026-09-07**

- Debezium — Architecture and Features (Debezium 3.6 documentation): https://debezium.io/documentation/reference/stable/architecture.html , https://debezium.io/documentation/reference/stable/features.html
- AWS Database Migration Service — User Guide: Introduction, Components, and "Creating tasks for ongoing replication": https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.html , https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.Components.md , https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html
- Oracle GoldenGate — product family documentation hub and overview: https://docs.oracle.com/en/middleware/goldengate/index.html , https://docs.oracle.com/en/database/goldengate/core/index.html , https://docs.oracle.com/en/middleware/goldengate/core/19.1/coredoc/overview-oracle-goldengate.html
- Qlik Replicate — online help: welcome, System Architecture, Using Change Tables: https://help.qlik.com/en-US/replicate/Content/Replicate/Main/Home.htm , https://help.qlik.com/en-US/replicate/May2026/Content/Replicate/Main/Introduction/System_Architecture.htm , https://help.qlik.com/en-US/replicate/May2026/Content/Replicate/Main/Change%20Tables/use_change_tables.htm
- Fivetran — Core Concepts, Sync Overview, Sync Modes: https://fivetran.com/docs/core-concepts , https://fivetran.com/docs/core-concepts/syncoverview , https://fivetran.com/docs/core-concepts/syncoverview/sync-modes

> Sourcing limitation: Oracle GoldenGate's in-depth concept chapters (capture and apply process internals) were not retrievable from the research environment (JavaScript-rendered pages); GoldenGate-related statements are limited to its product-family documentation, overview page, and documented topic structure. Precise numeric limits, default settings, latency figures, and per-engine configuration details are intentionally not stated in this document; product-by-product evidence is recorded in the paired Research Notes.
