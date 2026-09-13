# SIEM

## Overview

A **SIEM** (Security Information and Event Management) is the security team's analytics system over the organization's own security-relevant event data. It centrally collects security events and logs from across the organization's systems, continuously evaluates that data against security detection logic, and gives analysts a console in which alerts are triaged, investigated against the underlying events, and resolved.

The defining structure is small:

```text
Organization-wide security event data plane
└── Continuous security detection over the collected events
    └── Security alerts
        └── Analyst investigation loop (triage → drill into events/entities → recorded outcome)
```

Everything else the market associates with SIEM — normalization schemas, vendor-supplied detection content, incident/case records, entity risk scoring, threat-intelligence matching, behavioral analytics, attack-technique coverage views, threat hunting, bundled response automation, compliance reporting, cloud delivery — is widespread in current products but is not what makes a product a SIEM. Older correlation-engine products with none of that machinery, and open-source products without a first-class case object, still fit the definition.

Two boundaries follow directly. When the analyzed data shrinks to a single product's own telemetry and response acts through that product's own instrumentation, the product is drifting toward a different Application Type (endpoint or network detection-and-response, or their cross-domain umbrella). When the security detection and investigation layer is removed and only collection, storage, and search remain, what is left is Log Management.

## Users & Context

The primary users are the members of a security operations function:

- **SOC analyst** — the daily operator: watches the alert queue, triages new alerts, investigates the ones that matter, escalates or closes the rest.
- **Detection engineer / security engineer** — authors and tunes detection rules, onboards data sources, manages coverage and rule health.
- **SOC manager / security lead** — oversees queues and workloads, tracks detection performance and coverage, reports upward.
- **Incident responders and threat hunters** — drill into raw events, reconstruct attack timelines, hunt proactively before alerts exist, and document what they find.

Secondary users include compliance and audit stakeholders (who consume the SIEM's reporting), IT administrators (who help onboard data sources), and managed security service providers, who operate one SIEM deployment on behalf of many customer organizations.

The work context is the security operations center (SOC). The SIEM is the SOC's primary working console: the place where the organization's security telemetry becomes visible, where suspicious activity is named, and where the response to it is coordinated. It runs continuously — detections evaluate incoming data around the clock, and the alert queue is worked in shifts.

## Core Model

### The Defining Core

Three structures, jointly held. Remove any one and the product stops being a SIEM.

**1. The organization-wide security event data plane.** The SIEM's subject matter is the stream of security-relevant events emitted by the organization's own systems — endpoints, network devices, identity providers, cloud platforms, applications, and security products. These sources are outside the SIEM itself; the SIEM collects their output through agents, syslog receivers, API-based connectors, and log forwarders, and holds the accumulated event corpus as the data everything else operates on. The scope is the organization, not one product: a SIEM that only saw one vendor's telemetry would not be doing what a SIEM does.

**2. Continuous security detection over that data.** Detection logic — rules, correlation conditions, behavioral analytics, threat-indicator matching — is evaluated against the collected events on an ongoing basis. When the logic matches, the SIEM raises a **security alert**: a record naming what was detected, the evidence behind it, a severity, and the entities involved (users, hosts, addresses, files). Detection is the layer that turns an event archive into a security instrument; it is also the layer the customer controls, by activating, customizing, and authoring detection logic.

**3. The analyst investigation loop over alerts.** Alerts are surfaced to people. An analyst reviews the queue, prioritizes, and investigates — drilling from the alert back into the underlying events, the entities involved, and their history — and records an outcome: a disposition, a closure reason, an escalation. The loop is what makes the system *management* rather than a detection engine feeding a notification pipe.

These three are load-bearing in combination:

```text
Data plane alone                      → log management / a security data lake
Detection without the data plane      → point detection products (IDS/EDR engines)
Investigation without 1 + 2           → a case tool triaging nothing
Data plane + detection, no loop       → an alert generator, not management
Data plane + loop, no detection       → a log store with a case tool bolted on
```

### Standard Capabilities

Mature products commonly carry most of the following. They make a SIEM practical; they do not define it.

- **Normalization** — incoming events from heterogeneous sources are mapped into a common schema (a shared field model for users, hosts, processes, network activity), so a single detection rule or query can span sources. Each major product maintains such a schema; the specific model is an implementation choice.
- **Detection content** — vendor-maintained libraries of prebuilt detection rules (updated as threats evolve), beside which customers author their own rules. Rule authorship is a spectrum: activate vendor content as-is, customize it, or write rules from scratch in the product's query language. Rules-as-code export for version-controlled management is common.
- **Alert aggregation** — related alerts are grouped into higher-level records (incidents, cases, finding groups) so analysts work one investigation, not forty duplicate alerts.
- **Entity model** — the people, hosts, addresses, and services appearing in events are held as addressable entities with their own pages: identity details, activity timelines, and commonly a risk standing accumulated from detections and analytics.
- **Threat intelligence** — indicator feeds (malicious domains, IPs, hashes) matched against collected events, and used to enrich alerts and investigations.
- **SOC overview surfaces** — dashboards summarizing alert volume by severity and source, detection coverage mapped to adversary-technique frameworks, and detection-performance measures such as time-to-detect and false-positive rates.
- **Threat hunting** — proactive search over the event corpus before any alert exists; hunting results are saved as reusable artifacts and commonly promoted into standing detection rules.
- **Behavioral analytics** — baselines of normal activity with anomaly detection layered on top, feeding entity risk and detection rules. Depth varies widely.
- **Retention management** — the event corpus is kept for a bounded period, with cost-tiered storage options in mature products; retention bounds how far back detection, hunting, and investigation can reach.
- **Compliance mapping** — mapping of collected and detected activity to regulatory frameworks, with reports demonstrating control monitoring. Emphasis varies by segment.
- **Outbound integration** — alerts and cases forwarded to ticketing systems, orchestration platforms, and notification channels.
- **Roles** — role-based access separating at minimum the people who investigate, the people who author detection and configuration, and the people who administer the platform.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently, and the vocabulary differs more than the structure:

```text
Concept:            Security event collection
Implementations:    endpoint agents, syslog receivers, cloud/API connectors, log forwarders

Concept:            Detection logic
Implementations:    scheduled query-language rules, streaming correlation rules,
                    anomaly/ML analytics, threat-indicator matching

Concept:            The alert
Implementations:    "alerts", "signals", "notable events", "findings" — one structure,
                    vendor naming varies

Concept:            The investigation record
Implementations:    incidents, cases, investigations — the common realization of the
                    investigation loop; some products run the loop directly on the
                    alert queue without a first-class case object
```

A reader who has only seen one product should still be able to recognize the others from the core model.

## How It Works

The SIEM's operating rhythm is a continuous loop with a maintenance cycle around it.

### Connect the estate

```text
Identify the sources worth watching
→ connect them (agent, syslog, API connector, forwarder)
→ confirm events are arriving and parsing correctly
→ map them into the common schema
```

Data-source onboarding is a permanent activity, not a setup step: new systems, new cloud services, and new security products all become new sources. Mature products monitor source health and surface coverage gaps, because a silent source is a blind spot.

### Author or activate detection

```text
Start from vendor-maintained detection content
→ activate rules for the threats that matter
→ customize thresholds, filters, and exceptions for the environment
→ author custom rules for environment-specific risks
→ validate new rules against historical data before enabling
```

Detection authorship is the customer's lever of control. Vendor content is a starting point and a maintenance stream; the customer decides what actually fires in their environment.

### Detect and triage

```text
Detections evaluate incoming events continuously
→ matching logic raises alerts with severity and entities
→ related alerts are aggregated into incidents/cases
→ analysts work the queue: prioritize, assess, dismiss the benign
```

Triage is where the noise battle is fought. Products provide severity ranking, grouping, deduplication, and — critically — mechanisms to suppress known-benign patterns so the same alert does not return daily.

### Investigate

```text
Open the alert or case
→ read the detection's logic and the evidence that matched
→ drill into the underlying events (query the corpus in context)
→ examine the entities involved: identity, activity timeline, risk
→ reconstruct the timeline; pull in related alerts and artifacts
→ record findings, comments, and saved queries as the record of the investigation
```

The investigation surface is the SIEM's depth. Every product provides a path from alert back to raw events without leaving the investigation context, entity dossiers with activity timelines, and a way to save what was found — as bookmarks, attached timelines, or case notes — so the investigation is documented and hand-off-able.

### Resolve and respond

```text
Decide the outcome: true positive / benign / false positive
→ close with a recorded reason
→ for confirmed threats: trigger response —
   automated playbooks/workflows, or hand-off to
   orchestration tooling, endpoint/identity controls, or the incident-response process
```

Response in a SIEM is most commonly orchestration-by-hand-off: the SIEM names and documents the threat; the actions that contain it are executed by other systems, whether automation bundled with the SIEM or separate tooling. Some products script responses directly on endpoints; that depth is a variant, not the norm.

### Maintain the program

```text
Review detection performance (volume, false-positive rates, time-to-detect)
→ tune noisy rules; add exceptions and suppression
→ review coverage against adversary-technique frameworks; close gaps
→ update content from the vendor's stream
→ manage retention and storage cost
```

This maintenance cycle is a defining part of living with a SIEM: detection programs are tended, not installed.

### Capability tiers

**Defining core** — without these, not a SIEM:

- organization-wide security event collection
- continuous security detection producing alerts
- the analyst investigation loop over alerts

**Standard capabilities** — present in most mature products:

- normalization, detection content libraries, alert aggregation, entity model, threat intelligence, overview dashboards and KPIs, hunting, behavioral analytics, retention management, compliance mapping, outbound integrations, roles

**Variant / optional** — depends on segment, deployment, and era:

- substrate ownership (own platform vs shared log platform vs cloud service)
- bundled response automation depth, endpoint-scripted response
- managed-service operation, multi-tenancy
- AI assistance (era-current)

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Alert / incident queue

The analyst's primary entry surface.

- lists alerts or aggregated incidents with severity, status, age, source rule, and entities
- primary actions: triage (prioritize, assign, change state), open for investigation, dismiss with a reason

### Alert / incident detail (investigation workspace)

The center of the investigation loop.

- detection logic that fired, matching evidence, severity and status, entity list
- embedded event query access, entity dossiers, timeline reconstruction, related-alert expansion
- primary actions: drill into events, inspect entities, add/remove related alerts, annotate, run response actions, close with a disposition

### Event search / exploration

Direct access to the event corpus.

- query language or faceted search over collected events, time-bounded by retention
- primary actions: search, filter, visualize, save queries, promote a query into a detection rule or a saved hunting artifact

### Entity pages

The per-object view of the estate's actors.

- identity details, activity timeline across sources, associated alerts, risk standing
- primary actions: review history, pivot to related alerts, add to watchlists or threat intelligence

### Detection rule management

The detection engineer's workbench.

- active rules and vendor rule templates, rule logic, schedules, exceptions, suppression, execution health
- primary actions: activate, customize, author, test against historical data, disable, export as code

### Data source / connector management

- available and connected sources, ingestion health, parsing/normalization status
- primary actions: connect a source, fix broken ingestion, review coverage gaps

### Dashboards / overviews

- alert volume and trends, coverage maps over adversary-technique frameworks, detection-performance KPIs, top risky entities
- primary actions: filter into the queue, customize views, export reports

### Configuration / administration

- roles and permissions, retention and storage tiers, integration endpoints, platform settings

## Important Rules / Behaviors

### Detection is customer-controlled logic

The customer decides what counts as a detection in their environment. Vendor content accelerates this but does not replace it: rules must be tuned to the environment's normal activity, and unreviewed vendor content is understood to be a starting point, not a finished program.

### Alerts are derived; the investigation record is durable

Alerts regenerate as conditions recur; they are derived from the event corpus. The durable artifacts are the investigation records — cases, notes, saved queries, dispositions — which document what was found and decided. Products differ in whether aggregation happens before the analyst (incidents) or during (cases), but the derived-versus-durable distinction holds throughout.

### Triage states and dispositions are first-class

Alerts and cases move through managed states (new/open → in-review → closed, with labels varying by product) and close with recorded reasons — true positive, benign, false positive. These dispositions feed back into tuning: a rule whose alerts are routinely dismissed as false positives is a rule to fix.

### Coverage is bounded by data

No source, no detection. The system can only detect what it collects, which is why source health monitoring and coverage-gap awareness are built into mature products — and why "connect more of the estate" is a permanent workstream rather than a completed task.

### Noise management is a permanent activity

Detection at organization scale produces volume; the practical value of a SIEM depends on suppressing the benign and surfacing the meaningful. Exceptions, suppression, thresholds, and grouping exist in mature products precisely because the raw alert stream is not workable without them.

### Retention bounds the past

Detection, hunting, and investigation can only reach back as far as retention keeps data. Cost pressure makes retention tiering a standard concern; the investigation window is a configured property, not an unlimited one.

### Roles gate the loop

Investigating, authoring detection, and administering the platform are separately permissioned in mature products. In multi-tenant operation (service providers), tenant boundaries are enforced on data and on the people who may see it.

### Response usually lives elsewhere

The SIEM's native output is the named, evidenced, documented threat. Containment actions are typically executed through integrations — orchestration platforms, endpoint and identity controls, ticketing systems — whether triggered manually by the analyst or automatically by rules. Products that act directly on endpoints through their own instrumentation are converging toward neighboring Types.

## Variants

- **Platform-owned SIEM** — the SIEM as an application on a dedicated security data platform the vendor also sells as a log/data platform; deep query languages, extensive app ecosystems.
- **Shared-substrate SIEM** — the SIEM as a security layer over a general log/observability platform; security and operations teams share one data estate, with retention cost management as a first-class concern.
- **Cloud-native service SIEM** — the SIEM as a managed cloud service on a hyperscaler substrate; on-demand scale, connector ecosystems, and convergence with the vendor's broader security portfolio.
- **Open-source / self-hosted SIEM** — the SIEM as self-managed software; agent-based collection, file-based rule authoring, compliance-led packaging; common in cost-sensitive and air-gapped environments.
- **Compliance-led deployments** — regulated segments where framework mapping and reporting drive the configuration.
- **Managed SIEM** — the SIEM operated by a provider on behalf of customer organizations, with multi-tenant isolation.
- **Converged security-operations platforms** — era-current packaging in which SIEM, response orchestration, threat intelligence, and cross-domain detection are sold as one platform; the SIEM core remains identifiable inside the bundle.

A variant remains a variant unless it changes the core users, objects, or loop — in which case it has become one of the neighboring Types below.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Log Management | same event substrate (collection, storage, search); lacks the security detection and investigation layer — vendors build SIEM on top of log platforms, which is exactly why the two are distinct Types |
| Extended Detection & Response / XDR | cross-domain security telemetry curated by the vendor, vendor-authored detections, response executed through the platform's own instrumentation; the SIEM holds the customer's org-wide event plane and customer-controlled detection logic — convergence is real and market-visible, but the seams hold |
| SOAR | orchestrates response across external tools with playbooks and case automation; the SIEM detects and investigates — mature SIEMs bundle SOAR-like automation, which is packaging, not identity |
| SOC Platform | the whole-operations layer (process, workforce, metrics) around security operations; the SIEM is the analytics system that layer operates |
| Endpoint / Network Detection & Response | single-domain telemetry with response through the product's own instrumentation; their alerts are among the sources a SIEM ingests |
| Threat Intelligence Platform | manages, produces, and distributes intelligence; the SIEM consumes it — matching indicators against events and enriching investigations |
| Cyber Incident Response Platform | the downstream program-level case and process layer for incident response; a SIEM's case object serves alert investigation, not the response program record |
| Insider Risk Management / UEBA | person-level risk records with a human disposition loop; the SIEM is event-level analytics — insider-risk alerts are commonly exported to the SIEM |
| Vulnerability Management | assesses a known asset population for vulnerabilities; the SIEM ingests scanner findings as events and may surface them, but does not own the vulnerability lifecycle |
| Network Monitoring / Observability | the same event-plane machinery aimed at operational health rather than security; the security purpose is what makes the analytics a SIEM |
| Data Loss Prevention / Cloud Security Platforms / Attack Simulation | producers of security findings that flow into the SIEM as sources; the SIEM is their downstream consumer |

The boundary with Log Management is the structural one (substrate vs security layer). The boundary with XDR is the strategic one, because the market is actively converging: the durable seams are data authority (whose telemetry, how broad), detection authorship (who writes the logic), and response actuation (whose instrumentation acts).

## Representative Products

- Splunk Enterprise Security
- Microsoft Sentinel
- Elastic Security
- Datadog Cloud SIEM
- Wazuh

The core model was checked against the older correlation-engine generation of SIEM products (no cloud, no ML, no modern schema frameworks) and against the open-source pole to avoid defining the Type by the current cloud-era implementation.

## Sources

Research date: **2026-09-09**

Primary vendor documentation (official product docs):

- Splunk — Enterprise Security 8 documentation: https://help.splunk.com/en/splunk-enterprise-security-8 (incl. "About Splunk Enterprise Security")
- Microsoft — Microsoft Sentinel documentation: https://learn.microsoft.com/en-us/azure/sentinel/overview , https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-built-in , https://learn.microsoft.com/en-us/azure/sentinel/investigate-incidents
- Elastic — Elastic Security documentation: https://www.elastic.co/docs/solutions/security , https://www.elastic.co/docs/solutions/security/detect-and-alert , https://www.elastic.co/docs/solutions/security/investigate/security-cases
- Datadog — Cloud SIEM documentation: https://docs.datadoghq.com/security/cloud_siem/
- Wazuh — SIEM platform page and documentation: https://wazuh.com/platform/siem/ , https://documentation.wazuh.com/current/getting-started/index.html

> Sourcing limitation: IBM's documentation site (QRadar family) was not reachable from the research environment (403 on two attempts) and was abandoned per the network-restriction rule. No product-specific claims are made about it. The legacy enterprise on-prem generation of SIEM products is therefore represented conceptually (via the historical check) rather than by direct documentation evidence. Precise operational details — exact state names, retention defaults, rule cadence limits, pricing — are intentionally not asserted in this document; they vary by product and were not uniformly verified.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis against neighboring Types are recorded in the paired Research Notes.
