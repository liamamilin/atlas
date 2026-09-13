# Research Notes — Container Management

## Research Goal

Understand what "Container Management" is as an Application Type: what object domain it operates (containers, images, hosts/nodes, clusters, environments), which lifecycle operations define it (deploy, run, scale, update, observe), how it relates to the underlying container runtimes and orchestrators (Docker, Swarm, Podman, Kubernetes, Nomad, cloud services), and how the Type is bounded against Kubernetes Management Platform, Virtualization Management, Cloud Management Platform, PaaS, registries, monitoring, and IaC.

Context: the directory splits §14 into `container-management` and `kubernetes-management-platform` as sibling leaves. The container-kubernetes-security pass (processed) already recorded the seam "same object domain, different function: deploy/scale/observe vs assess/enforce/gate; remove security findings/policies → K8s management". This pass researches the operate side on its own terms and must decide how much of the modern Kubernetes-dominated market belongs here.

## Initial Boundary

Working hypothesis before research:

- Core use: operate containerized workloads through their lifecycle — deploy images as running containers, control them (start/stop/scale/update), observe their state — against connected container runtime environments.
- Users: DevOps engineers, platform/SRE teams, developers deploying containerized applications; administrators governing container infrastructure.
- Nearest neighbors: Kubernetes Management Platform (§14 sibling), Virtualization Management, Cloud Management Platform, PaaS Management Console, Serverless Management Platform, Service Mesh Management, Infrastructure Monitoring, Application Deployment Management, Artifact Repository, IaC Platform, Configuration Management, Container & Kubernetes Security (processed).
- Main unknowns: (1) is "multi-host orchestration" definitional or common (single-host Docker GUIs exist); (2) is Kubernetes-specificity definitional or a market-era artifact (pre-Kubernetes products must still fit); (3) where cluster provisioning belongs; (4) how much registry/monitoring/GitOps machinery is inside the Type vs adjacent.

## Research Questions

1. What are the core objects (container, image, volume, network, node, cluster, environment/endpoint, service, stack/app/job)?
2. How does a user connect/register a container environment to the manager?
3. What is the deploy flow (image → running workload) and the update/rollback flow?
4. What lifecycle controls exist (start/stop/restart/scale/remove, logs, console, stats)?
5. How are workloads grouped (stack, project, service, job, namespace)?
6. What roles/permissions exist and how are they scoped?
7. What is built-in for state/events vs delegated to monitoring tools?
8. Is registry/image management in scope?
9. Multi-environment / multi-runtime support: how is it realized?
10. Where does cluster provisioning belong, and where is the Kubernetes Management Platform seam?

## Representative Products

Selected for market representativeness, documentation quality, distinct product philosophies, and distinct customer tiers:

| Product | Philosophy pole | Customer tier |
|---|---|---|
| Portainer | runtime-neutral management GUI over Docker/Swarm/Podman/Kubernetes/ACI/edge; OSS core + commercial edition | individual devs → SMB → mid-market |
| Rancher (SUSE) | multi-cluster enterprise management platform; self-described "container management platform" and "Kubernetes management tool" | mid-market → enterprise |
| Nomad (HashiCorp) | orchestrator-native, single binary, runtime-flexible (containers + legacy workloads), small scope composing with Consul/Vault | mid-market → enterprise |
| Amazon ECS | cloud-managed container orchestration service; no separate UI product — the service console is the surface | AWS-committed orgs, all tiers |
| Docker | container-native toolchain vendor (engine/CLI/Hub/Desktop) — structural anchor only; docs unreachable (see Sources) | individual devs → enterprise |

Avoided: only-Kubernetes products (reserved for the Kubernetes Management Platform leaf), dead tools (Kitematic, Shipyard), and single-vendor suite modules without standalone identity.

## Sources

Research date: 2026-09-07. All fetches via WebFetch.

- Portainer documentation (GitBook, `.md` endpoints): sitemap index; `/start/architecture.md`; `/user/home.md`; `/admin/user/roles.md`; `/advanced/access-control.md` — all reachable. Evidence layer A.
- Rancher Manager docs (ranchermanager.docs.rancher.com): "What is Rancher?" / getting-started overview page (content extracted from saved output; TOC confirms full guide structure: cluster administration, projects/namespaces, workloads deploy/upgrade/rollback, RBAC global+cluster+project roles, Helm apps, Fleet, monitoring/alerting, backup/DR, CLI) — reachable. Evidence layer A.
- Nomad docs (developer.hashicorp.com/nomad/docs): `/docs` home; `/docs/what-is-nomad`; `/docs/glossary` — reachable. Evidence layer A.
- Amazon ECS Developer Guide (docs.aws.amazon.com): `clusters.html`; `task_definitions.html` — reachable. `what-is-ecs.html` returned title only (content extraction failed); not relied on. Evidence layer A.
- Docker (docs.docker.com): `/desktop/` and `/` both failed with transport errors (2 attempts). Source abandoned per network-restriction rule. Docker is retained as a structural anchor with NO product-specific claims; the limitation is recorded here and in the final document's Sources.

## Product A — Portainer

### Key observations (evidence layer A unless noted)

**Architecture / environment model.**
- Portainer consists of a Portainer Server and Portainer Agents; both run as containers on the user's existing containerized infrastructure. Agents deploy to each node and report back to the server. A single server "will accept connections from any number of Portainer Agents, providing the ability to manage multiple clusters from one centralized interface."
- Edge Agent vs classic Agent: with the Edge Agent, remote environments reach the server over an encrypted TLS tunnel (for internet-connected sites where the agent must not be exposed); classic Agent = server reaches agents on the same network. Fleet Governance Policies require the Edge Agent.
- Runs exclusively on the user's servers, behind their firewalls; can run air-gapped.

**Environment (endpoint) abstraction.**
- Environment types: Docker Standalone, Docker Swarm, Podman, Kubernetes, Azure ACI (container instances), KubeSolo (edge). Connection methods per type: Portainer Agent, Edge Agent (standard/async), Docker API, Docker socket, Podman socket, kubeconfig import for Kubernetes, ACI API, Portainer API; auto-onboarding flow; environments can be grouped, tagged; Kubernetes cluster creation via Talos/Omni integration.
- Home page: card-based environment list with at-a-glance health/performance metrics; fleet health breakdown header; unassigned-environment callout; filter by group/platform/health; status badges (Up/Down; Heartbeat/Down for Edge); per-type metrics (containers count for Docker hosts, nodes count for Kubernetes/Swarm, GPU usage, CPU/memory); combined kubeconfig download for Kubernetes environments.

**Docker-side object surface (per environment).**
- Dashboard; Templates (application templates, custom templates; deploy a stack or a container from a template); Stacks (add/edit, webhooks, migrate/duplicate/rename, remove); Services (add, configure, scale, view tasks, logs, rollback, webhooks); Containers (add, view details, inspect, edit/duplicate, advanced settings, webhooks, attach volume, logs, stats, console, change ownership, remove); Images (pull, build, import, export, prune dangling/unused); Networks (add/remove); Volumes (add, browse, remove); Configs; Secrets; Events; Host (details, setup, registries, policies); Swarm (details, cluster visualizer, setup).

**Kubernetes-side object surface (per environment).**
- Dashboard with kubectl shell and kubeconfig; custom templates; Namespaces (add/manage/access/remove); Applications (add via form or code — manifest or Helm chart; inspect/edit incl. Helm apps; webhooks; detach volume; remove); Networking (services, ingresses — manual or manifest); ConfigMaps & Secrets; Volumes; GPU; More Resources (custom resources, cron jobs & jobs, service accounts, cluster roles, roles); Cluster (details, node inspect, setup, security constraints, registries, policies).

**Delivery / edge / automation.**
- App Delivery: Workflows; Sources (Git repository sources).
- Edge Compute: Edge Groups, Edge Stacks (deploy via Compose, Kubernetes manifest, or Helm chart), Edge Jobs, Edge Configurations, Waiting Room, Edge Templates.
- Alerting rules; stack/application auto-update (GitOps features referenced in FAQ); webhooks on stacks/services/containers/applications.

**Administration / RBAC.**
- Users (add, promote to admin, reset password), Teams, Roles. "A role is a predefined set of privileges… pair a user or team with a role then associate that pairing with an environment or environment group. A single user or team can have different roles for different environments."
- Built-in roles: Environment administrator (full access within an environment, no host management, no Portainer settings), Edge administrator, Operator (visibility across all resources; in K8s can redeploy/rollback/edit configurations but not create/edit/delete; in Docker can view logs/console but not create/edit/delete/start/stop), Helpdesk (read-only, no console), Namespace Operator (K8s-only, Operator scoped to namespaces), Standard User (full control over resources they or their team deploy), Read-Only User; global Administrator above all.
- Effective access viewer. "Because Docker does not natively provide role-based access control, we implement our own role management… On a Kubernetes environment, we leverage the RBAC functionality built into Kubernetes alongside our own role management."
- Access control on resources: all Docker/Swarm resources (except images) deployed through Portainer carry access-control settings (admin-only / all users / restricted to teams+users); children inherit from parent stack/service; resources deployed outside Portainer are marked `external` with limited control, governable via `io.portainer.accesscontrol.*` labels.
- Environment policies (BE): Kubernetes RBAC/security/network/setup/registry/observability/PSS policies; Docker RBAC/security/setup/registry/image-cleanup policies; banner & change-confirmation policy.
- Registries: add DockerHub, AWS ECR, Quay.io, ProGet, Azure, GitLab, GitHub GHCR, custom; browse/manage registries.
- Logs: authentication and activity logs; SIEM streaming (advanced). Settings: LDAP/AD/OAuth authentication; shared credentials (Sidero Omni, SSH, Git); edge settings.
- Licensing: CE free; BE node-based licensing; 3-nodes free license; RBAC is a BE feature (licensing detail — L3).

## Product B — Rancher (SUSE)

### Key observations (evidence layer A unless noted)

**Positioning (vendor's own words).**
- "Rancher is a container management platform built for organizations that deploy containers in production. Rancher makes it easy to run Kubernetes everywhere, meet IT requirements, and empower DevOps teams."
- A second page version states: "Rancher is a Kubernetes management tool to deploy and run clusters anywhere and on any provider" and "Rancher is a *complete* container management platform for Kubernetes."
- Note: the vendor uses both phrases — direct evidence that the container-management / Kubernetes-management boundary is commercially fuzzy (recorded in Boundary Findings).

**Run Kubernetes everywhere.**
- Users create Kubernetes clusters with Rancher Kubernetes Engine (RKE) or cloud Kubernetes services (GKE, AKS, EKS); can also import and manage existing clusters "created using any Kubernetes distribution or installer."
- Cluster provisioning machinery: node drivers/cluster drivers (EC2, DigitalOcean, Azure, vSphere, Nutanix), machine pools, node templates, cloud credentials, RKE cluster templates, registering existing clusters, syncing hosted clusters, Windows clusters, cloud providers.

**Meet IT requirements.**
- "Centralized authentication, access control, and monitoring for all Kubernetes clusters under its control." Examples: use Active Directory credentials against GKE-hosted clusters; enforce access control and security policies "across all users, groups, projects, clusters, and clouds"; view health and capacity of clusters from a single-pane-of-glass.
- Auth providers: local, AD, LDAP/OpenLDAP, FreeIPA, Entra ID, GitHub, Keycloak/OIDC, SAML (AD FS, Shibboleth, PingIdentity, Okta), Amazon Cognito, Google OAuth.
- RBAC: global permissions, global resources, cluster and project roles, custom roles, locked roles. Pod Security Standards/PSA configuration. Global default private registry; authenticated private registries.

**Empower DevOps teams.**
- "Intuitive user interface for DevOps engineers to manage their application workload. The user does not need to have in-depth knowledge of Kubernetes concepts to start using Rancher." Catalog of Helm charts for repeated application deployment; certified ecosystem (security tools, monitoring systems, container registries, storage and networking drivers).

**API-server feature set (vendor enumeration).**
- User management + authorization/RBAC; provisioning Kubernetes clusters on existing nodes + upgrades; catalog management (Helm); **projects** — "a group of multiple namespaces and access control policies within a cluster. A project is a Rancher concept, not a Kubernetes concept"; Fleet continuous delivery — "deploy applications from git repositories, without any manual operation, to targeted downstream Kubernetes clusters"; Istio integration delivered to developers; tracking nodes; dynamic provisioning of nodes and persistent storage; logging/monitoring (Prometheus integration)/alerting.

**Workload operations (how-to guides).**
- Deploying workloads, rolling back workloads, upgrading workloads, adding sidecars; HPA management via UI or kubectl; services; load balancer/ingresses; configmaps; secrets; registries; persistent volumes/storage classes; projects & namespaces; adding users to projects; certificate rotation; encryption key rotation; cluster templates; nodes and machine pools; backup/restore/DR; compliance scans (CIS-style); monitoring/alerting enablement per cluster/project; Rancher CLI and kubectl access with kubeconfig; authorized cluster endpoint.

## Product C — Nomad (HashiCorp)

### Key observations (evidence layer A unless noted)

**Positioning.**
- "Nomad is a flexible workload orchestrator that enables an organization to easily deploy and manage any containerized or legacy application using a single, unified workflow. Nomad can run a diverse workload of Docker, non-containerized, microservice, and batch applications."
- Single binary, self-contained; "does not require any external services for storage or coordination"; handles application, node, and driver failures; leader election and state replication for HA.
- Multi-region federation: multiple clusters linked; deploy jobs to any cluster in any region; replication of ACL policies, namespaces, resource quotas, Sentinel policies across clusters (authoritative region concept).
- Ecosystem composition: Terraform (provisioning), Consul (service discovery), Vault (secrets). Nomad "only aims to focus on cluster management and scheduling" (vendor's own scope statement vs Kubernetes).

**Object vocabulary (glossary — direct evidence).**
- **Job**: "a specification provided by users that declares a workload… A Job is a form of *desired state*; the user is expressing that the job should be running, but not where it should be run. The responsibility of Nomad is to make sure the *actual state* matches the user desired state. A Job is composed of one or more task groups."
- **Task Group**: "a set of tasks that must be run together… the unit of scheduling."
- **Task**: "the smallest unit of work… executed by drivers" — drivers include Docker, QEMU, Java, static binaries.
- **Allocation**: "a mapping between a task group in a job and a client node," created by servers as part of scheduling.
- **Client / Server agents**: clients run and manage tasks on machines; servers "manage all jobs and clients, run evaluations, and create task allocations."
- **Evaluation**: "the mechanism by which Nomad makes scheduling decisions. When either the *desired state* (jobs) or *actual state* (clients) changes, Nomad creates a new evaluation…"
- **Deployment**: "the mechanism by which Nomad rolls out changes to cluster state in a step-by-step fashion" (service jobs only); monitors allocation health and emits evaluations for the next step.
- **Node pools**: group nodes and restrict which jobs place allocations there (by environment/department/function). Regions/datacenters model infrastructure; bin packing optimizes placement.

**Boundary articulation (vendor's own words — valuable for this Type's seams).**
- Nomad vs Terraform: "Nomad runs on existing infrastructure and manages the lifecycle of applications running on that infrastructure"; Terraform is "an offline tool that runs to completion," Nomad "an online system with long lived servers" where "new jobs [can] be submitted, existing jobs updated or deleted, and… node failures" handled continuously.
- Nomad vs Kubernetes: Nomad focuses on cluster management + scheduling; composes with Consul/Vault rather than bundling.
- Nomad vs ECS (vendor comparison page — treat as vendor claim, not fact): ECS "only available within AWS," servers closed/managed by Amazon; Nomad open source, environment-agnostic.

**Operations surfaces.** CLI + API + web UI; Nomad Autoscaler (horizontal application and cluster autoscaling); Nomad Pack (job-spec templates/packs); namespaces, resource quotas, Sentinel policies, ACLs (governance layer); device plugins/GPU.

## Product D — Amazon ECS

### Key observations (evidence layer A unless noted)

**Cluster model.**
- "An Amazon ECS cluster is a logical grouping of tasks or services that provides the infrastructure capacity for your containerized applications."
- Three infrastructure types: Amazon ECS Managed Instances (AWS fully manages underlying EC2 — provisioning, patching, scaling), Fargate (serverless; pay per task resources; no infrastructure management), Amazon EC2 (full control). A cluster can mix them via launch types / capacity-provider strategies.
- Cluster components: network (VPC/subnet), optional Service Connect namespace, monitoring option (CloudWatch Container Insights — "automatically collects, aggregates, and summarizes Amazon ECS metrics and logs").
- Cluster states: ACTIVE / PROVISIONING / DEPROVISIONING / FAILED / INACTIVE. Clusters are region-specific. Access restricted via IAM policies.

**Capacity providers.**
- "Amazon ECS capacity providers manage the scaling of infrastructure for tasks in your clusters." A capacity-provider strategy determines how tasks spread across providers; clusters can define a default strategy.

**Workload model (task definitions → tasks → services).**
- **Task definition**: "a blueprint for your application… a text file in JSON format that describes the parameters and one or more containers that form your application." Parameters include: capacity to use, the Docker image per container, CPU/memory, OS, Docker networking mode, logging configuration, whether the task continues if the container finishes/fails, the container command, data volumes, IAM role.
- **Task**: "the instantiation of a task definition within a cluster"; user specifies the number of tasks to run.
- **Service**: "runs and maintains your desired number of tasks simultaneously in an Amazon ECS cluster… if any of your tasks fail or stop for any reason, the Amazon ECS service scheduler launches another instance based on your task definition… to replace it and thereby maintain your desired number of tasks."
- Console lifecycle: create task definition → run as task or service; update task definition (new revisions), deregister/delete revisions; Service Auto Scaling for Fargate tasks; Amazon Q Developer recommendations in the console (L3 detail).

## Product E — Docker (degraded anchor)

- docs.docker.com unreachable (transport errors on both attempts). No product-specific claims are made.
- Structural role retained in the sample because the container-native toolchain pole (engine + images + CLI + registry + desktop tooling) is historically where the container-management category began; the L0 below is checked against this pole conceptually (single-host, image→container, lifecycle, state) without asserting Docker-specific features.

## Cross-product Comparison

| Dimension | Portainer | Rancher | Nomad | ECS | Docker (anchor) |
|---|---|---|---|---|---|
| Managed subject | containers/stacks/services/images/volumes/networks across Docker/Swarm/Podman/K8s/ACI/edge environments | Kubernetes clusters + the workloads in them | jobs → task groups → tasks → allocations (Docker/QEMU/Java/binary drivers) | task definitions → tasks/services in clusters | containers/images on local engine(s) |
| Environment abstraction | "Environment" (endpoint) added via agent/edge agent/API/socket/import | "Cluster" (provisioned RKE/cloud-hosted/imported) | region + datacenter; servers + clients | cluster (region-scoped, capacity providers) | engine/endpoint |
| Deployment unit | stack (Compose), container, service; K8s application (form/manifest/Helm) | workload (deployment/pod), Helm app, Fleet git→clusters | job (HCL jobspec) | task definition → task/service | image → container |
| Lifecycle ops | start/stop/restart/remove, scale service, redeploy/rollback app, logs, console, stats | deploy/upgrade/rollback workloads, scale, HPA | job run/stop/scale, step-by-step deployment rollout, autoscaler | run task, service maintains desired count, auto scaling | start/stop/remove (structural) |
| Grouping | stack, environment group, tags | project (namespaces + policies), namespace | job/task group, node pool, namespace | service, cluster | compose project (structural) |
| Scheduling | delegates to runtime (Swarm/K8s) | delegates to Kubernetes | built-in scheduler (evaluations, bin packing) | built-in scheduler + capacity providers | none (single host) |
| RBAC | users/teams × roles × environments; resource ownership; external-resource labels | global permissions; cluster/project roles; enterprise auth providers | ACLs, namespaces, quotas, Sentinel policies | IAM policies | (unverified) |
| Registry | registry connection management (DockerHub/ECR/Quay/custom…) | private-registry configuration (global default, authenticated) | external (ecosystem) | ECR integration | Hub (structural) |
| Monitoring | built-in stats/events; alerting rules (BE) | Prometheus/Grafana integration; single-pane cluster health | UI metrics; ecosystem integrations | CloudWatch Container Insights | (unverified) |
| GitOps / delivery | Edge stacks, workflows, Git sources, webhooks, auto-update | Fleet (git → downstream clusters), Helm catalog | Nomad Pack templates | external CI/CD | (unverified) |
| Edge | Edge Agent, Edge Stacks/Jobs/Groups, Waiting Room | K3s heritage; Elemental (separate product) | single binary at edge | Outposts/Local Zones | (unverified) |
| Cluster provisioning | can create K8s cluster (Talos/Omni) | full cluster lifecycle (create/upgrade/import) | self-managed cluster | AWS-managed (Managed Instances/Fargate) | n/a |
| Delivery model | self-hosted software (OSS + paid) | self-hosted software (OSS heritage + Prime) | self-hosted binary (CE + Enterprise) | managed cloud service | freemium toolchain |

**Stable commonalities (B-layer):** every sampled product (1) binds to one or more container runtime environments; (2) deploys workloads from images via a declarative or form-based specification; (3) controls running workloads (start/stop/scale/update/rollback/remove); (4) exposes workload state (status, logs, resource consumption, events); (5) groups workloads above the raw container; (6) ships a web console plus CLI/API access (ECS: console + API/CLI/IaC; Nomad: CLI-first with UI).

**Stable divergences (vendor/variant):** where scheduling lives (delegated vs built-in); whether the product provisions clusters or inherits them; runtime breadth (multi-runtime vs single-platform); delivery model (self-hosted vs managed service); how much security/monitoring/GitOps is bundled.

## Canonical Model

### L0 — Defining Invariant (minimal)

A Container Management application **operates a population of containerized workloads through their lifecycle**:

1. **Connected container environment(s)** — one or more runtime environments (a host, a cluster, or a managed service) registered as the managed substrate. The manager operates *through* this connection; it does not replace the runtime.
2. **Image-based workload deployment** — workloads are instantiated from container images, with configuration (compute resources, networking, storage, environment).
3. **Lifecycle control over running workloads** — start/stop/restart/scale/update/rollback/remove.
4. **Observable workload state** — status, logs, and resource consumption surfaced for operation.

Test: remove any element → no longer recognizable as container management (a registry without deployment is an Artifact Repository; state visibility without control is monitoring; control without images is generic process/host management).

**Historical / market-sample check (§24):** single-host Docker-era GUIs (Kitematic-class, early Portainer), ECS (2015), Mesos/Marathon-era schedulers, and the Kubernetes Dashboard all satisfy this four-element core without multi-cluster aggregation, RBAC, GitOps, edge, or Kubernetes itself. The core is deliberately era- and orchestrator-agnostic. Passed.

### L1 — Common Mature Structure

- **Declarative workload specification + desired-state reconciliation** — Compose files, HCL jobs, task definitions, Kubernetes manifests; the system maintains desired state against actual state (Nomad's job/evaluation model and ECS's service scheduler are the clearest articulations; Portainer stacks and Rancher workloads realize the same pattern).
- **Multi-host scheduling/orchestration** — when the environment is a cluster: placement, rescheduling on failure, bin packing (Nomad), capacity providers (ECS), or delegation to Kubernetes/Swarm (Portainer, Rancher).
- **Application-level grouping** — stack (Portainer), project (Rancher), job/task group (Nomad), service (ECS): a unit above raw containers that carries configuration and access control.
- **Scaling** — manual scale + auto scaling (Nomad Autoscaler, ECS Service Auto Scaling, K8s HPA via Rancher).
- **Update / rollback** — rolling updates and step-by-step deployments (Nomad deployments), workload upgrade/rollback (Rancher), service rollback (Portainer), task-definition revisions (ECS).
- **Per-workload operational access** — logs, console/exec, stats/metrics, inspect.
- **Registry connection management** — configure which registries workloads pull from (Portainer registries, Rancher private registries, ECS/ECR).
- **Events / activity visibility** — environment events, audit/activity logs.
- **RBAC** — users/teams/roles scoped by environment, cluster, project, or namespace (Portainer roles, Rancher global/cluster/project roles, Nomad ACLs/namespaces, ECS IAM).
- **Web console + CLI + API** — every sampled product ships at least two of the three surfaces.

### L2 — Variant / Optional Structure

- **Multi-environment / multi-runtime aggregation** (Portainer environments, Rancher clusters) vs single-platform depth (ECS, Nomad).
- **Cluster provisioning & lifecycle** — create/upgrade/import clusters (Rancher full lifecycle; Portainer via Talos/Omni; ECS is the cluster; Nomad self-managed).
- **GitOps / continuous delivery** — Fleet (Rancher), Portainer workflows/edge stacks/auto-update; absent in ECS/Nomad cores.
- **Edge deployment** — Edge Agent/Edge Stacks/Waiting Room (Portainer); single-binary edge (Nomad).
- **Security machinery** — environment policies, image-cleanup policies (Portainer), compliance scans (Rancher), Sentinel policies (Nomad); deep security is the separate Container & Kubernetes Security Type.
- **Monitoring/alerting bundling** — Prometheus/Grafana (Rancher), CloudWatch Container Insights (ECS), alerting rules (Portainer).
- **Service mesh integration** (Rancher/Istio).
- **Non-container workload support** — QEMU VMs, Java, static binaries as tasks (Nomad drivers).
- **Serverless compute mode** (Fargate).
- **Managed-service vs self-hosted delivery** (ECS vs the rest).

### L3 — Vendor-specific (research notes only)

- Portainer: Edge Agent vs classic Agent semantics; Waiting Room; environment groups/tags; `io.portainer.accesscontrol.*` labels; effective access viewer; KubeSolo/ACI support; 3-nodes free license; node-based BE licensing; add-ons; recommendations.
- Rancher: RKE/RKE2/K3s; projects as a Rancher-specific concept; Fleet; authorized cluster endpoint; node/cluster drivers; RKE1 templates; Harvester/Longhorn/NeuVector/Elemental integrations; Prime branding.
- Nomad: evaluations; bin packing; authoritative region; Nomad Pack; Sentinel; Autopilot; device plugins; single-binary architecture.
- ECS: capacity providers & strategies; launch types; task-definition revisions; Service Connect namespaces; cluster state machine (ACTIVE/PROVISIONING/…); Amazon Q console recommendations; Managed Instances.
- Docker: (unverified — docs unreachable).

## Vendor-specific Findings

- Rancher's self-description oscillates between "container management platform" and "Kubernetes management tool" across its own doc pages — the strongest single piece of evidence that the market boundary between this leaf and Kubernetes Management Platform is commercially fuzzy.
- Nomad's docs articulate the IaC boundary from the inside: "Nomad runs on existing infrastructure and manages the lifecycle of applications running on that infrastructure" vs Terraform's offline run-to-completion model. Reused (attributed as vendor articulation) in the final document's boundary section.
- Nomad's comparison pages contain dated/vendor-claimed statements about ECS and Kubernetes (e.g., ECS "can only be used for Docker workloads"); treated as vendor claims, never as facts about ECS.
- Portainer implements its own RBAC over Docker because "Docker does not natively provide role-based access control" — evidence that RBAC in this Type is a management-layer capability, not a runtime given.

## Boundary Findings

1. **vs Kubernetes Management Platform (§14 sibling, unprocessed)** — the sharpest seam. Axis: runtime breadth vs Kubernetes specificity. Container Management operates containerized workloads across arbitrary runtimes/environments (Docker, Swarm, Podman, Nomad, cloud services, Kubernetes among them); a Kubernetes Management Platform manages Kubernetes clusters and K8s-native resources specifically (cluster lifecycle, GitOps, Helm, kubectl-grade surface). Test: restrict the managed substrate to Kubernetes clusters + K8s objects → Kubernetes Management Platform; operate non-K8s runtimes → this Type. Overlap zone is large and commercially real (Rancher self-describes as both; Portainer's largest surface is Kubernetes). Joint review recommended when kubernetes-management-platform is processed.
2. **vs Virtualization Management** — workload unit: containers (shared-kernel processes from images) vs virtual machines. Convergence exists (Nomad schedules QEMU VMs as tasks; Rancher's ecosystem includes the Harvester HCI) but the managed unit remains the seam.
3. **vs Cloud Management Platform (processed)** — CMP governs cloud accounts/resources/cost across providers; Container Management operates workloads on the runtime substrate. ECS is a cloud service, but its console is workload-centric (task definitions/services/clusters), not account-governance-centric.
4. **vs PaaS Management Console** — PaaS abstracts the runtime away (push code → running app); Container Management exposes the container substrate as the object of work.
5. **vs Artifact Repository / Package Registry** — registries store and distribute images; container management deploys from and operates on them. Portainer/Rancher include registry *connection* configuration, not registry operation.
6. **vs Infrastructure Monitoring / Observability** — this Type exposes operational state (status, logs, stats, events) as part of operating workloads; deep metrics/alerting/dashboards are integrations or bundles (Prometheus/Grafana, CloudWatch), belonging to the monitoring Types.
7. **vs IaC Platform** — vendor-articulated seam (Nomad docs): IaC provisions infrastructure offline and runs to completion; container management is an online, long-lived system operating application lifecycle on existing infrastructure.
8. **vs Configuration Management (processed)** — configuration management enforces desired state on machines/nodes; container management operates workloads on the container substrate.
9. **vs Service Mesh Management** — mesh manages inter-service traffic/mTLS; container management manages workload lifecycle.
10. **vs Container & Kubernetes Security (processed)** — same object domain, different function: operate (deploy/scale/observe) vs assess/enforce/gate. Consistent with that pass's recorded seam.
11. **vs Application Deployment Management** — that leaf concerns deploying application packages to endpoints/hosts; container management operates containerized workloads on container runtimes.

**去掉什么就变成另一个 Type:**
- Remove multi-runtime breadth; keep only Kubernetes cluster lifecycle + K8s objects → Kubernetes Management Platform.
- Replace container workloads with VMs → Virtualization Management.
- Remove workload operations; keep account/resource/cost governance → Cloud Management Platform.
- Remove runtime exposure; abstract to "deploy app, get URL" → PaaS.
- Remove workload operations; keep image storage/distribution → Artifact Registry.
- Remove operations; add assessment/enforcement → Container & Kubernetes Security.

## Uncertainties

- Docker's official documentation was unreachable (2 transport errors). Docker is retained as a structural anchor only; no Docker-specific feature claims appear anywhere. If a later pass needs Docker specifics, docs.docker.com must be retried from a different network path.
- `what-is-ecs.html` content extraction failed (title only); ECS observations rest on `clusters.html` and `task_definitions.html`, which were sufficient for the cluster/task/service model but not for console walkthrough detail.
- The exact split of scope between this leaf and Kubernetes Management Platform cannot be fully settled from one side; flagged for joint review rather than resolved unilaterally.
- Nomad's claims about competitors (ECS/Kubernetes) are vendor comparisons and were not independently verified; not used as evidence about those products.
- Rancher's "What is Rancher?" page exists in two doc versions with slightly different framing; both were captured and the divergence itself recorded as evidence.

## Final Synthesis

Container Management is the operator-facing application Type whose managed subject is the population of containerized workloads running on container runtime environments. Its defining core is small: one or more connected container environments; deployment of workloads from images with configuration; lifecycle control over running workloads (run/stop/scale/update/rollback/remove); and observable workload state. Around this core, mature products assemble a stable standard structure: declarative workload specifications reconciled against actual state, multi-host scheduling (built in or delegated to an orchestrator), application-level grouping, scaling, rolling update/rollback, per-workload logs/console/stats, registry connection management, events/audit, RBAC, and web-console + CLI/API delivery. The Type's poles: runtime-neutral management GUIs (Portainer), multi-cluster enterprise platforms (Rancher), orchestrator-native systems (Nomad), and cloud-managed services (ECS), with the container-native toolchain (Docker) as the historical anchor. The boundary with Kubernetes Management Platform is the Type's most important open seam: the axis is runtime breadth vs Kubernetes specificity, the overlap zone is commercially large, and joint review is recommended. The definition survives the historical check — pre-Kubernetes, single-host, and non-Kubernetes products all satisfy the four-element core.
