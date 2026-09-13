# Data Integration Platform

## Overview

A **Data Integration Platform** is an application for building, running, and managing **data pipelines**: persistent, configured flows that move data from source systems to destination systems. The platform connects to systems whose data it does not own — operational databases, SaaS business applications, files, event systems on one side; data warehouses, data lakes, databases, and other operational systems on the other — and carries data between them on an ongoing basis, applying whatever selection, mapping, and transformation the pipeline defines.

The problem it exists to solve is structural: organizations run many systems that each create data, and the systems that need that data (analytics stores, other operational systems) cannot fetch it themselves in a reliable, repeatable way. Hand-built point-to-point scripts handle one pair of systems and break when systems, schemas, or priorities change. An integration platform turns each such flow into a managed object — a pipeline that is configured once, runs unattended, survives failures, and is visible to the people responsible for it.

The defining structure is small:

```text
Connections to external data systems the platform does not own
  └── Pipeline: a persistent configured unit of data movement
      (what data, how selected and mapped, where it lands)
        └── Managed execution with run visibility
            (runs on schedule or trigger; status, history, logs)
```

Everything else commonly associated with the category — huge connector catalogs, visual design canvases, ELT-style transformation in the destination, change-data-capture sync, schema-drift automation, AI-assisted design — is standard capability or variant, not what makes the product an integration platform. Older, platform-embedded, designer-era ETL products satisfy the same core without any of the modern additions; fully managed modern products satisfy it without a design canvas.

The boundary sentence: **the platform owns the movement, not the data.** Data at rest belongs to the source and destination systems; the platform is the custodian of everything that happens between them. When a product instead offers a unified logical view without copying data, it is data virtualization; when it holds the estate's storage and compute itself, it is a data warehouse or lakehouse.

## Users & Context

Primary users are technical:

- **Data / analytics engineers** build and operate the pipelines: connect sources, define what moves and how, keep syncs healthy, and hand clean data to downstream consumers.
- **BI engineers and analytics teams** are the usual beneficiaries: they consume warehouse/lake tables that pipelines keep supplied, and often request or co-design pipelines.
- **Data architects / platform teams** (in enterprise deployments) set integration standards, manage environments and credentials, and decide which patterns (batch, replication, streaming) apply to which workloads.
- **Operations / infrastructure engineers** run self-hosted deployments, monitor load, and handle scaling and availability.

Typical scenarios: feeding a cloud data warehouse or lake from operational databases and SaaS applications so analysts can query everything in one place; keeping a second system synchronized with a system of record; landing vendor or partner files; routing event and file data between internal systems; keeping AI/vector and search stores supplied with current data.

The work has a distinctive rhythm: a pipeline is built once and then runs indefinitely. Most day-to-day interaction is **monitoring** — checking that last night's syncs completed, reacting to failures, reviewing schema changes — rather than building. Building spikes happen when a new source is onboarded or an existing pipeline needs rework.

## Core Model

### The defining core

Three structures. Remove any one and the product stops being an integration platform:

- **Connections.** Named configuration objects that reach external systems: endpoint plus credentials plus settings, testable before use, kept and reused across pipelines. The platform holds a **connector** for each kind of system it can talk to — the reusable machinery that knows the system's protocol, authentication, and how to read or write its data. Sources and destinations are usually two faces of the same connector idea. The connector catalog is the platform's reach; without connections the product is a transformation engine or an SDK, not an integration platform.

- **The pipeline.** The central managed object: a persistent, named, editable unit of data movement that binds source(s) to destination(s) and specifies what travels between them — which tables, streams, files, or objects; how they are selected, filtered, renamed, and typed; where they land (namespace, schema, naming convention); and how movement behaves (full reload vs incremental, and the write behavior on the destination side). Pipelines are kept objects: they persist, can be re-run, edited, versioned, and deleted — never one-shot. The pipeline's content is data *moving between systems*; a product whose answer is a unified logical view over data that never moves is a different Type.

- **Managed execution and run visibility.** The platform runs pipelines — on schedules (intervals or CRON-style), on demand, on events, or continuously — and records what happened: run instances with status, start/end, volume, and logs or equivalent diagnostics. An operator can see at a glance which pipelines succeeded, which failed, and why. Without execution and visibility, the product is a design tool; without persistence of runs, failures cannot be diagnosed or audited.

Products name these objects differently — a "connection" in configuration-driven products, a "job" or "flow" in canvas products, a "package" in designer-era products — but the trio of connection + persistent pipeline + managed execution with visibility is present in all of them.

### Standard capabilities around the core

Mature products add a consistent set of machinery that makes the core usable in practice:

- **Connector catalog.** Pre-built connectors for the common source kinds — relational databases, SaaS business applications (CRM, billing, support, marketing), files and object storage, event systems — and destination kinds — warehouses, lakes, databases. Custom connectors via an SDK or a guided builder extend the catalog when the long tail of sources outgrows it.
- **Initial load and ongoing sync.** A first full copy of the selected data (backfill), then repeated syncs that move only what changed, using cursors, watermarks, or read-from-change-log techniques. A **re-sync** invalidates incremental state and re-fetches everything — the recovery path when continuity is broken.
- **Sync modes.** Full refresh vs incremental; append-only vs upsert/merge write behavior on the destination. The mode pair chosen per table/stream determines both correctness and destination shape.
- **Checkpointing, resumability, retries.** Progress is checkpointed so a failed run resumes rather than restarts; transient failures are retried automatically. This is what makes unattended operation trustworthy.
- **Schema-change handling.** Sources evolve: new columns, changed types, new tables. Mature products detect these changes and apply a defined policy — propagate automatically, flag for review, or fail the pipeline — and manage type mapping between systems whose native types differ.
- **Monitoring surfaces.** Run history, per-pipeline status, logs, notifications/alerts on failure; some products add lineage or provenance tracking of individual data objects through the flow.
- **Scheduling and programmatic control.** Schedule management (intervals, CRON expressions, manual runs) plus APIs, CLIs, SDKs, and infrastructure-as-code providers, so pipelines can be managed like any other infrastructure.
- **Transformation layer, in some form.** Every product can map and reshape data somewhat (typing, renaming, filtering); where deeper transformation lives is a philosophy split — some platforms push it to the destination (transform after load), others offer in-platform component-based transformation, others keep it minimal.
- **Team machinery.** Projects/workspaces, environments (dev/prod against different destination accounts), roles and permissions, audit logs, credential/secret management, version control integration.

### One structure, many implementations

The core model is written conceptually; the Variants section below enumerates how realizations differ.

```text
Pipeline object:      config-defined connection, canvas-built job or flow, designer-era package
Transformation:       post-load in destination · in-platform components · minimal routing only
Triggering:           managed schedules · manual runs · events · continuous queue-driven processing
```

A reader who has only seen one style — say, config-driven managed products with no canvas — should still recognize a canvas-built, component-based, designer-era product as the same Type from the core model.

## How It Works

A pipeline has one build phase and an indefinitely long run phase.

### Build: connect, define, schedule

```text
Register the source connection (kind, endpoint, credentials; test)
→ register the destination connection
→ create the pipeline: select data (tables / streams / objects, columns, filters)
→ set mapping: destination namespace, naming, type handling
→ choose sync behavior: full vs incremental; append vs upsert
→ set trigger: schedule, manual, or event
→ (optionally) attach transformations — position depends on the product's philosophy
→ save; run the first load
```

Configuration is validated as far as the platform can: connection tests, permission checks on the source, reachability of the destination. In canvas-style products the "define" step is drawing the flow on a design surface from components (readers, transformers, writers, control elements); in configuration-driven products it is filling settings screens; in designer-era products it is composing a package in a graphical tool. The output is the same kind of object: a saved pipeline.

### Run: initial load, then steady state

```text
Start pipeline
→ initial load: full copy of the selected data
→ steady state: repeated syncs move only what changed
   (incremental cursors / watermarks / change-log reads)
→ each run is recorded: status, timing, volume, logs
→ failures retry automatically; persistent failure surfaces as an alert
```

After the initial load, the pipeline's job is to keep the destination current according to its schedule and mode. Incremental syncs carry a **position** — a cursor, watermark, or checkpoint — recording how far the last run got. A run that fails resumes from its checkpoint; a run that cannot trust its incremental state (a broken cursor, an outage that outlasted the source's change history) falls back to a full re-sync: invalidate the position, re-fetch everything, overwrite the destination.

### Maintain: the standing loop

```text
Watch run history / alerts
→ diagnose failures from logs and diagnostics
→ absorb source schema changes (per the product's drift policy)
→ edit the pipeline: add tables, change modes, adjust mappings
→ occasionally re-sync when continuity is in doubt
→ manage credentials, environments, and access as the estate grows
```

### Defining core, standard, and optional, at a glance

**Defining core** — without these, not this Type:

- connections to external data systems the platform does not own
- persistent configured pipelines carrying data between them
- managed execution with run visibility

**Standard capabilities** — present in most mature products:

- connector catalog with custom-connector extension
- initial load + incremental sync; sync modes; re-sync
- checkpoints, retries, resumability
- schema-change handling and type mapping
- monitoring: run history, logs, alerts (lineage/provenance in some)
- scheduling + API/CLI/infrastructure-as-code control
- a transformation layer in some form
- team machinery: workspaces/environments, permissions, credential management, version control

**Optional / variant** — depends on segment, era, deployment:

- visual canvas vs config wizard vs code-first management
- deep in-platform transformation (ETL-style) vs minimal transformation with post-load modeling (ELT-style)
- log-based change capture; streaming/continuous processing; file routing
- outward data activation (writing back into SaaS/operational tools)
- managed SaaS vs self-hosted vs hybrid vs platform-embedded deployment
- AI-era additions: suggested mappings, natural-language pipeline building, context layers for agents

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Connection / connector catalog

The entry surface for onboarding a system.

- searchable catalog of supported source and destination kinds; custom-connector entry point
- a setup flow per connector: credentials, endpoint/settings, permission and connectivity tests
- primary actions: add connection, test, edit credentials, retire

### Pipeline editor / builder

Where a pipeline is defined. Takes one of three recognizable forms:

- **configuration screens** — pick source connection, pick data (tables/streams, columns, filters), pick destination, set sync mode, schedule, naming
- **design canvas** — a visual graph of components (readers, transformations, writers, control elements) wired left-to-right or top-to-bottom, each with parameter panels
- **code / API surface** — pipelines declared as configuration files or via API, managed like infrastructure with version control

Typical information: source and destination bindings, selected data, sync mode, schedule, last-run status. Primary actions: create, edit, clone, disable/enable, delete, run now.

### Run history / monitoring

The daily working surface.

- list of runs (or per-pipeline status): state (succeeded/failed/running), timestamps, rows/volume, duration
- drill into a run: logs, error diagnostics, per-table/per-stream detail
- primary actions: filter, inspect logs, retry/re-run, re-sync, configure alerts

### Administration

- credentials and secret storage; environments (dev/prod destination bindings)
- users, roles, permissions, audit history
- deployment/instance management (for self-hosted or instance-based products)

### Programmatic surfaces

- REST API and SDKs mirroring the UI's operations; CLIs; Terraform/infrastructure-as-code providers in modern products — the same objects (connections, pipelines, schedules) addressable without the UI.

## Important Rules / Behaviors

### Pipelines run unattended; monitoring is the norm

The built pipeline is expected to run indefinitely without a person present. The product's reliability machinery (checkpoints, retries, alerts) exists precisely because nobody is watching each run; the operator's job is the exception queue, not the run itself.

### Incremental state is the correctness anchor

An incremental pipeline's cursor/checkpoint is the record of what has already been delivered. Breaking or losing it does not merely pause the pipeline — it makes "what has the destination already received?" unanswerable, which is why mature products pair incremental sync with an explicit, disruptive re-sync fallback.

### The destination schema is a contract

The pipeline defines where data lands and in what shape (namespace, table names, column names and types). Ongoing syncs depend on that shape staying stable, so products define how source-side changes reconcile with it: automatic promotion (widening types, adding columns), flagged review, or deliberate failure. Silent reshaping is the failure mode these policies exist to prevent.

### The platform is a mover, not a system of record

Data at rest belongs to the source and destination systems. The platform may stage data briefly in flight, but deleting the platform does not delete the estate's data; deleting a destination table's source pipeline leaves that table frozen, not deleted. This is also why source-side load is treated with care: pipelines read from production systems, and the read burden is a real operational cost the platform makes visible and tunable.

### Credentials are first-class objects

Pipelines authenticate as configured identities with read access to sources and write access to destinations. Credential storage, rotation, and permissioning are core administration, not an afterthought; in enterprise products, pipeline-level access control and audit trails follow.

### Movement is physical

Data is copied from source to destination. This is the line against logical-access alternatives: if answering a question requires leaving the platform and querying the source system directly, the platform is not doing integration in this sense — it is describing or federating data.

## Variants

Common realizations of the Type:

- **Managed automation platforms** — configuration-driven, no canvas; the vendor operates the extract-load machinery and connector maintenance; transformation pushed post-load into the destination. Dominate the mid-market analytics feed use case.
- **Open-source connector-catalog platforms** — self-hostable or managed cloud; very large community connector catalogs plus builder tooling; pipelines managed via UI or as code.
- **Visual low-code designers with pushdown transformation** — canvas-built jobs whose transformation components execute on the destination platform's compute (cloud warehouses); popular where transformation logic is central and teams prefer visual development.
- **Flow-based dataflow systems** — continuous, queue-driven processing of discrete data objects through graphs of processors; strongest in routing, mediation, and file/event movement rather than warehouse ELT; deep lineage and guaranteed-delivery machinery.
- **Enterprise data-management suites** — integration as the flagship service of a broader platform (catalog, quality, MDM, governance sold alongside); multiple integration patterns (batch, replication, CDC, streaming) behind one design and operations surface.
- **Designer-era / platform-embedded ETL** — packages built in a graphical tool inside a database platform's ecosystem, executed and managed from a catalog or scheduler; the historical baseline of the Type and still widely deployed.
- **Direction extension: data activation** — some platforms add outward flows (warehouse → SaaS/operational tools), often branded separately; a capability layered on the same pipeline machinery rather than a different core.

A variant remains a variant unless it changes the core: a product with no persistent pipelines is not a lighter integration platform but a different tool; a product that stops moving data — and only reads it in place — has left the Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| ETL / ELT Platform | nearest sibling; describes the technique emphasis (extract-transform-load jobs, or load-then-transform) rather than the pipeline-management center; in the market the same products are labeled both ways — boundary recorded as a taxonomy note for joint review |
| Change Data Capture Platform | promises an ordered, continuous stream of row-level change events to consumers; integration platforms use change capture as one sync mechanism inside pipelines |
| Data Replication Platform | promises a synchronized target *copy* of a source (a state contract); integration platforms promise managed flows; same machinery, different promise |
| Reverse ETL Platform | the outward direction only — warehouse/serving store into SaaS and operational tools; some integration platforms include it as an optional capability |
| Data Virtualization Platform | answers the same "many systems, one need" problem with query-time logical access and **no physical copy**; integration platforms physically move data |
| Data Fabric Platform | estate-spanning unified metadata/governance layer in which integration is one function; the integration platform has the pipeline, not the estate, as its center |
| Data Exchange Platform | inter-organizational dataset offerings with entitlements and delivery; integration platforms move data within one organization's systems |
| Workflow Automation / application integration platforms | operate at record/event level to trigger business actions (send a message, create a ticket); integration platforms move datasets in bulk without business side effects |
| Managed File Transfer | manages file-transfer events (delivery, transfer semantics, endpoints); integration pipelines may carry files, but the managed object is the standing pipeline |
| Data Warehouse / Lakehouse Platform | destination-side systems that own storage and compute and are the usual landing zone; the integration platform owns neither |
| Business Intelligence Platform | downstream consumer; BI reads what integration supplies and holds no source connections of its own |

The two most important boundaries: against **data virtualization** (movement vs no-movement — the fork between the two fundamental ways to make distributed data usable) and against the **delivery-contract siblings** (CDC/replication/ELT — the same machinery marketed under different promises, with label drift so heavy that vendor self-descriptions cross the leaves).

## Representative Products

- Fivetran
- Airbyte
- Matillion
- Apache NiFi
- Informatica (Intelligent Data Management Cloud — Data Integration & Engineering)

The definition was checked against an older, platform-embedded, designer-era product (SQL Server Integration Services) to avoid over-fitting to the modern managed-ELT pattern: designer-built packages, catalog-managed execution, and source/destination connectivity satisfy the same core with none of the modern additions.

## Sources

Research date: **2026-09-07**

- Fivetran — Documentation and Core Concepts (connector/destination/connection model, syncs, checkpoints, re-sync, ELT shared-responsibility model) — https://fivetran.com/docs , https://fivetran.com/docs/core-concepts
- Airbyte — Data replication platform and Core Concepts (source/destination/connector/connection, streams and records, sync modes and schedules, resumability, schema propagation, movement taxonomy) — https://docs.airbyte.com/platform/ , https://docs.airbyte.com/platform/using-airbyte/core-concepts
- Matillion — Matillion ETL documentation structure (jobs, orchestration vs transformation components, connectors, schedules, task history, CDC module, permissions) — https://docs.matillion.com/metl/
- Apache NiFi — Project overview and overview document (dataflow automation, FlowFile/processor/connection model, provenance, guaranteed delivery, visual command and control) — https://nifi.apache.org/ , https://nifi.apache.org/docs/nifi-docs/html/overview.html
- Informatica — Data Integration and Engineering product page (suite positioning, integration patterns including ELT/ETL/replication/CDC, low/no-code posture) — https://www.informatica.com/products/cloud-data-integration.html
- Microsoft — SQL Server Integration Services overview (packages, tasks and transformations, graphical designer, catalog-based execution) — https://learn.microsoft.com/en-us/sql/integration-services/sql-server-integration-services

> Sourcing limitation: Informatica's operational documentation portal was not article-accessible from the research environment on 2026-09-07; Informatica evidence is product-page level, so no precise operational details are asserted for it. Vendor connector counts and marketing figures are treated as positioning claims and are not repeated as facts. Precise product-specific behaviors (pricing units, release phases, plan tiers) are recorded in the paired Research Notes rather than in this document.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis against the neighboring data-movement Types are recorded in the paired Research Notes.
