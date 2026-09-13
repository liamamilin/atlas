# Research Notes — SaaS Security Posture Management / SSPM

Research date: 2026-09-09

## Research Goal

Understand, from real products, what a SaaS Security Posture Management (SSPM) application actually is as a Type: its defining structure, its canonical workflow loop, who operates it, what it assesses, and how it is distinguished from the crowded posture/security neighborhood (CSPM, DSPM, CASB/SSE, SaaS Management, IAM/IGA, Vulnerability Management, Security Compliance Platform, ITDR).

This pass also discharges three counterparty notes left by processed sibling passes:

- **cloud-security-posture-management-cspm** (§14): "Object domain: SaaS tenant configuration vs cloud infrastructure resources. Swap cloud-account connectors for SaaS-app connectors → SSPM."
- **data-security-posture-management-dspm** (§15): "Assessed object test: tenant configuration of a SaaS app vs the data it holds. Recommend the future SSPM pass adopt the same 'assessed object' discriminator."
- **saas-management** (§14): "Expected seam = SSPM governs security posture of sanctioned SaaS (misconfigurations, OAuth risk, data exposure) vs SaaS Management governs the estate's commercial/operational lifecycle (spend, seats, renewals, access); drift zone runs both directions."

## Initial Boundary

- **What it likely is:** a security-side management application that connects to an organization's SaaS applications, continuously assesses their security-relevant configuration (and, in mature products, their identity/integration/data-sharing surface), produces prioritized findings, and drives remediation.
- **Primary users:** security team (analysts, engineers), security/IT admins; app owners pulled into remediation; CISO-level reporting.
- **Nearest neighbors:** CSPM (cloud infra config), DSPM (data content inside stores), CASB/SSE (inline session enforcement + network-based discovery), SaaS Management (commercial estate), IAM/IGA (identity lifecycle), Vulnerability Management (CVEs), Security Compliance Platform (audit/controls), ITSM (remediation ticketing), ITDR (identity threats).
- **Likely confusions:** SSPM vs CASB (historically entangled — many SSPM products grew out of CASB vendors); SSPM vs SaaS Management (same estate, different object); SSPM vs CSPM/DSPM (the "posture" family).
- **Unknowns at start:** how discovery of shadow SaaS relates to the posture core; how deep remediation goes (auto vs guided); whether identity/NHI assessment is definitional or an extension; whether SSPM is standalone or always a module.

## Research Questions

1. What does an SSPM connect to, and how (API connectors, credentials, scopes, other vantage points)?
2. What is the core object model: connected app/instance, security expectation (benchmark/policy/baseline), finding, remediation action?
3. What domains does it assess: tenant configuration, identity posture, OAuth/third-party integrations, data-sharing exposure, devices, threats?
4. How does the assess → find → prioritize → remediate → verify loop work? Where is it automated vs human?
5. How does SaaS discovery (sanctioned/shadow) relate to the posture core — definitional or adjacent?
6. What interfaces exist: posture dashboard/score, app inventory, findings queue, per-app posture page, policy library, integrations?
7. What rules matter: least-privilege connection credentials, per-app capability variance, drift detection, severity/context enrichment?
8. Where are the seams vs CSPM / DSPM / CASB-SSE / SaaS Management / IAM / VM / compliance?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Philosophy | Tier |
|---|---|---|
| CrowdStrike Falcon Shield (ex-Adaptive Shield) | posture-benchmark pure-play, absorbed into a platform vendor; enterprise | Tier 2 (product page; docs portal JS-gated) |
| Microsoft Defender for Cloud Apps | suite module (CASB + SSPM + XDR) with explicit per-app SSPM capability matrix | Tier 1 (official docs) |
| Nudge Security | discovery-first "modern SSPM"; perimeterless multi-vantage discovery; human-in-the-loop remediation; mid-market | Tier 1 (KB) + Tier 2 (product pages) |
| Valence Security | remediation-workflow-first; drift detection; compliance mapping | Tier 2 (product pages) |

Rejected from sample: **Wing Security** — has pivoted to "With Wings / Agent Exposure Management" (AI-agent authority management); no longer a representative SSPM product. Recorded as market-drift evidence, not sampled.

## Sources

- Microsoft Learn — Defender for Cloud Apps overview: https://learn.microsoft.com/en-us/defender-cloud-apps/what-is-defender-for-cloud-apps (fetched 2026-09-09)
- Microsoft Learn — Connect apps with API connectors (incl. per-app SSPM capability table): https://learn.microsoft.com/en-us/defender-cloud-apps/enable-instant-visibility-protection-and-governance-actions-for-your-apps (fetched 2026-09-09)
- CrowdStrike — Falcon Shield product page (Adaptive Shield now redirects here): https://www.adaptive-shield.com/ → https://www.crowdstrike.com/en-us/platform/falcon-shield/ (fetched 2026-09-09)
- Nudge Security — root, SSPM use-case page: https://www.nudgesecurity.com/ , https://www.nudgesecurity.com/use-cases/saas-security-posture-management (fetched 2026-09-09)
- Nudge Security Support Center (KB): https://help.nudgesecurity.com/en/ ; Integrations collection; "Configure the Okta Connected App" article (fetched 2026-09-09)
- Valence Security — root and SSPM platform page: https://www.valencesecurity.com/ , https://www.valencesecurity.com/platform/saas-security-posture-management (fetched 2026-09-09)
- With Wings (ex-Wing Security) — pivot evidence: https://www.wing.security/ (fetched 2026-09-09)

**Source-access limitations:**

- docs.crowdstrike.com requires JavaScript; Falcon Shield operational documentation not reachable. Falcon Shield evidence is Tier-2 (official product page) only; precise operational claims for this product are avoided.
- Microsoft SSPM-specific tutorial URLs (/defender-cloud-apps/sspm, /tutorial-sspm, /security-configuration-management, /security-recommendations) returned 404; abandoned after repeated misses per network rule. Microsoft evidence rests on the two successfully fetched Tier-1 pages.
- No vendor pricing, check-list contents, or numeric SLA details were researched; none are claimed.

## Product Observations

### Microsoft Defender for Cloud Apps (Tier 1)

Key observations [A = directly observed in official docs]:

- SSPM is a **named feature pillar**: "SaaS Security Posture Management (SSPM) features, enabling security teams to improve the organization's security posture." The product's four pillars: CASB, SSPM, advanced threat protection (XDR), app-to-app protection (OAuth app governance). [A]
- SSPM mechanics: "surfacing misconfigurations and recommending specific actions to strengthen the security posture for each **connected app**. Recommendations are based on industry standards like the **Center for Internet Security** and follow best practices set by the specific app provider." [A]
- SSPM output flows into **Microsoft Secure Score** "for any supported and connected app." [A]
- **Connection model**: "App connectors use the APIs of app providers"; the product is "deployed with system admin privileges to allow full access to all objects"; scan flow = authentication permissions → user list → activities/files, then periodic scans. [A]
- **Per-connector capability variance is explicit**: capability tables per app (account info, audit trail, account governance, app permissions, app-permission governance, data scan, data governance) — "not all app connectors support all abilities." [A]
- **SSPM is a per-connected-app capability column**: the table "User, app governance, and security configuration visibility" has an explicit "SaaS Security Posture Management (SSPM)" column, ✔ for Atlassian, Citrix ShareFile, DocuSign, Dropbox, GitHub, Google Workspace, Microsoft 365, Okta, ServiceNow, Salesforce, Zendesk; Preview for NetDocuments, Workplace by Meta, Zoom; blank for others. [A]
- **Multi-instance support**: two instances of the same app (e.g., two Salesforce tenants) can be connected and managed separately. [A]
- **Three app states**: API connected apps, Cloud Discovered apps, Proxy connected apps — posture work happens on API-connected apps; discovery is a separate CASB mechanism (network traffic + app catalog, 90+ risk indicators). [A]
- **OAuth app governance** is a separate pillar: "OAuth apps often behave unnoticed, while still having extensive permissions to access data in other apps on behalf of an employee… Watch for unused apps and monitor both current and expired credentials." [A]
- Governance actions on connected apps: suspend users, revoke passwords, remove tokens, quarantine files. [A]

### CrowdStrike Falcon Shield (ex-Adaptive Shield) (Tier 2)

- Self-positioning: "Gain full visibility and control into **misconfigurations, identities, and threats** targeting your SaaS applications." [A]
- Scale claims: "3,500+ unique application hardening and configuration checks"; "200+ integrated SaaS apps out of the box"; "Monitor SaaS applications in minutes — instantly connect your SaaS apps to uncover misconfigurations, enforce governance." [A]
- "Discover connected and shadow applications." [A]
- "Proactive threat detection and response — real-time alerts and automated responses to suspicious user behavior, login anomalies, and device issues." [A]
- Identity posture: "find and secure human and non-human identities (NHI) that are over-permissioned, high risk, dormant, or partially deprovisioned… visibility into all SaaS apps in use, including sanctioned, unsanctioned, and those connected to your core SaaS stack." [A]
- Custom checks: "use over 3,500 built-in security checks and easily create custom Security Checks to detect misconfigurations." [A]
- AI-agent discovery across SaaS platforms (Microsoft 365, Salesforce, OpenAI): "Map their system access, detect risky behavior." [A]
- Category validation: "Named the Leader in 2025 Frost Radar for SSPM" and "2025 GigaOm Radar for SSPM — Only Leader & Outperformer." SSPM is an externally validated analyst category. [A]
- Market fact: adaptive-shield.com now serves CrowdStrike Falcon Shield — the SSPM pure-play pioneer was absorbed into a platform vendor. [A]
- Limitation: operational docs unreachable (JS-gated); no precise workflow claims made for this product.

### Nudge Security (Tier 1 KB + Tier 2)

- Self-label: "SaaS & AI Security Platform | SSPM Solution"; platform pillar: "SaaS security posture management — Detect misconfigurations, identity risks, and more across business-critical apps." [A]
- Vendor's own Type definition (FAQ): "SSPM is the practice of continuously monitoring, assessing, and improving the security posture of an organization's SaaS applications. While early SSPM tools focused primarily on configuration checks for a small set of known apps, modern SSPM must account for how SaaS is actually used today — including identities, integrations, non-human access, and data flowing through SaaS and AI tools." [A]
- Canonical 4-step workflow on the SSPM page: **Discover → Detect → Prioritize → Remediate**. [A]
- Discover: "perimeterless discovery" via "multiple vantage points (workspace provider, browser, and connected apps)"; managed and shadow apps; app instances and associated accounts; continuously updated inventory; "no agents or pre-built integrations required." [A]
- Detect: "posture risks for over 200,000+ SaaS and AI tools, **with or without an API integration**"; identity risks (unused, shared, weakly protected accounts); "OAuth grants, API keys, AI agents, service accounts, and other non-human identities"; "risky app-to-app integrations, MCP servers"; vendor risk signals and supply chain exposures. [A]
- Prioritize: findings enriched with "approved app list, business criticality, data sensitivity, app owners, vendor breach records." [A]
- Remediate: "combining automation with human-in-the-loop workflows"; "Route issues to the right app owners, admins, or users"; "step-by-step remediation guidance"; "Verify remediation actions to ensure closure"; "last-mile remediation." [A]
- **Security Nudges**: behavior-change mechanism — notifications to employees/admins to fix issues ("Some of these people don't respond to emails or tickets, but they responded to the damn nudge!" — customer quote). Playbooks automate nudges. [A]
- KB (Tier 1) operational detail:
  - Connected app = API integration configured with a **least-privilege read-only service identity + API token** (Okta article walks through creating a custom read-only role, a dedicated user, and a token, then pasting domain+token into Settings → Integrations and "Verify Connection"). [A]
  - **IdP-based discovery**: "Configure Okta SSO Analysis… to analyze apps using Okta SSO and apps to onboard to Okta SSO." [A]
  - **Chat-tool integrations** (Slack, Teams) for nudge delivery; **ticketing integrations** (Jira, ServiceNow): "Route security findings straight into Jira… create a Jira ticket from any finding… keep both systems in sync." [A]
  - Browser extension as a discovery vantage point (13-article collection). [A]
  - Public API. [A]
- FAQ boundary statements: SSPM↔IAM relationship ("Nudge Security connects SSPM insights directly to identities… enforce least privilege, clean up stale access"); shadow SaaS as "a foundational SSPM challenge, because you can't secure what you can't see"; compliance support via continuously updated inventory + remediation records as audit evidence. [A]
- Nudge explicitly positions against: legacy SSPM (API-integration-first), CASB (network-based discovery blind spots), browser-centric security, and SMP ("Nudge vs. SMP — insights into SaaS use, spend, and risk all in one place"). One product deliberately spans both SSPM and SaaS Management use cases — the drift zone the SaaS Management pass predicted. [A]

### Valence Security (Tier 2)

- Platform modules: SaaS and AI Discovery; **SSPM** ("Identify and prioritize risk across SaaS applications"); AI Security Posture Management (AI-SPM); SaaS and AI Risk Remediation; ITDR. [A]
- SSPM page: "centralizes SaaS and AI security by **continuously monitoring configurations, permissions, and integrations across all connected applications**. The platform identifies **misconfigurations, policy gaps, and configuration drift**, presenting clear priorities and actionable remediation paths. It also validates alignment with industry best practices and regulatory frameworks." [A]
- FAQ definition: "SSPM is a security practice that continuously monitors SaaS applications for misconfigurations and compliance gaps. It ensures SaaS apps remain aligned with organizational security policies." [A]
- Drift: "early detection of configuration drift"; baseline enforcement via "collaboration with SaaS admins." [A]
- Remediation depth: "flexible options ranging from **one-click remediation to automated workflows**"; "collaboration features that engage users and admins to gain necessary business context"; one-click/automated remediation of "overly permissive sharing links." [A]
- Compliance mapping: "supports SOC 2, ISO 27001, HIPAA, and dozens of other compliance and best practice frameworks by automatically flagging SaaS misconfigurations that could lead to compliance violations." [A]
- Scale: "Over 175 Supported SaaS and AI Applications." [A]
- Use cases: manage configurations, comply with standards, strengthen identity security, secure AI agents, govern non-human identities, reduce data exposure, detect and respond to threats. [A]

### Market-drift observations (context, not sampled products)

- **Consolidation**: Adaptive Shield (the SSPM category pioneer) absorbed into CrowdStrike Falcon Shield. [A]
- **Pivot**: Wing Security → "With Wings," repositioned entirely to AI-agent exposure management. [A]
- **AI-era expansion**: Nudge and Valence both ship sibling "AI Security Posture Management" modules; Falcon Shield ships AI-agent discovery; Nudge detects "MCP servers and other emerging AI connections." [A]
- **Category span**: Nudge sells both SSPM and SaaS Management use cases from one platform — confirming the two Types share the estate but split on object (security posture vs commercial lifecycle). [A]

## Cross-product Comparison

| Dimension | Falcon Shield (ex-Adaptive Shield) | Defender for Cloud Apps | Nudge Security | Valence Security |
|---|---|---|---|---|
| Self-label | SSPM (Frost/GigaOm radar leader) | SSPM as named pillar of a CASB/XDR suite | "SSPM Solution" (discovery-first) | SSPM platform module |
| Connection substrate | 200+ integrated apps (API) | API connectors per app; admin privileges | API connected apps + IdP + browser extension (multi-vantage) | 175+ supported apps (API) |
| Assessed object | misconfigurations + identities (human/NHI) + threats | security configuration per connected app (explicit SSPM column) | misconfigurations + identity hygiene + OAuth/NHI + vendor risk | configurations + permissions + integrations + drift |
| Expectation source | 3,500+ built-in checks + custom checks | CIS benchmarks + provider best practices | posture checks (count not stated) | best practices + SOC 2/ISO/HIPAA frameworks |
| Findings form | alerts, prioritized | recommendations → Secure Score | context-enriched findings | prioritized misconfigurations + compliance gaps |
| Remediation | automated responses | governance actions (suspend/revoke/quarantine) | human-in-the-loop nudges + playbooks + verification | one-click → automated workflows + collaboration |
| Shadow-SaaS discovery | yes ("connected and shadow applications") | yes, via CASB cloud discovery (separate mechanism) | yes, central (perimeterless, multi-vantage) | yes (SaaS and AI Discovery module) |
| Score/report | not stated | Microsoft Secure Score | posture dashboard | not stated |
| Drift detection | not stated on fetched page | not stated on fetched pages | continuous monitoring implied | explicit ("configuration drift") |
| Ticketing/chat handoff | not stated | not stated on fetched pages | Jira, ServiceNow, Slack, Teams | collaboration features (not named) |
| Identity posture | human + NHI, dormant/over-permissioned | account governance actions | unused/shared/weakly protected accounts; NHIs | identity security use case |
| AI-era extension | AI-agent discovery | app-to-app OAuth protection | AI agents, MCP servers, AI-SPM sibling | AI-SPM sibling module |

**Reading of the comparison:** every product connects to SaaS apps, continuously evaluates their security state against defined expectations, produces prioritized findings, and drives remediation to closure. Everything else varies: discovery method and centrality, identity/NHI depth, threat detection, compliance mapping, remediation automation depth, score mechanics. The stable joint structure is the posture loop over a connected SaaS estate.

## Canonical Model

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **The connected SaaS application estate as the assessed inventory of record.** Persistent per-app (and per-instance) records of the organization's SaaS applications under assessment, established through connections to those apps — API connectors with granted credentials being the dominant implementation, other vantage points (IdP logs, browser) appearing in some products. Remove → a benchmark checklist or audit template with nothing under assessment.
2. **Continuous security-configuration assessment producing findings.** The system evaluates each connected app's security-relevant configuration — tenant settings, and in mature products the identity, integration (OAuth/third-party), and data-sharing surface those settings expose — against defined security expectations (industry benchmarks, vendor best practices, baselines, custom policies), on a recurring basis, recording results as findings with severity. Remove → an app inventory or activity monitor with no security judgment.
3. **The remediation loop on findings.** Each finding carries a recommended action and a path to resolution — manual guidance, guided workflow, one-click fix, or automated remediation — routed to an owner and tracked to verified closure. Remove → a scanner/report generator; the "management" is gone.

Jointly-held load-bearing test:

- 1 alone = SaaS app inventory (SaaS Management / CMDB-adjacent).
- 2 without 1 = generic policy checker / one-off audit.
- 3 without 1+2 = ticketing with nothing to fix.
- 1+2 without 3 = assessment reporting (audit artifact, not management).
- 2+3 without 1 = point checks with no estate view.
- 1+3 without 2 = inventory with a fix queue but no security evaluation.

**Assessed-object discriminator (adopted per DSPM pass):** the object SSPM assesses is the **SaaS tenant's security configuration** — the application's settings and the access/integration surface they govern — not the data content held in the app (DSPM), not cloud infrastructure resources (CSPM), not the commercial facts of the subscription (SaaS Management).

**Historical / market-sample check:** the earliest SSPM generation (configuration checks over a small set of known apps via API, CIS-benchmark findings, remediation recommendations — the pattern Nudge's FAQ explicitly calls "early SSPM tools") satisfies all three legs with no shadow discovery, no NHI, no AI, no score. A manual CIS-benchmark tenant audit is the paper-era lineage: it has assessment + findings + remediation guidance but lacks the connected recurring loop — it is the ancestry, not the Type. The definition does not depend on any current-era implementation (multi-vantage discovery, NHI, AI agents).

### L1 — Common Mature Structure

- Benchmark/baseline libraries (CIS-family and provider best practices) and compliance-framework mapping (SOC 2, ISO 27001, HIPAA observed).
- Posture score / secure score aggregating findings (Microsoft Secure Score; posture dashboards elsewhere).
- OAuth / third-party app (app-to-app) governance: inventory of granted integrations, permission visibility, revocation.
- Identity posture inside apps: MFA/SSO coverage, dormant/shared/weakly protected accounts, over-privileged users, service accounts and other non-human identities.
- Data-sharing exposure findings (e.g., overly permissive sharing links, external collaborators).
- Configuration drift detection against baselines.
- Remediation automation spectrum: guidance → one-click → automated playbooks; verification of closure.
- Integration ecosystem: IdP/SSO connections, ticketing (Jira/ServiceNow), chat (Slack/Teams), API/SIEM export.
- Executive/compliance reporting and audit evidence from the posture record.

### L2 — Variant / Optional Structure

- **Shadow-SaaS discovery** — presence and method vary widely: network-traffic + catalog (CASB-style), IdP-log analysis, browser extension, email-security telemetry; some products make it central (Nudge), others treat it as a separate CASB mechanism (Microsoft) or a module (Valence). Not definitional: Microsoft's SSPM column operates on connected apps regardless.
- **Threat detection / ITDR on SaaS** — UEBA, anomalous logins, session/device anomalies (Falcon Shield, Valence ITDR, Defender XDR). A different discipline bolted onto the same estate.
- **Remediation automation depth** — from advisory-only to fully automated playbooks; product philosophy axis.
- **Depth-vs-breadth axis** — deep checks on core business apps (Microsoft's per-app capability matrix; Falcon Shield's 200+ apps with 3,500+ checks) vs breadth-first posture signals across very large app universes without API integration (Nudge's 200,000+).
- **AI-era extensions** — AI-agent discovery, AI-SPM siblings, MCP-connection monitoring. Emerging, not yet stabilizing into the Type's core.
- **Packaging** — standalone pure-play, suite module (CASB/XDR platform), or platform pillar; market currently consolidating toward platforms.

### L3 — Vendor-specific Structure (Research Notes only)

- Microsoft Secure Score as the aggregation surface; per-app SSPM capability matrix with Preview states; multi-instance connector support.
- Nudge "Security Nudges" behavior-change mechanism; "perimeterless discovery" branding; Okta SSO Analysis as a named discovery method.
- Falcon Shield's "3,500+ checks / 200+ apps" figures; custom Security Checks; AI-agent discovery across named platforms.
- Valence AI-SPM module naming; "one-click remediation" of sharing links as a marketed capability.
- Numeric claims (90+ risk indicators, 70 average OAuth grants per employee, etc.) — vendor marketing figures, not Type structure.

## Vendor-specific Findings

- Microsoft: SSPM recommendations feed Microsoft Secure Score; SSPM availability is explicitly per-connector (some apps Preview, some unsupported) — direct evidence that SSPM capability is bounded by what each provider's API exposes.
- Nudge: remediation is deliberately human-in-the-loop ("last-mile remediation") because "API automation falls short" for apps without integrations — a philosophy contrast with auto-remediation-first products.
- Valence: drift detection and baseline enforcement via security↔admin collaboration is the marketed differentiator.
- Falcon Shield: identity-threat and AI-agent layers sit beside the posture core; custom check authorship is exposed to customers.

## Boundary Findings

| Neighbor | Discriminator | Remove-test |
|---|---|---|
| **CSPM** | Assessed object: SaaS tenant configuration vs cloud infrastructure resources. Counterparty seam RATIFIED: swap SaaS-app connectors for cloud-account connectors → CSPM; swap back → SSPM. | Remove the SaaS-tenant object domain, assess cloud resources → CSPM. |
| **DSPM** | Assessed object: tenant configuration vs data content held in stores. Counterparty discriminator adopted. | Assess data sensitivity/classification/exposure of stored content → DSPM. |
| **CASB / SSE (SASE/SSE leaf)** | Control plane: API/config-plane assessment vs inline session enforcement (proxy). Shadow-SaaS discovery is the overlap zone. No separate CASB leaf in the directory; CASB capability lives under SASE/SSE Platform. | Move enforcement inline into proxied sessions → CASB/SSE territory. |
| **SaaS Management** | Object: security posture vs commercial/operational lifecycle (spend, seats, renewals, access). Counterparty seam RATIFIED. Drift zone both directions: Nudge sells both use cases; discovery feeds shared; SMPs add file-governance/security extensions. | Track spend/seats/renewals instead of security state → SaaS Management. |
| **IAM / IGA** | SSPM assesses identity posture *within* SaaS tenants and reports; IAM/IGA owns the identity lifecycle and access decisions themselves. | Start provisioning/deprovisioning identities and certifying access → IAM/IGA. |
| **Vulnerability Management** | Findings are misconfigurations/posture gaps, not software CVEs with CVSS on owned assets. | Findings become CVEs against software inventory → VM. |
| **Security Compliance Platform** | Compliance mapping is a capability of SSPM (findings mapped to frameworks), not an audit/controls-management system of record. | The system of record becomes controls/audits/evidence across the org → Security Compliance Platform. |
| **ITSM** | SSPM hands findings to ticketing (Jira/ServiceNow integrations observed); it does not own ticket workflows. | The finding becomes a generic ticket with no security-posture semantics → ITSM. |
| **ITDR** | Threat detection/response on identities is an optional layer some SSPM products add; the posture loop remains the core. | Primary object becomes live identity-threat detection and response → ITDR. |

**"去掉什么就变成另一个 Type" summary:** remove the SaaS-tenant assessed object → CSPM (infra) or DSPM (data); remove the security judgment → SaaS Management or app inventory; remove the connected recurring loop → one-off audit/compliance assessment; remove the remediation loop → monitoring/scanning; move enforcement inline → CASB/SSE.

## Uncertainties

- **Falcon Shield operational detail** unreachable (JS-gated docs); its workflow specifics (connector setup, check taxonomy, remediation mechanics) are unverified — only product-page claims recorded.
- **Exact check/benchmark taxonomies** (which CIS versions, which settings per app) not researched; no numeric check counts claimed beyond vendor-stated figures.
- **Score mechanics** (how posture scores are computed) not researched for any product beyond Microsoft's Secure Score linkage.
- **Discovery-method mix per product** partially observed (Nudge multi-vantage documented; Falcon Shield/Valence discovery mechanics not detailed on fetched pages).
- Whether the market will stabilize "AI-SPM" as a sibling Type or fold it into SSPM — left open; recorded as drift, not resolved.
- CASB has no directory leaf of its own (folded under SASE/SSE Platform); this pass documents the seam but does not propose taxonomy changes.

## Final Synthesis

SSPM is the security team's management loop over the security posture of its SaaS application estate. The defining core is three jointly-held structures: (1) the connected SaaS app estate as the assessed inventory of record — persistent per-app/per-instance records established through connections (API connectors dominant, other vantage points variant); (2) continuous security-configuration assessment — evaluating each connected app's tenant configuration (and, in mature products, its identity, integration, and data-sharing surface) against defined security expectations (benchmarks, baselines, policies), producing severity-bearing findings; (3) the remediation loop — every finding carries a recommended action and a resolution path (guidance, one-click, automated), routed to an owner and tracked to verified closure. The assessed object is the SaaS tenant's security configuration — the discriminator separating SSPM from CSPM (infrastructure), DSPM (data content), and SaaS Management (commercial lifecycle). Shadow-SaaS discovery, identity/NHI depth, threat detection, compliance mapping, score mechanics, and remediation-automation depth are common mature structure or variant axes, not definition. The Type is externally validated (analyst SSPM radars), currently consolidating into platform vendors and expanding toward AI-agent security — both drift phenomena, not Type changes.
