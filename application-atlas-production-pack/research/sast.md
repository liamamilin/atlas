# Research Notes — SAST (Static Application Security Testing)

Research date: 2026-09-09

## Research Goal

Understand what a SAST application actually is as an Application Type: its defining core, its standard capabilities, its variants, and its boundaries against neighboring Types (DAST/IAST, SCA, Static Code Analysis Platform, Code Quality Platform, Application Security Platform, Vulnerability Management, Secrets Security).

## Initial Boundary

SAST = Static Application Security Testing. Working hypothesis: tools that analyze an application's own code (source or compiled form) **without executing it** to find **security vulnerabilities**, producing findings that developers fix before release.

Easily confused with:

- Static Code Analysis Platform (§12) — same machinery, quality/bug orientation
- Code Quality Platform (§12) — platform layer over analyzers (already processed; recorded a vs-SAST seam)
- DAST / IAST (§15) — runtime testing of the running application
- SCA (§15) — third-party/open-source dependencies, not first-party code
- Application Security Platform (§15, processed) — program layer; left a joint-review flag for the engine leaves
- Vulnerability Management (§15) — org-wide vuln lifecycle, infrastructure-oriented
- Secrets Security (§15) — hardcoded-credential detection as its own Type

## Research Questions

1. What is the object of analysis (source? bytecode? binary?) and is execution ever involved?
2. What is the unit of detection knowledge (rules / queries / checkers) and can users extend it?
3. What is the output unit (finding / alert / flaw / result) and what does it carry (location, severity, flow, guidance)?
4. How do findings get triaged, suppressed, and tracked across scans and code movement?
5. How does SAST embed in the development workflow (IDE, pre-commit, PR/MR, CI/CD, gates)?
6. What policy/compliance machinery exists at portfolio level?
7. Which analysis techniques are definitional vs variant (pattern matching vs dataflow/taint vs cross-file)?
8. Where is the boundary against quality-first static analysis and against runtime testing?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / tier | Evidence tier |
|---|---|---|
| Semgrep (CE + AppSec Platform) | developer-first, OSS engine + commercial platform, pattern+dataflow rules | Tier 1 (docs.semgrep.dev) |
| GitHub Code Scanning / CodeQL | platform-embedded in code hosting; query-language semantic analysis; SARIF interop | Tier 1 (docs.github.com) |
| Veracode Static Analysis | policy-centric cloud platform; **binary/bytecode upload** (no source required) | Tier 1 (docs.veracode.com) |
| Checkmarx One SAST | enterprise SaaS platform; source-based code-graph queries; heavyweight triage | Tier 1 (docs.checkmarx.com) |
| GitLab SAST | platform-embedded in DevOps; multi-analyzer (own Advanced SAST + wrapped OSS engines) | Tier 1 (docs.gitlab.com) |

Dropped: OpenText Fortify (enterprise on-prem classic) — official docs unreachable (opentext.com 444, microfocus.com/documentation 404; 2 attempts each per network rules). Recorded as sourcing limitation; Fortify used only as market context, no claims rest on it.

## Sources

- Semgrep: https://semgrep.dev/docs/ ; https://docs.semgrep.dev/introduction.md ; https://docs.semgrep.dev/learn/security-foundations/sast/overview.md ; https://docs.semgrep.dev/semgrep-ci/findings-ci.md ; https://docs.semgrep.dev/llms.txt (page map)
- GitHub: https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning ; https://docs.github.com/en/code-security/concepts/code-scanning/codeql/codeql-code-scanning ; https://docs.github.com/en/code-security/concepts/code-scanning/code-scanning-alerts ; https://docs.github.com/en/code-security/how-tos/manage-security-alerts/manage-code-scanning-alerts/resolve-alerts
- Veracode: https://docs.veracode.com/ ; https://docs.veracode.com/r/c_static_overview ; https://docs.veracode.com/r/c_appsec_policies
- Checkmarx: https://docs.checkmarx.com/ ; https://docs.checkmarx.com/en/34965-324470-sast-scanner.html ; https://docs.checkmarx.com/en/34965-373312-triaging-sast-results.html
- GitLab: https://docs.gitlab.com/ee/user/application_security/sast/

## Product Observations (evidence layer A = directly observed)

### Semgrep (CE + AppSec Platform)

Key observations (all Tier 1):

- Self-label: "a software security tool that provides static application security testing (SAST), software composition analysis (SCA), and secrets detection. Semgrep identifies vulnerabilities in your source code **without executing your code**."
- SAST product (Semgrep Code) "detects security vulnerabilities in your **first-party code**" — explicit split vs Supply Chain (SCA, dependencies) and Secrets (credentials).
- Rules "encapsulate pattern matching logic and data flow analysis"; out-of-the-box registry rules + community rules + custom rules; rule schema matches code semantically.
- Intraprocedural data-flow engine; taint mode with sources/sinks (its own SAST learning guide: sources = HTTP params/cookies/DB results/file uploads; sinks = SQL exec, exec()/system(), HTML rendering, file I/O, serialization).
- Community Edition = OSS engine + community rules + IDE plugins, 30+ languages; AppSec Platform adds managed scans, Pro rules, SCA, secrets, PR comments, AI triage/remediation.
- Finding identity in CI = 4-tuple (rule ID, file path, syntactic context, index); diff-aware scans show only new findings relative to a baseline commit.
- Platform finding statuses: OPEN / REVIEWING / PROVISIONALLY_IGNORED / FIXING ("To fix") / IGNORED / FIXED; ignore reasons: False positive / Acceptable risk / No time to fix; suppression via `nosemgrep` code comment; triage propagates across branches/refs; "removed findings" concept (rule disabled/updated, file gone, PR closed).
- Delivery surfaces: local CLI, IDE extensions, pre-commit, CI/CD (GitHub Actions/GitLab/Jenkins/CircleCI/Azure/Bitbucket/Buildkite), managed cloud scans, PR/MR comments.
- "No build required for most languages" — explicit positioning vs CodeQL.

### GitHub Code Scanning / CodeQL

Key observations (all Tier 1):

- "Code scanning is a feature that you use to analyze the code in a GitHub repository to find security vulnerabilities and coding errors. Any problems identified by the analysis are shown in your repository."
- CodeQL = "the code analysis engine developed by GitHub to automate security checks"; workflow: generate a CodeQL database representing the codebase → run CodeQL queries → results shown as code scanning alerts. Supports compiled and interpreted languages.
- Third-party tools interoperate via SARIF (open standard) upload; can run in external CI.
- Default setup (auto languages/query suite/triggers) vs advanced setup (workflow file) vs external CI.
- Alerts carry: triggering line, severity (Error/Warning/Note) and security severity (Critical/High/Medium/Low, CVSS-based; computed from CWE-tagged CVE percentiles), when first introduced, fix information (CodeQL).
- Data-flow alerts: "GitHub shows you how data moves through the code"; multiple code paths reaching the same unsafe operation are grouped under a single alert.
- Alert lifecycle: fix the code (alert closes) or dismiss (reason recorded + optional comment; removed from current count; moved to Closed; reopenable; next scan won't regenerate). Bulk dismiss with filters (e.g., by CWE).
- PR surfaces: check results + annotations; branch protection can make "Code scanning results" a required check. Scheduled scans + push-triggered scans.
- Labels for non-application code: Generated / Test / Library / Documentation (path-based categorization).
- Copilot Autofix (suggested fix → PR) and Copilot cloud-agent agentic fixing (current generation).
- Query suites; queries open source; CWE coverage published.

### Veracode Static Analysis

Key observations (all Tier 1):

- Self-label: "Veracode Static Analysis is a Static Application Security Testing (SAST) solution that enables you to quickly identify and remediate application security findings (flaws) in source code. It can analyze major frameworks and languages **without requiring source code**."
- Engine "scans and analyzes the compiled binary code or bytecode of an application uploaded as a packaged artifact"; methodology "creates a complete model of the application's control and data flow from the executable binary. It then tests the model to detect flaw patterns."
- Two solutions: Upload and Scan (full risk assessment; policy scans + development sandboxes; includes SCA) and Pipeline Scan (fast, in-pipeline, not connected to platform; baseline file of known findings; break builds on security thresholds or specific CWEs).
- Packaging: WAR/TAR/ZIP artifacts; prescan verification (validates packaging, identifies top-level modules with entry points); extensive prescan error taxonomy (missing debug info, obfuscated/optimized code, missing entry point, minified JS, etc.).
- Flaws = "security findings in your application code found by static analysis that represent potentially dangerous code paths"; two categories: vulnerabilities (exploitable) vs potential vulnerabilities (unreachable or mitigated today).
- Debug info required to report source file + line; otherwise module/class/function-relative location.
- Policies: assigned to application profiles; constraints = Veracode Level (VL1–VL5, minimum security score), rules (findings that must not exist — OWASP, OWASP Mobile, CWE Top 25, PCI), required scans + frequency, evaluation timeframes, grace periods; status Passed / Did Not Pass / Conditional Pass / Not Assessed (color-coded shield).
- IDE plugins, CI/CD, SCM integrations; Veracode Fix (suggested code patches); one-on-one remediation advice service.
- Data retention rules for uploaded binaries/templates/datapaths (vendor operational detail).

### Checkmarx One SAST

Key observations (all Tier 1):

- "Checkmarx's Static Application Security Testing (SAST) scanner examines your application's code. It looks for common security weaknesses by analyzing the code's structure and how data flows through the application."
- "SAST builds a logical graph of the code's elements and flows **without needing to build or compile** a software project's source code. SAST then queries this internal code graph." "The input to SAST's scanning and analysis is the source code, not binaries... The code doesn't even need to be able to compile and link properly."
- "Hundreds of pre-configured queries for known security vulnerabilities for each programming language"; Query Editor to write custom queries "for security, QA, and business logic purposes"; Presets (query sets; mandatory; default ASA Premium).
- Fast Scan mode (up to 90% faster, fewer flows explored) vs In-Depth mode; Light Queries (subset focused on most exploitable vulnerabilities).
- Incremental scans: scan only code changed since last full scan + "closure"; results merged with base full scan; threshold converts to full scan when breached (default 7% — vendor number, research notes only).
- Triage: each risk instance has a state; initial state **To Verify** ("hasn't been assessed by your AppSec team yet"); states: Not Exploitable / Proposed Not Exploitable / Confirmed / Urgent (+ custom states); note required for Not Exploitable; change log per result; triage permissions (update-result-state-*, update-result-severity); severity primarily CVSS-based, adjustable 0.0–10.0 (Critical/High/Medium/Low/Info bands); results scope project-level vs application-level.
- Similarity ID for grouping similar results; SAST Results Viewer; scan scheduling; SAST is one scanner among many in Checkmarx One (SCA, IaC, Container, API Security, Secrets, AI Supply Chain).
- IDE plugins (Eclipse/JetBrains/VS Code/Visual Studio/Cursor/Windsurf/Kiro), CI/CD plugins (Jenkins/TeamCity/GitHub Actions/Azure DevOps/CLI), PR decorations, Policy Management with break-build, feedback apps (Jira/Azure Boards/GitHub Issues/Slack/Teams/email), SARIF output.

### GitLab SAST

Key observations (all Tier 1):

- "Static application security testing (SAST) discovers vulnerabilities in your source code before they reach production. Integrated directly into your CI/CD pipeline... SAST scans happen automatically with each commit."
- Finding vs vulnerability distinction: "Findings are generated on feature branches. When they are merged into the default branch, they become vulnerabilities."
- Vulnerability details: Description (cause/impact/remediation), Status (triaged/resolved), Severity (six levels), Location (filename + line, opens code view), Scanner (which analyzer), Identifiers (CWE + rule IDs). "SAST vulnerabilities are named according to the primary CWE identifier."
- Surfaces: pipeline Security tab, merge request widget (newly introduced/resolved findings), MR changes view inline annotations, vulnerability report (default branch), downloadable JSON report artifact.
- Multi-analyzer architecture: GitLab Advanced SAST (Ultimate; cross-file, cross-function scanning) + standard analyzers based on open-source scanners (Semgrep-based with GitLab-managed rules, SpotBugs+find-sec-bugs, PMD-Apex, Sobelow, Brakeman, Kubesec for K8s manifests).
- Customization: disable rules / exclude paths via `.gitlab/sast-ruleset.toml` + CI variables; remote ruleset files; enforced scan execution across groups.
- Advanced vulnerability tracking: algorithm tracks "the same vulnerability" as code moves within/between files.
- Automatic vulnerability resolution when a rule is disabled/removed (with comment); reopened if rule re-enabled.
- GitLab Duo false positive detection (confidence scores + explanations) and agentic SAST vulnerability resolution (auto-generated MRs with fixes) — current generation.
- FIPS-enabled scanner images; offline environments.

## Cross-product Comparison

| Dimension | Semgrep | GitHub Code Scanning | Veracode Static | Checkmarx One SAST | GitLab SAST |
|---|---|---|---|---|---|
| Object of analysis | first-party source | codebase → CodeQL database | compiled binary/bytecode | source (no build needed) | source (some analyzers compile, e.g. SpotBugs) |
| Execution involved | never | never | never | never | never |
| Detection knowledge | rules (pattern + dataflow/taint) | CodeQL queries (+ third-party via SARIF) | engine flaw patterns over control/data-flow model | queries over internal code graph | managed rules + OSS analyzer rules |
| Custom detection | custom rules (YAML schema) | own queries / query packs | (engine-side; not user-authored in docs fetched) | Query Editor + presets | ruleset customization (disable/replace/add) |
| Output unit | finding | alert | flaw | result / risk instance | finding → vulnerability |
| Location | file path + syntactic context | file + line | file + line (needs debug info) | file + line | file + line |
| Weakness classification | rule IDs | CWE coverage; security severity | CWE-based rules (OWASP/CWE Top 25/PCI) | CVSS-based severity; query IDs | primary CWE identifier names the vulnerability |
| Severity model | rule severity | Error/Warning/Note + CVSS security severity | CVSS-derived; VL scoring | CVSS-based, adjustable 0–10 | six levels |
| Data-flow evidence | taint mode (sources/sinks) | data-flow alerts, paths grouped | control/data-flow model; datapath | code graph flows | Advanced SAST cross-file/cross-function |
| Triage states | OPEN/REVIEWING/PROVISIONALLY_IGNORED/FIXING/IGNORED/FIXED | open → fixed / dismissed (+reason, reopen) | platform review + mitigation | To Verify → Not Exploitable/Proposed Not Exploitable/Confirmed/Urgent (+custom) | status in vulnerability report (triaged/resolved) |
| Suppression | nosemgrep comment; ignore reasons | dismissal with reason + comment | (mitigation workflow) | Not Exploitable + mandatory note | rule disable; path exclusion |
| Cross-scan tracking | 4-tuple identity; diff-aware baseline | alert persists; fixed-in-branch semantics | datapath retention; baseline file (Pipeline) | similarity ID; incremental merge | advanced vulnerability tracking |
| Dev-workflow surfaces | CLI, IDE, pre-commit, CI, PR comments, managed scans | repo security tab, PR checks/annotations, API/webhooks | platform, IDE, CI/CD, SCM | platform viewers, IDE plugins, CI plugins, PR decorations | pipeline security tab, MR widget/annotations, vulnerability report |
| Gates | org policies, PR comments | required check (branch protection) | policy pass/fail (VL, grace periods) | break-build policy | scan enforcement, MR approvals |
| Portfolio reporting | platform dashboards | security overview, org API | policy compliance, analytics, reports | dashboards, reports, ASPM layer | security dashboard, vulnerability report |
| Adjacent capabilities bundled | SCA, Secrets | (secret scanning as separate feature) | SCA, containers/IaC/secrets, DAST, EASM | SCA, IaC, Container, API Sec, Secrets | dependency scanning, IaC, secret detection, DAST, fuzzing |

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **Static analysis of the application's own code without executing it.** The object of analysis is the codebase itself — source code or the application's own compiled form (bytecode/binary). The test never runs the application. Remove → DAST/IAST territory (runtime testing) or manual secure code review.
2. **Security-oriented detection knowledge.** The analysis is driven by packaged detection knowledge — rules, queries, or checkers — that encodes vulnerability classes (injection, XSS, insecure crypto, hardcoded credentials, dangerous APIs...). Remove → general static analysis / linter (bugs, smells, style).
3. **Vulnerability findings located in the code.** The output is a set of findings, each locating a potential weakness at a code location, identifying the weakness class, commonly carrying severity and remediation guidance, actionable by developers. Remove → a grade/score without locations, or runtime scan output.

Jointly-held load-bearing:

- 1 alone (no security orientation) = general static analysis / code quality
- 2 alone (no code analysis) = vulnerability knowledge base / secure-coding checklist
- 3 alone (no static analysis) = manual code-review / pentest report
- 1+2 without 3 = analysis machinery with no consumable findings
- 2+3 without 1 = runtime or manual findings, not static
- 1+3 without 2 = ad-hoc pattern grep, not a managed testing capability

### L1 — Common Mature Structure

- The scan as the unit of work over a codebase snapshot; full scans plus incremental/baseline/diff-aware modes
- Finding identity and tracking across scans and code movement (similarity/tracking; new-vs-known findings)
- Triage lifecycle with states (unreviewed → confirmed / not exploitable / dismissed / fixed) with recorded reasons/notes and permissions
- Suppression machinery (inline comments, rule disabling, path exclusions) with audit trail
- Severity model (commonly CVSS-derived) + weakness classification (CWE/OWASP-style identifiers)
- Remediation guidance; suggested/auto fixes (current generation)
- CI/CD integration; PR/MR surfaces (annotations, comments, checks); gates (required check / break build / policy pass-fail)
- IDE plugins and local scanning
- Dashboards, reports, exports (SARIF / JSON / CSV)
- Policy/compliance evaluation at portfolio level
- Custom rule authoring / ruleset customization

### L2 — Variant / Optional Structure

- Input form: source code vs compiled binary/bytecode (Veracode pole vs Checkmarx "no build needed" pole)
- Analysis technique: pattern matching vs intraprocedural dataflow/taint vs cross-file/cross-function (GitLab Advanced SAST names this explicitly)
- Delivery: OSS CLI, on-prem engine, SaaS platform, platform-embedded in code hosting/DevOps
- Posture: standalone engine vs module inside an AppSec platform/suite
- Language breadth (varies widely; some engines need builds, some don't)
- Scan depth modes (fast vs in-depth), light query subsets
- AI-assisted triage / false-positive detection / agentic fixing
- Bundled adjacent capabilities (secrets, IaC, SCA, containers) — packaging, not identity

### L3 — Vendor-specific (research notes only)

- Semgrep: rule schema, `nosemgrep` comment, 4-tuple finding identity, CE-vs-Pro split, Multimodal autotriage
- GitHub: CodeQL database/query language, SARIF ingestion, configurations, Copilot Autofix/agentic sessions, security-severity-from-CVE-percentile calculation
- Veracode: packaged artifacts/prescan/top-level modules, sandbox vs policy scans, Veracode Levels VL1–VL5, shields, retention windows (45/60/90 days), Pipeline Scan baseline files
- Checkmarx: Query Editor/presets (ASA Premium default), Fast Scan/In-Depth, Light Queries, incremental threshold default, similarity ID, To Verify state names, project-vs-application triage scope
- GitLab: `.gitlab/sast-ruleset.toml`, analyzer fleet (semgrep/spotbugs/pmd-apex/sobelow/brakeman/kubesec), findings→vulnerabilities promotion on merge, Duo false-positive detection, FIPS images

## Vendor-specific Findings

- Veracode is the only sampled product whose primary input is compiled binary/bytecode rather than source; Checkmarx explicitly states source input with no build/compile requirement; GitLab's SpotBugs analyzer compiles code as a step. Input form is a variant axis, not definitional.
- GitHub's security-severity calculation (75th percentile of CVSS across CWE-tagged CVEs) is a vendor-specific methodology.
- Checkmarx's default incremental threshold (7%) and Veracode's retention windows are precise vendor numbers — kept out of the final document.
- GitLab's findings→vulnerabilities promotion at merge to default branch is a platform-specific lifecycle realization of the general "new findings vs backlog" concept.

## Boundary Findings

- **vs Static Code Analysis Platform (§12, unprocessed)** — same static-analysis machinery; the seam is detection orientation and consuming program: SAST findings are security weaknesses consumed by an AppSec workflow; static code analysis findings are bugs/smells/style consumed by a code-quality workflow. Many products serve both (Semgrep explicitly does both; SonarQube-class products bundle a security axis). Record as boundary note for the unprocessed sibling; recommend the "security-first vs quality-first orientation" seam.
- **vs Code Quality Platform (§12, processed)** — that pass recorded "vs SAST (security as one bundled axis vs security-first)". Confirmed from this side. Also: a code-quality platform wraps analyzers (its own core model), and GitLab demonstrates a DevOps platform wrapping SAST engines (Semgrep-based analyzer) — engine layer vs platform layer holds in both directions.
- **vs DAST / IAST (§15, unprocessed)** — static (code not executed) vs dynamic (running application) vs instrumented runtime. Vendor-documented separateness: Veracode sells Static and Dynamic as separate products; GitLab has separate SAST and DAST features; Checkmarx One has separate scanners. Complementary, different Types.
- **vs SCA (§15, unprocessed)** — first-party code vs third-party dependencies. Vendor-documented split at every sampled suite: Semgrep Code vs Supply Chain; Veracode Static vs SCA; Checkmarx SAST vs SCA scanners; GitLab SAST vs Dependency Scanning.
- **vs Application Security Platform (§15, processed)** — DISCHARGES that pass's joint-review flag from this side: keep-both RATIFIED on the capability-layer vs program-layer seam. The same vendor products substantiate both leaves depending on the surface described (Checkmarx One SAST scanner = engine inside the Checkmarx One platform; Veracode Static Analysis = engine inside the Veracode platform). SAST documents the testing capability; application-security-platform documents application records + finding lifecycle + policy/gates + portfolio management.
- **vs Vulnerability Management (§15, unprocessed)** — SAST produces code-level findings; VM owns the org-wide vulnerability lifecycle (infrastructure-inclusive). Semgrep's own docs mention exporting findings to vulnerability management systems — hand-off, not identity.
- **vs Secrets Security (§15, unprocessed)** — hardcoded-secret detection ships inside SAST products (Semgrep Secrets, Checkmarx Secret Detection, GitLab secret detection) but is a distinct Type; SAST's vulnerability classes include hardcoded credentials as one class among many.
- **vs Code Review Platform (§12, processed)** — SAST findings surface in PR/MR as annotations/checks, but the human review of proposed changes is a different Type; SAST is an automated checker feeding that surface.
- **vs Debugger / Profiler (§12, processed)** — static vs dynamic execution analysis; the profiler pass already used "static analyzer" as its removal test; consistent.

## Historical / Market-Sample Check

Would older, regional, or platform-native products still fit the L0?

- Early-2000s open-source scanners (Flawfinder-class; ITS4/RATS lineage) scan C/C++ source for dangerous function calls and report security findings with locations — no taint analysis, no CI integration, no platform, no cloud. They satisfy L0 legs 1–3. → pattern matching is a technique variant, not definitional; platform/triage machinery is L1.
- Fortify (2003+ enterprise generation, on-prem engine + audit client) fits the same core (docs unreachable this pass — held as market context only).
- Platform-native realizations (GitHub code scanning inside a hosting platform; GitLab SAST inside a DevOps platform) fit — delivery surface is a variant.
- Binary-input SAST (Veracode) fits — input form is a variant.
- Conclusion: L0 holds across eras and delivery forms; no era machinery (cloud, CI, AI, SARIF, CVSS) is definitional.

## Uncertainties

- Fortify official docs unreachable (2×2 failures) — the enterprise on-prem classic is held as market context only; no claims rest on it. If a later pass needs Fortify specifics, re-fetch docs.opentext.com.
- Custom-rule authoring depth at Veracode was not confirmed from fetched pages (engine-side rules not user-documented in the fetched set) — custom detection is held as L1 "common", not universal.
- Exact triage-state vocabularies differ per product; the final document uses conceptual states, not vendor labels.
- Whether "policy gate" is universal: all five sampled products have some gate/policy surface, but bare OSS engines (Flawfinder-class) do not — held L1, not L0.
- IAST interaction (hybrid SAST+IAST runtimes) not researched this pass — left to the DAST/IAST leaf.

## Final Synthesis

SAST is the security-testing capability that analyzes an application's own code without executing it, driven by packaged security detection knowledge, and outputs located, classified, actionable vulnerability findings for developers to fix before release. The defining core is exactly the three legs above; everything else — scan modes, triage platforms, CI gates, policies, IDE plugins, AI fixes — is mature market structure layered on that core, and the input form (source vs binary), technique (pattern vs dataflow), and delivery (CLI vs platform-embedded) are variant axes. The Type sits between quality-first static analysis (different orientation, same machinery) and runtime testing (DAST/IAST/SCA — different object), and feeds the application-security program layer rather than being that layer.
