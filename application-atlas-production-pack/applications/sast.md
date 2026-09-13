# SAST (Static Application Security Testing)

## Overview

A **SAST tool** analyzes an application's own code — its source code, or the compiled form it produces — **without executing the application**, in order to find security vulnerabilities before the software runs anywhere. It is an automated security reviewer of code: it reads the code, reasons about how data moves through it, and reports places where a weakness (an injection flaw, cross-site scripting, insecure cryptography, a hardcoded credential, a dangerous API call) appears to exist.

Three properties make the Type what it is:

- the object of analysis is the application's **own first-party code**, and the code is **never executed** as part of the test;
- the analysis is driven by **security-oriented detection knowledge** — packaged rules, queries, or checkers that encode vulnerability classes;
- the output is **vulnerability findings located in the code** — each finding points at a file and line, names the weakness class, and tells a developer what to do about it.

Everything else commonly associated with SAST — CI/CD integration, pull-request annotations, triage consoles, policy gates, dashboards, AI-suggested fixes — is mature market structure built around that core, not part of the definition. Remove the security orientation and the same machinery becomes general static analysis; remove the "code is not executed" property and it becomes dynamic testing; remove "own code" and it becomes dependency analysis.

## Users & Context

Primary users:

- **Developers** — receive findings in the places they already work (editor, pull request, pipeline), fix the flagged code, and occasionally suppress a finding with a justification.
- **Application security engineers** — select and tune the detection rules, triage findings the developers cannot resolve, decide what is exploitable, and manage suppression policy.
- **Security/compliance leads** — consume aggregate views: which applications are scanned, what the risk posture is, whether security policy is met.

Typical context: a development organization that wants vulnerabilities caught **at code-writing time**, when fixing is cheapest. The tool therefore lives inside the development workflow — triggered on commits and pull requests, surfaced in editors and code review — rather than in a separate security operations cycle. A security team typically owns the configuration and the backlog; development teams own the fixes.

## Core Model

The world of a SAST tool consists of a small set of objects bound together by one loop:

```text
Managed codebase (project / repository / application)
  └── Scan (analysis run over a code snapshot)
        ├── driven by Detection knowledge (rules / queries / checkers)
        └── produces Findings
              ├── located in code (file + line, commonly with a data path)
              ├── classified (weakness class, severity)
              └── moved through a Triage lifecycle
                    ├── fixed in code (verified by a later scan)
                    └── suppressed with a recorded reason
  └── Policy / gate (decides whether the code may proceed)
```

### The defining core

- **Static analysis of the application's own code, without executing it.** The tool consumes the codebase — source text, or the application's own bytecode/binary — and analyzes its structure and data flow. Running the application is never part of the test; that is what separates SAST from dynamic testing.
- **Detection knowledge.** The analysis is not ad-hoc: it is driven by a catalog of rules, queries, or checkers, each encoding a vulnerability class (SQL injection, XSS, command injection, insecure deserialization, weak hashing, exposed secrets, and so on). Mature products ship large built-in catalogs and let the organization extend them.
- **Findings.** The output unit. A finding identifies a potential vulnerability: where it is (file, line, commonly the path data takes from an untrusted source to a dangerous sink), what class of weakness it is, how severe it is, and how to fix it. Findings are the currency of everything else — triage, gates, reports.

### Standard capabilities of mature products

These are widespread in current products but do not define the Type:

- **Scan modes** — a full scan of the codebase, plus faster modes that scan only what changed (incremental scanning, diff-aware scanning against a baseline commit) for use inside pipelines and pull requests.
- **Finding identity and tracking** — findings persist between scans and are recognized as "the same finding" even when code moves; products distinguish new findings from the existing backlog.
- **Triage lifecycle** — each finding carries a state (unreviewed → confirmed / not exploitable / dismissed / fixed), with recorded reasons, notes, and permissions governing who may change what.
- **Suppression machinery** — inline code comments, rule disabling, and path exclusions, all recorded and auditable, so a suppressed finding stops reappearing.
- **Severity and classification** — a severity rating (commonly derived from CVSS-style scoring) plus weakness classification using industry identifiers (CWE-style), sometimes mapped to standards such as OWASP Top 10.
- **Remediation guidance** — an explanation of the flaw and how to fix it; current-generation products add suggested patches and AI-generated fixes.
- **Development-workflow integration** — CI/CD jobs, pull-request annotations and comments, required checks that block merges, IDE plugins, local CLI scanning.
- **Policy and portfolio surfaces** — organization-wide rules about which findings may not exist, whether scans must run and how often, and pass/fail evaluation per application; dashboards and exportable reports (SARIF/JSON/CSV are common exchange formats).
- **Custom detection** — authoring or customizing rules for internal frameworks and organization-specific patterns.

### One structure, many implementations

The core model is conceptual; products realize each piece differently:

```text
Concept:            Object of analysis
Implementations:    source code read directly; compiled bytecode/binary uploaded for analysis

Concept:            Detection knowledge
Implementations:    pattern-based rules; queries over a code database or code graph;
                    engine-internal flaw patterns over a control/data-flow model

Concept:            Finding identity across scans
Implementations:    rule + file + code-context tuples; similarity/tracking algorithms

Concept:            Severity
Implementations:    CVSS-derived bands; qualitative levels; adjustable scores

Concept:            Gate
Implementations:    required pull-request check; build-breaking policy; portfolio pass/fail rating
```

A reader who has only seen one implementation — say, a source-scanning engine inside a CI pipeline — should still be able to recognize a binary-upload platform or a hosting-platform-embedded scanner as the same Type.

## How It Works

The typical life of a SAST deployment runs as follows.

### 1. Bring a codebase under testing

The organization registers the target — a repository, project, or application profile — and selects the detection rules (a preset or query suite appropriate to the languages and risk posture). Some engines analyze source directly with no build; others require the code compiled into artifacts first. Path exclusions (test code, generated code) are commonly configured here.

### 2. Scan

A scan analyzes a snapshot of the code: the engine parses it, builds its internal representation (syntax trees, a code database, a code graph, or a control/data-flow model), and evaluates the detection knowledge against it. Full scans establish the baseline; incremental or diff-aware scans cover only changed code plus its surroundings, trading coverage for speed so scanning can run on every commit or pull request.

### 3. Review findings

Each finding is presented with its location in the code, the weakness class, a severity, and — for data-flow-based detection — the path the data takes from an untrusted source to the dangerous sink. Multiple code paths reaching the same unsafe operation are commonly grouped under one finding. Remediation guidance explains the fix.

### 4. Triage

A reviewer — usually the developer for straightforward cases, the security team for the rest — moves each finding through its lifecycle: confirm it as a real issue, mark it not exploitable or a false positive (with a recorded reason or note), or assign it for fixing. Triage decisions typically propagate across branches so the same finding is not re-litigated everywhere it appears.

### 5. Fix and verify

The developer changes the code. The next scan no longer detects the finding, and the finding closes as fixed. Suppressed findings stay closed unless the code changes in ways that re-trigger the rule. Some products generate a suggested patch or open a fix pull request automatically.

### 6. Gate the change

Where the organization enforces security, the scan result participates in the delivery decision: a pull-request check that must pass before merge, a build that breaks on new critical findings, or a portfolio policy that rates the application pass/fail against rules such as "no high-severity injection findings" and "scanned within the required window".

### 7. Report and govern

Aggregated views answer management questions: how many findings exist per application, how fast they are fixed, whether policy is met, where the risk concentrates. Results export in standard formats for consumption by other security systems.

## Interfaces

The surfaces below are described conceptually; exact layouts and names vary by product.

### Editor / IDE surface

Purpose: catch issues while code is being written.
Typical information: findings for the open file, inline markers, quick access to guidance.
Primary actions: view finding detail, apply suggested fix, suppress with reason.

### Pull-request / merge-request surface

Purpose: put security findings into the code-review conversation.
Typical information: newly introduced findings as annotations on changed lines, a summary check (pass/fail, new vs resolved findings).
Primary actions: view finding, fix, dismiss with reason; the check may be required for merge.

### Pipeline / CI surface

Purpose: run scans automatically on every change.
Typical information: job status, scan configuration, result artifacts in standard formats.
Primary actions: configure triggers and variables, fail the build on thresholds, publish results onward.

### Security console (findings list and finding detail)

Purpose: the security team's working surface over the finding backlog.
Typical information: filterable list of findings per project/application with severity, state, age, and owner; a detail view with the flagged code, the data path from source to sink, classification, guidance, and the triage history.
Primary actions: change state, change severity, add notes, assign, bulk-triage, export.

### Rule / preset configuration

Purpose: control what the tool looks for.
Typical information: built-in rule catalogs grouped by language and weakness class, presets or query suites, custom rules.
Primary actions: enable/disable rules, tune severity, write or import custom rules, exclude paths.

### Dashboards and reports

Purpose: aggregate posture for teams and management.
Typical information: findings trends, fix rates, policy compliance per application, scan coverage.
Primary actions: filter, export, schedule reports.

### CLI

Purpose: local and pipeline scanning without a UI.
Typical information: scan progress, findings in machine-readable output.
Primary actions: run a scan, diff against a baseline, emit results in a standard format.

## Important Rules / Behaviors

- **Findings are potential vulnerabilities, not proven exploits.** Static analysis reasons about code without running it, so false positives are an expected, structural part of the workflow — which is why triage with recorded justifications exists in every mature product. Products differ in how aggressively they filter (some offer fast modes that report only the most exploitable patterns, at the cost of coverage).
- **Suppression is deliberate and recorded.** A finding is never silently ignored: dismissing it requires a reason (false positive, acceptable risk, won't fix, test code), commonly a note, and the dismissal is auditable. The next scan does not regenerate a dismissed finding.
- **Findings persist and travel.** The same weakness is tracked across scans even when the code moves within or between files; triage decisions usually follow the finding across branches. Disabling a rule typically resolves (or removes) its findings, and re-enabling restores them.
- **The code is never executed — but it may need to be built.** Analysis is static by definition; whether the engine consumes raw source or requires compiled artifacts is a product characteristic. Engines that build models from binaries depend on debug information to report precise file-and-line locations.
- **Branch semantics matter.** Findings on a feature branch and on the default branch are related but distinct; products commonly treat the default branch as the canonical backlog and surface new findings per pull request.
- **Coverage depends on framework modeling.** Detection quality relies on modeled knowledge of frameworks and libraries; code using unsupported frameworks may produce incomplete results rather than failures.
- **Depth versus speed is an explicit trade-off.** Products offer scan modes that trade thoroughness (fewer flows explored, fewer findings) for pipeline-friendly runtimes.
- **Severity is standardized-ish but adjustable.** Ratings commonly derive from CVSS-style scoring and CWE-style classification, and security teams can usually override severity per finding under permission controls.

## Variants

Common forms of the Type:

- **Standalone engine** — a CLI/library that scans code and emits findings; consumed directly or embedded by other tools. Minimal form of the Type.
- **Security platform module** — the scanner sold as one scanner inside a broader application-security suite (beside dependency, container, and dynamic scanners), sharing one console and one triage workflow.
- **Platform-embedded** — scanning delivered as a feature of a code-hosting or DevOps platform, with findings surfaced as repository alerts and pull-request checks; may wrap third-party engines under its own rules.
- **Policy-centric cloud platform** — applications are uploaded (source or compiled artifacts), scanned by the vendor's engine, and evaluated against portfolio security policies with pass/fail ratings.
- **Developer-first lightweight** — fast, low-setup scanning designed to run in editors, pre-commit hooks, and every pull request, with simple pattern-based rules and easy custom rule authoring.

Variant axes that cut across all forms: input form (source vs compiled binary), analysis technique (pattern matching vs dataflow/taint vs cross-file/cross-function), language breadth and build requirements, deployment (self-hosted vs SaaS), and the degree of AI assistance in triage and fixing.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| DAST / IAST | sibling testing Type | DAST tests the **running** application from the outside; IAST instruments it at runtime. SAST analyzes code that never runs. Vendors ship them as separate products/features; they complement each other. |
| Software Composition Analysis / SCA | sibling testing Type | SCA finds vulnerabilities in **third-party dependencies**; SAST finds them in **first-party code**. Suites ship both as separate scanners. |
| Static Code Analysis Platform | closest machinery overlap | Same static-analysis machinery, different orientation: general static analysis targets bugs, smells, and style for code quality; SAST targets security weaknesses for an AppSec program. Many products serve both orientations. |
| Code Quality Platform | adjacent platform layer | A code-quality platform keeps persistent quality state and pass/fail verdicts on changes, and may wrap analyzers — including SAST engines — as one input among several. Security-first detection vs quality-first platform. |
| Application Security Platform | program layer it feeds | The program layer holds application records, consolidated finding lifecycles, policies, and portfolio management. SAST is one of the engines whose findings feed that layer; the same vendor often sells both. |
| Vulnerability Management | downstream consumer | Vulnerability management owns the organization-wide vulnerability lifecycle across infrastructure; SAST findings are one input, commonly handed off via exports/integrations. |
| Secrets Security | partially overlapping capability | Dedicated secrets detection is its own Type; SAST includes hardcoded credentials as one vulnerability class among many, and suites often ship a separate secrets scanner. |
| Code Review Platform | adjacent workflow surface | Code review is the human review of proposed changes; SAST contributes automated findings and checks into that surface but does not manage human review. |
| Software Supply Chain Security | broader program | Supply-chain security spans dependencies, build pipelines, and artifacts; SAST is the first-party-code testing slice of that world. |

The sharpest boundaries are the two sibling testing Types: change the object from "code that is not run" to "a running application" and the Type becomes DAST/IAST; change it from "the application's own code" to "its dependencies" and it becomes SCA. Change the orientation from security to general code health and it becomes static code analysis.

## Representative Products

- **Semgrep** (Community Edition + AppSec Platform) — developer-first pattern/dataflow rules; OSS engine with a commercial platform
- **GitHub Code Scanning with CodeQL** — platform-embedded scanning with a query-language engine and SARIF interop
- **Veracode Static Analysis** — policy-centric cloud platform; analyzes compiled binaries/bytecode without requiring source
- **Checkmarx One SAST** — enterprise SaaS scanner querying a code graph, with heavyweight triage workflows
- **GitLab SAST** — DevOps-platform-embedded, multi-analyzer (own advanced engine plus wrapped open-source engines)

Fortify is the long-established enterprise on-prem representative of the Type; its documentation could not be reached during research (see Sources), so it is listed as market context only.

## Sources

Research date: **2026-09-09**

- Semgrep — https://semgrep.dev/docs/ ; https://docs.semgrep.dev/introduction.md ; https://docs.semgrep.dev/learn/security-foundations/sast/overview.md ; https://docs.semgrep.dev/semgrep-ci/findings-ci.md
- GitHub — https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning ; https://docs.github.com/en/code-security/concepts/code-scanning/codeql/codeql-code-scanning ; https://docs.github.com/en/code-security/concepts/code-scanning/code-scanning-alerts ; https://docs.github.com/en/code-security/how-tos/manage-security-alerts/manage-code-scanning-alerts/resolve-alerts
- Veracode — https://docs.veracode.com/r/c_static_overview ; https://docs.veracode.com/r/c_appsec_policies
- Checkmarx — https://docs.checkmarx.com/en/34965-324470-sast-scanner.html ; https://docs.checkmarx.com/en/34965-373312-triaging-sast-results.html
- GitLab — https://docs.gitlab.com/ee/user/application_security/sast/

> Sourcing limitation: OpenText Fortify official documentation was unreachable from the research environment (product page and documentation host both failed repeatedly). Fortify is used only as market context; no operational claims in this document rest on it. Precise vendor-specific numbers (scan thresholds, retention windows, default presets, scoring formulas) observed in vendor documentation are intentionally not stated here; they remain in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
