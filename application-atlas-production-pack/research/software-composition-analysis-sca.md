# Research Notes — Software Composition Analysis / SCA

Research date: 2026-09-09

## Research Goal

Understand what a Software Composition Analysis application actually is as an Application Type: its defining core, its standard capabilities, its variants, and its boundaries against neighboring Types (SAST, SBOM Management, Vulnerability Management, Software Supply Chain Security, Dependency Management Application, Package Registry, Static Code Analysis Platform, Application Security Platform).

This pass also discharges the forward flag left by the SAST pass (2026-09-09): "software-composition-analysis-sca (§15) — first-party vs dependency seam vendor-documented at every sampled suite (Semgrep Code vs Supply Chain, Veracode Static vs SCA, Checkmarx SAST vs SCA scanners, GitLab SAST vs Dependency Scanning)".

## Initial Boundary

SCA = Software Composition Analysis. Working hypothesis: tools that analyze the **third-party (commonly open-source) components** an application is composed of — the dependency population — and match them against maintained knowledge (vulnerability advisories, license data) to produce component-level findings that development teams fix.

Easily confused with:

- SAST (§15, processed) — analyzes the application's own first-party code
- SBOM Management (§15, unprocessed) — the SBOM artifact (inventory of record) vs the analysis over the composition
- Vulnerability Management (§15, unprocessed) — org-wide vulnerability lifecycle across asset types
- Software Supply Chain Security (§15, unprocessed) — broader program (build integrity, provenance, CI/CD)
- Dependency Management Application (§12, unprocessed) — developer-facing dependency updating
- Package Registry (§12, processed) — the venue components are published to / fetched from
- Static Code Analysis Platform (§12, unprocessed) — code-level findings, quality orientation
- Application Security Platform (§15, processed) — program layer; engines (incl. SCA scanners) are modules inside it

## Research Questions

1. How is the component inventory constructed (manifests, lockfiles, binary analysis, SBOM ingestion, build-time submission)? Is transitive resolution universal?
2. What knowledge is matched against (vulnerability advisories, license data, malicious packages, component health)? Whose knowledge (own curated DB vs public aggregators)?
3. What is the finding unit and what does it carry (component, version, advisory, severity, fixed version, introduction path)?
4. How does remediation work (upgrade guidance, auto-PR, waiver)? Direct vs transitive responsibility?
5. How does the Type embed in the dev workflow (CLI, IDE, CI/CD, PR, repository integrations)? What gate semantics exist?
6. Is continuous re-analysis (as advisories change) universal or variant?
7. What is the relationship to SBOMs (generation, consumption, SBOM-centric products)?
8. Where are the boundaries: vs SAST (first-party vs dependency), vs SBOM Management (artifact vs analysis), vs Dependency Management (risk vs currency), vs VM (component findings vs org-wide lifecycle)?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / tier | Evidence tier |
|---|---|---|
| Snyk Open Source | developer-first SaaS; find-and-fix posture; own vulnerability DB | Tier 1 (docs.snyk.io, doc query interface) |
| Sonatype Lifecycle (IQ) | policy/governance-first enterprise; policy engine over component risk; repository-integrated heritage | Tier 1 (help.sonatype.com/en/) |
| Mend SCA (WhiteSource lineage) | enterprise SCA with license-compliance heritage; reachability + malicious-package detection; module of Mend AppSec Platform | Tier 1 (docs.mend.io) |
| OWASP Dependency-Track | SBOM-centric open-source pole; consumes/produces CycloneDX; aggregator of public advisory sources | Tier 1 (docs.dependencytrack.org) |
| GitHub (dependency graph + Dependabot + dependency review) | platform-native, free tier; analysis embedded in code hosting | Tier 1 (docs.github.com) |

Dropped: Black Duck (enterprise audit-grade classic, license-compliance heavyweight) — official documentation site is a JavaScript-only application (documentation.blackduck.com, 2 URL patterns tried, no server-rendered content) and the product site 404'd (2 URL patterns tried). Per network rules the source was abandoned after repeated failures. Black Duck is held as market context only; no claims rest on it. Recorded as a sourcing limitation.

## Sources

- Snyk: https://docs.snyk.io/scan-fix-and-prevent/scan-with-snyk/snyk-open-source.md (doc query interface; sources cited within: scan-open-source-libraries-and-licenses, fix-your-vulnerabilities, snyk-cli-for-open-source, open-source-license-compliance, manage-risk, how-the-snyk-security-scan-task-works)
- Sonatype: https://help.sonatype.com/en/sonatype-lifecycle.html ; /en/policy-concepts.html ; /en/component-identification.html ; /en/continuous-monitoring-concepts.html ; /en/creating-a-lifecycle-remediation-plan.html ; /en/application-management.html ; /en/application-composition-report.html
- Mend: https://docs.mend.io/sca/latest ; /platform/latest/mend-sca ; /platform/latest/scan-sca-with-mend-cli ; /platform/latest/sca-reachability ; /platform/latest/risk-factors ; /legacy-sca/latest
- Dependency-Track: https://docs.dependencytrack.org/ (Introduction/features) ; /analysis-types/known-vulnerabilities/ ; /triage/analysis-states/ ; /usage/cicd/
- GitHub: https://docs.github.com/en/code-security/concepts/supply-chain-security/dependency-graph ; /concepts/supply-chain-security/dependabot-alerts ; /concepts/supply-chain-security/dependency-review ; /dependabot/dependabot-security-updates/about-dependabot-security-updates ; /dependabot/working-with-dependabot/dependabot-options-reference

## Product Observations (evidence layer A = directly observed)

### Snyk Open Source

Key observations (all Tier 1, via docs.snyk.io doc query interface):

- Self-label: "a software composition analysis (SCA) solution. It helps you find and fix vulnerabilities in the open-source libraries used by your applications, and it can also detect license issues in (or caused by) those libraries."
- Inventory: scans a Project's dependencies "typically by analyzing manifest files (for example package-lock.json, pom.xml, go.mod)"; the CLI "builds a dependency tree including direct and transitive dependencies, and tracks where packages are introduced."
- Matching: "Snyk checks anywhere in that dependency tree using its vulnerability database."
- Findings: vulnerabilities (including "the path of introduction") and license issues ("comparing licenses against those known to Snyk"); license policy assigns severities; license issues display in the same workflows as vulnerabilities.
- Remediation: upgrade the dependency to a secure version; pin a package/version (including installing an indirect dependency as a top-level dependency); Snyk precision patch when no upgrade is available; fix PRs/MRs can be opened from the Issues view.
- Continuous monitoring: `snyk test` (point-in-time) then `snyk monitor` — "save a dependency snapshot in your snyk.io account and be alerted when new issues are found later in those dependencies"; monitoring tracks newly discovered issues against earlier snapshots.
- Governance: Snyk Policies automate security and license governance (rules that adjust issue severities and compliance requirements). CI: the Snyk Security Scan task can fail the pipeline or allow it to continue based on configuration.
- Surfaces: Web UI, IDE plugins, CLI, CI/CD, API.

### Sonatype Lifecycle (IQ)

Key observations (all Tier 1):

- Self-label: "the solution to identify open-source risks and secure your software supply chain. With Lifecycle, you create custom policies that are enforceable across all stages of your software development lifecycle (SDLC)."
- Policy engine framing (vendor's own): "a policy is a rule for how to act when certain constraints are met. In Lifecycle, a policy tells Lifecycle what to do when an aspect of a component meets a specified condition. Some example conditions are the component's age, the CVSS score of a discovered vulnerability, or the obligations from the component's license."
- Four risk categories: security, license (e.g. GPL public-disclosure obligation), quality (age, popularity), other (e.g. ownership).
- Policy actions: "warn the user, block/fail the build, or just record this information in a report"; each policy carries a threat score for cross-domain comparison; reference policies ship as a base template.
- SDLC enforcement stages: Proxy (Repository Firewall), Develop (IDE), Source (SCM), Build (CI), Stage release, Release, Operate, Compliance (SBOM Manager).
- Application model: applications organized in organizations; policy configuration, notifications, access controls inherited from the organization; Application ID is the external identifier scanners target; waivers inherited from org.
- Component identification: match states — Exact (SHA1 hash match against public repository), Unknown (unmatched: proprietary, modified, non-repository, or maliciously altered), Similar (resembles a known component with unexplained modifications — hardened forks, emergency patches, commercially supported builds), Embedded (constituent of an uber JAR). Identification source shown on Component Details Page; claiming components; proprietary component configuration.
- Report: Application Composition Report — "a point-in-time report detailing the policy violations affecting the use of open-source components found in your application."
- Continuous monitoring: "Continuous Monitoring always evaluates the latest scan for that application in the stage you select"; notifies only on new violations or changed violation details; email + webhook notifications.
- Remediation: "In most cases, the remediation path is to upgrade to a patched version"; resolution order: upgrade → migrate to a component without the violation → request a waiver (with justification: app, policy, CVE, why); work direct dependencies first, transitive last; Component Information Panel (CIP) in UI and IDE shows newer versions, most popular versions, security and licensing issues; automated pull requests (Go, Maven, npm, Gradle); legacy violations feature (pre-adoption backlog doesn't fail builds; new violations do); component labels; waivers.
- Prioritization: reachability analysis shipped in CI/CD integrations (Azure DevOps, Bamboo, GitHub Actions, GitLab CI, Jenkins, Sonatype CLI); dashboards; MTTR success metrics; Jira integration.

### Mend SCA

Key observations (all Tier 1):

- Self-label: "Mend SCA gives organizations full visibility and control over open source usage and security... It can issue real-time alerts with automatic remediation capabilities, or even proactively block malicious packages and licensing violations."
- Engine: "The Mend CLI Software Composition Analysis (SCA) engine performs an extensive analysis of the open source components within your application to detect CVE vulnerabilities as well as MSC vulnerabilities for malicious packages."
- Scan steps: Scanning (directory scanned "for SCA vulnerabilities and malicious packages"), Retrieving (vulnerability information fetched from the Mend Application for the summary).
- Platform model: applications/projects in the Mend AppSec Platform; findings views; Risk Factors column — for Dependencies: Exploitable, Reachable, Malicious.
- Reachability: "the Reachability Algorithm is engineered to assess whether a given vulnerability associated with an open-source library is reachable within the application's source code"; "We analyze imports in your application's source code to identify the classes being utilized, generating a comprehensive relationship graph of these classes and associated files"; only metadata (file/class names) uploaded, not source.
- Legacy SCA application (WhiteSource lineage) self-description: "View and analyze all the open-source libraries in an organization's projects for licenses and vulnerabilities"; "Mark libraries of non-open-source code as proprietary to remove them from further analysis"; "Assign copyrights, notices, and licenses to projects' open-source libraries"; "Enforce policies automatically throughout the SDLC and get real-time alerts on critical issues"; "Generate up-to-date reports... by maintaining a repository of open-source libraries or details about license approval processes."
- Surfaces: Mend CLI (`mend dep`), Unified Agent, repository integrations (GitHub/GitLab/Azure/Bitbucket), platform UI, API 3.0; sourceUrl/branch/commit tags bind scans to projects.

### OWASP Dependency-Track

Key observations (all Tier 1):

- Self-label: "an intelligent Component Analysis platform that allows organizations to identify and reduce risk in the software supply chain. Dependency-Track takes a unique and highly beneficial approach by leveraging the capabilities of Software Bill of Materials (SBOM). This approach provides capabilities that traditional Software Composition Analysis (SCA) solutions cannot achieve."
- Portfolio posture: "monitors component usage across all versions of every application in its portfolio in order to proactively identify risk across an organization."
- Inventory: consumes and produces CycloneDX SBOM (and VEX); BOMs published via REST API / Jenkins plugin / GitHub Action; projects identified by name+version or UUID, auto-creation supported.
- Analysis types (the product's own taxonomy): Known Vulnerability Analysis; Outdated Component Analysis; License Evaluation; Component Identity; Integrity Verification.
- Vulnerability matching: multiple analyzers — Internal (dictionary auto-populated from NVD, GitHub Advisories, OSV, VulnDB mirroring; CPE + PURL matching with NIST CPE-name-matching spec and custom false-positive reductions), OSS Index (Sonatype service), VulnDB, Snyk (REST, direct vulnerabilities per purl); analyzers independently enable/disable; datasource routing; private vulnerability repository for internal components.
- Triage: analysis states per finding — EXPLOITABLE / IN_TRIAGE / FALSE_POSITIVE / NOT_AFFECTED / NOT_SET; "Audit history is maintained for every finding including changes to analysis states" (user + timestamp appended).
- Policy engine: "global and per-project policies — security risk and compliance, license risk and compliance, operational risk and compliance."
- Continuous monitoring: "Dependency-Track continuously monitors components for known vulnerabilities... All components in Dependency-Track, regardless of changes, are automatically analyzed on a daily basis."
- Prioritization: EPSS (Exploit Prediction Scoring System) support; VEX consumption.
- License: SPDX license IDs tracked by component; license evaluation as a first-class analysis type.
- Ecosystem-agnostic: repository metadata support for Cargo, Composer, Gems, Hex, Maven, NPM, NuGet, PyPI; metrics per component/project/portfolio; notifications (Slack, Teams, Mattermost, webhooks, email, Jira); integrations with Kenna, Fortify SSC, ThreadFix, DefectDojo; API-first.

### GitHub (dependency graph + Dependabot + dependency review)

Key observations (all Tier 1):

- Dependency graph: "a summary of the manifest and lock files stored in a repository and any dependencies that are submitted for the repository using the dependency submission API." Per dependency: version, license information, the manifest file which included it, whether it has known vulnerabilities; for ecosystems with transitive dependencies, relationship status and "Show paths" to see the transitive path; dependents ("Used by") for public repos.
- Dependabot alerts: "Dependabot scans your repository's default branch and sends alerts when: A new vulnerability is added to the GitHub Advisory Database; Your dependency graph changes." Each alert includes "a link to the affected file, details about the vulnerability and its severity, information about a fixed version (when available)." Auto-triage rules (auto-dismiss low-risk); assignment to people/teams/AI agents (agents open draft fix PRs); notifications configurable.
- Dependabot security updates: "Dependabot can fix vulnerable dependencies for you by raising pull requests with security updates"; "raises a pull request to update the dependency to the minimum version that includes the patch and links the pull request to the Dependabot alert"; security updates trigger "only for dependencies that are specified in a manifest or lock file"; grouped security updates; compatibility scores (percentage of CI runs that passed when updating between specific versions, computed from CI tests in other public repositories).
- Dependabot version updates: a separate feature — scheduled PRs to keep dependencies at the latest version "even when they don't have any vulnerabilities" (dependabot.yml: package-ecosystem, directory, schedule.interval; allow/ignore; cooldown with a 3-day default for version updates, not security updates).
- Dependency review: PR-level "rich diff" on the Files Changed tab — "which dependencies were added, removed, or updated, along with the release dates; how many projects use these components; vulnerability data"; includes indirect dependencies changed in lock files. The dependency review action enforces in CI: "By default, the dependency review action check will fail if it discovers any vulnerable packages"; configurable severity thresholds and "allow or deny list for licenses"; can be a required check blocking merge; enforced org-wide via rulesets.
- SBOM export: "Export a software bill of materials (SBOM) for audit or compliance purposes... a formal, machine-readable inventory of a project's dependencies."
- Limitations (vendor-stated): alerts can't catch every security issue; new vulnerabilities take time to appear in the advisory database; only reviewed advisories trigger alerts; archived repos not scanned.

## Cross-product Comparison

| Dimension | Snyk | Sonatype Lifecycle | Mend SCA | Dependency-Track | GitHub |
|---|---|---|---|---|---|
| Analyzed subject | Project (repo) | Application (in org hierarchy) | Application/Project (platform) | Project (SBOM-published) | Repository |
| Inventory construction | manifest files → dependency tree (direct + transitive, introduction paths) | binary/manifest analysis via CLI/build/SCM tools; SHA1 match states | directory scan via CLI/Unified Agent/repo integrations | CycloneDX SBOM ingestion (+ production) | manifest + lock files + dependency submission API |
| Transitive coverage | explicit (dependency tree) | explicit (Embedded uber-JAR constituents) | explicit (dependency resolution per package manager) | explicit (SBOM carries full graph) | explicit (lock files; "Show paths") |
| Knowledge matched | Snyk vulnerability DB + licenses known to Snyk | Sonatype Intelligence (security/license/quality/malware) | Mend vulnerability DB (CVE + MSC malicious) | NVD/GitHub Advisories/OSV/OSS Index/Snyk/VulnDB + SPDX license data | GitHub Advisory Database + license info |
| Finding unit | issue (vulnerability/license) | policy violation (component × policy condition, threat level) | finding (vulnerability/malicious/license) with risk factors | finding (vulnerability/outdated/license) with analysis state | Dependabot alert (vulnerable dependency) |
| Finding carries | path of introduction, severity, fix options | component, violated policy, threat score, stage | severity, risk factors (reachable/exploitable/malicious) | advisory data, analysis state, audit trail | affected file, severity, fixed version |
| Remediation | upgrade / pin / precision patch; fix PRs | upgrade → migrate → waiver; automated PRs (Go/Maven/npm/Gradle) | fixed version options; automatic remediation alerts | advisory data + triage (no auto-fix in fetched docs) | auto-PR to minimum patched version (security updates) |
| Triage/suppression | issue states, ignore | waivers (justification), legacy violations, labels | platform triage | 5 analysis states + audit history | dismiss with reason, auto-triage rules, assignment |
| Continuous re-analysis | snyk monitor snapshots + alerts | continuous monitoring re-evaluates latest scan | real-time alerts | continuous; daily re-analysis of all components | alerts on new advisories + graph changes |
| Gates | CI task fail/continue | policy actions: warn / fail build / record; 8 SDLC stages | policies; block malicious packages | global/per-project policy engine | dependency review action as required check |
| License analysis | license issues vs license policy | license policies (obligations) | license violations; copyright/notices assignment (legacy) | License Evaluation analysis type; SPDX | license info in graph; license allow/deny in review action |
| SBOM | (not confirmed in fetched pages) | SBOM Manager sibling product on IQ Server | (not in fetched pages) | consumes AND produces CycloneDX | SBOM export |
| Reachability | prioritization features (Essentials) | reachability analysis in CI integrations | SCA Reachability (import analysis) | EPSS + VEX (exploit signals, not code-level) | compatibility scores (not code-level) |
| Portfolio layer | projects in account, dashboards | organizations → applications, dashboards, MTTR | applications/projects, dashboards | portfolio across all versions of every project | org-level dependency review dashboard |
| Delivery | SaaS (+ CLI/IDE/CI clients) | self-hosted IQ Server or SaaS | SaaS platform | self-hosted open source | platform-native (code hosting) |

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **The resolved third-party component inventory of an analyzed software unit.** The analyzed subject is an application/project/repository; the inventory is the population of external components it is composed of — direct and transitive — at their resolved versions. Remove → advisory feed, package listing, or a bare SBOM artifact.
2. **Matching the inventory against maintained external component knowledge.** The knowledge is about the components themselves — known vulnerabilities as the canonical class (advisory databases), with license obligations and other component risk as common extensions — and it is continuously updated by parties other than the analyzed software's authors. Remove → plain dependency listing (the package manager's own job) or a static audit.
3. **Per-component findings as the consumable output.** Each finding binds a risk to a specific component at a specific version inside the analyzed unit — identified, severitied, actionable by the owning team. Remove → raw data service or a score with no component binding.

Jointly-held load-bearing:

- 1 alone = dependency list / SBOM artifact (SBOM Management territory; package manager listing)
- 2 alone = advisory database (NVD-class)
- 3 alone = manual audit report
- 1+2 without 3 = matching pipeline with no consumable output
- 2+3 without 1 = advisory feed not bound to your software
- 1+3 without 2 = hand-maintained audit

### L1 — Common Mature Structure

- Remediation direction: fixed/secure version and upgrade path (Snyk fix options; Sonatype remediation plan; Mend fixed version options; GitHub fixed version + auto-PR; Dependency-Track via advisory data)
- Severity model (CVSS-based) + advisory identifiers (CVE/GHSA-class)
- Introduction/transitive path visibility (Snyk path of introduction; GitHub "Show paths"; Sonatype Embedded uber-JAR)
- Triage lifecycle with states and suppression/waivers with recorded reasons and audit trail (all five)
- Continuous re-analysis as advisories change (all five, in different machinery)
- CI/CD integration and policy gates (fail build / required check) (all five)
- License analysis: per-component license detection + license policies (all five in some form; Dependency-Track documents it as a distinct analysis type from vulnerability analysis — evidence it is separable, hence not definitional)
- Prioritization overlays: exploit signals (EPSS), reachability, risk factors, social trends (multiple products)
- Dev-workflow surfaces: CLI, IDE plugins, PR/MR annotations/comments, dashboards, reports/exports
- Organization/portfolio layer: applications/projects, org hierarchy, portfolio dashboards, metrics
- SBOM generation/export (GitHub export; Dependency-Track produces; Sonatype via sibling product)

### L2 — Variant / Optional Structure

- Inventory construction method: manifest/lockfile parsing vs binary/hash analysis vs SBOM ingestion vs build-time submission API
- Knowledge base posture: own curated commercial DB (Snyk/Sonatype/Mend) vs aggregator of public sources (Dependency-Track) vs platform-native advisory DB (GitHub)
- Knowledge classes beyond vulnerabilities: license obligations, malicious packages, component health/age/popularity/EOL, outdated-version analysis
- Auto-remediation: automated fix PRs vs advisory-only
- Delivery: SaaS vs self-hosted vs platform-embedded in code hosting
- Posture: standalone product vs module inside an AppSec platform vs feature of a hosting platform
- Policy enforcement depth: advisory vs blocking (proxy-stage blocking = Repository Firewall territory)
- Code-level reachability analysis (import/call analysis over first-party code to prioritize dependency findings)
- VEX/EPSS exploit intelligence consumption

### L3 — Vendor-specific (research notes only)

- Sonatype: match states (Exact/Unknown/Similar/Embedded), threat scores, 8 SDLC enforcement stages, legacy violations, Component Information Panel, claiming components, Innersource Insights, uber-JAR embedded detection, Repository Firewall proxy stage
- Snyk: precision patches, pin fixes, snyk monitor snapshots, fix PRs from Issues view
- Mend: Risk Factors column (Exploitable/Reachable/Malicious), Unified Agent, MSC malicious-package vulnerability class, sourceUrl/branch/commit scan tags, metadata-only reachability upload
- Dependency-Track: CycloneDX-native consumption/production, 5-state analysis vocabulary, internal analyzer dictionary, datasource routing, private vulnerability repository, collection projects, daily full re-analysis
- GitHub: Dependabot alerts/security-updates/version-updates triad, dependency review action, compatibility scores, auto-triage rules, dependency submission API, "Used by" dependents data, 3-day default cooldown on version updates

## Vendor-specific Findings

- Sonatype is the only sampled product whose component identification is hash-based against public repositories with explicit match states for modified/unknown components; the others identify from manifests/lockfiles/SBOMs. Identification method is a variant axis, not definitional.
- GitHub is the only sampled product where the analysis is a free feature of the code-hosting platform itself and where the advisory database is also the matching source (platform-native loop).
- Dependency-Track is the only sampled product that takes the SBOM (not the source tree) as the primary input — and it explicitly frames this as "capabilities that traditional SCA solutions cannot achieve" (portfolio-wide component usage across all versions).
- Mend's legacy application documents copyright/notices assignment — the deepest license-compliance machinery in the sample; license depth is a variant axis.
- Precise vendor numbers (e.g. Dependabot's 3-day default cooldown, Dependency-Track's daily re-analysis cadence) are kept in research notes only.

## Boundary Findings

- **vs SAST (§15, processed)** — DISCHARGES the SAST pass's forward flag from this side: keep-both RATIFIED on the first-party vs dependency seam. SAST analyzes the application's own code (source or compiled form); SCA analyzes the third-party components the application is composed of. Vendor-documented at every suite in both passes: Semgrep Code vs Supply Chain; Veracode Static vs SCA; Checkmarx SAST vs SCA scanners; GitLab SAST vs Dependency Scanning; Mend SCA vs Mend SAST as separate products in one platform. Overlap zone: SCA reachability analysis reads first-party code (imports, class usage) — but the object of the finding remains the component, not a code location; the code reading is prioritization machinery.
- **vs SBOM Management (§15, unprocessed)** — the artifact vs the analysis. SBOM Management's unit of record is the SBOM (machine-readable component inventory: formats, generation, distribution, compliance consumption); SCA's unit is the analyzed application's component population plus the matching→findings loop. Overlap: SCA tools generate/export SBOMs (GitHub export, Dependency-Track produces CycloneDX); SBOM-centric platforms run vulnerability matching (Dependency-Track self-describes as an SCA-adjacent "Component Analysis platform" whose SBOM approach yields "capabilities that traditional SCA solutions cannot achieve"). Dependency-Track straddles the seam — flag for the SBOM Management pass: proposed seam is artifact-of-record + sharing/compliance workflow vs analysis loop over the composition; products converge when the SBOM is the substrate.
- **vs Vulnerability Management (§15, unprocessed)** — SCA produces component-level findings inside the development pipeline; VM owns the org-wide vulnerability lifecycle across asset types (infrastructure, endpoints, applications). Hand-off documented: Dependency-Track integrates Kenna/Fortify SSC/ThreadFix/DefectDojo; Sonatype integrates Jira. SCA findings are an input to VM, not the same Type.
- **vs Software Supply Chain Security (§15, unprocessed)** — SCA is the analysis core over the composition; SSCS is the broader program (build integrity, provenance/attestation, CI/CD security, ingestion blocking). Sonatype's own portfolio draws the line: Repository Firewall (blocks at the proxy stage) vs Lifecycle (analyzes applications). Malicious-package detection appears on both sides (Mend SCA detects MSC malicious packages; Sonatype malware data) — the seam is where the concern lives: inside composition analysis vs the whole supply-chain program. Flag for that pass.
- **vs Dependency Management Application (§12, unprocessed)** — risk-oriented analysis vs version-currency maintenance. GitHub's own documentation separates "Dependabot security updates" (driven by known vulnerabilities; alerts → fix PRs) from "Dependabot version updates" (driven by new version availability; scheduled PRs) — a vendor-documented seam inside one product family. The driver (advisory vs release) and the consuming workflow (security vs developer maintenance) decide the Type. Flag for that pass.
- **vs Package Registry (§12, processed)** — the venue components are published to and fetched from vs the analysis of compositions. Sonatype's portfolio pairs them (Nexus Repository + Lifecycle on one IQ Server); the registry pass's own core (catalog + publication path + resolution path) contains no matching-against-advisories loop. Different Types; adjacent in the same workflow.
- **vs Static Code Analysis Platform (§12, unprocessed)** — SCA findings bind to components, not code locations; static code analysis findings bind to code locations. Different output units and different knowledge (advisories vs rules). Reachability overlays blur the surface but not the finding object.
- **vs Application Security Platform (§15, processed)** — same engine-vs-program seam that pass recorded for SAST: SCA engines/scanners ship as modules inside AppSec platforms (Mend SCA inside Mend Platform; Checkmarx SCA scanner; Veracode SCA). SCA documents the analysis capability; the platform documents application records + finding lifecycle + policy/gates + portfolio management.

## Historical / Market-Sample Check

Would older, regional, platform-native, or differently positioned products still fit the L0?

- Package-manager-native audit commands (npm audit / bundler-audit class): scan the resolved dependency tree, match against an advisory database, report vulnerable components with suggested fixes — no license analysis, no policy engine, no platform, no continuous monitoring. They satisfy all three L0 legs. → license analysis, policy gates, platform machinery, and continuous monitoring are all L1, not definitional. (Held as a class from general knowledge, not from a fetched source — used only for the historical check, no specific claims.)
- Early license-audit generation (early-2000s open-source governance tools: component + license discovery, license bills, approval workflows): satisfies legs 1 and 3 but lacks the vulnerability-matching class of leg 2. Held as conceptual ancestors of the Type's license-analysis capability (L1), not as the defining core — consistent with the directory placing SCA in the cybersecurity section and with every product self-labeled "SCA" today carrying vulnerability matching.
- SBOM-centric realization (Dependency-Track) satisfies L0 — SBOM ingestion is a variant of inventory construction.
- Platform-native realization (GitHub) satisfies L0 — delivery surface is a variant.
- Self-hosted open-source (Dependency-Track), SaaS (Snyk/Mend), self-hosted commercial (Sonatype IQ) all satisfy — delivery is a variant axis.
- Conclusion: L0 holds across eras and delivery forms; no era machinery (cloud, CI, SBOM formats, CVSS, auto-PR, AI) is definitional.

## Uncertainties

- Black Duck official documentation unreachable (JS-only app; product site 404 ×2) — the enterprise audit-grade classic is held as market context only; no claims rest on it. Its license-compliance depth is asserted nowhere in the final document.
- Snyk SBOM generation and Mend SBOM output were not confirmed from fetched pages — SBOM generation is held as L1 "present in part of the sample", not universal.
- Whether "policy gate" is universal: all five sampled products have some gate/policy surface, but the minimal audit-command class does not — held L1, not L0.
- Reachability analysis depth varies (code-level import analysis at Mend/Sonatype integrations vs exploit-signal overlays at Dependency-Track/GitHub) — held L2 for the code-level form, L1 for prioritization overlays generally.
- Exact triage-state vocabularies differ per product; the final document uses conceptual states, not vendor labels.
- Veracode SCA / Checkmarx SCA / Semgrep Supply Chain were not re-fetched this pass (their SAST-vs-SCA split evidence comes from the SAST pass's fetches); no product-specific claims about them are made here beyond the seam they document.

## Final Synthesis

SCA is the analysis capability that turns an application's third-party component population into a set of actionable risk findings: it resolves what the software is actually composed of (direct and transitive, at pinned versions), matches that inventory against continuously maintained knowledge about the components themselves (known vulnerabilities as the canonical class, license obligations the other long-standing class), and binds every finding to a specific component at a specific version inside the analyzed unit. The defining core is exactly the three legs above; everything else — remediation guidance, triage/waivers, continuous re-analysis, CI gates, license machinery, SBOM export, reachability overlays, auto-fix PRs — is mature market structure layered on that core. The inventory-construction method (manifests vs binary hashes vs SBOMs vs build-time submission), the knowledge-base posture (curated vs aggregated vs platform-native), and the delivery form (SaaS vs self-hosted vs platform-embedded) are variant axes. The Type sits between first-party code analysis (SAST — different object), the SBOM artifact world (inventory of record without the analysis loop), and the broader supply-chain program (integrity/provenance/ingestion control), and it feeds findings into vulnerability management rather than owning the org-wide lifecycle.
