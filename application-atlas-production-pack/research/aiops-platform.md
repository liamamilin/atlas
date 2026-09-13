# Research Notes — AIOps Platform

## Research Goal

Understand what an "AIOps Platform" actually is as an Application Type: what objects exist inside it, what the automated analysis really does, how operational work flows through it, and where its boundary lies against monitoring/observability products, incident-management products, and security event platforms.

## Initial Boundary

Working hypothesis before research:

- AIOps = "Artificial Intelligence for IT Operations" — a layer that applies automated analysis (ML/statistics/rules) to IT operations data (alerts, events, metrics, logs) to reduce noise, correlate related signals, detect anomalies, identify probable cause, and drive response.
- Nearest neighbors: Observability Platform, APM, Infrastructure Monitoring (collection/visualization layer); Incident Management and On-call Management (human workflow layer); SIEM (security-domain analog); Event Stream Processing (data-infrastructure analog).
- Suspected taxonomy tension: "AIOps" is simultaneously marketed as (a) a standalone product category (event-correlation platforms) and (b) a capability embedded inside observability/ITSM suites. The research must decide whether the Type is the standalone form, the capability, or an abstraction covering both.

## Research Questions

1. What are the core objects? (event, alert, incident, anomaly, problem, topology, tag/enrichment, runbook/action)
2. What does the automated analysis actually do, step by step? (dedup, filter, correlate, anomaly detection, root cause)
3. What is the lifecycle of the central output object (incident/problem)?
4. What does the platform ingest, from where, and in what posture (own telemetry vs third-party monitors)?
5. How do humans interact? (console, triage, configuration, analytics)
6. What rules govern behavior? (correlation windows/patterns, suppression/maintenance, severity mapping, reopen logic)
7. How does output reach response? (notification, ticketing, chat, automation)
8. Where is the boundary against monitoring, incident management, and SIEM?

## Representative Products

Selected for market representativeness, documentation completeness, and different product philosophies / positions in the stack:

| Product | Philosophy / position | Customer tier |
|---|---|---|
| BigPanda | Pure-play, domain-agnostic event-correlation AIOps platform sitting above existing monitoring tools | Enterprise NOC / IT Ops |
| Datadog (Watchdog + Event Management) | Cloud observability suite with embedded AIOps capabilities | Cloud-native, mid-market → enterprise |
| Dynatrace (Dynatrace Intelligence / Davis) | Full-stack observability suite with embedded causal AI and topology | Enterprise |
| Moogsoft (Dell APEX AIOps Incident Management) | Pure-play ML/NLP alert-correlation product | Enterprise IT Ops |

Also sampled: **ServiceNow** (ITSM-integrated AIOps within ITOM) — official docs could not be fetched (JavaScript-rendered application; content not retrievable from the research environment). Assertions about ServiceNow are therefore NOT evidence-based here; it is retained only as a named example of the ITSM-embedded variant, with reduced confidence.

## Sources

Research date: 2026-09-06. All fetched same day.

- BigPanda — docs.bigpanda.io: "Get Started with BigPanda", "Event Management", "Events to Incidents Lifecycle (ADR)", "Incidents in BigPanda" (fetched OK)
- Datadog — docs.datadoghq.com: "Datadog Watchdog™", "Event Management", "Event Management > Correlation" (fetched OK); Datadog product-page URLs for AIOps returned 404 (abandoned after 2 attempts); AIOps positioning confirmed via official blog title cited in Datadog docs ("Aggregate, correlate, and act on alerts faster with AIOps-powered Event Management")
- Dynatrace — docs.dynatrace.com: "Analyze, Explore, and Automate" (section index), "Alerting and notifications" (fetched OK); a direct Davis-AI path 404'd, content obtained via the alerting page's links to Dynatrace Intelligence / Problems app
- Moogsoft / Dell — docs.moogsoft.com: "APEX AIOps Incident Management" portal, "What is AIOps and how can it help you?", "Step 3: Check alert correlation" (fetched OK)
- ServiceNow — docs.servicenow.com and servicenow.com product page: not retrievable (JS app / timeout). Limitation recorded; no ServiceNow-specific claims made.

## Product Observations

### BigPanda (evidence layer A — directly observed)

Self-description: "an algorithmic event correlation platform" providing "AIOps that transform IT data into insight and action" for IT Ops / NOC / DevOps teams.

Observed pipeline (Events to Incidents Lifecycle):

1. **Event ingestion** — events received from monitoring integrations (e.g., Nagios, SolarWinds, AppDynamics). "An event is a point in time that represents the state of a service, application, or infrastructure component."
2. **Event deduplication** — exact-duplicate payloads discarded; updates to existing alerts merged rather than creating new alerts.
3. **Event filtering** — user-defined criteria (BigPanda Query Language) drop unactionable events at ingestion: misconfigured events missing critical tags, lowest severity, non-production environments, non-alerts (info events, logs).
4. **Alert formation** — post-dedupe events clustered into **alerts**, each representing "a single issue within your environment"; status updates and repeat events merge into one alert so its lifecycle is visible over time.
5. **Alert enrichment** — alert **tags** (key-value pairs) add context; tags drive normalization, dedup, correlation, enrichment, and automation.
6. **Incident formation** — an **incident** is "the correlation of one or more alerts that represent an issue that can impact the business through a service disruption." Correlation uses **correlation patterns** clustering alerts by source system, tags, time window, and optional query filter. Documented mechanics: check for matching alerts via incident key → check matching correlation patterns (largest correlation window wins) → update the incident's active patterns → update incident title → update incident status from the most severe active alert. A documented maximum of 300 alerts per correlated incident.
7. **Incident enrichment** — incident tags summarize context (cluster/datacenter location, links to metrics and runbooks).
8. **Incident classification** — incidents grouped into **environments** (filters on source/priority etc.) so teams see the incidents relevant to their role.

Observed incident lifecycle logic:

- Incident remains active while at least one contained alert is active; automatically resolved when all alerts resolve; reopened when a resolved alert becomes active again (documented default reopen window: 60 minutes; incidents older than 30 days never reopened — precise numbers are vendor-specific).
- **Flapping** state when alerts change state too frequently (documented default: more than 4 state changes per hour); notifications suppressed while flapping.
- Snoozed incidents; time-based alert resolution for orphaned alerts.

Observed operator actions: assign to user, share (manually or **AutoShare** to email/SMS/ServiceNow/Jira), adjust priority, comment, snooze, manually resolve; triage and remediate within the Incident Feed.

Observed admin/config: integrations (monitoring, collaboration, change, topology tools), enrichment/tag management, correlation pattern management, environments, roles management, SSO, API keys, Unified Analytics dashboards. Newer agentic layer: "AI Incident Assistant" (Biggy) web app with guided onboarding and indexed organizational knowledge.

### Datadog — Watchdog + Event Management (evidence layer A — directly observed)

Watchdog (self-described "Datadog's AI engine"):

- "providing you with automated alerts, insights, and root cause analyses that draw from observability data across the entire Datadog platform"; "All Watchdog features come built-in, and do not require setup."
- **Proactive alerts**: "Watchdog proactively computes a baseline of expected behavior for your systems, applications, and deployments. This baseline is then used to detect anomalous behavior."
- **Investigation assistance**: context-based insights in all explorers, root cause analysis (RCA) searches, impact analysis (identifies when an anomaly adversely impacts users), faulty deployment detection.
- Related monitor algorithms user-configurable: anomaly, forecast, outlier.

Event Management:

- "Ingest, enrich and normalize, and correlate your events from any source into actionable insights." Events auto-created from Datadog products (monitors, Watchdog, Error Tracking) and ingestible "from any source, including alert events from third parties, change requests, deployments, configuration changes." 100+ integrations listed (Kubernetes, Docker, Jenkins, Chef, Puppet, ECS, Sentry, Nagios…).
- Components: ingest; **pipelines and processors** (enrich and normalize); **triage inbox** ("Triage, investigate, collaborate, and resolve incidents"); **events explorer** (view, search, notify); **correlation** — "groups events based on their relationships or on user-defined configurations to reduce the number of notifications and issues identified from the environment"; correlation analytics (work items assigned, counts by service, etc.).
- Stated purpose of correlation: "Reduce alert fatigue; Reduce the number of tickets and notifications you receive; Have all affected teams aware of a single issue instead of working in silos."

Positioning: Datadog's own blog title (cited in its docs) calls Event Management "AIOps-powered."

### Dynatrace — Dynatrace Intelligence / Davis (evidence layer A — directly observed)

From "Alerting and notifications" (Latest Dynatrace):

- "Dynatrace Intelligence groups related alert instances represented in Grail as **Davis events**, into a **problem**, and enriches each problem with impacted components, dependency context, and root cause analysis, so that you can identify the issue."
- "Dynatrace uses AI-powered anomaly detection to continuously monitor your environment for deviations from normal behavior" — performance bottlenecks, service downtime, unusual metric patterns; sensitivity adjustable to reduce false positives/missed anomalies.
- **Custom alerts**: user-defined conditions for specific metrics/thresholds/log patterns, configured in the Anomaly Detection app.
- **Problem detection**: "Dynatrace correlates Davis events with contextual data to identify the root cause of issues. Detected problems are enriched with detailed information, including impacted services, dependency mappings, and root cause analysis." Problems app = "centralized view of all detected problems and supports efficient triage and investigation."
- **Workflows**: triggers on problems/events → notifications (email, Slack, Microsoft Teams, ServiceNow) or automation; "agentic workflows" where Dynatrace Intelligence "assess[es] a situation and act[s] for you… summarizing a problem, computing a score, or automatically triggering remediation based on that score." Simple vs standard workflows (escalation rules, multi-step automation).
- Topology context: Smartscape visualizes entities and dependencies (listed under Analyze/Explore).

### Moogsoft / Dell APEX AIOps Incident Management (evidence layer A — directly observed)

Vendor's own definition of the category: "AIOps is an application which automates IT operations workflow via AI, machine learning, data science, and algorithms. But for a solution to provide value, it must work with the existing tools and within the current framework."

Vendor's articulation of "the five core capabilities required by an AIOps solution":

1. **Problem detection** — "Detects and identifies anomalies in time series data and makes predictive analyses based on trends; Deduplicates alarms and provides the ability to filter out unimportant or non-actionable items."
2. **Correlation** — "Discovers shared patterns in data and groups related items together; Makes relatedness decisions based on natural language processing (NLP), rather than relying on static rules or topology."
3. **Ticket creation and assignment** — "Creates tickets with relevant information; Assigns them automatically to the right teams or individuals."
4. **Investigation** — "Compares incidents past and present and can surface solutions which resolved previous similar incidents."
5. **Remediation** — "Implements remediation via automation."

Product mechanics observed:

- Quick start flow: (1) ingest monitoring data via integrations; (2) check **noise reduction**; (3) check **alert correlation** — "The Correlation Engine groups alerts by their relatedness, and creates incidents. It works out of the box, although you can fine tune it… and set up multiple correlation engines to process different types of data. The default correlation engine groups alerts from the same or similar sources."
- Incident = "A cluster of alerts that all relate to the same actionable incident… clusters alerts based on the similarity of their time stamps and data fields." Correlation engines configured with scope filters and "fields to correlate."
- Correlation glossary definition: "The process of finding correlations between alerts, based on similarities between data fields of interest, and clustering correlated alerts into actionable incidents."
- Surfaces: Incidents list with Total Alerts column; Incident Details pane with Alerts tab; System Configuration; Workflow Engine ("process your monitoring data with sequences of configurable actions"); inbound integrations (ingestion services); outbound integrations (notifications); APIs ("API-first"); Executive Summary dashboard.
- Note: if only metrics are ingested, anomaly identification takes time before incidents appear — indicating metrics-based anomaly detection is part of the same product.

## Cross-product Comparison

| Dimension | BigPanda | Datadog | Dynatrace | Moogsoft/APEX |
|---|---|---|---|---|
| Ingest posture | Aggregates events from third-party monitoring tools | Ingests events from any source + its own platform's events | Native full-stack telemetry (logs/metrics/traces/events) + third-party | Ingests from external monitoring tools |
| Normalization/enrichment | Tags; pipelines of enrichment | Pipelines & processors | Grail semantic dictionary / context | Tags/fields; workflow engine |
| Dedup & filtering | Explicit documented stages | In Event Management processing | Implicit in problem grouping | Explicit ("noise reduction" step) |
| Correlation into higher-level object | Correlation patterns (source/tags/time window/query) → incident | Correlation (relationships or user-defined configs) → correlated issues/work items | Davis events → problems | Correlation engines (NLP/similarity) → incidents |
| Anomaly detection | Not the core pitch (event-centric) | Watchdog baselines; anomaly/forecast/outlier monitors | AI-powered anomaly detection, adjustable sensitivity | Anomaly detection in time series + predictive analyses |
| Root cause / probable cause | Context enrichment (links, tags) | Watchdog RCA + impact analysis | RCA with impacted components + dependency context | Investigation comparing past incidents |
| Central output object | Incident | Correlated events / incidents (triage inbox) | Problem | Incident |
| Lifecycle rules | Explicit: active while ≥1 alert active; auto-resolve; reopen; flapping; snooze | Work items / triage states | Problem lifecycle (detected → …) | Incident states in console |
| Response routing | AutoShare: email/SMS/ServiceNow/Jira | Notifications; tickets | Workflows → email/Slack/Teams/ServiceNow | Outbound integrations; ticket creation & assignment |
| Automation | Automation via tags/rules; AI Incident Assistant | Workflows; monitors | Workflows; auto-remediation; agentic workflows | Workflow Engine; remediation via automation |
| Analytics | Unified Analytics dashboards | Correlation analytics | Problems app views | Executive Summary |
| Admin | Roles, SSO, API keys, integrations | Standard platform admin | Platform admin | System configuration, APIs |

Cross-product commonalities (evidence layer B):

1. All four ingest machine-generated operational signals describing the state of the IT estate.
2. All four run automated, machine-executed interpretation over the signal stream: deduplication and filtering (all four), correlation/grouping into a higher-level object (all four), anomaly detection from baselines (three of four — not BigPanda's core), probable-cause/context enrichment (all four in some form).
3. All four produce a named higher-level operational object — "incident" (BigPanda, Moogsoft, Datadog triage) or "problem" (Dynatrace) — that is the unit of triage.
4. All four route output to humans and systems: notification channels, ticket systems, and automation hooks.
5. All four expose configuration of the analysis itself (correlation patterns/engines, sensitivity, filters) — the analysis is policy-configured, not hardcoded.
6. All four provide operational analytics (noise reduction, volumes, trends).

Differences (posture, not essence):

- Where signals come from: third-party monitors (BigPanda, Moogsoft) vs native telemetry (Dynatrace, Datadog) — an ingestion-posture variant.
- Analysis technique: rule/pattern correlation (BigPanda), NLP/similarity (Moogsoft), causal/topology-driven (Dynatrace), baseline statistics (Datadog Watchdog) — a technique variant.
- Whether the platform owns telemetry collection: standalone aggregator vs observability suite vs (unverified here) ITSM-embedded.

## Canonical Abstraction

### L0 — Defining Invariant

Minimal structure without which the product stops being an AIOps Platform:

1. **Operational signal ingestion** — the platform takes in machine-generated operational signals (alerts/events; in suite form also metrics/logs/traces) describing the state of the organization's IT estate.
2. **Automated machine-executed analysis over the signal stream** — the platform itself performs interpretation steps (deduplication, filtering, correlation/grouping, deviation detection) without a human composing each conclusion. The technique may be rules, statistics, ML, NLP, or topology — "automated analysis" is the invariant, not "machine learning" specifically.
3. **Actionable operational output** — the analysis produces a higher-level managed object (correlated incident / detected anomaly / probable cause) with a lifecycle, surfaced for operational response.

Tests:

- Remove #2 → the product is a monitoring/event console with human triage (not AIOps).
- Remove #3 → the product is a data pipeline / stream processor (not AIOps).
- Remove #1 → the product is generic analytics/ML tooling with no operational domain (not AIOps).

Historical check: pre-ML event-correlation engines (rule-based alarm correlation in older NMS/event consoles) satisfy this L0 via rule-based analysis; modern products satisfy it via ML/statistics. Defining the Type as "ML-based" would exclude the historical ancestors and is a market-era artifact, not an invariant. Conversely, requiring "multi-source aggregation" would exclude suite-embedded AIOps; multi-source is the standalone variant's posture (L2), not the invariant.

### L1 — Common Mature Structure

Present across the researched sample; expected in mature products but not definitional:

- normalization & enrichment of signals into a shared tagged schema
- deduplication and filtering/suppression (maintenance windows, non-production, low severity)
- correlation of signals into incidents (time windows, shared attributes, patterns; technique varies)
- anomaly detection from learned baselines (in 3 of 4 sampled)
- probable-cause / root-cause enrichment using context (topology/dependencies, past incidents)
- incident lifecycle management (active → resolved; reopen on recurrence; flapping/snooze handling in some)
- routing & notification (email/chat/ITSM tickets/on-call systems)
- incident console / triage surface (feed + detail + actions: assign, prioritize, comment, resolve, share)
- operational analytics (noise reduction, event volumes, MTTR-style metrics)
- automation hooks (workflow engines, runbooks, webhooks, auto-remediation)
- administration: integrations, roles/SSO, APIs

### L2 — Variant / Optional Structure

- **Ingestion posture**: standalone aggregator above third-party monitors ↔ observability suite with native telemetry ↔ ITSM-suite-embedded AIOps
- **Analysis technique**: rule/pattern correlation ↔ statistical/ML anomaly detection ↔ NLP similarity ↔ topology/causal reasoning
- **Topology/CMDB depth**: none → tag-based context → live dependency topology
- **Remediation depth**: notify-only → runbook automation → agentic remediation
- **Deployment**: SaaS vs on-premises/hosted
- **Scope**: event-centric point platform vs full observability/ITOM suite
- **Generative/agentic assistant layer** (newer products)
- **Customer tier / scale** packaging

### L3 — Vendor-specific (research notes only)

- BigPanda: correlation patterns with documented 300-alert max per incident; BPQL filter language; environments; AutoShare; Biggy AI Incident Assistant; documented reopen window (60 min default, 30-day max) and flapping threshold (4 state changes/hour default).
- Datadog: Watchdog brand; Bits AI; Event Management triage inbox; monitor algorithm types (anomaly/forecast/outlier); documented monitor aggregation-key migration note.
- Dynatrace: Davis / Dynatrace Intelligence branding; Davis events; Problems app; Grail; Smartscape; simple vs standard workflows; agentic workflows.
- Moogsoft/Dell: multiple configurable correlation engines; five-capability AIOps framing; Workflow Engine; Executive Summary; legacy Moogsoft AIOps v7.x naming ("Situations" era) vs current APEX AIOps Incident Management.

## Vendor-specific Findings

See L3. Additionally: Moogsoft's own docs define AIOps with five capabilities — useful as a vendor articulation of the category, but it bundles ticket creation and remediation (which other vendors treat as integrations/workflows) into the definition; treated as vendor framing, not canonical.

## Boundary Findings

- **vs Observability Platform / APM / Infrastructure Monitoring**: those Types collect, store, and visualize telemetry and evaluate configured alert rules. An AIOps layer performs automated *interpretation* across signals (correlation, anomaly baselines, cause analysis) and emits higher-level conclusions. Suites (Datadog, Dynatrace) embed both layers; standalone AIOps platforms (BigPanda, Moogsoft) deliberately sit above existing monitors and do not replace them. **Remove the automated cross-signal interpretation layer → you have monitoring/observability.**
- **vs Incident Management (ITSM)**: incident management is the human workflow over tickets (acknowledge, escalate, resolve, postmortem). AIOps *creates* correlated incident intelligence and feeds it into that workflow. **Remove automated correlation/analysis → you have incident management.**
- **vs On-call Management**: on-call manages who gets paged and when (schedules, escalations). AIOps decides *what constitutes one actionable issue* worth paging about. Complementary; often integrated.
- **vs SIEM**: same structural pattern (ingest many sources → normalize → correlate → actionable case → response), different domain: security threats vs IT service availability/performance. Domain of the signals and the response playbook is the boundary.
- **vs Event Stream Processing Platform**: stream processing is data infrastructure for building pipelines; AIOps is an operational application with domain semantics (incidents, alerts, remediation) — though it may be built on such infrastructure.
- **vs Capacity Management / forecasting**: AIOps predictive analytics overlaps with forecasting, but capacity planning is a planning discipline with its own objects (capacity models, headroom); AIOps prediction serves incident prevention/detection.
- **Taxonomy tension (recorded)**: "AIOps" is both a standalone product category and a capability embedded in observability/ITSM suites. The Type is best understood as the *automated interpretation layer*; the standalone platform is its clearest instantiation, and suite-embedded AIOps is the same capability delivered inside another Type's container. Flagged in STATUS as a capability-vs-type review candidate.

## Uncertainties

- ServiceNow's AIOps/ITOM mechanics could not be verified (docs not retrievable). The ITSM-embedded variant is described structurally, not from ServiceNow evidence.
- Precise lifecycle rules (reopen windows, flapping thresholds, correlation limits) were documented only for BigPanda; equivalent rules presumably exist elsewhere but were not observed — treated as vendor-specific.
- How widely "agentic remediation" (AI deciding and executing fixes) has spread beyond the newest releases is unclear from the sampled docs; treated as an emerging L2 variant.
- Whether anomaly detection is definitional: BigPanda (event-correlation-centric) does not pitch it as core; three of four products have it. Kept in L1, not L0.
- Moogsoft's post-acquisition packaging (Dell APEX AIOps) may shift naming; observations are from the current docs portal.

## Final Synthesis

An AIOps Platform is the automated interpretation layer of IT operations: it ingests the operational signal stream produced by an organization's monitoring estate, runs machine-executed analysis over that stream (deduplicate, filter, correlate, detect anomalies, attribute probable cause), and emits a small number of actionable operational conclusions — correlated incidents and detected anomalies with context — that drive response through notification, ticketing, and automation. Its defining value is the substitution of machine interpretation for manual NOC triage: many raw signals in, few actionable issues out. The standalone "event correlation platform" is the purest form; observability suites and ITSM suites deliver the same layer embedded in their own containers. The invariant is automated analysis over operational signals producing actionable operational output — not any particular algorithm, ingestion posture, or remediation depth.
