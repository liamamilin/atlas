# Metrics Monitoring

## Overview

A **Metrics Monitoring** application continuously collects numeric measurements from the systems under observation, stores each metric as a persistent time series, lets people read behavior over time through aggregated graphs and queries, and evaluates those series against defined conditions to raise alerts when values leave their expected range.

The defining core is small:

```text
Identified metric time series
└── Continuous collection from the observed environment
    └── Time-and-dimension evaluation (the read loop)
        └── Condition → alert watch loop
```

Everything commonly associated with modern products — metric-type vocabularies, expressive query languages, dashboard catalogs, cardinality controls, standardized telemetry protocols — is widespread standard capability, not part of what makes the product a metrics monitoring application. Older tools that kept a flat list of per-target series with no dimensional labels still fit this definition; so does a cloud platform's built-in metrics service and an open-source toolkit.

When the organizing spine becomes a managed inventory of watched hosts and devices with per-entity health states, the product has crossed into Infrastructure Monitoring. When the records under inspection are individual timestamped events rather than numeric series, it has crossed into Log Management.

## Users & Context

Primary users are engineering and operations teams responsible for the health of running systems — infrastructure, platform, and application operations roles. They configure what gets measured, build the charts their teams read daily, define the alert rules that decide when something is wrong, and are the people those alerts wake up.

Secondary users:

- application developers instrumenting their own services and reading their performance series
- service and product owners who consume operational numbers (request rates, error rates, queue depths) alongside business-shaped series such as signups, orders, or commit counts — the same structures carry both
- adjacent teams (security, finance, support) reading dashboards produced from these series

The context is always-on operational software. The application is consulted routinely for health checks and capacity awareness, and most urgently during incidents. Because the tool must be readable precisely when other systems are failing, its own availability is treated as a first-order product expectation rather than an afterthought.

## Core Model

### The Defining Core

Four properties. Remove any one and the product stops being recognizable as metrics monitoring:

- **The identified metric time series** — each metric is a persistent series of timestamped numeric measurements, individually identified by a metric name plus identifying attribute values (labels, tags, or dimensions; the oldest implementations used a flat per-target name). The series — not the individual event, not the request, not the managed machine — is the addressable unit the application stores, queries, and alerts on. Without series identity, the product is an unstructured numeric store.
- **Continuous collection from the observed environment** — measurements flow in on an ongoing basis from the systems under watch, through code instrumentation, agents, data exporters, integration catalogs, or platform-provided feeds, by push or by pull, on a collection cadence the product operates. The data's subject is always the behavior of *other* systems. Without this, it is a passive database awaiting manual loads.
- **Time-and-dimension evaluation** — stored series are aggregated over time windows and split or combined across their identifying dimensions, and read primarily as time-oriented graphs and queries. This is how users see state, change, and pattern over time. Without it, the product is a raw telemetry archive.
- **The condition → alert watch loop** — rules continuously evaluate series against defined conditions (thresholds, rates, computed expressions) and emit alerts that are routed to people or channels, with noise control (suppression windows, hysteresis) and recovery signaling. Without it, the product is a metrics warehouse or a graphing system — the recognized precursor, not the Type.

These four are jointly held. A time-series database without collection, a collection pipeline without history, a charting layer without alerts, and an alerting engine over unretained streams each describe a different kind of software.

### Capabilities Shared by Mature Products

A typical modern product carries most of the following. They are not what makes the product metrics monitoring, but they make it practical:

- **Metric types** — gauge, counter, rate, and distribution/histogram families; the declared type determines which graphs and functions are available for a metric.
- **A query language or query API** combining time aggregation (which is always applied — every read collapses points into time buckets) with space aggregation (grouping or splitting series by their attribute values, and arithmetic between series).
- **Derived series** — recorded series computed from other series by rule, or metrics computed from raw events (for example, counting occurrences in event streams into a numeric series).
- **A broad ingestion surface** — agents on hosts, exporters and integrations for third-party services, direct API publishing, and increasingly a vendor-neutral telemetry protocol as a common ingestion path.
- **Dashboards and metric catalogs** — chart surfaces for teams, plus explorer/summary views listing which metrics are actively reporting and with what metadata.
- **Alert lifecycle management** — routing notifications to the right people and channels, muting or suppressing alerts during maintenance, aggregating related alerts, and signaling recovery.
- **Retention with coarsening** — series are retained over bounded horizons, commonly aggregated at coarser granularity as data ages. Exact horizons differ substantially by product.
- **Volume and cardinality management** — as usage grows, products expose tooling to understand and control how many distinct series are being produced, which becomes both an operational and a cost concern.

### One Structure, Many Implementations

The core model is written conceptually. Implementations differ on every axis:

```text
Concept:            Identified metric time series
Implementations:    name + key/value labels · namespace + name + dimensions · flat per-target series (historical)

Concept:            Collection
Implementations:    pull/scrape from exposed endpoints · agent push on flush intervals · platform-vended feeds · API publishing · remote-write into storage backends

Concept:            Read loop
Implementations:    dedicated expression query languages · SQL-flavored query APIs · prebuilt dashboards · generated chart pages (historical)
```

A reader who has only seen one modern implementation should still be able to recognize the historical and platform-native forms from this table.

## How It Works

### Bring measurements in

```text
Decide what to measure
→ instrument code or install agents/exporters, or rely on platform-vended metrics
→ expose, push, or publish the values
→ the product operates the collection cadence and manages the ingest
→ series accumulate as identified time series
```

There is no fixed list of "the metrics" — the collection surface is open-ended, spanning machine resources, service behavior, platform quotas, and business counters. The product's job is to keep the pipeline running and to make the arriving series discoverable.

### Read behavior over time

```text
Pick a metric (by name, from a catalog or explorer)
→ filter by attribute values (environment, region, service…)
→ choose a time window and aggregation (sum / average / min / max / count)
→ optionally group or split by another dimension, or combine series arithmetically
→ read the result as a graph or a single computed value
```

This loop is the daily bread of the product: comparing now against earlier, spotting spikes, correlating one series against another. Aggregation over time is always present — graphs never show every raw point; they show windowed aggregates whose granularity adapts to the span being viewed.

### Turn series into alerts

```text
Define a rule: a condition over one or more series (threshold, rate, computed expression)
→ the product evaluates it continuously against incoming data
→ when the condition holds, an alert fires
→ the alert is routed to people/channels with context (which series, which values, since when)
→ while maintenance makes alerts unwanted, muting windows suppress them
→ when the value returns to normal, recovery is signaled
```

Alerts, not dashboards, are what make this application a *watch* system: the product is expected to notice out-of-bounds behavior without a human looking.

### Capability tiers

- **Defining core** — identified numeric time series; continuous collection from observed systems; time-and-dimension evaluation with graphs; condition evaluation producing alerts.
- **Standard capabilities** — metric types, query languages/APIs, derived series, broad integration surfaces, dashboards and metric catalogs, alert lifecycle management, bounded retention with coarsening, volume/cardinality tooling.
- **Optional / variant** — pull vs push collection, identity model (labels vs dimensions), standardized telemetry protocols, multi-tenancy, high-availability machinery, cloud-native pay-per-use delivery, business-KPI emphasis.

## Interfaces

The surfaces below are described conceptually; exact layout and naming vary by product.

### Metric explorer / catalog

The discovery surface for what is being measured.

- lists actively reporting metrics with metadata (type, units, where values come from, which attribute values exist)
- primary actions: search, inspect a metric's dimensions and volume, jump to a chart or an alert rule

### Dashboard / charts

The team's standing read surface.

- time-series graphs organized into panels; single-value and top-N views alongside
- primary actions: compose a query per panel, set the time span, save/share the layout

### Query surface

Where precision work happens.

- an expression editor (dedicated query language or SQL-like API) with filtering, grouping, arithmetic, and functions
- primary actions: build/validate a query, compare series, turn a query into a panel or an alert condition

### Alert rule editor

The watch configuration surface.

- the condition (a query plus thresholds), the evaluation cadence context, and notification routing
- primary actions: define/edit rules, set severities, attach runbook-style context, configure mute windows

### Alert list / alert status

Where fired alerts live.

- current firing alerts with their series, values, start times, and routing state; recent history including recoveries
- primary actions: acknowledge, silence, inspect the underlying chart, follow the notification trail

### Collection configuration

How the pipeline is administered.

- agent/integration management, scrape or publish endpoints, and the cadence of collection
- primary actions: add or edit sources, verify data is arriving, retire stale sources

## Important Rules / Behaviors

- **Data is numeric, sampled, and approximate by nature.** Collection runs on intervals; values represent samples or interval aggregates, not a complete record of every occurrence. Such systems are not suited to uses that require per-item accounting accuracy (such as billing); they are built instead for continuous watching, including during failures.
- **Aggregation is always applied on read.** Any view over a span shows windowed aggregates, so the granularity of what you see depends on the span. Misreading aggregated graphs is a known operational hazard the interfaces work to expose.
- **Series identity drives everything.** Filtering, grouping, alert scoping, and access to the data all operate on the identifying attribute values. Managing those attributes well (and keeping the number of distinct series under control) is an operational discipline of its own.
- **Alerts are evaluated continuously, not on demand.** A rule is a standing definition; the product watches every new data point against it. Noise control — suppression during maintenance, hysteresis against flapping, grouping of related alerts — is part of the loop, not an add-on, because uncontrolled alerting defeats the watch.
- **Recovery is signaled, not silent.** The loop includes the return-to-normal event, delivered through the same channels as the breach.
- **History is bounded and coarsens with age.** Products retain series for finite horizons; older data is commonly kept at coarser granularity. Long-horizon analysis depends on the product's retention design.
- **Built to be read during failures.** The monitoring surface is expected to remain available and queryable while the systems it watches are degraded; the self-hosted toolkit form states this as an explicit, documented design goal.

## Variants

Common shapes the Type takes; none changes the defining core:

- **Open-source toolkit** — self-hosted collection, storage, rules, and alerting as separable components; a large integration/exporter ecosystem around it.
- **Scalable storage backend** — long-term, horizontally scaled series storage that accepts streams from collection agents and serves query and alerting layers; often multi-tenant.
- **Commercial SaaS observability pillar** — metrics as a managed product area inside a broader suite alongside logs and traces; metered by series volume or ingest.
- **Cloud-platform-native service** — metrics service built into a cloud provider, with metrics vended automatically from the platform's own services plus customer-published custom metrics; pay-per-use.
- **Scope emphases** — machine-centric, service-oriented, and business-KPI deployments share the same structures.
- **Cardinality postures** — products (or product modes) optimized for low-cardinality platform metrics versus high-cardinality dimensional telemetry.

A variant stops being a variant when the organizing spine changes: adding a managed watched-estate inventory with per-entity health states yields Infrastructure Monitoring, not a metrics monitoring variant.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Infrastructure Monitoring | organizes collection, health, and alerting around a persistent inventory of watched entities (hosts, devices, instances) with per-entity health states; metrics monitoring holds and watches series with no estate inventory — hosts appear only as attribute values |
| Log Management | holds individual timestamped event records inspected one-by-one; metrics monitoring holds numeric series evaluated over time; computing a metric from event patterns is a one-way bridge into this Type |
| Application Performance Monitoring (APM) | centers request/operation-centric performance telemetry of an instrumented service population with drill-down into individual request traces; metrics monitoring is subject-agnostic over any numeric series and has no request-path records |
| Distributed Tracing | records spans assembled into per-request traces; here the record is a numeric series over time, not a request path |
| Observability Platform | the umbrella suite bundling metrics, logs, traces, and more; metrics monitoring is its metrics pillar and also exists fully standalone |
| Network Monitoring | specializes in network devices, links, flows, and latency semantics; network measurements otherwise land here as ordinary series |
| Synthetic Monitoring | produces measurements by running scripted probes; those measurements are consumed as series — producer versus the series layer |
| Capacity Management | consumes series history for forward-looking demand-vs-supply projection and right-sizing; metrics monitoring observes current and recent state only |
| Dashboard Platform / Business Intelligence | reads curated, human-loaded business datasets for reporting; metrics monitoring's data arrives continuously from observed systems and feeds a standing watch loop |
| Event Stream Processing | computes over in-flight streams without retained history as the object; metrics monitoring stores, retains, and evaluates series over historical windows |
| Incident Management / On-call Management | takes over after the alert fires — deduplication into incidents, escalation, schedules, postmortems; metrics monitoring ends at alert emission and routing |
| Industrial Historian / SCADA family | structural cousin for plant floor numeric series; carries process-control and industrial-protocol semantics that IT telemetry monitoring does not |

The most load-bearing seam is with Infrastructure Monitoring, because the market bundles the two: a suite's "infrastructure" product area sits on the metrics layer and adds the entity inventory and per-entity health states. The tell is the organizing spine — series and their attributes here; watched entities and their health states there.

## Representative Products

- Prometheus — open-source monitoring and alerting toolkit (pull-based, expression query language, rules + separate alert manager)
- Datadog (Metrics) — managed metrics product area of a commercial SaaS observability suite (agents and integrations, metric types, monitors)
- Amazon CloudWatch (Metrics) — cloud-platform-native metrics service with platform-vended and customer-published metrics and built-in alarms
- Grafana Mimir — horizontally scalable, multi-tenant long-term storage backend for Prometheus/OpenTelemetry-compatible metrics

The core model was checked against the 1990s data-logging-and-graphing lineage (MRTG over RRDtool — scheduled SNMP/script collection, per-target series, generated graphs, and built-in threshold checking with break/recovery notifications) to avoid over-fitting the definition to modern cloud-native implementations.

## Sources

Research date: **2026-09-08**

- Prometheus — Overview: https://prometheus.io/docs/introduction/overview/
- Prometheus — Alerting overview: https://prometheus.io/docs/alerting/latest/overview/
- Datadog — Metrics: https://docs.datadoghq.com/metrics/
- Datadog — Monitors: https://docs.datadoghq.com/monitors/
- AWS — Metrics in Amazon CloudWatch: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html
- Grafana Mimir — documentation root: https://grafana.com/docs/mimir/latest/
- RRDtool — About: https://oss.oetiker.ch/rrdtool/
- MRTG — What it does: https://oss.oetiker.ch/mrtg/
- MRTG — configuration reference (threshold checking): https://oss.oetiker.ch/mrtg/doc/mrtg-reference.en.html

> Sourcing limitations: Grafana Mimir was researched at documentation-root depth only, and CloudWatch alarm mechanics beyond the overview level were not fetched. Precise product facts (retention spans, numeric limits, pricing meters, exact metric-type lists, evaluation defaults) are intentionally not asserted in this document; claims are calibrated to the depth of documentation actually reachable. Such details remain in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical breadth check are recorded in the paired Research Notes.
