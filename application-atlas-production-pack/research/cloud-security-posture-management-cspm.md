# Research Notes — Cloud Security Posture Management / CSPM

## Research Goal

Understand what a Cloud Security Posture Management (CSPM) application actually is as a software type: its core objects, its defining workflow loop, its user surfaces, its lifecycle and behavioral rules, and its boundary against neighboring security/cloud types (CNAPP, CWPP, SSPM, DSPM, Vulnerability Management, Attack Surface Management, Cloud Management Platform, Security Compliance Platform, SIEM, IaC platforms).

## Initial Boundary

Working hypothesis before research:

- CSPM = continuous assessment of the *configuration* of resources inside connected cloud accounts (IaaS/PaaS) against security policies and best-practice benchmarks, producing tracked misconfiguration findings.
- Core loop guess: connect cloud account → inventory resources → evaluate configuration against policies → findings → remediate → re-evaluate.
- Likely confusions: CNAPP (the umbrella platform that contains CSPM as a module), CWPP (workload/runtime), SSPM (SaaS settings), DSPM (data objects), Vulnerability Management (CVEs), ASM (outside-in), CMP (provisioning/operations).

## Research Questions

1. What is the central object — "resource"? "control"? "finding"? "policy"? How do they relate?
2. How does the product get visibility into cloud configuration (connectors, read-only roles, config recorders, agents, agentless scanning)?
3. What exactly is evaluated (what is a "misconfiguration") and against what (benchmarks, standards, custom rules)?
4. What is the lifecycle of a finding — creation, severity, ownership, acceptance/suppression, resolution?
5. How do compliance frameworks (CIS, PCI DSS, NIST, ISO, SOC 2…) appear as product structure?
6. What surfaces exist (dashboards, findings lists, inventory explorers, policy editors, compliance reports)?
7. What integrations carry findings outward (ITSM, chat, SIEM, event buses)?
8. What is shift-left (IaC scanning) and is it definitional or an extension?
9. What distinguishes the platform-native pole (AWS Config / Security Hub / Defender / SCC) from third-party multi-cloud CSPM?
10. Where is the CNAPP boundary — what makes CSPM the posture core of a broader platform?

## Representative Products

Selection rationale: platform-native vs third-party poles, bundled vs standalone posture, agent-based vs agentless heritage, enterprise vs broad-market positioning. Fetch status noted per product.

| Product | Pole | Evidence depth |
|---|---|---|
| AWS Config + AWS Security Hub (CSPM) | platform-native (AWS) | Tier-1 full article bodies fetched |
| Microsoft Defender for Cloud (Foundational CSPM / Defender CSPM plan) | cloud-native CNAPP, hybrid + multicloud, free-tier vs paid-plan posture | Tier-1 full article body fetched |
| Sysdig Secure (Posture + Compliance modules) | third-party CNAPP with explicit CSPM module | Tier-1: nav structure + full page bodies (Posture Overview, Posture Findings) |
| Prisma Cloud (Palo Alto Networks — Governance pillar) | third-party CNAPP, policy/alert-led CSPM heritage | Tier-1 documentation *structure* (full sitemap) — page bodies not fetched |
| FortiCNAPP (formerly Lacework) | third-party CNAPP, agent-heritage, query-language policy engine | Documentation index only (guide list) |

Unreachable (abandoned after 1–2 failures each, per network rule): Wiz (404 ×2 on product/docs URLs; docs behind auth), Orca Security (SPA shell + 404), Google Security Command Center (timeout ×2), Prisma page bodies via ask interface (timeout ×2), Wikipedia CSPM article (timeout). Consequence: the two most prominent agentless-CNAPP vendors are **market context only**; no claims are made about their internals, and cross-product commonality is grounded in the four sampled vendors with direct/structural evidence.

## Sources

- Microsoft Learn — "Microsoft Defender for Cloud Overview" (learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction), fetched 2026-09-07. Direct evidence for: CNAPP composition (CSPM/DevSecOps/CWPP), Foundational (free) vs Defender CSPM (paid) split, recommendations, secure score, multicloud agentless connectors (AWS/GCP), Microsoft cloud security benchmark, regulatory compliance, cloud security graph/explorer, attack path analysis, governance rules, AI SPM, DSPM module, IaC findings via DevSecOps, plans for servers/containers/storage/databases/APIs.
- AWS Docs — "What Is AWS Config?" (docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html), fetched 2026-09-07. Direct evidence for: resource configuration recording, config history + relationships, config rules → noncompliant flags, continuous evaluation on create/change/delete, remediation, conformance packs, multi-account aggregators, advanced queries against current configuration state.
- AWS Docs — "Introduction to AWS Security Hub CSPM" (docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html), fetched 2026-09-07. Direct evidence for: AWS explicitly naming its product "Security Hub CSPM"; security standards (AWS FSBP, CIS, PCI DSS, NIST) as collections of controls; control findings; continuous account-level configuration checks; security scores; findings consolidation (ASFF); automation rules + suppression; EventBridge custom actions; administrator/member multi-account; cross-region aggregation; dependency on AWS Config for most controls; no retroactive findings before enablement; usage-based pricing (checks, ingested findings); 30-day trial.
- Sysdig Docs — "Posture Overview" and "Posture Findings" (docs.sysdig.com/en/sysdig-secure/posture/...), fetched 2026-09-07. Direct evidence for: page explicitly titled "Cloud Security Posture (CSPM)"; Posture Overview dashboard (passing score, high-severity passing score, 30-day trends, least-secure resources/categories/controls); Posture Findings table (severity High/Medium/Low, risk-accepted state, account ID, control name, platform AWS/Azure/GCP/OCI/Kubernetes, resource category/family/type, first-seen, grouping by control/resource); Zones as scope groupings; Posture Policies + Posture Controls; Posture Admission Policies; IaC Policy Controls; separate Identity (CIEM) module; agentless cloud account connections for AWS/Azure/GCP/OCI; SIEM forwarding (Splunk/Sentinel/QRadar/Google SecOps), Jira/ServiceNow ticketing.
- Prisma Cloud Docs — documentation sitemap (docs.prismacloud.io/sitemap.md), fetched 2026-09-07 (structure only). Evidence for: Connect Cloud Accounts (AWS org/account, Azure tenant/subscription, GCP org/project, OCI, Alibaba; per-provider "APIs ingested" lists; audit/flow/DNS log configuration); Governance (policies: custom, attack-path, anomaly, workload-protection, IAM, network exposure, custom build with code/visual editors); Cloud and Software Inventory (asset, applications, compute workloads, API endpoints, data, IaC resources); Compliance (built-in standards, custom standards, reports); Alerts (alert rules for cloud infrastructure, third-party notification targets, alert status reasons, state-change notifications, suppression, saved views); Search & Investigate (RQL asset/config/vulnerability/permission/network/audit-event query families); administration (roles, account groups, SSO, audit logs, action plans); integrations (Security Hub, GCP SCC, XSOAR, Jira, ServiceNow, Slack, Teams, PagerDuty, Splunk, webhooks); IAM Security (CIEM) and Runtime Security (Defenders, agentless scanning) as separate pillars.
- Fortinet Docs — FortiCNAPP documentation index (docs.fortinet.com/product/forticnapp), fetched 2026-09-07 (index only). Evidence for: Lacework heritage; guide set: Getting Started, Administration Guide, Alerts Reference, Integration Permissions Reference, API Reference, CLI Reference, LQL (Lacework Query Language) Reference, Policies guide.
- Internal cross-checks: `research/attack-surface-management.md` (CSPM boundary: outside-in vs inside-account config evaluation) and `research/ai-security-platform.md` (AI-SPM emerging as a Defender CSPM module) — consistency confirmations only, not independent sources.

## Product Observations

### AWS Config + AWS Security Hub CSPM (platform-native pole)

Key observations (evidence layer A):

- **Config recorder → resource inventory with configuration state and history.** AWS Config "provides a detailed view of the configuration of AWS resources," including "how the resources are related to one another and how they were configured in the past." Requires an IAM role; writes snapshots/history to S3; SNS notifications.
- **Rules as the evaluation unit.** "You can use AWS Config rules to evaluate the configuration settings of your AWS resources. When AWS Config detects that a resource violates the conditions in one of your rules, AWS Config flags the resource as **noncompliant** and sends a notification. AWS Config **continuously evaluates** your resources as they are created, changed, or deleted."
- **Conformance packs** = collections of rules deployed/monitored as a single entity; **aggregators** = multi-account/multi-region central view of inventory and compliance; **advanced queries** over current configuration state.
- **Remediation** is a first-class Config feature (remediate noncompliant resources).
- **Security Hub** (whose own docs now title it "AWS Security Hub **CSPM**"): "provides you with a comprehensive view of your security state in AWS and helps you assess your AWS environment against security industry standards and best practices." Standards (AWS FSBP, CIS, PCI DSS, NIST) each contain **controls**; "Security Hub CSPM runs checks against security controls and generates **control findings**."
- **Cross-service finding hub**: receives findings from GuardDuty/Inspector/Macie and third parties; normalizes to ASFF; can send findings onward. Correlates findings across providers for prioritization.
- **Security scores** computed from check results; "identifies specific accounts and resources that require attention."
- **Automation**: automation rules modify/suppress findings by criteria; EventBridge integration for automatic responses; custom actions to send findings to ticketing/remediation systems.
- **Multi-account**: administrator/member accounts; cross-region aggregation.
- **Dependency rule**: "Security Hub CSPM uses service-linked rules from AWS Config to run security checks for most controls. You must enable AWS Config and record resources in AWS Config for Security Hub CSPM to generate most control findings." → posture checks sit on top of a configuration-data layer.
- **Enablement boundary**: "only detects and consolidates findings that are generated after you enable"; no retroactive detection. Full CIS coverage requires enabling in all supported Regions.
- Pricing: per security check and per ingested finding; 30-day trial (usage-based commercial shape).

### Microsoft Defender for Cloud (cloud-native CNAPP pole)

Key observations (evidence layer A):

- Explicit CNAPP decomposition: "**Cloud Security Posture Management (CSPM)** checks and improves the security posture of cloud resources", DevSecOps, and "**Cloud Workload Protection Platform (CWPP)** defends workloads such as VMs, containers, storage, databases, and serverless functions from threats."
- **Tiered posture**: free "Foundational CSPM" (centralized policy management, secure score, multicloud agentless coverage, CSPM dashboard) vs paid "Defender CSPM" (governance, regulatory compliance, cloud security explorer/graph, attack path analysis, data-aware posture/DSPM, AI SPM).
- **Policy → recommendations**: "The policy translates to recommendations that identify resource configurations that violate your security policy. The Microsoft cloud security benchmark is a built-in standard…" — recommendations are the finding type; secure score summarizes posture and "improves as you remediate recommendations."
- **Multicloud by agentless connection**: "Connect to your multicloud environments by using agentless methods for CSPM insight" (AWS and GCP onboarding).
- **Graph/context features** (paid): cloud security graph, cloud security explorer (query-based), attack path analysis (model risk paths before changes).
- **Governance loop**: security governance assigns tasks to resource owners and tracks progress — posture program management machinery.
- **Adjacent posture extensions**: DSPM ("automatically discovers datastores containing sensitive data"), AI SPM (AI BOM, AI workload discovery), DevSecOps (IaC misconfigurations + exposed secrets in repos/pipelines, correlated with cloud context).
- CWPP plans (servers/containers/storage/databases/App Service/Key Vault/APIs/Resource Manager) are clearly separate plan lines from CSPM — confirms the workload/config split.
- Security alerts (threat detections) are a CWPP-side artifact; CSPM side produces recommendations — two different artifact families inside one product.

### Sysdig Secure (third-party CNAPP pole — Posture module)

Key observations (evidence layer A):

- The docs literally frame Posture as CSPM: "The Posture > Overview page provides a high-level view of your **Cloud Security Posture (CSPM)**".
- **Scope grouping**: "Zones — logical groupings of resources such as accounts, clusters, or applications"; global dashboard filters by Zone and Platform (AWS, Azure, GCP).
- **Scores**: "Posture Passing Score: percentage of controls that pass across all severities"; high-severity passing score; 30-day time-series for both ("detect posture improvements or regressions").
- **Prioritization widgets**: least-secure resources by category, resources with lowest passing score, controls with lowest passing score (high severity / all), findings-by-severity trend.
- **Findings table**: control × resource rows; filters (severity High/Medium/Low, risk accepted, account ID, cluster name, control name, organization, owner, platform, resource category/family/type/ID/name); grouping by control or resource; **First Seen** timestamp; **Accepted** flag.
- **Policy machinery**: Posture Policies ("Manage Posture Policies", "Posture Controls"), Posture Admission Policies (gate at deployment), IaC Policy Controls integrated from source-code-management connections.
- **Separate sibling modules** (confirms CNAPP composition): Threats (runtime detection with Falco), Vulnerabilities (CVE management), Identity (CIEM — users/roles/groups/service-identities entitlement optimization), Compliance (findings; "Legacy Versions" implies an evolving compliance engine), Inventory, Reporting.
- **Connectivity**: cloud account onboarding for AWS/Azure/GCP/OCI described with "Agentless Connections" troubleshooting pages; optional agents (Shield) for runtime; per-provider permission pages ("Permissions and Resources").
- **Outbound flows**: forwarding findings to SIEM/data platforms (Splunk, Sentinel, QRadar, Google SecOps, Kinesis, SQS, syslog, webhooks), ticketing (Jira, ServiceNow).

### Prisma Cloud (third-party CNAPP pole — Governance pillar; structure-level evidence)

Key observations (evidence layer A at structure level — page bodies not fetched, so no behavioral claims):

- Documentation organized by: **Connect** (cloud accounts onboarding per provider: AWS organizations/accounts with role setup and "APIs ingested by Prisma Cloud" lists; Azure tenants/subscriptions; GCP organizations/projects; OCI tenants; Alibaba accounts; audit/flow/DNS log configuration) → **Governance** (policies: custom, attack path, anomaly, workload protection, IAM, network exposure; custom build policies with code/visual editors) → **Cloud and Software Inventory** (asset inventory, applications, compute workloads, API endpoints, data inventory, IaC resources) → **Compliance** (built-in compliance standards, custom compliance standards, compliance reports) → **Alerts** (alert rules for cloud infrastructure, third-party notifications, alert status reasons, state-change notifications, suppression, saved views) → **Search and Investigate** (query families: asset, asset configuration, vulnerability, permission, network, audit event; RQL operators; query library) → **Administration** (roles, account groups, SSO, audit logs, action plans, collections).
- External integrations include AWS Security Hub, Google Security Command Center, Cortex XSOAR, Jira, ServiceNow, Slack, Teams, PagerDuty, Splunk, webhooks — the CSPM interoperates with both platform-native posture services and SOC/ticketing tools.
- IAM Security (CIEM) and Runtime Security (Defenders, agentless scanning) are separate pillar trees — again confirming that posture, identity posture, and workload protection are distinct modules.
- "Action Plans" under administration — remediation-plan artifact (structure-level only).

### FortiCNAPP / Lacework (agent-heritage pole; index-level evidence)

Key observations (evidence layer A at index level only):

- Documentation index: Getting Started, Administration Guide, Release Notes, Agent Support, CLI Reference, Alerts Reference, Integration Permissions Reference, API Reference, **LQL (Lacework Query Language) Reference**, **Policies** guide.
- Product is positioned by the vendor under "Cloud-Native Security / Cloud-Native Application Protection" and renamed from Lacework — consistent with the market-wide CNAPP consolidation; retains a query-language policy engine and alerts reference as the posture machinery.

### Cross-check with internal sibling research (context only)

- The ASM leaf recorded the CSPM boundary from the other side: "CSPM evaluates configurations inside connected cloud accounts. ASM observes exposure from outside; cloud connectors are the bridge, not the core." Consistent with this pass.
- The AI Security leaf recorded that AI-SPM ships as a Defender CSPM plan module — an example of the general pattern: new posture domains (data, AI) get absorbed as CSPM modules rather than changing the CSPM core.

## Cross-product Comparison

| Dimension | AWS Config + Security Hub | Defender for Cloud | Sysdig Secure | Prisma Cloud | FortiCNAPP (Lacework) |
|---|---|---|---|---|---|
| Cloud visibility source | AWS Config recorder (API-side, IAM role); "must enable AWS Config" for most Security Hub controls | Agentless multicloud connectors (AWS/GCP) + Azure-native; agents only for CWPP plans | Agentless cloud account connections (AWS/Azure/GCP/OCI); optional Shield agents for runtime, not posture | Connector per provider with documented "APIs ingested"; role/credential authorization (structure) | Agent-heritage platform + cloud integrations ("Integration Permissions Reference"); agents not posture-definitional |
| Inventory | Resource configuration + history + relationships | Asset inventory / recommendations per resource | Inventory (resources) + Zones scope | Cloud & software inventory incl. IaC resources (structure) | (not fetched at this depth) |
| Evaluation unit | Config rules → noncompliant resources; standards = controls → control findings | Policy (benchmark-backed) → recommendations | Posture Policies made of Posture Controls → findings | Policies (build/cloud/workload/IAM/network families) → alerts | Policies; LQL queries (index-level) |
| Finding name | control findings / noncompliant resources | recommendations | posture findings | alerts | alerts |
| Severity | severity on findings | (recommendation severity; secure score impact) | High/Medium/Low | (structure-level; not asserted) | (not asserted) |
| Posture score | security scores from check results | secure score | Posture Passing Score + high-severity score + 30-day trend | (not asserted) | (not asserted) |
| Compliance mapping | standards: AWS FSBP, CIS, PCI DSS, NIST; per-standard compliance view | regulatory compliance dashboard (paid); Microsoft cloud security benchmark built-in | Compliance module with findings (benchmarks; legacy engine) | built-in + custom compliance standards, reports (structure) | (not asserted) |
| Finding lifecycle | open until resource compliant; suppression via automation rules; resolved-state on ASFF; no retroactive findings before enablement | remediate recommendations → score improves; governance tasks to owners | risk-accepted state; first-seen timestamps; drill to remediation | alert status reasons, state-change notifications, suppression (structure) | (not asserted) |
| Remediation | Config remediation (automated fix actions) | recommendations carry fix guidance; governance tracks | remediation actions from findings page | action plans (structure) | (not asserted) |
| Outbound integrations | EventBridge, SNS, third-party providers both directions | SIEM/SOAR/ITSM export for alerts; Defender XDR portal | SIEM forwarding, Jira/ServiceNow | Security Hub, SCC, XSOAR, Jira, ServiceNow, Slack, Teams, PagerDuty, Splunk, webhooks (structure) | alerts/integrations references (index) |
| Multi-account machinery | aggregators; administrator/member accounts; cross-region aggregation | management-group/subscription structure; multicloud connectors | Zones; organization/account/project scoping | account groups; org-level onboarding (structure) | (not asserted) |
| IaC / shift-left | (config history covers API changes; IaC scanning not the Config model) | DevSecOps: IaC misconfigurations + secrets in repos/pipelines | IaC policy controls from SCM connections; CLI scanner IaC mode | custom build policies; IaC resources in inventory (structure) | (not asserted) |
| Adjacent modules in same product | GuardDuty/Inspector/Macie feed findings in | CWPP plans; DSPM; AI SPM | Threats, Vulnerabilities, Identity (CIEM) | Runtime Security, IAM Security, network security | (not asserted) |

Reading: the *connect → inventory → policy evaluation → findings → remediation/track* loop appears in every sampled product regardless of pole. Compliance-mapped standards, severity, scores, acceptance/suppression, multi-account scoping, and outbound integrations appear in ≥3 sampled products — Layer B (cross-product commonality). Graph/context engines and attack-path analysis appear in the premium tiers of some products — optional structure, not definitional.

## Canonical Model

### L0 — Defining Invariant (minimal)

A Cloud Security Posture Management application is recognizable by exactly this structure:

1. **Connected cloud environment** — a standing, credential-authorized read connection into the customer's cloud (account/subscription/project/tenant) through the cloud providers' own management APIs or recording mechanisms. Without this, there is no cloud to have posture about.
2. **Cloud resource inventory with configuration state** — the discovered cloud resources (compute, storage, network, identity, database, etc.) and their current configuration, maintained as data inside the application. Without this it is a point-in-time audit, not management.
3. **Policy-driven configuration evaluation** — evaluation of that configuration against a library of security policies/controls (provider best practices, industry benchmarks, custom rules), producing pass/fail assessments per resource per control. Without this, it is a config inventory tool (asset management), not posture assessment.
4. **Misconfiguration findings as managed, continuously re-evaluated records** — a finding binds an affected resource to a failed control with a severity, persists until the configuration passes (or the risk is accepted), and is re-evaluated as the environment changes. Without tracking over time, it is a scan report, not posture management.

Test: remove the connected-cloud-account data source → generic policy checker; remove evaluation → cloud inventory/asset management; remove findings-with-lifecycle → static compliance report; remove resource-configuration domain → SaaS posture (SSPM) or generic compliance platform.

### L1 — Common Mature Structure (cross-product, evidence layer B)

- Cloud-provider connectors with role/credential-based read authorization; organization/tenant-level onboarding; per-provider supported-API scopes.
- Multi-cloud coverage as the third-party default (AWS/Azure/GCP, often OCI/Alibaba); platform-native products are single-cloud by construction.
- Built-in control libraries; benchmark/regulatory framework mapping (CIS, PCI DSS, NIST, ISO/SOC 2 families; provider-native benchmarks like AWS FSBP and Microsoft cloud security benchmark) with compliance views and reports.
- Severity classification of findings; posture/security scores with trend views; prioritization views (worst resources/controls).
- Remediation guidance attached to findings (and remediation execution in some products); risk acceptance/suppression as managed state; first-seen/last-seen timestamps.
- Notification/forwarding machinery: alert rules, email/chat targets, ITSM (Jira, ServiceNow, PagerDuty), SIEM/event-bus forwarding, webhooks.
- Governance scoping: account groups/zones/aggregators, administrator/member or role hierarchies, RBAC, SSO, audit logs.
- APIs/CLI; query languages or filter systems over inventory and findings.
- IaC policy controls / code-to-cloud linkage in modern products.

### L2 — Variant / Optional Structure

- Attack-path analysis / relationship-graph context engines ("toxic combination" reasoning) — premium tier features in some products.
- Agentless vs sensor-based collection as the product philosophy axis; hybrid (agents for runtime, API for posture).
- Auto-remediation execution (config-driven fixes, event-triggered automation) vs guidance-only.
- Drift detection and configuration history/change timelines (strongest in the config-recorder pole).
- Kubernetes/container posture (KSPM), admission-control enforcement at deploy time.
- Sibling modules inside the same platform: CIEM (identity entitlements), DSPM (data-aware posture), AI SPM, vulnerability scanning, cloud detection & response — the CNAPP bundle shape.
- Standalone CSPM vs cloud-native free tier vs paid plan vs CNAPP module (packaging axis).
- Regulated-industry/government tuning; sovereign/regional deployments.
- Custom policy authoring depth (visual editors, query languages).

### L3 — Vendor-specific (research notes only)

- AWS: Config recorder/S3-snapshot/SNS plumbing; conformance packs; aggregators; ASFF finding format; automation rules; EventBridge custom actions; Security Hub pricing per check/ingested finding + 30-day trial; "all Regions" CIS caveat; renaming to "AWS Security Hub CSPM".
- Microsoft: Foundational vs Defender CSPM plan split; secure score; Microsoft cloud security benchmark; cloud security graph/explorer; Defender portal migration note; governance rules; AI BOM; DSPM module in CSPM plan; plan ladder (Servers P1/P2 etc.); Defender XDR integration.
- Sysdig: Zones; North-Star passing-score metrics; Posture Admission Policies; Risk Accepted filter; SysQL; Falco-based Threats sibling; "Legacy Versions" of compliance engine; IaC mode in CLI scanner.
- Prisma Cloud: RQL; alert rules per scope; alert status reasons; action plans; collections; account groups; Code-to-Cloud dashboard; per-provider "APIs ingested" docs; Defenders/agentless scanning under Runtime Security; Enterprise vs Compute editions.
- Lacework/FortiCNAPP: LQL; renaming under Fortinet; agent-support guide as first-class doc.

## Vendor-specific Findings

(See L3 — none of these enter the canonical document except as unnamed variant examples.)

## Boundary Findings

| Neighbor | Sharpest seam | Remove-what-to-become test |
|---|---|---|
| CNAPP | CNAPP is the umbrella platform; CSPM is its posture core module. Every sampled CNAPP documents posture as one pillar among workload/identity/data pillars. | Remove workload runtime protection, CIEM, runtime detection from the bundle → CSPM. |
| CWPP | CWPP defends running workloads (VMs/containers/serverless) with sensors/threat detection; CSPM evaluates configuration state. Defender splits these into plan families; Sysdig splits Posture vs Threats. | Point the evaluation at runtime/host behavior with agents → CWPP. |
| SSPM | Object domain: SaaS tenant configuration (M365/Salesforce-style app settings) vs cloud infrastructure resources. | Swap cloud-account connectors for SaaS-app connectors → SSPM. |
| DSPM | Object domain: data stores/content sensitivity/exposure vs infrastructure configuration. Defender ships DSPM inside the CSPM plan — a module relationship. | Make data content/sensitivity the assessed object → DSPM. |
| Vulnerability Management | VM assesses software flaws (CVEs in installed software/images); CSPM assesses configuration choices. They coexist as sibling modules (Sysdig Vulnerabilities vs Posture; Defender CSPM adds agentless vuln scanning as a paid module). | Assessment keyed to CVE/software inventory → VM. |
| Attack Surface Management (ASM) | ASM discovers/examines the org's footprint from outside without prior knowledge of assets; CSPM evaluates inside connected accounts using granted credentials. (Consistent with the ASM leaf's recorded seam.) | Replace credentialed inside-account assessment with outside-in observation → ASM. |
| Cloud Management Platform | CMP operates/provisions/monitors cloud for efficiency; CSPM evaluates security configuration. Overlap only in shared inventory. | Remove security-policy evaluation and findings → CMP. |
| Security Compliance Platform (§11) | Organizational compliance-program workflow (obligations, audits, evidence, attestations) vs technical cloud-config assessment. Compliance-framework mapping inside CSPM is a *view* over technical controls, not a program workflow. | Remove the resource×control engine; manage obligations/audits instead → Compliance Management Platform. |
| SIEM | SIEM correlates security events/logs for detection; CSPM evaluates standing configuration state. The finding→SIEM forwarding integration documents the seam. | Event/log stream analysis as the core → SIEM. |
| IaC Platform | IaC platforms author/provision infrastructure; CSPM (via IaC scanning) evaluates the same definitions for risk. Code-to-cloud tracing bridges them. | Authoring/deployment of resources → IaC Platform. |
| Cyber Asset Management | Inventory-centric across all environments; CSPM is assessment-centric over cloud configuration. Inventory is one CSPM component, not the whole. | No policy/finding machinery → asset management. |
| Configuration Management (§14) | Server/endpoint OS configuration (often agent-based IT domain) vs cloud-native resource configuration. | Target OS/app config on hosts → Patch/Config Management. |

Type-honesty note: the directory also lists CNAPP, CWPP, SSPM, DSPM as separate leaves. This research supports those as separate Types only in the packaging sense (CSPM = posture core; the others = workload/sibling modules or umbrella). Market reality is that most "CSPM" products ship as CNAPP platforms with these modules; the leaves should document the *module cores* separately, which this document does for CSPM.

## Uncertainties

- Wiz and Orca (agentless CNAPP leaders) could not be fetched — no claims made about them; the agentless-vs-sensor variant axis is grounded in Defender ("agentless methods") and Sysdig ("Agentless Connections") docs plus Prisma's agentless-scanning tree, so the axis itself is well supported, but those two vendors' distinctive mechanics (graph engines, side-scanning) are unverified here.
- Google Security Command Center not fetched (timeouts) — the GCP platform-native pole is reasoned structurally (Azure/AWS platform-native evidence is strong), not asserted from GCP docs.
- Prisma Cloud and FortiCNAPP evidence is structural (sitemap/index), not behavioral — no defaults, limits, or workflow specifics asserted for them.
- Exact counts of built-in controls/standards, and pricing mechanics, are product-specific and intentionally not generalized.
- Whether "continuous event-driven" vs "periodic re-evaluation" is universal is not fully verifiable from fetched text; AWS's "continuously evaluates… as they are created, changed, or deleted" is the strongest direct formulation. The canonical claim is kept at "re-evaluated as the environment changes."

## Final Synthesis

CSPM is the *configuration-state* security system of record for cloud estates. Its defining loop — connect to cloud accounts with read credentials, maintain a resource-configuration inventory, evaluate that configuration continuously against a policy/control library, and manage the resulting misconfiguration findings (severity, ownership, acceptance, remediation, resolution) — appears identically in the platform-native pole (AWS Config+Security Hub, Defender for Cloud) and the third-party pole (Sysdig, Prisma Cloud, Lacework/FortiCNAPP). Everything else in modern products — compliance framework mapping, scores, IaC shift-left, attack-path graphs, CIEM/DSPM/AI-SPM modules, auto-remediation — is layered structure on that loop, and the CNAPP form is the packaging of this loop together with workload/identity/data siblings. The historical check holds: AWS Config (pre-"CSPM" term), platform-native policy engines, and open-source-era API scanners all satisfy the minimal definition; agents, graphs, attack paths, and multi-cloud breadth are market-era additions, not the Type.
