# Research Notes — Internal Developer Portal

## Research Goal

Understand the **Internal Developer Portal** as an Application Type: what exists inside it, who uses it, how work flows through it, and where its boundaries lie — above all against the sibling Type **Internal Developer Platform / IDP** (§12, processed 2026-09-08, joint-review flag pre-hung in STATUS.md), and against Developer Documentation Portal (§12, processed), API Management Platform's "developer portal" surface (§12, processed), CMDB, Engineering Productivity Analytics, Intranet/Employee Portal, Enterprise Wiki, and Project Scaffolding / Code Generator.

Special difficulty: this is the market's sharpest vocabulary seam. "IDP" and "internal developer portal" are used interchangeably in marketing, while engine-pole vendors explicitly split them. The IDP pass proposed the seam and left the portal side to this pass: *portal centers the developer-facing surface (catalog/scorecards/docs/scaffolding; integrates with other tools; does not hold deployment state); IDP centers the provisioning machinery of record.* This pass must confirm, refine, or correct that seam from portal-side evidence.

## Initial Boundary

Working hypothesis before research:

- Core use: one place where an organization's developers find every piece of software, who owns it, how it scores against standards, and where they act (scaffold new services, trigger operations) without jumping between tool UIs.
- Primary users: application developers (consumers); platform engineering (configurers); engineering leaders/SREs/security (governance consumers).
- Nearest neighbors: **Internal Developer Platform** (machinery vs surface), **Developer Documentation Portal** (external-facing docs corpus), **API Management developer portal** (API-consumer surface), **CMDB** (IT-facing inventory), **Engineering Productivity Analytics** (measurement-centric).
- Unknowns: is the catalog definitional or merely universal? Is self-service action definitional or common? Does "does not hold deployment state" hold for every sampled product? How does the era-current AI layer (agents, MCP) affect the seam?

## Research Questions

1. What are the core objects? (catalog, entity, ownership, template/scaffolder, action/workflow, scorecard, integration)
2. Who does what: what does the platform team configure, what do developers consume, what do leaders consume?
3. What is the canonical workflow from "portal configured" to "developer finds and acts"?
4. Where does the data come from — and where do actions execute? Is the portal ever the provisioning machinery?
5. What is the exact seam vs the IDP (sibling)? Does the proposed "surface vs machinery" seam hold from portal-side evidence?
6. What is the seam vs Developer Documentation Portal, API-management developer portal, CMDB, wiki, intranet?
7. Would older/analog forms (wiki service directories, template repos, manual standards audits) still fit the definition?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer tiers:

| Product | Pole | Evidence depth |
|---|---|---|
| Backstage | open-source framework you assemble and host yourself; the category's archetype (Spotify lineage, CNCF) | Tier 1 (backstage.io docs: what-is, software-catalog, software-templates) |
| Port | SaaS portal platform; config-driven data model (blueprints/entities); catalog + self-service actions + scorecards | Tier 1 (docs.port.io: overview, glossary) |
| Cortex | SaaS portal; engineering-excellence/standards-first philosophy (scorecards, initiatives, workflows) | Tier 1 (docs.cortex.io: readme, workflows, scorecards) |
| OpsLevel | SaaS portal; mid-market; catalog-engine + rubrics/checks + actions | Tier 1 (docs.opslevel.com: introducing-opslevel) |

Companion evidence from the sibling pass (fetched 2026-09-08, Tier 1): Humanitec's "How Humanitec relates: Backstage, Port, Cortex etc." — the terminology-defining vendor's own portal definition. Combined portal+platform packaging (Cycloid) documented in the sibling research notes.

## Sources

All fetched 2026-09-08:

- Backstage — "What is Backstage?" (https://backstage.io/docs/overview/what-is-backstage/), "Backstage Software Catalog" (https://backstage.io/docs/features/software-catalog/), "Backstage Software Templates" (https://backstage.io/docs/features/software-templates/)
- Port — docs overview (https://docs.port.io/), Glossary (https://docs.port.io/glossary/)
- Cortex — documentation readme (https://docs.cortex.io/), Workflows (https://docs.cortex.io/streamline/workflows.md), Scorecards overview (https://docs.cortex.io/standardize/scorecards.md)
- OpsLevel — "Introducing OpsLevel" (https://docs.opslevel.com/docs/introducing-opslevel)
- Humanitec — "How Humanitec relates: Backstage, Port, Cortex etc." (https://developer.humanitec.com/platform-orchestrator/docs/humanitec-vs-others/backstage-port-cortex-etc./) — fetched by the sibling IDP pass, 2026-09-08
- Not directly accessible: Gartner/analyst definitions of "internal developer portal" (same limitation as the IDP pass); platformengineering.org wiki 404'd in the sibling pass.

## Product Observations

### Backstage (open-source framework pole) — Evidence A

- Self-description: "Backstage is an open source framework for building developer portals. Powered by a centralized software catalog, Backstage restores order to your microservices and infrastructure…" "Backstage unifies all your infrastructure tooling, services, and documentation to create a streamlined development environment from end to end."
- Out of the box: **Software Catalog** ("for managing all your software (microservices, libraries, data pipelines, websites, ML models, etc.)"), **Software Templates** ("quickly spinning up new projects and standardizing your tooling with your organization's best practices"), **TechDocs** ("docs like code"), plus an open-source plugin ecosystem.
- Catalog mechanics: "a centralized system that keeps track of ownership and metadata for all the software in your ecosystem"; built around metadata YAML files stored with the code, harvested and visualized. Two use cases: teams manage what they own (uniform view); all software + ownership discoverable ("No more orphan software").
- Three ways entities enter the catalog: manual registration (URL to the YAML in source control), creation through Software Templates (auto-registered), external integrations. Owning teams maintain metadata via their normal Git workflow; the catalog updates automatically.
- Plugins organize tools around entities: "The software catalog is a great way to organize the infrastructure tools you use to manage the software. This is how Backstage creates one developer portal for all your tools. Rather than asking teams to jump between different infrastructure user interfaces… most of these tools can be organized around the entities in the catalog."
- Scaffolder flow: choose template → enter variables → review → run (per-step logs, cancel, task list with unique IDs, re-run "Start Over") → results link to the created repository. "By default, it has the ability to load skeletons of code, template in some variables, and then publish the template to some locations like GitHub or GitLab." Created components are automatically registered in the catalog.
- Roles: engineering managers (standards, migrations, test certification), developers (build components in a standardized way, central place for projects and docs), platform engineers (integrate tools via plugins).

### Port (SaaS config-driven pole) — Evidence A

- Self-description (era-current): "Port is an agentic SDLC platform… Agents & humans can query your catalog, trigger tools and collaborate on SDLC workflows." The glossary still defines the product register: "**Portal**: Port's developer portal product — the web application… where developers interact with the catalog, run self-service actions, and view scorecards."
- **Software catalog**: "The central registry in Port that contains all entities, organized by blueprints and linked by relations. The software catalog is the core of Port, giving teams a unified, queryable view of their infrastructure, services, and resources."
- **Blueprint** = schema definition for a catalog type (properties, relations; "closer to a class definition"); **Entity** = "a catalog record — a concrete instance of a blueprint… Entities hold the actual data (property values, relation links) for each resource tracked in Port."
- **Self-service action**: "A user-triggered workflow… that lets developers perform predefined operations (provision resources, open tickets, deploy services) directly from the portal." **Automation** = event-triggered on catalog events. **Run** = "a single execution… including its inputs, status, logs, and audit trail… can be inspected after the fact to understand what was triggered, by whom, and what the outcome was."
- **Integration**: "an Ocean-based connector that syncs data from a third-party tool (GitHub, Jira, AWS, Datadog, and others) into the software catalog." Catalog auto-discovery: "automatically detect and ingest resources from connected tools." **Execution agent**: a self-hosted relay letting action webhook nodes "reach services inside a private network" — i.e., execution reaches *into* the customer's network; Port triggers and tracks, external systems execute.
- **Scorecard**: "tracking compliance, quality, and maturity standards across catalog entities… levels and rules… evaluates each entity… integrated directly with the catalog data model and update in real time."
- **Ownership**: "assigning a team as the responsible owner of an entity… used to drive accountability, filter catalog views, and scope RBAC permissions — for example, restricting who can trigger actions on a given service."
- Pillars: context lake (unify data from the engineering ecosystem into a queryable knowledge layer), workflows & tools (self-service actions + automations: "Scaffold services, provision resources, and automatically respond to catalog events"), Port AI, agent management, interface builder (dashboards, catalog views, approvals, notifications), governance layer (scorecards), platform administration (SSO, RBAC).
- Guides evidence the action range: scaffold a new service, provision cloud resources via Terraform, manage ArgoCD/Kubernetes, rollback deployments, DORA metrics, production-readiness scorecards.

### Cortex (standards-first SaaS pole) — Evidence A

- Self-description: "Cortex is the EngOps Platform that keeps your entire engineering organization moving as one." Four pillars: security, reliability, velocity, efficiency.
- Connect data: "Pull in data from Git, Snyk, PagerDuty, and your other essential tools to build a complete picture of your software ecosystem." Define ownership: "Establish clear ownership of services and entities to drive accountability, streamline incident response." GitOps: "Configure a GitOps workflow to manage entities in your Cortex workspace."
- **Scorecards**: "a set of rules that Cortex measures your entities against, continuously and automatically. You write down what 'good' looks like once, and Cortex tells you which entities meet that bar, which don't, and why." Pre-portal state named explicitly: "Standards tend to live in wiki pages, onboarding checklists, and the heads of a few senior engineers. They drift. Scorecards move those standards into a place where they're visible, measurable, and hard to quietly ignore."
- Scorecard anatomy: entities (scope by type/group/query), rules ("a single, checkable statement about an entity… Rules can read an entity's metadata inside Cortex or pull live data from your integrations"), levels or points, an evaluation window (default recheck every 4 hours — precise number kept out of the final document). Failure messages "can link straight to a runbook or a Workflow that fixes the problem." Exemptions and rule filters. Scorecards as code (GitOps) or UI.
- **Workflows**: "an automated, multi-step process that runs entirely within your Cortex workspace. It lets teams define tasks, trigger actions, collect input, and route approvals in one place." Blocks: core (HTTP request, branch, JQ, JavaScript, manual approval, run workflow, **scaffolder** — "run a scaffolder template", user input), Cortex blocks (create/update entity, add custom data, list deployments, get scorecard scores), integration blocks (GitHub, PagerDuty, ServiceNow, Slack, Jenkins — "Creating a new GitHub repository… Triggering a Jenkins job or pipeline"). Runs have status/history; permissions gate blocks ("If the initiating user doesn't have permission to perform the block's action, the block fails").
- Golden paths: "automated golden paths that let developers bootstrap new services with security, observability, and operational standards pre-configured." Workflows automate "scaffolding new services or managing migrations" and incident response ("rollback, restart pods").
- Surrounding layer: Initiatives (deadlines on scorecard goals), Reports (roll-ups), Eng Intelligence (DORA/velocity dashboards), Engineering homepage.

### OpsLevel (mid-market SaaS pole) — Evidence A (intro-page depth)

- Self-description: "OpsLevel is the AI-powered internal developer portal that catalogues every element of your software ecosystem in minutes, enforces standards automatically, and unblocks engineers with one-click self-service—all from a single pane of glass."
- Three pillars named: **Visibility, Standards, Self-Service** with Automation as the foundation.
- Catalog Engine: "discovers services from Git, Kubernetes, CI/CD, and cloud providers—then fills the gaps with AI-generated descriptions and owners." Connect a repo; optional `opslevel.yml` for rich metadata; "auto-maps relationships and flags unregistered services."
- Standards: Scorecards & Checks — "every service gets a living report card"; 80+ checks out-of-the-box (precise count kept out of the final document); AI-suggested checks; Rubric + Scorecards structure checks into an overall Component Level; Campaigns "automate org-wide fixes—no spreadsheets"; alert integrations "nudge owners in Slack or Teams"; aggregated Maturity Report.
- Actions: "Actions turn runbooks into safe, reusable buttons—complete with optional approval flows." Use cases: deploy-freeze override, "spin up a new microservice scaffold", "create a compliant S3 bucket via Terraform", "rollback a bad release". Approvals route to Slack, email, or PagerDuty; "every Action is version-controlled alongside your code."

### Humanitec (terminology-defining vendor; evidence from the sibling IDP pass) — Evidence A

- "Developer portals like Backstage, Port, Cortex, Harness etc. enable developers to self-serve key actions… They often provide a service or software catalog for discovery, and offer scaffolding or software templating… They do this by integrating with other tools and data sources, such as a VCS, a CI/CD system, or a Platform Orchestrator."
- "A developer portal as a self-service go-to place used in tandem with the Humanitec Platform Orchestrator as a backend make a powerful combination."
- The Platform Orchestrator is the provisioning backend that "powers" an IDP; the portal is the self-service surface in front of it.

## Cross-product Comparison

| Dimension | Backstage | Port | Cortex | OpsLevel |
|---|---|---|---|---|
| Self-description | "open source framework for building developer portals" | "agentic SDLC platform" (era-current); glossary still defines "developer portal" | "the EngOps Platform" | "the AI-powered internal developer portal" |
| Catalog as central registry | Software Catalog — "centralized system that keeps track of ownership and metadata for all the software" | Software catalog — "the core of Port"; entities organized by blueprints, linked by relations | Catalog — entities with ownership; GitOps-managed | Catalog Engine — discovers services from Git/K8s/CI-CD/cloud |
| Entity model | metadata YAML descriptors in Git; kinds (components, APIs, resources, systems…) | blueprints (types) → entities (records) with properties + relations | entities with descriptors (`cortex.yaml`), custom data | services + components; `opslevel.yml` |
| Ownership first-class | catalog tracks ownership; teams maintain via Git | Ownership mechanism — accountability, view filtering, RBAC scoping | "Define Ownership… drive accountability" | AI-suggested owners + yml |
| Catalog ingestion | manual register / templates / external integrations | Ocean integrations, API, webhooks, auto-discovery | integrations (Git, Snyk, PagerDuty…), GitOps | Catalog Engine auto-discovery + yml |
| Self-service action | Software Templates (scaffolder): skeleton → variables → publish to GitHub/GitLab → auto-register | Self-service actions: "provision resources, open tickets, deploy services"; runs with logs/audit; automations on catalog events | Workflows: multi-step blocks (HTTP, approvals, scaffolder, integrations); runs with status/history | Actions: "runbooks into safe, reusable buttons" with optional approvals |
| Where actions execute | external systems (publish to GitHub/GitLab; plugins call external tools) | external backends (GitHub workflows, webhooks, custom backends; execution agent relays into private networks) | external systems (HTTP, Jenkins, GitHub, ServiceNow, Slack) + Cortex catalog ops | external systems (Terraform, deploy tooling); approvals via Slack/email/PagerDuty |
| Governance/standards | via ecosystem plugins (not a core out-of-box pillar) | Scorecards: levels + rules, real-time evaluation | Scorecards: rules/levels/points, continuous evaluation, exemptions; Initiatives; Reports | Scorecards & Checks + Rubrics → Component Level; Campaigns; Maturity Report |
| Docs | TechDocs — core pillar ("docs like code") | capability (guide: "Manage and surface technical documentation") | not evidenced as a core pillar on fetched pages | not evidenced on fetched page |
| Search/browse | catalog browse + search + starring | queryable catalog; pages/dashboards | catalog + homepage | catalog browse |
| RBAC/SSO/audit | auth/identity + permissions core features | RBAC, SSO, audit logs | access controls on workflows; roles | (not detailed on fetched page) |
| API/CLI/as-code | API + YAML descriptors in Git | API, Terraform provider, config sync | API + GitOps for entities/workflows/scorecards | GraphQL API + CLI + yml |
| AI layer | AI features in docs nav (era-current) | Port AI, agents, MCP server, skills | Cortex MCP, AI assistant | AI catalog engine, AI-generated checks |
| Packaging | open-source framework, self-hosted, assemble-your-own | SaaS | SaaS | SaaS |

Reading of the comparison:

- **Universal (4/4)**: the software catalog as the central registry of entities with ownership and metadata; ownership as a first-class accountability mechanism; self-service action through the portal (scaffolding and/or predefined operations) with runs recorded; integration-based ingestion from the systems where the work happens; actions executing in external systems (the portal triggers and tracks, never provisions runtime itself); the organization's own engineers as the served population; API access; RBAC.
- **Strong common (3/4 or module-gated)**: scorecards/standards governance (core in Port/Cortex/OpsLevel; ecosystem-plugin in Backstage); search; dashboards/homepage; notifications; config-as-code/GitOps for entities and portal configuration.
- **Common but not universal**: docs surfaced per entity (core pillar in Backstage; capability in Port; not evidenced in Cortex/OpsLevel fetched pages).
- **Era-current**: AI layer (AI-generated metadata, assistants, MCP servers, agents operating the portal) — present across poles, treated as capability layer.

## Abstraction Levels

### L0 — Defining Invariant

Four jointly-held structures. The Type holds only while all four are present:

1. **The organization's developer-facing self-service surface** — one standing place where the organization's own software developers go to find and act on the software estate, instead of jumping between infrastructure tool UIs or asking around. Remove → scattered tool UIs; point the surface at external developers → Developer Documentation Portal / API-consumer portal territory.
2. **The software catalog of record** — the organization's software entities (services, libraries, websites, pipelines, resources…) held as individually addressable records with ownership and metadata, accumulated as the authoritative inventory of what exists and who owns it. Remove → a docs site, dashboard, or wiki with no entity inventory.
3. **Aggregation through integration, not execution** — the catalog and its views are assembled by integrating with the systems where the work happens (VCS, CI/CD, monitoring, cloud, ticketing); the portal displays state and triggers actions in those systems but is not itself the machinery that builds, provisions, or runs software, and does not hold deployment state. Remove the machinery boundary → Internal Developer Platform (the sibling); remove the integrations → a manually-maintained static directory (the thin ancestor).
4. **Self-service action through the surface** — developers act through the portal: scaffold new services from organization templates, trigger predefined operations (deploy, provision, rollback, open tickets) that execute in the connected systems, with each run recorded. Remove → a read-only inventory/report, below the Type.

Jointly-held is load-bearing:

- 1 alone = a generic intranet/employee portal
- 2 without 1+3 = a static service inventory / CMDB-lite
- 3 without 2 = tool dashboards with no unified entity spine
- 4 without 2+3 = a generic workflow/automation tool
- 2+3 without 4 = a read-only catalog (thin form, below the Type)
- 2+4 without 3 = a manually-maintained catalog with forms (the wiki+forms ancestor)
- 1+2 without 3+4 = a static directory page
- 1+3 without 2 = a tool aggregator with no software-entity spine

Consistency with the sibling IDP pass: the IDP's L0 analysis records "2+4 without 3 = developer portal" (developer self-service + org-defined abstraction layer without the platform's own provisioning machinery). This pass confirms that reading from the portal side: the portal carries self-service action and org-defined templates, executed through integrations; what it never carries is the machinery of record.

Historical check (§24): the market category is young (Backstage open-sourced from Spotify's internal tool ~2020; commercial portals followed), so the check guards against over-fitting to the current packaging rather than against a long product lineage. The analog pre-history is documented by the vendors themselves: Cortex names it ("Standards tend to live in wiki pages, onboarding checklists, and the heads of a few senior engineers. They drift."), Backstage names it ("No more orphan software hiding in the dark corners"). The analog ancestor — a wiki service directory + template repos + runbook pages + manual standards audits — satisfies the catalog leg at analog level but fails the self-service-action leg (copy-the-template-repo is manual work); it is the pre-history the Type digitized, not a variant. No older software product was directly evidenced satisfying all four legs; the historical check is therefore conceptual, and the definition is abstracted above the current AI/catalog-engine packaging (no AI, no specific integration set, no scorecard mechanics in L0).

### L1 — Common Mature Structure

Present across most of the sample; expected in the market but not definitional:

- **Scorecards / standards governance** — rules evaluated continuously against catalog entities, levels or points, roll-up reports; core in 3/4, ecosystem-plugin in Backstage
- **Docs per entity** — docs-as-code surfaced on the entity page (core pillar in Backstage; capability elsewhere)
- **Search** across the estate
- **Dashboards / homepage** — per-team and per-person views
- **RBAC / SSO / audit logs**
- **Notifications** — nudges to owners via chat tools
- **API / CLI parity**; config-as-code / GitOps for entities and portal configuration
- **Engineering intelligence metrics** (DORA-class) — Cortex (Eng Intelligence), Port (guides)
- **Initiatives / campaigns** — deadline-driven standards adoption (Cortex, OpsLevel)

### L2 — Variant / Optional Structure

- Packaging: open-source framework assembled and self-hosted (Backstage) vs SaaS portal (Port/Cortex/OpsLevel)
- Catalog construction: descriptor files in Git (Backstage YAML, `cortex.yaml`, `opslevel.yml`) vs integration auto-discovery vs AI-assisted discovery
- Center-of-gravity emphasis: catalog-first (Backstage, Port) vs standards-first (Cortex, OpsLevel)
- Entity scope breadth: services only vs broad estates (websites, ML models, data pipelines, AI agents as catalog entries)
- AI-agent operation of the portal (agents querying the catalog, triggering actions via MCP) — era-current
- Customer tier: self-hosted enterprise platform teams (Backstage) vs mid-market SaaS (OpsLevel) vs enterprise SaaS (Port, Cortex)

### L3 — Vendor-specific (Research Notes only)

- Backstage: plugin architecture; entity kinds and system model (components/APIs/resources/systems/domains); scaffolder tasks with unique IDs and "Start Over"; TechDocs; CNCF project governance; "Made at Spotify" lineage.
- Port: blueprints/entities/Ocean integration framework/Context Lake/execution agent (`port-agent` relay)/interface builder/pages & widgets/meta-properties; "agentic SDLC platform" repositioning.
- Cortex: CQL (Cortex Query Language); Initiatives; Eng Intelligence dashboards; Engineering homepage; default 4-hour scorecard evaluation window; Bird's eye/Progress/Report card reports.
- OpsLevel: Rubrics; Checks (80+ out-of-box); Campaigns; Maturity Report; Catalog Engine with AI-generated descriptions/owners; `opslevel.yml`.

## Vendor-specific Findings

- Humanitec is the terminology-defining vendor for the portal-vs-platform seam (Evidence A, single-vendor definition corroborated by market structure: Cycloid sells "Internal Developer Portal" and "Internal Developer Platform" as separate solution pages of one product — sibling pass evidence).
- Port's 2026-era self-repositioning as an "agentic SDLC platform" shows positioning drift over a stable structure: its own glossary still defines the product as a developer portal ("where developers interact with the catalog, run self-service actions, and view scorecards") and the catalog as "the core of Port". Treated as era-current marketing drift, not a Type change.
- Backstage is the only sampled product without scorecards as a core out-of-box pillar (ecosystem plugins instead) — evidence that governance is common-mature, not definitional.
- The AI layer (Port agents/MCP, Cortex MCP, OpsLevel AI catalog engine) is era-current across all poles; treated as L2.

## Rejected Findings

- "Portal = IDP with a nicer UI" — rejected: the machinery boundary is structural, not cosmetic. Every sampled portal triggers external systems and tracks runs; none provisions or runs software itself. Port's execution agent exists precisely to reach *into* private networks *from* the portal — the portal remains the trigger side.
- "The catalog is just a feature" — rejected: all four products name the catalog as the center ("the core of Port"; Backstage "powered by a centralized software catalog"; Cortex "complete visibility through the Catalog"; OpsLevel pillar 1 Visibility via the Catalog Engine).
- "Scorecards are definitional" — rejected: 3/4 core + Backstage ecosystem plugins; a portal without scorecards (catalog + scaffolding + docs) is still recognizably a portal. Held as common-mature.
- "Docs are definitional" — rejected: core pillar only in Backstage; capability elsewhere. Held as common.
- "AI agents are definitional" — rejected: era-current layer across poles; the Type predates it.
- "The portal must be SaaS" — rejected: Backstage is an open-source self-hosted framework; packaging is a variant.
- "The portal holds the deployment state" — rejected: deployment/runtime state appears in portals only as *ingested* data (e.g., Port guides to "visualize your services' k8s runtime" via ArgoCD — visualization of another system's state). The executing record lives in the connected systems.

## Boundary Findings

**vs Internal Developer Platform / IDP (§12 sibling, processed 2026-09-08)** — the sharpest seam; JOINT REVIEW DISCHARGED from this side (the IDP pass recorded its side; see STATUS.md):
- Portal = the developer-facing surface organized around the catalog: discovery, ownership, standards views, scaffolding, self-service actions; integrates with other tools; triggers actions in them; does not build, provision, or run software; does not hold deployment state.
- IDP = the provisioning machinery of record: turns requests into running software on the org's infrastructure and holds the deployment state.
- Evidence: Humanitec's own docs (portal as "self-service go-to place… in tandem with the… Orchestrator as a backend"; portals "integrate with other tools… such as a VCS, a CI/CD system, or a Platform Orchestrator"); Port's glossary (portal = "interact with the catalog, run self-service actions, view scorecards" — no provisioning claim; execution agent relays to external backends); Cortex workflows trigger external systems (Jenkins, GitHub, ServiceNow).
- Removal test, both directions: remove the machinery behind an IDP (keep catalog/scorecards/docs/scaffolding) → a portal; give the portal its own provisioning machinery holding deployment state → an IDP.
- Combined packaging exists (Cycloid unified portal+platform; Humanitec Portal + Orchestrator; Northflank managed platform with a console) — fix by center of gravity, not feature presence, per the sibling pass's straddle warning.

**vs Developer Documentation Portal (§12, processed 2026-09-08)** — that Type centers the build-with-product corpus (quickstarts/tutorials/reference) authored by a product's own team for the product's developers — an external-facing publishing surface. The internal developer portal centers the org's own software-estate catalog and self-service for the org's own developers; documentation is one per-entity capability (TechDocs-class), not the organizing corpus. Audience seam: external developers of a product vs the org's internal developer population.

**vs API Management Platform's developer portal (§12, processed 2026-09-06)** — the API-management developer portal surfaces a platform's APIs to API consumers (frequently external), bound to the API lifecycle and consumer onboarding. The internal portal's catalog spans the whole software estate; internal APIs may appear as entities, but the center is the estate, not the API product. Same word, different Type.

**vs CMDB (§14)** — both are inventories of "things that exist", but the audiences and metadata differ: the CMDB serves IT service management (configuration items, service dependencies for incident/change processes); the portal catalog serves software development (services, ownership, standards, scaffolding, actions). A portal catalog may feed a CMDB; the center of gravity decides.

**vs Engineering Productivity Analytics** — metrics overlap (DORA-class dashboards appear in Cortex and Port). The analytics Type centers measurement of engineering work; the portal centers the catalog + self-service over the estate. Analytics is a capability layer inside portals, not their identity.

**vs Intranet Platform / Employee Portal (§10)** — generic organization-wide portals serve all employees with company content and services; the internal developer portal serves the engineering population specifically, organized around the software estate. Different audience, different objects.

**vs Enterprise Wiki (§02.06)** — the wiki holds knowledge pages; the portal holds entity records with ownership, live integration data, and actions. Cortex's own copy names the seam: standards "live in wiki pages… They drift. Scorecards move those standards into a place where they're visible, measurable." TechDocs borrows the reading surface but hangs off catalog entities.

**vs Project Scaffolding / Code Generator (§12 leaf)** — scaffolding is one capability inside the portal (templates/scaffolder). A dedicated scaffolding tool centers code generation alone; the portal's scaffold is embedded in the catalog (auto-registration), governance (standards pre-configured), and self-service context.

**vs Code Search Platform (§12)** — code-level retrieval vs entity-level inventory and action. Complementary; a portal may link to code search.

## Uncertainties

- OpsLevel evidence is intro-page depth (the "Introducing OpsLevel" page); deeper operational pages (checks catalog, permissions model) were not fetched. No precise operational claims made for OpsLevel beyond that page.
- Cortex's docs surface was sampled at readme + workflows + scorecards depth; the catalog ingestion mechanics page was not separately fetched (GitOps entity management evidenced from the readme).
- Backstage's scorecard capability is ecosystem-plugin; the specific plugin landscape was not surveyed.
- Gartner/analyst definitions of "internal developer portal" were not directly accessible (same limitation as the IDP pass); the seam rests on vendor documentation and market structure.
- No older software product was directly evidenced for the historical check; the check is conceptual (analog pre-history documented via vendor copy).
- Exact plan/limit/pricing details deliberately not asserted (none researched).

## Final Synthesis

The Internal Developer Portal is the organization's developer-facing surface of record over its own software estate. Its defining core is four jointly-held structures: (1) the organization's developer-facing self-service surface — one place the org's developers go to find and act; (2) the software catalog of record — the org's software entities held as individually addressable records with ownership and metadata; (3) aggregation through integration, not execution — the portal assembles its picture from the systems where the work happens and triggers actions in them, but never builds, provisions, or runs software and holds no deployment state; (4) self-service action through the surface — scaffolding from org templates and predefined operations, executed in the connected systems, with runs recorded.

The market realizes the Type in poles: the open-source framework pole (Backstage — assemble and host your own), the SaaS config-driven pole (Port — blueprints/entities, actions, scorecards), the standards-first EngOps pole (Cortex — scorecards/initiatives/workflows), and the mid-market catalog+rubric pole (OpsLevel). The sibling Type Internal Developer Platform is the complementary machinery; the two are sold separately and combined, and the seam is the center of gravity (surface vs machinery). The thin ancestor is the wiki service directory + template repos + manual standards audits — the pre-history the portal digitized; scorecard governance, docs, search, and the AI layer are common-mature or era-current capabilities, not the definition.
