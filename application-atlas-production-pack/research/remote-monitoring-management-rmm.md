# Research Notes — Remote Monitoring & Management / RMM

Research date: 2026-09-09

## Research Goal

Understand what a Remote Monitoring & Management (RMM) application actually is from real products: its unit of record, its monitoring model, its management-action model, its automation model, who operates it (MSP technicians vs internal IT admins), and where its boundaries lie against Endpoint Management/UEM, Network Monitoring, Infrastructure Monitoring, Patch Management, PSA/MSP Management Platforms, Remote Support, and EDR.

## Initial Boundary

Initial hypothesis: RMM is a central console through which an IT operator observes the health of many distributed devices (workstations, servers, network devices) and takes management actions on them remotely, typically via an installed agent. Dominant users: MSP technicians managing many client environments; internal IT admins managing their organization's fleet.

Easily confused with: Endpoint Management/UEM (policy/compliance for user endpoints), Network Monitoring (network health via SNMP/flow), Infrastructure Monitoring/APM (observability without device-level management actions), Patch Management (a capability inside RMM), PSA/MSP Management Platform (the service business around the devices), Remote Support (interactive help sessions), EDR (security telemetry/response).

## Research Questions

1. What is the unit of record? How do devices become managed (agent vs probe/SNMP enrollment)?
2. What does the console show, and how are devices organized (clients/sites/organizations, groups/folders)?
3. What is monitored (checks: availability, metrics, services, events, custom/script-based), and how do alerts flow (condition → alert → notification → resolution → auto-remediation)?
4. What management actions execute remotely (remote control, shell/script, patching, software deployment, service/process/file/registry operations, reboot/wake)?
5. How does automation work (policies applied to device groups, scheduled automations, alert-triggered auto-healing)?
6. How does the MSP posture differ from the internal-IT posture (multi-tenancy, client separation, ticketing/billing integration)?
7. Where are the boundaries against the neighboring Types listed above?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

1. **Atera** — all-in-one MSP platform (RMM + PSA + remote access + billing), per-technician pricing, SMB-MSP tier. Deep operational documentation (support center).
2. **Action1** — cloud-native RMM positioned for internal IT departments (with MSP multi-tenancy), patch/vulnerability-centric. Deep operational documentation.
3. **Pulseway** — mobile-first RMM, SMB tier, Kaseya-owned. Product-page evidence only (help center unreachable).
4. **ManageEngine RMM Central** — MSP-focused RMM with strong network-device orientation (Zoho family). Product-page evidence only.

Rejected/abandoned samples: NinjaOne (docs.ninjarmm.com transport error ×1; ninjarmm.com/support 404; ninjarmm.com/products/rmm/ 404 — abandoned after 3 attempts), N-able N-sight RMM (documentation.n-able.com 403), Kaseya VSA (help.kaseya.com transport error; kaseya.com/products/vsa/ 404), Syncro (help center returned empty shell), Datto RMM (rmm.datto.com/help returned empty).

## Sources

- Atera Support Center (Tier 1): https://support.atera.com/hc/en-us — sections: RMM (https://support.atera.com/hc/en-us/sections/12842741667228-RMM), Agent-monitored devices (…/13581246051868), Alerts (…/13573176961820), Live manage (…/13581284010268); FAQ/pricing pages
- Action1 Documentation (Tier 1): https://www.action1.com/documentation/ — Getting Started (…/getting-started-with-action1/), Alerts (…/alerts/), plus full doc map (endpoints, patch management, automation, remote desktop, multi-tenancy, audit)
- Pulseway (Tier 2): https://www.pulseway.com/ — product page (RMM features, add-ons, solutions)
- ManageEngine RMM Central (Tier 2): https://www.manageengine.com/remote-monitoring-management/ — product page (discover/manage/monitor/secure frame, feature list)

Source-access limitation: NinjaOne, N-able, Kaseya VSA, Syncro, Datto official documentation could not be fetched from the research environment. Cross-product claims below rest on 2 products with Tier-1 operational documentation (Atera, Action1) plus 2 products with Tier-2 product-page evidence (Pulseway, RMM Central). Claims are calibrated accordingly; no precise operational details are asserted beyond what fetched pages state.

## Product A — Atera (Tier 1, evidence layer A)

### Key observations

- The RMM module's own documentation structure names the capability set: *Atera agent / Agent-installed devices / Agent-monitored devices / Remote access / Alerts / Patch management / Software management / Scripts / Assets / Live manage / RMM FAQs*.
- **Enrollment**: an agent is installed on Windows/Mac devices ("agent-installed devices"). Non-computer devices are monitored without an agent: SNMP devices (with SNMP templates and OID management), HTTP devices (websites), TCP port devices, generic devices (switches, printers, UPS), and hypervisors (Hyper-V/ESX). So the device population = agent-managed computers + probe/SNMP-monitored network/infrastructure devices.
- **Organization**: devices are organized under *customers* (MSP clients) with *sites* and *folders*; threshold profiles are assigned at customer/site/folder/agent level. Custom fields and saved device views/filters exist.
- **Monitoring/alerts**: threshold profiles define monitored conditions (disk, events, online status, script-based thresholds); alerts appear on an Alerts page; alerts can be emailed; sound alerts exist; alerts can create/assign *tickets* automatically (PSA integration); **auto-healing scripts** run in response to alerts; alert time intervals control evaluation.
- **Management actions ("Live manage")** — per-device tool set: SSH, Service manager, File transfer, Task manager, Software inventory, Patch management, PowerShell, Event viewer, User activity, Command prompt, Run script, Registry editor; plus one-click AV installation (Webroot).
- **Patch management** and **software management** as first-class modules (Windows/Mac/Linux).
- **Scripts**: script library + shared script library; scripts run on demand or via automation.
- **Assets**: IT asset records alongside devices.
- **All-in-one posture**: RMM + ticketing/PSA + billing + CRM + customer portal in one product; per-technician pricing with unlimited devices/customers; positioned at both MSPs and IT departments; SaaS.
- Separate **Network Discovery** module (product-level, discover devices on client networks).

## Product B — Action1 (Tier 1, evidence layer A)

### Key observations

- **Enrollment**: agent installed on Windows/macOS/Linux endpoints — manually (per-OS installers preconfigured with the organization's connection parameters), or at scale via Microsoft Intune, Group Policy, PC images, or the "Action1 Deployer". Agent runs as a service (Windows, LOCAL SYSTEM) or daemon (macOS/Linux). Agent remains idle unless patching or a status refresh is needed. Cloud regions (North America / Europe / Australia); firewall allowlists documented.
- **Console**: *Endpoints* page shows all endpoints with real-time system info — missing updates, installed software, hardware details; *Dashboard* for fleet-level health (vulnerability remediation compliance, pending deployments, required reboots). Endpoint groups; custom attributes.
- **Organization**: *Organizations* and *Enterprises*; endpoints can be moved between organizations; **multi-tenancy documented for MSPs and enterprises**; branding (white-labeling) for MSPs.
- **Patch management** (the flagship module): review and approve updates with an approval workflow; deploy-updates wizard with reboot options and scheduling; automated patch-management policies; **update rings** for phased rollout; installed-updates reports and patch-compliance reporting.
- **Vulnerability management**: detect CVEs, configure remediation SLAs, remediate vulnerabilities.
- **Software deployment**: app-store catalog + custom packages (multi-file, per-OS install settings), P2P distribution technology, uninstall.
- **Automation**: "Automations" — create an automation (e.g., deploy critical updates N days after release), target endpoints/groups, schedule, run/stop, view history, pause deployments. Script library (add/edit/delete/use scripts). Remote actions: restart endpoints, run scripts on remote computers, remote desktop (browser-based).
- **Reports & alerts**: built-in reports (software inventory, hardware inventory, endpoint security & configuration, vulnerability management), custom reports, scheduled report delivery; **alerts are rules based on queries/reports** — trigger on created/deleted/modified events with filters/logic, delivered by email to Action1 users; uptime alerts; custom data sources can feed alerting. (Precise suppression limits exist in-product; details kept here, not in the final document.)
- **Access & governance**: users/roles/permissions with Organization/Enterprise scope, MFA, SSO (Entra ID, Duo, Okta, Google), audit trail, IP allow list; documented agent data collection.

## Product C — Pulseway (Tier 2, evidence layer A- [product page only])

### Key observations

- Self-labels "RMM Software | Remote Monitoring and Management"; positioning: "manage workstations, servers, and network devices from anywhere"; mobile-first ("An IT Management Solution That You Can Take Anywhere"; mobile app as command center).
- Core platform: **Monitoring & Alerting** (Windows, Mac, Linux; network devices & IoT), **Remote Control** (unlimited sessions, multi-screen), **Patch Management** (OS + third-party apps), **Scripting & Automation** (scripting, auto-remediation).
- Add-ons: security (antivirus, ransomware detection, phishing defense), business operations (IT documentation, ticketing, NOC & helpdesk), backup (endpoint backup, appliance BCDR, SaaS backup).
- Solutions: MSPs, IT departments, education. Owned by Kaseya (co-branding on site).

## Product D — ManageEngine RMM Central (Tier 2, evidence layer A- [product page only])

### Key observations

- Self-labels "Remote Monitoring and Management (RMM) Software for MSPs".
- Canonical 4-step frame stated on the product page: **Discover → Manage → Monitor → Secure**.
- **Discover**: network discovery of "all types of network devices such as servers, routers, storage devices, virtual machines… including customer devices like laptops, mobiles" via AD, Layer-2 mapping, subnet scanning.
- **Monitor**: device metrics, performance, bandwidth, alarms "of multiple customer networks"; protocols SSH, WMI, SNMP for network devices (servers, switches, WLCs, virtual devices).
- **Manage**: application management, remote troubleshooting, IT asset inventory "from a single console"; server management across Windows/Linux/Solaris/Unix/VMware.
- **Secure**: patch deployment (Windows/Mac/Linux + 1000+ third-party apps), access restriction, security policies, per-customer configuration.
- Also: real-time alerting, remote control (multi-user collaboration, file transfer, video recording), MDM, ITAM, analytics/reporting (100+ out-of-box reports).
- MSP positioning: "manage and monitor multiple client accounts, domains and networks from a unified console".

## Cross-product Comparison

| Dimension | Atera | Action1 | Pulseway | RMM Central | Reading |
|---|---|---|---|---|---|
| Unit of record | Device (agent-installed) + agent-monitored non-agent devices (SNMP/HTTP/TCP/generic) + assets | Managed endpoint (agent on Win/macOS/Linux) | Workstations, servers, network devices & IoT | Servers, routers, storage, VMs, laptops, mobiles (discovered) | **Device as enrolled managed unit — invariant**; agent is the dominant substrate, probes/SNMP for non-computer devices |
| Central console | Web console; device list w/ filters, views, custom fields | Web console; Endpoints page + Dashboard, real-time | Web + **mobile app** console | "Single console" for all clients | **Central operator console — invariant**; form factor varies |
| Monitoring | Threshold profiles (disk, events, online status, script-based), SNMP/OID metrics | Query/report-based alert rules, uptime alerts, custom data sources | Monitoring & alerting across OS + network/IoT | Metrics, performance, bandwidth, alarms; SSH/WMI/SNMP | **Continuous monitoring with alerting — invariant**; check catalog varies |
| Alerts flow | Alert page → email/sound → auto-create ticket → auto-healing script | Alert rule → email to users; uptime alerts | Alerting + auto-remediation | Real-time alerting, email | **Alert → notification → response — invariant**; response can be human or automated |
| Management actions | Live manage: SSH, services, task mgr, files, PowerShell/CMD, registry, event viewer, run script, patch, AV install | Remote actions: restart, run scripts, remote desktop; patch deploy; software deploy/uninstall | Remote control, patching, scripting | Remote control (multi-user, file transfer), patching, policies | **Remote management actions from console — invariant**; action catalog varies |
| Patch management | Module (Win/Mac/Linux) | Flagship module: approval workflow, policies, update rings, compliance reports | Module (OS + 3rd party) | Module (OS + 1000+ 3rd party) | **Common mature structure**, not definitional (standalone patch tools exist) |
| Software deployment | Software management module | App store + custom packages + P2P | — (in scripting/automation scope) | Application management | Common mature structure |
| Automation | Scripts + auto-healing + threshold automation | Automations (scheduled, targeted, history) + script library | Scripting + auto-remediation | Patch automation, security policies | Common mature structure; alert-triggered auto-remediation appears in 3/4 |
| Organization containers | Customers → sites → folders; threshold profiles at each level | Organizations/Enterprises; endpoint groups; multi-tenancy for MSPs | Client environments (MSP solutions) | Multiple client accounts/domains/networks | **Container hierarchy — common mature structure**; MSP multi-tenancy is the dominant but not sole posture (Action1 sells to internal IT; Pulseway/RMM Central also sell to IT departments) |
| Remote control | Remote access module | Browser-based remote desktop | Remote control (multi-screen) | Remote control (collaboration, recording) | Common mature structure; the most iconic single action |
| Security add-ons | AV install (Webroot), AV integrations | Vulnerability management, security posture reports | Antivirus, ransomware, phishing | Access restriction, security policies | Optional/variant; overlaps EDR/AV territory |
| PSA/ticketing | Built-in (tickets from alerts, billing, CRM, portal) | Jira connector; ticketing rules | Ticketing add-on, NOC, IT documentation | — | Optional/variant (all-in-one vs standalone posture) |
| Deployment | SaaS | SaaS (cloud regions) | SaaS | SaaS (Zoho family) | In this sample all cloud; legacy-generation RMM (not sampled, docs unreachable) historically offered on-prem — held as variant, not asserted from evidence |

## Canonical Model

```text
Managed device (enrolled unit of record)
  ├── agent substrate (installed service/daemon) — dominant implementation
  ├── probe/SNMP substrate (network devices, websites, ports, hypervisors) — common for non-computers
  └── organized in containers (customer/site/organization, groups/folders)
        │
Central operator console
  ├── device inventory (status, hardware/software, custom fields)
  ├── monitoring checks (availability, metrics, services, events, script-based)
  ├── alerts (condition → alert → notification → resolution)
  └── management actions (remote control, shell/script, patch, software deploy,
                         service/process/file/registry ops, reboot/wake)
        │
Automation layer (policies over groups; scheduled automations; alert-triggered auto-remediation)
```

## L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being an RMM:

1. **Enrolled managed devices** — devices bound to the system as individually addressable managed units (agent- or probe-enrolled), organized in a fleet inventory. Remove → an unowned dashboard/data feed (asset inventory or monitoring without a managed fleet).
2. **Continuous monitoring with alerting** — the console continuously observes device state against defined conditions and raises alerts that demand a response. Remove → a remote-execution/remote-access tool with no proactive observation.
3. **Remote management actions executed from the console against devices** — operator-initiated changes carried out on devices without physical presence (remote control, script execution, patching, software deployment). Remove → pure monitoring = Network Monitoring / Infrastructure Monitoring territory.

Jointly-held load-bearing checks:
- 1 alone = asset inventory / device registry
- 2 alone = monitoring platform (network/infrastructure monitoring)
- 3 alone = remote access / remote support tool
- 1+2 without 3 = monitoring with no remediation path
- 1+3 without 2 = break-fix tooling with no proactive observation
- 2+3 without 1 = scripts and dashboards with no managed fleet

Anti-overfit: the **agent** is NOT definitional (agentless SNMP/probe monitoring of network devices is in-type in Atera and RMM Central; the invariant is enrollment/binding of the device, however implemented). **Patch management** is NOT definitional (it is one management action; standalone patch tools exist as a separate Type). **MSP multi-tenancy** is NOT definitional (internal-IT single-organization posture is in-type — Action1's primary positioning). **Remote control** alone is NOT definitional (it is one action inside the management leg).

## L1 — Common Mature Structure

- agent as the standard substrate for computers (service/daemon reporting to the console)
- device inventory: hardware, installed software, OS state, custom fields/attributes
- container hierarchy: customers/sites (MSP) or organizations/sites + device groups/folders
- patch management for OS + third-party software, with approval workflows and compliance reporting
- software deployment from a catalog/repository plus custom packages
- script library + scheduled automations + alert-triggered auto-remediation
- interactive remote control (remote desktop / SSH)
- reporting (built-in + custom, scheduled delivery)
- role-based access, MFA/SSO, audit trail of actions
- alert→ticket handoff into PSA/ITSM tooling

## L2 — Variant / Optional Structure

- tenancy posture: MSP multi-client separation vs internal-IT single organization
- network-device monitoring depth (SNMP templates/OIDs, bandwidth, L2 mapping)
- bundled security: AV management, ransomware detection, vulnerability management
- bundled backup / BCDR
- MDM for mobile devices
- all-in-one bundling: PSA/ticketing/billing/CRM/customer portal vs standalone RMM
- deployment model: cloud SaaS vs on-prem (legacy generation; not directly evidenced in this sample)
- mobile console as first-class surface
- white-labeling/branding for MSPs
- NOC services (vendor-operated monitoring as a service)

## L3 — Vendor-specific Structure (research notes only)

- Atera: per-technician pricing (unlimited devices/customers), AI Copilot / Robin autonomous-IT branding, Webroot one-click install, sound alerts
- Action1: P2P patch distribution, update rings, alert suppression limits (10 alerts/hour/endpoint), 60-minute default reboot grace window, cloud regions NA/EU/AU, Jira connector, free edition
- Pulseway: mobile-app-first console, Kaseya ownership, NOC services
- RMM Central: ML-based forecast reports, Layer-2 mapping, 100+ out-of-box reports, Zoho/MangeEngine family packaging (MSP Central)

## Boundary Findings

| Neighboring Type | Relationship | Distinction (what to remove / what makes it the other Type) |
|---|---|---|
| Endpoint Management / UEM | adjacent, heavy overlap on endpoints | UEM centers on policy/profile/compliance lifecycle for **user endpoints** (esp. mobile), app config, enrollment programs; RMM centers on **operator-side observation + remediation** of a heterogeneous fleet (servers + workstations + network devices) with monitoring/alerts as the driver. Remove continuous monitoring/alerting + fleet-operations posture → UEM territory. RMM Central ships an MDM module — bundling, not identity. |
| Network Monitoring | adjacent | Network monitoring centers on network health (devices, links, bandwidth, protocols) via SNMP/flow with no device-level management actions; RMM's center is computers/servers as manageable units. RMM commonly includes some SNMP device monitoring (Atera, RMM Central) — common structure, not the center. Remove management actions → network monitoring. |
| Infrastructure Monitoring / APM | adjacent | Observability platforms watch services/apps/infra and alert; they do not execute per-device management actions (no patching/remote control/script execution as first-class objects). Remove the management-action leg → infrastructure monitoring. |
| Patch Management | capability-overlap | Standalone patch tools center on update catalogs, approval, deployment. In RMM, patching is one management action bound to the enrolled fleet and monitoring loop. A patch-only product lacks the monitoring/alert leg → not an RMM. |
| MSP Management Platform / PSA | bundling neighbor | PSA centers on the service business (tickets, clients, contracts, time, billing); RMM centers on the devices. All-in-one products (Atera) bundle both; the RMM core remains the device-operations layer. Remove device monitoring/actions → PSA. |
| Remote Support / Remote Access | adjacent | Remote-support tools center on interactive sessions to help a person; RMM centers on the fleet with monitoring + unattended management. Remote control is one action inside RMM. A tool with only sessions → remote support, not RMM. |
| EDR / Endpoint Protection | security neighbor | EDR centers on threat telemetry, detection, and response; RMM centers on IT operations. RMM may manage third-party AV (Atera/Webroot) or add ransomware detection (Pulseway) — optional bundling. Remove operations, keep threat detection → EDR. |

"去掉什么就变成另一个 Type" 判据：去掉管理动作腿 → 监控平台（Network/Infrastructure Monitoring）；去掉监控告警腿 → 远程接入/远程支持工具；去掉设备注册（enrollment）→ 无主数据仪表盘；把中心从设备运维换成端点策略/合规生命周期 → UEM；把中心从设备换成服务业务（工单/账单）→ PSA。

## Historical / Market-Sample Check

The RMM label descends from the 2000s MSP tooling generation (Level Platforms, early N-able, Kaseya VSA, LabTech — none directly fetchable in this pass): agent installed on Windows machines, central dashboard, threshold alerts, scripts, patching. That generation satisfies the same triad (enrolled devices + monitoring/alerts + remote management actions) with no cloud, no mobile app, no AI. Platform-native ancestors (LANDesk/Altiris-style management suites) evolved toward the Endpoint Management/UEM family — consistent with the boundary drawn above (their center is policy/compliance lifecycle, not monitoring-driven fleet operations). The triad therefore survives the historical check; nothing in the L0 depends on cloud delivery, mobile consoles, or modern security add-ons.

## Uncertainties

- On-premises RMM deployment could not be verified from fetched sources in this pass (all four sampled products are cloud/SaaS); legacy-generation products historically offered on-prem. Held as variant with low-confidence sourcing; not asserted in the final document beyond "deployment models vary".
- NinjaOne, N-able N-sight, Kaseya VSA, Datto RMM, Syncro documentation unreachable — the sample skews toward cloud-native products. Cross-product claims rest on 2 Tier-1 + 2 Tier-2 sources.
- Exact alert-state vocabularies (open/acknowledged/resolved etc.) vary per product; only Atera's alert→ticket and auto-healing flows and Action1's rule-based alert model were directly observed. State names are not asserted as industry-standard in the final document.
- Whether "RMM" and "Endpoint Management" should be one Type or two remains a market-blur question (Action1 markets itself as an "endpoint management platform" while its documentation is RMM-shaped). Recorded as a taxonomy observation, not resolved here.

## Final Synthesis

An RMM is the IT operator's remote-operations system for a fleet of devices. Its defining core is the joint presence of (1) enrolled managed devices held in a fleet inventory, (2) continuous monitoring that raises alerts demanding response, and (3) management actions executed remotely from a central console. The agent is the dominant but not definitional substrate; patching, software deployment, scripting/automation, remote control, reporting, and access governance are the standard capability set; MSP multi-tenancy, all-in-one bundling, security add-ons, and mobile consoles are variants. The Type sits between monitoring platforms (which observe but do not act) and endpoint management (which manages user-device policy but does not run monitoring-driven fleet operations), with PSA as the business layer that frequently wraps it.
