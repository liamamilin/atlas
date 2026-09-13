# Research Notes — SCADA (Supervisory Control and Data Acquisition)

Research date: 2026-09-09
Slug: `scada` (DIRECTORY §16 Engineering, Manufacturing & Industrial)

Evidence layers used below: **[A]** = directly observed on an official source for a named product this pass; **[B]** = cross-product commonality across the sampled set (this pass + sibling-pass records); **[C]** = canonical inference from cross-product comparison and Type-boundary reasoning.

---

## Research Goal

Understand what SCADA really is as an Application Type: the defining structure that makes a product this Type (vs HMI, DCS, historian, IIoT platform, ADMS/EMS), the objects it holds (field units, points, alarms, commands), how the supervisory loop works, who operates it, and — critically — to discharge the open HMI↔SCADA joint-review flag and to position the Type against the grid-operations umbrella document that recorded SCADA as its "substrate member".

## Joint-review obligations carried into this pass

1. **hmi (§16, processed 2026-09-08)** — FORWARD FLAG for this leaf: "the market straddles the seam hard — one sampled platform self-labels both 'HMI software' and 'SCADA software' on one product; another vendor keeps its HMI line and SCADA line as separate products; every SCADA deployment contains operator HMI surfaces, so the operator-screen core cannot be the discriminator. Proposed discriminator: HMI = the operator-interface layer for a machine or local process; SCADA = the multi-site supervisory system. Joint review required when scada is processed — that pass should ratify or sharpen the seam and define its Type so that it contains (not competes with) this one." → Discharged below (Boundary Findings #1).
2. **grid-operations-platform (§19, processed 2026-09-08)** — counterparty: "unprocessed member leaves (scada, distribution-management-system-dms, outage-management-system-oms) should treat this document as counterparty." The umbrella document records SCADA as the substrate member ("Point-based telemetry/alarm/control. The umbrella's estate always contains it; removing the network model + analysis + domain applications leaves SCADA."). → Consistency check below.
3. **advanced-distribution-management-system-adms (§19, processed 2026-09-06)** — "SCADA is the point-based telemetry/control substrate — the connected network model is the ADMS differentiator." → Ratified from this side.
4. **energy-management-system-ems (§19, processed 2026-09-08)** — "SCADA = point-based telemetry, alarming, remote control. Add the maintained network model + network-level analysis + balancing → EMS." → Ratified from this side.
5. **industrial-historian (§16, processed 2026-09-08)** — "SCADA = supervisory control of distributed assets: telemetry, alarming, operator control write-back. Historian = neutral archival infrastructure with no control duty." → Ratified from this side.
6. **industrial-iot-platform (§16, processed 2026-09-08)** — "vs SCADA seam recorded from this side (no live-process supervision/control duty; async operations through agents/gateways)" — that pass explicitly left the HMI↔SCADA joint review open with this pass. → IIoT seam re-affirmed below.
7. **distributed-control-system-dcs (§16, processed 2026-09-07)** — ratified keep-distinct for SCADA/HMI/Historian/PLC-PE/MES; Emerson sells DCS, SIS, PLC, MES, SCADA as separate lines. → Consistent.

## Initial Boundary

Working hypothesis at intake (to be tested, not asserted):

- SCADA = supervisory control and data acquisition: a central supervisory system acquiring telemetry from and issuing control commands to distributed field units (RTUs, PLCs, IEDs) over wide-area communication links, with alarming and operator consoles at the center.
- Nearest neighbors in DIRECTORY.md §16: HMI (previous sibling, open joint review), Industrial Historian, DCS, PLC Programming Environment, Industrial IoT Platform. §19 siblings: EMS, ADMS/DMS, OMS, Grid Operations Platform (umbrella counterparty).
- Known market hazards going in: (a) products self-label "HMI", "SCADA", "HMI/SCADA" interchangeably; (b) the same vendor often sells HMI and SCADA as separate lines; (c) "SCADA" is used both for the classic wide-area utility/pipeline pattern and for plant-floor supervision of many PLCs; (d) large-vendor documentation (Siemens, Schneider, Rockwell, Hitachi) unreachable in prior passes.

## Research Questions

1. What is the defining architecture — what must exist for a system to be SCADA (master station? field units? communication links? points?)?
2. What is the unit of supervised data (point/tag) and how is it organized (points vs network model)?
3. What does "supervisory" control mean operationally — who executes, what is written back, what bounds it?
4. What role do RTUs/PLCs/IEDs play, and is field-side local autonomy part of the structure?
5. What communication machinery is standard (polling, report-by-exception, store-and-forward, redundancy)?
6. What do operators actually do (observe, acknowledge, command), and on what surfaces?
7. Where is the HMI↔SCADA seam, given the market's "HMI/SCADA" bundling — and does the SCADA Type contain the HMI Type?
8. Where are the seams vs DCS, vs ADMS/EMS (network model), vs historian, vs IIoT platform?
9. Would older/regional products (1970s master+RTU systems, regional utility SCADA) still satisfy the definition?

## Representative Products

Selected for market representativeness + documentation completeness + different product philosophies + different customer tiers:

| Product | Vendor | Pole | Customer tier | Evidence reached |
|---|---|---|---|---|
| Ignition | Inductive Automation | independent platform, "HMI/SCADA" straddler, web-deployed, unlimited licensing | integrators/end users, single machine → enterprise; water districts + manufacturing | Tier 2 SCADA page + product page (this pass); Tier 1 user manual (HMI pass, 2026-09-08) |
| AVEVA Plant SCADA (ex-Citect SCADA) | AVEVA | large-vendor industrial SCADA lineage (Citect), plant/infrastructure | plant personnel, mining, tunnels, pipelines | Tier 2 product page |
| SurvalentONE SCADA (+ Optional Applications) | Survalent | utility/multi-utility SCADA specialist, mid-market modular catalog | 700+ electric/water/gas/transit utilities | Tier 2 product page + optional-applications page |
| VTScada | Trihedral | independent all-in-one SCADA platform, water/oil&gas pole, 35-year lineage | municipal utilities, oil & gas, marine, broadcasting | Tier 2 product + licensing pages |
| GE Vernova CIMPLICITY / iFIX / iPower | GE Vernova | automation-vendor "HMI/SCADA" family pole; iPower = utility control-room SCADA | manufacturing plants → utility control rooms | Tier 2 HMI/SCADA extensions page |

Deliberately not sampled after access failure (network-restriction rule; consistent with prior passes): Siemens WinCC/TeleControl (403/404 in prior passes), Schneider EcoStruxure (403), Rockwell FactoryTalk (404), Hitachi Energy (404 across three passes). Their absence is recorded under Uncertainties and lowers claim strength for the PLC-vendor-ecosystem pole only.

## Sources

Fetched 2026-09-09:

- Inductive Automation — Ignition SCADA software page: https://inductiveautomation.com/scada-software
- Inductive Automation — Ignition product page: https://inductiveautomation.com/ignition/
- AVEVA — Plant SCADA product page: https://www.aveva.com/en/products/plant-scada/
- Survalent — SurvalentONE SCADA page: https://www.survalent.com/products/scada/
- Survalent — SurvalentONE SCADA Optional Applications page: https://www.survalent.com/products/survalentone-scada-optional-applications/
- Trihedral — What is VTScada Software: https://www.vtscada.com/what-is-vtscada/
- Trihedral — VTScada Software Licensing: https://www.vtscada.com/software-licensing/
- GE Vernova — CIMPLICITY HMI SCADA Extensions page: https://www.gevernova.com/software/products/hmi-scada/cimplicity (fetched via /software/products/cimplicity/ redirect)

Sibling-pass sources reused as corroboration (not re-fetched): Ignition 8.3 User Manual (HMI pass — Gateway/Designer/Vision/Perspective, tags, alarming state machine, historian, security); SurvalentONE SCADA page + Network Topology Processor page (EMS pass); Oracle Utilities NMS documentation (ADMS pass — Flex SCADA module inside an ADMS); Emerson DeltaV pages (DCS pass — SCADA as a separate product line, "DeltaV SaaS SCADA… scalable IIoT-ready").

Unreachable / limited: inductiveautomation.com/solutions/scada (404 — used /scada-software instead); Siemens/Schneider/Rockwell/Hitachi (per prior passes). No detail filled from memory.

---

## Product Observations

### Product A — Ignition (Inductive Automation)

Key observations (Layer A unless noted):

**Positioning.** "One Industrial Platform for SCADA, IIoT, MES, and More"; SCADA is the first solution in the platform's own solution list; "Ignition SCADA… combines an unlimited licensing model, with instant web-based deployment, and the industry-leading toolset for supervisory control and data acquisition (SCADA) — all on one open and scalable universal platform." Water districts cited as mission-critical SCADA users ("Water districts all over the country trust Ignition with their mission-critical SCADA systems").

**Vendor's own SCADA definition (FAQ, A):** "Supervisory Control and Data Acquisition (SCADA) software is used to monitor/control industrial processes. SCADA software works by receiving real-time data (via PLCs or RTUs) from devices (like sensors or pumps) on the plant floor. It then processes, distributes, and displays that data."

**Standard SCADA package (FAQ, A):** Vision (runtime clients), OPC UA with drivers, Tag Historian, Alarm Notification, Reporting, SQL Bridge — i.e., acquisition + clients + history + alarming + reporting + transaction machinery as the vendor's own SCADA bundle.

**Feature surface (A):**
- Data acquisition: built-in OPC UA "to connect to practically any PLC"; native driver suites; SQL database connections; MQTT for IIoT devices.
- Real-time monitoring: "engineered to streamline data-throughput so you see true real-time tag values… quickly see the status of your facility, on any device."
- Control via HMIs: "easily start and stop processes, monitor multiple data points at multiple locations, and check the status of the entire plant floor."
- Visualization: dashboards, charts, KPIs, trending.
- Deployment: "instantly web-launch an unlimited number of zero-install, full runtime clients on virtually any device from a central server"; mobile-responsive SCADA applications; cross-platform server (Windows/Linux/macOS, even Raspberry Pi-class per FAQ).
- Store-and-Forward: "Store-and-forward historical data so you never lose it."
- Mission-critical: "Easily add fault tolerance for mission-critical systems by adding redundant servers."
- Security: SSL, federated identity, MFA, SSO.
- Scalability: "Scale from a single client installation to an enterprise-wide system."

**Platform architecture (Tier 1, HMI pass — reused as corroboration):** Gateway (central server: device connections, tag database, alarm state, redundancy), Designer (development environment, save-to-server deployment), Vision/Perspective runtime clients; tags as named data points decoupled from device addresses with quality codes; per-tag alarming with Active/Cleared × Unacknowledged/Acknowledged states, acknowledgment, shelving, alarm journal, notification pipelines; tag historian to SQL.

### Product B — AVEVA Plant SCADA (ex-Citect SCADA)

Key observations (Layer A, Tier 2):

- Positioning: "Flexible, high-performance supervisory control and data acquisition (SCADA) software for plant personnel." "Citect SCADA is now AVEVA Plant SCADA."
- Operator awareness: "Context-aware SCADA visualization with an out-of-the-box situational awareness layout"; "Equipment-driven interface gives operators real-time, holistic situational context"; "A single interface seamlessly integrates alarming, trending, interlocks and control data together across multiple monitors."
- Alarm management: alarm indicators with severity; **alarm shelving** ("temporarily silence alarms for a specific duration or until a specified time—with the ability to re-shelve"); "Define up to 8 causes, responses and consequences for your alarms"; "instant visual alarm summary shows the highest priority alarm for each piece of equipment."
- Engineering: configurable symbol library (situational-awareness best practices); integrated development environment; equipment templates ("reusing, duplicating and propagating changes"); **"Deploy changes live without interrupting operations, stopping data gathering or taking systems offline"**; "Centralized project deployment provides controlled transfer of project changes to servers and clients, native version control with local and remote rollback, and delta-only transfer"; Cicode scripting language.
- Additional capabilities: HTML5 web client (local network); Access Anywhere extension (external network, read/write secure access); real-time reporting; process analyst trending; SPC module; **"Architectural flexibility for centralized or distributed systems, inclusive of clustering"**; **client and server redundancy**; **"150+ communication drivers"**; role-based user security; multi-language.
- Portfolio context: AVEVA Historian as companion ("process database integrated with operations control"); AVEVA Insight (SaaS analytics); InTouch HMI remains a separate product line (HMI pass).
- Customer stories: pipeline monitoring (North American energy provider), mining, tunnel, iron/steel.

### Product C — SurvalentONE SCADA (+ Optional Applications)

Key observations (Layer A, Tier 2):

- Positioning: "an industry-leading, real-time supervisory control and data acquisition solution that allows utilities to dramatically improve the way they operate, monitor, and control their network." "With real-time equipment status, metering data, alarming, and control, operators can detect problems before they occur and take action to prevent outages." "Advanced data collection capabilities enable operators to manage remote assets and help field crews identify the outage location quickly." "ability to remotely control network devices."
- Foundation posture: "a solid foundation for adding new ADMS applications and devices" — the vendor's own framing of SCADA as the substrate beneath ADMS.
- Industries: electric, gas, water, transit, renewable energy generation, data centers, mining, oil & gas, plant operations. "700+ utilities worldwide."
- Control-room clients: SmartVU ("for Control Room" brochure); STC Explorer; WebSurv (web client).
- **Optional applications (the utility SCADA module surface, A):**
  - **Automatic Generation Control (AGC)** — "a feedback control system that regulates the power output of electric generators within your control area so as to maintain scheduled system frequency and/or power interchange" — generation regulation sold as a SCADA add-on, not part of the SCADA core.
  - **Control Panel** — an IED represented by its front-panel image; "dynamic elements display current values of the points in the IED, and allows the user to issue controls and set-points."
  - **Database Transcription** — bi-directional transcription of SCADA data (current values, historical data, operation messages including alarms, event logs including **SOE**) into relational databases.
  - **Disturbance Capture** — monitors analog/status points, defines trigger events, generates disturbance capture files.
  - **Excel Add-in** — real-time point data + historical information in spreadsheets.
  - **Fault Data Recorder** — uploads fault data from protective relays.
  - **IED Wizard** — automates creation of database points for supported IEDs (templates).
  - **Alarm Suppression** — primary/secondary alarm point relationships for suppression or group acknowledgement.
  - **Operations & Outage Accounting** — Event Data Recording "records all status changes and control operations" (retention figure vendor-specific, research notes only).
  - **Replicator** — real-time replication of the SCADA/ADMS database to a DMZ SQL Server for corporate access.
  - **Virtual RTU** — "a virtual device that can be polled by another master station via DNP3.0 or Modbus… a great alternative to ICCP for sharing data between two SCADA master stations" — master-to-master data exchange as a named concern.
  - **Remote Alarm Annunciation (RAA)** — separate brochure; alarm notification beyond the control room.
- Sibling-pass corroboration (EMS pass): Network Topology Processor sits above SCADA points feeding network-analysis applications (the ADMS-side seam).

### Product D — VTScada (Trihedral)

Key observations (Layer A, Tier 2):

- **Vendor's own SCADA definition (A):** "Supervisory control and data acquisition (SCADA) systems are comprised of HMI software (such as VTScada) that uses a network to communicate with distributed remote telemetry units (RTUs) and programmable logic controllers (PLCs) to control remote hardware and retrieve logged process information. For example, municipal utilities can use radios to centrally monitor and control water distribution and wastewater collection sites spread over a wide geographical area or an Ethernet network to oversee multiple treatment plants."
  - Structurally load-bearing: (1) SCADA *comprises* HMI software — the HMI layer is a component of SCADA; (2) the network + distributed RTUs/PLCs + remote control + logged-process retrieval are the defining elements; (3) the canonical example is wide-area radio, with plant-Ethernet as the second example — geographic spread is canonical, not exclusive.
- "More than HMI and SCADA Software — VTScada also natively includes components not commonly found in HMI or SCADA software platforms such as polling management, historian, trends viewer, report generation, application version control, alarm notification, and system backup."
- Scale drift in one product (A): "Easily expand your system from a simple OEM machine interface or standalone workstations to a large, distributed client/server system." — the HMI→SCADA continuum inside one product family.
- "Built for applications monitoring hundreds to millions of I/O on a single server"; "VTScada's hardware independence and open connectivity support all major PLCs or RTUs and provide an advancement over polling with Master PLCs."
- Integrated components (licensing page, A): Application Server ("primary or redundant event-driven execution for any scale"); Runtime Client ("can function as a complete or partial back-up for system operations"); widgets/graphics library; **Historian** ("high performance with zero set-up"); security (privilege + role-based); SNMP resource monitoring; **Alarms and Events** ("unlimited logging of all user and system actions"); **Trending** ("automatic"); reporting; slippy maps; **Electronic Operator Logbooks** ("tamperproof recording of noteworthy events").
- Drivers (A): Common (Modbus, DF1, CIP/ENIP, Siemens S7, Omron Host Link, OPC); Advanced (**DNP3**, SNMP, Motorola ACE, CalAmp and MDS **radio diagnostics**); proprietary; DataLogger.
- Development (A): Idea Studio ("online, offline and multi-developer"); Automatic Version Control ("system-wide disaster recovery and audit tools"); Change Deployment ("remotely update all computers with a single click"); scripting (700+ functions); ODBC/OPC servers, web services.
- Feature catalog (A): process displays, page navigation, slippy maps, alarm and event management, Historical Data Viewer, report generator, application security, encrypted operator notes, batch & recipe management, **Control Tokens & Lock System**, thin clients, alarm notification, real-time configuration tools, changesets, realm area filtering, hierarchical tag browser, **lift station templates** (water-sector equipment templates), soft logic control, legacy conversion, OEM layers, **redundancy and automatic failover**, real-time history and configuration backup, workstation health monitoring, historical data logging, SCADA historian, ODBC server, OPC client/server, web services, **modem management**, device driver library, **polling management**, edge computing, **I/O and PLC deadbanding**, **read-only DMZ server**, **master & subordinate applications**.
- Licensing (A): per-seat Runtime vs Development Runtime (each "can simultaneously function as a client as well as a primary or backup server"); I/O tag-count tiers; thin clients (Internet Client for PCs without VTScada; Mobile Internet Client for phones/tablets).
- History (A): 1988 DOS HMI ('WEB') → 1995 VTS → 2001 "VTScada, a set of dedicated telemetry features included with every license" → modern VTScada; "trusted SCADA alternative for 35 years"; industries: water/wastewater, oil & gas, power generation, marine, broadcasting, food & beverage, manufacturing, airports.

### Product E — GE Vernova CIMPLICITY / iFIX / iPower

Key observations (Layer A, Tier 2):

- Family framing: "HMI/SCADA" is one product family (CIMPLICITY | iFIX) in GE Vernova's software catalog — the automation-vendor bundling pole.
- CIMPLICITY: "designed to do far more than monitor and display. As a proven, enterprise-class HMI/SCADA, CIMPLICITY empowers your operators with the insight, context, and tools they need to act quickly and confidently—**across single sites or multi-site operations**." High-performance HMI design concepts (ISA and GE research-based); certificate-based communications.
- **iPower (the utility SCADA description, A):** "an open, standards-based SCADA solution, is scalable from substation automation systems to complex computer networks in larger utility control rooms. It provides **real-time data collection, db management, dynamic display, and secure operator supervisory control**." — the four-part utility-SCADA function statement from a second vendor.
- Extensions: Industrial Gateway Server / Proficy Webspace (web/mobile clients extending iFIX/CIMPLICITY "full control, visualization"); Dream Report (reporting over archives); MTConnect-OPC UA driver (non-polling collection).
- Portfolio context: GE Vernova sells GridOS (ADMS/EMS/DERMS) and Proficy Historian as separate lines — SCADA/HMI is distinct from both the network-model estate and the historian.

---

## Cross-product Comparison

| Dimension | Ignition | AVEVA Plant SCADA | SurvalentONE SCADA | VTScada | GE Vernova (CIMPLICITY/iPower) |
|---|---|---|---|---|---|
| Self-label | "SCADA" (platform also sells HMI as a solution) | "SCADA software for plant personnel" | "real-time supervisory control and data acquisition solution" | "SCADA software"; SCADA "comprised of HMI software" | "enterprise-class HMI/SCADA"; iPower "a SCADA solution" |
| Field side | PLCs/RTUs via OPC UA + drivers; MQTT for IIoT | 150+ communication drivers | IEDs, relays, remote network devices; IED Wizard; protocols incl. DNP3/Modbus | RTUs and PLCs; Modbus/DF1/DNP3/radio drivers; polling management | PLCs; substation automation → utility control rooms (iPower) |
| Central data object | tags (named points, quality codes) | equipment-driven context over SCADA data | SCADA database points (status/analog); SOE event logs | hierarchical tag browser; I/O tags | "real-time data collection, db management" |
| Supervisory control | "start and stop processes"; write-back via bindings | interlocks + control data in one interface | "remotely control network devices"; controls and set-points on IED panels | "control remote hardware"; control tokens & locks | "secure operator supervisory control" |
| Alarming | per-tag alarms, ack, shelving, journal, notification pipelines | indicators, shelving, causes/responses/consequences, priority summary | alarming + alarm suppression (primary/secondary) + remote alarm annunciation | alarms & events, alarm notification, unlimited logging | alarm surfaces implied (HMI/SCADA core) |
| History | Tag Historian module; store-and-forward | AVEVA Historian companion; trending | Database Transcription; historian in estate (Helix) | historian + trending integrated, "zero set-up" | Dream Report over archives; Proficy Historian separate |
| Communication integrity | store-and-forward; redundant servers | client/server redundancy; clustering | Replicator to DMZ; Virtual RTU master-to-master | redundancy/failover, store-and-forward-class backup, deadbanding, modem management, polling management | certificate-based comms |
| Engineering environment | Designer IDE, save-to-server | IDE, equipment templates, live deployment, version control + rollback | IED Wizard, Project Development System | Idea Studio, version control, changesets, one-click deployment | database/modeling capabilities ("easy repeatability, modeling") |
| Operator surfaces | Vision desktop + Perspective web/mobile; dashboards | desktop client + HTML5 web + Access Anywhere | SmartVU control room; WebSurv web | runtime clients, thin clients, mobile internet client, slippy maps | desktop + Webspace web/mobile |
| Security | SSL, MFA, SSO, federated identity | role-based permissions | DMZ replication; secure supervisory control | privilege + role models; read-only DMZ server | certificate-based communications |
| Scope drift | single machine → enterprise; water districts | plant → infrastructure (tunnels, pipelines, mining) | distribution network → multi-utility | OEM machine interface → distributed client/server | single site → multi-site; substation → utility control room |
| Business model | unlimited server license | editions + subscription | modular catalog | per-seat + I/O tag count | enterprise suite |

### Cross-product commonalities (Layer B)

1. **The master↔field-unit architecture.** Every sampled product is a central supervisory system acquiring data from and issuing commands to a population of field devices (PLCs, RTUs, IEDs, relays, remote network devices) through industrial drivers/protocols. The field side is always *other* units — the SCADA is not itself the controller.
2. **The point database as the central data organization.** All samples hold the supervised estate as named points/tags (status + analog + events), decoupled from raw device addressing. None of the sampled SCADA products requires a connected network model — that layer appears only in the ADMS/EMS siblings (Survalent's own NTP product sits above SCADA points).
3. **Supervisory control write-back.** Every sample pairs acquisition with operator command of remote devices (start/stop, open/close, setpoints), with the command executed by the field unit's own logic. GE's iPower names it exactly: "secure operator supervisory control."
4. **Alarm machinery in the core offering.** Annunciation, acknowledgment, shelving/suppression, alarm/event logging, and notification beyond the control room appear across the sample (state-machine depth verified Tier-1 in Ignition via the HMI pass).
5. **Communication-integrity machinery.** Store-and-forward, redundancy/failover, deadbanding, polling management, modem/radio management, DMZ segregation — the unreliable-link reality is a first-class concern in every product that names it.
6. **Engineering/runtime separation with deployment.** A development environment (Designer / IDE / Idea Studio / IED Wizard / Project Development System) creates the point database, screens, alarms, and connections; deployment to servers/clients is a distinct act, with version control and rollback in the mature products.
7. **Operator HMI surfaces inside the SCADA.** Every SCADA ships operator screens (process displays, alarm lists, trends, control faces) — the HMI layer is a component of SCADA, stated verbatim by VTScada ("comprised of HMI software") and practiced by all.
8. **History/trends present in some form** — embedded historian modules or companion historian products; never absent from the offering.
9. **Security as an operational requirement** — role-based access, control tokens/locks, DMZ patterns, certificate-based comms.
10. **Scale drift is native.** Every sampled family spans from single-machine/OEM scope to distributed multi-site systems — the HMI→SCADA continuum lives inside single product families.

### What is product-specific (A-only) or vendor-packaging

- Ignition: Gateway/Designer/Vision/Perspective naming; unlimited licensing; module bundle composition; MQTT/IIoT posture.
- AVEVA: Cicode; Access Anywhere; situational-awareness library; 8-cause alarm annotation; 150+ driver count (vendor figure).
- Survalent: SmartVU/STC/WebSurv clients; AGC/Virtual RTU/Replicator/Disturbance Capture/Fault Data Recorder module names; 30-day event retention figure; 700+ utilities figure.
- VTScada: Idea Studio/changesets; control tokens & lock system; lift-station templates; operator logbooks; slippy maps; reactive-language heritage; 35-year lineage claims.
- GE: iPower naming; IGS/Webspace; Dream Report; ISA/GE high-performance-HMI design program.

---

## Abstraction Hierarchy

### L0 — Defining Invariant (deliberately minimal)

A system is recognizable as SCADA only if all three hold:

1. **The distributed field-unit population under supervision.** The supervised estate is a population of field endpoints — RTUs, PLCs, IEDs, relays, meters, remote devices — each individually addressable, each acquiring local measurements/statuses and executing commands locally with local control autonomy: the process keeps running under field-side control when the supervisory link is down. Classically the units are geographically remote (pipelines, utility networks, scattered sites) — the wide-area spread is the canonical context and the reason the communication machinery exists — but a plant-wide estate of many autonomous controllers satisfies the same structure. Remove → the operator interface of one local process (HMI territory) or a plant-integrated control system (DCS territory).
2. **Central supervisory acquisition into a point database.** A central master station continuously acquires telemetry — measurements, statuses, events — from the field units over the communication network into a central database of named points (values + quality/state), decoupled from raw device addressing. The organization is point-based; no connected network model is required (its presence marks the ADMS/EMS siblings). Remove → scattered device-local displays; no central system.
3. **Supervisory control write-back to remote devices.** Operators (or supervised automation) at the center issue commands — start/stop, open/close, setpoints, mode changes — to remote field units through the same point layer; the field unit's local logic executes them, and the control is supervisory (from above), not the execution of the process control itself. Remove → telemetry monitoring only; the "supervisory control" half of the name is gone.

Jointly-held is load-bearing:

- 1 alone = a fleet of autonomous controllers with no supervisory system.
- 2 without 1+3 = a telemetry collector/logger.
- 3 without 1+2 = a blind command channel with no acquired picture.
- 1+2 without 3 = monitoring-only telemetry (the "DA" without the "SC").
- 1+3 without 2 = remote control with no central picture.
- 2+3 without 1 = a monitoring/control system over local devices — HMI/DCS operator-station territory.

Anti-overfitting notes applied:

- **"Multi-site"/geographic spread is NOT in L0.** The canonical context is wide-area (utility, pipeline, water), but plant-wide SCADA over many PLCs (AVEVA "for plant personnel", Ignition "entire plant floor", VTScada Ethernet example) satisfies the core. The invariant is the distributed autonomous field-unit population, not the geography.
- **RTU as a device class is NOT in L0.** PLCs, IEDs, relays, meters, gateways all serve as field endpoints; "RTU" is the classic name for the class.
- **Specific protocols are NOT in L0.** DNP3, Modbus, IEC 60870/61850, OPC UA, MQTT, proprietary radio — all observed as implementations. Protocol-agnostic is the invariant.
- **The historian is NOT in L0** — embedded modules or companion products (consistent with the historian pass).
- **Alarming is NOT in L0** — held at L1 (standard, effectively universal; a minimal SCADA with few alarms is still SCADA), consistent with the HMI pass's resolution.
- **Operator screens are NOT in L0** — they are the HMI layer *inside* SCADA (standard structure), not the SCADA's defining structure; the operator-screen core cannot discriminate (HMI pass's own finding, ratified).
- **Web/cloud/mobile deployment is NOT in L0** — classic master-station deployments satisfy without any of it.

### L1 — Common Mature Structure

- **Operator HMI surfaces**: process/mimic displays, equipment faces, alarm lists, trend displays, control faces — the HMI layer inside the SCADA (the HMI Type's core, embedded here).
- **Alarm machinery**: condition evaluation on points, annunciation, operator acknowledgment, shelving/suppression, alarm/event journals, notification beyond the control room (email/SMS/voice, remote annunciation).
- **Historical logging + trends**: embedded historian modules or companion historian products; store-and-forward so history survives link interruptions.
- **Communication-integrity machinery**: polling management, report-by-exception/deadbanding, store-and-forward buffering, time-stamping at source, modem/radio management, redundant servers with automatic failover.
- **Engineering environment**: point-database configuration (incl. IED templates/wizards), screen development, driver/connection configuration, alarm configuration, deployment with version control and rollback.
- **Security**: role-based operational access, control tokens/locks on devices, DMZ segregation for corporate access, certificate-based communications.
- **Driver/protocol library**: broad multi-vendor driver sets (Modbus, DNP3, OPC, vendor protocols, radio).
- **Event/SOE recording**: sequence-of-events and disturbance capture in the utility pole; operation/outage accounting.
- **Master-to-master data sharing**: Virtual RTU-class republishing, ICCP-class exchange between SCADA systems.
- **Web/mobile/thin clients** and remote access.

### L2 — Variant / Optional Structure

- **Domain/industry**: utility distribution SCADA (electric/gas/water/transit), pipeline/oil & gas SCADA, plant/factory SCADA, infrastructure (tunnels, airports, marine, broadcasting), renewables.
- **Scale**: single-server small systems → distributed client/server → multi-site enterprise; tag-count tiers vs unlimited licensing.
- **Packaging**: standalone SCADA product; module composing an ADMS/EMS estate (Oracle Flex SCADA, SurvalentONE SCADA as ADMS foundation); one solution on a multi-purpose platform (Ignition); one member of an automation vendor's HMI/SCADA family (GE).
- **Deployment**: on-premises hardened servers (classic) → web-deployed clients → cloud-hosted/edge editions.
- **Control posture**: manual supervisory control as the base; supervised automation as add-ons (AGC-class feedback control sold as a SCADA option at Survalent; soft-logic control at VTScada).
- **Generation-control content**: AGC as an add-on module (utility pole) — not part of the SCADA core (it is the EMS-side balancing leg when combined with network analysis).
- **Era naming**: "telecontrol/telemetry systems" → "SCADA" → "industrial platform/IoT-ready SCADA" — the current platform-era vocabulary over the same structure.

### L3 — Vendor-specific (research notes only)

- Ignition: Gateway/Designer/Vision/Perspective; unlimited-tags licensing; Tag Historian/SQL Bridge/Alarm Notification module bundle; Edge editions; MQTT/Sparkplug partner modules.
- AVEVA: Plant SCADA/Citect lineage; Cicode; Access Anywhere; situational-awareness symbol library; "up to 8 causes/responses/consequences"; 150+ drivers claim; AVEVA Historian/Insight pairing.
- Survalent: SmartVU/STC Explorer/WebSurv; AGC, Control Panel, Database Transcription, Disturbance Capture, Excel Add-in, Fault Data Recorder, IED Wizard, Alarm Suppression, Operations & Outage Accounting (30-day event retention), Replicator, Virtual RTU, RAA; Themis/Helix/Polaris estate siblings.
- VTScada: Idea Studio; changesets; control tokens & locks; lift-station templates; operator logbooks; slippy maps; VTScadaLIGHT free tier; reactive-language heritage; 1988 DOS lineage.
- GE Vernova: CIMPLICITY/iFIX family; iPower; IGS/Webspace; Dream Report; MTConnect-OPC UA driver; Proficy Historian as a separate line.
- (Siemens/Rockwell/Schneider/Hitachi SCADA lines — unreachable across passes; excluded from all assertions.)

## Vendor-specific Findings

See L3. Two vendor statements are structurally informative:

- **VTScada's own definition**: "SCADA systems are comprised of HMI software… that uses a network to communicate with distributed remote telemetry units (RTUs) and programmable logic controllers (PLCs) to control remote hardware and retrieve logged process information." — first-hand vendor confirmation that (a) the HMI layer is a *component* of SCADA, and (b) the distributed RTU/PLC population + remote control + logged-data retrieval are the defining elements.
- **Ignition's own definition (FAQ)**: "SCADA software works by receiving real-time data (via PLCs or RTUs) from devices… It then processes, distributes, and displays that data." — the acquisition-first framing from the platform pole.
- **GE iPower's function statement**: "real-time data collection, db management, dynamic display, and secure operator supervisory control" — a second vendor's four-part decomposition of utility SCADA.
- **Survalent's foundation posture**: SCADA is "a solid foundation for adding new ADMS applications" — the substrate relationship to the network-model siblings, from the utility specialist itself.

## Rejected Findings (anti-overfit)

- **"SCADA = HMI software."** Rejected as the definition: every SCADA contains HMI surfaces, but the HMI core (screens + write-back for a machine/local process) does not require the distributed field-unit population. The straddle is real (Ignition self-labels both; GE sells one "HMI/SCADA" family) but the structures differ — see Boundary #1.
- **"SCADA = multi-site only."** Rejected: plant-wide SCADA over many PLCs on one site is marketed and deployed as SCADA (AVEVA "for plant personnel"; VTScada Ethernet example). The invariant is the distributed autonomous field-unit population; geographic spread is canonical context.
- **"SCADA = DNP3/Modbus polling."** Rejected: OPC UA, MQTT, IEC protocols, proprietary radio all observed; polling vs report-by-exception vs publish-subscribe all observed. Protocol- and acquisition-style-agnostic is the invariant.
- **"SCADA includes the historian."** Rejected as definitional: historians appear as embedded modules or companion products; the historian pass holds the archive as a distinct Type with no control duty.
- **"SCADA includes AGC/generation control."** Rejected: AGC appears as an *optional application* (Survalent) — the balancing leg belongs to the EMS sibling when combined with network analysis.
- **"SCADA includes the network model."** Rejected: the point-based organization without a required network model is precisely the seam to ADMS/EMS (ADMS/EMS passes; Survalent's NTP sits above SCADA points).
- **"SCADA = IIoT platform."** Rejected: IIoT platforms hold device fleets with async operations and no live supervisory control duty over a process (IIoT pass's own seam); SCADA's defining loop is live supervision + control.
- **"Cloud/web deployment is definitional."** Rejected: classic master-station SCADA predates all of it; era machinery.

## Boundary Findings

### 1. vs HMI — the joint review (DISCHARGED)

The HMI pass's proposed discriminator is **ratified and sharpened**:

- **HMI** = the operator-interface layer for a machine or local process: live process-data layer + engineered operator screens + operator write-back. Scope: an operator station or panel; a plant area at most.
- **SCADA** = the supervisory system over a distributed field-unit population: central master station + point database + supervisory control write-back to field units with local autonomy. The operator screens are the SCADA's HMI layer — a standard component, not the defining structure.
- **Containment, not competition**: the SCADA Type *contains* HMI surfaces as its operator interface (VTScada: SCADA "is comprised of HMI software"); the HMI Type remains distinct as the operator-interface layer defined by its own three-leg core. The two Types share the tag/write-back/screen machinery; the discriminator is the **supervisory master↔field-unit architecture** — the distributed autonomous field-unit population (leg 1) and the central supervisory station (leg 2).
- Remove-tests both directions: strip the distributed field-unit architecture from a SCADA deployment (one local process, one controller) → a clean HMI remains; add remote field units + a supervisory center to an HMI deployment → the same product family becomes SCADA. Both observed inside single product families (Ignition HMI solution vs SCADA solution; VTScada "from a simple OEM machine interface… to a large, distributed client/server system"; GE one "HMI/SCADA" family spanning both).
- Market straddle documented, not resolved away: Ignition self-labels both; AVEVA keeps InTouch HMI and Plant SCADA as separate lines; GE sells one HMI/SCADA family. The seam is architectural scope, and vendors package across it freely.

### 2. vs DCS

DCS = plant-wide integrated control system: distributed controllers executing configured control strategies as the system's core function, with integrated engineering of the control logic. SCADA = supervision over field units whose local controllers run the process; the SCADA's own function is acquisition + supervisory command, not control execution. Emerson sells DCS and SCADA as separate lines (DCS pass). Remove the field-side autonomy + supervisory posture and add integrated control-strategy engineering → DCS.

### 3. vs ADMS / EMS (network-model siblings)

SCADA is point-based; the connected electrical network model + network analysis is the differentiator (ADMS/EMS passes, ratified). Survalent's own catalog: SCADA is the foundation; the Network Topology Processor and DMS applications sit above the points. Oracle's Flex SCADA is a module inside the ADMS. Remove the network model + analysis + domain applications → SCADA remains (the grid-operations umbrella document's own removal test, consistent from this side).

### 4. vs Industrial Historian

Historian = archival infrastructure with no control duty; SCADA = live supervision + control. SCADA commonly embeds or pairs a historian (Ignition Tag Historian; AVEVA Historian companion; VTScada integrated historian; Helix beside SurvalentONE). Consistent with the historian pass.

### 5. vs Industrial IoT Platform

IIoT = device connectivity + fleet management + data access, with async operations through agents/gateways (Cumulocity's dial-up rationale) and no live supervisory control duty over a process. SCADA = live supervision + control write-back over field units. Convergence zone: MQTT/IIoT transports feed SCADA data layers (Ignition MQTT modules); edge editions blur deployment, not structure. Consistent with the IIoT pass's seam.

### 6. vs PLC Programming Environment

The PLC-PE engineers the controller's control logic; SCADA supervises the running result. Same vendor suites bundle both (packaging, not identity). Consistent with the HMI/DCS passes.

### 7. vs Grid Operations Platform (umbrella counterparty)

Consistent: SCADA is the substrate member of the control-room family; the umbrella document's removal test ("removing the network model + analysis + domain applications leaves SCADA") matches this pass's L0 exactly. No conflict; the member mapping stands.

### 8. vs monitoring dashboards / telemetry-only systems

Acquisition without supervisory control write-back is telemetry monitoring, not SCADA — the "SC" half of the name is load-bearing. (Same wall as the HMI pass's "monitoring dashboard" remove-test.)

## Historical / Market-Sample Check

- **Founding-generation SCADA (1960s–70s utility/pipeline era)**: master station in a control room + RTUs at remote sites over leased lines/radio; cyclic polling; telemetry (analog + status); supervisory trip/close commands; alarm annunciation on mimic boards; paper/tape logs. Satisfies all three L0 legs with no screens-as-software, no historian database, no network model, no web/cloud. The point-based organization and supervisory write-back are exactly the founding structure.
- **1980s–90s software SCADA generation** (Citect, FIX, RSView-class, early VTScada lineage): tag databases, animated mimics, alarm annunciation + acknowledgment, trends, polling drivers, client/server — satisfies all three legs.
- **Panel/machine HMI generation** (Pro-face, PanelView-class): satisfies the HMI core but *not* the SCADA L0 (no distributed field-unit population under supervision) — correctly excluded, confirming leg 1 discriminates.
- **Modern platform SCADA** (Ignition, Plant SCADA, VTScada current): satisfies with web/mobile deployment, embedded historians, MQTT — nothing era-specific enters the core.
- **Regional/utility variants** (European telecontrol, Asian utility SCADA): the L0 names no protocol, vendor, or regulatory regime; safety/protocol specifics are L1/L2.
- Conclusion: the L0 holds across eras and geographies; the definition names no deployment shape, protocol, device class, or business model. Check passed.

## Uncertainties

1. **PLC-vendor-ecosystem SCADA specifics** (Siemens WinCC/TeleControl, Rockwell FactoryTalk, Schneider EcoStruxure, Hitachi Energy) unreachable across multiple passes; the automation-vendor pole is evidenced only through GE Vernova's pages. Claims about that pole are held at market-structure strength.
2. **Operational depth**: no Tier-1 operational manual was fetched this pass (the Ignition Tier-1 manual evidence is reused from the HMI pass). Precise operational rules (exact polling semantics, exact redundancy behavior, exact SOE handling) are therefore not asserted; module/capability claims are Tier-2 strength.
3. **Whether alarming should be L0**: resolved to L1 with the same reasoning as the HMI pass; recorded for any future joint review.
4. **"Multi-site" phrasing risk**: the HMI pass proposed "multi-site supervisory system"; this pass sharpens to "distributed field-unit population" because plant-wide SCADA is in-sample. The HMI document's Related-Types table says "multi-site supervisory system" — a taxonomy pass may wish to harmonize the phrasing; the seam itself is unaffected.
5. Numeric claims (700+ utilities, 150+ drivers, 30-day retention, tag-count tiers) observed only as vendor figures; deliberately excluded from the final document.
6. AGC's placement (SCADA option vs EMS content) is packaging-dependent; documented as an add-on module, not core.

## Final Synthesis

**SCADA is the supervisory control and data acquisition system over a distributed field-unit population.** Its defining structure is three jointly-held legs: (1) a population of distributed — classically geographically remote — field endpoints (RTUs, PLCs, IEDs, relays, remote devices), each individually addressable, each acquiring local data and executing commands locally with local control autonomy; (2) a central master station continuously acquiring telemetry from those units into a central point database (named points, values + quality, decoupled from device addresses, no network model required); (3) supervisory control write-back — operators (or supervised automation) commanding remote devices through the same point layer, with the field units' own logic executing. Around that core, mature products carry the operator HMI layer, alarm machinery with acknowledgment and notification, historical logging/trends with store-and-forward, communication-integrity machinery (polling management, deadbanding, redundancy/failover), an engineering environment with deployment and version control, security (roles, control tokens, DMZ), broad driver libraries, and event/SOE recording. The HMI seam is resolved by containment: SCADA *contains* HMI surfaces as its operator layer; the HMI Type remains the operator-interface layer for machine/local-process scope — the discriminator is the supervisory master↔field-unit architecture, not the screens. The ADMS/EMS seam is the network model; the DCS seam is control execution vs supervision; the historian seam is archive vs supervision; the IIoT seam is live supervisory duty vs async device management. The historical check passes: founding-generation master+RTU systems satisfy the core with none of the modern machinery.
