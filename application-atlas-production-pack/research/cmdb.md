# Research Notes — CMDB

Research date: 2026-09-07

## Research Goal

Understand what a CMDB (Configuration Management Database) actually is as an application type: what objects live inside it, how it is populated and kept trustworthy, how it relates to ITSM processes, and how it differs from adjacent registers (asset management, data catalog, specialized inventories).

## Initial Boundary (hypothesis before research)

- What it is (hypothesis): a system of record for IT configuration — identified records of IT components ("configuration items") plus the relationships between them, maintained to support IT operations decisions (change risk, incident triage, impact analysis).
- Likely users: IT operations teams, ITSM process owners (change/incident/problem managers), asset managers, architects.
- Likely nearest types: IT Asset Management, Configuration Management (the practice), ITSM, IT Change Management, Data Catalog / Metadata Management, Application Portfolio Management, Cyber Asset Management, DCIM/IPAM (specialized registers).
- Likely confusions: CMDB vs ITAM (financial/lifecycle focus); CMDB vs generic "asset inventory"; CMDB vs the Configuration Management *discipline*; CMDB vs monitoring/observability (live telemetry vs configuration state).

## Research Questions

1. What exactly is a "configuration item" (CI)? What kinds of things become CIs? Who defines the classification?
2. How are relationships between CIs modeled, and what do users do with them (impact analysis, maps)?
3. How does data get into the CMDB — discovery, integrations, manual entry, imports — and how do products prevent duplicates/conflicts between sources?
4. How is the CMDB coupled to ITSM workflows (change, incident, problem)?
5. What health/quality/trust mechanisms exist (completeness, staleness, orphans, baselines, drift, audit trail)?
6. What interfaces do operators actually face (CI lists, CI detail, relationship graph, dashboards, admin)?
7. What rules govern the data (states, ownership, lifecycle, archiving)?
8. Boundary: what distinguishes a CMDB from an asset register, a data catalog, or the configuration-management discipline?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / tier | What was fetched |
|---|---|---|
| ManageEngine ServiceDesk Plus CMDB | mid-market ITSM suite with built-in CMDB | official CMDB feature page (operational, feature-named) |
| Atlassian Jira Service Management — Assets | mid-market ITSM; flexible object-schema CMDB capability | official support docs (Assets ↔ change/incident connection, AQL) |
| Freshservice (Freshworks) | SMB/mid-market cloud ITSM; CMDB under ITAM umbrella | official CMDB product page |
| Device42 | discovery-first standalone platform (DCIM/ITAM/CMDB hybrid) | official docs root + CMDB/ITSM feature pages |
| iTop (Combodo) | open-source, CMDB-first ITSM (European heritage) — also serves the historical/regional check | official wiki: "What is iTop", Data Model (CMDB), Configuration Management Core (full CI class reference) |

Enterprise market leaders **ServiceNow CMDB** and **BMC Helix CMDB** were selected a priori but their official documentation was not reachable from this environment (see Sources — access limitations). They are retained as market context only; **no operational claim in either file is based on them**.

## Sources

Fetched 2026-09-07:

- ManageEngine ServiceDesk Plus — "ITIL Configuration Management Database (CMDB) Software" — https://www.manageengine.com/products/service-desk/cmdb.html
- Atlassian — "Connect Assets schemas with changes" (JSM Cloud support) — https://support.atlassian.com/jira-service-management-cloud/docs/connect-assets-schemas-with-changes/
- Atlassian — JSM Cloud documentation index (Assets/AQL doc slugs located via index) — https://support.atlassian.com/jira-service-management-cloud/resources/
- Freshworks — "Freshservice CMDB" product page — https://www.freshworks.com/freshservice/features/it-asset-management/cmdb/
- Device42 — documentation root — https://docs.device42.com/
- Device42 — "CMDB Features" — https://www.device42.com/features/cmdb/
- Device42 — "ITSM" — https://www.device42.com/itsm/
- iTop (Combodo) — "What is iTop" — https://www.itophub.io/wiki/page?id=start
- iTop — Data Model Documentation (Configuration Management / CMDB) — https://www.itophub.io/wiki/page?id=3_2_0:datamodel:start
- iTop — Configuration Management (CMDB) Module — https://www.itophub.io/wiki/page?id=3_2_0:datamodel:itop-config-mgmt

Access limitations encountered:

- docs.servicenow.com — JavaScript-gated app shell, content not retrievable (2 attempts on different URLs).
- servicenow.com product pages — timeout ×2.
- docs.bmc.com / bmc.com — HTTP 403 ×2.
- support.atlassian.com — several wrong-slug 404s before reaching the documentation index; one Tier-1 article + doc index captured.
- support.freshservice.com support articles — not reached; Freshworks product page used instead (Tier 2).
- Device42 /features/cmdb/ body largely truncated by page navigation chrome in fetch; docs root + ITSM page captured instead.

Consequence (evidence rule): no claim about ServiceNow/BMC internal mechanisms (identification/reconciliation engines, common service data models, federation) appears anywhere in the outputs. Enterprise-tier behavior is asserted only where the sampled products support it.

## Product Observations

### ManageEngine ServiceDesk Plus — CMDB (evidence layer A throughout)

- CMDB = "the centralized system of record for configuration data"; goal framed as "a single source of truth for your IT infrastructure".
- CI definition (FAQ): "A configuration item (CI) is any component within the IT environment that directly or indirectly contributes to service delivery. This includes IT hardware, software, teams, individual contributors, and external vendors."
- Population: built-in discovery or third-party tools; auto-sync of newly discovered assets as CIs using sync rules, identifier rules, and field mappings "that prevent duplicate assets and CIs".
- Relationships: drag-and-drop canvas to "define custom relationships between CIs"; service-specific segments saved as "Business Views"; impact path tables.
- CI Impact Analysis: pick a CI or set conditions with depth and direction filtering; "see the full impact path laid out".
- ITSM coupling: CIs associated with incidents, service requests, changes, problems, releases; stakeholders view the dependency map in one click from the process record.
- CMDB Baselines: versioned snapshots of CI attributes and relationships across time; compare versions to spot added/removed/modified configuration ("detect configuration drift"); per-CI version history on the CI details page.
- Data quality: policies configured per CI type — completeness (required fields), staleness (duration), orphan (essential relationships); per-CI data-quality scorecard; CMDB dashboard with CI counts by state, DQ metrics by CI type, and CI-to-module associations.
- Source tracking: "Integration Mapping" records which integration each CI came from, down to the instance; used for filtering and duplicate tracking.
- Observability integrations: CIs and dependencies (Layer 2 devices, applications) pulled from ManageEngine and third-party monitoring/observability suites.
- FAQ: CMDB "essential for incident resolution, root cause analysis, change risk assessment…".

### Atlassian Jira Service Management — Assets (evidence layer A)

- Assets is JSM's CMDB capability. Objects described as "Assets objects (such as hardware, software, or other resources)".
- Structure: objects live in "object schemas"; objects are attached to change/incident work items via dedicated "Assets object" custom fields mapped to schemas.
- Change coupling: "Risk insights: View potential change conflicts on specific Assets objects"; "Change calendar: Track which Assets objects will be impacted by upcoming changes."
- Same mechanism documented for connecting Assets schemas with incidents.
- Query language: "Use service objects in AQL" (Assets Query Language) exists as a documented surface for querying objects.
- Separate JSM feature "service relationships" exists alongside (JSM Services vs Assets distinction — vendor structure).

### Freshservice (Freshworks) (evidence layer A; product page = Tier 2)

- "A modern CMDB for 360° visibility into your infrastructure… integrated source of truth for your assets and their complete lifecycle."
- Multi-source population: "out-of-the-box native discovery solutions and real-time connectors with leading discovery solutions, identity providers, and endpoint management tools"; "auto-updating CMDB" across cloud and on-premises.
- ITSM coupling: "asset relationship information available at your fingertips, perform efficient change deployments and accurate root cause analyses by precisely gauging upstream and downstream impact."
- Trust: "complete audit trails capturing updates and visibility into all incidents, problems, and changes associated with your assets."
- Asset-lifecycle integration: "managing everything from procurement to retirement right within Freshservice"; financial management of asset value/expenses in the same pane.
- Advanced relationship mapping sourced via Device42 integration ("self-documenting CMDB with real-time discovery of device data and granular dependencies").
- Product page sits under the IT Asset Management umbrella — market blurs CMDB and ITAM at this tier.

### Device42 (evidence layer A for positioning; feature pages Tier 2)

- Positioned as "Integrated DCIM, CMDB, ITAM, reporting and more in a single platform"; CMDB framed as "Next Generation CMDB… Near Real-time, automated, with actionable insights".
- Discovery-first philosophy: comprehensive infrastructure/cloud discovery (mainframes to containers) feeding the CMDB; native Application Dependency Mapping ("built-in native ADM").
- Data quality via "EnrichAI": "standardize, normalize, and enrich CI data".
- Open RESTful API + 30+ named integrations feeding ITSM tools (ServiceNow, JSM, Freshservice, Cherwell, Zendesk, Samanage…) — Device42 frequently acts as the discovery/population source for another platform's CMDB.
- Companion capabilities that touch the same data: IPAM, SSL certificate management, storage discovery, software license management, password management.

### iTop (Combodo) — open-source, CMDB-first (evidence layer A; Tier-1 wiki)

- "At the heart of iTop is the CMDB… originally the first part of iTop that was developed. Then came the tickets and all the derived processes."
- Philosophy: "a CMDB must be an operational tool. The only way for a CMDB to be accurate and up to date is to be used day-to-day by the IT teams"; accuracy improves with integration with monitoring/reporting/inventory tools.
- Function: "Document your IT infrastructure and all the relationships between the various pieces and stakeholders of the infrastructure (servers, applications, network devices, virtual machines, contacts, locations…)"; "Mass import (manually and using scripts) or synchronize/federate any data from external systems."
- Data model (Configuration Management Core, mandatory module): Organizations, Contacts (Persons, Teams), Documents (file/note/web), and CIs: Servers, Network Devices, DB Servers, Database Schemas, Middleware + Middleware Instances, Web Servers + Web Applications, PC/Other Software, Application Solutions, Business Processes, Software Licences, Patches, Locations, Racks, Enclosures, Power Connections. Optional modules add: End-Users Devices (PCs, phones, printers), Virtualization (VMs, hypervisors, farms), Advanced Storage (SAN, NAS, volumes), Data Center (racks, enclosures, power).
- CI record anatomy (per class reference): attributes — name, Organization (multi-org scoping), Status (class-specific lifecycle: e.g., implementation / production / stock / obsolete for devices; active/inactive for software; draft/obsolete/published for documents), Business criticity (high/medium/low), Location/Rack/Enclosure, brand/model/OS, serial number, asset number, purchase date, end of warranty, move-to-production date.
- Standard CI tabs (association hub): Contacts, Documents, Tickets, Application solutions depending on this CI, Services impacted, Provider contracts.
- Directed relationship semantics throughout the data model: every CI class documents "Impacts: …" and "Depends on: …" — e.g., a DB Server impacts its database schemas and the Application Solutions it belongs to, and depends on the system it runs on; Business Process depends on Application Solutions; Application Solution's "main information conveyed … is its list of relationships."
- Lifecycle hygiene: per-class "obsolescence" flag (obsolete objects can be hidden from lists) and "archiving" as a soft delete.
- Ticketing modules link tickets to CIs; change management (simple and ITIL flavors) operates over the same data; service management defines services/SLAs/contracts in enterprise vs provider flavors.
- Users: help desk agents, support engineers, service managers, IT managers.

## Cross-product Comparison

| Dimension | ServiceDesk Plus | Atlassian JSM Assets | Freshservice | Device42 | iTop |
|---|---|---|---|---|---|
| Core record | CI ("any component… contributing to service delivery" incl. teams, vendors) | Assets object (hardware/software/resources) in object schemas | asset/CI with relationships | discovered device/app/CI data | typed CI classes (servers, software, VMs, contacts, locations…) |
| Classification | CI types (admin-managed) | user-definable object schemas/types/attributes | asset/CI types | platform-defined discovered types | predefined class hierarchy, modular extension |
| Relationships | custom relationships, visual canvas, Business Views | object references; objects attached to work items via fields | asset relationships; upstream/downstream impact | discovered dependency mapping (native ADM) | Impacts / Depends on semantics on every class |
| Population | built-in discovery + third-party tools; auto-sync with identifier rules | object creation + imports (documented in wider docs; not directly fetched) | native discovery + real-time connectors (IdPs, endpoint mgmt) | own deep discovery (physical/virtual/cloud) | manual documentation; mass import; synchronize/federate external systems |
| Duplicate/conflict handling | sync rules, identifier rules, field mappings; integration-mapping source tracking | (not directly observed) | (not directly observed on fetched page) | normalize/enrich (EnrichAI) | (not directly observed in fetched pages) |
| ITSM coupling | CIs ↔ incidents/SRs/changes/problems/releases | Assets objects ↔ change requests (risk insights, change calendar) and incidents | CMDB as backbone; audit trail; incidents/problems/changes on assets | feeds third-party ITSM tools | tickets/changes/problems link to CIs; CMDB predates ticketing |
| Impact analysis | CI Impact Analysis (depth/direction, impact path) | change conflicts per object; impacted objects on calendar | upstream/downstream impact for change & RCA | dependency maps for resolution/migration | Impacts/Depends on graph; services impacted per CI |
| Data quality/health | per-type DQ policies (completeness/staleness/orphan), scorecards, CMDB dashboard | (not directly observed) | audit trails | standardize/normalize/enrich | obsolescence flag; archiving (soft delete) |
| Baselines/drift | CMDB Baselines, version compare, CI version history | (not directly observed) | (not directly observed) | (near-real-time discovery refresh) | (not directly observed) |
| Financial/asset fields | separate ITAM capability alongside | asset-oriented naming (Assets) | procurement→retirement, asset value, financial mgmt | ITAM/SAM license comparison in same platform | serial/asset numbers, purchase date, warranty, licences on CIs |
| Deployment tier | mid-market suite | mid-market suite | SMB/mid SaaS | standalone discovery platform | open source, self-hosted, CMDB-first |

Evidence-layer note: "CI + type + attributes", "relationships feeding impact analysis", "multi-source population", "ITSM record association" are observed in ≥3 products each (layer B). Baselines/drift and DQ-policy machinery observed in 1–2 products (keep qualified: common in mature products, shapes vary). Atlassian duplicate-handling and iTop reconciliation internals were not observed — no claims.

## Canonical Abstraction

### Level 0 — Defining Invariant

The smallest structure without which the product stops being recognizable as a CMDB:

```text
CI — identified, typed record of a component of the organization's IT estate
  (attributes carry the component's configuration identity: name, class,
   state, ownership/location, key technical facts)
└── Relationships between CIs — recorded links that connect the records
    into a dependency/impact model of the environment
    └── Maintained as the authoritative configuration record
        (single curated place where the organization trusts its
         configuration data — which is why keeping it current is the
         application's central problem)
```

Three properties. Remove the relationships and it degrades into a plain asset/inventory register (a different type). Remove the maintained/authoritative posture and it is just a discovered snapshot or a spreadsheet. Remove the CI records themselves and there is no CMDB at all.

The purpose anchor — serving IT operations decisions (change risk, incident triage, impact analysis) — is implicit in the L0: the relationship graph exists precisely to be consulted. It is stated explicitly in the definition sentence rather than as a fourth structure.

### Level 1 — Common Mature Structure

Present in most mature products; not required to recognize the Type:

- multi-source population: built-in discovery, integrations/connectors, CSV/import, manual entry; duplicate-prevention rules (identifier/sync rules) and source tracking
- CI detail as an association hub: work items (incidents/changes/problems/requests), contacts/teams, documents, contracts, services attached to the record
- impact/dependency analysis over the relationship graph (upstream/downstream, path views, service maps)
- list/table exploration by CI type with search/filter; query language in several products
- change history / audit trail on CI records
- dashboards summarizing CI population and quality
- role-based administration of the schema and the data

### Level 2 — Variant / Optional Structure

- CMDB-health machinery: completeness/staleness/orphan policies, per-CI scorecards, health dashboards (shape varies; not universal in the sample)
- reconciliation/precedence engines arbitrating multiple authoritative sources (documented for some products; not directly observed in this sample — see uncertainties)
- service discovery/mapping from network or observability data feeding relationships automatically
- baselines/drift detection (snapshot compare)
- business criticality scoring and business-process CIs at the top of the dependency chain
- asset-financial fields (purchase/warranty/contract/licence) and lifecycle from procurement to retirement — the ITAM convergence zone
- federation (querying external sources live rather than copying), multi-organization/multi-tenant scoping
- archiving/obsolescence policies, soft delete
- product-shape poles: ITSM-suite module vs CMDB-first product vs discovery-first platform; open-source self-hosted vs SaaS; enterprise vs provider (MSP) flavors

### Level 3 — Vendor-specific (kept out of the final document)

- ServiceDesk Plus: Business Views, CI Impact Analysis naming, CMDB Baselines, Integration Mapping, sync/identifier rule machinery, CMDB Dashboard
- Atlassian: Assets object schemas, object types/attributes, "Assets object" custom-field mechanism, AQL, change-risk-insights/change-calendar surfaces, JSM Services vs Assets split
- Freshservice: native discovery + connector catalog, Orchestration Center, SaaS Management adjacency, Device42-powered deep mapping
- Device42: EnrichAI normalization, InsightsAI/DOQL SQL surfaces, Affinity move groups, DCIM depth (racks/patch panels), position as population source for other platforms' CMDBs
- iTop: exact class list (DB Server, Middleware Instance, Database Schema…), enterprise-vs-provider service-management modules, obsolescence/archiving features, CSV import/synchro data-source machinery

## Vendor-specific Findings

- ServiceDesk Plus's data-quality scorecard and baseline-compare loop is the most explicit "keep the record trustworthy" program in the sample (single product — do not generalize as definitional).
- Atlassian's route into the CMDB is via custom fields on work items rather than a standalone map-first surface (single-product shape; shows the coupling can be field-based rather than graph-first).
- iTop's design statement that "a CMDB must be an operational tool… used day-to-day" is a philosophy claim from one vendor, but it converges with the trust mechanics observed in ServiceDesk Plus (quality programs) and Freshservice (audit trails).
- Device42 demonstrates that a CMDB-capable product can be sold primarily as a discovery platform whose data populates other platforms' CMDBs — an ecosystem position, not a separate type.

## Rejected Findings (considered, not promoted)

- "CMDB = auto-discovery": rejected. iTop documents manual documentation + mass import/synchronization as first-class population; discovery-driven population is a mature-market implementation, not the invariant.
- "CMDB = enterprise reconciliation engine with precedence rules": rejected for L0/L1 — not directly observed in the sample; classified as a variant/advanced capability.
- "CIs are only hardware/software": rejected — ServiceDesk Plus explicitly names teams, individual contributors, and vendors as CIs; iTop models Persons, Teams, Locations, Business Processes as CI classes.
- "CMDB must include financial asset data": rejected — present in several products but separable (ServiceDesk Plus ships ITAM as a distinct capability).
- "CMDB is a graph database": rejected — implementation detail; every sampled product implements the graph differently.
- "CMDB = ITIL compliance artifact": rejected — iTop explicitly states it "does not dictate any specific process".

## Boundary Findings

- **vs IT Asset Management**: ITAM's managed object is the *asset* (financial ownership: procurement, cost, contract, depreciation, disposal). The CMDB's managed object is the *CI as configuration*, whose defining structure is relationships/dependencies. Test: delete relationships and service context from a CMDB → an asset register (ITAM). Delete financial/lifecycle data → still a CMDB. The market converges (Freshservice sells CMDB under ITAM; Device42 sells both; iTop puts warranty/licence fields on CIs), so the seam is structural, not commercial. Both directory leaves stand.
- **vs Configuration Management (the practice/leaf)**: the practice is the process discipline; the CMDB is its system of record. Also distinct from config-as-code drift-management tools (those manage desired-state of servers, not an organization-wide CI graph).
- **vs ITSM**: ITSM platforms consume the CMDB; the CMDB predates and outlives ticketing (iTop built the CMDB first, then tickets — vendor statement, but the architecture is consistent across the sample). CMDB without ticketing is common (Device42 as population source).
- **vs Data Catalog / Metadata Management**: identical "inventory + ownership + relationships + search" pattern applied to *data assets*; the CMDB's object domain is IT/service components. Domain shift = type shift.
- **vs Application Portfolio Management**: APM is a coarser, business-level application register; the CMDB decomposes at technical CI granularity and connects applications to infrastructure.
- **vs DCIM / IPAM / Cyber Asset Management**: specialized registers for subsets of the estate (datacenter, addresses, security-relevant assets). They either feed the CMDB (Device42 feeds others) or overlap as subset lenses. A CMDB that only ever held datacenter racks would be drifting toward DCIM.
- **"Remove-what" test (the sharpest seam)**: remove the *relationships/impact model* and what remains is asset/inventory management; remove the *IT-component domain* and the same structure becomes a data catalog; remove the *maintained-record* posture and it becomes a monitoring/discovery snapshot.

## Uncertainties

- Enterprise-leader mechanics (ServiceNow/BMC identification/reconciliation engines, federation, common service data models) not verified from official sources — deliberately absent from both files.
- Atlassian Assets: duplicate-prevention and import mechanics not directly fetched; only object-schema/change/incident coupling verified.
- iTop: reconciliation/synchronization internals (its data-synchro machinery) not fetched in this pass; "synchronize/federate" verified at capability level only.
- Whether CMDB-health programs (DQ policies) are now universal at enterprise tier could not be verified beyond the sample.
- Exact numeric limits (e.g., Atlassian's documented 30-activated-Assets-fields-per-space cap) observed but excluded from the final document as product detail.

## Final Synthesis

A CMDB is best understood as **a maintained system of record for IT configuration**: typed configuration-item records carrying the identity and state of the organization's IT components, connected by explicit relationships into a dependency model that IT teams consult when they need to know what exists, how it is connected, and what is affected.

Everything else in the market — automated discovery, reconciliation between sources, impact maps, baselines and drift detection, data-quality scorecards, financial lifecycle fields, ITSM embedding — is mature machinery that has accreted around that core to fight the core's one endemic failure mode: the record drifting away from reality. Products differ on where they sit between "document and govern" (ITSM-suite CMDBs, iTop), "discover and feed" (Device42), and "attach configuration to work" (JSM Assets), but the CI + relationship + authoritative-record structure is stable across all of them, across deployment tiers, and across decades.
