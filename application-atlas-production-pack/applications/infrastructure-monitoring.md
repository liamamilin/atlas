# Infrastructure Monitoring

## Overview

An **Infrastructure Monitoring** application is an operations-side observation system that watches a defined estate of infrastructure components — servers and virtual machines, containers, network devices, cloud instances — by keeping a live inventory of those components, continuously collecting their resource condition (metrics and check results), and evaluating that data against configured conditions to produce health and alert states.

Its purpose is to make infrastructure trouble visible before or as it happens: a disk filling up, a machine going down, a container restarting, a device becoming unreachable. The defining core is small:

```text
Monitored infrastructure entities (a live inventory of what is being watched)
└── Continuous condition collection per entity (resource metrics / check results, over time)
    └── Condition evaluation → health & alert states (with transitions)
```

Everything else commonly associated with the category — agents, tags, dashboards, containers and Kubernetes, cloud integrations, anomaly detection — is widespread in current products but is not what makes the product an infrastructure monitoring system. Older, agentless, self-hosted products from the dial-up-and-SNMP era satisfy the same core without any of those specifics.

When the primary measured unit shifts from resource condition to the requests flowing through application code, the product is drifting toward Application Performance Monitoring. When the system stops watching and starts mobilizing people to respond, it has crossed into Incident Management.

## Users & Context

Primary users are the people accountable for keeping infrastructure running:

- **System administrators / IT operations** — keep the estate healthy; configure what is monitored and what counts as a problem; triage alerts during business hours.
- **SREs / DevOps engineers** — treat the monitoring system as the operational truth source for the platforms they run; write alert conditions and dashboards as part of operating services.
- **NOC / operations-center operators** — watch standing problem consoles and wall displays; acknowledge, annotate, and route problems.

Secondary users:

- **Team leads / managers** — consume availability reports and trend views.
- **Capacity planners** — use accumulated metric history for trend and headroom analysis.

The work context is a standing operational surface: the console is kept open during the day, consulted during incidents, and arranged on wall displays in operations centers. The estate being watched may be a self-hosted data center, a cloud estate, or — most commonly today — a hybrid of both.

## Core Model

### The Defining Core

Three structures, jointly held. Remove any one and the product stops being infrastructure monitoring:

- **Monitored infrastructure entities.** The system holds persistent, individually identified records of the components under watch — a host, a virtual machine, a network device, a container, a cloud instance. The entity is the unit of organization: collected data, health states, and alerts all attach to it. The entity concept is deliberately broader than "physical machine" — one researched product defines a host as any physical or virtual device, application, service, or other logically-related collection of monitored parameters. Without the inventory there is nothing being watched — the product degenerates into a generic metrics store.
- **Continuous condition collection per entity.** The system repeatedly collects resource-condition telemetry from or about each entity — CPU, memory, disk, filesystem, network I/O, process and service state, reachability — and retains it as history. Collection runs on a schedule or on demand, through installed agents, agentless protocols, or cloud APIs. Without collection the inventory is static — an asset register, not a monitoring system.
- **Condition evaluation producing health/alert states.** Collected data is continuously evaluated against configured conditions — threshold comparisons, logical expressions, check results — and each entity (or each check on it) carries a user-visible health state that transitions between normal and problem levels. This is the "monitoring" itself: watching for trouble, not merely recording numbers. Without it the product is a telemetry pipeline.

### Standard Capabilities of Mature Products

These are present across the researched sample and expected by the market, but they are capabilities, not the definition:

- **Collection mechanisms** — an agent installed on the monitored machine is the dominant modern mechanism, alongside agentless protocols (SNMP and IPMI for devices, HTTP checks, SSH), cloud-provider integrations, and push endpoints for short-lived workloads.
- **The standard resource-metric set** — CPU, memory, disk usage and capacity, filesystems, network interfaces, load, processes.
- **Severity-tiered alerting** — conditions typically distinguish at least a warning level from a critical level, with the alert state transitioning between them; many products add further severity scales.
- **Notification and escalation** — problem states are delivered to people and channels (email, chat, paging services) according to routing rules, with escalation sequences when problems persist, and recovery notifications when they resolve.
- **Dashboards and entity detail** — charts of metric history at estate and per-entity level.
- **Estate organization** — groups and tags that organize entities, often doubling as permission scopes and alert-routing scopes.
- **Discovery** — automatic enrollment of entities: agent self-registration, network scanning, cloud-account sync, and discovery of sub-entities on a machine (filesystems, network interfaces, containers).
- **Reusable monitoring configuration** — templates, integrations, and rule files that attach a standard set of checks and thresholds to an entity class instead of configuring each machine by hand.
- **Maintenance windows** — scheduled muting of alerts for entities undergoing planned work.
- **Problem acknowledgment** — operators acknowledge, annotate, re-severity, or manually close problems, leaving a handling trail.
- **Availability reporting** — uptime percentages, availability reports, and top-offender lists computed from the collected history.

### One Structure, Many Implementations

The core model is conceptual. Implementations differ on every axis:

```text
Concept:   Monitored entity
Implementations:  agent-reported host, SNMP device, cloud instance,
                  scrape target, auto-discovered container/process

Concept:   Condition collection
Implementations:  installed agent (push), scheduled polling (pull),
                  SNMP/IPMI/HTTP probes, cloud API sync, push gateway

Concept:   Condition evaluation
Implementations:  static thresholds, logical expressions over metrics,
                  plugin check results, statistical anomaly/forecast rules

Concept:   Health/alert state
Implementations:  host UP/DOWN states, trigger Ok/Problem states,
                  monitor OK/Warning/Alert states, health-alert vs warning-signal classification
```

A reader who has only seen a modern SaaS agent product should still be able to recognize an agentless, file-configured, CGI-web-UI product from the same era as the same Application Type — the three core structures are identical.

## How It Works

### Establish the estate

```text
Register or discover entities
→ (install agents, or point agentless checks / cloud integrations at them)
→ attach a monitoring configuration (template / integration / rule set)
→ entities appear in the inventory and begin reporting
```

Enrollment ranges from fully manual (defining each monitored device in configuration) to fully automatic (agents self-register on install; cloud integrations sweep an account; network discovery finds devices). Discovery also applies inside a machine: filesystems, interfaces, and containers are found and given their own checks automatically.

### Collect and evaluate, continuously

```text
Scheduled collection cycle (poll or receive)
→ values stored as history per entity
→ evaluation of conditions against the data
→ entity/check health state set or transitioned
```

Collection and evaluation never stop. A condition crossing a threshold moves the associated check into a warning or problem state; sustained normal data returns it to normal. Many products add a deliberate delay before a problem is declared "real" — a check must fail repeatedly across retries before it counts as a confirmed problem — to keep transient glitches from paging anyone.

### Alert, route, mute

```text
Problem state confirmed
→ notification composed (entity, condition, severity, guidance)
→ routed to the people/channels scoped for that entity or tag
→ escalation sequence if unhandled
→ recovery notification when the state returns to normal
→ muted entirely during declared maintenance windows
```

Routing is driven by the estate organization: groups, tags, and severity decide who is woken up. Escalation sequences re-notify or widen the audience when a problem persists. Maintenance windows suppress the noise of planned work.

### Investigate and handle

```text
Operator opens the problem console
→ drills into the entity detail (metric charts, related checks, sub-entities)
→ acknowledges / annotates / re-severities the problem
→ resolves or waits for recovery
```

The entity detail view is the diagnostic heart: metric history around the problem time, the entity's checks and their states, its containers or processes, its position relative to other entities (topology, when the product offers it).

### Report

Availability reports, top-problem rankings, and capacity trends are computed from the accumulated history — the same data that drives the live states, read at management and planning cadence instead of operational cadence.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Entity list (the estate inventory)

The primary entry surface — a live list of everything being watched.

- typical information: entity name/identity, health state, tags/groups, key metrics, last-seen/activity, source (agent/cloud/protocol)
- primary actions: filter and search the estate, sort by health or metric, open an entity, save views

### Entity detail

The per-component workspace.

- typical information: identity and aliases, tags, metric charts (CPU, memory, disk, network), checks and their states, sub-entities (containers, processes, interfaces), collection status
- primary actions: inspect metric history over a time range, open related problems, mute/maintain, acknowledge

### Problem / alert console

The triage surface — what is currently wrong.

- typical information: open problems with entity, condition, severity, age, acknowledgment state
- primary actions: acknowledge, annotate, change severity, close manually, route/notify, mute

### Alert configuration

Where the watching rules are defined.

- typical information: condition definition (metric/expression/check), scope (which entities), thresholds and severity tiers, notification routing, escalation, permissions
- primary actions: create/edit/clone/disable alert rules, apply templates, test

### Dashboards

Composed views of metric history and current health for a team, service, or the whole estate.

- typical information: time-series charts, status summaries, top-N rankings, maps
- primary actions: arrange widgets, set time ranges, share

### Maps / topology (optional surface)

Spatial or relational views of the estate — hosts grouped and colored by metric or health, network diagrams with parent/child reachability.

### Reports

Availability and trend output for non-real-time consumption.

- typical information: uptime/availability per entity or group, most-frequent problems, capacity trends

### Administration

Users, roles, and permission scopes (often bound to entity groups), notification channels, collection infrastructure (proxies/collectors), data retention.

## Important Rules / Behaviors

### The entity is the anchor

Every datum, state, and alert attaches to an identified entity. This is what makes the system answer operational questions ("which machines are in trouble?", "what is the history of this host?") rather than only series questions ("what is the value of this metric?").

### Transient failure ≠ confirmed problem

Mature products distinguish a first detection from a confirmed problem: a check typically must fail across repeated attempts before notifications fire. State models in the researched sample formalize this as soft vs hard problem states, or as warning-before-critical tiers. The purpose is the same: keep transient glitches from paging people.

### States transition — and notify on transition

Health states move between normal and problem levels as data changes; notifications are tied to transitions (into problem, back to recovery), not to every collected value. Products commonly suppress notifications when an entity flaps — oscillating between states too frequently.

### Maintenance mutes, but collection continues

Scheduled maintenance windows suppress alerting for scoped entities while data collection and state evaluation continue underneath; the record of what happened during maintenance is preserved.

### The estate organization is load-bearing

Groups and tags are not cosmetic: in several researched products they scope permissions (who may see or configure which entities) and alert routing (who gets notified). Changing an entity's organization can change who gets woken up.

### Observation, not control

The system's primary output is states, alerts, and records — not changes to the monitored estate. Reaction hooks exist (alert-triggered remote commands or handler scripts in some products), but they are automation attached to alerting, not the primary purpose. The authoritative control plane for changing infrastructure belongs to management and deployment tools.

## Variants

Common shapes the Type takes; all keep the defining core intact:

- **Classic self-hosted, agentless-first** — file-configured checks over the network (SNMP, probes, plugins), CGI-era or web UI; the historical norm and still common in device-heavy estates.
- **Modern agent-based SaaS** — a collector agent streams rich per-host data to a hosted platform; tags organize the estate; cloud integrations sweep accounts; the vendor operates the storage and UI.
- **Open-source metrics stack** — pull-based collection into a local time-series store with a label-dimension data model; alerting handled by a separate routing component; visualization by companion tools. The entity layer is thinner (targets/instances) but the core structures hold.
- **Enterprise observability suite module** — infrastructure monitoring as one pillar of a suite alongside APM, logs, and tracing; auto-discovery populates the estate; critical events are handed to the suite's incident/problem layer.
- **Estate emphasis variants** — device-heavy (network/SNMP-centric), container/Kubernetes-heavy, cloud-heavy, hybrid data center. These change what is collected and which surfaces dominate, not the core model.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Application Performance Monitoring / APM | adjacent sibling | APM's measured unit is the request flowing through instrumented application code; infrastructure monitoring's unit is the resource condition of components. Remove in-process request semantics from APM and you are here. |
| Metrics Monitoring | adjacent sibling | generic storage/query/alerting over metric series with no notion of a watched estate; infrastructure monitoring organizes metrics around an entity inventory with per-entity health states. |
| Network Monitoring | specialization | confines the estate to network devices, links, and traffic; infrastructure monitoring covers network devices as one entity class among the whole estate. |
| Server Management Platform | adjacent | management is the control plane (patch, configure, provision, remote control); monitoring is the observation plane. Monitoring products may trigger remote commands as alert automation, but do not own configuration. |
| Incident Management | downstream | monitoring detects and notifies; incident management owns the response loop — mobilizing responders, coordinating the work, recording the disposition. Monitoring ends at alert state + acknowledgment. |
| Observability Platform | umbrella | bundles infrastructure metrics, APM, logs, tracing, and user monitoring into one suite; infrastructure monitoring is the resource-condition pillar of such suites. |
| Digital Experience Monitoring | complementary | measures experienced quality from the consumer side of the delivery path; resource metrics on the serving side belong here. |
| CMDB / IT Asset Management | adjacent | the CMDB is the authoritative configuration/asset record with relationships and change history; the monitoring inventory is operational, auto-discovered, and oriented to current health. |
| Capacity Management | downstream consumer | capacity planning is a planning discipline that consumes the accumulated history this Type produces. |

The most important boundary is with APM: the two are bundled in most observability suites and share dashboards and alerting machinery, but the measured unit differs — resource condition vs request behavior. The second most important is with Incident Management: monitoring produces and delivers problem states; it does not run the response.

## Representative Products

- **Datadog** (Infrastructure Monitoring) — modern commercial SaaS; agent + cloud integrations; tag-centric estate; monitors as the alerting layer.
- **Zabbix** — open-source, self-hosted classic; host/item/trigger model; agent and many agentless collection types; templates and discovery.
- **Nagios Core** — the historical ancestor; plugin checks over hosts and services; UP/DOWN/UNREACHABLE states with soft/hard problem confirmation.
- **Prometheus** — open-source pull-based metrics and alerting toolkit; label-dimension data model; separate alert-routing component.
- **Dynatrace** (Infrastructure Observability) — enterprise suite module; auto-discovered hosts/VMs/containers/processes; health alerts vs warning signals feeding a problems layer.

The defining core was checked against the historical sample (Nagios Core, SNMP-era device monitoring) to avoid over-fitting the definition to the modern agent-based SaaS pattern.

## Sources

Research date: **2026-09-08**

- Datadog — Infrastructure overview, Host List, Monitors, Monitor Types, Getting Started with Monitors: https://docs.datadoghq.com/infrastructure/ , https://docs.datadoghq.com/infrastructure/list/ , https://docs.datadoghq.com/monitors/ , https://docs.datadoghq.com/monitors/types/ , https://docs.datadoghq.com/getting_started/monitors/
- Zabbix — What is Zabbix, Definitions, Manual structure: https://www.zabbix.com/documentation/current/en/manual/introduction/about , https://www.zabbix.com/documentation/current/en/manual/definitions , https://www.zabbix.com/documentation/current/en/manual
- Nagios Core 4 — Host Checks, State Types, Table of Contents: https://assets.nagios.com/downloads/nagioscore/docs/nagioscore/4/en/hostchecks.html , https://assets.nagios.com/downloads/nagioscore/docs/nagioscore/4/en/statetypes.html , https://assets.nagios.com/downloads/nagioscore/docs/nagioscore/4/en/toc.html
- Prometheus — Overview: https://prometheus.io/docs/introduction/overview/
- Dynatrace — Infrastructure Observability, Health alerts and warning signals: https://docs.dynatrace.com/docs/observe/infrastructure-monitoring , https://docs.dynatrace.com/docs/observe/infrastructure-observability/health-alerts-warning-signals

> Sourcing note: all listed pages were fetched directly on the research date. Precise product-specific figures (default activity windows, exact threshold values, exact severity scales, retention defaults) observed in vendor documentation are intentionally not restated in this document; they remain in the paired Research Notes. Boundaries against three sibling Types (Metrics Monitoring, Network Monitoring, Observability Platform) are stated from this research plus previously ratified sibling passes; those leaves are documented separately.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical market-sample check are recorded in the paired Research Notes.
