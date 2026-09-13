# Infrastructure-as-Code Platform

## Overview

An **Infrastructure-as-Code Platform** is a system in which infrastructure resources — compute, network, storage, and higher-level services on cloud or on-prem platforms — are declared in machine-readable, versionable files, and the platform itself creates, changes, and destroys those resources by driving the target platforms' APIs, while holding a persistent record of the resources it manages.

The defining core is three structures held together:

```text
Infrastructure declared as code
  (versionable files describing what should exist — the source of truth)
└── bound to
    Managed lifecycle execution
      (the platform computes and executes create / update / destroy
       operations against the target platforms' APIs)
    └── tracked in
        The managed-resource record
          (persistent bindings between each declared resource and the
           real object it created or adopted)
```

Remove any one and the category collapses: without declarations it is ad-hoc API scripting; without execution it is a diagramming or documentation tool; without the managed-resource record it is one-shot provisioning — able to create resources but unable to answer "what did I create," re-apply incrementally, or destroy what it manages as a set.

Everything else commonly associated with the category — plan/preview steps, provider ecosystems, reusable modules, drift detection, remote state, collaboration consoles, policy checks — is widespread in current products but is not what makes a product an infrastructure-as-code platform. A first-generation template service with none of the modern collaboration layer, and a bare CLI tool with a local record file, both satisfy the defining core completely.

The category's central promise is that infrastructure has a **source of truth in code and a managed lifecycle**: the same declaration can be applied repeatedly, changes are computed as diffs against what already exists, and removing a resource from the code removes the real object.

## Users & Context

The primary users are the people responsible for provisioning and evolving infrastructure:

- **Infrastructure / platform engineers** — author the declarations (networks, machines, load balancers, managed services), package them into reusable units, and own the record and its backend.
- **DevOps / SRE engineers** — wire declarations into version control and pipelines, execute changes through preview-and-apply flows, and handle drift and failures.
- **Application teams (secondary)** — consume infrastructure through modules and self-service workflows that platform teams expose; they typically do not touch the record directly.

Secondary concerns fall to the same engineering organization: security and compliance teams review proposed changes through policy checks in mature deployments; secrets the platform needs (cloud credentials) are managed through vault integrations or identity mechanisms so they never sit in plaintext.

The work environment is a split surface: **authoring happens in code repositories and editors**, while **execution happens through a command-line tool or a collaboration console** that shows proposed changes, runs, and the managed-resource record. In team settings the record lives in a shared backend, and changes flow through pull requests: propose a change, see the computed plan on the pull request, review, merge, apply.

## Core Model

### The Defining Core

**1. Infrastructure declared as code.** The user writes machine-readable declarations that describe the infrastructure that should exist — virtual machines, networks, subnets, load balancers, DNS records, databases, message queues, and higher-level services. The essential property is that declarations describe **the desired end state, not the steps**: a declaration says "a load balancer with these listeners exists," and the platform works out how to create or change it. Declarations are plain files: they can be versioned, reviewed, reused, and shared like any other code, and the history of the files is the history of the infrastructure.

**2. Managed lifecycle execution.** The platform is the actor that turns declarations into real infrastructure. It translates each declared resource into calls against the target platform's API — creating objects that do not exist, changing objects whose declared properties differ, and destroying objects that the declaration no longer describes. Execution is computed, not scripted: the platform derives the operations and their order from the declaration and from what it already manages, and it can run the same declaration again safely.

**3. The managed-resource record.** The platform holds a persistent record that binds each declared resource to the real object it created (or later adopted). This record is what makes the lifecycle *managed*: it lets the platform compute what changed since the last run, apply only the differences, destroy exactly the objects it tracks when they leave the declaration, and detect when the real world has been changed by other means. The record takes different physical forms across products — a file the team stores in a backend, a stack held by a cloud service, objects in a control plane — but the binding function is constant.

### Standard Capabilities

Mature products commonly add the following. They make the core practical at scale but do not define the Type.

- **Preview step.** Before executing, the platform computes and displays the proposed operations — what will be created, updated, or destroyed — usually as a diff against the current managed state. Some products make this a separate command; some make it an optional artifact; some reconcile continuously. The preview-before-change discipline is near-universal.
- **Providers.** Pluggable adapters that translate declarations into a specific platform's API calls. One tool manages many platforms through different providers; public registries distribute them.
- **Reusable modules.** Declarations packaged into shareable, versioned units — a standard network, a standard database — consumed from public or private registries.
- **Dependency ordering.** The platform derives the order of operations from declared relationships between resources (a machine needs its subnet to exist first) and runs independent work in parallel.
- **Drift detection.** Comparing actual infrastructure against the recorded or declared state, because resources get changed outside the platform — through cloud consoles, other tools, or manual fixes. Products surface drift as reports, scheduled checks, or automatic reconciliation.
- **Import/adoption.** Bringing externally-created resources under management by binding them into the record, so existing infrastructure can be taken over without recreating it.
- **Remote record storage and locking.** The record is stored in a shared backend with concurrency protection, so team members do not corrupt it by running changes simultaneously.
- **Version-control workflow.** Declarations live in repositories; changes are proposed as pull requests; the platform posts computed plans to the pull request and applies after merge.
- **Outputs.** Values produced by the managed resources (addresses, IDs, connection strings) exported for other systems or other stacks to consume.
- **Per-environment parameterization.** The same declaration instantiated for development, staging, and production, with variables supplying the differences.
- **Command-line and API surfaces.** The engine is automation-first: everything the console does can be done programmatically, so pipelines and other systems can drive the same lifecycle.

### One Structure, Many Implementations

The core model is conceptual. Products realize each concept differently, and a reader who has only seen one implementation should still be able to recognize the others:

```text
Concept:                 Declaration substrate
Implementations:         a dedicated declarative language; general-purpose
                         programming languages with resource SDKs;
                         JSON/YAML templates; Kubernetes custom resources

Concept:                 Managed-resource record
Implementations:         a state file stored locally or in a remote backend;
                         a stack held by the cloud service itself;
                         resource objects in a control plane

Concept:                 Execution model
Implementations:         run-based (compute a plan, apply on demand or on
                         merge); continuously reconciling (a control plane
                         watches declared resources and corrects drift)

Concept:                 Preview
Implementations:         a plan command; a preview diff; a change set
                         created and executed separately; continuous
                         reconciliation with visible diffs
```

## How It Works

### Author the declaration

An engineer writes declaration files describing the infrastructure for a piece of the estate — typically in a version-controlled repository. Declarations are organized into reusable modules and parameterized so the same module serves multiple environments. Before anything runs, the platform needs two connections: the providers for the target platforms, and the location of the managed-resource record.

### Preview the change

```text
Read the declaration
→ compare it against the managed-resource record
→ compute the operations needed (create / update / destroy)
→ display the proposed changes for review
```

The preview is the discipline's safety surface: the user sees exactly what will happen — including explicit destructions — before anything is touched. In mature team workflows this preview is posted automatically to a pull request, so review of infrastructure changes looks like review of code.

### Apply

On approval, the platform executes the proposed operations in dependency order, calling the target platforms' APIs and updating the record as objects are created, changed, or destroyed. Partial failures are recoverable because the record is updated transactionally as work proceeds; a re-run resumes from the recorded state.

### Iterate and evolve

Infrastructure changes by editing the declaration and repeating the preview-apply loop. Because the record remembers what the platform manages, an edit produces a minimal diff — changing one property updates one property — and removing a resource from the declaration destroys the object it tracked. The version-control history of the declarations is the audit trail of the infrastructure.

### Adopt and reconcile

Resources created outside the platform (by consoles, other tools, or by hand) can be imported into the record so they come under management. When the real world drifts — someone changed a resource out-of-band — the platform detects the difference against its record; the team then either updates the declaration to accept the change or re-applies to revert it. Products differ in whether they refresh their view of reality automatically before each run or require an explicit refresh; both behaviors exist in the market.

### Destroy

Tearing down is a first-class operation: the platform destroys exactly the objects its record tracks — nothing more — and clears the bindings. In the service-held form, deleting the stack deletes all resources in it.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Declaration files (authoring surface)

Where the infrastructure is defined.

- declaration files in the product's language or format, organized into modules, under version control
- primary actions: write/modify declarations, review diffs, publish module versions

### Command-line tool

The engine's primary surface.

- commands to initialize against providers and the record backend, compute and show plans, apply or destroy, import resources, inspect and manipulate the record
- primary actions: preview a change, execute it, adopt existing resources, inspect managed state

### Collaboration console (team and platform editions)

The web surface over the engine in team settings.

- workspaces or projects (one declaration bound to one environment and one record), run history with plans and logs, approval gates, drift reports, policy-check results, role-based access
- primary actions: trigger or approve runs, review proposed changes, inspect the managed-resource inventory, manage access and policy

### API

Programmatic access mirroring the console and CLI, consumed by pipelines and automation.

### Registries

Public or private catalogs of providers and modules for distribution and reuse.

## Important Rules / Behaviors

### The record is the authority on what is managed

The platform manages exactly what its record binds — no more, no less. Resources created outside the platform are invisible to it until imported; resources it created are fully its responsibility, including destruction. This one-to-one binding between declaration and real object is what keeps the lifecycle coherent, and products treat violations of it (two declarations binding the same object) as errors.

### Preview before execution, with destroys explicit

The computed plan distinguishes creates, updates, and destroys, and destructions are shown explicitly because they are the dangerous class. Execution follows the reviewed plan.

### Re-application converges

Applying the same declaration again changes nothing if reality already matches it. This idempotent behavior is what makes repeated runs, drift correction, and environment replication safe.

### Order is derived, not scripted

The platform derives operation order from declared dependencies. Authors state what depends on what (or express relationships structurally); they do not write step-by-step procedures. This is the declarative contract that separates the category from plain automation scripts.

### Concurrency is guarded

Two simultaneous changes against the same record can corrupt it, so shared record backends provide locking or serialized runs. Solo local use does not need this; teams do.

### The record is sensitive

The record can contain resource attributes that are secret-like (passwords, keys, connection strings), and it is itself the map of the estate. Products provide encryption of sensitive values in the record, marking of sensitive outputs, and integration with external vaults; storing the record in an unprotected shared location is treated as a defect.

### Drift is expected and surfaced

Real infrastructure gets changed outside the platform — consoles are too convenient. Products differ in whether they detect drift automatically, on schedule, or on demand, and whether they auto-reconcile; but every mature product has an answer to "the world changed behind my back."

## Variants

Common forms the Type takes; each keeps the defining core intact.

- **By declaration substrate** — a dedicated declarative language; general-purpose programming languages with resource SDKs (logic and loops come from the language, the resource model stays declarative); JSON/YAML templates; Kubernetes custom resources.
- **By record substrate** — a team-managed state file in a local or remote backend; a stack record held by the cloud service itself; objects in a continuously reconciling control plane.
- **By execution model** — run-based (plan/apply on demand, on a schedule, or triggered by version-control events) versus continuously reconciling (the control plane watches declared resources and corrects divergence automatically).
- **By scope** — multi-cloud tools that manage many platforms through providers; single-cloud native services operated by the cloud provider itself; on-prem/virtualization targets; Kubernetes-mediated control planes.
- **By packaging** — an open-source engine alone; an engine plus a vendor-operated collaboration service; an engine plus third-party operations platforms (a recognized market segment of team/automation layers built around the major engines); a cloud-native service where the whole loop is the provider's own offering.
- **By operations depth** — plain engine; plus policy-as-code checks on plans; plus role-based access, audit logging, secrets handling, self-hosted runners/agents, drift jobs, and estate-wide reporting in enterprise editions.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Configuration Management | closest sibling, often blurred | configuration management enforces the *interior state of running systems* (packages, files, services) and keeps them converged over time; infrastructure-as-code manages the *lifecycle of infrastructure resources* (create/change/destroy machines, networks, managed services). The visible seam: a configuration tool can create cloud resources through API modules, but holds no record of what it created — no managed lifecycle. Products blur it from both sides; the primary managed object decides |
| Cloud Management Platform | adjacent, name-adjacent | a CMP manages the *estate inventory* and its lifecycle through consoles, catalogs, and approvals; an IaC platform manages *code, the record, and runs*. The same product family can appear in both markets; the managed object is the discriminator |
| Infrastructure Automation Platform | umbrella-term neighbor | vendors market broader orchestration suites (configuration management plus workflow plus event-driven automation) as "automation platforms"; the IaC Type is the code-defined infrastructure-lifecycle core within that space |
| Application Deployment Management / Continuous Delivery | pipeline neighbor | deployment tools move *application artifacts* through environments; IaC platforms provision the *infrastructure resources* those environments run on. They interlock (pipelines trigger IaC runs) but the managed object differs |
| Kubernetes Management Platform | adjacent | managing clusters and their workloads is a different Type; a Kubernetes-native control plane that manages *external cloud resources* through custom resources is a variant form of IaC, not cluster management |
| Secrets Management | integration neighbor | IaC declarations and records carry credentials; vault products store and govern them. IaC platforms consume vaults; they do not provide vault services as their core |
| IT Change Management (ITSM) | process-layer neighbor | the ITSM discipline governs *whether and how* changes may happen; the IaC platform is execution machinery. Policy checks on plans are where the two interlock |
| Server Management Platform | adjacent | centers on operational oversight of servers (inventory, health, patching); IaC platforms provision and change infrastructure rather than observe it |

The two most important seams: **vs Configuration Management** (resource lifecycle vs system interior — the market's most persistent blur) and **vs Cloud Management Platform** (code/state/runs vs estate inventory — the two product families are frequently confused because both speak of "managing cloud infrastructure").

## Representative Products

- **Terraform** (HashiCorp) — the category-defining multi-cloud tool: a dedicated declarative language, a state-file record with remote backends, a large provider registry, and a vendor-operated collaboration layer for teams
- **OpenTofu** (Linux Foundation) — the open-source fork of Terraform; evidence that the engine model is a community standard rather than a vendor artifact, and the namer of the third-party operations-layer segment
- **Pulumi** — infrastructure declared in general-purpose programming languages (with a YAML option), same record-and-diff lifecycle, with a hosted collaboration backend
- **AWS CloudFormation** — the platform-native pole: the cloud provider's own template-and-stack service, where the record is held by the service and preview takes the form of change sets

Variant anchors checked during research: a Kubernetes-native control-plane framework (Crossplane) for the continuously-reconciling form, and a configuration-management tool's cloud modules (Ansible) for the boundary position that lacks the managed-resource record.

## Sources

Research date: **2026-09-08**

- Terraform — "What is Terraform?"; State; Purpose of State — https://developer.hashicorp.com/terraform/intro , https://developer.hashicorp.com/terraform/language/state , https://developer.hashicorp.com/terraform/language/state/purpose
- OpenTofu — Getting started; "What are TACOS?" — https://opentofu.org/docs/intro/ , https://opentofu.org/docs/intro/tacos/
- Pulumi — Concepts; State & backends — https://www.pulumi.com/docs/iac/concepts/ , https://www.pulumi.com/docs/iac/concepts/state-and-backends/
- AWS CloudFormation — What is CloudFormation?; Change sets; Drift detection — https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html , https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html , https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html
- Crossplane — What's Crossplane? — https://docs.crossplane.io/latest/whats-crossplane/
- Ansible (Red Hat) — How Ansible works — https://www.ansible.com/overview/how-ansible-works
- Scalr — product page — https://www.scalr.com/

> Sourcing limitations: the Ansible community documentation site was rate-limited on the research date, so Ansible evidence rests on the vendor's official overview page only, and no deep operational claims are made about it. The collaboration layers of the sampled tools were evidenced at capability level (intro/product pages), not at detailed feature level; third-party operations platforms are evidenced through one vendor plus the engine project's own category definition. Accordingly, no precise limits, defaults, or edition-specific mechanics are stated in this document. Detailed observations, the cross-product comparison, and the historical-sample check are recorded in the paired Research Notes.
