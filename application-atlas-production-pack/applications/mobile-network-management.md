# Mobile Network Management

## Overview

A **Mobile Network Management** system is the mobile operator's run-time operations system for its deployed cellular network. It holds the live network's elements — above all the radio base stations and their cells — as a managed estate, and operates that estate through a joint loop of configuration, fault, and performance management.

The defining structure is small:

```text
The operator's live mobile network
    held as a managed estate of network elements
        ├── Configuration management — read and write operational parameters and software
        ├── Fault management — network problems surfaced as alarms, worked to resolution
        └── Performance management — operational measurements collected and analyzed
```

Everything else commonly associated with the category — self-organizing-network (SON) automation, zero-touch site onboarding, AI-assisted alarm correlation, energy management, network-slice control, cloud-native packaging — is widespread in current products but is not part of the defining core. Operations-and-maintenance centers from earlier network generations satisfy the same definition with none of it.

The boundary drifts are equally clear: a system that only watches service-level quality, without the authority to change network elements, has become a service-assurance tool; one that models a network that does not yet exist is a planning or design tool; one that spans the operator's entire fulfillment-and-assurance estate is the Telecom OSS umbrella rather than this domain slice of it.

## Users & Context

Primary users work in the operator's network operations organization:

- **NOC / operations staff** — watch the estate, triage alarms, keep the network healthy shift by shift
- **RAN / O&M engineers** — configure elements, run parameter changes and software upgrades, investigate quality problems
- **Rollout and integration teams** — bring new sites and cells into the managed estate
- **Vendor support and managed-services teams** — operate or assist with their vendor's equipment inside the operator's estate

The work context is defined by scale and heterogeneity: a nationwide operator's network comprises very large numbers of sites and cells across multiple technology generations, frequently from several suppliers. Manual per-element operation does not scale, which is why fleet-level operations — bulk changes, automation, closed-loop optimization — are structural to the category rather than premium extras. The same core also serves much smaller estates: enterprise and campus networks and rural operators are served by small-footprint packaging of the same structures.

## Core Model

### The Defining Core

Four properties. If any one is removed, the product is no longer recognizable as mobile network management:

- **The live mobile network as managed estate** — the operator's deployed network elements (chiefly radio base stations and their cells/sectors; scope may extend to controller, core, and transport nodes) are held as managed records: identity, hardware and software state, operational parameters. Without this, the product is a design-time tool modeling a network that does not exist, or a single-element local shell.
- **Configuration management of the elements** — the system reads and writes operational parameters and software on network elements, individually and at fleet scale (bulk changes with verification). Without this, the system can observe the network but not operate it.
- **Fault management** — problems the network detects are surfaced as alarms and events that are tracked and worked to resolution. Without this, operations has no incident surface.
- **Performance management** — operational measurements (accessibility, dropped-call and handover behavior, throughput, coverage, capacity) are collected from the network and made analyzable. Without this, there is no quality basis for operating and optimizing the estate.

Together the three operating legs are the classical operations-and-maintenance triad — configure, fault, perform — realized against a mobile network's object world. The Type typically sits at the management-system layer: above individual element managers, inside or beneath the operator's wider OSS estate.

### Standard Capabilities

Mature products commonly add:

- **Software and firmware management** — versioned software packages for network elements, upgrade campaigns across the fleet
- **Multi-technology and multi-vendor reach** — one management system addressing several radio generations (2G through 5G) and equipment from several suppliers
- **Zero-touch site integration** — new sites and cells power up, are discovered, and are configured into service with minimal manual steps; hardware and software inventory maintained automatically
- **SON-style optimization loops** — automatic neighbor relations, load balancing and traffic steering, coverage-and-capacity optimization, mobility robustness, interference coordination; self-healing behaviors such as neighbor-cell coverage compensation for a failed cell
- **KPI dashboards, reports, and analytics** — the quality picture that drives optimization
- **Bulk operations with verification** — mass parameter changes applied and checked across the fleet
- **Open interfaces** — REST APIs, CLI, workflow automation; integration with element managers below and upper-level management systems above
- **Energy monitoring and management** — consumption visibility and, in some products, automated energy-saving behavior
- **AI-assisted operations** — alarm correlation, anomaly detection, recommendations

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:            Managed estate scope
Implementations:    RAN-only management ↔ multi-domain (radio + core + transport)

Concept:            Vendor posture
Implementations:    vendor-native network manager (own equipment + third-party integration)
                    ↔ Open RAN-native multi-vendor orchestration

Concept:            Automation style
Implementations:    separate SON solution ↔ integrated SON module ↔ RIC/xApp/rApp frameworks

Concept:            Deployment and scale
Implementations:    on-premises nationwide NMS ↔ cloud-native platform ↔ small-footprint campus/enterprise packaging
```

A reader who encounters only one implementation — say a single-vendor nationwide network manager — should still be able to recognize a cloud-native Open RAN orchestration product, or a campus-scale management package, from the same core.

## How It Works

### The operations loop

```text
Network elements report alarms and counters
→ operations staff (or automation) triage and correlate
→ diagnose against the element's configuration and performance context
→ act: change a parameter, restart or re-provision an element, compensate coverage
→ verify: alarm clears, KPIs recover
→ record the resolution
```

This loop runs continuously; it is the day-to-day life of the system.

### The change loop

```text
Prepare a configuration change (single element or bulk across the fleet)
→ apply it to the live network
→ verify the result (element state, KPI behavior)
→ confirm, or roll back to the previous working state
```

Verification is a first-class step, not an afterthought: products expose explicit mass-change verification, and closed-loop automation reverts to the last working state when network degradation follows a change.

### The site-integration loop

```text
New site powers up / cell added
→ system discovers the new element
→ initial configuration computed (cell identity and access parameters, neighbor relations, transmit power)
→ element onboarded into the managed estate, inventory updated
→ cell in service
```

### The software-upgrade loop

```text
New software/firmware version prepared
→ upgrade campaign planned across the element fleet
→ executed in controlled waves
→ element software state updated in the estate records
```

### The optimization loop

```text
KPIs observed (drop rate, handover success, throughput, coverage, load)
→ optimization policies or SON functions decide adjustments
→ parameter changes applied automatically
→ network feedback watched; degradation triggers reversion
```

### Capability tiers

**Defining core** — without these, not mobile network management:

- live network as managed estate
- configuration management of the elements
- fault management (alarms)
- performance management (counters/KPIs)

**Standard capabilities** — present in most mature products:

- software/firmware management and upgrade campaigns
- multi-technology, multi-vendor reach
- zero-touch site integration and automatic inventory
- SON optimization loops and self-healing
- KPI dashboards, reports, analytics
- bulk operations with verification
- open APIs, CLI, workflow automation
- integration with element managers and upper OSS
- energy monitoring
- AI-assisted alarm correlation

**Variant or optional** — depends on product, scale, and era:

- estate scope: RAN-only vs radio + core + transport
- vendor posture: vendor-native vs Open RAN multi-vendor orchestration
- deployment: on-premises vs cloud-native; nationwide vs campus/enterprise packaging
- network-slice management (radio slicing configuration and performance automation) — present in some products
- automation-ecosystem machinery: RIC frameworks, rApp marketplaces, intent-based orchestration
- energy-management depth: monitoring/reporting vs automated energy saving

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Network topology / element views

The estate picture: network elements organized by region, technology, or hierarchy, with operational state per element.

- typical information: element identity, site/location, technology, software version, operational state
- primary actions: open an element's detail, filter and group the estate, launch element operations

### Alarm / event console

The incident surface.

- typical information: active alarms with severity, affected element/cell, time raised, correlation groupings
- primary actions: acknowledge, annotate, assign, investigate the affected element, track to clear

### Performance dashboards and reports

The quality surface.

- typical information: KPIs per cell/site/region — accessibility, retainability, handover success, throughput, utilization, coverage
- primary actions: analyze trends, compare regions or technologies, drill from a KPI degradation to the affected elements

### Configuration management surfaces

Where the network is actually changed.

- typical information: parameter sets per element/cell, planned vs applied values, change history
- primary actions: edit parameters, compose bulk changes, apply with verification, roll back

### Software management views

- typical information: software versions per element, campaign status
- primary actions: plan and execute upgrades, track progress

### Automation / policy surfaces

Where optimization behavior is configured.

- typical information: SON function status, policy thresholds, automation activity logs
- primary actions: enable/disable functions, tune thresholds, review automated changes

### Open interfaces

REST APIs, CLI, and workflow automation are standard integration surfaces — management systems are operated programmatically as much as through screens, and they integrate upward into the operator's OSS estate.

## Important Rules / Behaviors

### The system can change the live network

This is the defining authority. Monitoring and analytics without write access to network elements is a different kind of product; the ability — and the operational discipline — to change parameters, software, and element state is what makes this a management system.

### Changes are verified, and automation reverts

Bulk changes are checked after application; closed-loop automation takes network feedback into account and reverts to the last working state when degradation follows a change. Operating a live network at fleet scale without verification and rollback is not a viable pattern, and mature products treat it structurally.

### Alarms are worked, not just displayed

Alarms exist to be driven to resolution — acknowledged, diagnosed against configuration and performance context, remediated (manually or by self-healing behaviors), and cleared. Per-alarm state conventions vary by product; the work-to-resolution discipline is the constant.

### The management hierarchy is real

Element managers sit below (vendor- or device-specific management of individual equipment), upper-level management and OSS systems sit above. A mobile network management system commonly integrates both ways: it aggregates element managers and third-party elements, and it exposes its data and operations upward.

### Scale forces automation

Large operator networks exceed manual per-element operation by orders of magnitude. Fleet-level operations — bulk changes, automatic neighbor relations, zero-touch onboarding, closed-loop optimization — are structural responses to scale, not add-ons.

### Multi-vendor, multi-technology is the normal estate

Operators run mixed estates across technology generations and suppliers. A management system built around a single vendor's equipment is one pole; multi-vendor reach is the market's center of gravity and the reason open interfaces are standard.

## Variants

- **Vendor-native nationwide network manager** — one vendor's management system for its own equipment estate, integrating third-party elements and upper OSS; the classical form
- **Open RAN multi-vendor orchestration** — management software born for disaggregated, multi-supplier radio networks; orchestration and RIC-style automation frameworks in front
- **Campus / enterprise small-footprint management** — the same core packaged for enterprise and campus networks, software-only, on generic hardware
- **RAN-only vs multi-domain scope** — some products manage only the radio access network; others span radio, core, and transport
- **On-premises vs cloud-native deployment** — the classical NMS form vs cloud-native platforms
- **SON as separate product vs integrated module** — the same optimization capability packaged differently

A variant remains a variant unless it changes the core object world: a product that stops managing network elements (service-level monitoring only, or design-time only) has left the Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Telecom OSS | the umbrella: the operator's whole network-operations estate (fulfillment + assurance + inventory + workforce); this Type is the mobile-domain network-management slice within it |
| Telecom Service Assurance | monitors service-level quality and detects degradation across services; this Type operates the network elements themselves — the seam is the authority to change the network |
| Telecom Provisioning Platform | activates individual services on the network, order-driven; this Type continuously operates the network itself, always-on |
| Telecom Network Planning / Design | design-time: models a not-yet-built network and produces candidate designs; this Type operates the live estate — live data flows into planning, live-network operation stays here |
| Fiber Network Management | fixed fiber plant of record (cables, strands, splices, ports) vs radio network elements; complementary domain-specific management systems |
| Network Management (enterprise IT) | shared vocabulary, different object world: enterprise/campus IT device estates vs carrier mobile network elements |
| Tower Management Platform | passive site infrastructure (towers, space, leases) vs active radio equipment and its radio function |
| SIM / eSIM Management, Subscriber Management | subscriber and credential records (commercial side) vs network-side element operations |
| Telecom Network Inventory | the estate leg exists inside this Type as managed records; standalone inventory products are broader multi-domain records without the operate loop |

The most important boundary is with Telecom Service Assurance, because both watch the network. The structural difference: assurance detects and diagnoses degradation of services; mobile network management holds the authority and the tools to change the network — configuration, software, element state — and is judged by the network's resulting behavior.

## Representative Products

- Nokia MantaRay family (MantaRay NM network manager, MantaRay SON, MantaRay SMO) — vendor-native network manager pole, nationwide multi-technology scale
- Parallel Wireless Open RAN network software (Open RAN Controller, Real-time ALL G SON) — disaggregated Open RAN multi-vendor pole

Other major vendors in this category (Ericsson, Huawei, ZTE) are certainly market representatives, but their operational documentation could not be reached during research; no product-level claims about them are made here.

## Sources

Research date: **2026-09-09** (official pages fetched); document finalized 2026-09-10.

- Nokia MantaRay NM — https://networks.nokia.com/products/netact
- Nokia MantaRay SON — https://www.nokia.com/mobile-networks/ran-operations/network-management-son/
- Nokia MantaRay SMO — https://www.nokia.com/mobile-networks/ran-operations/mantaray-smo/
- Parallel Wireless Open RAN Network Software — https://www.parallelwireless.com/products/openran-network-software/
- Parallel Wireless Real-time ALL G SON — https://www.parallelwireless.com/products/real-time-all-g-son/

> Sourcing limitation: Ericsson Network Manager, Huawei carrier network management, and ZTE NetNumen could not be reached from the research environment (unreachable or timed-out official URLs); Parallel Wireless's documentation portal was also unreachable, so its evidence comes from official product pages only. Per-alarm state conventions (raise/acknowledge/clear) were not directly documented on any fetched page, so alarm handling is described conceptually. Precise operational details (numeric limits, exact parameter names, product-specific defaults) are intentionally not stated; they remain in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical / market-sample check are recorded in the paired Research Notes.
