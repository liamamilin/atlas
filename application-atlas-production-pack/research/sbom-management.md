# Research Notes — SBOM Management

## Research Goal

Understand what an SBOM Management application really is, from real products: what objects exist inside it, how SBOMs enter the system, what "management" means operationally, who uses it, and where its boundaries lie against Software Composition Analysis (SCA), Dependency Management, Artifact Repository, and Vulnerability Management.

## Initial Boundary

Working hypothesis before research:

- Core purpose: produce, hold, and operate machine-readable software component inventories (SBOMs) for software products/releases.
- Likely users: application security teams, compliance teams, software suppliers, engineering/DevOps.
- Nearest neighbors: SCA (risk analysis of dependencies), Dependency Management (project-side version selection), Artifact Repository (custody of build outputs), Vulnerability Management (findings workflow), Software Supply Chain Security (umbrella).
- Expected confusion: many SCA products also generate SBOMs; the boundary is whether the SBOM as a retained, operated record is the center.

## Research Questions

1. What is the central managed object — the SBOM file, the component, the product, or the release?
2. How do SBOMs enter the system: generated internally, imported from external generators, or collected from suppliers?
3. What happens to an SBOM after ingestion (validation, parsing, enrichment, re-analysis)?
4. How are SBOMs organized (product/version hierarchies) and what is the unit of aggregation?
5. What analysis layers operate on the inventory (vulnerabilities, licenses, policy, quality)?
6. How are SBOMs delivered onward (export, distribution to customers/regulators)?
7. What roles/permissions exist?
8. Where exactly is the seam to SCA, Dependency Management, and Artifact Repository?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

1. **OWASP Dependency-Track** — open-source, SBOM-centric component-analysis platform; the archetype of "SBOM as the primary object". Self-hosted.
2. **Anchore Enterprise** — commercial "SBOM-powered" platform with a dedicated SBOM Management framework (App → App Version → Asset); container-centric heritage.
3. **Sonatype SBOM Manager** — a distinct product inside the Sonatype platform, separated by the vendor itself from its SCA product (Lifecycle); compliance/VEX/distribution-oriented.
4. **Interlynk** — pure-play SBOM management SaaS (no SCA suite around it); proves the Type stands alone; supplier-collection posture.

Deliberately not sampled (source-access limitation): Mend, Snyk, Black Duck — SCA-first vendors whose SBOM features are documented behind pages not reachable in this pass; sbomify (transport error). No claims about them are made below.

## Sources

Research date: 2026-09-09. All Tier 1 (official operational documentation):

- Dependency-Track — https://docs.dependencytrack.org/ (Introduction); https://docs.dependencytrack.org/terminology/ ; https://docs.dependencytrack.org/usage/cicd/
- Anchore Enterprise — https://docs.anchore.com/current/docs/ ; https://docs.anchore.com/current/docs/sbom_management/how_it_works/
- Sonatype SBOM Manager — https://help.sonatype.com/en/sonatype-sbom-manager.html (product overview page; full section nav: Getting Started, SBOM, Dashboard/Organizations/Applications/Advanced Search/Legal views, API, Importing SBOMs, Bill of Material View, Component Details View, Continuous Monitoring, VEX Workflow)
- Interlynk — https://docs.interlynk.io/ ; https://docs.interlynk.io/interlynk-core-concepts/core-concepts.md

## Product Observations

### OWASP Dependency-Track

Evidence layer: A (directly observed, official docs).

- Self-description: "an intelligent Component Analysis platform that allows organizations to identify and reduce risk in the software supply chain. Dependency-Track takes a unique and highly beneficial approach by leveraging the capabilities of Software Bill of Materials (SBOM). This approach provides capabilities that traditional Software Composition Analysis (SCA) solutions cannot achieve." (vendor's own SCA-vs-SBOM framing)
- Core objects (Terminology page): **Project** ("high-level categorization and collection of components... along with sub projects. A project could represent a software application, an environment, a medical or IoT device, or an automobile"), **Component** ("a standalone entity... open source component, third-party library, first-party library, an operating system, or a hardware device"), **Dependency** ("a project that includes a component"), **Portfolio** ("the sum total of all projects defined in the system"), **BOM** ("contents of all components bundled with the software including authors, publishers, names, versions, licenses, and copyrights").
- Ingest: consumes and produces CycloneDX SBOM; consumes and produces CycloneDX VEX. BOM generation "often occur[s] during CI" using external tools (CycloneDX Tool Center referenced); publishing via Jenkins plugin, GitHub Action, or raw API calls (API key + project UUID; `autoCreate` option; parent/child project hierarchy via `parentUUID`/`parentName`).
- Processing: "When components are added or updated... an analysis is performed against the component. This action occurs during ingestion... All components... are automatically analyzed on a daily basis." (continuous re-analysis)
- Analysis types: known vulnerabilities (multiple intel sources: NVD, GitHub Advisories, OSV, OSS Index, Snyk, Trivy, VulnDB), outdated component analysis, license evaluation (SPDX license IDs), component identity, integrity verification.
- Policy engine: global and per-project policies (security/license/operational risk and compliance).
- Auditing workflow: triage of findings with analysis states and suppression; "audit trail that captures the thought process and decisions made for each finding".
- Risk rollup: "Vulnerabilities from dependent components and sub projects are reported up to the project level. This is called inherited risk."
- Component scope: applications, libraries, frameworks, operating systems, containers, firmware, files, hardware, services.
- API-first design; OpenAPI documentation; OIDC/LDAP/API-key auth; teams with API keys.
- Dedicated "U.S. Executive Order 14028" usage page (regulatory context).

### Anchore Enterprise

Evidence layer: A (directly observed, official docs).

- Self-description: "an SBOM-powered (Software Bill of Materials) solution that enables continuous analysis of applications... embedding automation into development toolchains to generate SBOMs and accurately identify vulnerabilities, malware, misconfigurations, and secrets."
- Dedicated documentation section "SBOM Management": How It Works; Apps, Versions and Assets; Generate SBOMs; View Contents; Export; Search.
- Core model: three-level hierarchy — **App** ("the top-level entity representing a piece of software you ship or host"; name, description, contact, optional default policy), **App Version** ("a point-in-time release of an app"; name typically semver/release tag; optional reference to previous version; release date; status `in_progress`/`released`/`eol`), **Asset** ("a concrete thing that was analyzed and whose SBOM lives inside an app version": container image, filesystem analysis, or externally supplied Syft/CycloneDX/SPDX document).
- "The app version is the unit of aggregation: when Anchore Enterprise reports the packages, vulnerabilities, or policy status of 'a release,' it is summarizing across the assets attached to a version."
- Asset types: `container`, `filesystem`, plus CycloneDX-taxonomy types `application`, `library`, `module`, `file`, `firmware`, `device`, `virtual_machine_disk`, `unknown`.
- Asset lifecycle: asynchronous **jobs** — `pending` → `processing` → `complete` / `failed` / `cancelled`; job analyzes artifact and generates SBOM (or takes uploaded SBOM), processes contents, attaches asset to app version.
- Two generation postures: **centralized analysis** (platform pulls image from registry, analyzes server-side) and **distributed analysis** (CLI generates SBOM locally, uploads result; "Anchore Enterprise never sees the image bytes" — for air-gapped/sensitive pipelines).
- Formats: uploads validated for schema correctness; CycloneDX 1.2–1.7 (JSON/XML), SPDX 2.2–2.3 (JSON/tag-value), SPDX 3.0, Syft native.
- Unified data queries across an app version: list packages, list vulnerabilities, find assets containing a given package, find packages affected by a vulnerability — "they let you answer 'which images in this release contain openssl 3.0.13?' with one request."
- Vulnerability rescans "run on a periodic schedule against the existing asset inventory as new vulnerability data lands".
- Compliance Management section separate: policy gates/packs (FedRAMP, NIST SSDF, CIS, PCI DSS...), **SBOM Drift** analysis.
- Security Analysis and Reporting section separate from SBOM Management (annotations and VEX under vulnerability management).
- Account scoping (per-account isolation, `x-anchore-account` header), RBAC with user groups, SSO (SAML via Okta/Entra/KeyCloak), API keys; REST + GraphQL APIs; AnchoreCTL CLI.

### Sonatype SBOM Manager

Evidence layer: A (directly observed, official docs).

- A distinct product in the Sonatype platform, documented as its own section ("Sonatype SBOM Manager") separate from Sonatype Lifecycle (the SCA product); the help site even carries a comparison page "CPE Matching Experience in SBOM Manager vs. Lifecycle" — vendor-maintained separation of the two products.
- Product page value claims: "Become and remain compliant — Ensure adherence to regulations and standards with automated SBOM generation and reporting"; "Streamlined VEX workflow — Add vulnerability details (VEX)... to each SBOM".
- The vendor's own functional decomposition (product overview page):
  - **Ingest** — "import both CycloneDX and SPDX formats using various component identifiers while retaining the original SBOMs for compliance. VEX information may be imported and automatically produced using Sonatype data."
  - **Analyze** — "Complete component intelligence across all supported ecosystems. SBOM-centric metrics and trends to track progress toward policy goals."
  - **Store** — "Provide original SBOM and any augmented SBOMs by application version."
  - **Catalog** — "Check whether third-party applications and libraries comply with your organization's compliance and security policies."
  - **Search** — "locate components, vulnerabilities, and policy violations across your portfolio. Reduce response time to incidents by searching through your SBOM database to find any compromised components."
  - **Audit** — compliance rules; "Create rules to scale and automate the VEX process."
  - **Continuously Monitor** — "monitor SBOMs for new information about components; provide notifications/alerts based on monitoring."
  - **VEX Workflow** — "Manage a full VEX-based SBOM Release Workflow. Embed VEX information in your SBOMs to explain vulnerabilities."
  - **Distribute** — "Share or send SBOMs as pdfs and data files. Share SBOMs with your customers, regulators, and certification bodies."
- Documentation section structure (nav): Dashboard View, Organizations View, Applications View, Advanced Search View, Legal View, SBOM Manager API, Importing SBOMs, SBOM Bill of Material View, SBOM Component Details View, SBOM Continuous Monitoring, SBOM VEX Workflow.

### Interlynk

Evidence layer: A (directly observed, official docs).

- Self-description: "a platform for automating software supply chain security. It uses Software Bill of Materials (SBOM) and Vulnerability Exploitability eXchange (VEX) as base artifacts for managing and eliminating software supply chain risks."
- Capabilities: Generate SBOMs (lynkctl CLI from build systems/package manifests); **Manage SBOMs** — "Request and collect SBOMs from first-party build pipelines or third-party suppliers"; monitor vulnerabilities; enforce policies; prioritize remediation; meet compliance (open-source license and SBOM compliance obligations).
- Core model (Core Concepts page): `Organization → Product → Environment → Version (SBOM) → Components → Vulnerabilities`, with **Parts** ("references to other Product Versions that are embedded or bundled alongside the primary SBOM" — embedded sub-SBOMs).
- **Version** = "a point-in-time snapshot of the software's composition"; "Each Version is an immutable record of the software's composition at upload time."
- Environments reflect deployment stages (e.g., Development, Production); vulnerability data does not merge across Environments.
- Processing pipeline on upload: 1. SBOM Checks (quality, completeness) → 2. Internal Component Labeling → 3. Automation Rules execution → 4. Vulnerability Scanning → 5. Component Support Analysis → 6. Policy Evaluation. "After processing completes, the Version and its Components are available for querying, reporting, and compliance evaluation."
- Vulnerability mapping "using package identifiers (PURL, CPE) and vulnerability databases".
- Isolation boundaries: Organization (tenant), Product (independent policies/labels), Environment (independent settings/history), Version (immutable).
- Administration: user management, roles, SSO, integrations (GitHub, GitLab, Jira, Slack).
- Productivity tools: sbomqs (SBOM quality scoring), sbomasm (SBOM assembly/manipulation), pylynk, lynk-mcp.

## Cross-product Comparison

| Dimension | Dependency-Track | Anchore Enterprise | Sonatype SBOM Manager | Interlynk |
|---|---|---|---|---|
| Self-positioning | Component-analysis platform that "leverage[s] SBOM"; explicitly contrasted with traditional SCA | "SBOM-powered solution"; SBOM Management is a named framework | Standalone SBOM product, vendor-separated from its SCA product (Lifecycle) | Supply-chain automation platform with "SBOM and VEX as base artifacts" |
| Product container | Project (+ sub-projects) | App | Application | Product |
| Release/version object | Project version | App Version (in_progress / released / eol) | Application version | Version (immutable snapshot) |
| SBOM record | BOM ingested per project | Asset (SBOM attached to app version) | Original + augmented SBOMs per application version | Version (SBOM) + Parts (embedded sub-SBOMs) |
| Acquisition | Import only (external generators via CI plugins/API) | Both: internal generation (centralized or CLI-distributed) and import | Import (CycloneDX + SPDX) + "automated SBOM generation" | Both: lynkctl generation and upload; supplier collection |
| Ingest processing | Analysis at ingestion + daily re-analysis | Schema validation; async job pipeline (pending→processing→complete/failed/cancelled) | Ingest with identifier handling; originals retained | Quality/completeness checks → labeling → automation rules → vuln scan → support analysis → policy evaluation |
| Analysis layers | Known vulns, outdated, license, identity, integrity | Packages, vulnerabilities, policy | Component intelligence, metrics/trends, policy violations | Vulnerabilities, licenses, policies, quality |
| Portfolio query | Portfolio-wide ("identify what is affected, and where") | Unified queries across app version (assets-by-package, packages-by-vulnerability) | Search components/vulns/policy violations across portfolio; find compromised components | Analytics across portfolio |
| VEX | Consumes and produces | Annotations and VEX (under vuln management) | VEX workflow; embed VEX in SBOMs | VEX as base artifact |
| Distribution | API, badges, notifications | Export | Distribute as PDFs/data files to customers, regulators, certification bodies | (inbound supplier collection is the emphasized direction) |
| Policy engine | Global + per-project (security/license/operational) | Gates + packs (FedRAMP, NIST, CIS, PCI...) | Compliance policies, audit rules | Policies per product/org |
| Tenancy/access | Teams, API keys, LDAP/OIDC | Accounts, RBAC, SSO | Organizations view | Organization tenant, roles, SSO |
| Component scope | Apps, libraries, frameworks, OS, containers, firmware, files, hardware, services | Container, filesystem, application, library, module, file, firmware, device, VM disk | Third-party applications and libraries | Libraries, packages, modules |
| Deployment | Self-hosted OSS | Self-hosted + cloud image | Part of Sonatype platform (SaaS/self-hosted) | SaaS |

## Canonical Abstraction

### L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being SBOM Management:

1. **The SBOM as a managed record of record** — a persistent, individually identified, machine-readable component inventory in a standard interchange format (CycloneDX/SPDX-class), held as a first-class object: retained (originals preserved), attached to a specific software artifact, re-usable by other processes. Remove → transient scan output (SCA territory) or a one-shot generator.
2. **The product-and-release binding** — SBOMs are organized under identified software products and their versions; the release/version is the unit of aggregation and the anchor for all component, vulnerability, and policy data. Remove → a component database or package catalog with no product binding.
3. **The managed SBOM lifecycle** — the system acquires SBOMs (by generating them and/or importing externally produced ones), processes them into queryable component data, and serves the inventory onward: portfolio-wide query/analysis and delivery of SBOMs to consumers. Remove the acquisition+processing+service loop → a static document archive; remove the record → generic component intelligence.

Jointly load-bearing checks:
- 1 alone = SBOM file store / generator tooling
- 2 alone = product catalog with attachments
- 3 without 1+2 = generic document processing
- 1+2 without 3 = static SBOM archive (the "management" gone)
- 1+3 without 2 = component intelligence platform without product binding (drifts toward SCA/component DB)
- 2+3 without 1 = portfolio tool with no SBOM records

### L1 — Common Mature Structure

Present in essentially all mature products, but not required to recognize the Type:

- Vulnerability matching against advisory feeds (4/4 in-sample — but see anti-overfit note below)
- License inventory and license-compliance evaluation
- Policy evaluation (security/license/operational rules) against the inventory
- Continuous re-evaluation: periodic rescans as new vulnerability/intelligence data arrives
- VEX support (consume and/or produce exploitability statements; VEX-embedded SBOM release workflows)
- Portfolio-wide search: "where is component X used", "which releases contain Y"
- Portfolio dashboards, metrics, trends
- API-first operation + CI/CD integration (plugins, CLI, upload endpoints)
- Notifications (Slack/Teams/email/Jira/webhook-class)
- RBAC / multi-tenancy / SSO

### L2 — Variant / Optional Structure

- Format posture: CycloneDX-first (Dependency-Track) vs dual CycloneDX+SPDX (Anchore, Sonatype, Interlynk) vs native formats (Syft)
- Generation posture: import-only (Dependency-Track in-type proof) vs internal generation (centralized server-side vs distributed CLI-local — Anchore documents both) vs both
- Audience posture: producer-side (ship your own SBOMs) vs consumer-side (request/collect supplier SBOMs — Interlynk explicit; Sonatype "Catalog" third-party check) vs both
- Component scope: software libraries only vs extended to containers, firmware, OS, hardware, devices, services (Dependency-Track, Anchore)
- Embedded composition: sub-SBOMs / Parts referencing other product versions (Interlynk); parent/child projects (Dependency-Track)
- Regulatory context: US EO 14028 (Dependency-Track dedicated page), EU CRA (Anchore quickstart), FedRAMP/NIST/PCI policy packs (Anchore)
- SBOM quality scoring (Interlynk sbomqs; quality checks in pipeline)
- Drift analysis between SBOM versions (Anchore SBOM Drift)
- Distribution formats: PDF + data files (Sonatype)
- Deployment: OSS self-hosted / commercial self-hosted / SaaS

### L3 — Vendor-specific (Research Notes only)

- Dependency-Track: EPSS prioritization support; private vulnerability repository; internal components datasource; datasource routing; SVG badges; risk-score formula ((critical*10)+(high*5)+(medium*3)+(low*1)+(unassigned*5)); daily automatic re-analysis cadence.
- Anchore: exact asset-type taxonomy (`virtual_machine_disk` etc.); job state names; `x-anchore-account` header; pagination default/max 1000; "tuned for releases of up to roughly 10,000 assets"; GraphQL reports API; AnchoreCTL `--wait` flag.
- Sonatype: "CPE Matching Experience in SBOM Manager vs. Lifecycle" comparison page; Advanced Legal Pack; VEX auto-production from Sonatype data.
- Interlynk: lynkctl/pylynk/lynk-mcp/sbomqs/sbomasm tool family; Environment-level vulnerability-data isolation.

### Anti-overfit Notes

- **Vulnerability matching is 4/4 in-sample but NOT definitional.** Per the shared-implementation rule, universal presence in the sampled market does not make it part of the definition: a compliance-oriented SBOM manager that only generates, retains, and distributes SBOMs (license/quality focus, no vuln matching) would still be recognized as this Type. Vulnerability/license/policy analysis is the analysis layer that mature products add on top of the inventory — the inventory record is the defining object. Supporting signal: Anchore's own docs split "SBOM Management" from "Security Analysis and Reporting"; Sonatype ships SBOM Manager separately from Lifecycle (SCA).
- **Standard format IS part of the record concept** (an SBOM is by definition a standard-format inventory — that is what distinguishes it from a proprietary component list), but *which* standard (CycloneDX vs SPDX vs native) is a variant axis.
- **Generation is not definitional; acquisition is.** Dependency-Track proves import-only is in-type; Anchore proves generate-internal is in-type. The invariant is that the system acquires SBOMs, by either or both paths.
- **Continuous monitoring is not definitional** — the minimal lifecycle (acquire → process → serve) satisfies the Type; continuous re-evaluation is the mature-market layer.

### Historical / Market-Sample Check

The Type is young (SBOM practice mainstreamed after US EO 14028, 2021; SPDX/CycloneDX matured through the late 2010s). The earliest recognizable form — generate an SBOM at build, retain it per release, parse it for component data, provide it on request — satisfies all three L0 legs with no continuous monitoring, no policy engine, no VEX. The check passes: the definition is not over-fitted to the current regulatory-driven feature set. Platform-native SBOM generation (registry- or platform-embedded SBOM output) is a generator, not a manager, unless the output is retained and operated as a record.

## Vendor-specific / Rejected Findings

Rejected from the canonical core (vendor-specific or over-fit):

- Specific job-state vocabularies (Anchore's pending/processing/complete/failed/cancelled) — implementation detail.
- Exact supported format version matrices (Anchore's CycloneDX 1.2–1.7 etc.) — product-specific; only the multi-format principle generalizes.
- Daily re-analysis cadence (Dependency-Track) — one product's scheduling; the generalizable claim is "periodic re-evaluation as intelligence updates".
- PDF distribution (Sonatype) — one product's documented delivery format.
- EPSS, private vulnerability repos, SVG badges (Dependency-Track) — vendor-specific modules.
- sbomqs quality scoring (Interlynk) — product-specific tooling.
- "CPE matching experience" differences (Sonatype) — vendor-internal product comparison.

## Boundary Findings

- **vs Software Composition Analysis (SCA)** — the closest and most important seam. SCA analyzes code/dependencies for risk and produces findings; SBOM management holds and operates the inventory record. Evidence of the vendor-recognized split: Dependency-Track's own framing ("capabilities that traditional SCA solutions cannot achieve"); Sonatype ships SBOM Manager as a separate product from Lifecycle with its own comparison page; Anchore's docs separate "SBOM Management" from "Security Analysis and Reporting". Integration seam: SCA tools commonly export SBOMs; SBOM managers commonly import them and may run their own matching. Remove the retained record (keep scanning) → SCA.
- **vs Dependency Management Application** — dependency management maintains the project-side working state (manifests, lockfiles, version selection, update proposals); SBOM management records what a shipped artifact is composed of (release-side record of record). Different primary consumers (developers vs security/compliance) and lifecycles. The dependency-management pass independently recorded this seam ("An SBOM is a compliance-oriented inventory record derived from dependency states").
- **vs Artifact Repository** — custodies build artifacts/binaries; an SBOM may be stored there as a file, but the repository does not parse, aggregate, or operate it. SBOM management custodies records *about* composition, not the artifacts themselves.
- **vs Vulnerability Management** — VM runs the findings/remediation workflow across the estate; SBOM management's vulnerability matching is component-level intelligence attached to the inventory. (VM leaf not yet processed in the atlas — seam to be confirmed from that side.)
- **vs Software Supply Chain Security** — umbrella Type (SCA + signing + CI/CD security + SBOM); SBOM management is one artifact family within it.
- **vs Cyber/IT Asset Management** — asset management tracks deployed instances in the estate; SBOM management tracks the composition of software products, not where instances run.
- **"去掉什么就变成另一个 Type" judgments**: remove the retained SBOM record → SCA; remove the product/release binding → component intelligence database; remove the operate loop → document archive; remove the standard-format requirement → proprietary component catalog (not SBOM); remove the software domain → physical-goods BOM (PLM territory).

## Uncertainties

- Mend, Snyk, Black Duck SBOM capabilities were not directly observed (pages unreachable in this pass); no claims made about them. The "SCA-first vendor ships a separate SBOM product" pattern is evidenced by Sonatype only — marked accordingly.
- sbomify (pure-play tier) unreachable; the pure-play pole is evidenced by Interlynk alone.
- SWID tag support across sampled products: not verified; not claimed.
- Dependency-Track's exact supported CycloneDX version range: not fetched; not stated.
- Whether distribution/consumption portals for SBOM recipients (self-service download portals) are common across the market: Sonatype documents distribution; Anchore documents export; Interlynk emphasizes inbound collection. A recipient-facing portal pattern is plausible but unverified — not claimed.
- Exact relationship to Vulnerability Management leaf to be confirmed when that leaf is processed.

## Final Synthesis

SBOM Management is the organization's system of record for software composition inventories. Its defining core is three jointly-held structures: (1) the SBOM as a managed, retained, standard-format machine-readable record of what a software artifact contains; (2) the binding of those records to identified software products and their versions, with the release as the unit of aggregation; (3) the managed lifecycle that acquires SBOMs (generated and/or imported), processes them into queryable component data, and serves the inventory onward — portfolio-wide query and analysis, and delivery of SBOMs to the consumers who need them (customers, regulators, auditors, downstream teams). Mature products add the analysis layer (vulnerability matching, license evaluation, policy evaluation, continuous re-evaluation, VEX), but the inventory record — not the analysis — is what defines the Type. The vendor market itself confirms the seam: SCA vendors ship SBOM management as distinct products or distinct product sections, and the open-source archetype defines itself through what "traditional SCA solutions cannot achieve" — operating the SBOM as a first-class, portfolio-wide record.
