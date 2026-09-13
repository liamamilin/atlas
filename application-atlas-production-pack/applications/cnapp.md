# CNAPP (Cloud-Native Application Protection Platform)

## Overview

A **CNAPP (Cloud-Native Application Protection Platform)** is a security platform that unifies several previously separate cloud security functions — configuration posture management, workload threat protection, vulnerability management, identity-entitlement analytics, and often data security — into a single product operating on one shared inventory of the customer's cloud estate, with the resulting risks correlated, prioritized, and managed as one picture.

The distinguishing structure is the **unification itself**. Each function inside the platform also exists as a standalone application type (a cloud security posture manager, a workload protection product, an identity-entitlement analyzer); what makes a product a CNAPP is that these domains are evaluated against one shared estate data model and operated from one platform — one console, one policy framework, one administration plane — rather than as separately operated point tools sold side by side.

The category exists because cloud-native estates are attacked across these domains in combination: a critical vulnerability matters most when it sits on an internet-exposed workload with an over-privileged identity; a misconfiguration matters most when it opens a path to sensitive data. Point tools produce siloed findings; the platform's job is to join them into a single, prioritized view of real risk.

The boundary is structural: remove the extra domains and a single-domain tool remains (posture management or workload protection); remove the shared inventory and single risk picture — separate consoles and separate data — and what remains is a portfolio, not a platform.

## Users & Context

Primary users:

- **Cloud security engineers** — the platform's main operators. They connect cloud accounts, deploy sensors where required, tune policies across domains, and own the unified risk picture.
- **SOC analysts / incident responders** — work the security-event queue produced by the runtime-protection domain, investigate incidents with the platform's correlation context, and execute containment.
- **DevOps / platform engineers** — receive and fix findings (misconfigurations, vulnerabilities, entitlement problems) on the resources and workloads they own; in some organizations they also deploy the platform's instrumentation.
- **Developers** — increasingly first-class remediation recipients: code-to-cloud linkage points runtime problems back to the repository, pipeline, or infrastructure-code that produced them.

Secondary consumers: compliance and audit stakeholders (framework-mapped reporting), security leadership (program-level scores, trends, adoption metrics), and resource owners assigned remediation work by the platform's governance machinery.

The working context is a multi-cloud estate — typically several cloud accounts, subscriptions, or projects across providers, spanning VM fleets, Kubernetes clusters, serverless functions, data stores, and the pipelines that deploy them. Because such estates change continuously and their risks interlock across domains, the platform is a standing operational system rather than a periodic audit tool. Adoption is usually driven by consolidation: replacing a set of separately operated cloud security tools with one platform.

## Core Model

### The defining core

```text
Connected cloud estate
└── Unified estate inventory (one data model spanning configuration AND running workloads)
    └── Multi-domain security evaluation (posture + other domains, on the shared inventory)
        └── Single risk picture (one place where all findings are correlated,
            prioritized, and operated)
```

Four properties. If any one is removed, the product is no longer recognizable as a CNAPP:

- **Connected cloud estate** — a standing, credential-authorized connection into the customer's cloud environments and the workloads running in them, established through provider APIs and identity mechanisms, with additional instrumentation (sensors) where a domain requires live visibility. Without the connection there is nothing to protect.
- **Unified estate inventory** — the estate held as *one* inventory: cloud resources and their configuration, the running workloads (hosts, containers, pods, functions), and — in mature products — cloud identities, data stores, API endpoints, and the code/pipeline origins of each. This shared substrate is what lets a finding in one domain reference context from another. Without it, the product is a bundle of separate tools.
- **Multi-domain security evaluation** — more than one security domain continuously assessed against that shared inventory. Configuration-posture evaluation is always present; the standard companions are workload vulnerability management, runtime threat detection, and identity-entitlement analytics. A product that evaluates only one domain is that domain's tool (a posture manager, a workload protector) — not a CNAPP.
- **Single risk picture** — the findings, events, and risks from all domains land in one place: one console, one policy framework, one alerting/forwarding path, one administration plane — where they are correlated, prioritized, and worked to closure. Without this, the product is a portfolio.

### The standard pillars

Mature platforms in this category commonly carry these domains. They are the expected contents of the unification, not each definitional:

- **Configuration posture (CSPM)** — continuous evaluation of cloud resource configuration against security policies and benchmarks, producing posture findings.
- **Workload vulnerability management** — discovery and scoring of software vulnerabilities in images, registries, pipelines, and running workloads, prioritized by runtime context.
- **Runtime threat protection (CWPP)** — sensors (or equivalent telemetry) watching running workloads for malicious behavior, producing security events, with an investigate-and-respond loop ending on the workload.
- **Identity-entitlement analytics (CIEM)** — inventory of cloud identities and their effective permissions, surfacing over-entitlement and identity-based risk.

Commonly added on top:

- **Data security posture** — discovery of data stores and classification of sensitive data as additional evaluation context.
- **API security posture** — inventory and risk assessment of exposed API endpoints.
- **Kubernetes posture** — cluster-level configuration and admission controls.
- **Code-to-cloud linkage** — connecting running resources to the repositories, pipelines, and infrastructure-as-code that created them.
- **External attack surface and internet-exposure analysis** — how the estate appears from outside.

### One structure, many implementations

The core model is written conceptually. Products realize each concept differently, and the differences are where philosophies diverge:

```text
Concept:                   Connected cloud estate
Implementations:           agentless API connections with provider-side roles,
                           provider-operated log/config pipelines,
                           deployed sensor families (host, cluster, serverless)

Concept:                   Unified inventory
Implementations:           asset inventory lists,
                           relationship graphs linking resources–workloads–identities–data,
                           per-domain inventories joined by a search layer

Concept:                   Single risk picture
Implementations:           security-graph attack-path analysis ("toxic combinations"),
                           cross-domain risk scores and prioritized issue lists,
                           unified alert queues with per-domain views

Concept:                   Cross-domain evaluation
Implementations:           one shared policy framework with per-domain policy families,
                           one query language spanning all domains,
                           per-domain dashboards over the same data
```

A reader who has only seen one implementation — a cloud provider's built-in security center, or an agentless graph product — should still be able to recognize the other shape as the same platform type from the core model.

## How It Works

The platform runs several loops at once. The most defining ones:

### Onboard the estate

```text
Connect cloud accounts (organization-wide where possible, via provider-side read roles)
→ choose instrumentation: agentless connection alone, or plus sensors for runtime domains
→ deploy sensors where used (cluster agents, host installers, embedded components)
→ connect registries, pipelines, and code repositories
→ verify coverage: which accounts, clusters, and workloads are visible to which domains
```

Onboarding is the platform's front door and its standing operational concern: what is not connected or instrumented is invisible to every domain at once, so coverage and connection health are first-class surfaces.

### Build and maintain the unified inventory

Once connected, the platform assembles the estate into one picture: discovered resources with their configuration, the workloads running on them, the identities that can act on them, the data they hold, and — where code-to-cloud linkage is active — the pipelines and repositories that produced them. The inventory updates continuously as the estate changes, and every domain's findings attach back to it.

### Evaluate each domain continuously

Each domain runs its own assessment loop against the shared inventory: posture controls check resource configuration; vulnerability scanning covers images, registries, and running workloads; runtime sensors (or cloud-log analytics) watch workload behavior and raise security events; entitlement analysis computes effective identity permissions. Each domain has its own policy families — but they live in one policy framework and write into one data model.

### Correlate and prioritize

This is the platform's signature step. Cross-domain context turns isolated findings into ranked, explainable risk:

```text
vulnerability on a package
  + running on an internet-exposed workload
  + reachable via an over-privileged identity
  + path continues to a sensitive-data store
→ one prioritized attack path, with the next best action
```

Mature platforms implement this idea in different shapes — relationship graphs, attack-path analysis, or cross-domain prioritization — and the market expectation is that the platform, not the analyst, performs the joining.

### Work the risk lifecycle

```text
Review the unified worklist (prioritized issues across domains)
→ investigate with the platform's context (graph, audit trails, related findings)
→ decide: remediate, assign to an owner, or formally accept the risk
→ route: ticketing/chat/SIEM forwarding; owner assignment via governance rules
→ remediate: fix in the cloud, or fix at source via code-to-cloud flows
  (some products generate a fix as a code change / pull request)
→ runtime events: contain on the workload (isolate, stop, quarantine), recorded and reversible
→ track: findings resolve when the underlying state passes; acceptance is a recorded state
```

### Report the program

Alongside operations runs the reporting loop: compliance frameworks computed over the same data, posture scores and trends, risk-priority dashboards, and — in some products — program-adoption views for leadership.

### Capability tiers

**Defining core** — without these, not a CNAPP:

- connected cloud estate
- unified estate inventory spanning configuration and workloads
- multi-domain evaluation (posture + at least one other domain)
- single risk picture in one platform

**Standard capabilities** — expected in mature products:

- the four standard pillars (posture, vulnerability, runtime protection, identity entitlements)
- cross-domain correlation and prioritization (attack paths / risk graphs)
- platform-wide search and query
- shared policy framework with per-domain policy families
- compliance framework mapping and reports
- findings/alerts lifecycle with SIEM/ITSM/chat forwarding
- scoping/RBAC machinery; SSO; audit trails
- remediation guidance and ownership routing

**Optional / common variants** — depending on product and customer:

- data posture, API posture, AI-workload posture, external attack surface
- runtime response actions and continuous enforcement (vs detection-only)
- self-hosted or air-gapped deployment
- AI assistants over search/investigation; workflow orchestration
- managed analyst services layered on the platform

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Overview / command-center dashboard

- Purpose: program-level entry — the state of the whole estate across domains.
- Typical information: overall risk and posture scores, trends, top prioritized issues, coverage/health indicators, domain summaries.
- Primary actions: drill into any domain or issue, filter by scope, export/share.

### Inventory / resource explorer

- Purpose: see the estate as one population — resources, workloads, identities, data, and their relationships.
- Typical information: resource and workload records with platform/type/ownership, protection and scan status, linked code origins, per-record risk summaries.
- Primary actions: search and filter, inspect a record's cross-domain context, open its findings.

### Prioritized risk / findings worklist

- Purpose: the operator's home — one ranked list across domains.
- Typical information: finding or event, affected resource/workload, domain, severity and computed priority, correlation context (exposure, privilege, data proximity), first-seen, state.
- Primary actions: triage, inspect attack path, assign/accept, route to ticketing, trigger remediation or response.

### Attack-path / graph views

- Purpose: visualize how weaknesses combine into reachable risk.
- Typical information: nodes (resources, identities, data) and edges (exposure, permission, trust), the path's business impact, suggested remediation points.
- Primary actions: explore, query the graph, break the path at a chosen node.

### Domain consoles

Posture findings, vulnerability findings, and runtime events each retain their own working views (the artifact families differ), even though they share inventory and routing. Runtime consoles additionally carry investigation artifacts (activity trails, captures) and the response-action surface.

### Policy management

- Purpose: one governance surface for all domains.
- Typical information: built-in policy/controls libraries per domain (posture controls, threat rules, vulnerability policies, entitlement checks, admission controls), enabled state, severities, scoping, custom rules.
- Primary actions: enable/tune/scope policies, author custom rules in the platform's query language, manage exclusions.

### Compliance views

- Purpose: read the same evaluation results through regulatory/benchmark frameworks.
- Primary actions: select framework and scope, review failing controls, generate reports.

### Administration

- Purpose: run the platform itself.
- Typical information: connected accounts and their health, sensor/agent fleets, users and roles, scope groupings, integration targets, licensing/plan state, audit logs.
- Primary actions: connect/disconnect environments, manage roles and scopes, configure forwarding targets, review plan entitlements.

## Important Rules / Behaviors

- **One estate, one data model.** The same resource appears across every domain's evaluation; findings in different domains reference the same inventory record. This shared reference is what makes cross-domain prioritization possible — and its absence is what makes a tool bundle not-a-platform.
- **Coverage follows the connection.** An unconnected account or uninstrumented cluster is invisible to all domains simultaneously. Products therefore expose connection/agent health prominently, and partial onboarding can silently narrow what the "unified" picture covers.
- **Domain enablement is incremental.** Platforms are typically licensed and activated per domain or per workload class; a deployment may start posture-only and add runtime later. The platform structure persists across this — but a deployment that never adds a second domain is, operationally, a single-domain tool.
- **Snapshot and live visibility are different guarantees.** Agentless collection sees configuration and point-in-time workload state; live behavioral detection requires deployed instrumentation. Mature platforms offer both and keep the distinction visible to the operator.
- **Artifact families stay distinct.** Posture findings (statements about state that resolve when state changes), vulnerability findings, and runtime security events (evidence of something that happened) are different record types with different lifecycles — kept in separate views even when they feed the same queues.
- **Priority is computed, not just declared.** The platform's distinctive severity comes from joining domains (exposure × vulnerability × privilege × sensitivity); the same finding's priority can change as context changes, and calibrated severities remain vendor choices rather than universal constants.
- **Acceptance is a recorded state.** Deliberately tolerated risks are marked as accepted with the decision retained — keeping "remediated", "compliant", and "accepted" auditable apart.
- **Read-first, act-deliberately.** Data flows from the cloud into the platform under read-oriented grants; acting on the estate (auto-remediation, runtime containment) is a separately granted, deliberately scoped capability whose executions are recorded.

## Variants

Common implementations of the type:

- **Platform-native CNAPP** — a cloud provider's own platform spanning its cloud (deepest integration) plus other clouds via connectors; often a free foundational tier with paid plan families per domain.
- **Agentless-first pure-play platforms** — independent vendors connecting via cloud APIs within minutes, building relationship-graph-based risk context; runtime protection added via sensors or cloud telemetry where adopted.
- **Runtime-heritage platforms** — products born from workload sensors and container security that grew posture, vulnerability, and identity domains around the same inventory; strongest in Kubernetes-heavy estates; sometimes deployable self-hosted.
- **Suite-heritage platforms** — security-suite vendors that unified previously separate products (posture, workload, code security) into one console and data plane.
- **Deployment variants** — SaaS-operated vs self-hosted/on-premises (including air-gapped); multi-cloud vs single-cloud-by-construction.
- **Scope variants** — estates weighted toward VMs, toward Kubernetes/containers, or toward serverless; regulated-industry deployments with heavier compliance and residency needs; managed-service layers on top.

A variant remains a variant while the core holds: multiple domains, one shared estate inventory, one risk picture. When the domains collapse to one, the product has become that domain's tool; when the shared data plane collapses into separate consoles, it has become a portfolio.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Cloud Security Posture Management / CSPM | posture pillar | CSPM evaluates standing configuration and produces posture findings; a CNAPP contains that as one domain and adds the unified cross-domain picture. Remove the other domains → a CSPM remains. |
| Cloud Workload Protection / CWPP | runtime pillar | CWPP defends running workloads with sensors, events, and response; inside a CNAPP it is one pillar feeding the shared inventory. Remove the other domains → a CWPP remains. |
| Identity-entitlement analytics (CIEM) | identity domain | Cloud-identity effective-permission analysis; usually shipped as a module inside CNAPPs, occasionally standalone. |
| Data Security Posture Management / DSPM | data domain | Data-store discovery and sensitivity analysis as evaluation context; a common CNAPP extension, also standalone. |
| Container & Kubernetes Security | object-domain specialization | Deep image/registry/admission/cluster security; a CNAPP carries the container slice inside the wider estate, often with KSPM as a domain. |
| Vulnerability Management | adjacent program | Enterprise-wide flaw programs span all assets; CNAPP vulnerability management is the cloud-native slice, prioritized by cloud context. |
| Security suite / tool portfolio | the boundary case | Multiple security products from one vendor with separate consoles, inventories, and policy engines = a portfolio. The shared inventory + single risk picture is the platform test. |
| SIEM / SOAR | downstream consumer | SIEM correlates event streams; SOAR orchestrates response. CNAPP forwards findings/events into them; its runtime pillar itself executes workload-level containment. |
| EDR / XDR | machinery sibling | Converged detection-and-response over endpoints/devices; CNAPP converges over the cloud-native estate. Machinery overlaps; object domain differs (some vendors' ecosystems now bridge both). |
| Attack Surface Management | opposite vantage | ASM observes exposure from outside without prior knowledge; CNAPP evaluates inside connected accounts with granted credentials. Exposure analysis inside CNAPPs is the bridging capability. |
| Cloud Management Platform | operations sibling | CMPs provision, operate, and optimize the estate; CNAPPs secure it. Same inventory surface, opposite purpose. |

The most consequential boundaries are the two pillars it contains. The structural tests: *remove a pillar → a single-domain tool remains; remove the unification → a portfolio remains.* Only the multi-domain evaluation on one shared estate inventory, operated as one risk picture, is a CNAPP.

## Representative Products

- Microsoft Defender for Cloud (platform-native heritage; self-describes as a CNAPP combining CSPM, DevSecOps, and CWPP)
- Prisma Cloud (suite-heritage platform; one policy framework, unified inventory, and query language across domains)
- Sysdig Secure (runtime-heritage platform, Falco-based detection; self-describes as a CNAPP delivering threat detection, vulnerability management, posture, and identity entitlement management)
- Wiz (agentless-first pure-play; graph-based cross-domain risk correlation)
- FortiCNAPP, formerly Lacework (agentless-heritage platform within a security-suite portfolio)

These span the platform-native vs third-party poles, agentless-first vs sensor-heritage philosophies, pure-play vs suite packaging, and SaaS vs self-hosted deployment. The core model was checked against pre-label integrated cloud security platforms (provider security centers and multi-domain platforms that predate the current category term) to avoid defining the type by today's packaging wave.

## Sources

Research date: **2026-09-07**

- Microsoft — "Microsoft Defender for Cloud Overview", Microsoft Learn — https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction
- Microsoft — "What is Cloud Security Posture Management (CSPM)", Microsoft Learn — https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management
- Prisma Cloud — documentation index (full documentation map) — https://docs.prismacloud.io/llms.txt
- Sysdig — "Sysdig Secure" documentation overview and table of contents — https://docs.sysdig.com/en/docs/sysdig-secure/
- Wiz — "Cloud & AI Security Platform" product page — https://www.wiz.io/platform
- Fortinet — FortiCNAPP documentation library / Administration Guide index — https://docs.fortinet.com/product/forticnapp , https://docs.fortinet.com/document/forticnapp/latest/administration-guide

> Sourcing limitations: Wiz's operational documentation is behind a login; its structures are evidenced at product-page (positioning) level only, and no operational mechanics are claimed for it. FortiCNAPP's documentation pages rendered as navigation shells; evidence for it is limited to the documented guide set and heritage naming (structure level). Plan names, prices, counts, and other vendor-specific figures are intentionally not stated in this document; they remain, where observed, in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, boundary reasoning, and the historical market-sample check are recorded in the paired Research Notes.
