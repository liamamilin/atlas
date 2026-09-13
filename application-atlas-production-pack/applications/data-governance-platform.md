# Data Governance Platform

## Overview

A **Data Governance Platform** is the application that makes an organization's data governance program operational. Where a governance framework describes what should happen — policies, roles, standards — the platform is the system in which that program actually runs: the rules are held as managed records attached to the data they govern, accountability is assigned to named people across an organization-aligned structure, and the program's work moves through governed processes whose steps are attributable and reviewable.

The defining structure is deliberately small:

```text
Governance rules as managed records (policies/standards attached to the data they govern)
└── Accountability structure over data (named stewards/owners across org-aligned domains)
    └── Governed processes (requests, approvals, certifications, issue resolution —
        attributable, reviewable, retained as history)
```

Everything else that modern products carry — the embedded data catalog, automated harvesting and classification, business glossaries, certification and trust flags, compliance checks, access controls, quality scores, lineage, health dashboards, data products, AI assistance — enriches the program but does not define it. A governance program run on paper (a council with named roles, a policy binder, a change board) satisfies the same structure; the platform digitizes and scales it.

The boundary with the **Data Catalog** is the most important one, because the two are sold together everywhere and often ship as one product. The working distinction, stated in a sampled vendor's own FAQ: *a catalog shows what data exists; governance defines how it should be used, who has access, and how compliance is enforced.* The catalog's objects are descriptive (what the data is and means); the governance platform's objects are normative and operational (what must hold, who is accountable, which processes change state).

## Users & Context

The primary users are the people accountable for the organization's data as an asset:

- **Central data office / chief data officer** — sets the governance strategy, owns the operating model, watches program-level health and compliance. In a federated model (a pattern mature products support and name), this office sets the rules while distributed roles govern their own data.
- **Data owners** — accountable for specific data areas or assets: they register assets, manage classifications and access, and answer for quality and policy adherence.
- **Data stewards** — the working layer of governance: they curate definitions, maintain glossary terms, resolve data issues, and execute the review steps in governance workflows.
- **Governance administrators** — configure the platform itself: domains, roles, workflow definitions, policy templates, integrations.

Secondary users are **data consumers** (analysts, scientists, and increasingly AI agents and their developers), who encounter governance as guardrails: trust flags on assets, policies surfaced at the point of use, access requests routed through the platform.

Typical context: an enterprise with many data systems and teams, regulatory pressure (privacy laws, industry regulation), and — in the current era — AI initiatives that raise the stakes of data trust. The platform is usually bought as part of a broader data-intelligence or data-management investment, and the governance program it operationalizes is an organizational change effort as much as a software deployment.

## Core Model

### The Defining Core

Three structures. If any one is removed, the product stops being a governance platform:

**1. Governance rules as managed records.** The organization's policies, standards, and rules for data and its use exist as first-class objects inside the platform — named, described, versionable, and linked to the data they apply to. This is what separates a governance platform from a policy binder: a policy that is linked to the tables, reports, or domains it governs can be surfaced where the data is used, checked against the estate, and changed through a process. Policies come in two common forms: business-authored policies (data-source agnostic rules the organization writes) and source-extracted policies (technical policies read out of the data platforms themselves, such as masking or row-access rules). Both are held as objects with their own pages, not as document attachments.

**2. Accountability structure over data.** Governance is someone's job. The platform models that assignment: named data owners and stewards attached to data areas, assets, and domains, organized through containers that mirror the organization (domains, communities, governance domains). The structure carries the operating model — in a federated pattern, a central data office sets the rules while owners and stewards in business areas govern their own data under them. Roles are explicit and differentiated: what an owner may decide, what a steward may curate, what an administrator may configure, what a consumer may see.

**3. Governed processes.** Governance state changes through attributable, reviewable steps. The common implementations are workflows: change requests on catalog fields and policies (suggest → designated reviewer approves or rejects → change applied, history retained), access requests routed to owners, certification of trusted assets, and data-issue tickets tracked to resolution. The invariant is the pattern — steps that are attributable to people, reviewable by designated parties, and retained as history — not any specific workflow engine. A change board running the same loop by email satisfies it; the platform makes it continuous and auditable.

### Standard Capabilities

Mature products commonly add the following. They make the program practical; they are not what makes the product a governance platform.

- **Embedded catalog / metadata inventory** — the governed estate represented as asset records harvested from source systems. Governance objects attach to these records; the catalog is the substrate the program acts on (and the visible surface of most governance suites).
- **Automated harvesting and classification** — connectors and scanners keep the inventory current; AI-assisted classification labels sensitive data and suggests descriptions at scale.
- **Business glossary** — the shared vocabulary of terms and definitions, approved and linked to assets; the "single source of truth for business terms."
- **Domains as organizing containers** — governance domains or communities scoping accountability, curation, and visibility to business areas.
- **Certification and trust states** — marks on assets (certified, verified, trust flags) produced through review, signaling which data is approved for use.
- **Compliance checking** — automated validation of assets against policy conditions, with violations flagged and adherence overviewed for audits.
- **Access machinery** — access policies on data products and assets, self-service access requests routed to owners, masking and row-level controls in deeper deployments.
- **Data quality and lineage integration** — quality scores and rules, lineage graphs for impact and root-cause analysis, surfaced inside the governance view.
- **Program visibility** — governance dashboards, health scores, usage analytics, objectives linked to data products; data-issue management (helpdesk-style incident workflows).
- **Data products and marketplace** — governed, reusable bundles of assets published for consumption with their policies attached (an emerging common layer).
- **AI assistance** — suggested descriptions, automated classification, copilots, enrichment agents; universal in current products but recent-era.
- **Integration surfaces** — APIs for programmatic access; governance actions embedded in chat and collaboration tools.

## How It Works

### Establish the operating model

The deployment starts with structure, not data: define the domains that mirror the organization, assign owners and stewards to them, configure roles and permissions, and author the first policies and glossary terms. This is the governance program's skeleton; everything else attaches to it.

### Connect the estate

Connectors and scanners harvest metadata from the organization's data systems into the platform's inventory. Classification runs over the estate (increasingly AI-assisted), labeling sensitive data and suggesting descriptions. The result is the governed substrate: asset records that policies, owners, and processes can attach to.

### Govern through processes

The day-to-day loop runs through the platform's process machinery:

```text
Someone proposes a change (new term, field edit, policy update, access request)
→ routed to the designated reviewer/owner
→ approved or rejected, with the decision recorded
→ applied to the governance record
→ history retained on the record and in the program's audit trail
```

The same pattern covers certification (an asset is reviewed and marked trusted), issue resolution (a data problem is submitted, assigned, worked, and closed), and access (a consumer requests data; the owner decides). Objects can sit in multiple workflows; products resolve conflicts with explicit precedence rules.

### Enforce and monitor

Policies are checked against the estate — automatically where the platform can evaluate them, by flagging where it cannot. Violations surface to the accountable parties. Health and compliance scores aggregate the state of the program: which assets are certified, which policies are adhered to, which domains are falling behind.

### Report

Dashboards and reports make the program visible to its sponsors: adoption, coverage, policy adherence, issue aging, value delivered. Audit evidence — who approved what, when — is a first-class output, not an afterthought.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Governance dashboard / program home

The program-level view for the data office.

- typical information: coverage and health scores, policy adherence, certification status, adoption and usage, issue backlog
- primary actions: drill into domains and assets, track objectives, export evidence

### Policy center

The managed library of governance rules.

- typical information: policy records (business and source-extracted), the data each policy applies to, status and review state
- primary actions: author and edit policies, link them to assets/domains, run or review compliance checks, propose changes through workflow

### Workflow inbox / tasks

The reviewer's working surface.

- typical information: assigned change requests, access requests, certifications, issues — with context on the affected record
- primary actions: approve, reject, request changes, reassign; completed work moves to history

### Domain / community workspace

The accountability container for a business area.

- typical information: the domain's assets, glossary terms, policies, owners and stewards, health
- primary actions: curate assets and terms, manage membership and roles, monitor the domain's state

### Asset page (governance surfaces)

The governance view attached to a data asset — usually the same page the catalog presents, with governance elements on it.

- typical information: owner and stewards, linked policies, certification/trust state, quality and lineage signals, access controls
- primary actions: request access, propose a change, raise an issue, certify (for reviewers)

### Administration / configuration

The platform-configuring surface for governance administrators.

- typical information: domains, roles and permissions, workflow definitions, templates, integrations, feature toggles
- primary actions: build the operating model, publish workflow definitions, manage connectors and users

## Important Rules / Behaviors

### Governance state changes only through governed steps

The platform's central discipline: changes to governance records — policy text, glossary definitions, certifications, access grants — move through the review machinery rather than being edited silently. The steps are attributable to named users and retained as history. This is what makes the platform's output auditable.

### Policies attach to data

A policy that is not linked to the data it governs is a document. The platform's policy records carry explicit links to assets, domains, or data products; those links are what allow policies to be surfaced at the point of use, checked against the estate, and reported on.

### Accountability is explicit and role-differentiated

Every governed object has accountable parties. What each role may do differs: owners decide, stewards curate, reviewers approve, administrators configure, consumers read and request. Products enforce these differences through permission models, and some products allow a domain's visibility to be isolated from general readership for regulatory or legal reasons.

### The catalog is metadata, not data

Governance platforms describe and govern data; they do not hold it. Permissions in the platform govern the governance records and the metadata, not the underlying data itself — access to the data remains with the source systems (with the platform's access machinery acting as the policy and request layer over it).

### Precedence and enrollment rules exist where objects meet multiple processes

An asset or policy can be enrolled in more than one workflow; products define explicit precedence (commonly, the oldest enrollment wins) so that concurrent processes have deterministic outcomes.

## Variants

- **Packaging** — the dominant axis. Governance-first suites (governance as the flagship with a catalog inside), catalog-first products with governance delivered as apps on the catalog, hyperscaler platform components (governance bundled inside a broader security/compliance platform), and data-management-suite service families (governance as one service beside integration, quality, and MDM).
- **Operating-model philosophy** — centralized (the data office governs directly), federated (the office sets rules; distributed owners and stewards govern their areas — explicitly named and structured in mature products), decentralized.
- **Enforcement depth** — advisory posture (policies documented, violations flagged, users guided by trust signals) versus enforced posture (masking, row-level controls, access policies executed at the data layer).
- **Scope** — data assets only versus data plus AI assets (models, agents, AI use cases) — the current era is extending governance scope to AI, and most sampled products now govern AI assets in some form.
- **Regulatory emphasis** — programs shaped by privacy law (GDPR/CCPA-class), industry regulation, or AI regulation; some deployments isolate domains from general visibility for legal reasons.
- **Deployment** — SaaS, self-hosted, and hybrid postures all exist.
- **Customer tier** — enterprise governance programs (the dominant market) versus lighter mid-market deployments; consumption-based pricing appears at the suite pole.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Data Catalog | closest sibling; sold together, often one product | catalog = descriptive inventory + discovery loop (what data exists and what it means); governance = normative rules + accountability + governed processes (how data must be used, who is accountable). Remove the governance machinery → a catalog; remove the discovery inventory → a governance workflow tool. |
| Metadata Management Platform | broader discipline, soft seam | metadata management treats metadata itself as governed enterprise content (standards, models, exchange); the governance platform centers the governance program over the data estate. |
| Data Access Governance | name-collision neighbor | access governance centers the access-decision loop over effective permissions (who can access what, least privilege); the governance platform centers the program (policies, stewardship, compliance) with access machinery as one capability. |
| Data Quality Platform | capability seam | quality platforms center rule/test/monitoring machinery; governance platforms integrate quality as one governed dimension feeding health and compliance views. |
| Data Lineage Platform | capability seam | lineage platforms center capture/tracing depth; governance platforms use lineage for impact and root-cause analysis. |
| Privacy Management Platform | opposite stakeholder, same objects | privacy platforms optimize accountable handling toward individuals and regulators (processing records, obligations, rights requests); governance platforms optimize data use for the organization. Governance translates privacy mandates into data controls. |
| Governance Risk & Compliance Platform | domain-generic umbrella | GRC holds the enterprise risk×control×requirement interlock; data governance is the data-specific program (policies about data, stewards of data, data health). |
| Master Data Management | adjacent | MDM manages the master data records themselves (golden records); governance governs the estate programmatically. Critical-data-element mapping sits at the seam. |
| AI Governance Platform | scope-extension neighbor | AI governance centers the AI-system registry/review lifecycle; data governance platforms extend to AI assets as governed objects — a convergence trend, not a merge. |
| Data Fabric Platform | layer sibling | a fabric spans the estate with integration, governance, and delivery as functions of one metadata layer; the governance platform centers the governance program itself. |

## Representative Products

- Collibra — governance-first data intelligence suite; workflows, policies, stewardship, and a catalog inside one platform
- Informatica (Cloud Data Governance & Catalog) — governance as a service family inside a data-management cloud
- Microsoft Purview (Data Map + Unified Catalog) — hyperscaler-bundled governance with an explicitly federated operating model
- Alation — catalog-first platform with governance delivered as apps on the catalog (Policy Center, Workflow Center, Stewardship Workbench, Governance Dashboard)
- Atlan — modern cloud-native governance as automation and control surfaces on a metadata graph

## Sources

Research date: **2026-09-07**

Primary official surfaces:

- Collibra — Data Governance product page: https://www.collibra.com/us/en/products/data-governance ; workflow publishing documentation: https://developer.collibra.com/workflows/managing-workflows-in-collibra/publish-a-workflow.md
- Informatica — Data & AI Governance, Access and Privacy: https://www.informatica.com/products/data-governance.html ; Cloud Data Governance and Catalog: https://www.informatica.com/products/data-governance/cloud-data-governance-and-catalog.html
- Microsoft Purview — platform overview: https://learn.microsoft.com/en-us/purview/purview ; data governance overview: https://learn.microsoft.com/en-us/purview/data-governance-overview ; data governance roles and permissions: https://learn.microsoft.com/en-us/purview/data-governance-roles-permissions ; Unified Catalog (carried from the same-date data-catalog research): https://learn.microsoft.com/en-us/purview/unified-catalog
- Alation — Data Governance product page: https://alation.com/product/data-governance/ ; Policy Center documentation: https://docs.alation.com/en/latest/steward/PolicyCenter/index.html ; Workflow Center documentation: https://docs.alation.com/en/latest/steward/Workflow/index.html ; documentation index: https://docs.alation.com/en/latest/index.html
- Atlan — documentation root: https://docs.atlan.com/ ; Context Agents Studio: https://docs.atlan.com/product/capabilities/governance/context-agents-studio

> Sourcing limitations: Collibra's product documentation site rendered only its root page on repeated attempts (JavaScript-rendered), so Collibra's deeper governance mechanics rest on its product page and workflow documentation. Informatica's documentation portal was not fetched; its operational mechanics are asserted at product-page strength. Atlan's governance concept pages returned 404 on two attempts; its governance structures are evidenced by its documentation root, the Context Agents Studio page, and same-date fetches recorded in the paired research notes. Precise vendor parameters (numeric limits, plan gating, billing mechanics) are intentionally not stated in this document; they remain in the research notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis against neighboring data-platform Types are recorded in the paired Research Notes.
