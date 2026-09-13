# Research Notes — Server Management Platform

Research date: 2026-09-09
Slug: server-management-platform
Directory leaf: Server Management Platform (§14 IT, Cloud & Infrastructure)

## Research Goal

Understand what a "Server Management Platform" actually is as an Application Type: what the managed object is, what the platform does to it, how work flows, and where the Type's boundaries lie against the dense cluster of already-processed §14 siblings (RMM, UEM, Patch Management, Configuration Management, Infrastructure Automation, IaC, CMP, Virtualization/Container/K8s Management, Infrastructure Monitoring, Network Management, DCIM, HCI, ITOM, CMDB/ITAM).

## Pre-hung Flags From Sibling Passes (must be honored)

1. **network-management (§14, 2026-09-08)**: "server-management-platform — seam = managed object class (network infrastructure devices vs servers/endpoints); RMM-class tools manage both, hold the estate-subject seam."
2. **network-monitoring (§14, 2026-09-09)**: "server-management-platform (estate-subject seam echoed: network infrastructure devices vs servers/endpoints)."
3. **patch-management (§14, 2026-09-09)**: "FLAG for unprocessed server-management-platform — patching is one slice of server ops; Satellite straddle (provisioning+patching+config) = suite drift zone, same pattern as UEM/Endpoint Central."
4. **infrastructure-monitoring (§14, 2026-09-08)**: "vs Server Management (observation plane vs control plane; alert-triggered remote commands held as automation hooks not purpose — leaf unprocessed)."
5. **configuration-management (§14, 2026-09-07)**: boundary held vs Server Management (desired-state conformance engine vs estate platform).
6. **infrastructure-automation-platform (§14, 2026-09-08)**: generic governed automation content vs server ops machinery.
7. **container-management / kubernetes-management-platform / paas-management-console**: substrate seams (containers/clusters/PaaS runtime vs OS machines).
8. **remote-monitoring-management-rmm (§14, 2026-09-09)**: RMM core = enrolled managed devices + continuous monitoring with alerting + remote management actions; monitoring is DEFINITIONAL there. Its boundary list did not name this leaf; the estate-subject seam from network-management applies.

## Initial Boundary (hypothesis before research)

- Core purpose: operate an organization's server machines as an estate — bring under management, inventory, provision, patch/configure, operate remotely, retire.
- Users: sysadmins / infrastructure & operations teams; MSPs secondarily.
- Nearest neighbors: RMM, UEM, Patch Management, Configuration Management, Infrastructure Monitoring, Network Management, Virtualization Management, CMP, DCIM, ITOM.
- Open questions: Is provisioning definitional? Is monitoring definitional? Is the hardware/out-of-band pole the same Type? Is the cloud-native pole (agent + control plane) the same Type?

## Research Questions

1. What exactly is the managed object (server machine? OS instance? node? hardware?)
2. How do machines enter management (agent, registration, activation, bootstrap)?
3. What lifecycle does the platform execute (entry → maintain → operate → exit)?
4. What are the core objects (machine records, groups, channels/repos, actions/activities, profiles)?
5. What operations exist (package/patch, remote command/script, config, power, reboot)?
6. Is monitoring definitional? (test: find in-type products without it)
7. Is provisioning definitional? (test: find in-type products without it)
8. How are roles/permissions structured?
9. What interfaces exist (console, CLI, API, agent channel)?
10. Where are the boundaries vs each processed sibling?

## Representative Products

| Product | Pole | Evidence tier |
|---|---|---|
| AWS Systems Manager | cloud-native node operations control plane | Tier-1 (3 doc pages fetched) |
| Canonical Landscape | OS-vendor estate platform (Ubuntu), SaaS + self-hosted | Tier-1 (4 doc pages fetched) |
| Uyuni (open-source upstream of SUSE Multi-Linux Manager) | open-source multi-distro estate platform | Tier-1 (3 pages fetched) |
| Red Hat Satellite | enterprise subscription Linux lifecycle platform | Tier-2 (product page; docs.redhat.com 403) |

Dropped: Dell OpenManage Enterprise (404 ×2 — hardware/out-of-band pole recorded as market posture only, no product claims); SUSE Manager commercial pages (403 — represented via Uyuni, whose own site links SUSE Multi-Linux Manager as the related commercial product).

## Sources

Fetched 2026-09-09:

- AWS Systems Manager — What is AWS Systems Manager: https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html (Tier-1)
- AWS Systems Manager — Using AWS Systems Manager tools: https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-tools.html (Tier-1)
- AWS Systems Manager — Managing nodes in hybrid and multicloud environments: https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-hybrid-multicloud.html (Tier-1)
- Landscape Documentation index: https://docs.ubuntu.com/landscape/en/ (Tier-1)
- Landscape — What is Landscape?: https://docs.ubuntu.com/landscape/en/what-is-landscape (Tier-1)
- Landscape — How to manage instances: https://docs.ubuntu.com/landscape/en/how-to-guides/web-portal/web-portal-24-04-or-later/manage-instances (Tier-1)
- Landscape — Activities (explanation): https://docs.ubuntu.com/landscape/en/explanation/features/activities (Tier-1)
- Landscape — Profiles (terms reference): https://docs.ubuntu.com/landscape/en/reference/terms/profiles (Tier-1)
- Uyuni Documentation index: https://www.uyuni-project.org/uyuni-docs/en/uyuni/index.html (Tier-1)
- Uyuni — Actions: https://www.uyuni-project.org/uyuni-docs/en/uyuni/administration/actions.html (Tier-1)
- Uyuni project home: https://www.uyuni-project.org/ (Tier-1)
- Red Hat Satellite product page: https://www.redhat.com/en/technologies/management/satellite (Tier-2)

Unreachable (recorded limitations, 1–2 attempts each then abandoned):

- docs.redhat.com — 403 (Satellite operational tier unverified; consistent with patch-management pass's identical limitation). No Satellite operational parameters asserted anywhere.
- suse.com — 403 (SUSE Manager commercial pole evidenced only via Uyuni's own related-links page).
- dell.com OpenManage Enterprise — 404 ×2 (hardware/out-of-band pole: market posture only, no product claims).
- docs.aws.amazon.com systems-manager-managednodes.html — JS-gated (title only); hybrid-multicloud page used instead, which contains the managed-node definition.

## Product A — AWS Systems Manager (Tier-1)

### Key observations

- Self-description: "AWS Systems Manager helps you centrally view, manage, and operate nodes at scale in AWS, on-premises, and multicloud environments." Unified console "consolidates various tools to help you complete common node tasks across AWS accounts and AWS Regions." [A]
- Managed object: "Any machine that has been configured for use with Systems Manager is called a *managed node*." EC2 instances + on-premises servers + edge devices + VMs in other clouds (Azure named). Hybrid-activated node IDs prefixed "mi-" vs EC2 "i-". [A]
- Entry mechanisms: SSM Agent installed + communicates with the service; two onboarding methods for non-EC2 machines — **Cloud Connectors** (automatically onboard Azure VMs at scale: "handle identity federation, agent installation, and VM registration without requiring direct access to your Azure VMs"; new VMs auto-enrolled) and **Hybrid Activations** (register individual machines via activation code + ID, "functions like an Amazon EC2 access ID and secret key"). [A]
- Node tools (the Type-relevant core): Compliance (scan fleet for patch compliance + configuration inconsistencies), Distributor (create/deploy packages), Fleet Manager ("unified UI... remotely manage your nodes... view the health and performance status of your entire fleet from one console... viewing directory and file contents, Windows registry management, operating system user management"), Hybrid Activations, Inventory ("automates the process of collecting software inventory... applications, files, components, patches"), Patch Manager (patch baselines, auto-approval rules, approved/rejected lists, maintenance windows, Linux repo override), Run Command ("remotely and securely manage the configuration of your managed nodes at scale... on-demand changes such as updating applications or running Linux shell scripts and Windows PowerShell commands on a target set of dozens or hundreds of managed nodes"), Session Manager ("interactive single-step browser-based shell... without needing to open inbound ports, maintain bastion hosts, or manage SSH keys... fully auditable logs"), State Manager ("keeping your managed nodes in a defined state... bootstrapped with specific software at startup, joined to a Windows domain, or patched"). [A]
- Change-management tools: Automation (runbooks: AMI creation, driver/agent updates, password resets, patching), Change Calendar, Change Manager (closing to new customers), Documents (SSM documents define actions — Command documents, Automation runbooks), Maintenance Windows ("recurring schedules for managed instances to run administrative tasks"), Quick Setup. [A]
- Adjacent bundled tools NOT part of the machine-operations core: AppConfig, Application Manager, Parameter Store (application config/secrets), Explorer, Incident Manager, OpsCenter, CloudWatch Dashboards (operations dashboards). Suite-drift observation: the SSM umbrella is broader than the Type; the node tools are the Type's center. [A]
- Benefit framing: "safe and secure remote management of your nodes at scale without logging into your servers. You no longer need to use bastion hosts, SSH, or remote PowerShell"; "automating common administrative tasks across groups of nodes such as registry edits, user management, and software and patch installations." [A]
- Users: "IT operations managers and operators, DevOps engineers, security and compliance managers, and IT directors and CIOs." [A]
- Value framing: centralized view; centralized access control (IAM); centralized auditing (CloudTrail); "Create a consistent and secure way to remotely manage your hybrid and multicloud workloads from one location using the same tools or scripts." [A]
- Name history: "Amazon Simple Systems Manager (SSM)" → "Amazon EC2 Systems Manager" → "AWS Systems Manager". [A]
- NO provisioning of new machines (EC2 provisioning is EC2's job; SSM manages existing instances). NO built-in metric monitoring (CloudWatch separate). [A — negative evidence]

## Product B — Canonical Landscape (Tier-1)

### Key observations

- Self-description: "Landscape is Canonical's systems management solution. You can use Landscape to manage all of your Ubuntu systems: desktops, servers, cloud instances, IoT devices, and more." "At its core, Landscape allows you to manage all of your systems from a single portal... managing software updates across your Ubuntu estate, executing scripts on your clients remotely, managing packages and repositories, configuring Role-Based Access Control (RBAC), monitoring your client machines, and much more." [A]
- Architecture: client-server. Landscape Server (central; web portal + API) + Landscape Client (agent on each managed machine; "sending client information to the server, receiving updates from the server, and executing commands on the client from the server"). Message system carries server↔client communication. [A]
- What it does: "System monitoring, management, and alerts" (health, hardware info, alerts "when security upgrades are available, when a client machine needs to be rebooted"); "Package and upgrade management"; "Remote scripting"; "Repository management" (custom repos across the estate); "User management and RBAC". [A]
- Editions: SaaS (Canonical-hosted, multi-tenant), Managed (single-tenant hosted in customer environment, Canonical-operated), Self-hosted (on-prem/cloud). [A]
- Instances page: list with hostname/title, status (online/offline, alerts, reboot required), OS+version, tags; saved searches; per-instance tabs (activities view/cancel/undo/redo; kernel upgrade/downgrade; snaps + Debian packages; fix security issues; hardware info; Info: status, last ping, access group, registration details); bulk actions (restart, attach Pro tokens, run scripts); removal ("Removing an instance only removes it from Landscape's management. This action doesn't affect the actual machine"); removal profiles auto-remove inactive instances. [A]
- **Activities** (first-class object): "Landscape tracks the progress of various tasks using activities, such as script execution and installing packages." Client activities + server activities. Full state machine: Queued / Scheduled / Waiting / Blocked → In Progress → Failed / Succeeded / Canceled (final). Created "by an admin action or scheduled profile". Activity types include: ChangePackagesRequest, UpgradeAllPackagesRequest, ReleaseUpgradeRequest, Upgrade/DowngradeKernelPackageRequest, SignalProcessRequest, ExecuteScriptRequest, RestartRequest, ShutdownRequest, Install/Remove/Refresh/Hold/UnholdSnaps, user/group management, Attach/DetachProRequest, UsgActivity, RemoveComputerActivity, WSL instance ops, ArchiveRequest, GenerateFDERecoveryKeyRequest. [A]
- **Profiles** (reusable management rules): "reusable sets of rules that define how Landscape should manage certain instances... applied to groups of instances matching the tags and/or access group... Landscape automatically applies any relevant existing profiles to newly accepted instances... Many profiles have a notion of **compliance**. When an instance becomes associated with a profile, Landscape will create activities to bring that instance into compliance." Types: Package profile (meta-package constraints — packages systems "should always get, or never get"; evaluated periodically; non-compliance reported), Reboot profile (scheduled reboots, staggered delivery window), Removal profile (auto-remove after N days without data exchange; releases license seat), Repository profile (pockets + APT sources applied once), Script profile (script + executing user + time limit + trigger), USG profile (CIS/DISA-STIG compliance evaluation on schedule, optional remediation), Upgrade profile (weekly schedule, security-only or all upgrades, randomized delivery across the estate), WSL profile (install Ubuntu WSL instances on Windows hosts, compliance-evaluated). [A]
- Repository mirroring: internally distribute software, manage custom repositories, air-gapped support, tiered mirrors (self-hosted/managed only, not SaaS). [A]
- Provisioning: autoinstall provisioning for Ubuntu machines (configure deployment, provision a workstation) — present but scoped (workstations/Ubuntu installer integration). [A]
- Scope breadth: desktops, servers, cloud instances, IoT devices (Ubuntu Core snap), WSL instances on Windows hosts, NVIDIA DGX Spark. [A]
- RBAC: administrators, roles, access groups (access groups scope both instances and profiles); external auth (AD, OIDC, PAM). [A]
- Interfaces: web portal, REST API + legacy API (API endpoints include Computers, Activities, Alerts, Packages, Repositories, Scripts, Snaps, Profiles, RBAC...). [A]
- Ansible relationship: "Landscape and Ansible" related-tools page (integration, not embedded engine — coexistence framing). [A]

## Product C — Uyuni (Tier-1; open-source upstream of SUSE Multi-Linux Manager)

### Key observations

- Self-description: "Uyuni is a solution for organizations that require robust control over maintenance and package deployment on their servers. It enables you to manage large sets of Linux systems and keep them up-to-date, with automated software management, asset management, and system provisioning. It also allows you to maintain a high level of security while effectively managing system life-cycle requirements." Home page: "configuration and infrastructure management tool that saves you time and headaches when you have to manage and update tens, hundreds or even thousands of machines." [A]
- Engine: "Uyuni uses Salt to provide event-driven configuration and management control. The Salt-master orchestrates tens of thousands of Salt clients (Uyuni clients) using remote execution." "The Uyuni Server is a full-fledged Salt Master node." [A]
- Multi-distro: SUSE Linux Enterprise, openSUSE, RHEL, CentOS, Oracle Linux, Ubuntu, Debian, Amazon Linux, AlmaLinux, Raspberry Pi OS (+ Alibaba, openEuler, OES in client-registration tree); on-prem, public/private/hybrid/multi-cloud. [A]
- Core objects (WebUI reference tree): **Systems** (systems list, system groups, System Set Manager for bulk operations, bootstrapping, activation keys, stored profiles, custom system info, autoinstallation, virtual host managers); **System Details** (properties, remote command, connection, reactivation, hardware, transfer, notes, custom info; Software: patches, packages, AppStreams, software channels, product migration; Configuration; Provisioning; Groups; Audit; States; Formulas; Ansible; Events; Proxy); **Salt** (keys, remote commands, formula catalog); **Patches** (patch details, relevant/all lists, manage, clone); **Software** (channel details/list, package search, manage channels/packages/repositories); **Content Lifecycle Management** (projects, filters); **Audit** (CVE audit, subscription matching, OpenSCAP); **Configuration** (channels, files, managed/target systems); **Schedule** (pending actions, recurring actions, completed, failed, archived, action chains, maintenance windows); **Users**; **Admin** (setup wizard, organizations, access control, manager configuration incl. Cobbler, task schedules). [A]
- **Actions** model: recurring actions (highstate / custom states) applied to individual clients, system groups, or entire organizations; hourly/daily/weekly/monthly/custom-quartz frequency; test mode; action chains (ordered sequences — "If one action in an action chain fails, the action chain stops, and no further actions are executed"); remote commands ("issue commands to individual clients, or to all clients that match a search term"); schedule views: pending/recurring/completed/failed/archived + maintenance windows. [A]
- Client operations: package management, patch management, system locking, configuration management, power management, custom system info, System Set Manager, system groups, system types. [A]
- Entry: client registration via Web UI / bootstrap script / CLI; activation keys; bootstrap repository; contact methods (Salt default, SSH push, SSH push with tunnel, Salt Bundle); public-cloud auto-registration (Terraform-created clients). [A]
- Content machinery: software channels, repositories, software products, AppStreams, GPG keys, custom channels, third-party channels, Content Lifecycle Management (projects + filters — stage content through lifecycle environments), content staging, disconnected setup, live patching. [A]
- Provisioning: autoinstallation (reinstall registered systems, PXE boot, CD/USB, autoinstallable distributions, autoinstallation profiles, unattended provisioning); Cobbler referenced in admin config (the embedded provisioning engine); image building (build OS images, profiles, stores); retail vertical (branch servers + terminal deployment via Saltboot). [A]
- Virtual Host Managers: discover and manage VMs from AWS, Azure, Nutanix, VMware as systems. [A]
- Compliance/audit: OpenSCAP (scans, XCCDF diff, SCAP content, policies, tailoring files), CVE audit, subscription matching, package auditing. [A]
- Monitoring: "Monitoring with Prometheus and Grafana" — an administration module (optional), not the core. [A]
- RBAC: role-based access control, organizations, users, system group configuration. Auth: SSO, PAM. [A]
- Interfaces: Web UI, spacecmd CLI (functions: activationkey, configchannel, distribution, errata, kickstart, package, repo, scap, softwarechannel, system, user...), XML-RPC API, reporting database. [A]
- Lineage evidence: Uyuni's own related-links page lists **SUSE Multi-Linux Manager** (commercial sibling), **Salt Project**, **Cobbler**, **Spacewalk**; spacecmd/kickstart/errata vocabulary carries the Spacewalk/Satellite-5 heritage. [A — lineage]

## Product D — Red Hat Satellite (Tier-2; docs unreachable)

### Key observations

- Self-description: "The premier management solution for Red Hat Enterprise Linux." "Red Hat Satellite simplifies the provisioning, patching, and management of your Red Hat Enterprise Linux environments to keep them running efficiently and in compliance with various security standards." [B — product page]
- "Red Hat Satellite can manage your entire hybrid Red Hat Enterprise Linux footprint—from on-premise to the cloud—from a single console." "Meet the demand for provisioning, securing and maintaining thousands of distributed systems across multiple data centers and the cloud." [B]
- Feature groups (product page): Security management (centralized security hub — "Issue updates at scale on custom schedules from a local, centralized point"; compliance enforcement; configuration assessment; data sovereignty); Patch management and content distribution (supply chain verification — "Verify digital signatures on all synced content"; lifecycle curation — "Curate specific repositories and patches for Dev, QA, and Production environments"; precision patching — "Deploy specific, critical patches... without forced system-wide upgrades"); Provisioning (bare-metal discovery — "Automate the discovery, setup, and provisioning of new hardware with a rules-based workflow"; standardized compute profiles — "Define CPU, RAM, and storage parameters across VMware, KVM, and physical builds"; unified provisioning — "Integrate DNS, DHCP, and identity services into a single management console"); Knowledge and analytics (configuration advisories, vulnerability prioritization — "Scan and rank named threats and CVEs", offline knowledge portal). [B]
- Satellite 6.20: containerized packaging; MCP servers (tech preview) for AI workflows. 6.19: "expanded Ansible automation, faster content publishing, enhanced reporting." [B]
- **No operational parameters asserted** — docs.redhat.com 403 (same limitation as the patch-management pass). All Satellite claims above are Tier-2 positioning claims.

## Cross-product Comparison

| Dimension | AWS SSM | Landscape | Uyuni | Satellite (Tier-2 only) |
|---|---|---|---|---|
| Managed object name | managed node | instance / computer | system / client | (systems; docs unreachable) |
| Object class | machine (EC2, on-prem server, edge, other-cloud VM) | Ubuntu machine (desktop, server, cloud instance, IoT, WSL) | Linux machine (multi-distro, incl. IoT, retail terminals) | RHEL systems |
| Entry | SSM Agent + hybrid activation / Cloud Connector | Landscape Client install + registration | registration (bootstrap/Web UI/CLI) + activation keys | registration/subscription (docs unreachable) |
| Estate organization | Fleet Manager, filters (OS/region/account/agent) | access groups, tags, saved searches | system groups, System Set Manager, tags, organizations | single console (product page) |
| Inventory | Inventory tool (apps, files, components, patches) | hardware info, package reporting | hardware, custom info, packages | (docs unreachable) |
| Maintenance | Patch Manager (baselines, windows), Distributor | package/snaps mgmt, upgrade profiles, Livepatch, repo mirrors | package/patch mgmt, channels, CLM, live patching | patch + content distribution, lifecycle curation |
| Operations | Run Command, Session Manager, State Manager, Automation | remote script execution, activities (restart/shutdown/signal) | remote commands, action chains, recurring actions, power mgmt | (docs unreachable; "expanded Ansible automation") |
| Configuration | State Manager associations | profiles (package/repo/script/upgrade/USG/WSL) | Salt states/config channels/formulas | configuration assessment |
| Compliance | Compliance tool | USG profiles (CIS/DISA-STIG), package reporting | OpenSCAP, CVE audit, subscription matching | compliance enforcement, CVE prioritization |
| Provisioning | **none** | autoinstall (workstations) | autoinstallation (PXE/profiles/reinstall), image building | bare-metal discovery, compute profiles |
| Activity tracking | command history, Automation executions, maintenance windows | activities with full state machine | actions (pending/recurring/completed/failed/archived), action chains | (docs unreachable) |
| Monitoring | none (CloudWatch separate) | management-event alerts | optional Prometheus/Grafana module | not on product page |
| RBAC | IAM | administrators/roles/access groups | RBAC/organizations/users | (docs unreachable) |
| Interfaces | console, CLI, SDKs | web portal, REST + legacy API | Web UI, spacecmd, XML-RPC API | single console |
| Exit | deregister managed instance | remove from Landscape (machine unaffected), removal profiles, sanitize | client deletion | (docs unreachable) |

### Convergent findings (evidence layer B unless noted)

1. All four center on a **managed machine population** with an explicit entry step (agent/registration/activation) — the management relationship is established deliberately, per machine. [B]
2. All four execute **maintenance + operations from a central console without per-machine login** — patch/package management, remote command/script execution, configuration. [B]
3. All four **record platform actions as tracked units** (activities / actions / command & automation history) with states and outcomes, attached to machines. [B]
4. All four organize the estate in **groups/tags** and scope **RBAC** through them. [B]
5. All four carry **update/content machinery** (patch baselines / upgrade profiles + repo mirrors / channels + CLM / content curation) — forms differ strongly. [B]
6. All four carry **compliance machinery** (scanning against baselines/benchmarks). [B]
7. All four expose **console + API (+ CLI in 3 of 4)**. [B]
8. **Monitoring is NOT convergent**: SSM none, Landscape management-event alerts only, Uyuni optional module, Satellite not evidenced. → not definitional. [B — negative]
9. **Provisioning is NOT convergent**: SSM none; Landscape scoped (workstations); Uyuni/Satellite full. → not definitional; dominant in the enterprise-Linux pole. [B — negative]
10. **Exit is managed**: removal from management (explicitly not machine destruction — Landscape), deregistration (SSM), deletion (Uyuni), sanitize (Landscape). [B]
11. Suite drift: SSM bundles application/operations tools beyond the machine core; Uyuni bundles retail vertical + image building; Satellite bundles knowledge portal. The Type's center survives as the machine-estate core. [B]

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (three jointly-held structures)

1. **The managed machine estate** — the organization's machines (servers the center of gravity; physical, virtual, cloud instances) held as persistent individually identified managed records, brought under management via a deliberate entry step (agent/registration/activation), organized in groups, carrying inventory facts. Remove → asset inventory/CMDB.
2. **The estate control plane** — maintenance and operations executed from the central console against machines without per-machine login: software/patch management through the OS's own package machinery, remote command/script execution, configuration/profiles applied to individual machines and groups. Remove → observation-only monitoring (Infrastructure Monitoring territory) or a bare script runner.
3. **The managed lifecycle with recorded activity** — machines are carried through an operational lifecycle under the platform (entry → maintenance → operations → exit), and what the platform does to each machine is recorded as tracked activities/jobs with states and outcomes against the machine record. Remove → one-shot tools; the "management" dies.

Jointly-held load-bearing:
- 1 alone = server inventory / CMDB slice
- 2 without 1 = script runner / patch tool with no estate
- 3 without 1+2 = lifecycle paperwork with no operations
- 1+2 without 3 = ad-hoc ops console (automation-lite)
- 1+3 without 2 = records nobody operates
- 2+3 without 1 = operations with no estate memory

### L1 — Common Mature Structure (standard, not definitional)

- Provisioning / OS deployment (bare-metal discovery, PXE/autoinstall/autoinstallation profiles, image templates, reinstall) — dominant in the enterprise-Linux pole, absent in the cloud-native pole
- Update/content machinery: software channels/repositories/mirrors, patch baselines, content lifecycle staging, subscription/entitlement management (subscription matching, Ubuntu Pro attach, license seats)
- Configuration machinery: embedded config engine (Salt/Ansible) or profile system (package/repository/script/upgrade profiles, State Manager associations)
- Compliance machinery: OpenSCAP / USG (CIS, DISA-STIG) / CVE audit / compliance scanning + reports
- Inventory facts + reporting + saved searches
- RBAC scoped by groups + external auth (AD/OIDC/PAM/SSO)
- API + CLI as peer surfaces to the console
- Management-relevant alerts (security upgrades available, reboot required, non-compliance)
- Reboot management (reboot profiles, live patching, kernel up/downgrade)
- Multi-environment reach (on-prem, public cloud, other clouds, edge/IoT, WSL)
- Session/interactive access without inbound ports (Session Manager pole)

### L2 — Variant / Optional Structure

- Vendor anchoring: OS vendor (Red Hat / SUSE / Canonical) vs cloud vendor (AWS) vs hardware vendor (Dell/OpenManage — degraded evidence, market posture only)
- Delivery: SaaS vs self-hosted vs vendor-managed single-tenant (Landscape's three editions)
- Scope breadth: servers-only center of gravity vs +desktops/IoT/WSL (Landscape, Uyuni)
- Provisioning depth: full bare-metal/PXE vs scoped vs none
- Contact method: persistent agent vs SSH push vs agent bundle (Uyuni's Salt/SSH/Salt Bundle); out-of-band BMC (hardware pole, degraded)
- Monitoring depth: none vs management-event alerts vs optional metrics module
- Multi-OS vs single-OS-family anchoring
- Embedded verticals (retail branch/terminal deployment in Uyuni)

### L3 — Vendor-specific (research notes only)

- Satellite: Foreman/Katello/Candlepin/Pulp componentry, content views, subscription allocation, Satellite 6.20 container packaging, MCP servers
- Uyuni/SUSE Manager: spacecmd, Salt formulas/pillars, System Set Manager, Cobbler embedding, retail branch server/Saltboot, mgradm, reporting database, Taskomatic
- Landscape: message-system, pockets/Debarchive, charms (Juju), lsctl, FDE recovery keys, WSL profiles, Ubuntu Pro token attach, license seats
- SSM: SSM Documents (Command/Automation), Parameter Store, Distributor packages, Fleet Manager, mi- vs i- ID prefixes, hybrid activation code/ID, Quick Setup, Change Manager (sunset to new customers), advanced-instances tier removal (2026)

## Vendor-specific Findings

See L3. Additionally: SSM's umbrella includes non-machine tools (AppConfig, Parameter Store, Incident Manager, OpsCenter) — suite packaging, not Type structure. Uyuni's retail guide (branch servers, terminal imaging) is a vertical realization. Landscape's WSL/IoT/DGX Spark reach is scope-breadth variant.

## Boundary Findings

1. **vs Infrastructure Monitoring** (pre-hung, ratified direction): observation plane vs control plane. Monitoring is not definitional here (SSM none; Landscape management-event alerts; Uyuni optional module). Remove the control-plane actions → Infrastructure Monitoring territory. Alert-triggered remote commands here are operations, not the purpose.
2. **vs Patch Management** (pre-hung): patching is one slice of server ops. Patch tools center on update currency (catalog + assessment + deployment); here the center is the estate + lifecycle + operations, with patch machinery embedded as one capability. Remove everything but the update-currency machinery → Patch Management territory. The Satellite straddle (provisioning+patching+config) is the Type's normal breadth, not suite drift — the drift zone is where a product is ONLY patching (patch tool) or ONLY provisioning (Cobbler/MAAS-class, below the Type).
3. **vs Configuration Management**: desired-state conformance engine vs estate platform. Uyuni embeds Salt; Satellite embeds Ansible; Landscape uses profiles; SSM has State Manager. The embedded engine is machinery. Remove the estate/lifecycle and keep only desired-state content + convergence → Configuration Management territory.
4. **vs Infrastructure Automation Platform**: generic governed automation content (the reusable artifact is the unit of record) vs machine-estate operations (the machine is the unit of record; actions are machine-scoped operations). Remove the estate and keep governed automation content → Infrastructure Automation territory.
5. **vs RMM** (hardest seam): RMM = device fleet (heterogeneous: workstations/laptops/servers/network devices), monitoring-first (continuous monitoring with alerting is a DEFINING leg there), MSP-oriented. This Type = machine estate (server-centered), lifecycle-first (monitoring NOT definitional — SSM/Landscape poles), org-estate-oriented. RMM-class tools manage both estates (per network-management pass) — the estate-subject seam holds. Supporting differences: OS-provisioning machinery exists here (not in RMM's core); OS-vendor content channels here; RMM's remote-control-first posture vs this Type's lifecycle posture.
6. **vs UEM**: user endpoint devices (policy/compliance for user-carried devices, enrollment of personal/corporate endpoints) vs infrastructure machines operated as an estate. Same estate-subject seam family.
7. **vs Network Management / Network Monitoring**: managed object class (network infrastructure devices vs server machines) — pre-hung seam ratified. Suites (SolarWinds NPM/NCM pattern) sell both as separate products over one platform.
8. **vs Virtualization Management** (UNPROCESSED — flag hung): VMs as hypervisor-level objects (create/start/snapshot/migrate, host resources) vs machines as OS-level managed records. Uyuni's Virtual Host Managers discover VMs from AWS/Azure/VMware/Nutanix and manage them AS SYSTEMS (OS layer) — the VM enters this Type as a machine. Remove the OS layer and operate the hypervisor/VM lifecycle → Virtualization Management territory.
9. **vs Cloud Management Platform**: CMP = account/resource governance over cloud estates (provisioning from specs, day-2 vocabulary, cost/quota governance); here the object is the machine, not the account/resource portfolio. SSM is cloud-native but machine-scoped. Remove the machine layer and govern accounts/resources → CMP territory.
10. **vs DCIM**: physical layer (racks/power/cooling/placement) vs machine operational layer. DCIM holds servers in its physical inventory; here the server is the operated machine. Remove the OS/operations layer and keep physical placement/power → DCIM territory.
11. **vs Container Management / Kubernetes Management**: workload substrate (containers/clusters) vs OS machines. Uyuni can deploy/manage Kubernetes-adjacent machinery but the managed record is the machine. Remove the OS-machine layer and operate containers → Container/K8s Management territory.
12. **vs IaC Platform**: declared resource lifecycle (run-to-completion against provider APIs) vs standing machine operations. Remove the standing estate and keep declared infrastructure → IaC territory.
13. **vs CMDB / IT Asset Management**: operational agent-connected actionable estate vs authoritative asset/commercial record. The estate here is operational, not the system of record for assets.
14. **vs HCI Management**: converged cluster stack plane (compute+storage pools, node grain) vs individual machines. Remove the machine grain and manage the converged stack → HCI territory.
15. **vs ITOM**: whole-estate multi-domain operations layer vs single-domain (server/machine) platform. Consistent with ITOM pass's "single-domain tool" boundary framing.
16. **vs Backup Management**: no recovery-point custody here; pre-patch snapshots are operator practice, not a Type structure.
17. **Provisioning-only tools** (Cobbler, MAAS): provisioning machinery without the estate operations → below/outside the Type. Cobbler appears INSIDE Uyuni as the autoinstallation engine — machinery, not the Type.
18. **vs PaaS Management Console**: PaaS abstracts servers away (substrate not exposed); here the machine IS the object of work.

## Historical / Market-Sample Check (§24)

- **Spacewalk** (2008-era open-source systems management, EOL; Uyuni's own related-links page lists it; spacecmd/kickstart/errata vocabulary carried in Uyuni): systems + software channels + errata + kickstart provisioning + remote commands — satisfies all three L0 legs with no cloud/AI/SaaS. [A — lineage via Uyuni's own page]
- **Classic Satellite 5 / RHN generation**: same model (conceptual — Satellite docs unreachable; positioning consistent).
- **SSM name history** (Tier-1): "Amazon Simple Systems Manager" → "Amazon EC2 Systems Manager" → "AWS Systems Manager" — the cloud-native pole is a renaming/extension of the same concept, not a new Type.
- **Analog ancestor** (conceptual): server room practice — kickstart/autoinstall files + internal package mirror + SSH + inventory spreadsheet + change log — satisfies the three legs at analog level (estate = spreadsheet, control plane = scripts/mirror, lifecycle = manual records). Marked conceptual, no fetched source.
- **Hardware/out-of-band pole** (Dell OpenManage/iDRAC, HPE OneView/iLO class): same managed object (the server machine), different operating layer (BMC/firmware). Unreachable this pass — held as a variant pole with degraded evidence; no product claims. If a later pass observes it, revisit whether the out-of-band layer challenges the "OS machinery" phrasing of L0 leg 2 (current phrasing "through the machine's own update/execution channels" is deliberately layer-neutral).
- Older/regional/platform-native products fit: the definition names no cloud, no SaaS, no AI, no specific OS, no agent protocol.

## Uncertainties

1. Satellite's operational model (host object, remote execution, content views) is inferred from Tier-2 positioning only — docs 403. No operational parameters asserted for Satellite anywhere in the final document.
2. SUSE Manager commercial packaging (pricing, tiers, exact deltas from Uyuni) unverified (suse.com 403); Uyuni's own related-links page evidences the relationship at the level of "related commercial product".
3. Hardware/out-of-band pole (OpenManage/OneView/iLO class) unobserved — variant status is market posture, not sampled structure.
4. Whether any in-type product lacks BOTH groups/tags AND RBAC scoping — not tested (all sampled have both); the L0 does not depend on it.
5. Exact activity-state vocabularies differ per product (Landscape's Queued/Blocked/... vs Uyuni's pending/completed/failed/archived); the canonical claim is "tracked activity with states and outcomes", not a universal state set.
6. Whether Windows-server-centric estate platforms (e.g., SCCM's server role) belong here or under UEM's lineage — the UEM pass resolved SCCM+MDM as one Type on the endpoint side; the server-side slice was not sampled this pass. Recorded as an open seam, not resolved.

## Final Synthesis

A Server Management Platform is the organization's server estate operations platform: a standing control plane through which the operations team brings machines under management (agent/registration/activation), keeps them current and compliant (patch/package/configuration machinery, commonly with content channels and compliance benchmarks), operates them remotely (commands/scripts/sessions/power without per-machine login), and retires them (removal/deregistration/sanitize) — with every platform action recorded as a tracked activity against the machine record.

The defining core is three jointly-held structures: the managed machine estate, the estate control plane, and the managed lifecycle with recorded activity. Monitoring is not part of the core (observation plane belongs to Infrastructure Monitoring). Provisioning is not part of the core (dominant in the enterprise-Linux pole, absent in the cloud-native pole). The managed object is the machine — the estate-subject seam that separates this Type from network management (network devices), UEM (user endpoints), RMM (heterogeneous device fleets, monitoring-first), virtualization management (hypervisor-level VMs), container/K8s management (workload substrate), CMP (account/resource governance), and DCIM (the physical layer).
