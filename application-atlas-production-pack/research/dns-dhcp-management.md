# Research Notes — DNS & DHCP Management

Research date: 2026-09-08
Slug: `dns-dhcp-management` (Directory §14 IT, Cloud & Infrastructure)

## Research Goal

Understand what a "DNS & DHCP Management" application actually is as an Application Type: what objects it manages, what "management" means as distinct from running a DNS or DHCP server, how the two services interlock, who operates it, and where its boundaries lie against IPAM, network management, and DNS server/hosting surfaces.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: this is the enterprise "DDI" discipline (DNS + DHCP + IPAM) minus the pure IPAM planning layer — the operator layer that centrally configures and operates the two foundational network services instead of configuring each server separately.
- Likely confusion surfaces: IPAM (sibling leaf), Network Management / Network Monitoring (devices, health), cloud provider DNS consoles (single-provider zones), web-hosting control panels (zones as hosting artifacts), domain registrars (registration, not resolution operation).
- Key unknown: is the DHCP↔DNS linkage (lease → name record) definitional, or merely the structural reason the two are managed together? Is "multiple servers" part of the definition?

## Research Questions

1. What are the core managed objects on the DNS side? (zones, record types, views, forwarding, DNSSEC, ACLs)
2. What are the core managed objects on the DHCP side? (scopes/subnets, pools, options, reservations, leases, failover)
3. What makes it "management" rather than "server software"? Is there a config→deploy→operate loop?
4. How do DNS and DHCP interlock? (dynamic DNS, A/PTR updates from leases, shared address model)
5. What governance exists? (RBAC, approval workflows, audit/change history, server authorization)
6. What interfaces? (web console organization, APIs, automation integrations)
7. How is the serving infrastructure modeled? (own appliances vs overlay over third-party servers vs OS roles vs single box)
8. Boundary vs IPAM: what exactly does the management application do that IPAM doesn't?
9. Historical check: do pre-cloud, pre-API DDI products fit the same core?

## Representative Products

| Product | Philosophy / pole | Why selected |
|---|---|---|
| Infoblox Universal DDI (NIOS / NIOS-X / Portal) | Cloud-managed enterprise DDI suite; manages its own serving infrastructure AND third-party/cloud DNS | Market-leading enterprise DDI; richest structural evidence |
| Micetro (Men&Mice product line, now under BlueCat) | Backend-agnostic overlay DDI over existing heterogeneous servers | Opposite philosophy: management layer without replacing servers |
| Microsoft Windows Server DNS / DHCP / IPAM | Platform-native: services as OS roles + central IPAM management feature | The non-suite, bundled-in-OS pole; historical/platform-native check |
| Technitium DNS Server | Open-source, self-hosted DNS (+DHCP) with built-in web console; optional clustering | Thin/SMB/self-hosted pole; management surface embedded in serving product |

Rejected from sample due to access failures (recorded, not silently dropped): BlueCat Address Manager (docs.bluecat.net — 2 transport errors), EfficientIP SOLIDserver (doc.efficientip.com — 2 transport errors). Both are known DDI vendors; their absence weakens enterprise-suite breadth evidence and is compensated by lowering assertion strength, not by memory-filling.

## Sources

Evidence layer A (directly observed, fetched 2026-09-08):

1. Infoblox Documentation Portal — https://docs.infoblox.com/
2. Infoblox Universal DDI Management — https://docs.infoblox.com/space/BloxOneDDI/186614365/Infoblox+Universal+DDI+Management
3. Infoblox Universal DDI Overview — https://infoblox-docs.atlassian.net/wiki/spaces/BloxOneDDI/pages/684523986
4. Infoblox Universal DDI — DNS — https://infoblox-docs.atlassian.net/wiki/spaces/BloxOneDDI/pages/186810605/DNS
5. Infoblox Universal DDI — DHCP — https://infoblox-docs.atlassian.net/wiki/spaces/BloxOneDDI/pages/186810534/DHCP
6. Micetro 25.1 documentation (root) — https://docs.menandmice.com/
7. Micetro User Guide — DNS — https://docs.menandmice.com/en/latest/guides/user-manual/dns/
8. Micetro User Guide — Workflow — https://docs.menandmice.com/en/latest/guides/user-manual/webapp_workflows/
9. Microsoft Learn — Domain Name System (DNS) in Windows and Windows Server — https://learn.microsoft.com/en-us/windows-server/networking/dns/dns-top
10. Microsoft Learn — What is DHCP Server in Windows Server — https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-top
11. Microsoft Learn — IP Address Management (IPAM) — https://learn.microsoft.com/en-us/windows-server/networking/technologies/ipam/ipam-top
12. Microsoft Learn — What's new in Windows Server 2016 (IPAM section) — https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-in-windows-server-2016
13. Technitium DNS Server — https://technitium.com/dns/

Access limitations: BlueCat Address Manager and EfficientIP SOLIDserver documentation unreachable (transport errors). Infoblox doc content partially fetched from the Atlassian wiki mirror (anonymous access; some child pages not fetched). Consequence: enterprise-suite commonality claims rest on 2 enterprise products (Infoblox, Micetro) plus platform-native and open-source poles; assertions calibrated accordingly; no precise numeric limits from vendor docs are reproduced in the final document.

## Product Observations

### Infoblox Universal DDI (NIOS / NIOS-X / Infoblox Portal) — layer A

- Positioned as SaaS "Universal DDI Management … simplif[ying] DDI management (DNS, DHCP, and IP address management) across on-premises environments and public clouds … unified management, in-depth visibility and insights, and infrastructure-free deployment."
- "Consolidates configuration and control of several DDI services, including Microsoft DNS, BIND, NIOS Grid deployments, NIOS-X Physical and Virtual Servers …, Amazon Route 53, Azure DNS and Google Cloud DNS." → the management layer spans heterogeneous serving infrastructure, including competitors' servers and public-cloud DNS zones.
- Universal DDI Overview: NIOS (on-prem), Infoblox Platform (hybrid), Third-Party Cloud Providers — "management of objects from AWS, Azure, and GCP with two-way synchronization." Single pane of glass = Infoblox Portal; portal "enables seamless management of all DDI objects."
- DNS area tabs (portal): Zones, DNS Config Profiles, DNS Server Groups, DNS Servers, Access Control Lists, Global DNS Configuration. Supported config: Primary authoritative DNS, Secondary authoritative DNS, DNS server groups, ACL templates, recursion, forwarding. Additional modules: DNS Views, Resource Records, TSIG Keys, GSS-TSIG, Third Party DNS Providers, DNS Traffic Control, Zone Federation, Cloud Forwarders, Response Policy Zones.
- DHCP area tasks (portal): Global DHCP Properties, DHCP Config Profiles, Option Spaces, Option Groups, IPv4 Filters, HA Groups, NIOS-X Server configuration; scope resizing; DHCPv4 fingerprints. DHCPv4/v6 (DORA, stateful/stateless) protocol descriptions included in admin docs.
- Deployment loop (direct evidence): "NIOS-X allows DNS configuration updates to be applied sequentially on NIOS-X servers … Configuration updates are performed one NIOS-X server at a time, progressing to the next server only after the configuration on the current server has been updated successfully." A documentation table correlates zone/record counts with "Service Reload Time" and "Expected DNS Server Update Interval … the time it takes for a DNS configuration to be sent from the Infoblox Portal to the NIOS-X Server." → configuration is held centrally and pushed to serving servers; propagation cost/status is user-visible.
- Other structure: Recycle Bin, Importing and Exporting Data, Viewing Reports, API Guide (WAPI), Ansible Collections, Terraform Provider, VMware Aria provider, Anycast Addressing, Microsoft Integration, IPAM Federation. (Layer A observations of module existence; details not fetched.)

### Micetro (Men&Mice / BlueCat) — layer A

- Self-description: "a backend-agnostic DDI orchestration software for complex enterprise network environments. Deployed in any on-premises, hybrid, or multicloud network environment, Micetro acts as a non-disruptive overlay that unifies server management under a single GUI and API. Micetro is a modular, software-defined DDI solution … accessed through a unified user interface and API." → overlay philosophy: it manages whatever DNS/DHCP servers the customer already runs.
- Documentation structure: User Guide (Using Micetro, DNS, IPAM, Reports, Workflow, Folder Management, Object Change History, Automation); Admin Guide (Access Management, Service Management, Failover Management, SNMP Profiles, xDNS Redundancy, Event Hooks, Address Space Management, Custom Properties, Object History and Logs, SSO, Integrating and Managing Appliances).
- DNS page: granular access control with built-in roles (DNS Administrators, DNS Viewers) and permissions ("Access DNS module", "List (or view) DNS server", "List (or view) zone"); zone-specific access definable per zone. Sub-pages: DNS Zones, DNS Resource Records, Importing DNS Records. → zones→records hierarchy with per-object RBAC.
- Workflow module (change governance, directly observed): users with limited access submit "change requests" for creating/modifying/deleting DNS records instead of applying immediately; Requesters and Approvers roles; approvers "only able to approve requests that involve DNS Zones in which they have access to edit records"; on approval "the DNS change is made and the DNS zone is updated automatically with the new data, either immediately or at a time specified in the request"; request states Pending / Approved / Rejected / Failed / Applied (closed states Scheduled, Fulfilled); "Failed — requests that encountered an error while being applied to the DNS servers"; scheduled changes; rejection records a reason in history. Authorized users can also use requests "in order to make scheduled changes."
- Cross-service coupling (direct evidence): "After a DNS request for a DNS change has been created, the corresponding IP address will be set in to a pending state and will not be available, for example when requesting the next Free IP address in the subnet." → a DNS record change interacts with address availability in the IPAM/address-space layer.
- Service Management, Failover Management, appliance integration, Address Space Management documented as admin areas (module existence observed; details not fetched).

### Microsoft Windows Server DNS / DHCP / IPAM — layer A

- DNS: "a server role that can be installed using Server Manager or PowerShell"; stores/replicates DNS zones; AD-integrated or standalone (public or private zones). Features: AD integration (secure updates + replication), dynamic updates ("Automatic registration and updates of client DNS records"), DNSSEC, forwarding/conditional forwarding, caching, monitoring/logging, DNS policies, anycast.
- DHCP: server role that "automates the assignment and management of IP addresses"; server database holds "valid TCP/IP configuration parameters … valid IP addresses, maintained in a pool … as well as excluded addresses … Reserved IP addresses associated with particular DHCP clients … The lease duration." Options include Router, DNS Servers, DNS Domain Name. Features: DHCP policies (per client characteristics e.g. MAC/vendor class), audit logging ("track DHCP server activity, including lease assignments and renewals"), management via "Windows PowerShell, the DHCP console, or the Windows Admin Center," DHCP server authorization in Active Directory ("preventing unauthorized servers from providing IP addresses"), **"DHCP server integration with DNS. Dynamic DNS automatically update DNS records when DHCP leases are assigned or renewed"**, IPv4+IPv6, **failover: "two DHCP servers to share a single scope, providing redundancy and load balancing"**, integration with IPAM.
- IPAM: "an integrated suite of tools to enable end-to-end planning, deploying, managing and monitoring of your IP address infrastructure … IPAM automatically discovers IP address infrastructure servers and Domain Name System (DNS) servers on your network and enables you to manage them from a central interface."
- IPAM DDI capabilities (What's New, WS2016 section): "Integrated DNS, DHCP, and IP address (DDI) management. You can now view all DNS resource records associated with an IP address in the IP Address Inventory. You can also automatically keep pointer (PTR) records of IP addresses and manage IP address lifecycles for both DNS and DHCP operations." DNS service management: resource-record collection, record property/operation configuration, "DNS zone management for both domain-joined Active Directory-integrated and file-backed DNS servers" (Primary/Secondary/Stub), conditional forwarders, RBAC for records and zones. Multiple AD forest support; IP utilization data with purge; free-subnet/free-range finders; RBAC access scopes in PowerShell.
- Structural note: each service also has its own per-server console; the *management application* (IPAM) adds discovery, central management, DDI coupling, RBAC, and reporting across many servers. → clear evidence that "management layer" is separable from "server role" in the platform-native pole.

### Technitium DNS Server — layer A (product page level)

- "Open source authoritative as well as recursive DNS server … provides a user friendly web console accessible using any modern web browser." Runs on Windows/Linux/macOS/Raspberry Pi, Docker.
- "Includes built-in Clustering feature to allow managing two or more DNS Server instances from a single admin web console." → even the thin pole has the console-over-instances structure when scaled.
- Zones: Primary, Secondary, Stub, Conditional Forwarder zones; catalog zones; DNSSEC signed zones (NSEC/NSEC3); zone transfer AXFR/IXFR + NOTIFY, TSIG; dynamic DNS updates "with security policy"; record aging; split horizon / geolocation via "DNS Apps".
- "Built-in DHCP Server that can work for multiple networks" → DNS+DHCP jointly present in the thin pole.
- Governance: "Multi-user role based access with non-expiring API token support"; TOTP 2FA; "Built in HTTP API … all the actions that the web console does can be performed via the API"; built-in logging and query logging.
- Many recursive-resolver/privacy features (block lists, DoT/DoH/DoQ, CNAME cloaking, ECS, DNS64…) — these are resolver capabilities of the serving software, not management-layer structure; used here only as the boundary that the management surface configures whatever the serving software offers.

## Cross-product Comparison

| Dimension | Infoblox Universal DDI | Micetro | Windows Server DNS/DHCP/IPAM | Technitium |
|---|---|---|---|---|
| Authoritative DNS config as managed data | Zones, views, resource records, ACLs, TSIG, config profiles | Zones, resource records (per-object RBAC), imports | Zones (primary/secondary/stub), records, conditional forwarders, DNSSEC | Primary/secondary/stub/forwarder zones, records, DNSSEC |
| DHCP config as managed data | Scopes (+resize), option spaces/groups, filters, fingerprints, HA groups | (via managed servers + address spaces; details not fetched) | Scopes, pools, exclusions, reservations, lease duration, options, policies | Built-in DHCP for multiple networks |
| Managed propagation to servers | Explicit: sequential per-server config updates from Portal, update-interval visibility | Explicit: approved changes applied to DNS servers; Failed state on application errors | Explicit: IPAM manages discovered DNS/DHCP servers centrally; per-server consoles coexist | Explicit: clustering console manages 2+ instances |
| Serving infra model | Own NIOS/NIOS-X servers + Microsoft DNS + BIND + Route 53/Azure/GCP (two-way sync) | Agnostic overlay over existing servers/appliances | OS roles on domain-joined servers, multi-forest | Own server instances (clustered) |
| DNS↔DHCP/IP coupling | IPAM module + DDI consolidation; Microsoft Integration; (PTR automation evidenced in IPAM-influenced suites; here: IPAM Federation) | DNS request pends the corresponding IP address for allocation | Dynamic DNS from leases; auto-keep PTR; DDI lifecycle for both operations | Co-resident DHCP + DNS on same server |
| RBAC | Portal users + ACLs (zone-level ACL templates observed) | Built-in + custom roles, per-zone/per-server permissions, SSO | IPAM RBAC with access scopes (incl. DNS records/zones) | Multi-user RBAC + API tokens |
| Change governance | Recycle Bin, import/export, reports, audit surfaces (details not fetched) | Approval workflow (Requester/Approver), scheduling, reject-with-reason, object change history | DHCP audit logging; utilization history | Query/system logging (no formal approval workflow observed) |
| API/automation | WAPI, Terraform, Ansible, VMware Aria providers | Single unified API over heterogeneous backends | PowerShell/IPAM cmdlets; Server Manager; Windows Admin Center | HTTP API |
| Operational visibility | Reports, service reload/update interval disclosure | Reports, object history/logs, service management | Monitoring/logging features; utilization data | DNS stats, logs |
| High availability | DHCP HA groups; anycast addressing | Failover management; xDNS redundancy | DHCP failover (two servers share a scope) | (not observed on page) |
| Security-add-on adjacency | Threat Defense (separate product); RPZ, DNS Forwarding Proxy | SNMP profiles, event hooks | DNSSEC, secure dynamic updates, AD authorization | RPZ-style block lists, DoT/DoH/DoQ |

Layer-B cross-product commonalities (observed across the sample):
- All four separate the *management surface* from the *serving instances*, with a config→apply→operate loop, in different architectures (cloud portal, overlay, OS feature, embedded console + clustering).
- All four hold DNS zone/record data and DHCP assignment config as managed objects with RBAC around them.
- Three of four explicitly evidence the DHCP↔DNS coupling (dynamic DNS from leases / PTR maintenance / record-change-pends-IP). The fourth (Technitium) co-residents DHCP+DNS but page-level evidence of automatic coupling was not fetched.
- All four expose an API or automation surface for the same actions as the GUI.
- High-availability arrangement of DHCP serving is evidenced in three of four (Infoblox, Micetro, Microsoft).

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (minimal)

The Type is recognizable when all three hold:

1. **Authoritative DNS configuration as managed data** — zones of resource records (the network's name→address/service data) exist as manageable objects, defined and edited apart from any single server's local configuration.
2. **Authoritative DHCP assignment configuration as managed data** — address-assignment policy (scopes/subnets with pools, exclusions, reservations, options, lease terms) exists as manageable objects.
3. **Managed propagation to serving instances** — the application carries its configuration onto the servers that actually answer DNS queries and grant DHCP leases (one or many), i.e., a config→apply→operate loop owned by the management layer.

Remove 1 or 2 → it becomes management of only one service (a partial capability, typically inside another Type's surface). Remove 3 → it becomes direct per-server administration (editing zone files / server config by hand), i.e., server software administration, not a management application.

Not in L0 (deliberately): multiple-server fleets (single-instance consoles still count — the layer/instance separation is the signature, not the count); dynamic DNS coupling; IPAM; RBAC; audit; APIs; cloud; DNSSEC. Historical check: 1990s-era central DDI management (central store of DNS/DHCP config pushed to BIND/DHCPd servers) satisfies all three legs with no cloud, API, or RBAC; platform-native Windows satisfies them with AD-integrated zones + IPAM; the pre-Type state is per-server config editing (fails leg 3). Check passed.

### L1 — Common Mature Structure (standard capabilities in mature products)

- **Serving-instance inventory** — the DNS servers and DHCP servers being managed, with grouping (server groups / grids / clusters), discovery (Windows IPAM discovers servers), and deployment status.
- **DNS management breadth** — multiple zone types (primary/secondary/stub/forward), record-type breadth, zone views / split-horizon, ACLs, forwarding/conditional forwarding, TSIG/GSS-TSIG, DNSSEC signing.
- **DHCP management breadth** — option spaces/groups, client filters/policies, reservations, scope resizing, high-availability pairing/failover.
- **DNS↔DHCP coupling** — leases trigger automatic DNS record updates (A/PTR); record and address views are linked. This is the structural reason the two services are managed together (industry: "DDI"), though a product can satisfy L0 without it.
- **IPAM integration** — address-space data (blocks/subnets/utilization/free-address) alongside assignment config; record changes can affect address availability.
- **Governance** — RBAC with per-object scoping; audit/change history; in the enterprise pole, approval workflows with scheduling for changes before they reach servers.
- **Operational visibility** — service health/status, query and lease activity, reports, utilization.
- **API/automation surface** — REST/HTTP API, PowerShell, Terraform/Ansible providers; "everything the GUI does" is commonly scriptable.

### L2 — Variant / Optional Structure

- Deployment posture: cloud-managed SaaS with lightweight serving nodes vs on-prem appliance/grid vs agnostic overlay over third-party servers vs OS-native roles + management feature vs open-source single box with embedded console.
- Public-cloud DNS integration (managing AWS/Azure/GCP zones, two-way sync) — evidenced in the cloud-managed suite pole.
- Approval workflows for DNS changes (module/edition dependent — direct evidence in one product).
- DNS traffic control (weighting/geo responses), response-policy zones, anycast management — advanced/security-adjacent options.
- Tenant/forest/multi-org scoping (multi-forest AD support; MSP-style segmentation).
- Security-operations adjacency (DNS-layer threat defense) — typically a separate product/edition.

### L3 — Vendor-specific (kept out of final document)

- Infoblox: NIOS Grid, NIOS-X as a Service, Infoblox Portal licensing/license pooling, WAPI native syntax, IPAM Federation, B1 appliance models, specific reload-time/update-interval tables.
- Micetro: xDNS Redundancy, specific Request state machine labels, folder management, SNMP profiles, license-key-gated Workflow module.
- Microsoft: AD/DNS/DHCP role interplay specifics, DHCP authorization in AD, Windows Admin Center, IPAM purge/utilization specifics, Find-IpamFreeSubnet/Range cmdlets.
- Technitium: DNS Apps, ANAME/APP proprietary records, block-list machinery, specific default console credentials flow.

## Rejected Findings

- "Resolver features (caching, DoH/DoT, ad blocking, ECS)" are NOT part of the management Type — they are capabilities of the serving software that the management layer exposes/configures. Admitting them would collapse the Type into "DNS server software."
- "Cloud DNS console" as the Type's center would overfit one deployment era: those consoles manage a single provider's zones with no DHCP side and no fleet propagation.
- "DDI = DNS+DHCP+IPAM always fused" as a definitional claim: fusion is the dominant packaging, not the definition — IPAM planning data is L1 coupling, and platform-native pole satisfies the Type with looser coupling.
- Approval workflow as definitional: single-product direct evidence (Micetro); enterprise-plausible but must stay Common/Optional.

## Boundary Findings

- **vs IPAM (sibling leaf)**: IPAM is the address-space discipline (plan, track, discover, report utilization of IP space). DNS & DHCP Management operates the *services* (resolution and assignment). Seam test: remove the ability to configure/operate DNS and DHCP services themselves → pure IPAM; remove IPAM planning data → still DNS & DHCP Management. In the market they ship fused (all enterprise samples), which is packaging, not taxonomy.
- **vs Network Management / Network Monitoring**: different object domain (devices, interfaces, routing, health metrics vs zone/record/scope/lease configuration). Monitoring observes; this Type operates configuration.
- **vs DNS server software (BIND, PowerDNS, Windows DNS role alone)**: server software *is* a serving instance; the Type is the layer that manages authoritative config and propagation across instances. A product can embed both (open-source pole), but the management surface remains the Type's subject.
- **vs cloud provider DNS consoles (Route 53, Azure DNS, GCP console)**: single-provider DNS-zone surfaces, no DHCP, no multi-server propagation of the operator's own fleet; DDI products instead *integrate* them as managed targets. Adjacent capability, not the Type's center.
- **vs web-hosting control panels**: they manage zones as artifacts of hosting accounts, not as network-service infrastructure operation.
- **vs domain registrars**: registration/delegation of public names vs operation of resolution for a network.
- **"去掉什么就变成另一个 Type" judgments**: remove DHCP side → DNS-only management (adjacent capability; in cloud consoles belongs to cloud platforms); remove DNS side → DHCP management only (rare standalone; usually a server console); remove propagation leg → server administration tooling; remove both service configs and keep only address planning → IPAM.

## Uncertainties

- BlueCat Address Manager and EfficientIP SOLIDserver could not be fetched; enterprise-suite breadth rests on 2 enterprise products + category structure. Claims about "most enterprise products" are calibrated to "mature products commonly / in the researched sample."
- Micetro DHCP-side object detail (scopes/leases UI) was not fetched; its DHCP evidence comes from the admin-guide structure and its overlay self-description.
- Technitium DHCP management depth (leases view, reservations) not fetched; only "built-in DHCP Server" at page level.
- Infoblox report/audit surface details not fetched (module existence only).
- Whether the DHCP↔DNS coupling is universal in the thin pole is unverified.

## Final Synthesis

A DNS & DHCP Management application is the network team's operating layer over the two foundational network services. Its defining structure: authoritative name data (zones/records) and authoritative assignment policy (scopes/pools/options/reservations) held as centrally managed objects, plus a deployment mechanism that carries that configuration onto the running servers that resolve names and grant leases. Around that core, mature products add server inventory and grouping, the lease→record coupling that motivates joint "DDI" management, IPAM-adjacent address data, RBAC/audit/approval governance, operational visibility, and automation APIs. Packaging varies sharply — cloud-managed suites that manage their own and others' servers, agnostic overlays over existing servers, OS-native roles with a central management feature, and open-source boxes with embedded consoles — but the management-layer-over-serving-instances structure and the two authoritative data domains recur in all poles and across eras (historical check passed against pre-cloud central DDI management and platform-native deployments).
