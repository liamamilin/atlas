# Dev Container / Workspace Platform

## Overview

A **Dev Container / Workspace Platform** turns a project's development environment into a shareable, machine-independent definition, provisions runnable and disposable environments from that definition, and lets developers enter those environments with the editing and terminal tools they already use.

The problem it solves is environmental, not editorial: assembling a working toolchain for a codebase by hand is slow, error-prone, and personal. Two developers on the same repository can end up running different runtime versions, missing native dependencies, and half-remembered setup steps; a new hire can spend hours untangling onboarding; a personal workstation accumulates conflicting toolchains across projects. The platform's answer is to treat the environment the way source control treats code: as a versioned record from which anyone can recreate the same working state, and to make that working state disposable — the durable assets, the code and the definition, live outside it.

The boundary that separates this Type from its neighbors: the **environment is the product, the editor is not**. The platform defines, builds, runs, and discards environments; the editing surface — desktop IDE, browser editor, terminal — remains the developer's own and attaches to the environment from outside. When the editing experience itself becomes the hosted product, the software is a Cloud IDE; when the environment is the developer's own machine being curated in place, it is developer-environment management rather than workspace provisioning.

## Users & Context

**Primary users:**

- **Individual developer** — reproduces a project's environment on their own machine (or a machine they point at), so the project's toolchain never collides with their personal setup; also runs isolated copies of a repository to review a branch or pull request without touching local work.
- **Team members** — each provisions the same environment from the definition committed with the project, replacing "follow the setup README and hope" with a single provision action.

**Secondary users:**

- **Platform / infrastructure team (enterprise pole)** — authors and maintains the environment templates that workspaces are created from, enforces approved images and resource limits, and operates the platform on organization-controlled infrastructure.
- **New joiners and occasional contributors** — the onboarding audience the loop most directly serves: provision, work, delete.

Typical contexts: polyglot or dependency-heavy codebases where hand setup is genuinely painful; teams wanting identical local environments; security-conscious organizations that keep source code and credentials off laptops by running workspaces on controlled infrastructure; CI-adjacent reuse of the same definitions for testing.

## Core Model

The defining core is three structures held together. Remove any one and what remains is a different kind of software.

```text
Environment Definition (of record)
  │  machine-independent, shareable, versioned
  ▼
Provisioned Workspace Instance
  │  runnable, disposable, lifecycle-bound
  ▼  (developer's tools attach)
Attach Layer
     editor · terminal · debugger · browser
```

### The environment definition

A persistent, declarative description of one project's complete development environment: the runtime and language toolchain, dependencies and system packages, project-specific tool and editor configuration, how the application's ports surface, and sometimes the compute the environment needs. It is written once and exists independently of any machine and any person — that independence is what makes the environment reproducible for everyone else. It lives alongside or near the project it describes, or in a platform-team-managed catalog in enterprise settings.

The definition is the artifact developers actually author and review. Formats vary — a container-image-and-tools manifest is the current dominant pattern, but infrastructure-definition languages and older single-file formats serve the same role — so the concept, not the file format, is what defines the Type.

### The workspace (environment instance)

The running thing the platform creates from the definition: a working environment that holds the project's source code together with the toolchain needed to edit, build, run, and debug it. One project can have several instances; an instance typically belongs to one developer. It has a real lifecycle:

```text
create / build  →  start  →  (work)  →  stop  →  start ...
      │                                              │
      └── rebuild (apply definition changes)         └── delete
```

The workspace is disposable by design. Stopping it preserves its state; rebuilding it recreates it from the definition; deleting it loses nothing that matters, because durable assets — the code and the definition — live outside it.

The substrate underneath is an implementation choice: a container, a virtual machine, a pod or cloud machine. Where the workspace runs is equally an implementation choice — the developer's own machine, a remote machine they control, organization-operated infrastructure, or vendor-hosted cloud compute.

### The attach layer

The developer's ordinary tools connect into the environment and work against it: an editor extension that opens a window "inside" the workspace, an SSH or terminal session, a browser-based editor, or a CLI exec. Execution — builds, tests, the application process, the debugger target — happens in the environment; the editing and personal tooling stay on the client side. Because attachment is decoupled, the same workspace can be reached from different clients, and the same client can switch between entirely different environments — changing the toolchain by reconnecting rather than by reinstalling anything locally.

For the application being developed to be reachable, the platform surfaces its ports from the environment to the client (port forwarding or publication), so the developer opens the running app in a local browser as if it ran on the laptop.

### One structure, many implementations

```text
Concept:   Environment definition
Common implementations:  container manifest (devcontainer.json),
                         infrastructure template (Terraform),
                         single-file VM definition (Vagrantfile — historical),
                         container image + compose files

Concept:   Workspace substrate
Common implementations:  container, virtual machine, Kubernetes pod, cloud instance

Concept:   Hosting locus
Common implementations:  local container runtime, remote machine via SSH,
                         self-hosted organization platform, vendor-hosted service

Concept:   Attach client
Common implementations:  editor extension, SSH/terminal session, browser IDE, CLI
```

A reader who has only seen one shape — say, a dev container running in local Docker opened through a desktop editor — should still be able to recognize a Terraform-defined cloud workspace or a VM-based historical tool as the same Type from this model.

### Standard capabilities

Mature products commonly add, without these defining the Type:

- **Setup automation** — ordered setup hooks that run when the environment is created (install dependencies, prepare content), before or after the developer first attaches.
- **Fast start** — pre-built images, prebuilds, or ready-made template catalogs so creating a workspace takes moments rather than a full build.
- **Idle handling** — automatic stop of unused workspaces to save compute cost, with quick restart.
- **Personalization** — dotfiles repositories, editor settings, and credential sync applied at attach time, on top of the project-defined environment.
- **Sharing ecosystems** — reusable installable units (features) and whole-environment templates, published and shared across projects and organizations.
- **Governance (enterprise pole)** — admin-managed templates enforcing approved images and resource policies, quotas, SSO, and audit.
- **Headless reuse** — the same definitions consumed by CI systems for build and test.

## How It Works

### 1. Define

```text
Author or adopt an environment definition for the project
→ (pick a starting template, or wrap an existing image/Dockerfile/compose file)
→ commit it with the code (common pattern)
```

The definition becomes part of the project. Editing it is ordinary code review — a changed toolchain requirement is a diff.

### 2. Provision

```text
Create a workspace from the definition
→ platform builds or pulls the environment image
→ starts the environment with the project's source mounted, cloned, or copied in
→ runs setup hooks (dependencies, content preparation)
→ workspace ready to enter
```

On large projects this step is commonly accelerated by prebuilds — the expensive part has been done in advance and cached. If the build fails, some products surface the creation log and offer a recovery path rather than leaving a broken environment.

### 3. Attach and work

```text
Open the workspace from the editor (or terminal, or browser)
→ editor extension connects into the environment
→ terminal, builds, tests, and debugging all execute inside it
→ application ports forwarded to the client
→ personalization (dotfiles, settings, credentials) applied on attach
```

From here the experience is designed to feel like local development — full editor functionality regardless of where the code and tools physically run. Switching projects can mean switching entire toolchains, simply by opening a different workspace.

### 4. Maintain

```text
Stop the workspace when done (or automatically when idle)
→ restart later with state intact
→ rebuild when the definition changes
→ delete when the work is finished
```

### 5. Share

Teammates provision their own instances from the same definition — identical environments without communication. In enterprise deployments, platform teams govern what can be provisioned by publishing maintained templates and constraining the rest. Teams get onboarding for free: the setup the first developer encoded is the setup everyone gets.

## Interfaces

### Environment definition files

The primary authoring surface, edited like any other project file.

- Typical content: base image or machine reference, tool/package installation, editor/tool customization, forwarded ports, setup commands, resource requirements
- Primary actions: create (from template or from scratch), edit, commit, review

### Workspace list / dashboard

The management surface — as a desktop app, web dashboard, or CLI.

- Typical information: workspace name, project/repository, running or stopped state, where it runs, age
- Primary actions: create, open/connect, stop, rebuild, delete

### Attached editor session

The working surface — the developer's editor bound to the environment.

- Typical information: the project's files and code; an integrated terminal that runs inside the environment; forwarded-ports panel; environment status indicator
- Primary actions: edit, run and debug, execute commands in the environment, open forwarded application URLs

### Build and lifecycle logs

Provisioning visibility.

- Typical information: build progress, setup-hook output, errors with recovery options
- Primary actions: retry, open a recovery environment to fix a failed definition, rebuild

### Admin console (enterprise deployments)

Governance surface for platform teams.

- Typical information: templates and their versions, workspace usage, resource consumption, users and groups
- Primary actions: publish/update templates, set resource limits and approved images, manage access

## Important Rules / Behaviors

### The definition is the source of truth

Local, hand-made changes to a workspace are conveniences, not records. When the definition changes, the workspace is rebuilt from it — environments conform to the record, never the reverse. This asymmetry is what keeps a team's environments identical.

### Stop, rebuild, and delete do different things

Stopping preserves workspace state for later restart. Rebuilding recreates the environment to apply definition changes; what survives a rebuild (rather than being re-provisioned) varies by product. Deleting destroys the environment — including any uncommitted work inside it; the durable assets are the code in version control and the definition. Developers are expected to delete and recreate routinely, which makes committing work early a practical necessity.

### The editing surface is decoupled from the environment

The same workspace accepts different clients, and the same client attaches to different workspaces — including environments on entirely different machines. Toolchain changes happen by reconnecting, not by reinstalling on the workstation.

### Setup runs in order and can fail

Creation-time setup hooks run in a defined order, and a failure halts subsequent steps — a broken definition produces a visible, diagnosable failure (with recovery paths in mature products), not a silently half-configured environment.

### The running application is reachable only through surfaced ports

Services inside the environment must be forwarded or published to be opened from the client side. The platform mediates this, which also lets it mediate who else can reach a running application.

### Declared requirements gate provisioning

When a definition declares compute needs (memory, CPU, storage, GPU), the platform uses them — to select an appropriately sized machine where compute is offered, or to warn when the host cannot satisfy them.

### Executable definitions are a trust surface

An environment definition is runnable code from the repository it describes. Some products treat attaching or provisioning from an unfamiliar definition as an explicit trust decision requiring user confirmation.

## Variants

- **Local-first editor extension** — the environment runs in a container runtime on the developer's own machine; the desktop editor attaches into it. The oldest mainstream shape and a common individual pattern.
- **Provider-pluggable CLI / open-source tool** — one definition format, many backends: the same workspace recipe can run locally, on a spare remote machine, on any cloud, or on a cluster; switching backends is a command-line choice, not a migration.
- **Self-hosted organization platform** — the organization operates the platform on its own infrastructure; platform teams own the templates that workspaces are created from, with governance (approved images, resource limits, SSO) as a first-class concern.
- **Vendor-hosted SaaS** — workspaces run on the vendor's cloud, created directly from a repository; machine sizing, quotas, and retention are handled by the service. This shape blends toward Cloud IDE depending on how fused the editing experience is (see Related Application Types).
- **VM-based (historical lineage)** — the same define → provision → attach loop over virtual machines instead of containers; the direct ancestor of the modern container-based forms.
- **Agent substrate (current market layer)** — AI coding agents running in the same provisioned workspaces developers use, sharing the infrastructure and often the definitions; an emerging posture, not yet a definitional shift.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Cloud IDE | closest modern seam | A Cloud IDE hosts the remote compute and delivers the editing-and-execution experience as a fused service; a dev-container/workspace platform defines and provisions environments that may run anywhere — including the developer's own machine — and is consumed through whatever editor the developer already uses. Hosted repo-attached products can genuinely sit on both sides of this line; the working test is where the editing surface lives: pluggable client (this Type) vs delivered product (Cloud IDE). |
| Developer Environment Manager | sibling | Curates the developer's own machine — toolchain versions, settings, project-local runtimes managed in place — where machine state is the thing managed. This Type provisions self-contained, disposable environments separate from the machine. Boundary pending joint review. |
| Integrated Development Environment / Code Editor | attach client | The IDE is one of the clients that attaches into workspaces. It does not define, provision, or lifecycle environments; the platform does. |
| Infrastructure-as-Code Platform | provisioner overlap | IaC's object of record is infrastructure; here IaC may serve as the mechanism that creates workspaces, but the output only becomes this Type when it is a developer-enterable environment with tools attached. |
| Container Management / Kubernetes Management Platform | substrate overlap | Both may run containers, but container management operates shared fleet services with health and scaling as working objects; here environments are single-developer-scale, disposable, and organized around the definition-plus-attach loop. |
| Project Scaffolding / Code Generator | adjacent creation tool | Scaffolding generates a codebase once; this Type provisions the working environment for a project — usually an existing one — continuously. |
| Internal Developer Platform | enterprise overlap | An IDP offers org-wide self-service across many service kinds; this Type is specifically scoped to development environments. Platform-team administration exists in both, which can make enterprise deployments resemble each other. |
| Continuous Integration Platform | consumer relationship | CI consumes these environment definitions headlessly for builds and tests; it does not provide the interactive developer workspace. |

## Representative Products

- Visual Studio Code Dev Containers — local-first editor-extension pattern; co-originator of the dev container specification
- DevPod — open-source, client-only tool with pluggable providers; one definition, many backends
- Coder — self-hosted enterprise platform; Terraform-defined workspaces on operator-controlled infrastructure
- GitHub Codespaces — vendor-hosted, repository-attached workspaces; the hosted pole of the configuration-as-code pattern

The defining core was checked against a historical non-container sample (Vagrant's VM-based workflow) and against the open development-container specification, to avoid defining the Type by today's dominant container-and-manifest implementation.

## Sources

Research date: **2026-09-08**

- Development Container Specification — https://containers.dev/
- Dev Container metadata reference — https://containers.dev/implementors/json_reference/
- VS Code Dev Containers documentation — https://code.visualstudio.com/docs/devcontainers/containers
- DevPod documentation — https://devpod.sh/docs/what-is-devpod , https://devpod.sh/docs/developing-in-workspaces/what-are-workspaces
- Coder documentation (About) — https://coder.com/docs
- GitHub Codespaces documentation — https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces
- Vagrant introduction — https://www.vagrantup.com/intro

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and boundary analysis (including the relationship with Cloud IDE and the pending Developer Environment Manager seam) are recorded in the paired Research Notes.
