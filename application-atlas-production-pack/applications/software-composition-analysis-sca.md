# Software Composition Analysis / SCA

## Overview

A **Software Composition Analysis (SCA) application** analyzes the third-party components an application is composed of — its dependency population at resolved versions — and matches that inventory against continuously maintained knowledge about those components to produce per-component risk findings that the owning team can act on.

The defining structure is small:

```text
Analyzed software unit (application / project / repository)
└── Resolved third-party component inventory (direct + transitive, at pinned versions)
    └── Matching against maintained component knowledge
        └── Per-component findings (component × version × risk)
```

Known vulnerabilities are the canonical knowledge class; license obligations are the other long-standing class. Everything else commonly associated with modern SCA — remediation guidance, automated fix pull requests, policy gates, SBOM export, reachability analysis, portfolio dashboards — is widespread in current products but is not part of the defining core. Package-manager audit commands, SBOM-centric platforms, and code-hosting-native features all fit this definition without any of those specifics.

When the dominant object shifts to the application's own first-party code, to the SBOM artifact as an inventory of record, or to the whole supply-chain protection program, the product is drifting toward a different Application Type (SAST, SBOM Management, Software Supply Chain Security).

## Users & Context

The primary users are developers and application security engineers on teams that build software from third-party — mostly open-source — components. Their recurring questions are: *what is this application actually composed of, which of those components carry known risk, and what should we do about it?*

Secondary users:

- **security / compliance managers** — configure policies, review risk posture across projects, own the gate behavior in the pipeline
- **license / legal reviewers** — consume license findings and obligations attached to components
- **release / engineering managers** — consume portfolio-level reports and metrics

The work context is the software development workflow itself: scans run from a CLI, an IDE, a build or CI step, or a repository integration; findings are consumed in pull-request review and in a web console used for triage, policy configuration, and reporting.

## Core Model

### The Defining Core

Three structures. If any one is removed, the product is no longer recognizable as SCA:

- **The resolved third-party component inventory of an analyzed software unit.** The analyzed subject is an application, project, or repository; the inventory is the population of external components it is composed of — direct and transitive — at their resolved versions. Without this, the product is an advisory feed, a package listing, or a bare SBOM artifact.
- **Matching the inventory against maintained external component knowledge.** The knowledge is about the components themselves — known vulnerabilities as the canonical class (advisory databases), with license obligations and other component risk as common extensions — and it is continuously updated by parties other than the authors of the analyzed software. Without this, the product is a plain dependency listing (the package manager's own job) or a static audit.
- **Per-component findings as the consumable output.** Each finding binds a risk to a specific component at a specific version inside the analyzed unit — identified, severitied, and actionable by the owning team. Without this, the product is a raw data service or a score with no component binding.

The three are jointly load-bearing: an inventory without matching is a dependency list; matching without an inventory is an advisory database; findings without the first two are a hand-maintained audit report.

### Standard Capabilities of Mature Products

A typical modern SCA product carries most of these. They are not what makes the product an SCA, but they make it practical:

- **Remediation direction** — the fixed or secure version and an upgrade path for each affected component.
- **Severity model and advisory identifiers** — CVSS-based severity and CVE/GHSA-class identifiers on findings.
- **Introduction / transitive path visibility** — how a risky component entered the tree (which manifest, which parent dependency).
- **Triage lifecycle** — findings move through managed states; suppression and waivers are recorded with reasons and retained as history.
- **Continuous re-analysis** — the inventory is re-checked as new advisories appear, so risk surfaces without any change to the software itself.
- **CI/CD integration and policy gates** — scans run in the pipeline and policy conditions can fail a build or block a merge.
- **License analysis** — per-component license detection and license policies; in some products documented as a distinct analysis type separable from vulnerability analysis.
- **Prioritization overlays** — exploit signals, code-level reachability, risk factors, popularity/age signals layered on top of raw findings.
- **Development-workflow surfaces** — CLI, IDE plugins, PR/MR annotations, dashboards, reports and exports.
- **Organization / portfolio layer** — applications and projects grouped under organizations, with cross-project dashboards and metrics.
- **SBOM generation / export** — present in part of the sample; not universal.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. Common implementations realize each concept differently:

```text
Concept:          Component inventory
Implementations:  manifest/lockfile parsing, binary/hash analysis,
                  SBOM ingestion, build-time dependency submission

Concept:          Component knowledge
Implementations:  own curated commercial database,
                  aggregation of public advisory sources,
                  platform-native advisory database

Concept:          Delivery form
Implementations:  standalone SaaS, self-hosted server,
                  feature embedded in a code-hosting platform
```

A reader who only encounters one implementation (e.g. a manifest-scanning SaaS) should still be able to recognize an SBOM-ingesting or hash-matching product as the same Type from the Core Model.

## How It Works

### Resolve the inventory

```text
Point the analyzer at an application (repo, project, or build)
→ it resolves what the software is composed of:
  manifests and lock files parsed, or binaries hashed and matched,
  or an SBOM consumed, or dependencies submitted at build time
→ direct and transitive dependencies identified at their resolved versions
```

Transitive coverage is explicit in every mature implementation: the risk often sits in a dependency the team never chose directly.

### Match against component knowledge

```text
For each component (name + version)
→ look up maintained knowledge: known vulnerabilities, license obligations,
  and in some products malicious-package or component-health data
→ produce findings where knowledge matches the component
```

The knowledge base is external to the analyzed software and continuously updated — this is what makes yesterday's clean scan turn up new findings today.

### Consume and act on findings

```text
Review the finding: component, version, advisory, severity,
  introduction path, fixed version
→ triage: confirm, dismiss with reason, or waive with justification
→ remediate: upgrade to the fixed version; some products advise
  working direct dependencies before transitive ones, and some open
  automated fix pull requests
→ re-scan to confirm resolution
```

### Gate the pipeline

```text
Scan runs as a CI/CD step or required check
→ policy conditions evaluated (severity thresholds, license rules,
  security policies)
→ pass, warn, or fail the build / block the merge per configuration
```

### Keep watching

```text
Inventory retained (snapshot, monitored application, or published SBOM)
→ re-checked continuously or on a schedule as advisories change
→ new findings alert the owning team without a new scan being run
```

### Capability tiers

**Defining core** — without these, not SCA:

- resolved third-party component inventory of an analyzed unit
- matching against maintained component knowledge
- per-component findings as the consumable output

**Standard mature structure** — present in most modern products:

- remediation direction, severity + advisory identifiers, path visibility
- triage lifecycle with recorded waivers/suppressions
- continuous re-analysis, CI/CD gates, license analysis
- prioritization overlays, dev-workflow surfaces, portfolio layer

**Variant / optional** — depends on posture, delivery, and customer:

- inventory construction method (manifests vs hashes vs SBOMs vs build-time submission)
- knowledge-base posture (curated vs aggregated vs platform-native)
- knowledge classes beyond vulnerabilities and licenses (malicious packages, component health/age/EOL, outdated-version analysis)
- automated fix pull requests
- code-level reachability analysis over first-party code
- exploit-intelligence consumption (EPSS, VEX)
- delivery form (SaaS / self-hosted / platform-embedded) and packaging (standalone / module of an AppSec platform / feature of a hosting platform)

## Interfaces

The following surfaces are described in conceptual terms; exact layouts and names vary by product.

### Scan surface

The entry point that produces the inventory: a CLI command, an IDE action, a build/CI step, or a repository integration that scans on push or on schedule. Typical information: the analyzed unit, the resolved dependency tree, scan status. Primary actions: run a scan, view the tree.

### Findings dashboard / issues view

The team's working list of open findings across a project.

- typical information: component, version, advisory, severity, introduction path, triage state, age
- primary actions: filter and sort, open a finding, assign, triage/dismiss/waive, start remediation

### Component / finding detail

The single finding's full context.

- typical information: advisory description and references, affected version range, fixed version, license obligations where applicable, exploit/reachability signals where offered
- primary actions: view the introduction path, choose a fix, record a triage decision

### Pull-request integration

Findings and fixes surfaced where code changes are reviewed.

- typical information: vulnerabilities introduced or resolved by the change, license changes, dependency diffs including lock-file-level transitive changes
- primary actions: review the dependency diff, enable automated fix PRs, enforce as a required check

### Policy / gate configuration

Where the organization's rules live.

- typical information: policy conditions (severity, license, component risk), enforcement actions (warn / fail / record), scope (project, organization)
- primary actions: create and edit policies, set enforcement stages, manage waivers

### Reports and exports

Point-in-time and periodic outputs for audit and compliance: application composition reports, license bills, SBOM exports.

### Portfolio dashboards

Cross-project risk posture for security and engineering management: open findings by severity, remediation progress, policy violations, trends.

## Important Rules / Behaviors

### Findings bind to components, not code locations

This is the structural signature of the Type. A SAST finding points at a line of the application's own code; an SCA finding points at a component at a version inside the composition. Reachability analysis may read first-party code to prioritize a dependency finding, but the object of the finding remains the component.

### Transitive dependencies are in scope

The inventory includes dependencies introduced indirectly. A team can carry risk it never directly selected; introduction-path visibility exists precisely to make this traceable.

### Findings can appear without any change to the software

Because the knowledge base is continuously updated, a previously clean application can develop findings overnight. Continuous re-analysis against a retained inventory is the standard answer; the minimal form (a point-in-time audit command) simply lacks it.

### Triage and suppression are recorded

Dismissing or waiving a finding is a governed act: a reason is captured, the decision is attributed and retained, and the finding's history is auditable. Unexplained suppression is not the norm in mature products.

### License findings share the security workflow

License issues are surfaced, severitied, and triaged in the same views and pipelines as vulnerability findings — a deliberate design choice that makes license compliance part of the development loop rather than a separate legal audit.

### Gates are configurable, not automatic

Whether a finding fails a build or blocks a merge is a policy decision: products range from advisory-only to blocking enforcement, and the same product typically supports both postures.

## Variants

Common realizations of the Type:

- **developer-first SaaS (find-and-fix posture)** — fast scan-to-fix loop, automated fix PRs, developer-facing UX
- **policy/governance-first enterprise** — a policy engine over component risk, enforcement across many SDLC stages, organization hierarchies and waivers
- **SBOM-centric component-analysis platform** — consumes (and produces) SBOMs as the inventory substrate, portfolio-wide component monitoring, aggregator of multiple public advisory sources
- **platform-native** — analysis embedded as a free feature of the code-hosting platform itself, with the platform's own advisory database as the matching source
- **license-compliance-heavy audit-grade** — deep license machinery (obligations, notices, copyrights, approval workflows) descending from the early open-source-governance generation
- **package-manager-native audit command** — the minimal form: scan the resolved tree, match against an advisory database, report vulnerable components with suggested fixes; no platform, no policy engine, no continuous monitoring

A variant remains a **Variant** as long as the three-part defining core holds; the inventory-construction method, knowledge-base posture, and delivery form are variant axes, not identity.

## Related Application Types

| Application Type | Distinction |
|---|---|
| SAST | analyzes the application's **own first-party code**; SCA analyzes the **third-party components** it is composed of. Vendor-documented at every sampled suite (separate SAST and SCA products inside the same platforms). Overlap zone: SCA reachability reads first-party code, but only as prioritization machinery — the finding object stays the component. |
| SBOM Management | the **artifact** vs the **analysis**: SBOM Management's unit of record is the machine-readable component inventory (formats, generation, distribution, compliance consumption); SCA's unit is the analyzed application's component population plus the matching→findings loop. SCA tools commonly generate/export SBOMs; SBOM-centric platforms run vulnerability matching — the seam is where the SBOM becomes the substrate. |
| Vulnerability Management | SCA produces component-level findings **inside the development pipeline**; VM owns the **org-wide vulnerability lifecycle** across asset types (infrastructure, endpoints, applications). SCA findings are an input to VM, not the same Type. |
| Software Supply Chain Security | SCA is the **analysis capability over the composition**; SSCS is the broader **chain-protection posture** (adversarial-supplier threat model, malicious/tampered software evaluation, trust decisions enforced where software crosses chain boundaries). SSCS products commonly bundle SCA capability; bundling does not merge the Types. |
| Dependency Management Application | **risk-oriented analysis** vs **version-currency maintenance**: security updates are driven by known vulnerabilities, version updates by new release availability — a seam vendors themselves document inside one product family. The driver (advisory vs release) and the consuming workflow decide the Type. |
| Package Registry | the **venue** components are published to and fetched from vs the **analysis** of compositions; adjacent in the same workflow, different Types. |
| Static Code Analysis Platform | findings bind to **code locations** vs **components**; different output units and different knowledge (rules vs advisories). |
| Application Security Platform | the **engine vs program** seam: SCA scanners ship as modules inside AppSec platforms; the platform adds application records, finding lifecycle, policy/gates, and portfolio management. |

The boundary with SAST is the most important one, because the two are sold side by side in the same suites. The structural difference is the analyzed object: the application's own code versus the components it is composed of.

## Representative Products

- Snyk Open Source
- Sonatype Lifecycle (IQ)
- Mend SCA
- OWASP Dependency-Track
- GitHub (dependency graph + Dependabot + dependency review)

These were selected to span the market's product philosophies and customer tiers: developer-first SaaS, policy-first enterprise, SBOM-centric open source, and platform-native free tier. The defining core was checked against the minimal package-manager audit-command form and the early license-audit generation to avoid over-fitting to the modern platform era.

## Sources

Research date: **2026-09-09**

Primary vendor documentation (official operational documentation):

- Snyk — https://docs.snyk.io/scan-fix-and-prevent/scan-with-snyk/snyk-open-source.md (and pages cited within)
- Sonatype — https://help.sonatype.com/en/sonatype-lifecycle.html ; /en/policy-concepts.html ; /en/component-identification.html ; /en/continuous-monitoring-concepts.html ; /en/creating-a-lifecycle-remediation-plan.html ; /en/application-composition-report.html
- Mend — https://docs.mend.io/sca/latest ; /platform/latest/mend-sca ; /platform/latest/sca-reachability ; /legacy-sca/latest
- OWASP Dependency-Track — https://docs.dependencytrack.org/ (Introduction/features; analysis types; triage; CI/CD usage)
- GitHub — https://docs.github.com/en/code-security/concepts/supply-chain-security/ (dependency graph; Dependabot alerts; dependency review) and Dependabot security-updates documentation

> Sourcing limitation: Black Duck's official documentation site is a JavaScript-only application and its product site was unreachable during the research pass; the enterprise audit-grade classic is held as market context only and no claim in this document rests on it. Precise vendor-specific facts (numeric limits, default schedules, exact state vocabularies) are intentionally not stated here; they remain in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical / market-sample breadth check are recorded in the paired Research Notes.
