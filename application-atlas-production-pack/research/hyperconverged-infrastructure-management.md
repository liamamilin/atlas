# Research Notes — Hyperconverged Infrastructure Management

## Research Goal

Understand what "Hyperconverged Infrastructure Management" is as an Application Type: what object domain it operates (nodes, clusters, software-defined storage pools, VMs, the management plane itself), which operations define it (provision VMs on pooled resources, expand/shrink clusters at node grain, update the stack as a unit, keep services available through failure), how the management layer relates to the HCI platform it manages (embedded vs centralized vs cloud-hosted consoles), and how the Type is bounded against Virtualization Management, Server Management Platform, Storage Management, Cloud Management Platform, DCIM, Infrastructure Monitoring, Backup/DR, and Kubernetes Management.

Context: the leaf sits in §14 IT, Cloud & Infrastructure between sibling leaves (Server Management Platform, Virtualization Management, Storage Management, Cloud Management Platform, DCIM). The distinguishing question from the start: is "HCI Management" just "virtualization management with a different label" — or does the converged compute+storage subject and the whole-stack operating authority make it a structurally distinct Type?

## Initial Boundary

Working hypothesis before research:

- Core use: operate a hyperconverged cluster — server nodes that each contribute compute AND local storage to shared software-defined pools — through one management plane: monitor health, provision and manage VMs, expand/shrink capacity by adding/removing nodes, update the platform stack as a unit, handle failure/rebuild.
- Users: IT infrastructure administrators, virtualization/infrastructure engineers, operations teams in SMB/mid-market/enterprise; MSP/edge operators managing fleets.
- Nearest neighbors: Virtualization Management (closest sibling — same VM/host vocabulary), Server Management Platform (node/firmware layer), Storage Management (storage-only subject), Cloud Management Platform (multicloud brokering), DCIM (facility layer), Infrastructure Monitoring (observe-only), Backup Management / DR Platform (protection layer), Kubernetes Management Platform (container workloads on the same substrate).
- Main unknowns: (1) is the converged compute+storage subject definitional, or do external-storage deployments still count; (2) is "single pane" definitional when products offer multiple surfaces (local console + cloud portal + PowerShell); (3) how much of monitoring/protection belongs inside the Type vs adjacent; (4) is the cloud-connected fleet layer (Arc-style) an era artifact or definitional; (5) appliance vs software-only vs platform packaging — variant or separate Type.

## Research Questions

1. What is the core object domain (node, cluster, storage pool/data store, VM, network) and how do the objects relate?
2. What does the management plane cover (health, compute, storage, network, VMs) and how is it delivered (embedded per-cluster console, virtual appliance, cloud portal, CLI/API, legacy local tools)?
3. What are the defining lifecycle operations: VM provisioning, node add/remove (cluster expansion/shrink), stack/software/firmware updates, failure handling/rebuild?
4. What data services are standard (snapshots, replication, dedupe/compression/erasure coding) and how are backup/DR realized?
5. What does the health/monitoring surface look like (dashboards, alerts, diagnostics, self-healing automation)?
6. How is multi-cluster / fleet management realized (central manager, cloud-hosted fleet console)?
7. What identity/RBAC/SSO machinery is standard?
8. How do hypervisors relate to the management layer (own hypervisor, third-party support, platform OS)?
9. What packaging variants exist (software-only, OEM-validated hardware, turnkey integrated platform, hypervisor-suite extension)?
10. Where are the exact seams with Virtualization Management, Storage Management, Cloud Management Platform, and Infrastructure Monitoring?

## Representative Products

Selected for market representativeness, documentation quality, distinct product philosophies, and distinct customer tiers:

| Product | Philosophy pole | Customer tier |
|---|---|---|
| Nutanix Prism (with Nutanix Cloud Infrastructure) | software-defined HCI market leader; hypervisor-agnostic; embedded per-cluster manager (Prism Element) + centralized multi-cluster manager (Prism Central) + cloud fleet console (Nutanix Central) | mid-market → enterprise |
| VMware vSphere 9.1 (vCenter) | hypervisor-suite pole: HCI is the suite's converged form (software-defined storage technologies on the same hosts); management via vCenter/vSphere Client + Lifecycle Manager | enterprise; historically the incumbent |
| Microsoft Azure Local (formerly Azure Stack HCI) | platform-vendor hybrid-cloud pole: management plane delivered through the cloud platform (Azure portal / Arc) with local tools (Windows Admin Center, PowerShell) retained; OEM-validated hardware catalog | mid-market → enterprise |
| Scale Computing SC//HyperCore | SMB/edge simplification pole: fully integrated software+servers+storage platform, self-healing automation, cloud-hosted fleet manager (SC//Fleet Manager) | SMB → distributed edge |

Target fifth sample (appliance pole): Dell VxRail. ABANDONED — vendor doc surfaces unreachable (see Sources). The appliance pole is instead covered indirectly: Azure Local's "validated hardware from Microsoft hardware partners" model and Scale's "fully integrated platform" description document the turnkey/validated-hardware form from two sampled vendors' own docs.

Avoided: studying the same vendor's multiple products as separate samples; over-sampling marketing-heavy pages without operational documentation.

## Sources

Research date: 2026-09-08. All fetches via WebFetch.

- Nutanix — Prism product page (nutanix.com/products/prism): reachable. Includes vendor FAQ ("What is Nutanix Prism?", "difference between Prism and Nutanix Central", deployment options). Evidence layer A. (Nav confirms product-family structure: NCI [AOS Storage, AHV, DR, Flow, NC2, NCI with External Storage], Nutanix Central, NCM [Intelligent Operations, Self-Service, Cost Governance, Security Central], NUS [Files/Objects/Volumes], NDB, NKP, LCM, Move.)
- Nutanix — Tech Center blog "Introducing X-Small Prism Central" (nutanix.com/tech-center, 2024-05-31): reachable. Prism Central capability list, sizing tiers, one-click upgrade via LCM, cluster-profiles related article. Evidence layer A.
- VMware — vSphere 9.1 documentation landing (techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1.html): reachable. Full doc-set structure + doc descriptions. Evidence layer A (structure; not deep page content).
- Microsoft — Azure Local overview + documentation landing + "Overview of Hyperconverged Deployments" (learn.microsoft.com, azure/azure-local): all reachable. Evidence layer A. Old URL path /azure-stack/hci observed redirecting to azure-local (rename evidence).
- Scale Computing — Products page + SC//HyperCore product page (scalecomputing.com): reachable. Evidence layer A.
- Dell VxRail — NOT REACHED: infohub.delltechnologies.com blocked by security-verification interstitial (1 attempt); dell.com product URLs returned 404 (2 attempts). Source abandoned per network-restriction rule. No product-specific claims drawn from model memory; limitation recorded here and in the final document's Sources.
- VMware vSAN dedicated doc pages — NOT REACHED (URL guesses 404/redirect to generic TechDocs home, 2 attempts). vSAN therefore appears only as "software-defined storage technologies" within the fetched vSphere Storage doc description; no vSAN operational specifics asserted.
- Wikipedia "Hyper-converged infrastructure" — NOT REACHED (timeouts ×2). Neutral historical framing not available; historical check done structurally (see below).

## Product A — Nutanix Prism

### Key observations (evidence layer A unless noted)

**Positioning (vendor's own words).**
- "Nutanix Prism is the unified management plane for the Nutanix Cloud Infrastructure. It simplifies operations by consolidating the management of your entire infrastructure, including compute, storage, networking, and virtual machines (VMs) into a single, intuitive interface. This eliminates the need for multiple management tools…"
- Benefit framing: "Monitor and manage VMs, storage, and networks across on-premises clusters and public clouds from a single console." / "Prism supports multi-cluster management with high availability and scale-out architecture."

**Management plane delivery.**
- Prism "deploys as a virtual machine" (FAQ); deployment options: multiple VM configuration sizes (X-Small → X-Large), single VM for smaller environments or a three-VM scale-out cluster "for enhanced resilience and scalability in larger production environments."
- Two-level topology: Prism manages "one or more Nutanix clusters within a specific domain"; "for organizations that need to manage a large fleet of Nutanix environments across different global locations, Nutanix Central provides a cloud-based console for unified, global-scale visibility and operations." (FAQ)
- Prism is included with Nutanix Cloud Infrastructure "at no additional cost" — the management plane ships with the platform.
- Connectivity to Nutanix Central is listed among Prism Central capabilities (blog).

**Capability surface (product page "Streamlined Infrastructure Operations" etc.).**
- Proactive health monitoring: "comprehensive insights into performance and reliability across your entire environment from storage, compute, and networking to containers and cloud resources with intelligent diagnostics and alerts."
- Centralized multi-cluster management: "Manage common administrative tasks across all clusters from a single interface, reducing complexity, and accelerating response times."
- Automated lifecycle management: "Keep clusters up to date with non-disruptive upgrades and firmware updates across your entire environment." Separate LCM (Life Cycle Manager) product: "Automate and simplify the process of upgrading software and firmware across your Nutanix environment."
- VM management: "Deploy VMs quickly using templates and images based on policies and customization that ensure optimal placement and performance." / "Seamless Live Migration: Move workloads intelligently across clusters without downtime, preserving network and security configurations."
- Protection: "Integrated Protection Plans: Safeguard critical applications with automated recovery policies and consistent backup scheduling without any manual intervention."
- Network: "Lifecycle-Based Network Management: Simplify network and security policy management with intuitive workflows"; "Granular Microsegmentation … through Nutanix Flow (available under a separate license)."
- Governance: "Fine-Grained RBAC … customizable permissions across users, teams, and projects, supporting SSO and identity federation"; "Native encryption, backup and restore options, and RBAC."
- Organization: "Categories and Projects: Organize infrastructure with user-defined categories and project-based resource grouping."
- APIs: "v4 APIs and SDKs … Terraform and Ansible support."
- Era-current: "Intelligent Recommendations … Nutanix Intelligent Virtual Agent" (AI assistant layer).

**X-Small Prism Central blog (operational depth).**
- Prism Central = "multi-cluster management console"; XS sizing "with up to 5 clusters, 50 hosts, and 500 VMs."
- Capabilities supported on XS Prism Central (vendor enumeration — the de facto capability set of the central manager): multicluster management; VM management; Host Management; Infrastructure management, monitoring and health; enterprise authentication and RBAC; REST APIs; comprehensive search; Pulse and Nutanix Insights (telemetry/support); LCM Full-stack Update Manager; PC Backup Restore; Categories; Projects; IAMv2; connectivity to Nutanix Central; app switcher / admin center.
- Capabilities NOT in XS (i.e., higher-tier/extension surfaces): Nutanix Disaster Recovery; Nutanix Kubernetes Engine; Flow Virtual Networking; Flow Network Security; Foundation (FVM) and Foundation Central (cluster imaging/deployment machinery); NCM Self-Service / Intelligent Operations / Marketplace / Quotas / Security Dashboard / Reporting; Nutanix Files/Objects storage.
- Upgrade paths: "upgraded using the one-click upgrade or via Lifecycle Manager (LCM)."
- Related article confirms cluster profiles: "define a cluster profile in Prism Central and assign it to a group of clusters" — "a centralized blueprint for your core infrastructure settings that, instead of managing configuration options at the individual cluster level…" (positioning from summary text).

**Family structure (nav evidence — for boundary work).**
- NCI (the HCI platform: AOS Storage, AHV Virtualization, DR, Flow, NC2 cloud clusters) is separate from NCM (Nutanix Cloud Manager: Intelligent Operations, Self-Service, Cost Governance, Security Central — the multicloud/broking layer) and from NUS (Files/Objects/Volumes — file/object storage services) and NDB (database service) and NKP (Kubernetes platform).
- "NCI with External Storage (compute)" exists as a distinct product entry — the vendor itself separates converged-storage deployments from compute-over-external-storage deployments. (Boundary corroboration: the converged storage leg is what defines the HCI form.)

## Product B — VMware vSphere 9.1 (vCenter)

### Key observations (evidence layer A for doc structure; not deep page content)

**Positioning.** TechDocs featured blurb: "Transform data centers into aggregated computing infrastructures, managing CPU, storage, and networking resources." (VMware Cloud Foundation 9 blurb: "Design, plan, deploy, and manage your SDDC by using automation capabilities.")

**Management plane.** vCenter is the management server (separate deployment doc: "deploy the VMware vCenter appliance"); the vSphere Client is the UI ("Learn how to use the VMware vSphere Client components"). vSphere Authentication doc covers "certificate management and vCenter Single Sign-On configuration."

**Object/operation surface (doc-set structure — each a named doc).**
- Hosts/clusters: "vCenter and Host Management — …configure and manage hosts, and migrate virtual machines in your vCenter environment."
- Lifecycle: "Managing Host and Cluster Lifecycle — …configuring and using VMware vSphere Lifecycle Manager to manage the ESX hosts and clusters in your environment." (Stack-update machinery at host/cluster grain.)
- Configuration at cluster grain: "vSphere Configuration Profiles — manage the configuration of all hosts in a cluster collectively"; "vSphere Host Profiles."
- VMs: "create, configure, and manage virtual machines in the VMware vSphere environment."
- Networking: "create vSphere distributed switches and vSphere standard switches."
- Storage: "describes virtualized and software-defined storage technologies that VMware ESX and VMware vCenter offer, and explains how to configure and use these technologies." (The converged-storage leg of the suite; vSAN-specific pages unreachable — see Sources.)
- Availability: "vSphere High Availability (HA) and vSphere Fault Tolerance."
- Monitoring: "several tools to help you monitor your virtual environment and to locate the source of potential issues and current problems."
- Resource management, security, upgrade docs for both ESX and vCenter.
- Single-host surface exists separately: "VMware Host Client" (per-host management without vCenter).

**Interpretation for this Type (C-layer).** vSphere's converged form (suite + software-defined storage from the same hosts) is the hypervisor-suite pole of HCI management; the same vCenter operating over hosts with external SAN storage would be the sibling Type's subject (Virtualization Management). The suite itself does not rename its management console for the HCI form — the management plane is continuous; the *subject* (converged vs external storage) is what varies. This product is the boundary witness for the HCI/virtualization-management seam.

## Product C — Microsoft Azure Local (formerly Azure Stack HCI)

### Key observations (evidence layer A)

**Positioning.**
- "Azure Local is Microsoft's distributed infrastructure solution that extends Azure capabilities to customer-owned environments." "…using Azure Arc as the unifying control plane."
- "Azure Local includes all the familiar Azure management plane tooling via Azure portal, Azure CLI, and ARM templates to provision and manage resources. You can also onboard Azure services such as Azure Policy, Microsoft Defender for Cloud, Azure Monitor, and Copilot for Azure. Manage, govern, and secure your infrastructure and the workloads running on them from a single pane of glass."
- Priced "per physical core on your on-premises machines, plus any consumption-based charges for additional Azure services."
- Rename evidence: docs live under azure/azure-local; the older /azure-stack/hci path resolves into the same doc set. (Formerly Azure Stack HCI.)

**Hyperconverged deployment model (dedicated doc).**
- "A hyperconverged deployment of Azure Local consists of a machine or a cluster of machines connected to Azure. You can use the Azure portal to view, monitor, and manage individual Azure Local instances or your entire fleet. You can also manage Azure Local with your existing tools, including Windows Admin Center and PowerShell."
- "Hyperconverged deployments come in different sizes, from a single machine footprint to a maximum of 16 machines that use hyperconverged storage. They offer a unified management control plane and support a wide range of validated hardware from trusted Microsoft partners."
- "Azure Local is built on proven technologies including Hyper-V, Storage Spaces Direct, Failover Clustering, and core Azure Management service."

**Features table (direct evidence of the object domain).**
- Hardware: "Validated hardware procured from a Microsoft hardware partner. Each instance can have one to 16 Azure Local machines." Catalog + sizing tool; hardware partners enumerated (ASUS, DataON, Dell EMC, Fujitsu, HPE, Hitachi, Lenovo, NEC, QCT, Supermicro, etc.).
- Storage: "Storage Spaces Direct-based virtualized storage. External SAN storage with Fibre Channel and iSCSI is generally available for qualified vendors." (Converged storage is the default; external storage exists as a qualified variant — same seam as Nutanix's "NCI with External Storage".)
- Networking: "Customer-managed networking that uses physical switches and VLANs … with the option of enabling software-defined networking (SDN) services." SDN docs: create/manage NSGs.
- Services: "Azure Local virtual machines for general purpose VM workloads and Azure Kubernetes services (AKS) enabled by Azure Arc for containerized workloads."
- Azure management services: "Onboard Azure Arc services such as Azure Policy, Azure Monitor, and Microsoft Defender for Cloud…"
- Observability: "Metrics and logs are sent from on-premises to Azure Monitor and Log Analytics for both infrastructure and workload resources."
- Management tools (two layers, explicitly): "Cloud management via Azure portal, Azure CLI, and Azure Resource Manager/Bicep/Terraform templates. On-premises management via local tools such as PowerShell, Windows Admin Center, Hyper-V Manager, and Failover Cluster Manager."
- Disaster recovery: "Can be enabled through Azure Backup, Azure Site Recovery, and non-Microsoft partners." (Protection = integration, not the organizing core.)
- Security: "secure-by-default configuration with more than 300 security settings … drift control mechanism"; Trusted launch for VMs; Defender for Cloud posture.

**Lifecycle.**
- "Solution updates make it easy to keep the entire solution up-to-date." (Whole-solution update machinery.)
- Deployment itself runs through the Azure portal ("Deploy hyperconverged deployments" doc; rack-aware cluster deployment via portal; "Deploy using local identity with Key Vault (preview)").
- VMs: "Azure Local VMs enabled by Azure Arc — Deploy Windows and Linux VMs hosted on your Azure Local instance"; VM management prerequisites docs; monitoring docs "Azure Monitor metrics for hyperconverged deployments"; troubleshooting docs (collect logs, remote support).
- Connectivity: machines must connect via HTTPS outbound "at least every 30 days" (cloud-connected posture); "Disconnected operations" exist as a documented alternative (deploy/manage disconnected).
- Scale variants documented: single machine → 16 machines; multi-rack deployments; small-form-factor deployments; rack-aware clusters.

## Product D — Scale Computing SC//HyperCore

### Key observations (evidence layer A)

**Positioning.**
- "SC//HyperCore virtualization suite saves you time and valuable resources because your software, servers, and storage are in a fully integrated platform. The same innovative software and simple user interface power your infrastructure regardless of your hardware configuration."
- Category corroboration: Scale's review links point to the Gartner Peer Insights "hyperconverged infrastructure" market.
- "Move beyond traditional IT silos" — explicitly anti-silo framing.

**Storage convergence.**
- "NO NEED FOR TRADITIONAL STORAGE MANAGEMENT: … SCRIBE combines SC//HyperCore storage drives into a single storage pool, requiring zero user administration, and is available to all nodes of the system without requiring any file systems, protocols, or VSAs."
- "Reduce latency while eliminating the need for traditional storage management."

**Operations posture.**
- "the award-winning self-healing platform identifies, reduces, and corrects problems in real-time. Achieve results easier and faster, even when local IT resources are scarce."
- "Scale Computing's self-healing technology automatically corrects issues, so you can avoid an IT crisis… Keep systems up to date, and repair failures as part of a regularly scheduled maintenance cycle." (Update + repair folded into a maintenance cycle — the no-admin posture.)
- "SC//HyperCore virtualization suite is designed to scale as your business grows, without downtime, disruption, or rigid hardware requirements… scaling linearly or strategically with whatever hardware best meets your needs."
- "Automation & Infrastructure as Code: … integrates directly into your infrastructure-as-code workflows… programmable infrastructure."
- Simplicity as the pole: "operational simplicity and high availability from the core data center to the most distributed edge locations."

**Fleet layer.**
- SC//Fleet Manager: "Cloud-hosted command platform built for edge computing infrastructure and app delivery at scale." (Cloud-hosted fleet console over local clusters — same topology family as Prism Central/Azure portal, realized as a hosted service.)
- Family: SC//AcuVigil (managed network), SC//Connect (SD-WAN), SC//Reliant (edge computing as a service, container-first) — separate products, not the HyperCore core.

## Cross-product Comparison

| Dimension | Nutanix Prism | VMware vSphere 9.1 | Microsoft Azure Local | Scale SC//HyperCore |
|---|---|---|---|---|
| Converged subject | cluster of nodes; AOS storage + AHV/ESXi on same nodes | suite + "virtualized and software-defined storage technologies" on ESX hosts (HCI form) | cluster of 1–16 machines; Storage Spaces Direct virtualized storage | integrated platform; SCRIBE pools all node drives, "zero user administration" |
| Management plane wording | "unified management plane… single, intuitive interface" | vCenter/vSphere Client as central surface | "unified management control plane"; "single pane of glass" | "simple user interface"; "fully integrated platform" |
| Plane delivery | VM-deployed console (Prism Central, 1 or 3 VMs) + embedded per-cluster UI + cloud fleet console (Nutanix Central) | vCenter appliance + vSphere Client (+ per-host Host Client) | cloud portal (Arc) + local tools (WAC, PowerShell, Hyper-V Manager, Failover Cluster Manager) | local UI + cloud-hosted Fleet Manager |
| VM ops | templates/images, policies for placement, cross-cluster live migration | create/configure/manage VMs; migrate VMs in vCenter | Azure Local VMs enabled by Arc | (integrated; not detailed on fetched page) |
| Node/cluster lifecycle | multi-cluster management; host management; expandable sizing | host/cluster lifecycle via Lifecycle Manager; add/manage hosts | 1–16 machines; deploy via portal; rack-aware clusters | "scale… without downtime… whatever hardware best meets your needs" |
| Stack updates | "non-disruptive upgrades and firmware updates"; LCM; one-click upgrade | vSphere Lifecycle Manager for ESX hosts and clusters | "Solution updates… keep the entire solution up-to-date" | "Keep systems up to date… scheduled maintenance cycle" |
| Health/monitoring | proactive health monitoring, diagnostics, alerts; telemetry (Pulse/Insights) | vSphere Monitoring and Performance doc set | Azure Monitor metrics/logs for infra + workloads | self-healing automation; real-time correction |
| HA/failure | high availability (scale-out Prism) | vSphere HA / Fault Tolerance | Failover Clustering | self-healing / repair failures |
| Data services | protection plans, backup scheduling, native encryption | snapshots within VM/storage docs (not fetched deep) | Storage Spaces Direct features; Azure Backup/ASR integration | integrated protection (Veeam pairing marketed) |
| RBAC/identity | fine-grained RBAC, SSO, identity federation, projects/categories | vCenter SSO, authentication doc set | Azure RBAC + Azure Policy | not evidenced on fetched page |
| Multi-cluster/fleet | Prism Central (domain) → Nutanix Central (global cloud) | vCenter centrally manages many hosts/clusters | "individual Azure Local instances or your entire fleet" | Fleet Manager (cloud-hosted, edge scale) |
| API/CLI/automation | REST APIs, SDKs, Terraform/Ansible | vCenter API implied by doc set (not directly quoted) | portal, Azure CLI, ARM/Bicep/Terraform, PowerShell | IaC integration |
| Networking layer | lifecycle-based network management; microsegmentation (Flow, separate license) | standard/distributed switches | VLANs + optional SDN (NSGs) | (not detailed) |
| Hypervisor substrate | AHV own hypervisor; ESXi support | ESX (own) | Hyper-V (own OS) | own embedded virtualization (KVM-class; not asserted beyond "virtualization suite") |
| Packaging | software on certified OEM hardware | software suite | validated hardware catalog + OS (per-core subscription) | fully integrated platform (software+hardware) |

**Stable commonalities (evidence layer B).** All four: (1) a converged compute+storage cluster as the managed subject, storage software-defined from the same nodes; (2) a single management plane covering the whole stack (health + compute + storage + network + VMs), whatever the delivery surface; (3) VM lifecycle operations on the pooled resources; (4) node-grain cluster lifecycle; (5) whole-stack update machinery (lifecycle manager / solution updates / maintenance cycle); (6) failure handling as a designed behavior (HA / self-healing); (7) multi-cluster or fleet management in the mature form; (8) APIs/automation surfaces.

**Varies by product (evidence layer A, product-specific).** Where the console lives (VM-deployed, appliance, cloud portal, hosted service); whether the hypervisor is own-OS or third-party-supported; data-services depth; identity machinery; SDN/microsegmentation; DR packaging (separate product/license in Nutanix; separate Azure services; partner pairing at Scale); AI/self-healing automation depth.

## Canonical Model (L0 → L3)

### L0 — Defining Invariant (minimal)

The management application for hyperconverged infrastructure holds exactly three structures jointly:

1. **The converged cluster as the managed subject of record.** A persistent, individually identified cluster of server nodes in which each node contributes both compute and storage to shared, software-defined pools managed by the same system; storage is not an external SAN/array system, and capacity is grown/shrunk at node grain. (Remove → virtualization management over externally stored infra, or the storage/compute platform itself without a management layer.)
2. **A single management plane over the whole stack.** One consistent control surface (console and/or API/CLI) through which the administrator observes and operates the entire environment — health, compute, storage, networking, VMs — replacing separate per-component tools. Delivery form (local web console, VM-deployed manager, cloud portal, hosted fleet service) is a variant; "one plane for the whole converged environment" is the invariant. (Remove → per-node hypervisor/storage tooling; no management application.)
3. **Stack-level operating authority.** The application executes the operations the converged form exists for: provisioning and running VMs on the pooled resources, expanding/shrinking the cluster by adding/removing nodes, updating the platform stack as a unit (platform software + firmware), and keeping services available through node/disk failure (HA/rebuild/re-protect). (Remove → observe-only monitoring/inventory console.)

Jointly-held is load-bearing:
- 1 alone = the HCI platform (software-defined storage + virtualization) — a product this management ships with, not a management application.
- 2 alone = a generic infrastructure/cloud management console (subject not converged) — Virtualization Management / Cloud Management Platform territory.
- 3 alone = automation tooling with no managed environment of record.
- 1+2 without 3 = static inventory/health console.
- 2+3 without 1 = virtualization management (the sibling seam).

### L1 — Common Mature Structure

Present across the sampled products but not required to recognize the Type:

- VM lifecycle: create from templates/images, configure, start/stop, resize, live-migrate (within/across clusters), snapshot, delete.
- Health dashboards, diagnostics, alerting; telemetry to vendor/cloud services.
- Host/node management views (state, maintenance) and cluster-level configuration profiles.
- Dedicated update machinery for the stack (named "Lifecycle Manager" / "solution updates" / one-click upgrade patterns).
- Data services with varying depth (snapshots, replication, dedupe/compression/erasure coding where documented).
- RBAC + identity federation/SSO; resource organization (categories/projects/tags).
- Multi-cluster/fleet management (central manager or cloud-hosted fleet console).
- REST APIs + CLI + IaC integrations (Terraform/Ansible/PowerShell).
- Backup/DR integration surfaces.
- Optional network virtualization/microsegmentation layers.

### L2 — Variant / Optional Structure

- Packaging: software-only on certified hardware vs OEM-validated hardware catalog ("Premier Solutions", Bill of Materials) vs fully integrated turnkey platform vs hypervisor-suite extension.
- Hypervisor substrate: vendor's own hypervisor/OS (AHV, ESX, Hyper-V, Scale's embedded virtualization) vs multi-hypervisor support (Nutanix supports ESXi per its own product structure).
- Management topology: embedded per-cluster console only; + centralized multi-cluster manager; + cloud-hosted/global fleet console; legacy local tools retained alongside (WAC/PowerShell/Hyper-V Manager/Failover Cluster Manager).
- Cloud posture: cloud-connected (Arc control plane, telemetry, policy; periodic-connectivity requirements) vs documented disconnected operations.
- Scale pole: single-machine/small-footprint edge and ROBO vs multi-rack datacenter; SMB simplicity-first vs enterprise fleet governance.
- Workload extensions on the substrate: file/object storage services, Kubernetes engines, database services, VDI.
- Economics: bundled with platform (Prism "no additional cost") vs per-core subscription (Azure Local) vs platform purchase.

### L3 — Vendor-specific (Research Notes only)

- Prism Central sizing tiers and limits (XS = up to 5 clusters / 50 hosts / 500 VMs / 5 concurrent users; single-VM vs 3-VM scale-out); Nutanix Central vs Prism domain split; Foundation/Foundation Central imaging machinery; NCM (Intelligent Operations, Self-Service, Marketplace, Quotas, Security Dashboard, Reporting); Pulse/Insights telemetry; IVA AI assistant; v4 API program; Flow microsegmentation licensing; XS capability carve-outs (no DR/NKE/Flow/Files/Objects at XS).
- Azure Local specifics: 1–16 machine instances (8 max rack-aware), 300+ security settings baseline, 30-day connectivity minimum, disconnected-operations SKU, multi-rack/small-form-factor variants, per-core pricing, Azure Local Catalog partner list.
- vSphere specifics: doc-set naming (vSphere Configuration Profiles vs Host Profiles transition), VMware Host Client single-host surface, VMware Cloud Foundation suite framing.
- Scale specifics: SCRIBE pooling design, SC//Fleet Manager, AIME (Autonomous Infrastructure Management Engine, per video title), AcuVigil/Reliant satellites.
- Dell VxRail: not researched (unreachable); appliance-pole observations drawn only from the two vendors' own validated-hardware/integrated-platform documentation.

## Vendor-specific Findings

- The two-level manager topology (embedded per-cluster console + separate central manager) is explicit at Nutanix (Prism Element heritage → Prism Central → Nutanix Central) and structurally present at Scale (HyperCore UI + Fleet Manager) and Microsoft (WAC local + Azure portal fleet). VMware realizes it differently: one vCenter is itself the central manager, with a separate per-host client — so "embedded + central" is common but NOT definitional (VMware counter-shape).
- The vendor's own product splits mark the adjacent Types: Nutanix ships Prism (infrastructure management) separately from NCM (multicloud/self-service/cost), NUS (file/object), NDB, NKP; Microsoft ships Azure Backup/ASR as separate services; Scale pairs with Veeam. Protection, self-service, cost governance, Kubernetes, file/object are extensions, not the HCI management core.
- Azure Local documents external SAN (FC/iSCSI) for qualified vendors and Nutanix lists "NCI with External Storage" — both vendors treat external-storage compute as a distinct form, corroborating that converged storage is definitional (L0 leg 1), with external-storage as a documented minority variant.

## Boundary Findings

- **vs Virtualization Management (closest sibling).** Same VM/host vocabulary, but the subject differs: virtualization management operates VMs/hosts over whatever storage exists (external arrays included); HCI management's subject is the converged cluster where software-defined storage comes from the same nodes and the plane operates the whole stack (storage pool + compute + node lifecycle + stack updates) as one system. Test: remove the converged storage leg (point the hosts at an external SAN) and the same console continues as virtualization management — the HCI subject is gone. Counter-shape witness: VMware's vCenter serves both forms without changing its identity — the Types are distinguished by deployment subject, not by product name.
- **vs Storage Management.** Storage Management's subject is storage systems (arrays, volumes, data stores); HCI management always co-operates compute and treats storage as one pooled fabric of the cluster it manages. A storage-only console cannot be HCI management no matter how software-defined.
- **vs Server Management Platform.** Server management operates individual machines (hardware health, firmware, OS) without pooled-storage/VM-fabric semantics. HCI management includes node/firmware operations but subordinated to the cluster's pooled operation.
- **vs Cloud Management Platform.** CMP brokers multiple clouds (self-service, cost, multicloud orchestration). HCI management operates the organization's own converged infrastructure. Vendor-confirmed split: Nutanix Prism (NCI management) vs Nutanix Cloud Manager; Microsoft's Arc layer straddles (the portal is a cloud surface managing on-prem infra) — hence plane *delivery* is variant, not definition.
- **vs Data Center Infrastructure Management (DCIM).** DCIM's subject is the facility layer (power, cooling, racks, PDU). Disjoint subject; no overlap of centers.
- **vs Infrastructure Monitoring.** Monitoring observes; HCI management operates (provisions, expands, updates, heals). Health monitoring with alerts is inside HCI management as a capability, but observe-only products fail the operating-authority leg.
- **vs Backup Management / Disaster Recovery Platform.** Protection exists in every sampled product only as data services or integrations (separate products/licenses/services). The organizing center of HCI management is operating the converged environment, not data protection.
- **vs Kubernetes Management Platform.** Container platforms (NKP, AKS on Arc) ride on the HCI substrate as extensions; the HCI management plane's native workload unit remains the VM.

### "Remove what to become another Type" judgments

- Remove the converged-storage subject (external SAN) → Virtualization Management.
- Remove the operating authority (observe-only) → Infrastructure Monitoring.
- Remove the whole-stack scope (storage ops only) → Storage Management.
- Remove the infrastructure subject (multicloud brokering/self-service/cost) → Cloud Management Platform.
- Remove the software-defined cluster (single machines' firmware/OS) → Server Management Platform.

## Historical / Market-Sample Check (§24)

HCI as a category is software-era (no paper ancestor): the "older product" check is therefore structural rather than generational. The frozen L0 contains no cloud connectivity, no AI/self-healing automation, no managed-fleet services, no IaC, and no specific hypervisor. A first-generation HCI product — a web console over a converged cluster providing health views, VM provisioning, node expansion, and stack upgrades — satisfies all three legs. Conversely, the era-current layers observed in the sample (cloud control planes/Arc, AI recommendations, self-healing engines, global fleet consoles, disconnected-operations modes) are correctly held at L1/L2, not in the definition. Hypervisor plurality (AHV/ESX/Hyper-V/embedded) and packaging plurality (software-only/validated-hardware/integrated) both satisfy the L0 — the definition does not over-fit to the appliance pole or the cloud-connected pole. (Canonical inference, evidence layer C — the sampled set is current-market.)

## Uncertainties

1. vSAN operational specifics were not directly documented in this pass (dedicated doc pages unreachable); the VMware column rests on the fetched vSphere doc-set structure and descriptions. Assertions about VMware's storage layer are kept at the "software-defined storage technologies" level of the fetched text.
2. Dell VxRail (the classic appliance pole) was unreachable; the appliance/validated-hardware form is evidenced via Azure Local's partner-hardware model and Scale's integrated-platform description, not via VxRail itself. No VxRail-specific claims are made anywhere.
3. Scale Computing's RBAC/identity machinery and VM-operation depth were not evidenced on the fetched pages (marketing-grade page only); corresponding claims are not made.
4. Data-services depth (dedupe/compression/erasure coding specifics) varies per product and was only partially documented on fetched pages; held generic in the final document.
5. Whether a pure "external-storage HCI management" product exists as a distinct market shape (compute-only pole) was not researched; both vendors' external-storage entries suggest it is a variant, not a separate market.
6. The rename Azure Stack HCI → Azure Local is evidenced by doc paths, not by an official rename announcement; treated as established but cited via the docs.

## Final Synthesis

Hyperconverged Infrastructure Management is the operator's single management plane over a converged compute+storage cluster. Its defining core is three jointly-held structures: (1) the converged cluster of record — nodes each contributing compute and storage to shared software-defined pools, expanded/shrunk at node grain; (2) one management plane over the whole stack — health, compute, storage, network, and VMs operated through one consistent surface family (delivery surface varies: local console, VM-deployed manager, cloud portal, hosted fleet service); (3) stack-level operating authority — provisioning VMs on the pooled resources, expanding/shrinking the cluster, updating the platform stack as a unit, and keeping services available through failure. Everything else observed — self-healing/AI automation, cloud-connected fleet services, data-services depth, RBAC, APIs, hypervisor choice, packaging form — is common mature structure or variant, not definition. The Type's sharpest seam is with Virtualization Management: remove the converged storage subject and the same console becomes that sibling Type; the two are distinguished by the managed subject, not by product naming.
