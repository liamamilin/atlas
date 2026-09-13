# CMDB

## Overview

A **CMDB** (Configuration Management Database) is an operator-facing system of record for IT configuration. It stores **configuration items (CIs)** — identified, typed records representing the components of an organization's IT estate: servers, applications, databases, network devices, virtual machines, services, locations, and sometimes the teams and vendors responsible for them — together with the **relationships between those items**, so that the environment exists not just as a list of things but as a connected dependency model.

Three structures define the type. Remove any one and it stops being a CMDB:

```text
Configuration item — an identified, typed record of a managed IT component
└── Relationships — recorded links between CIs, forming a dependency/impact model
    └── Maintained authoritative record — one curated place where the
        organization trusts its configuration data
```

- Without the **records**, there is nothing to manage.
- Without the **relationships**, what remains is a plain asset or inventory register — a different type of application.
- Without the **maintained-authoritative posture** — the expectation that the record is curated, current, and trustworthy — the software is just a discovery snapshot or a spreadsheet.

The point of the whole structure is that someone, at an operational moment, consults it: before a change is approved ("what else depends on this database?"), while an incident is triaged ("which services run on this host?"), or when planning ("what exists in this data center?"). Keeping the record aligned with reality is the CMDB's central, permanent problem, and most of its mature machinery exists to fight that drift.

## Users & Context

A CMDB is an internal IT operations tool. Nobody outside the IT organization (or a managed service provider operating on its behalf) touches it.

Primary users and their relationship to the data:

- **Service desk / support agents** — attach incidents and requests to the CIs involved, and read the dependency context to understand what a broken component affects.
- **Change and release managers** — assess the blast radius of a proposed change by walking the relationship graph, and record which CIs a change touched.
- **Incident and problem managers** — use upstream/downstream impact to prioritize and to find root causes.
- **IT operations engineers and architects** — document the environment, maintain relationships, and plan work (migrations, decommissionings, capacity) against the model.
- **CMDB or configuration managers / IT asset managers** — own the record itself: the classification, population rules, quality programs, and lifecycle hygiene.

The usage context is continuous rather than episodic: a CMDB that is only visited once a year for an audit decays immediately. Products in this space are therefore built to be consulted and updated day-to-day, embedded inside or alongside the ITSM tooling the same teams already use (incident queues, change calendars), with discovery and monitoring integrations doing much of the writing.

## Core Model

### Configuration item (CI)

The CI is the unit of record: one identified row (or object) per managed thing. A CI carries:

- **identity** — a name and stable identifier within the database;
- **classification** — a CI type or class (server, network device, application, database instance, virtual machine, location, business process, document, contact, team…), usually drawn from a combination of pre-built and user-definable types;
- **attributes** — the configuration facts that matter for that class: technical facts (operating system, IP address, version, rack unit), organizational facts (owning organization, location, support team), and state (see Rules);
- **associations** — pointers to the records attached to the CI: work items (incidents, changes, problems, requests), contacts and teams, documents, contracts, and the services the CI supports.

The breadth of "what can be a CI" is wider than newcomers expect. Hardware and software are the obvious cases, but organizations routinely model non-physical things as CIs because they, too, have dependencies and owners: business processes, application solutions, documentation, and — in several products — people, teams, and external vendors, so that "who to call when this application breaks" is answerable from the record itself.

### Relationships

Relationships are what turn a list of CIs into a model. They are typically:

- **typed and directional** — a common formulation is a pair of inverse readings of the same link: *A depends on B* and *B impacts A*. A database schema depends on its database server; the server impacts the schema. An application solution depends on the hosts, middleware, and databases it is built from; those components impact the application, which impacts the business processes above it.
- **layered from infrastructure up to business** — a typical chain reads: racks/locations → hosts and network devices → software instances and databases → application solutions → business services/processes. Organization and location records anchor the whole graph.
- **both documented and discovered** — some relationships are declared by people; others are derived from discovery of what actually runs where, and from integrations with network or monitoring data.

### The dependency model as a whole

The aggregate of CIs plus relationships is the product's real asset: a consultable picture of the environment. Impact questions are answered by traversing it ("if this switch fails, which application solutions are hit, and who owns them?"). In several products the model is explicitly organized into **service views** — named sub-graphs that correspond to a business service — so that a team can look at one service's whole dependency segment at once.

### One structure, several product shapes

The core model is stable, but where a product concentrates its effort varies:

- ITSM-suite CMDBs emphasize governance: classification discipline, quality programs, and tight coupling of CIs to ticket and change records.
- Discovery-first platforms emphasize automatic population: the same CI + relationship structure, but fed primarily by their own scanning of the environment.
- Flexible-object ITSM systems emphasize adaptability: user-defined types and attributes assembled into a schema, with CIs attached to work items through configurable fields.

These are emphases, not different types. All of them store typed CIs, link them, and hold themselves out as the authoritative record.

## How It Works

A CMDB's operation is a standing loop rather than a single workflow. Four loops matter most.

### 1. Define the classification

Before data exists, the organization decides what its world is made of:

```text
Choose or adapt CI types/classes
→ define the attributes each type carries
→ define the relationship kinds allowed between types
→ set lifecycle states and required fields
```

Simple deployments start from the product's pre-built types; mature deployments tune the schema deliberately, because every type added is a type that must be kept truthful.

### 2. Populate and keep populated

Data enters from multiple directions, and the population mechanics are a defining part of operating the application:

```text
Automated discovery scans → create/update CIs and relationships
Integrations/connectors (monitoring, cloud, endpoint, IdP tools) → enrich or create CIs
Bulk imports (spreadsheets, migrations from other tools) → seed or extend the record
Manual entry → special cases, business-level CIs, corrections
```

Because the same server will be seen by several sources, mature products commonly provide **duplicate prevention** — matching rules that reconcile an incoming discovered device with the existing record instead of creating a second one — and several also keep **source tracking**, which records where each CI and each field's value came from. This is the machinery that makes "one authoritative record" more than an aspiration; how strictly individual products mechanize it varies.

### 3. Consult and attach work

The consumption loop is the reason the CMDB exists:

```text
Search or browse for a CI
→ open its record: attributes, relationships, attachments
→ traverse the graph for impact (upstream/downstream, path views)
→ attach the work: incident, change, problem, request linked to the CI
```

Change assessment is the canonical use: the change record carries the affected CIs, and the relationship graph supplies what those CIs touch. Several products render this as a calendar or risk view of upcoming changes with their impacted configuration.

### 4. Maintain trust

The record decays as the environment changes, so maintenance is a loop of its own:

```text
Track changes to CIs over time (history, version snapshots)
→ compare against baselines to detect drift
→ run data-quality checks (missing required fields, stale records, CIs with no relationships)
→ correct, re-discover, or retire records
```

Records are rarely hard-deleted; retirement is expressed as a lifecycle state (obsolete, archived) so history and impact analysis are preserved. How much of this loop is mechanized — full version snapshots and quality scorecards versus simple audit history — varies considerably between products; the intent to preserve trust is common across the type.

### Capability tiers

- **Defining core** — CI records with classification and attributes; relationships between CIs; the maintained-authoritative posture that makes it a system of record.
- **Standard capabilities in mature products** — multi-source population (with duplicate prevention common in mature products); CI detail as an association hub for work items and documents; impact/dependency analysis; list/table exploration with search; audit history; dashboards; role-based administration of schema and data.
- **Common optional extensions** — automated dependency mapping from network/observability data; baselines and drift detection; formal data-quality policy engines; asset-financial fields (purchase, warranty, contract, licence); federated or query-language access; business-criticality scoring; service views and business-process CIs.

## Interfaces

The interfaces are browser-based operational consoles. Exact layouts vary; the surfaces below recur across the type.

### CI list / explorer

The primary entry surface: a table or list of CIs, filterable and searchable by type, state, location, owner, or free text.

- typical information: name, type, state, key attributes, owner/support team, relationship counts
- primary actions: search, filter, open a CI, create a CI, run bulk operations

### CI detail page

The workhorse surface — one page per configuration item, organized as an association hub.

- typical information: all attributes for the class; relationship lists (what it depends on, what depends on it); attached work items; contacts and teams; documents; history of changes to the record; data-quality indicators where offered
- primary actions: edit attributes, add/remove relationships, attach work items or documents, view impact, retire/archive

### Relationship / impact map

A graphical canvas over the dependency model.

- typical information: a sub-graph of CIs and links, usually centered on a chosen CI or saved service view
- primary actions: navigate the graph, run impact analysis in a chosen direction and depth, save a view, define or edit relationships

### Dashboards / health views

Summary surfaces over the population and its quality.

- typical information: CI counts by type and state, data-quality metrics (completeness, staleness, orphaned records), CI-to-work-item associations
- primary actions: drill into problem areas, export, track trends

### Administration / schema editor

Where the classification lives.

- typical information: CI types and their attributes, relationship definitions, discovery/integration configurations, import mappings, user roles
- primary actions: create/modify types and fields, configure duplicate-prevention rules, connect data sources, manage access

## Important Rules / Behaviors

### The record must stay true — and the type is built around that

Unlike most registers, a CMDB's value is entirely conditional on accuracy. This is why the standard machinery of the type — duplicate-prevention rules, source tracking, audit trails, quality scorecards, baselines — all targets the same failure mode: the record diverging from reality. A CMDB's rules are, in essence, trust-preservation rules.

### Identity and duplication

The same component seen through two sources must resolve to one CI. Products differ in how strictly they enforce this, but duplicate CIs are treated as defects throughout the type, and matching/identifier rules are the standard defense.

### CIs carry lifecycle state

State values are product- and organization-specific, but the pattern is universal: a CI is acquired/built, enters production, and eventually becomes obsolete or retired. Hidden-but-present states (obsolete, archived) are preferred over deletion, because impact history must survive the component.

### Relationships carry direction

Dependency links are directional and consultable in both readings. The practical rule: impact flows along the graph. Tools that let users traverse "upstream" (what breaks this?) and "downstream" (what does this break?) are expressing one invariant.

### CIs are reference targets

Incidents, changes, problems, and requests attach to CIs. The attachment is what makes the CMDB operational rather than academic — it is how the record gets consulted during real work, and how day-to-day usage keeps it accurate.

### Access is graduated

Editing the schema (adding types, changing attributes) is an administrative act distinct from editing data; discovery-driven writes are system acts distinct from human edits. Who may declare a relationship, correct an attribute, or retire a CI varies by organization, but the separation of schema governance from data stewardship is standard.

## Variants

- **ITSM-suite module** — the dominant shape: the CMDB lives inside a service management platform and is coupled to its incident/change/problem records.
- **CMDB-first product** — the configuration database is the core, with ticketing and other processes built around it (common in open-source and specialist products).
- **Discovery-first platform** — a standalone configuration platform whose automatic discovery is the selling point; it either *is* the CMDB or serves as the population engine feeding other platforms' CMDBs.
- **Flexible object store** — user-defined types/attributes assembled into a schema, with configuration attached to work items via configurable fields (common in mid-market ITSM).
- **Deployment poles** — cloud SaaS vs self-hosted; open-source vs commercial; single-organization vs multi-tenant (MSP/provider operation for many customers).
- **ITAM convergence** — products that fuse configuration records with asset-financial lifecycle (procurement to retirement) under one record or one suite; the seam with IT Asset Management is commercial as much as structural.
- **Scale poles** — documentation-first deployments (predominantly manual entry and imports) vs large continuous-discovery deployments with dedicated configuration-manager roles; the appropriate schema discipline and quality machinery scale accordingly.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| IT Asset Management | closest sibling, heavy market overlap | ITAM's object is the *asset* under financial/lifecycle management (purchase, contract, depreciation, disposal); the CMDB's object is the *CI* under configuration/dependency management. Remove relationships and service context → ITAM; remove financial lifecycle → still a CMDB. Products commonly ship both. |
| IT Service Management / ITSM | container and consumer | ITSM platforms run the processes (ticketing, change) that consume CMDB data; the CMDB can exist without the ticketing, and predates it architecturally. |
| IT Change Management | consumer process | change workflows read impact from the CMDB and write back affected-CI associations; the CMDB itself is the data system, not the approval workflow. |
| Configuration Management (the practice) | discipline vs system of record | the practice is the process discipline for managing configuration; the CMDB is the record it operates on. Also unrelated to config-as-code drift tools, which manage desired server state rather than an organization-wide CI graph. |
| Data Catalog / Metadata Management | same pattern, different domain | catalogs inventory *data assets* with ownership and lineage; CMDBs inventory *IT components* with dependencies. The structure is analogous; the object domain is not. |
| Application Portfolio Management | coarser register | APM tracks applications at business level (owner, spend, lifecycle stage); the CMDB decomposes to technical granularity and links applications to infrastructure. |
| Enterprise Asset Registry | adjacent, different estate | registries for physical/plant/facility assets rather than IT configuration; overlap only at the datacenter-hardware edge. |
| DCIM / IPAM / Cyber Asset Management | specialized subset registers | each holds one lens of the estate (datacenter, IP space, security-relevant assets); they feed the CMDB or duplicate a slice of it. |
| Infrastructure Monitoring / Observability | live state vs curated record | monitoring sees current telemetry; the CMDB holds curated configuration identity and dependencies. Monitoring integrations are a major *source* for the CMDB, not a substitute. |

The sharpest seam is with **IT Asset Management**, because the market sells the two in the same suites and both keep inventories of the same hardware. The structural test is the relationship graph: a register without dependencies-and-impact is asset management, however it is labeled.

## Representative Products

- ManageEngine ServiceDesk Plus (built-in CMDB) — ITSM-suite pole
- Atlassian Jira Service Management (Assets) — flexible object-store pole
- Freshservice (Freshworks) — SMB/mid-market cloud ITSM pole
- Device42 — discovery-first platform pole
- iTop (Combodo) — open-source, CMDB-first pole

The enterprise market also includes much larger configuration-management platforms at the top tier of the ITSM market; they were not document-verified in this pass and are not relied on for any claim above. The core model was additionally checked against an open-source, manually documented, regionally European product to avoid over-fitting the definition to modern auto-discovery platforms: a CMDB built by hand-entered records and bulk imports satisfies the same defining structure.

## Sources

Research date: **2026-09-07**

- ManageEngine — "ITIL Configuration Management Database (CMDB) Software" (ServiceDesk Plus) — https://www.manageengine.com/products/service-desk/cmdb.html
- Atlassian — "Connect Assets schemas with changes" and JSM Cloud documentation index — https://support.atlassian.com/jira-service-management-cloud/docs/connect-assets-schemas-with-changes/ , https://support.atlassian.com/jira-service-management-cloud/resources/
- Freshworks — "Freshservice CMDB" — https://www.freshworks.com/freshservice/features/it-asset-management/cmdb/
- Device42 — documentation root, CMDB and ITSM pages — https://docs.device42.com/ , https://www.device42.com/features/cmdb/ , https://www.device42.com/itsm/
- iTop (Combodo) — "What is iTop", Data Model Documentation, Configuration Management (CMDB) Module — https://www.itophub.io/wiki/page?id=start , https://www.itophub.io/wiki/page?id=3_2_0:datamodel:start , https://www.itophub.io/wiki/page?id=3_2_0:datamodel:itop-config-mgmt

> Sourcing limitation: official documentation for the two largest enterprise vendors in this category could not be retrieved from the research environment on 2026-09-07 (JavaScript-gated docs application; blocked requests). All operational statements in this document rest on the five products above; enterprise-specific mechanics (e.g., reconciliation engines between competing data sources) are therefore described only where the sampled products document them, and no numeric limits or defaults are asserted.
