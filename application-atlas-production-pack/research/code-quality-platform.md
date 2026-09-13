# Research Notes — Code Quality Platform

Research date: 2026-09-07

## Research Goal

Understand what a **Code Quality Platform** actually is as an Application Type: its defining structure, how it works day-to-day, where its boundaries run against neighboring Types (Static Code Analysis Platform, SAST, Code Review Platform, CI), and which structures are definitional versus merely common in the current market.

## Initial Boundary (hypothesis before research)

- Core guess: a platform that continuously analyzes a codebase, maintains a persistent quality state (findings + metrics + history), and enforces/exposes a quality standard through gates in the delivery workflow.
- Likely confusion points:
  - **Static Code Analysis Platform** — a sibling leaf in the same directory; the analyzer engine itself vs. the platform layer.
  - **SAST** — security-first static analysis; quality platforms commonly bundle a security axis.
  - **Code Review Platform** — human review conversation; quality platform supplies automated checks to it.
  - **CI** — executes pipelines; the quality platform is triggered by / reports into CI.
  - **Engineering Productivity Analytics** — measures people/flow, not code health.
- Unknowns going in: is the quality gate definitional or just the dominant modern implementation? Is the "new code vs overall code" split definitional? Is coverage ingestion definitional? Does the enterprise portfolio layer matter at Type level?

## Research Questions

1. What objects exist inside such a system? (project, branch, PR, issue, metric, rating, rule set, gate…)
2. How do analysis runs get triggered, and what does the platform record?
3. What exactly is a quality gate, and what happens when it fails?
4. How are findings (issues) managed over their life (assignment, disposition, resolution)?
5. What metrics/ratings vocabulary does the market use?
6. How do org/enterprise layers work (policies, portfolios, reporting)?
7. What is delivered by the platform vs. by external analyzers/CI/test tooling?
8. What distinguishes this Type from a bare static analyzer, from SAST, and from code review?

## Representative Products

| Product | Posture | Why selected |
|---|---|---|
| SonarQube Server + SonarQube Cloud (Sonar) | self-managed server + SaaS + IDE companion; category-defining | market leader; richest concept vocabulary (quality profile, quality gate, new code) |
| Codacy | SaaS-first + self-hosted (Kubernetes) | Git-provider-native org model; org-level gate policies |
| DeepSource | SaaS-native, developer-workflow-first | analyzer auto-detection, autofix/formatters posture |
| Qlty (from the makers of Code Climate) | cloud "Code Health Platform"; grade-based philosophy | letter-grade ratings heritage (first cloud code quality platform, 2011); CLI/plugin wrapping of third-party analyzers |

Coverage: different philosophies (standards/gates vs. grades vs. autofix), different customer tiers (enterprise self-managed → SMB SaaS), cloud vs self-hosted.

## Sources

All fetched 2026-09-07 (Tier-1 official documentation):

- SonarQube Server readme: https://docs.sonarsource.com/sonarqube-server/readme.md
- SonarQube Server — Pull request analysis: https://docs.sonarsource.com/sonarqube-server/discovering/code-analysis/pull-request-analysis.md
- SonarQube Server — Managing issues (introduction): https://docs.sonarsource.com/sonarqube-server/user-guide/issues/introduction.md
- SonarQube Cloud — Quality gates: https://docs.sonarsource.com/sonarqube-cloud/standards/quality-gates.md
- SonarQube Cloud — Quality standards and new code: https://docs.sonarsource.com/sonarqube-cloud/standards/about-new-code.md
- SonarQube Cloud — Measures and metrics: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/metric-definitions.md
- Codacy docs home: https://docs.codacy.com/
- Codacy — Quickstart: https://docs.codacy.com/getting-started/codacy-quickstart/
- Codacy — Adjusting quality gates: https://docs.codacy.com/repositories-configure/adjusting-quality-gates/
- Codacy — Using gate policies: https://docs.codacy.com/organizations/using-gate-policies/
- DeepSource — Quickstart: https://docs.deepsource.com/docs/platform/getting-started
- DeepSource — Configure analyzers: https://docs.deepsource.com/docs/platform/getting-started/configure-analyzers
- Qlty — What is Qlty (docs.codeclimate.com → docs.qlty.sh): https://docs.qlty.sh/
- Qlty — Quality Gates: https://docs.qlty.sh/cloud/gates.md
- Qlty — Maintainability Metrics and Ratings: https://docs.qlty.sh/cloud/maintainability/metrics.md

Notes on access: Sonar quality-gates page URL guessing failed twice before locating via sitemap (no content loss). Qlty at docs.qlty.io timed out twice (abandoned); docs.codeclimate.com redirected to docs.qlty.sh and worked. Codacy older paths 404'd; new mkdocs structure worked.

## Product Observations

### SonarQube (Server + Cloud) — evidence layer A (directly observed)

- Positioning (Server readme): "automated code review and static analysis tool", checks code "against an extensive set of rules" covering maintainability, reliability, security "on each merge/pull request". Delivery: SonarQube Server (self-managed), SonarQube Cloud (SaaS), SonarQube for IDE (companion plugin in Connected Mode).
- Analysis intake: scanners integrate with CI pipeline; analysis runs on branches and pull requests. Activity page "displays a history of analyses performed on your project" — measures evolution + events (quality gate status changes, quality profile updates).
- **Quality profile**: per-language set of rules applied during analysis; built-in "Sonar way" profile designed for most projects. (Cloud standards pages.)
- **Quality gate**: "an indicator that tells you whether your code meets the minimum level of quality required"; a set of **conditions applied to the results of each analysis**; **Passed / Failed** (or Not computed). Displayed in the product and as **pull request decoration** in the DevOps platform. Quality gate history "helps you monitor guardrails adherence… over time". Default gate is "Sonar way"; custom gates need Administer Quality Gates permission; default gate auto-applied to new projects.
- **New code definition**: previous version / number of days / specific version / specific date; configurable at organization and project level (org default applies to new projects; project-level precedence). Metrics computed for **overall code** and **new code** separately. Built-in "Sonar way" gate conditions apply to new code only.
- **Three-stage model**: IDE (fix as introduced) → PR analysis (all code to be merged clean) → branch analysis (main branch ready for release).
- PR analysis: only issues **introduced by the pull request** are reported; gate uses new-code conditions; results reported to the DevOps platform (decoration, inline annotations); issue attributes synchronized between PR and target branch. Gate not computed after only one analysis.
- **Issues**: raised when a coding rule is broken; severity inherited from rule; auto-assigned to last committer of the line (if correlatable), reassignable; primary + secondary locations; lifecycle statuses incl. **Accepted** (fix later), **False positive**, reopen; tagging, comments, notifications; code-level resolution (`sonar-resolve`) for C/C++/Obj-C; fix suggestions (AI) in PRs; Jira work-item creation.
- **Metrics vocabulary** (Measures page + Web API): software-quality issue counts and worst-severity (security/reliability/maintainability) + letter **ratings A–E** per quality; security **hotspots** count + % reviewed + review rating; coverage (line/condition/new), uncovered lines, unit-test stats; duplicated lines density/blocks; size (LOC, ncloc, statements, functions, classes, files, comment density); **cyclomatic** and **cognitive** complexity; **technical debt** (sum of remediation effort minutes; 8-hour day display) and **technical debt ratio** with maintainability rating grid (A ≤5% … E ≥50%); issue density; quality gate status metrics. Deprecated bug/vulnerability/code-smell type vocabulary noted.
- **Enterprise**: portfolios (aggregate view of projects' metrics and risks), portfolio dashboards + PDF reports, project regulatory reports, org-level quality-standard management.
- Advanced Security (SCA) metrics + SBOM export + dependency risk (plan-level product).
- Deployment: server self-managed; cloud SaaS; pricing plans gate features (portfolios, Advanced Security).

### Codacy — evidence layer A

- Positioning (quickstart): "an automated code quality and coverage platform that analyzes your source code and identifies issues as you go"; 40+ languages; "protects your codebase from unwelcome changes".
- Onboarding: sign up **with a Git provider** (GitHub/GitLab/Bitbucket); organizations mirror Git-provider orgs; adding a repository triggers an **initial analysis** and sets up analysis of subsequent commits.
- **Metrics monitored** "from organization and repository level to individual files, pull requests, and commits": **Issues** (violations of a rule/standard/convention/best practice), **Complexity** (execution paths), **Duplication**, **Coverage** (lines covered by automated tests).
- Repository surfaces: Repository Dashboard, Commits page, Files page, Issues page, Coverage page, Pull Requests page.
- **Quality gates** (repo Settings > Gates): New issues are over (≥ severity), New security issues are over, Complexity is over, Duplication is over, **Coverage variation is under**, **Diff coverage is under**. Result: metrics colored on the PR/commit "quality overview" and a **pull request status reported to the Git provider**, "optionally block merging pull requests that aren't up to standards".
- **Gate policies** (org level): built-in **Codacy Gate Policy** applied by default to newly added repositories; org can create custom policies, set one default, apply to selected repositories; removing a policy **restores the repository's previous quality gates**; built-in policy cannot be edited/deleted.
- Configuration: **code patterns** (rules) per repo; per-language configuration; ignore files; `.codacy` configuration file; **client-side tools** for local analysis (ESLint, SpotBugs, Dart analyzer, deadcode, aligncheck); coverage reporter CLI (multiple run modes, troubleshooting docs); badges; API (metrics for files/directories, current issues, coverage gaps, **DAST result uploads**, DAST scan triggering); IDE integrations (VS Code, IntelliJ).
- Org layer: organizations, **segments**, reporting (org overview, issues metrics, Codacy usage), coding standards, **AI Risk Hub**, security & risk management, people management, audit logs, roles from Git-provider permissions.
- Deployment: Cloud (latest) + **Self-hosted** (Kubernetes chart, licensing, upgrades); Enterprise Cloud (GitHub Enterprise Cloud).
- FAQ evidence: metrics calculated (incl. duplication caveats), analysis limits, status-check bypass possible, reanalysis, file-size ceiling (150 KB) — precise figures kept here only.

### DeepSource — evidence layer A

- Positioning: "runs a full review and shows you bugs, security issues, and anti-patterns"; PR-centric ("pick a pull request… DeepSource runs its analysis on your pull request and creates a **baseline** for the repository").
- Onboarding: team via Git provider (GitHub/GitLab/Bitbucket/Azure DevOps); **auto-detects languages and suggests analyzers**; feature selection (code review, security scanning, coverage tracking).
- **Analyzers**: enabled per repo; per-analyzer settings (cyclomatic complexity threshold: low→critical; runtime/language version; doc-coverage exclusions); `.deepsource.toml` committed to the **default branch** required for analysis activation.
- **Issues flow**: results as PR comments + dashboard breakdown of "issues, metrics, and recommendations"; **Autofix** (automated fixes, branded); **code formatters** auto-format PRs; secrets detection toggled per repo, "fails the check if a secret is found".
- Codebase context: test-file and excluded-file glob patterns to reduce false positives.
- Adjacent modules: code coverage tracking (test-coverage docs), dependency vulnerability scanning, license compliance enforcement, CLI usable with AI agents.

### Qlty (Code Climate heritage) — evidence layer A

- Positioning: "next generation, cloud-based **Code Health Platform**… take control of technical debt"; "Qlty is from the makers of Code Climate, who built the **first cloud-based code quality platform in 2011**".
- Problems framed: slow code reviews → automated code review; **noisy static analysis** → "Qlty focuses on *newly introduced* issues… Pre-existing issues are available to browse and fix whenever you're ready"; tool sprawl → linting + SAST + IaC scanning + coverage in one; hidden technical debt → "clear answers about status and trends".
- Flow: open PR → analyze changes → "automated code review comments for newly introduced issues" in the PR → **"Configurable Quality Gates evaluate the mergeability of the change in a simple go/no-go status"** → preventing new quality issues from merging improves the codebase over time. Runs in cloud "without needing to run static analysis on your CI system"; simple **coverage uploader**.
- **Quality gates** (GitHub commit statuses): **Qlty Gate** (go/no-go from analysis; configurable to consider new issues, vulnerabilities, file maintainability), **Qlty Coverage** (fail if coverage decreases vs base branch), **Qlty Diff Coverage** (fail if modified-code coverage below threshold).
- **Metrics**: lines of code; issues (incl. lint results from **plugins wrapping third-party analyzers** — ESLint, Semgrep, Clippy) with **levels** high/medium/low and **effort** (minutes) for smells; code smells (Duplication + Structure categories); cognitive complexity (primary) + cyclomatic; duplication %; **technical debt** (sum of remediation effort) and **technical debt ratio** (vs COCOMO-estimated rewrite effort).
- **Ratings** at project/directory/file level: maintainability **letter grade A–F** from technical-debt-ratio bands (A <5% … F ≥50%); coverage letter grade (A ≥90% … F <60%); duplication %; T-shirt **size rating** (XS–XL). API exposes metric **series** (time series per metric) for projects/components.

## Cross-product Comparison

| Structure | Sonar | Codacy | DeepSource | Qlty | Verdict |
|---|---|---|---|---|---|
| Analysis runs triggered by repo events (commit/PR) + recorded | ✓ (branch/PR analysis, Activity history) | ✓ (initial + per-commit analysis) | ✓ (PR review + baseline) | ✓ (PR analysis) | universal (B) |
| Persistent platform-side state: issues + metrics kept over time with history/trends | ✓ (Activity, Measures, gate history) | ✓ (dashboards, issues, coverage pages) | ✓ (dashboard, baseline) | ✓ (metric series API, trends) | universal (B) — the *platform* is the system of record |
| Findings as managed issue records bound to code locations, with dispositions | ✓ (assign/Accepted/False positive/tags/comments) | ✓ (Issues page; pattern config; ignores) | ✓ (PR comments + dashboard; autofix) | ✓ (issues w/ levels; pre-existing browsable) | universal (B) |
| Configurable quality standard: rule set (own engines + third-party analyzers) | ✓ (quality profiles; Sonar way) | ✓ (code patterns; client-side tools; config file) | ✓ (analyzers + .deepsource.toml) | ✓ (plugins wrapping ESLint/Semgrep/Clippy) | universal (B) |
| Go/no-go **quality gate** evaluated per analysis, surfaced as status in the delivery workflow | ✓ (Passed/Failed; PR decoration) | ✓ (PR status on Git provider) | ✓ (PR checks; secrets check fails) | ✓ (commit statuses) | universal (B) |
| Gate can optionally **block** merge / fail pipeline | ✓ (via CI wiring; Terraform run tasks, Jenkins pause docs) | ✓ ("optionally block merging") | ✓ (checks gate PRs) | ✓ ("evaluate the mergeability") | common (B) — enforcement optional, verdict definitional |
| **New-code orientation** (gate/reporting on introduced changes; diff coverage; overall-vs-new split) | ✓ (new code definition; Sonar way gate = new-code conditions) | ✓ ("New issues…", diff coverage gates) | ✓ (PR + baseline framing) | ✓ ("newly introduced issues" focus) | near-universal modern posture (B) → L1, not definitional |
| Ratings/grades aggregating metrics | ✓ (A–E per quality, debt-ratio grid) | ✓ (grades on metrics; quality goals) | ✓ (metrics + recommendations) | ✓ (A–F grades, T-shirt size) | common (B) — form varies |
| Coverage ingestion (uploader/reporter, not running tests) | ✓ | ✓ (Coverage Reporter) | ✓ (coverage tracking) | ✓ (uploader, diff coverage) | common (B) |
| Duplication + complexity metrics | ✓ (both, + cognitive) | ✓ (both) | ✓ (thresholds per analyzer) | ✓ (cognitive + cyclomatic) | common (B) |
| Security as bundled axis (hotspots/SCA/secrets) | ✓ (hotspots, Advanced Security) | ✓ (security issues, AI Risk Hub, DAST upload) | ✓ (vuln scanning, secrets) | ✓ (SAST, vulnerabilities in gate) | common module (B) — not definitional |
| Org layer: org-level policy application to repos | ✓ (org-level new-code/gate defaults) | ✓ (gate policies default) | team-level feature selection | ✓ (org plans) | common (B) |
| Enterprise portfolio/reporting over many repos | ✓ (portfolios, PDF/regulatory reports) | ✓ (org overview, segments, reports) | — (not observed in fetched pages) | — (org plans; API metric series) | common/optional (A/B) |
| Self-hosted deployment option | ✓ (Server) | ✓ (Self-hosted K8s) | — (SaaS) | — (cloud; CLI local) | variant |
| IDE companion in connected mode | ✓ (Connected Mode) | ✓ (IDE integrations) | ✓ (CLI w/ AI agents; docs mention) | ✓ (CLI) | common/optional |
| AI assistance (fix suggestions, autofix, risk) | ✓ (fix suggestions) | ✓ (Codacy AI) | ✓ (Autofix) | — (not observed in fetched pages) | era-common (B) |

## Canonical Abstraction

### L0 — Defining Invariant

Minimal structure without which the product stops being recognizable as a Code Quality Platform:

1. **Recorded analysis runs over a managed project's code** — the platform ingests/produces analysis results (its own engines and/or third-party analyzers) each time the project's code changes (commit/push/PR) and on initial onboarding.
2. **Persistent quality state held platform-side** — findings (issues) and measures (metrics) for the project/branch are stored and maintained over time, with history; the platform — not a one-off local tool run — is the system of record for code health.
3. **A configurable quality standard** — a maintained definition of what "good" means for this code: which rules/patterns to apply and/or which thresholds the measures must meet.
4. **A quality verdict surfaced in the delivery workflow** — evaluation of analysis results against the standard, reported as a user-visible pass/fail (gate/check/status) attached to the change (PR/commit/branch), which the team uses in merge/release decisions. (The *enforcement* — blocking merge or failing the pipeline — is a common optional wiring, not the invariant.)

Test against §24 (historical/market-sample check):
- Sonar's pre-"quality-gate" era used threshold **alerts** on dashboards — still satisfies #4 (visible verdict against thresholds). Code Climate 2011 grades satisfied it as letter-grade verdicts + badges.
- Bare analyzers (Checkstyle/ESLint/PMD/FxCop-class tools, historical or current) fail #2 and #4 — they produce findings for a run but hold no platform state, history, standard, or verdict. This confirms they belong to the analyzer layer (Static Code Analysis), not this Type.
- The new-code/PR orientation and PR decoration are modern postures (L1), NOT required: a branch-analysis-plus-dashboard product with threshold alerts still qualifies.

### L1 — Common Mature Structure

- **New-code orientation** as the dominant modern philosophy: gates/reporting focus on issues *introduced* by the change (new-code definitions, diff coverage, baseline-vs-new), with overall-code metrics kept alongside.
- Issue lifecycle management: auto-assignment to the author/committer, dispositions (accepted/won't-fix, false positive), tags/comments, reopen on recurrence, suppression tracking.
- Metrics vocabulary shared across market: issues by severity, duplication, complexity (cyclomatic and/or cognitive), size (LOC), test coverage, technical debt/effort estimates.
- Ratings/grades aggregating metrics into at-a-glance assessments (letter grades or scores), at project/file/directory levels.
- Coverage ingestion via uploader/reporter (the platform consumes coverage reports produced by test tooling; it does not run the tests).
- PR/commit reporting into the DevOps platform: status checks, PR decoration, inline comments.
- Branch + PR analysis modes; analysis activity history; trend views; quality-gate history.
- Integrations: CI-based analysis (scanner/CLI), Git-provider connections, badges, API/webhooks.
- Organizational layer: org-level default policies applied to new repositories; org dashboards; multi-repo reporting.
- Deployment duality: cloud SaaS and/or self-managed server.
- AI-era additions: fix suggestions, autofix, AI risk surfaces (era-common, not definitional).

### L2 — Variant / Optional Structure

- Bundled security axis: security hotspot review flows, SCA/dependency risk, secrets detection, license compliance, IaC scanning, DAST-result ingestion — common modules, but security-*first* products are SAST/SCA Types.
- Code transformation: auto-formatters/transformers applied to PRs; autofix engines.
- Language breadth (20–40+ languages), IaC/platform coverage, monorepo support.
- Enterprise packaging: portfolios, segments, regulatory/PDF reports, usage analytics, plan-gated features.
- Self-hosted form (server VM or Kubernetes chart).
- IDE companion in connected mode; CLI for local runs.
- Public-repo free tiers, badges as public signals.

### L3 — Vendor-specific (research notes only)

- Sonar: "Sonar way" profile/gate names; new-code definition options (previous version / N days / specific version / specific date); technical-debt-ratio rating grids (A ≤5%…E ≥50%); 8-hour-day display assumption; security hotspots concept; Sandbox triage; `sonar-resolve`; Connected Mode; Remediation Agent; "7 million developers" claim; Cyclomatic/Cognitive complexity definitions per language; duplicated-block token thresholds (100 tokens/10 lines, Java 10 statements); coverage formula `(CT+LC)/(B+EL)`.
- Codacy: built-in "Codacy Gate Policy" (non-editable/non-deletable); gate semantics incl. the coverage-variation margin tip (−0.10%); policy removal restores previous repo gates; 150 KB file ceiling; segments; AI Risk Hub; Guardrails; client-side tools list (aligncheck, deadcode, SpotBugs…); DAST upload/trigger API; Self-hosted chart/K8s ops; Enterprise Cloud.
- Qlty: T-shirt size bands (XS <1k … XL >500k LOC); COCOMO-based rewrite estimate for tech-debt ratio; coverage grade bands (A ≥90%…F <60%); plugin wrapping of ESLint/Semgrep/Clippy; "first cloud code quality platform 2011" heritage; `qlty smells` CLI.
- DeepSource: `Autofix™`; `.deepsource.toml` must be on the default branch; complexity-threshold vocabulary (low→critical); transformers/formatters; CLI-with-AI-agents positioning.

## Rejected Findings (considered, not promoted)

- "Quality platform = SaaS" — rejected; self-managed server products are central to the market.
- "Gate must block merges" — rejected; blocking is optional wiring in every observed product; the verdict is the invariant.
- "New-code orientation is definitional" — rejected; it is the dominant modern philosophy but the historical form (threshold alerts on overall code) is still the same Type.
- "Coverage tracking is definitional" — rejected; one sampled pole (DeepSource) treats coverage as an optional feature toggle, and coverage is supplied by external test tooling in all products.
- "A platform runs its own analyzers only" — rejected; wrapping third-party analyzers (Codacy client-side tools, Qlty plugins, DeepSource analyzer catalog incl. third-party tools) is an established pattern.
- "Letter grades are the market's rating form" — rejected; Sonar uses A–E on multiple axes + debt ratio; Codacy mixes grades and goals; grades are one implementation of "aggregated rating".

## Boundary Findings

| Neighbor Type | Relationship | Distinction — what to remove/shift to become the other Type |
|---|---|---|
| Static Code Analysis Platform (directory sibling) | heavy overlap; the engine layer vs the platform layer | Remove persistent platform state + history + standard + verdict → a run-only analyzer (report findings for a run; Checkstyle/ESLint/PMD-class, deep analyzers). Many products are *both* (they embed engines). The seam drawn here: **state-over-time + standard + verdict = platform**. Taxonomy note recorded: these two leaves need joint review; as separate Types they must be defined at different layers (engine vs system-of-record). |
| SAST | adjacent module / distinct Type | Shift the subject from code health (all qualities) to security vulnerabilities/attack surface, with security-only rule semantics and exploit-oriented triage → SAST. Quality platforms treat security as one bundled axis; SAST products center it. |
| Code Review Platform | complementary | Remove automated analysis; make the human PR conversation the subject (review requests, approvals, discussion threads) → Code Review Platform. The quality platform feeds checks *into* that flow. |
| Continuous Integration Platform | complementary | Remove quality semantics; orchestrate builds/pipelines as the subject → CI. The quality platform is typically *triggered by* CI and reports results back (gate webhooks, pipeline pause), but does not orchestrate builds. |
| Test Automation / coverage tooling | data supplier | The platform ingests coverage reports; it does not author, run, or manage tests. |
| Dependency Management / SCA | optional module | Dependency/license risk appears here as a bundled axis; the dedicated Type centers the dependency graph itself. |
| Error Tracking Platform | different object | Runtime failures/exceptions in production vs. source-code quality measured before merge. |
| Engineering Productivity Analytics | different subject | Measures delivery flow and people throughput; the quality platform measures the health of the code itself. |

## Uncertainties

- Codacy/DeepSource portfolio-level aggregation depth beyond org dashboards was not directly observed in fetched pages (plan-dependent features); kept out of the final document's strong claims.
- Qlty org/enterprise layer evidence is thin (org plans referenced but not detailed); treated structurally only.
- Historical details of pre-2013 Sonar "alerts" come from product-name evolution knowledge, not fetched pages — used only as a reasoning aid for the L0 verdict concept, not as a citable claim.
- Exact enforcement mechanics (which CI systems fail pipelines on gate failure) verified for Sonar (Jenkins pause, Azure DevOps release gate, Terraform run tasks) and asserted only softly elsewhere.

## Final Synthesis

A Code Quality Platform is the **continuous, stateful layer between code analysis engines and the delivery workflow**: it records analysis runs on a managed project's code, maintains a persistent quality state (issues + metrics + history), holds a configurable quality standard (rules and/or thresholds), and renders a pass/fail verdict into the merge/release flow. The dominant modern implementation philosophy orients everything at *newly introduced* issues ("clean as you write"), with overall-code state retained as the debt picture. Bare analyzers supply findings; CI triggers runs; test tooling supplies coverage; code review platforms receive the checks — but none of them are the system of record for code health. That system-of-record role, plus the standard and the verdict, is what defines this Type.
