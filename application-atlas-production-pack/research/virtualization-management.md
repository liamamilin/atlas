# Research Notes — Virtualization Management

## Research Goal

Understand what "Virtualization Management" is as an Application Type: what object domain it operates (virtual machines, hypervisor hosts, clusters/pools, virtual hardware), which operations define it (create/configure/power/snapshot/migrate VMs; manage hosts), how the management layer relates to the hypervisor it operates, and where its boundaries sit against neighboring §14 Types (Hyperconverged Infrastructure Management, Storage Management, Server Management Platform, Container Management, Cloud Management Platform, Desktop Application Delivery, Backup Management, Infrastructure Monitoring, Capacity Management, IaC).

Context: the leaf sits in §14 IT, Cloud & Infrastructure. Three sibling passes have pre-hung boundary notes for this leaf:

1. **hyperconverged-infrastructure-management (2026-09-08)**: the hypervisor-suite pole (vCenter-class console) serves BOTH types depending on deployment subject — over external SAN storage it operates as virtualization management, over its own software-defined storage on the same hosts as HCI. "The future virtualization-management pass should treat converged-storage deployments as this leaf's territory [i.e., NOT this leaf's]."
2. **storage-management (2026-09-09)**: ratified — the managed subject decides: the storage layer itself (drives→pools→volumes/LUNs/shares/buckets) = storage-management territory; **VMs over arbitrary infrastructure = virtualization-management territory**; converged compute+storage clusters = HCI territory; a hypervisor console's datastore view touches storage objects but its center of gravity is the VM.
3. **server-management-platform (2026-09-09)**: NEW FLAG — proposed seam: VM as hypervisor-level object (create/start/snapshot/migrate, host resources) vs VM as OS-level managed machine (Uyuni Virtual Host Managers manage VMs AS SYSTEMS); keep-both expected.

## Initial Boundary

- What it probably is: the operator-facing application that manages virtual machines and the hypervisor hosts that run them — VM lifecycle, host/cluster management, virtual networking and storage presentation, templates, migration, HA.
- Nearest neighbors: HCI Management (converged subject), Storage Management (storage layer), Server Management Platform (OS-layer machine management), Container Management (container workloads), Cloud Management Platform (multi-cloud brokering), Desktop Application Delivery (consumes hypervisors for VDI), Infrastructure Monitoring (observe-only), Capacity Management (planning over time), Backup Management (protection layer).
- Unknowns: does the defining core require multi-host centralization, or does a single-host hypervisor console qualify? Is virtual networking/storage configuration definitional or common? Do guest agents, HA, migration belong in the core?

## Research Questions

1. What is the central object of record, and what does the product hold about it (config, state, placement)?
2. How are hypervisor hosts modeled — and what does "host management" mean (add, patch, profile, lifecycle)?
3. What is the full VM lifecycle: creation (blank/template/clone/import), configuration (virtual hardware), power ops, snapshots, migration, removal?
4. What is the management-layer architecture: standalone console vs central management server vs integrated platform?
5. How do virtual networking and storage appear — as first-class managed objects or as VM-attachment context?
6. What roles/permissions exist (admin vs self-service/VM-user surfaces)?
7. What automation surfaces exist (CLI, API, providers)?
8. Where exactly are the seams with HCI, storage, server, container, and cloud management?

## Representative Products

Selection logic: market representation + documentation completeness + different product philosophies + different customer tiers.

| Product | Philosophy / tier | Hypervisor substrate |
|---|---|---|
| VMware vSphere (ESX + vCenter) | proprietary enterprise incumbent; full management suite | bundled (ESX) |
| Microsoft System Center VMM | manager inside a Microsoft management suite; Windows datacenter | manages Hyper-V hosts (and VMware hosts) |
| Proxmox VE | open-source integrated platform (hypervisor + management in one product) | bundled (QEMU/KVM + LXC) |
| oVirt (Red Hat Virtualization lineage) | open-source central-management engine over KVM hosts | managed (KVM) |
| Xen Orchestra (Vates) | agent-less manager over an existing open-source Xen stack | managed (XCP-ng/XenServer) |

This sample covers: bundled-suite pole (vSphere), suite-manager pole (SCVMM), integrated open-source platform (PVE), engine-over-hosts pole (oVirt), agent-less external manager (XO). It also contains the boundary witnesses for HCI (vSphere's converged form), containers (PVE's LXC), and multi-hypervisor management (SCVMM).

## Sources

Research date: **2026-09-09**

- VMware vSphere 9.1 documentation (Broadcom TechDocs): product doc map — https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1.html ; VM Administration map — …/vsphere-virtual-machine-administration.html (A)
- Microsoft Learn, "What is Virtual Machine Manager?" (SCVMM 2025) — https://learn.microsoft.com/en-us/system-center/vmm/overview?view=sc-vmm-2025 (A)
- Proxmox VE wiki Main Page — https://pve.proxmox.com/wiki/Main_Page (A); QEMU/KVM Virtual Machines chapter — https://pve.proxmox.com/wiki/QEMU/KVM_Virtual_Machines (A)
- oVirt Documentation index — https://ovirt.org/documentation/ (A); Virtual Machine Management Guide — https://ovirt.org/documentation/virtual_machine_management_guide/index.html (A)
- Xen Orchestra documentation intro — https://xen-orchestra.com/docs/ (A)

Source-access limitations: two attempts at deeper Microsoft Learn SCVMM pages (`manage-vms`, `library-overview`) returned 404; only the SCVMM overview page was reachable — Microsoft evidence is A-layer on the overview's stated capability set, and no deeper Microsoft operational detail is claimed. `pve.proxmox.com` wiki article-path variants 404'd twice before `Main_Page` succeeded; PVE evidence is Tier-1 but from two pages only. No product-specific numeric/limit claims are made beyond what the fetched pages state.

## Product Observations

### VMware vSphere (ESX + vCenter) — evidence layer A

From the vSphere 9.1 documentation map and guide descriptions:

- Documentation structure itself maps the Type's object domain: ESX Install/Upgrade (hypervisor), vCenter Deployment/Upgrade/Configuration (central management server), vSphere Authentication (SSO/certificates), **vCenter and Host Management** ("configure and manage hosts, and migrate virtual machines in your vCenter environment"), **Managing Host and Cluster Lifecycle** (Lifecycle Manager for ESX hosts/clusters), **vSphere Configuration Profiles** ("manage the configuration of all hosts in a cluster collectively"), Host Profiles, **vSphere Virtual Machine Administration** ("create, configure, and manage virtual machines"), vSphere Networking (standard and distributed switches), vSphere Storage, vSphere Security, vSphere Resource Management, vSphere Availability (HA, Fault Tolerance), vSphere Monitoring and Performance, and **Single Host Management — VMware Host Client** (managing a single host without vCenter).
- VM definition (VM Administration guide): "A virtual machine is a software computer that, like a physical computer, runs an operating system and applications. The virtual machine consists of a set of specification and configuration files and is backed by the physical resources of a host. Every virtual machine has virtual devices that provide the same functionality as physical hardware but are more portable, more secure, and easier to manage."
- VM Administration coverage: creating/deploying VMs, templates, and clones; OVF/OVA deploy/export; **content libraries** ("container objects for VM and vApp templates and other types of files, such as ISO images"); configuring VM hardware; VM options ("VMware Tools scripts, control user access to the remote console, configure startup behavior"); **vApp** (package multiple interoperating VMs as one unit); managing VMs "including using snapshots"; upgrading VMs (compatibility level + VMware Tools); troubleshooting.
- Audience: "experienced Windows or Linux system administrators who are familiar with virtualization."
- Boundary witness: this same suite is the HCI pass's hypervisor-suite pole — with vSAN/converged storage it serves HCI management; with external storage it operates as virtualization management. The console identity is continuous; the deployment subject varies.

### Microsoft System Center VMM — evidence layer A

From the SCVMM 2025 overview:

- Positioning: "part of the System Center suite used to configure, manage, and transform traditional datacenters… unified management experience across on-premises, service provider, and the Azure cloud."
- **Fabric** concept: "Configure and manage your datacenter components as a single fabric… Datacenter components include virtualization servers, networking components, and storage resources. VMM provisions and manages the resources needed to create and deploy virtual machines and services to private clouds."
- Hosts: "VMM can add, provision, and manage **Hyper-V and VMware** virtualization hosts and clusters" (multi-hypervisor management — product-specific).
- Networking: network sites (IP subnets, VLANs), logical switches, static IP and MAC pools, network virtualization for tenant isolation, gateways.
- Storage: "discover, classify, provision, allocate, and assign local and remote storage… block storage (FC, iSCSI, SAS SANs)" — storage appears inside the fabric as VM-deployment context.
- **Library**: "a library of file-based and non file-based resources that are used to create and deploy VMs and services… file-based resources include virtual hard disks, ISO images, and scripts. Non file-based resources include templates and profiles that are used to standardize the creation of VMs." Accessed through library shares.
- Azure Arc onboarding: self-service VM management with Azure RBAC; SDKs/Terraform/ARM/Bicep/REST/CLI/PowerShell; Azure services (Defender, Monitor, Update Manager, Policy) applied to SCVMM VMs (product-specific, hybrid-cloud bridge).

### Proxmox VE — evidence layer A

From the wiki Main Page and the QEMU/KVM Virtual Machines chapter:

- Self-definition: "an open source server virtualization management solution based on QEMU/KVM and LXC. You can manage virtual machines, containers, highly available clusters, storage and networks with an integrated, easy-to-use web interface or via CLI."
- Two workload kinds: QEMU/KVM VMs **and LXC containers** (container workloads as a product variant, not the Type's core).
- Documentation sections: Host System Administration (package repositories, network configuration, system software updates, disk health), Cluster Manager ("connect your Proxmox VE hosts in clusters"), High Availability ("for your virtual machines and containers once you have setup a cluster"), Storage (RBD, ZFS, iSCSI, NFS, PBS, …), hyper-converged Ceph deployment (HCI pole as an optional deployment), Backup and Restore, Firewall, Software-Defined Network, User Management (authentication + permissions).
- VM creation settings (web GUI): **Node** (physical server the VM will run on), **VM ID** (unique number in the installation), Name, **Resource Pool** ("a logical group of VMs"); OS type (optimizes low-level parameters); System (display type, SCSI controller, **QEMU Agent** checkbox — guest agent lets PVE "show some more information, and complete some actions (for example, shutdown or snapshots) more intelligently"; firmware SeaBIOS/OVMF; machine type/version); Hard Disk (bus/controller incl. VirtIO, image format raw/qcow2, cache mode, discard/TRIM, SSD emulation, IO thread, no-backup, skip-replication); CPU (sockets/cores; **cpulimit**; **cpuunits** weight; affinity; CPU type chosen with live-migration compatibility in mind).
- Migration chapter: cluster required; **Online (live) Migration** vs **Offline Migration**; `qm migrate <vmid> <target>`; the web interface defaults to live migration when the VM is running. Live-migration compatibility shaped by CPU-type and machine-version choices.
- Other chapters: Copies and Clones; Virtual Machine Templates; Importing Virtual Machines; Hibernation (suspend-to-disk, with state-storage selection); Snapshots (stored as config sections with `parent`/`snaptime`; optional `vmstate` memory); **Locks** (configuration locking); `qm` CLI as a full management surface.
- Product-specific rule: "Proxmox VE will prevent you from starting VMs with more virtual CPU cores than physically available."

### oVirt — evidence layer A

From the documentation index and the Virtual Machine Management Guide:

- Definition: "A virtual machine is a software implementation of a computer. The oVirt environment enables you to create virtual desktops and virtual servers."
- Two portals: **VM Portal** and **Administration Portal** — "Most virtual machine tasks… can be performed in both the VM Portal and Administration Portal… Which portal you use, and which tasks you can perform in each, is determined by your level of permissions."
- REST API documented as a first-class management surface; Ansible roles/collections, Python/Java/Ruby SDKs.
- VM creation procedure (New Virtual Machine window): select Operating System, Name; attach or create a virtual disk; add a network interface by selecting a **vNIC profile**; specify **Memory Size**; choose boot **First Device** → created with status **Down** → **Run** → status **Up**.
- Status vocabulary and operations: starting, shutting down, suspending, rebooting/resetting, removing, cloning.
- **VM will not start on an overloaded host** ("By default, a host's CPU is considered overloaded if it has a load of more than 80% for 2 minutes, but these values can be changed using scheduling policies" — product-specific defaults).
- Guest agents and drivers (virtio family, qemu-guest-agent): graceful shutdown/reboot from the portals; report resource usage and IP addresses.
- Consoles: SPICE/VNC/RDP via Remote Viewer; `console.vv` ticket file; serial console proxied by the Engine over SSH with per-user keys.
- Editing VMs: network interfaces (add/edit/hot-plug/remove), virtual disks (add/attach/extend/hot-plug/remove), virtual memory and vCPU hot plug/unplug, host pinning, CD change, smart cards, watchdog, virtual NUMA, headless VMs.
- **Snapshots**: create, use to restore, create a VM from a snapshot, delete.
- **Live migration**: manual and automatic; prerequisites; priority; canceling; preventing automatic migration; migration events/notifications. **VM High Availability**: configure a highly available VM. **Affinity groups/labels**: keep VMs together/apart.
- **Permissions**: Virtual Machine Administrator Roles and User Roles; assign VMs to users; remove access.
- **Templates**: create from a VM, seal with `virt-sysprep`, edit/delete/export/import, Cloud-Init and Sysprep for initial-run configuration, clone from template. Also VM pools.
- **Import/export**: from a VMware provider, from a KVM host, from a RHEL 5 Xen host, via export/data domains (V2V in-product).
- Architecture named in docs: the **Engine** (management server) and **hosts**; self-hosted engine (Manager runs as a VM in the environment it manages) — a distinctive deployment form.

### Xen Orchestra (Vates) — evidence layer A

From the documentation intro:

- Self-definition: "the complete solution to **visualize, manage, back up and delegate** your XCP-ng (or XenServer) infrastructure: any number of pools, on any site, from one place. **No agent** is required."
- Administration: "complete control of your pools, hosts, VMs, storage and networks, from a modern web interface or from XO 5" (two web interfaces, one server).
- Backup/DR: rolling snapshots, full and incremental backups, replication, mirroring, immutability toward S3/NFS/SMB/Azure targets.
- Migration: **V2V** — "import your ESXi VMs directly into your pools" (VMware-to-Xen import in-product).
- Automation: REST API, CLI, and providers for Terraform, Ansible, Pulumi, Packer, PowerShell; Kubernetes recipes.
- Delegation: users, groups, **RBAC** "to give each team exactly the access it needs."
- Scale: "one XO manages any number of pools on any number of sites, over LAN or WAN."
- Diagram of estate shape: team → XO → pools (multi-site) → hosts → VMs; backup repository separate.

## Cross-product Comparison

| Structure | vSphere | SCVMM | Proxmox VE | oVirt | Xen Orchestra | Layer |
|---|---|---|---|---|---|---|
| VM as managed record (software computer, virtual hardware + run state) | Y ("software computer… set of specification and configuration files") | Y (provisions/manages VMs; library resources to create them) | Y (VM ID/name/node/settings) | Y ("software implementation of a computer", Down→Up) | Y (VMs managed over pools) | **L0** |
| Hypervisor host as managed substrate | Y (host management, host client, host profiles, lifecycle manager) | Y ("add, provision, and manage Hyper-V and VMware hosts and clusters") | Y (Node; Host System Administration; Cluster Manager) | Y (hosts; host pinning; Engine↔hosts) | Y (hosts inside pools) | **L0** |
| VM lifecycle authority (create/configure/power/snapshot/migrate/remove) | Y (deploy/config/snapshots; "migrate virtual machines") | Y (provision and deploy VMs) | Y (create/migrate/hibernate/snapshot/clone/templates) | Y (full VM management guide) | Y (manage; snapshots; backup/replication) | **L0** |
| Central management layer above hosts | Y (vCenter) | Y (VMM server) | Y (web UI over cluster) | Y (Engine; self-hosted engine) | Y (XO server, agent-less) | L1 |
| Host clustering / estate grouping | Y (clusters, data centers) | Y (host clusters; fabric) | Y (clusters; resource pools) | Y (clusters; data centers; affinity groups) | Y (pools) | L1 |
| Templates/clones + image library | Y (templates, OVF/OVA, content libraries) | Y (library: VHDs, ISOs, scripts, templates, profiles) | Y (templates, clones, imports) | Y (templates, sealing, VM pools) | Y (backup repository; VM copies) | L1 |
| Snapshots | Y | implied (VM management) | Y (config-section snapshots, vmstate) | Y (create/restore/branch) | Y (rolling snapshots) | L1 |
| Live migration between hosts | Y ("migrate virtual machines in your vCenter environment") | Y (within managed hosts) | Y (online/offline) | Y (manual/automatic, priorities) | Y (replication/mirroring; live migration via XCP-ng toolstack) | L1 |
| VM high availability / restart-on-failure | Y (HA, Fault Tolerance) | Y (private-cloud services) | Y (HA after cluster setup) | Y (VM HA config) | Y (HA via pool features) | L1 |
| Guest agents/drivers | Y (VMware Tools, VM options) | Y (implied by library scripts/roles) | Y (QEMU Agent option) | Y (virtio + guest agents, explicit) | N/A (agent-less manager; hypervisor-side tools) | L1 (substrate varies) |
| Virtual networking configuration | Y (standard/distributed switches) | Y (logical switches, VLANs, IP/MAC pools) | Y (SDN; network config per host) | Y (vNIC profiles) | Y (networks listed among managed objects) | L1 |
| Storage presentation for VMs | Y (vSphere Storage guide) | Y (discover/classify/provision/assign) | Y (storage backends per VM disk) | Y (storage domains; attach/create disks) | Y (storage among managed objects) | L1 (center of gravity = VM) |
| Embedded monitoring/performance views | Y (Monitoring and Performance guide) | Y (via suite/Arc services) | Y (host/VM views; external metric servers) | Y (Engine events; Data Warehouse guide) | Y (dashboard) | L1 (observe-only deep monitoring = Infrastructure Monitoring territory) |
| RBAC / roles / self-service surface | Y (authentication; roles in client) | Y (Azure RBAC via Arc; self-service) | Y (user management, permissions) | Y (admin vs user roles; VM Portal) | Y (RBAC, delegation) | L1 |
| CLI / API / automation | Y (vSphere client + APIs; automation surface) | Y (PowerShell, SDKs, Terraform/ARM/Bicep) | Y (qm CLI, API) | Y (REST API, SDKs, Ansible) | Y (REST, CLI, Terraform/Ansible/Pulumi) | L1 |
| Host patch/upgrade machinery | Y (Lifecycle Manager, ESX Upgrade) | Y (via suite/Azure Update Manager) | Y (package repositories, updates) | Y (host reinstall; upgrade guide) | Y (via XCP-ng host tooling) | L1 |
| Multi-hypervisor management | (suite-bound) | **Y — manages Hyper-V AND VMware** (product-specific) | (bundled QEMU/KVM + LXC) | (KVM; imports from VMware/KVM/Xen) | (XCP-ng/XenServer; V2V from ESXi) | L2 variant |
| Container workloads alongside VMs | N (separate products) | N | **Y — LXC** (product-specific variant) | N | N | L2 variant |
| HCI/converged-storage deployment | Y (vSAN form — witness for the HCI seam) | N | Y (Ceph HCI deployment optional) | (RHV HCI existed; oVirt sample docs show DR/warehousing, not converged pole) | N | L2 → HCI territory |
| Cloud-connected control plane | (VCF fleet context) | **Y — Azure Arc onboarding** (product-specific) | N (Proxmox Datacenter Manager is separate) | N | N | L2 variant |

**Interpretation (C-layer).** Every sampled product, regardless of architecture, holds the same three-part structure: a persistent VM record (a software computer with virtual hardware and run state), managed hypervisor hosts as the resource substrate, and operating authority over the VM lifecycle against those hosts. Everything else — centralization, clustering, templates, migration, HA, networking/storage surfaces, RBAC, monitoring, automation — is the common mature dressing that makes the estate operable at scale, and it appears with varying depth but without changing the subject.

## L0 — Defining Invariant (minimal)

**Virtualization Management is the operator's control layer over virtual machines and the hypervisor hosts that run them.** The defining core is exactly three jointly-held structures:

1. **The virtual machine as the managed object of record** — a persistent identified software computer whose virtual hardware (vCPU, memory, virtual NICs, virtual disks, boot/firmware settings) and run state (powered on/off/suspended) are held as managed configuration, operated at the hypervisor layer. Remove → hypervisor installer/host OS tooling, or a VM inventory nobody operates.
2. **The virtualization host as the managed resource substrate** — hypervisor hosts whose physical CPU/memory/storage/network back the VMs, held as managed members of the estate (add/register/configure). Remove → a VM list with no placement or resource substrate = bare inventory.
3. **VM lifecycle authority against the hypervisor layer** — create, configure, power, snapshot, migrate, and remove VMs through the manager, with placement on hosts. Remove → observe-only console = Infrastructure Monitoring territory; manage-the-guest-OS instead = Server Management territory.

Jointly-held load-bearing: (1) alone = VM inventory; (2) alone = host inventory; (3) without 1+2 = free-floating ops scripts; (1)+(3) without 2 = VM operations with nowhere to place VMs (cloud-console-shaped, not hypervisor-estate management); (2)+(3) without 1 = host management with no VM object = partial (pre-VM hypervisor tooling).

**Anti-overfitting notes:**
- **Multi-host centralization is NOT definitional** — the vSphere docs ship a dedicated manual for single-host management without vCenter (A-layer evidence that single-host hypervisor consoles are a recognized form of this Type). Centralized multi-host management is L1.
- **Virtual networking / storage configuration is NOT definitional as first-class estate objects** — it appears everywhere, but its role is to give VMs networks and disks; the center of gravity stays the VM. The storage layer itself is Storage Management territory (ratified seam).
- **Guest agents are NOT definitional** — XO is explicitly agent-less; agents are the common optimization layer (graceful ops, IP reporting).
- **Specific hypervisor, container support, HCI form, cloud connection, any AI/era-current machinery** — all L2/L3.

## L1 — Common Mature Structure

Present across the sample with varying depth; expected in any mature product but not required to recognize the Type:

- central management layer above hosts (management server, appliance, or web UI spanning the estate)
- host clustering / estate grouping (clusters, pools, data centers, resource pools) with placement/scheduling policies
- templates, clones, and an image/library layer (ISOs, OVF/OVA, VHDs, customization: Cloud-Init/Sysprep/guest customization)
- snapshots; integrated or adjacent backup/replication machinery
- live migration between hosts (online/offline forms); VM high availability
- virtual networking configuration and storage presentation as VM-attachment context
- guest agents/paravirtualized drivers as the optimization layer
- embedded monitoring/performance/event views
- RBAC with distinct administrator vs self-service surfaces (e.g., portals for VM users vs estate admins)
- CLI/API/automation surfaces (PowerShell, qm, REST, Terraform/Ansible providers)
- host patch/upgrade/profile machinery (lifecycle management, host profiles)

## L2 — Variant / Optional Structure

- **Hypervisor substrate**: bundled proprietary (ESX, Hyper-V), KVM (oVirt, PVE), Xen (XCP-ng/XenServer)
- **Architecture**: integrated platform (hypervisor + manager as one product: PVE, vSphere suite) vs standalone manager over existing hypervisors (SCVMM, XO, oVirt Engine)
- **Multi-hypervisor management**: one manager for several hypervisors (SCVMM manages Hyper-V + VMware) — product-specific in the sample
- **Container workloads alongside VMs** (PVE's LXC) — variant of the workload domain
- **HCI/converged-storage deployment** of the same consoles → serves the sibling HCI Type (see Boundary Findings)
- **Cloud-connected control plane** (Azure Arc onboarding of SCVMM; fleet services) — hybrid-era variant
- **Scale posture**: single-host console vs multi-host cluster estates vs multi-site managers (XO over WAN pools)
- **Management-server deployment form**: Windows service (SCVMM), appliance/VM (vCenter), self-hosted engine (oVirt — the manager runs as a VM inside the estate), external agent-less server (XO), web UI embedded in hosts (PVE)
- Import/export postures: in-product V2V (XO from ESXi; oVirt import from VMware/KVM/Xen) vs OVF file exchange

## L3 — Vendor-specific Structure (research notes only)

- vSphere: content libraries as named objects; vApp packaging of multi-VM applications; Fault Tolerance; vSphere Configuration Profiles as the successor direction for Host Profiles; Host Client naming; VMware Tools/VM options; vCenter SSO.
- SCVMM: **fabric** as the umbrella noun for hosts+network+storage; library shares; private clouds as deployment targets; Azure Arc-enabled SCVMM specifics (Defender/Monitor/Update Manager/Policy from Azure).
- Proxmox VE: VM ID as the primary VM identifier; resource pools as "logical group of VMs"; machine-version pinning and the `+pveX` revision scheme; locks; qm/pvesh CLI verbs; Proxmox Backup Server integration; LXC coexistence.
- oVirt: Engine + self-hosted engine architecture; vNIC profiles; affinity groups/labels; sealing with virt-sysprep; console.vv ticket files; scheduling-policy overload defaults (80%/2min); Data Warehouse; export/import domains.
- Xen Orchestra: XO 5 vs XO 6 dual interface; XOA appliance; agent-less posture as a marketing/technical claim; V2V from ESXi; immutability targets (S3/NFS/SMB/Azure).

## Vendor-specific Findings (not promoted to canonical core)

- PVE prevents starting VMs with more vCPUs than physical cores (product-specific rule).
- oVirt's default overload threshold (80% for 2 minutes) is a scheduling-policy default, not a Type rule.
- XO's "no agent" is a product design choice; other products rely on in-guest agents.
- SCVMM's cross-hypervisor management (Hyper-V + VMware) is the sample's only multi-hypervisor pole.

## Rejected Findings (considered and not placed in the core)

- "Virtualization management = cloud VM console" — rejected: provider-operated IaaS consoles share the VM-lifecycle shape but the substrate is a provider-operated cloud platform, and estate brokering belongs to Cloud Management Platform; this Type centers on operator-run hypervisor estates. SCVMM's Arc bridge is a variant, not the definition.
- "Backup is definitional" — rejected: backup/DR machinery appears in most products (PVE, XO, oVirt DR guide) but is the Backup Management layer; a product without integrated backup still unmistakably is virtualization management.
- "HA is definitional" — rejected: present broadly but requires clusters; single-host consoles lack it and remain in-type.
- "Multi-host is definitional" — rejected on the single-host manual evidence (vSphere Host Client).
- "Containers are definitional" — rejected: one product in the sample carries LXC; the managed unit that defines this Type is the VM.

## Boundary Findings

1. **vs Hyperconverged Infrastructure Management (ratified seam, discharged from this side)**: the managed subject decides. VMs over arbitrary infrastructure (external storage included) = this Type; converged compute+storage clusters whose storage comes from the same nodes = HCI territory. The hypervisor-suite console (vCenter-class) is the boundary witness: over external SAN it operates as this Type, over its own software-defined storage as HCI. Converged-storage deployments are NOT this leaf's territory.
2. **vs Storage Management (ratified seam, corroborated from this side)**: the storage layer itself (drives→pools→volumes/LUNs/shares/buckets) = Storage Management. In this Type, datastores/storage domains appear as VM-attachment targets; the hypervisor console's storage view touches storage objects but its center of gravity is the VM. Remove the VM and operate the storage layer → Storage Management.
3. **vs Server Management Platform (flag DISCHARGED, keep-both ratified from this side)**: the VM enters this Type as a **hypervisor-level object** (virtual hardware config, power state, snapshots, live migration, placement on hosts). In Server Management, a VM enters as an **OS-level machine** (discovered/registered record managed through the OS's own package/execution machinery — the Uyuni Virtual Host Manager pattern). The same VM is legitimately the subject of both Types at different layers; remove the hypervisor layer (manage the guest OS through its OS channels) → Server Management territory.
4. **vs Container Management (container pass's seam, corroborated)**: managed unit is the seam — containers (from images, runtime-operated) vs VMs (hypervisor-operated). Convergence exists (PVE manages LXC alongside VMs; orchestrators can schedule VMs as tasks) but the defining unit here is the VM. Remove VMs, manage container workloads → Container Management.
5. **vs Cloud Management Platform**: a CMP brokers multi-cloud estates (account/resource/cost governance); this Type performs hypervisor- and host-specific operations directly. A CMP treats a hypervisor estate as one estate member among others. Remove direct hypervisor operations, add multi-cloud brokering → CMP.
6. **vs Desktop Application Delivery (VDI)**: VDI consumes this layer — supported hypervisors appear there as connections, not as the product's subject. Delivery of interactive sessions to end users vs operating the VM/host estate.
7. **vs Infrastructure Monitoring**: the management plane embeds performance/event views, but its defining act is control. Observe-only with alerting → Infrastructure Monitoring.
8. **vs Capacity Management**: lifecycle/config authority vs supply-vs-demand planning over time; management platforms may bundle capacity views.
9. **vs Backup Management / DR Platform**: protection-point custody is the sibling Type's subject; integrated backup in PVE/XO is common structure.
10. **vs IaaS cloud consoles / CMP boundary**: when the VM substrate is a provider-operated cloud and the surface is the provider's service console, the estate is the provider's, not the customer's hypervisor estate — the canonical VM-lifecycle shape recurs, but the Type as sampled is the operator-run hypervisor estate. Recorded as a boundary observation for the CMP/cloud-console passes, not resolved here.

**"去掉什么就变成另一个 Type" 判据 (remove-tests)**:
- Remove VMs as the managed record, keep converged compute+storage → HCI Management.
- Remove the VM center of gravity, manage drives→pools→volumes → Storage Management.
- Remove the hypervisor layer, manage VMs as OS-level machines → Server Management Platform.
- Replace VMs with containers/images → Container Management.
- Remove direct hypervisor operations, broker multi-cloud estates → Cloud Management Platform.
- Remove control authority (keep observation) → Infrastructure Monitoring.

## Historical / Market-Sample Check (per workflow §24 spirit)

Would older, regional, platform-native, or differently positioned products still fit?

- The vSphere documentation set itself still ships **Single Host Management** as a first-class manual — a bare hypervisor with a host-level client is a recognized operating form; it contains VM records, a host, and lifecycle authority, and nothing else from the L1 list.
- Platform-native consoles (e.g., a hypervisor's bundled manager) and earlier-generation centralized managers (VirtualCenter-era, XenCenter-era, SCVMM lineage) carry the same three-part core without cloud connections, containers, HCI, AI, or fleet services.
- Regional/open-source stacks (oVirt's descendants, PVE, XCP-ng/XO) fit with different substrates and no proprietary machinery.
- Conclusion: the three-part core survives the historical check; the L1 list is the modern market's common dressing, not the definition. The Type predates and outlives any specific substrate, packaging, or era-current capability.

## Uncertainties

- Microsoft evidence is limited to the SCVMM overview page (deeper Learn pages 404). SCVMM's VM-lifecycle details (self-service roles, VM templates depth, placement logic) are asserted only at the overview's level of specificity. If a later pass reaches the deeper pages, the multi-hypervisor and library observations stand but operational detail could be refined.
- Xen Orchestra's day-to-day VM operations (power ops, per-VM config forms) were taken from the intro page's capability list, not from per-task pages; asserted at that strength.
- oVirt's sample documentation is the 4.5-era VM Management Guide; Red Hat Virtualization product documentation (docs.redhat.com) is known-403 from sibling passes, so RHV-specific claims were not made.
- Public-cloud IaaS consoles were not sampled (out of leaf); the CMP/cloud-console boundary observation is reasoning from this sample plus prior CMP/server-management seams, not a fresh product study.
- Desktop-Application-Delivery-facing hypervisor integration (how VDI products consume hypervisors) was not re-sampled; the seam is taken from that pass's ratified note.

## Final Synthesis

**Virtualization Management** is the operator-side application whose world consists of virtual machines and the hypervisor hosts that run them. Its defining core is three jointly-held structures: (1) the **VM as the managed object of record** — a persistent software computer whose virtual hardware and run state are held and operated as configuration at the hypervisor layer; (2) the **virtualization host as the managed resource substrate** — hypervisor hosts registered/configured whose CPU, memory, storage, and network back the VMs; (3) **VM lifecycle authority** — create, configure, power, snapshot, migrate, and remove VMs with placement on hosts, executed through the manager. Everything the modern market adds — central management servers, clusters/pools, templates and image libraries, snapshots and backup machinery, live migration and HA, virtual networking and storage presentation, guest agents, embedded monitoring, RBAC with self-service portals, CLI/API automation, host lifecycle management — is common mature structure. Substrate (hypervisor family), architecture (bundled suite vs standalone manager), multi-hypervisor support, container coexistence, HCI deployment, cloud-connected control planes, and scale posture are variants. The Type's sharpest seams: converged-storage clusters belong to HCI Management; the storage layer itself to Storage Management; OS-level machine management to Server Management Platform; container workloads to Container Management; multi-cloud brokering to Cloud Management Platform; session delivery to Desktop Application Delivery; observe-only tooling to Infrastructure Monitoring. Single-host consoles satisfy the core; the historical check passes for every generation of hypervisor tooling that held a VM record, a host, and lifecycle authority.
