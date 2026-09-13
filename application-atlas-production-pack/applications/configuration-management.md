# Configuration Management

## Overview

A **Configuration Management** application manages the configuration of IT infrastructure by holding machine-readable declarations of what managed systems *should* look like, and automatically applying and re-applying those declarations to a managed population of machines so that the systems converge to — and stay in — the declared state.

The defining structure is small:

```text
Desired-state declarations (code/data describing what systems should be)
└── bound to
    Managed node population (identified target systems, grouped and scoped)
    └── enforced by
        Automated convergence (apply → change only what is out of conformance → re-apply over time)
```

Everything else commonly associated with the category — agents or agentless transport, push or pull execution, a particular authoring language, web consoles, role-based access, compliance content packs, event-driven automation — is widespread in current products but is not what makes a product a configuration-management tool. The category's founding-generation product satisfies the defining structure with none of those modern features, and the newest platforms still reduce to the same three-part core.

The category's central promise is that configuration is **code that is continuously enforced**, not documentation and not one-off scripts. When the primary object shifts to *creating and destroying infrastructure resources* (rather than maintaining the state of existing systems), the product is drifting toward Infrastructure-as-Code; when it shifts to *records of what exists* (rather than enforcement of what should be), it is drifting toward a CMDB.

## Users & Context

The primary users are the people responsible for keeping server and infrastructure fleets consistent:

- **Infrastructure / platform engineers** — author the desired-state declarations (packages, files, services, users, settings), organize them into reusable units, and keep them in version control.
- **System administrators / operations teams** — bind declarations to groups of machines, trigger or schedule enforcement runs, and handle the machines that fail to converge.
- **Security & compliance teams** — define and verify security baselines (hardening standards, allowed services, password policies) and consume the resulting compliance reports.

Secondary concerns fall to the same engineering organization: managing credentials the tool uses to reach machines, integrating with version control and ticketing systems, and operating the central console in larger deployments.

The work environment is a split surface: **authoring happens in code repositories and editor/CLI tooling**, while **operation happens through a CLI and — in enterprise editions — a web console** showing machines, runs, and compliance. The managed population is typically servers and virtual machines, extending in many products to containers, network devices, cloud services, and sometimes desktop workstations.

## Core Model

### The Defining Core

**1. Desired-state declarations.** The tool holds machine-readable definitions that describe the state a system should be in — which packages installed at which version, which services enabled and running, which files exist with which content and permissions, which users and settings configured. The essential property is that declarations describe *the end state, not the steps*: a declaration says "this package is installed" or "this service is running," and the tool works out how to get there. This is why the same declaration can be applied to a machine that lacks the package and to one that already has it.

**2. Managed node population.** The declarations bind to an identified, addressable set of target systems — the tool's inventory of machines. Nodes are named, grouped (by role, environment, location, or platform), and can carry per-node or per-group data that parameterizes the declarations. The inventory is both a targeting mechanism (which declarations reach which machines) and the tool's map of what it manages.

**3. Automated convergence.** The tool applies the declared state to the nodes and can re-apply it. On each enforcement run it compares the declared state with the machine's actual state and changes only what is out of conformance — installing a missing package, restarting a stopped service, rewriting a modified file — and reports what it changed. Re-running the same declarations on a conforming machine changes nothing. This repeatability is what turns configuration from a procedure into a maintained state: after any change, failure, or unauthorized modification, another run moves the machine back toward the declared state.

Remove any one of the three and the Type collapses: without declarations it is ad-hoc remote execution or scripting; without a managed node population it is local configuration tooling; without convergence it is one-shot provisioning or a runbook executor.

### Standard Capabilities

Mature products commonly add the following. They make the core practical at scale but do not define the Type.

- **Reusable content units.** Declarations are packaged into shareable, versioned units — bundles of declarations for a piece of software or a system role — with public or in-house repositories for distributing them (community content hubs exist across the category).
- **Parameters and per-node data.** Variables set at group or node level, plus separate data sources for sensitive or environment-specific values, feed into declarations; configuration files are typically rendered from templates rather than copied verbatim.
- **Run results and change reporting.** Every enforcement run produces an observable outcome — which nodes were reached, what changed, what failed. Mature products retain this history and surface it as feeds, dashboards, or queryable records.
- **Drift detection.** The flip side of convergence: comparing actual state against declared state and reporting the difference, either as part of enforcement runs or as dedicated compliance views.
- **Central management surface.** Enterprise editions commonly wrap the engine in a web console and API: job history, node/host views, scheduling, access control, and reporting across teams.
- **Recurring enforcement.** Pull-model products run their client agents on a schedule so convergence happens continuously; push-model products re-apply on demand or on schedules provided by their platform layer.
- **Secrets handling.** Encrypted variables in the tool's own format and/or integration with external vault products, since declarations routinely need passwords, keys, and tokens that must not sit in plaintext.
- **Orchestration above single-node state.** Coordinating multi-step, multi-machine work — rolling changes across tiers, sequencing dependencies, reacting to events — as a layer on top of state enforcement.
- **Programmatic access.** Command-line interfaces throughout, and REST APIs on the central surfaces, so enforcement can be triggered from pipelines and other systems.
- **Authoring safeguards.** Validation, linting, and testing tooling for declarations — checking syntax, exercising declarations against throwaway machines, and verifying the resulting state before it reaches production.

### One Structure, Many Implementations

The core model is conceptual. Products realize each concept differently, and a reader who has only seen one implementation should still be able to recognize the others:

```text
Concept:            Desired-state declarations
Implementations:    YAML task files calling state-enforcing modules;
                    a dedicated declarative language; Ruby code built
                    from state-declaring resources; state files rendered
                    to a common data structure; promise-based policy

Concept:            Managed node population
Implementations:    simple text-file inventories with groups;
                    server-held node metadata; agent registries on a
                    central hub; targeting by system properties

Concept:            Convergence
Implementations:    push over SSH with no resident agent;
   	                periodic agent runs pulling policy from a server;
                    event-triggered or scheduled state application
```

## How It Works

### Author the declarations

An engineer writes desired-state definitions in the tool's language, usually inside a version-controlled repository: which packages, which files (often from templates), which services, which users and settings. Declarations are organized into reusable units — per software component or per system role — and parameterized so the same unit serves multiple environments. Before deployment, mature toolchains validate and test the declarations: syntax checks, style linting, and trial runs against disposable machines.

### Bind declarations to machines

The declarations are mapped onto the managed population: machines are listed and grouped in an inventory (a static file, a server-held registry, or a dynamic source such as a cloud provider's API), and groups or individual nodes are assigned the content units that apply to them. Per-group and per-node data fills in the differences — hostnames, sizes, feature flags, environment-specific settings.

### Enforce — and keep enforcing

Enforcement is the category's characteristic loop:

```text
Select target nodes
→ reach each node (push over a protocol such as SSH, or an agent pulls its policy)
→ compare declared state with actual state
→ change only what is out of conformance
→ report the outcome (changed / unchanged / failed)
```

In pull-model products the agent repeats this on a schedule, so every machine is continuously re-checked and re-converged. In push-model products the operator (or an automation platform) triggers runs, and enterprise layers add schedules and event triggers. Either way, the same declarations can be applied repeatedly and safely: a conforming machine is left alone, a drifted machine is brought back.

### Observe and remediate

Run outcomes accumulate into an operational record: what changed where, what failed and why, which machines have not reported. Operators work from this record — re-running failed nodes, investigating unexpected changes, and using drift and compliance views to find machines that no longer match their declared state (or the security baseline encoded in it).

### Evolve the configuration

Declarations change through the same discipline as application code: edit in the repository, review, test, release, and the next enforcement run carries the change out to the fleet. Shared content units are updated, swapped for community-maintained equivalents, or extended with custom ones. Above single-node state, orchestration layers sequence larger changes — taking machines out of load balancers, updating in waves, restarting dependent services.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Authoring surface (repository + local tooling)

Where declarations live and are developed.

- declaration files in the product's language, organized into reusable units, under version control
- local CLI tooling for validating, linting, testing, and packaging declarations
- primary actions: write/modify declarations, run checks, publish a new content version

### Execution CLI

The engine's command surface.

- commands to apply declarations to selected nodes, run ad-hoc commands or checks, and inspect node state
- primary actions: target nodes, execute a run, read the run output

### Central console (enterprise editions)

The web surface over the engine in larger deployments.

- job/run history with per-node outcomes; node or host lists with grouping and search; compliance and drift views; scheduling; role-based access control
- primary actions: trigger or schedule runs, inspect a node's state and history, review compliance posture, manage access

### Reporting / compliance views

Aggregated views over run and state data.

- change reports, failure summaries, conformance against security baselines (hardening standards), exportable reports
- primary actions: filter and drill into results, export, feed external systems

### APIs

Programmatic access for automation.

- trigger runs, query node state and run history, manage inventory and content — consumed by pipelines, ticketing systems, and other operational tools

## Important Rules / Behaviors

### Declarations describe state, not procedure

The author states the intended end state; the tool determines the steps. Authors do not normally encode explicit ordering or low-level commands for state-managed aspects — the engine derives and orders the work. (Procedural escape hatches exist for genuinely sequential work, but the state-managed path is the category's center of gravity.)

### Re-application is safe and expected

Applying the same declarations twice should not double-apply changes. This idempotent behavior is what makes recurring enforcement, drift correction, and fleet-wide re-convergence possible, and products treat violations of it as defects in content.

### Only out-of-conformance changes are applied

A run against a conforming machine changes nothing. This is the observable signature of the convergence model and the basis of drift detection: *changes* are the exception, and they are reported as such.

### The inventory is also a scope boundary

Declarations reach only the machines the inventory knows about, in the groups they are bound to. Grouping therefore functions as both a targeting mechanism and an implicit access/scope control — a declaration cannot affect machines outside its binding.

### Secrets must not be plaintext

Because declarations are versioned and widely readable, credentials embedded in them are a standing risk. Products provide encrypted-variable mechanisms and/or vault integrations, and mature practice treats plaintext secrets in declarations as a defect.

### Failures are visible, not silent

A node that cannot be reached, a declaration that fails, a change that does not stick — each produces an explicit failed outcome in the run record. The operational loop depends on this visibility; unreported failure would break the drift-correction promise.

### The declared state is versioned code

Declarations live in repositories, change through review-and-release discipline, and can be rolled back. The tool's enforcement surface follows the repository, which is what makes configuration auditable: the history of *what should be* is the history of the code.

## Variants

Common forms the Type takes; each keeps the defining core intact.

- **By execution model** — push (control machine reaches out over a protocol such as SSH, no resident agent), pull (agents on nodes fetch policy from a central server on a schedule), or hybrid; agentless and agent-based transports are alternatives, not different Types.
- **By authoring language** — YAML-based task files, dedicated declarative languages, general-language code built on state-declaring primitives, or renderer systems that accept several source formats and reduce them to one internal state structure.
- **By scope extension** — server fleets (the classic case); network devices and appliances; desktop workstations (the same machinery applied to endpoint configuration); cloud services (declarations that call provider APIs); containers.
- **By packaging** — open-source engine alone; open-source engine plus a commercial enterprise platform (console, access control, analytics, support); hardened vendor-built distributions; SaaS delivery of the central surface.
- **By automation depth** — plain state enforcement; plus event-driven automation (runs triggered by events rather than schedules); plus orchestration/workflow layers for multi-step, multi-machine change.
- **By compliance posture** — general-purpose declarations; plus prebuilt content packs encoding recognized security baselines (industry hardening benchmarks) with conformance reporting.
- **By assistance** — manual authoring; plus AI-assisted declaration generation in current platform editions.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| CMDB | adjacent, often confused by name | a CMDB is a maintained *record* of configuration items and their relationships (what exists, consulted for impact analysis); configuration management *enforces* what systems should be. A CMDB without enforcement is still a CMDB; a configuration-management tool without a CI graph is still itself |
| Infrastructure-as-Code Platform | adjacent sibling | IaC centers on provisioning the *lifecycle of infrastructure resources* (create/modify/destroy machines, networks, load balancers); configuration management centers on the *interior state of running systems*, maintained continuously. Products blur the seam (cloud modules on both sides), but the primary object differs |
| Infrastructure Automation Platform | umbrella-term neighbor | vendors market configuration-management products as "automation platforms"; the configuration-management Type is the desired-state enforcement core, while broader automation platforms add orchestration, workflow, and event layers on top |
| Server Management Platform | adjacent | centers on operational oversight of servers (inventory, health, monitoring, OS lifecycle); configuration management changes and maintains system state rather than observing it |
| Patch Management | adjacent | centers on distributing vendor-published updates with approval and maintenance-window workflow; configuration management treats package installation as one state declaration among many |
| Application Deployment Management | adjacent | distributes and tracks *application packages* on managed endpoints; configuration management declares *machine configuration* broadly (files, services, users, settings), with software installation as one part |
| Endpoint Management / UEM | adjacent | centers on managing device fleets (profiles, compliance, mobile/desktop lifecycle); configuration management centers on declared system state — a configuration-management product can target desktops, so the seam is the object model, not the device class |
| IT Change Management (ITSM) | process-layer neighbor | the ITIL configuration-management discipline (baselines, change advisory, CMDB) governs *whether and how* changes may happen; configuration-management tools are engines that execute authorized state changes |
| Secrets Management | integration neighbor | configuration management consumes vaults for credentials; it does not provide vault services as its core |
| Continuous Delivery Platform | pipeline neighbor | CD pipelines deploy application releases through environments; configuration management maintains system state — some vendors ship both as separate products |

The two most important seams: **vs CMDB** (record of what exists vs enforcement of what should be — the name collision is historical, and the CMDB research pass records the same seam from its side) and **vs Infrastructure-as-Code** (resource lifecycle vs system state — the market blurs it, so the primary-object test is the reliable separator).

## Representative Products

- **Ansible** (community edition and Red Hat Ansible Automation Platform) — agentless push over SSH, YAML declarations calling idempotent modules; the largest current market footprint
- **Puppet** (open source, Puppet Core, Puppet Enterprise) — declarative, model-based automation with a dedicated language and agent pull
- **Chef** (Chef Infra, with Chef Automate / Chef 360) — code-first declarations in Ruby, workstation-centric authoring and testing, periodic client-run convergence
- **Salt** (Salt Project) — remote-execution core with a states layer on top; master/minion and agentless modes; event-driven extensions
- **CFEngine** — the category's founding-generation product and the historical anchor: promise-based policy and agent-pull convergence, checked to ensure the definition above is not over-fitted to the modern platform era

## Sources

Research date: **2026-09-07**

- Salt Project — Introduction to Salt; Configuration Management (states) — https://docs.saltproject.io/en/latest/topics/index.html , https://docs.saltproject.io/en/latest/topics/states/index.html
- Chef — Platform Overview; documentation root — https://docs.chef.io/platform_overview/ , https://docs.chef.io/
- CFEngine — Documentation root (language concepts, promise types, components, Web UI, API) — https://docs.cfengine.com/
- Red Hat / Ansible Collaborative — How Ansible works — https://www.ansible.com/overview/how-ansible-works
- Puppet — Puppet Core documentation root, product page and FAQ, help portal — https://www.puppet.com/docs/puppet/8/ , https://www.puppet.com/products/puppet-core , https://help.puppet.com/

> Sourcing limitation: the Ansible community documentation site (docs.ansible.com) was rate-limited on the research date, and Puppet's deep operational documentation was not reachable (single-page-application shell / timeout). Ansible evidence relies on Red Hat's official product-education page; Puppet evidence is limited to official positioning, product-family, and licensing pages. Accordingly, no precise operational details (run intervals, node limits, default settings, edition-specific mechanics) are stated in this document for any product. Detailed observations, the cross-product comparison, and the historical-sample check are recorded in the paired Research Notes.
