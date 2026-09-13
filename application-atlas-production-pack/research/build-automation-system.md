# Research Notes — Build Automation System

Research date: 2026-09-06
Evidence layers: **A** = directly observed in an official source for a specific product; **B** = cross-product commonality across the researched sample; **C** = canonical inference from comparison and boundary reasoning.

## Research Goal

Understand what a Build Automation System is as an Application Type: the core objects of its world model, who uses it, how a build actually flows from definition to artifact, which rules govern its behavior, and where it separates from neighboring developer-tooling Types (Continuous Integration Platform, Artifact/Package Registry, Dependency Management Application, IDE, task runners).

## Initial Boundary (pre-research hypothesis)

- Hypothesis: the Type is the "build engine" family — Make, Maven, Gradle, Bazel, MSBuild, CMake-class tools. A project-resident build definition + an engine that evaluates and executes it + artifact production.
- Nearest neighbors to separate from: CI Platform (when/where builds run, shared infrastructure, orchestration and history), Artifact Repository / Package Registry (custody of outputs), Dependency Management Application (version selection), IDE (consumes/invoke builds), task runners (arbitrary command chaining without build-artifact semantics).
- Known risk: ecosystem-native tools (cargo, npm/yarn/pnpm-class, MSBuild) fuse build + dependency resolution + publishing, so sampled general-purpose tools may over-shape the definition. Also risk of over-fitting to the modern daemon/cache era (Gradle/Bazel) versus 1970s–2000s tools (Make, CMake).

## Research Questions

1. What are the core objects? (build definition, unit of work, dependency graph, inputs/outputs, artifacts, toolchain)
2. What does the engine actually do at invocation time? (load → evaluate/analyze → execute)
3. How does incremental evaluation work, and is it definitional or common?
4. How are dependencies and toolchains handled? Are they part of the defining core?
5. How do multi-module / multi-variant builds work?
6. What interfaces exist (CLI, files, GUI, IDE, query surfaces, daemon)?
7. What rules matter (up-to-date correctness, output placement, failure semantics, reproducibility)?
8. How does the Type relate to CI, artifact repositories, and dependency management?
9. Historical check: does a 1977-era tool (Make) and a generator-era tool (CMake) fit the same model as modern daemon/cache tools?

## Representative Products

Selected for market representativeness, documentation quality, distinct product philosophies, and distinct eras:

| Product | Philosophy / era | Why sampled |
|---|---|---|
| GNU Make | target-based dependency tool; 1970s origin, POSIX-standardized | historical anchor; the minimal form of the Type |
| Apache Maven | convention-over-configuration; fixed lifecycle; POM model | the declarative-model pole; dominant Java-era convention |
| Gradle | incremental task graph + daemon + caches + plugin ecosystem | modern JVM/Android standard; incremental-evaluation pole |
| Bazel | hermetic, action-graph, remote cache/execution; monorepo scale | correctness-at-scale pole |
| CMake | meta-build generator; produces native buildsystems | variant anchor; separates "definition" from "execution engine" |

## Sources

All fetched 2026-09-06. No fetch failures in this pass.

- GNU Make manual — Overview: https://www.gnu.org/software/make/manual/html_node/Overview.html
- GNU Make manual — Rule Introduction: https://www.gnu.org/software/make/manual/html_node/Rule-Introduction.html
- Apache Maven — What is Maven: https://maven.apache.org/what-is-maven.html
- Apache Maven — Introduction to the POM: https://maven.apache.org/guides/introduction/introduction-to-the-pom.html
- Apache Maven — Introduction to the Build Lifecycle: https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html
- Gradle User Manual (9.7.1) — table of contents: https://docs.gradle.org/current/userguide/userguide.html
- Gradle User Manual — Incremental build: https://docs.gradle.org/current/userguide/incremental_build.html
- Bazel — Intro to Bazel: https://bazel.build/about/intro
- Bazel — Repositories, workspaces, packages, and targets: https://bazel.build/concepts/build-ref
- Bazel — Hermeticity: https://bazel.build/basics/hermeticity
- CMake — Overview: https://cmake.org/overview/
- CMake 4.4.3 — User Interaction Guide: https://cmake.org/cmake/help/latest/guide/user-interaction/index.html

## Product Observations

### GNU Make (evidence A)

- Positioning: "The `make` utility automatically determines which pieces of a large program need to be recompiled, and issues commands to recompile them."
- General purpose: usable for "any task where some files must be updated automatically from others whenever the others change" — not limited to a language.
- Standardized: conforms to POSIX.2 (IEEE Std 1003.2-1992).
- Build definition = makefile, resident in the project, made of **rules**: `target … : prerequisites …` + recipe (commands). "A *rule* … explains how and when to remake certain files."
- Target is usually a file generated by a program (executable, object file); can also be an action to carry out (e.g. `clean`) — phony targets with no prerequisites.
- Prerequisite = input file used to create the target; recipe runs to create/update the target "if any of the prerequisites change."
- Recipe lines are executed by the shell (tab-prefixed).
- No dependency acquisition, no repository concept, no toolchain management — the environment's tools are invoked directly by recipes.

### Apache Maven (evidence A)

- Positioning: a uniform build system for Java-based projects: "Once you familiarize yourself with one Maven project, you know how all Maven projects build."
- Build definition = **POM** ("Project Object Model"), "the fundamental unit of work", an XML file with project info and build configuration; ships defaults (build directory `target`, source directory `src/main/java`, test source directory `src/test/java`).
- Project coordinates: groupId:artifactId:version; packaging type (default `jar`) determines the artifact form.
- Defaults inherited from a **Super POM** (including repository configuration pointing to Maven Central) — inheritance is a first-class mechanism (parent POMs), alongside **aggregation** (multi-module: parent declares `<modules>`, packaging `pom`; commands run against all modules).
- **Build lifecycle** is "the central concept": three built-in lifecycles (`default`, `clean`, `site`); the default lifecycle is an ordered phase list — validate, compile, test, package, verify, install, deploy (plus intermediate phases); invoking a phase runs all preceding phases.
- Phases are implemented by **plugin goals**: packagings bind standard goals (compiler:compile, surefire:test, jar:jar, install:install, deploy:deploy); custom plugins/goals can be bound to phases; goals can also be invoked directly.
- Dependency management: project declares dependencies; artifacts are downloaded from (central) repositories; a central-repository mechanism "your project's clients can use to download any JARs required for building your project."
- Model-based: "build any number of projects into predefined output types such as a JAR, WAR, or distribution based on metadata about the project, without the need to do any scripting in most cases."
- Also does: site/documentation generation, release management, report generation (quality project information).
- Notably: no fine-grained per-task up-to-date skipping is presented in the lifecycle model — phases/goals run in sequence (Gradle's manual explicitly contrasts modern incremental behavior; Maven's own docs do not claim task-level incrementality). Evidence of a build automation system that does NOT center incremental evaluation.

### Gradle (evidence A)

- User manual structure documents the object world: settings file, build file, tasks, dependencies, plugins, multi-project builds, composite builds, build lifecycle, build cache, configuration cache, daemon, wrapper, tooling API, toolchains, IDE integration.
- **Incremental build**: "An important part of any build tool is the ability to avoid doing work that has already been done." A **task** takes inputs and produces outputs; Gradle "tests whether any of the task inputs or outputs has changed since the last build. If they haven't, Gradle can consider the task up to date and therefore skip executing its actions." Console marker `UP-TO-DATE`.
- Declared inputs/outputs via annotations (`@Input`, `@InputFiles`, `@OutputDirectory`, `@Classpath`, `@CompileClasspath`, `@Destroys`, `@LocalState`, `@Nested`, …); benefits enumerated: **inferred task dependencies** (one task's output wired to another's input), input/output validation, **continuous build** (re-run on change), **task parallelism** (from declared I/O), caching.
- Correctness rules: non-deterministic tasks should not be configured for incremental build; tasks failing input/output validation are "executed without any optimizations" (never up-to-date, never cacheable, never parallel, never incremental); **stale task outputs** are removed.
- **Build cache** (local + remote) and **configuration cache** are first-class documented subsystems; **file system watching** backs the daemon; **daemon** and **wrapper** (project-pinned tool launcher) are core reference sections.
- Dependency machinery is extensive: configurations, repositories, version catalogs, constraints/conflict resolution, locking, variant-aware resolution — the build tool embeds a dependency-resolution engine (JVM ecosystem posture).
- Multi-project structuring (settings file; sharing build logic between subprojects; composite builds) and plugin authoring (convention plugins, binary plugins) are core chapters.
- **Gradle on CI** documentation: dedicated integration chapters for GitHub Actions, GitLab CI, Jenkins, TeamCity, Travis CI — the build tool is documented as the invoked tool inside CI systems, not as CI itself.

### Bazel (evidence A)

- Positioning: "an open-source build and test tool similar to Make, Maven, and Gradle" — self-places in this Type.
- High-level build language: describes "the build properties of your project at a high semantical level"; operates on "the *concepts* of libraries, binaries, scripts, and data sets", shielding users from individual compiler/linker invocations.
- Object hierarchy: **repositories** (directory trees with a boundary marker file) → **workspace** (main repo + external repos) → **packages** (a directory with a `BUILD` file + its files; no file belongs to two packages) → **targets** (two kinds: *files* — source vs generated — and *rules*). "Each rule instance specifies the relationship between a set of input and a set of output files"; rule inputs may be outputs of other rules (dependency graph); generated files always belong to the same package as their rule.
- Build process: 1) **Load** relevant BUILD files; 2) **Analyze** inputs + dependencies, apply rules, produce an **action graph**; 3) **Execute** the actions until outputs are produced. "Since all previous build work is cached, Bazel can identify and reuse cached artifacts and only rebuild or retest what's changed."
- **Hermeticity**: "When given the same input source code and product configuration, a hermetic build system always returns the same output by isolating the build from changes to the host system." Two aspects: **isolation** (tools treated as source code, downloaded into managed file trees) and **source identity** (hashes identify input changes). Benefits: cacheable actions, parallel execution from the action graph, multiple tool versions on one machine, reproducibility. Sandbox execution; remote caching/execution are adjacent subsystems.
- CLI invocation; outputs placed within the workspace; `query` to trace dependencies in code.

### CMake (evidence A)

- Positioning: "an open source, cross-platform family of tools designed to build, test, and package software"; "gives you control of the software compilation process using simple independent configuration files"; "designed to be used in conjunction with the native build environment."
- **Generator architecture**: CMake "generate[s] a native build environment" (Makefiles, Ninja, Visual Studio solutions, Xcode projects) from CMake configuration files; the user then invokes that generated buildsystem (`cmake --build .` delegates to the generator's build tool). "The generated buildsystem is specific to the machine used to generate it and is not redistributable"; "should generally be treated as read-only."
- Workflow: create an out-of-source build directory → configure/generate (`cmake .. -G Ninja -DCMAKE_BUILD_TYPE=Debug`) → build (`cmake --build .`) → optionally `--target install`.
- **Cache**: `CMakeCache.txt` key-value file in the build directory persists compiler/tool/dependency paths and options; `option()` declares toggles; `CMakePresets.json` saves named configure presets (generator, build dir, cache variables, environment).
- Built-in targets across buildsystems: `all`, `help` (lists targets), `clean`, `test`, `install`, `package`, `package_source`.
- Installation rules (`install()` → `CMAKE_INSTALL_PREFIX`); tests executed via the bundled `ctest(1)` tool; binary/source packaging via CPack targets.
- Errors reported while processing CMake files: unsupported compiler, missing dependency → user must resolve (choose another compiler, install or point to dependencies).
- IDE native support documented (KDevelop4, QtCreator, CLion "have native support for CMake-based buildsystems").
- Note: CMake itself is not the execution engine for compilation — the generated native buildsystem is. Evidence that the "definition" and the "engine" roles can be split across two programs while remaining one Type.

## Cross-product Comparison

| Dimension | GNU Make | Apache Maven | Gradle | Bazel | CMake |
|---|---|---|---|---|---|
| Build definition resident in project | makefile (rules: target : prereqs + recipe) | POM (XML) + plugin bindings | settings + build files, task/plugin code | BUILD files (Starlark rules) | CMakeLists/config files |
| Unit of work | target | phase (goal-bound) | task | target/rule → action | target in generated buildsystem |
| Dependency graph | target→prerequisite edges | phase order (fixed lifecycle) + module order | task input/output graph; inferred deps | action graph over rules | expressed in generated buildsystem |
| Engine behavior at invocation | evaluate rules, remake changed | read POM → run lifecycle to requested phase | configure → task graph → execute with up-to-date checks | load → analyze (action graph) → execute | configure/generate → delegate to native build tool |
| Incremental evaluation | yes (remake what changed) — original purpose | not a presented core mechanism | yes, first-class (UP-TO-DATE) | yes, hash-based, cache-backed | delegated to generated build tool (make/ninja do it) |
| Up-to-date correctness emphasis | change detection via prerequisites | low emphasis | declared I/O + validation + cache keys | hermeticity, hashes, sandboxing | generator/tool level |
| External dependency acquisition | none | yes (repositories, central) | yes (repositories, catalogs, locking) | yes (external repos, repo rules) | finds installed packages (no auto-download in core) |
| Multi-module | directory recursion (documented as usable for any task; recursion common practice — not in fetched pages) | aggregation via modules | multi-project + composite builds | packages/repositories; scales to 100k+ files | directory hierarchies (add_subdirectory) |
| Variants/configurations | via variables/conditionals | profiles; packaging types | variants/attributes; flavors via plugins | configurations/platforms | build types (Debug/Release), multi-config generators |
| Tests | recipe-defined | test phases (surefire binding) | test tasks | "build and test tool"; test targets | ctest companion |
| Packaging/install | recipe-defined | package/install/deploy phases | packaging/distribution/publish plugins | deployable packages | install rules + CPack package targets |
| Toolchain handling | assumes environment tools | JVM via plugins | toolchains (declared/resolvable) | tools as source (managed trees), isolation | detects compilers; toolchain files; generator selection |
| Daemon / persistent process | none | separate mvnd tool exists | daemon (documented) | server | none (per-invocation tools) |
| Caching | none in core | none documented | build cache (local/remote) + configuration cache | aggressive caching incl. remote | CMakeCache.txt is *configuration* cache, not output cache |
| Remote/shared execution | no | no | remote build cache; remote exec via Develocity-class (vendor, L3) | remote cache + remote execution | no |
| GUI surfaces | none | none documented | IDE integration (Tooling API; IDE plugins) | CLI-centric | cmake-gui / ccmake |
| IDE integration | editor-level | IDE-level | first-class (Tooling API + IDE plugins) | IDE integrations | native IDE generators/support |
| Wrapper (pinned launcher) | n/a | Maven Wrapper exists (tools list) | Gradle Wrapper (core chapter) | Bazelisk-class (not in fetched pages) | n/a (presets instead) |
| Query/inspection | (target listing via make -qp etc. — not fetched) | (goals via plugins — not fetched) | tasks listing; dependency reports; build scans | `query` documented | `help` target lists targets |
| Reproducibility posture | convention | convention | convention + cache keys | enforced (hermeticity) | machine-specific generated buildsystem (explicitly not redistributable) |

## Abstraction Hierarchy

### L0 — Defining Invariant

Minimal structure without which the product is not recognizable as a build automation system:

1. **Project-resident build definition** — a file (or set of files) inside the project's source tree that declares units of build work, the dependencies between them, and how each output is produced. It travels with the source; anyone with the source has the build.
2. **Ordering engine** — the tool evaluates that definition into a graph and executes units in dependency-correct order (it invokes the project's toolchains/commands — compilers, linkers, packagers, arbitrary commands — as prescribed by the definition).
3. **Artifact production** — execution transforms project inputs (sources, resources, resolved dependencies) into declared outputs (build artifacts) placed in a build/output space, so the build can be re-run against the same definition.

That is the whole core. Notably NOT in L0 (each has a counter-example inside the sample):

- Incremental/up-to-date evaluation — near-universal and historically the founding purpose (Make), but Maven's documented lifecycle model does not center per-unit skipping; a build tool that rebuilds everything each run is still a build automation system. Placed at the top of L1.
- External dependency acquisition — Maven/Gradle/Bazel embed it; Make/CMake do not.
- Daemon, caching, remote execution, wrapper — modern performance machinery (Gradle/Bazel-era); absent in Make/Maven-core/CMake.
- Fixed lifecycle/convention (Maven), rule language (Bazel), generator architecture (CMake) — poles, not core.

### L1 — Common Mature Structure

Present across most/all sampled products; makes the Type practical but not definitional:

- **Incremental evaluation / up-to-date checks** (Make: remake what changed; Gradle: UP-TO-DATE; Bazel: rebuild only what changed; CMake: delegated to generated make/ninja). Depth varies; Maven's is weakest in the sample.
- **Dependency resolution from external repositories** (Maven, Gradle, Bazel) — embedded in ecosystem-oriented tools; environment-oriented tools (Make, CMake) consume system-installed libraries instead.
- **Multi-module structuring** (Maven aggregation, Gradle multi-project/composite, Bazel packages, CMake directory hierarchies).
- **Target/task discovery and dependency inspection** (CMake `help` target documented; Bazel `query` documented; Gradle task listing/dependency reports in manual structure).
- **Clean** as a built-in action (Make phony `clean` pattern; Maven clean lifecycle; CMake clean target; Gradle clean task).
- **Test execution integration** (Bazel "build and test tool"; Maven test phases; Gradle test tasks; CTest).
- **Packaging / install / publish steps** (Maven package/install/deploy; CMake install rules + package targets; Gradle packaging/distribution/publish plugins).
- **Configuration variants** (Maven profiles/packagings; Gradle variants/attributes; Bazel configurations/platforms; CMake build types/multi-config).
- **Toolchain discovery/selection** (CMake compiler detection + toolchain files; Gradle toolchains; Bazel tool isolation).
- **IDE integration surfaces** (Gradle Tooling API + IDE plugins; CMake native IDE support/generators; Bazel IDE integrations).
- **CI invocation as a documented integration** (Gradle's own per-CI-system chapters; Bazel positioned as the tool CI runs).
- **Wrapper / pinned launcher** (Gradle Wrapper and Maven Wrapper documented) — version pinning of the build tool itself per project.
- **Background daemon / persistent process for speed** (Gradle daemon; Bazel server; Maven daemon ships as a separate tool mvnd) — common in the modern era, not universal.

### L2 — Variant / Optional Structure

Depends on philosophy, scale, ecosystem, era:

- **Generator architecture** — definition tool emits a native buildsystem executed by another program (CMake; Ninja sits on the engine side). Splits the L0 roles across two programs.
- **Convention-over-configuration with a fixed lifecycle** (Maven pole) vs **free-form task graph** (Make/Gradle) vs **abstract rule language over concepts** (Bazel).
- **Hermeticity & reproducibility enforcement** — sandboxing, tool isolation, input hashing (Bazel); others rely on convention; CMake explicitly generates machine-specific, non-redistributable buildsystems.
- **Remote caching / remote execution** — Bazel remote cache/execution; Gradle remote build cache; absent in Make/Maven/CMake core.
- **Monorepo / very-large-scale orientation** (Bazel: 100k+ source files, tens of thousands of users).
- **Polyglot vs single-ecosystem** — Gradle/Bazel/CMake span languages; ecosystem-native tools (cargo/npm-class; outside deep sample) fuse build with package management and publishing.
- **Build logic as programs** — plugins/rules authored in a real language (Gradle plugins, Bazel Starlark rules, Maven plugins) vs declarative-only definitions.
- **Presets/profiles for consumer-facing configuration** (CMake presets, Maven profiles).
- **Reporting/analysis surfaces** — build scans/reports, project sites (Maven site), dependency reports.
- **Dependency verification / signing of build inputs** (Gradle dependency verification documented; Bazel source identity).
- **Continuous build** (re-run on file change; Gradle documents it).

### L3 — Vendor-specific Structure (research notes only; must not enter the final document)

- Gradle: `@Input/@Output…` annotation taxonomy, `UP-TO-DATE`/`NO-SOURCE` console labels, `@Destroys`/`@LocalState`, configuration cache + file-system watching, Tooling API, version catalogs, composite builds, Build Scan®/Develocity, wrapper scripts, settings-file vs build-file split, validation warning = "no optimizations" rule, per-CI integration chapters (GitHub Actions/GitLab CI/Jenkins/TeamCity/Travis).
- Maven: Super POM defaults (`target/`, `src/main/java`, `src/test/java`), three named lifecycles (default/clean/site) and exact phase names (validate…deploy), packaging→goal binding tables (compiler:compile, surefire:test, jar:jar…), groupId:artifactId:version coordinates, `<modules>`/packaging=pom aggregation, mvnd/mvnsh/maven-wrapper tool family, site generation.
- Bazel: Starlark, MODULE.bazel/REPO.bazel/WORKSPACE boundary markers, package/BUILD-file definition (no file in two packages; outputs stay in the rule's package), action graph terminology, package_group/visibility, sandboxing, remote execution "dynamic strategy", BazelCon ecosystem talks (SpaceX/Uber/BMW…), `--experimental_workspace_rules_log_file`.
- CMake: cmake(1)/cmake-gui(1)/ccmake(1) tool family, CMakeCache.txt, CMakePresets.json/CMakeUserPresets.json, generator names (Unix Makefiles, Ninja, NMake, MinGW, Visual Studio, Xcode, Watcom WMake…), `-G` irreversibility, `--target`/`--config`/`--verbose`, built-in targets (all/help/clean/test/install/package/package_source), `/fast` target variants, EXCLUDE_FROM_ALL, CMAKE_ variable namespace conventions, CTest flags (-R/-E/-j/-V/CTEST_PARALLEL_LEVEL), CPack, compile_commands.json export.
- Make: tab-recipe syntax + `.RECIPEPREFIX`, phony targets, POSIX.2 conformance, GNU implementation history (Stallman/McGrath/Smith).

## Rejected Findings

- **"Build automation = incremental builds"** — rejected as L0: Maven's documented model does not center per-unit skipping; Make/CMake delegate or predate fine-grained caching. The engine's ordering duty is the invariant; re-execution policy is a spectrum.
- **"Build automation includes dependency download"** — rejected as L0: Make and CMake (core) build without acquiring dependencies.
- **"A build system owns a lifecycle with named phases"** — rejected: Maven-specific philosophy (L2 pole); Make/Gradle/Bazel/CMake expose targets/tasks/rules, not a fixed phase ladder.
- **"CMake is a different Type (a 'build generator')"** — rejected after reading CMake's own positioning ("designed to build, test, and package software"; self-described "de-facto standard software build system"): it is a variant of this Type in which definition-evaluation and command-execution are split across programs.
- **"The build space must be outside the source tree"** — rejected as universal rule: strong convention (CMake documents out-of-source builds as recommended; Bazel writes within the workspace; Gradle build dirs), but Bazel's documented layout contradicts a strict "never in source tree" invariant. Treated as a common convention with product variation.
- **"Remote caching is part of the Type"** — rejected: only the scale-oriented products document it (L2).
- **"Task runners (npm-scripts/Gulp-class) are the same Type"** — deferred: no directory leaf exists for task runners; they lack artifact-graph semantics. Recorded as adjacent concept in boundary findings, not as evidence about this Type.

## Boundary Findings

- **vs Continuous Integration Platform** (§12 sibling; *unprocessed at pass time — joint-review flag*): the build tool answers "how does this project build" — it evaluates a project-resident definition and produces artifacts within one invocation, on a developer machine or a CI agent. The CI platform answers "when/where do builds run, for whom, with what history" — triggers, shared/hosted execution, orchestration across jobs, result records. Evidence of the seam from the build-tool side: Gradle documents dedicated chapters for running *under* GitHub Actions/GitLab CI/Jenkins/TeamCity; Bazel positions itself as the build+test tool that gets run. Removal test: remove the project-resident build definition + artifact production → orchestration platform (CI); remove triggers/hosting/history → build automation system. Recommend joint review when continuous-integration-platform is processed.
- **vs Artifact Repository / Package Registry** (§12 siblings; artifact-repository already processed): the build tool *produces* artifacts and may *publish* them (Maven deploy phase, Gradle publish plugins); it does not *operate custody* of published artifacts (repositories, promotion, proxying). Consistent with artifact-repository pass's recorded seam ("CI Platform executes builds vs keeps records; Dependency Management declares/chooses versions vs stores/serves artifacts").
- **vs Dependency Management Application** (§12 sibling; unprocessed): heavy overlap in Maven/Gradle/Bazel (embedded resolution engines, version catalogs, conflict rules, locking). Working seam: dependency management centers version selection/reconciliation as the managed problem; the build tool consumes resolved dependencies as build inputs and orders work. Existence proof of separation: Make and CMake-core build without any dependency resolution, so resolution is not definitional for build automation. Flag for joint review when that leaf is processed; ecosystem-native tools (cargo/npm-class) will straddle.
- **vs Task Runner (adjacent concept, no directory leaf)**: chaining arbitrary commands by hand (run-anything scripts) without a declared input→output dependency graph drifts out of this Type. Make's own generality ("any task where some files must be updated automatically from others") shows the graph semantics are what keep a task runner inside the Type.
- **vs IDE / Code Editor** (§12 siblings): IDEs consume and invoke build systems (CMake native IDE support; Gradle Tooling API + IDE plugins; CMake "generated buildsystems… no reason to populate properties manually in an IDE"). The build system remains the definition+engine; the IDE is an invoker/presenter. Not a boundary issue, recorded for completeness.
- **vs Infrastructure-as-Code Platform** (§14 sibling): same abstract pattern (declared graph + engine + converge), different object domain (infrastructure provisioning vs software artifact production). No market confusion observed; recorded to preempt over-abstraction.
- **vs Project Scaffolding / Code Generator** (§12 sibling): scaffolding creates the initial project (Maven archetypes, Gradle build-init are side features); the build automation system repeatedly builds the project thereafter. One-shot generation vs repeatable production loop.

## Historical / Market-Sample Check (per §24 spirit)

- **1977-era Make** fits the L0 definition fully: project-resident rule file, dependency-ordered execution, artifact production. It lacks every modern L1/L2 item (daemon, cache, remote, dependency acquisition) and remains unmistakably a build automation system → definition is not over-fit to the modern era.
- **POSIX-standardized Make** (IEEE 1003.2-1992) shows the Type predates and transcends any single vendor's feature set.
- **CMake** (1990s–2000s generator era) fits with the engine role delegated → definition must not require "one program does both definition-evaluation and execution".
- **Modern era (Gradle/Bazel)** adds daemon/caching/remote/hermeticity — all correctly excluded from the definition.
- Regional/ecosystem-native tools (MSBuild, cargo, npm-class) were not deeply sampled; the conceptual core (definition + ordered engine + artifacts) is expected to hold, but their fused dependency/package semantics are recorded as a known straddle, not evidence.

## Uncertainties

- Make's exact up-to-date mechanism (timestamp comparison) is classic knowledge but was not on the fetched pages; the fetched text documents behavior ("remake when prerequisites change") without the mechanism. Final doc states behavior, not mechanism.
- Maven's actual incremental behavior (e.g., compiler plugin useIncrementalCompilation) was not researched; the doc only claims what Maven's own pages present — a fixed lifecycle — and avoids asserting "Maven never skips work".
- Bazel/Bazelisk wrapper-class tooling and Maven wrapper details come from tool listings, not deep pages; wrapper claims kept generic (Gradle's wrapper is the deeply documented case).
- Gradle remote execution was not claimed (only remote build cache is documented in the fetched material); Develocity-class remote execution kept at L3-market-knowledge level.
- Task-runner products (npm scripts, Gulp) were not fetched at all; the boundary statement about them is conceptual, marked as such.
- Ecosystem-native build tools (cargo, MSBuild, npm/yarn/pnpm) were not sampled deeply; the Variants section describes them at low assertive strength.

## Final Synthesis

A Build Automation System is the software that turns a project's build definition into built artifacts. Its canonical world model:

```text
Project source tree
└── Build definition (project-resident files)
    ├── Units of build work (targets / tasks / rules / phases)
    ├── Dependencies between units
    └── Input → output prescription (how each output is produced)
          ↓ evaluated by
Build engine (order units, invoke toolchains, skip/repeat as designed)
          ↓ produces
Build artifacts (binaries, packages, reports) in a build/output space
```

Defining core (3 properties): project-resident build definition; dependency-ordered execution engine invoking the project's toolchains; artifact production from project inputs. Common mature structure adds incremental evaluation, dependency resolution, multi-module structuring, discovery/clean/test/package/install surfaces, variants, toolchain handling, IDE and CI integration, wrappers, daemons, caches. Variant poles: convention-lifecycle (Maven), generator architecture (CMake), free-form task graph (Make/Gradle), hermetic action-graph at monorepo scale (Bazel). The Type is bounded by: CI platforms (when/where vs how), artifact repositories (custody vs production), dependency management (selection vs consumption), IDEs (invoker vs engine).
