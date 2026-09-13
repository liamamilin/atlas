# Network Management

## Overview

A **Network Management** application is the network team's operating system for its own device estate: it holds the organization's network infrastructure devices — switches, routers, firewalls, wireless access points and controllers — as individually managed records, holds each device's configuration as versioned, comparable, restorable state, and applies changes to devices through itself as the normal course of operation.

The defining core is small:

```text
Network device estate of record
└── Device configuration as managed substance
    └── Write path to devices
```

- **Device estate of record** — every managed device is a persistent, individually identified record with its management-plane reachability (management address, credentials or adopted/registered state), organized into sites, groups, or domains.
- **Configuration as the managed substance** — the system holds device configuration as state that outlives any session: retrieved from devices, authored in the system, or held by a controller; preserved as revisions; comparable across devices and over time; restorable.
- **The write path** — configuration changes are applied to devices through the system — to one device, a group, or the whole estate. The system is an operator of the network, not only an observer or an archivist.

Everything else commonly bundled with these products — device discovery and zero-touch onboarding, firmware upgrades, compliance audits, change-approval workflows, dashboards, integrated health views — is standard capability, not what makes the product a network management application. Remove the write path and what remains is network monitoring or a configuration archive; remove the configuration substance and what remains is an asset inventory; remove the device estate and what remains is a config-file repository with nothing to manage.

## Users & Context

Primary users are the people accountable for keeping an organization's network running:

- **Network engineers / administrators** — onboard devices, author and apply configuration changes, manage firmware, restore configurations after failures.
- **Network operations (NOC) staff** — watch the estate's state, respond to change alerts and device events, execute routine changes across sites.
- **Network architects / lead engineers** — define standard configurations, templates, and policies that others apply.

Secondary users include security teams (when firewall estates are managed here), MSP/MSSP operators managing many client networks, and auditors consuming compliance reports and change history.

The work context is change-with-care: network changes can take down connectivity for the whole organization, so the application's value concentrates on controlled change (staged, reviewed, reversible) and on recovery (getting a device back to a known-good state quickly). Estates range from a handful of devices in a small business to tens of thousands across distributed sites.

## Core Model

### The device estate of record

The center of the world is the **managed device record**. Each record identifies one physical or virtual network device — a switch, router, firewall, wireless access point, wireless controller, or gateway — and carries:

- its identity (name, model, serial, vendor)
- its management-plane reachability: the address the system uses to reach it, and the credentials or the adopted/registered state that authorizes the connection
- its organization: site/location, role, group or administrative domain
- its current management state: reachable/unreachable, config in sync or drifted, firmware version

Devices are organized into **sites** (physical locations), **groups** (roles, models, tiers), or **administrative domains** (in multi-tenant deployments). The estate — not an individual device — is the unit of scale: operations are routinely expressed against groups and sites, not just one box.

### Configuration as the managed substance

The second structure is the **configuration state** the system holds for each device:

- **Retrieved configuration** — configs pulled from devices on a schedule or on demand, stored as versioned backups.
- **Authored configuration** — changes written in the system (direct edits, templates, configlets, or policy objects) that represent what devices should run.
- **Controller-held configuration** — in controller-style products, the system's database is the authoritative config; devices receive it when they adopt or when changes install.

Across all realizations, the held configuration is **versioned** (revisions accumulate), **comparable** (side-by-side diffs between versions of one device, or between devices), and **restorable** (a saved version can be pushed back to a device — including a replacement device after hardware failure). Change history records what changed, when, and by whom.

### The write path

The third structure is what separates management from observation: **changes are applied to devices through the system**. Concretely:

- a configuration edit, template, or policy package is **installed/pushed** to one device, a selected group, or the whole estate
- firmware/software images are **distributed** to devices
- new devices are **provisioned** into service (adopted, modeled, or zero-touch onboarded) with their configuration applied
- a saved configuration is **restored** onto a device — the recovery expression of the same write path

The direction of configuration flow varies by product philosophy (see Variants): multi-vendor config managers emphasize retrieving configs from devices and pushing changes back; controllers emphasize authoring config in the system and installing it to adopted devices. The invariant is that the system holds the configuration and devices receive changes through it.

### What surrounds the core

Standard capabilities that mature products commonly add around this core:

- **Discovery and onboarding** — finding devices on the network and bringing them under management, up to zero-touch provisioning where a factory-fresh device registers itself and receives configuration automatically.
- **Firmware/software management** — tracking versions across the estate, distributing upgrades, often with vulnerability correlation.
- **Compliance** — defining configuration policies (industry standards or house rules), checking device configs against them, reporting violations, and remediating.
- **Change control** — detecting configuration changes that happen outside the system, alerting on them, optionally auto-reverting; approval workflows for planned changes; user-activity audit.
- **Operational visibility** — device health/status dashboards, topology views, and often integrated monitoring surfaces.
- **Access control** — role-based permissions over who can view, edit, approve, and install configuration.

## How It Works

### Bring devices under management

```text
Discover or register devices
→ establish the management connection (credentials / adoption / authorization)
→ devices appear as records in the estate, organized by site/group
→ initial configuration applied (template or policy)
```

In controller-style products, a factory-fresh or newly connected device is **adopted** by the controller and immediately receives the configuration held for it. In config-manager-style products, devices are **added** by address and credentials — sometimes first as offline "model" placeholders before they are physically installed — and their running configuration is retrieved to seed the backup history.

### Change the network

```text
Author the change (edit config / adjust template / modify policy object)
→ (optionally) stage and review / approve
→ install or push to the target device(s) — one, a group, or all
→ system records the change: what, when, who
→ device-side result retrievable and diffable against the intent
```

This is the interaction loop the product exists for. Bulk operations — applying one approved change to hundreds of devices — are a defining convenience of the Type. Changes that happen on the device directly (outside the system) are detected, alerted on, and pulled back into the version history so the system's picture stays authoritative.

### Keep the estate current and compliant

```text
Scheduled jobs run: config backups, compliance checks, firmware scans
→ violations / vulnerabilities / drift surfaced per device
→ remediation: push corrected config, schedule firmware upgrade
→ reports accumulate for audit
```

### Recover

```text
Device fails / change causes an outage
→ select last-known-good configuration
→ restore it to the device (or its replacement)
→ service returns; the incident is visible in change history
```

Recovery is the write path's most valued expression: the difference between minutes and hours of downtime is often whether a known-good configuration can be pushed back immediately.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Device inventory / estate view

The primary surface: the list (or map) of managed devices with site/group organization, management state, config-sync state, firmware version, and reachability.

- typical information: device identity, model, site, group, status, last backup, config drift indicators
- primary actions: add/adopt device, open device detail, select devices for bulk operations, filter/search

### Device detail

One device's world: its configuration (current and revision history), diffs between versions, installed policy/package, firmware, events, and backups.

- primary actions: retrieve config, edit config, compare versions, restore a version, push change, upgrade firmware

### Configuration authoring surfaces

Templates, configlets, policy objects, or direct device-database editors — where changes are written before they are installed. In controller-style products this includes the network's service definitions (networks, WLANs, port profiles) that compile into device configuration.

### Install / push workflow

The guided act of applying staged changes to targets: select the change, select devices/groups, review the diff, execute, observe per-device results.

### Compliance and reports

Policy definitions, per-device violation lists, remediation actions, and audit-ready reports (inventory, changes, compliance status).

### Administration

Users, roles, and permissions; credentials for device access; scheduled jobs; notification settings; in multi-tenant products, the tenant/domain layer.

## Important Rules / Behaviors

### The system's config picture is meant to stay authoritative

Out-of-band changes (made directly on a device) are treated as events to be detected and reconciled — retrieved into the version history, alerted on, and in some products automatically reverted. The estate record is the reference; device-side drift is an exception to surface, not a parallel source of truth.

### Changes are staged, then installed

In controller-style products, edits land in the system's database first and reach devices only when an install/push is executed. This two-step shape (author → install) is what makes review, approval, and scheduling possible.

### Restore targets last-known-good

Backups exist to be restored — after a failed change, a compromised device, or hardware replacement. The versioned config history is the recovery mechanism, not just an archive.

### Write access is the privileged act

Permissions concentrate on who may author, approve, and install changes. Viewing is broad; pushing to devices is the controlled operation. Multi-tenant products scope entire device populations and config objects per tenant/domain.

### Scale is expressed as groups, not one-offs

Bulk application to groups/sites is normal operation. A tool that can only configure one device at a time through a terminal is not this Type — it is the ad-hoc CLI work this Type replaces.

## Variants

- **Single-vendor controller** — the estate is one vendor's devices; configuration is authored in the system (networks, WLANs, policies) and installed to adopted devices; deployment as a cloud service, a controller appliance, or self-hosted software. Common in campus/wireless-centric estates.
- **Multi-vendor configuration manager** — the estate is heterogeneous (routers, switches, firewalls from many vendors); the system retrieves configs, versions them, checks compliance, and pushes changes via vendor-specific templates/scripts. Common as an overlay on estates already running vendor gear.
- **Firewall/security-estate manager** — a controller specialized to security devices, with policy packages as the config medium; often marketed alongside security operations.
- **Deployment shapes** — vendor-hosted cloud management, customer-hosted controller hardware, on-premises server software, and distributed enterprise editions with central aggregation for very large or multi-site estates.
- **Multi-tenant / MSP posture** — administrative domains per client network, with role-scoped access per tenant.
- **Scope variants** — wired+wireless+gateway estates vs config-lifecycle-only overlays; SD-WAN orchestration as a managed overlay on some products.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Network Monitoring | closest sibling; same device estate | monitoring measures availability/performance and alerts (read path); network management applies configuration, firmware, provisioning (write path). Vendors commonly sell them as separate products and bundle them in suites |
| Infrastructure Monitoring | adjacent, read-only | watches hosts, cloud resources, and network devices as one entity class for health; no configuration write path and no config-of-record per device |
| Network Detection & Response / Network Security Platform | adjacent, security-side | detects and responds to threats on the network; firewall device configuration management belongs here, threat detection belongs there |
| Load Balancer Management | adjacent, single-device-class | the distribution point, backend pool, and health-gated rotation are the entire record there; a load balancer is one device class in this estate |
| Server Management Platform | adjacent, different estate | manages servers/endpoints; this Type manages network infrastructure devices |
| Configuration Management (systems) | adjacent, different subject | manages server/application configuration state; network device configuration management is this Type's center |
| Infrastructure Automation Platform | adjacent, different unit of record | centers reusable automation content executed against targets with governance; no per-device configuration of record. They interoperate: automation tools can consume this Type's records, and this Type's scheduled jobs are its built-in automation expression |
| IP Address Management / DNS & DHCP Management | adjacent, different managed object | manages address space and name/address service records; integrated with this Type in suites but a different record base |
| CMDB / IT Asset Management / network source-of-truth | below this Type | holds device records and documentation without operating devices; the record layer this Type builds its estate on |
| Endpoint Management / UEM | adjacent, different estate | manages user devices (laptops/phones), not network infrastructure |
| Telecom / Mobile / Fiber / EV-charging Network Management | same words, different subjects | carrier network elements and OSS processes, the physical fiber plant, or charger fleets — not the enterprise IT device estate |

The boundary that matters most is with **Network Monitoring**: the two Types share the device estate and are frequently bundled, so the seam is the action center — writing changes to devices versus measuring and alerting on them — not the device list, the telemetry, or the vendor.

## Representative Products

- **Ubiquiti UniFi Network** — single-vendor controller; control plane as cloud gateway, dedicated console, vendor hosting, or self-hosted; sites; license-free management
- **Fortinet FortiManager** — single-vendor controller for a firewall-centric estate; device manager, administrative domains, policy packages, install/retrieve/revert operations, zero-touch provisioning
- **SolarWinds Network Configuration Manager** — multi-vendor config lifecycle (backup, diff, rollback, compliance, bulk push, firmware) as a platform module
- **ManageEngine Network Configuration Manager** — multi-vendor configuration and change management; scheduled backups, real-time change detection with auto-rollback, compliance, bulk configlets, distributed enterprise edition

The defining core was checked against the record-layer pole (open-source network source-of-truth tools) and the read-only monitoring pole (network performance monitoring products) to hold the write-path boundary, and against the 2000s device-management lineage (inventory + config archive + image management + scheduled config jobs) to avoid over-fitting to current cloud/AI packaging.

## Sources

Research date: **2026-09-08**

- Ubiquiti — Help Center, "Choosing the Right UniFi Control Plane": https://help.ui.com/hc/en-us/articles/30127033090071-Choosing-the-Right-UniFi-Control-Plane
- Fortinet — FortiManager 7.6 Administration Guide: https://docs.fortinet.com/document/fortimanager/7.6.7/administration-guide
- SolarWinds — Network Configuration Manager (product page & FAQ): https://www.solarwinds.com/network-configuration-manager ; NCM Administrator Guide: https://documentation.solarwinds.com/en/success_center/ncm/content/ncm_administrator_guide.htm
- SolarWinds — Network Performance Monitor (product page & FAQ, seam evidence): https://www.solarwinds.com/network-performance-monitor
- ManageEngine — Network Configuration Manager (product page): https://www.manageengine.com/network-configuration-manager/
- NetBox — official documentation (boundary evidence, record-layer pole): https://docs.netbox.dev/en/stable/

> Sourcing limitation: the cloud-managed enterprise WLAN/campus products (Aruba Central, Cisco Catalyst Center, Juniper Mist documentation) were not reachable from the research environment (access denied / not found). The controller-style pole is therefore evidenced through the reachable controller products; claims specific to those unreachable products are not made. Precise operational details (device-count limits, protocol specifics, exact retention windows) are intentionally not stated; where a product's documentation depth was limited (sign-in-gated help articles), assertions are calibrated accordingly.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
