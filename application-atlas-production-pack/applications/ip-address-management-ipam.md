# IP Address Management / IPAM

## Overview

An **IP Address Management (IPAM) application** is the network team's system of record for an organization's IP address space: it holds the space itself — blocks, subnets, and individual addresses — as a structured, searchable record, and it is the medium through which that space is planned, allocated, tracked, and reclaimed.

The problem it solves is as old as networking itself: IP addresses are a finite shared resource consumed by many teams, systems, and sites at once. Without a ledger, the same address gets assigned twice, orphaned allocations are never reclaimed, nobody can say how full a subnet is, and planning for growth means guessing. IPAM turns "who has what address, what is free, and how much is left" into questions answered from a maintained record instead of tribal memory and spreadsheets.

The defining core is deliberately small — two structures held together:

```text
The address space as a structured record
└── CIDR-organized containers (blocks / aggregates → subnets)
    └── Individually addressable entries, each carrying state and attributes
        plus
The allocation lifecycle performed against that record
    (divide → allocate / reserve → track → find free → reclaim → report)
```

Everything else commonly associated with the category — automated network scanning, DNS/DHCP integration, VLAN and VRF overlays, cloud sync, approval workflows, REST APIs — is widespread in current products but is not what makes a product an IPAM. Pure address ledgers without any of those capabilities satisfy this definition; the pre-software form of this discipline, a maintained spreadsheet of subnets and assignments, satisfies it too.

## Users & Context

The primary users are network engineers and network administrators — the people who own address space, run subnets, and hand out addresses. Typical moments that open the application:

- provision a new segment: carve a subnet out of available space for a new site, VLAN, or workload
- assign addresses: pick a free address for a new device, server, or tenant and record who holds it
- answer questions: "is 10.1.2.3 in use?", "what is still free in this subnet?", "who holds this address?", "how full is this range?"
- reclaim and audit: find abandoned allocations before a subnet runs out; prepare utilization reports for planning
- investigate trouble: track down the holder of a conflicting or misbehaving address

Secondary users include infrastructure architects (planning the address plan itself), operations teams consuming the record through integrations and automation, and — in service-provider variants — provisioning staff who allocate address ranges to customers. The work environment is a web console over the whole estate; usage spikes around provisioning and audit moments rather than being continuous.

## Core Model

### The Defining Core

**1. The address space as structured data.** The application holds the organization's IP space as records organized by the CIDR hierarchy of networking itself:

```text
Address space (the estate)
└── Containers: top-level blocks / aggregates
    └── Subnets / prefixes (individually named, sized, and scoped records)
        └── Address entries (each host address, held as its own record)
```

Every record carries attributes: the network and mask; an **allocation state** (free, in use, reserved, and similar product-specific states); a **holder** (hostname, device, tenant, requester); and context — site or section, VLAN or routing-table placement, purpose or role, often a DNS name. Because the geometry is CIDR, the records carry real arithmetic: a subnet knows its parent, its children, its usable range, and its size; containment, overlap, and free space are computable properties of the record, not manual judgment calls.

**2. The allocation lifecycle.** The record is not a static map — it is the ledger through which space is consumed and released:

```text
Plan the space        (import or declare top-level blocks)
→ Divide              (create child subnets; split or resize existing ones)
→ Allocate / reserve  (assign addresses or ranges to holders; reserve for future use)
→ Track               (state and holder maintained on every entry)
→ Find free           (first-free address, free subnet of a requested size)
→ Reclaim             (release, delete, or re-mark unused allocations)
→ Report              (utilization, history, depletion planning)
```

Both structures are load-bearing. Keep the record but drop the lifecycle — allowing only viewing and reporting — and the product becomes a network map or inventory viewer, not management. Keep a lifecycle but drop the address-shaped record — no CIDR structure, no containment math, no address identity — and it is a generic asset or booking tool. The two together are the Type.

### What Mature Products Add

Standard capabilities that current products commonly carry, on top of the defining core:

- **Space organization layer** — groupings above subnets (sections, sites, regions, locations) used to structure large estates and scope permissions.
- **Named state vocabulary** — explicit statuses and roles on addresses and subnets (for example: in use, reserved, free, abandoned; functional roles such as loopback or virtual IP). Exact state names vary by product.
- **Free-space and capacity machinery** — find the next free address; find a free subnet of a requested size; utilization percentages, thresholds, and depletion alerts.
- **Reconciliation against the live network** — automated scanning, ping checks, or infrastructure discovery that compares the record with reality. Posture varies: some products make continuous discovery central, while source-of-truth-oriented products center on documenting the intended network rather than live scanning.
- **IP ↔ DNS name linkage** — a DNS name held as an address attribute; in some products, creating or deleting an address creates or removes the corresponding DNS record. Operating DNS itself belongs to a different Type (see Related Application Types).
- **DHCP visibility** — pool and lease data feeding the address picture; in products that bundle service management, DHCP servers and scopes are operated from the same console. Pure IPAM products lack this entirely.
- **Context overlays** — VLAN association, VRF / routing-table separation (allowing the same address range to exist in several contexts), NAT relationships, device or virtual-machine interface binding, tenancy.
- **Governance** — permission scoping down to section and subnet; authentication against directory systems; in some products, request/approval workflows for allocations.
- **Search and reporting** — estate-wide search by address, hostname, or MAC; utilization history and audit trails.
- **IPv4 and IPv6 dual-stack** throughout the data model.
- **API surface** — the same objects and operations exposed for automation.

### One Structure, Many Implementations

The core is written in conceptual terms; implementations differ on posture:

```text
Concept:            the record of the space
Posture A:          planned / documented — the record is the authoritative intent,
                    maintained by hand or through integrations (source-of-truth style)
Posture B:          discovered / reconciled — the record is continuously compared
                    against the live network by scanning or discovery
(Many products combine both: a planned ledger with optional or scheduled checks.)
```

A reader who has only seen a scanning-driven product should still be able to recognize a documentation-first product as the same Type from the core model — and vice versa.

## How It Works

### Set up the estate

```text
Declare or import the top-level space
  (entered directly; in many products imported from upstream registry
   delegations or from existing spreadsheets; or discovered from infrastructure)
→ organize it: sections / sites / locations; routing contexts (VRFs)
→ define the first subnets
```

### The allocation loop (the defining workflow)

```text
Pick a container
→ find free space (next free address, or a free subnet of the requested size)
→ allocate or reserve it: record the holder, purpose, and state
→ the entry now counts as consumed; parents' utilization updates
→ later: release or reclaim it, and the space becomes free again
```

Everything the Type is for concentrates here: division of space (creating child subnets; in many products also splitting or resizing existing ones), consumption (assignment and reservation), and recovery (reclaiming abandoned allocations before depletion). In products with allocation request workflows, this loop is wrapped in a request → approve → apply cycle instead of direct entry.

### Keep the record true to reality

Two postures, often combined:

- **Reconcile down**: the product probes the network — subnet scans, address status checks, infrastructure discovery — and marks addresses it finds alive, surfacing discrepancies between the record and what answers on the wire, including address conflicts where detected.
- **Document up**: the product is the intended state that automation deploys from; keeping the record current is a matter of process and integrations rather than scanning.

Record-versus-reality drift is the endemic failure mode of the discipline, and products differ mainly in how much of the fight they automate.

### Answer questions and report

The standing interaction loop is query-shaped: search for an address or hostname, inspect a subnet's address table with free space visible, read utilization over time, export reports. In the scanning-led posture this loop extends to alerting on conflicts and depleted scopes.

### Core vs standard vs optional

**Defining core** — without these, not an IPAM:

- the address space held as CIDR-structured records (containers and addressable entries)
- allocation state and holder attributes on the records
- the allocation lifecycle: divide, allocate/reserve, track, find free, reclaim
- authoritative answers from the record: what is free, what is taken, who holds it, how full is this subnet

**Standard capabilities** — present in most mature products:

- space-organization layer (sections/sites), named states and roles, free-space and utilization machinery, IP↔DNS name linkage, VLAN/VRF/NAT/device overlays, permission scoping, search and reporting, IPv6 dual-stack, API

**Optional / variant** — depends on posture, segment, and packaging:

- continuous network scanning and conflict alerting; DHCP pool/lease visibility; DNS record write-back; request/approval workflows; automated subnet delivery to customers; bundled DCIM (racks/devices); cloud-environment scope; bundling with DNS/DHCP service management (the "DDI" package)

## Interfaces

Described in conceptual terms; exact layouts and names vary by product.

### Subnet / space explorer

The primary navigation surface.

- presents the space as a navigable hierarchy (blocks → subnets, grouped by section/site)
- surfaces utilization at every level
- primary actions: create or navigate to subnets, drill down, add child space

### Subnet detail

The workhorse surface for one subnet.

- the address table: every address in the range with its state, holder, and attributes; free space visually distinguished
- primary actions: allocate or reserve an address (often "next free"), edit entries, add child subnets (in some products, split or resize the subnet itself), view usage

### Address detail

One address as an individually addressable record.

- state, holder (hostname/device/tenant), purpose, DNS name, context (VLAN/VRF), history where kept
- primary actions: edit, reassign, release, ping/check status in products with scanning

### Search

A real surface because the ledger is the estate's memory: lookup by address, hostname, MAC, or free-space query across the whole database.

### Reports / utilization

- utilization over time per subnet or container, thresholds, depletion forecasts, audit/change history
- primary actions: run, filter, export

### Administration

- sections/sites and grouping, permission scoping per group or role, discovery/scan job configuration in scanning-led products, API credential management

## Important Rules / Behaviors

### Every address counts against the hierarchy

Allocation state is computed within CIDR containment: a child subnet consumes its parent's space; utilization, free space, and overlap are consequences of the tree structure. Products therefore enforce or at least surface structural facts — a subnet cannot meaningfully exceed its parent, overlaps are detectable, and the "same" range can coexist only when explicitly separated into different routing contexts.

### Allocation state is explicit and user-visible

The distinction between free, reserved, in-use, and abandoned is a first-class part of every record, not a footnote. Reservations differ from assignments (space held for the future versus space with a holder), and both differ from free. Exact state names vary by product.

### The record is authoritative — but its truthfulness is a posture

In the documentation-first posture, the record is the intent and wins by definition. In the scanning-led posture, the record is continuously corrected against the network. Either way, the record — not ad-hoc live queries — is the basis for allocation decisions; drift between record and reality is treated as a condition to be fought (scans, checks, audits), not ignored.

### Uniqueness is per context

An address is unique within its routing context (VRF / table). Products that support multiple contexts can hold the same address range several times; products that do not, cannot. Uniqueness enforcement within a context is what prevents the classic duplicate-address failure.

### Space is reclaimed, not just consumed

The lifecycle is deliberately closed: releasing, deleting, or re-marking entries is as much a part of the model as allocation, because finite space runs out. Depletion planning — knowing how soon a subnet or scope will be exhausted — is the reporting consequence of this rule.

### Couplings exist but are not the ledger

DNS names and DHCP pool data commonly attach to addresses, and some products write DNS records or read leases as part of address operations. The ledger, however, remains complete without any of these couplings — a product can be a fully functional IPAM while never operating a DNS or DHCP service.

## Variants

Common product shapes and deployments:

- **pure standalone IPAM** — the ledger and lifecycle with overlays; no DNS/DHCP service operation at all (common in open-source and self-hosted deployments)
- **network source-of-truth platform** — IPAM embedded in a broader curated network model alongside data-center inventory; documentation-first posture, built to feed automation
- **monitoring-suite module** — commercial IPAM sold as part of a network-management suite, with continuous scanning, conflict alerting, and bundled DHCP/DNS management
- **enterprise DDI suite** — IPAM as one leg of a fused DNS/DHCP/IPAM platform, typically cloud-managed with serving infrastructure included
- **OS-native feature** — address management provided as a central feature of a server operating system over its own network services
- **cloud-provider-native address management** — address-space management scoped to one provider's virtual networks
- **service-provider / MSP variants** — multi-tenant segmentation, overlapping address space per customer, automated range delivery
- **IPv6-heavy estates** — dual-stack is standard; some deployments are IPv6-dominant in practice

A variant remains a variant as long as the defining core — the space as record plus the allocation lifecycle — still describes it.

## Related Application Types

| Application Type | Distinction |
|---|---|
| DNS & DHCP Management | operates the *services* (resolution, lease assignment) — zones, records, scopes, servers; IPAM holds the *address ledger*. Market products fuse them ("DDI"), but the seam holds in both directions: a pure IPAM without service operation exists, and service management without the address ledger exists |
| Network Management | manages devices, interfaces, and their configuration; the address ledger is not its subject |
| Network Monitoring | observes live health and performance and alerts; holds no allocation record. Scanning-led IPAM borrows monitoring's techniques, but its output is ledger state, not health state |
| CMDB | holds generic configuration items and typed relationships; IPAM holds IP-space-specific structure (CIDR math, containment, allocation state) and commonly feeds the CMDB as a population source |
| Data Center Infrastructure Management (DCIM) | models the physical layer (racks, power, cabling); IPAM models the logical address layer. Some platforms ship both as distinct model families |
| IT Asset Management | tracks the financial and contractual lifecycle of assets; IPAM tracks an operational network resource |
| Cloud Management Platform | controls cloud estates (provisioning, lifecycle, cost); IPAM is the address-space discipline that cloud address management feeds into or aligns with |

The boundary with DNS & DHCP Management is the most important one, because the market overwhelmingly packages the two (plus DHCP) together. The structural test: if a product can no longer configure or operate DNS and DHCP services, what remains — planning, allocating, tracking, and reporting on address space — is still fully IPAM; if the address ledger is removed, what remains is still service management.

## Representative Products

- phpIPAM — open-source, self-hosted, pure standalone IPAM
- NetBox — open-source network source-of-truth platform (IPAM + DCIM), documentation-first posture
- SolarWinds IP Address Manager — commercial standalone IPAM module, scanning-led, DDI-bundled
- Infoblox (Universal DDI) — enterprise cloud-managed DDI suite with IPAM as one leg
- Microsoft Windows Server IPAM — platform-native OS feature (the historical / platform-native check)

## Sources

Research date: **2026-09-08**

- phpIPAM — home page, feature list, API reference: https://phpipam.net/ , https://phpipam.net/documents/features/ , https://phpipam.net/api/api_reference/
- NetBox — documentation root and IPAM model pages (prefix, IP address): https://docs.netbox.dev/en/stable/ , https://docs.netbox.dev/en/stable/models/ipam/
- Microsoft Learn — IP Address Management (IPAM), Manage IPAM: https://learn.microsoft.com/en-us/windows-server/networking/technologies/ipam/ipam-top , https://learn.microsoft.com/en-us/windows-server/networking/technologies/ipam/manage-ipam
- SolarWinds — IP Address Manager product page: https://www.solarwinds.com/ip-address-manager
- Infoblox — Documentation Portal, Universal DDI Management: https://docs.infoblox.com/ , https://docs.infoblox.com/space/BloxOneDDI/186614365/Infoblox+Universal+DDI+Management

> Sourcing limitations: the SolarWinds administrator-guide body was not served to the research environment (navigation shell only), so that product's evidence is limited to its product page. The Infoblox IPAM module's object-level detail was not directly reachable; its evidence rests on suite-level documentation. Enterprise vendors BlueCat and EfficientIP were unreachable in the sibling research pass and were not re-attempted. Accordingly, no precise numeric limits, scan intervals, or plan-gated defaults are stated in this document; posture- and packaging-dependent findings are marked as common or optional rather than defining.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical / market-sample breadth check are recorded in the paired Research Notes.
