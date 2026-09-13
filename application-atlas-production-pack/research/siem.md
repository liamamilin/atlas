# Research Notes — SIEM

Research date: 2026-09-09

## Research Goal

Understand what a SIEM (Security Information and Event Management) application actually is as an Application Type: its defining core structure, its standard operating loop, its interfaces, its rules and states, and — critically — its boundaries against the neighboring Types that share its substrate or its workflow (Log Management, XDR, SOAR, SOC Platform, EDR/NDR, Threat Intelligence, UEBA/Insider Risk).

## Initial Boundary (pre-research hypothesis)

- Hypothesis: a SIEM is the security team's central analytics system over the organization's own security-relevant event data — collect from everywhere, detect with security logic, investigate alerts.
- Likely confusions:
  - vs **Log Management** — same event substrate; the log-management pass (processed 2026-09-08) left a forward note: "SIEM must not treat log storage/search as SIEM-defining — vendors build SIEM ON the log corpus; the seam is the security analytics/detection/investigation layer."
  - vs **XDR** — the XDR pass (processed 2026-09-08) left a forward note proposing the seam: data authority (customer's own org-wide log plane vs vendor-curated security telemetry), who authors detection (customer analytics rules vs vendor-delivered content), response actuation (XDR through own instrumentation vs SIEM alert/hand-off). Convergence is real: one sampled XDR vendor folds SIEM+XDR into one portal.
  - vs **SOAR** — orchestration of response across tools vs analytics over event data.
  - vs **SOC Platform** — whole-operations layer vs the analytics system.
  - vs **EDR/NDR** — single-domain telemetry + response vs org-wide event plane.
- Unknowns going in: whether the case/incident object is definitional or common; whether owning the log store is definitional; how thin the investigation loop can be and still be a SIEM (open-source pole).

## Research Questions

1. What are the core objects? (data sources/connectors, events, normalized schema, detection rules, alerts/signals, incidents/cases, entities, threat intel, dashboards)
2. What is the canonical operating loop? (ingest → normalize → detect → triage → investigate → respond/hand-off)
3. Who authors detection content — customer, vendor, or both? How is it maintained?
4. What states/lifecycles exist on alerts and cases? What roles gate them?
5. What does the SIEM do that the underlying log platform does not?
6. Where does response live — inside the SIEM, in a bundled SOAR, or handed off?
7. What varies by segment/deployment/era (cloud vs self-hosted, ML depth, compliance reporting, managed-service tier)?
8. Historical check: does the definition hold for the pre-cloud SIEM generation (no ML, no ATT&CK, no OCSF, no SOAR, no cloud)?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / tier | Evidence level |
|---|---|---|
| Splunk Enterprise Security 8 | classic data-platform SIEM; SIEM+SOAR+TI convergence; large enterprise; on-prem + cloud | Tier-1 docs (About page + portal) |
| Microsoft Sentinel | cloud-native hyperscaler SIEM; content-hub model; converging into Defender portal | Tier-1 docs (overview, threat detection, incident investigation) |
| Elastic Security | open-source-rooted unified SIEM/XDR/endpoint; detection-as-a-program framing | Tier-1 docs (overview, detections, cases) |
| Datadog Cloud SIEM | SIEM as a layer on a shared observability/log platform (does not own a separate log store) | Tier-1 docs (Cloud SIEM overview) |
| Wazuh | open-source, self-hosted SIEM/XDR pole; mid-market; compliance-led | Tier-1 docs (getting started, platform/SIEM page) |

Considered and rejected/dropped: IBM QRadar (ibm.com/docs returned 403 twice — abandoned per source-access rule; legacy enterprise pole not directly examined, limitation recorded), Exabeam/Securonix/Sumo/Google SecOps (not needed — stop conditions reached), Wazuh's XDR framing (the EDR pass flagged Wazuh as a SIEM/XDR straddler; used here only as the open-source SIEM pole, its endpoint machinery treated as out-of-core).

## Sources

All fetched 2026-09-09 unless noted.

- Splunk — Enterprise Security 8 docs portal: https://help.splunk.com/en/splunk-enterprise-security-8 ; About Splunk Enterprise Security: https://help.splunk.com/en/splunk-enterprise-security-8/user-guide/8.7/introduction/about-splunk-enterprise-security ; legacy docs root: https://docs.splunk.com/Documentation/ES
- Microsoft — Sentinel overview: https://learn.microsoft.com/en-us/azure/sentinel/overview ; Threat detection: https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-built-in ; Investigate incidents: https://learn.microsoft.com/en-us/azure/sentinel/investigate-incidents
- Elastic — Security overview: https://www.elastic.co/docs/solutions/security ; Detections and alerts: https://www.elastic.co/docs/solutions/security/detect-and-alert ; Cases: https://www.elastic.co/docs/solutions/security/investigate/security-cases
- Datadog — Cloud SIEM: https://docs.datadoghq.com/security/cloud_siem/
- Wazuh — SIEM platform page: https://wazuh.com/platform/siem/ ; Getting started: https://documentation.wazuh.com/current/getting-started/index.html
- Attempted, failed: https://www.ibm.com/docs/en/qradar-on-cloud (403), https://www.ibm.com/docs/en/sqs (403) — IBM docs domain blocked; QRadar excluded from product-specific claims.

## Product Observations

### Splunk Enterprise Security 8 (Layer A)

- Self-description: "comprehensive threat detection, investigation, and response solution"; "combines the best features and functionalities of Splunk's Security Information and Event Monitoring (SIEM), Security Orchestration Automation and Response (SOAR), and threat intelligence management capabilities". (Note: Splunk's own docs expand SIEM as "Security Information and Event Monitoring" here; Datadog uses "Security Information and Event Management" — naming variance recorded.)
- "Built on the Splunk operational intelligence platform and uses the search and correlation capabilities, allowing users to capture, monitor, and report on data from security devices, systems, and applications. As issues are identified, security analysts can quickly investigate and resolve the security threats across the access, endpoint, and network protection domains." → SIEM as an app on a shared data platform; the security layer is the app.
- Benefits list: unified UX + integrated workflow for **case management, alert triage, investigation, and response**; taxonomy aligned to **OCSF**; **risk-based alerting** creating "high confidence alerts"; **alert aggregation using finding groups** mapped to rules based on common security frameworks/techniques; automation with Splunk SOAR.
- Main surfaces: **Mission Control** (analyst queue integrating the prior Incident Review page + Mission Control; overview of "detections, findings and investigations"), **Analytics** (dashboards), **Security content** page (manage security content and response plans), **Configure** (findings/investigations, threat intelligence data, SOAR data), **Search** (platform search).
- API exposes: "findings, investigations, risk scores, assets, and identities" → object model: findings (aggregated alerts), investigations (cases), risk scores, assets, identities.
- Related machinery: Security Content Update (ESCU — regularly updated threat detection content), Common Information Model (CIM — "shared semantic model to normalize and manage data"), User Behavior Analytics, Exposure analytics, federated search incl. Amazon Security Lake datasets, Cisco Talos Intelligence deployment, App for PCI Compliance, App for Fraud Analytics (risk-based alerting for fraud).

### Microsoft Sentinel (Layer A)

- Self-description: "cloud-native SIEM solution... combines AI, automation, and threat intelligence to support threat detection, investigation, response, and proactive hunting." Runs on the Azure Monitor/Log Analytics substrate (append-only platform; tamper-proofing inherited).
- Content model: "security content packaged in SIEM solutions that enable you to ingest data, monitor, alert, hunt, investigate, respond, and connect" — content hub with solutions from Microsoft and third-party vendors.
- Collection: out-of-box **data connectors** (Microsoft + non-Microsoft; CEF, Syslog, REST-API), custom connectors; **data normalization** via ASIM (Advanced Security Information Model) at query time and ingestion time.
- Detection: "threat detection rules that run regularly, querying the collected data and analyzing it to discover threats... collectively known as **analytics rules**. These rules generate **alerts**... Alerts contain information about the events detected, such as the **entities** (users, devices, addresses, and other items) involved. Alerts are aggregated and correlated into **incidents**—case files—that you can assign and investigate."
- Rule types: **Scheduled** (KQL queries on a schedule over a lookback window; threshold → alert), **NRT** (≈1-minute cadence), **Anomaly** (ML baselines; anomalies recorded to a table, not alerts), **Microsoft security rules** (create Sentinel incidents from alerts of other Microsoft security products), **Threat intelligence matching** (CEF/Syslog/Windows DNS events matched against domain/IP/URL indicators), **Fusion** (ML correlation of many low-fidelity alerts across products into high-fidelity incidents), **ML behavior analytics**. Templates from the content hub ("pre-built rule prototypes, designed by teams of security experts") — use as-is, customize, or write from scratch; export to ARM templates (rules as code).
- Investigation: "Microsoft Sentinel incidents are files that contain an aggregation of all the relevant evidence for specific investigations"; "a complete, full-featured case management platform". Incident details page: left panel (details, evidence: Events/Alerts/Bookmarks, entities), **Overview tab** (incident timeline, similar incidents, entities, top insights), **Entities tab** (entity dossier: info, timeline incl. alerts outside the incident, insights; add alerts to incident; add entity to TI; run playbook on entity), **Tasks** (SOC process standardization), **Activity log** (audit + comments), in-context **Logs** query panel, **investigation graph** (visual entity relationships, exploration queries, timeline). Roles: **Responder** required to investigate; **Contributor** to delete comments.
- Response: **automation rules** (central incident handling) + **playbooks** (Azure Logic Apps workflows; ServiceNow/Jira connectors); run manually or auto-triggered.
- Hunting: proactive search before alerts; results saved as **bookmarks**; hunting queries promotable to detection rules; Jupyter notebooks.
- Other: watchlists (customer data correlated into detections/hunting/playbooks), workbooks (interactive reports), UEBA insights, MITRE ATT&CK coverage visualization, threat intelligence integration, MSSP multi-tenancy via Azure Lighthouse.
- Era-current drift: Sentinel is converging into the Microsoft Defender portal ("unified security operations platform"); Azure-portal retirement announced for 2027. Custom detections positioned as the unified rule authoring experience across Sentinel + Defender XDR.

### Elastic Security (Layer A)

- Self-description: "unified security solution that unifies SIEM, XDR, endpoint security, and cloud security into a single platform"; SIEM use case = "a centralized platform for ingesting, analyzing, and managing security data from various sources"; third-party integration support to "centralize your security data". Runs on Elasticsearch/Kibana; cloud or self-managed.
- Detection: "The detection engine evaluates your data against detection rules and generates alerts when rule criteria are met. Rules can correlate events across all connected data sources to surface threats that no single data stream would reveal on its own." Rule types from field-value matches to event correlation and ML anomaly detection. Also surfaces alerts from its own endpoint protection (Elastic Defend) and **external alerts** from third-party tools (e.g., Suricata) — "a unified view of threats across your security stack".
- Detection program lifecycle (vendor-documented): confirm requirements → assess coverage gaps (MITRE ATT&CK coverage) → enable prebuilt rules → build custom rules → validate against historical data → monitor rule health → reduce noise (tune, exceptions, suppression, snooze). "A minimal viable detection program... is a meaningful outcome at any stage."
- Alerts: carry host/user/network contextual data; open/acknowledged/closed states with **closing reasons** (customizable); exceptions and alert suppression as security-specific capabilities.
- Investigation: **Timeline** (investigate events, build queries, add events from various sources, import/export for collaboration); **Cases** ("collect and share information about security incidents and investigations... attach alerts, document findings, and collaborate with your SOC team"; integrates external ticketing — Jira, ServiceNow, IBM Resilient; case metrics: total alerts, associated users/hosts, durations; attach events, TI indicators, Timelines, entities; detection rules can create cases directly via a connector; automated triage workflows).
- Entity analytics: risk for hosts/users/services; ML anomaly jobs feeding detection rules.
- Era-current: AI Assistant, Attack Discovery (LLM alert correlation), Agent Builder, Elastic AI SOC Engine.

### Datadog Cloud SIEM (Layer A)

- Self-description: "a security data analysis and correlation system. It enables your entire security operations team to view, detect, investigate, and respond to security issues. Leveraging Datadog's scalable platform, Cloud SIEM ingests telemetry from both cloud and on-premises systems using the Datadog Agent and API-based integrations." "Cloud SIEM continuously analyzes incoming data to detect threats, generate actionable security **signals**, and correlate them across multiple sources."
- Substrate pole: "Cloud SIEM is integrated with Datadog Log Management so you can choose the appropriate retention and querying capability for your security logs" (standard indexing / Flex Logs / Log Archives) — the SIEM is a security layer over a shared log platform, with cost-tiered storage as a first-class concern.
- Content: **Content Packs** — "a curated set of Datadog integrations designed for security teams... detection rules, out-of-the-box interactive dashboards, parsers, and SOAR workflows" + content-pack health monitoring (coverage-gap awareness).
- Overview page (SOC console): important signals + open cases + high-risk entities; content-pack health; top signals by geography/ISP; **MITRE ATT&CK coverage** (rule density, signals per tactic/technique); **detection rules performance** (MTTD KPIs, false-positive rates, rules by signal change, archived reasons incl. "True Positive: Malicious/Benign"); risk insights (top risky entities with risk scores, entity type breakdown); threat map.
- Triage: **Signal Explorer** (signals grouped by rule, severity-filtered); **Case Management** ("track signals that require further analysis"); signal states incl. "under review" and "archive" with archive reasons.
- Response: Security Workflows / SOAR workflows (automate investigation and remediation); detection-as-code blog track.
- Vendor research arm: Security Labs threat research feeding detections.

### Wazuh (Layer A)

- Self-description (SIEM page): "a centralized platform for aggregating and analyzing telemetry in real time for threat detection and compliance. Wazuh collects event data from various sources like endpoints, network devices, cloud workloads, and applications for broader security coverage."
- Capabilities: security log analysis ("aggregates, stores, and analyzes security event data to identify anomalies or indicators of compromise. The SIEM platform adds contextual information to alerts to expedite investigations"), vulnerability detection, security configuration assessment (CIS benchmarks), regulatory compliance (PCI DSS, NIST 800-53, GDPR, TSC SOC2, HIPAA).
- Features: alerting and notification ("correlates events from multiple sources, integrates threat intelligence feeds, and provides customizable dashboards and reports"), reporting.
- Architecture (docs): **agent** (endpoint collection) + **server/manager** (analysis: **decoders** normalize incoming logs, **rules** classify/match and raise **alerts**, CDB lists, MITRE ATT&CK tagging) + **indexer** (storage) + **dashboard** (visualize/alerts/threat-hunting). Capabilities beyond the SIEM core: FIM, malware detection, SCA, active response (scripted endpoint response), vulnerability detection, command monitoring, container security, system inventory, agentless monitoring, cloud log collection (AWS/Azure/GCP/O365/GitHub).
- Compliance documentation is a first-class section (per-framework pages mapping capabilities to controls).
- Straddler note (from EDR pass): Wazuh self-describes as SIEM/XDR; its agent/active-response machinery is EDR-shaped. Used here only as the open-source self-hosted SIEM pole. Notably, the sampled Wazuh documentation presents **no first-class case/incident object** — the investigation loop runs through alert review and event drill-down in the dashboard. This makes Wazuh the counter-shape proving the case object is common-mature, not definitional.

## Cross-product Comparison

| Structure | Splunk ES | Sentinel | Elastic | Datadog | Wazuh | Layer |
|---|---|---|---|---|---|---|
| Multi-source security event collection (connectors/agents/syslog/API) | ✓ (platform inputs + add-ons) | ✓ (data connectors, CEF/Syslog/REST) | ✓ (integrations, external alerts) | ✓ (Agent + API integrations) | ✓ (agents, syslog, cloud modules) | A→B |
| Normalization into a common schema | ✓ CIM; OCSF-aligned taxonomy | ✓ ASIM | ✓ ECS | ✓ (parsers in content packs) | ✓ decoders | B |
| Detection rules evaluated over collected data → alerts | ✓ (correlation searches; risk-based alerting) | ✓ (analytics rules: scheduled/NRT/anomaly/TI/Fusion/ML) | ✓ (detection engine, rule types) | ✓ (detection rules → signals) | ✓ (rules → alerts) | B |
| Vendor-maintained detection content + customer authoring | ✓ (ESCU content updates; custom content) | ✓ (content hub templates; custom rules; ARM export) | ✓ (prebuilt rule library; custom rules) | ✓ (content packs) | ✓ (default ruleset; custom rules XML) | B |
| Alert aggregation into higher-level records | ✓ (finding groups; risk-based alerting) | ✓ (alerts → incidents) | ✓ (alerts; cases attach alerts) | ✓ (signals; cases) | — (alerts only) | B (case object common, not universal) |
| Analyst triage queue with states/dispositions | ✓ (Mission Control analyst queue) | ✓ (incidents grid; status/severity/owner) | ✓ (alert states + closing reasons) | ✓ (Signal Explorer; under review/archive) | partial (severity filtering; no disposition state machine observed) | B |
| Investigation surface drilling into events/entities | ✓ (investigations; search) | ✓ (incident details, entity dossiers, graph, in-context logs) | ✓ (Timeline, entity flyouts) | ✓ (signal details → log explorer) | ✓ (dashboard drill-down, threat hunting) | B |
| Entity model (users/hosts/IPs) with risk/context | ✓ (assets & identities, risk scores) | ✓ (entities, entity pages, UEBA insights) | ✓ (entity analytics, risk) | ✓ (risky entities, risk scores) | partial (context added to alerts) | B |
| Threat intelligence matching/enrichment | ✓ (TI data management; Talos) | ✓ (TI analytics rule; TI integration) | ✓ (TI indicators; attach to cases) | ✓ (TI feeds) | ✓ (TI feeds, CDB lists) | B |
| Proactive hunting | ✓ (search; threat data sharing) | ✓ (hunting, bookmarks → rules) | ✓ (threat hunting tools) | ✓ (log explorer; security research) | ✓ (threat hunting use case) | B |
| UEBA / behavioral analytics | ✓ (UBA, behavioral analytics service) | ✓ (UEBA, anomaly rules, ML behavior) | ✓ (ML anomaly jobs, entity risk) | ✓ (risky entities) | — | B (depth varies) |
| MITRE ATT&CK mapping/coverage views | ✓ (framework-mapped finding groups) | ✓ (ATT&CK coverage page) | ✓ (ATT&CK coverage) | ✓ (ATT&CK coverage page) | ✓ (ATT&CK tagging in ruleset) | B |
| Dashboards/overviews + KPIs | ✓ (Analytics page) | ✓ (workbooks) | ✓ (dashboards) | ✓ (overview page, MTTD/false-positive KPIs) | ✓ (dashboards, reports) | B |
| Compliance reporting | ✓ (App for PCI) | ✓ (workbooks/audit; less foregrounded) | — (not foregrounded) | — (audit trail blog track) | ✓ (per-framework compliance docs) | B (segment-dependent emphasis) |
| Bundled response automation (SOAR-like) | ✓ (SOAR integration; response plans) | ✓ (automation rules + playbooks) | ✓ (workflows; cases connector) | ✓ (security/SOAR workflows) | ✓ (active response — endpoint-scripted) | B (depth/location varies) |
| Owns its data platform | ✓ (Splunk platform) | ✓ (Log Analytics substrate — hyperscaler-owned) | ✓ (Elasticsearch) | ✗ (shared Datadog log platform) | ✓ (indexer) | B (NOT definitional) |
| Cloud-only | ✗ (on-prem + cloud) | ✓ | ✗ (cloud or self-managed) | ✓ | ✗ (self-hosted; cloud optional) | B (NOT definitional) |
| Case/incident object as first-class record | ✓ | ✓ | ✓ | ✓ | ✗ (not observed) | B (common, not definitional) |

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the product stops being recognizable as a SIEM — three jointly-held structures:

1. **The organization-wide security event data plane** — central collection of security-relevant event/log data from across the organization's systems (endpoints, network, identity, cloud, applications — sources the SIEM does not itself run), as the analyzed subject. Remove → single-product telemetry (EDR/NDR territory) or nothing to analyze.
2. **Continuous security detection over that data** — detection logic (rules, correlation, analytics, threat-intel matching) evaluated against the collected events, producing security alerts. Remove → log management (same substrate, no security analytics layer).
3. **The analyst investigation loop over alerts** — alerts surfaced for human triage and investigated by drilling back into the underlying events and entities, with the outcome recorded. Remove → detection engine / alert feed; the "management" dies.

Jointly-held is load-bearing:
- 1 alone = log management / security data lake
- 2 without 1 = point detection products (IDS/EDR detection engines)
- 3 without 1+2 = case tool triaging nothing
- 1+2 without 3 = alert generator, not management
- 1+3 without 2 = log store with a case tool bolted on

Deliberately NOT in L0 (tested against the historical check): normalization schema, case/incident object, threat-intel matching, UEBA/ML, ATT&CK mapping, SOAR, compliance reporting, cloud delivery, big-data storage engine, hunting. A mid-2000s correlation-engine SIEM (multi-source event collection + correlation rules + alert console + investigation) satisfies all three legs with none of the modern machinery; Wazuh satisfies the core with no first-class case object; Datadog satisfies the core without owning a separate log store.

### L1 — Common Mature Structure

- Normalization into a common schema (CIM / ASIM / ECS / OCSF-class) enabling cross-source correlation
- Detection content libraries maintained by the vendor (content updates, content packs, rule templates) beside customer-authored rules; rules-as-code export
- Alert aggregation/correlation into higher-level records (incidents, finding groups, signals→cases)
- Entity model (users, hosts, IPs, files, services) with entity pages/timelines and entity risk
- Threat intelligence integration (indicator matching, enrichment)
- SOC overview surfaces: dashboards, ATT&CK coverage views, detection-performance KPIs (MTTD, false-positive rates)
- Proactive threat hunting with saved artifacts (bookmarks/timelines) promotable into detections
- UEBA/behavioral analytics (baselines, anomalies, risk scores)
- Retention management with cost-tiered storage
- Compliance framework mapping/reporting
- Outbound integration (ticketing, SOAR, notification)
- Role-based access (analyst/responder/contributor/admin-class roles)

### L2 — Variant / Optional

- Substrate ownership: own data platform vs shared log platform vs hyperscaler service substrate
- Deployment: cloud SaaS / self-hosted / hybrid / air-gapped
- Detection-authorship posture: vendor-content-heavy ↔ customer-authored ↔ open rule ecosystems
- Response depth: hand-off only ↔ bundled SOAR (playbooks/automation) ↔ endpoint-scripted response
- ML/anomaly depth: none → anomaly tables → full UEBA
- Compliance emphasis (regulated segments lead with it)
- Managed-service tier (MDR/MSSP multi-tenancy)
- AI assistance (era-current)
- Case-management depth (first-class case objects ↔ alert-review-only loops)

### L3 — Vendor-specific (research notes only)

- Splunk: Mission Control, findings/finding groups, risk-based alerting, ESCU, CIM, SPL, assets & identities, App for PCI/Fraud Analytics, SOAR apps, MCP server app.
- Sentinel: analytics rule type taxonomy (scheduled/NRT/anomaly/Fusion/ML behavior/Microsoft security/TI matching), ASIM, watchlists, workbooks, bookmarks, Logic Apps playbooks, automation rules, Defender-portal convergence timeline, ARM export, Lighthouse MSSP, incident comment limits (30k chars/comment, 100/incident — precise figures kept here only).
- Elastic: detection-engine rule types, Timeline, Elastic Defend, case closing reasons, `securitySolution:detectionsCloseReasons` setting, Agent Builder, Attack Discovery, EASE, ES|QL alerting distinction.
- Datadog: signals (naming), Signal Explorer, content packs + health monitoring, Flex Logs, Bits AI, Security Labs, MTTD KPIs, archive reasons taxonomy.
- Wazuh: decoders/rules XML syntax, CDB lists, active response scripts, SCA policies, agent enrollment machinery, Wazuh indexer/server/dashboard component split.

## Rejected Findings (anti-overfit)

- "SIEM = big-data search platform" — rejected: Datadog runs SIEM on a shared log platform without owning a separate store; the platform is substrate, not definition.
- "SIEM = cloud service" — rejected: Splunk Enterprise (on-prem), Elastic self-managed, Wazuh self-hosted all in-type.
- "SIEM = ML/UEBA" — rejected: historical generation and Wazuh pole lack it; held common/optional.
- "SIEM = ATT&CK-mapped detections" — rejected: era-current machinery; historical pole predates it.
- "SIEM = case management" — rejected as definitional: Wazuh pole runs the loop without a first-class case object; the case object is the common mature realization of the investigation loop.
- "SIEM = SOAR" — rejected: response automation is bundled in mature products but the orchestration-across-tools behavior is a different Type.
- "SIEM = compliance reporting" — rejected: segment emphasis, not structure.
- "Alerts are called X" — rejected: alerts/signals/notable events/findings are vendor naming over one structure.

## Boundary Findings

- **vs Log Management** (§14, processed): same event substrate is legitimate; the seam is the security analytics/detection/investigation layer. Vendors build SIEM ON the log corpus (Splunk ES on Splunk; Datadog Cloud SIEM explicitly integrated with Log Management; Sentinel on Log Analytics). Remove detection + investigation → Log Management. Honors the log-management pass's forward note.
- **vs XDR** (§15, processed): convergence is real (Splunk ES 8 folds SIEM+SOAR+TI; Sentinel converging into Defender portal; Elastic unifies SIEM+XDR). Seam per the XDR pass's forward note, confirmed from this side: data authority (org-wide event plane incl. non-security IT logs vs vendor-curated security telemetry), detection authorship (customer-controlled analytics rules vs vendor-delivered content), response actuation (SIEM alerts/hand-off vs XDR acting through its own instrumentation). Keep-both.
- **vs SOAR** (§15, unprocessed): SIEM detects and investigates; SOAR orchestrates response across external tools. Mature SIEMs bundle SOAR-like automation (playbooks, workflows, automation rules) — packaging, not identity. Forward note for the SOAR pass.
- **vs SOC Platform** (§15, unprocessed): the SIEM is the analytics system; the SOC platform is the whole-operations layer (process, workforce, metrics). Forward note.
- **vs Cyber Incident Response Platform** (§15, processed): that pass observed the case-management layer is delivered inside SIEM/SOAR/TI platforms; the SIEM's case object serves alert investigation, not the incident-response program record. Downstream relationship.
- **vs EDR/NDR** (§15, processed): single-domain telemetry + response vs org-wide event plane; EDR/NDR alerts are ingested INTO the SIEM as sources (Sentinel Microsoft security rules; Elastic external alerts; Splunk AWS Security Hub add-on).
- **vs Threat Intelligence Platform** (§15, unprocessed): SIEM consumes TI (matching analytics, enrichment); TIP manages/produces/distributes intel. Forward note.
- **vs UEBA / Insider Risk Management** (§15, processed): event-level analytics vs person-level risk records + disposition loop; IRM alerts export TO the SIEM (per that pass).
- **vs Vulnerability Management** (§15, unprocessed): VM assesses a known population; SIEM ingests scanner findings as events and may surface vulnerability context (Wazuh) — consumption, not the VM lifecycle.
- **vs DLP / CNAPP / BAS** (§15, processed): SIEM is the downstream consumer of their detections (per those passes' own boundary notes).
- **vs Network Monitoring / Observability** (§14, processed): same event-plane machinery, different purpose (security vs operations); the security purpose is what makes the analytics a SIEM.

## Uncertainties

- IBM QRadar unreachable (403 ×2) — the legacy enterprise on-prem pole is not directly examined; historical-generation reasoning kept conceptual, no QRadar-specific claims made.
- Wazuh's absence of a first-class case object is based on the fetched documentation set (docs TOC + platform page); not exhaustively verified against every Wazuh module. Held as "not observed in sampled docs", not as an absolute claim.
- Exact alert/incident state names, retention defaults, rule cadence limits, and pricing tiers deliberately not asserted (evidence would require deeper per-product fetches; precision rule applied).
- Sentinel's Defender-portal convergence is mid-transition (announced timeline); the SIEM surface description may shift again — recorded as era-current drift, not structural change.
- The historical check is conceptual (mid-2000s correlation-engine generation) because those products are EOL and their docs are not reliably reachable; the check relies on the well-documented structure of that generation rather than fresh fetches.

## Final Synthesis

A SIEM is the security team's analytics system over the organization's own security-relevant event data. Its defining core is three jointly-held structures: the org-wide security event data plane (multi-source collection of security-relevant events from systems the SIEM does not itself run), continuous security detection over that data (customer-controlled detection logic producing alerts), and the analyst investigation loop over alerts (triage, drill-down into events/entities, recorded outcomes). Everything else the market associates with SIEM — normalization schemas, vendor detection content, incident/case objects, entity risk, threat-intel matching, UEBA, ATT&CK coverage views, hunting, SOAR bundling, compliance reporting, cloud delivery, AI assistance — is common mature structure or variant machinery, not definition. The Type's sharpest seams: against Log Management (same substrate, no security analytics layer), against XDR (data authority + detection authorship + response actuation), against SOAR (analytics vs orchestration), and against the SOC platform layer (system vs operations).
