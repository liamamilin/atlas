# Research Notes — Network Monitoring

## Research Goal

Understand what "Network Monitoring" is as an Application Type in the enterprise/campus/datacenter IT sense: what objects it watches (devices? links? traffic? paths?), how measurement enters the system, what it produces (states, alerts, views), who operates it, and where its boundaries sit against the processed siblings Network Management, Network Detection & Response, Infrastructure Monitoring, Metrics Monitoring, DDoS Protection Platform, Digital Experience Monitoring, and ITOM — plus the unprocessed Synthetic Monitoring and Observability Platform.

## Initial Boundary

Working hypothesis before research: Network Monitoring is the network team's read-path observation system — it watches the organization's network (devices, the links between them, and the traffic crossing them) for availability and performance, and turns measurements into health states and alerts. It is NOT:

- Network Management (write path: configuration/firmware/provisioning) — seam pre-hung by the network-management pass at write-vs-read
- NDR (security question asked of the traffic) — seam pre-hung by the NDR pass at the question asked + detection object class
- Infrastructure Monitoring (whole-estate entity conditions; network devices are one entity class there) — seam pre-hung by the infrastructure-monitoring pass at primary measured object
- Metrics Monitoring (subject-agnostic numeric series) — seam pre-hung by the metrics-monitoring pass at primary measured object
- DDoS Protection (executes traffic countermeasures) — ratified by the ddos pass
- DEM (experienced service quality from consumption points) — ratified by the DEM pass

## Research Questions

1. What objects exist inside a network monitoring product? Are interfaces/links first-class monitored units, or only devices?
2. What data does it collect and how (SNMP, ICMP, flow exports, packet capture, active probes, controller APIs, agent-based connection data)?
3. What does it produce — health states, alerts, topology, path views, reports? What is the state model?
4. How does alerting work (thresholds, baselines, dependencies, acknowledgment)?
5. Who uses it, in what operating context (NOC, network team, MSP)?
6. What are the variant poles (on-prem poller vs SaaS; device-centric vs flow-centric; standalone vs suite module)?
7. Where exactly are the seams with each processed sibling, and what must be ratified with unprocessed ones?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

1. **SolarWinds Network Performance Monitor (NPM)** — classic enterprise on-prem SNMP poller; Orion module; counterparty evidence from the network-management pass (NPM vs NCM separately licensed).
2. **PRTG Network Monitor (Paessler)** — sensor-philosophy monitor, mid-market, self-hosted + hosted variants; full Tier-1 manual.
3. **ManageEngine OpManager** — device-centric enterprise network monitor; counterparty evidence from the network-management pass (OpManager vs NCM separately sold); full Tier-1 FAQ.
4. **Datadog Network Monitoring** — cloud SaaS, flow-centric, inside an observability platform; full Tier-1 docs (CNM / NDM / NetFlow / Network Path).

## Sources

All fetched 2026-09-09:

- SolarWinds — Network Performance Monitor product page + FAQ: https://www.solarwinds.com/network-performance-monitor (Tier 2; admin-guide URL 404'd once, product page used instead)
- PRTG — Manual: Object Hierarchy (https://www.paessler.com/manuals/prtg/object_hierarchy), Sensor States (https://www.paessler.com/manuals/prtg/sensor_states), full TOC (https://www.paessler.com/manuals/prtg) (Tier 1)
- ManageEngine — OpManager FAQ (https://www.manageengine.com/network-monitoring/faq.html), Help landing (https://www.manageengine.com/products/opmanager/help/) (Tier 1 FAQ + Tier 2 landing)
- Datadog — Network Monitoring section index (https://docs.datadoghq.com/network_monitoring/), Cloud Network Monitoring (…/cloud_network_monitoring.md), Network Device Monitoring (…/devices.md), NetFlow Monitoring (…/netflow.md) (Tier 1)

Cross-referenced processed passes (no new fetch): network-management, network-detection-response-ndr, infrastructure-monitoring, metrics-monitoring, ddos-protection-platform, digital-experience-monitoring, it-operations-management-itom, ip-address-management-ipam, dns-dhcp-management.

## Product A — SolarWinds NPM (evidence layer A)

Key observations:

- Vendor's own definition of the practice: "Network performance monitoring is the practice of tracking availability, traffic, and device health so you can detect and resolve issues affecting network performance." FAQ: "tracking the availability, health, and performance of network devices, interfaces, and paths so you can identify and resolve issues that affect connectivity and user experience."
- Watched objects: routers, switches, firewalls, wireless controllers, wireless access points and clients — and **interfaces** and **paths** as named objects ("devices, interfaces, and paths").
- Metrics collected: device and interface availability, response time, packet loss, bandwidth utilization, errors and discards, hardware health (CPU, memory, temperature, fan speed).
- Collection: "industry-standard protocols to poll network devices" (SNMP named in discovery context); continuous polling; historical data stored.
- Discovery: finds SNMP-enabled devices; builds topology views showing how devices and interfaces relate, including high-traffic links and potential single points of failure.
- Path measurement: NetPath — hop-by-hop path visualization across on-premises, service-provider, and cloud segments; latency and packet loss at each hop.
- Correlation surface: PerfStack — drag-and-drop network, system, and application metrics onto a single timeline (works across Orion modules).
- Alerting: pre-built alert templates + customizable thresholds; historical baselines ("what normal looks like"); **dependency-aware alerting** — suppress alerts for downstream devices when an upstream dependency is unavailable.
- Wireless: controllers, APs, clients, Wi-Fi heat maps (Cisco APs named).
- Capacity forecasting reports (saturated links, upgrade planning).
- Suite architecture: NPM is an Orion module; Network Configuration Manager (write path), NetFlow Traffic Analyzer (flows), IP Address Manager are separate products — the market's own product split documents the seams.

## Product B — PRTG (evidence layer A)

Key observations:

- Object model (manual, Tier 1): tree hierarchy **Root Group → Probe → Group → Device → Sensor**, with inheritance of settings down the tree.
- Device = "real hardware or a virtual device in your network… routers or network switches… almost every device in your network that has its own IP address."
- Sensor = "monitors one single aspect of a device" — e.g. a network service (SMTP/FTP/HTTP), the traffic on a network switch. The sensor is the unit that carries state, channels (metric series), and notification triggers.
- Probes: local probe (with core), remote probes (outside the network), cluster probe ("data from different perspectives") — multi-vantage-point collection is structural.
- Sensor states (Tier 1): **Down, Down (Partial), Down (Acknowledged), Warning, Unusual, Up, Paused, Unknown** — with priority rollup: a device/group/map shows the highest-priority state of its sensors.
  - Warning = transient (sensor retrying; may become Down) or warning limit/lookup.
  - **Unusual = baseline anomaly**: "reports unusual values for this weekday and this time of the day… based on the sensor's historic average data" (configurable/disableable).
  - Paused = by time span, indefinitely, or **because of a dependency** (downstream objects pause when the parent is down).
  - Down (Acknowledged) = user acknowledged; no further notifications.
  - Down behavior: sensor either stops recording channels, or continues recording when Down comes from an error limit/lookup.
- Network-relevant sensor types: Ping, Ping Jitter, QoS One Way / Round Trip, SNMP Traffic, SNMP Trap Receiver, NetFlow v5/v9, sFlow, IPFIX, jFlow, Packet Sniffer, Traceroute Hop Count, Cisco IP SLA, Syslog Receiver, Port, DNS, DHCP — alongside many non-network sensors (WMI, VMware, AWS, …). PRTG is a general infrastructure monitor whose heritage and headline use case is network monitoring.
- Setup machinery: auto-discovery, device templates, recommended sensors.
- Surfaces: device tree, maps, geo maps, libraries, reports, toplists, alarms, logs; access rights management.
- Deployment variants: PRTG Network Monitor (self-hosted), PRTG Hosted Monitor, PRTG Enterprise Monitor.

## Product C — ManageEngine OpManager (evidence layer A)

Key observations:

- Positioning (FAQ): "comprehensive network monitoring tool designed to help IT admins gain real-time insights into the performance of devices like routers, switches, servers, firewalls, and VMs."
- Collection (FAQ): agent-less, using "ICMP, SNMP, WMI, CLI (Telnet/SSH), TFTP, SCP"; includes "Syslog daemon, SNMP Trap listener and Flow collectors for NetFlow, sFlow."
- Licensing unit = the device ("any device that responds to an ICMP ping"); scale unit = the **interface** ("polling engine can monitor up to 10,000 Interfaces" — product-specific number, research notes only).
- Discovery: scheduled discovery, auto VM discovery, discover-via-trap, discovery rule engine; device templates + device categories (Servers, Routers, Switches, Firewall, Wireless); devices categorized "Unknown" when credentials fail or no template matches.
- **Interface status polling**: "polls interfaces at regular intervals to check their status using SNMP. It monitors both administrative and operational statuses, based on which it raises alerts in case of any anomaly."
- **Interface thresholds**: per-interface severity tiers (attention/trouble/critical) for **Utilization, Error Rate, Discard Rate**.
- Availability check method: ICMP by default; switchable to TCP or SNMP per device (ICMP blocked → false "down" — a documented operational rule).
- Layer 2 discovery: Bridge MIB, ARP, routing tables, CDP/LLDP, IF-MIB → Layer 2 network maps; auto-assigned uplink **dependencies** between devices (disableable).
- Architecture: Central–Probe for distributed networks (Enterprise Edition); MSP edition for multi-client operations.
- Add-ons separately licensed: Network Configuration Manager, Firewall Log Analysis, NetFlow/Flow Analysis, IPAM, Switch Port Management, APM plugin, Storage Monitoring, Access Point Monitoring, IP SLA Monitoring, URL Monitoring — the suite split again documents the seams.
- Surfaces: dashboards, NOC/CCTV views, business views, device snapshot pages, interface graphs, reports; REST API.

## Product D — Datadog Network Monitoring (evidence layer A)

Key observations:

- Product section = four named areas: **Cloud Network Monitoring (CNM)**, **DNS Monitoring**, **Network Device Monitoring (NDM)**, **NetFlow Monitoring**, plus **Network Path**.
- CNM: "visibility into your network traffic between services, containers, availability zones, and any other tag… Connection data at the IP, port, and PID levels is aggregated into application-layer dependencies between meaningful client and server endpoints" — analyzed via a network page and network map; network health; network analytics; monitors. Collection is Agent-based (connection data), NOT SNMP — proof that SNMP is not the invariant.
- NDM: "visibility into your on-premises and virtual network devices, such as routers, switches, and firewalls. Automatically discover devices… collecting metrics like bandwidth utilization, volume of bytes sent, and determine whether devices are up or down." Summary page = "health of your network at a glance"; SNMP metrics; device profiles; device health (correlates issues with configuration changes); device maps ("physical and geographical connections").
- NetFlow: flows collected from devices exporting flow data (routers, firewalls, switches); views: Traffic Volume, Device Health, Flows, Conversations, Autonomous Systems, Geo IP, Source/Destination Ports, Protocols, Flags. Flow record fields: direction, start/end time, ether type, flow type, IP protocol, next hop IP, TCP flags, bytes, packets, ingress/egress interface (alias/index/name); device fields (device IP, exporter IP, model, name, namespace, vendor). Enrichment: cloud provider service/region, IANA port names, custom port/IP mappings, reverse DNS. Conversation stitching (A→B + B→A into A↔B). NetFlow monitors. Retention options and per-flush volume caps are product-specific (research notes only).
- Network Path: scheduled tests + dynamic tests; "hop-by-hop route and latency context"; dynamic tests can auto-target destinations observed in NetFlow records.
- DNS Monitoring: "diagnose and debug DNS server issues."

## Cross-product Comparison

| Dimension | SolarWinds NPM | PRTG | OpManager | Datadog |
|---|---|---|---|---|
| Unit of record | device + interface + path | device → sensor (per aspect) | device + interface | device + interface (NDM); flow/conversation between tagged endpoints (CNM) |
| Watched population | network devices, interfaces, paths | any IP-addressable device, sensor per aspect | routers/switches/firewalls/servers/VMs + interfaces | network devices + interfaces; service-to-service traffic |
| Collection | SNMP/ICMP polling | sensors over SNMP/ICMP/flow/packet/probe; local+remote+cluster probes | agent-less ICMP/SNMP/WMI/CLI + trap listener + syslog + flow collectors | SNMP (NDM); Agent-based connection data (CNM); flow listeners |
| Availability semantics | device/interface availability, response time, packet loss | sensor states with rollup (Up/Warning/Unusual/Down/…) | device availability (ICMP/TCP/SNMP) + interface admin/oper status | device up/down |
| Performance semantics | utilization, errors/discards, latency, loss | channel limits, QoS sensors, Unusual baseline | utilization/error/discard rate thresholds with severities | bandwidth utilization, bytes, flow volumes |
| Traffic/flow plane | NTA sibling product + NetPath | NetFlow/sFlow/IPFIX/jFlow/packet-sniffer sensors | NetFlow Analyzer add-on | NetFlow + CNM core |
| Path/latency plane | NetPath hop-by-hop | QoS one-way/round-trip, traceroute-hop sensors, Cisco IP SLA | IP SLA add-on | Network Path scheduled/dynamic tests |
| Topology | topology maps (devices+interfaces, single points of failure) | geo maps + dependency tree (no auto L2 map in core) | L2 maps via CDP/LLDP/Bridge MIB + auto uplink dependencies | device maps (physical/geographical) |
| Evaluation → output | thresholds + baselines → alerts; dependency-aware suppression | state machine + notification triggers; acknowledgment | threshold severities → alerts; notification profiles | monitors → alerts |
| Deployment | on-prem (Orion) | self-hosted / hosted | on-prem, central-probe | SaaS |
| Packaging | Orion module; NCM/NTA/IPAM siblings | standalone (+Enterprise/Hosted) | standalone + separately-licensed add-ons | observability-platform module |
| Customer tier | enterprise/mid-market | mid-market/small–large | enterprise/mid-market/MSP | cloud-native enterprise |

Cross-product commonalities (evidence layer B): the device+interface watched population; continuous polling/collection retained as history; availability + utilization/error evaluation; health states with alerting/notification; discovery; dashboards/maps/reports; multi-protocol collection mix; dependency-aware noise control (3 of 4 explicit); flow analysis (all four, but as add-on/sensor/area — not the core in the classic pollers); latency/loss probing (3 of 4 as named capability); wireless (3 of 4).

## Canonical Model

### L0 — Defining Invariant (three jointly-held structures)

1. **The network estate under watch** — persistent, individually identified records of the network infrastructure being watched: network devices (routers, switches, firewalls, wireless controllers/APs) **and their interfaces/links as first-class monitored units alongside the devices**. The interface/link — not only the device — is a unit that carries measurement, state, and alerts. (Remove → asset inventory/CMDB [records without measurement]; or Infrastructure Monitoring, where the entity is the unit and the link/flow/path is not first-class.)
2. **Continuous network measurement** — repeated collection of availability and performance observations from the network's planes: device reachability/health and interface/link counters (traffic, errors, discards) at the core, commonly extended with traffic-flow records and latency/loss probes; retained as history. (Remove → static inventory.)
3. **Evaluation → network health states and alerts** — measurements continuously evaluated against thresholds/baselines/status semantics, producing user-visible per-object health states (up/down, degraded, saturated) with alerting/notification as the standard output. (Remove → telemetry pipeline or graphing archive; the "monitoring" is gone.)

Jointly-held is load-bearing: 1 alone = device inventory/CMDB; 2 without 1 = generic series collection (Metrics Monitoring); 3 without 1+2 = rules engine; 1+2 without 3 = data logging/graphing archive; 2+3 without 1 = generic metric alerting with no estate; 1+3 without 2 = stateless pinger.

The question asked is availability/performance ("is it up, is it slow, where is the congestion/loss") — not threat (NDR), not configuration change (Network Management), not whole-estate resource conditions (Infrastructure Monitoring), not user-experienced quality (DEM).

### L1 — Common Mature Structure (standard, not definitional)

- discovery/auto-discovery of devices (4/4)
- device and interface detail views with metric graphs/history (4/4)
- alerting with thresholds, severities, notification routing, acknowledgment (4/4)
- dashboards/maps/reports (4/4)
- multi-protocol collection mix (SNMP + ICMP + others) (4/4)
- dependency-aware alerting / downstream suppression (3/4 explicit)
- traffic-flow analysis (NetFlow/sFlow/IPFIX) (4/4, but as add-on/sensor/area in classic pollers)
- latency/loss/path measurement (3/4 as named capability)
- topology / L2 maps (3/4; PRTG has dependency tree + geo maps instead)
- wireless controller/AP/client monitoring (3/4)
- hardware health metrics (CPU/memory/temperature/fan) (3/4)
- baseline anomaly detection (SolarWinds baselines, PRTG Unusual, Datadog monitors)
- SNMP trap / syslog reception (2/4 explicit, common in class)
- multi-vantage-point collection (probes/agents) (3/4)
- RBAC, APIs, config-change correlation (Datadog NDM), capacity forecasting (SolarWinds)

### L2 — Variant / Optional Structure

- deployment: on-prem server/appliance vs SaaS vs hosted
- philosophy poles: device-poller (SolarWinds/OpManager) vs sensor-tree (PRTG) vs flow-first SaaS (Datadog)
- packaging: standalone product vs network-management-suite module vs observability-platform pillar
- scope specializations: wireless, SD-WAN, cloud/VPC flows, OT networks
- MSP/multi-tenant delivery
- licensing: per-device / per-interface / per-sensor / flow-volume
- agent-less vs agent-assisted collection

### L3 — Vendor-specific (research notes only)

- PRTG's exact sensor-state list and rollup priorities; sensor-based licensing
- OpManager device-template/vendor-template counts; port lists; Central–Probe edition split; add-on catalog
- Datadog NetFlow retention options, aggregation interval defaults, facet lists, truncation metrics
- SolarWinds NetPath/PerfStack branding; Orion module architecture

## Historical / Market-Sample Check

- **MRTG (late 1990s)**: scheduled SNMP polling of router interface counters → per-target traffic graphs → built-in threshold checking with break/recovery programs, mail notification, hysteresis. Satisfies all three L0 legs with no topology, no flows, no SaaS, no AI. Direct evidence for MRTG's structure was documented in the metrics-monitoring pass; MRTG is a **shared ancestor** of both Types (it polled network devices), consistent with the ratified seam that network measurements land in metrics monitoring as ordinary series.
- **Classic SNMP NMS platforms (HP OpenView-era)**: device polling + MIB-II interface counters + trap reception + threshold alarms — satisfies conceptually (layer C).
- **SNMP is a common transport, NOT the invariant**: Datadog CNM collects connection data from agents (no SNMP); wireless controllers are monitored via vendor APIs; PRTG/OpManager mix ICMP/WMI/CLI/flow. The definition names no protocol.
- **Device-level network monitoring also satisfies Infrastructure Monitoring's core** (their pass recorded this) — the Types share the evaluation loop; the separation is the watched object plane (below).
- No modern machinery (cloud, SaaS, AI, ML baselines) is required by the core.

## Vendor-specific Findings

- SolarWinds: NetPath (hop-by-hop path visualization incl. ISP/cloud segments), PerfStack (cross-module timeline overlay), Wi-Fi heat maps, capacity forecasting.
- PRTG: sensor as universal unit (one aspect per sensor); Unusual state driven by per-weekday/time-of-day historic averages; Down (Partial) in clusters; probe system (local/remote/cluster).
- OpManager: interface as licensing/scale unit; admin-vs-operational interface status distinction; L2 discovery via CDP/LLDP/Bridge MIB with auto uplink dependencies; availability-check method switchable per device (ICMP/TCP/SNMP).
- Datadog: CNM aggregates connection data to IP/port/PID level into application-layer dependencies between tagged endpoints; conversation stitching; flow enrichment (cloud provider, IANA ports, reverse DNS, custom CSV); dynamic path tests auto-targeting NetFlow destinations.

## Boundary Findings

1. **vs Network Management (§14, processed — ratified from both sides)**: seam = write path vs read path. Network Management applies configuration/firmware/provisioning to the device estate; Network Monitoring measures availability/performance and alerts. Same device population; SolarWinds (NPM vs NCM) and ManageEngine (OpManager vs NCM) sell them as separate products. Monitoring may include limited remediation actions, but the write path is not its center.
2. **vs NDR (§15, processed — ratified)**: seam = the question asked of the traffic + the detection object class. Same sensor plane possible (the NDR pass documented one platform shipping NDR and NPM as separately licensed modules over the same sensors). Performance/availability question + health/alert objects → Network Monitoring; threat question + security findings → NDR.
3. **vs Infrastructure Monitoring (§14, processed — their flag, confirmed here)**: seam = primary measured object. Infrastructure monitoring watches the whole estate (hosts/VMs/containers/devices/cloud) with per-entity resource conditions; network devices are one entity class there. Network monitoring confines the estate to the network and makes the **link/interface/flow/path** first-class with network semantics (utilization, errors/discards, latency, loss). Keep both; the seam is the object plane, not feature presence (Zabbix ships network-device templates; Datadog ships NDM inside its platform — feature presence proves nothing).
4. **vs Metrics Monitoring (§14, processed — their flag, confirmed here)**: seam = primary measured object. Metrics monitoring is subject-agnostic over identified numeric series; network measurements (interface counters, latency) land there as ordinary series. Narrow the watched series to network devices/links/traffic with network semantics and an estate frame → Network Monitoring.
5. **vs DDoS Protection Platform (§14, processed — ratified)**: monitoring observes, baselines, alerts; it never executes traffic countermeasures. The moment the product drops/scrubs/rate-limits/diverts attack traffic → DDoS Protection.
6. **vs Digital Experience Monitoring (§14, processed — ratified)**: network monitoring's objects are devices/links/health; DEM's object is experienced service quality from consumption points. Network data enters DEM as an attribution layer (path visualization, ISP breakdowns).
7. **vs ITOM (§14, processed — ratified)**: single-domain observation vs estate-wide operations layer with response loop.
8. **vs IPAM / DNS & DHCP Management (§14, processed — ratified)**: address/name/lease records vs live health/performance observation.
9. **vs Synthetic Monitoring (§14, unprocessed — FLAG for that pass)**: network monitoring uses active probes (ping/QoS/traceroute) as one collection method among several, with the network as the object; synthetic monitoring's center of gravity is probe machinery simulating user interactions against user-facing services. The object differs, not the probe technique. To be ratified on that side.
10. **vs Observability Platform (§14, unprocessed — FLAG for that pass)**: observability platforms bundle network monitoring as a pillar (Datadog ships Network Monitoring inside its platform), but the classic poles (SolarWinds NPM, PRTG, OpManager) exist fully standalone — pillar packaging is a variant, not a boundary failure.
11. **vs Server Management Platform (§14, unprocessed — echo of the network-management pass's flag)**: estate-subject seam — network infrastructure devices vs servers/endpoints; RMM-class tools manage both.
12. **"Remove what and it becomes another Type"**: remove the link/interface/flow/path plane and widen the estate → Infrastructure Monitoring; remove the estate frame and keep series → Metrics Monitoring; remove the read path and add the write path → Network Management; change the question to threat → NDR; add enforcement → DDoS Protection; re-anchor on experienced quality → DEM.

## Uncertainties

- Cloud-native network telemetry depth (VPC flow logs, cloud-provider reachability analysis) — evidenced only through Datadog CNM; other cloud-native poles not sampled; held as variant.
- Wireless-controller-native poles (Cisco Catalyst Center, Aruba Central, Juniper Mist) — unreachable in the network-management pass (403/404/transport) and not retried here; wireless monitoring evidenced via SolarWinds/PRTG/OpManager sensor and feature names only.
- Whether hop-by-hop path measurement is becoming definitional — currently common-not-universal (absent as a first-class path object in PRTG's core; present as sensors). Held at L1.
- OT-network monitoring convergence — PRTG markets OT monitoring; not researched deeply; held as variant.
- PRTG's exact positioning (general infrastructure monitor with network heritage vs pure network monitor) — resolved as: the Type is defined by the watched object plane, and PRTG's network sensor set + heritage satisfy it; its broader estate coverage is suite overlap, the same pattern the infrastructure pass recorded for Zabbix.

## Final Synthesis

A Network Monitoring application is the network team's read-path observation system: it holds the network estate under watch — devices and their interfaces/links as first-class monitored units — continuously measures availability and performance from the network's planes (device reachability, interface counters, commonly flows and latency/loss probes), and evaluates those measurements into per-object health states and alerts. Around that core, mature products add discovery, topology/L2 maps, flow analysis, path/latency probing, wireless monitoring, hardware health, baseline anomaly detection, dependency-aware alerting, dashboards/reports, and multi-vantage-point collection. The Type is realized in three poles — the classic on-prem SNMP poller, the sensor-tree general monitor with network heritage, and the flow-first cloud SaaS — plus suite-module and observability-platform-pillar packaging. Its boundaries are held at: the write path (Network Management), the question asked of traffic (NDR), the object plane (Infrastructure Monitoring, Metrics Monitoring), enforcement (DDoS), and the experience anchor (DEM); two flags stand for the unprocessed Synthetic Monitoring and Observability Platform passes.
