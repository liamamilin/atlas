# Research Notes — Application Modernization Platform

Research date: 2026-09-06

## Research Goal

Understand what an **Application Modernization Platform** actually is as a class of software: what objects exist inside it, what its core workflow is, how automation and human work divide, what its interfaces look like, and where its boundaries lie against neighboring Types (Code Migration Platform, Application Portfolio Management, cloud-migration tooling, static analysis, AI coding assistants/agents).

## Initial Boundary (hypothesis before research)

- A platform that takes an organization's **existing (legacy) application estate** and transforms it toward **modern targets** (cloud, containers, microservices, current languages/frameworks).
- Expected span: portfolio discovery/assessment → modernization decision/planning → transformation execution → validation/tracking.
- Nearest neighbors: **Code Migration Platform** (sibling directory leaf — expected to be the code-conversion act without the program wrapper), **Application Portfolio Management** (§14 — governs the estate without transforming it), **cloud migration tooling** (infrastructure moves, application unchanged), **static code analysis** (analysis without transformation), **AI coding assistants/agents** (developer-task scale, not program scale).

## Research Questions

1. What are the core objects? (application inventory, assessment findings, plans/waves, transformation jobs, deliverables)
2. What is the core workflow loop?
3. What does "modernization" concretely mean per product (containerize, refactor, convert language, upgrade framework, re-platform database, rehost)?
4. How is work divided between automation (deterministic or AI) and humans?
5. What interfaces exist (portfolio dashboard, assessment reports, workbench, IDE integration)?
6. Who uses it and in what roles?
7. Where is the boundary vs Code Migration Platform, APM, cloud migration, static analysis, AI coding agents?
8. What lifecycle states does an application pass through inside the program?
9. Is AI/LLM assistance defining, or a current-market implementation layer?

## Representative Products

Selected for market representation + documentation completeness + different philosophies + different customer tiers:

| Product | Philosophy / position | Customer tier |
|---|---|---|
| AWS Transform | hyperscaler-attached, agentic-AI transformation workbench spanning infrastructure migration + application modernization + continuous tech-debt reduction | large enterprise, self-serve |
| IBM watsonx Code Assistant for Z | mainframe-depth AI conversion (COBOL/PL/I → modular services/Java), IDE-anchored | large enterprise, mainframe estates |
| vFunction | independent specialist; runtime+static architectural analysis driving AI-assisted monolith decomposition | mid/large enterprise, Java/.NET |
| CAST Highlight | assessment-first portfolio intelligence (facts from source code; routes but does not execute) | large enterprise / M&A / public sector |
| Azure Migrate | hyperscaler migration hub (decide → plan → execute) with a thin application-modernization surface | broad, migration-program scale |

Secondary/historical data points used for the historical-sample check: AWS App2Container (older AWS tooling, closed to new customers Nov 2025), and (from market knowledge, not fetched) older automated-transformation vendors (TSRI, Blu Age, Micro Focus/OpenText, Anubex) — used only for the §24-style breadth check, not as evidence for specific claims.

## Sources

Fetched 2026-09-06:

- AWS Transform — product page https://aws.amazon.com/transform/ ; User Guide "What is AWS Transform" https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html ; FAQ https://aws.amazon.com/transform/faq/ ; docs root https://docs.aws.amazon.com/transform/
- AWS App2Container — https://docs.aws.amazon.com/app2container/latest/UserGuide/what-is-a2c.html
- Microsoft Azure Migrate — https://learn.microsoft.com/en-us/azure/migrate/migrate-services-overview
- IBM watsonx Code Assistant for Z — https://www.ibm.com/products/watsonx-code-assistant-z
- vFunction — https://vfunction.com/platform/
- CAST Highlight — https://www.castsoftware.com/highlight

**Source-access limitations:**

- IBM docs (ibm.com/docs) returned HTTP 403 → evidence for IBM limited to the product page; precise in-product workflow details not verified.
- GitHub Copilot app-modernization docs returned 404 twice (learn.microsoft.com/dotnet/ai/appmod/*, docs.github.com) → Microsoft's dev-tool-side modernization surface not directly verified; Azure Migrate used as the Microsoft sample instead.
- vFunction docs site (docs.vfunction.com) transport error → platform page used; per-feature operational detail not verified.
- AWS Transform user-guide sub-pages other than what-is-service.html render only titles (JS-rendered); the what-is-service page and FAQ were fully readable.
- CAST Highlight capabilities page not fetched; assessment-only posture inferred from the product page and use-case structure (moderate confidence).

## Product Observations

### AWS Transform (evidence layer A — official docs, product page, FAQ)

- Positioning: "collaborative enterprise IT transformation workbench powered by expert agents that accelerates cloud migration, application modernization, and continuous tech debt reduction."
- Scope spans three programs: infrastructure migration (VMware/Hyper-V/bare-metal → EC2), application modernization (mainframe z/OS & Fujitsu GS21; Windows/.NET + SQL Server; custom code transformations), and continuous modernization (always-on tech-debt analysis + autonomous remediation across repositories).
- Official object model (User Guide terminology): **Workspace** (container + permissions boundary) → **Connectors** (asset providers to customer-owned external systems) → **Assets** (inputs: source code, servers, databases, networks) → **Objective** (user-defined end state) → **Job** (long-running process, weeks/months+, made of tasks and collaborator requests) → **Plan** (list of tasks) → **Task** (unit of work) → **Collaborator request** (a task asking a human to do something — HITL) → **Worklog** (log of actions by service and users) → **Artifact** (output deliverable). **Agent** = task-specific service executing a specific transformation type.
- Roles: Administrator / Approver / Contributor / Reader. Critical HITL actions (merging to main, graph decomposition, deploying code to production) restricted to Administrators/Approvers.
- Migration program mechanics: discovery (collector OVA, RVTools/CSV imports, third-party exports) → assessment/business case (EC2 recommendations, TCO comparison, what-if scenarios; "directional estimates… not quotes") → wave planning (application groups, dependency mapping) → landing zone → network conversion (source configs → VPC IaC) → rehost (replication, testing, cutover) → optional source-code containerization (GitHub/GitLab/Bitbucket/zip → Dockerfile, image, security scan, ECS/EKS deploy artifacts).
- Windows/.NET modernization mechanics: connect to source repos → assessment (dependencies, private packages, third-party libraries) → generated transformation plan (customizable via chat, uploaded plan, steering documents; approvers can review/approve before proceeding) → transformation in a network-isolated environment → full build → AI-led evaluation loop to auto-remediate build errors → port and run unit tests → commit to a **new branch** for review → deploy as container (EC2/ECS). SQL Server → Aurora PostgreSQL: schema conversion (via DMS Schema Conversion) + agentic conversion of stored procedures/functions + data migration + code updates (connection strings, embedded SQL, Entity Framework/ADO.NET) + functional equivalence tests + synthetic data generation option.
- Mainframe: assessment analyzes the portfolio, "deterministically maps business functions," recommends a prioritized modernization plan; "reimagine" workflow extracts business rules with traceability and flows requirements into IDEs (Kiro etc.) via MCP.
- Custom transformations: out-of-the-box Java/Node/Python upgrades; custom version upgrades, runtime migrations, language translations, architectural changes.
- Continuous modernization (preview): visibility into tech debt across thousands of repositories; autonomously detect, prioritize, remediate, document findings (EOL dependencies, outdated frameworks, security vulnerabilities).
- Surfaces: unified web experience (chat + job plan + worklog + reports), CLI (custom transformations), Visual Studio extension, Kiro power / MCP server / agent plugins for Claude/Cursor/Codex — "same underlying job with consistent state."
- Containerization boundary (FAQ): requires source code; cannot reverse-engineer running servers; not a container-migration tool.

### IBM watsonx Code Assistant for Z (evidence layer A for product page claims; docs unreachable)

- Positioning: "accelerates mainframe application development and modernization with AI and automation… from application discovery and analysis to automated refactoring, code explanation, generation, optimization and transformation to newer languages and testing."
- Capabilities: automated discovery & analysis of mainframe applications, relationships, dependencies; AI agents document business logic; natural-language code explanation; COBOL code generation (chat + inline); **auto-refactor COBOL and PL/I into modular business services** (discovers the programs and data needed); performance optimization insights (prioritized, source-level, per COBOL module); **COBOL → Java conversion** with auto-generated unit tests comparing **semantic equivalence** of the new Java service to the original COBOL; maintains IBM Z runtimes/interoperability.
- Use cases: COBOL modernization; COBOL→Java; PL/I modernization; understand/explain code (onboarding).
- Anchored in the developer IDE; case-study metrics about analysis/understanding time reductions (vendor-reported).
- Note: this product is code-workbench-shaped (IDE-centric) rather than program-workbench-shaped; program-level portfolio tracking is not evidenced on the fetched surface.

### vFunction (evidence layer A for platform page claims; docs unreachable)

- Positioning: provides "the context needed to transform, re-architect, refactor or rewrite Java and .NET applications" for AI code assistants; "from converting monoliths into microservices and transforming databases, to generating the specs and integration tests AI coding tools need."
- Flow: **Collect data** (locally installed server; static + dynamic/runtime data: flows, call trees, resource access, dependencies; OpenTelemetry for distributed services) → **Visualize & analyze** (service boundaries, dependencies, domain boundaries, anti-patterns; sequence/C4/domain-driven diagrams) → **Plan & modularize** (compares target architecture to collected metrics → generates to-dos; detailed prompts; MCP server + plugins for Claude/VS Code/Kiro; generates specs for rewrite; generates integration tests from production flows) → **Extract/rewrite services** (guides code assistants to extract domains into separate services, generating APIs, client libraries, documentation; or specs for full rewrite) → **Modernize frameworks & databases** (e.g., .NET Framework → .NET 10, Struts → REST, JEE → Spring Boot; SQL Server/Oracle/DB2 → PostgreSQL via schema conversion + stored-procedure transformation).
- Modernization plan: tasks prioritized by business impact; filter by domain/status/priority/type; export to Jira / Azure DevOps; alerts configurable by goals.
- Real-time architectural documentation (sequence diagrams, service maps, domain maps, C4).
- Deployment: runs entirely within the customer environment (behind firewall / customer cloud).
- Explicit theory of the market: code assistants "rely on static analysis," lack domain context, runtime awareness, global view of million-line monoliths; vFunction supplies the architectural context that makes large-scale brownfield refactoring deterministic and tested.

### CAST Highlight (evidence layer A for product page claims; capabilities page not fetched)

- Positioning: "Govern software portfolios" — "source your facts from your source code."
- Portfolio facts: languages/frameworks/DBs and adoption pace; third-party & proprietary components and reuse; tech debt; AI opportunities; **cloud blockers**; IP risks; open-source vulnerabilities; green (CO2) insights.
- Cloud migration support: "automatically chart the best migration routes; identify blockers, fixes, and effort required; pinpoint the best-fit cloud native services."
- Governance: fragile-application detection, resource allocation based on facts, industry benchmarks, progress tracking ("prove progress using industry benchmarks").
- AI-adoption support: identify best applications for AI augmentation; agentic readiness, blockers, fixes.
- No evidence of transformation execution on the fetched surface — the product routes decisions (routes/effort/blockers) rather than performing conversion. Sibling product CAST Imaging ("see inside applications") provides deep structure visualization.
- Use-case framing includes "Modernization — rearchitect, replatform, refactor" as an outcome the insights serve.

### Azure Migrate (evidence layer A — official docs)

- Positioning: "helps you decide on, plan, and execute your migration to Azure" — a unified migration platform (free service) for servers, databases, web apps, virtual desktops, offline data.
- Phases: **Decide** (discovery via appliance/collector/import; business case with TCO/CapEx→OpEx) → **Plan** (assessments: Azure readiness, right-sizing, cost estimation, dependency analysis) → **Execute** (migration via integrated Microsoft and partner tools).
- Modernization surface: "assess, migrate, and modernize" — servers, SQL Server databases (→ Azure SQL targets), web apps (→ Azure App Service / AKS). The application-layer transformation depth is thin compared to the other samples; the center of gravity is infrastructure/workload migration.
- Azure Copilot migration agent (preview): conversational planning over discovered inventory — explore inventory, assess readiness, compare strategies, business-case insights, landing-zone templates; "migration execution continues in the Azure Migrate portal."
- Integrated partner ecosystem (assessment and migration ISVs).

### AWS App2Container (historical/secondary, evidence layer A)

- CLI tool: inventory running ASP.NET (Windows) / Java (Linux) apps on servers → analyze runtime dependencies (processes, network ports) → extract artifacts, generate Dockerfile → build container → generate AWS deployment artifacts (CloudFormation, ECR image, ECS task defs) → optional deploy → optional CI/CD pipeline. Works **without source code** (runtime artifacts). Console experience via Migration Hub Orchestrator "Replatform to ECS" template.
- Closed to new customers (Nov 2025), superseded by AWS Transform — useful as evidence that containerization mechanics predate the agentic-AI layer, i.e., AI is not definitional.

## Cross-product Comparison

| Dimension | AWS Transform | IBM WCA4Z | vFunction | CAST Highlight | Azure Migrate |
|---|---|---|---|---|---|
| Object of work | infra + apps + code portfolio | mainframe apps (COBOL/PL/I) | Java/.NET apps (deep, per-app) | software portfolio (code-derived facts) | servers/DBs/web apps |
| Estate discovery/inventory | discovery tool + any-format imports + connectors | automated discovery & analysis | local collector: static + runtime + OTel | source-code scans | appliance / collector / import |
| Assessment outputs | TCO business case, readiness, transformation plan, complexity scoring | dependency/relationship insight, business-logic docs, performance insights | architecture visualization, domain boundaries, anti-patterns, tech debt | health/resiliency, cloud blockers, software composition, IP risk | readiness, right-sizing, cost, dependency analysis |
| Decision/path | rehost vs replatform vs containerize vs convert; customizable, approvable plans | refactor-to-services vs convert-to-Java (stay-on-Z posture supported) | user-defined target architecture → refactoring plan | migration routes + effort + blockers (no execution) | business case + migration plan |
| Execution | agentic transformation: code conversion, containerization, DB conversion, deploy; HITL gates | auto-refactoring; COBOL→Java generation; unit-test generation | guided refactoring/rewrite via code assistants (MCP); spec + integration-test generation | none (assessment only) | migration execution via integrated tools (replication, DMS, App Service migration) |
| Validation | build + unit tests, functional-equivalence tests, transformation reports | auto-generated unit tests vs semantic equivalence | integration tests from production flows | progress metrics only | testing/cutover workflows |
| Program tracking | job/task/worklog, wave status, chat, roles | IDE-centric; program tracking not evidenced | task lists, Jira/Azure DevOps export | portfolio dashboards, benchmarks, trend tracking | unified portal tracking |
| Delivery posture | SaaS workbench + CLI + IDE/MCP surfaces | IDE-anchored (on customer infra) | in-customer-environment server + MCP/plugins | SaaS | SaaS hub + appliances |
| AI posture | agentic AI orchestration (defining of current product) | fine-tuned LLMs for Z | AI-assistant enablement (context provider) | AI-readiness analytics | Copilot planning agent (preview) |

### What repeats across all five (cross-product commonality, layer B)

1. The **existing application estate** is the object of work — held as inventory records with discovered facts.
2. **Analysis/assessment** of the estate producing structured findings (dependencies, complexity, risk, readiness, tech debt).
3. A **modernization path/decision** per application — target state plus route (rehost / replatform / containerize / refactor / convert / rewrite; retire exists in the broader market vocabulary but is not evidenced in the fetched surfaces).
4. A **plan** sequencing the work (waves, ordered tasks, priorities).
5. **Transformation execution or driving** — code/artifact changes produced by the platform itself, by AI agents it orchestrates, or by humans it guides.
6. **Validation** of transformed output (builds, unit/integration tests, equivalence checks) — where execution exists.
7. **Tracking/reporting** of progress against the plan (dashboards, worklogs, reports, exports).

### Where they differ (variant space)

- Estate scope: whole-portfolio programs (AWS, CAST, Azure) vs single-application depth (vFunction, IBM per-app workbench).
- Execution depth: full execution (AWS, IBM, Azure-migration) vs guided execution through external code assistants (vFunction) vs no execution (CAST).
- Target substrate: specific cloud (AWS/Azure), stay-on-platform with modern languages (IBM Z), architecture-neutral modularization (vFunction).
- Vertical emphasis: mainframe (IBM, AWS-mainframe), Windows/.NET (AWS), Java/.NET monoliths (vFunction), mixed portfolios (CAST, Azure).
- AI posture: agentic orchestration vs fine-tuned LLM conversion vs context-provider for external assistants vs analytics-only.
- Delivery: SaaS workbench vs in-customer-environment components vs IDE tools.

## Canonical Model (L0–L3)

### L0 — Defining Invariant

An Application Modernization Platform exists to move an organization's **existing applications** to a **defined modern target state**, and is recognizable by four properties:

1. **Existing application estate as the object of work** — the platform's world is populated by applications that already exist (legacy/brownfield), held as inventory records with discovered facts. It does not primarily build greenfield software.
2. **Assessment producing structured understanding** — analysis of the estate (dependencies, complexity, risk, readiness, tech debt) that is distinct from, and feeds, the decision.
3. **An explicit modernization path per application** — a decided target state plus route (e.g., rehost / replatform / containerize / refactor / convert / rewrite), normally recorded as a plan.
4. **Tracked transformation to a changed deliverable** — the platform executes, orchestrates, or directly drives the transformation work and tracks it to a validated, delivered result (modernized code/artifacts/deployment).

Remove #1–2 and it is a generic build/deploy tool; remove #3 and it is analysis software; remove #4 and it is portfolio governance/assessment software. All four together are what make it a modernization *platform* rather than a converter, an analyzer, or a governance registry.

### L1 — Common Mature Structure

Present in most mature products; not definitional:

- discovery/inventory collection machinery (collectors, connectors, repo scans, imports in arbitrary formats)
- dependency mapping (application-to-application, application-to-data, network)
- portfolio/program-level dashboard and wave planning
- automated code conversion/refactoring — in current products commonly AI/LLM-assisted
- containerization and re-platforming generation (container images, IaC, deploy configs)
- database conversion (schema + code objects + data movement)
- validation machinery (builds, unit/integration tests, equivalence checks)
- transformation reports / worklogs / audit trails
- human-in-the-loop approval gates for critical actions
- IDE / code-assistant integration surfaces
- program roles and permissions on the workspace

### L2 — Variant / Optional Structure

- target substrate: specific public cloud, on-prem containers, stay-on-platform modernization (e.g., remain on Z with modern languages)
- strategy mix per application: rehost / replatform / refactor / rearchitect / rewrite / replace / retire
- estate verticals: mainframe (COBOL/PL/I), Windows/.NET, Java monoliths, mixed portfolios
- program shape: one-time migration/modernization program vs continuous always-on tech-debt remediation
- economics layer: TCO/business-case modeling, license-cost reduction framing
- adjacent analytics: open-source/IP risk, green/CO2 insights, AI-readiness scoring
- delivery posture: SaaS workbench vs in-customer-environment vs IDE-anchored vs CLI
- services-led vs product-led delivery (consultants/SIs often operate the platform)

### L3 — Vendor-specific Structure (research notes only)

- AWS Transform: workspace/connector/asset/objective/job/task/collaborator-request/worklog/artifact terminology; MGN-based rehost; Aurora PostgreSQL targets; landing-zone automation via Control Tower; Kiro powers; free-of-charge positioning.
- IBM: fine-tuned LLMs trained on Z; WCA4Z/WDA module naming; Z runtime interoperability guarantees.
- vFunction: domain-driven visualization, C4/sequence diagram generation, patented static+dynamic analysis, in-customer deployment.
- CAST: ISO 5055-based structural benchmarks; software-composition/IP risk; green-software metrics; sibling CAST Imaging.
- Microsoft: Azure Migrate appliance/collector; business-case module; partner-ISV ecosystem; Copilot migration agent (preview).

## Vendor-specific Findings

- AWS Transform's object model (objective → job → plan → tasks → collaborator requests → worklog) is the most explicit published program-management model in the sample; treat the specific nouns as vendor-specific, the shape (objective → planned tasks → tracked execution with HITL) as cross-product.
- IBM's "semantic equivalence" unit-testing of converted COBOL→Java is a notable validation pattern; only evidenced for IBM.
- vFunction's "context provider for code assistants" posture (MCP server, generated specs/prompts/integration tests) is a distinct execution philosophy: the platform drives transformation *through* external AI assistants rather than executing itself.
- CAST Highlight demonstrates the assessment-only pole; its absence of execution is the basis for a boundary finding below.
- Azure Migrate demonstrates that hyperscaler "migration hubs" are infrastructure-centric; their application-modernization surface (web apps → App Service/AKS) is comparatively thin.

## Boundary Findings

1. **vs Code Migration Platform (sibling leaf).** A code migration platform centers the code-conversion act itself (language-to-language, framework upgrade, database migration) as a developer-facing tool. An application modernization platform wraps the whole program: estate assessment → decision → planned execution → tracking, in which code conversion is one phase. Boundary test: a product with conversion but no estate-level assessment/program tracking is a code migration tool; a product managing a portfolio program of which conversion is one part is an application modernization platform. In practice the two categories are converging (agentic conversion inside program workbenches); the directory keeps both leaves, so the distinction should be preserved as program-wrapper vs conversion-act. **Flag for STATUS.md.**
2. **vs infrastructure/cloud migration tooling.** If the application's code and artifacts are unchanged (servers moved, data replicated), it is infrastructure migration. Application modernization changes the application itself. Azure Migrate is largely the former with a thin modernization surface; AWS Transform deliberately spans both, which makes it a boundary-spanning product rather than a counterexample.
3. **vs Application Portfolio Management (§14 leaf).** APM inventories and governs the estate (lifecycle, cost, risk, business fit) without transforming it. Assessment overlaps; execution is the differentiator. CAST Highlight sits between the two (deep code facts + recommendations, no execution).
4. **vs Static Code Analysis / Code Quality.** Those analyze code continuously in development for defects/quality; modernization platforms analyze for transformation decisions and drive the transformation. Analysis is a component, not the whole.
5. **vs AI Coding Assistant / AI Coding Agent.** Assistants/agents operate at developer-task scale inside a codebase; modernization platforms operate at program/estate scale with assessment, planning, and tracked multi-application transformation. The boundary is increasingly porous (vFunction feeds assistants; AWS Transform invokes coding agents), but the program wrapper remains the distinguishing structure.
6. **vs Low-code Application Platform.** The "replace/rebuild" route of a modernization program may land on a low-code platform, but building new applications is a different Type; the modernization platform's object is the existing estate.

## Historical / Market-Sample Check

Would older, regional, or differently positioned products still fit the L0?

- Older automated-transformation vendors (TSRI, Blu Age, Micro Focus/OpenText, Anubex — market knowledge, not fetched) follow the same shape: existing estate → assessment → conversion path → executed, tracked transformation, without any LLM. This supports keeping **AI/agentic assistance out of L0** (it is a current-market implementation layer, L1/L2).
- AWS App2Container (pre-agentic AWS tooling) executed containerization with deterministic analysis — same conclusion.
- Regional mainframe-modernization vendors and stay-on-platform modernization (IBM's "maintain Z runtimes") show the **cloud destination is not definitional** — the target state is user-defined; cloud is the most common variant.
- Azure Migrate shows a migration hub can carry the name "modernize" while being infrastructure-centric — the L0's "changed deliverable" property is what separates true application modernization from rehost-only programs.

Conclusion: the L0 holds across eras and positions; the sampled modern products differ mainly in the AI execution layer and program breadth.

## Uncertainties

- IBM in-product workflow detail unverified (docs 403). Claims about WCA4Z limited to product-page-level capabilities.
- GitHub Copilot app modernization (Microsoft's dev-tool-side modernization) not verified; the Microsoft sample is Azure Migrate. The final document should not make claims about that product.
- CAST Highlight's exact capability set (beyond the product page) unverified; its assessment-only posture is moderately confident (product page + use-case structure) but not confirmed from a capabilities doc.
- vFunction operational detail (docs unreachable) limited to platform-page claims.
- The exact market boundary between "Application Modernization Platform" and "Code Migration Platform" is converging in the AI era; the directory distinction is preserved but real products increasingly span both.
- Retirement/replace routes ("6R/7R" vocabulary) are common market knowledge but not evidenced in the fetched surfaces; kept out of precise claims.

## Final Synthesis

An Application Modernization Platform is a program-level platform for transforming an organization's existing application estate toward defined modern targets. Its world consists of: an inventoried estate of existing applications; assessment findings about that estate (dependencies, complexity, risk, readiness); a decided modernization path per application; a plan sequencing the work; transformation work executed or driven by the platform (increasingly by AI agents under human approval); validation of the changed output; and program tracking to delivered results. The defining core is deliberately small: existing estate + assessment + explicit path + tracked transformation. AI assistance, cloud destinations, portfolio dashboards, containerization, database conversion, and continuous tech-debt remediation are common mature or variant structures, not definitional ones.
