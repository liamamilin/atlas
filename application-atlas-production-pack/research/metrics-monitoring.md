# Research Notes — Metrics Monitoring

Research date: 2026-09-08
Slug: metrics-monitoring
Directory leaf: Metrics Monitoring (§14 IT, Cloud & Infrastructure)

## Research Goal

Understand what a Metrics Monitoring application is from real products: what the unit of record is, how numeric telemetry gets in, how it is stored and identified, how people read it, and what makes it "monitoring" rather than a time-series database or a charting tool. Establish the seam against the already-processed sibling Types (Infrastructure Monitoring, Log Management, APM, Distributed Tracing, Capacity Management), whose passes pre-hung joint-review seams with this leaf.

## Initial Boundary

Working hypothesis before research:

- Core use: continuously collect numeric measurements from systems (hosts, services, applications, platform services, business processes), store them as time series, query/graph them over time, and evaluate them against conditions to raise alerts.
- Users: engineering/operations teams (SRE, platform, DevOps, IT ops); secondarily anyone consuming operational numbers (product, business).
- Nearest neighbors: Infrastructure Monitoring, APM, Log Management, Distributed Tracing, Observability Platform, Network Monitoring, Synthetic Monitoring, Capacity Management, Dashboard Platform, Event Stream Processing, Data Observability, industrial Historian.
- Suspected boundary: infrastructure monitoring was defined in its own pass as entity-inventory + per-entity health states, with "1+2 without 3 = metrics monitoring" — i.e. metrics monitoring is expected to be the series-centric layer *without* the watched-estate inventory. Log management was defined around timestamped event records inspected one-by-one; metrics monitoring expected to hold numeric series evaluated over time.

Unresolved at start: is condition evaluation/alerting definitional or merely common? Is the graph/query read loop definitional? Is "no entity inventory" a true invariant or just the modern sample?

## Research Questions

1. What exactly is a "metric" in each product's data model — what identifies one, what does a data point look like?
2. How do measurements enter the system (pull/push/agents/integrations/platform-vended)? Is collection a product responsibility or assumed?
3. What does the standard read loop look like (query language, time/space aggregation, rollups, graphs)?
4. Is alerting built in, and what is its shape (rules → evaluation → notification → recovery)?
5. What derived series machinery exists (recording rules, metrics-from-logs, computed statistics)?
6. What retention/rollup behavior is documented?
7. Is there a managed inventory of monitored entities (hosts/devices) as the organizing spine — or are series the only addressable unit?
8. How do the historical pre-cloud lineage (MRTG/RRDtool) and the platform-native lineage (CloudWatch) realize the same structures?

## Representative Products

Selection rationale: market representation + document completeness + different product philosophies + different customer tiers/business models.

| Product | Philosophy pole | Business model | Notes |
|---|---|---|---|
| Prometheus | open-source monitoring & alerting toolkit; pull-based; de-facto cloud-native standard | free OSS (CNCF) | metrics-first, self-contained |
| Datadog (Metrics product area) | commercial SaaS observability suite; metrics as a managed product area | SaaS subscription | metrics alongside logs/APM in one platform |
| Amazon CloudWatch Metrics | cloud-platform-native metrics service | pay-per-use cloud service | vended + custom metrics; two metric models |
| Grafana Mimir | horizontally scalable metrics backend (long-term storage for Prometheus/OTel metrics) | OSS + commercial support | storage-first pole; multi-tenant |
| MRTG + RRDtool | historical anchor (1990s lineage) | free OSS | market-sample/historical check |

## Sources

All fetched 2026-09-08 (Tier 1 — official operational documentation):

1. Prometheus — Overview: https://prometheus.io/docs/introduction/overview/
2. Prometheus — Alerting overview: https://prometheus.io/docs/alerting/latest/overview/
3. Datadog — Metrics: https://docs.datadoghq.com/metrics/
4. Datadog — Monitors: https://docs.datadoghq.com/monitors/
5. AWS — Metrics in Amazon CloudWatch: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html
6. Grafana Mimir — documentation root: https://grafana.com/docs/mimir/latest/
7. RRDtool — About: https://oss.oetiker.ch/rrdtool/
8. MRTG — What it does: https://oss.oetiker.ch/mrtg/
9. MRTG — configuration reference (threshold checking sections): https://oss.oetiker.ch/mrtg/doc/mrtg-reference.en.html

Source-access limitations: Mimir fetched at documentation-root depth only (structure-level evidence, not page-level detail). CloudWatch fetched at the metrics-overview level; alarm mechanics beyond the overview table not fetched. Datadog monitor *types* page not fetched (overview page only). PromQL function-level semantics not fetched; query-language claims are kept at the structural level observed. These limitations are respected in assertion strength below.

## Product Observations

Evidence layers: A = directly observed in fetched official source for that product; B = cross-product commonality; C = canonical inference.

### Prometheus (A)

- Self-description: "open-source systems monitoring and alerting toolkit"; collects and stores metrics **as time series data** — "metrics information is stored with the timestamp at which it was recorded, alongside optional key-value pairs called labels."
- "Metrics are numerical measurements."
- Multi-dimensional data model: time series identified by **metric name + key/value label pairs**.
- PromQL — "flexible query language to leverage this dimensionality."
- Collection: pull model over HTTP; push supported "via an intermediary gateway" (Pushgateway for short-lived jobs); targets discovered via service discovery or static configuration.
- Components: Prometheus server (scrapes and stores), client libraries for instrumenting application code, exporters for services, Alertmanager.
- Rules run over stored data: **recording rules** ("aggregate and record new time series from existing data") and **alerting rules** ("generate alerts").
- Visualization: Grafana or other API consumers; also expression browser and console templates.
- Scope claim: "works well for recording any purely numeric time series. It fits both machine-centric monitoring as well as monitoring of highly dynamic service-oriented architectures."
- Explicit limitation: not for 100%-accuracy needs (e.g. per-request billing) — collected data "will likely not be detailed and complete enough"; designed instead for reliability so it stays usable during outages ("the system you go to during an outage").
- Alerting (alerting overview, A): "separated into two parts. Alerting rules in Prometheus servers send alerts to an Alertmanager. The Alertmanager then manages those alerts, including silencing, inhibition, aggregation and sending out notifications via methods such as email, on-call notification systems, and chat platforms."
- No mention of a managed inventory of monitored entities with health states; the addressable objects are series (name+labels) and scrape targets (jobs/instances).

### Datadog Metrics + Monitors (A)

- "Metrics are numerical values that can track anything about your environment over time, from latency to error rates to user signups."
- Data model: "metric data is ingested and stored as data points with a value and timestamp"; a sequence of data points is "a timeseries"; same-timestamp points overwrite.
- Metric types: **count, rate, gauge, histogram, distribution** — "Metric types determine which graphs and functions are available."
- Submission paths: 1,000+ vendor-supported integrations (metrics out of the box); the Agent "automatically sends several standard metrics (such as CPU and disk usage)"; custom metrics via Agent, DogStatsD, or HTTP API; **logs-to-metrics** ("count error status codes appearing in your logs and store that as a new metric"); OpenTelemetry ingestion.
- Query anatomy (A): metric name → tag filter (e.g. `account:prod`) → **time aggregation** (rollup into time buckets; sum/min/max/avg/count; "time aggregation is *always* applied in every query") → **space aggregation** (split by tags such as host, container, region; group by produces one line per group; aggregators sum/min/max/avg) → optional arithmetic functions between metrics.
- Read surfaces: Metrics Explorer, Metrics Summary ("actively reporting" metrics with metadata: type, unit, interval, number of distinct metrics, reporting hosts, tags), Dashboards, Notebooks, Monitors.
- Business metrics explicitly in scope: "custom metrics" such as "number of user logins or user cart sizes to the frequency of your team's code commits."
- Monitors (A): "configuring monitors to track key metrics and thresholds, organizations can receive immediate alerts"; "checking metrics, integration availability, and network endpoints through the Alerting platform"; notifications routed "to the correct people" with template variables and snapshots (email/Slack); **downtimes** mute alerts during maintenance ("reduce alerting fatigue"); alert status pages for investigation; monitor-quality tooling for misconfigured monitors.
- Host appears as a **tag dimension** in queries; the metrics docs do not organize around a host inventory (that is the separate Infrastructure Monitoring product area).

### Amazon CloudWatch Metrics (A)

- "Metrics are data about the performance of your systems."
- Two ingestion paths: **AWS vended metrics** from services (EC2, EBS, RDS...) and **custom metrics** published via OpenTelemetry Protocol (OTLP) or the CloudWatch API.
- Two metric models (documented side by side):
  - OTel model: identity = metric name + up to 150 labels; types gauge/sum/histogram/exponential histogram; ingestion via OTLP; **PromQL query API**; PromQL-based alarms.
  - Classic model: identity = **namespace + metric name + up to 30 dimensions**; single values and statistic sets; PutMetricData API / EMF; query via GetMetricData/GetMetricStatistics/ListMetrics and Metrics Insights (SQL); standard alarms.
- Storage: "up to 15 months" with **automatic rollup** (classic model).
- Pricing differs by model: per-GB-ingested (OTel) vs per-metric-per-month (classic) — evidence that the unit of measure of this product category is the series/data volume, not users or entities.
- Alarms are part of both models (standard alarms; PromQL-based alarms).
- The OTel page frames convergence: "the same OTel SDKs and collectors that work with Prometheus, Grafana, and other backends work with CloudWatch out of the box."

### Grafana Mimir (A, root-level depth)

- Self-description: "horizontally scalable, highly available, multi-tenant, long-term storage for Prometheus and OpenTelemetry metrics."
- Capabilities named at root: ingest Prometheus or OTel metrics; run queries; "create new data through the use of recording rules"; "set up alerting rules across multiple tenants to leverage tenant federation."
- Data sources: Prometheus, OpenTelemetry Collector, Grafana Alloy.
- Querying/visualization via Grafana or the Mimir HTTP API.
- Ships "best-practice dashboards, alerts, and runbooks" for monitoring the health of Mimir itself (self-monitoring).
- No entity inventory or per-entity health model at this documentation level; the managed object is the metric series across tenants.

### MRTG + RRDtool (historical anchors, A)

- RRDtool self-description: "OpenSource industry standard, high performance **data logging and graphing system for time series data**."
- MRTG self-description: "will monitor SNMP network devices and draw pretty pictures showing how much traffic has passed through each interface"; "Routers are only the beginning... graph all sorts of network devices as well as everything else from weather data to vending machines."
- Configuration reference (A) confirms the full modern structure in 1990s form:
  - **Target** — each monitored series has a unique per-target name used "for naming the generated webpages, logfiles and images"; sources include SNMP OIDs and **external monitoring scripts** returning numeric values.
  - **Interval** — scheduled polling ("How often do you call mrtg? The default is 5 minutes"); daemon mode or cron.
  - Storage in RRD ("LogFormat: rrdtool") or native logs; **multi-target arithmetic expressions** ("aggregate both B channels", "calculate the percentage hard disk utilization... from the absolute used space and total capacity") — a primitive of series math/aggregation.
  - **Graphs** as the read output (day/week/month/year views, scaling options, legends).
  - **Threshold checking** (A): per-target `ThreshMinI`/`ThreshMaxI` — "the minimum acceptable value... If the parameter falls below this value, the program specified in ThreshProgI will be run and a mail will be sent to the ThreshMailAddress"; `ThreshProgOKI` — "defines a program to be run if the parameter is currently OK... but wasn't OK on the previous running" (recovery notification); `ThreshHyst` hysteresis to avoid flapping ("only send an unbroken message once the current value is 0.1 (10%) away from the threshold", customizable).
  - Invalid readings filtered via `MaxBytes`/`AbsMax` ("If a number higher than MaxBytes is returned, it is ignored").
  - Forwarding to other stores (`SendToGraphite`).
- No watched-estate inventory with per-entity health states: the target list is a config file of series definitions, not a managed inventory of hosts/devices with status. No dynamic discovery, no per-entity state model.

## Cross-product Comparison

| Structure | Prometheus | Datadog | CloudWatch | Mimir | MRTG/RRDtool |
|---|---|---|---|---|---|
| Numeric time series as unit of record | yes (A) | yes (A) | yes (A) | yes (A) | yes (A) |
| Series identity: name + identifying attributes | name + labels (A) | name + tags (A) | name + labels OR namespace + name + dimensions (A) | Prometheus/OTel identity (A) | unique target name (A) |
| Collection from observed systems | pull over HTTP + push gateway + exporters + client libs (A) | Agent + 1,000+ integrations + DogStatsD + HTTP API + OTel (A) | vended from AWS services + custom via OTLP/API (A) | remote ingest from Prometheus/OTel Collector/Alloy (A) | scheduled SNMP polling + external scripts (A) |
| Query/aggregation over time windows | PromQL (A) | time aggregation always applied; rollup; functions (A) | PromQL API / GetMetricData / Metrics Insights SQL (A) | PromQL via API/Grafana (A) | multi-target arithmetic expressions (A) |
| Dimensional splitting/grouping | label-based (A) | group by tags; space aggregation (A) | dimensions (A) | label-based (A) | per-target only (no group-by) |
| Graphing as read surface | Grafana/expression browser/consoles (A) | dashboards/explorer/notebooks (A) | CloudWatch console / Query Studio (A) | Grafana (A) | generated graphs (A) |
| Derived series | recording rules (A) | logs-to-metrics (A) | statistic sets (A, partial evidence) | recording rules (A) | computed expressions (A) |
| Condition evaluation → alerts | alerting rules (A) | monitors on metrics/thresholds (A) | standard + PromQL alarms (A) | alerting rules (A) | threshold checking (A) |
| Alert lifecycle management (silencing/downtime/hysteresis, routing, recovery) | Alertmanager: silencing, inhibition, aggregation, notification (A) | downtimes, notification routing, templates, status page (A) | alarms (mechanics beyond overview not fetched) | alerting rules + tenant federation (A) | hysteresis, break/recovery programs, mail (A) |
| Retention/rollup over time | local storage; retention configurable (not fetched in detail) | query-time rollup (A) | 15 months with automatic rollup (A) | long-term storage (A) | RRD round-robin/log aging (A, partly structural) |
| Managed estate inventory w/ per-entity health states | no (A) | separate product area, host as tag (A) | no (A) | no (A) | no (A) |
| Metric types vocabulary | counter/gauge/histogram/summary (named in docs nav; detail not fetched) | count/rate/gauge/histogram/distribution (A) | gauge/sum/histogram/exponential histogram (A) | inherits Prometheus (A) | gauge/counter options (Options keyword, A) |
| Business/custom metrics in scope | any numeric series (A) | custom business metrics (A) | custom metrics (A) | any ingested series (A) | weather data, vending machines (A) |

Reading: every modern sample and the 1990s lineage agree on the first nine rows. The only structural absence in the historical sample is dimensional group-by (flat per-target identity) — an implementation-generation difference, not a Type difference. No sampled product organizes metrics monitoring around an entity inventory.

## Canonical Abstraction

### L0 — Defining Invariant

Four jointly-held structures. Remove any one and the product stops being metrics monitoring:

1. **The identified metric time series as the unit of record.** Each metric is a persistent series of timestamped numeric measurements, individually identified by a metric name plus identifying attribute values (labels/tags/dimensions — flat per-target identity in the oldest implementations). The series — not the individual event, not the request, not the managed entity — is the addressable unit the application stores, queries, and alerts on. Remove → event log, entity register, or unstructured numeric store.
2. **Continuous collection from the observed environment.** Measurements flow in on an ongoing basis from the systems under observation, through instrumentation/agents/exporters/integrations/platform-vended feeds, by push or pull, on a collection cadence the product operates. The data's subject is always the behavior of other systems. Remove → a passive database awaiting manual loads (BI/analysis territory), or an empty store.
3. **Time-and-dimension evaluation as the read loop.** Stored series are aggregated over time windows (rollup) and split/combined across identifying dimensions (group-by, arithmetic between series), and read primarily as time-oriented graphs and queries — the way users see state, change, and pattern over time. Remove → a raw telemetry archive or per-event inspector.
4. **The condition → alert watch loop.** Rules continuously evaluate series against defined conditions (thresholds, rates, computed expressions) and emit alerts — with notification routing, suppression/muting or hysteresis against noise, and recovery signaling — so out-of-bounds behavior surfaces to people instead of merely accumulating. Remove → a metrics warehouse / graphing system; the "monitoring" is gone.

Jointly-held load-bearing checks (all four have direct evidence in every sampled product, including the 1990s lineage):

- 1 alone = time-series database / spreadsheet
- 2 alone = telemetry pipeline / firehose
- 1+2 without 3 = raw metrics store (TSDB as component)
- 1+2+3 without 4 = data logging & graphing system (the RRDtool pole — storage and graphing without the watch loop; the recognized precursor, not the Type)
- 2+3+4 without 1 = in-flight stream alerting (stream-processing territory)
- 1+3+4 without 2 = analysis of imported data (BI workbench over series)

### L1 — Common Mature Structure

Cross-product commonality (Layer B), not definitional:

- **Metric type vocabulary** — gauge, counter/count, rate, histogram/distribution variants; types determine available graphing and functions (Datadog A; CloudWatch A; Prometheus type pages exist though detail not fetched).
- **A query language / query API** with time aggregation (always applied) and space aggregation (group by dimensions, arithmetic between series) — PromQL (A), Datadog query anatomy (A), CloudWatch PromQL API + SQL-flavored Insights (A), Mimir PromQL (A).
- **Derived/computed series** — recording rules (Prometheus A, Mimir A), metrics generated from log patterns (Datadog logs-to-metrics A), statistic sets (CloudWatch A).
- **Rich ingestion surface** — agents, exporters, integrations catalogs (Datadog "1,000+" A), OpenTelemetry as a converging vendor-neutral path (CloudWatch A explicitly; Prometheus guides A; Mimir A).
- **Dashboards and charting** as the primary read surfaces, with metric explorers/summaries listing actively reporting metrics and their metadata (Datadog A; CloudWatch console A; Prometheus Grafana/expression browser A; Mimir Grafana A).
- **Alert lifecycle management** — routing/notifications to people and channels, silencing/inhibition, downtime windows, hysteresis/flapping control, recovery notifications (Alertmanager A; Datadog monitors A; MRTG threshold machinery A; CloudWatch alarms A at overview level).
- **Retention horizons with coarsening over time** — CloudWatch 15 months with automatic rollup (A); query-time rollup (Datadog A); RRD round-robin aging (A). Exact horizons are product-specific.
- **Cardinality/volume management as an operational concern** — Datadog Metrics Summary/Metrics without Limits (A); CloudWatch's two-model split is explicitly framed around cardinality ("high-cardinality" vs "low-cardinality") (A). Feature names vendor-specific; the concern is common.
- **Self-monitoring packaging** — dashboards/alerts for the monitoring system's own health (Mimir A).
- **Multi-source, multi-shape deployment machinery** — HA, federation, remote write, multi-tenancy (Prometheus docs nav A; Mimir A).

### L2 — Variant / Optional Structure

- **Collection direction**: pull-based scrape (Prometheus A) vs agent-push with flush intervals (Datadog A) vs platform-vended + API push (CloudWatch A) vs remote-write backend (Mimir A). Mixed models coexist (Prometheus pushgateway A).
- **Series identity model**: name+labels (Prometheus/OTel A) vs namespace+name+dimensions (CloudWatch classic A) vs flat per-target identity (MRTG A). Historical check confirms identity attributes are the invariant, not any particular labeling scheme.
- **Business model / delivery**: free OSS toolkit (Prometheus), OSS scalable backend + support (Mimir), SaaS suite (Datadog), cloud-platform-native pay-per-use (CloudWatch). Pricing may meter series counts or ingest volume (CloudWatch A) — a variant, not a structure.
- **Scope emphasis**: machine-centric vs service-oriented vs business KPIs (Prometheus's own framing A; Datadog custom business metrics A) — the Type spans all of them; specialization by subject matter is a variant axis.
- **Cardinality posture**: low-cardinality classic model vs high-cardinality OTel model documented as two supported options in one product (CloudWatch A).
- **Standalone vs embedded**: metrics monitoring exists as a standalone product (Prometheus, Mimir, CloudWatch Metrics) and as a pillar inside broader observability/infrastructure suites (Datadog Metrics area). Both realizations observed; the pillar form is packaging, not a different Type.

### L3 — Vendor-specific Structure

(Research notes only — not for the canonical document.)

- Metrics without Limits™, DogStatsD, monitor template gallery, Monitor Quality page (Datadog).
- CloudWatch Metrics Insights (SQL), EMF (Embedded Metric Format), PutMetricData, per-metric-per-month pricing, namespace/dimension limits (30 dimensions), 150-label OTel limit, Query Studio.
- Pushgateway, Agent Mode, native histograms, federation, remote-write tuning, OpenMetrics specification (Prometheus).
- Tenant federation, Grafana Alloy as shipper, monolithic mode (Mimir).
- ThreshDir/ThreshHyst/ThreshProgI machinery, MaxBytes filtering, SendToGraphite (MRTG).

## Rejected Findings

- **"Metrics monitoring = TSDB."** Rejected: the sampled products all add collection-from-live-systems, the read loop, and the watch loop; a bare database is one component (Prometheus explicitly separates server/TSDB from rules/Alertmanager; Mimir is storage-first yet still ships rules and alerting). The TSDB-alone pole fails the L0 jointly-held check.
- **"Dimensional labels are definitional."** Rejected after historical check: MRTG's flat per-target identity and CloudWatch's namespace+dimensions both realize "identified series"; the abstract invariant is the individually identified series, not any specific labeling scheme.
- **"Alerting is optional."** Rejected: condition evaluation with alerts is documented in every sampled product including the 1990s anchor (threshold checking). Removing it leaves "data logging and graphing" — a recognized precursor category, not this Type.
- **"Metrics monitoring includes the watched-estate inventory"** (host lists, device registers, per-entity health states). Rejected: no sampled metrics product organizes on it; where Datadog provides one it is the separate Infrastructure Monitoring product area, and its own pass defined that as the sibling Type's core. Host/region appear here as *tag dimensions*, not as inventory records.
- **"15-month retention / specific rollup windows / specific metric-type sets are definitional."** Rejected as false precision: retention horizons and type vocabularies differ across products; only their existence is cross-product.
- **"Metrics monitoring is inherently about machines."** Rejected: sampled products explicitly extend to business KPIs (signups, logins, code commits) and arbitrary numeric series (weather, vending machines in the historical anchor).

## Boundary Findings

| Related Type | Seam | Test ("remove what → becomes the other") |
|---|---|---|
| Infrastructure Monitoring (processed) | Metrics monitoring holds and watches *series*; infrastructure monitoring organizes collection, health, and alerting around a *persistent entity inventory* of the watched estate with per-entity health/alert states. Products bundle both (Datadog's "Infrastructure Monitoring" is a separate product area whose monitors sit on the metrics layer). | Add a managed watched-estate inventory with per-entity health states on top → infrastructure monitoring. Remove it → metrics monitoring. |
| Log Management (processed) | Unit of record: individual timestamped *event records* inspected one-by-one (logs) vs numeric *series* evaluated over time (metrics). Metrics-from-logs derivation (Datadog logs-to-metrics A) is a one-way bridge: once the object is a derived numeric series with its own query/alerting, it has crossed into metrics monitoring. | Convert every record to a free-text/structured event inspected individually → log management. Aggregate events into named numeric series over time → metrics monitoring. |
| APM (processed) | APM centers request/operation-centric performance telemetry (latency/error/throughput per operation) of an instrumented application-service population, with drill-down into traces. Metrics monitoring is signal-generic (hosts, services, platforms, business) and organized purely on series; APM's per-service health views are an entity/service-centric layer. | Restrict the watched series to request/operation performance of instrumented services and add trace drill-down → APM. |
| Distributed Tracing (processed) | Spans assembled into per-request traces vs numeric series evaluated over time. | Replace series with request-path records → distributed tracing. |
| Observability Platform (§14, unprocessed) | Umbrella suite bundling metrics + logs + traces + APM + infra monitoring. Metrics monitoring is its metrics pillar — also shipped standalone (Prometheus, CloudWatch Metrics, Mimir). | Bundle all telemetry pillars under one suite → observability platform. |
| Network Monitoring (§14, unprocessed) | Network devices/links/flows/latency as the specialized subject and entity frame; metrics monitoring is subject-agnostic over any numeric series. Network measurements (interface counters etc.) land here as series. | Narrow the watched series to network-device/link telemetry with network semantics → network monitoring. |
| Synthetic Monitoring (§14, unprocessed) | Synthetic monitoring *produces* measurements from scripted probes; those measurements are consumed as series. Producer vs the series layer. | Make scripted probes the primary object → synthetic monitoring. |
| Capacity Management (processed) | Current/recent-state observation of series vs forward-looking supply-vs-demand projection and right-sizing decisions. Metrics monitoring feeds capacity management. | Add demand-vs-capacity projection and placement/right-sizing decision support → capacity management. |
| Dashboard Platform / BI (§13) | BI reads human-loaded/business datasets; metrics monitoring's data arrives continuously from observed systems and feeds a watch loop. Shared surface: charts. | Remove continuous collection + alerting; load curated business datasets → dashboard/BI platform. |
| Event Stream Processing / Stream Analytics (§13) | Processing in-flight streams vs storing, retaining, and evaluating series over historical windows. | Discard stored history; operate only on in-flight streams → stream processing. |
| Data Observability (§13, processed) | Subject matter: the health/quality of data pipelines and datasets; metrics monitoring's subject is any observed system's numeric behavior. | Restrict monitored series to data-pipeline quality indicators → data observability. |
| Industrial Historian / SCADA family (§16) | Structural cousin (plant numeric series, historian storage, graphing); industrial domain Types carry process-control semantics and protocols outside IT telemetry. | Add process-control/actuation and industrial protocol semantics → SCADA/Historian family. |
| Incident Management / On-call (§14) | Metrics monitoring ends at alert emission + routing; incident lifecycle (dedup into incidents, escalation policies, on-call schedules, postmortems) is the sibling's core. Alert output is the connective seam. | Take over incident lifecycle after the alert fires → incident/on-call management. |

## Uncertainties

- **Mimir depth**: only the documentation root was fetched. Claims about Mimir are held at structure level (ingest/query/recording rules/alerting rules/multi-tenant) with no page-level detail. No canonical claim depends on Mimir alone.
- **CloudWatch alarm mechanics**: alarms are confirmed at overview level (both models); per-alarm state machinery (OK/ALARM/INSUFFICIENT_DATA-style semantics) was not fetched and is deliberately not asserted.
- **Prometheus metric-type detail**: counter/gauge/histogram/summary names appear in documentation navigation; the type-semantics page was not fetched. Type vocabulary is asserted from Datadog (A) and CloudWatch (A); Prometheus's exact type list is not quoted.
- **Retention specifics**: only CloudWatch's 15-month rollup is directly documented; all other products' retention behavior is asserted only as "retained over bounded horizons, commonly coarsening over time."
- **Datadog monitor types**: the monitors overview confirms metric-based monitors and the alerting platform; the enumerated monitor-type taxonomy page was not fetched, so no precise monitor-type list is asserted.
- **Early-lineage breadth**: MRTG/RRDtool confirm the four L0 legs exist deep in the lineage, but whether threshold checking was universal in that era's tools (vs graphing-only tools like pure RRDtool use) was not surveyed beyond these two anchors. RRDtool itself is storage+graphing (no watch loop) and is treated as the precursor pole, consistent with the L0 jointly-held check.
- **Growth of OTel convergence**: CloudWatch's documentation presents OpenTelemetry as the recommended path; the direction is observed in-sample, but the end-state of the market is not asserted anywhere in the canonical document.

## Final Synthesis

A Metrics Monitoring application is the operations team's numeric-series watch system: it continuously collects numeric measurements from the systems under observation, stores each metric as a persistent time series individually identified by name and identifying attribute values, lets users read behavior over time through windowed and dimensional aggregation rendered as graphs and queries, and continuously evaluates the series against defined conditions, emitting alerts routed to people — with noise control and recovery signaling — so out-of-bounds behavior surfaces rather than merely accumulates.

The Type is deliberately subject-agnostic: the same four structures carry host CPU, service error rates, queue depths, platform quotas, and business KPIs like signups. What it does not carry is equally defining: no per-event record inspection (logs), no request-path records (tracing), no watched-estate inventory with per-entity health states (infrastructure monitoring), no forward-looking capacity projection, no incident lifecycle after the alert fires.

The definition survives the historical check: the 1990s MRTG+RRDtool lineage realizes all four defining structures (scheduled SNMP/script collection, identified per-target series, graphs, threshold checking with mail/recovery/hysteresis) with no labels, no cloud, no SaaS, and no cardinality machinery — so none of those belongs in the defining core. The definitional core is small; everything else modern products do — metric types, query languages, recorders, cardinality control, OTel convergence — is mature common structure layered on top.
