# Cyber Asset Management

## Overview

A **Cyber Asset Management** application maintains a continuously refreshed, deduplicated inventory of an organization's technology assets — devices, cloud resources, identities, software, services, certificates — and turns that population into answers for security decisions: what exists, what is exposed, what is unprotected, and what matters most.

Its defining core is small:

```text
Cyber-asset population (one record per real asset)
└── assembled automatically from the environment
    └── kept continuously current
        └── shaped for security decisions
```

Everything else commonly associated with the category — adapter catalogs, discovery sensors, risk scoring, relationship graphs, compliance mappings, ticketing flows — is widespread in mature products but is not what makes the product a Cyber Asset Management application. Older, simpler network-inventory scanners satisfy the same core without any of those specifics.

The category answers a question no other security tool asks about itself: *can we even see everything we are responsible for protecting?* When the population is reduced to internet-facing exposure only, the product drifts toward Attack Surface Management; when findings rather than assets become the primary object, it drifts toward Vulnerability Management; when the orientation becomes financial lifecycle rather than security, it becomes IT Asset Management.

## Users & Context

The primary user is a security practitioner responsible for knowing and protecting the organization's estate:

- **Asset / exposure owners** — maintain the completeness of the inventory, investigate gaps, assign ownership and criticality.
- **SecOps analysts** — interrogate the population during triage and incident response ("which systems run this service?", "what is reachable from this segment?", "which assets have no endpoint protection?").
- **Security architects / CISO** — use coverage, exposure, and criticality views to steer the program.

Secondary users:

- **IT operations** — the same asset data serves daily operations; several products explicitly position the inventory as the shared source where IT and security meet.
- **Compliance and audit** — the population is the evidence base for control coverage and framework reporting (an auditor's "show me everything connected" question).
- **Managed service providers** — run the same inventory across many client environments.

The work context is continuous: the estate changes daily (new devices, cloud resources, SaaS adoption, decommissions), so the application runs as an always-on background process with periodic human attention, not as a session-based tool.

## Core Model

### The Defining Core

Four properties. If any one is removed, the product is no longer recognizable as Cyber Asset Management:

- **A standing cyber-asset population** — a persistent set of records, one per identified asset of the organization's estate, spanning more than one asset class. A single list of laptops is an inventory; the type is defined by breadth across the technology estate.
- **Environment-derived assembly** — records are created and refreshed automatically from data observed in or ingested from the environment (network observation, API connections, endpoint agents). The system, not a person, keeps the population current. A hand-maintained register is not this application.
- **Asset identity resolution** — multiple observations and multiple sources converge on one record per real asset. The same server seen by a network scan, a cloud API, and an endpoint agent is one asset, not three.
- **Security-decision orientation** — the population and its attribute vocabulary exist to answer security questions and feed security workflows: coverage gaps, exposure, criticality, ownership, response, compliance evidence.

### The Asset Record

The central object is the asset record. Across the researched sample it consistently carries several kinds of information:

- **Identity attributes** — hostnames, addresses (IP/MAC), hardware identifiers, vendor/model/OS. These are the keys by which an asset is recognized again.
- **Classification** — what kind of thing it is: device type and category (traditional IT, operational technology, IoT), and in graph-shaped products a formal class layer over source-specific types.
- **Location and network context** — site, segment, addresses observed, in some products route/segmentation context.
- **Exposure context** — services and software observed running, vulnerabilities and security findings attached to the asset, certificates.
- **Control coverage** — which security tools report on the asset (endpoint agents, vulnerability scanners, management systems) — and, critically, which do not.
- **Ownership and business context** — owner, business unit, location, criticality to the organization.
- **Lifecycle** — first seen, last seen, current alive/offline state, decommission markers.

### Asset Classes

The population is deliberately broad. Common classes across the sample:

- networked devices (servers, workstations, network gear, virtualization hosts)
- cloud resources (instances, storage, managed services, containers)
- identities (user accounts, service/non-human accounts, directories)
- software and services (installed software, running services, SaaS applications)
- security-relevant adjuncts (vulnerabilities/findings, certificates, wireless networks)
- operational technology and connected devices (PLCs, sensors, cameras, medical devices)

### Sources and Normalization

The population is assembled from two complementary kinds of sources:

- **Observation of the environment** — active network scanning, passive traffic listening, endpoint agents. Observation finds what nobody logged, including unmanaged and shadow assets.
- **Ingestion from existing systems** — API connections to endpoint protection, vulnerability scanners, cloud providers, directories, MDM, CMDBs, and external exposure data. Ingestion adds depth and context for assets already known to those tools.

Data from every source is normalized into a common attribute vocabulary — the same field means the same thing regardless of which tool reported it (severity labels are a typical normalization target).

### One Structure, Many Implementations

The core model is conceptual. Products realize it differently:

```text
Concept:            Environment-derived assembly
Implementations:    adapter/API ingestion, active scanning, passive listening, endpoint agents

Concept:            Asset identity resolution
Implementations:    correlation across scans (multi-attribute), merge on stable
                    hardware identifiers (MAC/serial/hostname), entity keying in a graph

Concept:            Security-decision orientation
Implementations:    agent-coverage views, vulnerability enrichment, risk/criticality
                    models, control-coverage queries, compliance framework mapping
```

A reader who has only seen one implementation (say, an aggregation platform) should still recognize a discovery-scanner product as the same application type.

## How It Works

The application runs a continuous loop:

### 1. Connect sources / deploy collectors

The operator connects API integrations to existing security and IT tools and/or deploys collection points — network scanners, passive listeners, endpoint agents, cloud connections. Collection points are typically placed per network segment or site; cloud connections are credential-based.

### 2. Observe and ingest

Collectors observe the environment (probing hosts, listening to traffic, querying cloud APIs) and integrations pull records from connected tools. Observation discovers assets nobody registered; ingestion enriches assets other tools already track.

### 3. Normalize and merge into one record per asset

Incoming data is mapped to the common schema, then correlated with the existing population. Matching uses stable identifiers — hardware addresses, serial numbers, hostnames — rather than volatile ones like IP address, so an asset that changes address remains the same asset. When sources disagree, the record keeps the contributing sources visible rather than silently overwriting.

### 4. Enrich

Each record gains security context: attached vulnerabilities and findings, which protection/management tools cover it, business ownership, criticality, computed risk. Some enrichment is automatic (risk inferred from findings); some is human-assigned (criticality, ownership).

### 5. Interrogate

Users query the population — ad hoc questions and saved queries — and read dashboards and reports. Typical questions:

- What exists in this segment / cloud account / site?
- Which assets have no endpoint protection, no vulnerability scanning, no management agent?
- Which assets are exposed (running a risky service, holding a vulnerable version, internet-reachable)?
- Which assets are critical — and what is true about them?

### 6. Act

Answers flow outward: tickets created in ITSM systems, alerts raised on inventory changes (a new device appearing, a critical asset going offline), exports to SIEM and data platforms, records synced to CMDBs. In several products the application can also trigger enrichment or remediation workflows directly.

### 7. Refresh continuously

The loop repeats on schedules. Assets not seen again are marked offline rather than deleted immediately; new observations create or update records. The inventory is never "done" — currency is the product.

### Capability Tiers

**Defining core** — without these, not Cyber Asset Management:

- standing multi-class asset population
- automatic environment-derived assembly and refresh
- identity resolution into one record per asset
- security-oriented attributes and interrogation

**Standard capabilities in mature products:**

- multi-source ingestion (endpoint, vulnerability, cloud, identity, CMDB, external data)
- active and/or passive discovery; optional agents for off-network endpoints
- vulnerability/finding enrichment and risk scoring
- control-coverage analysis (agent/scanner/management gaps)
- query language or builder with saved queries and libraries
- dashboards, reports, export
- ownership, criticality, and business-context assignment
- alerts/rules on inventory change
- outbound flow to tickets, SIEM, CMDB/ITSM
- compliance framework mapping
- relationship/topology visualization
- role-based access, SSO, audit trails

**Optional / variant:**

- OT/IoT/medical-device specialization
- external attack-surface data inclusion
- exposure-management depth (SLA tracking, exception workflows, remediation ownership)
- continuous controls monitoring / compliance automation depth
- multi-tenant structures for service providers
- natural-language/AI assistance over the population

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Asset inventory (list)

The primary surface: a filterable, queryable table of all asset records.

- typical information: name/hostname, addresses, type/category, OS, site/location, last seen, criticality, coverage indicators
- primary actions: search/filter, open asset detail, bulk select and modify (criticality, ownership, tags), export

### Asset detail

The full record for one asset.

- typical information: all identity attributes, every contributing source and when it reported, attached findings/vulnerabilities, coverage by security tools, relationships (network, owner, installed software), lifecycle timestamps
- primary actions: edit ownership/criticality/tags, trace relationships, open in source tool, create ticket

### Query surface

A query builder or query language over the normalized schema, with saved queries and shared query libraries. This is the analytical heart: coverage-gap questions, exposure questions, and report definitions are all queries. In several products, dashboards, reports, and automations are all built on saved queries.

### Dashboards and reports

Aggregated views: population composition, coverage posture, risk distribution, changes over time. Specialized reports commonly include coverage reports (how much of the address space is actually seen), risk reports (grouped by criticality), and external-exposure reports.

### Graph / topology views

Visual surfaces over relationships: asset connection graphs, network maps, segment/segmentation views, traffic-derived dependency views. Depth varies widely — from a network map to a fully typed relationship graph.

### Integration / collector configuration

The setup surface: connecting API integrations (credentials, scopes, fetch schedules), deploying and monitoring collectors/sensors, managing scan templates and discovery scopes.

### Automation and alerting

Rule surfaces that watch the population: alert when a query matches (new device appears, critical asset changes), automatic actions (assign criticality, create ticket, notify, export).

### Administration

Users and roles, site/organization hierarchy, licenses (asset count is the common commercial unit), data retention.

## Important Rules / Behaviors

### One record per real asset, keyed on stable identity

The inventory's correctness rests on identity resolution. Merge keys are stable identifiers — hardware addresses, serial numbers, hostnames — rather than volatile ones such as IP addresses, which change. A device that moves or changes address must remain the same record. Products differ in strictness: some scope correlation to a site or segment, treating the same physical system seen from different scopes as separate records by design.

### Absence is a state, not a deletion

An asset not seen again is typically marked offline / inactive rather than deleted, retaining its history; reappearance restores it. Substantial identity change (new network adapter, reimaged system) may legitimately produce a new record, with the old one left offline; products expect some manual cleanup and provide it.

### Risk is inferred; criticality is assigned

A recurring pattern: **risk** is computed from evidence attached to the asset (vulnerabilities, risky configurations), while **criticality** is a human judgment about the asset's importance to the organization. The two are deliberately separate — a low-risk asset can be business-critical, and a high-risk asset may be disposable. Automation can apply criticality by rule, but the value originates in human intent.

### Sources are preserved, not silently merged

When multiple tools report on the same asset, the record keeps every contributing source and when it reported. Conflicting values are a first-class display concern, because "which tool is right?" is itself a security question.

### Coverage honesty is a feature

The application reports what it has *not* seen: address ranges with no visibility, assets with no agent from any security tool, segments outside scan scope. An inventory that only lists what it found, without measuring its own blind spots, fails the type's core promise.

### Suppression exists for known noise

Repeatedly observed but understood artifacts (known lab devices, expected duplicates) can be suppressed from views and alerts without deleting the underlying record.

### The population is the organizing quantity

The asset population is the number the whole product is organized around: commercial plans are typically sized to the environment rather than to seats, and retention policies and query performance are sized against population scale.

## Variants

Common shapes of the same application:

- **Aggregation-first platforms** — build the population by normalizing and correlating data fetched from the organization's existing security and IT tools; strongest where many tools already exist; typically SaaS, enterprise-oriented.
- **Discovery-first scanners** — build the population by actively probing and passively observing networks, with API ingestion as enrichment; strongest where unmanaged/OT assets and unknown blind spots dominate; available as SaaS or self-hosted.
- **Sensor-based deep-inventory platforms** — combine network sensors (IT, OT, traffic) with optional agents and cloud connections; long heritage in IT inventory, now security-positioned; span SMB to enterprise.
- **Graph-first platforms** — model the estate as a typed entity-relationship graph with a dedicated query language; strongest for relationship questions (what reaches what), compliance/controls mapping, and cloud-native estates.
- **Scope specializations** — OT/ICS-focused, medical-device (IoMT)-focused, identity-focused, SaaS-focused, or external-exposure-extended deployments of the same core.
- **Deployment variants** — SaaS vs self-hosted; sensor placement models; agentless vs agent-assisted postures.
- **Service-provider variants** — multi-tenant structures for MSSPs running the inventory across client environments.

A variant remains a variant while the defining core applies. When a product's primary object stops being the asset population — findings-first (vulnerability management), outside-in-first (attack surface management), finance-first (ITAM) — it has become a different application type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| IT Asset Management | sibling (same object, different orientation) | ITAM serves procurement, financial, and lifecycle decisions (contracts, licenses, cost, refresh); CAM serves security decisions (exposure, coverage, criticality). Products straddling both exist. |
| CMDB | adjacent, mutually feeding | CMDB maintains curated configuration items in service of IT service management (services, change); CAM's population is auto-derived from the environment and security-shaped. CAM products commonly ingest from and sync to CMDBs. |
| Attack Surface Management | adjacent, opposite vantage | ASM discovers internet-facing exposure from outside (attacker view); CAM maintains the internal estate view. CAM may ingest external data, but its population is internal-first. |
| Vulnerability Management | adjacent, different center of gravity | Vulnerability management is finding-centric (scan, rank, remediate); CAM is asset-centric, with findings as one enrichment stream. CAM uniquely answers "which assets have no scanner coverage at all?" Top-end CAM products drift toward exposure management, blurring this edge. |
| Cloud Security Posture Management | adjacent, domain-specific | CSPM evaluates cloud configuration posture; its resource inventory is one ingestion source for CAM. CAM is domain-general across the estate. |
| Network Monitoring | adjacent, different question | Network monitoring optimizes device health and performance; CAM treats network devices as one asset class among many, oriented to security questions. |
| Endpoint Management / UEM | adjacent, action vs knowledge | UEM manages endpoint configuration and lifecycle; CAM inventories endpoints and checks which management/protection tools cover them. |
| Data Center Infrastructure Management | adjacent, physical focus | DCIM manages physical facility infrastructure (power, racks); CAM's population is the logical/technology estate. |

The two most important boundaries: **ITAM** (same records, different decision vocabulary — security vs finance) and **CMDB** (auto-derived security population vs curated service-oriented records). Both boundaries are confirmed by the products themselves, which integrate with — rather than replace — those systems.

## Representative Products

- **Axonius** — aggregation-first asset-intelligence platform; adapter-based normalization and correlation; enterprise SaaS
- **runZero** — discovery-first attack-surface and exposure platform; active scanning + passive sampling + integrations; SaaS or self-hosted
- **Lansweeper** — sensor-based deep inventory (IT/OT/traffic sensors, agent, cloud APIs) with credential-free device recognition; SMB to enterprise
- **JupiterOne** — graph-first platform; typed entity-relationship model with a dedicated query language; compliance/controls orientation

The defining core was checked against simpler and older shapes (single-sensor network inventory scanners, and by contrast hand-maintained registers and curated network source-of-truth tools) to avoid over-fitting the definition to the current aggregation-heavy market.

## Sources

Research date: **2026-09-07**

- Axonius — Documentation site: https://docs.axonius.com/ (Cyber Assets, Adapters List, Queries, Asset Cloud section index)
- runZero — Documentation site: https://www.runzero.com/docs/ and https://help.runzero.com/docs/ (Understanding assets, Asset risk and criticality)
- Lansweeper — Official product pages: https://www.lansweeper.com/ , https://www.lansweeper.com/product/asset-discovery/
- JupiterOne — Official site and documentation: https://jupiterone.com/ , https://docs.jupiterone.io/ (Data Model)

> Sourcing limitation: Lansweeper evidence comes from official product pages rather than a help center, so its mechanics are vendor-stated and treated with correspondingly calibrated confidence. Axonius's adapter catalog is a vendor-maintained remote table and was not enumerated item by item. Precise operational parameters (adapter counts, exact merge algorithms, retention defaults) are intentionally not stated in this document; they remain in the Research Notes.

Detailed product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
