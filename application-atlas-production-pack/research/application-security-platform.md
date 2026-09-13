# Research Notes — Application Security Platform

Research date: 2026-09-06

## Research Goal

Understand what "Application Security Platform" (directory leaf, §15 Cybersecurity, Identity & Trust) means as an Application Type: what the system's world is made of, who uses it, how security work flows through it, and — critically — how it differs from the adjacent engine leaves in the same directory section (SAST, DAST / IAST, SCA, Software Supply Chain Security, SBOM Management, Secrets Security, API Security Platform) and from Vulnerability Management.

## Initial Boundary

Initial hypothesis (pre-research):

- The object of protection is the organization's **own applications** — their code, third-party components, APIs, containers, and runtime behavior — across the development lifecycle.
- The platform is the **application-centric management layer**: it holds application records, attaches security findings to them, and manages a remediation lifecycle. Analysis engines (SAST/SCA/DAST/IAST/secrets/container) are the *means*, not the definition.
- Nearest neighbors that must be separated: engine leaves (analysis capability), Vulnerability Management (infrastructure object domain), API Security Platform (API runtime center of gravity), WAF (real-time edge protection), GRC/Security Compliance (consumes outputs, doesn't manage findings).
- Risk observed up front: the term "Application Security Platform" is also used loosely as a marketing umbrella; and "Application Security Posture Management (ASPM)" names an aggregation-first variant of the same layer.

## Research Questions

1. What is the unit of record? (application vs project/repo vs component)
2. How do findings come into existence? (built-in engines, external/imported results, both?)
3. What is the finding lifecycle? (states, triage decisions, auto-fix detection, reopening)
4. Who are the users and what roles exist? (AppSec team, developers, managers, admins)
5. What surfaces exist? (portfolio view, finding detail, developer surfaces: PR/IDE/CLI/CI gates, dashboards, policy management, admin)
6. What rules govern behavior? (policy gates, scan reconciliation/dedup, severity/risk scoring, RBAC)
7. Where is the boundary with engine leaves, Vulnerability Management, API Security, WAF, supply-chain leaves, GRC?
8. Historical/market-sample check: would older or differently positioned application-security products (on-prem results centers, scanner-portal products) still fit the definition?

## Representative Products

Chosen for market representation, documentation quality, and deliberately different product philosophies:

| Product | Philosophy / position | Segment |
|---|---|---|
| Veracode Platform | Enterprise program suite; application portfolio + policy + ratings; oldest continuous lineage (mid-2000s SaaS AppSec) | enterprise |
| Checkmarx One | Scanner-suite-grown multi-engine platform with explicit ASPM layer and BYOR import | enterprise |
| Snyk | Developer-first; developer tools (CLI/IDE/SCM/CI) as first-class surfaces | developer / mid-market-to-enterprise |
| Semgrep AppSec Platform | Engine-led modern platform (SAST engine + rules-as-code expanding to SCA/secrets) | developer / modern eng orgs |
| Contrast Security | Runtime-instrumentation philosophy (agents in the running app); includes runtime defense | enterprise (hosted + on-prem) |

## Sources

All fetched 2026-09-06. Evidence layer A (directly observed) unless noted.

- Veracode — https://docs.veracode.com/ (docs home), https://docs.veracode.com/r/review_main (Manage risk), https://docs.veracode.com/r/Getting_Started_with_Veracode_Products
- Checkmarx — https://docs.checkmarx.com/ (documentation portal), https://docs.checkmarx.com/en/34965-68517-checkmarx-one-user-guide.html (Checkmarx One User Guide TOC)
- Snyk — https://docs.snyk.io/ (docs home + GitBook `ask` query over official docs; cited pages: Snyk Projects, Understand your issues, Navigate the Snyk Web UI, Pre-defined roles)
- Semgrep — https://semgrep.dev/docs/ (docs home), https://docs.semgrep.dev/semgrep-code/triage-remediation (Triage and remediate findings)
- Contrast Security — https://docs.contrastsecurity.com/ (docs home), https://docs.contrastsecurity.com/en/welcome-to-contrast.html (positioning + interface structure only)

Sourcing limitation: Contrast was observed at positioning/structure level only (its welcome page and docs index); no lifecycle or policy detail pages were fetched. Contrast-based claims below are kept at that strength. Historical products (HP Fortify SSC-class on-prem results centers, IBM AppScan, WhiteHat/Qualys WAS-class web-app scanning portals) were not fetched; the historical check is reasoning-level (layer C).

## Product A — Veracode Platform

### Key observations (layer A)

- Docs home describes the Veracode Platform as "the central hub for managing your application security program, including administration, security testing, and scan results."
- **Application inventory / portfolio**: the documented ARM ("Application Risk Management") methodology starts with creating a portfolio of applications "being developed, purchased, or maintained by an outsourcing provider," including business units/procurement/vendor management. Each application gets a **business criticality** (reputation damage, financial loss, operational risk, sensitive-information disclosure, personal safety, legal violations). Business criticality determines the extent of testing methods.
- **Analysis methods** as services under one platform: Static Analysis (SAST, incl. Pipeline Scan for dev tools), Software Composition Analysis (incl. agent-based scans), Dynamic Analysis (web applications + REST APIs), Manual Penetration Testing, Container/IaC/secrets scanning, External Attack Surface Management, Package Firewall (blocks untrusted packages at artifact repositories).
- **Findings**: "the flaws and vulnerabilities that Veracode scanning found in your application code … available in the Veracode Platform", with severities and resolution guidance; a **Triage Flaws page**; **mitigation** and **remediation plan** documentation. Findings statuses include Open / Closed / Reopened (observed in Analytics description).
- **Policies**: application security policy = rules/constraints + **grace periods** ("how much time teams must resolve findings to bring an application into compliance"); default policy derived from business criticality; remediation periods and acceptable thresholds.
- **Scoring**: integrates CVSS severity and CWE classification; Security Quality Score (0–100) aggregated per application; Veracode Levels (1–5) factored by testing technique and criticality.
- **Analytics/reports**: dashboards across the whole application portfolio (findings, policy compliance, scan usage); downloadable reports (customizable, detailed, summary, PCI, application activity).
- **Developer/program surfaces**: IDE plugins (upload, scan, review, AI-generated patches "Veracode Fix"), CI/CD integrations, SCM repository scanning, **ticketing/issue-tracking integrations** ("import and manage security findings in Agile and defect-tracking tools"), GRC integrations, APIs/CLI.
- **Aggregation variant**: Veracode Risk Manager is an "advanced Application Security Posture Management (ASPM) solution" importing findings "from multiple sources" via connectors and managing them as "issues."
- **Administration**: user account types, UI/API role permissions, API credentials.

## Product B — Checkmarx One

### Key observations (layer A)

- Platform hierarchy: **Tenant → Applications → Projects**. "Managing Applications" (create/configure/delete; Applications Page; Application Details Page) and "Managing Projects" (scan units; config-as-code) are separate top-level areas; a documented enhancement adds direct association of Projects to Applications.
- **Scanners** (one platform): SAST, SCA, IaC Security, Container Security, API Security (with API Inventory), Secret Detection, AI Supply Chain Security (LLM Risks), Repository Health (OSSF Scorecard); DAST results service/triage exists.
- **Results**: per-scanner **Results Viewers**; **triage per scanner type**; custom triage states; grouping of similar results (similarity IDs); AI Triage & Remediation.
- **ASPM layer**: "Application Security Posture Management" section — What is ASPM; **Application Risk Management**; **BYOR ("Bring Your Own Results")** — external results can be imported and triaged in-platform.
- **Global Inventory** (portfolio-wide) surface.
- **Policy Management**: create policies, view policies and **incidents**, **break build** enforcement.
- **Analytics**: Vulnerabilities, Scans, Engineering Overview, Executive Overview dashboards. **Reports**: scan/project/**application**/global-CSV/**SBOM**/package reports.
- **Integrations**: SCM (GitHub/GitLab/Bitbucket/Azure DevOps; PR decorations; monitor new repos; break build), CI/CD (Jenkins/TeamCity/GitHub Actions/Azure DevOps/Maven/CLI), **feedback apps** (Jira, Azure Boards, GitHub Issues, Slack, Teams, email) — i.e., findings pushed to developer work systems; IDE plugins incl. "Developer Assist".
- **Access control**: IAM console with users/groups/roles, SAML/Okta/AAD/OIDC/LDAP identity providers, OAuth clients, API keys, sessions.
- **Severity/prioritization**: critical severity support; CxScore risk prioritization for SCA. Engine tuning: SAST/IaC/secrets **query editors and presets**.

## Product C — Snyk

### Key observations (layer A)

- Core object chain (official docs): **Target** (external scanned resource — e.g., code repository or Kubernetes workload; a container for scanned results) → **Project** (defines *what* is scanned inside the Target and *how* — manifest files, scan type) → **Test** (the act of running a scan) → **Issues** (findings produced by scans, carrying Target/Project/Organization context).
- Web UI side menu: **Analytics, Inventory, Projects, Issues, Policies, Settings**, with a scope selector **Tenant → Group → Organization**.
- RBAC with predefined roles at tenant, group, and organization levels.
- Positioning: "Find, fix, and prevent issues across your software development lifecycle. Prioritize fixes and enforce policies."
- **Developer tools as first-class**: Snyk CLI (`snyk test` checks projects for open-source vulnerabilities and license issues and displays the issues found), IDE plugins, SCM and CI/CD integrations, Snyk API.
- Prioritization machinery for fixing (e.g., prioritization docs for its Essentials offering); Agent-security surface (Snyk Studio / Agent Scan / Agent Guard) for AI-driven development (2026-era addition).

## Product D — Semgrep AppSec Platform

### Key observations (layer A)

- Positioning: "Deploy static application security testing (SAST), software composition analysis (SCA), and secrets scans from one platform." Products: Semgrep Code (SAST), Semgrep Supply Chain (SCA with reachability analysis), Semgrep Secrets.
- **Findings page** with grouping (by rule / no grouping), filters, open-tab default.
- **Triage statuses** (documented table): **Open** (default; present in last scan and not ignored), **Reviewing**, **Provisionally ignored** (AI autotriage-flagged likely false positives; human confirms → Ignored or → To fix), **To fix** ("commonly used to indicate that these findings are tracked in Jira or assigned to developers"), **Fixed** (detected previously, no longer detected in the most recent scan of that branch — automatic), **Ignored** (present in code but dispositioned; ignore reasons: False positive, Acceptable risk, No time, No triage reason, Duplicate, Ignored via nosemgrep).
- **Removed** findings: finding not found in the latest scan because the rule was disabled/updated, the path disappeared, or the PR was closed without merge — removed findings do not count toward fix rate.
- **Triage propagation**: triage states carry across branches/refs for full scans; diff-aware scans differ. Reopening supported at any time.
- **Triage via PR/MR comments** (/fp, /ar, /other, /open replies) and a **bulk triage API**; org setting "Allow developers to triage findings".
- **Policies page**: rules/rulesets enable/disable and modes; remediation policies whose action can **block merge and comment on PR/MR**.
- **Fix support**: Autofix (AI-generated proposed change opened as a draft PR; humans review/merge); Multimodal remediation advice, suggested fixes, autotriage, noise filtering, component tags; custom rule writing (rules-as-code) and curated rulesets; **fix rate** as a tracked metric.

## Product E — Contrast Security

### Key observations (layer A at positioning/structure level; layer B where noted)

- Positioning: "Across your applications and APIs, Contrast Security helps you find and fix vulnerabilities, and detect and block attacks."
- Mechanism is **runtime instrumentation**: agents (Java, .NET, Node.js, PHP, Python, Go; Agent Operator for Kubernetes; Flex Agent) inside the running application feed the platform.
- Functional areas observed: **Assess** (runtime vulnerability analysis), **SCA**, **Protect** (attack blocking), **Scan** (SAST), Serverless Application Security, **ADR (Application Detection & Response)**.
- Management interface: two documented web interfaces (Northstar — new streamlined workflow with **Contrast Graph**, **Contrast Score**, workflows; and "Classic"). Reference section includes **Application scoring guide** and **Library scoring guide**, plus roles/permissions (EAC) and actions/permissions.
- Delivery: hosted and on-premises releases documented.
- (Layer B inference from the above: even the runtime-instrumentation philosophy lands on the same management-layer shape — applications as records, findings/attacks attached, scoring, roles.)

## Cross-product Comparison

| Dimension | Veracode | Checkmarx One | Snyk | Semgrep | Contrast |
|---|---|---|---|---|---|
| Unit of record | Application (portfolio) w/ business criticality | Application (tenant-level) containing Projects | Target → Project under Organization hierarchy | Repository/org findings (grouped by rule) | Application + APIs (agent-instrumented) |
| Findings vocabulary | "findings"/"flaws", mitigations | "results"/vulnerabilities per scanner | "Issues" | "Findings" w/ explicit state table | vulnerabilities + attack events |
| Finding sources | Built-in engines (SAST/SCA/DAST/MPT/containers/EASM) | Built-in engines (SAST/SCA/IaC/container/API/secrets/AI-SCA/scorecard/DAST) | Built-in engines (code/OS/container/IaC/cloud) | Built-in engines (SAST/SCA/secrets) | Runtime agents + SCA + SAST |
| External result import | VRM connectors (ASPM) | BYOR (Bring Your Own Results) | (integrations; not verified in detail) | — | — |
| Triage lifecycle | Triage Flaws page; mitigation; remediation plan; Open/Closed/Reopened statuses | Per-scanner triage; custom states; grouping | Issue triage in Issues UI; prioritization | Open/Reviewing/Provisionally ignored/To fix/Fixed/Ignored (+Removed); reasons; bulk & PR-comment triage | (not fetched — lifecycle pages not accessed) |
| Auto fix-detection | Analytics tracks Open/Closed/Reopened; policy compliance | Similarity-based grouping; change indicators | Issue lifecycle tied to scans | Automatic Fixed when no longer detected; Removed when rule/path gone | (not fetched) |
| Policy / gates | Policies: rules + grace periods + thresholds; Veracode Levels | Policy Management + incidents + break build | Policies menu; "enforce policies" | Policies page (rule modes); block-merge remediation policies | (not fetched) |
| Developer surfaces | IDE plugins, CI/CD, SCM repo scanning, ticketing import, AI Fix | IDE plugins (+Developer Assist), PR decorations, CI plugins, feedback apps (Jira/Boards/Issues/Slack/Teams) | CLI, IDE, SCM, CI/CD, API | PR/MR comments + triage commands, Autofix draft PRs, IDE, CI | (agent + platform; integrations section exists) |
| Portfolio analytics | Dashboards + reports across portfolio | Vulnerabilities/Scans/Engineering/Executive dashboards; app/scan/SBOM/CSV reports | Analytics + Inventory | Fix rate; findings dashboards | Application/Library scoring guides; Contrast Score |
| Scoring / prioritization | SQS 0–100, Veracode Levels 1–5, CVSS/CWE | CxScore (SCA prioritization), severity calc | Prioritization for fixing | Reachability analysis, component tags, autotriage | Contrast Score (app + library) |
| Roles / admin | User roles (UI/API), API credentials | IAM console: users/groups/roles/IdP, OAuth/API keys | RBAC: tenant/group/org predefined roles | Org settings (e.g., developer triage) | Roles & permissions (EAC), actions/permissions |
| Delivery | Cloud SaaS | Cloud SaaS (multi-tenant + single-tenant documented) | Cloud SaaS | Cloud platform + self-hosted engine | Hosted + on-premises |

## Canonical Model — Abstraction Layers

### Level 0 — Defining Invariant

Deliberately minimal; each item fails the "remove it and the Type stops being recognizable" test:

1. **Application records** — identified records of the organization's own applications (with ownership/criticality metadata) serve as the unit around which security work is organized. Without them there is no application-centric security platform — just a scanner or a ticket queue.
2. **Security findings attached to applications** — vulnerability/weakness records (from built-in analysis engines and/or imported external results) attributed to those application records.
3. **Tracked triage-and-remediation lifecycle** — each finding moves through a state lifecycle with recorded human decisions (triage: fix / ignore-with-reason / accept-risk; fix tracking; verified closure; reopening), and the platform tracks resolution over time (fix rate / open-closed trends).

Historical check (§24 reasoning): this core survives contact with older and differently positioned products — on-prem application-security results centers and scanner-portal products of earlier eras also held application/site records with findings and remediation tracking; what differs across eras is delivery, engine breadth, triage automation, and scoring — all of which stay outside L0.

### Level 1 — Common Mature Structure

Very common in mature modern products but not required to recognize the Type:

- **Multiple built-in analysis engines** — SAST, SCA, DAST, container/IaC, secrets, API security, (IAST-style runtime analysis) — orchestrated from the same platform.
- **External result ingestion** — importing findings from third-party/other tools for unified management (explicit in 2/5 sampled: VRM connectors, BYOR; implied by ASPM category).
- **Developer-facing surfaces** — PR/MR comments and merge gates, IDE plugins, CLI, CI/CD break-build, ticketing/feedback sync (Jira etc.).
- **Policy management** — configurable rules + thresholds + remediation deadlines (grace periods) + gate actions (fail build / block merge), and policy-compliance tracking.
- **Portfolio analytics & reporting** — dashboards across applications, findings trends (open/closed/reopened), fix rate, downloadable reports.
- **Severity/risk scoring & prioritization** — standardized severity inputs (CVSS/CWE-class inputs observed) plus vendor prioritization scores; reachability/criticality factors.
- **RBAC and organization hierarchy** — security admins vs developers vs managers; tenants/groups/organizations or equivalent.
- **Deduplication / scan reconciliation** — matching findings across scans (similarity/change indicators), auto-close when no longer detected, reopening on reappearance.
- **Remediation support** — resolution guidance; AI-generated fix suggestions/patches in modern products.
- **Administration & integration layer** — user/role admin, SCM/CI/ticketing integrations, APIs/CLI.

### Level 2 — Variant / Optional Structure

- Platform origin philosophy: enterprise-program-first (Veracode), scanner-suite-first (Checkmarx), developer-first (Snyk), engine-led (Semgrep), runtime-instrumentation-first (Contrast).
- Aggregation posture: engine-carrying platform vs aggregation-first ASPM posture vs hybrid.
- Delivery: cloud SaaS (multi- or single-tenant), on-premises/self-hosted engines.
- Security-testing services: managed/manual penetration testing, request-security-test flows.
- Security training modules for developers.
- Runtime defense (attack blocking, application detection & response) — edges toward runtime protection Types.
- External attack-surface discovery; artifact/package blocking; SBOM generation/reports.
- AI triage/autotriage, AI fix suggestions (recent; product-dependent maturity).
- Licensing/metering models (credits/engines/products).

### Level 3 — Vendor-specific Structure (kept out of the final document)

- Veracode: binary-packaging requirements for SAST; Security Quality Score/Veracode Level formulas; business-criticality→default-policy mapping; Package Firewall; Security Labs/eLearning; Greenlight; Pipeline Scan.
- Checkmarx One: CxScore; similarity IDs; credit usage; presets/query editors; Cloud Insights (CNAPP enrichment via Wiz/CrowdStrike/AWS/Sysdig/Uptycs); AppSec HD; Codebashing; 2ms secrets; AI Supply Chain Security/LLM Risks scanner.
- Snyk: Target/Project model specifics; Tenant/Group/Org hierarchy; Broker; Essentials vs other packaging; Studio/Agent Scan/Agent Guard.
- Semgrep: rules-as-code DSL, rulesets, diff-aware vs full scans, nosemgrep comments, Multimodal autotriage, bulk-triage API shape.
- Contrast: agent architecture, Assess/Protect/Scan naming, Contrast Graph/Score, Northstar vs Classic, ADR terminology.

## Rejected Findings

- "All platforms include developer training" — only 2/5 sampled → optional, not canonical.
- "All platforms include runtime attack blocking" — 1/5 → vendor-specific edge; not part of the Type.
- "Application Security Platform = ASPM" — ASPM names an aggregation-first posture within the same layer; engine-carrying platforms without heavy aggregation still clearly belong to the Type. Do not equate.
- "Findings are called 'issues'" — vocabulary differs (issues / findings / flaws / results); treat as implementation vocabulary.
- "Cloud-only" — on-premises/self-hosted delivery exists in the sample.
- "AI triage is core" — recent, product-dependent; keep optional.
- Precise numbers (grace-period lengths, scoring formulas, state-name sets) — asserted nowhere in the final document; product-specific details remain in these notes.

## Boundary Findings

1. **vs SAST / DAST-IAST / SCA (engine leaves, §15)** — relationship: capability ⊂ platform. Engine leaves describe analysis/testing *capabilities* (engines, rules, scan mechanics, result interpretation). The Application Security Platform is the *application-centric management layer* — records, finding lifecycle, policy/gates, portfolio management. A pure engine/CLI without application records and lifecycle management is not the platform; a platform always includes or ingests engine output. The same vendor product can substantiate both leaves depending on the surface being described. **"Remove the application records + lifecycle → you have an engine leaf; remove the engines (keep import) → still a platform (aggregation posture)."**
2. **vs Vulnerability Management (§15)** — object domain split. Vulnerability Management manages vulnerabilities of infrastructure/host/asset populations (remediation = patching/configuration on systems); the Application Security Platform manages weaknesses of application artifacts (code, dependencies, APIs, builds; remediation = developer code/component changes). Both share finding-lifecycle shape; the domain and the remediation actor differ. (Reasoning-level for the VM side; VM leaf not yet processed — flagged for joint review.)
3. **vs API Security Platform (§15)** — API security's center of gravity is API runtime discovery/inventory/defense; within AppSec platforms, API security appears as one scanner module (Checkmarx API Security + API Inventory). An API-first runtime defense product is a different center of gravity.
4. **vs WAF (§15)** — WAF protects traffic at the edge in real time; no application records, no finding lifecycle, no SDLC integration. Protection surface vs program layer.
5. **vs Software Supply Chain Security / SBOM Management / Secrets Security (§15)** — focused capabilities that appear as modules of the platform (secret detection, SBOM reports, package blocking, AI supply chain). Standalone leaves exist where those capabilities are the whole product.
6. **vs CNAPP / CSPM / CWPP (§15)** — cloud-infrastructure object domain; platforms integrate/enrich with CNAPP data (Checkmarx Cloud Insights) rather than owning that domain.
7. **vs Static Code Analysis / Code Quality Platform (§12)** — code-quality platforms' primary lens is code health/maintainability (with security as one category); the AppSec platform's primary lens is security risk of applications with program/policy machinery. Boundary genuinely fuzzy for SAST-flavored tools; held on center of gravity.
8. **vs SIEM / SOC / incident response (§15)** — runtime security-event management vs SDLC finding management; different object domains (events vs application weaknesses).

Taxonomy note: §15 contains both this platform leaf and its engine leaves (SAST, DAST/IAST, SCA, plus supply-chain/secrets/SBOM). The directory appears to intend a capability-layer vs program-layer split; this research supports that reading but the family is inherently entangled — recorded for Boundary Issues.

## Uncertainties

- Contrast lifecycle/policy specifics were not fetched; Contrast-based observations are positioning/structure-level. Claims in the final document that rest on Contrast are kept weak ("some products", "runtime-instrumentation philosophy").
- Snyk's "Inventory" surface semantics (exact scope of the inventory page) not verified in detail.
- Historical products (Fortify SSC-class, IBM AppScan, WhiteHat/Qualys WAS-class) not directly researched; historical generalization is layer C reasoning anchored on Veracode's documented long-standing portfolio/policy methodology.
- Whether external-result import is "common" or "variant" — explicit in 2/5 sampled plus the ASPM category's existence; treated as common-to-variant (L1/L2 boundary), written as "some products" in the final doc.
- "Application Security Platform" is also used in the market as an umbrella marketing phrase; the researched products define the concrete layer documented here.

## Final Synthesis

An Application Security Platform is the application-centric security management layer of the software development lifecycle. Its world is small: applications as managed records; security findings attached to those records from analysis engines and/or imported results; and a tracked triage-and-remediation lifecycle that ends in fixes, documented dispositions, or reopenings. Around this core, mature products add engines, developer surfaces (PR/IDE/CLI/CI gates), policy gates, portfolio analytics, scoring, RBAC, and integrations. The platform manages and tracks; engines analyze; developers fix. It is not infrastructure vulnerability management (different object domain), not a WAF or runtime defense product (no finding lifecycle), and not GRC (consumes, not manages). Aggregation-first (ASPM) and engine-carrying are postures of the same Type, not separate Types.
