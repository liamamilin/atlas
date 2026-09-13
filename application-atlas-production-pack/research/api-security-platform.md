# Research Notes — API Security Platform

Research date: 2026-09-06
Leaf: API Security Platform (DIRECTORY.md §15 Cybersecurity, Identity & Trust)
Slug: api-security-platform

---

## Research Goal

Understand what an API Security Platform actually is as an Application Type: what objects exist inside it, how it observes APIs, what security work it performs, who operates it, and where its boundary lies against WAF, API Gateway consoles, application security testing, and adjacent security Types.

## Initial Boundary (hypothesis before research)

- Core purpose: secure an organization's APIs — discover them, evaluate their security posture, detect API-specific attacks and abuse in traffic, and drive remediation/enforcement.
- Likely users: application security (AppSec) engineers, security operations (SOC) analysts, API platform teams, developers.
- Nearest neighbors: Web Application Firewall (WAF), API Gateway Management Console, DAST/IAST, Application Security Platform (SAST/SCA), Vulnerability Management, Attack Surface Management, API Documentation Platform.
- Expected boundary: API-semantic understanding (inventory of endpoints, per-endpoint behavior) vs generic HTTP inspection (WAF); risk/threat evaluation vs traffic management (gateway).
- Unknowns: whether an inventory is universal or product-specific; how enforcement is realized; how testing fits; how findings lifecycle works.

## Research Questions

1. What is the central managed object — API inventory record, attack event, specification, or finding?
2. How does the platform acquire visibility into API traffic (inline, out-of-band, gateway plugin, eBPF/tracing, spec import)?
3. What does "discovery" concretely produce (shadow/zombie/orphan APIs, parameters, sensitive data)?
4. What does "posture" mean (risk scoring, authentication detection, spec quality, drift)?
5. What does runtime threat detection mean (attack classes, attacker/session analysis, scoring)?
6. What does testing mean (conformance scans, DAST-style, passive detection)?
7. How is enforcement realized (own enforcement point, gateway plugin, external WAF integration, monitor-only)?
8. Who uses the platform and through which interfaces?
9. What lifecycle do findings/attacks follow?
10. Which rules matter (sensitive data handling, monitor-vs-block posture, noise filtering, privacy)?

## Representative Products

Selected for market representation, documentation quality, differing product philosophy, and differing customer positioning:

| Product | Philosophy | Evidence tier |
|---|---|---|
| 42Crunch | Contract-first: the OpenAPI/GraphQL definition is the security substrate; audit → scan → protect | A (official docs, deep) |
| Wallarm | Inline/out-of-band detection platform (WAAP + API security); traffic-first discovery | A (official docs, deep) |
| Traceable | Deep observability: tracing-grade traffic capture drives discovery, protection, testing | A (official docs, deep) |
| Salt Security | Out-of-band, behavioral/ML detection; agentic-AI extension | B (official product pages only; docs site unreachable) |

Akamai API Security (ex-Noname) was sampled as a market anchor but its techdocs were not reachable from the research environment (JS-rendered; `.md` fallback also failed). Not used as evidence.

## Sources

- 42Crunch Platform documentation — https://docs.42crunch.com/latest/content/home.htm ; concepts: API Security Audit (api_contract_security_audit.htm), API Scan (api_contract_conformance_scan.htm), API Protection (api_protection.htm). Fetched 2026-09-06.
- Wallarm documentation — https://docs.wallarm.com/ ; pages: about-wallarm/overview.md, api-discovery/overview.md, user-guides/events/overview.md. Fetched 2026-09-06.
- Traceable documentation — https://docs.traceable.ai/ ; pages: docs/product-ovw (Product Overview), docs index. Fetched 2026-09-06.
- Salt Security — https://salt.security/ (product pages: /platform, /surface, /connect, /collect, /protect, use-case pages). Fetched 2026-09-06. Docs site https://docs.salt.security/ returned a transport error; product-page evidence only.
- Akamai API Security — https://techdocs.akamai.com/api-security/docs/welcome-to-api-security (and `.md` variant) — not reachable (JS-rendered shell). No evidence used.

---

## Product A — 42Crunch (evidence layer A)

### Key observations

**Platform framing.** "42Crunch API Security Platform" with three pillars: API Security Audit (definition), API Scan (conformance), API Protection (API Firewall). Explicit philosophy: "The starting point for the API security is the API definition itself."

**API Security Audit (static, spec-centric).**
- Import an OpenAPI (v2/v3.0/v3.1) or GraphQL definition; audit runs static analysis with 200+ checks on structure, semantics, security definitions, and input/output data definition.
- Produces an audit score per API (100-point pool: security analysis max 30, data validation max 70); issues carry severity and stable fingerprints for tracking fixes across audits.
- Audit report lists issues, occurrences, score impact; issues link to a Security Editor for fixing and re-audit.
- Security quality gates (SQGs): organizational gates an API must pass; audit report shows why an API failed SQGs.
- Customizations via `x-42c` vendor extensions or platform audit rules (sensitivity per operation, mTLS declaration, skipping known-safe issues).
- CI/CD integration so API changes are audited automatically; audit score trends chart per API.

**API Scan (dynamic, contract conformance).**
- Dynamic runtime analysis against the live API endpoint: generates real traffic; happy-path baseline first, then conformance tests (schema/parameter/header injection, authn/authz tests, HTTP method tests); Scan v2 adds drift scan, unhappy-path and custom test scenarios.
- Scan configuration per API (endpoint, authentication, tests); scan token for on-premises Docker scan agents; scan report with expected vs received HTTP status codes; scan logs.
- Explicit safety rule: invasive scans only against owned, non-production systems; only non-invasive drift scans in production.
- Scan results feed SQG approval; reference scan configuration represents the API's quality in lists/trends.

**API Protection (enforcement).**
- API Firewall: "an API-native micro firewall tailor-made for your API", deployed in front of APIs (positive security model).
- Builds an allowlist of valid operations and input data from the API contract; blocks non-conforming requests/responses: undocumented methods, undocumented error codes, undocumented schemas, undocumented query/path parameters, schema-violating data.
- Requires audit score ≥ 70 for "reliable" protection (allowlist quality depends on definition quality).
- Security-as-code: protection applied via `x-42c` extensions inside the API definition; developers participate in defining security; security team defines protection strategies.
- Explicit WAF contrast: perimeter WAF "no longer enough"; micro-firewall "can distinguish hacking API calls from legitimate API traffic, unlike a traditional WAF-based solution".

**Interfaces observed.** API collections list, API summary (audit + scan tiles, trends), audit report, scan reports, Security Editor, SQG configuration, tags, CI/CD integration pages, API monitoring.

## Product B — Wallarm (evidence layer A)

### Key observations

**Platform framing.** "Wallarm AI Control Platform" with a four-stage loop: Discover → Observe → Enforce → Govern. API Security is one product inside it (alongside AI Hypervisor, Infrastructure Discovery, API Security Testing).

**Discover (inventory).**
- API Discovery "continuously analyzes the real traffic requests and builds the API inventory (full picture of your active APIs and MCP servers)".
- Inventory includes: hosts and endpoints; required/optional parameters and headers with type/format and last-updated timestamps; HTTP methods; GraphQL operations and schema; SOAP/gRPC operations; MCP servers with tools/resources/prompts.
- Multi-protocol: REST, GraphQL, SOAP, gRPC, MCP.
- Rogue endpoints: shadow and zombie APIs identified.
- Sensitive data detection: PII, login credentials, financial data, medical data, technical data (IP/MAC).
- Authentication flow detection per endpoint from headers/parameters; filter endpoints lacking authentication ("the #1 API security risk").
- Per-endpoint risk score ("understand which endpoints are most likely to be an attack target").
- Sensitive business flows: auto-tagging of endpoints belonging to critical business functions (authentication, account management, billing), manually adjustable.
- Noise detection: endpoint stability (minimum request count + traffic outside a short timeframe) and parameter stability (>1% occurrence) before an endpoint enters the inventory; only 2xx responses processed; scanner traffic excluded.
- Hybrid local/cloud analysis, privacy-first: parameter values hashed (SHA-256) or kept local; only endpoint/parameter names and statistics uploaded.

**Observe (threat detection).**
- Analyzes every request/response for OWASP Top 10 and OWASP API Top 10 attacks, API-specific bot abuse, credential stuffing, behavioral anomalies.

**Enforce.**
- Detection inline and out-of-band; rate limiting (L7 DoS); custom regex rules; geolocation controls; virtual patches; filtration mode controls (monitor/block posture).
- Deployment: managed Security Edge, self-hosted (Kubernetes/cloud), connectors, API gateways, CDN.

**Govern / operations.**
- Threat Management: Dashboards (Threat Prevention, API Discovery, OWASP API Top 10 2023 coverage; custom BI dashboards); Attacks section (filter by type/source/endpoint/status, grouping into attacks, save views, create rules from attacks, mark false positives, CSV export, up to 6 months history); Incidents (attacks targeting a confirmed vulnerability, linked vulnerability data); Sessions (request sequences for context; detection configurable); PDF/CSV reports.
- Security Issues section consolidates all found vulnerabilities regardless of detection method (passive detection, AASM).
- Integrations: SIEM (Splunk, Sentinel, Sumo), SOAR, ticketing, chat (Slack), PagerDuty, webhooks, S3, Fluentd.
- Wallarm Console: events, triggers & alerts, search & reports, users & access.

## Product C — Traceable (evidence layer A)

### Key observations

**Platform framing.** "API and application security platform"; three modules: Discovery, Protection, Testing (AST), plus platform administration.

**Discovery.**
- "Continuously observing API traffic across your environment, Traceable automatically discovers and analyzes every API as it is actually used in production." Identifies internal and external APIs, shadow APIs, zombie APIs ("replaced by newer versions but not removed"), orphan endpoints (documented but never observed in traffic).
- All API types: REST, SOAP, gRPC, GraphQL, WebSocket.
- Inventory captures endpoints, specifications, ownership, runtime behavior; per-endpoint: methods in use, call frequency, authentication applied, connections to services/domains/environments.
- Sensitive data: personal/financial/regulated data identified from live requests/responses and mapped to specific parameters.
- Risk evaluation: unauthenticated or overly exposed endpoints highlighted; abnormal behavior and attack attempts detected; activity mapped to common API threat patterns; risk levels update automatically as traffic changes.
- Spec generation: OpenAPI and GraphQL specifications generated from live traffic; existing specs can be uploaded and validated against production behavior.
- Conformance analysis: continuous comparison of specs vs live traffic → API drift, shadow endpoints (in traffic, not documented), orphan endpoints, parameter/header/payload mismatches; on-demand or scheduled.
- Identity stitching: API calls linked to users/sessions from headers/tokens/cookies; requests stitched into sessions.
- All Assets page: APIs, MCP tools and servers, services, with risk score, data types, usage, last activity.
- Application Flow topology map: traffic through services/APIs, dependencies, per-component risk.

**Issues workflow (lifecycle).**
- "Every issue in Traceable follows a structured lifecycle": discovered via traffic/integrations/test scans → evaluated against policies/plugins → enriched with severity, category, affected endpoints → response paths: fix, mark for review, accept known risk, dismiss → consolidated on Issues page with trends/grouping/filtering → after remediation, continuous monitoring; if an issue reoccurs it is automatically reopened.

**Protection.**
- Built-in policies (rate limiting, bot protection, IP rules, attack detection) with immediate visibility "without requiring any upfront configuration"; "begin in monitoring mode to observe threats and traffic patterns, and move to enforcement as you gain confidence".
- Custom policies: rules on traffic sources, request patterns, sensitive data access, request frequency; actions allow/block/monitor.
- Policy families: WAF policies, API protection policies, AI application protection, bot protection, exclusion policies.
- Threat Actors page: suspicious users/IPs, activity patterns, evidence, status updates (monitor/allow/block).
- Threat Activity page: real-time security events, sources, severity, affected endpoints, timelines, tickets.
- Threat scoring: dynamic per-user risk scores from anomalies/events; users progress from monitored to threat actors; low/medium/high/critical categories with adjustable thresholds; auto-blocking with exclusions/allowlists.

**Testing (AST).**
- Scans define which endpoints, traffic type, and security rules: XAST Live (live traffic), XAST Replay (historical traffic), DAST (specification-based black-box: OpenAPI, Postman, GraphQL).
- On-demand or scheduled (daily/weekly/monthly); policies/attack sets; runners, timeouts, request delays; logs, API coverage metrics, detected issues.

**Administration & integrations.**
- RBAC roles: Account Owner, Security Admin, Security Analyst, Global Reader, Developer (module/scope-level access).
- Integrations: CI/CD (GitHub Actions, GitLab, Jenkins, Azure DevOps, Harness), SIEM/SOAR (Splunk, HEC, Syslog), WAF integrations (AWS WAF, Akamai, Imperva, Fortinet, F5, Azure, Cloudflare, Google Cloud Armor), cloud (Wiz), ticketing (Jira, ServiceNow ITSM/CMDB).
- AI features: natural-language chatbot over platform data; AI-explained issues with remediation suggestions.
- Dashboards: Home, AI Security, custom dashboards with widgets.

## Product D — Salt Security (evidence layer B — product pages only)

### Key observations

- Positioning: "Agentic Security Platform" spanning API security + MCP/AI-agent security; API security is the foundation ("You can't have AI security without API security").
- Discovery: "automatically discovers every agent, MCP server and API across your environment, including the shadow and zombie APIs nobody knows are there"; unified inventory use case ("Create a Unified Inventory — Full API landscape view").
- Posture: "analyzes every component ... for misconfigurations, excessive permissions, and exposed credentials"; exposed internal APIs; authentication and authorization weaknesses; hardcoded tokens.
- Runtime protection: "real-time detection of abuse, anomalous behavior, and active attacks ... including the internal traffic your perimeter tools never see"; "Stop Behavioral API Attacks — Block business abuse"; Salt Protect ("Block logic-based threats"); Salt Collect ("Analyze live traffic data").
- External exposure: Salt Surface ("Map external exposure"); Salt Connect ("See APIs in your cloud").
- Behavioral/ML approach: crowd-sourced attack learning is the vendor's known marketing claim (not verified in docs; not used).
- Integrations: CrowdStrike, AWS, GitHub, Azure/Sentinel, Kong, GCP.
- Industry solutions: finance, transportation, healthcare, retail, software — enterprise skew.

**Limitation:** docs.salt.security unreachable; observations are from marketing/product pages (Tier 2). Per evidence rules, Salt observations are used only for cross-product commonality confirmation of discovery/posture/protection, not for precise operational claims.

---

## Cross-product Comparison

| Dimension | 42Crunch | Wallarm | Traceable | Salt |
|---|---|---|---|---|
| Central object | API definition (OpenAPI/GraphQL) as managed record + audit/scan/protection state | API inventory (hosts/endpoints/params) built from traffic | API endpoint inventory + assets (services, MCP) from traffic | API inventory from traffic (agent-collected) |
| Visibility acquisition | Spec import (design-time); protection via gateway/firewall deployment | Inline node or out-of-band; managed edge, self-hosted, connector, gateway, CDN | Platform agent, eBPF, traffic mirroring, integrations | Out-of-band collectors/agents |
| Discovery output | Audited spec records; (runtime discovery not evidenced in fetched pages) | Inventory: endpoints, params, methods, schemas; rogue (shadow/zombie) APIs; noise filtering | Inventory: endpoints, specs, ownership, behavior; shadow/zombie/orphan | Inventory incl. shadow/zombie APIs |
| Posture evaluation | Audit score per spec; SQGs; sensitivity levels | Per-endpoint risk score; auth-flow detection; sensitive data; sensitive business flows | Risk score; unauthenticated/over-exposed flags; conformance/drift analysis | Misconfigurations, auth weaknesses, exposed credentials |
| Sensitive data | Data-definition quality in spec (indirect) | PII/credentials/financial/medical/technical detection per endpoint | Sensitive data mapped to parameters | Sensitive-data tracking (use case listed) |
| Runtime threat detection | Not the primary pillar (protection is allowlist enforcement) | OWASP API Top 10, bots, credential stuffing, anomalies; attacks/incidents/sessions | Threat activity, threat actors, threat scoring, anomaly detection | Behavioral attacks, anomalies (ML) |
| Active testing | API Scan: conformance + drift scans, happy-path baseline | Passive detection + external AASM (active testing not evidenced in fetched pages) | AST: XAST Live / XAST Replay / DAST scans | Not evidenced |
| Enforcement | API Firewall allowlist (positive security model) | Inline block, rate limiting, virtual patch, filtration modes | Policies allow/block/monitor; auto-block; external WAF push | Salt Protect (block logic-based threats) |
| Findings lifecycle | Issue fingerprints tracked across audits; SQG gates | Attacks/incidents/vulnerabilities with rules, false-positive marking | Explicit issue lifecycle: detect → enrich → fix/review/accept/dismiss → auto-reopen on recurrence | Not evidenced |
| Spec generation/validation | Spec is the input substrate | Builds API specs from traffic | Generates OpenAPI/GraphQL specs from traffic; validates uploaded specs | Not evidenced |
| Interfaces | Collections, audit/scan reports, Security Editor, SQG | Console: dashboards, attacks, incidents, sessions, inventory, rules/triggers | Inventory, endpoint details, issues, threat actors/activity, AST scans, dashboards, topology | Console not publicly documented |
| Users | Developers + AppSec (security-as-code framing) | SOC/AppSec teams | RBAC: security admin/analyst, developer, global reader | AppSec/SOC (enterprise) |
| Integrations | CI/CD, IDE plugins | SIEM/SOAR/ticketing/chat/webhooks | CI/CD, SIEM/SOAR, WAFs, ticketing, cloud posture | Endpoint/cloud/SCM/gateway vendors |
| Adjacent extension | APIsecurity.io content hub | AI Hypervisor, Infrastructure Discovery, AASM | AI application protection, MCP assets, AI chatbot | Agentic Security Graph, MCP/AI-agent security |

### Stable commonalities (evidence layer B)

1. **API-semantic inventory.** All four maintain identified records of the organization's APIs (hosts/endpoints/operations) — from traffic (Wallarm, Traceable, Salt) and/or from specifications (42Crunch). Findings attach to these records.
2. **Security findings as managed objects.** All four produce security-relevant findings about APIs — posture risks (weak auth, sensitive data, misconfiguration, spec quality) and/or observed threats (attacks, abuse, anomalies) — and manage them through a triage/remediation workflow.
3. **Rogue-API identification.** Shadow/zombie (and orphan, in Traceable) APIs are named, first-class discovery outcomes in all four.
4. **Sensitive-data awareness.** All four connect APIs to the sensitive data they carry (directly evidenced in Wallarm, Traceable; posture framing in Salt; data-definition quality in 42Crunch).
5. **Risk scoring/prioritization.** Per-endpoint or per-API risk scores (Wallarm, Traceable explicit; 42Crunch audit score; Salt posture risk framing).
6. **Authentication evaluation.** Detecting how endpoints authenticate and flagging unauthenticated/weakly authenticated endpoints (Wallarm, Traceable explicit; Salt posture; 42Crunch security-definitions audit).
7. **Enforcement path.** All four can act on traffic or definitions (42Crunch firewall, Wallarm inline/vpatch, Traceable policies/auto-block, Salt Protect). Monitor-only operation is a supported posture (Wallarm filtration modes; Traceable monitor mode).
8. **Integration into security/dev workflows.** SIEM/SOAR/ticketing/CI-CD/chat integrations in all evidenced products.
9. **Multi-role operation.** Security teams plus developers/API teams (42Crunch security-as-code; Traceable RBAC with Developer role; Wallarm grants developers inventory access).

### Product-specific differences (candidates for L2/L3)

- 42Crunch: contract-first substrate; positive-security allowlist firewall; audit score arithmetic; SQGs; x-42c extensions; scan safety rules (non-prod for invasive scans).
- Wallarm: four-stage Discover/Observe/Enforce/Govern loop; noise-detection thresholds; SHA-256 parameter-value hashing; sensitive business flows; MCP discovery; OWASP API Top 10 coverage dashboard.
- Traceable: tracing-grade capture (eBPF); XAST Live/Replay/DAST traffic types; threat-actor scoring with auto-block; application-flow topology; AI chatbot; explicit issue auto-reopen.
- Salt: agentic security graph; module naming (Surface/Connect/Code/Collect/Protect); ML behavioral detection emphasis.

---

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Minimal structure without which the Type is not recognizable:

1. **API-semantic inventory** — the platform maintains persistent, identified records of the organization's APIs (endpoints/operations), understood at the API level (paths, methods, parameters, authentication), not as anonymous HTTP traffic.
2. **Security findings about APIs** — the platform produces security findings attached to that inventory, derived from (a) analysis of API traffic (attacks, abuse, anomalies, sensitive-data exposure) and/or (b) evaluation of API definitions/behavior (spec quality, misconfiguration, drift).
3. **Security workflow on findings** — findings are managed objects: prioritized, triaged, and driven toward remediation or protective action.

Justification: remove the API-semantic layer → generic web protection (WAF). Remove findings → API catalog/gateway analytics. Remove the workflow → a report generator, not a platform. All four sampled products exhibit all three.

Historical/market check: the definition holds for contract-first products (42Crunch), traffic-first out-of-band products (Salt, Noname-lineage), inline WAAP-derived products (Wallarm, Imperva lineage), and tracing-based products (Traceable). It does not depend on any one visibility mechanism, protocol set, or enforcement locus.

### L1 — Common Mature Structure

Present in most mature products; not required for the definition:

- Sensitive-data detection/classification mapped to endpoints and parameters
- Per-endpoint/API risk scoring and prioritization
- Rogue-API identification (shadow / zombie / orphan)
- Authentication detection and unauthenticated-endpoint flagging
- Runtime threat detection (attack events, OWASP API Top 10 mapping, behavioral anomalies, attacker/session analysis)
- Enforcement capability (block / rate-limit / virtual patch) via an inline point or integrations
- Specification generation from traffic and/or spec-vs-behavior conformance analysis
- Active security testing of APIs (conformance/DAST-style scans) — common but delivered unevenly (some products passive-only)
- Findings lifecycle management (severity, status, assignment, reopen on recurrence)
- Integrations: SIEM/SOAR, ticketing, CI/CD, chat/webhooks
- Multi-role access (security admin/analyst, developer/reader roles)
- Dashboards and reports

### L2 — Variant / Optional Structure

- Visibility acquisition mode: inline proxy vs out-of-band mirroring vs gateway plugin vs eBPF/tracing vs agentless external scanning
- Philosophy: contract-first (spec as substrate) vs traffic-first (behavior as substrate)
- Enforcement locus: own enforcement point vs gateway plugin vs external WAF/gateway integration vs monitor-only
- Protocol breadth: REST/GraphQL/gRPC/SOAP/WebSocket/MCP coverage varies
- Deployment: SaaS-only vs hybrid with self-hosted components; data-privacy posture (local analysis, value hashing, sampling)
- External attack surface management (agentless discovery of exposed APIs)
- AI-workload security extension (MCP servers, AI agents, AI application protection)
- AI assistance (chatbots, AI-explained findings)
- Service topology / application-flow mapping

### L3 — Vendor-specific (Research Notes only)

- 42Crunch: 100-point audit score split (30 security / 70 data validation); ≥70 score threshold before protection; 200+ audit checks; issue fingerprints; 30-occurrence report limit; SQGs; x-42c extensions; API Firewall allowlist semantics; scan tokens; invasive-scan-only-on-non-prod rule; 4096-char scan string limit; 8 KB response truncation; 3600 s scan timeout.
- Wallarm: noise-detection criteria (endpoint stability, >1% parameter occurrence, 2xx-only, method/host/path validation); ~10% response sampling for REST-family discovery (100% for MCP); SHA-256 parameter-value hashing; sensitive business flow tags; filtration mode names; trigger mechanism; 6-month attack history window; OWASP API Top 10 2023 dashboard.
- Traceable: XAST Live/Replay/DAST naming; threat-actor risk categories with adjustable thresholds; RBAC role names (Account Owner, Security Admin, Security Analyst, Global Reader, Developer); named WAF integration list; AI chatbot; Application Flow topology; issue auto-reopen behavior.
- Salt: Agentic Security Graph; module names (Salt Surface / Connect / Code / Collect / Protect); Pepper AI; crowd-sourced attack learning claim (unverified).

---

## Vendor-specific Findings

See L3 above. None of these enter the canonical document except as neutral, vendor-attributed examples where useful.

## Boundary Findings

| Neighbor Type | Relationship | Distinction | "Remove what → becomes the other" |
|---|---|---|---|
| Web Application Firewall (WAF) | closest neighbor | WAF inspects generic HTTP for generic attack patterns without maintaining an API-semantic inventory; API Security Platform's defining layer is the inventory + per-endpoint understanding. Several platforms embed WAF-like policy families as one module (Wallarm WAAP, Traceable WAF policies), and 42Crunch explicitly contrasts its API firewall with WAF. | Remove the API-semantic inventory/understanding → WAF / generic web protection |
| API Gateway Management Console | adjacent, complementary | Gateway = traffic management + policy enforcement point (routing, authN, quotas), owned by API/platform teams; security platform = risk evaluation + threat detection. They integrate (protection deployed via gateways; gateway traffic feeds discovery). | Remove security findings/evaluation → gateway console/analytics |
| DAST / IAST | overlapping module | DAST/IAST test applications generally; API security testing is contract-aware and is one module of the platform, not the whole. | Remove runtime inventory + traffic observation, keep testing → API security testing tool (DAST variant) |
| Application Security Platform (SAST/SCA) | sibling | Those center on code/artifacts in the SDLC; API security centers on the running API estate and its traffic. | Center the object on code rather than the API estate → AppSec platform |
| Vulnerability Management | consumer/aggregate | VM aggregates vulnerabilities across all asset classes; API security platform's scope is APIs specifically, with traffic-derived evidence. | Generalize findings across all asset classes → vulnerability management |
| Attack Surface Management | overlapping module | ASM discovers external exposure broadly (domains, hosts, certs); some API platforms include an external-API-surface module (Wallarm AASM, Salt Surface) but the core remains API-semantic. | Drop API semantics, discover all external assets → ASM |
| API Documentation Platform | superficial overlap | Spec generation overlaps, but documentation serves API consumers; the security platform serves risk/threat workflows. | Drop findings/security workflow → API catalog/documentation |

## Uncertainties

1. Salt Security operational details (console structure, detection mechanics, enforcement depth) unverified — docs unreachable; only product-page claims.
2. Akamai API Security (ex-Noname) not verified; treated as market context only.
3. Whether every product of the Type ships active testing — evidenced in 42Crunch and Traceable; Wallarm evidenced with passive detection + external surface module; treated as Common-with-variation, not Core.
4. Whether spec generation from traffic is universal — evidenced in Wallarm and Traceable; 42Crunch treats specs as input rather than output; treated as Common, not Core.
5. Exact enforcement depth per product (e.g., granularity of blocking) not uniformly documented; final document uses calibrated wording ("can enforce", "monitor-first posture") rather than precise mechanics.
6. Market boundary drift toward AI/agent security (MCP, agentic AI) is recent and fast-moving; treated as an emerging extension, not part of the Type definition.

## Final Synthesis

An API Security Platform is defined by a small core: a persistent, API-semantic inventory of the organization's APIs; security findings about those APIs derived from traffic analysis and/or definition/behavior evaluation; and a security workflow that prioritizes and acts on those findings. Around that core, mature products add sensitive-data mapping, risk scoring, rogue-API identification, authentication evaluation, runtime threat detection, enforcement, testing, spec generation/conformance, integrations, and multi-role operation. Products differ most in how they acquire visibility (inline, out-of-band, gateway, tracing, spec import) and where enforcement happens (own firewall, gateway, external WAF, monitor-only) — implementation dimensions, not defining ones. The Type sits between the WAF (generic HTTP protection without API semantics) and the API Gateway (traffic management without security evaluation); removing the API-semantic inventory collapses it into a WAF, removing the findings collapses it into an API catalog.
