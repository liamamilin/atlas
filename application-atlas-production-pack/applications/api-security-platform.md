# API Security Platform

## Overview

An **API Security Platform** is a security application whose working world is an organization's API estate. It maintains a living inventory of the APIs the organization actually runs, continuously evaluates those APIs for security risks, detects attacks and abuse in API traffic, and drives the resulting findings through a security workflow toward remediation or enforcement.

The defining core is small:

```text
API-semantic inventory (identified endpoint records)
└── Security findings attached to those APIs
    │   ├── posture findings — risks in definitions, configuration, behavior
    │   └── threat findings — attacks, abuse, anomalies observed in traffic
    └── Security workflow — prioritize → triage → remediate / enforce → verify
```

Everything else commonly associated with the category — sensitive-data mapping, per-endpoint risk scores, shadow-API detection, specification generation, active testing, traffic blocking — is standard capability that mature products add. It makes the platform practical, but it is not what makes the product an API Security Platform. A product that inspects generic HTTP traffic without maintaining an API inventory is a web application firewall; a product that lists APIs without producing security findings is an API catalog. The inventory-plus-findings-plus-workflow structure is the boundary.

## Users & Context

Primary users:

- **Application security engineers** — own the platform's posture view: review the API inventory, assess which endpoints are risky and why, define policies, and drive findings to the teams that own the APIs.
- **Security operations analysts** — work the runtime side: watch attack and abuse events, investigate attacker behavior and sessions, escalate genuine incidents, and tune detection.

Secondary users:

- **API platform teams and developers** — consume findings about the APIs they own: fix specification and validation weaknesses, close authentication gaps, and provide specifications or context back to the platform. In some products developers also help define per-API protection rules.
- **Compliance and governance stakeholders** — consume reports and evidence about sensitive-data exposure and security coverage.

The work context is a production API estate: internal service-to-service APIs, partner-facing endpoints, and public APIs, spread across teams, environments, and clouds — typically far more APIs, and far less documented, than any team believes. The platform is operated from a web console by security staff, while its sensors and integrations live inside the organization's traffic path and delivery pipelines.

## Core Model

### The Defining Core

**API inventory.** The central object is the endpoint record: one identified API operation (host, path, method or operation type) with everything the platform has learned about it — parameters and headers observed in requests and responses, the data types and sensitive data those parameters carry, how the endpoint authenticates its callers, how frequently it is called, which services and environments it belongs to, and who owns it. The inventory is persistent: it survives restarts and redeployments, updates as traffic changes, and serves as the anchor to which all findings attach. Inventories are built from two possible substrates — analysis of live traffic, or the organization's API specifications (such as OpenAPI documents) — and most platforms combine both.

**Security findings.** A finding is a security-relevant statement about one or more inventory records. Findings come in two families:

- *Posture findings* — risks inherent in how an API is defined, configured, or behaving: missing or weak authentication, sensitive data exposed in responses, excessive data exposure, drift between the documented specification and observed behavior, misconfigurations, exposed credentials.
- *Threat findings* — attacks and abuse observed in traffic: exploitation attempts against known API weakness classes, credential stuffing, scraping and bot abuse, business-logic abuse, anomalous behavior from a specific user, session, or source.

**Security workflow.** Findings are managed objects, not just log lines. They carry severity and status, can be assigned, accepted as known risk, dismissed as false positives, or marked for review; they link to the affected endpoints and to remediation paths (a ticket, a code fix, a policy change); and when a "resolved" problem reappears in traffic, the finding reopens. This workflow is what distinguishes a platform from a detector.

### Standard Capabilities

Mature products commonly add the following around the core. Each is widespread, but a product lacking one can still be recognized as an API Security Platform:

- **Sensitive-data detection** — identifying personal, financial, credential, health, or other regulated data flowing through APIs and mapping it to specific endpoints and parameters.
- **Risk scoring** — a per-endpoint or per-API risk score combining exposure, sensitivity, authentication strength, and observed abuse, used to prioritize work.
- **Rogue-API identification** — classifying endpoints that should not exist as they do: *shadow* APIs (live in traffic but unknown to documentation), *zombie* APIs (deprecated but still serving traffic), and *orphan* endpoints (documented but never observed).
- **Authentication evaluation** — detecting how each endpoint authenticates and flagging endpoints that accept unauthenticated or weakly authenticated traffic.
- **Runtime threat detection** — recognizing attack patterns against APIs (including the OWASP API Security Top 10 weakness classes), grouping related requests into attacks and sessions, and scoring attacker behavior.
- **Enforcement** — the ability to act on traffic: blocking, rate limiting, virtual patching, or pushing protective rules into an enforcement point (the platform's own, an API gateway, or an external WAF).
- **Specification generation and conformance** — generating API specification documents from observed traffic, and continuously comparing declared specifications against real behavior to surface drift.
- **Active security testing** — probing APIs with generated attack traffic (conformance scans, fuzzing-style tests) to find vulnerabilities before attackers do; commonly present, though some products deliver only passive detection.
- **Integrations** — forwarding findings into SIEM/SOAR, ticketing, chat, and CI/CD systems, and ingesting context from cloud and identity sources.
- **Multi-role access** — role-based access separating security administrators, analysts, read-only stakeholders, and developers scoped to their own APIs.
- **Dashboards and reports** — aggregated views of attack volume, inventory coverage, sensitive-data exposure, and security-standard coverage.

### One Structure, Many Implementations

The core model is conceptual. Products differ in how they realize each part:

```text
Concept:      Visibility into API traffic
Implementations:  inline inspection point, out-of-band traffic mirror,
                  gateway plugin, language/runtime-level tracing agents,
                  agentless external scanning

Concept:      Inventory substrate
Implementations:  traffic-derived inventory, specification-derived inventory,
                  hybrid (traffic builds it, specs enrich and validate it)

Concept:      Enforcement
Implementations:  platform's own enforcement point, plugin inside an API
                  gateway, rules pushed to an external WAF/CDN,
                  monitor-only (detection without blocking)
```

A reader who has only seen one implementation — say, an out-of-band sensor feeding a cloud console — should still be able to recognize a contract-first platform or a gateway-embedded one from the core model.

## How It Works

The platform runs several loops at once. Together they form its operational rhythm.

### Loop 1 — Connect and discover

```text
Attach a visibility source (inline point, mirror, gateway plugin, tracing agent,
or import specifications)
→ traffic and/or specs flow to the platform
→ the platform reconstructs API structure: hosts, endpoints, operations,
  parameters, authentication
→ unstable or one-off traffic is filtered out as noise
→ endpoints enter the inventory, classified as known, shadow, zombie, or orphan
→ the inventory updates continuously as APIs appear, change, and disappear
```

Discovery is the platform's answer to the fact that no organization reliably knows its own API surface. The inventory is built from what actually runs, not from what was documented.

### Loop 2 — Evaluate posture

```text
For each inventory record, evaluate:
  → what sensitive data it carries
  → how it authenticates
  → whether its specification and its behavior agree
  → whether its definition contains security weaknesses
→ produce posture findings with severity and affected endpoints
→ score each endpoint's risk
→ route findings to owners (security queue, ticketing, CI/CD)
```

### Loop 3 — Detect threats

```text
Analyze each request/response against API semantics and learned behavior
→ recognize attack patterns and abuse (including API-specific weakness classes)
→ group related requests into attacks and attacker sessions
→ score actors and flag anomalies
→ raise threat findings with full request evidence attached
→ optionally trigger enforcement automatically or await analyst decision
```

### Loop 4 — Act and verify

```text
Triage the finding (fix / accept risk / dismiss / escalate)
→ remediation happens outside the platform (code, spec, configuration)
  or inside it (policy change, virtual patch, block rule)
→ the platform keeps watching the affected endpoints
→ if the problem recurs, the finding reopens
```

### The testing loop (common module)

Where the product includes active testing, it runs as a separate, scheduled or on-demand loop: select endpoints, generate probe traffic (from the specification or from recorded traffic), run attack simulations against a target environment, and file the results as findings in the same workflow. Because generated traffic can affect live systems, testing is typically scoped to non-production environments or non-invasive checks in production.

### Monitor-first posture

A defining behavioral pattern across the category: platforms are deployed in detection (monitor) mode first, letting security teams observe real traffic and validate findings before switching any enforcement on. Blocking is a deliberate, policy-scoped step, not the default state.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### API inventory / explorer

The platform's map of the estate.

- lists discovered endpoints and APIs with protocol, environment, risk score, sensitive-data flags, authentication state, and classification (known / shadow / zombie / orphan)
- filterable by sensitivity, authentication, ownership, environment
- primary actions: inspect an endpoint, filter and group, export, assign ownership

### Endpoint detail

The record for one API operation.

- observed parameters and headers with data types, sensitive-data annotations, authentication method, call frequency, recent changes, related findings and attacks
- primary actions: review findings for this endpoint, adjust classification or tags, create a protection rule, hand off to the owning team

### Findings / issues queue

The security work list.

- posture and testing findings with severity, category, affected endpoints, detection context, and status
- primary actions: triage (fix / accept risk / dismiss / mark for review), assign, link to ticketing, view remediation guidance

### Attack / threat timeline

The runtime operations surface.

- detected attacks and abuse events with source, target endpoint, attack class, evidence requests, and actions taken; attacker and session views grouping related activity
- primary actions: investigate evidence, mark false positive, create a rule from the event, escalate, export

### Policy and rules configuration

Where protective behavior is defined.

- detection and enforcement policies (attack detection, rate limiting, bot handling, data-access rules), scoped per environment or endpoint, with monitor/block actions
- primary actions: create or edit rules, set enforcement mode, define exclusions for trusted traffic

### Dashboards and reports

Aggregated views for security leadership and governance: attack volume and distribution, inventory coverage and growth, sensitive-data exposure, coverage against security standards such as the OWASP API Security Top 10, and exportable reports.

### Administration

User and role management (security admin, analyst, developer, read-only roles), integration configuration (SIEM, ticketing, CI/CD, chat), and sensor/deployment management.

## Important Rules / Behaviors

- **Findings attach to endpoints.** Every finding, attack, and risk score is anchored to inventory records. An attack without an endpoint context, or a risk score without an API, does not occur in this Type.
- **Resolved findings can reopen.** Platforms commonly keep observing endpoints after a finding is closed; where this continuous verification exists, a weakness or abuse pattern that reappears causes the finding to return, so status reflects production reality rather than optimism.
- **Discovery filters noise.** Traffic-based inventory building commonly excludes unstable signals — endpoints seen only briefly, one-off parameter spikes, scanner traffic, health-check noise — so the inventory represents the real, stable API surface rather than every request ever seen.
- **Enforcement is deliberate and scoped.** Blocking, rate limiting, and virtual patching apply through explicit policies, per environment or endpoint, and can be reverted. Monitor mode remains a fully supported operating posture.
- **Specification–behavior drift is a first-class signal.** A mismatch between what an API declares and what it does — undocumented endpoints, undocumented parameters, retired versions still serving traffic — is itself a security finding, not merely a documentation problem.
- **Traffic is sensitive by nature.** API traffic carries personal and regulated data, so platforms commonly minimize what they store or forward: analyzing locally where possible, aggregating or hashing values, and letting organizations exclude sensitive traffic from collection.
- **Testing is scoped for safety.** Active testing generates real attack traffic; mature products constrain it to owned, typically non-production targets, or restrict production testing to non-invasive checks.
- **False positives are a managed state.** Analysts can mark detections as false positives, and the platform uses that feedback to tune future behavior — detection quality is treated as an ongoing operational concern, not a fixed property.

## Variants

The Type is implemented in several recognizable shapes. These differ in philosophy and deployment, not in core structure:

- **Contract-first platforms** — the API specification is the security substrate: definitions are audited for security quality, implementations are scanned for conformance to the contract, and protection enforces the contract as a strict allowlist. Strong developer participation ("security as code"). (e.g. 42Crunch)
- **Traffic-first detection platforms** — sensors observe production traffic out-of-band or inline; the inventory and all findings derive from observed behavior; enforcement is policy-driven. (e.g. Salt Security, Akamai API Security lineage)
- **Inline protection platforms** — descended from web application protection; detection and blocking happen in the traffic path, with API discovery and posture layered on top. Often packaged with broader web protection (WAAP). (e.g. Wallarm)
- **Tracing-based platforms** — deep, tracing-grade capture (including runtime agents) feeds unusually rich behavioral analysis, session stitching, and service-topology views. (e.g. Traceable)
- **Suite-embedded API security** — API security sold as a module of a broader security suite (CDN/edge vendor, cloud platform, or WAAP vendor), sharing its enforcement fabric.
- **External-surface-led variants** — discovery starts agentlessly from outside the organization (internet-facing API discovery) and pulls the internal platform along.
- **AI-workload extensions** — an emerging overlay extending the same inventory-findings-workflow structure to AI agents, MCP servers, and model endpoints as additional protected entities.

A variant remains a variant unless it abandons the core: a product with no inventory and no findings is not an API Security Platform regardless of its marketing.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Web Application Firewall / WAF | closest neighbor | inspects generic HTTP for generic attack patterns; no persistent API-semantic inventory, no per-endpoint posture model. Removing the inventory from an API Security Platform collapses it into a WAF. Many API platforms embed WAF-like policies as one module, and integrate with external WAFs for enforcement. |
| API Gateway Management Console | adjacent, complementary | traffic management and policy enforcement (routing, authentication, quotas) owned by API teams; no security evaluation or threat detection. The two integrate: gateway traffic feeds discovery, and platforms push protection into gateways. |
| DAST / IAST | overlapping module | tests applications generally; API security testing is contract-aware and is one module of the platform. Removing the runtime inventory and traffic observation, keeping only testing, yields an API testing tool. |
| Application Security Platform (SAST/SCA) | sibling | centers on source code and dependencies in the SDLC; the API Security Platform centers on the running API estate and its traffic. |
| Vulnerability Management | consumer / aggregate | aggregates vulnerabilities across all asset classes and drives remediation programs; the API Security Platform's scope is APIs specifically, with traffic-derived evidence it can feed upward. |
| Attack Surface Management | overlapping module | discovers external exposure broadly (domains, hosts, certificates); some API platforms include an external-API-surface module, but the core remains API-semantic. |
| API Documentation Platform | superficial overlap | both may produce API specifications; documentation serves API consumers, the security platform serves risk and threat workflows. |
| API Development Workbench | different phase | design and testing of APIs during development; the security platform's object is the deployed, production API estate. |

The WAF boundary is the most important one, because the two overlap on HTTP inspection and blocking. The structural difference is whether the system understands *which API* each request belongs to — maintaining endpoint records, per-endpoint behavior, and API-specific weakness classes — or treats traffic as anonymous HTTP.

## Representative Products

- 42Crunch — contract-first platform (audit / scan / protect around OpenAPI definitions)
- Wallarm — inline and out-of-band API security within a broader web protection platform
- Traceable — tracing-based deep observability platform spanning discovery, protection, and testing
- Salt Security — out-of-band, behavior-focused API and agentic-AI security

The core model was checked across these four philosophies (contract-first, inline, tracing-based, out-of-band behavioral) to avoid over-fitting the definition to any one visibility or enforcement mechanism.

## Sources

Research date: **2026-09-06**

- 42Crunch — API Security Platform documentation (API Security Audit, API Scan, API Protection): https://docs.42crunch.com/latest/content/home.htm
- Wallarm — documentation (platform overview, API Discovery, Threat Management): https://docs.wallarm.com/
- Traceable — documentation (Product Overview, Discovery, Protection, AST): https://docs.traceable.ai/docs/product-ovw
- Salt Security — official product pages (platform, discovery, posture, protection use cases): https://salt.security/

> Sourcing limitation: the dedicated documentation sites for Salt Security (docs.salt.security) and Akamai API Security (techdocs.akamai.com) could not be retrieved from the research environment on 2026-09-06. Salt observations rest on official product pages only and were used to confirm cross-product commonality, not for precise operational claims; Akamai API Security was treated as market context and not used as evidence. Precise vendor-specific parameters (scoring formulas, thresholds, sampling rates, limits) are intentionally not stated in this document; they are recorded, where observed, in the paired Research Notes.

Detailed product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
