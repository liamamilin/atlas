# Research Notes — CNAPP (Cloud-Native Application Protection Platform)

## Research Goal

Understand what a Cloud-Native Application Protection Platform actually is as an application type: what it consists of, what its defining structure is (as distinct from its pillar siblings CSPM and CWPP, both already documented in this atlas), how the unified platform differs from a portfolio of separately operated point tools, and where the boundaries with neighboring security types lie.

Special methodological situation: two sibling leaves (CSPM, CWPP) were researched the same day from overlapping product samples. This research deliberately reuses those observations where they bear on the CNAPP boundary, and focuses new evidence on the *platform-level* structures: unified inventory, cross-domain correlation, shared policy/query/administration planes, and domain breadth.

## Initial Boundary

Working hypothesis before research:

- CNAPP is a **platform-level packaging** of multiple cloud security functions — posture management (CSPM), workload/runtime protection (CWPP), identity entitlement analytics (CIEM), and often data posture (DSPM) — sold and operated as one product.
- It is最容易混淆的邻近 Type：CSPM（posture core）、CWPP（runtime pillar）、以及"security suite"（多产品无统一数据面）。
- Key open question: does CNAPP have a defining core of its own, or is it only an alias/umbrella over CSPM+CWPP+…? If it has a core, it is most plausibly the *unification itself* (shared inventory + single risk picture) rather than any additional behavior.

## Research Questions

1. How do vendors themselves define CNAPP? (Self-descriptions matter for a vendor-coined category.)
2. What domains do sampled CNAPP products actually cover, and which domains are definitional vs optional?
3. What platform-level structures exist across products: unified inventory? graph/correlation? shared query languages? shared policy framework? shared administration?
4. How does onboarding work (cloud account connection vs sensor deployment), and how does the agentless-vs-sensor split map onto the platform?
5. How are risks from different domains combined (attack paths, toxic combinations, in-use prioritization)?
6. What is the packaging model (plans, pillars, editions) and is it variable across products?
7. Boundary: what would a product need to *lack* to stop being a CNAPP and become a CSPM, a CWPP, or a mere portfolio?
8. Historical check: did integrated multi-domain cloud security platforms exist before the CNAPP term, and do they fit the same core?

## Representative Products

| Product | Heritage / philosophy | Customer posture | Evidence quality |
|---|---|---|---|
| Microsoft Defender for Cloud | platform-native (Azure-operated, multi-cloud via connectors) | free foundational tier + paid plans, per-workload plans | Tier 1 docs, full pages (fetched) |
| Prisma Cloud (Palo Alto Networks) | suite giant; the product most associated with coining/pushing the CNAPP framing | enterprise; Enterprise vs Compute editions; SaaS or self-hosted console | Tier 1 docs map (llms.txt, full index fetched) |
| Sysdig Secure | runtime heritage (Falco), posture added; on-prem available | mid-market to enterprise | Tier 1 docs, overview page + full doc tree (fetched) |
| Wiz | agentless-first pure-play; graph-centric; largest pure-play CNAPP vendor | enterprise (Fortune-100 heavy) | Tier 2 product page (fetched); docs behind login |
| FortiCNAPP (formerly Lacework) | agentless-heritage (Lacework Polygraph), acquired by Fortinet | enterprise | structure-level only (guide set index; nav shell) |

Sample spans: platform-native vs third-party; agentless-first vs sensor-heritage vs suite; pure-play vs suite module; SaaS vs self-hosted; free-tier vs enterprise-only.

## Sources

- Microsoft Learn — "Microsoft Defender for Cloud Overview" — https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction — fetched 2026-09-07 (A)
- Microsoft Learn — "What is Cloud Security Posture Management (CSPM)" — https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management — fetched 2026-09-07 (A)
- Prisma Cloud documentation index (llms.txt full doc map) — https://docs.prismacloud.io/llms.txt — fetched 2026-09-07 (A, structure)
- Sysdig — "Sysdig Secure" documentation overview + full TOC — https://docs.sysdig.com/en/docs/sysdig-secure/ — fetched 2026-09-07 (A)
- Wiz — "Cloud & AI Security Platform" product page — https://www.wiz.io/platform — fetched 2026-09-07 (B, marketing/positioning only)
- Fortinet — FortiCNAPP documentation library / Getting Started + Administration Guide index — https://docs.fortinet.com/product/forticnapp , https://docs.fortinet.com/document/forticnapp/latest/administration-guide — fetched 2026-09-07 (C, structure/navigation only; page body is a nav shell)
- Prior same-day atlas research: research/cloud-security-posture-management-cspm.md and research/cloud-workload-protection-cwpp.md (overlapping samples: Defender, Sysdig, Prisma, FortiCNAPP)

Source-access limitations:

- Wiz's operational documentation is behind login; evidence is product-page level. Claims about Wiz's internal mechanics are not made; its platform page confirms positioning structures (agentless connection, Security Graph, attack paths, projects/RBAC, code-to-cloud, runtime sensor) at positioning level only.
- FortiCNAPP's documentation body could not be fetched (navigation shell); evidence is the documented guide set (Getting Started, Administration Guide, Alerts Reference, Integration Permissions Reference, API/CLI References, LQL (Lacework Query Language) Reference, Policies guide) — structure-level. The "Lacework FortiCNAPP" naming and "Cloud-Native Security" placement are visible in Fortinet's product library.
- No precise numbers (plan prices, resource counts, limits) are used anywhere; none were needed.

## Product Observations

### Microsoft Defender for Cloud (A — direct)

- Self-definition (docs, 2026-08 revision): "Microsoft Defender for Cloud is a Cloud Native Application Protection Platform (CNAPP), which is a unified solution that combines multiple cloud security tools to protect applications across their entire lifecycle." Three named core components: CSPM, DevSecOps (code-level security), CWPP.
- Plan architecture: one platform, per-domain plans — CSPM plan (with free "Foundational CSPM" vs paid "Defender CSPM" split), Servers, Containers, Storage, Databases, Key Vault, App Service, Resource Manager, APIs, AI Services. Capabilities activate per plan.
- Platform-level structures documented: asset inventory spanning Azure/AWS/GCP/on-prem (Arc) plus registries (Docker Hub, JFrog); secure score; recommendations; cloud security graph; attack path analysis; cloud security explorer (query-based risk hunting); risk prioritization; governance rules (assign remediation to resource owners, track); regulatory compliance standards; code-to-cloud mapping (containers, IaC); data security posture management (sensitive data discovery); internet exposure analysis; external attack surface (EASM); AI SPM (AI BOM); workflow automation; export to SIEM.
- Onboarding: agentless connection for multicloud CSPM insight and CWPP protection; sensors for workload defense plans.
- Defender XDR portal integration — the platform converging into the vendor's wider security operations surface.

### Prisma Cloud (A — direct doc map; structure)

- Documentation map reveals the platform skeleton: Connect (cloud accounts across AWS/Azure/GCP/OCI/Alibaba, incl. organization-level onboarding; image registries; code/build providers; Defender agents) → Governance (one policy framework containing custom policies, **attack path policies**, anomaly policies, workload protection policies, IAM policies, network exposure policies, build policies) → **Cloud and Software Inventory** (Applications, Assets, Unmanaged Assets, Compute Workloads, API Endpoints, Data, IaC Resources) → Compliance (built-in + custom standards) → Reports → Dashboards (Code to Cloud, Command Center, Compliance, Discovery & Exposure Management, Identity, Vulnerabilities, Application Security) → Alerts + "Risk Prioritization and Remediation" → Search & Investigate (RQL queries spanning asset, configuration, vulnerability, application, permissions, network, audit-event domains) → Runtime Security (Defender family: container/host/orchestrator/serverless/app-embedded + agentless scanning; self-hostable Console) → IAM Security / CIEM (identity inventory, effective permissions, investigations, IdP integration incl. Okta) → Network security (Cloud Network Analyzer, container network exposure) → Administration (account groups, collections, custom permission groups, roles, SSO, license types, audit logs).
- Interpretation (C): the single documentation spine — one inventory, one policy framework, one query language, one alert/risk layer spanning all domains — is the platform-level structure this research is looking for.
- Editions: Enterprise Edition vs Compute Edition split documented (licensing structure exists; specifics not needed here).

### Sysdig Secure (A — direct)

- Self-definition: "Sysdig Secure is a Cloud-Native Application Protection Platform (CNAPP), delivering Threat Detection, vulnerability management, posture management, and identity & entitlement management. Powered by runtime insights…"
- Named platform features: "Risk prioritization to help you remediate on the most critical security issues"; "A unified view of all cloud risks and threats with Cloud Attack Graph"; AI assistant (Sysdig Sage) across search/vulnerability/detection workflows.
- Doc tree confirms platform-level structures: **Inventory** (Resources, Kubernetes Live, Network, Zones, Search, SysQL query language) → **Risk** (Risk Definitions, Risk Exceptions) → **Threats** (Events; Investigate: Activity Audit, Captures; Respond: Rapid Response, Response History, Response Actions) → **Vulnerabilities** (pipeline/registry/runtime; "In Use" prioritization; Accepted Risk) → **Posture** (findings, compliance) → **Identity** (CIEM: users/roles/groups/service identities, entitlement optimization) → Policies (threat detection incl. Falco libraries; VM policies; posture policies; supply-chain; admission) → Integrations (SIEM/SOC, IaC, Okta, SCM, ticketing) → Reporting.
- Cloud account onboarding per provider (AWS/Azure/GCP/OCI) with sensors (Host/Cluster Shield) + agentless components (Cloud Shield/CloudConnector); on-premises deployment exists.
- Artifact families stay distinct: events (runtime) vs posture findings vs vulnerability findings, each with own views and policies.

### Wiz (B — product page, positioning)

- Platform page structures (positioning level): agentless visibility via API connection "in minutes" across PaaS, VMs, containers, serverless, agents, models, repositories, pipelines; **Security Graph** ("analyzes the relationships between technologies running in your cloud environment… uncover the most critical pathways to a breach… single console"); **attack path analysis** ("toxic combinations… single list of prioritized issues"); cloud threat intelligence; projects + RBAC ("each team can own their own risks"); code-to-cloud correlation (resource → code/pipeline/developer; 1-click fix via pull request); cloud-to-code hardening (root-cause forensics); runtime protection via Wiz Sensor combined with agentless coverage; Champion Center (program adoption/maturity); workflow orchestration (no-code canvas).
- Product line names: Wiz Cloud, Wiz Defend (runtime), Wiz Code; AI-application protection positioning (AI-APP).
- Third-party category validation on the page: "Forrester Wave™: Cloud Native Application Protection Solutions, Q1 2026" — the category is externally recognized, not only vendor-coined.
- Caution: marketing page; used only for positioning structures, not operational mechanics.

### FortiCNAPP, formerly Lacework (C — structure only)

- Fortinet's library places it under "Cloud-Native Security" (alongside FortiDevSec) and retains "Lacework FortiCNAPP" naming — acquisition heritage visible.
- Documented guide set (from library): Getting Started, Administration Guide, Alerts Reference, Integration Permissions Reference, API Reference, CLI Reference, **LQL (Lacework Query Language) Reference**, Policies guide. The existence of a named cross-domain query language (LQL) and a policies guide is consistent with the platform structures seen elsewhere, but no page bodies were reachable — no operational claims are made for this product here.
- Prior same-day atlas research (CSPM/CWPP notes) recorded the same guide-set evidence plus Lacework heritage claims (Polygraph visualization heritage) at the same evidence tier.

## Cross-product Comparison

| Structure | Defender for Cloud | Prisma Cloud | Sysdig Secure | Wiz | FortiCNAPP |
|---|---|---|---|---|---|
| Multi-cloud account connection (agentless, org-level) | yes (A) | yes (A) | yes (A) | yes (B) | yes (C, implied by guide set) |
| Unified estate inventory spanning config + workloads | asset inventory (A) | Cloud & Software Inventory: assets/workloads/APIs/data/IaC (A) | Inventory (A) | Security Graph substrate (B) | n/a (C) |
| Configuration posture evaluation | yes (A) | yes (A) | yes (A) | yes (B) | yes (C, guide set) |
| Vulnerability management (pipeline/registry/runtime) | yes, agentless (A) | yes (A) | yes (A) | yes (B) | yes (C) |
| Runtime threat detection + response | yes (CWPP plans) (A) | yes (Defender agents) (A) | yes, Falco heritage (A) | yes, Wiz Sensor (B) | yes (C) |
| Identity-entitlement analytics (CIEM) | documented for Defender CSPM-era product family (prior research, A); not re-verified today | yes, IAM Security (A) | yes, Identity/CIEM (A) | identity as graph context (B) | n/a (C) |
| Data posture (DSPM) | yes (A) | Data Inventory (A) | Data Security Findings (A, doc tree) | data as graph context (B) | n/a (C) |
| Cross-domain correlation / attack paths | cloud security graph + attack path analysis + security explorer (A) | attack path policies + query exploration (A) | Cloud Attack Graph + Risk (A) | Security Graph + attack paths / toxic combinations (B) | Polygraph heritage (C, prior notes) |
| Cross-domain risk prioritization | yes (A) | yes (A) | yes (A) | yes (B) | n/a |
| Platform-wide query language | security explorer queries (A) | RQL (A) | SysQL (A) | graph queries (B) | LQL (C, existence only) |
| Shared policy framework with per-domain policy types | policy + recommendations + compliance standards (A) | one governance section, multiple policy families (A) | one Policies section: threat/VM/posture/supply-chain/admission (A) | n/a (B) | Policies guide (C) |
| Code-to-cloud linkage | yes (A) | yes (A: IaC resources, code-to-cloud dashboard) | pipeline scanning (A) | yes (B) | FortiDevSec adjacent (C) |
| Compliance frameworks + reports | yes (A) | yes (A) | yes (A) | yes (B) | yes (C) |
| Findings/alerts lifecycle + SIEM/ITSM forwarding | yes (A) | yes (A) | yes (A) | yes (B) | yes (C) |
| Scoping / RBAC machinery | management groups/subscriptions (A) | account groups, collections, permission groups (A) | teams, zones (A) | projects + RBAC (B) | n/a |
| Packaging variability | free foundational vs paid; per-workload plans (A) | editions (Enterprise/Compute) (A) | subscription; Secure vs Monitor sibling (A) | platform bundles (B) | part of Fortinet portfolio (C) |
| Self-hosted option | no (Microsoft-operated) (A) | yes (self-hosted Console) (A) | yes (on-premises) (A) | no evidence (B) | n/a |

Reading: every reachable product documents or positions the same platform skeleton — connect → unified inventory → multi-domain evaluation → cross-domain correlation/prioritization → one risk lifecycle → shared reporting/administration. Domain *breadth* varies (CIEM/DSPM/API/AI-SPM are not uniformly present); the *multi-domain unification* itself is universal in the sample.

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

```text
Connected cloud estate (customer's cloud accounts and the workloads running in them;
                        standing credential-authorized connection — agentless API and/or sensors)
└── Unified estate inventory — the estate held as ONE inventory/data model spanning
    resource configuration AND running workloads (identities/data/APIs/code in mature products)
└── Multi-domain security evaluation — more than one security domain continuously assessed
    against that shared inventory (configuration posture + at least one of:
    vulnerabilities / runtime threats / identity entitlements)
└── Single risk picture — findings, events and risks from all domains are correlated,
    prioritized and operated in one platform (one console, shared policy/query/
    integration/administration plane), not as separately operated point tools
```

Four properties. Remove any one:

- remove the unified inventory or the single risk picture → you have separate point tools sold together (a portfolio, not a platform);
- remove multi-domain evaluation → you have a single-domain tool (a CSPM, a CWPP, a CIEM, a vulnerability scanner);
- remove the connected estate → there is nothing to protect.

The defining core of CNAPP is the **unification itself**. A CNAPP is not defined by any one security behavior (those belong to its pillar types) but by operating several of them on one shared estate data model as one managed risk picture.

### L1 — Common Mature Structure

Present in essentially all mature sampled products; expected by the market but not definitional:

- **Cross-domain correlation layer** — security graph / attack-path analysis / "toxic combination" detection joining configuration, vulnerability, identity, exposure and runtime context into reachable-risk narratives (Defender cloud security graph + attack paths; Sysdig Cloud Attack Graph; Prisma attack path policies; Wiz Security Graph). The *graph as explicit productized feature* is the mature implementation of the L0 "single risk picture", not the definition itself.
- **Cross-domain risk prioritization** — a unified priority order across domains (e.g., in-use/runtime context for vulnerabilities; exposed+privileged+critical-resource combinations).
- **Platform-wide query/search** — one query language or explorer spanning all domains (RQL, SysQL, LQL, Defender security explorer, Wiz graph queries).
- **Shared policy framework** — one governance surface with per-domain policy families (posture controls, threat rules, vulnerability policies, IAM policies, admission/supply-chain policies).
- **Compliance mapping & reporting** — benchmark/regulatory frameworks computed over the same data (CIS-style, PCI DSS, NIST families, provider standards), audit-ready reports.
- **Findings/alerts lifecycle + outbound forwarding** — triage → assign → accept → remediate; SIEM/ITSM/chat integration.
- **Code-to-cloud linkage** — connecting runtime resources to the repositories, pipelines and IaC that produced them; fix-at-source flows (PR generation in some products).
- **Scoping & RBAC machinery** — org-modeled groupings (account groups/collections/teams/zones/projects) with role-scoped visibility; SSO.
- **Coverage & health monitoring** — connection status, agent/sensor health, blind-spot visibility.
- **Remediation guidance and ownership routing** — per-finding guidance, owner assignment, governance workflows.

### L2 — Variant / Optional Structure

Depends on vendor philosophy, customer scale, packaging:

- **Domain breadth** — core four (posture, vulnerabilities, runtime threats, identity entitlements) vs extended portfolio: data posture (DSPM), API security posture, AI/ML security posture (AI-SPM, AI BOM), external attack surface (EASM), Kubernetes posture (KSPM), serverless depth.
- **Collection mechanism** — agentless-first (API/snapshot) vs sensor-first (kernel/cluster agents) vs hybrid; the mix varies even inside one product (Prisma: Defenders + agentless scanning; Defender: agentless CSPM + sensor plans; Wiz: agentless + Wiz Sensor).
- **Platform-native vs third-party** — a cloud provider's own CNAPP spanning its own + other clouds (Defender for Cloud) vs cloud-agnostic independent platforms.
- **Deployment posture** — SaaS-only vs self-hosted/on-premises console (Prisma, Sysdig) including air-gapped.
- **Packaging model** — free foundational tier vs paid plans (Defender), per-domain plans, editions/licensing (Prisma), pillar bundles (Wiz), portfolio embedding (FortiCNAPP within Fortinet).
- **Runtime response depth** — detection-only vs response actions (containment) and continuous enforcement; managed analyst (MDR) layers.
- **AI-assistant layer** — vendor AI assistants spanning search/investigation workflows (Sysdig Sage; Prisma Copilot; era-common).
- **Program-management surfaces** — adoption/maturity centers, workflow orchestration canvases, governance rule engines.

### L3 — Vendor-specific (Research Notes only)

- Defender: Foundational CSPM (free) vs Defender CSPM (paid) plan split; per-workload plan family (Servers P1/P2, Containers, Storage, Databases, Key Vault, App Service, Resource Manager, APIs, AI Services); Microsoft Cloud Security Benchmark (MCSB); cloud security explorer / governance rules naming; Azure Arc hybrid onboarding; Defender XDR portal convergence; Foundational CSPM moving to opt-in for new subscriptions (announced for late 2026).
- Prisma Cloud: "Defender" agent family (container/host/orchestrator/serverless/app-embedded); RQL; Code-to-Cloud Dashboard; Command Center; Collections & Account Groups; Enterprise vs Compute Editions; self-hosted Console; Okta/IdP CIEM integrations; Cortex XSOAR/SIEM integration family.
- Sysdig: Falco heritage and Falco rule libraries; SysQL; Zones/Teams; Cloud Shield/CloudConnector; "In Use" vulnerability prioritization; Risk Definitions/Risk Exceptions; Rapid Response; on-premises deployment; Sysdig Sage; Secure vs Monitor sibling products.
- Wiz: Security Graph; "toxic combinations"; Wiz Sensor; Wiz Defend/Wiz Code/Wiz Cloud product names; Champion Center; WIN integration platform; AI-APP positioning; 65%-of-Fortune-100 marketing claim (unverified, marketing).
- FortiCNAPP: Lacework heritage; Polygraph (heritage, prior research notes); LQL; Fortinet portfolio placement alongside FortiDevSec.

## Vendor-specific Findings → Rejected for Canonical Core

- Plan/edition entitlement mechanics (Defender's plan table, Prisma's editions) — packaging, not structure.
- Any specific correlation-graph implementation (Security Graph vs Polygraph vs Cloud Attack Graph) — the *capability* (cross-domain correlation) is L1; the graph is its mature implementation.
- Specific query-language names and capabilities.
- Agentless-only or sensor-only posture — contradicted across the sample; neither is definitional.
- AI assistant, workflow orchestration, adoption centers — era-current features, L2.

## Boundary Findings

**vs CSPM** (sibling leaf): CSPM's defining core is configuration-state evaluation producing posture findings. A CNAPP necessarily *contains* posture evaluation, but adds: workload runtime domain, unified cross-domain inventory, correlation. Test: remove all non-posture domains → what remains is a CSPM. Remove posture → not a CNAPP either. CNAPP's differentiator is the unification, not the posture logic.

**vs CWPP** (sibling leaf): CWPP's core is runtime visibility + detection + response on workloads. CNAPP contains it as a pillar. Test: remove posture/identity/vulnerability-portfolio context and the unified inventory → a CWPP.

**vs CIEM / DSPM / KSPM / API-SPM**: each is a single-domain posture/analysis type; in the market they appear most often as modules *inside* CNAPPs. Their standalone existence does not contradict CNAPP; CNAPP is their unifier.

**vs "security suite" / portfolio**: a vendor selling a CSPM and a CWPP as separate products with separate consoles, inventories and policy engines is a portfolio, not a CNAPP. The structural test for CNAPP: **one shared estate inventory + one risk picture**. When a suite vendor unifies consoles/data models, the portfolio becomes a CNAPP; the market language follows that unification. (Recorded as a boundary issue in STATUS.md.)

**vs Vulnerability Management**: enterprise VM programs span all assets and own remediation workflow; CNAPP vulnerability management is the cloud-native estate slice inside the platform, prioritized by cloud context.

**vs SIEM/SOAR**: SIEM correlates event streams for detection; CNAPP evaluates security state of the cloud estate and forwards findings/events downstream. CNAPP's runtime pillar *executes* response on workloads (containment), which SIEM does not.

**vs Cloud Management Platform / CSP (finops, provisioning)**: same inventory surface, opposite purpose — operate/optimize vs secure.

**vs XDR/EDR**: EDR/XDR converge on endpoint telemetry; CNAPP converges on the cloud-native estate (resources + workloads + identities + data). Machinery overlaps (detection→triage→respond); object domain and estate differ. Defender for Cloud sits in both ecosystems (XDR portal convergence) — a convergence seam, not an identity.

**"去掉什么就变成另一个 Type" 判据**：去掉多领域（只剩配置评估）→ CSPM；只剩运行时防御 → CWPP；去掉统一清单/单一风险面（各自独立控制台）→ 产品组合而非 CNAPP；去掉云（对象域变成终端）→ EDR/XDR 家族。

## §24 Historical / Market-Sample Check

- The "CNAPP" label is recent (analyst-coined category; vendors self-apply it — Defender and Sysdig self-describe as CNAPP in current docs; Forrester runs a "Cloud Native Application Protection Solutions" evaluation). Did integrated multi-domain cloud security platforms exist **before** the term? Yes: Lacework (agentless posture + polygraph correlation + runtime, mid-2010s heritage), Redlock (multi-cloud posture+workload, became Prisma), Dome9, platform-native security centers (Azure Security Center → Defender for Cloud; AWS Security Hub + GuardDuty + Inspector families). These pre-label products combine posture + runtime + vulnerability + identity on shared infrastructure — they fit the L0 above. The definition is therefore not overfit to the 2021+ packaging wave.
- Would a *provider-native minimal security center* (config assessment + workload alerts on one inventory) fit? Yes — that is the platform-native variant; it holds ≥2 domains on one inventory. It is recognizable as the same platform structure in smaller form.
- Would a modern agentless product **without** runtime sensors fit? Yes under this L0 (multi-domain, unified inventory, one risk picture) — consistent with the market's acceptance of agentless-first CNAPPs whose runtime capability is achieved through cloud telemetry/snapshot rather than deployed sensors, or added later as a pillar. Requiring "runtime sensor" in L0 would wrongly exclude them; requiring "runtime threats" as one of the ≥2 domains would also overfit — hence the L0 formulation "posture + at least one other domain (vulnerabilities / runtime threats / identity entitlements)".
- Regional/self-hosted deployments (Prisma/Sysdig on-prem; sovereign clouds in Defender) fit the same core.

## Uncertainties

1. **CIEM as near-universal**: identity-entitlement analytics documented directly for Prisma/Sysdig (and for Defender via prior same-day research + CSPM-plan feature lists); for Wiz evidenced only at positioning level ("identity" as graph context). Sample suggests CIEM is a standard CNAPP domain, but the reachable evidence is 3-of-5 direct → stated as "mature products commonly include", not definitional.
2. **Whether the correlation graph is definitional or common-mature**: resolved as L1 (common mature) with L0 holding the weaker "single risk picture" — but the market increasingly treats attack-path correlation as the CNAPP value proposition. Future re-review may justify promoting it; current evidence (and the historical check: pre-graph integrated platforms) supports keeping it at L1.
3. **FortiCNAPP operational mechanics**: structure-level evidence only; nothing asserted about it beyond guide-set existence and heritage naming.
4. **Taxonomy status**: CNAPP vs CSPM leaf overlap is real (many "CSPM" product pages describe CNAPP platforms). This atlas keeps both leaves: CSPM = configuration-posture type; CNAPP = platform type whose core is the unification of pillar types. Recorded in STATUS.md Boundary Issues for editorial review.
5. **Exact domain count per product** varies by edition/plan; no attempt to enumerate per product in the final document.

## Final Synthesis

CNAPP is the platform-level application type of cloud-native security. Its defining core is not any single security behavior but the **unification**: a standing connection into the customer's cloud estate; one inventory spanning resource configuration and running workloads (plus identities, data, APIs, code in mature products); continuous evaluation of multiple security domains against that shared inventory; and one risk picture — correlated, prioritized, and operated — in a single platform with a shared policy/query/integration/administration plane. Posture evaluation (CSPM), workload protection (CWPP), vulnerability management, and identity-entitlement analytics are the standard pillars; data/API/AI posture extend the domain set in mature products. Cross-domain correlation (security graphs, attack paths) is the signature capability the market currently expects, built on top of the unification rather than defining it. The boundary test is structural: remove a pillar and a single-domain tool remains; remove the unification and a portfolio of point tools remains; only the unified multi-domain platform on one shared estate data model is a CNAPP.
