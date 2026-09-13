# Research Notes — Network Management

Research date: 2026-09-08
Leaf: Network Management (DIRECTORY.md §14 IT, Cloud & Infrastructure)
Slug: network-management

## Research Goal

Understand what "Network Management" is as an Application Type in the enterprise/campus IT sense — distinct from the sibling leaf Network Monitoring, from security-side network products (NDR, Network Security Platform), from the §19 telecom/fiber/EV-charging "network management" family, and from adjacent infrastructure Types (Infrastructure Monitoring, Server Management, Configuration Management, Infrastructure Automation, IPAM/DNS-DHCP, Load Balancer Management, CMDB/ITAM).

Produce a vendor-agnostic canonical model: what exists inside such a system, what users do with it, how work flows, which states/rules matter, and where the Type's boundaries lie.

## Initial Boundary (working hypothesis before research)

- Hypothesis: Network Management = the network operations team's system for managing an organization's OWN network device estate (switches, routers, firewalls, wireless APs/controllers): holding devices as managed records and operating them — configuration, provisioning, firmware, change control, recovery.
- Nearest neighbors: Network Monitoring (observe vs operate), Infrastructure Monitoring (entity inventory + health, read-only), NDR/Network Security (detection vs operation), Server Management (server estate vs network device estate), Infrastructure Automation Platform (automation content vs config-of-record), CMDB/ITAM/source-of-truth (records without operation), IPAM/DNS-DHCP (address/name/service records vs devices), Load Balancer Management (one device class vs the whole estate), §19 Telecom/Fiber/EV-charging network management (different subjects entirely).
- Known pre-hung flags to discharge or ratify:
  - load-balancer-management pass (§14, processed): "a load balancer is one managed device class there vs the entire record here — seam = distribution machinery inside this Type, device-estate breadth inside network management."
  - network-detection-response-ndr pass (§15, processed): boundary note for the unprocessed network-monitoring leaf — seam should be held at the question asked of the traffic, not telemetry.
  - metrics-monitoring / infrastructure-monitoring passes: flagged network-monitoring seam on "primary measured object".
- Open questions going in:
  1. Is the unit of record the device, the configuration, or the site/network?
  2. Does "management" require a write path to devices (push/apply), or is archive+diff enough?
  3. Is monitoring integration definitional? (Expected: no.)
  4. Is estate-scale operation (groups/fleet) definitional or just typical?
  5. Where exactly is the seam with Network Monitoring, given the market bundles both?

## Research Questions

1. What is the unit of record — device? configuration revision? site? policy?
2. How does configuration flow: retrieved from devices (pull/archive) vs authored in-system and pushed (controller)? Is one direction definitional?
3. Which operations constitute "management": onboarding/provisioning, config change, firmware/software distribution, compliance, recovery/rollback?
4. How do products organize the estate (sites, groups, ADOMs, hierarchy)?
5. What is the relationship to monitoring — bundled module, separate product, or separate Type?
6. What rules matter: change approval, RBAC, compliance policies, out-of-band change detection, auto-rollback?
7. Historical check: do 2000s-era device-management suites and open-source config-archival tools fit the same definition? What is the below-the-Type ancestor pole?

## Representative Products

Selected for market representation + documentation completeness + different product philosophy + different customer tier:

| Product | Pole | Philosophy | Customer tier | Evidence |
|---|---|---|---|---|
| Ubiquiti UniFi Network | single-vendor controller | self-hosted console / cloud gateway / hosted control plane, license-free | SMB → mid-market | Tier-1 help center (partial; root gated) |
| Fortinet FortiManager | single-vendor controller (firewall-centric estate) | on-prem/cloud appliance, NOC-SOC framing, policy packages | enterprise / MSSP | Tier-1 admin guide (docs.fortinet.com) |
| SolarWinds Network Configuration Manager | multi-vendor config lifecycle | Orion-platform module; backup/diff/compliance/bulk-push | mid-market → enterprise | Tier-1/2 product page + admin guide |
| ManageEngine Network Configuration Manager | multi-vendor config lifecycle | standalone Windows server; NCCM lifecycle | SMB → enterprise (distributed edition) | Tier-1/2 product page |

Boundary artifacts (not in-type, used for seam evidence):

- SolarWinds Network Performance Monitor (NPM) — the monitoring sibling sold as a separate product by the same vendor.
- NetBox — open-source "network source of truth" (IPAM+DCIM record layer), explicitly not an operator.

Rejected/considered: Juniper Mist (juniper.net docs 404 ×2 — dropped per network-constrained rule), Aruba Central (403 + transport error ×2 — dropped), Cisco Catalyst Center (403 — dropped). The cloud-managed enterprise WLAN pole is therefore evidenced only indirectly (via the controller-pole pattern in UniFi/FortiManager and market knowledge), and assertions about that pole are calibrated down.

## Sources

Tier-1 (official operational documentation):

- Fortinet — FortiManager 7.6 Administration Guide (key concepts, device manager, operations): https://docs.fortinet.com/document/fortimanager/7.6.7/administration-guide (fetched 2026-09-08)
- SolarWinds — NCM Administrator Guide: https://documentation.solarwinds.com/en/success_center/ncm/content/ncm_administrator_guide.htm (fetched 2026-09-08)
- Ubiquiti — Help Center article "Choosing the Right UniFi Control Plane": https://help.ui.com/hc/en-us/articles/30127033090071 (fetched 2026-09-08)

Tier-2 (official product pages):

- SolarWinds — Network Configuration Manager product page + FAQ: https://www.solarwinds.com/network-configuration-manager (fetched 2026-09-08)
- SolarWinds — Network Performance Monitor product page + FAQ: https://www.solarwinds.com/network-performance-monitor (fetched 2026-09-08)
- ManageEngine — Network Configuration Manager product page: https://www.manageengine.com/network-configuration-manager/ (fetched 2026-09-08)
- NetBox — official docs: https://docs.netbox.dev/en/stable/ (fetched 2026-09-08)

Unreachable (recorded limitation):

- Juniper Mist documentation (juniper.net 404 ×2)
- Aruba Central help center (403; help.cloud.arubanetworks.com transport error)
- Cisco Catalyst Center product page (403)
- Ubiquiti help center root and most article pages require sign-in (one public article fetched)

## Product Observations

### Ubiquiti UniFi Network (evidence layer A unless noted)

- Product shape: "UniFi Network" is the management application; it runs on a "control plane" — a Cloud Gateway (gateway hardware bundling the management software), a dedicated UniFi Console (CloudKey-class hardware), Official UniFi Hosting (vendor-hosted cloud), or self-hosted on the customer's own hardware. Vendor article: "Choosing the Right UniFi Control Plane" enumerates exactly these options. (A)
- Managed estate: UniFi access points, switches, and gateways. CloudKey Enterprise is documented as "a UniFi Network manager designed for larger networks, supporting up to 1,000 APs and switches." (A)
- Multi-site: "UniFi Site Manager" is a top-level help topic; sites are the organizing container for deployments. (A — article title/position; depth not fetched)
- Adoption model: devices are adopted by the controller; configuration (networks, WLANs, port profiles) is authored in the application and applied to adopted devices; firmware updates are pushed from the control plane. (A for control-plane/adoption framing; per-feature depth limited by sign-in wall — calibrated)
- License-free management is a stated positioning point ("scalable, license-free cloud management"). (A)
- The same control plane hosts sibling applications (Protect, Access, Talk, Connect) — network management is one application of a platform. (A)

### Fortinet FortiManager (evidence layer A)

- Positioning: "FortiManager is the NOC-SOC operations tool that was built with security perspective. It provides a single-pane-of-glass across the entire Fortinet Security Fabric." (A)
- Key concepts (admin guide TOC, Tier-1):
  - **Device Manager** — the managed-device workspace; devices organized in **ADOMs** (admin domains); device groups.
  - **Adding devices**: online devices via Discover mode (with Security Fabric authorization), offline "model devices" (added by serial number / pre-shared key / device template, CSV import), device blueprints, FortiGate HA clusters, automatic onboarding, **zero-touch and low-touch provisioning**. (A)
  - **Configuration through Device Manager**: "direct device database editing" and "indirect device database editing" — the manager holds a device database; edits can be applied directly or staged. (A)
  - **Policy packages** — configuration authored as policy objects in the manager, then **installed** to devices ("Install policy package", "Install device settings only", "Quick install (device db)", "Re-install policy"). (A)
  - **Retrieve configuration** / **Import configuration** — pulling device-side config back into the manager; **Auto-update and auto-retrieve**; **Auto-backup**. (A)
  - **Revert** — revision rollback of the manager-side device database. (A)
  - Firmware: "Updating the system firmware" (manager itself) and managed-device firmware lifecycle present in the guide structure. (A)
- The config-of-record lives in the manager's database; devices receive installs; device-side changes can be retrieved back. Both directions documented in one product. (A)

### SolarWinds Network Configuration Manager (evidence layer A)

- Definition (product-page FAQ): "A network configuration management tool automates the management of device configurations. Core tasks include device discovery, scheduling configuration backups, detecting and alerting on changes, comparing config versions to find differences, rolling back to previous versions, and auditing configs against compliance policies." (A)
- Capabilities (product page):
  - Scheduled automated config backups; "roll back to a last-known-good version after a failed change"; restore saved configurations. (A)
  - Real-time alerts on configuration changes; "identify and revert unauthorized modifications"; correlate changes with performance issues. (A)
  - Side-by-side config diffs; change history; last-known-good identification. (A)
  - "Push standardized configurations to hundreds of devices"; bulk deployment; device templates, custom templates, CLI commands, scheduled jobs across groups of devices; multi-vendor (routers, switches, firewalls). (A)
  - Compliance: policy reports for DISA STIG, NIST FISMA, HIPAA, PCI DSS; scheduled checks; remediation scripts. (A)
  - Firmware: firmware upgrade templates; vulnerability correlation with the NIST National Vulnerability Database; "support firmware upgrade operations from the same configuration-management workflow". (A)
- Packaging: NCM is a module of the self-hosted SolarWinds Platform ("adding devices, managing users… viewing monitored devices on maps" are platform features per the admin guide). (A)
- Family context: the vendor's own nav lists a "NETWORK MANAGEMENT" family — Network Performance Monitor, NetFlow Traffic Analyzer, IP Address Manager, Network Configuration Manager, Engineer's Toolset, Network Topology Mapper, Kiwi CatTools — i.e., "network management" is an umbrella over monitoring + config + IPAM products, with NCM and NPM as separately licensed products. (A)

### ManageEngine Network Configuration Manager (evidence layer A)

- Definition: "Network Configuration Manager is a multi-vendor network configuration and change management (NCCM) solution for switches, routers, firewalls and other network devices… helps automate and take total control of the entire life cycle of device configuration management." (A)
- Capabilities (product page):
  - Scheduled config backups; "All configuration data retrieved from devices are encrypted using AES 256-bits and stored in the database." (A)
  - Real-time change detection; instant notifications; "provision to initiate alerts or to automatically rollback device configurations upon identifying configuration changes." (A)
  - Configuration versioning & comparison (diff within a device or across devices). (A)
  - Compliance: define standards/policies, check configs for violations, remedial measures. (A)
  - Automation: "centrally applying configuration changes to devices in bulk" via configlets and scripts. (A)
  - Firmware vulnerability management: scan devices for firmware vulnerabilities (CVE ID, base score, severity), "remotely upgrade firmware". (A)
  - Change review & approval mechanism; role-based access control; user activity tracking ("who, what, when"); reports; color-coded alarms; scheduled jobs. (A)
  - Editions: Free (2 devices) → Professional (up to 10,000 devices) → Enterprise (up to 50,000 devices, distributed environment, central server aggregation). (A)
- Family context: related products listed — Network Monitoring (OpManager), NetFlow, OpUtils (switch port & IP address management), Firewall Management — and the page itself cross-sells: "Why stop at Configuration management when you can manage your entire network? Try OpManager Nexus." The vendor's own articulation separates config management from full network management (monitoring). (A)

### Boundary artifact — SolarWinds Network Performance Monitor (A)

- Definition: "Network performance monitoring is the practice of tracking availability, traffic, and device health so you can detect and resolve issues affecting network performance." Polls devices via SNMP; metrics: availability, response time, packet loss, bandwidth utilization, errors, hardware health; discovery, topology maps, alerts, capacity forecasting. (A)
- Same device estate as NCM (routers, switches, firewalls, wireless controllers), same platform — but the product's center is measurement/alerting, with no configuration write path. Sold separately from NCM. (A)

### Boundary artifact — NetBox (A)

- "NetBox is the leading solution for modeling and documenting modern networks… provides the ideal 'source of truth' to power network automation." Data model: sites/racks/devices/components/cables/IPAM/VLANs/VRFs etc. "Unlike general-purpose configuration management databases (CMDBs), NetBox has curated a data model which caters specifically to the needs of network engineers and operators." (A)
- Explicitly a record/documentation layer; it does not operate devices. This is the below-the-Type record pole: device estate of record WITHOUT the write path and WITHOUT config-as-substance. (A)

## Cross-product Comparison

| Dimension | UniFi Network | FortiManager | SolarWinds NCM | ManageEngine NCM |
|---|---|---|---|---|
| Unit of record | adopted device (AP/switch/gateway) in a site | managed device in an ADOM (+ model devices) | managed node (device) | managed device |
| Config held by system | yes — controller-held, applied on adopt/change | yes — device database + policy packages, installed to devices | yes — retrieved configs, versioned backups | yes — retrieved configs, encrypted storage, versioned |
| Config retrieval from devices | (adopt/state sync; depth unverified — sign-in wall) | yes — Retrieve/Import configuration, auto-retrieve | yes — scheduled backups | yes — scheduled backups |
| Config push to devices | yes — controller applies config | yes — Install policy package / device settings | yes — bulk push, templates, scripts | yes — bulk configlets/scripts |
| Diff / versioning | (config revision via controller; depth unverified) | yes — revisions, Revert | yes — side-by-side diffs, change history, last-known-good | yes — version comparison |
| Restore / rollback | (re-adopt/re-push; depth unverified) | yes — Revert | yes — rollback to last-known-good, restore | yes — rollback, incl. auto-rollback on change |
| Onboarding / provisioning | yes — adoption; cloud gateways | yes — discover, model devices, blueprints, zero-touch | yes — device discovery | yes — device add/discovery |
| Firmware/software management | yes — pushed from control plane | yes — managed-device firmware lifecycle | yes — firmware upgrade templates + NVD correlation | yes — vulnerability scan + remote upgrade |
| Compliance policies | (not observed in fetched docs) | policy packages as governed config objects | yes — DISA STIG/NIST/HIPAA/PCI reports | yes — policy definitions + checks |
| Change approval workflow | not observed | (governed via admin roles; not observed as explicit approval) | "support approval workflows" (feature text) | yes — change review & approval mechanism |
| Out-of-band change detection | not observed | yes — auto-retrieve/import | yes — real-time change alerts | yes — real-time detection + auto-rollback |
| RBAC | yes (platform roles; depth unverified) | yes (admin domains/roles) | yes (platform users) | yes — explicit RBAC page |
| Monitoring bundled | health/insight surfaces in-app (depth unverified) | FortiAnalyzer features toggleable in-product | separate product (NPM), same platform | separate product (OpManager) |
| Multi-tenancy / scale-out | sites; CloudKey Enterprise to 1,000 devices | ADOMs; MSSP posture | Orion platform scaling | Enterprise edition: distributed, 50k devices |
| Deployment | console hardware / cloud gateway / hosted / self-hosted | appliance / VM / cloud | self-hosted Windows platform module | self-hosted Windows server |

Cross-product commonalities (evidence layer B):

- Every sampled product holds a persistent, individually identified record per managed network device, organized into groups/sites/domains. (B: 4/4)
- Every sampled product holds device configuration as system-held state that outlives sessions and is applied to devices. (B: 4/4)
- Every sampled product can apply configuration changes to devices through the system (write path). (B: 4/4)
- Config versioning + comparison + restore/rollback appears in every product where documentation depth allowed verification (FortiManager, SolarWinds NCM, ManageEngine NCM; UniFi depth unverified). (B: 3/4 verified)
- Device onboarding/provisioning (discovery, adoption, zero-touch variants) in all. (B: 4/4)
- Firmware/software image management in all. (B: 4/4)
- RBAC in all. (B: 4/4)
- Compliance policy checking in the two multi-vendor config products; policy-governed config objects in FortiManager. (B: 3/4)
- Out-of-band change detection/alerting in 3/4 (not observed for UniFi in fetched docs).
- Monitoring is NOT the center anywhere: two vendors sell monitoring as a separate product; controllers include health surfaces but their documented center is device operation. (B)

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (three jointly-held structures)

1. **The network device estate of record.** Persistent, individually identified records of the organization's own network infrastructure devices — switches, routers, firewalls, wireless APs/controllers, and similar network equipment — each carrying its management-plane reachability (management address, credentials or adopted/registered state) and organized into sites/groups/domains. The subject is the network's own devices. Remove → IT asset inventory / CMDB / source-of-truth (NetBox pole).

2. **Device configuration as the managed substance.** The system holds each device's operative configuration as state that outlives any single session: retrieved from devices, authored in-system, or controller-held (direction is a variant); preserved as versioned revisions/backups; comparable (diffs across devices and over time); restorable/re-applicable. The configuration — not merely the device record — is what is managed. Remove → bare config-file repository, or the record layer alone.

3. **The write path to devices.** Configuration changes are applied to devices through the system as the normal course of operation — to one device, a group, or the fleet; via direct edit, template/configlet, or controller-held policy. The system is an operator of the estate, not only an observer or an archivist. Remove → read-only monitoring (Network Monitoring) or a static config archive.

Jointly-held load-bearing tests:

- 1 alone = asset inventory / CMDB / source-of-truth
- 2 without 1 = config file repository / version control
- 3 without 1+2 = ad-hoc CLI work / automation scripts (Infrastructure Automation territory)
- 1+2 without 3 = config archive (RANCID-class pole — the below-the-Type ancestor)
- 1+3 without 2 = onboarding + firmware push without config semantics (drifts toward endpoint-management shape)
- 2+3 without 1 = templates/policies with no device records to manage

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Device discovery / onboarding, incl. zero-touch provisioning
- Firmware / software image management (upgrade templates, vulnerability correlation)
- Configuration compliance policies and audit reports (DISA STIG / PCI DSS / HIPAA-class)
- Out-of-band change detection with alerts (and auto-rollback in some products)
- Change review / approval workflows
- RBAC and user-activity audit ("who/what/when" of changes)
- Dashboards, device health/status surfaces, topology views
- Scheduled jobs (backups, compliance checks, config pushes)
- Config/device search; reports (inventory, changes, compliance)
- Integrated monitoring surfaces (health/insight) — present but never the center

### L2 — Variant / Optional Structure

- Product philosophy: single-vendor controller (estate = that vendor's devices; config authored in-system) vs multi-vendor config manager (estate = heterogeneous devices; config retrieved from devices)
- Deployment: cloud-managed SaaS / vendor-hosted / self-hosted controller appliance / on-prem server software
- Estate scope: wired + wireless + gateway (controller pole) vs config-lifecycle-only (NCM pole) vs firewall-centric estate (FortiManager)
- Scale-out: distributed enterprise editions, central aggregation, multi-tenant MSP postures (ADOM-class)
- SD-WAN orchestration as a managed overlay
- Intent-based / AI-assisted configuration (era machinery; not observed in fetched docs for this sample — held at variant strength)
- License model: license-free management (UniFi) vs licensed modules

### L3 — Vendor-specific (research notes only)

- FortiManager: ADOMs, policy packages, Security Fabric authorization, model devices, device blueprints, FortiAnalyzer-features toggle
- UniFi: Cloud Gateway / Console / Official Hosting / Self-Hosted control-plane taxonomy; sites; sibling applications (Protect/Access/Talk/Connect) on one control plane; CloudKey Enterprise capacity framing
- SolarWinds: Orion platform module packaging; NIST NVD correlation; NetPath/PerfStack belong to NPM (monitoring sibling), not NCM
- ManageEngine: configlets; AES-256 config storage claim; Free/Professional/Enterprise edition ladder (2 / 10k / 50k devices); OpManager Nexus cross-sell
- NetBox (boundary artifact): plugins, custom fields, REST/GraphQL APIs — record-layer extensibility

## Historical / Market-Sample Check (§24)

- 2000s device-management suites (CiscoWorks-class: device inventory + config archive + software image management + scheduled config jobs): satisfy all three L0 legs conceptually — no cloud, AI, SDN, or SaaS required. Held as conceptual inference (C), not Tier-1 (legacy docs not fetched).
- Early-2000s open-source config archival tools (RANCID-class: device list + periodic config retrieval + version-controlled archive + change diffs): satisfy legs 1–2 but have no write path → correctly the below-the-Type ancestor pole. Conceptual (C).
- 1990s SNMP managers: predominantly read-only monitoring → belong to the Network Monitoring lineage, not this Type. Conceptual (C).
- Regional/platform-native products (Huawei/H3C-class enterprise network managers) follow the same controller pattern; not fetched — held at variant strength.
- Conclusion: the definition names no era machinery (no SNMP, no cloud, no AI, no SD-WAN, no specific vendor protocol). SNMP is a common transport for the management connection (NPM/NCM pole), while controller poles use vendor-proprietary protocols — so the management connection's protocol is explicitly NOT definitional.

## Vendor-specific Findings

- FortiManager's "NOC-SOC operations tool" framing is a straddling posture: it manages devices (this Type's center) while marketing security-operations adjacency. The documented center remains device management (Device Manager, policy packages, install/retrieve/revert).
- SolarWinds and ManageEngine both articulate the config-vs-monitoring split in their own product architecture (NCM vs NPM; NCM vs OpManager) — the strongest available Tier-1 evidence for the Network Management vs Network Monitoring seam.
- UniFi's control-plane taxonomy (gateway-bundled / console / hosted / self-hosted) shows the management software is separable from any particular hardware — useful evidence that "management application" is the Type, deployment is a variant.
- NetBox's own positioning ("source of truth to power network automation", "unlike general-purpose CMDBs") documents the record layer as a distinct, deliberately non-operational product — the cleanest below-the-Type pole.

## Boundary Findings

- **vs Network Monitoring (§14 sibling, unprocessed)** — the critical seam. Both Types organize on the same device estate. Seam = the write path vs the read path: Network Management applies configuration/firmware/provisioning to devices; Network Monitoring measures availability/performance and alerts. Two vendors sell them as separate products over the same platform (SolarWinds NCM vs NPM; ManageEngine NCM vs OpManager) and bundle them in suites — feature lists cannot separate the leaves; the action center must. Pre-hung flag for the network-monitoring pass: hold the seam at write-vs-read, not at telemetry or device class. Also recorded: the market's umbrella term "network management" spans monitoring + config + IPAM (SolarWinds' own "Network Management" product family and "Network Monitoring and Management" solutions page) — umbrella usage is naming, not a Type boundary.
- **vs Network Detection & Response / Network Security Platform (§15)** — detection/response vs estate operation. FortiManager is the straddling pole (NOC-SOC framing) but its documented center is device management. Firewall configuration management belongs here; threat detection belongs to security Types.
- **vs Load Balancer Management (§14, processed)** — ratifies that pass's pre-hung flag: distribution machinery (listener/pool/health-gated rotation) is the entire record there; a load balancer is one device class in the estate here. Seam = distribution machinery inside this Type, device-estate breadth inside network management.
- **vs Infrastructure Monitoring (§14, processed)** — infra monitoring's entity inventory includes network devices as one entity class, with per-entity health states; read-only. This Type's estate is exclusively network devices AND holds the write path. A Zabbix-class infra monitor is outside this Type.
- **vs Infrastructure Automation Platform (§14, processed)** — automation content × targets × governance there (no per-device config of record); device estate + config-of-record here. Ansible-class network automation is that Type; config backup/diff/restore/compliance with a device registry is this Type. They interoperate (automation tools consume source-of-truth records; NCM-class products add scheduled jobs/scripts).
- **vs CMDB / IT Asset Management / source-of-truth (NetBox pole)** — records without a write path and without config-as-substance → outside this Type. NetBox documents this explicitly.
- **vs Server Management Platform (§14, unprocessed)** — seam = managed object class: network infrastructure devices vs servers/endpoints. RMM-class tools manage both; that pass should hold the estate-subject seam. Pre-hung flag.
- **vs Configuration Management (§14 leaf, unprocessed)** — network device configuration management is THIS Type's center; that leaf should scope to system/application configuration (server-side config drift). Pre-hung flag.
- **vs IP Address Management / DNS & DHCP Management (§14 siblings, unprocessed)** — address/name/service records vs device estate. Integrated in suites (SolarWinds IPAM as a sibling product; ManageEngine OpUtils) — seam = managed object. Pre-hung flag.
- **vs Endpoint Management / UEM (§14)** — endpoints (laptops/phones) vs network infrastructure devices. Controllers manage APs/switches/gateways, not user endpoints.
- **vs §19 Telecom Network Management / Mobile Network Management / Fiber Network Management / EV Charging Network Management** — different subjects: carrier network elements and OSS processes; the physical fiber plant (geospatial, strand-level); charger fleets (CPO). This Type's subject is the enterprise/campus IT network device estate. The shared word "network" is domain vocabulary, not a Type identity.
- **vs DCIM (§14)** — physical infrastructure (power/cooling/racks) vs network devices; NetBox merges IPAM+DCIM at the record layer, which is exactly why the record layer is not this Type.
- **vs CDN Management (§14, processed)** — CDN edge service configuration vs the internal network device estate.

## Uncertainties

- Cloud-managed enterprise WLAN/campus pole (Aruba Central, Cisco Catalyst Center, Juniper Mist) unreachable (403/404/transport). The controller pattern is evidenced via UniFi/FortiManager; claims about intent-based networking, AI assistance, and cloud-controller specifics are held at variant strength and NOT asserted in the final document beyond the generic controller pattern.
- UniFi's per-feature depth (config revision mechanics, change detection, RBAC granularity) unverified — help center articles require sign-in. UniFi claims in the final document are limited to the control-plane/adoption/estate facts that were fetched.
- Whether change-approval workflows are universal: verified in ManageEngine (explicit feature) and hinted in SolarWinds ("support approval workflows"); not observed in FortiManager/UniFi fetched docs → held as common, not definitional.
- Whether out-of-band change detection is universal: verified in 3/4; not observed for UniFi → held as standard capability, not definitional.
- Historical claims (CiscoWorks-class suites, RANCID) are conceptual inference from model knowledge, not Tier-1 fetches — used only for the §24 check, not as evidence for any precise claim.
- The exact boundary of "network management" as an umbrella marketing term varies by vendor; recorded as naming observation, not resolved here.

## Final Synthesis

Network Management (§14) is the network team's device-estate operating system. Its defining core is three jointly-held structures: the network device estate of record; device configuration as the managed substance (versioned, comparable, restorable — retrieved, authored, or controller-held); and the write path to devices (changes applied through the system as normal operation). Remove the write path → Network Monitoring or a config archive. Remove the config substance → asset inventory/source-of-truth. Remove the device estate → config tooling with nothing to manage. The market realizes the Type in two poles — single-vendor controllers (config authored in-system, applied to adopted devices) and multi-vendor config managers (config retrieved from devices, versioned, pushed back) — plus deployment variants (cloud-managed, appliance, self-hosted server). Monitoring, compliance, approval workflows, firmware, zero-touch onboarding, RBAC are standard capabilities, not the definition. The seam with Network Monitoring must be held at write-vs-read, and the §19 "network management" leaves are different subjects sharing vocabulary.
