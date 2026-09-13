# Research Notes — Mobile Network Management

## Research Goal

Understand what "Mobile Network Management" software actually is in the market: what objects it manages, what users do with it, how operational work flows through it, and where its boundary sits against neighboring directory leaves (Network Management [enterprise IT], Telecom OSS, Telecom Service Assurance, Telecom Network Planning / Design, Fiber Network Management, SIM / eSIM Management, Tower Management, Telecom Provisioning Platform, Subscriber Management).

## Initial Boundary (hypothesis before research)

- Core use: operations software that a mobile network operator (MNO) runs against its **deployed cellular network** — chiefly the radio access network (base stations, cells/sectors, antennas) — covering configuration, fault, and performance management, plus optimization.
- Users: network operations center (NOC) staff, RAN/O&M engineers, rollout/integration teams, vendor support.
- Nearest types: enterprise Network Management (different subject), Telecom OSS (umbrella), Telecom Service Assurance (service-level layer), Fiber Network Management (fixed plant), Telecom Network Planning (design-time).
- Main unknowns: exact managed-object vocabulary; whether the Type is RAN-only or spans core/transport; how automation (SON) relates to the core; whether management-system hierarchy (element manager vs network manager) is structural.

## Research Questions

1. What are the managed objects? (network elements, cells, parameters, alarms, KPIs, software packages)
2. What do users do day to day? (monitor, triage alarms, change parameters, upgrade software, optimize)
3. What is the core operational loop and the site/cell lifecycle?
4. Single-vendor (vendor-native NMS) vs multi-vendor management — how does the market structure this?
5. Where do SON / automation / AI fit — core or layer?
6. What scope is definitional: RAN only, or RAN + core + transport?
7. How is this distinct from Telecom OSS, Service Assurance, Network Planning, and enterprise IT Network Management?
8. Would older/regional products (2G-era OMC/NMS) still fit the definition? (historical check)

## Representative Products

Selection rationale: market representativeness + different product philosophies (purpose-built-RAN vendor NMS vs disaggregated Open RAN software) + different customer scale (nationwide MNO vs enterprise/campus/rural) + reachable official documentation.

1. **Nokia MantaRay family** — MantaRay NM (network manager; NetAct lineage), MantaRay SON (self-organizing network), MantaRay SMO (service management and orchestration). Vendor network manager pole, nationwide MNO scale, multi-technology 2G–5G. Official pages fetched 2026-09-09.
2. **Parallel Wireless** — Open RAN network software: Open RAN Controller, Near-RT / non-RT RIC, Real-time ALL G SON module. Disaggregated Open RAN pole, multi-vendor orchestration philosophy, rural/campus scale. Official pages fetched 2026-09-09.

Known representatives whose official documentation could **not** be reached in this environment (recorded as source-access limitation, excluded from the product-observation base):

- Ericsson Network Manager (ericsson.com product URLs 404; docs.ericsson.com timed out twice)
- Huawei carrier network management (iManager M2000 / iMaster NCE; only enterprise-NCE and fixed-network U2000 pages indexed; wireless-carrier NMS pages unreachable)
- ZTE NetNumen (not attempted after other priorities consumed the fetch budget)

## Sources

Tier 1/2 (official vendor pages, fetched 2026-09-09):

- Nokia MantaRay NM — https://networks.nokia.com/products/netact (redirects to MantaRay NM product page)
- Nokia MantaRay SON — https://www.nokia.com/mobile-networks/ran-operations/network-management-son/
- Nokia MantaRay SMO — https://www.nokia.com/mobile-networks/ran-operations/mantaray-smo/
- Parallel Wireless Open RAN Network Software — https://www.parallelwireless.com/products/openran-network-software/
- Parallel Wireless Real-time ALL G SON — https://www.parallelwireless.com/products/real-time-all-g-son/
- Parallel Wireless home/products nav — https://www.parallelwireless.com/

Supporting context:

- O-RAN Alliance specifications page (portal link only; spec PDFs not fetched) — https://www.o-ran.org/specifications
- Bing search engine (URL discovery only)

Unreachable / abandoned (per network-restriction rule, 1–2 failures then abandon):

- https://www.ericsson.com/en/portfolio/networks/network-manager (404), https://www.ericsson.com/en/networks/offerings/network-manager (404)
- https://docs.ericsson.com/ and /en/ericsson-network-manager (timeouts ×2)
- https://docs.parallelwireless.com/ (transport error), GitHub ParallelWireless/docs (timeout)
- https://en.wikipedia.org/wiki/NetAct and /Self-organizing_network (timeouts ×2)
- Huawei support/carrier NMS pages (search pollution; product line not reachable in English)
- DuckDuckGo HTML search (timeouts)

Evidence layers used below: **A** = directly observed on an official page of a specific product; **B** = cross-product commonality across the sampled products; **C** = canonical inference from cross-product comparison and boundary reasoning.

---

## Product Observations

### Nokia MantaRay NM (network manager; NetAct lineage)

Key observations (evidence A):

- The page carries a generic definition of the domain, not just the product: *"Network management, an integral part of mobile networks, covers configuring, automation and optimization tasks as well as monitoring, analytics and troubleshooting."*
- *"A network management system consists of tools for handling various network elements in live network and for the future network expansion. It provides comprehensive operation and maintenance capabilities for network elements in core, radio and transport networks both for managing physical network elements as well as virtualized network functions."* — scope spans core + radio + transport; physical NEs + virtualized functions.
- Market framing: operators run **multi-supplier, multi-technology** networks (2G/3G/4G/5G); management must address complexity and traffic growth.
- MantaRay NM positioning: *"single management system for all technologies"*; handles *"5G, as well as 2G/3G/4G from day 1"*; manages purpose-built RAN, Packet/Mobile Core, enterprise RAN, Cloud RAN (incl. data-center hardware and CaaS).
- Feature set named on the page: **troubleshooting, administration, software management, configuration management, 4G/5G slice management**.
- Automation features: zero-touch 5G rollout with **Plug-and-Play**; **mass base station rebuilding** (SRAN migration); **mass change verification on network elements**.
- AI: big-data + AI for e.g. *"intelligent correlation of network alarms"*; central source of network-wide operations data feeding other AI applications.
- Energy: energy monitoring/reporting; identification of high-energy sites (MantaRay Energy).
- Integration hierarchy: *"Seamless integration with existing OSS environments, providing a set of open interfaces … easy integration with 3rd party network elements, element management systems and other upper-level management systems"* — evidence for the element-manager / network-manager / OSS layering.
- Interfaces/openness: pre-built customizable workflows, REST APIs, CLI.
- Scalability pole: MantaRay NM XS — software-only, any hardware platform, campus/enterprise networks (part of anyRAN for enterprises).
- MantaRay family layering (from NM/SON/SMO pages): NM = network management; SON = application automation layer (multi-supplier non-real-time RIC, O-RAN R1); SMO = service management & orchestration framework aligned with O-RAN SMO architecture and TM Forum Autonomous Networks; AutoPilot = intent-based orchestration of SON modules and rApps; Digital Operations Center hosts RAN Slice Controller.

### Nokia MantaRay SON (self-organizing networks)

Key observations (evidence A):

- Positioning: *"boosts 5G radio network quality, efficiency, customer experience … through automated operations"*; modules *"automate planning, provisioning and verification"*.
- Scale rationale: 5G brings *"thousands of base stations and millions of cells — too much for humans alone to manage"*; complexity grows with frequency bands, slices, software capabilities.
- Goals stated in operator terms: reduce human involvement in radio network optimization; solve problems faster; prevent issues; reduce energy consumption *"without any degradation in network KPIs"*.
- Quality mechanics mentioned: parameters and needed optimizations exceed human capacity; automation/AI *"eliminate the risk of human errors"*; "most network outages are caused by human error" (NM page).
- Customer-network claims (vendor case studies, do not generalize): throughput improvements, drop-call-rate reductions, handover reductions, energy reductions with "no degradation in network KPIs".

### Nokia MantaRay SMO

Key observations (evidence A):

- Definition: *"Service Management and Orchestration (SMO) is an open platform for managing a multi-supplier, multi-technology radio access network (RAN). SMO provides the intelligence, automation and coordination for managing the end-to-end lifecycle of the network."*
- Layering: *"The SMO framework consists of different layers, including multi-supplier network management, application automation and orchestration."*
- Closed loop: *"closed loop network operations, allowing the network to detect conditions, make decisions, and execute corrective actions with minimal or even no human intervention."*
- Openness: manages multi-supplier networks, standardized interfaces, O-RAN-compliant rApps portable between vendor platforms; rApp marketplace + SDK.
- Slice automation: dynamic orchestration of network slices against slice SLAs.

### Parallel Wireless — Open RAN network software

Key observations (evidence A):

- Portfolio shape: Network Software (Open RAN Controller, unified/cloud-native/end-to-end platforms, performance, multi-tenant/sharing MOCN/MORAN, security) + Network Intelligence (Analytics, Real-time ALL G SON, Network Orchestrator).
- Open RAN Controller: *"E2 interface-based, OpenRAN controller orchestrates multi-vendor outdoor and indoor 5G 4G 3G 2G RAN, automates networks, provides QoS for voice and data while reducing deployment and maintenance TCO"*.
- Software platform: aggregator (gateway for RAN interfaces toward core: vBSC/vRNC/vENB/HeNB-GW/HNB-GW roles), Near-RT RIC (xApp framework, AI/ML inference), non-RT RIC (rApp framework, AI/ML training).
- Benefits named: *"OPEX reduction by network automation; Streamlined network management"*. Suite scope includes *"service assurance including analytics and monitoring"* (homepage text).
- Deployment: cloud-native; private/public/hybrid cloud; small to large scale.

### Parallel Wireless — Real-time ALL G SON

Key observations (evidence A):

- Three self-* pillars: **self-configuration, self-optimizing, self-healing** — controller makes the network *"self-configuring, self-optimizing, and self-healing"*.
- Closed loop with rollback: *"works in a closed-loop, it is able to take feedback from the network into account and automatically revert back to the last working state in the case of network degradation, all without any human intervention."*
- Self-configuration: plug-n-play cell addition across the **complete life cycle of the cell** for any technology/vendor; identifies new cells; runs configuration algorithms; initial **PCI and RACH** parameter calculation; **neighbor list** computation (intra/inter-frequency, IRAT); transmit-power optimization for new cells; **"Each cell's hardware and software inventory are automatically managed which helps mobile operators easily maintain inventory lists and plan for future upgrades."**
- Self-optimization feature list: Automatic Neighbor Relations (ANR); PCI conflict/confusion avoidance; **load balancing and traffic steering**; coverage & capacity optimization (TX power / E-tilt); mobility robustness optimization (handover success rate); paging optimization; RACH optimization; inter-cell interference coordination (ICIC/eICIC).
- Self-healing: *"instructing neighboring cells to compensate coverage for the cell that went down"*; hands-free maintenance for cell outages.
- Interfaces: standard XML, REST, YANG; open APIs to macro SON.
- Goals in KPI terms: reduce drop rate, improve handover success rate, improve cell-edge throughput, better spectrum/resource utilization, energy/cost savings.

---

## Cross-product Comparison

| Aspect | Nokia MantaRay (NM/SON/SMO) | Parallel Wireless (Open RAN software) | Evidence layer |
|---|---|---|---|
| Managed estate | network elements in **core, radio, transport**; physical + virtualized | multi-vendor 2G/3G/4G/5G (+Wi-Fi) RAN; RAN interfaces toward core | A/A → B |
| Configuration management | configuration management, software management, mass change verification, mass rebuild | self-configuration of new cells (PCI/RACH/neighbor/power), plug-n-play | A/A → B |
| Fault management | troubleshooting; intelligent correlation of network alarms; "faster detection and repair of NW incidents" | self-healing, outage compensation by neighbors; service assurance incl. monitoring | A/A → B (alarm-lifecycle detail not directly evidenced at either — see Uncertainties) |
| Performance management | monitoring, analytics; KPIs named in case studies (throughput, drop call rate, utilization) | KPIs named (drop rate, handover success, cell-edge throughput, coverage) | A/A → B |
| Element inventory | network elements in live network + future expansion | automatic hardware/software inventory per cell | A/A → B |
| Site/cell lifecycle | zero-touch rollout, plug-and-play, mass onboarding | complete cell lifecycle self-configuration, "time to activate services" | A/A → B |
| Optimization/SON | separate SON solution (modules automate planning/provisioning/verification) + rApps; AutoPilot orchestration | SON software module (ANR, load balancing, CCO, MRO, ICIC, RACH/paging) | A/A → B |
| Multi-vendor posture | manages multi-supplier networks; integrates 3rd-party NEs/EMSs; O-RAN interfaces on roadmap/aligned SMO | Open RAN by design; E2-based orchestration of any-vendor RAN | A/A → B |
| Management hierarchy | integrates with existing OSS, EMSs, upper-level management systems | RIC/rApp/xApp layering; orchestrator | A/A → B |
| Scale | nationwide MNO pole ("thousands of base stations, millions of cells") + XS campus pole | small-to-large, rural/campus-friendly, cloud-native | A/A → B |
| Energy | energy monitoring/reporting; AI energy savings | energy savings via optimization (secondary benefit) | A/A → B (depth varies) |
| Slicing | 4G/5G radio slicing automation (config + performance), RAN Slice Controller | not evidenced on fetched pages | A/— (single product) |
| AI/ML positioning | AI across NM/SON/SMO; alarm correlation; autonomous operations | AI/ML in xApps/rApps (training/inference) | A/A → B |
| APIs | REST, CLI, workflows | XML/REST/YANG, open APIs | A/A → B |
| Rollback-on-degradation | "mass change verification" (verification) | automatic revert to last working state | A (PW explicit); Nokia verification — B |

## Canonical Model (synthesis)

**Defining core (L0)** — deliberately small; jointly held:

1. **The live mobile network as managed estate** — the system holds and addresses the operator's deployed network elements (chiefly radio base stations and their cells/sectors; commonly also controller, core, and transport nodes), as managed records (inventory with hardware/software state). Remove → RF-planning/design tool (models a not-yet-existing network) or a single-element local shell.
2. **Configuration management of the elements** — reading and writing operational parameters and software on network elements, individually and at fleet scale (bulk changes, verification). Remove → passive monitoring/analytics viewer; the network can no longer be *operated* from the system.
3. **Fault management (alarms)** — network-detected problems surfaced as alarms/events that are tracked and worked to resolution. Remove → KPI reporting warehouse; operations has no incident surface.
4. **Performance management (counters/KPIs)** — operational measurements collected from the network and made analyzable (accessibility, retainability/drops, handovers, throughput, coverage, capacity). Remove → alarm ticketing console; no quality basis for optimization.

Legs 2+3+4 together are the classical OAM/FCAPS triad realized against a mobile network. The Type is the **run-time operations system of the live mobile network** (management system layer, above element managers, below/within operator OSS).

Jointly-held load-bearing checks:

- 1 alone = asset inventory / network documentation tool
- 1+2 without 3 = change-management console with no incident surface (config tool)
- 1+3 without 4 = alarm console without quality visibility (trouble-ticket frontend)
- 1+4 without 2 = monitoring/assurance viewer (can observe, cannot operate)
- 2+3+4 without 1 = generic FCAPS toolkit with no mobile-network object world

**Common mature structure (L1)**:

- Software/firmware management and upgrade campaigns
- Multi-technology support (2G→5G) and multi-vendor management posture
- Plug-and-play / zero-touch site integration (self-configuration); automatic hardware/software inventory
- SON-style optimization loops: ANR, load balancing/traffic steering, coverage-capacity optimization, mobility robustness, interference coordination; self-healing with neighbor compensation; closed loops with rollback-to-last-working-state
- KPI dashboards, reports, analytics
- Bulk/mass operations (mass parameter change + verification)
- Workflow automation, REST/CLI/open APIs; SDK/app frameworks at the automation layer
- Integration with element managers and upper OSS (management hierarchy)
- Energy monitoring/management
- AI-assisted alarm correlation and anomaly handling

**Variant / optional structure (L2)**:

- Scope: RAN-only management vs multi-domain (RAN + core + transport) — both evidenced
- Vendor-native NMS (managing the vendor's own equipment, integrating 3rd-party) vs Open RAN-native multi-vendor orchestration
- Purpose-built RAN vs cloud RAN incl. data-center/CaaS management
- Deployment: on-prem classic NMS vs cloud-native; software-only small-scale (campus/enterprise) vs nationwide
- SMO/rApp marketplace ecosystems and O-RAN alignment (RIC/xApps/rApps)
- Slice management (radio slicing automation) — evidenced at one vendor; optional
- Energy-management depth (monitoring vs AI-driven savings)
- SON as separate product vs integrated module

**Vendor-specific (L3)** (kept out of final document; examples only):

- MantaRay NM fast pass (release independence from NMS-NE pairs), MantaRay NM XS packaging, AutoPilot intent-based orchestration, rApp Marketplace, RAN Slice Controller, "world's first automated 4G/5G slicing in RAN", MantaRay Energy stats
- Parallel Wireless: Aggregator (vBSC/vRNC/vENB), ALL-G including Wi-Fi, MOCN/MORAN sharing enablement, X2-based ICIC
- Vendor case-study numbers (e.g., 29% busy-hour throughput improvement, 22% drop-call-rate reduction, 15,000 autonomous operations/hour, 90% faster incident detection/repair) — vendor claims about specific deployments; not generalized.

## Historical / Market-Sample Check (§24)

Question: would older, regional, or differently positioned products still fit?

- 2G-era operations-and-maintenance centers (OMC-class systems managing BTS/BSC populations with alarm handling, parameter administration, and traffic/performance statistics) satisfy all four L0 legs with no SON, no cloud, no AI, no slicing. The definition does not overfit to the 5G/Open RAN era.
- Open RAN-disaggregated and campus-scale small-footprint products satisfy the same core with very different packaging.
- SON is excluded from the core: it post-dates the Type by roughly two decades and is still sold as a separate solution/module.
- The definitional constant across eras is the object world (live cellular network elements, cells, radio parameters, alarms, counters), not any specific radio technology or automation style.

## Vendor-specific Findings

See L3 above. Also: Nokia's own generic definition of mobile network management (NM page) and its SMO/SON/NM layering are Nokia's framing of the O-RAN SMO architecture — used as evidence for market structure, not copied as the Type definition.

## Boundary Findings

- **vs Network Management (enterprise IT)** — different subject: enterprise/campus IT device estates vs carrier mobile network elements (base stations, cells, radio parameters). Shared vocabulary ("network"), different object worlds. (The enterprise-IT pass recorded the same seam from its side.)
- **vs Telecom OSS (umbrella)** — OSS spans fulfillment, assurance, inventory, workforce, charging etc. across the operator; Mobile Network Management is the mobile-domain network-management slice. The directory intentionally keeps domain-specific NMS leaves (cf. Fiber Network Management). Recorded as a taxonomy seam, not resolved here.
- **vs Telecom Service Assurance** — assurance centers on monitoring service-level quality/SLAs and detecting degradation across services; Mobile Network Management centers on **operating the network elements themselves** (configuration control + fault handling + performance management). Overlap on monitoring/KPIs; the seam is the ability and authority to change the network.
- **vs Telecom Network Planning / Design** — design-time vs run-time. Planning tools model a not-yet-built network and produce candidate designs; this Type operates the live estate. Remove the live-estate leg → planning territory.
- **vs Fiber Network Management** — fixed fiber plant of record (cables/strands/splices/ports) vs radio network elements. Seam already ratified by the fiber pass ("mobile centers RAN; this Type centers fixed fiber plant").
- **vs Tower Management** — passive site infrastructure (towers, space, leases) vs active network equipment and its radio function. Complementary records; different object worlds.
- **vs SIM / eSIM Management, Subscriber Management, Telecom Charging, Telecom Order Management** — subscriber/commercial side (BSS) vs network-side operations. Different units of record entirely.
- **vs Telecom Provisioning Platform** — provisioning is the service-fulfillment act of activating services on the network; this Type is the continuous management/operation of the network itself. Adjacent, order-driven vs always-on.
- **vs Telecom Network Inventory** — inventory exists as a leg (managed estate) inside this Type; standalone inventory products are broader multi-domain records without the operate loop. (Directory leaf not in sample; noted only.)
- "去掉什么就变成另一个 Type" judgments: remove live estate → planning; remove configuration authority → service assurance/monitoring; remove alarm+KPI legs → pure config tool; remove mobile object world → enterprise Network Management.

### Seam discharges (joint review, from this side)

Four prior §19 passes pre-held seams against this leaf. All are ratified here as keep-both:

1. **telecom-oss** — single-domain network management vs the multi-domain OSS umbrella. This leaf is a component leaf under the suite-level Telecom OSS umbrella (the umbrella note from the telecom-oss pass is confirmed from this side). OSS spans the operator's whole fulfillment + assurance + inventory + workforce estate; this Type is the mobile-domain network-management slice. Neither collapses into the other.
2. **telecom-service-assurance** — single-domain (RAN/core) network management vs the cross-domain service-level assurance discipline. The seam is the authority and tools to change the network: assurance detects and diagnoses service degradation; this Type operates the elements. The prior pass's boundary witnesses (NetAct Monitor as multi-vendor alarm management inside a single-domain NMS; NSP Wireless Supervision as a domain instance of supervision) are consistent with this pass's evidence.
3. **telecom-provisioning-platform** — continuous network operation vs service-grain activation. The prior pass's NetAct Configurator witness (parameter/plan-grain operations over modification plans) is consistent with this pass: this Type's configuration management is element/parameter-grain, not service-order activation. The prior pass's caution stands — this Type's "provisioning" vocabulary (self-configuration of cells) must not be read as the provisioning Type's service-order activation.
4. **telecom-network-planning** — live data flows INTO planning; live-network operation stays here. Design-time vs run-time, confirmed from this side.

## Uncertainties

1. **Alarm lifecycle vocabulary** — alarm management's existence is evidenced (Nokia: troubleshooting, intelligent alarm correlation; PW: self-healing, service assurance/monitoring), but neither fetched page documents the per-alarm state model (raise/acknowledge/clear conventions). Final document therefore describes alarm handling conceptually without asserting a specific state machine.
2. **Ericsson / Huawei / ZTE depth** — these vendors are certainly major representatives of the same Type in the market, but their operational documentation was unreachable here; no product-level claims are made about them in the final document beyond the Representatives/Sources note.
3. **Scope generality of core+transport** — "management spans core, radio and transport" is directly evidenced at Nokia only; PW is RAN-centric with core-adjacent gateway functions. Final document phrases scope variation as a variant axis.
4. **Slicing** — single-product evidence (Nokia); kept optional.
5. **Standards-layer confirmation** — O-RAN/TM Forum alignment is evidenced through Nokia's own pages claiming alignment; the O-RAN spec texts themselves were not fetched.

## Final Synthesis

A Mobile Network Management system is the operator's run-time management system for its deployed mobile network: it holds the live network's elements as a managed estate, and operates them through the joint configuration + fault + performance loop. Around that core, mature products add software management, zero-touch onboarding, SON automation, analytics, open APIs, and multi-vendor/multi-technology reach, with packaging varying from single-vendor nationwide NMS to cloud-native Open RAN orchestration. It is not the planning tool (design-time), not the service-assurance layer (monitors but cannot operate elements), not the OSS umbrella (fulfillment/BSS scope), and not enterprise IT network management (different object world).
