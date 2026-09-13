# Research Notes — Dependency Management Application

Research date: 2026-09-07
Slug: dependency-management-application
Directory leaf: Dependency Management Application (§12 Software Development & Product Engineering)

## Research Goal

Understand what a Dependency Management Application is as an Application Type: the core objects of its world model (declaration, resolution, recorded selection), who uses it, how the dependency loop actually flows, which rules govern its behavior, and where it separates from neighboring developer-tooling Types (Build Automation System, Package Registry, Artifact Repository, SCA, SBOM Management, Source Code Hosting Platform).

Context from prior passes (STATUS.md boundary issues):
- build-automation-system (processed) recorded: "dependency management centers version selection/reconciliation as the managed problem; the build tool consumes resolved dependencies as build inputs and orders work. Existence proof of separation: Make and CMake-core build without any dependency resolution." Flagged a three-way straddle: ecosystem-native build tools (cargo/npm-class) fuse build + dependency resolution + publishing, needing a joint statement with dependency-management-application and package-registry.
- artifact-repository (processed) recorded: "Dependency Management Application | 下游消费侧 | 它管理项目内的依赖声明/版本选择（lockfile、升级）；Artifact Repository 只是满足这些声明的供给方。判据：管理的是'用哪个版本'还是'制品本身'" and "只剩'声明/选择依赖版本'，它是 Dependency Management".
- This pass must document its side of both seams and set up the joint review with the still-unprocessed package-registry leaf.

## Initial Boundary

Working hypothesis before research:

1. Core use: manage the external components (packages/libraries/modules) a software project depends on — declare them, resolve compatible versions, record the outcome, keep it current.
2. Users: software developers; in the automated-update form, the platform/automation acts on the team's behalf.
3. Nearest neighbors: Build Automation System (sibling, processed), Package Registry (sibling, unprocessed), Artifact Repository (sibling, processed), Software Composition Analysis / SCA (§15), SBOM Management (§15), Source Code Hosting Platform, Patch Management (§14).
4. Likely boundary confusion: (a) dependency resolution embedded inside build tools (Maven/Gradle/cargo-class); (b) security analysis of dependencies (SCA) vs dependency currency; (c) the registry (server-side venue) vs the manager (project-side selection).
5. Unknowns: does the Type span both the per-ecosystem dependency manager (Bundler/Cargo/Poetry class) and the automated dependency-update application (Renovate/Dependabot class)? Is the lockfile definitional or the modern implementation of something more abstract? How do older build-embedded realizations (Maven-class) fit?

## Research Questions

1. What are the core objects? (manifest/declaration, lockfile/recorded selection, config, sources)
2. What exactly does "resolution" mean in each product, and where does it run?
3. What is the change loop? (add/remove/upgrade commands; automated update proposals)
4. What rules govern the selection? (constraint semantics, compatibility policies, conflict behavior, lock priority, conservative re-resolution)
5. How does the recorded selection relate to reproducibility, review, and merge workflows?
6. Where does materialization (install/fetch) sit — definitional or common?
7. How do the two product lineages (per-ecosystem manager CLI vs cross-ecosystem update application) relate to one core?
8. Where does security integration (vulnerability alerts, security updates) sit relative to the Type's center?
9. How does the Type relate to build tools, registries, artifact repositories, and hosting platforms?

## Representative Products

Selection principles applied: market representation + documentation completeness + different product philosophies + different customer tiers; spanning both hypothesized lineages.

| Product | Lineage | Philosophy | Customer tier | Docs fetched |
|---|---|---|---|---|
| Renovate (Mend) | automated dependency updates | standalone, cross-ecosystem, config-driven automation; SaaS app or self-hosted OSS | individual OSS → enterprise (Mend-hosted app) | docs.renovatebot.com (home, key-concepts/how-renovate-works, key-concepts/dashboard) |
| Dependabot (GitHub) | automated dependency updates | platform-native, embedded in the code-hosting platform; framed under supply-chain security | all GitHub users (free) | docs.github.com (secure-your-supply-chain section: manage-your-dependency-security, controlling-dependencies-updated, configure-version-updates) |
| Bundler (Ruby) | per-ecosystem dependency manager | minimal manifest+lockfile CLI; "exit from dependency hell" | Ruby developers (community OSS, ships with Ruby) | bundler.io; guides.rubygems.org (gemfile, dependency-resolution, gemfile-lock, updating_gems) |
| Cargo (Rust) | ecosystem-native fused tool | package manager fused with build + publish; the recorded straddle case | Rust developers (community OSS) | doc.rust-lang.org/cargo (home, guide/why-cargo-exists, guide/cargo-toml-vs-cargo-lock, reference/resolver) |
| Poetry (Python) | per-ecosystem dependency manager | dependency management + packaging in one; environment isolation | Python developers (community OSS) | python-poetry.org/docs (introduction, basic-usage, managing-dependencies) |

Not sampled (recorded as gaps, not evidence): Maven/Gradle (covered by the build-automation pass as embedded-resolution straddle), npm/yarn/pnpm, Composer, CocoaPods, Go modules, pip-tools, PyUp, Greenkeeper (discontinued), Snyk/Mend SCA (SCA leaf territory), system package managers (APT-class).

## Sources

Tier 1 (official operational documentation), all fetched 2026-09-07:

- Renovate — https://docs.renovatebot.com/ ; https://docs.renovatebot.com/key-concepts/how-renovate-works/ ; https://docs.renovatebot.com/key-concepts/dashboard/
- Dependabot — https://docs.github.com/en/code-security/dependabot (section root) ; https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security ; https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/controlling-dependencies-updated ; https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies ; https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/configure-version-updates
- Bundler — https://bundler.io/ ; https://guides.rubygems.org/gemfile/ ; https://guides.rubygems.org/dependency-resolution/ ; https://guides.rubygems.org/gemfile-lock/ ; https://guides.rubygems.org/updating_gems/
- Cargo — https://doc.rust-lang.org/cargo/ ; https://doc.rust-lang.org/cargo/guide/why-cargo-exists.html ; https://doc.rust-lang.org/cargo/guide/cargo-toml-vs-cargo-lock.html ; https://doc.rust-lang.org/cargo/reference/resolver.html
- Poetry — https://python-poetry.org/docs/ ; https://python-poetry.org/docs/basic-usage/ ; https://python-poetry.org/docs/managing-dependencies/

Fetch notes: one 404 on a stale Dependabot URL (docs reorganized under "Securing your supply chain"); recovered via the section root. Large reference pages (Renovate configuration-options, Dependabot options reference, Cargo commands) intentionally not fetched; observations rely on the fetched concept/how-to pages. No source required abandonment.

## Product A — Renovate (Mend)

### Key observations (Layer A unless noted)

- Self-description: "Automated dependency updates. Multi-platform and multi-language." Value proposition: "Get pull requests to update your dependencies and lock files."
- Workflow (documented, key-concepts/how-renovate-works): clone repository → scan package files to extract dependencies → look up registries to check for updates → apply grouping rules → push branches and raise Pull Requests. Finalize: config migration, clean stale branches.
- Module architecture: platform (source-control interaction/clone), manager (find files by name, extract dependencies), datasource (look up versions of a dependency), versioning (validate and sort returned versions). Example documented: gitlabci manager finds `python:3.10-alpine` → docker datasource returns version list → docker versioning picks the compatible next version.
- Config: merged "most important to least: cli > env > file > default"; ESLint-like shareable config presets; behavior customization via configuration files.
- Finds "relevant package files automatically, including in monorepos"; replacement PRs to migrate from deprecated dependencies ("works with most managers").
- Dependency Dashboard: an issue created in the repository showing "an overview of the status of all updates"; enables an approval workflow (require approval for all / major-only / specific packages); lists Closed/Ignored updates with checkboxes to re-request; warns on registry-flagged deprecated packages and community-sourced replacements; abandonment detection preset (default abandonmentThreshold of 1 year in the recommended preset; prevents updates to truly abandoned packages).
- Scheduling: "Reduce noise by scheduling when Renovate creates PRs." Automerge as a key concept. Minimum release age as a key concept. Changelogs integration.
- Vulnerability remediation PRs "will still get created immediately without requiring approval" (security bypasses the approval workflow).
- Platforms: GitHub, GitLab, Bitbucket (Cloud/Server), Azure DevOps, AWS CodeCommit, Gitea, Forgejo, Gerrit (experimental). Run as npm package, container image, or Mend-hosted GitHub App. AGPL-3.0-only open source.
- Interpretation: Renovate never materializes dependencies and never builds; it operates on manifests + lockfiles and hands proposed changes to the platform's review flow. Its "resolution" work is update selection (which next version is valid per versioning rules), delegating full re-resolution/lockfile rewriting to the ecosystem tooling it invokes.

## Product B — Dependabot (GitHub)

### Key observations (Layer A unless noted)

- Positioning: GitHub's docs now place all Dependabot functions under "Securing your supply chain" — "Managing your dependency security — Customize and configure features for dependency management." Family: Dependabot alerts (vulnerable dependency found), malware alerts, security updates (PRs updating vulnerable dependencies), version updates (automatically update packages), dependency graph (identify/explore dependencies, incl. transitive via automatic dependency submission and a submission API), multi-ecosystem updates (group updates across ecosystems into one consolidated PR), auto-update GitHub Actions, innersource advisories, release integrity.
- Version updates enablement: commit a `dependabot.yml` to `.github/` (or enable via Settings → Advanced Security → Dependabot version updates, which creates a basic file). Mandatory keys: `version: 2`, `updates` list. Per entry: `package-ecosystem` (npm, docker, github-actions, bundler, composer, maven, pip, …), `directory`/`directories` (glob/globstar supported), `schedule.interval` (daily/weekly/monthly, optional day).
- Behavior: "Dependabot checks the manifest files on the default branch for outdated dependencies. If it finds outdated dependencies, it will raise pull requests against the default branch to update the dependencies."
- Selection policy config: `allow` (dependency-type: direct/all/production/development; update-types restricted to semver levels), `ignore` (dependency-name with wildcards, versions, update-types), `open-pull-requests-limit` (0 disables a manager), `versioning-strategy` (default: "increase the minimum version requirement" for apps, "widen the allowed version requirements" for libraries; options include increase, increase-if-necessary), `vendor` (maintain vendored dependencies — documented for Go modules automatically and Bundler vendor/cache), `registries` (private registry auth via encrypted secrets; can remove access to public registries).
- Defaults: "By default, Dependabot creates version update pull requests only for the dependencies that are explicitly defined in a manifest (direct dependencies)"; indirect (lockfile-defined) updates opt-in. Security updates "will always be created regardless of the update-types setting."
- Review-loop affordances: comment commands (`@dependabot ignore`, `@dependabot unignore`); status via the "Dependabot tab in the dependency graph" (configured managers + last check time); re-running jobs on GitHub Actions runners (hosted or self-hosted).
- Forks: version updates not auto-enabled on forks (explicit enablement required).
- Interpretation: platform-native realization of the update-application lineage; the dependency-management function (scan manifests, select updates, propose recorded-selection changes as reviewable PRs) is embedded in the hosting platform, with alerts/graph as SCA-adjacent satellites.

## Product C — Bundler (Ruby)

### Key observations (Layer A unless noted)

- Self-description: "Bundler provides a consistent environment for Ruby projects by tracking and installing the exact gems and versions that are needed. Bundler is an exit from dependency hell, and ensures that the gems you need are present in development, staging, and production. Starting work on a project is as simple as `bundle install`."
- Declaration: the Gemfile — "describes the gem dependencies required to execute associated Ruby code", placed in the project root. Syntax: global `source` (e.g. rubygems.org; only one global source since 1.13), `gem` lines with name (required) + optional version specifiers (`>= 1.4.2`, ranges, exact `=`, pessimistic `~>` which "constrains both a lower and an upper bound"), `require:` autorequire control, `group:`/`platforms:` membership, per-gem `source:`, `git:` (branch/tag/ref, submodules), `path:`, block forms, `install_if` conditional installs, `gemspec` method, `eval_gemfile` splitting. Source priority: explicit per-gem source > parent's source > global source.
- Resolution (concept page): "Resolving means choosing exactly one version of every gem in the graph so that all requirements hold at the same time." The graph includes gemspec-declared transitive deps; "the same gem often appears several times with different version requirements." "Simply taking the newest version of everything does not work" — documented conflict example (payments needs money >= 7.0, reporting needs money ~> 6.1; resolver picks an older payments). "Resolution is a search across combinations rather than a per-gem lookup." Algorithm: PubGrub ("originally developed for Dart's package manager and since adopted across ecosystems"); conflict errors "walk through the conflicting requirement chains, each step naming which gem demanded which versions of which dependency." Prerelease versions never considered unless explicitly named.
- Recorded selection (concept page): "Resolution does not happen on every install. The first `bundle install` resolves and writes the chosen versions to `Gemfile.lock`. From then on `bundle install` reuses the locked versions exactly, which is why it is fast and gives every machine and deploy the same gems. If you edit the Gemfile, the next `bundle install` re-resolves only as much as the change requires and leaves the rest of the lockfile untouched." "Without that record, two machines installing the same list of gems at different times can resolve to different versions, which is the problem Bundler was created to solve."
- Lockfile anatomy (documented): GEM blocks (remote + specs at exact versions, with requirement lines explaining why versions were chosen — "they are requirements, not choices"), GIT blocks (pinned `revision:` "plays the role that the version number plays"), PATH blocks, PLATFORMS, DEPENDENCIES (direct deps; `!` marks non-default source), CHECKSUMS (SHA-256 of packaged gem, "Bundler verifies every gem against it during installation. A gem that was tampered with after the lockfile was written fails to install"), RUBY VERSION, BUNDLED WITH (auto-switch to the writing Bundler version). "Bundler maintains the file. You never edit it by hand."
- Commit guidance: "For an application, always commit Gemfile.lock… For a gem, the lockfile is not part of the package" — consumers resolve from the gemspec constraints and ignore any shipped lockfile. Platform normalization (`bundle lock --normalize-platforms`) before committing. Merge conflicts: "never resolve a merge conflict in Gemfile.lock by hand. Bundler refuses to load a lockfile containing conflict markers"; restore one side, merge the Gemfile, re-lock.
- Change loop (updating_gems): conservative update semantics — "when you update a gem, bundler will not update a dependency of that gem if another gem still depends on it"; unmodified gems treated "as a single, unmodifiable unit"; `bundle install` after a Gemfile edit re-locks conservatively; `bundle update <gem>` updates one gem + its deps to latest allowed; `bundle update` re-resolves from scratch ignoring the lockfile ("keep `git reset --hard` and your test suite in your back pocket"). Transparent lock update at boot for minimal changes ("last known good" configuration persisted); failure instructs running `bundle install`.
- Cooldown (concept page): "excludes gem versions published less than a chosen number of days ago from resolution… versions already in your lockfile are never retracted by it."
- Materialization: `bundle install` installs the locked gems; `Bundler.setup`/`Bundler.require` scope the runtime load path to groups; `bundle config` for credentials/settings; deployment mode; caching/vendoring guides exist (nav-observed, not fetched).
- Constraint dilemma (documented discussion): too strict (`=`) vs too loose (`>=`) vs pessimistic (`~>`); "RubyGems has over 100,000 packages, this assumption [universal SemVer compliance] simply doesn't hold in practice."

## Product D — Cargo (Rust)

### Key observations (Layer A unless noted)

- Self-description: "Cargo is the Rust package manager. Cargo downloads your Rust package's dependencies, compiles your packages, makes distributable packages, and uploads them to crates.io, the Rust community's package registry." Motivation: "most non-trivial programs will likely have dependencies on external libraries, and will therefore also depend transitively on their dependencies. Obtaining the correct versions of all the necessary dependencies and keeping them up to date would be hard and error-prone if done by hand."
- Four documented functions: two metadata files; fetches and builds dependencies; invokes rustc with correct parameters; conventions. "Cargo will automatically fetch any dependencies you have defined for your artifact from a registry, and arrange for them to be added into your build as needed."
- Manifest vs lock (guide): "Cargo.toml is about describing your dependencies in a broad sense, and is written by you. Cargo.lock contains exact information about your dependencies. It is maintained by Cargo and should not be manually edited." "When in doubt, check Cargo.lock into the version control system." Reproducibility motivation documented via the git-dependency example (unpinned rev → different builds on different days; manual rev pinning "tedious and error prone"; Cargo.lock records the exact revision).
- Resolution (reference): "One of Cargo's primary tasks is to determine the versions of dependencies to use based on the version requirements specified in each package. This process is called 'dependency resolution' and is performed by the 'resolver'. The result of the resolution is stored in the Cargo.lock file which 'locks' the dependencies to specific versions, and keeps them fixed over time. The `cargo tree` command can be used to visualize the result of the resolver."
- Resolver mechanics (documented): backtracking search with pseudo-code; version unification ("Cargo reuses versions where possible to reduce build times and allow types from common dependencies to be passed between APIs"; conflicts → backtrack, error if no solution); prefers highest version; caret requirements as SemVer-compatible ranges (`"1.0"` = `>=1.0.0,<2.0.0`); incompatible requirements → multiple versions may coexist in the graph ("version-incompatibility hazards": types from different versions are distinct; `cargo tree -d` identifies duplicates); `links` constraint (one copy of a native library); yanked releases "ignored… unless they already exist in the Cargo.lock file or are explicitly requested by the `--precise` flag"; features resolved as-if all enabled for locking; resolver versions 1/2/3 (feature-unification and rust-version behavior differences); rust-version-aware selection (`resolver.incompatible-rust-versions`).
- Lock priority: "Cargo gives the highest priority to versions contained in the Cargo.lock file, when used. This is intended to balance reproducible builds with adjusting to changes in the manifest." Manifest edit → stale lock entry ignored → re-resolve → lock updated. `--locked`/`--frozen` flags "prevent automatic updates when requirements change, and return an error instead."
- Change loop: "Dependency resolution is automatically performed by all Cargo commands that need to know about the dependency graph." `cargo update` (all packages), `cargo update -p <pkg>` (targeted), `--precise`, `--recursive`. Overrides via `[patch]` ("appear as an overlay to a registry"). Dependency kinds: normal / build / dev (dev-deps of non-members ignored in resolution).
- Troubleshooting surfaces (documented): `cargo tree --invert` ("why was a dependency included"), `--edges features`, `--duplicates` ("unexpected dependency duplication"), resolver trace logging; guidance for SemVer-breaking patch releases (yank, `--precise`, `=` requirements, `--locked` installs).
- Interpretation: the recorded straddle case — Cargo fuses dependency management (manifest/lock/resolver/update) with build orchestration (compile/publish). Both functions are first-class in one tool.

## Product E — Poetry (Python)

### Key observations (Layer A unless noted)

- Self-description: "Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you. Poetry offers a lockfile to ensure repeatable installs, and can build your project for distribution." (The market's most explicit self-labeling of the Type.)
- Declaration: `pyproject.toml` — `project.dependencies` per PEP 621 (Poetry 2.0+) or `tool.poetry.dependencies` (legacy); "a mapping of package names and version constraints"; rich constraint syntax (caret, tilde, wildcard, inequality, multiple constraints); `poetry add pendulum` "will automatically find a suitable version constraint and install the package and sub-dependencies"; `poetry init` for existing projects; `poetry new` scaffolds.
- Operating modes: package mode (default; packaging metadata mandatory; project installed editable) vs non-package mode (`package-mode = false` — "If you want to use Poetry only for dependency management but not for packaging").
- Dependency groups: implicit `main` group (runtime); named groups per PEP 735 (`dependency-groups`) or `tool.poetry.group.<group>`; optional groups (`--with`), `--without`, `--only`, include-groups; "All dependencies must be compatible with each other across groups since they will be resolved regardless of whether they are required for installation or not"; groups are "labels… a way to organize the dependencies logically"; extras for runtime-optional functionality.
- Resolution: "the dependency resolver at the heart of Poetry" (FAQ); "it can take time to find a valid solution" for some dependency sets; searches registered repositories (`tool.poetry.source`) with PyPI fallback; "attempts to find the best match for the version constraint you have specified."
- Recorded selection: `poetry install` without lock → resolves, downloads, "writes all the packages and their exact versions… to the poetry.lock file, locking the project to those specific versions"; with lock → "uses the exact versions listed in poetry.lock to ensure that the package versions are consistent for everyone working on your project… This is by design, it ensures that your project does not break because of unexpected changes in dependencies." Commit guidance: applications commit poetry.lock ("Your CI server, production machines, other developers… everything and everyone runs on the same dependencies"); libraries omit it ("The application ignores your library's lock file. It can use whatever dependency version meets the constraints in your pyproject.toml") with a documented tradeoff discussion. Warning displayed "when executing an install command if poetry.lock and pyproject.toml are not synchronized."
- Change loop: `poetry update` — "fetch the latest matching versions (according to your pyproject.toml file) and update the lock file with the new versions. (This is equivalent to deleting the poetry.lock file and running install again.)"
- Synchronization: "Dependency synchronization ensures that the locked dependencies in the poetry.lock file are the only ones present in the environment, removing anything that's not necessary" (`poetry sync`, combinable with group options).
- Environment isolation: "Poetry makes project environment isolation one of its core features… it will always work isolated from your global Python installation"; virtualenv creation/management; `poetry run`; respects externally activated environments; universal locking across declared Python versions.
- Layering optional groups for multi-stage Docker builds documented.

## Cross-product Comparison

| Dimension | Renovate | Dependabot | Bundler | Cargo | Poetry |
|---|---|---|---|---|---|
| Self-label | "Automated dependency updates" | "dependency management" features under supply-chain security | "manage a Ruby application's gems"; "dependency management" (guides section name) | "the Rust package manager" | "dependency management and packaging" |
| Declaration object | reads existing package files (manager modules) | reads manifests per `package-ecosystem` | Gemfile (project root) | Cargo.toml `[dependencies]` | pyproject.toml `project.dependencies` |
| Recorded selection | updates lock files via PRs | updates manifests/lockfiles via PRs | Gemfile.lock (never hand-edited) | Cargo.lock (never hand-edited) | poetry.lock (never hand-edited) |
| Resolution locus | update-selection logic + delegated re-resolution | update-selection logic + delegated re-resolution | embedded resolver (PubGrub) | embedded resolver (backtracking + unification) | embedded resolver ("at the heart of Poetry") |
| Change loop form | scheduled scan → PRs (grouping, automerge, approval, presets) | scheduled scan → PRs (allow/ignore, versioning-strategy, comment commands) | commands: `bundle install` (conservative re-lock), `bundle update [gem]` | commands: `cargo update [-p] [--precise]`; auto re-resolve on manifest edit | commands: `poetry add/remove/update`, `poetry sync` |
| Materialization | none (hands off to CI) | none (hands off to CI) | `bundle install` + runtime setup | fetch + build integration | `poetry install` into managed virtualenv |
| Ecosystem scope | multi-ecosystem (manager modules) | multi-ecosystem (`package-ecosystem` values) | single (RubyGems) | single (crates.io + git/path) | single (PyPI + private repos) |
| Surface | platform PRs + Dependency Dashboard issue + config file | platform PRs + dependabot.yml + dependency-graph tab | CLI + Gemfile/Gemfile.lock + bundle config | CLI + Cargo.toml/Cargo.lock + config | CLI + pyproject.toml/poetry.lock + config.toml |
| Security integration | vulnerability remediation PRs bypass approval | alerts, security updates, malware alerts, dependency graph | (ecosystem-level CVE guide; not core) | (not core) | (not core) |
| Supply sources | datasource modules (registries) | registries config incl. private + secrets | source priority (global/per-gem/git/path) | registry + git/path + overrides overlay | registered repositories + PyPI fallback |
| Customer tier | OSS → enterprise (Mend-hosted) | all GitHub users | Ruby community (bundled with Ruby) | Rust community | Python community |

Cross-product commonalities (Layer B):

1. **Manifest + recorded-selection pair**: all five products operate on a declaration file and a recorded concrete selection (lockfile-class). The pair is the Type's shared object structure.
2. **Resolution as constrained search**: Bundler (PubGrub, "search across combinations"), Cargo (backtracking pseudo-code, unification), Poetry ("find a valid solution") document resolution as a search that can fail with explanations; Renovate/Dependabot perform the update-selection slice of the same problem.
3. **Recorded selection is machine-maintained**: Bundler ("You never edit it by hand"), Cargo ("should not be manually edited"), Poetry (written/updated by Poetry; warning on desynchronization). Hand-editing the record is anti-pattern across the sample.
4. **Lock-first reuse**: later operations reuse the recorded selection instead of re-deciding (Bundler, Cargo lock priority, Poetry) — with re-resolution triggered by declaration edits (all) or explicit update commands (all).
5. **Conservative change semantics**: Bundler documents it most explicitly (unmodifiable units, dependency-of-updated-gem protection); Cargo balances "reproducible builds with adjusting to changes in the manifest"; Poetry's update is scoped to "latest matching versions".
6. **Commit-the-lock guidance with an application/library split**: Bundler, Cargo, Poetry all document committing the lock for applications; library packages ship constraints only (Bundler and Poetry document that consumers ignore library lockfiles).
7. **Configured supply sources**: every product resolves against configurable sources (registries, git, path, private registries with credentials).
8. **Reviewable dependency changes**: in the update-application lineage, changes surface as PRs/MRs; in the manager lineage, manifest+lock diffs are the reviewable unit inside normal version-control workflow. Both make dependency changes explicit, diffable events.
9. **Conflict as first-class outcome**: resolution failure is a designed state with explanatory output (Bundler requirement chains, Cargo backtracking errors, Poetry resolution time/validity).

Lineage differences (Layer B):

- **Materialization** belongs to the manager lineage only; update applications never install.
- **Ecosystem scope**: manager lineage is per-ecosystem; update-application lineage is multi-ecosystem by design.
- **Surface**: manager lineage is CLI + files; update-application lineage is platform-integrated (PRs, dashboards, status tabs) + a config file.
- **Security integration**: strongest in the update-application lineage (and framed there as supply-chain security); manager lineages keep it ecosystem-level or absent.

## Canonical Model

### L0 — Defining Invariant

Three jointly-held structures. The jointly-held property is load-bearing:

1. **The dependency declaration of record** — a persistent, project-resident record of the external components the project depends on, each identified (name) and qualified (version constraint; optionally source/kind). Remove → there is no managed problem (a version feed or registry browser instead).
2. **Resolution into a concrete coherent selection** — the application computes the exact set of component versions — including transitive dependencies — that jointly satisfies the declared constraints, reconciling competing requirements by search over combinations (not per-component lookup), against available versions from configured sources. Remove → a manifest editor or a list, not management.
3. **The resolved selection held as the project's state of record** — the concrete chosen versions are held as durable project state that later operations reuse instead of re-deciding (lockfile-class record in the modern form; deterministic re-resolution over a persistent cache as the older build-embedded realization). Remove → per-operation resolution with drifting results; the reproducibility problem the Type exists to solve returns; update-applications become impossible (they diff recorded selections).

The **managed change loop** — deliberate, application-mediated change to the dependency set (declaration edits and/or selection refreshes) that re-runs resolution and moves the records forward coherently — is treated as the Type's defining interaction loop rather than a fourth invariant: it is implied by the three records being live (editable declaration + re-running resolution + maintained selection), and every sampled product realizes it (commands in the manager lineage; scheduled proposals in the update lineage).

Evidence: L0-1 (A×5: Gemfile, Cargo.toml, pyproject.toml, Dependabot manifests, Renovate package files); L0-2 (A×3 embedded resolvers + A×2 update-selection engines); L0-3 (A×5: Gemfile.lock, Cargo.lock, poetry.lock, Dependabot/Renovate lockfile updates).

### L1 — Common Mature Structure

- Materialization into the project environment (install/fetch; manager lineage; update lineage hands off to CI)
- Update/currency operations with per-dependency targeting and conservative semantics
- Transitive-dependency visibility (tree/graph inspection, "why is this included" inversion queries)
- Version-constraint semantics (pessimistic/caret/tilde/wildcard/inequality ranges; prerelease opt-in)
- Dependency classification (direct vs transitive; runtime vs dev/test/build; groups; platforms)
- Conflict machinery with explanatory failure output
- Lockfile hygiene (commit guidance, merge-conflict handling, platform normalization, checksums, toolchain pinning)
- Configured supply sources (public registry default; private registries with credentials; git/path sources)
- Config layering + shareable presets (update lineage; config commands in manager lineage)
- Monorepo/multi-project coordination (workspaces, directories globs, automatic package-file discovery)

### L2 — Variant / Optional Structure

- Automated update proposals as PRs with scheduling, grouping, automerge, approval workflows (the update-application lineage's core job; absent in manager lineage)
- Security-triggered updates bypassing normal cadence/approval (Dependabot security updates; Renovate vulnerability remediation)
- Vulnerability alerts, dependency graphs, license policies (SCA-adjacent satellites)
- Release-age policies: cooldown (Bundler), minimum release age (Renovate)
- Deprecation/abandonment detection and replacement migration (Renovate)
- Vendoring dependencies into the repository (Bundler cache, Dependabot vendor option, cargo vendor)
- Yanked-release handling policies (Cargo)
- Versioning-strategy selection (app vs library postures; pin vs widen)
- Environment isolation as a bundled concern (Poetry virtualenvs; Bundler runtime setup)
- Multi-ecosystem consolidated updates (Dependabot)
- System-level package management (APT-class) — adjacent domain with a machine-wide unit rather than a project dependency set; excluded from the Type

### L3 — Vendor-specific Structure (research notes only)

- Renovate: manager/datasource/platform/versioning module architecture; config merge order (cli > env > file > default); Dependency Dashboard as a repo issue with dynamic Markdown checkboxes; abandonment presets with community overrides; Mend-hosted app; AGPL licensing.
- Dependabot: comment commands (`@dependabot ignore/unignore`); Dependabot tab inside the dependency graph; fork non-auto-enable; innersource advisories; auto-triage rules for alerts; self-hosted runner configuration.
- Bundler: BUNDLED WITH auto-switching; transparent lock update at boot; `lockfile` method / `--no-lock` / `BUNDLE_LOCKFILE` precedence; `install_if`; `eval_gemfile`; git_source shorthands (github/gist/bitbucket); `force_ruby_platform`; PubGrub; source-priority heuristics; "unmodifiable unit" conservative-update articulation.
- Cargo: resolver versions 1/2/3; feature unification (incl. resolver "2" differences); `links` single-copy constraint; `[patch]`/overrides overlay; `--precise`/`--locked`/`--frozen`; rust-version-aware selection; semver-trick guidance; `cargo tree --invert/--duplicates` diagnostics.
- Poetry: package-mode vs non-package mode; PEP 621/PEP 735 alignment; `poetry sync`; layering optional groups for multi-stage Docker; universal locking across Python versions; virtualenv auto-management.

## Rejected Findings

- **"The lockfile is the defining structure"** — rejected as too implementation-specific. The recorded selection is definitional; the lockfile is its modern canonical implementation. Older build-embedded realizations (Maven-class, per the build pass) hold the selection via deterministic re-resolution over a persistent cache rather than a project-resident lock record — recorded as a weaker realization/boundary case, not silently excluded or silently folded in.
- **"Dependency management = installing packages"** — rejected: the update-application lineage (Renovate/Dependabot) never installs; materialization is L1.
- **"Dependency management = keeping dependencies secure"** — rejected: security analysis is SCA's center (§15); security-triggered updates are L2 integration. GitHub's supply-chain-security framing of Dependabot is market framing drift, recorded as evidence of the SCA boundary pressure, not as the Type's definition.
- **"Resolution always picks the newest version"** — rejected: all sampled resolvers pick the newest *allowed/compatible* version under constraints, unification rules, lock priority, and (variant) release-age policies; Cargo documents cases where it deliberately does not deduplicate.
- **"The registry is part of this Type"** — rejected: registries are the supply side (Package Registry / Artifact Repository leaves); the dependency manager consumes them as configured sources.
- **"Multi-ecosystem scope is definitional"** — rejected: manager lineage is single-ecosystem; multi-ecosystem is the update lineage's realization.

## Boundary Findings

1. **vs Build Automation System (§12 sibling, processed)** — seam confirmed from this side. The build tool answers "how does this project build" (project-resident build definition, dependency-ordered execution, artifact production); dependency management answers "what does this project depend on and which exact versions" (declaration, resolution, recorded selection, change loop). Overlap: Maven/Gradle/Bazel embed resolution engines; cargo/npm-class fuse both. Removal tests: remove the build definition/execution → still dependency management (Renovate/Dependabot build nothing); remove dependency selection → still build automation (Make/CMake-core per the build pass). Existence proof of separation holds in both directions. **Three-way statement for ecosystem-native tools (cargo/npm-class)**: they are one tool carrying two Types' functions; the atlas keeps the two leaves and documents the fused tool as the straddle case — center-of-gravity test: which managed problem is primary in the product's self-description and documentation weight (Cargo: "package manager" that also compiles; its resolver/lock/update docs are a peer chapter to its build docs). Joint review with the build pass's flag: this pass documents the dependency side; recommend the joint review be discharged when package-registry is processed (three-way statement recorded there).
2. **vs Package Registry (§12 sibling, unprocessed)** — client/project side vs server/venue side. The dependency manager consumes registries as configured supply sources (evidence: Bundler sources, Poetry repositories, Cargo registry, Renovate datasources, Dependabot registries); the registry hosts/publishes/serves packages per ecosystem protocol. Removal test: remove the project-side declaration/resolution → the registry remains a registry; remove the registry → the manager has no supply (but the manifest/lock records persist). Flag for joint review when package-registry is processed (together with the artifact-repository pass's pending Package Registry seam).
3. **vs Artifact Repository (§12 sibling, processed)** — consistent with its recorded seam: dependency management manages "which version" (declaration/selection/lock/update); the artifact repository custodies artifacts and satisfies declarations via proxy/upstream serving. No conflict found from this side.
4. **vs Software Composition Analysis / SCA (§15, unprocessed)** — selection/currency vs security/license analysis of the composition. Overlap zone: Dependabot alerts/security updates, Renovate vulnerability remediation, GitHub dependency graph, Bundler ecosystem CVE guides. Test: remove vulnerability/license analysis → still dependency management; remove selection/reconciliation/recorded selection → SCA. Record for the SCA pass.
5. **vs SBOM Management (§15, unprocessed)** — the recorded selection is a working project state consumed by builds; an SBOM is a compliance-oriented inventory record derived from (among other sources) such states. Different primary consumers and lifecycles. Record for the SBOM pass.
6. **vs Source Code Hosting Platform (§12)** — hosting platforms host the repos in which manifests/locks live and provide the PR/review surface the update lineage operates through; the dependency-management function (scan/select/propose) is distinct from hosting/collaboration. Dependabot is the platform-native embedding of the function, not a hosting feature.
7. **vs Patch Management (§14)** — machine/endpoint patching of installed software vs project-side dependency sets; different unit (device vs project), different actor (IT ops vs developers). No overlap found.
8. **System package managers (APT-class)** — adjacent domain: dependency resolution exists there too, but the unit is the machine-wide package store, not a project's dependency set of record; no project-resident declaration/lock. Excluded from the Type (canonical inference, not directly sampled).

## Historical / Market-Sample Check

- The three sampled manager-lineage products span 2009–2020s origins and three ecosystems; the update lineage spans platform-native and standalone forms. All satisfy the three L0 structures.
- **Maven-class build-embedded resolution (2002+)**: satisfies L0-1 (pom declaration) and L0-2 (transitive resolution + mediation) but holds the selection via deterministic re-resolution over a persistent local cache rather than a project-resident lock record — a weaker realization of L0-3. Reasoned from the build-automation pass's evidence (Maven/Gradle embedded engines, Gradle locking); not re-fetched this pass. The definition is phrased (recorded selection "or deterministic re-resolution equivalent") so this lineage fits without making the lockfile definitional.
- **CPAN-era (1995+) and APT-class system managers**: early dependency resolution exists, but the project-resident declaration-of-record + recorded-selection structure is absent or partial (installer-centric / machine-centric units). Treated as precursors/adjacent domain. Canonical inference from well-known lineage shape; not fetched — marked uncertain.
- **npm-class (2010+)**: manifest+lock+resolver+update fits the core (expected; not sampled this pass — recorded as a gap).
- Conclusion: the definition does not over-fit to the modern lockfile era; the lockfile is named as the modern implementation of the recorded-selection invariant, with the deterministic-re-resolution realization keeping older build-embedded products inside the Type's orbit.

## Uncertainties

1. Maven/Gradle not directly sampled this pass; their embedded-resolution realization relies on the build pass's evidence plus structural reasoning. Maven's exact current lockfile posture (Maven 4 changes) unverified.
2. Historical lineage (CPAN, APT, early Maven) reasoned conceptually; no period sources fetched.
3. npm/yarn/pnpm, Composer, CocoaPods, Go modules, pip-tools expected to fit the core but unverified this pass.
4. Renovate configuration-options reference and Dependabot options reference not fetched (large pages); config-shape observations come from concept/how-to pages. Exact numeric defaults (e.g., open-pull-requests-limit defaults) deliberately not asserted.
5. Bundler caching/vendoring and Cargo source-replacement pages observed via nav/links only, not fetched.
6. Whether the market will keep framing dependency currency under "supply-chain security" (GitHub's current taxonomy) — a framing drift worth re-checking when SCA is processed.

## Final Synthesis

A Dependency Management Application is the project-side application that holds a software project's dependency set as managed state — a declaration of the components it depends on (name + version constraint), a resolution of that declaration into one concrete, coherent selection of versions including transitive dependencies, and that selection held as durable project state — and operates the loop that keeps the set coherent and current: deliberate changes re-run resolution and move the records forward; the recorded selection makes every machine, teammate, deploy, and CI run on the same versions.

The market realizes this core in two lineages: the per-ecosystem dependency manager (CLI + manifest + lockfile + install; Bundler/Cargo/Poetry class) and the cross-ecosystem automated update application (scan → look up → propose recorded-selection changes as reviewable PRs; Renovate/Dependabot class). Ecosystem-native build tools (cargo/npm-class) fuse this core with build automation and are documented as the straddle case. The Type is bounded by: build automation (how it builds vs what it depends on), package registries/artifact repositories (supply/custody vs selection), SCA/SBOM (security/compliance analysis of the composition vs the working selection), and source hosting (the venue where the records live and where proposed changes are reviewed).
