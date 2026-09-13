# Research Notes — Data Governance Platform

Research date: 2026-09-07
Leaf: Data Governance Platform (DIRECTORY.md §13 Data, Analytics & AI Systems, line 999)

## Research Goal

Understand what a Data Governance Platform actually is as an Application Type: what its world is made of (the central governance objects), how the governance program is structured and operated, which machinery is definitional vs. merely common in the current market, and where its boundaries lie against neighboring data-platform Types (Data Catalog, Metadata Management, Data Access Governance, Data Quality, Data Lineage, Privacy Management, GRC, MDM, AI Governance, Data Fabric).

## Initial Boundary

Working hypothesis before research:

- Core purpose: make an organization's data governance program operational — hold the rules (policies/standards), assign accountability (stewards/owners), and run the governed processes (requests, approvals, certifications, issue resolution) that keep data trustworthy and compliant.
- Likely central objects: policy records, stewardship/ownership assignments, governance workflows, governance domains/communities, business glossary, governance state (health/compliance scores).
- Likely core loop: establish operating model (domains, roles, policies) → connect the data estate → govern through workflows → enforce/monitor → report evidence.
- Nearest Types: Data Catalog (sharpest seam — recorded flag from that pass), Metadata Management Platform, Data Access Governance (§15), Data Quality Platform, Data Lineage Platform, Privacy Management Platform (§11), Governance Risk & Compliance Platform (§11), Master Data Management, AI Governance Platform (§13), Data Fabric Platform (§13).
- Likely confusions: governance platforms vs. catalogs (suites blur them — governance vendors embed catalogs as their visible surface); "data governance" the practice vs. the software; access governance vs. asset governance (name collision).

## Research Questions

1. What does a governance platform hold as first-class objects? (policies, terms, domains, stewards, workflows, scores?)
2. How is accountability structured (roles, ownership, stewardship assignments, federated operating models)?
3. What governance processes exist as software (change/approval workflows, access requests, certifications, issue management)?
4. How are policies represented, linked to data, and enforced/checked?
5. How is the governed estate represented (embedded catalog? integration? scanning)?
6. How is governance state made visible (dashboards, health scores, compliance evidence)?
7. Which roles use the platform and how do their surfaces differ?
8. Which capabilities are definitional, and which are common-but-not-definitional or optional?
9. What breaks the boundary toward neighboring Types (catalog, access governance, privacy, GRC, quality, lineage, MDM, AI governance)?
10. Does the definition survive the historical check (pre-software governance programs)?

## Representative Products

Selected for market representation, documentation quality, distinct product philosophies, and distinct customer tiers:

| Product | Philosophy / position | Tier |
|---|---|---|
| Collibra | governance-first archetype; "Data Intelligence Platform" with governance as the flagship; workflows + policies + stewardship | large enterprise |
| Informatica (Cloud Data Governance & Catalog, ex-Axon) | data-management-suite-embedded governance; "Data & AI Governance, Access and Privacy" service family | large enterprise |
| Microsoft Purview (Data Map + Unified Catalog) | hyperscaler-bundled governance inside a security+compliance platform; federated operating model | enterprise / Microsoft estates |
| Alation | catalog-first with governance delivered as apps on the catalog (Policy Center, Workflow Center, Stewardship Workbench, Governance Dashboard) | large enterprise |
| Atlan | modern cloud-native "context layer for AI" pole; governance as automation + control surfaces on a metadata graph | mid-market to enterprise |

## Sources

Tier 1/2 official surfaces fetched 2026-09-07:

- Collibra
  - Product page: https://www.collibra.com/us/en/products/data-governance (Tier 2; includes vendor FAQ defining data governance and the four feature pillars)
  - Workflow publishing doc: https://developer.collibra.com/workflows/managing-workflows-in-collibra/publish-a-workflow.md (Tier 1; BPMN/ZIP workflow definitions, Workflow Administration permission)
  - Limitation: docs.collibra.com specific pages (operating model, About) returned the JS-rendered docs root on two attempts; abandoned per network rules. Deeper governance-machinery claims for Collibra rest on the product page + the workflow doc + the data-catalog pass's Collibra evidence.
- Informatica
  - Product page: https://www.informatica.com/products/data-governance.html (Tier 2; "Data & AI Governance, Access and Privacy"; FAQ definitions incl. the DAG distinction)
  - Product page: https://www.informatica.com/products/data-governance/cloud-data-governance-and-catalog.html (Tier 2; CDGC capabilities)
  - Limitation: docs.informatica.com not fetched; operational mechanics asserted at product-page strength.
- Microsoft Purview
  - https://learn.microsoft.com/en-us/purview/purview (Tier 1; platform overview)
  - https://learn.microsoft.com/en-us/purview/data-governance-overview (Tier 1; governance hub, federated approach, roles, workflow at a glance)
  - https://learn.microsoft.com/en-us/purview/data-governance-roles-permissions (Tier 1; full role model incl. data-asset lifecycle example)
  - Carried from the data-catalog pass (same date): https://learn.microsoft.com/en-us/purview/unified-catalog (governance domains, data products, glossary terms, CDEs, access policies, data quality, health management, OKRs)
- Alation
  - Product page: https://alation.com/product/data-governance/ (Tier 2; Trust Flags, Policy Center, Workflow Automation, Catalog Sets, AI governance; FAQ with the catalog-vs-governance seam and the Forrester definition)
  - Policy Center doc: https://docs.alation.com/en/latest/steward/PolicyCenter/index.html (Tier 1; two policy types, policy catalog pages, policy change workflows)
  - Workflow Center doc: https://docs.alation.com/en/latest/steward/Workflow/index.html (Tier 1; change management/approval workflow model, roles, history)
  - Docs index: https://docs.alation.com/en/latest/index.html (Tier 1; Governance App structure, Domains, Curation Automation, CDE Management)
  - Limitation: help.alation.com is JS-rendered (known from the catalog pass); docs.alation.com (customer-managed docs) used instead.
- Atlan
  - Docs root: https://docs.atlan.com/ (Tier 1; current structure, governance nav)
  - Context Agents Studio: https://docs.atlan.com/product/capabilities/governance/context-agents-studio (Tier 1; AI enrichment agents, Governance Admin role, collections/coverage)
  - Limitation: /product/capabilities/governance and /governance/concepts/what-are-purposes returned 404 on two attempts; abandoned per network rules. Atlan governance structures (domains, Purposes, playbooks, data contracts, certificates) carried from the data-catalog pass's same-date fetches.

Evidence layers: A = directly observed on the cited official page; B = cross-product commonality; C = canonical inference.

## Product A — Collibra

### Key observations (Layer A unless noted)

- Product framing: "Collibra Data Governance automates workflows and centralizes policies to create a single source of truth. Operationalize your strategy, ensure regulatory readiness and unlock data value."
- Four feature pillars (product page):
  1. **Create a shared language** — "Align the entire organization around a single, approved source of truth for all business terms"; business glossary; find and understand data with context; collaboration and data literacy.
  2. **Assign clear accountability** — "Assign roles and responsibilities to protect data assets"; granular role-based access controls; "establishing clear ownership and access policies."
  3. **Manage and enforce policies** — "automating compliance checks and flagging violations"; "Automatically validate that data assets meet predefined rules and policy conditions in real-time"; "Provide evidence of compliance during audits with a clean overview of policy adherence."
  4. **Automate stewardship** — AI-driven automation and workflows for curation, classification, governance tasks; auto-generated descriptions; automatic classification.
- Additional capabilities: **Flexible operating model** ("Configure domains and communities in Collibra to align with your organization's unique structure"); **Embedded collaboration** ("embedding workflows into Slack and Microsoft Teams"); **Usage analytics** (platform and asset usage to drive adoption); **Data Helpdesk** ("Proactively manage data issues by submitting, tracking and resolving them with automated incident workflows").
- Vendor FAQ (Tier 2): "Data governance is the system of policies, processes and roles designed to ensure an organization's data is accurate, trustworthy, consistent and available. It's the framework for managing and protecting data assets." Also distinguishes data governance (strategic framework for policies, roles, responsibilities) from data management (technical execution).
- Workflow machinery (Tier 1, developer docs): workflows are BPMN/ZIP/bpmn20-XML definitions authored in Workflow Designer and published to the platform; publishing requires a global role with **Workflow Administration** or System administration permission; uploading a workflow with the same process ID replaces the existing one; two workflows cannot share a display name.
- From the data-catalog pass (same date, product page): catalog positioned inside the "Data Intelligence Platform"; trust signals framed as "Data Confidence"; certification of trustworthy data; data products; data contracts and sharing agreements; Data Marketplace; AI Copilot; 100+ integrations; automated classification incl. PII/PHI labeling.

## Product B — Informatica (Cloud Data Governance & Catalog)

### Key observations

- Service family framing: "Data & AI Governance, Access and Privacy — Secure, manage and govern data" (one of the IDMC cloud services beside Data Catalog, Data Integration, Data Quality & Observability, MDM & 360, Data Marketplace).
- Value props: "Deliver trusted outcomes with AI-powered data governance"; accelerate decision-making (reliable data for human and AI agents); save time (AI-assisted data stewardship); scale and reduce compliance risks ("automated policy management and enforcement").
- Features: visibility into data sources **and AI models** for trusted insights; align business and technical users on data strategy (metadata linked with business context); integrate governed data quality and observability (profiling statistics, scorecards from a single pane); share AI-ready data products through a governed marketplace with policy-based access; CLAIRE AI engine to simplify and automate governance processes.
- CDGC product page: "Inventory, control, deliver and observe data and AI assets across complex environments with AI-powered capabilities"; unified view (centralized catalog, clear lineage, shared business context); mitigate risk exposure (policy automation); AI-powered data classification; browsable hierarchical views; automated lineage.
- Related products listed: Cloud Data Governance and Catalog, Cloud Data Marketplace, Cloud Data Quality and Observability, **Data Access Management** (de-identify sensitive data) — the suite splits access machinery into its own product.
- Vendor FAQ (Tier 2): "Data governance is a set of principles, standards and practices to help ensure your data is reliable, consistent and trustworthy. It involves establishing frameworks with policies and procedures that guide the creation, use and maintenance of data safely, securely and responsibly."
- Vendor FAQ explicitly separates **data access governance**: "a security and compliance discipline focused on managing, monitoring and enforcing who can access specific datasets, under what conditions and for what purpose… enforces policies like least privilege, RBAC and dynamic data masking down to individual rows and columns."
- Vendor FAQ on privacy/compliance: governance "translat[es] complex legal mandates (such as GDPR, CCPA and HIPAA) into enforceable, automated technical controls… discovers and classifies sensitive personal data (PII), enforces strict access restrictions and automates lifecycle rules like data retention and deletion."
- Market-category evidence: "Informatica is named a Leader — The Gartner® Magic Quadrant™ for Data & Analytics Governance Platforms marks its first-ever release." (Category name confirms the market label.)
- Heritage note: the governance service descends from Axon Data Governance (on-prem era); current cloud form is CDGC. (Positioning-level; not asserted as operational detail.)

## Product C — Microsoft Purview (Data Map + Unified Catalog)

### Key observations

- Platform framing: Purview = data security + data governance + data compliance solutions in one portal. Data governance solutions = **Data Map** + **Unified Catalog**.
- Governance hub (Tier 1): "Data governance ensures that the data you use in your business operations, reports, and analysis is discoverable, accurate, trusted, and protected. With ever-evolving regulations combined with the proliferation of AI and regulations for AI, data governance is as critical as data security."
- Structural note: "All data in Data Map and Unified Catalog is **metadata**, not the underlying data itself. None of the permissions or roles in Data Map or Unified Catalog provide access to underlying data itself."
- **Federated approach** (Tier 1): "A federated approach to data governance is a middle ground between a centralized and a decentralized approach. An organization's central data office sets the rules, while individuals in various roles and departments who use the data and understand its function are entrusted to govern that data appropriately."
- Role framing (Tier 1): Central data office (establishes and ensures governance policies, active metadata, compliance, insights into overall governance health); Data consumers (find and use trusted datasets through streamlined access request workflow); Data owners (register data assets, manage classifications and access, ensure quality standards); Data stewards (quality, discovery, glossary, consistency, lineage; work with central data office).
- Key capabilities (Tier 1): comprehensive visibility (Unified Catalog with AI-enabled recommendations; data products; actionable oversight tracking data health); data confidence (governance domains; lineage; data quality experiences); responsible innovation (role-based access controls; simplified access and discovery; analytics export).
- Workflow at a glance (Tier 1): 1. Assign a Data Governance Administrator; 2. Use Data Map to scan assets and multicloud sources to capture metadata; 3. In Unified Catalog, build governance domains and curate data products; 4. Connect data with business concepts (OKRs, glossary terms); 5. Improve data quality and remove data issues to improve data health.
- Role model (Tier 1, roles page): tenant role groups (Purview Administrators, Data Source Administrators, Data Governance); catalog-level roles (Data Governance Administrator, Data Health Owner/Reader, Global Asset Curator, Global Catalog Reader, Governance Domain Creator); governance-domain-level roles (Governance Domain Owner, Data Product Owner, Data Steward, Data Quality Steward/Reader, Data Profile Steward/Reader, Governance Domain Reader, Local Catalog Reader). **Local Catalog Reader** exists specifically to limit a governance domain "to meet regulatory or legal requirements."
- Data-asset lifecycle example (Tier 1): register source → scan → curate and certify → create governance domain → create data product → add asset to product → **add access policy to the data product** → users search → **user requests access** → view data health insights.
- From the data-catalog pass (same date, unified-catalog page): governance domains ("a boundary that aligns your data estate to your organization… a mini catalog inside Unified Catalog"); data products; glossary terms as active objects that can carry policies; critical data elements (quality rules and access policies attach to CDEs); self-service access requests; data quality scores at asset/product/domain levels; health management (health controls, health actions, scores); OKRs linking data products to business objectives.

## Product D — Alation

### Key observations

- Product framing: "Alation Data Governance enforces access, policy, and compliance across every system, for every consumer, people, and agents alike." "Govern once. Trust everywhere."
- Value props: eliminate data silos (single source of truth); stay compliant with evolving regulations ("automated workflows and policy management tools"); ensure high-quality data (lineage, curation, quality controls).
- Compliance machinery: **Trust Flags** ("lead users to trusted data with linked policies, ensuring they use the right information compliantly"); **Policy Center** ("Keep all policies organized and accessible"); **Workflow Automation** ("Assign and track tasks like policy updates and renewals"); **Catalog Sets** ("classify new data and apply the right policies"); row-level access controls and dynamic masking; AI governance (track and document AI models, training data, ethics-policy compliance).
- **Policy Center** (Tier 1 doc): component of the **Data Governance App**; "surfaces business policies created in the catalog and data policies extracted from Snowflake data sources, enabling data consumers to view applicable policies and understand their impact in a single place." Two policy types:
  - **Data Policies** — extracted directly from the database (currently Snowflake: Row Access and Dynamic Data Masking policy types); surfaced as catalog objects with their own pages.
  - **Business Policies** — "created and managed manually in the Policy Center… data-source agnostic and can be used to capture and manage policy information regardless of the underlying system"; linked to other catalog objects using Object Set fields.
  - Policy objects have catalog pages based on a (customizable) policy template; Server/Catalog Admins can deploy **change management workflows for policies**; users suggest changes to policy catalog fields.
- **Workflow Center** (Tier 1 doc): part of the Data Governance App; "a collaboration tool enabling users to view, create, and manage data governance workflows"; supports workflows for **change management and approval** for data objects in the Catalog; users suggest changes to built-in and custom fields on catalog pages; objects can be enrolled in any number of workflows (oldest takes precedence); reviewers approve/reject from the **Tasks** tab in their inbox; on approval, changes are applied to the fields; "The history of changes, reviews, and approvals is stored in the corresponding workflow and the Workflow Center"; the workflow name appears under Properties on the object page. Roles: Workflow Creators (Server/Catalog Admin), Workflow Reviewers (designated), other catalog users (suggest changes).
- Governance App structure (docs index): Policy Center, Workflow Center, Stewardship Workbench, Governance Dashboard (from the catalog pass's product-page evidence); Domains; Curation Automation ("AI-powered curation capability that automates governance rather than relying on manual processes" — under "Outcome-Based Governance"); CDE Management ("define, standardize, and monitor critical data elements").
- Vendor FAQ (Tier 2) — the catalog-vs-governance seam in the vendor's own words: "While a catalog shows what data exists, governance defines how it should be used, who has access, and how compliance is enforced. Together, these capabilities ensure data is trusted, contextualized, and well-managed."
- Vendor FAQ on solution composition: "A comprehensive solution includes policy management, access controls, workflow automation, stewardship tools, lineage tracking, and monitoring for compliance. It should also integrate with or be supported by data catalogs and quality solutions."
- Forrester definition cited by the vendor: data governance = "software and services that help manage data policies, quality, and compliance. Aspects include data definitions, policies, quality, stewardship, literacy, regulatory compliance, ethics, risk management, privacy, security, and end-to-end lifecycle management."

## Product E — Atlan

### Key observations

- Positioning (docs root): "the context layer for AI — connect your data estate, capture your business knowledge, and make it available to every AI tool you run." Governance nav item: Context Agents Studio.
- **Context Agents Studio** (Tier 1): "Automate metadata enrichment at scale using AI-powered context agents that generate descriptions, READMEs, and SQL intelligence across your most important data assets." Framing: "Most data catalogs fail not because they lack the right tools—but because keeping metadata current is too slow and manual to scale." Agents analyze usage signals (query history, lineage, BI activity) to generate descriptions/READMEs/SQL intelligence; coverage % tracked per attribute across collections; enrichment triggered across collections at scale. Roles: **Admin** and **Governance Admin** (full access).
- From the data-catalog pass (same date): governance capabilities include tags for sensitive data, granular access control ("**Purposes**"), **data contracts**, **playbooks** automating metadata enrichment, **domains** as organizational structure, **certificates** (Verified / Draft / Deprecated) as first-class trust states and filters; Enterprise Data Graph as the metadata substrate; MCP server exposing governed context to AI tools.

## Cross-product Comparison

| Dimension | Collibra | Informatica CDGC | Microsoft Purview | Alation | Atlan | Strength |
|---|---|---|---|---|---|---|
| Policies/rules as managed first-class objects | A (centralized policies; compliance checks) | A (policy automation) | A (policies on data products/CDEs; access policies) | A (Policy Center: business + data policies as catalog objects) | (Purposes/contracts; policy objects not directly fetched) | B — universal |
| Policies linked to the data they govern | A (policy adherence per asset) | A (policy-based access on products) | A (policies attach to data products/CDEs) | A (Object Set links; policies on catalog objects) | (Purposes on assets) | B — universal |
| Accountability structure (owners/stewards assigned) | A ("assign clear accountability"; roles/responsibilities) | A (AI-assisted stewardship) | A (owners/stewards roles; federated model) | A (stewardship tools; stewards create/curate) | A (Governance Admin; owners filter) | B — universal |
| Org-aligned containers (domains/communities) | A (domains and communities) | (hierarchical views; business-context linking) | A (governance domains) | A (Domains) | A (domains) | B — universal |
| Business glossary / shared vocabulary | A ("create a shared language"; approved source of truth for business terms) | A (metadata linked with business context) | A (glossary terms; OKRs) | A (Glossary Hub; business glossary) | A (terms linked to assets) | B — universal |
| Governed processes as workflows | A (BPMN workflows; Workflow Administration; Slack/Teams embedding) | A (AI-assisted governance processes; policy automation) | A (access request workflow; health actions) | A (Workflow Center: suggest → review → approve → apply, with history) | (playbooks; certificates workflow) | B — universal in mature products |
| Change/approval machinery on governance objects | A (workflow definitions replaceable by process ID) | (not detailed on fetched pages) | (health actions; not a generic change workflow on fetched pages) | A (change management workflows for policies and catalog objects) | (not directly fetched) | B — common, depth varies |
| Compliance checking / violation flagging | A (automated compliance checks; flagging violations; audit evidence) | A (automated policy management and enforcement) | (health controls/actions; quality scores) | A (Trust Flags linked to policies; compliance tasks) | (certificates; not directly fetched) | B — common |
| Governance state visible (dashboards/health/scores) | A (usage analytics; policy adherence overview) | A (scorecards from a single pane) | A (health management; OKRs; data health insights) | A (Governance Dashboard) | A (coverage % tracking) | B — universal |
| Embedded catalog / metadata inventory as substrate | A (catalog inside the platform) | A (CDGC = governance + catalog) | A (Data Map + Unified Catalog) | A (catalog is the substrate; governance apps on it) | A (Enterprise Data Graph) | B — universal |
| Automated harvesting/classification of the estate | A (AI classification; integrations) | A (AI-powered classification) | A (Data Map scanning) | A (Catalog Sets; connectors) | A (crawlers) | B — universal in modern products |
| Certification / trust states on assets | A (certification; Data Confidence) | (trusted insights framing) | A (curate and certify in lifecycle example) | A (Trust Flags) | A (Verified/Draft/Deprecated certificates) | B — common |
| Access machinery (policies, requests, masking) | A (access policies; role-based access controls) | A (Data Access Management as sibling product; masking) | A (access policies on products; self-service access requests) | A (row-level controls, dynamic masking; Trust Flags gate use) | A (Purposes) | B — common; depth and packaging vary |
| Data quality integration | (DQ&O as sibling product) | A (governed DQ and observability; scorecards) | A (data quality experiences; scores) | A (Open Data Quality Framework; ADQ) | (via observability sources) | B — common |
| Lineage | A (Data Lineage product) | A (automated lineage) | A (lineage capability) | A (data lineage) | A (lineage) | B — common |
| Data issue management | A (Data Helpdesk: submit/track/resolve with incident workflows) | (not on fetched pages) | A (remove data issues to improve health) | (not on fetched pages) | (not on fetched pages) | B — common, not universal on fetched evidence |
| Data products / marketplace layer | A (Data Marketplace; data products) | A (governed marketplace; policy-based access) | A (data products) | A (Data Products App + Marketplace) | A (data products capability) | B — emerging common layer |
| AI-asset governance (models/agents as governed objects) | A (AI Governance product; AI Command Center) | A ("data and AI assets"; visibility into AI models) | (AI-era framing; DSPM sibling) | A (AI governance: track/document models) | A (context for AI agents; MCP) | B — era-current extension |
| AI assistance over governance work | A (auto-generated descriptions; classification) | A (CLAIRE; AI-assisted stewardship) | A (AI-enabled recommendations; Security Copilot) | A (ALLIE; Curation Automation) | A (Context Agents) | B — universal in 2026 samples; recent-era |
| Programmatic APIs | A (developer portal) | (implied) | (Data Map ops; APIs implied) | A (REST APIs) | A (API/MCP) | B — common |
| Federated operating-model support | A (domains/communities configurable) | (business/technical alignment framing) | A (federated approach named and structured) | A (stewardship distributed across domains) | A (domains) | B — common |
| Regulatory/legal scoping of governance visibility | (role-based access controls) | (privacy/compliance use case) | A (Local Catalog Reader for regulatory/legal isolation) | (policy permissions) | (not directly fetched) | B — emerging, product-specific depth |

## Canonical Abstraction (for synthesis only — not for final doc)

### L0 — Defining Invariant (deliberately minimal)

1. **Governance rules held as managed records attached to the data they govern** — the organization's policies/standards/rules for data and its use exist as first-class, linkable objects (not just documents), connected to representations of the data assets they apply to.
2. **Accountability structure over data** — named stewards/owners assigned to data areas/assets through an organization-aligned structure (domains/communities/governance domains); the responsibility map that makes governance someone's job.
3. **Governed processes that change governance state through attributable, reviewable steps** — the machinery through which governance objects and data standing change (requests, approvals, certifications, issue resolution), with the steps recorded and reviewable — retained as history.

Removal tests:
- Drop (1) → a stewardship directory + task tool; the normative layer (what data must/must not be) is gone.
- Drop (2) → a policy library with workflows but no accountable parties; governance stops being an organization program and becomes document management.
- Drop (3) → static policy/steward documentation; a governance framework, not an operational platform. (This is the seam the data-catalog pass recorded: "remove policy workflows → pure catalog" inverted.)

### Historical / market-sample check

- Pre-software data governance (DAMA/DMBOK era, 1990s–2000s): a governance council with named roles (accountability structure), policy/standards documents in a binder or intranet (policy records), and governance processes run through meetings, change boards, and email approvals (governed processes, manually executed) — with policy registers and minutes as the evidence trail — satisfies the minimal core.
- Therefore: workflow engines, BPMN designers, embedded catalogs, automated harvesting, AI classification, health scores, OKRs, data products, marketplaces, access-request self-service, AI copilots are all **NOT definitional** — L1/L2. The historical check passes.
- Conversely, a pure metadata inventory with search but no rules/accountability/processes is a catalog (the sibling Type), not a governance platform — supports keeping the normative+accountability+process triple as the invariant.

### L1 — Common Mature Structure

- Embedded catalog / metadata inventory as the governed-estate substrate (governance objects attach to asset records harvested from source systems).
- Automated harvesting and classification of the estate (connectors/scanners; AI-assisted classification incl. sensitive-data labeling).
- Business glossary / shared vocabulary (terms, definitions) linked to assets — the "single approved source of truth for business terms."
- Domains/communities/governance domains as org-aligned containers scoping accountability and visibility.
- Certification/trust states on assets (certified data, trust flags, confidence scores) with review workflows.
- Compliance checking and violation flagging (automated validation of assets against policy conditions; audit-evidence views).
- Access machinery: access policies, self-service access requests, masking/row-level controls (capability seam toward Data Access Governance).
- Data quality integration (scores, rules, profiling — capability seam toward Data Quality Platform).
- Lineage (capability seam toward Data Lineage Platform).
- Governance state surfaces: dashboards, health scores, OKRs, usage analytics; data-issue management (helpdesk/incident workflows).
- Role model: governance admin, domain owner, data owner, data steward, data consumer/reader; federated operating-model support (central office sets rules, distributed stewards execute).
- Data products / marketplace layer (publish/consume governed bundles) — emerging common layer.
- AI assistance over governance work (suggested descriptions, classification, copilots, enrichment agents) — universal in the 2026 sample but recent-era; not definitional.
- APIs/programmatic access; embedded collaboration surfaces (Slack/Teams).

### L2 — Variant / Optional Structure

- Packaging: standalone governance suite vs. catalog-first with governance apps vs. hyperscaler platform component vs. data-management-suite service family.
- Governance philosophy: centralized vs. federated vs. decentralized operating models (Purview names and structures the federated middle).
- Enforcement depth: advisory (policies documented, violations flagged) vs. enforced (masking, row-level controls, access policies executed).
- Scope: data assets only vs. data + AI assets/models (era-current extension).
- Regulatory regime emphasis (GDPR/CCPA/HIPAA-driven programs; regulatory isolation of domains).
- Deployment: SaaS vs. self-hosted; tenancy models.
- Customer tier: enterprise governance programs vs. mid-market/lighter deployments.
- Consumption/pricing models (consumption-based pricing at one vendor).

### L3 — Vendor-specific (research notes only)

- Collibra: "Data Confidence" branding; Workflow Designer (BPMN apps, process-ID replacement rule, display-name uniqueness); Data Helpdesk; Control Tower; AI Command Center; communities/domains operating model; University/community ecosystem.
- Informatica: CLAIRE AI engine; CDGC naming (Axon heritage); "Data & AI Governance, Access and Privacy" service-family framing; Data Access Management as a separate product; consumption-based pricing; "catalog of catalogs" e-book framing.
- Microsoft Purview: Data Map/Unified Catalog naming; OKRs; health controls/actions/scores; Local Catalog Reader for regulatory isolation; capacity-unit billing (from the catalog pass); free vs. enterprise account types; Power BI metadata promotion; Security Copilot.
- Alation: Governance App (Policy Center / Workflow Center / Stewardship Workbench / Governance Dashboard); Trust Flags; Catalog Sets; Outcome-Based Governance / Curation Automation; CDE Management; Snowflake data-policy extraction (Row Access / Dynamic Data Masking); oldest-workflow-precedence rule; Creator/Explorer/Viewer license tiers (from the catalog pass).
- Atlan: Context Agents Studio (collections, coverage %, credit usage); Purposes; playbooks; data contracts; Enterprise Data Graph; Governance Admin role; MCP server; certificates (Verified/Draft/Deprecated).

## Rejected Findings

Considered and rejected as definitional (with reasons):

- **Embedded catalog / discovery inventory** — the sibling Type's defining core; governance platforms embed or integrate it as substrate (→ L1). The data-catalog pass recorded the seam from its side; this pass holds it from the governance side.
- **Automated harvesting/classification** — manual policy registers and steward rosters satisfy the core (→ L1).
- **Business glossary** — universal but a vocabulary layer, not the governance machinery itself (→ L1).
- **Workflow engines/BPMN** — the governed-process invariant is the attributable-reviewable-step pattern, not any specific engine; manual change boards satisfy it (→ L1 as implementation, L0 keeps the pattern).
- **Compliance checking/violation flagging** — common and important but advisory-depth varies; enforcement is a variant posture (→ L1).
- **Access machinery (policies/requests/masking)** — capability seam toward Data Access Governance; present in all sampled products but packaging and depth vary (→ L1).
- **Quality/lineage integration** — sibling Types' cores; integrated as capabilities (→ L1).
- **Health scores/OKRs/dashboards** — visibility surfaces over the records (→ L1).
- **Data products/marketplace** — emerging packaging layer (→ L1/L2).
- **AI-asset governance** — era-current extension of scope (→ L2).
- **AI assistance** — 2023+; historical check excludes from definition (→ L1/L2).
- **Cloud delivery** — on-prem/self-hosted governance platforms are first-class (→ L2).
- **Federated operating model** — one named philosophy among several (→ L2).

## Boundary Findings

- **vs. Data Catalog** — the sharpest seam, recorded from the catalog side ("governance organizes policy, stewardship organization, compliance workflows over the estate; the catalog supplies the inventory and discovery those processes act on"). Vendor-stated from this side (Alation FAQ): "While a catalog shows what data exists, governance defines how it should be used, who has access, and how compliance is enforced." Structural test: the catalog's objects are descriptive (what the data is/means); the governance platform's objects are normative and operational (what must hold, who is accountable, which processes change state). Removal tests: remove policy/stewardship/workflow machinery → pure catalog; remove the discovery inventory → governance workflow tool. Market reality: governance-first suites embed catalogs as their visible surface (Collibra, Purview, Informatica CDGC), and catalog-first products add governance apps (Alation) — heavy product overlap, both leaves stand on the primary object of work.
- **vs. Metadata Management Platform** — metadata management is the broader discipline (metadata itself as governed enterprise content: standards, models, exchange); the governance platform centers the governance program (rules/accountability/processes) over the data estate. Soft seam; governance platforms consume/manage metadata without making metadata-as-content the primary object. Recommend joint review when that leaf is processed.
- **vs. Data Access Governance (§15)** — Informatica's own FAQ draws it: DAG = "a security and compliance discipline focused on managing, monitoring and enforcing who can access specific datasets" (least privilege, RBAC, masking to row/column); data governance = the broader program (policies, quality, stewardship, compliance). Access machinery appears inside governance platforms (access policies, access requests, masking) as a capability; the DAG Type centers the access-decision loop over effective permissions. Name collision on the "data governance" umbrella documented from both sides.
- **vs. Data Quality Platform** — quality is one governed dimension; governance platforms integrate/surface quality scores and rules; dedicated quality platforms center the rule/test/monitoring machinery. Seam: quality rules as the primary object vs. quality as one governed dimension feeding compliance/health views.
- **vs. Data Lineage Platform** — lineage is a capability inside governance platforms (impact analysis, root cause); dedicated lineage platforms center capture/tracing depth at pipeline granularity.
- **vs. Privacy Management Platform (§11)** — consistent with that pass's recorded seam: governance/catalog optimize data *use* for the organization (findability, quality, stewardship); the privacy platform optimizes *accountable handling* toward individuals and regulators (processing records, obligations, rights requests). Same data objects, opposite stakeholder. Governance platforms translate privacy mandates into data controls (Informatica FAQ) — a capability seam, not a merge.
- **vs. Governance Risk & Compliance Platform (§11)** — the GRC pass recorded provisionally: "data-specific stewardship/quality/catalog machinery; not the GRC record core." Confirmed from this side: governance platforms may map policies to compliance frameworks and produce audit evidence, but the record core is data-specific (policies about data, stewards of data, data health) rather than the enterprise risk×control×requirement interlock.
- **vs. Master Data Management** — MDM manages the master data records themselves (golden records); the governance platform governs the estate programmatically. CDE management (mapping "Customer ID" across systems) sits at the seam.
- **vs. AI Governance Platform (§13)** — AI governance centers the AI-system registry/review lifecycle (use cases, models, agents with risk/review state); data governance platforms extend to AI assets (Informatica "data and AI governance"; Collibra AI Governance product; Alation AI governance; Atlan context-for-AI) — convergence documented as scope extension, not merge. The ai-governance pass's own boundary (organizational control plane over AI systems) remains distinct from the data-estate program.
- **vs. Data Fabric Platform** — the fabric pass listed governance as a single-function layer sibling: fabric = estate-spanning unified metadata layer with integration+governance+delivery as functions of one system; the governance platform centers the governance program itself. A fabric includes governance machinery; a governance platform is not a fabric.
- **"去掉什么就变成另一个 Type" tests**:
  - Remove rules/accountability/processes, keep inventory+discovery → Data Catalog.
  - Center on the access-decision loop over effective permissions → Data Access Governance.
  - Center on personal-data processing records + obligations + rights → Privacy Management Platform.
  - Center on quality rules/tests/monitoring → Data Quality Platform.
  - Center on metadata as governed content (standards/exchange) → Metadata Management Platform.
  - Center on golden records → Master Data Management.
  - Center on AI-system registry/review → AI Governance Platform.
  - Center on domain-generic risks/controls/requirements → GRC Platform.

## Uncertainties

- Collibra's operational documentation (operating model, stewardship internals) was not reachable (JS-rendered docs root on two attempts); its deeper workflow/stewardship mechanics are asserted at product-page + workflow-doc strength only.
- Informatica's docs portal was not fetched; CDGC operational mechanics (workflow specifics, policy object model) rest on product-page evidence.
- Atlan's governance concept pages (Purposes, playbooks) 404'd on two attempts; those structures are carried from the data-catalog pass's same-date fetches and the Context Agents Studio page.
- The exact edge between this leaf and Metadata Management Platform is genuinely soft in the market; flagged for joint review.
- Data-issue management (helpdesk/incident workflows) was directly evidenced at two products (Collibra Data Helpdesk, Purview health actions); treated as common-not-universal.
- Whether "governed processes" must include a formal workflow engine was resolved by the historical check (manual change boards satisfy the pattern); modern workflow automation is documented as the dominant implementation, not the invariant.
- AI-asset governance is expanding fast (all five sampled products now govern AI models/agents in some form); whether it stays a scope variant or hardens into its own requirement is left open.

## Final Synthesis

A Data Governance Platform is the application that makes an organization's data governance program operational. Its defining structure is a triple: governance rules held as managed records attached to the data they govern (policies/standards as first-class, linkable objects — not just documents); an accountability structure over data (named stewards and owners assigned across an organization-aligned structure of domains); and governed processes that change governance state through attributable, reviewable steps (requests, approvals, certifications, issue resolution — retained as history). Everything else that modern products pile on — the embedded catalog, automated harvesting and classification, business glossaries, certification and trust flags, compliance checks, access controls, quality scores, lineage, health dashboards, OKRs, data products, AI copilots — enriches the program but does not define it. The platform's reason to exist is the gap between having a governance framework on paper and actually operating one: rules that are linked to data, people who are accountable for it, and processes that keep both current — with the state of the program visible and auditable.
