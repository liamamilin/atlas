# Cloud Security Posture Management / CSPM

## Overview

A **Cloud Security Posture Management (CSPM)** application is a security system of record for the *configuration* of an organization's cloud estate. It connects to cloud environments (accounts, subscriptions, projects) with authorized read access, maintains an inventory of cloud resources and their current configuration, continuously evaluates that configuration against security policies and best-practice benchmarks, and tracks every resulting misconfiguration as a finding that is triaged, assigned, accepted, or remediated until the environment passes.

It exists because of the shared-responsibility reality of cloud computing: the cloud provider secures the infrastructure, while the customer is responsible for how resources are *configured* — public storage buckets, permissive network rules, over-broad identities, unencrypted datastores, unguarded management APIs. Most cloud breaches exploit exactly these configuration mistakes. A CSPM makes the configuration state visible, judges it continuously against known-good practice, and drives it toward compliance.

The boundary is configuration, not behavior: a CSPM judges *how resources are set up*, not what is happening on them at runtime, and not which software flaws they contain. When a product adds runtime threat detection, workload sensors, or identity-entitlement analytics, it is expanding into neighboring types (CWPP, CIEM) or bundling them into a broader platform (CNAPP).

## Users & Context

Primary users:

- **Cloud security engineers / security teams** — the main operators. They connect cloud accounts, tune policies, review findings, accept residual risks, and drive remediation across teams.
- **Cloud platform / DevOps engineers** — receive findings (directly or via ticketing) about resources they own, and fix the configurations, since they are the ones who create and change cloud resources.
- **Compliance and audit stakeholders** — consume the standards-mapped views (benchmark and regulatory frameworks) and compliance reports as evidence of the cloud estate's state.

Secondary roles include security leadership (posture scores and trend dashboards as program-level reporting) and resource owners who are assigned remediation tasks in products with governance features.

The work context is a multi-account cloud estate — typically many AWS accounts, Azure subscriptions, or GCP projects spanning teams and environments. Resources are created and changed constantly by automation and engineers, so configuration drift is continuous; this is why posture assessment is a standing, re-evaluating practice rather than a periodic audit.

## Core Model

### The defining core

```text
Connected cloud environment (read-authorized)
└── Resource inventory with configuration state
    └── Policy / control library
        └── Evaluation of each resource's configuration against each control
            └── Misconfiguration finding (resource × failed control, with severity)
                └── Tracked lifecycle: triage → assign / accept → remediate → resolved
```

Four structures. Remove any one and the product stops being a CSPM:

- **Connected cloud environment** — a standing, credential-authorized read connection into the customer's cloud, established through the provider's own management APIs and identity mechanisms (roles, service principals, or configuration recorders the provider operates). Without this, there is no cloud estate to have posture about.
- **Resource inventory with configuration state** — the discovered resources (compute instances, storage, networks, databases, identity objects, serverless functions, and more) held inside the application as data, each with its current configuration. This inventory is the substrate everything else evaluates.
- **Policy-driven configuration evaluation** — a library of security policies or controls — provider best practices, industry benchmarks, custom rules — that is checked against the configuration of each resource. A control either passes or fails per resource.
- **Misconfiguration findings with a managed lifecycle** — a finding binds one affected resource to one failed control, carries a severity, persists until the configuration passes (or the risk is formally accepted), and is re-evaluated as the environment changes. This is what makes it *management* rather than a scan report.

### Standard capabilities mature products add

Mature products commonly carry most of the following. They make a CSPM practical, but they are not what makes it a CSPM:

- **Compliance framework mapping** — the same control failures re-presented against industry benchmarks and regulatory frameworks (CIS-style benchmarks, PCI DSS, NIST-based standards, and provider-authored best-practice standards), with per-framework views, compliance reports, and custom standards in some products.
- **Posture scoring** — a summary score over the whole estate (percentage of passing controls, or a weighted security score), with trend views to show improvement or regression over time.
- **Severity and prioritization** — a severity on each finding, plus views that surface the worst resources, the most-failed controls, and the highest-severity backlog.
- **Remediation guidance** — each finding explains what is wrong and how to fix it (often with the exact console path or CLI command); some products can execute the fix automatically or hand it to automation.
- **Risk acceptance / suppression** — a managed state for findings the organization deliberately tolerates, with the acceptance recorded rather than silently ignored.
- **Scoping and multi-account machinery** — groupings of accounts/clusters/applications into business-facing scopes, central aggregation across accounts and regions, and role-based administration (which teams see and manage which parts).
- **Outbound workflow integrations** — routing findings to ticketing systems (Jira, ServiceNow, PagerDuty-style), chat, and SIEM/event buses so posture work lands in existing operations processes.
- **IaC / shift-left controls** — evaluation of infrastructure-as-code definitions in source control or pipelines, so misconfigurations are caught before resources are created, often with links connecting the code change to the resulting cloud finding.
- **Inventory exploration and query** — filters, saved views, and query languages over the resource inventory and the finding set.

### One structure, many implementations

The core model is written conceptually. Products implement each concept differently, and the differences are where product philosophies diverge:

```text
Concept:                    Connected cloud environment
Implementations:            role/service-principal authorization to read cloud APIs,
                            provider-operated configuration recorders,
                            agentless snapshot-style collection,
                            (in runtime-focused siblings: deployed sensors)

Concept:                    Policy / control library
Implementations:            provider-native best-practice standards,
                            industry benchmark packs (CIS, PCI DSS, NIST families),
                            custom rules in product-specific query languages or visual editors,
                            pipeline/IaC variants of the same controls

Concept:                    Finding
Implementations:            "noncompliant resource" (rule × resource),
                            "control finding" (control × resource),
                            "recommendation",
                            "alert" with status reasons and state-change notifications

Concept:                    Posture score
Implementations:            secure score over weighted controls,
                            passing-percentage of controls by severity,
                            per-scope or per-zone score trends
```

A reader who has only seen one implementation — for example a cloud provider's built-in dashboard — should still be able to recognize a third-party multi-cloud product, or an open-source configuration scanner, as the same application type from the core model.

## How It Works

### Connect the cloud environment

```text
Choose the cloud environment to protect
→ create a provider-side identity (role / service principal) granting read access
→ or enable the provider's own configuration recorder
→ the CSPM establishes the standing connection
→ first inventory discovery runs
→ optionally connect sibling clouds the same way
```

Onboarding is the product's front door. The connector's permissions are read-oriented for posture purposes; broader permissions are only needed when the product will also *act* (automatic remediation, response). Organization-level onboarding — enrolling an entire cloud organization or tenant rather than one account — is the common mature pattern for larger estates.

### Maintain the inventory and configuration state

Once connected, the CSPM keeps a current picture of what exists and how it is configured: resource types, attributes, and relationships (which instance is in which network using which security group, which role can access which bucket). In some implementations this is a continuous configuration stream; in others, recurring collection passes. Either way, the inventory is re-queried as the environment changes, so new, modified, and deleted resources flow through automatically.

### Evaluate configuration against policies

```text
For each discovered resource
  for each applicable control in the policy library
    → check the resource's configuration against the control's conditions
    → pass: nothing surfaces
    → fail: create or update a finding (resource × control)
```

Evaluation is ongoing, not one-shot: resources are re-evaluated as they are created, changed, or deleted. A resource that was failing and is fixed stops producing a failing finding; a change that breaks a previously passing resource produces a new one. This re-evaluation loop is the pulse of the product.

### Triage and manage findings

Findings accumulate in a worklist. The operational loop:

```text
Review new findings (filter by severity, scope, control, resource)
→ investigate: what exactly is misconfigured, on which resource, why it matters
→ decide: remediate now, assign to an owner, or formally accept the risk
→ route: ticket in the ITSM system / message the owning team / export to the SIEM
→ track: finding stays open until the configuration passes or is accepted
```

Mature products support suppression and automation on this loop — automatically modifying or dismissing classes of findings that match criteria, and triggering external responses when specific findings appear.

### Remediate and verify

Remediation closes the loop. The finding's guidance tells the owner what to change; the change lands in the cloud (directly, or through the team's normal IaC pipeline); the next evaluation pass detects the corrected configuration; the finding resolves and the posture score rises. Some products execute remediation themselves under explicit configuration, and some enforce policy at deployment time (blocking non-compliant infrastructure before it exists), but the verify-and-resolve step is the common shape.

### Report the compliance posture

Alongside the operational loop runs a reporting loop: control results roll up into benchmark and regulatory views, scores, and trend charts. Compliance owners read these as evidence ("which controls fail against PCI DSS in this account set"), and leadership reads them as program direction (is the estate getting safer). Findings history, first-seen timestamps, and resolution records make the report auditable.

### Capability tiers

**Defining core** — without these, not a CSPM:

- connected cloud environment with read-authorized visibility
- resource inventory with configuration state
- policy/control evaluation of that configuration
- misconfiguration findings tracked over time with re-evaluation

**Standard in mature products** — the working toolkit:

- compliance framework mapping and reports
- posture scores and prioritization views
- remediation guidance, acceptance/suppression states
- multi-account scoping, RBAC, aggregation
- outbound integrations (ticketing, chat, SIEM, event buses)
- IaC / shift-left controls
- APIs, filters, and query languages

**Optional / advanced** — depending on product and customer tier:

- automatic remediation execution and deployment-time enforcement
- attack-path and relationship-graph analysis combining multiple weaknesses into reachable-risk narratives
- configuration history and drift timelines
- identity-entitlement (CIEM), data-aware (DSPM), AI-workload, and Kubernetes posture as sibling modules of the same platform
- vulnerability scanning bundled into the posture plan
- custom compliance standards and custom control authoring

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Account / environment onboarding

- Purpose: establish the read connection to cloud environments.
- Typical information: cloud provider, account/subscription/project identifiers, required provider-side roles and permissions, connection status and health.
- Primary actions: connect an environment, set up the provider-side identity, scope what is included, verify the connection.

### Findings list (the main working surface)

- Purpose: manage the misconfiguration backlog.
- Typical information: failed control, affected resource, resource platform and type, severity, scope (account/zone/subscription), first-seen time, acceptance state.
- Primary actions: filter and group, inspect a finding's detail, assign or create a ticket, accept risk, mark/trigger remediation, drill into the resource.

### Resource inventory explorer

- Purpose: see what exists and how it is configured.
- Typical information: resources by provider/type/category, configuration attributes, relationships, per-resource pass/fail summary.
- Primary actions: search and filter, open a resource's findings, inspect configuration and related resources.

### Posture overview / score dashboard

- Purpose: program-level visibility for security owners.
- Typical information: overall and high-severity posture scores, trend over time, worst resources/controls/categories, findings by severity.
- Primary actions: filter by scope/platform, drill down into findings, export or share views.

### Compliance / standards view

- Purpose: read the same evaluation results through benchmark and regulatory frameworks.
- Typical information: standards (e.g., CIS-style benchmarks, PCI DSS, NIST-based standards, provider best-practice standards), controls per standard, pass/fail status per control, per-scope compliance summaries.
- Primary actions: select a standard and scope, review failed controls, jump to findings, generate compliance reports.

### Policy / controls management

- Purpose: tune what is evaluated and how.
- Typical information: built-in control libraries grouped by framework and resource type, enabled/disabled state, severities, custom rules.
- Primary actions: enable/disable controls, adjust severity, author custom policies (query or visual editors), deploy policy packs.

### Administration

- Purpose: run the product itself.
- Typical information: users and roles, scope groupings, connection health, notification channels, integration targets, audit logs.
- Primary actions: manage roles and scopes, configure notification/forwarding targets, connect ITSM/SIEM, review product audit history.

## Important Rules / Behaviors

- **Posture is read-first.** The data path from the cloud environment into the CSPM is credential-authorized reading of configuration. Writing back to the cloud (auto-remediation, response) is a distinct, separately-granted capability — a meaningful security boundary in how these products are deployed.
- **Findings exist only from enablement forward.** Connecting a new environment yields findings from that point on; products do not retroactively reconstruct a compliance history before they had visibility.
- **A finding is bound to a resource–control pair.** It is not a free-floating ticket: it resolves when that resource's configuration next passes that control, and re-opens if the same resource fails again. Fixing the resource — not the finding — is what closes the loop.
- **Evaluation is continuous and change-driven.** Resource creation, modification, and deletion all trigger re-evaluation; the finding set is a live reflection of the estate, not a snapshot.
- **Acceptance is a recorded state, not silence.** Tolerated risks are explicitly marked as accepted, keeping the difference between "compliant", "remediated", and "accepted" auditable.
- **Coverage follows the connector.** A control can only be evaluated on resources the product can see; multi-region and multi-account coverage determine whether a framework is truly satisfied. (Some benchmark regimes are explicitly evaluated per region/account, so partial onboarding can produce misleadingly clean results.)
- **Severity drives attention, not truth.** The severity ladder prioritizes work; the same misconfiguration can rate differently across products' libraries, since severity assignments are the vendor's (or customer's) calibration, not a universal constant.
- **Two artifact families must not be confused.** Posture findings (configuration problems, standing state) are a different artifact family from runtime security alerts (observed events). Products that contain both keep them distinct even when both can flow to the same SIEM or ticketing queue.

## Variants

Common implementations of the type:

- **Platform-native posture** — the cloud provider's own posture tooling over its own cloud (configuration recorders, policy engines, security hubs/centers). Deepest integration and data access; single-cloud by construction.
- **Third-party multi-cloud CSPM** — one control plane across AWS, Azure, GCP, and sometimes additional providers; the canonical "unified posture" posture, usually connected agentlessly.
- **Standalone vs bundled** — CSPM sold alone, as a free tier of a cloud platform, as a paid plan within a cloud-security product, or as the posture pillar of a broader cloud-native application protection platform (CNAPP) that also carries workload protection, identity entitlement analytics, and data-aware posture modules.
- **Agentless-first vs sensor-heritage** — products born from cloud-API assessment vs products that grew out of runtime agents and added posture evaluation; both converge on the same core loop.
- **Shift-left-heavy deployments** — posture controls executed primarily in pipelines and source control (IaC scanning, admission enforcement), with the runtime inventory as the verification layer.
- **Regulated-industry and sovereign deployments** — heavier compliance mapping, data-residency constraints, and evidence-reporting needs.

A variant remains a variant as long as the core loop — connect, inventory, evaluate, findings — is intact. If the product's primary object becomes the running workload (agents, runtime behavior) or the SaaS tenant configuration or the data content itself, it has crossed into CWPP, SSPM, or DSPM.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| CNAPP | umbrella platform | CNAPP bundles CSPM with workload protection, identity/data posture, and runtime detection; CSPM is its posture core. Remove the non-posture pillars and a CSPM remains. |
| Cloud Workload Protection / CWPP | sibling module | CWPP defends running workloads (VMs, containers, serverless) with sensors and threat detection; CSPM evaluates standing configuration. |
| SaaS Security Posture Management / SSPM | object-domain sibling | SSPM evaluates configuration of SaaS applications (tenants, sharing settings); CSPM's object domain is cloud infrastructure resources. |
| Data Security Posture Management / DSPM | object-domain sibling | DSPM's assessed object is data stores and data sensitivity; often shipped as a module *inside* CSPM products. |
| Vulnerability Management | adjacent assessment | Vulnerability management assesses software flaws (CVEs) in installed software and images; CSPM assesses configuration choices. They coexist as sibling modules in many platforms. |
| Attack Surface Management | opposite vantage | ASM discovers and observes an organization's exposure from outside, without prior asset knowledge; CSPM evaluates inside connected accounts with granted credentials. Cloud connectors are the bridge, not the core. |
| Cloud Management Platform | operations sibling | CMPs provision, operate, and optimize cloud resources; CSPM judges their security configuration. Inventory overlaps; purpose does not. |
| Security Compliance Platform | program-level neighbor | Compliance platforms manage organizational compliance programs (obligations, audits, evidence, attestations); CSPM's compliance views are a technical control mapping, not a program workflow. |
| SIEM / SOAR | downstream consumer | SIEM correlates security events and logs for detection; CSPM evaluates configuration state. CSPM findings are commonly forwarded into SIEM/SOAR workflows. |
| Infrastructure-as-Code Platform | upstream neighbor | IaC platforms author and provision infrastructure; CSPM evaluates the same definitions and the resulting resources for risk. IaC scanning is the bridge capability. |
| Cyber Asset Management | inventory-centric neighbor | Asset management is inventory across all environments; CSPM is assessment-centric — inventory is one component of it. |
| Configuration Management (IT) | domain sibling | Traditional configuration/patch management targets OS and application configuration on hosts; CSPM targets cloud-native resource configuration. |

The most important boundary is CNAPP, because most modern "CSPM" products ship as CNAPP platforms. The structural test: posture evaluation of cloud resource configuration is the CSPM; every other pillar (runtime workload defense, identity entitlements, data posture) is an additional module layered beside it.

## Representative Products

- AWS Config + AWS Security Hub (the platform-native pole on AWS)
- Microsoft Defender for Cloud (cloud-native platform with free and premium CSPM plans across Azure, AWS, GCP)
- Sysdig Secure (third-party multi-cloud platform with an explicit CSPM Posture module)
- Prisma Cloud (third-party multi-cloud platform with a policy/alert-led CSPM pillar)
- FortiCNAPP, formerly Lacework (third-party multi-cloud platform, sensor-heritage)

These span the platform-native vs third-party poles, free-tier vs paid-plan posture, and agentless vs sensor-heritage philosophies. The core model was checked against the platform-native ancestors (provider configuration recorders and policy engines that predate the CSPM marketing term) to avoid defining the type by the current CNAPP packaging.

## Sources

Research date: **2026-09-07**

- Microsoft — "Microsoft Defender for Cloud Overview", Microsoft Learn — https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction
- AWS — "What Is AWS Config?", AWS Config Developer Guide — https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html
- AWS — "Introduction to AWS Security Hub CSPM", Security Hub User Guide — https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html
- Sysdig — "Posture Overview" and "Posture Findings", Sysdig Secure documentation — https://docs.sysdig.com/en/sysdig-secure/posture/overview/ , https://docs.sysdig.com/en/sysdig-secure/posture/findings/
- Prisma Cloud — documentation index (structure-level evidence) — https://docs.prismacloud.io/
- Fortinet — FortiCNAPP (formerly Lacework) documentation index — https://docs.fortinet.com/product/forticnapp

> Sourcing limitation: several prominent vendors' documentation could not be fetched from the research environment on 2026-09-07 (two agentless-CNAPP leaders' sites returned errors or JavaScript-only shells; one cloud provider's security-center docs timed out; Prisma Cloud and FortiCNAPP were captured at documentation-structure level rather than full page bodies). Claims about those vendors' internal mechanics are therefore not made. Precise operational details (control counts, numeric limits, pricing mechanics, plan entitlements) are intentionally not stated in this document; they remain, where observed, in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and boundary reasoning are recorded in the paired Research Notes.
