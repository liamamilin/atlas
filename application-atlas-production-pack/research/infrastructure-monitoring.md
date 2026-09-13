# Research Notes — Infrastructure Monitoring

Research date: 2026-09-08
Slug: infrastructure-monitoring
Directory leaf: Infrastructure Monitoring (§14 IT, Cloud & Infrastructure)

## Research Goal

Understand what an Infrastructure Monitoring product actually is as an Application Type: its core objects, how telemetry about infrastructure enters and is evaluated, what operators do with it, and where its boundary lies against APM, Metrics Monitoring, Network Monitoring, Server Management, Incident Management, and Observability Platforms.

## Initial Boundary

Working hypothesis before research:

- Core use: continuously observe the health, availability, and resource condition of infrastructure components — servers/hosts, VMs, containers, network devices, cloud resources — by collecting metrics and check results, evaluating them against conditions, and surfacing health/alert states.
- Primary users: system administrators, IT operations, SREs, DevOps, NOC operators.
- Likely confusions: APM (request-centric), Metrics Monitoring (generic metric store), Network Monitoring (device specialization), Server Management Platform (control plane vs observation plane), Incident Management (response loop), Observability Platform (umbrella suite), CMDB (asset record vs operational inventory).

## Research Questions

1. What is the core monitored object, and how is the estate inventoried?
2. What telemetry is collected (metrics, check results, events) and through what mechanisms (agent, agentless, pull, push)?
3. How are health states defined and evaluated (thresholds, expressions, check states, severity)?
4. What is the alert/problem lifecycle (trigger → notify → acknowledge → resolve)?
5. What are the primary interfaces (entity list, entity detail, dashboards, problem console, maps, reports)?
6. How does the Type relate to APM / observability suites — where does infrastructure monitoring end?
7. What rules matter (maintenance windows, dependencies, flapping, escalation, permissions)?
8. Would older / agentless / non-cloud products still fit the definition (historical check)?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Philosophy / tier | Why sampled |
|---|---|---|
| Datadog (Infrastructure Monitoring) | Modern commercial SaaS, agent + cloud integrations, tag-centric | Market-leading commercial realization |
| Zabbix | Open-source classic, self-hosted, item/trigger model, agent + agentless | The classic open-source realization; extremely complete official manual |
| Nagios Core | Historical ancestor (1999-era), plugin checks, CGI UI | Historical / market-sample check |
| Prometheus | Open-source pull-based metrics stack, dimension model, CNCF | The cloud-native metrics realization |
| Dynatrace (Infrastructure Observability) | Enterprise suite, auto-discovery, AI classification | Enterprise-suite realization |

## Sources

All fetched 2026-09-08 (Tier 1 official documentation):

- Datadog — Infrastructure overview: https://docs.datadoghq.com/infrastructure/
- Datadog — Host List: https://docs.datadoghq.com/infrastructure/list/
- Datadog — Monitors: https://docs.datadoghq.com/monitors/
- Datadog — Monitor Types: https://docs.datadoghq.com/monitors/types/
- Datadog — Getting Started with Monitors: https://docs.datadoghq.com/getting_started/monitors/
- Zabbix — What is Zabbix: https://www.zabbix.com/documentation/current/en/manual/introduction/about
- Zabbix — Definitions: https://www.zabbix.com/documentation/current/en/manual/definitions
- Zabbix — Manual TOC (structure of concepts): https://www.zabbix.com/documentation/current/en/manual
- Nagios Core 4 — Host Checks: https://assets.nagios.com/downloads/nagioscore/docs/nagioscore/4/en/hostchecks.html
- Nagios Core 4 — State Types: https://assets.nagios.com/downloads/nagioscore/docs/nagioscore/4/en/statetypes.html
- Nagios Core 4 — TOC (topic structure): https://assets.nagios.com/downloads/nagioscore/docs/nagioscore/4/en/toc.html
- Prometheus — Overview: https://prometheus.io/docs/introduction/overview/
- Dynatrace — Infrastructure Observability: https://docs.dynatrace.com/docs/observe/infrastructure-monitoring
- Dynatrace — Health alerts and warning signals: https://docs.dynatrace.com/docs/observe/infrastructure-observability/health-alerts-warning-signals

Source-access notes: all key pages fetched successfully. Zabbix manual pages return a very large sidebar; definition and positioning content was extracted from the saved full output. No Tier-1 page required abandonment.

## Product Observations

### Datadog (Infrastructure Monitoring) — evidence layer A

- Positioning: "Infrastructure monitoring includes core Datadog features that visualize, monitor, and measure the performance of your hosts, containers, and processes." Components: Infrastructure List, Host and Container Maps, Containers View, Processes View.
- Host List: "a live inventory of all hosts reporting to Datadog through the Agent or cloud integrations." By default shows hosts with activity in the last 15 minutes. Filter panel: teams, cloud provider (AWS/Azure/GCP/Oracle/Alibaba), telemetry source (Datadog Agent or OpenTelemetry), OS, GPU; filter by any host property or tag (facets: Cloud Provider, Env, Region, Resource Type, Instance Type, OS, Agent version, Docker version); filter hosts by metric value range. Customizable columns: Host Attributes, Tags, Metrics. Combined columns: Configurations (cloud provider, OS, agent status), Software (web server, database, cache, container orchestrator — "if detected"), Integrations.
- Host detail side panel: hostnames and aliases, tags, metrics, containers, logs (if enabled), Agent configuration, OTel Collector configuration.
- Monitors: "actively check metrics, integration availability, network endpoints, and more." Metric monitor example: `system.disk.in_use` averaged by host and device, alert threshold > 0.9, warning threshold > 0.8. Detection methods include threshold, change, anomaly (based on historical data), forecast (projected threshold crossing), outlier. Monitor types include Host ("check if one or more hosts are reporting"), Metric, Live Process, Network (TCP/HTTP endpoint status), Service Check, Integration, Composite (expression combining monitors), plus types over other data domains (APM, Logs, RUM, CI, Cloud Cost, SLO, Synthetic).
- Automatic Monitors: on Agent install, Datadog auto-creates baseline monitors (host CPU/memory, Kubernetes pod restarts/node health, APM error rates/latency).
- Notification: title + message with template variables, routed to email/Slack/PagerDuty; downtimes "to mute alerts during application maintenance"; monitor permissions (edit access restricted to creator/teams/roles); monitor saved views; mobile triage.
- Alerting-platform framing: "By configuring monitors to track key metrics and thresholds, organizations can receive immediate alerts."

### Zabbix — evidence layer A

- Positioning: "Zabbix is an enterprise-class open source distributed monitoring solution… monitors numerous parameters of a network and the health and integrity of servers, virtual machines, applications, services, databases, websites, the cloud and more." "Supports both polling and trapping." "Reporting and data visualization features based on the stored data. This makes Zabbix ideal for capacity planning." Web-based frontend; "equally true for small organizations with a few servers and for large companies."
- Official definitions (verbatim, from the Definitions chapter):
  - **host** — "any physical or virtual device, application, service, or any other logically-related collection of monitored parameters."
  - **host group** — "a logical grouping of hosts. Host groups are used when assigning access rights to hosts for different user groups."
  - **item** — "a particular piece of data that you want to receive from a host, a metric of data."
  - **trigger** — "a logical expression that defines a problem threshold and is used to 'evaluate' data received in items. When received data is above the threshold, triggers go from 'Ok' into a 'Problem' state. When received data is below the threshold, triggers stay in/return to an 'Ok' state."
  - **template** — "a set of entities (items, triggers, graphs, low-level discovery rules, web scenarios) ready to be applied to one or several hosts… to speed up the deployment of monitoring tasks."
  - **event** — "a single occurrence of something that deserves attention such as a trigger changing state or a discovery/agent autoregistration taking place."
  - **problem** — "a trigger that is in 'Problem' state."
  - **problem update** — "adding comment, acknowledging, changing severity or closing manually."
  - **action** — "a predefined means of reacting to an event. An action consists of operations (e.g. sending a notification) and conditions (when the operation is carried out)."
  - **escalation** — "a custom scenario for executing operations within an action; a sequence of sending notifications/executing remote commands."
  - **media** — "a means of delivering notifications; delivery channel." **notification** — "a message about some event sent to a user via the chosen media channel."
  - **remote command** — "a pre-defined command that is automatically executed on a monitored host upon some condition."
  - **web scenario** — "one or several HTTP requests to check the availability of a web site."
  - **agent autoregistration** — "automated process whereby a Zabbix agent itself is registered as a host and started to monitor."
  - **network discovery** — "automated discovery of network devices."
  - **low-level discovery** — "automated discovery of low-level entities on a particular device (e.g. file systems, network interfaces, etc)" with item/trigger/graph/host prototypes.
- Item types (collection mechanisms): Zabbix agent, simple check, SNMP agent, SNMP trap, Zabbix trapper, external check, HTTP agent, IPMI, SSH, Telnet, JMX, ODBC database monitor, calculated item, dependent item, script, browser. Value preprocessing before storage. History and trends storage.
- Frontend sections: Dashboards (widgets: problems, problem hosts, host availability, graphs, top hosts, trigger overview, maps, SLA report…), Monitoring (Problems — incl. cause and symptom problems; Hosts — graphs, host dashboards; Latest data; Maps; Discovery), Services (service tree, SLA), Inventory (host inventory), Reports (availability report, top 100 triggers, system information, audit log), Data collection (hosts, templates, discovery, maintenance, correlation), Alerts (actions, media types), Users (roles, permissions), Administration.
- Operational machinery: maintenance periods; problem acknowledgment and suppression; event correlation (trigger-based and global); trigger dependencies and severity levels; notifications with conditions/operations/recovery operations/escalations; remote commands; distributed monitoring via proxies; user-group permissions scoped by host groups.

### Nagios Core — evidence layer A (historical sample)

- Host checks: performed "at regular intervals, as defined by the check_interval and retry_interval options" plus on-demand (when an associated service changes state, as part of host reachability logic, for predictive dependency checks). Scheduled host checks are optional (check_interval = 0 disables them; on-demand checks still occur).
- Host states: "UP, DOWN, UNREACHABLE." DOWN vs UNREACHABLE distinguished via parent-host reachability logic "as it allows admins to determine root cause of network outages faster."
- Checks are performed by plugins, which return OK / WARNING / UNKNOWN / CRITICAL; these map to preliminary host states (OK→UP; WARNING→UP (or DOWN under aggressive checking); UNKNOWN/CRITICAL→DOWN), then post-processing via parent state determines final DOWN vs UNREACHABLE.
- State types: SOFT and HARD. "In order to prevent false alarms from transient problems, Nagios Core allows you to define how many times a service or host should be (re)checked before it is considered to have a 'real' problem" (max_check_attempts). SOFT states: logged, event handlers run, no notifications. HARD states: logged, event handlers run, "contacts are notified of the host or service problem or recovery."
- "Detecting and dealing with state changes is what Nagios Core is all about."
- Flapping: "When hosts change state too frequently they are considered to be 'flapping'… Nagios can detect when hosts start flapping, and can suppress notifications until flapping stops."
- Topic structure (TOC): plugins, active checks, passive checks, state types, time periods, network reachability, notifications, notification escalations, on-call notification rotations, event handlers, volatile services, freshness checks, distributed monitoring, redundant/failover monitoring, flapping detection, service/host clusters, host and service dependencies, state stalking, performance data, scheduled downtime, adaptive monitoring, predictive dependency checks, cached checks, object inheritance with templates, CGI authorization.
- Configuration is file-based object definitions (hosts, services, commands, contacts, timeperiods); UI is CGIs (status lists, problem lists).

### Prometheus — evidence layer A

- Positioning: "an open-source systems monitoring and alerting toolkit." Collects and stores metrics as time series "with the timestamp at which it was recorded, alongside optional key-value pairs called labels."
- Main features: multi-dimensional data model (time series identified by metric name + key/value labels); PromQL; no reliance on distributed storage; "time series collection happens via a pull model over HTTP"; pushing supported via an intermediary gateway; "targets are discovered via service discovery or static configuration"; multiple modes of graphing and dashboarding.
- Components: Prometheus server (scrapes and stores), client libraries, push gateway for short-lived jobs, special-purpose exporters (HAProxy, StatsD, Graphite, etc.), Alertmanager "to handle alerts."
- Rules run over stored data "to either aggregate and record new time series from existing data or generate alerts." Grafana or other API consumers visualize.
- Fit: "works well for recording any purely numeric time series. It fits both machine-centric monitoring as well as monitoring of highly dynamic service-oriented architectures." "Designed for reliability, to be the system you go to during an outage to allow you to quickly diagnose problems."

### Dynatrace (Infrastructure Observability) — evidence layer A

- Positioning: "Monitor hosts, VMs, processes, and networks to detect issues and improve infrastructure performance." Apps: Infrastructure & Operations, Kubernetes, Databases, Clouds.
- Concepts: Hosts — "Monitor infrastructure hosts across physical machines, VMs, and cloud instances to track health, performance, and resource utilization." Processes — CPU and memory usage trends on hosts and containers. Containers — "across Kubernetes and standalone hosts." Network devices. Extensions (technology coverage). Classic: process groups, container platform monitoring, VMware vSphere, message queues.
- Health alerts and warning signals: "Health alerts and warning signals categorize infrastructure events by severity." A health alert is "a critical event and requires immediate resolution… raises a health alert and triggers a problem in Problems for investigation." A warning signal is "a non-critical, informative event… If a warning signal is left unresolved, it can escalate to a health alert." Warning signals don't trigger problems.

## Cross-product Comparison

| Dimension | Datadog | Zabbix | Nagios Core | Prometheus | Dynatrace |
|---|---|---|---|---|---|
| Core monitored object | host (agent/cloud-reported), containers, processes | host ("any physical or virtual device, application, service, or… collection of monitored parameters") | host (network device/server) + service | target/instance (scrape endpoint), machine-centric or service-oriented | host (physical/VM/cloud instance), processes, containers, network devices |
| Estate inventory | Host List — "live inventory of all hosts reporting" | Hosts + Inventory section; autoregistration; network discovery | host definitions in config; reachability logic | targets via service discovery or static config | auto-discovered hosts/VMs/containers (suite) |
| Collection mechanism | Agent + cloud integrations + OTel | agent, SNMP, IPMI, SSH, HTTP, JMX, ODBC, trapper, external… (poll + trap) | plugins (active) + passive checks (NSCA) | pull over HTTP; push gateway; exporters | OneAgent (suite), extensions |
| Collected data | metrics, check/service-check status, events | items (metrics), web scenarios, events | check results (states), performance data | numeric time series | metrics, health events |
| Evaluation → state | monitors with alert/warning thresholds; detection methods (threshold/change/anomaly/forecast/outlier) | triggers (expressions) → Ok/Problem; severity levels | plugin codes → UP/DOWN/UNREACHABLE; SOFT/HARD via retries | alerting rules → alerts to Alertmanager | health alerts vs warning signals; triggers Problems |
| Notification | monitor notifications → email/Slack/PagerDuty; downtimes | actions (conditions + operations), media types, escalations, recovery ops | notifications to contacts; escalations; on-call rotations; time periods | Alertmanager (routing, grouping) | health alerts trigger Problems (suite handles response) |
| Problem lifecycle | monitor status page, manage monitors, muting | problem update: acknowledge, comment, severity change, manual close; suppression | HARD/SOFT states, flapping suppression, downtime | alert lifecycle in Alertmanager (firing/resolved) | Problems app (suite) |
| Visualization | dashboards, Host Map, Container Map | dashboards, graphs, network maps | CGI status lists; perfdata (addons) | expression browser, Grafana/consoles | suite apps (host/process/container views) |
| Reusable config | monitor templates, integrations | templates linked to hosts; LLD prototypes | object templates/inheritance | scrape configs, rule files, recording rules | extensions, auto baselines |
| Organization of estate | tags/facets, teams, saved views | host groups (also permission scope), tags | hostgroups, parents (topology) | labels (multi-dimensional) | management zones / suite entities |
| Deployment | SaaS | self-hosted (server/proxy/agent/frontend) | self-hosted daemon + CGIs | self-hosted binaries | SaaS/managed |

Cross-product commonalities (evidence layer B — present in ≥4 of 5):

1. A persistent inventory of monitored entities (hosts/devices/instances) — all 5.
2. Repeated collection of per-entity condition data (metrics and/or check results) — all 5.
3. Evaluation of collected data against configured conditions producing health/alert states — all 5.
4. Notification/alert delivery to people or channels — all 5 (in Prometheus via the separate Alertmanager component; in Dynatrace via Problems in the suite).
5. Dashboards/graphs of metric history — all 5 (Nagios Core weakest: CGI lists + performance-data addons).
6. Maintenance/downtime muting or suppression — Datadog (downtimes), Zabbix (maintenance periods), Nagios (scheduled downtime), Prometheus (Alertmanager mute-time intervals in route config — documented in Alertmanager configuration; not fetched this pass, so held weaker), Dynatrace (maintenance via suite settings — not fetched, held weaker).
7. Discovery/auto-registration of entities — Datadog (agent + cloud integrations auto-populate), Zabbix (network discovery, autoregistration, LLD), Nagios (manual config; network reachability logic), Prometheus (service discovery), Dynatrace (auto-discovery).
8. Severity classification of problems — Datadog (alert/warning thresholds), Zabbix (trigger severities), Nagios (WARNING/CRITICAL + SOFT/HARD), Dynatrace (health alert vs warning signal), Prometheus (labels on alerts; severity conventions — held weaker, convention not enforced).
9. Acknowledgment/handling of problems by operators — Datadog (monitor status, muting), Zabbix (acknowledge/update), Nagios (acknowledge via CGI/external commands — TOC-level), Dynatrace (Problems app), Prometheus (Alertmanager silences — TOC-level).
10. Reusable monitoring configuration (templates/integrations/rules) — all 5.

## Canonical Model (L0–L3)

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures:

1. **The monitored infrastructure entity inventory** — the system holds persistent, individually identified records of the infrastructure components under watch (machines, devices, instances). The entity is the unit of organization: metrics and states attach to it. Remove → a generic metrics/telemetry store with nothing it "watches" (Metrics Monitoring / TSDB territory).
2. **Continuous condition collection per entity** — the system repeatedly collects resource-condition telemetry from/about each entity over time (resource metrics and/or check results), building history. Remove → a static inventory/CMDB.
3. **Condition evaluation producing health/alert states** — collected data is evaluated against configured conditions (thresholds, expressions, check logic), yielding user-visible health/problem/alert states per entity, with state transitions. Remove → pure telemetry collection; the "monitoring" (watching for trouble) is gone.

Jointly-held is load-bearing:
- 1 alone = asset inventory/CMDB.
- 2 alone = metrics collection/TSDB.
- 3 alone = a rules engine with no subject.
- 1+2 without 3 = metrics monitoring/telemetry store.
- 2+3 without 1 = generic metric alerting with no estate.
- 1+3 without 2 = stateless pinger.

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Agents/collectors as the dominant collection mechanism, alongside agentless protocols (SNMP, IPMI, HTTP checks) and cloud integrations.
- The standard resource-metric set: CPU, memory, disk/filesystem, network I/O, processes.
- Threshold alerting with at least two severity tiers (warning vs critical) and state transitions.
- Notification delivery to channels/people with escalation paths and recovery notifications.
- Dashboards and per-entity metric charts; entity detail views.
- Estate organization: groups/tags; permission scoping by group.
- Discovery/auto-registration of entities; low-level discovery of sub-entities (filesystems, interfaces).
- Reusable monitoring configuration (templates, integrations, rule files).
- Maintenance windows / downtime muting.
- Problem acknowledgment and annotation.
- Availability reporting (uptime/availability reports, top-offender reports).

### L2 — Variant / Optional Structure

- Container/Kubernetes monitoring (modern; absent in classic products).
- Cloud-provider integrations (AWS/Azure/GCP inventory + metrics).
- Process-level monitoring.
- Topology/map views (host maps, network maps, parent/child reachability).
- Business-service trees and SLA reporting (service monitoring layer above entities).
- Distributed collection architecture (proxies, HA, federation).
- Anomaly detection, forecasting, outlier detection, AI classification.
- Remote commands / event-handler auto-remediation.
- Pull vs push collection model; agent vs agentless posture.
- Self-hosted vs SaaS deployment.
- Host inventory attributes (hardware/OS metadata).
- Log collection attached to the same estate (drifts toward Log Management).

### L3 — Vendor-specific (kept out of the final document)

- Datadog: Watchdog, Fleet Automation, DDSQL editor, Live Process view, Automatic Monitors, host aliases, monitor quality page.
- Zabbix: item keys, LLD macros, zabbix_sender/get, proxy HA, value mapping, browser items, cause-and-symptom problem model.
- Nagios: CGIs, NRPE/NSCA/NRDP addons, stalking, volatile services, aggressive host checking, freshness checks.
- Dynatrace: OneAgent, Smartscape, Davis, process groups, Problems app, ready-made alert classification setting.
- Prometheus: PromQL, exporter pattern, pushgateway, scrape config, recording rules.

## Historical / Market-Sample Check

Nagios Core (1999-era, agentless plugin checks, file config, CGI UI) satisfies all three L0 legs: host definitions (inventory), scheduled + on-demand plugin checks (collection), state determination with SOFT/HARD transitions and notifications (evaluation → state). It lacks agents, tags, dashboards-in-the-modern-sense, cloud, containers — all correctly held in L1/L2, not L0.

SNMP-era device monitoring (the Zabbix SNMP item types and "standardized templates for network devices" document this lineage; Nagios monitors routers/switches per its TOC) satisfies the same legs at the device level. Zabbix's own definition of "host" ("any physical or virtual device, application, service, or any other logically-related collection of monitored parameters") shows the entity concept is deliberately broader than "physical machine" — the canonical concept is the monitored infrastructure entity, not the server.

Prometheus (pull-based, label-centric, no built-in entity UI) still satisfies the legs: targets discovered and held (inventory), scraped series (collection), alerting rules (evaluation). Its entity layer is thinner — the target/instance label — which marks one end of a real spectrum: the entity inventory can be a first-class UI surface (Datadog/Zabbix/Dynatrace) or a configuration-level concept (Prometheus). Held as a variant of structure, not a boundary failure.

Conclusion: L0 survives the historical check. Modern additions (tags, containers, cloud, AI, SaaS) are NOT definitional.

## Vendor-specific Findings

See L3 above. Also product-philosophy differences worth recording:

- Datadog frames the alerting layer as a platform ("Alerting platform") spanning many data domains; infrastructure monitoring is one pillar.
- Zabbix makes the entity (host) the permission-scoping unit (host groups ↔ user groups) — monitoring as an access-controlled operational system.
- Nagios encodes network topology (parent hosts) into state semantics (DOWN vs UNREACHABLE) — monitoring as reachability diagnosis.
- Prometheus separates storage/query (server) from alert routing (Alertmanager) as independent components.
- Dynatrace classifies events into health alerts vs warning signals and hands critical ones to a separate Problems app — monitoring as the feeder of an incident pipeline.

## Boundary Findings

- **vs APM** (sibling, processed 2026-09-06): APM is request-centric — in-process instrumentation of application services, request/transaction semantics. Infrastructure monitoring is resource-centric — hosts/devices/instances keyed by resource condition. The APM pass records: "Remove in-process instrumentation & request semantics → Infrastructure Monitoring." Consistent with this pass.
- **vs Metrics Monitoring** (sibling, NOT yet processed): metrics monitoring is the generic capability of storing/querying/alerting on metric series; infrastructure monitoring organizes the metric layer around an infrastructure entity inventory with health states. A TSDB or metrics platform without an entity inventory and per-entity health states is not infrastructure monitoring. Joint review recommended when metrics-monitoring is processed.
- **vs Network Monitoring** (sibling, not yet processed): network monitoring specializes in network devices/links/traffic (SNMP, flow, latency). Infrastructure monitoring covers the whole estate including network devices as one entity class among others. Network monitoring is a specialization; the boundary leaf should record the overlap (Zabbix ships network-device templates; Datadog has Network monitors).
- **vs Server Management Platform** (sibling, not yet processed): management = control plane (patch, configure, provision, remote control); monitoring = observation plane (collect, evaluate, alert). Monitoring products include reaction hooks (Zabbix remote commands, Nagios event handlers) but as alert-driven automation, not as the primary purpose.
- **vs Incident Management** (sibling, processed 2026-09-08): ratified there — monitoring Types are "the detection side: observe conditions and emit alerts; no response loop, no mobilization, no disposition of record." This pass confirms: monitoring products end at alert state + notification + acknowledgment; the response loop belongs to Incident Management / On-call Management.
- **vs Observability Platform** (sibling, not yet processed): the observability platform is the umbrella suite bundling infrastructure metrics + APM + logs + tracing + RUM. Infrastructure monitoring is one pillar; suites realize it as a module (Datadog "Infrastructure Monitoring" product area, Dynatrace "Infrastructure Observability" app).
- **vs DEM** (sibling, processed 2026-09-08): DEM measures experienced quality from the consumption point; "resource metrics belong to" infrastructure monitoring (DEM pass wording). Consistent.
- **vs CMDB / IT Asset Management**: the monitoring inventory is operational and auto-discovered, oriented to current health; the CMDB is the authoritative configuration/asset record with relationships and change history. Zabbix's "Inventory" section and Datadog's host attributes are health-adjacent metadata, not asset records of record.
- **去掉什么就变成另一个 Type 的判据**:
  - Remove the entity inventory → generic Metrics Monitoring / TSDB.
  - Remove resource-condition semantics and go in-process/request-centric → APM.
  - Remove evaluation→state → telemetry collection pipeline.
  - Add the response loop (mobilize/coordinate/resolve) → Incident Management territory.
  - Narrow the estate to network devices/links/flows → Network Monitoring.
  - Add control-plane operations (patch/config/provision) as the primary purpose → Server Management.

## Uncertainties

- Exact severity-level taxonomies vary per product (Zabbix trigger severities, Nagios WARNING/CRITICAL, Datadog alert/warning thresholds, Dynatrace health-alert/warning-signal). The final document deliberately describes "at least two severity tiers" without asserting a universal scale.
- Prometheus's entity layer (targets/instances) is thinner than UI-first products; whether Prometheus alone (without Grafana) constitutes a full realization of the Type or the metrics pillar of it is a matter of framing. Held as a variant.
- Alertmanager mute-time/maintenance behavior and Dynatrace maintenance settings were not fetched this pass; maintenance muting is held as cross-product commonality from Datadog/Zabbix/Nagios direct evidence (3 products, layer B), with the other two weaker.
- The exact default retention/scoping behaviors (e.g., Datadog Host List "last 15 minutes" default activity window) are product-specific and kept out of the final document.
- Metrics Monitoring, Network Monitoring, Observability Platform, Server Management leaves are unprocessed; boundaries against them are stated from this pass's evidence plus ratified sibling passes, and joint reviews are recommended.

## Final Synthesis

Infrastructure Monitoring is the operations-side observation system whose defining core is three jointly-held structures: (1) a persistent inventory of monitored infrastructure entities, (2) continuous per-entity condition collection (resource metrics / check results), and (3) evaluation of that data against configured conditions producing health/alert states with transitions. Around this core, mature products add agents and agentless collection, the standard resource-metric set, severity-tiered alerting with notification/escalation, dashboards and entity detail views, discovery, templates, maintenance muting, and acknowledgment. The Type is bounded against APM (request-centric), Metrics Monitoring (no entity inventory), Network Monitoring (specialization), Server Management (control plane), Incident Management (response loop), and Observability Platforms (umbrella suite). The historical check (Nagios, SNMP-era device monitoring) confirms the core without modern additions.
