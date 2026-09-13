# Code Quality Platform

## Overview

A **Code Quality Platform** is the system of record for the health of a codebase. It continuously analyzes a project's source code, keeps the resulting findings and measurements as persistent platform-side state over time, holds a configurable definition of what "good code" means for that project, and reports a pass/fail verdict on every change into the team's merge and release workflow.

Its reason to exist is a structural gap: code analyzers (linters, bug detectors, complexity and duplication tools) produce findings for a single run, but nothing that runs once can answer "is this codebase getting better or worse?" or "may this change be merged?". The platform sits between the analysis engines and the delivery workflow: it accumulates analysis results into a durable quality picture — issues, metrics, ratings, trends — and turns them into a go/no-go signal attached to each pull request and branch.

The defining core is deliberately small:

```text
Managed project (bound to a repository)
└── Recorded analysis runs (on onboarding and on every change)
    └── Persistent quality state (issues + metrics + history)
        └── Configurable quality standard (rules and/or thresholds)
            └── Quality verdict surfaced in the delivery workflow
```

Everything else commonly associated with these products — coverage tracking, letter grades, pull-request comments, portfolios, self-hosted servers, AI fix suggestions — is standard market capability or optional, not part of the definition.

## Users & Context

Primary users:

- **Developers** — the people whose code is analyzed. They meet the platform inside the pull request: automated review comments, issue annotations, and the quality check that must pass before merge. They also visit the platform to see their assigned issues and fix them.
- **Team / tech leads** — configure the quality standard (which rules, which thresholds), triage findings, and watch the trend of the code they own.
- **Engineering managers** — consume the aggregate picture: dashboards, reports, and portfolio views over many repositories.

Secondary users:

- **Platform / DevOps engineers** — wire the analysis into CI pipelines and connect gate results to pipeline behavior.
- **Organization administrators** — manage people, roles, org-wide policies, and integrations.

The work context is the software delivery workflow. Analysis is triggered by repository events (initial onboarding, pushed commits, opened or updated pull requests), and the platform's output is consumed at merge and release decision points. Direct interaction happens in a web console; indirect interaction happens through pull-request surfaces in the Git provider, CI logs, IDE companions, and APIs.

## Core Model

### The defining core

**Managed project.** The unit of management is a project bound to a source repository (or a defined part of one). Projects live inside an organization that usually mirrors the structure of the connected Git provider. Branches and pull requests of the project are first-class analysis subjects.

**Recorded analysis runs.** Each time code changes — and once when the project is first added — an analysis run executes (from the platform's own engines, from third-party analyzers the platform wraps, or both) and its results are recorded. The run, not the tool invocation, is the unit of history: platforms display a timeline of analyses and how measures evolved between them.

**Persistent quality state.** Findings and measurements are stored and maintained by the platform over time:

- **Issues** — individual findings bound to precise code locations, each raised because a rule was violated: bugs, code smells, complexity and duplication findings, security findings, lint results from wrapped tools.
- **Metrics** — measures computed for the project, branch, directory, or file: issue counts by severity, duplicated-code density, complexity, size (lines of code), test coverage, and remediation-effort estimates often expressed as technical debt.
- **History and trends** — the state survives across runs, which is what makes deterioration visible and improvement measurable.

**Configurable quality standard.** A maintained definition of "good" for this code, with two faces:

- a **rule set** — which checks apply (a per-language profile of rules, a pattern configuration, a set of enabled analyzers, or a committed configuration file in the repository);
- **thresholds and conditions** — what the measured values must satisfy for a change to be acceptable (no new high-severity issues, complexity below X, duplication below Y, coverage not decreased).

**Quality verdict.** The evaluation of an analysis run's results against the standard, reported as a visible pass/fail status attached to the change — a commit status, a pull-request check, or a gate badge — and used in merge/release decisions. Whether the verdict merely reports or actively blocks the merge is a wiring decision; the verdict itself is the invariant.

### Standard capabilities mature products add

- **New-code orientation.** The dominant modern philosophy: gates and reporting concentrate on issues *introduced* by the change under review, while the state of the whole codebase ("overall code") is tracked in parallel as the debt picture. Platforms implement this through a project-level definition of what counts as new code (changes since the last version, a date or day window, or the pull-request diff) and by comparing against a recorded baseline.
- **Issue lifecycle.** New issues are commonly auto-assigned to the person who authored the changed line. Issues carry dispositions that survive later analyses — accepted / won't fix, false positive — plus tags, comments, and reopen-on-recurrence.
- **Ratings and grades.** Aggregated at-a-glance assessments derived from metrics — letter grades or scores for reliability, security, maintainability, and coverage, computed at project and file level.
- **Coverage ingestion.** Test-coverage reports produced by the team's own test tooling are uploaded to the platform (via reporter CLIs), merged, trended, and usable as gate conditions — including diff coverage, i.e., coverage of the changed lines only.
- **Pull-request reporting.** Statuses, decorations, and inline issue annotations rendered directly in the Git provider's pull-request interface.
- **Integrations.** CI-based analysis (scanners/CLIs invoked from pipelines), Git-provider connections, badges, APIs and webhooks.
- **Organizational layer.** Org-level default standards automatically applied to newly added repositories, org dashboards, multi-repository reporting, and — in enterprise packaging — portfolio views that aggregate quality across many projects.
- **Deployment duality.** Cloud service and/or self-managed server installation; IDE companions that surface the platform's rules while writing code.

## How It Works

### Onboarding a project

```text
Connect the Git provider / import the organization
→ select repositories to manage
→ initial ("baseline") analysis runs
→ default rule set and thresholds apply
→ quality state appears: issues, metrics, ratings, trends
```

Baseline matters: several behaviors (gate computation, coverage trends, new-issue detection) only become meaningful once the platform has a first recorded state to compare against.

### The per-change loop (the defining workflow)

```text
Developer opens or updates a pull request
→ analysis run executes (from CI or the platform's cloud)
→ platform compares results against the baseline / new-code definition
→ new issues surface as automated review comments and annotations
→ quality gate evaluates the conditions
→ verdict (pass / fail) is reported as a status on the pull request
→ developer fixes or disposes the findings
→ re-run → verdict updates
→ merge is allowed (or optionally blocked until pass)
```

This loop is the product's core value: it converts quality from a periodic audit into a per-change constraint, and it is why these platforms are described as protecting the codebase "from unwelcome changes".

### The health loop

```text
Changes merge → branch analysis records the new state
→ metrics and ratings update; trends accumulate
→ teams review dashboards, fix assigned issues, adjust the standard
→ the overall picture is meant to improve as new code stays clean
```

### The organization loop

```text
Define org-level standard / gate policy → applied by default to new repositories
→ cross-repo reporting and (in enterprise tiers) portfolio views
→ policy changes propagate; previous per-repo settings can be restored on removal
```

## Interfaces

- **Repository dashboard** — the project's quality overview: metrics, ratings, recent analyses, gate status; primary actions: drill into issues, coverage, files, trends.
- **Issues view** — filterable list of findings (by severity, type, assignee, age, new-vs-existing); primary actions: open a finding at its code location, assign, tag, comment, dispose (false positive / accepted), see fix suggestions.
- **Pull-request / commit view** — per-change quality: introduced issues, diff coverage, condition-by-condition gate result; primary actions: review findings, read the verdict, follow links back into the code.
- **Files / code view** — quality mapped onto the file tree and source: per-file ratings and inline issue locations.
- **Coverage view** — test-coverage totals, trends, and per-line/diff coverage after report uploads.
- **Standards configuration** — rule/profile/pattern management per language; analyzers toggles; threshold editing; committed configuration files supported in the repo.
- **Gate configuration** — define conditions, set defaults, apply org policies; view gate history.
- **Organization reporting** — cross-repository overviews, segments or portfolios, exports/reports; admin surfaces for people, roles, and integrations.
- **External surfaces** — the pull-request UI of the Git provider (statuses, checks, decorations, inline comments), CI logs, badges, IDE companions, and an API (and commonly CLIs) for retrieving metrics/issues and automating configuration.

## Important Rules / Behaviors

- **The verdict is attached to the change, and enforcement is a choice.** The gate status always exists as a visible signal; whether it blocks merging or fails the pipeline depends on how the team wires the Git provider's branch protection and CI. Products document both postures; blocking is never forced by the platform alone.
- **Findings belong to code locations and persist until resolved.** An issue remains associated with its line(s) across analyses; when the code changes such that the finding disappears, it closes; dispositions (false positive, accepted) are remembered and reapplied on later runs rather than re-raised.
- **New-issue focus shapes what a review reports.** In the dominant modern mode, a pull-request analysis reports what the change introduced — not the pre-existing debt of untouched code. Pre-existing findings remain browsable in the platform. Consequence: a first analysis after onboarding may surface old-code findings that per-change reviews never showed.
- **Baselines gate the gate.** Before a baseline or a new-code definition exists, the verdict may be "not computed" rather than pass or fail.
- **The platform consumes coverage; it does not produce it.** Coverage conditions depend on the team uploading reports from their test tooling; missing reports are a first-class failure mode (gaps, stale data).
- **Organizational standards can override repository settings.** An org-level policy typically auto-applies to newly added repositories; removing it can restore the repository's previous settings. Built-in default policies are commonly protected from edit/delete.
- **The standard is code too, somewhere.** The rule set lives either platform-side (profiles/patterns edited in the console) or repository-side (committed configuration files), with committed files usually required to be on the default branch to take effect.
- **Assignment targets authors.** New findings are typically assigned to the committer/author of the offending line when the person can be matched to a platform user; reassignment is always possible.

## Variants

- **Self-managed server vs. cloud service.** The same Type is delivered as an installed server (enterprise data-center posture, common in regulated environments) or as a SaaS connected to the Git provider. Self-hosted Kubernetes-packaged installs also exist.
- **Own engines vs. analyzer aggregation.** Some platforms build their own analysis engines and rule sets; others primarily wrap third-party analyzers behind a unified configuration; most do some of both.
- **Grade-centric vs. standards-centric philosophy.** One pole expresses quality as letter grades per file/project and technical-debt ratios; the other as enforceable rule profiles and gate conditions; the market converges on providing both views.
- **Security-inclusive breadth.** Most platforms bundle a security axis (security findings, hotspot review, dependency risks, secrets detection, license compliance) — as modules. Security-first products are a different Type (see below).
- **Transformation posture.** Some platforms only observe and report; others also act — auto-formatting pull requests, applying automated fixes to findings.
- **Enterprise packaging.** Portfolio aggregation, regulatory/PDF reporting, advanced analytics, and usage reporting appear as higher-tier or enterprise-plan capabilities.
- **Integration depth.** IDE companions in connected mode, CI-triggered scans, API-driven headless use (including use by AI coding agents) vary by product.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Static Code Analysis Platform | the analyzer/engine layer: runs checks over code and reports findings for a run. Remove the platform's persistent state, history, standard, and verdict and you get an analyzer. Many quality platforms embed engines — the seam is the system-of-record layer, and the two leaf definitions must be kept at different layers. |
| SAST (Static Application Security Testing) | centers security vulnerabilities and attack-oriented findings; a quality platform treats security as one bundled quality axis among several. |
| Code Review Platform | the human review conversation is the subject (requests, diffs, approvals, threads); a quality platform supplies automated checks into that flow but does not host the review itself. |
| Continuous Integration Platform | orchestrates builds and pipelines; the quality platform is typically triggered by CI and reports back (failing a stage on a failed gate), but build orchestration is not its subject. |
| Test Automation / Software Test Management | authors, runs, and manages tests; the quality platform only ingests the coverage those tests produce. |
| Dependency Management / SCA | centers the dependency graph and its risks; on a quality platform, dependency and license risk appears as an optional bundled module. |
| Error Tracking Platform | monitors failures of running software in production; the quality platform judges source code before it merges. |
| Engineering Productivity Analytics | measures delivery flow and team throughput; the quality platform measures the health of the code itself, not the people producing it. |

The most important seam is the one with the bare static analyzer: if results live only in the run's output — no history, no standard, no verdict in the delivery flow — it is an analysis tool, not a platform.

## Representative Products

- **SonarQube** (Sonar) — delivered as a self-managed server and a cloud service, with an IDE companion; the source of much of the market's concept vocabulary (quality profiles, quality gates, new code).
- **Codacy** — SaaS-first with a self-hosted Kubernetes option; Git-provider-native organizations and org-level gate policies.
- **DeepSource** — SaaS-native, developer-workflow-first posture with analyzer auto-detection, formatters, and automated fixes.
- **Qlty** (from the makers of Code Climate, the first cloud-based code quality platform, 2011) — cloud "code health" posture with letter-grade ratings and quality gates as commit statuses.

## Sources

Research date: **2026-09-07**. All sources are official vendor documentation.

- Sonar — SonarQube Server homepage: https://docs.sonarsource.com/sonarqube-server/readme.md
- Sonar — Pull request analysis: https://docs.sonarsource.com/sonarqube-server/discovering/code-analysis/pull-request-analysis.md
- Sonar — Managing issues: https://docs.sonarsource.com/sonarqube-server/user-guide/issues/introduction.md
- Sonar — Quality gates: https://docs.sonarsource.com/sonarqube-cloud/standards/quality-gates.md
- Sonar — Quality standards and new code: https://docs.sonarsource.com/sonarqube-cloud/standards/about-new-code.md
- Sonar — Measures and metrics: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/metric-definitions.md
- Codacy — Documentation home / quickstart: https://docs.codacy.com/ , https://docs.codacy.com/getting-started/codacy-quickstart/
- Codacy — Adjusting quality gates: https://docs.codacy.com/repositories-configure/adjusting-quality-gates/
- Codacy — Using gate policies: https://docs.codacy.com/organizations/using-gate-policies/
- DeepSource — Quickstart: https://docs.deepsource.com/docs/platform/getting-started
- DeepSource — Configure analyzers: https://docs.deepsource.com/docs/platform/getting-started/configure-analyzers
- Qlty — What is Qlty / Quality Gates / Maintainability metrics and ratings: https://docs.qlty.sh/ , https://docs.qlty.sh/cloud/gates.md , https://docs.qlty.sh/cloud/maintainability/metrics.md

> Sourcing limitations: numeric thresholds, plan-gated features, and product-specific mechanics (exact gate values, file-size ceilings, rating-band grids) are documented per product and intentionally not asserted here as Type-level facts. Portfolio-level aggregation was directly verified for one vendor's enterprise tier and is stated as a common enterprise capability rather than a universal one. Qlty organization-layer detail was only lightly documented in fetched pages; no Type-level claims rest on it.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical-sample check are recorded in the paired Research Notes.
