# Code Migration Platform

## Overview

A **Code Migration Platform** is software that transforms existing code from a declared source form into a declared target form — a newer language version, a different framework or library, another database dialect or schema, a different runtime — and delivers the result as reviewable changes that a developer inspects and accepts through the normal version-control workflow.

The defining structure is small:

```text
Existing code in a source form
└── Declared target form (an explicit source → target conversion contract)
    └── Transformation performed by the system itself
        └── Equivalent-behavior output, delivered as reviewable changes
```

Everything else commonly associated with the category — AI-driven conversion, catalogs of prebuilt migrations, dry-run previews, dashboards, orchestrated campaigns across hundreds of repositories, automatic repair of failed builds — is widespread in current products but is not what makes the product a code migration platform. Older, purely deterministic converter tools with no AI and no console fit this definition exactly as well as modern agentic platforms.

The category's world is **brownfield**: it works on code that already exists. When a product primarily creates new applications from templates, produces analysis findings without performing the transformation, or wraps conversions inside a portfolio-wide modernization program with estate assessment and per-application route decisions, it has crossed into a different Application Type.

## Users & Context

Primary users:

- **Software engineers and developers** — run conversions on their own projects, review the changed code, resolve items the tool could not convert, and accept the result into the codebase.
- **Platform and tooling teams** — own migration standards at organization scale: which recipes or converters to use, how conversions roll out across repositories and teams, and how the resulting changes are reviewed and merged.

Secondary users:

- **Migration / modernization engineers** — prepare projects for conversion, tune conversion configurations, and work through the backlog of items that need manual attention after automated conversion.
- **Engineering managers / transformation leads** — track migration progress across repositories and teams, often through dashboards and project-management integrations.

Typical contexts: upgrading a language runtime before support ends; moving a framework to a new major version; leaving a proprietary database engine; adopting a modern runtime or library set; unifying codebases after an acquisition; rolling a compliance or standardization change through many repositories. The work happens inside the organization's existing engineering workflow — repositories, builds, pull requests — rather than in a separate operational environment.

## Core Model

### The Defining Core

```text
Existing code in a source form
└── Declared target form (source → target conversion contract)
    └── System-executed transformation
        └── Reviewable, equivalent-behavior output
```

Four properties. If any one is removed, the product is no longer recognizable as a code migration platform:

- **Existing code as the object of work.** The input is code that already exists — application source, build files, database schemas and scripts, embedded SQL. Without this property (input is templates or specifications), the product is a code generator.
- **A declared target form.** Every conversion is bound to an explicit contract: which source form, which target form, and — where relevant — which libraries or engine features are in scope. The contract may be a named recipe or codemod, a supported source-to-target version matrix, or a migration project configuration. Without this property (open-ended code editing on request), the product is an AI coding assistant.
- **The system performs the transformation.** The product outputs changed code — it executes the conversion, not merely recommends it. Findings, readiness scores, and effort estimates may precede the conversion, but the defining output is changed code. Without this property, the product is a static analysis or assessment tool.
- **Equivalent-behavior output delivered as reviewable changes.** The transformed code is intended to do what the original did, and it is delivered in a form the developer can inspect — a diff, a patch, a pull request, an editable converted artifact — before it replaces the original. No established product in this category applies converted code to the codebase sight unseen; the review-before-apply discipline is structural, not cosmetic.

### Standard Capabilities

Mature products commonly add the following. They make conversion practical and trustworthy at scale but do not define the Type:

- **Pre-conversion verification and analysis** — checking the project builds before converting, discovering which conversions apply, scoring readiness, or producing assessment reports that list what will and will not convert.
- **A catalog of prebuilt conversions** — searchable, versioned recipes, codemods, or supported source-to-target matrices maintained by the vendor and community.
- **Authorable custom conversions** — configuration files and authoring tools (including AI-assisted ones) for writing organization-specific transformations, plus mechanisms for emulating features the target platform lacks.
- **Preview surfaces** — dry runs, diff views, and inspection of converted output before anything is applied, often with per-change explanations of why a change was made.
- **Validation machinery** — builds and tests run after conversion; checks on generated pull requests; compile verification in the local environment.
- **Reporting** — summaries of what changed, lists of files touched, unresolved items, and suggested next steps.
- **Iterative repair** — re-running failed steps, patching generated pull requests when checks fail, and running additional conversion passes (for example, a dependency-upgrade pass after a language-upgrade pass).
- **Delivery into version control** — applying patches, opening branches and pull requests, and offering commit strategies (direct commit versus pull request).
- **Scale orchestration** — running conversions across organizations of repositories, splitting large migrations into sharded parallel tasks, tracking task status, and syncing with project-management tools.

### One Contract, Many Implementations

The Core Model is written in conceptual terms. Implementations differ on every layer:

```text
Concept:   Source → target conversion contract
Implementations:  named and versioned recipes or codemods in a catalog,
                  supported source/target version or engine matrices,
                  per-project migration configuration

Concept:   Transformation mechanism
Implementations:  deterministic rules over syntax/semantic trees,
                  AI models producing conversion patches,
                  hybrid: deterministic transforms plus AI-assisted fixups

Concept:   Validation
Implementations:  local builds and tests after conversion,
                  CI checks on generated pull requests,
                  assessment reports with manual-action lists

Concept:   Delivery
Implementations:  apply-patch acceptance in the IDE,
                  commit-strategy choice (commit / PR / branch),
                  one pull request per task in an orchestrated campaign
```

A reader who has only seen one shape — say, an AI assistant upgrading a project inside an IDE — should still be able to recognize a deterministic build-plugin engine or a database schema converter as the same Type.

## How It Works

### The core loop

```text
Choose the conversion (recipe / codemod / source→target contract)
→ point it at existing code (a project, repository, schema, or set of repositories)
→ verify the code is ready (builds, dependencies resolvable, scope understood)
→ preview or assess (dry run, findings, conversion plan)
→ convert (the system produces changed code)
→ validate (builds, tests, checks)
→ review the changes (diff, pull request, converted artifacts)
→ accept and merge (human decision)
→ repair and iterate (re-run failures, additional passes, manual items)
```

This loop runs at every scale the product supports: one developer converting one project inside an IDE, a tooling team running a recipe across an organization's repositories, or an orchestrated campaign opening hundreds of reviewable pull requests.

### Establishing the conversion contract

The conversion always begins with an explicit contract. In practice this takes three recurring shapes: picking a **named, versioned conversion unit** from a catalog (a recipe or codemod, often with configurable parameters such as target version); selecting a pair from a **supported source-to-target matrix** (which source languages, versions, or database engines convert to which targets); or configuring a **migration project** that records the source, the target, and the scope. Products commonly constrain conversions to known, tested pairs — a conversion is offered because someone maintains it, not because any input is theoretically possible.

### Verifying the code is ready

Mature products gate the conversion behind pre-conditions: the project builds successfully in its current form, dependencies resolve, and the code does not depend on resources the conversion environment cannot reach. This verification is not bureaucracy — conversion quality depends on it, and products document explicit failure conditions when pre-conditions are not met. Alongside the gate, assessment machinery (readiness findings, lists of what will and will not convert) sets expectations before work begins.

### Converting

The system produces changed code according to the contract. Three mechanisms coexist in the current market:

- **Deterministic transformation** — rules applied to a structured representation of the code, producing minimal, formatting-preserving changes. Predictable and repeatable; typical of catalog-driven engines and schema converters.
- **AI-driven conversion** — models generate the converted code, usually scoped by the contract and checked by builds. Typical of assistant-embedded and managed conversion flows.
- **Hybrid** — deterministic transforms for the mechanical bulk, AI-assisted fixups for what rules cannot reach, often combined in a single migration workflow.

Build files, dependency manifests, and schemas are typically transformed alongside source code — a migration that left the build unbuildable would not be a migration.

### Validating and handling what does not convert

Because the output must keep doing what the original did, validation is structural: builds must succeed, tests must pass, generated changes are checked before merge. Partial conversion is normal and explicitly supported — items the tool cannot convert become tracked follow-up work in one of several recurring forms: manual guidance ("how to create the equivalent in the target"), generated emulation code that supplies the missing feature, or a separate conversion pass. The honest product treats "not convertible automatically" as a first-class outcome, not an error to hide.

### Reviewing and accepting

Changed code enters the developer's normal workflow: a diff to inspect, a patch to apply, a pull request to review. Products commonly explain their changes (why each change was made), report remaining issues, and let the human choose the delivery strategy. The acceptance decision — merging converted code into the codebase — stays with the organization: nothing applies until it is accepted, and some products add explicit approval steps before critical actions.

### Repairing and iterating

Failed steps are re-run individually; failed checks can trigger automated repair of the generated changes, or even repair of the converter itself when failures look systematic; larger migrations run as sequences of passes (for example, a language upgrade followed by a dependency upgrade). Migration is iterative by nature, and mature products model that iteration rather than assuming a one-shot result.

### Core vs Common vs Optional

**Defining core** — without these, not a code migration platform:

- existing code in a source form as the object of work
- a declared source→target conversion contract
- system-executed transformation producing changed code
- equivalent-behavior output delivered as reviewable changes with human acceptance

**Standard capabilities** — present in most modern products:

- pre-conversion verification and assessment
- catalog of prebuilt conversions; authorable custom conversions
- preview/diff surfaces and change explanations
- validation machinery (builds, tests, checks)
- reporting and iterative repair
- delivery into version control with commit/PR strategies
- scale orchestration across repositories and teams

**Variant / optional** — depends on mechanism, segment, and scale:

- AI vs deterministic vs hybrid mechanism
- build-plugin/CLI, IDE-embedded, desktop, or SaaS console delivery
- single-repo vs fleet-scale operation; sharded campaigns
- coupling to a specific cloud or database vendor's targets
- free open-source engines alongside commercial platforms

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Conversion catalog / marketplace

The discovery surface for what can be converted.

- searchable list of available conversions with versions, parameters, and documentation; supported source→target combinations
- primary actions: search, inspect a conversion's contract, select one to run

### Project / job configuration

Where the conversion contract is set up.

- source selection (project, repository, schema), target selection, parameters (target versions, dependency lists, file scoping), and connectivity to source-control systems
- primary actions: choose source and target, configure parameters, verify pre-conditions, start the conversion

### Preview / diff surface

The inspection surface before anything is applied.

- source-vs-converted views per file, lists of affected files, per-change explanations
- primary actions: inspect changes, understand why a change was made, accept or reject, choose delivery strategy (apply patch, commit, open pull request)

### Execution dashboard

The monitoring surface, especially at scale.

- progress of conversion runs, per-task or per-repository status, logs, check results; task statuses that humans can update
- primary actions: monitor progress, re-run failed tasks, trigger repair, cancel runs

### Pull-request / delivery surface

The acceptance surface inside version control.

- generated branches and pull requests with descriptions, check summaries, and review threads
- primary actions: review diffs, run or inspect checks, comment, merge or request changes

### IDE-embedded surfaces

Where conversion meets the developer's editor.

- a way to request a conversion for the open project, progress views, and diff/accept flows without leaving the IDE
- primary actions: start a conversion, watch progress, view and apply the proposed changes

### Reports

The summary surface for decisions and follow-up.

- conversion summaries, changed-file lists, unresolved/manual items, assessment findings
- primary actions: export or share, feed manual items into the backlog

## Important Rules / Behaviors

### The conversion is contract-bound

A conversion happens only for a declared source→target pair the product supports (or a custom conversion someone authored). The product does not freely rewrite code on request; scope discipline is what distinguishes migration from general-purpose code editing.

### Nothing is applied unseen

Changed code is delivered for human review — as a diff, patch, or pull request — before it replaces the original. Platforms that orchestrate many repositories still deliver per-repository changes into review workflows. This is the trust foundation of the whole category.

### Equivalence is the intent, minimal change is the posture

The output is expected to behave like the original. Mature products convert minimally — changing what the target form requires and preserving formatting and structure wherever possible — so that the diff shows exactly what the migration changed and nothing else.

### Partial conversion is a normal outcome

Not everything converts automatically. The system records what did not convert and routes it to guidance, generated emulation, or follow-up passes. A clean migration report includes a list of remaining manual work; silence about unconvertible items would be a defect, not a feature.

### Pre-conditions gate the conversion

The code must typically build and be self-contained before conversion; unreachable dependencies, mixed tooling, or missing source versions are documented failure conditions. Readiness is verified before work starts because conversion quality depends on it.

### Failure is first-class

Conversions can fail, generated changes can break builds, and products expose failure explicitly: per-task failure states, re-run controls, and in some products automated recovery that patches the generated changes or repairs the converter. Iteration, not one-shot success, is the operating assumption.

### The converter is a maintained asset

Prebuilt conversions are versioned, parameterized, and tested artifacts — updated as frameworks and platforms evolve, repairable when they produce systematic failures, and shareable across teams. The catalog, not the individual run, is where migration knowledge accumulates.

### Analysis is the front half, not the product

Dry runs, readiness findings, and assessments exist to set up the conversion. A product that stops at findings — that never produces changed code — has crossed into assessment tooling.

## Variants

Common shapes of the Type:

- **By target domain** — language version upgrades (code to a newer runtime version); framework and library upgrades (one major version to the next, including build-file changes); database and SQL migration (schemas, stored logic, embedded SQL, and ETL scripts converted between engines or dialects); cross-language translation; runtime and platform moves; and adjacent remediation uses of the same machinery (security fixes, styling consistency, internationalization, standardization after mergers).
- **By mechanism** — deterministic rule engines; AI-driven conversion; hybrid workflows combining both.
- **By delivery surface** — build-tool plugins and CLIs that run in the developer's environment; IDE-embedded conversion flows; desktop project tools; SaaS consoles with registries and dashboards — frequently combined.
- **By scale posture** — single-project tools; engines run per repository; platforms that operate across an organization's repositories with orchestrated, sharded campaigns.
- **By commercial shape** — open-source engines paired with commercial platforms; vendor-managed conversion services; free desktop tools; subscription SaaS with pro/enterprise tiers.
- **By target coupling** — neutral converters (any supported target) versus tools whose targets are a specific vendor's managed services.

A variant remains a variant unless it changes the core objects or workflow: assessment-only products that never convert, and program wrappers around whole application estates, belong to neighboring Types.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Application Modernization Platform | closest sibling | the modernization platform wraps the whole program — estate inventory, assessment, per-application modernization decision (rehost/replatform/refactor/convert/rewrite), tracked multi-application delivery — of which conversion is one phase; the code migration platform is the conversion act itself, at whatever scale, starting from a source→target contract rather than from a portfolio decision. The two converge in the AI era (agentic conversion inside program workbenches; project tracking around large migrations), but the discriminator holds: what the product starts from and owns — the estate decision or the conversion |
| AI Coding Assistant / AI Coding Agent | different organizing object | assistants are general-purpose and conversational at task scale, with no fixed conversion contract and no equivalence-to-original expectation; migration products are organized around the migration itself (contract, catalog, validation, delivery). Assistant-embedded upgrade features are a growing convergence zone, but the structure differs |
| Static Code Analysis / Code Quality Platform | component relationship | analysis produces findings; migration produces changed code. Analysis commonly serves as the front half of migration (readiness findings, dry runs), and some engines ship both analysis and transformation capabilities — the defining output of this Type remains the transformation |
| Project Scaffolding / Code Generator | different input | generators create new code from templates or specifications; migration presupposes existing code and converts it to an equivalent form |
| Source Code Hosting / Code Review Platform | delivery relationship | hosting and review systems store, diff, and gate code; the migration platform produces the changed code that flows into them |
| ETL / Data Migration Platform | different object | data migration moves data; code migration transforms code. Schema definitions, DDL, and ETL scripts are code-like artifacts and belong here; the data itself does not |
| Build Automation System | adjacent | build tools compile and package code without changing its form; migration tools change the code itself (even when they run inside the build) |
| Application Portfolio Management | adjacent | governs the application estate (lifecycle, cost, risk) without transforming any code |

The most important boundary is with **Application Modernization Platform**, confirmed jointly from both sides: a product that manages a portfolio program of which conversion is one part belongs to the modernization platform; a product whose center is the code-conversion act belongs here.

## Representative Products

- **OpenRewrite** — open-source deterministic recipe engine for automated framework migrations and refactoring, run via build-tool plugins and CLI
- **Moderne** — commercial platform running the OpenRewrite recipe catalog at fleet scale (multi-repository dry runs, mass commit/PR strategies)
- **Amazon Q Developer (code transformation)** — managed AI-driven conversion delivered in the IDE, centered on language and dependency upgrades
- **AWS Schema Conversion Tool** — desktop project-based conversion of database schemas, SQL, and ETL scripts between engines, with manual-guidance and emulation fallbacks
- **Codemod** — AI-first codemod platform: registry of versioned conversions, AI-assisted authoring, and orchestrated campaigns producing reviewed pull requests across repositories

Together these span the Type's range: deterministic engine and its fleet-scale platform, managed AI conversion, database-dialect conversion, and an orchestrated codemod platform. The Core Model was checked against non-AI, non-platform shapes (build-plugin engine, desktop schema converter) to avoid defining the Type by the current AI-platform pattern.

## Sources

Research date: **2026-09-07**

- OpenRewrite — docs introduction: https://docs.openrewrite.org/ ; running-recipes quickstart: https://docs.openrewrite.org/running-recipes/getting-started
- Moderne — platform quickstart: https://docs.moderne.io/user-documentation/moderne-platform/getting-started/running-your-first-recipe
- Amazon Q Developer — user guide (what is / Java code transformation): https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html ; https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/code-transformation.html
- AWS Schema Conversion Tool — user guide (what is): https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html
- Codemod — docs introduction: https://docs.codemod.com/ ; campaigns: https://docs.codemod.com/platform/campaigns

> Sourcing limitations: assistant-embedded migration documentation (GitHub Copilot app modernization) and Google's SQL-translation service documentation were not reachable from the research environment during this pass; no claims in this document rely on them, and the assistant-embedded and SQL-translation poles are described structurally from the sampled products. Precise operational details (exact supported version matrices, numeric limits, product-specific parameters and failure conditions) are intentionally not stated here; they are recorded in the paired Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
