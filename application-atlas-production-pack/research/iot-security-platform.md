# Research Notes — IoT Security Platform

Research date: 2026-09-08
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what an IoT Security Platform actually is as an Application Type: what objects exist inside it, who operates it, how security work flows through it, and where its boundaries sit against neighboring security Types (EDR, NDR, OT Security, Cyber Asset Management, UEM, Vulnerability Management, NAC).

## Initial Boundary

Initial hypothesis (pre-research):

- Core use: secure the organization's population of network-connected devices that traditional endpoint security cannot cover — printers, cameras, sensors, medical devices, building systems, industrial equipment.
- Users: security teams (SOC analysts, security architects), network/IT operations, plus device-owning stakeholders (biomedical/clinical engineering in hospitals, plant engineers in industry).
- Nearest neighbors: EDR (agent-based endpoints), NDR (network traffic detection), OT Security Platform (industrial control), Cyber Asset Management (inventory), UEM (device administration), Vulnerability Management (scan-centric), NAC (access enforcement).
- Main unknowns: Is enforcement (segmentation/NAC) definitional or optional? Is the IoT/OT split real at the product level or one platform family? Is "agentless" definitional or a common implementation?

## Research Questions

1. What is the central object — the device record? What identity anchors it?
2. How do devices enter the system (discovery methods) if no agent is installed?
3. What security assessment attaches to each device (classification, vulnerabilities, risk)?
4. What does continuous monitoring actually watch, and what does it produce (alerts, anomalies, policy violations)?
5. Is policy enforcement (segmentation, access control) part of the core or an extension?
6. How does the platform integrate with the SOC stack (SIEM/SOAR/XDR) and with device-owning operations (CMMS, biomedical, plant)?
7. Where is the boundary vs EDR (managed endpoints), vs NDR (traffic-centric), vs Cyber Asset Management (inventory-centric), vs OT Security (industrial)?
8. What deployment shapes exist (cloud vs on-prem vs air-gapped; sensors vs agents)?
9. Historical check: would older/regional/earlier-generation products still fit the definition?

## Representative Products

Selected for market representation, different philosophies, different heritages, different customer tiers:

| Product | Heritage / philosophy | Customer tier | Evidence reached |
|---|---|---|---|
| Microsoft Defender for IoT | Platform-embedded (Azure/Defender ecosystem); OT sensors + enterprise IoT via Defender for Endpoint | Enterprise, Microsoft estates | Tier 1 (Microsoft Learn docs) |
| Forescout (Vistaro / eyeSight) | NAC heritage (2000s); enforcement-oriented zero-trust platform | Large enterprise, public sector | Tier 2 (official solution/platform pages) |
| Claroty (xDome / CTD) | CPS protection pure-play; vertical packaging (industrial / healthcare / commercial / public sector); SaaS + on-prem pair | Enterprise, healthcare-heavy | Tier 2 (official platform pages) |
| Nozomi Networks (Vantage / Guardian / Arc) | OT-monitoring heritage; sensor family + cloud/on-prem managers | Critical infrastructure, industrial | Tier 2 (official platform/solution pages) |
| Armis | Agentless device security pure-play | Enterprise | NOT reachable (403 direct; Wayback transport error ×2) — positioning corroborated only indirectly (see Sources) |

## Sources

Reached directly (2026-09-08):

- Microsoft Learn — Defender for IoT overview (organizations): https://learn.microsoft.com/en-us/azure/defender-for-iot/overview (fetched via /en-us/azure/defender-for-iot/organizations/overview) — Tier 1
- Microsoft Learn — Secure IoT devices (enterprise IoT): https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/concept-enterprise — Tier 1
- Microsoft Learn — Defender for IoT OT architecture and components: https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/architecture — Tier 1
- Forescout — IoT Security solution page: https://www.forescout.com/solutions/iot-security/ — Tier 2
- Forescout — corporate/platform page (Vistaro, product family, deployment options): https://www.forescout.com/ — Tier 2
- Claroty — Platform page (modules, discovery methods, CPS/XIoT scope): https://claroty.com/platform — Tier 2
- Claroty — corporate page (verticals, integrations catalog): https://claroty.com/ — Tier 2
- Nozomi Networks — IoT Security solution page: https://www.nozominetworks.com/solutions/iot-security — Tier 2
- Nozomi Networks — corporate/platform page (sensor family, managers, solutions): https://www.nozominetworks.com/ — Tier 2

Not reached:

- Armis — https://www.armis.com/platform/ returned 403; docs.armis.com requires login; Wayback Machine attempts returned transport errors (×2). Per source-access rules, no Armis-specific operational claims are made anywhere in this research. Armis's existence as a leading device-security platform is corroborated only indirectly: the Gartner MQ for CPS Protection Platforms graphic reproduced on Nozomi's own site lists Armis among the Leaders (alongside Claroty and Nozomi), with Forescout and Microsoft as Challenger/Niche.
- Forescout technical documentation (docs.forescout.com) returned empty content; Nozomi docs (docs.nozominetworks.com) transport error. Product-page depth only for these two vendors.
- Claroty xDome dedicated page (/xdome) 404'd; platform-level pages used instead.

Analyst-category context (Tier 2, reproduced on vendor pages): Gartner Magic Quadrant for CPS Protection Platforms (March 2026); Forrester Wave: OT Security Solutions Q3 2026; Forrester Wave: IoT Security Solutions Q3 2025 (Nozomi named Leader). These confirm the market treats "IoT security platforms" inside the broader CPS/device-security platform category.

## Product Observations

### Microsoft Defender for IoT (Tier 1 — strongest operational evidence)

Key observations (evidence layer A):

- Self-description: "a unified security solution built specifically to identify IoT and OT devices, vulnerabilities, and threats… including existing devices that might not have built-in security agents." Agentless, network-layer monitoring.
- Discovery: "Discover IoT/OT devices in your network, their details, and how they communicate. Gather data from network sensors, Microsoft Defender for Endpoint, and third-party sources."
- Assessment: "Assess risks and manage vulnerabilities using machine learning, threat intelligence, and behavioral analytics" — identifies unpatched devices, open ports, unauthorized applications, unauthorized connections, changes to device configurations, PLC code, firmware.
- Monitoring/detection: historical traffic search across dimensions/protocols; full-fidelity PCAP drill-down; detection of threats static IOCs miss (zero-day malware, fileless malware, living-off-the-land tactics).
- Response: integration with Microsoft Sentinel, SIEM/SOAR/XDR services, partner systems, APIs.
- Architecture: OT network sensors deployed on VM or physical appliance, connected to SPAN port or network TAP; "visibility into risks within minutes of connecting"; Layer-6/7 deep packet inspection; data collection/analysis/alerting on the sensor itself (low-bandwidth sites); only telemetry/insights forwarded to the Azure portal.
- Cloud-connected vs locally-managed sensors; air-gapped and hybrid configurations supported.
- Five named analytics engines: protocol violation detection (e.g., illegal MODBUS function code), policy violation (baseline deviation, e.g., unauthorized HTTP user agent), industrial malware detection (Conficker/BlackEnergy/Havex/WannaCry/NotPetya/Triton/Stuxnet signatures), anomaly detection (unusual M2M communications; ICS-modeled baselines per NISTIR 8219 behavioral anomaly detection), operational incident detection (e.g., unresponsive device, Siemens S7 stop command).
- Device inventory: devices listed "based on a unique IP and MAC address coupling"; infrastructure devices (switches/routers) counted; endpoints already managed by Defender for Endpoint NOT counted as separate devices; inactive devices (no network activity >60 days in OT networks) not counted against license.
- Enterprise IoT: extends agentless security beyond OT to corporate IoT — "printers, smart TVs, and conferencing systems and purpose-built, proprietary devices"; discovery via Defender for Endpoint passive AND active methods; per-device standalone licenses or E5 entitlements; IoT-specific security recommendations (require auth for Telnet/VNC management interfaces, disable Telnet, remove SNMPv1/v2).
- Vendor's own OT vs Enterprise IoT FAQ: OT = sensors for deep OT/ICS visibility, on-site collection/analysis/alerting; Enterprise IoT = visibility and security for corporate IoT devices (printers, cameras, purpose-built devices).

### Forescout (Tier 2 — solution/platform pages)

Key observations (evidence layer A, product-page depth):

- Platform framing: "Secure Every Connected Asset Across IT, OT, IoT, and IoMT"; "Agentless, vendor-agnostic"; "Managed & Unmanaged Cyber Assets".
- IoT Security solution: "actionable visibility and automated risk-based segmentation and compliance of every IoT, OT, and IoMT the instant they connect to your network, without ever requiring an agent. From connection to a device's end of life, the platform efficiently manages asset inventory and lifecycle management of every device."
- Named capabilities: complete device visibility and classification (unmanaged AND managed IoT/IoMT/OT); real-time continuous monitoring of IoT device communications and risky behaviors; assessing devices with factory-default or weak credentials and automating policy actions to enforce strong passwords; dynamic network segmentation into trusted zones by least-privilege zero-trust policy; automated zero-trust policy orchestration across multi-vendor environments and network domains; asset inventory and lifecycle management.
- Classification: automated three-dimensional taxonomy — device function & type, operating system & version, vendor & model; segmentation automated from that classification.
- Enforcement heritage: NAC ("Dynamically and continuously control what connects to your network"), network segmentation ("Automate and enforce segmentation to reduce the blast radius"), security automation across "180+ integrated tools".
- Deployment: on-premises, VM, Docker, air-gapped, appliances, hybrid, cloud; sensors as standalone appliances, installed directly on routers/switches, or configured as active sensors querying network infrastructure. eyeSight described as discovering/assessing/governing assets "without agents or active techniques that could compromise business operations."
- Scale claims (marketing, research-notes only): deployments of over 2 million devices; over a thousand locations.

### Claroty (Tier 2 — platform pages)

Key observations (evidence layer A, product-page depth):

- Category framing: "Cyber-Physical Systems (CPS) Protection Platform"; scope diagram enumerates three device worlds: OT (PLC, SCADA, DCS, HMI, RTU, IIoT gateway, sensors, embedded devices, elevators, BMS/BAS, smart grid, HVAC), Enterprise IoT (physical intrusion, video, card access, lighting & energy), IoMT (CT scanner, anesthesia machine, blood gas analyzer, hematology analyzer). Uses "XIoT" (extended IoT) terminology.
- Platform modules: Asset Inventory; Exposure Management ("automatically scopes all CPS assets… identify and prioritize vulnerabilities and other exposures… highlighting specific attack vectors and providing actionable recommendations"); Network Protection ("leverages the visibility… to automatically define and recommend network policies… monitor, refine, and automatically enforce these policies with your existing firewalls, switches, or NAC solutions… segmentation… Zero Trust"); Secure Access (controlled third-party remote access to CPS); Threat Detection ("continuously monitors… earliest indicators of both known and emerging threats. All alerts are contextualized… integrates with SIEM, SOAR, EDR").
- Discovery methods (named): Claroty Edge, Passive Monitoring, Safe Queries, Project File Analysis, Ecosystem Enrichment.
- Deployment pair: xDome (modular SaaS) vs Continuous Threat Detection/CTD (on-premise); "deployed on-premise or in the cloud."
- Integration catalog (evidence of the ecosystem posture): NAC (Forescout, Aruba ClearPass — Claroty passes device profiles/group baselines to the NAC for enforcement), CMMS/CMDB (Nuvolo, Accruent, TRIMEDX — device profiles incl. serial numbers, location, utilization), SIEM (Splunk), firewalls (Palo Alto Panorama, Check Point), vulnerability management (Qualys, Tenable, Rapid7 — bidirectional: scan results ingested back), DHCP (BlueCat, Infoblox — IP assignment enrichment), MDM (Intune, MobileIron), EDR (SentinelOne, Microsoft Defender ATP).
- Vertical packaging: Industrial, Healthcare (IoMT), Commercial (data centers, retail, buildings, hospitality), Public Sector.

### Nozomi Networks (Tier 2 — solution/platform pages)

Key observations (evidence layer A, product-page depth):

- Problem framing (IoT Security solution page): IoT devices "are typically unmanaged, connected across business applications and networks and have minimal built-in security controls for their lightweight operating systems… inherently difficult to segment to prevent the spread of malware."
- Solution pillars: "Identify all your connected devices, including both OT & IoT devices"; "Continuously monitor your IoT devices to detect changes that could increase cyber or operational risk"; "Pinpoint the cyber risks that matter most"; "Scale IoT asset management across your entire infrastructure."
- Collection posture: "options for passive, agentless and active data collection methods."
- Platform structure: managers — Vantage (cloud SaaS) and Central Management Console (on-prem); sensors — Guardian (network), Guardian Air (wireless), Arc (endpoint), Arc Embedded; enhancements — Asset Intelligence, Threat Intelligence, Smart Polling, TI Expansion Pack (powered by Mandiant), integrations.
- Solution set: Asset Inventory Management, Threat Detection & Response, Continuous Network Monitoring, Vulnerability Management, Risk Management, IoT Security, Data Center Cybersecurity, Building Automation System Cybersecurity.
- Dual alert semantics: security threats AND process/operational anomalies ("Detect the security threats and process anomalies that matter").
- Industry packaging: electric utilities, manufacturing, healthcare, smart cities, water, airports, maritime, rail, mining, oil & gas, pharma, retail.
- Marketing numbers (research-notes only): "102M+ OT, IoT and IT Devices Monitored", "11K+ Installations".

### Armis (NOT directly observed — limitation)

No operational claims. Indirect corroboration only: listed as a Leader in the Gartner MQ for CPS Protection Platforms graphic reproduced on Nozomi's site. Known in the market as an agentless device-security platform, but per evidence rules nothing product-specific is asserted here.

## Cross-product Comparison

| Dimension | Microsoft Defender for IoT | Forescout | Claroty | Nozomi Networks |
|---|---|---|---|---|
| Device population of record | Yes — device inventory keyed by IP+MAC coupling; managed endpoints excluded | Yes — every connected asset, managed & unmanaged | Yes — CPS/XIoT asset inventory across OT/IoT/IoMT | Yes — OT/IoT/IT device inventory |
| Self-assembled discovery (no device software required) | Yes — network sensors (SPAN/TAP) + Defender for Endpoint + third-party sources | Yes — "without ever requiring an agent"; passive + active sensors | Yes — Passive Monitoring, Edge, Safe Queries, Project File Analysis, Ecosystem Enrichment | Yes — passive, agentless, active collection |
| Per-device classification | Yes — device details, protocols, behaviors | Yes — 3-dimension taxonomy (function/type, OS/version, vendor/model) | Yes — fully-attributed device profiles (vendor, model, OS, firmware, serial, location) | Yes — asset intelligence with normal-behavior context |
| Per-device vulnerability/exposure assessment | Yes — unpatched devices, open ports, unauthorized apps/connections, config changes | Yes — weak/default credentials assessment; risk-based | Yes — Exposure Management module, prioritized vulnerabilities/attack vectors | Yes — Vulnerability Management solution, prioritized remediations |
| Continuous behavioral monitoring & alerting | Yes — 5 analytics engines, baseline learning (NISTIR 8219 BAD), PCAP drill-down | Yes — real-time continuous monitoring of communications & risky behaviors | Yes — Threat Detection module, contextualized alerts | Yes — continuous monitoring, threat + anomaly detection |
| Operational (non-security) signal | Yes — operational incident detection engine | Implicit (compliance) | Yes — operational efficiency module; business context | Yes — explicit "cyber or operational risk" |
| Policy/segmentation recommendation | Via recommendations + Sentinel/SOAR integration | Yes — native enforcement (NAC, segmentation, policy orchestration) | Yes — recommend + enforce via existing firewalls/switches/NAC | Recommendation-oriented (guided remediations); enforcement via integrations |
| Native enforcement execution | No (integrates out) | Yes (NAC heritage) | Via existing network controls, not own inline | No (integrates out) |
| Central management layer | Azure portal (cloud) + sensor consoles; air-gapped option | eyeFocus cloud console; on-prem options | xDome SaaS vs CTD on-prem | Vantage cloud vs CMC on-prem |
| SOC integration | Sentinel, SIEM/SOAR/XDR, APIs | 180+ integrated tools (security automation) | SIEM/SOAR/EDR/ticketing/CMMS | SIEM/SOAR, TI packs (Mandiant) |
| Vertical packaging | OT + Enterprise IoT split | IT/OT/IoT/IoMT + industries | Industrial/Healthcare/Commercial/Public Sector | Utilities/manufacturing/healthcare/smart cities/etc. |
| Wireless-specific collection | Not observed on fetched pages | Not observed on fetched pages | Not observed on fetched pages | Yes — Guardian Air wireless sensor |
| Endpoint sensor for select devices | Via Defender for Endpoint (separate product) | Not observed | Not observed | Yes — Arc / Arc Embedded endpoint sensors |
| Remote-access management | Not observed | Yes — Secure Remote Access solution | Yes — Secure Access module | Not observed on fetched pages |

## Abstraction Hierarchy

### L0 — Defining Invariant (minimal)

Three structures held jointly, plus the domain binding:

1. **The connected-device population of record** — a standing inventory of the organization's network-connected devices, each an individually identified record (identity anchored in network identifiers — e.g., IP/MAC coupling — enriched with vendor/model/type/OS classification), assembled and kept current BY THE SYSTEM through network-side observation and ecosystem integrations, not by installing software on the devices. The population exists because it is observed, not because it was enrolled. Remove → generic security monitoring with no device subject.
2. **Per-device security assessment** — each device record carries security posture: classification, known vulnerabilities/exposures matched to the device, configuration/credential weaknesses, and a risk standing that makes the risky subset prioritizable. Remove → plain device inventory (cyber-asset-management territory).
3. **Continuous device-behavior monitoring with security alerting** — the system watches device communications and activity over time, learns expected behavior, and raises security alerts on deviations, threats, and policy violations targeting the device population. Remove → static assessment/exposure tool (vulnerability-management territory).

Domain binding: the subject population is the organization's connected-device estate — devices that conventional endpoint security does not instrument (printers, cameras, sensors, medical devices, building systems; extending, in the same platforms, to industrial OT devices). Remove the binding → generic network detection/response.

Jointly-held is load-bearing:
- 1 alone = cyber-asset-management / network inventory
- 2 without 1+3 = exposure scanner with no device population
- 3 without 1+2 = traffic-centric anomaly detection (NDR territory)
- 1+2 without 3 = device inventory with exposure data, no security operations
- 1+3 without 2 = monitoring with no device-level security context

### L1 — Common Mature Structure

- Multi-method discovery: passive network sensors (SPAN/TAP), safe/limited active queries, ecosystem enrichment from existing tools (EDR, MDM, DHCP, NAC, CMMS/CMDB, project files)
- Distributed collection + central management (cloud console and/or on-prem manager aggregating sensors) — the "platform" shape; air-gapped variants
- Baseline learning period before anomaly detection matures
- Vulnerability/exposure management with risk prioritization and recommendations
- Communication topology / network map visualization
- Device-detail drill-down (attributes, history, traffic, PCAPs in some)
- SOC integration (SIEM/SOAR/XDR/ticketing) and threat-intelligence feeds
- Compliance/regulatory reporting (NERC CIP, ISA/IEC 62443, NIS2, etc. — named by Nozomi/Claroty/Forescout pages)
- Dual security + operational alert semantics
- Per-device or per-sensor commercial models

### L2 — Variant / Optional

- Enforcement execution: native inline enforcement (Forescout NAC/segmentation) vs recommend-and-orchestrate via existing firewalls/switches/NAC (Claroty) vs integrate-out only (Microsoft, Nozomi)
- Vertical packaging: healthcare/IoMT, industrial/OT, commercial buildings, data centers, smart cities
- Remote-access management for third parties (Claroty Secure Access, Forescout SRA)
- Wireless-specific sensors (Nozomi Guardian Air)
- Endpoint sensors for select device classes (Nozomi Arc)
- Agent-based collection as an extension where devices can carry one (Defender for Endpoint coupling)
- Managed-service delivery by partners/MSSPs
- Air-gapped deployment for high-security environments

### L3 — Vendor-specific (research notes only)

- Microsoft: Azure portal as management plane; Sentinel integration; E5/per-device licensing; five named analytics engines; 60-day OT inactivity rule; "Enterprise IoT" toggle in Defender portal; named recommendation set (Telnet/VNC/SNMP).
- Claroty: xDome vs CTD packaging; Claire AI agent; Team82 research unit; "XIoT"/CPS vocabulary; Edge/Safe Queries/Project File Analysis discovery methods; 60+ attribute Accruent integration.
- Forescout: Vistaro platform naming; eyeSight/eyeSegment/eyeFocus/eyeInspect/eyeExtend product family; 3-dimensional classification taxonomy; 2M+ device / 1000+ location scale claims; VistaroAI agentic AI.
- Nozomi: Vantage vs CMC; Guardian/Guardian Air/Arc/Arc Embedded sensor family; Vantage IQ; Mandiant-powered TI pack; Smart Polling; 102M devices / 11K installations claims.
- Category naming: Gartner "CPS Protection Platforms" MQ (2026) — Leaders Nozomi/Claroty/Armis, Challengers Forescout/Tenable/Fortinet, Visionaries Darktrace, Niche Microsoft/Cisco/Palo Alto/Honeywell/TXOne/Dragos; Forrester "OT Security Solutions" (Q3 2026) and "IoT Security Solutions" (Q3 2025) Waves.

## Historical / Market-Sample Check (conceptual)

No historical product was directly fetched this pass; the check is conceptual, per evidence rules:

- The definition is abstracted above current packaging: passive network sensors, protocol-aware DPI, cloud consoles, AI prioritization, enforcement machinery are all held as implementations, not invariants. A pre-cloud, pre-AI passive-sensor device monitor (device inventory + per-device assessment + behavioral alerting) satisfies all three L0 legs.
- The Type has two observable heritages in the sample: (a) the OT/ICS network-monitoring heritage (passive protocol-aware sensors — Microsoft/Nozomi/Claroty all ship this shape), and (b) the NAC/device-access-control heritage (Forescout: discovery + policy enforcement). Today's NAC-heritage products carry all three L0 legs; a pure legacy NAC appliance (discovery + enforcement without continuous behavioral detection) fails leg 3 and is correctly the ancestor, not the Type.
- The definition does not depend on any specific device class, protocol set, vertical, or deployment model — a hospital-IoMT-focused or smart-city-focused product satisfies the core.
- Consumer/home IoT security (router-gateway products protecting a household's devices) is a different population and commercial model; treated as out of scope for this enterprise leaf.

## Vendor-specific Findings

See L3 above. Notable for boundary work: Microsoft's own docs explicitly exclude Defender-for-Endpoint-managed endpoints from the IoT device population, and explicitly split "OT" (sensor-based ICS monitoring) from "Enterprise IoT" (corporate device security) — vendor-acknowledged seams used below.

## Boundary Findings

- **vs OT Security Platform (sibling leaf, unprocessed)**: every sampled product covers OT AND IoT in one platform; the market category (CPS Protection Platforms) spans both. The leaves differ by population emphasis, not by structure: OT security centers industrial control environments (PLC/SCADA/DCS/process networks, safety/downtime semantics); IoT security centers the enterprise/facility connected-device estate. One platform family, two population lenses. Joint review recommended when ot-security-platform is processed.
- **vs EDR (processed 2026-09-08)**: EDR's defining core is the instrumented endpoint estate — sensors deployed ON the org's devices, telemetry from the sensor. Here the security relationship is established from the network/ecosystem side against devices that cannot or should not carry agents. Microsoft's own docs operationalize the seam: endpoints managed by Defender for Endpoint are not counted as IoT devices; enterprise IoT extends via the EDR's discovery. Seam = where the security signal originates and whether the device is managed/instrumented.
- **vs NDR (unprocessed)**: both may use passive network sensors and behavioral detection. NDR's subject is network traffic/flows across the IT network; this Type's subject is the device population — each alert binds to an identified device record with classification, vulnerability, and risk context. Remove the device population of record → NDR territory.
- **vs Cyber Asset Management (processed 2026-09-07)**: CAM's core is the standing multi-class asset population (devices + cloud + identities + software + services) kept current, with identity resolution — inventory/identity-centric. This Type holds the device population as the substrate for security operations (assessment + continuous detection). CAM without per-device behavioral threat detection remains CAM; this Type without the multi-class scope remains device security.
- **vs UEM (processed 2026-09-08)**: UEM establishes a management relationship by enrollment (management credentials, config profiles, app delivery). This Type observes devices it cannot manage. The same physical device can appear in both (a managed tablet in UEM; an unmanaged camera here).
- **vs Vulnerability Management (unprocessed)**: VM scan-centric assessment of IT software assets; here vulnerability assessment is one leg of a device-security loop that also includes discovery and continuous behavioral detection, executed without credentialed scans against unmanageable devices.
- **vs Network Access Control**: NAC is enforcement machinery (admit/deny/quarantine at connection). In this Type, enforcement is a variant posture (native in the NAC-heritage pole, orchestrated via integrations elsewhere). NAC without the assessment+detection legs is below this Type.
- **vs Industrial IoT Platform (§16, unprocessed)**: IIoT platforms connect and operationalize industrial devices (telemetry, monitoring, control enablement) — not a security system of record. Different primary job despite overlapping device populations.

## Uncertainties

- Armis unreachable — its positioning (agentless device security, behavioral profiling) could not be verified from official sources this pass; excluded from all claims.
- Help-center/user-guide depth for Forescout and Nozomi not reached (docs sites empty/transport error); their observations are product-page depth (Tier 2). Workflow details (exact alert triage steps, exact policy editors) not asserted.
- Whether any sampled product offers native inline enforcement beyond the NAC-heritage pole (Forescout) — Claroty enforces "with your existing firewalls, switches, or NAC solutions" (orchestration, not inline); Microsoft and Nozomi integrate out. Native-enforcement breadth unverified.
- Precise licensing mechanics (per-device vs per-sensor vs tiers) only partially documented (Microsoft per-device for enterprise IoT is Tier 1; others unverified).
- Historical products not directly sourced; historical check kept conceptual.

## Final Synthesis

An IoT Security Platform is the security team's system of record for the organization's connected-device estate — the population of network-attached devices that conventional endpoint security does not instrument. Its defining core is three jointly-held structures: (1) a self-maintained device population of record, assembled by the system from network-side observation and ecosystem integrations rather than by device enrollment; (2) per-device security assessment — classification, matched vulnerabilities/exposures, credential/configuration weaknesses, risk standing; (3) continuous monitoring of device behavior producing security alerts (threats, anomalies, policy violations), with operational-risk signals commonly alongside. Everything else — distributed sensor fleets, cloud/on-prem managers, enforcement (native or orchestrated), vertical packaging, remote-access control, wireless sensors, AI prioritization — is mature structure or variant, not definition. The market realizes one platform family serving IoT+OT+IoMT populations, with "IoT Security Platform" naming the device-estate-centered lens; the sibling OT Security Platform leaf is the industrial-control lens on the same family (joint review recommended).
