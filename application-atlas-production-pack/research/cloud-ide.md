# Research Notes — Cloud IDE

Research date: 2026-09-07

## Research Goal

Understand what a Cloud IDE (increasingly marketed as a "cloud development environment", CDE) actually is as an Application Type: what its core objects are (workspace, environment, editor, code), how its lifecycle works (create → configure → edit/run → stop/resume → delete), what is definitional vs merely common in today's market, and where its boundaries sit against the local IDE, dev-container/workspace platforms, web editors, source-hosting platforms, and AI coding agents.

## Initial Boundary (hypothesis before research)

- Core hypothesis: a Cloud IDE is a development environment whose code, toolchain and runtime live on vendor-managed (or self-hosted operator-managed) remote compute, with the editing surface delivered as a network client (browser or thin desktop connection) and execution (terminal/build/run) happening remotely.
- Nearest neighbors suspected: Integrated Development Environment / IDE, Code Editor, Dev Container / Workspace Platform, Web Development IDE, Source Code Hosting Platform, AI Coding Assistant / Agent.
- Known risk: the boundary vs Dev Container / Workspace Platform is conceptually thin (same config format, different hosting locus); the market is actively drifting (Gitpod → Ona "background agents", Replit → AI app-building), which may make "Cloud IDE" a moving target.

## Research Questions

1. What is the managed unit ("workspace"/"environment"/"codespace"/"project") and what does it bind together (code, toolchain, runtime, IDE)?
2. How is a workspace created (from repo, template, blank), configured, and reproduced (configuration-as-code)?
3. Which clients reach the workspace (browser, desktop editor via SSH/Gateway, CLI) — and is "browser" definitional?
4. How does execution work: terminal, build, run, debug; how does the user see the running app (port forwarding / preview URLs)?
5. What lifecycle and governance exist: stop/start, idle timeouts, retention, deletion, machine types, regions, quotas, org policies, audit?
6. How does source control integrate (clone, OAuth, commit/push, PR)?
7. How do startup-time optimizations work (prebuilds, image caching)?
8. What collaboration capabilities exist (pair programming, shared workspaces)?
9. What is the AI posture of each product in 2026 (extension, configurable tool, agent-first platform)?
10. Where do the boundaries with local IDEs, dev-container platforms, web editors, hosting platforms and AI agents actually sit?

## Representative Products

Selected for market spread, documentation quality, product-philosophy diversity and customer-tier diversity:

| Product | Why sampled | Docs tier reached |
|---|---|---|
| GitHub Codespaces | Market-defining repo-attached cloud environment; dev-container standard-bearer; individual + org/enterprise tiers | Tier 1 (docs.github.com Codespaces section + what-are-codespaces) |
| Eclipse Che | Self-hosted Kubernetes-native open-source pole; historical (2015+) and terminology anchor ("cloud development environments") | Tier 1 (eclipse.org/che docs, "What is Che?") |
| AWS Cloud9 | Classic "cloud IDE" bundled in a cloud console; pre-container-era environment model (EC2 / SSH server) | Tier 2 (aws.amazon.com/cloud9 product page; docs site returned JS shell) |
| Ona (Gitpod lineage) | Cloud-dev-environment-native vendor; ephemeral prebuilt environments; now repositioned around background agents; managed + VPC/self-hosted | Tier 1 (ona.com/docs overview + editors overview) |
| Replit | Consumer/education pole; long-running browser IDE now repositioned as AI build/publish platform | Tier 1 (docs.replit.com root + llms.txt index + Project Editor page) |

## Sources

- GitHub Codespaces docs — https://docs.github.com/en/codespaces ; https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces (fetched 2026-09-07)
- Eclipse Che docs — https://www.eclipse.org/che/docs/stable/discover/what-is-che/ (fetched 2026-09-07; reached via two redirects from eclipse.dev/che/docs)
- AWS Cloud9 — https://aws.amazon.com/cloud9/ (fetched 2026-09-07). Note: https://docs.aws.amazon.com/cloud9/latest/user-guide/what-is-cloud9.html returned only the page title (JS-rendered docs shell) — no operational docs extracted for Cloud9.
- Ona docs — https://ona.com/docs (overview) and https://ona.com/docs/ona/editors/overview (fetched 2026-09-07). https://gitpod.io/docs is a JS app ("You need to enable JavaScript") — Gitpod Classic docs not reachable.
- Replit docs — https://docs.replit.com/ root, https://docs.replit.com/llms.txt index, https://docs.replit.com/learn/projects-and-artifacts/project-editor.md (fetched 2026-09-07; the Project Editor page body was largely JS scaffolding; only its summary line and index descriptions were reliably observable).

Evidence layers used below: **A** = directly observed on the cited source for that product; **B** = cross-product commonality observed across the sample; **C** = canonical inference from comparison + boundary reasoning.

## Product Observations

### GitHub Codespaces (evidence A unless noted)

- Definition (official): "A codespace is a development environment that's hosted in the cloud."
- The environment is created in a Docker container running on a virtual machine hosted by GitHub; user connects "from your browser, from Visual Studio Code, or by using GitHub CLI"; when connected, the user is "placed within the Docker container" with limited access to the outer VM host.
- Machine selection exists (documented range 2 cores/8 GB/32 GB up to 32 cores/128 GB/128 GB — precise numbers noted here, kept out of the final document); default image is Ubuntu-based with popular languages/tools; codespaces always run Linux regardless of local OS.
- Creation sources: from any branch/commit of a repository, or from blank/work-type templates.
- Configuration-as-code: dev container configurations committed to the repository create "a repeatable codespace configuration for all users"; rebuild the container to apply config changes; dev container "features" add tools/runtimes.
- Lifecycle documentation is a first-class section: create → open/reopen → stop and start → delete; automatic deletion; retention configuration (stopped codespaces retained up to 30 days per docs — precise value kept here); idle timeout settings.
- Source control integration: commit and push from the codespace; PR creation/review in a codespace; "exporting changes to a branch" exists as a troubleshooting path (i.e., uncommitted workspace state is a real failure mode).
- Port forwarding to "test and debug your application"; port visibility can be shared within the organization or publicly; orgs can restrict port visibility.
- Prebuilds: "prebuilds help to speed up the creation of new codespaces for large or complex repositories"; configured per branch; managed/deleted as configurations.
- Organization surface: enable/disable Codespaces; choose who owns and pays; cost/usage limits; restrict machine types, base images, idle timeout, retention, number of org-billed codespaces; audit logs; security logs; org/repo/account-level development-environment secrets; GPG commit signing.
- Personalization: dotfiles repository; Settings Sync for editor settings/extensions; default editor and default region (data residency) user settings.
- Collaboration: "work collaboratively in a codespace by using Visual Studio Live Share."
- AI: GitHub Copilot usable inside Codespaces as a VS Code extension (reference doc exists).
- Boundary artifact observed: the separate **github.dev web-based editor** — browser file editing with commits, documented under the Codespaces section but distinct from codespaces (no hosted environment). This is the market's own example of an editing surface without managed compute → not a Cloud IDE.
- Client plurality is explicit: browser, VS Code desktop, GitHub CLI, and a command-shell connection mode are all documented.

### Eclipse Che (evidence A unless noted)

- Definition (official): "Eclipse Che is a Kubernetes-native platform that provides cloud development environments (CDEs) to development teams… developers get on-demand workspaces: container-based environments with all the tools, dependencies, and IDE access needed to code, build, test, and debug applications."
- Zero-install positioning: "accessible through a browser or desktop IDE."
- Workspace model (official, load-bearing): "Che defines a workspace as the project source code together with all dependencies necessary to edit, build, run, and debug it. The IDE and development runtime are treated as workspace dependencies, embedded and always included. This differentiates Che from traditional development environments where the IDE is bound to a workstation and runtimes are configured locally."
- Workspaces run as Kubernetes/OpenShift Pods; the platform is installed by an Operator (CheCluster custom resource), on OpenShift, Kubernetes (EKS, Azure), or locally (Minikube) — self-hosted posture; air-gapped installation documented.
- Environment defined by **devfile** (devfile registry, workspace templates); workspace components customizable; plugin registry.
- Editor is a workspace component and selectable: VS Code – Open Source in the browser by default; JetBrains IntelliJ via JetBrains Gateway (desktop); URL parameters allow choosing IDE, IDE image, container image, memory/CPU limits, storage, duplicate-workspace behavior, even AI provider — per-workspace configuration surface.
- Git integration: start a workspace from a git repository URL; Git authentication documented (personal access tokens); admin-configured OAuth for GitHub/GitLab/Bitbucket/Azure DevOps.
- Lifecycle: start/stop/restart; workspace idling (idle timeout, with a doc on preventing idling for long-running commands); backups/restores; persistent storage via claims; admin limits on workspaces kept per user and simultaneously running workspaces.
- Dashboard for workspace management; administrator roles (platform admin vs developer); OIDC identity; Kubernetes RBAC; monitoring (Prometheus) and telemetry plugins.
- Startup-time optimization: Image Puller for image caching across cluster nodes.
- AI posture: "Using AI assistants in workspaces" — configuring an AI provider API key, changing the AI tool per workspace, persisting Claude Code configuration, distributing skills. AI is a workspace component, not the product's identity.
- Terminology drift inside one vendor: nav labels use "cloud development environment" where older docs said "workspace" — Che itself equates the two.

### AWS Cloud9 (evidence A from the product page; docs tier limited)

- Self-classification (official): "A cloud IDE for writing, running, and debugging code" — "a cloud-based integrated development environment (IDE) that lets you write, run, and debug your code with just a browser. It includes a code editor, debugger, and terminal."
- Environment hosting: "run your development environment on a managed Amazon EC2 instance or any existing Linux server that supports SSH" — two hosting modes: vendor-managed instance, or connect-to-your-own-server. No container/devfile requirement on this page — a pre-container-style environment model.
- "Prepackaged with essential tools for popular programming languages"; "tooling for over 40 programming languages" (marketing-precision figure kept here only).
- Terminal: "browser-based shell experience… install additional software, do a git push, or enter commands" — git flows through the terminal, not a dedicated UI.
- Cloud-console coupling: terminal has sudo to the managed EC2 instance and a preauthenticated AWS CLI; serverless/Lambda local testing and debugging; position as the IDE adjacent to AWS resources.
- Collaboration: "share your development environment with your team… pair-program… see each other type in real time and instantly chat… from within the IDE."
- Multiple environments: "maintain multiple development environments to isolate your project's resources."
- Not observed on this page (docs shell unreachable): lifecycle details (stop/idle), devcontainer/devfile support, org governance. No claims made on those.

### Ona — Gitpod lineage (evidence A unless noted)

- Current definition (official): "The platform for background agents… Run a team of AI software engineers in the cloud, orchestrated, governed, and secured at the kernel." The company that defined the ephemeral-cloud-dev-environment category now leads with agents.
- Environment substrate still central: "Create reproducible environments: Define your dev setup as code with Dev Containers and Automations, so every environment starts identically. No 'works on my machine' problems."
- Environments are "ephemeral, isolated", with SSO, OIDC, SCIM and guardrails; governance/audit at organization level.
- Compute: runners — Ona Cloud (managed) or the customer's own VPC on AWS/GCP (hybrid/self-hosted posture).
- Editor client is pluggable (official editors matrix): VS Code (SSH via extension), **VS Code Browser (browser mode)**, Cursor, Windsurf (VS Code forks), JetBrains IDEs (Toolbox plugin), Zed (manual SSH). "Ona environments connect to your editor over SSH. Most editors support one-click open from the dashboard."
- devcontainer.json drives environment AND per-editor customizations (e.g., `customizations.vscode.extensions`, `customizations.jetbrains.plugins`).
- Prebuilds with "prebuild warmup" (JetBrains backend preinstalled and indexes built during prebuilds) — startup-time optimization machinery.
- Port forwarding: "access services running in your environment"; browser handling opens URLs from inside the environment in the local browser.
- Automations: start/stop services and tasks; trigger agents on schedules, pull-request events, or issue trackers; AGENTS.md and skills teach agents the codebase.
- Organization policies can constrain which editors are used ("organization editor policies") — governance reaches into the client choice.

### Replit (evidence A for structure of docs; moderate for workspace internals)

- Official docs reorganized around: Chat, Build, Design; Projects ("a Project brings together the code, data, and artifacts for substantial build and design work"); Conversations; Routines.
- Project Editor described as "your home base on Replit where you talk to Agent, see your app take shape, and manage everything" — editor + AI agent + app management in one surface.
- Development URLs documented: "preview and share your in-progress app" — preview surface for running code (A).
- Publishing/deployments documented ("Publish your app… verify the live version"; "Publishing… Share your Replit Apps with the world in just a few clicks") — the platform extends from development to hosting (A).
- Version control tooling documented; team workspaces; enterprise IAM (roles Admin/Member/Guest/Viewer, groups, SAML SSO, SCIM, audit logs, SIEM integration); usage quotas (CPU/RAM/storage per plan).
- Access surfaces: web, desktop app (macOS/Windows), mobile apps (iOS/Android) — beyond browser-only.
- The classic browser-IDE substrate (editor, runtime, shell) is presupposed by these structures but the current docs no longer lead with it; the product is positioned as an AI build/publish platform. Workspace internals (shell availability, Nix-based config) could not be directly verified in this pass — claims about them are kept out of the final document or marked moderate.

## Cross-product Comparison

| Dimension | GitHub Codespaces | Eclipse Che | AWS Cloud9 | Ona (Gitpod) | Replit |
|---|---|---|---|---|---|
| Managed unit name | codespace | workspace / "cloud development environment" | (dev) environment | environment | project/workspace |
| Unit binds | code + dev container + tooling on VM | source code + dependencies + IDE + runtime as pod | code + toolchain on EC2 or SSH server | code + dev container + automations | code + data + artifacts |
| Hosted by | GitHub (vendor cloud) | self-hosted operator's Kubernetes/OpenShift | AWS (managed EC2) or user's own Linux server via SSH | Ona Cloud or customer VPC (AWS/GCP) | Replit (vendor cloud) |
| Primary client | browser / desktop VS Code / CLI | browser (VS Code-OSS) or desktop via Gateway | browser | pluggable editors (browser VS Code, desktop VS Code/forks, JetBrains, Zed) | web / desktop / mobile apps |
| Config-as-code | devcontainer.json (committed to repo) | devfile | none on observed page (prepackaged tools) | devcontainer.json + Automations | project/templates (not verified in detail) |
| Execution | terminal in container; port forwarding | terminal in pod; endpoints/ports | terminal with sudo + preauthenticated AWS CLI | terminal; port forwarding; automations | preview URLs; publish/deploy |
| Lifecycle machinery | stop/start/delete, auto-delete, retention, idle timeout | start/stop/idling, backups, storage, admin limits | multiple environments (observed); lifecycle not verified | ephemeral by design + prebuilds | plan/usage quotas (lifecycle not verified) |
| Startup optimization | prebuilds | image puller / image caching | prepackaged tools | prebuilds + warmup | (not observed) |
| Collaboration | Live Share | (team workflow, PR review) | real-time shared env + chat | (multi-editor, org policies) | team workspaces, parallel agent tasks |
| Governance | org enablement, cost limits, machine/port/base-image restrictions, audit | RBAC, OIDC, namespaces, limits, monitoring | (not observed) | SSO/OIDC/SCIM, guardrails, audit, editor policies | roles/groups, SAML SSO, SCIM, audit |
| AI posture | Copilot as extension | configurable AI assistant per workspace | (predates AI era) | agent-first platform (background agents, Automations) | AI-first build platform (Agent, modes) |
| Self-description | "development environment that's hosted in the cloud" | "cloud development environments (CDEs)" | "cloud IDE" | "platform for background agents" | AI app-building platform |

## Canonical Model

### L0 — Defining Invariant

Three properties; remove any one and the product is no longer a Cloud IDE:

1. **Managed remote development workspace** — the product provisions and lifecycle-manages a remote compute unit that binds together the project's source code and the tools/runtimes needed to edit, build, run, and debug it. The environment lives on remote (or self-hosted-cluster) compute operated by the product — not on the developer's workstation.
2. **Client-delivered editing surface** — code editing is delivered as a network client: a browser IDE or a desktop editor attached over a managed remote connection. The editing surface may be the vendor's own editor or a pluggable client (Che: VS Code-OSS or JetBrains Gateway; Ona: SSH editor matrix), but editing happens against the remote workspace.
3. **Remote execution** — the user runs commands and builds/runs code on the workspace itself (terminal, run configs, preview of served ports/URLs). Compute for development happens remotely.

Why minimal: Cloud9 (plain EC2/SSH server, no containers, no config files) satisfies all three; Che (Kubernetes pods), Codespaces (container on VM), Ona (ephemeral dev containers), Replit (managed project runtime) satisfy all three in very different substrates. Anything strictly beyond these three is era- or posture-specific.

What is deliberately excluded from L0 despite being near-universal today: browser-only access (desktop thin clients and CLI connections are documented client modes), containers/Kubernetes (Cloud9's SSH-server mode lacks both), dev-container/devfile configuration files (absent in the observed Cloud9 model), git UI integration (Cloud9 documents git via terminal; older cloud editors used FTP), prebuilds, AI.

### L1 — Common Mature Structure

Present across the sample (evidence B), expected in modern products but not definitional:

- Source-control integration: create workspace from a repository/branch; OAuth/token auth to git providers; commit/push and PR flows from inside the environment (Codespaces, Che, Ona; Cloud9 documents terminal git push).
- Environment definition / configuration-as-code: devcontainer.json (Codespaces, Ona), devfile (Che), prepackaged stack templates (Cloud9) — the concept "a versioned definition of the environment that makes it repeatable for a whole team" is common mature structure; its format is implementation.
- Workspace dashboard/management surface: list, create, open, stop, delete workspaces; status.
- Port forwarding / preview URLs: view and share the running application from the browser (Codespaces, Ona, Che, Replit).
- Lifecycle controls: idle timeouts/auto-stop, retention policies, storage persistence across stop/start (Codespaces, Che documented; Ona ephemeral-by-design as the alternative pole).
- Startup-time optimization: prebuilds / image caching / prepackaged tooling (all five in some form).
- Editor machinery and personalization: extensions/plugins (Open VSX in Che; VS Code extensions in Codespaces/Ona), dotfiles/settings sync (Codespaces), selectable IDE (Che URL parameter; Ona editor matrix).
- Secrets and environment variables for workspaces (Codespaces org/repo/account secrets; Che secret mounting; enterprise-adjacent in Ona).
- Collaboration on a shared environment: real-time pair editing/environment sharing (Cloud9, Codespaces/Live Share), team workspaces (Replit).
- Organization governance: org enablement, cost/usage controls, audit logs (Codespaces, Ona, Che, Replit enterprise).

### L2 — Variant / Optional Structure

- Hosting/deployment posture: fully vendor-hosted SaaS (Codespaces, Replit) ↔ self-hosted platform on the operator's cluster (Che) ↔ hybrid managed/VPC runners (Ona) ↔ connect-to-own-server (Cloud9 SSH mode).
- Bundling posture: standalone product ↔ bundled in a source-hosting platform (Codespaces) ↔ bundled in a cloud provider console (Cloud9).
- Environment persistence philosophy: persistent workspaces with storage/retention (Codespaces, Che) ↔ ephemeral environments recreated per session from config (Ona).
- Identity substrate: platform account (GitHub), vendor account (Replit), enterprise IdP via OIDC/SAML/SCIM (Che, Ona, Replit enterprise); org-vs-personal billing ownership (Codespaces).
- Audience posture: consumer/education (Replit), individual + org (Codespaces), enterprise platform engineering (Che, Ona governance).
- AI posture: extension installed in the editor (Copilot in Codespaces), configurable per-workspace AI assistant (Che), background-agent platform built on the environment (Ona), AI-first app building and publishing (Replit) — a spectrum, era-current.
- Publish/deploy coupling: deploying from the environment to the vendor's cloud (Cloud9 → AWS; Replit → Replit hosting) — present in some products, absent as a requirement.
- Client surfaces beyond browser: desktop apps and mobile apps (Replit), desktop IDE clients (Che/Ona), CLI (Codespaces `gh`).
- Hardware/data-residency selection: machine types (Codespaces), region selection (Codespaces default region), CPU/memory per workspace via devfile URL params (Che).

### L3 — Vendor-specific (research notes only)

- Codespaces: dev container "features"; 2→32-core machine-type menu; Ubuntu default image; 30-day stopped-retention maximum; port-visibility policy controls; GPG signing; github.dev companion editor; disaster-recovery guidance.
- Che: CheCluster custom resource + Operator; chectl CLI; devfile registry and plugin registry; Open VSX registry administration; Image Puller; kubedock container-running; fuse-overlayfs storage driver; Woopra telemetry; URL-parameter matrix for workspace starts; multi-cluster/scale docs.
- Cloud9: preauthenticated AWS CLI in terminal; sudo to the EC2 host; Lambda/serverless local debugging; "40+ languages" prepackaging claim.
- Ona: SSH connection model with per-editor matrix; JetBrains prebuild warmup; Automations triggers (PR events, schedules, issue trackers via Linear/Jira); AGENTS.md + skills; `ona env ssh-config` CLI; organization editor policies; runners product names.
- Replit: Agent modes (Free/Power/Max), checkpoints, credit/allowance billing, Routines, Design canvas/frames/design systems (DESIGN.md), App Storage/Auth/Clerk connectors, Launch flow to App Store/Play, strike system.

## Historical / Market-Sample Check

- Era spread deliberately included: pre-container environment model (Cloud9 on EC2/SSH server, no config files), container era (Che 2015+, Codespaces 2020+), agentic era (Ona 2025+, Replit 2024+). All satisfy the L0 triple → definition is not over-fit to the container/devfile era.
- The word "IDE" itself is eroding: Che officially calls its output "cloud development environments (CDEs)"; Ona self-describes as an agent platform; Replit as an AI build platform. Only Cloud9 (2017-era positioning) still says "cloud IDE" on its product page. The directory leaf name "Cloud IDE" is the historical market name; the referent is stable (the L0 triple) while the label drifts. Record as naming drift, not a taxonomy conflict.
- Platform-native and regional samples not directly fetched this pass (e.g., Codeanywhere, Google Cloud Workstations, GitLab Web IDE, CNCF-baseline self-hosted stacks). Their structural fit is argued from category knowledge only — no claims about them in the final document. Risk to the definition is low because Cloud9 and Che already provide the older/platform-native poles.

## Vendor-specific Findings (kept out of final doc)

All L3 items above. Additionally:

- Codespaces billing mechanics (monthly quota, org-billed ownership, budgets) are product-specific packaging, not category structure.
- Che's Kubernetes-native RBAC/namespace model is one governance implementation; Codespaces org policies and Ona guardrails are different implementations of the same L1 governance concept.
- Replit's full current feature set (Agent modes, credits, Routines, Design suite) belongs to its AI-platform identity, not to the Cloud IDE Type; only its workspace/editor/preview/publish substrate was used.

## Boundary Findings

| Nearby Type | Seam | Test |
|---|---|---|
| Integrated Development Environment / IDE; Code Editor (both local) | Where the environment lives. Local IDE: editor + code + runtime on one machine. Cloud IDE: product-managed remote workspace; editor is a client against it. | Remove remote managed workspace → local IDE/editor. Note the blur: desktop IDEs can attach to remote machines via extensions; the Type question is whether the product itself provisions and lifecycle-manages the remote environment. |
| Dev Container / Workspace Platform (sibling leaf, unprocessed) | Same config substrate (devcontainer.json), different locus. Dev-container platform: define/share/provision environments, possibly running on the developer's own machine, consumed through any editor. Cloud IDE: the product hosts and manages the compute and delivers the editing+execution experience as a service. | If the environment runs on the developer's own machine from a config file → dev-container platform, not Cloud IDE. If the product operates the remote compute and its lifecycle → Cloud IDE. Sharpest unresolved seam in this Type — recommend joint review with that leaf (Codespaces/Che/Ona sit deliberately on both sides of the formats). |
| Web Development IDE (sibling leaf) | Orthogonal axes: "web" = target domain (building web apps); "cloud" = where the IDE/environment runs. A web-development IDE is usually local; a Cloud IDE targets any stack. | Name collision only, not structural overlap. |
| Web-based code editors (e.g., github.dev, paste-and-edit surfaces) | Edit-only, no managed runtime/workspace. | github.dev is documented by GitHub itself as a lighter surface distinct from codespaces; without remote execution it is not a Cloud IDE. |
| Source Code Hosting Platform | Stores/serves repos and PRs; may bundle a cloud IDE (Codespaces). | Remove the managed dev environment → still a hosting platform; remove hosting → the cloud IDE still edits/runs code from any git URL (Che documents starting from a raw repo URL). |
| AI Coding Assistant / AI Coding Agent | Assistant augments editing inside an environment; agent performs work. Cloud IDE is the environment substrate they plug into. | Ona (background agents) and Replit (Agent-first) show the environment product absorbing agentic capabilities — drift pressure documented in Variants, not a Type merge: remove agents and Ona's environment layer still is a CDE; remove the environment and the agent has nowhere to run. |
| PaaS Management Console / cloud consoles | Deploy target vs development environment. | Cloud9's cloud-console coupling is a bundling variant; its identity remains the IDE (editor/debugger/terminal). |

## Uncertainties

- Cloud9 operational documentation (docs.aws.amazon.com) could not be extracted (JS-rendered shell). Lifecycle, config-file support, and governance for Cloud9 are unverified here; only product-page facts were used.
- Gitpod Classic docs unreachable (JS app); Ona (its successor product) used instead. Heritage claims about Gitpod are context only, not asserted.
- Replit's current workspace internals (shell, Nix config, classic "Repl" lifecycle) not directly verified; the fetched Project Editor page was JS-heavy. Final-document claims about Replit are limited to what the docs index and page summaries state.
- Deprecation/availability status of AWS Cloud9 in 2026 not asserted (no banner observed on the fetched page; docs unreachable).
- No numeric limits, quotas, defaults, or timing values from any product were carried into the final document.
- Older/regional cloud IDEs (Codeanywhere, Koding, Google Cloud Workstations, GitLab Web IDE) not fetched; used only as unsampled market context.

## Final Synthesis

A Cloud IDE is a development environment product whose defining structure is a **managed remote workspace** (code + toolchain + runtime, provisioned and lifecycle-managed by the product on remote or cluster compute) that the developer reaches through a **client-delivered editing surface** (browser IDE or attached desktop editor) and on which **execution happens remotely** (terminal, build/run, preview of served ports). The market evolved through three eras — hosted browser IDE, containerized cloud development environment, agentic environment platform — and the L0 triple survives all three; everything else (dev files, prebuilds, governance, collaboration, AI) is common mature structure, variant posture, or vendor detail. The two live seams are: (1) local IDEs extending remote connections (mechanism convergence, locus test resolves it), and (2) the Dev Container / Workspace Platform leaf (same config format, different hosting locus — flagged for joint review). The Type name "Cloud IDE" should be read alongside its modern synonym "cloud development environment (CDE)".
