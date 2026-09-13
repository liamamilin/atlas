# Research Notes — Code Migration Platform

Research date: 2026-09-07

## Research Goal

Understand what a **Code Migration Platform** actually is as a class of software: what objects exist inside it, what its core workflow is, how conversion and human work divide, what its interfaces look like, and where its boundaries lie against neighboring Types — especially the already-processed sibling **Application Modernization Platform** (which flagged this leaf for joint boundary review), plus AI coding assistants, static code analysis, code generators, and data-migration tooling.

## Initial Boundary

Working hypothesis before research:

- A Code Migration Platform centers the **code-conversion act itself**: transforming existing code from one form to another (language version, framework/library, database dialect/schema, runtime) as a developer/engineer-facing tool.
- Nearest neighbors: **Application Modernization Platform** (§12 sibling — program wrapper vs conversion act, per its research notes), **AI Coding Assistant / AI Coding Agent** (task-scale, general-purpose), **Static Code Analysis / Code Quality** (analysis without transformation), **Project Scaffolding / Code Generator** (new code, not converted code), **Source Code Hosting / Code Review** (stores/reviews, does not transform), **ETL / Data Migration** (data, not code).
- "Migration" here must be distinguished from two homonyms: infrastructure/data migration (moving data/servers) and user-data migration (moving accounts between products).

## Research Questions

1. What objects exist inside such a system? (conversion jobs, recipes/codemods, catalogs, plans, diffs, validation results, PRs)
2. What is the core workflow from source code to accepted converted code?
3. How is equivalence to original behavior established and checked?
4. What human role remains after automation?
5. At what scale does it operate — file, repo, fleet of repos, organization?
6. What surfaces does it expose (CLI, build plugin, IDE, desktop app, SaaS console)?
7. Which target kinds are common (language version, framework, SQL/schema dialect, runtime)?
8. Where is the boundary vs Application Modernization Platform, AI coding assistants, code generators, static analysis?
9. Historical check (market-sample check): would older transpilers and schema-conversion tools, and non-AI tools, still fit the definition?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different delivery shapes:

| Product | Philosophy / shape | Why sampled |
|---|---|---|
| **OpenRewrite / Moderne** | open-source deterministic recipe engine (build plugins/CLI) + commercial multi-repo platform | the deterministic, non-AI pole; engine-vs-platform split; OSS-first |
| **Amazon Q Developer (code transformation)** | managed AI conversion delivered inside the IDE (Java language upgrades) | the managed-AI conversion pole; per-project job flow |
| **AWS Schema Conversion Tool** | desktop project-based tool converting database schemas/SQL between engines | the database/schema dialect pole; conversion-with-manual-fallback model |
| **GitHub Copilot app modernization** | assistant-embedded upgrade tooling | attempted; docs unreachable (404 ×2) — see Sources |

**Codemod** was added as a fourth researched product (AI-first codemod platform with registry + campaigns) after the Copilot docs proved unreachable; it also fills the orchestration-at-scale pole.

## Sources

All fetched 2026-09-07.

- OpenRewrite docs — Introduction: https://docs.openrewrite.org/
- OpenRewrite docs — Quickstart (running recipes): https://docs.openrewrite.org/running-recipes/getting-started
- Moderne docs — Platform quickstart: https://docs.moderne.io/user-documentation/moderne-platform/getting-started/running-your-first-recipe
- Amazon Q Developer User Guide — What is: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html
- Amazon Q Developer User Guide — Java code transformation: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/code-transformation.html
- AWS SCT User Guide — What is the AWS Schema Conversion Tool: https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html
- Codemod docs — Introduction: https://docs.codemod.com/
- Codemod docs — Campaigns: https://docs.codemod.com/platform/campaigns

**Source-access limitations:**
- GitHub Copilot app modernization docs: 404 on two guessed paths; abandoned per network rule. No product-level claims rest on it. Its existence as an assistant-embedded migration offering is treated as a market direction only (corroborated indirectly by the modernization-sibling research, which also could not reach those docs).
- Google BigQuery Migration Service (batch SQL translation) docs: timed out twice; abandoned. The SQL-dialect-conversion pole is evidenced instead through AWS SCT (schema/SQL/ETL-script conversion).
- All research came from Tier-1 official documentation; no external reviews were needed.

---

## Product A — OpenRewrite / Moderne

### Key observations (evidence layer A unless noted)

- **Definition (self-description):** "an open-source automated refactoring ecosystem for source code"; auto-refactoring engine running prepackaged recipes "for common framework migrations, security fixes, and stylistic consistency tasks."
- **Core objects:** *Recipes* (aggregated visitors) operating on *Lossless Semantic Trees* (LSTs) representing source code; modified trees are printed back to source "honoring the original formatting"; changes are "minimally invasive."
- **Delivery surfaces:** Maven/Gradle build plugins (one repo at a time), Moderne CLI (multi-repo, local), Moderne Platform (SaaS, fleet scale).
- **Workflow (quickstart):** add plugin → discover available recipes (`rewrite:discover`) → activate recipes in build config (including YAML-configured custom recipes) → run (`rewrite:run`) → review via `git diff` / IDE diff viewer → "confirm that everything still builds and passes its tests" (`mvn clean install`) → commit. Recipe composition: a Spring Boot 2/JUnit 4→5 migration recipe composes dependency-updating recipes (AddDependency/ChangeDependency/UpgradeDependencyVersion) and edits build files as well as source.
- **Catalog:** searchable recipe catalog; external recipe modules (rewrite-spring etc.); versioned recipe artifacts; a BOM for recipe versions.
- **Moderne Platform (fleet pole):** recipe marketplace ("over 7000 recipes"); select an *organization* of repositories → *Dry run* → results page listing affected repositories and code changes with a per-change "Why did this change?" explanation → *Commit selected results* with commit-strategy choice (direct commit, PR, branch name, commit message). Explicit statement: "Running a recipe *does not* automatically update the code"; the user decides what to commit. Large orgs (>100 repos) go to a slower queue (layer A, vendor-specific mechanics).
- **No AI required:** the engine is deterministic AST/semantic-tree manipulation; AI is not part of the engine's definition (Moderne now layers agent tools, but the core is rule-based).

## Product B — Amazon Q Developer (code transformation)

### Key observations (evidence layer A)

- **Scope:** AI assistant product; the transformation capability studied is **Java language upgrades** in the IDE (JetBrains modules, VS Code projects/workspaces): "updating deprecated code components and APIs as well as upgrading libraries, frameworks, and other dependencies."
- **Conversion contract:** explicit source→target version matrix (Java 8/11/17 → 17/21 etc.). Transforming to the same version is used for dependency-only upgrades.
- **Pre-check as gate:** "Amazon Q first builds your code in the source language version and verifies that it has the information necessary to perform the transformation." Prerequisites: Maven build success, correct source JDK locally, no private-network resources, UTF-8 only, build under a stated time limit — i.e., the tool requires the code to be buildable and self-contained before it will convert.
- **Job flow (IDE):** ask in chat → pick project → optional *dependency upgrade file* (YAML listing first/third-party dependencies and target versions; validated by the tool) → transformation runs with progress view (Transformation details / Transformation Hub) → **View diff** (source vs upgraded code) → **Accept** to apply patch in place → **Transformation summary** with suggested next steps.
- **Equivalence posture:** "Amazon Q Developer makes the minimal changes necessary to make your upgraded code compatible with the target JDK." Validation builds use the client-side environment ("initial and validation builds use the client-side environment"). A separate transformation pass upgrades dependencies after the minimum JDK upgrade.
- **Failure is first-class:** troubleshooting doc; many documented conditions make "the transformation will fail" — failure states are explicit product behavior, not edge trivia.

## Product C — AWS Schema Conversion Tool

### Key observations (evidence layer A)

- **Definition:** desktop tool "to convert your existing database schema from one database engine to another" (OLTP, data warehouse, NoSQL); also converts **ETL scripts** (Teradata BTEQ/FastLoad/MultiLoad, SSIS → AWS Glue/RSQL) and **SQL embedded in application code** (C++, C#, Java: "You can view, analyze, edit, and save the converted SQL code").
- **Conversion contract:** a published source→target support matrix (Db2/SQL Server/Oracle/MySQL/PostgreSQL/SAP ASE → Aurora-family engines; Teradata/Snowflake/BigQuery/… → Redshift; Cassandra → DynamoDB).
- **Project-based UI:** "AWS SCT provides a project-based user interface to automatically convert the database schema of your source database into a format compatible with your target."
- **Partial conversion is normal:** "If schema from your source database can't be converted automatically, AWS SCT provides guidance on how you can create equivalent schema in your target" — plus **extension packs**: installable emulation libraries (AWS Lambda functions and Python libraries) "to emulate the features that can't be converted."
- **Assessment machinery:** assessment reports; also DMS endpoint/task creation and data extract agents for the follow-on data move (the data move itself belongs to DMS, not SCT — boundary evidence).
- **Human-in-the-loop:** converted SQL is viewable/analyzable/editable/savable; the guidance-and-emulation model presumes human work on what automation cannot convert.

## Product D — Codemod

### Key observations (evidence layer A)

- **Definition (self-description):** "tools and infrastructure to automate repetitive or large-scale code maintenance projects end-to-end"; use cases: framework/library upgrades, compliance remediation, design-system migrations, i18n, post-M&A codebase sanitization, dependency management.
- **Positioning:** "pairs compiler-aware code graphs with AI to complement your coding agents" — explicitly hybrid: "Combine deterministic AST codemods with AI-powered fixups and shell scripts in a single workflow."
- **Core objects:** *codemods* (published, versioned transformation units in a **Registry** — public/private/pro); *workflows* (nodes → steps → tasks; DAG with dependencies; matrix strategies); *Campaigns* ("orchestrate large-scale code migrations"; execute a workflow, create tasks, open pull requests); *Insights* ("plan & track projects"); *Studio* ("generate and test codemods with AI assistance"); open-source CLI.
- **Campaign flow:** choose codemod from registry (version picker) → select target repositories (GitHub App / GitLab integration) → configure parameters (dynamic form from codemod schema; secrets referencing) → configure rollout (sharding by CODEOWNERS/directory with max files per shard; AI review step; CI recovery) → run → dashboard with DAG map view and task table → per-task branch → PR with CI check summaries → **auto-heal** (patch the generated PR, or repair the codemod package when failures look systematic; retry cap) → re-run failed tasks individually; task statuses (Todo / In Review / Done / Won't Do) with bidirectional Jira sync.
- **Scale pole:** orchestration across teams and repositories with resumable state, parallel matrix tasks, and leadership visibility.
- **Boundary-relevant:** Campaigns add project tracking, but the product starts from a chosen codemod + target repos; there is no estate inventory or per-application modernization decision machinery (rehost/replatform/refactor/rewrite route selection) in the documented core.

## Cross-product Comparison

| Dimension | OpenRewrite/Moderne | Amazon Q (Java upgrade) | AWS SCT | Codemod |
|---|---|---|---|---|
| Object of transformation | Java (+expanding) source & build files | Java project (Maven) | DB schemas, embedded/ETL SQL | Any code, via codemods (compiler-aware code graphs) |
| Conversion contract | recipe (named, versioned, configurable) | source→target version matrix + dependency upgrade file | source→target engine matrix (project-scoped) | codemod (versioned, parameterized) |
| Mechanism | deterministic LST visitors | AI model + local validation builds | deterministic rules + emulation libraries | deterministic AST codemods + AI fixups + scripts |
| Pre-conversion analysis | `rewrite:discover`; dry run (Moderne) | build-in-source-version verification | assessment reports | Insights; codemod testing in Studio |
| Preview before apply | run → `git diff` (repo); explicit Dry run (Moderne) | View diff before Accept | view/analyze/edit converted SQL | PR-based review |
| Validation | build + tests after run (documented step) | client-side validation builds | manual actions list + assessment | CI checks on PRs + auto-heal |
| Delivery | working-tree changes → commit (repo); commit-strategy modal incl. PR (Moderne) | apply patch in place after accept | saved converted schema/SQL project artifacts | per-task branch → PR per task |
| Unconvertible handling | minimal-invasive changes; recipes targeted at known patterns | separate dependency-upgrade pass; documented failure conditions | guidance for manual equivalent creation + extension packs | AI fixups + re-run + repair-republish |
| Scale | repo (plugin/CLI) → org of repos (platform) | one project/module per job | one migration project | repos × teams × shards (campaigns) |
| Surfaces | build plugin, CLI, SaaS platform | IDE chat/panels | desktop project app | SaaS console, CLI, registry, IDE-adjacent |

**Cross-product commonalities (evidence layer B):**

1. **Existing code in a source form → declared target form.** All four parameterize the conversion as an explicit source→target contract (version matrix, engine matrix, recipe, codemod).
2. **The system executes the transformation** — it produces changed code/build files/schema; it is not an advice-only tool. (All four.)
3. **Output is reviewable changed code before it becomes the codebase.** Diff-before-accept (Q), git diff (OpenRewrite), converted-SQL inspection (SCT), PR review (Codemod), dry-run-then-commit (Moderne). None of the four silently replaces the original.
4. **Equivalence to original behavior is the stated intent.** "Minimal changes" (Q), "honors original formatting"/"minimally invasive" (OpenRewrite), "equivalent schema" (SCT), compiler-aware transforms (Codemod).
5. **Pre-conversion verification/analysis as a gate or phase.** Build-first (Q), discover/dry-run (OpenRewrite/Moderne), assessment report (SCT), tested codemods (Codemod).
6. **Partial conversion with tracked follow-up.** Unconvertible items become guidance/manual actions/emulation (SCT), separate passes (Q), failed tasks to re-run (Codemod), targeted recipes (OpenRewrite).
7. **Delivery into the developer's version-control workflow** with human acceptance as the norm (all four).
8. **Conversion catalogs of prebuilt migrations** (recipe catalog, registry, engine matrices, version matrix).

## Canonical Model

### L0 — Defining Invariant

The smallest structure without which the product stops being recognizable as a code migration platform:

```text
Existing code in a source form  (the object of work)
└── Declared target form  (explicit source→target conversion contract)
    └── System-executed transformation  (produces changed code, not just advice)
        └── Equivalent-behavior output delivered as reviewable changes
            (human inspects → accepts before it becomes the codebase)
```

Four properties; remove any one and the product becomes a different Type:

1. **Existing code as the object.** Brownfield by definition: the input is code that already exists. Remove this (input = templates/specs) → code generator/scaffolding.
2. **Declared target form.** The conversion has an explicit contract (target language version, framework, engine/dialect, runtime). Remove this (open-ended code editing on request) → AI coding assistant.
3. **System-executed transformation.** The product itself performs the conversion and outputs changed code. Remove this (findings and recommendations only) → static code analysis / assessment tool.
4. **Equivalence-preserving output as reviewable changes.** The transformed code is intended to do what the original did, and it is delivered in a form a human can inspect, adjust, and accept. Remove the review-before-apply discipline and the product is definitionally untrustworthy; remove the equivalence intent → free-form code generation.

**Historical / market-sample check:** simple one-shot transpilers (web code converters, file converters), older schema-conversion wizards, deterministic rule engines, and AI/agentic platforms all satisfy these four properties — mechanism (deterministic vs AI), surface (desktop/IDE/CLI/SaaS), and scale (file→fleet) are all *outside* the definition. The word "platform" in the Type name is an umbrella: a build-plugin engine with no console (OpenRewrite OSS) is still fully in-type.

### L1 — Common Mature Structure

Very common in mature products, not definitional:

- **Pre-conversion analysis/verification** of the codebase (buildability checks, upgrade-target discovery, assessment reports, dry runs).
- **A catalog of prebuilt conversions** (recipes/codemods/matrices) with versions and search.
- **Authorable/custom conversion definitions** (YAML recipes, dependency upgrade files, AI-assisted codemod authoring, emulation extension packs).
- **Validation machinery** (builds/tests after conversion, CI checks on generated PRs, compile validation).
- **Preview/diff surfaces** ("View diff", dry run, converted-SQL inspection, "why did this change" explanations).
- **Reporting** (transformation summaries, lists of changed files, unresolved items, suggested next steps).
- **Iterative repair loop** (re-run failed tasks, fix build errors, auto-heal, repair-and-republish the converter itself).
- **Delivery machinery into version control** (apply patch, commit strategies, per-task branches → PRs).
- **Scale orchestration across repos/teams** (organizations of repositories, campaigns, sharding, dashboards, project-management sync).

### L2 — Variant / Optional Structure

Depends on segment, mechanism, scale, deployment:

- **Target domain:** same-language version upgrades; framework/library upgrades; cross-language translation; database schema/SQL dialect conversion; runtime/platform moves; adjacent remediation uses (stylistic consistency, security fixes, i18n, compliance patterns).
- **Mechanism:** deterministic rules over syntax/semantic trees vs AI/LLM conversion vs hybrid (deterministic transforms + AI fixups).
- **Delivery surface:** build-tool plugin, CLI, IDE-embedded flow, desktop project app, SaaS console, registry/marketplace.
- **Scope of a run:** one file/project/repo vs an organization of repos vs sharded multi-team campaigns.
- **Commercial shape:** OSS engine + commercial platform split; managed service; free desktop tool; pro/enterprise SaaS tiers.
- **Coupling to the target platform's own cloud** (e.g., conversion tools that target a specific vendor's managed services) vs neutral conversion.

### L3 — Vendor-specific Structure (research notes only)

- OpenRewrite: Lossless Semantic Trees, visitors, Maven/Gradle goals (`rewrite:run`, `rewriteDiscover`), rewrite.yml recipe format, recipe BOM, Code Genome Project artifact repository.
- Moderne: recipe marketplace (7000+ recipes figure), organizations of repos, "Why did this change?", fast/slow run lanes, DevCenter, data tables, commit-strategy modal.
- Amazon Q: dependency upgrade YAML schema fields (identifier/targetVersion/versionProperty/originType), supported Java upgrade table (8/11/17→17/21), Transformation details/Hub tabs, 55-minute build prerequisite, UTF-8-only caveat, private-network failure conditions, Bedrock foundation.
- AWS SCT: exact source→target engine matrix, extension pack wizard (Lambda/Python emulation), DMS endpoint/task creation, data extract agents, Redshift optimization recommendations.
- Codemod: JSSG transforms, workflow node/step/task DAG, matrix strategy, sharding by CODEOWNERS, auto-heal retry cap, repair-and-republish of source-available codemod packages, Jira status mapping (Todo→To Do etc.), Codemod Wish, MCP server, Pro/Enterprise tiers.

## Vendor-specific Findings

All L3 items above. Notable product-posture findings worth keeping as examples:

- OpenRewrite/Moderne is the clearest **engine/platform split**: a free deterministic engine for one repo, a commercial platform for fleets — evidence that scale orchestration is separable from the conversion act.
- Amazon Q documents **failure as designed behavior** (extensive "the transformation will fail" conditions) — evidence that pre-conditions and failure states are first-class, not exceptional.
- AWS SCT documents **the emulation pattern** for unconvertible features — evidence that partial conversion + generated support code is a mature pattern.
- Codemod documents **converter repair** (repair and republish the codemod package when CI failures look systematic) — evidence that the converter itself is a maintained, versioned asset, not a one-shot script.

## Rejected Findings

- ❌ "A code migration platform is an AI product." Rejected: OpenRewrite and AWS SCT are deterministic/non-AI and unambiguously in-type. Mechanism is a variant, not a property.
- ❌ "It must have estate assessment, waves, and program tracking." Rejected: that is the Application Modernization Platform's program wrapper. Repo-level conversion tools are fully in-type without any of it.
- ❌ "Migration = moving code between repos/hosting/services." Rejected: that is source-control/hosting/infrastructure territory. The Type's "migration" is *form-to-form conversion of code*.
- ❌ "Conversion must be complete/lossless." Rejected: all sampled products document partial conversion, manual fallback, or separate passes as normal operation.
- ❌ "It is defined by a dashboard/console." Rejected: OpenRewrite OSS has no console and is fully in-type; "platform" in the leaf name is an umbrella, not a requirement.
- ❌ "It must target cloud platforms." Rejected: SCT converts engine-to-engine; OpenRewrite upgrades frameworks in place; target substrate is a variant.

## Boundary Findings

### vs Application Modernization Platform (joint review with the processed sibling)

The sibling's research defined the boundary as **program wrapper vs conversion act** and flagged this leaf for joint review. This research confirms the same test from the migration side:

- The modernization platform **starts from the estate**: inventory → assessment → a per-application modernization decision (rehost/replatform/refactor/convert/rewrite) → tracked multi-application program.
- The code migration platform **starts from the conversion**: a source form, a target form, and the transformation between them — whether for one repo or a thousand. It does not require, and typically lacks, estate-level portfolio assessment and route-decision machinery.
- Convergence is real and documented on both sides: modernization platforms now embed agentic conversion (sibling research), and migration platforms add project tracking across repos (Codemod Campaigns). The working discriminator remains **what the product starts from and owns**: the portfolio decision (modernization) vs the conversion act (migration). A product with conversion but no estate-level assessment/portfolio decision belongs here; a product managing a portfolio program of which conversion is one phase belongs to the sibling.
- **去掉什么就变成另一个 Type:** take away the conversion act (assess + plan + track only) → modernization/portfolio tool. Take away the estate program (convert only) → this Type.

### vs AI Coding Assistant / AI Coding Agent

- Assistants are general-purpose, conversational, task-scale; there is no conversion contract and no equivalence-to-original expectation as the organizing object. A migration platform's organizing object is the migration itself (recipe/job/campaign with source→target contract, validation, delivery).
- Assistant-embedded migration features (e.g., upgrades triggered from an assistant) blur the surface but not the structure; evidence for those specific features was not directly reachable in this research (see Uncertainties).
- **去掉什么就变成另一个 Type:** remove the fixed source→target contract and equivalence expectation (edit anything on request) → AI coding assistant.

### vs Static Code Analysis / Code Quality Platform

- Analysis produces findings; migration produces changed code. Convergence exists: analysis is the front half of migration (SCT assessment reports; Moderne dry run; OpenRewrite `discover`), and OpenRewrite ships static-analysis recipes — a tool can serve both. The Type's defining output remains the transformation.
- **判据:** remove the transformation (recommend only) → static analysis.

### vs Project Scaffolding / Code Generator

- Generators create new code from templates/specifications; no existing code as input, no equivalence intent. Migration platforms presuppose existing code.
- **判据:** remove the existing-code input → generator/scaffolding.

### vs Source Code Hosting / Code Review

- Hosting/review systems store, diff, and gate code; they do not transform it. Migration platforms deliver their changes *into* these systems (branches, PRs, checks).
- **判据:** the system that produces the diff is the migration platform; the one that stores and gates it is hosting/review.

### vs ETL / Data Migration Platform

- Data migration moves data; code migration transforms code. AWS SCT sits at the seam: it converts schema (DDL — code) and ETL *scripts* (code), while the actual data movement belongs to DMS — confirming that converted *code-like artifacts* are in-type and data movement is not.
- **判据:** if the transformed object is data rows/files, it is data migration; if it is code/schema/scripts, it is here.

### vs Build Automation System

- Build tools compile/package code without changing its form; migration tools change the code itself. OpenRewrite runs *inside* the build (plugin) — the boundary is what changes: build inputs unchanged vs source code changed.

## Uncertainties

- **Assistant-embedded migration offerings:** GitHub Copilot app modernization docs were unreachable (404 ×2). Its existence as a product direction is corroborated only indirectly (modernization-sibling research hit the same wall). No claims about specific assistant-embedded migration features are made in the final document.
- **Google SQL translation service:** BigQuery migration docs timed out; SQL-dialect conversion is evidenced through AWS SCT instead. Google's translation service was not directly documented.
- **Cross-language translation depth:** the sample documents same-language version upgrades (Amazon Q), framework upgrades (OpenRewrite, Codemod), and schema/SQL conversion (SCT). Full cross-language translation (e.g., procedural legacy → modern language) is known in the market but was not directly documented in the sampled docs; the final document treats it as a variant without precise claims.
- **Naming:** no sampled product self-identifies primarily as a "code migration platform" (self-descriptions: automated refactoring ecosystem; code transformation; schema conversion; codemod platform). The directory leaf is treated as an umbrella name for the conversion-act category. Recorded as a naming observation, not a taxonomy conflict.

## Final Synthesis

A **Code Migration Platform** is software that transforms existing code from a declared source form into a declared target form — language version, framework/library, database dialect/schema, or runtime — and delivers the result as reviewable, equivalent-behavior changes into the developer's normal version-control workflow.

The defining core is exactly: **existing code in → explicit target form → system-executed transformation → equivalence-preserving, human-reviewable changed code out.** Everything else commonly associated with the category — AI mechanisms, catalogs of prebuilt migrations, dashboards, campaigns across hundreds of repositories, dry-run previews, auto-healing CI recovery, project-management sync — is mature market structure layered on that core, not part of it. The mechanism may be deterministic rules, AI models, or a hybrid; the surface may be a build plugin, CLI, IDE panel, desktop tool, or SaaS console; the scale may be one file or a sharded fleet — none of these change what the product *is*.

The Type sits between the program wrapper (Application Modernization Platform) and the analysis/generation/hosting neighbors, and the joint boundary review with the sibling confirms the working discriminator: **estate decision vs conversion act.** The conversion act, at whatever scale and by whatever mechanism, is this Type.
