# Research Notes — IP Address Management / IPAM

Research date: 2026-09-08
Slug: `ip-address-management-ipam` (Directory §14 IT, Cloud & Infrastructure)

## Research Goal

Understand what an "IP Address Management / IPAM" application actually is as an Application Type: what objects it manages (space, subnets, addresses), what "management" means (plan? allocate? discover? report?), how it relates to the sibling Type DNS & DHCP Management (the "DDI" bundle), who operates it, and where its boundaries lie against network management/monitoring, CMDB, DCIM, and cloud management.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: IPAM is the address-space discipline of the DDI triad — the system of record for planning, allocating, tracking, and auditing an organization's IP address space (blocks, subnets, individual addresses) — as distinct from operating DNS/DHCP services (sibling leaf `dns-dhcp-management`, processed pass drew the seam: "IPAM is the address-space discipline (plan, track, discover, report utilization of IP space). DNS & DHCP Management operates the *services*").
- Likely confusion surfaces: DNS & DHCP Management (sibling; market fuses them as "DDI"), Network Management / Network Monitoring (device health vs address ledger), CMDB (generic CI records vs IP-specific structure), DCIM (physical layer vs logical address layer), IT Asset Management (financial lifecycle vs address resource), cloud-provider VPC address consoles.
- Key unknowns: Is discovery/scanning definitional or a common population mechanism? Is DNS/DHCP integration definitional or packaging? Does a pure-IPAM product shape exist in the market (to prove the seam)? Historical check: does the spreadsheet-era IP ledger satisfy the definition?

## Research Questions

1. What are the core managed objects? (aggregates/blocks, subnets/prefixes, addresses, ranges; what attributes and states does each carry?)
2. What does "management" mean operationally — what are the defining workflows over those objects? (divide/subnet, allocate/reserve, find-free, reclaim, report utilization)
3. How does the record relate to reality? (manual entry / planned source-of-truth vs live discovery/scanning reconciliation; address status semantics)
4. What couplings exist to DNS and DHCP? Are they definitional or common/packaging?
5. What organizational structures wrap the space? (sections/sites, VRFs/routing contexts, VLANs, tenancy)
6. What governance exists? (RBAC per section/subnet, request/approval workflows, audit)
7. What interfaces? (subnet tree explorer, address tables, free-space display, search, utilization reports, API)
8. Boundary vs sibling DDI leaf and vs monitoring/CMDB/DCIM — what exactly does IPAM do that they don't?
9. Historical check: do spreadsheet-era IP ledgers and pre-cloud IPAM products fit the same core?

## Representative Products

| Product | Philosophy / pole | Why selected |
|---|---|---|
| phpIPAM | Open-source, self-hosted, *pure* standalone IPAM (no DNS/DHCP service operation in core) | The cleanest pure-address-management pole; rich API documents the data model |
| NetBox | Open-source network "source of truth" (IPAM + DCIM); planned/documented data, not live scanning | Opposite posture: IPAM as part of a curated network model; proves discovery is not definitional |
| SolarWinds IP Address Manager | Commercial standalone mid-market IPAM module; discovery/scanning-led with DHCP/DNS management included | The discovery-led commercial pole; markets itself as "replace IP tracking spreadsheets" |
| Infoblox Universal DDI | Enterprise cloud-managed DDI suite; IPAM fused with DNS/DHCP service operation | Enterprise-suite pole; the market's reference "DDI" packaging |
| Microsoft Windows Server IPAM | Platform-native OS feature; central management over AD-joined servers | Non-suite, bundled-in-OS pole + platform-native/historical check |

Rejected from sample (recorded, not silently dropped): BlueCat Address Manager and EfficientIP SOLIDserver — sibling pass (dns-dhcp-management, 2026-09-08) recorded repeated transport errors on both vendors' doc sites; not re-attempted per network-restriction rules. Their absence weakens enterprise-pure-IPAM breadth; assertions calibrated accordingly.

## Sources

Evidence layer A (directly observed, fetched 2026-09-08):

1. phpIPAM — home page: https://phpipam.net/
2. phpIPAM — Feature list: https://phpipam.net/documents/features/
3. phpIPAM — API reference: https://phpipam.net/api/api_reference/
4. NetBox — documentation root: https://docs.netbox.dev/en/stable/
5. NetBox — IPAM models index: https://docs.netbox.dev/en/stable/models/ipam/
6. NetBox — Prefix model: https://docs.netbox.dev/en/stable/models/ipam/prefix/
7. NetBox — IP Address model: https://docs.netbox.dev/en/stable/models/ipam/ipaddress/
8. Microsoft Learn — IP Address Management (IPAM) top: https://learn.microsoft.com/en-us/windows-server/networking/technologies/ipam/ipam-top
9. Microsoft Learn — Manage IPAM: https://learn.microsoft.com/en-us/windows-server/networking/technologies/ipam/manage-ipam
10. SolarWinds — IP Address Manager product page: https://www.solarwinds.com/ip-address-manager
11. SolarWinds — IPAM Administrator Guide (shell; body content not served): https://documentation.solarwinds.com/en/success_center/ipam/content/ipam_administrator_guide.htm
12. Infoblox — Documentation Portal root: https://docs.infoblox.com/
13. Infoblox — Universal DDI Management: https://docs.infoblox.com/space/BloxOneDDI/186614365/Infoblox+Universal+DDI+Management

Inherited layer-A evidence from the sibling pass (research/dns-dhcp-management.md, 2026-09-08): Microsoft WS2016 "What's new" DDI/IPAM quotes (IP address inventory with associated DNS records, auto PTR maintenance, DNS zone/record management, RBAC with access scopes, utilization data with purge, free-subnet/free-range finders, multi-forest); Infoblox portal DNS/DHCP area structure; Micetro DNS-change-pends-IP-address coupling quote.

Access limitations: SolarWinds admin-guide body unreachable (page shell + nav only) — SolarWinds evidence is Tier-2 (product page) only. Infoblox IPAM-module object detail (address/subnet model inside Universal DDI) not directly fetched — enterprise IPAM evidence rests on DDI consolidation text (Tier-1) plus inherited sibling evidence. NetBox allocation-helper endpoints (available-IP/available-prefix) not fetched — allocation workflow inferred from model pages, not quoted. No precise numeric limits, scan intervals, or plan-gated defaults are reproduced anywhere.

## Product Observations

### phpIPAM (open source) — layer A

- Self-description: "open-source web IP address management application (IPAM)" with "IPv4/IPv6 IP address management", "Section / Subnet management", "Automatic free space display for subnets", "Visual subnet display", "Automatic subnet scanning / IP status checks", "IP database search", "VLAN management", "VRF management", "IPv4 / IPv6 calculator", "IP request module", "Per-group section/subnet permissions", "Domain authentication (AD, LDAP, Radius)", "Device / device types management", "RIPE subnets import", "XLS / CVS subnets import", "NAT support", "RACK management", "PowerDNS integration", "REST API".
- API reference exposes the canonical object graph directly:
  - **Sections** (top-level containers) → `sections/{id}/subnets`, `sections/{id}/subnets/addresses`; deleting a section "deletes ... all belonging subnets and addresses".
  - **Subnets** → `subnets/{id}/usage` ("Returns subnet usage"), `slaves` / `slaves_recursive` (parent-child hierarchy), `subnets/{id}/addresses`, `subnets/{id}/first_free` ("Returns first available IP address in subnet"), `subnets/{id}/first_subnet/{mask}` / `all_subnets/{mask}` ("first/last/all available subnet within selected for mask"), `resize` ("Resizes subnet to new mask"), `split` ("Splits subnet to smaller subnets"), `truncate` ("Removes all addresses from subnet"), `permissions`, `overlapping/{subnet}` ("Returns all overlapping subnets"), search by CIDR.
  - **Addresses** → per-address `ping` ("Checks address status"), `tags` ("Returns all tags" + addresses per tag), `search/{ip}`, `search_hostname`, `search_mac`, `first_free/{subnetId}` including POST "Creates new address in subnets – first available", delete with "remove_dns=1 parameter to remove all related DNS records".
  - **VLANs + L2 domains**, **VRFs** (`vrf/{id}/subnets`), **devices** (`devices/{id}/addresses`, `devices/{id}/subnets`), **locations/racks**, **NAT objects**, and a **prefix-delivery controller** (`prefix/{customer_type}/...`: "Returns all subnets used to deliver new subnets", POST "Creates first available subnet for ip version and requested mask") — an MSP-style automated allocation API.
- Structural reading: the product is a ledger over address space (sections → subnets → addresses) with allocation helpers (first-free, subnet-splitting), state semantics (tags; ping status), context overlays (VLAN, VRF, device, location), and import from upstream registries/spreadsheets (RIPE, XLS/CSV). DNS integration is present (PowerDNS; remove-DNS-on-delete) but DNS zones are not managed here.

### NetBox (open source; network source of truth) — layer A

- Self-description: "By combining the traditional disciplines of IP address management (IPAM) and datacenter infrastructure management (DCIM) with powerful APIs and extensions, NetBox provides the ideal 'source of truth' to power network automation." "Unlike general-purpose configuration management databases (CMDBs), NetBox has curated a data model which caters specifically to the needs of network engineers and operators." Object list includes "IP prefixes, ranges, and addresses; VRFs and route targets; ... VLANs and scoped VLAN groups; AS numbers; hierarchical regions, sites, and locations; ... Virtual machines and clusters; ... Tenancy assignments."
- IPAM model page lists: Aggregate, ASN, ASN Range, FHRP Group (+assignment), IP Address, IP Range, Prefix, RIR, Role, Route Target, Service (+template), VLAN, VLAN Group, VLAN translation policy/rule, VRF.
- **Prefix model** (direct quotes): "A prefix is an IPv4 or IPv6 network and mask expressed in CIDR notation ... Prefixes are automatically organized by their parent aggregate and assigned VRF." Fields: Prefix; **Status** ("The prefix's operational status ... The 'container' status indicates that the prefix exists merely as a container for organizing child prefixes"); VRF ("Prefixes with no VRF assigned are considered to exist in the 'global' table"); Role (user-defined functional role); **Is a Pool** ("first and last IP addresses ... normally reserved as the network and broadcast addresses ... will be considered usable. This option is ideal for documenting NAT pools"); **Mark Utilized** ("this prefix will report 100% utilization regardless of how many child objects have been defined within it"); Scope (region/site/site group/location — "This field replaced the site field in NetBox v4.2"); VLAN ("This mapping is helpful for associating IP space with layer two domains. A VLAN may have multiple prefixes assigned to it").
- **IP Address model** (direct quotes): "An IP address object in NetBox comprises a single host address (either IPv4 or IPv6) and its subnet mask, and represents an IP address as configured on a network interface. IP addresses can be assigned to device and virtual machine interfaces, as well as to FHRP groups"; primary IP designation per device/VM per family; **NAT** ("An IP address can be designated as the network address translation (NAT) inside IP address for exactly one other IP address ... This relationship is followed in both directions"); fields: Address; **Status** ("operational status"); **Role** (Loopback, Secondary, Anycast, VIP, VRRP, HSRP, GLBP, CARP); VRF (optional, "global table"); **DNS Name** ("A DNS A/AAAA record value associated with this IP address").
- Structural reading: the space is a curated, planned model (aggregates from RIRs → prefixes → addresses) with explicit state and roles; live-network discovery is not part of the documented core — the product centers on *documenting/intending* the network (its own framing as "source of truth" for automation), with the address bound to the interface that will hold it. DNS appears only as an attribute (DNS name), not zone management.

### SolarWinds IP Address Manager (commercial standalone module) — layer B (Tier-2 product page; admin-guide body unreachable)

- Self-description: "IP address management software, a key feature of SolarWinds Observability Self-Hosted"; "comprehensive visibility, efficient IP allocation, and quick conflict resolution"; "Automatically discover and manage IP addresses across on-premises and cloud environments."
- FAQ-level operational claims (direct quotes): "helps you discover, track, and manage IPv4 and IPv6 addresses from a centralized interface. Automated IP address scanning gives you current visibility into address usage while reducing the time and errors associated with manual tracking"; "automatically scans your network to identify used, available, reserved, and abandoned IP addresses. You can search across subnets, reclaim unused addresses, and monitor DHCP address pools to find an available IP before making an assignment"; "combines IP address, DHCP, and DNS monitoring and management in one interface. You can manage DHCP servers and scopes, DNS servers and zones ... including support for Cisco, Infoblox, ISC, Kea, and Microsoft"; "monitors IP address activity and alerts you when it detects a conflict ... can also alert you to depleted subnets or DHCP scopes and mismatched DNS entries"; "Utilization views, historical usage data, alerts, and customizable reports help you identify limited address space and plan for subnet or DHCP scope depletion"; **"How can I replace IP tracking spreadsheets...?"** — "SolarWinds IPAM replaces manually maintained spreadsheets with automated discovery and centralized IP address data."
- Use-case page names: IP Address Scanner, IP Address Tracker, DDI (DNS/DHCP/IPAM), DHCP Management and Monitoring, IP Address Discovery, IP Address Planning, IP Subnetting, IPAM for Virtual Environments, Find IP Address, Network Scanner, Resolve IP Address Conflict.
- Structural reading: the discovery-led posture — the ledger is continuously reconciled against the live network (scanning), state vocabulary is used/available/reserved/abandoned, and the workflow emphasis is conflict detection, reclaim, and depletion planning. DNS/DHCP management is bundled (DDI packaging).

### Infoblox Universal DDI (enterprise cloud-managed suite) — layer A (positioning level) + inherited sibling layer-A detail

- Direct: "Universal DDI Management ... enables organizations to simplify DDI management (DNS, DHCP, and IP address management) across on-premises environments and public clouds by offering unified management, in-depth visibility and insights, and infrastructure-free deployment." "Consolidates configuration and control of several DDI services, including Microsoft DNS, BIND, NIOS Grid deployments, NIOS-X Physical and Virtual Servers ..., Amazon Route 53, Azure DNS and Google Cloud DNS." "The solution delivers secure, reliable, and centrally-managed DNS, DHCP, and IPAM services at each location."
- Pain points named on the page map to IPAM concerns: "Limited Visibility: ... Without a unified view of network assets, organizations struggle with undetected zombie workloads and resource mismanagement."
- Inherited sibling layer-A: Universal DDI portal areas (Zones, DNS Server Groups, DHCP Config Profiles, Option Spaces...), "IPAM Federation" and "Microsoft Integration" listed as modules; the IPAM module exists inside the suite but its object detail was not fetched this pass.
- Structural reading: in the enterprise pole, IPAM ships as one leg of a fused DDI suite; address management is presented together with — but distinct from — DNS/DHCP service configuration (the suite names them as three services).

### Microsoft Windows Server IPAM (platform-native feature) — layer A

- Direct: "IP Address Management (IPAM) is an integrated suite of tools to enable end-to-end planning, deploying, managing and monitoring of your IP address infrastructure, with a rich user experience. IPAM automatically discovers IP address infrastructure servers and Domain Name System (DNS) servers on your network and enables you to manage them from a central interface."
- Direct (Manage IPAM): "IPAM supports DNS resource record, conditional forwarder, and DNS zone management for both domain-joined Active Directory-integrated and file-backed DNS servers. In addition, IPAM supports role-based access control..."
- Inherited sibling layer-A (WS2016 What's New): "view all DNS resource records associated with an IP address in the IP Address Inventory"; "automatically keep pointer (PTR) records of IP addresses and manage IP address lifecycles for both DNS and DHCP operations"; IP utilization data with purge; free-subnet/free-range finders; RBAC with access scopes; multiple AD forests.
- Structural reading: the OS-native pole proves the management layer is separable from the services: IPAM discovers servers, holds a central address inventory with utilization, and finds free space — while ALSO bundling DNS/DHCP management (platform packaging).

## Cross-product Comparison

| Dimension | phpIPAM | NetBox | SolarWinds IPAM | Infoblox Universal DDI | Windows Server IPAM |
|---|---|---|---|---|---|
| Space as structured record | Sections → subnets → addresses (API-proven hierarchy: slaves, slaves_recursive) | Aggregates (RIR) → prefixes → addresses/ranges; container status; global table vs VRF | Subnets with scanning-derived address states; subnet planning/subnetting use-cases | IPAM leg of DDI suite (module named; detail not fetched) | Central IP address inventory over discovered infrastructure |
| Allocation state semantics | Address tags + ping status checks; free-space display | Status field on prefixes & addresses; roles (loopback/VIP/anycast...) | used / available / reserved / abandoned identified by scanning | (not directly fetched) | IP address inventory + utilization data |
| Allocation helpers | first_free (GET/POST), first_subnet/all_subnets by mask, resize, split, truncate, overlapping search | Model supports planned allocation (not directly quoted) | "find an available IP before making an assignment"; reclaim unused | (suite context) | free-subnet / free-range finders |
| Reconciliation vs plan | Scanning/IP status checks (opt-in automation) | Planned source of truth; live discovery not in documented core | Continuous automated scanning | Suite visibility angle ("undetected zombie workloads") | "automatically discovers IP address infrastructure servers" |
| DNS linkage | PowerDNS integration; remove_dns on delete; (zones NOT managed) | DNS Name attribute ("A/AAAA record value") | unified view; "mismatched DNS entries" alerts; DNS zones managed (DDI bundle) | DDI fusion (zones managed) | DNS record/zone management; auto-PTR (DDI bundle) |
| DHCP linkage | none in core (pure IPAM) | none in core (models, not operation) | DHCP pool monitoring; DHCP servers/scopes managed (DDI bundle) | DHCP managed (DDI fusion) | DHCP integrated; lease/DHCP lifecycle management (DDI bundle) |
| Context overlays | VLANs + L2 domains, VRFs, devices, locations, racks, NAT objects, customers (prefix delivery) | VRFs, VLANs, roles, tenancy, NAT inside/outside, FHRP groups, services | virtual environments; hybrid cloud scope | (suite) | AD forests as scope |
| Governance | per-group section/subnet permissions; AD/LDAP/RADIUS auth; IP request module | (users/tenancy models exist; detail not fetched) | platform user management | (suite) | role-based access control with access scopes |
| Reports/audit | changelogs; usage endpoint | utilization fields (mark-utilized) | utilization views, historical usage, alerts, reports | visibility/insights positioning | utilization data with purge; reporting |
| API | REST API (full CRUD + allocation) | REST & GraphQL | platform API (not fetched) | WAPI (inherited) | PowerShell cmdlets |
| Pure-IPAM or DDI-fused | PURE (no DNS/DHCP operation) | PURE (attributes only) | FUSED (bundle) | FUSED (suite) | FUSED (bundle) |

Layer-B cross-product commonalities (observed across the sample):

- All five hold the address space as a structured hierarchy of containers (blocks/aggregates/subnets) and individually addressable entries, with CIDR as the organizing geometry (direct evidence in 3 open/standalone poles; suite/platform poles name the inventory and planning).
- All five are built around allocation state: every address/subnet carries an explicit status, and the application answers "what is free / what is taken / who holds it" from its record (direct evidence in 4 of 5; Infoblox not directly fetched).
- All five connect addresses to DNS names in some form (direct in 4; Infoblox via DDI fusion), but only the DDI-fused poles manage zones/records as operational objects — the linkage is common, service operation is packaging.
- Hierarchical containment math is user-visible everywhere it was directly observed: subnet splitting/resizing, child subnets, overlapping detection, free-subnet finding (phpIPAM, Windows directly; SolarWinds use-case naming; NetBox prefix/container model).
- REST/PowerShell APIs exposing the same object graph as the GUI: direct in 4 (phpIPAM, NetBox, Windows, Infoblox-inherited).
- Two postures coexist in the market: planned source-of-truth (NetBox; phpIPAM's manual-plus-optional-scan) vs live-reconciliation (SolarWinds scanning; Windows discovery) — both keep the ledger as the center.

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (minimal)

The Type is recognizable when both hold:

1. **The address space as structured data of record** — the organization's IP space held as individually addressable records organized by CIDR hierarchy: containers (blocks/aggregates/subnets) and address entries, each carrying attributes and allocation state. (The record, not the live network, is the thing the application owns.)
2. **An allocation lifecycle performed against that record** — space is divided (subnetted), assigned, reserved, tracked to holders, searched for free space, and reclaimed through the application; "what is free, what is taken, who/what holds it, how full is this subnet" are answered authoritatively from the record.

Remove leg 2 → a static network map / inventory viewer / routing-table report (observation, not management). Remove leg 1 → a generic allocation or asset tool with nothing address-shaped (no CIDR structure, no hierarchy math, no address identity). Both legs are jointly load-bearing.

Not in L0 (deliberately): discovery/scanning (the source-of-truth pole lacks it; the spreadsheet pre-history lacks it); DNS/DHCP coupling or service operation (pure-IPAM poles lack it); RBAC, APIs, cloud, IPv6, VRFs, VLANs, conflict detection, reporting. Historical check below.

### Historical / Market-Sample Check (§24 analog-level)

- Spreadsheet-era IP ledger: a maintained spreadsheet of subnets and allocated addresses with holder/purpose columns, edited to allocate and free addresses — satisfies both legs at analog level (structured record + allocation lifecycle). SolarWinds itself names this pre-history ("replaces manually maintained spreadsheets").
- Pre-cloud standalone IPAM (2000s-era web IPAM): same ledger + allocation helpers, no cloud/API/SCIM-era machinery — satisfies.
- Platform-native and registry-adjacent forms: RIR delegation records and registry allocations show the "space as data + allocation" pattern outside the enterprise tool market, but the public registry is a distinct institution (delegation of public space) — adjacent, not this Type's center.
- NetBox (source-of-truth pole, no live scanning) and phpIPAM (no DHCP/DNS operation in core) both satisfy the two legs — proving discovery and DDI fusion are not definitional.
Check passed.

### L1 — Common Mature Structure (standard capabilities in mature products)

- **Space organization layer above subnets** — sections/groups/sites/locations/regions and scope assignment (phpIPAM sections, NetBox scope/region/site/location directly).
- **Allocation-state vocabulary** — named statuses/tags on addresses and subnets (in use / reserved / free / abandoned; operational statuses; functional roles) (phpIPAM tags, NetBox status/roles, SolarWinds state vocabulary directly).
- **Free-space and capacity machinery** — find-first-free address, find free subnet of a requested mask, utilization accounting and thresholds, depletion planning (phpIPAM first_free/first_subnet/usage, Windows finders/utilization, SolarWinds utilization views directly).
- **Reconciliation against reality** — automated subnet scanning/IP status checks (phpIPAM optional, SolarWinds continuous, Windows discovery) — common but posture-dependent: the source-of-truth pole deliberately omits it.
- **IP↔DNS name linkage** — DNS name as an address attribute; some products create/remove DNS records with the address (phpIPAM PowerDNS + remove_dns, NetBox dns_name attribute, SolarWinds mismatch alerts, Windows auto-PTR). Zone/record operation itself belongs to the sibling Type.
- **DHCP visibility** — pool/lease data feeding the address picture; in DDI-fused products, DHCP management (SolarWinds, Windows, Infoblox). Pure-IPAM poles lack it entirely.
- **Context overlays** — VLAN association, VRF / routing-table separation, NAT relationships, device/VM interface binding, tenancy (phpIPAM, NetBox directly; SolarWinds virtual environments).
- **Governance** — permission scoping down to section/subnet (phpIPAM, Windows RBAC directly); request/approval workflows for address requests in some products (phpIPAM IP request module — single-product direct → Optional).
- **Search and reporting** — database-wide search by IP/hostname/MAC; utilization/history reports (phpIPAM, SolarWinds directly).
- **IPv4+IPv6 dual-stack throughout** — named by every product whose documentation was fetched.
- **API surface** — REST/GraphQL/PowerShell covering the same operations as the GUI (4 of 5 directly).

### L2 — Variant / Optional Structure

- Product-shape poles: pure standalone IPAM (phpIPAM) vs network source-of-truth with DCIM (NetBox) vs commercial monitoring-suite module with DDI bundling (SolarWinds) vs enterprise cloud-managed DDI suite (Infoblox) vs OS-native feature (Windows IPAM) vs cloud-provider-native address management for their own virtual networks (market context; not fetched).
- Posture: planned/documentation-led vs discovery/scanning-led vs hybrid.
- Request/approval workflows for address allocation (single-product direct evidence → Optional).
- Automated subnet allocation "delivery" APIs for customers/tenants (phpIPAM prefix controller — single-product → Optional).
- MSP/multi-tenant segmentation; overlapping-space management via VRFs (products targeting larger/multi-tenant environments).
- Adjacent bundled modules: racks/DCIM, NAT policy, IP conflict alerting, "IPAM for virtual environments", cloud-scope extension.

### L3 — Vendor-specific (kept out of final document)

- phpIPAM: PowerDNS specifics, RIPE import, L2 domains, customer_type prefix API semantics, XLS/CSV import formats, version numbering.
- NetBox: FHRP groups, ASN/ASN-range/RIR models, route targets, VLAN translation policies, services/service templates, mark-utilized semantics, PREFER_IPV4, FIELD_CHOICES status customization, v4.2 scope-field migration.
- SolarWinds: Orion/SolarWinds Platform integration, supported DHCP/DNS vendor list (Cisco, Infoblox, ISC, Kea, Microsoft), 30-day trial, alert taxonomy.
- Infoblox: NIOS Grid, NIOS-X (as a Service), Universal Asset Insights, IPAM Federation, license pooling/portability, WAPI.
- Microsoft: AD forests, AD-integrated/file-backed DNS management, DHCP authorization, purge-utilization, IPAM cmdlets, access scopes in PowerShell.

## Rejected Findings

- **"IPAM = DDI" as definition** — rejected: fusion is the dominant commercial packaging, but two of five sampled products are pure IPAM with no DNS/DHCP service operation; the sibling pass drew the same seam from the other side.
- **"Discovery/scanning is definitional"** — rejected: source-of-truth pole excludes it; the spreadsheet pre-history lacks it; phpIPAM ships it as an optional check.
- **"IPAM manages devices"** — rejected: devices/hosts appear as attribute-holders of addresses (hostname, device binding), but device inventory/health belongs to network management/CMDB/DCIM.
- **"Conflict detection is definitional"** — rejected: it is a capability of the reconciliation layer in scanning-led products; single-/few-product evidence; Optional.
- **"The address ledger must be live-accurate"** — rejected as definitional: the planned posture holds intended state as authoritative; drift handling differs by posture (noted as behavior, not invariant).

## Boundary Findings

- **vs DNS & DHCP Management (sibling leaf)** — the sharpest seam, drawn jointly with the sibling pass: IPAM is the address-space discipline (plan, allocate, track, reclaim, report); DNS & DHCP Management operates the services (resolution and lease assignment). Seam test: remove the ability to configure/operate DNS and DHCP services → pure IPAM (phpIPAM, NetBox prove the shape exists as products); remove the address ledger → DNS & DHCP service management still stands. The market ships them fused (SolarWinds, Infoblox, Windows) — packaging, not taxonomy. Confirmed from both directions this pass.
- **vs Network Management / Network Monitoring** — different object domain: devices, interfaces, health metrics, alerts vs the address-space ledger. Monitoring observes live state; IPAM holds the allocation record. Scanning-led IPAM borrows monitoring's techniques (ping, SNMP, discovery) but the output is ledger state, not health/alerting (SolarWinds bundles both, which is packaging).
- **vs CMDB** — CMDB holds generic configuration items and typed relationships; IPAM holds IP-space-specific structure (CIDR hierarchy, containment math, allocation state). CMDB pass itself recorded IPAM as a "specialized subset register feeding the CMDB" / population source.
- **vs DCIM** — physical layer (racks, power, cabling) vs logical address layer; DCIM pass recorded "vs IPAM (bundled sibling, distinct model families)". NetBox ships both — model families remain distinct within one product.
- **vs IT Asset Management** — financial/contractual lifecycle of IT assets vs operational address resource management.
- **vs Cloud Management Platform** — CMPs control cloud estates (provisioning, lifecycle) and integrate DNS-IPAM as part of their integration fabric; IPAM is the address-space discipline across on-prem and cloud, not the estate control layer.
- **vs public registries (RIR / WHOIS)** — delegation of public space between institutions vs operational allocation within one organization's space; the org's space typically originates as registry delegations (phpIPAM imports RIPE subnets).
- **"去掉什么就变成另一个 Type" judgments**: remove the allocation lifecycle → static network map/inventory viewer; remove the CIDR-structured space → generic asset/allocation registry; add DNS/DHCP service operation → the DDI-suite packaging of the sibling Type; restrict to physical layer → DCIM; keep only discovered live state with no allocation ledger → monitoring/discovery territory.

## Uncertainties

- Infoblox IPAM-module object detail (how Universal DDI models subnets/addresses) not directly fetched; enterprise-suite IPAM evidence rests on the DDI consolidation text plus inherited sibling observations. Claims about the enterprise pole calibrated to "suite positioning" level.
- SolarWinds admin-guide body unreachable; its evidence is Tier-2 (product page claims). No structural claims beyond the page's own FAQ-level statements.
- NetBox allocation-helper endpoints not fetched; the allocation workflow is inferred from the model pages (status/container/pool fields), not quoted endpoints.
- Windows Server IPAM's current lifecycle status (deprecated in newer server channels?) not investigated; treated as the platform-native/historical pole regardless.
- Whether approval workflows for allocation are common in commercial IPAM is under-evidenced (phpIPAM's IP request module is the only direct sample; the DDI sibling shows change workflows on the DNS side).
- BlueCat / EfficientIP evidence inherited as unreachable from the sibling pass; not re-attempted.

## Final Synthesis

An IP Address Management application is the network team's ledger and planning system for the organization's IP address space. Its defining structure is two-fold and jointly held: the space itself held as structured, CIDR-organized records (containers — blocks, aggregates, subnets — and individually addressable entries carrying attributes and allocation state), and an allocation lifecycle performed against that record — dividing space into subnets, allocating and reserving addresses, tracking what holds them, finding free space, reclaiming the unused, and reporting utilization. Around this core, mature products add space-organization layers (sections/sites), named status vocabularies, free-space and capacity machinery, reconciliation against the live network (scanning/discovery — posture-dependent), IP↔DNS name linkage, DHCP visibility, context overlays (VLAN, VRF, NAT, device binding, tenancy), permission scoping, search, reporting, IPv6 dual-stack, and APIs. The market realizes the Type in sharply different product shapes — pure standalone open-source IPAM, network source-of-truth platforms, commercial monitoring-suite modules, enterprise DDI suites, OS-native features, and cloud-provider-native tools — but the two-leg core recurs in all poles and across eras (historical check: the maintained spreadsheet ledger satisfies it at analog level). The boundary with DNS & DHCP Management was confirmed from both directions: address-space discipline is IPAM; service operation is the sibling Type; fusion is packaging.
