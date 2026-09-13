# Research Notes — Data Observability Platform

Research date: 2026-09-07
Methodology: WORKFLOW v1.1 / WRITING GUIDE v1.1
Sibling context used: data-catalog (processed 2026-09-07), data-lineage-platform (processed 2026-09-07 — recorded seam "lineage = blast radius, observability = failing node"), data-governance-platform (processed — flagged capability seams vs data-quality-platform), data-integration-platform (processed — custodian-not-owner posture).

---

## Research Goal

Understand what a Data Observability Platform actually is as an Application Type: what objects exist inside it, how it watches data it does not own, what its operational loop is (detect → triage → resolve), which structures are defining vs merely common in the current market, and where its boundaries lie against the neighboring §13 Types (Data Quality Platform, Data Lineage Platform, Data Catalog, ETL/ELT Platform) and the §14 Observability Platform name-collision.

## Initial Boundary (Step 1 hypothesis)

- **What is it?** A platform that continuously watches the health of an organization's data and data pipelines (freshness, volume, schema, distribution, quality) and manages detected problems to resolution.
- **Who uses it?** Data engineers, analytics engineers, data platform teams; secondary: analysts and BI consumers who receive incident communication.
- **Nearest Types:** Data Quality Platform (rules/tests as primary object), Data Lineage Platform (flow graph as primary object), Data Catalog (inventory + discovery), Observability Platform §14 (software telemetry — name collision, different object), ML Model Monitoring (model performance vs data health), ETL/ELT Platform (movement vs watching), DataOps Platform.
- **Probable boundary test:** observability = ambient runtime health + incident loop over the estate; quality = defined expectations/rules as the primary object; lineage = structure of flows; catalog = descriptive inventory.
- **Unknowns:** whether the "incident" is a defining structure or only a common one; whether ML anomaly detection is definitional (some products are rules-first); whether catalog/lineage embedding collapses this Type into a suite sibling.

## Research Questions (Step 2)

1. What are the core objects? (assets, monitors/checks, metrics, issues/incidents)
2. How does the platform observe data it does not own? (agent vs agentless, query-based metadata collection, log parsing)
3. Which health dimensions are monitored, and are they canonical or vendor framing?
4. How are anomalies detected — learned baselines vs defined rules — and can both be first-class?
5. What is the issue/incident lifecycle and who works it?
6. How does lineage interact (impact analysis, incident grouping, affected dashboards)?
7. What notification/integration machinery exists?
8. What governance (roles, teams, ownership, SSO) matters?
9. Where do catalog, glossary, and CI/CD capabilities sit — core, common, or variant?
10. Boundary: what must be removed to land in each neighboring Type?

## Representative Products (Step 3)

| Product | Positioning | Segment / philosophy | Evidence tier |
|---|---|---|---|
| Bigeye | "Enterprise-grade data observability platform" — metrics/anomaly detection + rules + reconciliation + incident management | Enterprise, metric-first with rules complement | Tier-1 docs (A) |
| Metaplane | "Know when things break, what went wrong, and how to fix it" — warehouse-first, fast setup, ML anomaly detection with feedback | SMB/mid-market, monitors+incidents, lineage-centric | Tier-1 docs (A) |
| Sifflet | "Full Data Stack Observability Platform" — dependencies mapped across the whole data life cycle, ingestion → BI | Mid-market/enterprise, governance-flavored, embedded catalog | Tier-1 docs (A) |
| Anomalo | "Autonomous data quality monitoring / self-driving data" — no-code, ML-driven, enterprise verticals | Enterprise, no-code pole | Tier-2 product pages (B) |
| Monte Carlo | Category-creating incident-centric observability platform | Enterprise | **Unreachable** (403/transport ×2) — excluded from claims |

Monte Carlo selection was desirable (category origin, incident-first philosophy) but docs.montecarlodata.com and docs.montecarlodata.com/ both failed; per the source-access rules it was dropped rather than retry-looped, and no Monte Carlo claims appear anywhere in this pass.

## Sources

- Bigeye — https://docs.bigeye.com/docs (What is Bigeye?), llms.txt index, /docs/metrics, /docs/issues (Triaging an Issue), /docs/incidents (Declaring an Incident), /docs/scorecard — fetched 2026-09-07
- Metaplane — https://docs.metaplane.dev/docs (Welcome), llms.txt index, /docs/monitor-types, /docs/incidents — fetched 2026-09-07
- Sifflet — https://docs.siffletdata.com/docs (Overview), llms.txt index, /docs/incidents — fetched 2026-09-07
- Anomalo — https://www.anomalo.com/ (homepage/product menu), https://docs.anomalo.com/docs (redirects to marketing site; operational docs unreachable) — fetched 2026-09-07
- Sibling research notes: research/data-lineage-platform.md §Boundary Findings; research/data-catalog.md; STATUS.md boundary entries

---

## Product Observations (Step 4 — evidence-tagged)

### Bigeye (A — directly observed from official docs)

- Positioning: "enterprise-grade data observability platform… combines data lineage, anomaly detection, data quality rules, data reconciliation, incident management, and other tools into a single platform that creates complete visibility into data pipeline performance and quality."
- Category framing (vendor-stated): traditional data quality tools are "rooted in rules that must be hand written and manually updated"; data observability "uses dynamic metadata including continuous data profiling, data lineage, and other monitoring techniques… to detect both previously known, and never before seen types of problems."
- **Unit of measurement**: "Where in traditional data quality tools, a 'rule' is the most common unit of measurement, in data observability the most common unit is a 'metric'. It is a statistic that is calculated over the data which can then be tracked as a time series." Examples: average of a column, percent of null rows.
- **Connection layer**: data sources connected agent-based (Docker/K8s-deployed agents: data-source agent, lineage agent, data-health agent for external catalogs, sensitive-data scanning agent, cross-source agent, external-monitors agent for dbt tests) or agentless; warehouses/databases (Snowflake, BigQuery, Databricks, Redshift, Oracle, Teradata, DB2, SAP HANA…), BI connectors, ETL connectors (Informatica PowerCenter, DataStage, SSIS, Matillion, SnapLogic, ADF), dbt Core/Cloud.
- **Catalog surface**: "see all data sources you have connected" — catalog with popularity, schema change detection, business glossary, table preview, asset linking, favorites, tags.
- **Monitoring machinery**: Metrics (autothresholds — "get alerted when metrics move outside of their expected bounds" — or custom/manual thresholds); Freshness & Volume ("pipeline reliability"); data profiling; grouped metrics; row creation time; scheduled runs; templates.
- **Rules complement**: custom rules, custom SQL rules, join rules ("augment your metrics with custom rules… complex and unique business logic"); referential integrity guide.
- **Deltas**: compare similar datasets to validate replication, migration, or model code changes (product-specific framing).
- **Issues**: "An issue is generated when a metric starts alerting… every subsequent run that falls outside of threshold bounds while an issue is still open is an alert on that issue." Alerts related to the same metric aggregate into a single issue; status manage: acknowledge, resolve, close; mark alerts good/bad to improve anomaly detection; notes on closed issues; related issues; lineage view; debug query (metric query + debug rows in the source).
- **Incidents**: "Incidents combine multiple issues together into a single object with a common root cause." "Issues represent individual symptoms observed on specific columns and tables; Incidents represent underlying root causes." Merge/unmerge issues; incident status/assignee propagate to all member issues; incident priority = highest member priority; downstream-impacted issues auto-suggested for merging ("Bigeye automatically traces your lineage graph for issues that are directly impacted by a given issue"); comments posted to the incident timeline go to all associated notification channels.
- **Impact analysis**: "Instantly understand the impact of problems" — lineage-driven; deploying monitoring with lineage ("instantly monitor all upstream dependencies from any target asset").
- **Notifications**: Slack, email, MS Teams, webhooks, Jira, ServiceNow, PagerDuty, Azure Boards; failed-monitor notifications (monitor itself errored).
- **Health surfaces**: Scorecard — per data dimension, historical bars green (monitors deployed, no true-positive issues) / red (true-positive issues opened) / grey (no monitors); current scorecard = % metrics healthy with red/yellow/green bands; "true positive" definition differs for autothreshold (user-labelled) vs manual threshold issues.
- **Organization**: workspaces, groups, users, roles, permissions, MFA, SSO (Okta/Entra/Duo/Ping), service accounts; collections (group metrics + notifications); custom "data dimensions" to align health reporting to org structure; object owners; tags.
- **AI layer**: bigAI chat, AI issue/incident descriptions, suggested resolutions/preventions, cron suggestions, MCP server.
- **Programmatic**: bigConfig (configuration-as-code), CLI, Python SDK, REST APIs (metrics CRUD, lineage graph traversal, issue updates).
- **Extra module**: Data Sensitivity (PII scanning) as a separate module with its own agent.

### Metaplane (A)

- Positioning: "Metaplane is a data observability platform that helps data teams know when things break, what went wrong, and how to fix it." Purpose: "be the first, not the last, to know about data issues" (stakeholders currently find problems first — loss of trust framing).
- Mechanism (vendor-stated): "collects metrics, metadata, lineage, and logs… training anomaly detection models on historical values, then sending you alerts for outliers with options to provide model feedback."
- **Onboarding loop**: "add a source, integrate Slack, and add monitors" — in less than 10 minutes; only a warehouse connection is required to start; transformation (dbt) and BI (Looker/Tableau) integrations layer on.
- **Monitor types** (out-of-the-box): Row Count, Freshness, Column Count, Cardinality, Uniqueness, Nullness, Minimum, Maximum, Mean, Standard Deviation, Sum, Percent Zero, Percent Negative, Custom SQL. Optimization detail: row count/freshness pulled from information_schema where possible (cheaper), falling back to SQL aggregates.
- **Monitor configuration**: schedules, manual thresholds, rolling time windows, group-by monitors (per-segment anomaly detection), source-to-target monitors (cross-system flow), rules ("define criteria to automatically add monitors to specific parts of your database"), monitors-as-code, import historical observations, monitor forecasts, "New Normal" annotations.
- **Model feedback loop**: users mark detections good/bad ("providing model feedback") to improve detection; model troubleshooting guide exists (production ML is vendor-stated reality).
- **Incidents**: "Every failing monitor in Metaplane automatically triggers a new incident." Incidents group related failing monitors (same type + same failure direction + same schema/table neighborhood or lineage-related); purpose: higher-level view + combat alert fatigue ("instead of getting alerted for every individual failure… alert about related groups"); labels (custom or suggested); owner/DRI assignment with Slack/Teams @-mention mapping; drill into monitors; mark all/individual monitors normal; PagerDuty lifecycle sync (create on open, update title on new monitors, resolve on resolve); daily reminder for open incidents; auto-resolve setting with exclusions (labeled incidents and freshness incidents not auto-resolved); filter by status/source/tags.
- **Lineage**: end-to-end lineage; impact previews before merge (GitHub/GitLab data CI/CD integration) — "see the downstream impact before you merge."
- **Alerting**: Slack, Teams, webhooks, Google Chat (via function), alert routing, alert mentions (monitor owners @-mentioned), dbt node-level alerting, Jira integration.
- **Surfaces**: dashboards (custom monitoring views), pinning schema for quick access, tags to organize assets and prioritize incidents, Chrome extension, API (monitor CRUD, evaluation history, run, ingest datapoint, import historic data).
- **Sources breadth**: warehouses (Snowflake, BigQuery, Redshift, Databricks, ClickHouse, MySQL, Synapse), S3 (incl. Iceberg tables), SAP S/4HANA KPIs via REST/OData, Airbyte/Segment/Census/Hightouch, Airflow, dbt Core/Cloud, Looker (incl. LookML git), Tableau, Sigma, Hex; Snowflake Native App deployment option (no credentials leave the warehouse).

### Sifflet (A)

- Positioning: "Sifflet is a Full Data Stack Observability Platform on a mission to reduce Data Entropy. Our solution maps all dependencies across the entire life cycle of your data — from ingestion to BI tools."
- **Breadth of connection**: data platforms (Snowflake, BigQuery, Databricks, Redshift, Synapse, Athena, SQL Server, MySQL, Oracle, PostgreSQL, Cloud SQL, AlloyDB); BI tools (Power BI, Tableau, Looker, QuickSight, MicroStrategy β, Qlik β); pipelines (dbt Core/Cloud, Airflow incl. custom operators/MWAA/Composer, Fivetran, Databricks Workflows, Azure Data Factory β); code repositories (GitHub/GitLab with dbt impact analysis actions); external catalogs (Atlan β). Agent available for private networks; self-hosted deployments documented; Sifflet Native App for Snowflake.
- **Embedded catalog**: Data Catalog with asset pages (health status, usage, ownership, history, AI-generated metadata), field-level lineage, declarative assets & lineage (URI-based registration of external assets), reference assets, business glossary, data products, domains/subdomains.
- **Monitor template library** (first-class templates): Volume (dynamic/static), Freshness (two variants incl. update-time-gap), Schema change, Metrics (smart metrics = ML, custom metrics, correlated metrics), Referential integrity, Distribution change, Duplicates (row-level and key), Value list validation, Nulls, Unique, Value range, Is-an-email / is-a-phone-number / is-UUID / matches-regex, No-code condition, SQL condition, SQL query.
- **Monitor machinery**: setup and run flows, scan modes, time-based aggregation, partitioned-table auto-mode, failing rows surfaced, feedback loop ("how to improve the training process of ML models with user-generated input"), model sensitivity setting, special-dates handling, mute monitors (incl. bulk), schedules/calendars.
- **Automatic monitoring**: "Sentinel" (β) — AI monitor recommendations; AI Monitoring Optimization Suggestions (ML-monitoring setup at scale).
- **Incidents**: "an incident represents a specific, actionable issue or problem with your data… a centralized hub for investigating and resolving a data quality problem." Triggered by monitor-run results or dbt-test failures; contains one or more related failing checks; "Sifflet intelligently groups related failures into a single incident based on grouping rules." List page fields: auto-generated (editable) name, affected data assets, severity (inherited from triggering monitor), status (Open / In Progress / Closed), assignee(s), last failure timestamp, number of compromised dashboards. Detail page: header (status picker, create Jira/ServiceNow issue, edit) + five tabs — Overview (AI-generated description + details + RCA by "Sage" agent when enabled), Monitors (per-monitor status/severity/first+last failure/failed-run count; bulk qualify-as-passing; reassign monitors between incidents), Impacted Dashboards (downstream BI dashboards affected), Lineage (interactive graph centered on incident assets, failing assets highlighted), Notifications (active destinations); activity feed (creation, status changes, new monitors added, comments, fixes; Jira/ServiceNow events mirrored).
- **Notification machinery**: notification rules; destinations: email, Teams, Slack, Jira, ServiceNow, webhooks, PagerDuty, Statuspage, Google Chat.
- **Governance**: users, teams, domains/subdomains, access control guide, SSO (Okta/Google/AAD/ForgeRock), access tokens, audit logs.
- **Programmatic & enforcement**: CLI, monitors-as-code (YAML schema), Terraform provider, REST API, MCP server, data sharing; "Flow Stopper" integration — stops pipelines when failures detected (enforcement hook; examples documented).

### Anomalo (B — Tier-2 product pages only; operational docs unreachable)

- Homepage positioning: "autonomous data quality monitoring platform for the enterprise… autonomously monitors, investigates, surfaces, and reports… No code, no prompts, and no manual tedium required."
- Feature menu: Anomaly Detection, Data Validation, Data Governance, Data Observability ("cost-effective monitoring in minutes, no matter the scale"), Automated Data Lineage Tools, Unstructured Data Monitoring, AIDA conversational analyst.
- "Table Observability Agent": "always-on monitoring of data availability, freshness, and schema consistency."
- Enterprise posture: SOC 2 Type II / GDPR / HIPAA statements, SAML SSO (Okta/Google/Entra), VPC or SaaS deployment, bring-your-own-model option.
- Industry-tailored solutions (media/entertainment, telecom, financial services & insurance, retail/CPG, data providers, healthcare, energy).
- Agentic suite (several modules marked "coming soon") — treated as vendor-specific, not stable structure.
- Note: marketing claims only; no operational documentation fetched. All Anomalo-derived statements kept weak/product-specific.

---

## Cross-product Comparison (Step 6)

| Dimension | Bigeye | Metaplane | Sifflet | Anomalo (Tier-2) | Evidence |
|---|---|---|---|---|---|
| Connects to external data systems the platform doesn't own | A: agent/agentless sources, ETL, BI, dbt | A: warehouses, S3, SAP, Airbyte/CDPs, dbt, BI | A: platforms, BI, pipelines, repos, external catalogs | B: integrations menu | A×3 — defining |
| Monitored-asset model over the estate | A: catalog of sources/schemas/tables/columns | A: warehouse paths + dbt + BI objects | A: asset pages with health status/ownership | B: table observability | A×3 — defining |
| Automated health evaluation producing detections | A: metrics + autothresholds; rules complement | A: monitors + trained anomaly models | A: monitor templates incl. ML smart metrics + feedback loop | B: anomaly detection | A×3 — defining |
| Freshness / volume / schema-change / distribution-statistic dimensions | A: freshness & volume, schema change detection, profiling stats | A: row count, freshness, column count, nullness/uniqueness/min/max/mean | A: volume, freshness, schema change, distribution change, nulls/unique/range templates | B: availability, freshness, schema consistency | A×3 — common core vocabulary (not vendor framing) |
| ML/learned baselines as first-class | A: autothresholds + good/bad labels | A: trained models + model feedback | A: smart metrics + feedback loop + sensitivity | B: ML-driven | A×3 — common-not-core (manual thresholds/rules coexist) |
| Defined rules/checks as complement | A: custom SQL/join rules | A: custom SQL, manual thresholds, rules for auto-adding monitors | A: large static template library + SQL condition/query | B: data validation | A×3 — common |
| Stateful issue/incident record worked to resolution | A: issues (ack/resolve/close) + incidents (merged root cause) | A: incidents auto-created per failing monitor, grouped, DRI, auto-resolve | A: incidents Open/In Progress/Closed, assignee, severity, activity feed | B: monitoring/investigation framing | A×3 — defining |
| Grouping related failures | A: manual merge + lineage-suggested downstream merge | A: automatic grouping (type+direction+proximity/lineage) | A: grouping rules; reassignment between incidents | — | A×3 — common |
| Alert routing to chat/ticketing/on-call | A: Slack/Teams/email/webhook/Jira/ServiceNow/PagerDuty/Azure Boards | A: Slack/Teams/PagerDuty/webhook/Jira | A: Slack/Teams/Jira/ServiceNow/PagerDuty/Statuspage/email/webhook | — | A×3 — common |
| Lineage-based impact analysis | A: impact analysis; downstream merge suggestions | A: end-to-end lineage; PR impact previews | A: incident lineage tab; impacted-dashboards tab | B: automated lineage | A×3 — common |
| Health summary surfaces (scorecard/health status/dashboards) | A: scorecards per dimension | A: dashboards, pinning | A: asset health status, dashboards | — | A×3 — common |
| Ownership/teams/roles + SSO | A: workspaces/roles/SSO/MFA | A: users/assignments (SSO at commercial tiers — not verified this pass) | A: teams/domains/SSO/audit logs | B: SAML SSO | A×3 — common |
| Embedded catalog/glossary | A: catalog view + business glossary | (lighter — schema browsing; not a marketed catalog) | A: full catalog + glossary + data products | B: data governance | Common-optional — depth varies (B) |
| External test ingestion (dbt tests, external monitors) | A: external-monitors agent (dbt tests) | A: dbt test integration, dbt node alerting | A: dbt test failures trigger incidents | — | A×3 — common |
| Config-as-code / API / CLI | A: bigConfig, CLI, SDK, API | A: monitors-as-code, API | A: YAML monitors-as-code, CLI, Terraform, API | — | A×3 — common |
| CI/CD shift-left (impact previews at merge) | (not observed) | A: GitHub/GitLab impact previews | A: dbt impact analysis actions | — | A×2 — common-optional |
| Pipeline enforcement (stop flows on failure) | (not observed) | (not observed) | A: Flow Stopper | — | A×1 — product-specific (optional) |
| Data comparison/reconciliation | A: deltas | A: source-to-target monitors | A: correlated metrics (adjacent) | — | mixed — common-optional |
| Sensitive-data scanning | A: Data Sensitivity module | (not observed) | (not observed) | (not observed) | A×1 — product-specific (optional) |
| AI copilots / RCA agents | A: bigAI descriptions/resolutions/MCP | A: (feedback loops; ML guides) | A: Sage RCA, Sentinel recommendations | B: agentic suite | A×3 but depth/naming varies — common-optional |

---

## Model (Step 5) and Canonical Abstraction Hierarchy (§22)

### L0 — Defining Invariant (deliberately small)

Three structures. Remove any one and the product stops being recognizable as a Data Observability Platform:

1. **Connected external data estate.** The platform registers data assets — tables, files, dashboards, pipelines, models — that live in systems it does not own, and observes them through connections (direct/agentless or agent-deployed). The platform is a lens and custodian of health signals, never the system of record for the data itself. *(Remove → it is a data platform or an in-pipeline test library.)*
2. **Automated health evaluation over the estate.** The platform itself evaluates asset health on a continuing basis — via learned baselines and/or defined expectations (statistical monitors, template checks, SQL rules) — and flags deviations without a human running each check. *(Remove → static catalog or dashboard.)*
3. **The stateful incident record as the unit of response.** A detected deviation becomes a managed, stateful record (status, owner/severity, history, comments) that data teams work to resolution; alerting exists to drive this loop. *(Remove → a raw alert firehose / monitoring feed, not an operational platform.)*

Note on abstraction level: no specific detection algorithm (ML vs static) is in L0 — the sample proves products operate at both poles; no specific monitored medium (warehouse table vs dashboard vs file) is in L0; the exact incident taxonomy (issue vs incident vs monitor failure) varies by product and is documented as implementation variance over the same concept.

### L1 — Common Mature Structure

Very common across the researched sample; expected in practice, not definitional:

- **Monitor/check as the configured evaluation unit** — a statistic or expectation bound to an asset, run on a schedule, evaluated against learned bounds and/or thresholds; template libraries; mute/snooze.
- **Canonical health dimensions** — freshness, volume, schema change, distribution/statistics (nulls, uniqueness, cardinality, ranges, means) recur across all sampled products as the shared vocabulary of what to watch.
- **Feedback loops on detections** — marking detections as true/false ("good/bad", "anomalous/normal") to improve learning; sensitivity controls.
- **Defined rules as complement** — custom SQL checks, value/format rules, referential integrity, join/cross-source comparisons.
- **Alert routing** — chat (Slack/Teams), email, ticketing (Jira/ServiceNow), on-call (PagerDuty), webhooks; failed-monitor (monitor errored) as distinct from monitor-failed notifications.
- **Lineage-based impact analysis** — downstream affected assets/dashboards; incident grouping aided by lineage; monitoring rolled out along lineage.
- **Health summary surfaces** — scorecards/health statuses/dashboards over dimensions; popularity/usage to prioritize.
- **Ownership and organization** — asset owners, incident assignees/DRI, teams/workspaces, roles, SSO.
- **External test ingestion** — dbt tests and other pipeline-native checks folded into the same incident stream.
- **Programmatic control** — APIs, CLI, config-as-code, SDKs.

### L2 — Variant / Optional Structure

Depends on segment, stack, governance posture:

- Catalog/glossary depth (full embedded catalog with domains and data products at one pole; light schema browsing at the other)
- Data CI/CD shift-left (impact previews on PRs, pre-merge test previews)
- Pipeline enforcement hooks (halting pipelines on failure)
- Data comparison/reconciliation machinery (replication/migration validation)
- Sensitive-data scanning / classification modules
- Deployment posture (SaaS vs self-hosted vs VPC/native-app; agent vs agentless)
- AI copilots (RCA agents, auto-monitor recommendations, AI descriptions, MCP servers)
- Vertical/industry tuning
- Configuration-as-code depth, Terraform providers

### L3 — Vendor-specific (research notes only)

- Bigeye: "Deltas", "Collections", custom "Data Dimensions", scorecard color semantics (green/red/grey with true-positive definitions per threshold type), bigAI/bigIQ branding, Data Sensitivity module, Cross-Source Agent, incident priority inheritance rule, debug query/rows.
- Metaplane: incident grouping conditions (same type + same direction + same schema neighborhood or lineage-relation), auto-resolve exclusions (labeled and freshness incidents), daily open-incident reminders, "New Normal" annotations, monitor forecasts, import historical observations, information_schema optimization notes, per-monitor-type sample SQL, Chrome extension, Snowflake Native App.
- Sifflet: "Sage" RCA agent, "Sentinel" auto-monitor recommendations, Flow Stopper, the specific template taxonomy (is-email/is-phone/is-UUID…), domains/subdomains, data products, Statuspage destination, declarative URI-based assets, monitor reassignment between incidents, scan modes.
- Anomalo: agentic suite naming (Table Observability Agent, Data Insights Agent, AIDA…), unstructured-data monitoring, per-industry solution packaging.

### Rejected Findings (overfitting avoided)

- **"ML anomaly detection is the definition"** — rejected. The sample spans ML-first and template/rules-first products; Sifflet's monitor library is largely static expectations; Bigeye offers manual thresholds alongside autothresholds. Canonical abstraction: *learned baselines and/or defined expectations*.
- **"Warehouse tables are the object"** — rejected. Sample monitors S3 files/Iceberg tables, SAP KPIs, BI dashboards, dbt nodes, pipelines. Canonical: *data assets*.
- **"Issue vs Incident two-tier taxonomy"** — rejected as definitional. Bigeye distinguishes them (issues merge into incidents); Metaplane auto-creates one incident per failing monitor; Sifflet triggers an incident per failure and groups related ones. Canonical: a stateful record representing a detected problem, with grouping-as-implementation-variance.
- **"The five pillars framing (freshness/volume/schema/distribution/lineage)"** — not treated as a vendor-owned definition; the underlying dimensions are independently documented across all three Tier-1 samples (B-layer), and lineage is an integration point rather than a monitored dimension per se.
- **"Incident management belongs to ITSM, not here"** — rejected for the boundary; the incident record here is data-scoped and produced by data-health evaluation, even though ITSM handoff (Jira/ServiceNow) is common.

---

## Boundary Findings (Step 7)

- **vs Data Quality Platform** (§13 sibling, not yet processed). Closest seam. DQ centers on *defined expectations/rules executed against data* — the rule and its pass/fail result is the primary object (test suites, rule engines). Observability centers on *ambient health watching of the whole estate plus the incident loop* — detection (learned or defined) and response are the primary object. Observed interlock: observability products embed quality rules as one monitor family (Bigeye "augment your metrics with custom rules"; Sifflet template library; Metaplane custom SQL/manual thresholds), and vendor framing explicitly contrasts rules-rooted DQ with observability (Bigeye's "What is Bigeye"). Test: remove ambient learned baselines + estate-wide incident loop → a rules engine/DQ tool; remove defined-rule authoring as a first-class object → pure observability. Products sit on a gradient; joint review recommended when data-quality-platform is processed (consistent with the data-governance pass's earlier capability-seam flag).
- **vs Data Lineage Platform** (processed). Boundary held, both directions already recorded in the lineage pass: lineage = the flow graph + trace operations (structure, blast radius); observability = health evaluation + failing node (runtime state). Interlock documented from both sides: observability products embed lineage for impact analysis and incident grouping (A×3); the lineage pass noted a unified platform shipping an "observability layer" on the lineage graph. Remove health evaluation → lineage platform; remove the flow graph → still observability (lineage becomes an optional dependency).
- **vs Data Catalog** (processed). Catalog = descriptive inventory + discovery loop; observability = health + incident loop. Sifflet ships a genuine catalog (asset pages, glossary, data products) inside an observability platform — packaging convergence, consistent with the catalog pass's note that quality signals surface on catalog entries. Test: remove health evaluation + incidents → catalog; remove descriptive inventory as primary object → observability. Held as separate Types.
- **vs Observability Platform (§14)** — name collision, different object. §14 observability collects and inspects *software telemetry* (logs, metrics, traces of applications/infrastructure) for SRE/ops; this Type watches *data health* (freshness/volume/schema/distribution of datasets and pipelines) for data teams. Metaplane's own blog contrast ("Data Observability vs. Software Observability") confirms the market distinguishes them. Remove data assets → §14 Type; the shared word is vocabulary, not structure.
- **vs ML Model Monitoring Platform** (§13 sibling, unprocessed). Models' prediction performance/drift vs the health of data feeding models. Some observability products extend toward models feeding pipelines; the defining object here remains the data asset.
- **vs ETL/ELT Platform** (processed). Movement vs watching; the integration pass's custodian posture mirrors this pass's lens posture. ETL-native run monitoring is a partial realization (consistent with the lineage pass's note); remove movement execution → observability.
- **vs DataOps Platform** (§13 sibling, unprocessed). DataOps automates data-engineering practice (testing, CI/CD, deployment of pipelines); observability watches production data health. CI/CD impact previews (Metaplane/Sifflet) create a capability seam worth joint review.
- **Taxonomy observation**: several vendors position the same product under both "data quality" and "data observability" labels (Anomalo's own menu lists both; Bigeye's positioning contrasts the two). The Type boundary is a primary-object question, not a vendor-label question; flagged for joint review.

## Uncertainties

1. Monte Carlo (category originator) unreachable — the incident-centric pole is evidenced via Bigeye/Metaplane/Sifflet instead; any Monte Carlo-specific framing was avoided.
2. Anomalo evidence is Tier-2 (marketing) only; its no-code/ML-first claims are kept weak and product-specific.
3. Exact incident-status vocabularies differ per product (Open/In Progress/Closed vs acknowledge/resolve/close vs labels) — canonical document deliberately keeps conceptual states, not vendor labels.
4. Tier/plan gating of specific capabilities (e.g., Metaplane SSO, Sifflet RCA agent availability) was not systematically verified; the final document avoids plan-specific claims.
5. Whether the market consolidates observability into catalog/governance suites (Sifflet's catalog depth suggests convergence) — recorded as a market-structure note, not asserted as fact.
6. data-quality-platform and dataops-platform leaves unprocessed — boundaries from this side recorded; joint review recommended (see Boundary Issues for STATUS).

---

## Final Synthesis

A Data Observability Platform is the health-watching layer over an organization's data estate. Its defining core is small: it connects to data systems it does not own; it continuously evaluates the health of the registered data assets (freshness, volume, schema, distribution, defined expectations, learned baselines) and flags deviations automatically; and every detected problem becomes a stateful incident record that data teams work — assign, investigate, communicate, resolve — with alert routing pulling humans in where they work. Around that spine, mature products add the monitor template/vocabulary layer, feedback loops that improve detection, lineage-driven impact analysis, health scorecards, ownership/teams/SSO, external test ingestion, and programmatic control; and variants add catalog depth, CI/CD shift-left, pipeline enforcement, reconciliation, sensitive-data scanning, deployment postures, and AI copilots. The Type sits between the Data Quality Platform (rules-as-primary-object), the Data Lineage Platform (structure-of-flows), the Data Catalog (inventory-and-discovery), and the §14 Observability Platform (software telemetry — same word, different world).
