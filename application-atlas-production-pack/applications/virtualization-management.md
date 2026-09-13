# Virtualization Management

## Overview

A **Virtualization Management** application is the operator's control layer over a virtualization estate: it holds **virtual machines as managed records** — software computers whose virtual hardware and run state are configured and operated at the hypervisor layer — and manages the **hypervisor hosts** whose physical resources back those machines, carrying every VM through its lifecycle: create, configure, power on and off, snapshot, migrate, and remove.

It exists to make server consolidation operable. Instead of individually administered physical servers, workloads run as VMs consolidated onto shared hosts, and this application is where staff run that estate day to day: bring hosts under management, create and place VMs, standardize new machines from templates, move running VMs off hosts for maintenance, and recover them after failures.

The boundary follows the layer it operates: it manages VMs and hypervisors — not the operating systems inside the guests, not the storage arrays behind the hosts, and not a cloud provider's account and resource structure. When the managed subject changes, the Type changes: converged compute-plus-storage clusters belong to Hyperconverged Infrastructure Management, the storage layer itself to Storage Management, and guest OSes as managed machines to Server Management.

## Users & Context

Primary users are **infrastructure and virtualization administrators** — the audience one sampled product states explicitly as "experienced Windows or Linux system administrators who are familiar with virtualization." They work in on-premises datacenters and private-cloud estates, and their work is both project-shaped (deploy a new workload, expand the cluster) and operations-shaped (patch windows, capacity balancing, incident response).

Secondary users are **self-service consumers of VMs**: developers or teams who request and operate assigned VMs without estate-wide authority. Mature products commonly provide a second, reduced surface for exactly this group — a VM portal or self-service scope where a user sees and operates only the machines assigned to them, while administrators retain full estate control.

The working context is a small number of people operating a large estate: one administrator console typically governs many hosts and far more VMs, which is why grouping (clusters, pools), templates, and automation are standard parts of the picture.

## Core Model

### The defining core

```text
Virtualization Host (hypervisor, physical resources)
└── holds & runs
    └── Virtual Machine — managed record
        ├── virtual hardware: vCPU, memory, virtual NICs, virtual disks,
        │   firmware/boot settings
        ├── run state: powered on / off / suspended
        └── placement: which host it runs on
        └── operated through: VM lifecycle (create → configure → run →
            snapshot → migrate → remove)
```

Three structures are jointly required; remove any one and the product is no longer recognizable as virtualization management:

- **The virtual machine as the managed object of record.** A VM is a software computer — one sampled product defines it as "a software computer that, like a physical computer, runs an operating system and applications… consists of a set of specification and configuration files and is backed by the physical resources of a host"; another calls it "a software implementation of a computer." The record exists as managed configuration whether or not the machine is running: its virtual hardware (vCPU count, memory, virtual network interfaces, virtual disks, firmware and boot options) and its power state are held by the manager. Without the VM record, the product is hypervisor installer tooling or a bare inventory list.
- **The virtualization host as the managed resource substrate.** Physical machines running hypervisors are themselves held as managed members of the estate — added, registered, configured, grouped. A VM is always placed on a host, and the host's CPU, memory, storage connections, and network fabric back the VM's virtual hardware. Without hosts under management, VMs have nowhere to run and no resources to draw on.
- **Lifecycle authority over VMs at the hypervisor layer.** The manager does not merely observe: it creates VMs, configures their virtual hardware, powers them on and off, captures snapshots, migrates them between hosts, and removes them — with the placement decision (which host) as part of each operation. Without this authority, the product is an observation console, and observation-only estate tooling belongs to Infrastructure Monitoring.

Note what the core does **not** include: multi-host centralization, clustering, templates, migration, high availability, virtual networking as a first-class estate object, guest agents, containers, cloud connections. All of these are widespread — a single-host hypervisor console with just a VM list and lifecycle actions is still unmistakably this Type — but they are the market's standard dressing, not the definition.

### Standard capabilities of mature products

Mature products commonly add the following. They make the estate practical at scale; none of them is required to recognize the Type.

- **A central management layer above the hosts.** In every sampled product, day-to-day work happens in a management plane that spans more than one host — a central server (deployed as a Windows service, appliance, or a VM inside the estate it manages), a cluster-wide web UI, or an external management server that connects to hypervisors agent-lessly. Alongside it, a per-host console usually still exists for single-host operation.
- **Estate grouping and placement policies.** Hosts are organized into clusters, pools, or data centers; VMs are placed on hosts according to policies (load thresholds, affinity/anti-affinity rules, resource weights).
- **Templates, clones, and an image library.** A prepared VM becomes a template; new VMs are cloned from it with guest-customization applied on first boot. Libraries hold the raw materials — disk images, ISO installation media, portable VM packages — used to create and standardize machines.
- **Snapshots and protection machinery.** Point-in-time captures of a VM's state (configuration, and optionally memory) for restore and branching; commonly integrated backup and replication toward separate repositories.
- **Live migration and high availability.** Running VMs move between hosts (online migration) or stopped VMs move cheaply (offline migration); clustered products restart VMs on surviving hosts when a host fails.
- **Virtual networking and storage presentation.** Virtual switches, port groups, and per-VM network interfaces; storage locations (datastores, storage domains, storage backends) presented so VM disks can be created on them. These exist to serve the VM; the storage estate itself is a different Type's subject.
- **Guest agents and paravirtualized drivers.** In-guest software that enables graceful shutdown from the console, reports IP addresses and resource usage, and improves device performance. The common intent is identical even where one product advertises an explicitly agent-less manager design.
- **Embedded monitoring and events.** Performance charts, status views, and event logs inside the management surface — the observation slice of the same plane that controls.
- **Roles, permissions, and a self-service surface.** Administrator roles for the estate; reduced roles and portals for VM users; assignment of individual VMs to users or teams.
- **Automation surfaces.** A CLI, a REST API, and infrastructure-as-code providers against the same operations the GUI performs — the API is routinely a first-class management surface, not an afterthought.
- **Host lifecycle management.** Patching and upgrading hypervisor hosts, applying standardized host configurations from profiles, adding and removing hosts from clusters.

### One structure, many implementations

The core model is conceptual; products realize it differently, and a reader who has only seen one implementation should be able to recognize the others.

```text
Concept:   VM as managed record
Implementations:  configuration files held by a central server; a numbered
                  config record on an integrated platform; entries in a
                  management server's database

Concept:   Host grouping
Implementations:  clusters and data centers; pools; resource pools

Concept:   Image library
Implementations:  template + content library; library shares (disk images,
                  ISOs, scripts, profiles); built-in template machinery

Concept:   Placement
Implementations:  scheduling policies with load thresholds; placement with
                  resource-weight controls; high-availability managers
```

## How It Works

### Bring the estate under management

```text
Install/enable the hypervisor on each physical host
→ register each host with the management layer (add host / import)
→ group hosts into clusters or pools
→ present storage locations and configure virtual networks
→ the estate is now operable: hosts report status, VMs can be placed
```

### Create and provision a VM

```text
Open the new-VM wizard
→ name the VM, choose its guest OS type
→ create or attach a virtual disk (from storage the estate presents)
→ add a virtual network interface
→ set memory and vCPU
→ choose boot options
→ VM is created, powered off
→ install the guest OS from installation media or network boot,
  or clone from a template instead
→ install guest tools/drivers
```

Cloning from a template is the standard path at scale: a reference VM is prepared once (with its guest identity customized so clones do not collide), converted into a template, and new machines are stamped from it with per-VM customization applied on first boot.

### Operate a running VM

```text
Power on → the manager places the VM on a host per policy
→ open a remote console to see the VM's screen
→ monitor performance and events from the VM's detail page
→ adjust resources (some changes while running, some require power-off)
→ snapshot before risky changes
→ power off or remove when retired
```

### Keep the estate healthy

```text
Live-migrate running VMs off a host before maintenance
→ patch/upgrade the host, return it to the cluster
→ when a host fails, high-availability machinery
   restarts its VMs on surviving hosts
→ balance placement over time against policies
```

### Delegate

```text
Administrator role → full estate surface
→ assign specific VMs to users/teams with reduced roles
→ those users see a self-service portal scoped to their machines
   (power ops, console, limited configuration)
```

The same operations run without the GUI: every sampled product exposes the estate through a CLI and an API (with infrastructure-as-code providers on top), so provisioning and day-2 operations are commonly scripted rather than clicked.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Estate inventory tree

The administrator's home view.

- Purpose: orient across the estate and navigate to any object.
- Typical information: hosts and clusters (or pools), VMs and templates, status of each, counts and alerts.
- Primary actions: navigate to any VM/host/cluster, create new objects, run inventory-wide actions.

### VM detail view

- Purpose: operate one VM.
- Typical information: configuration summary (virtual hardware, placement), power state, performance charts, events, snapshots.
- Primary actions: power on/off/suspend, open console, edit hardware, snapshot/restore, migrate, clone, remove.

### New VM wizard

- Purpose: create a VM.
- Typical information: name, guest OS type, virtual disk creation or attachment, network interface selection, memory/vCPU sizing, boot options.
- Primary actions: create from blank or from template/clone; launch the machine.

### Remote console viewer

- Purpose: see and interact with the VM's screen as if at physical hardware.
- Typical information: the guest's display.
- Primary actions: keyboard/mouse interaction; products commonly hand the session to a locally installed viewer application, and some also provide serial-console access as a text-mode alternative.

### Host and cluster pages

- Purpose: manage the substrate.
- Typical information: host status, hardware summary, running VM count, network and storage attachments, patch/compliance state.
- Primary actions: enter/exit maintenance, add/remove from cluster, apply configuration profiles, migrate VMs away, upgrade.

### Storage and network pages

- Purpose: present the resources VMs consume.
- Typical information: storage locations and their capacity/consumption; virtual switches, port groups, and per-VM interfaces.
- Primary actions: add storage locations, create virtual networks, attach disks and NICs to VMs.

### Template / library pages

- Purpose: standardize VM creation.
- Typical information: templates, disk images, installation media, customization specifications.
- Primary actions: convert VM to template, clone from template, publish/import images.

### Administration surface

- Purpose: govern access.
- Typical information: users, groups, roles, per-object permissions.
- Primary actions: assign roles, assign VMs to users, configure self-service scope.

### Automation surfaces

CLI commands, REST APIs, and infrastructure-as-code providers mirroring the GUI's operations — used for bulk and repeatable work.

## Important Rules / Behaviors

### The record outlives the run state

A VM's configuration persists while it is powered off; powering a VM on places it on a host, and powering it off returns it to a stopped record. Configuration changes split into those the manager can apply to a running machine (hot-add of disks, NICs, memory, or vCPUs where supported) and those that require power-off.

### Placement is decided by the manager under policy

The manager chooses the host for each VM start or migration. Placement can legitimately refuse: one sampled product documents that a VM will not start on a host its scheduling policy considers overloaded, and another prevents starting a VM with more virtual cores than the host has physical cores. Scheduling policies (load thresholds, affinity rules, resource weights) are configurable.

### Live migration carries compatibility constraints

Moving a running VM between hosts requires the destination to present the guest a compatible virtual environment. Managers let operators control this at configuration time — generic virtual CPU types and pinned virtual hardware versions exist precisely so a VM can move between dissimilar hosts — and locally bound resources (such as passed-through physical devices) block live migration.

### Snapshots are point-in-time and branchable

A snapshot captures the VM's configuration (and optionally its memory) at a moment; the VM can be restored to it, and some products allow a new VM to be created from a snapshot. Snapshot chains are managed objects with their own lifecycle (create, restore, delete).

### Duplicated guests need identity customization

Cloning and templating duplicate a machine wholesale, so products provide first-run customization (host-name, network identity, and OS-specific preparation) to avoid colliding guest identities. Preparing a clean reference VM before converting it to a template is a documented, standard step.

### Permissions scope the surface

The self-service boundary is structural: VM-user roles see only machines assigned to them, and assignment is done by administrators per VM. Estate-wide configuration (hosts, clusters, storage, networks) remains with administrator roles.

### Conflicting operations are serialized

Products guard against concurrent conflicting changes to the same object — in one sampled product, a VM under migration, backup, or snapshot carries an explicit configuration lock until the task completes.

## Variants

Common forms the Type takes in the market:

- **Bundled hypervisor suite** — hypervisor and management layer shipped as one product family; the management server is the estate's control plane.
- **Standalone manager over existing hypervisors** — the manager is a separate deployment (suite component, external server, or agent-less appliance) that connects to hosts running a hypervisor it does not itself ship.
- **Integrated open-source platform** — hypervisor and web-based management installed together on every node; the cluster forms when nodes are joined.
- **Multi-hypervisor manager** — one manager controlling hosts of different hypervisor families.
- **Single-host console** — the per-host client for estates of one; the minimal form of the Type.
- **Converged (HCI) deployment** — the same consoles deployed over clusters whose storage comes from the hosts themselves; the converged subject belongs to Hyperconverged Infrastructure Management.
- **Cloud-connected control plane** — estate managers onboarded into a cloud control plane for cross-portal governance; a hybrid-era variant.
- **Workload-mixed platforms** — some platforms manage light-weight container workloads alongside VMs; the defining managed unit remains the VM.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Hyperconverged Infrastructure Management | closest sibling | its subject is a converged cluster whose compute and storage come from the same nodes, operated as one stack; point the same hosts at external storage and the same console continues as virtualization management — the managed subject decides |
| Storage Management | adjacent | manages the storage layer itself (drives, pools, volumes, LUNs, shares, buckets); a hypervisor console's storage view touches those objects only as places to put VM disks — its center of gravity is the VM |
| Server Management Platform | layer sibling | manages machines at the OS layer (patches through the OS's package machinery, remote execution, configuration inside the guest); a VM enters there as a machine record and here as a hypervisor-level object (virtual hardware, power state, snapshots, migration) — the same VM can be the subject of both |
| Container Management | adjacent | managed unit is containerized workloads instantiated from images through a container runtime; here the unit is the hypervisor-operated VM; convergence exists where one platform carries both |
| Cloud Management Platform | adjacent | brokers multi-cloud estates — account, resource, and cost governance across providers; virtualization management performs hypervisor- and host-specific operations directly on an operator-run estate |
| Desktop Application Delivery | underlying layer | delivers remote application/desktop sessions to end users from centrally hosted resources; it consumes hypervisors (supported hypervisors appear there as connections), while this Type operates them |
| Infrastructure Monitoring | observation sibling | watches estate health and alerts; it has no lifecycle authority; the management plane embeds monitoring views but is defined by control |
| Backup Management | protection layer | holds recovery points and runs protection jobs; virtualization products commonly integrate backup machinery, but recovery-point custody is the sibling Type's subject |
| Capacity Management | planning sibling | plans supply vs demand over time with forecasting; virtualization management executes configuration and lifecycle now |

The two seams most worth internalizing: **subject** separates this Type from HCI and Storage Management (VMs-over-arbitrary-infrastructure vs converged cluster vs storage layer), and **layer** separates it from Server Management (hypervisor-level object vs OS-level machine).

## Representative Products

- VMware vSphere (ESX + vCenter)
- Microsoft System Center Virtual Machine Manager
- Proxmox VE
- oVirt
- Xen Orchestra (over XCP-ng)

The sample deliberately spans the bundled proprietary suite, the suite-resident manager, the integrated open-source platform, the engine-over-hosts architecture, and the agent-less external manager; the single-host console form was checked against a major product's dedicated single-host management documentation.

## Sources

Research date: **2026-09-09**

- VMware vSphere 9.1 documentation (Broadcom TechDocs) — https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1.html (documentation map; Virtual Machine Administration guide)
- Microsoft Learn — "What is Virtual Machine Manager?" (System Center VMM 2025) — https://learn.microsoft.com/en-us/system-center/vmm/overview?view=sc-vmm-2025
- Proxmox VE wiki — Main Page and QEMU/KVM Virtual Machines chapter — https://pve.proxmox.com/wiki/Main_Page , https://pve.proxmox.com/wiki/QEMU/KVM_Virtual_Machines
- oVirt documentation — index and Virtual Machine Management Guide — https://ovirt.org/documentation/ , https://ovirt.org/documentation/virtual_machine_management_guide/index.html
- Xen Orchestra documentation — introduction — https://xen-orchestra.com/docs/

> Sourcing limitation: deeper Microsoft Learn pages for SCVMM operational detail returned errors and were not reachable; Microsoft claims in this document are held to the overview page's stated capabilities. Proxmox evidence rests on two wiki pages of the official reference documentation. Precise numeric limits and product defaults are stated only where fetched pages state them, and product-specific rules are marked as such in the text.
