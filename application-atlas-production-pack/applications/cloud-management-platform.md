# Cloud Management Platform

## Overview

A **Cloud Management Platform (CMP)** is an administrative platform that operates as an independent management layer above cloud infrastructure. It connects cloud environments — public cloud accounts and/or private-cloud and virtualization platforms — as managed estates, maintains a unified inventory of the resources inside them, and provides for the provisioning and ongoing lifecycle operation of those resources through one shared console.

The problems it exists to solve are familiar to any organization whose infrastructure has grown beyond a single environment: resources scattered across providers, accounts, and teams; no single picture of what exists; provisioning that depends on whichever specialist knows that console; and governance rules that each team interprets differently. The platform's answer is to bring the estates themselves — not just their billing data, not just their automation code — under one control plane with consistent inventory, consistent provisioning, and consistent rules.

Three properties form the defining core. Remove any one and the product stops being recognizable as this type:

1. **Connected cloud estates** — the platform onboards external cloud environments (accounts, subscriptions, virtualization platforms) as integrations and operates above their APIs.
2. **A unified inventory** — the resources of those estates, whether discovered as already existing or provisioned by the platform, are visible and manageable in one place.
3. **Lifecycle operations on those resources** — the platform can both create new resources from defined specifications and operate existing ones through their working life, including retiring them.

Everything else commonly associated with the category — multi-cloud breadth, self-service catalogs, cost dashboards, policy engines, Kubernetes support, SaaS delivery — is standard modern equipment, not the definition. A platform managing a single private cloud, a self-installed on-premises product, or a tool with no cost module at all still fits the same shape; older and platform-native products confirm this.

## Users & Context

**Primary users** are the people who own the infrastructure:

- **Cloud / infrastructure administrators** connect cloud accounts and virtualization platforms, keep the inventory current, and maintain the platform's configuration.
- **Platform or automation teams** design what may be provisioned (templates, blueprints, catalog offerings), write the policies that constrain provisioning and operations, and build integrations with surrounding tools.
- **Service-provider operators** run the same machinery on behalf of customers, using tenant structures, white-labeling, and chargeback where the product offers them.

**Secondary users** are consumers of infrastructure:

- **Developers and application teams** request environments and resources through a self-service catalog, then manage their deployments with the day-2 actions the platform exposes.
- **Team leads and application owners** see what their teams hold, approve or are subject to approvals, and consume reports.

**Tertiary consumers** include finance and FinOps functions reading cost allocation and showback views where the platform (or its sibling product) provides them.

The typical context is a mid-size or large organization running more than one cloud environment — often public clouds alongside a virtualized private cloud — where the number of accounts, teams, and manual steps has outgrown provider-by-provider console work. Governance and audit requirements are usually part of the motivation: the organization wants provisioning to happen only through approved shapes, and wants a record of who provisioned what.

## Core Model

The platform's world is built from six kinds of things.

### Connected cloud estate

The onboarding unit. An administrator registers a cloud environment — a public cloud account with credentials, a virtualization platform, or a container platform — and the platform establishes an integration with it. From that point the estate's capacity (its regions, zones, clusters, or host pools) becomes deployable space, and the platform can read from it and, within granted authority, act on it. An organization typically connects several estates; the same mechanics apply whether the estate is a public cloud account or an on-premises virtualization cluster.

### Resource inventory

The estate as the platform sees it: the machines, networks, storage, and other resources that exist across all connected estates, gathered into one searchable picture. Two origins are distinguished:

- **Discovered resources** — things that already exist in the connected estate, found by the platform when it reads the provider. These may be *onboarded* so the platform can manage them going forward.
- **Provisioned resources** — things the platform itself created, which are managed from birth through the platform's lifecycle machinery.

This distinction matters operationally: discovered resources give the platform its completeness ("everything we have, in one place"), while provisioned resources carry the platform's full governance lineage.

### Organizational units and roles

Provisioning and operations are not open to everyone on everything. The platform organizes users into units — commonly called projects, tenants, or domains — that bind people to specific estates and permissions: which environments a team may deploy into, which definitions they may use, which actions they may perform. In service-provider deployments the unit hierarchy carries commercial meaning as well, separating one customer's estate from another's.

### Deployment definitions

What may be provisioned is defined once, as a reusable specification: a template or blueprint describing the machines, networks, and services to create, or an offering with fixed size and capability parameters. In modern products these definitions are frequently code-shaped — YAML documents edited on a canvas, or imports of infrastructure-as-code configurations — so that the same artifact an engineer can read is the artifact the platform executes at provisioning time.

### Deployment

The provisioned unit. When a request is fulfilled, the platform creates a deployment — a managed set of resources created from a definition, placed in a specific estate, owned by a project, with its own lifecycle state. The deployment is the handle through which consumers find what they run and through which administrators audit what exists.

### Governance rules

Constraints that apply at the moments of truth: approval requirements and quotas checked when a request is made; tagging rules and budget thresholds enforced when resources are created; policy conditions evaluated when day-2 actions are taken. Roles determine who; rules determine what is allowed regardless of who.

```text
Cloud account / virtualization platform
  ↓ connected as
Estate (integrations, zones/capacity)
  ↓ read from / act upon
Resource inventory (discovered + provisioned)
  ↑ provisioned from
Deployment definitions (templates / blueprints / offerings)
  ↓ fulfilled as
Deployment (managed, stateful resource set)
  └─ governed by
Organizational units + roles + policies (who may do what, where, and within which limits)
```

Concept and implementation are deliberately kept apart. A "connected estate" may be a cloud account authenticated by credentials, a virtualization platform reached through its management API, or a Kubernetes cluster; a "deployment definition" may be a YAML template, an imported Terraform configuration, or a fixed-size offering. The structure holds across all of these.

## How It Works

The platform's working life is a loop that runs from connection to retirement.

### 1. Connect a cloud environment

The administrator registers a cloud account or platform, supplying credentials or the integration the provider requires. The platform validates access and the estate's capacity — its regions, zones, or clusters — becomes deployable space. Several environments are connected the same way; from here on the platform is the aggregate view.

### 2. Discover the estate

The platform reads the connected estates and builds its inventory: resources that already exist appear as discovered records. Administrators can onboard discovered resources so they become managed going forward, even though the platform did not create them.

### 3. Organize and govern

Users are arranged into projects or tenants; roles are assigned; estates and capacity are made available to the units that should use them; policies, quotas, and budgets are put in place. This is the step that turns a view of infrastructure into a governed platform.

### 4. Define what may be provisioned

The platform team authors or imports deployment definitions — templates, blueprints, or offerings — and publishes the approved ones, often to a self-service catalog. Mature products commonly separate the administration surface where definitions are designed from the consumer surface where they are requested.

### 5. Request and provision

A consumer picks a catalog item or submits a request; the platform checks it against governance (approval, quota, budget) and, once cleared, creates a deployment — driving the actual resource creation through the connected provider's APIs. The new resources enter the inventory as provisioned resources belonging to the requester's project.

### 6. Operate day-2

For the rest of the resource's life, the platform is the operations surface: reconfigure, resize, power, snapshot, migrate, patch, and eventually retire — with the actions available on each resource governed by its class and current state. Orchestration features let teams automate these operations or trigger them from events.

### 7. Account and report

Usage and cost information — where the platform or its sibling module ingests provider billing data — is attributed to projects and owners through tags and allocation rules, feeding showback, chargeback, and optimization reports. Audit records of who did what remain available for compliance.

### Capability tiers

**Defining core** — connected estates, unified inventory, provisioning plus day-2 lifecycle operations, one console.

**Standard capabilities** — present in essentially all mature products:

- self-service catalog with request forms and approvals
- projects/tenants with role-based access control
- governance policies, quotas, budget thresholds, tagging enforcement
- a broad day-2 action vocabulary per resource class
- aggregation across multiple providers and private-cloud/hypervisor platforms (and, commonly, Kubernetes)
- integration fabric: ITSM, identity providers, infrastructure-as-code tooling, monitoring, backup, DNS/IPAM
- orchestration and extensibility (event-triggered actions, custom workflows, scripting)
- APIs and CLI alongside the console; dashboards, reports, audit trails

**Common variants / optional** — depends on product and customer:

- cost management depth (showback/chargeback, forecasting, optimization recommendations) — sometimes a bundled module, sometimes a sibling product
- Kubernetes-specific self-service depth
- service-provider packaging (multi-tenancy for resale, white-label portals, chargeback)
- SaaS delivery vs self-hosted installation
- AI-era assistance (natural-language queries over the estate, AI-surfaced anomalies)

## Interfaces

### Administration console

The operator's home. Purpose: connect and organize estates, maintain inventory, define and govern provisioning. Typical information: connected accounts and their status, resource inventory across estates, projects and roles, definitions and catalogs, policies and quotas. Primary actions: connect/disconnect estates, onboard discovered resources, create projects and roles, author and publish definitions, set policies, inspect any resource's details and history.

### Design surface

Where deployment definitions are built. Purpose: author the reusable specifications for provisioning. Typical information: definition structure (resources, networks, sizing), target estates and constraints, versions. Primary actions: create/edit a definition (commonly on a visual canvas backed by code), validate, version, and release it for catalog use.

### Self-service catalog

The consumer's entry. Purpose: request and manage what teams run without touching provider consoles. Typical information: published catalog items with descriptions and request forms, the user's deployments and their states, pending requests. Primary actions: request an item, monitor provisioning progress, perform day-2 actions on own deployments, retire a deployment.

### Resource inventory / explorer

The estate-wide picture. Purpose: find and inspect anything that exists across connected environments. Typical information: resources by estate, type, project, owner, tags, lifecycle state, cost attribution where available. Primary actions: search and filter, open resource details, perform permitted actions, onboard discovered resources.

### Policy and governance views

Where rules live. Purpose: keep provisioning and operations inside intended limits. Typical information: approval workflows, quotas per project, budget thresholds, tagging and compliance rules, policy violations. Primary actions: define rules, review violations and approvals, adjust limits.

### Reporting and dashboards

Purpose: give administrators, owners, and finance their respective views. Typical information: estate growth, deployment counts, cost allocation and trends (where cost is ingested), compliance posture. Primary actions: configure reports, drill into a project or estate, export.

### API and integrations

Every console capability is typically matched by an API, and the platform's integration fabric reaches outward: creating tickets in ITSM systems when requests need approval chains, delegating authentication to enterprise identity providers, importing infrastructure-as-code configurations, and forwarding operational events to monitoring tools.

## Important Rules / Behaviors

### The platform acts within granted authority

Every operation the platform performs executes through the connected estate's own APIs, using the credentials and permissions granted at connection time. The platform cannot do more to an estate than the integration allows; its reach is exactly the authority delegated to it.

### Discovered is not the same as provisioned

A resource that exists in a connected estate is not automatically governed by the platform's rules. Onboarding brings it into inventory management; the platform's full lineage — definitions, approvals, lifecycle history — belongs to provisioned resources. Products commonly restrict some operations (for example, wholesale reconfiguration) to resources the platform provisioned itself.

### Deployment state gates actions

A deployment carries lifecycle state, and the available day-2 actions follow from it: a running machine can be stopped or resized but not started; a retired deployment cannot be modified further. The exact state names and action sets vary by product, but the state-gated structure is general.

### Governance is enforced before provisioning, not after

Approvals, quotas, and budget checks evaluate the request before resources are created. This is the mechanism by which the platform makes "everything goes through approved shapes" true in practice rather than in policy documents.

### Visibility follows membership

What a user can see and do is bounded by their project or tenant membership and role. The platform is multi-user by construction: estate-wide visibility is an administrator property, not a default.

### Cost is derived data

Where cost views exist, they are computed from provider billing information ingested through the integrations, attributed to projects and owners via tags and allocation rules. They are only as complete as the billing feeds and tagging discipline behind them — which is why tagging enforcement is a governance feature rather than a hygiene nicety.

## Variants

The type is implemented along several axes:

- **Philosophy of emphasis.** Automation-suite-led products build the platform around design-as-code, catalogs, and workflow orchestration. Governance-and-provisioning-led products lead with unified control and policy enforcement across heterogeneous environments. Some vendors embed cloud management inside an IT operations or service-management suite, where requests and approvals live in the service desk. Two adjacent philosophies — cost-first tools and infrastructure-as-code operations platforms — drift out of the type entirely (see Related Application Types).
- **Delivery posture.** Vendor-operated SaaS, self-installed software (appliance or cluster), and open-source platforms that are themselves cloud infrastructures all exist; the defining core is posture-independent.
- **Audience.** Enterprise IT is the center of gravity, but service providers and managed service providers are a distinct variant: multi-tenant operation for resale, white-labeled consumer portals, and chargeback as a commercial mechanism rather than a report.
- **Estate composition.** Products differ in heritage — some grew up managing virtualized private clouds and added public clouds; others were built multi-cloud first. Kubernetes may be a first-class estate member with dedicated self-service, a shallow integration, or absent.
- **Commercial shape.** Freemium entry tiers with resource caps, per-resource licensing, and suite bundling (with cost management or security sold as sibling products) all occur.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Infrastructure-as-Code Platform | adjacent — shares provisioning | manages code artifacts and runs (plans, applies, state) as its primary objects; has no estate inventory or per-resource lifecycle console. A CMP integrates IaC as one provisioning mechanism while the estate itself remains the managed object |
| Cloud Cost Management / FinOps | adjacent — shares the estate | manages spend and billing data, allocation, and optimization recommendations; does not provision or operate resources. Cost-first products often carry the CMP label in marketing but lack the lifecycle core |
| Native cloud provider console | baseline comparison | a provider's own console manages one provider from inside it; a CMP is an independent layer aggregating multiple estates and adding cross-estate governance |
| Virtualization Management | adjacent | performs hypervisor- and host-specific operations; a CMP treats virtualization platforms as estate members among others rather than as the whole scope |
| Kubernetes Management Platform | adjacent | cluster- and workload-specific management; a CMP may include clusters as estate members but does not replace cluster-specific tooling |
| Infrastructure Monitoring / APM | complementary | observes health and performance of the estate; a CMP changes the estate. The two integrate — alerts in a CMP typically come from an integrated monitoring product |
| IT Service Management / ITOM | adjacent — integration partner and possible container | provides the service-desk and process layer; CMPs integrate with ITSM for approvals and records. Where cloud management is embedded in an ITOM suite, the same core structure applies underneath |
| Server Management Platform | adjacent | manages individual machines at the OS level through agents; a CMP manages cloud resources through provider APIs at the estate level |
| Infrastructure Automation Platform | overlapping vocabulary | runbook and script automation across infrastructure; lacks the estate inventory, catalog governance, and lifecycle ownership that define a CMP |

The most consequential boundary is with the IaC platform, because both create cloud resources. The test is the managed object: if the product's primary surfaces are code, state, and runs — and the estate appears only as the place runs land — it is an IaC platform; if the primary surfaces are the estates and their resources — inventory, lifecycle, governance — it is a CMP, however much IaC it imports.

## Representative Products

- **VMware Aria Automation** — automation-suite-led platform; now delivered as part of VMware Cloud Foundation Automation. Researched through its official documentation (Assembler/Service Broker structure).
- **CloudBolt CMP** — governance-and-provisioning-led platform spanning public clouds, hypervisors, and Kubernetes, with a strong service-provider/reseller variant. Researched through official product surfaces.

Boundary and historical anchors used during research (not core samples): **Scalr** (infrastructure-as-code operations backend — the IaC pole), **IBM Turbonomic** (continuous resource optimization — the assurance pole), **Apache CloudStack** (open-source cloud platform whose own control plane historically shared the "cloud management platform" name — the platform-native sense).

## Sources

Research date: **2026-09-07**

- Broadcom — VMware Aria Automation 8.18 documentation (overview, Using Automation Assembler, Using Automation Service Broker): https://techdocs.broadcom.com/us/en/vmware-cis/aria/aria-automation/8-18.html
- CloudBolt — product pages and documentation portal: https://www.cloudbolt.io/ , https://www.cloudbolt.io/cloudbolt-cmp/ , https://docs.cloudbolt.io/
- Scalr — documentation: https://docs.scalr.io/
- Apache CloudStack — documentation: https://docs.cloudstack.apache.org/en/latest/
- IBM Turbonomic — product page: https://www.ibm.com/products/turbonomic

> Sourcing limitations: official operational documentation for two widely cited products (Morpheus Data, ServiceNow Cloud Management) could not be fetched from the research environment (repeated timeouts); they are treated as market context only and no product-specific claims about them are made. CloudBolt's documentation portal gates article bodies behind JavaScript, so its workflow detail rests on official product pages rather than operational docs. Consequently, no precise operational figures (provider counts, limits, defaults, pricing) from any single product are asserted in this document; claims are calibrated to what the fetched sources directly support.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical market-sample check are recorded in the paired Research Notes.
