# Research Notes — Log Management

- Slug: log-management
- Leaf: Log Management (DIRECTORY.md §14 IT, Cloud & Infrastructure)
- Research date: 2026-09-08
- Methodology: update-v1 (WORKFLOW_v1.1 + WRITING_GUIDE_v1.1)

---

## Research Goal

Understand, from real products' official operational documentation, what a Log Management application actually is: its unit of record, its core pipeline, the interaction loop users run, its lifecycle and rules (retention, volume, access), and — critically — how it is distinguished from the dense cluster of neighboring observability/monitoring Types already documented in §14 (Infrastructure Monitoring, APM, Distributed Tracing, Incident Management) and its unprocessed neighbors (Metrics Monitoring, Observability Platform, SIEM, Error Tracking Platform).

## Initial Boundary (hypothesis before research)

Log Management was hypothesized to sit at the center of a crowded seam:

- vs **Metrics Monitoring**: numeric time series vs individual event records?
- vs **Distributed Tracing**: causally assembled per-request span trees vs independent event records?
- vs **APM**: request/operation performance telemetry vs general-purpose event corpus?
- vs **Infrastructure Monitoring**: per-entity health states vs raw event records with no entity-of-record?
- vs **SIEM**: security-purpose analytics over the same substrate?
- vs **Error Tracking Platform**: exceptions grouped into issues vs raw records?
- vs **Observability Platform**: umbrella suite unifying multiple signals vs the log pillar itself?
- vs **Event Stream Processing Platform**: processing data in motion vs storing records for retrieval?

## Research Questions

- RQ1: What exactly is a "log" in these products — what is the unit of record and its structure?
- RQ2: How do logs get in — what collection machinery exists, and from what kinds of sources?
- RQ3: What processing happens between arrival and retrieval (parsing, field extraction, enrichment, routing)?
- RQ4: How is the corpus stored and organized — indexes, partitions, tiers, retention, archives?
- RQ5: What is the primary interaction loop — what does the user actually do all day?
- RQ6: What output surfaces exist beyond search (dashboards, alerts, reports, forwarding)?
- RQ7: What rules/constraints shape the system — volume economics, retention bounds, access control, sensitive data?
- RQ8: Where is the boundary against each neighboring Type, and does the market itself respect it?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer levels + different deployment postures:

| Product | Philosophy / posture | Customer tier |
|---|---|---|
| Splunk | search-first enterprise "data platform" (proprietary query language, on-prem + cloud) | large enterprise |
| Elastic (Observability) | open-source-rooted self-hostable stack, now also cloud | mid-market → enterprise |
| Graylog | open-source log-management pure-play (streams/alerts orientation) | SMB → mid-market |
| Datadog | SaaS observability suite, logs as one pillar, tightly coupled to metrics/traces | cloud-native mid → enterprise |
| Sumo Logic | cloud-native SaaS log analytics (Collector/Source model) | mid → enterprise |

Coverage check: ingestion-heavy (Splunk, Elastic, Sumo), suite-pillar (Datadog), pure-play (Graylog), open-source self-hosted (Elastic, Graylog), SaaS (Datadog, Sumo, Splunk Cloud). Historical/market-breadth reasoning done in the Historical Check below.

## Sources

All fetched 2026-09-08. Tier-1 (official operational documentation) except where noted.

- Datadog — Log Management docs overview — https://docs.datadoghq.com/logs/ (fetched)
- Splunk — Splunk Enterprise documentation landing (manual index incl. Getting Data In, Forwarding Data, Search Manual, Alerting, Dashboards, Knowledge Manager, Indexers, Distributed Deployment, Securing Splunk) — https://docs.splunk.com/Documentation/Splunk (fetched)
- Splunk — Search Tutorial ("About the Search Tutorial") — https://docs.splunk.com/Documentation/Splunk/8.2.12/SearchTutorial/WelcometotheSearchTutorial (fetched; first two URL attempts 404'd, resolved via docs landing)
- Elastic — Log monitoring (Elastic Observability solutions docs) — https://www.elastic.co/docs/solutions/observability/logs (fetched; first URL guess 404'd)
- Graylog — Documentation portal (nav/index across all product areas) — https://docs.graylog.org/ (fetched; deep-page host go2docs.graylog.org is JavaScript-login-walled — page bodies not accessible)
- Sumo Logic — Log Search docs — https://help.sumologic.com/docs/search/ (fetched)

Source-access limitations recorded:
- Graylog: individual doc pages blocked by JS login wall; observations limited to the documentation portal's structure and section naming (which is itself detailed and product-representative). All Graylog-specific claims kept at structure-level strength.
- Splunk: newer-version docs moved to help.splunk.com (not fetched); legacy docs.splunk.com pages used. Splunk retention-policy specifics not directly fetched — retention claims for Splunk kept weak (implied by index-management documentation).
- No pricing, quota, or numeric-limit pages were fetched; no precise operational numbers are asserted anywhere in this research or the final document.

---

## Product Observations

### Splunk

Evidence layer: A (direct, docs.splunk.com)

- Positioning (docs landing): "Splunk Enterprise is the data collection, indexing, and visualization engine for operational intelligence." Product suite spans Platform (Cloud Platform, Enterprise), Security (Enterprise Security/SIEM, SOAR, UBA), Observability (Infrastructure Monitoring, APM, ITSI). Log management is the platform's base substrate rather than a separately branded product area.
- Ingestion: "Getting Data In" manual — "How to get your machine data into your Splunk deployment and ensure that it is indexed efficiently and effectively." "Forwarding Data" manual — forwarders (Universal Forwarder is a dedicated, separately documented product) to get data into the deployment.
- Storage organization: "Managing Indexers and Clusters of Indexers" — indexes and indexers; distributed deployment manual separates forwarders, indexers, search heads as roles; workload management; capacity planning.
- Search as primary interface: Search & Reporting app is "the primary interface for using the Splunk software to run searches, save reports, and create dashboards." Search Tutorial flow: add data → search → use fields → use the search language (SPL) → subsearches → enrich events with lookups → create reports and charts → create dashboards. Time range picker is a dedicated tutorial part ("Specifying time ranges") — time-anchored search.
- Knowledge layer: Knowledge Manager Manual — "event types, tags, lookups, field extractions, workflow actions, reports, views, and data models" — i.e., structure extracted from events is itself a managed, curated asset.
- Outputs: Alerting Manual ("alerts that are triggered when specific conditions are met"), Dashboards and Visualizations, Reporting (scheduled reports, PDF printing), Pivot (no-code tables/charts), Analytics Workspace (browse/analyze without SPL).
- Administration: Securing Splunk Enterprise ("create, manage, and authenticate users… use audit features"), REST API, Splunkbase apps/add-ons ecosystem.

### Elastic (Observability — logs)

Evidence layer: A (direct, elastic.co/docs)

- Positioning: "deploy and manage logs at a petabyte scale… search across your logs in one place, troubleshoot in real time, and detect patterns and outliers with categorization and anomaly detection."
- Ingestion tools (four documented options): Elastic OpenTelemetry collector/SDKs ("collecting logs, metrics, and traces"); Elastic Agent (Fleet-managed or standalone, integrations "to ingest logs from Kubernetes, MySQL, and many more data sources"); Filebeat — "a lightweight shipper for forwarding and centralizing log data… monitors the log files or locations that you specify, collects log events, and forwards them to your Observability project for indexing"; Logstash — "a powerful data processing pipeline that can collect, transform, and enrich log data before sending to Elasticsearch… parse, filter, and transform logs before indexing… collect logs from various sources and normalize them… routing to multiple destinations."
- Storage configuration: data streams — "efficiently store append-only time series data in multiple backing indices partitioned by time and size"; mapping ("define how data is stored and indexed"); index lifecycle management — "configure the built-in logs policy based on your application's performance, resilience, and retention requirements."
- Processing: ingest pipelines — "parse and transform log entries into a suitable format before indexing."
- Retrieval: Discover — "search, filter, and tail all your logs ingested into your project in one place"; "Discover and explore all of the log events flowing in from your servers, virtual machines, and containers in a centralized view"; data views scope queries to specific datasets/namespaces.
- Analytics: filter and aggregate logs; pattern analysis on unstructured log messages; ML anomaly detection over logs.
- Quality control: Data Set Quality page — "get an idea of your overall data set quality, and find data sets that contain incorrectly parsed documents."
- Alerting: log threshold rule — "send an alert when the log aggregation exceeds a threshold."

### Graylog

Evidence layer: A (structure-level; page bodies behind JS login wall — see Sources limitation)

Documentation portal structure (naming is Graylog's own):

- Ingestion: "Create an Input" (Inputs, Secure Inputs with TLS); "Manage Log Collectors" (install Sidecar, deploy collectors).
- Routing/processing: "Route Logs with Graylog" — Streams and Pipelines; "Build Custom Pipeline Rules" (rule logic, pipeline functions).
- Storage: "Configure Index Sets" — Index Model, Data Tiering, Index Set Templates.
- Retrieval: "Write Search Queries" (Search Your Log Data, Search Scripting API); "Customize and Save Searches" — Decorators, Saved Searches, Search Configuration, Search Parameters, Search Filters, Message Summary Templates.
- Outputs: Widgets and Dashboards; Reports ("Create and Edit Reports", Export Search Results); "Define Events" (Event Definitions, Correlation Engine); "Set Up Alerts" (Alerts, Alert Types); Investigations.
- Long-term storage: "Set Up a Data Lake" (S3/GCS/Azure Blob backends, Data Routing).
- Security extension: Graylog Security — Security Events, Sigma Rules, Risk Scores, Asset Enrichment, Vulnerability Scanning.
- Administration: Permission Management, Users and Teams, SSO, REST API.

### Datadog (Log Management)

Evidence layer: A (direct, docs.datadoghq.com)

- Positioning: "Datadog Log Management… enables you to cost-effectively collect, process, archive, explore, and monitor all of your logs." Verb chain itself: collect → process → archive → explore → monitor.
- Volume philosophy: "removes these limitations by decoupling log ingestion from indexing" ("Logging without Limits") — ingest everything, choose what to index; "intuitive archiving to support your security and IT teams during audits and assessments."
- Ingestion: "Begin ingesting logs from your hosts, containers, cloud providers, and other sources."
- Processing: "process and enrich all your logs with pipelines and processors."
- Storage/cost: "provide control of your log management budget with indexes"; "manage your logs within storage-optimized archives"; "generate metrics from ingested logs."
- Exploration (Log Explorer): Search ("search through all of your logs"), Live Tail ("see your ingested logs in real time across all your environments"), Analytics ("perform Log Analytics over your indexed logs"), Patterns ("spot log patterns by clustering your indexed logs together"), Saved Views ("automatically configure your Log Explorer").
- Correlation: "Connect your logs and traces"; "Correlate your logs and metrics" — logs as one pillar among observability signals.
- Security extension: "Logging without Limits also powers Datadog Cloud SIEM, which detects security threats in your environment, without requiring you to index logs."
- Learning Center course covers: "log collection, querying, analytics, metrics, monitoring, processing, storage, and access control."

### Sumo Logic

Evidence layer: A (direct, help.sumologic.com)

- Positioning: "Log Search allows you to query and analyze log data sent to Sumo Logic."
- Ingestion: docs nav section "Collectors, Sources" (send-data); Live Tail defined as "Real-time live feed of log events associated with a Source or Collector" — the Collector/Source model is the ingestion vocabulary. "Journey of a log" micro-lesson: "the ingestion pipeline and the journey that a log message takes from collection into the Sumo Logic platform… turning a raw event into a schema and then into actionable insights."
- Storage organization: "Logs collected by Sumo Logic are indexed in Partitions and Scheduled Views." Partition — "stores your data in an index separate from the rest of your account data so you can optimize searches, manage variable retention, and specify certain data to forward to S3 or GCS." Data Tiers — Continuous/Frequent/Infrequent. Archive — "forward log data from Installed Collectors to Amazon S3 buckets to collect at a later time." Internal indexes: Health Events, Archive, Audit, Volume (Data Volume Index — visibility into how much data is being sent, to "fine tune your data ingest with respect to the data plan for your Sumo Logic subscription").
- Search: Search Query Language; LogReduce, LogCompare, LogExplain; Lookup Tables; Subqueries; Time Compare; search autocomplete; partitions to "optimize search performance… for forensic analysis and log management."
- Outputs: Dashboards and Alerts (top-level nav sections), Terraform resource for search provisioning ("sumologic_log_search").
- AI assistance: Mobot — "ask Mobot a question in plain language to analyze your logs… no query writing required."
- Broader platform nav: Metrics, Traces/RUM/APM, Security, Observability — Sumo is also a multi-signal platform with logs as one nav pillar.

---

## Cross-product Comparison

| Aspect | Splunk | Elastic | Graylog | Datadog | Sumo Logic | Strength |
|---|---|---|---|---|---|---|
| Unit of record | event | log entry / document | message | log event | log message/event | B: 5/5 (concept identical, naming varies) |
| Multi-source collection | forwarders, inputs ("machine data") | Agent, Filebeat, Logstash, OTel | Inputs + Sidecar collectors | Agent, hosts/containers/cloud | Collectors + Sources | B: 5/5 |
| Central store, time-organized | indexes | data streams (append-only, time-partitioned) | index sets + data tiering | indexes + archives | partitions + tiers | B: 5/5 |
| Processing/parsing layer | field extractions, knowledge objects | ingest pipelines | pipelines + (extractors) | pipelines + processors | pipeline ("journey… raw event into a schema") | B: 5/5 |
| Time-anchored search UI | Search app + time range picker | Discover | search + filters + parameters | Log Explorer | Log Search | B: 5/5 |
| Live tail | not directly fetched | "tail all your logs" (Discover) | — | Live Tail | Live Tail | B: 3/5 direct |
| Aggregation/analytics | stats/reports/charts, Pivot | filter+aggregate, pattern analysis | widgets/aggregations | Analytics, Patterns clustering | LogReduce/LogCompare | B: 5/5 |
| Retention management | index management (retention implied, not directly fetched) | ILM "retention requirements" | data tiering, index sets | indexes (budget) + archives | partitions "variable retention", tiers | B: 4/5 direct |
| Dashboards | Dashboards/Studio | (platform-level) | Dashboards/Widgets | (suite-level) | Dashboards | B: direct 3+, common |
| Alerting on log conditions | Alerting Manual | log threshold rule | Event Definitions + Alerts | monitors (suite) | Alerts nav | B: 5/5 |
| Export/archive-out | — (not fetched) | ILM-based | Data Lake (S3/GCS/Azure) | archives | forward to S3/GCS | B: 4/5 direct |
| Trace/log correlation | (suite-level) | OTel signal collection | — | connect logs & traces | "Open Trace" from search results | B: 3/5 direct |
| Metrics-from-logs | — | — | — | "generate metrics from ingested logs" | Scheduled Views pre-aggregation (related) | A: product-leaning (Datadog explicit) |
| Security/SIEM extension | Enterprise Security | — | Graylog Security (Sigma, risk scores) | Cloud SIEM | Security nav | B: 3/5 common extension |
| AI query assistance | AI Assistant for SPL (product list) | — | — | — | Mobot | A: 2/5, era-current |
| Data-quality views | — | Data Set Quality page | — | — | Volume/Health indexes (adjacent) | A: product-leaning (Elastic explicit) |
| RBAC/admin | Securing Splunk (users, audit) | (platform-level) | Permission Management, Users/Teams | access control (course topics) | Manage Account nav | B: common in enterprise posture |

Reading: the first eight rows are the Type's spine — present in all five sampled products with conceptually identical roles. Rows below the spine are common/optional extensions whose presence varies with posture (suite vs pure-play, security-leaning vs ops-leaning).

---

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant (three jointly-held structures)

1. **Multi-source collection of operational event records.** The system continuously gathers timestamped log records (log entries) emitted by other software systems, machines, and services — sources it does not itself own — through collection machinery (agents/collectors, file shippers, syslog/network receivers, HTTP/API endpoints, cloud-service integrations). Remove it → there is nothing to manage; a standalone shipper/forwarder is not log management.
2. **A centralized persistent store that organizes the accumulated record corpus for retrieval.** Entries are attributed to their source, organized by time, held persistently with retention, and physically organized for query (indexed or scannable). Remove it → the system is a pass-through forwarder or an ephemeral tail with no history; the corpus is the system of record for "what happened, when, where."
3. **Search and examination over the corpus as the primary interaction.** Users query by time range plus source/content/field filters, inspect individual entries, and aggregate (counts, groupings) — this retrieval loop is the product's defining surface. Remove it → the system is an archive dump with no application; a search engine over nothing is not log management either.

Jointly-held is load-bearing:
- 1 alone = shipper/forwarder (vendor docs themselves position Filebeat-class tools as "forwarding and centralizing… forwards them for indexing" — i.e., enablers of leg 1, not the whole Type)
- 2 alone = object-store bucket of rotated files / data lake
- 3 alone = a search engine with no ingestion
- 1+2 without 3 = compliance archive with no retrieval application
- 2+3 without 1 = manual imports; no ongoing operational corpus
- 1+3 without 2 = ephemeral tail service, no history to investigate

Deliberately NOT in L0 (per the historical check below): indexing per se (syslog-era satisfied leg 2 by organized files + grep), parsing/structuring (raw-text search suffices), dashboards, alerting, retention tiers, RBAC, correlation, AI.

### L1 — Common Mature Structure (present across the sampled population; not definitional)

- **Processing/normalization layer** — parse, extract fields, enrich, route at ingestion (ingest pipelines, processors, pipeline rules, field extractions; structure-as-curated-asset in Splunk's knowledge objects). Present 5/5.
- **Retention management and storage tiering** — per-index/partition/stream retention, hot/warm/cold-class tiers, archiving, forwarding out to object storage. Present 4/5 direct (Splunk implied).
- **Aggregation & analytics** — counts/groupings, pattern clustering, reduce/compare operators. 5/5.
- **Dashboards** — 3/5 direct product docs; suite products embed.
- **Alerting on log conditions** — threshold rules, event definitions. 5/5.
- **Saved searches / views** — saved views (Datadog), saved searches (Graylog, Splunk reports), search configuration (Graylog). 4/5 direct.
- **Reporting/export** — reports, search-result export. 2/5 direct; common in enterprise posture.
- **Log↔trace/metrics correlation** — 3/5 direct; common in suite products.
- **RBAC and audit** — enterprise posture; 2/5 direct documentation, universally claimed by the category.
- **Ingestion health & volume observability** — Sumo Health/Volume indexes, Elastic Data Set Quality. 2/5 explicit; the concern is common.

### L2 — Variant / Optional Structure

- **Deployment posture** — self-hosted stack (Splunk Enterprise, Elastic, Graylog) vs SaaS/cloud-native (Datadog, Sumo, Splunk Cloud) vs open-source core + commercial edition (Elastic, Graylog).
- **Packaging posture** — standalone pure-play (Graylog) vs pillar of an observability suite (Datadog, Sumo, Elastic Observability, Splunk Observability) vs platform substrate for security products (Splunk ES, Datadog Cloud SIEM, Graylog Security — the same log corpus extended with security analytics).
- **Indexing philosophy** — full-text indexing (classic) vs metadata/label-only vs decoupled ingest-and-index (Datadog's "Logging without Limits"). Products differ in what portion of the record is indexed and when.
- **When structure is extracted** — before storage (Elastic ingest pipelines, Datadog processing) vs at query time or as later-curated knowledge (Splunk field extractions, Elastic data-set-quality remediation). Products differ; the capability, not the timing, is common.
- **Query-language style** — proprietary pipeline language (SPL, Sumo) vs boolean/field syntax (Elastic, Datadog, Graylog) vs plain-language AI assistants (Sumo Mobot, Splunk AI Assistant for SPL — era-current).
- **Scale/pricing posture** — pricing models and volume levers differ by product (not researched in detail; no numeric claims made).
- **Protocol heritage** — syslog remains a named input class across products; OTel is the era-current collection standard (Elastic OTel collector, Splunk OTel add-on).
- **Compliance/audit retention emphasis** — archiving "to support your security and IT teams during audits" (Datadog); audit indexes (Sumo).

### L3 — Vendor-specific Structure (stays in Research Notes)

- Splunk: SPL; Universal Forwarder; forwarder/indexer/search-head role separation; Splexicon; Splunkbase apps; buckets.
- Elastic: Fleet, Elastic Agent, Filebeat, Logstash as named components; data streams/data views naming; `logs@custom` template.
- Graylog: Streams vs Pipelines as routing/processing vocabulary; Sidecar collector; Illuminate; Sigma-rule support as branded security layer.
- Datadog: "Logging without Limits" trademark; Log Explorer, Patterns clustering; Forager-class internals not researched.
- Sumo Logic: Collector/Source model; Partitions/Scheduled Views; LogReduce/LogCompare/LogExplain; Mobot; Data Volume Index.

### Rejected Findings (considered, then rejected as non-definitional)

- "Logs must be indexed" — rejected: syslog-era management predates indexing; leg 2 worded as "organized for retrieval," not "indexed."
- "Alerting is core" — rejected: absent from the pre-modern Type; all five have it, but as an output extension.
- "Dashboards are core" — rejected: reporting surface, not the defining structure.
- "Log management = SIEM input" — rejected: security is an extension posture; the general-purpose operational corpus is the Type.
- "Log management is inherently a suite pillar" — rejected: Graylog and classic ELK stacks prove the standalone form; packaging is variant.
- "Full-text search of message text is core" — weakened: search by time+source+metadata suffices for the Type; text-search depth is an implementation grade. (Kept inside leg 3 as "content/field filters" — content filter is core; full-text index machinery is not.)

---

## Historical / Market-Sample Check

Question: would older, regional, platform-native products still fit the three-leg definition?

- **Syslog-era central logging** (syslogd/rsyslog/syslog-ng on a central host): collects timestamped records from many networked machines (leg 1), stores them centrally in organized files with rotation/retention (leg 2), supports examination via grep/awk/scripted queries over time-and-host-organized files (leg 3). Satisfies all three legs with zero modern machinery. (C-layer canonical inference — conceptual, no single product fetch.)
- **ELK-class stacks** (shipper + search-engine store + KQL UI), the pre-SaaS standard pattern: exactly the three legs as three cooperating components. Confirmed directionally by Elastic's own component documentation (Filebeat "forwards… for indexing"; Logstash "collect, transform, enrich… before sending to Elasticsearch"; Discover as the view).
- **Splunk itself** frames the Type's origin as "machine data" search — collection + indexing + visualization, 2000s-era vocabulary, no cloud/AI/OTel.
- Modern additions (decoupled ingest/index, ML anomaly detection, AI assistants, SIEM extensions, petabyte SaaS scale) are all era machinery absent from the older forms — none belongs in the definition.

The definition does not over-fit the current SaaS observability market.

---

## Boundary Findings

1. **vs Metrics Monitoring (§14, unprocessed)** — sharpest unit-of-record seam: log management's unit is the individual timestamped event record (text/structured payload, inspected one-by-one); metrics monitoring's unit is the numeric time series (aggregated measurement, evaluated over time). Log products can *derive* metrics from logs (Datadog explicit; Sumo Scheduled Views pre-aggregation) — derivation is precisely the seam: once the object is a numeric series with its own query/alerting, it has crossed into the sibling Type. "Remove what": remove event records in favor of numeric series → metrics monitoring; keep records but drop the store/search application → forwarder. FLAG for the metrics-monitoring pass.
2. **vs Distributed Tracing (§14, processed)** — consistent with the DT pass: traces causally assemble spans of one request across services (propagation IDs stitch them); log records are independent events, at best correlated via IDs (L1). A log backend has no causal assembly requirement; a tracing backend has no general-corpus search mandate. Boundary held; no flag.
3. **vs APM (§14, processed)** — consistent with the APM pass: APM centers request/operation performance telemetry and service health with drill-down into traces; log management centers the general event-record corpus from *any* source (system, security device, network, cloud service — not only instrumented application services). APM pass already records cross-telemetry correlation (logs) as L1 — seam symmetric. Boundary held.
4. **vs Infrastructure Monitoring (§14, processed)** — infra monitoring centers a monitored-entity inventory with per-entity health/alert states; log management has no entity-of-record: sources are attributions on records, not managed inventory records with health states. The same server appears in both products as different objects (monitored entity vs log source). Boundary held; no flag.
5. **vs Observability Platform (§14, unprocessed)** — the umbrella-suite Type (unifying metrics/logs/traces) vs the log pillar. All suite vendors in-sample sell "logs" as a product area whose capability is exactly this Type; the suite's defining property (cross-signal unification) is not log management's. FLAG for the observability-platform pass: do not define that Type by any single pillar.
6. **vs SIEM (§15, unprocessed)** — same substrate, different purpose layer: vendors themselves build SIEM on log management (Splunk ES on Splunk; Datadog Cloud SIEM "powered by" log ingestion "without requiring you to index logs"; Graylog Security with Sigma rules/risk scores). The seam is the security analytics/detection/investigation layer, not storage or search. FLAG for the SIEM pass: log storage/search should not be treated as SIEM-defining.
7. **vs Error Tracking Platform (§12, unprocessed)** — error tracking centers exceptions grouped/deduplicated into issues with release context; log management stores raw event records without issue grouping. Grouping is the seam. FLAG for that pass.
8. **vs Event Stream Processing Platform (§13, unprocessed)** — processing data in motion (continuous transformation/routing of streams) vs persisting records for retrieval; many log pipelines *use* stream processors (Logstash described as a "data processing pipeline"), but the log system's terminus is the retrievable corpus. Reasoned from Type logic; no flag.
9. **vs Data Lake Platform (§13, unprocessed)** — a lake stores arbitrary data without the operational log loop (source-aware collection machinery, log-shaped exploration, log-shaped retention tiers); some log products offer "Data Lake" backends (Graylog) as storage extension. Reasoned from Type logic; no flag.

Boundary phrase for the final document (the "remove what" judgment): *remove the event-record store and its search application → you are left with a metrics system, a tracer, or a forwarder; remove multi-source collection → a search engine over nothing; remove nothing but narrow the purpose to security detection → SIEM; widen the scope to unify all signals → observability platform.*

## Uncertainties

- Precise retention defaults, index-sizing limits, ingestion quotas, pricing models: not researched; deliberately absent from both documents.
- Graylog page-level operation (stream creation mechanics, extractor UI detail): blocked by JS login wall; Graylog evidence is structure-level only.
- Splunk retention and indexing internals (buckets, TSIDX): implied by manual titles, not directly fetched; kept weak.
- Whether the market treats "log analytics" / "log observability" / "log management" as distinct categories: treated here as naming variance over one Type (the documented verb chains — collect/process/store/search/alert — are the same across labelings).
- Live tail in Graylog and Splunk: not directly evidenced in fetched material; not asserted for them.

## Final Synthesis

Log Management is the operational event-record system of record: it continuously collects timestamped log records from many external sources into one centralized, time-organized, source-attributed store, and it makes that corpus retrievable and examinable through time-anchored search as its primary interaction. Everything else the sampled products carry — parsing/enrichment pipelines, retention tiers and archives, aggregation and pattern analytics, dashboards, alerting, correlation, RBAC, AI assistance, security extensions — is mature common structure or posture-dependent variant, not the definition. The Type's identity is held by the jointly-held triple (collect from many sources; keep the corpus; search and examine it), which syslog-era, ELK-era, and SaaS-era implementations satisfy equally.
