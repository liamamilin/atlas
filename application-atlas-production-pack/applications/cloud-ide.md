# Cloud IDE

## Overview

A **Cloud IDE** is a development environment whose code, toolchain, and runtime live on remote compute that the product provisions and manages, while the developer works through a delivered editing surface — a browser-based IDE or a desktop editor attached to the remote environment — and runs code on that remote machine rather than on their own.

The defining core is small:

```text
Managed remote workspace   (source code + tools + runtime, lifecycle-managed by the product)
└── Client-delivered editor   (browser IDE, or desktop editor attached over a managed connection)
    └── Remote execution      (terminal, build, run, debug on the workspace)
```

Everything else commonly associated with the category — container images, environment-definition files, prebuilt environments, port forwarding, organization governance, real-time collaboration, AI assistance — is standard capability that mature products add, not what makes the product a Cloud IDE. The category is also widely known as a **cloud development environment (CDE)**; older products were marketed simply as "cloud IDEs", and the newest ones position themselves around AI agents built on top of the same environment substrate.

If the environment moves onto the developer's own machine, the product becomes a local IDE or a dev-container tool. If the editing surface disappears and only remote compute remains, it becomes remote machine management. If the runtime disappears and only editing remains, it becomes a web-based code editor. The three-part core is what holds the Type together.

## Users & Context

The primary user is a **software developer** who wants to edit, build, run, and debug a project without configuring a local machine for it.

Typical situations:

- **Onboarding**: a developer joining a project gets a fully configured environment in minutes instead of spending hours installing toolchains locally.
- **Inconsistency avoidance**: every team member works in an environment defined by the project, reducing "works on my machine" divergence.
- **Constrained or shared machines**: developers on locked-down laptops, Chromebooks, or machines without the required toolchain still get a full development experience.
- **Project isolation**: one developer keeps several workspaces, each isolated for a different project or task.
- **Contribution and review**: occasional contributors or reviewers open a ready-made environment for a repository branch or pull request without any local setup.

Secondary users:

- **Team leads / platform engineers**: define the standard environment for a project so everyone gets the same one.
- **Organization administrators**: control who can create workspaces, what resources they may consume, what they may connect to, and what the spend is.
- **Educators and learners** (in consumer-oriented products): run code in a browser with zero setup.

The work context is a browser on any machine, or a desktop editor connected to the remote environment. The developer's local machine needs no project tooling; it only needs the client.

## Core Model

### The defining core

**Workspace (managed remote development environment).** The central object. A workspace is a unit of remote compute — a virtual machine, a container, or a pod, depending on the product — that binds together:

- the project's **source code** (typically cloned from a repository, or created from a template),
- the **tools, runtimes, and dependencies** needed to edit, build, run, and debug that code,
- and, in most products, the **editor itself** as an embedded component of the environment.

The product owns the workspace's lifecycle: it creates it, starts and stops it, and deletes it. One developer commonly holds several workspaces, isolated from each other per project or task. This is the structural inversion that distinguishes the Type: in a traditional IDE the environment is bound to the workstation and configured locally; here the environment is a managed remote object and the developer's machine is only a window onto it.

**Client-delivered editing surface.** The editor reaches the workspace over the network. Two client families exist, and both are documented across the sample:

- a **browser IDE** — the editing UI is served by the product and runs in the browser;
- an **attached desktop editor** — a locally installed editor (or editor family) connects to the workspace over a managed remote connection, with the product providing the connection machinery and one-click open.

Some products also support connecting from a command-line tool. Which client is used does not change what the product is; that the editing surface is delivered against a remote workspace does.

**Remote execution.** The workspace includes a terminal and the ability to run the project: install dependencies, build, start the application, debug. Execution happens on the workspace's compute. When the running application needs to be seen, the product exposes it outward — typically by forwarding ports and presenting a preview URL that opens the app from the developer's browser.

### Standard capabilities of mature products

These are present across the researched sample and expected in a modern product, but they are additions to the core rather than its definition:

- **Source-control integration** — create a workspace from a repository branch or commit; authenticate to git providers; commit, push, and work with pull requests from inside the environment.
- **Environment definition as code** — a versioned configuration file committed with the project (container-based definitions, workspace-definition files, or prepackaged stack templates) that makes the environment repeatable for every user of the project. The concept is standard; the file format is implementation detail.
- **Workspace dashboard** — a management surface listing the user's workspaces with status, from which workspaces are created, opened, stopped, and deleted.
- **Port forwarding / preview URLs** — access to the application running inside the workspace, shareable with teammates in some products.
- **Lifecycle controls** — idle timeouts and automatic stopping, retention rules for stopped workspaces, persistent storage that survives stop/start.
- **Startup-time optimization** — prebuilt environment images or cached images so a new workspace starts quickly even for large projects.
- **Editor machinery and personalization** — extensions/plugins, settings sync, and personal dotfiles layered on top of the project-defined environment.
- **Secrets and environment variables** — credentials injected into workspaces at the account, project, or organization level rather than stored in code.
- **Collaboration** — sharing a running environment for pair programming, or team workspaces with shared projects.
- **Organization governance** — enabling the product for a team, cost and usage controls, audit logs, and policy limits on resources and configuration.

### One structure, many implementations

```text
Concept:                    Managed remote workspace
Implementations:            container on a hosted VM, Kubernetes pod,
                            managed cloud instance, SSH-connected server

Concept:                    Client-delivered editor
Implementations:            browser IDE, desktop editor attached over SSH/Gateway,
                            CLI connection

Concept:                    Environment definition
Implementations:            container config file committed to the repo,
                            workspace-definition file, prepackaged stack image
```

A reader who has only seen one implementation — for example, a container-based environment defined by a file in the repository — should still be able to recognize older or differently positioned products from the core: a browser IDE running on a plain cloud instance with a terminal is the same Type with fewer layers.

## How It Works

### Create a workspace

```text
Choose a source
  (repository branch/commit, project template, or blank)
→ the product provisions remote compute
→ the environment definition is applied
  (tools, runtimes, dependencies installed — or a prebuilt image is attached)
→ source code is cloned into the workspace
→ the workspace becomes running and reachable
```

Creation is the moment where the product's value concentrates: the developer does nothing locally, and the resulting environment matches the project's definition. Products that support prebuilds attach an already-prepared image so this step takes seconds instead of minutes.

### Enter and work

```text
Open the workspace from the dashboard
  (in the browser, or by attaching a desktop editor)
→ edit files in the delivered editor
→ use the workspace terminal to install, build, run
→ the running app is reachable through a forwarded port / preview URL
→ debug against the remote runtime
```

This edit–run loop is the daily interaction. The developer's local machine never runs the project; the loop simply happens on the remote workspace, viewed through the client.

### Persist work

```text
Commit and push changes to source control
  (from the editor's source-control UI or the terminal)
→ committed work is safe outside the workspace
→ uncommitted work lives in workspace storage
```

Workspace storage persists across stop/start in persistent-workspace products. The durable home for finished work, however, is the source-control system — which is why committing is the load-bearing habit of this Type (see Rules).

### Pause, resume, delete

```text
Stop the workspace
  (compute is released; storage is retained per the product's rules)
→ resume later and find the environment as it was left
→ delete when done
  (or let retention/idle policies delete it automatically)
```

Ephemeral-style products invert the emphasis: the environment is expected to be short-lived and is recreated from its definition on demand, with only source-control state treated as durable.

### Operate as a team or organization

Administrators define who may create workspaces, what machine sizes and configurations are allowed, how long stopped workspaces are kept, what the usage costs and limits are, and which resources workspaces may reach. Platform engineers publish the standard environment definition with the project so that every workspace created from it starts identically.

## Interfaces

### Workspace dashboard

The entry surface. Lists the user's workspaces with status (running/stopped), the project each belongs to, and creation options (from repository, from template, blank). Primary actions: create, open, stop, delete, and adjust workspace settings such as machine size or region where offered.

### Editor

The main working surface, delivered in the browser or through an attached desktop editor. Typical anatomy: file tree, editor tabs, integrated terminal, source-control panel, command palette, extension/plugin support. The editor is functionally the same surface a developer knows from local IDEs; the difference is invisible until the terminal is used — there it is the remote machine answering.

### Preview / ports surface

Shows the ports the workspace is serving and the URLs through which the running application can be opened, with visibility controls (private, organization, public) in some products. Purpose: see and share the in-progress application without deploying it.

### Settings and personalization

User-level preferences: default editor choice, default region for data residency, idle timeout, dotfiles/settings sync. Distinct from the project's environment definition — personal preference is layered on top of the shared environment, not mixed into it.

### Administration console

Organization-level surface: enablement, member access, cost and usage reporting, policy limits (machine types, timeouts, retention, base images, port visibility), secrets, and audit logs. Present in organization-oriented products; absent or minimal in consumer-oriented ones.

## Important Rules / Behaviors

- **The workspace is the machine.** Commands, builds, and the running application all execute remotely. Local tooling is irrelevant to the project; the local machine only renders the client.
- **Committed vs uncommitted state is the critical split.** Work pushed to source control survives anything. Uncommitted work exists only in workspace storage and is subject to the product's retention and deletion rules — including automatic deletion of inactive workspaces. Some products provide recovery paths (exporting changes to a branch), but the reliable rule is: commit early, push often.
- **Stopped is not deleted.** Stopping releases compute (and its cost) while keeping storage; deleting destroys the workspace. Retention policies can delete stopped workspaces automatically after a configured period.
- **The environment is reproducible; the person is not erased.** The project's environment definition determines the shared baseline; personal dotfiles, settings, and extensions are layered on per user. Rebuilding the environment applies definition changes but is a deliberate operation, because it resets the installed state.
- **The running app is not on localhost.** Applications are reached through forwarded ports and preview URLs, with visibility that may be governed by policy.
- **Workspaces typically run Linux.** Across the researched sample, the remote environment is a Linux machine regardless of the developer's local operating system; projects requiring other platforms are not served by this Type.
- **Governance can bind the environment.** Organizations may restrict machine sizes, idle timeouts, retention, base images, port visibility, and even which editor clients may connect; usage may be billed to the organization rather than the individual.
- **Cost accrues with running compute.** Because the product runs real machines, idle timeouts and stopping are first-class behaviors, and usage-based billing or quotas are common.

## Variants

- **Hosting posture** — fully vendor-hosted service; self-hosted platform installed on the organization's own cluster; hybrid (managed control plane with environments in the customer's cloud); connect-to-your-own-server mode where the product attaches its IDE to an existing machine.
- **Bundling posture** — standalone product; environment bundled into a source-hosting platform (create a workspace directly from a repository); environment bundled into a cloud provider's console as the IDE for that cloud.
- **Persistence philosophy** — persistent workspaces (storage survives stop/start; long-lived per project) versus ephemeral environments (recreated per session from the definition; only source control is durable).
- **Audience posture** — consumer/education products optimized for zero-setup first code; professional/enterprise products optimized for standardization, governance, and integration with identity providers.
- **AI posture** — a spectrum in current products: AI assistant installed as an editor extension; AI assistant configurable per workspace; background coding agents that run in the environment on schedules or events; and products repositioned wholesale as AI app-building platforms that still rest on the same workspace substrate.
- **Publish/deploy coupling** — some products extend from development to hosting, letting the user publish the built application to the vendor's cloud from the same surface; others stop at the environment boundary.
- **Client surfaces** — browser-only; browser plus attached desktop editors; plus CLI; a few consumer products add desktop and mobile apps as additional windows onto the same workspace.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Integrated Development Environment / IDE | nearest sibling | A local IDE binds editor, code, and runtime to one workstation that the user configures; a Cloud IDE binds them to a product-managed remote workspace. Desktop IDEs can attach to remote machines via extensions, but the Type question is whether the product itself provisions and lifecycle-manages the remote environment. |
| Code Editor | sibling | Editing-focused local tool without a managed runtime/build environment; a Cloud IDE's defining addition is the managed remote workspace with execution. |
| Dev Container / Workspace Platform | closest modern seam | Shares the same configuration substrate (container-based environment definitions). The distinction is locus: a dev-container platform defines and provisions environments that may run on the developer's own machine and be consumed through any editor; a Cloud IDE hosts and operates the remote compute and delivers the editing-and-execution experience as a service. Products in this space increasingly do both — flagged for joint review. |
| Web Development IDE | name-collision only | "Web" there refers to the target domain (building web applications) and is usually local; "cloud" here refers to where the environment runs. Different axes, not the same Type. |
| Source Code Hosting Platform | adjacent, often bundled | Hosts repositories and pull requests; some hosting platforms bundle a Cloud IDE. Hosting code is not the same as providing a managed development environment. |
| AI Coding Assistant | adjacent | Augments editing inside an environment; the Cloud IDE is the environment it plugs into. |
| AI Coding Agent | adjacent, converging | Performs development work autonomously; agent platforms run agents inside cloud environments. The environment substrate and the agent are distinct layers, even when one vendor sells both. |
| Web-based code editor (e.g., lightweight in-browser file editors) | boundary case | Offers editing and commits in a browser without a managed runtime or workspace; without remote execution it is not a Cloud IDE. |
| PaaS Management Console | adjacent | Manages deployment targets and cloud resources; a Cloud IDE is the developer's working environment, even when bundled alongside such a console. |

## Representative Products

- **GitHub Codespaces** — repository-attached cloud development environments built on dev containers, hosted by the platform; browser, desktop-editor, and CLI clients; strong organization governance.
- **Eclipse Che** — Kubernetes-native, self-hosted open-source platform delivering container-based cloud development environments defined by workspace-definition files; the terminology anchor for "CDE".
- **AWS Cloud9** — classic cloud IDE bundled with a cloud provider's console; browser editor, debugger, and terminal on a managed cloud instance or an SSH-connected server; the pre-container-era structural reference.
- **Ona (Gitpod lineage)** — cloud-environment-native vendor now positioned around background coding agents; ephemeral, prebuilt, dev-container-defined environments with pluggable editor clients and managed or customer-VPC compute.
- **Replit** — consumer/education-rooted browser development platform, now an AI-first build-and-publish product; the workspace/editor/preview substrate illustrates the consumer pole and the category's drift.

## Sources

Research date: **2026-09-07**

- GitHub Codespaces documentation — https://docs.github.com/en/codespaces and https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces
- Eclipse Che documentation — https://www.eclipse.org/che/docs/stable/discover/what-is-che/
- AWS Cloud9 product page — https://aws.amazon.com/cloud9/
- Ona documentation — https://ona.com/docs and https://ona.com/docs/ona/editors/overview
- Replit documentation — https://docs.replit.com/ (root, documentation index, and Project Editor overview)

> Sourcing limitations: the AWS Cloud9 operational documentation site and the Gitpod (Gitpod Classic) documentation site returned JavaScript-only shells and could not be extracted; Cloud9 claims are limited to its official product page, and the Gitpod lineage is represented by its successor product's documentation. Replit's Project Editor page was largely script scaffolding; Replit claims are limited to its documentation index and page summaries. Precise operational values (machine sizes, retention windows, quotas, defaults) observed during research were deliberately kept out of this document; they are recorded in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample breadth check are recorded in the paired Research Notes.
