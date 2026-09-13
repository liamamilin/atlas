# Application Modernization Platform

## Overview

An **Application Modernization Platform** is a platform for transforming an organization's **existing applications** toward a **defined modern target state** — newer architectures, runtimes, languages, frameworks, or hosting environments. It discovers and assesses the application estate, supports an explicit modernization decision for each application, executes or directly drives the transformation work, and tracks that work to validated, delivered results.

The defining core is small:

```text
Existing application estate (the object of work)
└── Assessment producing structured understanding
    └── An explicit modernization path per application
        └── Tracked transformation to a changed, validated deliverable
```

Everything else commonly associated with this category — AI-assisted code conversion, containerization, cloud destinations, portfolio dashboards, wave planning, continuous tech-debt remediation — is widespread in current products but is not what makes the platform a modernization platform. Older automated-transformation tools without any AI, and products that modernize applications while they stay on their existing platform, fit the same definition.

The platform's world is **brownfield**: it works on applications that already exist. When a product primarily builds new applications, moves infrastructure without changing the application, or merely analyzes code without driving a transformation program, it has crossed into a different Application Type.

## Users & Context

Primary users:

- **Enterprise / solution architects** — own the assessment and the modernization decision: what the estate looks like, which route each application takes, what the target state is.
- **Migration / modernization engineers** — run the transformation work: prepare inputs, execute or supervise automated conversion, resolve findings.
- **Application owners and delivery teams** — know the applications being transformed; review changed code, validate behavior, accept results.

Secondary users:

- **Program / project managers** — track waves, progress, and blockers across many applications.
- **Executive sponsors (CIO/CTO office)** — consume business cases, cost models, and progress reporting that justify and steer the program.
- **Developers and AI coding assistants** — increasingly the hands that perform code-level changes, guided by the platform.

Typical contexts: an enterprise running mainframe, Windows/.NET, or aging Java estates; a cloud-migration program that must decide what to rehost versus transform; a license-cost-reduction initiative (leaving expensive legacy runtimes or databases); a tech-debt reduction effort; or a skills-risk situation where the languages the estate is written in are becoming unsustainable to staff.

## Core Model

### The Defining Core

```text
Existing application estate
└── Assessment findings
    └── Modernization path (per application)
        └── Plan (sequenced work)
            └── Transformation work
                └── Validated deliverable
                    └── Program tracking
```

Four properties. If any one is removed, the product is no longer recognizable as an application modernization platform:

- **Existing application estate as the object of work.** The platform's world is populated by applications that already exist, held as inventory records with discovered facts (technologies, size, dependencies, ownership). It does not primarily create greenfield software.
- **Assessment producing structured understanding.** Analysis of the estate — dependencies, complexity, risk, readiness for the target — exists as a distinct activity with distinct outputs, and feeds the decision rather than being fused with it.
- **An explicit modernization path per application.** For each application, a decided target state and route (for example: keep as-is and rehost, re-platform to containers, refactor into modular services, convert to a modern language or database, or rewrite). The path is normally recorded as a plan that can be reviewed and adjusted.
- **Tracked transformation to a changed deliverable.** The platform executes, orchestrates, or directly drives the transformation — producing changed code, artifacts, or deployments — and tracks that work to a validated result. A product that only assesses and recommends, without carrying or driving the change, sits at the boundary of the Type (see Related Application Types).

### Standard Capabilities

Mature products commonly add the following. They make the platform practical at program scale but do not define it:

- **Discovery machinery** — collectors, connectors, or repository scans that build the inventory from servers, source repositories, databases, and network configurations; imports in arbitrary formats are commonly accepted.
- **Dependency mapping** — application-to-application, application-to-data, and network dependencies, so that transformation can be sequenced without breaking connected systems.
- **Portfolio dashboard and wave planning** — grouping applications into ordered batches (waves) so a large estate can be transformed incrementally.
- **Automated conversion and refactoring** — in current products, commonly performed by AI models or agents under human supervision; in older products, by deterministic rule-based converters.
- **Containerization and re-platforming generation** — producing container images, deployment configurations, and infrastructure definitions for the target runtime.
- **Database conversion** — transforming schemas, stored logic, and data access code toward a target database, alongside the application changes that depend on it.
- **Validation machinery** — builds, unit and integration tests, and behavioral comparisons that check the transformed application still does what the original did.
- **Reports, worklogs, and audit trails** — natural-language records of what was changed, by whom or by what, and why.
- **Human approval gates** — critical actions (merging transformed code into main branches, deploying to production) commonly sit behind explicit human approval in program-scale products.
- **IDE and coding-assistant integration** — surfaces that let developers and AI assistants work on the transformation from their own tools while the platform keeps the program state.
- **Program roles and permissions** — administrator, approver, contributor, and viewer roles over the program workspace.

### One Structure, Many Implementations

The Core Model is written conceptually. Implementations differ on every layer:

```text
Concept:   Estate inventory
Implementations:  automated discovery agents, repository scans, imported spreadsheets,
                  runtime observation of live servers

Concept:   Assessment
Implementations:  static code analysis, runtime/dynamic analysis, dependency graphs,
                  complexity scoring, cost/TCO modeling, cloud-readiness rules

Concept:   Modernization path
Implementations:  named routes (rehost / replatform / containerize / refactor /
                  convert / rewrite), per-application target architecture definitions

Concept:   Transformation work
Implementations:  deterministic converters, AI agents executing planned tasks,
                  generated prompts and specs executed by external coding assistants,
                  human engineers guided by the platform

Concept:   Validation
Implementations:  automated builds, ported unit tests, generated integration tests,
                  behavioral-equivalence comparisons between old and new code
```

## How It Works

### The core loop

```text
Connect to the estate (repositories, servers, databases, network configs)
→ discover and inventory the applications
→ assess each application (dependencies, complexity, risk, readiness)
→ decide the path per application (target state + route)
→ plan the work (waves, ordered tasks)
→ execute the transformation (automated / AI-assisted / guided)
→ validate the result (builds, tests, behavioral comparison)
→ deliver the changed code and artifacts for review and deployment
→ track progress and re-assess as the estate changes
```

This loop runs at two scales at once: per application (assess → decide → transform → validate) and per program (many applications sequenced into waves, with portfolio-level tracking).

### Deciding the path

The assessment produces the facts; the organization chooses the route. The recurring route vocabulary across products:

- **Rehost** — move the application's hosting environment without changing the application. This is the boundary with infrastructure migration; it is often the on-ramp to a modernization program rather than its endpoint.
- **Re-platform / containerize** — package the application for a modern runtime (containers, managed services) while keeping its code largely intact.
- **Refactor / re-architect** — restructure the application itself: break a monolith into modular services, untangle shared state, modernize internal architecture — while preserving behavior.
- **Convert** — translate the code to a modern language, framework, or database (for example, legacy procedural code to a modern managed language; a legacy database engine to an open one).
- **Rewrite** — regenerate a module or service from extracted specifications, discarding the original implementation.

A single program typically mixes routes: some applications rehosted, some containerized, a few deeply refactored.

### Executing the transformation

Execution is where products differ most, and where the current market has converged on AI assistance:

- The platform **executes** the change itself: agents or converters transform the code, run builds, repair errors, run tests, and deliver the result — with humans approving plans and critical steps.
- The platform **drives external hands**: it produces the architectural context, specifications, prompts, and tests, and coding assistants or developers perform the actual code changes under its guidance.
- The platform **routes and tracks**: it produces the plan and the findings, and humans (often with generic tooling) perform the work while the platform tracks progress.

In all three postures, the changed code is typically delivered back into the organization's own repositories — commonly on a separate branch — for human review, rather than silently replacing production code.

### Validating

Because the transformed application must keep doing what the original did, validation is structural, not optional: builds must succeed; ported or generated tests must pass; some products compare the behavior of old and new implementations directly (for example, generating tests that check the new code produces the same outcomes as the legacy code it replaced).

### Tracking

Program-scale products maintain a durable record of the work: plans with steps and sub-steps, logs of every action taken by the system and by humans, per-application status, and portfolio-level progress reporting. This record is what makes a multi-year, multi-application program manageable — and auditable.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Portfolio dashboard

The program-level entry surface.

- the application estate with per-application status, risk, and route
- wave/progress views across the program
- primary actions: drill into an application, adjust grouping, review program metrics

### Assessment report (per application)

The decision surface for one application.

- technologies, size, dependencies, complexity and risk findings, readiness for candidate targets, recommended route and effort
- primary actions: review findings, choose/adjust the route, feed the decision into planning

### Plan / wave board

The sequencing surface.

- ordered tasks or waves, owners, dependencies, status
- primary actions: approve or edit a plan, reorder work, assign owners, advance waves

### Transformation workbench

The execution surface.

- the current job or task, its steps and sub-steps, a conversational interface with the transformation agent in AI-driven products, and a worklog of actions taken
- primary actions: start/stop work, answer human-in-the-loop requests, inspect what changed and why

### Code review surface

The acceptance surface for changed code.

- transformed code delivered into the organization's repository (commonly on a review branch), with reports of modified files and remaining issues
- primary actions: review diffs, run tests, merge or request changes

### Reports and exports

The stakeholder surface.

- business cases, cost models, progress reports, audit trails; exports into external project-tracking tools

### IDE / assistant integration

The developer-side surface.

- plugins or protocol-based integrations that let developers and AI coding assistants participate in the transformation from their own environment, against the same program state

## Important Rules / Behaviors

### Source access determines the possible routes

What the platform can do depends on what it can reach. Some routes require application source code; others can work from runtime artifacts of live servers. Whether a given product can containerize or convert without source code varies by product and route — this is a practical gating rule when planning a program.

### Behavior preservation is the expectation

For refactor and convert routes, the transformed application is expected to behave like the original. Validation machinery (tests, builds, behavioral comparison) exists to check this, and gaps found by validation become tracked work.

### Changed code is delivered for review, not imposed

Transformed code lands in the organization's own repositories — commonly on a dedicated branch — and human owners accept it. Some products additionally restrict critical actions, such as merging transformed code into main branches or deploying to production, behind explicit approval roles.

### Assessment outputs are decision inputs, commonly directional

Findings, effort estimates, and cost models inform decisions; they are directional planning aids rather than guarantees. Programs treat them as hypotheses to refine, not contracts.

### Estate facts go stale

The inventory and assessments reflect a point in time. Estates change continuously, so discovery and assessment are repeated — and some products now run assessment and remediation continuously rather than as a one-time program.

### The platform works on the estate as it exists

The input is the real, messy, documented-and-undocumented estate. A large share of assessment value is making undocumented applications understandable (dependencies, business logic, dead code) before any transformation decision is made.

## Variants

Common shapes of the Type:

- **By estate vertical** — mainframe modernization (procedural legacy code toward modular services and modern languages), Windows/.NET estate modernization (legacy framework and database toward cross-platform runtimes), Java/.NET monolith decomposition, mixed-portfolio programs.
- **By program shape** — one-time migration/modernization programs (assess → transform → done) versus continuous modernization (always-on tech-debt analysis and remediation across the repository estate).
- **By execution posture** — platform-executed transformation (deterministic converters or AI agents), assistant-driven transformation (the platform supplies context, specs, and tests; coding assistants do the editing), and assessment-first products that route decisions to other tooling.
- **By target substrate** — a specific public cloud, on-premises container platforms, or staying on the existing platform while modernizing languages and architecture.
- **By delivery posture** — vendor-operated web workbenches, components installed inside the customer environment, IDE-anchored tools, and CLI tooling — often combined.

A variant remains a variant unless it changes the core objects or workflow: assessment-first products that never execute sit at the Type's boundary (see below), and infrastructure-only migration is a different Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Code Migration Platform | closest sibling | centers the code-conversion act itself (language-to-language, framework, database) as a developer-facing tool; the modernization platform wraps the whole program — estate assessment, decision, planned execution, tracking — of which conversion is one phase |
| Application Portfolio Management | adjacent | inventories and governs the estate (lifecycle, cost, risk, business fit) but does not transform applications; assessment overlaps, execution does not |
| Cloud migration tooling / infrastructure migration | adjacent | moves servers, data, and networks while leaving the application unchanged; modernization changes the application itself. Migration hubs often include a thin modernization surface |
| Static Code Analysis / Code Quality Platform | component relationship | analyzes code continuously in development for defects and quality; the modernization platform analyzes for transformation decisions and drives the transformation |
| AI Coding Assistant / AI Coding Agent | different scale | operates at developer-task scale inside a codebase; the modernization platform operates at program/estate scale with assessment, planning, and tracked multi-application transformation. The two increasingly interlock (platforms drive assistants) |
| Low-code Application Platform | different object | builds new applications; may serve as the destination of a "replace" route within a modernization program, but is not the program itself |
| Internal Developer Platform | different purpose | an ongoing delivery substrate for engineering teams; a modernization program is a bounded transformation of an existing estate |

The most important boundary is with **Code Migration Platform**: the two categories are converging as conversion becomes AI-driven inside program workbenches. The working distinction is program wrapper versus conversion act — a product that manages a portfolio program of which conversion is one part belongs here; a product that is primarily the conversion tool belongs there.

A second important boundary is the **assessment-only pole**: products that produce estate facts, routes, and effort estimates but perform no transformation are better understood as portfolio-intelligence tools that feed modernization programs than as modernization platforms proper.

## Representative Products

- **AWS Transform** — agentic transformation workbench spanning infrastructure migration, application modernization (mainframe, Windows/.NET, custom code), and continuous tech-debt reduction
- **IBM watsonx Code Assistant for Z** — mainframe-depth AI discovery, refactoring, and COBOL/PL/I-to-Java conversion anchored in the IDE
- **vFunction** — architectural analysis (static + runtime) that drives AI-assisted monolith decomposition through coding assistants
- **CAST Highlight** — assessment-first portfolio intelligence: code-derived facts, cloud-migration routes, risk and readiness scoring
- **Azure Migrate** — hyperscaler migration hub (decide → plan → execute) with an application-modernization surface for web apps and databases

Together these span the Type's range: full-lifecycle program workbench, deep vertical conversion, architecture-driven refactoring, assessment-only intelligence, and migration-centric hub.

## Sources

Research date: **2026-09-06**

- AWS Transform — product page: https://aws.amazon.com/transform/ ; User Guide (What is AWS Transform): https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html ; FAQ: https://aws.amazon.com/transform/faq/
- AWS App2Container (historical reference): https://docs.aws.amazon.com/app2container/latest/UserGuide/what-is-a2c.html
- Microsoft Azure Migrate — overview: https://learn.microsoft.com/en-us/azure/migrate/migrate-services-overview
- IBM watsonx Code Assistant for Z — product page: https://www.ibm.com/products/watsonx-code-assistant-z
- vFunction — platform page: https://vfunction.com/platform/
- CAST Highlight — product page: https://www.castsoftware.com/highlight

> Sourcing limitations: IBM's documentation site and vFunction's documentation site were not reachable from the research environment; claims for those products are calibrated to their official product pages. Microsoft's developer-tool-side modernization documentation was not reachable; Azure Migrate is used as the Microsoft sample. Precise operational details (exact version targets, numeric limits, pricing) are intentionally not stated in this document; they remain in the paired Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
