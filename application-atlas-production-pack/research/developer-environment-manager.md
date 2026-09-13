# Research Notes — Developer Environment Manager

## Research Goal

Understand what a "Developer Environment Manager" actually is as an Application Type: what software in this market does, what its core objects and workflows are, and where its boundaries lie against neighboring Types (Dev Container / Workspace Platform, Dependency Management, Package Registry, Configuration Management, Project Scaffolding).

## Initial Boundary

Working hypothesis before research:

- Core use: a developer (or a team) needs the correct toolchains/runtimes/packages/env-vars available in a project directory, reproducibly, without polluting the machine or conflicting across projects.
- Likely core objects: project, environment definition file, tool/package versions, shell activation, env vars, (optionally) services.
- Nearest neighbors: Dev Container / Workspace Platform (environment hosted in a container/cloud), Dependency Management Application (language-level libraries), Configuration Management (fleet/IT scale), Project Scaffolding (one-time creation).
- Unknowns: is this Type really distinct from "version manager" (asdf/mise class)? Is VM-based (Vagrant) in-type or a different Type? Is machine-level bootstrap (dotfiles, OS packages) in scope?

## Research Questions

1. What is the unit of record — the project, the machine, or the environment?
2. How is the environment specified (declarative file? version list? VM image?) and shared?
3. Who installs the software — the manager or the developer? Into what isolation?
4. How does the environment take effect (shell activation, shims, VM up, container exec)?
5. What lifecycle exists (install → activate → update → remove → reproduce elsewhere)?
6. What is common-but-not-definitional: services, tasks, secrets, dotfiles, CI usage, container output?
7. Where is the boundary vs Dev Container / Workspace Platform and vs Dependency Management?

## Representative Products

Selected for market representativeness, documentation quality, and distinct product philosophies:

| Product | Philosophy / pole | Evidence layer |
|---|---|---|
| Devbox (Jetify) | declarative per-project env, OS-level packages, Nix-backed, container output optional | A |
| mise | polyglot runtime/tool version manager + env vars + tasks + machine bootstrap, single CLI | A |
| devenv (Cachix) | Nix-native "whole environment declared": languages, services, processes, tasks, secrets | A |
| Vagrant (HashiCorp) | VM-image-based environment definition and lifecycle (historical/philosophy pole) | A |
| asdf | minimal plugin-based runtime version manager (older, simpler pole; historical check) | A |

## Sources

- Devbox docs — https://www.jetify.com/devbox/docs/ (fetched 2026-09-10)
- mise docs — https://mise.jdx.dev/ (fetched 2026-09-10)
- devenv docs — https://devenv.sh/ (fetched 2026-09-10)
- Vagrant intro — https://developer.hashicorp.com/vagrant/intro (fetched 2026-09-10)
- asdf — https://asdf-vm.com/ (fetched 2026-09-10)

All fetches succeeded (Tier 1 official documentation). No source-access limitation.

## Product Observations

### Devbox (Jetify) — Key observations

- "A command-line tool that lets you easily create isolated shells for development. You start by defining the list of packages required for your project, and Devbox creates an isolated, reproducible environment with those packages installed." (A)
- Definition lives in a `devbox.json` file in the project; "Declare the list of tools needed by your project via a devbox.json file and run devbox shell. Everyone working on the project gets a shell environment with the exact same version of those tools." (A)
- Manages OS-level packages ("the sort of thing you would normally install with brew or apt-get"), positioned as "similar to a package manager like yarn – except the packages it manages are at the operating-system level". (A)
- Isolation: environments "isolated from everything else in your laptop"; try/remove tools "while keeping your laptop pristine"; conflicting versions of the same binary per project. (A)
- Activation: `devbox shell` enters the environment. (A)
- Portability: one definition usable as local shell, devcontainer, Dockerfile, or cloud dev environment. (A)

### mise — Key observations

- "Declare your tool versions, environment variables, and commands in mise.toml. Use them in your shell, editor, and CI." (A)
- Per-project tool versions: `[tools] node = "24" ...`; `mise use node@24` installs and saves the version request in `mise.toml`. (A)
- Directory-driven activation: "Activate mise in your shell once. From then on, entering a project puts its installed tool versions on your PATH and loads its environment variables. Leave the project and mise restores the environment for your new directory." Shell hooks for bash/zsh/fish/etc., shims for editors/scripts, `mise exec` for Docker/CI. (A)
- Env vars: "Per-project env vars from mise.toml, .env files, secrets, and shell commands. Set when you enter, gone when you leave." (A)
- Multiple versions of the same tool across projects (node 22 in one dir, 24 in another). (A)
- Registry of 1000+ tools sourced from multiple backends (aqua, GitHub releases, cargo, npm, pipx, asdf plugins, etc.). (A)
- Beyond tools: tasks (`mise run`), machine bootstrap (`mise bootstrap`: OS packages via brew/apt/..., dotfiles, repos, services). (A)
- Backwards compatible with `.tool-versions` (asdf) and idiomatic version files (`.nvmrc`). (A)

### devenv (Cachix) — Key observations

- "Your whole development environment, declared. Define packages, languages, services, tasks, secrets, and tooling once. Give every developer and CI the same fast, reproducible environment." (A)
- Config in `devenv.nix` (Nix); activation via `devenv shell`; auto-activate on `cd`. (A)
- Services as first-class: 42 preconfigured services (PostgreSQL, Redis, MySQL, RabbitMQ, MinIO, ...), e.g. `services.postgres.enable = true`. (A)
- Processes: declarative process management with logs, restarts, dependencies; `devenv up` starts the whole stack. (A)
- Tasks & git hooks; secrets via SecretSpec (Keychain/1Password/dotenv sources); containers output ("Build OCI containers from your dev environment. Same packages, same versions, same behavior."); profiles (backend/frontend/fullstack); monorepo composition via imports. (A)
- Built on Nix; evaluation caching for fast shell startup. (A)

### Vagrant (HashiCorp) — Key observations

- "A tool for building complete development environments... Vagrant lowers development environment setup time, increases development/production parity, and makes the 'it works on my machine' excuse a relic of the past." (A)
- "building and managing virtual machine environments in a single workflow"; machines provisioned on VirtualBox/VMware/AWS/other providers; provisioning via shell scripts, Chef, Puppet. (A)
- Definition in a single `Vagrantfile`; "you just need to `vagrant up` and everything is installed and configured"; team members "create their development environments from the same configuration... all your team members are running code in the same environment". (A)
- Disposable, consistent, portable environment; isolation is a full VM. (A)
- Positioned for developers, operators, designers — the "everyone gets the same env" promise. (A)

### asdf — Key observations

- "The Multiple Runtime Version Manager. Manage all your runtime versions with one tool!" (A)
- Plugins per runtime; single config file `.tool-versions` "to manage all your tools, runtimes and their versions in a single, sharable place". (A)
- Shell support (Bash/ZSH/Fish) with shims; GitHub Action for CI. (A)
- No services, no tasks, no env-var layer, no machine bootstrap — the minimal pole of the Type. (A)

## Cross-product Comparison

| Dimension | Devbox | mise | devenv | Vagrant | asdf |
|---|---|---|---|---|---|
| Unit of record | project (`devbox.json`) | project (`mise.toml`) + machine config | project (`devenv.nix`) | project (`Vagrantfile`) | project (`.tool-versions`) |
| What is declared | OS-level packages | tool versions, env vars, tasks, bootstrap | packages, languages, services, processes, tasks, secrets | VM image + provisioning | runtime versions |
| Who installs | Devbox (Nix-backed) | mise (multi-backend) | devenv/Nix | provider + provisioners | asdf plugins |
| Isolation form | isolated shell env | per-project PATH selection, shared installs | Nix isolation | full VM | shims, per-project versions |
| Activation | `devbox shell` | shell hook / shims / `mise exec` | `devenv shell`, auto on cd | `vagrant up` + ssh | shims |
| Env vars | (via shell) | first-class | first-class | via provisioning | no |
| Services | no (container path instead) | via bootstrap | first-class (42 services, process supervisor) | via provisioning | no |
| Tasks | no | first-class | first-class | no | no |
| Machine-level setup | no | `mise bootstrap` (OS packages, dotfiles) | no | no | no |
| Container/other output | devcontainer, Dockerfile, cloud | `mise exec` in Docker/CI | OCI containers, Nix derivation | cloud providers | GitHub Action |
| Exact-version pinning | yes | yes | yes (Nix) | box version | yes |

## Canonical Model (four abstraction levels)

### L0 — Defining Invariant

Three jointly-held structures:

1. **The per-project environment definition of record** — a persisted, shareable specification (config file committed with the project) declaring what the development environment contains: the tools/runtimes/packages — and optionally env vars, services — needed to work on that project. Remove → a global package manager (Homebrew) or personal dotfiles; the definition is what makes the environment shareable and reproducible.
2. **Managed assembly of the declared environment** — the application itself resolves, downloads/installs, and versions the declared software into an environment that is per-project and does not disturb the machine's global state (isolated shell, per-project PATH selection, Nix store, or VM). Remove → a manifest/README nobody applies, or manual global installs with version conflicts.
3. **Activation into the developer's working session** — the environment can be entered/exited so the declared tools and settings take effect in the developer's shell/session (PATH, env vars), typically automatically per directory. Remove → a lockfile or setup script with no runtime effect.

Jointly-held load-bearing: (1) alone = a config file; (2) without (1) = a global package manager; (3) without (1)+(2) = shell rc editing; (1)+(2) without (3) = an installer; (2)+(3) without (1) = ad-hoc per-machine setup.

### L1 — Common Mature Structure

- Exact version pinning / lock semantics
- Multiple simultaneous versions of the same tool across projects
- Shell integration: hooks, shims, auto-activation on directory change
- Global/default tool versions alongside per-project ones
- Shared package store/cache with deduplication
- Environment-variable management
- Use of the same definition in CI (actions/exec modes)
- Registry/backends of installable tools

### L2 — Variant / Optional Structure

- Isolation backend: Nix store (Devbox, devenv) vs downloaded binaries + shims (mise, asdf) vs full VM (Vagrant) vs container
- Scope extension: whole-machine bootstrap (OS packages, dotfiles, repos, services — mise bootstrap)
- Services & processes (devenv services/process supervisor; Vagrant provisioning)
- Tasks (mise, devenv), git hooks, secrets management, profiles, monorepo composition
- Output paths: devcontainer/Dockerfile/OCI generation (Devbox, devenv), cloud environments
- GUI/dashboard surfaces (absent in the sampled CLI-first products; some market products add them)

### L3 — Vendor-specific

- Devbox: devcontainer/Dockerfile/cloud-env generation from one definition
- devenv: SecretSpec, native process supervisor with ready probes/socket activation, evaluation caching numbers
- mise: multi-backend registry (aqua, cargo, pipx, ...), `mise bootstrap plan`, remote hosts over SSH
- Vagrant: provider/provisioner plugin systems, Vagrant Cloud box distribution

## Vendor-specific Findings

See L3 above; none promoted to the canonical core.

## Boundary Findings

- **vs Dev Container / Workspace Platform**: that Type hosts the working environment itself inside a container/cloud workspace as the developer's primary working surface (editor runs against/in it). A Developer Environment Manager assembles the environment on the developer's own machine around their existing shell and editor. Devbox's own docs mark the seam: it creates a local shell "without an extra-layer of virtualization" and only turns the definition into a container "when you're ready to ship" — container output is a downstream artifact, not the working surface. Test: remove the local-shell activation and make the container the place you work → Dev Container territory.
- **vs Dependency Management Application**: dependency management handles a language project's library dependencies (the packages the *code* imports); the environment manager handles the toolchain/runtime layer *beneath* that (the compilers, runtimes, CLIs needed to build and run). mise's own framing shows the layering: it manages `node`/`python` versions; the project's `package.json`/`requirements.txt` remain the language package manager's domain.
- **vs Package Registry**: a registry distributes packages; the environment manager consumes them and assembles a working environment. Devbox's self-description ("similar to a package manager like yarn – except the packages it manages are at the operating-system level") is the clearest evidence of the distinction.
- **vs Configuration Management (IT/infra)**: configuration management targets org machines/servers at fleet scale with privileged, admin-facing operations; the environment manager is developer-facing, per-project, unprivileged, and exists to make *development* reproducible. mise's bootstrap is the closest straddle (machine-level OS packages/dotfiles) but remains developer-workflow-scoped.
- **vs Project Scaffolding / Code Generator**: scaffolding creates a new project once; the environment manager maintains the environment continuously across the project's life and across machines.
- **Is Vagrant in-type?** Yes, as a backend-variant pole: it satisfies all three L0 legs (Vagrantfile = definition; provisioning = managed assembly; `vagrant up`/ssh = activation) with a VM isolation backend. Its decline relative to container/Nix approaches is a market shift, not a Type boundary.

## Historical / Market-Sample Check

asdf (plugin-era, no services/tasks/env layer) and Vagrant (2011-era, VM-based) both satisfy the three-part core. The core therefore does not overfit to the modern Nix/TOML/services era. Conversely, a bare version-file (`.nvmrc`) without a manager, or a setup script without per-project activation, does not constitute the Type.

## Uncertainties

- The exact market edge of this Type is fuzzy: some products drift toward machine-setup/dotfiles management (mise bootstrap) or toward workspace hosting (devenv Cloud). The canonical core stays at the per-project environment; heavy machine-management or hosted-workspace drift is recorded as variant drift, not core.
- GUI/dashboard-style "developer environment" products (e.g. OS-vendor developer settings hubs) were not sampled; they may be a separate surface variant. Not resolved here.
- Naming collision risk: "environment" is also used for env-var-only tools (direnv-class). Those handle only the env-var leg and lack managed tool assembly; treated as a thinner adjacent utility, not sampled.

## Final Synthesis

A Developer Environment Manager is the developer-facing application whose defining core is: a per-project, shareable environment definition of record + the application's own managed assembly of the declared versioned tools/packages into a per-project (isolated) environment + activation of that environment into the developer's working session. Everything else — pinning, shims, services, tasks, secrets, machine bootstrap, container/VM backends, CI modes — is common mature structure or variant, not definition.
