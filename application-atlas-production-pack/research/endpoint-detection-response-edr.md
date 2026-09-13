# Research Notes — Endpoint Detection & Response / EDR

Research date: 2026-09-08
Directory leaf: "Endpoint Detection & Response / EDR" (§15 Cybersecurity, Identity & Trust)
Slug: endpoint-detection-response-edr

## Research Goal

Understand what an EDR actually is as an Application Type: what it instruments, what telemetry it collects, how detections are produced and shaped, how analysts investigate, what response actions exist and how they reach the endpoint, how the product is configured and governed, and how the Type is bounded against EPP, XDR, SIEM, CWPP, NDR, Threat Hunting, Digital Forensics, Cyber Incident Response, and UEM.

## Initial Boundary

Working hypothesis at start:

- EDR = security-operations software that (1) instruments endpoints with a sensor, (2) detects malicious/suspicious behavior in endpoint telemetry, (3) supports investigation of what happened, (4) executes response actions on the endpoint remotely.
- Users: SOC analysts, threat hunters, incident responders, security admins.
- Nearest neighbors: EPP (prevention-first sibling), XDR (cross-domain umbrella), SIEM (log aggregation), CWPP (server workloads — processed, boundary flag recorded), NDR (network path), Threat Hunting (proactive workflow), Digital Forensics (offline evidence — processed), Cyber Incident Response Platform (case management — processed), UEM (device management, §14).

Pre-existing boundary obligations from earlier passes:

- cloud-workload-protection-cwpp (processed): "the Type boundary rests on object domain + operational workflow (user endpoints vs the server/container estate), not on agent technology; record so the EDR pass does not absorb CWPP on mechanism grounds."
- cyber-incident-response-platform (processed): "detection is the SIEM/EDR's job, this Type takes over when signals become a managed incident."
- digital-forensics-platform (processed): preserved-copy examination vs "live-system analysis/EDR territory."
- browser-security-platform (processed): "remove session binding → EDR."

## Research Questions

1. How are endpoints instrumented (agent/sensor forms, OS coverage, sensor-only variants)?
2. What telemetry is collected, where does it live, how long is it kept?
3. What is a detection/alert — how produced, what does it contain, how are alerts organized (aggregation/cases)?
4. What is the investigation workflow (alert → entity → timeline/lineage → raw telemetry query)?
5. What response actions exist, how are they executed, how are they tracked?
6. What policy/configuration model governs the estate (groups, tags, policies, roles)?
7. How does prevention (EPP) coexist with EDR in the same product?
8. What automation and managed-service layers exist?
9. What integrations exist (SIEM/XDR/TI/APIs)?
10. Where are the boundaries vs the neighbor Types listed above?

## Representative Products

| Product | Pole | Evidence obtained |
|---|---|---|
| Microsoft Defender for Endpoint | platform-native EDR inside a broader XDR portal; enterprise; deep public docs | A — four Microsoft Learn pages fetched in full |
| Sophos EDR / XDR (Sophos Central) | EPP-converged mid-market suite with EDR/XDR tier and MDR service | A — five Sophos Central help pages fetched in full |
| CrowdStrike Falcon (Falcon Insight) | cloud-native pure-play market leader | B/Tier 2 — product page only (docs portal JS-only, 1 failure; abandoned) |
| Wazuh | open-source, self-hosted (or cloud) SIEM/XDR-branded platform with EDR-like endpoint machinery | A — docs index + capability pages fetched |

Selection rationale: platform-native vs pure-play vs suite vs open-source; cloud vs self-hosted; enterprise vs mid-market; EPP-converged vs sensor-only variant. SentinelOne was attempted (support portal transport error; www 403) and abandoned after 2 failures — market context only. Elastic Defend was attempted (guide URLs 404 ×2) and abandoned. Cortex XDR docs were reachable but the ask interface timed out twice and space URLs 404'd — abandoned after 3 failures; not sampled.

## Sources

Tier 1 (fetched in full, 2026-09-08):

- Microsoft Learn — Defender for Endpoint overview: https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-endpoint
- Microsoft Learn — Overview of endpoint detection and response capabilities: https://learn.microsoft.com/en-us/defender-endpoint/overview-endpoint-detection-response
- Microsoft Learn — Take response actions on a device: https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts
- Microsoft Learn — Investigate alerts: https://learn.microsoft.com/en-us/defender-endpoint/investigate-alerts
- Microsoft Learn — Advanced hunting overview (Defender XDR): https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-overview
- Sophos Central Admin help — EDR and XDR: https://docs.sophos.com/central/customer/help/en-us/ManageYourProducts/XDR/index.html
- Sophos Central Admin help — Endpoint: https://docs.sophos.com/central/customer/help/en-us/ManageYourProducts/EndpointProtection/index.html
- Sophos Central Admin help — Detections: https://docs.sophos.com/central/customer/help/en-us/ManageYourProducts/ThreatAnalysisCenter/Detections/index.html
- Sophos Central Admin help — Cases: https://docs.sophos.com/central/customer/help/en-us/ManageYourProducts/ThreatAnalysisCenter/Cases/index.html
- Wazuh documentation — Active Response: https://documentation.wazuh.com/current/user-manual/capabilities/active-response/index.html
- Wazuh documentation — Malware detection: https://documentation.wazuh.com/current/user-manual/capabilities/malware-detection/index.html
- Wazuh documentation — index: https://documentation.wazuh.com/current/index.html

Tier 2 (positioning only):

- CrowdStrike Endpoint Security product page: https://www.crowdstrike.com/products/endpoint-security/falcon-insight-edr/ (the /products/endpoint-security/ page was returned; Falcon Insight EDR positioning embedded)

Source-access limitations:

- CrowdStrike docs portal (docs.crowdstrike.com) is a JS-only application — no operational documentation reachable. All CrowdStrike findings are positioning-level; no operational claims are made from CrowdStrike.
- SentinelOne unreachable (support portal transport error; www.sentinelone.com 403). Not sampled.
- Elastic Defend guide URLs 404. Not sampled.
- Cortex XDR docs reachable but query interface timed out twice; not sampled.
- Consequence: response-action vocabulary and investigation surfaces are evidenced by 2 products in operational depth (Microsoft, Sophos) plus 1 open-source product (Wazuh); market-leader operational detail is under-evidenced and is NOT filled from model memory.

## Product Observations

### Microsoft Defender for Endpoint (evidence layer A)

Positioning (overview page):

- "enterprise endpoint security platform designed to help organizations prevent, detect, investigate, and respond to advanced threats on their endpoints. These endpoints include laptops, phones, tablets, PCs, access points, routers, and firewalls."
- Feeds endpoint signals into the unified Microsoft Defender XDR portal, which correlates with identity, email, cloud workload alerts into incidents.
- OS coverage: Windows, macOS, Linux, Android, iOS. Licensing tiers (Plan 1 / Plan 2 / Defender for Business) gate capability sets.

EDR capability page:

- "Endpoint detection and response capabilities ... provide advanced attack detections that are near real-time and actionable. Security analysts can prioritize alerts effectively, gain visibility into the full scope of a breach, and take response actions to remediate threats."
- "When a threat is detected, alerts are created in the system for an analyst to investigate. Alerts with the same attack techniques or attributed to the same attacker are aggregated into an entity called an incident."
- Explicitly NOT an auditing/logging solution: "Our sensor has an internal throttling mechanism, so the high rate of repeat identical events don't flood the logs."
- Telemetry: "continuously collects behavioral cyber telemetry. This includes process information, network activities, deep optics into the kernel and memory manager, user login activities, registry and file system changes, and others. The information is stored for six months, enabling an analyst to travel back in time to the start of an attack. The analyst can then pivot in various views and approach an investigation through multiple vectors." (six-month retention is a product-specific number — recorded here, not generalized)
- "Inspired by the 'assume breach' mindset."
- Automatic attack disruption (XDR-level): automatic containment incl. device isolation, user containment, IP containment.

Response actions page (device page actions):

- Manage tags; Initiate automated investigation; Initiate live response session ("instant access to a device through a remote shell connection ... collect forensic data, run scripts, send suspicious entities for analysis, fix threats, and hunt"); Collect investigation package (zip: autoruns/ASEPs, installed programs, network connections, prefetch, processes, scheduled tasks, security event log, services, SMB sessions, system info, temp dirs, users/groups); Run antivirus scan (quick/full); Restrict app execution (code-integrity policy allowing only Microsoft-signed files; reversible); Isolate device (full or selective; "disconnects the compromised device from the network while retaining connectivity to the Defender for Endpoint service, which continues to monitor the device"; automatically lifted after seven days; offline retry up to three days; user notification shown); Contain device (unmanaged devices: all onboarded devices block comms with the contained device); Contain user (blocks attack-related protocols on onboarded devices; automatic via attack disruption); Contain IP; Consult a threat expert.
- Action center: tracks each action's status, submitting user, success/failure.
- Permissions: "You must have at least the Active remediation actions role assigned"; device-group-scoped access; high-value assets can restrict specific actions.
- Plan 1 / Defender for Business include only a reduced manual action set (scan, isolate, stop & quarantine file, add indicator) — plan-gated capability depth.

Alert investigation page:

- Alerts queue → alert page: title, affected assets, details pane, alert story.
- Alert story: "details why the alert was triggered, related events that happened before and after, as well as other related entities"; entities clickable/expandable; actions available per entity.
- Alert timeline complements the process tree view ("condensed chronological view ... rapid triage").
- Resolution: mark Resolved, classify True/False alert, select determination; suppression rules for recurring false alerts.

Advanced hunting (XDR portal page):

- "query-based threat hunting tool ... explore up to 30 days of raw Defender XDR data"; guided (query builder) and advanced (KQL) modes.
- "You can use the same threat hunting queries to build custom detection rules. These rules run automatically to check for and then respond to suspected breach activity, misconfigured machines, and other findings."
- RBAC-gated; quotas (30-day range, row/time/CPU limits — product-specific numbers, not generalized).
- Endpoint data access governed by Defender for Endpoint RBAC.

### Sophos EDR / XDR (evidence layer A)

Positioning (EDR and XDR page):

- "Sophos EDR, XDR, and XDR Sensor enhance your threat detection and response capabilities."
- Both EDR and XDR: "Investigate detected threats. Search for new threats or security weaknesses. Monitor devices and fix issues remotely."
- XDR adds: third-party product data integrations + AI assistant.
- Features live in the Threat Analysis Center.
- XDR Sensor: "an alternative way to get the XDR features. You don't get threat protection, but you do get some of the detection, investigation, and response functions. You can run Sophos XDR Sensor alongside existing anti-malware." — a sensor-only variant without the prevention stack.
- Live Discover: "run queries about the software installed, processes running, registry changes, and more" — on devices (online) or on the Data Lake ("stores device data in the cloud ... query devices even when they're not connected, schedule your queries, and query data from multiple Sophos products").
- Live Response: "connect directly to an individual device to investigate and fix possible security issues."
- Threat graphs: "investigate and clean up malware attacks. You can find out where an attack started, how it spread, and which processes or files it has affected."
- Cases: "group together suspicious events reported by our Detections feature and help you or the MDR team do forensic work on them. We create cases for you automatically, but you can also create your own."

Detections page:

- "Detections identify activity on your devices that's unusual or suspicious but hasn't been blocked. They're different from events where we detect and block activity that we already know to be malicious." — the detection-vs-prevention distinction stated by the vendor itself.
- "We generate detections based on data that devices upload to the Sophos Data Lake. We check that data against threat classification rules. When there's a match, we show a detection."
- Detection list fields: severity; type (Threat / Vulnerability); detection name; time; entity (device); category (Endpoint, Network, Firewall, Email, Cloud, ID provider, Platform); source (Sophos or third-party); MITRE ATT&CK tactic/technique.
- Detection details pane: raw data tab; lineage tab; quick actions (open device details, detections on device); pivot queries (Live Discover on-device or Data Lake); enrichments (VirusTotal, SophosLabs Intelix reports); actions ("scan a device or start Sophos Live Response to access and investigate a device"); similar detections.
- Add detections to a case (existing or new: name, description, severity, status New/Investigating, assignee).

Cases page:

- Auto-created cases: "We create a case when there's a high-risk detection if it hasn't already been included in a case on the same day. We add later detections to the case if they share the same detection type."
- Managed by Sophos (MDR team investigates and responds) vs Self-managed (customer assigns an administrator).
- Severity levels (Critical "confirmed compromise" → Info); status sets differ for Sophos-managed (Investigating / Action required / Resolved) vs self-managed (Investigating / On Hold / Resolved).
- Case details tabs: Overview (detections count, MITRE tactics, devices/users affected, case summary, command line run by the threat, recent activity), Detections, Notebook (investigator's notes), Messages (MDR team correspondence), History.
- MDR service: "our analysts monitor your environment for malicious activity and contact you or respond on your behalf 24/7."

Endpoint product page:

- Endpoint Protection via policies applied to users/devices: Threat Protection, Application Control, Peripheral Control, Web Control, Data Loss Prevention, Update Management, Windows Firewall, Endpoint DNS Protection, and a "Data Collection and Investigation policy" (the EDR telemetry policy).
- Computers, Computer Groups as the device-organization layer.

### CrowdStrike Falcon (evidence layer B/Tier 2 — positioning only)

- "AI-native endpoint protection and EDR on the CrowdStrike Falcon® platform: stopping ransomware, supply chain, and AI-driven attacks."
- "single lightweight sensor and unified platform ... protect every major operating system."
- "AI-powered detection triage, investigations and response, reducing manual work and cutting mean time to response."
- Threat hunting and EPP+EDR convergence referenced; Falcon Insight XDR and Next-Gen SIEM as adjacent offerings.
- No operational detail asserted anywhere in this pass. Used only to confirm: (1) the market leader sells EDR as part of an endpoint-security platform; (2) EPP+EDR convergence on one sensor; (3) AI triage as a current differentiator; (4) cloud delivery.

### Wazuh (evidence layer A)

Positioning: self-describes as "Wazuh SIEM and XDR platform" (open source, self-hosted or cloud). Components: Wazuh agent (multi-OS: Windows/macOS/Linux/Solaris/AIX/HP-UX), Wazuh server (manager), Wazuh indexer, Wazuh dashboard. Agent enrollment, agent groups, labels, anti-tampering, remote upgrade (WPK).

Detection machinery:

- Rules engine: decoders + rules (default + custom), rule classification, CDB lists (threat intel lists incl. file hashes), MITRE ATT&CK mapping of rules.
- Malware detection: FIM (file integrity monitoring) events combined with threat detection rules + threat intelligence (VirusTotal integration, YARA scans); Rootcheck module ("detects rootkit behavior ... anomaly monitoring ensures Wazuh detects malware that signature-based techniques might have missed" + known rootkit/trojan signatures); log collection from third-party AV (Windows Defender, ClamAV).
- System inventory (Syscollector), command monitoring, system-call monitoring (audit), container security, vulnerability detection — adjacent capabilities in the same platform.

Active Response:

- "The Wazuh Active Response module executes these scripts on monitored endpoints when an alert of a specific rule ID, level, or rule group triggers."
- Stateless (one-time) vs stateful ("revert or stop their actions after a period of time").
- Out-of-the-box scripts: "block malicious network access and delete malicious files on monitored endpoints"; use cases include disabling a compromised Linux user account.
- Custom scripts supported; caution documented: "Poor implementation of rules and responses might increase the vulnerability of an endpoint."

Observation: Wazuh's response leg is automation-triggered (script on alert), not operator-initiated remote containment; its investigation surface is dashboard query/event search. It fits the minimal core (endpoint instrumentation + behavioral detection + investigation + endpoint-acting response) but realizes the response leg in an automation-first form. This is important calibration for the L0: response must be defined as "actions executed on the endpoint through the instrumentation channel," not "operator clicks isolate."

## Cross-product Comparison

| Aspect | Microsoft Defender for Endpoint | Sophos EDR/XDR | CrowdStrike Falcon (positioning) | Wazuh |
|---|---|---|---|---|
| Instrumentation | sensor on Windows/macOS/Linux/Android/iOS | endpoint agent; XDR Sensor variant (no prevention) | "single lightweight sensor," all major OS (positioning) | agent on Windows/macOS/Linux/Solaris/AIX/HP-UX |
| Telemetry character | behavioral: process, network, kernel/memory optics, logons, registry/file changes; throttled, not full audit logging | device data uploaded to cloud Data Lake; on-device query when online | (not asserted) | logs, FIM events, inventory, audit/syscall, command output |
| Detection output | alerts; aggregated into incidents | detections (unusual/suspicious, NOT blocked) + cases | detections with AI triage (positioning) | alerts from rules |
| Detection basis | behavioral telemetry + threat intel + ML (implied by docs) | threat classification rules over uploaded data | AI + IOCs (positioning) | rules + signatures + anomaly (rootcheck) + TI lists |
| Investigation surfaces | alert story tree, alert timeline, process tree, entity pivot, advanced hunting (KQL) | threat graphs (origin/spread/affected), detection raw data + lineage, Live Discover queries, cases | (positioning) | dashboard event search/queries |
| Response actions | isolate device (full/selective), live response remote shell, investigation package, AV scan, restrict app execution, contain device/user/IP | Live Response (direct device connection), scan device, cleanup via threat graphs | (positioning) | active response scripts (block network access, delete files, disable user) |
| Action tracking | Action center (status, submitting user, success/failure) | case history; actions from detections | (not asserted) | (not asserted) |
| Estate organization | device groups, tags, RBAC roles, high-value assets | computer groups, policies per product, admin roles | (not asserted) | agent groups, centralized config, RBAC |
| Automation | automated investigations; custom detection rules; automatic attack disruption (XDR-level) | auto-created cases; MDR service responds | AI triage (positioning) | active response automation |
| Managed service | Threat Experts consultation | MDR 24/7 team; Rapid Response (paid) | Falcon Complete (positioning) | professional support / community |
| Delivery | cloud portal (part of Defender XDR) | cloud (Sophos Central) | cloud | self-hosted or cloud |
| Prevention bundled | next-gen AV, ASR, ransomware prevention | full Endpoint policy set (threat/web/app/peripheral control) | EPP+EDR one sensor (positioning) | none native (relies on FIM/rules/third-party AV logs) |

Cross-product commonalities (layer B, directly observed in ≥2 products):

1. Endpoint instrumentation via deployed software (all four).
2. Continuous collection of endpoint activity telemetry (all four; character varies).
3. Detection of suspicious/malicious behavior surfaced as analyst-facing alerts/detections (all four).
4. An investigation surface into what happened on the endpoint (Microsoft alert story/timeline/hunting; Sophos threat graphs/lineage/Live Discover; Wazuh dashboard queries; CrowdStrike positioning).
5. Response that acts on the endpoint through the instrumentation channel (Microsoft isolate/live response; Sophos Live Response/scan; Wazuh active response scripts; CrowdStrike "response" positioning).
6. Estate organization by device groups/tags + policy assignment (Microsoft, Sophos, Wazuh).
7. MITRE ATT&CK mapping on detections (Sophos, Wazuh documented; Microsoft shows MITRE technique in event details).
8. Threat-intelligence enrichment of detections (Sophos Intelix/VirusTotal; Wazuh VirusTotal/CDB; Microsoft threat experts/TI).
9. Proactive query surface over collected telemetry (Microsoft advanced hunting; Sophos Live Discover; Wazuh dashboard queries).
10. EPP/prevention bundled in the same product (Microsoft, Sophos, CrowdStrike positioning) — with a documented sensor-only counter-shape (Sophos XDR Sensor) and a prevention-less open-source shape (Wazuh).
11. Automation/managed-service layer (Microsoft automated investigations + Threat Experts; Sophos auto cases + MDR; Wazuh active response; CrowdStrike AI triage positioning).
12. Forwarding/API integration into wider SOC tooling (Microsoft APIs/streaming; Sophos Data Lake integrations; Wazuh indexer/Splunk/Elastic integrations).

## Canonical Abstraction

### L0 — Defining Invariant

Four jointly-held structures. Remove any one and the product stops being recognizable as an EDR:

1. **The instrumented endpoint estate** — a population of the organization's endpoints (user devices, and commonly servers) carrying deployed sensor software that continuously observes activity on them. Remove → network/log tooling with nothing endpoint-native (SIEM/NDR territory).
2. **Behavioral detection over endpoint telemetry** — the collected activity is evaluated (rules, behavioral analytics, threat intel, ML) to surface malicious or suspicious behavior as analyst-facing alerts/detections — explicitly beyond blocking known-bad files. Remove → pure prevention (EPP/AV) or raw log collection.
3. **The investigation surface into endpoint activity** — the analyst can examine what happened on an endpoint around a detection: event timelines, process/lineage relationships, entity pivots, raw telemetry queries. Remove → an alert forwarder.
4. **Response acting on the endpoint through the instrumentation channel** — containment/remediation executed on the endpoint itself (isolate from network, terminate, quarantine, remote shell, scripted response), whether operator-initiated or automation-triggered. Remove → detection-and-alerting only; the "R" is gone.

Jointly-held is load-bearing:

- 1 alone = agent/asset inventory management.
- 2 without 1 = log analytics on whatever data exists.
- 1+2 without 3 = an alert feed with no way to understand an alert.
- 1+2+3 without 4 = detection & investigation without response (an "ED", not EDR).
- 3+4 without 1+2 = generic remote-administration tooling with nothing to investigate.

Historical/market-sample check (§24): the minimal core survives older and differently positioned shapes — pre-cloud on-prem EDR consoles (agent + console + response), and HIDS-lineage open-source platforms (Wazuh/OSSEC lineage: host telemetry + rule alerts + active-response scripts) all satisfy the four structures without cloud, AI, MITRE mapping, or managed services. Classic signature antivirus fails structures 2–4 and is correctly excluded (EPP/AV, not EDR). Network IDS fails 1 and 4. The definition is therefore not over-fitted to the current cloud/AI implementation era.

### L1 — Common Mature Structure

Present in most mature modern products; not required for the Type:

- cloud-hosted operator console as the primary surface (self-hosted console as the counter-shape)
- alert aggregation into higher-level containers (incidents / cases)
- MITRE ATT&CK mapping on detections
- threat-intelligence enrichment (vendor intel + third-party services)
- proactive query/hunting surface over collected telemetry
- estate organization: device groups, tags, policy assignment, RBAC roles
- bundled prevention (EPP convergence) — dominant but not universal (XDR Sensor, Wazuh counter-shapes)
- automated investigation/response and custom detection rules
- managed detection & response (MDR) service tier
- APIs/streaming into SIEM/SOAR and data lakes

### L2 — Variant / Optional Structure

- deployment: cloud SaaS vs self-hosted vs platform-native (embedded in a broader platform portal)
- sensor-only variant without prevention (runs alongside third-party AV)
- object-domain breadth: user endpoints only vs endpoints+servers vs mobile included
- managed-service depth (consultation vs 24/7 full-response MDR)
- AI assistants / AI triage (era-current differentiator)
- data-retention windows and query quotas (product-specific numbers)
- custom detection-rule engines
- cross-domain containment actions (contain user/IP — observed in one product, XDR-level)

### L3 — Vendor-specific Structure (research notes only)

- Microsoft: incident aggregation inside Defender XDR; automatic attack disruption; contain user/contain IP; live response script library; investigation package contents; Plan 1/Plan 2 capability gating; 7-day isolation auto-lift; high-value asset restrictions; six-month telemetry retention; 30-day hunting window; KQL.
- Sophos: Data Lake; Intelix; Security Heartbeat; XDR Sensor; Sophos-managed vs self-managed cases; MDR message tabs; Rapid Response service.
- CrowdStrike: Charlotte AI; Falcon Complete; single-sensor platform framing; Falcon Insight XDR packaging.
- Wazuh: ossec.conf/agent.conf configuration model; WPK remote upgrades; rootcheck; CDB lists; stateless/stateful active response; VirusTotal/YARA integrations.

## Vendor-specific Findings

See L3 above. Additionally:

- The EPP+EDR convergence is the dominant packaging (3 of 4 sampled products bundle prevention), but two documented counter-shapes (Sophos XDR Sensor; Wazuh without native AV) prove prevention is not definitional.
- The response-action vocabulary differs sharply by product (isolate/kill/quarantine/shell vs scripted responses). The invariant is "actions executed on the endpoint," not any specific action list.
- Alert-aggregation containers differ (incident vs case vs none); aggregation is common-mature, not definitional.

## Boundary Findings

| Neighbor Type | Relationship | Distinction test ("remove what → becomes the other Type") |
|---|---|---|
| Endpoint Protection Platform / EPP (§15 sibling, unprocessed) | closest sibling; same device population, usually same agent | EPP centers on preventing execution (blocking known/unwanted software); EDR centers on detecting what got through, investigating it, and responding. Remove investigation depth + retrospective telemetry + endpoint response → EPP. Remove prevention → pure EDR. Convergence is the market norm; the leaf boundary is the center of gravity, and both pure poles historically existed (standalone EDR without prevention; classic AV without EDR). Flag for joint review when EPP is processed. |
| Extended Detection & Response / XDR (§15 sibling, unprocessed) | umbrella over EDR | XDR correlates endpoint signals with other domains (identity, email, cloud, network) into unified incidents. Microsoft: Defender for Endpoint "feeds endpoint signals into the unified Defender portal" which correlates identity/email/cloud alerts. Sophos: XDR = EDR + third-party data integrations. Remove non-endpoint sources → EDR. Flag for joint review with XDR leaf. |
| SIEM (§15 sibling, unprocessed) | adjacent; data-plane overlap | SIEM aggregates organization-wide logs with correlation/compliance machinery; EDR's data is endpoint-telemetry-native and its response acts on endpoints. Wazuh straddles (self-describes SIEM/XDR) — its endpoint machinery is EDR-shaped, its aggregation machinery is SIEM-shaped. Remove endpoint agent instrumentation + endpoint response → SIEM. |
| Cloud Workload Protection / CWPP (§15, processed) | sibling; machinery convergence real | Boundary rests on object domain + operational workflow: user endpoint estate vs server/container/cloud-workload estate with image/vulnerability corpus. Do not absorb CWPP on agent-technology grounds (per CWPP pass flag). Servers commonly appear inside EDR estates; the CWPP Type is defined by the workload operational context, not by "has an agent." |
| Network Detection & Response / NDR (§15 sibling, unprocessed) | structural sibling on another path | NDR instruments the network path; EDR instruments the host. Remove endpoint instrumentation → NDR-shaped. |
| Threat Hunting Platform (§15 sibling, unprocessed) | capability vs Type | Hunting is a standard EDR capability (advanced hunting, Live Discover) over the EDR's own telemetry. A dedicated hunting platform centers the hunt workflow across sources. EDR keeps hunting as a surface, not the center of gravity. |
| Digital Forensics Platform (§15, processed) | adjacent; opposite evidence posture | Forensics examines preserved, verified copies offline with defensibility machinery; EDR investigates live telemetry in production. Per DF pass: "live-system analysis/EDR territory." |
| Cyber Incident Response Platform (§15, processed) | downstream | IR platforms manage incidents as cases with response lifecycle; detection is the SIEM/EDR's job. EDR case-like containers (Sophos cases) are detection-triage-shaped, not response-program-shaped. |
| Mobile Threat Defense (§15 sibling, unprocessed) | object-domain slice | Mobile is part of the endpoint estate in sampled products (Microsoft Android/iOS; Sophos Mobile product). MTD as a separate leaf covers the mobile-specialized pole; not absorbed here. |
| Endpoint Management / UEM (§14, processed sibling family) | different job on the same devices | UEM configures/complies/manages devices; EDR detects/responds to threats. Both may share agents. Remove threat detection/response → UEM. |
| Browser Security Platform (§15, processed) | adjacent | Browser security binds enforcement to the browsing session; per that pass, "remove session binding → EDR." |

## Uncertainties

1. CrowdStrike operational detail (detection model, response actions, console surfaces) unverified — docs JS-only. All CrowdStrike statements remain positioning-level. The market leader's operational shape is asserted only via cross-product commonality, not direct evidence.
2. SentinelOne, Elastic Defend, Cortex XDR not sampled (access failures). The AI-autonomous pole and the observability-heritage pole are documented structurally, not observationally.
3. Whether "servers" belong inside the EDR object domain by default or as a variant: sampled products differ (Microsoft supports Windows Server; Sophos splits Server into a separate product; Wazuh is server-heavy). Held as an object-domain breadth variant (L2), consistent with the CWPP boundary flag.
4. Detection-engine internals (ML models, behavioral analytics specifics) are not documented at operational depth by any sampled vendor; the research notes describe detection inputs and outputs, not engine internals.
5. Exact retention windows, quotas, and action-availability matrices are product- and plan-specific; none are generalized into the final document.

## Final Synthesis

An EDR is the security-operations application that turns an organization's endpoints from a blind spot into an observed, queryable, and controllable surface. Its world is built from four jointly-held structures: an instrumented endpoint estate (sensors deployed across the organization's devices, organized into groups/tags and governed by policy and roles); behavioral detection that continuously evaluates the collected endpoint telemetry and surfaces malicious or suspicious activity as analyst-facing alerts/detections (distinct from the prevention stack's blocking of known-bad files); an investigation surface where the analyst reconstructs what happened on an endpoint — alert stories, timelines, process lineage, entity pivots, raw telemetry queries; and response that acts on the endpoint itself through the same instrumentation channel — isolating it from the network while keeping the sensor alive, opening remote shells, collecting forensic packages, killing processes, quarantining files, or executing scripted containment — whether the analyst clicks the action or automation triggers it. Around this core, mature products add alert aggregation (incidents/cases), MITRE ATT&CK mapping, threat-intel enrichment, proactive hunting, bundled prevention, automated investigation, managed-service tiers, and SOC integrations. The Type's boundaries are held by object domain and workflow, not by agent technology: EPP is the prevention-first sibling on the same devices, XDR the cross-domain umbrella above it, SIEM the organization-wide log plane beside it, CWPP the server-workload estate, NDR the network path, forensics the offline preserved-copy world, and the incident-response platform the downstream case layer.
