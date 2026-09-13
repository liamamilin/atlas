# Internal Developer Platform / IDP

## Overview

An **Internal Developer Platform (IDP)** is an organization's own self-service runtime platform for its software developers: a platform-engineering team configures it over the organization's own infrastructure, and application developers use it to deploy, run, and operate their applications — obtaining environments, services, and dependencies like databases directly through the platform, without filing infrastructure tickets or learning the underlying infrastructure tooling.

The defining core is small:

```text
The organization as operator
└── Developer self-service consumption
    └── Provisioning machinery of record
        └── The organization-defined abstraction layer (golden paths)
```

- **The organization as operator** — the platform serves one organization's own developers; a platform-engineering function configures it, and the organization's own cloud accounts, clusters, or data centers are the substrate.
- **Developer self-service consumption** — developers directly create and operate their applications' runtime pieces through the platform's own surfaces.
- **Provisioning machinery of record** — the platform itself turns those requests into provisioned, running software and holds the state of what is deployed where.
- **The organization-defined abstraction layer** — reusable building blocks configured by the platform team (templates, stacks, resource definitions, golden-path catalogs) that determine what developers can consume and how their requests map onto infrastructure.

Everything else commonly associated with IDPs — Kubernetes, service catalogs, preview environments, built-in CI/CD, cost dashboards, AI assistants — is widespread in current products but is not what makes a platform an IDP. An organization-run internal PaaS from the previous decade satisfies the same core without any of them; a ticket-driven internal hosting request form is the pre-history this Type digitized.

The market also uses "IDP" as a concept — the assemblage a platform team composes in-house. This document describes the product Type that serves that concept. The sibling Type **Internal Developer Portal** is the developer-facing surface (catalog, scorecards, documentation) that commonly sits on top of or beside an IDP; the two are complementary and are sold both separately and combined.

## Users & Context

Two roles with a strict division of labor — this split is the most stable structural fact across the researched products:

**Platform engineers / platform team** (configuring role):

- connect the organization's cloud accounts or clusters to the platform
- define the building blocks developers may consume: templates, stacks, resource definitions, golden-path catalogs, defaults and guardrails
- manage tenancy: onboard teams, set roles and permissions, connect identity providers
- evolve the platform's standards over time without breaking the developers' experience

**Application developers** (consuming role):

- create projects and applications, deploy services, obtain databases and other dependencies
- get preview and staging environments for their changes
- view logs and metrics for what they deployed
- never (or rarely) touch the underlying infrastructure tooling directly

**Secondary roles**: engineering leadership (adoption, delivery metrics, cost visibility), security/compliance functions (policies, audit), and — increasingly — AI coding agents operating the same platform through agent interfaces on the developer's behalf.

The context is a software organization large enough that infrastructure requests have become a bottleneck: the IDP exists to remove that bottleneck by making the platform team's standards self-serviceable.

## Core Model

### The Defining Core

```text
Organization (the operator's scope)
└── Platform team configures:
    │   abstraction layer — templates / stacks / resource definitions / golden paths
    │   tenancy — teams, roles, identity
    │   substrate connections — cloud accounts, clusters
    ▼
Developer self-service consumption
    │   via console / CLI / API / Git
    ▼
Provisioning machinery of record
    │   turns requests into running software
    │   holds deployment state
    ▼
Running software on the organization's infrastructure
    ├── Environments (dev / staging / production / ephemeral)
    ├── Workloads / services (the developer's applications)
    └── Dependencies (databases, caches, queues, networking)
```

**The organization as operator.** The platform is bound to one organization: its members, its teams, its cloud accounts or clusters, its standards. This is what the "internal" names. A public cloud-vendor PaaS serves any customer with the vendor's generic abstractions; an IDP serves one organization with that organization's own abstractions.

**Developer self-service consumption.** The developer's unit of work is the application and its runtime needs — "deploy this service", "give me a database", "give me an environment for this pull request". The developer expresses these in the platform's terms and the platform acts. No ticket, no queue, no handoff to an operations team for routine requests. This is the property that separates the IDP from every ops-facing tool that merely *could* provision things.

**Provisioning machinery of record.** The platform is the executing counterpart: it builds or takes in artifacts, provisions the runtime pieces, wires them together (connection strings, DNS, secrets), keeps them running, and remembers what is deployed where. It is not a front over someone else's executor — when the developer asks for a database, the platform's own machinery creates it and records it.

**The organization-defined abstraction layer.** The platform team encodes the organization's standards as reusable building blocks. A developer consuming a "service" template gets the organization's way of running a service — its security policies, its resource defaults, its deployment pattern — without the organization's way being renegotiated per request. The abstraction layer is what makes the platform *opinionated* and what makes it the organization's own rather than generic.

### Standard Capabilities

Mature products commonly add, without these defining the Type:

- **Environments as managed objects** — named stages (development, staging, production) per project or application, each a coherent, addressable deployment context
- **Git-integrated build and deploy** — push to a branch triggers build and deployment; GitOps posture
- **Managed dependencies** — self-service databases, caches, message queues, with connection data automatically wired into the consuming application
- **Build machinery** — source code to container image (or artifact intake from external CI systems)
- **Multi-tenancy** — teams or projects sharing the platform with role-based access control and single sign-on
- **Networking and exposure** — domains, TLS certificates, ingress handled by the platform
- **Secrets and configuration management** — environment variables and secrets at project, environment, and service levels
- **Developer-level observability** — logs and metrics for deployed workloads, without separate tooling setup
- **Interface parity** — the same control plane reachable through web console, CLI, API, and infrastructure-as-code tooling
- **Cost visibility** — spend attributed to projects and environments

### One Structure, Many Implementations

```text
Concept:      Organization-defined abstraction layer
Realized as:  resource definitions + workload profiles (orchestrator-style),
              stacks + configuration forms (portal-suite style),
              Helm-chart catalogs as golden-path templates (pre-built-platform style),
              IaC/stack templates (managed-platform style),
              opinionated defaults (self-serve style)

Concept:      Provisioning machinery
Realized as:  a dedicated orchestration engine with a resource graph,
              a control plane driving build→deploy→run,
              operators + GitOps state management on the cluster

Concept:      The organization's infrastructure substrate
Realized as:  customer cloud accounts, customer Kubernetes clusters,
              vendor-operated cloud dedicated to the customer's tenancy,
              on-premise / self-hosted installations
```

A reader who has only seen one implementation — say, a Kubernetes-based IDP with a service catalog — should still be able to recognize the others from the core model.

## How It Works

The IDP runs as two interlocking loops: a configuration loop owned by the platform team, and a consumption loop owned by developers.

### Loop 1 — The platform team configures the platform

```text
Connect the substrate
→ (cloud accounts, Kubernetes clusters, identity provider)
→ Define the abstraction layer
→ (templates / stacks / resource definitions: what a "service" is,
   what databases may be provisioned, what defaults and guardrails apply)
→ Onboard teams
→ (tenancy, roles, quotas)
→ Publish
→ (the building blocks become self-serviceable)
→ Evolve
→ (standards change in one place; every consumer gets them on the next deployment)
```

This loop is continuous but low-frequency. Its output is the catalog of things developers can consume and the rules under which they can consume them.

### Loop 2 — The developer consumes the platform

```text
Create or open a project
→ describe the application
→ (source code in Git, or a container image; resource needs in the
   platform's terms — often by picking a template from the catalog)
→ deploy
→ the platform builds the artifact, provisions the declared resources
   (compute, database, networking, secrets), wires them together,
   and starts the workload
→ operate
→ (logs, metrics, scaling, configuration changes, rollbacks —
   all through the platform's surfaces)
→ iterate
→ (every push re-runs the deploy path; the platform reconciles
   the running state with the declared intent)
```

The developer never leaves the platform's abstraction: they describe *what* should run and *which* building blocks it needs; the platform decides *how* it maps onto the infrastructure, per the configured standards.

### The environment lifecycle

Environments are the platform's organizing rhythm for change:

```text
A change is proposed (pull request)
→ an ephemeral environment is created for it
   (in products that offer preview environments; created automatically
    per proposed change and disposed of when the change merges)
→ the change merges
→ it promotes through the standing environments
   (development → staging → production, by pipeline or promotion policy)
→ production runs under the platform's guardrails
   (health checks, rollbacks, zero-downtime replacement)
```

Standing environments persist; ephemeral ones exist per change. Both are platform-managed objects — the developer requests them, the platform creates, configures, and disposes of them.

### Core vs Common vs Optional

**Defining core** — without these, not an IDP:

- the organization as operator (platform team + org infrastructure + org's own developers)
- developer self-service consumption
- provisioning machinery of record
- the organization-defined abstraction layer

**Standard capabilities** — present in most mature products:

- environments as managed objects; Git-integrated build/deploy; managed dependencies; multi-tenancy with RBAC/SSO; networking/exposure; secrets management; developer observability; interface parity; cost visibility

**Common variants / optional** — depends on product philosophy, customer scale, and era:

- where the platform runs (vendor-managed cloud / customer cloud accounts / self-hosted)
- runtime substrate (Kubernetes-centric dominant; broader substrates exist)
- portal surface included or sold separately
- ephemeral preview environments as a default posture
- service catalog UI; scorecards; compliance/policy modules; FinOps/GreenOps depth
- AI-agent interfaces (agent skills, natural-language operation) — era-current

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Administration / platform-team surface

The configuring role's home.

- substrate connections (cloud accounts, clusters), the abstraction layer (templates, resource definitions, stacks), tenancy (teams, roles, identity), platform-wide settings and policies
- primary actions: connect infrastructure, author and version building blocks, onboard teams, set guardrails

### Developer console / self-service surface

The consuming role's home — in some products a general console, in others a catalog-first portal.

- projects and applications; the catalog of consumable building blocks; environment views with deployment status; workload detail (logs, metrics, configuration)
- primary actions: create/deploy a service from a template, obtain a dependency, open/inspect environments, roll back, scale

### Environment view

The state of one deployment stage.

- the services and dependencies running in that environment, their versions, health, and recent deployments; configuration and secrets scoped to the environment
- primary actions: deploy to the environment, promote a change into it, inspect or adjust configuration

### CLI / API / infrastructure-as-code interface

The same control plane without the console — the parity layer.

- commands or resources for projects, services, environments, and deployments; usable from scripts, pipelines, and AI agents
- primary actions: everything the console does, expressed programmatically

### Git as an interface

The dominant trigger surface.

- pushes to branches trigger builds and deployments; the platform reads its configuration from or writes its state to Git in GitOps postures

## Important Rules / Behaviors

### The self-service boundary is configured, not absolute

What developers may self-serve — and within what limits — is defined by the platform team's abstraction layer. A developer can obtain a database *because* the platform team made a database class consumable; the size, type, and policy constraints they operate under are the platform's configured guardrails, not the developer's choice. Self-service and governance are two sides of the same mechanism.

### The platform holds the deployment state

What is deployed where, in which version, with which configuration — the platform is the record. Redeploying, rolling back, and promoting are operations against this state. This is why the IDP is machinery, not just a surface: a portal that only displays or triggers external systems does not hold this state.

### Standards change centrally; consumption follows

When the platform team changes a building block — a new security policy, a new default — the change takes effect through the platform's deployment path, not by developers re-tooling individually. The abstraction layer is the point of control for org-wide standards.

### Environments are disposable or standing, never ad hoc

Ephemeral environments are created and destroyed by the platform around the change lifecycle; standing environments persist and are promoted into. Developers do not hand-build environments — that is the ticket-driven pattern the Type replaced.

### Multi-tenancy is structural

Teams share the platform (often the same clusters) with isolation enforced by the platform — namespaces, projects, roles, quotas. The isolation model is a platform-team concern; developers work inside their team's scope.

### The substrate stays reachable but abstracted

The platform runs on real cloud accounts and clusters, and platform engineers can reach the substrate directly. Developers normally cannot — and do not need to. The abstraction layer is precisely the line between the two.

## Variants

- **Engine / orchestrator pole** — the product sells the provisioning machinery only; the portal surface and other layers are separate products or integrations. The IDP is assembled from the engine plus companions.
- **Self-serve BYOC pole** — the product is a complete developer platform that runs on the customer's own cloud accounts or clusters; startup and mid-market friendly, self-service from day one.
- **Managed-platform pole** — the product offers its own managed cloud as the default substrate with customer-cloud (BYOC) as an option; strongest "batteries-included" developer experience.
- **Unified portal + platform pole** — the product packages the developer-facing portal (catalog, forms, governance views) and the platform machinery as one offering; common in enterprise and sovereignty-sensitive segments, frequently self-hostable.
- **Open-source / pre-built platform pole** — a pre-assembled, self-hostable stack of open-source components with a portal and golden-path catalogs; the organization installs it on its own clusters and adapts the catalogs.
- **The in-house assemblage (concept register)** — the organization composes its IDP from a portal, an orchestrator, IaC, and CI/CD. This is the usage of "IDP" as a concept; the product Types above are what vendors sell to serve it.
- **Era-current layer** — AI-agent interfaces (deploy and operate via coding agents and natural-language servers) are appearing across poles; a capability layer, not a pole of its own.

A variant remains a variant while the four-part defining core holds. If the developer-facing surface grows into the product's center (catalog, scorecards, docs as the point), the product has moved toward the Internal Developer Portal Type; if the machinery is consumed only by ops, it has moved toward infrastructure automation.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Internal Developer Portal | sibling; complementary and commonly bundled | portal = the developer-facing surface (service catalog, scorecards, docs, scaffolding) that integrates with other tools; IDP = the machinery that provisions and runs the software and holds deployment state. Vendor documentation in the engine pole describes the two as complementary — the portal as the self-service go-to place, the platform as the backend that provisions |
| Platform-as-a-Service (no dedicated leaf; Heroku-class) | adjacent, often confused | PaaS = vendor-owned runtime with the vendor's generic abstractions; IDP = the organization's own platform with org-defined abstractions over org infrastructure. An org-run PaaS foundation is the IDP's thin ancestor; a public PaaS is not an IDP |
| Cloud Management Platform | adjacent, different user | CMP = ops-facing control layer over cloud estates (inventory, governance, cost); IDP = developer-facing consumption of runtime capabilities. Different primary user; an IDP may sit atop the accounts a CMP governs |
| Infrastructure Automation Platform | adjacent, different user | automation platform = governed execution of automation content against a managed estate, consumed by ops; IDP = developer self-service consumption through org abstractions. IDP orchestrators commonly use IaC/automation as drivers underneath — integration, not identity |
| Continuous Delivery Platform | overlapping capability | CD centers the versioned deliverable moving through environments; the IDP centers the developer's runtime platform and may include or integrate CD. If the pipeline/deliverable is the center, it is CD; if the platform developers consume to run software is the center, it is an IDP |
| Dev Container / Workspace Platform | adjacent lifecycle stage | dev containers center the development-time environment (where code is edited and debugged); the IDP centers runtime environments (where software runs after commit) |
| Low-code Application Platform | different users entirely | low-code centers business-app construction by non-professional builders; the IDP centers professional software delivery infrastructure |
| Kubernetes Management Platform | substrate relationship | cluster-level operations vs the developer-facing app/service abstraction above the cluster; IDPs run on and manage Kubernetes as substrate |

The boundary with the **Internal Developer Portal** is the most important one: the market sells both separately and combined, and the vocabulary is contested. The structural test is the center of gravity — the surface (catalog/scorecards/docs) versus the machinery (provisioning and deployment state).

## Representative Products

- **Humanitec Platform Orchestrator** — the engine pole; sells the provisioning machinery that "powers" an IDP, with portals positioned as complementary surfaces
- **Qovery** — self-serve IDP running on the customer's own cloud accounts or clusters
- **Northflank** — managed developer platform / IDP product; managed cloud and bring-your-own-cloud
- **Cycloid** — unified Internal Developer Portal & Platform packaging; enterprise and sovereignty-focused segment
- **Akamai App Platform for LKE** (Otomi lineage) — open-source / pre-built Kubernetes developer platform, self-hosted on the organization's clusters

The defining core was checked against the org-run internal PaaS of the previous generation (Cloud Foundry) to avoid over-fitting to the current Kubernetes-and-catalog packaging.

## Sources

Research date: **2026-09-08**

- Humanitec — Platform Orchestrator documentation: overview and "How Humanitec relates: Backstage, Port, Cortex etc." — https://developer.humanitec.com/platform-orchestrator/docs/platform-orchestrator/overview/ , https://developer.humanitec.com/platform-orchestrator/docs/humanitec-vs-others/backstage-port-cortex-etc./
- Qovery — documentation: Introduction, Core Concepts, How Qovery Works — https://www.qovery.com/docs/ , https://www.qovery.com/docs/getting-started/basic-concepts , https://www.qovery.com/docs/getting-started/how-it-works
- Northflank — homepage and "Internal developer platform" product page — https://northflank.com/ , https://northflank.com/product/idp
- Cycloid — homepage — https://www.cycloid.io/
- Akamai App Platform for LKE — Welcome page (otomi.io redirects here) — https://techdocs.akamai.com/app-platform/docs/welcome
- Cloud Foundry — overview (historical anchor) — https://docs.cloudfoundry.org/concepts/overview.html

> Sourcing limitations: Northflank and Cycloid evidence is product-page depth (their documentation sites were not fetched); no precise operational parameters, plan limits, or pricing are asserted. Analyst definitions of "internal developer platform" vs "internal developer portal" were not directly accessible; the portal-vs-platform seam rests on vendor documentation and market structure. Detailed product-by-product observations, the cross-product comparison matrix, and the abstraction analysis are recorded in the paired Research Notes.
