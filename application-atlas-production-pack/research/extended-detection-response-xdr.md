# Research Notes — Extended Detection & Response / XDR

## Research Goal

Understand what an XDR product really is as an application — not the marketing version — by studying how real products organize cross-domain security telemetry, detection, correlation, investigation, and response. Establish the boundary against EDR (closest sibling, flagged by the endpoint-detection-response-edr pass for joint review), SIEM, SOAR, NDR, and the §15 SOC-platform cluster.

## Initial Boundary (pre-research hypothesis)

- XDR = EDR extended beyond the endpoint to other security domains (network, identity, email, cloud apps/cloud workload), with cross-domain correlation into unified incidents, unified investigation, and response across domains.
- Users: SOC analysts, detection engineers, incident responders; smaller orgs via MDR service wrappers.
- Confusable with: EDR (endpoint-only), SIEM (org-wide log plane), SOAR (orchestration across tools), NDR (network domain), SOC Platform (whole-operations layer), Cyber Incident Response Platform (downstream case layer), MDR (service, not product).
- Known market concern: some "XDR"-labeled products are EDR with a new label — the definition must be able to exclude those.

## Research Questions

1. Which security domains do XDR products actually cover, and through what mechanisms (own sensors vs product components vs third-party ingestion)?
2. What are the core objects? (telemetry source, detection/alert, incident/case, entity/asset, response action, telemetry store/query)
3. How does cross-domain correlation actually work in products? Is a unified incident container universal?
4. What response actions exist beyond the endpoint, and do they act through the platform's own instrumentation or through integrations?
5. What is the investigation surface (timeline, entity pivots, raw-data query, attack-story visualization)?
6. Where is the seam vs SIEM, SOAR, and SOC platform?
7. Does the historical/market check hold — do pre-"XDR"-label multi-domain security platforms satisfy the same core?

## Representative Products

| Product | Why selected | Evidence tier reached |
|---|---|---|
| Microsoft Defender XDR | Platform-native bundle: own security product per domain, unified portal | Tier 1 — full operational docs (learn.microsoft.com), direct |
| Cortex XDR (Palo Alto Networks) | Endpoint-vendor XDR with own data lake, firewall/identity ingestion, third-party sources | Tier 1 via docs portal Q&A mechanism, direct |
| Stellar Cyber (Open XDR platform) | "Open XDR" pole: multi-vendor sensors/connectors, platform-first rather than endpoint-first | Tier 1 — architecture KB, direct |
| Bitdefender GravityZone XDR | Mid-market pure-play endpoint vendor extending EDR with cross-domain sensors | Tier 1/2 — support-portal TOC + page titles (content pages returned TOC-level; see Source-access Limitation) |

Diversity achieved: native-suite (Microsoft) vs endpoint-first vendor XDR (Cortex) vs open platform (Stellar Cyber) vs endpoint-vendor sensor extension (Bitdefender). Excluded: Trend Micro Vision One (docs.trendmicro.com timed out twice — abandoned per network rule), SentinelOne (public docs behind login), CrowdStrike (prior EDR pass recorded JS-only docs).

## Sources

- Microsoft: https://learn.microsoft.com/en-us/defender-xdr/microsoft-365-defender (fetched 2026-09-08); https://learn.microsoft.com/en-us/defender-xdr/incidents-overview (fetched 2026-09-08)
- Cortex: https://cortex-docs.paloaltonetworks.com/ docs portal with `ask` mechanism (fetched 2026-09-08), answer compiled from "What is Cortex XDR?" and "Cortex XDR architecture" pages
- Stellar Cyber: https://docs.stellarcyber.ai/ and https://docs.stellarcyber.ai/Common/Stellar-Architecture.htm (fetched 2026-09-08)
- Bitdefender: https://www.bitdefender.com/business/support/en/77209-79436-welcome-to-gravityzone.html (TOC-level, fetched 2026-09-08); nav-confirmed XDR pages: "eXtended Detection and Response (XDR)" (77209-376320-xdr.html), "XDR architecture" (77209-376363-edr-architecture.html), "Sensor installation and integration" (77209-452340-...), "Investigating Incidents" (77209-151142-...)
- Trend Micro Vision One: https://docs.trendmicro.com/... — two timeouts, abandoned

## Product A — Microsoft Defender XDR

### Key observations (Evidence layer A unless noted)

- Self-definition: "a unified pre- and post-breach enterprise defense suite that natively coordinates **detection, prevention, investigation, and response across endpoints, identities, email, and applications**".
- Domain components are first-class Microsoft security products: Defender for Endpoint (endpoints), Defender for Office 365 (email/collaboration), Defender for Identity + Entra ID Protection (identity), Defender for Cloud Apps (SaaS apps), Defender Vulnerability Management (exposure), Defender for Cloud (cloud infra), plus DLP, Insider Risk, App Governance.
- Cross-product layer: "correlates signals … stitch together the threat signals that each of these products receive and determine the full scope and impact of the threat; how it entered, what it affected, how it's currently impacting".
- Two signal kinds: **alerts** (signals from threat-detection activities, malicious or suspicious events) and **incidents** (containers of related alerts that "tell the full story of an attack"). Alerts can also arrive from external solutions via Microsoft Sentinel and Defender for Cloud.
- Correlation is automatic: "correlation engines and algorithms … automatically aggregate and correlate related alerts together to form incidents"; AI "continually monitor[s] its telemetry sources and add[s] more evidence to already open incidents".
- Incident presentation: timelines of alerts and raw events, tactics used, lists of involved/impacted users, devices and resources, visual representation of how the players interact, logs of automated investigation/response actions, evidence collections (accounts, devices, files, processes, TI), textual attack-story summary.
- Response: **automatic attack disruption** — correlates high-confidence signals from multiple workloads and applies containment automatically; documented example: malicious file detected on an endpoint → instructs the email security workload to scan and remove the file from all email messages → blocked suite-wide. **Self-healing**: automated remediation of impacted devices, identities, mailboxes. Automated investigation can auto-resolve alerts.
- Cross-domain hunting: query-language access (KQL) to raw signal/alert data across the components from one portal.
- Incident management: queue, triage, manage, split into tasks for team accountability.

## Product B — Cortex XDR (Palo Alto Networks)

### Key observations (Evidence layer A via docs portal; some positioning-level)

- Self-definition: an XDR platform providing "protection, detection, and response by analyzing data from Cortex endpoints **and third-party sources**", delivering visibility "across network, endpoint, cloud, third-party, and identity telemetry from a single interface".
- Telemetry by domain: endpoint (unified agent: NGAV, EDR, host firewall, device control, disk encryption, optional forensic collection/host insights); network (broker VM collecting/forwarding logs; traffic logs from next-gen firewalls, Prisma Access/GlobalProtect, external firewalls; centralized log storage in a native data lake); identity (Cloud Identity Engine feeding AD/Okta context into UEBA); cloud (cloud-scale storage; cloud malware-analysis service for unknown files).
- Detection: analytics generate alerts for post-intrusion threats and abnormal network behavior (e.g., port scans); identity detection covering initial-access TTPs via out-of-the-box ITDR.
- Investigation & response: "one interface to investigate and triage alerts, take remediation actions, and define policies"; automation actions available.
- Portfolio drift observed: vendor now positions Cortex XSIAM ("unified security operations") alongside XDR; XDR remains a documented product with its own docs space. Era-current packaging noted; XDR model itself intact.

## Product C — Stellar Cyber (Open XDR platform)

### Key observations (Evidence layer A)

- Self-definition: "a unified platform for Security Operations … unifying together key data, tools and alerts for analysis", automating "both threat detection (using AI and machine learning) and response".
- Collection architecture: **sensors** (Linux/Windows server sensors as agents; modular sensors configurable with log forwarding, network-traffic ingestion, IDS, sandbox, aggregator, vulnerability-scan features; historical dedicated network/security sensors) capture via port mirrors, taps, agents, Netflow/IPFIX, logs; **connectors** actively collect from external data sources (many categories: security tools, identity, cloud) — one connector type per external source.
- Normalization: everything becomes **Interflow** JSON records into a **Data Lake** organized into **indices** (raw indices per source class; a security index of enhanced data). Enrichment with TI, geo, host/user context; JA3/JA4 TLS fingerprinting for encrypted traffic.
- Detection: ML over the Data Lake generates **alerts**, scored by AI for prioritization; alert types organized by kill-chain stage, tactic, technique.
- Correlation: ML correlates disparate alerts into a **case** — "a set of multiple correlated alerts and entities constituting a potential unified security attack, ranked by a dynamically updated score".
- Response: configurable **firewall actions** — platform instructs firewall(s) to block malicious traffic; triggered manually from event display or by **automated threat-hunting playbooks**.
- Assets: servers/routers/hosts auto-registered from sensors as an asset registry with per-asset threat/performance views.
- Interfaces: home dashboard (kill-chain oriented), alerts page, case management, investigate/threat-hunting (search over indices with a field dictionary), respond (playbooks), visualize/dashboards, system. CLI + REST API surfaces.

## Product D — Bitdefender GravityZone XDR

### Key observations (Evidence layer A for structure via portal nav; content-page depth not reached — see limitation)

- Product line: "eXtended Detection and Response (XDR)" is a tier of the GravityZone endpoint platform; EDR and XDR are adjacent sections ("EDR / XDR") with separate XDR installation doc.
- Cross-domain reach is implemented as **sensors** installed/integrated into the platform, documented per domain: Office 365 sensor (email/collaboration), Active Directory sensor and Azure AD sensor (identity), AWS / Azure Cloud / Google Cloud Platform / CSPM sensors (cloud), XDR Network Sensor (virtual appliance), plus sensors for Intune, Google Workspace, Atlassian Cloud, mobile, extended email security.
- Incident investigation documented as a portal function ("Investigating Incidents"); endpoint response machinery (isolate, kill, quarantine, remote shell) inherited from the EDR base; custom detection rules and YARA rules available.
- MDR service tier exists as a separately documented service wrapping the platform.
- Limitation: article bodies returned TOC-only content; assertions kept coarse (structure-level, not operational-detail-level).

## Cross-product Comparison

| Dimension | Microsoft Defender XDR | Cortex XDR | Stellar Cyber | Bitdefender GravityZone XDR |
|---|---|---|---|---|
| Endpoint telemetry | own product component | own agent | server sensors (agents) | own agent (EDR base) |
| Network telemetry | via cloud-apps/infra components (not a network sensor product in sampled docs) | firewall/Panorama/Prisma/external firewall logs via broker VM | network-traffic sensors (taps/mirrors, Netflow) | XDR network sensor appliance |
| Identity telemetry | Defender for Identity + Entra ID Protection | identity engine (AD/Okta) → UEBA | connectors (identity sources) | AD / Azure AD sensors |
| Email telemetry | Defender for Office 365 | third-party sources | connectors | Office 365 sensor |
| Cloud/SaaS telemetry | Cloud Apps, Defender for Cloud | cloud-scale storage; cloud malware service | connectors + cloud sources | AWS/Azure/GCP/CSPM sensors |
| Third-party ingestion | via Sentinel/Defender for Cloud connectors | broker VM + third-party sources (explicit) | connectors (core design — "open") | limited (sensor list is vendor-curated) |
| Detection unit | alerts | alerts | alerts (scored, kill-chain organized) | alerts/detections |
| Correlation container | **incident** (attack story) | unified investigation (alerts→remediation; cases in the converged XSIAM line) | **case** (ML-correlated alerts+entities, dynamic score) | **incidents** |
| Investigation surface | incident page: timeline, tactics, entities, attack-story graph, evidence, automated-action logs; KQL hunting over cross-domain raw data | one interface: triage, investigation, remediation, data-lake queries | threat hunting over data-lake indices; event evidence display; field dictionary | incident investigation view |
| Cross-domain response | attack disruption (endpoint↔email↔identity↔cloud containment), self-healing, automated investigation | endpoint remediation actions + automated actions; policies | firewall block actions + playbooks | endpoint response inherited + sensor-scoped actions |
| Store/query layer | unified portal + raw-signal query (KQL) | native data lake | data lake (Interflow indices) | platform data layer (Security Data Lake product documented) |
| Packaging posture | native suite (own components per domain) | vendor-suite XDR + third-party | open platform (multi-vendor first) | endpoint platform + vendor-curated sensors |

### Stable commonalities (Evidence layer B — across all four sampled products)

1. Multi-domain security telemetry beyond the endpoint — every product: endpoint + network and/or identity and/or email and/or cloud, via own components, agents/sensors, or connectors.
2. Detection content producing analyst-facing **alerts** from that combined telemetry (not just forwarding third-party alerts).
3. Correlation of related alerts into a **single prioritized cross-domain container** (incident / case / unified investigation) representing one attack story — automatic, with entity linkage.
4. A **unified investigation console**: queue + incident detail with timeline/evidence/entities, plus query access to the underlying telemetry (hunting).
5. **Response beyond alerting**: actions executed through the platform against entities in the covered domains (endpoint containment everywhere; network blocking, email purge, identity actions, disruption automation in at least some products).
6. Normalized storage/enrichment layer with entity context (users/devices/apps/IPs) shared across domains.

### Not universal (Evidence layer B/C)

- Native-per-domain product components (Microsoft model) vs sensors vs connectors — implementation posture varies; only the *multi-domain signal base* is invariant.
- Automated containment/attack disruption (strong in Microsoft, present elsewhere as automation/playbooks; not the minimal core).
- Third-party-source openness (definitional posture for Stellar Cyber's branding, optional elsewhere).
- Built-in UEBA/behavioral analytics, TI enrichment, ATT&CK-style tagging (common mature, not defining — although kill-chain/technique organization is very widely present).
- Network-traffic sensor as a first-class appliance (Cortex, Stellar, Bitdefender yes; Microsoft's sampled docs cover network via SaaS/cloud components rather than an NDR sensor).

## Canonical Abstraction

### L0 — Defining Invariant

A security-operations application whose defining core is four jointly-held structures over the organization's security signals:

1. **The multi-domain security signal base** — the platform holds security telemetry from more than one security domain (endpoint plus at least one of network, identity, email/collaboration, cloud/SaaS), collected through the platform's own instrumentation (agents, sensors, product components) or controlled integrations. *Remove the cross-domain extension → EDR (or NDR/ITDR/CDR — single-domain types).*
2. **Cross-domain detection & correlation into a unified incident** — detection content operates over the combined telemetry, and related signals are automatically correlated into one prioritized container (incident/case) that spans domains and carries the attack story (entities, evidence, chronology). *Remove correlation into a unified container → separate domain consoles or a raw alert feed.*
3. **Unified cross-domain investigation** — the analyst investigates the incident in one console: chronology, involved entities, evidence, pivoting between entities/domains, and query access to the underlying telemetry. *Remove → alert forwarder/distributor.*
4. **Response across the covered domains** — response actions execute through the platform against entities in more than one domain (endpoint isolation, traffic blocking, identity disable, message removal, containment automation). *Remove → detection-and-alerting only; the "R" of XDR is gone.*

Jointly-held is load-bearing: (1) alone = log/SIEM territory; (2) without (1) = generic alert correlation; (1)+(2) without (3) = alert aggregator; (1)+(2)+(3) without (4) = detection platform, not detection & response; (3)+(4) without (1)+(2) = endpoint tooling.

### L1 — Common Mature Structure

- Normalized telemetry store with entity enrichment (asset/user/app registries) and query language / field dictionaries for hunting.
- Threat-intel enrichment; behavioral analytics (UEBA) over identity/entity behavior; ATT&CK/kill-chain-style tactic-technique organization of detections.
- Attack-story visualization (entity graphs, timeline).
- Automation: automated investigation/remediation, containment/disruption of active attacks, response playbooks.
- Third-party source ingestion beyond native sensors (degrees vary).
- AI analyst assistance (era-current).

### L2 — Variant / Optional Structure

- Packaging posture: native suite (own component per domain) vs endpoint-vendor sensor extension vs open multi-vendor platform.
- Origin pole: endpoint-first (EDR expanded) vs platform-first (collection/detection platform adding response).
- Deployment: SaaS-only vs on-prem/hybrid virtual appliances.
- Tenant scope: single enterprise vs MSSP multi-tenant.
- MDR service wrapping (service tier, not product structure).
- SIEM-convergence pole (vendor folds SIEM and XDR into one console/platform) — era-current drift, see Boundary Findings.

### L3 — Vendor-specific (research notes only)

- Microsoft: automatic attack disruption mechanics (endpoint detection → email purge instruction suite-wide), self-healing wording, Sentinel unification into the Defender portal, 30-day raw-signal window for cross-product hunting (precise number — kept product-specific).
- Cortex: WildFire cloud malware analysis, broker VM, Cloud Identity Engine, XSIAM portfolio drift.
- Stellar Cyber: Interflow record format, data-lake indices, JA3/JA4 fingerprinting, sensor profile system, firewall-action modes.
- Bitdefender: sensor-per-domain productization (O365/AD/AAD/AWS/Azure/GCP/Workspace/Intune/Atlassian sensors), GravityZone architecture, PHASR/IntelliZone, Security Data Lake product.

## Boundary Findings

- **vs EDR (closest sibling — discharges the joint-review flag raised by the EDR pass):** EDR's object domain is the endpoint estate; XDR's defining move is the multi-domain signal base + unified cross-domain incident + response in ≥2 domains. Same vendors sell both as tiers of one console — the boundary is object-domain breadth, not agent technology. Test: remove cross-domain telemetry/correlation/response → EDR; the EDR pass's four legs remain satisfied by EDR products regardless of the vendor also selling an XDR tier. **Keep both as separate Types.**
- **vs SIEM:** SIEM's center of gravity is the customer's own org-wide log plane (arbitrary sources, customer-authored analytics, compliance retention). XDR's center is vendor-delivered cross-domain detection content + response actuation over curated security telemetry. XDR products store normalized security telemetry (overlap is real); SIEMs add response increasingly (convergence is real — one vendor folds both into one portal; another positions a "unified security operations" platform). Proposed seam for joint review with the unprocessed SIEM pass: data authority (customer's log plane vs vendor's curated security telemetry) + who authors detection (customer rules vs vendor content) + response actuation through instrumentation.
- **vs SOAR:** SOAR orchestrates arbitrary third-party tools via playbooks/case management as its center; XDR's response acts through its own instrumentation/connectors, with light automation embedded. Embedded playbooks in an XDR do not make it a SOAR.
- **vs NDR / ITDR / CDR:** single-domain detection & response types; XDR's multi-domain signal base is the seam (a product covering only network → NDR).
- **vs SOC Platform / Cyber Incident Response Platform:** whole-operations layer (workflow, metrics, case management across the SOC) vs the detection/response product feeding it. Downstream case management can attach to XDR incidents; case-management-first products are a different Type.
- **"去掉什么就变成另一个 Type" 判据:** remove cross-domain extension → EDR; remove vendor content+response and keep the open log plane → SIEM; remove the unified cross-domain incident → a bundle of point products; remove investigation+response → monitoring/forwarding, below the Type.

## Historical / Market-Sample Check (§24 applied)

- The "XDR" label is era-current (coined ~2018–2019 by a network-security vendor). Pre-label thin ancestors exist and satisfy the core: early-2010s advanced-threat platforms combining network + email + endpoint detection with a central investigation console and endpoint containment (firewall-era equivalents of the same structure) — no cloud data lake, no AI, no ATT&CK tagging required by the core.
- Counter-shape check: an endpoint-only product re-labeled "XDR" fails leg 1–4 by design — matches the market criticism that some "XDR" is EDR rebranded; the definition correctly excludes it.
- Regional/deployment check: on-prem virtual-appliance platforms (sampled product offers on-prem deployment) satisfy the core without SaaS; small-business XDR tiers (sensor add-ons on an endpoint console) satisfy it too.
- No cloud/AI/ATT&CK/third-party-openness is in the core — all are L1/L2.

## Uncertainties

- Trend Micro Vision One not sampled (docs unreachable) — a major XDR vendor's operational model rests on cross-product commonality, not direct evidence in this pass.
- Bitdefender content pages returned TOC-level output; its operational details (response-action inventory per sensor, incident correlation mechanics) asserted at structure level only.
- Cortex XDR vs Cortex XSIAM packaging is actively converging; exact scope of "XDR" as sold may shift. Kept at model level.
- Exact per-product automation triggers/defaults (e.g., when containment fires automatically) were not uniformly documented; the doc keeps automation as common mature structure, not a universal rule.
- Network-domain coverage in Microsoft's model is via cloud/SaaS components in the sampled docs; a network-sensor-equivalent may exist elsewhere in the portfolio — kept out of the canonical model.

## Final Synthesis

XDR is best modeled as **the SOC's cross-domain detection-and-response product**: it assembles the organization's security signals from more than one domain (endpoint + others), runs detection content over them, correlates related signals into unified incidents that read as one attack story, gives analysts one console to investigate and query, and executes response against entities across those domains. Everything else — how domains are instrumented (own components vs sensors vs connectors), how open the platform is to third-party sources, how much is automated, whether a data lake and hunting language are exposed, whether an MDR service wraps it — is mature structure or variant, not definition.
