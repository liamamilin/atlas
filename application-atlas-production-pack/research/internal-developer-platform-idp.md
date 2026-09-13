# Research Notes — Internal Developer Platform / IDP

## Research Goal

Understand what an **Internal Developer Platform (IDP)** is as an Application Type: what exists inside it, who uses it, how work flows through it, and where its boundaries lie against the neighboring Types in §12 (Internal Developer Portal, Continuous Delivery Platform, Dev Container/Workspace Platform, Project Scaffolding) and adjacent sections (Cloud Management Platform, Infrastructure Automation Platform, PaaS-class products, Low-code platforms).

Special difficulty: "IDP" is used in the market in two registers — (a) a **concept** (an assemblage a platform-engineering team composes: portal + orchestrator + CI/CD + observability), and (b) a **product category** (commercial products sold as "an IDP" or as the core engine of one). This pass defines the product Type and treats the concept usage as context.

## Initial Boundary

Working hypothesis before research:

- Core use: let an organization's application developers self-serve the runtime side of software delivery (deploy services, get environments and databases) without filing infrastructure tickets.
- Primary users: application developers (consumers) + platform engineers (configurers).
- Nearest neighbors: **Internal Developer Portal** (sibling leaf, unprocessed — expected to be the UI/catalog layer), **PaaS** (vendor-owned runtime), **Cloud Management Platform** (ops-facing), **Infrastructure Automation Platform** (ops-facing governed execution; that pass flagged convergence from self-service automation portals), **Continuous Delivery Platform** (pipeline-centric).
- Unknowns: whether "runs on the org's own infrastructure" is definitional; whether the portal-vs-platform seam holds across the market; whether preview/ephemeral environments are definitional or common; how the in-house-built pole relates to the product Type.

## Research Questions

1. What are the core objects? (organization, project/application, environment, service/workload, resources/dependencies, templates/golden paths)
2. Who does what: what does the platform team configure, what do developers consume?
3. What is the canonical workflow from "platform team sets up" to "developer deploys and operates"?
4. What role do environments (esp. ephemeral/preview) play — definitional or common?
5. Where does the platform run — vendor cloud, customer cloud accounts, on-prem? Is that definitional?
6. What is the exact seam vs the Internal Developer Portal (sibling leaf)?
7. What is the seam vs PaaS, IaC, CMP, infrastructure automation, CD?
8. Would older products (internal PaaS era, pre-self-service internal hosting) still fit the definition?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer tiers:

| Product | Pole | Evidence depth |
|---|---|---|
| Humanitec Platform Orchestrator | engine/orchestrator pole — sells the core machinery of an IDP, explicitly not the portal | Tier 1 (developer.humanitec.com docs) |
| Qovery | self-serve IDP running on the customer's own cloud accounts (BYOC pole) | Tier 1 (docs.qovery.com → qovery.com/docs) |
| Northflank | managed developer platform / IDP product; managed cloud + BYOC; startup-to-enterprise | Tier 2 (northflank.com product pages incl. named /product/idp) |
| Cycloid | unified "Internal Developer Portal & Platform" packaging; enterprise/sovereign/public-sector pole | Tier 2 (cycloid.io) |
| Akamai App Platform for LKE (Otomi lineage) | open-source / pre-built Kubernetes developer platform pole | Tier 1 (techdocs.akamai.com) |

Historical anchor (not a representative product): **Cloud Foundry** (docs.cloudfoundry.org, Tier 1) — the org-run internal PaaS of the 2010s, used for the historical/market-sample check.

## Sources

- Humanitec — Platform Orchestrator docs: overview (https://developer.humanitec.com/platform-orchestrator/docs/platform-orchestrator/overview/), "How Humanitec relates: Backstage, Port, Cortex etc." (…/docs/humanitec-vs-others/backstage-port-cortex-etc./). Fetched 2026-09-08.
- Qovery — docs: Introduction, Core Concepts, How Qovery Works (https://www.qovery.com/docs/, /docs/getting-started/basic-concepts, /docs/getting-started/how-it-works). Fetched 2026-09-08.
- Northflank — homepage and "Internal developer platform" product page (https://northflank.com/, https://northflank.com/product/idp). Fetched 2026-09-08.
- Cycloid — homepage (https://www.cycloid.io/). Fetched 2026-09-08.
- Akamai App Platform for LKE — Welcome page (https://techdocs.akamai.com/app-platform/docs/welcome; otomi.io now redirects here). Fetched 2026-09-08.
- Cloud Foundry — overview (https://docs.cloudfoundry.org/concepts/overview.html). Fetched 2026-09-08.
- platformengineering.org wiki page 404'd (one attempt; not retried). Gartner definitions not directly accessible; Gartner referenced only via Cycloid's own page ("named in Gartner Hype Cycle 2026 for Platform Engineering").

## Product Observations

### Humanitec Platform Orchestrator (engine pole) — Evidence A

- Self-description: "The Platform Orchestrator is the core component that powers your Internal Developer Platform. It removes infrastructure bottlenecks and creates golden paths for developers by automating provisioning and deployment of resources." (docs overview)
- Mechanism (RMCD loop): **Read** the deployment delta (typically derived from a Score workload file) → **Match** the deployment context (Application, target Environment, Environment Type) against the org's **Resource Definitions** → **Create** application configurations and provision resources via **Drivers**, ordered by a constructed **Resource Graph** → **Deploy** the Workloads.
- Object model: Organizations → Applications → Environments (with Environment Types) → Workloads; Resources (types, classes, definitions, versions); Drivers (Terraform, database, DNS, Kubernetes, custom); Workload Profiles (built-in and custom); Deployment Sets and Deltas.
- Division of labor: "Developers describe their resource requirements in Score files checked into source control… The Platform Orchestrator interprets these workload definitions and provisions the required resources." "It enables self-service provisioning of resources while still giving platform teams control and governance over how resources are configured and deployed."
- Deployment posture: SaaS operated by Humanitec, "securely integrated with your infrastructure" — cloud accounts (AWS/Azure/GCP/OCI) connected; agents/operators run inside the customer's clusters.
- Portal seam (from "How Humanitec relates"): "Developer portals like Backstage, Port, Cortex, Harness etc. enable developers to self-serve key actions… They often provide a service or software catalog for discovery, and offer scaffolding or software templating… They do this by integrating with other tools and data sources, such as a VCS, a CI/CD system, or a Platform Orchestrator." "A developer portal as a self-service go-to place used in tandem with the Humanitec Platform Orchestrator as a backend make a powerful combination." Humanitec also ships its own "Humanitec Portal" specialized for the Orchestrator.
- CI/CD relationship: integrates with existing CI/CD pipelines (container registries, workload artefacts); also ships its own Humanitec Pipelines (deployment pipelines, artefact automation, API-triggered).

### Qovery (BYOC self-serve pole) — Evidence A

- Self-description: "The Kubernetes control plane for humans and AI agents — on your own infrastructure, cloud or on-premise." "Describe what you want to deploy and an AI agent handles the rest — or use the console, CLI, Terraform, API, or MCP directly. Either way, operational best practices and guardrails are built in."
- Object hierarchy (Core Concepts): **Organization** (the company's workspace; RBAC, shared cloud credentials, billing) → **Cluster** (Kubernetes; Qovery-managed on AWS/GCP/Azure/Scaleway, or self-managed BYOK "connect your existing cluster") → **Project** (groups related services) → **Environment** (deployment stage tied to a Git branch: production/staging/development + **Preview** environments "automatically created for each pull request and deleted when merged") → **Services** (Application, Database, Cron Job, Lifecycle Job, Helm Chart, Terraform).
- Deployment: fetch code from Git → build container image (auto-detects framework or Dockerfile) → push to registry → provision Kubernetes resources (pods, services, ingress, secrets) → health checks; GitOps auto-deploy on push; one-click rollback; pipeline stages.
- Auto-generated connection variables between services and databases (e.g. database host/port/URI surfaced as environment variables).
- Positioning vs PaaS: "Unlike traditional PaaS (Heroku, Platform.sh), Qovery runs on **your own cloud accounts**: Full Ownership… No Vendor Lock-in… Cost Transparency… Data Sovereignty."
- Interfaces: web console, CLI, API, Terraform provider, AI Agent Skill (source → deployed), MCP Server (operate via natural language). Era-current AI layer.
- Scope claims: provision (managed Kubernetes), deploy, observe (logs/metrics/events), optimize (cost), secure (RBAC/SSO/secrets/audit).

### Northflank (managed platform + BYOC pole) — Evidence A (product pages)

- Named product page: "Build your Internal Developer Platform (IDP)" — "Northflank provides powerful and composable IaC primitives that accelerate platform creation." "Building a custom Internal Developer Platform (IDP) from scratch is risky and time-consuming. With Northflank, you get a battle-tested platform."
- Value framing: "Use the right building blocks to ship your platform quickly… higher-level primitives… based on Kubernetes and cloud-native technologies… ready-to-go solutions for build, deployments, delivery, secure multi-tenancy." "Give your teams the best DevEx, **with you defining the defaults and guardrails**. All your developers need is a Dockerfile or Buildpack."
- Golden paths: "Build golden paths — Pipelines and automatic preview environments are your golden path to production. Codify your workflows and graduation policies."
- Objects: services, databases, jobs, inference/GPU workloads; preview/staging/production environments; IaC templates ("Group multiple services, jobs, and stateful workloads together into a single IaC template"); managed addons ("managed services inside your clusters… the six most popular databases… bring your own Helm charts").
- Runtime: Northflank Cloud or customer clouds (EKS/GKE/AKS/OKE/CKS…) / "Bring Your Own Cloud"; "Deploy to Northflank's cloud for maximum simplicity, or connect your GKE, EKS, AKS, or bare-metal to deliver a managed platform experience."
- PaaS contrast (customer quote): "It's more powerful and flexible than traditional PaaS – all within our VPC."
- Interfaces: "Choice of UI, CLI, APIs & GitOps."

### Cycloid (unified portal+platform, enterprise pole) — Evidence A (product pages)

- Self-description: "Your unified Internal Developer Portal & Platform… Sovereign by design, secure by nature, made to scale platform engineering initiatives." "Cycloid's GitOps first approach… reduces bottlenecks with its Internal Developer Portal and Platform in one."
- Named capability blocks: **Service Catalog** ("Landing zone, infrastructures, applications, display anything you want in your service catalog to bring self-service portal to developers while keeping best practices, security and automation in place"); **StackForms** ("forms designed by your platform teams. It allows anyone to interact with tools, cloud and automation without having to become a DevOps expert"); **Platform Orchestration** ("Create custom workflows to simplify the deployment processes for end-users… connected to your continuous integration tool"); governance/observability (RBAC, approvals, SSO/MFA, dashboards, asset inventory); FinOps/GreenOps; plugins; AI assistant & MCP server.
- Role framing: solutions split by role — "Platform Teams" vs "End-Users and Developers"; also sells "Internal Developer Portal" and "Internal Developer Platform" as two separate solution pages from the same product.
- Deployment posture: digital sovereignty, native self-hosting; hybrid and multi-cloud; enterprise/public-sector customers (European Commission, Siemens, CMA CGM logos).
- Straddle note: Cycloid explicitly packages portal + platform as one product — the market's combined-packing pole.

### Akamai App Platform for LKE (Otomi lineage; open-source/pre-built pole) — Evidence A

- Self-description: "App Platform is a pre-built Kubernetes developer platform that is intended to accelerate your platform development… It combines both developer-centric and operations-centric tooling into a single self-service portal." (Otomi's open-source IDP, now productized by Akamai; otomi.io redirects here.)
- Composition: "An integrated and pre-configured stack of open source Kubernetes projects"; "A self-service portal for developers to deploy workloads from Helm charts, build images, and publicly expose services"; "A **catalog** with Helm charts that serve as **golden path templates** and can be added, removed, or modified according to your needs"; "Kubernetes Operators and GitOps to manage the state of the platform based on configuration-as-code."
- Multi-tenancy: "Support multi-tenancy by allowing multiple teams or projects to share the same cluster, with self-service features that enable faster, independent deployments by developers." "Onboard development teams to the same multi-tenant cluster."
- Two-level usage structure (docs nav): "Platform-level usage (for administrators)" — teams, users, app catalogs, platform settings, GitOps; "Team-level usage (for devs)" — apps, catalog, code repositories, container images, secrets, workloads, services, network policies.
- Developer enablement list: build OCI images from source, deploy workloads via quickstarts or BYO golden path templates, auto image updates, expose apps, logs/metrics/traces, private registry, network policies, security policies, secrets, built-in CI/CD.

### Cloud Foundry (historical anchor, org-run internal PaaS) — Evidence A

- PaaS layer model (traditional/IaaS/PaaS comparison); "Deployment automation: Developers can deploy their apps… with zero modification to their code"; "Flexible infrastructure: You can deploy Cloud Foundry to run your apps on your own computing infrastructure, or deploy on an IaaS."
- Org structure: UAA roles (admin/developer/auditor) scoped to **orgs and spaces** — the multi-tenant org structure.
- Org-configured abstraction: **buildpacks** (including custom buildpacks managed by admins) + **stacks**; **service brokers** advertise "a catalog of service offerings"; developers provision service instances and bind credentials to apps.
- Developer loop: `cf push` → stage (stack + buildpack + source → droplet) → run on Diego-managed VMs; routes/domains; logs via Loggregator.
- Reading for the historical check: an enterprise-run CF foundation satisfies developer self-service (push, provision service instances), platform provisioning machinery (Cloud Controller/Diego/BOSH), and an org-defined abstraction layer (curated buildpacks/stacks/service catalog/quotas/domains) on the org's own infrastructure. It lacks the modern portal/catalog-UI packaging and ephemeral preview environments — those are era-current additions, not the core.

## Cross-product Comparison

| Dimension | Humanitec | Qovery | Northflank | Cycloid | Akamai App Platform |
|---|---|---|---|---|---|
| Sells itself as | core engine ("powers your Internal Developer Platform") | Kubernetes control plane / IDP on your cloud | "Internal Developer Platform (IDP)" product | "unified Internal Developer Portal & Platform" | "pre-built Kubernetes developer platform" |
| Primary configuring role | platform engineers (resource definitions, workload profiles, drivers) | platform engineers/org admins (clusters, RBAC, credentials) | platform teams ("you defining the defaults and guardrails") | platform teams (stacks, StackForms, workflows) | administrators (platform-level: teams, catalogs, settings) |
| Primary consuming role | developers (Score files, self-service) | developers (+ AI agents) | developers ("all your developers need is a Dockerfile") | end-users/developers via forms | dev teams (team-level usage) |
| Self-service consumption | yes (explicit) | yes (explicit) | yes (explicit) | yes (explicit) | yes (explicit) |
| Provisioning machinery of its own | yes (RMCD orchestrator, resource graph) | yes (control plane drives build→deploy→run) | yes (build/deploy/run primitives) | yes (orchestration workflows connected to CI) | yes (operators + GitOps state management) |
| Org-defined abstraction layer | resource definitions + workload profiles + Score | opinionated defaults + project/environment structure + templates | IaC templates + stack templates + golden paths | stacks + StackForms + service catalog | Helm-chart catalog as golden path templates (add/remove/modify) |
| Environments as managed objects | yes (Environment Types, per-app environments) | yes (dev/staging/prod + per-PR preview, auto-delete) | yes (preview/staging/production) | via projects/workflows (less environment-centric on homepage evidence) | via GitOps workloads per team (weaker homepage evidence) |
| Ephemeral/preview environments | not evidenced on fetched pages | yes (per-PR, auto-created/deleted) | yes (from pull requests) | not evidenced | not evidenced |
| Managed dependencies (DBs etc.) | yes (database/DNS/volume drivers) | yes (PostgreSQL/MySQL/MongoDB/Redis; container or managed modes) | yes ("six most popular databases", BYO Helm addons) | via stacks/plugins | yes (catalog apps, e.g. PostgreSQL lab) |
| Runs where | SaaS control plane + customer cloud accounts/clusters | customer cloud accounts or BYOK clusters | Northflank Cloud or customer clouds (BYOC) | customer infra, self-hostable, sovereign | customer Kubernetes cluster (LKE-optimized, any conformant cluster) |
| Git/CI integration | integrates with existing CI/CD; own pipelines too | GitOps auto-deploy on push; built-in build | Git-triggered builds; pipelines; GitOps | GitOps-first; connected to CI tool | built-in Gitea/Harbor/CI; GitOps |
| Portal/catalog UI | separate product (Humanitec Portal; Backstage/Port integrations) | console (not catalog-framed) | console + stack templates | yes — service catalog first-class | yes — self-service portal + catalog |
| Multi-tenancy/RBAC | organizations, RBAC, service users | organizations, RBAC, SSO | secure multi-tenancy | RBAC, SSO/MFA, approvals | teams on shared cluster, roles |
| Observability access | container logs (fetched page) | logs/metrics/events built-in | logs/metrics/alerts included | dashboards/asset inventory | logs/metrics/traces built-in |
| AI layer | MCP knowledge server | AI Agent Skill + MCP server | (AI workloads focus, not agent-ops) | AI assistant + MCP server | none evidenced |

Reading of the comparison:

- **Universal (5/5)**: organization-scoped platform operated for the org's own developers; a configuring role (platform team/admins) distinct from a consuming role (developers); developer self-service consumption; the platform's own provisioning machinery that turns requests into running software; an org-defined abstraction layer (templates/definitions/stacks/catalogs) through which consumption happens; Git/CI integration; RBAC/multi-tenancy; developer-level observability access.
- **Strong common (3–4/5 or module-gated)**: environments as first-class managed objects; managed dependencies (databases); exposure/networking (domains/TLS); secrets management; CLI/API/UI parity; cost visibility.
- **Variant**: ephemeral preview environments as default posture; portal/catalog UI included vs separate; Kubernetes-centric vs broader; managed-cloud vs BYOC vs self-hosted; AI-agent interfaces (era-current); FinOps/GreenOps; scorecards/compliance.

## Abstraction Levels

### L0 — Defining Invariant

Four jointly-held structures. The Type holds only while all four are present:

1. **The organization as operator** — the platform is operated for one organization's own software developers; a platform-engineering/administrative function configures it, and the organization's own infrastructure (its cloud accounts, clusters, or data centers) is the substrate. Remove → a public/vendor PaaS or a vendor cloud console.
2. **Developer self-service consumption** — application developers directly create and operate their applications' runtime pieces (deploy a service, obtain an environment, obtain a database) through the platform's own surfaces, without routing each request through an operations team as a ticket. Remove → ops-facing tooling (CMP / infrastructure automation) or ticket-driven internal hosting.
3. **Provisioning machinery of record** — the platform itself turns those requests into provisioned, running software (environments, workloads, and their dependencies) on the organization's infrastructure and holds the state of what is deployed where; it is the executing counterpart, not a front over someone else's executor. Remove → a portal/catalog UI (the sibling Type) or a request queue.
4. **The organization-defined abstraction layer** — reusable building blocks configured by the platform team (templates, stacks, resource definitions, golden-path catalogs) that determine what developers can consume and how their requests map onto infrastructure, abstracting the underlying substrate. Remove → raw multi-tenant cluster/infrastructure management.

Jointly-held is load-bearing:

- 1 alone = vendor cloud console / managed cloud
- 2 without 1 = public PaaS (Heroku-class)
- 3 without 2 = ops-facing automation (CMP / infrastructure-automation territory)
- 4 without 2+3 = a template library or documentation
- 2+4 without 3 = a developer portal with scaffolding (sibling Type)
- 1+3 without 4 = managed Kubernetes / cluster management
- 1+2 without 3 = portal surface with no machinery behind it
- 3+4 without 2 = a governed provisioning engine used only by ops (infrastructure automation)

Historical check (§24): an org-run Cloud Foundry foundation satisfies all four legs — developer self-service (`cf push`, service-instance provisioning), platform provisioning machinery (Cloud Controller/Diego/BOSH), org-defined abstraction (curated buildpacks/stacks/service-broker catalog/quotas/domains), organization as operator (orgs/spaces/roles on the org's own infrastructure). Pre-self-service internal hosting (request forms + ops provisioning) fails leg 2 and is correctly the pre-history the Type digitized. Kubernetes, portals, preview environments, AI agents are all absent from the historical leg — none is definitional.

### L1 — Common Mature Structure

Present across most of the sample; expected in the market but not definitional:

- Environments as first-class managed objects (named stages: dev/staging/production, per-application or per-project)
- Git integration with build-and-deploy automation (GitOps posture: push → build → deploy)
- Managed dependencies as self-service resources (databases, caches, queues) with auto-wired connection data
- Build machinery (source → container image) or artifact intake from external CI
- Multi-tenancy: teams/projects sharing the platform with RBAC and SSO
- Networking/exposure: domains, TLS, ingress handled by the platform
- Secrets/configuration management
- Developer-level observability access (logs, metrics)
- CLI / API / UI parity for the same control plane
- Cost visibility at project/environment level

### L2 — Variant / Optional Structure

- Runtime substrate: Kubernetes-centric (dominant in the sample) vs broader/multi-substrate
- Where it runs: vendor-managed cloud vs customer cloud accounts (BYOC) vs self-hosted/on-prem (sovereignty pole)
- Portal inclusion: platform-only (Humanitec engine pole) vs unified portal+platform packaging (Cycloid, App Platform) — packaging, not identity
- Ephemeral preview environments as a default posture (per-change environments)
- Service catalog UI as the consumption surface
- AI-agent interfaces (agent skills, MCP servers) — era-current
- Governance/compliance depth (approvals, policies, audit), FinOps/GreenOps modules
- In-house-built IDPs (Backstage + orchestrator + IaC assemblages) — the concept register of the term; the product Type is what vendors sell to serve that concept
- Customer tier: startup self-serve (Qovery/Northflank low tier) vs enterprise/sovereign (Cycloid, Humanitec)

### L3 — Vendor-specific (Research Notes only)

- Humanitec: Score workload specification; RMCD (Read/Match/Create/Deploy) loop; Resource Graph; Drivers (Terraform/database/DNS/Kubernetes/custom); Workload Profiles; Deployment Sets and Deltas; Humanitec Portal as a specialized companion; "How Humanitec relates" pages.
- Qovery: five named products (Provision/Deploy/Observe/Optimize/Secure); BYOK; AI Agent Skill + MCP Server; auto-generated `QOVERY_DATABASE_*` connection variables; `*.qovery.io` domains.
- Northflank: Sandboxes/microVMs; GPU workloads; stack templates marketplace; "We fixed Kubernetes" framing; six managed databases; graduation policies.
- Cycloid: StackForms; Stacks; InfraView; Infra Import; Asset Inventory; FinOps/GreenOps; plugins; MCP server + AI assistant; sovereignty/self-hosting emphasis.
- Akamai App Platform: LKE optimization; integrated CNCF stack (Gitea, Harbor, ArgoCD-class); platform-view vs team-view console; labs.

## Vendor-specific Findings

- Humanitec is the terminology-defining vendor: its docs define the IDP as something the Orchestrator "powers" and explicitly position portals (Backstage/Port/Cortex/Harness) as complementary UI layers integrating with the Orchestrator as backend. This is the strongest single statement of the portal-vs-platform seam (Evidence A, single-vendor — corroborated structurally by the market: Cycloid sells portal and platform as separate solution pages; Port-class products are not in this sample).
- Qovery's "unlike traditional PaaS" positioning is the clearest vendor articulation of the PaaS seam (Evidence A, single-vendor phrasing; Northflank testimonial echoes it).
- The AI-agent layer (Qovery Agent Skill/MCP, Cycloid MCP, Humanitec MCP knowledge server) is era-current; treated as L2, not definitional.

## Rejected Findings

- "IDP = Kubernetes platform" — rejected as definitional. 4/5 sampled products are Kubernetes-centric, but the historical leg (Cloud Foundry, VM-based) and Humanitec's serverless/containerization breadth show the substrate is an implementation choice. Held as common implementation.
- "IDP = portal + catalog + scorecards" — rejected: that is the sibling Type's center (portal). The platform's center is provisioning machinery. Catalog UIs appear in several IDP products but as packaging.
- "Preview environments are definitional" — rejected: present strongly in 2/5 fetched samples (Qovery, Northflank), absent from the historical leg; held as common/variant.
- "Runs only on the customer's own cloud accounts" — rejected as definitional: Northflank Cloud and Qovery-managed clusters are vendor-operated runtimes within products that are still IDPs; the invariant is that the platform serves the org's own developers and encodes the org's standards, not who bills the compute. BYOC is the dominant pole but a variant.
- "IDP must include CI/CD" — rejected: Humanitec explicitly integrates with existing CI/CD; built-in pipelines are common but the CD function can live in an external system.
- "Golden paths must be named 'golden paths'" — rejected: realized variously as resource definitions/workload profiles (Humanitec), stacks/StackForms (Cycloid), Helm-chart catalogs (App Platform), IaC/stack templates (Northflank), opinionated defaults (Qovery).

## Boundary Findings

**vs Internal Developer Portal (sibling leaf, §12, unprocessed)** — the sharpest seam, and the market's own vocabulary splits it:
- Portal = the developer-facing self-service *surface*: service/software catalog for discovery, scorecards, docs, scaffolding templates; integrates with other tools (VCS, CI/CD, orchestrators) via plugins; its center is visibility, discovery, governance UI.
- Platform = the *machinery*: provisions and runs the software, holds deployment state, executes against the org's infrastructure.
- Evidence: Humanitec's own docs ("a developer portal… used in tandem with the Humanitec Platform Orchestrator as a backend"; portals "integrate with other tools… such as a VCS, a CI/CD system, or a Platform Orchestrator"). Cycloid sells "Internal Developer Portal" and "Internal Developer Platform" as two solution pages of one product — combined packaging exists.
- Removal test: remove the provisioning machinery (keep catalog/scorecards/docs UI) → portal; remove the portal surface (keep machinery, consumed via CLI/API) → still an IDP.
- JOINT REVIEW recommended with the internal-developer-portal pass.

**vs PaaS (no dedicated leaf; Heroku-class)** — PaaS = vendor-owned generic runtime; developers self-serve but the abstraction layer is the vendor's, not the org's, and the substrate is the vendor's. IDP = the org's own platform: org-configured abstractions, org infrastructure (or at least org-scoped tenancy with org-defined standards). Qovery's and Northflank's own positioning draws this line. An org-run PaaS foundation (Cloud Foundry) functions as the thin ancestor — it satisfies the L0 legs; a public PaaS does not (fails leg 1 and leg 4).

**vs Cloud Management Platform (§14, processed)** — CMP: ops-facing independent control layer over cloud estates (inventories, governance, cost across accounts). IDP: developer-facing consumption of runtime capabilities. Different primary user and different center; an IDP may sit on top of the same cloud accounts the CMP governs.

**vs Infrastructure Automation Platform (§14, processed)** — that pass flagged "self-service automation portals show possible convergence toward Internal Developer Platform territory." Discharged from this side: the seam holds. Infrastructure automation centers governed *execution of automation content* against a managed estate, consumed by ops; the IDP centers *developer consumption of runtime capabilities* through org-defined abstractions. An IDP's orchestrator may use IaC/automation as drivers underneath (Humanitec Terraform drivers; Qovery Terraform service type) — integration, not identity. If a product's only "self-service" is ops-authored runbooks offered to developers, it remains on the automation side.

**vs Continuous Delivery Platform (§12, processed)** — CD centers the versioned deliverable moving through named environments between build output and running software. The IDP centers the developer's self-service runtime platform (environments, services, dependencies) and may *include* CD machinery or integrate with external CD. Overlap zone: IDPs with built-in GitOps deploy (Qovery, Northflank). Seam: if the product's center is the pipeline/deliverable, it is CD; if the center is the platform developers consume to run their software, it is an IDP.

**vs Dev Container / Workspace Platform (§12, processed)** — dev containers center the *development-time* environment definition (where code is edited/built/debugged). The IDP centers *runtime* environments where software runs after commit. Different lifecycle stage; both may be called "environments" — the seam is dev-time vs run-time.

**vs Low-code Application Platform (§12)** — low-code centers business-app construction by non-professional builders; the IDP centers professional software delivery infrastructure. Different users and objects.

**vs Kubernetes Management Platform (§14)** — cluster-level operations (nodes, workloads, upgrades) vs developer-facing app/service abstraction above the cluster. Several IDPs run on Kubernetes and manage clusters as a substrate layer; the developer consumption layer is the discriminator.

## Uncertainties

- Cycloid's environment model and ephemeral-environment support were not evidenced from the fetched pages (homepage only; docs.cycloid.io not fetched). No claims made about Cycloid's environment semantics.
- Northflank evidence is product-page depth (docs.northflank.com not fetched); structural claims only, no operational parameters.
- Gartner's official definitions of "internal developer platform" vs "internal developer portal" were not directly accessible (platformengineering.org wiki 404; one attempt only). The portal-vs-platform seam is evidenced from Humanitec's docs and market structure, not from analyst definitions.
- The in-house-built IDP pole (Backstage + orchestrator assemblages) is reasoned from Humanitec's integration docs, not from a dedicated study of in-house platforms.
- Exact plan/limit/pricing details deliberately not asserted (none researched).
- Akamai App Platform's Otomi lineage (otomi.io redirect) observed from the redirect itself; the historical Otomi docs were not separately fetched.

## Final Synthesis

The Internal Developer Platform is the organization's own self-service runtime platform for its software developers. Its defining core is four jointly-held structures: (1) the organization as operator — a platform-engineering function configures the platform over the organization's own infrastructure for the org's own developers; (2) developer self-service consumption — developers directly create and operate their applications' runtime pieces without ops tickets; (3) provisioning machinery of record — the platform turns requests into provisioned, running software (environments, workloads, dependencies) and holds the deployment state; (4) the organization-defined abstraction layer — platform-team-configured building blocks (templates/stacks/resource definitions/golden paths) that abstract the infrastructure and encode the org's standards.

The market realizes the Type in poles: the engine/orchestrator pole (Humanitec), the self-serve BYOC pole (Qovery), the managed-platform pole (Northflank), the unified portal+platform enterprise pole (Cycloid), and the open-source pre-built pole (Akamai App Platform/Otomi). The sibling leaf Internal Developer Portal is a distinct Type centered on the developer-facing surface (catalog/scorecards/docs); the two are complementary and are sold both separately and combined. The thin ancestor is the org-run internal PaaS (Cloud Foundry era); the pre-history is ticket-driven internal hosting, which the self-service leg is precisely what the Type digitized.
