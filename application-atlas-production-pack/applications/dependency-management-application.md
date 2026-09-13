# Dependency Management Application

## Overview

A **Dependency Management Application** is the project-side application that holds a software project's dependency set as managed state — the external components the project depends on, the exact versions selected for use — and operates the loop that keeps that set coherent and current as both the project and its ecosystem change.

The problem it exists to solve is version drift. A non-trivial software project depends on external libraries, which depend transitively on further libraries. Available versions change constantly: new releases appear, old ones are withdrawn, and incompatible requirements collide. Left to manual choice, two machines setting up the same project at different times can end up running different dependency versions — the classic "dependency hell". This Type of application answers three questions permanently and repeatably: *what does this project depend on, which exact versions is it using, and how do those choices change safely over time?*

The defining structure is small:

```text
Dependency Declaration (project-resident record: component + version constraint)
└── Resolution (compute one concrete, coherent selection, including transitive dependencies)
    └── Recorded Selection (the chosen versions held as durable project state)
        └── the managed change loop (deliberate change → re-resolve → records move forward)
```

Everything else commonly associated with the category — installing packages, update-automation robots, security alerting, monorepo support — is standard or optional capability layered on this core, not what makes the product one of this Type.

The market realizes the core in two lineages that this document covers together: the **per-ecosystem dependency manager** (a command-line tool working directly in the project: manifest, lockfile, install, update) and the **automated dependency-update application** (a service that watches the project's manifests and proposes recorded-selection changes as reviewable pull requests). The boundary sentence: this is not the tool that *builds* the project (Build Automation), not the server that *hosts* packages (Package Registry / Artifact Repository), and not the scanner that *analyzes* the dependency set for vulnerabilities and licenses (Software Composition Analysis) — it is the application that *decides and records which versions are used*.

## Users & Context

The primary user is a software developer working inside a project repository. Two recurring situations bring them to the application:

- **Project setup and onboarding** — reproduce the project's dependency environment exactly; across the sample, a single install command is the documented entry point.
- **Dependency maintenance** — adding a capability (add a library), keeping current (refresh versions to the newest allowed), and responding to breakage (a dependency released something incompatible; a component was deprecated or withdrawn).

A second, increasingly dominant user is **automation acting on the team's behalf**: update applications run on a schedule, scan manifests, and open pull requests; humans review and merge. In this lineage the developer's role shifts from issuing commands to reviewing proposed dependency changes.

Downstream consumers matter to the context though they are not operators: CI pipelines and production deploys run on the recorded selection, which is why the selection is held as committed, reviewable project state rather than a local side effect.

## Core Model

### The Defining Core

Three structures, held jointly. Remove any one and the product stops being recognizable as dependency management:

- **The dependency declaration of record** — a persistent, project-resident record of the components the project depends on. Each entry identifies a component by name and qualifies it with a *version constraint* — a rule (range, compatible-release bound, exact pin) rather than a single version. The declaration is written and edited by people; it expresses intent, not outcome. Without it there is nothing to manage.
- **Resolution** — the application computes the *concrete* set of component versions that will actually be used: every declared component plus every transitive dependency those components themselves require, at exactly one version each, such that **all requirements hold at the same time**. This is a search over combinations, not a per-component lookup: choosing a version for one component narrows the choices for its dependents, competing requirements on the same component must be reconciled, and the search can legitimately fail — with an explanation of the conflicting requirement chains. Resolution consults the configured supply sources for the set of available versions. Without it, the product is a list editor, not management.
- **The recorded selection** — the concrete chosen versions are held as durable project state that later operations *reuse instead of re-deciding*. In the modern form this is a lockfile-class record: machine-maintained, committed to version control, listing every component (direct and transitive) at its exact chosen version, often with source and integrity information. Its purpose is reproducibility: every machine, teammate, deploy, and CI run gets the same versions. Without it, resolution is ephemeral and the drift problem returns.

Around the three structures runs the **managed change loop**: the dependency set changes through deliberate, application-mediated operations — editing the declaration (add, remove, re-constrain) or refreshing the selection (update to the newest allowed versions) — and every change re-runs resolution and moves both records forward coherently. The loop is what makes the recorded selection a living state rather than a frozen snapshot, and in the update-application lineage it is essentially the whole product.

### Standard Capabilities

Mature products across both lineages commonly provide:

- **Materialization** — fetching the selected components and placing them into the project's environment so the project can run (install/sync commands; managed environments). Standard in the manager lineage; absent in the update-application lineage, which hands execution to CI.
- **Update operations with conservative semantics** — update commands that target one component or everything, deliberately *not* re-resolving untouched parts of the set (an unmodified component and its dependents are treated as a stable unit unless the change forces otherwise).
- **Transitive-dependency visibility** — tree/graph views of the resolved selection, including "why is this component included" inversion queries and duplicate-version detection.
- **Version-constraint semantics** — a grammar of constraints (compatible-release operators, ranges, exact pins, wildcards) with defined compatibility rules that determine what an update may pick; prerelease versions typically opt-in only.
- **Dependency classification** — direct vs transitive; runtime vs development/test/build; groups or kinds with install-time selection; platform-specific variants.
- **Conflict machinery** — resolution failure as a designed, explained outcome rather than a crash.
- **Record hygiene** — commit guidance (commit it for applications, omit it for libraries), merge-conflict handling (never hand-resolve; regenerate), integrity checksums, toolchain pinning, platform normalization.
- **Configured supply sources** — a default public registry plus configurable alternatives: private registries with credentials, version-control repositories, local paths, mirrors.
- **Configuration layering and presets** — tool configuration files, shareable policy presets, per-project override of defaults.
- **Multi-project coordination** — workspaces/monorepos: one coherent resolution across many packages in one repository; automatic discovery of package files.

### One Structure, Many Implementations

The core is written conceptually; products realize each structure differently, and a reader who has only met one realization should still recognize the others:

```text
Concept:            Dependency Declaration
Implementations:    Gemfile-class, Cargo.toml-class, pyproject.toml-class,
                    package.json-class manifests; Dockerfile and workflow
                    files treated as dependency-bearing by update tools

Concept:            Resolution
Implementations:    embedded solver engines (version-solving algorithms with
                    backtracking and conflict explanation); update-selection
                    engines that pick the next valid version per policy and
                    delegate full re-resolution to ecosystem tooling

Concept:            Recorded Selection
Implementations:    lockfile committed to the repository (modern canonical form);
                    deterministic re-resolution over a persistent local cache
                    (older build-embedded form)

Concept:            Managed Change Loop
Implementations:    developer-issued commands (install / update / add / remove);
                    scheduled automation proposing changes as pull requests
                    with review, approval, and merge policies
```

## How It Works

### The core loop (manager lineage)

```text
Declare
→ author the manifest: component name + version constraint
→ (or issue an add command; the tool picks a suitable constraint and records it)

Resolve
→ the tool consults the configured sources for available versions
→ searches for one version of every component — direct and transitive —
  that satisfies all requirements simultaneously
→ on conflict: fail with the requirement chains that clash

Record
→ write the chosen versions into the lockfile-class record
→ commit both files; from now on, installs reuse the recorded selection exactly

Materialize
→ fetch the selected components into the project environment
→ (optionally isolate the environment from the rest of the machine)

Change
→ edit the declaration (add/remove/re-constrain) → conservative re-resolution,
  untouched selections preserved
→ or refresh the selection (update command) → newest allowed versions,
  lockfile rewritten
```

Two distinct change operations are worth separating, because they answer different questions: *declaration-driven change* ("I want this project to use a different component or constraint") and *selection-driven change* ("keep the constraints, move to the newest versions they allow"). A full from-scratch re-resolution is the blunt instrument of the second kind — possible, but documented in mature products as something to do deliberately, with version control and a test suite as the safety net.

### The update-application realization

```text
Configure
→ commit a policy file: which ecosystems, which manifest locations,
  how often to check, what to allow/ignore, how to version-bump

Scan (scheduled)
→ locate the project's package files
→ extract every dependency with its current constraint and recorded version

Look up
→ query the supply sources for newer versions
→ apply versioning rules to find the next valid update per dependency

Propose
→ create a branch, apply the update to manifest and lockfile, open a
  pull request — the recorded-selection diff is the review surface
→ grouping rules may consolidate many updates into one proposal;
  approval policies may gate which proposals are created at all

Review & merge
→ humans (or automerge policies) accept; CI validates the proposed selection
→ security-driven updates typically bypass scheduling and approval entirely
```

The update-application lineage performs the same three core structures — it reads the declaration, performs update-selection against the sources, and rewrites the recorded selection — but it never materializes or builds; the proposed change is its output, and the project's normal review workflow is its control surface.

### What resolution actually does

Resolution is the intellectual center of the Type, and its documented behavior is consistent across the sample:

- It is a **search**: candidate versions are explored, dead ends are learned from, and the search backtracks rather than giving up at the first conflict.
- It **unifies**: where several components require the same library, one shared version is preferred (for build efficiency and type compatibility); only genuinely incompatible requirements result in multiple versions of one component coexisting — itself a documented hazard.
- It **prefers the newest allowed version** within the constraints — never simply the newest in existence.
- It **defers to the record**: an existing recorded selection is reused as-is until the declaration changes or an explicit update is requested; this "balance reproducibility with adjusting to changes" is the documented design intent.
- It **explains failure**: when no selection exists, the error traces the chains of requirements that contradict each other — which component demanded what, and why no version satisfies all.

## Interfaces

The Type's surfaces are unusual: files are primary interfaces, not just storage.

### Declaration file (manifest)

The project's statement of intent, authored by people.

- Typical content: component names, version constraints, source overrides, dependency groups/kinds, environment requirements
- Primary actions: add, remove, re-constrain entries; declare sources and groups

### Recorded-selection file (lockfile)

The machine-maintained outcome of resolution.

- Typical content: every component (direct + transitive) at its exact chosen version; source and revision for non-registry sources; integrity checksums; the tool version that wrote it; covered platforms
- Primary actions: none by hand — it is generated and updated by the application; humans review its diffs

### Tool configuration

Per-project and per-user settings for the application's own behavior.

- Typical content: supply sources and credentials, resolution/update policies, environment locations, group install defaults
- In the update lineage: the policy file that defines ecosystems, manifest locations, schedules, allow/ignore rules, grouping, and automerge/approval behavior

### Command-line interface (manager lineage)

- Commands for the loop: install (materialize from the record), add/remove (declaration change), update (selection refresh, per-component or full), plus inspection: dependency tree, outdated listings, why-included queries
- Output: resolution progress, conflict explanations with requirement chains, lockfile change summaries

### Platform surfaces (update-application lineage)

- Pull requests / merge requests as the primary change proposals, steered via comment commands or dashboard checkboxes depending on the product
- A dashboard view (commonly a repository issue or tab) summarizing pending, deferred, rejected, and deprecated-dependency states, doubling as an approval queue
- Status views showing which ecosystems are monitored and when each was last checked

### Inspection reports

Tree/graph renderings of the resolved selection — including inverted views ("what depends on this") and duplicate detection — are the standard way users understand and debug the selection.

## Important Rules / Behaviors

- **The record is machine-maintained.** Across the sample, hand-editing the lockfile-class record is explicitly an anti-pattern: the application owns it; people review its diffs. Merge conflicts in it are resolved by regenerating, never by hand-editing conflict markers.
- **Lock-first reuse.** Once a selection is recorded, subsequent operations reuse it exactly. Re-resolution happens on declaration edits (scoped conservatively to what the edit forces) or on explicit update operations — not on every run.
- **Conservative change semantics.** Updating one component does not silently update the components others still depend on; untouched parts of the set are preserved as stable units. This is a documented design rule, not an accident, and it is what makes dependency changes reviewable in small, attributable steps.
- **Conflicts are first-class outcomes.** A set of requirements with no satisfying selection is a normal, explained result — the application reports the conflicting chains rather than picking arbitrarily.
- **Constraint semantics govern updates.** What an update may pick is defined by the constraint grammar and compatibility rules (e.g., compatible-release bounds), plus any release-age policies (cooldowns, minimum release age) the product or project configures. Withdrawn releases are typically excluded from new selections but remain valid if already recorded.
- **Application vs library posture.** The recorded selection is committed for applications (reproducibility for every consumer of the repository) but omitted for published libraries: consumers resolve from the library's declared constraints and ignore any lockfile it ships. Products document this split explicitly.
- **Supply sources are configured and trusted.** Resolution and updates only see the configured sources; restricting them (e.g., to private registries) is a supported posture, and source configuration is security-sensitive because it determines where components come from.
- **Dependency changes are reviewable events.** Whether via a lockfile diff in a normal commit or a dedicated update pull request, the Type makes every selection change explicit, attributable, and reversible through version control.

## Variants

- **Per-ecosystem dependency manager** — the classic form: a single-ecosystem CLI (manifest + lockfile + install + update) bundled with or central to a language community.
- **Build-embedded resolution** — the resolution engine lives inside the build tool; the dependency-management function (declaration, transitive resolution, version mediation, update) is exercised through build configuration. Older realizations hold the selection via deterministic re-resolution over a persistent cache rather than a committed lockfile — a weaker but recognizable form of the same core.
- **Automated dependency-update application** — cross-ecosystem by design; operates through the code-hosting platform's review workflow; offered as hosted apps, platform-native features, or self-hostable open source.
- **Platform-native embedding** — the update function built directly into a code-hosting platform, configured by a repository file, with its status surfaced inside the platform's dependency views.
- **Adjacent domain (not this Type): system package management** — operating-system package managers also resolve dependencies, but their unit is the machine-wide package store, not a project's dependency set of record; they have no project-resident declaration or recorded selection.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Build Automation System | sibling, deepest overlap | The build tool answers *how the project builds* (build definition, dependency-ordered execution, artifact production); dependency management answers *what it depends on and which versions*. Existence proof of separation in both directions: update applications manage dependencies without building anything; some build tools build without resolving dependencies. Ecosystem-native tools (cargo/npm-class) fuse both functions in one tool — the straddle case. |
| Package Registry | sibling, supply side | The registry is the server-side venue where packages are published and served per ecosystem protocol; the dependency manager is the project-side client that selects versions from it. Remove the project-side declaration/resolution and the registry remains a registry. |
| Artifact Repository | sibling, custody side | Custodies and serves build artifacts (with proxy/upstream machinery that *satisfies* dependency declarations); it does not decide or record which versions a project uses. |
| Software Composition Analysis / SCA | adjacent, analysis lens | SCA analyzes the dependency composition for known vulnerabilities and license risk; dependency management selects and maintains the composition. Security-triggered updates are an integration point, but remove the security analysis and dependency management stands; remove selection/reconciliation and only the scanner remains. |
| SBOM Management | adjacent, compliance lens | An SBOM is a compliance-oriented inventory record derived from dependency states; the recorded selection is working project state consumed by builds. Different primary consumers and lifecycles. |
| Source Code Hosting Platform | venue | Hosts the repositories where manifests and lockfiles live and provides the review workflow through which update proposals flow; the scan/select/propose function remains dependency management even when embedded in the platform. |
| Continuous Integration Platform | consumer | CI runs on the recorded selection and validates proposed changes; it neither declares nor resolves the dependency set. |
| Patch Management | different domain | Patches installed software on machines and endpoints; different unit (device vs project), different actor (IT operations vs developers). |

## Representative Products

- **Renovate** (Mend) — standalone, cross-ecosystem automated dependency updates; hosted app or self-hosted open source; config presets, scheduling, grouping, automerge, dependency dashboard.
- **Dependabot** (GitHub) — platform-native automated version and security updates configured per repository; part of GitHub's supply-chain-security feature family alongside alerts and the dependency graph.
- **Bundler** (Ruby) — the canonical manifest+lockfile dependency manager; Gemfile / Gemfile.lock, conservative updates, PubGrub-based resolution with explained conflicts.
- **Cargo** (Rust) — ecosystem-native tool fusing dependency management with build and publish; Cargo.toml / Cargo.lock, backtracking resolver with version unification; the documented straddle case.
- **Poetry** (Python) — dependency management and packaging in one tool; pyproject.toml / poetry.lock, dependency groups, environment isolation, dependency synchronization.

The two lineages are both represented deliberately: Renovate and Dependabot embody the update-application form (standalone vs platform-native); Bundler, Cargo, and Poetry embody the manager form across three ecosystems with different philosophies (minimal lockfile-first; fused with build; packaging-inclusive with environment management).

## Sources

Research date: **2026-09-07**

Primary official documentation (Tier 1):

- Renovate — https://docs.renovatebot.com/ ; https://docs.renovatebot.com/key-concepts/how-renovate-works/ ; https://docs.renovatebot.com/key-concepts/dashboard/
- Dependabot — https://docs.github.com/en/code-security/dependabot ; https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security ; https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/controlling-dependencies-updated ; https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/configure-version-updates
- Bundler — https://bundler.io/ ; https://guides.rubygems.org/gemfile/ ; https://guides.rubygems.org/dependency-resolution/ ; https://guides.rubygems.org/gemfile-lock/ ; https://guides.rubygems.org/updating_gems/
- Cargo — https://doc.rust-lang.org/cargo/ ; https://doc.rust-lang.org/cargo/guide/why-cargo-exists.html ; https://doc.rust-lang.org/cargo/guide/cargo-toml-vs-cargo-lock.html ; https://doc.rust-lang.org/cargo/reference/resolver.html
- Poetry — https://python-poetry.org/docs/ ; https://python-poetry.org/docs/basic-usage/ ; https://python-poetry.org/docs/managing-dependencies/

> Sourcing limitations: large reference pages (full configuration-option references, complete command references) were not fetched; configuration observations come from the concept and how-to pages above, so exact numeric defaults and full option lists are intentionally not stated. Build-embedded realizations (Maven/Gradle-class) and historical lineage (early ecosystem installers, system package managers) were reasoned from the paired build-automation research and structural analysis rather than freshly fetched; claims about them are correspondingly qualified. Detailed product-by-product evidence, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
