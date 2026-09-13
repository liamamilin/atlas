# Research Notes — Infrastructure-as-Code Platform

Research date: 2026-09-08
Slug: `infrastructure-as-code-platform` (DIRECTORY §14 IT, Cloud & Infrastructure)

## Research Goal

Understand what an Infrastructure-as-Code (IaC) Platform is as an Application Type: its core objects, its characteristic workflow, its lifecycle semantics, the collaboration/operations layer that the word "platform" points at, and — critically — its boundaries against Configuration Management, Cloud Management Platform, deployment tooling, and Kubernetes-native control planes.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: an IaC platform lets users declare infrastructure resources (compute, network, storage, cloud services) in machine-readable files, then creates/changes/destroys those resources through platform APIs, holding a record of what it manages.
- Likely users: infrastructure / platform / DevOps engineers, SREs.
- Nearest neighbors: Configuration Management (interior state of running systems — sibling pass already processed), Cloud Management Platform (estate inventory + console lifecycle — sibling pass already processed and flagged IaC-operations products as belonging HERE), Infrastructure Automation Platform (umbrella leaf, unprocessed), Application Deployment Management / Continuous Delivery (app artifacts, not infrastructure resources), Kubernetes Management (cluster operations).
- Known seam from the sibling passes: the CMP pass recorded the discriminating test "managed object = code/state/runs (IaC) vs estate inventory + lifecycle (CMP)" and recommended applying it in this pass. The Configuration Management pass recorded "resource lifecycle vs system state" as the IaC seam.
- Unknowns going in: is the state record definitional or merely universal? Is the plan/preview step definitional? Where does the collaboration layer (Terraform Cloud / Pulumi Cloud / TACOS) sit? Does the platform-native pole (cloud-provider template services) fit the same core?

## Research Questions

1. What is the core object model? (declarations, resources, state, providers, modules/stacks)
2. What is the characteristic workflow? (author → preview → execute → iterate → destroy)
3. What is "state" and why does it exist? Is it definitional or an implementation choice?
4. How do providers/adapters let one tool manage many platforms?
5. What does the collaboration/operations layer add (workspaces, runs, RBAC, policy, drift jobs)?
6. What interfaces exist (CLI, web console, API, VCS-driven)?
7. Which rules matter (locking, drift, secrets in state, destroy semantics, import)?
8. Where are the boundaries: vs Configuration Management, vs CMP, vs deployment tools, vs Kubernetes-native control planes?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer levels:

| Product | Pole | Why selected |
|---|---|---|
| Terraform (HashiCorp) | category-defining multi-cloud CLI + SaaS collaboration layer (HCP Terraform) | the reference implementation of the declarative-DSL + state-file model |
| OpenTofu (Linux Foundation) | open-source fork of Terraform | confirms the Terraform model is not vendor-specific; documents the TACOS category |
| Pulumi | general-purpose-language IaC + Pulumi Cloud | different authoring philosophy (real programming languages), same state/plan model |
| AWS CloudFormation | platform-native pole (cloud provider's own IaC service) | template + stack model; state held by the service, not a user-managed file |

Boundary/variant anchors (not core samples):

- **Crossplane** — Kubernetes-native control-plane framework; continuous-reconciliation pole.
- **Ansible** (Red Hat) — configuration-management tool whose cloud modules create resources via APIs without a managed-resource record; the canonical straddler for the Configuration Management seam.
- **Scalr** — third-party IaC operations platform ("TACOS"); evidence for the operations-layer variant; also the product the CMP pass flagged as IaC, not CMP.

## Sources

Tier 1 (official operational documentation), fetched 2026-09-08:

- Terraform — "What is Terraform?" (intro) — https://developer.hashicorp.com/terraform/intro
- Terraform — State (overview) — https://developer.hashicorp.com/terraform/language/state
- Terraform — Purpose of Terraform State — https://developer.hashicorp.com/terraform/language/state/purpose
- OpenTofu — Getting started / "What is OpenTofu?" — https://opentofu.org/docs/intro/
- OpenTofu — "What are TACOS?" — https://opentofu.org/docs/intro/tacos/
- Pulumi — Concepts — https://www.pulumi.com/docs/iac/concepts/
- Pulumi — State & backends — https://www.pulumi.com/docs/iac/concepts/state-and-backends/
- AWS CloudFormation — What is CloudFormation? (Welcome) — https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html
- AWS CloudFormation — Update stacks using change sets — https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html
- AWS CloudFormation — Drift detection — https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html
- Crossplane — Welcome; What's Crossplane? — https://docs.crossplane.io/latest/ , https://docs.crossplane.io/latest/whats-crossplane/
- Ansible (Red Hat) — How Ansible works — https://www.ansible.com/overview/how-ansible-works

Tier 2 (official product/positioning pages):

- Scalr — homepage / product positioning — https://www.scalr.com/

Access limitations:

- docs.ansible.com returned HTTP 429 (rate-limited) on the research date; Ansible evidence relies on Red Hat's official "How Ansible works" page only. No deep operational claims about Ansible are made.
- Spacelift and env0 were not fetched; Scalr stands in for the third-party TACOS pole (its own positioning explicitly frames itself as a Terraform Cloud replacement).
- HCP Terraform deep docs (workspaces/runs internals) not fetched; collaboration-layer evidence for Terraform comes from the intro page's collaboration section.
- AWS CDK not fetched; no operational claims about it are made anywhere.

## Product Observations

### Terraform (HashiCorp) — evidence layer A

- Self-definition: "an infrastructure as code tool that lets you build, change, and version cloud and on-prem resources safely and efficiently"; define "cloud and on-prem resources in human-readable configuration files that you can version, reuse, and share"; "a consistent workflow to provision and manage all of your infrastructure throughout its lifecycle."
- Scope of managed objects: "low-level components like compute, storage, and networking resources, as well as high-level components like DNS entries and SaaS features."
- Execution substrate: "creates and manages resources on cloud platforms and other services through their application programming interfaces (APIs). Providers enable Terraform to work with virtually any platform or service with an accessible API." Thousands of providers in the Registry (AWS, Azure, GCP, Kubernetes, Helm, GitHub, Datadog, …).
- Core workflow (vendor-named): **Write → Plan → Apply**. Plan = "an execution plan describing the infrastructure it will create, update, or destroy based on the existing infrastructure and your configuration." Apply = "performs the proposed operations in the correct order, respecting any resource dependencies." Resource graph determines dependencies; non-dependent resources created in parallel.
- State: "keeps track of your real infrastructure in a state file, which acts as a source of truth for your environment. Terraform uses the state file to determine the changes to make to your infrastructure so that it will match your configuration." State overview: "Terraform must store state about your workspace's managed infrastructure and configuration… uses your workspace's state to map real world resources to your configuration." Primary purpose: "store bindings between objects in a remote system and resource instances declared in your configuration."
- State necessity (state/purpose page): "State is a necessary requirement for Terraform to function." Mapping to the real world (config → real object ID); metadata (dependency order for destruction); performance cache (explicitly "the most optional feature of Terraform state"); syncing (remote state + locking so teams operate on the same objects).
- State mechanics: default local file (`terraform.tfstate`); remote backends recommended for teams; locking to avoid concurrent runs; one-to-one binding between resource instances and remote objects; `terraform import` to adopt externally-created objects; `terraform state rm` to "forget"; refresh before operations to update state with real infrastructure.
- Declarative posture: "configuration files are declarative, meaning that they describe the end state of your infrastructure"; "Terraform takes an immutable approach to infrastructure."
- Modules: "reusable configuration components called modules that define configurable collections of infrastructure"; public Registry + private registry.
- Collaboration layer (HCP Terraform): "runs Terraform in a consistent, reliable environment and provides secure access to shared state and secret data, role-based access controls, a private registry for sharing both modules and providers, and more."

### OpenTofu (Linux Foundation) — evidence layer A

- Self-definition mirrors Terraform's almost verbatim ("an infrastructure as code tool that lets you define both cloud and on-prem resources in human-readable configuration files…"), with the same Write → Plan → Apply workflow, state file as "source of truth," declarative end-state files, resource graph, modules, and providers ("thousands of providers" in a public registry).
- Governance: a Linux Foundation project (LF Projects, LLC); docs carry MPL-2.0 licensing notices; positions itself as a migration path from Terraform.
- TACOS definition (official): "TF Automation and Collaboration Software (TACOS) are platforms which allow teams to manage and orchestrate OpenTofu execution. They offer a wide variety of services to provide a streamlined and collaborative experience." Both open-source and commercial TACOS exist; many support OpenTofu directly.
- CLI workflows "alone or with cloud backends"; cloud backend = "runs OpenTofu in a consistent, reliable environment and provides secure access to shared state and secret data, role-based access controls, a private registry."

### Pulumi — evidence layer A

- Self-definition: "a modern infrastructure as code platform. It uses existing programming languages—TypeScript, JavaScript, Python, Go, .NET, Java, and markup languages like YAML—and their native ecosystems to interact with cloud resources. A downloadable CLI, runtime, libraries, and a hosted service work together to deliver a robust platform for provisioning, updating, and managing cloud infrastructure."
- Architecture: program (in a general language) → language SDK (bindings per resource type per provider) → CLI drives a deployment engine → "the deployment engine computes the set of operations needed to drive the current state of your infrastructure into the desired state expressed by your program."
- Object model: programs declare **resources** (objects whose properties correspond to desired state); properties wire dependencies between resources; **stacks** are "an isolated and configurable instance of your program" — the deployment-environment unit (dev/staging/prod); **projects** contain the program; **outputs** export values from the stack.
- State: "Pulumi stores metadata about your infrastructure so that it can manage your cloud resources. This metadata is called state. Each stack has its own state, and state is how Pulumi knows when and how to create, read, delete, or update cloud resources."
- Backends: Pulumi Cloud (hosted, default; also self-hostable) or DIY backends (S3, Azure Blob, GCS, S3-compatible, PostgreSQL, local filesystem). State stored as transactional **checkpoints** ("records checkpoints early and often… similar to how database transactions work"); checkpoints let Pulumi "diff your program's goal state against the last known update, recover from failure, and destroy resources accurately."
- Refresh semantics: state records what infrastructure looked like after the last up/refresh; preview/up compares recorded state against the declared program; out-of-band changes are NOT automatically reflected (deliberate: performance, explicit control, predictability); `pulumi refresh` syncs state from the cloud; refresh does not modify the program — next `up` reverts external changes unless the program is updated.
- Drift: Pulumi Cloud provides scheduled drift detection + optional remediation (paid editions); CLI-side drift workflow documented (remediation vs adoption).
- Import: "supports importing resources that were already created outside of Pulumi… Resource metadata is imported into your Pulumi state and source code is generated in your chosen language."
- Secrets: encrypted in config and state (transitively); Pulumi Cloud uses server-side HSM by default; DIY backends use chosen encryption providers.
- Collaboration layer (Pulumi Cloud): "a managed backend that stores your state and adds access control, reusable configuration and secrets, policy enforcement, and drift detection for teams"; records "who on your team updated what, and when."

### AWS CloudFormation — evidence layer A (platform-native pole)

- Self-definition: "a service that helps you model and set up your AWS resources… You create a template that describes all the AWS resources that you want (like Amazon EC2 instances or Amazon RDS DB instances), and CloudFormation takes care of provisioning and configuring those resources for you."
- Unit of management: the **stack** — "When you use that template to create a CloudFormation stack, CloudFormation provisions the… resources for you… You can delete the stack just as easily, which deletes all the resources in the stack. By using CloudFormation, you easily manage a collection of resources as a single unit." (The stack IS the managed-resource record; the service holds it — no user-managed state file.)
- Replication/reuse: "Reuse your CloudFormation template to create your resources in a consistent and repeatable manner… provision the same resources over and over in multiple regions."
- Change tracking through code: "the CloudFormation template describes exactly what resources are provisioned and their settings. Because these templates are text files, you simply track differences in your templates to track changes to your infrastructure… you can use a version control system with your templates."
- Preview step: **change sets** — "allow you to preview how proposed changes to a stack might impact your running resources… CloudFormation compares your stack with the changes that you submitted to generate the change set; it doesn't make changes to your stack at this point… you can see which resources CloudFormation will add, modify, or delete… Execute the change set… CloudFormation updates your stack with those changes." Pre-deployment validation checks common failure causes at change-set creation.
- Drift: "users can change those resources outside of CloudFormation… You can use drift detection to identify stack resources to which configuration changes have been made outside of CloudFormation management… A resource is considered to have drifted if any of its actual property values differ from the expected property values… Resolving drift helps to ensure configuration consistency and successful stack operations." Resolution paths include updating resources to match the template or importing.
- Rollback: update failures can be rolled back to original settings.
- Surfaces: console, API, AWS CLI, SDKs.

### Crossplane — evidence layer A (variant anchor)

- Self-definition: "a control plane framework for platform engineering… lets you build control planes to manage your cloud native software… design the APIs and abstractions that your users use to interact with your control planes."
- Control-plane semantics: exposes an API; users declare desired state; "The control plane configures your software, then monitors it throughout its lifecycle. If your software ever drifts from your desired state, the control plane automatically corrects the drift." (Continuous reconciliation, not run-based.)
- Components: **Composition** (custom APIs built as Kubernetes custom resources, realized by pipelines of composition functions in YAML/KCL/Python/Go); **Managed resources** ("ready-made Kubernetes custom resources… an extensive library of managed resources you can use to manage almost any cloud provider, or cloud native software" — e.g., an RDS-instance MR managing AWS RDS); **Operations** (task pipelines: run-once / cron / watch); **Package manager** (providers, functions, configurations).
- Built on Kubernetes; works with Kubernetes tooling; import-existing-resources guide exists.

### Ansible (Red Hat) — evidence layer A (boundary anchor)

- Self-definition: "an open source, command-line IT automation software application… It can configure systems, deploy software, and orchestrate advanced workflows to support application deployment, system updates, and more."
- Model: control node + managed nodes; modules are "resource models of the desired state of the system," executed over SSH (agentless) and removed after execution; idempotent "so that they only make changes to a system when necessary."
- Cloud provisioning straddle: "For automating public clouds and web services, Ansible will also run modules locally and talk directly to their APIs" (AWS/GCP/Azure guides). The overview describes inventory (machines to automate) and credentials — but no persistent record binding declared cloud resources to created objects. Ansible can create cloud resources, but nothing in its model tracks the created-resource set as a managed portfolio (no state file, no stack, no destroy-what-I-created semantics).
- Enterprise layer (Red Hat Ansible Automation Platform): automation controller (WebUI + API based on AWX), automation mesh, event-driven automation, analytics.

### Scalr — evidence layer A for its own positioning (Tier 2; TACOS pole)

- Self-definition: "a cost effective, drop-in replacement for Terraform Cloud, with feature parity and better GitOps support"; "for platform engineers who want to build and manage their platform at scale while enabling developer self-service."
- Operations-layer feature set (all framed around Terraform/OpenTofu workspaces): state management (store state in Scalr or your own bucket), drift detection with notifications/remediation and drift dashboards, PR-native GitOps (apply-before-merge, `/scalr plan` `/scalr apply` slash commands, run summaries on PRs, branch-aware state protection), policy as code (OPA, Checkov), RBAC + SAML/OIDC + audit logging + secrets management, private module/provider registries, provider configurations (centrally managed credentials/OIDC), workflow hooks (pre-init → post-apply phases), self-hosted agents, reports (resource inventory, versions, stale workspaces), inheritance of policies/modules across scopes, per-run pricing.
- Confirms the TACOS category is a real market segment layered over the engines, and that its unit of management is the workspace/run/state — not an estate inventory (the CMP discriminator).

## Cross-product Comparison

| Dimension | Terraform | OpenTofu | Pulumi | CloudFormation | Crossplane | Ansible (cloud modules) |
|---|---|---|---|---|---|---|
| Declaration substrate | HCL files (DSL) | HCL files (DSL) | general-purpose languages + YAML | JSON/YAML templates | Kubernetes custom resources (YAML + composition functions) | YAML playbooks (task-oriented) |
| Managed object | infrastructure resources across platforms via providers | same | cloud resources via providers | AWS resources | cloud + cloud-native resources via providers/MRs | whatever the module touches; no managed-resource record |
| Execution | engine computes create/update/destroy plan → applies via APIs | same | deployment engine drives current → desired state | service provisions/updates stack from template | controllers continuously reconcile | modules execute tasks against APIs; no record of created set |
| Managed-resource record | state file (local/remote backend) | state file | state per stack (checkpoints; Pulumi Cloud or DIY backend) | stack held by the service | Kubernetes etcd (resource objects) | none |
| Preview step | plan (execution plan) | plan | preview / `pulumi up` diff | change set (preview → execute) | n/a (continuous reconciliation; diffs visible in resource state) | `--check` mode (dry-run); not a managed diff |
| Destroy semantics | destroy managed resources; state updated | same | destroy stack resources accurately via checkpoints | delete stack deletes all resources in it | delete resource object → reconciler deletes real resource | no managed-set destroy |
| Drift | refresh + compare; drift handling in platform layer | same | refresh (explicit); scheduled drift detection in Pulumi Cloud | drift detection (expected vs actual; status codes) | automatic drift correction (control-plane semantics) | n/a (config drift is its home turf for machines, not created cloud resources) |
| Import/adoption | `terraform import` | same | import + generated code | import operation (also drift resolution) | import guide | n/a |
| Reuse units | modules + registries | modules + registries | packages/components; converters from other tools | nested stacks / stack sets (not fetched in depth) | compositions + packages | roles/collections |
| Collaboration layer | HCP Terraform (SaaS): shared state, RBAC, private registry | cloud backends (TACOS category) | Pulumi Cloud: state, access control, policy, drift | none needed (AWS service; IAM governs access) | Kubernetes RBAC; platform-engineering framing | Ansible Automation Platform (controller, RBAC) |
| Primary surface | CLI + VCS; console in platform layer | CLI + VCS | CLI + VCS; Pulumi Cloud console | console / CLI / API / SDK | kubectl + Kubernetes tooling | CLI + controller UI |

Reading of the comparison:

- All four core products share: declaration files as source of truth; execution through target-platform APIs; a persistent managed-resource record; a preview/diff step; destroy-as-managed-set; import/adoption; reusable packaging; VCS-based change discipline. These are cross-product commonalities (evidence layer B).
- The managed-resource record takes different FORMS (user-managed state file vs service-held stack vs Kubernetes objects) — the record is the invariant; its substrate is an implementation choice.
- The preview step is present in all four core products but with different weight (separate command vs optional change set vs continuous reconciliation) — common mature structure, not invariant.
- Language substrate varies freely (DSL / general languages / YAML templates / K8s CRDs) — variant, not invariant.
- The collaboration layer is optional in the engine poles (CLI-only Terraform/OpenTofu/Pulumi work) and native in the platform-native pole (CloudFormation is a service) — standard/optional structure, not invariant.

## Canonical Abstraction

### L0 — Defining Invariant

Three jointly-held structures:

1. **Infrastructure declared as code.** The desired infrastructure — resources on cloud or on-prem platforms (compute, network, storage, and higher-level services) — is described in machine-readable, versionable declaration files that act as the source of truth for what should exist. (Remove → API scripts with no declared source of truth; a diagramming/documentation tool.)
2. **Managed lifecycle execution.** The platform itself drives the target platforms' APIs to create, change, and destroy the declared resources — provisioning, updating, and tearing down are the platform's acts, executed as computed operations against the declaration. (Remove → a documentation or planning tool; the "code" never becomes infrastructure.)
3. **The managed-resource record.** The platform holds a persistent record binding each declared resource to the real object it created (or adopted), so subsequent runs compute incremental changes against that record, and removing a resource from the declaration leads to destroying the object it tracks. (Remove → one-shot provisioning scripts: able to create, unable to answer "what did I create," re-apply incrementally, or destroy as a managed set — exactly the Ansible-cloud-modules position.)

Jointly-held is load-bearing:

- 1 alone = infrastructure diagrams / architecture-as-code documentation
- 2 alone = ad-hoc cloud automation scripts
- 3 alone = an asset inventory / CMDB
- 1+2 without 3 = one-shot provisioning scripts (create but not track/update/destroy)
- 1+3 without 2 = a plan that never executes
- 2+3 without 1 = click-ops with an audit trail — no code, not this Type

### L1 — Common Mature Structure

Present across the researched sample; make the Type practical but do not define it:

- **Preview/diff step** — execution plan (Terraform/OpenTofu), preview (Pulumi), change set (CloudFormation); the user sees proposed creates/updates/destroys before execution.
- **Provider/adapter architecture** — pluggable connectors translating declarations into target-platform API calls; public registries of providers.
- **Reusable packaging** — modules/packages/compositions with public and private registries.
- **Dependency graph & ordering** — the engine derives create/update/destroy order from declared dependencies; parallelizes independent work.
- **Drift detection** — comparing actual infrastructure against the recorded/declared state (refresh-based in CLI tools; scheduled in platform layers; native status codes in CloudFormation; automatic correction in Crossplane's reconciliation model).
- **Import/adoption** — bringing externally-created resources under management.
- **Remote state + locking** — shared record storage with concurrency protection for teams.
- **VCS-driven workflow** — declarations under version control; PR-based review; plan-on-PR / apply-on-merge patterns.
- **Outputs** — exporting values from the managed set for other systems/stacks.
- **Per-environment parameterization** — variables/config; stacks/workspaces as instances of the same declaration.
- **CLI as primary surface + API** — automation-first interaction; web console appears with the collaboration layer.

### L2 — Variant / Optional Structure

- **Language substrate** — dedicated DSL (HCL) vs general-purpose languages (Pulumi) vs YAML/JSON templates (CloudFormation) vs Kubernetes custom resources (Crossplane).
- **Record substrate** — user-managed state file (local/remote backend) vs service-held stack record vs Kubernetes object storage.
- **Execution model** — run-based (plan/apply on demand or via VCS events) vs continuously reconciling control plane (Crossplane pole).
- **Scope** — multi-cloud vs single-cloud-native vs on-prem/virtualization vs Kubernetes-mediated.
- **Collaboration/operations layer** — none (CLI-only) vs vendor SaaS (HCP Terraform, Pulumi Cloud) vs third-party TACOS (Scalr/Spacelift/env0 class) vs native to the cloud service (CloudFormation).
- **Enterprise operations features** — policy-as-code checks on plans, RBAC/SSO, audit logging, secrets management integration, self-hosted agents/runners, drift jobs, reports.
- **Secrets posture** — sensitive values encrypted in state/config; integration with external vaults.

### L3 — Vendor-specific (Research Notes only)

- Terraform: HCL specifics; `terraform.tfstate` JSON format; CLI workspaces; Sentinel/OPA policy; BSL licensing → the OpenTofu fork and its registry; MCP server; Terraform Stacks (newer, not fetched in depth).
- Pulumi: Pulumi Cloud architecture (credentials never leave the client); checkpoints/journaling; ESC environments; converters from other IaC tools; update plans.
- CloudFormation: stack sets; nested stacks; drift status codes (DRIFTED/IN_SYNC/DELETED/MODIFIED/NOT_CHECKED); express mode; private resource types/registry; CDK (not fetched — no claims made).
- Crossplane: composition functions; XRDs/XRs; operations (cron/watch); package manager.
- Scalr: per-run pricing model; inheritance across scopes; landing-zone "vending machine" pattern; MCP server.

## Historical / Market-Sample Check

- **Platform-native first generation fits.** CloudFormation — a template + stack service with change sets and drift detection, no SaaS collaboration layer, no registry, no policy engine — satisfies the L0 core completely. The definition is therefore not over-fitted to the modern multi-cloud SaaS era.
- **Engine-only fits.** Terraform/OpenTofu/Pulumi CLIs with a local state file and no collaboration layer satisfy the L0 core. The collaboration layer is deliberately held OUT of the definition.
- **Older/regional/platform-native products.** First-generation cloud template services and first-generation CLI tools (the Terraform-generation) both fit. The Type's history is inherently API-driven-infrastructure-era; before cloud APIs the practice has no substrate, and the nearest ancestor practice (server provisioning/configuration) matured into the Configuration Management Type instead — a different Type by the resource-lifecycle test.
- **Anti-overfitting applied.** "State file" is NOT the invariant (CloudFormation holds its record as a stack; Crossplane as Kubernetes objects) — the invariant is the managed-resource record as such. "HCL" is NOT the invariant (Pulumi/CloudFormation/Crossplane differ) — the invariant is machine-readable declaration. "Plan command" is NOT the invariant (CloudFormation change sets are optional; Crossplane reconciles continuously) — the invariant is managed lifecycle execution, of which preview is the common mature form.

## Vendor-specific Findings

See L3 above. Additionally:

- The TACOS category is vendor-neutral named by OpenTofu's own documentation ("TF Automation and Collaboration Software… platforms which allow teams to manage and orchestrate OpenTofu execution") — useful market vocabulary, held as variant-layer evidence.
- Scalr's positioning ("drop-in replacement for Terraform Cloud") confirms the collaboration layer is a substitutable commodity around a stable engine contract (same CLI commands, same state, same API endpoints).

## Boundary Findings

1. **vs Configuration Management** (sibling Type, processed): IaC manages the *lifecycle of infrastructure resources* (create/change/destroy machines, networks, load balancers, managed services); configuration management enforces the *interior state of running systems* (packages, files, services) and keeps them converged. The Ansible anchor shows the seam precisely: Ansible's cloud modules create resources via APIs but hold no record of the created set — no managed lifecycle, hence configuration management doing provisioning, not an IaC platform. Conversely, IaC tools can manage file/package-level resources on machines, but their center of gravity is the resource lifecycle. The Configuration Management pass records the same seam from its side ("resource lifecycle vs system state").
2. **vs Cloud Management Platform** (sibling Type, processed): the managed object decides — IaC platforms manage code/state/runs; CMPs manage the estate inventory and its lifecycle through consoles/catalogs/approvals. The CMP pass pre-recorded this test and classified Scalr/Terraform-Cloud-class products as IaC platforms; this pass confirms it from the IaC side (Scalr's own unit of management is workspace/run/state).
3. **vs Infrastructure Automation Platform** (directory sibling, unprocessed): "automation platform" is the umbrella vendors use for broader orchestration (config management + orchestration + event-driven automation — the Ansible Automation Platform framing). The IaC Type is the code-defined infrastructure-lifecycle core. Flag for the sibling's pass: the seam is orchestration-breadth vs resource-lifecycle-as-code.
4. **vs Application Deployment Management / Continuous Delivery**: deployment tools move *application artifacts* through environments; IaC platforms provision *infrastructure resources*. They interlock (pipelines call IaC; IaC creates the environments) and blur at the edge (serverless frameworks describe infrastructure and code together), but the managed object differs.
5. **vs Kubernetes Management Platform**: Crossplane runs inside Kubernetes and uses Kubernetes machinery, but its managed objects are external cloud/cloud-native resources declared as custom resources — a control-plane-form variant of IaC, not cluster management. Kubernetes Management (cluster operations) remains a separate Type.
6. **vs Secrets Management**: state/config carry sensitive values; IaC platforms encrypt them and integrate with vaults; they do not provide vault services as their core.
7. **vs IT Change Management (ITSM)**: process governance over whether/how changes happen; IaC platforms are the execution machinery. Policy-as-code on plans is the point where the two interlock.
8. **Naming observation**: "Infrastructure-as-Code" is also used generically for the *practice* (any infrastructure defined in code). The Type documented here is the *platform/product* category that operationalizes the practice. The directory leaf name ("Platform") supports this reading.

## Uncertainties

- HCP Terraform's detailed workspace/run mechanics were not fetched (evidence limited to the intro page's collaboration description); the collaboration layer is therefore described at capability level, not feature level.
- Spacelift and env0 not fetched; the third-party TACOS pole rests on Scalr + OpenTofu's TACOS definition. Pole existence is well-evidenced; pole breadth is not quantified.
- AWS CDK not fetched; no claims made about it anywhere in the outputs.
- CloudFormation nested stacks/stack sets only seen in doc navigation, not fetched; not used as evidence.
- The precise market boundary between "IaC engine" and "IaC operations platform" packaging varies by vendor (Pulumi Cloud is default-on; HCP Terraform is a separate tier; TACOS are separate products). Held as a packaging variant, not resolved further.
- Ansible deep documentation unreachable (429); the straddle claim rests on Red Hat's official overview page plus the absence of any managed-resource record in its described model. Assertion kept at moderate strength.

## Final Synthesis

An Infrastructure-as-Code Platform is the application category in which infrastructure resources are declared as machine-readable code, the platform executes that declaration against target-platform APIs to create/change/destroy the resources, and a persistent managed-resource record binds declarations to real objects so the lifecycle stays managed over time.

The defining core is three jointly-held structures: **declaration-as-code + managed lifecycle execution + the managed-resource record**. Everything else the market associates with the category — plan/preview steps, provider ecosystems, modules and registries, drift detection, remote state and locking, VCS-driven workflows, collaboration consoles, policy-as-code, RBAC — is standard mature structure or variant structure, not definition.

The Type spans three market poles that all satisfy the same core: multi-cloud engines with optional collaboration layers (Terraform/OpenTofu/Pulumi), platform-native services where the cloud provider operates the whole loop (CloudFormation), and Kubernetes-native control planes that reconcile continuously (Crossplane). The collaboration/operations layer (TACOS class) is a substitutable commodity around a stable engine contract.

The two load-bearing boundaries: **vs Configuration Management** (resource lifecycle vs interior system state — the Ansible cloud-modules position is the seam made visible) and **vs Cloud Management Platform** (code/state/runs vs estate inventory — the discriminator pre-recorded by the CMP pass and confirmed here).
