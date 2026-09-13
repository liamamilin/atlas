# Research Notes — DAST / IAST

Research date: 2026-09-07
Leaf: DAST / IAST (DIRECTORY.md §15 Cybersecurity, Identity & Trust)
Slug: dast-iast

---

## Research Goal

Understand what the "DAST / IAST" Application Type is as a single canonical Type: what objects exist inside it (targets, test sessions, findings), how the testing actually works from the outside (black-box dynamic scanning) and from within the running application (instrumented/interactive testing), who operates these products, and where the boundary lies against SAST, SCA, Vulnerability Management, WAF, penetration testing tooling, breach & attack simulation, functional testing, and API security platforms.

## Initial Boundary (hypothesis before research)

- The directory leaf merges two technique categories the market usually names separately:
  - **DAST** (Dynamic Application Security Testing) — black-box security testing of a running application from outside, by crawling/exercising it and analyzing responses.
  - **IAST** (Interactive Application Security Testing) — testing from inside the running application via an instrumentation agent that observes execution and data flow while the app is exercised.
- Hypothesis: one Type family — "security testing of a running application" — with the observation vantage (outside vs instrumented) as the principal variant axis, because both modes share: a running target, deliberate exercise of the application, runtime-evidence findings, and a remediation workflow.
- Likely users: application security engineers, penetration testers, QA/test teams, developers.
- Nearest neighbors: SAST, SCA, Application Security Platform, Vulnerability Management, WAF, Penetration Testing Management, Breach & Attack Simulation, End-to-end Testing Platform, API Security Platform, Software Test Management.
- Unknowns: whether IAST can be documented with 2+ products from official sources; whether the two modes share enough stable structure to be one Type; how false-positive posture differs and whether it is definitional.

## Research Questions

1. What is the central managed object — the target application, the scan/test session, or the finding?
2. How does a DAST product acquire the application surface (crawler, browser-driven exploration, spec import)?
3. How does the testing act work (passive observation vs active attack; intensity tiers)?
4. How does an IAST product acquire visibility (instrumentation agent, sensors; what does it observe)?
5. What does the application exercise in IAST mode — who generates the traffic (functional QA, DAST, manual use)?
6. What is a finding: structure, evidence types, severity/confidence, remediation guidance?
7. How are false positives handled (verification/proof-based checks, confidence ratings, triage states)?
8. What safety/authorization rules govern the testing act itself?
9. What lifecycle does a scan/test session follow, and what happens after findings (retest, verify, export)?
10. Which interfaces exist (desktop tool, web console, CLI/API/CI integrations)?
11. Do mature products combine DAST and IAST in one product, or ship them as separate products?
12. Where are the boundaries vs SAST / VM / WAF / pen-test tooling / BAS / functional testing?

## Representative Products

Selected for market representation, documentation quality, differing product philosophy, and differing customer tier:

| Product | Philosophy | Evidence tier |
|---|---|---|
| OWASP ZAP | Free open-source desktop DAST: proxy-first, manual + automated, community add-ons | A (official docs, deep) |
| Burp Suite (PortSwigger) | Manual-first professional toolkit with an embedded automated scanner; pen-tester centric | A (official docs, deep) |
| Contrast Security (Assess) | IAST pioneer: instrumented agent analyzes the application from within; accuracy-first | A (official docs) |
| Invicti Enterprise | Enterprise DAST scan-management platform (SaaS/on-prem) that also ships an IAST module (Shark) | A (official docs structure; category pages) |
| Black Duck Seeker | IAST product riding DevOps pipelines and QA testing | B (official product pages only; docs not fetched) |

## Sources

- OWASP ZAP — https://www.zaproxy.org/docs/ (documentation index) and https://www.zaproxy.org/getting-started/ (Getting Started Guide). Fetched 2026-09-07.
- OWASP ZAP — https://www.zaproxy.org/docs/alerts/ (ZAP Alert Details catalog). Fetched 2026-09-07.
- PortSwigger Burp Suite — https://portswigger.net/burp/documentation/scanner (Burp Scanner) and https://portswigger.net/burp/documentation/scanner/auditing (Auditing). Fetched 2026-09-07.
- Contrast Security — https://docs.contrastsecurity.com/ (index), /en/welcome-to-contrast.html, /en/assess.html (Assess), /en/ast-technology.html (AST technology). Fetched 2026-09-07.
- Invicti — https://www.invicti.com/support/ (docs portal), https://docs.invicti.com/ie-is/category/invicti-enterprise-and-standard, /ie-is/category/scans, /ie-is/category/invicti-shark. Fetched 2026-09-07. (https://www.invicti.com/docs/invicti-enterprise/ returned 404; docs live under docs.invicti.com.)
- Black Duck Seeker — https://www.blackduck.com/interactive-application-security-testing.html (Seeker Interactive product page). Fetched 2026-09-07. Product-page evidence only (Tier 2).

---

## Product A — OWASP ZAP (evidence layer A)

### Key observations

**Positioning.** "Zed Attack Proxy (ZAP) by Checkmarx is a free, open-source penetration testing tool... designed specifically for testing web applications." At its core a "manipulator-in-the-middle proxy" standing between the tester's browser and the web application to intercept, inspect, and modify messages. Runs as a desktop application or as a daemon process; versions for major OSes and Docker.

**Testing model (from the Getting Started Guide).**
- Defines the pentesting process as Explore → Attack → Report.
- **Quick Start Automated Scan**: enter the URL to attack → ZAP crawls the application with its spider and passively scans each page → then the active scanner "attacks all of the discovered pages, functionality, and parameters."
- Three spiders for crawling: traditional HTML-following spider, Client spider (drives real browsers for modern JS-heavy apps), AJAX Spider.
- **Passive scanning** analyzes proxied requests/responses without changing anything; "considered safe"; runs in the background during exploration.
- **Active scanning** "uses known attacks against the selected targets... is a real attack on those targets and can put the targets at risk, so do not use active scanning against targets you do not have permission to test."
- **Safe mode** prevents ZAP from causing harm (at reduced functionality) — an attack-mode control on the toolbar.
- Manual exploration: browse the app through the proxy; passive scanning and site-tree building continue; the HUD (Heads Up Display) overlays security functionality in the browser.

**Findings ("alerts").**
- Alerts are recorded as requests/responses are analyzed; footer counts alerts by risk category (Informational/Low/Medium/High).
- Alert detail shows the URL, the vulnerability detected, and the response with the offending part highlighted.
- The public Alert Details catalog lists every scan rule with: alert name, status (release / beta / alpha / deprecated), risk, type (Active / Passive / Tool), and CWE/WASC identifiers; many alerts carry tags mapping to OWASP Top 10 categories or OWASP Web Security Testing Guide chapters; technology tags let users skip tests for absent technologies.

**Session/state.** ZAP sessions (the recorded exploration + findings) can be persisted to a local database or discarded on exit.

**Automation.** Automation Framework, Docker-packaged scans, GitHub Actions, API and daemon mode. Authentication handled via a dedicated "Authentication Decision Tree" guide. Extensibility via a free add-on marketplace (plugin architecture).

## Product B — Burp Suite (evidence layer A)

### Key observations

**Positioning.** "Burp Scanner is an automated dynamic application security testing (DAST) web vulnerability scanner. Designed to replicate the actions and methodologies of a skilled manual tester." Powers scans in Burp Suite's desktop editions and the enterprise product ("Burp Suite DAST"). Edition ladder: Burp Suite DAST (enterprise), Professional ("web penetration testing toolkit"), Community ("best manual tools"). (A new "Burp AT" agentic-AI assistant can run scans/tasks.)

**Scan phases.** Scans "generally comprise two key phases":
- **Crawling** — catalogs the application's content and navigational paths; "navigates around the application in largely the same way that a human would. It follows links, submits forms, and logs in where necessary."
- **Auditing** — analyzes traffic and behavior to identify vulnerabilities; sends requests and examines results, using crawl information to work efficiently.

**Audit machinery (Auditing page).**
- Three audit phases: **passive** (observes normal traffic; consolidated reporting of identical issues across locations), **active** (sends modified requests; checks graded light / medium / intrusive with explicit caution warnings: medium checks "may trigger security alerts, log users out"; intrusive checks "carry a significant risk of modifying or damaging the application or its data... may cause permanent data loss, service outages"), **JavaScript analysis** (hybrid static + dynamic analysis of client code for DOM-based issues; static-only findings get lower confidence than dynamically confirmed ones).
- **Insertion points** — parameter locations within requests where payloads are placed; per-type encoding (URL/JSON/XML/Base64, nested encodings); parameter-location shifting to bypass protections.
- **Audit prioritization** — items scored on attack-surface exposure (unique insertion points) and interest level (state-changing methods, structured content types, authentication required); weighted 80/20; queue re-scores as the crawl discovers new items.
- **Automatic session handling** — re-walks crawl paths to obtain fresh session tokens; handles single-use CSRF tokens by re-issuing preceding requests; monitors session validity with checkpoints and rolls back on session loss.
- **Error handling** — granular failure tracking (individual check → insertion point → request → whole scan), retry passes for timeouts, optional pause/abort on excessive errors.

**Authenticated scanning.** Login credentials, identifying login/registration forms, recorded login sequences (recorded by the tester and replayed by the scanner), troubleshooting guidance.

**Scope & configuration.** Preset scan modes, custom scan configurations (crawl settings, audit settings, which scan checks are enabled), browser-powered scanning, API scanning (with requirements; OpenAPI/GraphQL-era APIs), SPA scanning support.

**Custom checks.** BChecks — user-defined scan check definitions (with worked examples including Collaborator-based out-of-band checks and Log4Shell); community submission of BChecks.

## Product C — Contrast Security / Contrast Assess (evidence layer A)

### Key observations

**Positioning.** "Contrast Assess is an application security testing tool that combines Static (SAST), Dynamic (DAST), and Interactive Application Security Testing (IAST) approaches to provide highly accurate and continuous information on security vulnerabilities in your applications." Platform framing (Welcome page): "helps you find and fix vulnerabilities, and detect and block attacks" across applications and APIs; Northstar interface (2025) alongside Classic; product lines Assess (testing), SCA, Protect (runtime defense), Scan, Serverless; ADR (Application Detection & Response) technology.

**IAST mechanism.**
- "Contrast AST uses an agent that instruments applications with sensors. The sensors look at data flow in real time and analyze the application from within" to find vulnerabilities in: libraries, frameworks, and custom code; configuration information; runtime control and data flow; HTTP requests and responses; back-end connections.
- "Appropriate for environments such as a test, QA, or staging servers. It is also applicable to developer workstations." IDE integrations (e.g., Visual Studio) let developers fix without leaving the IDE.

**Features.**
- Vulnerabilities list with remediation guidance.
- Application scores ("gauge the security of an application at a glance") — scoring guide documented.
- **Route coverage** — "detects possible routes by associating vulnerabilities with the originating web request."
- **Flow maps** — "insight into the architecture of the running application."
- Compliance and policy reporting.

**Customization.** Assess rules (enable/disable to tune detection); "security controls" — methods in the organization's own code that mark data as safe (teaching the agent what is validated).

**Agents & deployment.** Agents per technology (Java, .NET, Node.js, PHP, Python, Go, plus a "Flex Agent" and a Kubernetes "Agent Operator"); hosted and on-premises platform; roles and permissions documentation; release notes per agent. Agent installation documented (direct Java agent install, Helm chart).

## Product D — Invicti Enterprise (evidence layer A — documentation structure; category pages)

### Key observations

**Positioning.** Documentation portal covers three product lines: "Invicti AppSec Platform — dynamic and static application security testing with intelligent vulnerability management and seamless CI/CD integration" (plus ASPM via an acquired product); "Invicti Platform — enterprise-grade web application security scanning with advanced crawling technology" (on-demand and on-premises; security checks + Runtime SCA release notes); "Invicti Enterprise and Standard — automated web application security testing with industry-leading accuracy and minimal false positives." Self-described as "The Largest Dynamic Application Security Solutions Provider In The World" (help center).

**Documented module structure (Invicti Enterprise and Standard).**
- **Discovery** — visibility into online assets, web applications, and services; "Predictive Risk Scoring."
- **Targets** — "Add, import, and manage your web targets for scanning."
- **API security** — manage/monitor APIs; GraphQL API scanning pages.
- **Scans** — Introduction to Scanning; Authentication; Scan profiles; Security checks; Launch scans; Work with scans; Scan results.
- **Invicti Shark** — "Learn how to run Interactive Application Security Testing (IAST) using your Invicti Enterprise and Standard"; deployment sections per language: PHP, Java, .NET, Node.js.
- **Reports** (incl. compliance reports), **Issues** ("View and manage all security issues (vulnerabilities) assigned to you and your team"), **Technologies** (automatic identification of frameworks/languages/platforms for accurate testing), **Policies** (organization-wide scanning standards and governance), **Notifications**, **Integrations**, **Team management** (users/teams/roles), **Agents** (deploy scanning agents "for distributed or internal network scanning"), Settings.

**Observation.** This is the enterprise scan-management shape: the *target* (a registered website/API) is the central record; scans are launched and scheduled against targets; results become issues assigned to people; and IAST is offered as an add-on instrumentation layer (per-language agents) alongside the external scanner — evidence that DAST and IAST ship as two modes of one product family.

## Product E — Black Duck Seeker (evidence layer B — product pages only)

### Key observations

- Positioning: "The industry's first interactive application security testing (IAST) software solution with active verification and sensitive-data tracking for web-based applications"; automates "the security testing of modern web applications and services" for "development, QA, DevOps, and security teams."
- Mechanism claims (vendor marketing; not verified in operational docs): "Seeker monitors web app interactions in the background during normal testing"; "active verification technology — automatically retests identified application vulnerabilities and validates whether they are real and can be exploited"; "near-zero false positives"; pinpoints "vulnerable lines of code" with remediation advice/e-learning.
- Sensitive-data tracking (encryption posture of critical data; PCI DSS/GDPR compliance framing).
- Pipeline integration: native integrations, web APIs, plugins for CI/CD and DevOps workflows.
- API coverage: discovers known/unknown APIs (REST, SOAP, GraphQL specs; gRPC microservices) and verifies security posture.
- Component analysis: integrates Black Duck Binary Analysis for open-source vulnerabilities in binaries/libraries.
- Compliance dashboards: OWASP Top 10, PCI DSS, GDPR, CWE/SANS Top 25.
- Portfolio context: Black Duck sells DAST ("Continuous Dynamic"), SAST (Coverity), SCA, IAST (Seeker), and Fuzz Testing as separate products — market evidence that DAST and IAST are recognized as distinct technique categories, commonly sold alongside each other in AppSec portfolios.

**Limitation:** operational documentation not fetched; Seeker observations are used only to corroborate the IAST mechanism pattern (instrumented observation during exercised traffic + verification) and are not used for precise operational claims.

---

## Cross-product Comparison

| Dimension | ZAP | Burp Suite | Contrast Assess | Invicti Enterprise | Seeker (B) |
|---|---|---|---|---|---|
| Central object | ZAP session (explored site tree + alerts) over a target URL | Scan (crawl + audit) over a target; issues | Instrumented application in the platform (vulnerabilities, routes, flow maps) | Target (registered website/API) → scans → issues | Instrumented application monitored during testing |
| Observation vantage | Outside: intercepting proxy + scanner | Outside: scanner replicating a manual tester | Inside: instrumentation agent with sensors | Outside scanner + optional inside agent (Shark) | Inside (claimed) |
| Surface discovery | 3 spiders (HTML, browser-driven client spider, AJAX) | Crawl phase (links, forms, logins; browser-powered) | Route coverage from observed requests | Crawl technology; discovery of online assets | API/spec discovery (claimed) |
| Test act | Passive scan (safe) + active scan (real attack, permission warning) | Passive + active audit checks graded light/medium/intrusive; JS static+dynamic analysis | Observe data flow in real time during exercised use; no own attack engine documented | Scheduled/on-demand scans with security checks | Observe background interactions during normal testing; active-verification retests |
| Findings | Alerts: risk level, CWE/WASC, OWASP/WSTG tags, response evidence | Issues with evidence; confidence ratings; consolidation of duplicate issues | Vulnerabilities + remediation guidance; application score | Issues assignable to team members | Vulnerabilities correlated to source lines (claimed) |
| False-positive posture | Passive vs active distinction; safe mode | Static-JS findings rated lower confidence; dynamic confirmation prioritized | "Highly accurate" positioning; security controls teach validated code | "Minimal false positives" positioning | "Near-zero false positives" (vendor claim) |
| Authentication handling | Authentication decision tree; configured auth | Recorded login sequences; session maintenance with token handling | Rides real app sessions (QA/QA tools' traffic) | Scan authentication section | Rides normal testing (claimed) |
| Safety rules | Permission warning; safe mode; passive=safe / active=attack | Caution warnings per intensity; error escalation; pause/abort | Test/QA/staging environments recommended | Scan profiles/policies; distributed agents for internal networks | — |
| Workflow after findings | Alerts viewed/exported; re-scan | Issue reports; re-scan | Fix → retest; IDE handoff | Issues assigned; reports; re-scan | Remediation advice; retest (claimed) |
| Interfaces | Desktop UI (site tree, request/response workspace, alerts); daemon + API | Desktop suite (proxy tools + scanner); enterprise edition | Web platform (Northstar/Classic); IDE integrations | Web console; scan agents | Dashboards; CI plugins (claimed) |
| Automation | Automation Framework, Docker, GitHub Actions, API/daemon | CI-driven scanning; BChecks; enterprise scheduling | Agent deployment via Helm/direct; platform APIs | Scheduled scans; notifications; integrations | CI/CD native (claimed) |
| Team/org layer | None (single-user tool) | Roles in enterprise edition | Roles/permissions documented | Team management with roles | Enterprise |
| Adjacent add-ons | Add-on marketplace (incl. non-HTTP scans) | Extensions/BApps | SCA, Protect (runtime defense), ADR | Runtime SCA, discovery, ASPM | Binary Analysis (SCA), DAST sibling product |

### Stable commonalities (evidence layer B)

1. **A running target application under test.** All products organize their work around a specific, identified running application/endpoint (ZAP: URL/session; Burp: scan target; Contrast: instrumented application; Invicti: registered target; Seeker: monitored application).
2. **The application is deliberately exercised, and vulnerabilities are detected from runtime behavior.** Either the tool generates test traffic (ZAP/Burp active checks) or the tool observes exercised traffic from inside the application (Contrast sensors, Invicti Shark agents, Seeker monitoring). In both modes the evidence is the application's actual runtime behavior — never a source-code abstraction alone.
3. **Findings are structured, evidenced vulnerability records.** Every product records what was found, where (URL/request or code location/route), proof (response content, data-flow trace), severity/risk, and remediation guidance. Weakness-class mappings (CWE, OWASP Top 10/WSTG) appear in ZAP, Burp, Seeker, Invicti.
4. **Passive/observational testing is distinguished from active/attack testing.** ZAP: passive (safe) vs active (real attack); Burp: passive audit phase vs graded active checks; Contrast/Seeker: observational detection with separate active-verification steps (Contrast documents no attack engine; Seeker claims active verification retests). The passive/active distinction is a stable conceptual axis even where terminology differs.
5. **The testing act is treated as potentially harmful and gated.** Authorization warnings (ZAP: "do not use active scanning against targets you do not have permission to test"; Burp: caution notes on medium/intrusive checks), safe modes, intensity tiers, and staging-environment recommendations (Contrast: test/QA/staging) recur across the sample.
6. **Authentication is a first-class scanning concern.** Credentialed/authenticated testing machinery is documented in ZAP, Burp (recorded logins, session maintenance), and Invicti; IAST products sidestep it by riding real authenticated sessions.
7. **Verification/false-positive management is a core behavior.** Confidence ratings (Burp), security controls that mark validated code (Contrast), active verification/retesting (Seeker claimed; Burp dynamic confirmation), and accuracy positioning (Invicti, Contrast) all address the same problem: dynamic findings must be proven true.
8. **Results flow into a remediation workflow.** Issues/queues with assignment (Invicti), IDE/developer handoff (Contrast), reports and export (ZAP, Burp, Invicti), CI/CD and ticketing integrations across the sample.
9. **Automation and pipeline integration are standard in mature products** (ZAP automation/docker/API, Burp CI-driven scanning, Contrast agent deployment + APIs, Invicti scheduling/notifications/integrations, Seeker CI plugins).

### Product-specific differences (candidates for L2/L3)

- ZAP: single-user OSS desktop shape; add-on marketplace; HUD; alert catalog as public documentation; session persistence model.
- Burp: manual-tester replication philosophy; insertion-point machinery; 80/20 audit prioritization; BChecks custom check language; Collaborator out-of-band checks; edition ladder; agentic-AI assistant.
- Contrast: sensor instrumentation detail; route coverage; flow maps; security-controls customization; Protect (runtime defense) sibling; ADR; Northstar UI migration.
- Invicti: target-registered scan management at organization scale; distributed scan agents; technologies detection; Shark IAST as a per-language add-on layer; ASPM adjacency.
- Seeker: active-verification retesting as headline; sensitive-data tracking; Binary Analysis integration.

---

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Minimal structure without which the Type is not recognizable:

1. **A running target application under security test** — a specific, identified deployed/executing application (web app, API, service) is the subject. Not source code (→ SAST), not infrastructure (→ network scanners), not security controls (→ BAS).
2. **An exercise-and-observe test act against that running application** — the application is deliberately exercised (generated test requests and/or real functional use observed through in-app instrumentation), so that vulnerabilities can be detected from the application's actual runtime behavior and responses. This is what excludes static analysis and pure results-aggregation tools.
3. **Findings with runtime evidence** — identified vulnerabilities recorded as managed test results, each carrying proof from the run (request/response evidence, or a data-flow/code location inside the instrumented application), with severity and remediation guidance.

Justification: remove the running-application target and test source code → SAST. Remove the exercise act (aggregate findings from other tools only) → Vulnerability Management. Remove the security intent (test functional correctness) → functional/E2E testing. Remove evidence-based findings → a traffic log. All five sampled products exhibit all three invariants; both modes (outside scanning, inside instrumentation) satisfy them.

Historical/market check: the definition holds for pre-cloud desktop scanners and command-line web scanners of the 2000s generation (crawl + attack + alerts, no cloud, no console), for OSS proxy-first tools (ZAP), for enterprise SaaS scan platforms (Invicti), and for agent-based IAST (Contrast, Shark, Seeker). None of these eras or shapes is excluded — so the core must not require CI/CD, SaaS consoles, spec imports, browser engines, or team features. It does not.

### L1 — Common Mature Structure

Present in most mature products; not required for the definition:

- **Surface discovery** — crawlers/spiders (including browser-driven exploration for JS-heavy apps), or specification imports for APIs, or route discovery from instrumented traffic.
- **Authentication handling** — stored credentials, recorded login sequences, session maintenance (including single-use tokens) for credentialed testing.
- **Check libraries and scan policies** — collections of security checks mapped to weakness classes (CWE, OWASP Top 10 / WSTG), with configurable policies, per-technology scoping, and custom checks.
- **Test-intensity tiers** — safe/passive observation through progressively more intrusive active testing, with explicit warnings and options to enable/disable checks.
- **False-positive management** — confidence ratings, dynamic confirmation of static suspicions, retest/active-verification of findings, triage states, accuracy positioning.
- **Scan lifecycle** — launch (on-demand/scheduled/pipeline-triggered) → run → results → re-scan/retest of fixes; error handling and resumability at scale.
- **Results management** — issue queues with assignment, deduplication/consolidation, dashboards, reporting incl. compliance mapping (OWASP/PCI/GDPR).
- **Integration spine** — ticketing, CI/CD, notifications/chat, APIs.
- **Team/org layer** — roles, team management, organization-wide policies (in the enterprise/console shapes).
- **Distributed scan agents** — scanning internal networks from deployed agents (enterprise DAST shape).

### L2 — Variant / Optional Structure

- **Observation vantage (the DAST/IAST axis)** — external black-box scanning vs in-app instrumented testing vs both in one product (a DAST vendor adding per-language IAST agents; an IAST platform claiming to combine SAST/DAST/IAST approaches).
- **Operating shape** — desktop manual-first toolkit vs fully automated scheduled scanner vs SaaS scan-management platform vs pipeline-native IAST.
- **Trigger** — on-demand, scheduled, CI-triggered, or QA-driven (IAST rides normal functional testing).
- **Target breadth** — web apps, APIs (incl. GraphQL/gRPC-era surfaces), SPAs; per-language/runtime agent coverage on the IAST side.
- **Deployment** — desktop install, SaaS multi-tenant, on-premises platform, Docker/CLI, scan agents inside the network.
- **Adjacent add-ons bundled by the same vendor** — runtime protection (RASP/ADR), SCA/runtime SCA, asset discovery, ASPM aggregation.

### L3 — Vendor-specific (Research Notes only)

- ZAP: add-on marketplace; HUD; Automation Framework; session persistence to local HSQLDB; public alert catalog with per-rule CWE/WASC; safe-mode control; three named spiders.
- Burp: crawl/audit phase machinery; insertion points with per-type and nested encoding; parameter-location shifting; 80/20 attack-surface/interest prioritization; automatic session handling with checkpoints/rollback; granular error escalation (check → insertion point → request → scan); BChecks and Collaborator-based checks; Burp AT agentic assistant; editions (DAST/Professional/Community).
- Contrast: "sensors" instrumentation; route coverage; flow maps; Contrast Score; Assess rules; security controls; Northstar vs Classic; per-language agents + Flex Agent + Agent Operator (Helm); ADR technology; Protect runtime-defense sibling.
- Invicti: Targets/Scans/Shark/Issues module names; scan profiles; security-checks library; technologies detection; predictive risk scoring; distributed scan agents; Shark per-language agents (PHP/Java/.NET/Node.js); on-demand vs on-premises releases; ASPM via acquisition.
- Seeker: active-verification retesting; sensitive-data tracking; Black Duck Binary Analysis integration; "near-zero false positives" claim (unverified in docs); portfolio siblings (Continuous Dynamic DAST, Coverity SAST, Fuzz Testing).

---

## Vendor-specific Findings

See L3. None of these enter the canonical document except as neutral, vendor-attributed examples where useful. Numeric specifics (priority weighting 80/20; agent language lists) stay here.

## Boundary Findings

| Neighbor Type | Relationship | Distinction | "Remove what → becomes the other" |
|---|---|---|---|
| Static Code Analysis Platform (SAST) | closest testing neighbor | SAST analyzes source code without executing it; DAST/IAST test a running application and derive evidence from runtime behavior. | Remove the running-application exercise; analyze code statically → SAST |
| Software Composition Analysis (SCA) | sibling technique | SCA inventories dependency components and known vulnerabilities in them; DAST/IAST find vulnerabilities in the application's own running behavior. | Change the object from runtime behavior to third-party components → SCA |
| Vulnerability Management | consumer / aggregate | VM aggregates, deduplicates, prioritizes, and tracks remediation of findings from many scanners across asset classes; it does not exercise applications itself. | Remove the test act; keep aggregation/tracking of others' findings → Vulnerability Management |
| Web Application Firewall (WAF) | opposite side of the same traffic | WAF sits in traffic and blocks/enforces continuously in operation; DAST tests deliberately and reports, usually in test environments, without enforcement. | Change the act from test-and-report to enforce-and-block → WAF (and runtime application protection) |
| Penetration Testing Management | process around the act | PT management organizes human-led engagements (scoping, rules of engagement, reporting); DAST/IAST are the tools that actually perform systematic testing. Some DAST tools support manual testers (Burp, ZAP) without managing engagements. | Remove the systematic test engine; keep engagement organization → Penetration Testing Management |
| Breach & Attack Simulation | sibling "attack" family | BAS validates whether security controls detect/respond to attacks across infrastructure; DAST/IAST hunt vulnerabilities in the application itself. | Shift the subject from application vulnerabilities to control efficacy → BAS |
| End-to-end Testing Platform | functional testing neighbor | Both exercise running applications; E2E testing verifies functional correctness, DAST/IAST verify security properties, with security-specific checks and findings. | Remove the security intent and weakness vocabulary → E2E / functional testing |
| API Security Platform | adjacent, different object horizon | API security platforms maintain a continuous inventory of the whole API estate, observe production traffic, and enforce; DAST/IAST run bounded tests against identified targets and produce findings. API-security products embed DAST-style testing as one module. | Add continuous estate-wide inventory + traffic observation, remove the bounded test engagement → API Security Platform |
| Software Test Management | process neighbor | Test management organizes test cases/suites/runs for QA; DAST/IAST perform security testing with their own vulnerability semantics. | Replace vulnerability findings with functional test cases → Software Test Management |
| Fuzz Testing (technique/product family) | technique overlap | Fuzzing feeds malformed inputs to find crashes/vulnerabilities; fuzzing exists as a technique inside DAST products and as a separate product family outside this directory. | — (noted, adjacent) |

**Taxonomy observation.** The directory leaf merges two technique categories that the market commonly names and sells separately (Black Duck sells "Continuous Dynamic" DAST and "Seeker Interactive" IAST as distinct products; Gartner-class AppSec taxonomies list DAST and IAST as separate technique families). Research supports treating them as one Type family — security testing of a running application — with the observation vantage as the principal variant axis and documented convergence (vendors shipping both modes in one product). If the taxonomy is later split, it would fall cleanly along that axis. No silent taxonomy rewrite performed.

## Uncertainties

1. Seeker's operational documentation was not fetched; all Seeker observations are vendor product-page claims (Tier 2) and were used only to corroborate the IAST mechanism pattern, not for precise claims. The "near-zero false positives" figure is a vendor claim and is not asserted in the final document.
2. Whether every IAST product requires a companion traffic generator (DAST or QA tests) is not documented uniformly; the researched products all rely on exercised traffic (QA-driven or scanner-driven), but the final document phrases this as the common pattern rather than a rule.
3. Invicti evidence is strongest at the module-structure level (documentation architecture); detailed scan-mechanics pages were not fetched, so Invicti is not used for precise operational claims beyond its documented structure.
4. The degree to which modern DAST products cover non-HTTP protocols (e.g., gRPC) varies; evidenced only in vendor claims (Seeker, Invicti GraphQL pages) — kept generic in the final document.
5. The relative market size of IAST vs DAST deployments was not researched; the final document makes no market-share claims.
6. AI-assisted testing features (Burp AT, agentic scanning) are recent; treated as an emerging vendor-specific extension, not part of the Type definition.

## Final Synthesis

The DAST / IAST Type is defined by a small core: a running, identified application is placed under security test; the application is deliberately exercised — by generated test traffic from outside, or by real use observed through in-app instrumentation — and vulnerabilities are detected from the application's actual runtime behavior; and each finding is recorded as a structured, evidenced vulnerability (what, where, proof, severity, remediation guidance) managed as a test result. Around that core, mature products add surface discovery (crawlers or instrumentation-derived routes), authentication handling, check libraries and scan policies mapped to weakness classes, graded test intensity with safety gates, false-positive verification, scan lifecycle machinery, results/issue management with assignment and reporting, and CI/CD + ticketing integration. The principal variant axis is the observation vantage — outside (black-box scanning) vs inside (instrumented agent) — which the market names DAST and IAST respectively; mature products increasingly ship both modes in one portfolio or product. The Type is bounded against SAST (static, no running app), SCA (components, not behavior), Vulnerability Management (aggregates findings, does not test), WAF/runtime protection (enforces instead of tests), penetration testing management (organizes human engagements), BAS (validates controls, not app vulnerabilities), and functional testing (correctness, not security).
