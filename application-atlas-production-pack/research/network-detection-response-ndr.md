# Research Notes — Network Detection & Response / NDR

Research date: 2026-09-08
Slug: network-detection-response-ndr
Directory leaf: Network Detection & Response / NDR (§15 Cybersecurity, Identity & Trust)

---

## Research Goal

Understand what a Network Detection & Response (NDR) application actually is as a software type: what telemetry it consumes, what objects exist inside it, how detection → investigation → response actually flows, who operates it, and where its boundaries sit against EDR, SIEM, Network Monitoring, and inline network security products.

## Initial Boundary (working hypothesis before research)

- Core use: continuously observe network traffic to detect malicious/suspicious behavior that bypasses perimeter and endpoint defenses, and support investigation and response.
- Primary users: SOC analysts, threat hunters, network security engineers.
- Nearest neighbors: Network Monitoring (performance-oriented), EDR (endpoint agents), SIEM (log aggregation), Network Security Platform / IPS (inline prevention), XDR (cross-domain).
- Unknowns at start: exact response realizations (native vs integration-mediated), telemetry mix (packets vs flows), deployment shapes, how the asset/entity inventory relates to detection.

## Research Questions

1. What telemetry does NDR consume? (packets via TAP/SPAN, NetFlow/IPFIX, cloud flow logs, network-derived logs)
2. What are the core objects? (sensor, entity/device, detection, investigation, response action, retained evidence)
3. How are detections produced? (signatures/IDS, behavioral baselines, ML, threat intelligence, custom rules)
4. What is the lifecycle of a detection? (generation → triage → tracking → closure/tuning)
5. What does "response" concretely mean in current products? (native containment, integration-mediated actions, analyst-led)
6. What interfaces do analysts face? (detection queues, detection detail, entity pages, investigation workspaces, packet forensics)
7. What deployment shapes exist? (appliances, virtual, cloud, software sensors, SaaS consoles, self-managed)
8. How do vendors themselves articulate the boundary vs EDR / SIEM / NTA / NPM?

## Representative Products

Selected for market representativeness, different detection philosophies, and different organizational postures:

1. **Darktrace / NETWORK** — self-learning per-organization behavioral AI; autonomous response; multi-product platform (Network/Email/Cloud/OT/Identity/Endpoint). Evidence: product page + corporate site (Tier 2).
2. **Vectra AI Platform** — behavioral AI for SOC prioritization ("observe / signal / control"); network+identity+cloud expansion. Evidence: platform page (Tier 2); operational docs (docs.fusion.vectra.ai) not fetched.
3. **ExtraHop RevealX (Enterprise / 360)** — wire-data/packet analytics; NDR and NPM as licensed modules on one platform; extensive Tier-1 user documentation. Evidence: full doc portal (Tier 1).
4. **Corelight Open NDR Platform** — open NSM heritage (Zeek + Suricata), evidence-first philosophy; sensors + SaaS Investigator; federal/enterprise base. Evidence: product pages + glossary (Tier 2, product pages unusually operational).

Rejected/abandoned: Cisco Secure Network Analytics (flow-based pole) — product page returned HTTP 403 on fetch; per source-access rules the source was dropped rather than retried. The flow-telemetry pole is nonetheless documented through ExtraHop flow sensors (NetFlow + VPC flow logs) and Corelight Flow Log Sensors.

## Sources

- ExtraHop — Documentation portal: https://docs.extrahop.com/ (2026-09-08)
- ExtraHop — Introduction to the ExtraHop system: https://docs.extrahop.com/current/intro-to-eh-system/ (2026-09-08) [Tier 1]
- ExtraHop — Detections: https://docs.extrahop.com/current/detections-overview/ (2026-09-08) [Tier 1]
- Corelight — All Products: https://corelight.com/products (2026-09-08)
- Corelight — Investigator: https://corelight.com/platform/investigator (2026-09-08)
- Corelight — Glossary "What is NDR": https://corelight.com/resources/glossary/ndr-network-detection-and-response (2026-09-08)
- Darktrace — Darktrace / NETWORK: https://www.darktrace.com/products/network (2026-09-08)
- Darktrace — corporate site: https://darktrace.com/ (2026-09-08)
- Vectra AI — AI Cybersecurity Platform: https://www.vectra.ai/platform/ai-cybersecurity-platform (2026-09-08)
- Vectra AI — corporate site: https://www.vectra.ai/ (2026-09-08)

Evidence layers: A = directly observed on official product documentation for that product; B = cross-product commonality; C = canonical inference (labeled in Final Synthesis). Darktrace/Vectra observations are mostly A-at-product-page depth (marketing + FAQ), not help-center depth; ExtraHop observations are help-center depth. Assertion strength calibrated accordingly.

---

## Product A — ExtraHop RevealX (Tier 1 depth)

### Key observations (Layer A)

- **System architecture (sensors + stores + console):** packet sensors passively observe unstructured packets "through a port mirror or tap"; components are sensors, packetstores, recordstores, and consoles ("a command center for all connected components"). Solutions: RevealX Enterprise (self-managed) vs RevealX 360 (SaaS).
- **Sensor types:** packet sensors (wire data), IDS sensors (add-on module with packet sensor), flow sensors (NetFlow; VPC flow logs for AWS, RevealX 360 only). Flow logs are "ingested, deduplicated, and then grouped into flows," enriched from AWS EC2 APIs.
- **Wire-data pipeline:** TCP state machine reassembly → packets grouped into flows → transactions identified → devices automatically discovered and classified by activity → metrics generated per protocol → FIFO aging. This is the deepest public articulation of the telemetry plane found in the sample.
- **Three data depths:** metrics (aggregated observations), records (structured transaction/message/flow records, queryable, storable in recordstores or third-party Splunk/BigQuery), packets (raw, continuous capture in packetstores for "deeper investigations and forensic needs").
- **Device discovery:** automatic discovery of clients, servers, routers, load balancers, gateways by MAC (L2) or IP (L3); devices classified by activity; automatic role assignment (gateway, file server, database, load balancer); manual high-value designation; software/OS fingerprinting; VPN discovery correlating private VPN IPs with public IPs.
- **Detection generation — three methods (official):** (1) network traffic observation — indicators matching CVE exploit attempts, common attack tools, command-and-control frameworks, hardening opportunities (expired certificates, weak cipher suites); (2) machine learning analysis — long-term baselines per device and device groups, detections on deviation (activity spikes, first-time actions), dynamic risk scores, high-value device identification; (3) IDS detections — signature matches against cloud-updated IDS rulesets (Proofpoint Emerging Threats rulesets + vendor-curated), custom Suricata rules upload supported.
- **Detection object:** detection card with risk score (likelihood, complexity, business impact; color bands red 80–99 / orange 31–79 / yellow 1–30 — product-specific detail), participants (offender/victim; client/server or sender/receiver labels), duration ("ONGOING" state exists), metric data, signature (events/indicators/conditions/ML).
- **Participants:** endpoints involved; internal devices by name/IP; usernames only from specific protocols (FTP, Kerberos, LDAP, NTLM, RDP, RPC, SMB) — product-specific detail; external endpoints by IP with geolocation and whois lookup links.
- **Detection lifecycle:** status filter Open (default) / Acknowledged / In Progress / Closed; Hidden status via tuning rules; assignee; notes; optional third-party ticket ID ("detection tracking"). Tuning rules "hide past, present, and future detections that are of low-value." Custom detections can be created.
- **Views:** Summary (grouping by type/participant/none), Triage (Smart Triage — recommendations with factors: high value asset, high privilege user, high influence user, top offender, rare detection type, threat-intel-listed indicator, recommended investigation; rate limits per factor documented), MITRE map (detections plotted on ATT&CK matrix), Investigations table.
- **Investigations:** "add and view multiple detections in a single timeline and map" to judge whether behavior is one attack or a campaign; **recommended investigations** auto-created by the ML service "when a combination of attack techniques… might indicate malicious behavior."
- **Attack categories (official):** Command & Control, Reconnaissance, Exploitation, Lateral Movement, Actions on Objective, Caution; plus Performance categories (Authentication, Database, Network Infrastructure, Service Degradation, Storage, Web Application, Desktop & App Virtualization) and Hardening; plus Intrusion Detection. The performance categories belong to the NPM module — the same platform hosts both.
- **Module split (official):** NDR module (security detections, investigations, threat briefings, MITRE map, tuning/notification rules, threat intelligence, file analysis) vs NPM module (performance detections, alerts, flow-log collection) with RBAC per module; IDS module requires NDR; Packet Forensics module adds full packet capture/storage/retrieval.
- **Response:** integration-mediated — with a configured CrowdStrike integration, an analyst can "initiate containment of CrowdStrike devices that are participants in a security detection" ("Containment prevents devices from establishing connections to other devices"); Microsoft Entra ID / Okta integrations can add "additional user properties or response actions." No inline blocking.
- **Decryption:** TLS decryption configurable; "analyzes traffic in real-time and does not write decrypted payload data to disk" (product-specific).
- **Retention:** sensors provisioned with 30 days of metric lookback (product-specific); packetstores/recordstores extend evidence retention.
- **Cloud services:** detection catalog and threat intelligence updated from cloud.

## Product B — Corelight Open NDR Platform (Tier 2, operationally rich)

### Key observations (Layer A at product-page depth)

- **Platform structure:** "Evidence-first, open-core NDR with AI-powered detection and Agentic Triage." Capabilities listed as Network visibility ("AI-ready evidence"), Threat detection ("AI-driven ML, behavioral, and signature with explainability"), Incident response ("10x faster autonomous AI investigations"), Defensible AI.
- **Components:** Sensors ("Passive AI/ML intelligent monitors for any architecture"), Investigator (SaaS-based NDR — AI workflows and agentic triage), Fleet Manager (sensor fleet management, config templates, ML detection orchestration).
- **Sensor fleet:** appliance sensors (AP series, throughput tiers 4–125+ Gbps — product-specific), virtual (VMware/Hyper-V), software, cloud sensors (AWS/GCP/Azure; SaaS or self-managed), and **Flow Log Sensors** — "Transform raw cloud and network flow logs into enriched, security-ready Zeek data — extending visibility where packet mirroring isn't available."
- **Detection content:** Detection Collections — C2 Collection (50+ detections, MITRE ATT&CK C2 techniques), Core, Encrypted Traffic Collection ("insights into SSL, SSH, RDP connections… without decryption", JA3), Entity Collection ("searching and grouping on entity inventory, including identification of subnets and 80+ applications"), ICS/OT Collection (BACnet, DNP3, Ethercat, Modbus...), Analyzers Collection. Plus Suricata IDS module, Threat Intelligence (CrowdStrike premium + Corelight), YARA file analysis, Smart PCAP ("Capture just the packets you need… store months—not minutes—of traffic history").
- **Investigator (response/investigation console):** "Replace noisy, isolated alerts with clear, **entity-centric case files** and transparent reasoning." Agentic Triage: consolidates and analyzes highest-priority entities every 24 hours; investigates last 7 days of host activity; correlates detections and raw log queries "into a single narrative"; outputs narrative + reasoning + recommended next steps. Detections validated through "structured investigative workflows." MITRE ATT&CK coverage across 100+ techniques. Users: Tier 1 (summaries/triage), Tier 2 (root cause), Tier 3/threat hunters (evidence, queries, forensic access).
- **Response:** "built-in containment" — "analysts can isolate compromised hosts, enforce firewall policy changes, and trigger response actions directly from validated cases"; "Detection-to-response within one workflow"; "Evidence-backed justification for every action taken."
- **Deployment:** on-prem, SaaS, hybrid, multi-cloud; sensors sit out of band (per glossary: "Most NDR sensors sit out of band, which minimizes disruption within the ecosystem").
- **Category articulation (glossary):** NDR = "continuously monitors network traffic from physical and cloud-based environments. NDR solutions include extended visibility, enriched network data, detection, threat hunting, forensics and response capabilities… delivered as a combination of physical, virtual, software, and cloud appliances." Data collection from firewalls, cloud packet mirrors, SPAN ports, TAPs; structured into correlated logs. Coverage: north/south + east/west, remote users, encrypted telemetry, OT/ICS. Detection mix: signature IDS, YARA file analysis, anomaly-based, ML. Long-term PCAP for forensics; "forensic vaults… years-long lookbacks" (category-level claim). **SOC Visibility Triad:** EDR (endpoint depth) + NDR (network breadth) + SIEM (storage/aggregation). Response examples: "host isolation, automated ticket generation."
- **Encrypted traffic:** metadata-based analysis without decryption as an explicit alternative (timestamps, packet sizes, protocol behavior).

## Product C — Darktrace / NETWORK (Tier 2)

### Key observations (Layer A at product-page depth)

- **Philosophy:** "Traditional NDR relies on historical attack data… Darktrace / NETWORK learns normal behavior for your organization, spotting and stopping deviations." Self-Learning AI trained per customer ("we bring our Self-Learning AI directly to your data").
- **Coverage claim:** on-prem, virtual, cloud, hybrid networks, remote worker endpoints, OT devices, ZTNA; encrypted and decrypted traffic analysis.
- **Detection:** AI "continuously analyzes every connection, device, identity and attack path for unusual behavior"; self-tuning to "cut through the noise" (no manual tuning claim); secondary STIX/TAXII threat intel ingestion for known threats/custom IoC detections.
- **AI investigation:** Cyber AI Analyst — "continually performs end-to-end investigations of thousands of anomalous or risky alerts and prioritizes the ones with the most potential to impact your business"; "autonomously forming hypotheses and reaching conclusions"; correlates across network/endpoint/cloud/identity/OT/email/remote devices.
- **Response:** Autonomous Response — "isolating infected devices, forcing a user to reauthenticate, or blocking suspicious IP addresses"; "natively or via integrations with your existing security investments"; "fully customizable."
- **Ecosystem:** part of Darktrace platform (Email, Cloud, OT, Identity, Endpoint, ASM, Forensic Acquisition & Investigation, Incident Readiness & Recovery); MDR service offering (24/7 analyst monitoring of the customer's environment).
- **Vendor FAQ articulations (category evidence, Layer B corroboration):** NDR vs EDR — NDR monitors network traffic (lateral movement, C2), EDR device-level; NDR vs NTA — "NTA tools primarily focus on passive monitoring and analysis… while NDR is focused on security and adds a response capability. NTA systems can detect anomalies… but typically do not provide automated response capabilities, which is what NDR solutions are designed to do."; NDR vs SIEM — SIEM aggregates multi-source data, NDR specializes in network traffic; NDR vs signature-based IDS/IPS — behavioral detection of novel threats.

## Product D — Vectra AI Platform (Tier 2)

### Key observations (Layer A at product-page depth)

- **Philosophy:** "Your network is the source of truth. Attackers can bypass tools, but they can't bypass the network." Observe / Signal / Control structure.
- **Observability:** "continuously analyzes network activity to reveal every identity, device, and AI agent in real time" — entity inventory from network observation as a first-class function.
- **Signal:** "reveals real attacker behavior as it unfolds, including threats that bypass endpoint and log-based controls"; "200+ behavioral detections" trained on attacker behavior; detection across the attack lifecycle — "reconnaissance, credential abuse, lateral movement, and data access"; correlation and contextualization across hybrid environments for prioritization.
- **Control:** exposure/posture management (weak identities, risky access paths, unmanaged devices, insecure connections) — expansion beyond detection.
- **Integrations:** "delivers high-fidelity, identity-aware signals that make your existing SIEM, SOAR, EDR, and cloud tools more effective"; API/log-based connections; "sends prioritized detections and enriched metadata to SIEM and SOAR… integrating with EDR to correlate endpoint telemetry with network and identity signals"; "support automated response actions."
- **Deployment:** self-managed or MSSP/MDR; "agentless deployment"; "No infrastructure to install" (cloud-native integrations — this refers to the newest cloud offering; the classic product is sensor-based — the page mixes postures; recorded as uncertainty).
- **Category positioning:** Leader in Gartner MQ for NDR 2026, IDC Marketscape 2024 — category label "Network Detection and Response" used verbatim.
- **Blind-spot argument:** "30-40% of devices lack EDR coverage because agents cannot be deployed on them" — the unmanaged/IoT/OT device coverage argument.

---

## Cross-product Comparison

| Aspect | Darktrace / NETWORK | Vectra AI Platform | ExtraHop RevealX | Corelight Open NDR |
|---|---|---|---|---|
| Primary telemetry (A) | network traffic incl. encrypted/decrypted; endpoints incl. OT/ZTNA (product page) | network activity on-prem + multi-cloud (+ identity/M365/edge/IoT-OT expansion) | packets via tap/SPAN (wire data) + NetFlow + VPC flow logs (docs) | packets via TAP/SPAN (Zeek/Suricata sensors) + flow logs (Flow Log Sensors) + cloud sensors |
| Observation posture (A/B) | passive sensors; autonomous response acts via enforcement points/integrations | agentless/cloud-native; network as source of truth | passive port mirror/tap, explicitly | passive, out of band, explicitly |
| Entity inventory (B) | "every connection, device, identity and attack path" learned | entity discovery: identities, devices, AI agents | automatic device discovery (L2/L3), roles, high-value, users | Entity Collection inventory; asset classification |
| Detection machinery (B) | per-org self-learning AI + STIX/TAXII intel | behavioral AI detections (200+ claim), lifecycle-stage oriented | indicators + ML baselines + IDS signatures + custom detections | ML + behavioral + signature (Suricata) + threat intel + query-based collections |
| Detection object (B) | alerts/model breaches; AI analyst investigations | prioritized detections with attack narrative | detection cards: participants (offender/victim), risk score, category, status lifecycle | entity-centric case files with narrative + reasoning + next steps |
| Prioritization (B) | self-tuning AI; business-impact prioritization | AI-driven prioritization of real attacks | risk scores + Smart Triage recommendations + recommended investigations | agentic triage of highest-priority entities |
| Attack framework (B) | (not claimed on fetched pages) | MITRE ATT&CK coverage claim | MITRE map view + technique filters | MITRE ATT&CK mapping (100+ techniques claim) |
| Investigation surface (B) | Cyber AI Analyst + Threat Visualizer | AI-assisted investigations, threat hunts | Investigations view (timeline + map), detection detail page w/ metrics/records/packets | Investigator: structured investigation framework, single-screen entity triage, PCAP access |
| Response realization (B) | native autonomous actions (isolate device, re-auth user, block IP) + integrations | EDR-mediated + SIEM/SOAR orchestration of prioritized detections | integration-mediated (CrowdStrike containment; Entra ID/Okta actions) | built-in one-click host isolation + firewall policy changes from validated cases |
| Retained evidence (B) | (not detailed on fetched pages) | (not detailed on fetched pages) | packetstores (continuous capture), recordstores, metrics (30-day lookback claim) | Smart PCAP (months); category-level years-long lookback claim |
| Encrypted traffic (B) | encrypted + decrypted analysis claim | (not detailed on fetched pages) | metadata detections + optional TLS decryption (decrypted payload not persisted) | Encrypted Traffic Collection without decryption |
| Deployment (B) | (not detailed on fetched pages) | self-managed / MSSP; agentless cloud posture claimed | self-managed (Enterprise) vs SaaS (360); physical/virtual/cloud sensors | on-prem / SaaS / hybrid / multi-cloud; appliance+virtual+software+cloud+flow sensors |
| Adjacent modules (B) | platform products (email/cloud/OT/identity/endpoint) | exposure management, identity/cloud domains | NPM module, IDS module, Packet Forensics module | Zeek NSM, Suricata IDS, threat intel, YARA file analysis, performance & asset visibility, ICS/OT |
| Service wrapper (B) | MDR (24/7 analysts) | MDR/MSSP options | (not on fetched pages) | professional services |

Reading: all four products independently realize the same loop — observe network traffic → build entity picture → detect (behavioral/signature/intel mix) → prioritize → investigate with evidence → act. They differ in detection philosophy (per-org learning vs curated content vs open-source collections), response posture (autonomous vs analyst-click vs integration-mediated), telemetry depth (packet vs flow), and console deployment (self-managed vs SaaS).

---

## Canonical Abstraction

### Level 0 — Defining Invariant

Four jointly-held structures; removing any one breaks the Type:

1. **Network-observed telemetry as the primary evidence source.** The system watches the organization's network — traffic captured from network vantage points (taps/SPAN/port mirrors, cloud packet mirrors, flow-record exports) — rather than relying primarily on endpoint agents or arbitrary log aggregation. The network is the sensor plane. (Remove → EDR / SIEM / log analytics.)
2. **Continuous threat-oriented analysis of that traffic producing security detections.** The system itself analyzes observed traffic/flows for malicious or suspicious behavior — however implemented (signatures, behavioral baselines, ML, threat-intel matching) — and emits detections as named, persisted security findings. Threat orientation is what separates from Network Monitoring; self-analysis is what separates from a packet recorder. (Remove threat orientation → Network Monitoring/NPM; remove detection → capture/forensics storage.)
3. **Entity-anchored investigation of detections.** Detections surface in an analyst-facing console tied to the involved entities (devices/hosts, identities/users, external endpoints) with supporting network evidence (timeline, related activity, records/packets), so an analyst can validate, contextualize, and group detections into an attack picture. (Remove → bare IDS sensor emitting alerts.)
4. **A response loop operated through the platform.** The product's job does not end at the alert: detections are worked toward action — analyst-triggered containment (e.g., host isolation, firewall policy change), integration-mediated actions in connected tools (EDR containment, firewalls, SOAR), or autonomous response — with the platform supplying the evidence and workflow for that action. (Remove → NTA / classic NIDS; the market's own NDR-vs-NTA articulation marks response as the differentiating "R".)

Jointly-held load-bearing analysis:
- 1 without 2 = traffic/packet analytics or capture store (forensics storage, NPMD-class telemetry).
- 2 without 1 = log/endpoint detection machinery (EDR/SIEM rule packs).
- 1+2 without 3 = classic IDS / NTA alert generator (syslog out, no investigation surface).
- 1+2+3 without 4 = NTA / detection-only network analytics — the historical NIDS posture that the NDR label was coined to differentiate from.
- 3+4 without 1+2 = generic alert triage/IR workflow tool.

### Level 1 — Common Mature Structure (standard capabilities, not definitional)

- **Sensor fleet architecture**: physical/virtual/software/cloud sensors + central console; multi-site; fleet management.
- **Entity/asset inventory built from observed traffic**: automatic device discovery, classification/roles, high-value designation, identity attribution (usernames observed in protocols), including unmanaged/IoT/OT devices that cannot host agents.
- **Multiple detection engines in one product**: signature/IDS rules, behavioral baselines, ML anomaly models, threat-intel matching (STIX/TAXII or curated feeds), custom/user-defined detections.
- **Prioritization machinery**: risk scoring, triage recommendations, recommended investigations/attack-story correlation.
- **MITRE ATT&CK mapping** of detections/coverage.
- **Detection lifecycle management**: statuses (open/acknowledged/in-progress/closed-class), assignment, notes, tuning/suppression rules, notification rules, external ticket references.
- **Retained network evidence for forensics**: packet capture stores, structured records, traffic metadata lookback; packet viewer/export.
- **East-west + north-south coverage**, remote-user and cloud segment coverage.
- **Encrypted traffic analysis**: metadata/behavioral analysis without decryption; optional decryption where legal/technically configured.
- **Ecosystem integrations**: SIEM (feed detections/evidence), EDR (correlate + trigger containment), SOAR, firewalls, IdPs, ticketing.
- **API access** for automation.

### Level 2 — Variant / Optional Structure

- Telemetry depth: full-packet/wire-data-centric vs flow-only deployments (cloud VPC flow logs where mirroring is impossible).
- Console deployment: self-managed on-prem vs SaaS vs hybrid; where detection analytics run (sensor-local vs cloud).
- Detection philosophy: per-organization self-learning models vs vendor-curated global detection content vs open/open-core detection collections.
- Response posture: autonomous AI response vs analyst one-click containment vs purely integration-mediated.
- AI involvement: AI analyst/agentic triage layers vs classic rule+ML only.
- Domain extensions: OT/ICS protocol visibility, identity threat detection, cloud-native/agentless posture, exposure/posture management modules.
- Service wrapper: standalone product vs bundled MDR/MSSP operation.
- Platform embedding: NDR as licensed module of a broader network-observability or security platform.

### Level 3 — Vendor-specific (research notes only)

- Darktrace: Cyber AI Analyst (hypothesis-forming autonomous investigations), Threat Visualizer, "Self-Learning AI trained in-environment" positioning, Antigena-lineage autonomous response.
- Vectra: "Attack Signal Intelligence," entity discovery of "AI agents," security-event-horizon marketing frame, docs.fusion.vectra.ai for the newest cloud offering.
- ExtraHop: RevealX 360 vs Enterprise split; EDA packet sensors, ETA packetstores, EXA recordstores, ECA consoles; Triggers (JavaScript-based custom metric/record extraction); Smart Triage factor rate limits; risk-score color bands (80–99/31–79/1–30); 30-day metric lookback; username-bearing protocol list (FTP, Kerberos, LDAP, NTLM, RDP, RPC, SMB); decrypted payload never written to disk; CrowdStrike containment integration.
- Corelight: Zeek/Suricata open-core; AP-series sensor throughput ladder (4–125+ Gbps); Detection Collections names (C2, Core, Encrypted Traffic, Entity, ICS/OT, Analyzers); Investigator agentic triage cadence (24-hour cycles over 7 days of host activity — product-specific); Smart PCAP; Fleet Manager.

## Rejected Findings (candidate invariants rejected as overfit)

- **"ML/AI-based detection" as definitional** — REJECTED. IDS signatures are equally first-class in the sample (ExtraHop IDS module, Corelight Suricata); signature-based detection is 20+ years old and remains a live engine in mature products. Detection *machinery* is variant; threat-oriented detection itself is the invariant.
- **"Packet capture as the telemetry substrate"** — REJECTED. Flow-only realizations exist and are first-class (ExtraHop NetFlow/VPC flow sensors; Corelight Flow Log Sensors explicitly "where packet mirroring isn't available"). The invariant is network-observed telemetry, not packets per se.
- **"Autonomous AI response" as definitional** — REJECTED. Only some products respond autonomously; ExtraHop's documented response is integration-mediated. The invariant is that response is in the product's scope, not who pulls the trigger.
- **"Passive packet sensors as appliances"** — REJECTED as implementation. The out-of-band observation *posture* is the durable property (inline enforcement is a different Type); the appliance form is not.
- **"SaaS console"** — REJECTED. Self-managed and SaaS consoles coexist across the sample (ExtraHop ships both as separate solutions).
- **"Cloud-first / agentless"** — REJECTED (era machinery). Classic sensor deployments satisfy the Type fully.
- **"Per-organization behavioral learning" (Darktrace's philosophy)** — REJECTED as definitional; globally-curated detection content (Corelight collections, ExtraHop cloud-updated catalog) is an equally dominant philosophy.
- **"NDR = NPM + security"** — REJECTED; ExtraHop's module split shows the two can share one telemetry plane but are licensed, permissioned, and conceptualized as distinct modules. See Boundary Findings.

## Historical / Market-Sample Check

- Would older/regional/platform-native products fit the four-leg core?
  - **Classic NIDS/NSM stacks** (Snort/Bro-heritage sensor + alert console + packet evidence, e.g. Security Onion-style NSM): satisfies legs 1–3 fully; satisfies leg 4 at the "analyst works detections toward action, platform supplies evidence/workflow" level (case workflows, response via connected controls). Fits.
  - **2000s flow-based behavioral analysis (NBAD lineage)**: observes flow telemetry, behavioral detection, investigation consoles; response via analysts/connected tools. Fits legs 1–4 with flow telemetry — confirming "packets" must not be in the core.
  - **Inline IPS/NGFW**: fails leg 1 (in-path enforcement point, not out-of-band observer) — correctly excluded, it is a different Type.
  - **Endpoint agents with network inspection**: fails leg 1 (endpoint-derived telemetry) — EDR.
  - The **"NDR" label itself** is a 2018–2020 market naming (evolved from NTA/NBAD/IDS lineage); the naming event institutionalized the response+investigation legs on top of the older detection-only stack. This is consistent with leg 4 being category-defining for NDR *as a named Type* rather than overfit to one era: the response loop predates AI (analyst-led) and survives across eras.
- The definition names no ML, cloud, SaaS, AI analyst, or vendor-specific detection branding; signatur­es, ML, and behavioral analytics are all realized variants. Check passes.

---

## Boundary Findings

| Neighboring Type | Relationship | Distinction ("remove what → becomes the other") |
|---|---|---|
| Endpoint Detection & Response / EDR | complementary sibling | Evidence source: EDR runs agents on endpoints; NDR observes the network from network vantage points. Vendors articulate it themselves (SOC Visibility Triad; "NDR fills gaps left by EDR… devices that can't host agents"). Remove network observation → EDR; the response-loop shape is shared. |
| SIEM | aggregator vs generator | SIEM ingests and correlates logs from many sources and is the retention/correlation backbone; NDR generates its own detections from its own network-derived telemetry and feeds the SIEM. Remove own network analysis → a SIEM data source. |
| Network Monitoring (directory leaf) | same plane, different question | Both observe traffic and can share sensor infrastructure (ExtraHop: NDR vs NPM modules on one platform with RBAC). The question differs: performance/availability (is it slow/down?) vs security threat (is it compromised/attacking?). Remove threat orientation and detections → Network Monitoring; the performance-category detections in ExtraHop sit in the NPM module, not NDR. |
| Network Security Platform / NGFW / IPS | enforcement vs observation | Inline policy enforcement and blocking in the traffic path vs out-of-band observation and detection; NDR may *trigger* firewall/EDR actions but does not stand in the path by default. Make it inline → different Type. |
| XDR | specialist vs cross-domain correlator | XDR correlates across endpoint/network/identity/cloud domains (often within one vendor suite); NDR is the network-domain specialist whose high-fidelity detections feed XDR/SIEM. Corelight's own glossary frames NDR as one pillar of the (extended) visibility triad. |
| Deception Platform | adds decoys vs observes reality | Deception plants fake assets and detects interactions with them; NDR observes real traffic. Deception output can be consumed by NDR-class consoles but the mechanisms differ. |
| Threat Hunting Platform | activity vs standing system | Hunting is analyst activity over retained evidence; NDR products support hunting (Corelight explicitly lists threat hunting among its capabilities) but the standing defining loop of the NDR Type is continuous detection→response, not hypothesis-driven hunting campaigns. Directory has a separate Threat Hunting Platform leaf; hunting inside NDR = standard capability, not boundary violation. |
| Cyber Asset Management | byproduct vs purpose | NDR builds an entity/asset inventory from traffic as a *byproduct* enabling detection and investigation; asset management products make the inventory the managed record. Make inventory the center → different Type. |
| NTA / NBAD / IDS (historical labels, not directory leaves) | predecessor labels | Detection-only network analytics without the platform-level investigation/response loop. The market's own NDR-vs-NTA articulation (vendor FAQ, Layer A) marks response as the differentiator. |

No taxonomy conflict found: the leaf is a coherent, independently recognized Type (multiple analysts' categories named "Network Detection and Response" verbatim; vendor pages self-identify with the label).

## Uncertainties

1. **Darktrace operational depth** — help center not fetched; sensor deployment shapes, console structure, and retention specifics unverified. All Darktrace response claims are at product-page depth; treat specific autonomous-response actions (isolate/re-auth/block IP) as vendor-stated, not independently verified.
2. **Vectra operational depth** — docs.fusion.vectra.ai not fetched; console/detection-lifecycle specifics unverified. The "agentless / no infrastructure" deployment claim coexists with the classic sensor-based product; posture mixing recorded, not resolved.
3. **Cisco Secure Network Analytics** (flow-based pole) — 403 on fetch; not researched first-hand. Flow-telemetry findings rest on ExtraHop/Corelight flow-sensor documentation instead.
4. **Response depth of ExtraHop beyond integrations** — only CrowdStrike/Entra-ID/Okta response actions were documented; broader native response (if any) unverified.
5. **Retention norms** — "months vs years" lookback claims are vendor-stated (Corelight product pages/glossary); no cross-product numeric norm asserted.
6. **Historical NIDS/NBAD/NTA lineage** — treated conceptually; no historical source fetched directly (per source-access rules, kept at conceptual strength).

## Final Synthesis

A Network Detection & Response application is the security team's network-side threat detection system: it continuously observes the organization's network from network vantage points (taps/SPAN/cloud mirrors/flow exports) — not from endpoint agents — builds a live entity picture of devices, users, and external endpoints from that observation, and runs detection machinery (signature, behavioral, ML, threat-intelligence) over the observed traffic to generate security detections. Detections are surfaced in an analyst console anchored to the involved entities with retained network evidence, managed through a triage lifecycle, and operated toward response — analyst-triggered containment, integration-mediated actions in EDR/firewall/SOAR tools, or autonomous response. Packet depth, flow depth, AI machinery, SaaS consoles, autonomous response, per-org learning vs curated content, OT/identity/cloud extensions, and MDR wrappers are all variant realizations. The Type is separated from Network Monitoring by threat orientation, from EDR by the evidence plane, from SIEM by self-generated network detections, and from inline security platforms by its out-of-band observation posture.
