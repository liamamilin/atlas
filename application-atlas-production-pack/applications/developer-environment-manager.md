# Developer Environment Manager

## Overview

A **Developer Environment Manager** is a developer-facing tool that turns a project's required working environment — its toolchains, runtimes, command-line packages, and related settings — into a declared, shareable, reproducible unit that the tool itself assembles and activates on the developer's machine.

The problem it solves is the "works on my machine" gap: without such a tool, each developer installs tools globally by hand, versions conflict across projects, and a new machine or new teammate means hours of manual setup following stale wiki instructions.

The defining structure is small:

```text
Per-project environment definition (committed with the project)
└── Managed assembly of the declared tools/packages into a per-project environment
    └── Activation into the developer's working session (PATH, env vars)
```

Everything else commonly associated with the category — exact version pinning, shell hooks and shims, services like databases, task runners, secrets, machine-level bootstrap, container or VM backends — is widespread in current products but is not what makes the tool an environment manager. Older and simpler products (plugin-based version managers, VM-based environment builders) fit the same definition without any of the modern specifics.

When the environment stops being assembled on the developer's own machine and instead the container or cloud workspace *becomes* the place the developer works, the product is drifting toward a different Application Type (Dev Container / Workspace Platform).

## Users & Context

The primary user is a software developer working on one or more projects on their own machine (laptop or workstation), who needs the right versions of tools available in each project directory without breaking other projects or the system.

Typical situations:

- joining a project and needing its exact toolchain set up quickly
- switching between projects that require different versions of the same tool
- trying a new tool without polluting the machine
- sharing a team's setup so everyone (and CI) gets the same environment

Secondary users: team leads or platform engineers who author and maintain the environment definitions the team consumes; CI pipelines that apply the same definition headlessly.

The characteristic context is the terminal: these tools are almost universally CLI-first, wired into the developer's shell, with the project directory as the organizing unit.

## Core Model

### The Defining Core

```text
Per-project environment definition
└── Managed assembly of declared tools/packages (per-project, non-polluting)
    └── Activation into the developer's session
```

Three properties. If any one is removed, the product is no longer recognizable as an environment manager:

- **Per-project environment definition of record** — a persisted, shareable specification (a config file committed alongside the code) declaring what the environment contains: the tools, runtimes, and packages the project needs, and optionally environment variables and services. This file is what makes the environment reproducible and team-shareable. Without it, the tool is just a global package manager or a pile of personal dotfiles.
- **Managed assembly of the declared environment** — the tool itself resolves, downloads, installs, and versions the declared software into an environment belonging to that project, without disturbing the machine's global state or other projects' environments. Different projects can hold different versions of the same binary. Without this, the definition is a document nobody applies.
- **Activation into the working session** — the environment can be entered and exited so the declared tools and settings take effect in the developer's shell: the declared versions appear on `PATH`, declared environment variables are set. In mature products this happens automatically when the developer changes into the project directory, and is undone on leaving. Without this, the tool is an installer, not a living environment.

### Capabilities Shared by Mature Products

These are common in current products; they make the environment manager practical but do not define the Type:

- **Version pinning** — exact versions recorded so every machine gets the same ones.
- **Multiple simultaneous versions** — the same tool at different versions in different projects, coexisting on one machine.
- **Shell integration** — shell hooks, shims, or exec wrappers so editors, scripts, and CI (which never source the shell config) can also see the environment.
- **Global/default versions** — machine-wide fallback versions alongside per-project ones.
- **Shared package store** — a local cache/store where installed artifacts are deduplicated across projects.
- **Environment-variable management** — per-project variables loaded on entry and dropped on exit, sometimes sourced from `.env` files or secret stores.
- **CI usage** — the same definition applied in continuous integration via an exec mode or official action.
- **Tool registry/backends** — a catalog of installable tools, often sourced from multiple distribution channels.

### One Structure, Many Implementations

The core is conceptual; products realize each part differently:

```text
Concept:  Environment definition
Forms:    JSON/TOML config, Nix expression, version-list file, VM image + provisioning script

Concept:  Managed assembly
Forms:    Nix-store builds, downloaded binaries via multi-source backends, plugin-installed runtimes, VM provisioning

Concept:  Activation
Forms:    isolated subshell, shell hook + shims, auto-activation on cd, VM boot + ssh
```

A reader who has only seen one implementation (say, a Nix-backed declarative tool) should still recognize a plugin-based version manager or a VM-based environment builder as the same Type.

## How It Works

### Define the environment

```text
In the project directory
→ declare the tools/packages (and optionally env vars, services) the project needs
→ commit the definition file with the code
```

The definition is the single source of truth. Editing it and re-applying is the normal way the environment changes.

### Assemble the environment

```text
Run the install/apply command
→ the tool resolves the declared tools (from its registry/backends or package sources)
→ downloads and installs them into its managed store
→ the project's environment is ready, isolated from global state
```

Installation is idempotent: re-running converges the machine to the declared state. Artifacts are typically cached and shared across projects.

### Activate and work

```text
Enter the environment (explicit command, or automatically on cd into the project)
→ declared tool versions are on PATH; declared env vars are set
→ develop, build, test with the project's tools
→ leave the directory; the environment is restored for the new location
```

This enter/exit loop is the daily interaction. The developer's own shell and editor stay in place; only the environment around them changes.

### Reproduce elsewhere

```text
Clone the project on a new machine or in CI
→ apply the same definition
→ the same environment is assembled
```

This is the payoff of the definition-of-record: teammates and CI get identical environments without manual steps.

### Core vs Common vs Optional

**Defining core** — without these, not an environment manager:

- per-project shareable environment definition
- managed assembly of the declared tools/packages
- activation into the working session

**Common mature structure** — present in most modern products:

- version pinning, multi-version coexistence
- shell hooks / shims / exec modes
- env-var management
- shared store/cache
- CI application of the same definition
- tool registry

**Variant / optional** — depends on product philosophy and segment:

- isolation backend: Nix store, downloaded binaries, full VM, container
- services (databases, queues) and process supervision
- task running, git hooks
- secrets integration
- whole-machine bootstrap (OS packages, dotfiles)
- output paths: devcontainer/Dockerfile/OCI image generation, cloud environments

## Interfaces

These tools are CLI-first. The main surfaces, described conceptually:

### Definition file

The project's environment spec, edited by hand and committed with the code.

- typical content: tool names and versions, env vars, optionally services/tasks
- primary actions: add/remove/change a declaration, then re-apply

### Command line

The tool's verbs, roughly:

- install/apply — assemble the declared environment
- shell/activate — enter the environment
- list/current — show installed and active tools and their sources
- use/add — add a tool and record it in the definition in one step
- exec/run — run a command inside the environment (used by editors, scripts, CI)

### Shell integration

The invisible surface: a hook or shim layer wired into the shell so that directory changes activate the right environment automatically, and so non-shell consumers (editors, scripts) resolve the same tools.

### Status / listing output

A view of what is installed, at which versions, and which config file requested them — the developer's way of answering "why is this version of this tool active here?"

## Important Rules / Behaviors

### The definition file is the source of truth

Changing the environment means changing the declaration and re-applying — not hand-installing into the environment. Hand-installed state is exactly what the tool exists to prevent.

### Environments are per-project and non-interfering

Two projects can pin different versions of the same tool; entering one directory and then the other switches versions. The machine's global tools are not modified by project environments.

### Activation is scoped and reversible

The environment's effects (PATH, env vars) apply inside the activated session or directory and are undone on exit. Nothing leaks permanently into the shell.

### Assembly is convergent

Re-running installation converges the machine to the declared state; the same definition yields the same environment on different machines. Exact-reproducibility guarantees vary by backend (a fully pinned Nix-style definition is stricter than a floating version request) — the guarantee strength is a variant, not a constant.

### The developer's own tooling stays primary

The environment manager wraps the developer's existing shell, editor, and workflow; it does not replace them. This is the structural contrast with workspace-hosting products, where the hosted container replaces the local setup.

## Variants

- **Declarative Nix-backed managers** — whole-environment definitions built on a content-addressed package store; strongest reproducibility; often add services, processes, tasks, container output.
- **Polyglot version managers** — lightweight per-project tool-version selection via shims/hooks; broad tool registries; may grow env-var, task, and machine-bootstrap layers.
- **VM-based environment builders** — the environment is a disposable virtual machine defined by a config file and provisioned by scripts; heavier isolation, historically the first mainstream form of the Type.
- **Machine-setup-oriented variants** — extend the per-project core toward whole-machine provisioning (OS packages, dotfiles, services); still anchored on the project environment.
- **Minimal version-file managers** — only the tool-version leg; no env vars, services, or tasks; the historical simple pole.

A variant remains a Variant unless it changes the core users, objects, or workflow so much that the core model no longer applies — e.g. when the hosted container becomes the working surface itself.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Dev Container / Workspace Platform | the container/cloud workspace *is* the developer's working surface (editor runs in/against it); an environment manager assembles the environment on the developer's own machine around their existing shell and editor — container output from a definition is a downstream artifact, not the workspace |
| Dependency Management Application | manages a language project's library dependencies (what the code imports); the environment manager manages the toolchain/runtime layer beneath that (compilers, runtimes, CLIs) |
| Package Registry | distributes packages; the environment manager consumes them and assembles a working environment |
| Configuration Management | admin-facing, fleet-scale provisioning of org machines/servers; the environment manager is developer-facing, per-project, unprivileged |
| Project Scaffolding / Code Generator | creates a new project once; the environment manager maintains the environment continuously across the project's life and machines |
| Version Control System | shares the definition file as part of the repo, but does not assemble or activate environments |

The boundary with Dev Container / Workspace Platform is the most important one, because both promise "the same environment for everyone". The structural difference is where the environment lives and what the developer works *in*: local machine + own shell (environment manager) vs hosted container/workspace as the working surface (workspace platform).

## Representative Products

- Devbox (Jetify) — declarative per-project environments, Nix-backed, with container/cloud output paths
- mise — polyglot tool-version manager with env vars, tasks, and machine bootstrap
- devenv (Cachix) — Nix-native whole-environment declaration with services and processes
- Vagrant (HashiCorp) — VM-based environment definition and provisioning; the historical heavyweight pole
- asdf — plugin-based runtime version manager; the minimal pole

The core model was checked against the older/simpler poles (asdf, Vagrant) to avoid over-fitting the definition to the current Nix/TOML generation of tools.

## Sources

Research date: **2026-09-10**

- Devbox documentation — https://www.jetify.com/devbox/docs/
- mise documentation — https://mise.jdx.dev/
- devenv documentation — https://devenv.sh/
- Vagrant introduction — https://developer.hashicorp.com/vagrant/intro
- asdf — https://asdf-vm.com/

All sources are official product documentation, fetched successfully on the research date. Precise operational details (exact version-resolution rules, cache layouts, backend lists, performance figures) are intentionally not stated in this document; they remain in the paired Research Notes.
