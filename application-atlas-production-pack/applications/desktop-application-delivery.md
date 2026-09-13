# Desktop & Application Delivery

## Overview

A **Desktop & Application Delivery** product is an IT-operated platform that runs an organization's applications and desktops on centralized host computers — servers, virtual machines, or cloud hosts — and delivers them to users as live remote sessions, instead of installing the software on each user's device.

The user sits at any endpoint (managed PC, BYOD laptop, thin client, browser) and works inside a session: either a full remote desktop or a window containing a single remote application. The software executes, and the data stays, on the host side; only the interface travels to the endpoint.

The defining core is small:

```text
Centrally hosted execution
└── Published resources (applications and/or desktops, named and standing)
    └── Per-user / per-group entitlement
        └── Remote interactive session (full desktop or seamless application window)
            └── A managed fleet of hosts behind the resources
```

Remove centralized execution and the product becomes a software-deployment tool. Remove published resources and entitlement and it becomes ad-hoc remote access. Remove the session and it becomes a file-distribution mechanism. Remove the managed fleet and it becomes a one-to-one screen-sharing utility. What remains — the four structures above — is the Type.

Everything else commonly associated with the category — image catalogs, autoscale, printing and USB redirection, profile containers, gateways, HTML5 clients — is widespread in mature products but is not what makes the product a member of this Type. The definition also deliberately does not depend on the cloud generation: server-based computing products of the terminal-server era, which published applications from central servers to thin clients, satisfy the same core.

## Users & Context

**Primary operators — IT infrastructure / desktop teams.** They define the published resources, prepare the images and hosts those resources run on, decide which users and groups receive which resources, set session policies, and watch the environment through monitoring consoles. Their goals are concrete: give a new worker access in minutes rather than a procurement cycle, keep corporate data off unmanaged devices, run legacy or line-of-business applications that cannot be installed everywhere, and serve contractors, outsourcers, or entire subsidiaries without touching their hardware.

**Primary consumers — end employees and other users.** They sign in, see the resources they are entitled to, and launch them. From their point of view the experience is intended to be indistinguishable from a locally installed machine: full desktop, familiar applications, their own files and printers.

**Typical contexts:**

- remote and hybrid work from unmanaged or cross-platform devices
- secure containment: data must never land on the endpoint
- contractors, partners, seasonal or offshore staff who need app access without device management
- legacy or specialized line-of-business applications that cannot be redeployed to modern endpoints
- high-graphics or compute-heavy workloads served from GPU-equipped hosts
- education labs, call centers, and other shared-shift environments
- service providers delivering hosted applications and desktops to many customer tenants

## Core Model

### The defining structures

**Centralized host compute.** The world of this Type is anchored on a fleet of hosts — shared multi-user servers, dedicated virtual desktop machines, or remotely served physical PCs — that run the actual applications and desktops. The platform provisions this fleet, keeps it current, and decides which host serves which user. The endpoint is deliberately reduced to a display and input device for the session.

**Published resources.** Applications and desktops are surfaced to users as named deliverables — a published application ("the ERP client"), a published desktop ("the standard finance desktop"). Publishing is the act of making something on a host visible and launchable as a standing resource with a name, an icon, and configuration. A resource is catalog configuration, not a running thing: it exists before any user connects and persists across sessions. Products may publish individual applications, full desktops, or both; the resource mix is a variant, not a boundary — every product in the research sample supports application publishing, and desktop publishing accompanies it in all of them.

**Entitlement.** Each published resource is granted to specific users or groups. Entitlement decides what appears in a user's launcher and what the broker will connect them to; it is standing configuration managed by administrators, not an ad-hoc invitation. Users are typically assigned to multiple resources, and groups are the normal unit of assignment, usually sourced from the organization's directory.

**Remote interactive session.** When an entitled user launches a resource, the platform establishes a session: a live, interactive runtime on a host, presented through a display protocol to a client application or browser. A session is either a complete desktop or a seamless application window that appears local while running remotely. Sessions have a lifecycle: a session is active while the user is connected, becomes disconnected when the user closes the client without signing out, and ends when the user signs out. Reconnecting after a disconnection typically returns the user to the same session, with open work intact.

**The managed fleet.** Behind the resources stands a maintained population of hosts, provisioned from managed images or configurations that administrators prepare and update. Two fleet postures recur across the Type: hosts dedicated to a single user (persistent/personal — the user's environment, files, and installed changes persist between sessions) and shared or ephemeral hosts (non-persistent/pooled — sessions land on any available host, and user state is preserved through separate profile machinery rather than the machine itself).

### What mature products add

These capabilities are standard in the current market; they make delivery practical but do not define the Type:

- **Brokering and load balancing** — the platform authenticates the user, checks entitlements, and places the session on a suitable host, balancing load across the fleet.
- **Image-based provisioning** — fleets are created from golden images (base OS + applications + configuration); updating the fleet means updating the image and redeploying hosts, rather than patching each machine.
- **Power management and autoscale** — hosts are started, deallocated, or hibernated on schedules and load thresholds to control cost.
- **Session services** — the plumbing that makes a remote session usable as a local one: printing (often through universal print drivers), client drive and folder mapping, USB and peripheral redirection, clipboard transfer, multi-monitor support, webcam, audio and video optimization.
- **Session policy engine** — administrators govern session behavior (clipboard use, drive redirection, printing, session timeouts) per user, group, or context.
- **Profile management** — for non-persistent fleets, user state (settings, files, sometimes installed pieces) is carried in profile containers that follow the user between hosts.
- **Application packaging and layering** — applications are packaged and attached to hosts on demand (containerized app packages, layered disks), keeping base images small and letting one image serve many resource mixes.
- **Administration and monitoring** — a central console for publishing, fleet management, and policy, plus operational views over sessions, machines, usage, and cost, with delegated administration for large teams.
- **Identity and secure access** — integration with the organization's directory or identity provider, single sign-on, multi-factor authentication, and a gateway component that lets external users reach sessions without exposing hosts directly.
- **Client family** — native client applications for each desktop and mobile OS plus a browser-based client, so the same resources are reachable from any device.

### One structure, many implementations

The core model is conceptual; products realize it differently:

```text
Concept:   Published resource
Realized as: published application, published desktop, streamed application, virtual desktop

Concept:   Host fleet
Realized as: machine catalogs on hypervisors, host pools of cloud VMs,
             managed session hosts, remote physical PCs

Concept:   Entitlement
Realized as: delivery/application groups, user assignment to app groups,
             access-control rules in the admin console

Concept:   Session delivery
Realized as: remote display protocols of various kinds, delivered through
             installed client apps or plain web browsers
```

A reader who has only seen one implementation — for example, a cloud service that streams individual applications — should still be able to recognize an on-premises product that serves full desktops from a datacenter as the same Type.

## How It Works

### Build the platform (administrator)

```text
Install or subscribe to the delivery platform
→ connect it to compute (hypervisors, cloud subscriptions, or provider-managed hosts)
→ connect it to the organization's identity/directory
→ prepare a host image (OS + core applications + agent)
→ provision a fleet of session hosts from the image
```

The platform's agent on each host registers the machine with the management layer, which tracks capacity, registration state, and power.

### Publish resources (administrator)

```text
Choose what to publish (an application from the hosts, or a full desktop)
→ name and configure the resource (icon, app path, settings)
→ grant it to users/groups
→ surface it to a user-facing catalog/workspace
```

The resource now exists as standing configuration. Administrators iterate on this continuously: new applications get published, entitlements change with org structure, new images roll out to new host fleets.

### Connect and work (end user)

```text
Open the client app or web portal and sign in
→ see the resources entitled to you
→ launch one (application or desktop)
→ broker validates entitlement, selects a host, establishes the session
→ work inside the session; host-side execution, local-feeling interface
→ disconnect (session persists) or sign out (session ends)
→ reconnect later and resume where you left off
```

The interaction loop for the user is exactly this: sign in, launch, work, return. The heavy machinery — placement, load balancing, profile attachment, peripheral mapping — happens between "launch" and "window appears".

### Keep the fleet current (administrator)

```text
Update the golden image (patch, new app versions)
→ roll out new hosts from the image into the fleet
→ retire old hosts (draining sessions first)
```

For pooled fleets this image-redeployment cycle is the normal update path; for persistent machines, conventional in-place updating is common. This is the operational signature of the Type: the fleet is managed as a population generated from images, not as a set of individually groomed PCs.

### Scale and control cost

Hosts are powered on and off against schedules and load thresholds; capacity grows and shrinks with demand. Administrators monitor sessions, host health, usage patterns, and cost from the console, and intervene when sessions misbehave or capacity runs short.

### Defining vs standard vs optional

**Defining core** — without these, not this Type:

- centrally hosted execution of the delivered software
- published, named resources (applications and/or desktops)
- per-user/per-group entitlement to those resources
- remote interactive session as the delivery vehicle
- a managed fleet of hosts behind the resources

**Standard capabilities** — present in essentially all mature products:

- brokering and load balancing; session reconnection
- image-based fleet provisioning; persistent and non-persistent postures
- native + web client family
- session services: printing, drive mapping, peripheral redirection, multimedia
- session policy engine; profile management for non-persistent fleets
- admin console with monitoring; delegated administration
- directory/IdP integration, SSO/MFA, secure external access gateway
- application packaging/layering; power management/autoscale

**Optional / variant** — depends on segment, era, and posture:

- resource mix emphasis (apps-only, desktops-only, remote PCs)
- deployment substrate (on-prem, hybrid, provider-managed cloud)
- Linux or Windows hosts; single- or multi-user session hosts
- GPU/graphics workload support, session recording, multi-tenancy for service providers
- AI-era extensions (for example, granting automated agents access to hosted applications)

## Interfaces

### Administrator console

The operational center of the product.

- Purpose: define and run the delivery environment.
- Typical information: published resources and their entitlements; host fleets, host health, registration and power state; images; sessions; capacity and usage; alerts.
- Primary actions: publish/unpublish resources, assign and revoke entitlements, provision and image fleets, set policies, power-manage hosts, inspect and terminate sessions, delegate roles.

### User portal / client launcher

The user's entry surface.

- Purpose: show the user what they are entitled to and launch it.
- Typical information: resource icons and names grouped in a catalog or workspace, favorites, recent activity.
- Primary actions: launch an application or desktop, search, manage settings and devices.

### The session

The surface the user actually works in.

- Full-desktop mode: a complete remote desktop presented fullscreen or in a window.
- Application (seamless) mode: individual application windows that appear on the local desktop alongside local windows, with local taskbar integration where the client supports it.
- Connection controls: connection bar, full-screen toggle, multi-monitor selection, peripheral choices.

### Monitoring / analytics views

Operational dashboards over the environment.

- Purpose: keep the service healthy and explain what happened.
- Typical information: active/disconnected sessions per host, logon durations, resource usage, failures, cost drivers.
- Primary actions: filter by user/host/resource, drill into a session, run diagnostics, alert on thresholds.

## Important Rules / Behaviors

### Execution stays on the host

The system is architected so that application binaries and data remain on hosts. What the endpoint receives is presentation traffic. This is both the security promise ("data never stored on users' devices") and the operational premise (one image, many users).

### Entitlement gates everything

A user sees only what they are entitled to, and the broker will only place sessions onto hosts backing entitled resources. Entitlement changes take effect as configuration; there is no user-side installation step.

### Sessions persist across disconnection

Closing the client window does not end the session; it becomes disconnected and is typically resumable, preserving open applications and state. Signing out ends the session. Exact timeout and reconnection behavior is policy-configured.

### The two fleet postures behave differently

On persistent (personal) machines, the user's environment is that machine: files, settings, and often installed software persist locally on the host. On pooled hosts, machines are interchangeable and ephemeral; anything the user must keep is carried by profile machinery, and machine-level changes are discarded or re-imaged. Administrators choose posture per population, and it determines how updates and user state work.

### Publishing is decoupled from hosts

Resources reference what is installed on host images; the same fleet can back many published resources, and the same resource can be served by any capable host in its fleet. This decoupling — publish against a fleet, not a machine — is what lets the platform balance load and reassign hosts freely in pooled postures.

### Policy overrides the defaults

Session behavior (clipboard, redirection, printing, timeouts) is centrally governed; the administrator's policy, not the user's client, decides what crosses the session boundary. Restrictive postures (containment deployments) tighten these channels deliberately.

## Variants

- **Application-centric delivery** — published applications only (usually from shared multi-user hosts); the user never sees a remote desktop. Suited to task workers and contractors needing a few apps.
- **Desktop-centric delivery (VDI)** — full virtual desktops, personal or pooled; suited to complete-worker populations.
- **Remote PC mode** — the delivery framework remotes users into their existing physical office PCs; the fleet concept extends to physical machines.
- **On-premises full-stack** — the organization runs brokers, gateways, and hosts in its own datacenter on hypervisors of its choice.
- **Cloud control-plane** — hosts run in a public cloud while the provider operates the brokering and access infrastructure; administrators manage images, fleets, and entitlements only.
- **Fully managed desktops-as-a-service** — the provider operates everything; the customer defines bundles/images and assigns users; billing is consumption-shaped.
- **Service-provider / multi-tenant** — one platform instance hosts many customer tenants with isolated administration.
- **High-graphics workloads** — GPU-backed hosts for design, engineering, or specialized visualization.
- **Security-containment posture** — the deployment exists primarily so nothing sensitive ever reaches endpoints (high-risk data, regulated work, third parties).

A variant remains a variant while the published-resource + session + fleet model still describes it. When the surface stops being a delivered desktop or application session — for example, when the product's managed object becomes the endpoint device itself — it has crossed into a different Type.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Application Deployment Management | closest operational neighbor | its unit of work is a package installed onto a managed endpoint; here execution never lands on the endpoint — software is delivered as remote sessions |
| Endpoint Management / UEM | complementary neighbor | manages devices (enrollment, configuration, compliance, wipe); this Type manages resources, hosts, and sessions; vendors commonly sell both side by side |
| Patch Management | adjacent | keeps installed software current; this Type keeps fleets current via image redeployment as an operational pattern, not as its defining purpose |
| Remote Monitoring & Management / IT Service Management | adjacent | operate and support IT estates broadly; session delivery is one specific service this Type provides |
| Remote access / remote support tools | overlapping seam | deliver point-to-point sessions into one specific existing machine; this Type is a standing, cataloged, entitled service across a managed fleet (remote-PC remoting exists inside this Type as a mode, under the same published-resource and entitlement machinery) |
| Virtualization Management | underlying layer | runs hypervisors and virtual machines; this Type consumes that compute to serve users — supported hypervisors appear here as connections, not as the product's subject |
| Cloud IDE / dev workspace platforms | audience neighbor | same delivery mechanics (central compute, streamed environment) with a developer-audience, code-centric object model |
| VPN / ZTNA | different layer | network-layer reachability; the gateway inside a delivery product carries sessions, it does not open the network |
| SaaS / web applications | different delivery model | run in the provider's service and are consumed directly; no organizational host fleet, no published desktop/application sessions |

The boundary worth internalizing is against **Application Deployment Management**: both are about "getting software to users", and both are operated by the same IT teams. The structural test is where execution happens. If the software is installed and executed on the endpoint, it is deployment; if it executes centrally and arrives as a session, it is this Type.

## Representative Products

- Citrix Virtual Apps and Desktops
- Omnissa Horizon
- Microsoft Azure Virtual Desktop
- Parallels RAS
- Amazon WorkSpaces / WorkSpaces Applications

The defining core was checked against the terminal-server generation of server-based computing products to avoid over-fitting the definition to the current cloud generation; the definition holds without hypervisors, pools, web clients, or provider-managed control planes.

## Sources

Research date: **2026-09-08**

- Citrix — Virtual Apps and Desktops product documentation (docs structure and technical overview): https://docs.citrix.com/en-us/citrix-virtual-apps-desktops , https://docs.citrix.com/en-us/citrix-virtual-apps-desktops/technical-overview
- Microsoft Learn — Azure Virtual Desktop overview and terminology (host pools, application groups, workspaces, session states): https://learn.microsoft.com/en-us/azure/virtual-desktop/overview , https://learn.microsoft.com/en-us/azure/virtual-desktop/terminology
- Omnissa — Horizon 8 product overview (component descriptions, deployment options): https://www.omnissa.com/products/horizon/
- Parallels — Parallels RAS product overview (delivery model, publishing, session services, security): https://www.parallels.com/products/ras/
- AWS — Amazon WorkSpaces and WorkSpaces Applications documentation: https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces.html , https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html

> Sourcing limitations: Horizon and Parallels evidence comes from official product pages rather than deep admin documentation (their documentation portals were not reachable from the research environment on 2026-09-08); claims about those products are calibrated accordingly and lean on cross-product corroboration. One Citrix page (delivery methods) did not render its body text; Citrix observations rest on the product's official documentation structure. No precise numeric limits, defaults, or protocol parameters are asserted in this document.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical fit-check are recorded in the paired Research Notes.
