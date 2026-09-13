# Research Notes — OT Security Platform

Research date: 2026-09-09
Slug: ot-security-platform
Directory leaf: OT Security Platform (§15 Cybersecurity, Identity & Trust)
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1

---

## Research Goal

Understand what an OT Security Platform actually is as an Application Type: what its system of record is, what its users do with it, how the security loop runs, and where its boundary lies against neighboring Types (IoT Security Platform, NDR, Network Monitoring, Vulnerability Management, Cyber Asset Management, SIEM, inline Network Security Platform, and the §16 industrial control systems it protects).

## Initial Boundary (hypothesis before research)

- Core use: security visibility, detection, and risk management for industrial control environments (SCADA/DCS/PLC networks) that cannot be protected with endpoint tooling.
- Primary users: OT/security teams in critical infrastructure and manufacturing; control engineers as validators.
- Nearest neighbors: IoT Security Platform (sibling leaf, already documented), NDR, Network Monitoring, Vulnerability Management, Cyber Asset Management.
- Likely confusion: "OT security" is often marketed as one family with IoT security; the leaf split must be honored by finding the OT-specific center of gravity, not by duplicating the IoT doc's core model.
- Unknowns: whether vulnerability management is definitional or common; whether enforcement (blocking) is part of the Type; how the zone/site/Purdue structure sits in the abstraction; historical fit of pre-platform SCADA IDS tools.

## Research Questions

1. What is the platform's unit of record — devices? assets? the process network?
2. How is the estate discovered, given that controllers cannot be instrumented?
3. What does detection look like when the protected thing is a control process (protocol semantics, control-law changes, PLC states)?
4. What lifecycle do alerts/findings have, and how does triage work when "response" cannot touch the process?
5. How are vulnerability/exposure and risk handled when patching is frequently impossible?
6. Where do zones/sites/Purdue levels sit — definitional or common structure?
7. Where is enforcement in this Type — none, recommend-only, or native?
8. What distinguishes OT security from IoT security in product structure, not marketing?
9. Would older / regional / pre-cloud products still fit the proposed definition?

## Representative Products

Selected for market representation, documentation quality, differing product philosophy, and differing customer tiers:

| Product | Philosophy / heritage | Customer tier | Evidence depth |
|---|---|---|---|
| Microsoft Defender for IoT | cloud-native, Microsoft security ecosystem integration | broad enterprise + critical infrastructure | Tier 1 — full official docs (architecture, device inventory, alerts) |
| Nozomi Networks | network-monitoring-first, cloud + on-prem managers, sensor family | utilities/energy/manufacturing, large distributed estates | Tier 2 — official platform page |
| Dragos | OT-native threat-intelligence-led, expert services wrapped around platform | heavy industry / critical infrastructure | Tier 2 — official platform page |
| Claroty | asset/exposure-centric, multi-vertical CPS platform (industrial + healthcare + commercial) | enterprise + industrial + healthcare | Tier 2 — official platform + asset-inventory pages |
| Forescout (eyeSight) | NAC-heritage, agentless network-side visibility with enforcement lineage | enterprise network/security teams | Tier 2 — official product page |

Historical probe: Digital Bond Quickdraw (SCADA-protocol IDS generation) — **source unreachable** (transport errors on two attempts, 2026-09-09); historical check done conceptually with reduced confidence (see §24 check below).

## Sources

Tier 1 (full operational documentation):

- Microsoft Learn — Defender for IoT documentation hub: https://learn.microsoft.com/en-us/azure/defender-for-iot/ (fetched 2026-09-09)
- Microsoft Learn — OT architecture and components: https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/architecture (fetched 2026-09-09)
- Microsoft Learn — Device inventory: https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/device-inventory (fetched 2026-09-09)
- Microsoft Learn — Alerts: https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/alerts (fetched 2026-09-09)

Tier 2 (official product pages):

- Nozomi Networks — Platform: https://www.nozominetworks.com/platform (fetched 2026-09-09)
- Dragos — The Cybersecurity Platform: https://www.dragos.com/cybersecurity-platform/ (fetched 2026-09-09)
- Claroty — Platform: https://claroty.com/platform (fetched 2026-09-09)
- Claroty — Asset Inventory: https://claroty.com/platform/asset-inventory (fetched 2026-09-09)
- Forescout — eyeSight: https://www.forescout.com/platform/eyesight/ (fetched 2026-09-09)

Unreachable / degraded:

- docs.forescout.com — returned empty content (1 attempt); Forescout held at product-page depth.
- digitalbond.com (Quickdraw historical probe) — transport errors (2 attempts); abandoned per network-restricted rule.

Sibling documents consulted for boundary alignment:

- applications/iot-security-platform.md + research/iot-security-platform.md (processed 2026-09-08; explicitly records OT Security Platform as sibling, "recorded for joint review")
- STATUS.md entry for network-detection-response-ndr (processed 2026-09-08)

---

## Product Observations

### Microsoft Defender for IoT (Evidence layer: A — directly observed, full docs)

**Architecture / components**
- OT network sensors deployed on physical appliance or VM, connected to a SPAN port or network TAP; "purpose-built for OT/IoT networks"; visibility "within minutes of connecting".
- Sensors use "OT/IoT-aware analytics engines and Layer-6 Deep Packet Inspection (DPI)".
- Data collection, processing, analysis, and alerting happen on the sensor itself (for low-bandwidth/high-latency sites); only telemetry/insights go to management.
- Two management shapes: Azure portal (cloud; integrates Sentinel, workbooks, recommendations) vs locally-managed sensor console (fully on-premises). Cloud-connected sensors receive Microsoft threat-intelligence packages automatically; local sensors get them manually.
- Hybrid cloud/on-prem/hybrid deployment options; built for large geographically distributed environments.

**Analytics engines (named, on-sensor)**
- Protocol violation detection — packet structures/field values violating ICS protocol specifications (example alert: "Illegal MODBUS Operation (Function Code Zero)").
- Policy violation — deviation from learned/configured baseline; behavioral anomaly detection per NISTIR 8219; examples: unauthorized HTTP user agent, unauthorized function-code use, device configuration changes.
- Industrial malware detection — known ICS malware behaviors (Conficker, Black Energy, Havex, WannaCry, NotPetya, Triton; example: "Suspicion of Malicious Activity (Stuxnet)").
- Anomaly detection — unusual M2M communications; ICS-modeled engines "require a shorter learning period than analytics developed for IT"; examples: periodic behavior in communication channel, PLC scan detected.
- Operational incident detection — equipment-failure signs: "Device is Suspected to be Disconnected (Unresponsive)", Siemens S7 stop PLC command.
- Detection policy steers engines to focus on OT-relevant alerts: all engines except Malware trigger only if related to an OT subnet or protocol; Malware engine always triggers; Operational engine has exceptions for critical scenarios.

**Device inventory (the estate record)**
- Devices keyed by unique IP+MAC coupling; automatic consolidation of detections of the same device across sensors within the same zone; zones/sites structure is a first-class planning concept ("Define sites and zones … gain clarity in the data detected by your sensors").
- Device classes span manufacturing (pneumatic devices, packaging systems, industrial robots), building, healthcare, transportation/utilities, energy/resources ("DCS controllers, PLCs, historian devices, HMIs"), endpoints, enterprise, retail.
- OT-specific attributes: **PLC mode** (Key state: Run/Program/Remote/Stop/Invalid/Programming Disabled; Run state: Run/Program/Stop/Paused/Exception/Halted/Trapped/Idle/Offline), **Programming device** flag (engineering stations performing programming for PLCs/RTUs/controllers), **Purdue level**, protocols, VLAN, rack/slots/module address, firmware vendor/model/version, serial number.
- Editable enrichment: name, description, importance (Low/Medium/High), location, business function, type/subtype, tags.
- Authorization lifecycle: during the learning period all detected devices are *authorized*; afterwards new devices are *unauthorized* and *new*; unauthorized remains until a user manually marks the device authorized. Unauthorized devices feed attack-vector and risk-assessment reports as suspected rogue devices.
- "Important" marking feeds attack-vector simulations (as targets) and risk-assessment scoring.
- Endpoints already managed by Defender for Endpoint are not double-counted.

**Alerts / triage**
- Alerts triggered when sensors detect "changes or suspicious activity in network traffic that needs your attention".
- Statuses/triage: New, Active, Closed, **Learn** (close + add traffic as allowed → baseline update; e.g., firmware version change after standard maintenance, new expected device), **Mute** (close without allowing; e.g., investigated PLC-mode change deemed acceptable). Unlearning only on sensor.
- Learning mode: initial period after deployment; sensor learns baseline (devices, protocols, regular file transfers); learning-mode triage marks expected activity as authorized.
- Aggregation: alerts from different sensors in the same zone within a 10-minute window with same type/status/protocol/devices unified into one alert; violation-level export (CSV) for pattern analysis.
- Custom alert rules on sensors (example given: detect any written commands to a memory register on a specific IP/ethernet destination).
- Forwarding to partner SIEMs, syslog, email; MITRE ATT&CK tactics/techniques shown in Azure; Sentinel integration with incident linkage and status sync.
- Auto-close: new alerts automatically closed if no identical traffic for 90 days after initial detection.
- Device map and event timeline on sensor console as investigation surfaces.

**Risk / exposure**
- Vulnerability assessment + security recommendations in Azure portal; risk-based prioritization ("missing patches, vulnerabilities … prioritize fixes based on risk scoring and automated threat modeling").
- Attack vector reports: simulation of attack paths using unauthorized devices as suspected rogues and important devices as targets.
- Risk assessment reports with security scores.
- Zero Trust framing for OT networks.

### Nozomi Networks (Evidence layer: A for platform structure claims on the fetched page; B when generalized)

- Platform = **managers** (Vantage cloud; Central Management Console on-prem) + **sensors** (Guardian network; Arc endpoint; Arc Embedded — "security sensor embedded inside ICS endpoints" e.g. Mitsubishi PLC; Guardian Air wireless; Remote Collector for remote sites) + **analysis/intelligence add-ons** (Vantage IQ AI assistant; Asset Intelligence — classification accuracy + vulnerability/recall currency; Threat Intelligence — OT/IoT zero-days from Nozomi Labs; Smart Polling — "discrete active polling to proactively check devices").
- Solutions framing: asset inventory management, threat detection & response, continuous network monitoring, vulnerability management, risk management.
- "Continuously discover and map every connected asset — from sensor to software — across wired and wireless networks."
- Risk scoring "at the asset, zone, site and enterprise levels", standards-informed; customizable scoring aligned to operational realities.
- "Non-intrusive monitoring and prioritized remediation guidance help teams contain threats before they affect operations or safety."
- Multi-hierarchical management "nested and geo-distributed to 1,000s of locations".
- Compliance content: ISA/IEC 62443, NERC CIP (incl. CIP-015), NIS2, TSA security directives, SEC rules.
- Industries: electric utilities, oil & gas, manufacturing, water, mining, rail, maritime, airports, healthcare, pharma, retail, smart cities, government.

### Dragos (Evidence layer: A for platform structure claims on the fetched page; B when generalized)

- Platform pillars: **Asset Visibility** ("passive & active", OT-native protocols, "south of the firewall", inventory across "OT, IT, IoT, IIoT, and all systems whose failure would affect physical operations"); **Network Monitoring** ("600+ ICS protocols", active + passive, "without disrupting operations"); **Vulnerability Management** ("OT-corrected scoring", "Now, Next, Never" framework, "only 3-6% of OT vulnerabilities require immediate action"); **Threat Detection** (multi-detection enriched by OT threat intelligence; "26+ OT adversary groups"); **Response Playbooks** (expert-authored, case management); **Neighborhood Keeper** (anonymous collective-defense intelligence sharing); **EmberAI** (AI trained on OT telemetry/adversary research).
- Positioning: "The Cybersecurity Platform Built for OT Environments"; xOT (extended OT) framing.
- Detection philosophy: "Detects threats that generic security tools miss because it understands OT protocols, OT behavior, and the adversaries that specifically target OT environments."
- Services wrapped around the platform: OT Watch (proactive threat hunting / managed platform operations), OT cyber assessment, red team, tabletop, incident response (SLA-backed).
- Industries: oil & gas, electric, water, manufacturing, chemicals, pharma, mining, transportation, building automation.

### Claroty (Evidence layer: A for platform structure claims on the fetched pages; B when generalized)

- Platform modules: **Asset Inventory**, **Exposure Management**, **Network Protection**, **Secure Access**, **Threat Detection**, **Operational Efficiency**.
- Discovery methods (named): Claroty Edge, Passive Monitoring, Safe Queries, Project File Analysis, Ecosystem Enrichment — "multiple asset discovery methods … based on what's best for your unique environment"; "without disrupting daily operations"; inventory "in minutes".
- Asset inventory: precise attributes via "CPS Library"; "purpose-based hierarchy" organizing devices; per-asset risk scoring reflecting business impact ("If a certain device is critical to production, its risk score will reflect its business impact"); continuous measurement of visibility gaps with a remediation roadmap.
- Exposure management: automatic scoping of CPS assets, vulnerability identification/prioritization, "highlighting specific attack vectors", actionable recommendations.
- Network protection: leverages visibility to "automatically define and recommend network policies"; "monitor, refine, and automatically enforce these policies with your existing firewalls, switches, or NAC solutions" — segmentation and Zero Trust via orchestration, not a proprietary inline engine.
- Secure access: controlled third-party/vendor remote access to CPS.
- Threat detection: continuous monitoring for "earliest indicators of both known and emerging threats"; alerts contextualized; integrates with SIEM, SOAR, EDR.
- Deployment: xDome (SaaS, modular) vs CTD (on-premises, "flexibility to choose where and how to deploy … scalability, cost considerations, or compliance guidelines").
- Scope framing: CPS = OT (PLC, RTU, HMI, SCADA, DCS, historian) + IIoT + IoT + IoMT + BMS; verticals across industrial, healthcare, commercial, public sector.

### Forescout eyeSight (Evidence layer: A for product-page claims; B when generalized)

- "Agentless visibility" across "extended enterprise"; discovers "every IPv4 and IPv6 connected device, auto-classifies it, and assesses its compliance posture and risk the instant a device connects".
- "Passive-only profiling techniques" for "sensitive IoT, IoMT, OT and critical infrastructure systems without impacting system uptime, introducing operational risk or disrupting critical business processes".
- How it works: **Discover** (20+ passive and active monitoring techniques, managed and unmanaged devices) → **Classify** (multi-dimensional: function, type, OS incl. version, vendor, model) → **Assess** (configuration, state, security → compliance posture and risk profile).
- Complete asset inventory across campus, data center, cloud, and OT networks; IoT, IoMT, OT, mobile, network infrastructure.
- OT Security solution framing: "Agentless visibility, threat detection, and configuration monitoring for OT and ICS environments."
- Platform (Vistaro) siblings: NAC, network segmentation, ZTNA, exposure management, secure remote access — enforcement lineage visible in the solution family.

---

## Cross-product Comparison

| Dimension | Defender for IoT | Nozomi | Dragos | Claroty | Forescout eyeSight |
|---|---|---|---|---|---|
| Estate record (assets + communications) | Device inventory keyed by IP+MAC; consolidated per zone | Asset inventory "from sensor to software" | Asset visibility incl. "systems whose failure would affect physical operations" | Asset inventory with CPS Library attributes | Complete asset inventory, IPv4/IPv6 |
| Self-assembled (observed, not enrolled) | SPAN/TAP sensors; enrichment from Defender for Endpoint | Passive + active sensors; Smart Polling | Passive & active network monitoring | Passive Monitoring, Safe Queries, Project File Analysis, Ecosystem Enrichment, Edge | 20+ passive/active techniques; agentless |
| OT asset identity depth | PLC mode, programming-device flag, Purdue level, rack/slots | Asset Intelligence classification add-on | OT-native protocol identification | CPS Library precise attributes | function/type/OS/vendor/model classification |
| Protocol/process-aware detection | L6 DPI; protocol-violation engine; ICS-modeled anomaly engines; industrial malware engine | OT/IoT-specific detection; behavioral anomalies | 600+ ICS protocols; OT behavior + adversary detection | Continuous threat detection contextualized to CPS | Threat detection + configuration monitoring (OT/ICS) |
| Baseline learning | Learning mode; Learn/Mute semantics; NISTIR 8219 BAD | Behavioral baselines | (implied in detection) | (implied in detection) | (assessment-centric) |
| Change detection | New/unauthorized device states; config-change alerts | (in detection) | (in detection) | (in detection) | configuration monitoring |
| Vulnerability/exposure mgmt | Vulnerability assessment + recommendations + threat modeling | Vulnerability management solution | OT-corrected scoring; Now/Next/Never | Exposure Management module | Exposure Management (platform) |
| Risk scoring w/ operational context | Importance marking; risk-assessment reports | asset/zone/site/enterprise scoring | OT-corrected scoring | business-impact scoring per asset | compliance posture + risk profile |
| Production-structure organization | Sites, zones, Purdue level | zones, sites, enterprise hierarchy | (facility-oriented) | purpose-based hierarchy | (network-oriented) |
| Attack-path analysis | Attack vector reports | (risk views) | (in vulnerability mgmt) | "highlighting specific attack vectors" | (in exposure mgmt) |
| Threat intelligence | Microsoft TI packages pushed to sensors | Nozomi Labs TI; Mandiant pack | 26+ adversary groups; WorldView | Team82 | Vedere Labs |
| SOC integration | Sentinel, SIEM/syslog forwarding, ATT&CK mapping | Integrations ecosystem | Sentinel data flow; playbooks | SIEM/SOAR/EDR integration | (platform integrations) |
| Operational (non-security) alerts | Operational engine (disconnected device, S7 stop) | operational resilience framing | (operational context) | Operational Efficiency module | (uptime framing) |
| Enforcement | none observed (detect + integrate) | none observed (detect + integrate) | none observed (detect + integrate) | recommend + orchestrate via existing firewalls/switches/NAC | NAC/segmentation heritage in platform family |
| Deployment shapes | cloud (Azure) or fully local sensors | cloud (Vantage) or on-prem (CMC) | (platform + services) | SaaS (xDome) or on-prem (CTD) | appliances + platform |
| Population scope | OT + IoT (+ enterprise IoT via MDE) | OT + IoT | OT/IT/IoT/IIoT ("xOT") | OT + IIoT + IoT + IoMT + BMS (CPS) | extended enterprise incl. OT/IoT/IoMT |
| AI overlay | (Microsoft Copilot ecosystem adjacent) | Vantage IQ | EmberAI | Claire | VistaroAI |
| Managed service | (via Sentinel/MDE ecosystem) | professional services | OT Watch managed hunting/ops | (partner-delivered) | (partner-delivered) |

Reading of the comparison:

- The **estate record** and **continuous security detection** are present in all five, in every case assembled from network-side observation rather than device enrollment. (Layer B)
- **Protocol/process awareness** is claimed by all five in OT-specific terms (Layer B); Microsoft's engine list shows the concrete realization classes: protocol violations, baseline deviations, industrial malware, M2M anomalies, operational incidents. (Layer A)
- **Vulnerability/exposure management** is present in all five current products (Layer B) but is a module/solution in each — not the platform's spine. Historical SCADA-IDS generation lacked it (conceptual). → L1.
- **Zone/site/production-structure organization** appears in most (Microsoft sites/zones/Purdue; Nozomi zones/sites; Claroty purpose hierarchy) but not as a uniform structure; Forescout is network-oriented. → L1.
- **Enforcement** splits the sample: none / recommend-and-orchestrate / NAC-heritage. → L2 variant posture, not definitional.
- **Passive-first collection** is explicit in all five (SPAN/TAP, passive monitoring, "without disrupting operations", "passive-only profiling"). It is the behavioral signature of the Type. → rule, not structure.
- **Dual alert semantics** (security + operational) explicit in Microsoft (operational engine) and echoed in others' framing. → L1.
- **AI overlays** present in four of five current products → common-mature, not definitional.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (minimal)

Two jointly-held structures, both qualified by the OT orientation:

1. **The OT control-estate record.** A persistent, self-assembled model of the industrial control environment: control assets (controllers — PLC/RTU/DCS; operator and engineering stations; HMIs; historians; network devices) and their control communications, each held as an individually identified record classified in OT terms (device role/type, protocols spoken, firmware, location in the production structure). Assembled by observing the OT network itself — passive traffic analysis, carefully limited active queries, enrichment from systems that already know the assets — never by enrolling or instrumenting the controllers. *Remove → a protocol-aware IDS with no estate picture, or a generic asset list.*

2. **Control-aware security detection.** Continuous evaluation of observed OT activity against security expectations — learned baselines of normal control behavior, known-threat signatures/intelligence, and change rules (new or unknown device, new communication relationship, control-program/firmware/configuration change, protocol misuse) — producing security findings bound to identified assets, triaged by a human operator. *Remove → an asset inventory / cyber-asset-management territory.*

OT orientation (the qualifier that makes both structures OT rather than generic): the estate is the industrial control environment — safety- and availability-critical, where the platform itself must not disturb operations and where the semantics that matter are control semantics (what commands reach controllers, what changed in control logic), not generic IT traffic.

Jointly-held load-bearing tests:
- 1 without 2 = OT asset inventory / cyber asset management.
- 2 without 1 = industrial IDS / NDR territory (detection with no estate record).
- both without the OT orientation = IT network monitoring / generic device security.

### L1 — Common Mature Structure

- Production-structure organization: sites, zones, cells/lines, Purdue-level mapping.
- Vulnerability/exposure management matched against the estate, prioritized by operational impact; attack-path/exposure analysis.
- Risk scoring with asset criticality / business context.
- OT/ICS-specific threat intelligence feeds.
- SOC integration: SIEM/SOAR forwarding, ATT&CK-style mapping, ticketing.
- Compliance reporting (IEC 62443, NERC CIP, NIS2, TSA directives — regime-dependent).
- Operational alerts alongside security alerts (device unresponsive, controller stopped) — shared observation point.
- Learning period before behavioral alerting is trusted; learn/mute-style baseline updates.
- Communication topology / network map as investigation surface.
- Multi-site aggregation with central management (cloud or on-prem).
- AI assistance overlays.

### L2 — Variant / Optional Structure

- Enforcement posture: detect-and-integrate only (Microsoft/Nozomi/Dragos in sample) vs recommend-and-orchestrate through existing firewalls/switches/NAC (Claroty) vs native network enforcement lineage (Forescout platform family).
- Deployment: cloud-managed vs on-premises vs air-gapped/local-only sensors.
- Collection mix: passive-only (Forescout's posture for sensitive environments) vs passive + active queries; endpoint sensors (Nozomi Arc); sensors embedded in controllers (Nozomi Arc Embedded); agent-based collection for capable devices (Microsoft micro agent for device builders); project-file analysis (Claroty).
- Population scope: OT-only vs OT+IoT+IoMT+BMS ("CPS") vs "xOT".
- Vertical packaging: electric, water, oil & gas, manufacturing, healthcare/IoMT, building automation.
- Managed-service delivery: threat hunting / platform operation as a service (Dragos OT Watch).
- Secure remote-access management for vendors/third parties (Claroty Secure Access; Forescout SRA in family).
- Collective-defense intelligence sharing (Dragos Neighborhood Keeper).

### L3 — Vendor-specific (research notes only)

- Microsoft: Azure portal/Sentinel/MDE integration; NISTIR 8219 reference; named engine list; PLC Key/Run state vocabularies; 10-minute alert aggregation window; 90-day auto-close; Learn/Mute semantics; micro agent for device builders.
- Nozomi: Vantage/CMC/Guardian/Arc/Guardian Air product names; Mandiant-powered TI pack; Mitsubishi-embedded sensor; "1,000s of locations" claim.
- Dragos: Now/Next/Never framework; "600+ ICS protocols" and "3-6% of vulnerabilities" and "26+ threat groups" claims; Neighborhood Keeper; OT Watch; EmberAI.
- Claroty: xDome/CTD split; Team82; CPS Library; Claire; Edge/Safe Queries/Project File Analysis method names.
- Forescout: eyeSight/Vistaro naming; Vedere Labs; OT:ICEFALL research line; "20+ techniques" claim.

## Rejected Findings (considered for core, rejected)

- **Vulnerability management as definitional** — present in all five current products, but each implements it as a module; the SCADA-IDS generation (conceptual evidence, reduced confidence) detected without vulnerability matching; OTbase-style inventory+vuln products exist without detection (boundary probe). → L1.
- **Zone/Purdue organization as definitional** — common but not universal in the sample (Forescout network-oriented); a flat estate with OT classification still reads as the Type. → L1.
- **Enforcement/blocking as definitional** — majority of sample does not enforce inline; where enforcement exists it is a heritage posture or orchestration. → L2.
- **"Passive-only" as definitional** — all sample products are passive-first, but several actively query (Smart Polling, safe queries, active monitoring techniques); the invariant is "must not disturb operations", not "never actively queries". → rule.
- **Dual security/operational alerts as definitional** — strong pattern but operational alerts are a secondary reading; a security-only platform would still be recognized. → L1.
- **AI as definitional** — current-market overlay only. → L1.
- **Cloud management as definitional** — locally-managed/air-gapped sensors are first-class in the sample. → L2.

## Boundary Findings

- **vs IoT Security Platform (sibling leaf).** Same market family: security for device populations that cannot carry agents, built from network-side observation. The IoT doc's core (device population + per-device assessment + continuous behavior monitoring) also *describes* OT platforms at high generality — which is exactly why the leaves must be separated by center of gravity, not by mutually exclusive structure. OT security centers the **industrial control environment**: controllers and control protocols as the estate's spine, control-process semantics in detection (what wrote to the PLC, what changed the control law, what stopped the controller), production-structure organization, and safety/availability-first posture. IoT security centers the **enterprise/facility device estate** (printers, cameras, badges, medical devices, building systems) with per-device assessment emphasis. Most vendors serve both populations with the same platform family; the leaves differ by emphasis. **Recorded for joint review** — reciprocating the IoT doc's note. Boundary test: remove the control-process orientation (controllers, control protocols, production structure, availability-first constraint) and the product is an IoT security platform; remove the facility/enterprise device breadth and keep only the control environment, and it is an OT security platform.
- **vs NDR.** NDR's core is an out-of-band network observation plane + entity picture + threat detection + investigation loop over IT network traffic. An OT platform shares the passive observation plane and behavioral detection but its unit of record is the control estate with process semantics, its detection vocabulary is control-protocol-aware, and it carries the availability-first constraint. NDR without OT protocol/process semantics and without the control-estate record is below this Type; an OT platform is not a general IT-network threat-hunting surface.
- **vs Network Monitoring (IT).** Network monitoring's purpose is operational health of IT infrastructure; the OT platform's purpose is security of the control estate. The OT platform emits operational alerts (device unresponsive, controller stopped) as a secondary reading because security and process failure share one observation point — but an ops-health tool with no security detection is not this Type.
- **vs Vulnerability Management.** VM is scan-centric over IT software assets with patch pipelines. OT exposure management is executed without credentialed scans against unpatchable controllers, prioritized by operational impact, and leans on compensating controls (segmentation, access rules) because patching is frequently impossible. VM-style scanning of a control network would violate the Type's own constraint.
- **vs Cyber Asset Management.** Inventory-centric, multi-class estate record without the continuous security detection loop. An OT platform whose detection was removed would collapse into this.
- **vs SIEM.** Downstream aggregator of security events org-wide; the OT platform is a specialized detection source and asset-context provider feeding it (explicit forwarding integrations in the sample).
- **vs inline Network Security Platform (processed leaf).** The network security platform enforces policy on traffic paths (inline). The OT platform observes; even enforcement-capable relatives act at connection/admission or orchestrate existing controls, and the sample's majority does not enforce at all.
- **vs SCADA / DCS / HMI / Industrial Historian (§16 leaves).** Those are the operational control systems themselves — they run the process. The OT security platform observes and protects them and never writes to the process. A "security feature" inside a DCS is not this Type.
- **vs Industrial IoT Platform.** IIoT connects and operationalizes industrial devices for production purposes (telemetry, monitoring, control enablement); not a security system of record.

## §24 Historical / Market-Sample Check

Question: would older, regional, platform-native, or differently positioned products still fit the L0?

- **Pre-software era:** air-gapped control networks governed by policy and physical isolation — no software platform exists; the Type's lineage begins when monitoring software appears. No conflict.
- **SCADA-IDS generation (conceptual; source unreachable):** signature-based intrusion detection for industrial protocols (e.g., Snort preprocessors/rules for DNP3/Modbus) deployed on passive taps — estate-lite (protocol-aware device sightings) + control-aware detection, with no cloud, no AI, no vulnerability matching, no zone hierarchy, no risk scoring. This satisfies the two L0 structures and nothing else — supporting L0 minimalism. **Confidence reduced**: the primary source (Digital Bond) was unreachable; this leg rests on conceptual lineage, not fetched evidence.
- **Regional/heritage vendors:** European and Asian SCADA-security products follow the same passive-sensor + inventory + detection shape (conceptual, low confidence — not fetched). No conflict with L0.
- **Current minimal poles:** Forescout's passive-only posture and Claroty's on-prem CTD show cloud and AI are not required; Microsoft's locally-managed sensors show cloud management is not required. No conflict.
- **Check passes:** the L0 names no cloud, no AI, no vulnerability matching, no Purdue model, no specific protocol set, no enforcement. The earliest recognizable generation and the most constrained current deployments both satisfy it.

## Uncertainties

1. **Protocol coverage counts** ("600+ ICS protocols") are vendor marketing claims — not independently verified; kept out of the final document.
2. **Vulnerability-management universality:** all five sampled current products include it, but the sample is current-market; historical products apparently lacked it (unfetched). Held at L1 with this caveat.
3. **IoT/OT leaf seam:** the two leaves are one market family; the boundary is drawn by center of gravity. Some products are marketed under both names. Recorded in STATUS Boundary Issues for joint review rather than resolved unilaterally.
4. **Managed-service blur:** Dragos OT Watch (managed detection/hunting) wraps the platform in a service; whether "OT security platform" includes the service wrapper is a packaging question, not a Type question.
5. **Forescout/Nozomi/Dragos/Claroty observed at product-page depth only** (docs sites unreachable or empty); Microsoft at full docs depth. Precise operational details (numeric limits, exact state vocabularies, engine lists) for the four Tier-2 products are intentionally not asserted in the final document.
6. **Enforcement prevalence:** the sample suggests most OT platforms do not enforce inline, but the sample is small; held as variant posture with the NAC-heritage exception noted.

## Final Synthesis

An OT Security Platform is the security team's system of record for an industrial control environment and the engine of its security loop. Its defining core is two jointly-held structures: the **OT control-estate record** (control assets and their communications, self-assembled from network observation, classified in OT terms) and **control-aware security detection** (continuous evaluation of observed activity against baselines, threat intelligence, and change rules, producing asset-bound findings for human triage) — both qualified by the OT orientation: a safety- and availability-critical environment the platform must not disturb, where the semantics that matter are control semantics. Everything else — zones and Purdue mapping, vulnerability/exposure management, risk scoring, threat intelligence, SOC integration, compliance reporting, operational alerts, AI overlays — is mature structure; enforcement posture, deployment shape, collection mix, population scope, and vertical packaging are variants. The Type sits in a market family with IoT Security Platform (sibling, different center of gravity) and is bounded against NDR, Network Monitoring, Vulnerability Management, Cyber Asset Management, SIEM, inline network security, and the control systems it protects.
