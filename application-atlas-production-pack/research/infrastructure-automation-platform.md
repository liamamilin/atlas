# Research Notes — Infrastructure Automation Platform

Research date: 2026-09-08
Slug: infrastructure-automation-platform
Directory leaf: Infrastructure Automation Platform (§14 IT, Cloud & Infrastructure)

## Research Goal

Determine what "Infrastructure Automation Platform" names in the real market, and resolve the pre-recorded flag from the sibling passes:

- infrastructure-as-code-platform pass flag: "vendors market configuration-management-plus-orchestration suites as 'automation platforms' — expected seam is orchestration breadth vs resource-lifecycle-as-code, umbrella-vs-core resolution likely"
- configuration-management pass flag: "vs Infrastructure Automation Platform (umbrella risk — flagged for joint review)"

The specific question: is this leaf (a) an alias/umbrella over configuration-management (enterprise packaging of config engines), or (b) a distinct Application Type whose defining core is the platform layer over automation engines? If (b), define the minimal invariant and hold the seams against configuration-management, IaC, and the other §14 neighbors.

## Initial Boundary (pre-research hypothesis)

- Guess: products marketed as "automation platforms" are enterprise offerings that wrap an automation engine (config-management and/or remote-execution) with a central control plane: controller/UI, RBAC, credential custody, inventories, scheduling, run records, content distribution, self-service.
- Nearest neighbors: Configuration Management (engine discipline: desired state + convergence), Infrastructure-as-Code Platform (resource lifecycle as declared code with managed-resource record), Server Management Platform, Patch Management, Cloud Management Platform, Robotic Process Automation Platform, IT Change Management (ITSM process layer).
- Main risk: defining the Type by today's dominant vendors (Ansible/Puppet/Chef/Salt) and thereby creating a duplicate of configuration-management. The RunDeck-class counter-shape (runbook automation with no desired-state engine) is the key test.

## Research Questions

1. What do vendors that call their product an "infrastructure automation platform" actually consist of? What is the platform layer over the engine?
2. What is the unit of automation the platform manages (playbook/job/workflow/state/task)? Is it procedural, declarative, or both?
3. How are targets represented (inventories, node groups, resource models)?
4. What does execution produce (run records, logs, per-target outcomes)?
5. What governance does the platform add (RBAC, credentials/secrets, delegation, self-service, audit)?
6. How is automation content distributed/curated (hubs, forge, collections)?
7. What triggers execution (manual, schedule, API, event)?
8. Does the Type require a desired-state engine? (RunDeck test)
9. How does this differ from configuration-management, IaC, patch management, RPA, IT change management?
10. Historical check: would first-generation enterprise automation packaging and engine-agnostic job runners satisfy the definition?

## Representative Products

Selected for market representation, documentation quality, differing product philosophy, and differing customer layer:

| Product | Vendor / lineage | Philosophy | Evidence depth obtained |
|---|---|---|---|
| Red Hat Ansible Automation Platform (AAP) | Red Hat | procedural engine (YAML playbooks) + enterprise platform layer | Tier 2 product pages (overview, engine-vs-platform comparison) |
| Puppet Enterprise | Puppet (Perforce) | declarative desired-state engine ("model-driven") + tasks ("task-based") + platform | Tier 2 product page + docs landing |
| Chef 360 Platform / Chef Automate | Chef (Progress) | declarative engine (cookbooks) + compliance (InSpec) + app automation (Habitat) under a SaaS/control plane | Tier 1 docs site (structure + component pages) |
| Salt / SaltStack Config | Salt Project (VMware/Broadcom lineage) | remote-execution-first engine + states; enterprise layer = SaltStack Config | Tier 1 user guide |
| RunDeck / PagerDuty Runbook Automation | RunDeck project, PagerDuty | engine-agnostic runbook automation (explicitly orchestrates other engines) | Tier 1 docs (introduction + user guide structure) |

## Sources

Tier 1 (fetched 2026-09-08):

- Salt Project — Salt user guide, "Salt overview" (remote execution / config management / orchestration; SaltStack Config feature list): https://docs.saltproject.io/salt/user-guide/en/latest/topics/overview.html
- RunDeck docs — "Rundeck Introduction" (what is Rundeck; feature highlights; OSS vs Runbook Automation): https://docs.rundeck.com/docs/about/introduction.html ; user guide structure (Projects, Jobs, Nodes, Commands, Activity, Webhooks, Schedules, Key Storage, Plugins, Administration/Security, Enterprise Runner): https://docs.rundeck.com/docs/
- Chef docs — documentation root + Platform Overview (Chef 360 Platform versions; Chef Automate sections: IAM v2, Policies/Roles/Teams, Event Feed, Compliance scan jobs, Infrastructure/client runs, Applications dashboard; Chef Infra Server; Chef InSpec; Chef Habitat; Chef Desktop; Chef 360 SaaS: enroll nodes, run Courier jobs, Chef Node Management, skills): https://docs.chef.io/ , https://docs.chef.io/platform_overview/

Tier 2 (fetched 2026-09-08):

- Red Hat — Ansible Automation Platform product page (component/feature list: automation controller, execution environments, automation mesh, content collections, automation hub, event-driven Ansible, self-service portal, dashboard/analytics, orchestrator add-on; use cases: provisioning, configuration management, orchestration, network/OS/cloud/security/edge): https://www.redhat.com/en/technologies/management/ansible
- Red Hat — "Compare Ansible options" page (AAP vs community Ansible/AWX; enterprise capabilities: RBAC, audit trails, clustering/capacity management, certified content, private automation hub, self-service "pre-approved jobs"): https://www.redhat.com/en/technologies/management/ansible/compare-awx-vs-ansible-automation-platform
- Puppet — Puppet Enterprise product page ("IT Operations Platform"; capabilities: drift detection/auto-correction with run reports and audit trail, self-service catalog of Tasks and Plans, patching workflows, compliance enforcement, control plane for Linux/Windows/network/edge) + docs landing (PE = "task-based and model-driven automation"; Puppet Core = "Core Configuration Management and Infrastructure Automation Tool"; Forge): https://www.puppet.com/products/puppet-enterprise , https://www.puppet.com/docs

Source-access limitations:

- docs.ansible.com deep operational docs were rate-limited (429) in sibling passes; not retried this pass per the single-source retry rule. AAP claims therefore rest on Red Hat product pages (Tier 2), not deep Tier 1 docs.
- Puppet deep docs: /pe/current/... URLs returned 404 ×2 this pass (docs moved behind help.puppet.com, not fetched). Puppet observations are product-page (Tier 2) + docs-landing level; no precise operational parameters asserted for Puppet.
- Chef deep component pages beyond nav/overview not fetched; Chef observations rest on docs-site structure + section titles (Tier 1 structural, not operational depth).
- No enterprise batch/workload scheduler (Control-M class) fetched; that boundary is reasoned from Type logic, not product evidence (recorded in Uncertainties).

## Product Observations

### Red Hat Ansible Automation Platform (Layer A, Tier 2)

- Self-description: "An end-to-end automation platform that combines 20+ community projects in a unified, deployable solution through an enterprise subscription" — explicitly contrasted with DIY "community Ansible projects" + AWX.
- Platform components named: automation controller ("centralized web user interface and API"), automation execution environments, automation mesh (distributed execution), Ansible Content Collections + private automation hub ("curating, managing, and distributing trusted automation content across your organization"), event-driven Ansible ("connect events to actions using rules"), self-service automation portal ("launch pre-approved jobs without needing technical expertise"), automation dashboard/analytics, automation orchestrator add-on (IT operations workflows).
- Enterprise capabilities claimed: RBAC, audit trails, "security-hardened platform", clustering + capacity management for deployments across "thousands of nodes", cloud deployment options, certified partner content.
- Use-case span: provisioning, configuration management, orchestration, network automation, OS automation, cloud automation, security automation, edge automation, AIOps automation, application delivery, policy as code.
- Integration list includes Terraform (resource lifecycle handed off), ServiceNow (ITSM), vault products (secrets), monitoring/observability.

### Puppet Enterprise (Layer A, Tier 2)

- Docs landing: "Manage the configuration of your IT infrastructure through task-based and model-driven automation." Two automation modes named: model-driven (desired state) and task-based (procedural).
- Product page: PE = "An IT Operations Platform Designed to Automate, Scale and Secure your Infrastructure"; "the only automation platform designed to keep your systems secure and deployment-ready".
- Engine behavior described on product page: platform "detects configuration drift… shows where Puppet automatically corrected the drift to restore the desired state… users can review the latest Puppet run report that displays what Puppet detected and the actions taken, creating an audit trail."
- Platform capabilities: unified management — "Automation workflows for Linux and Windows servers, network peripherals, and edge devices from a single control plane"; self-service automation — "catalog of predefined Puppet Tasks and Plans… Limit self-service to certain roles and permissions"; patching workflows — "Define your patching strategy, including node groups, scheduling, blackout windows, and permissions"; event-driven automation (respond to threats, failures, drift, compliance violations); compliance enforcement (CIS/DISA STIG); impact analysis of code before merge; observability data connector; AI assistant with RBAC.
- Packaging split: Puppet Core ("A Core Configuration Management and Infrastructure Automation Tool") vs Puppet Enterprise (platform). Forge = module sharing hub.

### Salt / SaltStack Config (Layer A, Tier 1)

- Salt defined as: "a Python-based, open-source remote execution framework for configuration management, automation, provisioning, and orchestration." Remote management = "core function" ("execute multiple commands across thousands of systems in seconds").
- Configuration management = state system (declarative, deterministic). Automation & orchestration = coordinating sets of systems ("set up the load balancer first… then apply the same matching configuration consistently across the whole cluster").
- Architecture: master manages minions (agent) or agentless via salt-ssh / proxy minions for devices that cannot run the agent. Event bus connects everything; beacons + reactors = event-driven responses; runners + orchestration = master-side orchestration; scheduler = job scheduling.
- SaltStack Config (the enterprise platform layer) — feature list: web UI, RBAC, multi-master support, central job and event cache, LDAP/SAML/OIDC/AD integration, compliance profiles (CIS/DISA STIG), reporting, enterprise API.
- Purpose of the platform layer (verbatim): "Jobs in SaltStack Config can be built, stored, and scheduled so you spend less time and fewer resources executing routine functions. It also allows distributing the work to other skill-level employees and teams while securing your system and guarding the environment from the misuse of powerful tools."

### Chef 360 Platform / Chef Automate (Layer A, Tier 1 structural)

- Docs structure shows the platform stack: Chef 360 Platform (v1.0–1.7, SaaS and self-hosted) with sections: enroll nodes, node management settings, run Courier jobs, Chef Node Management, skills/skill assemblies, platform APIs/tokens, system administration.
- Chef Automate sections: IAM overview + IAM users guide + IAM actions (authorization), API tokens, Policies, Roles, Teams, Users; LDAP/SAML authentication; Event Feed; Compliance (Reports, Scan Jobs, Profiles, Nodes); Infrastructure (Client runs, Chef Infra Server); Applications dashboard (Chef EAS); Data feeds/notifications.
- Component family around the platform: Chef Infra Client/Server (config-management engine), Chef InSpec (compliance profiles), Chef Habitat (application automation + Builder/origin RBAC), Chef Desktop (endpoint variant), Chef Workstation (authoring).
- Reading: Chef sells the engine family plus a control plane (Automate / 360) that adds identity/RBAC, node enrollment, job running (Courier), event feed, compliance scanning, dashboards — same layering pattern as AAP and SaltStack Config.

### RunDeck / PagerDuty Runbook Automation (Layer A, Tier 1)

- Definition: "Rundeck is runbook automation that gives you and your colleagues self-service access to the processes and tools they need to get their job done."
- Core model: "create workflows (called 'jobs') from any of your existing tools or scripts. Trigger Rundeck jobs from the Web GUI, API, CLI, or by schedule. Rundeck's access control features make it easy to safely delegate control of tasks to those traditionally outside of operations."
- Engine-agnostic by design: "Rundeck doesn't make you replace the scripts, commands, or tools you use today. You use Rundeck to execute workflows across your existing automation (e.g., Ansible, Puppet, Chef, Jenkins, Docker, Kubernetes, legacy tools, and all of your custom scripts/APIs)."
- Feature highlights (verbatim list): distributed command execution; workflow (option passing, conditionals, error handling, multiple strategies); pluggable execution (SSH/WinRM); pluggable resource model (node inventory from external systems); on-demand (Web GUI/API/CLI) or scheduled execution; secure key store; RBAC with LDAP/AD/SSO; access-control policy editing; history and auditing logs; any scripting language.
- User guide structure: Projects, Jobs, Nodes, Commands, Activity, Webhooks, Schedules, Calendars, Key Storage, Plugins, Administration/Security, Enterprise Runner (distributed execution across network boundaries, remote node inventory, remote secrets).
- Commercial layer (Runbook Automation): clustering/HA, advanced workflow, enhanced ACL management, dashboards — enterprise packaging of the same core.
- **Key counter-shape result: RunDeck has no desired-state engine at all — it orchestrates. Yet it carries every platform-layer element (jobs, nodes, central execution, records, RBAC, credentials, self-service).** This is what breaks the "automation platform = config-mgmt packaging" umbrella hypothesis.

## Cross-product Comparison

| Structure | AAP | Puppet Enterprise | Chef 360/Automate | SaltStack Config | RunDeck |
|---|---|---|---|---|---|
| Named reusable automation content (playbooks/tasks/plans/cookbooks/states/jobs/runbooks; collections/modules/profiles) | ✓ collections, projects | ✓ tasks, plans, modules | ✓ cookbooks, profiles, Courier jobs, skills | ✓ states, jobs, pillars | ✓ jobs (workflows over scripts/tools) |
| Central execution against managed infrastructure population | ✓ controller, mesh | ✓ control plane over nodes | ✓ 360 node enrollment, Courier jobs; Automate client-run view | ✓ master/minion + Config UI, central job cache | ✓ server + runners, nodes |
| Recorded run outcomes (history/logs per execution) | ✓ job records, analytics | ✓ run reports, audit trail | ✓ client runs, event feed | ✓ central job/event cache, reporting | ✓ Activity, history/audit logs |
| RBAC / delegation to non-experts | ✓ RBAC, self-service portal, pre-approved jobs | ✓ RBAC, self-service catalog with roles/permissions | ✓ IAM v2, roles, teams, policies | ✓ RBAC, "distributing work to other skill-level employees… guarding misuse" | ✓ "safely delegate control… outside of operations" |
| Credential/secret custody at run time | ✓ (credential storage; vault integrations) | ✓ (implicit in platform; not deep-verified) | ✓ node credentials; API tokens | ✓ (securing powerful tools; key infrastructure) | ✓ key storage, remote secrets |
| Inventories / node targeting | ✓ inventories | ✓ node groups | ✓ node management, node lists | ✓ target globs/grains (user guide), Config node views | ✓ nodes + pluggable resource model |
| Scheduling | ✓ | ✓ patch schedules, blackout windows | ✓ (job scheduling in 360) | ✓ scheduler; Config "built, stored, and scheduled" | ✓ schedules + calendars |
| Event-driven triggering | ✓ event-driven Ansible | ✓ event-driven automation | ✓ (event feed; beacons/reactors in engine) | ✓ beacons + reactors | ✓ webhooks |
| Multi-step workflow composition | ✓ workflow templates; orchestrator add-on | ✓ (task/plan workflows) | ✓ Courier jobs | ✓ orchestrate runners | ✓ workflows with conditionals/error handling |
| Content hub / sharing | ✓ private automation hub, certified collections | ✓ Forge | ✓ Supermarket/Habitat Builder with origin RBAC | — (not observed in fetched pages) | ✓ plugins (sharing of executors, not content) |
| Desired-state config engine embedded | ✓ (playbook modules, idempotent) | ✓ (core; model-driven) | ✓ (Infra) | ✓ (state system) | ✗ (none — orchestrates engines) |
| Compliance content packs (CIS/DISA) | ✓ (use case) | ✓ (Security Compliance Enforcement) | ✓ InSpec profiles, scan jobs | ✓ compliance profiles | — |
| Distributed execution across network boundaries | ✓ automation mesh | — (not observed) | ✓ (SaaS/agent architecture) | ✓ multi-master, proxies | ✓ enterprise runners |
| Self-service catalog for non-automators | ✓ portal | ✓ catalog of Tasks/Plans | ✓ (platform posture) | ✓ distribute to other skill levels | ✓ self-service runbook access |
| ITSM integration | ✓ ServiceNow | ✓ ServiceNow self-service | ✓ ServiceNow integration app | — | ✓ ServiceNow plugins |

Reading: rows 1–5 (content, central execution, run records, RBAC/delegation, credential custody) hold in 5/5. Row 11 (embedded desired-state engine) holds in 4/5 and fails exactly where the product is engine-agnostic — so it cannot be part of the defining core. Rows 6–10 and 12–15 are common mature structure.

## Abstraction Levels

### L0 — Defining Invariant (minimal)

An Infrastructure Automation Platform is the operations platform for governed automation of infrastructure, jointly held by three structures:

1. **The automation content layer.** The platform holds machine-readable, reusable, named automation definitions — jobs, playbooks, workflows, states, tasks, plans, runbooks — as managed content. This is the unit that gets delegated, scheduled, audited, and shared. Remove → untracked ad-hoc scripts; there is nothing for a platform to govern.
2. **Central managed execution.** The platform itself launches and executes that content against a population of managed infrastructure systems (servers, network devices, cloud resources, edge — represented as inventories/node lists/targets), producing recorded run outcomes (per-run history, logs, per-target results). Remove → a content library plus local CLI engine; execution exists but the "platform" (central operational record and control) is gone.
3. **The governance/delegation layer.** The platform is the control point for who can run what against which targets and with which credentials: role-based access over automation × targets, custody/injection of credentials at run time, and audit of runs. Its purpose is to make automation safely delegable beyond the people who wrote it. Remove → shared cron + sudo scripts: automation exists but is ungoverned, undeliverable, and unauditable — the pre-platform condition.

Jointly-held is load-bearing:

- 1 alone = a script/module repository (a forge/hub with nothing running it).
- 2 without 1+3 = a bare remote command runner (SSH fan-out).
- 3 without 1+2 = an access-control layer with nothing to govern.
- 1+2 without 3 = an engine on cron (ungoverned automation; the "platform" value gone).
- 1+3 without 2 = governed library that never executes.
- 2+3 without 1 = a console that can only fire ad-hoc commands.

### L1 — Common Mature Structure (5/5 or near; not definitional)

- inventories / node groups / target selection
- multi-step workflow composition with conditionals and error handling
- scheduling and trigger variety (manual launch, API/CLI, webhooks, event rules)
- content hubs / registries and sharing (forge-class)
- run history, reporting, dashboards/analytics
- self-service catalogs / portals for non-expert users
- integrations: ITSM, CI/CD, secrets vaults, monitoring/observability
- HA/clustering and distributed execution across network boundaries
- audit logging
- compliance scanning/assessment adjacent to execution (scan jobs, profiles)

### L2 — Variant / Optional Structure

- Embedded desired-state engine (config-management core) vs engine-agnostic orchestration: both in-Type.
- Procedural-first vs declarative-first authoring philosophy.
- Event-driven posture (native event bus + reactors/rules vs add-on).
- Compliance content packs and enforcement (CIS/DISA STIG) as productized modules.
- Patching/vulnerability-remediation modules built on the job machinery.
- Scope extensions: network devices, edge devices, desktops (endpoint flavor), cloud.
- SaaS control plane vs self-managed enterprise installation vs open-source core + paid platform.
- Execution transport: agent-based, agentless SSH/WinRM, proxy for non-agentable devices.
- AI assistants over automation content and infrastructure data (era-current).

### L3 — Vendor-specific (Research Notes only)

- AAP: automation mesh, execution environments, AWX lineage, "20+ community projects" framing, orchestrator add-on, node-charged subscription model.
- Puppet: Tasks vs Plans distinction, node classification, Puppet Core/Enterprise split, Puppet Edge, impact analysis pre-merge.
- Chef: Courier jobs, skills/skill assemblies, Chef EAS applications dashboard, InSpec as separate engine, Habitat origins.
- Salt: master/minion/proxy-minion topology, ZeroMQ event bus, grains/pillars, salt-ssh roster, SaltStack Config RaaS layer.
- RunDeck: project model, option passing, Enterprise Runner, licensing tiers, PagerDuty rename history.

## Rejected Findings

- **"Automation platform = configuration management, enterprise-packaged" (the umbrella hypothesis).** Rejected: RunDeck carries the full platform core with no desired-state engine; the configuration-management pass itself recorded central consoles/RBAC/recurring enforcement as NOT definitional for config-mgmt — i.e., the platform structure has a different center of gravity (governed execution of automation across the estate) than config-mgmt's (convergence of node interior state to declared desired state). The Types are distinct and keep-both is ratified; vendors bundle both, which is exactly why the umbrella impression exists.
- **"Desired-state convergence is part of the L0."** Rejected (RunDeck counter-shape, 4/5 not 5/5).
- **"Multi-step workflow orchestration is definitional."** Held as L1: present in 5/5 sampled mature products, but a platform with single-job governed execution remains recognizable as the Type; the jointly-held legs do not depend on it.
- **"Event-driven automation is definitional."** L2 variant/posture; not present as a first-class primitive in the oldest generation (RunDeck webhooks are later additions).
- **"The platform must manage cloud resource lifecycle."** Rejected: that is the IaC platform's core (declared resources + managed-resource record). Automation platforms reach cloud resources through jobs/content; creation-without-resource-record is the documented engine position (Ansible cloud-modules position recorded in the IaC pass).

## Boundary Findings

- **vs Configuration Management (sibling pass seam confirmed, both sides).** Config-mgmt's defining act: desired-state declarations + managed node population + repeatable convergence of system interiors. Automation platform's defining act: governed execution of automation (any mode) across the estate. A config engine without console = config-mgmt; a platform without any desired-state engine = automation platform (RunDeck). Bundled in 4/5 sampled products → the seam is "engine discipline vs operations layer". Keep both Types.
- **vs Infrastructure-as-Code Platform (sibling pass seam confirmed).** IaC: infrastructure declared as code as source of truth + managed lifecycle execution + managed-resource record binding declarations to created objects. Automation platform: no resource-of-record model; operates on systems and services through jobs. Terraform appears in AAP's integration list as a partner (lifecycle delegated out), which is the seam made visible from the vendor side.
- **vs Patch Management.** Patch management owns the patch lifecycle (scan → approve → deploy → confirm) as the object of record. Automation platforms offer patching as one packaged workflow on the job machinery (observed in Puppet PE; patching is a standard AAP/RunDeck-class use case generally). Direction of containment: patch workflow inside automation platform, not the reverse.
- **vs Server Management Platform.** Server management centers the server estate as the managed object (inventory, health, lifecycle of the machines); the automation platform centers automation content and runs. Overlap: node inventories. Distinction: what is the record — the server or the run.
- **vs Cloud Management Platform (sibling pass discriminator applied).** CMP's managed object = connected cloud environments and their estate (inventory + lifecycle control above provider APIs). Automation platform's managed object = automation content + runs against systems regardless of substrate. A cloud automation job is automation; estate governance is CMP.
- **vs Robotic Process Automation Platform.** RPA's execution surface is application UIs/business workflows; infrastructure automation operates machines/devices/services via protocols, agents, and APIs. Different targets, different governance objects.
- **vs IT Change Management / ITSM.** IT change management is the approval-and-record process layer for changes (ITSM). Automation platforms integrate with it (ServiceNow integrations in 3/5 sampled products) and may execute approved changes, but approval-of-record lives in ITSM.
- **vs enterprise batch/workload schedulers (not sampled — reasoned boundary).** Batch schedulers center application/business batch jobs with SLAs; infrastructure automation centers systems/nodes/automation content. Held as a reasoning-level boundary only (see Uncertainties).
- **What to remove to leave the Type:** remove the platform layer (governance + central execution + records) leaving only desired-state convergence → Configuration Management; remove systems-interior automation and make declarations own cloud resource lifecycle → IaC Platform; keep only the patch lifecycle → Patch Management; keep only UI-driven application process automation → RPA.

## Historical / Market-Sample Check

- Would older, platform-native, or differently positioned products satisfy the L0?
  - First-generation enterprise packaging of config engines (console + RBAC + node groups + run reporting over a 2010s-era engine) satisfies all three legs — yes.
  - Early open-source runbook/job runners (job definitions + node execution + ACLs + audit + scheduling, pre-SaaS era) satisfy all three legs — yes.
  - The pre-platform condition (shared script repository + cron + sudoers + runbooks) fails legs 2 and 3 jointly: execution is not centrally recorded per run with attributed actors, and there is no credential custody/delegation machinery. Correctly pre-Type.
  - Engine-only deployments (CLI engine + cron, no platform) are Configuration Management territory (per that pass's own historical anchor), not this Type. Consistent.
- Anti-overfitting notes:
  - "Platform = SaaS" is NOT definitional (self-hosted enterprise installs and OSS cores satisfy).
  - "Agents" are NOT definitional (agentless SSH/WinRM and proxy transports satisfy).
  - "YAML/playbook authoring" is NOT definitional (multiple authoring substrates across the sample).
  - "Compliance packs / patching / AI" are L2-era features, not invariants.
  - The name "automation platform" is partly marketing inflation: some vendors use it for what is essentially a config engine. The canonical concept — the operations platform layer that makes automation governed and delegable — is what the market's flagship products all build.

## Uncertainties

- Puppet's operational depth (how tasks/plans and self-service catalogs concretely surface) was not verifiable this pass (docs 404s); PE capability claims rest on vendor product-page descriptions (Tier 2). No precise Puppet operational parameters asserted anywhere.
- Chef 360's exact job/skill model was read from docs structure and section titles only; treated as structural evidence, not operational depth.
- SaltStack Config's deeper enterprise behaviors (multi-tenancy, approval flows) not fetched; only the feature list is asserted.
- Enterprise batch/workload schedulers (Control-M class) were not sampled; the boundary against them is reasoned, not evidence-backed. If a future pass processes a scheduling leaf, revisit.
- The exact position of "AIOps automation" claims (event-driven remediation at scale) is marketing-era language; held as a use case, not a structure.
- Whether some products' self-service catalogs constitute a drift toward "internal developer platform" territory: possible convergence observed (automation portals), held as variant posture; flagged for any future IDP pass.

## Final Synthesis

The leaf resolves as a **distinct Application Type**: the operations platform for governed infrastructure automation. Its defining core is jointly held by (1) reusable machine-readable automation content, (2) central managed execution against a managed infrastructure population with recorded run outcomes, and (3) the governance/delegation layer (RBAC over automation × targets, run-time credential custody, audit) that makes automation safely delegable beyond its authors. An embedded desired-state engine is common but not definitional (engine-agnostic orchestrators satisfy the core). The umbrella-vs-core flag is resolved as umbrella-marketing over a real, separable core: the market bundles engines into platforms, but the platform layer itself — content × execution × governance — is the Type. Seams held against configuration-management (engine discipline vs operations layer), IaC (resource-lifecycle-of-record vs governed runs), patch management (patch lifecycle as object vs one packaged workflow), server management (server-as-record vs run-as-record), CMP (estate inventory vs automation runs), RPA (UI automation vs system automation), and IT change management (approval-of-record vs execution).

STATUS.md one-liner (for Processed): governed-infrastructure-automation operations platform; jointly-held L0 = reusable machine-readable automation content (jobs/playbooks/workflows/states/tasks) + central managed execution against a managed infrastructure population with recorded run outcomes (inventories, per-run history/logs) + the governance/delegation layer (RBAC over automation × targets, run-time credential custody, audit) making automation safely delegable beyond its authors; embedded desired-state engine common-NOT-definitional (RunDeck counter-shape); umbrella-vs-core flag from IaC + config-mgmt passes DISCHARGED as keep-both (engine discipline vs operations layer; 4/5 bundled, 1/5 engine-agnostic).
