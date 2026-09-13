# Research Notes — Dev Container / Workspace Platform

Research date: **2026-09-08**

## Research Goal

Understand what a "Dev Container / Workspace Platform" actually is as an Application Type: what the core objects are (environment definition, workspace/environment instance, attach client), how the define → provision → attach → maintain loop works, what is definitional vs merely common in today's market, and where the boundaries sit against Cloud IDE, Developer Environment Manager (unprocessed sibling leaf), IaC/configuration management, container management, project scaffolding, and internal developer portals.

This pass also owes a boundary answer to the earlier cloud-ide pass, which recorded: "a dev-container/workspace platform defines, shares, and provisions environments that may run on the developer's own machine and be consumed through any local editor, while a Cloud IDE hosts and lifecycle-manages the remote compute and delivers the editing+execution experience as a service" (research/cloud-ide.md, Boundary Findings) and recommended joint review from this side.

## Initial Boundary (hypothesis before research)

- Core hypothesis: the Type is about **environment provisioning, not editing**. The product defines a complete development environment as a shareable record, creates a runnable environment from it, and lets the developer's ordinary tools attach to it. The editing surface is external and pluggable.
- Nearest neighbors suspected: Cloud IDE (§12, processed — sharpest seam), Developer Environment Manager (§12, unprocessed sibling), Integrated Development Environment / IDE and Code Editor (the attach clients), Infrastructure-as-Code Platform, Configuration Management, Container Management / Kubernetes Management, Project Scaffolding / Code Generator, Internal Developer Platform / IDP, Continuous Integration Platform (headless reuse of the same definitions).
- Known risks: (1) the seam vs Cloud IDE is thin at the mechanism level (same devcontainer/devfile substrate; Codespaces is arguably a member of both); (2) "Developer Environment Manager" is unprocessed and may collide; (3) the market may have drifted so that hosted products (Codespaces-class) dominate the label while the leaf name suggests local dev containers.

## Research Questions

1. What is the environment definition — what does it describe, where does it live, what formats exist?
2. What is the provisioned unit (workspace / codespace / environment) and what does it bind (code, toolchain, runtime, personalization)?
3. Where can the environment run (local Docker, remote machine, org infrastructure, vendor cloud) — and is remote/cloud definitional?
4. How does the developer attach (editor extension, SSH/terminal, browser IDE, CLI) — and is any particular client definitional?
5. What lifecycle does the environment have (create → start/stop → rebuild → delete) and what survives each transition?
6. What automates the loop: setup hooks, prebuilds, auto-stop, dotfiles, port forwarding, credential sync?
7. How is the definition shared and reused (repo-committed config, features/templates ecosystems, admin-managed template registries)?
8. What governance exists at the enterprise pole (templates, quotas, approved images, SSO/RBAC, audit)?
9. What do the products themselves say they are *not* (boundary evidence)?
10. Would older / differently-positioned products (VM-era dev environments, e.g. Vagrant) still fit the definition?

## Representative Products

Selected for market spread, documentation quality, product-philosophy diversity and customer-tier diversity:

| Product | Why sampled | Docs tier reached |
|---|---|---|
| Visual Studio Code Dev Containers | Local-machine pole; editor-extension posture; co-originator of the dev container spec | Tier 1 (code.visualstudio.com Dev Containers docs) |
| DevPod (Loft Labs) | Open-source, client-only, provider-pluggable pole; "dev containers everywhere" philosophy | Tier 1 (devpod.sh docs: what-is-devpod, what-are-workspaces) |
| Coder | Self-hosted enterprise platform pole; Terraform-defined workspaces; explicit "what Coder is not" boundary statements | Tier 1 (coder.com/docs About page) |
| GitHub Codespaces | Vendor-hosted SaaS pole; repo-attached configuration-as-code; sampled from the definition/provisioning angle (its hosted-editor angle was sampled in the cloud-ide pass) | Tier 1 (docs.github.com what-are-codespaces) |
| Vagrant (HashiCorp) | Historical / market-sample check: VM-era (2013+) dev-environment tooling, non-container substrate | Tier 1 (vagrantup.com intro) |
| Development Container Specification (containers.dev) | Spec-level anchor: defines the shared vocabulary and what supporting tools do | Tier 1 (containers.dev root, json_reference) |

## Sources

- Development Container Specification — https://containers.dev/ (fetched 2026-09-08)
- Dev Container metadata reference (devcontainer.json) — https://containers.dev/implementors/json_reference/ (fetched 2026-09-08)
- VS Code Dev Containers — https://code.visualstudio.com/docs/devcontainers/containers (fetched 2026-09-08)
- DevPod — https://devpod.sh/docs/what-is-devpod and https://devpod.sh/docs/developing-in-workspaces/what-are-workspaces (fetched 2026-09-08)
- Coder — https://coder.com/docs (About; fetched 2026-09-08)
- GitHub Codespaces — https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces (fetched 2026-09-08)
- Vagrant — https://www.vagrantup.com/intro (fetched 2026-09-08)
- Prior-pass evidence: research/cloud-ide.md (Codespaces org governance, prebuilds, idle timeout, port sharing observed 2026-09-07) — used as cross-pass evidence, marked where relied on.

Evidence layers used below: **A** = directly observed on the cited source for that product; **B** = cross-product commonality observed across the sample; **C** = canonical inference from comparison + boundary reasoning.

All fetches succeeded on first attempt; no source-access limitation applies to this pass. Sub-pages not fetched (e.g. DevPod prebuilds page, Coder templates admin docs, Codespaces prebuilds) mean details known only from navigation labels or prior-pass notes are treated as lower-confidence and kept out of the final document.

## Product Observations

### Development Container Specification (evidence A)

- "A development container allows you to use a container as a full-featured development environment. It can be used to run an application, to separate tools, libraries, or runtimes needed for working with a codebase, and to aid in continuous integration and testing. Dev containers can be run **locally or remotely**, in a private or public cloud, in a variety of **supporting tools and editors**."
- The spec "enrich[es] existing formats with common development specific settings, tools, and configuration while still providing a simplified, un-orchestrated single container option."
- Sharing/reuse is a first-class spec concern: **Features** ("quickly share and reuse container setup steps") and **Templates**.
- devcontainer.json reference: the file "contains any needed metadata and settings required to configure a development container for a given well-defined tool and runtime stack. It can be used by tools and services that support the dev container spec to create a **development environment** that contains one or more development containers."
- Definition content surface (observed property groups): image / Dockerfile / Docker Compose reference; Features; **lifecycle scripts** (initialize → onCreate → updateContent → postCreate → postStart → postAttach, with documented order and "if one of the lifecycle scripts fails, any subsequent scripts will not be executed"); forwardPorts + port attributes; container/remote env vars; remoteUser/containerUser; mounts; runArgs; **hostRequirements** (cpus/memory/storage/gpu — "Cloud services can use these properties to automatically default to the best compute option available, while in other cases … a warning"); `customizations` explicitly marked "Product specific properties, defined in supporting tools".
- Scope statement: "The focus of `devcontainer.json` is to describe how to enrich a container **for the purposes of development** rather than acting as a multi-container orchestrator format. Instead, container orchestrator formats can be referenced when needed."
- Prebuild metadata can be stored in a container image label (`devcontainer.metadata`) and is auto-merged at creation.

### Visual Studio Code Dev Containers (evidence A)

- "The Dev Containers extension lets you use a container as a full-featured development environment. It allows you to open any folder inside (or mounted into) a container… A devcontainer.json file in your project tells VS Code how to access (or create) a development container with a well-defined tool and runtime stack."
- "Workspace files are mounted from the local file system or copied or cloned into the container. Extensions are installed and run inside the container… you can seamlessly switch your entire development environment just by connecting to a different container."
- "Local-quality development experience … regardless of where your tools (or code) are located."
- Two operating models: container as full-time dev environment; attach to a running container to inspect it.
- Host flexibility: Docker locally, Docker on a remote environment (via Remote-SSH or Remote-Tunnels — "You do not even need to have a Docker client installed locally"), other Docker-compliant CLIs, or attach to a Kubernetes cluster with kubectl.
- Creation flows: Open Folder in Container; Add Dev Container Configuration Files (pick a Template from a filterable list, or reuse an existing Dockerfile / Docker Compose file); Clone Repository (or GitHub PR) in Container Volume (isolated volume; PR auto-checkout); Reopen in Container; Rebuild Container to apply config changes.
- Failure path: on build failure, "Reopen in Recovery Container" opens a minimal container with the creation log to fix the Dockerfile — evidence that failed provisioning is a designed-for state.
- Features: "self-contained, shareable units of installation code"; installable from a central index; publishable as OCI artifacts.
- Pre-building images recommended ("faster container startup… pin to a specific version"); pre-built images can carry dev container metadata labels; CI integration via dev container CLI / GitHub Actions.
- Port forwarding: `forwardPorts` in the definition; temporary per-session forwarding; publishing vs forwarding distinction (from Docker semantics).
- Terminal: any terminal opened in the window "will automatically run in the container"; debugging attaches to the app in the container; `code` CLI usable inside.
- Extensions run inside the container (workspace extensions) vs locally (UI extensions); opt-out and "always installed" mechanisms; per-container toolchain switching framed as the core value.
- Personalization: dotfiles repositories.
- Workspace Trust prompts at several attach/clone/attach-to-container points (security posture around executing repo-provided config).

### DevPod (evidence A)

- "DevPod is a tool used to create **reproducible developer environments**. Each developer environment runs in a separate container and is specified through a devcontainer.json. DevPod providers can create these containers on **the local computer, any reachable remote machine, or in a public or private cloud**. It's also possible to extend DevPod and write your own custom providers."
- "You can think of DevPod as the **glue connecting your local IDE to a machine you want to use for development**… Within DevPod, every workspace is managed the same way, which also makes it easy to switch between workspaces that might be hosted somewhere else."
- Positioning vs hosted services (Codespaces / JetBrains Spaces / Google Cloud Workstations): cost, no vendor lock-in (switch provider with one command), local development with the same experience, cross-IDE (VS Code, full JetBrains suite, others via SSH), **client-only** ("No need to install a server backend, DevPod runs solely on your computer"), open-source/extensible, prebuilds, auto inactivity shutdown, git & docker credentials sync, desktop app + CLI.
- Workspace model: "A workspace in DevPod is a containerized development environment, that holds the **source code of a project as well as the dependencies** to work on that project, such as a compiler and debugger. The underlying environment where the container runs will be created and managed through a DevPod provider… which can be a remote machine in a public cloud, localhost or even a Kubernetes cluster."
- Config reuse: reuses devcontainer.json ("also used by other popular tools, such as VS Code dev containers or GitHub Codespaces") so existing projects work; "If no configuration is found, DevPod will automatically try to find out what programming language is used and provide an appropriate template."
- Lifecycle: "A workspace in DevPod can be **stopped and restarted without losing its state**… Depending on the Provider, DevPod will also automatically determine when a workspace is currently not being used and shutdown any unused resources to save costs." Docs sections exist for: create, connect, prebuild, dotfiles, credentials reuse, inactivity timeout, stop, delete.

### Coder (evidence A)

- "Coder is a **self-hosted platform** for running AI coding agents and cloud development environments on **infrastructure you control**. It works with any cloud, IDE, OS, Git provider, and IDP."
- Workspaces: "cloud development environments **defined with Terraform**, connected through a secure Wireguard tunnel, and automatically shut down when not in use. Agents and developers share the same workspace infrastructure."
- "Templates describe the infrastructure for each workspace, from EC2 VMs and Kubernetes Pods to Docker containers." "Any architecture and OS: ARM and x86-64 across Windows, Linux, and macOS from a single deployment."
- Governance: "Platform teams create and maintain templates that enforce **approved images, resource limits, and security policies**." SSO and RBAC documented. A template registry provides production-ready templates for major clouds and Kubernetes.
- Access: "Connect through VS Code, JetBrains, Cursor, a web terminal, remote desktop, or SSH." Web IDEs (code-server, JetBrains Projector, Jupyter) and remote-dev clients (JetBrains Gateway, VS Code Remote, Emacs TRAMP) plus file sync (Mutagen) listed as connection options.
- Lifecycle: "Idle workspaces stop automatically to reduce cloud spend, and restart in seconds when needed." Persistent workspaces described as "like local machines, but faster and hosted by a cloud service."
- Problem framing (official): "Provisioning consistent development environments for a large engineering team is difficult… A missed step during onboarding or an unsupported local configuration can cost hours of debugging… The developer's laptop becomes a portal into the actual compute where work happens. If a device is lost or replaced, access is simply revoked; no source code or credentials are stored locally."
- **"What Coder is not"** (boundary evidence, quoted): not an IaC platform ("Terraform is the first IaC *provisioner* in Coder, allowing Coder admins to define Terraform resources as Coder workspaces"); not a DevOps/CI platform; **not an online IDE** ("Coder supports common editors, such as VS Code, vim, and JetBrains, all over HTTPS or SSH"); not a collaboration platform; not SaaS/fully-managed.
- Consistency framing: "Infrastructure tools such as Terraform, nix, Docker, and Dev Containers produce identical environments for every developer."

### GitHub Codespaces (evidence A; hosted-editor aspects previously observed in cloud-ide pass)

- "A codespace is a development environment that's hosted in the cloud. You can customize your project for GitHub Codespaces by committing configuration files to your repository (often known as **Configuration-as-Code**), which creates a **repeatable codespace configuration for all users** of your project."
- "Each codespace you create is hosted by GitHub in a Docker container, running on a virtual machine… When you connect, you are **placed within the Docker container**. You have limited access to the outer Linux virtual machine host."
- Creation sources: template (blank or work-type) or "any branch or commit in a repository."
- Default image: Ubuntu-based with popular languages/tools; custom Linux images configurable; "Regardless of your local operating system, your codespace will run in a Linux environment."
- Connect clients: "from your browser, from Visual Studio Code, or by using GitHub CLI."
- Personalization: public dotfiles repository; Settings Sync for editor settings/shortcuts/snippets/extensions.
- Ownership/billing: personal quota; org-billed codespaces owned by the org and deletable by org owners; spending limits/budgets. (Org-side governance — enablement, machine-type restriction, secrets, audit — observed in the cloud-ide pass, 2026-09-07.)
- Prebuilds ("speed up the creation of new codespaces for large or complex repositories") and idle timeout/retention observed in the cloud-ide pass (cross-pass evidence B/A-2026-09-07).

### Vagrant (evidence A — historical / market-sample check)

- "Vagrant is a tool for **building complete development environments**… lowers development environment setup time, increases development/production parity, and makes the 'it works on my machine' excuse a relic of the past."
- "Easy to configure, **reproducible, and portable** work environments built on top of industry-standard technology and controlled by a single consistent workflow."
- Substrate is explicitly non-container: "Machines are provisioned on top of VirtualBox, VMware, AWS, or any other provider. Then, industry-standard provisioning tools such as shell scripts, Chef, or Puppet can automatically install and configure software on the virtual machine."
- Definition: "Once you or someone else creates a single **Vagrantfile**, you just need to `vagrant up` and everything is installed and configured for you to work. Other members of your team create their development environments from the same configuration…"
- Developer posture: "Vagrant will isolate dependencies and their configuration within a single **disposable, consistent environment, without sacrificing any of the tools you are used to working with (editors, browsers, debuggers, etc.)**."
- Operator/designer audiences documented as secondary users of the same workflow.

## Cross-product Comparison

| Dimension | VS Code Dev Containers | DevPod | Coder | GitHub Codespaces | Vagrant (historical) |
|---|---|---|---|---|---|
| Definition artifact | devcontainer.json (+ Dockerfile/compose) | devcontainer.json (+ auto-template fallback) | Terraform template (+ registry templates) | devcontainer.json committed to repo (Configuration-as-Code) | Vagrantfile |
| Definition owner | project author (per repo) | project author (per repo) | platform team (admin-managed templates) | project author; org governs | project author (per repo) |
| Substrate | Docker container (local/remote/other CLI/k8s attach) | container via pluggable provider | VM, K8s pod, or Docker container | Docker container on vendor VM | VM (VirtualBox/VMware/AWS) |
| Where it runs | local machine or remote host you point at | localhost, remote machine, any cloud, k8s | operator-controlled infra, any cloud | vendor-hosted VM | local VM or cloud provider |
| Attach clients | VS Code extension (window in container); terminal; debugger | VS Code, JetBrains suite, SSH; desktop app + CLI | VS Code, JetBrains, Cursor, web terminal, remote desktop, SSH; Mutagen sync | browser, VS Code, GitHub CLI | editors/browsers/debuggers stay local; `vagrant ssh`; synced folders |
| Lifecycle observed | build → connect; reopen; rebuild; recovery container on failure | create → connect → stop (state kept) → restart → delete; inactivity shutdown | provisioned → running; auto-stop when idle; restart in seconds | create → open/stop/start → delete; retention + idle timeout (prior pass) | `vagrant up` → halt/resume → destroy |
| Fast-start machinery | pre-built images + metadata labels; CI builds | prebuilds (docs section) | template registry; (prebuild machinery not verified) | prebuilds per branch (prior pass) | base boxes / provisioning |
| Personalization | dotfiles repo; extension opt-in/out; default features | dotfiles; git & docker credentials sync | (SSO/RBAC; personalization not fetched) | dotfiles repo; Settings Sync | — |
| App access | forwardPorts; temporary forwarding; publish vs forward | (via provider networking; not detailed) | (not detailed on fetched page) | port forwarding + visibility (prior pass) | forwarded ports / networking (not fetched) |
| Governance | Workspace Trust prompts | none documented (client-only) | approved images, resource limits, security policies, SSO, RBAC | org enablement, machine/timeout/retention policy, secrets, audit, billing (prior pass) | — |
| Headless reuse | CI via dev container CLI/GitHub Action | — | explicitly not a CI platform | — | — |
| AI-era posture | (VS Code agent features elsewhere) | — | AI agents share workspace infrastructure; control-plane agent loop | (not re-fetched) | — |

Notes on the comparison:

- Every sampled product holds the same three-part skeleton: **a shareable environment definition → a provisioned runnable environment → developer tools attached into it**. What varies is where the environment runs, who owns the definition, and which client attaches.
- The definition format is *not* stable across the Type (devcontainer.json vs Terraform vs Vagrantfile), and the substrate is *not* stable (container vs VM vs pod). Both are implementation layers.
- The editing surface is external in every sampled product — including the vendor-hosted one, whose docs say the user is "placed within the Docker container" while the editor (browser or desktop) remains the client. Coder states outright it is "not an online IDE."

## Abstraction Levels

### L0 — Defining Invariant

The Type is the joint holding of three structures:

1. **The environment definition of record** — a persistent, declarative, machine-independent description of a project's complete development environment (runtime, toolchain, dependencies, project-specific tool/IDE configuration, and how the running app is reached). It exists independently of any machine and any person, and is shareable — that shareability is the point ("other members of your team create their development environments from the same configuration"). Remove → setup documentation, personal install scripts, or a bare spec/catalog with no execution.
2. **The provisioned workspace/environment instance** — the platform itself builds or creates a runnable environment from the definition: code + toolchain together in one place the developer can enter, with a lifecycle (create/build → start → stop → rebuild → delete). Remove → a format/spec, a scaffolding tool, or config management that never produces a developer-enterable working environment.
3. **The attach layer** — the developer's ordinary tools (editor, terminal, debugger, browser) connect into the environment and work against it; execution happens in the environment while editing/personal tooling stays on the client side and is pluggable. Remove → headless CI environment definitions or plain container build tooling.

The purpose the joint hold serves is **reproducibility and disposability**: every developer and machine gets the same environment from the same record, and the environment itself is disposable (delete/rebuild) because the durable assets are the code and the definition, not the environment.

Deliberately excluded from L0 despite near-universality in the modern market (each fails the "remove → different Type" test or the historical check):

- Containers/Kubernetes as substrate (Vagrant: VMs; Coder: VMs and pods; spec: substrate-agnostic "supporting tools")
- devcontainer.json or any specific definition format (Coder: Terraform; Vagrant: Vagrantfile)
- Repository-committed configuration-as-code (Coder's templates are admin-owned, not repo files)
- Cloud/remote hosting (VS Code Dev Containers and DevPod document full local operation; the spec says "locally or remotely")
- Any specific client — browser, desktop extension, or CLI (all three modes documented across the sample)
- Prebuilds, idle auto-stop, port forwarding, dotfiles, features/templates ecosystems, governance

### L1 — Common Mature Structure

Present across the sample (evidence B), expected in modern products but not definitional:

- Container-based substrate with a Linux-flavored default image (every modern product; Vagrant's VM shows it is implementation, not essence)
- Definition stored with the project's source (repo-committed devcontainer.json / Vagrantfile) — the *project-coupled* pole; admin-managed template registries (Coder) are the enterprise-coupled alternative, so "committed to the repo" is common, not invariant
- Named lifecycle hooks around creation (setup commands ordered before/after content and user assignment; failure halts subsequent setup — spec-documented)
- Prebuilds / pre-built images / template registries to make provisioning fast
- Stop/restart with state preserved; idle auto-shutdown to save cost (DevPod, Coder, Codespaces)
- Port forwarding/publishing so the running application is reachable from the client
- Personalization: dotfiles repositories, credential/settings sync applied at attach
- Tool/extension injection into the environment (editor extensions installed inside; per-environment toolchain switching)
- Editor-client breadth: desktop IDE via extension/gateway, SSH/terminal, browser IDE, CLI
- Reuse of the same definitions beyond interactive dev: CI/testing (spec + VS Code CI action); Coder explicitly disclaims being a CI platform, showing reuse is an adjacent capability, not the platform's job
- AI coding agents sharing workspace infrastructure (Coder) — current-market layer, not definitional

### L2 — Variant / Optional Structure

- Hosting locus: local-only (Docker on the dev machine) ↔ client-only pluggable providers ↔ self-hosted org platform ↔ vendor-hosted SaaS
- Governance depth: none (individual) ↔ org billing/quota/machine-type/timeout policy ↔ platform-team template governance with approved images, resource limits, security policy, SSO/RBAC, audit
- Definition ownership: project-authored (per-repo) vs platform-authored (admin templates) vs spec-community-authored (features/templates collections)
- UI form: editor extension vs standalone desktop app vs CLI vs web dashboard
- Environment persistence posture: persistent/restartable by default vs ephemeral-by-design
- Multiple containers per environment (compose-based service stacks) — advanced variant
- Machine-type selection / declared resource requirements (hostRequirements; vendor machine pickers)
- Ecosystem sharing of features/templates (spec registries, template registries)

### L3 — Vendor-specific Structure

(stays in Research Notes)

- Codespaces: machine-size menu, retention/idle-timeout windows, monthly quotas, spending limits, org-billed ownership rules, preview-URL domains, Linux-only remote container OS
- DevPod: "5–10× cheaper than hosted services" marketing claim; one-command provider switching; client-only architecture framing
- Coder: Wireguard tunnel transport; Coder Agents control-plane agent loop (LLM credentials kept out of workspaces, per-user spend limits, air-gapped support); Coder Registry
- VS Code: Workspace Trust prompts; Recovery Container; Remote Tunnels; `dev.containers.defaultExtensions` / `defaultFeatures` settings; extension kind forcing (`remote.extensionKind`)
- Spec internals: exact lifecycle property names (`onCreateCommand` etc.), `devcontainer.metadata` image-label merge logic, `devcontainerId` variable, port-attribute options

## Vendor-specific Findings

- Coder's "What Coder is not" list is the market's own boundary articulation and is used as direct evidence in Boundary Findings (not generalized beyond Coder, but consistent with the locus seam).
- VS Code's Workspace Trust and Recovery Container are product-specific safety machinery around executing repo-supplied environment definitions — a real risk class for the Type (definitions are executable), but the specific mechanisms are vendor-specific.
- DevPod's provider plugin model (write your own provider) is the purest expression of "environment substrate is pluggable" but its single-provider-at-a-time client-only model is product-specific.

## Rejected Findings

- **"Dev container = Docker container"** — rejected. Vagrant (VMs), Coder (VMs, pods, containers), and the spec's substrate-agnostic "supporting tools and editors" framing all show the container is the current dominant substrate, not the invariant.
- **"devcontainer.json is the defining artifact"** — rejected. It is the dominant shared format (spec + VS Code + DevPod + Codespaces), but Coder uses Terraform templates and Vagrant used Vagrantfile. The invariant is "machine-independent shareable environment definition," not a format.
- **"Cloud-hosted / browser-delivered"** — rejected. That is the Cloud IDE pattern; this Type's local poles (VS Code Dev Containers, DevPod) and self-hosted pole (Coder) are first-class, and the spec says "locally or remotely."
- **"Configuration-as-code committed to the project repo"** — rejected as invariant. Common (VS Code, DevPod, Codespaces, Vagrant) but Coder's enterprise model has admin-owned templates; the invariant is the shareable record, wherever it lives.
- **"Prebuilds / fast-start caching is core"** — rejected. Common mature structure; provisioning speed is an optimization of the create step, not the defining act.
- **"The platform includes an editor/IDE"** — rejected as invariant. Editor support exists everywhere, but as *attach clients* to the environment; the defining act is environment definition+provisioning. Coder: "not an online IDE."
- **"Auto-stop / cost machinery is core"** — rejected. A consequence of hosted/disposable postures, absent in the local pole.

## Boundary Findings

**vs Cloud IDE (§12, processed) — the sharpest seam; ratified from this side.**
The working seam is **locus of operation + editing-surface fusion**: a dev-container/workspace platform defines and provisions environments that may run anywhere — including the developer's own machine — and is consumed through whatever editor the developer already uses; a Cloud IDE hosts and lifecycle-manages remote compute and delivers the editing-and-execution experience as a fused service. Evidence from this pass: Coder — a self-described cloud-development-environment platform on vendor-class infrastructure — states it is "not an online IDE" because it "supports common editors… all over HTTPS or SSH" (the environment is the product; the editor is pluggable); DevPod calls itself "the glue connecting your local IDE to a machine"; the VS Code pole attaches a *local* IDE to a *local* container, which no Cloud IDE framing covers; the spec addresses "supporting tools and editors" in the plural. The seam blurs exactly where the cloud-ide pass said it would: repo-attached hosted products (Codespaces-class) are simultaneously Cloud IDEs (fused experience, vendor compute) and members of this Type's substrate ecosystem (devcontainer.json configuration-as-code). Recommendation stands: **joint review**; candidate outcomes are keep-both-Types with the locus test as the recorded seam, or a two-leaf split (environment-definition platform vs hosted environment service).

**vs Developer Environment Manager (§12 sibling, unprocessed) — flagged for joint review.**
Hypothesis from this side: an environment *manager* curates the developer's own machine — installing/syncing toolchains, editor settings, project-local runtimes on the workstation itself, where the machine state is the thing managed. A workspace *platform* provisions **self-contained, disposable environments from a per-project definition**, where the environment is separate from (or even replaces) the developer's machine state. Coder's official problem framing ("Each developer has preferences for operating systems, editors, and toolchains, and ensuring a reliable build environment across all of them is a maintenance burden… moving the environment off the developer's machine") articulates the platform side of this seam. Unresolvable from one side; record for the next pass.

**vs Infrastructure-as-Code Platform / Configuration Management.**
Direct evidence: Coder ("Coder is not an IaC platform — Terraform is the first IaC *provisioner* in Coder, allowing Coder admins to define Terraform resources as Coder workspaces"). IaC's object of record is infrastructure; here IaC is at most a provisioner whose output only becomes the Type when it is a developer-enterable workspace attached to tools. The devcontainer spec makes the same move internally: "describe how to enrich a container for the purposes of development rather than acting as a multi-container orchestrator format."

**vs Container Management / Kubernetes Management Platform.**
Container management operates shared fleet workloads (services) with health/scaling/rollout as the working objects. Here environments are single-developer-scale, disposable/rebuildable by design, and the working objects are the definition and the personal workspace instance. Substrate overlap (both may run containers on k8s) does not transfer the model.

**vs Project Scaffolding / Code Generator.**
Scaffolding produces a codebase once; this Type provisions the working *environment* for a project (usually an existing one), continuously, from a definition. DevPod's no-config fallback (detect language, pick template) is the closest approach between the two, but it provisions an environment around the code, it does not generate the code.

**vs Internal Developer Platform / IDP (§12) — mild overlap at the enterprise pole.**
Platform teams administer both. Distinction proposed: the IDP's scope is org-wide self-service across many service kinds (catalog, scaffolding, deployments); this Type's scope is specifically development environments. Coder's template governance is dev-workspace-scoped. Flagged, low urgency.

**vs Continuous Integration Platform.**
The same definitions are deliberately reusable headlessly (spec: "aid in continuous integration and testing"; VS Code ships a CI action). CI platforms consume definitions as inputs; they do not provide the developer-attach workspace. Coder's "not a DevOps/CI platform" reinforces.

**The spec itself is a boundary anchor.** containers.dev is the Type's shared definition format but is *not* an instance of the Type — no provisioning, no workspaces, no attach. Useful test case that the definition alone is not the application.

## Uncertainties

- Coder's exact relationship to devcontainer.json inside Terraform templates (supported natively? via setup scripts?) was not verified — the About page lists "Dev Containers" among consistency tools without detailing mechanics. Not claimed either way.
- DevPod prebuild mechanics and Coder prebuild/cache machinery were not fetched (docs sections exist / registry exists); fast-start is asserted as common structure at the concept level only.
- Vagrant's current attach ergonomics (synced folders vs IDE integrations) were not deeply fetched; the historical check only needs the definition-provision-consume skeleton, which is documented.
- The enterprise governance picture is documented directly only for Coder and (via prior pass) Codespaces; generalizing governance depth across the Type's enterprise pole is inference (marked C where used).
- The "Developer Environment Manager" seam is a hypothesis from one side.
- Market drift risk: several hosted vendors repositioned around AI agents (Coder Agents, Gitpod→Ona per prior pass). Workspace infrastructure appears stable as the substrate for agents; whether that changes the Type's center of gravity is unknown.

## Final Synthesis

A Dev Container / Workspace Platform is a developer-facing platform whose world consists of exactly three jointly-held things: an **environment definition of record** (machine-independent, shareable description of a project's complete dev environment), the **provisioned workspace instance** (a runnable, disposable environment holding code + toolchain, with a create → start/stop → rebuild → delete lifecycle), and the **attach layer** (the developer's ordinary editor/terminal/debugger connecting into that environment). The purpose the joint hold serves is reproducibility — every developer and every machine gets the same environment from the same record — and disposability — the environment is routinely destroyed and recreated because the durable assets are the code and the definition.

The substrate (container, VM, pod), the definition format (devcontainer.json, Terraform, Vagrantfile), the hosting locus (local, self-hosted, vendor cloud), the client (editor extension, SSH, browser, CLI), prebuilds, auto-stop, port forwarding, dotfiles, features/templates ecosystems, and org governance are all real layers of the modern market but none is definitional — the VM-era lineage passes the historical check on the bare skeleton, and the market's own boundary statements ("not an online IDE", "not an IaC platform") confirm that the environment — not the editor, not the infrastructure — is the product.
