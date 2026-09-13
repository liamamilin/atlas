# Research Notes — Configuration Management

Research date: 2026-09-07
Leaf: Configuration Management (DIRECTORY §14 IT, Cloud & Infrastructure)
Slug: configuration-management

## Research Goal

Understand what "Configuration Management" is as an Application Type in the IT/Cloud/Infrastructure neighborhood: what objects live inside such a product, who operates it, how configuration actually gets declared, applied, and maintained over time, and where it ends relative to neighboring Types (CMDB, Infrastructure-as-Code Platform, Infrastructure Automation Platform, Server Management Platform, Patch Management, Application Deployment Management, UEM, IT Change Management, Secrets Management).

## Initial Boundary (term-collision resolution)

"Configuration management" has two established meanings in the market:

1. **ITIL/ITSM sense** — the practice of managing configuration items, baselines, and change control; its system of record is the CMDB. The CMDB leaf is already processed; its research explicitly recorded: "Configuration Management (§14) is the practice/discipline the CMDB is the system of record for, not a duplicate of it," and separately distinguished "config-as-code drift-management tools (those manage desired-state of servers, not an organization-wide CI graph)."
2. **Infrastructure-tools sense** — the tool category that declares desired system state and automatically enforces/maintains it on managed machines (Ansible / Puppet / Chef / Salt / CFEngine class).

**Decision:** the directory neighborhood (between Hyperconverged Infrastructure Management and Infrastructure Automation Platform, near IaC Platform / Server Management / Patch Management) and the cmdb pass precedent both support reading this leaf as sense 2 — the infrastructure configuration-management tool Type. The ITIL-practice sense is covered by CMDB (+ IT Change Management, unprocessed). This resolution is recorded in STATUS.md Boundary Issues.

## Research Questions

1. What is the core object model? (declarations, nodes/inventory, enforcement runs, content units)
2. What does "managing configuration" mean operationally — what is the defining loop?
3. Is convergence/idempotence definitional or merely common?
4. Push vs pull, agent vs agentless — definitional or variant?
5. What do users author, where, and in what language?
6. How are nodes identified, grouped, and bound to definitions?
7. What reporting/observability exists around enforcement runs?
8. How do compliance/security and secrets concerns attach?
9. Where is the seam to IaC provisioning, server management, patch management, endpoint management?
10. Historical check: does the oldest product (CFEngine, 1993) fit the same core without modern platform features?

## Representative Products

| Product | Why selected | Philosophy / tier |
|---|---|---|
| Ansible (community + Red Hat Ansible Automation Platform) | dominant market share; agentless push; YAML | procedural-flavored tasks built from idempotent modules; OSS + enterprise platform |
| Puppet (Core / Enterprise) | classic enterprise CM; declarative DSL; agent pull | model-driven, declarative; OSS core + commercial hardened builds |
| Chef (Progress) | code-first heritage; strong test/compliance tooling | infrastructure-as-code in Ruby; workstation-centric developer workflow |
| Salt (Salt Project) | event-driven; remote-execution core + states | Python, master/minion, speed at scale |
| CFEngine | historical anchor (1993, oldest surviving product) | promise theory, convergence; used for the historical/market-sample check |

## Sources

Tier 1 (official operational documentation, directly fetched 2026-09-07):

- Salt Project — Introduction to Salt — https://docs.saltproject.io/en/latest/topics/index.html
- Salt Project — Configuration Management (states) — https://docs.saltproject.io/en/latest/topics/states/index.html
- Chef — Platform Overview — https://docs.chef.io/platform_overview/
- Chef — Documentation root (product family nav) — https://docs.chef.io/
- CFEngine — Documentation root (promise types, language concepts, components, Web UI, API) — https://docs.cfengine.com/
- Red Hat — How Ansible works — https://www.ansible.com/overview/how-ansible-works (official Ansible Collaborative page; docs.ansible.com returned HTTP 429 twice and was abandoned per network rules)

Tier 2 (official product/positioning pages):

- Puppet — Puppet Core Documentation root — https://www.puppet.com/docs/puppet/8/ (SPA shell; deep pages return the same shell)
- Puppet — Puppet Core product page + FAQ — https://www.puppet.com/products/puppet-core
- Puppet — Help portal — https://help.puppet.com/ ("Manage the configuration of your IT infrastructure through task-based and model-driven automation")

Source-access limitations:

- docs.ansible.com: HTTP 429 on two attempts → abandoned; Ansible evidence relies on Red Hat's official "How Ansible works" page (Tier 1/2 hybrid) plus links it exposes.
- Puppet deep operational docs (help.puppet.com/pe/current/default.htm returned empty; www.puppet.com/docs/pe/2025.2/pe_user_guide.html timed out) → Puppet-specific claims kept at positioning/product-family strength; no precise operational details asserted for Puppet.
- Salt commercial/enterprise packaging (post-Broadcom era) not verified this pass → no claims about Salt commercial editions.

## Product Observations

### Ansible (Red Hat) — evidence layer A unless noted

- "Ansible is an open source, command-line IT automation software application written in Python. It can configure systems, deploy software, and orchestrate advanced workflows to support application deployment, system updates, and more."
- Architecture: "built on the concept of a control node and a managed node." Ansible executes from the control node (e.g., where a user runs `ansible-playbook`); managed nodes are the devices being automated.
- Modules: "pushes out small programs—called Ansible modules—to them. These programs are written to be resource models of the desired state of the system... executes these modules (over SSH by default), and removes them when finished. These modules are designed to be idempotent when possible, so that they only make changes to a system when necessary."
- Agentless: "Since Ansible is agentless, it can still communicate with devices without requiring an application or service to be installed on the managed node." OpenSSH default transport; other transports and pull modes as alternatives.
- Inventory: "By default, Ansible represents which machines it manages using a very simple INI file that puts all of your managed machines in groups of your own choosing." Variables in `group_vars/` / `host_vars/`; dynamic inventory plugins draw from AWS, GCP, Azure, VMware vCenter.
- Credentials: "For Ansible to execute, it needs an inventory (what are the managed nodes I am trying to automate?) and credentials (how do I login and connect to those managed nodes?)." Ansible Vault encrypts secrets; the platform integrates CyberArk AIM, Conjur, HashiCorp Vault, Azure Key Vault.
- Playbooks: YAML tasks; example shows `yum: state: latest`, `service: enabled: true, state: started`, `copy:` — desired-state vocabulary in task arguments. "you never have to do things like declare explicit ordering relationships or write code in a programming language."
- Extensibility: modules can be written in any language returning JSON; inventory plugins; connection/callback plugins.
- Red Hat Ansible Automation Platform: automation controller (WebUI + API, based on upstream AWX), automation hub (certified/validated content collections), automation mesh (execution capacity across sites), event-driven automation, automation dashboard/analytics, charged by node, on-prem or managed/self-managed public cloud. Ansible Lightspeed (generative AI).
- Cross-product commonality (B): inventory+credentials as the two execution prerequisites; idempotent desired-state modules; reusable content ecosystem.

### Puppet (Perforce) — evidence layer A for positioning pages; deep operational docs NOT verified

- Help portal: "Puppet Enterprise® — Manage the configuration of your IT infrastructure through task-based and model-driven automation."
- Docs root: "Puppet Core is an enterprise-ready, hardened platform built on the foundations of open source Puppet... supporting configuration management, robust security, and adherence to a desired state across global infrastructures." Nav: "Use Puppet code — Define the desired state of your infrastructure using Puppet code."
- Product page FAQ: "Puppet Core provides declarative, model-based automation for managing server infrastructure across Windows, Linux, hybrid, and cloud environments." With Puppet Edge: "orchestrate both declarative (desired state) and imperative (task-based/playbook) workflows within a single, unified platform."
- Product family: Puppet Core (hardened OSS builds; free Developer License up to 25 nodes, commercial beyond), Puppet Enterprise ("IT Operations Platform Designed to Automate, Scale and Secure your Infrastructure"), Bolt (task-based orchestration), PuppetDB, PDK (module development), Continuous Delivery, Security Compliance Management / Security Compliance Enforcement (prebuilt modules aligned to CIS Benchmarks and DISA STIGs), Puppet Edge (firewalls, network appliances, POS endpoints).
- Ecosystem: Puppet Forge — "thousands of downloadable modules."
- NOT verified this pass: agent/master run mechanics, console feature names, orchestration scheduling details. No precise operational claims made for Puppet anywhere in this research.

### Chef (Progress) — evidence layer A

- "Chef Infra is a powerful automation platform that transforms infrastructure into code... automates how infrastructure is configured, deployed, and managed across your network, no matter its size."
- Authoring: Chef Workstation "allows you to author cookbooks and administer your infrastructure"; ships Cookstyle, ChefSpec, Chef InSpec, Test Kitchen ("make sure your Chef Infra code does what you intended before you deploy it to environments used by others, such as staging or production").
- Resources: "A resource corresponds to some piece of infrastructure, such as a file, a template, or a package. Each resource declares what state a part of the system should be in, but not how to get there. Chef Infra handles these complexities for you." Recipe = file grouping related resources; cookbook = structure.
- Server: "The Chef Infra Server acts as a hub for configuration data. It stores cookbooks, the policies that are applied to the systems in your infrastructure and metadata that describes each system." `knife` CLI uploads cookbooks.
- Nodes & convergence: "A node represents any system you manage and is typically a virtual machine, container instance, or physical server... All nodes have Chef Infra Client installed... Periodically, Chef Infra Client contacts the Chef Infra Server to retrieve the latest cookbooks. If (and only if) the current state of the node doesn't conform to what the cookbook says it should be, Chef Infra Client executes the cookbook instructions. This iterative process ensures that the network as a whole converges to the state envisioned by business policy."
- Chef Automate (visibility/compliance UI): client runs, event feed, compliance reports/scan jobs/profiles/nodes, IAM (users/teams/roles/policies/API tokens, LDAP/SAML), ServiceNow integration (incident creation), applications dashboard.
- Chef 360 Platform (SaaS): enroll nodes, node management, Courier jobs, skills.
- Chef Desktop: same machinery aimed at macOS/Windows desktops (resources: firewall, disk encryption, password policy, screensaver, automatic software updates, zero-touch enrollment).
- Chef Habitat: separate application packaging/supervision product (adjacent, not the CM core).

### Salt (Salt Project) — evidence layer A

- "Salt is: A configuration management system. Salt is capable of maintaining remote nodes in defined states. For example, it can ensure that specific packages are installed and that specific services are running. A distributed remote execution system used to execute commands and query data on remote nodes."
- "Salt contains a robust and flexible configuration management framework, which is built on the remote execution core. This framework executes on the minions, allowing effortless, simultaneous configuration of tens of thousands of hosts, by rendering language specific state files."
- States: "Express the state of a host using small, easy to read, easy to understand configuration files. No programming required." State list: "install packages, create users, transfer files, start services, and so on." Highstate data structure = "technical representation of the configuration format that states represent."
- Renderers: "Salt's configuration management system is, under the hood, language agnostic... Salt states are only concerned with the ultimate highstate data structure, not how the data structure was created." YAML is one choice.
- Pillar system (per-node data); targeting "not just by hostname, but also by system properties" (grains); master/minion topology; ZeroMQ networking, public-key auth + AES payloads; Salt SSH (agentless mode); Salt Cloud; Proxy Minion; Events & Reactor; Orchestration; Network Automation; remote execution parallel at scale.
- Docs nav literally carries a "Configuration Management" section (states) distinct from "Remote Execution" — the product itself separates the two concepts.

### CFEngine (Northern.tech) — evidence layer A; historical anchor

- "This site contains information on how to manage and automate infrastructure with CFEngine."
- Language concepts: bundles, bodies, **promises**, variables, classes, decisions. Promise types: processes, packages, users, files, storage, services, commands, methods, reports, etc. — the unit of policy is a promise about a system aspect.
- Components: cf-agent (enforcement), cf-serverd (policy/file server), cf-execd (scheduling), cf-promises (validation), cf-monitord, cf-hub (reporting hub), cf-runagent (remote runs), cf-secret.
- Enterprise Web UI (Mission Portal): hosts, compliance, alerts/notifications, enterprise reporting, federated reporting, measurements, policy deployment, RBAC, audit logs, decommissioning hosts; Enterprise API includes Changes REST API, File changes, CMDB API (node data input — vendor naming, not the CMDB Type), Inventory API, Host REST API, VCS settings.
- Tutorials: manage packages, manage processes and services, manage local users, distribute files from a central location, file editing, "Reporting and remediation of security vulnerabilities", "Controlling frequency" (agent run scheduling), policy layers of abstraction, testing policy.
- Example promise patterns: ensure a service is enabled and running, install packages, ensure a process is not running, set up sudo, NTP, SSH keys — the same canonical configuration concerns as the other four products.
- Additional topics: ITIL, change management, STIGs, DevOps, orchestration.
- CFEngine Build: catalog of policy and modules (community content sharing).

## Cross-product Comparison

| Dimension | Ansible | Puppet | Chef | Salt | CFEngine |
|---|---|---|---|---|---|
| Declared-state vocabulary | modules as "resource models of the desired state"; task args like `state: latest/started` | "declarative, model-based automation"; "define the desired state... using Puppet code" | resources "declare what state... should be in, but not how to get there" | states "express the state of a host"; highstate data structure | promises about system aspects (packages, services, files, users) |
| Node population concept | control node + managed nodes; inventory (INI/YAML/dynamic) | nodes / server infrastructure (25-node dev license tier) | node = "any system you manage"; Chef Infra Client installed | minions; targeting by hostname or system properties | hosts/agents bootstrapped to policy hub |
| Convergence / idempotence | modules "idempotent when possible... only make changes when necessary" | "adherence to a desired state" (model-driven) | "If (and only if) the current state... doesn't conform... executes"; "converges to the state envisioned by business policy" | "maintaining remote nodes in defined states" | promise theory; change detection; "What did CFEngine change?" |
| Transport model | push, agentless (SSH default); pull modes as alternative | agent pull (model-driven; not directly verified this pass) | agent pull, periodic client runs | master/minion push-pull hybrid; Salt SSH agentless | agent pull on schedule |
| Reusable content units | roles, collections; Galaxy / automation hub | modules; Puppet Forge | cookbooks/recipes; Supermarket | formulas/state modules; renderers | bundles/promise types; CFEngine Build, masterfiles framework |
| Per-node/group data | group_vars/host_vars, dynamic inventory | (not verified this pass) | attributes, node metadata on server | grains (system props) + pillars | classes, augments, CMDB API inputs |
| Central console (enterprise) | automation controller (WebUI+API, AWX-based), dashboard/analytics | Puppet Enterprise console (positioning only) | Chef Automate (client runs, event feed, compliance) | (commercial shape not verified) | Mission Portal (hosts, compliance, alerts, reporting) |
| Run reporting | job outcomes via controller; automation analytics | (not verified this pass) | client runs, event feed | job/return machinery (docs nav) | changes API, file changes, reporting UI |
| Compliance/security | security/reporting tools in platform positioning | Security Compliance Enforcement (CIS/DISA modules) | InSpec profiles, scan jobs, compliance reports | (not verified) | STIGs topic, vulnerability reporting & remediation tutorial |
| Secrets | Vault encryption; CyberArk/Conjur/HashiCorp Vault/Azure Key Vault integrations | (not verified this pass) | node credentials; Chef Vault heritage (lint cops) | pillar data (sensitive data handling) | cf-secret component |
| Orchestration/workflow | playbooks orchestrate; event-driven automation; automation mesh | Bolt (task-based); "declarative + imperative in one platform" | Chef 360 Courier jobs | orchestrate module; Events & Reactor; Thorium | methods, orchestration topic |
| Scope extension | network devices, cloud APIs, Windows | Puppet Edge (firewalls, POS, appliances) | Chef Desktop (macOS/Windows), cloud | Salt Cloud, Proxy Minion, network automation | (edge/OT positioning on vendor site — not doc-verified) |
| Authoring language | YAML playbooks (+ any language for modules) | Puppet DSL | Ruby DSL | SLS (YAML default + renderers; PyDSL) | CFEngine promise language |
| Commercial shape | OSS + Red Hat subscription (node-charged; SaaS option) | OSS + Core (hardened) + Enterprise | OSS + Automate/360 (SaaS option) | OSS (commercial shape not verified) | OSS + Enterprise (Mission Portal) |

## Canonical Abstraction

### L0 — Defining Invariant

Minimal structure without which the product stops being recognizable as a configuration-management application:

1. **Declared desired-state definitions** — machine-readable configuration code/data held by the tool that describes what managed systems *should* be (not a record of what they are, and not a one-off script). Every sampled product centers on this: Ansible modules as "resource models of the desired state"; Chef resources that "declare what state a part of the system should be in, but not how to get there"; Salt states expressing "the state of a host"; CFEngine promises; Puppet "declarative, model-based automation" of "desired state."
2. **Managed node population** — an identified, addressable set of target systems (servers/VMs/containers/devices) that the definitions bind to, with grouping/scoping. Ansible inventory, Chef nodes, Salt minions, CFEngine hosts, Puppet nodes.
3. **Automated convergence** — the tool applies the declared state to nodes and can re-apply it, moving systems toward the declared state and re-establishing it after change or drift, changing only what is out of conformance. Chef: "If (and only if) the current state of the node doesn't conform... executes... converges"; Ansible: "idempotent... only make changes to a system when necessary"; Salt: "maintaining remote nodes in defined states"; CFEngine: promise-based convergence with change detection.

The enforcement run's outcome is observable to the operator (what changed, what failed) — treated here as intrinsic to operating the loop rather than a separate invariant; rich reporting surfaces are L1.

**Historical check (§24):** CFEngine (1993) satisfies all three invariants with none of the modern platform features (no YAML, no cloud, no SaaS, no web console as core — Mission Portal is an enterprise add-on; policy is text files; agent pull on a schedule). Early Puppet/Chef (mid-2000s) fit identically. Modern platforms (AAP, Chef 360) also fit. The L0 is not an artifact of the current platform era. Conversely, removing any invariant changes the Type: without declared state it is ad-hoc remote execution / scripting; without a managed node population it is local config tooling; without convergence it is one-shot provisioning or a runbook executor.

### L1 — Common Mature Structure

Present across the sampled products; expected in mature offerings but not definitional:

- **Inventory / node registry with grouping and scoping** — static files (Ansible INI), server-held node metadata (Chef), system-property targeting (Salt grains), hub host registry (CFEngine); dynamic inventory from cloud providers (Ansible plugins — directly observed).
- **Reusable content units + sharing ecosystem** — roles/collections (Galaxy, automation hub), cookbooks (Supermarket), modules (Forge), formulas/state modules, bundles/policy (CFEngine Build).
- **Parameters and per-node/per-group data** — group/host vars, attributes, pillars, classes/augments; templating of config files (Ansible templates, Chef templates, Salt renderers, CFEngine Mustache).
- **Run reporting / observability of enforcement** — job outcomes, client-run history, event feeds, change tracking (CFEngine Changes API; Chef Automate client runs; AAP automation analytics).
- **Drift detection / change reporting** — detecting non-conformance between declared and actual state (CFEngine change detection + alerts; Chef's conform check is the enforcement-side form; compliance views aggregate it).
- **Central management surface for enterprise editions** — WebUI + API over the engine (automation controller, Chef Automate, Mission Portal, PE console).
- **Recurring enforcement** — periodic agent runs (Chef "Periodically, Chef Infra Client contacts..."; CFEngine "Controlling frequency", distributed scheduling); push tools re-apply on demand or via schedules in their platform layers.
- **Compliance / security posture** — scanning and enforcement against standards: InSpec profiles + scan jobs (Chef), CIS/DISA modules (Puppet), STIG topic + vulnerability remediation (CFEngine).
- **Secrets handling** — encrypted vars (Ansible Vault), integrations with external vaults (CyberArk, Conjur, HashiCorp Vault, Azure Key Vault), node credentials (Chef), cf-secret (CFEngine), pillar data (Salt).
- **Orchestration / workflow layer above single-node state** — multi-node orchestration (Ansible playbooks, Salt orchestrate, Chef 360 Courier, Bolt, CFEngine methods), event-driven automation (Red Hat event-driven Ansible; Salt Reactor/Thorium).
- **Programmatic access** — CLIs throughout; REST APIs on the enterprise surfaces (CFEngine Enterprise API, Chef Automate API, AAP controller API).

### L2 — Variant / Optional Structure

- **Execution model**: push vs pull vs hybrid; agent vs agentless (Ansible agentless-SSH; Salt both; Chef/Puppet/CFEngine agented pull).
- **Authoring language**: YAML (Ansible), Puppet DSL, Ruby (Chef), SLS + renderer system (Salt), promise language (CFEngine). Language-agnostic rendering exists (Salt renderers) — the invariant is machine-readable declarations, not any specific syntax.
- **Scope extension**: network devices (Ansible network automation, Salt network automation, Puppet Edge), desktops (Chef Desktop), cloud resources (Salt Cloud, Ansible cloud modules, dynamic inventory), appliances/edge/POS (Puppet Edge).
- **Commercial packaging**: OSS engine + enterprise platform (AAP, Puppet Enterprise, Chef Automate/360, CFEngine Enterprise/Mission Portal); SaaS delivery options (AAP public cloud, Chef 360 SaaS); hardened vendor builds (Puppet Core); node-charged licensing (AAP; Puppet 25-node dev tier).
- **Event-driven automation** as a distinct layer (event-driven Ansible; Salt Reactor).
- **Compliance content packs** (CIS Benchmarks, DISA STIGs).
- **AI assistance** (Ansible Lightspeed; CFEngine AI agent / AI chat API).

### L3 — Vendor-specific (research notes only; excluded from the final document)

- Ansible: AWX→automation-controller lineage; automation mesh; node-charged licensing; Lightspeed; collections naming; "beginner's guide" e-book funnel.
- Chef: cookbooks/recipes/knife/chef-repo naming; Habitat (app packaging — separate product); InSpec; 360 Courier/skills; OpsWorks migration path; applications dashboard.
- Puppet: Forge; PDK; Bolt; PuppetDB; Core/Enterprise/Edge product split; CVE remediation SLAs (CVSS 9–10: 14 days; 7–8.9: 30 days); 25-node free Developer License; System Hardening Assessment marketing site.
- Salt: grains/pillars terminology; ZeroMQ/msgpack transport; Reactor/Thorium; Proxy Minion; Venafi tools; Salt Virt.
- CFEngine: promise-theory vocabulary (bundles/bodies/promise types); Mission Portal; cf-* component names; CMDB API (node-data input — name collision with the CMDB Type); federated reporting; Masterfiles Policy Framework; cfbs tooling.

## Rejected Findings

- **"Configuration management = CMDB"** — rejected. The CMDB is a system of record about what exists (CIs + relationships); configuration-management tools enforce what systems should be. The cmdb pass already recorded the seam. CFEngine's "CMDB API" is node-data input for policy — a vendor naming collision, not evidence of Type identity.
- **"Configuration management = Infrastructure-as-Code"** — rejected as identity. Overlap is real (both are code-managed infrastructure; Ansible/Salt can provision cloud resources), but the center of gravity differs: resource lifecycle provisioning (create/destroy VMs, networks) vs interior system state (packages, files, services, users) maintained over time. See Boundary Findings.
- **"Idempotence requires agents"** — rejected. Ansible is agentless and idempotent; CFEngine/Chef/Puppet are agented. Transport is a variant, not the invariant.
- **"Configuration management is defined by YAML"** — rejected. Five different authoring languages in the sample; Salt explicitly renders language-agnostically to a common data structure.
- **"Modern platforms (web consoles, RBAC, analytics) define the Type"** — rejected by the historical check: CFEngine's core satisfies L0 with none of these.
- **"Salt is 'just' remote execution"** — rejected: Salt's own docs separate Remote Execution from Configuration Management (states) while building states on the execution core; both are present.

## Boundary Findings

1. **vs CMDB (processed)** — CMDB: maintained record of configuration items + relationships + impact model (what exists, consulted). Configuration Management: declared desired state + enforcement on nodes (what should be, applied). Remove-the-declared-state test: a CMDB without enforcement remains a CMDB; a CfM tool without a CI graph remains CfM. Integration seam exists (config tools feed inventory/facts; CMDBs inform scoping). Aligned with research/cmdb.md.
2. **vs Infrastructure-as-Code Platform (unprocessed — joint review recommended)** — IaC platforms center on provisioning resource lifecycles (create/modify/destroy cloud/infra resources from code); configuration management centers on the interior state of running systems, maintained continuously. The market blurs the seam (Ansible/Salt ship cloud modules; Terraform-class tools occasionally touch files), and vendors describe themselves with both vocabularies. Recommended seam test: does the product's primary object model describe *resources to be created/destroyed* (→ IaC) or *state to be established and maintained on existing systems* (→ CfM)?
3. **vs Infrastructure Automation Platform (unprocessed — joint review recommended; umbrella-term risk)** — vendors themselves straddle: Puppet Core's own nav reads "A Core Configuration Management and Infrastructure Automation Tool"; Red Hat positions Ansible as an "automation platform." If the Infrastructure Automation Platform leaf is processed as a broader orchestration/runbook Type, the seam is: desired-state enforcement (CfM) vs workflow/orchestration breadth (IAP). If research shows it is an alias of this Type, record as duplicate rather than merging silently.
4. **vs Server Management Platform (unprocessed)** — server management centers on operational oversight of servers (inventory, health, monitoring, OS lifecycle); configuration management centers on state enforcement. A CfM run changes state; a server-management console observes and operates.
5. **vs Patch Management (unprocessed)** — patch management centers on vendor-published update content with approval/maintenance-window/compliance workflow; configuration management installs packages as one state declaration among many. Chef Desktop's `windows_automatic_software_updates` resource shows the seam from the CfM side.
6. **vs Application Deployment Management (processed)** — that pass recorded: "ADM enforces installed-software presence via installer execution on managed endpoints; IaC/CfM declares machine configuration broadly. Overlap exists (re-assertion loops) but objects differ (apps vs full config)." Aligned.
7. **vs Endpoint Management / UEM (unprocessed)** — UEM centers on device fleets (MDM profiles, compliance, mobile/desktop lifecycle); configuration management centers on declared system state regardless of device class — Chef Desktop proves a CfM product can target desktops, so the seam is the object model (device fleet management vs state declarations), not the target OS.
8. **vs IT Change Management / ITSM (unprocessed)** — the ITIL configuration-management discipline (baselines, change advisory, CMDB) is a process layer; CfM tools are enforcement engines that change may authorize. Chef Automate's ServiceNow incident integration is an integration seam, not identity.
9. **vs Secrets Management (unprocessed)** — CfM tools consume/integrate vaults (Ansible + HashiCorp Vault/CyberArk/Conjur; Chef node credentials; CFEngine cf-secret) but do not provide vault services as their core.
10. **vs Continuous Delivery Platform (unprocessed)** — CD pipelines deploy application releases through environments; CfM maintains system state. Puppet ships a separate "Continuous Delivery" product — suite adjacency, not Type overlap.

## Uncertainties

- Puppet deep operational documentation was unreachable this pass (SPA shell + timeout). All Puppet-specific operational mechanics (agent run model, console features, scheduling) are intentionally absent; Puppet claims are limited to official positioning, product family, and licensing facts.
- Salt's commercial/enterprise packaging was not verified; no claims made.
- Whether drift detection is always a first-class named feature vs an emergent property of convergence: treated as common mature structure (L1), not definitional.
- Exact scheduling defaults, run intervals, node limits: not asserted anywhere (no evidence fetched for them).
- Ansible's pull modes and Windows transport details: mentioned by Red Hat as alternatives but not researched in depth; not asserted.
- The Infrastructure Automation Platform leaf's intended meaning is unresolved (umbrella vs distinct Type) — flagged for joint review.
- CFEngine's widely documented founding year (1993) was not verifiable from the fetched documentation pages; the historical-anchor argument relies only on the fetched evidence (promise-based policy language, agent/hub architecture, enterprise add-on console), which independently establishes a pre-platform generation. No founding-year claim is made in the final document.

## Final Synthesis

A Configuration Management application is defined by a small invariant: **machine-readable declarations of desired system state + a managed, identified population of target systems + automated, repeatable convergence of those systems toward the declared state.** Everything else the market associates with the category — agents or agentless transport, push or pull, YAML or DSL, web consoles, RBAC, compliance packs, event-driven automation, AI — is implementation or variant. The type's central promise is that configuration is *code that is continuously enforced*, not documentation or one-off scripts; its central loop is declare → bind to nodes → enforce → observe → re-converge. The term collides with the ITIL practice sense (covered by the CMDB leaf) and blurs commercially into "infrastructure automation" and IaC; the seams are recorded above and flagged for joint review where the neighboring leaf is unprocessed.
